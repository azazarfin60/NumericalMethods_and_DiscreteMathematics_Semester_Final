# Scripts

Build scripts, quality gates, and data files that drive the answer pipeline.

## Quality gate scripts

| Script | Gate | What it checks |
| :-- | :-- | :-- |
| `gate_v1.sh` | V1 | Source freeze: SHA-256 hashes of the 9 question files match `source_manifest.sha256`. |
| `gate_v2.sh` | V2 | Manifest completeness: every sub-question in the papers has a row in `answer_manifest.csv`. |
| `gate_v3.py` | V3 | One-block-per-file: every unit appears in exactly one file, in exactly one block. |
| `gate_v4.py` | V4 | Heading parity: both topic-wise folders have identical block headings and provenance lines. |
| `gate_v5.py` | V5 | Boxed-result match: every `\boxed{}` in explanation and topic-wise files is character-identical to the exam-style origin. |
| `gate_v7.py` | V7 | Cross-reference health: no dead pointers, no pointer-only files pointing at nothing. |
| `gate_v8.py` | V8 | Number provenance: every box and long numeral traces to a year-wise section. |
| `gate_v9.sh` | V9 | Build hygiene: no Practice/Extra/Similar/Bonus strings in the answer directories. |
| `gate_v12.py` | V12 | Manifest arithmetic: marks sum correctly per paper. |
| `gate_v13.py` | V13 | Coverage audit: every manifest row has an answer in the expected file. |
| `gate_v14.py` | V14 | Full lint: no retyped boxes, every cited unit is real, no dead pointers. |
| `gate_v15.py` | V15 | Final reconciliation: all gates pass together. |

## Generator scripts

| Script | What it does |
| :-- | :-- |
| `gen_topicwise.py` | Generates both topic-wise answer folders from the year-wise files + `merge_map.csv`. |
| `build_manifest.py` | Builds `answer_manifest.csv` from the question papers. |
| `build_merge_map.py` | Builds `merge_map.csv` with merge/split decisions for repeated questions. |
| `build_filelist.py` | Generates `filelist.txt` and `subtopics_with_file.txt` from the taxonomy. |

## Linters

| Script | What it checks |
| :-- | :-- |
| `lint_register.py` | Enforces `exam_register.md` rules (no second person, no commentary) on exam-style files. |
| `lint_explanation.py` | Enforces `writing_style.md` rules on explanation files. |
| `check_paper.py` | Validates a single paper's structure against the manifest. |
| `audit_numbers.py` | Audits numerical results across all answer layers for consistency. |
| `strip_code.py` | Strips code fences from markdown files (utility). |
| `normalize-vault-math.mjs` | Normalizes LaTeX math fences for Obsidian vault compatibility. |

## Utility

| Script | What it does |
| :-- | :-- |
| `generate_2018_q4c_plot.py` | Generates the regression plot for 2018 Q.4(c). |
| `topic_lib.py` | Shared library: taxonomy parsing, file naming, ID resolution. |

## Data files

| File | What it holds |
| :-- | :-- |
| `answer_manifest.csv` | 202 rows. One row per sub-question. Year, question number, marks, subtopic, merge tier, filing target. |
| `merge_map.csv` | Merge/split decisions for repeated questions. Read by `gen_topicwise.py`. |
| `filelist.txt` | Expected file list for the topic-wise directories. |
| `filelist_no_file.txt` | Subtopics with no exam presence (no file created). |
| `subtopics_with_file.txt` | Subtopics that have at least one question (84 of 105). |
| `source_manifest.sha256` | SHA-256 hashes of the 9 frozen source files. |
