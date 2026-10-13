---
title: "DM-5.5 · Modular Exponentiation"
tags:
  - numerical-methods
  - discrete-mathematics
  - topicwise
---


[🏠 Subtopic Index](00_Index.md) | [← Prev: DM-5.4 Modular Arithmetic & Congruence](DM-5.4_Modular_Arithmetic_and_Congruence.md) | [Next: DM-5.7 Chinese Remainder Theorem →](DM-5.7_Chinese_Remainder_Theorem.md)

---

# DM-5.5 · Modular Exponentiation

Every block below is copied from `../answers_explanation/`. The reasoning
is written once, in the year-wise file, and is not restated here.


### [2022 Q.7(b), 2024 Q.8(b)]

**Appeared in:** 2022 Q.7(b), 2024 Q.8(b)

**Question.** Solve $3^{644} \bmod 645$ using a well-known algorithm.

*[Marks: 03, CO: 3]*

**Solution.**

The well-known algorithm is **repeated squaring**, also called the
square-and-multiply method. It exploits $x^{2k} = (x^k)^2$, so each squaring
roughly doubles the exponent covered while the numbers stay small.

**Step 1. Binary expansion of the exponent.**

$$
644 = 512 + 128 + 4 = (1010000100)_2
$$

**Step 2. Square repeatedly, reducing modulo 645 at every step.**

$$
3^1 = 3
$$

$$
3^2 = 9
$$

$$
3^4 = 9^2 = 81
$$

$$
3^8 = 81^2 = 6561 = 645(10) + 111 \equiv 111
$$

$$
3^{16} = 111^2 = 12321 = 645(19) + 66 \equiv 66
$$

$$
3^{32} = 66^2 = 4356 = 645(6) + 486 \equiv 486
$$

$$
3^{64} = 486^2 = 236196 = 645(366) + 126 \equiv 126
$$

$$
3^{128} = 126^2 = 15876 = 645(24) + 396 \equiv 396
$$

$$
3^{256} = 396^2 = 156816 = 645(243) + 81 \equiv 81
$$

$$
3^{512} = 81^2 = 6561 \equiv 111
$$

**Step 3. Multiply the powers named by the set bits**, which are
$2^9 = 512$, $2^7 = 128$ and $2^2 = 4$:

$$
3^{644} \equiv 3^{512} \cdot 3^{128} \cdot 3^4
$$

$$
= 111 \times 396 \times 81
$$

$$
111 \times 396 = 43956 = 645(68) + 96 \equiv 96
$$

$$
96 \times 81 = 7776 = 645(12) + 36 \equiv 36
$$

$$\boxed{3^{644} \bmod 645 = 36}$$

> [!info] A completely different route, by the Chinese remainder theorem
> Factor $645 = 3 \times 5 \times 43$ and work modulo each prime:
>
> | Modulus | Result | Working |
> | :-- | :-- | :-- |
> | $3$ | 0 | $3^{644}$ is a multiple of 3 |
> | $5$ | 1 | $3^4 \equiv 1$ and $644 = 4(161)$ |
> | $43$ | 36 | $\phi(43) = 42$, $644 = 42(15)+14$, so $3^{644} \equiv 3^{14} = 3^8 \cdot 3^4 \cdot 3^2 \equiv 25 \times 38 \times 9 \equiv 36$ |
>
> Checking $36$: $36 \bmod 3 = 0$ ✓, $36 \bmod 5 = 1$ ✓, $36 \bmod 43 = 36$ ✓.
> Both routes give $36$, which is a genuine confirmation because they share no
> intermediate arithmetic.

> [!warning] Two traps in this computation
> **Do not let the residues grow.** Reducing after every squaring is what keeps
> the largest intermediate at $486^2 = 236196$. Squaring without reducing reaches
> $3^{644}$ with about $307$ digits, which is not wrong so much as pointless.
>
> **$3^{256} \equiv 81$ is not a typo.** The sequence is periodic in a way that
> looks wrong at first glance, and $81 = 3^4$ is exactly what makes $3^{512}$
> come out equal to $3^8$. If one of these entries surprises you, recompute it
> rather than adjusting it to look tidier.

> [!note] Which algorithm the question means
> "A well-known algorithm" for modular exponentiation is repeated squaring.
> **Fermat's little theorem** would also work, via
> $3^{644} = 3^{\phi(645) + 164}$ with $\phi(645) = 268$, but the modulus is not
> prime, so the theorem only applies to each prime factor separately, which is
> the CRT route above rather than a single reduction.
>
> Repeated squaring is the right answer to the question as asked because it
> applies to any modulus, prime or not, and takes about $\log_2 644 = 10$
> squarings.

---

[🏠 Subtopic Index](00_Index.md) | [← Prev: DM-5.4 Modular Arithmetic & Congruence](DM-5.4_Modular_Arithmetic_and_Congruence.md) | [Next: DM-5.7 Chinese Remainder Theorem →](DM-5.7_Chinese_Remainder_Theorem.md)
