# -*- coding: utf-8 -*-
import os
import re
import urllib.parse
import sys

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = r"c:\Code\StudyCastle"
FAVICON_SVG_PATH = os.path.join(BASE_DIR, "favicon.svg")

with open(FAVICON_SVG_PATH, "r", encoding="utf-8") as f:
    svg_raw = f.read().strip()

# 製作 URL 編碼的 Data URI，即使瀏覽器不載入外部檔案也能直接解析
svg_encoded = urllib.parse.quote(svg_raw)
data_uri = f"data:image/svg+xml,{svg_encoded}"

FAVICON_TAGS = f'''    <!-- Favicon 網站圖示 -->
    <link rel="icon" type="image/svg+xml" href="favicon.svg">
    <link rel="alternate icon" type="image/svg+xml" href="{data_uri}">
    <link rel="apple-touch-icon" href="favicon.svg">'''

html_files = [f for f in os.listdir(BASE_DIR) if f.endswith(".html")]
print(f"找到 {len(html_files)} 個 HTML 檔案，準備加入 Favicon...")

updated_count = 0
for hf in html_files:
    file_path = os.path.join(BASE_DIR, hf)
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # 檢查是否已包含 favicon
    if "rel=\"icon\"" in content or "rel='icon'" in content:
        # 替換既有 favicon 標籤
        content = re.sub(r'<link\s+[^>]*rel=[\'"](?:alternate\s+)?icon[\'"][^>]*>', '', content, flags=re.IGNORECASE)

    # 在 <title> 標籤後面或 <head> 後面插入
    if "<title>" in content:
        content = re.sub(r'(<title>.*?</title>)', r'\1\n' + FAVICON_TAGS, content, count=1, flags=re.DOTALL)
    elif "<head>" in content:
        content = content.replace("<head>", "<head>\n" + FAVICON_TAGS, 1)
    else:
        continue

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    updated_count += 1
    print(f"✅ 已更新 Favicon：{hf}")

print(f"\n全部完成！共更新 {updated_count} 個網頁的 Favicon！")
