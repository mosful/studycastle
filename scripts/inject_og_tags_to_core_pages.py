# -*- coding: utf-8 -*-
import os
import re
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

pages_meta = {
    "chinese3_curriculum.html": {
        "title": "115上 國小國語三上 互動學習城堡 (康軒第1~12課全冊練習簿與測驗卷) | 學習城堡",
        "desc": "115上最新康軒國語3上全冊自修！深度收錄全冊12課課文脈絡、生字成語辭典、字謎拆合、造句仿作與新挑戰測驗卷60題全真題庫解析！",
        "url": "chinese3_curriculum.html"
    },
    "chinese6_curriculum.html": {
        "title": "6上國語 全冊自修旗艦城堡 (康軒第1~12課全冊練習簿與期中期末大考) | 學習城堡",
        "desc": "國語六上全冊旗艦自修！涵蓋第1~12課課文深度賞析、字音字形辨析、高階成語詞彙、素養長文思維與全真測驗試題解析！",
        "url": "chinese6_curriculum.html"
    },
    "chinese6_midterm.html": {
        "title": "6上國語 期中自修學力考查 (康軒第1~6課期中複習全真試題) | 學習城堡",
        "desc": "國語六上期中自修考查！針對康軒版第1~6課課前預習、成語辭典、多音字形近字與全真模擬測驗解析！",
        "url": "chinese6_midterm.html"
    },
    "chinese6_final.html": {
        "title": "6上國語 期末學力大考 (新挑戰測驗卷第20~24回高鑑別度題庫) | 學習城堡",
        "desc": "國語六上期末學力大考！涵蓋新挑戰測驗卷第20~24回全真高鑑別度模擬試題、詳細步驟解題與錯題診斷！",
        "url": "chinese6_final.html"
    },
    "social6_curriculum.html": {
        "title": "6上社會 全冊自修學習城堡 (翰林第1~6單元全課綱精華題庫) | 學習城堡",
        "desc": "翰林版社會六上全冊自修城堡！深入涵蓋科技生活、投資理財、憲法與人權、地方創生及多元世界文化！",
        "url": "social6_curriculum.html"
    }
}

for page, meta in pages_meta.items():
    if not os.path.exists(page):
        continue
    with open(page, "r", encoding="utf-8") as f:
        content = f.read()
    
    if "og:title" in content:
        print(f"ℹ️ {page} 已具備 Open Graph 標籤，跳過。")
        continue
    
    og_block = f'''
    <!-- 社群分享 Open Graph & Twitter Cards 標籤 -->
    <meta property="og:type" content="article">
    <meta property="og:site_name" content="學習城堡 Study Castle">
    <meta property="og:url" content="https://mosful.github.io/studycastle/{meta['url']}">
    <meta property="og:title" content="{meta['title']}">
    <meta property="og:description" content="{meta['desc']}">
    <meta property="og:image" content="https://mosful.github.io/studycastle/favicon.svg">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{meta['title']}">
    <meta name="twitter:description" content="{meta['desc']}">
    <meta name="twitter:image" content="https://mosful.github.io/studycastle/favicon.svg">'''

    # 插入在 <title> 或 favicon 之後
    if "</title>" in content:
        content = content.replace("</title>", "</title>" + og_block, 1)
    else:
        content = content.replace("<head>", "<head>" + og_block, 1)
        
    with open(page, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"✅ 成功為 {page} 注入 Open Graph 標籤！")
