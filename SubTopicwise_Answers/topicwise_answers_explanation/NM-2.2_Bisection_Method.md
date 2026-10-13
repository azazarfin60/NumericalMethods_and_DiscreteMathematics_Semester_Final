---
title: "NM-2.2 · Bisection Method"
tags:
  - numerical-methods
  - discrete-mathematics
  - topicwise
---


[🏠 Subtopic Index](00_Index.md) | [← Prev: NM-2.1 Fundamentals & Classification](NM-2.1_Fundamentals_and_Classification.md) | [Next: NM-2.3 False Position / Regula Falsi →](NM-2.3_False_Position_and_Regula_Falsi.md)

---

# NM-2.2 · Bisection Method

Every block below is copied from `../answers_explanation/`. The reasoning
is written once, in the year-wise file, and is not restated here.


### [2017 Q.3(c)]

**Question.** Explain the bisection method for finding a real root of the equation $f(x) = 0$ and write an algorithm for its implementation with a test for relative accuracy.

*[Marks: 06]*

**Solution.**

**The method.** Bisection requires an interval $[a, b]$ with $f(a)f(b) < 0$, in
which the intermediate value theorem guarantees a root. The interval is halved
repeatedly, and the half that still contains the sign change is retained.

**Algorithm.**

1. Read $f(x)$, the relative tolerance $\varepsilon_r$, and the maximum
   iteration count $N$.
2. Accept the ends $a$ and $b$.
3. Compute $f(a)$ and $f(b)$. If $f(a)f(b) > 0$, report that the interval does
   not bracket a root and stop.
4. Set the midpoint $c = \dfrac{a + b}{2}$ and compute $f(c)$.
5. **Test for relative accuracy.** Compute
   $$|e_a| = \left|\frac{c - c_{\text{old}}}{c}\right|\times 100\%$$
   If $|e_a| < \varepsilon_r$, or if $|f(c)| < \varepsilon$, accept $c$ and stop.
6. If $f(a)f(c) < 0$, set $b = c$; otherwise set $a = c$. Store the previous
   midpoint as $c_{\text{old}}$.
7. If the iteration count exceeds $N$, report non-convergence and stop.
   Otherwise return to step 4.

**The relative accuracy test, in detail.** The approximate relative error
after step $k$ is

$$|e_a|_k = \left|\frac{c_k - c_{k-1}}{c_k}\right|\times100\%$$

This measures the *change between successive midpoints*, not the distance from
the current midpoint to the true root. Because the interval halves each time,
$|e_a|$ roughly halves each time too, so it is a reliable monitor: when it
falls below $\varepsilon_r$ the remaining uncertainty is at most the current
interval width, and the reported relative error is a valid statement of how far
the answer may be from the truth.

**Worked example.** For $f(x) = x^3 - x - 2$ on $[1, 2]$:

| Iteration | $a$ | $b$ | $c = (a+b)/2$ | $f(c)$ | $b - a$ |
| :--: | :--: | :--: | :--: | :--: | :--: |
| 1 | 1 | 2 | 1.500000 | $-0.1250$ | 1 |
| 2 | 1.5 | 2 | 1.750000 | $1.6094$ | 0.5 |
| 3 | 1.5 | 1.75 | 1.625000 | $0.6660$ | 0.25 |
| 4 | 1.5 | 1.625 | 1.562500 | $0.2522$ | 0.125 |
| 5 | 1.5 | 1.5625 | 1.531250 | $0.0591$ | 0.0625 |
| 6 | 1.5 | 1.53125 | 1.515625 | $-0.0341$ | 0.03125 |

The true root is $x = 1.5214$. After six halvings the interval width is
$0.03125$, so the half-width $0.015625$ bounds the error and the approximate
relative error is under $1.1\%$. The number of iterations needed for a given
tolerance is known in advance:

$$n = \left\lceil \log_2\frac{b - a}{\varepsilon}\right\rceil$$

> [!warning] The bracket must be carried, not just the midpoint
> Look down the $a$ and $b$ columns: $a$ stays at $1$ until iteration 6, and
> $b$ walks down from $2$. That is forced by the function. $f$ is negative on
> $[1, 1.5214]$ and positive above it, so every midpoint *above* the root sends
> $b$ down and every midpoint *below* it sends $a$ up. A table in which both ends
> move in the same iteration has a sign error in step 6, and it will still print
> plausible midpoints, because the midpoint is computed from $a$ and $b$ before
> either is updated.
>
> The second check is free: $f(c)$ must change sign between consecutive rows
> whenever $c$ crosses the root, and the recorded bracket must always contain a
> sign change. If the printed bracket does not contain the printed root, one of
> the two is wrong.

---

### [2018 Q.2(a)]

**Question.** Develop an algorithm to calculate the root of any non-linear equation by bisection method.

*[Marks: 04]*

**Solution.**

**The idea in one sentence.** $f$ is continuous and changes sign on $[a,b]$, so
halve the interval, keep the half that still changes sign, and repeat. The
error halves every step, so the method cannot stall.

**Algorithm.**

1. Read $f(x)$, the tolerance $\varepsilon$, and a maximum iteration count $N$.
2. Accept the bracket $a$, $b$.
3. Compute $f(a)$ and $f(b)$. If $f(a)f(b) > 0$, report that the interval does
   not bracket a root and stop.
4. Set $c = \dfrac{a + b}{2}$ and compute $f(c)$.
5. If $|f(c)| < \varepsilon$, or $|b - a| < \varepsilon$, accept $c$ and stop.
6. If $f(a)f(c) < 0$, set $b = c$; otherwise set $a = c$.
7. If the iteration count exceeds $N$, report non-convergence and stop.
   Otherwise return to step 4.

**Why the iteration count is known in advance.** After $n$ halvings the
interval has width $\dfrac{b-a}{2^n}$, and $c$ is its midpoint, so the error in
$c$ is at most half the width:

$$n = \left\lceil \log_2\frac{b-a}{\varepsilon}\right\rceil$$

That closed form is the reason bisection is worth writing an algorithm for at
all. Newton is faster but you cannot predict how long it will take.

**Merits.** Guaranteed convergence whenever the initial interval brackets a
root and $f$ is continuous, and exactly one evaluation of $f$ per step.

**Demerits.** Slow compared with Newton or regula falsi, because halving throws
away half the information each time. The count is fixed by the tolerance rather
than by the shape of $f$. And you must find a bracketing interval first, which
for an even-multiplicity root can be impossible.

> [!warning] Where bisection quietly fails
> If $f$ has a root at which it touches zero without changing sign, such as
> $(x-2)^2$, then $f(a)f(b) > 0$ at the true bracket and step 3 rejects it. The
> method cannot find an even-multiplicity root at all, and no amount of
> iteration will help. This is not a bug in the algorithm; it is a property of
> sign-change bracketing.

---

### [2024 Q.2(a)]

**Question.** Given the polynomial $f(x) = x^3 - 6x^2 + 11x - 6$, use the bisection (bracketing) method to find a root in the interval up to two iterations.

*[Marks: 03, CO: 2]*

**Solution.**

**The setup.** The question gives no interval, so the first task is to find one.
Bisection needs $f$ to change sign across the interval, so scan for a sign
change before iterating.

$$f(x) = x^3 - 6x^2 + 11x - 6$$

| $x$ | $f(x)$ |
| :--: | :--: |
| 2.5 | $-0.375$ |
| 3.4 | $+1.344$ |

**The three roots are exactly $1, 2, 3$.** This is worth checking at the outset,
because it is the fastest possible verification of everything that follows:

$$x^3 - 6x^2 + 11x - 6 = (x-1)(x-2)(x-3)$$

Any bisection result must converge to one of these three values. A result that
converges elsewhere is wrong, and this is the check to apply before accepting
any number of iterations.

**Choosing the interval.** Take $[2.5, 3.4]$, which brackets $x = 3$ without
landing on it, so each iteration narrows the bracket:

$$
f(2.5) = 15.625 - 37.5 + 27.5 - 6 = -0.375, \qquad f(3.4) = 39.304 - 69.36 + 37.4 - 6 = +1.344
$$

$f(2.5) \cdot f(3.4) = -0.504 < 0$, so a root lies in $(2.5, 3.4)$.

> [!warning] Do not bisect on $[1, 2]$ or $[2, 3]$
> The three roots are $1$, $2$ and $3$, so the intervals between consecutive roots
> look attractive. They are the worst possible choice: $f(1) = f(2) = f(3) = 0$,
> so both endpoints of $[1, 2]$ are already roots and there is no sign change to
> narrow. A midpoint test on such an interval is meaningless, because no
> sub-interval of it has endpoints of opposite sign.
>
> **Pick an interval that contains one root strictly inside it.** $[2.5, 3.4]$
> does, and its endpoints are not roots, which is the second thing to check after
> the sign change.

**Iteration 1.** Midpoint $x_1 = (2.5 + 3.4)/2 = 2.95$

$$
f(2.95) = 25.6724 - 52.2150 + 32.45 - 6 = -0.092625
$$

$f(2.95) < 0$, the same sign as $f(2.5)$, so the root is in $(2.95, 3.4)$.

**Iteration 2.** Midpoint $x_2 = (2.95 + 3.4)/2 = 3.175$

$$
f(3.175) = 32.005984 - 60.483750 + 34.925 - 6 = +0.447234
$$

$f(3.175) > 0$, so the root is in $(2.95, 3.175)$.

| Iteration | $a$ | $b$ | midpoint | $f(\text{midpoint})$ | retained |
| :--: | --: | --: | --: | --: | :--: |
| 1 | 2.5 | 3.4 | 2.95 | $-0.092625$ | $(2.95, 3.4)$ |
| 2 | 2.95 | 3.4 | 3.175 | $+0.447234$ | $(2.95, 3.175)$ |

$$\boxed{x_2 = 3.175, \qquad \text{root} \in (2.95,\ 3.175), \qquad \text{true root} = 3}$$

The interval halves each time, so after $n$ iterations its width is
$\dfrac{b-a}{2^n}$, and the answer is known to lie inside it. This is the
feature that makes bisection valuable despite being slow: **the error is
bounded at every step**, whether or not the iteration has converged.

**Why bisection is chosen here.** The marks are for the method, not for the
algebra, so the polynomial's factoring is the check rather than the answer. The
question is asking for the bracketing procedure, and the demonstration of it
requires a valid bracket, which requires finding a sign change.

**Convergence rate.** Bisection is first order: halving the interval halves the
error, so gaining one decimal place costs about $3.3$ iterations. Compare
Newton–Raphson at second order, where the number of correct digits roughly
doubles per step. The trade is reliability for speed.

> [!warning] The trap: a repeated root
> If the interval is chosen so that a root sits exactly at an endpoint, the
> bisection test $f(a)f(c) < 0$ will select the wrong half on the first step,
> because one factor is zero rather than negative. The standard fix is to check
> $f(c) = 0$ separately before testing the sign, which is what a correct
> algorithm does. Without it, a root at an endpoint is lost.

---

[🏠 Subtopic Index](00_Index.md) | [← Prev: NM-2.1 Fundamentals & Classification](NM-2.1_Fundamentals_and_Classification.md) | [Next: NM-2.3 False Position / Regula Falsi →](NM-2.3_False_Position_and_Regula_Falsi.md)
