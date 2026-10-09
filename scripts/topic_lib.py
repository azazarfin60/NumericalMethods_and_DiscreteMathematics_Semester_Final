#!/usr/bin/env python3
"""Shared helpers for the topic-wise layer.

Both generators and both parity gates read P1/P2 through this module, so there
is exactly one parser. A second parser is a second opinion nobody asked for,
and the two would eventually disagree.

Nothing here writes a number. It only moves text.
"""

import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

P1_DIR = os.path.join(ROOT, "answers_exam_style")
P2_DIR = os.path.join(ROOT, "answers_explanation")
MAP = os.path.join(ROOT, "scripts", "merge_map.csv")
FILELIST = os.path.join(ROOT, "scripts", "filelist.txt")
NOFILE = os.path.join(ROOT, "scripts", "filelist_no_file.txt")
MANIFEST = os.path.join(ROOT, "scripts", "answer_manifest.csv")

PAPERS = ["2017", "2018", "2019", "2020", "2021", "2022", "2023", "2024"]

# '### **(a) Question text ... [Marks: 04, CO: 1]**'
HEAD = re.compile(r"(?m)^### \*\*\(([a-z])\)\s(.*?)\*\*\s*$")
# '## Question 3'
QHEAD = re.compile(r"(?m)^## Question (\S+)\s*$")
MARKS = re.compile(r"\[Marks:\s*([^\]]*)\]")


def units_in(text):
    """[(question, part, heading, body)] for one year-wise file.

    `heading` is the raw question text with the marks field stripped off; `body`
    is everything up to the next part or the next question.
    """
    out = []
    secs = QHEAD.split(text)
    # secs = [preamble, qno, body, qno, body, ...]
    for i in range(1, len(secs) - 1, 2):
        qno, body = secs[i], secs[i + 1]
        ms = list(HEAD.finditer(body))
        for j, m in enumerate(ms):
            start = m.end()
            end = ms[j + 1].start() if j + 1 < len(ms) else len(body)
            raw = m.group(2)
            mm = MARKS.search(raw)
            marks = mm.group(1) if mm else ""
            qtext = " ".join(MARKS.sub("", raw).split())
            out.append((qno, m.group(1), qtext, marks, body[start:end].strip("\n")))
    return out


def load_year(directory, year, suffix):
    path = os.path.join(directory, "%s%s.md" % (year, suffix))
    if not os.path.exists(path):
        return {}
    text = open(path, encoding="utf-8").read()
    out = {}
    for qno, part, qtext, marks, body in units_in(text):
        out["%s Q.%s(%s)" % (year, qno, part)] = {
            "question": qtext,
            "marks": marks,
            "body": body,
            "year": year,
            "qno": qno,
            "part": part,
        }
    return out


def load_p1():
    """unit_id -> section, from answers_exam_style/."""
    out = {}
    for y in PAPERS:
        out.update(load_year(P1_DIR, y, "_answer"))
    return out


def load_p2():
    """unit_id -> section, from answers_explanation/.

    A P2 heading prints the paper's question text exactly and carries its marks
    on the following line as `*[Marks: NN]*`, so the marks are read from there
    rather than from the heading.
    """
    out = {}
    for y in PAPERS:
        path = os.path.join(P2_DIR, "%s_explanation.md" % y)
        if not os.path.exists(path):
            continue
        text = open(path, encoding="utf-8").read()
        secs = QHEAD.split(text)
        for i in range(1, len(secs) - 1, 2):
            qno, body = secs[i], secs[i + 1]
            ms = list(HEAD.finditer(body))
            for j, m in enumerate(ms):
                start = m.end()
                end = ms[j + 1].start() if j + 1 < len(ms) else len(body)
                raw = " ".join(MARKS.sub("", m.group(2)).split())
                chunk = body[start:end]
                mm = re.search(r"\*\[Marks:\s*([^\]]*)\]\*", chunk)
                out["%s Q.%s(%s)" % (y, qno, m.group(1))] = {
                    "question": raw,
                    "marks": mm.group(1) if mm else "",
                    "body": chunk.strip("\n"),
                    "year": y,
                    "qno": qno,
                    "part": m.group(1),
                }
    return out


def load_map():
    import csv
    return list(csv.DictReader(open(MAP, encoding="utf-8")))


def load_filelist():
    return [l.strip() for l in open(FILELIST, encoding="utf-8") if l.strip()]


def slug_id(slug):
    m = re.match(r"((?:NM|DM)-\d+\.\d+)_", slug)
    return m.group(1) if m else None


def slug_for(sid):
    for s in load_filelist():
        if slug_id(s) == sid:
            return s
    return None


def title_of(sid, bank=None):
    """The subtopic's display title, from the frozen topic bank."""
    path = bank or os.path.join(ROOT, "PreviousYearQuestions",
                                "topic_wise_sorted_questions.md")
    for line in open(path, encoding="utf-8"):
        m = re.match(r"^##\s+((?:NM|DM)-\d+\.\d+)\s*·\s*(.+?)\s*$", line.rstrip())
        if m and m.group(1) == sid:
            t = re.sub(r"\s*\*\(.*?\)\*\s*$", "", m.group(2)).strip()
            return t
    return sid


BOX_OPEN = re.compile(r"\\boxed\{")


def boxes(text):
    """Every \\boxed{...} body, brace-matched, whitespace-normalised.

    Same rule as gate_v5: braces inside are counted, a backslash escapes the
    next character, and the body is compared with runs of whitespace collapsed
    so a re-wrapped line is not reported as a change.
    """
    out = []
    for m in BOX_OPEN.finditer(text):
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


def normalise(s):
    """The comparison form for a copied number or phrase."""
    return " ".join(s.split()).replace("\\ ", " ")
