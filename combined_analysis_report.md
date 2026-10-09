---
course_code: ECE 2213
course_title: Numerical Methods & Discrete Mathematics
document_type: Combined Analysis Report
sources:
  - PreviousYearAnalysisReport.md (2017-2024 papers + Class Tests)
  - question_tally_audit.md (per-sub-question mark tally; arithmetic backing)
  - Analysis_report_classnote_Fahad.md + raw class notes
  - Analysis_report_classnote_Raidah.md + raw class notes
  - ECE2213_Syllabus.md
tags:
  - combined-analysis
  - ece2213
  - exam-strategy
  - numerical-methods
  - discrete-mathematics
---

# ECE 2213 — Combined Analysis Report
## Previous Year Questions × Class Notes × Syllabus

**Institution:** Rajshahi University of Engineering & Technology (RUET)
**Department:** Electrical & Computer Engineering
**Course:** ECE 2213 — Numerical Methods & Discrete Mathematics (3.00 Credits)

**Inputs synthesized:**
1. `PreviousYearAnalysisReport.md` — 8 semester finals (2017–2024) + 4 class tests
2. `question_tally_audit.md` — per-sub-question mark tally backing every number below
3. Fahad's class notes (raw) + `Analysis_report_classnote_Fahad.md`
4. Raidah's class notes (raw) + `Analysis_report_classnote_Raidah.md`
5. `ECE2213_Syllabus.md` — official syllabus

> **Two epistemic caveats that shape everything below.**
>
> **1. The lecture slides are not in evidence.** Both note sets record an instructor instruction that the
> slides are **mandatory** reading, and Fahad's notes state that nested-quantifier and algorithm-proof
> questions are "taken directly from the department lecture slides." Every conclusion touching
> quantifiers, sets or proof techniques therefore rests on a **visibility gap**, flagged in place.
>
> **2. The two note sets are not fully independent — and this matters.** Both cohorts had **Nadim Sir** for
> Numerical Methods and Discrete Mathematics. Numerical Methods was additionally delivered by
> **Faysal Sir** in Fahad's cohort and by **NRP Sir** in Raidah's cohort. So for **Discrete Mathematics the
> two note sets are two students' records of the same instructor's lectures** — a verbal tip appearing in
> both is *one* piece of evidence recorded twice, not two independent confirmations. This document does not
> count shared-Discrete-Mathematics tips as cross-validated (§3.2).

> **How to check this report.** Every frequency, mark count and share is taken from
> `question_tally_audit.md`, which lists all **183** sub-questions with their marks and a topic cluster
> (721 marks = 601 numerical + 120 discrete). Class-note claims are quoted from the **raw notes**, with
> line-level provenance where it matters. Statements tagged **[judgement]** are opinion, not measurement.

---

## 1. Executive Summary

Three evidence streams were cross-referenced: **what has actually been asked** (8 years of papers),
**what was actually delivered** (two students' notes), and **what is officially required** (the syllabus).
They disagree in useful, exploitable ways.

### The headline findings

| # | Finding | Consequence |
| :--- | :--- | :--- |
| **1** | **Papers and lectures mostly agree on what to skip.** PDEs, Optimization, LU Decomposition, Relations and Eigenvalue problems are near-absent from the recent papers *and* absent from the raw notes. | Genuinely low-risk. The agreement of two streams is much stronger evidence than either alone. |
| **2** | **Least-Square Regression is the biggest structural trap in the course.** It appears in **6 of 8 papers** (41 marks), and Fahad's notes park it under *"Supplementary Self-Study"* while adding *"other advanced curve-fitting topics are omitted from exam evaluation."* | **Highest-priority self-study item.** A topic asked in three-quarters of all papers was pushed out of lectures. |
| **3** | **"Self-study" does not mean "not examined" — proven twice.** Raidah's notes flag Gauss Forward/Backward/Stirling as self-study; **2021 Q.4b asked Gauss' forward formula outright.** Fahad's notes carry an instructor scope note saying those formulas were off the CT but **"can appear in the Semester Final."** | Treat every "self-study" flag as an exam topic, not an exemption. |
| **4** | **The instructor's stated Section-B weightage is recorded in *both* note sets, and is 3-right-1-wrong.** Logic "minimum 2 sets" ✓, Number Theory "1–1.5 sets" ✓, Sets & Functions "0.5–1 set" ✗ (observed: **zero, in all three papers**), Counting over-predicted by both. | The over-prediction is specific and actionable: the "Sets" half of the "Sets and Logic" bundle resolves to **Logic**, never to Sets. |
| **5** | **Counting has a documented hole in one note set.** Fahad's notes list Pigeonhole and Inclusion-Exclusion as missing; Raidah's notes rate Counting 🟢 Complete, and Raidah's slide roadmap explicitly lists *"Slide 6: Counting & Combinatorics (Pigeonhole Principle)."* **Pigeonhole appeared in all 3 OBE papers.** | Use Raidah's notes for Counting. If one set is all you carry, carry this one. |
| **6** | **Cubic Splines: taught in depth, off-syllabus, never examined.** Both notes cover Runge's phenomenon and natural cubic splines. **Splines appear in neither the syllabus nor any of the 8 papers.** | Recognition level only — and note this is a syllabus-irrelevance argument, not just a "not examined" one. |
| **7** | **CRT is over-sold by both note sets but still worth 20 minutes.** Fahad: *"a guaranteed semester final exam problem!"* Raidah: "must study." The papers show **1 appearance in 3 years** (2022 Q.8a, 4 marks of 120). | Prepare it — it is a short algorithm — but the item that appears every year is the plain `a ≡ r (mod n)` combination. |
| **8** | **Recycling is near-total for 2023 and partial for 2024.** 2023's Section A is **≈94 %** traceable to earlier papers; 2024's Section B is **35 %**; 2024's Section A **42.5 %**. | 2023 is effectively free marks if you have solved 2021. 2024 is *not* — see §7. |

### The one-line strategy

> **Master Propositional Logic, Interpolation, Roots of Equations, Error Analysis, Gauss-Seidel-on-a-circuit, Modular Arithmetic and Pigeonhole — then patch the self-study gaps (Regression above all, then Taylor series and Gauss Forward/Backward) — then solve 2021, 2022, 2023 and 2024 end to end.**

---

## 2. The Curriculum Discontinuity — Why the Two Streams Look Different

| Era | Years | Title | Marks answerable | Content |
| :--- | :--- | :--- | :---: | :--- |
| **Pre-OBE** | 2017 – 2021 | *Numerical Methods* | 72 | 100% Numerical Methods (Sections A **and** B) |
| **OBE** | 2022 – 2024 | *Numerical Methods & Discrete Mathematics* | 60 | Section A = Numerical, Section B = Discrete |

**Discrete Mathematics did not exist in this course before 2022.** The 2017–2021 papers contain zero discrete
mathematics. 2021 is the hinge: still 100 % numerical, still 72 marks, but the first paper to carry CLO tags
— OBE *machinery* arrived in 2021, OBE *content* in 2022.

**What this does to the evidence base:**

| Stream | Numerical Methods evidence | Discrete Mathematics evidence |
| :--- | :--- | :--- |
| Papers | **8 papers** — deep, stable, highly repetitive | **3 papers** (2022–2024) + CT-04 — thin |
| Class notes | 2 sets, but overlapping in instructor | 2 sets, **same instructor** — partially dependent |

**The interpretive asymmetry used throughout:** for the **numerical half** the papers are the stronger
signal — eight years of consistent behaviour outvotes a verbal tip. For the **discrete half** the papers give
only three data points, so the class notes carry proportionally more weight *except* where all three papers
agree (and where they agree they agree emphatically — Pigeonhole and modular arithmetic, 3/3 each).

**One consequence of the 2022 split that the mark tallies make explicit:** where a topic sits *inside* a
section changed meaning. In 2017–2021, interpolation and curve fitting were Section B material (2017 Q.5,
2018 Q.3, 2019 Q.5). From 2022 they are Section A. So the same topic counts as "Section B practice" before
2022 and "Section A practice" after — which is why §3.2 scores regression by *appearance in a paper at
all* rather than by section.

---

## 3. The Four-Quadrant Cross-Validation Framework

Every topic is placed by crossing **"has it been examined?"** against **"was it delivered?"**

```
                         DELIVERED IN CLASS                 NOT DELIVERED / SELF-STUDY
                    ┌──────────────────────────┬──────────────────────────────────┐
                    │   ① CORE                 │   ② DANGER ZONE                  │
    ASKED IN        │   Maximum confidence.    │   Asked but not delivered.       │
    PAPERS          │   Study to full depth.   │   MUST self-study from textbook. │
                    │                          │   This is where marks are lost.  │
                    ├──────────────────────────┼──────────────────────────────────┤
                    │   ③ OVER-TAUGHT          │   ④ RESIDUAL RISK                │
    NOT ASKED       │   Delivered in depth but │   In syllabus only. Absent from  │
    IN PAPERS       │   never examined.        │   both papers and lectures.      │
                    │   Recognition level.     │   Lowest priority.               │
                    └──────────────────────────┴──────────────────────────────────┘
```

### 3.1 Quadrant ① CORE — Asked and Delivered

| Topic | Paper evidence | Class-note evidence |
| :--- | :--- | :--- |
| **Error Analysis** (accuracy/precision, error representations, Taylor) | **8/8 papers, and Q.1 of Section A in 8 of 8** | Both: covered. *Gap: Raidah's notes list Taylor/truncation as missing* |
| **Roots: Bisection, False Position, N-R, Secant** | **8/8 papers**, at **Q.1 or Q.2** (Q.1 in 2021–23; Q.2 in 2017–20, 2024) | Fahad: "thoroughly covered with strict exam rules"; Raidah: 🟢 |
| **Interpolation: Lagrange, Newton Fwd/Bwd, Divided Difference** | **8/8 papers**, 103 marks — the single largest cluster | Both: 🟢 highly detailed |
| **Numerical Integration**: Trapezoidal, Simpson 1/3 & 3/8, Romberg | 6/8 papers, 87 marks | Both: 🟢 high coverage |
| **ODEs**: Euler, Heun, RK2, RK4 | 7/8 papers + CT-02B | Both: 🟢 covered |
| **Linear systems**: Gauss-Seidel, Jacobi, Gauss Elimination | 7/8 papers + CT-02B, 73 marks | Both: 🟢 (LU excepted) |
| **Propositional Logic** (full unit) | **3/3 OBE papers, 64 of 120 Section-B marks (53 %)**, + all of CT-04 | Both: "minimum 2 sets" / "at least 2 complete question sets" |
| **Number Theory**: modular arithmetic, congruence, GCD, primes | **3/3 OBE papers**, 32 marks | Both: 🟢 "excellent" / "complete" |
| **Rules of Inference**: modus ponens/tollens, syllogisms | 2023 Q.6b (define all four), 2023 Q.6c (apply) | Raidah's notes: "frequent targets for short notes and derivation problems" |
| **Pigeonhole** | **3/3 OBE papers** (2022 Q.8c ≡ 2024 Q.8c, 2023 Q.8a) | Raidah: 🟢. **Fahad: ❌ missing** |

**Together these ten blocks are 469 of the 601 numerical marks set (78 %), plus 113 of the 120 discrete
marks (94 %).** Counting is deliberately *not* listed as a ① block — see §3.2.

### 3.2 Quadrant ② DANGER ZONE — Asked but NOT delivered

This quadrant is the most valuable output of combining the sources, because neither stream alone reveals it.

| Topic | Paper evidence | Class-note status (raw notes) | Severity |
| :--- | :--- | :--- | :---: |
| **Least-Square Regression** | **6 of 8 papers**, 41 marks: 2017 Q.5b/6a/6b, 2018 Q.4c, 2019 Q.4a/4b/4c, 2020 Q.3c, 2022 Q.2b, 2024 Q.3c. *(2021 Q.4a and 2023 Q.4a only ask for a curve-fitting **example**/discussion — no fitting.)* | Fahad (raw, end of Part 1): *"**Supplementary Self-Study**: If desired, students may review the Least Squares Regression technique…; other advanced curve-fitting topics are omitted from exam evaluation."* Raidah: **❌ Missing** | 🔴🔴🔴 **CRITICAL** |
| **Gauss Forward / Backward / Stirling** | **2021 Q.4b asked Gauss' forward formula directly** (5 marks) | **Raidah** (raw): `[!note] Self Study — Central difference formulas: Gauss Forward, Gauss Backward, and Stirling's.` **Fahad** (raw) — *not* a self-study flag, an instructor scope note: *"will **not** appear in the Class Test (CT-2), but they **can appear in the Semester Final Examination."* | 🔴🔴 **HIGH** — Raidah-only gap; Fahad's note is a *warning to prepare* |
| **Taylor Series & Truncation Error** | 5/8 papers (2017 Q.1c, 2018 Q.1c, 2021 Q.1c, 2022 Q.1b, 2024 Q.1b) + CT-01 Q.1 | Fahad: 🟢 covered. **Raidah: ❌ "Missing: Truncation errors, Taylor series"** | 🔴🔴 **HIGH** for Raidah users |
| **Eigenvalues & Eigenvectors** | 2017 Q.7b and 2023 Q.3a — **identical matrix**, 11 marks total | Fahad: absent (0 hits). Raidah: ❌ "Missing: Eigenvalue problems" | 🔴 **MEDIUM-HIGH** — trivially cheap: one matrix, twice asked |
| **Boundary Value Problems** | 2021 Q.5a (define, 2) + Q.5b (solve, 5); 2024 Q.4a (theory, 3) — 10 marks | Both: ❌ absent | 🔴 **MEDIUM** |
| **Mathematical Modeling** | 2024 Q.1a (3), CT-01 Q.1a, plus 2017 Q.1a/8c, 2018 Q.1a, 2019 Q.1a, 2021 Q.1a, 2023 Q.1a | Fahad: ❌ "entirely absent". Raidah: ❌ missing | 🟠 **MEDIUM** — pure theory, cheap |
| **Extended Euclidean Algorithm** | 2022 Q.7c (2 marks) | Fahad: "self-study". Raidah (raw): *"Extended Euclidean Algorithm → Self-study topic, best practiced and prepared in tabular format."* | 🟠 **MEDIUM** |
| **Numerical Differentiation, second-derivative formula** | 2017 Q.6c (derive), 2018 Q.5a (Newton forward for d²y/dx²) | Both notes cover **first-order** forward difference only | 🟡 **LOW-MEDIUM** — narrow gap, not a whole topic |

> **This is where the exam is won or lost.** A student studying only from one note set walks into an exam
> that has asked about Least-Square Regression in six of eight years without having been taught it.

### 3.3 Quadrant ③ OVER-TAUGHT — Delivered in Depth but Never Asked

| Topic | Class-note evidence (raw) | Paper evidence | Extra point |
| :--- | :--- | :---: | :--- |
| **Cubic Splines** | Both: Runge's phenomenon, natural-cubic-spline formulation, worked problem. **Raidah only:** "Governing Tridiagonal Equation" + "memorize the tridiagonal equations". **Fahad's notes contain no tridiagonal section.** | **0 of 8** | **Not in the syllabus either** — so irrelevant *and* unexamined |
| **Sets** (operations, power set, Venn, Cartesian product) | Fahad: covered, incl. power sets and Venn. Raidah: 🟢 partial-to-good | **0 of 3 OBE papers** | Predicted 0.5–1 set by **both** note sets |
| **Predicates & Quantifiers** (∀, ∃, nested) | Both: heavy. Raidah (raw): "always use Implication (→)" for ∀, "always use Conjunction (∧)" for ∃; nested-quantifier order "is critical" | **0 of 3 OBE papers** | Fahad: questions "taken directly from the department lecture slides" — see visibility gap |
| **Functions**: injective / surjective / bijective | Fahad: covered extensively (three full subsections). Raidah: covered | **0 of 3** | **Not a syllabus unit at all** |
| **Proof by Contradiction** | Fahad: √2, √3 irrationality. Raidah: covered | **0 of 3** standalone | Only embedded NT proofs: 2022 Q.7d, 2023 Q.7c |
| **Proof by Contraposition / Bidirectional** | Both: covered | **0 of 3** standalone | — |

**How to read this quadrant honestly.** Three OBE papers is a small sample, and the lecture emphasis is real
evidence that these *could* appear. The quantifier case is instructive: both note sets flag it as
high-emphasis and slide-sourced, and it still produced nothing across three papers. The defensible position
is **recognition level** — know the definitions, the two quantifier translation rules, the power-set formula,
and what an injection is. Do not build these into deep practice at the expense of Quadrant ① or ②.

> **Visibility caveat:** if the slides contain worked quantifier or set problems, the risk here is higher than
> the paper record suggests. Both note sets record that reading the slides is mandatory — honour that.

### 3.4 Quadrant ④ RESIDUAL RISK — In the Syllabus, Absent from Both Papers and Lectures

| Topic | Syllabus | Papers | Class notes |
| :--- | :---: | :---: | :--- |
| **Relations** (properties, binary, partial ordering, equivalence) | ✅ Full unit | **0/3** | **❌ Fahad's raw notes: 0 mentions.** Raidah: "Entirely Missing" |
| **Mathematical Induction** | ✅ Listed | **0/3** | **❌ Fahad's raw notes: 0 mentions.** Raidah: ❌ omitted |
| **PDEs** (Laplace, Poisson, Liebmann) | ✅ Listed | 4/8 papers, **29 marks across 2018–2021**, then **0/8 since** | **❌ Fahad's raw notes: 0 mentions of Poisson/Liebmann/Laplace**; his analysis records an explicit professor exclusion |
| **One-dimensional Unconstrained Optimization** | ✅ Listed | **2/8** — 2021 Q.6b/6d (5 marks); 2018 Q.5b asks for a tabulated maximum (6) | **❌ Fahad's raw notes: 0 mentions.** Raidah: "Entirely Missing" |
| **LU Decomposition & Matrix Inversion** | ✅ Listed | 1/8, theory only (2017 Q.4b, 4 marks) | ❌ Both: missing |
| **Inclusion-Exclusion** | ✅ Listed | **0/3** | Raidah: 🟢 covered. Fahad: ❌ missing |
| **Algebraic Properties / Computer Representation of Sets** | ✅ Listed | **0/3** | ❌ Both: missing |
| **Interpolation with two independent variables** | ✅ Listed | **0/8** | ❌ Both: missing |
| **Programming and Software** | ✅ Listed | **0/8** | ❌ Both: missing |

**Two streams agreeing on absence is the strongest deprioritisation signal available** — a topic missing from
both the examiner's behaviour over eight years *and* the lecturer's delivery is very unlikely to appear.

**Two exceptions worth naming:**
- **Mathematical Induction** is the most defensible ④ investment: a named syllabus topic, a standard
  discrete-mathematics staple, and the discrete section has only three papers of history — the smallest
  sample in the analysis. One hour on the three-step template is cheap insurance. A softer supporting signal:
  **2022 Q.2c** asks for `Sₙ = 1³ + 2³ + … + n³` via Newton's forward formula, the numerical analogue of
  the classic induction exercise — so the setter does use the sum-of-cubes identity. **[judgement]** one
  appearance is thin evidence, but it costs nothing to note.
- **PDEs** carry the strongest *disconfirming* signal in the course: 29 marks over 2018–2021, then **zero**
  appearances in 2022, 2023 and 2024 (the 2024 paper asked only a 2-mark boundary-condition theory part),
  plus Fahad's notes contain no PDE material whatsoever. **Learn the 5-point stencil for a theory answer; do
  not drill grid solutions.**

---

## 4. Conflict Resolution Table

| # | Topic | Papers say | Class notes say | **Verdict** | Reasoning |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | **Least-Square Regression** | Asked in **6/8** | Self-study (Fahad) / missing (Raidah) | **🔴 STUDY TO FULL DEPTH** | Six of eight papers, 41 marks, and the syllabus names it as a separate bullet from Interpolation. Not negotiable. |
| 2 | **Gauss Fwd/Bwd/Stirling** | Asked 2021 Q.4b | Raidah: self-study. Fahad: *"can appear in the Semester Final"* | **🔴 STUDY** | Already proven examinable, and both notes point you at it — Fahad as a warning, Raidah as a gap to patch. |
| 3 | **Sets** | **0/3** | Both: 🟢, "0.5–1 set" / "2 question sets" | **🟡 RECOGNITION LEVEL** | Three papers of total silence from a *doubly-stated* prediction. The "Sets and Logic" bundle resolves to Logic in practice. |
| 4 | **Quantifiers** | **0/3** | Both: heavy, slide-sourced | **🟡 RULES OF THUMB ONLY** | Memorize ∀→implication and ∃→conjunction. Slides not visible, so residual risk acknowledged. |
| 5 | **Counting** | 17 of 120 marks (14 %); pigeonhole 3/3 but combinations and binomial theorem **1/3** each | Fahad 1 set, Raidah 1–1.5 sets; **Fahad ❌ missing the topics** | **🟠 STUDY, VIA RAIDAH'S NOTES** | Both over-predicted the volume, but pigeonhole hit 3/3 and Fahad's notes have the hole. |
| 6 | **CRT** | 1/3 (2022 Q.8a) | Both: "guaranteed" / "must study" | **🟠 PREPARE — it is short** | Tips over-state frequency, but CRT is compact and the professor's stated favourite. |
| 7 | **Cubic Splines** | **0/8** | Both: detailed | **🟡 RECOGNITION LEVEL** | Eight years of silence *and* off-syllabus. Know *why* splines exist (Runge's phenomenon) — good comparison material — but skip the tridiagonal solve. |
| 8 | **PDEs** | 4 papers 2018–2021, then 0 | Fahad: explicitly excluded | **🟡 THEORY ONLY** | Papers and lectures agree on the drop. 5-point stencil for a 2-mark answer (as in 2024 Q.4c). |
| 9 | **Optimization** | 2/8 (2021 explicit; 2018 Q.5b unlabelled) | Both: missing | **🟡 DEFINITIONS ONLY** | Constrained vs. unconstrained (2 marks) + Newton's method for a maximum. ~15 minutes total. |
| 10 | **Eigenvalues** | 2/8, **same matrix twice**, 11 marks | Both: missing | **🟠 LEARN THE ONE MATRIX** | The cheapest ② item in the course. |
| 11 | **Taylor Series** | 5/8 + CT-01 | Fahad 🟢 / **Raidah ❌** | **🔴 STUDY** | Papers plus one note set agree it is core. |
| 12 | **Mathematical Induction** | **0/3** | Both: missing | **🟡 ONE HOUR OF INSURANCE** | Syllabus-listed, zero coverage anywhere, smallest sample in the analysis. |
| 13 | **Relations** | **0/3** | Both: entirely missing | **⚫ LOWEST PRIORITY** | Both streams agree on absence. |
| 14 | **Algorithms / Complexity** | 2024 Q.7a (6 marks) | Both: absent (correctly — off-syllabus) | **🟠 20 MINUTES OF INSURANCE** | One sort name + average complexity, binary search pseudocode + O(log n), one-line greedy definition. |
| 15 | **Number Theory vs. Counting split** | 2022 Q.8 = CRT **+** product rule **+** pigeonhole in one question | Fahad's weightage table: Counting *"May be combined with Number Theory!"* | **✅ NOTES PREDICTED THE HYBRID** | The only place a class tip matched a paper's *structure* rather than just its topics. |

---

## 5. The Instructor's Stated Section-B Weightage — Reconciled Against Three Papers

Both note sets independently record a final-exam weightage breakdown. **This is the single most
under-used piece of evidence in the course**, because it is a quantified prediction, recorded twice.

| Topic | Fahad's table (raw notes) | Raidah's table (raw notes) | **Observed 2022–2024** (in 10-mark "sets") | Verdict |
| :--- | :--- | :--- | :--- | :--- |
| **Propositional Logic** | Minimum **2 sets** | Minimum **2 sets** | 2.0, 2.0, **2.4** → mean **2.13** | ✅ **Accurate — and under-delivered on** (2024 added Q.7b) |
| **Number Theory** | **1–1.5 sets** | **1–1.5 sets** | 1.4, 1.0, 0.8 → mean **1.07** | ✅ **Accurate** |
| **Counting / Combinatorics** | **1 set** | **1–1.5 sets** | 0.6, 0.9, **0.2** → mean **0.57** | ⚠️ **Both over-predicted** — Fahad closer |
| **Sets & Functions** | **0.5–1 set** | **0.5–1 set** | **0, 0, 0** | ❌ **Did not materialize** |

**Two observations that sharpen this:**

1. **The stated weightages sum to ~5.25 sets, but Section B only contains 4.** The four rows are therefore
   *relative priorities*, not a partition of the paper. Read that way, Logic's "minimum 2" is a floor, and
   the sets freed by Sets scoring zero went to Logic (2024) and to the off-syllabus algorithms question.
2. **The over-prediction is precisely located.** Sets and Quantifiers — named in the syllabus, emphasised in
   lectures, predicted by both note sets — have never appeared. The instructor's "Sets and Logic" bundle
   resolved entirely into **Logic**. Raidah's notes also record Fahad-compatible emphasis on quantifiers
   that has likewise produced nothing in three papers.

### 5.1 The reconciled structure of Section B

```
Q.5  →  Propositional Logic   (10 marks)  ─┐
Q.6  →  Propositional Logic   (10 marks)  ─┴─ the stable core, 2 sets every year
Q.7  →  Number Theory         (10 marks)  ─── 1 set, 2022 & 2023
Q.8  →  Counting              (10 marks)  ─── 2022 only; 2024 Q.8a is CRT, Q.8b–d Counting
```

**Two documented deviations, which is why this is a template and not a guarantee:**

- **2022 Q.8a** is Chinese Remainder Theorem + Fermat's little theorem — *Number Theory* inside the
  "Counting" question. Fahad's note anticipated exactly this: Counting *"May be combined with Number
  Theory!"*
- **2024** breaks the template twice: **Q.7a is the off-syllabus algorithms question** (6 marks, no Number
  Theory at all that year) and the **biconditional item moved to Q.7b**. 2024's Number Theory fell to 8 marks
  — its lowest in three years.

Since you answer **any 3 of 4**, the operative consequence survives every deviation:

> **Mastering Propositional Logic (Q.5 + Q.6) plus EITHER Number Theory OR Counting covers the full 30
> Section B marks.** This is the most reliable strategic fact in the course — *and* it is exactly what both
> note sets' weightage tables imply.

---

## 6. Numerical Methods — Where the Marks Actually Live

**Method.** Every sub-question classified once (`question_tally_audit.md`). Denominator = all marks set:
2017–2021 = 96+96+96+96+**97** = **481**; 2022–2024 Section A = 40×3 = **120**; total **601**.
Both pre-OBE sections count (they are 100 % numerical) against OBE Section A only.

| Cluster | Marks | Share | Quadrant | Both note sets' coverage |
| :--- | ---: | ---: | :--- | :--- |
| Errors + Roots of Equations | 163 | **27.1 %** | ① Core | 🟢 (Taylor gap in Raidah's) |
| Interpolation | 103 | **17.1 %** | ① Core | 🟢 |
| Integration + Differentiation | 87 | **14.5 %** | ① Core | 🟢 Strong |
| Linear systems (incl. circuits) | 73 | **12.1 %** | ① Core | 🟢 (LU excepted) |
| ODE + BVP | 79 | **13.1 %** | ① Core + ② (BVP) | 🟢 ODE / ❌ BVP |
| Regression | 43 | **7.2 %** | **② Danger** | **❌ Both** |
| PDE + Eigenvalue + Optimization | 53 | **8.8 %** | ③ / ④ | ❌ Absent |

*Shares sum to 99.9 % (rounding). This table splits **Regression** out of the interpolation cluster because it is
the one Quadrant-② item sitting inside a Tier-1 cluster — see below. For the source report's six-cluster
roll-up, which keeps them merged, see `question_tally_audit.md` §B.*

**Concentration of marks.** On this table's split, the top four rows — errors+roots, interpolation,
integration+differentiation, linear systems — are **426 of 601 marks = 71 %**. Merging Regression back with
Interpolation, as the source report does, gives **469 of 601 = 78 %** for the same four conceptual clusters.

**Reading the tail honestly — this replaces a common error.** PDE + Eigenvalue + Optimization is **8.8 %**,
not the "~2 %" a glance at the recent paper list suggests. PDE alone is **29 marks (4.8 %)** across 2018–2021.
So the lecture triage was *mostly* rational but not perfectly aligned:

| Dropped topic | Marks | Share | Rational? |
| :--- | ---: | ---: | :--- |
| Eigenvalue | 11 | 1.8 % | ✅ Rational — twice, same matrix, cheap either way |
| Optimization | 11 | 1.8 % | ✅ Rational — 2 of the 11 marks are definition |
| LU Decomposition | 4 | 0.7 % | ✅ Rational — one theory appearance |
| **PDE** | **31** | **5.2 %** | ⚠️ **Least rational** — it was a whole question every year until 2021, and the professor's *explicit* exclusion may reflect a genuine change of scope rather than a marks judgement |
| **Regression** | **43** | **7.2 %** | ❌ **Irrational** — inside the two largest clusters and pushed to self-study |

**The mismatch to act on is Regression, not PDE.** Both were excluded from lectures; only one of them
deserved it on marks grounds.

---

## 7. The Repeat-Question Multiplier

The paper analysis identified **22 repeat pairs: 15 verbatim, 4 near-verbatim (same data, one value
changed), 3 same-concept.** Combined with the class-note tips this yields a sharper list than either source
gives alone.

### 7.1 Recycling rates — marks of §7.1-register items ÷ marks set

| Paper / Section | Marks set | Recycled marks | Share | Primary source |
| :--- | ---: | ---: | ---: | :--- |
| **2023 Section A** | 40 | 37.5 | **≈ 94 %** | 2021 (items 8–12) + 2017 (1, 2) + 2018 (7) + 2020 (13) |
| **2024 Section A** | 40 | 17 | **42.5 %** | 2017 (4, 6) + 2020 (14, 21) |
| **2024 Section B** | 40 | 14 | **35.0 %** | 2022 (items 15–18) |
| **2022 Section A** | 40 | 4 | **10.0 %** | 2017 (item 3) |
| **2020** | 96 | 9 | **9.4 %** | 2017 (items 5, 6) |

Topical echoes (same method, reworded or re-parameterised) are **excluded** from these figures; including
them raises each by roughly 10–25 points. The measure is deliberately conservative.

**Direct evidence of copy-paste setting:** 2023 Q.1c reprints the typo *"discuss this problems of it"*
verbatim from 2021 Q.1b. Smaller ones travel too — 2022 Q.8b's "Los Angles", 2018 Q.4c's "linier", 2024 Q.4b's
"circulation", 2024 Q.7b's "true of false".

### 7.2 Why this amplifies the class-note tips

The class notes tell you *which methods* the professor emphasised. The repeat register tells you *which
specific problems* the setter reaches for.

| Recurring item | Appearances | Confirmed by class tips? |
| :--- | :--- | :--- |
| Define interpolation / extrapolation / curve fitting | **6 of 8 papers** | 🟢 Yes — top-priority in both |
| Gauss-Seidel on a DC circuit | 5 papers + CT-02B | 🟢 Yes |
| Lagrange on a small table | 5 papers + CT-02A | 🟢 Yes |
| Decennial census (46, 66, 81, 93, 101) | 2017, 2020, 2024 | 🟢 Yes — tests the Forward/Backward choice rule |
| `a ≡ r (mod n)` combination → find `c` | **3 of 3 OBE papers** | 🟢 Yes |
| Generalized pigeonhole, real-world example | **3 of 3 OBE papers** | 🟢 Raidah only (**Fahad has the gap**) |
| "What is pivoting / partial vs. complete" | 4 papers | 🟢 Yes |
| Derive Newton's forward interpolation formula | 2020, 2021, 2023 | 🟢 Yes |
| Biconditional four-item set | 2022, 2024 (verbatim) | 🟢 Yes |
| `3^644 mod 645` | 2022, 2024 (verbatim) | 🟢 Yes |
| Rocket integral → Simpson 1/3 + error chain | 2018, 2023 | 🟢 Yes |
| **Eigenvalues of `[ [5,0,1],[0,−2,0],[1,0,5] ]`** | 2017, 2023 (same matrix) | ❌ **No — ② gap** |
| **Least-squares straight line, x = 1…7** | 2017, 2024 (verbatim) | ❌ **No — ② gap** |
| **`y = a·e^(bx)` exponential fit** | 2017, 2020 (verbatim) | ❌ **No — ② gap** |

**The bottom three rows are the point of this section.** Three *specific, already-printed* problems — each
reproduced verbatim years later, each in a topic the notes push to self-study. Solving those three once is
probably the highest-return hour available in this course.

### 7.3 Operational conclusion

> **2021 is the master paper.** 2023 is ≈94 % traceable to it, 2017 and 2020. **2022 is the master paper for
> Section B** — but note it supplies 2024 with only 35 %, so treat 2024 Section B as *recurring*, not
> *recycled*. Order: **solve 2021 in full → 2022 Section B → 2023 → 2024 → sweep 2017** (four of its items
> resurfaced six to seven years later).

---

## 8. Unified Study Plan

### Phase 1 — Core, maximum confidence (Quadrant ①)

**Numerical Methods**
- [ ] Error taxonomy: accuracy vs. precision, round-off vs. truncation, true/absolute/relative/percentage
      error. Practice on an instrument reading (2019 Q.1c, 2020 Q.1b). **This is Q.1 of Section A in 8 of 8
      papers — start here.**
- [ ] Roots: derive Newton-Raphson; state its failure modes (inflection points, `f′(x) → 0`, divergence)
      **and the fixes**; algorithm steps for Bisection and False Position; the full four-way comparison table.
- [ ] **Apply the notes' rules:** NR terminates when two consecutive iterations match exactly (NRP Sir);
      bisection stops when 3 digits match (Fahad); secant guesses must be independent non-roots (NRP Sir).
- [ ] Interpolation: Lagrange; Newton Forward, Backward, Divided Difference; build the difference table
      cleanly. **Fahad's rule: forward when the target is near the top/beginning of the table, backward when
      near the bottom/end** (Fahad's own examples: forward for `y(7)` with `x₀ = 5`; backward for `y(17)`
      with `xₙ = 20`).
- [ ] Derive Newton's forward interpolation formula (asked 3 times: 2020, 2021, 2023).
- [ ] Gauss-Seidel: the full **circuit → KVL/KCL → rearrange → iterate → absolute error** pipeline. Plus
      Jacobi, Gauss Elimination, pivoting theory, relaxation (λ), ill-conditioned systems.
- [ ] Integration: Trapezoidal (derive), Simpson 1/3 (derive; exact to degree 3), Simpson 3/8, Romberg.
      **Memorize: 1/3 → n even; 3/8 → n multiple of 3.** Drill the (i) value → (ii) true error →
      (iii) absolute relative true error chain.
- [ ] ODEs: Euler, Heun (derive it; state Euler's limitation), RK2, RK4. **Default to RK4 when no method is
      named** (Fahad). Second-order ODE reduced to a system.
- [ ] Numerical differentiation from a table: first and second derivative by forward difference; physical
      framings (`v = L·di/dt`, angular velocity).

**Discrete Mathematics**
- [ ] Propositional logic: truth tables; tautology / contradiction / contingency; valid / satisfiable /
      unsatisfiable; logical equivalence both by truth table and by algebraic reduction.
- [ ] **Translation drill** — system specifications into logic, then consistency checks. **Connector traps:
      "unless" → `p → q`, "however"/"moreover" → `∧`, "until", "only if", "neither…nor".** Both note sets
      flag "unless", "however" and "until" independently.
- [ ] Rewrite expressions using only `¬, ∨, ∧`; functional completeness of `{¬, ∧}`; CNF and DNF with
      transformation steps shown.
- [ ] Rules of inference: modus ponens, modus tollens, hypothetical syllogism, disjunctive syllogism —
      definitions, truth tables, examples, and constructing a multi-premise valid argument.
- [ ] Logic puzzles: knights/knaves/spies, exactly-one-truth-teller. Logic → digital circuit construction.
- [ ] Modular arithmetic: `a ≡ r (mod n)` combinations (linear, quadratic, cubic); fast modular
      exponentiation. **This pair — pigeonhole + `a ≡ r (mod n)` — is 3/3 across all OBE papers.**
- [ ] Pigeonhole and generalized pigeonhole — with a prepared real-world example.

### Phase 2 — Patch the Danger Zone (Quadrant ②) 🔴 **do not skip**

- [ ] **Least-Square Regression — highest priority.** Derive the normal equations for a straight line; the
      `y = a·e^(bx)` log-linearization; the `y = x/(a+bx)` reciprocal linearization; why minimum-sum and
      minimum-absolute-error criteria are ill-suited (2017 Q.6a). **Solve the two recycled datasets
      directly: `x = 1…7` (2017 Q.6b ≡ 2024 Q.3c) and the exponential set (2017 Q.5b ≡ 2020 Q.3c).**
- [ ] **Gauss Forward / Backward / Stirling interpolation** — self-study in Raidah's notes, flagged
      "can appear in the final" in Fahad's, and **already examined** (2021 Q.4b).
- [ ] **Taylor series and truncation error** — expansion to a stated decimal accuracy; number-of-terms
      problems; truncation-error estimation. *(Critical if studying from Raidah's notes.)*
- [ ] **Eigenvalues of a 3×3 matrix** — characteristic-polynomial method. **Do the recurring matrix
      `[ [5,0,1],[0,−2,0],[1,0,5] ]` once** (2017 Q.7b ≡ 2023 Q.3a).
- [ ] **Boundary Value Problems** — the general numerical approach vs. IVP; the shooting idea.
- [ ] **Mathematical modeling** — write a short model with stated assumptions (2024 Q.1a, CT-01 Q.1a).
- [ ] **Extended Euclidean algorithm** — in tabular form, as Raidah's notes specify.
- [ ] **Chinese Remainder Theorem** — the full construction (compute `M`, `Mᵢ`, modular inverses).

### Phase 3 — Cheap insurance

- [ ] Liebmann 5-point stencil — enough to answer *"importance of boundary conditions in solving PDEs
      numerically"* (2024 Q.4c) and name the method.
- [ ] One-dimensional unconstrained optimization: Newton's method for a maximum; constrained vs.
      unconstrained definitions.
- [ ] LU decomposition — concept only ("how can a square matrix be factorized into LU form?").
- [ ] Algorithms wildcard: one O(n log n) sort by name with average complexity; binary search pseudocode with
      O(log n); one-line definition of a greedy strategy.
- [ ] Combinations `C(n,r)`; binomial-theorem coefficient extraction. *(Note the decline: combinations
      1/3 and binomial theorem 1/3 of OBE papers. Cover them, don't over-invest.)*
- [ ] **Theory-answer bank** — one-paragraph answers for the recurring 2-markers: *what is pivoting; define
      bracketing methods; interpolation vs. extrapolation vs. curve fitting; compare Simpson's 1/3 and 3/8;
      real-life example of curve fitting; real-life application of numerical differentiation; why ECE
      engineers need numerical methods; ill-conditioned system; over- and under-relaxation; BVP vs. IVP.*
      **These recycle harder than any computation in the course.**

### Phase 4 — Residual risk, only if time remains

- [ ] **Mathematical Induction** — the three-step template. Most defensible ④ item.
- [ ] Sets: operations, power set theorem (`|P(S)| = 2^|S|`), Venn diagrams — recognition level.
- [ ] Quantifiers: **∀ → implication; ∃ → conjunction.** Nested-quantifier order is critical when mixing.
      Two lines, memorize them.
- [ ] Relations: reflexive / symmetric / transitive, equivalence, partial order — definitions only.
- [ ] Inclusion-exclusion for two and three sets. Permutations (e.g. word-arrangement multiplicity).
- [ ] Proof by contradiction (√2 irrational) and contraposition — one worked example each.
- [ ] Cubic splines — know *why* they exist (Runge's phenomenon); skip the tridiagonal solve.

---

## 9. Exam-Day Checklist

1. **Confirm the section split before writing.** Answer exactly 3 from Section A and 3 from Section B, on
   **separate answer scripts**. 30 marks are locked behind Discrete Mathematics and cannot be substituted.
2. **Scan all 8 questions for repeats first.** Expect at least one repeat per section — near-certain in
   2023-style papers, likely but not guaranteed in 2024-style ones.
3. **Harvest the theory parts before computing.** Roughly **30–38 %** of an OBE paper is definitions,
   comparisons and conceptual items. Sweep every (a) part across your six chosen questions first.
4. **Respect iteration caps.** "Three iterations only" means three. The tabulation itself carries marks.
5. **For circuit questions, write KVL/KCL explicitly before iterating.** Equation formulation is marked
   independently of the arithmetic.
6. **Check the target value in table problems.** The census dataset (46, 66, 81, 93, 101) is identical
   across three papers while the requested year changed — 1955 → **backward**, 1895 & 1925 → **forward and
   backward**, 1995 → **extrapolation**. Decide the method from the target's position, not from memory.
7. **Finish chained integration questions.** (i) value → (ii) true error → (iii) absolute relative true error
   are all marked separately.
8. **Watch the connectors in logic translation.** "Unless", "only if", "if and only if", "neither…nor".
   Both note sets and CT-04 Q.3 flag these.
9. **State the Simpson constraint when you use it.** "n must be even for 1/3" / "n must be a multiple of 3
   for 3/8" is a free mark in any comparison question.
10. **Don't assume the Section B template held last year.** In 2024, Q.7a was off-syllabus algorithms and the
    biconditional item moved to Q.7b. Read Q.7 and Q.8 before committing.
11. **Read the lecture slides.** Both note sets record this as mandatory, and Fahad's notes state that
    nested-quantifier and algorithm-proof questions come directly from them. The slides are the one evidence
    stream not visible to this analysis.

---

## 10. Final Synthesis

**The papers reveal a small, openly-recycled question bank.** Twenty-two repeat pairs — 15 verbatim, several
carrying their typographical errors across six years. 2023's Section A is ≈94 % traceable to 2021, 2017 and
2020, with exactly one new sub-question in the whole section. 2024 splits: Section A recycles ~43 % from the
pre-OBE bank, Section B ~35 % from 2022. The examined syllabus is far narrower than the written one — four
numerical clusters carry **78 % of the 601 numerical marks set**, and Propositional Logic alone carries
**53 %** of Section B, while three of six discrete units have never been asked.

**The class notes reveal a lecture triage that is right about most things and wrong about two.** Dropping
Eigenvalues (1.8 %), Optimization (1.8 %) and LU Decomposition (0.7 %) was well-judged on the marks. But
**PDE was dropped at 4.8 %** with four straight years of a full 5–6 mark question behind it — that looks like
a genuine change of scope rather than a marks decision, and Fahad's note records an explicit verbal
exclusion, so treat it as settled. The one clearly irrational exclusion is **Least-Square Regression**:
inside the two largest clusters, named in the syllabus as its own bullet, and pushed to self-study. The
stated weightages also over-predicted **Sets** and **Quantifiers** — both named in the syllabus, both
emphasised in lectures, both predicted by *both* note sets, and both absent from all three papers.

**The class tests reveal the assessment style.** CT-01 asks for no numbers at all — build a model, state
assumptions, identify error sources, diagnose why Regula Falsi stagnates. CT-04 is pure logic translation.
Every class-test topic reappears in the finals, which makes them a preview rather than a separate syllabus.

**Put together, the course reduces to a short, concrete plan:**

> Study the ten Quadrant-① blocks to full depth. Patch the Quadrant-② gaps — **Regression above all**,
> then Taylor series, Gauss Forward/Backward, and the one recurring eigenvalue matrix. Keep Sets, Quantifiers,
> Splines and Functions at recognition level despite their lecture emphasis. Deprioritize Relations,
> PDE grids, Optimization and LU Decomposition, where papers and lectures agree. Spend one hour on
> Mathematical Induction and twenty minutes on algorithm complexity as insurance. Then solve 2021, 2022,
> 2023, 2024 and 2017 in that order.

**The one structural fact to internalize:** since 2022 the paper is a hard 50/50 split with no cross-section
substitution. Thirty marks sit behind Propositional Logic, Modular Arithmetic and Counting — which happen to
be the three most repetitive and narrowly-scoped topics in the course. That is not a threat; it is the
easiest 30 marks on the paper, provided you do not ignore them. **But the Section B template held in only
two of three years** — expect to *choose* between Logic, Number Theory and Counting rather than bank a
guaranteed third.

---

*Synthesized from: `PreviousYearAnalysisReport.md`, `question_tally_audit.md`, Fahad's raw class notes +
analysis, Raidah's raw class notes + analysis, `ECE2213_Syllabus.md`*
*Note: department lecture slides referenced by both note sets were not available to this analysis. The two
note sets share an instructor for both halves of the course, so their agreement is corroboration, not
independent replication.*