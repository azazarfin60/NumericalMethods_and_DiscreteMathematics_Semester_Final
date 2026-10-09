---
title: "NM-4.1 · Concepts"
tags:
  - numerical-methods
  - discrete-mathematics
  - topicwise
---

# NM-4.1 · Concepts

Every block below is copied from `../answers_explanation/`. The reasoning
is written once, in the year-wise file, and is not restated here.


### [2017 Q.5(a)]

**Question.** Define: (i) Interpolation (ii) Extrapolation (iii) Curve Fitting.

*[Marks: 03]*

**Solution.**

**Interpolation** is the estimation of a value of a function at a point
**within** the range covered by a set of known values. The estimate is obtained
from the known values alone, and the interpolation curve passes *exactly*
through them. For a table covering $[x_0, x_n]$, a target with
$x_0 < x < x_n$ is interpolated.

**Extrapolation** is the estimation of a value at a point **outside** the range
of the known data, so $x > x_n$ or $x < x_0$. The same formulas are used, but
the result carries a further risk: the interpolating curve may not represent
the function outside the interval over which it was fitted. Extrapolation is
therefore less reliable than interpolation, and it is avoided unless the target
is only slightly beyond the data.

**Curve fitting** is the construction of an equation $y = f(x)$ that describes
the *trend* of a set of data points, without requiring the curve to pass
through any of them. Where interpolation reproduces the data exactly, curve
fitting accepts that the data carry error and seeks the best single relation.

**The distinction between the three.** All three estimate values from data.
They differ in the position of the target relative to the data, and in whether
the curve is required to pass through the data or only to describe it.

| | Target relative to data | Passes through the data |
| :-- | :-- | :-- |
| Interpolation | inside | yes, exactly |
| Extrapolation | outside | yes, exactly |
| Curve fitting | inside | no |

> [!note] The third column is the one that gets confused
> Interpolation and curve fitting both answer questions *inside* the data, so
> the position of the target does not separate them. What separates them is
> whether the data are assumed exact. With exact data, interpolation is
> correct and fitting through them is right. With measured data, the ordinates
> carry error, forcing the curve to miss some of them, and then the best
> single relation is the fit rather than the interpolant. A noise-free table
> asks for interpolation; a table with $0.5$ of scatter in it asks for fitting.

---

### [2019 Q.4(a)]

**Question.** What is curve fitting? Why is it required for ECE engineers? Discuss least square technique condition.

*[Marks: 04]*

**Solution.**

**Curve fitting** is the construction of an equation $y = f(x)$ that represents the
trend of a set of data points $(x_i, y_i)$. Where interpolation forces the curve
through every point, curve fitting accepts that the points carry error and seeks a
single relation that describes the whole set.

**Why it is required for ECE engineers**

1. **Data are noisy.** A voltage, a gain, a delay or a bit-error rate measured
   repeatedly gives scattered values. Fitting an underlying law separates the trend
   from the scatter and quantifies the scatter.
2. **A compact model is wanted.** A characteristic measured at ten points is
   replaced by two or three constants, which is what a simulator and a hand
   calculation both use.
3. **Values must be predicted** where no measurement exists, inside and immediately
   outside the measured range.
4. **Parameters must be extracted.** Resistance, inductance, time constant,
   cut-off frequency and beta are all obtained by fitting the measured response to
   the known equation of the device.

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

which follows directly from the two normal equations. The three conditions are the
algebraic signature of the fit: the line passes through the centroid
$(\bar x, \bar y)$, and the residuals are uncorrelated with the fitted values.

> [!info] Check against the centroid condition
> Substituting $\sum r_i = 0$ into the definition $r_i = y_i - a - bx_i$ gives
> $a = \bar y - b\bar x$, which is the intercept rewritten in terms of the slope.
> The identity holds for any data set, so it is a structural check on the normal
> equations rather than on a particular calculation.

> [!note] The one-line check that needs no algebra
> $\sum r_i = 0$ is the cheapest test of a least squares fit that exists. Add the
> residuals: if they do not cancel to zero, the coefficients are wrong or the
> arithmetic is. It costs one addition per data point.
>
> It is the fitting analogue of the bracketing sign change, and it catches the
> commonest fitting error, which is swapping the two normal equations.

---

### [2019 Q.5(a)]

**Question.** Define interpolation and extrapolation. List two general techniques of curve fitting.

*[Marks: 03]*

**Solution.**

**Interpolation** is the estimation of an intermediate value of a function from a
set of known values, at a point **within** the range covered by the known data.
**Extrapolation** is the estimation of a value at a point **outside** that range.
Interpolation is bounded by the data; extrapolation extends beyond it.

The two are distinguished by the position of the target relative to the tabulated
interval. For a table covering $[x_0, x_n]$, a target $x$ with $x_0 < x < x_n$ is
interpolated; a target with $x > x_n$ or $x < x_0$ is extrapolated. Extrapolation
carries the further risk that the fitted relation may not hold outside the range
where it was fitted at all.

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

> [!note] The dividing line is the data, not the method
> The same Lagrange polynomial does both interpolation and extrapolation. What
> changes is only whether $x$ lies inside the node set.
>
> **The choice is therefore made before the arithmetic, not during it.** Once the
> target is outside the range, no amount of care in the calculation recovers the
> missing information, and the honest response is to report the estimate together
> with the distance past the last point, so a reader can judge it.
>
> Part (b) below is an interpolation and gets $2.46$ A against a true $2.4$ A. Had
> the target been $30$ V instead of $12$ V, the same formula would give a number
> with no useful meaning at all, and nothing in the calculation would say so.

---

### [2020 Q.3(a)]

**Question.** What is the main difference between interpolation and extrapolation? Where are they used?

*[Marks: 03]*

**Solution.**

**The difference.**

| | Interpolation | Extrapolation |
| :-- | :-- | :-- |
| Target $x$ | **Inside** the data range, $x_{\min} \le x \le x_{\max}$ | **Outside** it |
| What the curve is doing | Bridging a known span | Continuing past the last data point |
| Reliability | High, the data surround the target | **Low**, the polynomial is unsupported there |
| Typical error | Small | Grows rapidly with distance |
| What it assumes | The function is smooth in the region | The function stays smooth **outside** the region, which nothing guarantees |

$$\boxed{\text{Interpolation fills a gap the data surround; extrapolation guesses past the edge}}$$

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
a population projection or a demand forecast. Continuing a trajectory in time from
sampled position data, as in Q.3(b) below. Filling a small gap just past the edge
of a measured range. Using a Taylor series about a known point.

The shared caution: interpolation needs the data to bracket the target, and
extrapolation needs the underlying function to stay well behaved past the edge.
Only the first is under control.

> [!warning] The same line of code does both
> A Lagrange or Newton interpolant does not know whether $x$ is inside or outside
> the node set. It evaluates happily either way and returns a number of very
> different quality. **The caller must check.** Always ask where the target sits
> relative to the first and last node before trusting the result.

---

### [2021 Q.3(a)]

**Question.** When should we use interpolation instead of curve fitting?

*[Marks: 02, CO: 2]*

**Solution.**

Apply **interpolation** when the data are **exact** and the target lies **between**
the given points.

Two conditions must both hold.

1. **The data are exact.** Interpolation forces the curve through every point, so
   any measurement error is copied faithfully into the answer. Noise in, noise
   out, amplified.
2. **The target lies inside the data range.** Outside it the method is
   extrapolation, which is far less trustworthy.

Typical situations: a value read off a mathematical function, a quantity defined
by interpolation in a standard, a small number of exact tabulated constants.

Apply **curve fitting** when the data carry measurement error, when the underlying
trend is the object of interest rather than reproduction of every point, or when a
lower-degree form is wanted from many noisy points.

$$\boxed{\text{Exact data and a target between the points: interpolate. Noisy data: fit.}}$$

> [!warning] The asymmetry that catches people
> Interpolation and fitting are not two names for the same calculation. They
> optimise different things.
>
> Interpolation minimises **nothing**. It is determined exactly by the data, and
> the data determine it completely. Fitting minimises a sum of squared residuals,
> which means the answer depends on the data only through those residuals and
> deliberately does **not** pass through the points.
>
> So the question "which is better" has no answer. The question "are these numbers
> measurements or exact values" has one, and that is the question to ask.

---

### [2021 Q.4(a)]

**Question.** Give a real life example of curve fitting.

*[Marks: 02, CO: 2]*

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
comes closest, and the fitted curve then calibrates the instrument: a raw reading
of $9.20$ mV converts to a temperature through the fit.

Second example: a **load-extension test**, where the raw data scatter because the
specimen is not perfectly uniform, and the fitted line gives the engineering
stress and stiffness.

$$\boxed{\text{Sensor calibration: noisy readings in, a best-fit law out, and predictions follow}}$$

> [!warning] Why fitting rather than interpolation, stated as a number
> The four certified points are known only to about $\pm 0.5^{\circ}\text{C}$.
> Interpolating would force the curve through each one exactly, importing that
> uncertainty into every answer, and would make the answer wobble as though the
> uncertainty were real structure.
>
> Least squares smooths it and gives a usable law between and beyond the points.
> This is the Q.3(a) distinction with a consequence attached: here the choice is
> worth half a degree, and on a steep part of the calibration that is a real error
> in the reported temperature.

---

### [2022 Q.1(c)]

**Question.** Explain a real life application of curve-fitting. For what type of data points will you use Lagrange's interpolation formula?

*[Marks: 04, CO: 2]*

**Solution.**

**A real application.** Calibrating a **thermocouple**, or any sensor, against
certified reference temperatures.

A calibration certificate lists reference points:

| Reference temperature ($^{\circ}$C) | Indicated reading (mV) |
| --: | --: |
| 0 | 0.00 |
| 100 | 4.09 |
| 200 | 7.33 |
| 400 | 12.45 |

Each reading carries thermal drift and instrument noise, so no curve passes
exactly through all four points. Least squares finds the one that comes closest,
and the fitted curve then **calibrates** the instrument: a raw reading of
$9.20$ mV is converted to a temperature through it. The calibration curve is not
an interpolation of the data, it is a fit, because the data are measurements.

A second application: a **load-extension test**, where the raw data scatter
because the specimen is not perfectly uniform, and the fitted curve is what
gives the engineering stress and stiffness.

**When to reach for Lagrange.** Use it when **all** of these hold.

1. **The data are exact.** Interpolation forces the curve through every point, so
   any error in a data point is copied straight into the answer.
2. **The points are few.** Two give a line, three a parabola; the degree rises by
   one with each extra point. Many exact points make the expression unwieldy.
3. **The spacing is uneven.** Lagrange needs no common difference $h$. Newton
   forward and backward both require equal spacing.
4. **The target is inside the data range.** Outside it, Lagrange oscillates badly
   and a fitted curve is the right tool instead.

| Situation | Method |
| :-- | :-- |
| Few, exact, irregularly spaced | **Lagrange** |
| Many, equally spaced, exact, near the start | Newton forward |
| Many, equally spaced, exact, near the end | Newton backward |
| Noisy data, any spacing | Least squares |
| Target outside the data | Least squares, not interpolation |

> [!warning] Interpolating noisy data guarantees a wrong answer
> Lagrange reproduces every data point **exactly**, including its noise. If the
> "data" come off a real instrument, that means the answer is wrong at least as
> often as the instrument is.
>
> The test to apply is quick: ask whether the data are measurements or values of
> a mathematical function. Measurements call for fitting. Values call for
> interpolation. Mixing them up is the single most common misuse of Lagrange's
> formula.

> [!note] Cost and numerical stability
> Lagrange costs $O(n^2)$ work per evaluation and grows less efficient as points
> are added, since each new point adds a term without improving the fit
> elsewhere. Near large $n$ the expression is a sum of large cancelling terms,
> which is where round off bites. Newton's divided difference form, or Neville's
> algorithm, is better behaved numerically when many points are involved.

---

### [2023 Q.4(a)]

**Question.** Briefly explain interpolation, extrapolation and curve fitting with examples.

*[Marks: 03, CO: 1]*

**Solution.**

All three take discrete data and produce a continuous relation. They differ in
what they **promise**, and the promise is what you are choosing when you pick
one.

**Interpolation** builds a function that passes through **every** given point
exactly:

$$
P(x_i) = y_i \quad \text{for every } i
$$

The answer is exact at the data and carries no modelling error at all. Example: a
thermocouple is calibrated at $0^{\circ}$C and $100^{\circ}$C, and its reading at
$37^{\circ}$C is found by interpolating between those two calibrations.

**Extrapolation** evaluates a fitted function **outside** the range of the data.
The function may pass through every point perfectly and still say nothing
trustworthy outside, because **nothing constrains it there**. Example: predicting
next year's sales figure from five years of history. The fit is exact on those
five years and can still be badly wrong on the sixth, because the polynomial that
threads five points has no particular opinion about the sixth.

**Curve fitting** finds the function that comes **closest** to all points without
passing through any, by minimising a misfit such as

$$
\sum_i \left[y_i - f(x_i)\right]^2
$$

Example: fitting a straight line to seven noisy voltage readings to recover the
true calibration slope. The line deliberately misses the readings, because
passing through them would reproduce the noise as well as the signal.

| | Interpolation | Extrapolation | Curve fitting |
| :-- | :-- | :-- | :-- |
| Passes through data | Yes | May or may not | No |
| Outside the data | Not defined | Defined but unreliable | Defined, degree dependent |
| Data assumed | Exact | Exact | Noisy |
| Point count | Need $n+1$ points for degree $n$ | Same | Can use fewer |
| Risk | Runge oscillation far out | Large and growing error | Under-fitting if too simple |

**Choosing between them.** Interpolate inside the data. Fit when the data are
noisy, or when the underlying trend rather than the individual points is the
object of interest. Extrapolation is required only when the target genuinely
lies outside the data range, and then only over a short distance, at most about
one data interval.

> [!warning] Extrapolation is not interpolation with a different number
> The trap is thinking that a degree 4 polynomial through five points is a
> reliable description of the function everywhere. It is an exact description
> at five points and an arbitrary one everywhere else. The dramatic version is
> Runge's phenomenon: a high-degree interpolant oscillates violently outside the
> data range while fitting perfectly inside it. Adding *more* data points makes
> this worse, not better.

> [!note] The one-line version
> $$\boxed{\text{interpolation passes through, extrapolation goes beyond, fitting minimises}}$$
>
> Three verbs, one per technique, and they are the whole distinction. If you
> remember nothing else from this question, remember that the first passes through,
> the second goes beyond, and the third gets as close as it can without touching.

---

### [2024 Q.3(a)]

**Question.** Discuss the operation of curve fitting and interpolation.

*[Marks: 02, CO: 1]*

**Solution.**

Both estimate the value of a function from data, and the difference is whether
the estimated curve is required to pass through the known points.

**Interpolation** constructs a curve through every tabulated point exactly. The
interpolant reproduces the data. It is the right tool when the data are known to
be accurate and the noise is negligible, such as values taken from a table of a
known function or a calibrated instrument.

**Curve fitting** constructs a curve that captures the trend without passing
through the points. The fitted curve does not reproduce the data; it summarises
them. It is the right tool when the data carry measurement error, because
forcing the curve through noisy points reproduces the noise as well as the
signal.

**How the difference shows up.** With five points, interpolating gives a quartic
that passes through all five, including any scatter among them. Fitting a line
to the same five points gives a line that misses all five but shows the
direction. Neither is wrong; they answer different questions.

**The test for which to use.** Ask what the data are: exact tabulated values, or
measurements? Ask what is wanted: the value at an intermediate point, or the
model of the trend? Exact data and an intermediate value gives interpolation.
Measured data and a model gives fitting.

$$\boxed{\text{Interpolation reproduces data; curve fitting explains it}}$$

**The general methods.**

| Method | Curve through points | Best for |
| :-- | :-: | :-- |
| Lagrange interpolation | yes | exact, unevenly spaced data |
| Newton divided differences | yes | exact, equally spaced, points added later |
| Least squares fitting | no | noisy data, a trend model |
| Piecewise (spline) interpolation | yes, locally | many points, avoiding oscillation |

> [!note] Why the exam asks this
> Two marks for a comparison, so the marks are for stating the distinction and
> the test for choosing, not for listing methods. The most common way to lose
> both marks is to describe interpolation in detail and then write "curve fitting
> is similar" without saying what is different.

---

---

**Also asked here.**

- *2020 Q.3(c)* is the same question as [[NM-4.3|NM-4.3]], which is written in `NM-4.3`.

---
