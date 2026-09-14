import os
import json
import pymupdf
from rapidocr_onnxruntime import RapidOCR

def run():
    doc = pymupdf.open('114上-康軒國小-新挑戰-6上國語-自修.pdf')
    engine = RapidOCR()
    
    out_file = 'ocr_progress.json'
    data = {}
    if os.path.exists(out_file):
        try:
            with open(out_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except Exception:
            data = {}
            
    print(f"Starting page scanning. Current cached pages: {len(data)}")
    
    # Target P.1 to P.107 (index 0 to 106)
    for p_idx in range(107):
        p_str = str(p_idx + 1)
        if p_str in data:
            continue
        
        pix = doc[p_idx].get_pixmap(dpi=120)
        img_bytes = pix.tobytes("png")
        res, _ = engine(img_bytes)
        
        lines = [r[1] for r in res] if res else []
        data[p_str] = lines
        
        # Save every 5 pages
        if (p_idx + 1) % 5 == 0 or p_idx == 106:
            with open(out_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            print(f"Saved progress up to Page {p_idx + 1}")
            
    # Final save
    with open(out_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print("OCR scanning completed for P.1~107!")

if __name__ == '__main__':
    run()
