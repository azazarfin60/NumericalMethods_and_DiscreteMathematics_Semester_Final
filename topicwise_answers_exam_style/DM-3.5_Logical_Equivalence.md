---
title: "DM-3.5 · Logical Equivalence"
tags:
  - numerical-methods
  - discrete-mathematics
  - topicwise
---

# DM-3.5 · Logical Equivalence

Every block below is copied from `../answers_exam_style/`, which is the
only place an answer is authored. A number here is the same number, character
for character, as the one it came from.


### [2023 Q.6(a)]

**Question.** Show that $\neg(p \leftrightarrow q)$ and $\neg p \leftrightarrow q$ are logically equivalent.

**Solution.**

**Step 1. Build the truth table.**

| $p$ | $q$ | $p \leftrightarrow q$ | $\neg(p \leftrightarrow q)$ | $\neg p$ | $\neg p \leftrightarrow q$ |
| :-: | :-: | :-: | :-: | :-: | :-: |
| F | F | T | F | T | F |
| F | T | F | T | T | T |
| T | F | F | T | F | T |
| T | T | T | F | F | F |

The two computed columns are identical: **F, T, T, F** reading down the rows
$F F$, $F T$, $T F$, $T T$. Hence the formulas are logically equivalent.

$$
\boxed{\neg(p \leftrightarrow q) \equiv (\neg p \leftrightarrow q)}
$$

**Step 2. Algebraic proof.** Rewrite both sides.

$$
\neg(p \leftrightarrow q) = \neg\big[(p \to q) \land (q \to p)\big]
= \neg(p \to q) \lor \neg(q \to p)
= (p \land \neg q) \lor (\neg p \land q)
$$

This is exclusive-or. Now the right-hand side,

$$
\neg p \leftrightarrow q = (\neg p \to q) \land (q \to \neg p) = (p \lor q) \land (\neg q \lor \neg p)
$$

Distribute:

$$
(p \lor q) \land (\neg q \lor \neg p)
= \big[(p \land \neg q) \lor (p \land \neg p) \lor (q \land \neg q) \lor (q \land \neg p)\big]
$$

$$
= (p \land \neg q) \lor 0 \lor 0 \lor (\neg p \land q) = (p \land \neg q) \lor (\neg p \land q)
$$

Both sides reduce to the same expression, so the equivalence is proven.

**In words.** "$p$ and $q$ disagree" is exactly one true statement. If $p$ is
false, then "$q$ agrees with $\neg p$" means $q$ is true, which is precisely the
case where they disagree. Flipping one input and asking for agreement tests the
same thing as asking for disagreement without the flip.

---
