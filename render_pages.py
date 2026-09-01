import pymupdf
import os

output_dir = "c:/Code/StudyCastle/extracted_pages"
os.makedirs(output_dir, exist_ok=True)

doc = pymupdf.open("114上-南一國小-數學6上-作業簿-教用.pdf")

for i in range(26):
    page = doc[i]
    # 2x zoom for high clarity
    pix = page.get_pixmap(dpi=150)
    output_path = os.path.join(output_dir, f"page_{i+1:02d}.png")
    pix.save(output_path)
    print(f"Saved {output_path} ({pix.width}x{pix.height})")
