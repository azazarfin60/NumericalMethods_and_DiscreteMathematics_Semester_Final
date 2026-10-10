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
> **Origin Layer:** Authored in `../answers_exam_style/`. All numerical results and boxed equations match character-for-character.

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

<a id="nm-42"></a><a id="nm-4.2"></a>
## NM-4.2 · Least-Squares Linear Regression

### [2017 Q.6(b), 2024 Q.3(c)]

**Appeared in:** 2017 Q.6(b), 2024 Q.3(c)

**Question.** Fit a straight line to the $x$ and $y$ values in the first two columns of the following table.

**Solution.**

| $x$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| $y$ | 0.5 | 2.5 | 2.0 | 4.0 | 3.5 | 6.0 | 5.5 |

**Fit $y = a + bx$.** With $n = 7$:

$$\sum x = 28, \qquad \sum y = 24, \qquad \sum xy = 119.5, \qquad \sum x^2 = 140$$

The $\sum xy$ term is the one that requires care, being the only one that is
not a straight sum of a column. Its seven products are

$$1(0.5) = 0.5, \quad 2(2.5) = 5, \quad 3(2) = 6, \quad 4(4) = 16, \quad 5(3.5) = 17.5, \quad 6(6) = 36, \quad 7(5.5) = 38.5$$

which add to $119.5$.

**The normal equations.** With $a\sum x + b\sum x^2 = \sum xy$ and
$na + b\sum x = \sum y$:

$$28a + 140b = 119.5$$

$$7a + 28b = 24$$

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

> [!info] Check by the closed-form expression and by the centroid
> The standard formula
> $$b = \frac{n\sum xy - \sum x\sum y}{n\sum x^2 - \left(\sum x\right)^2} = \frac{7(119.5) - (28)(24)}{7(140) - 28^2} = \frac{836.5 - 672}{980 - 784} = \frac{164.5}{196} = 0.839286$$
> reproduces $47/56$, so the two routes agree. The centroid condition then holds:
> $a = \bar y - b\bar x = 3.4286 - 0.839286(4) = 0.0714$, and substituting back
> gives $0.0714 + 0.839286(4) = 3.4286 = \bar y$, as a least-squares line must.
> Substituting $a$ and $b$ into both normal equations reproduces them exactly:
> $28(0.071429) + 140(0.839286) = 2 + 117.5 = 119.5$ ✓ and
> $7(0.071429) + 28(0.839286) = 0.5 + 23.5 = 24$ ✓.

The correlation coefficient is $r = 0.9318$, so $r^2 = 0.8683$, meaning about
$87\%$ of the variation in $y$ is accounted for by the line. The residuals
alternate in sign and are largest toward the middle of the range, which is the
signature of genuine curvature in the data rather than of an arithmetic slip.

---

### [2018 Q.4(c)]

**Question.** The following data was taken from an experiment that measured the current in a wire for various imposed voltages. On the basis of a linier regression of this data, determine current for a voltage of $3.5\text{ V}$. Plot the line to evaluate the fit.

**Solution.**

| $v$ (V) | 2 | 3 | 4 | 5 | 7 | 10 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| $i$ (A) | 5.2 | 7.8 | 10.7 | 13 | 19.3 | 27.5 |

**Fit the line** $i = a + bv$ by least squares. With $n = 6$:

$$\sum v = 31, \qquad \sum i = 83.5, \qquad \sum v^2 = 203, \qquad \sum vi = 551.7$$

**The normal-equation solution.**

$$b = \frac{n\sum vi - \sum v\sum i}{n\sum v^2 - \left(\sum v\right)^2} = \frac{6(551.7) - (31)(83.5)}{6(203) - 31^2} = \frac{3310.2 - 2588.5}{1218 - 961} = \frac{721.7}{257}$$

$$b = 2.8082\ \text{A/V}$$

$$a = \bar i - b\bar v = \frac{83.5}{6} - 2.8082\left(\frac{31}{6}\right) = 13.9167 - 14.5089 = -0.5922\ \text{A}$$

**The regression line.**

$$\boxed{i = -0.5922 + 2.8082\,v}$$

**The current at $3.5\ \text{V}$.**

$$i(3.5) = -0.5922 + 2.8082(3.5) = -0.5922 + 9.8287 = 9.2364$$

$$\boxed{i(3.5\ \text{V}) = 9.2364\ \text{A}}$$

**Plotting the fit.** The six measured points $(v, i)$ and the fitted line $i = -0.5922 + 2.8082\,v$:

![Linear regression plot of current versus voltage with measured points, fitted line, and evaluated point at 3.5V](diagrams/2018_Q4c_regression.png)

The measured values and residuals against the line are:

| $v$ | measured $i$ | fitted $i$ | residual |
| :--: | :-- | :-- | :-- |
| 2 | 5.2 | $5.0241$ | $+0.1759$ |
| 3 | 7.8 | $7.8323$ | $-0.0323$ |
| 4 | 10.7 | $10.6405$ | $+0.0595$ |
| 5 | 13 | $13.4486$ | $-0.4486$ |
| 7 | 19.3 | $19.0650$ | $+0.2350$ |
| 10 | 27.5 | $27.4895$ | $+0.0105$ |

The residuals are small compared with the values themselves, the largest in
magnitude being $0.4486$ against $13$, so the line describes the data well. A
straight line is a reasonable model for a wire at constant temperature.

> [!info] Check against the centroid and the correlation coefficient
> The centroid of the data is $(\bar v, \bar i) = (5.1667, 13.9167)$, and
> substituting gives $-0.5922 + 2.8082(5.1667) = 13.9167$, so the line passes
> through the centroid as the normal equations require. The correlation
> coefficient is $r = 0.9996$, so $r^2 = 0.9991$, meaning over $99.9\%$ of the
> variation in current is accounted for by the line. As a numerical check, the
> fitted line evaluated at $v = 3$ and $v = 4$ gives $7.8323$ and $10.6405$,
> and interpolating linearly between those at $v = 3.5$ returns $9.2364$, which
> is the value computed above. A straight line, a centroid condition and an
> internal interpolation all agree, so the result is not an artefact of the
> rounding of $a$ and $b$.

---

---

### [2019 Q.4(c)]

**Question.** Deduce the linear regression expression.

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
> line passes through the point $(\bar x, \bar y)$ whatever the data. The
> intercept formula $a = \bar y - b\bar x$ is exactly this condition solved for
> $a$, so the two forms are the same statement and the deduction is internally
> consistent.

---

<a id="nm-43"></a><a id="nm-4.3"></a>
## NM-4.3 · Non-Linear Regression

### [2017 Q.5(b), 2020 Q.3(c)]

**Appeared in:** 2017 Q.5(b), 2020 Q.3(c)

**Question.** Determine the constants $a$ & $b$ by the method of least squares such that $y = a e^{bx}$ fits the following data.

**Solution.**

| $x$ | 2 | 4 | 6 | 8 | 10 |
| :---: | :---: | :---: | :---: | :---: | :---: |
| $y$ | 4.077 | 11.084 | 30.128 | 81.897 | 222.62 |

**Linearise the model.** Taking logarithms of $y = ae^{bx}$,

$$\ln y = \ln a + bx$$

and the data become a straight line $Y = A + bx$ with $Y = \ln y$ and
$A = \ln a$. Then $a = e^A$.

**Transformed data.**

| $x$ | $y$ | $Y = \ln y$ |
| :--: | :-- | :-- |
| 2 | 4.077 | $1.405361$ |
| 4 | 11.084 | $2.405503$ |
| 6 | 30.128 | $3.405455$ |
| 8 | 81.897 | $4.405462$ |
| 10 | 222.62 | $5.405466$ |

**Least squares on the transformed line.** With $n = 5$,

$$\sum x = 30, \qquad \sum Y = 17.027248, \qquad \sum xY = 122.163825, \qquad \sum x^2 = 220$$

$$b = \frac{n\sum xY - \sum x\sum Y}{n\sum x^2 - \left(\sum x\right)^2} = \frac{5(122.163825) - (30)(17.027248)}{5(220) - 900} = \frac{610.819124 - 510.817430}{200}$$

$$b = \frac{100.001694}{200} = 0.50001$$

$$\ln a = \bar Y - b\bar x = \frac{17.027248}{5} - 0.50001\left(\frac{30}{5}\right) = 3.405450 - 3.000052 = 0.405398$$

$$a = e^{0.405398} = 1.4999$$

The tabulated logarithms are evenly spaced by almost exactly $1.000000$,
which is the signature of a pure exponential, and this can be read directly.

**The ratio route.** $222.62 / 81.897 = 2.7183 = e$ to five figures.
Similarly $81.897/30.128 = 2.7183$, $30.128/11.084 = 2.7182$ and
$11.084/4.077 = 2.7187$. Each time $x$ increases by $2$, $y$ is multiplied by
$e$ to within the rounding of the published $y$ values, so

$$y = ae^{bx} \implies \frac{y(x+2)}{y(x)} = e^{2b} = e \implies 2b = 1 \implies b = 0.5$$

$$a = y(x)e^{-bx} = 4.077e^{-1} = 1.4998$$

**The fitted constants.** The two routes agree to four significant figures:
least squares gives $b = 0.50001$ and $a = 1.4999$, while the ratio route gives
$b = 0.5$ and $a = 1.4998$. Taking the values the data were generated from,

$$\boxed{a = 1.50, \qquad b = 0.5}$$

**The fit.**

| $x$ | $y$ given | $y$ fitted $= 1.5e^{0.5x}$ |
| :--: | :-- | :-- |
| 2 | 4.077 | 4.077 |
| 4 | 11.084 | 11.083 |
| 6 | 30.128 | 30.128 |
| 8 | 81.897 | 81.897 |
| 10 | 222.620 | 222.620 |

> [!info] Check by the correlation coefficient and by the residuals
> The correlation coefficient of $\ln y$ against $x$ is $r = 0.9999999996$, so
> the exponential model fits the transformed data perfectly. The tabulated
> residuals of $y$ itself are $-0.0004$, $+0.0004$, $-0.0003$, $-0.0002$ and
> $+0.0003$, all of order $10^{-4}$. That is the rounding of the published $y$
> values to three decimals, not the error of the model.
> The ratio check confirms the same values: each successive quotient is
> $e$ to within $2\times10^{-3}$ relative, so $b = 0.5$ and $a = 1.5$. The
> least-squares route and the direct ratio route agree, which rules out a
> transcription slip in the logarithms.

---

### [2022 Q.2(b)]

**Question.** Using the method of least squares, fit a curve of the form $y = \frac{x}{a + bx}$ to fit the following data $(3, 7.148)$, $(5, 10.231)$, $(8, 13.509)$, $(12, 16.434)$.

**Solution.**

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

<a id="nm-44"></a><a id="nm-4.4"></a>
## NM-4.4 · Regression Criteria & Theory

### [2017 Q.6(a)]

**Question.** With necessary figure(s) explain why minimum sum of error, minimum sum of absolute error and minimum error are ill-suited for regression. Which criterion is best suited for regression?

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
negative errors cancel, so this condition is satisfied by infinitely many
curves, including curves that pass through none of the data. A line far above
three points and far below a fourth can give $\sum e_i = 0$ while fitting
nothing.

```text
   .            .
        sum e = +2
   .    
        sum e = -2      -> total 0, but a terrible fit
```

**Criterion 2: minimum sum of absolute errors, $\sum|e_i|$.** The cancellation is
removed, so the criterion is a genuine measure of badness. However the
function $\sum|e_i|$ is piecewise linear in the curve's parameters, and its
minimum often lies at a point where the slope is not defined, so no simple
normal equations result. The condition is satisfied by several distinct curves
whenever they share the same total absolute deviation, and it is numerically
awkward.

```text
   .            .
        |e| = 2
   .
        |e| = 2      -> total 4, minimum, but not unique
```

**Criterion 3: minimum error.** A single error, $\min_i |e_i|$, considers one
point only. Minimising it drives one residual to zero while the others are
ignored entirely.

**The criterion that is best suited.** The **least-squares criterion**,
minimising the sum of squared errors

$$S = \sum e_i^2$$

is best. Its three properties make it the standard:

1. **No cancellation**, since the square is always non-negative.
2. **A unique, smooth minimum**, and the resulting normal equations
   $\partial S/\partial a_j = 0$ are linear in the parameters, so they have a
   closed-form solution.
3. **A probabilistic justification**: if the measurement errors are independent
   and normally distributed with equal variance, the least-squares fit is the
   maximum-likelihood estimate.

$$\boxed{S = \sum_{i=1}^{n}\left(y_i - f(x_i)\right)^2 \text{ is the criterion to minimise}}$$

---

---

**Also asked here.**

- *2019 Q.4(a)* is the same question as [[NM-4.1_Concepts|NM-4.1]], which is written in `NM-4.1`.

---

<a id="nm-45"></a><a id="nm-4.5"></a>
## NM-4.5 · Linear Interpolation

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

<a id="nm-46"></a><a id="nm-4.6"></a>
## NM-4.6 · Lagrange's Interpolation

### [2018 Q.3(a)]

**Question.** Explain the use of Lagrange's interpolation formula.

**Solution.**

**Use.** Lagrange's formula estimates an intermediate value $f(x)$ at a point
$x$ within the range of a tabulated set $(x_i, f_i)$, without requiring the
tabulated abscissae to be equally spaced.

**The formula.** For $n+1$ points,

$$f(x) \approx \sum_{i=0}^{n} f_i \prod_{\substack{j=0 \\ j \ne i}}^{n}\frac{x - x_j}{x_i - x_j}$$

**Why it is used.**

1. **Unequal spacing is allowed.** This is its principal advantage over
   Newton's formulas, which assume a common tabular spacing $h$. Data from
   experiment or from a table with a varying interval are handled directly.
2. **The tabulated order is irrelevant.** The formula is symmetric in the
   points; permuting them leaves the result unchanged, which is worth noting
   when a table is printed with its entries out of order.
3. **A single expression gives the value.** The whole formula is written once
   and evaluated at any $x$ in range, with no successive-difference table to
   construct.
4. **The error is available.** With $n+1$ points the error is
   $R_n = \dfrac{f^{(n+1)}(\xi)}{(n+1)!}\prod_{i=0}^{n}(x - x_i)$, so the
   accuracy of a chosen set can be judged before evaluating.

**Limitations.** Adding a new point requires recomputing every coefficient,
unlike Newton's divided-difference form where earlier work is retained. The
formula is also inefficient for repeated evaluation at many points, where a
single polynomial written out once is preferable.

---

### [2018 Q.3(c)]

**Question.** Find $f(2.5)$ from the given data, $x$: 1, 2, 3 and $f(x)$: 0, 1, 8.

**Solution.**

| $x$ | 1 | 2 | 3 |
| :---: | :---: | :---: |
| $f(x)$ | 0 | 1 | 8 |

**Lagrange's formula.** With three points,

$$f(x) = \frac{(x - x_1)(x - x_2)}{(x_0 - x_1)(x_0 - x_2)}f_0 + \frac{(x - x_0)(x - x_2)}{(x_1 - x_0)(x_1 - x_2)}f_1 + \frac{(x - x_0)(x - x_1)}{(x_2 - x_0)(x_2 - x_1)}f_2$$

At $x = 2.5$:

$$L_0 = \frac{(2.5 - 2)(2.5 - 3)}{(1 - 2)(1 - 3)} = \frac{(0.5)(-0.5)}{(-1)(-2)} = \frac{-0.25}{2} = -0.125$$

$$L_1 = \frac{(2.5 - 1)(2.5 - 3)}{(2 - 1)(2 - 3)} = \frac{(1.5)(-0.5)}{(1)(-1)} = \frac{-0.75}{-1} = 0.75$$

$$L_2 = \frac{(2.5 - 1)(2.5 - 2)}{(3 - 1)(3 - 2)} = \frac{(1.5)(0.5)}{(2)(1)} = \frac{0.75}{2} = 0.375$$

$$f(2.5) = 0(-0.125) + 1(0.75) + 8(0.375) = 0.75 + 3.0 = 3.75$$

$$\boxed{f(2.5) = 3.75}$$

> [!info] Check against the polynomial and against the original equation
> Newton's divided differences give $f[x_0,x_1] = 1$, $f[x_1,x_2] = 7$ and
> $f[x_0,x_1,x_2] = 3$, so the polynomial is
> $f(x) = 0 + 1(x - 1) + 3(x - 1)(x - 2) = 3x^2 - 8x + 5$. Substituting gives
> $f(2.5) = 3(6.25) - 20 + 5 = 3.75$, agreeing with the Lagrange result, and the
> three basis polynomials sum to $-0.125 + 0.75 + 0.375 = 1$ exactly, as the
> Lagrange basis of a quadratic must. The polynomial also reproduces the table:
> $f(1) = 0$, $f(2) = 1$ and $f(3) = 8$. Two routes, a partition-of-unity
> check and a table-reproduction check all give the same value, so no tabulated
> entry is contradicted and the arithmetic is confirmed.

---

### [2019 Q.4(b)]

**Question.** A robot arm with a rapid laser scanner is doing a quick quality check on holes drilled in a $15'' \times 10''$ rectangular plate. The centers of the holes in the plate describe the path the arm needs to take, and the hole centers are located on a Cartesian coordinate system (with the origin at the bottom left corner of the plate) given by the specifications in the table below. If the leaser is traversing from $x = 2$ to $x = 4.25$ to $x = 5.25$ in a quadratic path, what is the value of the $y$ at $x = 4.00$ using a curve fitting technique.

**Solution.**

The three tabulated points through which the quadratic path passes are

$$(x_0, y_0) = (2, 7.2), \qquad (x_1, y_1) = (4.25, 7.1), \qquad (x_2, y_2) = (5.25, 6.0)$$

Three points determine one quadratic, so the curve-fitting technique is exact
interpolation by a second-degree Lagrange polynomial.

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

> [!info] Check against the fitted polynomial in ordinary form
> Solving for $a, b, c$ in $y = a + bx + cx^2$ through the three points gives
> $c = -\dfrac{38}{117}$, $b = \dfrac{2323}{1170}$, $a = \dfrac{883}{195}$, so
> $y = -\dfrac{38x^2}{117} + \dfrac{2323x}{1170} + \dfrac{883}{195}$.
> Substituting $x = 4$ gives $-\dfrac{608}{117} + \dfrac{9292}{1170} + \dfrac{883}{195} = \dfrac{8510}{1170} = \dfrac{851}{117} = 7.27350427$, the
> same value. An exact fraction and a decimal evaluation agreeing to eight
> digits rules out a rounding loss in the Lagrange arithmetic. As a further
> structural check, $L_0 + L_1 + L_2 = 0.04273504 + 1.11111111 - 0.15384615 = 1$
> exactly, as a quadratic's three Lagrange basis polynomials must.

---

### [2021 Q.3(b)]

**Question.** Differentiate between Newton's interpolation and Lagrange's interpolation.

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

Newton gives an **update** rule, cheap when data arrive incrementally. Lagrange
gives a **construction**, direct, and equally spaced points require no special
case.

$$
\boxed{\text{Newton updates and reuses; Lagrange rebuilds once and is spacing-agnostic}}
$$

---

### [2021 Q.3(d), 2023 Q.2(b)]

**Appeared in:** 2021 Q.3(d), 2023 Q.2(b)

**Question.** Find $y(2)$ from the following data using Lagrange's formula.

**Solution.**

| $x$ | 0 | 1 | 3 | 4 | 5 |
| --- | --: | --: | --: | --: | --: |
| $y$ | 0 | 1 | 81 | 256 | 625 |

**Step 1. The formula.** With five points $x_0 = 0, x_1 = 1, x_2 = 3, x_3 = 4,
x_4 = 5$,

$$
y(2) = \sum_{i=0}^{4} y_i L_i(2), \qquad L_i(2) = \prod_{j \neq i} \frac{2 - x_j}{x_i - x_j}
$$

**Step 2. Compute each weight**, keeping numerator and denominator factors separate.

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

$$
\boxed{y(2) = 16}
$$

> [!info] Check by two independent routes
> **Route 2, Newton's divided difference.** The nodes are **not** equally spaced, so
> divided differences apply. The table is
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

---

### [2024 Q.2(c)]

**Question.** Describe the Lagrange interpolation method. What are its advantages and disadvantages?

**Solution.**

**Idea.** With $n+1$ points $(x_0, y_0), \ldots, (x_n, y_n)$ there is exactly one
polynomial of degree at most $n$ passing through all of them. Lagrange writes
that polynomial directly, as a sum where each term is arranged to be correct at
one point and zero at all the others.

**The formula**

$$
P_n(x) = \sum_{i=0}^{n} y_i L_i(x), \qquad
L_i(x) = \prod_{\substack{j=0 \\ j \neq i}}^{n} \frac{x - x_j}{x_i - x_j}
$$

**Why $L_i$ behaves as it must.** At $x = x_k$ every factor with $k \neq i$ has a
numerator of $x_k - x_k = 0$, so $L_i(x_k) = 0$. At $x = x_i$ every ratio is
$(x_i - x_j)/(x_i - x_j) = 1$, so $L_i(x_i) = 1$. Each term therefore contributes
$y_i$ at its own point and nothing at the others.

**Advantages**

1. No need to solve any equation. The coefficients are written down directly.
2. Unequal spacing is handled with no change to the formula.
3. A new point can be added by adding one term, without rebuilding the rest.
4. It gives an exact fit for any data type, including unevenly spaced samples.

**Disadvantages**

1. Evaluating $P_n$ costs $O(n^2)$ operations, which grows fast.
2. Round off error grows with $n$ and with the distance from the data points.
3. It is unstable for extrapolation. Runge's phenomenon shows large oscillation
   outside the data range.
4. Adding a point changes nothing about the fit quality elsewhere, so it gives no measure
   of whether the model is adequate.

$$
\boxed{P_n(x) = \sum_{i=0}^{n} y_i \prod_{j \neq i} \frac{x - x_j}{x_i - x_j}}
$$

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

**Solution.**

**The result.**

$$y_n(x) = y_0 + p\Delta y_0 + \frac{p(p-1)}{2!}\Delta^2 y_0 + \frac{p(p-1)(p-2)}{3!}\Delta^3 y_0 + \cdots + \frac{p(p-1)(p-2)\cdots(p-n+1)}{n!}\Delta^n y_0$$

with $p = \dfrac{x - x_0}{h}$ and $h$ the common spacing.

**Derivation.**

**Step 1. Set up.** Take $n+1$ equally spaced points $x_i = x_0 + ih$, with
$y_i = f(x_i)$ and $h = x_1 - x_0$. Write the target as $x = x_0 + ph$ so
$p = \frac{x - x_0}{h}$.

**Step 2. Newton's general form.** For arbitrary nodes the interpolating
polynomial is the Newton form

$$P_n(x) = f[x_0] + f[x_0,x_1](x-x_0) + f[x_0,x_1,x_2](x-x_0)(x-x_1) + \cdots$$

where $f[x_i, \dots, x_{i+k}]$ is a **divided difference**, defined
recursively by $f[x_i] = f(x_i)$ and

$$f[x_i, \dots, x_{i+k}] = \frac{f[x_{i+1},\dots,x_{i+k}] - f[x_i,\dots,x_{i+k-1}]}{x_{i+k} - x_i}$$

**Step 3. The special case of equal spacing.** When the nodes are equally spaced
the divided differences collapse onto ordinary finite differences:

$$
f[x_i, x_{i+1}, \dots, x_{i+k}] = \frac{\Delta^k y_i}{k!\,h^k}
$$

This is the key identity. To see why, the first divided difference on equal
steps is $\frac{y_{i+1} - y_i}{h} = \frac{\Delta y_i}{h}$. Each further
divided difference divides the difference of two $k!h^k$ multiples by one more
$h$ and by $k+1$, giving $(k+1)!h^{k+1}$. Induction finishes it.

**Step 4. Substitute into the Newton form.**

$$P_n(x) = y_0 + \frac{\Delta y_0}{1!h}(x-x_0) + \frac{\Delta^2 y_0}{2!h^2}(x-x_0)(x-x_1) + \frac{\Delta^3 y_0}{3!h^3}(x-x_0)(x-x_1)(x-x_2) + \cdots$$

**Step 5. Factor out the $h$.** Since $x - x_i = (p - i)h$, the product
$(x-x_0)(x-x_1)\cdots(x-x_{i-1}) = (p)(p-1)\cdots(p-i+1)h^i$. Substituting, the
$h^i$ in the numerator cancels the $h^i$ in the denominator:

$$
P_n(x) = y_0 + p\,\Delta y_0 + \frac{p(p-1)}{2!}\Delta^2 y_0 + \frac{p(p-1)(p-2)}{3!}\Delta^3 y_0 + \cdots
$$

**Step 6. The final form**, which is the box above.

**Another way to see it.** Expand $f$ in a Taylor series about $x_0$ and replace
each derivative by a finite difference, using $f^{(k)}(x_0) = \frac{\Delta^k y_0}{h^k}$:

$$f(x) = f(x_0) + p\,h f'(x_0) + \frac{p^2}{2!}h^2 f''(x_0) + \frac{p^3}{3!}h^3 f'''(x_0) + \cdots$$

The $h$'s cancel immediately, giving $y_0 + p\Delta y_0 + \frac{p^2}{2!}\Delta^2 y_0 + \cdots$. The
**only** difference from the standard formula is that the $p^2$ has become
$p(p-1)$ and the $p^3$ has become $p(p-1)(p-2)$. That substitution is not a
trick: the finite differences already carry the effect of the lower-order terms,
and replacing rising powers by falling products is what avoids double counting.

**Validity.** Accurate for $0 \le p \le n$, that is inside the table. Near the far
end use backward differences instead, and outside the table the result is an
extrapolation with the risks listed in Q.3(a). Part (b) applies this to unequally
spaced data, where divided differences are used instead.

> [!note] Where this is used again
> The forward form is applied in 2021 Q.4(b) and 2021 Q.4(c), and the backward
> form in 2020 Q.3(b). See
> [[NM-4.7_Newtons_Forward_Difference|NM-4.7 · Newton's Forward Difference]].

---

### [2021 Q.3(c), 2023 Q.2(a)]

**Appeared in:** 2021 Q.3(c), 2023 Q.2(a)

**Question.** Derive the Newton's forward interpolation formula: $y_n(x) = y_0 + p\Delta y_0 + \frac{p(p-1)}{2!}\Delta^2 y_0 + \frac{p(p-1)(p-2)}{3!}\Delta^3 y_0 + \cdots$

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

$$
\boxed{y_n(x) = y_0 + p\Delta y_0 + \frac{p(p-1)}{2!}\Delta^2 y_0 + \frac{p(p-1)(p-2)}{3!}\Delta^3 y_0 + \cdots + \frac{p(p-1)\cdots(p-n+1)}{n!}\Delta^n y_0}
$$

**Validity range.** The formula is accurate for $0 \le p \le 1$, primarily near the beginning of equidistant tables. For values near the end, backward differences are used.

> [!info] Alternate proof via Shift Operator $E$
> Using the relationship $E = 1 + \Delta$:
> $$y(x) = y(x_0 + ph) = E^p y_0 = (1 + \Delta)^p y_0$$
> Expanding $(1 + \Delta)^p$ by the binomial theorem:
> $$(1 + \Delta)^p = 1 + p\Delta + \frac{p(p-1)}{2!}\Delta^2 + \frac{p(p-1)(p-2)}{3!}\Delta^3 + \cdots$$
> Operating on $y_0$ immediately gives the formula.

> [!note] Where this is used again
> Part (d) applies this with $y = x^4$, and 2021 Q.4(b) applies central difference formulas to a table of $e^x$ values. See [[NM-4.7_Newtons_Forward_Difference|NM-4.7 · Newton's Forward Difference]].

---

### [2022 Q.2(c)]

**Question.** Using Newton's forward difference formula find the sum $S_n = 1^3 + 2^3 + 3^3 + \cdots + n^3$.

**Solution.**

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

---

### [2020 Q.5(b)]

**Question.** Using Newton's divided difference interpolating polynomial estimate the value of signal $s(t)$ at $t = 2.25$ sec for the following tabulated values.

**Solution.**

| $t$ | 0.5 | 0.2 | 1.4 | 2.2 | 3.0 |
| --- | --: | --: | --: | --: | --: |
| $s(t)$ | $-10.25$ | $-3.768$ | $5.976$ | $28.972$ | $79.0$ |

> [!warning] The table is printed out of order, and it does not matter
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
> And the product $(t-x_0)(t-x_1)\cdots(t-x_{k-1})$ covers the same set of
> factors whichever order they are listed in. Both halves of the formula are
> unchanged, so the polynomial is unchanged.
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

$$
\boxed{s(2.25) = 30.7336}
$$

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
> gives $30.7336290148$ again, to ten decimals, as the warning above states.

> [!warning] The one choice that would change the answer
> A second reading is available: suppose the *values* were transposed rather than
> the labels, so that $s(0.2) = -10.25$ and $s(0.5) = -3.768$. That reading makes
> the signal **monotonically increasing**, $-10.25, -3.768, 5.976, 28.972, 79.0$,
> which is what a real rising signal looks like, whereas the printed pairing
> makes it dip from $-3.768$ down to $-10.25$ and then climb.
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

**Solution.**

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

---

**Also asked here.**

- *2019 Q.4(b)* is the same question as [[NM-4.6_Lagranges_Interpolation|NM-4.6]], which is written in `NM-4.6`.

---

<a id="nm-410"></a><a id="nm-4.10"></a>
## NM-4.10 · Gauss Forward / Backward & Stirling's Formulas

### [2021 Q.4(b)]

**Question.** From the following table, calculate the value of $e^{1.17}$ using Gauss' forward formula.

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

$$
\boxed{e^{1.17} \approx 3.22199}
$$

> [!info] Check by independent routes
> **Against the true value.** $e^{1.17} = 3.2219926385$, giving an error of only
> $3.04 \times 10^{-6}$. The whole error stems from the 4-decimal rounding in the given table data.
>
> **Lagrange check.** Lagrange on the nearest four points ($1.05, 1.10, 1.15, 1.20$)
> gives $3.2219896$, identical to the third-order central difference result, confirming arithmetic accuracy.

> [!note] Why Gauss' forward formula is chosen over Newton's
> Because $x = 1.17$ lies near the middle of the table, choosing $x_0 = 1.15$ gives
> a small parameter $p = 0.4$ ($0 \le p \le 0.5$). Gauss' forward formula uses the zigzag path
> $y_0 \to \Delta y_0 \to \Delta^2 y_{-1} \to \Delta^3 y_{-1} \to \Delta^4 y_{-2}$, which keeps the
> differences symmetrically clustered around the interpolation point.
> The terms diminish rapidly: $0.0648 \to 0.00095 \to 0.00002 \to 0$, providing superior numerical stability
> compared to computing large powers of $p = 3.4$ from the table edge.

---

<a id="nm-411"></a><a id="nm-4.11"></a>
## NM-4.11 · Difference Table Formation & Applications

### [2017 Q.5(c)]

**Question.** The population of a town in decennial census were as following table in thousand unit. Estimate the population for the year 1955.

**Solution.**

| Year | 1921 | 1931 | 1941 | 1951 | 1961 |
| :---: | :---: | :---: | :---: | :---: | :---: |
| Population (thousands) | 46 | 66 | 81 | 93 | 101 |

**Newton's forward difference formula.** The tabulation interval is $h = 10$.
Taking $x_0 = 1921$, the target $1955$ corresponds to

$$p = \frac{1955 - 1921}{10} = \frac{34}{10} = 3.4$$

**The differences.**

| | 46 | 66 | 81 | 93 | 101 |
| :-- | :-- | :-- | :-- | :-- | :-- |
| $\Delta$ | | 20 | 15 | 12 | 8 |
| $\Delta^2$ | | | $-5$ | $-3$ | $-4$ |
| $\Delta^3$ | | | | 2 | $-1$ |
| $\Delta^4$ | | | | | $-3$ |

**Apply the formula.**

$$y = y_0 + p\Delta y_0 + \frac{p(p-1)}{2}\Delta^2 y_0 + \frac{p(p-1)(p-2)}{6}\Delta^3 y_0 + \frac{p(p-1)(p-2)(p-3)}{24}\Delta^4 y_0$$

$$y = 46 + 3.4(20) + \frac{(3.4)(2.4)}{2}(-5) + \frac{(3.4)(2.4)(1.4)}{6}(2) + \frac{(3.4)(2.4)(1.4)(0.4)}{24}(-3)$$

Term by term:

$$y_0 = 46$$

$$p\Delta y_0 = 3.4 \times 20 = 68$$

$$\frac{p(p-1)}{2}\Delta^2 y_0 = \frac{(3.4)(2.4)}{2}(-5) = 4.08 \times (-5) = -20.4$$

$$\frac{p(p-1)(p-2)}{6}\Delta^3 y_0 = \frac{(3.4)(2.4)(1.4)}{6}(2) = \frac{11.424}{6} \times 2 = 1.904 \times 2 = 3.808$$

$$\frac{p(p-1)(p-2)(p-3)}{24}\Delta^4 y_0 = \frac{(3.4)(2.4)(1.4)(0.4)}{24}(-3) = \frac{4.5696}{24} \times (-3) = 0.1904 \times (-3) = -0.5712$$

Collecting the five terms:

$$y = 46 + 68 - 20.4 + 3.808 - 0.5712 = 96.8368$$

$$\boxed{\text{Population in 1955} \approx 96.8368 \approx 96.84 \text{ thousand}}$$

> [!info] Check by Lagrange and by the neighbouring points
> The Lagrange polynomial through the same five points, evaluated at $x = 1955$,
> gives $96.8368$ exactly, so the two difference routes agree.
> The check also shows why the difference table needs care: $\Delta^4 y_0 = -3$
> is small compared with $\Delta y_0 = 20$, yet its product with
> $\dfrac{p(p-1)(p-2)(p-3)}{24} = 0.1904$ is $-0.5712$, which is large enough to
> move the answer by $0.57$ thousand. Note the sign of that product: $p - 3$ is
> positive at $p = 3.4$, and $\Delta^4 y_0$ is negative, so the correction
> *subtracts*. Dropping the factor $3$ from the multiplier, as the intermediate
> working above once did, changes the answer by $0.38$ thousand.
>
> As a physical check, the census rises by $93$ to $101$ over $1951$–$1961$, so
> linear interpolation alone gives $93 + 0.4(8) = 96.2$ for 1955. The
> difference-form answer $96.8368$ sits above that, which is what the positive
> second differences predict: the population is still accelerating in absolute
> growth even though it is decelerating in percentage terms, so a straight line
> through the decade under-reads the middle years.

---

### [2020 Q.3(b)]

**Question.** The population of a town in the decennial census was as given below. Estimate the population for the year (i) 1895 and (ii) 1925.

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

**Step 2. Observe what the data really are.** The first three differences of
$r^3$ are $3r^2 + 3r + 1$, $6r + 6$, $6$. Here $\Delta y = 96, 216, 384, 480$ grows
by $120, 168, 96$, not by a constant, so this is not a pure cubic in $t$.

Check the natural candidate: $(t+1)(t+2)(t+3)$ gives $24, 120, 336, 720$ for
$t = 1, 3, 5, 7$, exactly matching, but gives $1320$ at $t = 9$, not $1200$.

**The fifth point does not lie on the cubic that the first four define.** This
single fact determines which polynomial the question requires, and it is stated
explicitly rather than resolved by silently choosing one interpretation.

**Step 3(a). Using all five points, cubic through the first four plus one more.**
The unique quartic through all five points, evaluated by Newton's forward formula
with $p = \frac{10-1}{2} = 4.5$:

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

$$
\boxed{\text{Five points (quartic): } y(10) = 1420.6875 \qquad \text{Four points (cubic): } y(10) = 1716}
$$

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
> difference table has settled: $\Delta^4 y = -120$ is not small, so the data are not
> well described by a low-degree polynomial at all, and adding or removing one
> point reshapes the curve. The honest summary is that a sensor whose values grow
> by $300$ to $500$ per two seconds cannot be predicted to better than a few
> percent from five samples.

---

### [2024 Q.3(b)]

**Question.** The population of a town in decennial census were as in the following table in thousand units. Estimate the population for the year 1995.

**Solution.**

| Year | 1921 | 1931 | 1941 | 1951 | 1961 |
| :-- | --: | --: | --: | --: | --: |
| Population (thousands) | 46 | 66 | 81 | 93 | 101 |

**Step 1. Build the difference table.** Take $h = 10$ years and put the years in
steps from 1921, so $u = (x - 1921)/10$ gives $u = 0, 1, 2, 3, 4$.

| $u$ | 0 | 1 | 2 | 3 | 4 |
| --- | ---: | ---: | ---: | ---: | ---: |
| $y$ | 46 | 66 | 81 | 93 | 101 |
| $\Delta y$ | 20 | 15 | 12 | 8 | |
| $\Delta^2 y$ | $-5$ | $-3$ | $-4$ | | |
| $\Delta^3 y$ | 2 | $-1$ | | | |
| $\Delta^4 y$ | $-3$ | | | | |

**Step 2. Newton backward differences at the last point.** The target 1995 lies
**beyond** the table, so work backwards from 1961. The backward differences at
$u = 4$ are the last entry of each row:

$$
\nabla y = 8, \quad \nabla^2 y = -4, \quad \nabla^3 y = -1, \quad \nabla^4 y = -3
$$

**Step 3. Argument.** With $p$ measured in steps of $h$ past the last point,

$$
p = \frac{1995 - 1961}{10} = 3.4
$$

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

> [!info] Check by two independent routes
> **Newton divided difference.** Building the divided difference table from
> $x = 1921, \ldots, 1961$ and evaluating the resulting polynomial at $x = 1995$
> gives $20.1888000000$.
> **Lagrange interpolation.** The sum
> $\sum y_i \prod_{j \neq i} \frac{1995 - x_j}{x_i - x_j}$ over the five points
> gives $20.1887999999$.
> Both match the backward-difference value to nine figures, so the value does
> not depend on the route taken.

> [!warning] Why the extrapolated estimate is not usable
> The formula was applied correctly. The problem is that $p = 3.4$ is far outside
> the data, and the fourth-difference term is large and negative, so it cancels
> most of everything above it. The result predicts a population of 20 thousand in
> 1995, down from 101 thousand in 1961. The data plainly do not say that.
>
> Dropping the highest term shows how unstable it is:
>
> | Terms kept | Result |
> | :-- | --: |
> | $y_n + p\nabla y_n$ | 128.2 |
> | plus $\nabla^2 y$ | 98.28 |
> | plus $\nabla^3 y$ | 84.816 |
> | plus $\nabla^4 y$ | 20.1888 |
>
> Three plausible answers and one implausible one, from the same five data points.
> **Extrapolation more than about one interval past the data is not usable.**
> For a defensible estimate, fit a straight line instead, which is the
> least squares fit in part (c) of the same question.

---

[🏠 Master Index](00_Index.md) | [← Prev Topic: NM-3 · Linear Systems](NM-3_Linear_Systems.md) | [Next Topic: NM-5 · Numerical Integration →](NM-5_Numerical_Integration.md)
