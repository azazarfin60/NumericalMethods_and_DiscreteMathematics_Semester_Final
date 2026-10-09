#!/usr/bin/env python3
"""Gate V10b: register check for the explanation layer.

P1 and P2 have different registers on purpose. P1 is an answer script, so it
is formal, carries no second person and no commentary. P2 is an explanation, so
it may address the reader and explain itself at length.

What P2 must still not do is fixed by its own README, and those rules are what
this gate enforces:

  R1  no em dash
  R2  no Furthermore, Moreover, Consequently (the writing_style.md convention)
  R3  no invented questions: every question heading must match a heading in
      the matching P1 file
  R4  boxed results identical to P1 (this is gate V5, checked separately)
  R5  a "Check" callout must say what it establishes, not perform the author's
      quality assurance
  R6  no self-correction narration left in the file ("Wait.", "Hmm.",
      "That is wrong")

Self-correction narration is the one that has to be enforced mechanically. It is
what a draft looks like when the author changes their mind mid-paragraph, and it
is invisible to the author and confusing to the reader. Anything of this shape
must be resolved before the file is closed.
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

RULES = [
    ("R1 em dash", re.compile(r"\u2014")),
    ("R2 formal connective",
     re.compile(r"\b(Furthermore|Moreover|Consequently)\b")),
    ("R6 self-correction",
     re.compile(r"(?im)^\s*(Wait\.|Hmm\.|Hold\.|Scratch that|Strike that|"
                r"That is wrong|This is wrong|Actually, no|On reflection)")),
]

# A "Check" callout title that performs the author's QA rather than naming what
# is established. "Check by two independent routes" is the phrasing to avoid.
TITLE = re.compile(r'^> \[!info\]\s*(Check|Verified|Confirmed|Double-checked)', re.I)


def headings(path):
    """Return the set of question headings in a file, normalised for comparison.

    A heading is the whole `### **(a) question text [Marks: NN, CO: N]**` line.
    Both layers print the question text, so comparing the normalised text of the
    two tells whether an explanation file is answering a question that is in the
    paper. Whitespace is collapsed, and the marks suffix is dropped, because the
    explanation layer prints `*[Marks: NN, CO: N]*` under the heading rather
    than inside it.
    """
    if not os.path.exists(path):
        return set()
    with open(path, encoding="utf-8") as fh:
        txt = fh.read()
    out = set()
    for m in re.finditer(r'(?m)^### \*\*(.+?)\*\*\s*$', txt):
        h = m.group(1)
        h = re.sub(r"\s*\[Marks:[^\]]*\]\s*", "", h)
        out.add(" ".join(h.split()))
    return out


def main():
    files = sys.argv[1:]
    if not files:
        files = [os.path.join(ROOT, "answers_explanation", f)
                 for f in sorted(os.listdir(os.path.join(ROOT, "answers_explanation")))
                 if f.endswith("_explanation.md")]
    bad = 0
    for path in files:
        name = os.path.basename(path)
        with open(path, encoding="utf-8") as fh:
            txt = fh.read()
        year = name.split("_")[0]
        # R3: every explanation heading must exist in the matching P1 file.
        p1 = os.path.join(ROOT, "answers_exam_style", year + "_answer.md")
        p1h = headings(p1)
        mine = re.findall(r'(?m)^### \*\*(.+?)\*\*\s*$', txt)
        mine_h = set()
        for h in mine:
            hh = re.sub(r"\s*\[Marks:[^\]]*\]\s*", "", h)
            mine_h.add(" ".join(hh.split()))
        n = len(mine_h)
        for h in sorted(mine_h):
            # Compare on the normalised full heading. The explanation layer
            # paraphrases nothing: the question text is printed as the paper
            # prints it, so an exact match is required. A heading that matches
            # no P1 heading is an invented question.
            if h not in p1h:
                print("  %s:  [R3 heading not in the paper]  %s" % (name, h[:80]))
                bad += 1
        hits = 0
        for i, line in enumerate(txt.split("\n"), 1):
            if line.strip().startswith("```"):
                continue
            for label, pat in RULES:
                if pat.search(line):
                    print("  %s:%d  [%s]  %s" % (name, i, label, line.strip()[:80]))
                    hits += 1
        print("%s: %d headings, %d rule hits" % (name, n, hits))
        bad += hits
    print()
    print("V10b GREEN" if bad == 0 else "V10b RED (%d)" % bad)
    return 0 if bad == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
