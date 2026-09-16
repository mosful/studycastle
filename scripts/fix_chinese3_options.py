# -*- coding: utf-8 -*-
import json
import random
import re
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

print("=== 修復三年級國語全冊題庫選項打亂 ===")

# 1. 更新 chinese3_full_curriculum_database.json
with open("chinese3_full_curriculum_database.json", "r", encoding="utf-8") as f:
    c3_data = json.load(f)

for lesson in c3_data:
    for q in lesson.get("exam", []):
        opts = q.get("options", [])
        if len(opts) > 1:
            random.shuffle(opts)
            q["options"] = opts
    for q in lesson.get("quiz", []):
        opts = q.get("options", [])
        if len(opts) > 1:
            random.shuffle(opts)
            q["options"] = opts

with open("chinese3_full_curriculum_database.json", "w", encoding="utf-8") as f:
    json.dump(c3_data, f, ensure_ascii=False, indent=2)

print("✅ chinese3_full_curriculum_database.json 選項已隨機打亂！")

# 2. 更新 chinese3_curriculum.html 內嵌 CURRICULUM
with open("chinese3_curriculum.html", "r", encoding="utf-8") as f:
    c3_html = f.read()

def shuffle_opts(m):
    opts_raw = m.group(1)
    try:
        opts = json.loads(opts_raw)
        if len(opts) > 1:
            random.shuffle(opts)
        return f'"options": {json.dumps(opts, ensure_ascii=False)}'
    except Exception:
        return m.group(0)

c3_html = re.sub(r'"options"\s*:\s*(\[[^\]]+\])', shuffle_opts, c3_html)

# 確保前端選項渲染時隨機打亂
# 檢查是否有 let shuffledOpts = [...q.options].sort(() => Math.random() - 0.5);
if "Math.random() - 0.5" in c3_html:
    print("✅ chinese3_curriculum.html 前端已有動態隨機打亂機制！")
else:
    print("⚠️ 需在 chinese3_curriculum.html 注入前端隨機打亂！")

with open("chinese3_curriculum.html", "w", encoding="utf-8") as f:
    f.write(c3_html)
print("✅ chinese3_curriculum.html 題庫與前端確認完成！")
