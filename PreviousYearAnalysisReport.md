---
course_code: ECE 2213
course_title: Numerical Methods & Discrete Mathematics
document_type: Previous Year Question Analysis Report
years_analyzed: 2017-2024 + Class Tests
tags:
  - exam-analysis
  - ece2213
  - numerical-methods
  - discrete-mathematics
  - previous-year-questions
---

# ECE 2213 — Comprehensive Previous Year Question Analysis Report

**Institution:** Rajshahi University of Engineering & Technology (RUET)
**Department:** Electrical & Computer Engineering
**Course:** ECE 2213 — Numerical Methods & Discrete Mathematics (3.00 Credits)
**Papers Analyzed:** 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024 + Class Tests (CT-01, CT-02 Set A, CT-02 Set B, CT-04)

> **How to check this report.** Every quantitative claim here is derived from
> `question_tally_audit.md`, which lists all **183** sub-questions across the 8 papers with their
> marks and a topic cluster (721 marks total = 601 numerical + 120 discrete). Any table below can be
> recomputed from that file. Statements marked **[judgement]** are opinion, not measurement.

---

## 1. Executive Summary

Eight semester-final papers and four class tests were analyzed against the official syllabus. The dominant finding is that **ECE 2213 is two different courses wearing one course code**, split by a curriculum reform:

| Era | Years | Course Title | Marks Answerable | Content |
| :--- | :--- | :--- | :---: | :--- |
| **Pre-OBE** | 2017 – 2021 | *Numerical Methods* | 72 | 100% Numerical Methods (both sections) |
| **OBE** | 2022 – 2024 | *Numerical Methods & Discrete Mathematics* | 60 | 50% Numerical Methods + 50% Discrete Mathematics |

**The three highest-value conclusions:**

1. **Question recycling is the defining feature of this course.** 2023's Section A is roughly **94% traceable** to 2021 + 2017 + 2018 + 2020 — only one sub-question in the whole section is new. 2024's Section B is **35% traceable** to 2022. The register in Section 7 lists **22 repeat pairs: 15 verbatim, 4 near-verbatim (same data, one value changed), 3 same-concept.** Solving past papers is not revision for this exam — it *is* the exam.
2. **Error Analysis is Q.1 of Section A in 8 of 8 papers — without exception.** Roots of Equations also appears in 8 of 8, sitting at **Q.1 or Q.2** (Q.1 in 2021–2023; Q.2 in 2017–2020 and 2024, plus Q.3c in 2017). Interpolation appears in 8 of 8. These three blocks carry the bulk of Section A.
3. **Discrete Mathematics is overwhelmingly Propositional Logic.** Across 2022–2024, Logic takes **64 of 120 Section B marks (53%)**, Number Theory **32 (27%)**, Counting **17 (14%)**. **Sets, Relations and Proof Techniques — three of six syllabus units — have never produced a single question.**

---

## 2. Critical Context: The 2022 OBE Curriculum Change

This is essential for correctly reading the older papers.

### 2.1 What Changed

- **Before 2022** (papers 2017–2021): The course was titled simply **"Numerical Methods."** There was **no Discrete Mathematics component in the course at all.** Both Section A and Section B of those papers are pure numerical methods. Full marks were **72** — 6 questions answered × 12 marks, taking 3 from each section of 8 set. (Marks *set* per paper = 96.)
- **From 2022 onward** (papers 2022–2024): The curriculum was revised to the **Outcome-Based Education (OBE)** framework, and **Discrete Mathematics was added as a new half of the course.** The title became **"Numerical Methods & Discrete Mathematics."** Full marks dropped to **60** (6 × 10), and the section split became rigid:
  - **Section A = Numerical Methods only (Q.1 – Q.4)**, 40 marks set
  - **Section B = Discrete Mathematics only (Q.5 – Q.8)**, 40 marks set

### 2.2 How to Read the Old Papers

> **Do not use 2017–2021 papers to predict the Discrete Mathematics section — they contain zero discrete mathematics.** They remain highly valuable, but only for Section A, where the OBE-era questions are 12 → 10 marks and are competing with an entire second subject for space. **[judgement]** This makes the pre-OBE numerical questions moderately harder per mark, but the difference is small.

Practical consequence: **2017–2021 gives you ~5 papers' worth of Section A practice but 0 papers of Section B practice.** Section B prediction rests entirely on 2022, 2023, 2024 and CT-04 — a thin base, which is precisely why the recycling rate matters so much.

### 2.3 The Transitional Year: 2021

2021 is the hinge paper and deserves special attention:
- Still titled "Numerical Methods," still 72 marks, still 100% numerical.
- **It is the first paper to carry CLO (Course Learning Outcome) tags in the margin** — "Figures in the margin indicate full marks and course learning outcomes (CLOs)."
- It is also the broadest numerical paper ever set. It is **the only paper to examine the Optimization syllabus unit** (Q.6b Newton's method for a maximum of 2 sin x − x²/10; Q.6d constrained vs. unconstrained). Note that **2018 Q.5b also asks for the x at which a tabulated y is maximum** — the same method, presented as a tabulation exercise rather than labelled optimisation.
- It is the only paper with an **explicit solved Boundary Value Problem** (Q.5b). 2024 Q.4a is BVP *theory* only; 2018 Q.8a and 2019 Q.8b are PDE problems posed on a bounded domain.

So OBE *assessment machinery* arrived in 2021; OBE *content* arrived in 2022. Interpretation **[judgement]**: 2021 was written by a numerical-methods instructor already being asked to tag outcomes, which pushed them to cover the full syllabus breadth. **2023 then recycled 2021 heavily — making 2021 the single most important pre-OBE paper to master.**

*Source note:* the transcribed 2021 paper totals **97 marks set**, not 96 — Q.7 is listed as 2 + 6 + 5. This is a transcription artefact; the other seven questions are 12 each and full marks answerable remain 72.

### 2.4 CLO / CO Tagging Evolution

| Year | Margin Tags |
| :--- | :--- |
| 2017 – 2020 | None |
| 2021 | CLO1, CLO2, CLO3 |
| 2022 | CLOs column (CLO1–CLO3) |
| 2023 | CLOs column (CLO1–CLO3) |
| 2024 | CO column (CO 1, CO 2) — only two COs used in the whole paper |

In 2024, every Section B question is tagged **CO2**, and 10 of the 12 Section A sub-questions are **CO1** — the two exceptions being Q.1c (round-off vs truncation) and Q.2a (bisection), both tagged CO2. So the mapping is *nearly* "Section A = CO1, Section B = CO2", which makes CO tags close to useless for predicting content.

---

## 3. Paper Structure & Rubric Comparison

| Feature | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Full Marks (answerable) | 72 | 72 | 72 | 72 | 72 | 60 | 60 | 60 |
| Time | 3 h | 3 h | 3 h | 3 h | 3 h | 3 h | 3 h | 3 h |
| Questions set | 8 | 8 | 8 | 8 | 8 | 8 | 8 | 8 |
| Questions to answer | 6 (3+3) | 6 (3+3) | 6 (3+3) | 6 (3+3) | 6 (3+3) | 6 (3+3) | 6 (3+3) | 6 (3+3) |
| Marks per question | 12 | 12 | 12 | 12 | 12 | 10 | 10 | 10 |
| Marks set (whole paper) | 96 | 96 | 96 | 96 | 97* | 80 | 80 | 80 |
| Section A content | NM | NM | NM | NM | NM | **NM** | **NM** | **NM** |
| Section B content | NM | NM | NM | NM | NM | **DM** | **DM** | **DM** |
| Separate scripts per section | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Circuit-based question | – | Q.4b | Q.3c | Q.4b | Q.7b | – | – | Q.2b |
| PDE grid question | – | Q.8a | Q.8b | Q.8b | Q.6c | – | – | – |

\* see §2.3. Marks *set* = 8 questions × marks per question; full marks answerable = 6 × marks per question.

**Invariant across all 8 years:** 8 questions set, answer any 6 taking any 3 from each section, separate answer script per section, figures in margin indicate full marks.

**Structural implication for the OBE era:** Section A is 4 questions, you answer 3. Section B is 4 questions, you answer 3. So **30 marks of Numerical Methods and 30 marks of Discrete Mathematics — you cannot trade one section against the other.** Neglecting Discrete Mathematics caps you at 50%.

---

## 4. Numerical Methods — Topic Frequency Analysis (2017–2024)

### 4.1 Master Frequency Table

Each ✓ = one sub-question. The **Papers** column counts years in which the topic appears at all.

| # | Syllabus Topic | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | Papers | Marks (of 601) | CTs |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | ---: | :--- |
| 1 | Modeling, Errors & Taylor Series | ✓✓✓✓✓✓ | ✓✓✓ | ✓✓✓ | ✓✓ | ✓✓ | ✓ | ✓✓ | ✓✓✓ | **8/8** | 85 | CT-01 |
| 2 | Roots of Equations | ✓✓✓✓ | ✓✓✓ | ✓✓✓ | ✓✓ | ✓✓✓✓ | ✓ | ✓ | ✓ | **8/8** | 78 | CT-01 |
| 3 | Linear Algebraic Equations | ✓✓✓✓ | ✓✓ | ✓✓✓ | ✓✓ | ✓✓ | ✓✓✓✓ | – | ✓ | **7/8** | 73 | CT-02B |
| 4a | Curve Fitting — Regression | ✓✓✓ | ✓ | ✓✓✓ | ✓ | ✓ | ✓✓ | ✓ | ✓✓ | **8/8** | 43 | – |
| 4b | Curve Fitting — Interpolation | ✓✓ | ✓✓✓ | ✓✓✓ | ✓✓✓ | ✓✓✓✓✓✓ | ✓✓✓ | ✓✓✓ | ✓✓✓ | **8/8** | 103 | CT-02A |
| 5 | Numerical Integration | – | ✓✓ | ✓✓✓ | ✓✓ | ✓✓ | ✓ | ✓✓✓ | – | **6/8** | 87 | – |
| 6 | Optimization | – | ✓ | – | – | ✓✓ | – | – | – | **2/8** (1/8 explicit) | 11 | – |
| 7a | Numerical Differentiation | ✓ | ✓ | ✓✓ | ✓ | ✓✓ | ✓ | – | – | **6/8** | — | – |
| 7b | ODE (Euler / Heun / RK) | ✓✓ | ✓✓✓ | ✓✓ | ✓✓✓ | ✓✓ | – | ✓ | ✓ | **7/8** | 69 | CT-02B |
| 7c | Boundary Value / Eigenvalue | ✓ | – | – | – | ✓✓ | – | ✓ | ✓ | **4/8** | 21 | – |
| 7d | PDE (Laplace / Poisson / Liebmann) | – | ✓ | ✓ | ✓✓ | ✓ | – | – | ✓ | **4/8** | 31 | – |

Marks column uses the aggregate in `question_tally_audit.md` §A. For rows 7a–7d the marks are split with row 5 (differentiation shares the integration row in the aggregate) and rows 7c/7d are listed separately: BVP 10, eigenvalue 11, PDE 31.

**Two frequency facts that are often overstated, stated correctly here:**
- **Bracketing methods specifically** appear in only **6 of 8 papers** — absent from 2019 (Q.2 is entirely open-method) and 2023 (Q.1c is N-R).
- **Open methods specifically** appear in **7 of 8 applied** — 2024's only root-finding item (Q.2a) is bisection, a bracketing method. 2022 Q.1a names open methods but applies none.

### 4.2 Tier Classification for Numerical Methods

**🔴 TIER 1 — Guaranteed (appeared in 8/8 papers, never skipped)**

| Topic | What is actually asked |
| :--- | :--- |
| **Errors & Taylor Series** | Define numerical methods; numerical vs. analytical; why ECE engineers need them; accuracy vs. precision; round-off vs. truncation error; error representations (true / absolute / relative / percentage) applied to an instrument reading; round-off in digit summation; Taylor expansion to a stated decimal accuracy; relative error of a composite function; relative error of the expansion used to evaluate e⁻⁵ |
| **Roots of Equations** | Bisection, False Position (Regula Falsi), Newton-Raphson, Secant — derivation, algorithm steps, limitations, merits/demerits, cross-comparison, and numeric iterations (usually 2–4) on a cubic or a physically-framed current equation |
| **Interpolation** | Lagrange, Newton's Forward, Newton's Backward, Newton's Divided Difference, Gauss forward; definitions of interpolation vs. extrapolation vs. curve fitting; derivation of Newton's forward formula; the recurring decennial-census population problem |
| **Regression / Curve Fitting** | Least squares straight-line fit; exponential fit `y = a·e^(bx)`; non-linear fit `y = x/(a+bx)`; quadratic path fit; why min-error / min-absolute-error criteria are ill-suited; deducing the linear regression normal equations |

**🟠 TIER 2 — Near-Certain (6–7 of 8 papers)**

| Topic | What is actually asked |
| :--- | :--- |
| **Linear Algebraic Equations** | Gauss-Seidel is the dominant applied method — 4 of its 7 appearances are a **DC circuit** (mesh or nodal) you must first reduce to equations yourself. Also Jacobi, Gauss Elimination, pivoting theory (partial vs. complete, why it matters), relaxation (over/under, λ), ill-conditioned systems, LU decomposition (theory only, 2017 Q.4b) |
| **Numerical Integration / Differentiation** | Trapezoidal rule (derivation + step-count for a target error); Simpson's 1/3 and 3/8 (derivation, comparison, exactness up to degree 3); Romberg's method; forward-difference formulas for dy/dx and d²y/dx²; the recurring rocket-distance integral with true error and absolute relative true error |
| **ODE Solvers** | Euler, Modified Euler / Heun (derivation + limitation), RK2, RK4. Always a small-step tabulated march (h = 0.1 or 0.2, two or three steps). Also second-order ODE reduced to a system, and ODE formulation from a physical scenario |

**🟡 TIER 3 — Pre-OBE Only / Mostly Dropped (verify before investing)**

| Topic | Status |
| :--- | :--- |
| **PDE (Laplace, Poisson, Liebmann's method)** | **29 marks across 2018–2021** (31 including 2024's 2-mark theory part) — a 6-mark grid question in 2018, 2019 and twice in 2020, plus a 5-mark Poisson in 2021. Then **vanished completely in 2022 and 2023**. 2024 asked only a 2-mark theory part ("importance of boundary conditions in solving PDEs numerically"). **Both class-note analyses confirm the professor explicitly excluded PDEs from exam scope.** Pattern and class evidence agree: learn the 5-point stencil for a 2-mark theory answer, do not drill full grid solutions |
| **Eigenvalues / Eigenvectors** | Asked twice only — 2017 Q.7b and 2023 Q.3a — **with the identical matrix.** 11 marks. Cheap to prepare, non-zero chance of a third appearance |
| **Boundary Value Problems** | 2021 Q.5a/b (define + solve, 7 marks), 2024 Q.4a (theory, 3 marks) — 10 marks in total, 7 of them before the OBE reform. Trending toward theory-only |
| **Optimization** | **11 marks across two papers.** 2021 Q.6b (Newton for a maximum, 3) and Q.6d (constrained vs. unconstrained, 2); 2018 Q.5b (tabulated maximum, 6) is the same method unlabelled. So only **2 of the 11 marks is definition.** Both class-note analyses list the syllabus unit as **entirely missing from lectures**. Minimal investment justified |
| **LU Decomposition / Matrix Inversion** | One theory appearance (2017 Q.4b, 4 marks). Both class notes list it as missing from lectures |

### 4.3 Where the Numerical Marks Actually Live

**Method.** Every sub-question is classified once (see `question_tally_audit.md`). The denominator is
**all marks set**: 2017–2021 = 96 + 96 + 96 + 96 + 97 = **481**, and 2022–2024 Section A = 40 × 3 = **120**,
for **601 marks**. Note this counts *both* sections of the pre-OBE papers (they are 100% numerical) against
*Section A only* of the OBE papers (the other half is discrete mathematics, tallied in §5.2).
Per-era columns are given so the shift is visible.

| Cluster | Pre-OBE (481) | OBE Section A (120) | Combined (601) | Share |
| :--- | ---: | ---: | ---: | ---: |
| Errors + Roots of Equations | 134 | 29 | **163** | **27.1 %** |
| Interpolation + Regression | 109 | 37 | **146** | **24.3 %** |
| Linear systems (incl. circuits) | 57 | 16 | **73** | **12.1 %** |
| Integration + Differentiation | 69 | 18 | **87** | **14.5 %** |
| ODE + BVP | 66 | 13 | **79** | **13.1 %** |
| PDE + Eigenvalue + Optimization | 46 | 7 | **53** | **8.8 %** |

**The first four clusters are 469 of 601 marks = 78 % of the numerical marks.**

The most important correction here is the last row: **PDE + Eigenvalue + Optimization is 8.8 %, not the ~2 % that a casual reading of the paper list suggests.** PDE alone is 31 marks (5.2 %), spread across four consecutive papers. It is genuinely dead in the OBE era — that conclusion rests on the 2022–2024 record and the class notes, not on the small share.

---

## 5. Discrete Mathematics — Topic Frequency Analysis (2022–2024 only)

> Reminder: this section is based on **three papers and one class test**, because Discrete Mathematics did not exist in this course before 2022.

### 5.1 Master Frequency Table

| # | Syllabus Topic | 2022 | 2023 | 2024 | Papers | Marks (of 120) | CT |
| :--- | :--- | :---: | :---: | :---: | :---: | ---: | :--- |
| 1 | **Set** (operations, algebraic properties, power set) | – | – | – | **0/3** | 0 | – |
| 2 | **Relation** (binary, partial order, equivalence) | – | – | – | **0/3** | 0 | – |
| 3 | **Propositional Logic** | ✓✓✓✓✓✓ | ✓✓✓✓✓✓ | ✓✓✓✓✓✓ | **3/3** | 64 | CT-04 (all 3 Qs) |
| 4 | **Proof Techniques** (direct, contradiction, induction) | (✓) | (✓) | – | **0/3 standalone** | 0 | – |
| 5 | **Number Theory** | ✓✓✓✓✓ | ✓✓✓ | ✓✓ | **3/3** | 32 | – |
| 6 | **Counting** (inclusion-exclusion, pigeonhole, P&C) | ✓✓✓ | ✓✓✓ | ✓ | **3/3** | 17 | – |
| 7 | **Misc** ("why discrete math matters") | – | ✓ | – | 1/3 | 1 | – |
| — | **Algorithms** *(NOT in syllabus)* | – | – | ✓ | **1/3** | 6 | – |

*"(✓)" = a proof appears but embedded inside another question — 2022 Q.7d (Number Theory) and 2022 Q.8d (Counting), 2023 Q.7c (Number Theory). Never as a standalone "Proof Techniques" question.*

### 5.2 Section B Mark Distribution

| Topic | 2022 | 2023 | 2024 | Total of 120 set | Share |
| :--- | :---: | :---: | :---: | :---: | ---: |
| Propositional Logic | 20 | 20 | 24 | **64** | **53.3 %** |
| Number Theory | 14 | 10 | 8 | **32** | **26.7 %** |
| Counting | 6 | 9 | 2 | **17** | **14.2 %** |
| Algorithms (off-syllabus) | 0 | 0 | 6 | **6** | 5.0 % |
| Misc / "why discrete math matters" | 0 | 1 | 0 | **1** | 0.8 % |
| **Total** | **40** | **40** | **40** | **120** | 100 % |

Each column sums to the 40 marks set in that Section B, verified in `question_tally_audit.md` §C.

**Structural regularity — Section B follows a template that holds in 3 of 3 OBE papers:**

```
Q.5  →  Propositional Logic  (definitions, fuzzy logic, functional completeness, arguments)
Q.6  →  Propositional Logic  (circuits, equivalence, inference rules, CNF/DNF)
Q.7  →  Number Theory        (modular arithmetic, GCD, fast exponentiation)
Q.8  →  Counting             (pigeonhole, combinations, binomial theorem)
```

2024 deviates in two ways: Q.7a became an off-syllabus algorithms question, and the biconditional item moved from Q.6b to Q.7b. 2022 also folds CRT + Fermat's little theorem into Q.8a, so its "Counting" question is half Number Theory. Since you answer any 3 of 4, **mastering Logic (Q.5 + Q.6) plus either Number Theory or Counting covers the full 30 Section B marks.**

### 5.3 Tier Classification for Discrete Mathematics

**🔴 TIER 1 — Guaranteed, over half of Section B**

**Propositional Logic.** Every form it has taken:
- Definitions: proposition vs. traditional sentence (2022 Q.5a); proposition vs. propositional variable (2024 Q.5a); tautology / contradiction / contingency (2024 Q.6a)
- Truth-table proofs of tautology (2023 Q.5c, CT-04 Q.1) and of logical equivalence (2023 Q.6a)
- Valid / satisfiable / unsatisfiable classification (2024 Q.5b)
- Biconditional truth evaluation (2022 Q.6b ≡ 2024 Q.7b — **identical item**)
- English → logic translation of **system specifications**, then a consistency check (2024 Q.5c, CT-04 Q.2, CT-04 Q.3)
- **Rules of inference** — construct a valid argument from premises (2023 Q.6c); define modus ponens / modus tollens / hypothetical syllogism / disjunctive syllogism (2023 Q.6b)
- **Logic puzzles** — knights/knaves/spies (2022 Q.6a), four suspects with exactly one truth-teller (2023 Q.5b), Lewis Carroll humming-birds (2022 Q.5d)
- Functional completeness of {¬, ∧} (2022 Q.5c); rewrite using only ¬, ∨, ∧ (CT-04 Q.2b)
- **CNF / DNF conversion** from a real-world condition (2024 Q.6b)
- **Logic → digital circuit** construction (2023 Q.5a)
- Fuzzy-logic conjunction as a minimum (2022 Q.5b)

**🟠 TIER 2 — Near-certain**

**Number Theory.** The asked forms are narrow and extremely repetitive:
- `a ≡ r₁ (mod n)`, `b ≡ r₂ (mod n)` → find `c` for a linear and a cubic/quadratic combination (2022 Q.7a ≡ 2024 Q.8a; 2023 Q.7a is the same template with different numbers) — **this item has appeared in all three OBE papers**
- **Modular exponentiation**: `3^644 mod 645` (2022 Q.7b ≡ 2024 Q.8b — identical)
- **GCD via Extended Euclidean algorithm** (2022 Q.7c)
- **Chinese Remainder Theorem** + Fermat's little theorem (2022 Q.8a)
- Proof-style number theory: `(2^a − 1) mod (2^b − 1) = 2^(a mod b) − 1` (2022 Q.7d); composite `n` has a prime divisor ≤ √n (2023 Q.7c)
- Binary addition (2023 Q.7b)

> ⚠️ **Note the gap between papers and lectures on CRT.** Both class-note analyses call the Chinese Remainder Theorem a *guaranteed*, *must-study*, high-priority topic. But in the papers CRT has appeared **once in three years** (2022 Q.8a, 4 marks of 120). The resolution: CRT is cheap to prepare and is the professor's stated favourite — **prepare it, but do not mistake it for the core.** The modular-arithmetic `a ≡ r (mod n)` item is the one that appears every year.

**Counting.** Also narrow, and shrinking:
- **Pigeonhole / generalized pigeonhole** — a real-world example (2022 Q.8c ≡ 2024 Q.8c, identical; 2023 Q.8a) — **all three papers**
- Pigeonhole as a proof: among `d+1` integers, two share a remainder mod `d` (2022 Q.8d)
- Product rule (2022 Q.8b — Boston→Detroit→LA routes)
- Combinations `C(30,6)` (2023 Q.8b)
- **Binomial theorem** — coefficient extraction from `(2x − 3y)^25` (2023 Q.8c)

Counting fell from 14 marks (2022) to 10 (2023) to 2 (2024). **Only 17 of 120 Section B marks are Counting** — this is the weakest of the three Tier-1/Tier-2 blocks, and the Section B blueprint below reflects that.

**⚫ TIER 4 — Never Asked (the single most surprising finding)**

| Syllabus Unit | Appearances in 2022 / 2023 / 2024 |
| :--- | :--- |
| **Set** — operations, algebraic properties, computer representation, power set theorem | **0** |
| **Relation** — properties, binary, partial ordering, equivalence | **0** |
| **Proof Techniques** — formal proof structure, direct proof, contradiction, **mathematical induction** | **0 standalone** |
| Predicates & Quantifiers (∀ / ∃, nested) | **0** — despite being a Propositional Logic sub-unit |

Three of six Discrete Mathematics syllabus units have **never produced a single question.**

> **How to read this against the class notes.** Fahad's notes report "Sets and Logic will constitute at least 2 complete question sets," and Raidah's notes record Nadim Sir's weightage as "Sets and Functions: minimum 0.5 to 1 set" and heavy emphasis on quantifiers. **The three-year paper record contradicts both on Sets and Quantifiers.** Most probable reading **[judgement]**: the professor's "Sets and Logic" bundle resolves in practice to *Logic*, and sets/quantifiers function as teaching scaffolding rather than assessment targets. Keep sets and quantifiers at recognition level (they are also quick marks if they ever appear), but **never at the expense of Logic, Modular Arithmetic, Pigeonhole and Binomial Theorem.** Mathematical Induction is the one genuine coin-flip: it is prominent in the syllabus, absent from both sets of class notes, and absent from all three papers.

### 5.4 ⚠️ Off-Syllabus Alert: 2024 Q.7a

2024 Q.7a (6 marks, CO2) asked about **sorting algorithms, binary search with pseudocode, greedy van assignment, and time complexity** — framed as a delivery-company scenario.

**None of this is in the ECE 2213 syllabus.** There is no algorithms/complexity unit in either section. This is the only off-syllabus question in eight years, and it was worth 6 of 60 marks (5 % of the paper).

Interpretation and action: treat basic algorithmic literacy as **cheap insurance** — know one O(n log n) sort by name with its average complexity, binary search pseudocode with O(log n), and the one-line definition of a greedy strategy. That is perhaps 20 minutes of preparation covering a 6-mark risk. It also signals that the OBE "CO2" bucket is being read loosely by the setter, so a scenario-framed computing question is possible again.

---

## 6. Question Style & Framing Patterns

### 6.1 The Electrical/ECE Framing Signature

This is a Numerical Methods course taught to ECE students, and the setters consistently dress numerical problems in electrical clothing. Recognizing the wrapper is half the work:

| Framing | Where | Underlying method |
| :--- | :--- | :--- |
| DC mesh/nodal circuit → solve for currents | 2018 Q.4b, 2019 Q.3c, 2020 Q.4b, 2021 Q.7b, 2024 Q.2b | **Gauss-Seidel** (you must derive the equations via KVL/KCL first) |
| Power balance `5I² + 50I = 1000` | 2019 Q.2b | Root finding (iterative) |
| Power equation `3I² − 4I − 4 = 0` | 2020 Q.2b | Newton-Raphson, 3 iterations |
| PT-voltmeter reads 999 V instead of 1 kV | 2019 Q.1c | Error representations |
| Ammeter reads 9.05 A instead of 10 A | 2020 Q.1b | Error representations |
| Ohm's law V–I table → current at 12 V | 2019 Q.5b | Linear interpolation |
| Current-vs-voltage experiment → I at 3.5 V | 2018 Q.4c | Linear regression |
| 1 H inductor, I(t) table → voltage at t = 0.27 s | 2019 Q.6b | Numerical differentiation (`v = L·di/dt`) |
| Op-amp integrator `v₀ = −(1/RC)∫vᵢ dt` | 2020 Q.6b | Simpson's 1/3 rule |
| Capacitor losing 4% charge per second | 2021 Q.5c | Formulate + solve an ODE |
| Laplace/Poisson on a plate with boundary potentials | 2018 Q.8a, 2019 Q.8b, 2020 Q.8a/b, 2021 Q.6c | Liebmann's method (5-point stencil) |
| Gas sensor reading at t = 10 s | 2021 Q.4c | Extrapolation |
| Rocket upward velocity / vertical distance | 2018 Q.3b, 2018 Q.6a, 2023 Q.4b | Interpolation / Simpson's 1/3 |
| Robot arm laser scanning drilled holes | 2019 Q.4b | Quadratic curve fitting |

**The Discrete Mathematics section has its own parallel signature** — computing-scenario framing: university examination system (CT-04 Q.2), embedded sensor/controller (CT-04 Q.3), multiuser/kernel/interrupt-mode OS specification (2024 Q.5c), security alarm system (2024 Q.6b), unauthorized computer access investigation (2023 Q.5b), delivery-van routing (2024 Q.7a). **Expect to translate an engineering requirement into logic, not to be handed bare `p`s and `q`s.**

### 6.2 Standard Sub-Question Anatomy

Nearly every question follows a predictable internal shape:

```
(a)  2–4 marks  →  Definition / comparison / "why is this needed" theory
(b)  4–6 marks  →  The main computational problem
(c)  2–4 marks  →  A second shorter computation, or applied theory
```

**Consequence:** a large fraction of every paper is definitional theory. Measured on the OBE papers, purely definitional/conceptual items account for **~30 % of 2023 and ~38 % of 2024**; the pre-OBE papers run a little lighter. Items such as "What is pivoting?" (2 marks, 2022 Q.3c), "Define bracketing methods" (2 marks, 2021 Q.2a), "Give a real-life example of curve fitting" (2 marks, 2021 Q.4a), "Compare Simpson's 1/3 and 3/8" (3 marks 2020 Q.6a, 2 marks 2023 Q.4c), "Briefly describe the pigeonhole principle with a real-world example" (2 marks, 2023 Q.8a) are free marks for anyone who has prepared one-paragraph answers. These items repeat far more aggressively than the computations.

### 6.3 Recurring Instruction Conventions

- Iteration counts are almost always capped: *"use three iterations only"* (2017 Q.4c), *"use four iterations only"* (2017 Q.2c), *"show two iterations only"* (2019 Q.3c), *"up to two iterations"* (2024 Q.2a). **Do not over-compute** — marks are for the tabulated iterations requested.
- Step sizes are almost always given: `h = 0.1`, `h = 0.2`, `h = 0.02` (2017 Q.8a), and the Romberg triple `h = 0.5 / 0.25 / 0.125` (2021 Q.8b, 2023 Q.2c).
- Integration questions frequently chain **(i) compute → (ii) true error → (iii) absolute relative true error** (2018 Q.6a, 2023 Q.4b). Prepare that three-part habit.
- Several questions ask you to **derive** rather than apply: Newton's forward formula (2020 Q.5a, 2021 Q.3c, 2023 Q.2a), Newton-Raphson (2021 Q.1b, 2023 Q.1c), modified Euler (2020 Q.7a), trapezoidal rule (2021 Q.8a), Simpson's 1/3 (2019 Q.7a), second-derivative formula (2017 Q.6c), linear regression normal equations (2019 Q.4c). Derivations are a distinct, heavily-recurring skill.

---

## 7. ⭐ Repeat Question Register — The Highest-Value Section

All 22 pairs below were checked against the source papers. **15 are verbatim** (identical data and near-identical wording), **4 are near-verbatim** (identical method and data with one value changed), **3 are same-concept** (identical syllabus topic, reworded).

### 7.1 Verbatim & Near-Verbatim Repeats

| # | Question | First Appearance | Repeat(s) | Match | Type |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | Relative error of `u = 5xy²/z³` at x=y=z=1, errors 0.001 | **2017 Q.3b** | **2023 Q.1b** | Verbatim | Verbatim |
| 2 | Eigenvalues & eigenvectors of `A = [[5,0,1],[0,−2,0],[1,0,5]]` | **2017 Q.7b** | **2023 Q.3a** | Verbatim, same matrix | Verbatim |
| 3 | Jacobi: `6x+y+z=20`, `x+4y−z=6`, `x−y+5z=7` | **2017 Q.7a** | **2022 Q.4a** | Verbatim | Verbatim |
| 4 | Fit a straight line, x = 1…7, y = 0.5, 2.5, 2, 4, 3.5, 6, 5.5 | **2017 Q.6b** | **2024 Q.3c** | Verbatim | Verbatim |
| 5 | Least squares `y = a·e^(bx)`, x = 2…10, y = 4.077…222.62 | **2017 Q.5b** | **2020 Q.3c** | Same data; 2020 prepends "define curve fitting" | Near-verbatim |
| 6 | Decennial census population 46, 66, 81, 93, 101 | **2017 Q.5c** (1921–1961 → 1955) | **2020 Q.3b** (1891–1931 → 1895 & 1925), **2024 Q.3b** (1921–1961 → 1995) | Same five population values, 3 papers, target year changed | Near-verbatim |
| 7 | Rocket distance `∫₈³⁰(2000 ln[140000/(140000−2100t)] − 9.8t)dt` → Simpson's 1/3 + true error + absolute relative error | **2018 Q.6a** | **2023 Q.4b** | Verbatim (2018 specifies eight segments; 2023 does not) | Verbatim |
| 8 | Derive Newton's forward interpolation formula | **2021 Q.3c** | **2023 Q.2a** | Verbatim, same displayed formula | Verbatim |
| 9 | Lagrange `y(2)` from x = 0,1,3,4,5; y = 0,1,81,256,625 | **2021 Q.3d** | **2023 Q.2b** | Verbatim | Verbatim |
| 10 | Romberg's method for `∫₁² dx/(2+x)`, h = 0.5, 0.25, 0.125 | **2021 Q.8b** | **2023 Q.2c** | Verbatim | Verbatim |
| 11 | Euler's method, `dy/dx = (3/5)x³y`, `y(0) = 1` | **2021 Q.8c** | **2023 Q.3b(i)** | Verbatim | Verbatim |
| 12 | Derive Newton-Raphson + discuss its problems + how to solve them | **2021 Q.1b** | **2023 Q.1c** | Verbatim — 2023 reprints the typo "discuss this problems of it" | Verbatim |
| 13 | Compare Simpson's 1/3 and 3/8 rules | **2020 Q.6a** | **2023 Q.4c** | Verbatim | Verbatim |
| 14 | Three-mesh DC circuit → `I₁, I₂, I₃` by Gauss-Seidel | **2020 Q.4b** (400 V, 10 A, 20/40/10/100 Ω) | **2024 Q.2b** (500 V, 5 A, 10/20/100 Ω) | Same method, same I₁/I₂/I₃ naming; 2020 has four resistors, 2024 three | Near-verbatim |
| 15 | Biconditionals true/false: `2+2=4 iff 1+1=2`; `1+1=2 iff 2+3=4`; `1+1=3 iff monkeys can fly`; `0>1 iff 2>1` | **2022 Q.6b** | **2024 Q.7b** | Verbatim, all four items | Verbatim |
| 16 | `a ≡ 11 (mod 19)`, `b ≡ 3 (mod 19)` → find `c` for `7a+3b` and `a³+4b³` | **2022 Q.7a** | **2024 Q.8a** | Verbatim | Verbatim |
| 17 | `3^644 mod 645` using a well-known algorithm | **2022 Q.7b** | **2024 Q.8b** | Verbatim | Verbatim |
| 18 | Real-world example of the generalized pigeonhole principle | **2022 Q.8c** | **2024 Q.8c** | Verbatim | Verbatim |
| 19 | "What is pivoting / why is pivoting important / partial vs. complete pivoting" | **2017 Q.4a** | **2019 Q.3b**, **2021 Q.7a**, **2022 Q.3c** | Same concept, 4 papers | Same-concept |
| 20 | Define / distinguish interpolation, extrapolation, curve fitting | **2017 Q.5a** | **2019 Q.5a**, **2020 Q.3a**, **2021 Q.3a**, **2023 Q.4a**, **2024 Q.3a** | Same concept, **6 papers** (2020 Q.3a covers only interpolation vs. extrapolation) | Same-concept |
| 21 | ODE `dy/dx = x + y`, h = 0.2 / 0.1 | **2020 Q.7b** (y(0)=0, Euler) | **2024 Q.4b** (y(0)=1, RK4) | Same ODE, initial value and method changed | Near-verbatim |
| 22 | "Why do ECE engineers require numerical methods / numerical vs. analytical" | **2019 Q.1a** | **2021 Q.1a**, **2023 Q.1a** | Same concept | Same-concept |

**Known omissions from the register** (same method and topic as an earlier paper, but reworded or re-parameterised — treat these as *topical* echoes rather than counted repeats):
2021 Q.1a/2a → 2022 Q.1a (bracketing); 2021 Q.1c → 2022 Q.1b (Taylor evaluation);
2021 Q.3b/3d → 2022 Q.1c (Lagrange); 2021 Q.3c → 2022 Q.2c (Newton forward);
2021 Q.7a → 2022 Q.3c (pivoting); 2021 Q.8b → 2022 Q.3a (Romberg);
2018 Q.8a → 2020 Q.8b (Liebmann); 2019 Q.3c/2019 Q.2a → 2024 Q.2a (root-finding framing).

### 7.2 Recycling Rate by Paper

**Method.** Marks of sub-questions that appear in the §7.1 register (verbatim, near-verbatim, and same-concept rows),
divided by marks set in that paper or section. Topical echoes listed in §7.1's omission note are **excluded**
from the count — including them is a judgement call and moves every figure up by 10–25 points.

| Paper / Section | Marks set | Recycled marks | Share | Primary source |
| :--- | ---: | ---: | ---: | :--- |
| **2023 Section A** | 40 | 37.5 | **≈ 94 %** | 2021 (items 8, 9, 10, 11, 12) + 2017 (1, 2) + 2018 (7) + 2020 (13) + concepts 20, 22 |
| **2024 Section A** | 40 | 17 (+2 concept) | **42.5 %** (47.5 %) | 2017 (4, 6) + 2020 (14, 21) |
| **2024 Section B** | 40 | 14 (+2 concept) | **35.0 %** (40.0 %) | 2022 (items 15, 16, 17, 18) |
| **2022 Section A** | 40 | 4 | **10.0 %** | 2017 (3) |
| **2020** | 96 | 9 | **9.4 %** | 2017 (5, 6) |

**Reading these numbers honestly:**
- **2023 is the extreme case.** Every one of its four Section A questions is a repeat. The only genuinely new sub-question in the whole section is **2023 Q.3b(ii)**, `dy/dx = 1+y², y(0) = 0`.
- **2024's two halves recycle very differently.** Section A draws on the pre-OBE bank at ~43 %; Section B draws on 2022 at only **35 %**. 2024 Q.5b, Q.5c, Q.6a, Q.6b and Q.7a have **no precedent in 2022** — no validity classification, no system-specification consistency check, no CNF/DNF work. Section B in the OBE era is *recurring*, not *recycled*.
- **2020 and 2022 are the least recycled papers** in the set, both under 10 %. Earlier drafts of this report claimed ~35 % and ~25 % for them; those figures were not reproducible and are withdrawn.

### 7.3 What This Means Operationally

1. **2021 is the master paper; 2022 is the master paper for Section B only.** 2023 is very largely 2021 recycled (≈94 %). 2024's Section B reuses four items from 2022 but is otherwise new. If time is short: **solve 2021 in full, then 2022 Section B, then 2023 and 2024 to see the recycling in action.**
2. **The 2017 paper is still live.** Four of its items resurfaced in 2022, 2023 and 2024 — six to seven years later. Do not dismiss it as obsolete.
3. **Theory items recycle hardest.** "Define interpolation/extrapolation/curve fitting" has appeared in six of eight papers. "What is pivoting" in four. These are the most reliably bankable marks in the course.
4. **Typos travel with the question.** 2023 Q.1c reprints "discuss this problems of it" from 2021 Q.1b — direct evidence of copy-paste question setting rather than fresh authoring. So do the smaller ones: 2022 Q.8b's "Los Angles", 2018 Q.4c's "linier", 2024 Q.4b's "circulation", 2024 Q.7b's "true of false".
5. **When a repeat appears, the data is reused but the target may shift.** The census problem kept the same five population values across three papers while moving the requested year (1955 → 1895 & 1925 → 1995), which switches the required method between **Newton's forward**, **Newton's backward** and **extrapolation**. Prepare the *data set*, not a memorized answer.

---

## 8. Class Test Analysis

Four class tests were available. They are structurally different from the finals and reveal the OBE assessment style more sharply.

| Test | Marks | Time | Topics | Style |
| :--- | :---: | :---: | :--- | :--- |
| **CT-01** | 20 | 20 min | Modelling & error sources; Bisection vs. Regula Falsi | **Pure scenario-based, no computation** |
| **CT-02 Set A** | not stated | 25 min | Lagrange interpolation; Newton's forward/backward interpolation | Applied computation, real-world data |
| **CT-02 Set B** | 20 | 40 min | Gauss-Seidel (4 iterations + absolute error); RK2 & RK4 | Heavy computation, multi-part |
| **CT-04** | 20 | 30 min | Tautology by complete truth table; requirement → logic translation, ¬∨∧ rewrite, truth table; three-statement conjunction containing **"unless"** → satisfying assignments | Pure propositional logic |

### 8.1 Key Observations

**CT-01 is the clearest signal of OBE question design.** Neither question asks for a number. Q.1 presents a reactor-temperature simulation with 5-significant-digit storage and a 4-term Taylor truncation, and asks you to *build the mathematical model, state your assumptions, and identify three sources of numerical error with their effect*. Q.2 asks you to *compare* Bisection and Regula Falsi on application conditions, convergence behaviour and suitability for a safety-critical system, then diagnose **why Regula Falsi stagnates by updating only one endpoint** and propose an improvement.

This is the CO1-style "analyze and justify" question. It maps directly onto the finals' recurring comparison items (2020 Q.2a "list the comparisons among bisection, secant, false position and Newton-Raphson"; 2022 Q.1a "difference between open and bracketing method"). **The Regula Falsi one-sided-stagnation point and its fix (the modified/Illinois false-position method) is a specific, named, high-probability answer worth memorizing** — no final has asked it, so it rests on class-test evidence alone.

**CT-02 Set A/B split confirms the examinable core of the numerical half.** Between the two sets: Lagrange, Newton forward/backward, Gauss-Seidel, RK2, RK4 — exactly the Tier-1/Tier-2 list from Section 4. Set B also demands **absolute error between the third and fourth iterations** and **comparison of RK2 against RK4** — error quantification and method comparison, not just the march.

**CT-04 is 100% propositional logic** and reinforces the finals' pattern precisely:
- Q.1 — prove `[(p→q) ∧ (q→r)] → (p→r)` is a tautology by complete truth table. Note that **2024 Q.5b** asked about the related formula `(p→q) ∧ (q→r)`, and **2023 Q.6c** is the inference-rule version of the same hypothetical-syllogism idea. The same logical skeleton appears in three places.
- Q.2 — translate a university examination requirement ("if and only if the student is authenticated and the server is available"), then **rewrite using only ¬, ∨, ∧** (compare 2022 Q.5c on the functional completeness of {¬, ∧}), then truth-table it.
- Q.3 — translate three statements, one of which uses **"unless"** ("the controller does not receive data unless the sensor is active"), conjoin them, truth-table, and find the satisfying assignments.

> The **"unless"** connector in CT-04 Q.3 deserves flagging: both class-note analyses specifically warn about it (Fahad's notes list `unless → p → q`; Raidah's notes list "unless" among tricky connectors). Class tips, class notes and the class test all converge on this one point — it is as close to a guaranteed trap as the record offers.

### 8.2 CT → Final Mapping

| CT item | Corresponding final-exam items |
| :--- | :--- |
| CT-01 Q.1 (model + 3 error sources) | 2024 Q.1a, 2024 Q.1c, 2019 Q.1b, 2020 Q.1a, 2018 Q.1b |
| CT-01 Q.2 (bisection vs. regula falsi) | 2020 Q.2a, 2022 Q.1a, 2017 Q.2a, 2019 Q.2c |
| CT-02A Q.1 (Lagrange) | 2021 Q.3d, 2023 Q.2b, 2018 Q.3a, 2018 Q.3c, 2024 Q.2c |
| CT-02A Q.2 (Newton fwd/bwd) | 2020 Q.3b, 2020 Q.5a, 2021 Q.3c, 2023 Q.2a, 2017 Q.5c |
| CT-02B Q.1 (Gauss-Seidel + error) | 2017 Q.4c, 2019 Q.3c, 2020 Q.4b, 2021 Q.7b, 2024 Q.2b |
| CT-02B Q.2 (RK2 & RK4) | 2017 Q.8b, 2018 Q.7b, 2020 Q.7c, 2024 Q.4b |
| CT-04 Q.1 (tautology by truth table) | 2023 Q.5c (truth-table proof), 2024 Q.5b (validity of the same (p→q)∧(q→r) skeleton), 2024 Q.6a (tautology/contradiction/contingency concepts) |
| CT-04 Q.2, Q.3 (requirement → logic) | 2024 Q.5c, 2024 Q.6b, 2022 Q.5c |

**Every class test topic reappears in the finals.** The class tests are a reliable preview, not a separate syllabus.

---

## 9. Syllabus Coverage Audit

How much of the official syllabus has actually ever been examined? Counted against the syllabus as written in
`ECE2213_Syllabus.md` — 22 Numerical Methods bullets, 31 Discrete Mathematics bullets.

### 9.1 Numerical Methods

| Syllabus Item | Examined? | Evidence |
| :--- | :--- | :--- |
| Mathematical modeling & engineering problem solving | ✅ Yes | 2024 Q.1a, CT-01 Q.1a |
| Programming and software | ❌ **Never** | — |
| Approximations and round-off errors | ✅ Heavily | Every paper |
| Truncation errors and the Taylor series | ✅ Heavily | 2017 Q.1c, 2018 Q.1c, 2021 Q.1c, 2022 Q.1b, 2024 Q.1b |
| Bracketing methods | ✅ 6 of 8 | 2017 Q.3c, 2018 Q.2a, 2020 Q.2a, 2021 Q.2a/b, 2022 Q.1a, 2024 Q.2a — **absent 2019 and 2023** |
| Open methods | ✅ 7 of 8 applied | 2017 Q.2a/c, 2018 Q.2c, 2019 Q.2c, 2020 Q.2b, 2021 Q.1b, 2023 Q.1c; named in 2022 Q.1a — **2024 has none (its only root item is bisection)** |
| Roots of polynomials | ✅ Yes | 2017 Q.2c, 2021 Q.2c, 2024 Q.2a |
| Gauss elimination | ✅ Yes | 2019 Q.3a, 2020 Q.4a, 2022 Q.4b |
| LU decomposition & matrix inversion | ⚠️ Once, theory only | 2017 Q.4b |
| Gauss-Seidel | ✅ Heavily | 2017, 2018, 2019, 2020, 2021, 2024, CT-02B |
| Least-square regression | ✅ Yes, 6 of 8 | 2017, 2018, 2019, 2020, 2022, 2024 (absent 2021 and 2023) |
| Interpolation (one variable) | ✅ Heavily | Every paper |
| Interpolation with two independent variables | ❌ **Never** | — |
| Formation of difference tables | ✅ Yes | 2020 Q.5a, 2021 Q.3c, 2022 Q.2c, 2023 Q.2a |
| Newton's forward & backward difference | ✅ Heavily | 2018 Q.5a, 2020 Q.3b/5a, 2021 Q.3c, 2022 Q.2c, 2023 Q.2a, CT-02A |
| Lagrange's interpolation | ✅ Heavily | 2018 Q.3a/3c, 2021 Q.3d, 2022 Q.1c, 2023 Q.2b, 2024 Q.2c, CT-02A |
| Newton-Cotes integration formulas | ✅ Heavily | 2018, 2019, 2020, 2021, 2022, 2023 (absent 2017 and 2024) |
| Integration of equations | ❌ **Never** | The nearest items (2018 Q.6a, 2020 Q.6b, 2022 Q.3a, 2023 Q.4b) are all **definite integrals of a known function**, not integration of differential equations |
| One-dimensional unconstrained optimization | ⚠️ Once as a computation | 2021 Q.6b (3), Q.6d (2). 2018 Q.5b asks for a tabulated maximum by the same method |
| Runge-Kutta methods | ✅ Heavily | 2017, 2018, 2020, 2024, CT-02B (Euler/Heun in 2017, 2018, 2019, 2020, 2021, 2023) |
| Boundary-value problems | ⚠️ Twice | 2021 Q.5a/b (7), 2024 Q.4a (3, theory) |
| Eigenvalue problems | ⚠️ Twice, same matrix | 2017 Q.7b, 2023 Q.3a |
| Numerical solution of PDEs | ⚠️ 2018–2021 only, then dropped | 2018 Q.8a, 2019 Q.8b, 2020 Q.8a/b, 2021 Q.6c, 2024 Q.4c (theory) |

**Verdict.** Examined at least once: **19 of 22 syllabus bullets (86 %)**. Examined repeatedly / heavily:
**15 of 22 (68 %)**. **Three bullets have never been examined**: programming and software; interpolation with
two independent variables; integration of equations. A single "coverage" figure hides the important fact that
four more bullets (LU/matrix inversion, interpolation with two variables, integration of equations, 1-D
optimisation) have been examined at most once and only as theory.

### 9.2 Discrete Mathematics

| Syllabus Item | Examined? | Evidence |
| :--- | :--- | :--- |
| Operations on sets | ❌ **Never** | — |
| Algebraic properties of set | ❌ **Never** | — |
| Computer representation of set | ❌ **Never** | — |
| The power set theorem | ❌ **Never** | — |
| Properties of relation / binary relations | ❌ **Never** | — |
| Partial ordering relations | ❌ **Never** | — |
| Equivalence relations | ❌ **Never** | — |
| Propositional syntax | ✅ Yes | 2022 Q.5a, 2024 Q.5a |
| Semantics | ✅ Yes | 2022 Q.5a, 2024 Q.5a |
| Valid / satisfiable / unsatisfiable formulas | ✅ Yes | 2024 Q.5b |
| Encoding & validity of logical arguments | ✅ Heavily | 2022 Q.5d/6a, 2023 Q.5b/6c, 2024 Q.5c, CT-04 |
| Predicate and quantifier | ❌ **Never** | — |
| Universal & existential quantification | ❌ **Never** | — |
| Modus ponens and modus tollens | ✅ Yes | 2023 Q.6b, 2023 Q.6c |
| Structure of formal proofs / direct proofs | ⚠️ Embedded only | 2022 Q.7d, 2022 Q.8d, 2023 Q.7c |
| Proof by contradiction | ❌ **Never** | — |
| Mathematical induction | ❌ **Never** | — |
| Theorem of arithmetic | ⚠️ Indirect only | 2023 Q.7c uses the lemma "composite n has a prime divisor ≤ √n" but never states or uses unique prime factorisation |
| Modular arithmetic | ✅ Heavily | 2022 Q.7a/b, 2023 Q.7a, 2024 Q.8a/b |
| GCD, LCM | ⚠️ GCD only | 2022 Q.7c (LCM never) |
| Prime number | ✅ Yes | 2023 Q.7c |
| Congruence | ✅ Heavily | 2022 Q.7a, 2023 Q.7a, 2024 Q.8a |
| Application of congruence | ✅ Heavily | 2022 Q.7a/b/8a, 2023 Q.7a, 2024 Q.8a/b |
| Application of number theory | ✅ Yes | 2022 Q.7d, 2023 Q.7c, 2023 Q.7b (binary addition) |
| Chinese Remainder Theorem | ⚠️ **Once only** | 2022 Q.8a (4 marks of 120) |
| Basic counting techniques | ✅ Yes | 2022 Q.8b (product rule, Boston→Detroit→LA) |
| Inclusion and exclusion | ❌ **Never** | — |
| Pigeonhole principle | ✅ All 3 papers | 2022 Q.8c/8d, 2023 Q.8a, 2024 Q.8c |
| Permutation | ❌ **Never** | — |
| Combination | ✅ Yes | 2023 Q.8b |
| *Binomial theorem* (not explicitly in syllabus) | ✅ Yes | 2023 Q.8c |
| *Algorithms & complexity* (**not in syllabus**) | ⚠️ Once | 2024 Q.7a (6 marks) |

**Verdict.** By syllabus unit: Set **0/4**, Relation **0/4**, Propositional Logic **5/7**, Proof Techniques **0/4**,
Number Theory **7/8**, Counting **2/4**. Overall **14 of 31 bullets examined = 45 %**. The Discrete Mathematics
half is examined far more narrowly than it is written.

---

## 10. Predicted Question Blueprint

Based on eight years of structural regularity and the recycling patterns of Section 7.

### 10.1 Section A — Numerical Methods (answer 3 of 4, 30 marks)

| Q | Most likely content | Confidence |
| :--- | :--- | :---: |
| **Q.1** | Errors & modeling: numerical vs. analytical / why ECE needs numerical methods (2–4 m) + round-off vs. truncation **or** error representations on an instrument reading (3–4 m) + Taylor series to a stated accuracy or truncation-error estimate (3–4 m) | **Very High** — this exact question sat at Q.1 in **8 of 8** papers |
| **Q.1 or Q.2** | Roots of equations: open vs. bracketing comparison **or** Newton-Raphson derivation with its failure modes (2–4 m) + numeric iterations on a cubic or a current equation (3–4 m). **Position note:** Q.1 in 2021, 2022, 2023; Q.2 in 2017, 2018, 2019, 2020, 2024 | **Very High** on content, **Medium** on position |
| **Q.2 / Q.3** | Curve fitting: define interpolation / extrapolation / curve fitting (2–3 m) + the census population problem **or** a Lagrange/Newton table estimate (4 m) + least-squares straight line or exponential fit (3–4 m) | **Very High** |
| **Q.2 / Q.4** | Gauss-Seidel on a DC circuit (4 m) — highest-yield single item, present in 4 of the last 5 papers | **High** |
| **Q.3 / Q.4** | Integration **or** ODE: Simpson's 1/3 with true & absolute relative error, **or** Romberg, **or** RK4/Euler march with h = 0.1–0.2 (4–5 m) + BVP vs. IVP theory or PDE boundary-condition theory (2–3 m) | **High** |

### 10.2 Section B — Discrete Mathematics (answer 3 of 4, 30 marks)

| Q | Most likely content | Confidence |
| :--- | :--- | :---: |
| **Q.5** | Propositional logic foundations: definitions (proposition vs. sentence, proposition vs. variable, tautology/contradiction/contingency) (2–4 m) + validity/satisfiability or a truth-table tautology proof (4 m) + translate a system specification and test consistency (4 m) | **Very High** |
| **Q.6** | Propositional logic applications: logical equivalence proof, rules of inference (modus ponens/tollens, syllogisms), CNF/DNF conversion, logic→digital circuit, **or** a knights/knaves/truth-teller puzzle | **Very High** |
| **Q.7** | Either Number Theory (as in 2022 and 2023: `a ≡ r₁ (mod n)`, `b ≡ r₂ (mod n)` → find `c`; modular exponentiation; Extended Euclidean GCD; a short number-theoretic proof) **or** an off-syllabus algorithms item (as in 2024). A biconditional item may land here too | **High** on Number Theory, **Medium** on the 2024 deviation repeating |
| **Q.8** | Counting: generalized pigeonhole with a real-world example (2 m) + combinations (3 m) + binomial coefficient extraction (4 m). **Note the trend:** Counting fell to 2 marks in 2024; expect roughly 2–10 marks here, not a full question | **High** on pigeonhole, **Medium** on combinations/binomial |

### 10.3 Highest-Probability Specific Items

Ranked by evidence strength across papers, class tests and class notes:

1. **Define/distinguish interpolation, extrapolation, curve fitting** — 6 of 8 papers
2. **Error representations applied to an instrument reading** — 2019, 2020, plus error theory in all 8
3. **Newton-Raphson derivation + its problems + the fix** — 2017, 2019, 2021, 2023
4. **Decennial census population estimate** (46, 66, 81, 93, 101) — 2017, 2020, 2024
5. **Gauss-Seidel on a DC mesh circuit** — 2018, 2019, 2020, 2021, 2024 + CT-02B
6. **Lagrange interpolation on a small table** — 2018, 2021, 2022, 2023, 2024 + CT-02A
7. **Derive Newton's forward interpolation formula** — 2020, 2021, 2023
8. **Simpson's 1/3 + true error + absolute relative true error** (rocket integral) — 2018, 2023
9. **Compare Simpson's 1/3 vs. 3/8** (n even vs. n multiple of 3) — 2020, 2023
10. **RK4 / modified Euler march, h = 0.1 or 0.2** — 2017, 2018, 2020, 2024 + CT-02B
11. **What is pivoting / partial vs. complete** — 2017, 2019, 2021, 2022
12. **Translate a system specification into logic and test consistency** — 2024 + CT-04 ×2
13. **Truth-table proof of a tautology** (hypothetical-syllogism skeleton) — 2023, 2024, CT-04
14. **Biconditional truth evaluation** (the four-item set) — 2022, 2024
15. **`a ≡ r (mod n)` combination → find `c`** — 2022, 2023, 2024 (**all three OBE papers**)
16. **`3^644 mod 645`** — 2022, 2024
17. **Generalized pigeonhole, real-world example** — 2022, 2023, 2024 (**all three OBE papers**)
18. **Rules of inference / modus ponens & tollens** — 2023 ×2, flagged as high-yield in both class notes
19. **Chinese Remainder Theorem** — 2022 only (4 marks), but called "guaranteed" by both class-note sets
20. **Binomial coefficient extraction** — 2023 only; natural partner to the combinations item

---

## 11. Strategic Recommendations

### 11.1 Priority Ordering

**Phase 1 — Lock the guaranteed marks (highest return per hour)**
- All error definitions and representations; Taylor series to a stated decimal accuracy; round-off vs. truncation. **This is Q.1 in 8 of 8 papers — start here.**
- Bisection, Regula Falsi, Newton-Raphson, Secant: derivation, algorithm steps, limitations, and the full four-way comparison table
- Lagrange + Newton forward/backward/divided-difference interpolation, including the difference table
- Least-squares straight line and the `y = a·e^(bx)` linearization
- Gauss-Seidel, specifically the **circuit → KVL/KCL → iterate** pipeline
- Propositional logic end to end: truth tables, translation (watch **"unless"**, "only if", "however"), tautology/contradiction/contingency, logical equivalence, CNF/DNF, rules of inference
- Modular arithmetic: `a ≡ r (mod n)` combinations and fast modular exponentiation
- Pigeonhole (including the generalized form) with a ready real-world example

**Phase 2 — Secure the near-certain block**
- Trapezoidal, Simpson's 1/3, Simpson's 3/8 (with the n-even / n-multiple-of-3 constraints), Romberg; the true-error and absolute-relative-true-error triple
- Euler, Modified Euler/Heun, RK2, RK4 marches; second-order ODE reduced to a system
- Numerical differentiation: forward-difference first and second derivatives from a table
- Jacobi, Gauss elimination, pivoting theory, ill-conditioned systems, relaxation
- Extended Euclidean algorithm (tabular form), Chinese Remainder Theorem, combinations, binomial theorem

**Phase 3 — Cheap insurance (low time, non-zero payoff)**
- Eigenvalues of the recurring 3×3 matrix (it has appeared twice unchanged, 11 marks total)
- Liebmann 5-point stencil — enough for a 2-mark theory answer on PDE boundary conditions. *Note: PDE was worth 31 marks across 2018–2021, so this is cheap relative to what it once was — but it has not appeared since 2021.*
- One-dimensional unconstrained optimization: Newton's method for a maximum; constrained vs. unconstrained definition
- BVP vs. IVP distinction
- One sorting algorithm with its average complexity, binary search pseudocode with O(log n), the definition of a greedy strategy (covers the 2024 Q.7a style)
- LU decomposition concept (theory only)

**Phase 4 — Only if time remains**
- Sets, Relations, Mathematical Induction, Predicates & Quantifiers, Inclusion-Exclusion, Permutation, LCM. These are in the syllabus but have **never been examined** in the OBE era. Mathematical Induction is the most defensible item here, being a named syllabus topic absent from both class-note sets.

### 11.2 Exam-Day Tactics

1. **Read the N.B. and confirm the section split.** You must answer exactly 3 from each section on separate scripts. 30 marks are locked behind Discrete Mathematics — there is no way to substitute numerical answers for them.
2. **Harvest the theory parts first.** Roughly 30–38 % of an OBE paper is definitions and comparisons. Sweep every (a) part across your six chosen questions before starting any long computation.
3. **Respect the iteration cap.** "Three iterations only" means three. Tabulate them cleanly — the tabulation itself earns marks.
4. **Scan for a repeat before you start computing.** Given the recycling rate, at least one question per section will likely be one you have already solved from a previous paper.
5. **For circuit questions, write the KVL/KCL equations explicitly before iterating.** The equation formulation carries marks independently of the iteration arithmetic.
6. **Check the target value in table problems.** The census data is identical across three papers while the requested year changed, flipping the method between forward difference, backward difference and extrapolation.
7. **Finish integration questions completely.** If the question chains (i) value → (ii) true error → (iii) absolute relative true error, all three parts are marked.
8. **Do not over-invest in Section B Counting.** It is 17 of 120 Section B marks and shrank to 2 marks in 2024. Cover pigeonhole and the binomial theorem; treat permutations and inclusion-exclusion as optional.

### 11.3 Residual Risks

| Risk | Evidence | Mitigation |
| :--- | :--- | :--- |
| A Sets / Relations / Induction question finally appears | Three syllabus units with 0/3 appearances; both class notes flag them as lecture gaps | Phase 4 — recognition-level prep only; they are low-mark items if they come |
| Another off-syllabus computing question | 2024 Q.7a (6 marks) | Phase 3 insurance item — 20 minutes of prep |
| PDE returns | 4 consecutive appearances 2018–2021 (29 marks), then absent 2022–2023 | Learn the 5-point stencil; both class notes report explicit exclusion, so do not drill grids |
| Quantifiers appear | Both class notes emphasize them heavily (∀→implication, ∃→conjunction) but 0/3 in papers | Memorize the two translation rules of thumb — that is nearly all that is ever asked |
| CRT appears despite one appearance | Called "guaranteed" by both class-note sets | Phase 2 — it is a short algorithm, prepare it |
| Roots of equations lands at Q.2, not Q.1 | Q.1 in 2021–2023, Q.2 in the other five | Do not anchor on position; scan Q.1 and Q.2 both before choosing your three Section A questions |

---

## 12. Conclusion

ECE 2213 is an unusually predictable examination, for three reasons that reinforce each other.

**First, the structure has not moved in eight years.** Eight questions, answer six, three per section, separate scripts, a theory part and a computation part inside nearly every question. Only the marks total and the Section B subject matter changed — both at the single 2022 OBE boundary.

**Second, the question bank is small and openly reused.** 22 repeat pairs are on record: 15 verbatim down to the typographical errors, 4 near-verbatim, 3 same-concept. 2023's Section A is roughly **94 %** traceable to 2021, 2017, 2018 and 2020 — its only new sub-question is `dy/dx = 1+y²`. 2024's Section B reuses four items from 2022 but is otherwise new, so the OBE Section B is *recurring* rather than *recycled*. The practical conclusion is blunt: **working through 2021 in full, then 2022, then 2023 and 2024, covers more of the likely paper than any textbook chapter would.**

**Third, the examined syllabus is much narrower than the written syllabus.** On the numerical side, four clusters — errors, roots, interpolation/regression, and linear systems — account for **469 of the 601 numerical marks set (78 %)**, while Optimization, PDEs, Eigenvalues and Boundary-Value Problems together account for only **63 marks (10.5 %)**, and over 80 % of that before 2022. On the discrete side, Propositional Logic alone is **53 %** of Section B, and three of six syllabus units have never been asked at all.

**The one structural trap** is the 50/50 section lock introduced in 2022. In the pre-OBE papers a strong numerical student could answer all six questions from numerical methods. From 2022 that is impossible: 30 marks sit behind Discrete Mathematics, and the only route to them is Propositional Logic, Modular Arithmetic and Counting. Fortunately those three are also the most repetitive, most narrowly-scoped and cheapest-to-prepare topics in the entire course.

---

*Report derived from: 2017.md, 2018.md, 2019.md, 2020.md, 2021.md, 2022.md, 2023.md, 2024.md, ClassTestQuestions.md, ECE2213_Syllabus.md*
*Arithmetic backing and full sub-question tally: `question_tally_audit.md`*