# -*- coding: utf-8 -*-
"""
驗證所有 HTML 檔案有效性
"""

import sys
import os
sys.stdout.reconfigure(encoding='utf-8')

files_to_check = [
    "prime.html",
    "fraction-division.html",
    "decimal-division.html",
    "circle-area.html",
    "index.html",
    "portal.html"
]

all_passed = True

for fname in files_to_check:
    path = os.path.join("c:/Code/StudyCastle", fname)
    if not os.path.exists(path):
        print(f"[FAIL] Missing file: {fname}")
        all_passed = False
        continue
    
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # 檢查基本的 HTML 結構
    if "<!DOCTYPE html>" not in content or "</html>" not in content:
        print(f"[FAIL] Invalid HTML structure in {fname}")
        all_passed = False
    else:
        print(f"[OK] {fname} ({len(content):,} chars) validated successfully.")

if all_passed:
    print("\nALL HTML FILES CHECKED & PASSED!")
