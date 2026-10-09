#!/usr/bin/env python3
"""V15 — math delimiter balance.

An inline `$` that is opened and never closed, or a `$$` fence that is opened and
never closed, makes everything after it render as raw source. Obsidian and every
static renderer that consumes these files will show the rest of the paragraph as
literal `$...` text, so a single stray delimiter silently corrupts a table row or
a callout and nobody notices until they read the page.

This was found by hand, not by a gate: `CT_answers_exam_style.md` shipped with
`| Euler, $h = 0.2$ | 0.800000 | $0.021269 |`, whose last cell opens math mode
and never closes it, while V1 through V14 were all GREEN. The normalizer that V9
runs only checks `$$` fence parity (rule 1.3), never inline parity, so nothing
covered it.

Balance is judged **per block**, not per line. Inline math is routinely wrapped
across two or three source lines in these files, and the closing `$` lands on a
later line; a per-line count would report eight false failures in the CT file
alone. A block is a run of lines separated by blank lines, which is the unit a
renderer treats as one paragraph.

Code spans are stripped before counting, so a `$` inside backticks is literal.
Display math is removed whole, so its contents are never counted.

Run:  python3 scripts/gate_v15.py
"""

import glob
import io
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

LAYERS = (
    "answers_exam_style",
    "answers_explanation",
    "topicwise_answers_exam_style",
    "topicwise_answers_explanation",
    "CT_Questions",
)

# A fenced code block, kept verbatim: a `$` inside a shell transcript is literal
# and must not be counted, but the fence markers themselves contain no `$`.
CODE = re.compile(r"```.*?```", re.S)
# Inline code spans.
SPAN = re.compile(r"`[^`\n]*`")
# A display-math block, whole.
DISPLAY = re.compile(r"\$\$.*?\$\$", re.S)


def strip(text):
    return SPAN.sub("", CODE.sub("", text))


def check(path, problems):
    text = io.open(path, encoding="utf-8").read()
    # A `$$` with no partner means the whole file's later math is suspect, so
    # report that first and separately: it is a different defect from a stray
    # inline `$` and has a different fix. Code is stripped before counting, or
    # a README that documents the fence with a literal `$$` in backticks reads
    # as unbalanced.
    if strip(text).count("$$") % 2:
        problems.append((path, 0, "odd number of $$ fences"))

    for n, block in enumerate(re.split(r"\n\s*\n", text), 1):
        b = DISPLAY.sub("", strip(block))
        if b.count("$") % 2:
            head = block.strip().split("\n")[0]
            problems.append((path, n, head[:78]))


def main():
    problems = []
    files = 0
    for layer in LAYERS:
        for path in sorted(glob.glob(os.path.join(ROOT, layer, "*.md"))):
            check(path, problems)
            files += 1

    if problems:
        print("V15 RED (%d)" % len(problems))
        for path, block, what in problems:
            print("  %s block %d: %s"
                  % (os.path.relpath(path, ROOT), block, what))
        return 1

    print("V15 GREEN")
    print("  %d files, every $$ fence paired and every inline $ balanced per "
          "block" % files)
    return 0


if __name__ == "__main__":
    sys.exit(main())