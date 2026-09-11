import json

def generate_lesson_pages():
    with open('chinese6_full_curriculum_database.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    template = """<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>6上國語 {lesson_title} | 素養高階挑戰 | 學習城堡</title>
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Fredoka:wght@500;600;700&family=Noto+Serif+TC:wght@600;700;900&family=Noto+Sans+TC:wght@400;500;700;900&display=swap" rel="stylesheet">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/canvas-confetti/1.9.2/confetti.browser.min.js"></script>
    <style>
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
            font-size: 0.75rem;
            font-weight: 800;
            margin-bottom: 6px;
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
            gap: 10px;
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

        <div class="section-card">
            <h2 class="section-title">🎯 課堂素養高階挑戰（共 {quiz_count} 題）</h2>
            <div class="quiz-hud">
                <span class="quiz-progress" id="quizProg">進度：第 1 / {quiz_count} 題</span>
                <span class="quiz-score">得分：<span id="quizScore">0</span> 分</span>
            </div>

            <div class="question-box">
                <span class="question-type" id="qType">考點解析</span>
                <div class="question-text" id="qText">題目載入中...</div>
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

            const optGrid = document.getElementById('optGrid');
            optGrid.innerHTML = '';

            q.options.forEach((opt, idx) => {{
                const btn = document.createElement('button');
                btn.className = 'quiz-opt-btn';
                btn.textContent = `${{['A', 'B', 'C', 'D'][idx]}}. ${{opt}}`;
                btn.onclick = () => handleAnswer(opt, q, btn);
                optGrid.appendChild(btn);
            }});
        }}

        function handleAnswer(chosen, q, btn) {{
            if (answered) return;
            answered = true;

            const isCorrect = (chosen.trim() === q.ans.trim()) || 
                              (q.ans.length === 1 && ['A','B','C','D'].includes(q.ans) && q.options[['A','B','C','D'].indexOf(q.ans)] === chosen);

            const allBtns = document.querySelectorAll('.quiz-opt-btn');
            allBtns.forEach(b => {{
                b.disabled = true;
                if (b.textContent.includes(q.ans) || (q.ans.length === 1 && b.textContent.startsWith(q.ans))) {{
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
    for idx, lesson in enumerate(data):
        lesson_num = idx + 1
        fname = f"chinese6_lesson{lesson_num}.html"
        rendered = template.format(
            lesson_title=lesson["title"],
            lesson_author=lesson.get("author", "康軒語文編輯小組"),
            lesson_type=lesson.get("type", "課文"),
            lesson_topic=lesson.get("topic", ""),
            quiz_count=len(lesson.get("quiz", [])),
            quiz_json=json.dumps(lesson.get("quiz", []), ensure_ascii=False)
        )
        with open(fname, "w", encoding="utf-8") as out_f:
            out_f.write(rendered)
        print(f"Generated {fname} ({len(lesson.get('quiz', []))} questions)")

if __name__ == "__main__":
    generate_lesson_pages()
