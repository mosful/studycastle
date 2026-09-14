import json

# 讀取 12 課完整資料庫
with open('chinese3_full_curriculum_database.json', 'r', encoding='utf-8') as f:
    curriculum_data = json.load(f)

curriculum_json_str = json.dumps(curriculum_data, ensure_ascii=False, indent=2)

html_content = f'''<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>115上 國小國語三上 互動學習城堡 (康軒版第1~12課 全冊練習簿與測驗卷題庫) | 學習城堡</title>
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Fredoka:wght@600;700&family=Noto+Serif+TC:wght@600;900&family=Noto+Sans+TC:wght@400;500;700;900&display=swap" rel="stylesheet">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/canvas-confetti/1.9.2/confetti.browser.min.js"></script>
    <style>
        :root {{
            --primary: #EA580C;
            --primary-dark: #C2410C;
            --primary-light: #FFEDD5;
            --secondary: #0284C7;
            --secondary-dark: #0369A1;
            --secondary-light: #E0F2FE;
            --accent-amber: #D97706;
            --accent-green: #16A34A;
            --accent-purple: #7C3AED;
            --bg-color: #FFF7ED;
            --card-bg: #FFFFFF;
            --text-main: #1F2937;
            --text-muted: #6B7280;
            --border-color: #FED7AA;
            --shadow-card: 0 10px 25px -5px rgba(234, 88, 12, 0.12);
        }}

        * {{ box-sizing: border-box; margin: 0; padding: 0; font-family: 'Noto Sans TC', sans-serif; }}

        body {{
            background-color: var(--bg-color);
            background-image: 
                radial-gradient(circle at 10% 20%, rgba(234, 88, 12, 0.08) 0%, transparent 40%),
                radial-gradient(circle at 90% 80%, rgba(2, 132, 199, 0.08) 0%, transparent 40%);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            padding: 16px 12px 60px;
            color: var(--text-main);
            user-select: none;
        }}

        .app-container {{
            width: 100%;
            max-width: 900px;
            display: flex;
            flex-direction: column;
        }}

        /* 頂部導航列 */
        .top-bar {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 14px;
            gap: 8px;
            position: relative;
        }}
        .nav-btn {{
            display: inline-flex;
            align-items: center;
            gap: 6px;
            padding: 8px 16px;
            background: #FFF;
            border: 2px solid var(--primary);
            border-radius: 20px;
            color: var(--primary-dark);
            font-weight: 700;
            font-size: 0.95rem;
            text-decoration: none;
            cursor: pointer;
            box-shadow: 0 3px 0 #C2410C;
            transition: all 0.15s ease;
        }}
        .nav-btn:hover {{ background: var(--primary-light); transform: translateY(-2px); box-shadow: 0 5px 0 #C2410C; }}
        .nav-btn:active {{ transform: translateY(2px); box-shadow: 0 1px 0 #C2410C; }}
        
        .unit-badge {{
            font-size: 0.88rem;
            font-weight: 800;
            padding: 8px 16px;
            border-radius: 20px;
            background: linear-gradient(135deg, var(--primary), var(--secondary));
            color: #FFF;
            box-shadow: 0 3px 10px rgba(234, 88, 12, 0.35);
            display: inline-flex;
            align-items: center;
            gap: 6px;
            border: none;
            cursor: pointer;
            transition: all 0.2s ease;
            user-select: none;
        }}
        .unit-badge.nav-badge-btn:hover {{
            transform: translateY(-2px);
            box-shadow: 0 6px 16px rgba(234, 88, 12, 0.45);
            filter: brightness(1.08);
        }}
        .unit-badge .dropdown-arrow {{
            font-size: 0.72rem;
            transition: transform 0.25s ease;
        }}
        .unit-badge.open .dropdown-arrow {{
            transform: rotate(180deg);
        }}

        /* 快速選課下拉選單彈窗 */
        .quick-lesson-menu {{
            position: absolute;
            top: 52px;
            right: 0;
            width: min(94vw, 480px);
            background: #FFFFFF;
            border: 2.5px solid var(--primary);
            border-radius: 20px;
            box-shadow: 0 15px 35px -5px rgba(234, 88, 12, 0.25), 0 0 0 1000px rgba(0,0,0,0.35);
            padding: 16px;
            z-index: 9999;
            display: none;
            animation: menuPop 0.25s cubic-bezier(0.34, 1.56, 0.64, 1);
        }}
        .quick-lesson-menu.show {{
            display: block;
        }}
        @keyframes menuPop {{
            from {{ opacity: 0; transform: translateY(-8px) scale(0.96); }}
            to {{ opacity: 1; transform: translateY(0) scale(1); }}
        }}
        .quick-menu-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 12px;
            padding-bottom: 8px;
            border-bottom: 2px dashed var(--border-color);
        }}
        .quick-menu-title {{
            font-size: 1rem;
            font-weight: 900;
            color: var(--primary-dark);
            display: flex;
            align-items: center;
            gap: 6px;
        }}
        .quick-menu-close {{
            background: #F3F4F6;
            border: none;
            width: 28px;
            height: 28px;
            border-radius: 50%;
            cursor: pointer;
            font-weight: 800;
            color: #6B7280;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: all 0.2s;
        }}
        .quick-menu-close:hover {{
            background: #E5E7EB;
            color: #111827;
        }}
        .quick-grid {{
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 8px;
            max-height: 55vh;
            overflow-y: auto;
            padding-right: 4px;
        }}
        .quick-item-btn {{
            background: #FFF7ED;
            border: 1.5px solid var(--border-color);
            border-radius: 12px;
            padding: 8px 10px;
            text-align: left;
            cursor: pointer;
            transition: all 0.15s ease;
            display: flex;
            flex-direction: column;
            gap: 2px;
        }}
        .quick-item-btn:hover {{
            background: #FFEDD5;
            border-color: var(--primary);
            transform: translateY(-2px);
        }}
        .quick-item-btn.active {{
            background: var(--primary);
            border-color: var(--primary-dark);
            color: #FFF;
        }}
        .quick-item-btn.active .quick-item-num,
        .quick-item-btn.active .quick-item-title,
        .quick-item-btn.active .quick-item-type {{
            color: #FFF !important;
        }}
        .quick-item-num {{
            font-size: 0.72rem;
            font-weight: 900;
            color: var(--primary);
        }}
        .quick-item-title {{
            font-size: 0.86rem;
            font-weight: 800;
            color: var(--text-main);
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
        }}
        .quick-item-type {{
            font-size: 0.7rem;
            color: var(--text-muted);
        }}

        /* 英雄區塊 */
        .hero-banner {{
            background: var(--card-bg);
            border-radius: 24px;
            padding: 24px 20px;
            text-align: center;
            border: 3px solid var(--primary);
            box-shadow: var(--shadow-card);
            margin-bottom: 18px;
            position: relative;
        }}
        .hero-icon {{ font-size: 3.2rem; margin-bottom: 6px; display: inline-block; animation: floatIcon 3s ease-in-out infinite; }}
        @keyframes floatIcon {{ 0%,100%{{transform:translateY(0);}} 50%{{transform:translateY(-6px);}} }}

        h1 {{
            font-family: 'Noto Serif TC', serif;
            font-size: clamp(1.5rem, 4vw, 2.1rem);
            color: var(--primary-dark);
            font-weight: 900;
            margin-bottom: 6px;
        }}
        .sub-title {{ color: var(--text-muted); font-size: 0.95rem; line-height: 1.5; }}
        .badge-tags {{
            display: flex;
            justify-content: center;
            gap: 8px;
            margin-top: 10px;
            flex-wrap: wrap;
        }}
        .tag-pill {{
            font-size: 0.75rem;
            font-weight: 700;
            padding: 4px 10px;
            border-radius: 12px;
            background: var(--primary-light);
            color: var(--primary-dark);
            border: 1px solid var(--border-color);
        }}

        /* 頁籤切換列 */
        .tab-bar {{
            display: flex;
            gap: 6px;
            margin-bottom: 16px;
            overflow-x: auto;
            padding-bottom: 4px;
            -webkit-overflow-scrolling: touch;
        }}
        .tab-btn {{
            flex: 1;
            min-width: 100px;
            padding: 10px 8px;
            background: #FFF;
            border: 2px solid var(--border-color);
            border-radius: 16px;
            font-size: 0.88rem;
            font-weight: 700;
            color: var(--text-muted);
            cursor: pointer;
            transition: all 0.2s;
            text-align: center;
            white-space: nowrap;
        }}
        .tab-btn:hover {{
            background: var(--primary-light);
            color: var(--primary-dark);
        }}
        .tab-btn.active {{
            background: var(--primary-dark);
            border-color: var(--primary-dark);
            color: #FFF;
            box-shadow: 0 4px 10px rgba(234, 88, 12, 0.25);
            transform: translateY(-2px);
        }}

        /* 內容卡片 */
        .content-card {{
            background: var(--card-bg);
            border: 2px solid var(--border-color);
            border-radius: 20px;
            padding: 22px 18px;
            box-shadow: var(--shadow-card);
            margin-bottom: 16px;
        }}

        /* 課次卡片網格 */
        .lesson-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
            gap: 12px;
            margin-top: 10px;
        }}
        .lesson-item-card {{
            background: #FFF;
            border: 2px solid var(--border-color);
            border-radius: 16px;
            padding: 14px;
            cursor: pointer;
            transition: all 0.2s;
            text-align: left;
            position: relative;
        }}
        .lesson-item-card:hover {{
            border-color: var(--primary);
            transform: translateY(-3px);
            box-shadow: 0 6px 15px rgba(234, 88, 12, 0.15);
        }}
        .lesson-item-card.active-lesson {{
            border-color: var(--primary-dark);
            background: #FFFDF9;
            box-shadow: 0 0 0 2px var(--primary-dark);
        }}
        .lesson-tag {{
            display: inline-block;
            font-size: 0.72rem;
            font-weight: 800;
            padding: 2px 8px;
            background: var(--primary-light);
            color: var(--primary-dark);
            border-radius: 8px;
            margin-bottom: 6px;
        }}
        .lesson-name {{
            font-size: 1.05rem;
            font-weight: 800;
            color: var(--text-main);
            margin-bottom: 4px;
            font-family: 'Noto Serif TC', serif;
        }}
        .lesson-type {{
            font-size: 0.8rem;
            color: var(--text-muted);
        }}

        /* 詳情區塊區段樣式 */
        .section-header {{
            display: flex;
            align-items: center;
            gap: 8px;
            font-size: 1.15rem;
            font-weight: 900;
            color: var(--primary-dark);
            margin: 20px 0 10px;
            padding-bottom: 6px;
            border-bottom: 2px dashed var(--border-color);
            font-family: 'Noto Serif TC', serif;
        }}
        .info-pill-box {{
            background: #FFF7ED;
            border: 1px solid var(--border-color);
            border-radius: 14px;
            padding: 14px 16px;
            margin-bottom: 12px;
            font-size: 0.95rem;
            line-height: 1.6;
        }}

        /* 詞彙卡片網格 */
        .vocab-list-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
            gap: 10px;
            margin-top: 10px;
        }}
        .vocab-mini-card {{
            background: #FFFFFF;
            border: 1.5px solid var(--border-color);
            border-radius: 14px;
            padding: 12px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.03);
            transition: transform 0.15s;
        }}
        .vocab-mini-card:hover {{
            transform: translateY(-2px);
            border-color: var(--primary);
        }}
        .v-word {{
            font-size: 1.15rem;
            font-weight: 900;
            color: var(--primary-dark);
            margin-bottom: 2px;
        }}
        .v-zhu {{
            font-size: 0.85rem;
            color: var(--accent-amber);
            font-weight: 700;
            margin-bottom: 6px;
        }}
        .v-mean {{
            font-size: 0.88rem;
            color: #4B5563;
            line-height: 1.45;
        }}

        /* 練習簿專區專屬卡片 */
        .wb-section-card {{
            background: #FFFFFF;
            border: 2px solid #FED7AA;
            border-radius: 16px;
            padding: 16px;
            margin-bottom: 16px;
            box-shadow: 0 4px 12px rgba(234,88,12,0.06);
        }}
        .wb-section-title {{
            display: flex;
            align-items: center;
            gap: 8px;
            font-size: 1.1rem;
            font-weight: 800;
            color: var(--primary-dark);
            margin-bottom: 12px;
            padding-bottom: 6px;
            border-bottom: 1.5px solid #FFEDD5;
        }}
        .wb-char-box {{
            background: #F0FDF4;
            border: 1.5px solid #BBF7D0;
            border-radius: 12px;
            padding: 12px;
            margin-bottom: 10px;
        }}
        .wb-btn-reveal {{
            padding: 4px 10px;
            background: #0284C7;
            color: #FFF;
            border: none;
            border-radius: 8px;
            font-size: 0.8rem;
            font-weight: 700;
            cursor: pointer;
            transition: all 0.2s;
        }}
        .wb-btn-reveal:hover {{
            background: #0369A1;
        }}

        /* 測驗專區 */
        .quiz-box {{
            padding: 10px 0;
        }}
        .quiz-meta-bar {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 16px;
            font-weight: 800;
            font-size: 0.95rem;
            color: var(--primary-dark);
        }}
        .quiz-q-box {{
            font-size: 1.15rem;
            font-weight: 800;
            color: #111827;
            margin-bottom: 16px;
            line-height: 1.5;
            background: #FFF7ED;
            padding: 16px;
            border-radius: 16px;
            border: 2px solid var(--border-color);
        }}
        .quiz-tag {{
            display: inline-block;
            font-size: 0.75rem;
            font-weight: 800;
            padding: 2px 8px;
            background: #0284C7;
            color: #FFF;
            border-radius: 6px;
            margin-right: 6px;
            vertical-align: middle;
        }}
        .options-list {{
            display: flex;
            flex-direction: column;
            gap: 10px;
            margin-bottom: 16px;
        }}
        .opt-btn {{
            width: 100%;
            padding: 14px 16px;
            text-align: left;
            background: #FFFFFF;
            border: 2px solid #E5E7EB;
            border-radius: 14px;
            font-size: 1rem;
            font-weight: 700;
            color: #374151;
            cursor: pointer;
            transition: all 0.15s ease;
        }}
        .opt-btn:hover {{
            background: #F3F4F6;
            border-color: var(--primary);
            transform: translateX(3px);
        }}
        .opt-btn.correct {{
            background: #DCFCE7 !important;
            border-color: #16A34A !important;
            color: #15803D !important;
        }}
        .opt-btn.wrong {{
            background: #FEE2E2 !important;
            border-color: #EF4444 !important;
            color: #B91C1C !important;
        }}
        .explanation-box {{
            display: none;
            background: #F8FAFC;
            border: 2px solid #CBD5E1;
            border-radius: 14px;
            padding: 14px;
            margin-top: 14px;
            font-size: 0.95rem;
            line-height: 1.5;
        }}
        .explanation-box.show {{
            display: block;
            animation: fadeIn 0.3s ease;
        }}
        @keyframes fadeIn {{
            from {{ opacity: 0; transform: translateY(-4px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}
        .btn-action {{
            display: inline-flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
            width: 100%;
            padding: 14px;
            background: linear-gradient(135deg, var(--primary), var(--primary-dark));
            color: #FFF;
            border: none;
            border-radius: 16px;
            font-size: 1.05rem;
            font-weight: 800;
            cursor: pointer;
            box-shadow: 0 4px 12px rgba(234, 88, 12, 0.3);
            transition: all 0.2s;
        }}
        .btn-action:hover {{
            transform: translateY(-2px);
            box-shadow: 0 6px 16px rgba(234, 88, 12, 0.4);
        }}

        .hidden {{ display: none !important; }}
    </style>
</head>
<body>

<div class="app-container">
    <!-- 頂部導航 -->
    <div class="top-bar">
        <a href="portal.html" class="nav-btn">🏰 回城堡首頁</a>
        <button id="btnQuickLessonPicker" class="unit-badge nav-badge-btn" onclick="toggleQuickLessonMenu(event)">
            <span>📚 115上 康軒三上 12課快選</span>
            <span class="dropdown-arrow">▼</span>
        </button>

        <!-- 快速選課下拉選單 -->
        <div id="quickLessonMenu" class="quick-lesson-menu">
            <div class="quick-menu-header">
                <div class="quick-menu-title">
                    <span>📖</span>
                    <span>全冊 12 課快速直達</span>
                </div>
                <button class="quick-menu-close" onclick="closeQuickLessonMenu(event)">✕</button>
            </div>
            <div id="quickLessonsContainer" class="quick-grid"></div>
        </div>
    </div>

    <!-- 英雄區塊 -->
    <div class="hero-banner">
        <div class="hero-icon">🏮</div>
        <h1>國語 3上 互動學習城堡</h1>
        <p class="sub-title">完整收錄 115 上 康軒版國小國語三上 12 課課文精華、練習簿生字拆合與新挑戰測驗題庫！</p>
        <div class="badge-tags">
            <span class="tag-pill">✨ 康軒 115 上最新課綱</span>
            <span class="tag-pill">📝 練習簿題型濃縮</span>
            <span class="tag-pill">📋 新挑戰測驗實戰</span>
            <span class="tag-pill">🏆 即時解析與彩花</span>
        </div>
    </div>

    <!-- 頁籤導覽列 -->
    <div class="tab-bar">
        <button class="tab-btn active" id="tab-overview" onclick="switchTab('overview')">📖 課文架構</button>
        <button class="tab-btn" id="tab-workbook" onclick="switchTab('workbook')">📝 課課練習簿</button>
        <button class="tab-btn" id="tab-vocab" onclick="switchTab('vocab')">📚 生字成語辭典</button>
        <button class="tab-btn" id="tab-rhetoric" onclick="switchTab('rhetoric')">💡 修辭賞析</button>
        <button class="tab-btn" id="tab-quiz" onclick="switchTab('quiz')">📋 測驗實戰挑戰</button>
    </div>

    <!-- 檢視 1：課文導讀與架構 (Overview) -->
    <div id="view-overview">
        <!-- 課次切換卡片 -->
        <div class="content-card">
            <div style="font-weight:800; font-size:1.1rem; color:var(--primary-dark); margin-bottom:8px;">
                🎯 點擊切換閱讀課次（共 12 課，涵蓋 4 大單元）
            </div>
            <div class="lesson-grid" id="lesson-cards-grid"></div>
        </div>

        <!-- 單課詳情卡片 -->
        <div class="content-card" id="lesson-detail-box"></div>
    </div>

    <!-- 檢視 2：課課練習簿精華 (Workbook) -->
    <div id="view-workbook" class="hidden">
        <div class="content-card">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px; flex-wrap:wrap; gap:8px;">
                <div style="font-weight:800; font-size:1.1rem; color:var(--primary-dark);">
                    📝 康軒練習簿 重點題型與互動樂園
                </div>
                <select id="wb-lesson-filter" style="padding:6px 12px; border-radius:10px; border:1.5px solid var(--primary); font-weight:700; background:#FFF;" onchange="renderWorkbookView()">
                </select>
            </div>
            <div id="wb-content-container"></div>
        </div>
    </div>

    <!-- 檢視 3：生字成語辭典 (Vocab) -->
    <div id="view-vocab" class="hidden">
        <div class="content-card">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:14px; flex-wrap:wrap; gap:8px;">
                <div style="font-weight:800; font-size:1.1rem; color:var(--primary-dark);">
                    📚 全冊重點成語與詞彙速查寶庫
                </div>
                <select id="vocab-lesson-filter" style="padding:6px 12px; border-radius:10px; border:1.5px solid var(--primary); font-weight:700; background:#FFF;" onchange="renderVocabList()">
                    <option value="all">全冊 12 課全部成語詞彙</option>
                </select>
            </div>
            <div class="vocab-list-grid" id="vocab-grid-container"></div>
        </div>
    </div>

    <!-- 檢視 4：修辭賞析 (Rhetoric) -->
    <div id="view-rhetoric" class="hidden">
        <div class="content-card">
            <div style="font-weight:800; font-size:1.1rem; color:var(--primary-dark); margin-bottom:12px;">
                💡 課文精彩修辭技巧賞析
            </div>
            <div id="rhetoric-container"></div>
        </div>
    </div>

    <!-- 檢視 5：新挑戰測驗實戰 (Quiz) -->
    <div id="view-quiz" class="hidden">
        <div class="content-card">
            <!-- 測驗歡迎與設定區塊 -->
            <div id="quiz-intro-box" style="text-align:center; padding:16px 8px;">
                <div style="font-size:3rem; margin-bottom:8px;">🎯</div>
                <h3 style="color:var(--primary-dark); font-size:1.4rem; font-family:'Noto Serif TC'; margin-bottom:8px;">
                    115上 國語 3上 挑戰測驗卷實戰
                </h3>
                <p style="color:var(--text-muted); font-size:0.95rem; margin-bottom:18px; max-width:540px; margin-left:auto; margin-right:auto;">
                    精選自康軒三上新挑戰測驗卷核心試題！題目涵蓋字音字形、詞語成語辨析、閱讀理解與修辭手法，並附有詳盡的解題說明。
                </p>
                <div style="display:flex; justify-content:center; gap:12px; margin-bottom:20px; flex-wrap:wrap;">
                    <button class="btn-action" style="width:auto; min-width:180px;" onclick="startQuiz('current')">
                        ⚡ 當前課次專項測驗 (5 題)
                    </button>
                    <button class="btn-action" style="width:auto; min-width:180px; background:linear-gradient(135deg, var(--secondary), var(--secondary-dark));" onclick="startQuiz('all')">
                        🎲 全冊跨課模擬考 (10 題)
                    </button>
                </div>
            </div>

            <!-- 測驗答題互動區塊 -->
            <div id="quiz-play-box" class="quiz-box hidden">
                <div class="quiz-meta-bar">
                    <span id="quiz-mode-title">當前挑戰</span>
                    <span>題號：<span id="quiz-curr" style="color:var(--accent-amber);">1</span> / <span id="quiz-total">10</span></span>
                    <span>得分：<span id="quiz-score" style="color:var(--accent-green);">0</span> 分</span>
                </div>

                <div class="quiz-q-box" id="quiz-question-text">
                    題目載入中...
                </div>

                <div class="options-list" id="quiz-options-box"></div>

                <div class="explanation-box" id="quiz-explanation-box"></div>

                <button id="btn-next-quiz" class="btn-action hidden" style="margin-top:14px;" onclick="nextQuizQuestion()">
                    下一題 ➔
                </button>
            </div>

            <!-- 測驗結果結算區塊 -->
            <div id="quiz-result-box" class="quiz-box hidden" style="text-align:center; padding:24px 8px;">
                <div style="font-size:3.5rem; margin-bottom:6px;" id="quiz-res-icon">🏆</div>
                <h3 id="quiz-res-title" style="color:var(--primary-dark); font-size:1.5rem; font-family:'Noto Serif TC'; margin-bottom:6px;">恭喜完成測驗！</h3>
                <p id="quiz-res-desc" style="color:var(--text-muted); font-size:0.95rem; margin-bottom:14px;"></p>
                <div style="background:#FFF7ED; border:2px solid var(--border-color); border-radius:18px; padding:18px; max-width:300px; margin:0 auto 20px;">
                    <div style="font-size:0.9rem; color:var(--text-muted);">總得分</div>
                    <div style="font-size:3.5rem; font-weight:900; color:var(--accent-amber); font-family:'Fredoka';" id="quiz-final-score">100</div>
                    <div id="quiz-score-detail" style="color:var(--text-muted); font-size:0.95rem; margin-top:4px;">答對 10 / 10 題</div>
                </div>
                <div style="display:flex; justify-content:center; gap:10px; flex-wrap:wrap;">
                    <button class="btn-action" style="width:auto; min-width:160px;" onclick="startQuiz('current')">🔄 重測本課試題</button>
                    <button class="btn-action" style="width:auto; min-width:160px; background:linear-gradient(135deg, var(--secondary), var(--secondary-dark));" onclick="startQuiz('all')">🎲 全冊隨機抽測</button>
                </div>
            </div>
        </div>
    </div>
</div>

<script>
// 音效合成引擎
const audioCtx = new (window.AudioContext || window.webkitAudioContext)();
function playSound(type) {{
    if (audioCtx.state === 'suspended') audioCtx.resume();
    const osc = audioCtx.createOscillator();
    const gainNode = audioCtx.createGain();
    osc.connect(gainNode);
    gainNode.connect(audioCtx.destination);
    const now = audioCtx.currentTime;
    if (type === 'correct') {{
        osc.type = 'triangle';
        osc.frequency.setValueAtTime(523.25, now);
        osc.frequency.setValueAtTime(659.25, now + 0.1);
        osc.frequency.setValueAtTime(783.99, now + 0.2);
        gainNode.gain.setValueAtTime(0.25, now);
        gainNode.gain.exponentialRampToValueAtTime(0.01, now + 0.4);
        osc.start(now); osc.stop(now + 0.4);
    }} else if (type === 'wrong') {{
        osc.type = 'sawtooth';
        osc.frequency.setValueAtTime(220, now);
        osc.frequency.setValueAtTime(180, now + 0.15);
        gainNode.gain.setValueAtTime(0.25, now);
        gainNode.gain.exponentialRampToValueAtTime(0.01, now + 0.35);
        osc.start(now); osc.stop(now + 0.35);
    }}
}}

// 115上 康軒版國小國語三上 12 課完整資料庫 (含練習簿與測驗卷)
const CURRICULUM = {curriculum_json_str};

let selectedLessonId = 'l1';

// 測驗變數
let quizQuestions = [];
let currentQuizIdx = 0;
let quizScore = 0;
let quizAnswered = false;

// 頁面初始化
document.addEventListener('DOMContentLoaded', () => {{
    renderLessonCards();
    renderLessonDetail(selectedLessonId);
    initSelectOptions();
    renderVocabList();
    renderRhetoricList();
    renderWorkbookView();
    renderQuickLessons();

    // 點擊外部自動關閉快速選課選單
    document.addEventListener('click', (e) => {{
        const menu = document.getElementById('quickLessonMenu');
        const btn = document.getElementById('btnQuickLessonPicker');
        if (menu && menu.classList.contains('show')) {{
            if (!menu.contains(e.target) && !btn.contains(e.target)) {{
                closeQuickLessonMenu();
            }}
        }}
    }});
}});

// 初始化各篩選下拉選單
function initSelectOptions() {{
    const wbSelect = document.getElementById('wb-lesson-filter');
    const vocabSelect = document.getElementById('vocab-lesson-filter');
    if (wbSelect) {{
        wbSelect.innerHTML = CURRICULUM.map(l => `<option value="${{l.id}}">${{l.title}}</option>`).join('');
    }}
    if (vocabSelect) {{
        vocabSelect.innerHTML = '<option value="all">全冊 12 課全部成語詞彙</option>' + 
            CURRICULUM.map(l => `<option value="${{l.id}}">${{l.title}}</option>`).join('');
    }}
}}

// 渲染右上角快速選課清單
function renderQuickLessons() {{
    const container = document.getElementById('quickLessonsContainer');
    if (!container) return;
    container.innerHTML = CURRICULUM.map(lesson => `
        <button class="quick-item-btn ${{lesson.id === selectedLessonId ? 'active' : ''}}" onclick="jumpToLessonFromQuickMenu('${{lesson.id}}', event)">
            <span class="quick-item-num">${{lesson.id.toUpperCase()}}</span>
            <span class="quick-item-title">${{lesson.title}}</span>
            <span class="quick-item-type">${{lesson.unit}}</span>
        </button>
    `).join('');
}}

function toggleQuickLessonMenu(e) {{
    if (e) {{ e.preventDefault(); e.stopPropagation(); }}
    const menu = document.getElementById('quickLessonMenu');
    const btn = document.getElementById('btnQuickLessonPicker');
    if (!menu) return;
    const isShowing = menu.classList.contains('show');
    if (isShowing) {{
        closeQuickLessonMenu();
    }} else {{
        renderQuickLessons();
        menu.classList.add('show');
        if (btn) btn.classList.add('open');
    }}
}}

function closeQuickLessonMenu(e) {{
    if (e) {{ e.preventDefault(); e.stopPropagation(); }}
    const menu = document.getElementById('quickLessonMenu');
    const btn = document.getElementById('btnQuickLessonPicker');
    if (menu) menu.classList.remove('show');
    if (btn) btn.classList.remove('open');
}}

function jumpToLessonFromQuickMenu(id, e) {{
    if (e) {{ e.preventDefault(); e.stopPropagation(); }}
    selectLesson(id);
    switchTab('overview');
    closeQuickLessonMenu();
    playSound('correct');

    const detailBox = document.getElementById('lesson-detail-box');
    if (detailBox) {{
        detailBox.scrollIntoView({{ behavior: 'smooth', block: 'start' }});
    }}
}}

function switchTab(tabKey) {{
    document.querySelectorAll('.tab-btn').forEach(btn => btn.classList.remove('active'));
    const targetBtn = document.getElementById(`tab-${{tabKey}}`);
    if (targetBtn) targetBtn.classList.add('active');

    ['overview', 'workbook', 'vocab', 'rhetoric', 'quiz'].forEach(k => {{
        const v = document.getElementById(`view-${{k}}`);
        if (v) v.classList.toggle('hidden', k !== tabKey);
    }});
}}

function renderLessonCards() {{
    const container = document.getElementById('lesson-cards-grid');
    if (!container) return;
    container.innerHTML = CURRICULUM.map(lesson => `
        <div class="lesson-item-card ${{lesson.id === selectedLessonId ? 'active-lesson' : ''}}" onclick="selectLesson('${{lesson.id}}')">
            <span class="lesson-tag">${{lesson.unit || lesson.id.toUpperCase()}}</span>
            <div class="lesson-name">${{lesson.title}}</div>
            <div class="lesson-type">文體：${{lesson.type}}</div>
            <div style="font-size:0.8rem; color:#4B5563; margin-top:4px;">作者：${{lesson.author}}</div>
        </div>
    `).join('');
}}

function selectLesson(id) {{
    selectedLessonId = id;
    renderLessonCards();
    renderLessonDetail(id);
    const wbSelect = document.getElementById('wb-lesson-filter');
    if (wbSelect) {{
        wbSelect.value = id;
        renderWorkbookView();
    }}
}}

function renderLessonDetail(id) {{
    const lesson = CURRICULUM.find(x => x.id === id);
    if (!lesson) return;
    const container = document.getElementById('lesson-detail-box');
    
    const wb = lesson.workbook || {{}};
    const wpSample = (wb.writing_practice || []).slice(0, 2);
    const puzzleSample = (wb.word_puzzle || []).slice(0, 2);

    container.innerHTML = `
        <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:8px;">
            <h3 style="color:var(--primary-dark); font-size:1.35rem; font-family:'Noto Serif TC';">
                📖 ${{lesson.title}} <span style="font-size:0.95rem; color:var(--text-muted); font-weight:normal;">（${{lesson.author}}）</span>
            </h3>
            <span style="font-size:0.8rem; background:var(--secondary-light); color:var(--secondary-dark); font-weight:800; padding:4px 10px; border-radius:12px;">
                ${{lesson.unit}} · ${{lesson.type}}
            </span>
        </div>
        
        <div class="section-header">🎯 課文核心主旨</div>
        <div class="info-pill-box" style="border-left:4px solid var(--primary); font-weight:700; color:#9A3412;">
            ${{lesson.topic}}
        </div>

        <div class="section-header">📑 課文脈絡與結構分段分析</div>
        <div class="info-pill-box">
            ${{lesson.structure.map(s => `<p style="margin-bottom:6px;">• ${{s}}</p>`).join('')}}
        </div>

        <div class="section-header">✍️ 課文成語與重點生詞 (${{lesson.vocab.length}} 組)</div>
        <div class="vocab-list-grid">
            ${{lesson.vocab.map(v => `
                <div class="vocab-mini-card">
                    <div class="v-word">${{v.word}}</div>
                    <div class="v-zhu">${{v.zhu}}</div>
                    <div class="v-mean">${{v.meaning}}</div>
                </div>
            `).join('')}}
        </div>

        <div class="section-header">💡 修辭技法精彩賞析</div>
        <div class="info-pill-box">
            ${{lesson.rhetoric.map(r => `
                <div style="margin-bottom:8px;">
                    <span style="background:#FFEDD5; color:#C2410C; font-weight:800; font-size:0.8rem; padding:2px 6px; border-radius:6px;">${{r.type}}</span>
                    <p style="font-weight:700; margin:3px 0; color:#1F2937;">「${{r.example}}」</p>
                    <p style="font-size:0.85rem; color:#6B7280;">解析：${{r.analysis}}</p>
                </div>
            `).join('')}}
        </div>

        <div class="section-header">📝 康軒練習簿焦點精要</div>
        <div class="info-pill-box" style="background:#FFF;">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px;">
                <span style="font-weight:800; color:#0369A1;">✍️ 語境生字練習：</span>
                <button class="nav-btn" style="padding:4px 10px; font-size:0.8rem;" onclick="goToWorkbookLesson('${{lesson.id}}')">進入練習簿專題 ➔</button>
            </div>
            ${{wpSample.map(p => `<p style="margin-bottom:6px; color:#374151;">• ${{p}}</p>`).join('')}}
            
            <div style="margin-top:10px; padding-top:8px; border-top:1px dashed #FED7AA; font-weight:800; color:#047857;">
                🧩 精選字謎試身手：
            </div>
            ${{puzzleSample.map(pz => `<p style="margin-top:4px; font-size:0.9rem; color:#4B5563;">• ${{pz}}</p>`).join('')}}
        </div>

        <div style="margin-top:16px; text-align:center;">
            <button class="btn-action" style="width:auto; min-width:240px;" onclick="startSingleLessonQuiz('${{lesson.id}}')">
                📋 立即測驗本課（新挑戰試題）➔
            </button>
        </div>
    `;
}}

// 切換至練習簿頁籤並定位到指定課
function goToWorkbookLesson(lessonId) {{
    const wbSelect = document.getElementById('wb-lesson-filter');
    if (wbSelect) wbSelect.value = lessonId;
    switchTab('workbook');
    renderWorkbookView();
}}

// 渲染課課練習簿專區
function renderWorkbookView() {{
    const filter = document.getElementById('wb-lesson-filter').value;
    const lesson = CURRICULUM.find(x => x.id === filter);
    const container = document.getElementById('wb-content-container');
    if (!lesson || !container) return;

    const wb = lesson.workbook || {{}};
    const writingPractice = wb.writing_practice || [];
    const wordPuzzle = wb.word_puzzle || [];
    const compComb = wb.component_combination || [];
    const sentencePractice = wb.sentence_practice || [];

    container.innerHTML = `
        <div style="margin-bottom:16px; border-left:4px solid var(--primary); padding-left:12px;">
            <h3 style="color:var(--primary-dark); font-size:1.3rem; font-family:'Noto Serif TC';">
                ${{lesson.title}} · 康軒練習簿精華薈萃
            </h3>
            <p style="color:var(--text-muted); font-size:0.9rem;">收錄寫國字注音語境題、字謎探險、部件拆合拼字與句型改寫造句</p>
        </div>

        <!-- 1. 寫國字注音情境練習 -->
        <div class="wb-section-card">
            <div class="wb-section-title">
                <span>✍️</span> 一、看注音寫國字 / 語境生字練習
            </div>
            <div style="display:flex; flex-direction:column; gap:8px;">
                ${{writingPractice.map((item, idx) => `
                    <div style="background:#FFF7ED; border:1px solid #FED7AA; border-radius:10px; padding:10px 14px; font-size:0.95rem; line-height:1.5;">
                        <span style="color:var(--primary-dark); font-weight:800; margin-right:6px;">(${{idx+1}})</span> ${{item}}
                    </div>
                `).join('')}}
            </div>
        </div>

        <!-- 2. 字謎挑戰 -->
        <div class="wb-section-card">
            <div class="wb-section-title">
                <span>🏮</span> 二、趣味字謎大挑戰
            </div>
            ${{wordPuzzle.map((item, idx) => {{
                const parts = item.split('→');
                const prompt = parts[0];
                const ans = parts.length > 1 ? parts[1] : '';
                return `
                    <div class="wb-char-box">
                        <div style="font-weight:800; color:#1F2937; margin-bottom:6px;">
                            謎題 ${{idx + 1}}：${{prompt}}
                        </div>
                        <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:8px;">
                            <span style="font-size:0.88rem; color:#047857; font-weight:700;">
                                💡 思考：動動腦筋，想一想是什麼字？
                            </span>
                            <button class="wb-btn-reveal" onclick="toggleRevealChar('puzzle-res-${{idx}}', this)">
                                👀 揭曉謎底
                            </button>
                        </div>
                        <div id="puzzle-res-${{idx}}" style="display:none; margin-top:8px; padding-top:6px; border-top:1px dashed #BBF7D0; font-size:1.15rem; font-weight:900; color:#B91C1C;">
                            謎底：${{ans}}
                        </div>
                    </div>
                `;
            }}).join('')}}
        </div>

        <!-- 3. 部件拆合拼字 -->
        <div class="wb-section-card">
            <div class="wb-section-title">
                <span>🧩</span> 三、部件拆合與文字組合樂園
            </div>
            ${{compComb.map((item, idx) => {{
                const parts = item.split('=');
                const formula = parts[0];
                const res = parts.length > 1 ? parts[1] : '';
                return `
                    <div class="wb-char-box" style="background:#F0F9FF; border-color:#BAE6FD;">
                        <div style="font-weight:800; color:#0369A1; margin-bottom:6px;">
                            拼字 ${{idx + 1}}：${{formula}} = ？
                        </div>
                        <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:8px;">
                            <span style="font-size:0.88rem; color:#0284C7; font-weight:700;">
                                💡 提示：將左側部件組合起來並想出一個常用語詞
                            </span>
                            <button class="wb-btn-reveal" style="background:#0284C7;" onclick="toggleRevealChar('comb-res-${{idx}}', this)">
                                👀 揭曉答案
                            </button>
                        </div>
                        <div id="comb-res-${{idx}}" style="display:none; margin-top:8px; padding-top:6px; border-top:1px dashed #BAE6FD; font-size:1.15rem; font-weight:900; color:#1D4ED8;">
                            解答：${{res}}
                        </div>
                    </div>
                `;
            }}).join('')}}
        </div>

        <!-- 4. 照樣造句與句型 -->
        <div class="wb-section-card">
            <div class="wb-section-title">
                <span>💬</span> 四、照樣造句與句型變換練習
            </div>
            ${{sentencePractice.map((sp, idx) => {{
                const parts = sp.split('→');
                const origin = parts[0];
                const res = parts.length > 1 ? parts[1] : '';
                return `
                    <div style="background:#FFFDF7; border:1.5px solid #FED7AA; border-radius:12px; padding:12px; margin-bottom:10px;">
                        <div style="font-weight:800; color:#9A3412; font-size:0.95rem; margin-bottom:4px;">
                            題型 ${{idx + 1}}：${{origin}}
                        </div>
                        <div style="font-size:0.92rem; color:#15803D; font-weight:700; margin-top:4px;">
                            ➤ 範例正解：${{res}}
                        </div>
                    </div>
                `;
            }}).join('')}}
        </div>
    `;
}}

function toggleRevealChar(id, btn) {{
    const el = document.getElementById(id);
    if (!el) return;
    if (el.style.display === 'none') {{
        el.style.display = 'block';
        btn.textContent = '🔒 隱藏謎底';
        playSound('correct');
    }} else {{
        el.style.display = 'none';
        btn.textContent = '👀 揭曉謎底';
    }}
}}

// 渲染詞彙寶庫
function renderVocabList() {{
    const filter = document.getElementById('vocab-lesson-filter').value;
    const container = document.getElementById('vocab-grid-container');
    if (!container) return;
    let list = [];
    if (filter === 'all') {{
        CURRICULUM.forEach(l => {{ list.push(...l.vocab); }});
    }} else {{
        const l = CURRICULUM.find(x => x.id === filter);
        if (l) list = l.vocab;
    }}
    container.innerHTML = list.map(v => `
        <div class="vocab-mini-card">
            <div class="v-word">${{v.word}}</div>
            <div class="v-zhu">${{v.zhu}}</div>
            <div class="v-mean">${{v.meaning}}</div>
        </div>
    `).join('');
}}

// 渲染修辭寶庫
function renderRhetoricList() {{
    const container = document.getElementById('rhetoric-container');
    if (!container) return;
    let allRhetorics = [];
    CURRICULUM.forEach(l => {{
        (l.rhetoric || []).forEach(r => {{
            allRhetorics.push({{ lesson: l.title, ...r }});
        }});
    }});
    container.innerHTML = allRhetorics.map(r => `
        <div class="info-pill-box" style="margin-bottom:12px; border-left:4px solid var(--secondary);">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:4px;">
                <span style="font-weight:800; color:var(--primary-dark); font-size:1.05rem;">${{r.type}}</span>
                <span style="font-size:0.8rem; color:var(--text-muted); background:#F3F4F6; padding:2px 8px; border-radius:10px;">${{r.lesson}}</span>
            </div>
            <p style="font-size:1.05rem; font-weight:700; color:#1F2937; margin:6px 0;">「${{r.example}}」</p>
            <p style="font-size:0.9rem; color:#4B5563;">💡 <b>修辭解析：</b>${{r.analysis}}</p>
        </div>
    `).join('');
}}

// 測驗邏輯
function startSingleLessonQuiz(lessonId) {{
    const lesson = CURRICULUM.find(x => x.id === lessonId);
    if (!lesson) return;
    switchTab('quiz');
    quizQuestions = [...(lesson.exam || lesson.quiz || [])];
    initQuizPlay(`${{lesson.title}} · 實戰測驗`);
}}

function startQuiz(mode) {{
    if (mode === 'current') {{
        const lesson = CURRICULUM.find(x => x.id === selectedLessonId);
        if (!lesson) return;
        quizQuestions = [...(lesson.exam || lesson.quiz || [])];
        initQuizPlay(`${{lesson.title}} · 實戰測驗`);
    }} else {{
        // 全冊抽題 10 題
        let pool = [];
        CURRICULUM.forEach(l => {{
            if (l.exam) pool.push(...l.exam);
            else if (l.quiz) pool.push(...l.quiz);
        }});
        quizQuestions = pool.sort(() => Math.random() - 0.5).slice(0, 10);
        initQuizPlay('全冊 12 課 跨單元綜合模擬考');
    }}
}}

function initQuizPlay(title) {{
    currentQuizIdx = 0;
    quizScore = 0;
    
    document.getElementById('quiz-intro-box').classList.add('hidden');
    document.getElementById('quiz-result-box').classList.add('hidden');
    document.getElementById('quiz-play-box').classList.remove('hidden');
    document.getElementById('quiz-mode-title').textContent = title;
    document.getElementById('quiz-total').textContent = quizQuestions.length;

    loadQuizQuestion();
}}

function loadQuizQuestion() {{
    quizAnswered = false;
    document.getElementById('btn-next-quiz').classList.add('hidden');
    document.getElementById('quiz-explanation-box').classList.remove('show');
    document.getElementById('quiz-curr').textContent = currentQuizIdx + 1;
    document.getElementById('quiz-score').textContent = quizScore;

    const q = quizQuestions[currentQuizIdx];
    const tagHtml = q.tag ? `<span class="quiz-tag">${{q.tag}}</span>` : '';
    document.getElementById('quiz-question-text').innerHTML = `${{tagHtml}}<b>第 ${{currentQuizIdx + 1}} 題：</b> ${{q.q}}`;
    
    let shuffledOpts = [...q.options].sort(() => Math.random() - 0.5);
    const optionsBox = document.getElementById('quiz-options-box');
    optionsBox.innerHTML = shuffledOpts.map(opt => `
        <button class="opt-btn" onclick="checkQuizAnswer('${{opt}}', this)">${{opt}}</button>
    `).join('');
}}

function checkQuizAnswer(selected, btn) {{
    if (quizAnswered) return;
    quizAnswered = true;

    const q = quizQuestions[currentQuizIdx];
    const isRight = (selected === q.ans);
    const expBox = document.getElementById('quiz-explanation-box');

    const scorePerQ = Math.round(100 / quizQuestions.length);

    if (isRight) {{
        playSound('correct');
        quizScore += scorePerQ;
        btn.classList.add('correct');
    }} else {{
        playSound('wrong');
        btn.classList.add('wrong');
        document.querySelectorAll('.opt-btn').forEach(b => {{
            if (b.textContent.trim() === q.ans) b.classList.add('correct');
        }});
    }}

    document.getElementById('quiz-score').textContent = quizScore;

    expBox.innerHTML = `
        <div style="font-weight:bold; font-size:1.05rem; margin-bottom:6px; color:${{isRight ? '#065F46' : '#991B1B'}};">
            ${{isRight ? '✓ 太棒了！回答正確！' : '✕ 可惜答錯囉！標準答案為：' + q.ans}}
        </div>
        <div>💡 <b>解析說明：</b>${{q.steps || ''}}</div>
    `;
    expBox.classList.add('show');

    document.getElementById('btn-next-quiz').classList.remove('hidden');
}}

function nextQuizQuestion() {{
    currentQuizIdx++;
    if (currentQuizIdx >= quizQuestions.length) {{
        showQuizResult();
    }} else {{
        loadQuizQuestion();
    }}
}}

function showQuizResult() {{
    document.getElementById('quiz-play-box').classList.add('hidden');
    document.getElementById('quiz-result-box').classList.remove('hidden');
    document.getElementById('quiz-final-score').textContent = quizScore;

    const correctCount = Math.round(quizScore / (100 / quizQuestions.length));
    document.getElementById('quiz-score-detail').textContent = `答對 ${{correctCount}} 題 / 共 ${{quizQuestions.length}} 題`;

    if (quizScore >= 80) {{
        confetti({{ particleCount: 130, spread: 85, origin: {{ y: 0.6 }} }});
        document.getElementById('quiz-res-icon').textContent = '👑';
        document.getElementById('quiz-res-title').textContent = '康軒 3上國語 狀元王！';
        document.getElementById('quiz-res-desc').textContent = '太厲害了！生字、成語、句型與課文理解全面滿分通關！';
    }} else {{
        document.getElementById('quiz-res-icon').textContent = '🦁';
        document.getElementById('quiz-res-title').textContent = '測驗完成，繼續加油！';
        document.getElementById('quiz-res-desc').textContent = '可以多利用「課課練習簿」與「生字成語辭典」複習，下次一定能拿 100 分！';
    }}
}}
</script>
</body>
</html>
'''

with open('chinese3_curriculum.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("成功更新 chinese3_curriculum.html！")
