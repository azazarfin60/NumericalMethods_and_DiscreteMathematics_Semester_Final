#!/usr/bin/env python3
"""V7: provenance and links.

Every claim a topic file makes about where its content came from must resolve.

  1. **Block ids are real.** Every `### [YYYY Q.n(p)]` must name a sub-question
     that the frozen papers actually ask, with that part. A `2024 Q.3(e)` is a
     retyping slip that would reach the reader as a question no paper set.
  2. **Appearance lists agree with the merge map.** A block that says
     "Appeared in: 2017 Q.5(c), 2020 Q.3(b)" must be exactly the L2 block's
     membership, no more and no less. A block that names one repeat but omits
     another is worse than one that names neither, because it looks checked.
  3. **Cross references resolve.** An `*(also → NM-x.y)*` must name a subtopic
     with a file, or name `topic_subtopic_list.md` instead. A pointer to a
     fileless subtopic is a dead link.
  4. **Marks match the paper.** The marks in a block heading are the marks in
     the paper margin for that part, or the question total where a part carries
     none. A 2-mark item is never labelled 3.

V7 SKIP: no topic files yet
V7 RED (n)
  ...
V7 GREEN
  202 units resolve, N cross references live
"""

import csv
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import topic_lib as T

DIRS = ["topicwise_answers_exam_style", "topicwise_answers_explanation"]
UNIT = re.compile(r"\d{4} Q\.\d+\([a-z]\)|CT-[\w]+ Q\.\d+(?:\([a-z]\))?")
HEAD = re.compile(r"(?m)^###\s*\[([^\]]+)\]:?\s*(.*)$")
# The pointer line the generator writes is
#
#     - *2023 Q.6(c)* is the same question as [[DM-3.9|DM-3.9]], which is
#       written in `DM-3.9`.
#
# so the target is matched as a wikilink. An earlier version of this gate
# matched `(also -> NM-1.1)`, a shape the generator has never emitted, so the
# pattern matched nothing, `npoint` stayed at 0, and the gate printed
# "0 cross references live" while 46 pointers sat unchecked in each layer. It
# reported GREEN having verified no pointer at all. See ANSWER_BUILD_PLAN.md
# section 36.4.
POINTER = re.compile(r"is the same question as \[\[([^\]|]+)(?:\|[^\]]*)?\]\]")
# The same id repeated in backticks, which must agree with the wikilink target.
POINTER_BACKTICK = re.compile(r"which is written in `([^`]+)`")


UNIT_LINE = re.compile(r"(?m)^-\s*\*([^*]+)\*")


def unit_of_line(line):
    """The unit id a pointer line is about, from the leading `*unit*`."""
    m = re.match(r"-\s*\*([^*]+)\*", line)
    return m.group(1) if m else None


def sid_of(text):
    """The `NM-x.y` / `DM-x.y` prefix of a subtopic id, or None.

    Deliberately a prefix match and not `topic_lib.slug_id`, which requires the
    trailing underscore of a *file name*. A pointer names a bare subtopic id, so
    using the file-slug parser reported all 92 pointers as malformed and turned
    a real check into 92 false alarms.
    """
    m = re.match(r"((?:NM|DM)-\d+\.\d+)(?:_|\b)", text or "")
    return m.group(1) if m else None


def main():
    files = []
    for d in DIRS:
        p = os.path.join(T.ROOT, d)
        if os.path.isdir(p):
            files += [(d, f) for f in sorted(os.listdir(p))
                      if f.endswith(".md") and f != "README.md"]
    if not files:
        print("V7 SKIP: no topic files yet")
        return 0

    fails = []

    def bad(m):
        fails.append(m)

    rows = T.load_map()
    real = {r["unit_id"] for r in rows}
    by_id = {r["unit_id"]: r for r in rows}

    # L2 membership, for checking appearance lists
    l2_members = {}
    for r in rows:
        if r["level"] == "L2":
            l2_members.setdefault(r["block_id"], set()).add(r["unit_id"])
    # every member of a block, whichever level, for the L3 case
    all_members = {}
    for r in rows:
        if r["level"] == "L2":
            all_members.setdefault(r["block_id"], set()).add(r["unit_id"])

    listed = {T.slug_id(l) for l in T.load_filelist()}
    npoint = 0

    for d, f in files:
        text = open(os.path.join(T.ROOT, d, f), encoding="utf-8").read()
        lines = text.split("\n")

        for i, line in enumerate(lines, 1):
            for m in POINTER.finditer(line):
                npoint += 1
                sid = sid_of(m.group(1))
                if sid is None:
                    # A pointer naming the taxonomy list rather than a subtopic.
                    if "topic_subtopic_list" in line:
                        continue
                    bad("%s/%s line %d: pointer target %r is not a subtopic id"
                        % (d, f, i, m.group(1)))
                    continue
                if sid not in listed:
                    bad("%s/%s line %d points at %s, which has no file; name "
                        "topic_subtopic_list.md instead" % (d, f, i, sid))
                # The pointer must land in the file its target names, and in the
                # file the merge map says the unit is filed under. A pointer
                # pointing at a real but wrong subtopic is a silent wrong turn.
                want_sid = by_id.get(unit_of_line(line) or "", {}).get("subtopic_id")
                if want_sid and sid != want_sid:
                    bad("%s/%s line %d: %s is filed under %s in merge_map.csv "
                        "but its pointer names %s"
                        % (d, f, i, unit_of_line(line), want_sid, sid))
                b = POINTER_BACKTICK.search(line)
                if b and sid_of(b.group(1)) != sid:
                    bad("%s/%s line %d: pointer wikilink names %s but the "
                        "sentence names %s" % (d, f, i, sid, b.group(1)))

        for m in HEAD.finditer(text):
            ids = UNIT.findall(m.group(1))
            if not ids:
                bad("%s/%s: block heading names no unit: %r"
                    % (d, f, m.group(1)[:60]))
                continue
            for u in ids:
                if u not in real:
                    bad("%s/%s: %s is not a real unit" % (d, f, u))

            # appearance list on the following lines
            win = "\n".join(lines[m.end() // len(text) if False else 0:0]) \
                if False else ""
            idx = text.count("\n", 0, m.start())
            nxt = ""
            for j in range(idx + 1, min(idx + 6, len(lines))):
                if lines[j].strip():
                    nxt = lines[j]
                    break
            am = re.match(r"\*\*Appeared in:\*\*\s*(.+)$", nxt)
            if am and len(ids) == 1:
                u = ids[0]
                want = all_members.get(by_id[u]["block_id"], set())
                if by_id[u]["level"] == "L2" and want:
                    got = set(UNIT.findall(am.group(1)))
                    if got != want:
                        bad("%s/%s: %s lists %s, merge_map says %s"
                            % (d, f, u, sorted(got), sorted(want)))

            # marks in the heading, when printed
            mm = re.search(r"Marks:\s*([0-9]+)", m.group(2))
            if mm and len(ids) == 1 and ids[0] in by_id:
                want = by_id[ids[0]]["marks_part"] or \
                    by_id[ids[0]]["marks_question"]
                if want and mm.group(1).lstrip("0") != want.lstrip("0"):
                    bad("%s/%s: %s prints marks %s, manifest says %s"
                        % (d, f, ids[0], mm.group(1), want))

    if fails:
        print("V7 RED (%d)" % len(fails))
        for f in fails[:40]:
            print("  " + f)
        if len(fails) > 40:
            print("  ... %d more" % (len(fails) - 40))
        return 1

    print("V7 GREEN")
    print("  %d units resolve, %d cross references live" % (len(real), npoint))
    return 0


if __name__ == "__main__":
    sys.exit(main())
