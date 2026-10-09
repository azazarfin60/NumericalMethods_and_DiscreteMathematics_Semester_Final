---
title: "NM-2.5 · Secant Method"
tags:
  - numerical-methods
  - discrete-mathematics
  - topicwise
---

# NM-2.5 · Secant Method

Every block below is copied from `../answers_explanation/`. The reasoning
is written once, in the year-wise file, and is not restated here.


### [2017 Q.2(c)]

**Question.** Find the positive root of the equation $f(x) = x^3 - 3x^2 - x - 3 = 0$ by secant method (Use four iterations only).

*[Marks: 04]*

**Solution.**

**What the secant method is.** Replace $f'(x_n)$ by a finite difference through
the last two iterates:

$$x_{n+1} = x_n - \frac{f(x_n)(x_n - x_{n-1})}{f(x_n) - f(x_{n-1})}$$

It needs one function evaluation per step instead of two, keeps roughly the
superlinear convergence of Newton, and has no derivative to divide by. The
price is that it needs *two* starting values and no longer guarantees to
converge from anywhere.

**Sign check.** $f(2) = -9$ and $f(4) = 64 - 48 - 4 - 3 = 9$, so a positive
root lies in $(2, 4)$. Take $x_0 = 2$, $x_1 = 3$, for which
$f(2) = -9$ and $f(3) = 27 - 27 - 3 - 3 = -6$.

**Iteration 1.**

$$x_2 = 3 - \frac{(-6)(3 - 2)}{(-6) - (-9)} = 3 - \frac{-6}{3} = 5.0000$$

**Iteration 2.** $f(5) = 125 - 75 - 5 - 3 = 42$.

$$x_3 = 5 - \frac{42(5 - 3)}{42 - (-6)} = 5 - \frac{84}{48} = 3.2500$$

**Iteration 3.** $f(3.25) = 34.328125 - 31.6875 - 6.25 = -3.609375$.

$$x_4 = 3.25 - \frac{(-3.609375)(3.25 - 5)}{(-3.609375) - 42} = 3.25 + \frac{6.316406}{45.609375} = 3.388489$$

**Iteration 4.** $f(3.388489) = 38.906149 - 34.445573 - 6.388489 = -1.927914$.

$$x_5 = 3.388489 - \frac{(-1.927914)(3.388489 - 3.25)}{(-1.927914) - (-3.609375)} = 3.388489 + \frac{0.266995}{1.681461} = 3.547276$$

**The four iterations.**

| Iteration | $x_n$ | $f(x_n)$ |
| :--: | :-- | :-- |
| 1 | $5.000000$ | $42.000000$ |
| 2 | $3.250000$ | $-3.609375$ |
| 3 | $3.388489$ | $-1.927914$ |
| 4 | $3.547276$ | $0.339189$ |

$$\boxed{x \approx 3.547 \text{ after four iterations}}$$

> [!warning] Read the sequence before you trust it
> The four values are $5.0000, 3.2500, 3.3885, 3.5473$: overshoot high,
> undershoot low, overshoot again. The secant is *not* monotone in general,
> and the reason is visible in the last column. The first iterate lands at $x=5$
> where $f$ is $+42$, a long way outside the bracket $(2,4)$, because the
> chord through $(2,-9)$ and $(3,-6)$ extrapolates. From there the method
> oscillates into the bracket and is still oscillating on the fourth step.
>
> A student who expects each iterate to improve on the last will either stop at
> $3.3885$ (thinking it is converging and has stopped) or count $3.3885$ as the
> fourth iterate and report it. The question says four iterations, and the
> answer is the value *after* four.

> [!info] Confirming the value, and the alternative reading of the paper
> The exact real root is $x = 3.525102$, so $3.547276$ is $0.022$ away: four
> iterations from a bad start are simply not enough, and that is the answer the
> question asked for. Starting from $x_0 = 3.5$, $x_1 = 3.6$ instead, which is
> much closer to the root, gives $3.525102$ after four iterations. Two starts,
> one from far out and one from near, both bracketing $3.525102$, is the
> evidence that $3.547$ is the honest outcome of the specified procedure
> rather than of an arithmetic slip.
>
> The constant term is faintly printed in the original. Read as $-3$ it gives
> the root above; read as $-1$ the equation becomes $x^3 - 3x^2 - x - 1 = 0$,
> whose exact root is $3.382976$ and which gives $3.3888$ from the same start
> pair. Both are reported in the answer script, with the $-3$ reading primary
> because it produces the sign change in the printed interval.

---
