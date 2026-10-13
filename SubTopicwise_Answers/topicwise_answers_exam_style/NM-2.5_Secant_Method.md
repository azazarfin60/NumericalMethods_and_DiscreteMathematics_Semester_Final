---
title: "NM-2.5 · Secant Method"
tags:
  - numerical-methods
  - discrete-mathematics
  - topicwise
---


[🏠 Subtopic Index](00_Index.md) | [← Prev: NM-2.4 Newton-Raphson Method](NM-2.4_Newton_Raphson_Method.md) | [Next: NM-2.6 Method Comparison & Convergence →](NM-2.6_Method_Comparison_and_Convergence.md)

---

# NM-2.5 · Secant Method

Every block below is copied from `../answers_exam_style/`, which is the
only place an answer is authored. A number here is the same number, character
for character, as the one it came from.


### [2017 Q.2(c)]

**Question.** Find the positive root of the equation $f(x) = x^3 - 3x^2 - x - 3 = 0$ by secant method (Use four iterations only).

**Solution.**

*Note.* The constant term is faintly printed in the original. It is read here as
$-3$, giving $f(x) = x^3 - 3x^2 - x - 3$, and the alternative reading $-1$ is
discussed at the end.

**Sign check.** $f(0) = -3$, $f(1) = -6$, $f(2) = 8 - 12 - 2 - 3 = -9$, and
$f(4) = 64 - 48 - 4 - 3 = 9$. The sign changes between $2$ and $4$, so a
positive root lies in that interval. Take $x_0 = 2$ and $x_1 = 3$, for which
$f(2) = -9$ and $f(3) = 27 - 27 - 3 - 3 = -6$.

**The secant iteration.**

$$x_{n+1} = x_n - \frac{f(x_n)(x_n - x_{n-1})}{f(x_n) - f(x_{n-1})}$$

**Iteration 1.**

$$x_2 = 3 - \frac{(-6)(3 - 2)}{(-6) - (-9)} = 3 - \frac{-6}{3} = 3 + 2 = 5.0000$$

**Iteration 2.** $f(5) = 125 - 75 - 5 - 3 = 42$.

$$x_3 = 5 - \frac{42(5 - 3)}{42 - (-6)} = 5 - \frac{84}{48} = 5 - 1.7500 = 3.2500$$

**Iteration 3.** $f(3.25) = 3.25^3 - 3(3.25)^2 - 3.25 - 3 = 34.328125 - 31.6875 - 6.25 = -3.609375$.

$$x_4 = 3.25 - \frac{(-3.609375)(3.25 - 5)}{(-3.609375) - 42} = 3.25 - \frac{6.316406}{-45.609375} = 3.25 + 0.138489 = 3.388489$$

**Iteration 4.** $f(3.388489) = 38.906148 - 34.445573 - 6.388489 = -1.927914$.

$$x_5 = 3.388489 - \frac{(-1.927914)(3.388489 - 3.25)}{(-1.927914) - (-3.609375)} = 3.388489 + \frac{0.266995}{1.681461} = 3.547276$$

**The four iterations.**

| Iteration | $x_n$ | $f(x_n)$ |
| :--: | :-- | :-- |
| 1 | $5.000000$ | $42.000000$ |
| 2 | $3.250000$ | $-3.609375$ |
| 3 | $3.388489$ | $-1.927914$ |
| 4 | $3.547276$ | $0.339189$ |

$$\boxed{x \approx 3.547 \text{ after four iterations}}$$

> [!info] Check by substitution and by a second pair of starts
> Substituting $x = 3.547276$ gives $f = 0.339189$, still a long way from zero,
> so the answer is the value after four steps as asked rather than the root.
> Solving the cubic exactly gives the real root $x = 3.525102$, so the four
> iterations are still $0.022$ away. Starting the secant from $x_0 = 3.5$,
> $x_1 = 3.6$ instead, which is much closer to the root, gives $3.525102$ after
> four iterations, converging on the exact root. That the two starts bracket
> $3.525102$ confirms $3.547$ is the outcome of the requested imperfect start,
> not of an arithmetic slip.
>
> A note on reading the four-step sequence: the secant is not monotone, so
> $5.0000, 3.2500, 3.3885, 3.5473$ overshoots low, undershoots, then overshoots
> again. A student expecting monotone convergence after the first step will
> misread the third value and stop early.

> [!note] On the faint constant term
> If the constant were read as $-1$, giving $f(x) = x^3 - 3x^2 - x - 1$, the
> exact root is $x = 3.382976$ and the same start pair $x_0 = 2$, $x_1 = 3$
> gives $3.3888$ after four iterations. Both readings are handled here, with the
> $-3$ reading presented as the primary answer because it is the one that
> yields the sign change in the printed interval and the cleaner arithmetic.

---

[🏠 Subtopic Index](00_Index.md) | [← Prev: NM-2.4 Newton-Raphson Method](NM-2.4_Newton_Raphson_Method.md) | [Next: NM-2.6 Method Comparison & Convergence →](NM-2.6_Method_Comparison_and_Convergence.md)
