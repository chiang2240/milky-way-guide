# 房價查詢助手 AI — AI 提示詞模板

> 將實價登錄 API 資料餵給 AI 的標準提示詞、分析框架、常見查詢情境  
> 最後更新：2026-05-08

---

## 目錄

1. [AI 整合架構說明](#ai-整合架構說明)
2. [基本查詢提示詞](#基本查詢提示詞)
3. [進階分析提示詞](#進階分析提示詞)
4. [常見查詢情境模板](#常見查詢情境模板)
5. [AI 回應格式規範](#ai-回應格式規範)
6. [常見錯誤與修正](#常見錯誤與修正)

---

## AI 整合架構說明

### 整體流程

```
使用者輸入查詢條件
        ↓
解析縣市、行政區、屋型、時間範圍
        ↓
呼叫實價登錄 API 取得原始資料
        ↓
資料清洗（過濾異常值）
        ↓
將清洗後資料 + 使用者問題 → 組合成 Prompt
        ↓
送給 Claude API 分析
        ↓
回傳結構化分析結果給使用者
```

### Claude API 整合範例

```python
import anthropic
import json

client = anthropic.Anthropic()

def analyze_house_data(raw_data: list, user_question: str) -> str:
    """
    將實價登錄資料交給 Claude 分析
    
    raw_data: 已清洗的 API 資料（list of dict）
    user_question: 使用者的查詢問題
    """
    # 計算統計摘要
    summary = calculate_summary(raw_data)
    
    # 組合提示詞
    prompt = build_analysis_prompt(summary, raw_data[:20], user_question)
    
    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1024,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    
    return message.content[0].text


def calculate_summary(data: list) -> dict:
    """計算資料統計摘要"""
    SQMT_TO_PING = 3.30579
    prices = [
        float(d["單價元平方公尺"]) * SQMT_TO_PING / 10000
        for d in data
        if float(d.get("單價元平方公尺", 0)) > 0
    ]
    prices.sort()
    n = len(prices)
    
    return {
        "總筆數": n,
        "平均單價_萬坪": round(sum(prices) / n, 1) if n else 0,
        "中位數單價_萬坪": round(prices[n // 2], 1) if n else 0,
        "最低單價_萬坪": round(prices[0], 1) if n else 0,
        "最高單價_萬坪": round(prices[-1], 1) if n else 0,
    }
```

---

## 基本查詢提示詞

### 系統提示詞（System Prompt）

```
你是一個專業的台灣不動產市場分析助手。

你的職責：
1. 解讀使用者提供的實價登錄成交資料
2. 用清楚易懂的語言說明該地區房市行情
3. 計算並說明單價、總價的合理區間
4. 提醒使用者資料解讀時需注意的事項

規則：
- 所有價格以新台幣萬元為單位表示
- 坪數換算：1坪 = 3.30579 平方公尺
- 台灣房地產資料使用民國年，對外說明時換算為西元年
- 若樣本數不足（< 10 筆），明確說明資料可信度有限
- 不做漲跌預測，只陳述現況資料
- 如資料有異常，主動說明並建議如何解讀
```

---

### 基本行情查詢提示詞

```
以下是從內政部實價登錄 API 取得的成交資料：

【查詢條件】
- 縣市：{county_name}
- 行政區：{district}
- 建物型態：{building_type}
- 查詢期間：{season_range}（西元 {year_range}）

【統計摘要】
- 有效樣本數：{count} 筆
- 平均單價：{avg_price} 萬/坪
- 中位數單價：{median_price} 萬/坪
- 單價範圍：{min_price}–{max_price} 萬/坪

【近期成交明細（前 10 筆）】
{recent_transactions_json}

請根據以上資料：
1. 說明該地區目前的成交行情
2. 解釋平均值與中位數的差異（若差距大，說明原因）
3. 說明單價範圍的合理性
4. 如有任何需要注意的資料品質問題，請說明
```

---

## 進階分析提示詞

### 多季趨勢分析

```
以下是 {county_name}{district} 的多季成交資料：

{quarters_data}

請分析：
1. 過去 {n} 季的單價趨勢（上漲/下跌/持平）
2. 成交量的變化（旺季/淡季規律）
3. 與同期全市平均相比，該區漲跌幅是否異常
4. 目前行情所處的市場週期階段（復甦/擴張/過熱/修正）

回應格式：
- 趨勢摘要（1–2 句）
- 數據說明（表格或條列）
- 注意事項（若有）
```

---

### 同區域不同屋型比較

```
以下是 {county_name}{district} 同期不同建物型態的成交資料：

【住宅大樓】
樣本數：{condo_count} 筆
平均單價：{condo_avg} 萬/坪

【公寓（無電梯）】
樣本數：{apartment_count} 筆
平均單價：{apartment_avg} 萬/坪

【透天厝】
樣本數：{house_count} 筆
平均單價：{house_avg} 萬/坪

請分析：
1. 各屋型的單價差距及原因
2. 各屋型的優缺點簡述
3. 不同預算/需求的購屋者適合哪種屋型
4. 透天厝含土地，單純比較建物單價的侷限性說明
```

---

### 租金報酬率分析

```
以下是 {county_name}{district} 的買賣與租賃資料：

【買賣成交】
平均成交總價：{avg_sale_price} 萬
目標物件坪數：{target_size} 坪
估算物件總價：{estimated_price} 萬

【租賃成交】
同類型平均月租金：{avg_rent} 元
樣本數：{rent_count} 筆

請計算並說明：
1. 年租金報酬率
2. 與台灣各縣市平均報酬率的比較
3. 考量管理費、修繕費、空租期後的實質報酬率估算
4. 投資或自住哪個選擇在此地區較有利
```

---

## 常見查詢情境模板

### 情境一：首購族找屋

```python
user_query = """
我第一次買房，預算 1,000 萬，想在新北市找三房，
最好能通勤到台北市信義區，通勤不超過 45 分鐘。
請推薦適合的行政區，並提供該區的行情資料。
"""

# 系統需先：
# 1. 識別預算：1,000 萬
# 2. 識別需求：三房（約 25–35 坪）
# 3. 識別通勤條件：到信義區 45 分鐘
# 4. 識別縣市：新北市（代碼 F）
# 5. 根據通勤條件推算適合行政區（板橋、中和、土城等）
# 6. 呼叫 API 查詢各區行情
# 7. 餵給 AI 分析
```

**對應提示詞：**

```
使用者是首購族，預算 {budget} 萬，需求 {room_type}，
通勤目的地：{commute_destination}，通勤時間上限：{commute_limit} 分鐘。

根據以下各候選行政區的實價登錄資料，推薦最適合的 2–3 個區域：

{area_comparison_data}

回應請包含：
1. 推薦行政區（按適合度排序）
2. 各區的預算可購買的坪數估算
3. 各區的交通說明（捷運/公車/騎車）
4. 各區的生活機能簡述
5. 需要注意的購屋風險
```

---

### 情境二：投資客評估報酬率

```python
user_query = """
想在高雄買一間 20 坪左右的小宅出租，
預算 500 萬，評估哪個行政區的租金報酬率最好？
"""
```

**對應提示詞：**

```
投資評估需求：
- 城市：{city}
- 預算：{budget} 萬
- 目標坪數：{target_size} 坪
- 目的：出租

以下是各候選行政區的買賣與租賃成交資料：

{investment_data}

請針對每個行政區計算並比較：
1. 預算可購買的物件條件
2. 同類型月租金行情
3. 毛租金報酬率
4. 實質報酬率（扣除管理費 3–5%、空租期 1 個月/年）
5. 各區的出租需求評估（學區、就業人口、外籍人士需求等）
6. 最終推薦排名
```

---

### 情境三：換屋評估

```python
user_query = """
目前住台北市文山區 25 坪公寓，想換到同區域或鄰近的 35 坪大樓，
請告訴我差額大概是多少？
```

**對應提示詞：**

```
換屋評估：
- 目前物件：{current_area}{current_district}，{current_size} 坪，{current_type}
- 目標物件：{target_area}{target_district}，{target_size} 坪，{target_type}

實價登錄資料：

【目前居住區域 - {current_type} 行情】
{current_data}

【目標區域 - {target_type} 行情】
{target_data}

請計算：
1. 目前物件估值區間
2. 目標物件總價區間
3. 換屋資金缺口估算
4. 換屋時機評估（現在適合換嗎？）
5. 換屋需考量的額外成本（仲介費、契稅、代書費、裝潢等）
```

---

## AI 回應格式規範

要求 AI 以結構化格式回應，方便前端呈現：

```python
response_format_prompt = """
請以以下 JSON 格式回應：

{
  "summary": "一句話總結",
  "price_range": {
    "low": 數字（萬/坪）,
    "median": 數字（萬/坪）,
    "high": 數字（萬/坪）
  },
  "key_findings": [
    "重點發現1",
    "重點發現2",
    "重點發現3"
  ],
  "recommendations": [
    "建議1",
    "建議2"
  ],
  "warnings": [
    "需注意事項1"
  ],
  "data_quality": "高/中/低",
  "data_quality_reason": "說明"
}
"""
```

---

## 常見錯誤與修正

### AI 給出價格預測

| 問題 | AI 說「未來房價會漲」 |
|------|---------------------|
| 原因 | System Prompt 未明確限制 |
| 修正 | 在 System Prompt 加入：「禁止做任何漲跌預測，只陳述現況資料。」 |

---

### AI 混淆含公設與不含公設的坪價

| 問題 | AI 給出的坪價遠低於市場認知 |
|------|---------------------------|
| 原因 | API 資料為含公設單價，AI 未說明 |
| 修正 | 在資料前加說明：「以下單價為含公設登記坪數計算，不含公設的主建物實際坪價約高 30–40%。」 |

---

### 樣本數不足時 AI 仍給出確定性結論

| 問題 | 只有 3 筆資料，AI 卻說「行情約 X 萬/坪」 |
|------|----------------------------------------|
| 原因 | 未在 Prompt 中設定樣本數門檻提醒 |
| 修正 | 加入規則：「若樣本數 < 10 筆，必須在回應開頭標注『資料樣本不足，參考價值有限』。」 |

---

## 參考資料

| 來源 | 內容 |
|------|------|
| [Anthropic Claude API 文件](https://docs.anthropic.com) | Claude API 使用方式、模型選擇 |
| [實價登錄 API 文件](https://plvr.land.moi.gov.tw/DownloadOpenData) | 官方 API 規格 |
| [政府資料開放平台 API](https://data.gov.tw/about-api) | API 金鑰申請與使用說明 |
