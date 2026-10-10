[← Previous: DM-5.6 Fermat's Little Theorem](DM-5.6_Fermats_Little_Theorem.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: DM-5.8 Number Bases →](DM-5.8_Number_Bases.md)

---

# DM-5.7: Chinese Remainder Theorem

> 🟠 **Priority:** Secondary | **Tested:** 1/3 papers (2022 Q.8(a)) | **Typical marks:** 3 to 4

## What This Is (and Why It Matters)

Legend says that ancient Chinese military commanders counted their armies without counting each soldier individually. They had soldiers line up in rows of 3 and counted the leftovers, then rows of 5, then rows of 7. Knowing only the remainders from these three line-ups, they could calculate the exact size of their entire army.

In modern mathematics, this is the **Chinese Remainder Theorem (CRT)**. It solves a system of simultaneous linear congruences:

$$
x \equiv a_1 \pmod{n_1}, \quad x \equiv a_2 \pmod{n_2}, \quad \dots, \quad x \equiv a_k \pmod{n_k}
$$

As long as the moduli $n_1, n_2, \dots, n_k$ are pairwise coprime (no two moduli share a common factor), there is always **exactly one** unique solution modulo their product $N = n_1 n_2 \cdots n_k$.

In 2022 Q.8(a), RUET tested the exact constructive formula for a 3-congruence system. It is one of the cleanest 4-mark questions on the exam once you master the step-by-step formula.

---

## 📝 Key Definitions

> **Chinese Remainder Theorem:** "Let $m_1, m_2, \dots, m_n$ be pairwise relatively prime positive integers greater than one and $a_1, a_2, \dots, a_n$ arbitrary integers. Then the system $x \equiv a_1 \pmod{m_1}, x \equiv a_2 \pmod{m_2}, \dots, x \equiv a_n \pmod{m_n}$ has a unique solution modulo $m = m_1 m_2 \dots m_n$." -- Rosen, §4.4, Theorem 2
>
> **In simple words:** If your moduli do not share any common factors, a system of congruence clues always locks onto one unique number between $0$ and the product of the moduli minus 1.

> **Pairwise Relatively Prime:** "The integers $a_1, a_2, \dots, a_n$ are **pairwise relatively prime** if $\gcd(a_i, a_j) = 1$ whenever $1 \leq i < j \leq n$." -- Rosen, §4.3, Definition 4
>
> **In simple words:** Pick any pair of moduli from your set; their greatest common divisor must be 1. The moduli themselves do not need to be prime numbers (for instance, 4 is composite, but 3, 4, and 5 are pairwise coprime).

> **The CRT Construction Variables:** $N = \prod_{i=1}^k n_i$, $M_i = \frac{N}{n_i}$, and $u_i = M_i^{-1} \pmod{n_i}$. -- Rosen, §4.4
>
> **In simple words:** $N$ is the product of all moduli. $M_i$ is that product with the $i$-th modulus removed. And $u_i$ is the modular inverse of $M_i$ modulo $n_i$.

---

## The Core Idea

### The Construction Formula

The unique solution modulo $N = n_1 n_2 \cdots n_k$ is given by:

$$
x = \sum_{i=1}^k a_i u_i M_i \pmod N
$$

**Why this formula works (the orthogonality trick):**
Look at what happens to the term $a_i u_i M_i$ when you check it modulo any $n_j$:

1. **When evaluating modulo $n_j$ where $j \neq i$:**  
   $M_i$ was defined as the product of all moduli **except** $n_i$. Therefore, $n_j$ is one of the factors inside $M_i$. This means $M_i$ is an exact multiple of $n_j$:
   $$
   M_i \equiv 0 \pmod{n_j} \implies a_i u_i M_i \equiv 0 \pmod{n_j}
   $$
   Every single term in the sum vanishes to 0 except the $j$-th term!

2. **When evaluating modulo $n_i$ (its own modulus):**  
   By definition, $u_i$ is the inverse of $M_i$ modulo $n_i$, meaning $M_i u_i \equiv 1 \pmod{n_i}$. So:
   $$
   a_i u_i M_i \equiv a_i (1) = a_i \pmod{n_i}
   $$

When you add them all up, the sum automatically satisfies $x \equiv a_i \pmod{n_i}$ for every single congruence!

---

### How to Find Modular Inverses $u_i$ Quickly

Under exam pressure, you do not need the Extended Euclidean Algorithm for small moduli like $3, 4, 5$. Just reduce $M_i \bmod n_i$ and test $u = 1, 2, 3, \dots$ until the product leaves a remainder of 1:

| Modulus $n_i$ | Product $M_i = N/n_i$ | Reduced $M_i \bmod n_i$ | Equation to solve | Inverse $u_i$ | Check ($M_i u_i \bmod n_i$) |
| :--: | :--: | :--: | :--: | :--: | :--: |
| 3 | $60 / 3 = 20$ | 2 | $2u_1 \equiv 1 \pmod 3$ | **2** | $2 \times 2 = 4 \equiv 1$ |
| 4 | $60 / 4 = 15$ | 3 | $3u_2 \equiv 1 \pmod 4$ | **3** | $3 \times 3 = 9 \equiv 1$ |
| 5 | $60 / 5 = 12$ | 2 | $2u_3 \equiv 1 \pmod 5$ | **3** | $2 \times 3 = 6 \equiv 1$ |

---

### Alternative Method: Iterative Substitution

If you ever forget the construction formula, you can solve the system by combining two congruences at a time:

1. Take $x \equiv 2 \pmod 3$. Write $x$ in parametric form: $x = 2 + 3k$.
2. Substitute into the second congruence $x \equiv 1 \pmod 4$:
   $$
   2 + 3k \equiv 1 \pmod 4 \implies 3k \equiv -1 \equiv 3 \pmod 4 \implies k \equiv 1 \pmod 4
   $$
   Write $k = 1 + 4m$, which gives:
   $$
   x = 2 + 3(1 + 4m) = 5 + 12m
   $$
   Notice that $5 \bmod 3 = 2$ and $5 \bmod 4 = 1$. It satisfies both!
3. Now substitute into the third congruence $x \equiv 3 \pmod 5$:
   $$
   5 + 12m \equiv 3 \pmod 5 \implies 2m \equiv 3 \equiv 8 \pmod 5 \implies m \equiv 4 \pmod 5
   $$
   Substitute $m = 4$:
   $$
   x = 5 + 12(4) = 53
   $$
Both methods produce the exact same answer: $x \equiv 53 \pmod{60}$.

---

## 🔧 Worked Example

> **From:** 2022 Q.8(a) -- [Marks: 04]

**Question.** Define Fermat's little theorem. Use the construction in the proof of the Chinese remainder theorem to find all solutions to $x \equiv 2 \pmod 3$, $x \equiv 1 \pmod 4$, $x \equiv 3 \pmod 5$.

**Solution.**

**Fermat's little theorem.** If $p$ is prime and $\gcd(a, p) = 1$, then

$$
\boxed{a^{p-1} \equiv 1 \pmod p}
$$

Equivalently $a^p \equiv a \pmod p$ for every integer $a$, with no coprimality condition needed. A worked case: $2^2 = 4 \equiv 1 \pmod 3$, and $4^4 = 256 \equiv 1 \pmod 5$.

**The CRT construction.** For moduli $n_1, n_2, \dots, n_k$ that are pairwise coprime, put $N = n_1 n_2 \cdots n_k$ and

$$
M_i = \frac{N}{n_i}, \qquad u_i = M_i^{-1} \pmod{n_i}
$$

Then the solution to $x \equiv a_i \pmod{n_i}$ for all $i$ is

$$
x = \sum_{i=1}^{k} a_i u_i M_i \pmod N
$$

**Direct evaluation using the CRT construction formula.**  
Here $a_1 = 2, n_1 = 3$; $a_2 = 1, n_2 = 4$; $a_3 = 3, n_3 = 5$.  
The moduli are pairwise coprime, with $N = 3 \times 4 \times 5 = 60$.

1. $M_1 = \frac{60}{3} = 20$.  
   We need $u_1 \equiv M_1^{-1} \pmod{n_1}$, so $20 u_1 \equiv 1 \pmod 3$.  
   Since $20 \equiv 2 \pmod 3$, $2 u_1 \equiv 1 \implies u_1 = 2$.

2. $M_2 = \frac{60}{4} = 15$.  
   We need $u_2 \equiv M_2^{-1} \pmod{n_2}$, so $15 u_2 \equiv 1 \pmod 4$.  
   Since $15 \equiv 3 \pmod 4$, $3 u_2 \equiv 1 \implies u_2 = 3$.

3. $M_3 = \frac{60}{5} = 12$.  
   We need $u_3 \equiv M_3^{-1} \pmod{n_3}$, so $12 u_3 \equiv 1 \pmod 5$.  
   Since $12 \equiv 2 \pmod 5$, $2 u_3 \equiv 1 \implies u_3 = 3$.

Now evaluate the sum:

$$
x = a_1 u_1 M_1 + a_2 u_2 M_2 + a_3 u_3 M_3
= 2(2)(20) + 1(3)(15) + 3(3)(12)
$$

$$
= 80 + 45 + 108 = 233
$$

Reducing modulo $N = 60$:

$$
233 = 3(60) + 53 \equiv 53 \pmod{60}
$$

**Alternative verification: combining two congruences at a time.**

Combine the first two, $x \equiv 2 \pmod 3$ and $x \equiv 1 \pmod 4$. Write $x = 2 + 3k$. Substituting into the second:

$$
2 + 3k \equiv 1 \pmod 4 \quad \Longrightarrow \quad 3k \equiv -1 \equiv 3 \pmod 4
$$

Since $3^{-1} \equiv 3 \pmod 4$, $k \equiv 3 \times 3 = 9 \equiv 1 \pmod 4$. Hence $k = 1 + 4m$ and

$$
x = 2 + 3(1 + 4m) = 5 + 12m
$$

**Check:** $5 \bmod 3 = 2$ ✓ and $5 \bmod 4 = 1$ ✓.

Now impose the third, $x \equiv 3 \pmod 5$:

$$
5 + 12m \equiv 3 \pmod 5 \quad \Longrightarrow \quad 12m \equiv -2 \equiv 3 \pmod 5
$$

Since $12 \equiv 2 \pmod 5$ and $2^{-1} \equiv 3 \pmod 5$,

$$
m \equiv 3 \times 3 = 9 \equiv 4 \pmod 5
$$

Take $m = 4$:

$$
x = 5 + 12(4) = 53
$$

$$
\boxed{x \equiv 53 \pmod{60}}
$$

**Verify all three:**

$$
53 \bmod 3 = 2 \quad \checkmark \qquad 53 \bmod 4 = 1 \quad \checkmark \qquad 53 \bmod 5 = 3 \quad \checkmark
$$

Since $N = 3 \cdot 4 \cdot 5 = 60$, the complete solution set is:

$$
x = 53 + 60k \quad \text{for every integer } k
$$

---

## ⚡ Common Traps & Exam Tips

> [!WARNING] Common Trap: Leaving the Answer as 233
> The construction formula yields $x = 233$. But $233 > 60$. The question asks for the solution to the system modulo $N = 60$. You must write $233 = 3(60) + 53 \equiv 53 \pmod{60}$.

> [!TIP] "Pairwise Coprime" Does Not Mean Primes
> Notice that in 2022 Q.8(a), the moduli are $3, 4, 5$. The number $4$ is composite. CRT does not require prime moduli; it requires **pairwise coprime** moduli ($\gcd(3,4) = 1, \gcd(4,5) = 1, \gcd(3,5) = 1$).

---

[← Previous: DM-5.6 Fermat's Little Theorem](DM-5.6_Fermats_Little_Theorem.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: DM-5.8 Number Bases →](DM-5.8_Number_Bases.md)
