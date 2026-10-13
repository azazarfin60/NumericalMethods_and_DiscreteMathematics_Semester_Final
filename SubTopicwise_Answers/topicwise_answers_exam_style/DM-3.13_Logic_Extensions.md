---
title: "DM-3.13 · Logic Extensions"
tags:
  - numerical-methods
  - discrete-mathematics
  - topicwise
---


[🏠 Subtopic Index](00_Index.md) | [← Prev: DM-3.11 Logic Gates & Digital Circuits](DM-3.11_Logic_Gates_and_Digital_Circuits.md) | [Next: DM-5.2 Prime Numbers →](DM-5.2_Prime_Numbers.md)

---

# DM-3.13 · Logic Extensions

Every block below is copied from `../answers_exam_style/`, which is the
only place an answer is authored. A number here is the same number, character
for character, as the one it came from.


### [2022 Q.5(b)]

**Question.** The truth value of the conjunction of two propositions in fuzzy logic is the minimum of the truth values of the statements "Fred and John are happy" and "Neither Fred nor John is happy". Prove the statement.

**Solution.**

**Setup.** Fuzzy logic assigns each proposition a truth value in $[0, 1]$, where
$0$ is false and $1$ is true. Fuzzy conjunction is defined by

$$
T(A \wedge B) = \min\left(T(A),\, T(B)\right)
$$

**Assign variables.** Let

$$
h = T(\text{Fred is happy}), \qquad j = T(\text{John is happy}), \qquad 0 \le h, j \le 1
$$

**Statement A: "Fred and John are happy."** A conjunction of two, so

$$
T(A) = \min(h, j)
$$

**Statement B: "Neither Fred nor John is happy."** "Neither A nor B" expands to
$\neg A \wedge \neg B$, and fuzzy negation is $T(\neg P) = 1 - T(P)$:

$$
T(B) = \min(1 - h,\; 1 - j) = 1 - \max(h, j)
$$

**Statement C: the conjunction $A \wedge B$.** By the definition of fuzzy
conjunction,

$$
T(C) = \min\left(T(A), T(B)\right) = \min\left(\min(h, j),\; 1 - \max(h, j)\right)
$$

**This is exactly what the question asserts**, so the claim holds by the defining
rule. Written out in full,

$$
T(C) = \min(h,\; j,\; 1 - h,\; 1 - j)
$$

> [!info] Check by numerical sweep
> The identity $T(A \wedge B) = \min(T(A), T(B))$ was evaluated at all $121$
> points of the grid $h, j \in \{0, 0.1, \dots, 1.0\}$. In every case the
> computed conjunction equals the minimum of the two statement truth values, so
> no counterexample exists.

> [!warning] The bound is the content, not the identity
> The identity itself is the *definition* of fuzzy AND, so it needs no proof.
> The two chosen sentences yield a strong limit. Writing
> $T(C) = \min(h, 1-h) \le \frac{1}{2}$, so:
>
> | Case | $T(A)$ | $T(B)$ | $T(C)$ |
> | :-- | :-- | :-- | :-- |
> | $h = j = 1$ | 1 | 0 | **0** |
> | $h = j = 0$ | 0 | 1 | **0** |
> | $h = 0.3, j = 0.4$ | 0.3 | 0.6 | **0.3** |
> | $h = j = 0.5$ | 0.5 | 0.5 | **0.5** |
> | $h = j = 0.7$ | 0.7 | 0.3 | **0.3** |
>
> **The conjunction never exceeds $0.5$, and its maximum is attained only at
> $h = j = 0.5$.** A numerical sweep over the unit square confirms the maximum is
> $0.5$. Since $A$ and $B$ are contradictories, fuzzy logic cannot rate their
> conjunction above "barely true", even when the evidence is maximally split.
> Classical logic calls $A \wedge B$ always false; fuzzy logic softens that to
> "at most half true".

---

[🏠 Subtopic Index](00_Index.md) | [← Prev: DM-3.11 Logic Gates & Digital Circuits](DM-3.11_Logic_Gates_and_Digital_Circuits.md) | [Next: DM-5.2 Prime Numbers →](DM-5.2_Prime_Numbers.md)
