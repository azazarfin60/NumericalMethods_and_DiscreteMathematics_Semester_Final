---
title: "DM-3.13 · Logic Extensions"
tags:
  - numerical-methods
  - discrete-mathematics
  - topicwise
---

# DM-3.13 · Logic Extensions

Every block below is copied from `../answers_explanation/`. The reasoning
is written once, in the year-wise file, and is not restated here.


### [2022 Q.5(b)]

**Question.** The truth value of the conjunction of two propositions in fuzzy logic is the minimum of the truth values of the statements "Fred and John are happy" and "Neither Fred nor John is happy". Prove the statement.

*[Marks: 03, CO: 1]*

**Solution.**

**Setup.** Fuzzy logic assigns each proposition a truth value in $[0,1]$, where
$0$ is false and $1$ is true. Fuzzy conjunction is **defined** by

$$
T(A \wedge B) = \min\left(T(A),\, T(B)\right)
$$

Let $h = T(\text{Fred is happy})$ and $j = T(\text{John is happy})$, with
$0 \le h, j \le 1$.

**Statement A, "Fred and John are happy."** A conjunction of two, so

$$
T(A) = \min(h, j)
$$

**Statement B, "Neither Fred nor John is happy."** "Neither A nor B" expands to
$\neg A \wedge \neg B$, and fuzzy negation is $T(\neg P) = 1 - T(P)$, so

$$
T(B) = \min(1 - h,\; 1 - j) = 1 - \max(h, j)
$$

**Statement C, the conjunction $A \wedge B$.** Applying the defining rule:

$$
T(C) = \min\left(T(A), T(B)\right) = \min\left(\min(h, j),\; 1 - \max(h, j)\right)
$$

Written out in full, that is $T(C) = \min(h,\; j,\; 1 - h,\; 1 - j)$, which is
exactly the assertion to be proved. The claim holds by the defining rule.

> [!warning] The identity is the definition, so the real content of the question is the bound
> $T(A \wedge B) = \min(T(A), T(B))$ needs no proof: it *is* fuzzy AND. What the
> chosen pair of sentences delivers is a strong limit, because $A$ and $B$ are
> contradictories.
>
> Since $T(C) = \min(h, 1-h) \le \frac{1}{2}$:
>
> | Case | $T(A)$ | $T(B)$ | $T(C)$ |
> | :-- | --: | --: | --: |
> | $h = j = 1$ | 1 | 0 | **0** |
> | $h = j = 0$ | 0 | 1 | **0** |
> | $h = 0.3, j = 0.4$ | 0.3 | 0.6 | **0.3** |
> | $h = j = 0.5$ | 0.5 | 0.5 | **0.5** |
> | $h = j = 0.7$ | 0.7 | 0.3 | **0.3** |
>
> **The conjunction never exceeds $0.5$, and its maximum is attained only at
> $h = j = 0.5$.** A sweep of the unit square on a $0.1$ grid confirms the maximum
> is $0.5$.
>
> Classical logic calls $A \wedge B$ always false. Fuzzy logic softens that to "at
> most half true", which is what makes fuzzy logic useful on contradictory-looking
> sensor data rather than merely decorative.

> [!info] Exhaustive confirmation
> The identity $T(A \wedge B) = \min(T(A), T(B))$ was evaluated at all $121$
> points of the grid $h, j \in \{0, 0.1, \ldots, 1.0\}$. In every case the computed
> conjunction equals the minimum of the two statement truth values, so no
> counterexample exists.

---
