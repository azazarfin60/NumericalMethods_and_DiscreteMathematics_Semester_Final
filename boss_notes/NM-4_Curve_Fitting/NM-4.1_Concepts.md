[← Previous: NM-3.8 Circuit Applications](../NM-3_Linear_Systems/NM-3.8_Circuit_Applications.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: NM-4.2 Linear Regression →](NM-4.2_Linear_Regression.md)

---

# NM-4.1: Curve Fitting Concepts

> 🔴 **Priority:** Critical | **Tested:** 7/8 years | **Typical marks:** 3–4

## What This Is (and Why It Matters)

Imagine you take voltage and current measurements in the lab. Your voltmeter jiggles, your resistor gets warm, and your readings scatter. If you draw a jagged line connecting every single noisy reading, you get an ugly zigzag that makes no physical sense. That is why we need curve fitting: we fit a smooth curve that captures the true underlying physical trend while ignoring the random measurement noise.

The exam loves this subtopic. It has appeared in 7 out of 8 semester finals. Examiners use it as an easy 3 to 4 mark opener, asking you to define and contrast interpolation, extrapolation, and curve fitting, or explain why ECE engineers need them.

---

## 📝 Key Definitions

> **Interpolation:** "Given the set of tabular values $(x_0, y_0), (x_1, y_1), (x_2, y_2), \dots, (x_n, y_n)$ satisfying the relation $y = f(x)$ where the explicit nature of $f(x)$ is not known, it is required to find a simpler function, say $\phi(x)$, such that $f(x)$ and $\phi(x)$ agree *at the set of tabulated points*. Such a process is called *interpolation*." -- Jain, §3.1 (p. 73)
>
> **In simple words:** You have exact data points and you want to find a missing value inside the boundaries of your table. You construct a curve that passes through every known point without missing a single one.

> **Extrapolation:** "Extrapolation is the estimation of a value of a function at a point outside the range of the known data values." -- Jain, §3.1
>
> **In simple words:** You use your existing data points to guess what happens outside the boundaries of your table (either before the first point or after the last point). It is much riskier because curves can shoot off to infinity once they leave your known data.

> **Curve Fitting / Least Squares:** "In experimental work, we often encounter the problem of fitting a curve to data which are subject to errors. The strategy for such cases is to derive an approximating function that *broadly* fits the data without necessarily passing through the given points. The curve drawn is such that the discrepancy between the data points and the curve is least. In the method of least squares, the sum of the squares of the errors is minimized." -- Jain, §4.1 (p. 126)
>
> **In simple words:** You have noisy lab data and you want to discover the general physical law. You do not force the curve through every point. Instead, you find the single smooth curve that sits as close as possible to all points at once.

---

## The Core Idea

Whenever you have a collection of data pairs $(x_i, y_i)$, you must decide what to do based on two questions:
1. Is your data clean and exact, or is it noisy and experimental?
2. Is your target point inside your data range, or outside it?

### The Three Operations at a Glance

| Feature | Interpolation | Extrapolation | Curve Fitting |
| :-- | :-- | :-- | :-- |
| **Target point $x$** | Inside the data span ($x_0 \le x \le x_n$) | Outside the data span ($x < x_0$ or $x > x_n$) | Usually inside the data span |
| **Passes through points?** | Yes, passes through every point exactly | Yes, curve passes through known points | No, passes near points without hitting them |
| **Data nature** | Exact, certified, error-free | Exact, certified | Experimental measurements with noise |
| **Primary goal** | Read missing values between points | Predict future trends beyond points | Discover underlying physical relationships |
| **Reliability** | Very high (data brackets the target) | Low (polynomials diverge rapidly) | High for overall trend |

### Why ECE Engineers Need Curve Fitting

In electrical and computer engineering, curve fitting is indispensable for four clear reasons:

1. **Experimental data always carries noise.** Every real-world sensor reading contains thermal noise, ADC quantization noise, and component tolerance variations. Curve fitting filters out random scatter to reveal the real signal.
2. **Compact mathematical models for simulators.** Circuit simulators like SPICE cannot store tables containing millions of raw lab measurements. They need compact equations with two or three constants (such as diode saturation current $I_s$ or ideality factor $\eta$).
3. **Parameter extraction.** We measure $v\text{--}i$ data to extract resistance $R$, transient capacitor charge curves to extract time constant $\tau = RC$, or frequency response curves to find cutoff frequencies.
4. **Prediction.** A fitted equation lets you predict circuit behavior at operating points that were never explicitly tested in the lab.

### Mathematical Signature of Least Squares

Let your measured points be $(x_i, y_i)$ for $i = 1, 2, \dots, n$. We propose a model $y = f(x)$.

The error (or residual) at each point is:

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

#### The Algebraic Signature of a Straight-Line Fit

For a straight line $y = a + bx$, setting derivatives to zero gives:

$$
\sum y = na + b\sum x
$$

$$
\sum xy = a\sum x + b\sum x^2
$$

These equations enforce three geometric and algebraic properties:
1. **Sum of squared errors is strictly minimized.**
2. **Sum of residuals is exactly zero:** $\sum r_i = 0$. The positive errors above the line cancel the negative errors below the line.
3. **The fitted line passes through the centroid:** Dividing the first normal equation by $n$ gives $\bar{y} = a + b\bar{x}$. The line is anchored at the center of mass $(\bar{x}, \bar{y})$ of the dataset.

> [!WARNING] Common Trap
> Never use high-degree polynomial interpolation on noisy experimental data. Forcing a 6th-degree polynomial through 7 noisy data points causes wild oscillations between points (known as Runge's phenomenon). For noisy data, always use low-degree least-squares curve fitting.

---

## 🏆 Past Exam Questions

### 2017 Q.5(a): Define Interpolation, Extrapolation, and Curve Fitting [03 Marks]

**The question:** Define: (i) Interpolation (ii) Extrapolation (iii) Curve Fitting.

**Let's answer this clearly step by step.**

**(i) Interpolation:** Estimating the value of a function at a target point $x$ that lies **inside** the range covered by known data points ($x_0 < x < x_n$). The interpolating function is required to pass through every tabulated data point exactly ($P(x_i) = y_i$).

**(ii) Extrapolation:** Estimating the value of a function at a target point $x$ that lies **outside** the range of known data points ($x < x_0$ or $x > x_n$). While it uses the same formulas, extrapolation is much less reliable because polynomials can diverge wildly beyond the boundaries of the data.

**(iii) Curve fitting:** Constructing a mathematical function $y = f(x)$ that describes the overall trend of a dataset without being forced to pass through every individual point. It minimizes the total discrepancy between the curve and the data points, which makes it ideal for noisy experimental measurements.

---

### 2019 Q.4(a): Curve Fitting for ECE Engineers & Least Squares Condition [04 Marks]

**The question:** What is curve fitting? Why is it required for ECE engineers? Discuss least square technique condition.

**Let's answer this like a tutor explaining the full picture.**

**What is curve fitting:** Curve fitting is the process of constructing an analytical equation $y = f(x)$ that represents the underlying trend of a dataset $(x_i, y_i)$ without requiring the curve to pass through every individual data point.

**Why it is required for ECE engineers:**
1. **Dealing with noisy measurements:** Physical measurements of voltage, current, power, and gain always contain experimental noise. Curve fitting averages out the noise to isolate the true physical relationship.
2. **Compact device modeling:** Replaces large lookup tables with compact analytic formulas that circuit simulators can evaluate quickly.
3. **Parameter extraction:** Allows engineers to determine physical device parameters (such as resistance from Ohm's law, transconductance, or capacitance) from lab sweeps.
4. **Prediction:** Enables engineers to forecast circuit response between measured points and slightly beyond tested limits.

**Least square technique condition:**
Let the model curve be $y = f(x; a_0, a_1, \dots)$. The residual at point $i$ is $r_i = y_i - f(x_i)$. The condition of least squares requires choosing the parameters such that the sum of squared residuals:

$$
S = \sum_{i=1}^n r_i^2 = \sum_{i=1}^n [y_i - f(x_i)]^2
$$

is minimized. This requires setting the partial derivatives with respect to each parameter to zero:

$$
\frac{\partial S}{\partial a_j} = 0 \quad \text{for all } j
$$

This yields the system of linear normal equations. The fitted curve satisfies three key conditions:
- $\sum r_i^2$ is minimum,
- $\sum r_i = 0$ (residuals sum to zero),
- The fitted line passes through the data centroid $(\bar{x}, \bar{y})$.

---

### 2020 Q.3(a): Main Difference Between Interpolation and Extrapolation [03 Marks]

**The question:** What is the main difference between interpolation and extrapolation? Where are they used?

**Let's break this down.**

**The core difference:**

| Feature | Interpolation | Extrapolation |
| :-- | :-- | :-- |
| Target location | Inside the data span ($x_{\min} \le x \le x_{\max}$) | Outside the data span ($x < x_{\min}$ or $x > x_{\max}$) |
| Curve behavior | Bridges a gap between known points | Extends into the unknown beyond points |
| Reliability | High (bracketed by real data) | Low (errors grow rapidly) |

**Where interpolation is used:**
- Reading intermediate values from certified calibration tables (such as steam tables or thermocouple charts).
- Digital signal reconstruction (reconstructing a continuous audio waveform from discrete digital samples).

**Where extrapolation is used:**
- Forecasting future population census trends or electrical grid load demands.
- Tracking flight paths and missile trajectories beyond the last radar ping.

$$
\boxed{\text{Interpolation fills a gap the data surround; extrapolation guesses past the edge}}
$$

---

### 2021 Q.3(a): When to Use Interpolation Instead of Curve Fitting [03 Marks]

**The question:** When should we use interpolation instead of curve fitting?

**Let's answer this directly.**

Use **interpolation** when both of these conditions are met:
1. **The data is exact and error-free:** Because interpolation forces the curve through every point, any measurement error would be treated as truth and baked into your answer. Use it on mathematical function tables or certified reference tables.
2. **The target point lies strictly between known data points:** The target must be surrounded by data points so the polynomial remains stable.

Use **curve fitting** when the data comes from experimental tests with random measurement noise, when you want to discover the underlying physical law, or when you need a simple compact formula for many data points.

$$
\boxed{\text{Exact data and a target between the points: interpolate. Noisy data: fit.}}
$$

---

### 2021 Q.4(a): Real-Life Example of Curve Fitting [02 Marks]

**The question:** Give a real life example of curve fitting.

**Let's explain with a clear ECE example.**

**Calibrating a temperature sensor (Thermocouple):**
In a calibration lab, a thermocouple is placed in known reference temperature baths ($0^\circ\text{C}, 100^\circ\text{C}, 200^\circ\text{C}, 400^\circ\text{C}$) and the output millivolts are recorded. Because of electronic noise and ambient thermal drift, the millivolt readings fluctuate slightly.

Instead of drawing a jagged interpolation line that copies every microvolt of noise, we use **least-squares curve fitting** to fit a smooth polynomial. This fitted equation provides the clean calibration curve that the microcontroller uses to convert real-time voltage readings into accurate temperatures.

$$
\boxed{\text{Sensor calibration: noisy readings in, a best-fit law out, and predictions follow}}
$$

---

### 2023 Q.4(a): Comparison with Examples [04 Marks]

**The question:** Briefly explain interpolation, extrapolation and curve fitting with examples.

**Let's summarize each with a clear practical example.**

- **Interpolation:** Passes through every given point exactly ($P(x_i) = y_i$). Example: Estimating the speed of sound at $25^\circ\text{C}$ from a standard physics table listing values at $20^\circ\text{C}$ and $30^\circ\text{C}$.
- **Extrapolation:** Evaluates a fitted or interpolating function beyond known limits ($x > x_n$). Example: Predicting next year's peak power demand using historical records from the last ten years.
- **Curve fitting:** Minimizes total error discrepancy $\sum [y_i - f(x_i)]^2$ without passing through every individual point. Example: Determining the resistance of an unknown wire by fitting a straight line to scattered current measurements at different voltages.

$$
\boxed{\text{interpolation passes through, extrapolation goes beyond, fitting minimises}}
$$

---

### 2024 Q.3(a): Operation of Curve Fitting and Interpolation [03 Marks]

**The question:** Discuss the operation of curve fitting and interpolation.

**Let's give the core distinction.**

Both operations transform discrete tabular data into a continuous mathematical relationship, but they serve opposite data conditions:
- **Interpolation** assumes the data points are accurate facts. It forces a polynomial to pass through every coordinate pair to evaluate missing values between points.
- **Curve fitting** assumes the data points are noisy observations of an underlying law. It minimizes the sum of squared deviations so that the curve explains the general behavior without overfitting individual errors.

$$
\boxed{\text{Interpolation reproduces data; curve fitting explains it}}
$$

---

## ⚡ Quick Review

**The core difference in one sentence:** Interpolation passes through every point of clean data; curve fitting finds the best trend through noisy data; extrapolation ventures into the unknown past the data edges.

**The condition you must memorize:**
$$
S = \sum_{i=1}^n [y_i - f(x_i)]^2 \implies \frac{\partial S}{\partial a_j} = 0
$$

**The most common exam mistake:** Recommending interpolation for noisy experimental measurements. Interpolation amplifies noise; curve fitting smooths it out.

**Time estimate in exam:** ~4 minutes for any definition or distinction question.

---

## 🔗 Connected Topics

- [← NM-3.8: Circuit Applications](../NM-3_Linear_Systems/NM-3.8_Circuit_Applications.md) -- solving circuit matrices from physical networks.
- [→ NM-4.2: Linear Regression](NM-4.2_Linear_Regression.md) -- deriving and applying the straight-line least squares formulas.
- [NM-4.6: Lagrange Interpolation](NM-4.6_Lagrange_Interpolation.md) -- the premier exact polynomial interpolation method for uneven data.

---

[← Previous: NM-3.8 Circuit Applications](../NM-3_Linear_Systems/NM-3.8_Circuit_Applications.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: NM-4.2 Linear Regression →](NM-4.2_Linear_Regression.md)
