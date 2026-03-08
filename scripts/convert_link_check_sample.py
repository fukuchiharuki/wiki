#!/usr/bin/env python3
import argparse
import csv
import pathlib
import re
import shutil
import unicodedata
from typing import Dict, List, Tuple


ROOT = pathlib.Path(__file__).resolve().parent.parent
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
    return "{{ site.baseurl }}{% post_url " + stem + " %}"


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

    # str.format() で Liquid の中括弧が崩れないように二重でエスケープする
    web_path = "{{{{ '/images/wiki/{}' | relative_url }}}}".format(src.name)
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


def open_code_block(lines: List[str]) -> None:
    ensure_blank_before(lines)
    lines.append("{% raw %}")
    lines.append("```")


def close_code_block(lines: List[str]) -> None:
    lines.append("```")
    lines.append("{% endraw %}")
    ensure_blank_after(lines)


def squeeze_blank_lines(lines: List[str]) -> List[str]:
    out = []
    for line in lines:
        if line == "" and out and out[-1] == "":
            continue
        out.append(line)
    return out


def is_list_line(line: str) -> bool:
    return bool(re.match(r"^\s*(?:- |\d+\. )", line))


def normalize_list_spacing(lines: List[str]) -> List[str]:
    out: List[str] = []
    n = len(lines)

    for i, line in enumerate(lines):
        if line and is_list_line(line):
            if out and out[-1] != "" and not is_list_line(out[-1]):
                out.append("")
            out.append(line)
            next_line = lines[i + 1] if i + 1 < n else ""
            if next_line != "" and not is_list_line(next_line):
                out.append("")
            continue

        out.append(line)

    return squeeze_blank_lines(out)


def parse_table_row(line: str) -> Tuple[List[str], bool]:
    stripped = line.strip()
    if not stripped:
        return [], False

    # PukiWiki table: |col1|col2|
    if stripped.startswith("|"):
        core = stripped[1:]
        if core.endswith("|"):
            core = core[:-1]
        cells = [c.strip() for c in core.split("|")]
        is_header = False
        if cells and cells[-1].lower() == "h":
            is_header = True
            cells = cells[:-1]
        return cells, is_header

    return [], False


def table_lines(
    table_rows: List[Tuple[List[str], bool]], inventory: Dict[str, Dict[str, str]], current_page: str = ""
) -> List[str]:
    if not table_rows:
        return []

    rows_only = [r for r, _ in table_rows]
    cols = max(len(r) for r in rows_only)

    def normalize_row(row: List[str]) -> List[str]:
        return row + [""] * (cols - len(row))

    normalized_rows = []
    for row in rows_only:
        normalized = normalize_row(row)
        cleaned = [c[1:].strip() if c.startswith("~") else c for c in normalized]
        normalized_rows.append(cleaned)

    header_index = next((idx for idx, (_, is_header) in enumerate(table_rows) if is_header), -1)
    if header_index >= 0:
        header = normalized_rows[header_index]
        body = [row for idx, row in enumerate(normalized_rows) if idx != header_index]
    else:
        header = [""] * cols
        body = normalized_rows

    out = []
    out.append("| " + " | ".join(convert_inline(c, inventory, current_page) for c in header) + " |")
    out.append("| " + " | ".join(["---"] * cols) + " |")
    for row in body:
        out.append("| " + " | ".join(convert_inline(c, inventory, current_page) for c in row) + " |")
    return out


def parse_definition_row(line: str) -> Tuple[str, str]:
    stripped = line.strip()
    if not stripped.startswith(":") or "|" not in stripped:
        return "", ""
    term, desc = stripped[1:].split("|", 1)
    return term.strip(), desc.strip()


def convert_definition_desc(desc: str, inventory: Dict[str, Dict[str, str]], current_page: str = "") -> str:
    if not desc:
        return ""
    parts = desc.split("\n")
    converted = []
    for idx, part in enumerate(parts):
        line = convert_inline(part, inventory, current_page)
        # 複数行説明は改行が潰れないように明示的に繋ぐ
        if idx < len(parts) - 1 and line and not line.endswith("<br>"):
            line += "<br>"
        converted.append(line)
    return "".join(converted)


def definition_lines(rows: List[Tuple[str, str]], inventory: Dict[str, Dict[str, str]], current_page: str = "") -> List[str]:
    out = ["<dl>"]
    for term, desc in rows:
        out.append("<dt>{}</dt>".format(convert_inline(term, inventory, current_page)))
        out.append("<dd>{}</dd>".format(convert_definition_desc(desc, inventory, current_page)))
    out.append("</dl>")
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


def convert_inline(text: str, inventory: Dict[str, Dict[str, str]], current_page: str = "") -> str:
    text = re.sub(r"'''(.*?)'''", r"**\1**", text)
    text = re.sub(r"''(.*?)''", r"*\1*", text)
    # PukiWiki line break plugin
    text = re.sub(r"&br\(\);?|&br;|&br(?=[^A-Za-z0-9_]|$)", "<br>", text, flags=re.IGNORECASE)
    if text.endswith("~"):
        text = text[:-1] + "<br>"

    def repl(m):
        inner = m.group(1)
        if ">" in inner:
            # 末尾の '>' を区切りとして扱う。
            # `[[>label>https://...]]` のように先頭に '>' がある記法もあるため。
            label, target = inner.rsplit(">", 1)
            label = label.strip()
            target = target.strip()
            if label.startswith(">"):
                label = label[1:].strip()
            if not label:
                label = target
        else:
            s = inner.strip()
            # `[[label:https://example.com]]` のような記法に対応する
            mm = re.match(r"^(.*?)([a-zA-Z][a-zA-Z0-9+.-]*://.+)$", s)
            if mm:
                label = re.sub(r"[:\s]+$", "", mm.group(1)).strip()
                target = mm.group(2).strip()
                if not label:
                    label = target
            else:
                label = s
                target = s

        label = label.replace("&nbsp;", " ")
        # kramdown で表セル区切りと誤解釈されるのを避ける
        label = label.replace("|", r"\|")

        if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*://", target):
            return "[{}]({})".format(label, target)

        anchor = ""
        if "#" in target:
            target, anc = target.split("#", 1)
            anchor = "#" + anc
        target = target.strip()

        resolved_target = target
        if target not in inventory and current_page and "/" in current_page:
            parent = current_page.rsplit("/", 1)[0]
            # `[[SubPage]]` を同一ディレクトリ配下の相対指定として補完する
            if "/" not in target:
                candidate = parent + "/" + target
                if candidate in inventory:
                    resolved_target = candidate
            # PukiWiki の `[[../SubPage]]` / `[[./SubPage]]` を sibling 指定として補完する
            elif target.startswith("../"):
                candidate = parent + "/" + target[3:]
                if candidate in inventory:
                    resolved_target = candidate
            elif target.startswith("./"):
                candidate = parent + "/" + target[2:]
                if candidate in inventory:
                    resolved_target = candidate

        if resolved_target in inventory:
            expr = post_url_expr(inventory[resolved_target]["converted_filename"])
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

        # Preformatted blocks must be preserved as code fences before other line-level conversions.
        if stripped.startswith((" ", "\t")):
            if not in_code:
                open_code_block(out)
                in_code = True
            out.append(stripped[1:] if stripped else "")
            i += 1
            continue
        elif in_code:
            close_code_block(out)
            in_code = False

        def_term, def_desc = parse_definition_row(stripped)
        if def_term:
            rows: List[Tuple[str, str]] = []
            j = i + 1
            desc_lines = [def_desc] if def_desc else []
            while j < len(lines):
                next_line = lines[j].rstrip("\n")
                next_term, next_desc = parse_definition_row(next_line)
                if next_term:
                    rows.append((def_term, "\n".join(desc_lines)))
                    def_term, def_desc = next_term, next_desc
                    desc_lines = [def_desc] if def_desc else []
                    j += 1
                    continue
                if next_line.strip() == "":
                    break
                if next_line.startswith((" ", "\t")):
                    break
                if parse_table_row(next_line)[0]:
                    break
                if re.match(r"^#\S", next_line):
                    break
                if re.match(r"^&[A-Za-z0-9_]+\(.*\);$", next_line):
                    break
                heading = re.match(r"^(\*{1,3})\s*(.*?)\s*(\[#.*\])?\s*$", next_line)
                if heading and heading.group(2):
                    break
                if re.match(r"^(-+)\s*(.*)$", next_line):
                    break
                if re.match(r"^(\++)\s*(.*)$", next_line):
                    break
                desc_lines.append(next_line.strip())
                j += 1
            rows.append((def_term, "\n".join(desc_lines)))
            ensure_blank_before(out)
            out.extend(definition_lines(rows, inventory, page))
            ensure_blank_after(out)
            i = j
            continue

        row, is_header = parse_table_row(stripped)
        if row:
            rows = [(row, is_header)]
            j = i + 1
            while j < len(lines):
                next_row, next_is_header = parse_table_row(lines[j].rstrip("\n"))
                if not next_row:
                    break
                rows.append((next_row, next_is_header))
                j += 1
            ensure_blank_before(out)
            out.extend(table_lines(rows, inventory, page))
            ensure_blank_after(out)
            i = j
            continue

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
            out.append("#" * level + " " + convert_inline(title, inventory, page))
            i += 1
            continue

        m = re.match(r"^(-+)\s*(.*)$", stripped)
        if m:
            depth = len(m.group(1)) - 1
            body = convert_inline(m.group(2), inventory, page).strip()
            if body:
                out.append("  " * depth + "- " + body)
            i += 1
            continue

        m = re.match(r"^(\++)\s*(.*)$", stripped)
        if m:
            depth = len(m.group(1)) - 1
            body = convert_inline(m.group(2), inventory, page).strip()
            if body:
                out.append("  " * depth + "1. " + body)
            i += 1
            continue

        out.append(convert_inline(stripped, inventory, page))
        i += 1

    if in_code:
        close_code_block(out)
    out = normalize_list_spacing(out)

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
