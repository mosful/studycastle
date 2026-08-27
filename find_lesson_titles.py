import pymupdf
from rapidocr_onnxruntime import RapidOCR

def find_titles():
    doc = pymupdf.open('114上-康軒國小-新挑戰-6上國語-自修.pdf')
    engine = RapidOCR()
    
    with open('extracted_titles.txt', 'w', encoding='utf-8') as out:
        for p_idx in range(107):
            pix = doc[p_idx].get_pixmap(dpi=100)
            res, _ = engine(pix.tobytes("png"))
            lines = [r[1] for r in res] if res else []
            full_text = "".join(lines)
            
            # Print page number if any key indicators match
            if any(k in full_text for k in ["第一課", "第二課", "第三課", "第四課", "第五課", "第六課", "課文探測器", "第一次", "期中"]):
                out.write(f"=== Page {p_idx + 1} ===\n")
                for line in lines[:10]:
                    out.write(line + "\n")
                out.write("\n")
    print("Done finding titles!")

if __name__ == "__main__":
    find_titles()
