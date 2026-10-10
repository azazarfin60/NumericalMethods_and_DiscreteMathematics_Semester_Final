[← Previous: DM-3 Lower-b: Puzzles, Gates, Extensions](DM-3_Lower_b_Puzzles_Gates_Extensions.md) | [🏠 Index](00_Index.md) | [Next: DM-5.5 Modular Exponentiation →](DM-5.5_Modular_Exponentiation.md)

---

# DM-5.4: Modular Arithmetic and Congruence
> **Section:** B (Discrete Mathematics) | **Priority:** 🔴 | **Exam Frequency:** 3/3 DM papers (2022, 2023, 2024)
> **Subtopics:** DM-5.4 (Modular Arithmetic and Congruence)
> **Sources:** Rosen §4.1 (pp. 3–13), §4.4, Fahad Notes Class-19, Raidah Notes §5, Shishir Notes §5, §9–§11

## Why This Topic Matters

This is the only DM subtopic that has appeared in **every single paper** since Section B began. It is also the cheapest one to prepare, because the exam always asks the same thing: given residues of $a$ and $b$ modulo some modulus, find the residue of a linear or polynomial combination of $a$ and $b$. Learn three theorems and you own the whole question.

The whole trick is in one sentence: **replace $a$ and $b$ by their residues before doing any arithmetic.** The numbers stay under the modulus the entire time.

---

## 📝 Key Definitions

> **Divisibility:** "**$a \mid b$ ($a$ divides $b$):** there is an integer $c$ such that $b = ac$." — Rosen, §4.1, Key Terms (p. 2)

> **The Division Algorithm:** "Let $a$ be an integer and $d$ a positive integer. Then there are unique integers $q$ and $r$ with $0 \leq r < d$ such that $a = dq + r$." — Rosen, §4.1, Theorem 2 (p. 5)

> **Divisor / dividend / quotient / remainder:** "In the equality given in the division algorithm, $d$ is called the **divisor**, $a$ is called the **dividend**, $q$ is called the **quotient**, and $r$ is called the **remainder**." — Rosen, §4.1, Definition 2 (p. 5)

> **Mod and div:** "$q = a \text{ div } d$, $r = a \bmod d$." — Rosen, §4.1, Definition 2 (p. 5). And "$a \bmod d$ is the remainder obtained when $a$ is divided by the positive integer $d$, equal to $a - d\lfloor a/d \rfloor$." — Rosen, §4.1, Key Terms (p. 2)

> **Congruence:** "If $a$ and $b$ are integers and $m$ is a positive integer, then $a$ is **congruent to** $b$ **modulo** $m$ if $m$ divides $a - b$. We use the notation $a \equiv b \pmod m$ to indicate that $a$ is congruent to $b$ modulo $m$. We say that $a \equiv b \pmod m$ is a **congruence** and that $m$ is its **modulus** (plural *moduli*)." — Rosen, §4.1 (p. 6)

> **The compatibility theorem, and the whole exam:** "**Theorem 5.** Let $m$ be a positive integer. If $a \equiv b \pmod m$ and $c \equiv d \pmod m$, then $a + c \equiv b + d \pmod m$ and $ac \equiv bd \pmod m$." — Rosen, §4.1 (p. 7)

> **Why it works:** "by Theorem 4 there are integers $s$ and $t$ with $b = a + sm$ and $d = c + tm$. Hence $b + d = (a + c) + m(s + t)$ and $bd = ac + m(at + cs + stm)$." — Rosen, §4.1, proof of Theorem 5 (p. 7)

> **Modular arithmetic:** "arithmetic operations $+_m$ and $\cdot_m$ defined on $\mathbf{Z}_m = \{0, 1, \dots, m - 1\}$." — Rosen, §4.1, Key Terms (p. 2)

---

## The Division Algorithm and the Long Division Picture

Every integer splits uniquely into a quotient and a remainder. That is the foundation of everything in this file.

![Long division schematic marking the quotient, dividend, divisor and remainder (Shishir Notes p. 81)](diagrams/dm5_division_algorithm_schematic.jpg)

The picture shows $27 \div 4 = 6$ remainder $3$, that is $27 = 4(6) + 3$. The remainder satisfies $0 \le r < d$, and it is the only value of $r$ that does.

| Notation | Meaning | For $a = 27$, $d = 4$ |
| :-- | :-- | :-- |
| $a \text{ div } d$ | quotient $\lfloor a/d \rfloor$ | 6 |
| $a \bmod d$ | remainder $a - d\lfloor a/d \rfloor$ | 3 |
| $a = dq + r$ | the equality | $27 = 4 \times 6 + 3$ |

> [!NOTE] Mod in a calculator
> Shishir notes p. 89 shows the trick. Compute $3 \div 7 = 0.4285\ldots$, then take $0.4285\ldots \times 7 = 2.999\ldots$, round up to 3. So $3 \bmod 7 = 3$. This works whenever $a < m$, where the answer is just $a$ again.

## What Congruence Really Means

$a \equiv b \pmod m$ says exactly one thing: $m$ divides $a - b$. Nothing more.

$$
a \equiv b \pmod m \iff a - b = km \text{ for some integer } k
$$

**Two directions, both needed in the exam.**

| Direction | How to use it | Example with $m = 19$ |
| :-- | :-- | :-- |
| $a \equiv b \Rightarrow a + km$ | generate all members of the class | $11, 30, 49, 68, 87, \ldots$ are all $\equiv 11$ |
| $a \equiv b \Rightarrow a - b$ is a multiple of $m$ | prove a congruence | $86 \equiv 10$ because $86 - 10 = 76 = 4 \times 19$ |

**The residue is the representative in $[0, m-1]$.** When a question says "find the integer $c$ with $0 \le c \le 18$", it is asking for that unique representative. Every integer in the class has exactly one.

> [!WARNING] Congruence is not equality
> $a \equiv b \pmod{19}$ does **not** mean $a = b$. It means they differ by a multiple of 19. Writing $86 = 10$ is wrong; writing $86 \equiv 10 \pmod{19}$ is right. And $a \equiv b \pmod{19}$ says nothing at all about $\pmod{20}$.

## The Three Properties That Solve the Exam

All three follow from Theorem 5 by choosing the $c, d$ wisely.

**Property 1. Compatibility with addition.**
$a \equiv b \pmod m$ and $c \equiv d \pmod m \Rightarrow a + c \equiv b + d \pmod m$

**Property 2. Compatibility with multiplication.**
$a \equiv b \pmod m$ and $c \equiv d \pmod m \Rightarrow ac \equiv bd \pmod m$

**Property 3. Reduction of intermediate residues.** Property 2 applied to a whole chain: once $x \equiv r \pmod m$, you may use $r$ anywhere $x$ appears, and $r$ can be reduced again at any point. This is the property the exam actually tests.

$$
x \equiv r \pmod m \Rightarrow x^k \equiv r^k \pmod m \quad \text{for every } k \ge 1
$$

**The algorithm, in four lines.**

1. Replace every given variable by its residue.
2. Evaluate the expression on the residues, reducing after each operation.
3. If the result is $\ge m$, subtract multiples of $m$ until you are in $[0, m-1]$.
4. That value is the answer $c$.

> [!TIP] Reduce after **every** operation, not at the end
> For $11^3 \bmod 19$: $11^3 = 1331$ is a four-digit number. But $11^2 = 121 = 19 \times 6 + 7$, so $11^2 \equiv 7$, and then $7 \times 11 = 77 = 19 \times 4 + 1$, giving 1. You never write 1331. Same answer, and the small-number route cannot overflow a fixed-width register.

## Worked Example (PYQ 2022 Q.7(a) and 2024 Q.8(a))

> **Source:** 2022 Q.7(a), 2024 Q.8(a). The same question appears in both papers.

**Question.** Suppose that $a$ and $b$ are integers, $a \equiv 11 \pmod{19}$ and $b \equiv 3 \pmod{19}$. Find the integer $c$ with $0 \le c \le 18$ such that (i) $c \equiv 7a + 3b \pmod{19}$, (ii) $c \equiv a^3 + 4b^3 \pmod{19}$.

**Solution.** Work with the residues, then reduce to $0 \le c \le 18$.

**(i) $c \equiv 7a + 3b \pmod{19}$**

$$
c \equiv 7(11) + 3(3) = 77 + 9 = 86 \pmod{19}
$$

Divide: $86 = 19(4) + 10$.

$$
\boxed{c = 10}
$$

**(ii) $c \equiv a^3 + 4b^3 \pmod{19}$**

Reduce the powers first to keep the numbers small:

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

$$
\boxed{c = 14}
$$

> [!info] Check by an independent route
> **Direct substitution.** $11^3 + 4 \cdot 3^3 = 1331 + 108 = 1439$, and $1439 = 19(75) + 14$, giving $c = 14$.
> **Part (i) direct.** $86 = 19(4) + 10$, giving $c = 10$.
> Both agree, and every remainder satisfies $0 \le c \le 18$.

**The order of operations that matters.** In part (ii) the cube was computed as $(a^2) \cdot a$ using a reduced intermediate. The direct route computes $11^3 = 1331$ in one step. Both are legal because reduction is compatible with multiplication at every stage. What is **not** legal is reducing partway and then treating the reduced number as if it were the original in a context where the modulus differs.

## Worked Example (PYQ 2023 Q.7(a))

> **Source:** 2023 Q.7(a)

**Question.** Suppose that $a$ and $b$ are integers, $a \equiv 4 \pmod{13}$, and $b \equiv 9 \pmod{13}$. Find the integer $c$ with $0 \le c \le 12$ such that (i) $c = 2a + 3b \pmod{13}$, (ii) $c = a^2 + b^2 \pmod{13}$.

**Solution.** Work entirely with the residues, then reduce to $0 \le c \le 12$.

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

> [!info] Check
> **(i)** $13 \times 2 = 26$ and $26 + 9 = 35$
> **(ii)** $13 \times 7 = 91$ and $91 + 6 = 97$
> Both remainders satisfy $0 \le c \le 12$ as the question requires.
>
> Squaring reduced residues is safe here, since $16 \equiv 3 \pmod{13}$ and $81 \equiv 3 \pmod{13}$, so $c \equiv 3 + 3 = 6$. The same answer from much smaller numbers confirms the first computation.

> [!note] Reducing early keeps the numbers small
> Writing $b \equiv 9$, then $b^2 \equiv 3$, then $c \equiv 3 + 3 = 6$, never produces a number above 9. Direct squaring gave 97. Same answer, and the first route cannot overflow a fixed-width register.

---

## Reference: reductions you should be able to do by sight

| $m$ | Useful identities |
| :-- | :-- |
| 3 | $a \equiv 0,1,2 \pmod 3$; $3 \equiv 0$ |
| 4 | $2^2 \equiv 0$, $2^3 \equiv 0$; $3 \cdot 3 = 9 \equiv 1$ |
| 5 | $2^4 \equiv 1$, $3^4 \equiv 1$, $4 \equiv -1$ |
| 13 | $3^3 = 27 = 13 \times 2 + 1 \equiv 1$, so $3^{3k} \equiv 1$ |
| 19 | $7^3 = 343 = 19 \times 18 + 1 \equiv 1$, so $7^{3k} \equiv 1$ |
| 43 | prime, so $\phi(43) = 42$ and $a^{42} \equiv 1$ for $43 \nmid a$ |

**Negative residues.** $a \equiv -k \pmod m$ whenever $m - k \equiv a$. So $-3 \equiv 16 \pmod{19}$ and $-4 \equiv 9 \pmod{13}$. Working with small negative numbers and adding the modulus once at the end is usually the shortest route.

---

## Exam Variants

| Year | Question | Data | Part (i) | Part (ii) |
| :--- | :--- | :--- | :-- | :-- |
| 2022 Q.7(a) | $7a + 3b$, $a^3 + 4b^3$ | $a \equiv 11$, $b \equiv 3 \pmod{19}$ | $\boxed{c = 10}$ | $\boxed{c = 14}$ |
| 2024 Q.8(a) | recycled verbatim from 2022 | $a \equiv 11$, $b \equiv 3 \pmod{19}$ | $\boxed{c = 10}$ | $\boxed{c = 14}$ |
| 2023 Q.7(a) | $2a + 3b$, $a^2 + b^2$ | $a \equiv 4$, $b \equiv 9 \pmod{13}$ | $\boxed{c = 9}$ | $\boxed{c = 6}$ |

The question shape has been stable across all three papers: two residues given, two expressions asked, modulus $13$ or $19$. Note that 2022 and 2024 share every number. Treat 2023's modulus as the variant to rehearse.

---

## ⚡ Exam Tips & Common Mistakes

1. **Substitute residues immediately.** Write $a = 11$, not $a \equiv 11$ then carry the symbol around. It prevents a misplaced congruence bar later.
2. **Reduce after every single operation,** not once at the end. $11^3 \bmod 19$ becomes two small steps instead of a division of 1331.
3. **Check the range before you stop.** The question almost always specifies $0 \le c \le m-1$. If your answer is 33 or 97 instead of 14 or 6, you did the arithmetic but skipped the reduction.
4. **When the result is negative, add $m$ until it is positive.** Modulo arithmetic on residues always lands in $[0, m-1]$, never in $(-\lfloor m/2 \rfloor, \lfloor m/2 \rfloor]$.
5. **Write the division out.** "$86 = 19 \times 4 + 10$" earns the arithmetic mark. Just writing "$\equiv 10$" may not.
6. **A residue stands in for its whole class.** Once $b \equiv 9 \pmod{13}$, you may use 9 anywhere $b$ appears. You are not claiming $b = 9$.
7. **Do not reduce modulo a different number.** $86 \equiv 10 \pmod{19}$ and $86 \equiv 5 \pmod{27}$ are both true. The modulus is part of the statement.
8. **Part (i) is a sanity check for part (ii).** If the linear form goes wrong, the quadratic and cubic parts will too. Solve (i) first.

## 🔗 Related Topics

- [DM-3_Lower_b: Puzzles, Gates, Extensions](DM-3_Lower_b_Puzzles_Gates_Extensions.md) — previous in the chain, last file of the logic block
- [DM-5.5: Modular Exponentiation](DM-5.5_Modular_Exponentiation.md) — next in the chain, where reduction compatibility does the heavy lifting
- [DM-5_Lower_a: Primes, GCD, Fermat, CRT](DM-5_Lower_a_Primes_GCD_Fermat_CRT.md) — the theorems that turn congruences into solutions

---

[← Previous: DM-3 Lower-b: Puzzles, Gates, Extensions](DM-3_Lower_b_Puzzles_Gates_Extensions.md) | [🏠 Index](00_Index.md) | [Next: DM-5.5 Modular Exponentiation →](DM-5.5_Modular_Exponentiation.md)