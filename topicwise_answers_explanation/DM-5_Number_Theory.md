---
title: "DM-5 · Number Theory & Cryptography"
tags:
  - numerical-methods
  - discrete-mathematics
  - topicwise-clusters
---

[🏠 Master Index](00_Index.md) | [← Prev Topic: DM-3 · Propositional Logic](DM-3_Propositional_Logic.md) | [Next Topic: DM-6 · Counting →](DM-6_Counting_and_Combinatorics.md)

---

# DM-5 · Number Theory & Cryptography

> **Topic ID:** DM-5  
> **Section:** Section B -- Discrete Mathematics  
> **Exam Weight:** 🔴 High Priority (Tier 1) | 3/3 Years (2022–2024) (100% Frequency) | Typical Weight: 10–14 marks (Question 6/7)  
> **Subtopics Included:** 7 subtopics (DM-5.2 through DM-5.9)  
> **Origin Layer:** Authored in `../answers_explanation/`. All numerical results and boxed equations match character-for-character.

---

## 📑 Subtopics Covered in this Cluster

| Subtopic ID | Subtopic Title | Priority | Exam Frequency | Section Navigation |
|:---|:---|:---:|:---:|:---|
| **DM-5.2** | Prime Numbers | 🟠 | 2023 | [Jump to DM-5.2](#dm-52) |
| **DM-5.3** | GCD, LCM & Euclidean Algorithm | 🟠 ⚠️ | 2022 | [Jump to DM-5.3](#dm-53) |
| **DM-5.4** | Modular Arithmetic & Congruence | 🔴 | 2022, 2023, 2024 | [Jump to DM-5.4](#dm-54) |
| **DM-5.5** | Modular Exponentiation | 🔴 | 2022, 2024 | [Jump to DM-5.5](#dm-55) |
| **DM-5.7** | Chinese Remainder Theorem | 🟠 | 2022 | [Jump to DM-5.7](#dm-57) |
| **DM-5.8** | Number Bases & Binary Arithmetic | 🟡 | 2023 | [Jump to DM-5.8](#dm-58) |
| **DM-5.9** | Number-Theoretic Proofs | 🟠 | 2022, 2023 | [Jump to DM-5.9](#dm-59) |

---

<a id="dm-52"></a><a id="dm-5.2"></a>
## DM-5.2 · Prime Numbers

### [2023 Q.7(c)]

**Question.** If $n$ is a composite integer then $n$ has a prime divisor less than or equal to $\sqrt{n}$.

*[Marks: 03, CO: 2]*

**Solution.**

**Proof.**

Let $n$ be composite. Then by definition $n = ab$ for integers $a, b$ with
$1 < a < n$ and $1 < b < n$.

**Key observation.** At least one of $a$ and $b$ is at most $\sqrt{n}$. Suppose
both were larger:

$$
a > \sqrt{n} \quad \text{and} \quad b > \sqrt{n} \quad \Longrightarrow \quad ab > \sqrt{n}\sqrt{n} = n
$$

Since $ab = n$, this is a contradiction. Hence $a \le \sqrt{n}$ or
$b \le \sqrt{n}$. Without loss of generality suppose $a \le \sqrt{n}$, so
$1 < a \le \sqrt{n}$.

**Now find a prime divisor at most $a$.** Every integer $a > 1$ has a prime
divisor: keep dividing by a prime factor until the result is 1, and the last
prime divided out is a prime $p$ dividing $a$. So there is a prime $p$ with
$p \mid a$.

Since $a \mid n$ and $p \mid a$, transitivity of divisibility gives $p \mid n$. And
$p \le a \le \sqrt{n}$.

$$
\boxed{\text{Every composite } n \text{ has a prime divisor } p \text{ with } p \le \sqrt{n}}
$$

> [!note] Why this matters
> This is the fact that makes trial division for factorisation terminate at
> $\sqrt{n}$ instead of at $n$. Without it you would test every integer up to $n$,
> which is about as slow as factoring can be; with it you test only up to the square
> root, which is the square root of the work. It is the reason a primality test
> runs in milliseconds rather than minutes.
>
> Worked examples: $91 = 7 \times 13$ with $\sqrt{91} = 9.539$, and the prime
> divisor $7$ is indeed below it. $97$ is prime, so the statement does not apply
> to it, which is why a trial division up to $9$ establishes its primality.

> [!warning] The precise statement is *at most*, not *less than*
> $p \le \sqrt{n}$, not $p < \sqrt{n}$. The equality case is real: $n = 49 = 7^2$
> has the prime divisor $7 = \sqrt{49}$. Getting this boundary wrong loses the
> proof of the $n = 4$, $9$, $25$, $49$ cases, and more importantly it loses the
> marks for precision in a question whose whole content is the inequality.
>
> The proof is also worth understanding structurally, because the key move is
> cheap: **if $ab = n$ then $\min(a, b) \le \sqrt{n}$**, since otherwise the product
> would exceed $n$. Every elementary factorisation algorithm is built on that one
> line.

---

<a id="dm-53"></a><a id="dm-5.3"></a>
## DM-5.3 · GCD, LCM & Euclidean Algorithm

### [2022 Q.7(c)]

**Question.** Find the greatest common divisor of 414 and 662 using the extended Euclidean algorithm.

*[Marks: 02, CO: 2]*

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

**Step 2. Extended part, back-substituting** to find integers $s, t$ with
$414s + 662t = 2$.

From the last division, $2 = 166 - 2 \times 82$. Substitute $82 = 248 - 166$:

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
8(414) - 5(662) = 3312 - 3310 = 2 \quad \checkmark
$$

$$\boxed{\gcd(414, 662) = 2, \qquad 8(414) - 5(662) = 2}$$

> [!info] The forward method gives the same coefficients
> The forward extended Euclidean algorithm, which carries the coefficients
> $(s, t)$ alongside the remainders rather than back-substituting, returns
> $(2, 8, -5)$: gcd $2$, $s = 8$, $t = -5$. The identity
> $8 \times 414 + (-5) \times 662 = 2$ verifies it.

> [!note] Why the extended form is worth the extra work
> Ordinary Euclid gives the gcd. The extended form also gives the Bezout
> coefficients $s$ and $t$, and that is what modular inverses are built from: if
> $\gcd(a, n) = 1$ then $sa + tn = 1$, so $s$ is the inverse of $a$ modulo $n$.
>
> Solving congruences by hand almost always needs this, so the question is really
> marking one skill that pays for itself in the parts to come.
>
> One habit saves time here: because $414$ and $662$ are both even, the gcd is
> even, which flags $2$ as plausible before the last division is reached.

---

<a id="dm-54"></a><a id="dm-5.4"></a>
## DM-5.4 · Modular Arithmetic & Congruence

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

<a id="dm-55"></a><a id="dm-5.5"></a>
## DM-5.5 · Modular Exponentiation

### [2022 Q.7(b), 2024 Q.8(b)]

**Appeared in:** 2022 Q.7(b), 2024 Q.8(b)

**Question.** Solve $3^{644} \bmod 645$ using a well-known algorithm.

*[Marks: 03, CO: 3]*

**Solution.**

The well-known algorithm is **repeated squaring**, also called the
square-and-multiply method. It exploits $x^{2k} = (x^k)^2$, so each squaring
roughly doubles the exponent covered while the numbers stay small.

**Step 1. Binary expansion of the exponent.**

$$
644 = 512 + 128 + 4 = (1010000100)_2
$$

**Step 2. Square repeatedly, reducing modulo 645 at every step.**

$$
3^1 = 3
$$

$$
3^2 = 9
$$

$$
3^4 = 9^2 = 81
$$

$$
3^8 = 81^2 = 6561 = 645(10) + 111 \equiv 111
$$

$$
3^{16} = 111^2 = 12321 = 645(19) + 66 \equiv 66
$$

$$
3^{32} = 66^2 = 4356 = 645(6) + 486 \equiv 486
$$

$$
3^{64} = 486^2 = 236196 = 645(366) + 126 \equiv 126
$$

$$
3^{128} = 126^2 = 15876 = 645(24) + 396 \equiv 396
$$

$$
3^{256} = 396^2 = 156816 = 645(243) + 81 \equiv 81
$$

$$
3^{512} = 81^2 = 6561 \equiv 111
$$

**Step 3. Multiply the powers named by the set bits**, which are
$2^9 = 512$, $2^7 = 128$ and $2^2 = 4$:

$$
3^{644} \equiv 3^{512} \cdot 3^{128} \cdot 3^4
$$

$$
= 111 \times 396 \times 81
$$

$$
111 \times 396 = 43956 = 645(68) + 96 \equiv 96
$$

$$
96 \times 81 = 7776 = 645(12) + 36 \equiv 36
$$

$$\boxed{3^{644} \bmod 645 = 36}$$

> [!info] A completely different route, by the Chinese remainder theorem
> Factor $645 = 3 \times 5 \times 43$ and work modulo each prime:
>
> | Modulus | Result | Working |
> | :-- | :-- | :-- |
> | $3$ | 0 | $3^{644}$ is a multiple of 3 |
> | $5$ | 1 | $3^4 \equiv 1$ and $644 = 4(161)$ |
> | $43$ | 36 | $\phi(43) = 42$, $644 = 42(15)+14$, so $3^{644} \equiv 3^{14} = 3^8 \cdot 3^4 \cdot 3^2 \equiv 25 \times 38 \times 9 \equiv 36$ |
>
> Checking $36$: $36 \bmod 3 = 0$ ✓, $36 \bmod 5 = 1$ ✓, $36 \bmod 43 = 36$ ✓.
> Both routes give $36$, which is a genuine confirmation because they share no
> intermediate arithmetic.

> [!warning] Two traps in this computation
> **Do not let the residues grow.** Reducing after every squaring is what keeps
> the largest intermediate at $486^2 = 236196$. Squaring without reducing reaches
> $3^{644}$ with about $307$ digits, which is not wrong so much as pointless.
>
> **$3^{256} \equiv 81$ is not a typo.** The sequence is periodic in a way that
> looks wrong at first glance, and $81 = 3^4$ is exactly what makes $3^{512}$
> come out equal to $3^8$. If one of these entries surprises you, recompute it
> rather than adjusting it to look tidier.

> [!note] Which algorithm the question means
> "A well-known algorithm" for modular exponentiation is repeated squaring.
> **Fermat's little theorem** would also work, via
> $3^{644} = 3^{\phi(645) + 164}$ with $\phi(645) = 268$, but the modulus is not
> prime, so the theorem only applies to each prime factor separately, which is
> the CRT route above rather than a single reduction.
>
> Repeated squaring is the right answer to the question as asked because it
> applies to any modulus, prime or not, and takes about $\log_2 644 = 10$
> squarings.

---

<a id="dm-57"></a><a id="dm-5.7"></a>
## DM-5.7 · Chinese Remainder Theorem

### [2022 Q.8(a)]

**Question.** Define Fermat's little theorem. Use the construction in the proof of the Chinese remainder theorem to find all solutions to $x \equiv 2 \pmod 3$, $x \equiv 1 \pmod 4$, $x \equiv 3 \pmod 5$.

*[Marks: 04, CO: 2]*

**Solution.**

**Fermat's little theorem.** If $p$ is prime and $\gcd(a, p) = 1$, then

$$\boxed{a^{p-1} \equiv 1 \pmod p}$$

Equivalently $a^p \equiv a \pmod p$ for every integer $a$, with no coprimality
condition needed. Worked cases: $2^2 = 4 \equiv 1 \pmod 3$, and
$4^4 = 256 \equiv 1 \pmod 5$.

**The CRT construction.** For moduli $n_1, n_2, \dots, n_k$ that are pairwise
coprime, put $N = n_1 n_2 \cdots n_k$ and

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

**Alternative verification: combining two congruences at a time.** Combine the first two,
$x \equiv 2 \pmod 3$ and $x \equiv 1 \pmod 4$. Write $x = 2 + 3k$ and substitute
into the second:

$$
2 + 3k \equiv 1 \pmod 4 \quad \Longrightarrow \quad 3k \equiv -1 \equiv 3 \pmod 4
$$

Since $3^{-1} \equiv 3 \pmod 4$, $k \equiv 3 \times 3 = 9 \equiv 1 \pmod 4$. Hence
$k = 1 + 4m$ and

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

$$\boxed{x \equiv 53 \pmod{60}}$$

**Verify all three.**

$$
53 \bmod 3 = 2 \quad \checkmark \qquad 53 \bmod 4 = 1 \quad \checkmark \qquad 53 \bmod 5 = 3 \quad \checkmark
$$

Since $N = 3 \cdot 4 \cdot 5 = 60$, the complete solution set is $x = 53 + 60k$
for every integer $k$.

> [!info] Exhaustive search confirms uniqueness
> Testing every residue $x$ from 0 to 59 against all three congruences returns
> exactly one, namely $53$. The solution is therefore unique modulo 60, which is
> what CRT guarantees when the moduli are pairwise coprime.
>
> Note that $4$ is **not** prime, so Fermat does not apply to it. Coprimality is
> all CRT needs, and $\gcd(3,4) = \gcd(4,5) = \gcd(3,5) = 1$.

> [!note] Solving by inspection, as a cheaper check
> $x \equiv 1 \pmod 4$ and $x \equiv 3 \pmod 5$ together give $x \equiv 13 \pmod{20}$.
> The values below 60 are $13$, $33$, $53$, and of those only $53$ is $2 \pmod 3$.
>
> For three small congruences this is faster than the general construction, and
> it is a good check on the formula-based route because it shares none of its
> arithmetic.

> [!warning] Fermat needs the modulus to be prime, and coprimality on the base
> Two conditions, both easy to forget. $2^{10} \equiv 2 \pmod{10}$ does not give
> $2^9 \equiv 1 \pmod{10}$, because $10$ is not prime. And $a \equiv 0 \pmod p$ has
> no inverse, so the coprimality requirement is genuine rather than a technicality.
>
> When a modulus is composite but its factors are known, the route is to reduce
> modulo each prime factor separately and combine, which is what the CRT route
> does.

---

<a id="dm-58"></a><a id="dm-5.8"></a>
## DM-5.8 · Number Bases & Binary Arithmetic

### [2023 Q.7(b)]

**Question.** Add $a = (1110)_2$ and $b = (1011)_2$.

*[Marks: 03, CO: 2]*

**Solution.**

**Method 1, positional value.**

$$
(1110)_2 = 1(2^3) + 1(2^2) + 1(2^1) + 0(2^0) = 8 + 4 + 2 + 0 = 14
$$

$$
(1011)_2 = 1(2^3) + 0(2^2) + 1(2^1) + 1(2^0) = 8 + 0 + 2 + 1 = 11
$$

$$
14 + 11 = 25
$$

Convert back: $25 = 16 + 8 + 1 = (11001)_2$.

**Method 2, binary addition, column by column.**

| Column | $2^4$ | $2^3$ | $2^2$ | $2^1$ | $2^0$ |
| :-- | :-: | :-: | :-: | :-: | :-: |
| **Carry row** | 1 | 1 | 1 | 0 | - |
| $a$ | 0 | 1 | 1 | 1 | 0 |
| $b$ | 0 | 1 | 0 | 1 | 1 |
| **Sum** | **1** | **1** | **0** | **0** | **1** |

Working right to left:

- $2^0$: $0 + 1 = 1$, write 1, carry 0
- $2^1$: $1 + 1 = 2$, write 0, carry 1
- $2^2$: $1 + 0 + 1 = 2$, write 0, carry 1
- $2^3$: $1 + 1 + 1 = 3$, write 1, carry 1 into $2^4$

$$
\boxed{(1110)_2 + (1011)_2 = (11001)_2 = 25_{10}}
$$

> [!info] What confirms the result
> Expand the result back to base 10:
> $(11001)_2 = 1(2^4) + 1(2^3) + 0(2^2) + 0(2^1) + 1(2^0) = 16 + 8 + 0 + 0 + 1 = 25$,
> which matches $14 + 11 = 25$.
>
> Both methods agree on 25, and the round trip is a complete check: positional
> value in, addition, positional value out.
>
> Note that $2^4$ appears in the answer, so the sum needs **five** bits.
> $14 + 11 = 25 > 15 = (1111)_2$, the largest four-bit value. This is overflow in
> four-bit arithmetic, so the result must be stored in five bits. That is the
> practical point of the question, and it is worth stating explicitly.

> [!warning] Carries are the only part that needs care
> The addition itself is trivial; the carries are where slips happen. Working
> right to left:
> $2^0$: $0 + 1 = 1$, write 1, **carry 0**.
> $2^1$: $1 + 1 = 2$, write 0, **carry 1**.
> $2^2$: $1 + 0 + 1 = 2$, write 0, **carry 1**.
> $2^3$: $1 + 1 + 1 = 3$, write 1, **carry 1** into $2^4$.
>
> Forgetting to add the incoming carry into the next column is the classic slip,
> and it is the only place where this problem can go wrong. Write the carry row
> explicitly in the table, as above, rather than holding it in your head.

---

<a id="dm-59"></a><a id="dm-5.9"></a>
## DM-5.9 · Number-Theoretic Proofs

### [2022 Q.7(d)]

**Question.** Show that if $a$ and $b$ are positive integers then $(2^a - 1) \bmod (2^b - 1) \equiv 2^{a \bmod b} - 1$.

*[Marks: 02, CO: 2]*

**Solution.**

**Step 1. Write $a = qb + r$** with $q = \lfloor a/b \rfloor \ge 0$ and
$r = a \bmod b$, so $0 \le r < b$.

**Step 2. Reduce the power.**

$$
2^a - 1 = 2^{qb+r} - 1 = 2^r\left(2^{qb}\right) - 1
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

Since $r = a \bmod b$:

$$\boxed{(2^a - 1) \bmod (2^b - 1) \equiv 2^{a \bmod b} - 1}$$

**Step 5. The residue really is the least one.** Since $0 \le r < b$ we have
$0 \le 2^r - 1 < 2^b - 1$, so $2^r - 1$ is the actual remainder and not merely a
congruent value. This is what makes the statement an equality of remainders rather
than only a congruence.

> [!info] Worked cases
> | $a$ | $b$ | $(2^a-1) \bmod (2^b-1)$ | $2^{a \bmod b} - 1$ |
> | --: | --: | --: | --: |
> | 13 | 5 | 7 | 7 |
> | 10 | 3 | 1 | 1 |
> | 20 | 6 | 3 | 3 |
> | 9 | 4 | 1 | 1 |
> | 7 | 7 | 0 | 0 |
>
> The identity was checked directly for every pair with $1 \le a \le 29$ and
> $1 \le b \le 11$, with no counterexample. The $a = b$ row is the boundary case
> worth noting: $a \bmod b = 0$ and $2^0 - 1 = 0$, which is correct since
> $2^b - 1$ divides itself.

> [!note] The general result, and why it matters
> Nothing above used anything specific to the base $2$. The identical proof works
> for any base $c$:
> $(c^a - 1) \bmod (c^b - 1) \equiv c^{a \bmod b} - 1$.
>
> This is the standard trick for simplifying large modular exponentiations, and it
> is why $3^{644} \bmod 645$ in part (b) collapses so cheaply whenever the modulus
> happens to have the form $c^k - 1$. $645$ is not of that form, which is exactly
> why (b) needs repeated squaring instead.

---

---

**Also asked here.**

- *2022 Q.8(d)* is the same question as [[DM-6.3_Pigeonhole_Principle|DM-6.3]], which is written in `DM-6.3`.
- *2023 Q.7(c)* is the same question as [[DM-5.2_Prime_Numbers|DM-5.2]], which is written in `DM-5.2`.

---

[🏠 Master Index](00_Index.md) | [← Prev Topic: DM-3 · Propositional Logic](DM-3_Propositional_Logic.md) | [Next Topic: DM-6 · Counting →](DM-6_Counting_and_Combinatorics.md)
