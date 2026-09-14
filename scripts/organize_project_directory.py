# -*- coding: utf-8 -*-
import os
import shutil

BASE_DIR = r"c:\Code\StudyCastle"

# 目標目錄
SCRIPTS_DIR = os.path.join(BASE_DIR, "scripts")
ARCHIVE_OCR_DIR = os.path.join(BASE_DIR, "archive", "ocr_raw")
ARCHIVE_TXT_DIR = os.path.join(BASE_DIR, "archive", "temp_txt")
ARCHIVE_PAGES_DIR = os.path.join(BASE_DIR, "archive", "extracted_pages")

for d in [SCRIPTS_DIR, ARCHIVE_OCR_DIR, ARCHIVE_TXT_DIR, ARCHIVE_PAGES_DIR]:
    os.makedirs(d, exist_ok=True)

# 核心白名單（必須保留在根目錄）
ROOT_WHITELIST = {
    "index.html",
    "portal.html",
    "chinese3_curriculum.html",
    "chinese6_curriculum.html",
    "chinese6_final.html",
    "chinese6_midterm.html",
    "chinese6_lesson1.html",
    "chinese6_lesson2.html",
    "chinese6_lesson3.html",
    "chinese6_lesson4.html",
    "chinese6_lesson5.html",
    "chinese6_lesson6.html",
    "chinese6_lesson7.html",
    "chinese6_lesson8.html",
    "chinese6_lesson9.html",
    "chinese6_lesson10.html",
    "chinese6_lesson11.html",
    "chinese6_lesson12.html",
    "math3_addition.html",
    "math3_geometry.html",
    "math3_measurement.html",
    "math3_multiplication.html",
    "math3_numbers.html",
    "prime.html",
    "fraction-division.html",
    "decimal-division.html",
    "circle-area.html",
    "social6_curriculum.html",
    "2mathgame.html",
    "5mathgame.html",
    "idiom_game.html",
    "element_game.html",
    "vocab_game.html",
    "chinese6_visual_engine.js",
    "chinese3_full_curriculum_database.json",
    "chinese6_full_curriculum_database.json",
    "social6_full_curriculum_database.json",
    "menu_cinnamoroll.png",
    "README.md",
    ".gitignore",
    ".git",
    ".venv",
    ".agents",
    "scripts",
    "archive",
    "organize_project_directory.py"
}

# 檔案分類移動規則
for item in os.listdir(BASE_DIR):
    if item in ROOT_WHITELIST or item.startswith("."):
        continue

    item_path = os.path.join(BASE_DIR, item)

    # 目錄處理
    if os.path.isdir(item_path):
        if item.startswith("extracted_pages"):
            target_path = os.path.join(ARCHIVE_PAGES_DIR, item)
            print(f"移動截圖資料夾: {item} -> archive/extracted_pages/")
            if os.path.exists(target_path):
                shutil.rmtree(target_path)
            shutil.move(item_path, target_path)
        continue

    # 檔案處理
    if item.endswith(".py") or item == "google_apps_script.js":
        target = os.path.join(SCRIPTS_DIR, item)
        print(f"移動工具腳本: {item} -> scripts/")
        shutil.move(item_path, target)
    elif item.endswith(".txt") or item == "chinese6_comprehensive_summary.md":
        target = os.path.join(ARCHIVE_TXT_DIR, item)
        print(f"移動文字記錄: {item} -> archive/temp_txt/")
        shutil.move(item_path, target)
    elif item.endswith(".json") and item not in ROOT_WHITELIST:
        target = os.path.join(ARCHIVE_OCR_DIR, item)
        print(f"移動中介JSON: {item} -> archive/ocr_raw/")
        shutil.move(item_path, target)

print("\n專案目錄整理完成！")
