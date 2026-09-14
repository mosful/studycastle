import json

def update_curriculum_html():
    with open('chinese6_full_curriculum_database.json', 'r', encoding='utf-8') as f:
        db = json.load(f)

    with open('chinese6_curriculum.html', 'r', encoding='utf-8') as f:
        html = f.read()

    inline_str = f"const INLINE_CURRICULUM = {json.dumps(db, ensure_ascii=False)};"

    target = "curriculumData = await response.json();"
    replacement = """curriculumData = await response.json();
            } catch (err) {
                console.warn("使用內嵌備援資料庫:", err);
                curriculumData = INLINE_CURRICULUM;
            }"""

    # 在 script 開頭注入 INLINE_CURRICULUM
    script_tag = "<script>"
    script_replacement = f"<script>\n        {inline_str}\n"

    if script_tag in html and target in html:
        html = html.replace(script_tag, script_replacement, 1)
        # 替換 catch 錯誤邏輯
        old_catch = """            } catch (err) {
                console.error("載入課程資料失敗:", err);
                document.getElementById('displayLessonTitle').textContent = "載入失敗，請確認資料庫檔案存在。";
            }"""
        new_catch = """            } catch (err) {
                console.warn("fetch 失敗（可能在 file:// 協議下），改用內嵌課程資料庫:", err);
                curriculumData = INLINE_CURRICULUM;
            }"""
        html = html.replace(old_catch, new_catch, 1)
        with open('chinese6_curriculum.html', 'w', encoding='utf-8') as f:
            f.write(html)
        print("Updated chinese6_curriculum.html with INLINE_CURRICULUM successfully!")
    else:
        print("Target tags not found.")

if __name__ == "__main__":
    update_curriculum_html()
