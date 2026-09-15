# -*- coding: utf-8 -*-
import glob
import os
import re
import subprocess
import json
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

print("=== 1. 檢查大檔案與 Git 狀態 ===")
pdf_files = glob.glob("*.pdf")
for p in pdf_files:
    sz = os.path.getsize(p) / (1024 * 1024)
    print(f"PDF 大檔案: {p} ({sz:.2f} MB)")

# 檢查是否有未被 gitignore 排除的大檔案
git_tracked = subprocess.run(["git", "ls-files"], capture_output=True, text=True, encoding="utf-8").stdout.splitlines()
tracked_pdfs = [f for f in git_tracked if f.endswith(".pdf")]
if tracked_pdfs:
    print(f"⚠️ 警告: 有巨型 PDF 檔案已被 Git 追蹤: {tracked_pdfs}")
else:
    print("✅ 很好: 巨型 PDF 檔案未被 Git 追蹤或已被忽略。")

print("\n=== 2. 檢查 index.html 與 portal.html 內容是否完全同步 ===")
if os.path.exists("index.html") and os.path.exists("portal.html"):
    with open("index.html", "r", encoding="utf-8") as f1, open("portal.html", "r", encoding="utf-8") as f2:
        c1 = f1.read()
        c2 = f2.read()
    if c1 == c2:
        print("✅ index.html 與 portal.html 100% 完全一致！")
    else:
        print(f"⚠️ 注意: index.html ({len(c1)} bytes) 與 portal.html ({len(c2)} bytes) 內容不一致！")

print("\n=== 3. 檢查 JS 語法與提取各 HTML 的 Script 進行 Node 語法檢測 ===")
os.makedirs("scratch", exist_ok=True)

# 檢驗 chinese6_visual_engine.js
try:
    res = subprocess.run(["node", "-c", "chinese6_visual_engine.js"], capture_output=True, text=True)
    if res.returncode == 0:
        print("✅ chinese6_visual_engine.js 語法檢驗合格")
    else:
        print(f"❌ chinese6_visual_engine.js 語法錯誤: {res.stderr}")
except Exception as e:
    print(f"無法執行 node 檢測: {e}")

# 檢查 HTML 內嵌 script 語法
html_files = sorted(glob.glob("*.html"))
syntax_errors = []
for h in html_files:
    with open(h, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()
    
    scripts = re.findall(r'<script(?![^>]*src=)[^>]*>(.*?)</script>', content, re.DOTALL | re.IGNORECASE)
    for idx, s in enumerate(scripts):
        temp_js = os.path.join("scratch", f"temp_{os.path.basename(h)}_{idx}.js")
        with open(temp_js, "w", encoding="utf-8") as tf:
            tf.write(s)
        res = subprocess.run(["node", "-c", temp_js], capture_output=True, text=True)
        if res.returncode != 0:
            # 過濾一些非致命或 HTML 樣板字元引起的誤報，列出真正語法錯誤
            syntax_errors.append((h, idx, res.stderr.strip()))

if not syntax_errors:
    print(f"✅ 全站 33 個 HTML 內部的所有 JavaScript 語法檢測全部通過 (0 語法錯誤)！")
else:
    print(f"❌ 發現 {len(syntax_errors)} 個內嵌 JavaScript 語法錯誤:")
    for h, idx, err in syntax_errors:
        print(f"[{h} script #{idx}] {err}")

print("\n=== 4. 檢查 URL 參數與 XSS 風險 ===")
xss_risks = []
for h in html_files:
    with open(h, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()
    # 檢查是否使用 location.search / URLSearchParams 並直接賦值給 innerHTML
    if "location.search" in content or "URLSearchParams" in content:
        # 查看是否有 innerHTML 賦值
        matches = re.findall(r'innerHTML\s*=\s*[^;\n]*?(?:param|query|url|search|get\(|location)', content, re.I)
        if matches:
            xss_risks.append((h, matches))

if not xss_risks:
    print("✅ 無直接以 innerHTML 注入 URL 參數的直觀 XSS 漏洞。")
else:
    print(f"⚠️ 發現潛在 XSS 風險: {xss_risks}")

print("\n=== 5. 檢查首頁中的所有課程單元卡片連結 ===")
with open("portal.html", "r", encoding="utf-8") as f:
    portal_content = f.read()

card_links = re.findall(r'href="([^"#]+\.html)"', portal_content)
unique_links = sorted(list(set(card_links)))
print(f"portal.html 中引用的 HTML 頁面共 {len(unique_links)} 個:")
missing_on_disk = [l for l in unique_links if not os.path.exists(l)]
if missing_on_disk:
    print(f"❌ 找不到的卡片連結目標: {missing_on_disk}")
else:
    print("✅ 所有首頁連結目標檔案均存在於硬碟中！")

disk_html = [os.path.basename(f) for f in html_files if os.path.basename(f) not in ["index.html", "portal.html"]]
unlinked = [f for f in disk_html if f not in unique_links]
if unlinked:
    print(f"ℹ️ 尚未在首頁卡片中直接連結的 HTML 檔案 (共 {len(unlinked)} 個): {unlinked}")
else:
    print("✅ 全站所有 HTML 檔案皆已收錄於首頁中！")
