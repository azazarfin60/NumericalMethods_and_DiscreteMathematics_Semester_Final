---
title: "DM-3.7 · System Specification & Consistency"
tags:
  - numerical-methods
  - discrete-mathematics
  - topicwise
---

# DM-3.7 · System Specification & Consistency

Every block below is copied from `../answers_explanation/`. The reasoning
is written once, in the year-wise file, and is not restated here.


### [2024 Q.5(c)]

**Question.** Are these system specifications consistent?

*[Marks: 04, CO: 2]*

**Solution.**

> The system is in multiuser state if and only if it is operating normally, the
> kernel is functioning. The kernel is not functioning or the system is in
> interrupt mode. If the system is not in multiuser state, then it is in
> interrupt mode. The system is not in interrupt mode.

**What consistency means.** A set of specifications is consistent when at least
one assignment of truth values makes all of them true at the same time. The
object being tested is the **conjunction** of the four, not each one on its own.
Four individually plausible sentences can easily be jointly impossible.

**Assign variables.** One symbol per simple statement:

| Symbol | Meaning |
| :-- | :-- |
| $p$ | system is in multiuser state |
| $q$ | kernel is functioning |
| $r$ | system is in interrupt mode |

**Translate.** The four sentences become

| # | English | Logic |
| :-: | :-- | :-- |
| 1 | multiuser if and only if the kernel is functioning | $p \leftrightarrow q$ |
| 2 | kernel not functioning, or interrupt mode | $\neg q \lor r$ |
| 3 | if not multiuser, then interrupt mode | $\neg p \to r$, equivalent to $p \lor r$ |
| 4 | not in interrupt mode | $\neg r$ |

Two of these translations need care. Sentence 3 is a conditional whose
consequent is $r$, so $\neg p \to r$ is equivalent to $p \lor r$ by the
definition of implication, and writing it as $p \lor r$ makes the truth table
easier to read. Sentence 2 is a disjunction, so it is true whenever the kernel
is broken *or* interrupt mode holds; the mistake is to read it as a conjunction.

**Test all eight assignments.** Three variables, so $2^3 = 8$ rows.

| $p$ | $q$ | $r$ | (1) $p \leftrightarrow q$ | (2) $\neg q \lor r$ | (3) $p \lor r$ | (4) $\neg r$ | all four |
| :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| F | F | F | T | T | F | T | **F** |
| F | F | T | T | T | T | F | F |
| F | T | F | F | F | F | T | F |
| F | T | T | F | T | T | F | F |
| T | F | F | F | T | T | T | **F** |
| T | F | T | F | T | T | F | F |
| T | T | F | T | F | F | T | F |
| T | T | T | T | T | T | F | F |

No row satisfies all four, so the set is inconsistent.

**Reason without a table.** This is faster and worth writing alongside, since it
shows *where* the conflict is. Sentence 4 forces $r = \mathrm{F}$. Sentence 2,
$\neg q \lor r$, then has both terms false unless $q$ is false, so $q = \mathrm{F}$.
Sentence 1 ties $p$ to $q$, so $p = \mathrm{F}$. Sentence 3 then reads
$p \lor r = \mathrm{F} \lor \mathrm{F} = \mathrm{F}$, contradicting the requirement that
all four hold.

$$\boxed{\text{The specifications are INCONSISTENT: no assignment satisfies all four}}$$

> [!warning] Where the contradiction comes from
> Sentence 4 says the system is **never** in interrupt mode. Sentence 2 then
> forces the kernel to be broken. Sentence 1 ties multiuser state to a working
> kernel, so the system cannot be in multiuser state either. Sentence 3 says a
> system that is not in multiuser state must be in interrupt mode, which
> sentence 4 has already ruled out. The set describes a machine that cannot
> exist. In practice this means one of the four requirements is a typo, usually
> sentence 4.

> [!info] Check by exhaustive enumeration
> The truth table above is the exhaustive check: all $2^3 = 8$ assignments were
> tested and none satisfied the conjunction. The chain of forcing steps is the
> same argument presented as a derivation, and it reaches the same conclusion,
> which is the confirmation that no row was skipped. The two routes disagree only
> if a row in the table was mis-evaluated, so comparing the count of satisfying
> rows (zero) against the chain's result (zero) is a complete check.

---

---

**Also asked here.**

- *2024 Q.6(b)* is the same question as [[DM-3.8_Normal_Forms_and_Functional_Completeness|DM-3.8]], which is written in `DM-3.8`.
- *CT-04 Q.2(b)* is the same question as [[DM-3.8_Normal_Forms_and_Functional_Completeness|DM-3.8]], which is written in `DM-3.8`.
- *CT-04 Q.2(c)* is the same question as [[DM-3.2_Logical_Connectives_and_Truth_Tables|DM-3.2]], which is written in `DM-3.2`.
- *CT-04 Q.3(c)* is the same question as [[DM-3.2_Logical_Connectives_and_Truth_Tables|DM-3.2]], which is written in `DM-3.2`.

---

**Answered in phase P6, in `../CT_Questions/`.**

- *CT-04 Q.2(a)* is a class-test question. Its answer is in `../CT_Questions/CT_answers_exam_style.md`, with the reasoning in `../CT_Questions/CT_answers_explanation.md`.
- *CT-04 Q.3(b)* is a class-test question. Its answer is in `../CT_Questions/CT_answers_exam_style.md`, with the reasoning in `../CT_Questions/CT_answers_explanation.md`.
