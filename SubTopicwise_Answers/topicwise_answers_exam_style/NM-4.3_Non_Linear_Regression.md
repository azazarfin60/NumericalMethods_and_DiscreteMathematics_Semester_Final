---
title: "NM-4.3 · Non-Linear Regression"
tags:
  - numerical-methods
  - discrete-mathematics
  - topicwise
---


[🏠 Subtopic Index](00_Index.md) | [← Prev: NM-4.2 Least-Squares Linear Regression](NM-4.2_Least_Squares_Linear_Regression.md) | [Next: NM-4.4 Regression Criteria & Theory →](NM-4.4_Regression_Criteria_and_Theory.md)

---

# NM-4.3 · Non-Linear Regression

Every block below is copied from `../answers_exam_style/`, which is the
only place an answer is authored. A number here is the same number, character
for character, as the one it came from.


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

[🏠 Subtopic Index](00_Index.md) | [← Prev: NM-4.2 Least-Squares Linear Regression](NM-4.2_Least_Squares_Linear_Regression.md) | [Next: NM-4.4 Regression Criteria & Theory →](NM-4.4_Regression_Criteria_and_Theory.md)
