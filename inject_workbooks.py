# -*- coding: utf-8 -*-
"""
完整注入作業簿模組到 prime.html, fraction-division.html, decimal-division.html
"""

import json

with open("c:/Code/StudyCastle/workbook_6th_math_u1_u4.json", "r", encoding="utf-8") as f:
    ALL_WB = json.load(f)

# ==========================================
# 1. 注入 prime.html (單元 1：第 1~3 回)
# ==========================================
with open("c:/Code/StudyCastle/prime.html", "r", encoding="utf-8") as f:
    prime_content = f.read()

# 在頂部 top-bar 加上作業簿按鈕
if "openWbModal()" not in prime_content:
    top_bar_target = '<div style="display: flex; gap: 8px; align-items: center;">'
    top_bar_repl = '''<div style="display: flex; gap: 8px; align-items: center;">
      <button class="nav-btn" style="background:linear-gradient(135deg,#FF6B5B,#FF8E53);color:#fff;border-color:#fff;" onclick="openWbModal()">
        <span>📑</span>
        <span>南一作業簿隨堂考 (第1~3回)</span>
      </button>'''
    prime_content = prime_content.replace(top_bar_target, top_bar_repl, 1)

# 加入 Modal HTML 與 JS
u1_data_js = json.dumps(ALL_WB["unit1"], ensure_ascii=False)

wb_prime_addon = f'''
<!-- 南一作業簿隨堂測驗 Modal -->
<div class="wb-modal-overlay" id="wbModalOverlay">
  <div class="wb-modal-content">
    <div class="wb-header">
      <div class="wb-title">📑 南一 6上數學 作業簿隨堂測驗（第 1 單元）</div>
      <button class="wb-close-btn" onclick="closeWbModal()">✕</button>
    </div>
    <div class="wb-tabs" id="wbTabs">
      <button class="wb-tab active" onclick="switchWbRev(1)">第 1 回 (1-1~1-4 質數與合數)</button>
      <button class="wb-tab" onclick="switchWbRev(2)">第 2 回 (1-5 短除法求 GCD)</button>
      <button class="wb-tab" onclick="switchWbRev(3)">第 3 回 (1-6 短除法求 LCM)</button>
    </div>
    <div id="wbQuizBody"></div>
    <div class="wb-submit-bar">
      <div class="wb-score-text" id="wbScoreDisp">狀態：做題中（未交卷）</div>
      <div style="display:flex; gap:10px;">
        <button class="btn gold small" onclick="resetWbQuiz()">🔄 重填</button>
        <button class="wb-btn-submit" onclick="gradeWbQuiz()">📝 交卷批改並看詳解</button>
      </div>
    </div>
  </div>
</div>

<style>
.wb-modal-overlay {{
  display: none;
  position: fixed;
  inset: 0;
  background: rgba(11, 79, 108, 0.85);
  backdrop-filter: blur(8px);
  z-index: 1000;
  overflow-y: auto;
  padding: 20px 12px 60px;
}}
.wb-modal-overlay.open {{ display: block; }}
.wb-modal-content {{
  background: #FFFDF5;
  border: 3px solid #1C86A6;
  border-radius: 24px;
  max-width: 820px;
  margin: 0 auto;
  padding: 24px 20px;
  color: #12303B;
  box-shadow: 0 16px 40px rgba(0,0,0,0.4);
}}
.wb-header {{
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-bottom: 2px solid #E9D9A6;
  padding-bottom: 12px;
  margin-bottom: 16px;
}}
.wb-title {{ font-size: 20px; font-weight: 800; color: #0B4F6C; display: flex; align-items: center; gap: 8px; }}
.wb-close-btn {{
  width: 38px; height: 38px; border-radius: 50%; border: 2px solid #12303B; background: #FFF;
  font-weight: 900; font-size: 18px; cursor: pointer;
}}
.wb-tabs {{ display: flex; gap: 8px; margin-bottom: 16px; flex-wrap: wrap; }}
.wb-tab {{
  flex: 1; min-width: 140px; padding: 10px 14px; border-radius: 12px; border: 2px solid #E9D9A6;
  background: #FFF; font-weight: 800; font-size: 13.5px; cursor: pointer; color: #5C6B70;
  text-align: center; transition: all 0.2s;
}}
.wb-tab.active {{ background: #FFB703; border-color: #D48800; color: #12303B; box-shadow: 0 4px 0 #D48800; }}
.wb-sec-card {{ background: #FFF; border: 2px solid #E9D9A6; border-radius: 16px; padding: 18px; margin-bottom: 16px; }}
.wb-sec-title {{ font-size: 16px; font-weight: 800; color: #0B4F6C; margin-bottom: 12px; border-bottom: 1.5px dashed #E9D9A6; padding-bottom: 6px; }}
.wb-q-item {{ background: #FBF0D3; border-radius: 12px; padding: 14px; margin-bottom: 12px; border: 1px solid #E9D9A6; }}
.wb-q-text {{ font-size: 15px; font-weight: 600; line-height: 1.6; margin-bottom: 8px; }}
.wb-input {{
  background: #FFF; border: 2px solid #1C86A6; border-radius: 8px; padding: 6px 12px;
  font-size: 15px; font-weight: 700; color: #12303B; outline: none; min-width: 120px;
}}
.wb-input:focus {{ border-color: #FF6B5B; box-shadow: 0 0 8px rgba(255,107,91,0.4); }}
.wb-sol-panel {{ display: none; background: #E6F8F6; border: 1.5px solid #2EC4B6; border-radius: 10px; padding: 12px; margin-top: 10px; font-size: 14px; }}
.wb-sol-panel.show {{ display: block; }}
.wb-sol-steps {{ font-family: 'Fredoka', monospace; background: #FFF; padding: 8px; border-radius: 6px; margin: 6px 0; white-space: pre-wrap; color: #0B4F6C; font-weight: 700; }}
.wb-sol-ans {{ color: #D48800; font-weight: 800; }}
.wb-submit-bar {{
  position: sticky; bottom: 0; background: #FFFDF5; border-top: 2px solid #E9D9A6;
  padding: 14px 0 0; display: flex; justify-content: space-between; align-items: center;
  flex-wrap: wrap; gap: 10px; z-index: 10;
}}
.wb-score-text {{ font-size: 18px; font-weight: 800; color: #0B4F6C; }}
.wb-btn-submit {{
  background: linear-gradient(135deg, #2EC4B6 0%, #0E7C7B 100%);
  border: none; color: #FFF; font-weight: 800; font-size: 15px; padding: 10px 24px;
  border-radius: 12px; cursor: pointer; box-shadow: 0 4px 0 #0A5A59;
}}
</style>

<script>
const U1_WB_DATA = {u1_data_js};
let wbCurrentRevId = 1;
let wbAnswers = {{}};

function openWbModal() {{
  document.getElementById('wbModalOverlay').classList.add('open');
  document.body.style.overflow = 'hidden';
  switchWbRev(1);
}}
function closeWbModal() {{
  document.getElementById('wbModalOverlay').classList.remove('open');
  document.body.style.overflow = '';
}}

function switchWbRev(revId) {{
  wbCurrentRevId = revId;
  wbAnswers = {{}};
  document.querySelectorAll('.wb-tab').forEach((t, i) => t.classList.toggle('active', i + 1 === revId));
  document.getElementById('wbScoreDisp').textContent = '狀態：做題中（未交卷）';
  renderWbQuizBody();
}}

function renderWbQuizBody() {{
  const rev = U1_WB_DATA.reviews.find(r => r.review_id === wbCurrentRevId);
  const container = document.getElementById('wbQuizBody');
  if (!rev) return;

  let html = '';
  rev.sections.forEach((sec, sIdx) => {{
    html += `<div class="wb-sec-card">
      <div class="wb-sec-title">📌 ${{sec.section_title}}</div>`;

    if (sec.type === 'prime_composite_check') {{
      html += '<div style="display:grid; grid-template-columns:repeat(auto-fill, minmax(130px, 1fr)); gap:10px;">';
      sec.items.forEach((item, iIdx) => {{
        const itemId = `u1_r${{wbCurrentRevId}}_s${{sIdx}}_${{iIdx}}`;
        html += `
          <div style="background:#FFF; border:1.5px solid #E9D9A6; border-radius:10px; padding:10px; text-align:center;">
            <div style="font-size:22px; font-weight:800; color:#0B4F6C; margin-bottom:6px;">${{item.num}}</div>
            <select class="wb-input" style="min-width:90px; text-align:center;" id="${{itemId}}" onchange="wbSave('${{itemId}}', this.value)">
              <option value="">選擇</option>
              <option value="prime">○ 質數</option>
              <option value="composite">✓ 合數</option>
            </select>
            <div class="wb-sol-panel" id="sol_${{itemId}}">
              <div class="wb-sol-ans">${{item.label === '○' ? '○ 質數' : '✓ 合數'}}</div>
              <small>${{item.note}}</small>
            </div>
          </div>`;
      }});
      html += '</div>';
    }} else if (sec.type === 'fill_in' || sec.type === 'coprime_check') {{
      sec.items.forEach((item, iIdx) => {{
        const itemId = `u1_r${{wbCurrentRevId}}_s${{sIdx}}_${{iIdx}}`;
        if (sec.type === 'coprime_check') {{
          html += `
            <div class="wb-q-item">
              <div class="wb-q-text">第 (${{iIdx+1}}) 組：<b>${{item.pair}}</b></div>
              <div style="display:flex; align-items:center; gap:8px;">
                <span>是否互質？</span>
                <select class="wb-input" id="${{itemId}}" onchange="wbSave('${{itemId}}', this.value)">
                  <option value="">請選擇</option>
                  <option value="yes">✓ 互質</option>
                  <option value="no">✕ 沒有互質</option>
                </select>
              </div>
              <div class="wb-sol-panel" id="sol_${{itemId}}">
                <div class="wb-sol-steps">${{item.f1}}\\n${{item.f2}}\\n${{item.common}}</div>
                <div class="wb-sol-ans">標準判定：${{item.result}}</div>
              </div>
            </div>`;
        }} else {{
          html += `
            <div class="wb-q-item">
              <div class="wb-q-text">${{item.q}}</div>
              <input type="text" class="wb-input" id="${{itemId}}" placeholder="請填寫答案" oninput="wbSave('${{itemId}}', this.value)">
              <div class="wb-sol-panel" id="sol_${{itemId}}">
                <div class="wb-sol-ans">標準答案：${{item.ans}}</div>
                <small>${{item.explanation}}</small>
              </div>
            </div>`;
        }}
      }});
    }} else if (sec.type === 'tree_factorization' || sec.type === 'prime_factorization' || sec.type === 'short_division_factor' || sec.type === 'short_division_gcd' || sec.type === 'factor_expr_gcd' || sec.type === 'short_division_lcm' || sec.type === 'factor_expr_lcm') {{
      html += '<div style="display:grid; grid-template-columns:repeat(auto-fill, minmax(240px, 1fr)); gap:12px;">';
      sec.items.forEach((item, iIdx) => {{
        const itemId = `u1_r${{wbCurrentRevId}}_s${{sIdx}}_${{iIdx}}`;
        const qTitle = item.num ? `數字：<b>${{item.num}}</b>` : `各組數：<b>${{item.pair}}</b>`;
        html += `
          <div class="wb-q-item">
            <div class="wb-q-text">${{qTitle}}</div>
            <input type="text" class="wb-input" style="width:100%;" id="${{itemId}}" placeholder="填寫質因數分解式或數值" oninput="wbSave('${{itemId}}', this.value)">
            <div class="wb-sol-panel" id="sol_${{itemId}}">
              <div class="wb-sol-steps">${{item.steps || item.tree || item.common_factors || ''}}</div>
              <div class="wb-sol-ans">標準答案：${{item.ans}}</div>
            </div>
          </div>`;
      }});
      html += '</div>';
    }} else if (sec.type === 'word_problems') {{
      sec.items.forEach((item, iIdx) => {{
        const itemId = `u1_r${{wbCurrentRevId}}_s${{sIdx}}_${{iIdx}}`;
        html += `
          <div class="wb-q-item">
            <div class="wb-q-text">${{item.q}}</div>
            <input type="text" class="wb-input" style="width:100%; max-width:320px;" id="${{itemId}}" placeholder="輸入答案數值" oninput="wbSave('${{itemId}}', this.value)">
            <div class="wb-sol-panel" id="sol_${{itemId}}">
              <div class="wb-sol-steps">${{item.steps}}</div>
              <div class="wb-sol-ans">標準答案：${{item.ans}}</div>
            </div>
          </div>`;
      }});
    }}

    html += '</div>';
  }});
  container.innerHTML = html;
}}

function wbSave(id, val) {{
  wbAnswers[id] = val.trim();
}}

function gradeWbQuiz() {{
  const rev = U1_WB_DATA.reviews.find(r => r.review_id === wbCurrentRevId);
  let total = 0, correct = 0;

  rev.sections.forEach((sec, sIdx) => {{
    sec.items.forEach((item, iIdx) => {{
      total++;
      const itemId = `u1_r${{wbCurrentRevId}}_s${{sIdx}}_${{iIdx}}`;
      const userVal = wbAnswers[itemId] || '';
      let isRight = false;

      if (sec.type === 'prime_composite_check') {{
        isRight = (userVal === item.answer);
      }} else if (sec.type === 'coprime_check') {{
        isRight = (item.coprime ? userVal === 'yes' : userVal === 'no');
      }} else {{
        const cleanUser = userVal.replace(/[\\s\\*xX×]/g, '').replace(/公分|公尺|個|束|張|日|月|元|個學生|個蘋果和|個梨子/g, '');
        const cleanAns = String(item.ans).replace(/[\\s\\*xX×]/g, '').replace(/公分|公尺|個|束|張|日|月|元|個學生|個蘋果和|個梨子/g, '');
        isRight = cleanUser === cleanAns || cleanUser.includes(cleanAns) || (cleanAns.includes('、') && cleanAns.split('、').every(x => cleanUser.includes(x)));
      }}

      if (isRight) correct++;
      const panel = document.getElementById(`sol_${{itemId}}`);
      if (panel) {{
        panel.classList.add('show');
        panel.style.borderLeft = isRight ? '4px solid #2EC4B6' : '4px solid #FF4757';
      }}
    }});
  }});

  const score = Math.round((correct / total) * 100);
  document.getElementById('wbScoreDisp').innerHTML = `得分：<b>${{score}} 分</b> (${{correct}} / ${{total}} 題正確)`;
  if (score >= 80 && window.confetti) {{
    confetti({{ particleCount: 100, spread: 70, origin: {{ y: 0.6 }} }});
  }}
  alert(`🎉 隨堂測驗批改完成！\\n\\n得分：${{score}} 分\\n所有題目的南一教用版詳解與短除法步驟已在下方完整顯示！✨`);
}}

function resetWbQuiz() {{
  wbAnswers = {{}};
  renderWbQuizBody();
  document.getElementById('wbScoreDisp').textContent = '狀態：做題中（未交卷）';
}}
</script>
'''

if "wbModalOverlay" not in prime_content:
    prime_content = prime_content.replace('</body>', wb_prime_addon + '\n</body>')
    with open("c:/Code/StudyCastle/prime.html", "w", encoding="utf-8") as f:
        f.write(prime_content)
    print("Injected unit 1 into prime.html successfully!")


# ==========================================
# 2. 注入 fraction-division.html (單元 2：第 4~6 回)
# ==========================================
with open("c:/Code/StudyCastle/fraction-division.html", "r", encoding="utf-8") as f:
    frac_content = f.read()

u2_data_js = json.dumps(ALL_WB["unit2"], ensure_ascii=False)

if "openFracWbModal()" not in frac_content:
    # 頂部導航按鈕
    frac_top_target = '<div class="hdr-left">'
    frac_top_repl = '''<div class="hdr-left">
      <button class="back-btn" style="background:linear-gradient(135deg,#E63946,#F4A261);color:#fff;" onclick="openFracWbModal()">
        <span>📑</span>
        <span>南一作業簿隨堂考 (第4~6回)</span>
      </button>'''
    frac_content = frac_content.replace(frac_top_target, frac_top_repl, 1)

wb_frac_addon = f'''
<!-- 南一作業簿隨堂測驗 Modal (分數除法) -->
<div class="wb-modal-overlay" id="fracWbModalOverlay">
  <div class="wb-modal-content" style="border-color:#E63946;">
    <div class="wb-header">
      <div class="wb-title" style="color:#C1440E;">📑 南一 6上數學 作業簿隨堂測驗（第 2 單元 分數除法）</div>
      <button class="wb-close-btn" onclick="closeFracWbModal()">✕</button>
    </div>
    <div class="wb-tabs">
      <button class="wb-tab active" onclick="switchFracWbRev(4)" id="ftab4">第 4 回 (2-1 最簡分數、2-2 同分母除法)</button>
      <button class="wb-tab" onclick="switchFracWbRev(5)" id="ftab5">第 5 回 (2-3 異分母分數的除法)</button>
      <button class="wb-tab" onclick="switchFracWbRev(6)" id="ftab6">第 6 回 (2-4 應用題、2-5 商與被除數關係)</button>
    </div>
    <div id="fracWbQuizBody"></div>
    <div class="wb-submit-bar">
      <div class="wb-score-text" id="fracWbScoreDisp" style="color:#C1440E;">狀態：做題中（未交卷）</div>
      <div style="display:flex; gap:10px;">
        <button class="btn gold small" style="padding:10px 18px; border-radius:12px;" onclick="resetFracWbQuiz()">🔄 重填</button>
        <button class="wb-btn-submit" style="background:linear-gradient(135deg,#E63946,#C1440E);" onclick="gradeFracWbQuiz()">📝 交卷批改並看詳解</button>
      </div>
    </div>
  </div>
</div>

<script>
const U2_WB_DATA = {u2_data_js};
let fracCurrentRevId = 4;
let fracAnswers = {{}};

function openFracWbModal() {{
  document.getElementById('fracWbModalOverlay').classList.add('open');
  document.body.style.overflow = 'hidden';
  switchFracWbRev(4);
}}
function closeFracWbModal() {{
  document.getElementById('fracWbModalOverlay').classList.remove('open');
  document.body.style.overflow = '';
}}

function switchFracWbRev(revId) {{
  fracCurrentRevId = revId;
  fracAnswers = {{}};
  document.querySelectorAll('#fracWbModalOverlay .wb-tab').forEach((t, i) => t.classList.toggle('active', i + 4 === revId));
  document.getElementById('fracWbScoreDisp').textContent = '狀態：做題中（未交卷）';
  renderFracWbQuizBody();
}}

function renderFracWbQuizBody() {{
  const rev = U2_WB_DATA.reviews.find(r => r.review_id === fracCurrentRevId);
  const container = document.getElementById('fracWbQuizBody');
  if (!rev) return;

  let html = '';
  rev.sections.forEach((sec, sIdx) => {{
    html += `<div class="wb-sec-card">
      <div class="wb-sec-title" style="color:#C1440E;">📌 ${{sec.section_title}}</div>`;

    if (sec.type === 'multiple_choice') {{
      sec.items.forEach((item, iIdx) => {{
        const itemId = `u2_r${{fracCurrentRevId}}_s${{sIdx}}_${{iIdx}}`;
        html += `
          <div class="wb-q-item">
            <div class="wb-q-text">${{item.q}}</div>
            <div style="font-size:14px; margin-bottom:8px; color:#5C3317;">${{item.options.join('　')}}</div>
            <select class="wb-input" id="${{itemId}}" onchange="fracSave('${{itemId}}', this.value)">
              <option value="">選擇選項</option>
              <option value="①">①</option>
              <option value="②">②</option>
              <option value="③">③</option>
              <option value="④">④</option>
            </select>
            <div class="wb-sol-panel" id="sol_${{itemId}}">
              <div class="wb-sol-ans">標準答案：${{item.ans}}</div>
              <small>${{item.explanation}}</small>
            </div>
          </div>`;
      }});
    }} else if (sec.type === 'quotient_relations') {{
      html += '<div style="background:#FFF8F0; padding:10px; border-radius:10px; margin-bottom:12px; font-size:14px; border:1px solid #F4A261;"><b>算式代號庫：</b><br>';
      for (const [k, v] of Object.entries(sec.options_pool)) {{
        html += `【${{k}}】 ${{v}}　`;
      }}
      html += '</div>';
      sec.items.forEach((item, iIdx) => {{
        const itemId = `u2_r${{fracCurrentRevId}}_s${{sIdx}}_${{iIdx}}`;
        html += `
          <div class="wb-q-item">
            <div class="wb-q-text">${{item.q}}</div>
            <input type="text" class="wb-input" style="width:100%; max-width:240px;" id="${{itemId}}" placeholder="填寫代號如：ㄇ、ㄉ" oninput="fracSave('${{itemId}}', this.value)">
            <div class="wb-sol-panel" id="sol_${{itemId}}">
              <div class="wb-sol-ans">標準答案：${{item.ans}}</div>
              <small>${{item.explanation}}</small>
            </div>
          </div>`;
      }});
    }} else if (sec.type === 'comparison') {{
      html += '<div style="display:grid; grid-template-columns:repeat(auto-fill, minmax(240px, 1fr)); gap:10px;">';
      sec.items.forEach((item, iIdx) => {{
        const itemId = `u2_r${{fracCurrentRevId}}_s${{sIdx}}_${{iIdx}}`;
        html += `
          <div class="wb-q-item">
            <div class="wb-q-text">${{item.q}}</div>
            <select class="wb-input" id="${{itemId}}" onchange="fracSave('${{itemId}}', this.value)">
              <option value="">請選擇</option>
              <option value=">">&gt;</option>
              <option value="<">&lt;</option>
              <option value="=">=</option>
            </select>
            <div class="wb-sol-panel" id="sol_${{itemId}}">
              <div class="wb-sol-ans">答案：${{item.ans}}</div>
              <small>${{item.steps}}</small>
            </div>
          </div>`;
      }});
      html += '</div>';
    }} else if (sec.type === 'simplify_fraction' || sec.type === 'same_denominator_calc' || sec.type === 'diff_denominator_calc') {{
      html += '<div style="display:grid; grid-template-columns:repeat(auto-fill, minmax(230px, 1fr)); gap:10px;">';
      sec.items.forEach((item, iIdx) => {{
        const itemId = `u2_r${{fracCurrentRevId}}_s${{sIdx}}_${{iIdx}}`;
        html += `
          <div class="wb-q-item">
            <div class="wb-q-text">算式：<b>${{item.q}}</b></div>
            <input type="text" class="wb-input" style="width:100%;" id="${{itemId}}" placeholder="輸入最簡分數或答案" oninput="fracSave('${{itemId}}', this.value)">
            <div class="wb-sol-panel" id="sol_${{itemId}}">
              <div class="wb-sol-steps">${{item.steps}}</div>
              <div class="wb-sol-ans">標準答案：${{item.ans}}</div>
            </div>
          </div>`;
      }});
      html += '</div>';
    }} else if (sec.type === 'fill_in' || sec.type === 'word_problems') {{
      sec.items.forEach((item, iIdx) => {{
        const itemId = `u2_r${{fracCurrentRevId}}_s${{sIdx}}_${{iIdx}}`;
        html += `
          <div class="wb-q-item">
            <div class="wb-q-text">${{item.q}}</div>
            <input type="text" class="wb-input" style="width:100%; max-width:320px;" id="${{itemId}}" placeholder="輸入答案" oninput="fracSave('${{itemId}}', this.value)">
            <div class="wb-sol-panel" id="sol_${{itemId}}">
              <div class="wb-sol-steps">${{item.steps || ''}}</div>
              <div class="wb-sol-ans">標準答案：${{item.ans}}</div>
              ${{item.explanation ? `<small>${{item.explanation}}</small>` : ''}}
            </div>
          </div>`;
      }});
    }}

    html += '</div>';
  }});
  container.innerHTML = html;
}}

function fracSave(id, val) {{
  fracAnswers[id] = val.trim();
}}

function gradeFracWbQuiz() {{
  const rev = U2_WB_DATA.reviews.find(r => r.review_id === fracCurrentRevId);
  let total = 0, correct = 0;

  rev.sections.forEach((sec, sIdx) => {{
    sec.items.forEach((item, iIdx) => {{
      total++;
      const itemId = `u2_r${{fracCurrentRevId}}_s${{sIdx}}_${{iIdx}}`;
      const userVal = fracAnswers[itemId] || '';
      let isRight = false;

      const cleanUser = userVal.replace(/[\\s]/g, '').replace(/段|公尺|次|倍|瓶|元|包|公升/g, '');
      const cleanAns = String(item.ans).replace(/[\\s]/g, '').replace(/段|公尺|次|倍|瓶|元|包|公升/g, '');

      if (cleanUser === cleanAns || cleanUser.includes(cleanAns)) {{
        isRight = true;
      }} else if (cleanAns.includes('或')) {{
        const parts = cleanAns.split('或');
        isRight = parts.some(p => cleanUser === p.trim());
      }} else if (cleanAns.includes('、')) {{
        const parts = cleanAns.split('、');
        isRight = parts.every(p => cleanUser.includes(p.trim()));
      }}

      if (isRight) correct++;
      const panel = document.getElementById(`sol_${{itemId}}`);
      if (panel) {{
        panel.classList.add('show');
        panel.style.borderLeft = isRight ? '4px solid #57CC99' : '4px solid #E63946';
      }}
    }});
  }});

  const score = Math.round((correct / total) * 100);
  document.getElementById('fracWbScoreDisp').innerHTML = `得分：<b>${{score}} 分</b> (${{correct}} / ${{total}} 題正確)`;
  if (score >= 80 && window.confetti) {{
    confetti({{ particleCount: 100, spread: 70, origin: {{ y: 0.6 }} }});
  }}
  alert(`🎉 隨堂測驗批改完成！\\n\\n得分：${{score}} 分\\n所有題目的南一教用版標準解答、約分與直式算式已完整展示！✨`);
}}

function resetFracWbQuiz() {{
  fracAnswers = {{}};
  renderFracWbQuizBody();
  document.getElementById('fracWbScoreDisp').textContent = '狀態：做題中（未交卷）';
}}
</script>
'''

if "fracWbModalOverlay" not in frac_content:
    frac_content = frac_content.replace('</body>', wb_frac_addon + '\n</body>')
    with open("c:/Code/StudyCastle/fraction-division.html", "w", encoding="utf-8") as f:
        f.write(frac_content)
    print("Injected unit 2 into fraction-division.html successfully!")


# ==========================================
# 3. 注入 decimal-division.html (單元 3：第 7~9 回)
# ==========================================
with open("c:/Code/StudyCastle/decimal-division.html", "r", encoding="utf-8") as f:
    dec_content = f.read()

u3_data_js = json.dumps(ALL_WB["unit3"], ensure_ascii=False)

if "openDecWbModal()" not in dec_content:
    dec_top_target = '<div class="hdr-left">'
    dec_top_repl = '''<div class="hdr-left">
      <button class="back-btn" style="background:linear-gradient(135deg,#7209B7,#3A0CA3);color:#fff;border-color:#4CC9F0;" onclick="openDecWbModal()">
        <span>📑</span>
        <span>南一作業簿隨堂考 (第7~9回)</span>
      </button>'''
    dec_content = dec_content.replace(dec_top_target, dec_top_repl, 1)

wb_dec_addon = f'''
<!-- 南一作業簿隨堂測驗 Modal (小數除法) -->
<div class="wb-modal-overlay" id="decWbModalOverlay">
  <div class="wb-modal-content" style="background:#0F0E17; border-color:#4CC9F0; color:#FFF;">
    <div class="wb-header" style="border-color:rgba(76,201,240,0.3);">
      <div class="wb-title" style="color:#4CC9F0;">📑 南一 6上數學 作業簿隨堂測驗（第 3 單元 小數除法）</div>
      <button class="wb-close-btn" style="background:#1A1830; color:#FFF; border-color:#4CC9F0;" onclick="closeDecWbModal()">✕</button>
    </div>
    <div class="wb-tabs">
      <button class="wb-tab active" onclick="switchDecWbRev(7)">第 7 回 (3-1 整數除以小數)</button>
      <button class="wb-tab" onclick="switchDecWbRev(8)">第 8 回 (3-2 小數除以小數)</button>
      <button class="wb-tab" onclick="switchDecWbRev(9)">第 9 回 (3-3 商與被除數關係、3-4 概數與應用)</button>
    </div>
    <div id="decWbQuizBody"></div>
    <div class="wb-submit-bar" style="background:#0F0E17; border-color:rgba(76,201,240,0.4);">
      <div class="wb-score-text" id="decWbScoreDisp" style="color:#FFD166;">狀態：做題中（未交卷）</div>
      <div style="display:flex; gap:10px;">
        <button class="btn small" style="background:rgba(255,255,255,0.15); color:#fff; border-radius:12px; padding:10px 18px;" onclick="resetDecWbQuiz()">🔄 重填</button>
        <button class="wb-btn-submit" style="background:linear-gradient(135deg,#4CC9F0,#7209B7);" onclick="gradeDecWbQuiz()">📝 交卷批改並看詳解</button>
      </div>
    </div>
  </div>
</div>

<script>
const U3_WB_DATA = {u3_data_js};
let decCurrentRevId = 7;
let decAnswers = {{}};

function openDecWbModal() {{
  document.getElementById('decWbModalOverlay').classList.add('open');
  document.body.style.overflow = 'hidden';
  switchDecWbRev(7);
}}
function closeDecWbModal() {{
  document.getElementById('decWbModalOverlay').classList.remove('open');
  document.body.style.overflow = '';
}}

function switchDecWbRev(revId) {{
  decCurrentRevId = revId;
  decAnswers = {{}};
  document.querySelectorAll('#decWbModalOverlay .wb-tab').forEach((t, i) => t.classList.toggle('active', i + 7 === revId));
  document.getElementById('decWbScoreDisp').textContent = '狀態：做題中（未交卷）';
  renderDecWbQuizBody();
}}

function renderDecWbQuizBody() {{
  const rev = U3_WB_DATA.reviews.find(r => r.review_id === decCurrentRevId);
  const container = document.getElementById('decWbQuizBody');
  if (!rev) return;

  let html = '';
  rev.sections.forEach((sec, sIdx) => {{
    html += `<div class="wb-sec-card" style="background:rgba(26,24,48,0.9); border-color:rgba(76,201,240,0.3);">
      <div class="wb-sec-title" style="color:#FFD166; border-color:rgba(255,209,102,0.3);">📌 ${{sec.section_title}}</div>`;

    if (sec.type === 'table_rounding') {{
      html += `<table style="width:100%; border-collapse:collapse; text-align:center; margin-bottom:12px; font-size:14px;">
        <thead>
          <tr style="background:rgba(76,201,240,0.2); color:#4CC9F0;">
            <th style="padding:8px; border:1px solid rgba(255,255,255,0.2);">指定位數</th>
            <th style="padding:8px; border:1px solid rgba(255,255,255,0.2);">取到個位</th>
            <th style="padding:8px; border:1px solid rgba(255,255,255,0.2);">取到小數第一位</th>
            <th style="padding:8px; border:1px solid rgba(255,255,255,0.2);">取到小數第二位</th>
          </tr>
        </thead>
        <tbody>`;
      sec.table_data.forEach((row, rIdx) => {{
        const id1 = `u3_r${{decCurrentRevId}}_tab_${{rIdx}}_1`;
        const id2 = `u3_r${{decCurrentRevId}}_tab_${{rIdx}}_2`;
        const id3 = `u3_r${{decCurrentRevId}}_tab_${{rIdx}}_3`;
        html += `<tr>
          <td style="padding:8px; border:1px solid rgba(255,255,255,0.2); font-weight:800; color:#FFD166;">${{row.num}}</td>
          <td style="padding:8px; border:1px solid rgba(255,255,255,0.2);"><input type="text" class="wb-input" style="width:80px;" id="${{id1}}" oninput="decSave('${{id1}}', this.value)"><div class="wb-sol-panel" id="sol_${{id1}}">${{row.to_unit}}</div></td>
          <td style="padding:8px; border:1px solid rgba(255,255,255,0.2);"><input type="text" class="wb-input" style="width:80px;" id="${{id2}}" oninput="decSave('${{id2}}', this.value)"><div class="wb-sol-panel" id="sol_${{id2}}">${{row.to_tenth}}</div></td>
          <td style="padding:8px; border:1px solid rgba(255,255,255,0.2);"><input type="text" class="wb-input" style="width:80px;" id="${{id3}}" oninput="decSave('${{id3}}', this.value)"><div class="wb-sol-panel" id="sol_${{id3}}">${{row.to_hundredth}}</div></td>
        </tr>`;
      }});
      html += '</tbody></table>';
    }} else if (sec.type === 'comparison') {{
      html += '<div style="display:grid; grid-template-columns:repeat(auto-fill, minmax(230px, 1fr)); gap:10px;">';
      sec.items.forEach((item, iIdx) => {{
        const itemId = `u3_r${{decCurrentRevId}}_s${{sIdx}}_${{iIdx}}`;
        html += `
          <div class="wb-q-item" style="background:rgba(15,14,23,0.7); border-color:rgba(76,201,240,0.2);">
            <div class="wb-q-text" style="color:#FFF;">${{item.q}}</div>
            <select class="wb-input" id="${{itemId}}" onchange="decSave('${{itemId}}', this.value)">
              <option value="">請選擇</option>
              <option value=">">&gt;</option>
              <option value="<">&lt;</option>
              <option value="=">=</option>
            </select>
            <div class="wb-sol-panel" id="sol_${{itemId}}">
              <div class="wb-sol-ans">答案：${{item.ans}}</div>
              <small>${{item.steps}}</small>
            </div>
          </div>`;
      }});
      html += '</div>';
    }} else if (sec.type === 'vertical_division_calc' || sec.type === 'rounding_quotient_1' || sec.type === 'rounding_quotient_2') {{
      html += '<div style="display:grid; grid-template-columns:repeat(auto-fill, minmax(230px, 1fr)); gap:10px;">';
      sec.items.forEach((item, iIdx) => {{
        const itemId = `u3_r${{decCurrentRevId}}_s${{sIdx}}_${{iIdx}}`;
        html += `
          <div class="wb-q-item" style="background:rgba(15,14,23,0.7); border-color:rgba(76,201,240,0.2);">
            <div class="wb-q-text" style="color:#FFF;">題目：<b>${{item.q}}</b></div>
            <input type="text" class="wb-input" style="width:100%;" id="${{itemId}}" placeholder="輸入商數值" oninput="decSave('${{itemId}}', this.value)">
            <div class="wb-sol-panel" id="sol_${{itemId}}">
              <div class="wb-sol-steps">${{item.steps || item.calc || ''}}</div>
              <div class="wb-sol-ans">標準答案：${{item.ans}}</div>
            </div>
          </div>`;
      }});
      html += '</div>';
    }} else if (sec.type === 'fill_in' || sec.type === 'circle_correct' || sec.type === 'word_problems') {{
      sec.items.forEach((item, iIdx) => {{
        const itemId = `u3_r${{decCurrentRevId}}_s${{sIdx}}_${{iIdx}}`;
        html += `
          <div class="wb-q-item" style="background:rgba(15,14,23,0.7); border-color:rgba(76,201,240,0.2);">
            <div class="wb-q-text" style="color:#FFF;">${{item.q}}</div>
            <input type="text" class="wb-input" style="width:100%; max-width:320px;" id="${{itemId}}" placeholder="請輸入答案" oninput="decSave('${{itemId}}', this.value)">
            <div class="wb-sol-panel" id="sol_${{itemId}}">
              <div class="wb-sol-steps">${{item.steps || ''}}</div>
              <div class="wb-sol-ans">標準答案：${{item.ans}}</div>
              ${{item.explanation ? `<small>${{item.explanation}}</small>` : ''}}
            </div>
          </div>`;
      }});
    }}

    html += '</div>';
  }});
  container.innerHTML = html;
}}

function decSave(id, val) {{
  decAnswers[id] = val.trim();
}}

function gradeDecWbQuiz() {{
  const rev = U3_WB_DATA.reviews.find(r => r.review_id === decCurrentRevId);
  let total = 0, correct = 0;

  rev.sections.forEach((sec, sIdx) => {{
    if (sec.type === 'table_rounding') {{
      sec.table_data.forEach((row, rIdx) => {{
        ['1', '2', '3'].forEach((k, colIdx) => {{
          total++;
          const itemId = `u3_r${{decCurrentRevId}}_tab_${{rIdx}}_${{k}}`;
          const expected = (colIdx === 0 ? row.to_unit : colIdx === 1 ? row.to_tenth : row.to_hundredth);
          const isRight = (decAnswers[itemId] || '').trim() === expected;
          if (isRight) correct++;
          const p = document.getElementById(`sol_${{itemId}}`);
          if (p) {{ p.classList.add('show'); p.style.color = isRight ? '#06D6A0' : '#F72585'; }}
        }});
      }});
    }} else {{
      sec.items.forEach((item, iIdx) => {{
        total++;
        const itemId = `u3_r${{decCurrentRevId}}_s${{sIdx}}_${{iIdx}}`;
        const userVal = decAnswers[itemId] || '';
        let isRight = false;

        const cleanUser = userVal.replace(/[\\s]/g, '').replace(/袋|倍|朵|分鐘|公升|公分|公尺|公斤|坪|包|約/g, '');
        const cleanAns = String(item.ans).replace(/[\\s]/g, '').replace(/袋|倍|朵|分鐘|公升|公分|公尺|公斤|坪|包|約/g, '');

        if (cleanUser === cleanAns || cleanUser.includes(cleanAns)) {{
          isRight = true;
        }} else if (cleanAns.includes('、')) {{
          const parts = cleanAns.split('、');
          isRight = parts.every(p => cleanUser.includes(p.trim()));
        }} else if (cleanAns.includes(',')) {{
          const parts = cleanAns.split(',');
          isRight = parts.every(p => cleanUser.includes(p.trim()));
        }}

        if (isRight) correct++;
        const panel = document.getElementById(`sol_${{itemId}}`);
        if (panel) {{
          panel.classList.add('show');
          panel.style.borderLeft = isRight ? '4px solid #06D6A0' : '4px solid #F72585';
        }}
      }});
    }}
  }});

  const score = Math.round((correct / total) * 100);
  document.getElementById('decWbScoreDisp').innerHTML = `得分：<b>${{score}} 分</b> (${{correct}} / ${{total}} 題正確)`;
  if (score >= 80 && window.confetti) {{
    confetti({{ particleCount: 100, spread: 70, origin: {{ y: 0.6 }} }});
  }}
  alert(`🎉 隨堂測驗批改完成！\\n\\n得分：${{score}} 分\\n所有題目的南一教用版直式計算、四捨五入過程與標準解答已展開顯示！✨`);
}}

function resetDecWbQuiz() {{
  decAnswers = {{}};
  renderDecWbQuizBody();
  document.getElementById('decWbScoreDisp').textContent = '狀態：做題中（未交卷）';
}}
</script>
'''

if "decWbModalOverlay" not in dec_content:
    dec_content = dec_content.replace('</body>', wb_dec_addon + '\n</body>')
    with open("c:/Code/StudyCastle/decimal-division.html", "w", encoding="utf-8") as f:
        f.write(dec_content)
    print("Injected unit 3 into decimal-division.html successfully!")

