---
title: "DM-5.5 · Modular Exponentiation"
tags:
  - numerical-methods
  - discrete-mathematics
  - topicwise
---

# DM-5.5 · Modular Exponentiation

Every block below is copied from `../answers_exam_style/`, which is the
only place an answer is authored. A number here is the same number, character
for character, as the one it came from.


### [2022 Q.7(b), 2024 Q.8(b)]

**Appeared in:** 2022 Q.7(b), 2024 Q.8(b)

**Question.** Solve $3^{644} \bmod 645$ using a well-known algorithm.

**Solution.**

The well-known algorithm is **repeated squaring**.

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

$$
\boxed{3^{644} \bmod 645 = 36}
$$

> [!info] Check by an independent route
> Factor $645 = 3 \times 5 \times 43$ and apply the Chinese remainder theorem.
>
> | Modulus | Result | Working |
> | :-- | --: | :-- |
> | $3$ | 0 | $3^{644}$ is a multiple of 3 |
> | $5$ | 1 | $3^4 \equiv 1$ and $644 = 4(161)$ |
> | $43$ | 36 | $\phi(43) = 42$, $644 = 42(15)+14$, so $3^{644} \equiv 3^{14} = 3^8 \cdot 3^4 \cdot 3^2 \equiv 25 \times 38 \times 9 \equiv 36$ |
>
> Checking $36$: $36 \bmod 3 = 0$ ✓, $36 \bmod 5 = 1$ ✓, $36 \bmod 43 = 36$ ✓.
> The repeated-squaring result was also produced independently by a direct
> modular exponentiation routine, which returned 36.

---
