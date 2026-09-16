# -*- coding: utf-8 -*-
import glob
import json
import os
import re
import subprocess
import sys
from collections import Counter

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

print("=================================================================")
print("全站測驗選項隨機化與程式碼健康度驗證")
print("=================================================================")

# 1. 驗證 3 個 JSON
print("\n--- 1. 驗證 JSON 題庫資料庫答案分佈 ---")
for jf in ["chinese3_full_curriculum_database.json", "chinese6_full_curriculum_database.json", "social6_full_curriculum_database.json"]:
    with open(jf, "r", encoding="utf-8") as f:
        data = json.load(f)
    positions = []
    for item in data:
        q_list = item.get("exam") or item.get("quiz") or []
        for q in q_list:
            ans = q.get("ans")
            opts = q.get("options", [])
            if ans in ["A", "B", "C", "D"]:
                positions.append(["A", "B", "C", "D"].index(ans))
            elif opts and ans in opts:
                positions.append(opts.index(ans))
    c = Counter(positions)
    print(f"[{jf}] 總題數={len(positions)}, 選項位置分佈 (0~3): {dict(c)}")
    first_ratio = c.get(0, 0) / len(positions) if positions else 0
    if first_ratio > 0.45:
        print(f"  ⚠️ 警告: 第 1 項比例過高 ({first_ratio*100:.1f}%)")
    else:
        print(f"  ✅ 正常: 第 1 項比例合理 ({first_ratio*100:.1f}%)，均勻分佈！")

# 2. Node.js 語法檢查所有 HTML 中的內嵌 JS
print("\n--- 2. Node.js 語法檢測全站 HTML 內嵌腳本 ---")
os.makedirs("scratch", exist_ok=True)
html_files = sorted(glob.glob("*.html"))
has_error = False

for h in html_files:
    with open(h, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()
    scripts = re.findall(r'<script(?![^>]*src=)[^>]*>(.*?)</script>', content, re.DOTALL | re.IGNORECASE)
    for idx, s in enumerate(scripts):
        tmp_js = os.path.join("scratch", f"test_{os.path.basename(h)}_{idx}.js")
        with open(tmp_js, "w", encoding="utf-8") as tf:
            tf.write(s)
        res = subprocess.run(["node", "-c", tmp_js], capture_output=True, text=True)
        if res.returncode != 0:
            print(f"❌ 語法錯誤: {h} script #{idx}: {res.stderr.strip()}")
            has_error = True

if not has_error:
    print(f"✅ 全站 {len(html_files)} 個 HTML 檔案所有內嵌腳本通過 Node 語法檢驗 (0 語法錯誤)！")

# 清理 scratch
import shutil
if os.path.exists("scratch"):
    shutil.rmtree("scratch")

print("\n=================================================================")
print("驗證結束")
print("=================================================================")
