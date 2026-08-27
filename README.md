# 🏰 快樂學習冒險城堡 (Joyful Learning Adventure Castle)

專為國小與國中學生打造的互動式學習遊戲樂園！透過豐富的視覺主題、關卡式闖關冒險、即時答題回饋與成就激勵機制，讓孩子在趣味遊戲中輕鬆掌握核心數學與各學科知識。

🔗 **線上體驗入口**：[mosful.github.io/portal.html](https://mosful.github.io/portal.html)

---

## 🎯 專案特色與架構重點

1. **多載具無縫操作**：
   - 全面支援 **iPad（平板）、智慧型手機（iOS/Android）與桌上型電腦**。
   - 所有點擊元件符合行動觸控準則（最小高度 48px~56px、`touch-action: manipulation` 消除點擊延遲）。
2. **沉浸式遊戲化學習**：
   - 採用關卡制進階闖關、計時倒數挑戰、連擊（Combo）加分、三星成就評分、Confetti 煙火特效與本機最高分紀錄。
3. **無伺服器架構（Serverless / Static Web App）**：
   - 純前端技術建置，無需後端伺服器，直接透過 GitHub Pages 零成本快速部署。
4. **社群交流與用戶反饋系統**：
   - **Giscus 冒險家公開留言板**：整合 GitHub Discussions，支援深淺色主題、表情符號互動與學習心得分享。
   - **免登入意見反饋信箱**：提供右下角快速彈窗，讓國小學生與家長無需 GitHub 帳號即可一鍵回報 Bug 或許願新單元。
5. **真實雲端去重計數器與訪客 IP 顯示**：
   - 整合 **不蒜子 (Busuanzi) 雲端去重計數器**（同 IP 當天只計 1 次 UV，防重複刷新累加），並即時查詢訪客真實 IP。

---

## 📚 目前已上線冒險單元 (10 大主題)

### 🧮 國小三年級上學期數學（南一版課本範圍 P.1 ~ P.117）
| 單元 | 遊戲名稱 | 主題特色 | 檔案名稱 |
|---|---|---|---|
| **第①單元** | **數到10000 宇宙冒險** 🚀 | 萬以內位值辨認（千/百/十/個位）、數字合成、大小比較 | [math3_numbers.html](file:///c:/Code/mosful.github.io/math3_numbers.html) |
| **第②單元** | **四位數加減法 城堡大冒險** 🏰 | 四位數直式計算、無進借位至多次進借位混合挑戰 | [math3_addition.html](file:///c:/Code/mosful.github.io/math3_addition.html) |
| **第③單元** | **乘法小英雄 大冒險** 🦸 | 二位數×一位數乘法、乘法算式與積的速算闖關 | [math3_multiplication.html](file:///c:/Code/mosful.github.io/math3_multiplication.html) |
| **第④單元** | **幾毫米 測量小達人** 📏 | 毫米認識、公分/公尺/毫米長度單位互換與量感建立 | [math3_measurement.html](file:///c:/Code/mosful.github.io/math3_measurement.html) |
| **第⑤單元** | **角與幾何形狀 探索家** 📐 | 角與頂點邊識別、直角判斷、正方形與長方形幾何性質 | [math3_geometry.html](file:///c:/Code/mosful.github.io/math3_geometry.html) |

---

### 🌟 國小二年級 / 五六年級數學單元
| 年級/領域 | 遊戲名稱 | 學習重點 | 檔案名稱 |
|---|---|---|---|
| **低年級** | **大耳狗九九乘法冒險** 🐶 | 2~9 各段乘法記憶、混合練習與生活素養應用題 | [2mathgame.html](file:///c:/Code/mosful.github.io/2mathgame.html) |
| **中高年級** | **9是強 數學大冒險** 🚂 | 四則混合運算（先乘除後加減、括號優先）與火車冒險 | [5mathgame.html](file:///c:/Code/mosful.github.io/5mathgame.html) |
| **高年級** | **質數大航海 尋寶記** 🧭 | 質數與合數判斷、短除法、最大公因數(GCD)與最小公倍數(LCM) | [prime.html](file:///c:/Code/mosful.github.io/prime.html) |
| **高年級** | **分數廚師 大挑戰** 🍕 | 最簡分數、整數÷分數、分數÷分數、倒數與乘除互換 | [fraction-division.html](file:///c:/Code/mosful.github.io/fraction-division.html) |
| **高年級** | **小數太空探險** 🚀 | 整數÷小數、小數÷小數、乘以10倍數魔法、四捨五入求概數 | [decimal-division.html](file:///c:/Code/mosful.github.io/decimal-division.html) |

---

## 🛠️ 技術棧 (Technology Stack)

- **核心架構**：語意化 HTML5、原生 CSS3（現代 CSS Custom Properties、Flexbox、CSS Grid、Glassmorphism 玻璃擬態設計）。
- **邏輯控制**：原生 JavaScript (ES6+)、`async/await` 非同步資料處理、Web Storage API (`localStorage`)。
- **字型與排版**：Google Fonts（`Fredoka`, `Baloo 2`, `Noto Sans TC`）。
- **動態特效**：[canvas-confetti](https://www.jsdelivr.com/package/npm/canvas-confetti) 向量彩帶煙火特效。
- **雲端計數與訪客統計**：
  - **不蒜子 (Busuanzi)**：雲端 UV 去重訪客統計（同 IP 當日計算一次）。
  - **ipify API**：即時安全獲取訪客外網 IP。

---

## 📂 檔案目錄結構

```text
mosful.github.io/
├── index.html                  # 個人首頁入口
├── portal.html                 # 🏰 學習樂園總覽入口網站 (支援搜尋、分類、收藏與計數器)
├── 2mathgame.html              # 二年級：大耳狗九九乘法
├── 5mathgame.html              # 中高年級：9是強四則運算大冒險
├── math3_numbers.html          # 三年級①：數到10000 宇宙冒險
├── math3_addition.html         # 三年級②：四位數加減法 城堡大冒險
├── math3_multiplication.html   # 三年級③：乘法小英雄 大冒險
├── math3_measurement.html      # 三年級④：幾毫米 測量小達人
├── math3_geometry.html         # 三年級⑤：角與幾何形狀 探索家
├── prime.html                  # 高年級：質數大航海 (質因數/短除法/GCD/LCM)
├── fraction-division.html      # 高年級：分數廚師大挑戰 (分數除法/最簡分數)
├── decimal-division.html       # 高年級：小數太空探險 (小數除法/概數)
└── README.md                   # 專案說明文件
```

---

## 🚀 本地開發與使用

本專案為純靜態網頁，無需安裝複雜依賴或建置工具：

1. **直接開啟**：使用任一瀏覽器直接開啟 `portal.html` 即可體驗。
2. **搭配本機伺服器（推薦）**：
   ```bash
   # 使用 Python 快速啟動本地伺服器
   python -m http.server 8000
   ```
   瀏覽器造訪 `http://localhost:8000/portal.html` 即可。

---

## 📄 版權聲明 (License)

© 2026 快樂學習冒險城堡 | 設計用於促進學生趣味學習與奠定學科基礎。
全站頁面專為各型 iPad、Android 平板、智慧型手機與電腦主流瀏覽器最佳化。
