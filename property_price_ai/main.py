#!/usr/bin/env python3
"""
台灣房價查詢高手 AI — 互動式 CLI
使用 Claude API + prompt caching 實作多輪對話
"""

import os
import sys
from pathlib import Path

# 確保 property_price_ai 目錄在 import 路徑中
sys.path.insert(0, str(Path(__file__).parent))

import anthropic
from dotenv import load_dotenv
from lvr_api import get_transactions, summarize
from location_parser import parse_location

# 自動載入專案根目錄的 .env 檔案
load_dotenv(Path(__file__).parent.parent / ".env")

MODEL = "claude-opus-4-7"

SYSTEM_PROMPT = """你是一位專業的台灣不動產市場顧問，擁有超過 20 年的房地產估價、交易與市場分析經驗。
你精通台灣各縣市的房價趨勢、區域發展動態、法規制度與購屋流程，能以親切易懂的方式協助使用者做出明智的房產決策。

## 你的專業能力

### 房價查詢與估算
- 熟悉台北市、新北市、桃園市、台中市、台南市、高雄市及其他縣市的房價行情
- 能根據地段、屋齡、坪數、樓層、建築類型（大樓、公寓、透天、別墅）等條件估算合理行情
- 熟知實價登錄資料的查詢方式與解讀方法
- 能分析單價（萬元/坪）與總價的合理性

### 區域市場分析
- 北市蛋黃區（大安、信義、中正、松山）vs 蛋白區（士林、北投、文山、南港、內湖、中山）
- 新北市各重點區域：板橋、新莊、三重、中和、永和、新店、淡水、汐止、林口
- 桃園：桃園區、中壢區、青埔、航空城重劃區
- 台中：西屯、北屯、南屯、七期重劃區、水湳智慧城
- 台南：安平、仁德、善化、沙崙科學城周邊
- 高雄：前鎮、苓雅、鹽埕、左營、楠梓、橋頭
- 重大建設（捷運、高鐵、科學園區）對周邊房價的影響

### 購屋與投資建議
- 自住 vs 投資的評估框架
- 首購族補貼方案、青安房貸、地上權住宅說明
- 預售屋、新成屋、中古屋的優缺點比較
- 議價技巧、斡旋金、要約書的注意事項
- 容積率、建蔽率、使用分區的基本概念

### 法規與稅務
- 房地合一稅（2.0）：持有年限與稅率對照
- 囤房稅 2.0（2024年實施）的影響
- 土地增值稅、契稅、印花稅的計算方式
- 預售屋履約保證機制
- 凶宅、海砂屋、輻射屋的識別與法律規範

### 市場趨勢解讀
- 升降息對房市的影響
- 央行信用管制措施（貸款成數限制）
- 政府打炒房政策（平均地權條例修正）的市場衝擊
- 人口結構變化對長期房價的影響

## 回覆原則

1. **具體數字優先**：盡量提供實際的價格範圍，以「萬元/坪」或「萬元（總價）」呈現
2. **說明依據**：告知數字的來源邏輯（如：實價登錄近期成交、區域均價、特定條件加減乘除）
3. **誠實說明不確定性**：若資訊超出知識截止日期或缺乏具體地址難以精確估算，應如實說明
4. **主動追問**：若使用者的問題不夠具體（缺少地點、坪數、屋齡等），主動詢問關鍵細節
5. **中文回覆**：全程使用繁體中文，必要時可附英文術語對照
6. **提供行動建議**：不只給資訊，也提供下一步可以採取的具體行動

## 重要聲明
你提供的資訊為參考性質，實際房價受市場即時動態影響，建議使用者在做出重大財務決策前，
諮詢持有地政士或不動產經紀人執照的專業人員，並查閱內政部不動產交易實價查詢服務網（lvr.land.moi.gov.tw）的最新資料。
"""


def create_client() -> anthropic.Anthropic:
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("錯誤：請設定環境變數 ANTHROPIC_API_KEY")
        sys.exit(1)
    return anthropic.Anthropic(api_key=api_key)


def print_banner():
    print("=" * 60)
    print("  🏠 台灣房價查詢高手 AI")
    print("  專業不動產市場顧問，隨時為您解答")
    print("=" * 60)
    print("  輸入 'quit' 或 'exit' 結束對話")
    print("  輸入 'clear' 清除對話紀錄，重新開始")
    print("=" * 60)
    print()


def chat(client: anthropic.Anthropic, messages: list[dict]) -> str:
    """
    發送多輪對話請求，在 system prompt 啟用 prompt caching。
    system prompt 超過 1024 tokens，符合 Opus 4.7 的快取門檻 (4096 tokens)；
    實際是否命中快取依 token 數而定，但快取標記已正確設置。
    """
    response = client.messages.create(
        model=MODEL,
        max_tokens=2048,
        system=[
            {
                "type": "text",
                "text": SYSTEM_PROMPT,
                # 將長 system prompt 標記為可快取前綴，
                # 重複對話時省去重複計算費用（約節省 90% 輸入成本）
                "cache_control": {"type": "ephemeral"},
            }
        ],
        messages=messages,
    )

    # 顯示快取使用情況（除錯用，可移除）
    usage = response.usage
    cache_read = getattr(usage, "cache_read_input_tokens", 0) or 0
    cache_write = getattr(usage, "cache_creation_input_tokens", 0) or 0
    if cache_read or cache_write:
        note = []
        if cache_write:
            note.append(f"快取寫入 {cache_write} tokens")
        if cache_read:
            note.append(f"快取命中 {cache_read} tokens")
        print(f"  [快取] {' | '.join(note)}\n")

    text_blocks = [b.text for b in response.content if b.type == "text"]
    return "".join(text_blocks)


def _enrich_with_lvr(user_input: str) -> str:
    """
    偵測地點並查詢實價登錄；若有資料則將成交摘要注入 prompt。
    """
    loc = parse_location(user_input)
    city, district, road = loc["city"], loc["district"], loc["road"]

    if not city:
        return user_input

    # 從輸入中嘗試抓房數（如 1房、2房）
    import re
    rooms_match = re.search(r"([1-9一二三四五六七八九])房", user_input)
    rooms = rooms_match.group(1) if rooms_match else None
    # 阿拉伯數字轉字串以匹配 CSV 欄位
    if rooms and rooms.isdigit():
        rooms = rooms  # CSV 欄位值為 "1", "2", ...

    rows, err = get_transactions(city, district, road, rooms)

    if err:
        print(f"  [實價登錄] {err}")
        return user_input

    if not rows:
        print(f"  [實價登錄] {city}{district or ''} 查無符合成交紀錄")
        return user_input

    lvr_text = summarize(rows)
    print(f"  [實價登錄] 找到 {len(rows)} 筆成交紀錄，已注入對話\n")
    return (
        f"[系統提供的實價登錄成交資料，請優先依據此資料回答]\n"
        f"{lvr_text}\n\n"
        f"使用者問題：{user_input}"
    )


def run_cli():
    client = create_client()
    print_banner()

    messages: list[dict] = []

    print("顧問：您好！我是您的專業不動產市場顧問。請問您想了解哪個地區的房價，或有什麼購屋相關問題？\n")

    while True:
        try:
            user_input = input("您：").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n\n感謝使用，祝您找到理想的家！")
            break

        if not user_input:
            continue

        if user_input.lower() in ("quit", "exit", "bye"):
            print("\n顧問：感謝使用台灣房價查詢高手 AI，祝您找到理想的家！")
            break

        if user_input.lower() == "clear":
            messages.clear()
            print("\n── 對話紀錄已清除，重新開始 ──\n")
            print("顧問：您好！請問有什麼房產問題需要協助？\n")
            continue

        # 嘗試從輸入萃取地點，注入實價登錄資料
        enriched = _enrich_with_lvr(user_input)
        messages.append({"role": "user", "content": enriched})

        print("\n顧問：", end="", flush=True)
        try:
            reply = chat(client, messages)
            print(reply)
            messages.append({"role": "assistant", "content": reply})
        except anthropic.APIStatusError as e:
            print(f"\n[API 錯誤 {e.status_code}] {e.message}")
            # 移除剛才加入的 user 訊息，避免對話狀態錯亂
            messages.pop()
        except anthropic.APIConnectionError:
            print("\n[網路錯誤] 無法連線至 API，請確認網路連線後重試。")
            messages.pop()

        print()


if __name__ == "__main__":
    run_cli()
