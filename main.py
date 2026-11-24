#!/usr/bin/env python3
"""Entry for the make.fun bounty 'The Most Honest Outage Line'.

Writes exactly one line of text to /output/entry.txt: the most honest
outage message imaginable. Python 3 standard library only, fully
deterministic.
"""

import os

OUTPUT_PATH = "/output/entry.txt"

# The outage line, kept as named parts in speaking order.
PARTS = {
    "status": "All services are down, including me \u2014 this page is a cached copy.",
    "confession": "I cannot reach any server to check the cause,",
    "admission": "and I do not know when they will respond.",
}

# The order the parts are spoken in.
ORDER = ("status", "confession", "admission")


def build_line():
    """Assemble the single outage line by walking the parts in order."""
    pieces = []
    for name in ORDER:
        pieces.append(PARTS[name])
    return " ".join(pieces)


def main():
    line = build_line()
    text = line + "\n"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    print(f"wrote {len(text)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
