---
title: "NM-7.2 · First Derivative from Tabulated Data"
tags:
  - numerical-methods
  - discrete-mathematics
  - topicwise
---


[🏠 Subtopic Index](00_Index.md) | [← Prev: NM-7.1 Basis & Difference Formulas](NM-7.1_Basis_and_Difference_Formulas.md) | [Next: NM-7.3 Second Derivative & Formula Derivation →](NM-7.3_Second_Derivative_and_Formula_Derivation.md)

---

# NM-7.2 · First Derivative from Tabulated Data

Every block below is copied from `../answers_exam_style/`, which is the
only place an answer is authored. A number here is the same number, character
for character, as the one it came from.


### [2019 Q.6(b)]

**Question.** A 1 Henry inductance gets current through it at different times as follows. Obtain the voltage across it at $t = 0.27\text{ sec}$ using numerical differentiation.

**Solution.**

| $t$ (sec) | 0.25 | 0.26 | 0.27 | 0.28 | 0.29 |
| :---: | :---: | :---: | :---: | :---: | :---: |
| $I$ (amp) | 0.2474 | 0.2571 | 0.2667 | 0.2764 | 0.2860 |

The tabular spacing is $h = 0.01$. The target $t = 0.27$ has two points on each
side, so the five-point central formula is available and is the most accurate.

**Five-point central difference.**

$$f'(x_n) = \frac{f_{n-2} - 8f_{n-1} + 8f_{n+1} - f_{n+2}}{12h}$$

With $f_{n-2} = 0.2474$, $f_{n-1} = 0.2571$, $f_{n+1} = 0.2764$, $f_{n+2} = 0.2860$:

$$\left.\frac{dI}{dt}\right|_{t = 0.27} = \frac{0.2474 - 8(0.2571) + 8(0.2764) - 0.2860}{12(0.01)}$$

$$\frac{dI}{dt} = \frac{0.2474 - 2.0568 + 2.2112 - 0.2860}{0.12} = \frac{0.1158}{0.12} = 0.965$$

**Voltage across the inductor.** For $L = 1\ \text{H}$, $v = L\dfrac{dI}{dt}$:

$$v = 1 \times 0.965 = 0.965\ \text{V}$$

$$\boxed{v(0.27) = 0.965\ \text{V}}$$

> [!info] Check by the three-point central formula
> The three-point central formula gives $\dfrac{I_{n+1} - I_{n-1}}{2h} = \dfrac{0.2764 - 0.2571}{0.02} = \dfrac{0.0193}{0.02} = 0.965$, the
> same value to four digits. The first differences of the tabulated current are
> $0.0097, 0.0096, 0.0097, 0.0096$, averaging $0.00965$, which is the same slope
> observed over the whole span. Three agreeing estimates at two different orders
> of accuracy indicate the data are locally straight and the derivative is not
> dominated by the rounding of the fourth decimal.
>
> The one-sided formulas are less reliable here. The two-point forms, which are
> $O(h)$, give $0.970$ forward and $0.960$ backward. The three-point one-sided
> forms, which are $O(h^2)$, give $0.975$ forward and $0.955$ backward. Either pair
> straddles the true value with a spread of $\pm 0.01$, which is the truncation
> error of those formulas rather than any disagreement about the value itself.

---

### [2020 Q.6(c)]

**Question.** The following table gives the angular displacements $\theta$ (radian) at different time intervals of time $t$ (sec). Calculate the angular velocity at the instant $t = 0.06$ sec.

**Solution.**

| $t$ | 0 | 0.02 | 0.04 | 0.06 | 0.08 | 0.10 | 0.12 |
| --- | --: | --: | --: | --: | --: | --: | --: |
| $\theta$ | 0.052 | 0.105 | 0.168 | 0.242 | 0.327 | 0.408 | 0.489 |

**Step 1. Angular velocity is the derivative.** $\omega = \dfrac{d\theta}{dt}$, so
this is numerical differentiation of a table with $h = 0.02$ s.

**Step 2. $t = 0.06$ is an interior node.** Data exist on both sides, at
$0.04$ and $0.08$, so the **three-point central** formula applies and is both
the most accurate of the three-point formulas and the natural one here.

$$
\left.\frac{d\theta}{dt}\right|_{0.06} \approx \frac{\theta_{0.08} - \theta_{0.04}}{2h} = \frac{0.327 - 0.168}{2(0.02)} = \frac{0.159}{0.04} = 3.975
$$

$$
\boxed{\left.\frac{d\theta}{dt}\right|_{t=0.06} \approx 3.975 \text{ rad/s}}
$$

**Step 3. The other available formulas**, for comparison.

| Formula | Nodes needed | Value at $t = 0.06$ |
| :-- | :-- | --: |
| Three-point central | $0.04, 0.06, 0.08$ | $3.975$ |
| Five-point central | $0.02$ to $0.10$ | $4.0375$ |
| Three-point forward | $0.06, 0.08, 0.10$ | $4.350$ |
| Three-point backward | $0.02, 0.04, 0.06$ | $3.975$ |

The five-point central formula is available here, because $0.06 - 2h = 0.02$ is
in the table:

$$
\left.\frac{d\theta}{dt}\right|_{0.06} \approx \frac{\theta_{0.02} - 8\theta_{0.04} + 8\theta_{0.08} - \theta_{0.10}}{12h} = \frac{0.105 - 8(0.168) + 8(0.327) - 0.408}{0.24}
$$

$$
= \frac{0.105 - 1.344 + 2.616 - 0.408}{0.24} = \frac{0.969}{0.24} = 4.0375
$$

> [!warning] The table is not smooth, and that is why the formulas disagree
> Build the difference table:
>
> | Order | Values |
> | :-- | :-- |
> | $\theta$ | 0.052, 0.105, 0.168, 0.242, 0.327, 0.408, 0.489 |
> | $\Delta\theta$ | 0.053, 0.063, 0.074, 0.085, 0.081, 0.081 |
> | $\Delta^2\theta$ | 0.010, 0.011, 0.011, $-0.004$, 0.000 |
> | $\Delta^3\theta$ | 0.001, 0.000, $-0.015$, 0.004 |
>
> The first differences grow smoothly, $0.053, 0.063, 0.074, 0.085$, then **drop
> to $0.081$ and stay flat**. For a body starting from rest under constant angular
> acceleration the first differences should grow linearly and the second
> differences should be constant. Here the second differences run
> $0.010, 0.011, 0.011$ and then jump to $-0.004$ and $0.000$. So the last three
> samples do not belong to the same smooth motion as the first four.
>
> **This is why the three-point and five-point answers differ by $1.6\%$.** The
> five-point formula reaches out to $t = 0.02$ and $0.10$, sampling the
> discontinuity, and returns the larger value. The three-point formula uses only
> the smooth middle region.
>
> **Write the three-point central answer, $3.975$ rad/s, and mention the
> discrepancy.** Reporting a single value without noting that the data are irregular
> leaves the table unchecked. Note also the physical reading: a first difference
> of $0.085$ over $0.02$ s already gives a velocity of
> $4.25$ rad/s, so an answer near $4$ is the right order and any answer near
> $3$ warrants re-examination.

> [!note] Central, forward, or backward
> At an **interior** node with data on both sides, the central formula is the
> natural choice and the most accurate among three-point formulas. The five-point central
> formula is $O(h^4)$ against $O(h^2)$ for the three-point, and it is available
> here, so if the data had been smooth it would be the better answer.
>
> Use a one-sided formula only when the node is near an edge and no data exist on
> the other side. In 2021 Q.7(c) the five-point central formula was **not**
> available at the requested node and the three-point one was forced; here both
> are available, so the choice is about data quality rather than availability.

---

### [2021 Q.7(c)]

**Question.** From the values of $x$ and $y$ in the following table, determine $\frac{dy}{dx}$ and $\frac{d^2y}{dx^2}$ for $x = 1.2$.

**Solution.**

| $x$ | 1.0 | 1.2 | 1.4 | 1.6 | 1.8 | 2.0 | 2.2 |
| --- | --: | --: | --: | --: | --: | --: | --: |
| $y$ | 2.7183 | 3.3201 | 4.0552 | 4.9530 | 6.0496 | 7.3891 | 9.0250 |

The nodes are equally spaced with $h = 0.2$, and the values are $e^x$ rounded to
four decimals.

> [!note] The five-point formula cannot be used here
> The five-point **central** difference for $f'$ at $x$ needs points at
> $x - 2h$, $x - h$, $x$, $x + h$, $x + 2h$. At $x = 1.2$ that is
> $0.8, 1.0, 1.2, 1.4, 1.6$, and **the table has no $x = 0.8$**. The five-point
> formula is available at $x = 1.4$ onward, not at $x = 1.2$.
>
> So the three-point formula is the intended one.

**First derivative, three-point central.** Uses $x = 1.0, 1.2, 1.4$:

$$
\left.\frac{dy}{dx}\right|_{1.2} \approx \frac{y_{1.4} - y_{1.0}}{2h} = \frac{4.0552 - 2.7183}{0.4} = \frac{1.3369}{0.4} = 3.34225
$$

**First derivative, three-point forward.** Uses $x = 1.2, 1.4, 1.6$:

$$
\left.\frac{dy}{dx}\right|_{1.2} \approx \frac{-3y_{1.2} + 4y_{1.4} - y_{1.6}}{2h} = \frac{-3(3.3201) + 4(4.0552) - 4.9530}{0.4} = \frac{-9.9603 + 16.2208 - 4.9530}{0.4} = \frac{1.3075}{0.4} = 3.26875
$$

The central form is both more accurate and symmetric, and it is therefore preferred. The true
value is $e^{1.2} = 3.3201169$, giving errors of $+0.0221$ and $-0.0514$
respectively.

**Second derivative, three-point central.**

$$
\left.\frac{d^2y}{dx^2}\right|_{1.2} \approx \frac{y_{1.4} - 2y_{1.2} + y_{1.0}}{h^2} = \frac{4.0552 - 2(3.3201) + 2.7183}{0.04} = \frac{0.1333}{0.04} = 3.3325
$$

**Second derivative, three-point forward.**

$$
\left.\frac{d^2y}{dx^2}\right|_{1.2} \approx \frac{y_{1.6} - 2y_{1.4} + y_{1.2}}{h^2} = \frac{4.9530 - 2(4.0552) + 3.3201}{0.04} = \frac{0.1627}{0.04} = 4.0675
$$

The central form is again much better: error $+0.0124$ against $+0.7474$.

$$
\boxed{\frac{dy}{dx}\bigg|_{1.2} \approx 3.3423, \qquad \frac{d^2y}{dx^2}\bigg|_{1.2} \approx 3.3325}
$$

> [!info] Check
> The table is $e^x$ rounded to four decimals, so the exact answers are
> $e^{1.2} = 3.3201169$ for both the first and second derivative, since
> $\frac{d^2}{dx^2}e^x = e^x$. The central values $3.34225$ and $3.3325$ are within
> $0.7\%$ and $0.4\%$ of that, consistent with $O(h^2)$ truncation plus the
> four-decimal rounding in the data.
>
> The five-point central formula **does** work at $x = 1.4$, where $x - 2h = 1.0$ is
> present: it gives $f'(1.4) = 4.0549583$ against the exact $4.0552000$, an error
> of $2.4\times10^{-4}$. The three-point central form at the same point gives
> $4.0822500$, an error of $2.7\times10^{-2}$, so the five-point formula is about
> $110$ times better. That confirms the table is sound and only the **position**
> $x = 1.2$ prevents the better formula.

> [!warning] Three traps in this question
> **1. Reaching for five points when only three fit.** The instinct is to use the
> most accurate formula available. At $x = 1.2$ it is not available. Check that the
> required nodes exist before choosing a formula.
>
> **2. Using a one-sided formula at an interior point.** $x = 1.2$ has data on both
> sides, so the central formula applies and is both more accurate and naturally
> symmetric. A forward formula at an interior point throws away information for
> no reason, and for the second derivative it costs a factor of 60 in error here.
>
> **3. Dividing by $2h$ when the formula says $h$.** The three-point first
> derivative uses $2h$ in the denominator; the three-point second derivative uses
> $h^2$. Confusing the two is the most common slip in this question, and it gives
> answers exactly twice or $2h$ times too large.

---

### [2022 Q.3(b)]

**Question.** A cubic function $y = f(x)$ satisfies the data $x = 0, 1, 3, 4, 2$ with $f(x) = 1, 4, 40, 85, 17$. Determine the value of $f'(4)$.

**Solution.**

> [!warning] The printed question says "cubic", but the data are not a cubic
> Put the nodes in **increasing** order of $x$ first:
> $(0,1), (1,4), (2,17), (3,40), (4,85)$. Note that the paper lists the $x$
> column as $0, 1, 3, 4, 2$, out of order.
>
> The divided differences are
>
> | Order | Values | How each entry is computed |
> | :-- | :-- | :-- |
> | $y$ | 1, 4, 17, 40, 85 | given |
> | $1^{st}$ | 3, 13, 23, 45 | $(4-1)/1 = 3$, $(17-4)/1 = 13$, $(40-17)/1 = 23$, $(85-40)/1 = 45$ |
> | $2^{nd}$ | 5, 5, 11 | $(13-3)/2 = 5$, $(23-13)/2 = 5$, $(45-23)/2 = 11$ |
> | $3^{rd}$ | 0, 2 | $(5-5)/3 = 0$, $(11-5)/3 = 2$ |
> | $4^{th}$ | $\frac{1}{2}$ | $(2-0)/4 = \frac{1}{2}$ |
>
> The fourth divided difference is $\frac{1}{2}$, **not zero**, so the data lie on
> a **quartic**, not a cubic. Confirmed directly: the system with four cubic
> coefficients and five equations is inconsistent, with augmented rank 5 against
> coefficient rank 4.
>
> This does not make the question unanswerable. Five points determine exactly one
> polynomial of degree at most 4, so $f'(4)$ is still unique.

**Step 1. Newton's divided difference form.** Using the leading diagonal of the
table above, $1, 3, 5, 0, \frac{1}{2}$:

$$
f(x) = 1 + 3x + 5x(x-1) + 0\cdot x(x-1)(x-2) + \frac{1}{2}x(x-1)(x-2)(x-3)
$$

The third divided difference is zero, so that term vanishes entirely.

**Step 2. Expand.** Using
$x(x-1)(x-2)(x-3) = x^4 - 6x^3 + 11x^2 - 6x$:

$$
f(x) = 1 + 3x + 5x^2 - 5x + \frac{1}{2}\left(x^4 - 6x^3 + 11x^2 - 6x\right)
$$

$$
\boxed{f(x) = \frac{x^4}{2} - 3x^3 + \frac{21}{2}x^2 - 5x + 1}
$$

**Step 3. Verify all five points** before differentiating anything.

| $x$ | $\frac{x^4}{2}$ | $-3x^3$ | $\frac{21}{2}x^2$ | $-5x$ | $1$ | Total | Given | |
| --: | --: | --: | --: | --: | --: | --: | --: | :-- |
| 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | ✓ |
| 1 | 0.5 | $-3$ | 10.5 | $-5$ | 1 | 4 | 4 | ✓ |
| 2 | 8 | $-24$ | 42 | $-10$ | 1 | 17 | 17 | ✓ |
| 3 | 40.5 | $-81$ | 94.5 | $-15$ | 1 | 40 | 40 | ✓ |
| 4 | 128 | $-192$ | 168 | $-20$ | 1 | 85 | 85 | ✓ |

All five points are reproduced exactly.

**Step 4. Differentiate and evaluate.**

$$
f'(x) = 2x^3 - 9x^2 + 21x - 5
$$

$$
f'(4) = 2(64) - 9(16) + 21(4) - 5 = 128 - 144 + 84 - 5
$$

$$
= -16 + 84 - 5 = 68 - 5 = 63
$$

$$
\boxed{f'(4) = 63}
$$

> [!info] Check by two independent routes
> **Route 2, Lagrange form expanded.** The five-point Lagrange sum, whose
> denominators $\prod_{j \ne i}(x_i - x_j)$ for $x = 0, 1, 2, 3, 4$ are
> $24, -6, 4, -6, 24$, expands to the same polynomial
> $\frac{x^4}{2} - 3x^3 + \frac{21}{2}x^2 - 5x + 1$, and differentiating that
> gives $63$ at $x = 4$.
>
> **Route 3, central difference on the fitted polynomial.** Evaluating the
> polynomial at $x = 4.01$ and $x = 3.99$ and dividing the difference by $0.02$:
> $$f'(4) \approx \frac{f(4.01) - f(3.99)}{0.02} = \frac{126001}{2000} = 63.0005$$
> The error is $O(h^2) = O(0.0001)$, so this is consistent with $63$ and
> confirms it. Note that the secant slopes $\frac{f(4)-f(3)}{1} = 45$ and
> $\frac{f(4)-f(2)}{2} = 34$ are both far from $63$: they are averages of the
> slope over a wide interval, not the slope at $4$, and the quartic's curvature
> makes that difference large.

> [!warning] The word "cubic" and the printed row order
> Two features of the printed question decide the answer.
>
> **The word "cubic" is wrong.** Forcing a cubic through five points gives no
> solution, and quietly dropping a point changes $f'(4)$. The operative reading
> is "find the polynomial through these five points, whatever its degree", which
> is the reading followed above.
>
> **The $x$ column is out of order** in the printed table ($0, 1, 3, 4, 2$). A
> divided difference table built without sorting the nodes first gives nonsense,
> because each entry divides by the distance between *adjacent listed* nodes and
> those distances are assumed correct. Sorting the nodes precedes differencing.
>
> Note also that the zero third divided difference is not an accident. For any
> cubic in $x$, the third divided difference is constant and the fourth is zero.
> Here the fourth is $\frac{1}{2}$, which is exactly the evidence that the data
> are a quartic.

---

[🏠 Subtopic Index](00_Index.md) | [← Prev: NM-7.1 Basis & Difference Formulas](NM-7.1_Basis_and_Difference_Formulas.md) | [Next: NM-7.3 Second Derivative & Formula Derivation →](NM-7.3_Second_Derivative_and_Formula_Derivation.md)
