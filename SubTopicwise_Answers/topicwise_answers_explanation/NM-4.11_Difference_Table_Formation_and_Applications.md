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

Every block below is copied from `../answers_explanation/`. The reasoning
is written once, in the year-wise file, and is not restated here.


### [2017 Q.5(c)]

**Question.** The population of a town in decennial census were as following table in thousand unit. Estimate the population for the year 1955.

*[Marks: 05]*

**Solution.**

| Year | 1921 | 1931 | 1941 | 1951 | 1961 |
| :---: | :---: | :---: | :---: | :---: | :---: |
| Population (thousands) | 46 | 66 | 81 | 93 | 101 |

**Step 1, set up the forward difference formula.** The tabulation interval is
$h = 10$. Taking $x_0 = 1921$, the target $1955$ corresponds to

$$p = \frac{1955 - 1921}{10} = \frac{34}{10} = 3.4$$

**Step 2, the difference table.**

| | 46 | 66 | 81 | 93 | 101 |
| :-- | :-- | :-- | :-- | :-- | :-- |
| $\Delta$ | | 20 | 15 | 12 | 8 |
| $\Delta^2$ | | | $-5$ | $-3$ | $-4$ |
| $\Delta^3$ | | | 2 | $-1$ |
| $\Delta^4$ | | | | $-3$ |

**Step 3, apply the formula.**

$$y = y_0 + p\Delta y_0 + \frac{p(p-1)}{2}\Delta^2 y_0 + \frac{p(p-1)(p-2)}{6}\Delta^3 y_0 + \frac{p(p-1)(p-2)(p-3)}{24}\Delta^4 y_0$$

Term by term:

$$y_0 = 46$$

$$p\Delta y_0 = 3.4 \times 20 = 68$$

$$\frac{p(p-1)}{2}\Delta^2 y_0 = \frac{(3.4)(2.4)}{2}(-5) = 4.08 \times (-5) = -20.4$$

$$\frac{p(p-1)(p-2)}{6}\Delta^3 y_0 = \frac{(3.4)(2.4)(1.4)}{6}(2) = \frac{11.424}{6} \times 2 = 1.904 \times 2 = 3.808$$

$$\frac{p(p-1)(p-2)(p-3)}{24}\Delta^4 y_0 = \frac{(3.4)(2.4)(1.4)(0.4)}{24}(-3) = \frac{4.5696}{24} \times (-3) = 0.1904 \times (-3) = -0.5712$$

Collecting the five terms:

$$y = 46 + 68 - 20.4 + 3.808 - 0.5712 = 96.8368$$

$$\boxed{\text{Population in 1955} \approx 96.8368 \approx 96.84 \text{ thousand}}$$

> [!warning] The fourth-difference term is the one that gets dropped
> $\Delta^4 y_0 = -3$ looks negligible beside $\Delta y_0 = 20$. It is not. Its
> multiplier is $\dfrac{p(p-1)(p-2)(p-3)}{24} = 0.1904$, and $0.1904 \times (-3)
> = -0.5712$, which moves the answer by more than half a thousand people. The
> test is not "is the difference small" but "is the difference times its
> multiplier small", and those are different questions.
>
> Two slips account for most wrong answers here. Dropping the trailing $3$ from
> the multiplier, giving $0.1904$ where $0.5712$ is wanted, changes the answer
> by $0.3808$. And forgetting the sign: $p - 3 = 0.4$ is positive and
> $\Delta^4 y_0 = -3$ is negative, so the term *subtracts*.

> [!info] Confirming the value two ways
> **Lagrange.** The polynomial through the same five points, evaluated at
> $x = 1955$, gives $96.8368$ exactly. Two different arrangements of the same
> five numbers, arriving at the same value to six figures.
>
> **Physical.** The census rises from $93$ to $101$ over $1951$–$1961$, so
> linear interpolation alone gives $93 + 0.4(8) = 96.2$. The difference-form
> answer $96.8368$ sits *above* that, and it must: the second differences are
> all negative, so the population curve is concave, and a concave curve lies
> above its chords. Note what this says physically, because it is the opposite
> of the intuitive reading. The census is still *gaining* people faster than
> before in absolute terms, 20, 15, 12, 8 per decade is a falling *increment*,
> but the percentage growth rate $20/46$, $15/66$, $12/81$, $8/93$ is falling
> much faster, and a concave curve on this data means deceleration in
> proportional terms while the absolute increase remains substantial. Reporting
> $96.8$ as "slightly below the midpoint" would be reading the shape backwards.

---

### [2020 Q.3(b)]

**Question.** The population of a town in the decennial census was as given below. Estimate the population for the year (i) 1895 and (ii) 1925.

*[Marks: 04]*

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

*[Marks: 05, CO: 2]*

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

### [2024 Q.3(b)]

**Question.** The population of a town in decennial census were as in the following table in thousand units. Estimate the population for the year 1995.

*[Marks: 04, CO: 1]*

**Solution.**

**The setup.** A census table is equally spaced with $h = 10$, so the difference
methods apply. But note where the target sits: the table ends at 1961 and the
question asks for **1995**, which is outside the data. That single fact decides
the whole method.

**Step 1. Build the difference table.** Take $h = 10$ years and put the years in
steps from 1921, so $u = (x - 1921)/10$ gives $u = 0, 1, 2, 3, 4$.

| $u$ | 0 | 1 | 2 | 3 | 4 |
| --- | --: | --: | --: | --: | --: |
| $y$ | 46 | 66 | 81 | 93 | 101 |
| $\Delta y$ | 20 | 15 | 12 | 8 | |
| $\Delta^2 y$ | $-5$ | $-3$ | $-4$ | | |
| $\Delta^3 y$ | 2 | $-1$ | | | |
| $\Delta^4 y$ | $-3$ | | | | |

The first differences fall steadily, which means the increments are getting
smaller and the population is decelerating.

**Step 2. Choose backward, not forward.** Because 1995 lies beyond the table,
work from the last point, 1961, and use **backward** differences. Those are the
last entry of each row:

$$
\nabla y = 8, \quad \nabla^2 y = -4, \quad \nabla^3 y = -1, \quad \nabla^4 y = -3
$$

**Step 3. The argument.** With $p$ measured in steps of $h$ past the last point,

$$
p = \frac{1995 - 1961}{10} = 3.4
$$

> [!warning] The trap: this is an extrapolation, and the argument must match
> Forward differences want $p = \frac{1995 - 1921}{10} = 7.4$, which is past the
> far end of the table; backward differences want $p = 3.4$ measured from 1961.
> Both are legitimate, but they are different expansions of the *same* polynomial,
> so they agree only if the difference order is matched to the end you start from.
>
> **Read the target year against the table before choosing.** A target inside the
> table wants forward differences from the left; a target past the right end wants
> backward differences from the right. Choosing forward differences and then
> reading $p$ from 1961 is the mismatch that produces a wrong answer with no
> visible symptom.

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

**Is this sensible?** A sanity check matters more here than usual, because the
answer is small when a large number would have been the giveaway. The increments
were $20, 15, 12, 8$, the last of them only $8$ thousand per decade. Extrapolating
$3.4$ decades past 1961 on a degree 4 polynomial that has been decelerating for
two decades gives a *decrease* to $20.19$ thousand. That is the polynomial's
answer and it is arithmetically correct, but it is not a plausible prediction: a
linear reading of the last increment alone gives $101 + 3.4(8) = 128.2$.

> [!warning] Why a correct extrapolation can still be wrong
> This is the cleanest example in the paper of a number that is exactly right and
> practically meaningless. The degree 4 interpolating polynomial through five
> points is unique, and evaluating it at 1995 has one answer, $20.1888$. But
> nothing in the data constrains the polynomial beyond 1961, and the extrapolation
> error grows fast: the $\nabla^4$ term alone contributes $-64.6$, which is three
> times the size of the answer.
>
> **The general lesson.** Extrapolate only about one interval beyond the data, and
> even then say that it is an extrapolation. Here the target is $3.4$ intervals
> past the last point, far outside the range where any polynomial can be trusted.
> The responsible engineering answer would be to fit a saturation model, not to
> report $20.19$ thousand as a population.

**Route 2, as a check.** Newton forward from 1921 with $p = 7.4$ gives
$20.1888000000$, matching to nine figures. Lagrange on the five points gives
$20.1887999999$. Both agree with the backward-difference value because all three
evaluate the same unique degree 4 polynomial, so this confirms the arithmetic but
not the modelling. Confirming that a computation is right and confirming that it
answers the question are two different things.

---

[🏠 Subtopic Index](00_Index.md) | [← Prev: NM-4.10 Gauss Forward / Backward & Stirling's Formulas](NM-4.10_Gauss_Forward_and_Backward_and_Stirlings_Formulas.md) | [Next: NM-5.1 Trapezoidal Rule →](NM-5.1_Trapezoidal_Rule.md)
