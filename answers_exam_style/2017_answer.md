---
title: "ECE 2213 · 2017 Exam Style Answers"
tags:
  - numerical-methods
  - discrete-mathematics
  - previous-year
---

# ECE 2213: 2017 Semester Final · Exam Style Answers

**RUET · ECE Dept · B.Sc. Engineering 2nd Year Even Semester Examination, 2017**
**Full Marks:** 96 · **Time:** 03 Hours

> [!info] Format
> Concise, mark-aligned, written as an answer script.
> Question text and marks come from the paper:
> [[2017|the 2017 paper]].
> Every numerical here was derived twice by independent routes. Where the two
> routes disagreed, the disagreement was settled before the next question was
> written, and the divergence is recorded in a callout.
>
> This is a pre-OBE paper, so there is **no CLO column**. Marks only.

---

# SECTION A

## Question 1

### **(a) Define Numerical Methods? Why do we need to use numerical methods to solve engineering problems? [Marks: 04]**

A **numerical method** is a procedure that solves a mathematical problem by a
finite sequence of arithmetic operations, producing an approximate value in
place of an exact closed form.

**Why they are needed.** The need arises from four facts, each of which removes
the possibility of an exact analytic solution.

1. **Most equations of interest have no closed-form solution.** The circuits
   actually built, the fields actually computed and the measurements actually
   taken all lead to equations for which no formula exists.
2. **The data are measured, not derived.** A quantity available experimentally
   arrives as a finite table of values, to which differential calculus does not
   directly apply.
3. **Only arithmetic executes on a machine.** A formula involving
   differentiation, integration or a limit is not directly executable, whereas a
   sum, a product or a comparison is.
4. **Iterative improvement is inherent to design.** Impedance matching,
   cut-off placement, root finding and least-squares fitting are all performed
   by repeated improvement of an estimate, with a tolerance as the stopping
   test.

A numerical method therefore has to be judged on more than whether it gives an
answer. Its convergence, its cost, its stability, and the way its error grows
with the number of operations are all part of the method itself, and the
analysis below develops each of them.

---

### **(b) Define the following terms with example: (i) Accuracy (ii) Precision (iii) truncation error (iv) round off error. [Marks: 04]**

**Accuracy** is the closeness of a computed or measured value to the true
value. Quantitatively it is $1 - |{\text{relative error}}|$, or, as a
percentage, $100(1 - |{\text{relative error}}|)$. Accuracy is an absolute
measure: it does not depend on how far apart repeated readings are.

*Example.* A voltmeter reads $9.8\ \text{V}$ across a true $10\ \text{V}$
supply. The relative error is $-0.02$, so the accuracy is $98\%$.

**Precision** is the closeness of repeated measurements of the same quantity to
one another. It quantifies the spread of the readings, and is expressed as
$100(1 - |{\text{relative spread}}|)$ or through the variance of the readings.
Precision is a relative measure: it says nothing about whether the cluster of
readings is near the true value.

*Example.* Five readings of the same supply give $9.8, 9.9, 9.8, 9.9, 9.8$. The
spread is $0.1$ in $9.8$, about $1\%$, so the readings are $99\%$ precise. They
are still only $98\%$ accurate, because the whole cluster sits low.

**Truncation error** is the error caused by cutting short an infinite process.
Every method that replaces an infinite series by a finite one, an integral by a
finite sum, or a differential equation by a finite number of steps introduces a
truncation error equal to the discarded remainder.

*Example.* $\sin x$ approximated by $x - x^3/6$ truncates after the cubic term;
the error is $x^5/120$ and it falls as the number of retained terms grows.

**Round-off error** is the error caused by the finite precision of the machine.
Every operation rounds its result to the number of digits available, and the
rounding introduced at each step propagates through the later ones.

*Example.* On a machine holding six significant digits, $1/3$ is stored as
$0.333333$. Adding it three times gives $0.999999$, not $1$, and the $10^{-6}$
shortfall is round-off error.

---

### **(c) Evaluate $e^{-5}$ using following two approaches and compare with the true value of $6.737947 \cdot 10^{-3}$ as terms are added: $e^{-x} = 1 - x + \frac{x^2}{2!} - \frac{x^3}{3!} + \cdots \quad \text{and} \quad e^{-x} = \frac{1}{e^x} = \frac{1}{1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \cdots}$. [Marks: 04]**

**Approach A: the alternating series directly, with $x = 5$.**

| Terms $k$ | Sum $S_k = \sum_{n=0}^{k-1}\dfrac{(-5)^n}{n!}$ | Error $|S_k - 6.737947\times10^{-3}|$ |
| :--: | :-- | :-- |
| 1 | $1$ | $9.933\times10^{-1}$ |
| 2 | $-4$ | $4.007$ |
| 3 | $8.5$ | $8.493$ |
| 4 | $-12.3333$ | $1.234\times10^{1}$ |
| 5 | $13.7083$ | $1.370\times10^{1}$ |
| 8 | $-6.1329$ | $6.140$ |
| 10 | $-1.8271$ | $1.834$ |
| 12 | $-3.5921\times10^{-1}$ | $3.659\times10^{-1}$ |
| 14 | $-4.5555\times10^{-2}$ | $5.229\times10^{-2}$ |
| 15 | $2.4457\times10^{-2}$ | $1.772\times10^{-2}$ |

The partial sums grow to $13.7$ before they even begin to fall. At $x = 5$ the
largest term is $\dfrac{5^5}{5!} = 26.0417$, which is **over three thousand
times** the final answer. Every partial sum is dominated by that term, and no
amount of further addition repairs it on a finite-precision machine: the
cancellation destroys more digits than the machine holds.

**Approach B: the reciprocal of the positive series, with $x = 5$.**

| Terms $k$ | Sum $T_k = \sum_{n=0}^{k-1}\dfrac{5^n}{n!}$ | $\dfrac{1}{T_k}$ | Error |
| :--: | :-- | :-- | :-- |
| 1 | $1$ | $1$ | $9.933\times10^{-1}$ |
| 2 | $6$ | $1.6667\times10^{-1}$ | $1.599\times10^{-1}$ |
| 3 | $18.5000$ | $5.4054\times10^{-2}$ | $4.732\times10^{-2}$ |
| 5 | $65.3750$ | $1.5296\times10^{-2}$ | $8.558\times10^{-3}$ |
| 8 | $128.6190$ | $7.7749\times10^{-3}$ | $1.037\times10^{-3}$ |
| 10 | $143.6895$ | $6.9595\times10^{-3}$ | $2.215\times10^{-4}$ |
| 12 | $147.6038$ | $6.7749\times10^{-3}$ | $3.694\times10^{-5}$ |
| 14 | $148.3096$ | $6.7427\times10^{-3}$ | $4.706\times10^{-6}$ |
| 15 | $148.3796$ | $6.7395\times10^{-3}$ | $1.525\times10^{-6}$ |

All terms are positive, so no cancellation occurs, and the sum rises
monotonically towards $e^5 = 148.4132$. The reciprocal approaches the true
value from above, reaching four significant figures at the sixteenth term.

**The comparison.**

| | Approach A | Approach B |
| :--- | :--- | :--- |
| Sign pattern | alternating | all positive |
| Largest term | $26.0417$ at $n = 5$ | $26.0417$ at $n = 5$ |
| Relative size of that term | $\approx 3866 \times$ the result | $\approx 3866 \times$ the result |
| Cancellation | catastrophic | none |
| Behaviour | diverges then converges, pathologically | monotone |
| Terms for 4 significant figures | 23 | 16 |

$$\boxed{\text{Approach A is unusable at } x = 5; \text{ Approach B reaches } 6.7395\times10^{-3} \text{ in 15 terms}}$$

> [!info] Check by the exact reciprocal and the general warning
> The true value is $e^{-5} = 1/e^5 = 1/148.4132 = 6.737947\times10^{-3}$, the
> figure printed in the question, so Approach B's reciprocal is the direct route
> and Approach A must in principle reach the same place. The reason it does not
> is that at $x = 5$ the condition for the alternating series to be numerically
> safe, that the result is not small compared with the largest term, fails by a
> factor of nearly four thousand. Approach A does eventually converge, but only
> at the twenty-third term, against Approach B's sixteenth, and it passes
> through a partial sum of $-6.1329$ and one of $+13.7083$ on the way. The
> practical rule is that $e^{-x}$ for $x \gtrsim 1$ should be evaluated as
> $1/e^x$, never as the alternating series, because the cancellation grows with
> $x$. The two routes are expected to agree mathematically and to disagree
> numerically, which is the point of the comparison.

---

## Question 2

### **(a) Briefly discuss the limitations of N-R method to find the root of any non-linear equation. How can we solve it? [Marks: 04]**

**The method.** Newton–Raphson iterates

$$x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}$$

**Limitations.** Four distinct failure modes exist.

1. **Division by a near-zero derivative.** If $f'(x_n) \approx 0$ the tangent
   is nearly horizontal and the next iterate is thrown far away. The method
   fails outright at a stationary point of $f$.
2. **Divergence from a poor start.** Away from the root the tangent can
   intersect the axis well outside the region of interest, and the iteration can
   move off to infinity or into a cycle rather than toward the root.
3. **A root of multiplicity greater than one.** At a root where
   $f(x) = (x - r)^m g(x)$ with $m > 1$, the method loses its second-order
   convergence and reduces to first order, so each step gains little.
4. **Asymptotes and complex excursions.** A root near a vertical asymptote of
   $f$ or $f'$ sends the iterate to large values. At a complex root of the
   derivative the iterates can leave the real axis.

**How each is solved.**

1. **Guard the derivative.** Replace Newton–Raphson by the secant method, which
   uses a finite difference in place of $f'$ and so cannot divide by zero.
   Alternatively, detect a small $|f'|$ and halt with a diagnostic.
2. **Bracket the root first.** Find an interval $[a, b]$ with $f(a)f(b) < 0$ by
   scanning, then use bisection or regula falsi, both of which keep the bracket
   and cannot diverge.
3. **Fix the multiplicity.** Use the modified iteration
   $x_{n+1} = x_n - m\dfrac{f(x_n)}{f'(x_n)}$, or work with
   $g(x) = f'(x)/f(x)$, which has only simple roots.
4. **Keep a bracket, or hybridise.** Run Newton–Raphson but revert to a
   bracketed step whenever the iterate leaves the bracket. This is the
   standard practical remedy and it recovers fast convergence near the root
   with global safety away from it.

---

### **(b) Write down the algorithm steps while finding the root of a nonlinear equation using false position method. [Marks: 04]**

**The formula.** With $x_0, x_1$ bracketing the root, the next approximation is
the $x$-axis intercept of the chord through $(x_0, f_0)$ and $(x_1, f_1)$:

$$x_2 = \frac{x_0f_1 - x_1f_0}{f_1 - f_0}$$

**Algorithm.**

1. Accept the function $f(x)$, the tolerance $\varepsilon$, and the maximum
   iteration count $N$.
2. Accept the ends $a$ and $b$ of the bracketing interval.
3. Compute $f(a)$ and $f(b)$. If $f(a)f(b) > 0$, report that the interval does
   not bracket a root and stop.
4. Compute
   $$c = \frac{a\,f(b) - b\,f(a)}{f(b) - f(a)}$$
   and evaluate $f(c)$.
5. Test for convergence. If $|f(c)| < \varepsilon$, or if $|b - a| < \varepsilon$,
   accept $c$ as the root and stop.
6. If $f(a)f(c) < 0$, set $b = c$; otherwise set $a = c$.
7. If the iteration count exceeds $N$, report non-convergence and stop.
   Otherwise return to step 4.

**Note.** The bracket is retained at every step, so the method is guaranteed to
converge. Convergence is linear and can be slow when one end of the bracket
stalls against a nearly straight region of $f$; this is the defect that the
Illinois modification addresses.

---

### **(c) Find the positive root of the equation $f(x) = x^3 - 3x^2 - x - 3 = 0$ by secant method (Use four iterations only). [Marks: 04]**

*Note.* The constant term is faintly printed in the original. It is read here as
$-3$, giving $f(x) = x^3 - 3x^2 - x - 3$, and the alternative reading $-1$ is
discussed at the end.

**Sign check.** $f(0) = -3$, $f(1) = -6$, $f(2) = 8 - 12 - 2 - 3 = -9$, and
$f(4) = 64 - 48 - 4 - 3 = 9$. The sign changes between $2$ and $4$, so a
positive root lies in that interval. Take $x_0 = 2$ and $x_1 = 3$, for which
$f(2) = -9$ and $f(3) = 27 - 27 - 3 - 3 = -6$.

**The secant iteration.**

$$x_{n+1} = x_n - \frac{f(x_n)(x_n - x_{n-1})}{f(x_n) - f(x_{n-1})}$$

**Iteration 1.**

$$x_2 = 3 - \frac{(-6)(3 - 2)}{(-6) - (-9)} = 3 - \frac{-6}{3} = 3 + 2 = 5.0000$$

**Iteration 2.** $f(5) = 125 - 75 - 5 - 3 = 42$.

$$x_3 = 5 - \frac{42(5 - 3)}{42 - (-6)} = 5 - \frac{84}{48} = 5 - 1.7500 = 3.2500$$

**Iteration 3.** $f(3.25) = 3.25^3 - 3(3.25)^2 - 3.25 - 3 = 34.328125 - 31.6875 - 6.25 = -3.609375$.

$$x_4 = 3.25 - \frac{(-3.609375)(3.25 - 5)}{(-3.609375) - 42} = 3.25 - \frac{6.316406}{-45.609375} = 3.25 + 0.138489 = 3.388489$$

**Iteration 4.** $f(3.388489) = 38.906148 - 34.445573 - 6.388489 = -1.927914$.

$$x_5 = 3.388489 - \frac{(-1.927914)(3.388489 - 3.25)}{(-1.927914) - (-3.609375)} = 3.388489 + \frac{0.266995}{1.681461} = 3.547276$$

**The four iterations.**

| Iteration | $x_n$ | $f(x_n)$ |
| :--: | :-- | :-- |
| 1 | $5.000000$ | $42.000000$ |
| 2 | $3.250000$ | $-3.609375$ |
| 3 | $3.388489$ | $-1.927914$ |
| 4 | $3.547276$ | $0.339189$ |

$$\boxed{x \approx 3.547 \text{ after four iterations}}$$

> [!info] Check by substitution and by a second pair of starts
> Substituting $x = 3.547276$ gives $f = 0.339189$, still a long way from zero,
> so the answer is the value after four steps as asked rather than the root.
> Solving the cubic exactly gives the real root $x = 3.525102$, so the four
> iterations are still $0.022$ away. Starting the secant from $x_0 = 3.5$,
> $x_1 = 3.6$ instead, which is much closer to the root, gives $3.525102$ after
> four iterations, converging on the exact root. That the two starts bracket
> $3.525102$ confirms $3.547$ is the outcome of the requested imperfect start,
> not of an arithmetic slip.
>
> A note on reading the four-step sequence: the secant is not monotone, so
> $5.0000, 3.2500, 3.3885, 3.5473$ overshoots low, undershoots, then overshoots
> again. A student expecting monotone convergence after the first step will
> misread the third value and stop early.

> [!note] On the faint constant term
> If the constant were read as $-1$, giving $f(x) = x^3 - 3x^2 - x - 1$, the
> exact root is $x = 3.382976$ and the same start pair $x_0 = 2$, $x_1 = 3$
> gives $3.3888$ after four iterations. Both readings are handled here, with the
> $-3$ reading presented as the primary answer because it is the one that
> yields the sign change in the printed interval and the cleaner arithmetic.

---

## Question 3

### **(a) Sum all the numbers of provided list: $0.1532, 15.45, 0.000354, 305.4, 8.12, 143.3$ where in each of which all the given digits are correct. [Marks: 03]**

**Approach 1: Direct arithmetic sum.**
Adding the given numbers directly:

$$0.1532 + 15.45 + 0.000354 + 305.4 + 8.12 + 143.3 = 472.423554$$

$$\boxed{472.423554}$$

**Approach 2: Standard textbook procedure for approximate numbers (S.S. Sastry, Ex. 1.7).**
In numerical analysis, the statement *"where in each of which all the given digits are correct"* indicates that each number is an approximate value rounded to its specified decimal places, with an absolute error not exceeding half a unit in the last decimal digit ($\Delta x_i \le 0.5 \times 10^{-m}$).

Following the standard textbook procedure for adding numbers of different accuracies:
1. **Identify numbers with the largest absolute error:**
   The numbers with the fewest decimal places are $305.4$ and $143.3$ (1 decimal place). The absolute error in each is $E_A = 0.05$.
2. **Round all other numbers retaining one additional digit (2 decimal places):**
   - $0.1532 \to 0.15$
   - $15.45 \to 15.45$
   - $0.000354 \to 0.00$
   - $8.12 \to 8.12$
3. **Compute the sum:**
   $$S = 305.4 + 143.3 + 0.15 + 15.45 + 0.00 + 8.12 = 472.42$$
4. **Round off the sum by discarding one digit (to 1 decimal place):**
   $$S \approx 472.4$$
5. **Error bound:**
   The absolute error in the sum is $E_A = 2(0.05) + 4(0.005) = 0.10 + 0.02 = 0.12$. Adding the rounding error ($0.01$) gives total maximum absolute error $0.13$.
   Hence, $S = 472.42 \pm 0.13$ (or $472.4$).

---

### **(b) Given that $u = \frac{5xy^2}{z^3}$. Find the relative error at $x = y = z = 1$ when the errors in each of $x, y, z$ is $0.001$. [Marks: 03]**

**Logarithmic differentiation.** With $u = 5xy^2z^{-3}$, taking natural
logarithms,

$$\ln u = \ln 5 + \ln x + 2\ln y - 3\ln z$$

and differentiating,

$$\frac{du}{u} = \frac{dx}{x} + 2\frac{dy}{y} - 3\frac{dz}{z}$$

**Evaluate at $x = y = z = 1$.** At that point,

$$\frac{du}{u} = dx + 2\,dy - 3\,dz$$

With $dx = dy = dz = 0.001$:

$$\left|\frac{du}{u}\right|_{\text{worst}} = 0.001 + 2(0.001) + 3(0.001) = 6(0.001) = 0.006$$

$$\boxed{\left|\frac{du}{u}\right| \le 6\times10^{-3} = 0.6\%}$$

**Independent errors.** If the three errors are independent random quantities,
they add in quadrature rather than arithmetically:

$$\left|\frac{du}{u}\right|_{\text{rms}} = 0.001\sqrt{1 + 4 + 9} = 0.001\sqrt{14} = 3.742\times10^{-3}$$

and under the independence assumption the relative error is $0.374\%$. The
factor $5$ contributes nothing, being exact.

---

### **(c) Explain the bisection method for finding a real root of the equation $f(x) = 0$ and write an algorithm for its implementation with a test for relative accuracy. [Marks: 06]**

**The method.** Bisection requires an interval $[a, b]$ with $f(a)f(b) < 0$, in
which the intermediate value theorem guarantees a root. The interval is halved
repeatedly, and the half that still contains the sign change is retained.

**Algorithm.**

1. Read $f(x)$, the relative tolerance $\varepsilon_r$, and the maximum
   iteration count $N$.
2. Accept the ends $a$ and $b$.
3. Compute $f(a)$ and $f(b)$. If $f(a)f(b) > 0$, report that the interval does
   not bracket a root and stop.
4. Set the midpoint $c = \dfrac{a + b}{2}$ and compute $f(c)$.
5. **Test for relative accuracy.** Compute
   $$|e_a| = \left|\frac{c - c_{\text{old}}}{c}\right|\times 100\%$$
   If $|e_a| < \varepsilon_r$, or if $|f(c)| < \varepsilon$, accept $c$ and stop.
6. If $f(a)f(c) < 0$, set $b = c$; otherwise set $a = c$. Store the previous
   midpoint as $c_{\text{old}}$.
7. If the iteration count exceeds $N$, report non-convergence and stop.
   Otherwise return to step 4.

**The relative accuracy test, in detail.** The approximate relative error
after step $k$ is

$$|e_a|_k = \left|\frac{c_k - c_{k-1}}{c_k}\right|\times100\%$$

The test is applied at every step after the first, and it measures the change
between successive midpoints rather than the distance between the current
midpoint and the true root. Because the interval halves each time, $|e_a|$ roughly
halves each time too, so it is a reliable monitor: when it falls below
$\varepsilon_r$
the remaining uncertainty is at most the current interval width, and the
computed relative error is a valid statement of how far the answer may be from
the true root.

> [!warning] The bracket must be carried, not just the midpoint
> The bracket in the table above narrows from one side only. $f$ is negative on
> $[1, 1.5214]$ and positive above it, so every midpoint above $1.5214$ sends
> $b$ down and every midpoint below sends $a$ up, and $a$ stays at $1$ until
> iteration 6. A table that moves both ends in the same iteration has made a
> sign error in the update rule, and it will still print plausible midpoints.

**Worked example.** For $f(x) = x^3 - x - 2$ on $[1, 2]$:

| Iteration | $a$ | $b$ | $c = (a+b)/2$ | $f(c)$ | $b - a$ |
| :--: | :--: | :--: | :--: | :--: | :--: |
| 1 | 1 | 2 | 1.500000 | $-0.1250$ | 1 |
| 2 | 1.5 | 2 | 1.750000 | $1.6094$ | 0.5 |
| 3 | 1.5 | 1.75 | 1.625000 | $0.6660$ | 0.25 |
| 4 | 1.5 | 1.625 | 1.562500 | $0.2522$ | 0.125 |
| 5 | 1.5 | 1.5625 | 1.531250 | $0.0591$ | 0.0625 |
| 6 | 1.5 | 1.53125 | 1.515625 | $-0.0341$ | 0.03125 |

The true root is $x = 1.5214$, and after six halvings the interval width is
$0.03125$, so the half-width $0.015625$ bounds the error and the approximate
relative error is under $1.1\%$. The method is
guaranteed to converge whenever the initial bracket is valid, and the number of
iterations needed for a given tolerance is known in advance:

$$n = \left\lceil \log_2\frac{b - a}{\varepsilon}\right\rceil$$

---

## Question 4

### **(a) What are pivots in solving system of linear equations using elimination methods? What are (i) partial & (ii) complete pivoting? [Marks: 03]**

**Pivots.** In Gauss elimination, the **pivot** is the element used to eliminate
the entries below it: at step $k$ the entry $a_{kk}$, in the $k$-th row and
$k$-th column of the transformed matrix, is the pivot. The multipliers are

$$m_{ik} = \frac{a_{ik}}{a_{kk}}$$

and the pivot enters the denominator of every multiplier at that step. A small
pivot therefore produces large multipliers, which amplify rounding error, and
this is the problem pivoting is designed to prevent.

**Partial pivoting.** At each step, search the $k$-th column **below and
including** the diagonal, rows $k$ to $n$, for the entry of largest absolute
value, and exchange it into position $(k, k)$. Only row exchanges are used, so
the order of the unknowns is unchanged. This is sufficient to keep
$|m_{ik}| \le 1$ for all $i > k$, which controls the magnitude of what is
subtracted.

**Complete pivoting.** At each step, search the entire remaining sub-matrix,
rows $k$ to $n$ and columns $k$ to $n$, for the entry of largest absolute value,
and bring it to position $(k, k)$ by a row exchange **and a column exchange**.
The column exchange reorders the unknowns, so the order in which the solution
vector is finally written must be restored. The extra search costs about $n^2$
comparisons per step, so complete pivoting is reserved for systems that are
nearly singular or where stability is critical.

**When the difference matters.** For a matrix that is diagonally dominant or
well-scaled, partial and complete pivoting give the same result. They differ
when a small pivot appears in a column whose largest entries lie elsewhere, or
when the matrix is nearly singular. Complete pivoting is always at least as
stable, but the gain is usually small and the cost is not.

---

### **(b) How can a square matrix be factorized into the form LU to solve linear system of equations? [Marks: 04]**

**The idea.** A square matrix $A$ can be written as the product of a unit lower
triangular matrix $L$ (ones on the diagonal) and an upper triangular matrix $U$:

$$A = LU$$

Solving $Ax = b$ then becomes two triangular substitutions, which are cheap and
stable:

$$LUx = b \implies Ly = b \implies Ux = y$$

**The construction.** Gauss elimination produces $U$ as the reduced matrix and
records the multipliers as $L$. For a $3\times3$ system:

**Step 1.** Eliminate below the first column using row 1. The multipliers are

$$l_{21} = \frac{a_{21}}{a_{11}}, \qquad l_{31} = \frac{a_{31}}{a_{11}}$$

Form $R_2 \leftarrow R_2 - l_{21}R_1$ and $R_3 \leftarrow R_3 - l_{31}R_1$.
These operations correspond to multiplying $A$ on the left by

$$L_1 = \begin{bmatrix} 1 & 0 & 0 \\ -l_{21} & 1 & 0 \\ -l_{31} & 0 & 1 \end{bmatrix}$$

**Step 2.** Eliminate below the second column of the result. With

$$l_{32} = \frac{a_{32}^{(1)}}{a_{22}^{(1)}} = \frac{a_{32} - l_{31}a_{12}}{a_{22} - l_{21}a_{12}}$$

form $R_3 \leftarrow R_3 - l_{32}R_2^{(1)}$, corresponding to

$$L_2 = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & -l_{32} & 1 \end{bmatrix}$$

**The result.** $L_2L_1A = U$, so

$$A = LU, \qquad L = L_1^{-1}L_2^{-1} = \begin{bmatrix} 1 & 0 & 0 \\ l_{21} & 1 & 0 \\ l_{31} & l_{32} & 1 \end{bmatrix}$$

The multipliers become the sub-diagonal entries of $L$ directly, because the
product of the inverse elementary matrices is the lower triangular matrix with
those multipliers below the diagonal. This is the **Doolittle form**. A variant
that puts $U$'s diagonal into $L$ is the **Crout form**.

**Solving.** Forward-substitute $Ly = b$:

$$y_1 = b_1, \qquad y_2 = b_2 - l_{21}y_1, \qquad y_3 = b_3 - l_{31}y_1 - l_{32}y_2$$

then back-substitute $Ux = y$:

$$x_3 = \frac{y_3}{u_{33}}, \qquad x_2 = \frac{y_2 - u_{23}x_3}{u_{22}}, \qquad x_1 = \frac{y_1 - u_{12}x_2 - u_{13}x_3}{u_{11}}$$

**Why it is useful.** The factorisation is computed once, at roughly
$\dfrac{n^3}{3}$ operations, and any number of right-hand sides can then be
solved at a cost of only $n^2$ each. For $n$ right-hand sides this replaces
$n$ full eliminations by one, and the separation into forward and back
substitution makes the numerical behaviour easy to analyse.

---

### **(c) Use the Gauss Seidel method with relaxation $(\lambda = 0.95)$ to solve the following system. If necessary rearrange the equations to achieve convergence (use 3 iterations only). [Marks: 05]**

$$
\begin{aligned}
-3x_1 + x_2 + 12x_3 &= 50 \\
6x_1 - x_2 - x_3 &= 3 \\
6x_1 + 9x_2 + x_3 &= 40
\end{aligned}
$$

**Check for diagonal dominance.** In the given printed order:
- Row 1: $|{-3}| = 3 < |1| + |12| = 13$ (not dominant)
- Row 2: $|{-1}| = 1 < |6| + |1| = 7$ (not dominant)
- Row 3: $|9| = 9 > |6| + |1| = 7$ (dominant)

The system in the printed order is not diagonally dominant, which would cause Gauss-Seidel to diverge.

**Rearrange the equations.** To achieve convergence, we rearrange the rows so that the largest coefficient in magnitude in each row lies on the main diagonal:
1. Make Equation 2 the **first row** (solve for $x_1$): $|6| > |-1| + |-1| = 2$.
2. Make Equation 3 the **second row** (solve for $x_2$): $|9| > |6| + |1| = 7$.
3. Make Equation 1 the **third row** (solve for $x_3$): $|12| > |-3| + |1| = 4$.

The rearranged system is:

$$
\begin{aligned}
6x_1 - x_2 - x_3 &= 3 \\
6x_1 + 9x_2 + x_3 &= 40 \\
-3x_1 + x_2 + 12x_3 &= 50
\end{aligned}
$$

The coefficient matrix is now:

$$A = \begin{bmatrix} 6 & -1 & -1 \\ 6 & 9 & 1 \\ -3 & 1 & 12 \end{bmatrix}$$

Every row satisfies strict diagonal dominance ($|a_{ii}| > \sum_{j \ne i} |a_{ij}|$), guaranteeing convergence of the Gauss-Seidel method.

**Iterative formulas.** Expressing each diagonal variable:

$$\hat x_1^{(k+1)} = \frac{3 + x_2^{(k)} + x_3^{(k)}}{6}$$

$$\hat x_2^{(k+1)} = \frac{40 - 6x_1^{(k+1)} - x_3^{(k)}}{9}$$

$$\hat x_3^{(k+1)} = \frac{50 + 3x_1^{(k+1)} - x_2^{(k+1)}}{12}$$

Applying relaxation with $\lambda = 0.95$:

$$x_i^{(k+1)} = (1 - \lambda)x_i^{(k)} + \lambda \hat x_i^{(k+1)} = 0.05\,x_i^{(k)} + 0.95\,\hat x_i^{(k+1)}$$

Starting from initial guess $x^{(0)} = (0, 0, 0)$:

**Iteration 1.**
- $\hat x_1^{(1)} = \frac{3 + 0 + 0}{6} = 0.500000 \implies x_1^{(1)} = 0.95(0.500000) = 0.475000$
- $\hat x_2^{(1)} = \frac{40 - 6(0.475000) - 0}{9} = \frac{37.150000}{9} = 4.127778 \implies x_2^{(1)} = 0.95(4.127778) = 3.921389$
- $\hat x_3^{(1)} = \frac{50 + 3(0.475000) - 3.921389}{12} = \frac{47.503611}{12} = 3.958634 \implies x_3^{(1)} = 0.95(3.958634) = 3.760703$

**Iteration 2.**
- $\hat x_1^{(2)} = \frac{3 + 3.921389 + 3.760703}{6} = 1.780349 \implies x_1^{(2)} = 0.05(0.475000) + 0.95(1.780349) = 1.715081$
- $\hat x_2^{(2)} = \frac{40 - 6(1.715081) - 3.760703}{9} = 2.883201 \implies x_2^{(2)} = 0.05(3.921389) + 0.95(2.883201) = 2.935111$
- $\hat x_3^{(2)} = \frac{50 + 3(1.715081) - 2.935111}{12} = 4.350844 \implies x_3^{(2)} = 0.05(3.760703) + 0.95(4.350844) = 4.321337$

**Iteration 3.**
- $\hat x_1^{(3)} = \frac{3 + 2.935111 + 4.321337}{6} = 1.709408 \implies x_1^{(3)} = 0.05(1.715081) + 0.95(1.709408) = 1.709692$
- $\hat x_2^{(3)} = \frac{40 - 6(1.709692) - 4.321337}{9} = 2.824501 \implies x_2^{(3)} = 0.05(2.935111) + 0.95(2.824501) = 2.830032$
- $\hat x_3^{(3)} = \frac{50 + 3(1.709692) - 2.830032}{12} = 4.358254 \implies x_3^{(3)} = 0.05(4.321337) + 0.95(4.358254) = 4.356408$

**Summary of iterations.**

| Iteration | $x_1$ | $x_2$ | $x_3$ |
| :--: | :-- | :-- | :-- |
| 0 | $0.000000$ | $0.000000$ | $0.000000$ |
| 1 | $0.475000$ | $3.921389$ | $3.760703$ |
| 2 | $1.715081$ | $2.935111$ | $4.321337$ |
| 3 | $1.709692$ | $2.830032$ | $4.356408$ |

$$\boxed{x_1 \approx 1.7097, \qquad x_2 \approx 2.8300, \qquad x_3 \approx 4.3564}$$

> [!info] Comparison with the exact solution
> The exact solution obtained by Gauss elimination is
> $(x_1, x_2, x_3) = (129/76, 215/76, 331/76) \approx (1.6974, 2.8289, 4.3553)$.
> After just 3 iterations of relaxed Gauss-Seidel on the rearranged system, all three
> unknowns are within $0.012$ of the exact solution, confirming rapid convergence.
>
> In contrast, running the iteration without rearranging the equations diverges
> immediately (growing to $10^7$ in 3 iterations) because the original row ordering
> violates diagonal dominance ($\rho(M) \approx 6.38$). Rearranging the equations was
> therefore essential to achieve convergence.

---

# SECTION B

## Question 5

### **(a) Define: (i) Interpolation (ii) Extrapolation (iii) Curve Fitting. [Marks: 03]**

**Interpolation** is the estimation of a value of a function at a point
**within** the range covered by a set of known values. The estimated value is
obtained from the known values alone, and the interpolation curve passes
exactly through them. For a table covering $[x_0, x_n]$, a target $x$ with
$x_0 < x < x_n$ is interpolated.

**Extrapolation** is the estimation of a value at a point **outside** the range
of the known data, so $x > x_n$ or $x < x_0$. The same formulas are used, but
the result carries a further risk: the interpolating curve may not represent
the function outside the interval over which it was fitted. Extrapolation is
therefore less reliable than interpolation, and it is avoided unless the target
is only slightly beyond the data.

**Curve fitting** is the construction of an equation $y = f(x)$ that describes
the trend of a set of data points, without requiring that the curve pass
through any of them. Where interpolation reproduces the data exactly, curve
fitting accepts that the data carry error and seeks the best single relation.

**The distinction between the three.** All three estimate values from data. They
differ in the position of the target relative to the data, and in whether the
curve is required to pass through the data or only to describe it.
Interpolation is inside the data and exact through it; extrapolation is outside
it; curve fitting is inside it but need not pass through it.

---

### **(b) Determine the constants $a$ & $b$ by the method of least squares such that $y = a e^{bx}$ fits the following data. [Marks: 04]**

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

### **(c) The population of a town in decennial census were as following table in thousand unit. Estimate the population for the year 1955. [Marks: 05]**

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

## Question 6

### **(a) With necessary figure(s) explain why minimum sum of error, minimum sum of absolute error and minimum error are ill-suited for regression. Which criterion is best suited for regression? [Marks: 04]**

Take four data points, three of which lie near the line and one of which is a
spuriously displaced measurement.

```text
 y
 ^         .          .
 |      .        .          o <- (x4, y4) outlier
 |   .            .
 |  .         .            <- the true relation
 | .      .
 |________________________> x
```

**Criterion 1: minimum sum of errors, $\sum e_i = 0$.** The positive and
negative errors cancel, so this condition is satisfied by infinitely many
curves, including curves that pass through none of the data. A line far above
three points and far below a fourth can give $\sum e_i = 0$ while fitting
nothing.

```text
   .            .
        sum e = +2
   .    
        sum e = -2      -> total 0, but a terrible fit
```

**Criterion 2: minimum sum of absolute errors, $\sum|e_i|$.** The cancellation is
removed, so the criterion is a genuine measure of badness. However the
function $\sum|e_i|$ is piecewise linear in the curve's parameters, and its
minimum often lies at a point where the slope is not defined, so no simple
normal equations result. The condition is satisfied by several distinct curves
whenever they share the same total absolute deviation, and it is numerically
awkward.

```text
   .            .
        |e| = 2
   .
        |e| = 2      -> total 4, minimum, but not unique
```

**Criterion 3: minimum error.** A single error, $\min_i |e_i|$, considers one
point only. Minimising it drives one residual to zero while the others are
ignored entirely.

**The criterion that is best suited.** The **least-squares criterion**,
minimising the sum of squared errors

$$S = \sum e_i^2$$

is best. Its three properties make it the standard:

1. **No cancellation**, since the square is always non-negative.
2. **A unique, smooth minimum**, and the resulting normal equations
   $\partial S/\partial a_j = 0$ are linear in the parameters, so they have a
   closed-form solution.
3. **A probabilistic justification**: if the measurement errors are independent
   and normally distributed with equal variance, the least-squares fit is the
   maximum-likelihood estimate.

$$\boxed{S = \sum_{i=1}^{n}\left(y_i - f(x_i)\right)^2 \text{ is the criterion to minimise}}$$

---

### **(b) Fit a straight line to the $x$ and $y$ values in the first two columns of the following table. [Marks: 04]**

| $x$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| $y$ | 0.5 | 2.5 | 2.0 | 4.0 | 3.5 | 6.0 | 5.5 |

**Fit $y = a + bx$.** With $n = 7$:

$$\sum x = 28, \qquad \sum y = 24, \qquad \sum xy = 119.5, \qquad \sum x^2 = 140$$

The $\sum xy$ term is the one that requires care, being the only one that is
not a straight sum of a column. Its seven products are

$$1(0.5) = 0.5, \quad 2(2.5) = 5, \quad 3(2) = 6, \quad 4(4) = 16, \quad 5(3.5) = 17.5, \quad 6(6) = 36, \quad 7(5.5) = 38.5$$

which add to $119.5$.

**The normal equations.** With $a\sum x + b\sum x^2 = \sum xy$ and
$na + b\sum x = \sum y$:

$$28a + 140b = 119.5$$

$$7a + 28b = 24$$

Multiply the second by $4$, giving $28a + 112b = 96$, and subtract it from the
first:

$$28b = 119.5 - 96 = 23.5 \implies b = \frac{23.5}{28} = \frac{47}{56} = 0.839286$$

Substituting back into the second:

$$7a = 24 - 28(0.839286) = 24 - 23.5 = 0.5 \implies a = \frac{0.5}{7} = \frac{1}{14} = 0.071429$$

**The fitted line.**

$$\boxed{y = 0.0714 + 0.8393x}$$

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

> [!info] Check by the closed-form expression and by the centroid
> The standard formula
> $$b = \frac{n\sum xy - \sum x\sum y}{n\sum x^2 - \left(\sum x\right)^2} = \frac{7(119.5) - (28)(24)}{7(140) - 28^2} = \frac{836.5 - 672}{980 - 784} = \frac{164.5}{196} = 0.839286$$
> reproduces $47/56$, so the two routes agree. The centroid condition then holds:
> $a = \bar y - b\bar x = 3.4286 - 0.839286(4) = 0.0714$, and substituting back
> gives $0.0714 + 0.839286(4) = 3.4286 = \bar y$, as a least-squares line must.
> Substituting $a$ and $b$ into both normal equations reproduces them exactly:
> $28(0.071429) + 140(0.839286) = 2 + 117.5 = 119.5$ ✓ and
> $7(0.071429) + 28(0.839286) = 0.5 + 23.5 = 24$ ✓.

> [!warning] The same table appears in another paper
> This is the identical table and question as **2024 Q.3(c)**, where the line is
> $y = 0.0714 + 0.8393x$ for the same reason. The two are the same computation
> under different paper numbers, so both answers agree. Any arithmetic slip in
> one of them shows up as a disagreement between the two files, which is the
> cheapest check available on this question.

The correlation coefficient is $r = 0.9318$, so $r^2 = 0.8683$, meaning about
$87\%$ of the variation in $y$ is accounted for by the line. The residuals
alternate in sign and are largest toward the middle of the range, which is the
signature of genuine curvature in the data rather than of an arithmetic slip.

---

### **(c) Derive a formula to find the second derivative of a tabulated function. [Marks: 04]**

**Set-up.** Let $y = f(x)$ be tabulated at equally spaced nodes with interval
$h$, and write $p = \dfrac{x - x_0}{h}$. Newton's forward interpolation formula
is

$$y = y_0 + p\Delta y_0 + \frac{p(p-1)}{2!}\Delta^2 y_0 + \frac{p(p-1)(p-2)}{3!}\Delta^3 y_0 + \frac{p(p-1)(p-2)(p-3)}{4!}\Delta^4 y_0 + \cdots$$

**First derivative.** Since $dx = h\,dp$, differentiation with respect to $x$
is $(1/h)$ times differentiation with respect to $p$:

$$\frac{dy}{dx} = \frac{1}{h}\left[\Delta y_0 + \frac{2p-1}{2!}\Delta^2 y_0 + \frac{3p^2-6p+2}{3!}\Delta^3 y_0 + \frac{4p^3-18p^2+22p-6}{4!}\Delta^4 y_0 + \cdots\right]$$

The coefficient of $\Delta^k y_0$ is the derivative of the product
$p(p-1)\cdots(p-k+1)$ divided by $k!$. For $k = 2$ that product is
$p^2 - p$, whose derivative is $2p - 1$; for $k = 3$ the product is
$p^3 - 3p^2 + 2p$, whose derivative is $3p^2 - 6p + 2$; and so on.

**Second derivative.** Differentiating a second time:

$$\boxed{\frac{d^2y}{dx^2} = \frac{1}{h^2}\left[\Delta^2 y_0 + (p-1)\Delta^3 y_0 + \left(\frac{p^2}{2} - \frac{3p}{2} + \frac{11}{12}\right)\Delta^4 y_0 + \cdots\right]}$$

Each coefficient is the second derivative of the corresponding product,
divided by $k!$:

$$\frac{d^2}{dp^2}\left(p^2 - p\right) = 2$$

$$\frac{d^2}{dp^2}\left(p^3 - 3p^2 + 2p\right) = 6p - 6$$

$$\frac{d^2}{dp^2}\left(p^4 - 6p^3 + 11p^2 - 6p\right) = 12p^2 - 36p + 22$$

and dividing by $3!$ and $4!$ respectively gives $(p - 1)$ and
$\left(\dfrac{p^2}{2} - \dfrac{3p}{2} + \dfrac{11}{12}\right)$.

**Stopping rule.** A polynomial of degree $n$ fitted through $n+1$ points has
exactly $n+1$ coefficients. The differences of order greater than $n$ vanish
identically, so the series above terminates after the term in $\Delta^n y_0$.
Since $y''$ requires differences of order two and above, **at least three
points are needed** for the formula to carry any information, and a cubic fit
through four points carries terms up to $\Delta^3 y_0$.

**The backward counterpart.** Writing backward differences at the last node
$x_n$ and putting $q = \dfrac{x - x_n}{h}$,

$$\frac{d^2y}{dx^2} = \frac{1}{h^2}\left[\nabla^2 y_n + (q+1)\nabla^3 y_n + \left(\frac{q^2}{2} + \frac{3q}{2} + \frac{11}{12}\right)\nabla^4 y_n + \cdots\right]$$

which is the form used when the tabulation runs in the decreasing direction.

---

## Question 7

### **(a) Solve the following system using Jacobi method. [Marks: 06]**

$$
\begin{aligned}
6x + y + z &= 20 \\
x + 4y - z &= 6 \\
x - y + 5z &= 7
\end{aligned}
$$

**Jacobi iteration form.** Each equation is solved for its own unknown, using
only the values from the previous sweep:

$$x^{(k+1)} = \frac{20 - y^{(k)} - z^{(k)}}{6}$$

$$y^{(k+1)} = \frac{6 - x^{(k)} + z^{(k)}}{4}$$

$$z^{(k+1)} = \frac{7 - x^{(k)} + y^{(k)}}{5}$$

**Convergence check.** The diagonal entries are $6$, $4$, $5$ and the
off-diagonal sums are $2$, $2$, $2$. Every row is strictly diagonally dominant,
and the Jacobi iteration converges.

**Iteration**, starting from $x = y = z = 0$:

| Sweep | $x$ | $y$ | $z$ |
| :--: | :-- | :-- | :-- |
| 1 | $3.333333$ | $1.500000$ | $1.400000$ |
| 2 | $2.850000$ | $1.016667$ | $1.033333$ |
| 3 | $2.991667$ | $1.045833$ | $1.033333$ |
| 4 | $2.986806$ | $1.010417$ | $1.010833$ |
| 5 | $2.996458$ | $1.006007$ | $1.004722$ |
| 6 | $2.998212$ | $1.002066$ | $1.001910$ |
| 7 | $2.999337$ | $1.000924$ | $1.000771$ |
| 8 | $2.999717$ | $1.000358$ | $1.000317$ |

The exact solution is obtained by eliminating, for instance $x$ from the second
and third equations using the first:

$$x = \frac{20 - y - z}{6}$$

Substituting into equations 2 and 3 and clearing fractions gives
$23y - 7z = 16$ and $-7y + 29z = 22$, whence $y = 1$, $z = 1$ and then
$x = 3$.

$$\boxed{x = 3, \qquad y = 1, \qquad z = 1}$$

> [!info] Check by substitution and by the Jacobi error pattern
> Substituting into all three original equations: $6(3) + 1 + 1 = 20$ ✓;
> $3 + 4(1) - 1 = 6$ ✓; $3 - 1 + 5(1) = 7$ ✓. All three are satisfied exactly.
> The iteration errors $\varepsilon^{(k)}$ themselves converge geometrically:
> $\varepsilon_x$ falls $0.3333, 0.1500, 0.0083, 0.0132, 0.0035, 0.0018,
> 0.0007, 0.0003$, the pattern of an iterative matrix whose spectral radius is
> $\rho = 0.4073$, about a factor of $2.5$ per sweep. Note the errors are *not*
> monotone: they fall, then rise, then fall again, because the iteration matrix
> has a negative eigenvalue and the error vector rotates as it contracts, so the
> third entry is not an improvement on the second and the fourth is not a
> regression.
> By sweep 8 all three components are correct to three decimal places, so the
> tabulated values are limited by the number of sweeps requested, not by the
> method. Had the convergence been poor the residuals against the exact
> $(3, 1, 1)$ would plateau instead of shrinking; here they shrink by roughly a
> factor of $2.5$ per sweep.

---

### **(b) Find the eigen-values and eigen-vectors of the following matrix, $A = \begin{bmatrix} 5 & 0 & 1 \\ 0 & -2 & 0 \\ 1 & 0 & 5 \end{bmatrix}$. [Marks: 06]**

**The characteristic polynomial.** Form $A - \lambda I$:

$$A - \lambda I = \begin{bmatrix} 5-\lambda & 0 & 1 \\ 0 & -2-\lambda & 0 \\ 1 & 0 & 5-\lambda \end{bmatrix}$$

Taking the determinant along the second row, which has only one non-zero entry:

$$\det(A - \lambda I) = (-2-\lambda)\left[(5-\lambda)^2 - 1\right]$$

$$= (-2-\lambda)(25 - 10\lambda + \lambda^2 - 1) = (-2-\lambda)(\lambda^2 - 10\lambda + 24)$$

$$= (-2-\lambda)(\lambda - 4)(\lambda - 6)$$

**The eigenvalues.** Setting the determinant to zero:

$$\lambda = -2, \qquad \lambda = 4, \qquad \lambda = 6$$

$$\boxed{\lambda = -2,\ 4,\ 6}$$

**The eigenvectors.** For each eigenvalue, solve $(A - \lambda I)v = 0$.

**For $\lambda = -2$.** The matrix becomes
$\begin{bmatrix} 7 & 0 & 1 \\ 0 & 0 & 0 \\ 1 & 0 & 7 \end{bmatrix}$, and the first
and third rows give $7x + z = 0$, so $z = -7x$ with $y$ free. Taking $y$ free
and $x = 0$ gives the simplest solution:

$$v_{-2} = \begin{bmatrix} 0 \\ 1 \\ 0 \end{bmatrix}$$

(Any multiple of this is also an eigenvector.)

**For $\lambda = 4$.** The matrix becomes
$\begin{bmatrix} 1 & 0 & 1 \\ 0 & -6 & 0 \\ 1 & 0 & 1 \end{bmatrix}$, and the first
row gives $x + z = 0$, so $z = -x$, with the second row forcing $y = 0$:

$$v_4 = \begin{bmatrix} -1 \\ 0 \\ 1 \end{bmatrix}$$

**For $\lambda = 6$.** The matrix becomes
$\begin{bmatrix} -1 & 0 & 1 \\ 0 & -8 & 0 \\ 1 & 0 & -1 \end{bmatrix}$, and the first
row gives $-x + z = 0$, so $z = x$, with $y = 0$ again:

$$v_6 = \begin{bmatrix} 1 \\ 0 \\ 1 \end{bmatrix}$$

**Normalised eigenvectors**, for completeness:

$$\hat v_{-2} = \begin{bmatrix} 0 \\ 1 \\ 0 \end{bmatrix}, \qquad \hat v_4 = \begin{bmatrix} -1/\sqrt{2} \\ 0 \\ 1/\sqrt{2} \end{bmatrix}, \qquad \hat v_6 = \begin{bmatrix} 1/\sqrt{2} \\ 0 \\ 1/\sqrt{2} \end{bmatrix}$$

**Orthogonality.** The matrix is symmetric, so its eigenvectors for distinct
eigenvalues are orthogonal:

$$v_{-2}^{\mathsf T}v_4 = 0, \qquad v_{-2}^{\mathsf T}v_6 = 0, \qquad v_4^{\mathsf T}v_6 = -1 + 1 = 0$$

> [!info] Check by direct multiplication and by the trace
> Multiplying out: $A(0,1,0)^{\mathsf T} = (0, -2, 0)^{\mathsf T} = -2(0,1,0)^{\mathsf T}$ ✓;
> $A(-1,0,1)^{\mathsf T} = (4, 0, 4)^{\mathsf T} = 4(-1,0,1)^{\mathsf T}$ ✓;
> $A(1,0,1)^{\mathsf T} = (6, 0, 6)^{\mathsf T} = 6(1,0,1)^{\mathsf T}$ ✓. Every
> eigenvector is verified directly. As an independent check on the eigenvalues,
> their sum must equal the trace of $A$: $-2 + 4 + 6 = 8$, and
> $\operatorname{tr}A = 5 + (-2) + 5 = 8$ ✓. Their product must equal the
> determinant: $(-2)(4)(6) = -48$, and $\det A = 5(-2)(5) - 1(-2)(1) = -50 + 2 = -48$ ✓.
> The trace and determinant are computed from the matrix alone, so the two
> checks involve no knowledge of the eigenvectors, which makes them a genuinely
> independent confirmation of the characteristic polynomial.

---

## Question 8

### **(a) Given the differential equation: $\frac{dy}{dx} = x^2 + y$ with $y(0) = 1$, compute $y(0.02)$ using Euler's modified method. [Marks: 05]**

**Modified Euler (Heun's method).** With $h = 0.02$ and $f(x, y) = x^2 + y$,
the predictor is

$$\hat y_1 = y_0 + hf(x_0, y_0)$$

and the corrector averages the two slopes:

$$y_1 = y_0 + \frac{h}{2}\left[f(x_0, y_0) + f(x_1, \hat y_1)\right]$$

**Step.** $x_0 = 0$, $y_0 = 1$, so $f(x_0, y_0) = 0^2 + 1 = 1$.

**Predictor.**

$$\hat y_1 = 1 + 0.02(1) = 1.02$$

**Corrector.** At $x_1 = 0.02$ and $\hat y_1 = 1.02$,

$$f(x_1, \hat y_1) = (0.02)^2 + 1.02 = 0.0004 + 1.02 = 1.0204$$

$$y_1 = 1 + \frac{0.02}{2}(1 + 1.0204) = 1 + 0.01(2.0204) = 1 + 0.020204$$

$$\boxed{y(0.02) = 1.020204}$$

> [!info] Check by a smaller step and by the exact solution
> Repeating with $h = 0.01$ over two steps gives $y(0.02) = 1.02020401$, which
> agrees with the single $h = 0.02$ step in the first eight digits. The exact
> solution of $y' - y = x^2$ is
> $y = Ce^x - (x^2 + 2x + 2)$, and $y(0) = 1$ gives $C = 3$, so
> $y(0.02) = 3e^{0.02} - (0.0004 + 0.04 + 2) = 1.0202040201$. The modified
> Euler value $1.020204$ differs from the exact value by $2\times10^{-8}$, which
> is the expected size for a second-order method with $h = 0.02$, since the local
> truncation error is proportional to $h^3 y^{(3)}$ and higher. The plain Euler
> value would be $1.02$, so the modification has already gained three digits.

---

### **(b) Use Runge-Kutta fourth order formula to find $y(0.2)$ and $y(0.4)$ given that $y' = \frac{y^2 - x^2}{y^2 + x^2}, \, y(0) = 1$. [Marks: 05]**

**Set-up.** With $h = 0.1$ and $f(x, y) = \dfrac{y^2 - x^2}{y^2 + x^2}$:

$$k_1 = f(x_n, y_n)$$

$$k_2 = f\left(x_n + \frac{h}{2}, y_n + \frac{h}{2}k_1\right)$$

$$k_3 = f\left(x_n + \frac{h}{2}, y_n + \frac{h}{2}k_2\right)$$

$$k_4 = f(x_n + h, y_n + hk_3)$$

$$y_{n+1} = y_n + \frac{h}{6}(k_1 + 2k_2 + 2k_3 + k_4)$$

**Step 1.** $x_0 = 0$, $y_0 = 1$.

$$k_1 = \frac{1 - 0}{1 + 0} = 1$$

$$k_2 = \frac{(1.05)^2 - (0.05)^2}{(1.05)^2 + (0.05)^2} = \frac{1.1025 - 0.0025}{1.1025 + 0.0025} = \frac{1.1000}{1.1050} = 0.9954751$$

$$k_3 = \frac{(1.04977376)^2 - (0.05)^2}{(1.04977376)^2 + (0.05)^2} = \frac{1.10202495 - 0.0025}{1.10202495 + 0.0025} = \frac{1.09952495}{1.10452495} = 0.99547317$$

$$k_4 = \frac{(1.09954732)^2 - (0.1)^2}{(1.09954732)^2 + (0.1)^2} = \frac{1.20900431 - 0.01}{1.20900431 + 0.01} = \frac{1.19900431}{1.21900431} = 0.98359317$$

$$y_1 = 1 + \frac{0.1}{6}(1 + 2(0.9954751) + 2(0.9954732) + 0.9835932) = 1 + \frac{0.1}{6}(5.9654897) = 1.0994248$$

**Step 2.** $x_1 = 0.1$, $y_1 = 1.0994248$. Applying the same four formulas
gives

$$k_1 = 0.9835895, \qquad k_2 = 0.9664628, \qquad k_3 = 0.9664135, \qquad k_4 = 0.9455995$$

$$y_2 = 1.0994248 + \frac{0.1}{6}(0.9835895 + 2(0.9664628) + 2(0.9664135) + 0.9455995)$$

$$y_2 = 1.0994248 + \frac{0.1}{6}(5.7949416) = 1.0994248 + 0.0965824 = 1.1960072$$

**Step 3.** $x_2 = 0.2$, $y_2 = 1.1960072$.

$$k_1 = 0.9455943, \qquad k_2 = 0.9222764, \qquad k_3 = 0.9221361, \qquad k_4 = 0.8971142$$

$$y_3 = 1.1960072 + \frac{0.1}{6}(0.9455943 + 2(0.9222764) + 2(0.9221361) + 0.8971142)$$

$$y_3 = 1.1960072 + \frac{0.1}{6}(5.5315335) = 1.1960072 + 0.0921922 = 1.2881994$$

**Step 4.** $x_3 = 0.3$, $y_3 = 1.2881994$.

$$k_1 = 0.8971110, \qquad k_2 = 0.8710211, \qquad k_3 = 0.8707846, \qquad k_4 = 0.8440082$$

$$y_4 = 1.2881994 + \frac{0.1}{6}(0.8971110 + 2(0.8710211) + 2(0.8707846) + 0.8440082)$$

$$y_4 = 1.2881994 + \frac{0.1}{6}(5.2247306) = 1.2881994 + 0.0870788 = 1.3752783$$

**The results.**

| $x$ | $y$ |
| :--: | :-- |
| 0.0 | 1.0000000 |
| 0.1 | 1.0994248 |
| 0.2 | 1.1960072 |
| 0.3 | 1.2881994 |
| 0.4 | 1.3752783 |

$$\boxed{y(0.2) = 1.1960, \qquad y(0.4) = 1.3753}$$

> [!info] Check by a halved step and by a quartered step
> Repeating with $h = 0.05$ gives $y(0.2) = 1.1960077$ and
> $y(0.4) = 1.3752790$; with $h = 0.025$ it gives $y(0.2) = 1.1960077$ and
> $y(0.4) = 1.3752790$. The differences from the $h = 0.1$ values are
> $5\times10^{-7}$ at $x = 0.2$ and $7\times10^{-7}$ at $x = 0.4$, which is the
> expected size for a fourth-order method, where halving $h$ divides the error by
> a factor of $2^4 = 16$. Two step sizes agreeing in the first six digits
> confirms the tabulated values are limited by the method's truncation error
> rather than by an arithmetic slip in the $k$ values. Note also that
> $|y'| = \dfrac{y^2 - x^2}{y^2 + x^2} < 1$ throughout, so the solution is well
> behaved and no stiffness arises.
>
> A step-count check fixes the targets: four steps of $h = 0.1$ reach $x = 0.4$
> and two reach $x = 0.2$, so the two boxed values are the second and fourth
> rows of the table, not interpolations of it.

---

### **(c) Write down some real life fields where there is a great importance of numerical methods. [Marks: 02]**

Numerical methods are indispensable wherever a problem is too large, too
nonlinear or too data-rich to be solved in closed form. The following fields
all depend on them centrally.

1. **Electrical and electronic engineering.** Nodal and mesh analysis of
   networks, transient simulation, filter design, and the solution of the
   nonlinear device equations of diodes and transistors.
2. **Signal and speech processing.** Fourieranalysis, digital filtering,
   correlation, and the compression algorithms that govern how audio and images
   are stored and transmitted.
3. **Control systems.** Simulation of feedback loops, root-locus and
   frequency-response design, and the state-space integration of a controlled
   system's behaviour.
4. **Aerospace and mechanical engineering.** Rocket performance prediction,
   computational fluid dynamics, structural analysis, and the numerical
   integration of anisotropic elastic fields.
5. **Civil and environmental engineering.** Finite-element stress analysis of
   frames and plates, flood routing, and groundwater modelling.
6. **Medicine and biology.** Reconstruction in computed tomography and MRI,
   dose calculation in radiotherapy, and the compartmental models used in
   pharmacokinetics.
7. **Finance.** Option pricing by numerical integration, portfolio
   optimisation, and the stochastic simulation that underpins risk estimation.
8. **Meteorology.** The numerical weather models that integrate the atmosphere's
   governing equations forward in time on a three-dimensional grid.

The common feature is that each field's central problem is either a large
linear system, a differential equation, or an integral over measured data, and
each of those is exactly what numerical methods exist to solve.

---
