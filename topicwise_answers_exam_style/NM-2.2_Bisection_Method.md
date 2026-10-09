---
title: "NM-2.2 · Bisection Method"
tags:
  - numerical-methods
  - discrete-mathematics
  - topicwise
---

# NM-2.2 · Bisection Method

Every block below is copied from `../answers_exam_style/`, which is the
only place an answer is authored. A number here is the same number, character
for character, as the one it came from.


### [2017 Q.3(c)]

**Question.** Explain the bisection method for finding a real root of the equation $f(x) = 0$ and write an algorithm for its implementation with a test for relative accuracy.

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

The test is applied at every step after the first, and it measures the change
between successive midpoints rather than the distance between the current
midpoint and the true root. Because the interval halves each time, $|e_a|$ roughly
halves each time too, so it is a reliable monitor: when it falls below
$\varepsilon_r$
the remaining uncertainty is at most the current interval width, and the
computed relative error is a valid statement of how far the answer may be from
the true root.

> [!warning] The bracket must be carried, not just the midpoint
> The bracket in the table above narrows from one side only. $f$ is negative on
> $[1, 1.5214]$ and positive above it, so every midpoint above $1.5214$ sends
> $b$ down and every midpoint below sends $a$ up, and $a$ stays at $1$ until
> iteration 6. A table that moves both ends in the same iteration has made a
> sign error in the update rule, and it will still print plausible midpoints.

**Worked example.** For $f(x) = x^3 - x - 2$ on $[1, 2]$:

| Iteration | $a$ | $b$ | $c = (a+b)/2$ | $f(c)$ | $b - a$ |
| :--: | :--: | :--: | :--: | :--: | :--: |
| 1 | 1 | 2 | 1.500000 | $-0.1250$ | 1 |
| 2 | 1.5 | 2 | 1.750000 | $1.6094$ | 0.5 |
| 3 | 1.5 | 1.75 | 1.625000 | $0.6660$ | 0.25 |
| 4 | 1.5 | 1.625 | 1.562500 | $0.2522$ | 0.125 |
| 5 | 1.5 | 1.5625 | 1.531250 | $0.0591$ | 0.0625 |
| 6 | 1.5 | 1.53125 | 1.515625 | $-0.0341$ | 0.03125 |

The true root is $x = 1.5214$, and after six halvings the interval width is
$0.03125$, so the half-width $0.015625$ bounds the error and the approximate
relative error is under $1.1\%$. The method is
guaranteed to converge whenever the initial bracket is valid, and the number of
iterations needed for a given tolerance is known in advance:

$$n = \left\lceil \log_2\frac{b - a}{\varepsilon}\right\rceil$$

---

### [2018 Q.2(a)]

**Question.** Develop an algorithm to calculate the root of any non-linear equation by bisection method.

**Solution.**

**Bisection** solves $f(x) = 0$ on an interval $[a, b]$ in which $f$ changes
sign, by repeatedly halving the interval and retaining the half that still
contains the sign change.

**Algorithm.**

1. Read $f(x)$, the tolerance $\varepsilon$, and the maximum iteration count $N$.
2. Accept the ends $a$ and $b$ of the bracketing interval.
3. Compute $f(a)$ and $f(b)$. If $f(a)f(b) > 0$, report that the interval does
   not bracket a root and stop.
4. Set $c = \dfrac{a + b}{2}$ and compute $f(c)$.
5. Test for convergence. If $|f(c)| < \varepsilon$, or if
   $|b - a| < \varepsilon$, accept $c$ as the root and stop.
6. If $f(a)f(c) < 0$, set $b = c$; otherwise set $a = c$.
7. If the iteration count exceeds $N$, report non-convergence and stop.
   Otherwise return to step 4.

**Convergence.** After $n$ bisections the interval has width $\dfrac{b-a}{2^n}$,
and the error in the midpoint is at most $\dfrac{b-a}{2^{n+1}}$. Halving the
interval therefore halves the error, and the number of iterations needed for
error below $\varepsilon$ is

$$n = \left\lceil \log_2\frac{b-a}{\varepsilon}\right\rceil$$

**Merits and demerits.** The method is guaranteed to converge whenever the
initial interval brackets a root and $f$ is continuous, and the error is known
in advance. It requires only one evaluation of $f$ per step. Its drawbacks are
that convergence is slow compared with Newton or regula falsi, that the number
of iterations is fixed by the tolerance rather than by the shape of $f$, and
that a bracketing interval must be found first.

---

### [2024 Q.2(a)]

**Question.** Given the polynomial $f(x) = x^3 - 6x^2 + 11x - 6$, use the bisection (bracketing) method to find a root in the interval up to two iterations.

**Solution.**

> [!note] A gap in the printed question
> The paper does not print an initial interval $[a, b]$. Bisection needs a sign
> change, so the interval must be chosen and stated. The polynomial factors as
> $(x-1)(x-2)(x-3)$, so roots lie at $x = 1, 2, 3$.

**Choose the interval.** Take $[2.5, 3.4]$, which brackets $x = 3$ without
landing on it, so each iteration narrows the bracket.

$$
f(2.5) = 15.625 - 37.5 + 27.5 - 6 = -0.375, \qquad f(3.4) = 39.304 - 69.36 + 37.4 - 6 = +1.344
$$

$f(2.5) \cdot f(3.4) < 0$, so a root lies in $(2.5, 3.4)$.

**Iteration 1.** Midpoint $x_1 = (2.5 + 3.4)/2 = 2.95$

$$
f(2.95) = 25.6724 - 52.2150 + 32.45 - 6 = -0.092625
$$

$f(2.95) < 0$, same sign as $f(2.5)$, so the root is in $(2.95, 3.4)$.

**Iteration 2.** Midpoint $x_2 = (2.95 + 3.4)/2 = 3.175$

$$
f(3.175) = 32.005984 - 60.483750 + 34.925 - 6 = +0.447234
$$

$f(3.175) > 0$, so the root is in $(2.95, 3.175)$.

$$
\boxed{x_2 = 3.175, \qquad \text{root} \in (2.95,\ 3.175), \qquad \text{true root} = 3}
$$

**Interval after $n$ iterations.** Each iteration halves the width, so

$$
\text{width}_n = \frac{b_0 - a_0}{2^n}
$$

The initial width is $b_0 - a_0 = 3.4 - 2.5 = 0.9$. After two iterations the
bracket is $(2.95, 3.175)$, of width $0.225$, which matches
$(b_0 - a_0)/2^2 = 0.9/4 = 0.225$.

The standard maximum error bound for the midpoint after $n$ iterations is
$|x_n - r| \le \frac{b_0 - a_0}{2^n}$. For $n = 2$:

$$
|x_2 - r| \le \frac{0.9}{2^2} = 0.225
$$

Since the true root is $r = 3$, the actual error is $|3.175 - 3| = 0.175$, which
strictly satisfies the theoretical bound:

$$
\text{guaranteed: root} \in (2.95, 3.175), \quad |3.175 - 3| = 0.175 \le 0.225
$$

> [!info] Check against exact factorisation
> The polynomial factors as
> $x^3 - 6x^2 + 11x - 6 = (x-1)(x-2)(x-3)$.
> The three roots are therefore exactly $1, 2, 3$, and the bisection bracket
> $(2.95, 3.175)$ does contain $x = 3$, so the two iterations have bracketed an exact root.

> [!warning] Choosing the interval $[2.5, 3.5]$
> This interval is also valid and is the one the paper's own margin note suggests.
> Its first midpoint is exactly $3.0$, and $f(3.0) = 0$, so the root is found
> in a single step and a second iteration is then unnecessary. That is still a correct
> answer. A midpoint
> landing exactly on the root is a coincidence of this polynomial, not a general
> property.

---
