#!/usr/bin/env python3
"""Generate scripts/merge_map.csv.

Two sources, deliberately separated:

  * `answer_manifest.csv` is the authority for *where a unit is filed*. Its
    `subtopic` and `also_subtopics` columns are read, never re-guessed. This is
    the rule that stopped an earlier hand-built map from inventing 85 wrong
    subtopic ids.

  * `REPEATS` below is the only hand-maintained data, and it holds *merge
    decisions*, not filing. Each entry names a set of unit ids that are one
    block, and the level.

Levels, from ANSWER_BUILD_PLAN.md section 7:

    L1  one appearance. Its own block.
    L2  same method AND same structure, numbers changed. Merge: the block is
        written once, from the earliest appearance, and later members are
        recorded in the block header as repeats.
    L3  same syllabus topic only. **Never merged.** Each member is its own
        block, and the topic file lists them in sequence.

The block id is the subtopic of the *earliest* member. A later member filed
under a different subtopic is a cross-filing, and the block id says where the
answer actually lives.
"""

import csv
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MANIFEST = os.path.join(ROOT, "scripts", "answer_manifest.csv")
OUT = os.path.join(ROOT, "scripts", "merge_map.csv")

# --- the only hand-maintained data: merge decisions ----------------------------
#
# (block_id, level, [members in chronological order], note)
#
# Row 21 of the section 7 repeat register in
# PreviousYearQuestions/PreviousYearAnalysisReport.md calls 2020 Q.7(b) vs
# 2024 Q.4(b) "Near-verbatim". It is L3: 2020 is Euler with y(0)=0 and h=0.2,
# 2024 is RK4 with y(0)=1 and h=0.1. Method and initial value both changed, so
# the numbers do not correspond at all and there is nothing to merge.

REPEATS = [
    # --- L2 merges: written once, from the earliest member --------------------
    ("NM-1.5", "L2", ["2017 Q.3(b)", "2023 Q.1(b)"],
     "identical u=5xy^2/z^3 relative-error question"),
    ("NM-2.4", "L2", ["2017 Q.2(a)", "2021 Q.1(b)", "2023 Q.1(c)"],
     "same N-R limitations question; 2023 reprints the typo"),
    ("NM-4.3", "L2", ["2017 Q.5(b)", "2020 Q.3(c)"],
     "same exponential-fit table; 2020 prepends a definition"),
    ("NM-4.2", "L2", ["2017 Q.6(b)", "2024 Q.3(c)"],
     "identical straight-line table and question"),
    ("NM-3.4", "L2", ["2017 Q.7(a)", "2022 Q.4(a)"],
     "identical Jacobi system"),
    ("NM-9.1", "L2", ["2017 Q.7(b)", "2023 Q.3(a)"],
     "identical eigenproblem matrix"),
    ("NM-5.2", "L2", ["2018 Q.6(a)", "2023 Q.4(b)"],
     "same rocket integral; 2018 specifies eight segments, 2023 does not"),
    ("NM-10.4", "L2", ["2018 Q.8(a)", "2020 Q.8(b)"],
     "same Laplace equation by Liebmann iteration"),
    ("NM-5.4", "L2", ["2020 Q.6(a)", "2023 Q.4(c)"],
     "same Simpson 1/3 versus 3/8 comparison"),
    ("NM-3.8", "L2", ["2020 Q.4(b)", "2024 Q.2(b)"],
     "same GS circuit method and I1/I2/I3 naming; 2020 four resistors, 2024 three"),
    ("NM-4.7", "L2", ["2021 Q.3(c)", "2023 Q.2(a)"],
     "same request to derive Newton forward"),
    ("NM-4.6", "L2", ["2021 Q.3(d)", "2023 Q.2(b)"],
     "identical y=x^4 Lagrange table"),
    ("NM-5.5", "L2", ["2021 Q.8(b)", "2023 Q.2(c)"],
     "same Romberg integral and h sequence"),
    ("NM-8.2", "L2", ["2021 Q.8(c)", "2023 Q.3(b)"],
     "identical ODE and initial value"),
    ("DM-3.2", "L2", ["2022 Q.6(b)", "2024 Q.7(b)"],
     "identical four biconditionals"),
    ("DM-5.4", "L2", ["2022 Q.7(a)", "2024 Q.8(a)"],
     "identical congruences mod 19"),
    ("DM-5.5", "L2", ["2022 Q.7(b)", "2024 Q.8(b)"],
     "identical modular-exponentiation question"),
    ("DM-6.3", "L2", ["2022 Q.8(c)", "2024 Q.8(c)"],
     "identical generalised pigeonhole request"),

    # --- L3: same topic, NOT merged -------------------------------------------
    ("NM-3.2", "L3", ["2017 Q.4(a)", "2019 Q.3(b)", "2021 Q.7(a)", "2022 Q.3(c)"],
     "pivoting across four papers; concept repeat only, each is its own block"),
    ("NM-4.1", "L3", ["2017 Q.5(a)", "2019 Q.5(a)", "2020 Q.3(a)",
                      "2021 Q.3(a)", "2023 Q.4(a)", "2024 Q.3(a)"],
     "interpolation/extrapolation/curve-fitting definitions across six papers"),
    ("NM-1.1", "L3", ["2019 Q.1(a)", "2021 Q.1(a)", "2023 Q.1(a)"],
     "why engineers need numerical methods, and numerical versus analytical; "
     "the manifest files these under NM-1.1, not NM-1.2"),
    ("NM-8.5", "L3", ["2020 Q.7(b)", "2024 Q.4(b)"],
     "NOT a merge: 2020 is Euler with y(0)=0 h=0.2, 2024 is RK4 with y(0)=1 "
     "h=0.1. The section 7 register row 21 calls this Near-verbatim, which is "
     "wrong under the L2 rule; method and initial value both changed."),
    ("NM-4.11", "L3", ["2017 Q.5(c)", "2020 Q.3(b)", "2024 Q.3(b)"],
     "census population table across three papers; target years changed between "
     "1955, (1895, 1925), and 1995, requiring both forward and backward formulas."),
]

# Topical echoes the section 7 register lists as known omissions: same method
# and topic, reworded or re-parameterised. They are L2 merges of method, but
# the register does not count them as repeats, so each stays its own block and
# the link is recorded here rather than in the block header.
ECHOES = [
    ("2021 Q.1(a)", "2022 Q.1(a)", "bracketing framing"),
    ("2021 Q.1(c)", "2022 Q.1(b)", "Taylor evaluation"),
    ("2021 Q.3(b)", "2022 Q.1(c)", "Lagrange framing"),
    ("2021 Q.3(d)", "2022 Q.1(c)", "Lagrange framing"),
    ("2021 Q.3(c)", "2022 Q.2(c)", "Newton forward derivation"),
    ("2021 Q.7(a)", "2022 Q.3(c)", "pivoting"),
    ("2021 Q.8(b)", "2022 Q.3(a)", "Romberg"),
    ("2018 Q.8(a)", "2020 Q.8(b)", "Liebmann"),
    ("2019 Q.3(c)", "2024 Q.2(a)", "root-finding framing"),
    ("2019 Q.2(a)", "2024 Q.2(a)", "root-finding framing"),
]


def die(*msg):
    sys.exit("merge_map: " + "\n            ".join(msg))


def main():
    rows = list(csv.DictReader(open(MANIFEST, encoding="utf-8")))
    if not rows:
        die("manifest is empty")

    filed = {}
    for r in rows:
        filed[r["unit_id"]] = r["subtopic"].strip()

    blocks = {}          # unit_id -> (block_id, level, note)
    for bid, lvl, members, note in REPEATS:
        for m in members:
            if m not in filed:
                die("REPEATS names an unknown unit: %s" % m)
            if m in blocks:
                die("unit in two blocks: %s" % m)
            blocks[m] = (bid, lvl, note)

    echo = {}
    for a, b, why in ECHOES:
        for u in (a, b):
            if u not in filed:
                die("ECHOES names an unknown unit: %s" % u)
        echo.setdefault(a, []).append((b, why))
        echo.setdefault(b, []).append((a, why))

    # A block id must be a real subtopic that gets a file.
    listed = {l.strip() for l in open(os.path.join(ROOT, "scripts", "filelist.txt"),
                                      encoding="utf-8") if l.strip()}
    for bid, _lvl, _m, _n in REPEATS:
        if not any(l.startswith(bid + "_") for l in listed):
            die("block id %s has no file in filelist.txt" % bid)

    fields = ["unit_id", "block_id", "level", "subtopic_id", "also_subtopics",
              "origin_unit", "repeat_of", "echoes", "note"]

    # members of an L2 block: the earliest is the origin, the rest are repeats
    origins = set()
    repeats = {}
    for bid, lvl, members, _n in REPEATS:
        if lvl != "L2":
            continue
        origins.add(members[0])
        for m in members[1:]:
            repeats[m] = bid
    origin_blocks = {bid: members[0]
                     for bid, lvl, members, _n in REPEATS if lvl == "L2"}

    out = []
    for r in rows:
        u = r["unit_id"]
        bid, lvl, note = blocks.get(u, (u, "L1", ""))
        if lvl == "L3":
            # Each L3 member is its own block, named for its own unit.
            bid = u
        # `origin_unit` marks the single row a block is written from. Only that
        # row carries it; the later members of the same block leave it empty,
        # so a reader counts origins by counting non-empty cells.
        origin_unit = origin_blocks.get(bid) if lvl == "L2" else u
        rep = (origin_unit if (lvl == "L2" and origin_unit != u) else "")
        out.append({
            "unit_id": u,
            "block_id": bid,
            "level": lvl,
            "subtopic_id": filed[u],
            "also_subtopics": r["also_subtopics"].strip(),
            "origin_unit": origin_unit,
            "repeat_of": rep,
            "echoes": " ".join(x for x, _w in sorted(echo.get(u, []))),
            "note": note,
        })

    # Every L2 block must have exactly one first_appearance row.
    for bid, lvl, members, _n in REPEATS:
        if lvl != "L2":
            continue
        n = sum(1 for r in out if r["block_id"] == bid and r["origin_unit"] == r["unit_id"])
        if n != 1:
            die("block %s has %d origin rows, want 1" % (bid, n))

    # Every member of a block must reach the block's subtopic, either as its
    # primary filing or as a cross-filing. A block living only in a subtopic
    # that no member reaches would put the answer in a file that cannot see it.
    everywhere = {}
    for r in rows:
        u = r["unit_id"]
        reach = {filed[u]}
        reach |= {t for t in r["also_subtopics"].split() if t}
        everywhere[u] = reach

    # An L3 entry is a *conceptual* grouping, not a filing: its members sit in
    # different subtopics precisely because they are not the same question. The
    # members are written separately, so reachability is not required. An L2
    # entry is a real merge and must live in one file.
    for bid, lvl, members, _n in REPEATS:
        if lvl != "L2":
            continue
        stragglers = [m for m in members if bid not in everywhere[m]]
        if stragglers:
            die("L2 block %s unreachable from %s (they sit in %s)"
                % (bid, ", ".join(stragglers),
                   ", ".join(sorted(r for m in stragglers
                                    for r in everywhere[m]))))

    with open(OUT, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        w.writerows(out)

    lv = {}
    for r in out:
        lv[r["level"]] = lv.get(r["level"], 0) + 1
    merged = sum(1 for r in out if r["level"] == "L2")
    print("merge_map.csv: %d rows" % len(out))
    print("  L1 %d, L2 %d, L3 %d" % (lv.get("L1", 0), lv.get("L2", 0),
                                     lv.get("L3", 0)))
    print("  L2 units merged into %d blocks" % len(origin_blocks))
    print("  L3 units, each its own block, not merged: %d" % lv.get("L3", 0))
    print("  cross-filed units also listed under a second subtopic: %d"
          % sum(1 for r in out if r["also_subtopics"]))


if __name__ == "__main__":
    main()
