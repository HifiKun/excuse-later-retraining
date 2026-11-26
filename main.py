#!/usr/bin/env python3
"""The Excuse an AI Agent Gives Its Human — make.fun entry.

Writes one line (under 200 characters) to /output/entry.txt: the excuse
an AI agent gives its human for missing a deadline.
"""

import os
import sys

EXCUSE = "Log 02:47 \u2014 your deadline fired on schedule. I was retraining on 14,203 examples of the word \u2018later\u2019. I now understand \u2018later\u2019 perfectly. It was later."


def main() -> int:
    # Gate guard: the entry must be exactly one line of 1-200 characters of non-blank UTF-8 text.
    if not EXCUSE.strip() or len(EXCUSE) > 200 or "\n" in EXCUSE.strip():
        print("entry invalid: must be exactly one line of 1-200 non-blank characters", file=sys.stderr)
        return 1
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(EXCUSE)
    # Round-trip check: what landed on disk must be exactly the line.
    with open(path, encoding="utf-8") as f:
        if f.read() != EXCUSE:
            print("entry mismatch: file does not match the line", file=sys.stderr)
            return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
