import json

def get_vocab_radical_badge(word):
    if not word: return ''
    if any(k in word for k in ['心', '情', '意', '悵', '忌', '懍']):
        return '<span class="radical-badge" title="心部：與情感、內心想法相關">❤️ 心部·內心情思</span>'
    if any(k in word for k in ['草', '芥', '蒂', '落', '萌', '茫']):
        return '<span class="radical-badge" title="艸部：與草木植物相關">🌱 艸部·植物生長</span>'
    if any(k in word for k in ['水', '海', '澎', '湃', '湧', '洋', '淋']):
        return '<span class="radical-badge" title="水部：與水流波濤相關">🌊 水部·波濤流動</span>'
    if any(k in word for k in ['刀', '券', '切', '刻', '劍', '利']):
        return '<span class="radical-badge" title="刀部：與利器切削、契約相關">🗡️ 刀部·利器契約</span>'
    if any(k in word for k in ['手', '持', '操', '挽', '推', '擬']):
        return '<span class="radical-badge" title="手部：與動作操作相關">✋ 手部·動作舉止</span>'
    if any(k in word for k in ['足', '踏', '蹈', '蹣', '跚', '跑']):
        return '<span class="radical-badge" title="足部：與雙腳步伐相關">👣 足部·步伐行動</span>'
    if any(k in word for k in ['目', '瞻', '仰', '瞪', '眺', '視']):
        return '<span class="radical-badge" title="目部：與眼睛注視相關">👁️ 目部·觀察凝視</span>'
    if any(k in word for k in ['口', '喊', '囂', '嘆', '咽', '嘲']):
        return '<span class="radical-badge" title="口部：與言語聲音相關">🗣️ 口部·言語聲響</span>'
    if any(k in word for k in ['虫', '蜿', '蜒', '蛇', '蝶']):
        return '<span class="radical-badge" title="虫部：與爬蟲曲折盤旋相關">🐛 虫部·曲折盤旋</span>'
    if any(k in word for k in ['羽', '翼', '翔', '翱']):
        return '<span class="radical-badge" title="羽部：與鳥羽飛翔相關">🪶 羽部·展翅高飛</span>'
    if any(k in word for k in ['玉', '璀', '璨', '琢']):
        return '<span class="radical-badge" title="玉部：與美玉光彩相關">💎 玉部·美玉星芒</span>'
    return '<span class="radical-badge">📝 字形意象</span>'

def generate_lesson_pages():
    with open('chinese6_full_curriculum_database.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    template = """<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>6上國語 {lesson_title} | 素養高階挑戰 | 學習城堡</title>
    <!-- Favicon 網站圖示 -->
    <link rel="icon" type="image/svg+xml" href="favicon.svg">
    <link rel="apple-touch-icon" href="favicon.svg">
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Fredoka:wght@500;600;700&family=Noto+Serif+TC:wght@600;700;900&family=Noto+Sans+TC:wght@400;500;700;900&display=swap" rel="stylesheet">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/canvas-confetti/1.9.2/confetti.browser.min.js"></script>
    <script src="chinese6_visual_engine.js"></script>
    <style>
        /* 題目圖像式情境卡片 */
        .quiz-visual-box {{
            margin: 14px 0 16px;
            background: #FFFFFF;
            border: 2px dashed #4F46E5;
            border-radius: 14px;
            padding: 12px 14px;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            box-shadow: inset 0 2px 6px rgba(79, 70, 229, 0.04);
        }}
        .visual-badge-tag {{
            align-self: flex-start;
            font-size: 11.5px;
            font-weight: 800;
            color: #3730A3;
            background: #EEF2FF;
            padding: 3px 10px;
            border-radius: 6px;
            margin-bottom: 8px;
            display: inline-flex;
            align-items: center;
            gap: 5px;
        }}
        .chinese-visual-svg {{
            max-width: 100%;
            height: auto;
            filter: drop-shadow(0 2px 4px rgba(0,0,0,0.05));
        }}
        :root {{
            --primary: #4F46E5;
            --primary-dark: #3730A3;
            --secondary: #0EA5E9;
            --accent-amber: #D97706;
            --accent-emerald: #059669;
            --accent-rose: #E11D48;
            --bg-gradient: linear-gradient(135deg, #F8FAFC 0%, #EEF2FF 50%, #F1F5F9 100%);
            --card-bg: rgba(255, 255, 255, 0.95);
            --text-main: #1E293B;
            --text-muted: #64748B;
            --border-color: #E2E8F0;
            --radius-lg: 20px;
            --radius-md: 14px;
            --shadow-md: 0 10px 25px -5px rgba(79, 70, 229, 0.15);
        }}

        * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: 'Noto Sans TC', sans-serif;
            transition: all 0.25s ease;
        }}

        body {{
            background: var(--bg-gradient);
            background-attachment: fixed;
            color: var(--text-main);
            min-height: 100vh;
            padding: 20px 14px 60px;
        }}

        .container {{
            max-width: 860px;
            margin: 0 auto;
            display: flex;
            flex-direction: column;
            gap: 18px;
        }}

        .header-nav {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 10px;
        }}

        .nav-link {{
            display: inline-flex;
            align-items: center;
            gap: 8px;
            padding: 8px 18px;
            background: var(--card-bg);
            border: 2px solid var(--primary);
            border-radius: 30px;
            color: var(--primary-dark);
            text-decoration: none;
            font-weight: 700;
            font-size: 0.95rem;
            box-shadow: 0 2px 6px rgba(0,0,0,0.05);
        }}

        .nav-link:hover {{
            background: var(--primary);
            color: #FFF;
            transform: translateY(-2px);
        }}

        .badge-group {{
            display: flex;
            gap: 8px;
        }}

        .hero-badge {{
            background: linear-gradient(135deg, var(--primary), #7C3AED);
            color: #FFF;
            padding: 6px 14px;
            border-radius: 20px;
            font-size: 0.85rem;
            font-weight: 800;
        }}

        .hero-banner {{
            background: var(--card-bg);
            border-radius: var(--radius-lg);
            padding: 26px 20px;
            text-align: center;
            border: 3px solid var(--primary);
            box-shadow: var(--shadow-md);
        }}

        .hero-title {{
            font-family: 'Noto Serif TC', serif;
            font-size: clamp(1.8rem, 3.5vw, 2.3rem);
            color: var(--primary-dark);
            font-weight: 900;
            margin-bottom: 6px;
        }}

        .hero-meta {{
            color: var(--text-muted);
            font-size: 0.95rem;
        }}

        .section-card {{
            background: var(--card-bg);
            border-radius: var(--radius-lg);
            padding: 22px 20px;
            border: 2px solid var(--border-color);
            box-shadow: 0 4px 15px rgba(0,0,0,0.04);
        }}

        .section-title {{
            font-size: 1.25rem;
            font-weight: 800;
            color: var(--primary-dark);
            margin-bottom: 12px;
            display: flex;
            align-items: center;
            gap: 8px;
            border-bottom: 2px dashed var(--border-color);
            padding-bottom: 8px;
        }}

        /* 課文思維導圖流向卡片 */
        .story-flow-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
            gap: 12px;
            margin: 14px 0 6px;
        }}
        .story-flow-node {{
            background: #FFFFFF;
            border: 2px solid var(--border-color);
            border-top: 5px solid var(--primary);
            border-radius: 12px;
            padding: 14px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.03);
            display: flex;
            flex-direction: column;
            gap: 6px;
        }}
        .flow-node-tag {{
            font-size: 0.85rem;
            font-weight: 800;
            color: var(--primary);
            background: #EEF2FF;
            padding: 2px 8px;
            border-radius: 6px;
            align-self: flex-start;
        }}
        .flow-node-content {{
            font-size: 0.95rem;
            line-height: 1.6;
            color: var(--text-main);
            font-weight: 600;
        }}

        /* 生字成語陷阱圖鑑卡片 */
        .vocab-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 12px;
            margin-top: 14px;
        }}
        .vocab-card {{
            background: #FFFFFF;
            border: 2px solid var(--border-color);
            border-radius: 14px;
            padding: 14px;
            box-shadow: 0 3px 8px rgba(0,0,0,0.03);
            display: flex;
            flex-direction: column;
            gap: 6px;
        }}
        .vocab-head {{
            display: flex;
            align-items: baseline;
            gap: 8px;
            border-bottom: 1.5px dashed var(--border-color);
            padding-bottom: 6px;
        }}
        .v-word {{
            font-size: 1.25rem;
            font-weight: 900;
            color: var(--primary-dark);
            font-family: 'Noto Serif TC', serif;
        }}
        .v-zhu {{
            color: var(--accent-amber);
            font-weight: 700;
            font-size: 0.9rem;
        }}
        .radical-badge {{
            display: inline-block;
            background: #FEF3C7;
            color: #92400E;
            border: 1px solid #FCD34D;
            padding: 2px 8px;
            border-radius: 6px;
            font-size: 0.8rem;
            font-weight: 700;
            align-self: flex-start;
        }}
        .v-meaning {{
            font-size: 0.9rem;
            line-height: 1.5;
            color: var(--text-main);
        }}
        .v-trap {{
            margin-top: 4px;
            background: #FEF2F2;
            border: 1px solid #FECACA;
            border-radius: 8px;
            padding: 6px 10px;
            font-size: 0.85rem;
            color: #991B1B;
            font-weight: 600;
        }}

        /* 題目互動介面 */
        .quiz-hud {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 16px;
        }}

        .quiz-progress {{
            font-weight: 700;
            color: var(--text-muted);
        }}

        .quiz-score {{
            font-size: 1.4rem;
            font-weight: 900;
            color: var(--accent-amber);
            font-family: 'Fredoka', sans-serif;
        }}

        .question-box {{
            background: #F8FAFC;
            border-left: 6px solid var(--primary);
            border-radius: 0 var(--radius-md) var(--radius-md) 0;
            padding: 16px;
            margin-bottom: 18px;
        }}

        .question-type {{
            display: inline-block;
            background: var(--primary);
            color: #FFF;
            padding: 2px 8px;
            border-radius: 6px;
            font-size: 0.8rem;
            font-weight: 800;
            margin-bottom: 8px;
        }}

        .question-text {{
            font-size: 1.15rem;
            font-weight: 800;
            line-height: 1.6;
            color: var(--text-main);
        }}

        .options-grid {{
            display: flex;
            flex-direction: column;
            gap: 12px;
        }}

        .quiz-opt-btn {{
            width: 100%;
            padding: 14px 18px;
            background: #FFF;
            border: 2px solid var(--border-color);
            border-radius: var(--radius-md);
            font-size: 1rem;
            font-weight: 600;
            color: var(--text-main);
            text-align: left;
            cursor: pointer;
            box-shadow: 0 2px 4px rgba(0,0,0,0.02);
            line-height: 1.5;
        }}

        .quiz-opt-btn:hover:not(:disabled) {{
            border-color: var(--primary);
            background: #EEF2FF;
            transform: translateX(4px);
        }}

        .quiz-opt-btn.correct {{
            background: #ECFDF5 !important;
            border-color: var(--accent-emerald) !important;
            color: #065F46 !important;
            font-weight: 800;
        }}

        .quiz-opt-btn.wrong {{
            background: #FEF2F2 !important;
            border-color: var(--accent-rose) !important;
            color: #991B1B !important;
            font-weight: 800;
        }}

        .feedback-box {{
            margin-top: 16px;
            padding: 14px;
            border-radius: var(--radius-md);
            line-height: 1.6;
            display: none;
        }}

        .feedback-box.correct {{
            background: #ECFDF5;
            border: 2px solid var(--accent-emerald);
            color: #065F46;
            display: block;
        }}

        .feedback-box.wrong {{
            background: #FEF2F2;
            border: 2px solid var(--accent-rose);
            color: #991B1B;
            display: block;
        }}

        .next-btn {{
            margin-top: 14px;
            padding: 10px 24px;
            background: var(--primary);
            color: #FFF;
            border: none;
            border-radius: 25px;
            font-size: 1rem;
            font-weight: 800;
            cursor: pointer;
            float: right;
            display: none;
        }}

        .next-btn:hover {{
            background: var(--primary-dark);
            transform: translateY(-2px);
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header-nav">
            <div style="display: flex; gap: 8px;">
                <a href="index.html" class="nav-link">🏠 回主頁</a>
                <a href="chinese6_curriculum.html" class="nav-link">📖 6上國語全冊總覽</a>
            </div>
            <div class="badge-group">
                <span class="hero-badge">康軒 6 上國語</span>
                <span class="hero-badge" style="background: linear-gradient(135deg, #EF4444, #F59E0B);">🔥 升級版試題</span>
            </div>
        </div>

        <div class="hero-banner">
            <h1 class="hero-title">{lesson_title}</h1>
            <p class="hero-meta">作者：{lesson_author} ｜ 文體：{lesson_type}</p>
        </div>

        <div class="section-card">
            <h2 class="section-title">📖 課文核心大意與精神</h2>
            <p style="line-height: 1.8; font-size: 1.05rem;">{lesson_topic}</p>
        </div>

        {story_flow_section}

        {vocab_section}

        <div class="section-card">
            <h2 class="section-title">🎯 課堂素養高階挑戰（共 {quiz_count} 題）</h2>
            <div class="quiz-hud">
                <span class="quiz-progress" id="quizProg">進度：第 1 / {quiz_count} 題</span>
                <span class="quiz-score">得分：<span id="quizScore">0</span> 分</span>
            </div>

            <div class="question-box">
                <span class="question-type" id="qType">考點解析</span>
                <div class="question-text" id="qText">題目載入中...</div>
                <div class="quiz-visual-box" id="quizVisualBox"></div>
            </div>

            <div class="options-grid" id="optGrid"></div>
            <div class="feedback-box" id="feedbackBox"></div>
            <button class="next-btn" id="nextBtn" onclick="nextQuestion()">下一題 ➔</button>
            <div style="clear: both;"></div>
        </div>
    </div>

    <script>
        const quizData = {quiz_json};
        let curIdx = 0;
        let score = 0;
        let answered = false;

        function renderQuestion() {{
            answered = false;
            document.getElementById('nextBtn').style.display = 'none';
            document.getElementById('feedbackBox').style.display = 'none';

            if (curIdx >= quizData.length) {{
                renderFinish();
                return;
            }}

            const q = quizData[curIdx];
            document.getElementById('quizProg').textContent = `進度：第 ${{curIdx + 1}} / ${{quizData.length}} 題`;
            document.getElementById('quizScore').textContent = score;
            document.getElementById('qType').textContent = q.type || '考點陷阱';
            document.getElementById('qText').textContent = q.q;

            // 渲染題目情境插畫與視覺鷹架
            const visualBox = document.getElementById('quizVisualBox');
            if (visualBox && typeof getChineseVisualBadge === 'function') {{
                const badgeSvg = getChineseVisualBadge(q, '{lesson_title}');
                visualBox.innerHTML = `
                    <div class="visual-badge-tag">💡 看圖懂題意（情境與字形圖解）</div>
                    ${{badgeSvg}}
                `;
            }}

            const optGrid = document.getElementById('optGrid');
            optGrid.innerHTML = '';

            const correctText = (q.ans.length === 1 && ['A','B','C','D'].includes(q.ans))
                ? q.options[['A','B','C','D'].indexOf(q.ans)]
                : q.ans;

            const shuffledOptions = [...q.options].sort(() => Math.random() - 0.5);

            shuffledOptions.forEach((opt, idx) => {{
                const btn = document.createElement('button');
                btn.className = 'quiz-opt-btn';
                btn.textContent = `${{['A', 'B', 'C', 'D'][idx]}}. ${{opt}}`;
                btn.onclick = () => handleAnswer(opt, correctText, q, btn);
                optGrid.appendChild(btn);
            }});
        }}

        function handleAnswer(chosen, correctText, q, btn) {{
            if (answered) return;
            answered = true;

            const isCorrect = (chosen.trim() === correctText.trim());

            const allBtns = document.querySelectorAll('.quiz-opt-btn');
            allBtns.forEach(b => {{
                b.disabled = true;
                if (b.textContent.includes(correctText.trim())) {{
                    b.classList.add('correct');
                }}
            }});

            const fb = document.getElementById('feedbackBox');
            if (isCorrect) {{
                btn.classList.add('correct');
                score += 10;
                document.getElementById('quizScore').textContent = score;
                fb.className = 'feedback-box correct';
                fb.innerHTML = `<strong>✅ 答對了！實力出色！</strong><br>${{q.steps || '完全掌握考題核心觀念！'}}`;
                if (typeof confetti === 'function') confetti({{ particleCount: 35, spread: 60, origin: {{ y: 0.8 }} }});
            }} else {{
                btn.classList.add('wrong');
                fb.className = 'feedback-box wrong';
                fb.innerHTML = `<strong>❌ 答錯了，請特別注意觀念陷阱！</strong><br>正確解答：<strong>${{q.ans}}</strong><br><strong>【考點詳解】</strong>：${{q.steps || '要仔細審題辨別字音字形與上下文語意！'}}`;
            }}

            document.getElementById('nextBtn').style.display = 'block';
        }}

        function nextQuestion() {{
            curIdx++;
            renderQuestion();
        }}

        function renderFinish() {{
            const maxScore = quizData.length * 10;
            const pct = Math.round((score / maxScore) * 100);
            document.getElementById('optGrid').innerHTML = `
                <div style="text-align: center; padding: 25px 10px;">
                    <h3 style="font-size: 1.8rem; color: var(--primary-dark);">🎉 恭喜完成本課挑戰！</h3>
                    <p style="font-size: 1.3rem; font-weight: 800; color: var(--accent-amber); margin: 10px 0;">最終得分：${{score}} / ${{maxScore}} 分 (${{pct}}%)</p>
                    <a href="chinese6_curriculum.html" style="display: inline-block; margin-top: 15px; padding: 10px 24px; background: var(--primary); color: #FFF; border-radius: 20px; font-weight: 800; text-decoration: none;">返回 6 上國語全冊總覽</a>
                </div>
            `;
            document.getElementById('qText').textContent = '挑戰總結算';
            document.getElementById('nextBtn').style.display = 'none';
            document.getElementById('feedbackBox').style.display = 'none';
            if (pct >= 80 && typeof confetti === 'function') {{
                confetti({{ particleCount: 80, spread: 70, origin: {{ y: 0.6 }} }});
            }}
        }}

        window.onload = renderQuestion;
    </script>
</body>
</html>
"""
    step_tags = ['🌱 起因背景', '🌊 情節發展', '⚡ 高潮轉折', '🌟 啟發結局']

    for idx, lesson in enumerate(data):
        lesson_num = idx + 1
        fname = f"chinese6_lesson{lesson_num}.html"

        # 構造課文思維導圖區塊
        story_flow_section = ""
        if lesson.get("structure") and len(lesson["structure"]) > 0:
            nodes_html = ""
            for sIdx, st in enumerate(lesson["structure"]):
                tag = step_tags[sIdx] if sIdx < len(step_tags) else f"第 {sIdx+1} 階段"
                parts = st.split('：')
                content = parts[1] if len(parts) > 1 else st
                nodes_html += f"""
                    <div class="story-flow-node">
                        <div class="flow-node-tag">{tag}</div>
                        <div class="flow-node-content">{content}</div>
                    </div>
                """
            story_flow_section = f"""
            <div class="section-card">
                <h2 class="section-title">🗺️ 課文情節起承轉合思維導圖</h2>
                <div class="story-flow-grid">
                    {nodes_html}
                </div>
            </div>
            """

        # 構造生字成語圖鑑區塊
        vocab_section = ""
        if lesson.get("vocab") and len(lesson["vocab"]) > 0:
            v_cards = ""
            for v in lesson["vocab"]:
                badge = get_vocab_radical_badge(v.get("word", ""))
                trap_html = f'<div class="v-trap">⚠️ 易錯考點：{v["trap"]}</div>' if v.get("trap") else ""
                v_cards += f"""
                    <div class="vocab-card">
                        <div class="vocab-head">
                            <span class="v-word">{v.get("word", "")}</span>
                            <span class="v-zhu">{v.get("zhu", "")}</span>
                        </div>
                        <div style="margin: 4px 0 6px;">{badge}</div>
                        <div class="v-meaning">{v.get("meaning", "")}</div>
                        {trap_html}
                    </div>
                """
            vocab_section = f"""
            <div class="section-card">
                <h2 class="section-title">💡 重點生字成語與部首象形圖鑑</h2>
                <div class="vocab-grid">
                    {v_cards}
                </div>
            </div>
            """

        rendered = template.format(
            lesson_title=lesson["title"],
            lesson_author=lesson.get("author", "康軒語文編輯小組"),
            lesson_type=lesson.get("type", "課文"),
            lesson_topic=lesson.get("topic", ""),
            story_flow_section=story_flow_section,
            vocab_section=vocab_section,
            quiz_count=len(lesson.get("quiz", [])),
            quiz_json=json.dumps(lesson.get("quiz", []), ensure_ascii=False)
        )
        with open(fname, "w", encoding="utf-8") as out_f:
            out_f.write(rendered)
        print(f"Generated {fname} ({len(lesson.get('quiz', []))} questions)")

if __name__ == "__main__":
    generate_lesson_pages()
