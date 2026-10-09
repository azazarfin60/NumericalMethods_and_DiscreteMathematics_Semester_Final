---
title: "DM-5.9 · Number-Theoretic Proofs"
tags:
  - numerical-methods
  - discrete-mathematics
  - topicwise
---

# DM-5.9 · Number-Theoretic Proofs

Every block below is copied from `../answers_explanation/`. The reasoning
is written once, in the year-wise file, and is not restated here.


### [2022 Q.7(d)]

**Question.** Show that if $a$ and $b$ are positive integers then $(2^a - 1) \bmod (2^b - 1) \equiv 2^{a \bmod b} - 1$.

*[Marks: 02, CO: 2]*

**Solution.**

**Step 1. Write $a = qb + r$** with $q = \lfloor a/b \rfloor \ge 0$ and
$r = a \bmod b$, so $0 \le r < b$.

**Step 2. Reduce the power.**

$$
2^a - 1 = 2^{qb+r} - 1 = 2^r\left(2^{qb}\right) - 1
$$

**Step 3. Show $2^b \equiv 1 \pmod{2^b - 1}$.** This is immediate:

$$
2^b - 1 \equiv 0 \pmod{2^b - 1} \quad \Longrightarrow \quad 2^b \equiv 1 \pmod{2^b - 1}
$$

Hence any positive power of $2^b$ is also congruent to $1$:

$$
2^{qb} = \left(2^b\right)^q \equiv 1^q = 1 \pmod{2^b - 1}
$$

**Step 4. Substitute.**

$$
2^a - 1 \equiv 2^r \times 1 - 1 = 2^r - 1 \pmod{2^b - 1}
$$

Since $r = a \bmod b$:

$$\boxed{(2^a - 1) \bmod (2^b - 1) \equiv 2^{a \bmod b} - 1}$$

**Step 5. The residue really is the least one.** Since $0 \le r < b$ we have
$0 \le 2^r - 1 < 2^b - 1$, so $2^r - 1$ is the actual remainder and not merely a
congruent value. This is what makes the statement an equality of remainders rather
than only a congruence.

> [!info] Worked cases
> | $a$ | $b$ | $(2^a-1) \bmod (2^b-1)$ | $2^{a \bmod b} - 1$ |
> | --: | --: | --: | --: |
> | 13 | 5 | 7 | 7 |
> | 10 | 3 | 1 | 1 |
> | 20 | 6 | 3 | 3 |
> | 9 | 4 | 1 | 1 |
> | 7 | 7 | 0 | 0 |
>
> The identity was checked directly for every pair with $1 \le a \le 29$ and
> $1 \le b \le 11$, with no counterexample. The $a = b$ row is the boundary case
> worth noting: $a \bmod b = 0$ and $2^0 - 1 = 0$, which is correct since
> $2^b - 1$ divides itself.

> [!note] The general result, and why it matters
> Nothing above used anything specific to the base $2$. The identical proof works
> for any base $c$:
> $(c^a - 1) \bmod (c^b - 1) \equiv c^{a \bmod b} - 1$.
>
> This is the standard trick for simplifying large modular exponentiations, and it
> is why $3^{644} \bmod 645$ in part (b) collapses so cheaply whenever the modulus
> happens to have the form $c^k - 1$. $645$ is not of that form, which is exactly
> why (b) needs repeated squaring instead.

---

---

**Also asked here.**

- *2022 Q.8(d)* is the same question as [[DM-6.3_Pigeonhole_Principle|DM-6.3]], which is written in `DM-6.3`.
- *2023 Q.7(c)* is the same question as [[DM-5.2_Prime_Numbers|DM-5.2]], which is written in `DM-5.2`.

---
