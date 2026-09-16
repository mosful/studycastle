# -*- coding: utf-8 -*-
import glob
import re
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

html_files = sorted(glob.glob("*.html"))

print("=== 掃描所有 HTML 檔案中的彈窗與 Alert 呼叫 ===")
for f in html_files:
    with open(f, "r", encoding="utf-8", errors="ignore") as fp:
        c = fp.read()
    alerts = re.findall(r'alert\s*\((.*?)\)', c, re.DOTALL)
    confirms = re.findall(r'confirm\s*\((.*?)\)', c, re.DOTALL)
    modals = re.findall(r'id=["\']([^"\']*(?:modal|dialog|popup)[^"\']*)["\']', c, re.I)
    
    if alerts or confirms or modals:
        print(f"\n[{f}]")
        if alerts:
            print(f"  🚨 發現 {len(alerts)} 個 alert() 呼叫:")
            for a in alerts[:3]:
                print(f"     -> {a.strip()[:100]}")
        if confirms:
            print(f"  ⚠️ 發現 {len(confirms)} 個 confirm() 呼叫:")
            for cf in confirms[:3]:
                print(f"     -> {cf.strip()[:100]}")
        if modals:
            print(f"  ℹ️ 現有 modal ID: {modals}")
