# -*- coding: utf-8 -*-
import glob
import json
import os
import re
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

print("=== 檢查各檔案中 ans 與 options 的格式比對 ===")

for filename in ["chinese6_midterm.html", "chinese6_final.html", "chinese6_curriculum.html", "chinese3_curriculum.html", "social6_curriculum.html"]:
    with open(filename, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()
    
    # 提取第一題的 q, options, ans
    q_match = re.search(r'["\']q["\']\s*:\s*["\'](.*?)["\']', content)
    opt_match = re.search(r'["\']options["\']\s*:\s*(\[.*?\])', content)
    ans_match = re.search(r'["\']ans["\']\s*:\s*["\'](.*?)["\']', content)
    
    print(f"\n[{filename}]")
    if q_match and opt_match and ans_match:
        print("  q:", q_match.group(1)[:40])
        print("  options:", opt_match.group(1)[:60])
        print("  ans:", ans_match.group(1))
    else:
        print("  (未找到標準 q/options/ans 結構)")
