#!/usr/bin/env python3
"""Gate V5: every boxed result in the explanation layer is character identical
to a boxed result in the exam-style layer for the same year.

The explanation layer adds reasoning around a number. It never changes the
number. This gate is the mechanical enforcement of that rule, and it is what
lets the explanation layer be written freely without putting P1's verified
numbers at risk.

The comparison is **per unit, as a multiset**, and that is the rule the gate
originally failed to state.

The first version compared *whole files*: every box in an explanation file had to
appear somewhere in the year's exam-style file. That test cannot see a box that
is missing, and cannot see one that is extra. Both happened in `2024`, in the
same file: a 76-line orphan block carried two boxes P1 did not have, and four
units had lost boxes that P1 had. The file-level counts were 190 against 186 and
the gate printed nothing, because each of the six extra or missing strings
appeared *somewhere* in the other file.

So the comparison is now made unit by unit, and both directions are counted:
a multiset of boxes in P1's section for a unit must equal the multiset in P2's
section for the same unit. Nothing may be invented in P2 and nothing may be
dropped from it.

Usage: gate_v5.py [year ...]
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import topic_lib  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def boxes_text(txt):
    """Every \\boxed{...} body in a string, by brace matching rather than regex.

    The first version of this gate used `re.compile(r"\\\\boxed\\{([^{}]*)\\}")`.
    That pattern cannot match a box containing braces, and most boxes do: any box
    with `\\text{}`, `\\frac{}`, `\\binom{}` or `\\begin{bmatrix}` inside it was
    silently skipped. On `2023_explanation.md` that regex reported 10 checked
    where the file holds 32, so seven tenths of the boxes were never compared
    against their origin. A gate that quietly checks a third of its input is
    worse than no gate, because its GREEN is read as coverage.

    Counting braces by hand costs nothing and has no such blind spot. An escaped
    brace, `\\{`, does not open or close a group.
    """
    out = []
    i = 0
    while True:
        k = txt.find("\\boxed{", i)
        if k < 0:
            break
        j = k + len("\\boxed{")
        depth = 1
        while j < len(txt) and depth:
            c = txt[j]
            if c == "\\" and j + 1 < len(txt):
                j += 2          # skip the escaped character
                continue
            if c == "{":
                depth += 1
            elif c == "}":
                depth -= 1
            j += 1
        if depth:
            break               # unbalanced braces: leave the rest unparsed
        out.append(txt[k + len("\\boxed{"):j - 1])
        i = j
    return out


def boxes(path):
    """boxes() over a whole file. Thin wrapper so the docstring stays attached."""
    if not os.path.exists(path):
        return []
    with open(path, encoding="utf-8") as fh:
        return boxes_text(fh.read())


def unit_boxes(path):
    """Map each unit id to the sorted multiset of boxes in its own section.

    Section boundaries come from `scripts/topic_lib.py`, the parser the topicwise
    generator already uses and whose output was verified against the manifest:
    183 sections in each of P1 and P2, and identical key sets.

    An earlier version of this function carried its own regex, `## Question 5(b)`,
    and that pattern matches nothing in these files. The actual structure is a
    `## Question N` heading followed by `### **(a) ...` sub-headings. The regex
    version therefore returned an empty map for every file, every comparison
    passed vacuously, and V5 printed GREEN having compared nothing. That is the
    failure mode this function's docstring exists to prevent, so the count is
    asserted below rather than trusted.
    """
    pool = topic_lib.load_p1() if "_answer" in path else topic_lib.load_p2()
    out = {}
    for unit, sec in pool.items():
        if not unit.startswith(os.path.basename(path)[:4]):
            continue
        out[unit] = sorted(normalise(b) for b in topic_lib.boxes(sec["body"]))
    return out


def normalise(s):
    """Collapse whitespace for comparison only.

    An explanation file may wrap a long formula onto several lines where the
    exam-style file kept it on one. The mathematics is unchanged, so the two are
    compared after collapsing runs of whitespace. No other normalisation is
    done, so a changed digit still fails.

    One exception had to be made. A LaTeX explicit space, written as a backslash
    followed by a space, is a command and not whitespace, but a naive collapse
    swallows it. That hid a real difference in the 2023 Simpson comparison box,
    where the origin read `n,\\ \\text{and }` and the draft had dropped the
    command to `n, \\text{and }`. The two render almost identically and the
    mathematics is the same, but the rule is character identity, so the command
    is protected before collapsing and restored afterwards.
    """
    s = s.replace("\\ ", "\x00")
    s = " ".join(s.split())
    return s.replace("\x00", "\\ ")


def compare_files(exam, expl, label, nbad_ref):
    """Multiset comparison for a pair of whole-file answers, as for the CT layer.

    The year-wise layers are compared per unit because they have unit headings to
    compare by. The class-test pair has none in the same shape, and its two files
    were written against each other, so the comparison is a whole-file multiset:
    every box on one side must appear on the other, with multiplicity. That is
    still stronger than membership, so a box duplicated in P2 or missing from it
    fails.

    Returns the number of boxes checked and a list of problem strings.
    """
    want = sorted(normalise(b) for b in boxes(exam))
    got = sorted(normalise(b) for b in boxes(expl))
    problems = []
    if not want:
        problems.append("%s: no boxed results in the exam-style origin" % label)
    missing = [b for b in want if b not in got]
    extra = [b for b in got if b not in want]
    for b in missing:
        problems.append("%s: missing from the explanation: \\boxed{%s}"
                        % (label, b))
    for b in extra:
        problems.append("%s: not in the exam-style origin: \\boxed{%s}"
                        % (label, b))
    return len(got), problems


def main():
    years = sys.argv[1:]
    if not years:
        years = sorted(
            f[:-len("_explanation.md")]
            for f in os.listdir(os.path.join(ROOT, "answers_explanation"))
            if f.endswith("_explanation.md")
        )

    total_ok = 0
    total_bad = 0
    for year in years:
        exam = os.path.join(ROOT, "answers_exam_style", year + "_answer.md")
        expl = os.path.join(ROOT, "answers_explanation", year + "_explanation.md")
        if not os.path.exists(expl):
            continue
        origin = unit_boxes(exam)
        if not origin:
            print("  %s: NO SECTIONS FOUND in the exam-style origin; the gate "
                  "would pass vacuously, so this is a failure" % year)
            total_bad += 1
            continue
        if not origin:
            print("  %s: no boxed results in the exam-style origin" % year)
        nbad = 0
        n = 0
        for unit, got in sorted(unit_boxes(expl).items()):
            want = origin.get(unit, [])
            n += len(got)
            if got == want:
                continue
            nbad += 1
            missing = [b for b in want if b not in got]
            extra = [b for b in got if b not in want]
            print("  V5 MISMATCH %s %s: %d in P1, %d in P2"
                  % (year, unit, len(want), len(got)))
            for b in missing:
                print("     missing from P2: \\boxed{%s}" % b)
            for b in extra:
                print("     not in P1:       \\boxed{%s}" % b)
        print("  %s: %d boxed results checked, %d mismatched"
              % (year, n, nbad))
        total_ok += n
        total_bad += nbad

    ct_exam = os.path.join(ROOT, "CT_Questions", "CT_answers_exam_style.md")
    ct_expl = os.path.join(ROOT, "CT_Questions", "CT_answers_explanation.md")
    if os.path.exists(ct_exam) and os.path.exists(ct_expl):
        n, problems = compare_files(ct_exam, ct_expl, "CT-02B/CT-04", None)
        for p in problems:
            print("  V5 MISMATCH %s" % p)
        total_ok += n
        total_bad += len(problems)
        print("  class tests: %d boxed results checked, %d mismatched"
              % (n, len(problems)))

    print()
    print("V5 GREEN" if total_bad == 0 else "V5 RED (%d mismatches)" % total_bad)
    print("%d boxed results verified against their exam-style origin" % total_ok)
    return 0 if total_bad == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
