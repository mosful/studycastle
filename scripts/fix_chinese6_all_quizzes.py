# -*- coding: utf-8 -*-
import glob
import json
import os
import re
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

print("=== 全面升級國語六上全冊自修、單課與段考題庫隨機洗牌 ===")

# 1. 升級 chinese6_curriculum.html
with open("chinese6_curriculum.html", "r", encoding="utf-8") as f:
    c6_curr = f.read()

# 替換 renderQuestion 裡的選項渲染
old_c6_render = """            const optContainer = document.getElementById('quizOptions');
            optContainer.innerHTML = '';

            q.options.forEach((opt, oIdx) => {
                const btn = document.createElement('button');
                btn.className = 'quiz-btn';
                btn.textContent = `${['A', 'B', 'C', 'D'][oIdx]}. ${opt}`;
                btn.onclick = () => checkAnswer(opt, q, btn);
                optContainer.appendChild(btn);
            });"""

new_c6_render = """            const optContainer = document.getElementById('quizOptions');
            optContainer.innerHTML = '';

            // 取得標準答案完整文字內容
            const correctText = (q.ans.length === 1 && ['A','B','C','D'].includes(q.ans))
                ? q.options[['A','B','C','D'].indexOf(q.ans)]
                : q.ans;

            // 動態隨機打亂選項順序
            const shuffledOptions = [...q.options].sort(() => Math.random() - 0.5);

            shuffledOptions.forEach((opt, oIdx) => {
                const btn = document.createElement('button');
                btn.className = 'quiz-btn';
                btn.textContent = `${['A', 'B', 'C', 'D'][oIdx]}. ${opt}`;
                btn.onclick = () => checkAnswer(opt, correctText, q, btn);
                optContainer.appendChild(btn);
            });"""

# 替換 checkAnswer
old_c6_check = """        function checkAnswer(selectedOpt, q, selectedBtn) {
            if (answeredCurrent) return;
            answeredCurrent = true;

            const isCorrect = (selectedOpt.trim() === q.ans.trim()) || 
                              (q.ans.length === 1 && ['A','B','C','D'].includes(q.ans) && q.options[['A','B','C','D'].indexOf(q.ans)] === selectedOpt);

            // 標記選項樣式
            const allBtns = document.querySelectorAll('.quiz-btn');
            allBtns.forEach(b => {
                b.disabled = true;
                if (b.textContent.includes(q.ans) || (q.ans.length === 1 && b.textContent.startsWith(q.ans))) {
                    b.classList.add('correct');
                }
            });"""

new_c6_check = """        function checkAnswer(selectedOpt, correctText, q, selectedBtn) {
            if (answeredCurrent) return;
            answeredCurrent = true;

            const isCorrect = (selectedOpt.trim() === correctText.trim());

            // 標記選項樣式
            const allBtns = document.querySelectorAll('.quiz-btn');
            allBtns.forEach(b => {
                b.disabled = true;
                if (b.textContent.includes(correctText.trim())) {
                    b.classList.add('correct');
                }
            });"""

if old_c6_render in c6_curr and old_c6_check in c6_curr:
    c6_curr = c6_curr.replace(old_c6_render, new_c6_render).replace(old_c6_check, new_c6_check)
    with open("chinese6_curriculum.html", "w", encoding="utf-8") as f:
        f.write(c6_curr)
    print("✅ chinese6_curriculum.html 升級完成！")
else:
    print("⚠️ chinese6_curriculum.html 未完全匹配模板，檢查正則替換...")
    # 彈性替換
    c6_curr = re.sub(
        r'q\.options\.forEach\(\(opt,\s*oIdx\)\s*=>\s*\{[\s\S]*?checkAnswer\(opt,\s*q,\s*btn\);[\s\S]*?\}\);',
        """const correctText = (q.ans.length === 1 && ['A','B','C','D'].includes(q.ans)) ? q.options[['A','B','C','D'].indexOf(q.ans)] : q.ans;
            const shuffledOptions = [...q.options].sort(() => Math.random() - 0.5);
            shuffledOptions.forEach((opt, oIdx) => {
                const btn = document.createElement('button');
                btn.className = 'quiz-btn';
                btn.textContent = `${['A', 'B', 'C', 'D'][oIdx]}. ${opt}`;
                btn.onclick = () => checkAnswer(opt, correctText, q, btn);
                optContainer.appendChild(btn);
            });""",
        c6_curr
    )
    c6_curr = re.sub(
        r'function\s+checkAnswer\s*\(selectedOpt,\s*q,\s*selectedBtn\)\s*\{[\s\S]*?const\s+isCorrect\s*=[^;]+;',
        """function checkAnswer(selectedOpt, correctText, q, selectedBtn) {
            if (answeredCurrent) return;
            answeredCurrent = true;
            const isCorrect = (selectedOpt.trim() === correctText.trim());""",
        c6_curr
    )
    with open("chinese6_curriculum.html", "w", encoding="utf-8") as f:
        f.write(c6_curr)
    print("✅ chinese6_curriculum.html (正則) 升級完成！")


# 2. 升級 chinese6_final.html
with open("chinese6_final.html", "r", encoding="utf-8") as f:
    c6_final = f.read()

old_final_render = """            q.options.forEach((opt, idx) => {
                const btn = document.createElement('button');
                btn.className = 'opt-btn';
                btn.textContent = `${['A', 'B', 'C', 'D'][idx]}. ${opt}`;
                btn.onclick = () => submitExamAnswer(opt, q, btn);
                optBox.appendChild(btn);
            });"""

new_final_render = """            const correctText = (q.ans.length === 1 && ['A','B','C','D'].includes(q.ans))
                ? q.options[['A','B','C','D'].indexOf(q.ans)]
                : q.ans;

            const shuffledOptions = [...q.options].sort(() => Math.random() - 0.5);

            shuffledOptions.forEach((opt, idx) => {
                const btn = document.createElement('button');
                btn.className = 'opt-btn';
                btn.textContent = `${['A', 'B', 'C', 'D'][idx]}. ${opt}`;
                btn.onclick = () => submitExamAnswer(opt, correctText, q, btn);
                optBox.appendChild(btn);
            });"""

old_final_submit = """        function submitExamAnswer(selected, q, btn) {
            if (isAnswered) return;
            isAnswered = true;

            const isCorrect = (selected.trim() === q.ans.trim()) || 
                              (q.ans.length === 1 && ['A','B','C','D'].includes(q.ans) && q.options[['A','B','C','D'].indexOf(q.ans)] === selected);

            const allBtns = document.querySelectorAll('.opt-btn');
            allBtns.forEach(b => {
                b.disabled = true;
                if (b.textContent.includes(q.ans) || (q.ans.length === 1 && b.textContent.startsWith(q.ans))) {
                    b.classList.add('correct');
                }
            });"""

new_final_submit = """        function submitExamAnswer(selected, correctText, q, btn) {
            if (isAnswered) return;
            isAnswered = true;

            const isCorrect = (selected.trim() === correctText.trim());

            const allBtns = document.querySelectorAll('.opt-btn');
            allBtns.forEach(b => {
                b.disabled = true;
                if (b.textContent.includes(correctText.trim())) {
                    b.classList.add('correct');
                }
            });"""

if old_final_render in c6_final and old_final_submit in c6_final:
    c6_final = c6_final.replace(old_final_render, new_final_render).replace(old_final_submit, new_final_submit)
    with open("chinese6_final.html", "w", encoding="utf-8") as f:
        f.write(c6_final)
    print("✅ chinese6_final.html 升級完成！")
else:
    print("⚠️ chinese6_final.html 未完全匹配模板")


# 3. 升級 scripts/generate_all_chinese6_lessons.py 並重新生成 12 課單課 HTML
with open("scripts/generate_all_chinese6_lessons.py", "r", encoding="utf-8") as f:
    gen_script = f.read()

old_lesson_render = """            q.options.forEach((opt, idx) => {
                const btn = document.createElement('button');
                btn.className = 'quiz-opt-btn';
                btn.textContent = `${['A', 'B', 'C', 'D'][idx]}. ${opt}`;
                btn.onclick = () => handleAnswer(opt, q, btn);
                optGrid.appendChild(btn);
            });"""

new_lesson_render = """            const correctText = (q.ans.length === 1 && ['A','B','C','D'].includes(q.ans))
                ? q.options[['A','B','C','D'].indexOf(q.ans)]
                : q.ans;

            const shuffledOptions = [...q.options].sort(() => Math.random() - 0.5);

            shuffledOptions.forEach((opt, idx) => {
                const btn = document.createElement('button');
                btn.className = 'quiz-opt-btn';
                btn.textContent = `${['A', 'B', 'C', 'D'][idx]}. ${opt}`;
                btn.onclick = () => handleAnswer(opt, correctText, q, btn);
                optGrid.appendChild(btn);
            });"""

old_lesson_handle = """        function handleAnswer(chosen, q, btn) {
            if (answered) return;
            answered = true;

            const isCorrect = (chosen.trim() === q.ans.trim()) || 
                              (q.ans.length === 1 && ['A','B','C','D'].includes(q.ans) && q.options[['A','B','C','D'].indexOf(q.ans)] === chosen);

            const allBtns = document.querySelectorAll('.quiz-opt-btn');
            allBtns.forEach(b => {
                b.disabled = true;
                if (b.textContent.includes(q.ans) || (q.ans.length === 1 && b.textContent.startsWith(q.ans))) {
                    b.classList.add('correct');
                }
            });"""

new_lesson_handle = """        function handleAnswer(chosen, correctText, q, btn) {
            if (answered) return;
            answered = true;

            const isCorrect = (chosen.trim() === correctText.trim());

            const allBtns = document.querySelectorAll('.quiz-opt-btn');
            allBtns.forEach(b => {
                b.disabled = true;
                if (b.textContent.includes(correctText.trim())) {
                    b.classList.add('correct');
                }
            });"""

if old_lesson_render in gen_script and old_lesson_handle in gen_script:
    gen_script = gen_script.replace(old_lesson_render, new_lesson_render).replace(old_lesson_handle, new_lesson_handle)
    with open("scripts/generate_all_chinese6_lessons.py", "w", encoding="utf-8") as f:
        f.write(gen_script)
    print("✅ scripts/generate_all_chinese6_lessons.py 升級完成！")
else:
    print("⚠️ scripts/generate_all_chinese6_lessons.py 未完全匹配模板")

# 4. 直接修改現有的 chinese6_lesson1.html ~ chinese6_lesson12.html
lesson_files = glob.glob("chinese6_lesson*.html")
for lf in sorted(lesson_files):
    with open(lf, "r", encoding="utf-8") as f:
        l_text = f.read()
    if old_lesson_render in l_text and old_lesson_handle in l_text:
        l_text = l_text.replace(old_lesson_render, new_lesson_render).replace(old_lesson_handle, new_lesson_handle)
        with open(lf, "w", encoding="utf-8") as f:
            f.write(l_text)
        print(f"✅ {lf} 升級完成！")
    else:
        # 正則相容替換
        l_text = re.sub(
            r'q\.options\.forEach\(\(opt,\s*idx\)\s*=>\s*\{[\s\S]*?handleAnswer\(opt,\s*q,\s*btn\);[\s\S]*?\}\);',
            new_lesson_render,
            l_text
        )
        l_text = re.sub(
            r'function\s+handleAnswer\s*\(chosen,\s*q,\s*btn\)\s*\{[\s\S]*?const\s+allBtns\s*=\s*document\.querySelectorAll\(\'\.quiz-opt-btn\'\);[\s\S]*?\}\);',
            new_lesson_handle,
            l_text
        )
        with open(lf, "w", encoding="utf-8") as f:
            f.write(l_text)
        print(f"✅ {lf} (正則) 升級完成！")
