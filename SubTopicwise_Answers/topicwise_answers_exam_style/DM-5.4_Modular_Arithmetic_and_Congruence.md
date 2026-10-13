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

Every block below is copied from `../answers_exam_style/`, which is the
only place an answer is authored. A number here is the same number, character
for character, as the one it came from.


### [2022 Q.7(a), 2024 Q.8(a)]

**Appeared in:** 2022 Q.7(a), 2024 Q.8(a)

**Question.** Suppose that $a$ and $b$ are integers, $a \equiv 11 \pmod{19}$ and $b \equiv 3 \pmod{19}$. Find the integer $c$ with $0 \le c \le 18$ such that (i) $c \equiv 7a + 3b \pmod{19}$, (ii) $c \equiv a^3 + 4b^3 \pmod{19}$.

**Solution.**

Work with the residues, then reduce to $0 \le c \le 18$.

**(i) $c \equiv 7a + 3b \pmod{19}$**

$$
c \equiv 7(11) + 3(3) = 77 + 9 = 86 \pmod{19}
$$

Divide: $86 = 19(4) + 10$.

$$
\boxed{c = 10}
$$

**(ii) $c \equiv a^3 + 4b^3 \pmod{19}$**

Reduce the powers first to keep the numbers small:

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

$$
\boxed{c = 14}
$$

> [!info] Check by an independent route
> **Direct substitution.** $11^3 + 4 \cdot 3^3 = 1331 + 108 = 1439$, and
> $1439 = 19(75) + 14$, giving $c = 14$.
> **Part (i) direct.** $86 = 19(4) + 10$, giving $c = 10$.
> Both agree, and every remainder satisfies $0 \le c \le 18$.

---

### [2023 Q.7(a)]

**Question.** Suppose that $a$ and $b$ are integers, $a \equiv 4 \pmod{13}$, and $b \equiv 9 \pmod{13}$. Find the integer $c$ with $0 \le c \le 12$ such that (i) $c = 2a + 3b \pmod{13}$, (ii) $c = a^2 + b^2 \pmod{13}$.

**Solution.**

Work entirely with the residues, then reduce to $0 \le c \le 12$.

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

> [!info] Check
> **(i)** $13 \times 2 = 26$ and $26 + 9 = 35$ ✓
> **(ii)** $13 \times 7 = 91$ and $91 + 6 = 97$ ✓
> Both remainders satisfy $0 \le c \le 12$ as the question requires.
>
> Squaring reduced residues is safe here, since $16 \equiv 3 \pmod{13}$ and
> $81 \equiv 3 \pmod{13}$, so $c \equiv 3 + 3 = 6$ ✓. The same answer from much
> smaller numbers confirms the first computation.

> [!note] Reducing early keeps the numbers small
> Writing $b \equiv 9$, then $b^2 \equiv 3$, then $c \equiv 3 + 3 = 6$, never
> produces a number above 9. Direct squaring gave 97. Same answer, and the first
> route cannot overflow a fixed-width register.

---

[🏠 Subtopic Index](00_Index.md) | [← Prev: DM-5.3 GCD, LCM & Euclidean Algorithm](DM-5.3_GCD_LCM_and_Euclidean_Algorithm.md) | [Next: DM-5.5 Modular Exponentiation →](DM-5.5_Modular_Exponentiation.md)
