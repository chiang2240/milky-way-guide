"""
內政部實價登錄開放資料整合模組
資料來源：https://plvr.land.moi.gov.tw/DownloadOpenData
"""

import csv
import io
import urllib.request
from pathlib import Path
from datetime import datetime, timedelta

COUNTY_CODES: dict[str, str] = {
    "台北市": "A", "臺北市": "A",
    "台中市": "B", "臺中市": "B",
    "基隆市": "C",
    "台南市": "D", "臺南市": "D",
    "高雄市": "E",
    "新北市": "F",
    "宜蘭縣": "G",
    "桃園市": "H",
    "嘉義縣": "I",
    "新竹縣": "J",
    "苗栗縣": "K",
    "南投縣": "M",
    "彰化縣": "N",
    "新竹市": "O",
    "雲林縣": "P",
    "嘉義市": "Q",
    "屏東縣": "T",
    "花蓮縣": "U",
    "台東縣": "V", "臺東縣": "V",
    "金門縣": "W",
    "澎湖縣": "X",
    "連江縣": "Z",
}

_CACHE_DIR = Path(__file__).parent / ".cache"
_CACHE_TTL = timedelta(hours=24)


def _cache_path(code: str) -> Path:
    _CACHE_DIR.mkdir(exist_ok=True)
    return _CACHE_DIR / f"{code}_lvr_land_A.csv"


def _is_fresh(path: Path) -> bool:
    if not path.exists():
        return False
    return datetime.now() - datetime.fromtimestamp(path.stat().st_mtime) < _CACHE_TTL


def _download(code: str) -> str:
    url = (
        "https://plvr.land.moi.gov.tw/DownloadOpenData"
        f"?type=A&format=CSV&fileName={code}_lvr_land_A.csv"
    )
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/124.0.0.0 Safari/537.36"
        ),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "zh-TW,zh;q=0.9,en;q=0.8",
        "Referer": "https://plvr.land.moi.gov.tw/DownloadOpenData",
    }
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            raw = r.read()
    except urllib.error.HTTPError as e:
        if e.code == 403:
            raise Exception(
                "存取被拒（403）。台灣政府 API 限制非台灣 IP，"
                "請在台灣網路環境下執行本程式。"
            )
        raise
    # 嘗試 utf-8-sig → utf-8 → big5
    for enc in ("utf-8-sig", "utf-8", "big5"):
        try:
            return raw.decode(enc)
        except UnicodeDecodeError:
            continue
    return raw.decode("utf-8", errors="replace")


def get_transactions(
    city: str,
    district: str | None = None,
    road: str | None = None,
    rooms: str | None = None,
) -> tuple[list[dict], str | None]:
    """
    取得實價登錄買賣成交資料，回傳 (rows, error)。
    """
    code = COUNTY_CODES.get(city)
    if not code:
        return [], f"不支援縣市：{city}"

    path = _cache_path(code)
    if _is_fresh(path):
        text = path.read_text(encoding="utf-8")
    else:
        try:
            text = _download(code)
            path.write_text(text, encoding="utf-8")
        except Exception as e:
            if path.exists():
                text = path.read_text(encoding="utf-8")
            else:
                return [], f"無法下載實價登錄資料：{e}"

    rows = []
    try:
        reader = csv.DictReader(io.StringIO(text))
        for row in reader:
            if "建物" not in row.get("交易標的", ""):
                continue
            if district and district not in row.get("鄉鎮市區", ""):
                continue
            if road and road not in row.get("土地位置建物門牌", ""):
                continue
            if rooms and row.get("建物現況格局-房", "").strip() != rooms:
                continue
            rows.append(row)
    except Exception as e:
        return [], f"解析資料失敗：{e}"

    return rows, None


def summarize(rows: list[dict], top_n: int = 15) -> str:
    """
    將成交紀錄整理為文字摘要，供 Claude 參考。
    """
    if not rows:
        return "查無符合條件的實價登錄成交紀錄。"

    def sort_key(r: dict) -> int:
        try:
            return int(r.get("交易年月日", "0"))
        except ValueError:
            return 0

    recent = sorted(rows, key=sort_key, reverse=True)[:top_n]
    lines: list[str] = []
    unit_prices: list[float] = []

    for r in recent:
        addr = r.get("土地位置建物門牌", "")
        date_raw = r.get("交易年月日", "")
        total_price_str = r.get("總價元", "")
        unit_price_sqm_str = r.get("單價元平方公尺", "")
        area_sqm_str = r.get("建物移轉總面積平方公尺", "")
        btype = r.get("建物型態", "")
        rooms = r.get("建物現況格局-房", "")
        floor = r.get("移轉層次", "")
        total_floor = r.get("總樓層數", "")

        try:
            date_str = f"{int(date_raw[:3]) + 1911}/{date_raw[3:5]}/{date_raw[5:7]}"
        except Exception:
            date_str = date_raw

        try:
            ping = float(area_sqm_str) / 3.3058
            ping_str = f"{ping:.1f}坪"
        except Exception:
            ping_str = "N/A"

        try:
            u = float(unit_price_sqm_str) * 3.3058 / 10000
            unit_prices.append(u)
            u_str = f"{u:.1f}萬/坪"
        except Exception:
            u_str = "N/A"

        try:
            t_str = f"{int(total_price_str) / 10000:.0f}萬"
        except Exception:
            t_str = "N/A"

        lines.append(
            f"• {date_str} ｜ {addr} ｜ {btype} {rooms}房 {floor}/{total_floor}F"
            f" ｜ {ping_str} ｜ {u_str} ｜ 總價{t_str}"
        )

    out = f"【實價登錄近期成交（共 {len(rows)} 筆符合，顯示最新 {len(recent)} 筆）】\n"
    out += "\n".join(lines)

    if unit_prices:
        avg = sum(unit_prices) / len(unit_prices)
        out += (
            f"\n\n統計（{len(unit_prices)} 筆）："
            f"均價 {avg:.1f} 萬/坪，"
            f"區間 {min(unit_prices):.1f}–{max(unit_prices):.1f} 萬/坪"
        )

    return out
