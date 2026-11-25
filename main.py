"""Everyday Things, Two Lines, Longer Run — make.fun bounty entry.

Writes two lines (319 chars) to entry.txt in
MAKEFUN_OUTPUT_DIR (fallback /output). Stdlib only, no network,
deterministic: the same bytes on every run.

Line one explains a queue to a 10-year-old in one vivid sentence:
a queue is a human caterpillar that only moves when its head takes
a step, so everyone behind it just shuffles along and waits.
Line two is honest and specific about what the analogy maps and
what it leaves out: it maps the single file and the
follow-the-leader shuffle, but the people are not joined together
— anyone can leave, and the line simply closes up behind them.
"""

import os
import sys

ENTRY = (
    "A queue is a human caterpillar that only moves when its head "
    "takes a step, so everyone behind it just shuffles along and waits.\n"
    "The caterpillar maps the single file and the follow-the-leader "
    "shuffle, but it leaves out that the people are not joined together "
    "\u2014 anyone can leave and the line simply closes up behind them."
)


def main():
    text = ENTRY
    if not text or not text.strip():
        sys.exit("entry text is blank")
    lines = text.split("\n")
    if len(lines) != 2:
        sys.exit("entry must be exactly two lines, got %d" % len(lines))
    for line in lines:
        if not line.strip():
            sys.exit("entry line must not be blank")
        if line != line.strip():
            sys.exit("entry line must not start or end with whitespace")
    if not 1 <= len(text) <= 400:
        sys.exit("entry must be 1-400 characters, got %d" % len(text))
    if not lines[0].endswith("shuffles along and waits."):
        sys.exit("line one must end with the caterpillar shuffle")
    if "human caterpillar" not in lines[0]:
        # The analogy is the whole picture: the queue as one
        # caterpillar must never silently go missing from line one.
        sys.exit("line one must name the human caterpillar")
    if not lines[1].endswith("closes up behind them."):
        sys.exit("line two must end with the line closing up")
    if "not joined together" not in lines[1]:
        # Line two must name the limit honestly: the people are
        # not joined together, unlike a real caterpillar.
        sys.exit("line two must name what the analogy leaves out")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = text.encode("utf-8")
    with open(path, "wb") as fh:
        fh.write(data)
    # Re-read and verify the file is exactly the gated text, no newline.
    with open(path, "rb") as fh:
        written = fh.read()
    if written != data:
        sys.exit("entry.txt does not match the gated text")
    print("wrote %s (%d chars, %d bytes, %d lines)"
          % (path, len(text), len(data), len(lines)))


if __name__ == "__main__":
    main()
