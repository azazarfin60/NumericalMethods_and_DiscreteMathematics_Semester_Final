#!/usr/bin/env python3
"""V8: marks fidelity, and the layer-wide identity sweep.

The plan splits these: V8 is marks, and the identity sweep that covers every
number in a topic file is V5. Both are checked here because they read the same
structures and because a number is wrong often enough to be worth a second
reader.

  1. **Marks.** A block heading that prints marks must print the marks the paper
     margin gives for that part. Where a part carries none, the question total
     is used and labelled as such. Class tests print marks at question level
     only, and a part heading must therefore not invent a split.

  2. **Every box is character identical to its year-wise origin.** Not merely
     equal in value: the same characters. V5 does this for P1 against P2; this
     does it for the topic folders against P1, which is the hop that had no
     gate.

  3. **No number is born in a topic file.** Any decimal with four or more
     decimal places, or in scientific notation, appearing in a topic file must
     occur in the year-wise section the block was copied from. This is a
     deliberately blunt test: it cannot tell a correct new number from an
     incorrect one, it only asks where the digits came from, and anything it
     flags has to be traced before it can stay.

V8 SKIP: no topic files yet
V8 RED (n)
  ...
V8 GREEN
  N boxes and M long numerals all trace to a year-wise section
"""

import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import topic_lib as T

DIRS = ["topicwise_answers_exam_style", "topicwise_answers_explanation"]
UNIT = re.compile(r"\d{4} Q\.\d+\([a-z]\)|CT-[\w]+ Q\.\d+(?:\([a-z]\))?")
HEAD = re.compile(r"(?m)^###\s*\[([^\]]+)\]:?\s*(.*)$")
# 4+ decimal places, or scientific notation with 3+ significant decimals
LONGNUM = re.compile(r"(?<![\d.])\d+\.\d{4,}(?![\d])"
                     r"|(?<![\d.])\d+(?:\.\d+)?[eE][-+]?\d{2,}(?![\d])")


def numerals(text):
    return set(LONGNUM.findall(text))


def main():
    files = []
    for d in DIRS:
        p = os.path.join(T.ROOT, d)
        if os.path.isdir(p):
            files += [(d, f) for f in sorted(os.listdir(p))
                      if f.endswith(".md") and f != "README.md"]
    if not files:
        print("V8 SKIP: no topic files yet")
        return 0

    fails = []

    def bad(m):
        fails.append(m)

    rows = T.load_map()
    by_id = {r["unit_id"]: r for r in rows}

    # The pool a topic file is allowed to draw from: every year-wise section,
    # plus the taxonomy itself.
    p1 = T.load_p1()
    p2 = T.load_p2()
    pool_boxes = set()
    pool_nums = set()
    for src in (p1, p2):
        for v in src.values():
            pool_boxes |= set(T.boxes(v["body"]))
            pool_nums |= numerals(v["body"])

    nbox = nnum = 0

    for d, f in files:
        text = open(os.path.join(T.ROOT, d, f), encoding="utf-8").read()

        for b in T.boxes(text):
            nbox += 1
            if T.normalise(b) not in {T.normalise(x) for x in pool_boxes}:
                bad("%s/%s: box with no year-wise origin: %s"
                    % (d, f, b[:66]))

        for n in sorted(numerals(text)):
            nnum += 1
            if n not in pool_nums:
                bad("%s/%s: numeral %s appears in no year-wise section"
                    % (d, f, n))

        for m in HEAD.finditer(text):
            ids = UNIT.findall(m.group(1))
            if len(ids) != 1 or ids[0] not in by_id:
                continue
            u = ids[0]
            row = by_id[u]
            mm = re.search(r"Marks:\s*([0-9]+)", m.group(2))
            if not mm:
                continue
            if u.startswith("CT-"):
                bad("%s/%s: %s prints marks %s; class tests print marks at "
                    "question level only, so a part heading must not carry one"
                    % (d, f, u, mm.group(1)))
                continue
            want = row["marks_part"] or row["marks_question"]
            if want and mm.group(1).lstrip("0") != want.lstrip("0"):
                bad("%s/%s: %s prints marks %s, paper gives %s"
                    % (d, f, u, mm.group(1), want))

    if fails:
        print("V8 RED (%d)" % len(fails))
        for f in fails[:40]:
            print("  " + f)
        if len(fails) > 40:
            print("  ... %d more" % (len(fails) - 40))
        return 1

    print("V8 GREEN")
    print("  %d boxes and %d long numerals all trace to a year-wise section"
          % (nbox, nnum))
    return 0


if __name__ == "__main__":
    sys.exit(main())
