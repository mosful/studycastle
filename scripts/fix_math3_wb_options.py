# -*- coding: utf-8 -*-
import os
import re
import sys
import random

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

print("=== 修復三年級數學 5 個檔案的題庫選項洗牌 ===")

math3_files = [
    "math3_numbers.html",
    "math3_addition.html",
    "math3_multiplication.html",
    "math3_measurement.html",
    "math3_geometry.html"
]

for fn in math3_files:
    with open(fn, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. 修改前端渲染邏輯，加入動態隨機打亂
    # 找 const opts = item.options || [item.ans];
    old_opts_line = "const opts = item.options || [item.ans];"
    new_opts_line = "const opts = (item.options ? [...item.options] : [item.ans]).sort(() => Math.random() - 0.5);"
    if old_opts_line in content:
        content = content.replace(old_opts_line, new_opts_line)
        print(f"[{fn}] 成功加入前端動態隨機打亂！")
    else:
        # 找正則
        content = re.sub(
            r'const\s+opts\s*=\s*(?:item\.options\s*\|\|\s*\[item\.ans\]);',
            r'const opts = (item.options ? [...item.options] : [item.ans]).sort(() => Math.random() - 0.5);',
            content
        )
        print(f"[{fn}] (正則) 加入前端動態隨機打亂！")

    # 2. 修改靜態 JSON/物件中的 options 順序，確保靜態儲存中答案也不是全部都在第 0 項
    # 尋找 "options": ["...", "...", ...]
    def shuffle_options_match(match):
        arr_str = match.group(1)
        # 用 json 解析陣列
        import json
        try:
            arr = json.loads(arr_str)
            if len(arr) > 1:
                # 打亂順序
                random.shuffle(arr)
            return f'"options": {json.dumps(arr, ensure_ascii=False)}'
        except Exception:
            return match.group(0)

    content = re.sub(r'"options"\s*:\s*(\[[^\]]+\])', shuffle_options_match, content)

    with open(fn, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"[{fn}] 題庫選項資料與渲染全部升級完成！")

# 同步更新 scripts/inject_math3_workbooks.py 與 scripts/build_math3_workbook_data.py
for sc in ["scripts/inject_math3_workbooks.py", "scripts/build_math3_workbook_data.py"]:
    if os.path.exists(sc):
        with open(sc, "r", encoding="utf-8") as f:
            sc_text = f.read()
        sc_text = sc_text.replace(
            "const opts = item.options || [item.ans];",
            "const opts = (item.options ? [...item.options] : [item.ans]).sort(() => Math.random() - 0.5);"
        )
        with open(sc, "w", encoding="utf-8") as f:
            f.write(sc_text)
        print(f"[{sc}] 同步腳本完成！")
