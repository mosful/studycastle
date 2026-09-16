# -*- coding: utf-8 -*-
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

with open('math3_addition.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('function loadQ')
print(text[idx:idx+1500])
