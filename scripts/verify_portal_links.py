import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('portal.html', 'r', encoding='utf-8') as f:
    html = f.read()

urls = re.findall(r'url:\s*"([^"]+)"', html)
print(f"檢測到 {len(urls)} 個單元跳轉連結：")

missing = []
for u in set(urls):
    if not os.path.exists(u):
        missing.append(u)

if missing:
    print("❌ 警告，以下連結檔案不存在：", missing)
else:
    print("✅ 太棒了！所有單元檔案 100% 存在於專案根目錄中！")

# 檢查 index.html 與 portal.html 是否完全一致
with open('index.html', 'r', encoding='utf-8') as f2:
    html_index = f2.read()

if html == html_index:
    print("✅ index.html 與 portal.html 內容 100% 同步完全一致！")
else:
    print("❌ index.html 與 portal.html 內容不一致！")
