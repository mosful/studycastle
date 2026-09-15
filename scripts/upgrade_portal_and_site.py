# -*- coding: utf-8 -*-
import os
import re
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

print("=== 開始升級 scripts/generate_modern_portal.py 與全站首頁 ===")

with open("scripts/generate_modern_portal.py", "r", encoding="utf-8") as f:
    content = f.read()

# 1. 注入 Open Graph / Twitter Meta 標籤
og_meta_tags = '''    <!-- Favicon 網站圖示 -->
    <link rel="icon" type="image/svg+xml" href="favicon.svg">
    <link rel="alternate icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><rect width='100' height='100' rx='25' fill='%233B82F6'/><text x='50%' y='50%' dominant-baseline='central' text-anchor='middle' font-size='60'>🏰</text></svg>">
    <link rel="apple-touch-icon" href="favicon.svg">
    
    <!-- 社群分享 Open Graph & Twitter Cards 標籤 -->
    <meta property="og:type" content="website">
    <meta property="og:site_name" content="學習城堡 Study Castle">
    <meta property="og:url" content="https://mosful.github.io/studycastle/portal.html">
    <meta property="og:title" content="學習城堡 Study Castle | 國小自修、全冊題庫與互動學習樂園">
    <meta property="og:description" content="專為國小與國中學生打造的現代化互動式自修與學習樂園！全面收錄 115 上康軒國語三上/六上全冊自修、新超群數學、社會自修與新挑戰測驗卷題庫！">
    <meta property="og:image" content="https://mosful.github.io/studycastle/favicon.svg">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="學習城堡 Study Castle | 國小自修、全冊題庫與互動學習樂園">
    <meta name="twitter:description" content="專為國小與國中學生打造的現代化互動式自修與學習樂園！全面收錄 115 上康軒國語三上/六上全冊自修、新超群數學、社會自修與新挑戰測驗卷題庫！">
    <meta name="twitter:image" content="https://mosful.github.io/studycastle/favicon.svg">'''

if "<!-- 社群分享 Open Graph" not in content:
    content = re.sub(r'    <!-- Favicon 網站圖示 -->[\s\S]*?<link rel="apple-touch-icon" href="favicon.svg">', og_meta_tags, content, count=1)

# 2. 注入返回頂部按鈕樣式與快捷鍵標籤樣式，以及 .unit-card 連結樣式相容
extra_css = '''
        /* 語意化卡片與返回頂部增強樣式 */
        .unit-card {
            text-decoration: none;
            color: inherit;
        }
        .search-shortcut-hint {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            padding: 2px 7px;
            font-size: 0.72rem;
            font-weight: 700;
            color: var(--text-sub);
            background: var(--bg-base);
            border: 1px solid var(--card-border);
            border-radius: 6px;
            pointer-events: none;
            user-select: none;
            margin-right: 8px;
        }
        .back-to-top-btn {
            position: fixed;
            bottom: 28px;
            right: 28px;
            width: 48px;
            height: 48px;
            border-radius: 50%;
            background: linear-gradient(135deg, var(--primary), var(--secondary));
            color: #FFFFFF;
            border: none;
            box-shadow: 0 8px 20px rgba(59, 130, 246, 0.35);
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.2rem;
            font-weight: 900;
            opacity: 0;
            visibility: hidden;
            transform: translateY(20px) scale(0.9);
            transition: all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
            z-index: 999;
        }
        .back-to-top-btn.visible {
            opacity: 1;
            visibility: visible;
            transform: translateY(0) scale(1);
        }
        .back-to-top-btn:hover {
            transform: translateY(-4px) scale(1.08);
            box-shadow: 0 12px 28px rgba(59, 130, 246, 0.48);
        }
        .back-to-top-btn:active {
            transform: translateY(0) scale(0.96);
        }
'''

if ".back-to-top-btn" not in content:
    content = content.replace("    <style>", "    <style>" + extra_css)

# 3. 注入返回頂部按鈕 DOM
back_to_top_html = '''    <!-- 浮動平滑返回頂部按鈕 -->
    <button id="btnBackToTop" class="back-to-top-btn" onclick="scrollToTop()" title="返回頁面頂端" aria-label="返回頁面頂端">▲</button>
'''
if "id=\"btnBackToTop\"" not in content:
    content = content.replace("    <!-- 主要內容區塊 -->", back_to_top_html + "\n    <!-- 主要內容區塊 -->")

# 4. 在搜尋框加入快捷鍵提示標籤
if "search-shortcut-hint" not in content:
    content = content.replace(
        '<button class="search-clear-btn" id="searchClearBtn" onclick="clearSearch()" title="清除搜尋">✕</button>',
        '<span class="search-shortcut-hint" title="快捷鍵：按下 / 鍵聚焦搜尋">/</span>\n                        <button class="search-clear-btn" id="searchClearBtn" onclick="clearSearch()" title="清除搜尋">✕</button>'
    )

# 5. 替換 JavaScript 邏輯：SafeStorage 與語意化 a 標籤卡片
safe_storage_code = '''
        // 安全本地快顯存取器 (防禦無痕模式或 Storage 異常)
        const SafeStorage = {
            get(key, fallback = null) {
                try {
                    const val = localStorage.getItem(key);
                    return val !== null ? val : fallback;
                } catch (e) {
                    console.warn('[SafeStorage] 本地儲存讀取失敗，降級記憶體模式:', e);
                    return fallback;
                }
            },
            set(key, value) {
                try {
                    localStorage.setItem(key, value);
                } catch (e) {
                    console.warn('[SafeStorage] 本地儲存寫入失敗，降級記憶體模式:', e);
                }
            }
        };

        // 狀態管理
        let currentGrade = 'all';
        let currentSubject = 'all';
        let searchQuery = '';
        let currentSort = 'default';
        let showSubcards = false;
        let favorites = [];
        try {
            favorites = JSON.parse(SafeStorage.get('study_castle_favs', '[]'));
            if (!Array.isArray(favorites)) favorites = [];
        } catch(e) {
            favorites = [];
        }
'''

content = re.sub(
    r'        // 狀態管理[\s\S]*?let favorites = JSON\.parse\(localStorage\.getItem\(\'study_castle_favs\'\) \|\| \'\[\]\'\);',
    safe_storage_code.strip(),
    content
)

# 替換主題讀寫
content = content.replace(
    "const savedTheme = localStorage.getItem('study_castle_theme') || 'light';",
    "const savedTheme = SafeStorage.get('study_castle_theme', 'light');"
)
content = content.replace(
    "localStorage.setItem('study_castle_theme', next);",
    "SafeStorage.set('study_castle_theme', next);"
)
content = content.replace(
    "localStorage.setItem('study_castle_favs', JSON.stringify(favorites));",
    "SafeStorage.set('study_castle_favs', JSON.stringify(favorites));"
)

# 替換 renderCards 輸出為標準 <a> 標籤
old_card_tpl = """                return `
                    <div class="unit-card ${item.isFeatured ? 'is-featured' : ''}" onclick="navigateToUnit('${item.url}')">
                        <div class="card-header-banner" style="background: ${item.bgGradient};">
                            <span class="card-emoji-icon">${item.image}</span>
                            <span class="card-badge-pill" style="background: ${item.badgeColor};">${item.badgeText}</span>
                            <button class="card-fav-btn ${isFav ? 'is-fav' : ''}" onclick="toggleFavorite('${item.id}', event)" title="${isFav ? '取消收藏' : '加入收藏'}">
                                ${isFav ? '❤️' : '🤍'}
                            </button>
                        </div>
                        <div class="card-body">
                            <h3 class="card-title">${item.title}</h3>
                            <p class="card-desc">${item.description}</p>
                            <div class="card-tags">
                                ${item.tags.slice(0, 4).map(t => `
                                    <span class="card-tag" onclick="handleTagClick('${t}', event)">#${t}</span>
                                `).join('')}
                            </div>
                            <div class="card-action-bar">
                                <span class="card-grade-badge">${item.gradeText}</span>
                                <span class="card-enter-btn">立即進入 ➔</span>
                            </div>
                        </div>
                    </div>
                `;"""

new_card_tpl = """                return `
                    <a href="${item.url}" class="unit-card ${item.isFeatured ? 'is-featured' : ''}" title="進入 ${item.title}">
                        <div class="card-header-banner" style="background: ${item.bgGradient};">
                            <span class="card-emoji-icon">${item.image}</span>
                            <span class="card-badge-pill" style="background: ${item.badgeColor};">${item.badgeText}</span>
                            <button class="card-fav-btn ${isFav ? 'is-fav' : ''}" onclick="toggleFavorite('${item.id}', event)" title="${isFav ? '取消收藏' : '加入收藏'}" aria-label="${isFav ? '取消收藏' : '加入收藏'}">
                                ${isFav ? '❤️' : '🤍'}
                            </button>
                        </div>
                        <div class="card-body">
                            <h3 class="card-title">${item.title}</h3>
                            <p class="card-desc">${item.description}</p>
                            <div class="card-tags">
                                ${item.tags.slice(0, 4).map(t => `
                                    <span class="card-tag" onclick="handleTagClick('${t}', event)">#${t}</span>
                                `).join('')}
                            </div>
                            <div class="card-action-bar">
                                <span class="card-grade-badge">${item.gradeText}</span>
                                <span class="card-enter-btn">立即進入 ➔</span>
                            </div>
                        </div>
                    </a>
                `;"""

if old_card_tpl in content:
    content = content.replace(old_card_tpl, new_card_tpl)
else:
    # 嘗試較彈性的正則替換
    content = re.sub(
        r'<div class="unit-card \${item\.isFeatured \? \'is-featured\' : \'\'}" onclick="navigateToUnit\(\'\${item\.url}\'\)">',
        r'<a href="${item.url}" class="unit-card ${item.isFeatured ? \'is-featured\' : \'\'}" title="進入 ${item.title}">',
        content
    )
    content = re.sub(r'</div>\s*</div>\s*`;\s*}\)\.join\(\'\'\);', r'</div>\s*</a>\s*`;\s*}).join(\'\');', content)

# 6. 加入 toggleFavorite 與 handleTagClick 的防冒泡
content = content.replace(
    "function toggleFavorite(id, e) {\n            e.stopPropagation();",
    "function toggleFavorite(id, e) {\n            if (e) { e.preventDefault(); e.stopPropagation(); }"
)
content = content.replace(
    "function handleTagClick(tagName, e) {\n            e.stopPropagation();",
    "function handleTagClick(tagName, e) {\n            if (e) { e.preventDefault(); e.stopPropagation(); }"
)

# 7. 加入返回頂部與全域快捷鍵
enhancements_js = '''
        // 平滑返回頂部
        function scrollToTop() {
            window.scrollTo({ top: 0, behavior: 'smooth' });
        }

        window.addEventListener('scroll', () => {
            const btn = document.getElementById('btnBackToTop');
            if (btn) {
                if (window.scrollY > 320) {
                    btn.classList.add('visible');
                } else {
                    btn.classList.remove('visible');
                }
            }
        });

        // 全域鍵盤快捷鍵支援
        window.addEventListener('keydown', (e) => {
            // 按下 '/' 快速聚焦搜尋
            if (e.key === '/' && document.activeElement.tagName !== 'INPUT' && document.activeElement.tagName !== 'TEXTAREA') {
                e.preventDefault();
                const searchInput = document.getElementById('searchInput');
                if (searchInput) {
                    searchInput.focus();
                    searchInput.select();
                }
            }
            // 按下 'Escape' 清空搜尋
            if (e.key === 'Escape') {
                const searchInput = document.getElementById('searchInput');
                if (searchInput && document.activeElement === searchInput) {
                    clearSearch();
                    searchInput.blur();
                }
            }
        });
'''

if "scrollToTop()" not in content:
    content = content.replace("    </script>\n</body>", enhancements_js + "\n    </script>\n</body>")

with open("scripts/generate_modern_portal.py", "w", encoding="utf-8") as f:
    f.write(content)

print("✅ scripts/generate_modern_portal.py 升級完成！")
