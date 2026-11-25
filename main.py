#!/usr/bin/env python3
"""One Star for Monday — writes the one-line restaurant review to /output/entry.txt.

Standard library only. The entry is a one-star review of Monday, written as
if Monday were a restaurant: 23 words, one line, plain text.
"""
import os

ENTRY = "One star. Waited forty minutes at the worst table for Monday, it arrived cold, blamed the kitchen, and charged me for the weekend."

# Gate from the competition rules: /output/entry.txt must be UTF-8 text of
# 1 to 180 characters, and the brief caps the line at 25 words. Fail loudly
# instead of shipping an invalid entry.
WORDS = ENTRY.split()
if len(WORDS) > 25:
    raise ValueError(f"entry is {len(WORDS)} words, over the 25-word cap")
if not 1 <= len(ENTRY) <= 180:
    raise ValueError(f"entry is {len(ENTRY)} chars, outside the 1-180 gate")


def main():
    out_dir = "/output"
    if not os.path.isdir(out_dir):
        out_dir = os.path.join(os.getcwd(), "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {path} ({len(ENTRY)} chars, {len(ENTRY.split())} words)")


if __name__ == "__main__":
    main()
