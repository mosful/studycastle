# -*- coding: utf-8 -*-
import glob
import os
import re
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

html_files = sorted(glob.glob("*.html"))

print("=== 檢測 1: Web Audio API 的 user gesture 與 resume 處理 ===")
audio_files = []
for h in html_files:
    with open(h, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()
    if "AudioContext" in content or "webkitAudioContext" in content:
        has_resume = "resume" in content
        audio_files.append((h, has_resume))

print(f"共有 {len(audio_files)} 個頁面使用 Web Audio API:")
for h, has_resume in audio_files:
    status = "✅ 有處理 resume" if has_resume else "⚠️ 缺少 audioCtx.resume() 喚醒機制 (可能在部分瀏覽器靜音)"
    print(f"  - {h:30}: {status}")

print("\n=== 檢測 2: 檢查社群分享 Open Graph (og:) 標籤 ===")
missing_og = []
for h in ["index.html", "portal.html", "chinese3_curriculum.html", "chinese6_curriculum.html", "social6_curriculum.html"]:
    with open(h, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()
    has_og = "og:title" in content
    if not has_og:
        missing_og.append(h)

if missing_og:
    print(f"⚠️ 以下重要頁面缺少 Open Graph (og:title, og:description, og:image) 社群分享標籤:")
    for m in missing_og:
        print(f"  - {m}")
else:
    print("✅ 核心頁面均已具備 Open Graph 標籤。")

print("\n=== 檢測 3: 檢查 localStorage 容錯處理 (防止在無痕/隱私模式或 QuotaExceeded 拋錯崩潰) ===")
ls_risks = []
for h in html_files:
    with open(h, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()
    if "localStorage" in content:
        # 檢查是否有 try-catch 保護
        matches = re.findall(r'(localStorage\.[a-zA-Z]+)', content)
        has_try_catch = "try" in content and "catch" in content
        if not has_try_catch:
            ls_risks.append((h, len(matches)))

if ls_risks:
    print(f"⚠️ 發現 {len(ls_risks)} 個頁面使用 localStorage 但可能未封裝 try-catch 容錯:")
    for h, cnt in ls_risks[:10]:
        print(f"  - {h:30}: {cnt} 次呼叫")
else:
    print("✅ localStorage 調用皆有基礎錯誤處理。")
