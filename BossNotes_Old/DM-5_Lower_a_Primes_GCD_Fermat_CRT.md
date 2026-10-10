[← Previous: DM-5.5 Modular Exponentiation](DM-5.5_Modular_Exponentiation.md) | [🏠 Index](00_Index.md) | [Next: DM-5 Lower-b: Bases and Proofs →](DM-5_Lower_b_Bases_Proofs.md)

---

# DM-5 Lower-a: Primes, GCD, Fermat, CRT
> **Section:** B (Discrete Mathematics) | **Priority:** 🟠🟡 (mixed) | **Exam Frequency:** 4/3 DM papers across 2022 and 2023
> **Subtopics:** DM-5.2 (Prime Numbers), DM-5.3 (GCD, LCM, Euclidean Algorithm), DM-5.6 (Fermat's Little Theorem), DM-5.7 (Chinese Remainder Theorem)
> **Sources:** Rosen §4.3 (pp. 21–35), §4.4 (pp. 41–45), Fahad Notes Class-19, Raidah Notes §5, Shishir Notes §3, §5

## Why This Topic Matters

Four small subtopics, each worth two or three marks, each appearing in a different year. Raidah's notes mark the Chinese Remainder Theorem as "**Must study / high exam priority topic!**", and 2022 Q.8(a) confirmed that: one question, FLT plus a three-congruence CRT system.

The Extended Euclidean Algorithm is a different story. Both class note sets record it as **self-study**, and Fahad says it "is marked for self-study and is best practiced in tabular form". It is the most fragile thing in the file, and 2022 Q.7(c) tested it.

> [!WARNING] Danger zone: Extended Euclidean Algorithm ⚠️
> Neither teacher covered it in class. It exists in Shishir's notes as a table with a diagonal-shift rule, and that table is the fastest route. Expect to be asked for it once, and expect the Bezout coefficients to carry as many marks as the gcd itself.

---

## 📝 Key Definitions

> **Prime:** "an integer greater than 1 with exactly two positive integer divisors (1 and itself)." — Rosen, §4.3, Key Terms (p. 20)

> **Composite:** "an integer greater than 1 that is not prime." — Rosen, §4.3, Key Terms (p. 20). Sharper: "The integer $n$ is composite if and only if there exists an integer $a$ such that $a \mid n$ and $1 < a < n$." — Rosen, §4.3 (p. 21)

> **Trial division:** "a brute-force method to test primality or find prime factors by dividing by primes up to $\sqrt{n}$." — Rosen, §4.3, Key Terms (p. 20)

> **Prime divisor bound:** "If $n$ is a composite integer, then $n$ has a prime divisor less than or equal to $\sqrt{n}$." — Rosen, §4.3, Key Results (p. 34)

> **GCD:** "the largest integer that divides both $a$ and $b$." — Rosen, §4.3, Key Terms (p. 32)

> **Relatively prime:** "integers $a$ and $b$ such that $\gcd(a, b) = 1$." — Rosen, §4.3, Key Terms (p. 32)

> **LCM:** "the smallest positive integer that is divisible by both $a$ and $b$." — Rosen, §4.3, Key Terms (p. 32)

> **Bézout's theorem:** "If $a$ and $b$ are positive integers, then there exist integers $s$ and $t$ such that $\gcd(a, b) = sa + tb$." — Rosen, §4.3 (p. 33)

> **Bézout coefficients and identity:** "If $a$ and $b$ are positive integers, then integers $s$ and $t$ such that $\gcd(a, b) = sa + tb$ are called **Bézout coefficients** of $a$ and $b$. Also, the equation $\gcd(a, b) = sa + tb$ is called **Bézout's identity**." — Rosen, §4.3, Definition 6 (p. 34)

> **Euclidean algorithm property:** "If $a = bq + r$, then $\gcd(a, b) = \gcd(b, r)$." — Rosen, §4.3, Key Results (p. 34). This single identity is why the algorithm terminates.

> **Fermat's Little Theorem:** "If $p$ is prime and $a$ is an integer not divisible by $p$, then $a^{p-1} \equiv 1 \pmod p$." — Rosen, §4.4, Theorem 3 (p. 42). The same theorem adds a second form: for every integer $a$ we have $a^p \equiv a \pmod p$, with no coprimality condition needed.

> **Chinese Remainder Theorem:** "Let $m_1, m_2, \dots, m_n$ be pairwise relatively prime positive integers greater than one and $a_1, a_2, \dots, a_n$ arbitrary integers. Then the system $x \equiv a_1 \pmod{m_1}, x \equiv a_2 \pmod{m_2}, \dots, x \equiv a_n \pmod{m_n}$ has a unique solution modulo $m = m_1 m_2 \dots m_n$." — Rosen, §4.4, Theorem 2 (p. 42)

---

## DM-5.2: Prime Numbers

A prime has exactly two positive divisors. That means 1 and itself, and nothing else. Every integer above 1 is either prime or composite.

| $n$ | Prime or composite? | Why |
| :-- | :-- | :-- |
| 2 | prime | divisors $1, 2$ only |
| 4 | composite | $4 = 2 \times 2$ |
| 7 | prime | not divisible by 2, 3, 4, 5, 6 |
| 9 | composite | $9 = 3 \times 3$ |
| 1 | **neither** | not greater than 1 |
| 97 | prime | no prime up to $\sqrt{97} = 9.85$ divides it |

> [!NOTE] 1 is not prime and 2 is the only even prime
> Every other even number $2k$ with $k > 1$ has $k$ as a proper divisor. So 2 is the only even prime, and 1 is excluded by the "greater than 1" clause.

### The Prime Divisor Bound

The most useful theorem in this subtopic. It says a composite number always has a small prime factor.

**Statement.** If $n$ is composite, then $n$ has a prime divisor $p$ with $p \le \sqrt{n}$.

**Why it matters.** Trial division for primality need only test divisors up to $\sqrt{n}$, not up to $n$. For a 64-bit number that is the difference between $2^{64}$ and $2^{32}$ trials.

### Worked Example (PYQ 2023 Q.7(c))

> **Source:** 2023 Q.7(c)

**Question.** If $n$ is a composite integer then $n$ has a prime divisor less than or equal to $\sqrt{n}$.

**Solution.**

**Proof.**

Let $n$ be composite. Then by definition $n = ab$ for integers $a, b$ with $1 < a < n$ and $1 < b < n$.

**Key observation.** At least one of $a$ and $b$ is at most $\sqrt{n}$. Suppose both were larger:

$$
a > \sqrt{n} \quad \text{and} \quad b > \sqrt{n} \quad \Longrightarrow \quad ab > \sqrt{n}\sqrt{n} = n
$$

Since $ab = n$, this is a contradiction. Hence $a \le \sqrt{n}$ or $b \le \sqrt{n}$.

WLOG suppose $a \le \sqrt{n}$, so $1 < a \le \sqrt{n}$.

**Now find a prime divisor at most $a$.** Every integer $a > 1$ has a prime divisor: keep dividing by a prime factor until the result is 1, and the last prime divided out is a prime $p$ dividing $a$. So there is a prime $p$ with $p \mid a$.

Since $a \mid n$ and $p \mid a$, transitivity of divisibility gives $p \mid n$. And $p \le a \le \sqrt{n}$.

$$
\boxed{\text{Every composite } n \text{ has a prime divisor } p \text{ with } p \le \sqrt{n}}
$$

> [!note] Why this matters
> This is the fact that makes trial division for factorisation terminate at $\sqrt{n}$ instead of at $n$. The trial-divisor test for primality therefore need only try divisors up to $\sqrt{n}$, which is the square root of the work.
>
> Worked examples: $91 = 7 \times 13$ with $\sqrt{91} = 9.539$, and the prime divisor $7$ is indeed below it. $97$ is prime, so the statement does not apply to it, which is why a trial division up to $9$ establishes its primality.

**The two lemmas the proof leans on, stated separately.**

1. If $p \mid ab$ and $p$ is prime, then $p \mid a$ or $p \mid b$. This is Euclid's Lemma, and it is what makes "every integer has a prime divisor" true: apply it repeatedly to factor $a$ until nothing is left.
2. If $a \mid n$ and $p \mid a$, then $p \mid n$. This is transitivity of divisibility, from Theorem 1 in Rosen §4.1.

**Trial division in practice, using the bound.**

| $n$ | $\sqrt{n}$ | Primes to test | Result |
| :-- | --: | :-- | :-- |
| 91 | 9.54 | 2, 3, 5, 7 | $91 = 7 \times 13$, composite |
| 97 | 9.85 | 2, 3, 5, 7 | none divide, prime |
| 121 | 11.0 | 2, 3, 5, 7, 11 | $121 = 11^2$, composite |
| 143 | 11.96 | 2, 3, 5, 7, 11 | $143 = 11 \times 13$, composite |

Testing 2, 3, 5, 7 for 97 is enough. Testing 11, 13 and up would be wasted, which is exactly what the bound buys.

---

## DM-5.3: GCD, LCM and the Euclidean Algorithm

### The identity behind the algorithm

$$
a = bq + r \implies \gcd(a, b) = \gcd(b, r)
$$

Any common divisor of $a$ and $b$ divides $bq + r - bq = r$, so it divides $\gcd(b, r)$. The argument runs in reverse too, so the two gcds are equal. Every step of the algorithm is this identity applied once.

**The last nonzero remainder is the gcd.** The sequence strictly decreases ($r < b$ always), so it must reach 0 in finite steps, and the remainder just before 0 is the answer.

### Ordinary Euclidean Algorithm

Two columns are enough, or use the four-column table that both note sets show:

![Hand-written Euclidean algorithm table with columns q, a, b, r for gcd(26, 118) = 2 (Shishir Notes p. 83)](diagrams/dm5_euclidean_algorithm_table.jpg)

| $a$ | $b$ | $r$ |
| --: | --: | --: |
| 118 | 26 | 14 |
| 26 | 14 | 12 |
| 14 | 12 | 2 |
| 12 | 2 | 0 |

Last nonzero remainder is 2, so $\gcd(26, 118) = 2$.

### Extended Euclidean Algorithm ⚠️

Ordinary Euclid gives the gcd. The extended form also gives the Bezout coefficients $s, t$ with $sa + tb = \gcd(a, b)$, and that is what modular inverses are built from. Two routes exist.

**Route A, back substitution.** Run the ordinary algorithm, then walk the divisions backwards rewriting each remainder. This is the method used in the 2022 answer and is the easiest to write under exam pressure, since you already have the divisions on the page.

**Route B, the tabular recurrence.** Carry the coefficients alongside. Shishir notes p. 84 give the rule and the table:

$$
s = s_1 - s_2 q, \qquad t = t_1 - t_2 q
$$

with initial values $s_1 = 1, s_2 = 0$, $t_1 = 0, t_2 = 1$. At each row the old pair shifts diagonally.

![Hand-written Extended Euclidean Algorithm table tracking Bezout coefficients s and t for gcd(275, 200) (Shishir Notes p. 84)](diagrams/dm5_extended_euclidean_bezout_table.jpg)

The table Shishir shows, for $\gcd(275, 200)$:

| $q$ | $a$ | $b$ | $r$ | $s_1$ | $s_2$ | $s = s_1 - s_2 q$ | $t_1$ | $t_2$ | $t = t_1 - t_2 q$ |
| --: | --: | --: | --: | --: | --: | :-- | --: | --: | :-- |
| 1 | 275 | 200 | 75 | 1 | 0 | $1 - 0(1) = 1$ | 0 | 1 | $0 - 1(1) = -1$ |
| 2 | 200 | 75 | 50 | 0 | 1 | $0 - 1(2) = -2$ | 1 | -1 | $1 - (-1)(2) = 3$ |
| 1 | 75 | 50 | 25 | 1 | -2 | $1 - (-2)(1) = 3$ | -1 | 3 | $-1 - 3(1) = -4$ |
| 2 | 50 | 25 | 0 | -2 | 3 | $-2 - 3(2) = -8$ | 3 | -4 | $3 - (-4)(2) = 11$ |
| - | **25** | 0 | - | **3** | -8 | - | **-4** | 11 | - |

Extracted values: $\gcd(275, 200) = 25$, coefficient of $275$ is $s = 3$, coefficient of $200$ is $t = -4$. Check: $3(275) - 4(200) = 825 - 800 = 25$.

> [!WARNING] Both teachers say this is self-study
> Fahad: "Extended Euclidean Algorithm is marked for self-study and is best practiced in tabular form." Raidah: "Extended Euclidean Algorithm -> Self-study topic, best practiced and prepared in tabular format." If the exam asks for it, the table form above is the one to have rehearsed, because both note sets gesture at it without walking through the arithmetic.

### Worked Example (PYQ 2022 Q.7(c))

> **Source:** 2022 Q.7(c)

**Question.** Find the greatest common divisor of 414 and 662 using the extended Euclidean algorithm.

**Solution.**

**Step 1. Ordinary Euclidean algorithm.**

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

The last nonzero remainder is $2$, so $\gcd(414, 662) = 2$.

**Step 2. Extended part, back-substituting** to find integers $s, t$ with $414s + 662t = 2$.

From the last division, $2 = 166 - 2 \times 82$.

Substitute $82 = 248 - 166$:

$$
2 = 166 - 2(248 - 166) = 3 \times 166 - 2 \times 248
$$

Substitute $166 = 414 - 248$:

$$
2 = 3(414 - 248) - 2 \times 248 = 3 \times 414 - 5 \times 248
$$

Substitute $248 = 662 - 414$:

$$
2 = 3 \times 414 - 5(662 - 414) = 8 \times 414 - 5 \times 662
$$

**Check.**

$$
8(414) - 5(662) = 3312 - 3310 = 2
$$

$$
\boxed{\gcd(414, 662) = 2, \qquad 8(414) - 5(662) = 2}
$$

> [!info] Check by an independent route
> The forward extended Euclidean algorithm, which carries the coefficients $(s, t)$ alongside the remainders rather than back-substituting, returns $(2, 8, -5)$: gcd $2$, $s = 8$, $t = -5$. Same answer, and the identity $8 \times 414 + (-5) \times 662 = 2$ verifies it.

**The back-substitution done in tabular form**, which is what the note sets push:

| $q$ | $a$ | $b$ | $r$ | $s_1$ | $s_2$ | $s$ | $t_1$ | $t_2$ | $t$ |
| --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 662 | 414 | 248 | 1 | 0 | $1 - 0(1) = 1$ | 0 | 1 | $0 - 1(1) = -1$ |
| 1 | 414 | 248 | 166 | 0 | 1 | $0 - 1(1) = -1$ | 1 | -1 | $1 - (-1)(1) = 2$ |
| 1 | 248 | 166 | 82 | 1 | -1 | $1 - (-1)(1) = 2$ | -1 | 2 | $-1 - 2(1) = -3$ |
| 2 | 166 | 82 | 2 | -1 | 2 | $-1 - 2(2) = -5$ | 2 | -3 | $2 - (-3)(2) = 8$ |
| 41 | 82 | 2 | 0 | 2 | -5 | - | -3 | 8 | - |

Reading the last computed row gives $\gcd = 2$, with the coefficient column showing $s = -5$ for $662$ and $t = 8$ for $414$. That is $8(414) - 5(662) = 2$, the same identity the back-substitution produced.

### LCM and the Product Identity

$$
\text{lcm}(a, b) = \frac{ab}{\gcd(a, b)}
$$

For $a = 414$ and $b = 662$: $\text{lcm} = \dfrac{414 \times 662}{2} = 137{,}034$. The product identity behind it is $ab = \gcd(a, b) \cdot \text{lcm}(a, b)$.

---

## DM-5.6: Fermat's Little Theorem

### The statement

If $p$ is prime and $p \nmid a$, then

$$
a^{p-1} \equiv 1 \pmod p
$$

and equivalently, for **every** integer $a$ with no coprimality condition at all,

$$
a^p \equiv a \pmod p
$$

> [!NOTE] The two forms are not equally useful
> The $a^p \equiv a$ form needs no coprimality condition but is harder to exploit. The $a^{p-1} \equiv 1$ form is the one that reduces exponents, and it requires $p \nmid a$. Working cases: $2^2 = 4 \equiv 1 \pmod 3$, and $4^4 = 256 \equiv 1 \pmod 5$.

**What it buys you.** Reduce a large exponent modulo $p - 1$. Since $\phi(p) = p - 1$ for a prime $p$, write $n = q(p-1) + r$ with $0 \le r < p-1$, then

$$
a^n = \left(a^{p-1}\right)^q a^r \equiv 1^q a^r = a^r \pmod p
$$

This is exactly what the CRT cross-check in [DM-5.5](DM-5.5_Modular_Exponentiation.md) uses to handle $3^{644}$ modulo $43$.

**The converse is false and the exam may test it.** If $a^{n-1} \equiv 1 \pmod n$ and $n$ is composite, then $n$ is a **pseudoprime to base $a$**. The smallest one is $341 = 11 \times 31$, since $2^{340} \equiv 1 \pmod{341}$ despite $341$ being composite.

### Worked Example (PYQ 2022 Q.8(a), part one)

> **Source:** 2022 Q.8(a)

**Question.** Define Fermat's little theorem.

**Solution.**

**Fermat's little theorem.** If $p$ is prime and $\gcd(a, p) = 1$, then

$$
\boxed{a^{p-1} \equiv 1 \pmod p}
$$

Equivalently $a^p \equiv a \pmod p$ for every integer $a$, with no coprimality condition needed. A worked case: $2^2 = 4 \equiv 1 \pmod 3$, and $4^4 = 256 \equiv 1 \pmod 5$.

---

## DM-5.7: Chinese Remainder Theorem

### What it claims

Given pairwise coprime moduli $n_1, \dots, n_k$ and a system $x \equiv a_i \pmod{n_i}$, there is **exactly one** solution modulo $N = n_1 n_2 \cdots n_k$.

### The construction formula

$$
M_i = \frac{N}{n_i}, \qquad u_i = M_i^{-1} \pmod{n_i}, \qquad x = \sum_{i=1}^{k} a_i u_i M_i \pmod N
$$

$M_i$ is the product of all moduli **except** $n_i$. Since $\gcd(M_i, n_i) = 1$, an inverse $u_i$ always exists. The formula is designed so that the $i$th term is congruent to $a_i$ modulo $n_i$ and to $0$ modulo every other $n_j$.

### How to find the inverse quickly

Shishir notes p. 88 give the method the students actually use: test $u = 1, 2, 3, \dots$ until $M_i u - 1$ is divisible by $n_i$. Since the moduli in the exam are small, this beats reaching for the Extended Euclidean Algorithm.

| $M_i$ | $n_i$ | $M_i \bmod n_i$ | Solve | $u_i$ |
| --: | --: | --: | :-- | --: |
| 20 | 3 | 2 | $2u \equiv 1$ | 2 |
| 15 | 4 | 3 | $3u \equiv 1$ | 3 |
| 12 | 5 | 2 | $2u \equiv 1$ | 3 |

### Worked Example (PYQ 2022 Q.8(a))

> **Source:** 2022 Q.8(a)

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

**Check:** $5 \bmod 3 = 2$ and $5 \bmod 4 = 1$.

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

**Verify all three.**

$$
53 \bmod 3 = 2 \quad \checkmark \qquad 53 \bmod 4 = 1 \quad \checkmark \qquad 53 \bmod 5 = 3 \quad \checkmark
$$

Since $N = 3 \cdot 4 \cdot 5 = 60$, the complete solution set is $x = 53 + 60k$ for every integer $k$.

> [!info] Check by exhaustive search
> Testing every residue $x$ from 0 to 59 against all three congruences returns exactly one, namely $53$. Hence the solution is unique modulo 60, which is what CRT guarantees when the moduli are pairwise coprime. Note that $4$ is **not** prime, so Fermat does not apply to it, but coprimality is all CRT needs and $\gcd(3,4) = \gcd(4,5) = \gcd(3,5) = 1$.

> [!note] Solving by inspection as a check
> $x \equiv 1 \pmod 4$ and $x \equiv 3 \pmod 5$ together give $x \equiv 13 \pmod{20}$. Values below 60 are $13, 33, 53$. Of these only $53$ is $2 \pmod 3$.

**Why $M_j \equiv 0 \pmod{n_k}$ when $j \ne k$.** $M_j$ is the product of all moduli except $n_j$, so $n_k$ appears as one of its factors whenever $j \ne k$. That single observation is why the CRT sum works: every term except the $k$th vanishes modulo $n_k$, leaving exactly $a_k$.

**The iterative method, which is easier under time pressure.** Combine two congruences at a time as shown above, growing $x$ from $x \equiv 5 \pmod{12}$ to $x \equiv 53 \pmod{60}$. Both routes give 53. If the moduli are small, this is shorter than computing three inverses.

---

## Exam Variants

| Year | Question | Task | Key Answer |
| :--- | :--- | :--- | :--- |
| 2023 Q.7(c) | Prove the prime divisor bound | direct proof, WLOG, Euclid's Lemma | $\boxed{\text{Every composite } n \text{ has a prime divisor } p \text{ with } p \le \sqrt{n}}$ |
| 2022 Q.7(c) | gcd(414, 662) by the extended algorithm ⚠️ | forward divisions plus back substitution | $\boxed{\gcd(414, 662) = 2, \qquad 8(414) - 5(662) = 2}$ |
| 2022 Q.8(a) | State FLT, then solve a CRT system | construction formula, then verify | $\boxed{a^{p-1} \equiv 1 \pmod p}$ and $\boxed{x \equiv 53 \pmod{60}}$ |

**PYQ coverage for DM-5.2, DM-5.3, DM-5.6, DM-5.7:** 3 exam questions, 3 blocks, 0 missing.

---

## ⚡ Exam Tips & Common Mistakes

1. **State FLT with its condition.** "$a^{p-1} \equiv 1 \pmod p$ for $p$ prime and $p \nmid a$". Dropping the coprimality clause loses a mark, and the $a^p \equiv a$ form does not need it.
2. **Never say "coprime moduli" and mean "prime moduli".** The 2022 CRT system has modulus 4, which is not prime, and CRT still applies. Pairwise coprimality is the whole requirement.
3. **Always reduce the CRT answer modulo $N$.** $233$ is a valid representative but $233 > 60$. The question wants the solution modulo $60$, so write $53$.
4. **Write the inverse hunt as a table.** Three rows of "$M_i \bmod n_i$, solve, get $u_i$" is faster than three separate derivations.
5. **For the extended algorithm, name both parts.** "Step 1: ordinary algorithm, gives 2. Step 2: back substitution." The coefficients carry separate marks and they are easy to forget.
6. **Check the Bezout identity numerically.** $8 \times 414 - 5 \times 662 = 3312 - 3310 = 2$. One line, and it turns a possible sign error into a visible one.
7. **Trial division stops at $\sqrt{n}$.** Testing divisors past the square root is not just wasted effort, it signals that you have forgotten the bound.
8. **In a prime divisor proof, do not skip the "every $a > 1$ has a prime divisor" step.** That step is the part being examined, and skipping it leaves a gap a marker will notice.

## 🔗 Related Topics

- [DM-5.5: Modular Exponentiation](DM-5.5_Modular_Exponentiation.md) — previous in the chain, where Fermat reduces the exponent and CRT checks the answer
- [DM-5_Lower_b: Bases and Proofs](DM-5_Lower_b_Bases_Proofs.md) — next in the chain, the last file of the number theory block
- [DM-5.4: Modular Arithmetic and Congruence](DM-5.4_Modular_Arithmetic_and_Congruence.md) — the congruence algebra every proof here depends on

---

[← Previous: DM-5.5 Modular Exponentiation](DM-5.5_Modular_Exponentiation.md) | [🏠 Index](00_Index.md) | [Next: DM-5 Lower-b: Bases and Proofs →](DM-5_Lower_b_Bases_Proofs.md)