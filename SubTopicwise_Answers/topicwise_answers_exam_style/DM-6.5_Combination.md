---
title: "DM-6.5 · Combination"
tags:
  - numerical-methods
  - discrete-mathematics
  - topicwise
---



[🏠 Subtopic Index](00_Index.md) | [← Prev: DM-6.3 Pigeonhole Principle](DM-6.3_Pigeonhole_Principle.md) | [Next: DM-6.6 Binomial Theorem →](DM-6.6_Binomial_Theorem.md)

---

# DM-6.5 · Combination

Every block below is copied from `../answers_exam_style/`, which is the
only place an answer is authored. A number here is the same number, character
for character, as the one it came from.


### [2023 Q.8(b)]

**Question.** A group of 30 people have been trained as astronauts to go on the first mission to mars. How many ways are there to select a crew of six people to go on this mission (assuming all crew members have the same job)?

**Solution.**

**Setting up.** Selection is without regard to order, so order does **not**
matter. Every crew member has the same job, so there is no assignment to count.
This is a combination, $\binom{n}{r}$, not a permutation.

$$
\text{Ways} = \binom{30}{6} = \frac{30!}{6!\,24!}
$$

**Computing the factorial ratio.**

$$
= \frac{30 \cdot 29 \cdot 28 \cdot 27 \cdot 26 \cdot 25}{6 \cdot 5 \cdot 4 \cdot 3 \cdot 2 \cdot 1} = \frac{30 \cdot 29 \cdot 28 \cdot 27 \cdot 26 \cdot 25}{720}
$$

Group the numerator in pairs:

$$
30 \cdot 29 = 870, \qquad 28 \cdot 27 = 756, \qquad 26 \cdot 25 = 650
$$

$$
870 \times 756 \times 650 = 427518000
$$

$$
\frac{427518000}{720} = 593775
$$

$$
\boxed{\binom{30}{6} = 593775 \text{ ways}}
$$

> [!info] Check
> Three routes agree:
> - $\frac{30!}{6!\,24!}$ evaluated directly gives $593775$
> - the paired product $\frac{870 \times 756 \times 650}{720}$ gives $\frac{427518000}{720} = 593775$
> - $\binom{30}{6}$ from an independent implementation gives $593775$
>
> Note $427518000 = 720 \times 593775$, which is the ordered count appearing below.

> [!warning] Do not split the numerator into three pairs and cancel incorrectly
> A tempting grouping is $\frac{30\cdot29}{2}\times\frac{28\cdot27}{6}\times 26\cdot25
> = 435 \times 126 \times 650 = 35626500$, which is **60 times too large**.
>
> The reason is that $2$ and $6$ cancel only $12$ of the required $720$. To
> cancel correctly the three divisors must multiply to $720$, for example
> $6! = 6 \times 120$ split as $2 \times 360$, or simply divide the whole
> numerator by $720$ in one step. Cancelling pairwise is where this answer most
> often goes wrong, and the error is silent because the arithmetic still looks
> tidy.

> [!note] Why the assumption matters
> "All crew members have the same job" is what makes this $\binom{30}{6}$. If
> the crew had a commander, the count would be $30 \times \binom{29}{5} =
> 30 \times 118755 = 3562650$, choosing the commander first. And if order were
> counted, $\frac{30!}{24!} = 427518000$, which is exactly $6! = 720$ times
> larger, because each crew could be seated in $720$ orders. The assumption in
> the question removes precisely that factor.

---

[🏠 Subtopic Index](00_Index.md) | [← Prev: DM-6.3 Pigeonhole Principle](DM-6.3_Pigeonhole_Principle.md) | [Next: DM-6.6 Binomial Theorem →](DM-6.6_Binomial_Theorem.md)
