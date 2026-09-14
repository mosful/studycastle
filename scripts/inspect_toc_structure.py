import os
import json
import pymupdf
from rapidocr_onnxruntime import RapidOCR

engine = RapidOCR()

def scan_toc_and_structure():
    files = [
        "115上 國小 康軒 新挑戰測驗卷 國語6上.pdf",
        "115上 國小 康軒 練習簿 國語6上_教用.pdf"
    ]
    
    result = {}
    for fpath in files:
        if not os.path.exists(fpath):
            print(f"File not found: {fpath}")
            continue
        doc = pymupdf.open(fpath)
        print(f"Scanning {fpath}, total pages: {len(doc)}")
        file_info = {"total_pages": len(doc), "pages": {}}
        # 掃描前 4 頁以取得目錄與前兩回
        for p in range(min(5, len(doc))):
            pix = doc[p].get_pixmap(dpi=150)
            res, _ = engine(pix.tobytes("png"))
            lines = [r[1] for r in res] if res else []
            file_info["pages"][p + 1] = lines
        result[fpath] = file_info
        
    with open("initial_scan_toc.json", "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    print("Completed initial scan to initial_scan_toc.json")

if __name__ == "__main__":
    scan_toc_and_structure()
