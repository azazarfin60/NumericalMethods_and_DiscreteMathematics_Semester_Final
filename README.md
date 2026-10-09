# ECE 2213 — Numerical Methods & Discrete Mathematics

Exam preparation repository for **ECE 2213** at Rajshahi University of Engineering & Technology (RUET), Department of Electrical & Computer Engineering. 3.00 credits.

## What this repo contains

| Layer | Directory | What it holds |
| :-- | :-- | :-- |
| **Source questions** | `PreviousYearQuestions/` | 8 semester-final papers (2017–2024), 4 class tests, and the topic-sorted question bank. Frozen after hashing. |
| **Exam-style answers** | `answers_exam_style/` | Year-wise model answers. Short-form working. The **origin layer** — every number is authored here and nowhere else. |
| **Explanation answers** | `answers_explanation/` | Year-wise answers with full reasoning, method names, formula explanations, and trap warnings. |
| **Topic-wise exam answers** | `topicwise_answers_exam_style/` | 84 subtopic files. Generated from the year-wise exam-style answers. Never hand-written. |
| **Topic-wise explanations** | `topicwise_answers_explanation/` | 84 subtopic files. Generated from the year-wise explanations. Same block IDs as the exam-style pair. |
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
| `exam_register.md` | Register rules for exam-style files. No second person, no commentary, no strategy advice. |
| `writing_style.md` | Prose style rules for everything else. Short sentences, plain words, no AI-sounding words. |
| `MARKDOWN-GUIDE.md` | LaTeX and Obsidian formatting conventions used throughout. |

## Scripts

`scripts/` holds 20 Python scripts, 3 shell scripts, and data files (manifests, merge maps, file lists). They run the quality gates (V1–V15), generate the topic-wise folders, lint the register, and audit number consistency. See `scripts/README.md`.

## How the data flows

```
PreviousYearQuestions/  (frozen source, never edited)
        │
        ├──► answers_exam_style/       (year-wise, origin layer)
        │         │
        │         └──► answers_explanation/  (year-wise, adds reasoning)
        │
        ├──► topicwise_answers_exam_style/   (generated, 84 files)
        ├──► topicwise_answers_explanation/  (generated, 84 files)
        │
        └──► CT_Questions/             (class test answers)
```

Numbers flow one way: exam-style origin → explanation → topic-wise. No number is ever born in a downstream file.

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

~980 files. ~380 markdown files. ~280 images. 202 manifest rows. 84 subtopic files per answer layer.
