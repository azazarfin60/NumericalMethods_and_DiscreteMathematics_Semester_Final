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

Every block below is copied from `../answers_exam_style/`, which is the
only place an answer is authored. A number here is the same number, character
for character, as the one it came from.


### [2018 Q.3(b)]

**Question.** The upward velocity of a rocket is given as a function of time in table below. Determine the value of the velocity at $t = 16$ seconds using $1^{\text{st}}$ order polynomial.

**Solution.**

| $t$ (sec) | 0 | 10 | 15 | 20 | 22.5 | 30 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| $v(t)$ (m/s) | 0 | 227.04 | 362.78 | 517.35 | 602.97 | 901.67 |

A first-order polynomial is linear interpolation, so the two tabulated points
bracketing $t = 16$ are required. They are $(15, 362.78)$ and $(20, 517.35)$.

**The linear polynomial.** Through $(t_0, v_0) = (15, 362.78)$ and
$(t_1, v_1) = (20, 517.35)$:

$$v(t) = v_0 + \frac{t - t_0}{t_1 - t_0}(v_1 - v_0)$$

$$v(t) = 362.78 + \frac{t - 15}{5}(517.35 - 362.78) = 362.78 + \frac{t - 15}{5}(154.57)$$

**Evaluate at $t = 16$.**

$$v(16) = 362.78 + \frac{16 - 15}{5}(154.57) = 362.78 + \frac{154.57}{5}$$

$$v(16) = 362.78 + 30.914 = 393.694$$

$$\boxed{v(16) = 393.694\ \text{m/s}}$$

> [!info] Check against the quadratic through the same three points
> A second-degree polynomial through $(10, 227.04)$, $(15, 362.78)$ and
> $(20, 517.35)$ is
> $v(t) = 0.37660t^2 + 17.7330t + 12.050$, and it gives
> $v(16) = 96.4096 + 283.728 + 12.050 = 392.1876$. The linear value $393.694$
> and the quadratic value $392.1876$ differ by $1.5064$ m/s, about $0.38\%$,
> which is the effect of the curvature of $v$ over the interval. Since a
> first-order polynomial was asked for, the linear value is the answer; the
> comparison is recorded to show the size of the curvature term being
> discarded. The tabulated slopes confirm that $v$ is steepening steadily near
> $t = 16$: they run $22.704$, $27.148$, $30.914$, $34.248$, $39.827$ over the
> successive steps $10$, $5$, $5$, $2.5$ and $7.5$, so the curve is convex and a
> straight chord through $[15, 20]$ lies above the parabola at $t = 16$, which
> is exactly the sign of the $1.5064$ difference.

---

### [2019 Q.5(b)]

**Question.** To verify Ohm's law, an experiment was performed and the results obtained are in the following table. Use linear interpolation to determine the current for $12\text{V}$ of supply. Explain why the result differs from actual value.

**Solution.**

| $V$ (volt) | 5 | 10 | 15 | 20 | 25 |
| :---: | :---: | :---: | :---: | :---: | :---: |
| $I$ (amps) | 1 | 2.1 | 3 | 4.2 | 5 |

The target $V = 12$ lies between $V_0 = 10$ and $V_1 = 15$, so the bracketing
data are $(10, 2.1)$ and $(15, 3)$.

**Linear interpolation.** The chord through the two points is

$$I(V) = I_0 + \frac{V - V_0}{V_1 - V_0}(I_1 - I_0)$$

$$I(12) = 2.1 + \frac{12 - 10}{15 - 10}(3 - 2.1) = 2.1 + \frac{2}{5}(0.9) = 2.1 + 0.36$$

$$\boxed{I(12\ \text{V}) = 2.46\ \text{A}}$$

**Why this differs from the true value.** The actual value follows Ohm's law,
$V = IR$, with the resistance from the data. The $5\ \text{V}$ and
$15\ \text{V}$ and $25\ \text{V}$ readings give $R = V/I = 5\ \Omega$ exactly,
whereas the $10\ \text{V}$ and $20\ \text{V}$ readings give $R \approx 4.76\ \Omega$.
The true current at $12\ \text{V}$ is therefore

$$I_{\text{true}} = \frac{12}{5} = 2.4\ \text{A}$$

against the interpolated $2.46\ \text{A}$, a difference of $0.06\ \text{A}$.

The cause is the data, not the method. Linear interpolation follows the chord
joining the two bracketing points, and that chord is not the Ohm's-law line: the
$10\ \text{V}$ reading carries a measurement error of $+0.1\ \text{A}$ against the
$2.0\ \text{A}$ the law predicts, so the chord from $(10, 2.1)$ to $(15, 3)$ has
slope $0.9/5 = 0.18\ \text{A/V}$ instead of the true $0.2\ \text{A/V}$. The
interpolated value inherits that slope over the whole interval from $10$ to
$15\ \text{V}$. The effect would be less at a point nearer an accurate reading,
and it would vanish if both bracketing readings were error-free.

> [!info] Check against the exact fraction
> $2.1 + \dfrac{2}{5}(0.9) = \dfrac{21}{10} + \dfrac{18}{50} = \dfrac{105}{50} + \dfrac{18}{50} = \dfrac{123}{50} = 2.46$, terminating in
> two decimals as the interpolated result does. The measured difference of
> $0.06\ \text{A}$ is $\dfrac{3}{50}$, and $2.46 - 0.06 = 2.4 = \dfrac{12}{5}$ exactly,
> so the residual between the interpolated and true value is precisely the
> propagated effect of the $0.1\ \text{A}$ error at the $10\ \text{V}$ point.

---

[🏠 Subtopic Index](00_Index.md) | [← Prev: NM-4.4 Regression Criteria & Theory](NM-4.4_Regression_Criteria_and_Theory.md) | [Next: NM-4.6 Lagrange's Interpolation →](NM-4.6_Lagranges_Interpolation.md)
