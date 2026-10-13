---
title: "DM-3.3 · Tautology, Contradiction & Contingency"
tags:
  - numerical-methods
  - discrete-mathematics
  - topicwise
---


[🏠 Subtopic Index](00_Index.md) | [← Prev: DM-3.2 Logical Connectives & Truth Tables](DM-3.2_Logical_Connectives_and_Truth_Tables.md) | [Next: DM-3.4 Valid, Satisfiable & Unsatisfiable Formulas →](DM-3.4_Valid_Satisfiable_and_Unsatisfiable_Formulas.md)

---

# DM-3.3 · Tautology, Contradiction & Contingency

Every block below is copied from `../answers_exam_style/`, which is the
only place an answer is authored. A number here is the same number, character
for character, as the one it came from.


### [2023 Q.5(c)]

**Question.** Show that each of the conditional statements is a tautology by using truth tables: (i) $\neg(p \to q) \to p$, (ii) $p \to (p \lor q)$.

**Solution.**

**(i) $\neg(p \to q) \to p$**

$p \to q$ is $F$ only when $p = T, q = F$. So $\neg(p \to q)$ is $T$ only there.

| $p$ | $q$ | $p \to q$ | $\neg(p \to q)$ | $\neg(p \to q) \to p$ |
| :-: | :-: | :-: | :-: | :-: |
| F | F | T | F | T |
| F | T | T | F | T |
| T | F | F | T | T |
| T | T | T | F | T |

The final column is T in every row.

**Algebraic confirmation.** $\neg(p \to q) = \neg(\neg p \lor q) = p \land \neg q$.
Then $(p \land \neg q) \to p = \neg(p \land \neg q) \lor p = (\neg p \lor q) \lor p = \top$.

$$
\boxed{(i)\ \neg(p \to q) \to p \text{ is a tautology}}
$$

**(ii) $p \to (p \lor q)$**

| $p$ | $q$ | $p \lor q$ | $p \to (p \lor q)$ |
| :-: | :-: | :-: | :-: |
| F | F | F | T |
| F | T | T | T |
| T | F | T | T |
| T | T | T | T |

The final column is T in every row.

**Algebraic confirmation.** $p \to (p \lor q) = \neg p \lor (p \lor q) = (\neg p \lor p) \lor q = \top$.

$$
\boxed{(ii)\ p \to (p \lor q) \text{ is a tautology}}
$$

---

### [2024 Q.6(a)]

**Question.** Explain the concepts of tautology, contradiction and contingency in propositional logic. Explain their characteristics with example.

**Solution.**

Every propositional formula falls into exactly one of three classes, decided by
its truth value across all assignments.

**1. Tautology.** True for **every** assignment of its variables. It is also called a
valid formula. It states a fact that cannot fail.

- Characteristic: the final column of the truth table is T throughout.
- Example: $p \lor \neg p$. One of $p$ and $\neg p$ must hold, so the disjunction
  is always true. No values needed.

**2. Contradiction.** False for **every** assignment. It is also called an unsatisfiable
formula, or an inconsistent set of conditions.

- Characteristic: the final column is F throughout. The negation is a tautology.
- Example: $p \land \neg p$. A proposition cannot be true and false at once.

**3. Contingency.** True for **some** assignments and false for **others**. It is also
called a satisfiable formula, or a non-tautology.

- Characteristic: the final column holds both T and F. It is the only class that
  depends on the input.
- Example: $p \lor q$. True unless both $p$ and $q$ are false.

**Comparison**

| | Tautology | Contradiction | Contingency |
| :-- | :-- | :-- | :-- |
| True for | All assignments | None | Some |
| False for | None | All assignments | Some |
| Negation | Contradiction | Tautology | Contingency |
| Truth table last column | All T | All F | Mixed |

**Worked example, classifying $A \to (B \lor \neg A)$**

| $A$ | $B$ | $\neg A$ | $B \lor \neg A$ | $A \to (B \lor \neg A)$ |
| :-: | :-: | :-: | :-: | :-: |
| F | F | T | T | T |
| F | T | T | T | T |
| T | F | F | F | F |
| T | T | F | T | T |

The last column holds T, T, F, T, so the formula is a **contingency**.

$$
\boxed{\text{tautology (always T), contradiction (always F), contingency (mixed)}}
$$

---

**Answered in phase P6, in `../CT_Questions/`.**

- *CT-04 Q.1* is a class-test question. Its answer is in `../CT_Questions/CT_answers_exam_style.md`, with the reasoning in `../CT_Questions/CT_answers_explanation.md`.

---

[🏠 Subtopic Index](00_Index.md) | [← Prev: DM-3.2 Logical Connectives & Truth Tables](DM-3.2_Logical_Connectives_and_Truth_Tables.md) | [Next: DM-3.4 Valid, Satisfiable & Unsatisfiable Formulas →](DM-3.4_Valid_Satisfiable_and_Unsatisfiable_Formulas.md)
