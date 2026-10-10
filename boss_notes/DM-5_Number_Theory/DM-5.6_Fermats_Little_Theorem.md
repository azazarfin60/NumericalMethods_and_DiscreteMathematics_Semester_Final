[← Previous: DM-5.5 Modular Exponentiation](DM-5.5_Modular_Exponentiation.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: DM-5.7 Chinese Remainder Theorem →](DM-5.7_Chinese_Remainder_Theorem.md)

---

# DM-5.6: Fermat's Little Theorem

> 🟡 **Priority:** Light Review | **Tested:** 1/3 papers (2022 Q.8(a) part 1) | **Typical marks:** 1 to 2

## What This Is (and Why It Matters)

Imagine you need to compute $7^{1000} \bmod 11$. Instead of building a full repeated squaring table, you can use a theorem discovered by Pierre de Fermat in 1640: whenever the modulus $p$ is a prime number, raising any integer coprime to $p$ to the power $(p - 1)$ always collapses to $1$.

Because 11 is prime, $7^{10} \equiv 1 \pmod{11}$. Since $1000 = 10 \times 100$, the exponent $1000$ vanishes completely:

$$
7^{1000} = (7^{10})^{100} \equiv 1^{100} = 1 \pmod{11}
$$

In 2022 Q.8(a), RUET paired "Define Fermat's Little Theorem" directly with a Chinese Remainder Theorem calculation. This is a quick definition question that takes two minutes to write and earns easy marks if you state the conditions precisely.

---

## 📝 Key Definitions

> **Fermat's Little Theorem (Exponential Form):** "If $p$ is prime and $a$ is an integer not divisible by $p$, then $a^{p-1} \equiv 1 \pmod p$." -- Rosen, §4.4, Theorem 3
>
> **In simple words:** When you raise a number to the power of $(p - 1)$ modulo a prime $p$ (and the number is not a multiple of $p$), the remainder is always 1.

> **Fermat's Little Theorem (Alternative Form):** "Also, for every integer $a$ we have $a^p \equiv a \pmod p$." -- Rosen, §4.4, Theorem 3
>
> **In simple words:** If you multiply both sides by $a$, the theorem works for every single integer $a$, including multiples of $p$, without needing any coprimality condition.

> **Pseudoprime to Base $b$:** "Let $n$ be a composite positive integer and $b$ a positive integer. If $b^{n-1} \equiv 1 \pmod n$, then $n$ is called a **pseudoprime to the base $b$**." -- Rosen, §4.4, Definition 1
>
> **In simple words:** A composite number that passes Fermat's primality test for a specific base, tricking you into thinking it might be prime even though it is composite.

---

## The Core Idea

### The Two Forms of the Theorem

Fermat's Little Theorem has two mathematical presentations. You must understand the difference:

#### Form 1: Exponent Reduction Form
$$
a^{p-1} \equiv 1 \pmod p \quad \text{provided } p \nmid a \text{ (or } \gcd(a, p) = 1\text{)}
$$
- This is the form you use to collapse large powers.
- **Why the condition matters:** If $p \mid a$, then $a \equiv 0 \pmod p$. But $0^{p-1} = 0 \not\equiv 1$. You cannot leave out the coprimality clause!

#### Form 2: Universal Polynomial Form
$$
a^p \equiv a \pmod p \quad \text{for every integer } a
$$
- If $\gcd(a, p) = 1$, multiplying $a^{p-1} \equiv 1$ by $a$ yields $a^p \equiv a$.
- If $p \mid a$, then $a \equiv 0 \pmod p$, so $0^p = 0 \equiv 0 \pmod p$.
- Therefore, Form 2 holds universally with zero exceptions.

### How to Reduce Exponents Modulo a Prime

To evaluate $a^n \bmod p$ where $p$ is prime and $p \nmid a$:

1. Divide the exponent $n$ by $(p - 1)$ using the Division Algorithm:
   $$
   n = q(p - 1) + r, \quad \text{with } 0 \le r < p - 1
   $$
2. Split the power into a multiple of $(p - 1)$ and the remainder $r$:
   $$
   a^n = a^{q(p-1) + r} = \left(a^{p-1}\right)^q \cdot a^r
   $$
3. Apply Fermat's Little Theorem ($a^{p-1} \equiv 1$):
   $$
   a^n \equiv (1)^q \cdot a^r = a^r \pmod p
   $$

#### Quick Example: $3^{644} \bmod 43$
43 is a prime number, so $p - 1 = 42$.  
Divide the exponent: $644 = 42 \times 15 + 14$.  
Therefore:
$$
3^{644} \equiv 3^{14} \pmod{43}
$$
This reduces an exponent of 644 down to just 14 in one line!

---

### The Converse is False: Pseudoprimes

Students often ask: if $b^{n-1} \equiv 1 \pmod n$, does that prove $n$ is prime?

**No.** The converse does not hold. Composite numbers can occasionally satisfy Fermat's congruence. These numbers are called **pseudoprimes**.

The most famous counterexample is $n = 341$:
- Factorization: $341 = 11 \times 31$ (clearly composite).
- But compute $2^{340} \bmod 341$:
  - By Fermat, $2^{10} \equiv 1 \pmod{11} \implies 2^{340} = (2^{10})^{34} \equiv 1^{34} = 1 \pmod{11}$.
  - Similarly, $2^5 = 32 \equiv 1 \pmod{31} \implies 2^{340} = (2^5)^{68} \equiv 1^{68} = 1 \pmod{31}$.
  - Since $2^{340} \equiv 1$ modulo both 11 and 31, by the Chinese Remainder Theorem:
  $$
  2^{340} \equiv 1 \pmod{341}
  $$
- Therefore, $341$ is a pseudoprime to base 2.

Composite numbers that are pseudoprimes to **every** coprime base are called **Carmichael numbers** (the smallest is $561 = 3 \times 11 \times 17$).

---

## 🔧 Worked Example

> **From:** 2022 Q.8(a), part one -- [Marks: 01 to 02]

**Question.** Define Fermat's little theorem.

**Solution.**

**Fermat's little theorem.** If $p$ is prime and $\gcd(a, p) = 1$, then

$$
\boxed{a^{p-1} \equiv 1 \pmod p}
$$

Equivalently $a^p \equiv a \pmod p$ for every integer $a$, with no coprimality condition needed. A worked case: $2^2 = 4 \equiv 1 \pmod 3$, and $4^4 = 256 \equiv 1 \pmod 5$.

---

## ⚡ Common Traps & Exam Tips

> [!WARNING] Common Trap: Forgetting the Coprimality Condition
> Stating "$a^{p-1} \equiv 1 \pmod p$ for all integers $a$" will lose you marks. If $a = 6$ and $p = 3$, $6^2 = 36 \equiv 0 \pmod 3 \neq 1$. You must explicitly write: **"where $p$ is prime and $p \nmid a$"** (or $\gcd(a, p) = 1$).

> [!TIP] Do Not Confuse with Fermat's Last Theorem
> Fermat's **Little** Theorem is about modular powers ($a^{p-1} \equiv 1 \pmod p$). Fermat's **Last** Theorem is about Diophantine equations ($x^n + y^n = z^n$ has no nonzero integer solutions for $n > 2$). Examiners ask for Fermat's Little Theorem!

---

[← Previous: DM-5.5 Modular Exponentiation](DM-5.5_Modular_Exponentiation.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: DM-5.7 Chinese Remainder Theorem →](DM-5.7_Chinese_Remainder_Theorem.md)
