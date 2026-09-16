# -*- coding: utf-8 -*-
with open("scripts/generate_all_chinese6_lessons.py", "r", encoding="utf-8") as f:
    text = f.read()

old_tpl = """            q.options.forEach((opt, idx) => {{
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
            }});"""

new_tpl = """            const correctText = (q.ans.length === 1 && ['A','B','C','D'].includes(q.ans))
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
            }});"""

text = text.replace(old_tpl, new_tpl)
with open("scripts/generate_all_chinese6_lessons.py", "w", encoding="utf-8") as f:
    f.write(text)
print("✅ scripts/generate_all_chinese6_lessons.py 模板已同步更新！")
