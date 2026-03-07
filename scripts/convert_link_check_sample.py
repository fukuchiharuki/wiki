#!/usr/bin/env python3
import argparse
import csv
import pathlib
import re
import shutil
import unicodedata
from typing import Dict, List


ROOT = pathlib.Path("/home/haruki/Workspace")
WIKI_DIR = ROOT / "www/html/wiki"
ATTACH_DIR = ROOT / "www/html/attach"
INVENTORY_CSV = ROOT / "pukiwiki_page_inventory.csv"
OUT_DIR = ROOT / "converted_link_check"

DEFAULT_PAGES = [
    "Git",
    "Git/GitHubでプルリクエストを作成する",
    "Git/GitHubと連携する",
]


def load_inventory() -> Dict[str, Dict[str, str]]:
    out = {}
    with INVENTORY_CSV.open(encoding="utf-8") as f:
        for row in csv.DictReader(f):
            out[row["page_name"]] = row
    return out


def source_path(page: str) -> pathlib.Path:
    return WIKI_DIR / (page.encode("utf-8").hex().upper() + ".txt")


def post_url_expr(converted_filename: str) -> str:
    # _posts/YYYY-MM-DD-ULID.md -> YYYY-MM-DD-ULID
    name = pathlib.Path(converted_filename).name
    stem = name[:-3] if name.endswith(".md") else name
    return "{% post_url " + stem + " %}"


def build_attach_key(page: str, ref_target: str) -> str:
    return page.encode("utf-8").hex().upper() + "_" + ref_target.encode("utf-8").hex().upper()


def resolve_attach(page: str, ref_target: str) -> pathlib.Path:
    candidates = []
    seen = set()
    for n in (ref_target, unicodedata.normalize("NFC", ref_target), unicodedata.normalize("NFD", ref_target)):
        if n in seen:
            continue
        seen.add(n)
        candidates.append(n)
    for c in candidates:
        p = ATTACH_DIR / build_attach_key(page, c)
        if p.exists():
            return p
    return pathlib.Path()


def image_line(page: str, ref_expr: str, image_dir: pathlib.Path) -> str:
    parts = [x.strip() for x in ref_expr.split(",")]
    target = parts[0] if parts else ""
    opts = parts[1:] if len(parts) > 1 else []

    if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*://", target):
        return "![{}]({})".format(target, target)

    src = resolve_attach(page, target)
    if not src or not src.exists():
        return "<!-- TODO: #ref({}) -->".format(ref_expr)

    image_dir.mkdir(parents=True, exist_ok=True)
    dest = image_dir / src.name
    if not dest.exists():
        shutil.copy2(src, dest)

    web_path = "/images/wiki/{}".format(src.name)
    # 幅指定などの見た目オプションは採用せず、画像記法は Markdown に統一する
    return "![{}]({})".format(target, web_path)


def ensure_blank_before(lines: List[str]) -> None:
    if lines and lines[-1] != "":
        lines.append("")


def ensure_blank_after(lines: List[str]) -> None:
    if not lines or lines[-1] != "":
        lines.append("")


def append_block_line(lines: List[str], line: str) -> None:
    # 画像行の前後に空行を置いて Markdown として見やすくする
    ensure_blank_before(lines)
    lines.append(line)
    ensure_blank_after(lines)


def squeeze_blank_lines(lines: List[str]) -> List[str]:
    out = []
    for line in lines:
        if line == "" and out and out[-1] == "":
            continue
        out.append(line)
    return out


def navi_lines(page: str, inventory: Dict[str, Dict[str, str]]) -> List[str]:
    prefix = page + "/"
    children = []
    for p in inventory:
        if not p.startswith(prefix):
            continue
        rest = p[len(prefix) :]
        if "/" in rest:
            continue
        children.append(p)
    children.sort()
    if not children:
        return ["<!-- TODO: #navi (no child pages found) -->"]
    out = []
    for child in children:
        out.append("- [{}]({})".format(child, post_url_expr(inventory[child]["converted_filename"])))
    return out


def convert_inline(text: str, inventory: Dict[str, Dict[str, str]]) -> str:
    text = re.sub(r"'''(.*?)'''", r"**\1**", text)
    text = re.sub(r"''(.*?)''", r"*\1*", text)
    if text.endswith("~"):
        text = text[:-1] + "<br>"

    def repl(m):
        inner = m.group(1)
        if ">" in inner:
            label, target = inner.split(">", 1)
            label = label.strip()
            target = target.strip()
        else:
            label = inner.strip()
            target = inner.strip()

        if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*://", target):
            return "[{}]({})".format(label, target)

        anchor = ""
        if "#" in target:
            target, anc = target.split("#", 1)
            anchor = "#" + anc
        target = target.strip()

        if target in inventory:
            expr = post_url_expr(inventory[target]["converted_filename"])
            return "[{}]({}{})".format(label, expr, anchor)
        return "[{}]({})".format(label, target + ".md")

    # ラベル内に ']' を含むケースがあるため、終端 ']]' まで非貪欲で拾う
    return re.sub(r"\[\[(.+?)\]\]", repl, text)


def convert_page(page: str, inventory: Dict[str, Dict[str, str]], image_dir: pathlib.Path) -> str:
    lines = source_path(page).read_text(encoding="utf-8", errors="replace").splitlines()
    out: List[str] = []
    in_code = False

    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.rstrip("\n")

        if re.match(r"^#author\(", stripped):
            i += 1
            continue

        m = re.match(r"^#ref\((.*)\)\s*$", stripped)
        if m:
            append_block_line(out, image_line(page, m.group(1), image_dir))
            i += 1
            continue

        m = re.match(r"^&ref\((.*)\);\s*$", stripped)
        if m:
            append_block_line(out, image_line(page, m.group(1), image_dir))
            i += 1
            continue

        if re.match(r"^#navi(?:\(\))?$", stripped):
            out.extend(navi_lines(page, inventory))
            i += 1
            continue

        if stripped.startswith((" ", "\t")):
            if not in_code:
                ensure_blank_before(out)
                out.append("```")
                in_code = True
            out.append(stripped[1:] if stripped else "")
            i += 1
            continue
        elif in_code:
            out.append("```")
            ensure_blank_after(out)
            in_code = False

        if re.match(r"^#\S", stripped):
            out.append("<!-- TODO: {} -->".format(stripped))
            i += 1
            continue
        if re.match(r"^&[A-Za-z0-9_]+\(.*\);$", stripped):
            out.append("<!-- TODO: {} -->".format(stripped))
            i += 1
            continue

        m = re.match(r"^(\*{1,3})\s*(.*?)\s*(\[#.*\])?\s*$", stripped)
        if m and m.group(2):
            level = len(m.group(1))
            title = re.sub(r"\s*\[#.*\]\s*$", "", m.group(2)).strip()
            out.append("#" * level + " " + convert_inline(title, inventory))
            i += 1
            continue

        m = re.match(r"^(-+)\s*(.*)$", stripped)
        if m:
            depth = len(m.group(1)) - 1
            out.append("  " * depth + "- " + convert_inline(m.group(2), inventory))
            i += 1
            continue

        m = re.match(r"^(\++)\s*(.*)$", stripped)
        if m:
            depth = len(m.group(1)) - 1
            out.append("  " * depth + "1. " + convert_inline(m.group(2), inventory))
            i += 1
            continue

        out.append(convert_inline(stripped, inventory))
        i += 1

    if in_code:
        out.append("```")
        ensure_blank_after(out)
    out = squeeze_blank_lines(out)

    # サブページでもディレクトリ情報が分かるようページ名をそのまま title に使う
    title = page
    date = inventory[page]["created_at"]
    last_modified_at = inventory[page]["updated_at"]
    doc = [
        "---",
        'title: "{}"'.format(title),
        "date: {}".format(date),
        "last_modified_at: {}".format(last_modified_at),
        "---",
        "",
    ] + out
    return "\n".join(doc).rstrip() + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out-dir", default=str(OUT_DIR))
    parser.add_argument("--page", action="append", dest="pages")
    parser.add_argument("--image-dir", default="")
    parser.add_argument("--include-builtin", action="store_true")
    parser.add_argument("--all", action="store_true")
    args = parser.parse_args()

    inventory = load_inventory()
    out_dir = pathlib.Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    if args.pages:
        pages = args.pages
    elif args.all:
        pages = sorted(inventory.keys())
    else:
        pages = DEFAULT_PAGES
    if args.image_dir:
        image_dir = pathlib.Path(args.image_dir)
    else:
        site_root = out_dir.parent if out_dir.name == "_posts" else out_dir
        image_dir = site_root / "images" / "wiki"

    converted = 0
    skipped_builtin = 0
    for page in pages:
        if not args.include_builtin and inventory[page].get("convert_target") == "false":
            print("skip builtin page: {}".format(page))
            skipped_builtin += 1
            continue
        converted_filename = inventory[page]["converted_filename"]
        rel = converted_filename
        if out_dir.name == "_posts" and rel.startswith("_posts/"):
            rel = rel[len("_posts/") :]
        dest = out_dir / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(convert_page(page, inventory, image_dir), encoding="utf-8")
        print("{} -> {}".format(page, converted_filename))
        converted += 1
    print("summary: converted={} skipped_builtin={}".format(converted, skipped_builtin))


if __name__ == "__main__":
    main()
