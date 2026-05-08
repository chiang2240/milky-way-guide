# Vivo X300 Ultra — 銀河拍攝教學手冊

> 機型：Vivo X300 Ultra (V2562)  
> 模式：專業模式（Pro Mode）  
> 最後更新：2026-05-08

---

## 鏡頭規格（已查證）

本手冊參數基於 Vivo X300 Ultra 實際硬體規格制定：

| 鏡頭 | 感測器 | 等效焦距 | 光圈 | 像素尺寸 |
|------|--------|----------|------|----------|
| 超廣角 | 50MP, 1/1.28" | **14mm** | f/2.0 | 1.22µm |
| 主鏡頭 | 200MP Sony Lytia 901, 1/1.12" | **35mm** | f/1.9 | 0.7µm |
| 望遠 | 200MP Samsung HP0, 1/1.4" | **85mm** | f/2.7 | 0.56µm |

> 資料來源：[GSMArena Vivo X300 Ultra 規格頁](https://www.gsmarena.com/vivo_x300_ultra_5g-14388.php)、[vivo 官方產品頁](https://www.vivo.com/eu/products/x300-ultra)

---

## 目錄

1. [出發前準備](#出發前準備)
2. [場景一：銀河核心拍攝](#場景一銀河核心拍攝)
3. [場景二：銀河全景拼接](#場景二銀河全景拼接)
4. [對焦校準流程](#對焦校準流程)
5. [500 法則與 NPF 法則說明](#500-法則與-npf-法則說明)
6. [常見問題排除](#常見問題排除)
7. [參數速查表](#參數速查表)
8. [後期處理建議](#後期處理建議)

---

## 出發前準備

### 器材清單

- [ ] Vivo X300 Ultra（電量充滿，儲存空間充足，SuperRAW 單張約 25–50MB）
- [ ] 手機腳架 + 雲台（必備，長曝不可手持）
- [ ] 藍牙遙控快門 或 使用倒數計時器（減少按壓震動）
- [ ] 行動電源（長時間拍攝 + 低溫環境耗電快）
- [ ] 紅光頭燈（不影響夜視適應）

### 環境確認

| 項目 | 建議 |
|------|------|
| 月相 | 新月前後 ±3 天最佳，避免月光干擾 |
| 光害 | 波特爾等級 3 以下最佳（可用 [Light Pollution Map](https://www.lightpollutionmap.info) 查詢） |
| 天氣 | 無雲、濕度低、無霧 |
| 銀河方位 | 使用 Stellarium 或 PhotoPills 確認升起時間與方位角 |
| 最佳季節 | 台灣 4–9 月，銀河核心可見於南方天空 |

> 參考：手機感測器較小，對光害更敏感。波特爾 5 以上的環境拍攝效果會大幅下降。([Milky Way Planner](https://www.milkywayplanner.com/intro-to-astrophotography/milky-way-photography-phone))

### 手機設定（拍攝前）

1. 開啟飛航模式（避免來電震動 + 省電）
2. 關閉螢幕自動亮度，手動調到最低（保護夜視適應，約需 20–45 分鐘）
3. 進入相機 → 專業模式
4. 確認 RAW 格式設為 **SuperRAW**
5. 關閉閃光燈

---

## 場景一：銀河核心拍攝

### 適用情境

使用超廣角鏡頭單張拍攝銀河中心最明亮的區域，一次涵蓋大範圍天空。

### 為什麼用超廣角（14mm）而非主鏡頭（35mm）？

- 14mm 視野達 116°，可一張涵蓋銀河核心 + 地景
- 500 法則允許更長曝光時間（32 秒），收集更多光線
- f/2.0 光圈搭配 1/1.28" 感測器，低光表現優秀

### 參數設定

| 參數 | 設定值 | 依據 |
|------|--------|------|
| 鏡頭 | **超廣角（14mm, f/2.0）** | 視野最廣，500 法則允許最長曝光 |
| ISO | **1600**（首選起點）→ 視情況提高至 **3200** | 手機星空攝影建議 ISO 1600–3200 起步 ([ViewBug](https://viewbug.com/knowledge/astrophotography-camera-settings), [vivo 社群](https://bbs.vivo.com/in/thread/175210)) |
| 快門速度 | **32"**（機身最長快門） | 500÷14=35.7s，機身上限 32s 在安全範圍內 |
| EV | **0** | 全手動曝光下固定 |
| 對焦 | **MF 1.00**（手動無限遠） | 星空必須手動對焦，AF 無法鎖定星點 ([vivo 社群](https://bbs.vivo.com/in/thread/175210)) |
| 白平衡 | **手動 3800K** / Tint 0 | 天文攝影標準建議 3800–4000K，保留銀河自然冷色調 ([ViewBug](https://viewbug.com/knowledge/astrophotography-camera-settings)) |
| RAW 格式 | **SuperRAW** | 最大動態範圍，後期降噪與調色空間最大 |
| 閃光燈 | **關** | 必須關閉 |

### 操作步驟

1. 架好腳架，切換至超廣角鏡頭，對準銀河核心方向
2. 進入專業模式，依上表設定所有參數
3. 執行[對焦校準流程](#對焦校準流程)
4. 使用遙控快門或 **2 秒倒數計時**拍攝（避免按壓震動）
5. 拍攝後**雙指放大檢查星點**是否銳利
6. 若星點模糊 → 微調對焦值（0.98 ↔ 1.00 之間嘗試）
7. 確認合焦後，**同參數連拍 8–15 張**（後期堆疊降噪用）

### 為什麼要堆疊？

手機感測器面積約為全片幅相機的 1/6，高 ISO 噪點不可避免。堆疊多張可在不提高 ISO 的情況下大幅改善信噪比。([Photography Life](https://photographylife.com/night-sky-image-stacking))

---

## 場景二：銀河全景拼接

### 適用情境

多張拼接覆蓋完整銀河弧線（可達 180°），最終獲得超高解析度全景圖。使用較長焦段拍攝每一格，拼接後同時擁有廣視野與高細節。

### 為什麼用主鏡頭（35mm）拼接？

> 「Some of the best Milky Way panoramas are shot at 35mm or 50mm... The longer focal length captures more detail in each panel, and stitching 8-12 panels together gives you both the wide view and the resolution.」  
> — [Milky Way Planner: Building a Milky Way Panorama](https://www.milkywayplanner.com/intro-to-astrophotography/milky-way-panorama)

- 35mm 主鏡頭擁有 200MP + 1/1.12" 大感測器 + f/1.9 大光圈，是本機最強低光鏡頭
- 拼接 10–12 張後總像素遠超單張超廣角，細節極為豐富
- f/1.9 是本機最大光圈，進光量最多

### 參數設定

| 參數 | 設定值 | 依據 |
|------|--------|------|
| 鏡頭 | **主鏡頭（35mm, f/1.9）** | 最大光圈 + 最大感測器，低光最強 |
| ISO | **1600**（首選）→ 視情況 **3200** | 與核心拍攝相同原則 |
| 快門速度 | **15"**（首選安全值） | 500÷35=14.3s，取機身可選值 15" |
| EV | **0** | 固定曝光，拼接亮度一致 |
| 對焦 | **MF 1.00**（手動無限遠） | 全程鎖定，絕對不可切換 AF |
| 白平衡 | **手動 3800K** / Tint 0 | 所有張數色溫必須一致，否則拼接色差明顯 |
| RAW 格式 | **SuperRAW** | 拼接裁切後仍保有細節 |
| 閃光燈 | **關** | 必須關閉 |

### 操作步驟

1. 架好腳架，雲台調整為可水平旋轉，**使用水平儀確認腳架水平**
2. 切換至主鏡頭（35mm），設定所有參數（**全程不可更動任何設定**）
3. 執行[對焦校準流程](#對焦校準流程)
4. **手機轉為直幅（Portrait）方向**拍攝 — 可獲得更多天地覆蓋範圍
5. 從銀河弧線一端開始，水平方向逐張拍攝
6. **每張重疊 30–40%**（寧多勿少）
7. 保持旋轉方向一致（左→右 或 右→左，不回頭）
8. **全部張數須在 5–8 分鐘內完成**（避免星星位移導致拼接失敗）

### 拼接要點

| 項目 | 要求 | 來源 |
|------|------|------|
| 重疊率 | 30–40%（建議偏多） | [Milky Way Planner](https://www.milkywayplanner.com/intro-to-astrophotography/milky-way-panorama) |
| 拍攝方向 | 直幅，單一方向掃描 | 同上 |
| 參數鎖定 | ISO / 快門 / 白平衡 / 對焦全程不變 | 同上 |
| 張數估算 | 35mm 直幅約需 **10–12 張**覆蓋完整弧線 | 同上 |
| 完成時間 | 5–8 分鐘內 | 同上 |
| 拼接軟體 | PTGui（推薦）/ Lightroom / Microsoft ICE / Hugin | 同上 |

---

## 對焦校準流程

銀河拍攝最關鍵的步驟。對焦不準，其他參數再完美也沒用。

> 「Focusing on stars is one of the most challenging aspects of astrophotography. Autofocus fails in the dark.」— [ViewBug](https://viewbug.com/knowledge/astrophotography-camera-settings)

### 步驟

1. 將對焦設為 **MF 1.00**（無限遠端）
2. 對準天空中**最亮的星星**（如織女星、天狼星、大角星）
3. ISO 暫時拉高至 **5000**，快門設 **6"**，拍攝一張測試照
4. **雙指放大至最大**，檢查星點：
   - ✅ 銳利小圓點 → 合焦成功
   - ❌ 模糊光斑 / 甜甜圈狀 → 需微調
5. 若不合焦，嘗試 **0.98** 再拍一張比較
6. 在 1.00 與 0.98 之間找到最銳利的位置
7. 確認後**全程不再觸碰對焦設定**
8. 將 ISO 和快門恢復為正式拍攝值

### 注意事項

- 溫度變化可能導致對焦漂移，每 30–60 分鐘重新確認一次
- 切勿誤觸螢幕上的對焦滑桿
- 如果找不到亮星，可對遠處山稜線上的燈光對焦（距離需 >500m）

---

## 500 法則與 NPF 法則說明

### 500 法則（快速估算）

最長快門秒數 = 500 ÷ 等效焦距

| 鏡頭 | 計算 | 最長快門 | 機身可選值 |
|------|------|----------|-----------|
| 超廣角 14mm | 500÷14 = 35.7s | ~36s | **32"**（機身上限，安全） |
| 主鏡頭 35mm | 500÷35 = 14.3s | ~14s | **15"**（最接近值） |
| 望遠 85mm | 500÷85 = 5.9s | ~6s | **6"** |

> 500 法則是傳統經驗法則，適用於一般觀看尺寸。若放大至 100% 像素檢視，可能仍有輕微拖線。([PetaPixel](https://petapixel.com/2017/04/07/npf-rule-formula-sharp-star-photos-every-time/), [ViewBug](https://viewbug.com/knowledge/500-rule-astrophotography))

### NPF 法則（精確計算）

(35 × 光圈值 + 30 × 像素尺寸µm) ÷ 焦距 = 最長快門秒數

| 鏡頭 | 計算 | 結果 |
|------|------|------|
| 超廣角 14mm, f/2.0, 1.22µm | (35×2.0 + 30×1.22) ÷ 14 | **7.6 秒** |
| 主鏡頭 35mm, f/1.9, 0.7µm | (35×1.9 + 30×0.7) ÷ 35 | **2.5 秒** |
| 望遠 85mm, f/2.7, 0.56µm | (35×2.7 + 30×0.56) ÷ 85 | **1.3 秒** |

> NPF 法則追求像素級銳利，對手機 200MP 高像素感測器來說極為嚴格。實際拍攝中，**500 法則的值在正常觀看尺寸下完全可接受**。若你追求極致銳利（例如大圖輸出），可取兩者中間值。([PetaPixel](https://petapixel.com/2017/04/07/npf-rule-formula-sharp-star-photos-every-time/))

### 實用建議

- **社群分享 / 手機螢幕觀看**：使用 500 法則的值（32" / 15" / 6"）
- **大圖輸出 / 100% 裁切**：縮短快門至 500 法則的 50–70%，用更高 ISO 補償
- **堆疊降噪**：可用較短快門 + 多張堆疊，同時獲得銳利星點與低噪點

---

## 常見問題排除

### 星點拖線（星軌）

| 原因 | 解決方案 |
|------|----------|
| 快門超過 500 法則上限 | 縮短快門（參考上方計算表） |
| 使用望遠鏡頭但快門太長 | 85mm 最長只能用 6"，不可更長 |

### 畫面全黑或極暗

| 原因 | 解決方案 |
|------|----------|
| ISO 太低 | 從 1600 提高至 3200，仍暗可試 5000 |
| 快門太短 | 延長至該鏡頭的 500 法則上限 |
| 鏡頭被遮擋 | 檢查手機殼是否擋到超廣角鏡頭 |
| 光害太重 | 環境問題，需更換地點 |

### 畫面過亮 / 天空泛白

| 原因 | 解決方案 |
|------|----------|
| 光害嚴重 | 更換拍攝地點（波特爾 3 以下） |
| ISO 過高 | 從 3200 降至 1600 |
| 快門過長 | 適度縮短 |

### 噪點嚴重

| 原因 | 解決方案 |
|------|----------|
| ISO 過高 | 盡量控制在 3200 以內 |
| 單張拍攝 | 改用堆疊法：同參數拍 8–15 張後期合成 |
| 手機過熱 | 休息幾分鐘讓感測器降溫（長時間拍攝感測器熱噪增加） |

### 星點不銳利（模糊）

| 原因 | 解決方案 |
|------|----------|
| 對焦不準 | 重新執行[對焦校準流程](#對焦校準流程) |
| 手震 | 使用遙控快門 + 倒數計時 |
| 腳架不穩 | 確認腳架穩固，避免風大時拍攝 |
| 快門過長導致拖線 | 參考 500 法則縮短快門 |

### 白平衡偏色

| 原因 | 解決方案 |
|------|----------|
| 使用 AUTO 白平衡 | 切換為手動 3800K |
| 色溫設太高（>5000K，偏黃） | 降低至 3800–4000K |
| 色溫設太低（<3000K，過藍） | 提高至 3800K |
| 拍 SuperRAW 後期可無損調整 | 現場大致正確即可，後期精修 |

### 拼接失敗 / 接縫明顯

| 原因 | 解決方案 |
|------|----------|
| 重疊率不足 | 確保每張重疊 30–40% |
| 各張曝光不一致 | 全程鎖定所有參數，不可動 |
| 拍攝間隔太久（>8 分鐘） | 加快節奏，全序列 5–8 分鐘內完成 |
| 腳架不水平 | 使用水平儀校正 |

---

## 參數速查表

拍攝現場快速查閱：

```
┌──────────────────────────────────────────────────────────────────┐
│            Vivo X300 Ultra 銀河拍攝速查                            │
├──────────────┬────────────────────┬───────────────────────────────┤
│     項目     │    銀河核心（單張） │    銀河全景拼接                │
├──────────────┼────────────────────┼───────────────────────────────┤
│ 鏡頭         │ 超廣角 14mm f/2.0  │ 主鏡頭 35mm f/1.9            │
│ ISO          │ 1600（→3200）      │ 1600（→3200）                │
│ 快門         │ 32"               │ 15"                          │
│ 對焦         │ MF 1.00            │ MF 1.00                      │
│ 白平衡       │ 3800K / Tint 0     │ 3800K / Tint 0               │
│ RAW          │ SuperRAW           │ SuperRAW                     │
│ EV           │ 0                  │ 0                            │
│ 閃光燈       │ 關                 │ 關                           │
├──────────────┼────────────────────┼───────────────────────────────┤
│ 方向         │ 橫幅               │ 直幅（Portrait）             │
│ 張數         │ 8–15 張（堆疊用）  │ 10–12 張（拼接用）           │
│ 重疊率       │ —                  │ 30–40%                       │
│ 完成時間     │ 不限               │ 5–8 分鐘內                   │
└──────────────┴────────────────────┴───────────────────────────────┘
```

---

## 後期處理建議

### 推薦軟體

| 用途 | 軟體 |
|------|------|
| RAW 處理 | Lightroom / RawTherapee / Snapseed |
| 堆疊降噪 | Sequator（Windows，免費）/ Starry Landscape Stacker（Mac） |
| 全景拼接 | PTGui（推薦，處理星空對齊最佳）/ Lightroom Panorama / Microsoft ICE / Hugin（免費） |
| 進階合成 | Photoshop / Affinity Photo |

### 基本後期流程

1. **匯入 SuperRAW 檔案**至 Lightroom 或 RawTherapee
2. **堆疊降噪**（如有多張）：匯入 Sequator，對齊星空後平均合成
3. **白平衡微調**：SuperRAW 可無損調整色溫，現場不完美也沒關係
4. **提升對比**：拉高清晰度 / 結構，讓銀河紋理浮現
5. **曲線調整**：壓暗天空背景光害，提亮銀河帶
6. **色彩校正**：適度提升飽和度，但避免過度失真
7. **裁切構圖**：200MP SuperRAW 允許大幅裁切仍保有細節

---

## 進階策略：高 ISO + 短曝 + 堆疊法

除了前面的「標準曝光法」，近年專業天文攝影社群發展出另一套更激進但效果更好的方法：**拉高 ISO、大幅縮短快門、大量堆疊**。這套方法原本用於單眼/無反相機，但原理完全適用於手機。

### 原理

> The Image Guild 建議：使用 ISO 12800、35mm 快門僅 3 秒、連拍 25 張堆疊。極短快門確保星點完全不拖線，高 ISO 的噪點透過堆疊消除。  
> — [The Image Guild: A Complete Guide to Night Sky Photography](https://www.theimageguild.com/post/how-to-photograph-milky-way-guide)

> PhotoPills 建議：ISO 3200–6400、使用 NPF 法則計算快門（通常 8–20 秒）、白平衡 3900K。  
> — [PhotoPills: Milky Way Photography Settings](https://photopills.com/articles/milky-way-photography-settings)

### 套用到 X300 Ultra 的設定

| 參數 | 標準曝光法（前述） | 高 ISO 堆疊法 |
|------|-------------------|---------------|
| ISO | 1600–3200 | **5000–12800** |
| 快門（14mm） | 32" | **6"** |
| 快門（35mm） | 15" | **2.5"**（取機身 1" 或手動計時） |
| 堆疊張數 | 8–15 張 | **20–30 張** |
| 星點銳利度 | 良好（500 法則） | **極銳利**（接近 NPF 法則） |
| 單張噪點 | 低–中 | 高（但堆疊後消除） |
| 後期難度 | 低 | 中（需堆疊軟體） |

### 限制與注意

- X300 Ultra 機身最短長曝為 **1"**（無法設定 2.5 秒或 3 秒），因此 35mm 鏡頭若要用此法，實際可選 **1"**（偏短，需更高 ISO）或 **2.5"**（若機身支援）
- 超廣角 14mm 用 **6"** 快門完全可行（機身有此選項），搭配 ISO 5000–10000 + 20 張堆疊
- 此法對後期軟體（Sequator）依賴度高，但最終成品品質可超越標準法

### 何時選擇哪種方法？

| 情境 | 建議方法 |
|------|----------|
| 第一次拍銀河，想簡單出片 | 標準曝光法 |
| 追求最銳利星點 + 最低噪點 | 高 ISO 堆疊法 |
| 現場時間有限 | 標準曝光法（張數少） |
| 有耐心 + 會用 Sequator | 高 ISO 堆疊法 |
| 全景拼接（每格需快速完成） | 高 ISO 堆疊法更適合（每格曝光短，整組完成更快） |

---

## 跨設備參數交叉比對

以下整理多個權威來源的銀河拍攝建議參數，涵蓋單眼相機、無反相機、手機，供你理解「業界共識」在哪裡：

| 來源 | 設備類型 | ISO | 快門 | 光圈 | 白平衡 | 特殊建議 |
|------|----------|-----|------|------|--------|----------|
| [PhotoPills](https://photopills.com/articles/milky-way-photography-settings) | 單眼/無反 | 3200–6400 | NPF 法則 (8–20s) | f/1.4–2.8 | **3900K** | 用 NPF 而非 500 法則 |
| [The Image Guild](https://www.theimageguild.com/post/how-to-photograph-milky-way-guide) | 單眼/無反 | **12800** | 35mm=3s, 24mm=4s, 14mm=8s | f/2.8 | **3750–4250K** | 25 張堆疊 |
| [ViewBug Cheat Sheet](https://viewbug.com/knowledge/astrophotography-camera-settings) | 通用 | 1600–6400 (起點 3200) | 500 法則 (15–25s) | f/1.4–2.8 | **3800–4000K** | RAW 必備 |
| [Capture the Atlas](https://capturetheatlas.com/how-to-photograph-the-milky-way) | 單眼/無反 | 3200–6400 | 10–25s | f/2.8 | — | 焦距越長快門越短 |
| [AstroBackyard](https://astrobackyard.com/how-to-photograph-milky-way/) | 單眼/無反 | 3200 | 20s (24mm) | f/1.4 | — | 單張曝光示範 |
| [vivo 社群實拍](https://bbs.vivo.com/in/thread/175210) | vivo 手機 | 1600–3200 | 25s | — | — | 腳架 + 計時器 |
| [Picture Correct (全景)](https://www.picturecorrect.com/milky-way-panorama-photo-tutorial/) | 單眼/無反 | 3200–6400 | 20s | f/2.8–3.2 | — | 15° 旋轉間隔 |
| [Milky Way Planner (全景)](https://www.milkywayplanner.com/intro-to-astrophotography/milky-way-panorama) | 通用 | — | — | — | — | 35mm 需 10–12 張, 30–40% 重疊 |

### 業界共識總結

從上表可以歸納出天文攝影社群的共識：

1. **ISO**：3200 是最常見的起點，範圍 1600–6400。搭配堆疊可推到 12800
2. **快門**：取決於焦距。500 法則是入門標準，NPF 法則是進階標準
3. **白平衡**：**3800–4000K** 是絕對共識（PhotoPills 建議 3900K）
4. **光圈**：越大越好，f/2.8 是基本門檻，f/1.4–1.9 是理想值
5. **格式**：RAW 是必須，沒有例外
6. **對焦**：手動無限遠，沒有例外
7. **堆疊**：從「進階技巧」變成「標準流程」，尤其對小感測器設備

### 對應到你的 X300 Ultra

- f/1.9 主鏡頭光圈**優於多數建議的 f/2.8 門檻**，進光量多 2 倍以上
- 1/1.12" 感測器是目前手機中最大等級之一，噪點控制力強
- ISO 3200 + 15" 快門 + f/1.9 的組合，進光量相當於單眼 f/2.8 + ISO 3200 + 15" 的 **2.2 倍**
- 你的硬體條件在手機中屬頂級，參數可以比一般手機建議更保守（更低 ISO）

---

## 現場即時諮詢指南

拍攝時如果遇到問題，可以直接描述以下資訊給我，我會根據本手冊和你的機器參數範圍給出調整建議：

1. **你正在用哪顆鏡頭**（超廣角 / 主鏡頭 / 望遠）
2. **目前的 ISO 和快門設定**
3. **你看到的問題**（例如：太暗、太亮、星點拖線、噪點多、對焦模糊）
4. **環境狀況**（有無月光、光害程度、是否有雲）

範例訊息：
> 「我用主鏡頭 35mm，ISO 3200，快門 15 秒，但畫面很暗幾乎看不到銀河，現場沒有月光，天空看起來很乾淨。」

---

## 參考資料

| 來源 | 內容 |
|------|------|
| [GSMArena - Vivo X300 Ultra 規格](https://www.gsmarena.com/vivo_x300_ultra_5g-14388.php) | 鏡頭焦距、光圈、感測器尺寸 |
| [ViewBug - Astrophotography Settings Cheat Sheet](https://viewbug.com/knowledge/astrophotography-camera-settings) | ISO 3200 起步、500 法則、白平衡 3800–4000K、RAW 格式 |
| [vivo 社群 - Milky Way 拍攝分享](https://bbs.vivo.com/in/thread/175210) | vivo 手機實拍：快門 25s、ISO 1600–3200、手動對焦無限遠 |
| [Milky Way Planner - Phone Photography](https://www.milkywayplanner.com/intro-to-astrophotography/milky-way-photography-phone) | 手機星空攝影限制與建議、暗空重要性 |
| [Milky Way Planner - Panorama](https://www.milkywayplanner.com/intro-to-astrophotography/milky-way-panorama) | 35mm 拼接需 10–12 張、30–40% 重疊、5–8 分鐘完成 |
| [PetaPixel - NPF Rule](https://petapixel.com/2017/04/07/npf-rule-formula-sharp-star-photos-every-time/) | NPF 精確計算公式 |
| [Photography Life - Night Sky Stacking](https://photographylife.com/night-sky-image-stacking) | 堆疊降噪原理與效果 |
| [PhotoPills - Milky Way Photography Settings](https://photopills.com/articles/milky-way-photography-settings) | ISO 3200–6400、NPF 法則、白平衡 3900K |
| [The Image Guild - Night Sky Photography Guide](https://www.theimageguild.com/post/how-to-photograph-milky-way-guide) | 高 ISO 堆疊法：ISO 12800 + 短曝 + 25 張堆疊 |
| [Capture the Atlas - Milky Way Photography](https://capturetheatlas.com/how-to-photograph-the-milky-way) | ISO 3200–6400、f/2.8、10–25s |
| [AstroBackyard - How to Photograph Milky Way](https://astrobackyard.com/how-to-photograph-milky-way/) | 單張 20s ISO 3200 實拍範例 |
| [Picture Correct - Milky Way Panorama Tutorial](https://www.picturecorrect.com/milky-way-panorama-photo-tutorial/) | 全景拼接：20s、ISO 3200–6400、15° 旋轉 |

---

*Content was rephrased for compliance with licensing restrictions.*

*祝拍攝順利，銀河入鏡！* 🌌
