[← Previous: DM-5.8 Number Bases](DM-5.8_Number_Bases.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: DM-6.1 Sum and Product Rules →](../DM-6_Counting/DM-6.1_Sum_and_Product_Rules.md)

---

# DM-5.9: Number-Theoretic Proofs

> 🟠 **Priority:** Secondary | **Tested:** 2/3 papers (2022 Q.7(d), 2023 Q.7(c)) | **Typical marks:** 2 to 3

## What This Is (and Why It Matters)

Students often feel anxious about mathematical proofs because they think a proof requires a flash of genius. In number theory, that is not true. Number-theoretic proofs in RUET exams follow strict, repeatable structural blueprints.

In 2022 Q.7(d), examiners asked students to prove the identity:

$$
(2^a - 1) \bmod (2^b - 1) \equiv 2^{a \bmod b} - 1
$$

This identity looks intimidating at first glance, but it unravels cleanly in five logical steps using only the Division Algorithm and basic modular arithmetic. Master this five-step template, and you will be able to handle any modular identity proof on exam day.

---

## 📝 Key Definitions

> **The Division Algorithm in Exponents:** "Let $a$ and $b$ be positive integers. Then there exist unique integers $q$ and $r$ such that $a = qb + r$ with $0 \leq r < b$." -- Rosen, §4.1, Theorem 2
>
> **In simple words:** You can always break an exponent $a$ down into a whole multiple of another exponent $b$, plus a remainder $r$ that is strictly smaller than $b$.

> **Mersenne Number and Prime:** "A **Mersenne number** is a number of the form $M_n = 2^n - 1$, where $n$ is a positive integer. If $M_p = 2^p - 1$ is prime (where $p$ is prime), it is called a **Mersenne prime**." -- Shishir Notes §5.1; Rosen §4.3
>
> **In simple words:** Numbers shaped like one less than a power of 2 ($3, 7, 31, 127, \dots$). The moduli in the 2022 proof are Mersenne numbers.

> **Least Non-Negative Residue:** "The remainder $r = a \bmod m$ satisfies $0 \leq r < m$. It is the unique representative of the congruence class of $a$ modulo $m$ in the set $\{0, 1, \dots, m-1\}$." -- Rosen, §4.1
>
> **In simple words:** A congruence only tells you that two numbers differ by a multiple of the modulus. To prove an expression is the actual *remainder* (mod operator), you must prove it lies between 0 and the modulus minus 1.

---

## The Core Idea

### The Five-Step Template for Exponent Modular Proofs

Whenever you encounter a proof asking to find or simplify $(c^a - 1) \bmod (c^b - 1)$, execute these five steps in order:

1. **Step 1: Divide the exponents.**  
   Apply the Division Algorithm to $a$ and $b$:
   $$
   a = qb + r \quad \text{where } q = \lfloor a/b \rfloor \ge 0 \text{ and } r = a \bmod b \text{ with } 0 \le r < b
   $$

2. **Step 2: Expand the power.**  
   Substitute $a = qb + r$ into the expression:
   $$
   2^a - 1 = 2^{qb + r} - 1 = 2^r \left(2^{qb}\right) - 1
   $$

3. **Step 3: Annihilate the large factor.**  
   Notice that $2^b \equiv 1 \pmod{2^b - 1}$ because:
   $$
   (2^b - 1) \equiv 0 \pmod{2^b - 1} \implies 2^b \equiv 1 \pmod{2^b - 1}
   $$
   Raising both sides to the power $q$:
   $$
   2^{qb} = \left(2^b\right)^q \equiv 1^q = 1 \pmod{2^b - 1}
   $$

4. **Step 4: Substitute and collapse.**  
   Replace $2^{qb}$ with $1$:
   $$
   2^a - 1 \equiv 2^r(1) - 1 = 2^r - 1 \pmod{2^b - 1}
   $$
   Since $r = a \bmod b$, this gives:
   $$
   2^a - 1 \equiv 2^{a \bmod b} - 1 \pmod{2^b - 1}
   $$

5. **Step 5: Bound the residue.**  
   *This is the critical step that many students omit.*  
   Because $0 \le r < b$, exponentiating with base 2 gives:
   $$
   0 \le r < b \implies 2^0 \le 2^r < 2^b \implies 1 \le 2^r < 2^b
   $$
   Subtract 1 from all parts:
   $$
   0 \le 2^r - 1 < 2^b - 1
   $$
   Since $2^r - 1$ is non-negative and strictly smaller than the modulus $2^b - 1$, it is not merely congruent; it is the **exact remainder**:
   $$
   (2^a - 1) \bmod (2^b - 1) = 2^{a \bmod b} - 1
   $$

---

### The Boundary Case: $r = 0$

What happens when $b$ divides $a$ cleanly?  
If $b \mid a$, then the remainder is $r = a \bmod b = 0$.

Plugging $r = 0$ into our formula yields:
$$
2^0 - 1 = 1 - 1 = 0
$$

Does $2^b - 1$ really divide $2^a - 1$ when $b \mid a$?  
Yes! Using the polynomial factorization formula:
$$
\frac{x^q - 1}{x - 1} = x^{q-1} + x^{q-2} + \dots + 1
$$
Letting $x = 2^b$, we see that $(2^b - 1)$ divides $(2^b)^q - 1 = 2^{qb} - 1 = 2^a - 1$ with remainder 0. The formula handles the $r = 0$ boundary case with complete mathematical precision.

---

### Generalization to Any Base $c$

Notice that nothing in the proof relied specifically on the number 2, except that $2^b \equiv 1 \pmod{2^b - 1}$. The exact same five-step argument applies to any integer base $c \ge 2$:

$$
(c^a - 1) \bmod (c^b - 1) \equiv c^{a \bmod b} - 1
$$

Writing this one-line observation on your exam paper demonstrates deep mathematical maturity to the examiner.

---

### Master Comparison of Exam Proofs in DM-5

| Proof topic | Year | Core technique | Key rule cited |
| :-- | :--: | :-- | :-- |
| $(2^a - 1) \bmod (2^b - 1)$ | 2022 Q.7(d) | Divide exponent $a = qb + r$, kill $2^{qb}$, bound residue | Division Algorithm, Congruence compatibility |
| Prime divisor bound $p \le \sqrt{n}$ | 2023 Q.7(c) | Suppose factors $a, b > \sqrt{n}$, reach contradiction $ab > n$ | Contradiction, Euclid's Lemma, Transitivity |
| Remainder distribution | 2022 Q.8(d) | $d + 1$ integers divided by $d$ yield at most $d$ possible remainders | Pigeonhole Principle (DM-6.3) |

---

## 🔧 Worked Example

> **From:** 2022 Q.7(d) -- [Marks: 02]

**Question.** Show that if $a$ and $b$ are positive integers then $(2^a - 1) \bmod (2^b - 1) \equiv 2^{a \bmod b} - 1$.

**Solution.**

**Step 1. Write $a = qb + r$** with $q = \lfloor a/b \rfloor \ge 0$ and
$r = a \bmod b$ so $0 \le r < b$. Then $a = qb + r$.

**Step 2. Reduce the power.**

$$
2^a - 1 = 2^{qb+r} - 1 = 2^r \left(2^{qb}\right) - 1
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

Since $r = a \bmod b$,

$$
\boxed{(2^a - 1) \bmod (2^b - 1) \equiv 2^{a \bmod b} - 1}
$$

**Step 5. The residue really is the least one.** Since $0 \le r < b$ we have
$0 \le 2^r - 1 < 2^b - 1$, so $2^r - 1$ is the actual remainder and not merely a
congruent value. This is what makes the statement an equality of remainders
rather than only a congruence.

---

### Verification Table on Concrete Numerical Pairs

| $a$ | $b$ | $2^a - 1$ | $2^b - 1$ | Division $(2^a - 1) \div (2^b - 1)$ | $(2^a - 1) \bmod (2^b - 1)$ | $a \bmod b$ | $2^{a \bmod b} - 1$ | Match? |
| :--: | :--: | :--: | :--: | :-- | :--: | :--: | :--: | :--: |
| 13 | 5 | $8191$ | $31$ | $8191 = 31(264) + 7$ | **7** | $13 \bmod 5 = 3$ | $2^3 - 1 = \mathbf{7}$ | ✓ |
| 10 | 3 | $1023$ | $7$ | $1023 = 7(146) + 1$ | **1** | $10 \bmod 3 = 1$ | $2^1 - 1 = \mathbf{1}$ | ✓ |
| 20 | 6 | $1048575$ | $63$ | $1048575 = 63(16644) + 3$ | **3** | $20 \bmod 6 = 2$ | $2^2 - 1 = \mathbf{3}$ | ✓ |
| 9 | 4 | $511$ | $15$ | $511 = 15(34) + 1$ | **1** | $9 \bmod 4 = 1$ | $2^1 - 1 = \mathbf{1}$ | ✓ |
| 7 | 7 | $127$ | $127$ | $127 = 127(1) + 0$ | **0** | $7 \bmod 7 = 0$ | $2^0 - 1 = \mathbf{0}$ | ✓ |

Every single test case confirms the theorem with zero discrepancies.

---

## ⚡ Common Traps & Exam Tips

> [!WARNING] Common Trap: Omitting Step 5 (Bounding the Residue)
> Showing that $2^a - 1 \equiv 2^r - 1 \pmod{2^b - 1}$ is only halfway through the proof. That only establishes a congruence. To prove that $2^r - 1$ is the **remainder** (which is what the $\bmod$ operator means), you must explicitly prove that $0 \le 2^r - 1 < 2^b - 1$.
> Marks are regularly deducted if Step 5 is missing.

> [!TIP] State the Division Algorithm by Name
> Start your answer with: "By the Division Algorithm, let $a = qb + r$ where $0 \le r < b$." Naming the algorithm shows rigor and provides the legal foundation for the subsequent algebra.

---

[← Previous: DM-5.8 Number Bases](DM-5.8_Number_Bases.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: DM-6.1 Sum and Product Rules →](../DM-6_Counting/DM-6.1_Sum_and_Product_Rules.md)
