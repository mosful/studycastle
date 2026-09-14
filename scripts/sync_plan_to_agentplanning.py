import os

plan_file = r"C:\Code\AgentPlanning\StudyCastle\implementation_plan\homepage_and_directory_cleanup.md"
os.makedirs(os.path.dirname(plan_file), exist_ok=True)

with open(r"C:\Users\MossLin林建良\.gemini\antigravity-ide\brain\9144a205-1117-488a-839a-5ed29ba2a797\implementation_plan.md", "r", encoding="utf-8") as src:
    content = src.read()

with open(plan_file, "w", encoding="utf-8") as dst:
    dst.write(content)

print("已同步留存 implementation_plan 到 AgentPlanning 目錄！")
