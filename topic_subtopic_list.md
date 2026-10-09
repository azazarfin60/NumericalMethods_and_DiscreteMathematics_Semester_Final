---
course_code: ECE 2213
course_title: Numerical Methods & Discrete Mathematics
document_type: Topic & Subtopic Taxonomy
purpose: Canonical classification scheme for topic-wise sorting of previous year questions
tags:
  - taxonomy
  - ece2213
  - topic-list
  - question-sorting
---

# ECE 2213 — Topic & Subtopic List

**Purpose:** canonical taxonomy for sorting all previous year and class test questions (2017–2024) into topic-wise sections. Every subtopic carries a stable ID (`NM-x.y` / `DM-x.y`) to be used as the section key in the sorted question bank.

**Structure:** Section 1 = Numerical Methods (10 topics, 62 subtopics). Section 2 = Discrete Mathematics (7 topics, 43 subtopics).

**Legend**

| Symbol | Meaning |
| :---: | :--- |
| 🔴 | **Tier 1 — High priority.** Heavily weighted *and/or* structurally central (typically a whole question set). **Not a frequency guarantee — see the Frequency Cross-Check below.** |
| 🟠 | **Tier 2 — Secondary.** Examined repeatedly and safe to prepare in depth, but smaller in weight. |
| 🟡 | **Tier 3 — Light.** One or two appearances. Prepare for recognition. |
| ⚫ | **Tier 4 — Never examined.** No paper in the analysed set. |
| ⚠️ | **Danger zone** — examined but *not taught* in class (self-study gap). |
| 📘 | Off-syllabus — appeared in a paper but absent from the official syllabus. |

> **Tier ≠ frequency.** Tier encodes **study priority**, which blends paper frequency, mark weight and
> structural centrality. Frequency and priority genuinely diverge in this course: several Tier-1 subtopics
> are new-appearing, and several Tier-2 subtopics appear more often. The **Years Appeared** column of each
> subtopic — not its tier — is the frequency of record. Quantified in *Tier Summary → Frequency Cross-Check*.

> **Era reminder:** Discrete Mathematics (`DM-*`) did not exist in this course before 2022. The 2017–2021 papers are 100% Numerical Methods in *both* sections. All `DM-*` evidence therefore comes only from 2022, 2023, 2024 and CT-04.

---

# SECTION 1 — NUMERICAL METHODS

## NM-1 · Modeling, Computers and Error Analysis

| ID | Subtopic | Tier | Years Appeared |
| :--- | :--- | :---: | :--- |
| **NM-1.1** | Foundations of Numerical Methods — definition, numerical vs. analytical methods, why ECE engineers need them, real-life application fields | 🔴 | 2017, 2018, 2019, 2020, 2021, 2023, 2024 |
| **NM-1.2** | Mathematical Modeling & Engineering Problem Solving — building a model, stating assumptions | 🟡 ⚠️ | 2024, CT-01 |
| **NM-1.3** | Accuracy, Precision & Significant Digits — definitions, summation of numbers with correct digits | 🟠 | 2017 |
| **NM-1.4** | Error Types & Sources — round-off error, truncation error, algorithmic/inherent error, how errors enter the process | 🔴 | 2017, 2018, 2019, 2020, 2024, CT-01 |
| **NM-1.5** | Error Representations & Propagation — true / absolute / relative / percentage error, choosing the better representation, relative error of a composite function | 🔴 | 2017, 2019, 2020, 2023 |
| **NM-1.6** | Taylor Series & Truncation Error — series expansion to stated decimal accuracy, number of terms required, truncation-error estimation | 🔴 ⚠️ | 2017, 2018, 2021, 2022, 2024, CT-01 |
| **NM-1.7** | Programming and Software | ⚫ | — |

## NM-2 · Roots of Equations

| ID | Subtopic | Tier | Years Appeared |
| :--- | :--- | :---: | :--- |
| **NM-2.1** | Fundamentals & Classification — definition of a root, bracketing vs. open methods, iterative-method concept and generalized steps | 🔴 | 2019, 2020, 2021, 2022 |
| **NM-2.2** | Bisection Method — explanation, algorithm with accuracy test, numeric iterations | 🔴 | 2017, 2018, 2020, 2024, CT-01 |
| **NM-2.3** | False Position / Regula Falsi — derivation of the next approximation, algorithm steps, one-sided stagnation and its fix, numeric iterations | 🔴 | 2017, 2018, 2020, 2021, CT-01 |
| **NM-2.4** | Newton-Raphson Method — derivation, steps, limitations (inflection points, vanishing derivative) and remedies, merits/demerits, numeric iterations | 🔴 | 2017, 2018, 2019, 2020, 2021, 2023 |
| **NM-2.5** | Secant Method — numeric iterations, initial-guess hazard | 🟠 | 2017, 2020 |
| **NM-2.6** | Method Comparison & Convergence — cross-comparison of bisection / false position / Newton-Raphson / secant | 🔴 | 2020, 2022, CT-01 |
| **NM-2.7** | Roots of Polynomials — smallest/positive root of a cubic, physically-framed power/current equations | 🟠 | 2017, 2019, 2020, 2021, 2024 |

## NM-3 · Linear Algebraic Equations

| ID | Subtopic | Tier | Years Appeared |
| :--- | :--- | :---: | :--- |
| **NM-3.1** | Direct Methods & Gauss Elimination — overview of direct methods, elimination procedure, back-substitution, answer verification | 🟠 | 2019, 2020, 2022 |
| **NM-3.2** | Pivoting — pivots, partial vs. complete pivoting, why pivoting matters | 🔴 | 2017, 2019, 2021, 2022 |
| **NM-3.3** | LU Decomposition & Matrix Inversion | 🟡 ⚠️ | 2017 |
| **NM-3.4** | Jacobi Iteration | 🟠 | 2017, 2022 |
| **NM-3.5** | Gauss-Seidel Iteration — rearrangement for convergence, iterative march, absolute error between iterations | 🔴 | 2017, 2018, 2019, 2020, 2021, 2024, CT-02B |
| **NM-3.6** | Relaxation — over-relaxation, under-relaxation, relaxation factor λ | 🟡 | 2017, 2018 |
| **NM-3.7** | Ill-Conditioned Systems | 🟡 | 2022 |
| **NM-3.8** | Circuit Applications — DC mesh/nodal analysis reduced to a linear system, then solved iteratively | 🔴 | 2018, 2019, 2020, 2021, 2024 |

## NM-4 · Curve Fitting

| ID | Subtopic | Tier | Years Appeared |
| :--- | :--- | :---: | :--- |
| **NM-4.1** | Concepts — interpolation vs. extrapolation vs. curve fitting, when to use which, general techniques, real-life examples | 🔴 | 2017, 2019, 2020, 2021, 2022, 2023, 2024 |
| **NM-4.2** | Least-Squares Linear Regression — normal equations, straight-line fit, prediction from the fitted line | 🔴 ⚠️ | 2017, 2018, 2019, 2024 |
| **NM-4.3** | Non-Linear Regression — exponential fit `y = a·e^(bx)`, reciprocal fit `y = x/(a+bx)`, linearization | 🔴 ⚠️ | 2017, 2020, 2022 |
| **NM-4.4** | Regression Criteria & Theory — why minimum-sum-of-error / minimum-absolute-error / minimum-error criteria are ill-suited, least-squares condition | 🟠 ⚠️ | 2017, 2019 |
| **NM-4.5** | Linear Interpolation — first-order polynomial estimate between two points | 🟠 | 2018, 2019 |
| **NM-4.6** | Lagrange's Interpolation — formula, use cases, suitable data types, advantages & disadvantages, numeric estimate | 🔴 | 2018, 2019, 2021, 2022, 2023, 2024, CT-02A |
| **NM-4.7** | Newton's Forward Difference — derivation of the formula, numeric estimate, summation identities | 🔴 | 2018, 2020, 2021, 2022, 2023, CT-02A |
| **NM-4.8** | Newton's Backward Difference — numeric estimate near the end of a table | 🟠 | 2017, 2020, 2024, CT-02A |
| **NM-4.9** | Newton's Divided Difference / General Interpolation — unequal intervals, polynomial construction, evaluation | 🟠 | 2019, 2020, 2022 |
| **NM-4.10** | Gauss Forward / Backward & Stirling's Formulas | 🟡 ⚠️ | 2021 |
| **NM-4.11** | Difference Table Formation & Applications — building forward/backward/divided-difference tables, extrapolation beyond the table | 🔴 | 2017, 2020, 2021, 2022, 2024 |
| **NM-4.12** | Interpolation with Two Independent Variables | ⚫ | — |

## NM-5 · Numerical Integration

| ID | Subtopic | Tier | Years Appeared |
| :--- | :--- | :---: | :--- |
| **NM-5.1** | Trapezoidal Rule — derivation, discussion, determining the number of segments for a target error | 🟠 | 2018, 2019, 2021, 2022 |
| **NM-5.2** | Simpson's 1/3 Rule — derivation, exactness up to degree three, multi-segment application | 🔴 | 2018, 2019, 2020, 2023 |
| **NM-5.3** | Simpson's 3/8 Rule | 🟠 | 2019 |
| **NM-5.4** | Rule Comparison & Step Constraints — Simpson's 1/3 vs. 3/8, `n` even vs. `n` multiple of 3 | 🔴 | 2020, 2023 |
| **NM-5.5** | Romberg's Method — Richardson extrapolation over h = 0.5, 0.25, 0.125 | 🟠 | 2021, 2022, 2023 |
| **NM-5.6** | Error Analysis in Integration — true error, absolute relative true error, error-bounded step selection | 🟠 | 2018, 2023 |
| **NM-5.7** | Applied Integration — rocket distance, op-amp integrator output | 🟠 | 2018, 2020, 2023 |

## NM-6 · Optimization

| ID | Subtopic | Tier | Years Appeared |
| :--- | :--- | :---: | :--- |
| **NM-6.1** | Optimization Concepts — constrained vs. unconstrained optimization | 🟡 ⚠️ | 2021 |
| **NM-6.2** | One-Dimensional Unconstrained Optimization — Newton's method for a maximum/minimum | 🟡 ⚠️ | 2021 |
| **NM-6.3** | Optima from Tabulated Data — locating the x at which y is maximum from a difference table | 🟡 | 2018 |

## NM-7 · Numerical Differentiation

| ID | Subtopic | Tier | Years Appeared |
| :--- | :--- | :---: | :--- |
| **NM-7.1** | Basis & Difference Formulas — what numerical differentiation rests on, forward/backward/central difference equations | 🟠 | 2019 |
| **NM-7.2** | First Derivative from Tabulated Data | 🟠 | 2019, 2020, 2021, 2022 |
| **NM-7.3** | Second Derivative & Formula Derivation — deriving `d²y/dx²` for a tabulated function, Newton's forward form | 🟠 ⚠️ | 2017, 2018, 2021 |
| **NM-7.4** | Applied Differentiation — inductor voltage `v = L·di/dt`, angular velocity from angular displacement, real-life applications | 🟠 | 2019, 2020, 2021 |

## NM-8 · Ordinary Differential Equations

| ID | Subtopic | Tier | Years Appeared |
| :--- | :--- | :---: | :--- |
| **NM-8.1** | IVP vs. BVP Concepts — definitions and the difference in solution approach | 🟠 | 2021, 2024 |
| **NM-8.2** | Euler's Method — discussion, limitation, numeric march | 🔴 | 2018, 2019, 2020, 2021, 2023 |
| **NM-8.3** | Modified Euler / Heun's Method — derivation, predictor-corrector march | 🟠 | 2017, 2018, 2020 |
| **NM-8.4** | Runge-Kutta 2nd Order — predictor and corrector steps | 🟠 | 2020, CT-02B |
| **NM-8.5** | Runge-Kutta 4th Order — full four-slope march, comparison against RK2 | 🔴 | 2017, 2018, 2019, 2024, CT-02B |
| **NM-8.6** | Higher-Order & Systems of ODEs — second-order ODE reduced to a first-order system | 🟡 | 2018 |
| **NM-8.7** | ODE Formulation from Physical Problems — developing the ODE then solving it | 🟡 | 2021 |
| **NM-8.8** | Boundary Value Problems — numerical solution, general approach | 🟡 ⚠️ | 2021, 2024 |

## NM-9 · Eigenvalue Problems

| ID | Subtopic | Tier | Years Appeared |
| :--- | :--- | :---: | :--- |
| **NM-9.1** | Eigenvalues & Eigenvectors — characteristic equation of a 3×3 matrix | 🟡 ⚠️ | 2017, 2023 |

## NM-10 · Partial Differential Equations

| ID | Subtopic | Tier | Years Appeared |
| :--- | :--- | :---: | :--- |
| **NM-10.1** | PDE Classification & Theory — types of PDE, numerical iterative solution process | 🟡 | 2020 |
| **NM-10.2** | Laplace Equation — 5-point finite-difference stencil on a square region | 🟡 | 2018, 2019, 2020 |
| **NM-10.3** | Poisson Equation — non-homogeneous 5-point stencil | 🟡 | 2021 |
| **NM-10.4** | Liebmann's Iterative Method — potential distribution at interior nodes | 🟡 | 2018, 2020 |
| **NM-10.5** | Boundary Conditions in PDEs — importance in numerical solution | 🟡 | 2024 |

---

# SECTION 2 — DISCRETE MATHEMATICS

> **Evidence base: 2022, 2023, 2024 and CT-04 only** (4 sources). Discrete Mathematics entered this course with the 2022 OBE curriculum revision.

## DM-1 · Set Theory

| ID | Subtopic | Tier | Years Appeared |
| :--- | :--- | :---: | :--- |
| **DM-1.1** | Operations on Sets — union, intersection, difference, complement, Cartesian product | ⚫ | — |
| **DM-1.2** | Algebraic Properties of Sets — identities, De Morgan's laws for sets | ⚫ | — |
| **DM-1.3** | Computer Representation of Sets — bit strings | ⚫ | — |
| **DM-1.4** | Power Set Theorem — the cardinality of the power set of S is 2^n, where n is the number of elements in S | ⚫ | — |

## DM-2 · Relations

| ID | Subtopic | Tier | Years Appeared |
| :--- | :--- | :---: | :--- |
| **DM-2.1** | Properties of Relations — reflexive, symmetric, antisymmetric, transitive | ⚫ | — |
| **DM-2.2** | Binary Relations — representation by matrix and digraph | ⚫ | — |
| **DM-2.3** | Partial Ordering Relations — posets, Hasse diagrams | ⚫ | — |
| **DM-2.4** | Equivalence Relations — equivalence classes, partitions | ⚫ | — |

## DM-3 · Propositional Logic

> **The largest block in Section B — but its shape is not identical across the three OBE papers.**
> 2022 and 2023 both place exactly two full sets in Q.5 and Q.6. **2024 differs:** its biconditional item
> moved to **Q.7b**, so Logic takes **Q.5 + Q.6 + Q.7b = 24 marks (2.4 sets)**, and Q.7a became the
> off-syllabus algorithms question — so 2024's Number Theory fell to 8 marks, its lowest of the three years.
> Treat Q.5 + Q.6 as the stable core and Q.7 / Q.8 as the variable slots.

| ID | Subtopic | Tier | Years Appeared |
| :--- | :--- | :---: | :--- |
| **DM-3.1** | Propositions & Syntax — definition of propositional logic, proposition vs. ordinary sentence, proposition vs. propositional variable | 🔴 | 2022, 2024 |
| **DM-3.2** | Logical Connectives & Truth Tables — ¬, ∧, ∨, →, ↔, ⊕; biconditional truth evaluation | 🔴 | 2022, 2023, 2024, CT-04 |
| **DM-3.3** | Tautology, Contradiction & Contingency — characteristics, truth-table proofs | 🔴 | 2023, 2024, CT-04 |
| **DM-3.4** | Valid, Satisfiable & Unsatisfiable Formulas — classification, satisfying assignments | 🟠 | 2024, CT-04 |
| **DM-3.5** | Logical Equivalence — proving equivalence by truth table or algebraically | 🟠 | 2023 |
| **DM-3.6** | Translation: English → Logic — connective traps ("unless", "only if", "if and only if", "neither…nor") | 🟠 | 2024, CT-04 |
| **DM-3.7** | System Specification & Consistency — translating engineering requirements, testing consistency | 🟠 | 2024, CT-04 |
| **DM-3.8** | Normal Forms & Functional Completeness — CNF, DNF, rewriting with only ¬/∨/∧, functional completeness of {¬, ∧} | 🔴 | 2022, 2024, CT-04 |
| **DM-3.9** | Rules of Inference & Valid Arguments — modus ponens, modus tollens, hypothetical syllogism, disjunctive syllogism; multi-premise argument construction | 🔴 | 2022, 2023 |
| **DM-3.10** | Logic Puzzles — knights/knaves/spies, exactly-one-truth-teller problems, Lewis Carroll syllogisms | 🟠 | 2022, 2023 |
| **DM-3.11** | Logic Gates & Digital Circuits — building a circuit from a compound proposition | 🟡 | 2023 |
| **DM-3.12** | Predicates & Quantifiers — universal/existential quantification, nested quantifiers (∀ → implication, ∃ → conjunction) | ⚫ | — |
| **DM-3.13** | Logic Extensions — fuzzy logic truth values | 🟡 | 2022 |

## DM-4 · Proof Techniques

| ID | Subtopic | Tier | Years Appeared |
| :--- | :--- | :---: | :--- |
| **DM-4.1** | Structure of Formal Proofs | ⚫ | — |
| **DM-4.2** | Direct Proofs | ⚫ (never standalone — see DM-5.9) | 2022, 2023 *(embedded only)* |
| **DM-4.3** | Proof by Contradiction | ⚫ | — |
| **DM-4.4** | Proof by Contraposition | ⚫ | — |
| **DM-4.5** | Mathematical Induction | ⚫ | — |

## DM-5 · Number Theory

| ID | Subtopic | Tier | Years Appeared |
| :--- | :--- | :---: | :--- |
| **DM-5.1** | Divisibility & Fundamental Theorem of Arithmetic | ⚫ | — *(invoked only implicitly by 2023 Q.7(c), which is filed under DM-5.2)* |
| **DM-5.2** | Prime Numbers — primality, composite-number properties | 🟠 | 2023 |
| **DM-5.3** | GCD, LCM & Euclidean Algorithm — including the Extended Euclidean algorithm | 🟠 ⚠️ | 2022 |
| **DM-5.4** | Modular Arithmetic & Congruence — `a ≡ r (mod n)` combinations, linear/quadratic/cubic forms | 🔴 | 2022, 2023, 2024 |
| **DM-5.5** | Modular Exponentiation — fast/repeated-squaring exponentiation | 🔴 | 2022, 2024 |
| **DM-5.6** | Fermat's Little Theorem | 🟡 | 2022 |
| **DM-5.7** | Chinese Remainder Theorem — construction and all solutions to a congruence system | 🟠 | 2022 |
| **DM-5.8** | Number Bases & Binary Arithmetic — binary addition | 🟡 | 2023 |
| **DM-5.9** | Number-Theoretic Proofs — proving congruence identities and prime-divisor bounds | 🟠 | 2022, 2023 |

## DM-6 · Introduction to Counting

| ID | Subtopic | Tier | Years Appeared |
| :--- | :--- | :---: | :--- |
| **DM-6.1** | Basic Counting Techniques — sum rule, product rule | 🟠 | 2022 |
| **DM-6.2** | Inclusion and Exclusion | ⚫ | — |
| **DM-6.3** | Pigeonhole Principle — basic and generalized forms, real-world examples, pigeonhole proofs | 🔴 | 2022, 2023, 2024 |
| **DM-6.4** | Permutation | ⚫ | — |
| **DM-6.5** | Combination — `C(n, r)` selection problems | 🟠 | 2023 |
| **DM-6.6** | Binomial Theorem — expansion and coefficient extraction | 🟠 | 2023 |

## DM-7 · Supplementary Topics

| ID | Subtopic | Tier | Years Appeared |
| :--- | :--- | :---: | :--- |
| **DM-7.1** | Algorithms & Complexity — sorting, binary search with pseudocode, greedy strategy, time complexity | 🟡 📘 | 2024 |
| **DM-7.2** | Relevance of Discrete Mathematics — importance in computer science and algorithm design | 🟡 | 2023 |

---

# Quick Reference Index

## Numerical Methods — 10 topics / 62 subtopics

| Topic | Subtopics | Count |
| :--- | :--- | :---: |
| **NM-1** Modeling, Computers & Error Analysis | NM-1.1 … NM-1.7 | 7 |
| **NM-2** Roots of Equations | NM-2.1 … NM-2.7 | 7 |
| **NM-3** Linear Algebraic Equations | NM-3.1 … NM-3.8 | 8 |
| **NM-4** Curve Fitting | NM-4.1 … NM-4.12 | 12 |
| **NM-5** Numerical Integration | NM-5.1 … NM-5.7 | 7 |
| **NM-6** Optimization | NM-6.1 … NM-6.3 | 3 |
| **NM-7** Numerical Differentiation | NM-7.1 … NM-7.4 | 4 |
| **NM-8** Ordinary Differential Equations | NM-8.1 … NM-8.8 | 8 |
| **NM-9** Eigenvalue Problems | NM-9.1 | 1 |
| **NM-10** Partial Differential Equations | NM-10.1 … NM-10.5 | 5 |

## Discrete Mathematics — 7 topics / 43 subtopics

| Topic | Subtopics | Count |
| :--- | :--- | :---: |
| **DM-1** Set Theory | DM-1.1 … DM-1.4 | 4 |
| **DM-2** Relations | DM-2.1 … DM-2.4 | 4 |
| **DM-3** Propositional Logic | DM-3.1 … DM-3.13 | 13 |
| **DM-4** Proof Techniques | DM-4.1 … DM-4.5 | 5 |
| **DM-5** Number Theory | DM-5.1 … DM-5.9 | 9 |
| **DM-6** Introduction to Counting | DM-6.1 … DM-6.6 | 6 |
| **DM-7** Supplementary Topics | DM-7.1 … DM-7.2 | 2 |

**Total: 17 topics, 105 subtopics.**

---

# Tier Summary

| Tier | Numerical Methods | Discrete Mathematics |
| :--- | :--- | :--- |
| 🔴 **Tier 1 — High priority** | NM-1.1, NM-1.4, NM-1.5, NM-1.6, NM-2.1, NM-2.2, NM-2.3, NM-2.4, NM-2.6, NM-3.2, NM-3.5, NM-3.8, NM-4.1, NM-4.2, NM-4.3, NM-4.6, NM-4.7, NM-4.11, NM-5.2, NM-5.4, NM-8.2, NM-8.5 | DM-3.1, DM-3.2, DM-3.3, DM-3.8, DM-3.9, DM-5.4, DM-5.5, DM-6.3 |
| 🟠 **Tier 2 — Secondary** | NM-1.3, NM-2.5, NM-2.7, NM-3.1, NM-3.4, NM-4.4, NM-4.5, NM-4.8, NM-4.9, NM-5.1, NM-5.3, NM-5.5, NM-5.6, NM-5.7, NM-7.1, NM-7.2, NM-7.3, NM-7.4, NM-8.1, NM-8.3, NM-8.4 | DM-3.4, DM-3.5, DM-3.6, DM-3.7, DM-3.10, DM-5.2, DM-5.3, DM-5.7, DM-5.9, DM-6.1, DM-6.5, DM-6.6 |
| 🟡 **Tier 3 — Light** | NM-1.2, NM-3.3, NM-3.6, NM-3.7, NM-4.10, NM-6.1, NM-6.2, NM-6.3, NM-8.6, NM-8.7, NM-8.8, NM-9.1, NM-10.1, NM-10.2, NM-10.3, NM-10.4, NM-10.5 | DM-3.11, DM-3.13, DM-5.6, DM-5.8, DM-7.1, DM-7.2 |
| ⚫ **Tier 4 — Never examined** | NM-1.7, NM-4.12 | DM-1.1–1.4, DM-2.1–2.4, DM-3.12, DM-4.1–4.5, DM-5.1, DM-6.2, DM-6.4 |

**Tier totals:** Tier 1 = 30 · Tier 2 = 33 · Tier 3 = 23 · Tier 4 = 19 · **sum = 105 ✓**

### Frequency Cross-Check — why tier is not a frequency rank

| Tier | Subtopics | Sources-appeared range | Mean |
| :--- | ---: | :--- | ---: |
| 🔴 Tier 1 | 30 | 2 – 7 | 4.4 |
| 🟠 Tier 2 | 33 | 1 – 5 | 2.2 |
| 🟡 Tier 3 | 23 | 1 – 3 | 1.3 |
| ⚫ Tier 4 | 19 | **0 – 2** | 0.16 |

Tier *means* are correctly ordered (4.4 > 2.2 > 1.3), and Tier 1 no longer contains any subtopic
with a single appearance — the ranges now separate cleanly at the bottom (Tier 1 starts at 2). Frequency
still does not *determine* tier, so three cases are worth naming while sorting:

- **Four Tier-1 subtopics sit at 2 sources** — **DM-3.1** (proposition definitions), **DM-3.9** (rules of
  inference), **DM-5.5** (modular exponentiation) and **NM-5.4** (Simpson comparison). DM-5.5 is recycled
  *verbatim* in 2022 and 2024 and is Tier 1 for that reason, not for breadth; NM-5.4 is a high-yield
  theory item that banks marks whenever it appears.
- **Tier 4 is not a clean zero tier.** **DM-4.2** (Direct Proofs) appears twice but only *embedded* — a
  proof sits inside 2022 Q.7(d) and 2023 Q.7(c), filed under DM-5.9, and no paper has ever asked for a
  proof technique by name. **DM-5.1** (Fundamental Theorem of Arithmetic) is likewise invoked implicitly
  by 2023 Q.7(c) without being stated. All other Tier-4 subtopics are true zeroes.
- **The three 2024-introduced subtopics** — **DM-3.4** (validity classification), **DM-3.6** (translation)
  and **DM-3.7** (specification consistency) — all descend from the single question 2024 Q.5 and are
  Tier 2. DM-3.6 in particular has **never** been asked in a final paper, only in CT-04; treat it as
  recognition-level despite the lecture emphasis both note sets place on translation.

**Rule of use: read the *Years Appeared* column for frequency, and the tier for priority.**

## ⚠️ Danger-Zone Subtopics (examined but not covered in class notes)

Ranked by severity — these are the self-study gaps identified in `combined_analysis_report.md`:

| Rank | ID | Subtopic | Why |
| :---: | :--- | :--- | :--- |
| 1 | **NM-4.2 / 4.3 / 4.4** | Least-Squares Regression (linear, non-linear, criteria) | **6 of 8 papers**, 41 marks (2017, 2018, 2019, 2020, 2022, 2024); marked "self-study" or missing in both note sets. **Not 8/8** — 2021 and 2023 ask only for a curve-fitting *example*/discussion, never a fit |
| 2 | **NM-4.10** | Gauss Forward / Backward / Stirling | **Raidah's notes: self-study. Fahad's notes: instructor scope note — off the CT but "can appear in the Semester Final."** Already examined in 2021 Q.4b |
| 3 | **NM-1.6** | Taylor Series & Truncation Error | 5 papers + CT-01; missing from Raidah's notes |
| 4 | **NM-9.1** | Eigenvalues & Eigenvectors | Twice, **same matrix both times**; absent from both note sets |
| 5 | **NM-8.8** | Boundary Value Problems | 2021 (solve) + 2024 (theory); absent from both note sets |
| 6 | **NM-1.2** | Mathematical Modeling | 2024 + CT-01; "entirely absent" from notes |
| 7 | **DM-5.3** | Extended Euclidean Algorithm | 2022; explicitly self-study in both note sets |
| 8 | **NM-7.3** | Second-Derivative Formula Derivation | 3 papers; notes cover forward difference only |
| 9 | **NM-3.3** | LU Decomposition | 2017 theory only (4 marks); absent from both note sets |
| 10 | **DM-7.1** | Algorithms & Complexity | 2024 Q.7a (6 marks); 📘 **off-syllabus** |

## Over-Taught Subtopics (covered in depth in class, never examined)

Keep these at recognition level — see `combined_analysis_report.md` §3③.

| ID | Subtopic | Class-note status |
| :--- | :--- | :--- |
| — | **Cubic Splines** *(not a syllabus item; no ID assigned)* | Both: Runge's phenomenon, natural cubic spline formulation, worked problem. **Raidah only:** "Governing Tridiagonal Equation" and the "memorize the tridiagonal equations" tip — Fahad's notes have no tridiagonal section. **0/8 papers.** |
| **DM-1.1 – DM-1.4** | Set Theory | Fahad: "fully covered & high priority". **0/3 papers.** |
| **DM-3.12** | Predicates & Quantifiers | Both: heavy emphasis, slide-sourced. **0/3 papers.** |
| **DM-4.3 / DM-4.4** | Proof by Contradiction / Contraposition | Both: covered (√2 irrational). **0/3 papers.** |
| — | **Functions (injective/surjective/bijective)** *(not a syllabus item)* | Fahad: "covered extensively". **0/3 papers.** |

---

# Sorting Rules

Conventions applied when assigning questions to subtopics in the sorted question bank:

1. **Classify by the method required, not by the surface framing.** A DC-circuit question solved by Gauss-Seidel is `NM-3.5` (with a cross-reference to `NM-3.8`), not an "electrical" topic.
2. **Multi-part questions are split.** A question with parts (a), (b), (c) spanning different topics is listed under each relevant subtopic, with the part letter given.
3. **Cross-references are explicit.** A question belonging to two subtopics is filed under its primary subtopic and cross-referenced from the secondary one.
4. **Theory and computation are kept together** within a subtopic but visually distinguished, since the two recycle at different rates.
5. **Repeats are marked.** Verbatim and near-verbatim repeats carry a 🔁 marker naming the other year(s).
6. **Era is always visible.** Pre-OBE (2017–2021) and OBE (2022–2024) questions are labelled, since the marks scale differs (12 vs. 10 marks per question).

---

*Taxonomy derived from `ECE2213_Syllabus.md`, cross-validated against `PreviousYearAnalysisReport.md`, `question_tally_audit.md` and `combined_analysis_report.md`.*

> **Two deliberate divergences from the official syllabus — do not read topic counts as syllabus unit counts.**
> The syllabus lists **7** Numerical Methods units; this taxonomy uses **10** NM topics, splitting the
> syllabus's combined *"Numerical Differentiation and Differential Equations"* unit into NM-7
> (Differentiation), NM-8 (ODE), NM-9 (Eigenvalue) and NM-10 (PDE) — because exam frequency and class-note
> coverage diverge sharply across those four. The syllabus lists **6** Discrete Mathematics units; this
> taxonomy uses **7** DM topics, adding **DM-7 Supplementary Topics** to hold items that appear in papers
> but sit outside the syllabus (**DM-7.1**, flagged 📘). Every subtopic ID maps to at least one syllabus
> bullet except DM-7.1 / DM-7.2, which by construction do not.
