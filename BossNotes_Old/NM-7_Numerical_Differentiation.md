[← Previous: NM-6 Optimization](NM-6_Optimization.md) | [🏠 Index](00_Index.md) | [Next: NM-8.2 Euler's Method →](NM-8.2_Eulers_Method.md)

---

# NM-7: Numerical Differentiation — Basis, First & Second Derivatives, Applications
> **Section:** A (Numerical Methods) | **Priority:** 🟠 | **Exam Frequency:** 5/8 years | **Subtopics:** NM-7.1, NM-7.2, NM-7.3, NM-7.4
> **Sources:** Jain Ch.6 §6.1–§6.2, Shishir Notes §03 pp.36–52

## Why This Topic Matters

Numerical differentiation shows up whenever a physical quantity must be recovered from a table of measurements. Velocity from GPS logs, voltage across an inductor from a current table, angular velocity from displacement data. The topic carries two distinct question types: formula recall (state four difference equations, 2019) and tabulated-data computation (2017, 2018, 2019, 2020, 2021, 2022). The second-derivative derivation question is the one to fear most, so it gets its own section below.

---

## 📝 Key Definitions

> **Basis of numerical differentiation:** "The general method for deriving the numerical differentiation formulae is to differentiate the interpolating polynomial. Hence, corresponding to each of the formulae derived in Chapter 3, we may derive a formula for the derivative." — Jain, §6.2 (p. 207)

> **Numerical differentiation problem:** "given the set of values of $x$ and $y$, as above, we shall derive formulae to compute (i) $\frac{dy}{dx}, \frac{d^2y}{dx^2}, \dots$ for any value of $x$ in $[x_0, x_n]$" — Jain, §6.1 (p. 207)

> **Why it is unreliable:** "although the tabulated function and its approximating polynomial would agree at the set of data points, *their slopes at these points may vary considerably*. Numerical differentiation, is, therefore, an unsatisfactory process and should be used only in 'rare cases.'" — Jain, §6.2 (p. 212)

> **Order of accuracy:** $O(h)$ for two-point formulas, $O(h^2)$ for three-point formulas, $O(h^4)$ for the five-point central formula. The symbol $O(h^p)$ means the error shrinks by a factor of $2^p$ when $h$ is halved.

---

## NM-7.1 — Basis and Difference Formulas

### Theory

The basis is simple. A function known only at discrete points is replaced by a polynomial that passes through those points, and the derivative of that polynomial is used for the derivative of the function.

Everything follows from the Taylor series at a neighbouring point:

$$
f(x + h) = f(x) + hf'(x) + \frac{h^2}{2}f''(x) + \frac{h^3}{6}f'''(x) + \cdots
$$

Combinations of the series at neighbouring points cancel the terms that are not wanted. Since the first omitted term is proportional to a power of $h$, the result is an approximation with an error $O(h)$ or $O(h^2)$.

### The standard formula set

With $h$ the tabular spacing and $f_n = f(x_n)$:

| Formula | Expression | Nodes needed | Order |
| :--- | :--- | :--: | :--: |
| Two-point forward | $\displaystyle f'(x_n) = \frac{f_{n+1} - f_n}{h}$ | $n, n+1$ | $O(h)$ |
| Two-point backward | $\displaystyle f'(x_n) = \frac{f_n - f_{n-1}}{h}$ | $n-1, n$ | $O(h)$ |
| Three-point central | $\displaystyle f'(x_n) = \frac{f_{n+1} - f_{n-1}}{2h}$ | $n-1, n+1$ | $O(h^2)$ |
| Three-point forward | $\displaystyle f'(x_n) = \frac{-3f_n + 4f_{n+1} - f_{n+2}}{2h}$ | $n, n+1, n+2$ | $O(h^2)$ |
| Three-point backward | $\displaystyle f'(x_n) = \frac{3f_n - 4f_{n-1} + f_{n-2}}{2h}$ | $n-2, n-1, n$ | $O(h^2)$ |
| Five-point central | $\displaystyle f'(x_n) = \frac{f_{n-2} - 8f_{n-1} + 8f_{n+1} - f_{n+2}}{12h}$ | $n-2, \ldots, n+2$ | $O(h^4)$ |

The central formulas are preferred where data exist on both sides, since their error is $O(h^2)$ and above rather than $O(h)$, and their error constants are smaller by the same factor.

### Second-derivative formulas (function-value form, Jain §6.2.3)

| Direction | First derivative | Second derivative |
| :--- | :--- | :--- |
| Forward | $\displaystyle y'(x_i) = \frac{y_{i+1} - y_i}{h}$ | $\displaystyle y''(x_i) = \frac{y_i - 2y_{i+1} + y_{i+2}}{h^2}$ |
| Forward (3-pt) | $\displaystyle y'(x_i) = \frac{-y_{i+2} + 4y_{i+1} - 3y_i}{2h}$ | $\displaystyle y''(x_i) = \frac{-y_{i+3} + 4y_{i+2} - 5y_{i+1} + 2y_i}{h^2}$ |
| Backward | $\displaystyle y'(x_i) = \frac{y_i - y_{i-1}}{h}$ | $\displaystyle y''(x_i) = \frac{y_i - 2y_{i-1} + y_{i-2}}{h^2}$ |
| Backward (3-pt) | $\displaystyle y'(x_i) = \frac{3y_i - 4y_{i-1} + y_{i-2}}{2h}$ | $\displaystyle y''(x_i) = \frac{2y_i - 5y_{i-1} + 4y_{i-2} - y_{i-3}}{h^2}$ |
| Central | $\displaystyle y'(x_i) = \frac{y_{i+1} - y_{i-1}}{2h}$ | $\displaystyle y''(x_i) = \frac{y_{i-1} - 2y_i + y_{i+1}}{h^2}$ |
| Central (5-pt) | $\displaystyle y'(x_i) = \frac{-y_{i+2} + 8y_{i+1} - 8y_{i-1} + y_{i-2}}{12h}$ | $\displaystyle y''(x_i) = \frac{-y_{i+2} + 16y_{i+1} - 30y_i + 16y_{i-1} - y_{i-2}}{12h^2}$ |

> [!WARNING] Cancellation is the reason for the denominators
> Look at what the central first-derivative formula is doing:
> $\frac{f_{n+1} - f_{n-1}}{2h}$. Two values of order $f$ are being subtracted, and the difference is of order $hf'$. So roughly $1/h$ significant digits are lost to cancellation before the division.
>
> That is why the **five-point** formula, with its coefficients $1, -8, 8, -1$, is not automatically better. It reaches $O(h^4)$ in truncation but cancels more heavily, and against data rounded to four decimals it can be the *worse* choice.
>
> **Order of accuracy is not the whole story.** There is an optimal $h$, and past it more points make the answer worse.

### 🏆 Golden Question for NM-7.1

#### 🎯 What is the basis of numerical differentiation? Write at least four difference equations to obtain numerical differentiation.
> **Appeared:** 2019 Q.6(a) — (04 marks)

**Full Answer:**

**The basis.** A function known only at discrete points is replaced by a polynomial that passes through those points, and the derivative of that polynomial is used for the derivative of the function. Starting from the Taylor series

$$
f(x + h) = f(x) + hf'(x) + \frac{h^2}{2}f''(x) + \frac{h^3}{6}f'''(x) + \cdots
$$

combinations of the series at neighbouring points cancel the terms that are not wanted. Since the first omitted term is proportional to a power of $h$, the result is an approximation with an error $O(h)$ or $O(h^2)$.

**Four difference equations.** With $h$ the tabular spacing and $f_n = f(x_n)$:

1. **Forward difference (two-point).**

   $$
   f'(x_n) = \frac{f_{n+1} - f_n}{h}, \qquad \text{error } O(h)
   $$

2. **Backward difference (two-point).**

   $$
   f'(x_n) = \frac{f_n - f_{n-1}}{h}, \qquad \text{error } O(h)
   $$

3. **Central difference (three-point).**

   $$
   f'(x_n) = \frac{f_{n+1} - f_{n-1}}{2h}, \qquad \text{error } O(h^2)
   $$

4. **Forward difference (three-point).**

   $$
   f'(x_n) = \frac{-3f_n + 4f_{n+1} - f_{n+2}}{2h}, \qquad \text{error } O(h^2)
   $$

5. **Central difference (five-point).**

   $$
   f'(x_n) = \frac{f_{n-2} - 8f_{n-1} + 8f_{n+1} - f_{n+2}}{12h}, \qquad \text{error } O(h^4)
   $$

The central formulas are preferred where data exist on both sides, since their error is $O(h^2)$ and above rather than $O(h)$, and their error constants are smaller by the same factor.

---

## NM-7.2 — First Derivative from Tabulated Data

### Theory

Given a table of $f$ at equally spaced nodes, the derivative at a node comes straight from the difference formula. The whole difficulty is choosing the right formula.

**The decision procedure, in order:**

1. **Availability first.** Check that the nodes the formula needs actually exist in the table.
2. **Position second.** At an interior node use a central formula. At an edge use a one-sided formula.
3. **Smoothness third.** Check the difference table. If the high differences are not small, the data will not support a high-order formula.

### Worked Example (PYQ 2021): $\frac{dy}{dx}$ and $\frac{d^2y}{dx^2}$ at $x = 1.2$

> **Source:** 2021 Q.7(c) [Marks: 05]

**Question.** From the values of $x$ and $y$ in the following table, determine $\frac{dy}{dx}$ and $\frac{d^2y}{dx^2}$ for $x = 1.2$.

| $x$ | 1.0 | 1.2 | 1.4 | 1.6 | 1.8 | 2.0 | 2.2 |
| --- | --: | --: | --: | --: | --: | --: | --: |
| $y$ | 2.7183 | 3.3201 | 4.0552 | 4.9530 | 6.0496 | 7.3891 | 9.0250 |

The nodes are equally spaced with $h = 0.2$, and the values are $e^x$ rounded to four decimals.

> [!WARNING] The five-point formula cannot be used at $x = 1.2$
> The five-point **central** difference for $f'$ at $x$ needs points at $x - 2h$, $x - h$, $x$, $x + h$, $x + 2h$. At $x = 1.2$ that is $0.8, 1.0, 1.2, 1.4, 1.6$, and **the table has no $x = 0.8$**. The five-point formula is available at $x = 1.4$ onward, not at $x = 1.2$.
>
> So the three-point formula is the intended one. Always check that the nodes the formula needs actually exist before choosing it.

**First derivative, three-point central.** Uses $x = 1.0, 1.2, 1.4$:

$$
\left.\frac{dy}{dx}\right|_{1.2} \approx \frac{y_{1.4} - y_{1.0}}{2h} = \frac{4.0552 - 2.7183}{0.4} = \frac{1.3369}{0.4} = 3.34225
$$

**First derivative, three-point forward.** Uses $x = 1.2, 1.4, 1.6$:

$$
\left.\frac{dy}{dx}\right|_{1.2} \approx \frac{-3y_{1.2} + 4y_{1.4} - y_{1.6}}{2h} = \frac{-3(3.3201) + 4(4.0552) - 4.9530}{0.4} = \frac{-9.9603 + 16.2208 - 4.9530}{0.4} = \frac{1.3075}{0.4} = 3.26875
$$

The central form is both more accurate and symmetric, and it is therefore preferred. The true value is $e^{1.2} = 3.3201169$, giving errors of $+0.0221$ and $-0.0514$ respectively.

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

> [!INFO] Check
> The table is $e^x$ rounded to four decimals, so the exact answers are $e^{1.2} = 3.3201169$ for both the first and second derivative, since $\frac{d^2}{dx^2}e^x = e^x$. The central values $3.34225$ and $3.3325$ are within $0.7\%$ and $0.4\%$ of that, consistent with $O(h^2)$ truncation plus the four-decimal rounding in the data.
>
> The five-point central formula **does** work at $x = 1.4$, where $x - 2h = 1.0$ is present: it gives $f'(1.4) = 4.0549583$ against the exact $4.0552000$, an error of $2.4\times10^{-4}$. The three-point central form at the same point gives $4.0822500$, an error of $2.7\times10^{-2}$, so the five-point formula is about $110$ times better. That confirms the table is sound and only the **position** $x = 1.2$ prevents the better formula.

> [!NOTE] The cancellation that makes this question hard
> Look at the numerator of the second derivative: $4.0552 - 2(3.3201) + 2.7183 = 0.1333$. The three terms are of order 4 and their sum is of order 0.13, so three significant digits have been cancelled away before the division.
>
> This is why second derivatives from finite differences are so much less accurate than first: the cancellation is worse by a factor of $2/h$ relative to the signal. The answer $3.3325$ looks precise to five figures and is only good to about half a percent.

### 🏆 Golden Question for NM-7.2

#### 🎯 A 1 Henry inductance gets current through it at different times as follows. Obtain the voltage across it at $t = 0.27$ sec using numerical differentiation.
> **Appeared:** 2019 Q.6(b) — (05 marks)

**Full Answer:**

| $t$ (sec) | 0.25 | 0.26 | 0.27 | 0.28 | 0.29 |
| :---: | :---: | :---: | :---: | :---: | :---: |
| $I$ (amp) | 0.2474 | 0.2571 | 0.2667 | 0.2764 | 0.2860 |

The tabular spacing is $h = 0.01$. The target $t = 0.27$ has two points on each side, so the five-point central formula is available and is the most accurate.

**Five-point central difference.**

$$
f'(x_n) = \frac{f_{n-2} - 8f_{n-1} + 8f_{n+1} - f_{n+2}}{12h}
$$

With $f_{n-2} = 0.2474$, $f_{n-1} = 0.2571$, $f_{n+1} = 0.2764$, $f_{n+2} = 0.2860$:

$$
\left.\frac{dI}{dt}\right|_{t = 0.27} = \frac{0.2474 - 8(0.2571) + 8(0.2764) - 0.2860}{12(0.01)}
$$

$$
\frac{dI}{dt} = \frac{0.2474 - 2.0568 + 2.2112 - 0.2860}{0.12} = \frac{0.1158}{0.12} = 0.965
$$

**Voltage across the inductor.** For $L = 1\ \text{H}$, $v = L\dfrac{dI}{dt}$:

$$
v = 1 \times 0.965 = 0.965\ \text{V}
$$

$$
\boxed{v(0.27) = 0.965\ \text{V}}
$$

> [!INFO] Check by the three-point central formula
> The three-point central formula gives $\dfrac{I_{n+1} - I_{n-1}}{2h} = \dfrac{0.2764 - 0.2571}{0.02} = \dfrac{0.0193}{0.02} = 0.965$, the same value to four digits. The first differences of the tabulated current are $0.0097, 0.0096, 0.0097, 0.0096$, averaging $0.00965$, which is the same slope observed over the whole span.
>
> The one-sided formulas are less reliable here. The two-point forms, which are $O(h)$, give $0.970$ forward and $0.960$ backward. The three-point one-sided forms, which are $O(h^2)$, give $0.975$ forward and $0.955$ backward. Either pair straddles the true value with a spread of $\pm 0.01$, which is the truncation error of those formulas rather than any disagreement about the value itself.

> [!NOTE] When the data is nearly straight, every formula gives the same answer
> The four first differences alternate between $0.0097$ and $0.0096$ and average $0.00965$. A straight line sampled at four-decimal precision produces exactly this, and for a straight line **every** difference formula is exact, whatever its order.
>
> So the agreement of the five-point and three-point results here is not evidence that the five-point formula is more accurate. It is evidence that there is nothing for the higher-order terms to measure. **When several formulas agree, the data is the limiting factor, not the choice of formula**, and the right move is to say so rather than to claim the extra digits of accuracy.

---

#### 🎯 The following table gives the angular displacements $\theta$ (radian) at different time intervals of time $t$ (sec). Calculate the angular velocity at the instant $t = 0.06$ sec.
> **Appeared:** 2020 Q.6(c) — (04 marks)

**Full Answer:**

| $t$ | 0 | 0.02 | 0.04 | 0.06 | 0.08 | 0.10 | 0.12 |
| --- | --: | --: | --: | --: | --: | --: | --: |
| $\theta$ | 0.052 | 0.105 | 0.168 | 0.242 | 0.327 | 0.408 | 0.489 |

**Step 1. Angular velocity is the derivative.** $\omega = \dfrac{d\theta}{dt}$, so this is numerical differentiation of a table with $h = 0.02$ s.

**Step 2. $t = 0.06$ is an interior node.** Data exist on both sides, at $0.04$ and $0.08$, so the **three-point central** formula applies and is both the most accurate of the three-point formulas and the natural one here.

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

The five-point central formula is available here, because $0.06 - 2h = 0.02$ is in the table:

$$
\left.\frac{d\theta}{dt}\right|_{0.06} \approx \frac{\theta_{0.02} - 8\theta_{0.04} + 8\theta_{0.08} - \theta_{0.10}}{12h} = \frac{0.105 - 8(0.168) + 8(0.327) - 0.408}{0.24}
$$

$$
= \frac{0.105 - 1.344 + 2.616 - 0.408}{0.24} = \frac{0.969}{0.24} = 4.0375
$$

> [!WARNING] The table is not smooth, and that is why the formulas disagree
> Build the difference table:
>
> | Order | Values |
> | :-- | :-- |
> | $\theta$ | 0.052, 0.105, 0.168, 0.242, 0.327, 0.408, 0.489 |
> | $\Delta\theta$ | 0.053, 0.063, 0.074, 0.085, 0.081, 0.081 |
> | $\Delta^2\theta$ | 0.010, 0.011, 0.011, $-0.004$, 0.000 |
> | $\Delta^3\theta$ | 0.001, 0.000, $-0.015$, 0.004 |
>
> The first differences grow smoothly, $0.053, 0.063, 0.074, 0.085$, then **drop to $0.081$ and stay flat**. For a body starting from rest under constant angular acceleration the first differences should grow linearly and the second differences should be constant. Here the second differences run $0.010, 0.011, 0.011$ and then jump to $-0.004$ and $0.000$. So the last three samples do not belong to the same smooth motion as the first four.
>
> **This is why the three-point and five-point answers differ by $1.6\%$.** The five-point formula reaches out to $t = 0.02$ and $0.10$, sampling the discontinuity, and returns the larger value. The three-point formula uses only the smooth middle region.
>
> **Write the three-point central answer, $3.975$ rad/s, and mention the discrepancy.** Reporting a single value without noting that the data are irregular leaves the table unchecked. Note also the physical reading: a first difference of $0.085$ over $0.02$ s already gives a velocity of $4.25$ rad/s, so an answer near $4$ is the right order and any answer near $3$ warrants re-examination.

---

#### 🎯 A cubic function $y = f(x)$ satisfies the data $x = 0, 1, 3, 4, 2$ with $f(x) = 1, 4, 40, 85, 17$. Determine the value of $f'(4)$.
> **Appeared:** 2022 Q.3(b) — (04 marks)

**Full Answer:**

> [!WARNING] Two printed defects decide this answer, and both must be handled before anything is computed
> **The word "cubic" is wrong.** Five points do not in general lie on a cubic, and these do not. Forcing a cubic through five points gives no solution at all: the coefficient matrix has rank $4$ while the augmented matrix has rank $5$, so the system is inconsistent.
>
> **The $x$ column is out of order.** The paper prints $x = 0, 1, 3, 4, 2$. Sort the nodes first, to $(0,1), (1,4), (2,17), (3,40), (4,85)$, before differencing.

**Step 1. Newton's divided difference form**, on the sorted nodes.

| Order | Values | How each entry is computed |
| :-- | :-- | :-- |
| $y$ | 1, 4, 17, 40, 85 | given |
| $1^{st}$ | 3, 13, 23, 45 | $(4-1)/1$, $(17-4)/1$, $(40-17)/1$, $(85-40)/1$ |
| $2^{nd}$ | 5, 5, 11 | $(13-3)/2 = 5$, $(23-13)/2 = 5$, $(45-23)/2 = 11$ |
| $3^{rd}$ | 0, 2 | $(5-5)/3 = 0$, $(11-5)/3 = 2$ |
| $4^{th}$ | $\frac{1}{2}$ | $(2-0)/4 = \frac{1}{2}$ |

The fourth divided difference is $\frac{1}{2}$, **not zero**. For any cubic in $x$ the third divided difference is constant and the fourth is zero, so this table is the proof that the data lie on a **quartic**, not a cubic.

The leading diagonal is $1, 3, 5, 0, \frac{1}{2}$, giving

$$
f(x) = 1 + 3x + 5x(x-1) + 0\cdot x(x-1)(x-2) + \frac{1}{2}x(x-1)(x-2)(x-3)
$$

The third divided difference is zero, so that term vanishes entirely.

**Step 2. Expand.** Using $x(x-1)(x-2)(x-3) = x^4 - 6x^3 + 11x^2 - 6x$:

$$
f(x) = 1 + 3x + 5x^2 - 5x + \frac{1}{2}\left(x^4 - 6x^3 + 11x^2 - 6x\right)
$$

$$
\boxed{f(x) = \frac{x^4}{2} - 3x^3 + \frac{21}{2}x^2 - 5x + 1}
$$

**Step 3. Verify all five points before differentiating anything.**

| $x$ | $\frac{x^4}{2}$ | $-3x^3$ | $\frac{21}{2}x^2$ | $-5x$ | $1$ | Total | Given | |
| --: | --: | --: | --: | --: | --: | --: | --: | :-- |
| 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | ✓ |
| 1 | 0.5 | $-3$ | 10.5 | $-5$ | 1 | 4 | 4 | ✓ |
| 2 | 8 | $-24$ | 42 | $-10$ | 1 | 17 | 17 | ✓ |
| 3 | 40.5 | $-81$ | 94.5 | $-15$ | 1 | 40 | 40 | ✓ |
| 4 | 128 | $-192$ | 168 | $-20$ | 1 | 85 | 85 | ✓ |

All five are reproduced exactly, with no rounding anywhere.

**Step 4. Differentiate and evaluate.**

$$
f'(x) = 2x^3 - 9x^2 + 21x - 5
$$

$$
f'(4) = 2(64) - 9(16) + 21(4) - 5 = 128 - 144 + 84 - 5 = 68 - 5
$$

$$
\boxed{f'(4) = 63}
$$

> [!WARNING] The secant slopes are nowhere near the answer
> $\frac{f(4)-f(3)}{1} = 45$ and $\frac{f(4)-f(2)}{2} = 34$, both far from $63$. A secant slope is an average of the slope over a wide interval, not the slope at a point, and this quartic curves enough for the difference to be large.
>
> If you are asked for a derivative and find yourself writing $\frac{f(4)-f(3)}{1}$, stop. That is a finite difference and it is not what was asked.

> [!NOTE] Why the question is still answerable despite being wrong
> Five points determine exactly one polynomial of degree at most four, so $f'(4)$ is unique even though the degree label is wrong. The operative reading is "find the polynomial through these five points, whatever its degree".
>
> **The unsorted table is worth seeing, because it is what happens if you skip the sorting step.** Differencing the nodes in the printed order gives first differences $3, 18, 45, 34$, second $5, 9, 11$, third $1, 2$, fourth $\frac{1}{2}$. The fourth entry is still $\frac{1}{2}$, since divided differences are symmetric, but the third row is $1, 2$ instead of $0, 2$, so the $x(x-1)(x-2)$ term does not vanish and the polynomial you get is wrong in a way that still reproduces all five points.

---

## NM-7.3 — Second Derivative and Formula Derivation ⚠️

> [!CAUTION] This is the derivation question
> 2017 and 2018 both asked for the Newton's-forward formula for $\frac{d^2y}{dx^2}$. Memorise the derivation structure, not just the result.

### Theory: the full derivation

**Set-up.** Let $y = f(x)$ be tabulated at equally spaced nodes with interval $h$, and write $p = \dfrac{x - x_0}{h}$. Newton's forward interpolation formula is

$$
y = y_0 + p\Delta y_0 + \frac{p(p-1)}{2!}\Delta^2 y_0 + \frac{p(p-1)(p-2)}{3!}\Delta^3 y_0 + \frac{p(p-1)(p-2)(p-3)}{4!}\Delta^4 y_0 + \cdots
$$

**The chain rule is the whole method.** Since $x$ enters only through $p$,

$$
\frac{d}{dx} = \frac{1}{h}\frac{d}{dp}, \qquad \frac{d^2y}{dx^2} = \frac{1}{h^2}\frac{d^2y}{dp^2}
$$

So you differentiate the falling-factorial products with respect to $p$, not with respect to $x$. That is why every coefficient in the answer is a polynomial in $p$.

**First derivative.** Differentiating term by term:

$$
\frac{dy}{dx} = \frac{1}{h}\left[\Delta y_0 + \frac{2p-1}{2!}\Delta^2 y_0 + \frac{3p^2-6p+2}{3!}\Delta^3 y_0 + \frac{4p^3-18p^2+22p-6}{4!}\Delta^4 y_0 + \cdots\right]
$$

The coefficient of $\Delta^k y_0$ is the derivative of the product $p(p-1)\cdots(p-k+1)$ divided by $k!$. For $k = 2$ that product is $p^2 - p$, whose derivative is $2p - 1$; for $k = 3$ the product is $p^3 - 3p^2 + 2p$, whose derivative is $3p^2 - 6p + 2$.

**Second derivative.** Differentiating a second time:

$$
\frac{d^2y}{dx^2} = \frac{1}{h^2}\left[\Delta^2 y_0 + \frac{6p - 6}{3!}\Delta^3 y_0 + \frac{12p^2 - 36p + 22}{4!}\Delta^4 y_0 + \cdots\right]
$$

Each coefficient is the second derivative of the corresponding product, divided by $k!$:

$$
\frac{d^2}{dp^2}\left(p^2 - p\right) = 2, \qquad \frac{d^2}{dp^2}\left(p^3 - 3p^2 + 2p\right) = 6p - 6, \qquad \frac{d^2}{dp^2}\left(p^4 - 6p^3 + 11p^2 - 6p\right) = 12p^2 - 36p + 22
$$

and dividing by $2!$, $3!$ and $4!$ gives $1$, $(p - 1)$ and $\left(\dfrac{p^2}{2} - \dfrac{3p}{2} + \dfrac{11}{12}\right)$.

$$
\boxed{\frac{d^2y}{dx^2} = \frac{1}{h^2}\left[\Delta^2 y_0 + (p - 1)\Delta^3 y_0 + \left(\frac{p^2}{2} - \frac{3p}{2} + \frac{11}{12}\right)\Delta^4 y_0 + \cdots\right]}
$$

**At the nodes** ($p = 0$), the formula collapses to the simpler forms:

$$
\left[\frac{dy}{dx}\right]_{x=x_0} = \frac{1}{h}\left(\Delta y_0 - \frac{1}{2}\Delta^2 y_0 + \frac{1}{3}\Delta^3 y_0 - \frac{1}{4}\Delta^4 y_0 + \cdots\right)
$$

$$
\left[\frac{d^2y}{dx^2}\right]_{x=x_0} = \frac{1}{h^2}\left(\Delta^2 y_0 - \Delta^3 y_0 + \frac{11}{12}\Delta^4 y_0 + \cdots\right)
$$

**Stopping rule.** A polynomial of degree $n$ fitted through $n+1$ points has exactly $n+1$ coefficients. The differences of order greater than $n$ vanish identically, so the series terminates after the term in $\Delta^n y_0$. Since $y''$ requires differences of order two and above, **at least three points** are needed, and a cubic fit through four points carries terms up to $\Delta^3 y_0$.

**The backward counterpart.** Writing backward differences at the last node $x_n$ and putting $q = \dfrac{x - x_n}{h}$,

$$
\frac{d^2y}{dx^2} = \frac{1}{h^2}\left[\nabla^2 y_n + (q+1)\nabla^3 y_n + \left(\frac{q^2}{2} + \frac{3q}{2} + \frac{11}{12}\right)\nabla^4 y_n + \cdots\right]
$$

**Validity.** The formula reproduces $\dfrac{d^2y}{dx^2}$ exactly for any polynomial of degree four or lower, because every term from $\Delta^5 y_0$ onward then vanishes. For a table of noisy experimental data the higher differences are not zero, and they are also the noisiest entries in the difference table, so the terms beyond the data's smoothness are not worth retaining.

### 🏆 Golden Question for NM-7.3

#### 🎯 Derive a formula to find the second derivative of a tabulated function.
> **Appeared:** 2017 Q.6(c) — (04 marks)

**Full Answer:**

**Set-up.** Let $y = f(x)$ be tabulated at equally spaced nodes with interval $h$, and write $p = \dfrac{x - x_0}{h}$. Newton's forward interpolation formula is

$$
y = y_0 + p\Delta y_0 + \frac{p(p-1)}{2!}\Delta^2 y_0 + \frac{p(p-1)(p-2)}{3!}\Delta^3 y_0 + \frac{p(p-1)(p-2)(p-3)}{4!}\Delta^4 y_0 + \cdots
$$

**First derivative.** Since $dx = h\,dp$, differentiation with respect to $x$ is $(1/h)$ times differentiation with respect to $p$:

$$
\frac{dy}{dx} = \frac{1}{h}\left[\Delta y_0 + \frac{2p-1}{2!}\Delta^2 y_0 + \frac{3p^2-6p+2}{3!}\Delta^3 y_0 + \frac{4p^3-18p^2+22p-6}{4!}\Delta^4 y_0 + \cdots\right]
$$

**Second derivative.** Differentiating a second time:

$$
\boxed{\frac{d^2y}{dx^2} = \frac{1}{h^2}\left[\Delta^2 y_0 + (p-1)\Delta^3 y_0 + \left(\frac{p^2}{2} - \frac{3p}{2} + \frac{11}{12}\right)\Delta^4 y_0 + \cdots\right]}
$$

**Stopping rule.** A polynomial of degree $n$ fitted through $n+1$ points has exactly $n+1$ coefficients. The differences of order greater than $n$ vanish identically, so the series terminates after the term in $\Delta^n y_0$. Since $y''$ requires differences of order two and above, **at least three points** are needed for the formula to carry any information.

> [!INFO] A test that shows the formula is exact, not a rule of thumb
> Take $y = ax^3$ tabulated from $x_0 = 0$ at spacing $h$, so $x = ph$. Then $\Delta^2 y_0 = y(2h) - 2y(h) + y(0) = 8ah^3 - 2ah^3 = 6ah^3$ and $\Delta^3 y_0 = 6ah^3$, with all higher differences zero. The formula gives
> $$
> \frac{1}{h^2}\left[6ah^3 + (p - 1)6ah^3\right] = 6ah\left[1 + p - 1\right] = 6aph.
> $$
> The true second derivative is $y'' = 6ax = 6a(ph) = 6aph$. The two agree for *every* $p$, not only at the nodes.
>
> The reason it is exact is worth stating plainly: the differences $\Delta^{n+1} y_0, \Delta^{n+2} y_0, \dots$ of a degree-$n$ polynomial are all zero, so the truncated series is not an approximation at all but the polynomial's own derivative.

---

#### 🎯 State Newton's forward formula to evaluate $\frac{d^2 y}{dx^2}$ for any value $x \in [x_0, x_n]$.
> **Appeared:** 2018 Q.5(a) — (06 marks)

**Full Answer:**

**Newton's forward formula.** For a tabular spacing $h$, the forward difference interpolation polynomial through $n+1$ points is

$$
y = y_0 + p\Delta y_0 + \frac{p(p-1)}{2!}\Delta^2 y_0 + \frac{p(p-1)(p-2)}{3!}\Delta^3 y_0 + \frac{p(p-1)(p-2)(p-3)}{4!}\Delta^4 y_0 + \cdots
$$

with

$$
p = \frac{x - x_0}{h}
$$

**First derivative.** Differentiating term by term, $\dfrac{d}{dx} = \dfrac{1}{h}\dfrac{d}{dp}$:

$$
\frac{dy}{dx} = \frac{1}{h}\left[\Delta y_0 + \frac{2p - 1}{2!}\Delta^2 y_0 + \frac{3p^2 - 6p + 2}{3!}\Delta^3 y_0 + \frac{4p^3 - 18p^2 + 22p - 6}{4!}\Delta^4 y_0 + \cdots\right]
$$

**Second derivative.** Differentiating a second time:

$$
\frac{d^2y}{dx^2} = \frac{1}{h^2}\left[\Delta^2 y_0 + \frac{6p - 6}{3!}\Delta^3 y_0 + \frac{12p^2 - 36p + 22}{4!}\Delta^4 y_0 + \cdots\right]
$$

which simplifies to

$$
\boxed{\frac{d^2y}{dx^2} = \frac{1}{h^2}\left[\Delta^2 y_0 + (p - 1)\Delta^3 y_0 + \left(\frac{p^2}{2} - \frac{3p}{2} + \frac{11}{12}\right)\Delta^4 y_0 + \cdots\right]}
$$

**Validity.** The formula reproduces $\dfrac{d^2y}{dx^2}$ exactly for any polynomial of degree four or lower, because every term from $\Delta^5 y_0$ onward then vanishes.

**Terms retained.** A polynomial of degree $n$ through $n+1$ points has exactly $n+1$ coefficients, so for $n = 1$ only the $\Delta y_0$ term exists, for $n = 2$ the terms up to $\Delta^2 y_0$ exist, and so on. Since $y''$ requires differences of order two and above, the formula needs at least **three points** for a quadratic fit, four for a cubic. The next term, omitted above, carries the coefficient

$$
\left(\frac{p^3}{6} - p^2 + \frac{7p}{4} - \frac{5}{6}\right)\Delta^5 y_0
$$

---

## NM-7.4 — Applied Differentiation

### Theory

Real applications of numerical differentiation come down to two ideas. First, a physical quantity that no instrument measures directly is recovered from one that does. Second, an extremum of a signal is located by differentiating it.

### 🏆 Golden Question for NM-7.4

#### 🎯 Write down a real-life application of numerical differentiation.
> **Appeared:** 2021 Q.6(a) — (03 marks)

**Full Answer:**

**Velocity and acceleration from position data.**

A vehicle's position $x(t)$ is logged by GPS, or a vibrating mass's displacement is recorded by an accelerometer. Neither instrument measures velocity directly, yet both are needed for control. The derivative is obtained from the finite difference

$$
v(t) = \frac{x(t+h) - x(t-h)}{2h}
$$

Accuracy is $O(h^2)$, and halving $h$ cuts the truncation error by 4 while multiplying the round off error by 2, so the optimal $h$ sits where the two cross, usually near the cube root of the machine epsilon.

Second application: finding the **peak** of a sampled signal, such as the peak acceleration in a crash test, where the maximum of the numerical derivative locates the maximum of the original.

$$
\boxed{\text{GPS or accelerometer data gives position; the numerical derivative gives velocity and acceleration}}
$$

---

## Exam Variants

| Year | Question | Data | Key Answer |
| :--- | :--- | :--- | :--- |
| 2017 Q.6(c) | Derive formula for 2nd derivative | Theory | $\boxed{\frac{d^2y}{dx^2} = \frac{1}{h^2}\left[\Delta^2 y_0 + (p - 1)\Delta^3 y_0 + \left(\frac{p^2}{2} - \frac{3p}{2} + \frac{11}{12}\right)\Delta^4 y_0 + \cdots\right]}$ |
| 2018 Q.5(a) | State Newton's forward formula for $d^2y/dx^2$ | Theory | same boxed formula |
| 2019 Q.6(a) | Basis + 4 difference equations | Theory | 5 formulas with orders $O(h)$, $O(h^2)$, $O(h^4)$ |
| 2019 Q.6(b) | Inductor voltage at $t = 0.27$ s | $L = 1$ H, 5 points | $\boxed{v(0.27) = 0.965\ \text{V}}$ |
| 2020 Q.6(c) | Angular velocity at $t = 0.06$ s | 7 points, $h = 0.02$ | $\boxed{\left.\frac{d\theta}{dt}\right|_{t=0.06} \approx 3.975 \text{ rad/s}}$ |
| 2021 Q.6(a) | Real-life application | Theory | $\boxed{\text{GPS or accelerometer data gives position; the numerical derivative gives velocity and acceleration}}$ |
| 2021 Q.7(c) | $dy/dx$ and $d^2y/dx^2$ at $x = 1.2$ | $e^x$ table, $h = 0.2$ | $\boxed{\frac{dy}{dx}\bigg|_{1.2} \approx 3.3423, \qquad \frac{d^2y}{dx^2}\bigg|_{1.2} \approx 3.3325}$ |
| 2022 Q.3(b) | $f'(4)$ from 5 points | Out-of-order $x$ column | $\boxed{f(x) = \frac{x^4}{2} - 3x^3 + \frac{21}{2}x^2 - 5x + 1}$ and $\boxed{f'(4) = 63}$ |

---

## ⚡ Exam Tips & Common Mistakes

1. **Check that the required nodes exist before choosing a formula.** In 2021 Q.7(c) the five-point central formula needs $x = 0.8$ and the table has no such row. Availability beats order.
2. **Never use a one-sided formula at an interior node.** If data exist on both sides, the central formula applies and is more accurate. In 2021 the one-sided second derivative was off by a factor of 60.
3. **Do not confuse the denominators.** The three-point first derivative uses $2h$. The three-point second derivative uses $h^2$. Mixing them gives answers twice or $2h$ times too large.
4. **A secant slope is not a derivative.** $\frac{f(4)-f(3)}{1}$ is an average slope over an interval. In 2022 it gives 45 when the answer is 63.
5. **Sort the $x$ column before differencing.** The 2022 paper printed $x = 0, 1, 3, 4, 2$. Every divided difference entry divides by the distance between adjacent listed nodes, so sorting comes first.
6. **Check the degree claim.** In 2022 the data were called "cubic" but the fourth divided difference was $\frac{1}{2}$, not zero. Five points always give a unique polynomial of degree at most four, so the question stays answerable.
7. **Order of accuracy is not the whole story.** The five-point formula cancels more heavily. Against four-decimal data it can be worse than the three-point one.

## 🔗 Related Topics

- [NM-4.11: Difference Table Formation](NM-4.11_Difference_Table_Formation.md) — how to build the difference tables these formulas consume
- [NM-4.7: Newton's Forward Difference](NM-4.7_Newtons_Forward_Difference.md) — the interpolation formula that NM-7.3 differentiates
- [NM-8.2: Euler's Method](NM-8.2_Eulers_Method.md) — the ODE solver built from the same Taylor series idea

---

[← Previous: NM-6 Optimization](NM-6_Optimization.md) | [🏠 Index](00_Index.md) | [Next: NM-8.2 Euler's Method →](NM-8.2_Eulers_Method.md)