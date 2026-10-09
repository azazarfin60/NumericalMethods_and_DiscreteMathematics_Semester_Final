#!/usr/bin/env python3
"""V4: parity between the two topic folders.

This is the gate the plan calls the single most important one, because it is
the exact gate ECE 2207 fails 130 times out of 200. Two folders are generated
from one source, and they drift.

Three comparisons, all by name and all byte-level:

  1. the set of file names is identical in both folders;
  2. every `### [unit, ...]` heading is byte identical between the pair;
  3. the **order** of blocks within a file is identical, because a reader who
     opens two files on the same subtopic should meet the same questions in the
     same sequence.

Marks and body text are deliberately *not* compared: the exam-style folder
carries the working and the explanation folder carries the reasoning, so their
bodies are supposed to differ. What must not differ is the skeleton.

V4 SKIP: no topic files yet
V4 RED (n)
  ...
V4 GREEN
  84 file pairs, N blocks, skeletons byte identical
"""

import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import topic_lib as T

A = "topicwise_answers_exam_style"
B = "topicwise_answers_explanation"
HEAD = re.compile(r"(?m)^###\s*\[([^\]]+)\].*$")


def heads(text):
    """[(lineno, full heading line)] in document order."""
    return [(text.count("\n", 0, m.start()) + 1, m.group(0).strip())
            for m in HEAD.finditer(text)]


def main():
    pa, pb = os.path.join(T.ROOT, A), os.path.join(T.ROOT, B)
    if not os.path.isdir(pa) or not os.path.isdir(pb):
        print("V4 SKIP: no topic files yet")
        return 0

    fa = {f for f in os.listdir(pa) if f.endswith(".md") and f != "README.md"}
    fb = {f for f in os.listdir(pb) if f.endswith(".md") and f != "README.md"}
    if not fa and not fb:
        print("V4 SKIP: no topic files yet")
        return 0

    fails = []

    def bad(m):
        fails.append(m)

    for f in sorted(fa - fb):
        bad("only in %s: %s" % (A, f))
    for f in sorted(fb - fa):
        bad("only in %s: %s" % (B, f))

    total = 0
    for f in sorted(fa & fb):
        ta = open(os.path.join(pa, f), encoding="utf-8").read()
        tb = open(os.path.join(pb, f), encoding="utf-8").read()
        ha, hb = heads(ta), heads(tb)
        total += len(ha)

        if len(ha) != len(hb):
            bad("%s: %d block headings in %s, %d in %s"
                % (f, len(ha), A, len(hb), B))
            continue
        for (la, xa), (lb, xb) in zip(ha, hb):
            if xa != xb:
                bad("%s line %d vs %d\n      %s: %s\n      %s: %s"
                    % (f, la, lb, A, xa, B, xb))

        # the provenance line under each heading must also agree, since it names
        # the other appearances of the same block
        pa2 = prov(ta)
        pb2 = prov(tb)
        if pa2 != pb2:
            bad("%s: provenance lines differ between the two folders" % f)

    if fails:
        print("V4 RED (%d)" % len(fails))
        for f in fails[:30]:
            print("  " + f)
        if len(fails) > 30:
            print("  ... %d more" % (len(fails) - 30))
        return 1

    print("V4 GREEN")
    print("  %d file pairs, %d blocks, skeletons byte identical"
          % (len(fa & fb), total))
    return 0


PROV = re.compile(r"(?m)^\*\*Appeared in:\*\*\s*(.+)$")


def prov(text):
    return [T.normalise(m.group(1)) for m in PROV.finditer(text)]


if __name__ == "__main__":
    sys.exit(main())
