---
title: "ECE 2213 · 2024 Explanations"
tags:
  - numerical-methods
  - discrete-mathematics
  - previous-year
---

# ECE 2213: 2024 Semester Final · Explained

**RUET · ECE Dept · B.Sc. Engineering 2nd Year Even Semester Examination, 2024**

This file explains the same questions as
[[2024_answer|the 2024 answer script]], written to be read
rather than copied. Every step is named, the reason a formula is chosen is
stated, and the traps that catch people are called out.

> [!info] How to use this file
> Read this to understand *why* the answer script does what it does. When you
> are ready to write in the hall, work from
> [[2024_answer|the exam-style file]], which is shorter and
> carries no commentary.
>
> **The rule that matters.** Every boxed number here is the same number as the
> one in the answer script, character for character. Gate V5 checks this. If the
> answer script says `1.6458333`, so does this file.

---

# SECTION A

## Question 1

### **(a) Explain the importance of mathematical modeling in engineering problem solving; provide examples of how a real-world engineering problem can be represented using mathematical models.**

*[Marks: 03, CO: 1]*

Engineering problems are too large to test directly. A model is a set of
equations that captures the behaviour that matters and drops the rest. That last
clause is the whole idea, and it is worth being precise about: a model is not a
copy of reality, it is a deliberate simplification of it. Choosing what to leave
out is the engineering judgement, and the choice is what a modelling question is
really testing.

**Why it matters.** Four reasons, in the order they tend to be asked:

1. **A real system cannot be tested directly.** A bridge cannot be built to see
   whether it falls down. A satellite cannot be launched to check the antenna
   gain. The model can be run as many times as needed, which is the only way the
   question "does this design survive X" gets asked before the design exists.
2. **Trials on the model are almost free.** One run costs nothing compared with
   one prototype. When a trial costs nothing, you run thousands of them, and
   thousands of trials is what tells you which parameter actually matters.
3. **The model identifies the driving quantity.** With a model you can vary one
   input and hold the rest, which is exactly what an experiment cannot do.
   Finding that the answer depends on $\tau$ and not on $R$ is worth a great deal
   before any hardware is chosen.
4. **It gives numbers before the hardware exists.** A budget is a set of numbers.
   So is a specification. Both need the model first.

**How a problem becomes a model.** The five steps are the standard ones, and
they are worth learning as a sequence because the question can be asked in the
form "describe the modelling process":

1. List the quantities of interest, with a symbol and a unit for each.
2. Write the physics or the statistics that relates them.
3. State the simplifications accepted. A model is wrong somewhere by design,
   and saying where is part of the answer.
4. Fix the input data and solve.
5. Compare the answer against a measurement already trusted, and correct the
   model if it is off.

**The worked example.** The answer script uses a thermocouple on a reactor
coolant loop. The thermocouple is slow, and the model is a first-order lag:

$$T_n = T_{n-1} + (T_\infty - T_{n-1})e^{-\Delta t/\tau}$$

with $\tau$ the sensor time constant. The reason this model is chosen is that
first-order lag is the standard description of any sensor whose response is
limited by a single energy or charge storage. For $\Delta t \ll \tau$ the
exponential reduces to a linear update, which is the form that can actually be
implemented in a loop running every second.

$$\boxed{\text{Model} = \text{physics written as equations, with stated limits}}$$

> [!note] What the marker is looking for
> Three marks divide naturally into three things: a definition, the reasons, and
> an example. The example needs to be concrete, with symbols and units. A common
> loss of marks is giving the reasons as a list of adjectives rather than as
> statements about what a model lets you do that an experiment does not.

---

### **(b) Given the function $f(x) = e^x$, derive the third order Taylor series expansion around $x = 0$. Estimate the truncation error if you use this expansion to approximate $f(0.5)$.**

*[Marks: 03, CO: 1]*

**The setup.** The Taylor series of $f$ about $x_0$ is

$$f(x) = \sum_{n=0}^{\infty}\frac{f^{(n)}(x_0)}{n!}(x - x_0)^n$$

For $f(x) = e^x$ about $x_0 = 0$, every derivative is $e^x$, and evaluated at
zero every derivative is $1$. This is why $e^x$ is the standard worked example:
the derivative never changes, so the series is simply

$$e^x = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \frac{x^4}{4!} + \cdots$$

**Third order means keeping terms up to $n = 3$.**

$$\boxed{e^x \approx P_3(x) = 1 + x + \frac{x^2}{2} + \frac{x^3}{6}}$$

At $x = 0.5$:

$$P_3(0.5) = 1 + 0.5 + \frac{0.25}{2} + \frac{0.125}{6} = 1 + 0.5 + 0.125 + 0.0208333 = 1.6458333$$

**The truncation error.** Taylor's theorem gives the exact remainder

$$R_n = \frac{f^{(n+1)}(\xi)}{(n+1)!}(x - x_0)^{n+1}$$

for some $\xi$ between $x_0$ and $x$. Here $n = 3$, so

$$R_3 = \frac{e^{\xi}}{4!}(0.5)^4 = \frac{e^{\xi}}{24}(0.0625) = e^{\xi} \times 0.0026042$$

To **bound** this, take the largest $e^\xi$ can be on the interval, which is at
$\xi = 0.5$:

$$|R_3| \le \frac{e^{0.5}}{24}(0.5)^4 = \frac{1.6487213}{24}(0.0625) = 0.0042935$$

$$\boxed{P_3(0.5) = 1.6458333, \qquad |E_3| = 0.0028879 \le 0.0042935}$$

**Why the bound and the actual differ.** The bound $0.0042935$ uses $e^\xi$ at
its worst, $\xi = 0.5$. The *actual* error is

$$|e^{0.5} - P_3(0.5)| = 1.6487213 - 1.6458333 = 0.0028879$$

which is about two thirds of the bound. The first neglected term alone is

$$\frac{(0.5)^4}{4!} = \frac{0.0625}{24} = 0.0026042$$

which is already $90\%$ of the actual error. This is the useful practical fact
about alternating-free Taylor series: **the first neglected term tells you the
size of the error**. For $e^x$ with positive $x$ the terms are all positive, so
the first neglected term is a lower bound on the error rather than an estimate
of it, and the ratio of consecutive terms tells you how many more terms you
would need.

> [!warning] The trap: which $x$ goes in the remainder
> The remainder carries $(x - x_0)^{n+1}$, evaluated at the point where you are
> approximating, that is $x = 0.5$, not at the expansion point. Writing
> $(0.5 - 0)^4$ and writing $(0.5)^4$ are the same thing, but writing
> $(0.5 - x_0)$ where $x_0 = 0$ and then forgetting the minus is the classic
> slip. Equally common is bounding $e^\xi$ by $e^0 = 1$, which is the *smallest*
> value on the interval, not the largest.

---

### **(c) What are round off and truncation errors? Discuss how each arises in numerical computation.**

*[Marks: 04, CO: 2]*

**Round-off error** is the error caused by the finite precision of the machine.
A computer holding $t$ significant digits cannot represent most numbers
exactly, so every arithmetic operation rounds its result to the $t$ digits
available. That rounding, introduced at one step, propagates into every later
step.

It arises in three distinct ways, and naming the type is usually what the marks
are for:

- **Representation error**, the error in storing a number at all. $1/3$ stored
  in six digits is $0.333333$, and the error is already there before anything is
  computed.
- **Arithmetic rounding**, the error in the result of an operation. Adding two
  $t$-digit numbers can require $t+1$ digits, so the last is dropped.
- **Absorption**, when a small number is added to a large one and vanishes.
  Adding $10^{-7}$ to $10^{6}$ on a six-digit machine leaves $10^6$ unchanged;
  the small number has been absorbed without effect.

**Truncation error** is the error caused by replacing an infinite process by a
finite one. It is not a property of the machine at all: it would be present even
with infinite precision, because it comes from the method.

It arises in three ways too:

- **Cutting a series**, as with the Taylor series in part (b), where keeping $n$
  terms discards the remainder.
- **Stepping a differential equation**, as with Euler, where advancing by a finite
  $h$ discards the $O(h^2)$ and higher terms.
- **Subdividing an integral**, as with Simpson's rule, where a finite number of
  panels approximates a continuous curve.

**The opposition between them.** This is the part of the answer that
distinguishes a good response from a listing. The two errors behave differently
as a method is refined:

- Truncation error **falls** as the number of terms, panels or steps is
  increased.
- Round-off error **grows**, because more terms means more operations, and each
  operation adds its own rounding.

So the total error has a minimum at some optimal refinement level, below which
making the method finer makes the answer **worse**. This is why the answer to
"how accurately can this integral be computed" is not always "use more panels".

**Why it matters in practice.** The stability of the method, not the precision
of the machine, decides whether round-off is amplified or damped. A method is
**well-conditioned** if an error introduced early is damped in later steps, and
**unstable** if it is amplified. The same machine precision can give six correct
digits on one method and none on another.

$$\boxed{\text{Total error} = \text{truncation} + \text{round off} + \text{data error}}$$

Note the three terms, not two. **Data error** is the error already present in the
inputs, and it is not reduced by choosing a better method. A method can drive
truncation and round off down indefinitely; data error only comes down by
measuring more carefully. The three do not always add, since a truncation error
and a round-off error can partly cancel, so the practical statement is a bound
rather than an equality. The box writes the standard decomposition, which is what
an exam expects.

> [!info] Check by an independent route: the sum of $e^{-5}$ two ways
> The cleanest demonstration that the two errors are distinct is 2017 Q.1(c).
> Evaluating $e^{-5}$ as the alternating series $1 - 5 + 25/2! - \cdots$ is
> mathematically exact and numerically hopeless, because the terms reach $26$
> while the answer is $0.0067$. The truncation error goes to zero as terms are
> added, while the round-off error from the cancellation that precedes it grows
> without bound. Recasting the same computation as $1/e^5$ removes the
> cancellation entirely, and the answer then converges monotonically. The method
> changed, the arithmetic precision did not, and only the round-off error moved.
> That is the separation the definition is describing.

---

## Question 2

### **(a) Given the polynomial $f(x) = x^3 - 6x^2 + 11x - 6$, use the bisection (bracketing) method to find a root in the interval up to two iterations.**

*[Marks: 03, CO: 2]*

**The setup.** The question gives no interval, so the first task is to find one.
Bisection needs $f$ to change sign across the interval, so scan for a sign
change before iterating.

$$f(x) = x^3 - 6x^2 + 11x - 6$$

| $x$ | $f(x)$ |
| :--: | :--: |
| 2.5 | $-0.375$ |
| 3.4 | $+1.344$ |

**The three roots are exactly $1, 2, 3$.** This is worth checking at the outset,
because it is the fastest possible verification of everything that follows:

$$x^3 - 6x^2 + 11x - 6 = (x-1)(x-2)(x-3)$$

Any bisection result must converge to one of these three values. A result that
converges elsewhere is wrong, and this is the check to apply before accepting
any number of iterations.

**Choosing the interval.** Take $[2.5, 3.4]$, which brackets $x = 3$ without
landing on it, so each iteration narrows the bracket:

$$
f(2.5) = 15.625 - 37.5 + 27.5 - 6 = -0.375, \qquad f(3.4) = 39.304 - 69.36 + 37.4 - 6 = +1.344
$$

$f(2.5) \cdot f(3.4) = -0.504 < 0$, so a root lies in $(2.5, 3.4)$.

> [!warning] Do not bisect on $[1, 2]$ or $[2, 3]$
> The three roots are $1$, $2$ and $3$, so the intervals between consecutive roots
> look attractive. They are the worst possible choice: $f(1) = f(2) = f(3) = 0$,
> so both endpoints of $[1, 2]$ are already roots and there is no sign change to
> narrow. A midpoint test on such an interval is meaningless, because no
> sub-interval of it has endpoints of opposite sign.
>
> **Pick an interval that contains one root strictly inside it.** $[2.5, 3.4]$
> does, and its endpoints are not roots, which is the second thing to check after
> the sign change.

**Iteration 1.** Midpoint $x_1 = (2.5 + 3.4)/2 = 2.95$

$$
f(2.95) = 25.6724 - 52.2150 + 32.45 - 6 = -0.092625
$$

$f(2.95) < 0$, the same sign as $f(2.5)$, so the root is in $(2.95, 3.4)$.

**Iteration 2.** Midpoint $x_2 = (2.95 + 3.4)/2 = 3.175$

$$
f(3.175) = 32.005984 - 60.483750 + 34.925 - 6 = +0.447234
$$

$f(3.175) > 0$, so the root is in $(2.95, 3.175)$.

| Iteration | $a$ | $b$ | midpoint | $f(\text{midpoint})$ | retained |
| :--: | --: | --: | --: | --: | :--: |
| 1 | 2.5 | 3.4 | 2.95 | $-0.092625$ | $(2.95, 3.4)$ |
| 2 | 2.95 | 3.4 | 3.175 | $+0.447234$ | $(2.95, 3.175)$ |

$$\boxed{x_2 = 3.175, \qquad \text{root} \in (2.95,\ 3.175), \qquad \text{true root} = 3}$$

The interval halves each time, so after $n$ iterations its width is
$\dfrac{b-a}{2^n}$, and the answer is known to lie inside it. This is the
feature that makes bisection valuable despite being slow: **the error is
bounded at every step**, whether or not the iteration has converged.

**Why bisection is chosen here.** The marks are for the method, not for the
algebra, so the polynomial's factoring is the check rather than the answer. The
question is asking for the bracketing procedure, and the demonstration of it
requires a valid bracket, which requires finding a sign change.

**Convergence rate.** Bisection is first order: halving the interval halves the
error, so gaining one decimal place costs about $3.3$ iterations. Compare
Newton–Raphson at second order, where the number of correct digits roughly
doubles per step. The trade is reliability for speed.

> [!warning] The trap: a repeated root
> If the interval is chosen so that a root sits exactly at an endpoint, the
> bisection test $f(a)f(c) < 0$ will select the wrong half on the first step,
> because one factor is zero rather than negative. The standard fix is to check
> $f(c) = 0$ separately before testing the sign, which is what a correct
> algorithm does. Without it, a root at an endpoint is lost.

---

### **(b) Solve $I_1$, $I_2$ and $I_3$ using the Gauss-Seidel method.**

*[Marks: 04, CO: 1]*

![Planar three-mesh DC resistive network with a 500 V source, 10, 20 and 100 ohm resistors, and a 5 A source, with clockwise mesh currents I1, I2 and I3](../answers_exam_style/diagrams/2024_Q2b_circuit.jpg)
*Figure Q2(b): Three-mesh DC resistive circuit with independent voltage and current sources (Source: Page 1, Q2(b))*

Gauss-Seidel solves a linear system by solving each equation for its own unknown
and immediately using every new value as soon as it is computed. The word
"immediately" is the whole method, and it is the difference from Jacobi.

**Jacobi versus Gauss-Seidel.** In Jacobi, the whole right-hand side is computed
from the previous sweep's values, and only then is the new sweep adopted. In
Gauss-Seidel, the $k$-th unknown is computed using $I_1$ through $I_{k-1}$ from
the *current* sweep and $I_{k+1}$ through $I_n$ from the previous one. Because
the new values are always at least as good as the old ones, Gauss-Seidel
converges in fewer sweeps than Jacobi on the same system, typically by a factor
of about two.

**The convergence condition.** Gauss-Seidel is guaranteed to converge when the
coefficient matrix is **strictly diagonally dominant**, meaning

$$|a_{ii}| > \sum_{j \ne i} |a_{ij}|$$

for every row. If the matrix is not diagonally dominant, convergence is possible
but not guaranteed, and checking this before iterating is the first step of the
answer. Where the matrix is not dominant in the given order, rearranging the
equations may make it so, and that rearrangement should be stated.

**Why the method is used on circuits.** Mesh and nodal analysis of a network with
more than two unknowns gives a linear system whose coefficients are the
conductances. Those systems are sparse and usually diagonally dominant, both of
which suit Gauss-Seidel. The method also has a practical advantage: if a
parameter changes, you restart from the previous solution rather than from zero,
and the iteration converges in a few sweeps.

**The general iteration.** Writing the system as $\sum_j a_{ij}I_j = b_i$ and
solving equation $i$ for $I_i$:

$$I_i^{(k+1)} = \frac{1}{a_{ii}}\left(b_i - \sum_{j < i}a_{ij}I_j^{(k+1)} - \sum_{j > i}a_{ij}I_j^{(k)}\right)$$

**The circuit.** Three meshes, all clockwise: a $500$ V source in mesh 1, a
$5$ A current source bounding mesh 3, and resistors $10$, $20$ and $100\ \Omega$.

**The mesh equations.**

- Mesh 1: the source opposes the current, the $10\ \Omega$ and $20\ \Omega$ carry
  $I_1$, and the $20\ \Omega$ is shared with mesh 2:
  $-500 + 10I_1 + 20(I_1 - I_2) = 0$
- Mesh 2: the $20\ \Omega$ and the $100\ \Omega$ are both shared:
  $20(I_2 - I_1) + 100(I_2 - I_3) = 0$
- Mesh 3: the right branch holds only the $5$ A source, aligned with $I_3$, so
  $I_3 = 5$

$$
\begin{cases}
30I_1 - 20I_2 = 500 \\
-20I_1 + 120I_2 - 100I_3 = 0 \\
I_3 = 5
\end{cases}
$$

**Rearrange each equation for its own unknown.**

$$
I_1 = \frac{500 + 20I_2}{30}, \qquad
I_2 = \frac{20I_1 + 100I_3}{120}, \qquad
I_3 = 5
$$

> [!warning] $I_3$ is not iterated
> Mesh 3 is bounded on the right by an ideal current source, so the branch current
> is fixed and $I_3 = 5$ from the first row of the table. It is **not** an unknown
> that starts at zero and converges. Treating $I_3$ as an unknown to be swept is
> the standard error on this circuit, and it corrupts the first sweep of $I_2$,
> whose numerator carries $100I_3$.

**The sweeps.** Start from $I_1^{(0)} = I_2^{(0)} = 0$, with $I_3 = 5$ throughout.

| Iteration | $I_1$ | $I_2$ | $I_3$ |
| ---: | ---: | ---: | ---: |
| 0 | 0 | 0 | 5.000000 |
| 1 | 16.666667 | 6.944444 | 5.000000 |
| 2 | 21.296296 | 7.716049 | 5.000000 |
| 3 | 21.810700 | 7.801783 | 5.000000 |
| 4 | 21.867856 | 7.811309 | 5.000000 |
| 5 | 21.874206 | 7.812368 | 5.000000 |
| 6 | 21.874912 | 7.812485 | 5.000000 |

Sweep 1 in full:

$$
I_1^{(1)} = \frac{500 + 20(0)}{30} = \frac{50}{3} = 16.666667
$$

$$
I_2^{(1)} = \frac{20(16.666667) + 100(5)}{120} = \frac{333.33334 + 500}{120} = \frac{125}{18} = 6.944444
$$

$$\boxed{I_1 \approx 21.875 \text{ A}, \quad I_2 \approx 7.8125 \text{ A}, \quad I_3 = 5 \text{ A}}$$

**The convergence test, applied here.** Row 1 has $|30|$ against $20$, so it is
dominant. Row 2 has $|120|$ against $20 + 100 = 120$, which is **equal**, not
strictly greater. So the matrix is not *strictly* diagonally dominant, and strict
dominance is not available as the justification. The iteration converges anyway,
because the off-diagonal coupling is weak in one direction and the two equations
pull towards the solution rather than away from it. Stating the near-equality is
more accurate than claiming dominance, and it costs nothing.

> [!info] Confirming by direct elimination
> Substitute $I_3 = 5$ and solve the two-equation system directly:
> $30I_1 - 20I_2 = 500$ and $-20I_1 + 120I_2 = 500$. Eliminating $I_1$ gives
> $160I_1 = 3500$, so $I_1 = \frac{175}{8} = 21.875$. Back substitution gives
> $I_2 = \frac{125}{16} = 7.8125$. Both match the iterated values.
>
> This is the check worth doing on any Gauss-Seidel answer, and it costs one line:
> an iterative method has no residual to inspect at the end, so the direct solve
> is the only independent confirmation available.
>
> **Check on the iteration.** The increments shrink by a factor near 4 each sweep,
> so by sweep 6 the sequence has settled to six figures. Note also that
> $21.874912$ at sweep 6 is still short of $21.875$ exactly; that is the method
> converging, not an error, and reporting $\approx$ is the honest form.

> [!note] What to show in the hall
> The marks are for the recursion, the convergence test, and at least two sweeps.
> Write out each sweep explicitly with the substitutions shown, because a table of
> numbers with no working gets no credit. Deal with the current source first, so
> the mesh it bounds never appears as an iterated unknown. Then state the
> diagonal dominance that justifies the iteration, or say plainly that it is not
> strictly available. Finish by checking the result in the original equations.

---

### **(c) Describe the Lagrange interpolation method. What are its advantages and disadvantages?**

*[Marks: 03, CO: 1]*

**The method.** Given $n+1$ points $(x_i, y_i)$, the unique polynomial of
degree at most $n$ through them is

$$\boxed{P_n(x) = \sum_{i=0}^{n} y_i \prod_{j \neq i} \frac{x - x_j}{x_i - x_j}}$$

Each $y_i$ is multiplied by a **basis polynomial** $L_i(x)$ that equals $1$ at
$x = x_i$ and $0$ at every other tabulated $x_j$. That construction is what
guarantees the interpolant passes through every point: at $x = x_k$, every term
except the $k$-th vanishes.

**The error.** With $n+1$ points,

$$f(x) - P_n(x) = \frac{f^{(n+1)}(\xi)}{(n+1)!}\prod_{i=0}^{n}(x - x_i)$$

for some $\xi$ in the interval. The product is zero at every node, so the error
is zero there, and it grows between nodes. This is why interpolation error is
not uniformly distributed across the interval.

**Advantages.**

1. **Equal spacing is not required.** This is the decisive advantage over
   Newton's formulas, which assume a constant tabular spacing $h$. Experimental
   data with irregular spacing are handled directly.
2. **The order of the points is irrelevant.** The formula is symmetric in the
   nodes, so a table printed with its entries out of order gives the same
   polynomial. This is useful when a printed table is disordered.
3. **The formula is written once.** A single expression evaluates at any $x$ in
   range, with no difference table to construct, and it is convenient for
   hand checking.

**Disadvantages.**

1. **Adding a point costs everything.** Every basis polynomial changes, so a new
   point forces a complete recomputation. Newton's divided-difference form keeps
   its earlier work, so appending a point costs one new column.
2. **It is inefficient for repeated evaluation.** Evaluating the product for
   every new $x$ costs $O(n^2)$ multiplications, whereas converting to power
   form once costs $O(n^2)$ and then gives $O(n)$ per evaluation.
3. **It cannot show the trend.** The formula gives a value, not a model. Fitting
   a line and reporting the slope is a different task, and interpolation does not
   answer it.

**When to use it.** Lagrangian interpolation is the right choice when the data
are exact, unevenly spaced, and evaluated at few points. For many points, or
when a model of the trend is wanted, use fitting instead.

---

## Question 3

### **(a) Discuss the operation of curve fitting and interpolation.**

*[Marks: 02, CO: 1]*

Both estimate the value of a function from data, and the difference is whether
the estimated curve is required to pass through the known points.

**Interpolation** constructs a curve through every tabulated point exactly. The
interpolant reproduces the data. It is the right tool when the data are known to
be accurate and the noise is negligible, such as values taken from a table of a
known function or a calibrated instrument.

**Curve fitting** constructs a curve that captures the trend without passing
through the points. The fitted curve does not reproduce the data; it summarises
them. It is the right tool when the data carry measurement error, because
forcing the curve through noisy points reproduces the noise as well as the
signal.

**How the difference shows up.** With five points, interpolating gives a quartic
that passes through all five, including any scatter among them. Fitting a line
to the same five points gives a line that misses all five but shows the
direction. Neither is wrong; they answer different questions.

**The test for which to use.** Ask what the data are: exact tabulated values, or
measurements? Ask what is wanted: the value at an intermediate point, or the
model of the trend? Exact data and an intermediate value gives interpolation.
Measured data and a model gives fitting.

$$\boxed{\text{Interpolation reproduces data; curve fitting explains it}}$$

**The general methods.**

| Method | Curve through points | Best for |
| :-- | :-: | :-- |
| Lagrange interpolation | yes | exact, unevenly spaced data |
| Newton divided differences | yes | exact, equally spaced, points added later |
| Least squares fitting | no | noisy data, a trend model |
| Piecewise (spline) interpolation | yes, locally | many points, avoiding oscillation |

> [!note] Why the exam asks this
> Two marks for a comparison, so the marks are for stating the distinction and
> the test for choosing, not for listing methods. The most common way to lose
> both marks is to describe interpolation in detail and then write "curve fitting
> is similar" without saying what is different.

---

### **(b) The population of a town in decennial census were as in the following table in thousand units. Estimate the population for the year 1995.**

*[Marks: 04, CO: 1]*

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

### **(c) Fit a straight line to the $x$ and $y$ values in the following table.**

*[Marks: 04, CO: 1]*

**The method.** Least squares picks the line $y = a + bx$ that minimises the sum
of squared vertical residuals. Differentiating with respect to $a$ and to $b$ and
setting both to zero gives the two **normal equations**:

$$na + b\sum x = \sum y$$

$$a\sum x + b\sum x^2 = \sum xy$$

These are two linear equations in the two unknowns $a$ and $b$, so they always
have a unique solution (provided the $x$ values are not all identical).

**Sums over the data.**

$$\sum x = 28, \qquad \sum y = 24, \qquad \sum xy = 119.5, \qquad \sum x^2 = 140, \qquad n = 7$$

The $\sum xy$ term is the one to compute carefully, because it is the only one
that is not a simple sum of a column. Its seven products are $0.5, 5, 6, 16,
17.5, 36$ and $38.5$, which add to $119.5$.

**Solve.**

$$7a + 28b = 24$$

$$28a + 140b = 119.5$$

Multiplying the first by $4$ gives $28a + 112b = 96$, and subtracting from the
second:

$$28b = 23.5 \implies b = \frac{23.5}{28} = \frac{47}{56} = 0.839286$$

Substituting back into the first:

$$7a = 24 - 28(0.839286) = 24 - 23.5 = 0.5 \implies a = \frac{0.5}{7} = \frac{1}{14} = 0.071429$$

$$\boxed{y = 0.0714 + 0.8393x}$$

**The centroid check.** The fitted line must pass through the point
$(\bar x, \bar y)$. Here $\bar x = 4$ and $\bar y = 24/7 = 3.4286$, and

$$0.0714 + 0.839286(4) = 0.0714 + 3.3571 = 3.4286$$

which matches. This check costs nothing and catches a transposition between the
two normal equations immediately, because a swapped pair of equations gives a
line that misses $\bar y$.

**The residuals.**

| $x$ | $y$ | $0.0714 + 0.8393x$ | $e = y - \hat y$ |
| :--: | :-- | :-- | :-- |
| 1 | 0.5 | 0.9107 | $-0.4107$ |
| 2 | 2.5 | 1.7500 | $+0.7500$ |
| 3 | 2.0 | 2.5893 | $-0.5893$ |
| 4 | 4.0 | 3.4286 | $+0.5714$ |
| 5 | 3.5 | 4.2679 | $-0.7679$ |
| 6 | 6.0 | 5.1071 | $+0.8929$ |
| 7 | 5.5 | 5.9464 | $-0.4464$ |

The residuals sum to zero, as the normal equations guarantee, and the sum of
squared residuals is $2.9911$.

**The quality of the fit.** The correlation coefficient is $r = 0.9318$, so
$r^2 = 0.8683$, meaning about $87\%$ of the variation in $y$ is accounted for
by the line. That is a good fit but not a strong one, and the residual table
shows why: the residuals alternate in sign and grow from both ends toward the
middle, which is the signature of a straight line fitted to data with genuine
curvature rather than of an arithmetic slip.

> [!warning] The trap: swapping the normal equations
> The equations are $na + b\sum x = \sum y$ and $a\sum x + b\sum x^2 = \sum xy$.
> Reading the second as $a\sum y + b\sum x^2 = \sum xy$ produces a system that
> still solves and looks entirely plausible, but the answer is wrong. The
> safeguard is the centroid check: a line that does not pass through
> $(\bar x, \bar y)$ has had its equations swapped.

---

## Question 4

### **(a) Describe the general approach for solving boundary value problems numerically. How does it differ from solving initial value problems?**

*[Marks: 03, CO: 1]*

**What a boundary value problem is.** A boundary value problem (BVP) gives
conditions at more than one point of the domain. The standard statement is a
differential equation on $[a, b]$ plus values of $y$ at $a$ and at $b$:

$$y'' = f(x, y, y'), \qquad y(a) = y_a, \qquad y(b) = y_b$$

An initial value problem (IVP) gives both conditions at the same point, usually
the left end, and asks for the solution at later points.

**The general numerical approach.** Three steps, and they are the same for every
BVP method:

1. **Discretise the domain.** Replace $[a, b]$ by a finite set of nodes
   $x_0, x_1, \ldots, x_n$ with spacing $h$. The solution is now sought at the
   nodes only, rather than at every point.
2. **Replace derivatives by finite differences.** Each derivative in the
   equation is replaced by an approximation involving nodal values. For
   $y''$ the standard choice is the central difference

   $$y''_i \approx \frac{y_{i+1} - 2y_i + y_{i-1}}{h^2}$$

   After this step the differential equation has become a linear (or nonlinear)
   **algebraic** equation at each interior node.
3. **Assemble and solve.** Collecting the nodal equations gives one algebraic
   system with $n - 1$ unknowns for $n-1$ interior nodes. The boundary values
   supply the terms that are already known. Solve the system, by elimination or,
   for a large mesh, by an iterative method such as Gauss-Seidel.

**Why the discretisation is sound.** The central difference for $y''$ is
second-order accurate, meaning the error is $O(h^2)$. Taylor expanding
$y(x \pm h)$ and subtracting gives

$$\frac{y_{i+1} - 2y_i + y_{i-1}}{h^2} = y''_i + \frac{h^2}{12}y^{(4)}_i + \cdots$$

so the approximation becomes exact as $h \to 0$, and the method converges.

**How it differs from an initial value problem.** The difference is not cosmetic;
it changes the whole structure of the computation.

| | Initial value problem | Boundary value problem |
| :-- | :-- | :-- |
| Where conditions are given | all at $x = a$ | at both $x = a$ and $x = b$ |
| Shape of the computation | marching, one node at a time | simultaneous, all nodes together |
| Does the solution grow or decay | matters greatly, errors accumulate | irrelevant, solved as a system |
| Method family | Euler, RK4, predictor-corrector | shooting, finite differences, relaxation |
| Can one value be found alone | yes, by marching to it | no, the whole mesh is coupled |

The one-line version: **an IVP can be solved by marching, a BVP cannot.** A BVP
must be solved as a simultaneous system, which is why the numerical linear
algebra of the earlier sections suddenly becomes relevant.

**Shooting, as the alternative.** The shooting method converts the BVP into a
sequence of IVPs: guess the missing initial slope, march forward, compare the
result at $x = b$ against the required value, and correct the guess. It is the
method of choice when the IVP machinery is already reliable and the interval is
long, and it fails when the underlying IVP is unstable, which is common.

> [!note] Why this is worth three marks
> The marks are for the three-step discretise-replace-solve structure and for the
> marching-versus-simultaneous contrast. Writing down the central difference
> formula without saying *why* a system appears gets the first mark only.

---

### **(b) Use the fourth-order Runge-Kutta method (RK4) to solve $\frac{dy}{dx} = x + y$ with initial condition $y(0) = 1$ over the interval $x = 0$ to $x = 0.2$ with a step size $h = 0.1$. Show intermediate calculations.**

*[Marks: 05, CO: 1]*

**Why RK4 rather than Euler.** Euler's method is $O(h)$ globally: halving $h$
halves the error, so six digits costs about a million steps. RK4 is $O(h^4)$
globally: halving $h$ reduces the error by a factor of sixteen. RK4 buys its
accuracy with four evaluations of $f$ per step, and for a smooth right-hand side
that trade is overwhelmingly worth it.

**The method.** Given $y' = f(x, y)$, $y(x_0) = y_0$ and step $h$:

$$k_1 = f(x_n, y_n)$$

$$k_2 = f\left(x_n + \tfrac{h}{2}, y_n + \tfrac{h}{2}k_1\right)$$

$$k_3 = f\left(x_n + \tfrac{h}{2}, y_n + \tfrac{h}{2}k_2\right)$$

$$k_4 = f(x_n + h, y_n + hk_3)$$

$$y_{n+1} = y_n + \frac{h}{6}(k_1 + 2k_2 + 2k_3 + k_4)$$

The four $k$ values are slopes evaluated at the start, two trial midpoints, and a
trial end. The weighted average weights the midpoints double, which is what
makes the fourth-order term cancel.

**Applying it.** With $f(x, y) = x + y$, $y(0) = 1$ and $h = 0.1$:

$$k_1 = 0 + 1 = 1$$

$$k_2 = 0.05 + \left(1 + \tfrac{0.1}{2}\cdot 1\right) = 0.05 + 1.05 = 1.1$$

$$k_3 = 0.05 + \left(1 + \tfrac{0.1}{2}\cdot 1.1\right) = 0.05 + 1.055 = 1.105$$

$$k_4 = 0.1 + \left(1 + 0.1\cdot 1.105\right) = 0.1 + 1.1105 = 1.2105$$

$$y(0.1) = 1 + \frac{0.1}{6}\left(1 + 2(1.1) + 2(1.105) + 1.2105\right) = 1 + \frac{0.1}{6}(6.6205) = 1.1103417$$

**Step 2.** From $x_1 = 0.1$, $y_1 = 1.1103417$:

$$k_1 = 0.1 + 1.1103417 = 1.2103417$$

$$k_2 = 0.15 + \left(1.1103417 + \tfrac{0.1}{2}\cdot 1.2103417\right) = 0.15 + 1.1708587 = 1.3208587$$

$$k_3 = 0.15 + \left(1.1103417 + \tfrac{0.1}{2}\cdot 1.3208587\right) = 0.15 + 1.1763846 = 1.3263846$$

$$k_4 = 0.2 + \left(1.1103417 + 0.1\cdot 1.3263846\right) = 0.2 + 1.2429801 = 1.4429801$$

$$y(0.2) = 1.1103417 + \frac{0.1}{6}\left(1.2103417 + 2(1.3208587) + 2(1.3263846) + 1.4429801\right)$$

$$= 1.1103417 + \frac{0.1}{6}(7.9478085) = 1.1103417 + 0.1324635 = 1.2428051$$

$$\boxed{y(0.2) = 1.2428051}$$

**Checking the answer.** The equation is linear, so it has a closed-form
solution:

$$y' - y = x \implies (ye^{-x})' = xe^{-x} \implies y = Ce^x - x - 1$$

With $y(0) = 1$, $C = 2$, so $y(x) = 2e^x - x - 1$, and

$$y(0.2) = 2(1.2214028) - 0.2 - 1 = 2.4428056 - 1.2 = 1.2428056$$

The RK4 value $1.2428051$ differs from the exact $1.2428056$ by $3.7 \times
10^{-7}$, which over two steps is the expected $O(h^4)$ accuracy.

> [!info] Check by a halved step
> Running the same recursion with $h = 0.05$ over four steps gives
> $y(0.2) = 1.2428054919$, an error of $2.4 \times 10^{-8}$ against the closed
> form. Halving $h$ multiplies the accuracy by sixteen, and the measured ratio is
> $0.3746/0.0244 = 15.4$, close to the predicted 16. That ratio is the check to
> use when no closed form is available: two step sizes whose errors differ by a
> factor near $2^4$ confirms the method is behaving at its designed order.

> [!warning] The trap: reusing $k_2$ where $k_3$ belongs
> The two midpoint slopes are not interchangeable, even though they are computed
> at the same $x$. $k_2$ uses $k_1$ to advance $y$, and $k_3$ uses $k_2$.
>
> There is a second slip in the same three lines, and it is easier to make,
> because both variants produce a tidy number. The trial value is
> $y_n + \tfrac{h}{2}k_1$, that is **add** $\tfrac{h}{2}k_1$ to $y_n$. Writing
> $\left(y_n + \tfrac{h}{2}\right)k_1$ multiplies instead, which turns $1.055$
> into $1.155$ and $1.1105$ into $1.3255$ without any obvious awkwardness. The
> two versions differ only by the placement of a bracket, which is exactly why a
> bracket-level slip survives a read-through.
>
> The safeguard is the halved-step check, since either slip changes the order and
> the error ratio stops being near sixteen.

---

### **(c) State the importance of boundary conditions in solving PDEs numerically.**

*[Marks: 02, CO: 1]*

A partial differential equation on its own has infinitely many solutions. The
boundary conditions are what select one, and this is why they are not an
optional addition to the problem but part of its statement.

**What they do, concretely.** For a problem discretised on a mesh, the boundary
conditions do three jobs:

1. **They fix the unknowns.** A mesh with $N$ interior nodes gives $N$ equations
   from the PDE. The boundary values supply the known terms those equations
   need. Without them the system is under-determined and does not have a unique
   answer.
2. **They make the solution physical.** The Laplace equation $u_{xx} + u_{yy} = 0$
   is satisfied by $u = 0$ and by $u = 100x^3 - 3xy^2$ and by infinitely many
   others. Specifying the potential on the four edges selects the one that
   describes the actual apparatus.
3. **They determine the character of the discretisation.** Whether the boundary
   nodes take part in the difference equations, or are already known, decides
   whether the system is square.

**The two kinds, and why they behave differently.**

| Kind | What is given | Behaviour |
| :-- | :-- | :-- |
| Dirichlet | the value of $u$ itself on the boundary | the boundary nodes are eliminated, the system shrinks |
| Neumann | the normal derivative $\partial u/\partial n$ | a ghost row or one-sided difference is needed, the system grows |

For a Neumann condition the derivative is unknown in terms of nodal values, so
one-sided differences are used, and this is where extra discretisation error
enters. Getting the boundary condition *kind* right is therefore as important as
getting the interior discretisation right.

**Why this matters practically.** Most of the numerical difficulty in a PDE
problem is at the boundary, not in the interior. The interior stencil is uniform
and its error is a clean $O(h^2)$. The boundary treatment is where the order can
drop, where the system can become ill-conditioned, and where the physics of the
problem is actually encoded. A mesh refinement study that improves slowly is
almost always showing boundary error, not interior error.

$$\boxed{\text{PDE} + \text{boundary conditions} = \text{a problem with one unique numerical solution}}$$

The PDE on its own has a whole family of solutions. The boundary conditions are
what select one of them, and they do it by fixing both the solution and the size
of the algebraic system that the discretisation produces, since only the interior
nodes become unknowns.

---

# SECTION B

## Question 5

### **(a) Define propositional logic and explain the difference between a proposition and propositional variable.**

*[Marks: 02, CO: 2]*

**Propositional logic** is the branch of logic that deals with propositions,
which are declarative statements that are either true or false, and with the
connectives that combine them. Unlike first-order logic it does not look inside a
proposition: it treats each one as a single indivisible unit and studies how the
truth values of whole propositions combine.

**A proposition** is a declarative sentence that has a definite truth value.
"Swift is a functional language" is a proposition. So is "The bridge opened."
The two essential requirements are that the sentence is declarative rather than
interrogative or imperative, and that it is unambiguously either true or false.
"Jaffna is a city in the world" is true. "Cairo is the capital of Egypt" is true.
"Are you hungry?" is not a proposition at all, because it is a question and has
no truth value.

**A propositional variable** is a symbol, usually $p, q, r$, that stands for a
proposition. The variable does not have a truth value by itself: it takes the
truth value of the proposition it represents. The propositional variable $p$ in
the formula $p \to q$ is a placeholder; the propositions are the statements
behind $p$ and behind $q$.

**The difference in one sentence.** A proposition is a *statement* with a truth
value; a propositional variable is a *name* for one, whose own truth value
depends on which proposition it names.

| | Proposition | Propositional variable |
| :-- | :-- | :-- |
| What it is | A declarative sentence with a definite truth value | A single letter standing for a proposition |
| Truth value | Has one of its own | Borrows the one it stands for |
| Example | "Cairo is the capital of Egypt" | $p$, standing for that statement |
| Not one | "Close the switch", an imperative with no truth value | |

$$\text{Proposition} = \text{declarative statement with a definite truth value};\ \text{variable} = \text{its symbol}$$

**Why the distinction matters.** It is the reason a truth table can be finite. A
single proposition has two possible truth values, so $n$ propositional variables
need $2^n$ rows to enumerate, which is a finite and complete account. If
propositions were allowed to be compound in arbitrary ways, no finite table
would suffice.

---

### **(b) Given the propositional formula $(p \to q) \land (q \to r)$, determine whether the formula is valid, satisfiable or unsatisfiable.**

*[Marks: 04, CO: 2]*

**The three definitions, because the question needs them.**

- **Valid**: true in *every* row of the truth table. A valid formula is called a
  tautology. Validity means "true for all possible truth values of $p, q, r$".
- **Satisfiable**: true in *at least one* row. A satisfiable formula is not
  necessarily valid; it only needs one witness.
- **Unsatisfiable**: true in *no* row. An unsatisfiable formula is a
  contradiction.

These are not mutually exclusive categories in the order they were asked. Every
valid formula is also satisfiable, because it is true in every row including at
least one. The standard classification of a formula asks whether it is a
tautology, a contradiction, or neither, and then reports satisfiability
separately.

**Building the truth table.** Three variables means $2^3 = 8$ rows.

| $p$ | $q$ | $r$ | $p \to q$ | $q \to r$ | $(p \to q) \land (q \to r)$ |
| :-: | :-: | :-: | :-: | :-: | :-: |
| T | T | T | T | T | **T** |
| T | T | F | T | F | **F** |
| T | F | T | F | T | **F** |
| T | F | F | F | T | **F** |
| F | T | T | T | T | **T** |
| F | T | F | T | F | **F** |
| F | F | T | T | T | **T** |
| F | F | F | T | T | **T** |

**Reading the table.** The formula is true in rows 1, 5, 7 and 8, and false in
rows 2, 3, 4 and 6.

$$\boxed{\text{Satisfiable but not valid}}$$

The formula is **not valid**, because there are rows where it is false. It is
**satisfiable**, because there are rows where it is true. It is **not
unsatisfiable**, for the same reason.

**The reasoning behind the result, stated in English.** $p \to q$ says that $p$
being true requires $q$ to be true. $q \to r$ says $q$ requires $r$. Together
they say the chain $p$ then $q$ then $r$ is consistent, which is exactly the
hypothetical syllogism. The formula fails precisely when $p$ and $q$ are both
true but $r$ is false: then $p \to q$ holds and $q \to r$ fails. That row is the
counterexample to validity, and it is the one to name in an answer.

> [!warning] The trap: assuming a true implication is a true conjunction
> $p \to q$ is true in three of four rows, so it is "almost always true". Two of
> them conjoined are true only in four of eight rows, not six. Conjunction
> requires both parts, so the result is false whenever either implication is
> false. The common slip is to reason "successful thesis contains hypothesis,
> successful thesis contains conclusion, therefore the combined formula is
> successful" which conflates *each part being often true* with *both parts being
> true together*.

---

### **(c) Are these system specifications consistent?**

*[Marks: 04, CO: 2]*

> The system is in multiuser state if and only if it is operating normally, the
> kernel is functioning. The kernel is not functioning or the system is in
> interrupt mode. If the system is not in multiuser state, then it is in
> interrupt mode. The system is not in interrupt mode.

**What consistency means.** A set of specifications is consistent when at least
one assignment of truth values makes all of them true at the same time. The
object being tested is the **conjunction** of the four, not each one on its own.
Four individually plausible sentences can easily be jointly impossible.

**Assign variables.** One symbol per simple statement:

| Symbol | Meaning |
| :-- | :-- |
| $p$ | system is in multiuser state |
| $q$ | kernel is functioning |
| $r$ | system is in interrupt mode |

**Translate.** The four sentences become

| # | English | Logic |
| :-: | :-- | :-- |
| 1 | multiuser if and only if the kernel is functioning | $p \leftrightarrow q$ |
| 2 | kernel not functioning, or interrupt mode | $\neg q \lor r$ |
| 3 | if not multiuser, then interrupt mode | $\neg p \to r$, equivalent to $p \lor r$ |
| 4 | not in interrupt mode | $\neg r$ |

Two of these translations need care. Sentence 3 is a conditional whose
consequent is $r$, so $\neg p \to r$ is equivalent to $p \lor r$ by the
definition of implication, and writing it as $p \lor r$ makes the truth table
easier to read. Sentence 2 is a disjunction, so it is true whenever the kernel
is broken *or* interrupt mode holds; the mistake is to read it as a conjunction.

**Test all eight assignments.** Three variables, so $2^3 = 8$ rows.

| $p$ | $q$ | $r$ | (1) $p \leftrightarrow q$ | (2) $\neg q \lor r$ | (3) $p \lor r$ | (4) $\neg r$ | all four |
| :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| F | F | F | T | T | F | T | **F** |
| F | F | T | T | T | T | F | F |
| F | T | F | F | F | F | T | F |
| F | T | T | F | T | T | F | F |
| T | F | F | F | T | T | T | **F** |
| T | F | T | F | T | T | F | F |
| T | T | F | T | F | F | T | F |
| T | T | T | T | T | T | F | F |

No row satisfies all four, so the set is inconsistent.

**Reason without a table.** This is faster and worth writing alongside, since it
shows *where* the conflict is. Sentence 4 forces $r = \mathrm{F}$. Sentence 2,
$\neg q \lor r$, then has both terms false unless $q$ is false, so $q = \mathrm{F}$.
Sentence 1 ties $p$ to $q$, so $p = \mathrm{F}$. Sentence 3 then reads
$p \lor r = \mathrm{F} \lor \mathrm{F} = \mathrm{F}$, contradicting the requirement that
all four hold.

$$\boxed{\text{The specifications are INCONSISTENT: no assignment satisfies all four}}$$

> [!warning] Where the contradiction comes from
> Sentence 4 says the system is **never** in interrupt mode. Sentence 2 then
> forces the kernel to be broken. Sentence 1 ties multiuser state to a working
> kernel, so the system cannot be in multiuser state either. Sentence 3 says a
> system that is not in multiuser state must be in interrupt mode, which
> sentence 4 has already ruled out. The set describes a machine that cannot
> exist. In practice this means one of the four requirements is a typo, usually
> sentence 4.

> [!info] Check by exhaustive enumeration
> The truth table above is the exhaustive check: all $2^3 = 8$ assignments were
> tested and none satisfied the conjunction. The chain of forcing steps is the
> same argument presented as a derivation, and it reaches the same conclusion,
> which is the confirmation that no row was skipped. The two routes disagree only
> if a row in the table was mis-evaluated, so comparing the count of satisfying
> rows (zero) against the chain's result (zero) is a complete check.

---

## Question 6

### **(a) Explain the concepts of tautology, contradiction and contingency in propositional logic. Explain their characteristics with example.**

*[Marks: 04, CO: 2]*

**The three classifications.** Given a formula, its class is decided by how many
rows of its truth table are true.

| Class | True in | Example |
| :-- | :-- | :-- |
| **Tautology** | every row | $p \lor \neg p$ |
| **Contradiction** | no row | $p \land \neg p$ |
| **Contingency** | some rows, not all | $p \land q$ |

The test is therefore mechanical: build the table, count the T's. A formula with
no variables is a tautology or a contradiction outright. A formula with $n$
variables is tested over $2^n$ rows.

**Where each class shows up.** Tautologies are the valid arguments of logic, and
they are what a proof system is designed to derive. Contradictions are what
makes a proof by contradiction work: if assuming $\neg \varphi$ yields a
contradiction, then $\varphi$ must be true. Contingencies are what describes
anything whose truth depends on facts, which is to say almost every sentence
actually used in a specification.

**The five connectives.**

| Connective | Symbol | Reads as | Truth condition |
| :-- | :-: | :-- | :-- |
| Negation | $\neg p$ | "not $p$" | true iff $p$ is false |
| Conjunction | $p \land q$ | "$p$ and $q$" | true iff both are true |
| Disjunction | $p \lor q$ | "$p$ or $q$" | true iff at least one is true |
| Implication | $p \to q$ | "if $p$ then $q$" | false only when $p$ true and $q$ false |
| Biconditional | $p \leftrightarrow q$ | "$p$ if and only if $q$" | true iff the two agree |

**Why the connectives matter.** They are the vocabulary in which every compound
proposition is written, and each one identifies a particular kind of valid
inference:

- **Negation** enables reductio ad absurdum, and it is what turns an assumption
  into its opposite.
- **Conjunction** combines hypotheses. A proof from $p \land q$ splits into two
  proofs, from $p$ and from $q$.
- **Disjunction** enables proof by cases. From $p \lor q$ and a conclusion that
  follows from each, the conclusion follows.
- **Implication** is the modus ponens engine: from $p$ and $p \to q$ follows $q$.
  Its truth table, which is true whenever the antecedent is false, is what makes
  "if pigs fly then I am a queen" a truth rather than a falsehood, and this is
  the single most counter-intuitive row in the subject.
- **Biconditional** records the two directions of an equivalence, so it lets one
  substitute one side for the other inside a larger argument.

**Functional completeness.** A set of connectives is functionally complete if
every truth function can be built from it. $\{\neg, \land, \lor\}$ is complete,
as is $\{\neg, \land\}$, as is $\{\mid\}$ (NAND) alone. The reason NAND alone
suffices is

$$\neg p \equiv p \mid p, \qquad p \land q \equiv (p \mid q) \mid (p \mid q)$$

and every other connective follows from those two. This is why a whole computer
processor can be built out of one gate type, and why the connectives are a
practical engineering matter rather than only a logical one.

$$\boxed{\text{tautology (always T), contradiction (always F), contingency (mixed)}}$$

> [!note] The row that catches people
> The $p \to q$ row with $p = \mathrm{F}$ and $q = \mathrm{F}$ returns **T**, and so does the
> row with $p = \mathrm{F}$ and $q = \mathrm{T}$. A conditional makes no claim about what
> happens when its antecedent is false, so it is vacuously true there. Every
> confusion about "if pigs fly then I am a queen" being true comes from reading
> more into the connective than the truth table puts in it.

---

### **(b) A security system triggers an alarm if (a) motion is detected and the window is open, or (b) the door sensor is active but the security code is not entered. (i) Assign propositional variables, (ii) express the alarm condition as a single proposition, (iii) convert it into both CNF and DNF, describing each transformation step.**

*[Marks: 06, CO: 2]*

**Assign variables.** Every variable is defined **positively**, so the negation
falls where the English puts it rather than where the reader expects it.

| Symbol | Meaning |
| :-- | :-- |
| $m$ | motion is detected |
| $w$ | window is open |
| $d$ | door sensor is active |
| $s$ | security code **is** entered |
| $A$ | the alarm triggers |

**The condition as one proposition.** Branch (a) is $m \land w$. Branch (b) is
$d \land \neg s$, because "the code is not entered" is $\neg s$ and not a new
variable. The two branches are alternatives, so they are joined by $\lor$:

$$A = (m \land w) \lor (d \land \neg s)$$

> [!warning] The trap: "but" is "and", and "not entered" negates the code
> "The code is not entered" is the negation of "$s$ = the code **is** entered".
> Defining $s$ to mean "the code is not entered" and then writing $\neg s$ gives
> $d \land s$ for the branch, which reads correctly but is the wrong polarity
> against the variable table. The safeguard is to state what each variable means
> **positively** in the table, then let the negation fall where the English puts
> it. The second trap is treating "but" as a different connective from "and".
> Logically it is conjunction, and the contrast is rhetorical, not logical.

**To DNF.** By definition, a compound proposition is in Disjunctive Normal Form (DNF)
if it is a disjunction of conjunctions of literals. The formulated condition:

$$A = (m \land w) \lor (d \land \neg s)$$

is already in DNF (minimal DNF), consisting of two clauses: $(m \land w)$ and $(d \land \neg s)$.

If the **full canonical DNF** (sum of minterms containing all 4 variables) is required,
we expand each clause using the identity $X \equiv X \land (Y \lor \neg Y)$:

$$
\begin{aligned}
m \land w &\equiv (m \land w) \land (d \lor \neg d) \land (s \lor \neg s) \\
&= (m \land w \land d \land s) \lor (m \land w \land d \land \neg s) \lor (m \land w \land \neg d \land s) \lor (m \land w \land \neg d \land \neg s)
\end{aligned}
$$

$$
\begin{aligned}
d \land \neg s &\equiv (m \lor \neg m) \land (w \lor \neg w) \land (d \land \neg s) \\
&= (m \land w \land d \land \neg s) \lor (m \land \neg w \land d \land \neg s) \lor (\neg m \land w \land d \land \neg s) \lor (\neg m \land \neg w \land d \land \neg s)
\end{aligned}
$$

Combining and removing the shared duplicate minterm $(m \land w \land d \land \neg s)$ yields the 7-minterm canonical DNF:

$$
\begin{aligned}
A_{\text{canonical DNF}} = &(m \land w \land d \land s) \lor (m \land w \land d \land \neg s) \lor (m \land w \land \neg d \land s) \lor (m \land w \land \neg d \land \neg s) \\
&\lor (m \land \neg w \land d \land \neg s) \lor (\neg m \land w \land d \land \neg s) \lor (\neg m \land \neg w \land d \land \neg s)
\end{aligned}
$$

**To CNF.** A conjunction of disjunctions, that is a product of sums.
Apply the distributive law $P \lor (Q \land R) \equiv (P \lor Q) \land (P \lor R)$:

$$
\begin{aligned}
A &= (m \land w) \lor (d \land \neg s) \\
  &= \big[(m \land w) \lor d\big] \land \big[(m \land w) \lor \neg s\big]
    && \text{distribute over } (d \land \neg s)\\
  &= \big[(m \lor d) \land (w \lor d)\big] \land \big[(m \lor \neg s) \land (w \lor \neg s)\big]
    && \text{distribute } d \text{ and } \neg s\\
  &= (m \lor d) \land (w \lor d) \land (m \lor \neg s) \land (w \lor \neg s)
    && \text{remove grouping brackets}\\
  &= (m \lor d) \land (m \lor \neg s) \land (w \lor d) \land (w \lor \neg s)
    && \text{reorder clauses}
\end{aligned}
$$

$$\boxed{\text{CNF: } (m \lor d)\land(m \lor \neg s)\land(w \lor d)\land(w \lor \neg s)}$$

**How to check the two forms.** The original proposition, the canonical DNF (7 minterms), and the CNF (4 clauses) are all logically equivalent and evaluate identically across all $2^4 = 16$ assignments of $(m, w, d, s)$.

> [!info] Check by exhaustive evaluation
> All three representations evaluate identically on all $2^4 = 16$ assignments of $m, w, d, s$.
> For instance, when $m = \mathrm{T}, w = \mathrm{T}, d = \mathrm{F}, s = \mathrm{T}$, $m \land w$ is true, so the alarm triggers;
> both the DNF and every clause of the CNF evaluate to true.
> An algebra mistake in either conversion shows up as a row where the representations disagree.

> [!note] Which form to use
> **CNF** suits resolution and automated theorem provers, which read conjunctions
> of disjunctions directly. **DNF** suits fast evaluation and hardware
> implementation, because each product can be tested in isolation and the first
> one that succeeds ends the computation. The CNF here also reads as four
> independent failure conditions: for no alarm, motion must be absent or the
> door inactive, the door must be active or no motion seen, the window must be
> shut or the door inactive, and the window must be shut or the code entered.

---

## Question 7

### **(a) A delivery company uses a computer system to manage customer orders. Sort all delivery addresses based on distance from the warehouse. Search for a customer's order by name or ID. Use a greedy approach to assign delivery vans to the nearest unserved address. Evaluate the time complexity of each algorithm used.**

*[Marks: 06, CO: 2]*

This is three algorithmic tasks plus a complexity analysis for each. The tasks are
independent, and each one has a natural choice whose justification is what the
marks are for.

**(i) Sorting the addresses by distance.**

**Algorithm chosen: merge sort.** The addresses are sorted on a single numeric
key, the distance from the warehouse. Merge sort divides the list in half, sorts
each half recursively, and merges the two sorted halves in linear time.

- Average time complexity: $O(n \log n)$
- Best case: $O(n \log n)$
- Worst case: $O(n \log n)$
- Space: $O(n)$

**Why merge sort and not the others.**

- **Bubble sort** is $O(n^2)$, which fails at tens of thousands of addresses, and
  a delivery list over a few years is comfortably in that range.
- **Quicksort** is $O(n \log n)$ on average but $O(n^2)$ if the list is already
  sorted, which is close to what a distance list looks like. That worst case is
  avoidable with a random pivot, but the guarantee is not there by default.
- **Heapsort** is $O(n \log n)$ in all cases and $O(1)$ space, but it is not
  stable, and equal distances would lose their original order.
- **Counting or radix sort** would be faster at $O(n + k)$, but only if the
  distances are integers in a known range, which floating-point distances are
  not.

Merge sort's selling point here is that its worst case equals its average case,
so a delivery system with a hard deadline can rely on it. The cost is $O(n)$
extra space.

**(ii) Searching for a customer's order.**

**Algorithm chosen: binary search**, since the list is already sorted from step
(i).

```
function BINARY-SEARCH(A, key):
    low  <- 0
    high <- length(A) - 1
    while low <= high:
        mid <- floor((low + high) / 2)
        if A[mid].id = key:
            return mid
        else if A[mid].id < key:
            low <- mid + 1
        else:
            high <- mid - 1
    return NOT-FOUND
```

- Average time complexity: $O(\log n)$
- Best case: $O(1)$, when the key sits at the first midpoint tried
- Worst case: $O(\log n)$
- Space: $O(1)$, since it iterates rather than recurses

Binary search halves the search interval at every step, so $n$ items need at
most $\lceil \log_2 n \rceil$ comparisons. For $n = 10^6$ that is 20 comparisons
against $10^6$ for a linear scan, which is the whole reason sorting is worth
doing once if many searches follow.

> [!warning] Binary search has one requirement
> The list must be sorted on the **same key** that is searched. Sorted by
> distance does **not** mean sorted by customer ID. Searching by ID requires
> either a second, ID-sorted index or a hash table. A hash table is the better
> answer for lookup by ID, at $O(1)$ average and $O(n)$ space, and this is the
> honest answer if the question allows more than one structure. The trap is to
> propose binary search on the distance-sorted list, which cannot find by ID.

**(iii) Assigning vans greedily.**

**Algorithm: nearest-neighbour greedy.** Scan the unserved addresses, take the
closest one, assign it, mark it served, and repeat.

```
function GREEDY-ASSIGN(addresses, vans):
    served <- {}
    for each van:
        current <- warehouse position
        while an unserved address remains and the van has capacity:
            best <- the unserved address nearest to current
            assign best to this van
            add best to served
            current <- position of best
    return assignment
```

- Time complexity: $O(V \cdot A)$ in the straightforward form, where $V$ is the
  number of vans and $A$ the number of addresses
- Space: $O(A)$

$$\boxed{\text{Sort } O(n \log n), \quad \text{search } O(\log n), \quad \text{assign } O(n \log n + nm)}$$

**The complexity analysis.** The outer loop runs $V$ times. For each van, the
inner loop scans the unserved list to find the nearest, and it does so once per
assigned address, giving $A$ scans in the worst case, each of cost $O(A)$ if the
list is not indexed. So the total is $O(V \cdot A^2)$ in the worst case, or
$O(A^2)$ when the number of vans is proportional to the address count. Using a
spatial index, a $k$-d tree or a grid hash, reduces the nearest-neighbour query
to $O(\log A)$, giving $O(V A \log A)$.

**Why greedy here, and what it costs.** Greedy is $O(VA^2)$ and simple, and for
a delivery list it is close to optimal in practice. It does **not** guarantee the
shortest total route, which is the travelling salesman problem and is NP-hard.
The bound is that greedy's tour is at most $O(\log A)$ times the optimal tour in
the worst case, and in practice it lands within a few percent. Since the exam
asks for a greedy approach, the answer is the nearest-neighbour construction with
its complexity stated, plus the note that it is a heuristic.

> [!info] Check the complexity by counting operations
> For $n$ items, merge sort performs about $n \log_2 n$ comparisons: $\log_2 n$
> levels, each doing a linear merge of $n$ items. Binary search does at most
> $\lceil \log_2 n \rceil$ comparisons, and the bound is tight when the key is
> absent. The greedy scan does one comparison per unserved address per assignment,
> so $A + (A-1) + \cdots + 1 = A(A+1)/2$ comparisons per van, which is $O(A^2)$,
> giving $O(VA^2)$ overall. These counts are what makes the table above more
> than a set of labels: each one can be derived by counting what the algorithm
> actually does, and the three agree with the standard classifications.

---

### **(b) Determine whether the biconditionals are true or false.**

*[Marks: 04, CO: 2]*

**The rule.** A biconditional $P \leftrightarrow Q$ is true exactly when the two
sides have the **same** truth value, that is when both are true or both are
false. It is false when they disagree.

$$P \leftrightarrow Q \equiv (P \to Q) \land (Q \to P)$$

So the evaluation is two steps: find the truth value of each side separately,
then compare. The comparison is the only step that decides the answer, and it is
the step people get wrong.

**The four cases.**

**(i)** $2 + 2 = 4$ is true. $1 + 1 = 2$ is true. Same value, so the
biconditional holds.

**(ii)** $1 + 1 = 2$ is true. $2 + 3 = 5$, not $4$, so $2 + 3 = 4$ is false. The
values disagree.

**(iii)** $1 + 1 = 3$ is false. Monkeys cannot fly, so that is false. Both false,
so they match, and the biconditional holds.

**(iv)** $0 > 1$ is false. $2 > 1$ is true. The values disagree.

$$\boxed{\text{(i) TRUE}}$$

$$\boxed{\text{(ii) FALSE}}$$

$$\boxed{\text{(iii) TRUE}}$$

$$\boxed{\text{(iv) FALSE}}$$

> [!warning] Why two false statements give a true biconditional
> Two false statements make a **true** biconditional. It asserts that the two
> sides have the same truth value, not that either is true. In (iii) both
> "$1 + 1 = 3$" and "monkeys can fly" are false, so they match, and the
> biconditional is true. The tempting conclusion "false, because $1 + 1 \ne 3$" is
> therefore wrong.
>
> The mathematical reading of "if and only if" is strict. It is a statement of
> equivalence, and it has exactly two possible values. Ordinary English uses the
> phrase more loosely, sometimes implying that both sides are true, and that
> implication is not part of the connective.

> [!info] Check against the two-conditionals form
> Each result can be verified by evaluating $(P \to Q) \land (Q \to P)$
> separately. For (iii), $P = Q = \mathrm{F}$, so both conditionals are vacuously
> true, and their conjunction is true, which matches the answer above. For (ii),
> $P = \mathrm{T}$ and $Q = \mathrm{F}$, so $P \to Q$ is false, the conjunction
> fails, and the biconditional is false. For (i) and (iv) the same two-step
> evaluation gives T and F respectively. Rewriting the connective as a
> conjunction of conditionals and evaluating that is an independent route to the
> same four answers, and it is the form to use when a biconditional appears
> inside a larger formula whose truth table is being built column by column.

## Question 8

### **(a) Suppose that $a$ and $b$ are integers, $a \equiv 11 \pmod{19}$ and $b \equiv 3 \pmod{19}$. Find the integer $c$ with $0 \le c \le 18$ such that (i) $c \equiv 7a + 3b \pmod{19}$, (ii) $c \equiv a^3 + 4b^3 \pmod{19}$.**

*[Marks: 04, CO: 2]*

**The rule that settles all of these.** Congruence behaves like equality under
addition, subtraction and multiplication. If $a \equiv c$ and $b \equiv d$
modulo $n$, then

$$a + b \equiv c + d, \qquad a - b \equiv c - d, \qquad ab \equiv cd \pmod{n}$$

So every part is computed by substituting the residues and reducing at the end.

**(i) $c \equiv 7a + 3b \pmod{19}$**

$$7a + 3b \equiv 7(11) + 3(3) = 77 + 9 = 86 \pmod{19}$$

Reduce: $86 = 19(4) + 10$.

$$\boxed{c = 10}$$

**(ii) $c \equiv a^3 + 4b^3 \pmod{19}$**

$$a^3 + 4b^3 \equiv 11^3 + 4(3^3) = 1331 + 108 = 1439 \pmod{19}$$

Reduce: $1439 = 19(75) + 14$.

$$\boxed{c = 14}$$

> [!warning] Two different questions look identical here
> With $a \equiv 11$ and $b \equiv 3$, the products $ab$ and $a + b$ also reduce to
> $14$, which is part (ii)'s answer. So a draft that computes $ab$ and $a+b$
> instead of $7a + 3b$ and $a^3 + 4b^3$ produces a part (ii) that looks right, and
> a part (i) that is wrong.
>
> This is not hypothetical; it is the specific failure recorded for this section.
> The reason it is hard to see is that the heading, the marks and even one of the
> two answers all agree with the correct version, so only part (i) carries the
> evidence.
>
> **The safeguard is to write the question's expression into the working before
> computing anything.** Not "part (i): 14" but "$7a + 3b \equiv 7(11) + 3(3) = 86$".
> Once the expression is on the page, a substituted expression cannot pass
> unnoticed, because it is visibly not the one that was asked for.

**Why substitution is legitimate.** The chain rule is what makes this work, and
it is worth stating once because it is used in every subsequent number theory
question. Write $a = 11 + 19m$ and $b = 3 + 19k$ for integers $m, k$. Then

$$ab = (11 + 19m)(3 + 19k) = 33 + 19(11k + 3m + 19mk)$$

so $ab - 33$ is a multiple of $19$, which is the definition of $ab \equiv 33$.
The multiple of $19$ that appears carries the information about $m$ and $k$, so
the residue does not depend on which representatives $a$ and $b$ were chosen.
This is the argument behind "substitute the residues".

**The reduction step.** After computing a residue, reduce it into the standard
range $0, 1, \ldots, n-1$ by subtracting $n$ until the result lies in range. For
$33$ modulo $19$ this means one subtraction, giving $14$. For large products the
efficient version is to reduce *during* the multiplication rather than at the
end, which is exactly what modular exponentiation does.

> [!info] Check by direct substitution
> Verify by choosing a specific $a$ and $b$ and computing the residue directly.
> Take the smallest, $a = 11$ and $b = 3$. Then $7a + 3b = 86$, and
> $86 = 19(4) + 10$, so the residue is $10$, matching part (i). Take a larger
> pair, $a = 30$ and $b = 41$, both of which are congruent to the given residues:
> $30 = 19 + 11$ and $41 = 38 + 3$. Then
> $7(30) + 3(41) = 210 + 123 = 333$, and $333 = 19(17) + 10$, so the residue is
> again $10$. A third pair, $a = 49$ and $b = 60$, gives
> $7(49) + 3(60) = 343 + 180 = 523 = 19(27) + 10$, again $10$. Three different
> representatives producing the same residue is what shows the substitution is
> legitimate rather than a coincidence of small numbers.
>
> For part (ii), $a = 11, b = 3$ gives $1439 = 19(75) + 14$; the pair $a = 30,
> b = 41$ gives $30^3 + 4(41^3) = 27000 + 275684 = 302684$, and
> $302684 = 19(15930) + 14$. Same residue, much larger numbers.

---

### **(b) Solve $3^{644} \bmod 645$ using a well-known algorithm.**

*[Marks: 04, CO: 2]*

**The algorithm is fast exponentiation, also called square-and-multiply.** It
computes $a^b \bmod n$ in $O(\log b)$ steps instead of $O(b)$ by writing the
exponent in binary and repeatedly squaring.

**The method.** Write $b$ in binary. Then

$$a^b \equiv \prod_{i \,:\, b_i = 1} \left(a^{2^i} \bmod n\right) \pmod{n}$$

and the terms $a^{2^i} \bmod n$ are generated by repeated squaring:

$$a^{2^0}, \qquad a^{2^{i+1}} \equiv \left(a^{2^i}\right)^2 \pmod{n}$$

Each is reduced modulo $n$ immediately, so no intermediate value exceeds $n^2$,
which is what keeps the computation inside machine precision. This is the point
of the method: without the reduction, $3^{644}$ has over $300$ digits.

**Write 644 in binary.**

$$644 = 512 + 128 + 4 = 2^9 + 2^7 + 2^2$$

So the binary form is $1010000100_2$, with ones in positions $9, 7$ and $2$.
Three rows of the table below will be used.

**Repeated squaring of $3$ modulo $645$.**

| $i$ | $2^i$ | $3^{2^i} \bmod 645$ | derived from |
| :--: | :--: | :-- | :-- |
| 0 | 1 | 3 | given |
| 1 | 2 | 9 | $3^2 = 9$ |
| 2 | 4 | 81 | $9^2 = 81$ |
| 3 | 8 | 111 | $81^2 = 6561 = 10(645) + 111$ |
| 4 | 16 | 66 | $111^2 = 12321 = 19(645) + 66$ |
| 5 | 32 | 486 | $66^2 = 4356 = 6(645) + 486$ |
| 6 | 64 | 126 | $486^2 = 236196 = 366(645) + 126$ |
| 7 | 128 | 396 | $126^2 = 15876 = 24(645) + 396$ |
| 8 | 256 | 81 | $396^2 = 156816 = 243(645) + 81$ |
| 9 | 512 | 111 | $81^2 = 6561 = 10(645) + 111$ |

The cycle visible in rows 2, 3, 8 and 9, namely $81 \to 111 \to 66 \to 486 \to 126 \to 396 \to 81$, is real and follows from $645 = 3 \times 5 \times 43$, which is not prime and not a prime power.

**Multiply the three rows that are one.** Positions $9, 7$ and $2$:

$$3^{644} \equiv 111 \times 396 \times 81 \pmod{645}$$

First, $111 \times 396 = 43956$. Reducing:

$$43956 = 68(645) + 96, \qquad \text{so } 111 \times 396 \equiv 96 \pmod{645}$$

Then

$$96 \times 81 = 7776 = 12(645) + 36$$

$$3^{644} \equiv 96 \times 81 \equiv 36 \pmod{645}$$

$$\boxed{3^{644} \bmod 645 = 36}$$

Both notations are correct and mean the same thing. The exam-style origin prints
the `bmod` form, so that is what is boxed here; the congruence form above is
easier to follow while working, since each step is a congruence rather than a
remainder.

> [!info] Check against the Chinese Remainder Theorem
> Factor the modulus: $645 = 3 \times 5 \times 43$, three coprime factors. Then
> compute the residue separately modulo each:

| modulus | $3^{644}$ mod it | why |
| :-- | :-- | :-- |
| 3 | 0 | $3$ divides $3^{644}$ |
| 5 | 1 | $3^4 = 81 \equiv 1 \pmod 5$, and $644 = 4(161)$, so the residue is $1$ |
| 43 | 36 | found by the same square-and-multiply method modulo 43 |

Combining the three residues by the Chinese Remainder Theorem gives the single
residue $36$ modulo $645$. The two routes, one direct and one via three smaller
moduli, agree on $36$, which is the confirmation worth having, because a single
wrong squaring propagates through every later row and produces an answer that
looks entirely reasonable. Note that Euler's theorem is **not** available here,
since $\gcd(3, 645) = 3 \ne 1$, so reducing the exponent modulo $\phi(645) = 336$
would be invalid. This is a good example of a method that works only when the
side condition is checked first.

---

### **(c) Give a real-world example of the generalized pigeonhole principle.**

*[Marks: 02, CO: 2]*

**The principle.** If $N$ objects are placed into $k$ boxes, then some box
contains at least $\lceil N/k \rceil$ objects.

The generalised form goes further than the simple one. The simple form says only
that $k + 1$ objects in $k$ boxes forces some box to hold at least two. The
generalised form gives the guaranteed minimum occupancy as a number, and that
number is the ceiling of the ratio.

**Why the ceiling.** Spreading $N$ objects as evenly as possible fills each box
with either $\lfloor N/k \rfloor$ or $\lceil N/k \rceil$ objects. No smaller
number than the ceiling can be guaranteed, because an even spread is always
achievable, and in it the fullest box holds exactly $\lceil N/k \rceil$.

**A real-world example.** A delivery company operates a call centre. Over $365$
days of recorded customer contacts, each day's contacts fall into one of $20$
issue categories: billing, delivery delay, damaged item, and so on. Since $365 >
20 \times 18 = 360$, at least one category received contacts on at least
$\lceil 365/20 \rceil = 19$ days. The number $19$ is what staffing has to plan
for, and the principle produces it without looking at a single record.

**A second example, closer to computing.** A warehouse receives $4800$ packages
for $250$ storage slots. Then some slot holds at least
$\lceil 4800/250 \rceil = \lceil 19.2 \rceil = 20$ packages, so the shelves must
be rated for $20$, and the figure comes from the principle alone.

**Why it matters in computing.** The principle is the basis of several standard
results. In hashing it guarantees collision counts: with $N$ keys in $m$ slots,
some slot receives at least $\lceil N/m \rceil$ keys, which is the worst-case
chain length for chained hashing. In sorting theory it gives the lower bound
$\Omega(n \log n)$: there are $n!$ possible orderings and only $2^c$ outcomes
from $c$ comparisons, so $2^c \ge n!$ and therefore $c \ge \log_2 n!$, which is
$\Omega(n \log n)$.

$$\boxed{\text{More objects than box capacity forces at least one crowded box}}$$

> [!note] What two marks need
> The statement of the principle **with the ceiling**, since that is what makes it
> the generalised form; one concrete example with the numbers worked; and the
> conclusion that follows. Restating only the simple form and then giving an
> example loses the generalisation mark, because the ceiling is never mentioned.
