# -*- coding: utf-8 -*-
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

for fn in ['math3_addition.html', 'math3_numbers.html']:
    with open(fn, 'r', encoding='utf-8') as f:
        text = f.read()
    print(f"=== {fn} startGame ===")
    idx = text.find('function startGame')
    print(text[idx:idx+800])
    
    # 找開始畫面上的按鈕
    btn_idx = text.find('startGame(')
    if btn_idx == -1: btn_idx = text.find('onclick="startGame')
    print("--- start button in HTML ---")
    print(text[btn_idx-150:btn_idx+200])
