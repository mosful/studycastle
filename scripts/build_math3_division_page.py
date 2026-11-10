# -*- coding: utf-8 -*-
"""
產生 國小數學 3上 第 6 單元【除法大冒險】math3_division.html
"""

html_content = '''<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>國小 3 上數學 第 6 單元：除法大冒險 | 學習城堡</title>
    <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@400;500;700;900&family=Fredoka:wght@600;700&display=swap" rel="stylesheet">
    <style>
        :root {
            --primary: #1E3A8A;
            --primary-light: #3B82F6;
            --primary-bg: #EFF6FF;
            --accent: #0D9488;
            --accent-light: #14B8A6;
            --accent-bg: #F0FDFA;
            --amber: #D97706;
            --rose: #E11D48;
            --text-dark: #1E293B;
            --text-gray: #64748B;
            --card-bg: #FFFFFF;
            --radius-lg: 24px;
            --radius-md: 16px;
            --radius-sm: 10px;
            --shadow: 0 10px 25px -5px rgba(30, 58, 138, 0.1), 0 8px 10px -6px rgba(30, 58, 138, 0.1);
            --shadow-hover: 0 20px 30px -10px rgba(30, 58, 138, 0.2);
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            -webkit-tap-highlight-color: transparent;
        }

        body {
            font-family: 'Noto Sans TC', sans-serif;
            background: linear-gradient(135deg, #F8FAFC 0%, #EFF6FF 100%);
            color: var(--text-dark);
            min-height: 100vh;
            padding-bottom: 80px;
            line-height: 1.6;
        }

        .header-nav {
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(12px);
            position: sticky;
            top: 0;
            z-index: 100;
            padding: 14px 24px;
            border-bottom: 1px solid rgba(226, 232, 240, 0.8);
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .back-btn {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            color: var(--primary);
            text-decoration: none;
            font-weight: 700;
            font-size: 0.95rem;
            padding: 8px 16px;
            border-radius: 999px;
            background: var(--primary-bg);
            transition: all 0.2s;
        }

        .back-btn:hover {
            background: #DBEAFE;
            transform: translateX(-3px);
        }

        .container {
            max-width: 1000px;
            margin: 0 auto;
            padding: 24px 20px;
        }

        /* Hero */
        .hero {
            background: linear-gradient(135deg, #1E3A8A 0%, #2563EB 50%, #0D9488 100%);
            color: white;
            padding: 40px 32px;
            border-radius: var(--radius-lg);
            margin-bottom: 32px;
            box-shadow: var(--shadow);
            position: relative;
            overflow: hidden;
        }

        .hero::after {
            content: "➗";
            font-size: 130px;
            position: absolute;
            right: 20px;
            bottom: -20px;
            opacity: 0.18;
            pointer-events: none;
        }

        .hero-badge {
            display: inline-block;
            background: rgba(255, 255, 255, 0.25);
            padding: 6px 14px;
            border-radius: 999px;
            font-size: 0.85rem;
            font-weight: 700;
            letter-spacing: 1px;
            margin-bottom: 12px;
            border: 1px solid rgba(255, 255, 255, 0.4);
        }

        .hero h1 {
            font-size: 2.2rem;
            font-weight: 900;
            margin-bottom: 12px;
            line-height: 1.3;
        }

        .hero p {
            font-size: 1.05rem;
            opacity: 0.95;
            max-width: 650px;
        }

        /* Grid */
        .grid-2 {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 24px;
            margin-bottom: 32px;
        }

        .card {
            background: var(--card-bg);
            border-radius: var(--radius-lg);
            padding: 28px;
            box-shadow: var(--shadow);
            border: 1px solid #E2E8F0;
            transition: transform 0.2s, box-shadow 0.2s;
        }

        .card:hover {
            transform: translateY(-3px);
            box-shadow: var(--shadow-hover);
        }

        .card-title {
            display: flex;
            align-items: center;
            gap: 12px;
            font-size: 1.3rem;
            font-weight: 800;
            color: var(--primary);
            margin-bottom: 16px;
            border-bottom: 2px solid var(--primary-bg);
            padding-bottom: 12px;
        }

        .card-icon {
            font-size: 1.6rem;
            background: var(--primary-bg);
            width: 44px;
            height: 44px;
            display: flex;
            align-items: center;
            justify-content: center;
            border-radius: 12px;
        }

        .highlight-box {
            background: var(--primary-bg);
            border-left: 5px solid var(--primary);
            padding: 14px 18px;
            border-radius: 0 var(--radius-sm) var(--radius-sm) 0;
            margin: 14px 0;
            font-weight: 500;
        }

        .alert-box {
            background: #FEF3C7;
            border-left: 5px solid var(--amber);
            padding: 14px 18px;
            border-radius: 0 var(--radius-sm) var(--radius-sm) 0;
            margin: 14px 0;
            color: #92400E;
            font-weight: 600;
        }

        /* 除法直式模擬器 */
        .interactive-tool {
            background: #FFFFFF;
            border-radius: var(--radius-lg);
            padding: 32px;
            margin-bottom: 36px;
            box-shadow: var(--shadow);
            border: 2px solid #BFDBFE;
        }

        .tool-title {
            font-size: 1.4rem;
            font-weight: 800;
            color: var(--primary);
            display: flex;
            align-items: center;
            gap: 10px;
            margin-bottom: 20px;
        }

        .tool-inputs {
            display: flex;
            flex-wrap: wrap;
            gap: 16px;
            align-items: center;
            margin-bottom: 24px;
        }

        .input-group {
            display: flex;
            align-items: center;
            gap: 8px;
            font-weight: 700;
            font-size: 1.1rem;
        }

        .tool-input {
            width: 90px;
            padding: 10px 14px;
            font-size: 1.2rem;
            font-weight: 800;
            border: 2px solid #CBD5E1;
            border-radius: var(--radius-sm);
            text-align: center;
            outline: none;
            color: var(--primary);
        }

        .tool-input:focus {
            border-color: var(--primary-light);
            box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.2);
        }

        .btn-calc {
            background: linear-gradient(135deg, var(--primary) 0%, var(--primary-light) 100%);
            color: white;
            border: none;
            padding: 10px 24px;
            border-radius: var(--radius-sm);
            font-weight: 700;
            font-size: 1.05rem;
            cursor: pointer;
            box-shadow: 0 4px 12px rgba(37, 99, 235, 0.3);
            transition: all 0.2s;
        }

        .btn-calc:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 16px rgba(37, 99, 235, 0.4);
        }

        .division-visual-board {
            display: flex;
            flex-wrap: wrap;
            gap: 32px;
            align-items: flex-start;
            background: #F8FAFC;
            padding: 24px;
            border-radius: var(--radius-md);
            border: 1px dashed #94A3B8;
        }

        .vertical-math {
            font-family: 'Fredoka', 'Noto Sans TC', monospace;
            font-size: 1.8rem;
            font-weight: 700;
            line-height: 1.2;
            display: inline-block;
            background: #FFFFFF;
            padding: 20px 30px;
            border-radius: 14px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.06);
            border: 1px solid #E2E8F0;
        }

        .vm-quotient {
            text-align: right;
            padding-right: 12px;
            color: var(--primary);
        }

        .vm-house {
            display: flex;
            align-items: baseline;
            border-top: 3px solid #1E293B;
            padding-top: 4px;
        }

        .vm-divisor {
            color: #D97706;
            margin-right: 4px;
        }

        .vm-bracket {
            border-left: 3px solid #1E293B;
            border-radius: 6px 0 0 0;
            padding-left: 10px;
            color: #0F172A;
        }

        .vm-product {
            text-align: right;
            border-bottom: 2px solid #1E293B;
            padding-right: 12px;
            margin-top: 4px;
            color: #64748B;
        }

        .vm-remainder {
            text-align: right;
            padding-right: 12px;
            margin-top: 4px;
            color: var(--rose);
        }

        .result-explanation {
            flex: 1;
            min-width: 260px;
            background: #FFFFFF;
            padding: 20px;
            border-radius: var(--radius-md);
            border: 1px solid #E2E8F0;
        }

        .result-explanation h4 {
            color: var(--primary);
            font-size: 1.2rem;
            margin-bottom: 12px;
        }

        /* 奇偶檢驗機 */
        .parity-box {
            display: flex;
            gap: 16px;
            align-items: center;
            flex-wrap: wrap;
            margin-top: 14px;
        }

        .parity-tag {
            display: inline-block;
            padding: 8px 16px;
            border-radius: 999px;
            font-weight: 800;
            font-size: 1.1rem;
        }

        .tag-even {
            background: #DCFCE7;
            color: #15803D;
            border: 2px solid #86EFAC;
        }

        .tag-odd {
            background: #FEE2E2;
            color: #B91C1C;
            border: 2px solid #FCA5A5;
        }

        /* 練習區 Quiz */
        .quiz-section {
            margin-top: 40px;
        }

        .quiz-card {
            background: var(--card-bg);
            border-radius: var(--radius-lg);
            padding: 28px;
            margin-bottom: 24px;
            box-shadow: var(--shadow);
            border: 1px solid #E2E8F0;
        }

        .quiz-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 14px;
        }

        .quiz-badge {
            background: #EEF2FF;
            color: #4F46E5;
            padding: 4px 12px;
            border-radius: 999px;
            font-size: 0.85rem;
            font-weight: 700;
        }

        .quiz-question {
            font-size: 1.15rem;
            font-weight: 700;
            color: var(--text-dark);
            margin-bottom: 18px;
            line-height: 1.5;
        }

        .quiz-options {
            display: grid;
            grid-template-columns: 1fr;
            gap: 12px;
        }

        @media (min-width: 640px) {
            .quiz-options {
                grid-template-columns: 1fr 1fr;
            }
        }

        .opt-btn {
            background: #F8FAFC;
            border: 2px solid #E2E8F0;
            border-radius: var(--radius-md);
            padding: 14px 18px;
            font-size: 1rem;
            font-weight: 600;
            text-align: left;
            cursor: pointer;
            transition: all 0.2s;
            color: var(--text-dark);
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .opt-btn:hover:not(:disabled) {
            border-color: var(--primary-light);
            background: var(--primary-bg);
            transform: translateY(-2px);
        }

        .opt-btn.correct {
            background: #DCFCE7 !important;
            border-color: #22C55E !important;
            color: #15803D !important;
        }

        .opt-btn.wrong {
            background: #FEE2E2 !important;
            border-color: #EF4444 !important;
            color: #B91C1C !important;
        }

        .feedback-box {
            display: none;
            margin-top: 16px;
            padding: 14px 18px;
            border-radius: var(--radius-sm);
            font-size: 0.95rem;
            line-height: 1.5;
        }

        .feedback-correct {
            background: #F0FDF4;
            border-left: 4px solid #22C55E;
            color: #166534;
        }

        .feedback-wrong {
            background: #FEF2F2;
            border-left: 4px solid #EF4444;
            color: #991B1B;
        }

        /* 總分結算 */
        .quiz-summary-card {
            background: linear-gradient(135deg, #1E3A8A 0%, #1E40AF 100%);
            color: white;
            border-radius: var(--radius-lg);
            padding: 32px;
            text-align: center;
            margin-top: 32px;
            box-shadow: var(--shadow);
        }

        .summary-score {
            font-family: 'Fredoka', sans-serif;
            font-size: 3.5rem;
            font-weight: 700;
            margin: 12px 0;
            color: #FBBF24;
        }

        .btn-reset {
            background: #FFFFFF;
            color: var(--primary);
            border: none;
            padding: 12px 28px;
            border-radius: 999px;
            font-weight: 700;
            font-size: 1rem;
            cursor: pointer;
            box-shadow: 0 4px 12px rgba(0,0,0,0.15);
            transition: all 0.2s;
            margin-top: 14px;
        }

        .btn-reset:hover {
            transform: scale(1.05);
        }
    </style>
</head>
<body>

    <header class="header-nav">
        <a href="portal.html" class="back-btn">
            <span>🏰</span> 回學習城堡首頁
        </a>
        <div style="font-weight: 800; color: var(--primary); font-size: 1rem;">
            國小 3 上數學・第 6 單元
        </div>
    </header>

    <div class="container">
        <!-- Hero 區塊 -->
        <section class="hero">
            <span class="hero-badge">國小 3 上數學・第 ⑥ 單元</span>
            <h1>➗ 除法大冒險：分裝、平分與餘數</h1>
            <p>
                歡迎來到除法魔法王國！掌握「分裝（包含除）」與「平分（等分除）」的神奇力量，學會除法直式計算的四步心法，牢記「餘數小於除數」的黃金法則，解開奇數與偶數的神秘代碼！
            </p>
        </section>

        <!-- 5 大核心觀念卡片 -->
        <div class="grid-2">
            <!-- 觀念 1 -->
            <div class="card">
                <div class="card-title">
                    <div class="card-icon">📦</div>
                    <span>6-1 分裝與平分（除法的意義）</span>
                </div>
                <p>除法是日常生活中分配物品的最重要工具，主要分為兩種情境：</p>
                <div class="highlight-box">
                    <strong>1. 分裝（包含除）：</strong>已知每份有多少，求分成幾份。<br>
                    例：18 公尺繩子，每 6 公尺剪 1 段，可剪幾段？<br>
                    記作：<code>18 ÷ 6 = 3</code>（段）
                </div>
                <div class="highlight-box">
                    <strong>2. 平分（等分除）：</strong>已知分成幾份，求每份有多少。<br>
                    例：18 公尺繩子，平分成 6 段，每段長幾公尺？<br>
                    記作：<code>18 ÷ 6 = 3</code>（公尺）
                </div>
                <p style="font-size: 0.9rem; color: var(--text-gray);">
                    ★ 記法：<strong>被除數 ÷ 除數 ＝ 商</strong>
                </p>
            </div>

            <!-- 觀念 2 -->
            <div class="card">
                <div class="card-title">
                    <div class="card-icon">⚡</div>
                    <span>6-2 認識餘數與黃金鐵律</span>
                </div>
                <p>當物品不能全部分完，剩下的就叫作<strong>「餘數」</strong>：</p>
                <div class="highlight-box">
                    例：16 個橘子，每 5 個裝 1 袋，可裝 3 袋，剩下 1 個。<br>
                    橫式記作：<code>16 ÷ 5 ＝ 3 … 1</code><br>
                    讀作：十六除以五等於三餘一。
                </div>
                <div class="alert-box">
                    ⚠️ <strong>餘數黃金鐵律：餘數一定要小於除數！</strong><br>
                    （餘數 ＜ 除數）。若餘數大於或等於除數，代表還能再分，商算太小了！<br>
                    例：除數是 6 時，可能的餘數只有 0、1、2、3、4、5。
                </div>
            </div>

            <!-- 觀念 3 -->
            <div class="card">
                <div class="card-title">
                    <div class="card-icon">📐</div>
                    <span>6-3 除法直式的四步心法</span>
                </div>
                <p>除法直式是高年級長除法的基礎，請牢記四大口訣：</p>
                <div class="highlight-box">
                    <strong>① 商：</strong>用九九乘法找出最接近且不超過被除數的商。<br>
                    <strong>② 乘：</strong>把商和除數相乘（<code>商 × 除數</code>）。<br>
                    <strong>③ 減：</strong>被除數減去乘積得到餘數。<br>
                    <strong>④ 比：</strong>檢查餘數是否「小於除數」。
                </div>
                <p style="font-size: 0.9rem; color: var(--text-gray);">
                    驗算公式：<code>除數 × 商 ＋ 餘數 ＝ 被除數</code>
                </p>
            </div>

            <!-- 觀念 4 -->
            <div class="card">
                <div class="card-title">
                    <div class="card-icon">🪄</div>
                    <span>6-4 0 和 1 的除法性質</span>
                </div>
                <p>除法中有幾個極為特殊的運算定律：</p>
                <div class="highlight-box">
                    <strong>1. 0 除以任何不是 0 的數都等於 0：</strong><br>
                    <code>0 ÷ 5 ＝ 0</code>（0 顆糖平分給 5 人，每人分 0 顆）。<br><br>
                    <strong>2. 任何數除以 1 都等於原本的數：</strong><br>
                    <code>9 ÷ 1 ＝ 9</code>（分給 1 個人，全歸他一人）。<br><br>
                    <strong>3. 兩相同大於 0 的數相除等於 1：</strong><br>
                    <code>8 ÷ 8 ＝ 1</code>
                </div>
                <div class="alert-box">
                    ⛔ <strong>特別禁忌：除數絕對不能是 0！</strong>（無意義）
                </div>
            </div>
        </div>

        <!-- 觀念 5 寬幅展示：奇數與偶數 -->
        <div class="card" style="margin-bottom: 32px;">
            <div class="card-title">
                <div class="card-icon">🔢</div>
                <span>6-5 認識奇數（單數）與偶數（雙數）</span>
            </div>
            <p>透過「2 個 2 個一數」或「除以 2 的餘數」來分類整數：</p>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px; margin-top: 14px;">
                <div style="background: #F0FDF4; border: 2px solid #86EFAC; border-radius: var(--radius-md); padding: 18px;">
                    <h3 style="color: #15803D; margin-bottom: 8px;">🟢 偶數（雙數）</h3>
                    <p>除以 2 <strong>餘數是 0</strong>（可以整除成雙）。</p>
                    <p style="margin-top: 8px; font-weight: 700; color: #166534;">
                        個位數字必定是：<span style="font-size: 1.2rem; background: #DCFCE7; padding: 2px 8px; border-radius: 6px;">0、2、4、6、8</span>
                    </p>
                    <p style="font-size: 0.85rem; color: #64748B; margin-top: 6px;">例如：12, 34, 752, 860, 500</p>
                </div>
                <div style="background: #FEF2F2; border: 2px solid #FCA5A5; border-radius: var(--radius-md); padding: 18px;">
                    <h3 style="color: #B91C1C; margin-bottom: 8px;">🔴 奇數（單數）</h3>
                    <p>除以 2 <strong>餘數是 1</strong>（分完後一定剩下 1 個）。</p>
                    <p style="margin-top: 8px; font-weight: 700; color: #991B1B;">
                        個位數字必定是：<span style="font-size: 1.2rem; background: #FEE2E2; padding: 2px 8px; border-radius: 6px;">1、3、5、7、9</span>
                    </p>
                    <p style="font-size: 0.85rem; color: #64748B; margin-top: 6px;">例如：11, 37, 145, 569, 99</p>
                </div>
            </div>

            <!-- 即時奇偶檢測小工具 -->
            <div class="parity-box" style="margin-top: 24px; padding-top: 18px; border-top: 1px dashed #CBD5E1;">
                <span style="font-weight: 700;">🔍 奇偶數即時檢測儀：</span>
                <input type="number" id="testNumber" value="569" class="tool-input" style="width: 120px;" placeholder="輸入整數">
                <button class="btn-calc" onclick="checkParity()">立即判斷</button>
                <div id="parityResult" class="parity-tag tag-odd">569 的個位數是 9 → 奇數 (單數)</div>
            </div>
        </div>

        <!-- 互動工具：除法直式動態演算機 -->
        <section class="interactive-tool">
            <div class="tool-title">
                <span>🧮</span>
                <span>除法直式動態演算模擬器</span>
            </div>
            <p style="color: var(--text-gray); margin-bottom: 18px;">
                輸入被除數與除數，觀察標準除法直式的結構、計算步驟與驗算過程：
            </p>

            <div class="tool-inputs">
                <div class="input-group">
                    <label>被除數：</label>
                    <input type="number" id="calcDividend" value="69" min="1" max="99" class="tool-input">
                </div>
                <span style="font-size: 1.5rem; font-weight: 800; color: var(--primary);">÷</span>
                <div class="input-group">
                    <label>除數：</label>
                    <input type="number" id="calcDivisor" value="8" min="1" max="9" class="tool-input">
                </div>
                <button class="btn-calc" onclick="runDivisionSim()">計算直式</button>
            </div>

            <div class="division-visual-board">
                <!-- 直式展示 -->
                <div id="verticalMathContainer" class="vertical-math">
                    <div class="vm-quotient" id="vmQuotient">8</div>
                    <div class="vm-house">
                        <span class="vm-divisor" id="vmDivisor">8</span>
                        <span class="vm-bracket" id="vmDividend">69</span>
                    </div>
                    <div class="vm-product" id="vmProduct">64</div>
                    <div class="vm-remainder" id="vmRemainder">5</div>
                </div>

                <!-- 解說與驗算 -->
                <div class="result-explanation">
                    <h4 id="calcSummaryTitle">69 ÷ 8 ＝ 8 … 5</h4>
                    <p id="calcStep1">1. 找出最接近且小於 69 的乘法：8 × <strong>8</strong> ＝ 64</p>
                    <p id="calcStep2">2. 計算相減：69 － 64 ＝ <strong>5</strong>（餘數）</p>
                    <p id="calcStep3" style="color: #15803D; font-weight: 700; margin-top: 6px;">
                        3. 檢查餘數：5 ＜ 8（餘數小於除數，正確！）
                    </p>
                    <div style="background: #F1F5F9; padding: 10px 14px; border-radius: 8px; margin-top: 10px; font-size: 0.95rem;">
                        <strong>驗算公式：</strong> 8 × 8 ＋ 5 ＝ 64 ＋ 5 ＝ 69 ✓
                    </div>
                </div>
            </div>
        </section>

        <!-- 練習 6 實戰評量題庫 -->
        <section class="quiz-section">
            <div style="display: flex; justify-content: space-between; align-items: flex-end; margin-bottom: 24px;">
                <div>
                    <h2 style="font-size: 1.8rem; font-weight: 900; color: var(--primary);">🎯 練習 6：除法實戰闖關挑戰</h2>
                    <p style="color: var(--text-gray);">完整取材自課本 P70~P101、112 年學力檢測題與資優精華題庫！</p>
                </div>
                <span style="font-weight: 700; color: var(--primary); background: var(--primary-bg); padding: 6px 14px; border-radius: 999px;">
                    共 10 題
                </span>
            </div>

            <div id="quizContainer">
                <!-- 題目將由 JavaScript 渲染並隨機打亂選項 -->
            </div>

            <!-- 總分結算卡 -->
            <div id="quizSummary" class="quiz-summary-card" style="display: none;">
                <h2>🎉 挑戰完成！除法冒險成效</h2>
                <div class="summary-score" id="finalScore">0 分</div>
                <p id="summaryMessage" style="font-size: 1.1rem; opacity: 0.95;"></p>
                <button class="btn-reset" onclick="resetQuiz()">🔄 再挑戰一次</button>
            </div>
        </section>
    </div>

    <script>
        // --- Web Audio API 音效 ---
        const audioCtx = new (window.AudioContext || window.webkitAudioContext)();
        function playSound(type) {
            if (audioCtx.state === 'suspended') {
                audioCtx.resume();
            }
            const osc = audioCtx.createOscillator();
            const gain = audioCtx.createGain();
            osc.connect(gain);
            gain.connect(audioCtx.destination);

            if (type === 'correct') {
                osc.type = 'triangle';
                osc.frequency.setValueAtTime(523.25, audioCtx.currentTime); // C5
                osc.frequency.exponentialRampToValueAtTime(783.99, audioCtx.currentTime + 0.15); // G5
                gain.gain.setValueAtTime(0.2, audioCtx.currentTime);
                gain.gain.exponentialRampToValueAtTime(0.01, audioCtx.currentTime + 0.3);
                osc.start();
                osc.stop(audioCtx.currentTime + 0.3);
            } else if (type === 'wrong') {
                osc.type = 'sawtooth';
                osc.frequency.setValueAtTime(220, audioCtx.currentTime); // A3
                osc.frequency.exponentialRampToValueAtTime(146.83, audioCtx.currentTime + 0.2); // D3
                gain.gain.setValueAtTime(0.25, audioCtx.currentTime);
                gain.gain.exponentialRampToValueAtTime(0.01, audioCtx.currentTime + 0.35);
                osc.start();
                osc.stop(audioCtx.currentTime + 0.35);
            } else if (type === 'complete') {
                const notes = [523.25, 659.25, 783.99, 1046.50];
                notes.forEach((freq, idx) => {
                    const noteOsc = audioCtx.createOscillator();
                    const noteGain = audioCtx.createGain();
                    noteOsc.connect(noteGain);
                    noteGain.connect(audioCtx.destination);
                    noteOsc.frequency.setValueAtTime(freq, audioCtx.currentTime + idx * 0.1);
                    noteGain.gain.setValueAtTime(0.18, audioCtx.currentTime + idx * 0.1);
                    noteGain.gain.exponentialRampToValueAtTime(0.01, audioCtx.currentTime + idx * 0.1 + 0.25);
                    noteOsc.start(audioCtx.currentTime + idx * 0.1);
                    noteOsc.stop(audioCtx.currentTime + idx * 0.1 + 0.25);
                });
            }
        }

        // --- 奇偶檢測機 ---
        function checkParity() {
            const numInput = document.getElementById('testNumber');
            const val = parseInt(numInput.value, 10);
            const resEl = document.getElementById('parityResult');

            if (isNaN(val)) {
                resEl.className = 'parity-tag';
                resEl.textContent = '請輸入有效整數';
                return;
            }

            const absVal = Math.abs(val);
            const lastDigit = absVal % 10;
            const isEven = (lastDigit % 2 === 0);

            if (isEven) {
                resEl.className = 'parity-tag tag-even';
                resEl.textContent = `${val} 的個位數是 ${lastDigit} → 偶數 (雙數)`;
            } else {
                resEl.className = 'parity-tag tag-odd';
                resEl.textContent = `${val} 的個位數是 ${lastDigit} → 奇數 (單數)`;
            }
            playSound('correct');
        }

        // --- 除法直式動態模擬器 ---
        function runDivisionSim() {
            const dividend = parseInt(document.getElementById('calcDividend').value, 10);
            const divisor = parseInt(document.getElementById('calcDivisor').value, 10);

            if (isNaN(dividend) || isNaN(divisor) || divisor <= 0) {
                alert("請輸入大於 0 的有效整數！");
                return;
            }

            const quotient = Math.floor(dividend / divisor);
            const remainder = dividend % divisor;
            const product = quotient * divisor;

            document.getElementById('vmQuotient').textContent = quotient;
            document.getElementById('vmDivisor').textContent = divisor;
            document.getElementById('vmDividend').textContent = dividend;
            document.getElementById('vmProduct').textContent = product;
            document.getElementById('vmRemainder').textContent = remainder;

            document.getElementById('calcSummaryTitle').textContent = `${dividend} ÷ ${divisor} ＝ ${quotient} … ${remainder}`;
            document.getElementById('calcStep1').innerHTML = `1. 找出最接近且小於或等於 ${dividend} 的乘法：${divisor} × <strong>${quotient}</strong> ＝ ${product}`;
            document.getElementById('calcStep2').innerHTML = `2. 計算相減：${dividend} － ${product} ＝ <strong>${remainder}</strong>（餘數）`;
            
            const checkEl = document.getElementById('calcStep3');
            if (remainder < divisor) {
                checkEl.style.color = '#15803D';
                checkEl.innerHTML = `3. 檢查餘數：${remainder} ＜ ${divisor}（餘數小於除數，完全正確！）`;
            } else {
                checkEl.style.color = '#B91C1C';
                checkEl.innerHTML = `3. 警告：餘數 ${remainder} 沒有小於除數 ${divisor}，商還能再增加！`;
            }
            playSound('correct');
        }

        // --- 練習 6 實戰測驗題庫 ---
        const QUIZ_RAW_DATA = [
            {
                id: 1,
                tag: "平分・等分除",
                q: "媽媽煮了 49 個水餃，平分成 7 盤，每盤有幾個水餃？",
                opts: ["7 個", "6 個", "8 個", "9 個"],
                ans: 0,
                exp: "平分成 7 盤屬於等分除，用除法算式記作：49 ÷ 7 ＝ 7（個）。"
            },
            {
                id: 2,
                tag: "112學力檢測題",
                q: "林阿姨將 46 塊餅乾分裝成袋，並用除法算式「46÷7＝6…4」記錄分裝的結果。下列哪個可能是林阿姨分裝餅乾的結果？",
                opts: [
                    "每袋裝 7 塊餅乾，總共裝滿了 6 袋，還剩下 4 塊沒有裝完",
                    "分裝成 6 袋，每袋裝 4 塊餅乾，總共裝滿了 7 袋",
                    "分裝成 7 袋，每袋裝 6 塊餅乾，可以全部裝完",
                    "每袋裝 7 塊餅乾，總共裝滿了 4 袋，還剩下 6 塊沒有裝完"
                ],
                ans: 0,
                exp: "除數是 7 代表每袋裝 7 塊，商是 6 代表裝滿 6 袋，餘數 4 代表剩下 4 塊沒有裝完。"
            },
            {
                id: 3,
                tag: "餘數黃金法則",
                q: "在一個除法算式中，除數是 8，那麼餘數最大可能是多少？",
                opts: ["7", "8", "9", "0"],
                ans: 0,
                exp: "餘數一定要小於除數（餘數 ＜ 除數）。除數是 8，餘數可能為 0～7，因此最大餘數是 7。"
            },
            {
                id: 4,
                tag: "生活長度分裝",
                q: "一條 20 公分長的彩帶，每 6 公分剪成 1 段，最多可以剪幾段？還剩下幾公分？",
                opts: [
                    "最多剪 3 段，剩下 2 公分",
                    "最多剪 2 段，剩下 8 公分",
                    "最多剪 3 段，剩下 0 公分",
                    "最多剪 4 段，剩下 2 公分"
                ],
                ans: 0,
                exp: "算式記作：20 ÷ 6 ＝ 3 … 2。因此最多剪 3 段，剩下 2 公分（餘數 2 ＜ 6）。"
            },
            {
                id: 5,
                tag: "生活曆法應用",
                q: "3 月份一共有 31 天，請問 3 月份相當於幾星期又幾天？（提示：1星期有 7 天）",
                opts: [
                    "4 星期又 3 天",
                    "3 星期又 4 天",
                    "4 星期又 2 天",
                    "5 星期又 1 天"
                ],
                ans: 0,
                exp: "算式記作：31 ÷ 7 ＝ 4 … 3。所以是 4 星期又 3 天。"
            },
            {
                id: 6,
                tag: "果凍平分情境",
                q: "把 26 個果凍平分給 3 個人，每個人分到幾個？還剩下幾個？",
                opts: [
                    "每人分到 8 個，剩下 2 個",
                    "每人分到 7 個，剩下 5 個",
                    "每人分到 8 個，剩下 0 個",
                    "每人分到 9 個，不夠 1 個"
                ],
                ans: 0,
                exp: "算式記作：26 ÷ 3 ＝ 8 … 2。若分 7 個剩 5 個則餘數比除數大，錯誤；因此每人分 8 個剩下 2 個。"
            },
            {
                id: 7,
                tag: "0 的除法性質",
                q: "盤子裡有 0 顆橘子，平分給 4 位同學，每位同學可以分到幾顆橘子？",
                opts: ["0 顆", "4 顆", "1 顆", "不能計算"],
                ans: 0,
                exp: "0 除以任何大於 0 的數都等於 0。記作：0 ÷ 4 ＝ 0（顆）。"
            },
            {
                id: 8,
                tag: "1 的除法性質",
                q: "任何大於 0 的整數除以 1，其答案是多少？",
                opts: ["原來的數", "0", "1", "無限多個答案"],
                ans: 0,
                exp: "除數為 1 時，相當於全部只分給 1 份，結果仍等於原本的被除數（原來的數）。"
            },
            {
                id: 9,
                tag: "奇偶數辨識",
                q: "下列數字中，哪一個是「奇數（單數）」？",
                opts: ["569", "752", "860", "34"],
                ans: 0,
                exp: "看個位數字判定：569 的個位數字是 9，屬於奇數；752、860、34 的個位數字分別是 2、0、4，皆為偶數。"
            },
            {
                id: 10,
                tag: "資優思維挑戰",
                q: "有兩個相同且大於 0 的整數相除（例如 25 ÷ 25），其結果會等於多少？",
                opts: ["1", "0", "兩數相加", "兩數相乘"],
                ans: 0,
                exp: "任何不為 0 的數除以它自己，結果必定等於 1（如 25 ÷ 25 ＝ 1）。"
            }
        ];

        // Fisher-Yates 隨機打亂演算法
        function shuffleArray(array) {
            for (let i = array.length - 1; i > 0; i--) {
                const j = Math.floor(Math.random() * (i + 1));
                [array[i], array[j]] = [array[j], array[i]];
            }
            return array;
        }

        let processedQuiz = [];
        let userAnswers = {};
        let score = 0;

        function initQuiz() {
            processedQuiz = QUIZ_RAW_DATA.map((item, idx) => {
                const originalCorrectText = item.opts[item.ans];
                const optionObjects = item.opts.map((optText, optIdx) => ({
                    text: optText,
                    isCorrect: optIdx === item.ans
                }));
                const shuffledOpts = shuffleArray([...optionObjects]);
                const newCorrectIndex = shuffledOpts.findIndex(o => o.isCorrect);

                return {
                    id: item.id,
                    displayNum: idx + 1,
                    tag: item.tag,
                    q: item.q,
                    options: shuffledOpts.map(o => o.text),
                    correctIndex: newCorrectIndex,
                    exp: item.exp
                };
            });

            renderQuiz();
        }

        function renderQuiz() {
            const container = document.getElementById('quizContainer');
            container.innerHTML = '';
            userAnswers = {};

            processedQuiz.forEach((qItem) => {
                const card = document.createElement('div');
                card.className = 'quiz-card';
                card.id = `quizCard_${qItem.id}`;

                const optHtml = qItem.options.map((opt, oIdx) => `
                    <button class="opt-btn" onclick="selectOption(${qItem.id}, ${oIdx})">
                        <span>(${String.fromCharCode(65 + oIdx)})</span>
                        <span>${opt}</span>
                    </button>
                `).join('');

                card.innerHTML = `
                    <div class="quiz-header">
                        <span class="quiz-badge">${qItem.tag}</span>
                        <span style="font-weight: 700; color: var(--text-gray);">第 ${qItem.displayNum} / 10 題</span>
                    </div>
                    <div class="quiz-question">${qItem.displayNum}. ${qItem.q}</div>
                    <div class="quiz-options" id="optGroup_${qItem.id}">
                        ${optHtml}
                    </div>
                    <div class="feedback-box" id="feedback_${qItem.id}"></div>
                `;
                container.appendChild(card);
            });
        }

        function selectOption(qId, selectedIdx) {
            if (userAnswers[qId] !== undefined) return;
            userAnswers[qId] = selectedIdx;

            const qItem = processedQuiz.find(q => q.id === qId);
            const optGroup = document.getElementById(`optGroup_${qId}`);
            const buttons = optGroup.getElementsByClassName('opt-btn');
            const feedbackEl = document.getElementById(`feedback_${qId}`);

            Array.from(buttons).forEach(btn => btn.disabled = true);

            const isCorrect = (selectedIdx === qItem.correctIndex);
            if (isCorrect) {
                buttons[selectedIdx].classList.add('correct');
                feedbackEl.className = 'feedback-box feedback-correct';
                feedbackEl.style.display = 'block';
                feedbackEl.innerHTML = `<strong>🎉 太棒了！回答正確！</strong><br>${qItem.exp}`;
                playSound('correct');
            } else {
                buttons[selectedIdx].classList.add('wrong');
                buttons[qItem.correctIndex].classList.add('correct');
                feedbackEl.className = 'feedback-box feedback-wrong';
                feedbackEl.style.display = 'block';
                feedbackEl.innerHTML = `<strong>💡 差一點點！正確答案是 (${String.fromCharCode(65 + qItem.correctIndex)}) ${qItem.options[qItem.correctIndex]}</strong><br>${qItem.exp}`;
                playSound('wrong');
            }

            checkAllAnswered();
        }

        function checkAllAnswered() {
            if (Object.keys(userAnswers).length === processedQuiz.length) {
                let correctCount = 0;
                processedQuiz.forEach(q => {
                    if (userAnswers[q.id] === q.correctIndex) {
                        correctCount++;
                    }
                });
                score = correctCount * 10;

                const summaryCard = document.getElementById('quizSummary');
                const scoreEl = document.getElementById('finalScore');
                const msgEl = document.getElementById('summaryMessage');

                scoreEl.textContent = `${score} 分`;
                if (score === 100) {
                    msgEl.textContent = "🏆 太厲害了！你已經完全精通除法、餘數與奇偶數，獲得除法大師勳章！";
                } else if (score >= 80) {
                    msgEl.textContent = "🌟 表現優異！對除法與直式掌握良好，稍微複習細節就能更上一層樓！";
                } else {
                    msgEl.textContent = "💪 繼續加油！多練習餘數小於除數的法則與直式步驟，一定能更進步！";
                }

                summaryCard.style.display = 'block';
                summaryCard.scrollIntoView({ behavior: 'smooth' });
                playSound('complete');
            }
        }

        function resetQuiz() {
            document.getElementById('quizSummary').style.display = 'none';
            initQuiz();
            window.scrollTo({ top: document.querySelector('.quiz-section').offsetTop - 80, behavior: 'smooth' });
        }

        window.addEventListener('DOMContentLoaded', () => {
            initQuiz();
        });
    </script>
</body>
</html>
'''

with open("math3_division.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Successfully generated math3_division.html (size: {len(html_content):,} chars)")

