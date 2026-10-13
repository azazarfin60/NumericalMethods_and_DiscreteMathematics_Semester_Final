# Scripts

Build scripts, quality gates, and data files that drive the answer pipeline.

## Quality gate scripts

| Script | Gate | What it checks |
| :-- | :-- | :-- |
| `gate_v1.sh` | V1 | Source freeze: SHA-256 hashes of the 9 question files match `source_manifest.sha256`. |
| `gate_v2.sh` | V2 | Manifest completeness: every sub-question in the papers has a row in `answer_manifest.csv` (202 rows, 84 examined subtopics). |
| `gate_v3.py` | V3 | Cluster & subtopic coverage: every unit appears in exactly one topic file, in exactly one block. |
| `gate_v4.py` | V4 | Heading parity: both topic-wise folders have identical block headings and provenance lines. |
| `gate_v5.py` | V5 | Boxed-result match: every `\boxed{}` in downstream files is character-identical to the exam-style origin. |
| `gate_v7.py` | V7 | Cross-reference health: no dead pointers, no pointer-only files pointing at nothing. |
| `gate_v8.py` | V8 | Number provenance: every box and long numeral traces to a year-wise section. |
| `gate_v9.sh` | V9 | Build hygiene: no Practice/Extra/Similar/Bonus strings in the answer directories. |
| `gate_v12.py` | V12 | Section metadata parity: explanation layer agrees with exam-style on marks and CO/CLO mapping. |
| `gate_v13.py` | V13 | Coverage audit: every manifest row has an answer in the expected file; merge-map invariants hold. |
| `gate_v14.py` | V14 | Topic layer lint: no retyped boxes, every cited unit is real, no dead pointers across all 30 topic files. |
| `gate_v15.py` | V15 | Math delimiter balance: paired `$$` fences and balanced inline `$` per block. |

## Generator scripts

| Script | What it does |
| :-- | :-- |
| `build_topicwise_clusters.py` | Clusters the 84 subtopic files into 14 consolidated topic-level modules and adds BossNote-style navigation indices. |
| `gen_topicwise.py` | Generates granular subtopic answer files in `SubTopicwise_Answers/` from the year-wise files + `merge_map.csv`. |
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
| `audit_ascii_diagrams.py` | Scans repository markdown files for leftover ASCII art diagrams. |
| `strip_code.py` | Strips code fences from markdown files (utility). |
| `normalize-vault-math.mjs` | Normalizes LaTeX math fences for Obsidian vault compatibility. |

## Diagram generators and utilities

| Script | What it does |
| :-- | :-- |
| `generate_2017_q6a_plot.py` | Generates the regression criteria comparison plot for 2017 Q.6(a). |
| `generate_2018_q4c_plot.py` | Generates the regression plot for 2018 Q.4(c). |
| `generate_2023_q5a_plot.py` | Generates logic circuit diagrams for 2023 Q.5(a). |
| `generate_boss_notes_plots.py` | Generates technical diagrams for Boss Notes (Laplace grid, precision/accuracy, relaxation spectrum, integrator circuit). |
| `generate_error_tradeoff_plot.py` | Generates truncation vs round-off error trade-off plot for NM-1. |
| `topic_lib.py` | Shared library: taxonomy parsing, file naming, ID resolution. |

## Data files

| File | What it holds |
| :-- | :-- |
| `answer_manifest.csv` | 202 rows. One row per sub-question. Year, question number, marks, subtopic, merge tier, filing target. |
| `merge_map.csv` | Merge/split decisions for repeated questions. Read by `gen_topicwise.py`. |
| `filelist.txt` | Expected file list for the subtopic-wise directories (84 files). |
| `filelist_no_file.txt` | Subtopics with no exam presence (21 of 105, no file created). |
| `subtopics_with_file.txt` | Subtopics that have at least one question (84 of 105). |
| `source_manifest.sha256` | SHA-256 hashes of the 9 frozen source files. |
