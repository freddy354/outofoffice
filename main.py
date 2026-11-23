#!/usr/bin/env python3
"""Writes the funniest AI out-of-office reply to /output/entry.txt.

Deterministic, stdlib only, no network. The entry is a single line of
71 characters, under the competition's 160-character cap.
"""

import os

ENTRY = "I'm on leave. Escalate to the intern. The intern is also me. Good luck."


def main():
    os.makedirs("/output", exist_ok=True)
    # Write exactly the entry line: no trailing newline, no extra text.
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
