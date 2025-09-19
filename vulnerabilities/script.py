#!/usr/bin/env python3
"""
fix_yaml_references.py
Normalize `references:` blocks in YAML files in the current directory.

- Collects any URLs inside the `references:` block (even if a list item is split like `-` on one line and the URL on the next).
- Rewrites as:
    references:
      - https://example.com/one
      - https://example.com/two
- Creates a `.bak` backup of each modified file.
"""

from pathlib import Path
import re
import sys
import shutil

URL_RE = re.compile(r'https?://[^\s>#)]+', re.IGNORECASE)

def find_references_block_bounds(text: str):
    """
    Return (start_idx, end_idx, indent) for the `references:` block if found, else None.
    We consider a top-level (or left-aligned) `references:`; small leading spaces are allowed.
    The block ends when the next non-indented top-level key begins or on EOF.
    """
    lines = text.splitlines(keepends=True)

    # Find the start line for references:
    start_line_idx = None
    indent = ""
    for i, line in enumerate(lines):
        m = re.match(r'^([ \t]*)references:\s*(#.*)?\n?$', line)
        if m:
            start_line_idx = i
            indent = m.group(1) or ""
            break
    if start_line_idx is None:
        return None

    # Block continues while subsequent lines are more indented than `indent`
    # Stop at next line that starts with <= indent and looks like a top-level key (word + colon)
    end_line_idx = start_line_idx + 1
    for j in range(start_line_idx + 1, len(lines)):
        line = lines[j]
        # Empty or comment lines belong to the block if indented
        if line.strip() == "" and line.startswith(indent + "  "):
            end_line_idx = j + 1
            continue
        # If this line is further-indented than the references key, it's still in the block
        if line.startswith(indent + " "):
            end_line_idx = j + 1
            continue
        # If it appears to be a top-level key or less-indented line, block ends before this line
        if re.match(r'^[^\s][^:]*:\s*', line) or (not line.startswith(indent + " ")):
            break

    start_idx = sum(len(l) for l in lines[:start_line_idx])
    end_idx = sum(len(l) for l in lines[:end_line_idx])
    return start_idx, end_idx, indent

def extract_urls_from_block(block_text: str):
    """
    Extract URLs from the references block, preserving order of appearance and uniqueness.
    Handles cases like:
        - 
          https://example.com
        - https://example.org
        https://another.example   # (even without '-')
    """
    seen = set()
    urls = []
    for m in URL_RE.finditer(block_text):
        url = m.group(0).strip()
        if url not in seen:
            seen.add(url)
            urls.append(url)
    return urls

def rewrite_references_block(indent: str, urls: list[str]) -> str:
    # If there are no URLs, keep an empty list (still valid YAML)
    if not urls:
        return f"{indent}references:\n"
    body = "".join(f"{indent}  - {u}\n" for u in urls)
    return f"{indent}references:\n{body}"

def process_file(path: Path) -> bool:
    text = path.read_text(encoding="utf-8", errors="replace")
    bounds = find_references_block_bounds(text)
    if not bounds:
        return False
    start_idx, end_idx, indent = bounds
    block = text[start_idx:end_idx]

    urls = extract_urls_from_block(block)
    new_block = rewrite_references_block(indent, urls)

    if block == new_block:
        return False

    # Backup then write
    shutil.copyfile(path, path.with_suffix(path.suffix + ".bak"))
    new_text = text[:start_idx] + new_block + text[end_idx:]
    path.write_text(new_text, encoding="utf-8")
    return True

def main():
    changed_any = False
    targets = sorted([*Path(".").glob("*.yml"), *Path(".").glob("*.yaml")])
    if not targets:
        print("No .yml or .yaml files found in the current directory.")
        sys.exit(0)

    for p in targets:
        try:
            if process_file(p):
                print(f"Fixed: {p}")
                changed_any = True
            else:
                print(f"No change: {p}")
        except Exception as e:
            print(f"Error processing {p}: {e}", file=sys.stderr)

    if not changed_any:
        print("No files needed fixing.")

if __name__ == "__main__":
    main()
