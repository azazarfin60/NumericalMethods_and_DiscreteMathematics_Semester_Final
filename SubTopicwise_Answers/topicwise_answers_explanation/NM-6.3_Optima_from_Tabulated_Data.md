---
title: "NM-6.3 · Optima from Tabulated Data"
tags:
  - numerical-methods
  - discrete-mathematics
  - topicwise
---


[🏠 Subtopic Index](00_Index.md) | [← Prev: NM-6.2 One-Dimensional Unconstrained Optimization](NM-6.2_One_Dimensional_Unconstrained_Optimization.md) | [Next: NM-7.1 Basis & Difference Formulas →](NM-7.1_Basis_and_Difference_Formulas.md)

---

# NM-6.3 · Optima from Tabulated Data

Every block below is copied from `../answers_explanation/`. The reasoning
is written once, in the year-wise file, and is not restated here.


### [2018 Q.5(b)]

**Question.** From the following table find $x$, correct to two decimal places for which $y$ is maximum and find this value of $y$.

*[Marks: 06]*

**Solution.**

| $x$ | 1.2 | 1.3 | 1.4 | 1.5 | 1.6 |
| :---: | :---: | :---: | :---: | :---: | :---: |
| $y$ | 0.9320 | 0.9636 | 0.9855 | 0.9975 | 0.9996 |

**Step 1, find the direction of the answer before computing anything.** Build
the difference table.

| | 0.9320 | 0.9636 | 0.9855 | 0.9975 | 0.9996 |
| :-- | :-- | :-- | :-- | :-- | :-- |
| $\Delta$ | | $0.0316$ | $0.0219$ | $0.0120$ | $0.0021$ |
| $\Delta^2$ | | | $-0.0097$ | $-0.0099$ | $-0.0099$ |
| $\Delta^3$ | | | | $-0.0002$ | $0.0000$ |
| $\Delta^4$ | | | | | $0.0002$ |

All four first differences are *positive*, so $y$ is still rising at $x = 1.5$.
But the last of them, $0.0021$, is small and the second differences are all
negative, so $y$ is levelling off and the peak lies just *inside* the end of the
table, close to but before $x = 1.6$. If you read that last $0.0021$ as having
"already changed sign" and go looking beyond $1.6$, you will extrapolate
outside the data and get a different answer.

**Step 2, use the backward form, because the maximum is at the far end.** At
$x_4 = 1.6$ with $q = (x - x_4)/h$,

$$\frac{dy}{dx} = \frac{1}{h}\left[\nabla y_4 + \frac{2q + 1}{2}\nabla^2 y_4 + \frac{3q^2 + 6q + 2}{6}\nabla^3 y_4 + \frac{4q^3 + 18q^2 + 22q + 6}{24}\nabla^4 y_4\right]$$

with

$$\nabla y_4 = 0.0021, \qquad \nabla^2 y_4 = -0.0099, \qquad \nabla^3 y_4 = 0.0000, \qquad \nabla^4 y_4 = 0.0002$$

**Step 3, set the derivative to zero.** With $\nabla^3 y_4 = 0$ and
$\nabla^4 y_4$ tiny, the stationary point is set almost entirely by the first
two terms:

$$0.0021 + \frac{2q + 1}{2}(-0.0099) = 0 \implies (q + 0.5)(0.0099) = 0.0021$$

$$q + 0.5 = \frac{0.0021}{0.0099} = 0.212121, \qquad q = -0.287879$$

$$x = x_4 + hq = 1.6 + 0.1(-0.287879) = 1.5712$$

The negative $q$ is the answer to "which side", stated numerically: the maximum
is inside the table.

**Step 4, evaluate $y$ there** with the full five-point backward polynomial,

$$y = y_4 + q\nabla y_4 + \frac{q(q+1)}{2}\nabla^2 y_4 + \frac{q(q+1)(q+2)}{6}\nabla^3 y_4 + \frac{q(q+1)(q+2)(q+3)}{24}\nabla^4 y_4$$

$$y = 0.9996 + (-0.287879)(0.0021) + \frac{(-0.287879)(0.712121)}{2}(-0.0099) + 0 + \frac{(-0.287879)(0.712121)(1.712121)(2.712121)}{24}(0.0002)$$

$$y = 0.9996 - 0.0006045 + 0.0010148 - 0.0000079 = 1.0000023$$

$$\boxed{x = 1.57 \text{ (correct to two decimal places)}, \qquad y_{\max} = 1.0000}$$

> [!note] Why $y_{\max} = 1.0000$ looks odd and is not an error
> The table's largest entry is $0.9996$, and the interpolated maximum comes out
> at $1.0000023$, which is just *above* $1$. That is exactly what a parabola
> through five points should do: the points at $1.5$ and $1.6$ are still rising
> at a decreasing rate, so the fitted curve peaks slightly above the last
> sample. Rounded to four decimals it reads $1.0000$. Do not "correct" it to
> $0.9996$; the tabulated value and the interpolated maximum are different
> quantities.

> [!info] Confirming with a completely separate route
> Fitting one polynomial through all five points by Lagrange interpolation gives
> $y = \dfrac{x^4}{12} - \dfrac{29x^3}{60} + \dfrac{133x^2}{240} +
> \dfrac{409x}{750} + \dfrac{71}{500}$, which reproduces $0.9320$, $0.9636$,
> $0.9855$, $0.9975$, $0.9996$ at $1.2$ through $1.6$ exactly. Differentiating,
> $y' = \dfrac{x^3}{3} - \dfrac{29x^2}{20} + \dfrac{133x}{120} +
> \dfrac{409}{750}$, and $y' = 0$ has three real roots, $x = -0.3344$,
> $x = 1.5713$ and $x = 3.1131$. Only $1.5713$ lies inside $[1.2, 1.6]$, so it
> is the only candidate, and $y$ there is $1.0000023$, matching the
> backward-difference route. The $\Delta^4$ term shifted the stationary point by
> $9.1\times10^{-5}$, which is why the two routes agree to the digits shown.
>
> Confirming it is a *maximum*: $y'' = x^2 - \dfrac{29x}{10} + \dfrac{133}{120}$
> evaluates to $-0.9795$ at $x = 1.5713$, which is negative. And the sign is
> forced by the second difference row, which is negative throughout, so $y$
> must be concave near the peak regardless of the polynomial used.

---

[🏠 Subtopic Index](00_Index.md) | [← Prev: NM-6.2 One-Dimensional Unconstrained Optimization](NM-6.2_One_Dimensional_Unconstrained_Optimization.md) | [Next: NM-7.1 Basis & Difference Formulas →](NM-7.1_Basis_and_Difference_Formulas.md)
