# Repository Guidelines

## 專案結構與模組配置

本專案是以原生 HTML、CSS 與 JavaScript 建立的靜態學習網站，無前端框架或編譯產物。根目錄的 `index.html` 與 `portal.html` 是同步入口；`chinese*_curriculum.html`、`math3_*.html`、`social6_curriculum.html` 與各遊戲頁面各自封裝畫面和互動。核心課程資料存放於 `*_full_curriculum_database.json`，共用六年級國語視覺邏輯位於 `chinese6_visual_engine.js`。維護、產生及驗證工具集中在 `scripts/`。`archive/`、`scratch/`、`.venv/` 與教材 PDF 屬本機素材或中介產物，不應提交。

## 建置、測試與開發指令

專案不需建置。請在儲存庫根目錄執行：

```powershell
uv run python -m http.server 8000
uv run python scripts/verify_html.py
uv run python scripts/verify_portal_links.py
uv run python scripts/verify_chinese6_system.py
uv run python scripts/verify_all_quiz_randomization.py
```

第一個指令於 `http://localhost:8000/portal.html` 啟動本機站台；其餘指令依序檢查 HTML 結構、入口連結與雙首頁同步、六年級國語系統及題目選項隨機化。若環境未安裝 `uv`，可將 `uv run python` 改為 `.venv\Scripts\python.exe` 或 `python`。

## 程式風格與命名規範

沿用既有格式：HTML、CSS、JavaScript 使用 4 空格縮排，Python 遵循 PEP 8，檔案皆採 UTF-8。頁面檔名使用小寫 kebab-case（如 `fraction-division.html`）或既有的科目加年級 snake_case（如 `math3_numbers.html`）；Python 函式與變數使用 snake_case，JavaScript 使用 camelCase。介面文案與註解使用繁體中文台灣用語。修改入口頁時，必須同步更新 `index.html` 與 `portal.html`。

## 測試準則

目前沒有獨立測試框架或覆蓋率門檻。依變更範圍執行相關 `scripts/verify_*.py`，並在桌面與手機寬度手動確認導覽、題目作答、Modal、音效與 `localStorage` 降級行為。新增驗證腳本時採 `verify_<功能>.py` 命名，失敗時應回傳非零結束碼。

## Commit 與 Pull Request 準則

近期提交以簡潔的繁體中文祈使句描述「變更範圍：具體成果」，例如 `全站測驗選項隨機打亂重構：修正答案固定問題`；亦可使用 `feat:`、`fix:` 等 Conventional Commit 前綴。每個 commit 聚焦單一主題。Pull Request 須說明目的、受影響頁面、驗證指令與結果；視覺變更附桌面及手機截圖，資料或題庫調整則註明來源與抽查方式。不得提交教材 PDF、憑證、Token 或個人資料。
