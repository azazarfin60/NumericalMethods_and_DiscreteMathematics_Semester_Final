#!/usr/bin/env python3
"""Generate the topic-wise layer. 84 files per folder, twice, from one map.

Reads `answers_exam_style/`, `answers_explanation/` and `scripts/merge_map.csv`.
Writes nothing that is not copied: every block body is the year-wise body with
its `---` fence and heading stripped, character for character. No number is
retyped, no box is invented, no question is re-answered.

Three rules decide the output:

  * **L1** one appearance. Its own block, in the file of its own subtopic.
  * **L2** same method and structure, numbers changed. One block, written from
    the *earliest* appearance, carrying an "Appeared in" list of every member.
    The later appearances are named, not re-answered.
  * **L3** same topic only. Never merged. Each member is its own block, and the
    topic file shows them in sequence, because a reader revising one subtopic
    wants all of them.

A unit cross-filed under a second subtopic is written **in full** in the file
of its block, and **referenced by a cross-reference line** in the other file.
Writing it twice would be the 2207 defect; omitting it would be V3's omission.

Usage:  python3 scripts/gen_topicwise.py [--only-exam | --only-expl]
"""

import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import topic_lib as T

EXAM_DIR = "topicwise_answers_exam_style"
EXPL_DIR = "topicwise_answers_explanation"

FRONT = """---
title: "{sid} · {title}"
tags:
  - numerical-methods
  - discrete-mathematics
  - topicwise
---

# {sid} · {title}

{blurb}

"""

BLURB_EXAM = """Every block below is copied from `../answers_exam_style/`, which is the
only place an answer is authored. A number here is the same number, character
for character, as the one it came from."""

BLURB_EXPL = """Every block below is copied from `../answers_explanation/`. The reasoning
is written once, in the year-wise file, and is not restated here."""

# A section divider inside a year-wise body. It belongs to the paper, not to a
# subtopic file, so it is dropped rather than reproduced: in a topic file it
# would assert a boundary that has nothing to do with the subtopic.
SECTION = re.compile(r"(?m)^#\s+SECTION\s+[AB]\s*$")
# Trailing prose of the year-wise answer that refers to another paper by number.
# In a subtopic file the reader has no list of papers to resolve "another paper"
# against, and the block already carries its own "Appeared in" line, so the
# sentence is dropped rather than left pointing at nothing.
CROSSREF = re.compile(
    r"(?:>\s*)?\[[!]\w+\]\s*[^\n]*\b(?:another paper|another year)\b"
    r"[^\n]*(?:\n>[^\n]*)*\n"
    r"|(?:>\s*)?\**[^\n]*\bidentical\b[^\n]*\b(?:paper|question as)\b"
    r"[^\n]*(?:\n>[^\n]*)*\n")


def clean_body(body):
    """Drop the year-wise section's own front matter and its trailing fence."""
    b = body.strip("\n")
    # a P2 body begins with its `*[Marks: ..]*` line, which the block header
    # already carries, so lift it out and return it separately
    marks = ""
    m = re.match(r"^\*\[Marks:\s*([^\]]*)\]\*\s*\n", b)
    if m:
        marks = m.group(1)
        b = b[m.end():]
    b = re.sub(r"\n*---\s*$", "", b).rstrip()
    b = SECTION.sub("", b)
    b = CROSSREF.sub("", b)
    b = re.sub(r"\n{3,}", "\n\n", b)
    return marks, b.strip("\n")


def origin_yearq(uid):
    """Sort key for a unit id: (year, question number, part).

    Class-test ids look like `CT-02B Q.1(b)` and sort after every paper, which
    is the right place for them since they were never in a past paper.
    """
    m = re.match(r"(\d{4}) Q\.(\d+)(?:\(([a-z])\))?$", uid)
    if m:
        return (int(m.group(1)), int(m.group(2)), m.group(3) or "a")
    m = re.match(r"CT-([\w]+) Q\.(\d+)(?:\(([a-z])\))?$", uid)
    if m:
        return (9000 + int(m.group(2)), 0, m.group(3) or m.group(1))
    raise SystemExit("unrecognised unit id: %r" % uid)


def build(subtopic_id, rows, src, blurb):
    """Return the file text for one subtopic."""
    title = T.title_of(subtopic_id)
    here = [r for r in rows if r["subtopic_id"] == subtopic_id]

    # A unit is written in full in exactly one file: the one it is *filed*
    # under, its `subtopic_id`. A subtopic that reaches it only through
    # `also_subtopics` gets a reference line, never a second copy of the answer.
    #
    # The block id is the subtopic of the *earliest member*, which need not be
    # where any member is filed: the Liebmann block is NM-10.4 while both its
    # members are filed under NM-10.2. The filing decides the home, and the
    # block id only has to be a subtopic with a file.
    blocks = {}
    refs = []

    filed_here = {r["unit_id"] for r in here}
    for r in here:
        u, bid = r["unit_id"], r["block_id"]
        # A repeat of a block already written in *this* file is named in that
        # block's "Appeared in" line. It needs no pointer here, and emitting one
        # would point the subtopic at itself.
        if r["level"] == "L2" and r["repeat_of"]:
            if r["repeat_of"] in filed_here:
                continue
            refs.append((u, bid))
            continue
        blocks.setdefault(bid, []).append(u)

    # An L2 repeat filed in a second subtopic belongs to the same block, so its
    # file has to show the whole block. Collecting members by block id across
    # every row is what keeps an "Appeared in" list complete on both sides.
    for r in rows:
        if r["level"] == "L2" and r["subtopic_id"] == subtopic_id:
            blocks.setdefault(r["block_id"], []).append(r["unit_id"])

    for r in rows:
        # Filed elsewhere but reachable from here. NM-3.8, NM-5.6, NM-5.7 and
        # NM-10.4 are never a primary filing, so they hold entry lines and a
        # file and yet own no block of their own: every unit that reaches them
        # is written in the subtopic it is filed under. Such a file gets a
        # pointer, and V3 accepts a pointer-only file as covered.
        #
        # The anchor rule below is deliberately *not* applied when the members
        # are filed elsewhere. An earlier version wrote the block a second time
        # in the anchor's file, which is the exact double-answer V3 exists to
        # catch: 2020 Q.4(b) appeared in full in both NM-3.5 and NM-3.8.
        if subtopic_id in r["also_subtopics"].split():
            refs.append((r["unit_id"], r["subtopic_id"]))

    blocks = {b: sorted(set(v), key=origin_yearq) for b, v in blocks.items()}
    refs = sorted(set(refs), key=lambda x: origin_yearq(x[0]))

    out = [FRONT.format(sid=subtopic_id, title=title, blurb=blurb)]
    written = 0

    ordered = sorted(blocks.items(),
                     key=lambda kv: origin_yearq(min(kv[1], key=origin_yearq)))

    deferred = []

    for bid, members in ordered:
        origin = min(members, key=origin_yearq)
        secs = sorted(members, key=origin_yearq)
        sec = src.get(origin)
        if sec is None:
            # A class-test unit has no year-wise section: the class tests are
            # answered in P6, in CT_Questions/, not in the year-wise folders, so
            # src has no section for it. The unit is named here so the omission
            # is visible in the file rather than silent, and V3 counts it as
            # covered by the deferral rather than as answered in place.
            deferred.extend(secs)
            continue
        marks, body = clean_body(sec["body"])
        qtext = sec["question"]

        # The heading carries only the unit ids. A title after the colon would
        # have to be identical in both folders for V4 to pass, and the two
        # layers legitimately phrase the same question differently, so the
        # heading stays skeletal and the question text sits below it.
        head = "### [%s]" % ", ".join(secs)
        out.append(head)
        out.append("")
        if len(secs) > 1:
            out.append("**Appeared in:** %s" % ", ".join(secs))
            out.append("")
        out.append("**Question.** %s" % qtext)
        out.append("")
        if marks:
            out.append("*[Marks: %s]*" % marks)
            out.append("")
        out.append("**Solution.**")
        out.append("")
        out.append(body)
        out.append("")
        out.append("---")
        out.append("")
        written += len(secs)

    if refs:
        out.append("---")
        out.append("")
        if written == 0:
            # Every unit reaching this subtopic is written in another one, so
            # saying so is more use than an empty heading would be.
            out.append("**Every question that reaches this subtopic is written "
                       "in the subtopic it is filed under.** Nothing is "
                       "answered here, and that is deliberate rather than an "
                       "omission: the subtopic holds the questions in the "
                       "taxonomy but owns no block of its own.")
        else:
            out.append("**Also asked here.**")
        out.append("")
        for u, bid in sorted(refs, key=lambda x: origin_yearq(x[0])):
            if bid == subtopic_id:
                out.append("- *%s* is written in this file, above." % u)
            else:
                out.append("- *%s* is the same question as [[%s|%s]], which is "
                           "written in `%s`." % (u, bid, bid, bid))
        out.append("")
        out.append("---")
        out.append("")

    if deferred:
        out.append("**Answered in phase P6, in `../CT_Questions/`.**")
        out.append("")
        for u in sorted(deferred, key=origin_yearq):
            out.append("- *%s* is a class-test question. Its answer is in "
                       "`../CT_Questions/CT_answers_exam_style.md`, with the "
                       "reasoning in `../CT_Questions/CT_answers_explanation.md`."
                       % u)
        out.append("")

    return "\n".join(out).rstrip() + "\n", written, len(refs), sorted(deferred)


def first_clause(qtext):
    """A short label for the block heading, from the question's own words."""
    s = re.split(r"(?<=[.?])\s", qtext.strip())[0]
    s = re.sub(r"\$[^$]*\$", "", s).strip()
    s = re.sub(r"\s+", " ", s).rstrip(".?")
    if len(s) > 58:
        cut = s[:58].rsplit(" ", 1)[0]
        s = cut + "..."
    return s


def main():
    only = None
    if "--only-exam" in sys.argv:
        only = EXAM_DIR
    elif "--only-expl" in sys.argv:
        only = EXPL_DIR

    rows = T.load_map()
    p1, p2 = T.load_p1(), T.load_p2()
    jobs = [(EXAM_DIR, p1, BLURB_EXAM), (EXPL_DIR, p2, BLURB_EXPL)]
    if only:
        jobs = [j for j in jobs if j[0] == only]

    grand = 0
    for folder, src, blurb in jobs:
        path = os.path.join(T.ROOT, folder)
        os.makedirs(os.path.join(path, "diagrams"), exist_ok=True)
        keep = {"README.md"}
        total = written = refcount = 0
        pend = []
        for slug in T.load_filelist():
            sid = T.slug_id(slug)
            text, w, rc, p = build(sid, rows, src, blurb)
            open(os.path.join(path, slug + ".md"), "w",
                 encoding="utf-8").write(text)
            keep.add(slug + ".md")
            total += 1
            written += w
            refcount += rc
            pend += p
        # remove anything a previous run generated that is no longer in the list
        for f in sorted(os.listdir(path)):
            if f.endswith(".md") and f not in keep:
                os.remove(os.path.join(path, f))
                print("  removed stale %s/%s" % (folder, f))
        print("%s: %d files, %d units written, %d cross references"
              % (folder, total, written, refcount))
        if pend:
            print("  %d class-test units deferred to P6: %s"
                  % (len(pend), ", ".join(sorted(set(pend)))))
        grand += written

    print("total units written: %d" % grand)


if __name__ == "__main__":
    main()
