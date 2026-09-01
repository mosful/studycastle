# -*- coding: utf-8 -*-
"""
將作業簿第 1~3 回、第 4~6 回、第 7~9 回的完整題目與批改模組整合到
prime.html, fraction-division.html, decimal-division.html 中。
"""

import json

with open("c:/Code/StudyCastle/workbook_6th_math_u1_u4.json", "r", encoding="utf-8") as f:
    wb_data = json.load(f)

# 1. 處理 prime.html
# 讀取現有 prime.html
with open("c:/Code/StudyCastle/prime.html", "r", encoding="utf-8") as f:
    prime_html = f.read()

# 在 prime.html 加入作業簿按鈕與模組
u1_json_str = json.dumps(wb_data["unit1"], ensure_ascii=False)

prime_wb_css = """
  /* 作業簿隨堂考樣式 */
  .wb-toggle-btn {
    background: linear-gradient(135deg, #FF6B5B 0%, #FF8E53 100%);
    border: 2px solid #FFF;
    border-radius: 50px;
    color: #FFF;
    font-size: 13.5px;
    font-weight: 800;
    padding: 6px 14px;
    cursor: pointer;
    box-shadow: 0 4px 10px rgba(0,0,0,0.25);
    display: inline-flex;
    align-items: center;
    gap: 5px;
    transition: transform 0.2s;
  }
  .wb-toggle-btn:hover { transform: scale(1.05); }

  .wb-modal-overlay {
    display: none;
    position: fixed;
    inset: 0;
    background: rgba(11, 79, 108, 0.85);
    backdrop-filter: blur(8px);
    z-index: 1000;
    overflow-y: auto;
    padding: 20px 12px 60px;
  }
  .wb-modal-overlay.open { display: block; }

  .wb-modal-content {
    background: #FFFDF5;
    border: 3px solid #1C86A6;
    border-radius: 24px;
    max-width: 820px;
    margin: 0 auto;
    padding: 24px 20px;
    color: #12303B;
    box-shadow: 0 16px 40px rgba(0,0,0,0.4);
    position: relative;
  }

  .wb-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 2px solid #E9D9A6;
    padding-bottom: 12px;
    margin-bottom: 16px;
  }
  .wb-title { font-size: 22px; font-weight: 800; color: #0B4F6C; display: flex; align-items: center; gap: 8px; }
  .wb-close-btn {
    width: 38px; height: 38px; border-radius: 50%; border: 2px solid #12303B; background: #FFF;
    font-weight: 900; font-size: 18px; cursor: pointer;
  }

  .wb-tabs { display: flex; gap: 8px; margin-bottom: 16px; flex-wrap: wrap; }
  .wb-tab {
    flex: 1; min-width: 140px; padding: 10px 14px; border-radius: 12px; border: 2px solid #E9D9A6;
    background: #FFF; font-weight: 800; font-size: 14px; cursor: pointer; color: #5C6B70;
    text-align: center; transition: all 0.2s;
  }
  .wb-tab.active { background: #FFB703; border-color: #D48800; color: #12303B; box-shadow: 0 4px 0 #D48800; }

  .wb-sec-card { background: #FFF; border: 2px solid #E9D9A6; border-radius: 16px; padding: 18px; margin-bottom: 16px; }
  .wb-sec-title { font-size: 16px; font-weight: 800; color: #0B4F6C; margin-bottom: 12px; border-bottom: 1.5px dashed #E9D9A6; padding-bottom: 6px; }

  .wb-q-item { background: #FBF0D3; border-radius: 12px; padding: 14px; margin-bottom: 12px; border: 1px solid #E9D9A6; }
  .wb-q-text { font-size: 15px; font-weight: 600; line-height: 1.6; margin-bottom: 8px; }

  .wb-input {
    background: #FFF; border: 2px solid #1C86A6; border-radius: 8px; padding: 6px 12px;
    font-size: 15px; font-weight: 700; color: #12303B; outline: none; min-width: 120px;
  }
  .wb-input:focus { border-color: #FF6B5B; box-shadow: 0 0 8px rgba(255,107,91,0.4); }

  .wb-sol-panel { display: none; background: #E6F8F6; border: 1.5px solid #2EC4B6; border-radius: 10px; padding: 12px; margin-top: 10px; font-size: 14px; }
  .wb-sol-panel.show { display: block; }
  .wb-sol-steps { font-family: 'Fredoka', monospace; background: #FFF; padding: 8px; border-radius: 6px; margin: 6px 0; white-space: pre-wrap; color: #0B4F6C; font-weight: 700; }
  .wb-sol-ans { color: #D48800; font-weight: 800; }

  .wb-submit-bar {
    position: sticky; bottom: 0; background: #FFFDF5; border-top: 2px solid #E9D9A6;
    padding: 14px 0 0; display: flex; justify-content: space-between; align-items: center;
    flex-wrap: wrap; gap: 10px;
  }
  .wb-score-text { font-size: 20px; font-weight: 800; color: #0B4F6C; }
  .wb-btn-submit {
    background: linear-gradient(135deg, #2EC4B6 0%, #0E7C7B 100%);
    border: none; color: #FFF; font-weight: 800; font-size: 15px; padding: 10px 24px;
    border-radius: 12px; cursor: pointer; box-shadow: 0 4px 0 #0A5A59;
  }
"""

print("Preparing injection scripts...")
