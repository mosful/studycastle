"""驗證全站共用 UI、平板適配與基礎無障礙設定。"""

from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parent.parent
REQUIRED_MARKERS = (
    '<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">',
    '<meta name="theme-color" content="#F5F7FC">',
    '<link rel="stylesheet" href="study-castle-ui.css">',
    '<script src="study-castle-ui.js" defer></script>',
)


def main() -> int:
    failures = []
    html_paths = sorted(ROOT.glob("*.html"))

    for path in html_paths:
        text = path.read_text(encoding="utf-8")
        for marker in REQUIRED_MARKERS:
            if marker not in text:
                failures.append(f"{path.name}: 缺少 {marker}")
        if re.search(r"maximum-scale|user-scalable", text, re.IGNORECASE):
            failures.append(f"{path.name}: 不應禁止使用者縮放")
        if re.search(r"transition:\s*all", text, re.IGNORECASE):
            failures.append(f"{path.name}: transition 應列出實際屬性")
        if re.search(r"outline:\s*none", text, re.IGNORECASE):
            failures.append(f"{path.name}: 不應移除焦點外框")

        for image in re.findall(r"<img\b[^>]*>", text, re.IGNORECASE):
            if not re.search(r"\balt=", image, re.IGNORECASE):
                failures.append(f"{path.name}: 圖片缺少 alt")
            if not re.search(r"\bwidth=", image, re.IGNORECASE):
                failures.append(f"{path.name}: 圖片缺少 width")
            if not re.search(r"\bheight=", image, re.IGNORECASE):
                failures.append(f"{path.name}: 圖片缺少 height")

    if (ROOT / "index.html").read_bytes() != (ROOT / "portal.html").read_bytes():
        failures.append("index.html 與 portal.html 必須保持同步")

    if failures:
        print("全站 UI 驗證失敗：")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print(f"全站 UI 驗證通過：{len(html_paths)} 個頁面皆已套用共用介面與縮放支援。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
