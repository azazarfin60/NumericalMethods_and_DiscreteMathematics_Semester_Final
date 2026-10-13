---
title: "NM-4.1 · Concepts"
tags:
  - numerical-methods
  - discrete-mathematics
  - topicwise
---


[🏠 Subtopic Index](00_Index.md) | [← Prev: NM-3.8 Circuit Applications](NM-3.8_Circuit_Applications.md) | [Next: NM-4.2 Least-Squares Linear Regression →](NM-4.2_Least_Squares_Linear_Regression.md)

---

# NM-4.1 · Concepts

Every block below is copied from `../answers_exam_style/`, which is the
only place an answer is authored. A number here is the same number, character
for character, as the one it came from.


### [2017 Q.5(a)]

**Question.** Define: (i) Interpolation (ii) Extrapolation (iii) Curve Fitting.

**Solution.**

**Interpolation** is the estimation of a value of a function at a point
**within** the range covered by a set of known values. The estimated value is
obtained from the known values alone, and the interpolation curve passes
exactly through them. For a table covering $[x_0, x_n]$, a target $x$ with
$x_0 < x < x_n$ is interpolated.

**Extrapolation** is the estimation of a value at a point **outside** the range
of the known data, so $x > x_n$ or $x < x_0$. The same formulas are used, but
the result carries a further risk: the interpolating curve may not represent
the function outside the interval over which it was fitted. Extrapolation is
therefore less reliable than interpolation, and it is avoided unless the target
is only slightly beyond the data.

**Curve fitting** is the construction of an equation $y = f(x)$ that describes
the trend of a set of data points, without requiring that the curve pass
through any of them. Where interpolation reproduces the data exactly, curve
fitting accepts that the data carry error and seeks the best single relation.

**The distinction between the three.** All three estimate values from data. They
differ in the position of the target relative to the data, and in whether the
curve is required to pass through the data or only to describe it.
Interpolation is inside the data and exact through it; extrapolation is outside
it; curve fitting is inside it but need not pass through it.

---

### [2019 Q.4(a)]

**Question.** What is curve fitting? Why is it required for ECE engineers? Discuss least square technique condition.

**Solution.**

**Curve fitting** is the construction of an equation $y = f(x)$ that represents
the trend of a set of data points $(x_i, y_i)$. Where interpolation forces the
curve through every point, curve fitting accepts that the points carry error and
seeks a single relation that describes the whole set.

**Why it is required for ECE engineers**

1. **Data are noisy.** A voltage, a gain, a delay or a bit-error rate measured
   repeatedly gives scattered values. Fitting an underlying law separates the
   trend from the scatter and quantifies the scatter.
2. **A compact model is wanted.** A characteristic measured at ten points is
   replaced by two or three constants, which is what a simulator and a hand
   calculation both use.
3. **Values must be predicted** where no measurement exists, inside and
   immediately outside the measured range.
4. **Parameters must be extracted.** Resistance, inductance, time constant,
   cut-off frequency and beta are all obtained by fitting the measured response
   to the known equation of the device.

**Least squares.** Let the trial curve be $y = a_0 + a_1 x + \cdots + a_m g_m(x)$.
The residual at point $i$ is $r_i = y_i - f(x_i)$. The coefficients are chosen to
minimise the sum of squared residuals,

$$S = \sum_{i=1}^{n} r_i^2 = \sum_{i=1}^{n}\left(y_i - f(x_i)\right)^2$$

The **conditions** are obtained by setting each partial derivative to zero:

$$\frac{\partial S}{\partial a_0} = 0, \quad \frac{\partial S}{\partial a_1} = 0, \quad \ldots$$

which gives the **normal equations**. For the straight line $y = a + bx$:

$$\sum y = na + b\sum x, \qquad \sum xy = a\sum x + b\sum x^2$$

and in general the squares are needed because the minimum, not the root, is
sought: setting the derivatives to zero locates the stationary point of $S$, and
the second derivatives are positive there, so it is a minimum.

**The least-squares condition, stated fully.** Of all curves in the chosen family,
the least squares curve is the one for which the residuals satisfy

- $\sum r_i^2$ is a minimum, and
- $\sum r_i = 0$ (the positive and negative residuals cancel),
- $\sum x_i r_i = 0$ (the residuals are orthogonal to the regressor),

which follows directly from the two normal equations. The three conditions are
the algebraic signature of the fit: the line passes through the centroid
$(\bar x, \bar y)$, and the residuals are uncorrelated with the fitted values.

> [!info] Check against the centroid condition
> Substituting $\sum r_i = 0$ into the definition $r_i = y_i - a - bx_i$ gives
> $a = \bar y - b\bar x$, which is the intercept rewritten in terms of the slope.
> The identity holds for any data set, so it is a structural check on the normal
> equations rather than on a particular calculation.

---

### [2019 Q.5(a)]

**Question.** Define interpolation and extrapolation. List two general techniques of curve fitting.

**Solution.**

**Interpolation** is the estimation of an intermediate value of a function from a
set of known values, at a point **within** the range covered by the known data.
**Extrapolation** is the estimation of a value at a point **outside** that range.
Interpolation is bounded by the data; extrapolation extends beyond it.

The two are distinguished by the position of the target relative to the tabulated
interval. For a table covering $[x_0, x_n]$, a target $x$ with $x_0 < x < x_n$ is
interpolated; a target with $x > x_n$ or $x < x_0$ is extrapolated.
Extrapolation carries the further risk that the fitted relation may not hold
outside the range where it was fitted at all.

**Two general techniques of curve fitting**

1. **Least squares fitting.** A curve $y = a + bx + \cdots$ is fitted by choosing
   its coefficients to minimise $\sum r_i^2$, the sum of squared residuals. The
   curve does not pass through the points, but captures the trend, so it is
   appropriate for noisy data.
2. **Exact interpolation fitting.** A curve is made to pass through every tabulated
   point, using the family of methods built from divided differences and Lagrange
   polynomials. It reproduces the data exactly and is appropriate where the data
   are error-free.

Other techniques include the geometric mean, moving average and orthogonal
polynomial fits; the two above are the general ones.

---

### [2020 Q.3(a)]

**Question.** What is the main difference between interpolation and extrapolation? Where are they used?

**Solution.**

**The difference.**

| | Interpolation | Extrapolation |
| :-- | :-- | :-- |
| Target $x$ | **Inside** the data range, $x_{\min} \le x \le x_{\max}$ | **Outside** it |
| What the curve is doing | Bridging a known span | Continuing past the last data point |
| Reliability | High, the data surround the target | **Low**, the polynomial is unsupported there |
| Typical error | Small | Grows rapidly with distance |
| What it assumes | The function is smooth in the region | The function stays smooth **outside** the region, which nothing guarantees |

**The reason extrapolation is risky.** A polynomial of degree $n$ through $n+1$
points matches the data exactly and says nothing at all beyond the last node. The
error term is

$$
f(x) - P_n(x) = \frac{f^{(n+1)}(\xi)}{(n+1)!}\prod_{i=0}^{n}(x - x_i)
$$

and outside the range that product **grows** while the points give no control
over $f^{(n+1)}$. A curve that is flat over the sampled region can turn over
completely just beyond it.

**Where interpolation is used.** Reading a value off a mathematical function at
an inconvenient argument. Values defined by interpolation in a standard, such as
a density table or a steam table. Reproducing a signal between samples, for
example a sine wave reconstructed from discrete samples.

**Where extrapolation is used.** Forecasting beyond the last observation, such as
a population projection or a demand forecast. Continuing a trajectory in time
from sampled position data, as in 2020 Q.3(b). Filling a small gap just past the
edge of a measured range. Using a Taylor series about a known point.

The shared caution: interpolation needs the data to bracket the target, and
extrapolation needs the underlying function to stay well behaved past the edge.
Only the first is under control.

> [!note] The same line of code does both
> A Lagrange or Newton interpolant does not know whether $x$ is inside or outside
> the node set. It evaluates happily either way and returns a number of very
> different quality. **The caller must check.** Always ask where the target sits
> relative to the first and last node before trusting the result.

$$
\boxed{\text{Interpolation fills a gap the data surround; extrapolation guesses past the edge}}
$$

---

### [2021 Q.3(a)]

**Question.** When should we use interpolation instead of curve fitting?

**Solution.**

Apply **interpolation** when the data are **exact** and the target lies **between**
the given points.

Two conditions must both hold:

1. **The data are exact.** Interpolation forces the curve through every point, so
   any measurement error is copied faithfully into the answer. Noise in, noise out,
   amplified.
2. **The target lies inside the data range.** Outside it the method is extrapolation,
   which is far less trustworthy.

Typical situations: a value read off a mathematical function, a quantity defined by
interpolation in a standard, a small number of exact tabulated constants.

Apply **curve fitting** when the data carry measurement error, when the underlying
trend is the object of interest rather than reproduction of every point, or when a
lower-degree form is wanted from many noisy points.

$$
\boxed{\text{Exact data and a target between the points: interpolate. Noisy data: fit.}}
$$

---

### [2021 Q.4(a)]

**Question.** Give a real life example of curve fitting.

**Solution.**

**Calibrating a thermocouple.**

A calibration certificate lists certified reference temperatures and the
corresponding indicated voltages:

| Reference ($^{\circ}$C) | Indicated (mV) |
| --: | --: |
| 0 | 0.00 |
| 100 | 4.09 |
| 200 | 7.33 |
| 400 | 12.45 |

The readings carry thermal drift and instrument noise, so no curve passes exactly
through all four. Fitting a polynomial by **least squares** finds the one that
comes closest, and the fitted curve then calibrates the instrument: a raw reading of
$9.20$ mV converts to a temperature through the fit.

Second example: a **load-extension test**, where the raw data scatter because the
specimen is not perfectly uniform, and the fitted line gives the engineering stress
and stiffness.

**Why fitting rather than interpolation.** The four certified points are known only
to about $\pm 0.5^{\circ}\text{C}$. Interpolating would force the curve through each
one exactly, importing that uncertainty into every answer. Least squares smooths it
and gives a usable law between and beyond the points.

$$
\boxed{\text{Sensor calibration: noisy readings in, a best-fit law out, and predictions follow}}
$$

---

### [2022 Q.1(c)]

**Question.** Explain a real life application of curve-fitting. For what type of data points will you use Lagrange's interpolation formula?

**Solution.**

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

### [2023 Q.4(a)]

**Question.** Briefly explain interpolation, extrapolation and curve fitting with examples.

**Solution.**

All three take discrete data and produce a continuous relation. They differ in
what they promise.

**Interpolation.** Build a function that passes through **every** given point
exactly.

$$
P(x_i) = y_i \quad \text{for every } i
$$

The answer is exact at the data and carries no modelling error. Example: a
thermocouple is calibrated at $0^{\circ}$C and $100^{\circ}$C, and its reading at
$37^{\circ}$C is found by interpolating between those two calibrations.

**Extrapolation.** Evaluate a fitted function **outside** the range of the data.
The function may pass through every point and still say nothing trustworthy
outside, because nothing constrains it there.

Example: predicting the sales figure for next year from five years of history.
The fit is exact on those five years and still can be badly wrong on the sixth.

**Curve fitting.** Find the function that comes **closest** to all points
without passing through any, by minimising a misfit such as
$\sum_i [y_i - f(x_i)]^2$.

Example: fitting a straight line to seven noisy voltage readings to recover the
true calibration slope.

| | Interpolation | Extrapolation | Curve fitting |
| :-- | :-- | :-- | :-- |
| Passes through data | Yes | May or may not | No |
| Outside the data | Not defined | Defined but unreliable | Defined, degree dependent |
| Data assumed | Exact | Exact | Noisy |
| Point count | Need $n+1$ points for degree $n$ | Same | Can use fewer |
| Risk | Runge oscillation far out | Large and growing error | Under-fitting if too simple |

**Choosing between them.** Interpolate inside the data. Fit when the data are
noisy, or when the underlying trend is the object of interest. Extrapolation is
required only when the target lies outside the data range, and only over a short
distance, no more than about one data interval.

$$
\boxed{\text{interpolation passes through, extrapolation goes beyond, fitting minimises}}
$$

---

### [2024 Q.3(a)]

**Question.** Discuss the operation of curve fitting and interpolation.

**Solution.**

Both take discrete data and produce a smooth relation, but they answer different
questions.

**Interpolation.** Find a function that passes through **every** given point
exactly. The result reproduces the data by construction.

$$
P(x_i) = y_i \quad \text{for all } i
$$

Interpolation applies when the data are accurate and values are needed between
them. Example: reading a voltage between two calibration points.

**Extrapolation.** The same formula evaluated **outside** the range of the data.
The result is an unconstrained estimate with no accuracy guarantee. Example:
predicting next year's population from five decades of census figures.

**Curve fitting.** Find the function that comes **closest** to all the points
without passing through any of them, by minimising a chosen measure of
misfit, usually

$$
\sum_{i=1}^{n} \left[y_i - f(x_i)\right]^2
$$

which is least squares. Use it when the data carry noise, or when a simpler form
than degree $n$ is wanted. Example: fitting a straight line through seven noisy
measurements.

| | Interpolation | Curve fitting |
| :-- | :-- | :-- |
| Passes through the data | Yes | No |
| Data assumed | Exact | Noisy |
| Degree | Up to $n$ for $n+1$ points | Chosen, often lower |
| Answers | What is between the points | What is the underlying trend |

$$
\boxed{\text{Interpolation reproduces data; curve fitting explains it}}
$$

---

---

**Also asked here.**

- *2020 Q.3(c)* is the same question as [[NM-4.3_Non_Linear_Regression|NM-4.3]], which is written in `NM-4.3`.

---

[🏠 Subtopic Index](00_Index.md) | [← Prev: NM-3.8 Circuit Applications](NM-3.8_Circuit_Applications.md) | [Next: NM-4.2 Least-Squares Linear Regression →](NM-4.2_Least_Squares_Linear_Regression.md)
