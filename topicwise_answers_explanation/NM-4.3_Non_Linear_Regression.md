---
title: "NM-4.3 · Non-Linear Regression"
tags:
  - numerical-methods
  - discrete-mathematics
  - topicwise
---

# NM-4.3 · Non-Linear Regression

Every block below is copied from `../answers_explanation/`. The reasoning
is written once, in the year-wise file, and is not restated here.


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
