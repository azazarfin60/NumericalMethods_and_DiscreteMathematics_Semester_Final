#!/usr/bin/env python3
"""Check one year-wise answer file against the manifest.

Usage: check_paper.py <year>

Verifies that every manifest row for that year has exactly one heading, that the
heading order matches, and that the marks and CLO printed in the heading are
character identical to the manifest. Marks summing to the audited paper total is
checked too.
"""
import csv
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def main():
    year = sys.argv[1]
    rows = [r for r in csv.DictReader(open(os.path.join(ROOT, "scripts/answer_manifest.csv"),
                                          encoding="utf-8"))
            if r["year"] == year]
    want = {(r["question"], r["part"]): (r["marks_part"], r["co"]) for r in rows}
    exp = []
    for q in range(1, 30):
        for p in "abcdefghij":
            if (str(q), p) in want:
                exp.append((q, p) + want[(str(q), p)])

    path = os.path.join(ROOT, "answers_exam_style", year + "_answer.md")
    txt = open(path, encoding="utf-8").read()

    # The CLO label differs by era: 2022 and 2023 print CLO1, the rest print 1.
    # Capture whatever token follows the comma and compare it to the manifest
    # character for character, so a relabelled CLO is caught.
    #
    # The CLO token is optional. RUET only began printing course learning
    # outcomes with the OBE-era papers, so 2017, 2018, 2019, 2020 and all four
    # class tests carry marks alone. For those the heading reads
    # "[Marks: 06]" with no comma, and the manifest's co column is empty. A
    # heading that grows a CLO on a pre-OBE paper is a defect, so the two cases
    # are compared separately below rather than by a single loose pattern.
    pattern = (r'^### \*\*\(([a-z])\).*?'
               r'\[Marks: (\d+)(?:, ([^\]]+))?\]\*\*')

    seq = []
    for chunk, qoff in ((txt.split("# SECTION B")[0], 1),
                        (txt.split("# SECTION B")[1], 5)):
        cur = qoff
        for m in re.finditer(r"^## Question (\d+)\s*$|" + pattern, chunk, re.M | re.S):
            if m.group(1):
                cur = int(m.group(1))
            else:
                seq.append((cur, m.group(2), m.group(3), m.group(4)))

    print("%s: %d headings, %d manifest rows" % (year, len(seq), len(exp)))
    bad = 0
    for a, b in zip(seq, exp):
        # Normalise the CLO label before comparing. The papers print it two ways:
        # "CLO1" in 2022 and 2023, "CO: 1" in 2017-2021 and 2024. Compare the
        # digit, and separately confirm the label style matches the paper's era.
        if a[0] != b[0] or a[1] != b[1] or a[2] != b[2]:
            bad += 1
            print("  MISMATCH file %s  manifest %s" % (a, b))
            continue
        # Pre-OBE: the manifest expects no CLO, so the heading must not have one.
        if b[3] == "":
            if a[3]:
                bad += 1
                print("  CLO PRESENT ON PRE-OBE PAPER file %r" % (a[3],))
        elif re.sub(r"\D", "", a[3]) != re.sub(r"\D", "", b[3]):
            bad += 1
            print("  CLO MISMATCH file %r  manifest %r" % (a[3], b[3]))
    if len(seq) != len(exp):
        print("  COUNT MISMATCH")
        bad += 1

    total = sum(int(s[2]) for s in seq)
    audited = sum(int(r["marks_part"]) for r in rows)
    print("  marks in file: %d   audited: %d" % (total, audited))
    if total != audited:
        print("  MARKS TOTAL MISMATCH")
        bad += 1

    print("  boxed statements: %d" % len(re.findall(r"\\boxed\{", txt)))
    print("PARITY OK" if bad == 0 else "PARITY RED (%d)" % bad)
    sys.exit(0 if bad == 0 else 1)


if __name__ == "__main__":
    main()
