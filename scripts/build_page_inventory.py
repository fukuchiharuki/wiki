#!/usr/bin/env python3
import csv
import datetime as dt
import hashlib
import pathlib
import re
from typing import Optional


ROOT = pathlib.Path(__file__).resolve().parent.parent
WIKI_DIR = ROOT / "www/html/wiki"
OUT_CSV = ROOT / "pukiwiki_page_inventory.csv"
BUILTIN_PAGES = ROOT / "pukiwiki_builtin_pages.txt"
JST = dt.timezone(dt.timedelta(hours=9), name="JST")
AUTHOR_RE = re.compile(r'^#author\("([^"]*)"')
ULID_ALPHABET = "0123456789ABCDEFGHJKMNPQRSTVWXYZ"


def parse_iso8601(s: str) -> Optional[dt.datetime]:
    s = s.strip()
    if not s:
        return None
    # Python 3.6 互換のため手動でパースする
    patterns = [
        "%Y-%m-%dT%H:%M:%S%z",
        "%Y-%m-%d %H:%M:%S%z",
        "%Y-%m-%dT%H:%M:%S",
        "%Y-%m-%d %H:%M:%S",
    ]
    cands = [s]
    if re.search(r"[+-]\d\d:\d\d$", s):
        cands.append(s[:-3] + s[-2:])  # +09:00 -> +0900

    for cand in cands:
        for p in patterns:
            try:
                d = dt.datetime.strptime(cand, p)
                if d.tzinfo is None:
                    d = d.replace(tzinfo=dt.timezone.utc)
                return d
            except ValueError:
                pass
    return None


def encode_crockford(data: bytes) -> str:
    value = int.from_bytes(data, "big")
    chars = []
    for _ in range(26):
        chars.append(ULID_ALPHABET[value & 0x1F])
        value >>= 5
    return "".join(reversed(chars))


def ulid_from(created: dt.datetime, page_name: str) -> str:
    if created.tzinfo is None:
        created = created.replace(tzinfo=JST)
    ts_ms = int(created.timestamp() * 1000)
    ts_bytes = ts_ms.to_bytes(6, "big", signed=False)
    entropy = hashlib.sha1((page_name + "|" + created.isoformat()).encode("utf-8")).digest()[:10]
    return encode_crockford(ts_bytes + entropy)


def main() -> None:
    builtin_pages = set()
    if BUILTIN_PAGES.exists():
        for line in BUILTIN_PAGES.read_text(encoding="utf-8").splitlines():
            s = line.strip()
            if not s or s.startswith("#"):
                continue
            builtin_pages.add(s)

    pages = []
    for src in sorted(WIKI_DIR.glob("*.txt")):
        stem = src.stem
        if not re.match(r"^[0-9A-Fa-f]+$", stem):
            continue
        try:
            page = bytes.fromhex(stem).decode("utf-8")
        except (ValueError, UnicodeDecodeError):
            continue
        pages.append(page)
    rows = []

    for page in pages:
        src = WIKI_DIR / (page.encode("utf-8").hex().upper() + ".txt")
        lines = src.read_text(encoding="utf-8", errors="replace").splitlines()
        first = lines[0] if lines else ""
        m = AUTHOR_RE.match(first)

        created = None
        updated = None
        created_source = ""
        updated_source = ""

        if m:
            raw = m.group(1)
            parts = raw.split(";")
            if len(parts) >= 2:
                # PukiWiki #author の先頭を更新日時、2番目を作成日時として扱う
                updated = parse_iso8601(parts[0])
                created = parse_iso8601(parts[1])
                updated_source = "#author"
                created_source = "#author"
            else:
                d = parse_iso8601(parts[0])
                if d is not None:
                    created = d
                    updated = d
                    created_source = "#author(single)"
                    updated_source = "#author(single)"

        if created is None or updated is None:
            mtime = dt.datetime.fromtimestamp(src.stat().st_mtime, tz=dt.timezone.utc)
            if created is None:
                created = mtime
                created_source = "file_mtime_utc"
            if updated is None:
                updated = mtime
                updated_source = "file_mtime_utc"

        created_jst = created.astimezone(JST)
        updated_jst = updated.astimezone(JST)

        ulid = ulid_from(created_jst, page)
        ymd = created_jst.date().isoformat()
        converted_filename = f"_posts/{ymd}-{ulid}.md"
        is_builtin = page in builtin_pages
        convert_target = (not is_builtin) and (not page.startswith(":"))

        rows.append(
            {
                "page_name": page,
                "created_at": created_jst.isoformat(),
                "updated_at": updated_jst.isoformat(),
                "converted_filename": converted_filename,
                "is_builtin": "true" if is_builtin else "false",
                "convert_target": "true" if convert_target else "false",
                "created_source": created_source,
                "updated_source": updated_source,
            }
        )

    rows.sort(key=lambda x: x["page_name"])

    with OUT_CSV.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "page_name",
                "created_at",
                "updated_at",
                "converted_filename",
                "is_builtin",
                "convert_target",
                "created_source",
                "updated_source",
            ],
        )
        writer.writeheader()
        writer.writerows(rows)

    print(f"wrote {len(rows)} rows to {OUT_CSV}")
    print("sample:")
    for row in rows[:10]:
        print(
            "\t".join(
                [
                    row["page_name"],
                    row["created_at"],
                    row["updated_at"],
                    row["converted_filename"],
                ]
            )
        )


if __name__ == "__main__":
    main()
