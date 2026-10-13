---
title: "NM-5.5 · Romberg's Method"
tags:
  - numerical-methods
  - discrete-mathematics
  - topicwise
---



[🏠 Subtopic Index](00_Index.md) | [← Prev: NM-5.4 Rule Comparison & Step Constraints](NM-5.4_Rule_Comparison_and_Step_Constraints.md) | [Next: NM-5.6 Error Analysis in Integration →](NM-5.6_Error_Analysis_in_Integration.md)

---

# NM-5.5 · Romberg's Method

Every block below is copied from `../answers_explanation/`. The reasoning
is written once, in the year-wise file, and is not restated here.


### [2021 Q.8(b), 2023 Q.2(c)]

**Appeared in:** 2021 Q.8(b), 2023 Q.2(c)

**Question.** Use Romberg's method to compute: $\int_1^2 \frac{1}{2+x}\,dx$. Consider $h = 0.5, 0.25, 0.125$.

*[Marks: 04, CO: 2]*

**Solution.**

**Step 1. The first column, composite trapezoid.**

$$
T_n = \frac{h}{2}\left[f_0 + 2f_1 + \cdots + 2f_{n-1} + f_n\right], \qquad f_i = \frac{1}{2+x_i}
$$

At $h = 0.5$, $n = 2$, nodes $x = 1, 1.5, 2$:

$$
T_2 = \frac{0.5}{2}\left[\frac{1}{3} + 2\cdot\frac{1}{3.5} + \frac{1}{4}\right] = 0.25\left[0.333333 + 0.571429 + 0.25\right] = 0.288690
$$

At $h = 0.25$, $n = 4$:

$$
T_4 = \frac{0.25}{2}\left[\frac{1}{3} + 2\left(\frac{1}{3.25} + \frac{1}{3.5} + \frac{1}{3.75} + \frac{1}{4.25}\right) + \frac{1}{4}\right] = 0.287935
$$

At $h = 0.125$, $n = 8$:

$$
T_8 = 0.287745
$$

**Step 2. Second column.** The trapezoid rule has $O(h^2)$ error, so extrapolate
with the factor $4^1 - 1 = 3$:

$$
R_{k,1} = R_{k,0} + \frac{R_{k,0} - R_{k-1,0}}{4 - 1}
$$

**Step 3. Third column.** The result above is Simpson's rule, carrying $O(h^4)$,
so the factor is $4^2 - 1 = 15$:

$$
R_{k,2} = R_{k,1} + \frac{R_{k,1} - R_{k-1,1}}{16 - 1}
$$

**The table.**

$$
\begin{array}{c|ccc}
R_{k,0} & R_{k,1} & R_{k,2} \\
\hline
0.288690 & & \\
0.287935 & 0.287683 & \\
0.287745 & 0.287682 & 0.287682
\end{array}
$$

Row 2: $0.287935 + \frac{0.287935 - 0.288690}{3} = 0.287935 - 0.000252 = 0.287683$
Row 3, column 1: $0.287745 + \frac{0.287745 - 0.287935}{3} = 0.287745 - 0.000063 = 0.287682$
Row 3, column 2: $R_{3,2} = R_{3,1} + \frac{R_{3,1} - R_{2,1}}{15}$

Taken literally at the six decimals the table prints, this gives
$0.287682 - \frac{10^{-6}}{15} = 0.2876819$. Carried unrounded, which is what the
answer below uses, the same line gives $0.2876820735$, since the unrounded entries
are $R_{2,1} = 0.2876832$ and $R_{3,1} = 0.2876821$.

$$\boxed{I \approx 0.2876821}$$

> [!info] Check against the exact integral
> $$\int_1^2\frac{dx}{2+x} = \ln(2+x)\Big|_1^2 = \ln 4 - \ln 3 = \ln\frac{4}{3} = 0.2876820725$$
> The Romberg value differs by $1.05\times10^{-9}$, a relative error of
> $3.6\times10^{-9}$.
>
> For comparison, plain composite Simpson with $n = 8$ gives $0.2876821408$, whose
> relative error is $2.4\times10^{-7}$. **Romberg is about 65 times more accurate
> from the same function values**, because each column only recombines entries
> already in the table. No extra work.

> [!warning] When the last row stops moving, that is the method working
> The left column converges slowly and alternates,
> $0.2887 \to 0.2879 \to 0.2877$, because the trapezoid error is negative and
> shrinking like $h^2$. Each step right multiplies the accuracy by about $4^2 = 16$
> or better.
>
> Three levels give roughly eighth-order accuracy from a second-order rule. That
> is the whole point of Romberg: **the third column is doing $h^2 \to h^4 \to
> h^8$**, and it costs only arithmetic.
>
> Watch the printed values here. The third column entry barely differs from the
> second, because by then the numbers are already agreeing to six decimals. That
> is the expected appearance of convergence, not a sign the calculation has stalled.

---

---

**Also asked here.**

- *2022 Q.3(a)* is the same question as [[NM-5.1_Trapezoidal_Rule|NM-5.1]], which is written in `NM-5.1`.

---

[🏠 Subtopic Index](00_Index.md) | [← Prev: NM-5.4 Rule Comparison & Step Constraints](NM-5.4_Rule_Comparison_and_Step_Constraints.md) | [Next: NM-5.6 Error Analysis in Integration →](NM-5.6_Error_Analysis_in_Integration.md)
