---
title: "DM-5.4 · Modular Arithmetic & Congruence"
tags:
  - numerical-methods
  - discrete-mathematics
  - topicwise
---



[🏠 Subtopic Index](00_Index.md) | [← Prev: DM-5.3 GCD, LCM & Euclidean Algorithm](DM-5.3_GCD_LCM_and_Euclidean_Algorithm.md) | [Next: DM-5.5 Modular Exponentiation →](DM-5.5_Modular_Exponentiation.md)

---

# DM-5.4 · Modular Arithmetic & Congruence

Every block below is copied from `../answers_explanation/`. The reasoning
is written once, in the year-wise file, and is not restated here.


### [2022 Q.7(a), 2024 Q.8(a)]

**Appeared in:** 2022 Q.7(a), 2024 Q.8(a)

**Question.** Suppose that $a$ and $b$ are integers, $a \equiv 11 \pmod{19}$ and $b \equiv 3 \pmod{19}$. Find the integer $c$ with $0 \le c \le 18$ such that (i) $c \equiv 7a + 3b \pmod{19}$, (ii) $c \equiv a^3 + 4b^3 \pmod{19}$.

*[Marks: 03, CO: 2]*

**Solution.**

Congruence behaves like equality under addition, subtraction and
multiplication, so every part is computed by substituting the residues and
reducing at the end.

**(i) $c \equiv 7a + 3b \pmod{19}$**

$$
7a + 3b \equiv 7(11) + 3(3) = 77 + 9 = 86 \pmod{19}
$$

Divide: $86 = 19(4) + 10$.

$$\boxed{c = 10}$$

**(ii) $c \equiv a^3 + 4b^3 \pmod{19}$**

Reduce the powers first, which keeps the numbers small:

$$
a^2 \equiv 11^2 = 121 = 19(6) + 7 \equiv 7 \pmod{19}
$$

$$
a^3 \equiv 7 \times 11 = 77 = 19(4) + 1 \equiv 1 \pmod{19}
$$

$$
b^3 \equiv 3^3 = 27 = 19(1) + 8 \equiv 8 \pmod{19}
$$

$$
c \equiv 1 + 4(8) = 1 + 32 = 33 = 19(1) + 14 \pmod{19}
$$

$$\boxed{c = 14}$$

> [!info] Direct substitution confirms both
> **Part (i).** $7(11) + 3(3) = 86$, and $86 = 19(4) + 10$, so $c = 10$.
>
> **Part (ii).** $11^3 + 4 \cdot 3^3 = 1331 + 108 = 1439$, and
> $1439 = 19(75) + 14$, so $c = 14$.
>
> Both remainders satisfy $0 \le c \le 18$, which the question requires. Note that
> reducing the powers in (ii) is a convenience, not a requirement: the direct
> route gives the same answer, which is the point of the check.

> [!warning] Write the question's expression into the working before computing anything
> With $a \equiv 11$ and $b \equiv 3$ the products $ab$ and the sums $a + b$ also
> reduce to $14$, which is part (ii)'s answer. A draft that computes $ab$ and
> $a+b$ instead of $7a + 3b$ and $a^3 + 4b^3$ therefore produces a part (ii) that
> looks right and a part (i) that is wrong.
>
> The safeguard is procedural rather than mathematical: write
> "$7a + 3b \equiv 7(11) + 3(3) = 86$" on the page, not just "part (i): 14". Once
> the expression is visible, a substituted expression cannot pass unnoticed,
> because it is visibly not the one that was asked for.

---

### [2023 Q.7(a)]

**Question.** Suppose that $a$ and $b$ are integers, $a \equiv 4 \pmod{13}$, and $b \equiv 9 \pmod{13}$. Find the integer $c$ with $0 \le c \le 12$ such that (i) $c = 2a + 3b \pmod{13}$, (ii) $c = a^2 + b^2 \pmod{13}$.

*[Marks: 04, CO: 2]*

**Solution.**

Work entirely with the residues, then reduce to $0 \le c \le 12$. Congruence
arithmetic is exactly real arithmetic modulo the modulus, so substituting the
residues for $a$ and $b$ is valid from the start and keeps every intermediate
number small.

**(i) $c \equiv 2a + 3b \pmod{13}$**

$$
c \equiv 2(4) + 3(9) = 8 + 27 = 35 \pmod{13}
$$

Divide: $35 = 13(2) + 9$.

$$
\boxed{c = 9}
$$

**(ii) $c \equiv a^2 + b^2 \pmod{13}$**

$$
c \equiv 4^2 + 9^2 = 16 + 81 = 97 \pmod{13}
$$

Divide: $97 = 13(7) + 6$.

$$
\boxed{c = 6}
$$

> [!info] Two independent confirmations
> **(i)** $13 \times 2 = 26$ and $26 + 9 = 35$.
> **(ii)** $13 \times 7 = 91$ and $91 + 6 = 97$.
>
> Both remainders satisfy $0 \le c \le 12$ as the question requires.
>
> For (ii) there is a genuinely shorter route. Squaring reduced residues is safe
> because $16 \equiv 3 \pmod{13}$ and $81 \equiv 3 \pmod{13}$, so
> $c \equiv 3 + 3 = 6$. The same answer from much smaller numbers, which confirms
> the first computation.

> [!note] Reducing early keeps the numbers small
> Write $b \equiv 9$, then $b^2 \equiv 3$, then $c \equiv 3 + 3 = 6$. That route
> never produces a number above 9. Direct squaring gave 97. Same answer, and the
> first route cannot overflow a fixed-width register, which is not a cosmetic
> concern when the modulus is large or you are working by hand under time
> pressure.
>
> The reduction step to write $\begin{pmatrix} 1 \\ 0 \\ 1 \end{pmatrix}$, that is
> $35$ as $13(2) + 9$, must be shown. The answer is not "35 mod 13"; the answer is
> the remainder itself.

---

[🏠 Subtopic Index](00_Index.md) | [← Prev: DM-5.3 GCD, LCM & Euclidean Algorithm](DM-5.3_GCD_LCM_and_Euclidean_Algorithm.md) | [Next: DM-5.5 Modular Exponentiation →](DM-5.5_Modular_Exponentiation.md)
