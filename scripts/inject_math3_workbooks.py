# -*- coding: utf-8 -*-
"""
注入 3上數學作業簿隨堂考模組到：
1. math3_numbers.html (第 1 單元：數到10000，第 1~3 回)
2. math3_addition.html (第 2 單元：四位數的加減，第 4~6 回)
3. math3_multiplication.html (第 3 單元：乘法，第 7~9 回)
4. math3_measurement.html (第 4 單元：幾毫米，第 10~12 回)
"""

import json
import re

with open("c:/Code/StudyCastle/math3_workbook_u1_u4.json", "r", encoding="utf-8") as f:
    ALL_WB = json.load(f)

# 共用 CSS
WB_CSS = """
<!-- 作業簿隨堂測驗樣式 -->
<style>
.wb-modal-overlay {
  display: none;
  position: fixed;
  inset: 0;
  background: rgba(11, 25, 44, 0.85);
  backdrop-filter: blur(8px);
  z-index: 1000;
  overflow-y: auto;
  padding: 20px 12px 60px;
}
.wb-modal-overlay.open { display: block; }
.wb-modal-content {
  background: #FFFDF5;
  border: 3px solid #F59E0B;
  border-radius: 24px;
  max-width: 820px;
  margin: 0 auto;
  padding: 24px 20px;
  color: #1E293B;
  box-shadow: 0 16px 40px rgba(0,0,0,0.4);
}
.wb-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-bottom: 2px solid #E2E8F0;
  padding-bottom: 12px;
  margin-bottom: 16px;
}
.wb-title { font-size: 20px; font-weight: 800; color: #1E293B; display: flex; align-items: center; gap: 8px; }
.wb-close-btn {
  width: 38px; height: 38px; border-radius: 50%; border: 2px solid #1E293B; background: #FFF;
  font-weight: 900; font-size: 18px; cursor: pointer; color: #1E293B;
}
.wb-tabs { display: flex; gap: 8px; margin-bottom: 16px; flex-wrap: wrap; }
.wb-tab {
  flex: 1; min-width: 140px; padding: 10px 14px; border-radius: 12px; border: 2px solid #CBD5E1;
  background: #FFF; font-weight: 800; font-size: 13.5px; cursor: pointer; color: #64748B;
  text-align: center; transition: all 0.2s;
}
.wb-tab.active { background: #F59E0B; border-color: #D97706; color: #FFF; box-shadow: 0 4px 0 #D97706; }
.wb-sec-card { background: #FFF; border: 2px solid #E2E8F0; border-radius: 16px; padding: 18px; margin-bottom: 16px; }
.wb-sec-title { font-size: 16px; font-weight: 800; color: #0F172A; margin-bottom: 12px; border-bottom: 1.5px dashed #CBD5E1; padding-bottom: 6px; }
.wb-q-item { background: #FEF3C7; border-radius: 14px; padding: 16px; margin-bottom: 14px; border: 2px solid #FDE68A; transition: all 0.3s ease; position: relative; }
.wb-q-item.is-correct { border: 3px solid #10B981 !important; background: #ECFDF5 !important; }
.wb-q-item.is-wrong { border: 3px solid #EF4444 !important; background: #FEF2F2 !important; }
.wb-q-badge {
  display: inline-block; padding: 3px 10px; border-radius: 8px; font-size: 13px; font-weight: 800; margin-bottom: 8px;
}
.wb-q-badge.correct { background: #10B981; color: #FFF; }
.wb-q-badge.wrong { background: #EF4444; color: #FFF; }

.wb-q-text { font-size: 15.5px; font-weight: 700; line-height: 1.6; margin-bottom: 10px; color: #1E293B; }

/* 作業簿選項大按鈕網格 (直接點選) */
.wb-opt-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(130px, 1fr));
  gap: 10px;
  margin-top: 8px;
}
.wb-opt-btn {
  background: #FFFFFF;
  border: 2px solid #0284C7;
  border-radius: 12px;
  padding: 10px 14px;
  font-size: 15px;
  font-weight: 800;
  color: #0F172A;
  cursor: pointer;
  transition: all 0.15s ease;
  text-align: center;
  box-shadow: 0 3px 0 rgba(0, 0, 0, 0.15);
  user-select: none;
}
.wb-opt-btn:hover {
  background: #EFF6FF;
  border-color: #2563EB;
  transform: translateY(-2px);
  box-shadow: 0 5px 0 rgba(0, 0, 0, 0.2);
}
.wb-opt-btn:active {
  transform: translateY(2px);
  box-shadow: 0 1px 0 rgba(0, 0, 0, 0.15);
}
.wb-opt-btn.selected {
  background: #F59E0B !important;
  border-color: #D97706 !important;
  color: #FFFFFF !important;
  box-shadow: 0 4px 0 #D97706 !important;
  transform: scale(1.02);
}

/* 批改鮮明顏色：選對 (翠綠色)、選錯 (鮮紅色)、正確答案提示 (綠色虛線) */
.wb-opt-btn.opt-correct {
  background: linear-gradient(135deg, #10B981, #059669) !important;
  color: #FFFFFF !important;
  border: 3px solid #047857 !important;
  box-shadow: 0 0 12px rgba(16, 185, 129, 0.6) !important;
  transform: scale(1.03);
}
.wb-opt-btn.opt-wrong {
  background: linear-gradient(135deg, #EF4444, #DC2626) !important;
  color: #FFFFFF !important;
  border: 3px solid #991B1B !important;
  box-shadow: 0 0 12px rgba(239, 68, 68, 0.6) !important;
  transform: scale(1.03);
}
.wb-opt-btn.opt-should-be {
  background: #D1FAE5 !important;
  color: #065F46 !important;
  border: 3px dashed #10B981 !important;
  font-weight: 900 !important;
}

.wb-sol-panel { display: none; background: #F0FDF4; border: 2px solid #86EFAC; border-radius: 10px; padding: 12px; margin-top: 12px; font-size: 14px; }
.wb-sol-panel.show { display: block; }
.wb-sol-steps { font-family: 'Noto Sans TC', sans-serif; background: #FFF; padding: 8px 12px; border-radius: 6px; margin: 6px 0; white-space: pre-wrap; color: #0F172A; font-weight: 700; line-height: 1.6; }
.wb-sol-ans { color: #059669; font-weight: 900; font-size: 15px; }
.wb-submit-bar {
  position: sticky; bottom: 0; background: #FFFDF5; border-top: 2px solid #E2E8F0;
  padding: 14px 0 0; display: flex; justify-content: space-between; align-items: center;
  flex-wrap: wrap; gap: 10px; z-index: 10;
}
.wb-score-text { font-size: 18px; font-weight: 800; color: #0F172A; }
.wb-btn-submit {
  background: linear-gradient(135deg, #10B981 0%, #059669 100%);
  border: none; color: #FFF; font-weight: 800; font-size: 15px; padding: 10px 24px;
  border-radius: 12px; cursor: pointer; box-shadow: 0 4px 0 #047857;
}
.wb-btn-reset {
  background: #F1F5F9; border: 2px solid #CBD5E1; color: #334155; font-weight: 800; font-size: 14px;
  padding: 10px 18px; border-radius: 12px; cursor: pointer;
}
@media (max-width: 480px) {
  .wb-opt-grid { grid-template-columns: 1fr; }
}
</style>
"""

def generate_wb_script(unit_data, unit_code):
    data_json = json.dumps(unit_data, ensure_ascii=False)
    return f"""
<script>
const WB_DATA_{unit_code} = {data_json};

let wbCurrentRevId = {unit_data['reviews'][0]['review_id']};
let wbAnswers = {{}};

function openWbModal() {{
  if(typeof playSound === 'function') playSound('click');
  document.getElementById('wbModalOverlay').classList.add('open');
  document.body.style.overflow = 'hidden';
  switchWbRev({unit_data['reviews'][0]['review_id']});
}}
function closeWbModal() {{
  document.getElementById('wbModalOverlay').classList.remove('open');
  document.body.style.overflow = '';
}}

function switchWbRev(revId) {{
  wbCurrentRevId = revId;
  wbAnswers = {{}};
  document.querySelectorAll('.wb-tab').forEach(t => {{
    t.classList.toggle('active', parseInt(t.getAttribute('data-rev')) === revId);
  }});
  document.getElementById('wbScoreDisp').textContent = '狀態：做題中（未交卷）';
  renderWbQuizBody();
}}

function wbPick(itemId, val, btnEl) {{
  if(typeof playSound === 'function') playSound('click');
  wbAnswers[itemId] = val;
  const parent = btnEl.closest('.wb-opt-grid');
  if (parent) {{
    parent.querySelectorAll('.wb-opt-btn').forEach(b => b.classList.remove('selected'));
    btnEl.classList.add('selected');
  }}
}}

function renderWbQuizBody() {{
  const rev = WB_DATA_{unit_code}.reviews.find(r => r.review_id === wbCurrentRevId);
  const container = document.getElementById('wbQuizBody');
  if (!rev) return;

  let html = '';
  rev.sections.forEach((sec, sIdx) => {{
    html += `<div class="wb-sec-card">
      <div class="wb-sec-title">📌 ${{sec.section_title}}</div>`;

    sec.items.forEach((item, iIdx) => {{
      const itemId = `{unit_code}_r${{wbCurrentRevId}}_s${{sIdx}}_${{iIdx}}`;
      const qTitle = item.q;
      const opts = (item.options ? [...item.options] : [item.ans]).sort(() => Math.random() - 0.5);

      html += `
        <div class="wb-q-item">
          <div class="wb-q-text">${{qTitle}}</div>
          <div class="wb-opt-grid">
            ${{opts.map(opt => `
              <button type="button" class="wb-opt-btn ${{wbAnswers[itemId] === opt ? 'selected' : ''}}" onclick="wbPick('${{itemId}}', '${{opt}}', this)">
                ${{opt}}
              </button>
            `).join('')}}
          </div>
          <div class="wb-sol-panel" id="sol_${{itemId}}">
            <div class="wb-sol-steps">${{item.steps || item.explanation || ''}}</div>
            <div class="wb-sol-ans">標準答案：${{item.ans}}</div>
          </div>
        </div>`;
    }});

    html += '</div>';
  }});
  container.innerHTML = html;
}}

function gradeWbQuiz() {{
  const rev = WB_DATA_{unit_code}.reviews.find(r => r.review_id === wbCurrentRevId);
  let total = 0, correct = 0;

  rev.sections.forEach((sec, sIdx) => {{
    sec.items.forEach((item, iIdx) => {{
      total++;
      const itemId = `{unit_code}_r${{wbCurrentRevId}}_s${{sIdx}}_${{iIdx}}`;
      const userVal = wbAnswers[itemId] || '';
      let isRight = false;

      const targetAns = item.ans;
      const cleanUser = userVal.replace(/[\\s\\*xX×]/g, '').replace(/公分|公尺|毫米|顆|張|枝|片|盒|元|個|人|塊|罐|分鐘|公克|m|cm|mm/g, '');
      const cleanAns = String(targetAns).replace(/[\\s\\*xX×]/g, '').replace(/公分|公尺|毫米|顆|張|枝|片|盒|元|個|人|塊|罐|分鐘|公克|m|cm|mm/g, '');

      if (cleanUser === cleanAns || cleanUser.includes(cleanAns) || userVal === targetAns) {{
        isRight = true;
      }}

      if (isRight) correct++;

      const panel = document.getElementById(`sol_${{itemId}}`);
      const qItem = panel ? panel.closest('.wb-q-item') : null;
      
      if (qItem) {{
        qItem.classList.remove('is-correct', 'is-wrong');
        qItem.classList.add(isRight ? 'is-correct' : 'is-wrong');
        
        const oldBadge = qItem.querySelector('.wb-q-badge');
        if (oldBadge) oldBadge.remove();
        
        const badge = document.createElement('div');
        badge.className = `wb-q-badge ${{isRight ? 'correct' : 'wrong'}}`;
        badge.innerHTML = isRight ? '✓ 答對了！' : (userVal ? '✕ 答錯了！' : '⚠️ 未作答！');
        qItem.insertBefore(badge, qItem.firstChild);

        const btns = qItem.querySelectorAll('.wb-opt-btn');
        btns.forEach(btn => {{
          btn.classList.remove('opt-correct', 'opt-wrong', 'opt-should-be');
          const btnVal = btn.textContent.trim();
          const cleanBtn = btnVal.replace(/[\\s\\*xX×]/g, '').replace(/公分|公尺|毫米|顆|張|枝|片|盒|元|個|人|塊|罐|分鐘|公克|m|cm|mm/g, '');
          
          if (btnVal === userVal) {{
            if (isRight) {{
              btn.classList.add('opt-correct');
              btn.innerHTML = `✓ ${{btnVal}}`;
            }} else {{
              btn.classList.add('opt-wrong');
              btn.innerHTML = `✕ ${{btnVal}}`;
            }}
          }} else if ((cleanBtn === cleanAns || btnVal === targetAns) && !isRight) {{
            btn.classList.add('opt-should-be');
            btn.innerHTML = `★ 正解：${{btnVal}}`;
          }}
        }});
      }}

      if (panel) {{
        panel.classList.add('show');
        panel.style.borderLeft = isRight ? '6px solid #10B981' : '6px solid #EF4444';
      }}
    }});
  }});

  const score = Math.round((correct / total) * 100);
  document.getElementById('wbScoreDisp').innerHTML = `得分：<b>${{score}} 分</b> (${{correct}} / ${{total}} 題正確)`;
  if (score >= 80) {{
    if(typeof playSound === 'function') playSound('correct');
    if (typeof confetti === 'function') confetti({{ particleCount: 100, spread: 70, origin: {{ y: 0.6 }} }});
  }} else {{
    if(typeof playSound === 'function') playSound('wrong');
  }}
  alert(`🎉 隨堂測驗批改完成！\\n\\n得分：${{score}} 分\\n綠色為答對選項，紅色為答錯選項，綠色虛線為標準正解！✨`);
}}

function resetWbQuiz() {{
  wbAnswers = {{}};
  renderWbQuizBody();
  document.getElementById('wbScoreDisp').textContent = '狀態：做題中（未交卷）';
}}
</script>
"""

def generate_wb_modal(unit_data, unit_code):
    reviews = unit_data['reviews']
    tabs_html = ""
    for idx, rev in enumerate(reviews):
        active_cls = "active" if idx == 0 else ""
        tabs_html += f'<button class="wb-tab {active_cls}" data-rev="{rev["review_id"]}" onclick="switchWbRev({rev["review_id"]})">第 {rev["review_id"]} 回 ({rev["range"]})</button>\n'

    return f"""
<!-- 作業簿隨堂測驗 Modal -->
<div class="wb-modal-overlay" id="wbModalOverlay">
  <div class="wb-modal-content">
    <div class="wb-header">
      <div class="wb-title">📑 3上數學 作業簿隨堂測驗（第 {unit_data['unit_id']} 單元・{unit_data['title']}）</div>
      <button class="wb-close-btn" onclick="closeWbModal()">✕</button>
    </div>
    <div class="wb-tabs" id="wbTabs">
      {tabs_html}
    </div>
    <div id="wbQuizBody"></div>
    <div class="wb-submit-bar">
      <div class="wb-score-text" id="wbScoreDisp">狀態：做題中（未交卷）</div>
      <div style="display:flex; gap:10px;">
        <button class="wb-btn-reset" onclick="resetWbQuiz()">🔄 重填</button>
        <button class="wb-btn-submit" onclick="gradeWbQuiz()">📝 交卷批改並看詳解</button>
      </div>
    </div>
  </div>
</div>
"""

# 針對 4 個檔案進行注入
TARGET_CONFIGS = [
    {
        "file": "c:/Code/StudyCastle/math3_numbers.html",
        "unit_key": "unit1",
        "unit_code": "u1",
        "rev_desc": "第1~3回"
    },
    {
        "file": "c:/Code/StudyCastle/math3_addition.html",
        "unit_key": "unit2",
        "unit_code": "u2",
        "rev_desc": "第4~6回"
    },
    {
        "file": "c:/Code/StudyCastle/math3_multiplication.html",
        "unit_key": "unit3",
        "unit_code": "u3",
        "rev_desc": "第7~9回"
    },
    {
        "file": "c:/Code/StudyCastle/math3_measurement.html",
        "unit_key": "unit4",
        "unit_code": "u4",
        "rev_desc": "第10~12回"
    },
]

for cfg in TARGET_CONFIGS:
    fpath = cfg["file"]
    with open(fpath, "r", encoding="utf-8") as f:
        html = f.read()

    unit_data = ALL_WB[cfg["unit_key"]]
    code = cfg["unit_code"]
    rev_desc = cfg["rev_desc"]

    # 1. 在 top-bar 加入按鈕
    # 尋找 <a href="portal.html" class="nav-btn">...</a> 後面插入
    if "openWbModal()" not in html:
        btn_html = f'''<button class="nav-btn" style="background:linear-gradient(135deg,#F59E0B,#D97706);color:#fff;border-color:rgba(255,255,255,0.4);" onclick="openWbModal()">
        <span>📑</span>
        <span>作業簿隨堂考 ({rev_desc})</span>
      </button>'''
        # 替換 top-bar 內部
        pattern = r'(<div class="top-bar">[\s\S]*?<a href="portal\.html"[^>]*>.*?</a>)'
        html = re.sub(pattern, r'\1\n      ' + btn_html, html, count=1)

    # 2. 加入 Modal HTML 與 CSS (放在 </body> 之前)
    modal_html = generate_wb_modal(unit_data, code)
    script_html = generate_wb_script(unit_data, code)
    addon = f"{modal_html}\n{WB_CSS}\n{script_html}"

    if "id=\"wbModalOverlay\"" not in html:
        html = html.replace("</body>", f"{addon}\n</body>")

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Successfully injected workbook into {fpath}!")

print("All 4 math3 files updated with workbook modal!")
