---
title: "ECE 2213 · 2019 Exam Style Answers"
tags:
  - numerical-methods
  - discrete-mathematics
  - previous-year
---

# ECE 2213: 2019 Semester Final · Exam Style Answers

**RUET · ECE Dept · B.Sc. Engineering 2nd Year Even Semester Examination, 2019**
**Full Marks:** 96 · **Time:** 03 Hours

> [!info] Format
> Concise, mark-aligned, written as an answer script.
> Question text and marks come from the paper:
> [[2019|the 2019 paper]].
> Every numerical here was derived twice by independent routes. Where the two
> routes disagreed, the disagreement was settled before the next question was
> written, and the divergence is recorded in a callout.
>
> This is a pre-OBE paper, so there is **no CLO column**. Marks only.

---

# SECTION A

## Question 1

### **(a) Define numerical method. How does it become popular? Why do ECE engineers require numerical methods? [Marks: 04]**

A **numerical method** is a procedure that obtains the answer of a mathematical
problem as a finite sequence of arithmetic operations, yielding an approximate
value in place of the exact closed form.

**Why it became popular**

1. Most engineering problems have no closed-form solution at all. The integral
   $\int e^{-x^2}\,dx$, the motion of three bodies under gravity, and the
   boundary-value problem of a transistor region have no elementary antiderivative
   or formula, yet all three must be evaluated in practice.
2. Only arithmetic can be executed by a machine. A numerical method converts a
   problem into additions, multiplications and comparisons, which is exactly what
   a computer performs.
3. The growth of computing power made long arithmetic chains cheap. Methods that
   required thousands of operations, and were therefore once unusable, became
   routine.
4. Tabulated results and hand computation gave way to direct evaluation at the
   point of interest, with the error under the engineer's control.

**Why ECE engineers require them**

1. Circuit quantities are often implicit. The diode equation
   $I = I_s(e^{V/V_T}-1)$ and the power balance $P = VI - \sum I^2R$ give $V$ and
   $I$ through equations that cannot be solved for the current in closed form.
2. Field problems reduce to difference equations. The potential distribution in
   a semiconductor region or a screening geometry is a Laplace or Poisson problem
   that is solved on a mesh, not in symbols.
3. Signal quantities are sampled. Any quantity derived from a discrete set of
   measurements, whether by differentiation, integration or a filter, is obtained
   numerically.
4. Optimisation is iterative. Impedance matching, cut-off frequency placement and
   bias-point selection are all found by repeated improvement of an estimate.

$$\boxed{\text{Numerical method} = \text{a finite arithmetic procedure for a problem without a usable closed form}}$$

---

### **(b) What are the errors involved in numerical methods? How do they enter into the process? Give example. [Marks: 04]**

The errors are **inherent error**, **absolute error**, and **relative error**.

**Inherent error.** The error already present in the physical statement, before
any computation. It subdivides into:

- **Data error**, from measurement. A resistance read off a meter as $4.7\ \Omega$
   carries the meter's own error, whatever is done afterwards.
- **Conversion error**, from the problem statement. When a continuous law is
   written as a formula, finite precision in the law's constants is carried in.
- **Modelling error**, from the assumptions made. The formula $I = V/R$ ignores
   temperature and tolerance; the neglected terms are the modelling error.

Inherent error is not produced by the arithmetic and cannot be reduced by
carrying more digits.

**Absolute error.** The difference between the approximate value $A$ and the true
value $T$:

$$E_{\text{abs}} = A - T, \qquad |E_{\text{abs}}| = |A - T|$$

**Relative error.** The absolute error measured against the true value:

$$E_{\text{rel}} = \frac{E_{\text{abs}}}{T}, \qquad E_{\text{pct}} = 100\frac{E_{\text{abs}}}{T}$$

**How they enter the process.** The steps of any computation are:

1. Formulate the physical problem, where **modelling error** enters.
2. Gather the data, where **data error** enters.
3. Choose a method and carry out the arithmetic, where **round-off error**
   enters at every step.
4. Apply truncation when an infinite process is cut short, where
   **truncation error** enters.
5. Report the result, where the errors of steps 1, 2, 4 and the propagated
   round-off of step 3 appear together.

**Example.** Take $R = 220\ \Omega$ and $V = 10\ \text{V}$, so
$I = 10/220 = 0.0454545\ \text{A}$. Reading the current as $0.045\ \text{A}$ on a
three-digit display gives

$$E_{\text{abs}} = 0.045 - 0.0454545 = -0.0004545\ \text{A}$$

$$E_{\text{rel}} = \frac{-0.0004545}{0.0454545} = -0.01 = -1\%$$

The $-1\%$ has two sources: the display rounding the reading to three decimals,
and the tolerance of the resistor. The first is round-off in the reporting, the
second is data error in the input.

---

### **(c) What are the error representations? Two PT-voltmeter arrangements give $999\text{V}$ and $9999\text{V}$ instead of $1\text{kV}$ and $10\text{kV}$. Obtain error by all possible error representations. Hence comment on error strength of the readings. [Marks: 04]**

**The representations.** Given a true value $T$ and an approximate value $A$,
with $e = A - T$:

1. **Absolute error:** $e = A - T$, and its magnitude $|e|$.
2. **Relative error:** $\dfrac{e}{T}$, the error measured against the true value.
3. **Percentage error:** $100\dfrac{e}{T}$.
4. **Relative (or percentage) accuracy:** $\dfrac{A}{T}$, equivalently
   $1 - \left|\dfrac{e}{T}\right|$, which measures how near $A$ is to $T$.
5. **Limiting error (error bound):** a stated bound $|e| \le \varepsilon$
   within which the value is guaranteed to lie.

**Arrangement 1: $A = 999\ \text{V}$, $T = 1000\ \text{V}$.**

$$e = 999 - 1000 = -1\ \text{V}, \qquad |e| = 1\ \text{V}$$

$$E_{\text{rel}} = \frac{-1}{1000} = -10^{-3} = -0.1\%$$

$$E_{\text{rel, reading}} = \frac{-1}{999} = -1.001 \times 10^{-3} = -0.1001\%$$

$$\text{Accuracy} = \frac{999}{1000} = 0.999 = 99.9\%$$

**Arrangement 2: $A = 9999\ \text{V}$, $T = 10000\ \text{V}$.**

$$e = 9999 - 10000 = -1\ \text{V}, \qquad |e| = 1\ \text{V}$$

$$E_{\text{rel}} = \frac{-1}{10000} = -10^{-4} = -0.01\%$$

$$E_{\text{rel, reading}} = \frac{-1}{9999} = -1.0001 \times 10^{-4} = -0.010001\%$$

$$\text{Accuracy} = \frac{9999}{10000} = 0.9999 = 99.99\%$$

**Comment on the error strength.** The absolute error is identical in the two
arrangements, $1\ \text{V}$, so the absolute error separates them not at all.
Against the true value, the $9999\ \text{V}$ reading has a relative error of
$0.01\%$ while the $999\ \text{V}$ reading has $0.1\%$, a factor of ten
difference. The $9999\ \text{V}$ reading is therefore the stronger one.

$$\boxed{|e| = 1\ \text{V}\ \text{for both, but}\ E_{\text{rel}} = 10^{-3}\ \text{against}\ 10^{-4}}$$

> [!info] Check against the exact ratios
> The ratio of the two relative errors equals the inverse ratio of the true
> values: $\dfrac{10^{-3}}{10^{-4}} = 10 = \dfrac{10000}{1000}$. A common absolute
> error on magnitudes differing by a factor of ten produces relative errors
> differing by the same factor, which is the point the comment rests on.

---

## Question 2

### **(a) What is meant by iterative method? Write the names of iterative methods to solve nonlinear equations. Write the generalized steps to solve the nonlinear equations using iterative methods. [Marks: 04]**

An **iterative method** solves $f(x) = 0$ by producing a sequence
$x_0, x_1, x_2, \ldots$ from a starting estimate $x_0$, each term obtained from
the preceding ones by a fixed rule, so that the sequence converges to the root
$x = r$. The answer is accepted when successive terms agree to the required
precision, rather than when a formula closes.

**Methods for a nonlinear equation**

1. Bisection (or false position, regula falsi)
2. Fixed-point iteration
3. Newton–Raphson
4. Secant
5. Bairstow (for polynomial roots)

**Generalized steps**

1. Rewrite the problem in the form $f(x) = 0$.
2. Determine the interval or interval of interest, and count the roots in it
   from a change of sign of $f$.
3. Choose a starting estimate $x_0$ and, where required, a second estimate.
4. Derive the iteration formula $x_{k+1} = g(x_k)$.
5. Apply the formula repeatedly, recording each iterate.
6. Test for convergence by comparing successive iterates,
   $|x_{k+1} - x_k| < \varepsilon$, with $\varepsilon$ the tolerance.
7. If the sequence diverges or stalls, restart from a better estimate or from
   another method, and note the failure.
8. Verify the accepted root by substitution back into $f(x) = 0$.

---

### **(b) Compute current, $I$ from the following power balance equation obtained from an electric circuit by using an iterative method: $5I^2 + 50I = 1000$. [Marks: 04]**

Write the equation in the form $f(I) = 0$:

$$f(I) = 5I^2 + 50I - 1000 = 0, \qquad f'(I) = 10I + 50$$

**Closed-form check on the answer.** Completing the square, or dividing by 5,

$$I^2 + 10I - 200 = 0 \implies I = \frac{-10 \pm \sqrt{100 + 800}}{2} = \frac{-10 \pm 30}{2}$$

the two roots are $I = 10$ and $I = -20$. The current is positive, so $I = 10$ is
the root of interest. This fixes the target against which the iterations below
are judged.

**Iteration by Newton–Raphson.** The formula is

$$I_{k+1} = I_k - \frac{5I_k^2 + 50I_k - 1000}{10I_k + 50}$$

Take $I_0 = 5$, and note $f(5) = 125 + 250 - 1000 = -625 < 0$ while
$f(20) = 2000 + 1000 - 1000 > 0$, so the root lies above $I_0$ and the iteration
moves the right way.

| $k$ | $I_k$ | $f(I_k)$ | $f'(I_k)$ | $I_{k+1}$ |
| :--: | :-- | :-- | :-- | :-- |
| 0 | 5 | $-625$ | 100 | $11.25$ |
| 1 | $11.25$ | $195.3125$ | $162.5$ | $10.0480769$ |
| 2 | $10.0480769$ | $7.2231$ | $150.4808$ | $10.0000768$ |
| 3 | $10.0000768$ | $0.0115$ | $150.0008$ | $10.0000000$ |

The iterates settle on $I = 10$. The last correction is $0.0000768$, already
below $10^{-4}$, so the value is accepted.

$$\boxed{I = 10\ \text{A}}$$

> [!info] Check against the original equation
> Substituting $I = 10$ directly, $5(100) + 50(10) = 500 + 500 = 1000$, matching
> the right-hand side exactly. The substitution is the simplest test available
> and it confirms both the arithmetic of the iteration and the algebraic solution
> $I = (-10 + 30)/2$.

---

### **(c) Write the steps of N-R method. Discuss its merits and demerits. [Marks: 04]**

**Newton–Raphson for $f(x) = 0$.**

1. Write the equation as $f(x) = 0$.
2. Compute the derivative $f'(x)$.
3. Choose $x_0$ close to the root, from a sign change or a physical estimate.
4. Apply $x_{k+1} = x_k - \dfrac{f(x_k)}{f'(x_k)}$.
5. Stop when $|x_{k+1} - x_k| < \varepsilon$, or when $|f(x_k)| < \varepsilon$.
6. Verify by substituting the root back into $f(x) = 0$.

Geometrically, $x_{k+1}$ is the intercept on the $x$-axis of the tangent to
$y = f(x)$ at $x_k$, so the root is approached along successive tangents.

**Merits**

1. **Fastest available.** Second-order convergence near the root: the number of
   correct digits roughly doubles per step, so three or four steps usually
   suffice where bisection needs thirty.
2. **One estimate is enough.** Only $x_0$ is needed, unlike the secant or
   regula-falsi methods which require two.
3. **Non-polynomial equations are handled.** Transcendental equations, for
   instance $x = \cos x$ or $I = I_s(e^{V/V_T}-1)$, are solved directly, with no
   need to isolate $x$.
4. **Extends to systems.** The same tangent idea applies to $n$ simultaneous
   equations through the Jacobian, which makes it the standard method for a
   nonlinear network.

**Demerits**

1. **$f'(x)$ must be available.** An analytic derivative is needed. When it is
   difficult or costly, the method loses its advantage.
2. **Poor $x_0$ can fail.** If the tangent is nearly horizontal, $f'(x_k) \approx 0$
   and the next iterate is thrown far away. Starting far from the root can send
   the sequence into divergence rather than toward it.
3. **No bracket is maintained.** Unlike bisection, the method gives no guaranteed
   interval containing the root, so a failure may not be detected until late.
4. **Repeated roots slow it down.** At a root of multiplicity $m > 1$ the
   convergence order falls from 2 toward 1, and each step gains little.
5. **Complex roots are awkward.** The iterates can leave the real axis when $f$
   or $f'$ takes complex values, so real-root isolation must be done beforehand.

---
## Question 3

### **(a) Discuss Gauss Elimination method to solve linear simultaneous algebraic equations. [Marks: 04]**

**Gauss elimination** solves $Ax = b$ by transforming the coefficient matrix into
upper triangular form using elementary row operations, then recovering the
unknowns by back substitution. The solution set is unchanged, since every
operation is reversible.

**The system.** For $n$ equations in $n$ unknowns,

$$a_{11}x_1 + a_{12}x_2 + \cdots + a_{1n}x_n = b_1$$

$$\vdots$$

$$a_{n1}x_1 + a_{n2}x_2 + \cdots + a_{nn}x_n = b_n$$

**Steps**

1. **Forward elimination.** Using $R_1$, eliminate $x_1$ from $R_2$ through $R_n$
   by forming $R_i \leftarrow R_i - \dfrac{a_{i1}}{a_{11}}R_1$. Then use the
   modified $R_2$ to eliminate $x_2$ from $R_3$ through $R_n$, and continue.
   After pass $k$ the first $k$ equations have $k$ non-zero coefficients and the
   remaining have zeros in the first $k$ columns.
2. **Triangular system.** After $n-1$ passes the matrix is upper triangular:

$$u_{11}x_1 + u_{12}x_2 + \cdots + u_{1n}x_n = b_1'$$

$$\qquad\qquad u_{22}x_2 + \cdots + u_{2n}x_n = b_2'$$

$$\qquad\qquad\qquad\qquad \ddots \qquad \vdots$$

$$\qquad\qquad\qquad\qquad u_{nn}x_n = b_n'$$

3. **Back substitution.** From the last equation,
   $x_n = b_n'/u_{nn}$. Substitute into the $(n-1)$-th, giving $x_{n-1}$, and
   continue upward to $x_1$.
4. **Division by zero.** If a pivot $u_{kk}$ is zero, the row is exchanged with
   one below having a non-zero entry in that column.
5. **Verification.** Substitute the obtained vector back into the original
   system.

**Operation count.** Forward elimination needs roughly $\dfrac{n^3}{3}$
multiplications and divisions; back substitution needs $\dfrac{n^2}{2}$. Total
cost grows as $n^3$, so the method is practical for moderate $n$ and for a single
right-hand side.

**Use in ECE.** Nodal analysis of a network with more than two nodes produces a
set of simultaneous equations larger than is comfortable by hand. Gauss
elimination converts it to a triangular set whose values are read off
successively, which is the standard automated form of that solution.

---

### **(b) Discuss partial and complete pivoting in brief. [Marks: 04]**

**Partial pivoting.** At step $k$ of the elimination, search column $k$ of the
rows $k$ through $n$ for the entry of largest absolute value, and exchange it
with the entry in position $(k,k)$ before forming the multipliers. The
multiplier is then

$$m_{ik} = \frac{a_{ik}}{a_{kk}}, \qquad |m_{ik}| \le 1$$

hence no multiplier exceeds one in magnitude, and the rounding introduced by the
multiplier is controlled. Partial pivoting searches one column only, and is
sufficient for the great majority of systems.

**Complete pivoting.** At step $k$, search the whole remaining sub-matrix, rows
$k$ through $n$ and columns $k$ through $n$, for the entry of largest absolute
value, and bring it to position $(k,k)$ by a row exchange **and** a column
exchange. Column exchanges reorder the unknowns, so the order in which the
solution vector is written must be restored afterwards. The extra search raises
the cost by a factor of about $n^2$ per step, which is why complete pivoting is
reserved for systems that are nearly singular or where numerical stability is
critical.

**Comparison.**

| | Partial pivoting | Complete pivoting |
| :--- | :--- | :--- |
| Search region | column $k$, rows $k$ to $n$ | sub-matrix, rows and columns $k$ to $n$ |
| Row exchange | yes | yes |
| Column exchange | no | yes, unknown order changes |
| Stability | adequate for most systems | best available |
| Cost | low | higher by a factor of about $n^2$ |

**When it matters.** If the pivot $a_{kk}$ is small relative to the entries below
it, the multiplier $m_{ik}$ is large, and the row $R_i - m_{ik}R_k$ carries a
value dominated by rounding. Choosing the largest available pivot keeps the
magnitude of what is subtracted under control, and prevents a small physical
quantity from being lost against a large one.

---

### **(c) Obtain the nodal equations from the following circuit. Hence solve for the unknowns using Gauss-Seidel iterative method. Show two iterations only. [Marks: 04]**

**Circuit.** Two non-reference nodes, $V_1$ and $V_2$, with a common reference
ground. Node 1 connects to ground through $2\ \Omega$ and to node 2 through
$4\ \Omega$, with a $5\ \text{A}$ source entering node 1 through the top branch.
Node 2 connects to ground through $6\ \Omega$ and to node 1 through
$4\ \Omega$, with a $5\ \text{A}$ source leaving toward node 1 and a
$10\ \text{A}$ source entering node 2.

```text
                    5 A (enters Node 1)
                +-----------( <- )-----------+
                |                           |
          Node 1|            4 Ω            |Node 2
          ------+----------/\/\/\-----------+-------+
          |                                 |       |
          |                                 |       |
        [2 Ω]                             [6 Ω]   ( ^ ) 10 A
          |                                 |       |
          |                                 |       |
          +---------------------------------+-------+
                          Reference Ground
```

**KCL at node 1.** Currents leaving: through $2\ \Omega$ to ground, through
$4\ \Omega$ to node 2, and $5\ \text{A}$ back through the top branch.

$$\frac{V_1}{2} + \frac{V_1 - V_2}{4} - 5 = 0$$

Multiplying by 4:

$$2V_1 + V_1 - V_2 - 20 = 0 \implies \boxed{3V_1 - V_2 = 20}$$

**KCL at node 2.** Currents leaving: through $6\ \Omega$ to ground, through
$4\ \Omega$ to node 1, and $5\ \text{A}$ through the top branch. The
$10\ \text{A}$ source enters, so it stands on the other side.

$$\frac{V_2}{6} + \frac{V_2 - V_1}{4} + 5 = 10$$

Multiplying by 12:

$$2V_2 + 3(V_2 - V_1) + 60 = 120 \implies \boxed{-3V_1 + 5V_2 = 60}$$

**Gauss-Seidel form.** Solve each equation for the diagonal unknown, and use the
most recent value of the other as soon as it is available.

$$V_1^{(k+1)} = \frac{20 + V_2^{(k)}}{3}, \qquad V_2^{(k+1)} = \frac{60 + 3V_1^{(k+1)}}{5}$$

The coefficient matrix is diagonally dominant, since $|3| > |-1|$ in the first
row and $|5| > |-3|$ in the second, so the iteration converges. Start from
$V_1^{(0)} = V_2^{(0)} = 0$.

| Iteration | $V_1^{(k+1)} = \dfrac{20 + V_2^{(k)}}{3}$ | $V_2^{(k+1)} = \dfrac{60 + 3V_1^{(k+1)}}{5}$ |
| :--: | :-- | :-- |
| 1 | $\dfrac{20 + 0}{3} = 6.666667$ | $\dfrac{60 + 3(6.666667)}{5} = 16.000000$ |
| 2 | $\dfrac{20 + 16}{3} = 12.000000$ | $\dfrac{60 + 3(12)}{5} = 19.200000$ |

Two iterations only, as required.

$$V_1^{(1)} = 6.666667\ \text{V}, \quad V_2^{(1)} = 16.000000\ \text{V}$$
$$V_1^{(2)} = 12.000000\ \text{V}, \quad V_2^{(2)} = 19.200000\ \text{V}$$

**The exact solution, for reference.** Adding the two equations eliminates $V_1$:

$$4V_2 = 80 \implies V_2 = 20\ \text{V}, \qquad 3V_1 = 40 \implies V_1 = 13.333333\ \text{V}$$

$$\boxed{V_1 = 13.3333\ \text{V}, \qquad V_2 = 20\ \text{V}}$$

> [!info] Check against the exact solution
> The iterates approach the exact pair from below in both components:
> $6.6667 \to 12 \to 13.0667 \to 13.28$ against $13.3333$, and
> $16 \to 19.2 \to 19.84 \to 19.968$ against $20$. The errors are
> $6.6667, 1.3333, 0.2667, 0.0533$ and $4, 0.8, 0.16, 0.032$, so each falls by a
> factor of exactly **five** per sweep.
>
> That factor is not an accident and it is worth deriving rather than accepting.
> The Jacobi iteration matrix is $T_J = \begin{bmatrix} 0 & 1/3 \\ 3/5 & 0 \end{bmatrix}$
> with spectral radius $\rho(T_J) = 1/\sqrt{5}$. For Gauss-Seidel, the iteration matrix is
> $T_{GS} = (D-L)^{-1}U = \begin{bmatrix} 0 & 1/3 \\ 0 & 1/5 \end{bmatrix}$, whose non-zero
> eigenvalue is $\lambda = 1/5 = \rho(T_J)^2$. The Gauss-Seidel spectral radius is therefore
> $\rho(T_{GS}) = 1/5$, which means the error contracts by a factor of exactly five in every sweep.
> Either way the recursion was written down the right way round, since a wrong ordering gives a
> spectral radius near or above one.

> [!warning] Where this exam meets the topic again
> The two-node Gauss-Seidel pattern above is the same construction used in
> **Q.8(b)**, where four interior nodes are solved instead of two.

---

## Question 4

### **(a) What is curve fitting? Why is it required for ECE engineers? Discuss least square technique condition. [Marks: 04]**

**Curve fitting** is the construction of an equation $y = f(x)$ that represents
the trend of a set of data points $(x_i, y_i)$. Where interpolation forces the
curve through every point, curve fitting accepts that the points carry error and
seeks a single relation that describes the whole set.

**Why it is required for ECE engineers**

1. **Data are noisy.** A voltage, a gain, a delay or a bit-error rate measured
   repeatedly gives scattered values. Fitting an underlying law separates the
   trend from the scatter and quantifies the scatter.
2. **A compact model is wanted.** A characteristic measured at ten points is
   replaced by two or three constants, which is what a simulator and a hand
   calculation both use.
3. **Values must be predicted** where no measurement exists, inside and
   immediately outside the measured range.
4. **Parameters must be extracted.** Resistance, inductance, time constant,
   cut-off frequency and beta are all obtained by fitting the measured response
   to the known equation of the device.

**Least squares.** Let the trial curve be $y = a_0 + a_1 x + \cdots + a_m g_m(x)$.
The residual at point $i$ is $r_i = y_i - f(x_i)$. The coefficients are chosen to
minimise the sum of squared residuals,

$$S = \sum_{i=1}^{n} r_i^2 = \sum_{i=1}^{n}\left(y_i - f(x_i)\right)^2$$

The **conditions** are obtained by setting each partial derivative to zero:

$$\frac{\partial S}{\partial a_0} = 0, \quad \frac{\partial S}{\partial a_1} = 0, \quad \ldots$$

which gives the **normal equations**. For the straight line $y = a + bx$:

$$\sum y = na + b\sum x, \qquad \sum xy = a\sum x + b\sum x^2$$

and in general the squares are needed because the minimum, not the root, is
sought: setting the derivatives to zero locates the stationary point of $S$, and
the second derivatives are positive there, so it is a minimum.

**The least-squares condition, stated fully.** Of all curves in the chosen family,
the least squares curve is the one for which the residuals satisfy

- $\sum r_i^2$ is a minimum, and
- $\sum r_i = 0$ (the positive and negative residuals cancel),
- $\sum x_i r_i = 0$ (the residuals are orthogonal to the regressor),

which follows directly from the two normal equations. The three conditions are
the algebraic signature of the fit: the line passes through the centroid
$(\bar x, \bar y)$, and the residuals are uncorrelated with the fitted values.

> [!info] Check against the centroid condition
> Substituting $\sum r_i = 0$ into the definition $r_i = y_i - a - bx_i$ gives
> $a = \bar y - b\bar x$, which is the intercept rewritten in terms of the slope.
> The identity holds for any data set, so it is a structural check on the normal
> equations rather than on a particular calculation.

---

### **(b) A robot arm with a rapid laser scanner is doing a quick quality check on holes drilled in a $15'' \times 10''$ rectangular plate. The centers of the holes in the plate describe the path the arm needs to take, and the hole centers are located on a Cartesian coordinate system (with the origin at the bottom left corner of the plate) given by the specifications in the table below. If the leaser is traversing from $x = 2$ to $x = 4.25$ to $x = 5.25$ in a quadratic path, what is the value of the $y$ at $x = 4.00$ using a curve fitting technique. [Marks: 06]**

The three tabulated points through which the quadratic path passes are

$$(x_0, y_0) = (2, 7.2), \qquad (x_1, y_1) = (4.25, 7.1), \qquad (x_2, y_2) = (5.25, 6.0)$$

Three points determine one quadratic, so the curve-fitting technique is exact
interpolation by a second-degree Lagrange polynomial.

**Lagrange basis.** With $x = 4.00$:

$$L_0 = \frac{(x - x_1)(x - x_2)}{(x_0 - x_1)(x_0 - x_2)} = \frac{(4 - 4.25)(4 - 5.25)}{(2 - 4.25)(2 - 5.25)} = \frac{(-0.25)(-1.25)}{(-2.25)(-3.25)}$$

$$L_0 = \frac{0.3125}{7.3125} = 0.04273504$$

$$L_1 = \frac{(x - x_0)(x - x_2)}{(x_1 - x_0)(x_1 - x_2)} = \frac{(4 - 2)(4 - 5.25)}{(4.25 - 2)(4.25 - 5.25)} = \frac{(2)(-1.25)}{(2.25)(-1)}$$

$$L_1 = \frac{-2.5}{-2.25} = 1.11111111$$

$$L_2 = \frac{(x - x_0)(x - x_1)}{(x_2 - x_0)(x_2 - x_1)} = \frac{(4 - 2)(4 - 4.25)}{(5.25 - 2)(5.25 - 4.25)} = \frac{(2)(-0.25)}{(3.25)(1)}$$

$$L_2 = \frac{-0.5}{3.25} = -0.15384615$$

**Evaluate the polynomial.**

$$y(4) = y_0 L_0 + y_1 L_1 + y_2 L_2 = 7.2(0.04273504) + 7.1(1.11111111) + 6.0(-0.15384615)$$

$$y(4) = 0.30769231 + 7.88888889 - 0.92307692 = 7.27350427$$

$$\boxed{y(4.00) = 7.2735\ \text{in.}}$$

> [!info] Check against the fitted polynomial in ordinary form
> Solving for $a, b, c$ in $y = a + bx + cx^2$ through the three points gives
> $c = -\dfrac{38}{117}$, $b = \dfrac{2323}{1170}$, $a = \dfrac{883}{195}$, so
> $y = -\dfrac{38x^2}{117} + \dfrac{2323x}{1170} + \dfrac{883}{195}$.
> Substituting $x = 4$ gives $-\dfrac{608}{117} + \dfrac{9292}{1170} + \dfrac{883}{195} = \dfrac{8510}{1170} = \dfrac{851}{117} = 7.27350427$, the
> same value. An exact fraction and a decimal evaluation agreeing to eight
> digits rules out a rounding loss in the Lagrange arithmetic. As a further
> structural check, $L_0 + L_1 + L_2 = 0.04273504 + 1.11111111 - 0.15384615 = 1$
> exactly, as a quadratic's three Lagrange basis polynomials must.

---

### **(c) Deduce the linear regression expression. [Marks: 02]**

Let the data be $(x_i, y_i)$, $i = 1, \ldots, n$, and let the fitted line be

$$\hat y = a + bx$$

The residual at point $i$ is $r_i = y_i - a - bx_i$. Minimise the sum of squared
residuals:

$$S(a, b) = \sum_{i=1}^{n}\left(y_i - a - bx_i\right)^2$$

At a minimum, both partial derivatives vanish:

$$\frac{\partial S}{\partial a} = -2\sum_{i=1}^{n}\left(y_i - a - bx_i\right) = 0 \implies \sum y_i = na + b\sum x_i$$

$$\frac{\partial S}{\partial b} = -2\sum_{i=1}^{n}x_i\left(y_i - a - bx_i\right) = 0 \implies \sum x_i y_i = a\sum x_i + b\sum x_i^2$$

These are the **normal equations**. Solving the $2 \times 2$ system:

$$na + b\sum x_i = \sum y_i$$

$$a\sum x_i + b\sum x_i^2 = \sum x_i y_i$$

Eliminating $a$ from the first, $a = \bar y - b\bar x$, and substituting into the
second:

$$\sum x_i y_i = (\bar y - b\bar x)\sum x_i + b\sum x_i^2$$

Dividing through and collecting terms in $b$:

$$b = \frac{n\sum x_i y_i - \sum x_i \sum y_i}{n\sum x_i^2 - \left(\sum x_i\right)^2}, \qquad a = \bar y - b\bar x$$

$$\boxed{y = \left(\bar y - b\bar x\right) + bx \quad\text{with}\quad b = \frac{n\sum xy - \sum x \sum y}{n\sum x^2 - \left(\sum x\right)^2}}$$

> [!info] Check against the centroid condition
> The first normal equation rearranged gives $a + b\bar x = \bar y$, so the fitted
> line passes through the point $(\bar x, \bar y)$ whatever the data. The
> intercept formula $a = \bar y - b\bar x$ is exactly this condition solved for
> $a$, so the two forms are the same statement and the deduction is internally
> consistent.

---

# SECTION B

## Question 5

### **(a) Define interpolation and extrapolation. List two general techniques of curve fitting. [Marks: 03]**

**Interpolation** is the estimation of an intermediate value of a function from a
set of known values, at a point **within** the range covered by the known data.
**Extrapolation** is the estimation of a value at a point **outside** that range.
Interpolation is bounded by the data; extrapolation extends beyond it.

The two are distinguished by the position of the target relative to the tabulated
interval. For a table covering $[x_0, x_n]$, a target $x$ with $x_0 < x < x_n$ is
interpolated; a target with $x > x_n$ or $x < x_0$ is extrapolated.
Extrapolation carries the further risk that the fitted relation may not hold
outside the range where it was fitted at all.

**Two general techniques of curve fitting**

1. **Least squares fitting.** A curve $y = a + bx + \cdots$ is fitted by choosing
   its coefficients to minimise $\sum r_i^2$, the sum of squared residuals. The
   curve does not pass through the points, but captures the trend, so it is
   appropriate for noisy data.
2. **Exact interpolation fitting.** A curve is made to pass through every tabulated
   point, using the family of methods built from divided differences and Lagrange
   polynomials. It reproduces the data exactly and is appropriate where the data
   are error-free.

Other techniques include the geometric mean, moving average and orthogonal
polynomial fits; the two above are the general ones.

---

### **(b) To verify Ohm's law, an experiment was performed and the results obtained are in the following table. Use linear interpolation to determine the current for $12\text{V}$ of supply. Explain why the result differs from actual value. [Marks: 05]**

| $V$ (volt) | 5 | 10 | 15 | 20 | 25 |
| :---: | :---: | :---: | :---: | :---: | :---: |
| $I$ (amps) | 1 | 2.1 | 3 | 4.2 | 5 |

The target $V = 12$ lies between $V_0 = 10$ and $V_1 = 15$, so the bracketing
data are $(10, 2.1)$ and $(15, 3)$.

**Linear interpolation.** The chord through the two points is

$$I(V) = I_0 + \frac{V - V_0}{V_1 - V_0}(I_1 - I_0)$$

$$I(12) = 2.1 + \frac{12 - 10}{15 - 10}(3 - 2.1) = 2.1 + \frac{2}{5}(0.9) = 2.1 + 0.36$$

$$\boxed{I(12\ \text{V}) = 2.46\ \text{A}}$$

**Why this differs from the true value.** The actual value follows Ohm's law,
$V = IR$, with the resistance from the data. The $5\ \text{V}$ and
$15\ \text{V}$ and $25\ \text{V}$ readings give $R = V/I = 5\ \Omega$ exactly,
whereas the $10\ \text{V}$ and $20\ \text{V}$ readings give $R \approx 4.76\ \Omega$.
The true current at $12\ \text{V}$ is therefore

$$I_{\text{true}} = \frac{12}{5} = 2.4\ \text{A}$$

against the interpolated $2.46\ \text{A}$, a difference of $0.06\ \text{A}$.

The cause is the data, not the method. Linear interpolation follows the chord
joining the two bracketing points, and that chord is not the Ohm's-law line: the
$10\ \text{V}$ reading carries a measurement error of $+0.1\ \text{A}$ against the
$2.0\ \text{A}$ the law predicts, so the chord from $(10, 2.1)$ to $(15, 3)$ has
slope $0.9/5 = 0.18\ \text{A/V}$ instead of the true $0.2\ \text{A/V}$. The
interpolated value inherits that slope over the whole interval from $10$ to
$15\ \text{V}$. The effect would be less at a point nearer an accurate reading,
and it would vanish if both bracketing readings were error-free.

> [!info] Check against the exact fraction
> $2.1 + \dfrac{2}{5}(0.9) = \dfrac{21}{10} + \dfrac{18}{50} = \dfrac{105}{50} + \dfrac{18}{50} = \dfrac{123}{50} = 2.46$, terminating in
> two decimals as the interpolated result does. The measured difference of
> $0.06\ \text{A}$ is $\dfrac{3}{50}$, and $2.46 - 0.06 = 2.4 = \dfrac{12}{5}$ exactly,
> so the residual between the interpolated and true value is precisely the
> propagated effect of the $0.1\ \text{A}$ error at the $10\ \text{V}$ point.

---

### **(c) Using Newton's general interpolation formula find $f(x)$ as a polynomial in $x$ for the following table. Also, determine $f(3.5)$ using the polynomial. [Marks: 04]**

| $x$ | $-1$ | 0 | 3 | 6 | 7 |
| :---: | :---: | :---: | :---: | :---: | :---: |
| $f(x)$ | 3 | $-6$ | 39 | 822 | 1611 |

**Divided differences.** Each entry is
$f[x_i, \ldots, x_{i+k}] = \dfrac{f[x_{i+1}, \ldots, x_{i+k}] - f[x_i, \ldots, x_{i+k-1}]}{x_{i+k} - x_i}$.

| Order | Values |
| :---: | :--- |
| 0 | $3,\ -6,\ 39,\ 822,\ 1611$ |
| 1 | $\dfrac{-6-3}{0-(-1)} = -9$; $\dfrac{39-(-6)}{3-0} = 15$; $\dfrac{822-39}{6-3} = 261$; $\dfrac{1611-822}{7-6} = 789$ |
| 2 | $\dfrac{15-(-9)}{3-(-1)} = 6$; $\dfrac{261-15}{6-0} = 41$; $\dfrac{789-261}{7-3} = 132$ |
| 3 | $\dfrac{41-6}{6-(-1)} = 5$; $\dfrac{132-41}{7-0} = 13$ |
| 4 | $\dfrac{13-5}{7-(-1)} = 1$ |

**Newton's general (divided difference) form.**

$$f(x) = f[x_0] + f[x_0, x_1](x - x_0) + f[x_0, x_1, x_2](x - x_0)(x - x_1) + \cdots$$

$$f(x) = 3 - 9(x + 1) + 6(x + 1)x + 5(x + 1)x(x - 3) + (x + 1)x(x - 3)(x - 6)$$

**Expand to a polynomial in $x$.** Working outward from the last term:

$$(x + 1)x(x - 3)(x - 6) = x^4 - 8x^3 + 9x^2 + 18x$$

$$5(x + 1)x(x - 3) = 5(x^3 - 2x^2 - 3x) = 5x^3 - 10x^2 - 15x$$

$$6(x + 1)x = 6x^2 + 6x, \qquad -9(x + 1) = -9x - 9$$

Collecting all terms:

$$f(x) = x^4 - 3x^3 + 5x^2 - 6$$

$$\boxed{f(x) = x^4 - 3x^3 + 5x^2 - 6}$$

**Apply it to $f(3.5)$.** Substituting into the expanded form:

$$f(3.5) = 150.0625 - 128.625 + 61.25 - 6 = 76.6875$$

$$\boxed{f(3.5) = 76.6875}$$

> [!info] Check against the Newton form and the tabulated values
> Substituting $x = 3.5$ into the unevaluated Newton form gives
> $3 - 9(4.5) + 6(15.75) + 5(7.875) + (-19.6875) = 76.6875$, the same value by a
> second route. And substituting the polynomial back into the tabulated
> abscissae reproduces every printed entry: $f(-1) = 1 + 3 + 5 - 6 = 3$,
> $f(0) = -6$, $f(3) = 81 - 81 + 45 - 6 = 39$, $f(6) = 1296 - 648 + 180 - 6 = 822$,
> and $f(7) = 2401 - 1029 + 245 - 6 = 1611$. The table is recovered exactly, so
> the polynomial is the interpolation polynomial and no tabulated value is
> contradicted.

---

## Question 6

### **(a) What is the basis of numerical differentiation? Write at least four difference equations to obtain numerical differentiation. [Marks: 04]**

**The basis.** A function known only at discrete points is replaced by a
polynomial that passes through those points, and the derivative of that
polynomial is used for the derivative of the function. Starting from the Taylor
series

$$f(x + h) = f(x) + hf'(x) + \frac{h^2}{2}f''(x) + \frac{h^3}{6}f'''(x) + \cdots$$

combinations of the series at neighbouring points cancel the terms that are not
wanted. Since the first omitted term is proportional to a power of $h$, the
result is an approximation with an error $O(h)$ or $O(h^2)$.

**Four difference equations.** With $h$ the tabular spacing and $f_n = f(x_n)$:

1. **Forward difference (two-point).**
$$f'(x_n) = \frac{f_{n+1} - f_n}{h}, \qquad \text{error } O(h)$$

2. **Backward difference (two-point).**
$$f'(x_n) = \frac{f_n - f_{n-1}}{h}, \qquad \text{error } O(h)$$

3. **Central difference (three-point).**
$$f'(x_n) = \frac{f_{n+1} - f_{n-1}}{2h}, \qquad \text{error } O(h^2)$$

4. **Forward difference (three-point).**
$$f'(x_n) = \frac{-3f_n + 4f_{n+1} - f_{n+2}}{2h}, \qquad \text{error } O(h^2)$$

5. **Central difference (five-point).**
$$f'(x_n) = \frac{f_{n-2} - 8f_{n-1} + 8f_{n+1} - f_{n+2}}{12h}, \qquad \text{error } O(h^4)$$

The central formulas are preferred where data exist on both sides, since their
error is $O(h^2)$ and above rather than $O(h)$, and their error constants are
smaller by the same factor.

---

### **(b) A 1 Henry inductance gets current through it at different times as follows. Obtain the voltage across it at $t = 0.27\text{ sec}$ using numerical differentiation. [Marks: 05]**

| $t$ (sec) | 0.25 | 0.26 | 0.27 | 0.28 | 0.29 |
| :---: | :---: | :---: | :---: | :---: | :---: |
| $I$ (amp) | 0.2474 | 0.2571 | 0.2667 | 0.2764 | 0.2860 |

The tabular spacing is $h = 0.01$. The target $t = 0.27$ has two points on each
side, so the five-point central formula is available and is the most accurate.

**Five-point central difference.**

$$f'(x_n) = \frac{f_{n-2} - 8f_{n-1} + 8f_{n+1} - f_{n+2}}{12h}$$

With $f_{n-2} = 0.2474$, $f_{n-1} = 0.2571$, $f_{n+1} = 0.2764$, $f_{n+2} = 0.2860$:

$$\left.\frac{dI}{dt}\right|_{t = 0.27} = \frac{0.2474 - 8(0.2571) + 8(0.2764) - 0.2860}{12(0.01)}$$

$$\frac{dI}{dt} = \frac{0.2474 - 2.0568 + 2.2112 - 0.2860}{0.12} = \frac{0.1158}{0.12} = 0.965$$

**Voltage across the inductor.** For $L = 1\ \text{H}$, $v = L\dfrac{dI}{dt}$:

$$v = 1 \times 0.965 = 0.965\ \text{V}$$

$$\boxed{v(0.27) = 0.965\ \text{V}}$$

> [!info] Check by the three-point central formula
> The three-point central formula gives $\dfrac{I_{n+1} - I_{n-1}}{2h} = \dfrac{0.2764 - 0.2571}{0.02} = \dfrac{0.0193}{0.02} = 0.965$, the
> same value to four digits. The first differences of the tabulated current are
> $0.0097, 0.0096, 0.0097, 0.0096$, averaging $0.00965$, which is the same slope
> observed over the whole span. Three agreeing estimates at two different orders
> of accuracy indicate the data are locally straight and the derivative is not
> dominated by the rounding of the fourth decimal.
>
> The one-sided formulas are less reliable here. The two-point forms, which are
> $O(h)$, give $0.970$ forward and $0.960$ backward. The three-point one-sided
> forms, which are $O(h^2)$, give $0.975$ forward and $0.955$ backward. Either pair
> straddles the true value with a spread of $\pm 0.01$, which is the truncation
> error of those formulas rather than any disagreement about the value itself.

---

### **(c) Discuss trapezoidal rule of numerical integration. [Marks: 03]**

The **trapezoidal rule** approximates $\int_a^b f(x)\,dx$ by replacing the curve
with a straight line joining the endpoints of each subinterval, so the area under
the curve becomes the area of a set of trapezoids.

**Derivation.** Over one interval $[x_0, x_0 + h]$, the straight line through
$(x_0, f_0)$ and $(x_1, f_1)$ has slope $\dfrac{f_1 - f_0}{h}$, and its integral
is

$$\int_{x_0}^{x_1} f(x)\,dx \approx \frac{h}{2}(f_0 + f_1)$$

**Composite rule.** Over $[a, b]$ with $n$ subintervals of width
$h = \dfrac{b - a}{n}$, summing the one-interval result gives

$$\int_a^b f(x)\,dx \approx \frac{h}{2}\left[f_0 + 2f_1 + 2f_2 + \cdots + 2f_{n-1} + f_n\right]$$

$$\boxed{\int_a^b f(x)\,dx \approx \frac{h}{2}\left[f(a) + f(b) + 2\sum_{i=1}^{n-1}f_i\right]}$$

**Error.** The error over one interval is $-\dfrac{h^3}{12}f''(\xi)$, so the
composite error is

$$E = -\frac{(b - a)h^2}{12}f''(\xi), \qquad O(h^2)$$

**Properties.**

1. First order of accuracy: halving $h$ reduces the error by a factor of four.
2. The rule is exact for a straight line, and over-shoots for a curve that
   is concave up, since the chord lies above the curve.
3. It is the basis of the trapezoidal rule for sampled data, where the area of a
   measured record is obtained with no requirement that the samples be equally
   spaced in value.
4. Its ease of use makes it the obvious first estimate, but Simpson's rules are
   preferred when smoothness and accuracy are required.

---

## Question 7

### **(a) Derive Simpson's one-third rule and hence show that the rule is exact up to degree three. [Marks: 04]**

**Derivation.** Take three equally spaced nodes

$$x_0,\qquad x_1 = x_0 + h,\qquad x_2 = x_0 + 2h$$

and replace $f$ by the quadratic $P_2(x)$ through the three values $f_0, f_1,
f_2$. The integral of $P_2$ is the approximation.

With $x = x_0 + ph$, so $dx = h\,dp$, the Lagrange basis is

$$L_0 = \frac{(p - 1)(p - 2)}{2}, \qquad L_1 = -p(p - 2), \qquad L_2 = \frac{p(p - 1)}{2}$$

and

$$\int_{x_0}^{x_2} P_2\,dx = h\int_0^2 \left[f_0\frac{(p-1)(p-2)}{2} - f_1 p(p-2) + f_2\frac{p(p-1)}{2}\right]dp$$

Integrating each basis function separately:

$$\int_0^2 \frac{(p-1)(p-2)}{2}dp = \frac{1}{2}\int_0^2(p^2 - 3p + 2)dp = \frac{1}{2}\left[\frac{8}{3} - 6 + 4\right] = \frac{1}{2}\cdot\frac{2}{3} = \frac{1}{3}$$

$$\int_0^2 -p(p - 2)\,dp = -\int_0^2(p^2 - 2p)dp = -\left[\frac{8}{3} - 4\right] = \frac{4}{3}$$

$$\int_0^2 \frac{p(p-1)}{2}dp = \frac{1}{2}\int_0^2(p^2 - p)dp = \frac{1}{2}\left[\frac{8}{3} - 2\right] = \frac{1}{2}\cdot\frac{2}{3} = \frac{1}{3}$$

Hence

$$\int_{x_0}^{x_2} f(x)\,dx \approx \frac{h}{3}\left(f_0 + 4f_1 + f_2\right)$$

which is **Simpson's one-third rule**. Over $[a, b]$ with $n$ even and
$h = \dfrac{b-a}{n}$, the composite form is

$$\int_a^b f(x)\,dx \approx \frac{h}{3}\left[f_0 + 4f_1 + 2f_2 + 4f_3 + \cdots + 2f_{n-2} + 4f_{n-1} + f_n\right]$$

**Exactness to degree three.** By construction the rule is exact for every
quadratic, since $P_2 = f$. For a cubic, apply the rule to
$f(x) = x^3$ on $[-h, h]$, which by symmetry is equivalent to any interval:

$$\int_{-h}^{h}x^3\,dx = \left[\frac{x^4}{4}\right]_{-h}^{h} = 0$$

$$\frac{h}{3}\left[(-h)^3 + 4(0)^3 + (h)^3\right] = \frac{h}{3}(-h^3 + h^3) = 0$$

The two agree. The cause is symmetry: for a cubic antisymmetric about the
midpoint, both the true integral and the weighted sum vanish identically, and
each weighted sum reproduces the exact area because the weights $1, 4, 1$ were
themselves derived from exact integration of the quadratic basis. Hence the rule
is exact for $1, x, x^2, x^3$.

**Failure at degree four.** For $f(x) = x^4$ on $[-h, h]$:

$$\int_{-h}^{h}x^4\,dx = \frac{2h^5}{5}, \qquad \frac{h}{3}\left(h^4 + 0 + h^4\right) = \frac{2h^5}{3}$$

and $\dfrac{2}{3} \ne \dfrac{2}{5}$, so the rule is not exact for quartics.

$$\boxed{\int_{x_0}^{x_2} f\,dx \approx \frac{h}{3}(f_0 + 4f_1 + f_2)\ \text{exact for all polynomials of degree}\ \le 3}$$

---

### **(b) Evaluate, $\int_1^2 (x^2 + 1) \, dx$ using Simpson's 3/8 rule. [Marks: 04]**

Simpson's **3/8 rule** applies over three subintervals, using four nodes. Over
$[1, 2]$, take $n = 3$, so

$$h = \frac{2 - 1}{3} = \frac{1}{3}, \qquad x = 1,\ \frac{4}{3},\ \frac{5}{3},\ 2$$

The ordinates:

$$f(1) = 1 + 1 = 2$$

$$f\!\left(\frac{4}{3}\right) = \frac{16}{9} + 1 = \frac{25}{9} \approx 2.777778$$

$$f\!\left(\frac{5}{3}\right) = \frac{25}{9} + 1 = \frac{34}{9} \approx 3.777778$$

$$f(2) = 4 + 1 = 5$$

$$\int_1^2(x^2 + 1)\,dx \approx \frac{3h}{8}\left[f_0 + 3f_1 + 3f_2 + f_3\right]$$

$$= \frac{3}{8}\cdot\frac{1}{3}\left[2 + 3\left(\frac{25}{9}\right) + 3\left(\frac{34}{9}\right) + 5\right]$$

$$= \frac{1}{8}\left[2 + \frac{25}{3} + \frac{34}{3} + 5\right] = \frac{1}{8}\left[7 + \frac{59}{3}\right] = \frac{1}{8}\cdot\frac{80}{3} = \frac{10}{3}$$

$$\boxed{\int_1^2(x^2 + 1)\,dx = \frac{10}{3} = 3.3333}$$

> [!info] Check by direct integration
> Antidifferentiating, $\int_1^2(x^2+1)dx = \left[\dfrac{x^3}{3} + x\right]_1^2 = \left(\dfrac{8}{3} + 2\right) - \left(\dfrac{1}{3} + 1\right) = \dfrac{7}{3} + 1 = \dfrac{10}{3}$, exactly
> the value the rule returns. The rule integrates cubics exactly and the
> integrand is only quadratic, so agreement is the expected outcome rather than a
> coincidence; the check confirms that the subinterval count was set to $3$ as
> the $3/8$ rule requires and that no weight was mistyped. Had the interval been
> left as one subinterval with $h = 1$, the four-node formula could not be
> applied at all, which is the error to avoid when the limits give a single
> interval.

---

### **(c) Discuss Euler's method to solve ordinary differential equations. [Marks: 04]**

**Purpose.** Given $y' = f(x, y)$ and $y(x_0) = y_0$, the value of $y$ is wanted
at $x_0 + nh$ for a step size $h$.

**Derivation.** Taylor expand about $x_n$:

$$y_{n+1} = y_n + hy'_n + \frac{h^2}{2}y''_n + \cdots$$

**Euler's method** keeps the first two terms and discards the rest:

$$y_{n+1} = y_n + hf(x_n, y_n)$$

Geometrically, $y_{n+1}$ is the value at $x_n + h$ of the tangent to the solution
curve at $(x_n, y_n)$, so the solution is followed along successive short tangent
segments.

**Procedure.** Set $x_{n+1} = x_n + h$. Starting from $(x_0, y_0)$, compute
$y_1 = y_0 + hf(x_0, y_0)$, then $y_2 = y_1 + hf(x_1, y_1)$, and continue.

**Error.** The local truncation error is $O(h^2)$ per step, from the discarded
$\dfrac{h^2}{2}y''$ term; over $n$ steps these accumulate into a global error
$O(h)$. Halving $h$ therefore halves the global error, which is the defining
property of a first-order method.

**Merits and demerits.**

1. Simple: one evaluation of $f$ per step, and no derivative of $f$ is needed.
2. Stable only for a sufficiently small $h$ on a stiff equation, because the
   method follows the tangent rather than the curve.
3. Inexact: the global error falls only linearly in $h$, so high accuracy
   requires many steps.
4. It is the foundation of the higher methods: Heun, the mid-point method, and
   the Runge–Kutta family all correct Euler's $\dfrac{h^2}{2}y''$ term.

$$\boxed{y_{n+1} = y_n + h\,f(x_n, y_n), \qquad \text{global error } O(h)}$$

---

## Question 8

### **(a) Given, $\frac{dy}{dx} = x^2 + y^2$ where $y = 0$ when $x = 0$. Find $y(0.4)$ assuming $h = 0.2$. [Marks: 06]**

**Step 1.** $x_0 = 0$, $y_0 = 0$.

$$f(x_0, y_0) = x_0^2 + y_0^2 = 0 + 0 = 0$$

$$y_1 = y_0 + h\,f(x_0, y_0) = 0 + 0.2(0) = 0$$

Hence $x_1 = 0.2$ and $y_1 = 0$.

**Step 2.** $x_1 = 0.2$, $y_1 = 0$.

$$f(x_1, y_1) = (0.2)^2 + 0^2 = 0.04$$

$$y_2 = y_1 + h\,f(x_1, y_1) = 0 + 0.2(0.04) = 0.008$$

Hence $x_2 = 0.4$ and $y_2 = 0.008$.

| Step | $x_n$ | $y_n$ | $f(x_n, y_n) = x_n^2 + y_n^2$ | $y_{n+1} = y_n + 0.2f$ |
| :--: | :--: | :--: | :--: | :--: |
| 0 | 0 | 0 | 0 | 0 |
| 1 | 0.2 | 0 | 0.04 | 0.008 |

$$\boxed{y(0.4) \approx 0.008}$$

> [!info] Check against an independent route
> Iterating the integral equation gives the Picard series
> $y(x) = \dfrac{x^3}{3} + \dfrac{x^7}{63} + \cdots$, from which
> $y(0.4) \approx \dfrac{0.064}{3} + \dfrac{0.0016384}{63} = 0.021359$. Euler's
> $0.008$ is well short of this, and the reason is the method, not the
> arithmetic. Euler's error per step is $O(h^2)$ and the solution has
> $y' = x^2 + y^2$ with $y''(0) = 2$, so the discarded $\dfrac{h^2}{2}y''$ alone
> is $\dfrac{0.04}{2}\cdot 2 = 0.04$ at the first step. A step of $h = 0.2$ is
> simply too coarse for this equation; the observation that Euler under-reads by
> roughly the local truncation term is the useful diagnostic when a computed
> value is compared against an exact or series solution.

---

### **(b) Solve the Laplace's equation for the square region shown in the following figure, the boundary values being indicated in the figure. [Marks: 06]**

**The mesh.** A uniform $3\times3$ mesh over the square, with four interior nodes
$u_1, u_2, u_3, u_4$ and the boundary values shown.

```text
                Y
                |       1       2       B
             C  +-------+-------+-------+
                |       |       |       |
                |       |  u₃   |  u₄   |
                |       |       |       |
             1  +-------+-------+-------+  4
                |       |       |       |
                |       |  u₁   |  u₂   |
                |       |       |       |
             2  +-------+-------+-------+  5
                |       |       |       |
                |       |       |       |
                +-------+-------+-------+---------> X
                0       4       5       A
```

**The standard Laplace finite-difference stencil.** For a square mesh with
uniform spacing $h$, $\nabla^2 u = 0$ gives

$$\frac{u_{i+1,j} - 2u_{i,j} + u_{i-1,j}}{h^2} + \frac{u_{i,j+1} - 2u_{i,j} + u_{i,j-1}}{h^2} = 0$$

and cancelling $h^2$:

$$u_{i,j} = \frac{1}{4}\left(u_{i+1,j} + u_{i-1,j} + u_{i,j+1} + u_{i,j-1}\right)$$

**The four nodal equations.** Reading the neighbours of each interior node from
the figure, and taking the boundary values in the order left, right, top, bottom:

$$u_1 = \frac{1}{4}\left(u_2 + u_3 + 4 + 2\right)$$

$$4u_1 - u_2 - u_3 = 6$$

$$u_2 = \frac{1}{4}\left(u_1 + u_4 + 5 + 5\right)$$

$$4u_2 - u_1 - u_4 = 10$$

$$u_3 = \frac{1}{4}\left(u_1 + u_4 + 1 + 1\right)$$

$$4u_3 - u_1 - u_4 = 2$$

$$u_4 = \frac{1}{4}\left(u_3 + u_2 + 2 + 4\right)$$

$$4u_4 - u_3 - u_2 = 6$$

**Solve the $4\times4$ system.**

$$4u_1 - u_2 - u_3 = 6$$
$$-u_1 + 4u_2 - u_4 = 10$$
$$-u_1 + 4u_3 - u_4 = 2$$
$$-u_3 - u_2 + 4u_4 = 6$$

Writing this as a matrix,

$$\begin{bmatrix} 4 & -1 & -1 & 0 \\ -1 & 4 & 0 & -1 \\ -1 & 0 & 4 & -1 \\ 0 & -1 & -1 & 4 \end{bmatrix} \begin{bmatrix} u_1 \\ u_2 \\ u_3 \\ u_4 \end{bmatrix} = \begin{bmatrix} 6 \\ 10 \\ 2 \\ 6 \end{bmatrix}$$

**Step 1. One relation from subtracting.** Equation 3 minus equation 2 cancels both
$u_1$ and $u_4$:

$$4u_3 - 4u_2 = -8 \implies u_3 = u_2 - 2$$

**Step 2. One relation from adding.** Adding all four, every column sums to $2$:

$$2(u_1 + u_2 + u_3 + u_4) = 24 \implies u_1 + u_2 + u_3 + u_4 = 12$$

**Step 3. Substitute $u_3 = u_2 - 2$** into that sum:

$$u_1 + 2u_2 + u_4 = 14, \quad u_4 = 14 - u_1 - 2u_2$$

**Step 4. Use equation 2.** Substituting that $u_4$ into $-u_1 + 4u_2 - u_4 = 10$:

$$-u_1 + 4u_2 - 14 + u_1 + 2u_2 = 10 \implies 6u_2 = 24 \implies u_2 = 4$$

Here $u_3 = 2$ and $u_4 = 6 - u_1$. Equation 1 then gives
$4u_1 - 4 - 2 = 6$, hence $u_1 = 3$ and $u_4 = 3$.

Every value is an integer, which is not a coincidence: the boundary data are
integers and the mesh is small, so the solution is a small rational that happens to
be integral.

$$\boxed{u_1 = 3, \qquad u_2 = 4, \qquad u_3 = 2, \qquad u_4 = 3}$$

> [!info] Check against the individual nodal equations
> Substituting into the four nodal equations directly:
> $4(3) - 4 - 2 = 6$ ✓; $-(3) + 4(4) - 3 = 10$ ✓;
> $-(3) + 4(2) - 3 = 2$ ✓; $-(2) - 4 + 4(3) = 6$ ✓. All four hold exactly.
> The values also insert into the difference form consistently,
> $u_1 = \tfrac{1}{4}(2 + 4 + 4 + 2) = 3$ and
> $u_3 = \tfrac{1}{4}(1 + 1 + 3 + 3) = 2$, in each case the mean of the four
> neighbours as the Laplace stencil requires. That the solution is a set of small
> integers when the boundary data are also integers is a property of this
> particular mesh, and it is itself a strong check: a wrong neighbour would leave
> a residual of order one-tenth rather than zero.

> [!info] Check by Gauss-Seidel iteration
> Taking the iteration form $u\leftarrow\tfrac{1}{4}(\text{sum of four neighbours})$
> and starting from $u_1 = u_2 = u_3 = u_4 = 0$ gives $1.500, 2.875, 0.875, 2.438$
> on the first iteration, then $2.438, 3.719, 1.719, 2.859$, then
> $2.859, 3.930, 1.930, 2.965$, approaching $3, 4, 2, 3$ as the iteration count
> rises, with the residual falling at each sweep. The coefficient matrix has
> diagonal $4$ and off-diagonal sum $2$, so it is strictly diagonally dominant
> and convergence is guaranteed. The iteration and the direct elimination agree
> on the same target, which is the independent confirmation of the solution.

---
