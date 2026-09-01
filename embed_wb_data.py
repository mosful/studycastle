# -*- coding: utf-8 -*-
"""
將 workbook JSON 資料直接內嵌進 fraction-division.html, decimal-division.html, circle-area.html
解決 file:// 協議下 fetch 被 CORS 阻擋導致點擊回數沒反應的問題
"""

import sys
import json
import re
sys.stdout.reconfigure(encoding='utf-8')

with open("c:/Code/StudyCastle/workbook_6th_math_u1_u4.json", "r", encoding="utf-8") as f:
    wb_all = json.load(f)

# 1. 處理 fraction-division.html
with open("c:/Code/StudyCastle/fraction-division.html", "r", encoding="utf-8") as f:
    frac_html = f.read()

u2_json_str = json.dumps(wb_all["unit2"], ensure_ascii=False)
# 替換 let U2_WB_DATA = null; fetch(...)
frac_pattern = r"let U2_WB_DATA = null;\s*fetch\('workbook_6th_math_u1_u4\.json'\)\.then\(r=>r\.json\(\)\)\.then\(d=>\{\s*U2_WB_DATA = d\.unit2;\s*\}\);"
frac_replacement = f"const U2_WB_DATA = {u2_json_str};"
if re.search(frac_pattern, frac_html):
    frac_html_new = re.sub(frac_pattern, frac_replacement, frac_html)
    with open("c:/Code/StudyCastle/fraction-division.html", "w", encoding="utf-8") as f:
        f.write(frac_html_new)
    print("[OK] fraction-division.html embedded U2_WB_DATA")
else:
    print("[WARN] fraction-division.html pattern not found, checking if already embedded")

# 2. 處理 decimal-division.html
with open("c:/Code/StudyCastle/decimal-division.html", "r", encoding="utf-8") as f:
    dec_html = f.read()

u3_json_str = json.dumps(wb_all["unit3"], ensure_ascii=False)
dec_pattern = r"let U3_WB_DATA = null;\s*fetch\('workbook_6th_math_u1_u4\.json'\)\.then\(r=>r\.json\(\)\)\.then\(d=>\{\s*U3_WB_DATA = d\.unit3;\s*\}\);"
dec_replacement = f"const U3_WB_DATA = {u3_json_str};"
if re.search(dec_pattern, dec_html):
    dec_html_new = re.sub(dec_pattern, dec_replacement, dec_html)
    with open("c:/Code/StudyCastle/decimal-division.html", "w", encoding="utf-8") as f:
        f.write(dec_html_new)
    print("[OK] decimal-division.html embedded U3_WB_DATA")
else:
    print("[WARN] decimal-division.html pattern not found")

# 3. 處理 circle-area.html
with open("c:/Code/StudyCastle/circle-area.html", "r", encoding="utf-8") as f:
    circ_html = f.read()

u4_json_str = json.dumps(wb_all["unit4"], ensure_ascii=False)
circ_pattern = r"let U4_WB_DATA = null;\s*fetch\('workbook_6th_math_u1_u4\.json'\)\.then\(r=>r\.json\(\)\)\.then\(d=>\{\s*U4_WB_DATA = d\.unit4;\s*\}\);"
circ_replacement = f"const U4_WB_DATA = {u4_json_str};"
if re.search(circ_pattern, circ_html):
    circ_html_new = re.sub(circ_pattern, circ_replacement, circ_html)
    with open("c:/Code/StudyCastle/circle-area.html", "w", encoding="utf-8") as f:
        f.write(circ_html_new)
    print("[OK] circle-area.html embedded U4_WB_DATA")
else:
    print("[WARN] circle-area.html pattern not found")
