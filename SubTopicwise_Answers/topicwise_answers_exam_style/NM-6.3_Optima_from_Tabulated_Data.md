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

Every block below is copied from `../answers_exam_style/`, which is the
only place an answer is authored. A number here is the same number, character
for character, as the one it came from.


### [2018 Q.5(b)]

**Question.** From the following table find $x$, correct to two decimal places for which $y$ is maximum and find this value of $y$.

**Solution.**

| $x$ | 1.2 | 1.3 | 1.4 | 1.5 | 1.6 |
| :---: | :---: | :---: | :---: | :---: | :---: |
| $y$ | 0.9320 | 0.9636 | 0.9855 | 0.9975 | 0.9996 |

**The differences.** With $h = 0.1$:

| | 0.9320 | 0.9636 | 0.9855 | 0.9975 | 0.9996 |
| :-- | :-- | :-- | :-- | :-- | :-- |
| $\Delta$ | | $0.0316$ | $0.0219$ | $0.0120$ | $0.0021$ |
| $\Delta^2$ | | | $-0.0097$ | $-0.0099$ | $-0.0099$ |
| $\Delta^3$ | | | | $-0.0002$ | $0.0000$ |
| $\Delta^4$ | | | | | $0.0002$ |

The first differences are all positive but falling, and the last of them,
$0.0021$, is small, so the maximum lies just inside the end of the table, close
to but before $x = 1.6$. The backward difference form is the natural one to use
from there, since the maximum is at the far end of the table.

**The backward derivative.** At $x = x_4 = 1.6$, with $q = (x - x_4)/h$,

$$\frac{dy}{dx} = \frac{1}{h}\left[\nabla y_4 + \frac{2q + 1}{2}\nabla^2 y_4 + \frac{3q^2 + 6q + 2}{6}\nabla^3 y_4 + \frac{4q^3 + 18q^2 + 22q + 6}{24}\nabla^4 y_4\right]$$

The backward differences at $x_4$ are

$$\nabla y_4 = 0.0021, \qquad \nabla^2 y_4 = -0.0099, \qquad \nabla^3 y_4 = 0.0000, \qquad \nabla^4 y_4 = 0.0002$$

**Set $\dfrac{dy}{dx} = 0$.** Since $\nabla^3 y_4 = 0$ and $\nabla^4 y_4$ is
small, the stationary point is set by the first two terms:

$$0.0021 + \frac{2q + 1}{2}(-0.0099) = 0$$

$$0.0021 = (q + 0.5)(0.0099)$$

$$q + 0.5 = \frac{0.0021}{0.0099} = 0.212121$$

$$q = -0.287879$$

$$x = x_4 + hq = 1.6 + 0.1(-0.287879) = 1.5712$$

**Evaluate $y$ there.** Using the backward Newton polynomial with all five
points,

$$y = y_4 + q\nabla y_4 + \frac{q(q+1)}{2}\nabla^2 y_4 + \frac{q(q+1)(q+2)}{6}\nabla^3 y_4 + \frac{q(q+1)(q+2)(q+3)}{24}\nabla^4 y_4$$

At $q = -0.287879$:

$$y = 0.9996 + (-0.287879)(0.0021) + \frac{(-0.287879)(0.712121)}{2}(-0.0099) + 0 + \frac{(-0.287879)(0.712121)(1.712121)(2.712121)}{24}(0.0002)$$

$$y = 0.9996 - 0.0006045 + 0.0010148 - 0.0000079 = 1.0000023$$

$$\boxed{x = 1.57 \text{ (correct to two decimal places)}, \qquad y_{\max} = 1.0000}$$

> [!info] Check against the full five-point polynomial
> Fitting a single polynomial through all five points by Lagrange interpolation
> gives $y = \dfrac{x^4}{12} - \dfrac{29x^3}{60} + \dfrac{133x^2}{240} + \dfrac{409x}{750} + \dfrac{71}{500}$.
> Setting $y' = 0$, that is
> $y' = \dfrac{x^3}{3} - \dfrac{29x^2}{20} + \dfrac{133x}{120} + \dfrac{409}{750}$, and
> solving gives $x = 1.5713$, with $y = 1.0000023$. The derivatives and values agree
> with the backward-difference route to the digits shown, and the $\Delta^4$ term
> shifts the stationary point by $9.1\times10^{-5}$. A maximum is confirmed
> because $y'' = x^2 - \dfrac{29x}{10} + \dfrac{133}{120}$ evaluates to
> $-0.9795$ at $x = 1.5713$, which is negative. The quartic has three real
> critical points, $x = -0.3344$, $x = 1.5713$ and $x = 3.1131$, and $1.5713$
> is the only one inside the table; the other two lie outside $[1.2, 1.6]$ and so
> cannot be the maximum of the tabulated function.

---

[🏠 Subtopic Index](00_Index.md) | [← Prev: NM-6.2 One-Dimensional Unconstrained Optimization](NM-6.2_One_Dimensional_Unconstrained_Optimization.md) | [Next: NM-7.1 Basis & Difference Formulas →](NM-7.1_Basis_and_Difference_Formulas.md)
