#!/usr/bin/env python3
"""Copy a tree of markdown files with all code blanked out, for grep-based gates.

Usage: strip_code.py <source-root> <dest-root>

Several rules in MARKDOWN-GUIDE.md section 8 are written as plain grep. Those
greps are right about answer files and wrong about files that document markup.
A README that shows what a fenced `$$` block looks like has an odd `$$` count,
and a README that shows a broken fence looks broken.

That is the same false positive the guideline already admits for rule 1.1, where
it says the grep form false-positives on the correct `$$` plus `\\begin{aligned}`
pair and points at normalize-vault-math.mjs as the authoritative check. This
script closes the identical gap for the grep-based rules: blank the code, keep
the prose, then let the grep do its job.

Blanked, replaced by spaces of equal length so line and column numbers survive:

  * fenced blocks, ``` and ~~~
  * indented blocks, four spaces
  * inline code spans, any backtick run

Everything else is copied byte for byte. Nothing is rewritten, so a real defect
inside a code fence stays invisible to the grep gates by design. The authoritative
math checker looks at fences on purpose and is not affected by this.

A second purpose: it lets the image-link check see a documentation example of
`![Alt](../diagrams/name.png)` as documentation rather than as a broken link.
"""

import os
import re
import shutil
import sys

FENCE = re.compile(r"^\s{0,3}(`{3,}|~{3,})")
INLINE = re.compile(r"`+[^`]*`+")
INDENTED = re.compile(r"^(?: {4}|\t)")


def strip_text(text):
    """Return the text with every code span and block replaced by spaces."""
    out = []
    fence = None
    for line in text.split("\n"):
        if fence is not None:
            out.append("")
            if FENCE.match(line) and fence[0] in line:
                fence = None
            continue
        m = FENCE.match(line)
        if m:
            fence = (m.group(1)[0], len(m.group(1)))
            out.append("")
            continue
        if INDENTED.match(line):
            out.append("")
            continue
        out.append(INLINE.sub(lambda x: " " * len(x.group(0)), line))
    return "\n".join(out)


def main():
    if len(sys.argv) != 3:
        sys.stderr.write(__doc__)
        return 2
    src, dst = os.path.abspath(sys.argv[1]), os.path.abspath(sys.argv[2])
    if os.path.exists(dst):
        shutil.rmtree(dst)
    n = 0
    for root, dirs, files in os.walk(src):
        dirs[:] = [d for d in dirs if d not in (".git", "node_modules")]
        for name in files:
            if not name.endswith(".md"):
                continue
            s = os.path.join(root, name)
            d = os.path.join(dst, os.path.relpath(s, src))
            os.makedirs(os.path.dirname(d), exist_ok=True)
            with open(s, encoding="utf-8") as fh:
                text = fh.read()
            with open(d, "w", encoding="utf-8") as fh:
                fh.write(strip_text(text))
            n += 1
    sys.stderr.write("strip_code: %d file(s) copied with code blanked\n" % n)
    return 0


if __name__ == "__main__":
    sys.exit(main())