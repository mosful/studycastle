# -*- coding: utf-8 -*-
import json
import random
import re
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

print("=== 均衡打亂 element_game 與 idiom_game 題庫靜態選項 ===")

for fn in ["element_game.html", "idiom_game.html"]:
    with open(fn, "r", encoding="utf-8") as f:
        text = f.read()

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

    with open(fn, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"✅ {fn} 靜態選項打亂完成！")
