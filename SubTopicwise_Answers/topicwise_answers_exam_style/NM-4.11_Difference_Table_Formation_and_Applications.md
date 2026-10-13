---
title: "NM-4.11 · Difference Table Formation & Applications"
tags:
  - numerical-methods
  - discrete-mathematics
  - topicwise
---


[🏠 Subtopic Index](00_Index.md) | [← Prev: NM-4.10 Gauss Forward / Backward & Stirling's Formulas](NM-4.10_Gauss_Forward_and_Backward_and_Stirlings_Formulas.md) | [Next: NM-5.1 Trapezoidal Rule →](NM-5.1_Trapezoidal_Rule.md)

---

# NM-4.11 · Difference Table Formation & Applications

Every block below is copied from `../answers_exam_style/`, which is the
only place an answer is authored. A number here is the same number, character
for character, as the one it came from.


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

[🏠 Subtopic Index](00_Index.md) | [← Prev: NM-4.10 Gauss Forward / Backward & Stirling's Formulas](NM-4.10_Gauss_Forward_and_Backward_and_Stirlings_Formulas.md) | [Next: NM-5.1 Trapezoidal Rule →](NM-5.1_Trapezoidal_Rule.md)
