import json

with open('chinese6_full_curriculum_database.json', 'r', encoding='utf-8') as f:
    full_db_json = f.read()

with open('chinese6_midterm.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

out = []
in_curriculum = False
skip_old_options = False

for line in lines:
    if 'const CURRICULUM = ' in line:
        out.append('// 課綱資料庫（全冊12課直接內嵌，支援任何離線環境）\n')
        out.append(f'const CURRICULUM = {full_db_json};\n')
        in_curriculum = True
    elif in_curriculum:
        if '// 測驗變數' in line:
            in_curriculum = False
            out.append(line)
    elif '全部課次 (第1~6課)' in line or '全部課次 (全冊第1~12課)' in line:
        out.append('                <option value="all">全部課次 (全冊第1~12課)</option>\n')
        out.append('                <option value="l1">第一課：跑道</option>\n')
        out.append('                <option value="l2">第二課：朱子治家格言選</option>\n')
        out.append('                <option value="l3">第三課：遇見更好的自己</option>\n')
        out.append('                <option value="l4">第四課：臺灣美食詩選</option>\n')
        out.append('                <option value="l5">第五課：下午茶風波</option>\n')
        out.append('                <option value="l6">第六課：珍珠奶茶</option>\n')
        out.append('                <option value="l7">第七課：大小剛好的鞋子</option>\n')
        out.append('                <option value="l8">第八課：狐假虎威</option>\n')
        out.append('                <option value="l9">第九課：空城計</option>\n')
        out.append('                <option value="l10">第十課：耶誕節</option>\n')
        out.append('                <option value="l11">第十一課：下午茶風波(安妮)</option>\n')
        out.append('                <option value="l12">第十二課：秘密花園</option>\n')
        skip_old_options = True
    elif skip_old_options:
        if '</select>' in line:
            skip_old_options = False
            out.append(line)
    elif '康軒 6上國語自修 (P.1~114)' in line:
        out.append(line.replace('(P.1~114)', '(全冊第1~12課)'))
    elif '完整涵蓋第一單元（第一~三課）與第二單元（第四~六課）' in line:
        out.append('        <p class="sub-title">完整涵蓋全學期四大單元（第一至十二課全部課次）<br>提供課前預習、課後複習、生字成語圖鑑、修辭解析與全真段考題庫闖關！</p>\n')
    else:
        out.append(line)

with open('chinese6_midterm.html', 'w', encoding='utf-8') as f:
    f.writelines(out)

print('[OK] Successfully upgraded chinese6_midterm.html to FULL 12 LESSONS!')
