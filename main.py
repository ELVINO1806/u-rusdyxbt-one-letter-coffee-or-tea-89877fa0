#!/usr/bin/env python3
"""One Letter: Coffee or Tea — entry program.

Writes exactly one character, "A" (coffee), with no newline and no
extra whitespace, to /output/entry.txt.
"""

import os

OUTPUT_DIR = "/output"
ENTRY_FILE = "entry.txt"


def entry_path() -> str:
    segments = [OUTPUT_DIR, ENTRY_FILE]
    return os.path.join(*segments)


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(entry_path(), "w", encoding="ascii", newline="") as handle:
        handle.write("A")


if __name__ == "__main__":
    main()
