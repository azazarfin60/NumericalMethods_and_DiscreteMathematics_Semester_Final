[← Previous: DM-5.1 Divisibility](DM-5.1_Divisibility.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: DM-5.3 GCD & Euclidean Algorithm →](DM-5.3_GCD_and_Euclidean.md)

---

# DM-5.2: Prime Numbers

> 🟠 **Priority:** Secondary | **Tested:** 1/3 papers (2023 Q.7(c)) | **Typical marks:** 3

## What This Is (and Why It Matters)

Prime numbers are the building blocks of arithmetic. Every integer larger than 1 is either a prime itself or can be built by multiplying primes together. Because primes cannot be factored any further, understanding them is essential for cryptography, hashing, and computer security.

The exam focuses heavily on one central theorem: the **prime divisor bound**. If you have a composite number $n$, you do not need to search all the way up to $n$ to find a prime factor. You only need to search up to $\sqrt{n}$. In 2023 Q.7(c), RUET asked students to prove this exact property from first principles.

---

## 📝 Key Definitions

> **Prime:** "An integer $p$ greater than 1 is called **prime** if the only positive factors of $p$ are 1 and $p$." -- Rosen, §4.3, Definition 1
>
> **In simple words:** A prime is a whole number greater than 1 that cannot be broken down into smaller integer multiples. It has exactly two positive divisors: 1 and itself.

> **Composite:** "A positive integer that is greater than 1 and is not prime is called **composite**." -- Rosen, §4.3, Definition 1
>
> **In simple words:** Any integer greater than 1 that has extra divisors beyond 1 and itself is composite. You can always write it as $n = ab$ where both $a$ and $b$ are strictly between $1$ and $n$.

> **Trial Division:** "A brute-force method to test primality or find prime factors by dividing by primes up to $\sqrt{n}$." -- Rosen, §4.3, Key Terms
>
> **In simple words:** You test whether a number is prime by trying to divide it by successive prime numbers ($2, 3, 5, 7, \dots$). If no prime up to $\sqrt{n}$ divides it, the number is guaranteed to be prime.

> **Prime Divisor Bound:** "If $n$ is a composite integer, then $n$ has a prime divisor less than or equal to $\sqrt{n}$." -- Rosen, §4.3, Theorem 3
>
> **In simple words:** A composite number cannot be formed solely by factors that are all strictly larger than its square root. At least one factor, and therefore at least one prime factor, must be at or below $\sqrt{n}$.

---

## The Core Idea

### Primes vs Composites

Every integer falls into one of three camps:
1. The number $1$ is **neither prime nor composite** (it is a unit). By excluding 1 from primes, prime factorizations stay unique (Fundamental Theorem of Arithmetic).
2. The number $2$ is the **only even prime**. Every larger even number $2k$ has $2$ and $k$ as proper divisors, so all other even numbers are composite.
3. Every integer $n > 1$ is either prime or composite.

| $n$ | Classification | Divisors | Why |
| :-- | :-- | :-- | :-- |
| 1 | **Neither** | 1 | By definition, primes and composites must exceed 1 |
| 2 | Prime | 1, 2 | Exactly two divisors; only even prime |
| 4 | Composite | 1, 2, 4 | Proper factorization $2 \times 2$ |
| 7 | Prime | 1, 7 | Cannot be factored into smaller positive integers |
| 9 | Composite | 1, 3, 9 | Proper factorization $3 \times 3$ |
| 91 | Composite | 1, 7, 13, 91 | Proper factorization $7 \times 13$ |
| 97 | Prime | 1, 97 | No prime up to $\sqrt{97} \approx 9.85$ divides it |

### Why the Prime Divisor Bound Works

Think about factoring a number $n = ab$.
- If both factors $a$ and $b$ were strictly greater than $\sqrt{n}$, their product would be:
$$
a > \sqrt{n} \quad \text{and} \quad b > \sqrt{n} \implies ab > \sqrt{n} \cdot \sqrt{n} = n
$$
- But $ab = n$. A product cannot be strictly greater than itself. That is an immediate contradiction.
- Therefore, at least one of the factors must be less than or equal to $\sqrt{n}$.
- Since that factor is greater than 1, it must possess a prime divisor. By transitivity of divisibility, that prime divisor also divides $n$, and it is bounded by $\sqrt{n}$.

### The Two Underlying Lemmas in the Proof

When writing the proof for full marks, you rely on two classical number-theoretic properties:
1. **Existence of a prime divisor:** Every integer $a > 1$ has at least one prime divisor. By Euclid's Lemma and the Fundamental Theorem of Arithmetic, we can factor $a$ into primes; the smallest factor greater than 1 is prime.
2. **Transitivity of divisibility:** If $p \mid a$ and $a \mid n$, then $p \mid n$.

### Trial Division in Practice

The prime divisor bound cuts primality testing down from an impossible search to a quick check. Instead of testing all numbers up to $n$, you only test primes up to $\lfloor\sqrt{n}\rfloor$.

| Number $n$ | $\sqrt{n}$ | Primes to test ($\le \sqrt{n}$) | Outcome | Result |
| :--: | :--: | :--: | :--: | :--: |
| 91 | 9.54 | 2, 3, 5, 7 | $91 = 7 \times 13$ | Composite |
| 97 | 9.85 | 2, 3, 5, 7 | None divide 97 | Prime |
| 121 | 11.00 | 2, 3, 5, 7, 11 | $121 = 11 \times 11$ | Composite |
| 143 | 11.96 | 2, 3, 5, 7, 11 | $143 = 11 \times 13$ | Composite |

For 97, once you check 2, 3, 5, and 7 and find no clean division, you stop. You do not need to test 11, 13, or any higher prime.

---

## 🔧 Worked Example

> **From:** 2023 Q.7(c) -- [Marks: 03]

**Question.** If $n$ is a composite integer then $n$ has a prime divisor less than or equal to $\sqrt{n}$.  
*(Note: Prove that if $n$ is a composite integer then $n$ has a prime divisor less than or equal to $\sqrt{n}$.)*

**Solution.**

**Step 1. Express the composite number as a product of factors.**  
Let $n$ be a composite integer. By definition of a composite number, $n = ab$ where $a$ and $b$ are integers such that:

$$
1 < a < n \quad \text{and} \quad 1 < b < n
$$

**Step 2. Show that at least one factor is bounded by $\sqrt{n}$.**  
We prove that $a \le \sqrt{n}$ or $b \le \sqrt{n}$ by contradiction.  
Suppose, for the sake of contradiction, that both $a > \sqrt{n}$ and $b > \sqrt{n}$.

Multiplying these two inequalities:

$$
a > \sqrt{n} \quad \text{and} \quad b > \sqrt{n} \implies ab > \sqrt{n}\sqrt{n} = n
$$

This gives $ab > n$, which contradicts the fact that $ab = n$.  
Therefore, our assumption was false. At least one of the factors must be less than or equal to $\sqrt{n}$.

Without loss of generality, assume $a \le \sqrt{n}$, so:

$$
1 < a \le \sqrt{n}
$$

**Step 3. Extract a prime divisor from factor $a$.**  
Since $a > 1$, by the Fundamental Theorem of Arithmetic (or the well-ordering principle), $a$ has at least one prime divisor $p$. That is:

$$
p \mid a \quad \text{where } p \text{ is prime}
$$

Because $p \mid a$, it follows that $p \le a$. Combining this with $a \le \sqrt{n}$:

$$
p \le a \le \sqrt{n} \implies p \le \sqrt{n}
$$

**Step 4. Conclude by transitivity of divisibility.**  
Since $p \mid a$ and $a \mid n$, by transitivity of divisibility we have:

$$
p \mid n
$$

Thus, $p$ is a prime divisor of $n$ that satisfies $p \le \sqrt{n}$.

$$
\boxed{\text{Every composite } n \text{ has a prime divisor } p \text{ with } p \le \sqrt{n}}
$$

---

## ⚡ Common Traps & Exam Tips

> [!WARNING] Common Trap: Forgetting the Factor Divisor Step
> Many students show $a \le \sqrt{n}$ and then stop, writing "$a$ is the divisor, so we are done." But $a$ might be composite itself (for example, $n = 48$, where $a = 6 \le \sqrt{48} \approx 6.93$, but 6 is not prime). You must explicitly state that $a$ has a prime factor $p \le a$, and by transitivity $p \mid n$.

> [!TIP] WLOG Notation
> Writing "Without loss of generality (WLOG), assume $a \le \sqrt{n}$" is mathematically standard and saves you from repeating identical lines for $b$.

---

[← Previous: DM-5.1 Divisibility](DM-5.1_Divisibility.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: DM-5.3 GCD & Euclidean Algorithm →](DM-5.3_GCD_and_Euclidean.md)
