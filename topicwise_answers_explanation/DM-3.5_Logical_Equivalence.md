---
title: "DM-3.5 · Logical Equivalence"
tags:
  - numerical-methods
  - discrete-mathematics
  - topicwise
---

# DM-3.5 · Logical Equivalence

Every block below is copied from `../answers_explanation/`. The reasoning
is written once, in the year-wise file, and is not restated here.


### [2023 Q.6(a)]

**Question.** Show that $\neg(p \leftrightarrow q)$ and $\neg p \leftrightarrow q$ are logically equivalent.

*[Marks: 02, CO: 3]*

**Solution.**

**Step 1. Build the truth table.**

| $p$ | $q$ | $p \leftrightarrow q$ | $\neg(p \leftrightarrow q)$ | $\neg p$ | $\neg p \leftrightarrow q$ |
| :-: | :-: | :-: | :-: | :-: | :-: |
| F | F | T | F | T | F |
| F | T | F | T | T | T |
| T | F | F | T | F | T |
| T | T | T | F | F | F |

The two computed columns are identical: F, T, T, F reading down the rows
$F F$, $F T$, $T F$, $T T$. Identical columns on every row means the formulas are
logically equivalent.

$$
\boxed{\neg(p \leftrightarrow q) \equiv (\neg p \leftrightarrow q)}
$$

**Step 2. Algebraic proof.** Rewrite both sides to the same thing.

Left side:

$$
\neg(p \leftrightarrow q) = \neg\big[(p \to q) \land (q \to p)\big]
= \neg(p \to q) \lor \neg(q \to p)
= (p \land \neg q) \lor (\neg p \land q)
$$

This is exclusive-or. Right side:

$$
\neg p \leftrightarrow q = (\neg p \to q) \land (q \to \neg p) = (p \lor q) \land (\neg q \lor \neg p)
$$

Distribute:

$$
(p \lor q) \land (\neg q \lor \neg p) = \big[(p \land \neg q) \lor (p \land \neg p) \lor (q \land \neg q) \lor (q \land \neg p)\big]
$$

The middle two terms are contradictions, since nothing is both a statement and its
negation:

$$
= (p \land \neg q) \lor 0 \lor 0 \lor (\neg p \land q) = (p \land \neg q) \lor (\neg p \land q)
$$

Both sides reduce to the same expression, so the equivalence is proven.

**In words.** "$p$ and $q$ disagree" means exactly one of them is true. If $p$ is
false, then "q agrees with $\neg p$" means $q$ is true, which is precisely the
case where they disagree. Flipping one input and asking for agreement tests the
same thing as asking for disagreement without the flip.

> [!note] Where the asymmetry comes from
> It is worth pausing on why this works for the *biconditional* and would not for
> the conditional. There is no analogous identity $\neg(p \to q) \equiv \neg p \to q$,
> and trying to assume one is a common slip.
>
> The reason is that $\leftrightarrow$ is symmetric under negation of an input
> while $\to$ is not. $p \leftrightarrow q$ is T when $p$ and $q$ agree. Negating
> $p$ makes it T when $p$ and $q$ *disagree*, which is exactly when
> $\neg(p \leftrightarrow q)$ is T. With $\to$, negating an input changes the
> structure of the formula rather than just flipping its value, so no such
> identity exists.

---
