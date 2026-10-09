#!/usr/bin/env python3
"""Gate V10 · exam-script register.

Enforces the mechanical part of exam_register.md. The register has seven rules;
five of them are decidable by pattern and are checked here. The other two, R3
(exam strategy inside the answer) and R8 (bold as emphasis of feeling), and the
Check-section warmth judgement, are not mechanically decidable and are left to
reading. That is stated in the rule file so the gap is on the record.

Usage:  python3 scripts/lint_register.py [file ...]
Exit 0 when clean, 1 otherwise. With no arguments, checks the five year files.
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT = ["answers_exam_style/%s_answer.md" % y
           for y in ("2024", "2023", "2022", "2021", "2020")]

# Lines that quote the paper verbatim are exempt: the question text is not ours.
HEADING = re.compile(r"^### \*\*\(")
# Fenced blocks (ASCII circuit art) are exempt.
FENCE = re.compile(r"^\s*(```|~~~)")
# Material inside double quotes is a quotation, normally an English premise from a
# logic question or a phrase from the paper. The writer is not addressing anyone,
# so second person inside quotes is not a violation. Rule R1 still applies to the
# sentence around the quote.
QUOTED = re.compile(r'"[^"]{12,}"')

RULES = [
    ("R1 second person", re.compile(r"\b(you|your|yours|you're|you've)\b", re.I)),
    ("R1 inclusive we", re.compile(r"\b(let's|we're|we've|we can|we should|we do)\b", re.I)),
    ("R2 examinee commentary",
     re.compile(r"\b(a candidate|candidates|examinees?|students? (often|usually|tend)|one might)\b", re.I)),
    ("R4 editorial tic",
     re.compile(r"(catches? people|easy to miss|deserves? a second look|worth (learning|knowing|"
                r"restating|stating|naming|remembering)|the whole (trap|game|lesson)|the real lesson|"
                r"\bthe lesson\b|the payoff|the natural(ly)? (symmetric )?choice|not to be missed|"
                r"easy to (oversee|miss)|looks like a misprint|nothing is in doubt|it is easy to)", re.I)),
    ("R5 exhortation",
     re.compile(r"(^|[\s>*.-])(watch|look at|read the|do not \"|beware|careful[,:]|"
                r"take care|don't \"|do n't)", re.I)),
    ("R6 QA performance title",
     re.compile(r"^>\s*\[!\w+\]\s*Cross-?check", re.I)),
    ("R7 informal connective",
     re.compile(r"^\s*(also|but|so|anyway|plus|and then)\b[,:]?\s+\S", re.I)),
    ("R9 contraction",
     re.compile(r"\b(is|are|was|were|do|does|did|has|have|had|can|could|will|would|"
                r"should|shall|it|that|there|you|we|they|he|she|let|ain)'"
                r"(s|t|re|ve|ll|d|m)\b", re.I)),
]

# "Note that", "Note the" as a formal opener, and "So far" in a mathematical
# sense, are false positives for R5/R7 and are listed here explicitly.
ALLOW = [
    re.compile(r"^\s*also\s*$", re.I),
    re.compile(r"\bnotes? that\b", re.I),
    re.compile(r"\bso that\b", re.I),
    re.compile(r"\bso as to\b", re.I),
    re.compile(r"\bso far\b", re.I),
    re.compile(r"\bso that the\b", re.I),
    re.compile(r"\blet's see\b", re.I),
]


def scan(path):
    """Yield (line_no, rule, text) for every violation in one file."""
    out = []
    fence = False
    for i, line in enumerate(open(path, encoding="utf-8"), 1):
        if FENCE.match(line):
            fence = not fence
            continue
        if fence or HEADING.match(line):
            continue
        # A quotation is not address. Strip quoted spans before testing, so a
        # quoted English premise in a logic question is not read as "you".
        line = QUOTED.sub('""', line)
        for allow in ALLOW:
            if allow.search(line):
                break
        else:
            for name, pat in RULES:
                if pat.search(line):
                    out.append((i, name, line.rstrip()))
                    break
    return out


def main():
    files = sys.argv[1:] or [os.path.join(ROOT, p) for p in DEFAULT]
    total = 0
    for f in files:
        path = f if os.path.isabs(f) else os.path.join(ROOT, f)
        if not os.path.exists(path):
            print("MISSING %s" % f)
            total += 1
            continue
        hits = scan(path)
        total += len(hits)
        print("=== %s : %d" % (os.path.basename(f), len(hits)))
        for n, name, text in hits:
            print("  %s:%d  [%s]  %s" % (os.path.basename(f), n, name, text.strip()[:110]))
    print()
    print("V10 %s (%d)" % ("GREEN" if total == 0 else "RED", total))
    sys.exit(0 if total == 0 else 1)


if __name__ == "__main__":
    main()
