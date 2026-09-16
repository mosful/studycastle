# -*- coding: utf-8 -*-
import glob
import json
import os
import re
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

print("=================================================================")
print("全站測驗與題庫選項渲染機制深入診斷")
print("=================================================================")

# 1. 檢查 3 個 JSON
for jf in ["chinese3_full_curriculum_database.json", "chinese6_full_curriculum_database.json", "social6_full_curriculum_database.json"]:
    with open(jf, "r", encoding="utf-8") as fp:
        data = json.load(fp)
    total_q = 0
    ans_at_0 = 0
    for item in data:
        q_list = item.get("exam") or item.get("quiz") or []
        for q in q_list:
            total_q += 1
            opts = q.get("options", [])
            ans = q.get("ans")
            # 如果 ans 是字母 A, B, C, D
            if ans in ["A", "B", "C", "D"]:
                if ans == "A":
                    ans_at_0 += 1
            elif opts and ans in opts:
                if opts.index(ans) == 0:
                    ans_at_0 += 1
    print(f"[JSON] {jf}: 總題數={total_q}, 答案在第1項(0/A)的數量={ans_at_0} ({ans_at_0/total_q*100:.1f}%)" if total_q else f"[JSON] {jf}: 0 題")

# 2. 檢查所有 HTML
html_files = sorted(glob.glob("*.html"))
for h in html_files:
    if h in ["index.html", "portal.html"]:
        continue
    with open(h, "r", encoding="utf-8", errors="ignore") as fp:
        content = fp.read()
    
    # 尋找與選項相關的邏輯
    # 檢查是否含有選項按鈕生成
    opt_renders = re.findall(r'(\.options\s*\.\s*(?:map|forEach)[\s\S]*?\{[\s\S]*?\})', content)
    opt_grids = re.findall(r'(\bopts\s*\.\s*(?:map|forEach)[\s\S]*?\{[\s\S]*?\})', content)
    
    has_shuffle = "shuffle" in content.lower() or "math.random" in content.lower()
    
    if opt_renders or opt_grids or "options" in content:
        print(f"\n[HTML] {h}:")
        # 看看選項陣列如何產生
        matches = re.findall(r'(let\s+opts\s*=[\s\S]*?;|const\s+opts\s*=[\s\S]*?;|opts\s*=[\s\S]*?;)', content)
        for m in matches[:3]:
            # 清理過長的內容
            clean_m = " ".join(m.split())[:120]
            print(f"   opts定義: {clean_m}")
        
        # 看看選項點擊與答案比對邏輯
        check_ans_matches = re.findall(r'((?:checkAnswer|grade|pick|check|click)[\s\S]*?\{[\s\S]*?\})', content, re.I)
        # 找按鈕綁定 onclick
        onclicks = re.findall(r'onclick=[\'"]([^\'"]*?(?:check|pick|ans|opt|select)[^\'"]*?)[\'"]', content, re.I)
        if onclicks:
            print(f"   選項點擊函式範例: {list(set(onclicks))[:3]}")
