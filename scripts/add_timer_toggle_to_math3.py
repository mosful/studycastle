# -*- coding: utf-8 -*-
import os
import re
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

print("=== 為三年級數學 5 個單元新增倒數計時開關（預設關閉） ===")

math3_files = [
    ("math3_addition.html", 25, "🏰 攻破城堡！開始冒險！", "st.timer", "TIMER"),
    ("math3_geometry.html", 25, "📐 進入幾何王國！出發！", "st.timer", "TIMER"),
    ("math3_measurement.html", 25, "📏 啟動測量儀！出發冒險！", "st.timer", "TIMER"),
    ("math3_multiplication.html", 20, "⚡ 召喚九九神力！出發！", "st.timer", "TIMER"),
    ("math3_numbers.html", 20, "🚀 啟動火箭！出發冒險！", "state.timerInterval", "TIMER_SECONDS")
]

# 通用 CSS 樣式
timer_toggle_css = """
/* ── 倒數計時開關與 HUD 按鈕樣式 ── */
.timer-setting-card {
  display: flex;
  align-items: center;
  justify-content: space-between;
  background: rgba(255, 255, 255, 0.08);
  border: 1.5px solid rgba(255, 255, 255, 0.16);
  border-radius: 20px;
  padding: 12px 18px;
  margin: 18px 0 16px;
  backdrop-filter: blur(10px);
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.15);
  transition: all 0.3s ease;
}
.timer-setting-card:hover {
  border-color: rgba(255, 255, 255, 0.3);
  background: rgba(255, 255, 255, 0.12);
}
.timer-setting-info {
  display: flex;
  align-items: center;
  gap: 12px;
  text-align: left;
}
.timer-setting-icon {
  font-size: 1.8rem;
  transition: transform 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
}
.timer-setting-title {
  font-size: 0.98rem;
  font-weight: 800;
  color: #FFFFFF;
  letter-spacing: 0.5px;
}
.timer-setting-subtitle {
  font-size: 0.78rem;
  color: rgba(255, 255, 255, 0.65);
  margin-top: 2px;
}
.switch-toggle {
  position: relative;
  display: inline-block;
  width: 52px;
  height: 28px;
  flex-shrink: 0;
  cursor: pointer;
}
.switch-toggle input {
  opacity: 0;
  width: 0;
  height: 0;
}
.slider-round {
  position: absolute;
  cursor: pointer;
  inset: 0;
  background-color: rgba(255, 255, 255, 0.2);
  border: 1.5px solid rgba(255, 255, 255, 0.3);
  border-radius: 34px;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}
.slider-round:before {
  position: absolute;
  content: "";
  height: 20px;
  width: 20px;
  left: 3px;
  bottom: 2.5px;
  background-color: #FFFFFF;
  border-radius: 50%;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.3);
  transition: all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
}
.switch-toggle input:checked + .slider-round {
  background: linear-gradient(135deg, #10B981, #059669);
  border-color: #34D399;
  box-shadow: 0 0 12px rgba(16, 185, 129, 0.4);
}
.switch-toggle input:checked + .slider-round:before {
  transform: translateX(24px);
}
.hud-timer-btn {
  display: inline-flex;
  align-items: center;
  gap: 5px;
  background: rgba(255, 255, 255, 0.08);
  border: 1.5px solid rgba(255, 255, 255, 0.2);
  border-radius: 20px;
  padding: 6px 14px;
  color: #FFFFFF;
  font-size: 0.82rem;
  font-weight: 700;
  cursor: pointer;
  transition: all 0.2s ease;
  backdrop-filter: blur(6px);
}
.hud-timer-btn:hover {
  background: rgba(255, 255, 255, 0.16);
  border-color: rgba(255, 255, 255, 0.4);
  transform: translateY(-1px);
}
.hud-timer-btn.active {
  background: rgba(16, 185, 129, 0.2);
  border-color: #10B981;
  color: #A7F3D0;
}
.timer-mode-pill {
  font-size: 0.75rem;
  font-weight: 700;
  padding: 2px 8px;
  border-radius: 10px;
  background: rgba(255, 255, 255, 0.1);
  color: rgba(255, 255, 255, 0.7);
  margin-left: 6px;
}
"""

for fn, default_sec, btn_text, timer_var, timer_const in math3_files:
    with open(fn, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. 注入 CSS
    if ".timer-setting-card" not in content:
        content = content.replace("</style>", timer_toggle_css + "\n</style>")

    # 2. 開始畫面注入切換卡片
    setting_card_html = f"""      <!-- 倒數計時開關選項 (預設關閉，讓學生自主無壓力學習) -->
      <div class="timer-setting-card">
        <div class="timer-setting-info">
          <span class="timer-setting-icon" id="startTimerIcon">🧘</span>
          <div>
            <div class="timer-setting-title">挑戰倒數計時</div>
            <div class="timer-setting-subtitle" id="startTimerSub">已關閉（無時間壓力，放鬆思考計算）</div>
          </div>
        </div>
        <label class="switch-toggle" title="切換倒數計時">
          <input type="checkbox" id="timerCheckbox" onchange="toggleTimerSetting(this.checked)">
          <span class="slider-round"></span>
        </label>
      </div>
"""
    if "timer-setting-card" not in content:
        content = content.replace(f'<button class="start-btn" id="startBtn">', setting_card_html + f'      <button class="start-btn" id="startBtn">')

    # 3. 遊戲中畫面 HUD 注入快捷切換按鈕
    hud_btn_html = """      <button type="button" class="hud-timer-btn" id="hudTimerBtn" onclick="toggleTimerSetting()" title="點擊切換倒數計時">
        <span id="hudTimerIcon">⏱️</span>
        <span id="hudTimerText">計時：關閉 🧘</span>
      </button>
"""
    if "hud-timer-btn" not in content:
        content = content.replace('<div class="stage-info"', hud_btn_html + '      <div class="stage-info"')

    # 4. JavaScript 邏輯注入
    is_numbers = (fn == "math3_numbers.html")
    stop_timer_call = "stopTimer();"
    timer_int_var = "state.timerInterval" if is_numbers else "st.timer"
    timer_sec_const = "TIMER_SECONDS" if is_numbers else "TIMER"
    timer_left_var = "state.timerLeft" if is_numbers else "st.tLeft"

    js_timer_logic = f"""
// ── 倒數計時偏好開關 (預設關閉，防禦性自主學習模式) ──
let timerEnabled = false;

function toggleTimerSetting(forcedVal) {{
  if (typeof forcedVal === 'boolean') {{
    timerEnabled = forcedVal;
  }} else {{
    timerEnabled = !timerEnabled;
  }}

  // 同步開始畫面 UI
  const chk = document.getElementById('timerCheckbox');
  if (chk) chk.checked = timerEnabled;
  
  const icon = document.getElementById('startTimerIcon');
  const sub = document.getElementById('startTimerSub');
  if (icon) icon.textContent = timerEnabled ? '⚡' : '🧘';
  if (sub) sub.textContent = timerEnabled ? '已開啟（每題 {default_sec} 秒限時挑戰）' : '已關閉（無時間壓力，放鬆思考計算）';

  // 同步 HUD 頂部按鈕
  const hudBtn = document.getElementById('hudTimerBtn');
  const hudText = document.getElementById('hudTimerText');
  if (hudBtn && hudText) {{
    if (timerEnabled) {{
      hudBtn.classList.add('active');
      hudText.textContent = '計時：開啟 ⚡';
    }} else {{
      hudBtn.classList.remove('active');
      hudText.textContent = '計時：關閉 🧘';
    }}
  }}

  // 同步控制計時進度條
  const timerBar = document.getElementById('timerBar');
  if (!timerEnabled) {{
    {stop_timer_call}
    if (timerBar) {{
      timerBar.style.width = '100%';
      timerBar.classList.remove('urgent');
    }}
  }} else {{
    // 若在答題畫面且尚未作答，重新啟動計時
    startTimer();
  }}
}}

// 初始化開關狀態
document.addEventListener('DOMContentLoaded', () => {{
  toggleTimerSetting(false);
}});
"""

    # 檢查是否已加入 toggleTimerSetting
    if "function toggleTimerSetting" not in content:
        content = content.replace("function startTimer()", js_timer_logic + "\nfunction startTimer()")

    # 5. 修改 startTimer() 確保 timerEnabled 為 false 時不倒數
    if is_numbers:
        # math3_numbers.html
        old_st = "function startTimer(){"
        new_st = """function startTimer(){
  if (!timerEnabled) {
    stopTimer();
    const bar = document.getElementById('timerBar');
    if (bar) { bar.style.width = '100%'; bar.classList.remove('urgent'); }
    return;
  }"""
        content = content.replace(old_st, new_st, 1)
    else:
        old_st = "function startTimer(){"
        new_st = """function startTimer(){
  if (!timerEnabled) {
    stopTimer();
    const bar = document.getElementById('timerBar');
    if (bar) { bar.style.width = '100%'; bar.classList.remove('urgent'); }
    return;
  }"""
        content = content.replace(old_st, new_st, 1)

    with open(fn, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"✅ {fn} 成功加入倒數計時開關（預設關閉）！")

print("\n全部 5 個三年級數學檔案升級完成！")
