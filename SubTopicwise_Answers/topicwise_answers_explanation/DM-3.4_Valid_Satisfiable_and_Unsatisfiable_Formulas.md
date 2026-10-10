---
title: "DM-3.4 · Valid, Satisfiable & Unsatisfiable Formulas"
tags:
  - numerical-methods
  - discrete-mathematics
  - topicwise
---





[🏠 Subtopic Index](00_Index.md) | [← Prev: DM-3.3 Tautology, Contradiction & Contingency](DM-3.3_Tautology_Contradiction_and_Contingency.md) | [Next: DM-3.5 Logical Equivalence →](DM-3.5_Logical_Equivalence.md)

---

# DM-3.4 · Valid, Satisfiable & Unsatisfiable Formulas

Every block below is copied from `../answers_explanation/`. The reasoning
is written once, in the year-wise file, and is not restated here.


### [2024 Q.5(b)]

**Question.** Given the propositional formula $(p \to q) \land (q \to r)$, determine whether the formula is valid, satisfiable or unsatisfiable.

*[Marks: 04, CO: 2]*

**Solution.**

**The three definitions, because the question needs them.**

- **Valid**: true in *every* row of the truth table. A valid formula is called a
  tautology. Validity means "true for all possible truth values of $p, q, r$".
- **Satisfiable**: true in *at least one* row. A satisfiable formula is not
  necessarily valid; it only needs one witness.
- **Unsatisfiable**: true in *no* row. An unsatisfiable formula is a
  contradiction.

These are not mutually exclusive categories in the order they were asked. Every
valid formula is also satisfiable, because it is true in every row including at
least one. The standard classification of a formula asks whether it is a
tautology, a contradiction, or neither, and then reports satisfiability
separately.

**Building the truth table.** Three variables means $2^3 = 8$ rows.

| $p$ | $q$ | $r$ | $p \to q$ | $q \to r$ | $(p \to q) \land (q \to r)$ |
| :-: | :-: | :-: | :-: | :-: | :-: |
| T | T | T | T | T | **T** |
| T | T | F | T | F | **F** |
| T | F | T | F | T | **F** |
| T | F | F | F | T | **F** |
| F | T | T | T | T | **T** |
| F | T | F | T | F | **F** |
| F | F | T | T | T | **T** |
| F | F | F | T | T | **T** |

**Reading the table.** The formula is true in rows 1, 5, 7 and 8, and false in
rows 2, 3, 4 and 6.

$$\boxed{\text{Satisfiable but not valid}}$$

The formula is **not valid**, because there are rows where it is false. It is
**satisfiable**, because there are rows where it is true. It is **not
unsatisfiable**, for the same reason.

**The reasoning behind the result, stated in English.** $p \to q$ says that $p$
being true requires $q$ to be true. $q \to r$ says $q$ requires $r$. Together
they say the chain $p$ then $q$ then $r$ is consistent, which is exactly the
hypothetical syllogism. The formula fails precisely when $p$ and $q$ are both
true but $r$ is false: then $p \to q$ holds and $q \to r$ fails. That row is the
counterexample to validity, and it is the one to name in an answer.

> [!warning] The trap: assuming a true implication is a true conjunction
> $p \to q$ is true in three of four rows, so it is "almost always true". Two of
> them conjoined are true only in four of eight rows, not six. Conjunction
> requires both parts, so the result is false whenever either implication is
> false. The common slip is to reason "successful thesis contains hypothesis,
> successful thesis contains conclusion, therefore the combined formula is
> successful" which conflates *each part being often true* with *both parts being
> true together*.

---

**Answered in phase P6, in `../CT_Questions/`.**

- *CT-04 Q.3(d)* is a class-test question. Its answer is in `../CT_Questions/CT_answers_exam_style.md`, with the reasoning in `../CT_Questions/CT_answers_explanation.md`.

---

[🏠 Subtopic Index](00_Index.md) | [← Prev: DM-3.3 Tautology, Contradiction & Contingency](DM-3.3_Tautology_Contradiction_and_Contingency.md) | [Next: DM-3.5 Logical Equivalence →](DM-3.5_Logical_Equivalence.md)
