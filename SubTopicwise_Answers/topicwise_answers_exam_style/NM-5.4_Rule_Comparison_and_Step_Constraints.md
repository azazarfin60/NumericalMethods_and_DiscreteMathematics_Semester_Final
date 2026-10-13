---
title: "NM-5.4 · Rule Comparison & Step Constraints"
tags:
  - numerical-methods
  - discrete-mathematics
  - topicwise
---


[🏠 Subtopic Index](00_Index.md) | [← Prev: NM-5.3 Simpson's 3/8 Rule](NM-5.3_Simpsons_3_8_Rule.md) | [Next: NM-5.5 Romberg's Method →](NM-5.5_Rombergs_Method.md)

---

# NM-5.4 · Rule Comparison & Step Constraints

Every block below is copied from `../answers_exam_style/`, which is the
only place an answer is authored. A number here is the same number, character
for character, as the one it came from.


### [2020 Q.6(a), 2023 Q.4(c)]

**Appeared in:** 2020 Q.6(a), 2023 Q.4(c)

**Question.** Compare Simpson's $1/3$rd and $3/8$th rules.

**Solution.**

Both are **Newton-Cotes** rules: they fit a polynomial through the data at
equally spaced nodes and integrate that polynomial exactly over the panel. They
differ in how many nodes each panel uses and therefore in which interval counts
each admits.

| | Simpson's $1/3$ | Simpson's $3/8$ |
| :-- | :-- | :-- |
| Subintervals per panel | 2 | 3 |
| Nodes per panel | 3 | 4 |
| Weights | $1,\ 4,\ 1$ | $1,\ 3,\ 3,\ 1$ |
| Prefactor | $\dfrac{h}{3}$ | $\dfrac{3h}{8}$ |
| Panel interval count | Must be **even** | Must be a **multiple of 3** |
| Total intervals $n$ | Even | Multiple of 3 |
| Order of accuracy | 4 | 4 |
| Leading error term | $-\dfrac{h^5}{90}f^{(4)}$ | $-\dfrac{3h^5}{80}f^{(4)}$ |
| Error constant | $\frac{1}{90} = 0.0111$ | $\frac{3}{80} = 0.0375$ |

**Both are fourth order**, so both need a function with $f^{(4)}$ continuous
over the range. Neither is fourth order on a function with a discontinuous
fourth derivative, and neither is safe near a vertical asymptote or a jump.

**The accuracy difference.** With the same $h$, Simpson's $3/8$ has a leading
error constant $3.375$ times larger than $1/3$. So for equal $h$, **$1/3$ is more
accurate**, and $1/3$ is the default choice.

**The one place $3/8$ wins.** When the total interval count is odd, $1/3$ is
inapplicable while $3/8$ can still be used, provided the count is a multiple of
$3$. Five intervals is the standard case: $1/3$ is stuck, $3/8$ takes three of
them and something else takes two. That exact situation is in Q.6(b) below, and it is why the rule is worth
knowing.

**Standard mixed strategy** for an odd $n$ not divisible by $3$, for example
$n = 5$: apply $3/8$ to the last three intervals and $1/3$ to the remaining two,
or apply $1/3$ to the largest even block and the trapezoid rule to the leftover
one interval. Both appear in Q.6(b).

**Why the error behaves as it does.** A $3$-node panel interpolates a quadratic,
whose integration error involves $f''$. A $4$-node panel interpolates a cubic,
involving $f^{(4)}$. Symmetry about the panel centre cancels the odd-order terms
in both cases, which is why both reach fourth order rather than third.

$$
\boxed{\text{Both are fourth order; } 1/3 \text{ is more accurate at equal } h \text{ but needs an even interval count}}
$$

---

[🏠 Subtopic Index](00_Index.md) | [← Prev: NM-5.3 Simpson's 3/8 Rule](NM-5.3_Simpsons_3_8_Rule.md) | [Next: NM-5.5 Romberg's Method →](NM-5.5_Rombergs_Method.md)
