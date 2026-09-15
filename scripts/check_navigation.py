# -*- coding: utf-8 -*-
import glob
import os
import re
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

html_files = sorted(glob.glob("*.html"))
nav_report = []

for h in html_files:
    if h in ["index.html", "portal.html"]:
        continue
    with open(h, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()
    
    # 檢查是否有連至 portal.html 或 index.html 的連結
    home_matches = re.findall(r'href=["\'](portal\.html|index\.html)["\']', content, re.I)
    if not home_matches:
        # 有無文字按鈕用 JS 跳轉
        has_js_nav = "portal.html" in content or "index.html" in content
        if has_js_nav:
            nav_report.append((h, "⚠️ 僅有 JS 變數提及，無標準 <a> 標籤"))
        else:
            nav_report.append((h, "❌ 缺少返回首頁連結"))
    else:
        nav_report.append((h, f"✅ 正常 (返回連結 {len(home_matches)} 處)"))

print(f"=== 課程頁面返回首頁導覽檢查 (共 {len(nav_report)} 個頁面) ===")
for h, res in nav_report:
    print(f"{h:32}: {res}")
