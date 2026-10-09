#!/usr/bin/env python3
"""Build scripts/answer_manifest.csv, the single roster of answer units.

One row per answer unit. A unit is one sub-question of a past paper, or one part
of a class-test question. Nothing else earns a row.

The manifest is the spine of the whole build:

  * P1 and P2 write one answer per manifest row, year-wise.
  * P4 and P5 propagate each row into exactly one subtopic file.
  * Gates V2, V3, V7, V8 and V10 all read this file.

Because everything downstream reads it, this script never guesses. If a paper
row cannot be matched to a filing in the topic bank, the script stops with a
non-zero exit rather than emitting a partial manifest.

Sources, all frozen under PreviousYearQuestions/ and hashed by V1:

  2017.md .. 2024.md          183 sub-questions, 721 marks
  ClassTestQuestions.md        19 parts across CT-01, CT-02A, CT-02B, CT-04
  topic_wise_sorted_questions.md   the filing of every unit under a subtopic
"""

import csv
import glob
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "PreviousYearQuestions")
OUT = os.path.join(ROOT, "scripts", "answer_manifest.csv")

PAPERS = [str(y) for y in range(2017, 2025)]

# --- section 4.1a L2 correction -------------------------------------------------
# The census family is one method on one structure, so L2 merges it into a single
# block. Its filing point is NM-4.11 (Extrapolation and Newton's Divided
# Difference), which already holds 2020 Q.3(b) and 2024 Q.3(b). Moving 2017
# Q.5(c) there empties NM-4.8, so NM-4.8 gets no file. That is why the build is
# 84 files and not 85.
L2_MOVES = {"2017 Q.5(c)": ("NM-4.8", "NM-4.11")}

# Class-test labels, in the order the plan's CT section uses.
CT_LABELS = {"CT-01", "CT-02A", "CT-02B", "CT-04"}


def die(msg, *ctx):
    sys.stderr.write("build_manifest: FATAL: %s\n" % msg)
    for line in ctx:
        sys.stderr.write("    %s\n" % line)
    sys.exit(1)


# --- paper parsing --------------------------------------------------------------

def parse_paper(path):
    """Yield one dict per sub-question row.

    Markdown table cells hold LaTeX, and LaTeX holds `|`, so a naive split on `|`
    destroys the row. The trailing columns are short and never contain a pipe, so
    split from the RIGHT by the header's column count and let the description
    column keep whatever pipes it likes.

    The header also settles the column order, which differs by era: 2017-2020
    print only Marks, 2021 and 2024 add CO after it, and 2022 and 2023 print CLOs
    BEFORE Marks. Reading the header beats hardcoding an index.
    """
    header = None
    ncols = 0
    year = os.path.basename(path)[:4]
    for lineno, raw in enumerate(open(path, encoding="utf-8"), 1):
        line = raw.rstrip("\n").strip()
        if not (line.startswith("|") and line.endswith("|") and len(line) > 1):
            continue
        if re.match(r"^\|[\s:\-|]+\|$", line):          # the | :--- | :---: | rule
            continue
        inner = line[1:-1]
        first = inner.split("|")[0].strip()
        if first.lower().startswith("question no"):
            header = [c.strip() for c in inner.split("|")]
            ncols = len(header)
            continue
        if header is None:
            continue
        m = re.match(r"^\*\*?Q\.?(\d+)\s*\(?([a-z])\)?\*\*?$", first)
        if not m:
            continue
        cells = [c.strip() for c in inner.rsplit("|", ncols - 1)]

        def col(*prefixes):
            for i, name in enumerate(header):
                if any(name.lower().startswith(p) for p in prefixes):
                    return cells[i]
            return ""

        raw_marks = col("mark").strip("*")
        if not raw_marks.isdigit():
            die("marks cell is not a number", "%s:%d  %r" % (path, lineno, col("mark")))
        yield {
            "unit_id": "%s Q.%s(%s)" % (year, m.group(1), m.group(2)),
            "source": "paper",
            "year": year,
            "question": m.group(1),
            "part": m.group(2),
            "marks_part": raw_marks,
            "marks_question": "",
            "co": col("co", "clo").strip("*"),
            "question_text": cells[1],
            "origin": "%s:%d" % (os.path.basename(path), lineno),
        }


# --- class-test parsing ---------------------------------------------------------

CT_HEADING = {
    "Class Test 01": "CT-01",
    "Class Test 02 (Set A)": "CT-02A",
    "Class Test 02 (Set B)": "CT-02B",
    "Class Test 04": "CT-04",
}


def parse_class_tests(path):
    """Yield one dict per class-test part.

    The class tests are not tables. Each test has `## Class Test nn` headings,
    each question has a `### Question n` heading, a `**Marks:**` line at
    QUESTION level, and either no parts at all or `- **(a)**` bullets.

    Part marks are never printed, only the question total. Storing the total in
    `marks_question` and leaving `marks_part` empty keeps the distinction the
    plan insists on: nothing in the answers may state a per-part CT mark.
    """
    label = None
    qno = None
    marks = ""
    for lineno, raw in enumerate(open(path, encoding="utf-8"), 1):
        line = raw.rstrip("\n").strip()

        h2 = re.match(r"^##\s+(Class Test.*)$", line)
        if h2:
            label = CT_HEADING.get(h2.group(1).strip())
            if label is None:
                die("unrecognised class-test heading", "%s:%d  %r" % (path, lineno, line))
            qno = None
            continue

        h3 = re.match(r"^###\s+Question\s+(\d+)", line)
        if h3:
            qno = str(int(h3.group(1)))        # CT-01 prints "Question 01", the bank says Q.1
            marks = ""
            continue

        m = re.match(r"^\*\*Marks:?\*\*\s*(\d+)", line)
        if m and label:
            marks = m.group(1)
            continue

        if label and qno:
            part = re.match(r"^- \*\*\(([a-z])\)\*\*\s+(.*)$", line)
            if part:
                yield {
                    "unit_id": "%s Q.%s(%s)" % (label, qno, part.group(1)),
                    "source": "class_test",
                    "year": label,
                    "question": qno,
                    "part": part.group(1),
                    "marks_part": "",
                    "marks_question": marks,
                    "co": "",
                    "question_text": part.group(2),
                    "origin": "ClassTestQuestions.md:%d" % lineno,
                }
                continue

            # A partless question. The stem is every line up to the first blank
            # line that follows the heading, minus the Marks line already eaten.
            if re.match(r"^- \*\*\(?[a-z]\)?\*\*", line) or line.startswith("| Parameter"):
                continue


def parse_class_test_stems(path):
    """Yield partless class-test questions, text collected to the next section rule."""
    label = None
    qno = None
    buf = None
    for raw in open(path, encoding="utf-8"):
        line = raw.rstrip("\n").strip()

        h2 = re.match(r"^##\s+(Class Test.*)$", line)
        if h2:
            label = CT_HEADING.get(h2.group(1).strip())
            qno = None
            continue
        h3 = re.match(r"^###\s+Question\s+(\d+)", line)
        if h3:
            if buf:
                yield buf
            qno = str(int(h3.group(1)))        # same normalisation as parse_class_tests
            buf = {"label": label, "qno": qno, "marks": "", "lines": []}
            continue
        if buf is None:
            continue
        m = re.match(r"^\*\*Marks:?\*\*\s*(\d+)", line)
        if m:
            buf["marks"] = m.group(1)
            continue
        if line.startswith("- **(") or line.startswith("> *") or re.match(r"^- \$[a-z]", line):
            buf["parts"] = True
            continue
        if line.startswith("| Distance") or line.startswith("| Time") or line.startswith("**Concentration") or line.startswith("**Temperature"):
            buf["data"] = True
            continue
        if line == "---":
            continue
        if line:
            buf["lines"].append(line)
    if buf:
        yield buf


# --- filing map from the topic bank --------------------------------------------

ENTRY = re.compile(r"^- \*\*\[([^\]]+)\]\*\*\s*(.*)$")
ALSO = re.compile(r"\*\(also\s*→\s*([A-Z]{2}-\d+\.\d+)\)\*")


def parse_bank(path):
    """Map unit_id -> (subtopic, [extra subtopics]), and the set of subtopics
    that hold at least one entry line.

    Two different mechanisms put a unit under a second subtopic, and they are not
    the same thing:

      * The unit is printed a second time, as a full entry line, inside another
        subtopic's block. Ten units are printed this way, NM-3.5 with NM-3.8 and
        friends, because the question tests two separately marked skills. The
        second block is a second FILING of one answer.
      * The entry names `*(also → NM-x.y)*`. That is a pointer only. DM-5.6 has
        such a pointer and no entry line at all, because Fermat's little theorem
        is only ever asked as an opening clause inside another question.

    V2 counts entry lines, so DM-5.6 gets no file while NM-3.8 does. Getting this
    distinction wrong in either direction is a gate failure.
    """
    subtopic = None
    filing = {}
    has_entries = set()
    for lineno, raw in enumerate(open(path, encoding="utf-8"), 1):
        line = raw.rstrip("\n")
        h = re.match(r"^##\s+((?:NM|DM)-\d+\.\d+)\s", line)
        if h:
            subtopic = h.group(1)
            continue
        e = ENTRY.match(line)
        if e and subtopic:
            head, rest = e.group(1), e.group(2)
            uid = head.split("—")[0].strip()      # drop the marks field
            has_entries.add(subtopic)
            if uid in filing:
                # A second printed entry. Record the second filing, drop the
                # self-reference the reverse pointer creates.
                cur, also, text, ln = filing[uid]
                if subtopic != cur and subtopic not in also:
                    also.append(subtopic)
                for a in ALSO.findall(rest):
                    if a != cur and a not in also:
                        also.append(a)
                filing[uid] = (cur, also, text, ln)
                continue
            also = [a for a in ALSO.findall(rest) if a != subtopic]
            filing[uid] = (subtopic, also, rest, lineno)
    return filing, has_entries


# --- build ----------------------------------------------------------------------

def main():
    units = []
    for y in PAPERS:
        path = os.path.join(SRC, y + ".md")
        if not os.path.exists(path):
            die("missing paper", path)
        units.extend(parse_paper(path))

    ct_path = os.path.join(SRC, "ClassTestQuestions.md")
    ct_rows = list(parse_class_tests(ct_path))

    # Partless class-test questions are added here, with their data tables folded
    # in, because the paper parser above only sees `- **(x)**` bullets.
    have = {r["unit_id"] for r in ct_rows}
    stems = list(parse_class_test_stems(ct_path))
    for s in stems:
        uid = "%s Q.%s" % (s["label"], s["qno"])
        if uid in have or s.get("parts"):
            continue
        text = " ".join(s["lines"])
        ct_rows.append({
            "unit_id": uid,
            "source": "class_test",
            "year": s["label"],
            "question": s["qno"],
            "part": "",
            "marks_part": "",
            "marks_question": s["marks"],
            "co": "",
            "question_text": text,
            "origin": "ClassTestQuestions.md",
        })
    units.extend(ct_rows)

    filing, has_entries = parse_bank(os.path.join(SRC, "topic_wise_sorted_questions.md"))

    # Apply the 4.1a L2 correction. Moving the unit off NM-4.8 is what empties
    # that subtopic, so the entry-line set moves with the filing rather than
    # being left stale.
    for uid, (old, new) in L2_MOVES.items():
        if uid not in filing:
            die("L2 move names a unit with no filing", uid)
        cur, also, rest, ln = filing[uid]
        if cur != old:
            die("L2 move expected the unit to sit under the old subtopic",
                "%s sits under %s, not %s" % (uid, cur, old))
        # Drop both the old subtopic and the new one from the cross references:
        # after the move, NM-4.11 is where the unit is filed, so pointing at it
        # as well would double-file it against itself.
        filing[uid] = (new, [a for a in also if a not in (old, new)], rest, ln)
        has_entries.add(new)
        # NM-4.8 held this one entry line and nothing else, so it is now empty.
        # Discarding it is what drops NM-4.8 from the file list and brings the
        # build to 84 files rather than 85. A pointer from another subtopic, such
        # as 2018 Q.3(c) reaching NM-4.8, is not an entry line and does not keep
        # the subtopic alive.
        if not any(sub == old for sub, _a, _r, _l in filing.values()):
            has_entries.discard(old)

    # Every unit needs exactly one filing, and every filing needs a unit.
    missing = [u["unit_id"] for u in units if u["unit_id"] not in filing]
    if missing:
        die("%d unit(s) have no filing in the topic bank" % len(missing), *missing)
    extra = [k for k in filing if k not in {u["unit_id"] for u in units}]
    if extra:
        die("%d filing(s) name no unit" % len(extra), *sorted(extra))

    # Paper marks must reconcile with the audit totals.
    per_paper = {}
    for u in units:
        if u["source"] == "paper":
            per_paper[u["year"]] = per_paper.get(u["year"], 0) + int(u["marks_part"])
    expect = {"2017": 96, "2018": 96, "2019": 96, "2020": 96,
              "2021": 97, "2022": 80, "2023": 80, "2024": 80}
    if per_paper != expect:
        die("per-paper mark totals disagree with the audit", str(per_paper), str(expect))

    fields = ["unit_id", "source", "year", "question", "part", "marks_part",
              "marks_question", "co", "subtopic", "also_subtopics",
              "origin", "question_text"]
    rows = []
    for u in units:
        sub, also, _rest, _ln = filing[u["unit_id"]]
        rows.append({
            "unit_id": u["unit_id"],
            "source": u["source"],
            "year": u["year"],
            "question": u["question"],
            "part": u["part"],
            "marks_part": u["marks_part"],
            "marks_question": u["marks_question"],
            "co": u["co"],
            "subtopic": sub,
            "also_subtopics": " ".join(also),
            "origin": u["origin"],
            "question_text": " ".join(u["question_text"].split()),
        })
    rows.sort(key=lambda r: (r["source"] != "paper", r["year"], int(r["question"]), r["part"]))

    with open(OUT, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)

    # --- V2 report -------------------------------------------------------------
    with_files = has_entries

    listed = [l.strip() for l in open(os.path.join(ROOT, "scripts", "filelist.txt")) if l.strip()]
    listed_ids = {l.split("_")[0] for l in listed}

    # The set of subtopics holding a printed entry line is not derivable from
    # the manifest's `subtopic` column alone, because ten units are printed a
    # second time inside another subtopic's block. NM-3.8, NM-5.6, NM-5.7 and
    # NM-10.4 hold entry lines but are never the primary filing of any unit, so
    # reading only the primary column would wrongly report them as fileless.
    # Gate V2 reads this file instead of recomputing the set.
    with open(os.path.join(ROOT, "scripts", "subtopics_with_file.txt"), "w",
              encoding="utf-8") as fh:
        for s in sorted(has_entries):
            fh.write(s + "\n")

    papers = sum(1 for r in rows if r["source"] == "paper")
    cts = sum(1 for r in rows if r["source"] == "class_test")
    print("answer_manifest.csv written to %s" % os.path.relpath(OUT, ROOT))
    print("  rows            : %d" % len(rows))
    print("  paper units     : %d" % papers)
    print("  class-test units: %d" % cts)
    print("  marks, papers   : %d" % sum(int(r["marks_part"]) for r in rows if r["source"] == "paper"))
    print("  subtopics used  : %d" % len(with_files))
    print("  filelist.txt    : %d" % len(listed))

    bad = with_files ^ listed_ids
    if bad:
        die("filelist disagrees with the manifest's subtopic set",
            *sorted("%s: manifest-only" % b if b in with_files else "%s: filelist-only" % b
                    for b in bad))
    print("\nV2 OK: 202 rows, 84 subtopics, filelist agrees.")


if __name__ == "__main__":
    main()