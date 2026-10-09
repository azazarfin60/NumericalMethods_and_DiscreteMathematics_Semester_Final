[← Previous: NM-3_Lower Systems of Linear Equations](NM-3_Lower_Gauss_Elim_LU_Jacobi_Relaxation.md) | [🏠 Index](00_Index.md) | [Next: NM-4.2 Least Squares Linear Regression →](NM-4.2_Least_Squares_Linear_Regression.md)

---

# NM-4.1: Curve Fitting Concepts
> **Section:** A (Numerical Methods) | **Priority:** 🔴 | **Exam Frequency:** 7/8 years
> **Sources:** Jain Ch.3 §3.1, Ch.4 §4.1; Fahad Notes Class-05; Raidah Notes p.8-9

## Why This Topic Matters

This topic appears in 7 out of 8 exam papers. It tests core definitions, conceptual distinctions, and engineering relevance. The questions are straightforward and offer easy marks. You must know how interpolation, extrapolation, and curve fitting differ, and when to use each one.

---

## 📝 Key Definitions

> **Interpolation:** "Given the set of tabular values $(x_0, y_0), (x_1, y_1), (x_2, y_2), \dots, (x_n, y_n)$ satisfying the relation $y = f(x)$ where the explicit nature of $f(x)$ is not known, it is required to find a simpler function, say $\phi(x)$, such that $f(x)$ and $\phi(x)$ agree *at the set of tabulated points*. Such a process is called *interpolation*." — Jain, §3.1 (p. 73)

> **Curve Fitting / Least Squares:** "In experimental work, we often encounter the problem of fitting a curve to data which are subject to errors. The strategy for such cases is to derive an approximating function that *broadly* fits the data without necessarily passing through the given points. The curve drawn is such that the discrepancy between the data points and the curve is least. In the method of least squares, the sum of the squares of the errors is minimized." — Jain, §4.1 (p. 126)

> **Extrapolation:** "Extrapolation is the estimation of a value of a function at a point outside the range of the known data values." — [paraphrased from Jain §3.1]

---

## Core Theory: The Three Fundamental Operations

Numerical analysis handles discrete data points $(x_i, y_i)$. Depending on the accuracy of the data and the location of the target point, we choose one of three operations.

### 1. Interpolation vs. Extrapolation vs. Curve Fitting

| Feature | Interpolation | Extrapolation | Curve Fitting |
| :-- | :-- | :-- | :-- |
| **Target point $x$** | Inside range ($x_0 \le x \le x_n$) | Outside range ($x < x_0$ or $x > x_n$) | Usually inside range |
| **Passes through data points?** | Yes, passes through every point exactly | Yes, curve passes through known points | No, misses individual noisy points |
| **Assumed data nature** | Exact, noise-free | Exact, noise-free | Noisy, experimental data with error |
| **Goal** | Find missing values within known bounds | Predict trends beyond known data | Find an underlying physical law |
| **Reliability** | High; data bracket the target | Low; polynomial diverges rapidly | High for overall trend |

### 2. Why ECE Engineers Need Curve Fitting

In electrical and computer engineering, measurements come from physical sensors and circuits. Curve fitting is needed for four practical reasons:

1. **Experimental data carry noise.** Sensor readings like voltage, current, and temperature always carry thermal drift and instrument noise. Curve fitting averages out random fluctuations and uncovers the underlying physical signal.
2. **Compact mathematical models.** Simulators need compact analytic equations rather than tables of thousands of data points. A fitted line or curve compresses data into two or three constants.
3. **Parameter extraction.** Engineers extract physical constants by fitting measured data to known laws. Examples include determining resistance from $v\text{--}i$ data, time constants from RC transient curves, and diode parameters.
4. **Prediction.** A fitted equation allows engineers to estimate output values between measurements and slightly beyond test boundaries.

### 3. General Techniques of Curve Fitting

Exam questions ask for two general techniques:

1. **Least squares regression.** Used for noisy experimental data. We choose parameters of a model function $y = f(x)$ to minimize the sum of squared residuals. The curve captures the trend without passing through every point.
2. **Exact polynomial interpolation.** Used for error-free or highly precise tabulated data. We construct a polynomial of degree $n$ through $n+1$ points (using Lagrange or Newton formulas). The polynomial passes through every point.

### 4. Mathematical Conditions for Least Squares

Let the measured data be $(x_i, y_i)$ for $i = 1, 2, \dots, n$. We propose a model curve $y = f(x; a_0, a_1, \dots)$.

The residual at point $i$ is:

$$
r_i = y_i - f(x_i)
$$

The sum of squared residuals is:

$$
S = \sum_{i=1}^n r_i^2 = \sum_{i=1}^n [y_i - f(x_i)]^2
$$

To minimize $S$, we set each partial derivative with respect to the unknown parameters to zero:

$$
\frac{\partial S}{\partial a_0} = 0, \quad \frac{\partial S}{\partial a_1} = 0, \quad \dots
$$

These equations are called the **normal equations**.

#### The Algebraic Signature of Least Squares

For a straight line $y = a + bx$, setting $\frac{\partial S}{\partial a} = 0$ and $\frac{\partial S}{\partial b} = 0$ yields two normal equations:

$$
\sum y = na + b\sum x
$$

$$
\sum xy = a\sum x + b\sum x^2
$$

These equations enforce three algebraic properties:

1. **Minimum sum of squares:** $\sum r_i^2$ is strictly minimized.
2. **Zero sum of residuals:** $\sum r_i = 0$. Positive and negative errors cancel out completely.
3. **Orthogonality:** $\sum x_i r_i = 0$. The residuals are uncorrelated with the independent variable.
4. **Centroid condition:** Dividing $\sum y = na + b\sum x$ by $n$ gives $\bar{y} = a + b\bar{x}$. The fitted line passes through the centroid $(\bar{x}, \bar{y})$ of the data points.

### 5. When to Choose Interpolation over Curve Fitting

Use **interpolation** when both conditions hold:
- The data are exact and noise-free (such as mathematical tables or certified standards).
- The target point lies strictly within the interval of given points.

Use **curve fitting** when:
- The data are experimental measurements with random noise.
- A compact functional relationship is needed.
- You have many data points and want a simple low-degree model.

---

## 🏆 Golden Questions (Past Exam Archive)

### 🎯 Define: (i) Interpolation (ii) Extrapolation (iii) Curve Fitting.
> **Appeared:** 2017 Q.5(a) — (03 marks)

**Full Answer:**

**(i) Interpolation** is the estimation of a value of a function at a point **within** the range covered by a set of known values. The estimated value is obtained from the known values alone, and the interpolation curve passes exactly through them. For a table covering $[x_0, x_n]$, a target $x$ with $x_0 < x < x_n$ is interpolated.

**(ii) Extrapolation** is the estimation of a value at a point **outside** the range of the known data, so $x > x_n$ or $x < x_0$. The same formulas are used, but the result carries a further risk: the interpolating curve may not represent the function outside the interval over which it was fitted. Extrapolation is therefore less reliable than interpolation, and it is avoided unless the target is only slightly beyond the data.

**(iii) Curve fitting** is the construction of an equation $y = f(x)$ that describes the trend of a set of data points, without requiring that the curve pass through any of them. Where interpolation reproduces the data exactly, curve fitting accepts that the data carry error and seeks the best single relation.

**The distinction between the three:** All three estimate values from data. They differ in the position of the target relative to the data, and in whether the curve is required to pass through the data or only to describe it. Interpolation is inside the data and exact through it; extrapolation is outside it; curve fitting is inside it but need not pass through it.

---

### 🎯 What is curve fitting? Why is it required for ECE engineers? Discuss least square technique condition.
> **Appeared:** 2019 Q.4(a) — (04 marks)

**Full Answer:**

**Curve fitting** is the construction of an equation $y = f(x)$ that represents the trend of a set of data points $(x_i, y_i)$. Where interpolation forces the curve through every point, curve fitting accepts that the points carry error and seeks a single relation that describes the whole set.

**Why it is required for ECE engineers:**

1. **Data are noisy.** A voltage, a gain, a delay, or a bit-error rate measured repeatedly gives scattered values. Fitting an underlying law separates the trend from the scatter and quantifies the scatter.
2. **A compact model is wanted.** A characteristic measured at ten points is replaced by two or three constants, which is what a simulator and a hand calculation both use.
3. **Values must be predicted** where no measurement exists, inside and immediately outside the measured range.
4. **Parameters must be extracted.** Resistance, inductance, time constant, cut-off frequency, and beta are all obtained by fitting the measured response to the known equation of the device.

**Least squares technique condition:** Let the trial curve be $y = a_0 + a_1 x + \dots + a_m g_m(x)$. The residual at point $i$ is $r_i = y_i - f(x_i)$. The coefficients are chosen to minimize the sum of squared residuals:

$$
S = \sum_{i=1}^n r_i^2 = \sum_{i=1}^n [y_i - f(x_i)]^2
$$

The conditions are obtained by setting each partial derivative to zero:

$$
\frac{\partial S}{\partial a_0} = 0, \quad \frac{\partial S}{\partial a_1} = 0, \quad \dots
$$

which gives the normal equations. For the straight line $y = a + bx$:

$$
\sum y = na + b\sum x, \qquad \sum xy = a\sum x + b\sum x^2
$$

Setting the derivatives to zero locates the stationary point of $S$. The second derivatives are positive there, confirming a minimum.

**The least-squares condition, stated fully:** Of all curves in the chosen family, the least squares curve is the one for which the residuals satisfy:
- $\sum r_i^2$ is a minimum,
- $\sum r_i = 0$ (the positive and negative residuals cancel),
- $\sum x_i r_i = 0$ (the residuals are orthogonal to the regressor).

The fitted line passes through the centroid $(\bar{x}, \bar{y})$.

---

### 🎯 Define interpolation and extrapolation. List two general techniques of curve fitting.
> **Appeared:** 2019 Q.5(a) — (03 marks)

**Full Answer:**

**Interpolation** is the estimation of an intermediate value of a function from a set of known values, at a point **within** the range covered by the known data. **Extrapolation** is the estimation of a value at a point **outside** that range. Interpolation is bounded by the data; extrapolation extends beyond it.

For a table covering $[x_0, x_n]$, a target $x$ with $x_0 < x < x_n$ is interpolated; a target with $x > x_n$ or $x < x_0$ is extrapolated. Extrapolation carries the risk that the fitted relation may not hold outside the sampled interval.

**Two general techniques of curve fitting:**

1. **Least squares fitting.** A curve $y = a + bx + \dots$ is fitted by choosing its coefficients to minimize $\sum r_i^2$, the sum of squared residuals. The curve does not pass through the points, but captures the trend. It is appropriate for noisy data.
2. **Exact interpolation fitting.** A curve is made to pass through every tabulated point, using divided differences or Lagrange polynomials. It reproduces the data exactly and is appropriate when the data are error-free.

---

### 🎯 What is the main difference between interpolation and extrapolation? Where are they used?
> **Appeared:** 2020 Q.3(a) — (03 marks)

**Full Answer:**

**The difference:**

| Feature | Interpolation | Extrapolation |
| :-- | :-- | :-- |
| Target $x$ | **Inside** the data range, $x_{\min} \le x \le x_{\max}$ | **Outside** it |
| What the curve is doing | Bridging a known span | Continuing past the last data point |
| Reliability | High, data surround the target | **Low**, polynomial is unsupported there |
| Typical error | Small | Grows rapidly with distance |
| What it assumes | Function is smooth in the region | Function stays smooth **outside** the region |

**The reason extrapolation is risky:** A polynomial of degree $n$ through $n+1$ points matches the data exactly and says nothing beyond the last node. The error term is:

$$
f(x) - P_n(x) = \frac{f^{(n+1)}(\xi)}{(n+1)!}\prod_{i=0}^n (x - x_i)
$$

Outside the range, that product grows rapidly, while the data provide no control over $f^{(n+1)}$.

**Where interpolation is used:**
- Reading intermediate values off mathematical tables (trigonometric, Bessel functions).
- Reading density or steam tables in engineering standards.
- Reconstructing an analog signal from discrete digital samples.

**Where extrapolation is used:**
- Forecasting future trends (population projections, energy demand forecasts).
- Continuing a flight trajectory in time from sampled tracking positions.
- Using a Taylor series expansion about a known point.

$$
\boxed{\text{Interpolation fills a gap the data surround; extrapolation guesses past the edge}}
$$

---

### 🎯 When should we use interpolation instead of curve fitting?
> **Appeared:** 2021 Q.3(a) — (03 marks)

**Full Answer:**

Apply **interpolation** when the data are **exact** and the target lies **between** the given points.

Two conditions must both hold:

1. **The data are exact.** Interpolation forces the curve through every point, so any measurement error is copied into the answer.
2. **The target lies inside the data range.** Outside the range the method becomes extrapolation, which is far less trustworthy.

Typical situations: reading values off mathematical function tables, consulting certified standard tables, or working with a small set of exact physical constants.

Apply **curve fitting** when the data carry measurement error, when the underlying trend is the primary goal, or when a simple lower-degree equation is wanted from many scattered data points.

$$
\boxed{\text{Exact data and a target between the points: interpolate. Noisy data: fit.}}
$$

---

### 🎯 Give a real life example of curve fitting.
> **Appeared:** 2021 Q.4(a) — (02 marks)

**Full Answer:**

**Calibrating a thermocouple.**

A calibration certificate lists certified reference temperatures and the corresponding measured voltages:

| Reference Temperature ($^{\circ}$C) | Indicated Output (mV) |
| --: | --: |
| 0 | 0.00 |
| 100 | 4.09 |
| 200 | 7.33 |
| 400 | 12.45 |

The voltage readings carry thermal drift and electronic noise, so no simple curve passes exactly through all points. Fitting a polynomial by **least squares** finds the curve that comes closest to all points. The fitted curve then calibrates the instrument: an unknown reading of $9.20\text{ mV}$ converts directly to a reliable temperature estimate.

A second example is a **tensile load-extension test**, where measured stress and strain scatter due to material non-uniformity. The fitted line yields the elastic modulus (Young's modulus).

**Why fitting rather than interpolation:** The reference points are known only within instrument tolerance ($\pm 0.5^{\circ}\text{C}$). Interpolation would force the curve through every error, copying noise into every calculation. Least squares smooths out the scatter.

$$
\boxed{\text{Sensor calibration: noisy readings in, a best-fit law out, and predictions follow}}
$$

---

### 🎯 Explain a real life application of curve-fitting. For what type of data points will you use Lagrange's interpolation formula?
> **Appeared:** 2022 Q.1(c) — (03 marks)

**Full Answer:**

**A real application of curve fitting:** Calibrating a sensor, such as a thermocouple, against certified reference temperatures. The measured voltages carry thermal drift and instrument noise. Fitting a polynomial by least squares finds the best approximating curve, which is then used to convert measured millivolts into temperature.

**When to use Lagrange's interpolation formula:** Use it when all four conditions hold:

1. **The data are exact**, with zero or negligible noise. Interpolation forces the curve through every point.
2. **The points are few.** Two points give a line, three give a parabola. With many points, high-degree polynomial interpolation oscillates wildly (Runge's phenomenon).
3. **The spacing is unequal or irregular.** Lagrange requires no common step size $h$, whereas Newton's forward and backward formulas require equal spacing.
4. **The target lies between the points.** The target must fall inside the range of known values.

| Situation | Recommended Method |
| :-- | :-- |
| Few, exact, irregularly spaced points | **Lagrange interpolation** |
| Many, equally spaced, exact, near table start | Newton forward difference |
| Many, equally spaced, exact, near table end | Newton backward difference |
| Noisy experimental data, any spacing | Least squares regression |
| Target lies outside data boundaries | Least squares trend model |

---

### 🎯 Briefly explain interpolation, extrapolation and curve fitting with examples.
> **Appeared:** 2023 Q.4(a) — (04 marks)

**Full Answer:**

All three take discrete data and produce a continuous relation. They differ in what they promise:

**Interpolation:** Build a function that passes through **every** given point exactly:

$$
P(x_i) = y_i \quad \text{for every } i
$$

The result is exact at the sample points. Example: a temperature sensor is calibrated at $0^{\circ}\text{C}$ and $100^{\circ}\text{C}$, and its reading at $37^{\circ}\text{C}$ is evaluated by interpolating between the two reference points.

**Extrapolation:** Evaluate an interpolating or fitted function **outside** the range of known data points ($x < x_0$ or $x > x_n$). Example: forecasting next year's sales from five past years of data. The fit matches historical records but carries risk when projected forward.

**Curve fitting:** Find the function that comes **closest** to all data points without passing through any individual point, by minimizing total error like $\sum [y_i - f(x_i)]^2$. Example: fitting a straight line through seven noisy current measurements to determine a wire's resistance.

| Comparison | Interpolation | Extrapolation | Curve Fitting |
| :-- | :-- | :-- | :-- |
| Passes through points | Yes | May or may not | No |
| Outside data span | Not defined | Defined, unreliable | Defined, depends on model |
| Data assumed | Exact | Exact | Noisy |
| Number of points | Needs $n+1$ points for degree $n$ | Same | Can use many points for low degree |

$$
\boxed{\text{interpolation passes through, extrapolation goes beyond, fitting minimises}}
$$

---

### 🎯 Discuss the operation of curve fitting and interpolation.
> **Appeared:** 2024 Q.3(a) — (03 marks)

**Full Answer:**

Both operations take discrete data and generate a smooth relation, but they address different data characteristics:

**Interpolation:** Finds a function $P(x)$ that satisfies $P(x_i) = y_i$ for all $i = 0, 1, \dots, n$. It forces the curve through every point. Use interpolation when the data are accurate and values are needed between known sample nodes. Example: evaluating values between points in a standard mathematical table.

**Curve fitting:** Finds a function $f(x)$ that describes the overall trend without passing through every individual point. It minimizes the sum of squared residuals:

$$
S = \sum_{i=1}^n [y_i - f(x_i)]^2
$$

Use curve fitting when data come from physical measurements with experimental noise. Example: finding the resistance of a resistor from scattered voltage and current readings.

$$
\boxed{\text{Interpolation reproduces data; curve fitting explains it}}
$$

---

## ⚡ Exam Tips & Common Mistakes

1. **State the three-way distinction clearly.** When asked to distinguish interpolation, extrapolation, and curve fitting, structure your answer by target position (inside vs. outside) and curve behavior (passes through vs. misses points).
2. **Never recommend interpolation for noisy data.** If the question describes physical sensor data with measurement error, state that interpolation is wrong because it amplifies noise. Curve fitting is the correct choice.
3. **Remember the least-squares signature.** If asked for the conditions of least squares, list both normal equations and the three geometric properties: sum of squared residuals is minimized, sum of residuals is zero, and the line passes through $(\bar{x}, \bar{y})$.
4. **Extrapolation warning.** Always note that polynomial extrapolation carries high risk because higher-order polynomials diverge rapidly outside the sampled interval.

## 🔗 Related Topics

- [NM-4.2: Least-Squares Linear Regression](NM-4.2_Least_Squares_Linear_Regression.md) — fitting a straight line $y = a + bx$ to experimental data
- [NM-4.3: Non-Linear Regression](NM-4.3_Non_Linear_Regression.md) — linearizing exponential and reciprocal models
- [NM-4.6: Lagrange's Interpolation](NM-4.6_Lagranges_Interpolation.md) — exact polynomial interpolation for unevenly spaced data
- [NM-4_Lower: Regression Theory & Interpolation Methods](NM-4_Lower_Regression_Theory_Interpolation_Methods.md) — regression criteria, divided differences, and central formulas

---

[← Previous: NM-3_Lower Systems of Linear Equations](NM-3_Lower_Gauss_Elim_LU_Jacobi_Relaxation.md) | [🏠 Index](00_Index.md) | [Next: NM-4.2 Least Squares Linear Regression →](NM-4.2_Least_Squares_Linear_Regression.md)
