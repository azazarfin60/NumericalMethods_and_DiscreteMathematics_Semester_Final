---
title: "ECE 2213 · 2022 Explanations"
tags:
  - numerical-methods
  - discrete-mathematics
  - previous-year
---

# ECE 2213: 2022 Semester Final · Explained

**RUET · ECE Dept · B.Sc. Engineering 2nd Year Even Semester Examination, 2022**

This file explains the same questions as
[[2022_answer|the 2022 answer script]], written to be read
rather than copied. Every step is named, the reason a formula is chosen is
stated, and the traps that catch people are called out.

> [!info] How to use this file
> Read this to understand *why* the answer script does what it does. When you
> are ready to write in the hall, work from
> [[2022_answer|the exam-style file]], which is shorter and
> carries no commentary.
>
> **The rule that matters.** Every boxed number here is the same number as the
> one in the answer script, character for character. Gate V5 checks this, and
> gate V12 checks that the marks and CO on every section agree with the answer
> script and with the manifest.

> [!note] What this paper is made of
> Questions 1 to 4 are numerical methods, Questions 5 to 8 are discrete
> mathematics. Every section is short, and the numerical half carries 34 of
> the 80 marks while the discrete half carries 46, so the balance tilts towards
> the logic questions even though the paper looks evenly split.
>
> **Notable questions in this paper**, all three worth knowing about before you
> start:
>
> | Where | What is notable |
> | :-- | :-- |
> | Q.2(b) | a least squares fit whose linearisation puts the slope and intercept in the reverse of the usual order |
> | Q.3(b) | says "a cubic function", but the five data points fit a **quartic** |
> | Q.5(d) | classic Lewis Carroll sorites from Kenneth Rosen; valid when complementary antonyms ("dull" $\equiv \neg\text{richly coloured}$, "small" $\equiv \neg\text{large}$) are formalized |
>
> Following the printed words without checking assumptions leads to traps: the
> file shows where the subtleties lie rather than only giving bare formulas.

---

# SECTION A

## Question 1

### **(a) What is the difference between open and bracketing method of root finding?**

*[Marks: 02, CO: 1]*

**Bracketing.** You start with an interval $[a,b]$ in which $f$ changes sign.

$$
f(a) \cdot f(b) < 0
$$

Continuity then guarantees at least one root inside. Each iteration throws away
the half of the interval that does not contain the sign change, so the interval
can never lose the root. That guarantee is the whole point.

**Open.** No interval. You start from a single guess $x_0$ and generate the next
point from a formula. Nothing keeps the iterates near the root, so a bad start
can send them off to infinity.

| Property | Bracketing | Open |
| :-- | :-- | :-- |
| Initial data | an interval with a sign change | one estimate $x_0$ |
| Needs | $f$ and its sign | $f$ **and** $f'$ |
| Convergence | always, from any valid bracket | only if $x_0$ is close enough |
| Rate | linear, $O(h)$ | superlinear, or quadratic |
| Examples | bisection, regula falsi | Newton-Raphson, secant, fixed point |

$$\boxed{\text{bracketing encloses the root and always converges; open methods start free and may not}}$$

> [!warning] The trade is safety against speed, not right against wrong
> An open method that converges is usually much faster: Newton-Raphson is
> quadratic, bisection is only linear, so Newton gets six correct digits in
> about five steps where bisection needs about thirty. The catch is that Newton
> can also fail completely, and there is no way to tell from the output that it
> has.
>
> This is why production root-finders keep a bracket and fall back to bisection
> whenever a Newton step leaves it. The hybrid gets the speed of the open method
> and the guarantee of the bracketing one, which is the reason the distinction
> matters beyond the two marks.

---

### **(b) Evaluate $f(1)$ using Taylor's series for $f(x)$, where $f(x) = x^3 - 3x^2 + 5x - 10$.**

*[Marks: 04, CO: 1]*

**Step 1. Write the series about $x = 0$.**

$$
f(x) = f(0) + x f'(0) + \frac{x^2}{2!}f''(0) + \frac{x^3}{3!}f'''(0) + \frac{x^4}{4!}f^{(4)}(0) + \cdots
$$

**Step 2. Differentiate and evaluate at zero.** All four rows are needed, because
a cubic is exactly the case where the fourth derivative decides whether the
series terminates.

| | $f(x)$ | $f'(x)$ | $f''(x)$ | $f'''(x)$ | $f^{(4)}(x)$ |
| :-- | :-- | :-- | :-- | :-- | :-- |
| | $x^3-3x^2+5x-10$ | $3x^2-6x+5$ | $6x-6$ | $6$ | $0$ |

$$
f(0) = -10, \qquad f'(0) = 5, \qquad f''(0) = -6, \qquad f'''(0) = 6, \qquad f^{(4)} = 0
$$

**Step 3. The series terminates.** The fourth derivative is identically zero, so
there is nothing after the cubic term:

$$
f(x) = -10 + 5x + \frac{-6}{2}x^2 + \frac{6}{6}x^3 = -10 + 5x - 3x^2 + x^3
$$

**Step 4. Put $x = 1$.**

$$
f(1) = -10 + 5(1) - 3(1)^2 + (1)^3 = -10 + 5 - 3 + 1
$$

$$\boxed{f(1) = -7}$$

> [!info] Three independent routes, all landing on $-7$
> **Direct substitution.** $1 - 3 + 5 - 10 = -7$.
>
> **Horner, with no powers written out.** $(-10 + 5 \cdot 1) \cdot 1 - 3 = -8$, then
> $-8 \cdot 1 + 1 = -7$.
>
> **The truncation error is exactly zero.** Because $f^{(4)} \equiv 0$, the
> remainder $R_3$ is identically zero, not merely small. There is no error term
> to bound here, which is the distinguishing feature of a cubic.

> [!note] Why this question has no error analysis
> Taylor's method earns its keep when the series is infinite. For a polynomial of
> degree $k$, the $k$-th order expansion is the polynomial itself, and the
> $(k+1)$-th derivative being zero is what makes the answer exact rather than
> approximate.
>
> So no remainder term is needed here, and writing one anyway would be padding.
> The four marks are for the derivative table: $f'$, $f''$, $f'''$ written out
> explicitly, then the substitution. That is the whole question.

---

### **(c) Explain a real life application of curve-fitting. For what type of data points will you use Lagrange's interpolation formula?**

*[Marks: 04, CO: 2]*

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

## Question 2

### **(a) Find the polynomial which fits the following data: $(-1, 7)$, $(1, 5)$, $(2, 15)$.**

*[Marks: 04, CO: 1]*

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

### **(b) Using the method of least squares, fit a curve of the form $y = \frac{x}{a + bx}$ to fit the following data $(3, 7.148)$, $(5, 10.231)$, $(8, 13.509)$, $(12, 16.434)$.**

*[Marks: 03, CO: 1]*

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

### **(c) Using Newton's forward difference formula find the sum $S_n = 1^3 + 2^3 + 3^3 + \cdots + n^3$.**

*[Marks: 03, CO: 1]*

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

## Question 3

### **(a) Compute the value of $I = \int_0^1 \frac{dx}{1 + x^2}$ using the trapezoidal rule with $h = 0.5, 0.25$ and $0.125$. Then obtain a better estimate using Romberg's method.**

*[Marks: 04, CO: 1]*

**Step 1. Function values.** All nine are needed, because the finest trapezoid
rule uses the whole set.

| $x$ | 0 | 0.125 | 0.25 | 0.375 | 0.5 | 0.625 | 0.75 | 0.875 | 1 |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| $f(x) = \frac{1}{1+x^2}$ | 1.000000 | 0.984615 | 0.941176 | 0.876712 | 0.800000 | 0.719101 | 0.640000 | 0.566372 | 0.500000 |

**Step 2. The trapezoidal rule, three step sizes.**

$$
T_n = \frac{h}{2}\left[f_0 + 2f_1 + 2f_2 + \cdots + 2f_{n-1} + f_n\right]
$$

At $h = 0.5$, $n = 2$:

$$
T_2 = \frac{0.5}{2}\left[1 + 2(0.8) + 0.5\right] = 0.25(3.1) = 0.775000
$$

At $h = 0.25$, $n = 4$:

$$
T_4 = 0.125\left[1 + 2(0.941176 + 0.8 + 0.640000) + 0.5\right] = 0.125(6.262352) = 0.782794
$$

At $h = 0.125$, $n = 8$:

$$
T_8 = 0.0625\left[1 + 2(0.984615 + 0.941176 + 0.876712 + 0.800000 + 0.719101 + 0.640000 + 0.566372) + 0.5\right]
$$

$$
= 0.0625\left[1 + 2(5.527976) + 0.5\right] = 0.0625(12.555952) = 0.784747
$$

**Step 3. Richardson extrapolation.** The trapezoid rule has $O(h^2)$ error, so
halving $h$ cuts the error by $4$, and each extrapolation removes a factor of
$4^j - 1$:

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

$$\boxed{I \approx 0.7853985 \quad \text{(trapezoid alone gives } 0.784747\text{)}}$$

> [!info] The exact answer is known here, so the error can be computed rather than estimated
> $$\int_0^1\frac{dx}{1+x^2} = \arctan x\Big|_0^1 = \arctan 1 = \frac{\pi}{4} = 0.7853981634$$
> The Romberg estimate $0.7853985235$ differs by $3.60 \times 10^{-7}$, a relative
> error of $4.6 \times 10^{-7}$. The bare trapezoid result at $h = 0.125$ is off by
> $6.51 \times 10^{-4}$, so Romberg improved the accuracy by a factor of about
> $1800$ using **no new function evaluations**.
>
> That last point is the whole appeal of Romberg. The same nine values of $f$
> serve every entry in the table, so accuracy is bought by rearranging numbers
> rather than by doing more work.

> [!note] Why each column divides by 3, then by 3, then by 15
> The denominators are $4^1 - 1 = 3$, $4^1 - 1 = 3$, $4^2 - 1 = 15$. The first
> column of extrapolations always uses $3$, because it is removing the $h^2$
> term. Only once two columns of trapezoid-like values have been combined does
> the order rise to $h^4$ and the denominator become $15$.
>
> The visible signature of a correct Romberg table is that each entry agrees with
> its neighbours to more digits than the one below it. If a column does not
> settle, the divisor is usually wrong rather than the arithmetic.

---

### **(b) A cubic function $y = f(x)$ satisfies the data $x = 0, 1, 3, 4, 2$ with $f(x) = 1, 4, 40, 85, 17$. Determine the value of $f'(4)$.**

*[Marks: 04, CO: 2]*

> [!warning] Two printed defects decide this answer, and both must be handled before anything is computed
> **The word "cubic" is wrong.** Five points do not in general lie on a cubic, and
> these do not. Forcing a cubic through five points gives no solution at all: the
> coefficient matrix has rank $4$ while the augmented matrix has rank $5$, so the
> system is inconsistent.
>
> **The $x$ column is out of order.** The paper prints $x = 0, 1, 3, 4, 2$. Sort the
> nodes first, to $(0,1), (1,4), (2,17), (3,40), (4,85)$, before differencing.

**Step 1. Newton's divided difference form**, on the sorted nodes.

| Order | Values | How each entry is computed |
| :-- | :-- | :-- |
| $y$ | 1, 4, 17, 40, 85 | given |
| $1^{st}$ | 3, 13, 23, 45 | $(4-1)/1$, $(17-4)/1$, $(40-17)/1$, $(85-40)/1$ |
| $2^{nd}$ | 5, 5, 11 | $(13-3)/2 = 5$, $(23-13)/2 = 5$, $(45-23)/2 = 11$ |
| $3^{rd}$ | 0, 2 | $(5-5)/3 = 0$, $(11-5)/3 = 2$ |
| $4^{th}$ | $\frac{1}{2}$ | $(2-0)/4 = \frac{1}{2}$ |

The fourth divided difference is $\frac{1}{2}$, **not zero**. For any cubic in $x$
the third divided difference is constant and the fourth is zero, so this table is
the proof that the data lie on a **quartic**, not a cubic.

The leading diagonal is $1, 3, 5, 0, \frac{1}{2}$, giving

$$
f(x) = 1 + 3x + 5x(x-1) + 0\cdot x(x-1)(x-2) + \frac{1}{2}x(x-1)(x-2)(x-3)
$$

The third divided difference is zero, so that term vanishes entirely. That is
also why the quartic has no $x(x-1)(x-2)$ contribution.

**Step 2. Expand.** Using $x(x-1)(x-2)(x-3) = x^4 - 6x^3 + 11x^2 - 6x$:

$$
f(x) = 1 + 3x + 5x^2 - 5x + \frac{1}{2}\left(x^4 - 6x^3 + 11x^2 - 6x\right)
$$

$$\boxed{f(x) = \frac{x^4}{2} - 3x^3 + \frac{21}{2}x^2 - 5x + 1}$$

**Step 3. Verify all five points before differentiating anything.**

| $x$ | $\frac{x^4}{2}$ | $-3x^3$ | $\frac{21}{2}x^2$ | $-5x$ | $1$ | Total | Given | |
| --: | --: | --: | --: | --: | --: | --: | --: | :-- |
| 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | ✓ |
| 1 | 0.5 | $-3$ | 10.5 | $-5$ | 1 | 4 | 4 | ✓ |
| 2 | 8 | $-24$ | 42 | $-10$ | 1 | 17 | 17 | ✓ |
| 3 | 40.5 | $-81$ | 94.5 | $-15$ | 1 | 40 | 40 | ✓ |
| 4 | 128 | $-192$ | 168 | $-20$ | 1 | 85 | 85 | ✓ |

All five are reproduced exactly, with no rounding anywhere.

**Step 4. Differentiate and evaluate.**

$$
f'(x) = 2x^3 - 9x^2 + 21x - 5
$$

$$
f'(4) = 2(64) - 9(16) + 21(4) - 5 = 128 - 144 + 84 - 5 = 68 - 5
$$

$$\boxed{f'(4) = 63}$$

> [!info] Two independent routes
> **Route 2, Lagrange form expanded.** The five-point Lagrange sum, whose
> denominators $\prod_{j \ne i}(x_i - x_j)$ for $x = 0, 1, 2, 3, 4$ are
> $24, -6, 4, -6, 24$, expands to the same polynomial
> $\frac{x^4}{2} - 3x^3 + \frac{21}{2}x^2 - 5x + 1$, and differentiating that gives
> $63$ at $x = 4$.
>
> **Route 3, central difference on the fitted polynomial.** Evaluating at
> $x = 4.01$ and $x = 3.99$ and dividing by $0.02$:
> $$f'(4) \approx \frac{f(4.01) - f(3.99)}{0.02} = 63.0005$$
> The error is $O(h^2) = O(0.0001)$, so this confirms $63$.

> [!warning] The secant slopes are nowhere near the answer
> $\frac{f(4)-f(3)}{1} = 45$ and $\frac{f(4)-f(2)}{2} = 34$, both far from $63$.
> A secant slope is an average of the slope over a wide interval, not the slope
> at a point, and this quartic curves enough for the difference to be large.
>
> If you are asked for a derivative and find yourself writing
> $\frac{f(4)-f(3)}{1}$, stop. That is a finite difference and it is not what was
> asked.

> [!note] Why the question is still answerable despite being wrong
> Five points determine exactly one polynomial of degree at most four, so
> $f'(4)$ is unique even though the degree label is wrong. The operative reading
> is "find the polynomial through these five points, whatever its degree".
>
> **The unsorted table is worth seeing, because it is what happens if you skip
> the sorting step.** Differencing the nodes in the printed order gives first
> differences $3, 18, 45, 34$, second $5, 9, 11$, third $1, 2$, fourth $\frac{1}{2}$.
> The fourth entry is still $\frac{1}{2}$, since divided differences are symmetric,
> but the third row is $1, 2$ instead of $0, 2$, so the $x(x-1)(x-2)$ term does
> not vanish and the polynomial you get is wrong in a way that still reproduces
> all five points.

---

### **(c) What is pivoting?**

*[Marks: 02, CO: 1]*

**Definition.** In Gaussian elimination, **pivoting** is interchanging rows, or
columns, so that the element chosen as the **pivot**, which is the next divisor,
is as large as possible in magnitude, or at least not negligibly small.

**Why it is needed.** Every elimination step divides by the pivot. If the pivot is
$0$ the step is impossible. If it is merely tiny, say $10^{-9}$, the multiplier
$a_{ik}/a_{kk}$ becomes enormous, and the elimination floods the remaining rows
with round off.

**Three forms.**

1. **Partial pivoting**, the usual choice. At step $k$, find the largest
   $|a_{ik}|$ in column $k$ below the diagonal and swap that row up. Cost is one
   comparison per candidate, no extra arithmetic, and it is stable in practice.
2. **Scaled partial pivoting**. Divide each candidate by its own row's largest
   magnitude first, then compare, choosing $k$ to maximise
   $$\frac{|a_{ik}|}{\max_j |a_{ij}|}$$.
   This stops a row with large entries but a small pivot from being unfairly
   penalised.
3. **Complete pivoting.** Search the whole remaining submatrix and permute both
   rows and columns. The most stable, but it scrambles the variable order, so it
   is confined largely to research codes.

$$\boxed{\text{Pivoting reorders rows or columns so the divisor is as large as possible, avoiding a tiny pivot and its round off}}$$

> [!warning] Pivoting cannot rescue a singular matrix
> If a whole column of the remaining submatrix is zero, the matrix is singular
> and no rearrangement helps. Pivoting makes a bad pivot large; it cannot
> manufacture a nonzero pivot where none exists.
>
> This is worth separating from **scaling**, which multiplies rows and columns
> by constants. Scaling is a legitimate operation on a system and changes the
> solution consistently. Row swapping changes nothing at all about the solution,
> which is why pivoting is always safe and scaling needs care.

> [!note] The one-line test for whether you need it
> Look at the first column. If the leading entry is smaller in magnitude than
> something below it, partial pivoting would have chosen differently. That single
> comparison costs nothing and covers the large majority of practical cases.

---

## Question 4

### **(a) Solve the system using Jacobi method: $6x + y + z = 20$, $x + 4y - z = 6$, $x - y + 5z = 7$.**

*[Marks: 04, CO: 1]*

**Step 1. Rearrange each equation to isolate its own variable.** Do this one
equation at a time and move every other term to the right, changing its sign.

$$
x = \frac{20 - y - z}{6}, \qquad
y = \frac{6 - x + z}{4}, \qquad
z = \frac{7 - x + y}{5}
$$

> [!warning] The third rearrangement is where this question is lost
> The third equation is $x - y + 5z = 7$. Moving $x$ and $y$ across gives
> $$5z = 7 - x + y \quad \Rightarrow \quad z = \frac{7 - x + y}{5}$$
> The $-x$ goes with a minus and the $+y$ keeps its plus, because moving $y$
> across flips its sign from $-y$ to $+y$. Writing $z = \frac{7 + x - y}{5}$
> keeps both signs as they appear in the original equation, which is exactly the
> wrong thing to do.
>
> **The test is instant.** Substitute the answer into the rearranged equation. At
> the true solution $x = 3$, $y = 1$, $z = 1$, the correct form gives
> $\frac{7-3+1}{5} = 1$ ✓ while the wrong form gives $\frac{7+3-1}{5} = 1.8$ ✗.
> A rearrangement that fails at a value you can guess has failed.

**Step 2. Check the convergence condition.** Jacobi converges when the matrix is
**strictly diagonally dominant**, that is when each diagonal entry exceeds the sum
of the off-diagonal entries in its own row.

| Row | Diagonal | Off-diagonal sum | |
| --: | --: | --: | :-- |
| 1 | 6 | 1 + 1 = 2 | $6 > 2$ ✓ |
| 2 | 4 | 1 + 1 = 2 | $4 > 2$ ✓ |
| 3 | 5 | 1 + 1 = 2 | $5 > 2$ ✓ |

Convergence is guaranteed. This check costs one line and decides whether the
iteration is worth running at all.

**Step 3. The Jacobi rule.** Use only values from the **previous** iteration,
never a value just computed:

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

$$\boxed{x = 3.000, \qquad y = 1.000, \qquad z = 1.000}$$

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

> [!info] Independent confirmation
> Solving the system directly by Gaussian elimination, or by Cramer's rule,
> returns $x = 3$, $y = 1$, $z = 1$ exactly. Since all three residuals are zero,
> the solution is unique.

> [!note] How fast is the convergence, and is the table consistent with the rule?
> The largest error falls $0.500000$, $0.150000$, $0.045833$, $0.013194$,
> $0.006007$, $0.002066$, $0.000924$, $0.000358$, so successive ratios are near
> $3$, which is the expected rate for Jacobi on a diagonally dominant system.
>
> **That consistency is itself a check on the iteration.** Recompute one row of
> the table directly from the printed rule. Row 2 for instance:
> $x^{(2)} = \frac{20 - 1.5 - 1.4}{6} = 2.85$ ✓,
> $y^{(2)} = \frac{6 - 3.333333 + 1.4}{4} = 1.016667$ ✓,
> $z^{(2)} = \frac{7 - 3.333333 + 1.5}{5} = 1.033333$ ✓.
> A table that does not reproduce from its own rule is a table built with a
> different rule, and no amount of correct arithmetic elsewhere will fix it.

> [!warning] Jacobi versus Gauss-Seidel uses a different rule, not a different starting value
> Gauss-Seidel would use the values **just computed** in the same sweep:
> $$y^{(k+1)} = \frac{6 - x^{(k+1)} + z^{(k)}}{4}$$
> Mixing the two rules produces a sequence that converges to the right answer
> from one direction, or to the wrong one, with no obvious symptom.
>
> Jacobi's advantage is that it needs no ordering of the variables and updates
> every unknown simultaneously, which suits parallel hardware.

---

### **(b) Solve the system using Gauss elimination: $2x_1 + x_2 - x_3 = -1$, $x_1 - 2x_2 + 3x_3 = 9$, $3x_1 - x_2 + 5x_3 = 14$. Check your answer by substituting into the original equations.**

*[Marks: 04, CO: 2]*

**Step 1. The augmented matrix.**

$$
\left[\begin{array}{ccc|c}
2 & 1 & -1 & -1 \\
1 & -2 & 3 & 9 \\
3 & -1 & 5 & 14
\end{array}\right]
$$

**Step 2. Eliminate $x_1$ from rows 2 and 3.** The multipliers are $\frac{1}{2}$
and $\frac{3}{2}$, taken as row entry over pivot.

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

Note the signs in the last two columns: $\frac{7}{2} = 3 - \frac{1}{2}(-1)$ is
positive because subtracting a negative $\frac{1}{2}(-1)$ adds $\frac{1}{2}$.

**Step 3. Eliminate $x_2$ from row 3.** The multiplier is
$\frac{-5/2}{-5/2} = 1$, so $R_3 \leftarrow R_3 - R_2$:

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

$$\boxed{x_1 = 1, \qquad x_2 = -1, \qquad x_3 = 2}$$

**The required check, by substitution into the original equations.**

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

> [!warning] The sign of $x_2$ is decided in one line, and it is easy to lose
> Row 2 gives $-\frac{5}{2}x_2 = +\frac{5}{2}$, so $x_2 = -1$. The minus sign is
> on both sides and cancels, but the minus on the left comes from the negative
> diagonal entry, not from the arithmetic of the step.
>
> A useful symmetry check: the same elimination written the other way round,
> $R_2 \leftarrow R_2 - R_3$, gives the row $[0, 0, -3, -6]$ instead of
> $[0, 0, 3, 6]$. Both give $x_3 = 2$, because the signs cancel. Writing one
> convention into the matrix and the other into the back substitution does not,
> so keep to whichever direction you started with.

> [!info] Independent confirmation
> The determinant of the coefficient matrix is
> $$\det = 2(-10 + 3) - 1(5 - 9) + (-1)(-1 + 6) = -14 + 4 - 5 = -15 \ne 0$$
> so the system has a unique solution, and Cramer's rule returns $(1, -1, 2)$.
> Note also that the three pivots $2$, $-\frac{5}{2}$ and $3$ are all comfortably
> away from zero, so no pivoting was needed here.

---

### **(c) Define ill-conditioned system.**

*[Marks: 02, CO: 1]*

**Definition.** A system of linear equations is **ill-conditioned** when a small
change in the input produces a disproportionately large change in the solution.

**Measure.** The **condition number** $\kappa$ of the coefficient matrix is the
ratio of the largest to the smallest relative error:

$$
\frac{\dfrac{\|\delta x\|}{\|x\|}}{\dfrac{\|\delta b\|}{\|b\|}} \le \kappa(A)
$$

So a relative error of $\epsilon$ in the data may become up to $\kappa\epsilon$ in
the answer.

| $\kappa$ | Behaviour |
| :-- | :-- |
| $\kappa = 1$ | Perfectly conditioned, error passes through unchanged |
| $\kappa \approx 10$ | Mild amplification |
| $\kappa \approx 10^{6}$ | Loss of about six significant digits |
| $\kappa > 10^{16}$ | All precision lost, the matrix is numerically singular |

**Causes.**

1. **A matrix that is nearly singular**, with an eigenvalue very close to zero
   or rows that are almost linearly dependent. Two nearly parallel equations
   constrain the solution very weakly.
2. **Rows or columns of wildly different magnitudes.** The small ones are
   effectively ignored.
3. **A bad choice of variables.** Two variables measuring nearly the same
   physical quantity make the corresponding columns almost equal.

$$\boxed{\text{ill-conditioned means small input errors produce large output errors; measured by }\kappa}$$

> [!warning] Conditioning is a property of the problem, not of the algorithm
> **Pivoting helps stability but does not change $\kappa$.** Switching to a better
> elimination order makes the computed answer closer to the exact answer of the
> system you were given; it does not make the system you were given better
> posed.
>
> This is the single most important distinction in the topic. A well-conditioned
> system solved badly gives a slightly wrong answer, and a badly conditioned
> system solved well gives a wildly wrong one. No amount of care in the
> algorithm repairs the second case.

> [!note] Why it matters in engineering
> The data itself has uncertainty, typically $10^{-4}$ relative from the
> instrument. With $\kappa = 10^{8}$ the answer then carries a relative
> uncertainty of $10^{4}$, which is useless, even though the computation ran to
> machine precision and printed fifteen digits.
>
> The remedies are all about the problem rather than the arithmetic: row or
> column scaling to make entries comparable, choosing better-conditioned
> variables, reformulating the physical problem, or using higher precision.

---

# SECTION B

## Question 5

### **(a) Explain how proposition differs from traditional sentence. Give some examples.**

*[Marks: 03, CO: 2]*

**Proposition.** A declarative sentence that is **unambiguously either true or
false**, with exactly one truth value. Nothing more is required. It need not be
meaningful, need not be verifiable today, and carries no quantifier.

**Traditional sentence.** Any statement of natural language. The category is
much wider, admitting sentences with no truth value at all.

| Sentence | Proposition? | Reason |
| :-- | :-- | :-- |
| The transistor conducts | **Yes** | true or false |
| $2 + 2 = 4$ | **Yes** | |
| Water boils at $100^{\circ}$C at sea level | **Yes** | a fact, though it needs a reference condition |
| Close the window | No | imperative, a command |
| Is the door open | No | interrogative, a question |
| Please hand me the tool | No | a request |
| $x + 1 > 0$ | No | depends on the unknown $x$ |
| The present king of France is bald | No | presupposes a non-existent referent, so no truth value |
| $1/0 = 3$ | No | meaningless, division by zero |

**The four tests.**

1. **Declarative.** It asserts rather than commands, asks or requests.
2. **Not interrogative.** No question in intent.
3. **Has a truth value.** Exactly one of true or false, with nothing in between.
4. **Meaningful.** Every symbol is defined, so the sentence can be evaluated.

> [!warning] The four rows that trip people up
> "$x + 1 > 0$" fails because $x$ is free, not because it is false. It becomes a
> proposition only once $x$ is bound: "for every real $x$, $x + 1 > 0$".
>
> "The present king of France is bald" fails because it presupposes something
> that does not exist, so the sentence can be neither true nor false. This is a
> different failure from being undecidable in practice; it has no truth value at
> all.
>
> "$1/0 = 3$" fails on meaningfulness. It is not false, it is not an equation
> between numbers.

> [!note] Propositions, compound propositions and predicates are three different things
> A **compound proposition** is built from simple ones using
> $\neg, \land, \lor, \to, \leftrightarrow$.
>
> A **predicate** such as "$x$ is prime" is not a proposition on its own,
> because $x$ is free. Binding it gives one.
>
> Propositional logic can only reason over things with a definite truth value, so
> anything else has to be translated into propositions first. That translation
> step is where most real errors in control logic occur, which is why the
> distinction is worth two marks of care rather than a definition to memorise.

---

### **(b) The truth value of the conjunction of two propositions in fuzzy logic is the minimum of the truth values of the statements "Fred and John are happy" and "Neither Fred nor John is happy". Prove the statement.**

*[Marks: 03, CO: 1]*

**Setup.** Fuzzy logic assigns each proposition a truth value in $[0,1]$, where
$0$ is false and $1$ is true. Fuzzy conjunction is **defined** by

$$
T(A \wedge B) = \min\left(T(A),\, T(B)\right)
$$

Let $h = T(\text{Fred is happy})$ and $j = T(\text{John is happy})$, with
$0 \le h, j \le 1$.

**Statement A, "Fred and John are happy."** A conjunction of two, so

$$
T(A) = \min(h, j)
$$

**Statement B, "Neither Fred nor John is happy."** "Neither A nor B" expands to
$\neg A \wedge \neg B$, and fuzzy negation is $T(\neg P) = 1 - T(P)$, so

$$
T(B) = \min(1 - h,\; 1 - j) = 1 - \max(h, j)
$$

**Statement C, the conjunction $A \wedge B$.** Applying the defining rule:

$$
T(C) = \min\left(T(A), T(B)\right) = \min\left(\min(h, j),\; 1 - \max(h, j)\right)
$$

Written out in full, that is $T(C) = \min(h,\; j,\; 1 - h,\; 1 - j)$, which is
exactly the assertion to be proved. The claim holds by the defining rule.

> [!warning] The identity is the definition, so the real content of the question is the bound
> $T(A \wedge B) = \min(T(A), T(B))$ needs no proof: it *is* fuzzy AND. What the
> chosen pair of sentences delivers is a strong limit, because $A$ and $B$ are
> contradictories.
>
> Since $T(C) = \min(h, 1-h) \le \frac{1}{2}$:
>
> | Case | $T(A)$ | $T(B)$ | $T(C)$ |
> | :-- | --: | --: | --: |
> | $h = j = 1$ | 1 | 0 | **0** |
> | $h = j = 0$ | 0 | 1 | **0** |
> | $h = 0.3, j = 0.4$ | 0.3 | 0.6 | **0.3** |
> | $h = j = 0.5$ | 0.5 | 0.5 | **0.5** |
> | $h = j = 0.7$ | 0.7 | 0.3 | **0.3** |
>
> **The conjunction never exceeds $0.5$, and its maximum is attained only at
> $h = j = 0.5$.** A sweep of the unit square on a $0.1$ grid confirms the maximum
> is $0.5$.
>
> Classical logic calls $A \wedge B$ always false. Fuzzy logic softens that to "at
> most half true", which is what makes fuzzy logic useful on contradictory-looking
> sensor data rather than merely decorative.

> [!info] Exhaustive confirmation
> The identity $T(A \wedge B) = \min(T(A), T(B))$ was evaluated at all $121$
> points of the grid $h, j \in \{0, 0.1, \ldots, 1.0\}$. In every case the computed
> conjunction equals the minimum of the two statement truth values, so no
> counterexample exists.

---

### **(c) Show that $\neg$ and $\land$ form a functionally complete collection of logical operators.**

*[Marks: 02, CO: 2]*

**Definition.** A collection of operators is **functionally complete** if every
other Boolean operator can be expressed using only those operators.

**Goal.** Build $\lor$ and $\to$ from $\neg$ and $\land$ alone.

**Step 1. Disjunction, by De Morgan.** Since $\neg(p \land q) = \neg p \lor \neg q$,

$$
p \lor q = \neg(\neg p \land \neg q)
$$

**Step 2. Implication.** Since $p \to q \equiv \neg p \lor q$,

$$
p \to q = \neg p \lor q = \neg(\neg(\neg p) \land \neg q)
$$

**Step 3. Biconditional.** Since $p \leftrightarrow q \equiv (p \to q) \land (q \to p)$,
substituting step 2 in both places expresses it in terms of $\neg$ and $\land$
too.

**Step 4. Verify against the truth tables.** Rows run $p$ outer, $q$ inner, each
taking $T$ then $F$.

| $p$ | $q$ | $\neg p$ | $\neg q$ | $p \lor q$ | $\neg(\neg p \land \neg q)$ | $p \to q$ | $\neg(\neg(\neg p) \land \neg q)$ |
| :-: | :-: | :-: | :-: | :-: | :-- | :-: | :-- |
| F | F | T | T | F | $\neg(T \land T) = F$ ✓ | T | $\neg(F \land T) = T$ ✓ |
| F | T | T | F | T | $\neg(T \land F) = T$ ✓ | T | $\neg(F \land F) = T$ ✓ |
| T | F | F | T | T | $\neg(F \land T) = T$ ✓ | F | $\neg(T \land T) = F$ ✓ |
| T | T | F | F | T | $\neg(F \land F) = T$ ✓ | T | $\neg(T \land F) = T$ ✓ |

Every constructed column matches its target in all four rows.

**Step 5. Conclusion.** The operators $\neg$ and $\land$ generate $\lor$, $\to$,
$\leftrightarrow$ and everything built from them, so the collection is
functionally complete.

$$\boxed{p \lor q = \neg(\neg p \land \neg q), \qquad p \to q = \neg(\neg(\neg p) \land \neg q)}$$

> [!warning] Count the negations in the implication formula, they are easy to lose
> $p \to q \equiv \neg p \lor q$, and then $\neg p \lor q$ is already in disjunctive
> form, so it needs no De Morgan step at all. The formula
> $\neg(\neg(\neg p) \land \neg q)$ comes from rewriting $\neg p$ as
> $\neg(\neg(\neg p))$ so that both operands of $\lor$ sit under negations.
>
> Dropping one of the three negations on $p$ gives a formula that looks
> perfectly reasonable and is false on the row $p = T, q = F$. That single row is
> the whole test, and the table above is where it is caught.

> [!note] There are exactly two minimal complete sets
> They are $\{\neg, \land\}$ and $\{\neg, \lor\}$.
>
> Neither $\land$ nor $\lor$ alone is complete, since neither can produce
> negation. A set containing no negation at all cannot realise $p \lor \neg p$,
> which is a tautology and must therefore be constantly true, and a monotone
> connective cannot do that. **This is why every functionally complete set must
> contain $\neg$, or something that produces it.**

---

### **(d) Consider these statements, of which the first three are premises and the fourth is a valid conclusion. "All humming are richly colored." "No large birds live on honey." "Birds that do not live on honey are dull in order." Conclusion: "Humming birds are small."**

*[Marks: 02, CO: 3]*

> [!note] Origin & Textual Corrections
> This question is taken verbatim from Kenneth H. Rosen, *Discrete Mathematics and Its Applications* (§1.6, Example 26: "Rules of Inference"), which adapts a classic sorites puzzle by Lewis Carroll (from *Symbolic Logic*, 1896).
> - *"All humming"* has the noun "birds" omitted in the printed question.
> - *"dull in order"* is a transcription error for *"dull in colour"*.

**Step 1. Formalise using Predicate Logic.**
In Lewis Carroll's logic puzzles and Rosen's formulation, natural-language antonyms are treated as logical complements:
- "dull in colour" is the exact complement of "richly coloured" ($\neg S(x)$).
- "small" is the exact complement of "large" ($\neg Q(x)$).

Let the universe of discourse $U$ be the set of all birds:
- $P(x)$: $x$ is a hummingbird
- $Q(x)$: $x$ is large $\implies \neg Q(x)$: $x$ is small
- $R(x)$: $x$ lives on honey $\implies \neg R(x)$: $x$ does not live on honey
- $S(x)$: $x$ is richly coloured $\implies \neg S(x)$: $x$ is dull in colour

**Step 2. Express premises and the conclusion.**
1. Premise 1 ($P_1$): "All hummingbirds are richly colored"
   $$\forall x\, (P(x) \to S(x))$$
2. Premise 2 ($P_2$): "No large birds live on honey" (if large, then does not live on honey)
   $$\forall x\, (Q(x) \to \neg R(x))$$
3. Premise 3 ($P_3$): "Birds that do not live on honey are dull in colour"
   $$\forall x\, (\neg R(x) \to \neg S(x))$$
4. Conclusion ($C$): "Hummingbirds are small"
   $$\forall x\, (P(x) \to \neg Q(x))$$

**Step 3. Rigorous proof using Rules of Inference.**
Let $c$ be an arbitrary bird in $U$:

| Step | Proposition | Justification |
| :--: | :-- | :-- |
| 1 | $P(c) \to S(c)$ | Premise 1 by Universal Instantiation |
| 2 | $\neg R(c) \to \neg S(c)$ | Premise 3 by Universal Instantiation |
| 3 | $S(c) \to R(c)$ | Contrapositive of Step 2 ($\neg B \to \neg A \equiv A \to B$) |
| 4 | $P(c) \to R(c)$ | Hypothetical Syllogism from Steps 1 and 3 |
| 5 | $Q(c) \to \neg R(c)$ | Premise 2 by Universal Instantiation |
| 6 | $R(c) \to \neg Q(c)$ | Contrapositive of Step 5 |
| 7 | $P(c) \to \neg Q(c)$ | Hypothetical Syllogism from Steps 4 and 6 |
| 8 | $\forall x\, (P(x) \to \neg Q(x))$ | Universal Generalization from Step 7 |

Since $\neg Q(x)$ means "$x$ is small", the deduction is complete and valid.

$$
\boxed{\text{The argument is VALID via Universal Instantiation, Contraposition, and Hypothetical Syllogism}}
$$

> [!tip] Why propositional translation fails
> If modeled naively with 6 independent propositional variables:
> $$P_1: H \to R, \quad P_2: L \to \neg N, \quad P_3: \neg N \to D, \quad \text{Claim: } H \to S$$
> there is no syntactic link connecting $D$ to $\neg R$ or $S$ to $\neg L$. A countermodel emerges where a bird is simultaneously richly coloured and dull ($R=T, D=T$). In natural language, however, "dull" and "richly coloured" are mutually exclusive antonyms. Lewis Carroll's Sorites relies on these semantic complements, which predicate logic formalizes directly as $S(x)$ and $\neg S(x)$.

---

## Question 6

### **(a) Knights always tell the truth, Knaves always lie, Spies can either. Three people A, B and C, one of each type, each knows the types of the other two. (i) A says "C is the Knave", B says "A is the Knight", C says "I am the spy". (ii) A says "I am the Knave", B says "I am the Knave", C says "I am the Knave". Determine whether there is a unique solution.**

*[Marks: 06, CO: 3]*

**Method.** A knight's every statement is true. A knave's every statement is
false. A spy is unconstrained. Each of A, B and C may be any of the three types
and the three types are all different, so there are only $3! = 6$ assignments to
test. Testing all six is exhaustive and cheap.

**Rule stated first, because it settles part (ii) outright.** Nobody can
truthfully say "I am the knave", because a knave is by definition not a knave.
Nobody can falsely say it either, because the statement would be true for a knave.
Therefore **only a spy can say "I am the knave"**, and a knight or knave saying
it is an immediate contradiction.

---

**(i) A says "C is the Knave." B says "A is the Knight." C says "I am the spy."**

The three statements are true when, respectively, $C$ is the knave, $A$ is the
knight, and $C$ is the spy.

| Assignment | A's statement | B's statement | C's statement | Verdict |
| :-- | :-- | :-- | :-- | :-- |
| A=K, B=N, C=S | false (C is a spy, not a knave) | true | true | **A is a knight but lies. Out.** |
| A=K, B=S, C=N | true | true | false | **Consistent.** |
| A=N, B=K, C=S | false | false | true | **B is a knight but lies. Out.** |
| A=N, B=S, C=K | false | false | false | **C is a knight but lies. Out.** |
| A=S, B=K, C=N | true | false | false | **B is a knight but lies. Out.** |
| A=S, B=N, C=K | false | true | false | **C is a knight but lies. Out.** |

Exactly one row survives, so **the solution is unique**:

$$\boxed{\text{(i) A = Knight, B = Spy, C = Knave}}$$

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

$$\boxed{\text{(ii) There is NO solution}}$$

**Reason, without the table.** From the rule above, "I am the knave" can only be
said by a spy. All three of A, B and C say it. Since exactly one of the three is
a spy, at least two are knights or knaves, and each of those contradicts what
they said.

> [!info] Exhaustive check
> All six permutations were tested against the knight and knave rules in both
> parts. Part (i) returned exactly one consistent assignment; part (ii) returned
> none. Both results are therefore unique, and no assignment was missed.

> [!note] What separates the two parts
> In **(i)** the three statements refer to **different** people, so one true
> statement can be pinned on the spy and the remaining two can be assigned to a
> knight and a knave consistently.
>
> In **(ii)** all three statements are the same self-referential claim. Only one
> spy exists, so two of the three speakers are making a sentence they cannot make.
> That is the standard way to show a knights-and-knaves puzzle has no solution: put
> everyone in the same corner and no consistent assignment remains.
>
> The rule stated before the tables is worth internalising, because it turns part
> (ii) from six rows of bookkeeping into one sentence.

---

### **(b) Determine whether the biconditionals are true or false: (i) $2 + 2 = 4$ if and only if $1 + 1 = 2$, (ii) $1 + 1 = 2$ if and only if $2 + 3 = 4$, (iii) $1 + 1 = 3$ if and only if monkeys can fly, (iv) $0 > 1$ if and only if $2 > 1$.**

*[Marks: 04, CO: 1]*

The biconditional $P \leftrightarrow Q$ is true when $P$ and $Q$ have the
**same** truth value, that is when both are true or both are false.

$$
P \leftrightarrow Q \equiv (P \to Q) \land (Q \to P)
$$

**(i) $2 + 2 = 4$ if and only if $1 + 1 = 2$**

$2+2=4$ is true. $1+1=2$ is true. Same value, so the biconditional holds.

$$\boxed{\text{(i) TRUE}}$$

**(ii) $1 + 1 = 2$ if and only if $2 + 3 = 4$**

$1+1=2$ is true. $2+3=5$, not $4$, so $2+3=4$ is false. The values disagree.

$$\boxed{\text{(ii) FALSE}}$$

**(iii) $1 + 1 = 3$ if and only if monkeys can fly**

$1+1=3$ is false. Monkeys cannot fly, so that is false as well. Both false, so
they match.

$$\boxed{\text{(iii) TRUE}}$$

**(iv) $0 > 1$ if and only if $2 > 1$**

$0 > 1$ is false. $2 > 1$ is true. The values disagree.

$$\boxed{\text{(iv) FALSE}}$$

> [!warning] Part (iii) is the whole question: two false statements give a TRUE biconditional
> A biconditional asserts that the two sides have the **same** truth value, not
> that either of them is true. Answering "false, because $1+1 \ne 3$" misreads
> the claim entirely.
>
> A quick way to see it: $P \leftrightarrow Q$ is the negation of
> $P \oplus Q$, the exclusive or. So "false if and only if false" is true, and
> "true if and only if false" is false. Parts (i) and (iii) are both
> true-and-true or false-and-false; parts (ii) and (iv) are both mixed.

> [!note] Why this distinction shows up in engineering
> Two sensors that both report "not faulty" do not by themselves certify that the
> system is healthy: they may share a common cause. Logic built on
> $\leftrightarrow$ assumes the two statements are independent, and safety
> arguments that conflate "same truth value" with "both true" fail in exactly the
> way part (iii) demonstrates.

---

## Question 7

### **(a) Suppose that $a$ and $b$ are integers, $a \equiv 11 \pmod{19}$ and $b \equiv 3 \pmod{19}$. Find the integer $c$ with $0 \le c \le 18$ such that (i) $c \equiv 7a + 3b \pmod{19}$, (ii) $c \equiv a^3 + 4b^3 \pmod{19}$.**

*[Marks: 03, CO: 2]*

Congruence behaves like equality under addition, subtraction and
multiplication, so every part is computed by substituting the residues and
reducing at the end.

**(i) $c \equiv 7a + 3b \pmod{19}$**

$$
7a + 3b \equiv 7(11) + 3(3) = 77 + 9 = 86 \pmod{19}
$$

Divide: $86 = 19(4) + 10$.

$$\boxed{c = 10}$$

**(ii) $c \equiv a^3 + 4b^3 \pmod{19}$**

Reduce the powers first, which keeps the numbers small:

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

$$\boxed{c = 14}$$

> [!info] Direct substitution confirms both
> **Part (i).** $7(11) + 3(3) = 86$, and $86 = 19(4) + 10$, so $c = 10$.
>
> **Part (ii).** $11^3 + 4 \cdot 3^3 = 1331 + 108 = 1439$, and
> $1439 = 19(75) + 14$, so $c = 14$.
>
> Both remainders satisfy $0 \le c \le 18$, which the question requires. Note that
> reducing the powers in (ii) is a convenience, not a requirement: the direct
> route gives the same answer, which is the point of the check.

> [!warning] Write the question's expression into the working before computing anything
> With $a \equiv 11$ and $b \equiv 3$ the products $ab$ and the sums $a + b$ also
> reduce to $14$, which is part (ii)'s answer. A draft that computes $ab$ and
> $a+b$ instead of $7a + 3b$ and $a^3 + 4b^3$ therefore produces a part (ii) that
> looks right and a part (i) that is wrong.
>
> The safeguard is procedural rather than mathematical: write
> "$7a + 3b \equiv 7(11) + 3(3) = 86$" on the page, not just "part (i): 14". Once
> the expression is visible, a substituted expression cannot pass unnoticed,
> because it is visibly not the one that was asked for.

---

### **(b) Solve $3^{644} \bmod 645$ using a well-known algorithm.**

*[Marks: 03, CO: 3]*

The well-known algorithm is **repeated squaring**, also called the
square-and-multiply method. It exploits $x^{2k} = (x^k)^2$, so each squaring
roughly doubles the exponent covered while the numbers stay small.

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

$$\boxed{3^{644} \bmod 645 = 36}$$

> [!info] A completely different route, by the Chinese remainder theorem
> Factor $645 = 3 \times 5 \times 43$ and work modulo each prime:
>
> | Modulus | Result | Working |
> | :-- | :-- | :-- |
> | $3$ | 0 | $3^{644}$ is a multiple of 3 |
> | $5$ | 1 | $3^4 \equiv 1$ and $644 = 4(161)$ |
> | $43$ | 36 | $\phi(43) = 42$, $644 = 42(15)+14$, so $3^{644} \equiv 3^{14} = 3^8 \cdot 3^4 \cdot 3^2 \equiv 25 \times 38 \times 9 \equiv 36$ |
>
> Checking $36$: $36 \bmod 3 = 0$ ✓, $36 \bmod 5 = 1$ ✓, $36 \bmod 43 = 36$ ✓.
> Both routes give $36$, which is a genuine confirmation because they share no
> intermediate arithmetic.

> [!warning] Two traps in this computation
> **Do not let the residues grow.** Reducing after every squaring is what keeps
> the largest intermediate at $486^2 = 236196$. Squaring without reducing reaches
> $3^{644}$ with about $307$ digits, which is not wrong so much as pointless.
>
> **$3^{256} \equiv 81$ is not a typo.** The sequence is periodic in a way that
> looks wrong at first glance, and $81 = 3^4$ is exactly what makes $3^{512}$
> come out equal to $3^8$. If one of these entries surprises you, recompute it
> rather than adjusting it to look tidier.

> [!note] Which algorithm the question means
> "A well-known algorithm" for modular exponentiation is repeated squaring.
> **Fermat's little theorem** would also work, via
> $3^{644} = 3^{\phi(645) + 164}$ with $\phi(645) = 268$, but the modulus is not
> prime, so the theorem only applies to each prime factor separately, which is
> the CRT route above rather than a single reduction.
>
> Repeated squaring is the right answer to the question as asked because it
> applies to any modulus, prime or not, and takes about $\log_2 644 = 10$
> squarings.

---

### **(c) Find the greatest common divisor of 414 and 662 using the extended Euclidean algorithm.**

*[Marks: 02, CO: 2]*

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

From the last division, $2 = 166 - 2 \times 82$. Substitute $82 = 248 - 166$:

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

$$\boxed{\gcd(414, 662) = 2, \qquad 8(414) - 5(662) = 2}$$

> [!info] The forward method gives the same coefficients
> The forward extended Euclidean algorithm, which carries the coefficients
> $(s, t)$ alongside the remainders rather than back-substituting, returns
> $(2, 8, -5)$: gcd $2$, $s = 8$, $t = -5$. The identity
> $8 \times 414 + (-5) \times 662 = 2$ verifies it.

> [!note] Why the extended form is worth the extra work
> Ordinary Euclid gives the gcd. The extended form also gives the Bezout
> coefficients $s$ and $t$, and that is what modular inverses are built from: if
> $\gcd(a, n) = 1$ then $sa + tn = 1$, so $s$ is the inverse of $a$ modulo $n$.
>
> Solving congruences by hand almost always needs this, so the question is really
> marking one skill that pays for itself in the parts to come.
>
> One habit saves time here: because $414$ and $662$ are both even, the gcd is
> even, which flags $2$ as plausible before the last division is reached.

---

### **(d) Show that if $a$ and $b$ are positive integers then $(2^a - 1) \bmod (2^b - 1) \equiv 2^{a \bmod b} - 1$.**

*[Marks: 02, CO: 2]*

**Step 1. Write $a = qb + r$** with $q = \lfloor a/b \rfloor \ge 0$ and
$r = a \bmod b$, so $0 \le r < b$.

**Step 2. Reduce the power.**

$$
2^a - 1 = 2^{qb+r} - 1 = 2^r\left(2^{qb}\right) - 1
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

Since $r = a \bmod b$:

$$\boxed{(2^a - 1) \bmod (2^b - 1) \equiv 2^{a \bmod b} - 1}$$

**Step 5. The residue really is the least one.** Since $0 \le r < b$ we have
$0 \le 2^r - 1 < 2^b - 1$, so $2^r - 1$ is the actual remainder and not merely a
congruent value. This is what makes the statement an equality of remainders rather
than only a congruence.

> [!info] Worked cases
> | $a$ | $b$ | $(2^a-1) \bmod (2^b-1)$ | $2^{a \bmod b} - 1$ |
> | --: | --: | --: | --: |
> | 13 | 5 | 7 | 7 |
> | 10 | 3 | 1 | 1 |
> | 20 | 6 | 3 | 3 |
> | 9 | 4 | 1 | 1 |
> | 7 | 7 | 0 | 0 |
>
> The identity was checked directly for every pair with $1 \le a \le 29$ and
> $1 \le b \le 11$, with no counterexample. The $a = b$ row is the boundary case
> worth noting: $a \bmod b = 0$ and $2^0 - 1 = 0$, which is correct since
> $2^b - 1$ divides itself.

> [!note] The general result, and why it matters
> Nothing above used anything specific to the base $2$. The identical proof works
> for any base $c$:
> $(c^a - 1) \bmod (c^b - 1) \equiv c^{a \bmod b} - 1$.
>
> This is the standard trick for simplifying large modular exponentiations, and it
> is why $3^{644} \bmod 645$ in part (b) collapses so cheaply whenever the modulus
> happens to have the form $c^k - 1$. $645$ is not of that form, which is exactly
> why (b) needs repeated squaring instead.

---

## Question 8

### **(a) Define Fermat's little theorem. Use the construction in the proof of the Chinese remainder theorem to find all solutions to $x \equiv 2 \pmod 3$, $x \equiv 1 \pmod 4$, $x \equiv 3 \pmod 5$.**

*[Marks: 04, CO: 2]*

**Fermat's little theorem.** If $p$ is prime and $\gcd(a, p) = 1$, then

$$\boxed{a^{p-1} \equiv 1 \pmod p}$$

Equivalently $a^p \equiv a \pmod p$ for every integer $a$, with no coprimality
condition needed. Worked cases: $2^2 = 4 \equiv 1 \pmod 3$, and
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

**Alternative verification: combining two congruences at a time.** Combine the first two,
$x \equiv 2 \pmod 3$ and $x \equiv 1 \pmod 4$. Write $x = 2 + 3k$ and substitute
into the second:

$$
2 + 3k \equiv 1 \pmod 4 \quad \Longrightarrow \quad 3k \equiv -1 \equiv 3 \pmod 4
$$

Since $3^{-1} \equiv 3 \pmod 4$, $k \equiv 3 \times 3 = 9 \equiv 1 \pmod 4$. Hence
$k = 1 + 4m$ and

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

$$\boxed{x \equiv 53 \pmod{60}}$$

**Verify all three.**

$$
53 \bmod 3 = 2 \quad \checkmark \qquad 53 \bmod 4 = 1 \quad \checkmark \qquad 53 \bmod 5 = 3 \quad \checkmark
$$

Since $N = 3 \cdot 4 \cdot 5 = 60$, the complete solution set is $x = 53 + 60k$
for every integer $k$.

> [!info] Exhaustive search confirms uniqueness
> Testing every residue $x$ from 0 to 59 against all three congruences returns
> exactly one, namely $53$. The solution is therefore unique modulo 60, which is
> what CRT guarantees when the moduli are pairwise coprime.
>
> Note that $4$ is **not** prime, so Fermat does not apply to it. Coprimality is
> all CRT needs, and $\gcd(3,4) = \gcd(4,5) = \gcd(3,5) = 1$.

> [!note] Solving by inspection, as a cheaper check
> $x \equiv 1 \pmod 4$ and $x \equiv 3 \pmod 5$ together give $x \equiv 13 \pmod{20}$.
> The values below 60 are $13$, $33$, $53$, and of those only $53$ is $2 \pmod 3$.
>
> For three small congruences this is faster than the general construction, and
> it is a good check on the formula-based route because it shares none of its
> arithmetic.

> [!warning] Fermat needs the modulus to be prime, and coprimality on the base
> Two conditions, both easy to forget. $2^{10} \equiv 2 \pmod{10}$ does not give
> $2^9 \equiv 1 \pmod{10}$, because $10$ is not prime. And $a \equiv 0 \pmod p$ has
> no inverse, so the coprimality requirement is genuine rather than a technicality.
>
> When a modulus is composite but its factors are known, the route is to reduce
> modulo each prime factor separately and combine, which is what the CRT route
> does.

---

### **(b) There are four major auto routes from Boston to Detroit and six from Detroit to Los Angeles. How many major auto routes are there from Boston to Los Angeles via Detroit?**

*[Marks: 02, CO: 3]*

**Setting up.** A route via Detroit is fully described by **one** choice from
Boston to Detroit **and one** choice from Detroit to Los Angeles. There is no
other freedom, and the order is fixed by the geography: Boston first, Detroit
second, Los Angeles third.

This is the **product rule**, also called the multiplication principle:

$$
\text{number of routes} = 4 \times 6
$$

$$\boxed{24 \text{ routes}}$$

> [!info] Check
> The four Boston choices against the six Detroit choices form a $4 \times 6$ grid
> of $24$ cells, one route each. The direct product confirms $4 \times 6 = 24$.

> [!warning] The sum rule does not apply here
> The **sum rule** applies to mutually exclusive alternatives: either go through
> Detroit or through Chicago, never both. Here every route *must* go through
> Detroit, so the choices are sequential rather than alternative, and the product
> rule is the one that fits.
>
> The quickest way to tell the two apart: ask whether the choices happen one after
> another (product) or instead of one another (sum). "Via Detroit" is the clearest
> possible example of the first kind.

> [!note] Why permutations do not apply either
> A route is fixed by its two legs, so choosing leg 1 then leg 2 already fixes the
> whole route. No reordering is possible or meaningful, so this is a
> combination-like count of $24$ distinct paths, not $24$ orderings of something.
>
> If the question had asked about the round trip, the count would change shape
> entirely, because a return leg is not independent of the outward one.

---

### **(c) Give a real-world example of generalized pigeonhole principle.**

*[Marks: 02, CO: 3]*

**The principle.** If $N$ objects are placed into $k$ boxes and $N > k$, then at
least one box holds at least two objects. The **generalized** form: if
$N > mk$, then some box holds at least $m + 1$ objects.

**Real-world examples.**

1. **Birth months in a class.** With 12 months, a class of 25 students guarantees
   that at least 3 share a birth month, since $25 > 2 \times 12 = 24$. Here
   $m = 2$, $k = 12$, and $N = 25$ is the smallest class that forces a triple.
2. **Socks from a drawer.** A drawer holds only black and white socks. Drawing 5
   socks guarantees at least 3 of one colour, since $5 > 2 \times 2 = 4$.
3. **Hash tables.** Storing $n$ keys in $m$ buckets forces a collision once
   $n > m$. Keeping the load factor below 1, typically near 0.75, is what
   guarantees headroom before collisions become frequent.
4. **Servers.** A cluster with $r$ racks and $2r+1$ machines must place at least
   3 machines in one rack, since $2r + 1 > 2 \times r$.

$$\boxed{\text{More than } mk \text{ objects in } k \text{ boxes forces some box to hold } m+1}$$

> [!warning] The plain and generalized forms are different statements
> The plain principle is the case $m = 1$. The generalized form needs $N > mk$,
> which is a **stronger** condition on $N$ and yields a **stronger** conclusion.
>
> The commonest slip is to use $N > k$ when $m > 1$, which forces only *two* in a
> box rather than $m + 1$. With 25 students and 12 months, "more students than
> months" forces only a pair. The $2 \times 12 = 24$ threshold is what forces a
> triple.

> [!note] Reading off $m$ and $k$ from the story
> In every example, $k$ is the number of boxes and is counted directly from the
> story: 12 months, 2 colours, $m$ buckets, $r$ racks. Then $m$ is the number
> above which you want a guarantee, and $N$ must exceed $mk$.
>
> Hashing is the case worth internalising, because the principle is not an
> accident there but a design constraint. A table that guarantees no collision at
> all would need one bucket per key, which defeats the purpose of hashing.

---

### **(d) Let $d$ be a positive integer. Show that among any group of $d+1$ (not necessarily consecutive) integers there are two with exactly the same remainder when they are divided by $d$.**

*[Marks: 02, CO: 3]*

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

**Step 3. Apply the pigeonhole principle.** There are $d+1$ integers placed into
$d$ boxes, and $d + 1 > d$. By the pigeonhole principle, at least one box contains
two or more integers.

**Step 4. Conclude.** Two integers $a_1, a_2$ share a box, so they share a
remainder. Writing $a_1 = q_1 d + r$ and $a_2 = q_2 d + r$ and subtracting gives

$$
a_1 - a_2 = (q_1 - q_2)d
$$

hence $d$ divides $a_1 - a_2$, which is exactly the statement that the two have the
same remainder on division by $d$.

$$\boxed{\text{Any } d+1 \text{ integers include two congruent modulo } d}$$

> [!info] Explicit cases
> | $d$ | Example with a forced repetition | Remainders |
> | --: | :-- | :-- |
> | 1 | $0, 0$ | $0, 0$ |
> | 3 | $0, 1, 2, 0$ | $0, 1, 2, 0$ |
> | 5 | $0, 1, 2, 3, 4, 0$ | $0, 1, 2, 3, 4, 0$ |
>
> In each case $d+1$ integers are given and $d$ remainders are available, so the
> repetition is forced rather than arranged.

> [!note] The bound is sharp, and that is what makes this a theorem
> With only $d$ integers no repetition is forced: take $0, 1, 2, \dots, d-1$,
> whose remainders are all distinct. Hence $d + 1$ is the **smallest** number of
> integers that guarantees a collision.
>
> The word "not necessarily consecutive" in the question is what rules out the
> other obvious route. If the integers were consecutive you could simply look at
> $d$ consecutive remainders, which cycle through all $d$ values and then repeat.
> The hypothesis has to be the general one for the pigeonhole argument to be
> needed at all.

> [!note] What this is used for
> This is the statement behind every proof of the pigeonhole principle for
> congruences, and behind the fact that $x \equiv y \pmod d$ has infinitely many
> solutions while $x \equiv y \pmod n$ with the same residue class has at most
> $\gcd(x-y, n)$ distinct residues.
>
> It is also the reason a hash table with $m$ buckets cannot hold $m+1$ distinct
> keys without a collision. Same counting argument, different words.
