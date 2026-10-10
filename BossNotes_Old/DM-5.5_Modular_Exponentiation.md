[← Previous: DM-5.4 Modular Arithmetic and Congruence](DM-5.4_Modular_Arithmetic_and_Congruence.md) | [🏠 Index](00_Index.md) | [Next: DM-5 Lower-a: Primes, GCD, Fermat, CRT →](DM-5_Lower_a_Primes_GCD_Fermat_CRT.md)

---

# DM-5.5: Modular Exponentiation
> **Section:** B (Discrete Mathematics) | **Priority:** 🔴 | **Exam Frequency:** 2/3 DM papers (2022 Q.7(b), 2024 Q.8(b), recycled verbatim)
> **Subtopics:** DM-5.5 (Modular Exponentiation)
> **Sources:** Rosen §4.2 (pp. 15–18, Algorithm 5 and Example 12), Fahad Notes Class-19, Raidah Notes §5, Shishir Notes §10–§11

## Why This Topic Matters

This is a two-paper topic with a single dominant question. 2022 and 2024 asked **exactly** the same computation, $3^{644} \bmod 645$, with the same answer. The paper says "using a well-known algorithm" and expects you to name it, so the algorithm name is worth marks on its own.

The idea behind the algorithm is worth more than the arithmetic. Modular exponentiation is how RSA and every modern cipher actually runs. Understanding why $O(\log n)$ squarings replace $n$ multiplications is the difference between memorizing a table and knowing the method.

---

## 📝 Key Definitions

> **The problem:** "In cryptography it is important to be able to find $b^n \bmod m$ efficiently, where $b, n,$ and $m$ are large integers. It is impractical to first compute $b^n$ and then find its remainder when divided by $m$ because $b^n$ will be a huge number." — Rosen, §4.2, Modular Exponentiation (p. 17)

> **The idea:** "to compute $b^n$, we need only compute the values of $b, b^2, (b^2)^2 = b^4, (b^4)^2 = b^8, \dots, b^{2^k}$. Once we have these values, we multiply the terms $b^{2^j}$ in this list, where $a_j = 1$." — Rosen, §4.2 (p. 17)

> **The algorithm:** "**Algorithm 5: Modular Exponentiation.**
> ```pascal
> procedure modular exponentiation(b: integer, n = (ak-1 ak-2 ... a1 a0)_2, m: positive integers)
> x := 1
> power := b mod m
> for i := 0 to k - 1
>     if ai = 1 then x := (x · power) mod m
>     power := (power · power) mod m
> return x {x equals b^n mod m}
> ```" — Rosen, §4.2 (p. 18)

> **The complexity:** "Algorithm 5 is quite efficient; it uses $O((\log m)^2 \log n)$ bit operations to find $b^n \bmod m$." — Rosen, §4.2 (p. 18). In terms of squarings and multiplications it is $O(\log n)$ of each.

> **Key term:** "**modular exponentiation:** computing $b^n \bmod m$ efficiently using the binary expansion of $n$." — Rosen, §4.2, Key Terms (p. 14)

---

## The Algorithm, Explained Before the Numbers

The name the exam wants is **repeated squaring**, also called **binary exponentiation** or the **square-and-multiply method**. All three are accepted. Say "repeated squaring" first, since that is Rosen's phrase in §4.2 and it is what the paper's "well-known algorithm" refers to.

### Why the naive route is hopeless

To compute $3^{644} \bmod 645$ by repeated multiplication you would multiply 644 times. Each result is under 645, so the arithmetic is easy, but 644 steps is a page of work with a large chance of one arithmetic slip near the end.

### What repeated squaring does instead

Write the exponent in binary. Each $1$ bit says "multiply in the power of two at this position."

$$
644 = 512 + 128 + 4 = (1010000100)_2
$$

So $3^{644} = 3^{512} \cdot 3^{128} \cdot 3^4$. Only three factors. And those factors are not independent: $3^{512} = (3^{256})^2$, $3^{256} = (3^{128})^2$, and so on. Squaring once produces the next power of two. So the whole computation needs:

- about $\log_2 644 \approx 9$ squarings to build the table, and
- about 3 multiplications to combine them.

### The method, step by step

1. **Write the exponent in binary.** Count the bits. That is how many squarings you need.
2. **Build the power table.** Start at $3^1$. Square and reduce modulo $m$ each time: $3^2$, $3^4$, $3^8$, and so on up to the highest bit.
3. **Read the set bits.** Every 1 in the binary expansion selects one row of the table.
4. **Multiply the selected rows,** reducing modulo $m$ after each multiplication.
5. **Report the final residue.** It lies in $[0, m-1]$.

> [!TIP] Reduce modulo $m$ after **every** line
> $3^8 = 6561$ is fine, but $3^16 = 6561^2$ is a seven-digit number. Writing $3^8 \equiv 111$ and then squaring 111 gives $12321$, which is manageable. The table never exceeds $m^2 \approx 415{,}000$, and $m^2$ has a quick division by $m$ since $m$ is a round-ish number.

### The pseudocode, in plain steps

Rosen's Algorithm 5, translated into a procedure you can write in the exam:

| Line | What it does |
| :-- | :-- |
| $x := 1$ | the running product, start at the multiplicative identity |
| $\text{power} := b \bmod m$ | the current row of the table, $b^{2^0}$ |
| for $i := 0$ to $k-1$ | one pass per bit of the exponent |
| if $a_i = 1$ then $x := (x \cdot \text{power}) \bmod m$ | multiply in this row only if the bit is set |
| $\text{power} := (\text{power} \cdot \text{power}) \bmod m$ | advance to the next row, $b^{2^{i+1}}$ |
| return $x$ | $x = b^n \bmod m$ |

The square happens **every** iteration. The multiply happens **conditionally**. That is the whole algorithm.

> [!NOTE] Why it is $O(\log n)$
> The loop runs once per bit of $n$, and a number with $n$ has about $\log_2 n$ bits. So the loop runs $\log_2 n$ times regardless of how large $n$ is. Going from $n = 1000$ to $n = 10^9$ adds about ten loop passes.

---

## Worked Example (PYQ 2022 Q.7(b) and 2024 Q.8(b))

> **Source:** 2022 Q.7(b), 2024 Q.8(b). The same question appears in both papers.

**Question.** Solve $3^{644} \bmod 645$ using a well-known algorithm.

**Solution.** The well-known algorithm is **repeated squaring**.

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

**Step 3. Multiply the powers named by the set bits**, which are $2^9 = 512$, $2^7 = 128$ and $2^2 = 4$:

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

$$
\boxed{3^{644} \bmod 645 = 36}
$$

> [!info] Check by an independent route
> Factor $645 = 3 \times 5 \times 43$ and apply the Chinese remainder theorem.
>
> | Modulus | Result | Working |
> | :-- | --: | :-- |
> | $3$ | 0 | $3^{644}$ is a multiple of 3 |
> | $5$ | 1 | $3^4 \equiv 1$ and $644 = 4(161)$ |
> | $43$ | 36 | $\phi(43) = 42$, $644 = 42(15)+14$, so $3^{644} \equiv 3^{14} = 3^8 \cdot 3^4 \cdot 3^2 \equiv 25 \times 38 \times 9 \equiv 36$ |
>
> Checking $36$: $36 \bmod 3 = 0$, $36 \bmod 5 = 1$, $36 \bmod 43 = 36$. The repeated-squaring result was also produced independently by a direct modular exponentiation routine, which returned 36.

**Reading the squaring table as a table.** The bits of $644 = (1010000100)_2$, read from position 0 on the right, are:

| Bit position $i$ | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| :-- | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| Bit $a_i$ | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 |
| $2^i$ | 512 | 256 | 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |
| $3^{2^i} \bmod 645$ | 111 | 81 | 396 | 126 | 486 | 66 | 111 | 81 | 9 | 3 |

Three bits are set, at positions 9, 7 and 2. Those three rows are the ones multiplied. Reading it this way is faster than working left to right, because the set bits jump out at you.

**Rosen's trace of the same computation.** This question is Rosen §4.2 Example 12 (p. 18) reproduced without credit. Rosen runs Algorithm 5 as written, tracking $x$ and `power` side by side:

| $i$ | $a_i$ | $x$ | $\text{power}$ |
| :-: | :-: | :-: | :-- |
| 0 | 0 | 1 | $3^2 \bmod 645 = 9$ |
| 1 | 0 | 1 | $9^2 \bmod 645 = 81$ |
| 2 | 1 | $81$ | $81^2 \bmod 645 = 111$ |
| 3 | 0 | 81 | $111^2 \bmod 645 = 66$ |
| 4 | 0 | 81 | $66^2 \bmod 645 = 486$ |
| 5 | 0 | 81 | $486^2 \bmod 645 = 126$ |
| 6 | 0 | 81 | $126^2 \bmod 645 = 396$ |
| 7 | 1 | 471 | $396^2 \bmod 645 = 81$ |
| 8 | 0 | 471 | $81^2 \bmod 645 = 111$ |
| 9 | 1 | 36 | done |

The `power` column reproduces the squaring table exactly. The $x$ column is the running product, and only three rows change it.

> [!NOTE] The order of multiplication does not matter
> The three factors are 111, 396 and 81. Multiplying them as $111 \times 396 \times 81$ gives intermediates 96 and then 36. Multiplying as $396 \times 81$ first gives $32076 = 645 \times 49 + 471$, so the first intermediate is 471, and then $111 \times 471 = 52281 = 645 \times 81 + 36$. Same answer. Pick the order that keeps the intermediates smallest, which here is the one used above.

> [!WARNING] The three common slips
> **Miss a set bit.** $644 = 512 + 128 + 4$, and forgetting the $+4$ gives a completely different answer. Write the binary expansion first and count the ones.
> **Square the residue, not the original.** $3^{16} \equiv 111^2$, not $9^2$. Using a stale entry in the table is the single most frequent error.
> **Multiply instead of add.** Repeated squaring is not "compute $3^4$ then $3^8$ then...". It is build the table, then multiply the selected rows.

## The general shape of the problem

Examiners will not always use 644 and 645. The method is the same.

| Step | Question | Answer |
| :-- | :-- | :-- |
| 1 | Write $n$ in binary | $n = (a_k \dots a_0)_2$ |
| 2 | Build $b^{2^i} \bmod m$ for $i = 0, \dots, k$ | about $\log_2 n$ squarings |
| 3 | Multiply the rows where $a_i = 1$ | about half of $\log_2 n$ multiplications |
| 4 | Report the residue | lies in $[0, m-1]$ |

**When the base shares a factor with the modulus,** stop immediately and read off the answer. $3 \mid 645$, so $3^{644} \equiv 0 \pmod 3$ without any work. That observation is what makes the CRT cross-check above cheap.

---

## Exam Variants

| Year | Question | Data | Algorithm | Answer |
| :--- | :--- | :--- | :--- | :-- |
| 2022 Q.7(b) | "Solve $3^{644} \bmod 645$ using a well-known algorithm" | $3^{644} \bmod 645$ | repeated squaring | $\boxed{3^{644} \bmod 645 = 36}$ |
| 2024 Q.8(b) | recycled verbatim from 2022 | $3^{644} \bmod 645$ | repeated squaring | $\boxed{3^{644} \bmod 645 = 36}$ |

The variant to rehearse is the method itself, not the numbers. If a paper asks for $2^{100} \bmod 101$ or $7^{1000} \bmod 11$, the same four steps apply.

---

## ⚡ Exam Tips & Common Mistakes

1. **Name the algorithm in the first line.** "The well-known algorithm is repeated squaring" costs five seconds and is worth a mark in every paper that asks "using a well-known algorithm".
2. **Write the binary expansion before touching the arithmetic.** $644 = (1010000100)_2$ tells you the table has ten rows and that exactly three of them get multiplied. Skipping this is how set bits get dropped.
3. **Reduce after every squaring,** so the biggest number you ever write is under $645^2 \approx 4.2 \times 10^5$.
4. **Always square the previous residue.** $3^{32} \equiv 66^2$, not $81^2$. Trace the chain backwards if a row looks wrong.
5. **Show the division.** "$6561 = 645 \times 10 + 111$" is the working. Writing "$3^8 \equiv 111$" with no division is an assertion, not a proof.
6. **A cross-check on one line is worth doing.** Factoring $645 = 3 \times 5 \times 43$ and reducing modulo each prime confirms the answer without repeating the table.
7. **Exploit a common factor.** If the base and modulus share a factor, the residue modulo that factor is $0$ and the work shrinks.
8. **$\phi(p) = p - 1$ for a prime $p$.** With $\phi(43) = 42$, reducing $644$ to $644 \bmod 42 = 14$ turns a ten-row table into a four-row one. Reach for this when the modulus is prime and large.

## 🔗 Related Topics

- [DM-5.4: Modular Arithmetic and Congruence](DM-5.4_Modular_Arithmetic_and_Congruence.md) — previous in the chain, the compatibility theorem that makes the table legal
- [DM-5_Lower_a: Primes, GCD, Fermat, CRT](DM-5_Lower_a_Primes_GCD_Fermat_CRT.md) — next in the chain, where $\phi(p) = p-1$ and the CRT cross-check are proved
- [DM-5_Lower_b: Bases and Proofs](DM-5_Lower_b_Bases_Proofs.md) — the binary expansions this file depends on

---

[← Previous: DM-5.4 Modular Arithmetic and Congruence](DM-5.4_Modular_Arithmetic_and_Congruence.md) | [🏠 Index](00_Index.md) | [Next: DM-5 Lower-a: Primes, GCD, Fermat, CRT →](DM-5_Lower_a_Primes_GCD_Fermat_CRT.md)