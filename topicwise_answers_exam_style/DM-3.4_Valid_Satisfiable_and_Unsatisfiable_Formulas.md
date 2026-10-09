---
title: "DM-3.4 · Valid, Satisfiable & Unsatisfiable Formulas"
tags:
  - numerical-methods
  - discrete-mathematics
  - topicwise
---

# DM-3.4 · Valid, Satisfiable & Unsatisfiable Formulas

Every block below is copied from `../answers_exam_style/`, which is the
only place an answer is authored. A number here is the same number, character
for character, as the one it came from.


### [2024 Q.5(b)]

**Question.** Given the propositional formula $(p \to q) \land (q \to r)$, determine whether the formula is valid, satisfiable or unsatisfiable.

**Solution.**

The three words are tested separately.

- **Valid (a tautology):** true for every assignment of $p, q, r$.
- **Satisfiable:** true for at least one assignment.
- **Unsatisfiable (a contradiction):** false for every assignment.

**Step 1. Expand the implications.**

$$
(p \to q) \land (q \to r) = (\neg p \lor q) \land (\neg q \lor r)
$$

**Step 2. Full truth table.**

| $p$ | $q$ | $r$ | $p \to q$ | $q \to r$ | $(p \to q) \land (q \to r)$ |
| :-: | :-: | :-: | :-: | :-: | :-: |
| F | F | F | T | T | **T** |
| F | F | T | T | T | **T** |
| F | T | F | T | F | F |
| F | T | T | T | T | **T** |
| T | F | F | F | T | F |
| T | F | T | F | T | F |
| T | T | F | T | F | F |
| T | T | T | T | T | **T** |

**Step 3. The verdict.** The column holds T in four rows and F in four rows.

- Not true in every row, so **not valid**.
- True in rows 1, 2, 4 and 8, so **satisfiable**.

$$
\boxed{\text{Satisfiable but not valid}}
$$

> [!note] Why it is not valid
> Any row with $p = T, q = F$ falsifies $p \to q$ and hence the whole
> formula, whatever $r$ is. Rows 5 and 6 are exactly that.

> [!info] What the formula means
> It is the transitivity rule. If the three rows of the truth table describe
> states that really occur, then "if $p$ then $q$" together with "if $q$ then $r$"
> forces "if $p$ then $r$". The table shows the rule does not hold in general, so
> it needs an extra premise to become a tautology.

---

**Answered in phase P6, in `../CT_Questions/`.**

- *CT-04 Q.3(d)* is a class-test question. Its answer is in `../CT_Questions/CT_answers_exam_style.md`, with the reasoning in `../CT_Questions/CT_answers_explanation.md`.
