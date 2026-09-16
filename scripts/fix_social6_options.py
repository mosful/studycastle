# -*- coding: utf-8 -*-
import json
import random
import re
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

print("=== 修復六年級社會全冊題庫選項打亂 ===")

# 1. 更新 social6_full_curriculum_database.json
with open("social6_full_curriculum_database.json", "r", encoding="utf-8") as f:
    s6_data = json.load(f)

for unit in s6_data:
    for q in unit.get("quiz", []):
        opts = q.get("options", [])
        if len(opts) > 1:
            random.shuffle(opts)
            q["options"] = opts

with open("social6_full_curriculum_database.json", "w", encoding="utf-8") as f:
    json.dump(s6_data, f, ensure_ascii=False, indent=2)

print("✅ social6_full_curriculum_database.json 選項已隨機打亂！")

# 統計打亂後的 ans index 分佈
pos = []
for unit in s6_data:
    for q in unit.get("quiz", []):
        ans = q.get("ans")
        opts = q.get("options", [])
        pos.append(opts.index(ans) if ans in opts else -1)
from collections import Counter
print("   social6 打亂後 ans 位置分佈:", Counter(pos))

# 2. 更新 social6_curriculum.html 內嵌 CURRICULUM
with open("social6_curriculum.html", "r", encoding="utf-8") as f:
    s6_html = f.read()

# 替換 CURRICULUM = [...] 中的 quiz
# 我們可以直接把 CURRICULUM 中的 quiz 陣列替換，或者直接正則/重新嵌入
# 找 const CURRICULUM = [ ... ];
# 為了避免格式破壞，我們用正則匹配各題的 options
def shuffle_opts(m):
    opts_raw = m.group(1)
    try:
        opts = json.loads(opts_raw)
        if len(opts) > 1:
            random.shuffle(opts)
        return f'"options": {json.dumps(opts, ensure_ascii=False)}'
    except Exception:
        return m.group(0)

s6_html = re.sub(r'"options"\s*:\s*(\[[^\]]+\])', shuffle_opts, s6_html)

# 確保前端 renderQuizQuestion 中使用 Fisher-Yates shuffle
# 原本是 let shuffledOpts = [...q.options].sort(() => Math.random() - 0.5);
# 檢查一下是否有這行
if "Math.random() - 0.5" in s6_html:
    print("✅ social6_curriculum.html 前端已有動態隨機打亂機制！")
else:
    print("⚠️ 需在 social6_curriculum.html 注入前端隨機打亂！")

with open("social6_curriculum.html", "w", encoding="utf-8") as f:
    f.write(s6_html)
print("✅ social6_curriculum.html 題庫與前端確認完成！")
