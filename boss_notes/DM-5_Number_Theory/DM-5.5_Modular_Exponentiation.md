[← Previous: DM-5.4 Modular Arithmetic](DM-5.4_Modular_Arithmetic.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: DM-5.6 Fermat's Little Theorem →](DM-5.6_Fermats_Little_Theorem.md)

---

# DM-5.5: Modular Exponentiation

> 🔴 **Priority:** Critical | **Tested:** 2/3 papers (2022 Q.7(b), 2024 Q.8(b), recycled verbatim) | **Typical marks:** 3 to 4

## What This Is (and Why It Matters)

Suppose you are asked to compute $3^{644} \bmod 645$. If you tried to calculate $3^{644}$ directly, you would get a monstrous number with over 300 decimal digits. No calculator or standard 64-bit register can hold that number. Even multiplying by 3 one step at a time would take 644 operations, which is far too slow and prone to errors.

**Repeated squaring** (also known as **binary exponentiation** or the **square-and-multiply algorithm**) solves this problem. By breaking the exponent down into powers of 2 using its binary representation, we replace hundreds of multiplications with just 9 successive squarings and 2 product steps.

This exact technique runs at the core of RSA encryption and secure web communication (HTTPS/SSL). In RUET exams, this question was tested word-for-word in both 2022 and 2024. The prompt says "using a well-known algorithm", so naming the algorithm on line 1 is worth marks by itself.

---

## 📝 Key Definitions

> **The Modular Exponentiation Problem:** "In cryptography it is important to be able to find $b^n \bmod m$ efficiently, where $b, n,$ and $m$ are large integers. It is impractical to first compute $b^n$ and then find its remainder when divided by $m$ because $b^n$ will be a huge number." -- Rosen, §4.2, Subsection on Modular Exponentiation
>
> **In simple words:** You need to calculate the remainder of a giant power without ever letting the actual giant power exist in memory or on paper.

> **Repeated Squaring:** "To compute $b^n$, we need only compute the values of $b, b^2, (b^2)^2 = b^4, (b^4)^2 = b^8, \dots, b^{2^k}$. Once we have these values, we multiply the terms $b^{2^j}$ in this list where $a_j = 1$." -- Rosen, §4.2
>
> **In simple words:** You square the base repeatedly, reducing modulo $m$ at every step. Then you multiply together only the squared terms corresponding to the 1s in the binary representation of your exponent.

> **Algorithm 5 (Modular Exponentiation):**
> ```pascal
> procedure modular exponentiation(b: integer, n = (a_{k-1} a_{k-2} ... a_1 a_0)_2, m: positive integers)
> x := 1
> power := b mod m
> for i := 0 to k - 1
>     if a_i = 1 then x := (x * power) mod m
>     power := (power * power) mod m
> return x {x equals b^n mod m}
> ```
> -- Rosen, §4.2, Algorithm 5
>
> **In simple words:** A simple loop that tracks two variables: `power` (which squares every turn) and `x` (which accumulates `power` whenever the current binary bit is 1).

> **Complexity:** "Algorithm 5 is quite efficient; it uses $O((\log m)^2 \log n)$ bit operations to find $b^n \bmod m$." -- Rosen, §4.2
>
> **In simple words:** While brute-force multiplication takes $O(n)$ operations, repeated squaring needs only $O(\log_2 n)$ squarings. For an exponent like $644$, that cuts the work down from 644 multiplications to about 10 steps.

---

## The Core Idea

### The Algorithm, Explained Simply

The method rests on three logical steps:

1. **Convert the exponent to binary:**  
   Every positive integer $n$ can be uniquely written in base 2:
   $$
   n = \sum_{i=0}^{k-1} a_i 2^i, \quad \text{where } a_i \in \{0, 1\}
   $$
   For $n = 644$:
   $$
   644 = 512 + 128 + 4 = 2^9 + 2^7 + 2^2 = (1010000100)_2
   $$
   This means:
   $$
   3^{644} = 3^{512 + 128 + 4} = 3^{512} \times 3^{128} \times 3^4
   $$
   Notice that instead of 644 factors, we only need to multiply **three** terms.

2. **Build the table of squarings modulo $m$:**  
   We start at $3^1$ and square each result to get the next power of 2:
   $$
   3^1 \to 3^2 \to 3^4 \to 3^8 \to 3^{16} \to 3^{32} \to 3^{64} \to 3^{128} \to 3^{256} \to 3^{512}
   $$
   Crucially, we reduce modulo $m$ after **every single squaring**. The numbers never grow larger than $m^2$. For $m = 645$, the largest intermediate is $645^2 = 416{,}025$, which is easy to handle by hand or calculator.

3. **Combine the selected powers:**  
   Multiply the powers that match the set bits ($a_i = 1$) and reduce after each product.

---

### Rosen's Trace Table

Here is how Algorithm 5 executes for $3^{644} \bmod 645$, showing bit position $i$, bit $a_i$, accumulator $x$, and `power`:

| Bit $i$ | Value $2^i$ | Bit $a_i$ | `power` before step | Action on accumulator $x$ | `power` after step ($^2 \bmod 645$) |
| :--: | :--: | :--: | :-- | :-- | :-- |
| 0 | 1 | 0 | $3$ | $x = 1$ (bit is 0, skip) | $3^2 = 9$ |
| 1 | 2 | 0 | $9$ | $x = 1$ (bit is 0, skip) | $9^2 = 81$ |
| 2 | 4 | **1** | $81$ | $x = (1 \times 81) \bmod 645 = 81$ | $81^2 = 6561 \equiv 111$ |
| 3 | 8 | 0 | $111$ | $x = 81$ (skip) | $111^2 = 12321 \equiv 66$ |
| 4 | 16 | 0 | $66$ | $x = 81$ (skip) | $66^2 = 4356 \equiv 486$ |
| 5 | 32 | 0 | $486$ | $x = 81$ (skip) | $486^2 = 236196 \equiv 126$ |
| 6 | 64 | 0 | $126$ | $x = 81$ (skip) | $126^2 = 15876 \equiv 396$ |
| 7 | 128 | **1** | $396$ | $x = (81 \times 396) \bmod 645 = 471$ | $396^2 = 156816 \equiv 81$ |
| 8 | 256 | 0 | $81$ | $x = 471$ (skip) | $81^2 = 6561 \equiv 111$ |
| 9 | 512 | **1** | $111$ | $x = (471 \times 111) \bmod 645 = 36$ | Finished |

Final output: $x = 36$.

---

## 🔧 Worked Example

> **From:** 2022 Q.7(b) and 2024 Q.8(b) -- [Marks: 03 in 2022, 04 in 2024]

**Question.** Solve $3^{644} \bmod 645$ using a well-known algorithm.

**Solution.**

The well-known algorithm is **repeated squaring** (binary exponentiation).

**Step 1. Find the binary expansion of the exponent.**

$$
644 = 512 + 128 + 4 = 2^9 + 2^7 + 2^2 = (1010000100)_2
$$

The set bits are at positions $i = 2, 7, 9$.

**Step 2. Compute the successive square powers modulo 645.**

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
3^8 = 81^2 = 6561 = 645(10) + 111 \equiv 111 \pmod{645}
$$

$$
3^{16} = 111^2 = 12321 = 645(19) + 66 \equiv 66 \pmod{645}
$$

$$
3^{32} = 66^2 = 4356 = 645(6) + 486 \equiv 486 \pmod{645}
$$

$$
3^{64} = 486^2 = 236196 = 645(366) + 126 \equiv 126 \pmod{645}
$$

$$
3^{128} = 126^2 = 15876 = 645(24) + 396 \equiv 396 \pmod{645}
$$

$$
3^{256} = 396^2 = 156816 = 645(243) + 81 \equiv 81 \pmod{645}
$$

$$
3^{512} = 81^2 = 6561 = 645(10) + 111 \equiv 111 \pmod{645}
$$

**Step 3. Multiply the factors corresponding to the set bits.**

The set bits correspond to powers $3^{512}$, $3^{128}$, and $3^4$:

$$
3^{644} \equiv 3^{512} \times 3^{128} \times 3^4 \pmod{645}
$$

Substitute the reduced residues:

$$
3^{644} \equiv 111 \times 396 \times 81 \pmod{645}
$$

Evaluate in pairs:

$$
111 \times 396 = 43956 = 645(68) + 96 \equiv 96 \pmod{645}
$$

Now multiply by the remaining factor 81:

$$
96 \times 81 = 7776 = 645(12) + 36 \equiv 36 \pmod{645}
$$

$$
\boxed{3^{644} \bmod 645 = 36}
$$

---

### Independent Verification via Chinese Remainder Theorem

Factor the modulus: $645 = 3 \times 5 \times 43$.

1. **Modulo 3:**
   $3^{644}$ has 3 as a base, so $3^{644} \equiv 0 \pmod 3$.
2. **Modulo 5:**
   By Fermat's Little Theorem, $3^4 \equiv 1 \pmod 5$. Since $644 = 4 \times 161$, $3^{644} \equiv (3^4)^{161} \equiv 1^{161} \equiv 1 \pmod 5$.
3. **Modulo 43:**
   43 is prime, so by Fermat's Little Theorem, $3^{42} \equiv 1 \pmod{43}$.  
   Divide the exponent: $644 = 42 \times 15 + 14$, so:
   $$
   3^{644} \equiv 3^{14} = 3^8 \times 3^4 \times 3^2 \pmod{43}
   $$
   Computing residues mod 43:
   - $3^2 = 9$
   - $3^4 = 81 = 43(1) + 38 \equiv -5 \pmod{43}$
   - $3^8 \equiv (-5)^2 = 25 \pmod{43}$
   - $3^{14} \equiv 25 \times (-5) \times 9 = -1125 = 43(-27) + 36 \equiv 36 \pmod{43}$.

Now test our answer $36$:
- $36 \bmod 3 = 0$ ✓
- $36 \bmod 5 = 1$ ✓
- $36 \bmod 43 = 36$ ✓

All three conditions match $36$ perfectly.

---

## ⚡ Common Traps & Exam Tips

> [!WARNING] Common Trap: Forgetting the Name of the Algorithm
> The RUET question begins with: "Solve $3^{644} \bmod 645$ using a well-known algorithm."  
> If you start calculating without writing the words **"Repeated Squaring"** (or **"Binary Exponentiation"**), you will lose marks. Always state the algorithm name prominently.

> [!TIP] Write the Binary Breakdown First
> Before computing any squarings, write: $644 = 512 + 128 + 4 = (1010000100)_2$.
> This immediately tells you that you must stop your table at $3^{512}$, and that only 3 numbers will be multiplied at the end.

---

[← Previous: DM-5.4 Modular Arithmetic](DM-5.4_Modular_Arithmetic.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: DM-5.6 Fermat's Little Theorem →](DM-5.6_Fermats_Little_Theorem.md)
