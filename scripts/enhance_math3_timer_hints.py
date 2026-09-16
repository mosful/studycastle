# -*- coding: utf-8 -*-
import sys
import re

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

print("=== 微調三年級數學開始畫面提示文字聯動 ===")

math3_files = [
    ("math3_addition.html", 25),
    ("math3_geometry.html", 25),
    ("math3_measurement.html", 25),
    ("math3_multiplication.html", 20),
    ("math3_numbers.html", 20)
]

for fn, sec in math3_files:
    with open(fn, "r", encoding="utf-8") as f:
        content = f.read()

    # 替換靜態說明段落
    old_p = f'<p style="margin-top:16px;color:rgba(255,255,255,0.4);font-size:0.8rem;">共 5 關 × 每關 8 題 ｜ 每題 {sec} 秒 ｜ 答對 6/8 才能前進</p>'
    new_p = f'<p id="startHintDesc" style="margin-top:14px;color:rgba(255,255,255,0.65);font-size:0.82rem;font-weight:600;">共 5 關 × 每關 8 題 ｜ 🧘 自主學習無時間限制 ｜ 答對 6/8 即可晉級</p>'

    if old_p in content:
        content = content.replace(old_p, new_p)
    else:
        # 正則相容替換
        content = re.sub(
            r'<p[^>]*>共 5 關 × 每關 8 題 ｜ 每題 \d+ 秒 ｜ 答對 6/8 才能前進</p>',
            new_p,
            content
        )

    # 在 toggleTimerSetting 裡加入 startHintDesc 聯動
    hint_sync_code = f"""
  const hintDesc = document.getElementById('startHintDesc');
  if (hintDesc) {{
    hintDesc.textContent = timerEnabled 
      ? '共 5 關 × 每關 8 題 ｜ ⚡ 限時 {sec} 秒挑戰 ｜ 答對 6/8 即可晉級'
      : '共 5 關 × 每關 8 題 ｜ 🧘 自主學習無時間限制 ｜ 答對 6/8 即可晉級';
  }}
"""
    if "const hintDesc = document.getElementById('startHintDesc');" not in content:
        content = content.replace(
            "const sub = document.getElementById('startTimerSub');",
            "const sub = document.getElementById('startTimerSub');" + hint_sync_code
        )

    with open(fn, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"✅ {fn} 提示文字動態聯動已配置！")

print("微調完成！")
