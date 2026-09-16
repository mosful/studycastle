# -*- coding: utf-8 -*-
import os
import re
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

print("=== 修復六年級數學作業簿 4 個檔案的選項隨機打亂 ===")

# 1. circle-area.html
with open("circle-area.html", "r", encoding="utf-8") as f:
    content = f.read()

# 替換 pi_table 的 opts
content = content.replace(
    "const opts = ['3.14', '3.15', '3.12', '3.16'];",
    "const opts = ['3.14', '3.15', '3.12', '3.16'].sort(() => Math.random() - 0.5);"
)

# 在 opts 定義後加入打亂
old_c_opts = """          opts = [
            ansStr,
            `${prefix}${(n * 2).toFixed(2).replace(/\\.00$/, '')}${unit}`,
            `${prefix}${(n + 10).toFixed(2).replace(/\\.00$/, '')}${unit}`,
            `${prefix}${Math.max(1, (n / 2)).toFixed(2).replace(/\\.00$/, '')}${unit}`
          ];"""

new_c_opts = """          opts = [
            ansStr,
            `${prefix}${(n * 2).toFixed(2).replace(/\\.00$/, '')}${unit}`,
            `${prefix}${(n + 10).toFixed(2).replace(/\\.00$/, '')}${unit}`,
            `${prefix}${Math.max(1, (n / 2)).toFixed(2).replace(/\\.00$/, '')}${unit}`
          ].sort(() => Math.random() - 0.5);"""

if old_c_opts in content:
    content = content.replace(old_c_opts, new_c_opts)
    print("✅ circle-area.html 主選項打亂成功")
else:
    # 彈性正則替換
    content = re.sub(
        r'(opts\s*=\s*\[\s*ansStr[\s\S]*?\];)',
        r'\1\n          opts.sort(() => Math.random() - 0.5);',
        content
    )
    print("✅ circle-area.html (正則) 主選項打亂成功")

with open("circle-area.html", "w", encoding="utf-8") as f:
    f.write(content)


# 2. decimal-division.html
with open("decimal-division.html", "r", encoding="utf-8") as f:
    d_content = f.read()

# 尋找 renderDecimalWbQuizBody
d_content = re.sub(
    r'(opts\s*=\s*\[\s*item\.ans[\s\S]*?\];)',
    r'\1\n          opts.sort(() => Math.random() - 0.5);',
    d_content
)
d_content = re.sub(
    r'(opts\s*=\s*\[\s*ansStr[\s\S]*?\];)',
    r'\1\n          opts.sort(() => Math.random() - 0.5);',
    d_content
)
# 檢查是否有 opts = ['>', '<', '=']
d_content = d_content.replace(
    "opts = ['>', '<', '='];",
    "opts = ['>', '<', '='].sort(() => Math.random() - 0.5);"
)
# 檢查 const opts = item.options || ...
d_content = re.sub(
    r'const\s+opts\s*=\s*(?:item\.options\s*\|\|\s*\[item\.ans[^\]]*\]);',
    r'const opts = [...(item.options || [item.ans])].sort(() => Math.random() - 0.5);',
    d_content
)

with open("decimal-division.html", "w", encoding="utf-8") as f:
    f.write(d_content)
print("✅ decimal-division.html 選項打亂成功")


# 3. fraction-division.html
with open("fraction-division.html", "r", encoding="utf-8") as f:
    frac_content = f.read()

frac_content = re.sub(
    r'(opts\s*=\s*\[\s*item\.ans[\s\S]*?\];)',
    r'\1\n          opts.sort(() => Math.random() - 0.5);',
    frac_content
)
frac_content = re.sub(
    r'const\s+opts\s*=\s*(?:item\.options\s*\|\|\s*\[item\.ans[^\]]*\]);',
    r'const opts = [...(item.options || [item.ans])].sort(() => Math.random() - 0.5);',
    frac_content
)

with open("fraction-division.html", "w", encoding="utf-8") as f:
    f.write(frac_content)
print("✅ fraction-division.html 選項打亂成功")


# 4. prime.html
with open("prime.html", "r", encoding="utf-8") as f:
    prime_content = f.read()

prime_content = re.sub(
    r'const\s+opts\s*=\s*item\.options\s*\|\|\s*\[item\.ans,\s*\'12\',\s*\'24\',\s*\'6\'\];',
    r'const opts = [...(item.options || [item.ans, \'12\', \'24\', \'6\'])].sort(() => Math.random() - 0.5);',
    prime_content
)
prime_content = re.sub(
    r'const\s+opts\s*=\s*item\.options\s*\|\|\s*\[item\.ans\];',
    r'const opts = [...(item.options || [item.ans])].sort(() => Math.random() - 0.5);',
    prime_content
)

with open("prime.html", "w", encoding="utf-8") as f:
    f.write(prime_content)
print("✅ prime.html 選項打亂成功")
