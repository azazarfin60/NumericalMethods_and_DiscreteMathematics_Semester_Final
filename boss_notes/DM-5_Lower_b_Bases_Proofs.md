[← Previous: DM-5 Lower-a: Primes, GCD, Fermat, CRT](DM-5_Lower_a_Primes_GCD_Fermat_CRT.md) | [🏠 Index](00_Index.md) | [Next: DM-6.3 Pigeonhole Principle →](DM-6.3_Pigeonhole_Principle.md)

---

# DM-5 Lower-b: Bases and Proofs
> **Section:** B (Discrete Mathematics) | **Priority:** 🟠🟡 (mixed) | **Exam Frequency:** 2/3 DM papers (2022 Q.7(d), 2023 Q.7(b))
> **Subtopics:** DM-5.8 (Number Bases and Binary Arithmetic), DM-5.9 (Number-Theoretic Proofs)
> **Sources:** Rosen §4.2 (pp. 14–16, Theorem 1, Figure 1), §4.1, Fahad Notes Class-19, Raidah Notes §5, Shishir Notes §1, §5.1

## Why This Topic Matters

Two small subtopics with one question each. 2023 Q.7(b) asked for a binary addition and took it straight from Rosen's own figure, carries and all. 2022 Q.7(d) asked for a congruence proof with a clean structure: divide the exponent, kill the big power, check the bound. Both are five-minute questions once you see the shape.

---

## 📝 Key Definitions

> **Base $b$ representation:** "**Theorem 1.** Let $b$ be an integer greater than 1. Then if $n$ is a positive integer, it can be expressed uniquely in the form $n = a_k b^k + a_{k-1} b^{k-1} + \dots + a_1 b + a_0$, where $k$ is a nonnegative integer, $a_0, a_1, \dots, a_k$ are nonnegative integers less than $b$, and $a_k \neq 0$." — Rosen, §4.2 (p. 14)

> **Binary representation:** "the base 2 representation of an integer." — Rosen, §4.2, Key Terms (p. 14). "In binary notation each digit is either a 0 or a 1. In other words, the binary expansion of an integer is just a bit string." — Rosen, §4.2 (p. 14)

> **Why computers use it:** "Binary expansions (and related expansions that are variants of binary expansions) are used by computers to represent and do arithmetic with integers." — Rosen, §4.2 (p. 14)

> **The addition algorithm:** "where $s_0$ is the rightmost bit in the binary expansion of $a + b$ and $c_0$ is the carry, which is either 0 or 1. Then add the next pair of bits and the carry, ... At the last stage, add $a_{n-1}, b_{n-1},$ and $c_{n-2}$ to obtain $c_{n-1} \cdot 2 + s_{n-1}$. The leading bit of the sum is $s_n = c_{n-1}$." — Rosen, §4.2, Addition Algorithm (p. 15)

> **Mersenne number:** "A **Mersenne number** is a number of the form $M_n = 2^n - 1$, where $n$ is a prime number. If $M_n$ is itself prime, it is called a **Mersenne prime**." — Shishir Notes §5.1 (p. 86). Rosen's Key Terms list it as "**Mersenne prime:** a prime of the form $2^p - 1$, where $p$ is prime" (§4.3, p. 20).

> **The Mersenne warning:** if $n$ is composite, then $2^n - 1$ is always composite. But $n$ prime is necessary and not sufficient: $2^{11} - 1 = 2047 = 23 \times 89$. — Shishir Notes §5.1 (p. 86)

---

## DM-5.8: Number Bases and Binary Arithmetic

### Positional value

Every base-$b$ numeral is a weighted sum. The rightmost digit has weight $b^0$, the next $b^1$, and so on.

$$
(a_k a_{k-1} \dots a_1 a_0)_b = a_k b^k + a_{k-1} b^{k-1} + \dots + a_1 b + a_0
$$

Worked conversion, $(1\ 0101\ 1111)_2$ (Rosen §4.2, p. 14):

$$
(1\ 0101\ 1111)_2 = 2^9 + 2^6 + 2^4 + 2^3 + 2^2 + 2^1 + 2^0 = 512 + 64 + 16 + 8 + 4 + 2 + 1 = 607
$$

**Converting decimal to base 2** runs the other way: divide by 2 repeatedly and read the remainders from the bottom up. Rosen's Algorithm 1 (p. 15) does exactly this.

| $n$ | $q = n \text{ div } 2$ | $n \bmod 2$ |
| --: | --: | :-: |
| 19 | 9 | 1 |
| 9 | 4 | 1 |
| 4 | 2 | 0 |
| 2 | 1 | 0 |
| 1 | 0 | 1 |

Reading the last column from the bottom: $(10011)_2 = 19$.

### Binary addition, and the only thing that can go wrong

The addition itself is trivial. The **carries** are where slips happen.

![Adding (1110)₂ and (1011)₂ to give (11001)₂, showing the carry row 1 1 1 above the sum (Rosen §4.2, Figure 1, p. 15)](diagrams/dm5_binary_addition_carry_model.jpg)

The rule at every column:

$$
\text{write} \;(\text{bit}_a + \text{bit}_b + \text{carry}) \bmod 2, \qquad
\text{next carry} = \left\lfloor \frac{\text{bit}_a + \text{bit}_b + \text{carry}}{2} \right\rfloor
$$

| $a + b$ + carry | bit written | carry out |
| --: | :-: | :-: |
| 0 | 0 | 0 |
| 1 | 1 | 0 |
| 2 | 0 | 1 |
| 3 | 1 | 1 |

> [!WARNING] The one classic slip
> Forgetting to add the **incoming** carry into the next column. Write the carry on the row above and read it down. That is the whole reason the figure shows a separate carry row.

### Worked Example (PYQ 2023 Q.7(b))

> **Source:** 2023 Q.7(b)

**Question.** Add $a = (1110)_2$ and $b = (1011)_2$.

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

> [!info] Check
> Expand the result back to base 10:
> $(11001)_2 = 1(2^4) + 1(2^3) + 0(2^2) + 0(2^1) + 1(2^0) = 16 + 8 + 0 + 0 + 1 = 25$
> which matches $14 + 11 = 25$.
>
> Both methods agree on 25. Note that $2^4$ appears, so the sum needs five bits: $14 + 11 = 25 > 15 = (1111)_2$, the largest four-bit value. This is overflow in four-bit arithmetic, so the result must be stored in five bits.

> [!warning] Carries are the only part that needs care
> The addition itself is trivial; the carries are where slips happen. Working right to left:
> $2^0$: $0 + 1 = 1$, write 1, **carry 0**.
> $2^1$: $1 + 1 = 2$, write 0, **carry 1**.
> $2^2$: $1 + 0 + 1 = 2$, write 0, **carry 1**.
> $2^3$: $1 + 1 + 1 = 3$, write 1, **carry 1** into $2^4$.
> Forgetting to add the incoming carry into the next column is the classic slip, and it is the only place where this problem can go wrong.

**This question is Rosen's own Figure 1**, reproduced in §4.2 (p. 15) with the caption "Adding $(1110)_2$ and $(1011)_2$". Same numbers, same answer. The exam asks for both methods, which matches the fact that a good answer must show the positional meaning and the mechanical procedure.

**The three bases you need.**

| Base | Digits | Place values | $1011_2$ in decimal |
| :-- | :-- | :-- | --: |
| 2 | 0, 1 | $1, 2, 4, 8, 16, \ldots$ | 11 |
| 8 | 0 to 7 | $1, 8, 64, \ldots$ | $13_8$ |
| 16 | 0 to 9, A to F | $1, 16, 256, \ldots$ | $\mathrm{B}_{16}$ |

$1011_2 = 8 + 2 + 1 = 11 = 13_8 = \mathrm{B}_{16}$. A binary digit group maps onto one octal digit or one hex digit, which is why $3$ bits become one octal digit.

---

## DM-5.9: Number-Theoretic Proofs

This subtopic holds a single proof in the exam record, but the shape recurs. Learn the shape, not just the instance.

### The five-step shape for a congruence identity

1. **Divide.** Write the exponent with the division algorithm, $a = qb + r$, $0 \le r < b$.
2. **Expand.** Substitute into the expression.
3. **Annihilate.** Show the large factor is congruent to 1 (or 0) modulo the modulus.
4. **Substitute.** Collapse to a small expression.
5. **Bound.** Show the result is in $[0, m-1]$, so it is the actual remainder.

Step 5 is the one students skip, and it is what turns "a congruence" into "the remainder".

### Worked Example (PYQ 2022 Q.7(d))

> **Source:** 2022 Q.7(d)

**Question.** Show that if $a$ and $b$ are positive integers then $(2^a - 1) \bmod (2^b - 1) \equiv 2^{a \bmod b} - 1$.

**Solution.**

**Step 1. Write $a = qb + r$** with $q = \lfloor a/b \rfloor \ge 0$ and $r = a \bmod b$ so $0 \le r < b$. Then $a = qb + r$.

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

**Step 5. The residue really is the least one.** Since $0 \le r < b$ we have $0 \le 2^r - 1 < 2^b - 1$, so $2^r - 1$ is the actual remainder and not merely a congruent value. This is what makes the statement an equality of remainders rather than only a congruence.

> [!info] Check
> The identity was verified by direct computation for every pair with $1 \le a \le 29$ and $1 \le b \le 11$, with no counterexample. Worked cases:
>
> | $a$ | $b$ | $(2^a-1) \bmod (2^b-1)$ | $2^{a \bmod b} - 1$ |
> | --: | --: | --: | --: |
> | 13 | 5 | 7 | 7 |
> | 10 | 3 | 1 | 1 |
> | 20 | 6 | 3 | 3 |
> | 9 | 4 | 1 | 1 |
> | 7 | 7 | 0 | 0 |

> [!note] The general result
> Everything above used only the fact that $2^b \equiv 1$. The identical proof works for any base $c$: $(c^a - 1) \bmod (c^b - 1) \equiv c^{a \bmod b} - 1$. This is the standard trick for simplifying large modular exponentiations, and it is the reason $2^{644} \bmod 645$ in part (b) reduces so cheaply when the modulus factors into numbers of that shape.

**The worked cases, by hand, so you can check them.**

Take $a = 13$, $b = 5$. Then $2^{13} - 1 = 8191$ and $2^5 - 1 = 31$. Divide: $8191 = 31 \times 264 + 7$, so the remainder is 7. Meanwhile $13 \bmod 5 = 3$, and $2^3 - 1 = 7$. Match.

Take $a = 7$, $b = 7$. Then $2^7 - 1 = 127$ and $2^7 - 1 = 127$, so the remainder is 0. Meanwhile $7 \bmod 7 = 0$ and $2^0 - 1 = 0$. Match. The edge case $r = 0$ is the one to check, because it is where a student writes $2^0 - 1$ and forgets the minus one.

**The $r = 0$ boundary, handled.** When $b \mid a$ the formula gives remainder $2^0 - 1 = 0$. That is correct, since $2^b - 1$ divides $2^{qb} - 1$ whenever $b \mid qb$. Using the general formula $\dfrac{x^n - 1}{x - 1} = x^{n-1} + \dots + 1$ with $x = 2^b$ makes it immediate.

### The other proof in this subtopic

The prime divisor bound from [DM-5_Lower_a](DM-5_Lower_a_Primes_GCD_Fermat_CRT.md) is filed here in the taxonomy as well, since 2023 Q.7(c) touches both. It is a divisibility proof rather than a congruence proof, and it follows the same discipline: state the claim, find the contradiction assumption, name the law used at each step.

| Proof type | Core move | Law named at each step |
| :-- | :-- | :-- |
| Prime divisor bound | suppose both factors exceed $\sqrt n$, get $ab > n$ | Euclid's Lemma, transitivity of divisibility |
| $(2^a - 1) \bmod (2^b - 1)$ | write $a = qb + r$, kill $2^{qb}$ | Division Algorithm, congruence compatibility |

---

## Exam Variants

| Year | Question | Task | Key Answer |
| :--- | :--- | :--- | :--- |
| 2023 Q.7(b) | Add $(1110)_2$ and $(1011)_2$ | positional expansion **and** column addition with carries | $\boxed{(1110)_2 + (1011)_2 = (11001)_2 = 25_{10}}$ |
| 2022 Q.7(d) | Show $(2^a-1) \bmod (2^b-1) \equiv 2^{a \bmod b} - 1$ | division algorithm, annihilate $2^b$, bound the residue | $\boxed{(2^a - 1) \bmod (2^b - 1) \equiv 2^{a \bmod b} - 1}$ |

**PYQ coverage for DM-5.8, DM-5.9:** 2 exam questions, 2 blocks, 0 missing.

---

## ⚡ Exam Tips & Common Mistakes

1. **Show both methods for a binary addition.** 2023 Q.7(b) wanted the positional expansion and the column procedure. One alone loses half the marks.
2. **Write the carry row explicitly.** It is the only bookkeeping that matters, and it stops the missed-carry error.
3. **Check the bit width.** $14 + 11 = 25 > 15 = (1111)_2$, so a four-bit register overflows. Say so; it is free marks.
4. **Never skip Step 5 of a congruence proof.** Showing $2^r - 1$ is congruent is half the job. Showing $0 \le 2^r - 1 < 2^b - 1$ is what makes it the *remainder*.
5. **Name the Division Algorithm explicitly** at the start of an exponent-splitting proof. It is the formal name for $a = qb + r$ with $0 \le r < b$, and it is what licenses the rest.
6. **Handle $r = 0$ explicitly.** $2^0 - 1 = 0$, not $2^0 = 1$. This is the boundary case and it is the one examiners pick.
7. **Any base works.** The proof used only $2^b \equiv 1 \pmod{2^b - 1}$, so the same argument gives $(c^a - 1) \bmod (c^b - 1) \equiv c^{a \bmod b} - 1$. Saying so costs one line and shows you saw the structure.
8. **Connect it to what came before.** The Mersenne numbers $2^b - 1$ are the moduli here, and Shishir notes p. 86 flags them as a special form worth recognizing on sight.

## 🔗 Related Topics

- [DM-5_Lower_a: Primes, GCD, Fermat, CRT](DM-5_Lower_a_Primes_GCD_Fermat_CRT.md) — previous in the chain, the prime divisor proof filed under the same subtopic
- [DM-5.5: Modular Exponentiation](DM-5.5_Modular_Exponentiation.md) — where the binary expansion of an exponent does its real work
- [DM-6.3: Pigeonhole Principle](DM-6.3_Pigeonhole_Principle.md) — next in the chain, opening the counting block

---

[← Previous: DM-5 Lower-a: Primes, GCD, Fermat, CRT](DM-5_Lower_a_Primes_GCD_Fermat_CRT.md) | [🏠 Index](00_Index.md) | [Next: DM-6.3 Pigeonhole Principle →](DM-6.3_Pigeonhole_Principle.md)