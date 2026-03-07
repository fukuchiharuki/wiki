# PukiWiki → Jekyll Markdown Conversion

## Goal
This project converts an entire local PukiWiki content directory
into Markdown files compatible with Jekyll.

The primary goal is **structural correctness and semantic fidelity**,
not perfect visual reproduction.

## Jekyll Runtime Environment (jekyll-now base)
- This repository root is the Jekyll site home
- Converted pages should be generated into `_posts/`
- Converted wiki images should be placed into `images/wiki/`
- Local setup script:
  - `./scripts/setup_jekyll_env.sh`
- Local preview:
  - `cd .`
  - `bundle exec jekyll serve --livereload`

## Scope
- Input: Local PukiWiki pages written in PukiWiki markup
- Output: Markdown files suitable for Jekyll
- One Markdown file per PukiWiki page
- Built-in PukiWiki pages are excluded from conversion targets
- Pages whose names start with `:` are excluded from conversion targets

## High-Level Rules
- Do NOT invent content
- Do NOT silently drop content
- When conversion is ambiguous, preserve the original meaning over formatting
- If a construct cannot be converted cleanly, leave a TODO comment

## Output Format (Jekyll)
Each output file must:
- Be valid Markdown
- Be renderable by Jekyll
- Include YAML Front Matter at the top
- Include `date` (page created date, JST)
- Include `last_modified_at` (page updated date, JST)

Example:

---
title: "Page Title"
---

## Heading
Content here

## Page Mapping
- PukiWiki page name → Markdown filename
- Use URL-safe, lowercase filenames where reasonable
- Preserve hierarchy if directory-like structure exists
- For this repository, the output filename must follow `pukiwiki_page_inventory.csv` column `converted_filename`
- The date part in `converted_filename` (`YEAR-MONTH-DAY`) must be JST-based

## PukiWiki Syntax Conversion Rules

### Headings
- `* Heading`      → `# Heading`
- `** Heading`     → `## Heading`
- `*** Heading`    → `### Heading`

### Lists
- `- item`         → `- item`
- `-- item`        → nested list
- `+ item`         → ordered list if semantically appropriate

### Links
- `[[PageName]]` → `[PageName](PageName.md)`
- `[[label>PageName]]` → `[label](PageName.md)`
- External links should remain unchanged
- Internal wiki links must be resolved using `pukiwiki_page_inventory.csv` (`page_name` -> `converted_filename`)
- For Jekyll posts, output internal links with `{% post_url YYYY-MM-DD-ULID %}` derived from `converted_filename`

### Inline Formatting
- `''italic''`     → `*italic*`
- `'''bold'''`     → `**bold**`
- `%%%` or similar inline styles → preserve text, drop styling if unclear

### Code Blocks
- PukiWiki preformatted blocks
  → fenced code blocks using triple backticks
- Preserve content exactly as written (no syntax conversion inside code blocks)
- Ensure one blank line before and after each fenced code block
- Once a line is treated as code-block content, do not apply any conversion rules in this document to that line

### Tables
- Convert simple tables to Markdown tables
- For table-like rows (`|...|`), if a row ends with `|h` (or `|h|`), treat that row as the header row
  - The trailing `h` marker is not part of header cell content
- If no header marker row exists, prepend an empty header row and a separator row
  - Example:
    - `| a | b |` becomes:
      - `|  |  |`
      - `| --- | --- |`
      - `| a | b |`
- If table structure is complex, preserve as-is using fenced blocks

### Definition Terms
- Convert definition rows (`:term|description`) to HTML definition lists
  - Consecutive definition rows must be grouped in one `<dl>`
  - If description continues on following lines, include those lines in the same `<dd>` until the next definition row or a block boundary
  - Output format:
    - `<dl><dt>term</dt><dd>description</dd>...</dl>`

### Plugins / Macros
- PukiWiki plugins (e.g. `#ref`, `#include`, `#ls`)
  → Do NOT execute or expand
  → Replace with:
    `<!-- TODO: original plugin here -->`
- Exception for image display:
  - `#ref(...)` and `&ref(...);` should be converted to image embeds when the referenced attachment exists
  - Output format for images must be unified to Markdown: `![alt](url)`
  - Ensure one blank line before and after each image line
  - If image resolution fails, retry resolution considering Unicode normalization differences (NFC/NFD), especially for Japanese voiced/semi-voiced characters
  - If the attachment cannot be resolved, emit a TODO comment instead of dropping it
- Exception for navigation:
  - `#navi` / `#navi()` should be resolved as a list of child pages under the current page directory
  - Do not add any heading text for `#navi` output; emit only the list

## Metadata Handling
- Page title should be derived from:
  1. Explicit title if available
  2. First heading
  3. Page filename fallback

## Error Handling Policy
- Never fail silently
- Prefer explicit TODO comments
- Preserve original text when unsure

## Working Style for Codex
- Read this README.md before starting any conversion
- Convert one page at a time
- Ask questions if assumptions are required
- Do not optimize prematurely
- For a fresh workspace, first generate `pukiwiki_page_inventory.csv`, then perform page conversion based on that inventory
- Use `pukiwiki_builtin_pages.txt` to mark built-in pages, and exclude rows with `convert_target=false`

## Non-Goals
- Perfect visual parity
- CSS or theme migration
- Plugin behavior emulation

---

This README defines the **source of truth** for conversion.
All generated files must comply with these rules.
