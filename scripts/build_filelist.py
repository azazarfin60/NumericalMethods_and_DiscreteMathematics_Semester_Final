#!/usr/bin/env python3
"""Derive scripts/filelist.txt from the topic bank. Never hand-edit the filelist.

Two facts come from outside this file:

  * the *title* of each subtopic, from the `## NN-n.n · Title` headings in
    PreviousYearQuestions/topic_wise_sorted_questions.md;
  * the *set* of subtopics that get a file, from
    scripts/subtopics_with_file.txt, which build_manifest.py derives from the
    entry lines in the same bank.

Everything else is here, so the naming rule exists in exactly one place.

Rule, per topicwise_answers_exam_style/README.md (`NM-4.6_Lagrange_Interpolation.md`):

    <ID>_<Title_Case_With_Underscores>.md

    ampersand / slash   -> "and"        Accuracy, Precision & Significant Digits
    hyphen, comma       -> "_"          Least-Squares Linear Regression
    apostrophe          -> dropped      Lagrange's Interpolation
    parenthesis         -> dropped      *(OFF-SYLLABUS)* annotation and "(OFF-SYLLABUS)"
    OFF-SYLLABUS        -> suffix _off_syllabus

Titles are stripped of the bank's own annotations before slugging, so a stray
note in the source cannot leak into a filename. Fails loudly rather than
emitting a duplicate or a bare ID.
"""

import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BANK = os.path.join(ROOT, "PreviousYearQuestions", "topic_wise_sorted_questions.md")
WITH_FILE = os.path.join(ROOT, "scripts", "subtopics_with_file.txt")
OUT = os.path.join(ROOT, "scripts", "filelist.txt")

HEAD = re.compile(r"^##\s+((?:NM|DM)-\d+\.\d+)\s*·\s*(.+?)\s*$")
# The bank annotates out-of-syllabus subtopics inline. That is a note for the
# reader of the bank, never part of the topic's name.
ANNOT = re.compile(r"\s*\*\(.*?\)\*\s*$")
# Words that stay lowercase inside a Title Case slug.
SMALL = {"and", "of", "in", "on", "at", "to", "for", "vs", "the", "a", "an",
         "from", "by", "with", "as"}
# Acronyms keep their capitals: IVP, LU Decomposition, ODE Formulation.
# Plural acronyms keep capitals too: ODEs, PDEs.
ACRONYM = {"ivp", "bvp", "pde", "ode", "lu", "gcd", "lcm", "nr"}


def _cap(w):
    """Capitalise one word, leaving known acronyms and their plurals alone."""
    low = w.lower()
    if low in ACRONYM:
        return low.upper()
    if low.endswith("s") and low[:-1] in ACRONYM:
        return low[:-1].upper() + "s"
    return low[:1].upper() + low[1:]


def _slash(word):
    """`1/3` is a fraction and keeps its digits; a bare `/` token joins words."""
    parts = word.split("/")
    if len(parts) == 2 and parts[0].isdigit() and parts[1].isdigit():
        return ["%s_%s" % (parts[0], parts[1])]
    return [p for p in parts if p]


def slugify(title):
    """Title Case -> underscored slug.  Ill-Conditioned -> Ill_Conditioned."""
    s = ANNOT.sub("", title).strip()
    off = bool(ANNOT.search(title))
    # A colon introduces an explanation, and an arrow a transformation; neither
    # belongs in a filename.
    s = re.sub(r"\s*->\s*|\s*→\s*", " to ", s)
    s = s.replace(":", " ")
    # A spaced slash separates two titles and becomes "and"; an unspaced one is
    # a fraction (Simpson's 1/3 Rule) and must survive as digits.
    s = re.sub(r"\s+/\s+", " and ", s)
    s = (s.replace("&", " and ")
          .replace("-", " ").replace(",", " ").replace("(", " ")
          .replace(")", " ").replace("'", "").replace("’", ""))
    words = []
    for w in re.split(r"\s+", s.strip()):
        words.extend(_slash(w))
    out = []
    for i, w in enumerate(words):
        low = w.lower()
        if "_" in w:                       # 1_3, already shaped
            out.append(w)
        elif low in ACRONYM:
            out.append(_cap(w))
        elif i and low in SMALL:
            out.append(low)
        else:
            out.append(_cap(w))
    slug = "_".join(out)
    if off:
        slug += "_off_syllabus"
    return re.sub(r"_+", "_", slug).strip("_")


def main():
    if not os.path.exists(BANK):
        sys.exit("missing bank: %s" % BANK)
    titles = {}
    for line in open(BANK, encoding="utf-8"):
        m = HEAD.match(line.rstrip("\n"))
        if m:
            titles.setdefault(m.group(1), m.group(2))

    if not os.path.exists(WITH_FILE):
        sys.exit("missing %s -- run build_manifest.py first" % WITH_FILE)
    ids = [l.strip() for l in open(WITH_FILE, encoding="utf-8") if l.strip()]

    missing = [i for i in ids if i not in titles]
    if missing:
        sys.exit("no bank heading for: %s" % ", ".join(missing))

    rows = ["%s_%s" % (i, slugify(titles[i])) for i in ids]

    dupes = {s for s in rows if rows.count(s) > 1}
    if dupes:
        sys.exit("slug collision: %s" % ", ".join(sorted(dupes)))

    bare = [s for s in rows if s.split("_", 1)[1] == ""]
    if bare:
        sys.exit("slugged to a bare ID: %s" % ", ".join(bare))

    # The bank's own reading order: every NM subtopic, then every DM subtopic.
    # Sorting DM first would put discrete mathematics above the numerical
    # methods that the course spends eight papers on.
    FAM = {"NM": 0, "DM": 1}

    def key(s):
        # Match the ID, not the whole slug: the minor number ends at the first
        # underscore, and a slug title carries its own digits ("1_3", "2nd").
        fam, major, minor = re.match(r"((?:NM|DM))-(\d+)\.(\d+)_", s).groups()
        return (FAM[fam], int(major), int(minor))

    rows.sort(key=key)
    with open(OUT, "w", encoding="utf-8") as fh:
        fh.write("\n".join(rows) + "\n")

    print("filelist.txt: %d slugs" % len(rows))
    print("  titles from : %s" % os.path.relpath(BANK, ROOT))
    print("  file set from: %s" % os.path.relpath(WITH_FILE, ROOT))


if __name__ == "__main__":
    main()
