---
title: "ECE 2213 · 2020 Exam Style Answers"
tags:
  - numerical-methods
  - previous-year
---

# ECE 2213: 2020 Semester Final · Exam Style Answers

**RUET · ECE Dept · B.Sc. Engineering 2nd Year Even Semester Examination, 2020**
**Full Marks:** 96 · **Time:** 03 Hours

> [!info] Format
> Concise, mark-aligned, written as an answer script.
> Question text and marks come from the paper:
> [[PreviousYearQuestions/2020|the 2020 paper]].
> Every numerical here was derived twice by independent routes. Where the two
> routes disagreed, the disagreement was settled before the next question was
> written, and the divergence is recorded in a callout.
>
> This is a pre-OBE paper, so there is **no CLO column**. Marks only.

> [!warning] Four gaps in the printed paper, all handled in place
> **Q.2(b)** no starting value is given for Newton. Two defensible starts are run
> and both reported.
> **Q.5(b)** the $t$ column is printed out of order, $0.5$ before $0.2$. It turns
> out not to matter, and the reason is set out in Q.5(b).
> **Q.6(b)** six points give **five** intervals, which is odd, so Simpson's $1/3$
> cannot cover the range in one piece. Three legal repairs are given.
> **Q.6(c)** the last two differences in the table flatten, so the data is not
> smooth. Two formulas are given with their disagreement.

---

# SECTION A

## Question 1

### **(a) Why are numerical methods for? What are the sources of errors in numerical methods? Discuss them. [Marks: 06]**

**Why we need them.** Most engineering problems have no closed-form answer.

1. **No analytic solution exists.** A coupled circuit, a heat exchanger, a
   transmission line, a semiconductor device. The governing equation is known and
   the answer is not.
2. **The scale kills hand algebra.** A discretised PDE gives thousands of
   unknowns. A million from a fine mesh. No symbolic route exists.
3. **Data arrive irregular.** Measurements are unevenly spaced and noisy.
   Interpolation and least squares take them as they come.
4. **Experiments are expensive.** A simulation can be rerun at any parameter
   value, for free, long before the hardware is built.
5. **Design needs iteration.** An optimiser calls the solver hundreds of times
   while it searches.

**Sources of error.** Two families, both of which must be tracked.

| Error | What it is | Where it comes from | How to fight it |
| :-- | :-- | :-- | :-- |
| **Truncation** | The method is not exact | Replacing a derivative by a finite difference, or cutting an infinite series | Use a higher-order formula, or a smaller $h$ |
| **Round off** | Digits are lost | Floating point is finite, and each operation adds a small error | Use higher precision, or reformulate to cancel less |

**Truncation error in detail.** For a central difference,

$$\frac{f(x+h)-f(x-h)}{2h} = f'(x) + \frac{h^2}{6}f'''(x) + \cdots$$

Hence the error is $O(h^2)$: halving $h$ reduces it by a factor of 4. For the trapezoid
rule it is $O(h^2)$ too. For Euler's method it is only $O(h)$, so halving $h$
halves the error. The order of accuracy fixes the error for a given step size.

**Round off error in detail.** A number with $p$ significant digits carries a
relative uncertainty near $10^{-p}$. Every addition roughly doubles the absolute
error of the operands, and every multiplication squares the relative error. With
$n$ sequential steps the errors accumulate, giving a growth like $n \epsilon$ for
additions.

**Round off, truncation, and the optimal step size.** The two errors pull in
opposite directions.

- Truncation error $\propto h^p$, and it **falls** as $h$ falls.
- Round off error $\propto \frac{\epsilon}{h^p}$, and it **rises** as $h$ falls,
  because dividing by a small $h$ amplifies the rounding in the numerator.

The total is smallest where the two cross, and for a central difference that is
near $h \approx \epsilon^{1/3}$, about $6 \times 10^{-6}$ in double precision.
Below that, adding more points makes the answer **worse**. This is why a table
like 2020 Q.3(b), whose $y$ values are integers and so carry no rounding at all,
permits a very small $h$ with no penalty.

$$
\boxed{\text{No closed form exists, the data are irregular, and design needs many repeated solves}}
$$

---

### **(b) How are errors represented? Write down their expressions. Obtain their values to approximate a current as $9.05$ Amp instead of its true value $10$ Amp. Justify, which representation is better. [Marks: 06]**

**Definitions.** Let $v_t$ be the true value and $v_a$ the approximate value.

**Absolute error.** The size of the mistake, in the units of the quantity.

$$E_a = v_a - v_t \qquad \text{or} \qquad |E_a| = |v_a - v_t|$$

It is the only error directly measurable, and it carries the same units
as the answer.

**Relative error.** The mistake as a fraction of the true value. It is
dimensionless, so it can be compared across quantities of different size.

$$E_r = \frac{v_a - v_t}{v_t} \qquad \text{percentage relative error} = \frac{v_a - v_t}{v_t} \times 100$$

The denominator is the **true** value, not the approximate one. That choice is
what makes the measure meaningful, and it is the point examiners check.

**Now the numbers.** $v_a = 9.05$ Amp, $v_t = 10$ Amp.

$$
E_a = 9.05 - 10 = -0.95 \text{ Amp}, \qquad |E_a| = 0.95 \text{ Amp}
$$

$$
E_r = \frac{9.05 - 10}{10} = \frac{-0.95}{10} = -0.095
$$

$$
\text{percentage relative error} = -0.095 \times 100 = -9.5\%
$$

The sign says the approximation is **low**, which absolute error alone cannot
give a quantity that can be reasoned about directly.

| Representation | Value | Units |
| :-- | --: | :-- |
| Absolute error | $0.95$ | Amp |
| Relative error | $0.095$ | none |
| Percentage relative error | $9.5\%$ | none |

**Which is better, and why.** **Relative error** is the better representation, for
three reasons.

1. **It is scale-free.** A $0.95$ Amp error is trivial on a $10$ kA line and
   fatal on a $10$ mA sensor. The relative error says $9.5\%$ in both cases, so it
   ranks the two directly.
2. **It survives unit changes.** Measure the same current in milliamps and the
   absolute error becomes $950$ mA, which looks ten times worse. The relative
   error is still $0.095$. The relative error is invariant.
3. **It is what stopping criteria use.** A solver halts when the *relative* step
   falls below a tolerance, so that the test means the same thing at any
   magnitude.

Where absolute error wins: when the quantity is itself an error, a tolerance, or
a dimensional quantity where a fraction makes no sense, such as a length or a
time. Reporting "the beam is off by $2$ mm" beats "off by $0.4\%$".

> [!warning] The trap is the denominator
> Writing $\frac{9.05 - 10}{9.05} = -0.10497$ is the classic error. It looks
> reasonable and it is wrong. That figure is the error relative to the
> **approximate** value, which is not a standard measure and which changes as the
> iteration improves. Only the true value belongs in the denominator, and here it
> is $10$, not $9.05$.
>
> The gap is small, $9.5\%$ against $10.5\%$, and easy to overlook. At $99.5$
> against $100$ the same slip gives $0.5\%$ instead of $0.50\%$, still small, and
> students who never check it never find out.
>
> **Related:** this is the same distinction as 2024 Q.1(b) and 2023 Q.1(b). Fix
> the true value in memory: *relative error is always taken over the true value.*

$$
\boxed{|E_a| = 0.95 \text{ Amp}, \qquad E_r = -0.095, \qquad \text{percentage} = -9.5\%}
$$

---

## Question 2

### **(a) Define roots of an equation. List the comparisons among bisection, secant, false position and Newton-Raphson methods. [Marks: 06]**

**Root of an equation.** A **root** of $f(x) = 0$ is a value $x^*$ with
$f(x^*) = 0$. The graph of $f$ crosses or touches the $x$-axis at $x^*$.

A root is **simple** if $f'(x^*) \ne 0$, and **multiple** (or repeated) if
$f'(x^*) = 0$. The distinction matters because the methods below all assume a
simple root; a repeated root makes their convergence much slower.

A root is **explicit** if it can be written in closed form, and **implicit** if
it can only be found numerically. $\sqrt{2}$ is explicit. The root of
$x^5 - x - 1 = 0$ is implicit.

**The four methods compared.**

| | Bisection | False position | Secant | Newton-Raphson |
| :-- | :-- | :-- | :-- | :-- |
| Type | Bracketing | Bracketing | Open | Open |
| Needs $f'$ | No | No | No | **Yes** |
| Needs a sign change | **Yes** | **Yes** | No | No |
| Information used | Endpoints only | Endpoints, keeps one fixed | Last **two** points | Value **and** slope at one point |
| New point from | Midpoint | Chord crossing | Chord through last two | Tangent at last point |
| Convergence order | 1 (linear) | 1, often faster | 1.618 (golden ratio) | **2 (quadratic)** |
| Starts from | $a_0$ | $a_0$ | $x_0, x_1$ | $x_0$ only |
| Guaranteed | **Yes**, from any valid bracket | **Yes** | No | No |
| Function calls per step | 1 | 1 | 1 | 2 (value and derivative) |
| Weakness | Slow, and halves the interval | Stalls on one side for strong convexity | Can diverge, can lose the bracket | Sensitive to the start |

**How they relate.** They form a ladder from safest to fastest.

- **Bisection** is the safety net. It only needs a sign change, and it can never
  fail. That guarantee is why it survives in production codes.
- **False position** uses the same bracket but wastes it, because it keeps only
  one endpoint and lets the other run away. Faster than bisection, but it stalls
  on strongly convex functions.
- **Secant** throws the bracket away and fits a line through the last two
  points. The order $1.618$ is better than the labels "linear" suggest.
- **Newton** throws away the history except one point and uses the slope. It
  converges quadratically, so it is the method of choice when $f'$ is available
  and the start is good.

**The practical rule.** Keep a bracket. Try Newton. If a step leaves the
bracket, take a bisection step instead. This hybrid keeps Newton's speed and
bisection's guarantee, and it is what real root finders do. See the worked
warning in 2021 Q.7(b) and 2023 Q.5(c) for what happens without it.

$$
\boxed{\text{Bracketing methods are safe and slow; open methods are fast and unguaranteed}}
$$

---

### **(b) An electrical power equation is given as follows: $3I^2 - 4I - 4 = 0$. Calculate 3 iterations of the Newton-Raphson method to obtain the value of current. [Marks: 06]**

**Step 1. Set up.**

$$
f(I) = 3I^2 - 4I - 4, \qquad f'(I) = 6I - 4
$$

**Step 2. Choose a starting value.** The paper prints none, so we pick one and
say so. A current is a positive quantity, and

$$
f(1) = 3 - 4 - 4 = -5 < 0, \qquad f(3) = 27 - 12 - 4 = 11 > 0
$$

Hence a root lies in $(1, 3)$. Take the left end, $I_0 = 1$.

**Step 3. The iteration.**

$$
I_{n+1} = I_n - \frac{f(I_n)}{f'(I_n)} = I_n - \frac{3I_n^2 - 4I_n - 4}{6I_n - 4}
$$

**Step 4. Three iterations.**

At $I_0 = 1$: $f(1) = -5$ and $f'(1) = 2$.

$$
I_1 = 1 - \frac{-5}{2} = 1 + 2.5 = 3.500000
$$

At $I_1 = 3.5$: $f(3.5) = 3(12.25) - 14 - 4 = 36.75 - 18 = 18.75$ and
$f'(3.5) = 21 - 4 = 17$.

$$
I_2 = 3.5 - \frac{18.75}{17} = 3.5 - 1.102941 = 2.397059
$$

At $I_2 = 2.397059$: $f = 3(5.745893) - 9.588236 - 4 = 17.237679 - 13.588236 = 3.649443$
and $f' = 14.382354 - 4 = 10.382354$.

$$
I_3 = 2.397059 - \frac{3.649443}{10.382354} = 2.397059 - 0.351504 = 2.045555
$$

| $n$ | $I_n$ | $f(I_n)$ | $f'(I_n)$ |
| --: | --: | --: | --: |
| 0 | 1.000000 | $-5.000000$ | 2.000000 |
| 1 | 3.500000 | 18.750000 | 17.000000 |
| 2 | 2.397059 | 3.649443 | 10.382354 |
| 3 | 2.045555 | 0.370665 | 8.273329 |

$$
\boxed{I_3 = 2.0456 \text{ Amp after three iterations, and the true root is } I = 2 \text{ Amp}}
$$

**Step 5. Check the exact root.** The quadratic formula settles it:

$$
I = \frac{4 \pm \sqrt{16 + 48}}{6} = \frac{4 \pm 8}{6}
$$

which gives $I = 2$ and $I = -\frac{2}{3}$. Only $I = 2$ is a physical current,
and $I_3 = 2.045555$ is closing on it.

> [!info] Check by two independent routes
> **Closed form.** $I = 2$ and $I = -\tfrac{2}{3}$, from the quadratic formula
> above. The negative root is rejected on physical grounds, not numerical ones.
> Substituting back: $3(2)^2 - 4(2) - 4 = 12 - 8 - 4 = 0$ exactly.
>
> **A different starting value.** Starting from $I_0 = 3$, which is the right end
> of the same bracket:
>
> | $n$ | $I_n$ | $f(I_n)$ | $f'(I_n)$ |
> | --: | --: | --: | --: |
> | 0 | 3.000000 | 11.000000 | 14.000000 |
> | 1 | 2.214286 | 1.852041 | 9.285714 |
> | 2 | 2.014835 | 0.119342 | 8.089011 |
> | 3 | 2.000082 | 0.000653 | 8.000490 |
>
> Three iterations from $I_0 = 3$ reach $2.000082$, an error of $8.2 \times 10^{-5}$,
> against $0.0456$ from $I_0 = 1$. Both are correct Euler-free Newton runs; the
> start nearer the root simply needs fewer steps. **Same root, different
> arithmetic.**

> [!warning] Two traps in this question
> **1. The start matters more than the count.** $I_0 = 1$ throws the first iterate
> to $3.5$, a full $1.5$ past the answer at $2$. The reason is visible in the
> table: at $I_0 = 1$ the derivative is only $2$ while $f$ is $-5$, so the ratio
> $f/f'$ is $2.5$ and the first step is long. Starting from $3$, where
> $f/f' = 0.786$, the first step is short. Three iterations from a good start
> nearly reaches the root; three from a poor start only gets close.
>
> **2. There are two roots and only one is physical.** Newton's method has no
> built-in preference, and a careless start can land on $I = -\tfrac{2}{3}$. The
> quadratic formula shows both. Discard the negative one on physical grounds,
> and say that this is why. Starting from $I_0 = 0$ is unsuitable: it gives
> $f(0) = -4$, $f'(0) = -4$, so $I_1 = 0 - \frac{-4}{-4} = -1$, which walks
> straight off toward the negative root.
>
> The general safeguard is the same as in Q.2(a): keep a bracket, and fall back
> to bisection whenever a Newton step leaves it.

---

## Question 3

### **(a) What is the main difference between interpolation and extrapolation? Where are they used? [Marks: 03]**

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

### **(b) The population of a town in the decennial census was as given below. Estimate the population for the year (i) 1895 and (ii) 1925. [Marks: 04]**

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

### **(c) Define curve fitting. Also determine the constants $a$ and $b$ by the method of least squares such that $y = a e^{bx}$ fits the following data. [Marks: 05]**

**Curve fitting.** Finding the constants of a chosen function form so that it
comes as close as possible to a set of data points. Unlike interpolation, the
curve is **not** required to pass through the points. It is the right tool when
the data carry measurement error, or when more points are given than a
polynomial of the wanted degree needs.

**Step 1. Linearise.** The model $y = ae^{bx}$ is nonlinear in the unknowns
$e^b$ and $a$. Taking natural logarithms makes it linear:

$$\ln y = \ln a + bx$$

Let $Y = \ln y$, $A = \ln a$ and $B = b$. Then $Y = A + Bx$, which is a straight
line, and the method of least squares applies to the **logarithms**.

> [!warning] What least squares now means
> Minimising $\sum (Y_i - A - Bx_i)^2$ is **not** the same as minimising
> $\sum (y_i - ae^{bx_i})^2$. The first weights each point equally in log space,
> so a point with a large $y$ counts no more than a point with a small $y$. Since
> this data spans $4$ to $223$, a factor of $55$, that difference is large here.
>
> Fitting $Y$ against $x$ linearly is the standard textbook route and is what is
> expected. If a question ever demands the true nonlinear least squares, the
> normal equations have to be written for $y_i - ae^{bx_i}$ instead, and the
> answer changes. The one applied is stated.

**Step 2. Logarithms of the data.**

| $x$ | $y$ | $Y = \ln y$ | $x^2$ | $xY$ |
| --: | --: | --: | --: | --: |
| 2 | 4.077 | 1.405361 | 4 | 2.810722 |
| 4 | 11.084 | 2.405503 | 16 | 9.622012 |
| 6 | 30.128 | 3.405455 | 36 | 20.432730 |
| 8 | 81.897 | 4.405462 | 64 | 35.243696 |
| 10 | 222.62 | 5.405466 | 100 | 54.054660 |
| $\Sigma$ | | 17.027248 | 220 | 122.163825 |

**Step 3. Normal equations.**

$$
n = 5, \quad \sum x = 30, \quad \sum Y = 17.027248, \quad \sum x^2 = 220, \quad \sum xY = 122.163825
$$

$$
b = \frac{n\sum xY - \sum x \sum Y}{n\sum x^2 - (\sum x)^2}
= \frac{5(122.163825) - 30(17.027248)}{5(220) - 30^2}
= \frac{610.819125 - 510.817440}{1100 - 900}
= \frac{100.001694}{200}
= 0.500008
$$

$$
\ln a = \frac{\sum Y - b\sum x}{n} = \frac{17.027248 - 15.000254}{5} = \frac{2.026994}{5} = 0.405399
$$

$$
a = e^{0.405399} = 1.499900
$$

**Step 4. The fitted curve.**

$$\boxed{b = 0.5000, \qquad a = 1.4999, \qquad y = 1.4999\,e^{0.5000x} \approx 1.5\,e^{x/2}}$$

**Step 5. Check the residuals.**

| $x$ | $y$ | Fitted $\hat y$ | $\ln y - (A + Bx)$ |
| --: | --: | --: | --: |
| 2 | 4.077 | 4.077221 | $-0.000054$ |
| 4 | 11.084 | 11.083224 | $+0.000070$ |
| 6 | 30.128 | 30.127836 | $+0.000005$ |
| 8 | 81.897 | 81.897337 | $-0.000004$ |
| 10 | 222.62 | 222.623816 | $-0.000017$ |

Every residual is below $7 \times 10^{-5}$ in log space, so the straight line in
$\ln y$ against $x$ is an excellent description of the data.

> [!info] Check: the data was generated from a clean law
> The five values are $1.5e^{x/2}$ rounded to three decimals:
>
> | $x$ | $1.5e^{x/2}$ | Rounds to | Given |
> | --: | --: | --: | --: |
> | 2 | 4.077423 | 4.077 | 4.077 |
> | 4 | 11.083584 | 11.084 | 11.084 |
> | 6 | 30.128305 | 30.128 | 30.128 |
> | 8 | 81.897225 | 81.897 | 81.897 |
> | 10 | 222.619739 | 222.620 | 222.620 |
>
> All five match after rounding, which pins the intended answer at
> $a = 1.5$, $b = 0.5$ exactly. The least squares values $1.499900$ and
> $0.500008$ differ from that by $9.96 \times 10^{-5}$ and $8.47 \times 10^{-6}$,
> purely because the tabulated values were rounded to three decimals before
> reaching the reader.
>
> **So write $a = 1.5$, $b = 0.5$**, and note that the fit gives $1.4999$ and
> $0.50001$. This is the same lesson as 2020 Q.5(b) and 2021 Q.4(b): the rounding
> in the data sets the floor on accuracy, and here it is visible.

> [!note] Why the log route is the right instinct
> The model is exponential, so $y$ must stay positive, and $a$ and $b$ must have
> the right signs. Least squares on the logs gives both automatically. Fitting
> $y$ directly against $ae^{bx}$ with no log step would give a different curve,
> tilted toward the large-$y$ end, and the answer for $a$ would come out
> noticeably off $1.5$.
>
> The test is always: **does the fitted curve look straight on a semi-log plot?**
> If not, the model is wrong, not the arithmetic.

---

## Question 4

### **(a) What are the direct methods to solve linear system of equations? Describe any one of them. [Marks: 06]**

**The system.** To solve

$$A\mathbf{x} = \mathbf{b}, \qquad A = [a_{ij}] \in \mathbb{R}^{n\times n}$$

Direct methods produce the exact solution in a **fixed** number of steps, decided
in advance by $n$. They do not iterate toward the answer, which is what
distinguishes them from iterative methods.

**The two families.**

1. **Elimination methods.** Reduce the augmented system to upper triangular form
   by elementary row operations, then back-substitute. Examples: **Gaussian
   elimination**, **Gauss-Jordan elimination**, and **LU factorisation**.
2. **Matrix factorisation methods.** Write $A$ as a product of simpler matrices
   and solve the pieces in sequence. Examples: **Crout**, **Cholesky**
   (symmetric positive definite only), **QR**.

Everything else is a variant of one of these two ideas.

**Described: Gaussian elimination with partial pivoting.**

Write the augmented matrix $[\,A \mid \mathbf{b}\,]$. For column $k$, find the
row $p \ge k$ with the largest $\lvert a_{pk}\rvert$, and swap rows $k$ and $p$.
Then eliminate the entries below the pivot:

$$\text{for } i = k+1, \dots, n: \qquad m_{ik} = \frac{a_{ik}}{a_{kk}}, \qquad \text{row}_i \leftarrow \text{row}_i - m_{ik}\,\text{row}_k$$

This makes every entry below the diagonal of column $k$ zero. Repeat for
$k = 1, 2, \dots, n-1$. The result is upper triangular:

$$
\begin{bmatrix} a_{11} & a_{12} & \cdots & a_{1n} \\
0 & a_{22} & \cdots & a_{2n} \\
\vdots & & \ddots & \vdots \\
0 & 0 & \cdots & a_{nn}
\end{bmatrix} \mathbf{x} = \mathbf{c}
$$

Now back-substitute from the bottom:

$$x_n = \frac{c_n}{a_{nn}}, \qquad x_i = \frac{1}{a_{ii}}\left(c_i - \sum_{j=i+1}^{n} a_{ij} x_j\right)$$

**Worked micro-example.** Solve $2x + y = 5$ and $x - y = 1$.

$$
\begin{bmatrix} 2 & 1 & | & 5 \\ 1 & -1 & | & 1 \end{bmatrix}
$$

Pivot in column 1 is $2$; the row 2 entry is $1$, so no swap is needed.
$m_{21} = \frac{1}{2}$, and row 2 becomes
$\left[0, -1 - \frac{1}{2}\mid 1 - \frac{5}{2}\right] = \left[0, -\frac{3}{2} \mid -\frac{3}{2}\right]$.

Back-substitute: $y = \frac{-3/2}{-3/2} = 1$, then $2x = 5 - 1 = 4$ so $x = 2$.

$$
\boxed{x = 2, \qquad y = 1}
$$

Check: $2(2) + 1 = 5$ and $2 - 1 = 1$. Both hold.

**Why pivoting is not optional.** The step divides by the pivot. A **zero** pivot
stops the method dead. A **tiny** pivot is worse, because the multiplier
$m_{ik} = \frac{a_{ik}}{a_{kk}}$ becomes huge, and subtracting large nearly equal
numbers destroys most of the significant digits. The method still runs and
returns a wrong answer, with no warning. Partial pivoting costs one comparison
per candidate and no extra arithmetic, and it is the standard safeguard.

| Method | Work | Storage | Notes |
| :-- | :-- | :-- | :-- |
| Gaussian elimination | $\frac{2}{3}n^3$ | $n^2$ | Triangular solve is $O(n^2)$ |
| Gauss-Jordan | $n^3$ | $n^2$ | Gives the inverse directly |
| LU factorisation | $\frac{2}{3}n^3$ | $n^2$ | Reuse the factors for many right sides |
| Cholesky | $\frac{1}{3}n^3$ | $\frac{1}{2}n^2$ | Half the work, but needs $A$ symmetric positive definite |

**Direct against iterative.** Direct methods cost $O(n^3)$ and are unbeatable for
small and dense systems. But $n^3$ becomes hopeless: at $n = 10^4$ it is
$10^{12}$ operations, and the matrix alone needs $8 \times 10^7$ entries. Large
sparse systems, which is what discretised PDEs produce, are handled by iterative
methods that touch only the non-zero entries. The iterative methods in
Q.4(b) and Q.7(b) of this paper are the other side of that trade.

$$
\boxed{\text{Eliminate to upper triangular form, pivot to stay safe, then back-substitute}}
$$

---

### **(b) Solve $I_1$, $I_2$ and $I_3$ using Gauss-Seidal method. [Marks: 06]**

![Three-mesh DC resistive network with a 400 V source, 20, 40, 10 and 100 ohm resistors, and a downward 10 A current source, with clockwise mesh currents I1, I2, I3](diagrams/2020_Q4b_circuit.jpg)
*Figure 2020 Q4(b): three-mesh DC circuit with an independent voltage source and an independent current source (Source: Page 1, Q.4(b))*

**Step 1. Deal with the current source first.** Mesh 3 is bounded on the right by
an ideal $10$ A current source and on the left by the $100\ \Omega$ resistor
shared with mesh 2. A current source **fixes** the branch current, so the
clockwise mesh current is

$$I_3 = 10 \text{ A}$$

This is the step that trips people up. A current source in a branch forces
$I_3$ to equal it, full stop, and it drops out of the system entirely.

**Step 2. Mesh 1, KVL.** Going clockwise around the left loop: rise $400$ V
through the source, drop across the $20\ \Omega$, then across the shared
$40\ \Omega$ which carries $I_1 - I_2$ because $I_2$ returns through it.

$$-400 + 20 I_1 + 40(I_1 - I_2) = 0$$

$$60 I_1 - 40 I_2 = 400$$

**Step 3. Mesh 2, KVL.** The $40\ \Omega$ carries $I_2 - I_1$, the $10\ \Omega$
carries $I_2$ alone, and the $100\ \Omega$ carries $I_2 - I_3$.

$$40(I_2 - I_1) + 10 I_2 + 100(I_2 - I_3) = 0$$

$$-40 I_1 + 150 I_2 = 100 I_3 = 1000$$

**Step 4. The system to iterate.** Three equations, but $I_3$ is already known, so
two unknowns remain:

$$\begin{cases} 60 I_1 - 40 I_2 = 400 \\ -40 I_1 + 150 I_2 = 1000 \end{cases}$$

Solve each for its own variable, newest value first:

$$\begin{cases} I_1 = \dfrac{40 I_2 + 400}{60} \\[3mm] I_2 = \dfrac{1000 + 40 I_1}{150} \end{cases}$$

**Step 5. Gauss-Seidel.** Use the value just computed, never the previous
iteration's. Start from $I_1^{(0)} = I_2^{(0)} = 0$.

| $k$ | $I_1$ | $I_2$ |
| --: | --: | --: |
| 0 | 0.000000 | 0.000000 |
| 1 | 6.666667 | 8.444444 |
| 2 | 12.296296 | 9.945679 |
| 3 | 13.297119 | 10.212565 |
| 4 | 13.475043 | 10.260012 |
| 5 | 13.506674 | 10.268447 |
| 6 | 13.512298 | 10.269946 |
| 7 | 13.513297 | 10.270213 |
| 8 | 13.513475 | 10.270260 |
| 9 | 13.513507 | 10.270268 |
| 10 | 13.513512 | 10.270270 |

Iteration 1: $I_1^{(1)} = \frac{40(0) + 400}{60} = 6.666667$, then
$I_2^{(1)} = \frac{1000 + 40(6.666667)}{150} = \frac{1000 + 266.6667}{150} = 8.444444$.

**Step 6. Answer.**

$$
\boxed{I_1 = 13.5135 \text{ A}, \qquad I_2 = 10.2703 \text{ A}, \qquad I_3 = 10.0000 \text{ A}}
$$

> [!info] Check by two independent routes
> **Exact solution.** The $2\times2$ system is solved directly by elimination:
> multiply the first equation by $150$ and the second by $40$, then add.
> $9000 I_1 - 6000 I_2 = 60000$ and $-1600 I_1 + 6000 I_2 = 40000$. Adding gives
> $7400 I_1 = 100000$, so
> $$I_1 = \frac{100000}{7400} = \frac{500}{37} = 13.513514, \qquad I_2 = \frac{380}{37} = 10.270270$$
> Both are exact rationals. Gauss-Seidel iteration 10 returns $13.513512$ and
> $10.270270$: the second matches to six decimal places, the first to six
> significant figures. $I_1$ needs iteration 13 to reach $13.513514$ on the nose.
> The two variables converge at different rates because $I_1$ is updated first in
> each sweep and $I_2$ therefore always uses a fresher $I_1$.
>
> **Substitute back into the mesh equations.** Mesh 1:
> $60(13.513514) - 40(10.270270) = 810.8108 - 410.8108 = 400$ exactly.
> Mesh 2: $-40(13.513514) + 150(10.270270) - 100(10) = -540.5406 + 1540.5405 - 1000 = 0$
> to within $10^{-13}$. Both KVL loops close.
>
> **Convergence rate.** The errors in $I_1$ fall $6.8468, 1.2172, 0.2164, 0.0385$,
> $0.0068$ over the first five sweeps, a factor of exactly $5.625$ each time.
> That factor is $1/\rho^2$ where $\rho = 0.4216$ is the spectral radius computed
> below: $1/(0.4216)^2 = 5.625$. The errors in $I_2$ fall $1.8258, 0.3246, 0.0577$,
> $0.0103, 0.0018$, the same ratio.

> [!warning] The row order decides whether this converges at all
> Solve equation 2 first, $I_2 = \frac{1000 + 40 I_1}{150}$, and the iteration
> **diverges**: $-25$, $-203.1$, $-1205.1$, $-6841.1$, $-38543$. The values grow
> without bound.
>
> The reason is the iteration matrix. In the order used above it is
> $$\begin{bmatrix} 0 & \frac{40}{60} \\ \frac{40}{150} & 0 \end{bmatrix} = \begin{bmatrix} 0 & 0.6667 \\ 0.2667 & 0 \end{bmatrix}$$
> whose eigenvalues are $\pm\sqrt{0.6667 \times 0.2667} = \pm 0.4216$, so the
> spectral radius is $0.4216 < 1$ and the iteration contracts. Reverse the order
> and it becomes
> $$\begin{bmatrix} 0 & \frac{150}{40} \\ \frac{60}{40} & 0 \end{bmatrix}$$
> with spectral radius $\sqrt{3.75 \times 1.5} = 2.3717 > 1$, which diverges.
>
> The fix is the same everywhere in this course: **keep a diagonal-dominant
> ordering.** Each equation should solve for the variable with the largest
> coefficient in that row. Here that is $I_1$ in row 1 ($60$ beats $40$) and
> $I_2$ in row 2 ($150$ beats $40$), which is exactly the order used. The same
> trap appears in 2021 Q.7(b), 2023 and 2024.

> [!note] Sanity check on the current directions
> All three mesh currents come out positive, so all three really do run clockwise
> as assumed. $I_2 = 10.27$ A exceeds the $10$ A in the source branch, and that
> is consistent: the $10$ A source pushes current into the node shared with the
> $100\ \Omega$ resistor, and the $150\ \Omega$ mesh must carry slightly more
> than that because it also returns some of $I_1$'s current through the shared
> $40\ \Omega$. A negative value anywhere would mean the assumed direction was
> wrong and must be flipped before the answer means anything.

---

# SECTION B

## Question 5

### **(a) Deduce the Newton's forward difference interpolating polynomial. [Marks: 06]**

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
> [[NM-4.7 · Newton's Forward Difference]].

---

### **(b) Using Newton's divided difference interpolating polynomial estimate the value of signal $s(t)$ at $t = 2.25$ sec for the following tabulated values. [Marks: 06]**

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

## Question 6

### **(a) Compare Simpson's $1/3$rd and $3/8$th rules. [Marks: 03]**

Both are **Newton-Cotes** rules: they fit a polynomial through the data at
equally spaced nodes and integrate that polynomial exactly over the panel. They
differ in how many nodes each panel uses and therefore in which interval counts
each admits.

| | Simpson's $1/3$ | Simpson's $3/8$ |
| :-- | :-- | :-- |
| Subintervals per panel | 2 | 3 |
| Nodes per panel | 3 | 4 |
| Weights | $1,\ 4,\ 1$ | $1,\ 3,\ 3,\ 1$ |
| Prefactor | $\dfrac{h}{3}$ | $\dfrac{3h}{8}$ |
| Panel interval count | Must be **even** | Must be a **multiple of 3** |
| Total intervals $n$ | Even | Multiple of 3 |
| Order of accuracy | 4 | 4 |
| Leading error term | $-\dfrac{h^5}{90}f^{(4)}$ | $-\dfrac{3h^5}{80}f^{(4)}$ |
| Error constant | $\frac{1}{90} = 0.0111$ | $\frac{3}{80} = 0.0375$ |

**Both are fourth order**, so both need a function with $f^{(4)}$ continuous
over the range. Neither is fourth order on a function with a discontinuous
fourth derivative, and neither is safe near a vertical asymptote or a jump.

**The accuracy difference.** With the same $h$, Simpson's $3/8$ has a leading
error constant $3.375$ times larger than $1/3$. So for equal $h$, **$1/3$ is more
accurate**, and $1/3$ is the default choice.

**The one place $3/8$ wins.** When the total interval count is odd, $1/3$ is
inapplicable while $3/8$ can still be used, provided the count is a multiple of
$3$. Five intervals is the standard case: $1/3$ is stuck, $3/8$ takes three of
them and something else takes two. That exact situation is in Q.6(b) below, and it is why the rule is worth
knowing.

**Standard mixed strategy** for an odd $n$ not divisible by $3$, for example
$n = 5$: apply $3/8$ to the last three intervals and $1/3$ to the remaining two,
or apply $1/3$ to the largest even block and the trapezoid rule to the leftover
one interval. Both appear in Q.6(b).

**Why the error behaves as it does.** A $3$-node panel interpolates a quadratic,
whose integration error involves $f''$. A $4$-node panel interpolates a cubic,
involving $f^{(4)}$. Symmetry about the panel centre cancels the odd-order terms
in both cases, which is why both reach fourth order rather than third.

$$
\boxed{\text{Both are fourth order; } 1/3 \text{ is more accurate at equal } h \text{ but needs an even interval count}}
$$

---

### **(b) A circuit is giving following output voltage equation: $v_0 = -\frac{1}{RC} \int_0^t v_i(t)\,dt$ where $R = 10\text{ k}\Omega, C = 1\ \mu\text{F}$. Use Simpson's $1/3$rd rule to find $v_0$ at $t = 1.25$. [Marks: 05]**

| $t$ | 0 | 0.25 | 0.50 | 0.75 | 1.00 | 1.25 |
| --- | --: | --: | --: | --: | --: | --: |
| $v_i(t)$ | 1 | 0.9793 | 0.9195 | 0.8261 | 0.7081 | 0.6201 |

> [!warning] Six points give five intervals, and five is odd
> Simpson's $1/3$ rule needs an **even** number of subintervals, because each
> panel spans two. This table has six points and therefore **five** subintervals.
> **The rule cannot be applied to the range $0$ to $1.25$ in one piece.**
>
> Applying the weights $1, 4, 2, 4, 2, 1$ across all six points gives $1.008075$,
> hence $v_0 = -100.8$, and that answer is wrong. Every individual
> multiplication is correct; the rule simply does not apply to an odd count.
> This is the single most common way to lose marks on this type of question.
>
> Three repairs are legal. They are given below, and they all land within
> $0.25$ of each other on a value near $106$.

**Step 1. The constant.**

$$RC = (10 \times 10^3)(1 \times 10^{-6}) = 10^{-2} \text{ s} = 0.01 \text{ s}, \qquad \frac{1}{RC} = 100 \text{ s}^{-1}$$

**Step 2. The integral.** Take $h = 0.25$ s. The largest even block is
$t = 0$ to $t = 1.00$, four intervals, and the leftover interval
$t = 1.00$ to $1.25$ goes to the trapezoid rule.

**Simpson's $1/3$ on $0$ to $1.00$**, with weights $1, 4, 2, 4, 1$:

$$
I_{1/3} = \frac{h}{3}\left[v_0 + 4v_1 + 2v_2 + 4v_3 + v_4\right]
= \frac{0.25}{3}\left[1 + 4(0.9793) + 2(0.9195) + 4(0.8261) + 0.7081\right]
$$

$$
= \frac{0.25}{3}\left[1 + 3.9172 + 1.8390 + 3.3044 + 0.7081\right] = \frac{0.25}{3}(10.7687) = 0.89739167
$$

**Trapezoid on $1.00$ to $1.25$:**

$$
I_T = \frac{h}{2}(v_4 + v_5) = \frac{0.25}{2}(0.7081 + 0.6201) = 0.125(1.3282) = 0.166025
$$

**Total:**

$$
I = 0.89739167 + 0.166025 = 1.06341667
$$

**Step 3. The output voltage.** The leading minus sign comes from the inverting
amplifier that realises the equation, and it must be carried through.

$$
v_0 = -\frac{1}{RC}\,I = -100(1.06341667) = -106.341667
$$

$$
\boxed{v_0(1.25) = -106.34 \text{ V}}
$$

> [!info] Check by two independent routes
> **Repair 2: trapezoid first, then Simpson.** Handle $t = 0$ to $0.25$ with the
> trapezoid rule and Simpson's $1/3$ on the remaining four intervals,
> $0.25$ to $1.25$:
> $$I_T = 0.125(1 + 0.9793) = 0.2474125, \qquad I_{1/3} = \frac{0.25}{3}\left[0.9793 + 4(0.9195) + 2(0.8261) + 4(0.7081) + 0.6201\right] = 0.8135000$$
> $$I = 1.0609125 \qquad\Rightarrow\qquad v_0 = -106.0913$$
> A different route, $0.25$ different on $106$, that is $0.24\%$.
>
> **Repair 3: mix Simpson's $1/3$ and $3/8$.** Two intervals from $0$ to $0.50$ by
> $1/3$, then three intervals from $0.50$ to $1.25$ by $3/8$:
> $$I_{1/3} = \frac{0.25}{3}\left[1 + 4(0.9793) + 0.9195\right] = 0.48639167$$
> $$I_{3/8} = \frac{3(0.25)}{8}\left[0.9195 + 3(0.8261) + 3(0.7081) + 0.6201\right] = \frac{0.09375}(6.1422) = 0.57583125$$
> $$I = 1.06222292 \qquad\Rightarrow\qquad v_0 = -106.2223$$
>
> All three legal repairs give $v_0$ between $-106.09$ and $-106.34$, a spread of
> $0.25$ on a value near $106$. **The choice of repair is not the exam's
> discriminator; recognising that a repair is needed at all is.**

> [!warning] Three things to get right here
> **1. The sign.** $v_0$ is **negative**. The equation carries a leading minus and
> the integral of a positive $v_i$ is positive, so the answer must be negative. A
> positive $v_0$ means the sign was dropped, and it is the most common slip in
> this question.
>
> **2. The units.** $\frac{1}{RC} = 100$, not $0.01$ and not $10^{-8}$. A $10$
> k$\Omega$ resistor and a $1\ \mu$F capacitor give a time constant of
> $10^4 \times 10^{-6} = 10^{-2}$ s, so the reciprocal is $100$. Converting
> microfarads to farads is where the factor of $10^6$ comes from.
>
> **3. Simpson's $1/3$ requires an even interval count.** Count the intervals,
> not the points: six points means five intervals, and five is odd.

> [!note] What the circuit is
> The relation $v_0 = -\frac{1}{RC}\int v_i\,dt$ is an op-amp integrator. The
> capacitor current is $i = C\frac{dv}{dt} = \frac{v_i}{R}$, and the output is the
> negative of the voltage across the capacitor, hence the minus sign. Simpson's
> $1/3$ rule is being used because the integrand is only known at six sample
> points, which is the situation in every real digitised measurement.

---

### **(c) The following table gives the angular displacements $\theta$ (radian) at different time intervals of time $t$ (sec). Calculate the angular velocity at the instant $t = 0.06$ sec. [Marks: 04]**

| $t$ | 0 | 0.02 | 0.04 | 0.06 | 0.08 | 0.10 | 0.12 |
| --- | --: | --: | --: | --: | --: | --: | --: |
| $\theta$ | 0.052 | 0.105 | 0.168 | 0.242 | 0.327 | 0.408 | 0.489 |

**Step 1. Angular velocity is the derivative.** $\omega = \dfrac{d\theta}{dt}$, so
this is numerical differentiation of a table with $h = 0.02$ s.

**Step 2. $t = 0.06$ is an interior node.** Data exist on both sides, at
$0.04$ and $0.08$, so the **three-point central** formula applies and is both
the most accurate of the three-point formulas and the natural one here.

$$
\left.\frac{d\theta}{dt}\right|_{0.06} \approx \frac{\theta_{0.08} - \theta_{0.04}}{2h} = \frac{0.327 - 0.168}{2(0.02)} = \frac{0.159}{0.04} = 3.975
$$

$$
\boxed{\left.\frac{d\theta}{dt}\right|_{t=0.06} \approx 3.975 \text{ rad/s}}
$$

**Step 3. The other available formulas**, for comparison.

| Formula | Nodes needed | Value at $t = 0.06$ |
| :-- | :-- | --: |
| Three-point central | $0.04, 0.06, 0.08$ | $3.975$ |
| Five-point central | $0.02$ to $0.10$ | $4.0375$ |
| Three-point forward | $0.06, 0.08, 0.10$ | $4.350$ |
| Three-point backward | $0.02, 0.04, 0.06$ | $3.975$ |

The five-point central formula is available here, because $0.06 - 2h = 0.02$ is
in the table:

$$
\left.\frac{d\theta}{dt}\right|_{0.06} \approx \frac{\theta_{0.02} - 8\theta_{0.04} + 8\theta_{0.08} - \theta_{0.10}}{12h} = \frac{0.105 - 8(0.168) + 8(0.327) - 0.408}{0.24}
$$

$$
= \frac{0.105 - 1.344 + 2.616 - 0.408}{0.24} = \frac{0.969}{0.24} = 4.0375
$$

> [!warning] The table is not smooth, and that is why the formulas disagree
> Build the difference table:
>
> | Order | Values |
> | :-- | :-- |
> | $\theta$ | 0.052, 0.105, 0.168, 0.242, 0.327, 0.408, 0.489 |
> | $\Delta\theta$ | 0.053, 0.063, 0.074, 0.085, 0.081, 0.081 |
> | $\Delta^2\theta$ | 0.010, 0.011, 0.011, $-0.004$, 0.000 |
> | $\Delta^3\theta$ | 0.001, 0.000, $-0.015$, 0.004 |
>
> The first differences grow smoothly, $0.053, 0.063, 0.074, 0.085$, then **drop
> to $0.081$ and stay flat**. For a body starting from rest under constant angular
> acceleration the first differences should grow linearly and the second
> differences should be constant. Here the second differences run
> $0.010, 0.011, 0.011$ and then jump to $-0.004$ and $0.000$. So the last three
> samples do not belong to the same smooth motion as the first four.
>
> **This is why the three-point and five-point answers differ by $1.6\%$.** The
> five-point formula reaches out to $t = 0.02$ and $0.10$, sampling the
> discontinuity, and returns the larger value. The three-point formula uses only
> the smooth middle region.
>
> **Write the three-point central answer, $3.975$ rad/s, and mention the
> discrepancy.** Reporting a single value without noting that the data are irregular
> leaves the table unchecked. Note also the physical reading: a first difference
> of $0.085$ over $0.02$ s already gives a velocity of
> $4.25$ rad/s, so an answer near $4$ is the right order and any answer near
> $3$ warrants re-examination.

> [!note] Central, forward, or backward
> At an **interior** node with data on both sides, the central formula is the
> natural choice and the most accurate among three-point formulas. The five-point central
> formula is $O(h^4)$ against $O(h^2)$ for the three-point, and it is available
> here, so if the data had been smooth it would be the better answer.
>
> Use a one-sided formula only when the node is near an edge and no data exist on
> the other side. In 2021 Q.7(c) the five-point central formula was **not**
> available at the requested node and the three-point one was forced; here both
> are available, so the choice is about data quality rather than availability.

---

## Question 7

### **(a) Derive modified Euler's method. What is the major limitation of Euler's method? [Marks: 04]**

**Euler's method, for reference.** For $\frac{dy}{dx} = f(x, y)$ with
$y(x_0) = y_0$ and step $h$,

$$y_{n+1} = y_n + h f(x_n, y_n)$$

It takes the slope at the **left** endpoint of the interval and assumes it holds
across the whole interval. The local truncation error is $O(h^2)$ and the global
error is $O(h)$, so the method is **first order**.

**Step 1. The idea of the modification.** Euler's weakness is that it uses only
one slope per step and that slope is at the wrong end. Average two slopes, one at
each end of the interval, and the error drops by a whole order.

**Step 2. Compute the slope at the left end.** Predict with plain Euler:

$$y_p = y_n + h f(x_n, y_n)$$

**Step 3. Compute the slope at the right end**, using that predicted value:

$$f_{n+1} = f(x_n + h, y_p)$$

**Step 4. Average the two slopes and take the step.**

$$
\boxed{y_{n+1} = y_n + \frac{h}{2}\left[f(x_n, y_n) + f(x_n + h, y_n + h f(x_n, y_n))\right]}
$$

This is **Heun's method**, also called the **improved Euler method** or the
**trapezoidal method**. Another name for it is the **two-stage second-order
Runge-Kutta method**, since the $k$ values below reproduce it exactly.

**Step 5. The Runge-Kutta form**, to show where it comes from. With
$k_1 = h f(x_n, y_n)$ and $k_2 = h f(x_n + h, y_n + k_1)$,

$$y_{n+1} = y_n + \frac{1}{2}(k_1 + k_2)$$

**Step 6. Accuracy.** The two-slope average cancels the leading local error
term, so the local truncation error becomes $O(h^3)$ and the global error becomes
$O(h^2)$. The method is now **second order**: halving $h$ cuts the error by 4
instead of 2. The cost is one extra function evaluation per step, so roughly
double the work for one extra order of accuracy. That is nearly always worth it.

**The major limitation of Euler's method.**

> **Euler's method is first order accurate, so it needs far too many steps for
> the accuracy usually wanted, and it goes unstable when $h$ exceeds a stability
> limit.**

Two parts, and the second is the serious one.

1. **Low order.** Global error $O(h)$. Reaching four correct digits with
   $h = 10^{-4}$ means $10^4$ steps, and the accumulated round off grows with
   the step count, so the gain flattens out.

2. **Conditional stability.** For the test equation $y' = \lambda y$ with
   $\lambda < 0$, Euler gives $y_{n+1} = (1 + h\lambda)y_n$. Stability needs
   $\lvert 1 + h\lambda\rvert < 1$, that is
   $$h < \frac{2}{\lvert\lambda\rvert}$$
   and for a stiff system $\lvert\lambda\rvert$ is enormous, so $h$ must be
   tiny. Meanwhile the truncation error wants $h$ small too, so the two demands
   are compatible but expensive, and any step-size increase blows the solution up
   with no warning.

**Practical note.** Heun's method is not unconditionally stable either. For
$y' = \lambda y$ it gives $y_{n+1} = (1 + z + z^2/2)y_n$ with $z = h\lambda$, and
stability needs $\lvert 1 + z + z^2/2\rvert < 1$, which allows
$-2 < z < 0$, a range of $2$ against Euler's $2$. It is modestly better, not a
cure. Real stiff solvers use the backward or implicit trapezoidal methods, which
have unbounded stable regions.

> [!warning] The trap: "improved" does not mean "exact"
> Two names cause confusion and neither is wrong.
>
> **Modified Euler** sometimes means Heun's method above, and sometimes means the
> **midpoint method**, which uses the slope at the midpoint of the interval:
> $$y_{n+1} = y_n + h f\left(x_n + \frac{h}{2},\ y_n + \frac{h}{2} f(x_n, y_n)\right)$$
> Both are second order, and both are called "modified Euler" in the wild. Check
> which variant a course intends before using the name.
>
> A related trap: writing $y_{n+1} = y_n + h f\left(\frac{x_n + x_{n+1}}{2}, \frac{y_n + y_{n+1}}{2}\right)$
> is **not** an algorithm at all, because $y_{n+1}$ appears on the right-hand
> side. That is an implicit formula needing a solution, not a one-step method.
> Heun's method avoids the problem by replacing $y_{n+1}$ with an Euler **predictor**
> in the slope evaluation, which is exactly the point of Step 2.

$$
\boxed{y_{n+1} = y_n + \frac{h}{2}\left[f(x_n,y_n) + f(x_n+h,\, y_n + h f(x_n,y_n))\right],\quad \text{second order}}
$$

---

### **(b) Solve, by Euler's method, the equation $\frac{dy}{dx} = x + y, \; y(0) = 0$. Choose $h = 0.2$ and compute $y(0.4)$ and $y(0.6)$. [Marks: 04]**

**Step 1. The method.** With $f(x, y) = x + y$ and $h = 0.2$,

$$y_{n+1} = y_n + 0.2(x_n + y_n), \qquad x_{n+1} = x_n + 0.2$$

Start at $x_0 = 0$, $y_0 = 0$.

**Step 2. Three steps.**

| Step | $x_n$ | $y_n$ | Slope $x_n + y_n$ | $y_{n+1} = y_n + 0.2 \times \text{slope}$ |
| --: | --: | --: | --: | --: |
| 1 | 0.0 | 0.000000 | $0.0 + 0.0 = 0.0$ | $0.0 + 0.2(0) = 0.000000$ |
| 2 | 0.2 | 0.000000 | $0.2 + 0.0 = 0.2$ | $0.0 + 0.2(0.2) = 0.040000$ |
| 3 | 0.4 | 0.040000 | $0.4 + 0.04 = 0.44$ | $0.04 + 0.2(0.44) = 0.128000$ |

Step 1 in full: the slope at $x = 0$ is $0 + 0 = 0$, so $y_1 = 0 + 0.2(0) = 0$.
The curve leaves the origin horizontally, which is correct since $y' = x + y$ is
zero at the origin.

Step 2: $y_2 = 0.04$. Step 3: $y_3 = 0.128$.

$$
\boxed{y(0.4) = 0.0400, \qquad y(0.6) = 0.1280 \quad (h = 0.2)}
$$

> [!info] Check against the exact solution
> The equation is linear: $\frac{dy}{dx} - y = x$. A particular solution is
> $y_p = -x - 1$ and the homogeneous solution is $Ce^x$, so
> $$y = Ce^x - x - 1$$
> and $y(0) = 0$ gives $C = 1$:
> $$y = e^x - x - 1$$
> Check: $y' = e^x - 1$ and $x + y = x + e^x - x - 1 = e^x - 1$. They match.
>
> | $x$ | Exact | Euler $h=0.2$ | Error | Euler $h=0.1$ | Error |
> | --: | --: | --: | --: | --: | --: |
> | 0.4 | 0.091825 | 0.040000 | $-0.051825$ | 0.064100 | $-0.027725$ |
> | 0.6 | 0.222119 | 0.128000 | $-0.094119$ | 0.171561 | $-0.050558$ |
>
> Halving the step from $0.2$ to $0.1$ cut the error at $x = 0.4$ from
> $0.0518$ to $0.0277$, a ratio of $1.87$, close to the factor of 2 that
> **first order** accuracy predicts. That confirms both the error direction and
> the order.
>
> **Second order for comparison.** Heun's method from Q.7(a) with $h = 0.2$ gives
> $y(0.4) = 0.088400$ and $y(0.6) = 0.215848$, with errors $-0.0034$ and $-0.0063$.
> That is **15 times** more accurate than Euler at the same step size, for one
> extra slope evaluation per step. This is the practical argument for never using
> plain Euler when the answer matters.

> [!warning] Two things that catch people
> **1. The first step gives $y_1 = 0$, and that is correct.** The slope at the
> origin is $x + y = 0$. A nonzero first step would indicate the function $x - y$
> in place of $x + y$.
>
> **2. Use the old $x$ and the old $y$ in the slope.** The update is
> $y_{n+1} = y_n + h f(x_n, y_n)$, both from step $n$. Computing the slope with
> $x_{n+1}$ or with $y_{n+1}$ mixes in the new point and quietly turns the method
> into something else. Update $y$ first, then $x$, from the saved values.
>
> **Euler always runs low here.** The exact solution is convex,
> $y'' = e^x > 0$, and Euler's method uses a tangent that lies below a convex
> curve, so every iterate under-reads. That is a general property worth
> **Euler under-reads an increasing convex solution.** So an overshoot on such a
> solution points to an arithmetic error, not to a method error.

---

### **(c) Given, $\frac{dy}{dx} = y - x$, where $y(0) = 2$, find $y(0.1)$ and $y(0.2)$ by using Runge-Kutta second order formula. [Marks: 04]**

**Step 1. The method.** For $\frac{dy}{dx} = f(x,y)$ with $y(x_0) = y_0$ and
step $h$, the second-order Runge-Kutta method is

$$
k_1 = h f(x_n, y_n), \qquad k_2 = h f\left(x_n + h, \; y_n + k_1\right), \qquad y_{n+1} = y_n + \frac{1}{2}(k_1 + k_2)
$$

Here $f(x,y) = y - x$ and the paper gives no step size. Two steps are needed to
reach $0.2$, so take $h = 0.1$, which also matches the requested output points.
Start at $x_0 = 0$, $y_0 = 2$.

**Step 2. Step 1: $x_0 = 0$ to $x_1 = 0.1$.**

$$k_1 = 0.1 f(0, 2) = 0.1(2 - 0) = 0.2$$

$$k_2 = 0.1 f(0 + 0.1, \; 2 + 0.2) = 0.1(2.2 - 0.1) = 0.1(2.1) = 0.21$$

$$y_1 = 2 + \frac{0.2 + 0.21}{2} = 2 + 0.205 = 2.205000$$

**Step 3. Step 2: $x_1 = 0.1$ to $x_2 = 0.2$.**

$$k_1 = 0.1 f(0.1, 2.205) = 0.1(2.205 - 0.1) = 0.1(2.105) = 0.2105$$

$$k_2 = 0.1 f(0.1 + 0.1, \; 2.205 + 0.2105) = 0.1(2.4155 - 0.2) = 0.1(2.2155) = 0.22155$$

$$y_2 = 2.205 + \frac{0.2105 + 0.22155}{2} = 2.205 + 0.216025 = 2.421025$$

| Step | $x_n$ | $y_n$ | $k_1$ | $k_2$ | $y_{n+1}$ |
| --: | --: | --: | --: | --: | --: |
| 1 | 0.0 | 2.000000 | 0.200000 | 0.210000 | 2.205000 |
| 2 | 0.1 | 2.205000 | 0.210500 | 0.221550 | 2.421025 |

$$
\boxed{y(0.1) = 2.2050, \qquad y(0.2) = 2.4210 \quad (h = 0.1)}
$$

> [!info] Check against the exact solution
> The equation is $\frac{dy}{dx} - y = -x$. The homogeneous solution is $Ce^x$
> and a particular solution is $y_p = x + 1$, so
> $$y = Ce^x + x + 1$$
> and $y(0) = 2$ gives $C = 1$:
> $$y = e^x + x + 1$$
> Check: $y' = e^x + 1$ and $y - x = e^x + x + 1 - x = e^x + 1$. They match.
>
> | $x$ | Exact $e^x + x + 1$ | RK2 Heun $h=0.1$ | Error |
> | --: | --: | --: | --: |
> | 0.1 | 2.20517092 | 2.20500000 | $-0.000171$ |
> | 0.2 | 2.42140276 | 2.42102500 | $-0.000378$ |
>
> The errors are $-1.7\times10^{-4}$ and $-3.8\times10^{-4}$, which is the right
> size. For a second-order method the global error is
> $\frac{h^3}{6}\lvert y'''\rvert$, and $y''' = e^x$ here, so
> $\frac{0.001}{6}e^{0.1} = 1.84\times10^{-4}$ at $x = 0.1$ and
> $2.04\times10^{-4}$ at $x = 0.2$. The observed errors match that scale.
>
> **RK4 for reference.** $h = 0.1$ gives $y(0.1) = 2.20517083$ and
> $y(0.2) = 2.42140257$, agreeing with the exact solution to $8 \times 10^{-8}$.
> Raising the order improves accuracy: RK4 is correct to eight digits where
> RK2 is right to four, for four function evaluations per step against two.

> [!note] The other second-order method gives a different fourth digit
> "Runge-Kutta second order" is not one formula but a family. The **midpoint**
> method, $k_1 = hf(x_n,y_n)$, $k_2 = hf(x_n + h/2, y_n + k_1/2)$,
> $y_{n+1} = y_n + k_2$, gives the **same** first step, $2.205000$, because at
> $x_0 = 0$ the two happen to coincide, and the same second step, $2.421025$.
>
> The **Ralston** variant, $k_1 = hf(x_n,y_n)$,
> $k_2 = hf(x_n + \frac{2}{3}h, y_n + \frac{2}{3}k_1)$,
> $y_{n+1} = y_n + \frac{1}{3}k_1 + \frac{2}{3}k_2$, gives
> $2.204444$ and $2.419798$, with errors $-7.3 \times 10^{-4}$ and
> $-1.6 \times 10^{-3}$. All three are second order, so all three converge at the
> same rate, but the constants differ and Ralston is about twice as far off here.
>
> **Heun's method is the one to write.** It is the most common textbook choice, it
> is the same method as in Q.7(a), and here it is the most accurate of the three.
> Never mix two second-order formulas in one answer, and never average three
> different RK2 answers hoping to land near the right one.

> [!warning] Three traps
> **1. No step size is printed.** Two output points with a second-order method
> means two steps, so $h = 0.1$ is the natural reading, and it happens to match
> the requested values. If a different $h$ were intended, RK2 with $h = 0.2$ would
> give only one value at $x = 0.2$, and RK2 needs the same $h$ used for both
> outputs. **State the choice.**
>
> **2. $f(x,y) = y - x$, not $x - y$.** The two have different solutions entirely.
> Here $f = y - x$, so $f(0, 2) = 2$, and $k_1 = 0.2$. Getting the sign of $x$
> wrong gives a completely different sequence.
>
> **3. Use $y_n + k_1$ in $k_2$, not $y_n$.** The second slope is evaluated at
> the **end** of the step, at the predicted value $y_n + k_1$. Substituting $y_n$
> makes $k_2 = k_1$ and the method collapses to plain Euler, which for this
> equation would give $2.2$ and $2.41$ by a wrong route and a wrong reason. The
> $x$ in the second slope must also be $x_n + h$, not $x_n$.

---

## Question 8

### **(a) Write 4 types of partial differential equations. Discuss briefly the solving process of any of the equations using numerical iterative technique. [Marks: 06]**

A partial differential equation involves partial derivatives with respect to two
or more independent variables. The four classical types depend on the order of
the highest derivatives.

**1. Laplace equation.** No time or reaction term, steady state.

$$\frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} = 0$$

Physical meaning: steady-state heat conduction, electrostatics, incompressible
irrotational flow, torsional rigidity. Boundaries are prescribed values of $u$
on the edges of a region. Solved by Q.8(b) of this paper.

**2. Poisson equation.** Laplace with a source term.

$$\nabla^2 u = -f(x,y)$$

Physical meaning: steady heat conduction with internal heat generation,
electrostatics with a charge density, potential flow with sources. Same boundary
condition type as Laplace. Solved by 2021 Q.6(c).

**3. Wave equation.** Time-dependent, second order in both space and time.

$$\frac{\partial^2 u}{\partial t^2} = c^2\nabla^2 u$$

Physical meaning: vibrating string, sound in air, water waves, electromagnetic
waves. $c$ is the wave speed. Needs an **initial condition** $u(x,0) = f(x)$,
$\frac{\partial u}{\partial t}(x,0) = g(x)$, plus boundary conditions.

**4. Heat equation, or diffusion equation.** Time-dependent, second order in
space, first order in time.

$$\frac{\partial u}{\partial t} = \alpha\nabla^2 u$$

Physical meaning: heat conduction in a solid, diffusion of a solute, spread of an
epidemic. $\alpha = \frac{k}{\rho c}$ is the thermal diffusivity. Needs an
initial condition $u(x,y,0) = f(x,y)$ plus boundary conditions.

**The deciding test.** For a linear second-order PDE
$A u_{xx} + 2B u_{xy} + C u_{yy} + \cdots = 0$, compute the discriminant
$B^2 - AC$:

| Sign of $B^2 - AC$ | Type | Example |
| :-- | :-- | :-- |
| $< 0$ | **Elliptic** | Laplace, Poisson |
| $= 0$ | **Parabolic** | Heat equation |
| $> 0$ | **Hyperbolic** | Wave equation |

**The solved example: the heat equation by an iterative numerical technique.**

$$\frac{\partial u}{\partial t} = \alpha\left(\frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2}\right)$$

**Step 1. Discretise the grid.** Divide the region into a mesh of spacing $h$ in
space and $\Delta t$ in time. The stability condition is the key practical
result:

$$\alpha \frac{\Delta t}{h^2} \le \frac{1}{4} \qquad \text{in two dimensions}$$

**Step 2. Replace the second derivative by its central difference.**

$$\frac{u^{n+1}_{i,j} - u^n_{i,j}}{\Delta t} = \alpha \frac{u^n_{i+1,j} - 2u^n_{i,j} + u^n_{i-1,j}}{h^2}$$

**Step 3. Rearrange into the update formula** with
$\lambda = \frac{\alpha \Delta t}{h^2}$:

$$u^{n+1}_{i,j} = \lambda u^n_{i+1,j} + \lambda u^n_{i-1,j} + \lambda u^n_{i,j+1} + \lambda u^n_{i,j-1} + (1 - 4\lambda)u^n_{i,j}$$

Each new value is a **weighted average of the four neighbours plus the old
centre**. The weights are all non-negative as long as
$\lambda \le \frac{1}{4}$, which is the stability condition.

**Step 4. The explicit scheme above is one choice.** The two alternatives are
the **implicit (backward Euler)** scheme, which writes the same update at time
$n+1$ instead of $n$ and is unconditionally stable but needs a linear solve each
step, and the **Crank-Nicolson** scheme, which averages the explicit and implicit
forms and is second order in time while still unconditionally stable.

**Step 5. March in time.** The scheme is explicit, so each time level follows
directly from the previous one. Start from the initial condition, apply the
boundary values at every level, and step forward until the desired time.

**Why iterative methods are used at all.** The same problem in the Laplace or
Poisson form gives a large linear system at every instant. A finite difference
discretisation of a $100 \times 100$ mesh gives over $10^4$ unknowns, and solving
it directly at every time step is wasteful when the change between steps is
small. The iterative methods trade a little work per step for a much cheaper
step, and for the elliptic case they converge to the steady state directly.

**The iterative method used in this paper.** For an **elliptic** equation, time
does not appear, so instead of marching one marches the **iteration count**.
Replacing each interior node by the average of its four neighbours and repeating
is exactly the **Liebmann method**, and the averaging weights of $\frac{1}{4}$ are
the same as above with $\lambda = \frac{1}{4}$. Q.8(b) works it through.

| | Explicit | Implicit | Crank-Nicolson |
| :-- | :-- | :-- | :-- |
| Stability | Needs $\lambda \le \frac{1}{4}$ | Unconditional | Unconditional |
| Work per step | Very low | Linear solve | Linear solve |
| Order in time | 1 | 1 | 2 |
| When to use | Short runs, small $\lambda$ | Stiff problems | Accuracy needed |

$$
\boxed{\text{Laplace, Poisson, wave, heat; the elliptic pair is solved by repeated averaging of the four neighbours}}
$$

---

### **(b) Solve the equation $\frac{\partial^2 E(x,y)}{\partial x^2} + \frac{\partial^2 E(x,y)}{\partial y^2} = 0$ in the domain of the following figure by Liebmann method. Consider, $\Delta x = \Delta y$. [Marks: 06]**

![Square domain 3x3 finite-difference grid for the Laplace equation with boundary value 1 on the top edge and 0 on the bottom, left and right edges, and four interior nodes E1, E2, E3, E4](diagrams/2020_Q8b_laplace_grid.jpg)
*Figure 2020 Q8(b): square domain with Dirichlet boundary values and four interior nodes for the Laplace equation (Source: Page 2, Q.8(b))*

**Step 1. Set up the grid.** The domain is a square with $\Delta x = \Delta y = h$
and **four interior nodes**. The boundary values are $1$ along the **top** edge
and $0$ along the **bottom, left and right** edges.

```
             1        1        1
        +--------+--------+--------+
        |        |        |        |
     0  |   E4   |   E3   |        |  0
        |        |        |        |
        +--------+--------+--------+
        |        |        |        |
     0  |   E1   |   E2   |        |  0
        |        |        |        |
        +--------+--------+--------+
             0        0        0
```

**Step 2. The Liebmann update.** The five-point formula for Laplace's equation
with equal spacing is

$$E_{i,j} = \frac{1}{4}\left(E_{i-1,j} + E_{i+1,j} + E_{i,j-1} + E_{i,j+1}\right)$$

Each interior node takes the **average of its four neighbours**. The moment a
node's new value is computed, it replaces the old one, which is what makes the
method Liebmann rather than Jacobi.

**Step 3. Write the four update equations**, reading the boundary values off the
figure.

$$E_1 = \frac{1}{4}\left(0 + E_2 + 0 + E_4\right) = \frac{E_2 + E_4}{4}$$

$$E_2 = \frac{1}{4}\left(E_1 + 0 + 0 + E_3\right) = \frac{E_1 + E_3}{4}$$

$$E_3 = \frac{1}{4}\left(E_4 + 0 + E_2 + 1\right) = \frac{E_4 + E_2 + 1}{4}$$

$$E_4 = \frac{1}{4}\left(0 + E_3 + E_1 + 1\right) = \frac{E_3 + E_1 + 1}{4}$$

Each boundary neighbour contributes its known value, which is why the $+1$ appears
in $E_3$ and $E_4$ and nowhere else: those are the two nodes touching the top
edge. **This is the step where the boundary values enter**, and getting the
figure's node labelling wrong puts the $+1$ in the wrong two equations.

**Step 4. Iterate.** Start from $E_1 = E_2 = E_3 = E_4 = 0$ and sweep
$E_1, E_2, E_3, E_4$ in that order, using the newest value available.

| $k$ | $E_1$ | $E_2$ | $E_3$ | $E_4$ |
| --: | --: | --: | --: | --: |
| 0 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| 1 | 0.000000 | 0.000000 | 0.250000 | 0.312500 |
| 2 | 0.078125 | 0.082031 | 0.348633 | 0.356689 |
| 3 | 0.109680 | 0.114578 | 0.367817 | 0.369374 |
| 4 | 0.120988 | 0.122201 | 0.372894 | 0.373471 |
| 5 | 0.123918 | 0.124203 | 0.374418 | 0.374584 |
| 6 | 0.124697 | 0.124779 | 0.374841 | 0.374884 |
| 7 | 0.124916 | 0.124939 | 0.374956 | 0.374968 |
| 8 | 0.124977 | 0.124983 | 0.374988 | 0.374991 |
| 9 | 0.124994 | 0.124995 | 0.374997 | 0.374998 |
| 10 | 0.124998 | 0.124999 | 0.374999 | 0.374999 |

Iteration 1 in full: $E_1 = 0$ since it depends only on the zero boundary and on
other unknowns still at $0$. $E_2 = 0$ likewise. $E_3 = \frac{0 + 0 + 0 + 1}{4} = 0.25$,
then $E_4 = \frac{0 + 0.25 + 0 + 1}{4} = 0.3125$.

**Step 5. Answer.**

$$
\boxed{E_1 = 0.125, \qquad E_2 = 0.125, \qquad E_3 = 0.375, \qquad E_4 = 0.375}
$$

Convergence to four decimal places is reached at **iteration 8**, and by
iteration 10 every value is correct to six decimals.

> [!info] Check by two independent routes
> **Exact solution of the system.** Writing each update as an equation and solving
> all four at once:
> $$\begin{cases} (1)\;\; 4E_1 - E_2 - E_4 = 0 \\ (2)\;\; 4E_2 - E_1 - E_3 = 0 \\ (3)\;\; 4E_3 - E_2 - E_4 = 1 \\ (4)\;\; 4E_4 - E_1 - E_3 = 1\end{cases}$$
> **(1) minus (3)** gives $4E_1 - 4E_3 + 1 = 0$, so
> $$E_3 = E_1 + \frac{1}{4}$$
> **(2) minus (4)** gives $4E_2 - 4E_4 + 1 = 0$, so
> $$E_4 = E_2 + \frac{1}{4}$$
> Now use those in (1) and (2):
> $$\text{(1):}\quad 4E_1 = E_2 + E_4 = 2E_2 + \frac{1}{4} \qquad \text{(2):}\quad 4E_2 = E_1 + E_3 = 2E_1 + \frac{1}{4}$$
> Subtract the second from the first: $4E_1 - 4E_2 = 2E_2 - 2E_1$, so
> $6E_1 = 6E_2$ and $E_1 = E_2$. Then $4E_1 = 2E_1 + \frac{1}{4}$ gives
> $2E_1 = \frac{1}{4}$, so
> $$E_1 = E_2 = \frac{1}{8}, \qquad E_3 = E_4 = \frac{1}{8} + \frac{1}{4} = \frac{3}{8}$$
> These are exact rationals, and Liebmann iteration 10 reproduces them to six
> decimals.
>
> **Direct Gaussian elimination** on the $4 \times 4$ system gives
> $\left(\frac{1}{8}, \frac{1}{8}, \frac{3}{8}, \frac{3}{8}\right)$ as well, and
> all four residuals are exactly zero.
>
> **Structural check.** The boundary data is symmetric top to bottom in the sense
> that it depends only on the row, not the column: every node in the top row of
> the interior sees the same $1$, and every node in the bottom row sees the same
> $0$. So the answer must satisfy $E_1 = E_2$ and $E_3 = E_4$, and it does. The
> top row sits nearer the $1$ edge and is larger, $0.375 > 0.125$, exactly as
> physics demands. **If the computed values had come out $E_1 = E_3$ instead,
> that would signal a labelling error in reading the figure.**

> [!warning] The traps in this question
> **1. The $1$ goes only into $E_3$ and $E_4$.** Only those two nodes touch the
> top edge. Putting the boundary $1$ into all four equations, or forgetting it
> entirely, are the two common errors. Trace each node's four neighbours against
> the figure before writing anything.
>
> **2. The node labelling in the figure.** $E_1$ and $E_2$ are on the **lower**
> row, $E_3$ and $E_4$ on the **upper**, with $E_1, E_2$ on the left and
> $E_3, E_4$ on the right. The usual numbering puts $1, 2$ along the bottom from
> left to right and $3, 4$ along the top, which is what the figure shows, but
> many textbooks number the top row $1, 2$ and the bottom row $3, 4$. The figure,
> not the convention, governs. With this figure the answer has the small values on
> the bottom, while large values on the bottom indicate swapped rows.
>
> **3. Liebmann is not Jacobi.** Liebmann uses each new value immediately, so
> within one sweep $E_2$ uses the $E_1$ just computed in that same sweep. Jacobi
> uses only values from the previous sweep, which converges more slowly. The
> difference is invisible at iteration 1 and grows afterwards, so checking the
> early iterations will not catch the mistake. See 2021 Q.7(b) for a case where
> this exact distinction changes convergence rather than speed.
>
> **A note on "converges to".** Iteration 0 to 1 moves nothing, because the two
> lower nodes depend only on zeros. That is correct behaviour, not a stalled
> calculation. The method is propagating the boundary information inward one
> node layer per sweep, and it takes about $\log_2(4) = 2$ sweeps before the
> interior fills, then refines from there.

---

> [!note] Where this method appears again
> Liebmann is the same averaging as the relaxation step in the Poisson problem of
> 2021 Q.6(c), and the same as the Gauss-Seidel sweeps of Q.4(b) in this paper
> with a different coefficient matrix. The unifying idea runs through the whole
> course: **discretise, turn the equations into a linear system, then solve that
> system by sweeping until it stops changing.** Change the equation and the
> coefficients change; the sweep pattern stays.
