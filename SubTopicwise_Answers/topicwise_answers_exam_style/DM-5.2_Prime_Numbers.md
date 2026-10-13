---
title: "DM-5.2 · Prime Numbers"
tags:
  - numerical-methods
  - discrete-mathematics
  - topicwise
---


[🏠 Subtopic Index](00_Index.md) | [← Prev: DM-3.13 Logic Extensions](DM-3.13_Logic_Extensions.md) | [Next: DM-5.3 GCD, LCM & Euclidean Algorithm →](DM-5.3_GCD_LCM_and_Euclidean_Algorithm.md)

---

# DM-5.2 · Prime Numbers

Every block below is copied from `../answers_exam_style/`, which is the
only place an answer is authored. A number here is the same number, character
for character, as the one it came from.


### [2023 Q.7(c)]

**Question.** If $n$ is a composite integer then $n$ has a prime divisor less than or equal to $\sqrt{n}$.

**Solution.**

**Proof.**

Let $n$ be composite. Then by definition $n = ab$ for integers $a, b$ with
$1 < a < n$ and $1 < b < n$.

**Key observation.** At least one of $a$ and $b$ is at most $\sqrt{n}$. Suppose
both were larger:

$$
a > \sqrt{n} \quad \text{and} \quad b > \sqrt{n} \quad \Longrightarrow \quad ab > \sqrt{n}\sqrt{n} = n
$$

Since $ab = n$, this is a contradiction. Hence $a \le \sqrt{n}$ or $b \le \sqrt{n}$.

WLOG suppose $a \le \sqrt{n}$, so $1 < a \le \sqrt{n}$.

**Now find a prime divisor at most $a$.** Every integer $a > 1$ has a prime
divisor: keep dividing by a prime factor until the result is 1, and the last
prime divided out is a prime $p$ dividing $a$. So there is a prime $p$ with
$p \mid a$.

Since $a \mid n$ and $p \mid a$, transitivity of divisibility gives $p \mid n$.
And $p \le a \le \sqrt{n}$.

$$
\boxed{\text{Every composite } n \text{ has a prime divisor } p \text{ with } p \le \sqrt{n}}
$$

> [!note] Why this matters
> This is the fact that makes trial division for factorisation terminate at
> $\sqrt{n}$ instead of at $n$. The trial-divisor test for primality therefore need
> only try divisors up to $\sqrt{n}$, which is the square root of the work.
>
> Worked examples: $91 = 7 \times 13$ with $\sqrt{91} = 9.539$, and the prime
> divisor $7$ is indeed below it. $97$ is prime, so the statement does not apply
> to it, which is why a trial division up to $9$ establishes its primality.

---

[🏠 Subtopic Index](00_Index.md) | [← Prev: DM-3.13 Logic Extensions](DM-3.13_Logic_Extensions.md) | [Next: DM-5.3 GCD, LCM & Euclidean Algorithm →](DM-5.3_GCD_LCM_and_Euclidean_Algorithm.md)
