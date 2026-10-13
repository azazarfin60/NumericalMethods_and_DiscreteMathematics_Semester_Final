---
title: "DM-5.7 · Chinese Remainder Theorem"
tags:
  - numerical-methods
  - discrete-mathematics
  - topicwise
---


[🏠 Subtopic Index](00_Index.md) | [← Prev: DM-5.5 Modular Exponentiation](DM-5.5_Modular_Exponentiation.md) | [Next: DM-5.8 Number Bases & Binary Arithmetic →](DM-5.8_Number_Bases_and_Binary_Arithmetic.md)

---

# DM-5.7 · Chinese Remainder Theorem

Every block below is copied from `../answers_explanation/`. The reasoning
is written once, in the year-wise file, and is not restated here.


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

[🏠 Subtopic Index](00_Index.md) | [← Prev: DM-5.5 Modular Exponentiation](DM-5.5_Modular_Exponentiation.md) | [Next: DM-5.8 Number Bases & Binary Arithmetic →](DM-5.8_Number_Bases_and_Binary_Arithmetic.md)
