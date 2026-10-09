---
title: "ECE 2213 · 2018 Exam Style Answers"
tags:
  - numerical-methods
  - discrete-mathematics
  - previous-year
---

# ECE 2213: 2018 Semester Final · Exam Style Answers

**RUET · ECE Dept · B.Sc. Engineering 2nd Year Even Semester Examination, 2018**
**Full Marks:** 96 · **Time:** 03 Hours

> [!info] Format
> Concise, mark-aligned, written as an answer script.
> Question text and marks come from the paper:
> [[2018|the 2018 paper]].
> Every numerical here was derived twice by independent routes. Where the two
> routes disagreed, the disagreement was settled before the next question was
> written, and the divergence is recorded in a callout.
>
> This is a pre-OBE paper, so there is **no CLO column**. Marks only.

---

# SECTION A

## Question 1

### **(a) What are the importances of numerical techniques in engineering? Briefly discuss. [Marks: 04]**

A numerical technique obtains the answer of a mathematical problem as a finite
sequence of arithmetic operations. Its importance in engineering rests on four
points.

**1. Problems with no closed form.** Most engineering problems have no
elementary solution. The integral $\int e^{-x^2}dx$, the potential in a
transistor region, and the motion of three bodies under mutual gravity all
require numerical treatment, and all three arise in practice. Where an exact
formula exists at all, it is often so long that evaluation is slower and less
accurate than a numerical scheme.

**2. Only arithmetic executes on a machine.** A numerical technique converts a
problem into additions, multiplications, comparisons and divisions, which is
exactly what a computer or a microprocessor performs. This is what turns an
analytic method into something that runs on hardware, and it is the reason
numerical techniques accompany every physical engineering discipline.

**3. Experimental and tabulated data must be used.** Measured data arrive as
discrete samples. Any quantity derived from them, whether a derivative, an
integral, a regression line or a filter output, is obtained numerically. An
engineer working from a data sheet is doing numerical analysis whether or not
the word appears.

**4. Design and optimisation are iterative.** Matching, cut-off placement,
bias-point selection and root finding are all performed by repeated
improvement of an estimate. Numerical techniques supply the estimate rule,
the stopping test and the error estimate that make iteration trustworthy.

The consequence is that a numerical technique is judged not only on whether it
converges, but on its cost, its stability, and how its error grows with the
number of operations. All three are what the analysis below develops.

---

### **(b) What are the algorithmic errors that may occur in numerical calculation? [Marks: 04]**

Algorithmic error is the error introduced by the computation itself, as opposed
to that already present in the data. It has three sources.

**1. Truncation error.** Every numerical method approximates an infinite process
by a finite one: an infinite series is cut after $n$ terms, an interval is cut
into $n$ panels, a differential equation is stepped with finite $h$. The
discarded remainder is the truncation error, and it is the error that decreases
as the approximation is refined.

**2. Round-off error.** A computer holds only a finite number of digits. Every
arithmetic operation rounds its result to that precision, and the rounding
introduced at one step propagates into every later step. Round-off error
grows with the number of operations, and is the reason a method may become
*less* accurate when refined too far.

**3. Propagation of error.** The two above do not simply add. A method is
**unstable** if an error introduced early is amplified in later steps, and
**well-conditioned** if it is damped. The amplification factor is a property of
the algorithm, not of the arithmetic precision.

**The two errors oppose each other.** For a method with step size $h$,
truncation error falls as a power of $h$ while round-off error grows with
$1/h$ (or worse, if the algorithm is unstable). The total error therefore has a
minimum at some optimal $h$, below which further refinement makes the answer
worse. This is the central practical fact of numerical computation, and it is
why the choice of $h$, the stopping test and the stability of the recurrence
are all parts of the method rather than details of implementation.

---

### **(c) Find the number of terms in the exponential series such that their sum gives the value of $e^x$ correct to five decimal places for all values of $x$ in the range $0 \le x \le 1$. [Marks: 04]**

**The series and its remainder.** For $0 \le x \le 1$,

$$e^x = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \cdots + \frac{x^n}{n!} + \cdots$$

After $k$ terms the remainder is, by Taylor's theorem with Lagrange form,

$$R_k = \frac{e^{\xi}x^k}{k!}, \qquad 0 < \xi < x$$

Since $0 \le x \le 1$ and $e^{\xi} \le e$, the largest possible remainder is
attained at $x = 1$ and

$$|R_k| \le \frac{e}{k!} = \frac{2.718282}{k!}$$

"Correct to five decimal places" requires the error to be below
$0.5 \times 10^{-5}$.

**Test $k$.** Taking the successive values:

| $k$ | Tail bound $\dfrac{1}{k!}\dfrac{k+1}{k}$ | Verdict |
| :--: | :-- | :-- |
| 8 | $\dfrac{1}{40320}\left(\dfrac{9}{8}\right) = 2.786 \times 10^{-5}$ | too large |
| 9 | $\dfrac{1}{362880}\left(\dfrac{10}{9}\right) = 3.062 \times 10^{-6}$ | below $5\times10^{-6}$ |

Hence the remainder tail is bounded by
$R_9 \le 3.062 \times 10^{-6} < 0.5 \times 10^{-5}$, which certifies 9 terms.

**Direct check at the worst point $x = 1$.** Summing the first nine terms:

$$S_9 = 1 + 1 + \frac{1}{2!} + \frac{1}{3!} + \frac{1}{4!} + \frac{1}{5!} + \frac{1}{6!} + \frac{1}{7!} + \frac{1}{8!}$$

$$S_9 = 2 + 0.5 + 0.166667 + 0.041667 + 0.008333 + 0.001389 + 0.000198 + 0.0000248$$

$$S_9 = 2.71827877$$

and $e = 2.71828183$, so the actual error is

$$|e - S_9| = 3.06 \times 10^{-6} < 0.5 \times 10^{-5}$$

With eight terms $S_8 = 2.71825397$, giving $|e - S_8| = 2.79 \times 10^{-5}$,
which is too large. Nine terms are therefore sufficient, and eight are not.

$$\boxed{9\ \text{terms}}$$

> [!info] Check by the Lagrange bound and exact tail
> The error after nine terms is the tail $R_9 = \sum_{n=9}^{\infty}\dfrac{1}{n!}$.
> Since $\dfrac{1}{9!} = 2.7557\times10^{-6}$ and the tail is bounded by
> $\dfrac{1}{9!}\left(1 + \dfrac{1}{10} + \dfrac{1}{10\cdot11} + \cdots\right) < \dfrac{10}{9\cdot9!} = 3.062\times10^{-6}$,
> the exact error $3.06\times10^{-6}$ clears the tolerance $0.5\times10^{-5}$ cleanly.
> Note that the cruder Lagrange bound $\dfrac{e}{k!}$ gives $\dfrac{e}{9!} = 7.491\times10^{-6}$,
> which exceeds $5\times10^{-6}$ only because $e \approx 2.718$ is a loose bound for $e^\xi$ on $[0,1]$;
> the exact geometric tail certifies that nine terms clear the tolerance while eight do not.

---

## Question 2

### **(a) Develop an algorithm to calculate the root of any non-linear equation by bisection method. [Marks: 04]**

**Bisection** solves $f(x) = 0$ on an interval $[a, b]$ in which $f$ changes
sign, by repeatedly halving the interval and retaining the half that still
contains the sign change.

**Algorithm.**

1. Read $f(x)$, the tolerance $\varepsilon$, and the maximum iteration count $N$.
2. Accept the ends $a$ and $b$ of the bracketing interval.
3. Compute $f(a)$ and $f(b)$. If $f(a)f(b) > 0$, report that the interval does
   not bracket a root and stop.
4. Set $c = \dfrac{a + b}{2}$ and compute $f(c)$.
5. Test for convergence. If $|f(c)| < \varepsilon$, or if
   $|b - a| < \varepsilon$, accept $c$ as the root and stop.
6. If $f(a)f(c) < 0$, set $b = c$; otherwise set $a = c$.
7. If the iteration count exceeds $N$, report non-convergence and stop.
   Otherwise return to step 4.

**Convergence.** After $n$ bisections the interval has width $\dfrac{b-a}{2^n}$,
and the error in the midpoint is at most $\dfrac{b-a}{2^{n+1}}$. Halving the
interval therefore halves the error, and the number of iterations needed for
error below $\varepsilon$ is

$$n = \left\lceil \log_2\frac{b-a}{\varepsilon}\right\rceil$$

**Merits and demerits.** The method is guaranteed to converge whenever the
initial interval brackets a root and $f$ is continuous, and the error is known
in advance. It requires only one evaluation of $f$ per step. Its drawbacks are
that convergence is slow compared with Newton or regula falsi, that the number
of iterations is fixed by the tolerance rather than by the shape of $f$, and
that a bracketing interval must be found first.

---

### **(b) Derive the expression of the next approximation of a root of the non-linear function $f(x) = 0$ using regula-falsi method. [Marks: 04]**

**Setup.** Let $x_0$ and $x_1$ be two points with $f(x_0)f(x_1) < 0$, so that a
root lies between them. Write $f_0 = f(x_0)$ and $f_1 = f(x_1)$.

**The idea.** Replace $f$ on $[x_0, x_1]$ by the straight line through
$(x_0, f_0)$ and $(x_1, f_1)$, and take the intercept of that line with the
$x$-axis as the next approximation.

**Derivation.** The equation of the chord is

$$\frac{y - f_0}{f_1 - f_0} = \frac{x - x_0}{x_1 - x_0}$$

The chord meets the $x$-axis at $y = 0$. Writing the next approximation as
$x_2$ and setting $y = 0$:

$$\frac{-f_0}{f_1 - f_0} = \frac{x_2 - x_0}{x_1 - x_0}$$

$$x_2 - x_0 = \frac{-f_0(x_1 - x_0)}{f_1 - f_0}$$

$$\boxed{x_2 = x_0 - \frac{f_0(x_1 - x_0)}{f_1 - f_0}}$$

**Equivalent forms.** Expanding the numerator:

$$x_2 = \frac{x_0f_1 - x_1f_0}{f_1 - f_0}$$

which shows that $x_2$ is a weighted average of $x_0$ and $x_1$, the weights
being the opposing function values. A third form places the unknown on one side:

$$x_2 = \frac{x_0f_1 - x_1f_0}{f_1 - f_0} = \frac{f_1x_0 - f_0x_1}{f_1 - f_0}$$

**Continuing.** Once $x_2$ is computed, $f(x_2)$ is evaluated and either $x_0$
or $x_1$ is replaced by $x_2$, retaining the sub-interval in which the sign
change occurs. The same formula is then applied again.

**Note on convergence.** The method always converges whenever the initial pair
brackets the root, since the sign change is preserved. Convergence is linear,
and is faster than bisection, because the chord is a better model of $f$ than
the midpoint. A drawback is that one end of the bracket may stall, in which
case the interval shrinks very slowly; this is the weakness the Illinois
modification is designed to repair.

---

### **(c) Find the real root of the equation $x \sin x + \cos x = 0$ using N-R method. [Marks: 04]**

**The function and its derivative.** Write

$$f(x) = x\sin x + \cos x$$

$$f'(x) = \frac{d}{dx}(x\sin x) + \frac{d}{dx}(\cos x) = (\sin x + x\cos x) - \sin x = x\cos x$$

The $\sin x$ terms cancel, which leaves the simple form $f'(x) = x\cos x$.

**Sign check for the starting value.** Evaluating $f$ at a few points:

| $x$ | $f(x) = x\sin x + \cos x$ |
| :--: | :-- |
| 2.0 | $2(0.90930) + (-0.41615) = 1.40245$ |
| 2.5 | $2.5(0.59847) + (-0.80114) = 0.69504$ |
| 3.0 | $3(0.14112) + (-0.98999) = -0.56663$ |

The sign changes between $2.5$ and $3.0$, so a root lies in that interval.
Take $x_0 = 3$.

**Newton–Raphson iteration.** With

$$x_{n+1} = x_n - \frac{x_n\sin x_n + \cos x_n}{x_n\cos x_n}$$

| $n$ | $x_n$ | $f(x_n)$ | $f'(x_n) = x_n\cos x_n$ | $x_{n+1}$ |
| :--: | :-- | :-- | :-- | :-- |
| 0 | $3.0000000$ | $-0.56663$ | $-2.96998$ | $2.8092132$ |
| 1 | $2.8092132$ | $-0.02864$ | $-2.65546$ | $2.7984273$ |
| 2 | $2.7984273$ | $-1.087\times10^{-4}$ | $-2.63526$ | $2.7983860$ |

The correction at the last step is $4.1 \times 10^{-5}$, already below
$10^{-4}$, so the value is accepted.

$$\boxed{x = 2.7984}$$

**Physical reading.** The equation $x\sin x + \cos x = 0$ rearranges to
$x = -\cot x$, so the root is the first positive point at which the line
$y = x$ meets the curve $y = -\cot x$. There is one such point near $2.80$,
which is the value found.

> [!info] Check by substitution and by a second start
> Substituting $x = 2.7983860$: $\sin x = 0.33651$, $\cos x = -0.94168$, so
> $f = 2.7983860(0.33651) + (-0.94168) = 0.94168 - 0.94168 = -1.2\times10^{-7}$, which is zero
> to the seven digits the root is quoted to. The correction at the final step,
> $2.7984273 - 2.7983860 = 4.1\times10^{-5}$, is consistent with that residual.
> Running the same iteration from $x_0 = 2.6$ instead of $3$ gives $2.7983860$ at
> the third step, so the root does not depend on the start within the bracket.
> The two starts agreeing is the confirmation that the iteration has settled on
> the root of this equation rather than on a stationary point of the iteration
> itself.

---

## Question 3

### **(a) Explain the use of Lagrange's interpolation formula. [Marks: 02]**

**Use.** Lagrange's formula estimates an intermediate value $f(x)$ at a point
$x$ within the range of a tabulated set $(x_i, f_i)$, without requiring the
tabulated abscissae to be equally spaced.

**The formula.** For $n+1$ points,

$$f(x) \approx \sum_{i=0}^{n} f_i \prod_{\substack{j=0 \\ j \ne i}}^{n}\frac{x - x_j}{x_i - x_j}$$

**Why it is used.**

1. **Unequal spacing is allowed.** This is its principal advantage over
   Newton's formulas, which assume a common tabular spacing $h$. Data from
   experiment or from a table with a varying interval are handled directly.
2. **The tabulated order is irrelevant.** The formula is symmetric in the
   points; permuting them leaves the result unchanged, which is worth noting
   when a table is printed with its entries out of order.
3. **A single expression gives the value.** The whole formula is written once
   and evaluated at any $x$ in range, with no successive-difference table to
   construct.
4. **The error is available.** With $n+1$ points the error is
   $R_n = \dfrac{f^{(n+1)}(\xi)}{(n+1)!}\prod_{i=0}^{n}(x - x_i)$, so the
   accuracy of a chosen set can be judged before evaluating.

**Limitations.** Adding a new point requires recomputing every coefficient,
unlike Newton's divided-difference form where earlier work is retained. The
formula is also inefficient for repeated evaluation at many points, where a
single polynomial written out once is preferable.

---

### **(b) The upward velocity of a rocket is given as a function of time in table below. Determine the value of the velocity at $t = 16$ seconds using $1^{\text{st}}$ order polynomial. [Marks: 06]**

| $t$ (sec) | 0 | 10 | 15 | 20 | 22.5 | 30 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| $v(t)$ (m/s) | 0 | 227.04 | 362.78 | 517.35 | 602.97 | 901.67 |

A first-order polynomial is linear interpolation, so the two tabulated points
bracketing $t = 16$ are required. They are $(15, 362.78)$ and $(20, 517.35)$.

**The linear polynomial.** Through $(t_0, v_0) = (15, 362.78)$ and
$(t_1, v_1) = (20, 517.35)$:

$$v(t) = v_0 + \frac{t - t_0}{t_1 - t_0}(v_1 - v_0)$$

$$v(t) = 362.78 + \frac{t - 15}{5}(517.35 - 362.78) = 362.78 + \frac{t - 15}{5}(154.57)$$

**Evaluate at $t = 16$.**

$$v(16) = 362.78 + \frac{16 - 15}{5}(154.57) = 362.78 + \frac{154.57}{5}$$

$$v(16) = 362.78 + 30.914 = 393.694$$

$$\boxed{v(16) = 393.694\ \text{m/s}}$$

> [!info] Check against the quadratic through the same three points
> A second-degree polynomial through $(10, 227.04)$, $(15, 362.78)$ and
> $(20, 517.35)$ is
> $v(t) = 0.37660t^2 + 17.7330t + 12.050$, and it gives
> $v(16) = 96.4096 + 283.728 + 12.050 = 392.1876$. The linear value $393.694$
> and the quadratic value $392.1876$ differ by $1.5064$ m/s, about $0.38\%$,
> which is the effect of the curvature of $v$ over the interval. Since a
> first-order polynomial was asked for, the linear value is the answer; the
> comparison is recorded to show the size of the curvature term being
> discarded. The tabulated slopes confirm that $v$ is steepening steadily near
> $t = 16$: they run $22.704$, $27.148$, $30.914$, $34.248$, $39.827$ over the
> successive steps $10$, $5$, $5$, $2.5$ and $7.5$, so the curve is convex and a
> straight chord through $[15, 20]$ lies above the parabola at $t = 16$, which
> is exactly the sign of the $1.5064$ difference.

---

### **(c) Find $f(2.5)$ from the given data, $x$: 1, 2, 3 and $f(x)$: 0, 1, 8. [Marks: 04]**

| $x$ | 1 | 2 | 3 |
| :---: | :---: | :---: |
| $f(x)$ | 0 | 1 | 8 |

**Lagrange's formula.** With three points,

$$f(x) = \frac{(x - x_1)(x - x_2)}{(x_0 - x_1)(x_0 - x_2)}f_0 + \frac{(x - x_0)(x - x_2)}{(x_1 - x_0)(x_1 - x_2)}f_1 + \frac{(x - x_0)(x - x_1)}{(x_2 - x_0)(x_2 - x_1)}f_2$$

At $x = 2.5$:

$$L_0 = \frac{(2.5 - 2)(2.5 - 3)}{(1 - 2)(1 - 3)} = \frac{(0.5)(-0.5)}{(-1)(-2)} = \frac{-0.25}{2} = -0.125$$

$$L_1 = \frac{(2.5 - 1)(2.5 - 3)}{(2 - 1)(2 - 3)} = \frac{(1.5)(-0.5)}{(1)(-1)} = \frac{-0.75}{-1} = 0.75$$

$$L_2 = \frac{(2.5 - 1)(2.5 - 2)}{(3 - 1)(3 - 2)} = \frac{(1.5)(0.5)}{(2)(1)} = \frac{0.75}{2} = 0.375$$

$$f(2.5) = 0(-0.125) + 1(0.75) + 8(0.375) = 0.75 + 3.0 = 3.75$$

$$\boxed{f(2.5) = 3.75}$$

> [!info] Check against the polynomial and against the original equation
> Newton's divided differences give $f[x_0,x_1] = 1$, $f[x_1,x_2] = 7$ and
> $f[x_0,x_1,x_2] = 3$, so the polynomial is
> $f(x) = 0 + 1(x - 1) + 3(x - 1)(x - 2) = 3x^2 - 8x + 5$. Substituting gives
> $f(2.5) = 3(6.25) - 20 + 5 = 3.75$, agreeing with the Lagrange result, and the
> three basis polynomials sum to $-0.125 + 0.75 + 0.375 = 1$ exactly, as the
> Lagrange basis of a quadratic must. The polynomial also reproduces the table:
> $f(1) = 0$, $f(2) = 1$ and $f(3) = 8$. Two routes, a partition-of-unity
> check and a table-reproduction check all give the same value, so no tabulated
> entry is contradicted and the arithmetic is confirmed.

---

## Question 4

### **(a) What is meant by over-relaxation and under-relaxation? [Marks: 02]**

Both terms describe a modification of the Gauss-Seidel iteration in which a
**relaxation parameter** $\omega$ is introduced.

**Relaxed Gauss-Seidel.** The ordinary Gauss-Seidel update is replaced by

$$x_i^{(k+1)} = (1 - \omega)x_i^{(k)} + \omega\hat x_i^{(k)}$$

where $\hat x_i^{(k)}$ is the value obtained from the ordinary Gauss-Seidel
recursion applied to iteration $k$.

**Under-relaxation, $0 < \omega < 1$.** Each new iterate is a weighted blend of
the old value and the new one, so the sequence moves toward the solution by a
fraction of the full step. This damps oscillation and is used when the ordinary
iteration diverges or oscillates, because it reduces the effective step and
restores convergence at the cost of more iterations.

**Over-relaxation, $1 < \omega < 2$.** Each new iterate overshoots the ordinary
Gauss-Seidel value, so the sequence moves toward the solution faster than the
plain iteration. The method is then called Successive Over-Relaxation (SOR),
and the choice of optimal $\omega$ reduces the iteration count substantially.

**The two regimes separated by $\omega = 1$.** At $\omega = 1$ the formula
reduces to ordinary Gauss-Seidel. Above $1$ the iteration is accelerated; below
$1$ it is stabilised. The purpose in both cases is the same, which is to
control the rate at which error is carried from one iteration to the next.

---

### **(b) Solve the following circuit by using Gauss-Seidel method. [Marks: 05]**

**The circuit.** A planar four-mesh DC network in a $2\times2$ arrangement.
Mesh 1 (top-left) contains a $10\ \Omega$ top branch, a $20\ \Omega$ right
branch shared with mesh 2, a $25\ \Omega$ bottom branch shared with mesh 4, and
a connecting wire on the left. Mesh 2 (top-right) contains a $10\ \text{A}$
current source in its top branch directed leftward, the shared $20\ \Omega$ on
its left, a $25\ \Omega$ bottom branch shared with mesh 3, and a wire on the
right. Mesh 3 (bottom-right) contains the shared $25\ \Omega$ on top, a
$4\ \Omega$ left branch shared with mesh 4, an $8\ \Omega$ right branch, and a
wire on the bottom. Mesh 4 (bottom-left) contains the shared $25\ \Omega$ on
top, the shared $4\ \Omega$ on the right, a $100\ \text{V}$ source on the left
directed upward, and a wire on the bottom.

```text
                  10 Ω                         10 A (←)
         +-------/\/\/\/\-------+-------------( ← )-----------+
         |                      |                            |
         |                      |                            |
         |                    [20 Ω]                         |
         |      (↻ I₁)          |            (↻ I₂)          |
         |                      |                            |
         +-------/\/\/\/\-------+------------/\/\/\/\--------+
         |        25 Ω          |             25 Ω           |
         |                      |                            |
       ( ↑ ) 100 V            [4 Ω]                        [8 Ω]
         |                      |                            |
         |      (↻ I₄)          |            (↻ I₃)          ||
         |                      |                            |
         +----------------------+----------------------------+
```

**The current-source constraint.** The $10\ \text{A}$ source occupies the top
branch of mesh 2 alone, so the current in that branch is fixed. Taking the mesh
currents clockwise, the branch carries $I_2$ and the source opposes it:

$$I_2 = -10\ \text{A}$$

**Mesh 1.** Traversing clockwise, the drops are $10I_1$ across the top branch,
$20(I_1 - I_2)$ across the shared $20\ \Omega$, and $25(I_1 - I_4)$ across the
shared $25\ \Omega$:

$$10I_1 + 20(I_1 - I_2) + 25(I_1 - I_4) = 0 \implies 55I_1 - 25I_4 = 20I_2 = -200$$

**Mesh 3.** Traversing clockwise, $8I_3$ across the right branch,
$25(I_3 - I_2)$ across the shared $25\ \Omega$, and $4(I_3 - I_4)$ across the
shared $4\ \Omega$:

$$8I_3 + 25(I_3 - I_2) + 4(I_3 - I_4) = 0 \implies 37I_3 - 4I_4 = 25I_2 = -250$$

**Mesh 4.** Traversing clockwise, $25(I_4 - I_1)$ and $4(I_4 - I_3)$ across the
two shared branches, and the $100\ \text{V}$ source entered against the
traversal:

$$25(I_4 - I_1) + 4(I_4 - I_3) = 100 \implies -25I_1 - 4I_3 + 29I_4 = 100$$

**Gauss-Seidel recursions.** Solve each equation for its diagonal unknown:

$$I_1^{(k+1)} = \frac{-200 + 25I_4^{(k)}}{55}$$

$$I_3^{(k+1)} = \frac{-250 + 4I_4^{(k)}}{37}$$

$$I_4^{(k+1)} = \frac{100 + 25I_1^{(k+1)} + 4I_3^{(k+1)}}{29}$$

Note the ordering: $I_1$ and $I_3$ are computed from the old $I_4$, then $I_4$
is computed from the two just-obtained values. Start from
$I_1 = I_3 = I_4 = 0$.

| Iteration | $I_1$ | $I_3$ | $I_4$ |
| :--: | :-- | :-- | :-- |
| 1 | $-3.636364$ | $-6.756757$ | $-0.618487$ |
| 2 | $-3.917494$ | $-6.823620$ | $-0.870063$ |
| 3 | $-4.031847$ | $-6.850818$ | $-0.972395$ |
| 4 | $-4.078361$ | $-6.861880$ | $-1.014019$ |
| 5 | $-4.097281$ | $-6.866380$ | $-1.030950$ |
| 6 | $-4.104977$ | $-6.868211$ | $-1.037837$ |
| 7 | $-4.108108$ | $-6.868955$ | $-1.040638$ |
| 8 | $-4.109381$ | $-6.869258$ | $-1.041778$ |

**The solution.** The iteration converges, and eliminating gives the same
values:

$$I_1 = -\frac{14390}{3501} = -4.1103\ \text{A}, \qquad I_3 = -\frac{24050}{3501} = -6.8695\ \text{A}, \qquad I_4 = -\frac{3650}{3501} = -1.0426\ \text{A}$$

$$\boxed{I_1 = -4.1103\ \text{A}, \quad I_2 = -10\ \text{A}, \quad I_3 = -6.8695\ \text{A}, \quad I_4 = -1.0426\ \text{A}}$$

> [!info] Check by mesh KVL and by nodal analysis
> Substituting the four mesh currents into the three mesh equations, at the
> four-decimal precision to which they are quoted, gives
> $55(-4.1103) - 25(-1.0426) = -226.0665 + 26.0650 = -200.0015 \approx -200$;
> $37(-6.8695) - 4(-1.0426) = -254.1715 + 4.1704 = -250.0011 \approx -250$;
> $-25(-4.1103) - 4(-6.8695) + 29(-1.0426) = 102.7575 + 27.4780 - 30.2354 = 100.0001 \approx 100$.
> Each residual is at the $10^{-4}$ level, which is what rounding four currents
> to four decimals must produce; on the exact fractions the three equations
> return $-200$, $-250$ and $100$ with no residual at all. Independently,
> nodal analysis with the top-middle, central and top-right nodes as unknowns,
> the left node held at $100\ \text{V}$ and the bottom rail as reference, gives
> node potentials $141.103\ \text{V}$, $23.308\ \text{V}$ and $-54.956\ \text{V}$.
> Reading the mesh currents back out of those potentials,
> $I_1 = (100 - 141.103)/10 = -4.1103$, $I_3 = -54.956/8 = -6.8695$, and
> $I_2 = -10$ follows from the source, agreeing with the mesh solution to four
> digits. Two entirely different formulations reaching the same currents is the
> strongest available confirmation.

> [!note] A convergence note
> The third row has $|29| = |{-25}| + |{-4}| = 29$, so the system is weakly
> diagonally dominant rather than strictly so, and the Gauss-Seidel iteration
> converges slowly. This is visible in the table: the correction per iteration
> falls only gradually. The elimination result is exact and is the value to
> report; the iteration demonstrates the method as asked.

---

### **(c) The following data was taken from an experiment that measured the current in a wire for various imposed voltages. On the basis of a linier regression of this data, determine current for a voltage of $3.5\text{ V}$. Plot the line to evaluate the fit. [Marks: 05]**

| $v$ (V) | 2 | 3 | 4 | 5 | 7 | 10 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| $i$ (A) | 5.2 | 7.8 | 10.7 | 13 | 19.3 | 27.5 |

**Fit the line** $i = a + bv$ by least squares. With $n = 6$:

$$\sum v = 31, \qquad \sum i = 83.5, \qquad \sum v^2 = 203, \qquad \sum vi = 551.7$$

**The normal-equation solution.**

$$b = \frac{n\sum vi - \sum v\sum i}{n\sum v^2 - \left(\sum v\right)^2} = \frac{6(551.7) - (31)(83.5)}{6(203) - 31^2} = \frac{3310.2 - 2588.5}{1218 - 961} = \frac{721.7}{257}$$

$$b = 2.8082\ \text{A/V}$$

$$a = \bar i - b\bar v = \frac{83.5}{6} - 2.8082\left(\frac{31}{6}\right) = 13.9167 - 14.5089 = -0.5922\ \text{A}$$

**The regression line.**

$$\boxed{i = -0.5922 + 2.8082\,v}$$

**The current at $3.5\ \text{V}$.**

$$i(3.5) = -0.5922 + 2.8082(3.5) = -0.5922 + 9.8287 = 9.2364$$

$$\boxed{i(3.5\ \text{V}) = 9.2364\ \text{A}}$$

**Plotting the fit.** The six measured points $(v, i)$ and the fitted line $i = -0.5922 + 2.8082\,v$:

![Linear regression plot of current versus voltage with measured points, fitted line, and evaluated point at 3.5V](diagrams/2018_Q4c_regression.png)

The measured values and residuals against the line are:

| $v$ | measured $i$ | fitted $i$ | residual |
| :--: | :-- | :-- | :-- |
| 2 | 5.2 | $5.0241$ | $+0.1759$ |
| 3 | 7.8 | $7.8323$ | $-0.0323$ |
| 4 | 10.7 | $10.6405$ | $+0.0595$ |
| 5 | 13 | $13.4486$ | $-0.4486$ |
| 7 | 19.3 | $19.0650$ | $+0.2350$ |
| 10 | 27.5 | $27.4895$ | $+0.0105$ |

The residuals are small compared with the values themselves, the largest in
magnitude being $0.4486$ against $13$, so the line describes the data well. A
straight line is a reasonable model for a wire at constant temperature.

> [!info] Check against the centroid and the correlation coefficient
> The centroid of the data is $(\bar v, \bar i) = (5.1667, 13.9167)$, and
> substituting gives $-0.5922 + 2.8082(5.1667) = 13.9167$, so the line passes
> through the centroid as the normal equations require. The correlation
> coefficient is $r = 0.9996$, so $r^2 = 0.9991$, meaning over $99.9\%$ of the
> variation in current is accounted for by the line. As a numerical check, the
> fitted line evaluated at $v = 3$ and $v = 4$ gives $7.8323$ and $10.6405$,
> and interpolating linearly between those at $v = 3.5$ returns $9.2364$, which
> is the value computed above. A straight line, a centroid condition and an
> internal interpolation all agree, so the result is not an artefact of the
> rounding of $a$ and $b$.

---

# SECTION B

## Question 5

### **(a) State Newton's forward formula to evaluate $\frac{d^2 y}{dx^2}$ for any value $x \in [x_0, x_n]$. [Marks: 06]**

**Newton's forward formula.** For a tabular spacing $h$, the forward difference
interpolation polynomial through $n+1$ points is

$$y = y_0 + p\Delta y_0 + \frac{p(p-1)}{2!}\Delta^2 y_0 + \frac{p(p-1)(p-2)}{3!}\Delta^3 y_0 + \frac{p(p-1)(p-2)(p-3)}{4!}\Delta^4 y_0 + \cdots$$

with

$$p = \frac{x - x_0}{h}$$

**First derivative.** Differentiating term by term,
$\dfrac{d}{dx} = \dfrac{1}{h}\dfrac{d}{dp}$:

$$\frac{dy}{dx} = \frac{1}{h}\left[\Delta y_0 + \frac{2p - 1}{2!}\Delta^2 y_0 + \frac{3p^2 - 6p + 2}{3!}\Delta^3 y_0 + \frac{4p^3 - 18p^2 + 22p - 6}{4!}\Delta^4 y_0 + \cdots\right]$$

**Second derivative.** Differentiating a second time:

$$\frac{d^2y}{dx^2} = \frac{1}{h^2}\left[\Delta^2 y_0 + \frac{6p - 6}{3!}\Delta^3 y_0 + \frac{12p^2 - 36p + 22}{4!}\Delta^4 y_0 + \cdots\right]$$

which simplifies to

$$\boxed{\frac{d^2y}{dx^2} = \frac{1}{h^2}\left[\Delta^2 y_0 + (p - 1)\Delta^3 y_0 + \left(\frac{p^2}{2} - \frac{3p}{2} + \frac{11}{12}\right)\Delta^4 y_0 + \cdots\right]}$$

**Validity.** The formula reproduces $\dfrac{d^2y}{dx^2}$ exactly for any
polynomial of degree four or lower, because every term from $\Delta^5 y_0$
onward then vanishes. For a table of noisy experimental data the higher
differences are not zero, and they are also the noisiest entries in the
difference table, so the terms beyond the data's smoothness are not worth
retaining.

**Terms retained.** A polynomial of degree $n$ through $n+1$ points has exactly
$n+1$ coefficients, so for $n = 1$ only the $\Delta y_0$ term exists, for
$n = 2$ the terms up to $\Delta^2 y_0$ exist, and so on. Since $y''$ requires
differences of order two and above, the formula needs at least **three points**
for a quadratic fit, four for a cubic, and so on. The next term, omitted above,
is

$$\left(\frac{p^3}{6} - p^2 + \frac{7p}{4} - \frac{5}{6}\right)\Delta^5 y_0$$

> [!info] Check against the exact second derivative of a cubic
> The formula is exact for any polynomial of degree at most the number of
> points used, and a cubic is the first case where this can be tested. Take
> $y = ax^3$ tabulated from $x_0 = 0$ at spacing $h$, so $x = ph$. Then
> $\Delta y_n = ah^3(9n^2 + 9n + 3)$, $\Delta^2 y_0 = 6ah^3$ and
> $\Delta^3 y_0 = 6ah^3$, with all higher differences zero. The formula gives
> $\dfrac{1}{h^2}\left[6ah^3 + (p - 1)6ah^3\right] = 6ah\left[1 + p - 1\right] = 6aph$.
> The true second derivative is $y'' = 6ax = 6a(ph) = 6aph$. The two agree for
> every $p$, not only at the nodes, which is the property that makes the formula
> usable for interpolation rather than only for differencing. For a quadratic
> $y = ax^2 + bx + c$ only $\Delta^2 y_n = 2ah^2$ survives, and the formula
> reduces to $\dfrac{1}{h^2}(2ah^2) = 2a$, again the exact second derivative.

---

### **(b) From the following table find $x$, correct to two decimal places for which $y$ is maximum and find this value of $y$. [Marks: 06]**

| $x$ | 1.2 | 1.3 | 1.4 | 1.5 | 1.6 |
| :---: | :---: | :---: | :---: | :---: | :---: |
| $y$ | 0.9320 | 0.9636 | 0.9855 | 0.9975 | 0.9996 |

**The differences.** With $h = 0.1$:

| | 0.9320 | 0.9636 | 0.9855 | 0.9975 | 0.9996 |
| :-- | :-- | :-- | :-- | :-- | :-- |
| $\Delta$ | | $0.0316$ | $0.0219$ | $0.0120$ | $0.0021$ |
| $\Delta^2$ | | | $-0.0097$ | $-0.0099$ | $-0.0099$ |
| $\Delta^3$ | | | | $-0.0002$ | $0.0000$ |
| $\Delta^4$ | | | | | $0.0002$ |

The first differences are all positive but falling, and the last of them,
$0.0021$, is small, so the maximum lies just inside the end of the table, close
to but before $x = 1.6$. The backward difference form is the natural one to use
from there, since the maximum is at the far end of the table.

**The backward derivative.** At $x = x_4 = 1.6$, with $q = (x - x_4)/h$,

$$\frac{dy}{dx} = \frac{1}{h}\left[\nabla y_4 + \frac{2q + 1}{2}\nabla^2 y_4 + \frac{3q^2 + 6q + 2}{6}\nabla^3 y_4 + \frac{4q^3 + 18q^2 + 22q + 6}{24}\nabla^4 y_4\right]$$

The backward differences at $x_4$ are

$$\nabla y_4 = 0.0021, \qquad \nabla^2 y_4 = -0.0099, \qquad \nabla^3 y_4 = 0.0000, \qquad \nabla^4 y_4 = 0.0002$$

**Set $\dfrac{dy}{dx} = 0$.** Since $\nabla^3 y_4 = 0$ and $\nabla^4 y_4$ is
small, the stationary point is set by the first two terms:

$$0.0021 + \frac{2q + 1}{2}(-0.0099) = 0$$

$$0.0021 = (q + 0.5)(0.0099)$$

$$q + 0.5 = \frac{0.0021}{0.0099} = 0.212121$$

$$q = -0.287879$$

$$x = x_4 + hq = 1.6 + 0.1(-0.287879) = 1.5712$$

**Evaluate $y$ there.** Using the backward Newton polynomial with all five
points,

$$y = y_4 + q\nabla y_4 + \frac{q(q+1)}{2}\nabla^2 y_4 + \frac{q(q+1)(q+2)}{6}\nabla^3 y_4 + \frac{q(q+1)(q+2)(q+3)}{24}\nabla^4 y_4$$

At $q = -0.287879$:

$$y = 0.9996 + (-0.287879)(0.0021) + \frac{(-0.287879)(0.712121)}{2}(-0.0099) + 0 + \frac{(-0.287879)(0.712121)(1.712121)(2.712121)}{24}(0.0002)$$

$$y = 0.9996 - 0.0006045 + 0.0010148 - 0.0000079 = 1.0000023$$

$$\boxed{x = 1.57 \text{ (correct to two decimal places)}, \qquad y_{\max} = 1.0000}$$

> [!info] Check against the full five-point polynomial
> Fitting a single polynomial through all five points by Lagrange interpolation
> gives $y = \dfrac{x^4}{12} - \dfrac{29x^3}{60} + \dfrac{133x^2}{240} + \dfrac{409x}{750} + \dfrac{71}{500}$.
> Setting $y' = 0$, that is
> $y' = \dfrac{x^3}{3} - \dfrac{29x^2}{20} + \dfrac{133x}{120} + \dfrac{409}{750}$, and
> solving gives $x = 1.5713$, with $y = 1.0000023$. The derivatives and values agree
> with the backward-difference route to the digits shown, and the $\Delta^4$ term
> shifts the stationary point by $9.1\times10^{-5}$. A maximum is confirmed
> because $y'' = x^2 - \dfrac{29x}{10} + \dfrac{133}{120}$ evaluates to
> $-0.9795$ at $x = 1.5713$, which is negative. The quartic has three real
> critical points, $x = -0.3344$, $x = 1.5713$ and $x = 3.1131$, and $1.5713$
> is the only one inside the table; the other two lie outside $[1.2, 1.6]$ and so
> cannot be the maximum of the tabulated function.

---

## Question 6

### **(a) The vertical distance covered by a rocket from $t = 8$ to $t = 30$ seconds is given by: $x = \int_8^{30} \left( 2000 \ln \left[ \frac{140000}{140000 - 2100t} \right] - 9.8t \right) dt$. (i) Use eight-segment Simpson's $\frac{1}{3}$ rule to find the distance covered. (ii) Find the true error of part (i). (iii) Find the absolute relative error for part (i). [Marks: 08]**

**(i) Eight-segment Simpson's $\frac{1}{3}$ rule.** With $n = 8$,
$h = \dfrac{30 - 8}{8} = 2.75$, the nodes are
$t = 8,\ 10.75,\ 13.5,\ 16.25,\ 19,\ 21.75,\ 24.5,\ 27.25,\ 30$.

Evaluating $f(t) = 2000\ln\left[\dfrac{140000}{140000 - 2100t}\right] - 9.8t$:

| $i$ | $t_i$ | $f(t_i)$ | weight |
| :--: | :--: | :-- | :--: |
| 0 | 8.00000 | 177.2667430 | 1 |
| 1 | 10.75000 | 246.3351814 | 4 |
| 2 | 13.50000 | 320.2468886 | 2 |
| 3 | 16.25000 | 399.5165393 | 4 |
| 4 | 19.00000 | 484.7454726 | 2 |
| 5 | 21.75000 | 576.6423135 | 4 |
| 6 | 24.50000 | 676.0501168 | 2 |
| 7 | 27.25000 | 783.9826784 | 4 |
| 8 | 30.00000 | 901.6740015 | 1 |

$$x \approx \frac{h}{3}\left[f_0 + f_8 + 4(f_1 + f_3 + f_5 + f_7) + 2(f_2 + f_4 + f_6)\right]$$

$$= \frac{2.75}{3}\left[177.2667430 + 901.6740015 + 4(246.3351814 + 399.5165393 + 576.6423135 + 783.9826784) + 2(320.2468886 + 484.7454726 + 676.0501168)\right]$$

The weighted sums are

$$4(2006.4767126) = 8025.9068504, \qquad 2(1481.0424780) = 2962.0849560$$

$$x \approx \frac{2.75}{3}(177.2667430 + 901.6740015 + 8025.9068504 + 2962.0849560) = \frac{2.75}{3}(12066.9325509)$$

$$\boxed{x \approx 11061.3548\ \text{m}}$$

**(ii) The true error.** The exact value of the integral is

$$x_{\text{exact}} = \int_8^{30}\left(2000\ln\left[\frac{140000}{140000 - 2100t}\right] - 9.8t\right)dt = 11061.3355\ \text{m}$$

Hence the true error is

$$E_t = x_{\text{exact}} - x \approx 11061.3355 - 11061.3548 = -0.0193\ \text{m}$$

$$\boxed{E_t \approx -0.0193\ \text{m}}$$

**(iii) The absolute relative error.**
 
$$|\varepsilon_t| = \left|\frac{\text{true error}}{\text{true value}}\right| \times 100\% = \left|\frac{-0.0193}{11061.3355}\right|\times 100\%$$

$$\boxed{|\varepsilon_t| \approx 0.00017\%}$$

> [!info] Check against the exact integral and a 16-segment estimate
> The exact value is obtained by antidifferentiation,
> $\int 2000\ln\left[\dfrac{140000}{140000-2100t}\right]dt = -\dfrac{2000}{2100}(140000-2100t)\left[\ln\left(\dfrac{140000-2100t}{140000}\right) - 1\right]$,
> which evaluates to $11061.3355$ between the limits. The eight-segment result
> $11061.3548$ is larger by $0.0193$, an error of $0.00017\%$. Repeating with
> $16$ segments gives $x = 11061.3368$, still above the exact integral but
> sixteen times closer to it, and a third pass with $32$ segments gives
> $11061.3356$. The errors $1.93\times10^{-2}$, $1.22\times10^{-3}$ and
> $7.6\times10^{-5}$ fall in the ratio $16:1$ at each halving of $h$, which is
> the $O(h^4)$ convergence of Simpson's rule and cannot be produced by an
> arithmetic slip. The error is a truncation error of the rule.

---

### **(b) Determine the value of $n$ so that the trapezoidal rule will approximate the value of $\int_0^1 \sqrt{1 + x^2} \, dx$ with an error that is less than $0.01$. [Marks: 04]**

**The error bound.** The composite trapezoidal rule over $[a, b]$ with $n$
subintervals has error

$$|E| = \left|\frac{(b - a)h^2}{12}f''(\xi)\right| \le \frac{(b - a)h^2}{12}\max|f''|$$

Here $a = 0$, $b = 1$, and

$$f(x) = \sqrt{1 + x^2}$$

$$f'(x) = \frac{x}{\sqrt{1+x^2}}, \qquad f''(x) = \frac{1}{(1+x^2)^{3/2}}$$

On $[0, 1]$ the maximum of $|f''|$ is at $x = 0$, where
$f''(0) = 1$. So

$$|E| \le \frac{h^2}{12}(1) = \frac{h^2}{12}$$

**Solve for $h$ then $n$.**

$$\frac{h^2}{12} < 0.01 \implies h^2 < 0.12 \implies h < 0.3464$$

$$n = \frac{b - a}{h} > \frac{1}{0.3464} = 2.8868$$

Hence the smallest integer satisfying the bound is

$$\boxed{n = 3}$$

**Direct check.** Evaluating the trapezoidal rule:

| $n$ | $h$ | Approximation | Error |
| :--: | :--: | :-- | :-- |
| 2 | 0.50 | 1.1625704 | $0.014777$ |
| 3 | 0.3333 | 1.1543499 | $0.006556$ |

At $n = 2$ the error exceeds $0.01$, and at $n = 3$ it falls below, confirming
$n = 3$.

> [!info] Check against the exact integral
> The exact value is
> $\int_0^1\sqrt{1+x^2}\,dx = \left[\dfrac{x\sqrt{1+x^2}}{2} + \dfrac{\ln(x + \sqrt{1+x^2})}{2}\right]_0^1 = \dfrac{\sqrt2 + \ln(1+\sqrt2)}{2} = 1.1477936$.
> The $n = 3$ value $1.1543499$ differs by $0.006556$, which is below $0.01$;
> the $n = 2$ value differs by $0.014777$, which is not. The error bound
> $\dfrac{h^2}{12}$ is also confirmed numerically: at $n = 3$, $h = 1/3$, the
> bound gives $\dfrac{1}{9\cdot12} = 0.009259$, and the actual error $0.006556$ is
> below the bound, as it must be.

---

## Question 7

### **(a) Solve $\frac{dy}{dx} = 1 - y$ with the initial condition $x = 0, y = 0$ by using modified Euler's method. Tabulate the solutions at $x = 0.1, 0.2, 0.3$. [Marks: 06]**

**The method.** With $h = 0.1$ and $f(x, y) = 1 - y$, the predictor is

$$\hat y_1 = y_n + hf(x_n, y_n)$$

and the corrector takes the average of the two slopes:

$$y_{n+1} = y_n + \frac{h}{2}\left[f(x_n, y_n) + f(x_{n+1}, \hat y_1)\right]$$

**Step 1.** $x_0 = 0$, $y_0 = 0$, $h = 0.1$.

$$f(x_0, y_0) = 1 - 0 = 1$$

$$\hat y_1 = 0 + 0.1(1) = 0.1$$

$$f(x_1, \hat y_1) = 1 - 0.1 = 0.9$$

$$y_1 = 0 + \frac{0.1}{2}(1 + 0.9) = 0.05(1.9) = 0.095$$

**Step 2.** $x_1 = 0.1$, $y_1 = 0.095$.

$$f(x_1, y_1) = 1 - 0.095 = 0.905$$

$$\hat y_2 = 0.095 + 0.1(0.905) = 0.1855$$

$$f(x_2, \hat y_2) = 1 - 0.1855 = 0.8145$$

$$y_2 = 0.095 + \frac{0.1}{2}(0.905 + 0.8145) = 0.095 + 0.05(1.7195) = 0.180975$$

**Step 3.** $x_2 = 0.2$, $y_2 = 0.180975$.

$$f(x_2, y_2) = 1 - 0.180975 = 0.819025$$

$$\hat y_3 = 0.180975 + 0.1(0.819025) = 0.2628775$$

$$f(x_3, \hat y_3) = 1 - 0.2628775 = 0.7371225$$

$$y_3 = 0.180975 + \frac{0.1}{2}(0.819025 + 0.7371225) = 0.180975 + 0.05(1.5561475) = 0.2587824$$

**The tabulated solutions.**

| $x$ | $y$ |
| :--: | :-- |
| 0.1 | $0.0950000$ |
| 0.2 | $0.1809750$ |
| 0.3 | $0.2587824$ |

$$\boxed{y(0.1) = 0.095, \qquad y(0.2) = 0.181, \qquad y(0.3) = 0.259}$$

> [!info] Check against the exact solution
> The equation is separable: $\dfrac{dy}{1-y} = dx$ gives $y = 1 - Ce^{-x}$,
> and $y(0) = 0$ gives $C = 1$, so $y = 1 - e^{-x}$. The exact values are
> $0.0951626$, $0.1812692$ and $0.2591818$ at $x = 0.1, 0.2, 0.3$. The computed
> values are low by $1.6\times10^{-4}$, $2.9\times10^{-4}$ and $4.0\times10^{-4}$
> respectively, a pattern of errors growing with $x$ as expected of a
> second-order method with fixed $h$, since the error accumulates with the
> number of steps. The plain (unmodified) Euler values would be $0.1$, $0.19$
> and $0.271$, whose errors are $4.84\times10^{-3}$, $8.73\times10^{-3}$ and
> $1.18\times10^{-2}$. The modification has therefore reduced the error by
> about thirty times, not by an order of magnitude less, which is what confirms
> the corrector was applied rather than only the predictor.

---

### **(b) Use the Runge-Kutta method to solve $10\frac{dy}{dx} = x^2 - y^2, \, y(0) = 1$ for the interval $0 < x \le 0.4$ with $h = 0.1$. [Marks: 06]**

**Rewrite the equation.**

$$\frac{dy}{dx} = \frac{x^2 - y^2}{10}, \qquad y(0) = 1$$

Hence $f(x, y) = \dfrac{x^2 - y^2}{10}$.

**Fourth-order Runge-Kutta.** With $h = 0.1$:

$$k_1 = f(x_n, y_n)$$

$$k_2 = f\left(x_n + \frac{h}{2}, y_n + \frac{h}{2}k_1\right)$$

$$k_3 = f\left(x_n + \frac{h}{2}, y_n + \frac{h}{2}k_2\right)$$

$$k_4 = f(x_n + h, y_n + hk_3)$$

$$y_{n+1} = y_n + \frac{h}{6}(k_1 + 2k_2 + 2k_3 + k_4)$$

**Step 1.** $x_0 = 0$, $y_0 = 1$, so $h/2 = 0.05$.

$$k_1 = \frac{0^2 - 1^2}{10} = -0.1$$

$$k_2 = \frac{(0.05)^2 - \left(1 + \frac{0.1}{2}(-0.1)\right)^2}{10} = \frac{0.0025 - (0.995)^2}{10} = \frac{0.0025 - 0.990025}{10} = -0.0987525$$

$$k_3 = \frac{(0.05)^2 - \left(1 + \frac{0.1}{2}(-0.0987525)\right)^2}{10} = \frac{0.0025 - (0.99506238)^2}{10} = \frac{0.0025 - 0.99014913}{10} = -0.09876491$$

$$k_4 = \frac{(0.1)^2 - \left(1 + 0.1(-0.09876491)\right)^2}{10} = \frac{0.01 - (0.99012351)^2}{10} = \frac{0.01 - 0.98034456}{10} = -0.09703446$$

$$y_1 = 1 + \frac{0.1}{6}\left(-0.1 + 2(-0.0987525) + 2(-0.09876491) + (-0.09703446)\right)$$

$$y_1 = 1 + 0.0166667(-0.59206928) = 0.9901322$$

**Steps 2 to 4.** The same procedure applied successively:

| Step | $x_n$ | $y_n$ | $k_1$ | $k_2$ | $k_3$ | $k_4$ | $y_{n+1}$ |
| :--: | :--: | :-- | :-- | :-- | :-- | :-- | :-- |
| 1 | 0.0 | 1.0000000 | $-0.1000000$ | $-0.0987525$ | $-0.0987649$ | $-0.0970345$ | $0.9901322$ |
| 2 | 0.1 | 0.9901322 | $-0.0970362$ | $-0.0948277$ | $-0.0948495$ | $-0.0921669$ | $0.9806562$ |
| 3 | 0.2 | 0.9806562 | $-0.0921687$ | $-0.0890169$ | $-0.0890477$ | $-0.0854301$ | $0.9717608$ |
| 4 | 0.3 | 0.9717608 | $-0.0854319$ | $-0.0813535$ | $-0.0813930$ | $-0.0768566$ | $0.9636311$ |

Every $k_1$ in the table is $f(x_n, y_n) = (x_n^2 - y_n^2)/10$ at the
$x_n$, $y_n$ printed beside it, so the $y$ column and the $k$ column are two
readings of the same run and must agree at each row.

$$\boxed{y(0.4) = 0.9636}$$

**Full tabulation.**

| $x$ | $y$ |
| :--: | :-- |
| 0.1 | $0.9901322$ |
| 0.2 | $0.9806562$ |
| 0.3 | $0.9717608$ |
| 0.4 | $0.9636311$ |

> [!info] Check by two step sizes and by a very small step
> Repeating with $h = 0.05$ over eight steps gives $y(0.4) = 0.963631060$, with
> $h = 0.2$ over two steps $y(0.4) = 0.963631064$, and with $h = 0.025$ over
> sixteen steps $y(0.4) = 0.963631060$. The three step sizes agree to nine
> digits. The differences between them, $4.3\times10^{-9}$ between $h = 0.2$ and
> $h = 0.1$ and $2.5\times10^{-10}$ between $h = 0.1$ and $h = 0.05$, fall by a
> factor of about sixteen on each halving of $h$, which is the fourth-order
> convergence of the method and confirms that what remains is truncation error
> of the right order and not a slip in the recurrence. The error is genuinely
> very small here because the right-hand side is smooth and $y$ varies little
> over the interval; it is not small because of rounding.
>
> A step-count check confirms the total: four steps of $h = 0.1$ reach $x = 0.4$
> exactly, and the interval stated in the question is $0 < x \le 0.4$, so the
> table is complete.

---

## Question 8

### **(a) Find the potential distribution at the interior nodes using Leibmann's method. [Marks: 06]**

**The mesh.** A $3\times3$ grid over a square region with uniform spacing $h$,
four interior nodes $1$ to $4$, and Dirichlet boundaries: top $100\ \text{V}$,
bottom $0\ \text{V}$, left $75\ \text{V}$, right $50\ \text{V}$.

```text
              Insulating Gap            V = 100 V           Insulating Gap
                            \                                /
                   (0,3)   +-----------+-----------+-------+   (3,3)
                           |           |           |       |
                           |    ①     |     ②     |       |
                   (0,2)   +-----------+-----------+-------+   (3,2)
                           |  (Node 1) | (Node 2)  |       |
             V = 75 V      |           |           |       |   V = 50 V
                   (0,1)   +-----------+-----------+-------+   (3,1)
                           |    ③     |     ④     |       |
                           |  (Node 3) | (Node 4)  |       |
                   (0,0)   +-----------+-----------+-------+   (3,0)
                            /                                \
              Insulating Gap             V = 0 V             Insulating Gap
```

**The stencil.** The Laplace finite-difference equation at an interior node is

$$u_{i,j} = \frac{1}{4}\left(u_{i+1,j} + u_{i-1,j} + u_{i,j+1} + u_{i,j-1}\right)$$

**Leibmann's method** is Gauss-Seidel applied to this system: each node is
updated from the most recent values of its neighbours as soon as they are
available.

**The four node equations.** Reading the neighbours of each interior node from
the figure:

$$V_1 = \frac{100 + V_2 + 75 + V_3}{4} = \frac{175 + V_2 + V_3}{4}$$

$$V_2 = \frac{100 + 50 + V_1 + V_4}{4} = \frac{150 + V_1 + V_4}{4}$$

$$V_3 = \frac{75 + V_4 + V_1 + 0}{4} = \frac{75 + V_1 + V_4}{4}$$

$$V_4 = \frac{V_3 + 50 + V_2 + 0}{4} = \frac{50 + V_2 + V_3}{4}$$

As a $4\times4$ system:

$$\begin{bmatrix} 4 & -1 & -1 & 0 \\ -1 & 4 & 0 & -1 \\ -1 & 0 & 4 & -1 \\ 0 & -1 & -1 & 4 \end{bmatrix}\begin{bmatrix} V_1 \\ V_2 \\ V_3 \\ V_4 \end{bmatrix} = \begin{bmatrix} 175 \\ 150 \\ 75 \\ 50 \end{bmatrix}$$

**Leibmann iteration.** Starting from $V_1 = V_2 = V_3 = V_4 = 0$:

| Sweep | $V_1$ | $V_2$ | $V_3$ | $V_4$ |
| :--: | :-- | :-- | :-- | :-- |
| 1 | 43.750000 | 48.437500 | 29.687500 | 32.031250 |
| 2 | 63.281250 | 61.328125 | 42.578125 | 38.476563 |
| 3 | 69.726563 | 64.550781 | 45.800781 | 40.087891 |
| 4 | 71.337891 | 65.356445 | 46.606445 | 40.490723 |
| 5 | 71.740723 | 65.557861 | 46.807861 | 40.591431 |
| 6 | 71.841431 | 65.608215 | 46.858215 | 40.616608 |

**The solution.** The iteration converges, and solving the $4\times4$ system
directly gives

$$V_1 = \frac{575}{8} = 71.875, \qquad V_2 = \frac{525}{8} = 65.625$$

$$V_3 = \frac{375}{8} = 46.875, \qquad V_4 = \frac{325}{8} = 40.625$$

$$\boxed{V_1 = 71.875\ \text{V}, \quad V_2 = 65.625\ \text{V}, \quad V_3 = 46.875\ \text{V}, \quad V_4 = 40.625\ \text{V}}$$

> [!info] Check by substitution into the four stencil equations
> Substituting back: $\dfrac{1}{4}(175 + 65.625 + 46.875) = \dfrac{287.5}{4} = 71.875$ ✓;
> $\dfrac{1}{4}(150 + 71.875 + 40.625) = \dfrac{262.5}{4} = 65.625$ ✓;
> $\dfrac{1}{4}(75 + 71.875 + 40.625) = \dfrac{187.5}{4} = 46.875$ ✓;
> $\dfrac{1}{4}(50 + 65.625 + 46.875) = \dfrac{162.5}{4} = 40.625$ ✓. All four hold
> exactly. The values come out as multiples of $1/8$, which is a strong check in
> itself, since the boundary data are multiples of $25$ and the average of four
> such numbers is a multiple of $1/4$ at worst; a wrong entry would leave a
> residual of order one-tenth rather than zero. Every one of the four sweeps
> approaches its limit from below, which is what a Gauss-Seidel start at the
> origin gives when the right-hand side is positive, and the increments in $V_1$
> fall in the ratio $19.53 : 6.45 : 1.61 : 0.40 : 0.10$, a factor of about four
> per sweep.

---

### **(b) Use the Euler's method to solve, $\frac{d^2 y}{dt^2} - 0.5t = y$ where, $y(0) = 2$ and $y'(0) = 0$. Solve from $t = 0$ to $0.4$ using $h = 0.1$. [Marks: 06]**

**Convert to a first-order system.** Rearranging,

$$\frac{d^2y}{dt^2} = y + 0.5t$$

Introduce $v = \dfrac{dy}{dt}$. Then

$$\frac{dy}{dt} = v, \qquad \frac{dv}{dt} = y + 0.5t$$

with $y(0) = 2$ and $v(0) = 0$.

**Euler's method applied to both equations.**

$$y_{n+1} = y_n + h\,v_n$$

$$v_{n+1} = v_n + h\,(y_n + 0.5t_n)$$

**Step 1.** $t_0 = 0$, $y_0 = 2$, $v_0 = 0$.

$$y_1 = 2 + 0.1(0) = 2.0$$

$$v_1 = 0 + 0.1(2 + 0) = 0.2$$

**Step 2.** $t_1 = 0.1$, $y_1 = 2.0$, $v_1 = 0.2$.

$$y_2 = 2.0 + 0.1(0.2) = 2.02$$

$$v_2 = 0.2 + 0.1(2.0 + 0.05) = 0.2 + 0.205 = 0.405$$

**Step 3.** $t_2 = 0.2$, $y_2 = 2.02$, $v_2 = 0.405$.

$$y_3 = 2.02 + 0.1(0.405) = 2.0605$$

$$v_3 = 0.405 + 0.1(2.02 + 0.1) = 0.405 + 0.212 = 0.617$$

**Step 4.** $t_3 = 0.3$, $y_3 = 2.0605$, $v_3 = 0.617$.

$$y_4 = 2.0605 + 0.1(0.617) = 2.1222$$

$$v_4 = 0.617 + 0.1(2.0605 + 0.15) = 0.617 + 0.22105 = 0.83805$$

**The results.**

| $t$ | $y$ | $v = y'$ |
| :--: | :-- | :-- |
| 0.0 | 2.0000 | 0.0000 |
| 0.1 | 2.0000 | 0.20000 |
| 0.2 | 2.0200 | 0.40500 |
| 0.3 | 2.0605 | 0.61700 |
| 0.4 | 2.1222 | 0.83805 |

$$\boxed{y(0.4) = 2.1222}$$

> [!info] Check against the exact solution
> The equation $\ddot y - \tfrac12 t = y$ has the solution
> $y = C_1 e^{-t} + C_2 e^{t} - \tfrac12 t$, and the two initial conditions give
> $C_1 + C_2 = 2$ and $-C_1 + C_2 = 0.5$ (from $y'(0) = -C_1 + C_2 - 0.5 = 0$,
> yielding $C_1 = 0.75, C_2 = 1.25$), so
> $y = 2\cosh t + \tfrac12\sinh t - \tfrac12 t$. At $t = 0.4$ that is
> $y(0.4) = 2.167521$, against which the Euler value $2.1222$ is low by
> $0.0453$, about $2.1\%$. That shortfall is the expected truncation error of a
> first-order method, whose global error over four steps is of order $h$.
> Halving $h$ to $0.05$ and running eight steps gives $y(0.4) = 2.144385$, and
> halving it again to $0.025$ gives $2.155822$: the successive gains are
> $0.022$ and $0.011$, in the ratio $2:1$ that an $O(h)$ error requires, so this
> is truncation error and not a slip in the recurrence. The same value can be
> reached from the other side, since differentiating $\ddot y = y + \tfrac12 t$
> repeatedly gives $y''(0) = 2$, $y'''(0) = 0.5$ and $y^{(4)}(0) = y(0) = 2$,
> so the four-term series gives $2 + 0.16 + 0.005333 + 0.002133 = 2.16747$.

---
