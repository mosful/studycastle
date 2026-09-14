import json
import sys

# 確保輸出為 utf-8
sys.stdout.reconfigure(encoding='utf-8')

data = json.load(open('chinese3_full_curriculum_database.json', encoding='utf-8'))
for item in data:
    print(f"{item.get('id')}: {item.get('title')}")
