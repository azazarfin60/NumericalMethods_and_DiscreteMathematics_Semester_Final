---
title: "DM-6.6 · Binomial Theorem"
tags:
  - numerical-methods
  - discrete-mathematics
  - topicwise
---

# DM-6.6 · Binomial Theorem

Every block below is copied from `../answers_exam_style/`, which is the
only place an answer is authored. A number here is the same number, character
for character, as the one it came from.


### [2023 Q.8(c)]

**Question.** Briefly describe the Binomial theorem, and what is the coefficient of $x^{12}y^{13}$ in the expansion of $(2x - 3y)^{25}$?

**Solution.**

**The theorem.** For positive integers $m$ and $n$,

$$
(x + y)^n = \sum_{r=0}^{n}\binom{n}{r}x^{n-r}y^r
$$

The general term is

$$
T_{r+1} = \binom{n}{r}x^{n-r}y^r, \qquad r = 0, 1, \ldots, n
$$

A proof by induction on $n$: the case $n = 1$ is immediate, and the step follows
from Pascal's identity $\binom{n+1}{r} = \binom{n}{r} + \binom{n}{r-1}$ applied to
$(x+y)^{n+1} = (x+y)^n \cdot (x+y)$.

**Applying it.** With $x \to 2x$ and $y \to -3y$ and $n = 25$,

$$
(2x - 3y)^{25} = \sum_{r=0}^{25}\binom{25}{r}(2x)^{25-r}(-3y)^r
$$

**Identify the term.** A general term carries $x^{25-r}y^r$. For
$x^{12}y^{13}$ we need

$$
25 - r = 12 \quad \text{and} \quad r = 13
$$

Both give $r = 13$, and the powers $12 + 13 = 25$ check out.

**The coefficient.**

$$
\text{coefficient} = \binom{25}{13}(2)^{12}(-3)^{13}
$$

Since $\binom{25}{13} = \binom{25}{12} = 5200300$,

$$
= 5200300 \times 4096 \times (-1594323)
$$

$$
\boxed{\text{coefficient of } x^{12}y^{13} = -33959763545702400}
$$

> [!info] Check
> Expanding $(2x - 3y)^{25}$ directly and reading off the coefficient of
> $x^{12}y^{13}$ returns $-33959763545702400$, the same value as
> $5200300 \times 4096 \times (-1594323)$. The three factors multiply out as
> $21300428800 \times (-1594323)$, confirming the product.

> [!warning] Two sign and index traps
> **The sign is negative.** The exponent of $y$ is $r = 13$, which is odd, and
> $(-3)^{13}$ is negative. Forgetting the sign of $(-3y)^{13}$ is the most
> common error here.
>
> **The power of 2 belongs to $x$, not to $y$.** $(2x)^{12}$ gives
> $2^{12} = 4096$. Writing $2^{13}$ instead is the second most common error.
> Since the exponent of $x$ is $n - r$, the factor $2$ carries $n - r = 12$
> while the factor $-3$ carries $r = 13$. The exponents of $x$ and $y$ in a term
> determine the base, hence the factor part.

---
