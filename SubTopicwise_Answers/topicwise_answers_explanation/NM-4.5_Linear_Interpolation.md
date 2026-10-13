---
title: "NM-4.5 · Linear Interpolation"
tags:
  - numerical-methods
  - discrete-mathematics
  - topicwise
---


[🏠 Subtopic Index](00_Index.md) | [← Prev: NM-4.4 Regression Criteria & Theory](NM-4.4_Regression_Criteria_and_Theory.md) | [Next: NM-4.6 Lagrange's Interpolation →](NM-4.6_Lagranges_Interpolation.md)

---

# NM-4.5 · Linear Interpolation

Every block below is copied from `../answers_explanation/`. The reasoning
is written once, in the year-wise file, and is not restated here.


### [2018 Q.3(b)]

**Question.** The upward velocity of a rocket is given as a function of time in table below. Determine the value of the velocity at $t = 16$ seconds using $1^{\text{st}}$ order polynomial.

*[Marks: 06]*

**Solution.**

| $t$ (sec) | 0 | 10 | 15 | 20 | 22.5 | 30 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| $v(t)$ (m/s) | 0 | 227.04 | 362.78 | 517.35 | 602.97 | 901.67 |

**"First order polynomial" means a straight line, and this is the trap in the
question.** Read the table and notice that $t = 16$ is *not* a tabulated value,
and the intervals are irregular: $10$, $5$, $5$, $2.5$, $7.5$. That rules out
every Newton's forward and backward formula, because there is no common $h$.
So the only tool that fits both the order requested and the spacing given is
the two-point linear form.

**Find the bracketing pair.** $16$ lies between $15$ and $20$, so use
$(t_0, v_0) = (15, 362.78)$ and $(t_1, v_1) = (20, 517.35)$. Using any other
pair would be extrapolation dressed up as interpolation.

**The linear polynomial.**

$$v(t) = v_0 + \frac{t - t_0}{t_1 - t_0}(v_1 - v_0) = 362.78 + \frac{t - 15}{5}(517.35 - 362.78)$$

**Evaluate at $t = 16$.**

$$v(16) = 362.78 + \frac{16 - 15}{5}(154.57) = 362.78 + \frac{154.57}{5} = 362.78 + 30.914$$

$$\boxed{v(16) = 393.694\ \text{m/s}}$$

> [!info] What a second-degree comparison tells you
> Fit a parabola through the *same three* points $(10, 227.04)$, $(15, 362.78)$
> and $(20, 517.35)$. Solving the three normal equations gives
> $v(t) = 0.37660t^2 + 17.7330t + 12.050$, and at $t = 16$ that is
> $96.4096 + 283.728 + 12.050 = 392.1876$. The two estimates differ by
> $1.5064$ m/s, about $0.38\%$.
>
> You can read that gap without solving for the parabola at all. The second
> difference of the three tabulated values is
> $\dfrac{227.04 - 2(362.78) + 517.35}{5^2} = \dfrac{18.83}{25} = 0.7532$, so
> $v'' \approx 0.7532$ m/s³ near $t = 16$. The error of a chord on $[15, 20]$
> at an interior point $x$ is $\tfrac12 v''(x)(x - a)(x - b)$, which at $x=16$
> is $\tfrac12(0.7532)(1)(-4) = -1.5064$. The linear value sits *above* the
> parabola because $(16-15)(16-20)$ is negative, and the size of the gap is
> exactly the printed $1.5064$. Two independent routes, one solving and one
> estimating from curvature, agreeing on both size and sign.
>
> The tabulated slopes make the sign inevitable anyway: they run $22.704$,
> $27.148$, $30.914$, $34.248$, $39.827$ across the successive steps $10$, $5$,
> $5$, $2.5$, $7.5$. The curve is steepening without interruption, so it is
> convex, so a chord lies below it on the left half of the interval and above it
> on the right, and $t=16$ is in the right half.

> [!warning] Do not over-answer this
> The question specifies a first-order polynomial and the answer is the linear
> value. Reporting the quadratic value as the answer costs the marks even
> though it is a defensible number. Report the requested order, and record the
> comparison only as a check.

---

### [2019 Q.5(b)]

**Question.** To verify Ohm's law, an experiment was performed and the results obtained are in the following table. Use linear interpolation to determine the current for $12\text{V}$ of supply. Explain why the result differs from actual value.

*[Marks: 05]*

**Solution.**

| $V$ (volt) | 5 | 10 | 15 | 20 | 25 |
| :---: | :---: | :---: | :---: | :---: | :---: |
| $I$ (amps) | 1 | 2.1 | 3 | 4.2 | 5 |

The target $V = 12$ lies between $V_0 = 10$ and $V_1 = 15$, so the bracketing data
are $(10, 2.1)$ and $(15, 3)$.

**Linear interpolation.** The chord through the two points is

$$I(V) = I_0 + \frac{V - V_0}{V_1 - V_0}(I_1 - I_0)$$

$$I(12) = 2.1 + \frac{12 - 10}{15 - 10}(3 - 2.1) = 2.1 + \frac{2}{5}(0.9) = 2.1 + 0.36$$

$$\boxed{I(12\ \text{V}) = 2.46\ \text{A}}$$

**Why this differs from the true value.** The actual value follows Ohm's law,
$V = IR$, with the resistance from the data. The $5\ \text{V}$, $15\ \text{V}$ and
$25\ \text{V}$ readings give $R = V/I = 5\ \Omega$ exactly, whereas the $10\ \text{V}$
and $20\ \text{V}$ readings give $R \approx 4.76\ \Omega$. The true current at
$12\ \text{V}$ is therefore

$$I_{\text{true}} = \frac{12}{5} = 2.4\ \text{A}$$

against the interpolated $2.46\ \text{A}$, a difference of $0.06\ \text{A}$.

The cause is the data, not the method. Linear interpolation follows the chord
joining the two bracketing points, and that chord is not the Ohm's-law line: the
$10\ \text{V}$ reading carries a measurement error of $+0.1\ \text{A}$ against the
$2.0\ \text{A}$ the law predicts, so the chord from $(10, 2.1)$ to $(15, 3)$ has
slope $0.9/5 = 0.18\ \text{A/V}$ instead of the true $0.2\ \text{A/V}$. The
interpolated value inherits that slope over the whole interval from $10$ to
$15\ \text{V}$. The effect would be less at a point nearer an accurate reading, and
it would vanish if both bracketing readings were error-free.

> [!info] Check against the exact fraction
> $2.1 + \dfrac{2}{5}(0.9) = \dfrac{21}{10} + \dfrac{18}{50} = \dfrac{105}{50} + \dfrac{18}{50} = \dfrac{123}{50} = 2.46$, terminating in
> two decimals as the interpolated result does. The measured difference of
> $0.06\ \text{A}$ is $\dfrac{3}{50}$, and $2.46 - 0.06 = 2.4 = \dfrac{12}{5}$ exactly,
> so the residual between the interpolated and true value is precisely the
> propagated effect of the $0.1\ \text{A}$ error at the $10\ \text{V}$ point.

> [!warning] The answer to "explain why the result differs" is a data statement, not a method statement
> It is tempting to say that linear interpolation is only approximate and that a
> better rule would agree with Ohm's law. That is not the reason here, and it is
> worth being precise about which failure occurred.
>
> Linear interpolation between **two correct** points on a straight line through
> the origin is **exact**. The error here is entirely the $+0.1$ A in the
> $10$ V reading, and it is propagated by the slope, which is why the whole
> $10$ to $15$ V interval is affected and not just the point $12$ V.
>
> **The general lesson.** Interpolation transfers the bracketing points' errors
> into the answer, and does so through the slope. A fit that uses all the data,
> such as least squares, would have diluted this particular outlier.

---

[🏠 Subtopic Index](00_Index.md) | [← Prev: NM-4.4 Regression Criteria & Theory](NM-4.4_Regression_Criteria_and_Theory.md) | [Next: NM-4.6 Lagrange's Interpolation →](NM-4.6_Lagranges_Interpolation.md)
