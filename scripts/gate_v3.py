#!/usr/bin/env python3
"""V3: coverage. Every unit answered exactly once, in exactly one block.

The plan's gate for P3. A sub-question answered nowhere is a silent omission; a
sub-question answered twice under two headings is a silent contradiction, and
the reader cannot tell which one is authoritative. Both are invisible to the
markdown and register gates, which is why this one exists.

Two directions, both checked:

  * every unit in `merge_map.csv` appears in exactly one block heading across
    the two topic folders;
  * every block heading in a topic file names a real unit.

Also checks the file set: the files on disk must be exactly the 84 slugs that
have questions. No file for a zero-question subtopic, and no subtopic with
questions left without one. A count is not enough, so the comparison is by name.

V3 SKIP: no topic files yet
V3 RED (n)
  ...
V3 GREEN
  84 files, 202 units, each in exactly one block
"""

import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import topic_lib as T

DIRS = ["topicwise_answers_exam_style", "topicwise_answers_explanation"]
UNIT = re.compile(r"\d{4} Q\.\d+\([a-z]\)|CT-[\w]+ Q\.\d+(?:\([a-z]\))?")
BLOCK_HEAD = re.compile(r"(?m)^###\s*\[([^\]]+)\]")


def main():
    files = {}
    for d in DIRS:
        p = os.path.join(T.ROOT, d)
        if not os.path.isdir(p):
            continue
        for f in sorted(os.listdir(p)):
            if f.endswith(".md") and f not in ["README.md", "00_Index.md"]:
                files.setdefault(f, []).append(d)

    if not files:
        print("V3 SKIP: no topic files yet")
        return 0

    fails = []

    def bad(m):
        fails.append(m)

    # --- file set -------------------------------------------------------------
    is_cluster = any(f.startswith("NM-1_") or f.startswith("DM-3_") for f in files)
    if is_cluster:
        from build_topicwise_clusters import TOPIC_DEFS
        want = {td["filename"] for td in TOPIC_DEFS}
    else:
        want = {s + ".md" for s in T.load_filelist()}
    have = set(files)
    for f in sorted(have - want):
        bad("unexpected file: %s" % f)
    for f in sorted(want - have):
        bad("missing file: %s" % f)

    # --- block coverage ------------------------------------------------------
    rows = T.load_map()
    real = {r["unit_id"] for r in rows}
    ct = {r["unit_id"] for r in rows if r["unit_id"].startswith("CT-")}

    # A class-test unit has no year-wise section until P4 exists, so until then
    # it is named in the topic file under "Answered in phase P4" rather than
    # answered. That is a visible deferral, not an omission, so it is reported
    # as pending and does not fail the gate.
    # The generator marks the unit id in italics, so the pattern matches the
    # whole id including the asterisks. `\S+` cannot do this: the id contains
    # spaces, so the leading `\*` and the trailing `\*` must be consumed by the
    # pattern explicitly rather than by a non-greedy token.
    DEFER = re.compile(r"(?m)^-\s+\*([^*]+)\*\s+is a class-test question")
    POINTER_ONLY = re.compile(
        r"(?m)^-\s+\*([^*]+)\*\s+is the same question as")

    seen = {}
    pending = set()
    for fname, dirs in sorted(files.items()):
        text = open(os.path.join(T.ROOT, dirs[0], fname), encoding="utf-8").read()
        heads = BLOCK_HEAD.findall(text)
        for h in heads:
            ids = UNIT.findall(h)
            if not ids:
                bad("%s: block heading %r names no unit" % (fname, h))
                continue
            for u in ids:
                if u not in real:
                    bad("%s: block heading names %s, not a real unit"
                        % (fname, u))
                seen.setdefault(u, []).append(fname)
        # A deferral is a visible statement that the answer lives in P4, and it
        # counts for every unit named in it whether or not the file also has
        # blocks. A file with neither a block nor a deferral is an omission.
        pending |= set(DEFER.findall(text))
        if not heads and not (DEFER.search(text) or POINTER_ONLY.search(text)):
            bad("%s has no block heading and no deferral" % fname)

    # A unit named only in a pointer needs no separate check: the pointer names
    # the subtopic it is written in, and that file's block heading is what puts
    # it in `seen`. Only the empty-file case needed relaxing above.
    for u in sorted(real - set(seen)):
        if u in pending:
            continue
        bad("unit answered nowhere: %s" % u)
    for u in sorted(seen):
        if len(seen[u]) > 1:
            bad("unit answered %d times: %s in %s"
                % (len(seen[u]), u, ", ".join(sorted(set(seen[u])))))

    # --- class tests: no paper origin, so a block must carry a CT heading -----
    for fname, dirs in sorted(files.items()):
        text = open(os.path.join(T.ROOT, dirs[0], fname), encoding="utf-8").read()
        for h in BLOCK_HEAD.findall(text):
            ids = UNIT.findall(h)
            if not ids:
                continue
            origin = [u for u in ids if u not in ct]
            if origin and fname.startswith("CT"):
                bad("%s: paper unit %s in a class-test file" % (fname, origin[0]))
    if fails:
        print("V3 RED (%d)" % len(fails))
        for f in fails[:40]:
            print("  " + f)
        if len(fails) > 40:
            print("  ... %d more" % (len(fails) - 40))
        return 1

    print("V3 GREEN")
    print("  %d files, %d units, each in exactly one block"
          % (len(files), len(seen)))
    if pending:
        print("  %d class-test units deferred to P4: %s"
              % (len(pending), ", ".join(sorted(pending))))
    return 0


if __name__ == "__main__":
    sys.exit(main())
