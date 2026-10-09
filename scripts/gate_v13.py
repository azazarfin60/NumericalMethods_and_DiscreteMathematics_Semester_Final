#!/usr/bin/env python3
"""V13: merge-map invariants. Structure and provenance, never arithmetic.

Checks `scripts/merge_map.csv` against `scripts/answer_manifest.csv` and
`scripts/filelist.txt`. Written before the first topic file, because the rule
being enforced is that a topic file is *generated* and never re-authored: every
unit must have exactly one block, every block exactly one origin, and no L3 pair
may share a block.

V13 RED (n)
  ...list of failures...
"""

import csv
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MAP = os.path.join(ROOT, "scripts", "merge_map.csv")
MANIFEST = os.path.join(ROOT, "scripts", "answer_manifest.csv")
FILELIST = os.path.join(ROOT, "scripts", "filelist.txt")

VALID = {"L1", "L2", "L3"}


def yearq(unit_id):
    m = re.match(r"(\d{4}) Q\.(\d+)", unit_id)
    return (int(m.group(1)), int(m.group(2))) if m else (9999, 9999)


def main():
    fails = []

    def bad(msg):
        fails.append(msg)

    if not os.path.exists(MAP):
        print("V13 RED (1)\n  merge_map.csv missing; run build_merge_map.py")
        return 1

    rows = list(csv.DictReader(open(MAP, encoding="utf-8")))
    man = {r["unit_id"]: r for r in csv.DictReader(open(MANIFEST, encoding="utf-8"))}
    listed = {l.strip() for l in open(FILELIST, encoding="utf-8") if l.strip()}

    # --- coverage ------------------------------------------------------------
    got = [r["unit_id"] for r in rows]
    if len(got) != len(set(got)):
        dupes = sorted({u for u in got if got.count(u) > 1})
        bad("unit appears twice in the map: %s" % ", ".join(dupes))
    for u in sorted(set(man) - set(got)):
        bad("unit has no map row: %s" % u)
    for u in sorted(set(got) - set(man)):
        bad("map row names no unit: %s" % u)

    # --- the map must not re-file anything -----------------------------------
    # Filing is the manifest's job. If the map disagrees, the generator has
    # started inventing placements, which is the failure this gate exists for.
    for r in rows:
        u = r["unit_id"]
        if u not in man:
            continue
        if r["subtopic_id"] != man[u]["subtopic"].strip():
            bad("%s: map files it under %s, manifest says %s"
                % (u, r["subtopic_id"], man[u]["subtopic"].strip()))
        if r["also_subtopics"] != man[u]["also_subtopics"].strip():
            bad("%s: map alters also_subtopics" % u)
        if r["level"] not in VALID:
            bad("%s: level %r is not L1/L2/L3" % (u, r["level"]))

    # --- block shape ---------------------------------------------------------
    blocks = {}
    for r in rows:
        blocks.setdefault((r["block_id"], r["level"]), []).append(r)

    for (bid, lvl), rs in blocks.items():
        origins = [x for x in rs if x["repeat_of"] == ""]

        if lvl == "L1":
            if len(rs) != 1:
                bad("L1 block %s holds %d units; L1 is one unit"
                    % (bid, len(rs)))
            if rs[0]["unit_id"] != bid:
                bad("L1 block %s is not named for its unit %s"
                    % (bid, rs[0]["unit_id"]))

        elif lvl == "L2":
            if len(origins) != 1:
                bad("L2 block %s has %d origins, want exactly 1"
                    % (bid, len(origins)))
                continue
            o = origins[0]["unit_id"]
            for x in rs:
                if x["unit_id"] == o:
                    continue
                if x["repeat_of"] != o:
                    bad("%s: repeat_of=%r but the origin is %s"
                        % (x["unit_id"], x["repeat_of"], o))
                elif yearq(x["unit_id"]) <= yearq(o):
                    bad("%s precedes the origin of its own block %s"
                        % (x["unit_id"], o))
            # An L2 block is one file. Every member must reach the block's
            # subtopic, or the answer sits in a file that cannot see it.
            if re.match(r"(?:NM|DM)-\d+\.\d+$", bid):
                for x in rs:
                    reach = {x["subtopic_id"]} | {
                        t for t in x["also_subtopics"].split() if t}
                    if bid not in reach:
                        bad("L2 block %s unreachable from %s"
                            % (bid, x["unit_id"]))

        elif lvl == "L3":
            for x in rs:
                if x["block_id"] != x["unit_id"]:
                    bad("%s is L3 but sits in shared block %s; L3 never merges"
                        % (x["unit_id"], x["block_id"]))
                if x["repeat_of"]:
                    bad("%s is L3 but claims to be a repeat of %s"
                        % (x["unit_id"], x["repeat_of"]))

    # --- every block that names a subtopic must have a file ------------------
    for (bid, lvl) in blocks:
        if not re.match(r"(?:NM|DM)-\d+\.\d+$", bid):
            continue
        if not any(l.startswith(bid + "_") for l in listed):
            bad("block %s has no file in filelist.txt" % bid)

    # --- the 2020 Q.7(b) / 2024 Q.4(b) pair, named explicitly -----------------
    # The section 7 register calls it Near-verbatim. It is L3, and this gate
    # fails loudly if anyone relabels it, because the label is what stops the
    # generator merging an Euler answer into an RK4 answer.
    pair = {r["unit_id"]: r for r in rows
            if r["unit_id"] in ("2020 Q.7(b)", "2024 Q.4(b)")}
    if len(pair) == 2:
        if pair["2020 Q.7(b)"]["level"] != "L3" or \
           pair["2024 Q.4(b)"]["level"] != "L3":
            bad("2020 Q.7(b) / 2024 Q.4(b) must stay L3: the method changed "
                "from Euler to RK4 and the initial value with it")
        if pair["2020 Q.7(b)"]["block_id"] == pair["2024 Q.4(b)"]["block_id"]:
            bad("2020 Q.7(b) / 2024 Q.4(b) must not share a block")

    if fails:
        print("V13 RED (%d)" % len(fails))
        for f in fails:
            print("  " + f)
        return 1

    l1 = sum(1 for r in rows if r["level"] == "L1")
    l2 = sum(1 for r in rows if r["level"] == "L2")
    l3 = sum(1 for r in rows if r["level"] == "L3")
    merged = len({r["block_id"] for r in rows if r["level"] == "L2"})
    print("V13 GREEN")
    print("  %d units: L1 %d, L2 %d into %d blocks, L3 %d never merged"
          % (len(rows), l1, l2, merged, l3))
    print("  L2 blocks written once from the earliest appearance")
    return 0


if __name__ == "__main__":
    sys.exit(main())
