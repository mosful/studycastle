import fitz # PyMuPDF
import sys

doc = fitz.open("114上-南一國小-數學6上-作業簿-教用.pdf")
print("Total pages:", len(doc))

for i in range(min(26, len(doc))):
    page = doc[i]
    text = page.get_text().strip()
    print(f"--- Page {i+1} ---")
    if text:
        print(text[:200] + ("..." if len(text) > 200 else ""))
    else:
        print("[No text layer found / Image only]")
