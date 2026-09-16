# -*- coding: utf-8 -*-
import json
import random
import re
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

print("=== 檢查並更新 chinese6_midterm.html 題庫選項 ===")

with open("chinese6_midterm.html", "r", encoding="utf-8") as f:
    text = f.read()

# 隨機打亂所有 "options": [...] 裡面的順序
def shuffle_opts(m):
    opts_raw = m.group(1)
    try:
        opts = json.loads(opts_raw)
        if len(opts) > 1:
            random.shuffle(opts)
        return f'"options": {json.dumps(opts, ensure_ascii=False)}'
    except Exception:
        return m.group(0)

text = re.sub(r'"options"\s*:\s*(\[[^\]]+\])', shuffle_opts, text)

# 確保前端選項按鈕渲染時有做隨機洗牌
# 檢查 renderQuizQuestion
if "Math.random() - 0.5" in text:
    print("✅ chinese6_midterm.html 前端已有動態隨機打亂機制！")
else:
    print("⚠️ 需在 chinese6_midterm.html 注入前端隨機打亂！")

with open("chinese6_midterm.html", "w", encoding="utf-8") as f:
    f.write(text)

print("✅ chinese6_midterm.html 更新完成！")
