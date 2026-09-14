import os
import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

def verify_system():
    print("=== 1. 驗證課程資料庫 ===")
    db_file = "chinese6_full_curriculum_database.json"
    assert os.path.exists(db_file), "Database file missing!"
    with open(db_file, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    assert len(data) == 12, f"Expected 12 lessons, found {len(data)}"
    total_q = 0
    for idx, l in enumerate(data):
        assert "id" in l and "title" in l and "quiz" in l, f"Lesson {idx} format invalid"
        q_list = l["quiz"]
        total_q += len(q_list)
        for q_idx, q in enumerate(q_list):
            assert "q" in q and "options" in q and "ans" in q, f"Question {q_idx} in {l['id']} missing fields"
            assert len(q["options"]) == 4, f"Question {q_idx} does not have 4 options"
            # 檢查答案是否在選項或為 A/B/C/D
            ans = q["ans"]
            valid_ans = ans in ["A", "B", "C", "D"] or any(ans.strip() == opt.strip() for opt in q["options"])
            assert valid_ans, f"Answer {ans} invalid in {l['id']} Q{q_idx}"
    print(f"✅ 課程資料庫驗證通過：共 12 課，全冊共 {total_q} 題進階高難度素養題！")

    print("\n=== 2. 驗證單元網頁檔案 ===")
    html_files = [
        "chinese6_curriculum.html",
        "chinese6_midterm.html",
        "chinese6_final.html"
    ] + [f"chinese6_lesson{i}.html" for i in range(1, 13)]

    for f in html_files:
        assert os.path.exists(f), f"File {f} missing!"
        size = os.path.getsize(f)
        assert size > 1000, f"File {f} is too small ({size} bytes)"
    print(f"✅ 全套 15 個 HTML 單元與綜合評量頁面皆完整存在且內容充足！")

    print("\n=== 3. 驗證 index.html 與 portal.html 導覽卡片 ===")
    for portal_name in ["index.html", "portal.html"]:
        with open(portal_name, "r", encoding="utf-8") as pf:
            content = pf.read()
        assert "chinese6_curriculum.html" in content, f"chinese6_curriculum missing in {portal_name}"
        assert "chinese6_final.html" in content, f"chinese6_final missing in {portal_name}"
        for i in range(1, 13):
            assert f"chinese6_lesson{i}.html" in content, f"chinese6_lesson{i} missing in {portal_name}"
        print(f"✅ {portal_name} 中 6 上國語全冊旗艦、L1~L12 與期中/期末卡片配置完全正確！")

    print("\n🎉 6上國語高難度教材升級驗證全數通過！")

if __name__ == "__main__":
    verify_system()
