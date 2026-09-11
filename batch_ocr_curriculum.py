import os
import json
import pymupdf
from rapidocr_onnxruntime import RapidOCR

engine = RapidOCR()

def extract_all_pages():
    targets = [
        ("quiz6", "115上 國小 康軒 新挑戰測驗卷 國語6上.pdf", 57),
        ("wb6", "115上 國小 康軒 練習簿 國語6上_教用.pdf", 42)
    ]
    
    out_file = "extracted_curriculum_raw.json"
    data = {}
    if os.path.exists(out_file):
        try:
            with open(out_file, "r", encoding="utf-8") as f:
                data = json.load(f)
        except Exception:
            data = {}

    for prefix, fpath, max_p in targets:
        if not os.path.exists(fpath):
            continue
        doc = pymupdf.open(fpath)
        print(f"Processing {prefix}: {fpath}, {len(doc)} pages")
        for p in range(min(max_p, len(doc))):
            key = f"{prefix}_p{p+1}"
            if key in data:
                continue
            pix = doc[p].get_pixmap(dpi=130)
            res, _ = engine(pix.tobytes("png"))
            lines = [r[1] for r in res] if res else []
            data[key] = lines
            if (p + 1) % 5 == 0:
                print(f"[{prefix}] Scanned page {p+1}/{len(doc)}")
                with open(out_file, "w", encoding="utf-8") as f:
                    json.dump(data, f, ensure_ascii=False, indent=2)

    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print("All pages OCR extracted successfully!")

if __name__ == "__main__":
    extract_all_pages()
