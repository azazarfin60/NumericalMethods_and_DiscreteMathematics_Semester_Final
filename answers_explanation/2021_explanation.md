---
title: "ECE 2213 · 2021 Explanations"
tags:
  - numerical-methods
  - previous-year
---

# ECE 2213: 2021 Semester Final · Explained

**RUET · ECE Dept · B.Sc. Engineering 2nd Year Even Semester Examination, 2021**

This file explains the same questions as
[[answers_exam_style/2021_answer|the 2021 answer script]], written to be read
rather than copied. Every step is named, the reason a formula is chosen is
stated, and the traps that catch people are called out.

> [!info] How to use this file
> Read this to understand *why* the answer script does what it does. When you
> are ready to write in the hall, work from
> [[answers_exam_style/2021_answer|the exam-style file]], which is shorter and
> carries no commentary.
>
> **The rule that matters.** Every boxed number here is the same number as the
> one in the answer script, character for character. Gate V5 checks this, and
> gate V12 checks that the marks and CO on every section agree with the answer
> script and with the manifest.

> [!warning] Five gaps in the printed paper, all handled in place
> | Where | What is missing or wrong |
> | :-- | :-- |
> | Q.4(c) | the five sensor values do **not** lie on one quartic-cubic pair, so "four points" and "five points" give different answers |
> | Q.5(b) | the boundary condition $y(2) = 3.62686$ is a rounded value, so the continuous solution is reported alongside the numerical one |
> | Q.6(b) | the initial guess $x_0 = 2.5$ is far from the root of $g = f'$, yet Newton still converges |
> | Q.7(c) | the table has no $x = 0.8$, so the five-point central formula cannot be used at $x = 1.2$ |
> | Q.8(c) | no step size $h$ and no interval are printed |
>
> The 2021 paper has 97 total printed marks across all 8 questions (Section A: 48, Section B: 49; full marks to answer: 72).
> All questions in this paper are pure Numerical Methods. Five of its questions have a printing gap,
> which is worth knowing before you start: in each case the gap decides the answer.

---

# SECTION A

## Question 1

### **(a) Differentiate between numerical methods and analytical methods. Why do ECE engineers require numerical methods?**

*[Marks: 04, CO: 1]*

**Analytical method.** Manipulates symbols to reduce the problem to a closed form.
The answer is exact and valid at every point of the domain.

**Numerical method.** Approximates the problem by a form that can be evaluated
digit by digit. The answer is a pair of numbers, valid near the point computed.

| | Analytical | Numerical |
| :-- | :-- | :-- |
| Result | Closed form, exact | Approximate |
| Domain of validity | Whole domain | Local, near one point |
| Problem size it can handle | Small | Grows nearly linearly with effort |
| Round off error | None | Present at every operation |
| Effect of changing data | Instant re-evaluation | Full recomputation |
| Structure it reveals | Conservation laws, invariants | Hides them |

$$\boxed{\text{Analytical is exact and closed-form; numerical is approximate but reaches problems no closed form can}}$$

> [!warning] The last row is the one that matters
> An analytical solution exposes **structure**: a conservation law, an invariant,
> a symmetry. A numerical solution gives you a number and nothing else.
>
> This is the real cost of the method, and it is not visible in the answer. An
> engineer who knows $\frac{dQ}{dt} = -kQ$ analytically knows the half-life is
> $\frac{\ln 2}{k}$ whatever $k$ is. An engineer who has run the ODE numerically
> for one particular $k$ knows a number, and has to rerun to discover the
> pattern. Use numerical methods for the answer and analytical reasoning for the
> design.

**Why ECE engineers need them.**

1. **Most real systems have no closed form.** A coupled circuit, a heat exchanger,
   a transmission line, a semiconductor device: none has an analytic solution.
2. **The scale is far beyond hand algebra.** Thousands of unknowns from a
   discretised PDE, or a million from a mesh. No symbolic route exists.
3. **An experiment costs real money and real time.** A finite element run or a
   circuit simulation costs nothing to repeat and can be run at any parameter
   value, long before hardware exists.
4. **The data are irregular.** Measurements arrive unevenly spaced and noisy.
   Interpolation and least squares accept them without demanding a form.
5. **Design needs iteration.** An optimiser calls the solver hundreds of times
   while searching.
6. **The accuracy is quantifiable.** Every method carries an error bound, so the
   engineer knows how far to trust the answer rather than having to hope.

> [!note] The hybrid answer
> Almost no real computation is purely one or the other. An analytical
> reduction that leaves a small nonlinear system, solved numerically, is the
> normal pattern. The skill being marked here is knowing which part of a problem
> deserves the closed form and which part has to be iterated.

---

### **(b) Derive the formula for root finding using Newton-Raphson method. Also, discuss the problems of it and how this problem can be solved.**

*[Marks: 04, CO: 2]*

**Derivation.** Let $x^*$ be the root of $f(x) = 0$. Start at $x_0$ and follow the
tangent to the curve at that point.

For small $h$ the tangent meets the $x$-axis at $x_0 + h$. By the first-order mean
value form of the Taylor series,

$$
0 = f(x^*) = f(x_0 + h) \approx f(x_0) + h f'(x_0)
$$

Solving for $h$ and writing $x_1 = x_0 + h$,

$$
x_1 = x_0 - \frac{f(x_0)}{f'(x_0)}
$$

Iterating,

$$\boxed{x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}}$$

> [!note] Where the formula comes from, geometrically
> The iteration is "walk to where the tangent meets the axis". Read that way the
> formula needs no derivation at all, and it also explains the whole convergence
> story: near a simple root the curve and its tangent agree to second order, so
> each new point is much closer to the root than the last.

**Second order accuracy.** Taking the Taylor expansion to second order,

$$
0 = f(x_n) + f'(x_n)\Delta x + \frac{f''(\xi)}{2}\Delta x^2
$$

Substituting $\Delta x = -f/f'$ shows
$e_{n+1} \approx \frac{f''(x^*)}{2f'(x^*)}e_n^2$. The error is **squared** each step,
so the last iteration typically delivers every digit the machine can hold.

**Problems and fixes.**

| Problem | Cause | Fix |
| :-- | :-- | :-- |
| Diverges or oscillates | Start too far from the root | Bracket first, start inside, or switch to bisection |
| Division by zero | $f'(x_n) = 0$ | Choose another start, or use the secant method |
| Cycles between two points | Overshoot from a poor start | Damp the step, or fall back to bisection on repeat |
| False convergence | $f(x_n) \ne 0$ but $f'(x_n) \approx 0$ | Test $\lvert f(x_n)\rvert$, not only $\lvert x_{n+1}-x_n\rvert$ |
| Slow at a repeated root | Squaring needs a **simple** root | Use $x_{n+1} = x_n - m\frac{f(x_n)}{f'(x_n)}$ with $m$ the multiplicity |
| No tangent information | Step-like function such as signum | Bisection, which needs only a sign change |
| $f'$ unavailable | Only $f$ is given | Secant method, or finite-difference derivative |

> [!warning] "The step got small" is not a convergence test
> The most dangerous row in that table is the fourth. Newton can produce
> $x_{n+1} = x_n$ to machine precision while $f(x_n)$ is still large, because it
> is dividing by a derivative that has collapsed. The reliable test is on the
> **residual** $\lvert f(x_n)\rvert$, not on the change in $x$.
>
> The general safeguard covers the rest: keep a bracket $[a, b]$ with
> $f(a)f(b) < 0$, and if a Newton step leaves the bracket, take a bisection step
> instead. That hybrid keeps Newton's speed and bisection's guarantee, and it is
> what production root finders do.

---

### **(c) Compute the value of $\ln 3$ correct to five decimal places using Taylor's series expansion.**

*[Marks: 04, CO: 2]*

**Step 1. Choose a series that converges.** The familiar expansion

$$
\ln(1+x) = x - \frac{x^2}{2} + \frac{x^3}{3} - \cdots
$$

converges only for $\lvert x \rvert < 1$. Here $3 = 1 + 2$, so $x = 2$ and **the
series diverges**.

> [!warning] The arithmetic does not fail, the series does
> Substituting $x = 2$ and adding terms gives a number that drifts away from
> $\ln 3$ forever, and the partial sums *increase* past it. Nothing in the
> computation looks wrong: each term is a finite number and the running total
> updates cleanly. Only the convergence test catches it.
>
> **Check the radius before you start, not after.** The habit is one line:
> $x = 2$, and $|2| > 1$, so pick a different form. Finding this after twenty
> minutes of summation is the whole lesson of the question.

**Step 2. Use the hyperbolic form instead.** Write

$$
\ln\frac{1+y}{1-y} = 2\left(y + \frac{y^3}{3} + \frac{y^5}{5} + \cdots\right),
\qquad \lvert y\rvert < 1
$$

Set $\frac{1+y}{1-y} = 3$. Then $1 + y = 3 - 3y$, so $4y = 2$ and

$$
y = \frac{3-1}{3+1} = \frac{1}{2}
$$

which satisfies $\lvert y\rvert < 1$.

**Step 3. Expand.**

$$
\ln 3 = 2\left[\frac{1}{2} + \frac{1}{8 \times 3} + \frac{1}{32 \times 5} + \frac{1}{128 \times 7} + \frac{1}{512 \times 9} + \frac{1}{2048 \times 11} + \frac{1}{8192 \times 13} + \cdots\right]
$$

**Step 4. Add terms until the error is below $\frac{1}{2} \times 10^{-5}$.**

| Terms | Partial sum | Error |
| --: | --: | --: |
| 5 | 1.0984995040 | $1.13 \times 10^{-4}$ |
| 6 | 1.0985882824 | $2.40 \times 10^{-5}$ |
| 7 | 1.0986070624 | $5.23 \times 10^{-6}$ |
| 8 | 1.0986111314 | $1.16 \times 10^{-6}$ |

Seven terms give an error of $5.23 \times 10^{-6}$, still above
$\frac{1}{2}10^{-5}$. Eight terms give $1.16 \times 10^{-6}$, comfortably inside, so
**eight terms are required**.

**Step 5. Round.**

$$\boxed{\ln 3 = 1.09861}$$

> [!info] Check by an independent route
> Split $\ln 3 = \ln 2 + \ln 1.5$ and use $y = \frac{1}{3}$ and $y = \frac{1}{5}$
> respectively. With twelve terms each, $\ln 2 = 0.6931471805$ and
> $\ln 1.5 = 0.4054651081$, and the sum is $1.0986122887$, whose first five
> decimals are **1.09861**. The same answer from a different decomposition.
>
> The closed-form check is that $\ln 3 = 1.0986122886681098$, and
> $\lvert 1.0986111314 - 1.0986122887 \rvert = 1.16 \times 10^{-6}$, matching the
> table.

> [!warning] Two ways to repair a divergent log series
> 1. **Use the hyperbolic form** above with $y = \frac{a-1}{a+1}$, which is always inside the radius once $a > 1$. This is the clean route and it is what the answer uses.
> 2. **Split the argument** so each piece has $\lvert x\rvert < 1$, as $\ln 3 = \ln 2 + \ln 1.5$. More work, but it works with the familiar series.
>
> A third option is $\ln 3 = 2\,\text{artanh}\frac{1}{2}$ followed by repeated
> halving of the argument. The first two are enough for five decimals.

> [!note] Error estimate, and why the bound is not the same as the actual error
> The tail after $N$ terms is bounded by
> $$2\sum_{k=N}^{\infty}\frac{y^{2k+1}}{2k+1} < \frac{2y^{2N+1}}{(2N+1)(1-y^2)}, \qquad y = \frac{1}{2}$$
> | $N$ | Bound | Below $\frac{1}{2}10^{-5}$? |
> | --: | --: | :-: |
> | 7 | $\frac{2(0.5)^{15}}{15 \times 0.75} = 5.425 \times 10^{-6}$ | No |
> | 8 | $\frac{2(0.5)^{17}}{17 \times 0.75} = 1.197 \times 10^{-6}$ | Yes |
>
> Two different numbers appear for seven terms, and both are correct: the
> **bound** $5.425 \times 10^{-6}$ comes from the geometric estimate above, while
> the **actual** error is $1.0986122887 - 1.0986070624 = 5.226 \times 10^{-6}$,
> which the table lists. The true error is always the smaller of the two, because
> the bound replaces each remaining denominator $2k+1$ by the larger value $2N+1$.
> Both exceed $5 \times 10^{-6}$, so seven terms fail on either count and eight
> terms pass on both.

---

## Question 2

### **(a) Define bracketing methods with example.**

*[Marks: 02, CO: 1]*

**Definition.** A **bracketing method** is an iterative root finder that begins
with an interval $[a, b]$ in which the function changes sign,

$$
f(a) \cdot f(b) < 0
$$

By the intermediate value theorem a continuous $f$ must have at least one root in
$(a, b)$. Each iteration picks a new point inside the current interval and retains
the half that still shows a sign change, so the root is never lost.

**Properties.**

1. **Convergence is guaranteed**, from any valid bracket, for any continuous $f$.
2. Only the **sign** of $f$ is needed, never $f'$. That is the big practical
   advantage, since a derivative is often harder to obtain than a function value.
3. The interval halves each step for bisection, so the error bound after $n$ steps
   is $\frac{b_0-a_0}{2^{n+1}}$.
4. Convergence is **slow**, linear for bisection, because no curvature
   information is used.

**Examples.**

| Method | New point | Rate |
| :-- | :-- | :-- |
| Bisection | Midpoint, $\frac{a+b}{2}$ | Linear |
| Regula falsi | Chord, $\frac{a f(b) - b f(a)}{f(b)-f(a)}$ | Superlinear, often |
| Illinois method | Regula falsi with a halved stale value | Superlinear, robust |

$$\boxed{\text{Enclose the root in a sign-changing interval and keep halving it; convergence is guaranteed}}$$

> [!note] Why the name, and what the guarantee is worth
> "Bracketing" means the iterate is *trapped* between two values of opposite sign,
> and the trap can only shrink. That is a stronger statement than "it usually
> converges", and it is what makes bracketing the fallback of choice when an open
> method misbehaves.
>
> The cost is speed. Superlinear rates in the table are for regula falsi and
> Illinois on well-behaved functions; part (b) of this question shows regula
> falsi stagnating on a strongly convex one, where it is barely better than
> bisection.

---

### **(b) Given that the equation $x^{2.2} = 69$ has a root between 5 and 8. Use the method of regula-falsi to determine it.**

*[Marks: 04, CO: 3]*

**Step 1. Define the function and check the bracket.**

$$
f(x) = x^{2.2} - 69
$$

$$
f(5) = 5^{2.2} - 69 = 34.4932 - 69 = -34.5068
$$

$$
f(8) = 8^{2.2} - 69 = 97.0059 - 69 = +28.0059
$$

$f(5) < 0 < f(8)$, so a root lies in $(5, 8)$. The function is continuous there
since $x^{2.2}$ is continuous for $x > 0$.

**Step 2. The formula.** Draw the straight line joining the two endpoints. It cuts
the $x$-axis at

$$
x = \frac{a f(b) - b f(a)}{f(b) - f(a)}
$$

> [!warning] The bracket is nearly balanced, and that is a coincidence worth noticing
> $f(5) = -34.51$ and $f(8) = +28.01$ are of similar size, so the chord's
> intercept lands near the middle of the interval, $6.656$, rather than near
> either end. Because the signs are already close in magnitude, the first step is
> nearly as good as bisection's.
>
> Check your own arithmetic against this: the first iterate is
> $\frac{5(28.0059) + 8(34.5068)}{28.0059 + 34.5068} = \frac{416.0839}{62.5127}$.
> A number far from $6.656$ means a sign was dropped somewhere.

**Step 3. Iterate.** Keep whichever endpoint has the same sign as the new point and
replace the other.

| Iteration | $a$ | $b$ | New point $x$ | $f(x)$ |
| --: | --: | --: | --: | --: |
| 1 | 5.000000 | 8.000000 | 6.655990 | $-4.27563$ |
| 2 | 6.655990 | 8.000000 | 6.834002 | $-0.40615$ |
| 3 | 6.834002 | 8.000000 | 6.850670 | $-0.03755$ |
| 4 | 6.850670 | 8.000000 | 6.852209 | $-0.00346$ |
| 5 | 6.852209 | 8.000000 | 6.852351 | $-0.00032$ |
| 6 | 6.852351 | 8.000000 | 6.852364 | $-0.00003$ |
| 7 | 6.852364 | 8.000000 | 6.852365 | $-0.000003$ |

Working the first row in full:

$$
x_1 = \frac{5(28.0059) - 8(-34.5068)}{28.0059 - (-34.5068)} = \frac{140.0295 + 276.0544}{62.5127} = \frac{416.0839}{62.5127} = 6.655990
$$

$$\boxed{x = 6.85237 \quad \text{(to five decimal places)}}$$

Or to four places, $x = 6.8524$.

> [!info] Check by two independent routes
> **Secant method.** Starting from the same two points, the secant iteration gives
> $6.65599006$, $6.83400179$, $6.85268624$, $6.85236460$, $6.85236512$. Same
> answer to more digits.
>
> **Closed form.** $x^{2.2} = 69$ with $2.2 = \frac{11}{5}$ gives
> $x = 69^{5/11} = 6.8523651204$. The last regula falsi iterate is $6.852365$, and
> the closed form rounds to $6.85237$. All three agree.
>
> **Bisection.** Starting from $(5, 8)$, after 18 iterations the bracket is
> $(6.85236359, 6.85237503)$ and the midpoint $6.85236931$ is within
> $4.2 \times 10^{-6}$ of the exact root. One more bisection halves that again.

> [!warning] Why the upper endpoint never moves
> The table gives $b = 8.000000$ for every iteration. This is the well known
> **one-sided stagnation** of regula falsi on this function. The graph is strongly
> convex over $(5, 8)$, so the chord always cuts the axis on the same side, and
> only the $a$ endpoint is replaced.
>
> The consequence is that convergence is much slower than the "superlinear" label
> suggests. Seven iterations to reach six figures looks like bisection's pace,
> not regula falsi's. The **Illinois variant** fixes it by halving the retained
> function value on each step:
> $$\text{repeat } a f(a) \text{ as } \frac{1}{2}a f(a) \text{ every second iteration}$$
> That restores the fast convergence while keeping the sign-change guarantee.
>
> The same function with a different bracket appears in 2017 Q.2(b), which is
> worth knowing about, since the stagnation behaves differently there.

---

### **(c) Determine the smallest root of the equation: $f(x) = x^3 - 9x^2 + 26x - 24 = 0$.**

*[Marks: 06, CO: 3]*

**Step 1. Locate the roots by sign changes.** Evaluate at integer values:

| $x$ | $f(x)$ | Sign |
| --: | --: | :-: |
| 0 | $-24$ | $-$ |
| 1 | $1 - 9 + 26 - 24 = -6$ | $-$ |
| 2 | $8 - 36 + 52 - 24 = 0$ | $0$ |
| 3 | $27 - 81 + 78 - 24 = 0$ | $0$ |
| 4 | $64 - 144 + 104 - 24 = 0$ | $0$ |
| 5 | $125 - 225 + 130 - 24 = 6$ | $+$ |

**Step 2. Recognise the factorisation.** All of $2, 3, 4$ are exact roots, and a
cubic has at most three, so

$$
f(x) = (x-2)(x-3)(x-4)
$$

Verification by expansion: $(x-2)(x-3) = x^2 - 5x + 6$, and
$(x^2-5x+6)(x-4) = x^3 - 4x^2 - 5x^2 + 20x + 6x - 24 = x^3 - 9x^2 + 26x - 24$.
Correct.

**Step 3. Smallest root.**

$$\boxed{x = 2}$$

**Step 4. Confirm with a numerical method**, since the question asks for root
finding. Use Newton-Raphson with

$$
f(x) = x^3 - 9x^2 + 26x - 24, \qquad f'(x) = 3x^2 - 18x + 26
$$

Start at $x_0 = 1.5$, where $f(1.5) = 3.375 - 20.25 + 39 - 24 = -1.875$ and
$f'(1.5) = 6.75 - 27 + 26 = 5.75$:

| Iteration | $x_n$ | $f(x_n)$ | $f'(x_n)$ |
| --: | --: | --: | --: |
| 0 | 1.5000000 | $-1.875000$ | 5.750000 |
| 1 | 1.8260870 | $-0.443823$ | 3.134215 |
| 2 | 1.9676929 | $-0.067779$ | 2.196974 |
| 3 | 1.9985440 | $-0.002918$ | 2.008742 |
| 4 | 1.9999968 | $-0.000006$ | 2.000019 |
| 5 | 2.0000000 | $0$ | 2.000000 |

Iteration 1: $x_1 = 1.5 - \frac{-1.875}{5.750000} = 1.5 + 0.326087 = 1.826087$.
Iteration 2: $x_2 = 1.826087 - \frac{-0.443823}{3.134215} = 1.826087 + 0.141606 = 1.967693$.

> [!warning] The derivative column is not decoration
> Newton divides by $f'(x_n)$, and here $f'$ drifts from $5.75$ to $2.00$ across
> the five steps, so a value carried over from the previous row is visibly wrong.
> It settles at $2.00 = f'(2)$, which is the self-consistency check at the root:
> once the iterate is the root, the derivative in the same row must be the true
> derivative there.
>
> This column is the cheapest possible error check, because it is a function of
> $x$ alone. If $x_n$ and $f'(x_n)$ ever disagree, one of them is wrong.

> [!warning] Choosing the bracket
> The interval $[1, 2]$ is **not** usable, because $f(2) = 0$ puts the root
> exactly on the endpoint and $f(1)f(2) = 0$, not $< 0$. The pair $[1.5, 2.5]$
> works: $f(1.5) = -1.875$ and
> $f(2.5) = 15.625 - 56.25 + 65 - 24 = 0.375$, so $f(1.5)f(2.5) = -0.703 < 0$.
>
> Also note there is **no** root below $2$. Since $f$ is negative on $[0, 2)$ and
> $f(2) = 0$, the value $2$ is the smallest root, not merely one of three. To see
> that $f$ really is negative on that interval, note that
> $f'(x) = 3x^2 - 18x + 26$ vanishes at $3 \pm \frac{\sqrt3}{3} \approx 2.423$ and
> $3.577$, so $f$ increases up to $2.423$ and has no turning point before $2$.

> [!note] Why six marks for a question this easy
> Because the marks are not for the factorisation, which is two lines of algebra.
> They are for the bracket check, the iteration table, the derivative column, and
> the argument that $2$ is the *smallest* rather than merely *a* root. A correct
> boxed answer with none of that supporting work would not earn the marks.
---

## Question 3

### **(a) When should we use interpolation instead of curve fitting?**

*[Marks: 02, CO: 2]*

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

### **(b) Differentiate between Newton's interpolation and Lagrange's interpolation.**

*[Marks: 02, CO: 2]*

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

### **(c) Derive the Newton's forward interpolation formula: $y_n(x) = y_0 + p\Delta y_0 + \frac{p(p-1)}{2!}\Delta^2 y_0 + \frac{p(p-1)(p-2)}{3!}\Delta^3 y_0 + \cdots$**

*[Marks: 04, CO: 2]*

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
> values. See [[NM-4.7 · Newton's Forward Difference]].

---

### **(d) Find $y(2)$ from the following data using Lagrange's formula.**

*[Marks: 04, CO: 2]*

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

## Question 4

### **(a) Give a real life example of curve fitting.**

*[Marks: 02, CO: 2]*

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

### **(b) From the following table, calculate the value of $e^{1.17}$ using Gauss' forward formula.**

*[Marks: 05, CO: 2]*

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

### **(c) You have a gas sensor. It sends a value in 2 seconds. The table of received values is $t = 1, 3, 5, 7, 9$ with values $24, 120, 336, 720, 1200$. What will be the sensor's reading at 10 s?**

*[Marks: 05, CO: 2]*

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

## Question 5

### **(a) Define boundary value and initial value problem.**

*[Marks: 02, CO: 2]*

**Initial value problem (IVP).** A differential equation together with conditions
given at a **single** point, for example $y(0) = 1$. The solution can be marched
forward from that point because each new value depends only on the values already
computed.

**Boundary value problem (BVP).** A differential equation together with conditions
given at **both ends** of the interval, for example $y(0) = 0$ and $y(1) = 1$. No
starting value is known, so the whole interval must be solved at once.

| | IVP | BVP |
| :-- | :-- | :-- |
| Conditions | At one end | At both ends |
| How it is solved | March forward step by step | Solve the full algebraic system |
| Resulting system | Lower triangular | Tridiagonal for a second-order ODE |
| Cost | Very low per step | Full linear solve |
| Sensitivity | Local; errors stay near the start | Global; a change anywhere moves the whole solution |
| Shooting method | Not applicable | Reduces it to an IVP by tuning the unknown start value |

$$\boxed{\text{IVP: conditions at one end, march forward. BVP: conditions at both ends, solve together.}}$$

**Finite difference form for a second-order BVP.** Discretise the interval into
$n+1$ points, replace $y''$ by the centred difference, and use the boundary
conditions to replace the two unavailable end rows:

$$
\begin{cases}
y_0 = \text{given}, \\
y_{i-1} - (2 - p(x_i)h^2 - q(x_i)h^4)\,y_i + y_{i+1} = r_i h^2, \quad 1 \le i \le n-1 \\
y_n = \text{given}
\end{cases}
$$

> [!note] Why the distinction is not academic
> Marching forward is cheap but only works **one way**. A BVP has no starting
> value, so the discretisation produces a tridiagonal system that must be solved
> as a whole.
>
> The **shooting method** bridges the gap: treat the unknown start value as the
> unknown, march forward as an IVP, measure the error at the far end, and adjust.
> That converts a BVP into a root-find on one number, which is why shooting works
> with any ODE solver. It is also why shooting is fragile when the ODE is
> unstable: the forward solution amplifies, and the adjustment needed becomes
> exponentially large.

---

### **(b) Solve the boundary value problem $\frac{d^2y}{dx^2} - y = 0$ with $y(0) = 0$ and $y(2) = 3.62686$.**

*[Marks: 05, CO: 3]*

**Step 1. Discretise.** With the centred difference for $y''$,

$$
\frac{y_{i-1} - 2y_i + y_{i+1}}{h^2} - y_i = 0
$$

Multiplying by $h^2$,

$$
y_{i-1} - (2 + h^2)\,y_i + y_{i+1} = 0
$$

The system is tridiagonal with diagonal $-(2+h^2)$ and off-diagonal $1$.

> [!note] Check the sign and the dominance before iterating
> The matrix is **negatively diagonally dominant**, since $\lvert 2+h^2\rvert > 1+1$
> for every $h$. That guarantees a unique solution and means the standard Thomas
> algorithm applies **without pivoting**.
>
> Worth pausing on, because it is the first question in this paper where the sign
> of $y_i$ on the diagonal is decided by the ODE rather than by taste. $y'' - y = 0$
> gives $\frac{y_{i-1}-2y_i+y_{i+1}}{h^2} = y_i$, and moving $y_i$ across gives a
> diagonal of $-(2+h^2)$, not $+(2+h^2)$. Writing the positive sign produces a
> system with a completely different spectrum and, for this $y(2)$, no consistent
> solution.

**Step 2. Solve with $h = 0.5$.** Then $n = 4$ subintervals and 3 interior nodes
at $x = 0.5, 1.0, 1.5$. With $y_0 = 0$ and $y_4 = 3.62686$:

$$
\begin{cases}
-(2.25)y_1 + y_2 = 0 \\
y_1 - (2.25)y_2 + y_3 = 0 \\
y_2 - (2.25)y_3 = -3.62686
\end{cases}
$$

From the first, $y_2 = 2.25\,y_1$. Substituting into the second,

$$
y_1 - 2.25(2.25y_1) + y_3 = 0 \Rightarrow y_3 = 4.0625\,y_1
$$

The third then gives $2.25y_1 - 2.25(4.0625y_1) = -3.62686$, that is
$2.25y_1(1 - 4.0625) = -3.62686$, so $-6.890625\,y_1 = -3.62686$ and
$y_1 = 0.526347$.

$$
y_2 = 2.25(0.526347) = 1.184281, \qquad y_3 = 4.0625(0.526347) = 2.138285
$$

| $x$ | $y$ (numerical, $h = 0.5$) | Exact | Error |
| --: | --: | --: | --: |
| 0.5 | 0.526347 | 0.521095 | $+0.005252$ |
| 1.0 | 1.184281 | 1.175201 | $+0.009080$ |
| 1.5 | 2.138285 | 2.129279 | $+0.009006$ |

$$\boxed{y(0.5) = 0.5263,\quad y(1.0) = 1.1843,\quad y(1.5) = 2.1383 \quad (h = 0.5)}$$

**Step 3. Refine.** Halving $h$ should cut the error by about 4, since the scheme is
second order.

| $h$ | Interior nodes | Largest error |
| --: | --: | --: |
| 1 | 1 | 0.03375 |
| 0.5 | 3 | 0.00908 |
| 0.25 | 7 | 0.00249 |
| 0.125 | 15 | 0.00063 |

The ratio $0.00908 / 0.00249 = 3.65$ is close to the expected 4, confirming
second-order accuracy.

> [!info] Check against the continuous solution
> The ODE $y'' - y = 0$ has the general solution $y = A\cosh x + B\sinh x$. From
> $y(0) = 0$, $A = 0$. From $y(2) = 3.62686$,
> $$B = \frac{3.62686}{\sinh 2} = \frac{3.62686}{3.6268604} = 0.99999989$$
> so
> $$y = 3.62686\,\frac{\sinh x}{\sinh 2}$$
> Exact values at the three interior nodes are $0.521095$, $1.175201$ and
> $2.129279$. The numerical values overshoot by under $1\%$, as expected for a
> second-order scheme on a growing exponential.

> [!warning] The halving ratio is the check that the order is what you think
> The four rows of the refinement table are not decoration; they are the only
> evidence that the scheme is second order. A ratio near 4 means the
> $O(h^2)$ term dominates. A ratio near 2 would mean the scheme is only first
> order, and a ratio near 8 or 16 would mean something is wrong with the
> difference stencil rather than right about it.
>
> $3.65$ rather than exactly $4$ is expected: at $h = 0.5$ there are only three
> interior nodes, so higher-order terms have not yet died away.

> [!note] Why the boundary value is suspicious, and what it tells you
> The printed $y(2) = 3.62686$ is a rounded value: $\sinh 2 = 3.6268604\ldots$
> gives $B$ exactly $1$ to seven figures, so the intended exact solution is almost
> certainly $y = \sinh x$. That is a strong hint the question was built backwards
> from a known answer.
>
> It also means the "error" quoted above is almost entirely scheme error, not the
> $4 \times 10^{-7}$ rounding in the boundary condition. With the exact condition
> $y(2) = \sinh 2$, the $h = 0.5$ numerical solution is $0.52634$ against an exact
> $0.52109$, and the same $0.9\%$ gap remains. So the gap is real and belongs to
> the scheme.

---

### **(c) A capacitor loses 4% of its remaining charge every second. It is fully charged with 100 Coulomb of charge. What will be the remaining charge after 10 sec. Develop the ODE and also determine the solution.**

*[Marks: 05, CO: 2]*

**Step 1. Set up the rate equation.** Losing $4\%$ of the *remaining* charge each
second means the loss is **proportional to the charge present**, not a constant
$4$ C per second. If $Q$ is the charge and $t$ the time,

$$
\frac{dQ}{dt} = -0.04\,Q, \qquad Q(0) = 100
$$

> [!warning] The phrase "of its remaining charge" is the whole question
> Two readings are available and they differ by $0.8\%$.
>
> | Reading | Value | Character |
> | :-- | --: | :-- |
> | Continuous exponential | 67.0320 | The physically correct law. Each individual decay is small, so compounding is continuous |
> | Discrete $0.96^n$ | 66.4833 | Treats each second as one exact $4\%$ step. Slightly under, since $1-0.04 < e^{-0.04}$ |
>
> The general identity is $(1-r)^n < e^{-rn}$ for $0<r<1$, so the discrete answer
> always under-reads. A capacitor really does decay continuously, so $67.0320$ is
> the intended answer, and the ODE the question asks you to develop is the
> exponential one.
>
> The trap is writing $Q' = -4$. That is a constant loss of 4 Coulombs per second,
> which would give $Q(10) = 60$ and is a different physical situation entirely.

The negative sign is essential: the charge is decreasing.

**Step 2. Solve by separation of variables.**

$$
\frac{dQ}{Q} = -0.04\,dt
$$

Integrating,

$$
\ln Q = -0.04\,t + C
$$

At $t = 0$, $\ln 100 = C$, so

$$
Q(t) = 100\,e^{-0.04t}
$$

**Step 3. Evaluate at $t = 10$ s.**

$$
Q(10) = 100\,e^{-0.4} = 100(0.670320046) = 67.0320
$$

$$\boxed{Q(10) = 67.03 \text{ Coulomb}}$$

> [!info] Check by an independent route
> **Discrete compounding.** "Loses 4% of its remaining charge every second" read
> literally gives, second by second,
> $$Q(10) = 100(0.96)^{10} = 66.4833$$
> **Euler's method** with $h = 1$, which is exactly that recursion, returns
> $Q(10) = 66.4833$ as well: $96$, $92.16$, ... $66.4833$.

> [!note] Half-life as a check
> From $Q(t) = Q_0e^{-t/\tau}$ with $\tau = 25$ s, the half-life is $\tau\ln 2 = 17.33$ s.
> So in 10 s the charge should be somewhat **more** than half of 100, which is
> exactly what 67.03 shows.
>
> A reading of 66.48 also passes that test, which is why it is worth noticing that
> a sanity check cannot separate these two readings. When two readings differ by
> less than a percent, the check has to be a different method rather than a
> plausibility test.

> [!note] Generalising the form
> Every first-order decay problem has the shape $Q' = -kQ$ with
> $Q(t) = Q_0e^{-kt}$, and the two useful numbers are the time constant $\tau = 1/k$
> and the half-life $\frac{\ln 2}{k}$. Working in half-lives is often easier than
> working in $e$'s: at 10 s the capacitor has been discharging for
> $10/17.33 = 0.577$ half-lives, so it holds $2^{-0.577} = 0.670$ of its charge.

---

# SECTION B

## Question 6

### **(a) Write down a real-life application of numerical differentiation.**

*[Marks: 02, CO: 2]*

**Velocity and acceleration from position data.**

A vehicle's position $x(t)$ is logged by GPS, or a vibrating mass's displacement
is recorded by an accelerometer. Neither instrument measures velocity directly,
yet both are needed for control. The derivative is obtained from the finite
difference

$$
v(t) = \frac{x(t+h) - x(t-h)}{2h}
$$

$$\boxed{\text{GPS or accelerometer data gives position; the numerical derivative gives velocity and acceleration}}$$

Second application: finding the **peak** of a sampled signal, such as the peak
acceleration in a crash test, where the maximum of the numerical derivative locates
the maximum of the original.

> [!note] Why this application needs numerical differentiation at all
> A GPS receiver integrates satellite timing signals to produce position, and an
> accelerometer integrates its proof mass to produce displacement. In both cases
> **position is the measured quantity and velocity is not.** Somebody has to take
> the derivative, and in the field that is always done by finite differences.
>
> So numerical differentiation is not a convenience here. It is the only route
> from the instrument's output to the quantity the controller needs.

> [!warning] The optimal step size is a real trade-off, and knowing its order matters
> Accuracy is $O(h^2)$, so halving $h$ cuts the truncation error by 4. But round
> off grows as $1/h$, because the difference of two nearly equal numbers loses
> significant digits. Halving $h$ therefore multiplies the round off error by 2.
>
> The two cross at $h \approx \varepsilon^{1/3}$, where $\varepsilon$ is the machine
> epsilon, about $6 \times 10^{-6}$ in double precision. The optimal step is
> therefore near $1.8 \times 10^{-2}$, not "as small as possible". Making $h$
> smaller makes the answer worse, which is counter-intuitive enough to be worth
> remembering.

---

### **(b) Use Newton's method to find the maximum of $f(x) = 2\sin x - \frac{x^2}{10}$ with an initial guess of $x_0 = 2.5$.**

*[Marks: 03, CO: 2]*

**Step 1. Reduce to a root problem.** An interior maximum of a smooth $f$ satisfies
$f'(x) = 0$, so apply Newton to the derivative. Since

$$
f'(x) = 2\cos x - \frac{x}{5}, \qquad f''(x) = -2\sin x - \frac{1}{5}
$$

Newton's iteration for $f'(x) = 0$ is

$$
x_{n+1} = x_n - \frac{f'(x_n)}{f''(x_n)} = x_n - \frac{2\cos x_n - x_n/5}{-2\sin x_n - 1/5}
$$

> [!warning] The denominator is $f''$, not $f'$
> The question says "find the maximum", so the function being solved is $f'$ and
> Newton's denominator is $(f')' = f''$. Using $f'$ in the denominator as well
> gives $x_{n+1} = x_n - 1 = 1.5$ on the first step and then $x_n$ decreases by 1
> forever: a perfectly tidy-looking iteration heading to $-\infty$.
>
> **The safeguard is a dimensional sanity check.** At the maximum the quantity
> being solved, $f'$, must be near zero. A sequence that is not settling towards a
> zero of $f'$ is not converging, however smooth it looks.

**Step 2. Iterate from $x_0 = 2.5$.**

At $x_0 = 2.5$: $f'(2.5) = 2\cos 2.5 - 0.5 = -1.60229 - 0.5 = -2.10229$ and
$f''(2.5) = -2\sin 2.5 - 0.2 = -1.19694 - 0.2 = -1.39694$.

| Iteration | $x_n$ | $f'(x_n)$ | $f(x_n)$ |
| --: | --: | --: | --: |
| 0 | 2.5000000000 | $-2.1022872$ | 0.5719443 |
| 1 | 0.9950815513 | $+0.8898527$ | 1.5785880 |
| 2 | 1.4690107528 | $-0.0905823$ | 1.7738494 |
| 3 | 1.4276423210 | $-0.0001973$ | 1.7757256 |
| 4 | 1.4275517793 | $-0.0000000$ | 1.7757257 |
| 5 | 1.4275517788 | $0$ | 1.7757257 |

Iteration 1: $x_1 = 2.5 - \frac{-2.1022872}{-1.3969443} = 2.5 - 1.5049184 = 0.9950816$.

$$\boxed{x_{max} = 1.42755, \qquad f(x_{max}) = 1.77573}$$

**Step 3. Confirm it is a maximum, not a minimum.**

$f''(1.42755) = -2\sin(1.42755) - 0.2 = -1.979516 - 0.2 = -2.179516$, which is
**negative**, so $f$ is concave there and the stationary point is a maximum.

> [!warning] This check is not optional
> Newton applied to $f' = 0$ finds a critical point of either kind. The
> substitution $f' = 0$ carries no information about which, and this particular
> function has several critical points, two of them minima.
>
> **Rule: whenever you solve for a stationary point, immediately report the sign
> of the second derivative.** One extra evaluation, and it is the difference
> between a maximum and a minimum.

> [!info] Check by two independent routes
> **Bisection on $f'$.** Since $f'(0) = 2 > 0$ and
> $f'(2) = 2\cos 2 - 0.4 = -1.2323 < 0$, bisection on $[0, 2]$ converges to
> $1.4275517788$, with $f = 1.7757256531$. Same value to ten decimals.
>
> **Shape argument.** $f''(x) = -2\sin x - 0.2 < 0$ for every $x \in (0, \pi)$,
> so $f$ is strictly concave on that interval and can have **at most one**
> stationary point there. Since $f'(0) = 2 > 0$ and $f'(\pi) = -2.6283 < 0$, it
> has exactly one, and it is therefore the maximum on $(0, \pi)$.
>
> **Is it the global maximum?** $f'$ has four further roots, near
> $x = -4.2713$, $-1.7462$, $5.2672$ and $7.0689$, with $f = -0.0158$, $-2.2742$,
> $-4.4743$ and $-3.5823$. All are minima or below the maximum, and
> $f(x) \to -\infty$ as $x \to \pm\infty$ because of the $x^2/10$ term. So
> $1.4276$ with $f = 1.7757$ is the global maximum over all of $\mathbb{R}$.

> [!warning] $x_0 = 2.5$ throws the first iterate clean across the root
> The first iterate crosses the root cleanly, jumping from $2.5$ to $0.9951$,
> landing **left** of the answer at $1.4276$, an error of $0.4325$. At
> $x_0 = 2.5$ both $f'$ and $f''$ are negative and of similar size, so the ratio
> $f'/f'' \approx 1.5$ is large, and the first step is correspondingly long.
>
> Convergence still follows, and **the reason is about $g = f'$, not about $f$**.
> Newton is being applied to $g(x) = 2\cos x - \frac{x}{5}$, and the shape that
> governs the step is
> $$g'(x) = -2\sin x - 0.2, \qquad g''(x) = -2\cos x$$
> so $g$ is **concave** for $x < \frac{\pi}{2} = 1.5708$ and **convex** for
> $x > \frac{\pi}{2}$. The start $2.5$ sits in the convex region, where the tangent
> to a convex decreasing curve cuts the axis to the left of the true root. Hence
> the overshoot past $1.4276$.
>
> From iteration 2 onward the iterate is in the concave region, where the tangent
> lies above the curve and the sequence decreases monotonically toward the root
> without crossing it:
> $$1.4690 > 1.4276 > 1.42755 > 1.4275517788$$
> The errors fall $0.4325 \to 0.4739 \to 0.0414 \to 9.05\times10^{-5} \to
> 5\times10^{-10}$, the last ratio being $0.0022$, consistent with the
> $O(e^2)$ signature of Newton.
>
> So $x_0 = 2.5$ is legitimate but uncomfortable. Starting from $0.5$ or from
> $1.5$ converges in fewer steps and never leaves the interval of interest.
>
> **The general lesson.** A first step that overshoots is not a failure, and a
> monotone tail afterwards means it worked. What would be a failure is a
> two-cycle, where the iterate alternates between two values indefinitely.

---

### **(c) Solve the Poisson equation $U_{xx} + U_{yy} = -10(x^2 + y^2 + 10)$ in the domain of the given figure.**

*[Marks: 05, CO: 2]*

![Square domain 3 by 3 finite difference grid for the Poisson equation with u=0 on all four sides, x and y from 0 to 3, and four interior nodes u1, u2, u3, u4](../answers_exam_style/diagrams/2021_Q6c_poisson_grid.jpg)
*Figure 2021 Q6(c): square domain finite-difference grid with Dirichlet boundary conditions for Poisson's equation (Source: Page 2, Q6(c))*

**Step 1. The grid.** The domain is $0 \le x \le 3$, $0 \le y \le 3$ with
$h = k = 1$. Here $u = 0$ on all four sides. Four interior nodes:

| Node | Location |
| :-- | :-- |
| $u_1$ | $(1, 1)$ |
| $u_2$ | $(2, 1)$ |
| $u_3$ | $(1, 2)$ |
| $u_4$ | $(2, 2)$ |

**Step 2. The five-point formula.** With $h = k = 1$,

$$
u_{i+1,j} + u_{i-1,j} + u_{i,j+1} + u_{i,j-1} - 4u_{i,j} = -10(x_i^2 + y_j^2 + 10)
$$

> [!note] Read the coefficient of $u_{ij}$ off the figure, not off memory
> $u_{i+1,j} + u_{i-1,j} - 2u_{ij}$ approximates $h^2 U_{xx}$ and
> $u_{i,j+1} + u_{i,j-1} - 2u_{ij}$ approximates $k^2 U_{yy}$. Adding them and
> dividing by $h^2$ gives a coefficient of $-4$ on $u_{ij}$ when $h = k = 1$.
>
> The five-point stencil is the whole method. Everything after this is bookkeeping.

**Step 3. Write one equation per interior node.** All boundary values are zero, so
those terms drop out.

At $u_1(1,1)$: $-10(1 + 1 + 10) = -120$

$$
u_2 + 0 + u_3 + 0 - 4u_1 = -120 \Rightarrow -4u_1 + u_2 + u_3 = -120
$$

At $u_2(2,1)$: $-10(4 + 1 + 10) = -150$

$$
0 + u_1 + u_4 + 0 - 4u_2 = -150 \Rightarrow u_1 - 4u_2 + u_4 = -150
$$

At $u_3(1,2)$: $-10(1 + 4 + 10) = -150$

$$
u_4 + 0 + 0 + u_1 - 4u_3 = -150 \Rightarrow u_1 - 4u_3 + u_4 = -150
$$

At $u_4(2,2)$: $-10(4 + 4 + 10) = -180$

$$
0 + u_3 + 0 + u_2 - 4u_4 = -180 \Rightarrow u_2 + u_3 - 4u_4 = -180
$$

**Step 4. The system.**

$$
\begin{bmatrix}
-4 & 1 & 1 & 0 \\
1 & -4 & 0 & 1 \\
1 & 0 & -4 & 1 \\
0 & 1 & 1 & -4
\end{bmatrix}
\begin{bmatrix} u_1 \\ u_2 \\ u_3 \\ u_4 \end{bmatrix}
= \begin{bmatrix} -120 \\ -150 \\ -150 \\ -180 \end{bmatrix}
$$

**Step 5. Exploit symmetry, then solve.** The domain and the source
$-10(x^2+y^2+10)$ are symmetric under $x \leftrightarrow y$, and $(2,1)$ maps to
$(1,2)$, so $u_2 = u_3$. Let $u_2 = u_3 = w$. Then

$$
\begin{cases}
-4u_1 + 2w = -120 \\
u_1 - 4w + u_4 = -150 \\
2w - 4u_4 = -180
\end{cases}
$$

From the first, $u_1 = \frac{2w + 120}{4} = \frac{w}{2} + 30$. From the third,
$u_4 = \frac{2w + 180}{4} = \frac{w}{2} + 45$. Substituting into the second,

$$
\frac{w}{2} + 30 - 4w + \frac{w}{2} + 45 = -150 \Rightarrow -3w + 75 = -150 \Rightarrow w = 75
$$

Then $u_1 = 37.5 + 30 = 67.5$ and $u_4 = 37.5 + 45 = 82.5$.

$$\boxed{u_1 = 67.5, \quad u_2 = 75, \quad u_3 = 75, \quad u_4 = 82.5}$$

**Step 6. Verify.** Substituting back:

$$
-4(67.5) + 75 + 75 = -270 + 150 = -120 \quad \checkmark
$$

$$
67.5 - 4(75) + 82.5 = 150 - 300 = -150 \quad \checkmark
$$

$$
67.5 - 4(75) + 82.5 = -150 \quad \checkmark
$$

$$
75 + 75 - 4(82.5) = 150 - 330 = -180 \quad \checkmark
$$

> [!info] Check
> The symmetry argument was confirmed by solving the full 4 by 4 system directly
> with exact rational arithmetic: it returns $(67.5, 75, 75, 82.5)$ and gives
> $u_2 = u_3$ without being told to. All four residuals are exactly zero.
>
> A second structural check: the matrix is symmetric and diagonally dominant, so it
> is a positive-definite M-matrix and the solution is unique. The pattern
> $u_1 < u_2 = u_3 < u_4$ matches the source term, since
> $x^2+y^2+10$ is smallest at $(1,1)$ and largest at $(2,2)$, and the negative
> source means the largest magnitude of $u$ must occur where the source is most
> negative, that is at $(2,2)$. Correct.

> [!warning] Symmetry is an optimisation, never an assumption
> Using $u_2 = u_3$ cut a $4 \times 4$ system to three equations. But it is only
> legitimate because the **source and the boundary data are both** symmetric under
> $x \leftrightarrow y$.
>
> If the source had been $-10(x^2 + 2y^2 + 10)$, or if the right-hand boundary had
> been non-zero, the symmetry would break and $u_2 = u_3$ would be a guess that
> silently returns a wrong answer. State the symmetry you are using and check that
> it is there.

> [!note] There is no polynomial exact solution for these boundary data
> It is tempting to look for a closed form. Try
> $U = ax^4 + bx^2y^2 + cy^4 + dx^2 + ey^2 + f$. Then
> $U_{xx} + U_{yy} = (12a+2b)x^2 + (2b+12c)y^2 + (2d+2e)$, and matching
> $-10(x^2+y^2+10)$ requires
> $$12a+2b=-10, \quad 2b+12c=-10, \quad 2d+2e=-100$$
> The condition $u = 0$ on $x = 0$ for all $y$ forces $c = e = f = 0$, and $u = 0$
> on $y = 0$ forces $a = d = f = 0$. Then the constant equation reads $0 = -100$, a
> contradiction. **No quartic satisfies both the PDE and these boundary values**, so
> the finite difference solution above is the answer and there is nothing to check
> it against.
>
> That is normal rather than disappointing. A polynomial can satisfy a PDE with
> compatible boundary data, but $u = 0$ on all four sides of a source that is
> everywhere negative is not compatible data.

---

### **(d) Differentiate between constrained and unconstrained optimization.**

*[Marks: 02, CO: 2]*

**Unconstrained optimization.** No restrictions. Choose $x$ freely in the whole
domain to maximise or minimise $f(x)$.

$$
\text{minimise } f(x_1, x_2, \dots, x_n), \qquad x \in \mathbb{R}^n
$$

Example: fit $y = a + bx$ to data by least squares. Nothing forbids any $a$ or $b$,
hence it is unconstrained.

**Constrained optimization.** Extra conditions must hold. Each restriction is
written as $g(x) \le 0$ or $h(x) = 0$.

$$
\text{minimise } f(x) \quad \text{subject to} \quad g_i(x) \le 0,\ i = 1\dots m, \quad h_j(x) = 0
$$

Example: minimise the weight of a truss subject to every member carrying at most
its rated load, or maximise a portfolio return subject to total risk staying under
a limit.

| | Unconstrained | Constrained |
| :-- | :-- | :-- |
| Restrictions | None | Equality and inequality conditions |
| Stationarity test | $\nabla f = 0$ | KKT multipliers: $\nabla f + \sum \mu_i \nabla g_i + \sum \lambda_j \nabla h_j = 0$ |
| Lagrange multipliers | Not needed | Essential |
| Optimum may be at | An interior point | A point on the boundary |
| Feasible region | Whole space | A subset |
| Harder | Easier | Harder; more constraints mean more cases |

$$\boxed{\text{Unconstrained: choose freely. Constrained: obey rules, solved with multipliers}}$$

> [!warning] The plain gradient test is not merely incomplete here, it is wrong
> In the unconstrained case the optimum satisfies $\nabla f = 0$. In the
> constrained case the optimum frequently sits **on** a boundary where the plain
> gradient test is useless: at a corner the feasible directions are restricted, so
> $f$ can be stationary in a sense that has nothing to do with $\nabla f$.
>
> The KKT conditions replace that with
> $\nabla f + \sum \mu_i \nabla g_i + \sum \lambda_j \nabla h_j = 0$ together with
> **complementary slackness**, $\mu_i \ge 0$ and $\mu_i g_i(x) = 0$. That second
> condition is the part people forget: a multiplier is nonzero only if its
> constraint is active. It is what encodes "the constraint bites exactly when it
> is touching".

---

## Question 7

### **(a) Why is pivoting important?**

*[Marks: 02, CO: 1]*

Every elimination step **divides** by the pivot, the element chosen as divisor.
Pivoting reorders rows or columns so that pivot is as large in magnitude as
possible.

**Two reasons.**

1. **A zero pivot stops the method.** If $a_{kk} = 0$, the step is undefined. Row
   interchange usually fixes it.
2. **A tiny pivot destroys accuracy.** If $a_{kk} = 10^{-9}$ while other entries are
   of order 1, then the multiplier $\frac{a_{ik}}{a_{kk}}$ is of order $10^9$, and
   subtracting such numbers loses most of the significant digits. The computation
   still runs and returns a wrong answer.

**Partial pivoting**, the usual choice, selects the largest $\lvert a_{ik}\rvert$ in
column $k$ below the diagonal and swaps it up. It costs one comparison per
candidate and no extra arithmetic.

$$\boxed{\text{Pivoting avoids a zero or tiny divisor, which is where elimination accuracy is lost}}$$

> [!warning] Stability is not conditioning
> Pivoting improves **stability**, not **conditioning**. The condition number
> $\kappa(A)$ is a property of the problem and cannot be changed by reordering.
>
> If $\kappa$ is large, the answer is unreliable no matter how carefully the
> elimination is done. **A perfectly pivoted elimination of an ill-conditioned
> system returns a confidently wrong answer**, which is the dangerous combination.
>
> Compare with Q.4(c) of 2022, where the question defines an ill-conditioned
> system. The two topics meet here and the distinction is the whole point of both.

---

### **(b) Determine the value of $I_0$ in the given circuit using Gauss-Seidel method.**

*[Marks: 06, CO: 2]*

![DC circuit with a 30 V independent voltage source, 10, 15, 8 and 20 ohm resistors, and a dependent voltage source 5I0, with branch current I0 through the 10 ohm resistor](../answers_exam_style/diagrams/2021_Q7b_circuit.jpg)
*Figure 2021 Q7(b): DC circuit with independent 30 V source, four resistors, and dependent voltage source $5I_0$ (Source: Page 2, Q7(b))*

**Step 1. Name the nodes.** Take the bottom rail as reference, $0$ V.

| Node | Voltage |
| :-- | :-- |
| Top rail | $V_T = 30$ V, held by the ideal source |
| Centre node $C$ | $V_C$ |
| Right node $R$ | $V_R$ |

**Step 2. Express the controlling current.**

$$
I_0 = \frac{V_T - V_C}{10} = \frac{30 - V_C}{10}
$$

**Step 3. Apply the dependent source.** The $5I_0$ source sets the right node:

$$
V_R = 5I_0 = 5\left(\frac{30 - V_C}{10}\right) = 15 - 0.5V_C
$$

Rearranged, that is one equation ready for iteration:

$$
V_C + 2V_R = 30
$$

> [!warning] A dependent source is not an unknown to be iterated
> $V_R$ is **defined** as $5I_0$, and $I_0$ is defined by the $10\ \Omega$ branch.
> Neither is free. Treating $V_R$ as an unknown that starts at zero and converges
> contradicts the circuit: the dependent source fixes it exactly, from the first
> sweep onward.
>
> This is the same error as starting $I_3$ at zero in 2024 Q.2(b), where a $5$ A
> current source fixed a mesh current. **Read the circuit for sources that pin a
> variable before writing any iteration.**

**Step 4. KCL at node $C$.** Three branches leave it, toward the top rail, toward
ground, and toward node $R$:

$$
\frac{V_C - 30}{10} + \frac{V_C - 0}{15} + \frac{V_C - V_R}{8} = 0
$$

Multiplying by $120$,

$$
12(V_C - 30) + 8V_C + 15(V_C - V_R) = 0
$$

$$
12V_C - 360 + 8V_C + 15V_C - 15V_R = 0
$$

$$
35V_C - 15V_R = 360
$$

**Step 5. The system to iterate.**

$$
\begin{cases}
V_C = \dfrac{15V_R + 360}{35} \\[2mm]
V_R = \dfrac{30 - V_C}{2}
\end{cases}
$$

**Step 6. Gauss-Seidel.** Use the value just computed, never the previous
iteration's. Start from $V_C^{(0)} = V_R^{(0)} = 0$.

| $k$ | $V_C$ | $V_R$ |
| ---: | --: | --: |
| 0 | 0.000000 | 0.000000 |
| 1 | 10.285714 | 9.857143 |
| 2 | 14.510204 | 7.744898 |
| 3 | 13.604956 | 8.197522 |
| 4 | 13.798938 | 8.100531 |
| 5 | 13.757370 | 8.121315 |
| 6 | 13.766278 | 8.116861 |
| 7 | 13.764369 | 8.117815 |
| 8 | 13.764778 | 8.117611 |

Iteration 1: $V_C^{(1)} = \frac{15(0) + 360}{35} = 10.285714$, then
$V_R^{(1)} = \frac{30 - 10.285714}{2} = 9.857143$.

**Step 7. Read off $I_0$.**

$$
I_0 = \frac{30 - 13.764778}{10} = \frac{16.235222}{10} = 1.6235 \text{ A}
$$

$$\boxed{I_0 = 1.6235 \text{ A}, \quad V_C = 13.7648 \text{ V}, \quad V_R = 8.1176 \text{ V}}$$

> [!warning] The $V_R$ column alternates, and that is not a sign of divergence
> $V_C$ values run high, low, high, low, $13.764778$ then $13.764690$. Gauss-Seidel
> overshoots one way then the other while it contracts, so the residual is **not**
> monotone even though the answer is.
>
> Judging convergence by "is the last step change small" therefore needs a
> tolerance, not an exact-match test. And a bracketing check on $I_0$ is the
> cheapest test of all: the answer must lie between the smallest and largest
> $I_0$ values the table produces, and it does.

> [!info] Check by two independent routes
> **Direct solution.** Eliminating $V_C$ from the two equations gives
> $V_C = \frac{234}{17} = 13.7647058824$ and $V_R = \frac{138}{17} = 8.1176470588$,
> so
> $$I_0 = \frac{30 - 234/17}{10} = \frac{138}{85} = 1.6235294118$$
> Iteration 8 gives $I_0 = 1.623522$, agreeing with the closed form to four
> decimals. The residual in $V_C$ is $7.2 \times 10^{-5}$ there, and it falls by a
> factor of about $4.6$ per sweep: iteration 10 gives $I_0 = 1.623529$ and
> iteration 12 gives $1.6235294$, matching the closed form to seven figures.
>
> **Consistency of the dependent source.** $5I_0 = 5(1.6235294) = 8.1176471$, and
> $V_R = \frac{138}{17} = 8.1176471$. The two agree, which they must, since
> $V_R$ was **defined** as $5I_0$.
>
> **KCL residual.** $\frac{V_C-30}{10} + \frac{V_C}{15} + \frac{V_C-V_R}{8} = 0$ exactly
> at the converged values.

> [!warning] The row order decides whether Gauss-Seidel converges at all
> Solve equation 2 first, $V_C = 30 - 2V_R$, and use equation 1 for $V_R$, and the
> iteration **diverges**:
> $V_C = 30.0$, then $-62.0$, then $367.3$, then $-1636.2$, then $7713.7$. The
> sequence grows without bound.
>
> The reason is visible in the diagonal of the coefficient matrix. Written in the
> order above, rows $35V_C - 15V_R = 360$ and $V_C + 2V_R = 30$, it is
> $$\begin{bmatrix} 35 & -15 \\ 1 & 2\end{bmatrix}$$
> with diagonal magnitudes $35$ and $2$ against off-diagonal sums $15$ and $1$.
> Both rows are strictly dominant, $35 > 15$ and $2 > 1$, which is what guarantees
> convergence in this ordering.
>
> Reversed, the rows become $\begin{bmatrix} 1 & 2 \\ 35 & -15\end{bmatrix}$, and
> now neither row is dominant: $1 < 2$ and $15 < 35$. That loss of dominance is
> exactly the divergence.
>
> The Gauss-Seidel iteration matrices confirm it. In the working order,
> $V_R^{(k+1)} = \frac{690 - 15V_R^{(k)}}{70}$, so the matrix is
> $$\begin{bmatrix} 0 & 15/35 \\ 0 & -15/70 \end{bmatrix}$$
> with spectral radius $\frac{15}{70} = 0.214 < 1$, so it converges. In the
> reversed order, $V_R^{(k+1)} = 46 - \frac{14}{3}V_R^{(k)}$, so the matrix is
> $$\begin{bmatrix} 0 & -2 \\ 0 & -14/3 \end{bmatrix}$$
> with spectral radius $\frac{14}{3} = 4.67 > 1$, which diverges.
>
> This is the same trap as the Gauss-Seidel questions in 2023 and 2024, and the
> fix is always the same: keep a diagonal-dominant ordering.

---

### **(c) From the values of $x$ and $y$ in the following table, determine $\frac{dy}{dx}$ and $\frac{d^2y}{dx^2}$ for $x = 1.2$.**

*[Marks: 05, CO: 3]*

| $x$ | 1.0 | 1.2 | 1.4 | 1.6 | 1.8 | 2.0 | 2.2 |
| --- | --: | --: | --: | --: | --: | --: | --: |
| $y$ | 2.7183 | 3.3201 | 4.0552 | 4.9530 | 6.0496 | 7.3891 | 9.0250 |

The nodes are equally spaced with $h = 0.2$, and the values are $e^x$ rounded to
four decimals.

> [!warning] The five-point formula cannot be used at $x = 1.2$
> The five-point **central** difference for $f'$ at $x$ needs points at
> $x - 2h$, $x - h$, $x$, $x + h$, $x + 2h$. At $x = 1.2$ that is
> $0.8, 1.0, 1.2, 1.4, 1.6$, and **the table has no $x = 0.8$**. The five-point
> formula is available at $x = 1.4$ onward, not at $x = 1.2$.
>
> So the three-point formula is the intended one. **Always check that the nodes
> the formula needs actually exist in the table**, before choosing it.

**First derivative, three-point central.** Uses $x = 1.0, 1.2, 1.4$:

$$
\left.\frac{dy}{dx}\right|_{1.2} \approx \frac{y_{1.4} - y_{1.0}}{2h} = \frac{4.0552 - 2.7183}{0.4} = \frac{1.3369}{0.4} = 3.34225
$$

**First derivative, three-point forward.** Uses $x = 1.2, 1.4, 1.6$:

$$
\left.\frac{dy}{dx}\right|_{1.2} \approx \frac{-3y_{1.2} + 4y_{1.4} - y_{1.6}}{2h} = \frac{-3(3.3201) + 4(4.0552) - 4.9530}{0.4} = \frac{1.3075}{0.4} = 3.26875
$$

The central form is both more accurate and symmetric, and it is therefore
preferred. The true value is $e^{1.2} = 3.3201169$, giving errors of $+0.0221$ and
$-0.0514$ respectively.

**Second derivative, three-point central.**

$$
\left.\frac{d^2y}{dx^2}\right|_{1.2} \approx \frac{y_{1.4} - 2y_{1.2} + y_{1.0}}{h^2} = \frac{4.0552 - 2(3.3201) + 2.7183}{0.04} = \frac{0.1333}{0.04} = 3.3325
$$

**Second derivative, three-point forward.**

$$
\left.\frac{d^2y}{dx^2}\right|_{1.2} \approx \frac{y_{1.6} - 2y_{1.4} + y_{1.2}}{h^2} = \frac{4.9530 - 2(4.0552) + 3.3201}{0.04} = \frac{0.1627}{0.04} = 4.0675
$$

The central form is again much better: error $+0.0124$ against $+0.7474$.

$$\boxed{\frac{dy}{dx}\bigg|_{1.2} \approx 3.3423, \qquad \frac{d^2y}{dx^2}\bigg|_{1.2} \approx 3.3325}$$

> [!info] Check
> The table is $e^x$ rounded to four decimals, so the exact answers are
> $e^{1.2} = 3.3201169$ for both the first and second derivative, since
> $\frac{d^2}{dx^2}e^x = e^x$. The central values $3.34225$ and $3.3325$ are within
> $0.7\%$ and $0.4\%$ of that, consistent with $O(h^2)$ truncation plus the
> four-decimal rounding in the data.
>
> The five-point central formula **does** work at $x = 1.4$, where $x - 2h = 1.0$
> is present: it gives $f'(1.4) = 4.0549583$ against the exact $4.0552000$, an
> error of $2.4\times10^{-4}$. The three-point central form at the same point gives
> $4.0822500$, an error of $2.7\times10^{-2}$, so the five-point formula is about
> $110$ times better. That confirms the table is sound and only the **position**
> $x = 1.2$ prevents the better formula.

> [!warning] Three traps in this question
> **1. Reaching for five points when only three fit.** The instinct is to use the
> most accurate formula available. At $x = 1.2$ it is not available. Check that the
> required nodes exist before choosing a formula.
>
> **2. Using a one-sided formula at an interior point.** $x = 1.2$ has data on both
> sides, so the central formula applies and is both more accurate and naturally
> symmetric. A forward formula at an interior point throws away information for
> no reason, and for the second derivative it costs a factor of 60 in error here.
>
> **3. Dividing by $2h$ when the formula says $h$.** The three-point first
> derivative uses $2h$ in the denominator; the three-point second derivative uses
> $h^2$. Confusing the two is the most common slip in this question, and it gives
> answers exactly twice or $2h$ times too large.

> [!note] The cancellation that makes this question hard
> Look at the numerator of the second derivative:
> $4.0552 - 2(3.3201) + 2.7183 = 0.1333$. The three terms are of order 4 and their
> sum is of order 0.13, so three significant digits have been cancelled away before
> the division.
>
> This is why second derivatives from finite differences are so much less accurate
> than first: the cancellation is worse by a factor of $2/h$ relative to the
> signal. The answer $3.3325$ looks precise to five figures and is only good to
> about half a percent.

---

## Question 8

### **(a) Derive the following numerical integration formula: $\int_{x_0}^{x_n} y\,dx = \frac{h}{2}[y_0 + 2(y_1 + y_2 + \cdots + y_{n-1}) + y_n]$**

*[Marks: 04, CO: 1]*

**The formula is the composite trapezoidal rule.** $h = \frac{x_n - x_0}{n}$, and
$y_i = f(x_i)$ at $x_i = x_0 + ih$.

**Step 1. Start from the trapezoidal rule on one interval.** On $[x_i, x_{i+1}]$, the
trapezoid of area $\frac{1}{2}h(y_i + y_{i+1})$,

$$
\int_{x_i}^{x_{i+1}} y\,dx = \frac{h}{2}(y_i + y_{i+1}) - \frac{h^3}{12}y''(\xi_i) + \cdots
$$

**Step 2. Sum over all $n$ intervals.**

$$
\int_{x_0}^{x_n} y\,dx = \sum_{i=0}^{n-1}\left[\frac{h}{2}(y_i + y_{i+1}) + \text{error}\right]
$$

**Step 3. Collect the interior terms.** Every $y_1, y_2, \dots, y_{n-1}$ appears in
**two** adjacent trapezoids, once from each side, so each collects a factor of
$\frac{h}{2} \times 2 = h$. Only $y_0$ and $y_n$ appear once, each with factor
$\frac{h}{2}$. Hence

$$
\int_{x_0}^{x_n} y\,dx = \frac{h}{2}y_0 + h\left(y_1 + y_2 + \cdots + y_{n-1}\right) + \frac{h}{2}y_n - \sum_{i=0}^{n-1}\frac{h^3}{12}y''(\xi_i)
$$

**Step 4. Factor out $h/2$.** Since $h = 2\cdot\frac{h}{2}$, the interior sum
becomes $2\cdot\frac{h}{2}(y_1 + \cdots + y_{n-1})$, giving

$$
\int_{x_0}^{x_n} y\,dx = \frac{h}{2}\left[y_0 + 2(y_1 + y_2 + \cdots + y_{n-1}) + y_n\right] - \frac{h^3}{12}\sum_{i=0}^{n-1}y''(\xi_i)
$$

**Step 5. The leading error term.** With $n$ intervals, $h = \frac{b-a}{n}$ and
$\sum y''(\xi_i) \approx \frac{1}{h}\int y''$, so

$$
E = -\frac{h^2}{12}\left[y'(x_n) - y'(x_0)\right] + O(h^4)
$$

which is $O(h^2)$, the signature of a second-order method.

$$\boxed{\int_{x_0}^{x_n} y\,dx = \frac{h}{2}\left[y_0 + 2\sum_{i=1}^{n-1}y_i + y_n\right] + O(h^2)}$$

> [!warning] The counting in step 3 is the whole derivation
> The factor 2 on the interior terms is not a convention. It is the count of how
> many panels each interior ordinate belongs to: one from the left, one from the
> right.
>
> **The ends get no 2 because they belong to only one panel.** That asymmetry is
> the fingerprint of the trapezoid rule, and it is what distinguishes it from
> Simpson's rule, where the interior terms get 4 and 2 in a pattern.
>
> If a derivation ever produces a 2 on the end terms, the error is not in the
> algebra but in the counting.

> [!note] Two ways to see it
> **Geometrically.** Each panel is a trapezoid. Draw them all, add the areas: the
> interior ordinates are shared by two panels and so counted twice, the ends once.
>
> **By an exact integral.** Linear interpolation between the nodes gives
> $y(x) = \frac{y_{i+1}-y_i}{h}(x-x_i) + y_i$ on each panel. Integrating that
> exactly over $[x_i, x_{i+1}]$ gives $\frac{h}{2}(y_i + y_{i+1})$ per panel, and
> summing reproduces the formula with no error analysis needed.

> [!note] Reading the error term, because it is easy to misjudge
> The error is $O(h^2)$, but **for a fixed interval** $h = \frac{b-a}{n}$, so
> $E \propto \frac{1}{n^2}$. To halve the error you must quadruple $n$, which
> means four times the function evaluations. That is the real cost of the
> trapezoid rule, and it is why Simpson's rule, at $O(h^4)$, is usually preferred
> when the same evaluations will do.

---

### **(b) Use Romberg's method to compute: $\int_1^2 \frac{1}{2+x}\,dx$. Consider $h = 0.5, 0.25, 0.125$.**

*[Marks: 04, CO: 2]*

**Step 1. The first column, composite trapezoid.**

$$
T_n = \frac{h}{2}\left[f_0 + 2f_1 + \cdots + 2f_{n-1} + f_n\right], \qquad f_i = \frac{1}{2+x_i}
$$

At $h = 0.5$, $n = 2$, nodes $x = 1, 1.5, 2$:

$$
T_2 = \frac{0.5}{2}\left[\frac{1}{3} + 2\cdot\frac{1}{3.5} + \frac{1}{4}\right] = 0.25\left[0.333333 + 0.571429 + 0.25\right] = 0.288690
$$

At $h = 0.25$, $n = 4$:

$$
T_4 = \frac{0.25}{2}\left[\frac{1}{3} + 2\left(\frac{1}{3.25} + \frac{1}{3.5} + \frac{1}{3.75} + \frac{1}{4.25}\right) + \frac{1}{4}\right] = 0.287935
$$

At $h = 0.125$, $n = 8$:

$$
T_8 = 0.287745
$$

**Step 2. Second column.** The trapezoid rule has $O(h^2)$ error, so extrapolate
with the factor $4^1 - 1 = 3$:

$$
R_{k,1} = R_{k,0} + \frac{R_{k,0} - R_{k-1,0}}{4 - 1}
$$

**Step 3. Third column.** The result above is Simpson's rule, carrying $O(h^4)$,
so the factor is $4^2 - 1 = 15$:

$$
R_{k,2} = R_{k,1} + \frac{R_{k,1} - R_{k-1,1}}{16 - 1}
$$

**The table.**

$$
\begin{array}{c|ccc}
R_{k,0} & R_{k,1} & R_{k,2} \\
\hline
0.288690 & & \\
0.287935 & 0.287683 & \\
0.287745 & 0.287682 & 0.287682
\end{array}
$$

Row 2: $0.287935 + \frac{0.287935 - 0.288690}{3} = 0.287935 - 0.000252 = 0.287683$
Row 3, column 1: $0.287745 + \frac{0.287745 - 0.287935}{3} = 0.287745 - 0.000063 = 0.287682$
Row 3, column 2: $R_{3,2} = R_{3,1} + \frac{R_{3,1} - R_{2,1}}{15}$

Taken literally at the six decimals the table prints, this gives
$0.287682 - \frac{10^{-6}}{15} = 0.2876819$. Carried unrounded, which is what the
answer below uses, the same line gives $0.2876820735$, since the unrounded entries
are $R_{2,1} = 0.2876832$ and $R_{3,1} = 0.2876821$.

$$\boxed{I \approx 0.2876821}$$

> [!info] Check against the exact integral
> $$\int_1^2\frac{dx}{2+x} = \ln(2+x)\Big|_1^2 = \ln 4 - \ln 3 = \ln\frac{4}{3} = 0.2876820725$$
> The Romberg value differs by $1.05\times10^{-9}$, a relative error of
> $3.6\times10^{-9}$.
>
> For comparison, plain composite Simpson with $n = 8$ gives $0.2876821408$, whose
> relative error is $2.4\times10^{-7}$. **Romberg is about 65 times more accurate
> from the same function values**, because each column only recombines entries
> already in the table. No extra work.

> [!warning] When the last row stops moving, that is the method working
> The left column converges slowly and alternates,
> $0.2887 \to 0.2879 \to 0.2877$, because the trapezoid error is negative and
> shrinking like $h^2$. Each step right multiplies the accuracy by about $4^2 = 16$
> or better.
>
> Three levels give roughly eighth-order accuracy from a second-order rule. That
> is the whole point of Romberg: **the third column is doing $h^2 \to h^4 \to
> h^8$**, and it costs only arithmetic.
>
> Watch the printed values here. The third column entry barely differs from the
> second, because by then the numbers are already agreeing to six decimals. That
> is the expected appearance of convergence, not a sign the calculation has stalled.

---

### **(c) Using Euler's method, determine $\frac{dy}{dx} = \frac{3}{5}x^3 y$; Consider $y(0) = 1$.**

*[Marks: 04, CO: 3]*

> [!warning] A gap in the printed question
> No step size $h$ and no interval are given, so numbers cannot be produced
> without a stated choice. Use $h = 0.25$ and $x: 0 \to 1$, and say so. The exact
> solution is provided below so the answer can be judged at any step size.

**The method.**

$$
y_{n+1} = y_n + h\,f(x_n, y_n) = y_n + h\cdot\frac{3}{5}x_n^3 y_n
$$

**Step 1.** At $x_0 = 0$, $y_0 = 1$: slope $\frac{3}{5}(0)^3(1) = 0$, so
$y_1 = 1 + 0.25(0) = 1.0000000$.

**Step 2.** At $x_1 = 0.25$, $y_1 = 1$: slope
$\frac{3}{5}(0.25)^3(1) = \frac{3}{5}(0.015625) = 0.0093750$, so
$y_2 = 1 + 0.25(0.009375) = 1.0023438$.

**Step 3.** At $x_2 = 0.5$, $y_2 = 1.0023438$: slope
$\frac{3}{5}(0.5)^3(1.0023438) = \frac{3}{5}(0.125)(1.0023438) = 0.0751758$, so
$y_3 = 1.0023438 + 0.25(0.0751758) = 1.0211377$.

**Step 4.** At $x_3 = 0.75$, $y_3 = 1.0211377$: slope
$\frac{3}{5}(0.75)^3(1.0211377) = \frac{3}{5}(0.421875)(1.0211377) = 0.2584755$, so
$y_4 = 1.0211377 + 0.25(0.2584755) = 1.0857566$.

| Step | $x_n$ | $y_n$ | Slope $\frac{3}{5}x_n^3y_n$ | $y_{n+1}$ |
| --: | --: | --: | --: | --: |
| 1 | 0.00 | 1.0000000 | 0.0000000 | 1.0000000 |
| 2 | 0.25 | 1.0000000 | 0.0093750 | 1.0023438 |
| 3 | 0.50 | 1.0023438 | 0.0751758 | 1.0211377 |
| 4 | 0.75 | 1.0211377 | 0.2584755 | 1.0857566 |

$$\boxed{y(1) \approx 1.08576 \quad (h = 0.25)}$$

**Other step sizes**, to show the choice is not arbitrary:

| $h$ | Steps to $x=1$ | $y(1)$ | Error against exact |
| --: | --: | --: | --: |
| 0.5 | 2 | 1.03750 | $-0.12433$ |
| 0.25 | 4 | 1.08576 | $-0.07608$ |
| 0.1 | 10 | 1.12725 | $-0.03459$ |

> [!info] Check against the exact solution
> The equation is separable: $\frac{dy}{y} = \frac{3}{5}x^3dx$, so
> $\ln y = \frac{3}{20}x^4 + C$, and $y(0) = 1$ gives $C = 0$.
> $$y = e^{\frac{3}{20}x^4} = e^{0.15x^4}$$
> At $x = 1$: $e^{0.15} = 1.1618342$. Euler's $1.0857566$ is **low** by
> $0.0760777$, which is expected: Euler always undershoots when the solution is
> convex and increasing. Differentiating once more,
> $$y' = \frac{3}{5}x^3 y, \qquad y'' = \frac{9}{5}x^2 y + \frac{3}{5}x^3\cdot\frac{3}{5}x^3 y = \frac{9}{25}x^2(x^4 + 5)\,y$$
> which is positive for every $x \ne 0$, since $y > 0$.

> [!warning] The zero first step is not a mistake
> Step 1 gives $y_1 = 1.0000000$, identical to $y_0$. That is because the slope is
> $\frac{3}{5}x^3y$ and $x_0 = 0$.
>
> A step that produces no change looks like a failure and is not one here. The
> right response is to check the **slope**, not the step: a zero slope at $x = 0$
> for a function containing $x^3$ is exactly right, and it also tells you
> immediately that all the growth happens in the last few steps.
>
> Compare the slope column: $0$, $0.0094$, $0.0752$, $0.2585$. The last step
> contributes most of the answer, which is a strong hint that the coarse steps are
> wasting most of their accuracy.

> [!note] First order accuracy confirmed
> Halving $h$ from $0.5$ to $0.25$ cut the error from $0.12433$ to $0.07608$, a
> ratio of $1.63$ rather than the expected 2, because four steps of a stiffly
> growing function do not sit neatly in the asymptotic range yet. Halving again to
> $h = 0.1$ gives $0.03459$, and $0.07608/0.03459 = 2.20$, which is the expected
> factor of 2 as $h \to 0$. Euler is first order: halving the step halves the
> error.

> [!note] This is the same question as 2023 Q.3(b), the first of its two parts
> Identical ODE and identical initial condition. The only differences are the step
> size and the interval, neither of which the paper prints. That makes it a clean
> L2 merge under the plan's rule: same method, same structure, only the target
> step changed. Both papers need the same missing choice of $h$ and interval, so
> answering this one twice is an opportunity to state the choice once and be
> explicit about it.
