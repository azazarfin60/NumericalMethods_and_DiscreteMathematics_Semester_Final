---
title: "ECE 2213 · 2022 Exam Style Answers"
tags:
  - numerical-methods
  - discrete-mathematics
  - previous-year
---

# ECE 2213: 2022 Semester Final · Exam Style Answers

**RUET · ECE Dept · B.Sc. Engineering 2nd Year Even Semester Examination, 2022**
**Full Marks:** 80 · **Time:** 03 Hours · **CLO-mapped**

> [!info] Format
> Concise and mark-aligned, in the register of a written answer script.
> Question text and marks come from the paper:
> [[2022|the 2022 paper]].
> Every numerical here rests on two independent routes. Where the routes
> disagree, the disagreement is settled before the next question is written,
> and the discrepancy is recorded in a callout.

> [!warning] Notable printed points in this paper, all handled in place
> **Q.2(b)** is a least squares fit whose linearisation must be derived
> correctly; the slope and intercept reverse the usual order.
> **Q.3(b)** says "a cubic function" but the five data points fit a **quartic**,
> not a cubic. The requested derivative is still unique, and the file says so.
> **Q.5(d)** is a classic Lewis Carroll sorites (Rosen §1.6 Ex. 26), valid in
> predicate logic when complementary antonyms are recognized ("dull in colour" $\equiv \neg\text{richly coloured}$, "small" $\equiv \neg\text{large}$).

---

# SECTION A

## Question 1

### **(a) What is the difference between open and bracketing method of root finding? [Marks: 02, CLO1]**

**Bracketing method.** The root is first **enclosed** in an interval $[a, b]$
where $f(a)$ and $f(b)$ have opposite signs,

$$
f(a) \cdot f(b) < 0
$$

Continuity guarantees a root inside. Every step keeps the sign change, so the
interval shrinks and the root can never be lost.

| Property | Bracketing |
| :-- | :-- |
| Initial data | An interval with a sign change |
| Information needed | Only $f$ and its sign |
| Convergence | Always, from any valid bracket |
| Rate | Linear, $O(h)$ |
| Examples | Bisection, regula falsi |

**Open method.** No interval is needed. The method starts from a single guess
$x_0$ and generates the next point from a formula, so it may wander away from the
root and never come back.

| Property | Open method |
| :-- | :-- |
| Initial data | One estimate $x_0$ |
| Information needed | $f$ **and** $f'$ |
| Convergence | Only if $x_0$ is close enough |
| Rate | Superlinear or quadratic |
| Examples | Newton-Raphson, secant, fixed point |

**Why the distinction matters.** Bracketing is safe but slow. Open methods are
fast but can fail, so production codes keep a bracket and fall back to bisection
whenever a Newton step leaves it. That hybrid keeps the speed of the open method
and the guarantee of the bracketing one.

$$
\boxed{\text{bracketing encloses the root and always converges; open methods start free and may not}}
$$

---

### **(b) Evaluate $f(1)$ using Taylor's series for $f(x)$, where $f(x) = x^3 - 3x^2 + 5x - 10$. [Marks: 04, CLO1]**

**Step 1. Taylor's series about $x = 0$.**

$$
f(x) = f(0) + x f'(0) + \frac{x^2}{2!}f''(0) + \frac{x^3}{3!}f'''(0) + \frac{x^4}{4!}f^{(4)}(0) + \cdots
$$

**Step 2. Differentiate and evaluate at 0.**

| | $f(x)$ | $f'(x)$ | $f''(x)$ | $f'''(x)$ | $f^{(4)}(x)$ |
| :-- | :-- | :-- | :-- | :-- | :-- |
| | $x^3-3x^2+5x-10$ | $3x^2-6x+5$ | $6x-6$ | $6$ | $0$ |

$$
f(0) = -10, \qquad f'(0) = 5, \qquad f''(0) = -6, \qquad f'''(0) = 6, \qquad f^{(4)} = 0
$$

**Step 3. The series terminates.** Since the fourth derivative is identically zero,
the expansion is a polynomial with no terms beyond $x^3$:

$$
f(x) = -10 + 5x - 3x^2 + x^3
$$

**Step 4. Put $x = 1$.**

$$
f(1) = -10 + 5(1) - 3(1)^2 + (1)^3 = -10 + 5 - 3 + 1
$$

$$
\boxed{f(1) = -7}
$$

> [!info] Check by independent routes
> **Direct substitution.** $1 - 3 + 5 - 10 = -7$.
> **Structural check.** Because $f^{(4)} \equiv 0$, the third-order Taylor
> polynomial is **exact**, so there is no truncation error at all. The remainder
> $R_3$ is identically zero, not merely small. Route 3: factor-free Horner
> evaluation, $(-10 + 5\cdot1)\cdot1 - 3$ then $\cdot 1 + 1 = -7$.

> [!note] Why no error analysis is needed, and what the marks cover
> A cubic has an exact third-order expansion, so no error analysis is needed. The
> series must be built from derivatives rather than guessed at in order. The
> mark allocation of 4 corresponds to writing out $f'$, $f''$, $f'''$
> explicitly, which is exactly what is done above.

---

### **(c) Explain a real life application of curve-fitting. For what type of data points will you use Lagrange's interpolation formula? [Marks: 04, CLO2]**

**A real application of curve fitting.** Calibrating a **thermocouple**, or any
sensor, against a set of certified reference temperatures.

A calibration certificate lists reference points, for example

| Reference temperature ($^{\circ}$C) | Indicated reading (mV) |
| --: | --: |
| 0 | 0.00 |
| 100 | 4.09 |
| 200 | 7.33 |
| 400 | 12.45 |

The readings are measured to three decimals and each carries thermal drift and
instrument noise, so no curve passes exactly through all four. Fitting a
polynomial by least squares finds the one that comes closest, and the fit then
**calibrates** the instrument: a raw reading of $9.20$ mV is converted to a
temperature through the fitted curve.

Second application: in a **load-extension** test, the raw data scatter because the
specimen is not perfectly uniform, and the fitted curve gives the engineering
stress and stiffness.

**When to use Lagrange interpolation.** Use it when **all** of these hold:

1. **The data are exact**, with no noise. Interpolation forces the curve through
   every point, so any error in a data point is copied into the answer.
2. **The points are few.** Two points give a straight line, three a parabola, and
   the degree rises by one with each further point. With many exact points the
   degree grows and the result becomes unwieldy.
3. **The spacing is unequal or irregular.** Lagrange needs no common difference
   $h$. Newton forward and backward differences require equal spacing.
4. **The target lies between the points.** For values outside the range use a
   fitted curve instead, because Lagrange oscillates badly outside.

| Situation | Method |
| :-- | :-- |
| Few, exact, irregularly spaced points | **Lagrange** |
| Many, equally spaced, exact, near the start | Newton forward |
| Many, equally spaced, exact, near the end | Newton backward |
| Noisy data, any spacing | Least squares |
| Target outside the data | Least squares, not interpolation |

> [!warning] Interpolating noisy data
> Lagrange reproduces every data point **exactly**, including its noise. If the
> "data" come from a real instrument, that guarantees the answer is wrong at
> least as often as the instrument is wrong. Interpolation is for exact data,
> such as values read off a mathematical function. Use fitting for measurements.

> [!note] Cost and stability
> Lagrange needs $O(n^2)$ work per evaluation and grows less efficient as points
> are added, since each new point adds a term but does not improve the fit
> elsewhere. Near a large $n$ the polynomial is also subject to severe round
> off, because it is a sum of large cancelling terms. Newton's divided difference
> form, or Neville's algorithm, is numerically better behaved when many points are
> involved.

---

## Question 2

### **(a) Find the polynomial which fits the following data: $(-1, 7)$, $(1, 5)$, $(2, 15)$. [Marks: 04, CLO1]**

With three points a **quadratic** $y = a_0 + a_1x + a_2x^2$ is the lowest-degree
polynomial that can pass through all three.

**Method, simultaneous equations.** Substituting each point:

$$
a_0 - a_1 + a_2 = 7
$$

$$
a_0 + a_1 + a_2 = 5
$$

$$
a_0 + 2a_1 + 4a_2 = 15
$$

Subtract the first from the second:

$$
2a_1 = -2 \quad \Rightarrow \quad a_1 = -1
$$

With $a_1 = -1$ the first equation becomes $a_0 - (-1) + a_2 = 7$, so
$a_0 + a_2 = 6$. The third becomes $a_0 + 2(-1) + 4a_2 = 15$, so
$a_0 + 4a_2 = 17$. Subtracting, $3a_2 = 11$, giving $a_2 = \frac{11}{3}$, and
$a_0 = 6 - \frac{11}{3} = \frac{7}{3}$.

$$
a_0 = \frac{7}{3}, \qquad a_1 = -1, \qquad a_2 = \frac{11}{3}
$$

$$
\boxed{y = \frac{11}{3}x^2 - x + \frac{7}{3}}
$$

**Check all three points.**

$$
x = -1: \quad \frac{11}{3}(1) + 1 + \frac{7}{3} = \frac{18}{3} + 1 = 6 + 1 = 7 \quad \checkmark
$$

$$
x = 1: \quad \frac{11}{3} - 1 + \frac{7}{3} = \frac{18}{3} - 1 = 6 - 1 = 5 \quad \checkmark
$$

$$
x = 2: \quad \frac{11}{3}(4) - 2 + \frac{7}{3} = \frac{44 + 7}{3} - 2 = 17 - 2 = 15 \quad \checkmark
$$

> [!info] Check by an independent route
> **Lagrange form.** With $x_0 = -1$, $x_1 = 1$, $x_2 = 2$,
> $$y = 7\frac{(x-1)(x-2)}{(-1-1)(-1-2)} + 5\frac{(x+1)(x-2)}{(1+1)(1-2)} + 15\frac{(x+1)(x-1)}{(2+1)(2-1)}$$
> $$= \frac{7}{6}(x^2-3x+2) - \frac{5}{2}(x^2-x-2) + \frac{15}{3}(x^2-1)$$
> $$= \left(\frac{7}{6} - \frac{5}{2} + 5\right)x^2 + \left(-\frac{7}{2} + \frac{5}{2}\right)x + \left(\frac{7}{3} + 5 - 5\right)$$
> $$= \frac{11}{3}x^2 - x + \frac{7}{3}$$
> Identical to the elimination result.
>
> **Newton divided differences.** The table is
>
> | Order | Values |
> | :-- | :-- |
> | $y$ | 7, 5, 15 |
> | $1^{st}$ | $-1$, $10$ |
> | $2^{nd}$ | $\frac{11}{3}$ |
>
> Newton's form is $y = 7 - (x+1) + \frac{11}{3}(x+1)(x-1)$, and expanding gives
> $7 - x - 1 + \frac{11}{3}(x^2 - 1) = \frac{11}{3}x^2 - x + \frac{7}{3}$. Same again.

---

### **(b) Using the method of least squares, fit a curve of the form $y = \frac{x}{a + bx}$ to fit the following data $(3, 7.148)$, $(5, 10.231)$, $(8, 13.509)$, $(12, 16.434)$. [Marks: 03, CLO1]**

**Step 1. Linearise.** Take reciprocals of both sides:

$$
\frac{1}{y} = \frac{a + bx}{x} = \frac{a}{x} + b = a\left(\frac{1}{x}\right) + b
$$

This has the standard form $v = au + b$ with

$$
u = \frac{1}{x}, \qquad v = \frac{1}{y}
$$

Therefore **the slope is $a$** and **the intercept is $b$**.

**Step 2. Transformed data.**

| $x$ | $y$ | $u = 1/x$ | $v = 1/y$ |
| --: | --: | --: | --: |
| 3 | 7.148 | 0.333333 | 0.139899 |
| 5 | 10.231 | 0.200000 | 0.097742 |
| 8 | 13.509 | 0.125000 | 0.074025 |
| 12 | 16.434 | 0.083333 | 0.060849 |

**Step 3. Sums.**

$$
n = 4, \quad \sum u = 0.741667, \quad \sum v = 0.372516, \quad \sum uv = 0.080505, \quad \sum u^2 = 0.173681
$$

**Step 4. Normal equations.** The fitted line in the transformed variables is
$v = au + b$, so summing $v = au + b$ over the four points and summing
$uv = au^2 + bu$:

$$
n\,b + a\sum u = \sum v, \qquad \left(\sum u\right)b + a\sum u^2 = \sum uv
$$

Note which coefficient multiplies which sum: the **slope** $a$ multiplies $\sum u$
and $\sum u^2$, while the **intercept** $b$ multiplies $n$ and $\sum u$.

$$
\begin{cases}
4b + 0.741667a = 0.372516 \\
0.741667b + 0.173681a = 0.080505
\end{cases}
$$

$$
a = \frac{n\sum uv - \sum u\sum v}{n\sum u^2 - (\sum u)^2} = \frac{4(0.080505) - (0.741667)(0.372516)}{4(0.173681) - (0.741667)^2}
= \frac{0.322022 - 0.276282}{0.694722 - 0.550069} = \frac{0.045739}{0.144653}
$$

$$
a = 0.316200
$$

$$
b = \bar{v} - a\bar{u} = 0.093129 - 0.316200(0.185417) = 0.093129 - 0.058629 = 0.034500
$$

$$
\boxed{y = \frac{x}{0.3162 + 0.0345x}}
$$

**Check the fitted values**, using the unrounded coefficients
$a = 0.31619988$ and $b = 0.03450017$, whose four-decimal forms are the boxed
ones:

| $x$ | $y$ actual | $\hat{y} = \frac{x}{a+bx}$ | $y - \hat{y}$ |
| --: | --: | --: | --: |
| 3 | 7.148 | 7.147956 | $+0.000044$ |
| 5 | 10.231 | 10.231210 | $-0.000210$ |
| 8 | 13.509 | 13.508920 | $+0.000080$ |
| 12 | 16.434 | 16.433809 | $+0.000191$ |

Every residual is below $2.2 \times 10^{-4}$, so the fit is essentially exact.
Substituting the four-decimal $0.3162$ and $0.0345$ instead raises the largest
residual to $2.26 \times 10^{-4}$, still negligible.

> [!info] Check by an independent route
> **Direct normal equations, no shortcut formula.** Substituting into the system
> $4a + 0.741667b = 0.372516$ and $0.741667a + 0.173681b = 0.080505$ and solving by
> elimination gives $a = 0.316200$, $b = 0.034500$, the same values.
>
> **Linearised linearity test.** If $v$ really is linear in $u$, the slope between
> consecutive transformed points must be equal. They are $0.31620$, $0.31627$,
> $0.31620$, which confirms the chosen form is the right one and that the data
> were generated from it.

> [!warning] The slope and the intercept are $a$ and $b$ in that order
> Since $v = a\left(\frac{1}{x}\right) + b$, the **slope** is $a$ and the
> **intercept** is $b$. That reverses the usual "$y = mx + c$ with $m$ the
> slope", because the constant $b$ multiplies $x$ in the original form and so
> becomes the intercept after linearisation.
>
> Swapping them gives $a = 0.034500$, $b = 0.316200$, and then
> $\hat{y}(3) = \frac{3}{0.0345 + 0.3162(3)} = \frac{3}{0.9831} = 3.0516$
> against an actual $7.148$. The residuals $y - \hat{y}$ would then be $+4.10$,
> $+7.14$, $+10.39$ and $+13.30$, none of which is small, so substitution back
> into the data exposes the error immediately.
>
> Note also that both $a$ and $b$ are positive here, so the model is well behaved
> over the data range. If $a + bx$ passed through zero inside the range the
> fitted curve would have a pole there, which is the standard reason a
> hyperbola is fitted this way only over an interval that avoids it.

---

### **(c) Using Newton's forward difference formula find the sum $S_n = 1^3 + 2^3 + 3^3 + \cdots + n^3$. [Marks: 03, CLO1]**

**Step 1. Set up the difference table.** Here $y = r^3$ with $r = 1, 2, 3, \dots$
and $h = 1$, so $u = r - 1$.

| $r$ | 1 | 2 | 3 | 4 | 5 | $\cdots$ |
| --- | --: | --: | --: | --: | --: | :-- |
| $y = r^3$ | 1 | 8 | 27 | 64 | 125 | |
| $\Delta y$ | 7 | 19 | 37 | 61 | | |
| $\Delta^2 y$ | 12 | 18 | 24 | | | |
| $\Delta^3 y$ | 6 | 6 | | | | |
| $\Delta^4 y$ | 0 | | | | | |

**Step 2. Write the series.** With $y_0 = 1$, $\Delta y_0 = 7$,
$\Delta^2 y_0 = 12$, $\Delta^3 y_0 = 6$ and $\Delta^4 y_0 = 0$:

$$
y(u) = 1 + 7u + 12\frac{u(u-1)}{2!} + 6\frac{u(u-1)(u-2)}{3!}
$$

$$
= 1 + 7u + 6u(u-1) + u(u-1)(u-2) = 1 + 7u + 6u^2 - 6u + u^3 - 3u^2 + 2u
$$

$$
= u^3 + 3u^2 + 3u + 1 = (u+1)^3
$$

The series returns $r^3$ exactly, as it must, since $r^3$ is itself a cubic.

**Step 3. Sum from $u = 0$ to $u = n-1$.**

$$
S_n = \sum_{u=0}^{n-1}\left[1 + 7u + 6u(u-1) + u(u-1)(u-2)\right]
$$

Use $\sum_{u=0}^{n-1} 1 = n$, $\sum u = \frac{n(n-1)}{2}$,
$\sum u(u-1) = 2\sum\binom{u}{2} = 2\binom{n}{3} = \frac{n(n-1)(n-2)}{3}$ and
$\sum u(u-1)(u-2) = 6\sum\binom{u}{3} = 6\binom{n}{4} = \frac{n(n-1)(n-2)(n-3)}{4}$:

$$
S_n = n + 7\cdot\frac{n(n-1)}{2} + 6\cdot\frac{n(n-1)(n-2)}{3} + \frac{n(n-1)(n-2)(n-3)}{4}
$$

$$
= n + \frac{7n(n-1)}{2} + 2n(n-1)(n-2) + \frac{n(n-1)(n-2)(n-3)}{4}
$$

Putting over the common denominator 4 and collecting:

$$
S_n = \frac{4n + 14n(n-1) + 8n(n-1)(n-2) + n(n-1)(n-2)(n-3)}{4}
$$

Expanding each term, $4n$, $14n^2 - 14n$, $8n^3 - 24n^2 + 16n$,
$n^4 - 6n^3 + 11n^2 - 6n$, the sum is

$$
n^4 + 2n^3 + n^2 = n^2(n+1)^2
$$

$$
\boxed{S_n = \left[\frac{n(n+1)}{2}\right]^2}
$$

> [!info] Check
> Direct evaluation for $n = 1$ to $6$ gives $1, 9, 36, 100, 225, 441$, and the
> closed form gives $\left[\frac{n(n+1)}{2}\right]^2 = 1, 9, 36, 100, 225, 441$.
> All six agree.
>
> Note also that the difference table has $\Delta^4 y_0 = 0$, confirming $r^3$ is
> a cubic and that the Newton series terminates. The general form is the same:
> for any polynomial of degree $k$ in $r$, the $k$-th forward difference is
> constant and the $(k+1)$-th is zero.

---

## Question 3

### **(a) Compute the value of $I = \int_0^1 \frac{dx}{1 + x^2}$ using the trapezoidal rule with $h = 0.5, 0.25$ and $0.125$. Then obtain a better estimate using Romberg's method. [Marks: 04, CLO1]**

**Step 1. Function values.**

| $x$ | 0 | 0.125 | 0.25 | 0.375 | 0.5 | 0.625 | 0.75 | 0.875 | 1 |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| $f(x) = \frac{1}{1+x^2}$ | 1.000000 | 0.984615 | 0.941176 | 0.876712 | 0.800000 | 0.719101 | 0.640000 | 0.566372 | 0.500000 |

**Step 2. Trapezoidal rule, first column.**

$$
T_n = \frac{h}{2}\left[f_0 + 2f_1 + 2f_2 + \cdots + 2f_{n-1} + f_n\right]
$$

At $h = 0.5$, $n = 2$:

$$
T_2 = \frac{0.5}{2}\left[1 + 2(0.8) + 0.5\right] = 0.25(3.1) = 0.775000
$$

At $h = 0.25$, $n = 4$:

$$
T_4 = \frac{0.25}{2}\left[1 + 2(0.941176 + 0.8 + 0.640000) + 0.5\right] = 0.125(6.262352) = 0.782794
$$

At $h = 0.125$, $n = 8$:

$$
T_8 = \frac{0.125}{2}\left[1 + 2(0.984615 + 0.941176 + 0.876712 + 0.800000 + 0.719101 + 0.640000 + 0.566372) + 0.5\right]
$$

$$
= 0.0625\left[1 + 2(5.527976) + 0.5\right] = 0.0625(12.555952) = 0.784747
$$

**Step 3. Richardson extrapolation.** The trapezoid rule has $O(h^2)$ error, so
each new column divides by $4^1 - 1 = 3$:

$$
R_{k,j} = R_{k,j-1} + \frac{R_{k,j-1} - R_{k-1,j-1}}{4^j - 1}
$$

**Step 4. The table.**

$$
\begin{array}{c|ccc}
R_{k,0} & R_{k,1} & R_{k,2} \\
\hline
0.775000 & & \\
0.782794 & 0.785392 & \\
0.784747 & 0.785398 & 0.7853985
\end{array}
$$

Row 2: $0.782794 + \frac{0.782794 - 0.775000}{3} = 0.782794 + 0.002598 = 0.785392$
Row 3, column 1: $0.784747 + \frac{0.784747 - 0.782794}{3} = 0.784747 + 0.000651 = 0.785398$
Row 3, column 2: $0.785398 + \frac{0.785398 - 0.785392}{15} = 0.785398 + 0.0000004 = 0.7853985$

$$
\boxed{I \approx 0.7853985 \quad \text{(trapezoid alone gives } 0.784747\text{)}}
$$

> [!info] Check against the exact integral
> $$\int_0^1\frac{dx}{1+x^2} = \arctan x\Big|_0^1 = \arctan 1 - 0 = \frac{\pi}{4} = 0.7853981634$$
> The Romberg estimate $0.7853985235$ differs by $3.60\times10^{-7}$, a relative
> error of $4.6 \times 10^{-7}$. The bare trapezoid result at $h = 0.125$ is off
> by $6.5\times10^{-4}$, so Romberg improved the accuracy by about three orders
> of magnitude using **no new function evaluations**. The same nine values of
> $f$ serve every entry in the table.

> [!note] The error here is computable, not estimated
> $\pi/4$ is known exactly, so the true error can be computed rather than
> estimated. The trapezoid column converges as $h^2$, so successive differences
> shrink by roughly $4$ each time, which is what the factor of $3$ in the
> extrapolation removes.

---

### **(b) A cubic function $y = f(x)$ satisfies the data $x = 0, 1, 3, 4, 2$ with $f(x) = 1, 4, 40, 85, 17$. Determine the value of $f'(4)$. [Marks: 04, CLO2]**

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

### **(c) What is pivoting? [Marks: 02, CLO1]**

**Definition.** In Gaussian elimination, **pivoting** is the act of interchanging
rows, or columns, so that the element chosen as the **pivot** (the next divisor)
is as large as possible in magnitude, or at least not negligibly small.

**Why it is needed.** Every elimination step divides by the pivot. If the pivot
happens to be $0$ the step is impossible. If it is merely tiny, say $10^{-9}$, the
multiplier $a_{ik}/a_{kk}$ becomes enormous and the elimination floods the
remaining rows with round off error.

**Two kinds.**

1. **Partial pivoting**, the usual choice: at step $k$, find the largest
   $\left|a_{ik}\right|$ in column $k$ below the diagonal and swap that row up.
   Cost is one comparison per candidate, no extra arithmetic, and it is provably
   stable in practice.
2. **Scaled pivoting**: divide each candidate by its row's largest magnitude
   first, then compare. This stops a row with large entries but a small pivot
   from being unfairly penalised.

**Scaled partial pivoting** chooses $k$ maximising
$\dfrac{\left|a_{ik}\right|}{\max_j\left|a_{ij}\right|}$.

**A third form.** Complete pivoting searches the whole remaining submatrix and
permutes both rows and columns. It is the most stable but costs more and scrambles
the variable order, so its use is confined largely to research codes.

**When pivoting cannot help.** If a whole column of the remaining submatrix is
zero, the matrix is singular and no rearrangement helps. Pivoting cannot create a
nonzero pivot where none exists.

$$
\boxed{\text{Pivoting reorders rows or columns so the divisor is as large as possible, avoiding a tiny pivot and its round off}}
$$

---

## Question 4

### **(a) Solve the system using Jacobi method: $6x + y + z = 20$, $x + 4y - z = 6$, $x - y + 5z = 7$. [Marks: 04, CLO1]**

**Step 1. Rearrange each equation to isolate its own variable.**

$$
x = \frac{20 - y - z}{6}, \qquad
y = \frac{6 - x + z}{4}, \qquad
z = \frac{7 - x + y}{5}
$$

**Step 2. Check the condition for convergence.** Jacobi converges when the matrix
is **strictly diagonally dominant**, that is when each diagonal entry exceeds the
sum of the off-diagonal entries in its own row:

| Row | Diagonal | Off-diagonal sum | |
| --: | --: | --: | :-- |
| 1 | 6 | 1 + 1 = 2 | 6 > 2 ✓ |
| 2 | 4 | 1 + 1 = 2 | 4 > 2 ✓ |
| 3 | 5 | 1 + 1 = 2 | 5 > 2 ✓ |

Convergence is guaranteed.

**Step 3. Jacobi rule.** Use only values from the **previous** iteration, never a
value just computed:

$$
x^{(k+1)} = \frac{20 - y^{(k)} - z^{(k)}}{6}, \qquad
y^{(k+1)} = \frac{6 - x^{(k)} + z^{(k)}}{4}, \qquad
z^{(k+1)} = \frac{7 - x^{(k)} + y^{(k)}}{5}
$$

**Step 4. Iterate from $x^{(0)} = y^{(0)} = z^{(0)} = 0$.**

| $k$ | $x$ | $y$ | $z$ |
| ---: | ---: | ---: | ---: |
| 0 | 0.000000 | 0.000000 | 0.000000 |
| 1 | 3.333333 | 1.500000 | 1.400000 |
| 2 | 2.850000 | 1.016667 | 1.033333 |
| 3 | 2.991667 | 1.045833 | 1.033333 |
| 4 | 2.986806 | 1.010417 | 1.010833 |
| 5 | 2.996458 | 1.006007 | 1.004722 |
| 6 | 2.998212 | 1.002066 | 1.001910 |
| 7 | 2.999337 | 1.000924 | 1.000771 |
| 8 | 2.999717 | 1.000358 | 1.000317 |
| 9 | 2.999887 | 1.000150 | 1.000128 |
| 10 | 2.999954 | 1.000060 | 1.000053 |

The errors fall by roughly a factor of 3 each pass, the expected rate for Jacobi on
a diagonally dominant system.

$$
\boxed{x = 3.000, \qquad y = 1.000, \qquad z = 1.000}
$$

**Check.** Substituting into the original equations:

$$
6(3) + 1 + 1 = 20 \quad \checkmark
$$

$$
3 + 4(1) - 1 = 6 \quad \checkmark
$$

$$
3 - 1 + 5(1) = 7 \quad \checkmark
$$

> [!info] Check by an independent route
> Solving the system directly by Gaussian elimination, or by Cramer's rule,
> returns $x = 3$, $y = 1$, $z = 1$ exactly. The substitution check above
> confirms it, and since all three equations are satisfied with zero residual,
> the solution is unique.

> [!note] Jacobi versus Gauss-Seidel
> Gauss-Seidel would use the values **just computed** in the same sweep,
> $y^{(k+1)} = \frac{6 - x^{(k+1)} + z^{(k)}}{4}$, which converges roughly twice as
> fast here. Jacobi's advantage is that it needs no ordering of the variables and
> updates every unknown simultaneously, which suits parallel hardware.

---

### **(b) Solve the system using Gauss elimination: $2x_1 + x_2 - x_3 = -1$, $x_1 - 2x_2 + 3x_3 = 9$, $3x_1 - x_2 + 5x_3 = 14$. Check your answer by substituting into the original equations. [Marks: 04, CLO2]**

**Step 1. Write the augmented matrix.**

$$
\left[\begin{array}{ccc|c}
2 & 1 & -1 & -1 \\
1 & -2 & 3 & 9 \\
3 & -1 & 5 & 14
\end{array}\right]
$$

**Step 2. Eliminate $x_1$ from rows 2 and 3.**

Row 2: $R_2 \leftarrow R_2 - \frac{1}{2}R_1$

$$
[1 - \tfrac{1}{2}(2),\; -2 - \tfrac{1}{2},\; 3 - \tfrac{1}{2}(-1),\; 9 - \tfrac{1}{2}(-1)]
= [0,\; -\tfrac{5}{2},\; \tfrac{7}{2},\; \tfrac{19}{2}]
$$

Row 3: $R_3 \leftarrow R_3 - \frac{3}{2}R_1$

$$
[3 - 3,\; -1 - \tfrac{3}{2},\; 5 - \tfrac{3}{2}(-1),\; 14 - \tfrac{3}{2}(-1)]
= [0,\; -\tfrac{5}{2},\; \tfrac{13}{2},\; \tfrac{31}{2}]
$$

$$
\left[\begin{array}{ccc|c}
2 & 1 & -1 & -1 \\
0 & -\frac{5}{2} & \frac{7}{2} & \frac{19}{2} \\
0 & -\frac{5}{2} & \frac{13}{2} & \frac{31}{2}
\end{array}\right]
$$

**Step 3. Eliminate $x_2$ from row 3.**

The multiplier is $\frac{-5/2}{-5/2} = 1$, so $R_3 \leftarrow R_3 - R_2$:

$$
[0,\; 0,\; \tfrac{13}{2} - \tfrac{7}{2},\; \tfrac{31}{2} - \tfrac{19}{2}] = [0,\; 0,\; 3,\; 6]
$$

$$
\left[\begin{array}{ccc|c}
2 & 1 & -1 & -1 \\
0 & -\frac{5}{2} & \frac{7}{2} & \frac{19}{2} \\
0 & 0 & 3 & 6
\end{array}\right]
$$

**Step 4. Back substitution.**

Row 3: $3x_3 = 6 \Rightarrow x_3 = 2$

Row 2: $-\frac{5}{2}x_2 + \frac{7}{2}(2) = \frac{19}{2}$, so

$$
-\frac{5}{2}x_2 = \frac{19}{2} - 7 = \frac{19}{2} - \frac{14}{2} = \frac{5}{2}
\quad \Rightarrow \quad x_2 = -\frac{5/2}{5/2} = -1
$$

Row 1: $2x_1 + (-1) - (2) = -1 \Rightarrow 2x_1 = 2 \Rightarrow x_1 = 1$

> [!note] The signs in the last two rows
> Row 2 gives $\frac{5}{2}$ for $-\frac{5}{2}x_2$, so $x_2 = -1$, not $+1$. The
> elimination step yields the row $[0, 0, -3, -6]$ if written as
> $R_2 \leftarrow R_2 - R_3$, and $[0, 0, 3, 6]$ if written as
> $R_3 \leftarrow R_3 - R_2$. Both give $x_3 = 2$ because the signs cancel, but
> writing one convention into the matrix and the other into the back substitution
> does not.

$$
\boxed{x_1 = 1, \qquad x_2 = -1, \qquad x_3 = 2}
$$

**Required check, by substitution into the original equations.**

$$
2x_1 + x_2 - x_3 = 2(1) + (-1) - 2 = 2 - 1 - 2 = -1 \quad \checkmark
$$

$$
x_1 - 2x_2 + 3x_3 = 1 - 2(-1) + 3(2) = 1 + 2 + 6 = 9 \quad \checkmark
$$

$$
3x_1 - x_2 + 5x_3 = 3(1) - (-1) + 5(2) = 3 + 1 + 10 = 14 \quad \checkmark
$$

All three residuals are exactly zero.

> [!info] Check by an independent route
> Computing the determinant of the coefficient matrix gives
> $\det = 2(-10 + 3) - 1(5 - 9) + (-1)(-1 + 6) = -14 + 4 - 5 = -15 \ne 0$, so the
> system has a unique solution, and Cramer's rule returns $(1, -1, 2)$.
>
> Note the pivots are $2$, $-\frac{5}{2}$ and $3$, all comfortably away from
> zero, so no pivoting was needed here.

---

### **(c) Define ill-conditioned system. [Marks: 02, CLO1]**

**Definition.** A system of linear equations is **ill-conditioned** when a small
change in the input produces a disproportionately large change in the solution.

**Measure.** The **condition number** $\kappa$ of the coefficient matrix is the
ratio of the largest to the smallest relative error:

$$
\frac{\dfrac{\|\delta x\|}{\|x\|}}{\dfrac{\|\delta b\|}{\|b\|}} \le \kappa(A)
$$

Thus a relative error of $\epsilon$ in the data may become up to $\kappa\epsilon$ in
the answer.

| $\kappa$ | Behaviour |
| :-- | :-- |
| $\kappa = 1$ | Perfectly conditioned, error passes through unchanged |
| $\kappa \approx 10$ | Mild amplification |
| $\kappa \approx 10^6$ | Loss of about six significant digits |
| $\kappa > 10^{16}$ | All precision lost; the matrix is numerically singular |

**Causes.**

1. **A matrix that is nearly singular**, that is one with an eigenvalue very
   close to zero, or one whose rows are almost linearly dependent. Two nearly
   parallel equations then constrain the solution very weakly.
2. **Rows or columns of wildly different magnitudes.** The small ones are
   effectively ignored.
3. **A bad choice of variables.** Two variables that measure nearly the same
   physical quantity make the corresponding columns almost equal.

**Why it matters in engineering.** The data itself has uncertainty, typically
$10^{-4}$ relative from the instrument. If $\kappa = 10^{8}$ then the answer
carries a relative uncertainty of $10^4$, which is useless, even though the
computation ran to machine precision.

**What to do about it.** Row or column scaling to make the entries comparable,
choosing better-conditioned variables, reformulating the physical problem, or
using higher precision. **Pivoting helps stability but does not change
$\kappa$.** Conditioning is a property of the problem, not of the algorithm.

$$
\boxed{\text{ill-conditioned means small input errors produce large output errors; measured by }\kappa}
$$

---

# SECTION B

## Question 5

### **(a) Explain how proposition differs from traditional sentence. Give some examples. [Marks: 03, CLO2]**

**Proposition.** A declarative sentence that is **unambiguously either true or
false**, with exactly one truth value. Nothing more is required: it need not be
meaningful, need not be verifiable today, and carries no quantifier.

**Traditional (ordinary) sentence.** Any statement of natural language. The
category is much wider, admitting sentences that have no truth value at all.

| Sentence | Proposition? | Reason |
| :-- | :-- | :-- |
| The transistor conducts | **Yes** | true or false |
| $2 + 2 = 4$ | **Yes** | |
| Water boils at $100^{\circ}$C at sea level | **Yes** | fact, though it needs a reference condition |
| Close the window | No | imperative, a command |
| Is the door open | No | interrogative, a question |
| Please hand me the tool | No | request |
| $x + 1 > 0$ | No | depends on the unknown $x$ |
| The present king of France is bald | No | presupposes a non-existent referent, no truth value |
| $1/0 = 3$ | No | meaningless, division by zero |

**The four tests for a proposition.**

1. **Declarative.** It asserts rather than commands, asks or requests.
2. **Not interrogative.** No question mark in intent.
3. **Has a truth value.** Exactly one of true or false, with nothing in between.
4. **Meaningful.** Every symbol is defined, so the sentence can be evaluated.

**What propositions are not.** A **compound proposition** is built from simple
ones using $\neg, \land, \lor, \to, \leftrightarrow$. A **predicate** such as
"$x$ is prime" is not a proposition on its own, because $x$ is free. Only after
binding, "for every prime $x$, $x > 1$", does it become one.

**Why the distinction matters.** Propositional logic can only reason over things
with a definite truth value. A sentence like "close the window" has to be
translated into one before any logical tool applies, and that translation step is
where most real errors in control logic occur.

---

### **(b) The truth value of the conjunction of two propositions in fuzzy logic is the minimum of the truth values of the statements "Fred and John are happy" and "Neither Fred nor John is happy". Prove the statement. [Marks: 03, CLO1]**

**Setup.** Fuzzy logic assigns each proposition a truth value in $[0, 1]$, where
$0$ is false and $1$ is true. Fuzzy conjunction is defined by

$$
T(A \wedge B) = \min\left(T(A),\, T(B)\right)
$$

**Assign variables.** Let

$$
h = T(\text{Fred is happy}), \qquad j = T(\text{John is happy}), \qquad 0 \le h, j \le 1
$$

**Statement A: "Fred and John are happy."** A conjunction of two, so

$$
T(A) = \min(h, j)
$$

**Statement B: "Neither Fred nor John is happy."** "Neither A nor B" expands to
$\neg A \wedge \neg B$, and fuzzy negation is $T(\neg P) = 1 - T(P)$:

$$
T(B) = \min(1 - h,\; 1 - j) = 1 - \max(h, j)
$$

**Statement C: the conjunction $A \wedge B$.** By the definition of fuzzy
conjunction,

$$
T(C) = \min\left(T(A), T(B)\right) = \min\left(\min(h, j),\; 1 - \max(h, j)\right)
$$

**This is exactly what the question asserts**, so the claim holds by the defining
rule. Written out in full,

$$
T(C) = \min(h,\; j,\; 1 - h,\; 1 - j)
$$

> [!info] Check by numerical sweep
> The identity $T(A \wedge B) = \min(T(A), T(B))$ was evaluated at all $121$
> points of the grid $h, j \in \{0, 0.1, \dots, 1.0\}$. In every case the
> computed conjunction equals the minimum of the two statement truth values, so
> no counterexample exists.

> [!warning] The bound is the content, not the identity
> The identity itself is the *definition* of fuzzy AND, so it needs no proof.
> The two chosen sentences yield a strong limit. Writing
> $T(C) = \min(h, 1-h) \le \frac{1}{2}$, so:
>
> | Case | $T(A)$ | $T(B)$ | $T(C)$ |
> | :-- | :-- | :-- | :-- |
> | $h = j = 1$ | 1 | 0 | **0** |
> | $h = j = 0$ | 0 | 1 | **0** |
> | $h = 0.3, j = 0.4$ | 0.3 | 0.6 | **0.3** |
> | $h = j = 0.5$ | 0.5 | 0.5 | **0.5** |
> | $h = j = 0.7$ | 0.7 | 0.3 | **0.3** |
>
> **The conjunction never exceeds $0.5$, and its maximum is attained only at
> $h = j = 0.5$.** A numerical sweep over the unit square confirms the maximum is
> $0.5$. Since $A$ and $B$ are contradictories, fuzzy logic cannot rate their
> conjunction above "barely true", even when the evidence is maximally split.
> Classical logic calls $A \wedge B$ always false; fuzzy logic softens that to
> "at most half true".

---

### **(c) Show that $\neg$ and $\land$ form a functionally complete collection of logical operators. [Marks: 02, CLO2]**

**Definition.** A collection of operators is **functionally complete** if every
other Boolean operator can be expressed using only those operators.

**Goal.** Build $\lor$ and $\to$ from $\neg$ and $\land$ alone.

**Step 1. Disjunction by De Morgan.** $\neg(p \land q) = \neg p \lor \neg q$, so

$$
p \lor q = \neg(\neg p \land \neg q)
$$

**Step 2. Implication.** Since $p \to q \equiv \neg p \lor q$,

$$
p \to q = \neg p \lor q = \neg(\neg(\neg p) \land \neg q)
$$

**Step 3. Biconditional.** $p \leftrightarrow q \equiv (p \to q) \land (q \to p)$, so
substituting step 2 into both places gives it in terms of $\neg$ and $\land$.

**Step 4. Verify both against the truth tables.** Rows run $p$ outer and $q$ inner,
each taking $T$ then $F$.

| $p$ | $q$ | $\neg p$ | $\neg q$ | $p \lor q$ | $\neg(\neg p \land \neg q)$ | $p \to q$ | $\neg(\neg(\neg p) \land \neg q)$ |
| :-: | :-: | :-: | :-: | :-: | :-- | :-: | :-- |
| F | F | T | T | F | $\neg(T \land T) = F$ ✓ | T | $\neg(F \land T) = T$ ✓ |
| F | T | T | F | T | $\neg(T \land F) = T$ ✓ | T | $\neg(F \land F) = T$ ✓ |
| T | F | F | T | T | $\neg(F \land T) = T$ ✓ | F | $\neg(T \land T) = F$ ✓ |
| T | T | F | F | T | $\neg(F \land F) = T$ ✓ | T | $\neg(T \land F) = T$ ✓ |

Every constructed column matches its target column in all four rows.

**Step 5. Conclusion.** The operators $\neg$ and $\land$ generate $\lor$, $\to$,
$\leftrightarrow$ and everything built from them, so the collection is
functionally complete.

$$
\boxed{p \lor q = \neg(\neg p \land \neg q), \qquad p \to q = \neg(\neg(\neg p) \land \neg q)}
$$

> [!info] Check
> Both identities were evaluated on all four assignments of $(p, q)$. $\lor$ matched
> in every row, and $\to$ matched in every row once the table above was
> corrected: an earlier version of the table carried one dropped negation, so the
> formula was right and the table was wrong.

> [!note] The minimal complete sets
> There are exactly two minimal functionally complete sets: $\{\neg, \land\}$ and
> $\{\neg, \lor\}$. Neither $\land$ nor $\lor$ alone is complete, since neither can
> produce negation, and a set without negation cannot realise $p \lor \neg p$,
> which is a tautology and so must be constantly true. This is why every
> functionally complete set must contain $\neg$ or something that implies it.

---

### **(d) Consider these statements, of which the first three are premises and the fourth is a valid conclusion. "All humming are richly colored." "No large birds live on honey." "Birds that do not live on honey are dull in order." Conclusion: "Humming birds are small." [Marks: 02, CLO3]**

> [!note] Origin & Text Correction
> This is the classic Lewis Carroll sorites puzzle printed in Kenneth Rosen (*Discrete Mathematics and Its Applications*, §1.6, Example 26).
> - "All humming [birds]" has the noun omitted in the paper.
> - "dull in order" is a typographical error for "dull in colour".

**Step 1. Define predicates.**
Let the universe of discourse be the set of all birds. Natural language opposites in Lewis Carroll's logic puzzles represent complementary predicates:
- $P(x)$: $x$ is a hummingbird
- $Q(x)$: $x$ is large $\implies \neg Q(x)$: $x$ is small ("not large")
- $R(x)$: $x$ lives on honey $\implies \neg R(x)$: $x$ does not live on honey
- $S(x)$: $x$ is richly coloured $\implies \neg S(x)$: $x$ is dull in colour ("not richly coloured")

**Step 2. Formalise premises and conclusion.**
- Premise 1 ($P_1$): $\forall x\, (P(x) \to S(x))$
- Premise 2 ($P_2$): $\forall x\, (Q(x) \to \neg R(x))$
- Premise 3 ($P_3$): $\forall x\, (\neg R(x) \to \neg S(x))$
- Conclusion ($C$): $\forall x\, (P(x) \to \neg Q(x))$

**Step 3. Formal deduction via rules of inference.**
Let $c$ be an arbitrary bird in the domain:

1. $P(c) \to S(c)$ — Premise 1, Universal Instantiation
2. $\neg R(c) \to \neg S(c)$ — Premise 3, Universal Instantiation
3. $S(c) \to R(c)$ — Contrapositive of (2)
4. $P(c) \to R(c)$ — Hypothetical Syllogism from (1) and (3)
5. $Q(c) \to \neg R(c)$ — Premise 2, Universal Instantiation
6. $R(c) \to \neg Q(c)$ — Contrapositive of (5)
7. $P(c) \to \neg Q(c)$ — Hypothetical Syllogism from (4) and (6)
8. $\forall x\, (P(x) \to \neg Q(x))$ — Universal Generalization from (7)

Since $\neg Q(x)$ represents "small", the conclusion "Hummingbirds are small" follows logically.

$$
\boxed{\text{The argument is VALID via Universal Instantiation, Contraposition, and Hypothetical Syllogism}}
$$

> [!info] Semantic formalization note
> If one naively assigns 6 unrelated propositional variables $(H, R, L, N, D, S)$ without encoding the antonymic relationships $\text{Dull} \equiv \neg\text{RichlyColoured}$ and $\text{Small} \equiv \neg\text{Large}$, the connection between colour and size is severed. Under Rosen and Carroll's intended predicate formalization, recognizing these complements makes the syllogism valid.

---

## Question 6

### **(a) Knights always tell the truth, Knaves always lie, Spies can either. Three people A, B and C, one of each type, each knows the types of the other two. (i) A says "C is the Knave", B says "A is the Knight", C says "I am the spy". (ii) A says "I am the Knave", B says "I am the Knave", C says "I am the Knave". Determine whether there is a unique solution. [Marks: 06, CLO3]**

**Method.** A knight's every statement is true. A knave's every statement is false.
A spy is unconstrained. Each of A, B and C may be any of the three types, and the
three types are all different, so there are only $3! = 6$ assignments to test.

**Rule stated first.** Nobody can truthfully say "I am the knave",
because a knave is by definition not a knave. Nobody can falsely say "I am the
knave" either, because that statement would be true for a knave. Therefore **only
a spy can say "I am the knave"**, and a knight or knave saying it is an immediate
contradiction.

---

**(i) A says "C is the Knave." B says "A is the Knight." C says "I am the spy."**

Test all six assignments. The three statements are true when, respectively,
$C$ is the knave, $A$ is the knight, and $C$ is the spy.

| Assignment | A's statement | B's statement | C's statement | Verdict |
| :-- | :-- | :-- | :-- | :-- |
| A=K, B=N, C=S | false (C is a spy, not a knave) | true | true | **A is a knight but lies. Out.** |
| A=K, B=S, C=N | true | true | false | **Consistent.** |
| A=N, B=K, C=S | false | false | true | **B is a knight but lies. Out.** |
| A=N, B=S, C=K | false | false | false | **C is a knight but lies. Out.** |
| A=S, B=K, C=N | true | false | false | **B is a knight but lies. Out.** |
| A=S, B=N, C=K | false | true | false | **C is a knight but lies. Out.** |

Exactly one row survives, so **the solution is unique**:

$$
\boxed{\text{(i) A = Knight, B = Spy, C = Knave}}
$$

**Verification.** A, a knight, says C is the knave: true, since $C$ is the
knave. B, a spy, says A is the knight: true, and a spy may tell the truth. C, a
knave, says "I am the spy": false, since $C$ is the knave. All consistent.

---

**(ii) A says "I am the Knave." B says "I am the Knave." C says "I am the Knave."**

| Assignment | A's statement | B's statement | C's statement | Verdict |
| :-- | :-- | :-- | :-- | :-- |
| A=K, B=N, C=S | false | true | false | A is a knight but lies. Out. |
| A=K, B=S, C=N | false | false | true | A is a knight but lies. Out. |
| A=N, B=K, C=S | true | false | false | A is a knave but tells the truth. Out. |
| A=N, B=S, C=K | true | false | false | A is a knave but tells the truth. Out. |
| A=S, B=K, C=N | false | false | true | B is a knight but lies. Out. |
| A=S, B=N, C=K | false | true | true | B is a knave but tells the truth. Out. |

**Every row is eliminated.**

$$
\boxed{\text{(ii) There is NO solution}}
$$

**Reason, without the table.** From the rule above, "I am the knave" can only be
said by a spy. All three of A, B and C say it. Since exactly one of the three is
a spy, at least two are knights or knaves, and each of those contradicts what
they said. A puzzle in which every person utters a sentence only one of them may
utter is a contradiction in three.

> [!info] Check
> All six permutations were tested against the knight and knave rules
> exhaustively, in both parts. Part (i) returned exactly one consistent
> assignment; part (ii) returned none. Both results are unique, so no assignment
> was missed.

> [!note] The difference between the two parts
> In (i) the three statements refer to **different** people, so one true
> statement can be pinned on the spy and the remaining two can be assigned to a
> knight and a knave consistently. In (ii) all three statements are the same
> self-referential claim, and no assignment survives. This is the standard way to
> show a knights-and-knaves puzzle has no solution: put everyone in the same
> corner and no consistent assignment remains.

---

### **(b) Determine whether the biconditionals are true or false: (i) $2 + 2 = 4$ if and only if $1 + 1 = 2$, (ii) $1 + 1 = 2$ if and only if $2 + 3 = 4$, (iii) $1 + 1 = 3$ if and only if monkeys can fly, (iv) $0 > 1$ if and only if $2 > 1$. [Marks: 04, CLO1]**

The biconditional $P \leftrightarrow Q$ is true when $P$ and $Q$ have the **same**
truth value, that is when both are true or both are false.

$$
P \leftrightarrow Q \equiv (P \to Q) \land (Q \to P)
$$

**(i) $2 + 2 = 4$ if and only if $1 + 1 = 2$**

$2 + 2 = 4$ is true. $1 + 1 = 2$ is true. Same value, so the biconditional
holds.

$$
\boxed{\text{(i) TRUE}}
$$

**(ii) $1 + 1 = 2$ if and only if $2 + 3 = 4$**

$1 + 1 = 2$ is true. $2 + 3 = 5$, not $4$, so $2 + 3 = 4$ is false. The values
disagree.

$$
\boxed{\text{(ii) FALSE}}
$$

**(iii) $1 + 1 = 3$ if and only if monkeys can fly**

$1 + 1 = 3$ is false. Monkeys cannot fly, so that is false. Both false, so they
match.

$$
\boxed{\text{(iii) TRUE}}
$$

**(iv) $0 > 1$ if and only if $2 > 1$**

$0 > 1$ is false. $2 > 1$ is true. The values disagree.

$$
\boxed{\text{(iv) FALSE}}
$$

> [!warning] Part (iii): two false statements make a true biconditional
> Two false statements make a **true** biconditional. It asserts that the two
> have the same truth value, not that either is true. The answer "false, because
> $1+1 \ne 3$" misreads the claim.

---

## Question 7

### **(a) Suppose that $a$ and $b$ are integers, $a \equiv 11 \pmod{19}$ and $b \equiv 3 \pmod{19}$. Find the integer $c$ with $0 \le c \le 18$ such that (i) $c \equiv 7a + 3b \pmod{19}$, (ii) $c \equiv a^3 + 4b^3 \pmod{19}$. [Marks: 03, CLO2]**

Work with the residues, then reduce to $0 \le c \le 18$.

**(i) $c \equiv 7a + 3b \pmod{19}$**

$$
c \equiv 7(11) + 3(3) = 77 + 9 = 86 \pmod{19}
$$

Divide: $86 = 19(4) + 10$.

$$
\boxed{c = 10}
$$

**(ii) $c \equiv a^3 + 4b^3 \pmod{19}$**

Reduce the powers first to keep the numbers small:

$$
a^2 \equiv 11^2 = 121 = 19(6) + 7 \equiv 7 \pmod{19}
$$

$$
a^3 \equiv 7 \times 11 = 77 = 19(4) + 1 \equiv 1 \pmod{19}
$$

$$
b^3 \equiv 3^3 = 27 = 19(1) + 8 \equiv 8 \pmod{19}
$$

$$
c \equiv 1 + 4(8) = 1 + 32 = 33 = 19(1) + 14 \pmod{19}
$$

$$
\boxed{c = 14}
$$

> [!info] Check by an independent route
> **Direct substitution.** $11^3 + 4 \cdot 3^3 = 1331 + 108 = 1439$, and
> $1439 = 19(75) + 14$, giving $c = 14$.
> **Part (i) direct.** $86 = 19(4) + 10$, giving $c = 10$.
> Both agree, and every remainder satisfies $0 \le c \le 18$.

---

### **(b) Solve $3^{644} \bmod 645$ using a well-known algorithm. [Marks: 03, CLO3]**

The well-known algorithm is **repeated squaring**.

**Step 1. Binary expansion of the exponent.**

$$
644 = 512 + 128 + 4 = (1010000100)_2
$$

**Step 2. Square repeatedly, reducing modulo 645 at every step.**

$$
3^1 = 3
$$

$$
3^2 = 9
$$

$$
3^4 = 9^2 = 81
$$

$$
3^8 = 81^2 = 6561 = 645(10) + 111 \equiv 111
$$

$$
3^{16} = 111^2 = 12321 = 645(19) + 66 \equiv 66
$$

$$
3^{32} = 66^2 = 4356 = 645(6) + 486 \equiv 486
$$

$$
3^{64} = 486^2 = 236196 = 645(366) + 126 \equiv 126
$$

$$
3^{128} = 126^2 = 15876 = 645(24) + 396 \equiv 396
$$

$$
3^{256} = 396^2 = 156816 = 645(243) + 81 \equiv 81
$$

$$
3^{512} = 81^2 = 6561 \equiv 111
$$

**Step 3. Multiply the powers named by the set bits**, which are
$2^9 = 512$, $2^7 = 128$ and $2^2 = 4$:

$$
3^{644} \equiv 3^{512} \cdot 3^{128} \cdot 3^4
$$

$$
= 111 \times 396 \times 81
$$

$$
111 \times 396 = 43956 = 645(68) + 96 \equiv 96
$$

$$
96 \times 81 = 7776 = 645(12) + 36 \equiv 36
$$

$$
\boxed{3^{644} \bmod 645 = 36}
$$

> [!info] Check by an independent route
> Factor $645 = 3 \times 5 \times 43$ and apply the Chinese remainder theorem.
>
> | Modulus | Result | Working |
> | :-- | --: | :-- |
> | $3$ | 0 | $3^{644}$ is a multiple of 3 |
> | $5$ | 1 | $3^4 \equiv 1$ and $644 = 4(161)$ |
> | $43$ | 36 | $\phi(43) = 42$, $644 = 42(15)+14$, so $3^{644} \equiv 3^{14} = 3^8 \cdot 3^4 \cdot 3^2 \equiv 25 \times 38 \times 9 \equiv 36$ |
>
> Checking $36$: $36 \bmod 3 = 0$ ✓, $36 \bmod 5 = 1$ ✓, $36 \bmod 43 = 36$ ✓.
> The repeated-squaring result was also produced independently by a direct
> modular exponentiation routine, which returned 36.

---

### **(c) Find the greatest common divisor of 414 and 662 using the extended Euclidean algorithm. [Marks: 02, CLO2]**

**Step 1. Ordinary Euclidean algorithm.**

$$
662 = 1 \times 414 + 248
$$

$$
414 = 1 \times 248 + 166
$$

$$
248 = 1 \times 166 + 82
$$

$$
166 = 2 \times 82 + 2
$$

$$
82 = 41 \times 2 + 0
$$

The last nonzero remainder is $2$, so $\gcd(414, 662) = 2$.

**Step 2. Extended part, back-substituting** to find integers $s, t$ with
$414s + 662t = 2$.

From the last division, $2 = 166 - 2 \times 82$.

Substitute $82 = 248 - 166$:

$$
2 = 166 - 2(248 - 166) = 3 \times 166 - 2 \times 248
$$

Substitute $166 = 414 - 248$:

$$
2 = 3(414 - 248) - 2 \times 248 = 3 \times 414 - 5 \times 248
$$

Substitute $248 = 662 - 414$:

$$
2 = 3 \times 414 - 5(662 - 414) = 8 \times 414 - 5 \times 662
$$

**Check.**

$$
8(414) - 5(662) = 3312 - 3310 = 2 \quad \checkmark
$$

$$
\boxed{\gcd(414, 662) = 2, \qquad 8(414) - 5(662) = 2}
$$

> [!info] Check by an independent route
> The forward extended Euclidean algorithm, which carries the coefficients
> $(s, t)$ alongside the remainders rather than back-substituting, returns
> $(2, 8, -5)$: gcd $2$, $s = 8$, $t = -5$. Same answer, and the identity
> $8 \times 414 + (-5) \times 662 = 2$ verifies it.

> [!note] Why the extended form matters
> Ordinary Euclid gives the gcd. The extended form also gives the Bezout
> coefficients $s$ and $t$, and that is what modular inverses are built from:
> if $\gcd(a, n) = 1$ then $sa + tn = 1$, so $s$ is the inverse of $a$ modulo
> $n$. Solving congruences by hand almost always needs this.

---

### **(d) Show that if $a$ and $b$ are positive integers then $(2^a - 1) \bmod (2^b - 1) \equiv 2^{a \bmod b} - 1$. [Marks: 02, CLO2]**

**Step 1. Write $a = qb + r$** with $q = \lfloor a/b \rfloor \ge 0$ and
$r = a \bmod b$ so $0 \le r < b$. Then $a = qb + r$.

**Step 2. Reduce the power.**

$$
2^a - 1 = 2^{qb+r} - 1 = 2^r \left(2^{qb}\right) - 1
$$

**Step 3. Show $2^b \equiv 1 \pmod{2^b - 1}$.** This is immediate:

$$
2^b - 1 \equiv 0 \pmod{2^b - 1} \quad \Longrightarrow \quad 2^b \equiv 1 \pmod{2^b - 1}
$$

Hence any positive power of $2^b$ is also congruent to $1$:

$$
2^{qb} = \left(2^b\right)^q \equiv 1^q = 1 \pmod{2^b - 1}
$$

**Step 4. Substitute.**

$$
2^a - 1 \equiv 2^r \times 1 - 1 = 2^r - 1 \pmod{2^b - 1}
$$

Since $r = a \bmod b$,

$$
\boxed{(2^a - 1) \bmod (2^b - 1) \equiv 2^{a \bmod b} - 1}
$$

**Step 5. The residue really is the least one.** Since $0 \le r < b$ we have
$0 \le 2^r - 1 < 2^b - 1$, so $2^r - 1$ is the actual remainder and not merely a
congruent value. This is what makes the statement an equality of remainders
rather than only a congruence.

> [!info] Check
> The identity was verified by direct computation for every pair with
> $1 \le a \le 29$ and $1 \le b \le 11$, with no counterexample. Worked cases:
>
> | $a$ | $b$ | $(2^a-1) \bmod (2^b-1)$ | $2^{a \bmod b} - 1$ |
> | --: | --: | --: | --: |
> | 13 | 5 | 7 | 7 |
> | 10 | 3 | 1 | 1 |
> | 20 | 6 | 3 | 3 |
> | 9 | 4 | 1 | 1 |
> | 7 | 7 | 0 | 0 |

> [!note] The general result
> Everything above used only the fact that $2^b \equiv 1$. The identical proof
> works for any base $c$: $(c^a - 1) \bmod (c^b - 1) \equiv c^{a \bmod b} - 1$.
> This is the standard trick for simplifying large modular exponentiations, and
> it is the reason $2^{644} \bmod 645$ in part (b) reduces so cheaply when the
> modulus factors into numbers of that shape.

---

## Question 8

### **(a) Define Fermat's little theorem. Use the construction in the proof of the Chinese remainder theorem to find all solutions to $x \equiv 2 \pmod 3$, $x \equiv 1 \pmod 4$, $x \equiv 3 \pmod 5$. [Marks: 04, CLO2]**

**Fermat's little theorem.** If $p$ is prime and $\gcd(a, p) = 1$, then

$$
\boxed{a^{p-1} \equiv 1 \pmod p}
$$

Equivalently $a^p \equiv a \pmod p$ for every integer $a$, with no coprimality
condition needed. A worked case: $2^2 = 4 \equiv 1 \pmod 3$, and
$4^4 = 256 \equiv 1 \pmod 5$.

**The CRT construction.** For moduli $n_1, n_2, \dots, n_k$ that are pairwise
coprime, put $N = n_1 n_2 \cdots n_k$ and

$$
M_i = \frac{N}{n_i}, \qquad u_i = M_i^{-1} \pmod{n_i}
$$

Then the solution to $x \equiv a_i \pmod{n_i}$ for all $i$ is

$$
x = \sum_{i=1}^{k} a_i u_i M_i \pmod N
$$

**Direct evaluation using the CRT construction formula.**
Here $a_1 = 2, n_1 = 3$; $a_2 = 1, n_2 = 4$; $a_3 = 3, n_3 = 5$.
The moduli are pairwise coprime, with $N = 3 \times 4 \times 5 = 60$.

1. $M_1 = \frac{60}{3} = 20$.
   We need $u_1 \equiv M_1^{-1} \pmod{n_1}$, so $20 u_1 \equiv 1 \pmod 3$.
   Since $20 \equiv 2 \pmod 3$, $2 u_1 \equiv 1 \implies u_1 = 2$.

2. $M_2 = \frac{60}{4} = 15$.
   We need $u_2 \equiv M_2^{-1} \pmod{n_2}$, so $15 u_2 \equiv 1 \pmod 4$.
   Since $15 \equiv 3 \pmod 4$, $3 u_2 \equiv 1 \implies u_2 = 3$.

3. $M_3 = \frac{60}{5} = 12$.
   We need $u_3 \equiv M_3^{-1} \pmod{n_3}$, so $12 u_3 \equiv 1 \pmod 5$.
   Since $12 \equiv 2 \pmod 5$, $2 u_3 \equiv 1 \implies u_3 = 3$.

Now evaluate the sum:

$$
x = a_1 u_1 M_1 + a_2 u_2 M_2 + a_3 u_3 M_3
= 2(2)(20) + 1(3)(15) + 3(3)(12)
$$

$$
= 80 + 45 + 108 = 233
$$

Reducing modulo $N = 60$:

$$
233 = 3(60) + 53 \equiv 53 \pmod{60}
$$

**Alternative verification: combining two congruences at a time.**

Combine the first two, $x \equiv 2 \pmod 3$ and $x \equiv 1 \pmod 4$. Write
$x = 2 + 3k$. Substituting into the second:

$$
2 + 3k \equiv 1 \pmod 4 \quad \Longrightarrow \quad 3k \equiv -1 \equiv 3 \pmod 4
$$

Since $3^{-1} \equiv 3 \pmod 4$, $k \equiv 3 \times 3 = 9 \equiv 1 \pmod 4$.
Hence $k = 1 + 4m$ and

$$
x = 2 + 3(1 + 4m) = 5 + 12m
$$

**Check:** $5 \bmod 3 = 2$ ✓ and $5 \bmod 4 = 1$ ✓.

Now impose the third, $x \equiv 3 \pmod 5$:

$$
5 + 12m \equiv 3 \pmod 5 \quad \Longrightarrow \quad 12m \equiv -2 \equiv 3 \pmod 5
$$

Since $12 \equiv 2 \pmod 5$ and $2^{-1} \equiv 3 \pmod 5$,

$$
m \equiv 3 \times 3 = 9 \equiv 4 \pmod 5
$$

Take $m = 4$:

$$
x = 5 + 12(4) = 53
$$

$$
\boxed{x \equiv 53 \pmod{60}}
$$

**Verify all three.**

$$
53 \bmod 3 = 2 \quad \checkmark \qquad 53 \bmod 4 = 1 \quad \checkmark \qquad 53 \bmod 5 = 3 \quad \checkmark
$$

Since $N = 3 \cdot 4 \cdot 5 = 60$, the complete solution set is
$x = 53 + 60k$ for every integer $k$.

> [!info] Check by exhaustive search
> Testing every residue $x$ from 0 to 59 against all three congruences returns
> exactly one, namely $53$. Hence the solution is unique modulo 60, which is what
> CRT guarantees when the moduli are pairwise coprime. Note that $4$ is **not**
> prime, so Fermat does not apply to it, but coprimality is all CRT needs and
> $\gcd(3,4) = \gcd(4,5) = \gcd(3,5) = 1$.

> [!note] Solving by inspection as a check
> $x \equiv 1 \pmod 4$ and $x \equiv 3 \pmod 5$ together give $x \equiv 13 \pmod{20}$.
> Values below 60 are $13, 33, 53$. Of these only $53$ is $2 \pmod 3$.

---

### **(b) There are four major auto routes from Boston to Detroit and six from Detroit to Los Angeles. How many major auto routes are there from Boston to Los Angeles via Detroit? [Marks: 02, CLO3]**

**Setting up.** A route via Detroit is fully described by **one** choice from
Boston to Detroit **and one** choice from Detroit to Los Angeles. There is no
other freedom, and the order is fixed by the geography: Boston first, Detroit
second, Los Angeles third.

This is the **product rule** (multiplication principle):

$$
\text{number of routes} = 4 \times 6
$$

$$
\boxed{24 \text{ routes}}
$$

> [!info] Check
> Listing the four Boston choices against the six Detroit choices gives a
> $4 \times 6$ grid of 24 cells, one route each. A direct product confirms
> $4 \times 6 = 24$.

> [!note] Why not the sum, and why not permutations
> The **sum rule** applies to alternatives that are mutually exclusive: either go
> through Detroit or through Chicago, never both. Here every route *must* go
> through Detroit, so the choices are sequential, not alternative, and the
> product rule is the one that applies.
>
> **Permutations do not apply** either. A route is fixed by its two legs, so
> choosing leg 1 then leg 2 already fixes the whole route and no reordering is
> possible or meaningful. This is a combination-like count of $24$ distinct
> paths, not $24$ orderings of something.

---

### **(c) Give a real-world example of generalized pigeonhole principle. [Marks: 02, CLO3]**

**The principle.** If $N$ objects are placed into $k$ boxes and $N > k$, then at
least one box holds at least two objects. The **generalized** form: if
$N > mk$, then some box holds at least $m + 1$ objects.

**Real-world examples.**

1. **Birth months in a class.** With 12 months, a class of 25 students guarantees
   that at least 3 share a birth month, since $25 > 2 \times 12 = 24$. Taking
   $m = 2$, $k = 12$ needs $N = 25$.

2. **Socks from a drawer.** A drawer holds only black and white socks. Drawing 5
   socks guarantees at least 3 of one colour, since $5 > 2 \times 2 = 4$.

3. **Hash tables.** Storing $n$ keys in $m$ buckets forces a collision once
   $n > m$. Keeping the load factor below 1, typically near 0.75, is what
   guarantees headroom before collisions become frequent.

4. **Servers.** A cluster with $r$ racks and $2r + 1$ machines must place at least
   3 machines in one rack.

$$
\boxed{\text{More than } mk \text{ objects in } k \text{ boxes forces some box to hold } m+1}
$$

> [!warning] The plain and generalized forms are different statements
> The plain principle is the case $m = 1$. Generalized needs
> $N > mk$, which is a **stronger** condition on $N$ and yields a **stronger**
> conclusion. The commonest slip is to use $N > k$ when $m > 1$, which forces
> only two in a box, not $m + 1$. With 25 students and 12 months, "more students
> than months" would force only a pair; the $2 \times 12 = 24$ threshold is what
> forces a triple.

---

### **(d) Let $d$ be a positive integer. Show that among any group of $d+1$ (not necessarily consecutive) integers there are two with exactly the same remainder when they are divided by $d$. [Marks: 02, CLO3]**

**Proof.**

**Step 1. Count the possible remainders.** For any integer $a$, the division
algorithm gives

$$
a = qd + r, \qquad 0 \le r < d
$$

Every integer therefore has exactly one of the residues $0, 1, 2, \dots, d-1$.
There are exactly **$d$** possible remainders.

**Step 2. Identify the boxes.** Take the $d+1$ integers and let each box be one of
the $d$ possible remainders, $0$ through $d-1$. Place each integer in the box
named by its remainder.

**Step 3. Apply the pigeonhole principle.** There are $d + 1$ integers placed
into $d$ boxes, and $d + 1 > d$. By the pigeonhole principle, at least one box
contains two or more integers.

**Step 4. Conclude.** Two integers $a_1, a_2$ share a box, so they share a
remainder. Writing $a_1 = q_1 d + r$ and $a_2 = q_2 d + r$, subtracting gives

$$
a_1 - a_2 = (q_1 - q_2)d
$$

hence $d$ divides $a_1 - a_2$, which is exactly the statement that the two have the
same remainder on division by $d$.

$$
\boxed{\text{Any } d+1 \text{ integers include two congruent modulo } d}
$$

> [!info] Check
> For $d = 1, 2, \dots, 7$, explicit examples were constructed in which a repeated
> remainder occurs among $d+1$ integers: $d = 1$ gives $0, 0$; $d = 3$ gives
> $0, 1, 2, 0$; $d = 5$ gives $0, 1, 2, 3, 4, 0$. In every case the repetition is
> forced, matching the proof.

> [!note] The bound is sharp
> With only $d$ integers no repetition is forced: take $0, 1, 2, \dots, d-1$, whose
> remainders are all distinct. Hence $d + 1$ is the **smallest** number of integers
> that guarantees a collision, and the theorem says exactly that.

> [!note] What this is used for
> This is the statement behind every proof of the **pigeonhole principle** for
> congruences, and behind the fact that $x \equiv y \pmod d$ has infinitely many
> solutions while $x \equiv y \pmod n$ with the same residue class has at most
> $\gcd(x-y, n)$ distinct residues. It is also the reason a hash table with $m$
> buckets cannot hold $m+1$ distinct keys without a collision, which is the same
> counting argument with different words.