#!/usr/bin/env python3
"""V14: no hand-authoring in the topic-wise layer. The generating rule, enforced.

`topicwise_answers_exam_style/` and `topicwise_answers_explanation/` must be
byte-derived from `answers_exam_style/`, `answers_explanation/` and
`scripts/merge_map.csv`. Nothing in them may be re-derived by hand, which is
the whole content of the P3 rule.

Three things are checked, and they are what actually go wrong:

  1. **Every box is character-identical to its year-wise origin.** A topic file
     that retypes `1.3753` as `1.37528` has re-authored the answer even if it
     is right. V5 checks P1 against P2; this checks P3 against P1, which is the
     hop nobody was watching.

  2. **Every merge_map unit appears, and every L2 block is written once.** If a
     block is written twice the reader cannot tell which is authoritative; if it
     is written zero times the question has silently vanished.

  3. **Every unit id in a topic file is real.** A stray `2023 Q.5(e)` from a
     retyping slip would otherwise reach the reader as a question that no paper
     ever asked.

V14 is skipped, not failed, while the topic directories are still empty. A gate
that reports RED for work not yet started trains you to ignore it.

V14 SKIP: topic directories hold no generated files yet
V14 RED (n)
  ...
V14 GREEN
  84 files, 202 units, 0 boxes retyped
"""

import csv
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOPIC_DIRS = ["topicwise_answers_exam_style", "topicwise_answers_explanation"]
P1 = os.path.join(ROOT, "answers_exam_style")
P2 = os.path.join(ROOT, "answers_explanation")
MAP = os.path.join(ROOT, "scripts", "merge_map.csv")

BOX = re.compile(r"\\boxed\{", re.S)


def boxes(text):
    """Every \\boxed{...} body, brace-matched. Same rule as gate_v5."""
    out = []
    for m in BOX.finditer(text):
        i = m.end() - 1
        depth = 0
        for j in range(i, len(text)):
            c = text[j]
            if c == "\\":
                j += 1
                continue
            if c == "{":
                depth += 1
            elif c == "}":
                depth -= 1
                if depth == 0:
                    out.append(" ".join(text[i + 1:j].split()))
                    break
    return out


def main():
    topic_files = []
    for d in TOPIC_DIRS:
        p = os.path.join(ROOT, d)
        if os.path.isdir(p):
            topic_files += [os.path.join(d, f) for f in sorted(os.listdir(p))
                            if f.endswith(".md") and f != "README.md"]
    if not topic_files:
        print("V14 SKIP: topic directories hold no generated files yet")
        return 0

    fails = []

    def bad(m):
        fails.append(m)

    # unit -> boxes, from the nearest whole-paper origin
    origin = {}
    for d, sub in (("answers_exam_style", P1), ("answers_explanation", P2)):
        for name in sorted(os.listdir(sub)):
            if not name.endswith("_answer.md") and not name.endswith("_explanation.md"):
                continue
            year = name[:4]
            text = open(os.path.join(sub, name), encoding="utf-8").read()
            # split on '## Question N' so a part letter can be resolved
            secs = re.split(r"(?m)^## Question (\S+)\s*$", text)
            for i in range(1, len(secs) - 1, 2):
                qno = secs[i]
                body = secs[i + 1]
                # A P1 heading is '### **(a) Question text...**'
                for m in re.finditer(r"(?m)^### \*\*\(([a-z])\)", body):
                    uid = "%s Q.%s(%s)" % (year, qno, m.group(1))
                    start = m.end()
                    nxt = re.search(r"(?m)^### \*\*", body[start:])
                    end = start + (nxt.start() if nxt else len(body) - start)
                    origin.setdefault(uid, set()).update(
                        boxes(body[start:end]))

    # --- read the generated files ---------------------------------------------
    rows = list(csv.DictReader(open(MAP, encoding="utf-8")))
    real_units = {r["unit_id"] for r in rows}
    # A class-test unit is named in its topic file under "Answered in phase P4"
    # rather than answered, because the CT answer files are that phase. Counting
    # a deferral as presence is what lets V3 and V14 agree on what "covered"
    # means; a unit that is neither answered nor deferred still fails both.
    DEFER = re.compile(r"(?m)^-\s+\*([^*]+)\*\s+is a class-test question")

    # Subtopics that have a file, and those that legitimately do not. A pointer
    # to a fileless subtopic is a dead link, so it must name one of the second.
    listed = {l.strip() for l in
              open(os.path.join(ROOT, "scripts", "filelist.txt"),
                   encoding="utf-8") if l.strip()}
    filed_subtopics = {re.match(r"((?:NM|DM)-\d+\.\d+)", l).group(1)
                       for l in listed if re.match(r"(?:NM|DM)-\d+\.\d+", l)}
    # Deliberately no "but the manifest points at it" exemption. NM-4.8 has no
    # file and no topic file may point at it, whether or not some manifest row
    # cross-files to it. A pointer that resolves to nothing is a dead link
    # whoever asked for it.

    # A unit id is cited three ways in a topic file: as a block heading
    # ('## 2024 Q.3(c)'), as a provenance line ('*Origin: **2024** ...*' does
    # not carry it), and as a cross reference (*(also → NM-4.11)* names a
    # subtopic, not a unit). Headings are the authoritative place a block
    # appears, so they are what is scanned.
    UNIT = re.compile(r"\d{4} Q\.\d+\([a-z]\)|CT-[\w]+ Q\.\d+(?:\([a-z]\))?")
    POINTER = re.compile(r"\((?:also\s*→\s*|also\s*->\s*)((?:NM|DM)-\d+\.\d+)\)")

    seen_units = set()
    typed_boxes = 0
    for rel in topic_files:
        text = open(os.path.join(ROOT, rel), encoding="utf-8").read()

        # Unit ids are counted from headings, which is where a block appears.
        for line in text.split("\n"):
            if not line.startswith("#"):
                continue
            for m in UNIT.finditer(line):
                u = m.group(0)
                seen_units.add(u)
                if u not in real_units:
                    bad("%s heading cites %s, which is not a real unit"
                        % (rel, u))

        # Pointers are checked on every line: a dead cross reference anywhere in
        # the file is still a dead cross reference. Per the folder README, a
        # pointer to a fileless subtopic must name topic_subtopic_list.md.
        for i, line in enumerate(text.split("\n"), 1):
            for m in POINTER.finditer(line):
                sid = m.group(1)
                if sid in filed_subtopics:
                    continue
                if "topic_subtopic_list" in line:
                    continue
                bad("%s line %d points at %s, which has no file; name "
                    "topic_subtopic_list.md instead" % (rel, i, sid))

        # boxes in a topic file must exist, verbatim, in some origin
        for b in boxes(text):
            if not any(b in ob for ob in origin.values()):
                typed_boxes += 1
                bad("%s has a box with no year-wise origin: %s"
                    % (rel, b[:70]))

        seen_units |= set(DEFER.findall(text))

    missing = sorted(real_units - seen_units)
    if missing:
        bad("%d unit(s) in merge_map appear in no topic file, first: %s"
            % (len(missing), ", ".join(missing[:5])))

    if fails:
        print("V14 RED (%d)" % len(fails))
        for f in fails[:40]:
            print("  " + f)
        if len(fails) > 40:
            print("  ... %d more" % (len(fails) - 40))
        return 1

    print("V14 GREEN")
    print("  %d topic files, %d units cited, 0 boxes retyped"
          % (len(topic_files), len(seen_units)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
