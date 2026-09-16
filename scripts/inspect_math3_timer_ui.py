# -*- coding: utf-8 -*-
import sys
import re

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

m3_files = ['math3_addition.html', 'math3_geometry.html', 'math3_measurement.html', 'math3_multiplication.html', 'math3_numbers.html']

for fn in m3_files:
    with open(fn, 'r', encoding='utf-8') as f:
        text = f.read()
    print(f"==================================================")
    print(f"檔案: {fn}")
    print(f"==================================================")
    
    # 找 timerBar 或 timer 相關的 HTML
    tb_idx = text.find('timerBar')
    if tb_idx != -1:
        print("--- Timer Bar HTML ---")
        print(text[tb_idx-150:tb_idx+200])
    else:
        # 找 timer-bar 或 timer
        m = re.search(r'(<div[^>]*timer[^>]*>[\s\S]*?</div>)', text, re.I)
        if m:
            print("--- Timer HTML ---")
            print(m.group(1)[:250])
    
    # 找 startTimer 與 state
    st_idx = text.find('function startTimer')
    if st_idx != -1:
        print("--- startTimer JS ---")
        print(text[st_idx:st_idx+400])
