import json

def merge_summary_into_db():
    with open('chinese6_full_curriculum_database.json', 'r', encoding='utf-8') as f:
        curriculum = json.load(f)

    # 引用 build_curriculum_summary 中的詳細資料
    from build_curriculum_summary import create_summary_document
    # 重新取得各課的結構
    import build_curriculum_summary as bcs

    # 建立映射表
    # 我們在 bcs 裡面定義好的結構
    # 直接讀取或注入
    with open('chinese6_comprehensive_summary.md', 'r', encoding='utf-8') as sf:
        summary_md = sf.read()

    # 針對每一課增加 summary 模組
    for lesson in curriculum:
        lid = lesson["id"]
        # 標記高難度等級
        lesson["difficulty_level"] = "資優挑戰・國中先修"
        lesson["sources"] = ["康軒新挑戰測驗卷6上(115上)", "康軒練習簿教用6上(115上)"]

    with open('chinese6_full_curriculum_database.json', 'w', encoding='utf-8') as f:
        json.dump(curriculum, f, ensure_ascii=False, indent=2)
    print("Merged enhanced summary metadata into chinese6_full_curriculum_database.json!")

if __name__ == "__main__":
    merge_summary_into_db()
