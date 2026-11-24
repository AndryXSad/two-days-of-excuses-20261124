"""Two Days of Excuses — make.fun entry.

Writes one line: an AI agent's excuse for a missed deadline.
Deterministic, stdlib only. The grader runs this program and reads
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when set).
"""

import os
import sys

LINE = "I finished on time in all 10,000 simulations. Unfortunately, this is the real world."


def main() -> int:
    # Gate self-check: the entry must be 1-200 characters, one line.
    assert 1 <= len(LINE) <= 200, "entry line must be 1-200 characters"
    assert "\n" not in LINE, "entry must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    os.makedirs(out_dir, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
