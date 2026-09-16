# -*- coding: utf-8 -*-
import glob
import json
import os
import re
import sys
from collections import Counter

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

html_files = sorted(glob.glob("*.html"))
print(f"=== 深入檢測全站 {len(html_files)} 個 HTML 中的題目與答案分佈 ===\n")

for h in html_files:
    if h in ["index.html", "portal.html"]:
        continue
    with open(h, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()

    # 檢查是否有測驗關鍵字
    if not any(k in content for k in ["options", "quiz", "Question", "ans", "answer"]):
        continue

    # 搜尋題目陣列
    # 找 options: [...]
    opts_matches = re.findall(r'options\s*:\s*(\[[^\]]+\])', content)
    ans_matches = re.findall(r'(?:ans|answer|correctAnswer|correctIndex)\s*:\s*([^,\}\n]+)', content)
    
    has_shuffle = bool(re.search(r'shuffle|Math\.random\s*\(\)\s*-\s*0\.5|sort\s*\(\s*\(\s*\)\s*=>\s*Math\.random', content, re.I))

    # 提取題目與答案判定方式
    print(f"📄 檔案: {h} (選項組數: {len(opts_matches)}, 答案項數: {len(ans_matches)}, 含洗牌函數: {has_shuffle})")
    
    if ans_matches:
        cleaned_ans = [a.strip().strip("'\"") for a in ans_matches]
        c = Counter(cleaned_ans)
        top_answers = c.most_common(5)
        print(f"   答案分佈: {top_answers}")
        if len(cleaned_ans) > 0 and (top_answers[0][0] in ["0", "A"] and top_answers[0][1] / len(cleaned_ans) > 0.6):
            print(f"   ⚠️ 警告: 此檔案答案極度偏向第 1 項 (0 或 A)！比例: {top_answers[0][1]}/{len(cleaned_ans)}")
        elif len(cleaned_ans) > 0 and len(opts_matches) > 0:
            # 檢查是否 ans 與 options[0] 經常相同
            pass
