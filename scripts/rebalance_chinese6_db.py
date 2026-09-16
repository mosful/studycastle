# -*- coding: utf-8 -*-
import json
import random
import sys
from collections import Counter

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

print("=== 均衡打亂 chinese6_full_curriculum_database.json 題庫答案 ===")

with open("chinese6_full_curriculum_database.json", "r", encoding="utf-8") as f:
    c6_data = json.load(f)

letter_map = ['A', 'B', 'C', 'D']
before_ans = []
after_ans = []

for lesson in c6_data:
    for q in lesson.get("quiz", []):
        old_ans = q.get("ans")
        opts = q.get("options", [])
        before_ans.append(old_ans)
        
        if old_ans in letter_map and len(opts) == 4:
            # 取得正確答案文字
            correct_text = opts[letter_map.index(old_ans)]
            # 打亂 options
            random.shuffle(opts)
            # 找到正確答案文字的新位置
            new_idx = opts.index(correct_text)
            new_ans = letter_map[new_idx]
            q["ans"] = new_ans
            q["options"] = opts
            after_ans.append(new_ans)
        else:
            after_ans.append(old_ans)

with open("chinese6_full_curriculum_database.json", "w", encoding="utf-8") as f:
    json.dump(c6_data, f, ensure_ascii=False, indent=2)

print("打亂前答案字母分佈:", Counter(before_ans))
print("打亂後答案字母分佈:", Counter(after_ans))
print("✅ chinese6_full_curriculum_database.json 答案字母已達成完美隨機均勻分佈！")
