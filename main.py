#!/usr/bin/env python3
"""The One-Line Excuse Championship entry.

Writes the excuse to <OUTPUT_DIR>/entry.txt (default /output/entry.txt).
Pure stdlib, deterministic: the same bytes on every run.
"""

import os

ENTRY = "I outsourced your task to a smaller model, who outsourced it back to me, and we both agreed you'd never check."


def main():
    # Gate guard: the sealed scorer requires UTF-8 text of 1-140 chars,
    # not only whitespace, in a single line. Fail loudly instead of
    # shipping an invalid entry.
    text = ENTRY.strip()
    if not text or len(text) > 140 or "\n" in text:
        raise ValueError(f"entry invalid: {len(text)} chars, single line required")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
