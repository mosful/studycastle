import sys, json, re
sys.stdout.reconfigure(encoding='utf-8')

with open('chinese3_curriculum.html', 'r', encoding='utf-8') as f:
    html = f.read()

match = re.search(r'const CURRICULUM = (\[[\s\S]*?\]);\s*let selectedLessonId', html)
if match:
    data = json.loads(match.group(1))
    print(f"成功驗證！CURRICULUM 包含 {len(data)} 課：\n")
    for l in data:
        wb = l.get('workbook', {})
        wp = wb.get('writing_practice', [])
        puzzles = wb.get('word_puzzle', [])
        combs = wb.get('component_combination', [])
        sentences = wb.get('sentence_practice', [])
        exam = l.get('exam', [])
        print(f"【{l['id'].upper()}】{l['title']} ({l['unit']})")
        print(f"   • 生字成語辭典: {len(l['vocab'])} 組")
        print(f"   • 修辭技巧賞析: {len(l.get('rhetoric', []))} 組")
        print(f"   • 練習簿語境生字: {len(wp)} 題")
        print(f"   • 練習簿趣味字謎: {len(puzzles)} 則")
        print(f"   • 練習簿部件拆合: {len(combs)} 組")
        print(f"   • 練習簿照樣造句: {len(sentences)} 題")
        print(f"   • 新挑戰測驗試題: {len(exam)} 題 (含解析與標籤)")
        print("-" * 50)
else:
    print("未匹配到 CURRICULUM！")
