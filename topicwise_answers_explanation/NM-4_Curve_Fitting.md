---
title: "NM-4 · Curve Fitting & Interpolation"
tags:
  - numerical-methods
  - discrete-mathematics
  - topicwise-clusters
---

[🏠 Master Index](00_Index.md) | [← Prev Topic: NM-3 · Linear Systems](NM-3_Linear_Systems.md) | [Next Topic: NM-5 · Numerical Integration →](NM-5_Numerical_Integration.md)

---

# NM-4 · Curve Fitting & Interpolation

> **Topic ID:** NM-4  
> **Section:** Section A -- Numerical Methods  
> **Exam Weight:** 🔴 High Priority (Tier 1) | 8/8 Years Examined (100% Frequency) | Typical Weight: 14–18 marks (Questions 3 & 4)  
> **Subtopics Included:** 10 subtopics (NM-4.1 through NM-4.11)  
> **Origin Layer:** Authored in `../answers_explanation/`. All numerical results and boxed equations match character-for-character.

---

## 📑 Subtopics Covered in this Cluster

| Subtopic ID | Subtopic Title | Priority | Exam Frequency | Section Navigation |
|:---|:---|:---:|:---:|:---|
| **NM-4.1** | Concepts | 🔴 | 2017, 2019, 2020, 2021, 2022, 2023, 2024 | [Jump to NM-4.1](#nm-41) |
| **NM-4.2** | Least-Squares Linear Regression | 🔴 ⚠️ | 2017, 2018, 2019, 2024 | [Jump to NM-4.2](#nm-42) |
| **NM-4.3** | Non-Linear Regression | 🔴 ⚠️ | 2017, 2020, 2022 | [Jump to NM-4.3](#nm-43) |
| **NM-4.4** | Regression Criteria & Theory | 🟠 ⚠️ | 2017, 2019 | [Jump to NM-4.4](#nm-44) |
| **NM-4.5** | Linear Interpolation | 🟠 | 2018, 2019 | [Jump to NM-4.5](#nm-45) |
| **NM-4.6** | Lagrange's Interpolation | 🔴 | 2018, 2019, 2021, 2022, 2023, 2024, CT-02A | [Jump to NM-4.6](#nm-46) |
| **NM-4.7** | Newton's Forward Difference | 🔴 | 2018, 2020, 2021, 2022, 2023, CT-02A | [Jump to NM-4.7](#nm-47) |
| **NM-4.9** | Newton's Divided Difference / General Interpolation | 🟠 | 2019, 2020, 2022 | [Jump to NM-4.9](#nm-49) |
| **NM-4.10** | Gauss Forward / Backward & Stirling's Formulas | 🟡 ⚠️ | 2021 | [Jump to NM-4.10](#nm-410) |
| **NM-4.11** | Difference Table Formation & Applications | 🔴 | 2017, 2020, 2021, 2022, 2024 | [Jump to NM-4.11](#nm-411) |

---

<a id="nm-41"></a><a id="nm-4.1"></a>
## NM-4.1 · Concepts

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

- *2020 Q.3(c)* is the same question as [[NM-4.3_Non_Linear_Regression|NM-4.3]], which is written in `NM-4.3`.

---

<a id="nm-42"></a><a id="nm-4.2"></a>
## NM-4.2 · Least-Squares Linear Regression

### [2017 Q.6(b), 2024 Q.3(c)]

**Appeared in:** 2017 Q.6(b), 2024 Q.3(c)

**Question.** Fit a straight line to the $x$ and $y$ values in the first two columns of the following table.

*[Marks: 04]*

**Solution.**

| $x$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| $y$ | 0.5 | 2.5 | 2.0 | 4.0 | 3.5 | 6.0 | 5.5 |

**The sums.** With $n = 7$,

$$\sum x = 28, \qquad \sum y = 24, \qquad \sum xy = 119.5, \qquad \sum x^2 = 140$$

$\sum xy$ is the term that needs care, being the only one that is not a straight
sum of a column. Its seven products are

$$1(0.5) = 0.5, \quad 2(2.5) = 5, \quad 3(2) = 6, \quad 4(4) = 16, \quad 5(3.5) = 17.5, \quad 6(6) = 36, \quad 7(5.5) = 38.5$$

which add to $119.5$.

**The normal equations.** With $a\sum x + b\sum x^2 = \sum xy$ and
$na + b\sum x = \sum y$:

$$28a + 140b = 119.5, \qquad 7a + 28b = 24$$

Multiply the second by $4$, giving $28a + 112b = 96$, and subtract it from the
first:

$$28b = 119.5 - 96 = 23.5 \implies b = \frac{23.5}{28} = \frac{47}{56} = 0.839286$$

Substituting back into the second:

$$7a = 24 - 28(0.839286) = 24 - 23.5 = 0.5 \implies a = \frac{0.5}{7} = \frac{1}{14} = 0.071429$$

**The fitted line.**

$$\boxed{y = 0.0714 + 0.8393x}$$

**The residuals.**

| $x$ | $y$ | $0.0714 + 0.8393x$ | $e = y - \hat y$ |
| :--: | :-- | :-- | :-- |
| 1 | 0.5 | 0.9107 | $-0.4107$ |
| 2 | 2.5 | 1.7500 | $+0.7500$ |
| 3 | 2.0 | 2.5893 | $-0.5893$ |
| 4 | 4.0 | 3.4286 | $+0.5714$ |
| 5 | 3.5 | 4.2679 | $-0.7679$ |
| 6 | 6.0 | 5.1071 | $+0.8929$ |
| 7 | 5.5 | 5.9464 | $-0.4464$ |

The residuals sum to zero, as the normal equations guarantee, and the sum of
squared residuals is $2.9911$.

> [!info] Three checks on the same line
> **The closed form.** The standard formula
> $$b = \frac{n\sum xy - \sum x\sum y}{n\sum x^2 - \left(\sum x\right)^2} = \frac{7(119.5) - 28(24)}{7(140) - 28^2} = \frac{164.5}{196} = 0.839286$$
> reproduces $47/56$, so the elimination and the closed form agree.
>
> **The centroid.** A least-squares line passes through
> $(\bar x, \bar y) = (4, 3.4286)$: $0.0714 + 0.839286(4) = 3.4286$. A line
> that misses the centroid has had its two normal equations swapped, which is
> the commonest slip in this question.
>
> **Substitution.** $28(0.071429) + 140(0.839286) = 2 + 117.5 = 119.5$ and
> $7(0.071429) + 28(0.839286) = 0.5 + 23.5 = 24$. Both equations are
> reproduced exactly, which they should be, since they are what was solved.
>
> **And the residuals sum to zero**, which is not built into the working
> anywhere and so is a genuine test. In exact arithmetic they are
> $-23/56,\, 42/56,\, -33/56,\, 32/56,\, -43/56,\, 50/56,\, -25/56$, whose
> numerators sum to $-23+42-33+32-43+50-25 = 0$. A printed table of fitted
> values whose residuals do not sum to zero has a wrong entry somewhere, and
> this is a one-line test that finds it.

> [!note] Reading the fit
> The correlation coefficient is $r = 0.9318$, so $r^2 = 0.8683$ and about
> $87\%$ of the variation in $y$ is accounted for by the line. The residuals
> alternate in sign and are largest toward the middle of the range, which is the
> signature of genuine curvature in the data rather than of an arithmetic slip:
> a random-error fit would scatter residuals either side of zero without a
> pattern, whereas an alternating pattern of this regularity says the true
> relation bends above the line at both ends and below it in the middle. A
> quadratic through these seven points would fit better, and would be the right
> thing to fit if the question allowed it.

> cheapest check available on this question.

---

### [2018 Q.4(c)]

**Question.** The following data was taken from an experiment that measured the current in a wire for various imposed voltages. On the basis of a linier regression of this data, determine current for a voltage of $3.5\text{ V}$. Plot the line to evaluate the fit.

*[Marks: 05]*

**Solution.**

| $v$ (V) | 2 | 3 | 4 | 5 | 7 | 10 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| $i$ (A) | 5.2 | 7.8 | 10.7 | 13 | 19.3 | 27.5 |

**The method.** Fit $i = a + bv$ by least squares, meaning the line that
minimises the sum of squared vertical residuals. With $n = 6$ the quantities
you need are

$$\sum v = 31, \qquad \sum i = 83.5, \qquad \sum v^2 = 203, \qquad \sum vi = 551.7$$

**The normal equations.**

$$na + b\sum v = \sum i, \qquad a\sum v + b\sum v^2 = \sum vi$$

Solving, or equivalently using the closed forms,

$$b = \frac{n\sum vi - \sum v\sum i}{n\sum v^2 - \left(\sum v\right)^2} = \frac{6(551.7) - 31(83.5)}{6(203) - 31^2} = \frac{721.7}{257} = 2.8082\ \text{A/V}$$

$$a = \bar i - b\bar v = \frac{83.5}{6} - 2.8082\left(\frac{31}{6}\right) = 13.9167 - 14.5089 = -0.5922\ \text{A}$$

$$\boxed{i = -0.5922 + 2.8082\,v}$$

**The current at $3.5\ \text{V}$.**

$$i(3.5) = -0.5922 + 2.8082(3.5) = -0.5922 + 9.8287 = 9.2364$$

$$\boxed{i(3.5\ \text{V}) = 9.2364\ \text{A}}$$

**Plotting the fit, and reading the quality off the plot.** The six measured points $(v, i)$ and the fitted line $i = -0.5922 + 2.8082\,v$:

![Linear regression plot of current versus voltage with measured points, fitted line, and evaluated point at 3.5V](../answers_exam_style/diagrams/2018_Q4c_regression.png)

The measured values and residuals against the line are:

| $v$ | measured $i$ | fitted $i$ | residual |
| :--: | :-- | :-- | :-- |
| 2 | 5.2 | $5.0241$ | $+0.1759$ |
| 3 | 7.8 | $7.8323$ | $-0.0323$ |
| 4 | 10.7 | $10.6405$ | $+0.0595$ |
| 5 | 13 | $13.4486$ | $-0.4486$ |
| 7 | 19.3 | $19.0650$ | $+0.2350$ |
| 10 | 27.5 | $27.4895$ | $+0.0105$ |

The residuals are small beside the values themselves, the largest in magnitude
being $0.4486$ against $13$, so a straight line is a reasonable model for a
wire at constant temperature.

> [!info] Three checks, each catching a different error
> **Residuals sum to zero.** A least-squares fit is defined by setting the
> derivatives of the sum of squared residuals to zero, and the derivative with
> respect to $a$ is $\sum (f_i - y_i)$. So the residuals *must* sum to zero, to
> rounding. Here they sum to $0.1759 - 0.0323 + 0.0595 - 0.4486 + 0.2350 +
> 0.0105 = 0.0000$. If a printed table of fitted values does not give residuals
> summing to zero, a fitted value is wrong, and this is a one-line test that
> finds it.
>
> **The line passes through the centroid.** The normal equations also give
> $a + b\bar v = \bar i$, so the fitted line must pass through
> $(\bar v, \bar i) = (5.1667, 13.9167)$. Substituting:
> $-0.5922 + 2.8082(5.1667) = 13.9167$. A line that misses the centroid has had
> the two normal equations swapped, which is the single commonest slip in this
> question.
>
> **Internal interpolation.** The fitted values at $v = 3$ and $v = 4$ are
> $7.8323$ and $10.6405$, and interpolating between them at $v = 3.5$ returns
> their mean, $9.2364$, which is the value computed above. This confirms the
> answer is not an artefact of rounding $a$ and $b$ to four decimals.
>
> **And the single summary number.** The correlation coefficient is
> $r = 0.9996$, so $r^2 = 0.9991$ and over $99.9\%$ of the variation in current
> is accounted for by the line.

> [!note] On the wording
> The paper prints "linier", an evident typo for "linear". It is also worth
> noticing that the question asks for the *current* at a *voltage*, so voltage
> is the independent variable and current is being regressed on voltage. Fitting
> the other way round, $v$ on $i$, is a different computation and a different
> answer.

---

---

### [2019 Q.4(c)]

**Question.** Deduce the linear regression expression.

*[Marks: 02]*

**Solution.**

Let the data be $(x_i, y_i)$, $i = 1, \ldots, n$, and let the fitted line be

$$\hat y = a + bx$$

The residual at point $i$ is $r_i = y_i - a - bx_i$. Minimise the sum of squared
residuals:

$$S(a, b) = \sum_{i=1}^{n}\left(y_i - a - bx_i\right)^2$$

At a minimum, both partial derivatives vanish:

$$\frac{\partial S}{\partial a} = -2\sum_{i=1}^{n}\left(y_i - a - bx_i\right) = 0 \implies \sum y_i = na + b\sum x_i$$

$$\frac{\partial S}{\partial b} = -2\sum_{i=1}^{n}x_i\left(y_i - a - bx_i\right) = 0 \implies \sum x_i y_i = a\sum x_i + b\sum x_i^2$$

These are the **normal equations**. Solving the $2 \times 2$ system:

$$na + b\sum x_i = \sum y_i$$
$$a\sum x_i + b\sum x_i^2 = \sum x_i y_i$$

Eliminating $a$ from the first, $a = \bar y - b\bar x$, and substituting into the
second:

$$\sum x_i y_i = (\bar y - b\bar x)\sum x_i + b\sum x_i^2$$

Dividing through and collecting terms in $b$:

$$b = \frac{n\sum x_i y_i - \sum x_i \sum y_i}{n\sum x_i^2 - \left(\sum x_i\right)^2}, \qquad a = \bar y - b\bar x$$

$$\boxed{y = \left(\bar y - b\bar x\right) + bx \quad\text{with}\quad b = \frac{n\sum xy - \sum x \sum y}{n\sum x^2 - \left(\sum x\right)^2}}$$

> [!info] Check against the centroid condition
> The first normal equation rearranged gives $a + b\bar x = \bar y$, so the fitted
> line passes through the point $(\bar x, \bar y)$ whatever the data. The intercept
> formula $a = \bar y - b\bar x$ is exactly this condition solved for $a$, so the
> two forms are the same statement and the deduction is internally consistent.

> [!note] Why the intercept is written twice, and which form to use
> $a = \bar y - b\bar x$ is the form to reach for when checking, because it makes
> the centroid property explicit. The closed form for $b$ is the form to reach for
> when computing, because it avoids accumulating rounding through two
> substitutions.
>
> Using the closed form for $b$ and then $\bar y - b\bar x$ for $a$ is the standard
> practice and is numerically the safer combination, since $\bar y - b\bar x$ is a
> difference of two similar quantities only when $a$ happens to be small.

---

<a id="nm-43"></a><a id="nm-4.3"></a>
## NM-4.3 · Non-Linear Regression

### [2017 Q.5(b), 2020 Q.3(c)]

**Appeared in:** 2017 Q.5(b), 2020 Q.3(c)

**Question.** Determine the constants $a$ & $b$ by the method of least squares such that $y = a e^{bx}$ fits the following data.

*[Marks: 04]*

**Solution.**

| $x$ | 2 | 4 | 6 | 8 | 10 |
| :---: | :---: | :---: | :---: | :---: | :---: |
| $y$ | 4.077 | 11.084 | 30.128 | 81.897 | 222.62 |

**Step 1, linearise the model.** Taking logarithms of $y = ae^{bx}$,

$$\ln y = \ln a + bx$$

so the data become a straight line $Y = A + bx$ with $Y = \ln y$ and
$A = \ln a$. Then $a = e^A$.

**This is the step that makes the problem solvable at all.** The model is
*nonlinear* in $(a, b)$ and linear in $(\ln a, b)$, so ordinary least squares
cannot be applied directly, but the transformed problem is a straight-line fit
with a closed-form solution. The cost of the transformation is that it minimises
the error in $\ln y$, not in $y$, so the fit is a maximum-likelihood fit for
*relative* error and a slightly different estimator for absolute error. That is
acceptable here and is the standard textbook treatment, but it is a real
approximation and worth naming.

**Step 2, the transformed data.**

| $x$ | $y$ | $Y = \ln y$ |
| :--: | :-- | :-- |
| 2 | 4.077 | $1.405361$ |
| 4 | 11.084 | $2.405503$ |
| 6 | 30.128 | $3.405455$ |
| 8 | 81.897 | $4.405462$ |
| 10 | 222.62 | $5.405466$ |

**Step 3, least squares on the transformed line.** With $n = 5$,

$$\sum x = 30, \qquad \sum Y = 17.027248, \qquad \sum xY = 122.163825, \qquad \sum x^2 = 220$$

$$b = \frac{n\sum xY - \sum x\sum Y}{n\sum x^2 - \left(\sum x\right)^2} = \frac{5(122.163825) - 30(17.027248)}{5(220) - 900} = \frac{610.819124 - 510.817430}{200}$$

$$b = \frac{100.001694}{200} = 0.50001$$

$$\ln a = \bar Y - b\bar x = 3.405450 - 3.000052 = 0.405398$$

$$a = e^{0.405398} = 1.4999$$

**Step 4, the ratio route, which needs no arithmetic beyond division.** Each time
$x$ increases by $2$, $y$ should be multiplied by a constant. The tabulated
quotients are

$$\frac{222.62}{81.897} = 2.7183, \quad \frac{81.897}{30.128} = 2.7183, \quad \frac{30.128}{11.084} = 2.7182, \quad \frac{11.084}{4.077} = 2.7187$$

and $e = 2.71828$. So $e^{2b} = e$, giving

$$2b = 1 \implies b = 0.5$$

$$a = y(x)e^{-bx} = 4.077e^{-1} = 1.4998$$

**Step 5, the fitted constants.** The two routes agree to four significant
figures: least squares gives $b = 0.50001$ and $a = 1.4999$, the ratio route
gives $b = 0.5$ and $a = 1.4998$. Taking the values the data were generated
from,

$$\boxed{a = 1.50, \qquad b = 0.5}$$

**The fit.**

| $x$ | $y$ given | $y$ fitted $= 1.5e^{0.5x}$ |
| :--: | :-- | :-- |
| 2 | 4.077 | 4.077 |
| 4 | 11.084 | 11.084 |
| 6 | 30.128 | 30.128 |
| 8 | 81.897 | 81.897 |
| 10 | 222.620 | 222.620 |

> [!info] Two checks, one on each route
> **The correlation coefficient** of $\ln y$ against $x$ is
> $r = 0.9999999996$, so the exponential model fits the transformed data
> essentially perfectly. Any other model, a power law or a polynomial in
> $x$, would be visibly worse on the same table.
>
> **The residuals** of $y$ itself are $-0.0004, +0.0004, -0.0003, -0.0002$ and
> $+0.0003$, all of order $10^{-4}$. That is the rounding of the published $y$
> values to three decimals, not the error of the model: the table was generated
> from $1.5e^{0.5x}$ and then printed to three places. So the two routes
> agreeing, together with residuals at the printing precision, rules out both a
> transcription slip in the logarithms and a genuine model misfit.

> [!note] Why the logarithm is legitimate here, and where it stops working
> It works because the model is a *pure* exponential with a single power on each
> variable. The moment a model has an offset, as in $y = a e^{bx} + c$, taking
> logarithms no longer linearises it, the correct method becomes non-linear least
> squares, and there is no closed-form normal-equation solution to write down.
> It also stops being legitimate when $y$ can be zero or negative, since
> $\ln y$ does not exist. Both restrictions are worth checking for before
> reaching for a log.

---

### [2022 Q.2(b)]

**Question.** Using the method of least squares, fit a curve of the form $y = \frac{x}{a + bx}$ to fit the following data $(3, 7.148)$, $(5, 10.231)$, $(8, 13.509)$, $(12, 16.434)$.

*[Marks: 03, CO: 1]*

**Solution.**

**Step 1. Linearise.** The model is not of the form $y = a + bx$, so least
squares cannot be applied directly. Take reciprocals of both sides:

$$
\frac{1}{y} = \frac{a + bx}{x} = \frac{a}{x} + b = a\left(\frac{1}{x}\right) + b
$$

That is the standard form $v = au + b$ with $u = \frac{1}{x}$ and
$v = \frac{1}{y}$.

> [!warning] The slope is $a$ and the intercept is $b$, which is the reverse of usual
> In $y = mx + c$ the slope $m$ multiplies the variable and the intercept $c$ is
> the constant. Here the linearised form is $v = a\,u + b$, so the coefficient
> multiplying $u = \frac{1}{x}$ is **$a$**, and the constant is **$b$**.
>
> That happens because in the original model $a$ is the constant term of
> $a + bx$ while $b$ multiplies $x$, and the transformation moves $a$ into the
> slope position. Reading the roles off $a + bx$ instead of off
> $v = au + b$ swaps them.

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

**Step 4. Normal equations.** Sum $v = au + b$ over the four points, and sum
$uv = au^2 + bu$:

$$
\begin{cases}
n\,b + a\sum u = \sum v \\
\left(\sum u\right)b + a\sum u^2 = \sum uv
\end{cases}
$$

Note which coefficient multiplies which sum: **the slope $a$** multiplies
$\sum u$ and $\sum u^2$, while **the intercept $b$** multiplies $n$ and
$\sum u$. Writing $4a + 0.741667b = 0.372516$ puts them the wrong way round, and
it is the single most common error in this question.

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

$$\boxed{y = \frac{x}{0.3162 + 0.0345x}}$$

**Check the fitted values**, using the unrounded $a = 0.31619988$ and
$b = 0.03450017$ whose four-decimal forms are the boxed ones:

| $x$ | $y$ actual | $\hat{y}$ | $y - \hat{y}$ |
| --: | --: | --: | --: |
| 3 | 7.148 | 7.147956 | $+0.000044$ |
| 5 | 10.231 | 10.231210 | $-0.000210$ |
| 8 | 13.509 | 13.508920 | $+0.000080$ |
| 12 | 16.434 | 16.433809 | $+0.000191$ |

Every residual is below $2.2 \times 10^{-4}$, so the fit is essentially exact.

> [!warning] Substituting back exposes a swapped $a$ and $b$ immediately
> Swap them, giving $a = 0.034500$ and $b = 0.316200$, and then
> $$\hat{y}(3) = \frac{3}{0.0345 + 0.3162(3)} = \frac{3}{0.9831} = 3.0516$$
> against an actual $7.148$. The residuals $y - \hat{y}$ become $+4.10$, $+7.14$,
> $+10.39$ and $+13.30$. Nothing about that is small, so one substitution
> settles it.
>
> **Substituting back is the general safeguard for any linearised fit.** A
> wrong linearisation usually still produces tidy coefficients, and the
> coefficients alone will not tell you. Residuals will.

> [!info] How to know the chosen form is the right one
> If $v$ really is linear in $u$, the slope between consecutive transformed
> points must be constant. They come out $0.31618$, $0.31623$, $0.31621$, which
> agree to four figures and confirm both that the model form is correct and that
> the data were generated from it. A linearity test like this is worth running
> before solving, because it validates the model and not merely the arithmetic.

> [!note] Why a hyperbola is fitted this way, and the one thing to watch
> The substitution $u = 1/x$ turns the model into a straight line, which is why
> least squares applies. Both coefficients come out positive here, so $a + bx$
> never passes through zero over the data range and the fitted curve has no pole
> inside it.
>
> If $a + bx$ did cross zero within the data range, the fitted curve would have a
> vertical asymptote sitting among the measurements, and the answer would be
> meaningless over that stretch. This is the standard reason a hyperbola is only
> fitted over an interval that avoids its pole.

---

<a id="nm-44"></a><a id="nm-4.4"></a>
## NM-4.4 · Regression Criteria & Theory

### [2017 Q.6(a)]

**Question.** With necessary figure(s) explain why minimum sum of error, minimum sum of absolute error and minimum error are ill-suited for regression. Which criterion is best suited for regression?

*[Marks: 04]*

**Solution.**

Take four data points, three of which lie near the line and one of which is a
spuriously displaced measurement.

```text
 y
 ^         .          .
 |      .        .          o <- (x4, y4) outlier
 |   .            .
 |  .         .            <- the true relation
 | .      .
 |________________________> x
```

**Criterion 1: minimum sum of errors, $\sum e_i = 0$.** The positive and
negative errors cancel, so this condition is satisfied by *infinitely many*
curves, including curves that pass through none of the data. A line far above
three points and far below a fourth gives $\sum e_i = 0$ while fitting nothing.

```text
   .            .
        sum e = +2
   .
        sum e = -2      -> total 0, but a terrible fit
```

**Criterion 2: minimum sum of absolute errors, $\sum\lvert e_i\rvert$.**
Cancellation is removed, so the criterion is a genuine measure of badness.
However $\sum\lvert e_i\rvert$ is piecewise linear in the curve's parameters,
its minimum often lies where the slope is not defined, and no normal equations
result. The condition is satisfied by several distinct curves whenever they
share the same total absolute deviation.

```text
   .            .
        |e| = 2
   .
        |e| = 2      -> total 4, minimum, but not unique
```

**Criterion 3: minimum error, $\min_i \lvert e_i\rvert$.** A single error
considers one point only. Minimising it drives one residual to zero while the
others are ignored entirely, which is worse still: it fits the *outlier*
perfectly if the outlier is the smallest residual.

**The criterion that is best suited.** The **least-squares criterion**,
minimising the sum of squared errors,

$$\boxed{S = \sum_{i=1}^{n}\left(y_i - f(x_i)\right)^2 \text{ is the criterion to minimise}}$$

Its three properties make it the standard.

1. **No cancellation**, since the square is always non-negative.
2. **A unique, smooth minimum**, and the normal equations
   $\partial S/\partial a_j = 0$ are *linear* in the parameters, so they have a
   closed-form solution.
3. **A probabilistic justification**: if the measurement errors are independent
   and normally distributed with equal variance, the least-squares fit is the
   maximum-likelihood estimate.

> [!note] Why property 3 is the deepest of the three
> Properties 1 and 2 make least squares *convenient*. Property 3 makes it
> *right*. Nothing forces a curve-fitter to minimise $\sum e_i^2$; it is simply
> that when the errors are independent Gaussian samples with a common variance,
> that is the curve the data are most likely to have come from. The other two
> criteria correspond to error models where one datum outweighs all the others
> by an unbounded factor, which is a strange thing to believe about a
> voltmeter.

---

---

**Also asked here.**

- *2019 Q.4(a)* is the same question as [[NM-4.1_Concepts|NM-4.1]], which is written in `NM-4.1`.

---

<a id="nm-45"></a><a id="nm-4.5"></a>
## NM-4.5 · Linear Interpolation

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

<a id="nm-46"></a><a id="nm-4.6"></a>
## NM-4.6 · Lagrange's Interpolation

### [2018 Q.3(a)]

**Question.** Explain the use of Lagrange's interpolation formula.

*[Marks: 02]*

**Solution.**

**The use.** Given a tabulated set $(x_i, f_i)$, estimate $f(x)$ at a point $x$
lying inside the range of the table, without assuming the abscissae are equally
spaced.

**The formula.** For $n+1$ points,

$$f(x) \approx \sum_{i=0}^{n} f_i \prod_{\substack{j=0 \\ j \ne i}}^{n}\frac{x - x_j}{x_i - x_j}$$

**Four reasons it is used.**

1. **Unequal spacing is allowed.** This is the principal advantage over
   Newton's forward and backward formulas, which both need a common tabular
   spacing $h$. Experimental data with a varying interval can be used directly.
2. **The tabulated order is irrelevant.** The formula is symmetric in the
   points; permuting them leaves the result unchanged. Worth knowing when a
   printed table lists its entries out of order.
3. **One expression gives the value.** The whole formula is written once and
   evaluated at any $x$ in range, with no successive-difference table to build.
4. **The error is available.** With $n+1$ points,
   $R_n = \dfrac{f^{(n+1)}(\xi)}{(n+1)!}\prod_{i=0}^{n}(x - x_i)$, so the
   accuracy of a chosen set can be judged before any arithmetic is done.

**Limitations.** Adding a point means recomputing every coefficient, unlike
Newton's divided-difference form where earlier work is retained. And it is
inefficient for repeated evaluation at many points, where writing the single
interpolating polynomial out once and evaluating it is cheaper.

> [!note] Newton's form and Lagrange's form are the same polynomial
> They differ only in organisation. If you have a regular table, build the
> divided-difference table and use Newton's form. If the spacing is irregular
> or you have only the points to hand, write Lagrange's directly. Never build
> Newton's *forward* formula on an irregular table, because $h$ does not exist.

---

### [2018 Q.3(c)]

**Question.** Find $f(2.5)$ from the given data, $x$: 1, 2, 3 and $f(x)$: 0, 1, 8.

*[Marks: 04]*

**Solution.**

| $x$ | 1 | 2 | 3 |
| :---: | :---: | :---: | :---: |
| $f(x)$ | 0 | 1 | 8 |

**The method.** Three points, so a quadratic, so Lagrange's formula. Here the
spacing *is* uniform, but Lagrange is still the shortest route because there is
no difference table to build and only three basis polynomials to evaluate.

$$f(x) = \frac{(x - x_1)(x - x_2)}{(x_0 - x_1)(x_0 - x_2)}f_0 + \frac{(x - x_0)(x - x_2)}{(x_1 - x_0)(x_1 - x_2)}f_1 + \frac{(x - x_0)(x - x_1)}{(x_2 - x_0)(x_2 - x_1)}f_2$$

**Evaluate each basis polynomial at $x = 2.5$.**

$$L_0 = \frac{(2.5 - 2)(2.5 - 3)}{(1 - 2)(1 - 3)} = \frac{(0.5)(-0.5)}{(-1)(-2)} = -0.125$$

$$L_1 = \frac{(2.5 - 1)(2.5 - 3)}{(2 - 1)(2 - 3)} = \frac{(1.5)(-0.5)}{(1)(-1)} = 0.75$$

$$L_2 = \frac{(2.5 - 1)(2.5 - 2)}{(3 - 1)(3 - 2)} = \frac{(1.5)(0.5)}{(2)(1)} = 0.375$$

$$f(2.5) = 0(-0.125) + 1(0.75) + 8(0.375) = 0 + 0.75 + 3.0$$

$$\boxed{f(2.5) = 3.75}$$

> [!info] Two checks that catch different mistakes
> **Partition of unity.** $-0.125 + 0.75 + 0.375 = 1$ exactly. The Lagrange
> basis polynomials of degree $n$ must sum to the constant $1$ at every $x$,
> because they are interpolating the function $y = 1$. If your three numbers do
> not sum to $1$, at least one of them was miscomputed, and you can find which by
> checking them one at a time.
>
> **The polynomial itself.** Newton's divided differences give
> $f[x_0,x_1] = 1$, $f[x_1,x_2] = 7$ and $f[x_0,x_1,x_2] = \dfrac{7 - 1}{3 - 1} = 3$, so
> $f(x) = 0 + 1(x - 1) + 3(x-1)(x-2) = 3x^2 - 8x + 5$. At $x = 2.5$:
> $3(6.25) - 8(2.5) + 5 = 18.75 - 20 + 5 = 3.75$. And the polynomial
> reproduces the table: $f(1) = 0$, $f(2) = 1$, $f(3) = 8$. Note that the
> divided-difference route is *also* a check on the answer, not merely a
> restatement: it uses the data through a completely different arrangement of
> the arithmetic.

---

### [2019 Q.4(b)]

**Question.** A robot arm with a rapid laser scanner is doing a quick quality check on holes drilled in a $15'' \times 10''$ rectangular plate. The centers of the holes in the plate describe the path the arm needs to take, and the hole centers are located on a Cartesian coordinate system (with the origin at the bottom left corner of the plate) given by the specifications in the table below. If the leaser is traversing from $x = 2$ to $x = 4.25$ to $x = 5.25$ in a quadratic path, what is the value of the $y$ at $x = 4.00$ using a curve fitting technique.

*[Marks: 06]*

**Solution.**

| $x$ (in.) | 2 | 4.25 | 5.25 |
| --: | --: | --: | --: |
| $y$ (in.) | 7.2 | 7.1 | 6.0 |

The three tabulated points through which the quadratic path passes are

$$(x_0, y_0) = (2, 7.2), \qquad (x_1, y_1) = (4.25, 7.1), \qquad (x_2, y_2) = (5.25, 6.0)$$

Three points determine one quadratic, so the curve-fitting technique is **exact
interpolation** by a second-degree Lagrange polynomial. The rest of the table,
$(7.81, 5.0), (9.20, 3.5), (10.60, 5.0)$, is not part of the specified path.

**Lagrange basis.** With $x = 4.00$:

$$L_0 = \frac{(x - x_1)(x - x_2)}{(x_0 - x_1)(x_0 - x_2)} = \frac{(4 - 4.25)(4 - 5.25)}{(2 - 4.25)(2 - 5.25)} = \frac{(-0.25)(-1.25)}{(-2.25)(-3.25)}$$

$$L_0 = \frac{0.3125}{7.3125} = 0.04273504$$

$$L_1 = \frac{(x - x_0)(x - x_2)}{(x_1 - x_0)(x_1 - x_2)} = \frac{(4 - 2)(4 - 5.25)}{(4.25 - 2)(4.25 - 5.25)} = \frac{(2)(-1.25)}{(2.25)(-1)}$$

$$L_1 = \frac{-2.5}{-2.25} = 1.11111111$$

$$L_2 = \frac{(x - x_0)(x - x_1)}{(x_2 - x_0)(x_2 - x_1)} = \frac{(4 - 2)(4 - 4.25)}{(5.25 - 2)(5.25 - 4.25)} = \frac{(2)(-0.25)}{(3.25)(1)}$$

$$L_2 = \frac{-0.5}{3.25} = -0.15384615$$

**Evaluate the polynomial.**

$$y(4) = y_0 L_0 + y_1 L_1 + y_2 L_2 = 7.2(0.04273504) + 7.1(1.11111111) + 6.0(-0.15384615)$$

$$y(4) = 0.30769231 + 7.88888889 - 0.92307692 = 7.27350427$$

$$\boxed{y(4.00) = 7.2735\ \text{in.}}$$

> [!warning] A weight greater than one is normal, and $L_1 = 1.111$ looks wrong until it is checked
> Lagrange weights are not a partition of unity in value. $L_1 > 1$ and
> $L_2 < 0$ together are exactly what an **extrapolation-free but off-node**
> evaluation produces: the target $4.00$ is between $x_0 = 2$ and $x_1 = 4.25$,
> close to $x_1$, so its weight is large and the neighbouring weight compensates
> negatively.
>
> The check is not "all weights in $[0,1]$". The check is that the weights **sum
> to 1**, which they do:
> $0.04273504 + 1.11111111 - 0.15384615 = 1$ exactly. That identity holds at any $x$,
> because interpolating the constant function $1$ must return $1$.

> [!info] Check against the fitted polynomial in ordinary form
> Solving for $a, b, c$ in $y = a + bx + cx^2$ through the three points gives
> $c = -\dfrac{38}{117}$, $b = \dfrac{2323}{1170}$, $a = \dfrac{883}{195}$, so
> $y = -\dfrac{38x^2}{117} + \dfrac{2323x}{1170} + \dfrac{883}{195}$.
> Substituting $x = 4$ gives $-\dfrac{608}{117} + \dfrac{9292}{1170} + \dfrac{883}{195} = \dfrac{8510}{1170} = \dfrac{851}{117} = 7.27350427$, the
> same value. An exact fraction and a decimal evaluation agreeing to eight digits
> rules out a rounding loss in the Lagrange arithmetic.

---

### [2021 Q.3(b)]

**Question.** Differentiate between Newton's interpolation and Lagrange's interpolation.

*[Marks: 02, CO: 2]*

**Solution.**

| | Newton's interpolation | Lagrange's interpolation |
| :-- | :-- | :-- |
| Form | **Successive approximation**, applied one point at a time | **Single polynomial**, all points at once |
| Basis | Divided differences or forward/backward differences | Products $\prod_{j\neq i}\frac{x-x_j}{x_i-x_j}$ |
| Adding a new point | Old result is **retained**; only a new term is added | Whole polynomial must be **rebuilt** |
| Equally spaced points | Forward/backward difference form is fastest | Works but ignores the equal spacing |
| Unequal spacing | Needs **divided** differences | Natural, no change needed |
| Cost per evaluation | $O(n)$ after setup | $O(n^2)$ directly, $O(n)$ with Neville |
| Near the table ends | Forward at the start, backward at the end | One formula for everywhere |
| Numerical stability | Better with the Neville form | Degrades with many points |

$$\boxed{\text{Newton updates and reuses; Lagrange rebuilds once and is spacing-agnostic}}$$

> [!note] The one distinction worth remembering
> Newton gives an **update** rule, cheap when data arrive incrementally. Lagrange
> gives a **construction**, direct, and equally spaced points require no special
> case.
>
> That is the whole difference in one sentence. Everything else in the table is a
> consequence of it: the update is why Newton is cheap to extend, and the direct
> construction is why Lagrange needs no difference table at all.
>
> In practice Newton's divided difference form is almost always what you compute,
> because it is both cheaper and better conditioned. Lagrange earns its place in
> an exam because it is the form with an obvious closed expression for the
> error term.

---

### [2021 Q.3(d), 2023 Q.2(b)]

**Appeared in:** 2021 Q.3(d), 2023 Q.2(b)

**Question.** Find $y(2)$ from the following data using Lagrange's formula.

*[Marks: 04, CO: 2]*

**Solution.**

| $x$ | 0 | 1 | 3 | 4 | 5 |
| --- | --: | --: | --: | --: | --: |
| $y$ | 0 | 1 | 81 | 256 | 625 |

**Step 1. The formula.** With five points $x_0 = 0, x_1 = 1, x_2 = 3, x_3 = 4,
x_4 = 5$,

$$
y(2) = \sum_{i=0}^{4} y_i L_i(2), \qquad L_i(2) = \prod_{j \neq i} \frac{2 - x_j}{x_i - x_j}
$$

**Step 2. Compute each weight**, keeping numerator and denominator factors
separate.

$$
L_0(2) = \frac{(2-1)(2-3)(2-4)(2-5)}{(0-1)(0-3)(0-4)(0-5)} = \frac{(1)(-1)(-2)(-3)}{(-1)(-3)(-4)(-5)} = \frac{-6}{60} = -\frac{1}{10}
$$

$$
L_1(2) = \frac{(2-0)(2-3)(2-4)(2-5)}{(1-0)(1-3)(1-4)(1-5)} = \frac{(2)(-1)(-2)(-3)}{(1)(-2)(-3)(-4)} = \frac{-12}{-24} = \frac{1}{2}
$$

$$
L_2(2) = \frac{(2-0)(2-1)(2-4)(2-5)}{(3-0)(3-1)(3-4)(3-5)} = \frac{(2)(1)(-2)(-3)}{(3)(2)(-1)(-2)} = \frac{12}{12} = 1
$$

$$
L_3(2) = \frac{(2-0)(2-1)(2-3)(2-5)}{(4-0)(4-1)(4-3)(4-5)} = \frac{(2)(1)(-1)(-3)}{(4)(3)(1)(-1)} = \frac{6}{-12} = -\frac{1}{2}
$$

$$
L_4(2) = \frac{(2-0)(2-1)(2-3)(2-4)}{(5-0)(5-1)(5-3)(5-4)} = \frac{(2)(1)(-1)(-2)}{(5)(4)(2)(1)} = \frac{4}{40} = \frac{1}{10}
$$

**Check.** The weights sum to 1:
$-\frac{1}{10} + \frac{1}{2} + 1 - \frac{1}{2} + \frac{1}{10} = 1$ ✓

This holds at **any** $x$, not only at a node, because interpolating the constant
function $1$ with a degree 4 polynomial must return $1$.

**Step 3. Assemble.**

$$
\begin{aligned}
y(2) &= (0)\left(-\tfrac{1}{10}\right) + (1)\left(\tfrac{1}{2}\right) + (81)(1) + (256)\left(-\tfrac{1}{2}\right) + (625)\left(\tfrac{1}{10}\right) \\
     &= 0 + 0.5 + 81 - 128 + 62.5 \\
     &= 16
\end{aligned}
$$

$$\boxed{y(2) = 16}$$

> [!info] Check by two independent routes
> **Route 2, Newton's divided difference.** The nodes are **not** equally spaced,
> so divided differences apply. The table is
>
> | Order | Values |
> | :-- | :-- |
> | $f[x_i]$ | 0, 1, 81, 256, 625 |
> | $1^{st}$ | 1, 40, 175, 369 |
> | $2^{nd}$ | 13, 45, 97 |
> | $3^{rd}$ | 8, 13 |
> | $4^{th}$ | 1 |
>
> Spot check: $f[x_1,x_2,x_3] = \frac{f[x_2,x_3] - f[x_1,x_2]}{x_3 - x_1} = \frac{175-40}{4-1} = 45$.
> The leading diagonal is $0, 1, 13, 8, 1$, and evaluating that polynomial at
> $x = 2$ gives **16**.
>
> **Route 3, recognise the data.** $0^4 = 0$, $1^4 = 1$, $3^4 = 81$,
> $4^4 = 256$, $5^4 = 625$. All five points lie on $y = x^4$ exactly, so
> $y(2) = 2^4 = 16$.

> [!warning] The weights are the whole calculation
> Each $L_i$ has four numerator and four denominator factors, since $j$ runs over
> the four indices other than $i$. A weight with three factors is wrong by
> construction. The two most often mis-signed are $L_0(2)$ and $L_1(2)$, whose
> denominators are $+60$ and $-24$.
>
> The sum-to-1 check above catches both of those and any other sign slip, for one
> line of work. Run it every time; it costs nothing and it is the only check
> available before the final assembly.

> [!note] Recognising the data beats computing them
> Route 3 is not a party trick. When the $y$ values look like familiar powers,
> identifying the generating function turns a twenty-line Lagrange sum into a
> single multiplication, and it also **validates** the table.
>
> If the data are $x^4$ then any interpolant must be $x^4$ exactly, since a
> degree 4 polynomial through five points on a quartic is that quartic. A computed
> answer that disagreed with $2^4 = 16$ would mean an arithmetic slip, not a
> modelling insight.

---

### [2024 Q.2(c)]

**Question.** Describe the Lagrange interpolation method. What are its advantages and disadvantages?

*[Marks: 03, CO: 1]*

**Solution.**

**The method.** Given $n+1$ points $(x_i, y_i)$, the unique polynomial of
degree at most $n$ through them is

$$\boxed{P_n(x) = \sum_{i=0}^{n} y_i \prod_{j \neq i} \frac{x - x_j}{x_i - x_j}}$$

Each $y_i$ is multiplied by a **basis polynomial** $L_i(x)$ that equals $1$ at
$x = x_i$ and $0$ at every other tabulated $x_j$. That construction is what
guarantees the interpolant passes through every point: at $x = x_k$, every term
except the $k$-th vanishes.

**The error.** With $n+1$ points,

$$f(x) - P_n(x) = \frac{f^{(n+1)}(\xi)}{(n+1)!}\prod_{i=0}^{n}(x - x_i)$$

for some $\xi$ in the interval. The product is zero at every node, so the error
is zero there, and it grows between nodes. This is why interpolation error is
not uniformly distributed across the interval.

**Advantages.**

1. **Equal spacing is not required.** This is the decisive advantage over
   Newton's formulas, which assume a constant tabular spacing $h$. Experimental
   data with irregular spacing are handled directly.
2. **The order of the points is irrelevant.** The formula is symmetric in the
   nodes, so a table printed with its entries out of order gives the same
   polynomial. This is useful when a printed table is disordered.
3. **The formula is written once.** A single expression evaluates at any $x$ in
   range, with no difference table to construct, and it is convenient for
   hand checking.

**Disadvantages.**

1. **Adding a point costs everything.** Every basis polynomial changes, so a new
   point forces a complete recomputation. Newton's divided-difference form keeps
   its earlier work, so appending a point costs one new column.
2. **It is inefficient for repeated evaluation.** Evaluating the product for
   every new $x$ costs $O(n^2)$ multiplications, whereas converting to power
   form once costs $O(n^2)$ and then gives $O(n)$ per evaluation.
3. **It cannot show the trend.** The formula gives a value, not a model. Fitting
   a line and reporting the slope is a different task, and interpolation does not
   answer it.

**When to use it.** Lagrangian interpolation is the right choice when the data
are exact, unevenly spaced, and evaluated at few points. For many points, or
when a model of the trend is wanted, use fitting instead.

---

---

**Also asked here.**

- *2022 Q.1(c)* is the same question as [[NM-4.1_Concepts|NM-4.1]], which is written in `NM-4.1`.
- *2022 Q.2(a)* is the same question as [[NM-4.9_Newtons_Divided_Difference_and_General_Interpolation|NM-4.9]], which is written in `NM-4.9`.

---

**Answered in phase P6, in `../CT_Questions/`.**

- *CT-02A Q.1* is a class-test question. Its answer is in `../CT_Questions/CT_answers_exam_style.md`, with the reasoning in `../CT_Questions/CT_answers_explanation.md`.

---

<a id="nm-47"></a><a id="nm-4.7"></a>
## NM-4.7 · Newton's Forward Difference

### [2020 Q.5(a)]

**Question.** Deduce the Newton's forward difference interpolating polynomial.

*[Marks: 06]*

**Solution.**

**Set up.** For $n+1$ equally spaced points with common difference $h$, write
$x = x_0 + ph$ so that $p = \frac{x - x_0}{h}$. The forward difference operator is
$\Delta y_0 = y_1 - y_0$.

**Step 1. Taylor expansion about $x_0$.**

$$
y(x) = y_0 + p\,h\,y'(x_0) + \frac{p^2}{2!}h^2 y''(x_0) + \frac{p^3}{3!}h^3 y'''(x_0) + \cdots
$$

**Step 2. Express the derivatives through differences.** For a polynomial sampled at
spacing $h$, the $k$-th derivative at $x_0$ satisfies

$$
y^{(k)}(x_0) = \frac{\Delta^k y_0}{h^k}
$$

because each forward difference lowers the degree of the underlying polynomial by
one and contributes a factor of $h$.

**Step 3. Substitute.** The factors of $h$ cancel term by term:

$$
y(x) = y_0 + p\,\Delta y_0 + \frac{p^2}{2!}\Delta^2 y_0 + \frac{p^3}{3!}\Delta^3 y_0 + \cdots
$$

**Step 4. Replace the rising powers by falling products.** This is the step that
produces the standard form. The identity needed is

$$
p^k = \sum_{j=0}^{k} s(k, j)\,p(p-1)(p-2)\cdots(p-j+1)
$$

where $s(k,j)$ is a Stirling number of the second kind, and the empty product for
$j = 0$ equals $1$. Equivalently, shifting the index,
$p^k = \sum_{j=0}^{k-1} s(k, j+1)\,p(p-1)\cdots(p-j)$. Spot check at $k = 2$:
$1\cdot p + 1\cdot p(p-1) = p^2$.

More directly, Newton's interpolation polynomial for a node set is

$$
P(x) = f[x_0] + f[x_0,x_1](x-x_0) + f[x_0,x_1,x_2](x-x_0)(x-x_1) + \cdots
$$

where $f[x_0,x_1,\dots,x_k] = \frac{\Delta^k y_0}{k!\,h^k}$ for equally spaced
points. Substituting $x - x_i = (p-i)h$ and cancelling $h^k$:

$$
P(x) = y_0 + \frac{\Delta y_0}{1!h}\,(p)h + \frac{\Delta^2 y_0}{2!h^2}\,p(p-1)h^2 + \frac{\Delta^3 y_0}{3!h^3}\,p(p-1)(p-2)h^3 + \cdots
$$

**Step 5. The result.**

$$
y_n(x) = y_0 + p\Delta y_0 + \frac{p(p-1)}{2!}\Delta^2 y_0 + \frac{p(p-1)(p-2)}{3!}\Delta^3 y_0 + \cdots + \frac{p(p-1)\cdots(p-n+1)}{n!}\Delta^n y_0
$$

> [!note] Why step 4 is not a trick
> The Taylor form has rising powers $p^2, p^3$; the Newton form has falling products
> $p(p-1)$, $p(p-1)(p-2)$. The substitution is not cosmetic.
>
> The finite differences already carry the effect of the lower-order terms, and
> replacing rising powers by falling products is what avoids double counting. A
> derivation that stops at step 3 has a formula that is correct and useless,
> because no one builds a difference table and then has to raise $p$ to a power
> for each row.

**Validity.** Accurate for $0 \le p \le n$, that is inside the table. Near the far
end use backward differences instead, and outside the table the result is an
extrapolation with the risks listed in Q.3(a). Part (b) applies this to unequally
spaced data, where divided differences are used instead.

> [!note] Where this is used again
> The forward form is applied in 2021 Q.4(b) and 2021 Q.4(c), and the backward
> form in Q.3(b) above. See [[NM-4.7_Newtons_Forward_Difference|NM-4.7 · Newton's Forward Difference]].

---

### [2021 Q.3(c), 2023 Q.2(a)]

**Appeared in:** 2021 Q.3(c), 2023 Q.2(a)

**Question.** Derive the Newton's forward interpolation formula: $y_n(x) = y_0 + p\Delta y_0 + \frac{p(p-1)}{2!}\Delta^2 y_0 + \frac{p(p-1)(p-2)}{3!}\Delta^3 y_0 + \cdots$

*[Marks: 04, CO: 2]*

**Solution.**

**Set up.** Let the function $y = f(x)$ take values $y_0, y_1, y_2, \dots, y_n$ at $n+1$ equidistant points $x_0, x_1, x_2, \dots, x_n$ with constant step size $h$, such that $x_i = x_0 + ih$.

Assume the interpolating polynomial $P_n(x)$ of degree $n$ in the form:

$$
P_n(x) = a_0 + a_1(x - x_0) + a_2(x - x_0)(x - x_1) + a_3(x - x_0)(x - x_1)(x - x_2) + \cdots + a_n(x - x_0)(x - x_1)\cdots(x - x_{n-1})
$$

**Step 1. Determine the coefficients $a_0, a_1, a_2, \dots$ successively.**

- At $x = x_0$:
  $$y_0 = P_n(x_0) = a_0 \implies a_0 = y_0$$

- At $x = x_1 = x_0 + h$:
  $$y_1 = P_n(x_1) = a_0 + a_1(x_1 - x_0) = y_0 + a_1 h$$
  $$a_1 = \frac{y_1 - y_0}{h} = \frac{\Delta y_0}{1!\,h}$$

- At $x = x_2 = x_0 + 2h$:
  $$y_2 = P_n(x_2) = a_0 + a_1(x_2 - x_0) + a_2(x_2 - x_0)(x_2 - x_1) = y_0 + a_1(2h) + a_2(2h)(h)$$
  $$y_2 = y_0 + 2\Delta y_0 + 2h^2 a_2$$
  Since $\Delta^2 y_0 = y_2 - 2y_1 + y_0 = y_2 - 2(y_0 + \Delta y_0) + y_0 = y_2 - y_0 - 2\Delta y_0$:
  $$2h^2 a_2 = \Delta^2 y_0 \implies a_2 = \frac{\Delta^2 y_0}{2!\,h^2}$$

- By induction, the general coefficient is:
  $$a_k = \frac{\Delta^k y_0}{k!\,h^k}, \qquad k = 0, 1, 2, \dots, n$$

**Step 2. Express in terms of the dimensionless variable $p$.**

Let $x = x_0 + ph$, so that $p = \frac{x - x_0}{h}$. Then:
$$x - x_0 = ph$$
$$x - x_1 = x_0 + ph - (x_0 + h) = (p - 1)h$$
$$x - x_2 = (p - 2)h, \quad \dots, \quad x - x_{k-1} = (p - k + 1)h$$

The product of factors becomes:
$$(x - x_0)(x - x_1)\cdots(x - x_{k-1}) = (ph)((p-1)h)\cdots((p-k+1)h) = p(p-1)\cdots(p-k+1)\,h^k$$

**Step 3. Substitute $a_k$ and product factors into $P_n(x)$.**

$$a_k (x - x_0)(x - x_1)\cdots(x - x_{k-1}) = \frac{\Delta^k y_0}{k!\,h^k} \cdot p(p-1)\cdots(p-k+1)\,h^k = \frac{p(p-1)\cdots(p-k+1)}{k!}\Delta^k y_0$$

Cancelling $h^k$ term by term yields Newton's forward interpolation formula:

$$\boxed{y_n(x) = y_0 + p\Delta y_0 + \frac{p(p-1)}{2!}\Delta^2 y_0 + \frac{p(p-1)(p-2)}{3!}\Delta^3 y_0 + \cdots + \frac{p(p-1)\cdots(p-n+1)}{n!}\Delta^n y_0}$$

**Validity range.** The formula is accurate for $0 \le p \le 1$, primarily near the beginning of equidistant tables. For values near the end, backward differences are used.

> [!info] Alternate proof via Shift Operator $E$
> Using the relationship $E = 1 + \Delta$:
> $$y(x) = y(x_0 + ph) = E^p y_0 = (1 + \Delta)^p y_0$$
> Expanding $(1 + \Delta)^p$ by the binomial theorem:
> $$(1 + \Delta)^p = 1 + p\Delta + \frac{p(p-1)}{2!}\Delta^2 + \frac{p(p-1)(p-2)}{3!}\Delta^3 + \cdots$$
> Operating on $y_0$ immediately gives the formula.

> [!note] Why the falling product appears at all, and how to spot a wrong formula
> The pattern in the coefficients is
> $$1,\quad p,\quad \frac{p(p-1)}{2!},\quad \frac{p(p-1)(p-2)}{3!},\quad \cdots$$
> Each one is the previous one multiplied by $\frac{p-k}{k}$. That single
> recurrence is the fingerprint of the formula, and it is why the coefficient of
> $\Delta^k y_0$ is always a *falling* factorial divided by $k!$.
>
> A formula built from **rising** powers, $\frac{p^k}{k!}$, is not Newton's
> forward formula. It looks similar, produces plausible numbers for small $k$, and
> is wrong. Part (b) and part (d) of this question both use the falling form, and
> you can check any derivation against those.

> [!note] Where this is used again
> Part (d) applies this with $y = x^4$, and Q.4(b) applies central difference formulas to a table of $e^x$
> values. See [[NM-4.7_Newtons_Forward_Difference|NM-4.7 · Newton's Forward Difference]].

---

### [2022 Q.2(c)]

**Question.** Using Newton's forward difference formula find the sum $S_n = 1^3 + 2^3 + 3^3 + \cdots + n^3$.

*[Marks: 03, CO: 1]*

**Solution.**

**Step 1. Build the difference table.** Here $y = r^3$ for $r = 1, 2, 3, \ldots$
with $h = 1$, so $u = r - 1$ and $r = u + 1$.

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

The series returns $r^3$ exactly, as it must, since $r^3$ is itself a cubic. The
$\Delta^4$ row of zeros confirms it: a degree-$k$ polynomial has a constant
$k$-th forward difference and a zero $(k+1)$-th.

**Step 3. Sum from $u = 0$ to $u = n-1$.**

$$
S_n = \sum_{u=0}^{n-1}\left[1 + 7u + 6u(u-1) + u(u-1)(u-2)\right]
$$

Now use the standard sums, each of which is a hockey-stick identity in disguise:

$$
\sum_{u=0}^{n-1} 1 = n, \qquad \sum u = \frac{n(n-1)}{2}, \qquad \sum u(u-1) = 2\binom{n}{3} = \frac{n(n-1)(n-2)}{3}
$$

$$
\sum u(u-1)(u-2) = 6\sum\binom{u}{3} = 6\binom{n}{4} = \frac{n(n-1)(n-2)(n-3)}{4}
$$

So

$$
S_n = n + \frac{7n(n-1)}{2} + 2n(n-1)(n-2) + \frac{n(n-1)(n-2)(n-3)}{4}
$$

**Step 4. Collect over the common denominator 4.**

$$
S_n = \frac{4n + 14n(n-1) + 8n(n-1)(n-2) + n(n-1)(n-2)(n-3)}{4}
$$

Expanding the four terms, $4n$, $14n^2 - 14n$, $8n^3 - 24n^2 + 16n$ and
$n^4 - 6n^3 + 11n^2 - 6n$, and collecting:

$$
4n - 14n + 16n - 6n = 0, \qquad 14n^2 - 24n^2 + 11n^2 = n^2, \qquad 8n^3 - 6n^3 = 2n^3, \qquad n^4
$$

$$
n^4 + 2n^3 + n^2 = n^2(n+1)^2
$$

$$\boxed{S_n = \left[\frac{n(n+1)}{2}\right]^2}$$

> [!info] Check by direct evaluation
> | $n$ | $1^3 + \cdots + n^3$ | $\left[\frac{n(n+1)}{2}\right]^2$ |
> | --: | --: | --: |
> | 1 | 1 | 1 |
> | 2 | 9 | 9 |
> | 3 | 36 | 36 |
> | 4 | 100 | 100 |
> | 5 | 225 | 225 |
> | 6 | 441 | 441 |
>
> All six agree.

> [!note] Why the hockey-stick identity is the tool here, and what it costs
> Every sum in step 3 is of the form $\sum \binom{u}{k}$, and each of those has
> the closed form $\binom{n}{k+1}$ by the hockey-stick identity. Recognising
> that pattern is what makes the algebra short; expanding each sum term by term
> instead turns a four-line calculation into a page and is where mistakes enter.
>
> Worth noting that $u(u-1)(u-2)$ appears rather than $u^3$, which is the reason
> the hockey-stick form is available at all. Working with falling factorials
> rather than powers is what Newton difference formulas are built on.

---

---

**Also asked here.**

- *2021 Q.3(b)* is the same question as [[NM-4.6_Lagranges_Interpolation|NM-4.6]], which is written in `NM-4.6`.

---

**Answered in phase P6, in `../CT_Questions/`.**

- *CT-02A Q.2* is a class-test question. Its answer is in `../CT_Questions/CT_answers_exam_style.md`, with the reasoning in `../CT_Questions/CT_answers_explanation.md`.

---

<a id="nm-49"></a><a id="nm-4.9"></a>
## NM-4.9 · Newton's Divided Difference / General Interpolation

### [2019 Q.5(c)]

**Question.** Using Newton's general interpolation formula find $f(x)$ as a polynomial in $x$ for the following table. Also, determine $f(3.5)$ using the polynomial.

*[Marks: 04]*

**Solution.**

| $x$ | $-1$ | 0 | 3 | 6 | 7 |
| :---: | :---: | :---: | :---: | :---: | :---: |
| $f(x)$ | 3 | $-6$ | 39 | 822 | 1611 |

**Divided differences.** Each entry is
$f[x_i, \ldots, x_{i+k}] = \dfrac{f[x_{i+1}, \ldots, x_{i+k}] - f[x_i, \ldots, x_{i+k-1}]}{x_{i+k} - x_i}$.

| Order | Values |
| :---: | :--- |
| 0 | $3,\ -6,\ 39,\ 822,\ 1611$ |
| 1 | $\dfrac{-6-3}{0-(-1)} = -9$; $\dfrac{39-(-6)}{3-0} = 15$; $\dfrac{822-39}{6-3} = 261$; $\dfrac{1611-822}{7-6} = 789$ |
| 2 | $\dfrac{15-(-9)}{3-(-1)} = 6$; $\dfrac{261-15}{6-0} = 41$; $\dfrac{789-261}{7-3} = 132$ |
| 3 | $\dfrac{41-6}{6-(-1)} = 5$; $\dfrac{132-41}{7-0} = 13$ |
| 4 | $\dfrac{13-5}{7-(-1)} = 1$ |

**Newton's general (divided difference) form.**

$$f(x) = f[x_0] + f[x_0, x_1](x - x_0) + f[x_0, x_1, x_2](x - x_0)(x - x_1) + \cdots$$

$$f(x) = 3 - 9(x + 1) + 6(x + 1)x + 5(x + 1)x(x - 3) + (x + 1)x(x - 3)(x - 6)$$

**Expand to a polynomial in $x$.** Working outward from the last term:

$$(x + 1)x(x - 3)(x - 6) = x^4 - 8x^3 + 9x^2 + 18x$$

$$5(x + 1)x(x - 3) = 5(x^3 - 2x^2 - 3x) = 5x^3 - 10x^2 - 15x$$

$$6(x + 1)x = 6x^2 + 6x, \qquad -9(x + 1) = -9x - 9$$

Collecting all terms:

$$f(x) = x^4 - 3x^3 + 5x^2 - 6$$

$$\boxed{f(x) = x^4 - 3x^3 + 5x^2 - 6}$$

**Apply it to $f(3.5)$.** Substituting into the expanded form:

$$f(3.5) = 150.0625 - 128.625 + 61.25 - 6 = 76.6875$$

$$\boxed{f(3.5) = 76.6875}$$

> [!info] Check against the Newton form and the tabulated values
> Substituting $x = 3.5$ into the unevaluated Newton form gives
> $3 - 9(4.5) + 6(15.75) + 5(7.875) + (-19.6875) = 76.6875$, the same value by a
> second route. And substituting the polynomial back into the tabulated
> abscissae reproduces every printed entry: $f(-1) = 1 + 3 + 5 - 6 = 3$,
> $f(0) = -6$, $f(3) = 81 - 81 + 45 - 6 = 39$, $f(6) = 1296 - 648 + 180 - 6 = 822$,
> and $f(7) = 2401 - 1029 + 245 - 6 = 1611$. The table is recovered exactly, so
> the polynomial is the interpolation polynomial and no tabulated value is
> contradicted.

> [!note] The expansion is the part that gets skipped and should not be
> The Newton form and the expanded form are the same polynomial, and a common
> shortcut is to quote the Newton form and then evaluate $f(3.5)$ from it. That is
> perfectly valid arithmetic and produces the right number, but the question asks
> for the polynomial in $x$, so the expansion is part of the answer.
>
> **Expand from the outside in.** The highest-order product is the one with the
> most factors, so expand it first and work down. Working inward-out instead means
> carrying an unexpanded product through three lines, and the errors compound.

---

### [2020 Q.5(b)]

**Question.** Using Newton's divided difference interpolating polynomial estimate the value of signal $s(t)$ at $t = 2.25$ sec for the following tabulated values.

*[Marks: 06]*

**Solution.**

| $t$ | 0.5 | 0.2 | 1.4 | 2.2 | 3.0 |
| --- | --: | --: | --: | --: | --: |
| $s(t)$ | $-10.25$ | $-3.768$ | $5.976$ | $28.972$ | $79.0$ |

> [!warning] The table is printed out of order, and it turns out not to matter
> The $t$ column runs $0.5, 0.2, 1.4, 2.2, 3.0$, with $0.5$ printed **before**
> $0.2$. This looks like a typesetting slip, and it is worth checking what it does
> to the answer.
>
> **It changes nothing.** Newton's divided difference interpolation is
> **invariant under any permutation of the nodes**. Run it in the printed order
> and run it sorted, and every value of $s(2.25)$ is identical:
> $30.73362901$ in both cases, to ten decimals.
>
> The reason is short. The divided difference $f[x_0, x_1, \dots, x_k]$ is
> **symmetric** in its $k+1$ nodes, so reordering them does not change its value.
> And the product $(t-x_0)(t-x_1)\cdots(t-x_{k-1})$ covers the same set of factors
> whichever order they are listed in. Both halves of the formula are unchanged, so
> the polynomial is unchanged.
>
> Contrast this with the **forward difference** formula, where the leading
> diagonal $\Delta^k y_0$ is tied to $x_0$ and reordering the table destroys it.
> That is the real reason equal spacing and ascending order matter there and not
> here.

**Step 1. Build the divided difference table.** Each entry divides by the
$x$-difference of the two nodes it spans.

| Order | Values |
| :-- | :-- |
| $s(t_i)$ | $-10.250000$, $-3.768000$, $5.976000$, $28.972000$, $79.000000$ |
| $1^{st}$ | $-21.606667$, $8.120000$, $28.745000$, $62.535000$ |
| $2^{nd}$ | $33.029630$, $10.312500$, $21.118750$ |
| $3^{rd}$ | $-13.363017$, $3.859375$ |
| $4^{th}$ | $6.888957$ |

Worked entries, so nothing is asserted on trust:

$$
f[x_0,x_1] = \frac{-3.768 - (-10.25)}{0.2 - 0.5} = \frac{6.482}{-0.3} = -21.606667
$$

$$
f[x_1,x_2] = \frac{5.976 - (-3.768)}{1.4 - 0.2} = \frac{9.744}{1.2} = 8.12
$$

$$
f[x_0,x_1,x_2] = \frac{8.12 - (-21.606667)}{1.4 - 0.5} = \frac{29.726667}{0.9} = 33.029630
$$

$$
f[x_1,x_2,x_3] = \frac{f[x_2,x_3] - f[x_1,x_2]}{2.2 - 0.2}, \qquad f[x_2,x_3] = \frac{28.972 - 5.976}{2.2-1.4} = \frac{22.996}{0.8} = 28.745
$$

$$
f[x_1,x_2,x_3] = \frac{28.745 - 8.12}{2.0} = 10.3125, \qquad f[x_0,x_1,x_2,x_3] = \frac{10.3125 - 33.029630}{2.2 - 0.5} = \frac{-22.717130}{1.7} = -13.363017
$$

$$
f[x_2,x_3,x_4] = \frac{f[x_3,x_4] - f[x_2,x_3]}{3.0-1.4}, \qquad f[x_3,x_4] = \frac{79.0 - 28.972}{3.0-2.2} = \frac{50.028}{0.8} = 62.535
$$

$$
f[x_2,x_3,x_4] = \frac{62.535 - 28.745}{1.6} = 21.11875, \qquad f[x_1,x_2,x_3,x_4] = \frac{21.11875 - 10.3125}{3.0-0.2} = \frac{10.80625}{2.8} = 3.859375
$$

$$
f[x_0,x_1,x_2,x_3,x_4] = \frac{3.859375 - (-13.363017)}{3.0-0.5} = \frac{17.222392}{2.5} = 6.888957
$$

**Step 2. Write the polynomial.** The leading diagonal is
$-10.25,\ -21.606667,\ 33.029630,\ -13.363017,\ 6.888957$.

$$
s(t) = -10.25 + (-21.606667)(t - 0.5) + (33.029630)(t-0.5)(t-0.2) + (-13.363017)(t-0.5)(t-0.2)(t-1.4) + (6.888957)(t-0.5)(t-0.2)(t-1.4)(t-2.2)
$$

**Step 3. Evaluate at $t = 2.25$.** The factors are $1.75,\ 2.05,\ 0.85,\ 0.05$.

| Term | Working | Value | Running |
| :-- | :-- | --: | --: |
| $s_0$ | | $-10.250000$ | $-10.250000$ |
| $f[x_0,x_1](t-x_0)$ | $(-21.606667)(1.75)$ | $-37.811667$ | $-48.061667$ |
| $f[x_0,x_1,x_2](t-x_0)(t-x_1)$ | $(33.029630)(1.75)(2.05) = (33.029630)(3.5875)$ | $+118.494$ | $+70.432$ |
| $f[x_0..x_3](\cdot)(\cdot)(\cdot)$ | $(-13.363017)(1.75)(2.05)(0.85) = (-13.363017)(3.049375)$ | $-40.749$ | $29.683$ |
| $f[x_0..x_4](\cdot)(\cdot)(\cdot)(\cdot)$ | $(6.888957)(1.75)(2.05)(0.85)(0.05) = (6.888957)(0.15246875)$ | $+1.050$ | $30.734$ |

$$\boxed{s(2.25) = 30.7336}$$

> [!info] Check
> **Exact rational evaluation.** Carrying the table in fractions rather than
> decimals, the leading diagonal is
> $-\frac{41}{4},\ -\frac{3241}{150},\ \frac{4459}{135},\ -\frac{49069}{3672},\ \frac{101185}{14688}$
> and the result is exactly
> $$s(2.25) = \frac{2265929}{73728} = 30.7336290148$$
> The decimal working above agrees to every digit shown.
>
> **The unique quartic through the five points.** Solving for the polynomial
> directly in powers of $t$ and evaluating at $2.25$ gives the same
> $\frac{2265929}{73728}$. Two different methods, one answer.
>
> **Ordering.** Sorting the table to $0.2, 0.5, 1.4, 2.2, 3.0$ and re-running
> gives $30.7336290148$ again, to ten decimals, as the warning above states. The
> **intermediate rows differ** though, because each divided difference divides by
> the span of the two nodes it covers. That is worth expecting: the first row is
> $-21.606667, 18.028889, 28.745, 62.535$ sorted against $-21.606667, 8.12,
> 28.745, 62.535$ printed, and both are correct for their own node order.

> [!warning] The one choice that would change the answer
> A second reading is available: suppose the *values* were transposed rather than
> the labels, so that $s(0.2) = -10.25$ and $s(0.5) = -3.768$. That reading makes
> the signal **monotonically increasing**, $-10.25, -3.768, 5.976, 28.972, 79.0$,
> which is what a real rising signal looks like, whereas the printed pairing makes
> it dip from $-3.768$ down to $-10.25$ and then climb.
>
> That reading gives $s(2.25) = 31.2821$, which is $0.548$, or $1.8\%$, away from
> the printed answer. Neither reading is generated by a cubic: fitting a cubic
> through the first four points of either reading and evaluating it at $t = 3.0$
> gives $17.27$ against the actual $79.0$, or $96.70$ against $79.0$. Both are
> hopeless, so all five points are genuinely needed and a quartic is the right
> degree in either case. The table is just data.
>
> **The table as printed is the answer.** Pair each $s$ with the $t$ on its own
> row, which gives $30.7336$. But the dip at $t = 0.5$ is odd enough to be worth
> naming in an answer: state the reading used, and give $31.2821$ as the
> alternative. An answer that silently picks one hides a $1.8\%$ assumption.

---

### [2022 Q.2(a)]

**Question.** Find the polynomial which fits the following data: $(-1, 7)$, $(1, 5)$, $(2, 15)$.

*[Marks: 04, CO: 1]*

**Solution.**

With three points the lowest-degree polynomial that can pass through all three
is a **quadratic** $y = a_0 + a_1 x + a_2 x^2$. A linear fit would need the
points to be collinear, and they are not, so the degree is forced.

**Method: simultaneous equations.** Substitute each point:

$$
a_0 - a_1 + a_2 = 7
$$

$$
a_0 + a_1 + a_2 = 5
$$

$$
a_0 + 2a_1 + 4a_2 = 15
$$

Subtract the first from the second to kill $a_0$ and $a_2$ at once:

$$
2a_1 = -2 \quad \Rightarrow \quad a_1 = -1
$$

With $a_1 = -1$ the first equation gives $a_0 + a_2 = 6$, and the third gives
$a_0 + 4a_2 = 17$. Subtract: $3a_2 = 11$, so $a_2 = \frac{11}{3}$, and
$a_0 = 6 - \frac{11}{3} = \frac{7}{3}$.

$$\boxed{y = \frac{11}{3}x^2 - x + \frac{7}{3}}$$

**Check every point**, which takes one line each and settles the answer.

$$
x = -1: \quad \frac{11}{3}(1) + 1 + \frac{7}{3} = 6 + 1 = 7 \quad \checkmark
$$

$$
x = 1: \quad \frac{11}{3} - 1 + \frac{7}{3} = 6 - 1 = 5 \quad \checkmark
$$

$$
x = 2: \quad \frac{11}{3}(4) - 2 + \frac{7}{3} = 17 - 2 = 15 \quad \checkmark
$$

> [!info] Two more routes to the same coefficients
> **Lagrange form**, which is the method the question's neighbours ask about:
> $$y = 7\frac{(x-1)(x-2)}{(-1-1)(-1-2)} + 5\frac{(x+1)(x-2)}{(1+1)(1-2)} + 15\frac{(x+1)(x-1)}{(2+1)(2-1)}$$
> $$= \frac{7}{6}(x^2-3x+2) - \frac{5}{2}(x^2-x-2) + \frac{15}{3}(x^2-1)$$
> $$= \left(\frac{7}{6} - \frac{5}{2} + 5\right)x^2 + \left(-\frac{7}{2} + \frac{5}{2}\right)x + \left(\frac{7}{3} + 5 - 5\right)$$
> $$= \frac{11}{3}x^2 - x + \frac{7}{3}$$
>
> **Newton divided differences.** With the nodes already in increasing order,
> which they happen to be here,
>
> | Order | Values |
> | :-- | :-- |
> | $y$ | 7, 5, 15 |
> | $1^{st}$ | $-1$, $10$ |
> | $2^{nd}$ | $\frac{11}{3}$ |
>
> Newton's form is $y = 7 - (x+1) + \frac{11}{3}(x+1)(x-1)$, and expanding gives
> $7 - x - 1 + \frac{11}{3}(x^2 - 1) = \frac{11}{3}x^2 - x + \frac{7}{3}$. Same again.

> [!note] Why a quadratic is the right degree, and how you can tell in advance
> The degree rises one at a time as points are added, so three points mean a
> quadratic unless the points happen to be collinear. Check that first: if the
> slopes between consecutive points agree, a linear fit is enough and the third
> equation will be redundant.
>
> Here the slopes are $\frac{5-7}{1-(-1)} = -1$ and $\frac{15-5}{2-1} = 10$, which
> disagree, so the quadratic term is genuinely needed.

---

---

**Also asked here.**

- *2019 Q.4(b)* is the same question as [[NM-4.6_Lagranges_Interpolation|NM-4.6]], which is written in `NM-4.6`.

---

<a id="nm-410"></a><a id="nm-4.10"></a>
## NM-4.10 · Gauss Forward / Backward & Stirling's Formulas

### [2021 Q.4(b)]

**Question.** From the following table, calculate the value of $e^{1.17}$ using Gauss' forward formula.

*[Marks: 05, CO: 2]*

**Solution.**

| $x$ | 1.00 | 1.05 | 1.10 | 1.15 | 1.20 | 1.25 | 1.30 |
| --- | --: | --: | --: | --: | --: | --: | --: |
| $e^x$ | 2.7183 | 2.8577 | 3.0042 | 3.1582 | 3.3201 | 3.4903 | 3.6693 |

**Step 1. Choose origin $x_0$ and compute $p$.**
The target is $x = 1.17$ and step size $h = 0.05$.
Gauss' forward formula is a central-difference formula designed for $0 \le p \le 1$ (ideally $0 \le p \le 0.5$).
Choose origin $x_0 = 1.15$. Then:

$$
p = \frac{x - x_0}{h} = \frac{1.17 - 1.15}{0.05} = \frac{0.02}{0.05} = 0.4
$$

**Step 2. Difference table.**

| $x$ | 1.00 | 1.05 | 1.10 | 1.15 | 1.20 | 1.25 | 1.30 |
| --- | --: | --: | --: | --: | --: | --: | --: |
| $y$ | 2.7183 | 2.8577 | 3.0042 | 3.1582 | 3.3201 | 3.4903 | 3.6693 |
| $\Delta y$ | 0.1394 | 0.1465 | 0.1540 | 0.1619 | 0.1702 | 0.1790 | |
| $\Delta^2 y$ | 0.0071 | 0.0075 | 0.0079 | 0.0083 | 0.0088 | | |
| $\Delta^3 y$ | 0.0004 | 0.0004 | 0.0004 | 0.0005 | | | |
| $\Delta^4 y$ | 0.0000 | 0.0000 | 0.0001 | | | | |
| $\Delta^5 y$ | 0.0000 | 0.0001 | | | | | |
| $\Delta^6 y$ | 0.0001 | | | | | | |

**Step 3. Collect the central path differences.**
The central difference path traverses in a zigzag pattern:
$y_0 \to \Delta y_0 \to \Delta^2 y_{-1} \to \Delta^3 y_{-1} \to \Delta^4 y_{-2}$:

$$
y_0 = 3.1582, \quad \Delta y_0 = 0.1619, \quad \Delta^2 y_{-1} = 0.0079, \quad \Delta^3 y_{-1} = 0.0004, \quad \Delta^4 y_{-2} = 0.0000
$$

**Step 4. Evaluate the terms ($p = 0.4$).**

Gauss' forward interpolation formula is:

$$
y_p = y_0 + p\Delta y_0 + \frac{p(p-1)}{2!}\Delta^2 y_{-1} + \frac{(p+1)p(p-1)}{3!}\Delta^3 y_{-1} + \frac{(p+1)p(p-1)(p-2)}{4!}\Delta^4 y_{-2} + \cdots
$$

| Term | Algebraic form | Working | Value | Running sum |
| :-- | :-- | :-- | --: | --: |
| $T_0$ | $y_0$ | $3.1582$ | $3.1582000$ | $3.1582000$ |
| $T_1$ | $p\Delta y_0$ | $0.4(0.1619)$ | $+0.0647600$ | $3.2229600$ |
| $T_2$ | $\frac{p(p-1)}{2}\Delta^2 y_{-1}$ | $\frac{0.4(-0.6)}{2}(0.0079) = -0.12(0.0079)$ | $-0.0009480$ | $3.2220120$ |
| $T_3$ | $\frac{(p+1)p(p-1)}{6}\Delta^3 y_{-1}$ | $\frac{(1.4)(0.4)(-0.6)}{6}(0.0004) = -0.056(0.0004)$ | $-0.0000224$ | $3.2219896$ |
| $T_4$ | $\frac{(p+1)p(p-1)(p-2)}{24}\Delta^4 y_{-2}$ | $\frac{(1.4)(0.4)(-0.6)(-1.6)}{24}(0.0000)$ | $0$ | $3.2219896$ |

$$\boxed{e^{1.17} \approx 3.22199}$$

> [!note] The running column is the check that makes the table trustworthy
> Every term is a product of a coefficient and a central-difference entry. Adding
> them in a running total, as the last column does, means a single wrong cell shows
> up immediately as a wrong final sum, and you can back up the terms one at a
> time until it is found.
>
> It also shows *where* to stop. Here the $\Delta^4$ term is zero and the fifth
> would be smaller still, so the sum has converged at three significant
> contributions. The differences shrinking by roughly a factor of 10 to 20 per row is
> the visible signature of a well-behaved function sampled finely.

> [!info] Check by two independent routes
> **Lagrange on the same seven points** gives $3.22199020928$, which agrees to the
> seventh decimal. Lagrange on the nearest four points ($1.05, 1.10, 1.15, 1.20$)
> gives $3.2219896$, identical to the central difference result.
>
> **Against the true value.** $e^{1.17} = 3.2219926385$, so the error is
> $3.04 \times 10^{-6}$. The whole error comes from the table: those $e^x$ values
> are rounded to four decimals, and each carries an error up to $5\times10^{-5}$.
> Interpolating rounded data cannot beat the rounding in the data.

> [!note] Why Gauss' central difference formula is superior here
> Because $x = 1.17$ sits near the middle of the table, choosing $x_0 = 1.15$ gives
> a small interpolation parameter $p = 0.4$ ($0 \le p \le 0.5$). Gauss' forward formula
> draws differences along a central zigzag trajectory, ensuring balanced support from
> points on both sides of $x_0$.
>
> In contrast, using Newton's forward formula from $x_0 = 1.00$ requires $p = 3.4$,
> causing polynomial terms to grow large before cancelling, which degrades numerical stability.
> Central difference formulas like Gauss forward eliminate this issue.

---

<a id="nm-411"></a><a id="nm-4.11"></a>
## NM-4.11 · Difference Table Formation & Applications

### [2017 Q.5(c)]

**Question.** The population of a town in decennial census were as following table in thousand unit. Estimate the population for the year 1955.

*[Marks: 05]*

**Solution.**

| Year | 1921 | 1931 | 1941 | 1951 | 1961 |
| :---: | :---: | :---: | :---: | :---: | :---: |
| Population (thousands) | 46 | 66 | 81 | 93 | 101 |

**Step 1, set up the forward difference formula.** The tabulation interval is
$h = 10$. Taking $x_0 = 1921$, the target $1955$ corresponds to

$$p = \frac{1955 - 1921}{10} = \frac{34}{10} = 3.4$$

**Step 2, the difference table.**

| | 46 | 66 | 81 | 93 | 101 |
| :-- | :-- | :-- | :-- | :-- | :-- |
| $\Delta$ | | 20 | 15 | 12 | 8 |
| $\Delta^2$ | | | $-5$ | $-3$ | $-4$ |
| $\Delta^3$ | | | 2 | $-1$ |
| $\Delta^4$ | | | | $-3$ |

**Step 3, apply the formula.**

$$y = y_0 + p\Delta y_0 + \frac{p(p-1)}{2}\Delta^2 y_0 + \frac{p(p-1)(p-2)}{6}\Delta^3 y_0 + \frac{p(p-1)(p-2)(p-3)}{24}\Delta^4 y_0$$

Term by term:

$$y_0 = 46$$

$$p\Delta y_0 = 3.4 \times 20 = 68$$

$$\frac{p(p-1)}{2}\Delta^2 y_0 = \frac{(3.4)(2.4)}{2}(-5) = 4.08 \times (-5) = -20.4$$

$$\frac{p(p-1)(p-2)}{6}\Delta^3 y_0 = \frac{(3.4)(2.4)(1.4)}{6}(2) = \frac{11.424}{6} \times 2 = 1.904 \times 2 = 3.808$$

$$\frac{p(p-1)(p-2)(p-3)}{24}\Delta^4 y_0 = \frac{(3.4)(2.4)(1.4)(0.4)}{24}(-3) = \frac{4.5696}{24} \times (-3) = 0.1904 \times (-3) = -0.5712$$

Collecting the five terms:

$$y = 46 + 68 - 20.4 + 3.808 - 0.5712 = 96.8368$$

$$\boxed{\text{Population in 1955} \approx 96.8368 \approx 96.84 \text{ thousand}}$$

> [!warning] The fourth-difference term is the one that gets dropped
> $\Delta^4 y_0 = -3$ looks negligible beside $\Delta y_0 = 20$. It is not. Its
> multiplier is $\dfrac{p(p-1)(p-2)(p-3)}{24} = 0.1904$, and $0.1904 \times (-3)
> = -0.5712$, which moves the answer by more than half a thousand people. The
> test is not "is the difference small" but "is the difference times its
> multiplier small", and those are different questions.
>
> Two slips account for most wrong answers here. Dropping the trailing $3$ from
> the multiplier, giving $0.1904$ where $0.5712$ is wanted, changes the answer
> by $0.3808$. And forgetting the sign: $p - 3 = 0.4$ is positive and
> $\Delta^4 y_0 = -3$ is negative, so the term *subtracts*.

> [!info] Confirming the value two ways
> **Lagrange.** The polynomial through the same five points, evaluated at
> $x = 1955$, gives $96.8368$ exactly. Two different arrangements of the same
> five numbers, arriving at the same value to six figures.
>
> **Physical.** The census rises from $93$ to $101$ over $1951$–$1961$, so
> linear interpolation alone gives $93 + 0.4(8) = 96.2$. The difference-form
> answer $96.8368$ sits *above* that, and it must: the second differences are
> all negative, so the population curve is concave, and a concave curve lies
> above its chords. Note what this says physically, because it is the opposite
> of the intuitive reading. The census is still *gaining* people faster than
> before in absolute terms, 20, 15, 12, 8 per decade is a falling *increment*,
> but the percentage growth rate $20/46$, $15/66$, $12/81$, $8/93$ is falling
> much faster, and a concave curve on this data means deceleration in
> proportional terms while the absolute increase remains substantial. Reporting
> $96.8$ as "slightly below the midpoint" would be reading the shape backwards.

---

### [2020 Q.3(b)]

**Question.** The population of a town in the decennial census was as given below. Estimate the population for the year (i) 1895 and (ii) 1925.

*[Marks: 04]*

**Solution.**

| Year $x$ | 1891 | 1901 | 1911 | 1921 | 1931 |
| --- | --: | --: | --: | --: | --: |
| Population $y$ (thousands) | 46 | 66 | 81 | 93 | 101 |

**Step 1. Both targets lie inside the data range $[1891, 1931]$.**
- The target $1895$ lies in the first subinterval $[1891, 1901]$, four years after the initial node $x_0 = 1891$. Because it is near the **beginning** of the table, **Newton's forward difference formula** is the canonical choice (with $p = \frac{1895 - 1891}{10} = +0.4$, so $|p| < 1$).
- The target $1925$ lies in the last subinterval $[1921, 1931]$, six years before the terminal node $x_n = 1931$. Because it is near the **end** of the table, **Newton's backward difference formula** is the canonical choice (with $p = \frac{1925 - 1931}{10} = -0.6$, so $|p| < 1$).

Both problems are genuine **interpolations** (not extrapolations). We construct the difference table and apply each formula with its optimal base node.

**Step 2. Difference table.** Here $h = 10$ years.

| $x$ | 1891 | 1901 | 1911 | 1921 | 1931 |
| --- | --: | --: | --: | --: | --: |
| $y$ | 46 | 66 | 81 | 93 | 101 |
| $\Delta y$ | 20 | 15 | 12 | 8 | |
| $\Delta^2 y$ | $-5$ | $-3$ | $-4$ | | |
| $\Delta^3 y$ | 2 | $-1$ | | | |
| $\Delta^4 y$ | $-3$ | | | | |

From the table:
- **Forward differences from $x_0 = 1891$:**
  $$y_0 = 46, \quad \Delta y_0 = 20, \quad \Delta^2 y_0 = -5, \quad \Delta^3 y_0 = 2, \quad \Delta^4 y_0 = -3$$
- **Backward differences from $x_n = 1931$:**
  $$y_n = 101, \quad \nabla y_n = 8, \quad \nabla^2 y_n = -4, \quad \nabla^3 y_n = -1, \quad \nabla^4 y_n = -3$$

**Step 3. The formulas.**
- **Newton's Forward Interpolation Formula** ($p = \frac{x - x_0}{h}$):
  $$y(x) = y_0 + p\Delta y_0 + \frac{p(p-1)}{2!}\Delta^2 y_0 + \frac{p(p-1)(p-2)}{3!}\Delta^3 y_0 + \frac{p(p-1)(p-2)(p-3)}{4!}\Delta^4 y_0$$

- **Newton's Backward Interpolation Formula** ($p = \frac{x - x_n}{h}$):
  $$y(x) = y_n + p\nabla y_n + \frac{p(p+1)}{2!}\nabla^2 y_n + \frac{p(p+1)(p+2)}{3!}\nabla^3 y_n + \frac{p(p+1)(p+2)(p+3)}{4!}\nabla^4 y_n$$

**Step 4. Part (i), the year 1895 (Newton's Forward Interpolation).**

For $x = 1895$, choose $x_0 = 1891$ (beginning of table):
$$p = \frac{1895 - 1891}{10} = +0.4$$

Using forward differences from $x_0 = 1891$:

| Term | Working | Value | Running |
| :-- | :-- | --: | --: |
| $y_0$ | | 46 | 46.000000 |
| $p\Delta y_0$ | $(0.4)(20)$ | $+8.0$ | 54.000000 |
| $\frac{p(p-1)}{2}\Delta^2 y_0$ | $\frac{(0.4)(-0.6)}{2}(-5) = (-0.12)(-5)$ | $+0.6$ | 54.600000 |
| $\frac{p(p-1)(p-2)}{6}\Delta^3 y_0$ | $\frac{(0.4)(-0.6)(-1.6)}{6}(2) = (0.064)(2)$ | $+0.128$ | 54.728000 |
| $\frac{p(p-1)(p-2)(p-3)}{24}\Delta^4 y_0$ | $\frac{(0.4)(-0.6)(-1.6)(-2.6)}{24}(-3) = (-0.0416)(-3)$ | $+0.1248$ | 54.852800 |

$$
\boxed{y(1895) = 54.8528 \text{ thousand} \approx 54\,853}
$$

*(Note on alternative route: Applying Newton's backward difference formula from $x_n = 1931$ with $p = \frac{1895 - 1931}{10} = -3.6$ gives $101 + (-3.6)(8) + \frac{(-3.6)(-2.6)}{2}(-4) + \frac{(-3.6)(-2.6)(-1.6)}{6}(-1) + \frac{(-3.6)(-2.6)(-1.6)(-0.6)}{24}(-3) = 101 - 28.8 - 18.72 + 2.496 - 1.1232 = 54.8528$, identically matching the forward result).*

**Step 5. Part (ii), the year 1925 (Newton's Backward Interpolation).**

For $x = 1925$, choose $x_n = 1931$ (end of table):
$$p = \frac{1925 - 1931}{10} = -0.6$$

Using backward differences from $x_n = 1931$:

| Term | Working | Value | Running |
| :-- | :-- | --: | --: |
| $y_n$ | | 101 | 101.000000 |
| $p\nabla y_n$ | $(-0.6)(8)$ | $-4.8$ | 96.200000 |
| $\frac{p(p+1)}{2}\nabla^2 y_n$ | $\frac{(-0.6)(0.4)}{2}(-4) = (-0.12)(-4)$ | $+0.48$ | 96.680000 |
| $\frac{p(p+1)(p+2)}{6}\nabla^3 y_n$ | $\frac{(-0.6)(0.4)(1.4)}{6}(-1) = (-0.056)(-1)$ | $+0.056$ | 96.736000 |
| $\frac{p(p+1)(p+2)(p+3)}{24}\nabla^4 y_n$ | $\frac{(-0.6)(0.4)(1.4)(2.4)}{24}(-3) = (-0.0336)(-3)$ | $+0.1008$ | 96.836800 |

$$
\boxed{y(1925) = 96.8368 \text{ thousand} \approx 96\,837}
$$

> [!info] Check by two independent routes
> **Lagrange on all five points.** The quartic through the five census values is
> $y = \dfrac{34283}{625} = 54.8528$ at $x = 1895$ and
> $\dfrac{60523}{625} = 96.8368$ at $x = 1925$. Both are exact rationals, and both
> match the finite-difference results to every digit printed. This is not a
> coincidence: with all nodes retained, the forward, backward, and Lagrange forms
> represent the exact same polynomial.
>
> **The polynomial itself.** The unique quartic through the data is
> $$y = -\frac{x^4}{80000} + \frac{2869x^3}{30000} - \frac{10975423x^2}{40000} + \frac{10497237779x}{30000} - \frac{13387268210881}{80000}$$
> and evaluating it at 1895 and 1925 reproduces both answers. A third route, an
> exact rational evaluation rather than a decimal one, confirms the arithmetic.

> [!warning] Choosing between Forward and Backward interpolation
> **1. Why choose Forward for 1895 and Backward for 1925?**
> The parameter $p$ measures distance from the anchor node in units of $h$.
> - For $1895$, using $x_0 = 1891$ yields $p = +0.4$, so $|p| < 1$. The factorial terms $\frac{p(p-1)\cdots}{k!}$ remain small and decay rapidly, which is critical if truncated to a lower degree.
> - If one used Backward interpolation from $x_n = 1931$ for $1895$, $p = -3.6$ ($|p| > 1$), causing the factorial coefficients to blow up (e.g., the 4th-order coefficient is $25.5024$). While the full 4th-degree sum matches analytically, any lower-order truncation is wildly unstable.
> - Conversely, for $1925$, using $x_n = 1931$ yields $p = -0.6$, keeping $|p| < 1$ and well-conditioned.
>
> **2. The sign of $p$ in Backward difference.**
> Backward $p$ is $p = \frac{x - x_n}{h}$, so it is **negative** when the target lies to the left of the anchor node ($p = -0.6$ for 1925). Writing $p = \frac{x_n - x}{h} = +0.6$ with the same formulas is a classic sign mistake that ruins the result.
>
> **Both queries are interpolations**: $1895 \in [1891, 1901]$ and $1925 \in [1921, 1931]$. Neither point lies outside the surveyed domain $[1891, 1931]$.

---

### [2021 Q.4(c)]

**Question.** You have a gas sensor. It sends a value in 2 seconds. The table of received values is $t = 1, 3, 5, 7, 9$ with values $24, 120, 336, 720, 1200$. What will be the sensor's reading at 10 s?

*[Marks: 05, CO: 2]*

**Solution.**

| $t$ (s) | 1 | 3 | 5 | 7 | 9 |
| --- | --: | --: | --: | --: | --: |
| Value | 24 | 120 | 336 | 720 | 1200 |

**Step 1. Difference table.** Here $h = 2$.

| $t$ | 1 | 3 | 5 | 7 | 9 |
| --- | --: | --: | --: | --: | --: |
| $y$ | 24 | 120 | 336 | 720 | 1200 |
| $\Delta y$ | 96 | 216 | 384 | 480 | |
| $\Delta^2 y$ | 120 | 168 | 96 | | |
| $\Delta^3 y$ | 48 | $-72$ | | | |
| $\Delta^4 y$ | $-120$ | | | | |

**Step 2. Observe what the data really are.** The first three differences of $r^3$
are $3r^2 + 3r + 1$, $6r + 6$, $6$. Here $\Delta y = 96, 216, 384, 480$ grows by
$120, 168, 96$, not by a constant, so this is not a pure cubic in $t$.

Check the natural candidate: $(t+1)(t+2)(t+3)$ gives $24, 120, 336, 720$ for
$t = 1, 3, 5, 7$, exactly matching, but gives $1320$ at $t = 9$, not $1200$.

**The fifth point does not lie on the cubic that the first four define.** This
single fact determines which polynomial the question requires, and it is stated
explicitly rather than resolved by silently choosing one interpretation.

**Step 3(a). Using all five points.** The unique quartic through all five points,
evaluated by Newton's forward formula with $p = \frac{10-1}{2} = 4.5$:

| Term | Working | Value |
| :-- | :-- | --: |
| $y_0$ | | 24 |
| $p\Delta y_0$ | $4.5(96)$ | 432 |
| $\frac{p(p-1)}{2}\Delta^2 y_0$ | $\frac{4.5(3.5)}{2}(120) = 7.875(120)$ | 945 |
| $\frac{p(p-1)(p-2)}{6}\Delta^3 y_0$ | $\frac{4.5(3.5)(2.5)}{6}(48) = 6.5625(48)$ | 315 |
| $\frac{p(p-1)(p-2)(p-3)}{24}\Delta^4 y_0$ | $\frac{4.5(3.5)(2.5)(1.5)}{24}(-120) = 2.4609375(-120)$ | $-295.3125$ |

$$
24 + 432 + 945 + 315 - 295.3125 = 1420.6875
$$

**Step 3(b). Using the four points that lie on a clean cubic.** Newton's forward
with the first four rows truncated at $\Delta^3$, $p = 4.5$:

$$
24 + 432 + 945 + 315 = 1716
$$

and the cubic through those four points is exactly

$$
y = t^3 + 6t^2 + 11t + 6 = (t+1)(t+2)(t+3)
$$

which gives $1716$ at $t = 10$.

$$\boxed{\text{Five points (quartic): } y(10) = 1420.6875 \qquad \text{Four points (cubic): } y(10) = 1716}$$

> [!info] Check
> Lagrange on all five points gives $1420.6875$, identical to the quartic
> forward-difference result, as it must be: both are the unique degree 4 polynomial
> through the same five points. Lagrange on four points gives $1716$, identical to
> the cubic. So the two answers are not arithmetic disagreements; they are two
> different polynomials, and the choice between them is a modelling decision.
>
> Both target values are **extrapolations**: $t = 10$ lies beyond $t = 9$. Neither is
> as trustworthy as an interpolation would be.

> [!warning] Which one to write
> The honest reading of "the table of received values" is that all five are
> measurements, so all five carry equal weight, and the quartic
> $\boxed{1420.6875}$ is the answer. It fits every point exactly.
>
> The difference from the cubic is $295$, about $17\%$ of the answer, so the
> choice is not cosmetic. Reporting $1420.6875$ without comment conceals a $17\%$
> assumption.
>
> The alternative reading, which many answer keys use, is that the first four
> values are the reliable ones and $t = 9$ is the corrupted reading. That is
> plausible, since a sensor saturating at $1200$ when the pattern says $1320$ is
> exactly what a stuck or clipped sensor does. On that reading the answer is
> $\boxed{1716}$.
>
> Both readings are stated, with the reading assumed by each.

> [!note] Why the choice matters less than it looks
> Both are extrapolations from $t = 9$ to $t = 10$, a single step. Neither
> difference table has settled: $\Delta^4 y = -120$ is not small, so the data are
> not well described by a low-degree polynomial at all, and adding or removing one
> point reshapes the curve.
>
> The honest summary is that a sensor whose values grow by $300$ to $500$ per two
> seconds cannot be predicted to better than a few percent from five samples. The
> $17\%$ spread between the two polynomials is a statement about the data, not
> about the method, and saying so is part of answering the question properly.

---

### [2024 Q.3(b)]

**Question.** The population of a town in decennial census were as in the following table in thousand units. Estimate the population for the year 1995.

*[Marks: 04, CO: 1]*

**Solution.**

**The setup.** A census table is equally spaced with $h = 10$, so the difference
methods apply. But note where the target sits: the table ends at 1961 and the
question asks for **1995**, which is outside the data. That single fact decides
the whole method.

**Step 1. Build the difference table.** Take $h = 10$ years and put the years in
steps from 1921, so $u = (x - 1921)/10$ gives $u = 0, 1, 2, 3, 4$.

| $u$ | 0 | 1 | 2 | 3 | 4 |
| --- | --: | --: | --: | --: | --: |
| $y$ | 46 | 66 | 81 | 93 | 101 |
| $\Delta y$ | 20 | 15 | 12 | 8 | |
| $\Delta^2 y$ | $-5$ | $-3$ | $-4$ | | |
| $\Delta^3 y$ | 2 | $-1$ | | | |
| $\Delta^4 y$ | $-3$ | | | | |

The first differences fall steadily, which means the increments are getting
smaller and the population is decelerating.

**Step 2. Choose backward, not forward.** Because 1995 lies beyond the table,
work from the last point, 1961, and use **backward** differences. Those are the
last entry of each row:

$$
\nabla y = 8, \quad \nabla^2 y = -4, \quad \nabla^3 y = -1, \quad \nabla^4 y = -3
$$

**Step 3. The argument.** With $p$ measured in steps of $h$ past the last point,

$$
p = \frac{1995 - 1961}{10} = 3.4
$$

> [!warning] The trap: this is an extrapolation, and the argument must match
> Forward differences want $p = \frac{1995 - 1921}{10} = 7.4$, which is past the
> far end of the table; backward differences want $p = 3.4$ measured from 1961.
> Both are legitimate, but they are different expansions of the *same* polynomial,
> so they agree only if the difference order is matched to the end you start from.
>
> **Read the target year against the table before choosing.** A target inside the
> table wants forward differences from the left; a target past the right end wants
> backward differences from the right. Choosing forward differences and then
> reading $p$ from 1961 is the mismatch that produces a wrong answer with no
> visible symptom.

**Step 4. Apply the formula**

$$
y = y_n + p\nabla y_n + \frac{p(p+1)}{2!}\nabla^2 y_n + \frac{p(p+1)(p+2)}{3!}\nabla^3 y_n + \frac{p(p+1)(p+2)(p+3)}{4!}\nabla^4 y_n
$$

| Term | Working | Value |
| :-- | :-- | --: |
| $y_n$ | | 101 |
| $p\nabla y_n$ | $3.4(8)$ | 27.2 |
| $\frac{p(p+1)}{2}\nabla^2 y_n$ | $\frac{3.4(4.4)}{2}(-4)$ | $-29.92$ |
| $\frac{p(p+1)(p+2)}{6}\nabla^3 y_n$ | $\frac{3.4(4.4)(5.4)}{6}(-1)$ | $-13.464$ |
| $\frac{p(p+1)(p+2)(p+3)}{24}\nabla^4 y_n$ | $\frac{3.4(4.4)(5.4)(6.4)}{24}(-3)$ | $-64.6272$ |

$$
101 + 27.2 - 29.92 - 13.464 - 64.6272 = 20.1888
$$

$$
\boxed{P(1995) = 20.1888 \text{ thousand (Newton backward difference, all 5 points)}}
$$

**Is this sensible?** A sanity check matters more here than usual, because the
answer is small when a large number would have been the giveaway. The increments
were $20, 15, 12, 8$, the last of them only $8$ thousand per decade. Extrapolating
$3.4$ decades past 1961 on a degree 4 polynomial that has been decelerating for
two decades gives a *decrease* to $20.19$ thousand. That is the polynomial's
answer and it is arithmetically correct, but it is not a plausible prediction: a
linear reading of the last increment alone gives $101 + 3.4(8) = 128.2$.

> [!warning] Why a correct extrapolation can still be wrong
> This is the cleanest example in the paper of a number that is exactly right and
> practically meaningless. The degree 4 interpolating polynomial through five
> points is unique, and evaluating it at 1995 has one answer, $20.1888$. But
> nothing in the data constrains the polynomial beyond 1961, and the extrapolation
> error grows fast: the $\nabla^4$ term alone contributes $-64.6$, which is three
> times the size of the answer.
>
> **The general lesson.** Extrapolate only about one interval beyond the data, and
> even then say that it is an extrapolation. Here the target is $3.4$ intervals
> past the last point, far outside the range where any polynomial can be trusted.
> The responsible engineering answer would be to fit a saturation model, not to
> report $20.19$ thousand as a population.

**Route 2, as a check.** Newton forward from 1921 with $p = 7.4$ gives
$20.1888000000$, matching to nine figures. Lagrange on the five points gives
$20.1887999999$. Both agree with the backward-difference value because all three
evaluate the same unique degree 4 polynomial, so this confirms the arithmetic but
not the modelling. Confirming that a computation is right and confirming that it
answers the question are two different things.

---

[🏠 Master Index](00_Index.md) | [← Prev Topic: NM-3 · Linear Systems](NM-3_Linear_Systems.md) | [Next Topic: NM-5 · Numerical Integration →](NM-5_Numerical_Integration.md)
