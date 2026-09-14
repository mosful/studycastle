import os

target_file = r"C:\Code\AgentPlanning\StudyCastle\walkthrough\homepage_and_directory_cleanup.md"
os.makedirs(os.path.dirname(target_file), exist_ok=True)

with open(r"C:\Users\MossLin林建良\.gemini\antigravity-ide\brain\9144a205-1117-488a-839a-5ed29ba2a797\walkthrough.md", "r", encoding="utf-8") as src:
    content = src.read()

with open(target_file, "w", encoding="utf-8") as dst:
    dst.write(content)

print("成功同步留存 walkthrough 到 AgentPlanning 目錄！")
