#!/usr/bin/env python3
"""Gate V12: the explanation layer must agree with the exam-style layer on marks
and on the CO/CLO mapping, for every section.

Why this gate exists
--------------------
Two existing gates look like they should already cover this, and neither does.

**V10b rule R3** compares question headings. It *strips* the marks suffix before
comparing, because P2 prints `*[Marks: NN, CO: N]*` on the line under the heading
rather than inside it. So the marks and CO were never part of the comparison.

**V5** compares boxed results. It says nothing about section metadata.

The result was that `2024_explanation.md` carried CO numbers running 1, 2, 3, 4,
5, 6, 7, 8 in sequence down the file, while the 2024 paper prints only CO 1 and
CO 2 and `answers_exam_style/2024_answer.md` uses only those two. Seventeen of
twenty-two sections were wrong, including a fabricated `CO: 8`, and no gate
objected, because a fabricated CO is a plausible-looking number in the right
place in the right format.

All 22 **marks** values happened to be right. Marks are read off the paper and
copied; CO numbers were invented, which is the failure mode this gate closes.

The rule it enforces
-------------------
For every section, in file order:

    P1  `### **(x) question text [Marks: NN, CO: N]**`
    P2  `### **(x) question text**`  followed by  `*[Marks: NN, CO: N]*`

the `NN` and `N` must be equal after normalising `CLO` to `CO`. The count of
sections must match on both sides as well, so a missing or extra section is
caught rather than silently shifting the comparison onto the wrong pair.

Deliberately not enforced: any claim about what the marks mean, whether they are
correctly allocated, or whether a CO mapping is pedagogically sensible. The only
question is whether the two layers agree with each other and with the manifest.

Usage: gate_v12.py [year ...]
"""
import csv
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

HEAD = re.compile(r"(?m)^### \*\*(.+?)\*\*\s*$")
P2_MARKS = re.compile(r"(?m)^\*\[Marks: ([^\]]*)\]\*$")
P1_MARKS = re.compile(r"\[Marks: ([^\]]*)\]")

# 2017 to 2020 and all class tests predate the CLO column, so those sections
# carry marks only. Normalising both sides the same way handles them.
#
# Four spellings of the same field exist across the project, and all four must
# compare equal or the gate reports noise instead of findings:
#
#   `04, CLO1`      the exam-style layer, 2021 to 2023
#   `04, CO: 1`     the explanation layer, and the 2024 exam-style file
#   `CLO1`          the manifest's `co` column, on its own
#   `04`            a pre-OBE section carrying no CO at all
def normalise(s):
    """Reduce any accepted spelling to `NN/CO n`, or to `NN` when there is no CO."""
    if s is None:
        return ""
    t = s.replace(" ", "")
    co = re.search(r"(?:CLO|CO:?):?(\d+)", t)
    n = re.search(r"(\d+)", t)
    if co and n:
        return "%02d/CO%d" % (int(n.group(1)), int(co.group(1)))
    return "%02d" % int(n.group(1)) if n else ""


def manifest_pairs(year):
    """The authority: marks and CO per section, in paper order.

    The manifest's `co` column is not spelled consistently. 2023 stores `CLO1`,
    2024 stores a bare `1`, and the pre-OBE papers store an empty string. A bare
    digit is promoted to `CO: n` so that normalise sees the same shape in every
    case; anything already carrying a label is passed through untouched.
    """
    path = os.path.join(ROOT, "scripts", "answer_manifest.csv")
    rows = [r for r in csv.DictReader(open(path, encoding="utf-8"))
            if r["year"] == year and r["source"] == "paper"]
    rows.sort(key=lambda r: (int(r["question"]), r["part"]))
    out = []
    for r in rows:
        co = (r.get("co") or "").strip()
        if co.isdigit():
            co = "CO: " + co
        out.append(normalise("%s, %s" % (r["marks_part"], co)))
    return out


def main():
    years = sys.argv[1:]
    if not years:
        years = sorted(
            f[:-len("_explanation.md")]
            for f in os.listdir(os.path.join(ROOT, "answers_explanation"))
            if f.endswith("_explanation.md")
        )
    bad = 0
    for year in years:
        p1p = os.path.join(ROOT, "answers_exam_style", year + "_answer.md")
        p2p = os.path.join(ROOT, "answers_explanation", year + "_explanation.md")
        if not os.path.exists(p2p):
            continue
        name = os.path.basename(p2p)
        t1 = open(p1p, encoding="utf-8").read()
        t2 = open(p2p, encoding="utf-8").read()
        a = [normalise(P1_MARKS.search(h).group(1))
             for h in HEAD.findall(t1) if P1_MARKS.search(h)]
        b = [normalise(x) for x in P2_MARKS.findall(t2)]
        if len(a) != len(b):
            print("  %s: section count differs, P1 %d vs P2 %d" % (name, len(a), len(b)))
            bad += 1
            continue
        man = manifest_pairs(year)
        hits = 0
        for i, (x, y) in enumerate(zip(a, b), 1):
            if x != y:
                print("  %s: section %2d  P1 %-10s P2 %-10s" % (name, i, x, y))
                hits += 1
                bad += 1
            if i <= len(man) and y != man[i - 1]:
                print("  %s: section %2d  P2 %-10s manifest %-10s" % (name, i, y, man[i - 1]))
                hits += 1
                bad += 1
        print("%s: %d sections, %d marks/CO disagreements" % (name, len(a), hits))
    print()
    print("V12 GREEN" if bad == 0 else "V12 RED (%d)" % bad)
    return 0 if bad == 0 else 1


if __name__ == "__main__":
    sys.exit(main())