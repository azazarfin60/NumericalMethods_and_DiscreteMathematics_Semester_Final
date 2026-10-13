# ECE 2213 — Numerical Methods & Discrete Mathematics

Exam preparation repository for **ECE 2213** at Rajshahi University of Engineering & Technology (RUET), Department of Electrical & Computer Engineering. 3.00 credits.

## What this repo contains

| Layer | Directory | What it holds |
| :-- | :-- | :-- |
| **Source questions** | `PreviousYearQuestions/` | 8 semester-final papers (2017–2024), 4 class tests, and the topic-sorted question bank. Frozen after hashing. |
| **Exam-style answers** | `answers_exam_style/` | Year-wise model answers. Short-form working. The **origin layer** — every number is authored here and nowhere else. |
| **Explanation answers** | `answers_explanation/` | Year-wise answers with full reasoning, method names, formula explanations, and trap warnings. |
| **Boss Notes v2.0 suite** | `boss_notes/` | 125-file comprehensive, exam-focused study suite across 17 topics (105 subtopic notes, 17 topic overviews, master formula sheet, index). Self-sufficient study material. |
| **Topic-wise exam clusters** | `topicwise_answers_exam_style/` | 14 consolidated topic-level modules (10 NM + 4 DM) + master index. Generated from the year-wise answers. |
| **Topic-wise explanation clusters** | `topicwise_answers_explanation/` | 14 consolidated topic-level modules (10 NM + 4 DM) + master index. Generated from the year-wise explanations. |
| **Subtopic-wise archive** | `SubTopicwise_Answers/` | 84 granular subtopic files per layer with BossNote-style navigation. Preserved isolate reference. |
| **Boss Notes v1.0 archive** | `BossNotes_Old/` | Preserved flat 46-file study suite (predecessor to v2.0 multi-folder architecture). |
| **Class test answers** | `CT_Questions/` | Exam-style and explanation answers for CT-01, CT-02A, CT-02B, CT-04. |

## Reference material (read-only)

| Directory | Source |
| :-- | :-- |
| `DiscreteMathTextbook/` | Digitized chapters from Rosen's *Discrete Mathematics and Its Applications*. 8 chapters. |
| `NumericalMethodTextbook/` | Digitized chapters from Jain, Iyengar & Jain's *Numerical Methods*. 11 chapters. |
| `ClassNote_By_Fahad/` | Digitized class notes (NM + DM). Instructors: Nadim Sir, Faysal Sir. |
| `ClassNote_by_Raidah/` | Digitized class notes (NM + DM). Instructors: Nadim Sir, NRP Sir. |
| `DiscreteMath_note_by_Shishir/` | DM lecture notes. 7 topic files + index. |
| `NumericalMethods_note_by_Shishir/` | NM lecture notes. 4 notebook segments. |

## Analysis and governance files

| File | Purpose |
| :-- | :-- |
| `ECE2213_Syllabus.md` | Official syllabus. Section 1 = Numerical Methods (7 topics). Section 2 = Discrete Mathematics (6 topics). |
| `topic_subtopic_list.md` | Canonical taxonomy: 105 subtopics across 17 clusters, with tier ratings, years appeared, and frequency data. |
| `combined_analysis_report.md` | Cross-reference of exam papers, class notes, and syllabus. Gaps, patterns, and study priorities. |
| `PreviousYearAnalysisReport.md` | Per-paper statistical analysis: mark distributions, topic weights, repeat patterns. |
| `question_tally_audit.md` | Per-sub-question mark tally. 183 finals + 19 CTs = 202 rows. Arithmetic backing for all reports. |
| `BOSS_NOTES_QA_REPORT_v1.0.md` | Comprehensive quality audit report verifying all 125 files in the Boss Notes v2.0 suite against repository gates. |
| `exam_register.md` | Register rules for exam-style files. No second person, no commentary, no strategy advice. |
| `writing_style.md` | Prose style rules for everything else. Short sentences, plain words, no AI-sounding words. |
| `MARKDOWN-GUIDE.md` | LaTeX and Obsidian formatting conventions used throughout. |

## Scripts

`scripts/` holds 25 Python scripts, 3 shell scripts, and data files (manifests, merge maps, file lists). They run the quality gates (V1–V15), assemble topic-wise clusters (`build_topicwise_clusters.py`), generate subtopic archives (`gen_topicwise.py`), produce matplotlib diagrams, and audit number consistency. See `scripts/README.md`.

## How the data flows

```
PreviousYearQuestions/  (frozen source, never edited)
        │
        ├──► answers_exam_style/       (year-wise, origin layer)
        │         │
        │         └──► answers_explanation/  (year-wise, adds reasoning)
        │                   │
        ▼                   ▼
    scripts/gen_topicwise.py + merge_map.csv
        │
        ├──► SubTopicwise_Answers/     (granular 84 files per layer)
        │         │
        ▼         ▼
    scripts/build_topicwise_clusters.py
        │
        ├──► topicwise_answers_exam_style/   (14 consolidated topic modules)
        ├──► topicwise_answers_explanation/  (14 consolidated topic modules)
        │
        ├──► boss_notes/               (125-file comprehensive study suite; Rule B parity)
        │
        └──► CT_Questions/             (class test answers)
```

Numbers flow one way: exam-style origin → explanation → topic-wise / boss notes. No number is ever born in a downstream file.

## The three rules

1. **Answers are authored in one place only** — the year-wise exam-style files.
2. **Every number is copied, never retyped** — boxed results are character-identical across all layers.
3. **No invented questions in answer directories** — drills belong elsewhere.

## Course structure

| Era | Section A | Section B |
| :-- | :-- | :-- |
| 2017–2021 | Numerical Methods | Numerical Methods |
| 2022–2024 | Numerical Methods | Discrete Mathematics |

Discrete Mathematics entered the course in 2022. The five older papers are 100% Numerical Methods.

## Scale

~1,430+ files. 614 markdown files. 483 images/diagrams. 202 manifest rows (183 semester-finals + 19 class-test parts). 84 examined subtopics (out of 105 total). 14 consolidated topic modules per answer layer. 125-file Boss Notes v2.0 study suite.
