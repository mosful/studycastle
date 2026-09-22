"""將共用的平板／兒童友善介面資源套用到所有靜態頁面。"""

from pathlib import Path
import re


ROOT = Path(__file__).resolve().parent.parent
UI_MARKER = '<link rel="stylesheet" href="study-castle-ui.css">'
SCRIPT_MARKER = '<script src="study-castle-ui.js" defer></script>'


def expand_transition(match: re.Match[str]) -> str:
    timing = match.group(1).strip()
    properties = (
        "color",
        "background-color",
        "border-color",
        "box-shadow",
        "transform",
        "opacity",
        "visibility",
    )
    return "transition: " + ", ".join(
        f"{property_name} {timing}" for property_name in properties
    ) + ";"


def update_html(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    original = text

    text = re.sub(
        r'<meta\s+name=["\']viewport["\']\s+content=["\'][^"\']*["\']\s*/?>',
        '<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">',
        text,
        count=1,
        flags=re.IGNORECASE,
    )
    if not re.search(r'<meta\s+name=["\']viewport["\']', text, re.IGNORECASE):
        text = text.replace(
            "<head>",
            '<head>\n    <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">',
            1,
        )

    if not re.search(r'<meta\s+name=["\']theme-color["\']', text, re.IGNORECASE):
        text = text.replace(
            "</head>",
            '    <meta name="theme-color" content="#F5F7FC">\n</head>',
            1,
        )

    if UI_MARKER not in text:
        text = text.replace(
            "</head>",
            f"    {UI_MARKER}\n    {SCRIPT_MARKER}\n</head>",
            1,
        )

    if "fonts.googleapis.com" in text and 'rel="preconnect" href="https://fonts.googleapis.com"' not in text:
        text = text.replace(
            '<link href="https://fonts.googleapis.com',
            '<link rel="preconnect" href="https://fonts.googleapis.com">\n'
            '    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
            '    <link href="https://fonts.googleapis.com',
            1,
        )

    text = re.sub(
        r"transition:\s*all\s+([^;]+);",
        expand_transition,
        text,
        flags=re.IGNORECASE,
    )
    text = re.sub(
        r"outline:\s*none\s*;",
        "outline: 2px solid transparent;",
        text,
        flags=re.IGNORECASE,
    )

    text = re.sub(
        r'<span class="tag-chip" onclick="([^"]+)">([^<]+)</span>',
        r'<button type="button" class="tag-chip" onclick="\1">\2</button>',
        text,
    )
    text = re.sub(
        r'<span class="card-tag" onclick="([^"]+)">([^<]+)</span>',
        r'<button type="button" class="card-tag" onclick="\1">\2</button>',
        text,
    )

    text = re.sub(
        r'<img\s+([^>]*class=["\'][^"\']*character-img[^"\']*["\'][^>]*)>',
        lambda match: _add_image_dimensions(match.group(0)),
        text,
        flags=re.IGNORECASE,
    )

    if text == original:
        return False
    path.write_text(text, encoding="utf-8", newline="\n")
    return True


def _add_image_dimensions(tag: str) -> str:
    if not re.search(r"\bwidth=", tag, re.IGNORECASE):
        tag = tag[:-1] + ' width="150">'
    if not re.search(r"\bheight=", tag, re.IGNORECASE):
        tag = tag[:-1] + ' height="150">'
    return tag


def main() -> None:
    updated = []
    for path in sorted(ROOT.glob("*.html")):
        if update_html(path):
            updated.append(path.name)
    print(f"已更新 {len(updated)} 個頁面")
    for name in updated:
        print(f"- {name}")


if __name__ == "__main__":
    main()
