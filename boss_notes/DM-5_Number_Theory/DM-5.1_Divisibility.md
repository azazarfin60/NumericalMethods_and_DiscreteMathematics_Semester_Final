[← Previous: DM-4.5 Mathematical Induction](../DM-4_Proof_Techniques/DM-4.5_Mathematical_Induction.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: DM-5.2 Prime Numbers →](DM-5.2_Prime_Numbers.md)

---

# DM-5.1: Divisibility & Fundamental Theorem of Arithmetic

> ⚫ **Priority:** Light Foundation | **Tested:** 0/3 direct questions (invoked implicitly in proofs) | **Typical marks:** 2 to 3

## What This Is (and Why It Matters)

Divisibility is the starting point of number theory. You already know how to divide integers with a calculator and get a decimal. Number theory does something different: it looks only at exact integer divisions with zero remainder, and what happens when a remainder is left over.

Even though RUET has not dedicated an entire question purely to defining divisibility, every single proof in DM-5.2 (prime bounds) and DM-5.9 (modular identities) rests directly on these definitions. If you do not know the formal laws of divisibility, your proofs will have logical gaps that cost marks.

---

## 📝 Key Definitions

> **Divisibility:** "If $a$ and $b$ are integers with $a \neq 0$, we say that $a$ **divides** $b$ if there is an integer $c$ such that $b = ac$, or equivalently, if $b/a$ is an integer." -- Rosen, §4.1, Definition 1
>
> **In simple words:** One integer divides another if it fits into it cleanly with nothing left over. We write this as $a \mid b$. For example, $3 \mid 12$ because $12 = 3 \times 4$.

> **The Division Algorithm:** "Let $a$ be an integer and $d$ a positive integer. Then there are unique integers $q$ and $r$, with $0 \leq r < d$, such that $a = dq + r$." -- Rosen, §4.1, Theorem 2
>
> **In simple words:** When you divide any integer by a positive integer divisor, you always get one unique quotient and one unique remainder. The remainder is never negative, and it is strictly smaller than the divisor.

> **Divisor, Dividend, Quotient, and Remainder:** "In the equality given in the division algorithm, $d$ is called the **divisor**, $a$ is called the **dividend**, $q$ is called the **quotient**, and $r$ is called the **remainder**." -- Rosen, §4.1, Definition 2
>
> **In simple words:** In $a = dq + r$, $a$ is the number you started with, $d$ is what you divide by, $q$ is how many whole times $d$ fits, and $r$ is the leftover piece.

> **Fundamental Theorem of Arithmetic:** "Every integer greater than 1 can be written uniquely as a prime or as the product of two or more primes where the prime factors are written in order of nondecreasing size." -- Rosen, §4.3, Theorem 2
>
> **In simple words:** Prime numbers are the indivisible atoms of integers. Every number above 1 has a unique prime fingerprint. For instance, 60 is always $2^2 \times 3 \times 5$, and no other prime combination can ever make 60.

---

## The Core Idea

### The Notation: $a \mid b$ vs $a / b$

Be very careful with your notation:
- $a \mid b$ is a **statement** (a relationship that is either true or false). It reads: "$a$ divides $b$."
- $a / b$ or $\frac{a}{b}$ is a **number** (an arithmetic fraction).

For example, $4 \mid 12$ is a true statement. But $12 / 4$ is the number $3$. Writing $4 / 12$ when you mean $4 \mid 12$ will confuse anyone reading your paper.

### The Three Basic Properties of Divisibility

Rosen establishes three fundamental theorems that you can cite in any proof:

1. **Sum property:** If $a \mid b$ and $a \mid c$, then $a \mid (b + c)$.
   - *Reason:* $b = ak_1$ and $c = ak_2$, so $b + c = a(k_1 + k_2)$.
2. **Scaling property:** If $a \mid b$, then $a \mid bc$ for all integers $c$.
   - *Reason:* $b = ak$, so $bc = a(kc)$.
3. **Transitivity:** If $a \mid b$ and $b \mid c$, then $a \mid c$.
   - *Reason:* $b = ak_1$ and $c = bk_2$, so $c = a(k_1 k_2)$.

### The Linear Combination Property

Combining the sum and scaling properties yields the most powerful tool in divisibility proofs:

$$
\text{If } a \mid b \text{ and } a \mid c, \text{ then } a \mid (sb + tc) \text{ for any integers } s \text{ and } t.
$$

**Reading this property:** If a number divides two quantities, it also divides any integer combination of those two quantities.

### The Division Algorithm in Action

When $a$ is divided by $d$, the remainder $r$ must satisfy:

$$
0 \le r < d
$$

Let us look at two cases:

1. **Positive dividend:** $101$ divided by $11$.
   $$
   101 = 11 \times 9 + 2 \implies q = 9, \; r = 2
   $$
2. **Negative dividend:** $-11$ divided by $3$.
   - A common error is writing $-11 = 3 \times (-3) - 2$. This is illegal because $r = -2 < 0$.
   - The correct formulation pushes the quotient one step lower:
   $$
   -11 = 3 \times (-4) + 1 \implies q = -4, \; r = 1
   $$
   Here $0 \le 1 < 3$, which satisfies the theorem.

### The Fundamental Theorem of Arithmetic (Unique Factorization)

Every integer $n > 1$ can be expressed in canonical prime factorization form:

$$
n = p_1^{a_1} p_2^{a_2} \cdots p_k^{a_k}
$$

where $p_1 < p_2 < \dots < p_k$ are distinct prime numbers, and each exponent $a_i$ is a positive integer.

#### Counting Total Positive Divisors

If $n = p_1^{a_1} p_2^{a_2} \cdots p_k^{a_k}$, any divisor $d$ must have the form $p_1^{b_1} p_2^{b_2} \cdots p_k^{b_k}$, where each exponent satisfies $0 \le b_i \le a_i$.

By the product rule of counting (DM-6.1), each exponent $b_i$ has $(a_i + 1)$ independent choices:

$$
\tau(n) = (a_1 + 1)(a_2 + 1)\cdots(a_k + 1)
$$

For example, take $n = 360$:
- Factor into primes: $360 = 2^3 \times 3^2 \times 5^1$.
- Total positive divisors: $\tau(360) = (3 + 1)(2 + 1)(1 + 1) = 4 \times 3 \times 2 = 24$.

---

## 🔧 Illustrative Examples

### Example 1: Divisibility Proof via Linear Combinations

**Problem.** Show that if $d$ divides both $2a + 3$ and $a + 5$ for an integer $a$, then $d$ must divide $7$.

**Solution.**
We are given:
$$
d \mid (2a + 3) \quad \text{and} \quad d \mid (a + 5)
$$

By the linear combination property, $d$ divides any combination $(2a + 3)s + (a + 5)t$. Choose $s = 1$ and $t = -2$ to cancel the variable $a$:

$$
(2a + 3)(1) + (a + 5)(-2) = 2a + 3 - 2a - 10 = -7
$$

Therefore:
$$
d \mid (-7) \implies d \mid 7
$$

Since the only divisors of $7$ are $\pm 1$ and $\pm 7$, $d$ must be one of these four values.

---

### Example 2: Division Algorithm with Negative Numbers

**Problem.** Find the quotient and remainder when $a = -22$ is divided by $d = 6$.

**Solution.**
We seek unique integers $q$ and $r$ such that:
$$
-22 = 6q + r, \quad \text{with } 0 \le r < 6
$$

Dividing $-22$ by $6$ yields $-3.666\ldots$  
Floor function gives $q = \lfloor -22/6 \rfloor = -4$.  
Now solve for $r$:
$$
r = -22 - 6(-4) = -22 + 24 = 2
$$

Since $0 \le 2 < 6$, this is the unique valid remainder:
$$
-22 = 6(-4) + 2 \implies q = -4, \; r = 2
$$

---

## ⚡ Common Traps & Exam Tips

> [!WARNING] Common Trap: Negative Remainders
> The modulo operator in many programming languages (like C/C++) can return negative values for negative dividends. But in discrete mathematics, the remainder $r$ must **always** satisfy $0 \le r < d$. If your arithmetic produces a negative remainder, subtract 1 from your quotient and add the divisor to your remainder.

> [!TIP] Proof Tip: Naming Divisibility Laws
> Whenever you transition from $a \mid b$ and $b \mid c$ to $a \mid c$ in a formal exam proof, explicitly write "by transitivity of divisibility". Naming the rule guarantees full marks.

---

[← Previous: DM-4.5 Mathematical Induction](../DM-4_Proof_Techniques/DM-4.5_Mathematical_Induction.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: DM-5.2 Prime Numbers →](DM-5.2_Prime_Numbers.md)
