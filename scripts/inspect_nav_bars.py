# -*- coding: utf-8 -*-
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

for fn in ['math3_addition.html', 'math3_numbers.html']:
    with open(fn, 'r', encoding='utf-8') as f:
        text = f.read()
    print(f"=== {fn} 頂部區域 ===")
    idx = text.find('class="top-bar"')
    if idx == -1: idx = text.find('class="nav')
    if idx == -1: idx = text.find('nav-btn')
    print(text[idx-50:idx+650])
