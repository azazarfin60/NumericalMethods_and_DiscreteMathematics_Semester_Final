---
title: "DM-5.8 · Number Bases & Binary Arithmetic"
tags:
  - numerical-methods
  - discrete-mathematics
  - topicwise
---



[🏠 Subtopic Index](00_Index.md) | [← Prev: DM-5.7 Chinese Remainder Theorem](DM-5.7_Chinese_Remainder_Theorem.md) | [Next: DM-5.9 Number-Theoretic Proofs →](DM-5.9_Number_Theoretic_Proofs.md)

---

# DM-5.8 · Number Bases & Binary Arithmetic

Every block below is copied from `../answers_exam_style/`, which is the
only place an answer is authored. A number here is the same number, character
for character, as the one it came from.


### [2023 Q.7(b)]

**Question.** Add $a = (1110)_2$ and $b = (1011)_2$.

**Solution.**

**Method 1, positional value.**

$$
(1110)_2 = 1(2^3) + 1(2^2) + 1(2^1) + 0(2^0) = 8 + 4 + 2 + 0 = 14
$$

$$
(1011)_2 = 1(2^3) + 0(2^2) + 1(2^1) + 1(2^0) = 8 + 0 + 2 + 1 = 11
$$

$$
14 + 11 = 25
$$

Convert back: $25 = 16 + 8 + 1 = (11001)_2$.

**Method 2, binary addition, column by column.**

| Column | $2^4$ | $2^3$ | $2^2$ | $2^1$ | $2^0$ |
| :-- | :-: | :-: | :-: | :-: | :-: |
| **Carry row** | 1 | 1 | 1 | 0 | - |
| $a$ | 0 | 1 | 1 | 1 | 0 |
| $b$ | 0 | 1 | 0 | 1 | 1 |
| **Sum** | **1** | **1** | **0** | **0** | **1** |

Working right to left:

- $2^0$: $0 + 1 = 1$, write 1, carry 0
- $2^1$: $1 + 1 = 2$, write 0, carry 1
- $2^2$: $1 + 0 + 1 = 2$, write 0, carry 1
- $2^3$: $1 + 1 + 1 = 3$, write 1, carry 1 into $2^4$

$$
\boxed{(1110)_2 + (1011)_2 = (11001)_2 = 25_{10}}
$$

> [!info] Check
> Expand the result back to base 10:
> $(11001)_2 = 1(2^4) + 1(2^3) + 0(2^2) + 0(2^1) + 1(2^0) = 16 + 8 + 0 + 0 + 1 = 25$ ✓
> which matches $14 + 11 = 25$.
>
> Both methods agree on 25. Note that $2^4$ appears, so the sum needs five bits:
> $14 + 11 = 25 > 15 = (1111)_2$, the largest four-bit value. This is overflow
> in four-bit arithmetic, so the result must be stored in five bits.

> [!warning] Carries are the only part that needs care
> The addition itself is trivial; the carries are where slips happen. Working
> right to left:
> $2^0$: $0 + 1 = 1$, write 1, **carry 0**.
> $2^1$: $1 + 1 = 2$, write 0, **carry 1**.
> $2^2$: $1 + 0 + 1 = 2$, write 0, **carry 1**.
> $2^3$: $1 + 1 + 1 = 3$, write 1, **carry 1** into $2^4$.
> Forgetting to add the incoming carry into the next column is the classic slip,
> and it is the only place where this problem can go wrong.

---

[🏠 Subtopic Index](00_Index.md) | [← Prev: DM-5.7 Chinese Remainder Theorem](DM-5.7_Chinese_Remainder_Theorem.md) | [Next: DM-5.9 Number-Theoretic Proofs →](DM-5.9_Number_Theoretic_Proofs.md)
