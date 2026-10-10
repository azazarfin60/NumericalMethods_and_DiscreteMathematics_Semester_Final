[← Previous: NM-4.2 Least Squares Linear Regression](NM-4.2_Least_Squares_Linear_Regression.md) | [🏠 Index](00_Index.md) | [Next: NM-4.6 Lagrange's Interpolation →](NM-4.6_Lagranges_Interpolation.md)

---

# NM-4.3: Non-Linear Regression
> **Section:** A (Numerical Methods) | **Priority:** 🔴⚠️ | **Exam Frequency:** 3/8 years
> **Sources:** Jain Ch.4 §4.2.3 (p. 130–132); Absent from Class Notes (Danger Zone!)

## Why This Topic Matters

Non-linear regression was omitted from class lectures, yet it appeared in 3 semester final exams. The exam questions ask students to fit exponential and reciprocal curves by linearizing them first. If you know the algebraic transformation into a straight line, these questions become straightforward linear regression problems.

---

## 📝 Key Definitions

> **Linearization of Nonlinear Laws:** "The given data may not always follow a linear relationship. This can be ascertained from a plot of the given data. If a nonlinear model is to be fitted, it can be conveniently transformed to a linear relationship." — Jain, §4.2.3 (p. 130)

> **Exponential Law:** "In this case, we write $\ln y = \ln a + bx \Rightarrow Y = A_0 + A_1 X$, where $Y = \ln y$, $A_0 = \ln a$, $A_1 = b$ and $X = x$." — Jain, §4.2.3 (p. 131)

---

## Core Theory: Linearization Techniques for Non-Linear Laws

Most experimental engineering relationships are non-linear. Direct non-linear optimization requires iterative solvers. But many common mathematical laws can be transformed into a linear form $Y = A + BX$ through suitable variable transformations.

### 1. Common Non-Linear Laws and Their Transformations

| Non-Linear Model | Transformation | Linear Variables | Parameters Recovered |
| :-- | :-- | :-- | :-- |
| **Exponential:** $y = ae^{bx}$ | Take natural logarithm: $\ln y = \ln a + bx$ | $Y = \ln y$, $X = x$ | $b = B$, $a = e^A$ |
| **Reciprocal / Saturation:** $y = \dfrac{x}{a + bx}$ | Take reciprocals: $\dfrac{1}{y} = a\left(\dfrac{1}{x}\right) + b$ | $v = \dfrac{1}{y}$, $u = \dfrac{1}{x}$ | Slope $= a$, Intercept $= b$ |
| **Power law:** $y = ax^b$ | Take base-10 log: $\log_{10} y = \log_{10} a + b\log_{10} x$ | $Y = \log_{10} y$, $X = \log_{10} x$ | $b = B$, $a = 10^A$ |
| **General exponential:** $y = ab^x$ | Take base-10 log: $\log_{10} y = \log_{10} a + x\log_{10} b$ | $Y = \log_{10} y$, $X = x$ | $b = 10^B$, $a = 10^A$ |
| **Rational sum:** $y = ax + \dfrac{b}{x}$ | Multiply by $x$: $xy = ax^2 + b$ | $Y = xy$, $X = x^2$ | Slope $= a$, Intercept $= b$ |

### 2. General Procedure for Linearized Regression

1. **Transform the coordinates.** Create transformed variables, such as $X_i = x_i$ and $Y_i = \ln y_i$, or $u_i = 1/x_i$ and $v_i = 1/y_i$.
2. **Form the calculation table.** Compute transformed values and summary sums: $\sum X$, $\sum Y$, $\sum X^2$, $\sum XY$.
3. **Fit the straight line.** Use the standard linear regression formulas:

$$
B = \frac{n\sum XY - \sum X\sum Y}{n\sum X^2 - (\sum X)^2}
$$

$$
A = \bar{Y} - B\bar{X}
$$

4. **Invert the transformation.** Recover original model parameters (for example, $a = e^A$ and $b = B$).
5. **State the final equation.** Write the non-linear formula with the numerical constants inserted.

---

## Worked Example (PYQ 2017 Q.5(b) / 2020 Q.3(c))

Determine constants $a$ and $b$ by the method of least squares such that $y = a e^{bx}$ fits the following data:

| $x$ | 2 | 4 | 6 | 8 | 10 |
| :---: | :---: | :---: | :---: | :---: | :---: |
| $y$ | 4.077 | 11.084 | 30.128 | 81.897 | 222.62 |

**Step 1: Linearise the Equation**

Take natural logarithms of both sides:

$$
\ln y = \ln a + bx
$$

Define transformed variables:

$$
Y = \ln y, \quad A = \ln a, \quad X = x
$$

The model becomes the linear equation:

$$
Y = A + bx
$$

Once $A$ is found, we recover $a = e^A$.

**Step 2: Transformed Data Table ($n = 5$)**

| $x$ | $y$ | $Y = \ln y$ | $x^2$ | $xY$ |
| :--: | :--: | :--: | :--: | :--: |
| 2 | 4.077 | 1.405361 | 4 | 2.810722 |
| 4 | 11.084 | 2.405503 | 16 | 9.622012 |
| 6 | 30.128 | 3.405455 | 36 | 20.432730 |
| 8 | 81.897 | 4.405462 | 64 | 35.243696 |
| 10 | 222.620 | 5.405466 | 100 | 54.054660 |
| **$\sum x = 30$** | — | **$\sum Y = 17.027248$** | **$\sum x^2 = 220$** | **$\sum xY = 122.163825$** |

Notice that the values of $Y = \ln y$ increase by almost exactly $1.0000$ for each step of $\Delta x = 2$. This reveals an underlying exponential relationship.

**Step 3: Solve for Slope $b$ and Intercept $A$**

$$
b = \frac{n\sum xY - \sum x\sum Y}{n\sum x^2 - (\sum x)^2} = \frac{5(122.163825) - (30)(17.027248)}{5(220) - 30^2}
$$

$$
b = \frac{610.819124 - 510.817430}{1100 - 900} = \frac{100.001694}{200} = 0.50001
$$

Now calculate the intercept $A = \ln a$:

$$
\bar{x} = \frac{30}{5} = 6.0, \quad \bar{Y} = \frac{17.027248}{5} = 3.405450
$$

$$
A = \ln a = \bar{Y} - b\bar{x} = 3.405450 - (0.50001)(6.0) = 3.405450 - 3.000052 = 0.405398
$$

Recover $a$:

$$
a = e^{0.405398} = 1.4999 \approx 1.50
$$

**Step 4: Ratio Inspection Check**

Take ratios of successive $y$ values:

$$
\frac{222.62}{81.897} = 2.7183 = e, \quad \frac{81.897}{30.128} = 2.7183 = e, \quad \frac{30.128}{11.084} = 2.7182 \approx e
$$

Every time $x$ increases by $2$, $y$ is multiplied by $e$. Thus:

$$
\frac{y(x+2)}{y(x)} = e^{2b} = e \implies 2b = 1 \implies b = 0.5
$$

$$
a = y(2)e^{-0.5(2)} = 4.077 e^{-1} = 1.4998 \approx 1.50
$$

Both least squares and the direct ratio check agree:

$$
\boxed{a = 1.50, \qquad b = 0.5}
$$

---

## Exam Variants

| Year | Function to Fit | Data Provided | Key Result |
| :---| :---| :---| :---|
| 2017 Q.5(b) / 2020 Q.3(c) | $y = a e^{bx}$ | $(2, 4.077), (4, 11.084), (6, 30.128), (8, 81.897), (10, 222.62)$ | $\boxed{a = 1.50, \qquad b = 0.5}$ |
| 2022 Q.2(b) | $y = \dfrac{x}{a + bx}$ | $(3, 7.148), (5, 10.231), (8, 13.509), (12, 16.434)$ | $\boxed{y = \frac{x}{0.3162 + 0.0345x}}$ |

---

## 🏆 Golden Questions (Past Exam Archive)

### 🎯 Determine the constants $a$ & $b$ by the method of least squares such that $y = a e^{bx}$ fits the following data.
> **Appeared:** 2017 Q.5(b), 2020 Q.3(c) — (04 marks)

**Full Answer:**

Given data:

| $x$ | 2 | 4 | 6 | 8 | 10 |
| :---: | :---: | :---: | :---: | :---: | :---: |
| $y$ | 4.077 | 11.084 | 30.128 | 81.897 | 222.62 |

**Linearise the model:** Taking natural logarithms of $y = ae^{bx}$:

$$
\ln y = \ln a + bx
$$

This represents a straight line $Y = A + bx$, where $Y = \ln y$ and $A = \ln a$.

**Transformed data table ($n = 5$):**

| $x$ | $y$ | $Y = \ln y$ |
| :--: | :--: | :--: |
| 2 | 4.077 | 1.405361 |
| 4 | 11.084 | 2.405503 |
| 6 | 30.128 | 3.405455 |
| 8 | 81.897 | 4.405462 |
| 10 | 222.62 | 5.405466 |

Summing the columns:

$$
\sum x = 30, \qquad \sum Y = 17.027248, \qquad \sum xY = 122.163825, \qquad \sum x^2 = 220
$$

Compute slope $b$:

$$
b = \frac{n\sum xY - \sum x\sum Y}{n\sum x^2 - (\sum x)^2} = \frac{5(122.163825) - (30)(17.027248)}{5(220) - 900} = \frac{610.819124 - 510.817430}{200} = 0.50001
$$

Compute intercept $A = \ln a$:

$$
\ln a = \bar{Y} - b\bar{x} = \frac{17.027248}{5} - 0.50001\left(\frac{30}{5}\right) = 3.405450 - 3.000052 = 0.405398
$$

$$
a = e^{0.405398} = 1.4999 \approx 1.50
$$

The data was generated from the exact exponential $y = 1.5e^{0.5x}$. The constants are:

$$
\boxed{a = 1.50, \qquad b = 0.5}
$$

**Fit comparison table:**

| $x$ | $y$ given | $y$ fitted $= 1.5e^{0.5x}$ |
| :--: | :--: | :--: |
| 2 | 4.077 | 4.077 |
| 4 | 11.084 | 11.083 |
| 6 | 30.128 | 30.128 |
| 8 | 81.897 | 81.897 |
| 10 | 222.620 | 222.620 |

---

### 🎯 Using the method of least squares, fit a curve of the form $y = \frac{x}{a + bx}$ to fit the following data $(3, 7.148)$, $(5, 10.231)$, $(8, 13.509)$, $(12, 16.434)$.
> **Appeared:** 2022 Q.2(b) — (04 marks)

**Full Answer:**

Given four data points:

$$
(3, 7.148), \quad (5, 10.231), \quad (8, 13.509), \quad (12, 16.434)
$$

**Step 1: Linearise the model.** Take the reciprocal of both sides:

$$
\frac{1}{y} = \frac{a + bx}{x} = \frac{a}{x} + b = a\left(\frac{1}{x}\right) + b
$$

Define transformed variables:

$$
u = \frac{1}{x}, \qquad v = \frac{1}{y}
$$

The equation becomes the linear form:

$$
v = au + b
$$

Notice that in this transformed line:
- The **slope** is $a$.
- The **intercept** is $b$.

**Step 2: Table of transformed data ($n = 4$):**

| $x$ | $y$ | $u = 1/x$ | $v = 1/y$ |
| --: | --: | --: | --: |
| 3 | 7.148 | 0.333333 | 0.139899 |
| 5 | 10.231 | 0.200000 | 0.097742 |
| 8 | 13.509 | 0.125000 | 0.074025 |
| 12 | 16.434 | 0.083333 | 0.060849 |

**Step 3: Summary sums:**

$$
\sum u = 0.333333 + 0.200000 + 0.125000 + 0.083333 = 0.741667
$$

$$
\sum v = 0.139899 + 0.097742 + 0.074025 + 0.060849 = 0.372516
$$

$$
\sum u^2 = (0.333333)^2 + (0.200000)^2 + (0.125000)^2 + (0.083333)^2 = 0.173681
$$

$$
\sum uv = (0.333333)(0.139899) + (0.2)(0.097742) + (0.125)(0.074025) + (0.083333)(0.060849) = 0.080505
$$

**Step 4: Normal equations for $v = au + b$:**

1. $nb + a\sum u = \sum v \implies 4b + 0.741667a = 0.372516$
2. $b\sum u + a\sum u^2 = \sum uv \implies 0.741667b + 0.173681a = 0.080505$

Solve for slope $a$:

$$
a = \frac{n\sum uv - \sum u\sum v}{n\sum u^2 - (\sum u)^2} = \frac{4(0.080505) - (0.741667)(0.372516)}{4(0.173681) - (0.741667)^2}
$$

$$
a = \frac{0.322022 - 0.276282}{0.694722 - 0.550069} = \frac{0.045739}{0.144653} = 0.316200
$$

Solve for intercept $b$:

$$
\bar{u} = \frac{0.741667}{4} = 0.185417, \qquad \bar{v} = \frac{0.372516}{4} = 0.093129
$$

$$
b = \bar{v} - a\bar{u} = 0.093129 - (0.316200)(0.185417) = 0.093129 - 0.058629 = 0.034500
$$

Inserting $a = 0.3162$ and $b = 0.0345$ into the original function gives:

$$
\boxed{y = \frac{x}{0.3162 + 0.0345x}}
$$

**Residual verification:**

| $x$ | $y$ actual | $\hat{y} = \dfrac{x}{0.3162 + 0.0345x}$ | Residual $y - \hat{y}$ |
| --: | --: | --: | --: |
| 3 | 7.148 | 7.1480 | $+0.00004$ |
| 5 | 10.231 | 10.2312 | $-0.00021$ |
| 8 | 13.509 | 13.5089 | $+0.00008$ |
| 12 | 16.434 | 16.4338 | $+0.00019$ |

The residuals are negligible (order $10^{-4}$), demonstrating an exact fit.

---

## ⚡ Exam Tips & Common Mistakes

1. **Watch the roles of $a$ and $b$ in reciprocal fits.** For $y = \frac{x}{a + bx}$, the linear form is $\frac{1}{y} = a\left(\frac{1}{x}\right) + b$. The slope is $a$ and the intercept is $b$. Swapping them leads to completely wrong predictions.
2. **Carry enough decimal places for transformed variables.** Logarithms and reciprocals are sensitive to rounding. Carry at least 5 to 6 decimal places during intermediate sum calculations before rounding the final parameters.
3. **Remember to exponentiate for $a$.** In exponential fitting $y = ae^{bx}$, the regression intercept is $A = \ln a$. Do not forget to compute $a = e^A$.
4. **Use natural logarithm for $e^{bx}$.** If the base is $e$, use $\ln$ ($\log_e$). If the model is $y = ab^x$ or $y = ax^b$, you can use either $\ln$ or $\log_{10}$, but be consistent.

## 🔗 Related Topics

- [NM-4.1: Curve Fitting Concepts](NM-4.1_Curve_Fitting_Concepts.md) — foundational principles of regression vs. interpolation
- [NM-4.2: Least-Squares Linear Regression](NM-4.2_Least_Squares_Linear_Regression.md) — standard linear regression equations and slope derivation
- [NM-4.6: Lagrange's Interpolation](NM-4.6_Lagranges_Interpolation.md) — exact interpolation for uneven intervals

---

[← Previous: NM-4.2 Least Squares Linear Regression](NM-4.2_Least_Squares_Linear_Regression.md) | [🏠 Index](00_Index.md) | [Next: NM-4.6 Lagrange's Interpolation →](NM-4.6_Lagranges_Interpolation.md)
