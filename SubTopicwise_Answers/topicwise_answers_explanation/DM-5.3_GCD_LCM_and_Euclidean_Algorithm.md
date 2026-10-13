---
title: "DM-5.3 · GCD, LCM & Euclidean Algorithm"
tags:
  - numerical-methods
  - discrete-mathematics
  - topicwise
---


[🏠 Subtopic Index](00_Index.md) | [← Prev: DM-5.2 Prime Numbers](DM-5.2_Prime_Numbers.md) | [Next: DM-5.4 Modular Arithmetic & Congruence →](DM-5.4_Modular_Arithmetic_and_Congruence.md)

---

# DM-5.3 · GCD, LCM & Euclidean Algorithm

Every block below is copied from `../answers_explanation/`. The reasoning
is written once, in the year-wise file, and is not restated here.


### [2022 Q.7(c)]

**Question.** Find the greatest common divisor of 414 and 662 using the extended Euclidean algorithm.

*[Marks: 02, CO: 2]*

**Solution.**

**Step 1. Ordinary Euclidean algorithm.**

$$
662 = 1 \times 414 + 248
$$

$$
414 = 1 \times 248 + 166
$$

$$
248 = 1 \times 166 + 82
$$

$$
166 = 2 \times 82 + 2
$$

$$
82 = 41 \times 2 + 0
$$

The last nonzero remainder is $2$, so $\gcd(414, 662) = 2$.

**Step 2. Extended part, back-substituting** to find integers $s, t$ with
$414s + 662t = 2$.

From the last division, $2 = 166 - 2 \times 82$. Substitute $82 = 248 - 166$:

$$
2 = 166 - 2(248 - 166) = 3 \times 166 - 2 \times 248
$$

Substitute $166 = 414 - 248$:

$$
2 = 3(414 - 248) - 2 \times 248 = 3 \times 414 - 5 \times 248
$$

Substitute $248 = 662 - 414$:

$$
2 = 3 \times 414 - 5(662 - 414) = 8 \times 414 - 5 \times 662
$$

**Check.**

$$
8(414) - 5(662) = 3312 - 3310 = 2 \quad \checkmark
$$

$$\boxed{\gcd(414, 662) = 2, \qquad 8(414) - 5(662) = 2}$$

> [!info] The forward method gives the same coefficients
> The forward extended Euclidean algorithm, which carries the coefficients
> $(s, t)$ alongside the remainders rather than back-substituting, returns
> $(2, 8, -5)$: gcd $2$, $s = 8$, $t = -5$. The identity
> $8 \times 414 + (-5) \times 662 = 2$ verifies it.

> [!note] Why the extended form is worth the extra work
> Ordinary Euclid gives the gcd. The extended form also gives the Bezout
> coefficients $s$ and $t$, and that is what modular inverses are built from: if
> $\gcd(a, n) = 1$ then $sa + tn = 1$, so $s$ is the inverse of $a$ modulo $n$.
>
> Solving congruences by hand almost always needs this, so the question is really
> marking one skill that pays for itself in the parts to come.
>
> One habit saves time here: because $414$ and $662$ are both even, the gcd is
> even, which flags $2$ as plausible before the last division is reached.

---

[🏠 Subtopic Index](00_Index.md) | [← Prev: DM-5.2 Prime Numbers](DM-5.2_Prime_Numbers.md) | [Next: DM-5.4 Modular Arithmetic & Congruence →](DM-5.4_Modular_Arithmetic_and_Congruence.md)
