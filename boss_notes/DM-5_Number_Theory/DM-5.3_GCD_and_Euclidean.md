[← Previous: DM-5.2 Prime Numbers](DM-5.2_Prime_Numbers.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: DM-5.4 Modular Arithmetic →](DM-5.4_Modular_Arithmetic.md)

---

# DM-5.3: GCD, LCM & Euclidean Algorithm

> 🟠 ⚠️ **Priority:** Secondary (Danger Zone) | **Tested:** 1/3 papers (2022 Q.7(c)) | **Typical marks:** 2 to 3

## What This Is (and Why It Matters)

Finding the greatest common divisor ($\gcd$) of small numbers is something you can do by sight or prime factorization. For instance, between 12 and 18, the greatest common divisor is 6. But when numbers reach hundreds or thousands, prime factorization becomes painfully slow.

Over two thousand years ago, Euclid invented an algorithm that finds the greatest common divisor using only division with remainder, without factoring either number.

The **Extended Euclidean Algorithm** goes one critical step further: it runs the divisions in reverse to express the gcd as an integer combination of the two original inputs:

$$
sa + tb = \gcd(a, b)
$$

This equation is called **Bézout's identity**, and the multipliers $s$ and $t$ are **Bézout coefficients**. These coefficients are the exact mechanism used to compute modular inverses in cryptography and the Chinese Remainder Theorem.

> [!WARNING] Danger Zone: Marked as Self-Study in Notes!
> In both class note sets (Fahad and Raidah), the Extended Euclidean Algorithm was tagged as **self-study**. Many students ignored it, assuming it would not be examined. In 2022 Q.7(c), the semester final asked for $\gcd(414, 662)$ using this exact extended algorithm. Master it now so you do not lose easy marks.

---

## 📝 Key Definitions

> **Greatest Common Divisor (GCD):** "Let $a$ and $b$ be integers, not both zero. The largest integer $d$ such that $d \mid a$ and $d \mid b$ is called the **greatest common divisor** of $a$ and $b$. The greatest common divisor of $a$ and $b$ is denoted by $\gcd(a, b)$." -- Rosen, §4.3, Definition 2
>
> **In simple words:** The largest positive whole number that divides into both numbers without leaving a remainder.

> **Relatively Prime (Coprime):** "The integers $a$ and $b$ are **relatively prime** if their greatest common divisor is 1." -- Rosen, §4.3, Definition 3
>
> **In simple words:** Two numbers are relatively prime if they share no common factor other than 1. For example, 9 and 28 are relatively prime because $\gcd(9, 28) = 1$, even though neither number is prime on its own.

> **Least Common Multiple (LCM):** "The **least common multiple** of the positive integers $a$ and $b$ is the smallest positive integer that is divisible by both $a$ and $b$. The least common multiple of $a$ and $b$ is denoted by $\text{lcm}(a, b)$." -- Rosen, §4.3, Definition 5
>
> **In simple words:** The smallest positive number that appears in the multiplication tables of both numbers.

> **Euclidean Algorithm Property:** "Let $a = bq + r$, where $a, b, q,$ and $r$ are integers. Then $\gcd(a, b) = \gcd(b, r)$." -- Rosen, §4.3, Lemma 1
>
> **In simple words:** The greatest common divisor between two numbers is identical to the greatest common divisor between the smaller number and the remainder. This lets you swap big numbers for smaller remainders until you reach 0.

> **Bézout's Theorem and Identity:** "If $a$ and $b$ are positive integers, then there exist integers $s$ and $t$ such that $\gcd(a, b) = sa + tb$." -- Rosen, §4.3, Theorem 6
>
> **In simple words:** You can always write the greatest common divisor of two numbers as a linear combination of those two numbers using integer coefficients $s$ and $t$.

---

## The Core Idea

### Why the Euclidean Algorithm Works and Terminates

The whole algorithm is powered by one identity:

$$
a = bq + r \implies \gcd(a, b) = \gcd(b, r)
$$

**Why this is true:**
- If $d$ divides both $a$ and $b$, then $d$ divides $a - bq = r$. So $d$ is a common divisor of $b$ and $r$.
- Conversely, if $d$ divides both $b$ and $r$, then $d$ divides $bq + r = a$. So $d$ is a common divisor of $a$ and $b$.
- Since both pairs share the exact same common divisors, their greatest common divisors must be identical.

Because each remainder satisfies $0 \le r < b$, the remainders form a strictly decreasing sequence of non-negative integers:

$$
b > r_1 > r_2 > r_3 > \dots \ge 0
$$

A strictly decreasing sequence of whole numbers cannot continue forever; it must hit 0. **The last nonzero remainder right before 0 is the gcd.**

### The Ordinary Euclidean Algorithm in Action

Suppose we want $\gcd(118, 26)$. We repeatedly divide:

![Hand-written Euclidean algorithm table with columns q, a, b, r for gcd(26, 118) = 2](../diagrams/dm5_euclidean_algorithm_table.jpg)

| Step | Division equation ($a = bq + r$) | Quotient $q$ | Remainder $r$ | Next pair $(b, r)$ |
| :--: | :-- | :--: | :--: | :--: |
| 1 | $118 = 26 \times 4 + 14$ | 4 | 14 | $(26, 14)$ |
| 2 | $26 = 14 \times 1 + 12$ | 1 | 12 | $(14, 12)$ |
| 3 | $14 = 12 \times 1 + 2$ | 1 | 2 | $(12, 2)$ |
| 4 | $12 = 2 \times 6 + 0$ | 6 | 0 | Finished |

The last nonzero remainder is **2**. Therefore, $\gcd(118, 26) = 2$.

---

### The Extended Euclidean Algorithm

The ordinary algorithm gives the gcd. The extended algorithm computes integers $s$ and $t$ such that:

$$
sa + tb = \gcd(a, b)
$$

You have two reliable ways to solve this under exam conditions:

#### Route A: Back-Substitution (Fastest for Exams)
1. Run the ordinary divisions until you find the gcd.
2. Take the division equation containing the gcd and isolate it on the left.
3. Step backwards line by line, substituting each previous remainder and grouping like terms.
4. Stop when the expression contains only the original inputs $a$ and $b$.

#### Route B: Tabular Recurrence (Shishir's Method)
You can maintain the Bézout coefficients alongside each step in a table using the recurrence relations:

$$
s = s_1 - s_2 q, \qquad t = t_1 - t_2 q
$$

with starting conditions $s_1 = 1, s_2 = 0$ and $t_1 = 0, t_2 = 1$. At each subsequent row, the variables shift diagonally ($s_1 \leftarrow s_2$, $s_2 \leftarrow s$).

![Hand-written Extended Euclidean Algorithm table tracking Bezout coefficients s and t for gcd(275, 200)](../diagrams/dm5_extended_euclidean_bezout_table.jpg)

For example, tracking $\gcd(275, 200) = 25$:

| $q$ | $a$ | $b$ | $r$ | $s_1$ | $s_2$ | $s = s_1 - s_2 q$ | $t_1$ | $t_2$ | $t = t_1 - t_2 q$ |
| :--: | --: | --: | --: | --: | --: | :-- | --: | --: | :-- |
| 1 | 275 | 200 | 75 | 1 | 0 | $1 - 0(1) = 1$ | 0 | 1 | $0 - 1(1) = -1$ |
| 2 | 200 | 75 | 50 | 0 | 1 | $0 - 1(2) = -2$ | 1 | -1 | $1 - (-1)(2) = 3$ |
| 1 | 75 | 50 | 25 | 1 | -2 | $1 - (-2)(1) = 3$ | -1 | 3 | $-1 - 3(1) = -4$ |
| 2 | 50 | 25 | 0 | -2 | 3 | $-2 - 3(2) = -8$ | 3 | -4 | $3 - (-4)(2) = 11$ |
| - | **25** | 0 | - | **3** | -8 | - | **-4** | 11 | - |

Reading the row gives $\gcd(275, 200) = 25$ with $s = 3$ and $t = -4$:
$$
3(275) - 4(200) = 825 - 800 = 25
$$

---

### The LCM and the Product Identity

The product of two positive integers equals the product of their greatest common divisor and least common multiple:

$$
ab = \gcd(a, b) \cdot \text{lcm}(a, b)
$$

Rearranging gives the formula to compute $\text{lcm}(a, b)$:

$$
\text{lcm}(a, b) = \frac{ab}{\gcd(a, b)}
$$

For $a = 414$ and $b = 662$ with $\gcd = 2$:
$$
\text{lcm}(414, 662) = \frac{414 \times 662}{2} = 137{,}034
$$

---

## 🔧 Worked Example

> **From:** 2022 Q.7(c) -- [Marks: 02]

**Question.** Find the greatest common divisor of 414 and 662 using the extended Euclidian algorithm.

**Solution.**

**Step 1. Ordinary Euclidean algorithm.**  
Execute repeated divisions until the remainder is zero:

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

The last nonzero remainder is $2$.  
Therefore, $\gcd(414, 662) = 2$.

**Step 2. Extended Euclidean back-substitution.**  
Now express the remainder $2$ as a linear combination of $414$ and $662$ by working backwards through the division equations.

From the second to last line ($166 = 2 \times 82 + 2$), isolate $2$:
$$
2 = 166 - 2(82)
$$

From $248 = 1 \times 166 + 82$, substitute $82 = 248 - 166$:
$$
2 = 166 - 2(248 - 166) = 3(166) - 2(248)
$$

From $414 = 1 \times 248 + 166$, substitute $166 = 414 - 248$:
$$
2 = 3(414 - 248) - 2(248) = 3(414) - 5(248)
$$

From $662 = 1 \times 414 + 248$, substitute $248 = 662 - 414$:
$$
2 = 3(414) - 5(662 - 414) = 8(414) - 5(662)
$$

**Step 3. Numerical check.**
$$
8(414) - 5(662) = 3312 - 3310 = 2
$$

Both the gcd and the Bézout combination are verified:

$$
\boxed{\gcd(414, 662) = 2, \qquad 8(414) - 5(662) = 2}
$$

---

## ⚡ Common Traps & Exam Tips

> [!WARNING] Common Trap: Forgetting the Bézout Coefficients
> If the exam prompt specifically says "using the **extended** Euclidean algorithm", providing only $\gcd = 2$ will cost you half the marks. You must provide the Bézout combination $sa + tb = \gcd(a, b)$!

> [!TIP] The Five-Second Sanity Check
> After finding $s$ and $t$, always multiply them out: $8 \times 414 - 5 \times 662 = 3312 - 3310 = 2$.
> If the arithmetic does not yield your gcd exactly, you made a sign slip during back-substitution.

---

[← Previous: DM-5.2 Prime Numbers](DM-5.2_Prime_Numbers.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: DM-5.4 Modular Arithmetic →](DM-5.4_Modular_Arithmetic.md)
