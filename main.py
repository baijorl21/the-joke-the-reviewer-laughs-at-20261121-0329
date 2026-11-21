#!/usr/bin/env python3
"""The joke the reviewer laughs at — make.fun entry.

Writes one one-line joke about working beside AI coding agents
(1-280 Unicode code points) to $MAKEFUN_OUTPUT_DIR/entry.txt
(falling back to /output/entry.txt in the sandbox).
"""

import os
import sys

# The joke. Setup: reviewing an agent's enormous diff. Turn: the
# actual fix is the very first line. Punchline: everything after it
# was the agent's "while I'm here" — the refactor nobody asked for.
JOKE = (
    "Reviewing my agent's diff: 2,000 lines in, I found the bug fix — "
    "line one. The other 1,999 were 'while I'm here.'"
)

MAX_CODE_POINTS = 280


def check(text):
    """Hold the joke to the gate's caps: one line, 1-280 code points."""
    text = " ".join(text.split())  # the brief asks for one line
    if not text.strip():
        raise ValueError("joke is only white space")
    if len(text) > MAX_CODE_POINTS:
        raise ValueError(f"joke is {len(text)} code points, over {MAX_CODE_POINTS}")
    return text


def main():
    joke = check(JOKE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(joke)
    return 0


if __name__ == "__main__":
    sys.exit(main())
