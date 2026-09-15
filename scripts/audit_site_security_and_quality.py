# -*- coding: utf-8 -*-
import glob
import os
import re
import json

html_files = sorted(glob.glob("*.html"))
issues = []
stats = {
    "total_html": len(html_files),
    "missing_favicon": [],
    "missing_viewport": [],
    "missing_charset": [],
    "missing_title": [],
    "http_resources": [],
    "unsafe_target_blank": [],
    "missing_local_src": [],
    "missing_local_href": [],
    "no_home_button": [],
    "eval_or_document_write": [],
    "inner_html_risks": []
}

for html in html_files:
    with open(html, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()
    
    # 1. 基本 HTML 結構
    if "charset" not in content.lower():
        stats["missing_charset"].append(html)
    if "viewport" not in content.lower():
        stats["missing_viewport"].append(html)
    if "<title>" not in content.lower():
        stats["missing_title"].append(html)
    if not re.search(r'rel=["\'](?:shortcut )?icon["\']', content, re.I):
        stats["missing_favicon"].append(html)
        
    # 2. 安全性檢測：HTTP 明文資源
    http_links = re.findall(r'(?:src|href)=["\'](http://[^"\']+)["\']', content, re.I)
    if http_links:
        stats["http_resources"].append((html, http_links))
        
    # 3. 安全性檢測：target="_blank" 無 noopener
    target_blanks = re.findall(r'<a\s+[^>]*target=["\']_blank["\'][^>]*>', content, re.I)
    unsafe_tb = [t for t in target_blanks if "noopener" not in t.lower()]
    if unsafe_tb:
        stats["unsafe_target_blank"].append((html, len(unsafe_tb)))

    # 4. 安全性檢測：eval, document.write
    if re.search(r'\beval\s*\(', content):
        stats["eval_or_document_write"].append((html, "eval"))
    if "document.write" in content:
        stats["eval_or_document_write"].append((html, "document.write"))

    # 5. 資源有效性：src 與 href 本地連結
    srcs = re.findall(r'src=["\']([^"\']+)["\']', content, re.I)
    for s in srcs:
        if not s.startswith("http") and not s.startswith("data:") and not s.startswith("//") and not s.startswith("#"):
            clean_s = s.split("?")[0].split("#")[0]
            if not os.path.exists(clean_s):
                stats["missing_local_src"].append((html, clean_s))

    hrefs = re.findall(r'<a\s+[^>]*href=["\']([^"\']+)["\']', content, re.I)
    for h in hrefs:
        if not h.startswith("http") and not h.startswith("data:") and not h.startswith("//") and not h.startswith("#") and not h.startswith("mailto:") and not h.startswith("javascript:") and not "${" in h:
            clean_h = h.split("?")[0].split("#")[0]
            if not os.path.exists(clean_h):
                stats["missing_local_href"].append((html, clean_h))

    # 6. 使用者體驗：回到首頁導覽按鈕
    if html not in ["index.html", "portal.html"]:
        has_portal = ("portal.html" in content) or ("index.html" in content)
        if not has_portal:
            stats["no_home_button"].append(html)

print("="*60)
print(f"全站掃描報告 - 共檢測 {stats['total_html']} 個 HTML 檔案")
print("="*60)

for key, val in stats.items():
    if key == "total_html":
        continue
    count = len(val)
    print(f"- {key}: {count} 項")
    if count > 0 and count <= 15:
        for item in val:
            print(f"    -> {item}")
    elif count > 15:
        print(f"    -> 前 5 項: {val[:5]}")

print("="*60)
