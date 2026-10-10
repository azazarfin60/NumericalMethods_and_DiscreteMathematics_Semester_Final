[← Previous: DM-5.3 GCD & Euclidean Algorithm](DM-5.3_GCD_and_Euclidean.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: DM-5.5 Modular Exponentiation →](DM-5.5_Modular_Exponentiation.md)

---

# DM-5.4: Modular Arithmetic & Congruence

> 🔴 **Priority:** Critical | **Tested:** 3/3 papers (2022, 2023, 2024) | **Typical marks:** 3 to 4

## What This Is (and Why It Matters)

Modular arithmetic is often called "clock arithmetic". On a standard 12-hour clock, if the time is 9 o'clock and you wait 5 hours, the clock does not read 14; it wraps around and reads 2. You performed arithmetic modulo 12: $(9 + 5) \bmod 12 = 2$.

This is the single most tested subtopic in Discrete Mathematics at RUET. It has appeared on **every single paper** since Section B was created.

Even better, examiners ask the exact same style of question every time: they give you the residues of two variables $a$ and $b$ modulo some number $m$, and ask you to find the remainder of a linear expression (like $7a + 3b$) and a polynomial expression (like $a^3 + 4b^3$).

The golden rule to solve this entire topic: **replace variables with their residues immediately, and reduce intermediate numbers after every operation.** If you do this, you will never have to deal with large numbers.

---

## 📝 Key Definitions

> **Congruence Modulo $m$:** "If $a$ and $b$ are integers and $m$ is a positive integer, then $a$ is **congruent to** $b$ **modulo** $m$ if $m$ divides $a - b$. We use the notation $a \equiv b \pmod m$ to indicate that $a$ is congruent to $b$ modulo $m$." -- Rosen, §4.1, Definition 3
>
> **In simple words:** Two numbers are congruent modulo $m$ if they leave the exact same remainder when divided by $m$, which means their difference is an exact multiple of $m$.

> **Mod and Div Functions:** "Let $a$ be an integer and $d$ a positive integer. We denote by $a \text{ div } d$ the quotient and by $a \bmod d$ the remainder obtained when $a$ is divided by $d$." -- Rosen, §4.1, Definition 2
>
> **In simple words:** $a \text{ div } d$ is the whole number quotient $\lfloor a/d \rfloor$, and $a \bmod d$ is the leftover remainder in the range $[0, d-1]$.

> **Compatibility with Addition and Multiplication:** "Let $m$ be a positive integer. If $a \equiv b \pmod m$ and $c \equiv d \pmod m$, then $a + c \equiv b + d \pmod m$ and $ac \equiv bd \pmod m$." -- Rosen, §4.1, Theorem 5
>
> **In simple words:** You can add or multiply congruences just like ordinary equations. Whenever you see a variable in an expression, you are legally allowed to swap it for its remainder modulo $m$.

> **Modular Arithmetic on $\mathbb{Z}_m$:** "The operations $+_m$ and $\cdot_m$ on $\mathbb{Z}_m = \{0, 1, \dots, m-1\}$ defined by $a +_m b = (a + b) \bmod m$ and $a \cdot_m b = (a \cdot b) \bmod m$ are called **modular addition** and **modular multiplication**." -- Rosen, §4.1, Definition 4
>
> **In simple words:** Arithmetic where every calculation is immediately folded back into the range from $0$ to $m-1$ by taking the remainder.

---

## The Core Idea

### The Division Algorithm Schematic

Every integer splits cleanly into a quotient and a non-negative remainder:

![Long division schematic marking the quotient, dividend, divisor and remainder](../diagrams/dm5_division_algorithm_schematic.jpg)

When dividing $27$ by $4$:
- $27 = 4 \times 6 + 3$
- The quotient is $q = 27 \text{ div } 4 = 6$
- The remainder is $r = 27 \bmod 4 = 3$, with $0 \le 3 < 4$

### What Congruence Really Means

Writing $a \equiv b \pmod m$ states that $m$ divides $a - b$:

$$
a \equiv b \pmod m \iff a - b = km \quad \text{for some integer } k
$$

This means $a = b + km$. All integers that share the same remainder form a **congruence class**.

For modulus $m = 19$:
- The numbers $11, 30, 49, 68, 87, 106$ all belong to the exact same equivalence class modulo 19 because each leaves a remainder of $11$.
- Any one of these numbers can stand in for any other in addition and multiplication.

> [!WARNING] Congruence is Not Ordinary Equality
> Writing $a \equiv b \pmod{19}$ does **not** mean $a = b$. It means they differ by a multiple of 19. Never write $86 = 10$; write $86 \equiv 10 \pmod{19}$.

### The Three Theorems That Solve Every Exam Problem

By Theorem 5 from Rosen §4.1, modular arithmetic preserves algebraic operations:

1. **Property 1: Addition compatibility**
   $$
   a \equiv b \pmod m \quad \text{and} \quad c \equiv d \pmod m \implies a + c \equiv b + d \pmod m
   $$
2. **Property 2: Multiplication compatibility**
   $$
   a \equiv b \pmod m \quad \text{and} \quad c \equiv d \pmod m \implies ac \equiv bd \pmod m
   $$
3. **Property 3: Exponent and intermediate reduction**
   $$
   x \equiv r \pmod m \implies x^k \equiv r^k \pmod m \quad \text{for all integers } k \ge 1
   $$

### The Step-by-Step Problem Solving Algorithm

Whenever an exam gives you $a \equiv r_a \pmod m$ and $b \equiv r_b \pmod m$ and asks for $c \equiv f(a, b) \pmod m$ with $0 \le c \le m - 1$:

1. **Substitute:** Replace every instance of $a$ with $r_a$ and $b$ with $r_b$.
2. **Reduce early:** If you need to calculate powers (like $11^3$), compute $11^2 = 121 \equiv 7 \pmod{19}$ first. Then multiply $7 \times 11 = 77 \equiv 1 \pmod{19}$. Never calculate $11^3 = 1331$ by hand!
3. **Combine:** Sum and multiply the small reduced numbers.
4. **Final remainder:** Divide your intermediate result by $m$ and report the unique remainder $c$ that satisfies $0 \le c \le m - 1$.

---

### Reference: Quick Sight Reductions

| Modulus $m$ | Helpful properties & powers | Example |
| :--: | :-- | :-- |
| 3 | $a \in \{0, 1, 2\}$, $3 \equiv 0$ | $8 \equiv 2 \pmod 3$ |
| 4 | $2^2 \equiv 0$, $3 \equiv -1 \pmod 4$ | $3^2 \equiv (-1)^2 = 1 \pmod 4$ |
| 5 | $4 \equiv -1$, $2^4 \equiv 16 \equiv 1$ | $4^3 \equiv (-1)^3 = -1 \equiv 4 \pmod 5$ |
| 13 | $3^3 = 27 \equiv 1$, $9 \equiv -4$ | $9^2 = 81 \equiv 3 \pmod{13}$ |
| 19 | $11^3 \equiv 1$, $7^3 \equiv 1$ | $77 = 19(4) + 1 \equiv 1 \pmod{19}$ |
| 43 | Prime, so $a^{42} \equiv 1$ for $43 \nmid a$ | Fermat's theorem base |

---

## 🔧 Worked Examples

### Worked Example 1: 2022 Q.7(a) & 2024 Q.8(a)

> **From:** 2022 Q.7(a) and 2024 Q.8(a) -- [Marks: 03 in 2022, 04 in 2024]

**Question.** Suppose that $a$ and $b$ are integers, $a \equiv 11 \pmod{19}$ and $b \equiv 3 \pmod{19}$. Find the integer $c$ with $0 \le c \le 18$ such that:  
(i) $c \equiv 7a + 3b \pmod{19}$  
(ii) $c \equiv a^3 + 4b^3 \pmod{19}$

**Solution.**

Work directly with the residues modulo 19:

**(i) Evaluation of $c \equiv 7a + 3b \pmod{19}$**

Substitute $a \equiv 11$ and $b \equiv 3$:

$$
c \equiv 7(11) + 3(3) = 77 + 9 = 86 \pmod{19}
$$

Divide 86 by 19:

$$
86 = 19(4) + 10
$$

The remainder is 10, which satisfies $0 \le 10 \le 18$:

$$
\boxed{c = 10}
$$

**(ii) Evaluation of $c \equiv a^3 + 4b^3 \pmod{19}$**

Reduce the powers in stages to avoid large numbers:

$$
a^2 \equiv 11^2 = 121 = 19(6) + 7 \equiv 7 \pmod{19}
$$

$$
a^3 \equiv 7 \times 11 = 77 = 19(4) + 1 \equiv 1 \pmod{19}
$$

$$
b^3 \equiv 3^3 = 27 = 19(1) + 8 \equiv 8 \pmod{19}
$$

Now substitute the reduced powers into the expression:

$$
c \equiv a^3 + 4b^3 \equiv 1 + 4(8) = 1 + 32 = 33 \pmod{19}
$$

Divide 33 by 19:

$$
33 = 19(1) + 14
$$

The remainder is 14, which satisfies $0 \le 14 \le 18$:

$$
\boxed{c = 14}
$$

> [!NOTE] Check via direct substitution
> $11^3 + 4(3^3) = 1331 + 4(27) = 1331 + 108 = 1439$.  
> Dividing: $1439 = 19 \times 75 + 14$.  
> The result matches $c = 14$ exactly, but early reduction required no large arithmetic.

---

### Worked Example 2: 2023 Q.7(a)

> **From:** 2023 Q.7(a) -- [Marks: 04]

**Question.** Suppose that $a$ and $b$ are integers, $a \equiv 4 \pmod{13}$, and $b \equiv 9 \pmod{13}$. Find the integer $c$ with $0 \le c \le 12$ such that:  
(i) $c = 2a + 3b \pmod{13}$  
(ii) $c = a^2 + b^2 \pmod{13}$

**Solution.**

Substitute the given residues modulo 13:

**(i) Evaluation of $c \equiv 2a + 3b \pmod{13}$**

Substitute $a \equiv 4$ and $b \equiv 9$:

$$
c \equiv 2(4) + 3(9) = 8 + 27 = 35 \pmod{13}
$$

Divide 35 by 13:

$$
35 = 13(2) + 9
$$

The remainder is 9, which satisfies $0 \le 9 \le 12$:

$$
\boxed{c = 9}
$$

**(ii) Evaluation of $c \equiv a^2 + b^2 \pmod{13}$**

Substitute $a \equiv 4$ and $b \equiv 9$:

$$
c \equiv 4^2 + 9^2 = 16 + 81 = 97 \pmod{13}
$$

Divide 97 by 13:

$$
97 = 13(7) + 6
$$

The remainder is 6, which satisfies $0 \le 6 \le 12$:

$$
\boxed{c = 6}
$$

> [!NOTE] Verification by early reduction
> $4^2 = 16 = 13(1) + 3 \equiv 3 \pmod{13}$.  
> $9 \equiv -4 \implies 9^2 \equiv (-4)^2 = 16 \equiv 3 \pmod{13}$.  
> Then $c \equiv 3 + 3 = 6$. The answer matches $\boxed{c = 6}$ without exceeding single-digit numbers.

---

## ⚡ Common Traps & Exam Tips

> [!WARNING] Common Trap: Forgetting the Final Reduction
> Students frequently write $c = 86$ or $c = 33$ or $c = 97$ and move to the next question. The prompt specifically instructs: "Find the integer $c$ with $0 \le c \le m - 1$." Leaving an unreduced number loses easy marks.

> [!TIP] Write Out the Division Line Explicitly
> Always write the formal division line, such as $86 = 19(4) + 10$. This proves to the examiner that you understand the Division Algorithm and did not guess the remainder.

---

[← Previous: DM-5.3 GCD & Euclidean Algorithm](DM-5.3_GCD_and_Euclidean.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: DM-5.5 Modular Exponentiation →](DM-5.5_Modular_Exponentiation.md)
