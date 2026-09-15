# -*- coding: utf-8 -*-
path = r"C:\Users\MossLin林建良\.gemini\GEMINI.md"

with open(path, "r", encoding="utf-8") as f:
    text = f.read()

target = "- 使用者已給予完整執行權限：可以直接修改程式碼、建立檔案與執行各項指令，不需每次詢問確認。"
replacement = """- 使用者已給予完整執行權限：可以直接修改程式碼、建立檔案與執行各項指令，不需每次詢問確認。
- 完全自主執行模式（免詢問）：
  1. 嚴禁呼叫 ask_question 工具，嚴禁詢問是非題或選項讓使用者挑選。
  2. 遇到任何決策、套件選擇或實作方案，一律由你自主評估並直接採取業界最佳方案執行到底。
  3. 建立或更新 implementation plan 後，一律立即自動接續執行，嚴禁停下來等待使用者核准。
  4. 執行過程中若遇報錯，一律自主排查、修復並重試，直到任務完全交付為止。"""

if target in text:
    text = text.replace(target, replacement)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    print("成功更新 GEMINI.md！")
else:
    print("目標文字未找到！")
