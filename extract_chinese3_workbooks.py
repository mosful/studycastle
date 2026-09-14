"""
提取國語3上練習簿和測驗卷的 PDF 頁面為圖片
"""
import pymupdf
import os

def extract_pages(pdf_path, output_dir, prefix):
    """提取所有頁面為 PNG 圖片"""
    os.makedirs(output_dir, exist_ok=True)
    doc = pymupdf.open(pdf_path)
    total = len(doc)
    print(f"[{prefix}] 共 {total} 頁")
    
    for i in range(total):
        page = doc[i]
        # 使用較高 DPI 以確保文字清晰
        pix = page.get_pixmap(dpi=200)
        out_path = os.path.join(output_dir, f"{prefix}_page_{i+1:03d}.png")
        pix.save(out_path)
        if (i+1) % 10 == 0 or i == 0 or i == total - 1:
            print(f"  已提取第 {i+1}/{total} 頁")
    
    doc.close()
    print(f"[{prefix}] 完成！圖片存放在 {output_dir}")

if __name__ == "__main__":
    # 練習簿
    extract_pages(
        r"c:\Code\StudyCastle\115上 國小 康軒 練習簿 國語3上_教用.pdf",
        r"c:\Code\StudyCastle\extracted_pages_chinese3_workbook",
        "wb"
    )
    
    # 測驗卷
    extract_pages(
        r"c:\Code\StudyCastle\115上 國小 康軒 新挑戰測驗卷 國語3上.pdf",
        r"c:\Code\StudyCastle\extracted_pages_chinese3_quiz",
        "quiz"
    )
