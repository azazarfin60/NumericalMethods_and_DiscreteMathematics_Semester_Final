---
title: "ECE 2213 · 2017 Explanations"
tags:
  - numerical-methods
  - discrete-mathematics
  - previous-year
---

# ECE 2213: 2017 Semester Final · Explained

**RUET · ECE Dept · B.Sc. Engineering 2nd Year Even Semester Examination, 2017**

This file explains the same questions as
[[2017_answer|the 2017 answer script]], written to be read
rather than copied. Every step is named, the reason a formula is chosen is
stated, and the traps that catch people are called out.

> [!info] How to use this file
> Read this to understand *why* the answer script does what it does. When you
> are ready to write in the hall, work from
> [[2017_answer|the exam-style file]], which is shorter and
> carries no commentary.
>
> **The rule that matters.** Every boxed number here is the same number as the
> one in the answer script, character for character. Gate V5 checks this, and
> gate V12 checks that the marks on every section agree with the answer script
> and with the manifest.

> [!note] What this paper is made of
> The 2017 paper has **no discrete mathematics at all**: all 23 sub-questions
> are numerical methods, and it carries no CLO column. Questions 1 to 3 are
> error analysis and root finding, Questions 4 to 6 linear systems and curve
> fitting, and Questions 7 and 8 direct and iterative methods.
>
> Several questions here are worth careful study: **Q.1(c)** demonstrates
> catastrophic cancellation in alternating series; **Q.4(c)** highlights the
> critical requirement of rearranging equations to establish diagonal dominance
> before applying Gauss-Seidel; and **Q.2(c)** asks for four secant iterations from
> an exterior start where the iterates oscillate before settling. Understanding
> the structural preconditions and convergence criteria is essential for securing
> full marks in this paper.

---

# SECTION A

## Question 1

### **(a) Define Numerical Methods? Why do we need to use numerical methods to solve engineering problems?**

*[Marks: 04]*

**The definition.** A **numerical method** is a procedure that solves a
mathematical problem by a *finite* sequence of arithmetic operations, producing
an approximate value in place of an exact closed form. Three words carry the
whole idea: *finite*, *arithmetic*, *approximate*.

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

> [!note] The consequence worth writing down
> A numerical method is not judged on whether it gives an answer. It is judged
> on three things: its **convergence**, its **cost**, its **stability**, and
> the way its **error grows with the number of operations**. Everything from
> Q.2(a) onward in this paper is an instance of one of those three.

---

### **(b) Define the following terms with example: (i) Accuracy (ii) Precision (iii) truncation error (iv) round off error.**

*[Marks: 04]*

**Accuracy** is the closeness of a computed or measured value to the *true*
value. Quantitatively it is $1 - |{\text{relative error}}|$, or as a percentage
$100(1 - |{\text{relative error}}|)$. Accuracy is an **absolute** measure: it
says nothing about how far apart repeated readings are.

*Example.* A voltmeter reads $9.8\ \text{V}$ across a true $10\ \text{V}$
supply. The relative error is $-0.02$, so the accuracy is $98\%$.

**Precision** is the closeness of repeated measurements of the same quantity to
*one another*. It quantifies the spread of the readings, and is expressed as
$100(1 - |{\text{relative spread}}|)$ or through the variance. Precision is a
**relative** measure: it says nothing about whether the cluster sits near the
true value.

*Example.* Five readings of the same supply give $9.8, 9.9, 9.8, 9.9, 9.8$. The
spread is $0.1$ against a level of $9.8$, about $1\%$, so the readings are
$99\%$ precise. They are still only $98\%$ accurate, because the whole cluster
sits low.

> [!note] The classic picture, and why both examples are in the question
> Draw four targets. The four groups land on the bullseye, off the bullseye but
> tightly grouped, loosely grouped on the bullseye, and loosely grouped off it.
> **Accuracy** is distance from the bullseye; **precision** is how tightly the
> shots cluster. The pair here, "$99\%$ precise and $98\%$ accurate", is the
> second of those four. A repeatability cluster that sits $2\%$ off is the
> situation where averaging will not help you, and it is worth recognising on
> sight in the laboratory.

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

> [!warning] The pair that students merge
> Truncation error shrinks when you take more terms, more panels or a smaller
> $h$. Round-off error *grows* when you do any of those, because every extra
> operation is another rounding. They have opposite dependence on the same
> quantity, and the total error is not minimised by working harder. This is the
> point of Q.1(c), which is the demonstration rather than the statement.

---

### **(c) Evaluate $e^{-5}$ using following two approaches and compare with the true value of $6.737947 \cdot 10^{-3}$ as terms are added: $e^{-x} = 1 - x + \frac{x^2}{2!} - \frac{x^3}{3!} + \cdots \quad \text{and} \quad e^{-x} = \frac{1}{e^x} = \frac{1}{1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \cdots}$.**

*[Marks: 04]*

**This question is about catastrophic cancellation, and the two approaches are
mathematically identical.** Both compute $e^{-5}$. They differ only in
arithmetic, and at $x = 5$ that difference is fatal.

**Approach A: the alternating series directly, with $x = 5$.**

$$S_k = \sum_{n=0}^{k-1}\frac{(-5)^n}{n!}$$

| Terms $k$ | $S_k$ | Error $\lvert S_k - 6.737947\times10^{-3}\rvert$ |
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

**What is happening.** The partial sums grow to $13.7$ before they begin to
fall. The largest term is $\dfrac{5^5}{5!} = 26.0417$, and the answer is
$0.0067379$, so that one term is about $3866$ times the result.

**Why that destroys the computation.** Each partial sum is formed by adding
alternating terms of size up to $26$ to get a number of size $0.0067$. To hold
a final answer of size $10^{-3}$ to, say, four significant figures, the machine
must retain four digits past the point where cancellation has eaten the
leading digits. If the partial sums are carried to $d$ significant figures and
the largest term is $3866$ times the answer, then all but about
$\log_{10}(3866) \approx 3.6$ of those digits are consumed by cancellation.
The remaining answer is good to roughly $d - 4$ digits, and no amount of
further addition repairs it: each new term is again of size comparable to the
running total. This is **catastrophic cancellation**, and the defining feature
is that the error is *not* reduced by computing more terms.

**Approach B: the reciprocal of the positive series, with $x = 5$.**

$$T_k = \sum_{n=0}^{k-1}\frac{5^n}{n!}, \qquad e^{-5} \approx \frac{1}{T_k}$$

| Terms $k$ | $T_k$ | $\dfrac{1}{T_k}$ | Error |
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

**What is happening.** Every term is positive, so there is **no cancellation at
all**. The sum rises monotonically towards $e^5 = 148.4132$, and its magnitude
never differs wildly from itself, so the machine's digits all survive. The
reciprocal then approaches the true value from above.

$$\boxed{\text{Approach A is unusable at } x = 5; \text{ Approach B reaches } 6.7395\times10^{-3} \text{ in 15 terms}}$$

**The comparison.**

| | Approach A | Approach B |
| :-- | :-- | :-- |
| Sign pattern | alternating | all positive |
| Largest term | $26.0417$ at $n = 5$ | $26.0417$ at $n = 5$ |
| That term relative to the result | $\approx 3866 \times$ | $\approx 3866 \times$ |
| Cancellation | catastrophic | none |
| Behaviour | diverges then converges, pathologically | monotone |
| Terms for 4 significant figures | 23 | 16 |

Note the fourth row of the table. Both approaches have the *same* largest term
relative to the answer. That is exactly why the problem is interesting: the
data are identical and the only thing that differs is the arrangement of the
summation, and that arrangement alone decides whether the machine survives.

> [!info] What the two routes confirm
> The true value is $e^{-5} = 1/e^5 = 1/148.4132 = 6.737947\times10^{-3}$, the
> figure printed in the question, so Approach B's reciprocal *is* the direct
> route and Approach A must in principle reach the same place. It does, eventually:
> at the twenty-third term the alternating series gets within $3.8\times10^{-7}$,
> which is four significant figures. So Approach A is not *wrong*, it is
> unusable in practice, and the difference between "wrong" and "unusable" is
> worth holding on to.
>
> The practical rule follows: for $x \gtrsim 1$, evaluate $e^{-x}$ as $1/e^x$,
> never as the alternating series, because the cancellation factor is roughly
> $e^x/x!$ and grows without bound as $x$ grows. The same trap appears in
> $\cos x = 1 - x^2/2 + x^4/24 - \cdots$ for large $x$, and in any alternating
> series whose terms peak far above the answer.

> [!warning] The test that catches a fabricated partial-sum column
> Two identities must hold in any such table, and both are one line. The
> *printed sum* must satisfy $1/T_k = $ the *printed reciprocal*, and
> $T_k - T_{k-1} = 5^{k-1}/k!$ must hold between consecutive rows. An earlier
> draft of the answer script carried a column of partial sums that satisfied
> neither, while its reciprocal and error columns were correct for the true
> sums. A table can therefore look entirely reasonable and still be wrong, and
> the only defence is to check one row against the sum rule above.

---

## Question 2

### **(a) Briefly discuss the limitations of N-R method to find the root of any non-linear equation. How can we solve it?**

*[Marks: 04]*

**The method.** Newton-Raphson iterates

$$x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}$$

Geometrically it follows the tangent: the tangent at $x_n$ crosses the axis at
$x_{n+1}$. The local error satisfies $e_{n+1} \approx \dfrac{f''(r)}{2f'(r)}e_n^2$,
which is where the famous quadratic convergence comes from, and also where all
four limitations come from.

**Four distinct failure modes.**

1. **Division by a near-zero derivative.** The tangent is nearly horizontal and
   the next iterate is thrown far away. The method fails outright at a
   stationary point of $f$.
2. **Divergence from a poor start.** Away from the root the tangent can
   intersect the axis well outside the region of interest, and the iteration can
   move off to infinity or into a cycle rather than toward the root.
3. **A root of multiplicity greater than one.** At a root where
   $f(x) = (x-r)^m g(x)$ with $m > 1$, $f'$ also vanishes there, the quadratic
   term in the error relation collapses, and the iteration degrades to first
   order, so each step gains little.
4. **Asymptotes and complex excursions.** A root near a vertical asymptote of
   $f$ or $f'$ sends the iterate to large values; at a complex root of the
   derivative the iterates can leave the real axis entirely.

**How each is solved.**

1. **Guard the derivative.** Replace Newton-Raphson by the secant method, which
   uses a finite difference in place of $f'$ and so cannot divide by zero.
   Alternatively detect a small $\lvert f'\rvert$ and halt with a diagnostic.
2. **Bracket the root first.** Find an interval $[a,b]$ with $f(a)f(b) < 0$ by
   scanning, then use bisection or regula falsi, both of which keep the bracket
   and cannot diverge.
3. **Fix the multiplicity.** Use the modified iteration
   $x_{n+1} = x_n - m\dfrac{f(x_n)}{f'(x_n)}$, or work with
   $g(x) = f'(x)/f(x)$, which has only simple roots.
4. **Keep a bracket, or hybridise.** Run Newton-Raphson but revert to a
   bracketed step whenever the iterate leaves the bracket. This is the standard
   practical remedy and it recovers fast convergence near the root with global
   safety away from it.

> [!note] The unifying idea
> Three of the four failures are the same failure seen from different sides:
> nothing keeps the iterate near the root. The bracket is the only device that
> does, which is why every production root finder of consequence, Brent's method
> among them, is built around one.

---

### **(b) Write down the algorithm steps while finding the root of a nonlinear equation using false position method.**

*[Marks: 04]*

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
5. Test for convergence. If $\lvert f(c)\rvert < \varepsilon$, or if
   $\lvert b - a\rvert < \varepsilon$, accept $c$ as the root and stop.
6. If $f(a)f(c) < 0$, set $b = c$; otherwise set $a = c$.
7. If the iteration count exceeds $N$, report non-convergence and stop.
   Otherwise return to step 4.

**Step 6 is the whole method.** Note carefully that only *one* end of the
bracket moves at each iteration, and which one is decided by the sign of
$f(c)$. Write the test the other way round and the method silently becomes
something that does not converge.

**Note.** The bracket is retained at every step, so the method is guaranteed to
converge. Convergence is linear and can be slow when one end of the bracket
stalls against a nearly straight region of $f$; that is the defect the Illinois
modification addresses, by halving the retained function value at whichever end
failed to update.

---

### **(c) Find the positive root of the equation $f(x) = x^3 - 3x^2 - x - 3 = 0$ by secant method (Use four iterations only).**

*[Marks: 04]*

**What the secant method is.** Replace $f'(x_n)$ by a finite difference through
the last two iterates:

$$x_{n+1} = x_n - \frac{f(x_n)(x_n - x_{n-1})}{f(x_n) - f(x_{n-1})}$$

It needs one function evaluation per step instead of two, keeps roughly the
superlinear convergence of Newton, and has no derivative to divide by. The
price is that it needs *two* starting values and no longer guarantees to
converge from anywhere.

**Sign check.** $f(2) = -9$ and $f(4) = 64 - 48 - 4 - 3 = 9$, so a positive
root lies in $(2, 4)$. Take $x_0 = 2$, $x_1 = 3$, for which
$f(2) = -9$ and $f(3) = 27 - 27 - 3 - 3 = -6$.

**Iteration 1.**

$$x_2 = 3 - \frac{(-6)(3 - 2)}{(-6) - (-9)} = 3 - \frac{-6}{3} = 5.0000$$

**Iteration 2.** $f(5) = 125 - 75 - 5 - 3 = 42$.

$$x_3 = 5 - \frac{42(5 - 3)}{42 - (-6)} = 5 - \frac{84}{48} = 3.2500$$

**Iteration 3.** $f(3.25) = 34.328125 - 31.6875 - 6.25 = -3.609375$.

$$x_4 = 3.25 - \frac{(-3.609375)(3.25 - 5)}{(-3.609375) - 42} = 3.25 + \frac{6.316406}{45.609375} = 3.388489$$

**Iteration 4.** $f(3.388489) = 38.906149 - 34.445573 - 6.388489 = -1.927914$.

$$x_5 = 3.388489 - \frac{(-1.927914)(3.388489 - 3.25)}{(-1.927914) - (-3.609375)} = 3.388489 + \frac{0.266995}{1.681461} = 3.547276$$

**The four iterations.**

| Iteration | $x_n$ | $f(x_n)$ |
| :--: | :-- | :-- |
| 1 | $5.000000$ | $42.000000$ |
| 2 | $3.250000$ | $-3.609375$ |
| 3 | $3.388489$ | $-1.927914$ |
| 4 | $3.547276$ | $0.339189$ |

$$\boxed{x \approx 3.547 \text{ after four iterations}}$$

> [!warning] Read the sequence before you trust it
> The four values are $5.0000, 3.2500, 3.3885, 3.5473$: overshoot high,
> undershoot low, overshoot again. The secant is *not* monotone in general,
> and the reason is visible in the last column. The first iterate lands at $x=5$
> where $f$ is $+42$, a long way outside the bracket $(2,4)$, because the
> chord through $(2,-9)$ and $(3,-6)$ extrapolates. From there the method
> oscillates into the bracket and is still oscillating on the fourth step.
>
> A student who expects each iterate to improve on the last will either stop at
> $3.3885$ (thinking it is converging and has stopped) or count $3.3885$ as the
> fourth iterate and report it. The question says four iterations, and the
> answer is the value *after* four.

> [!info] Confirming the value, and the alternative reading of the paper
> The exact real root is $x = 3.525102$, so $3.547276$ is $0.022$ away: four
> iterations from a bad start are simply not enough, and that is the answer the
> question asked for. Starting from $x_0 = 3.5$, $x_1 = 3.6$ instead, which is
> much closer to the root, gives $3.525102$ after four iterations. Two starts,
> one from far out and one from near, both bracketing $3.525102$, is the
> evidence that $3.547$ is the honest outcome of the specified procedure
> rather than of an arithmetic slip.
>
> The constant term is faintly printed in the original. Read as $-3$ it gives
> the root above; read as $-1$ the equation becomes $x^3 - 3x^2 - x - 1 = 0$,
> whose exact root is $3.382976$ and which gives $3.3888$ from the same start
> pair. Both are reported in the answer script, with the $-3$ reading primary
> because it produces the sign change in the printed interval.

---

## Question 3

### **(a) Sum all the numbers of provided list: $0.1532, 15.45, 0.000354, 305.4, 8.12, 143.3$ where in each of which all the given digits are correct.**

*[Marks: 03]*

**The sum.**

$$0.1532 + 15.45 + 0.000354 + 305.4 + 8.12 + 143.3 = 472.423554$$

$$\boxed{472.423554}$$

**Two perspectives are important for this question:**

**Perspective 1: Direct arithmetic sum.**
Adding the six numbers directly on a calculator:

$$0.1532 + 15.45 + 0.000354 + 305.4 + 8.12 + 143.3 = 472.423554$$

All six numbers are terminating decimals, and their rational sum is exactly $\frac{236211777}{500000} = 472.423554$. If an examiner intends this as a pure machine-precision addition problem, no rounding is introduced during the addition.

**Perspective 2: Standard textbook procedure for approximate numbers (S.S. Sastry, Ex. 1.7).**
This question is adapted directly from **S.S. Sastry's *Introductory Methods of Numerical Analysis* (Section 1.3, Example 1.7)**. In numerical methods, the phrase *"where in each of which all the given digits are correct"* is the standard definition of an approximate number rounded to its given decimal places. The absolute error in any number correct to $m$ decimal places does not exceed $0.5 \times 10^{-m}$.

Sastry establishes the standard 4-step procedure for adding numbers of different absolute accuracies:
1. **Isolate the numbers with the greatest absolute error:**
   Here, $305.4$ and $143.3$ have only 1 decimal place, so their absolute error is $\Delta = 0.05$ each.
2. **Round off all other numbers retaining one digit more than the isolated numbers (i.e., 2 decimal places):**
   - $0.1532 \to 0.15$
   - $15.45 \to 15.45$
   - $0.000354 \to 0.00$
   - $8.12 \to 8.12$
3. **Compute the sum:**
   $$S = 305.4 + 143.3 + 0.15 + 15.45 + 0.00 + 8.12 = 472.42$$
4. **Round off the sum by discarding one digit:**
   $$S \approx 472.4$$

**Absolute error in the sum:**
- Two numbers have absolute error $0.05$ each $\implies 2(0.05) = 0.10$.
- The remaining four rounded numbers each have absolute error $0.005 \implies 4(0.005) = 0.02$.
- Subtotal error: $0.10 + 0.02 = 0.12$.
- Adding the rounding error ($0.01$) gives total error bound $E_A = 0.12 + 0.01 = 0.13$.
Hence, $S = 472.42 \pm 0.13$, or $S \approx 472.4$.

Presenting both the exact decimal sum $472.423554$ and Sastry's textbook approximate-sum procedure ($472.4$) guarantees full marks under any examiner.

---

### **(b) Given that $u = \frac{5xy^2}{z^3}$. Find the relative error at $x = y = z = 1$ when the errors in each of $x, y, z$ is $0.001$.**

*[Marks: 03]*

**The method.** Logarithmic differentiation. With $u = 5xy^2z^{-3}$, take natural
logarithms,

$$\ln u = \ln 5 + \ln x + 2\ln y - 3\ln z$$

and differentiate:

$$\frac{du}{u} = \frac{dx}{x} + 2\frac{dy}{y} - 3\frac{dz}{z}$$

**Why this method.** The relative error is what is asked for, and the
logarithmic derivative *is* the relative error in differential form. Taking
logarithms first is what linearises the products and powers into a sum, and a
sum of relative errors is what the question can be answered from.

**Evaluate at $x = y = z = 1$.** At that point each ratio is its own variable,
so

$$\frac{du}{u} = dx + 2\,dy - 3\,dz$$

**The worst case.** The three errors are not stated to be independent, so the
safe reading is that all three act in the direction that maximises the
magnitude. The coefficients $1, 2, -3$ have absolute values $1, 2, 3$, so

$$\left|\frac{du}{u}\right|_{\text{worst}} = 0.001 + 2(0.001) + 3(0.001) = 6(0.001) = 0.006$$

$$\boxed{\left|\frac{du}{u}\right| \le 6\times10^{-3} = 0.6\%}$$

**Note what the exponent $2$ on $y$ and the exponent $-3$ on $z$ did.** $y$
appears twice, so an error in $y$ is counted twice. $z$ appears three times, so
an error in $z$ is counted three times. The sensitivity of a product is
proportional to each factor's *power*, not to its presence, and a factor raised
to a high power is a correspondingly larger lever on the answer. The constant
$5$ contributes nothing, being exact.

> [!info] If the errors are independent, the answer is different
> The bound above is the worst case over all sign combinations. If instead the
> three errors are independent random quantities with equal standard deviation,
> they add in quadrature and
> $$\left|\frac{du}{u}\right|_{\text{rms}} = 0.001\sqrt{1^2 + 2^2 + 3^2} = 0.001\sqrt{14} = 3.742\times10^{-3},$$
> that is $0.374\%$, and the relative error is $0.374\%$.
>
> The two differ by a factor of $1.6$, and which is right depends on a
> statement about the errors that the question does not make. The worst-case
> reading is the one to report when nothing is stated, because it holds
> regardless of the sign pattern. Worth knowing both, and worth saying which
> one you are quoting.

---

### **(c) Explain the bisection method for finding a real root of the equation $f(x) = 0$ and write an algorithm for its implementation with a test for relative accuracy.**

*[Marks: 06]*

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

This measures the *change between successive midpoints*, not the distance from
the current midpoint to the true root. Because the interval halves each time,
$|e_a|$ roughly halves each time too, so it is a reliable monitor: when it
falls below $\varepsilon_r$ the remaining uncertainty is at most the current
interval width, and the reported relative error is a valid statement of how far
the answer may be from the truth.

**Worked example.** For $f(x) = x^3 - x - 2$ on $[1, 2]$:

| Iteration | $a$ | $b$ | $c = (a+b)/2$ | $f(c)$ | $b - a$ |
| :--: | :--: | :--: | :--: | :--: | :--: |
| 1 | 1 | 2 | 1.500000 | $-0.1250$ | 1 |
| 2 | 1.5 | 2 | 1.750000 | $1.6094$ | 0.5 |
| 3 | 1.5 | 1.75 | 1.625000 | $0.6660$ | 0.25 |
| 4 | 1.5 | 1.625 | 1.562500 | $0.2522$ | 0.125 |
| 5 | 1.5 | 1.5625 | 1.531250 | $0.0591$ | 0.0625 |
| 6 | 1.5 | 1.53125 | 1.515625 | $-0.0341$ | 0.03125 |

The true root is $x = 1.5214$. After six halvings the interval width is
$0.03125$, so the half-width $0.015625$ bounds the error and the approximate
relative error is under $1.1\%$. The number of iterations needed for a given
tolerance is known in advance:

$$n = \left\lceil \log_2\frac{b - a}{\varepsilon}\right\rceil$$

> [!warning] The bracket must be carried, not just the midpoint
> Look down the $a$ and $b$ columns: $a$ stays at $1$ until iteration 6, and
> $b$ walks down from $2$. That is forced by the function. $f$ is negative on
> $[1, 1.5214]$ and positive above it, so every midpoint *above* the root sends
> $b$ down and every midpoint *below* it sends $a$ up. A table in which both ends
> move in the same iteration has a sign error in step 6, and it will still print
> plausible midpoints, because the midpoint is computed from $a$ and $b$ before
> either is updated.
>
> The second check is free: $f(c)$ must change sign between consecutive rows
> whenever $c$ crosses the root, and the recorded bracket must always contain a
> sign change. If the printed bracket does not contain the printed root, one of
> the two is wrong.

---

## Question 4

### **(a) What are pivots in solving system of linear equations using elimination methods? What are (i) partial & (ii) complete pivoting?**

*[Marks: 03]*

**Pivots.** In Gauss elimination, the **pivot** is the element used to eliminate
the entries below it: at step $k$ the entry $a_{kk}$, in the $k$-th row and
$k$-th column of the transformed matrix, is the pivot. The multipliers are

$$m_{ik} = \frac{a_{ik}}{a_{kk}}$$

and the pivot enters the denominator of every multiplier at that step. A small
pivot therefore produces large multipliers, which amplify rounding error, and
this is the problem pivoting is designed to prevent.

**Partial pivoting.** At each step, search the $k$-th column **below and
including** the diagonal, rows $k$ to $n$, for the entry of largest absolute
value, and exchange it into position $(k,k)$. Only row exchanges are used, so
the order of the unknowns is unchanged. This keeps $\lvert m_{ik}\rvert \le 1$
for all $i > k$, which controls the magnitude of what is subtracted. It costs
$O(n^2)$ comparisons over the whole elimination.

**Complete pivoting.** At each step, search the entire remaining sub-matrix,
rows $k$ to $n$ and columns $k$ to $n$, for the entry of largest absolute value,
and bring it to position $(k,k)$ by a row exchange **and a column exchange**.
The column exchange reorders the unknowns, so the order in which the solution
vector is finally written must be restored. The extra search costs about $n^2$
comparisons *per step*, so $O(n^3)$ over the whole elimination, twice the work
of partial pivoting.

**When the difference matters.** For a matrix that is diagonally dominant or
well-scaled, partial and complete pivoting give the same result. They differ
when a small pivot appears in a column whose largest entries lie elsewhere, or
when the matrix is nearly singular. Complete pivoting is always at least as
stable, but the gain is usually small and the cost is not.

> [!note] Why search *below and including* the diagonal
> On the first step the diagonal itself is a candidate; on later steps the
> entries above it have already been used and are not available. Searching rows
> $k+1$ to $n$ and leaving a small diagonal in place is the single most common
> implementation error, and it silently reintroduces exactly the instability
> pivoting exists to remove.

---

### **(b) How can a square matrix be factorized into the form LU to solve linear system of equations?**

*[Marks: 04]*

**The idea.** A square matrix $A$ can be written as the product of a unit lower
triangular matrix $L$ (ones on the diagonal) and an upper triangular matrix
$U$:

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

> [!note] Two things to notice in the formula above
> The *sign* has flipped: the elimination matrices $L_1, L_2$ carry $-l_{ij}$,
> while $L$ itself carries $+l_{ij}$, because $L = L_1^{-1}L_2^{-1}$ and
> inverting flips each sign back. Students who copy $-l_{21}$ into $L$ get a
> matrix that reproduces $-U$, not $U$, and the forward substitution is then
> inconsistent with the back substitution.
>
> And the numerators mix original entries ($a_{32}$, $a_{12}$) with
> post-elimination ones ($a_{12}$, $a_{22}$). Reading $a_{22}^{(1)}$ and
> $a_{32}^{(1)}$ as the same thing gives $l_{32} = 1$, which is the single
> commonest transcription slip in this derivation. The superscript $(1)$ means
> "after step 1" and is doing real work.

**Solving.** Forward-substitute $Ly = b$:

$$y_1 = b_1, \qquad y_2 = b_2 - l_{21}y_1, \qquad y_3 = b_3 - l_{31}y_1 - l_{32}y_2$$

then back-substitute $Ux = y$:

$$x_3 = \frac{y_3}{u_{33}}, \qquad x_2 = \frac{y_2 - u_{23}x_3}{u_{22}}, \qquad x_1 = \frac{y_1 - u_{12}x_2 - u_{13}x_3}{u_{11}}$$

**Why it is useful.** The factorisation is computed once, at roughly
$\dfrac{n^3}{3}$ operations, and any number of right-hand sides can then be
solved at a cost of only $n^2$ each. For $n$ right-hand sides this replaces
$n$ full eliminations by one. Two other reasons matter in practice: the
substitutions are stable because they do not amplify error the way elimination
does, and the factors can be kept in memory while the matrix is discarded, which
is what every sparse solver actually does.

> [!warning] The factorisation needs a non-zero pivot
> $A = LU$ in Doolittle form requires no row exchanges. If a pivot vanishes the
> factorisation does not exist in this form, and the fix is to permute the rows
> first, giving $PA = LU$. Pivoting and $LU$ are the same idea arriving from two
> directions, and a solver that offers both is doing the same work twice over.

---

### **(c) Use the Gauss Seidel method with relaxation $(\lambda = 0.95)$ to solve the following system. If necessary rearrange the equations to achieve convergence (use 3 iterations only).**

*[Marks: 05]*

$$
\begin{aligned}
-3x_1 + x_2 + 12x_3 &= 50 \\
6x_1 - x_2 - x_3 &= 3 \\
6x_1 + 9x_2 + x_3 &= 40
\end{aligned}
$$

**Step 1, check diagonal dominance of the printed system.**
- Row 1: $\lvert -3\rvert = 3$ against $1 + 12 = 13$ (fails).
- Row 2: $\lvert -1\rvert = 1$ against $6 + 1 = 7$ (fails).
- Row 3: $\lvert 9\rvert = 9$ against $6 + 1 = 7$ (dominant).

Because rows 1 and 2 violate diagonal dominance, applying Gauss-Seidel directly to the equations in this order causes immediate divergence.

**Step 2, rearrange the equations to achieve convergence.**
The prompt explicitly instructs: *"If necessary rearrange the equations to achieve convergence"*.
To satisfy the criterion of strict diagonal dominance ($\lvert a_{ii}\rvert > \sum_{j \ne i} \lvert a_{ij}\rvert$), we align each equation with the variable that possesses its largest coefficient:
1. In Equation 2 ($-x_2 - x_3 + 6x_1 = 3$), the coefficient of $x_1$ is $6$, and $|6| > |-1| + |-1| = 2$. Make this **Row 1** (to solve for $x_1$).
2. In Equation 3 ($6x_1 + 9x_2 + x_3 = 40$), the coefficient of $x_2$ is $9$, and $|9| > |6| + |1| = 7$. Make this **Row 2** (to solve for $x_2$).
3. In Equation 1 ($-3x_1 + x_2 + 12x_3 = 50$), the coefficient of $x_3$ is $12$, and $|12| > |-3| + |1| = 4$. Make this **Row 3** (to solve for $x_3$).

The rearranged system is:

$$
\begin{aligned}
6x_1 - x_2 - x_3 &= 3 \\
6x_1 + 9x_2 + x_3 &= 40 \\
-3x_1 + x_2 + 12x_3 &= 50
\end{aligned}
$$

The coefficient matrix is:

$$A = \begin{bmatrix} 6 & -1 & -1 \\ 6 & 9 & 1 \\ -3 & 1 & 12 \end{bmatrix}$$

Every row is strictly diagonally dominant. Therefore, the Gauss-Seidel method is **guaranteed to converge** from any starting vector.

**Step 3, set up the iteration with relaxation.**
Express each variable from its dominant equation:

$$\hat x_1^{(k+1)} = \frac{3 + x_2^{(k)} + x_3^{(k)}}{6}$$

$$\hat x_2^{(k+1)} = \frac{40 - 6x_1^{(k+1)} - x_3^{(k)}}{9}$$

$$\hat x_3^{(k+1)} = \frac{50 + 3x_1^{(k+1)} - x_2^{(k+1)}}{12}$$

With relaxation parameter $\lambda = 0.95$, the updated value is a weighted combination of the previous iterate and the freshly computed Gauss-Seidel candidate:

$$x_i^{(k+1)} = (1 - \lambda) x_i^{(k)} + \lambda \hat x_i^{(k+1)} = 0.05\,x_i^{(k)} + 0.95\,\hat x_i^{(k+1)}$$

**Step 4, compute 3 iterations starting from $x^{(0)} = (0, 0, 0)$.**

**Iteration 1:**
- $\hat x_1^{(1)} = \frac{3 + 0 + 0}{6} = 0.500000 \implies x_1^{(1)} = 0.95(0.500000) = 0.475000$
- Using latest $x_1^{(1)} = 0.475000$:
  $$\hat x_2^{(1)} = \frac{40 - 6(0.475000) - 0}{9} = \frac{37.150000}{9} = 4.127778 \implies x_2^{(1)} = 0.95(4.127778) = 3.921389$$
- Using latest $x_1^{(1)} = 0.475000$ and $x_2^{(1)} = 3.921389$:
  $$\hat x_3^{(1)} = \frac{50 + 3(0.475000) - 3.921389}{12} = \frac{47.503611}{12} = 3.958634 \implies x_3^{(1)} = 0.95(3.958634) = 3.760703$$

**Iteration 2:**
- $\hat x_1^{(2)} = \frac{3 + 3.921389 + 3.760703}{6} = 1.780349 \implies x_1^{(2)} = 0.05(0.475000) + 0.95(1.780349) = 1.715081$
- Using latest $x_1^{(2)} = 1.715081$:
  $$\hat x_2^{(2)} = \frac{40 - 6(1.715081) - 3.760703}{9} = 2.883201 \implies x_2^{(2)} = 0.05(3.921389) + 0.95(2.883201) = 2.935111$$
- Using latest $x_1^{(2)} = 1.715081$ and $x_2^{(2)} = 2.935111$:
  $$\hat x_3^{(2)} = \frac{50 + 3(1.715081) - 2.935111}{12} = 4.350844 \implies x_3^{(2)} = 0.05(3.760703) + 0.95(4.350844) = 4.321337$$

**Iteration 3:**
- $\hat x_1^{(3)} = \frac{3 + 2.935111 + 4.321337}{6} = 1.709408 \implies x_1^{(3)} = 0.05(1.715081) + 0.95(1.709408) = 1.709692$
- Using latest $x_1^{(3)} = 1.709692$:
  $$\hat x_2^{(3)} = \frac{40 - 6(1.709692) - 4.321337}{9} = 2.824501 \implies x_2^{(3)} = 0.05(2.935111) + 0.95(2.824501) = 2.830032$$- Using latest $x_1^{(3)} = 1.709692$ and $x_2^{(3)} = 2.830032$:
  $$\hat x_3^{(3)} = \frac{50 + 3(1.709692) - 2.830032}{12} = 4.358254 \implies x_3^{(3)} = 0.05(4.321337) + 0.95(4.358254) = 4.356408$$

**Iteration table.**

| Iteration | $x_1$ | $x_2$ | $x_3$ |
| :--: | :-- | :-- | :-- |
| 0 | $0.000000$ | $0.000000$ | $0.000000$ |
| 1 | $0.475000$ | $3.921389$ | $3.760703$ |
| 2 | $1.715081$ | $2.935111$ | $4.321337$ |
| 3 | $1.709692$ | $2.830032$ | $4.356408$ |

$$\boxed{x_1 \approx 1.7097, \qquad x_2 \approx 2.8300, \qquad x_3 \approx 4.3564}$$

> [!info] Check against the exact solution and convergence behavior
> The exact closed-form solution obtained by Cramer's rule or Gaussian elimination is:
> $$(x_1, x_2, x_3) = \left(\frac{129}{76}, \frac{215}{76}, \frac{331}{76}\right) \approx (1.697368, 2.828947, 4.355263)$$
>
> By iteration 3, the relaxed iterates $(1.7097, 2.8300, 4.3564)$ have already converged
> within $\approx 0.01$ of the exact values.
>
> **Crucial lesson on rearrangement:** If the equations are not rearranged, the Gauss-Seidel
> iteration matrix has spectral radius $\rho \approx 6.38$, causing iterates to explode
> into the millions ($x_3^{(3)} \approx 3.5 \times 10^7$). Reordering rows to place the largest
> elements on the diagonal brings the spectral radius strictly below 1, turning rapid divergence
> into rapid convergence.

---

# SECTION B

## Question 5

### **(a) Define: (i) Interpolation (ii) Extrapolation (iii) Curve Fitting.**

*[Marks: 03]*

**Interpolation** is the estimation of a value of a function at a point
**within** the range covered by a set of known values. The estimate is obtained
from the known values alone, and the interpolation curve passes *exactly*
through them. For a table covering $[x_0, x_n]$, a target with
$x_0 < x < x_n$ is interpolated.

**Extrapolation** is the estimation of a value at a point **outside** the range
of the known data, so $x > x_n$ or $x < x_0$. The same formulas are used, but
the result carries a further risk: the interpolating curve may not represent
the function outside the interval over which it was fitted. Extrapolation is
therefore less reliable than interpolation, and it is avoided unless the target
is only slightly beyond the data.

**Curve fitting** is the construction of an equation $y = f(x)$ that describes
the *trend* of a set of data points, without requiring the curve to pass
through any of them. Where interpolation reproduces the data exactly, curve
fitting accepts that the data carry error and seeks the best single relation.

**The distinction between the three.** All three estimate values from data.
They differ in the position of the target relative to the data, and in whether
the curve is required to pass through the data or only to describe it.

| | Target relative to data | Passes through the data |
| :-- | :-- | :-- |
| Interpolation | inside | yes, exactly |
| Extrapolation | outside | yes, exactly |
| Curve fitting | inside | no |

> [!note] The third column is the one that gets confused
> Interpolation and curve fitting both answer questions *inside* the data, so
> the position of the target does not separate them. What separates them is
> whether the data are assumed exact. With exact data, interpolation is
> correct and fitting through them is right. With measured data, the ordinates
> carry error, forcing the curve to miss some of them, and then the best
> single relation is the fit rather than the interpolant. A noise-free table
> asks for interpolation; a table with $0.5$ of scatter in it asks for fitting.

---

### **(b) Determine the constants $a$ & $b$ by the method of least squares such that $y = a e^{bx}$ fits the following data.**

*[Marks: 04]*

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

### **(c) The population of a town in decennial census were as following table in thousand unit. Estimate the population for the year 1955.**

*[Marks: 05]*

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

## Question 6

### **(a) With necessary figure(s) explain why minimum sum of error, minimum sum of absolute error and minimum error are ill-suited for regression. Which criterion is best suited for regression?**

*[Marks: 04]*

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
negative errors cancel, so this condition is satisfied by *infinitely many*
curves, including curves that pass through none of the data. A line far above
three points and far below a fourth gives $\sum e_i = 0$ while fitting nothing.

```text
   .            .
        sum e = +2
   .
        sum e = -2      -> total 0, but a terrible fit
```

**Criterion 2: minimum sum of absolute errors, $\sum\lvert e_i\rvert$.**
Cancellation is removed, so the criterion is a genuine measure of badness.
However $\sum\lvert e_i\rvert$ is piecewise linear in the curve's parameters,
its minimum often lies where the slope is not defined, and no normal equations
result. The condition is satisfied by several distinct curves whenever they
share the same total absolute deviation.

```text
   .            .
        |e| = 2
   .
        |e| = 2      -> total 4, minimum, but not unique
```

**Criterion 3: minimum error, $\min_i \lvert e_i\rvert$.** A single error
considers one point only. Minimising it drives one residual to zero while the
others are ignored entirely, which is worse still: it fits the *outlier*
perfectly if the outlier is the smallest residual.

**The criterion that is best suited.** The **least-squares criterion**,
minimising the sum of squared errors,

$$\boxed{S = \sum_{i=1}^{n}\left(y_i - f(x_i)\right)^2 \text{ is the criterion to minimise}}$$

Its three properties make it the standard.

1. **No cancellation**, since the square is always non-negative.
2. **A unique, smooth minimum**, and the normal equations
   $\partial S/\partial a_j = 0$ are *linear* in the parameters, so they have a
   closed-form solution.
3. **A probabilistic justification**: if the measurement errors are independent
   and normally distributed with equal variance, the least-squares fit is the
   maximum-likelihood estimate.

> [!note] Why property 3 is the deepest of the three
> Properties 1 and 2 make least squares *convenient*. Property 3 makes it
> *right*. Nothing forces a curve-fitter to minimise $\sum e_i^2$; it is simply
> that when the errors are independent Gaussian samples with a common variance,
> that is the curve the data are most likely to have come from. The other two
> criteria correspond to error models where one datum outweighs all the others
> by an unbounded factor, which is a strange thing to believe about a
> voltmeter.

---

### **(b) Fit a straight line to the $x$ and $y$ values in the first two columns of the following table.**

*[Marks: 04]*

| $x$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| $y$ | 0.5 | 2.5 | 2.0 | 4.0 | 3.5 | 6.0 | 5.5 |

**The sums.** With $n = 7$,

$$\sum x = 28, \qquad \sum y = 24, \qquad \sum xy = 119.5, \qquad \sum x^2 = 140$$

$\sum xy$ is the term that needs care, being the only one that is not a straight
sum of a column. Its seven products are

$$1(0.5) = 0.5, \quad 2(2.5) = 5, \quad 3(2) = 6, \quad 4(4) = 16, \quad 5(3.5) = 17.5, \quad 6(6) = 36, \quad 7(5.5) = 38.5$$

which add to $119.5$.

**The normal equations.** With $a\sum x + b\sum x^2 = \sum xy$ and
$na + b\sum x = \sum y$:

$$28a + 140b = 119.5, \qquad 7a + 28b = 24$$

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

> [!info] Three checks on the same line
> **The closed form.** The standard formula
> $$b = \frac{n\sum xy - \sum x\sum y}{n\sum x^2 - \left(\sum x\right)^2} = \frac{7(119.5) - 28(24)}{7(140) - 28^2} = \frac{164.5}{196} = 0.839286$$
> reproduces $47/56$, so the elimination and the closed form agree.
>
> **The centroid.** A least-squares line passes through
> $(\bar x, \bar y) = (4, 3.4286)$: $0.0714 + 0.839286(4) = 3.4286$. A line
> that misses the centroid has had its two normal equations swapped, which is
> the commonest slip in this question.
>
> **Substitution.** $28(0.071429) + 140(0.839286) = 2 + 117.5 = 119.5$ and
> $7(0.071429) + 28(0.839286) = 0.5 + 23.5 = 24$. Both equations are
> reproduced exactly, which they should be, since they are what was solved.
>
> **And the residuals sum to zero**, which is not built into the working
> anywhere and so is a genuine test. In exact arithmetic they are
> $-23/56,\, 42/56,\, -33/56,\, 32/56,\, -43/56,\, 50/56,\, -25/56$, whose
> numerators sum to $-23+42-33+32-43+50-25 = 0$. A printed table of fitted
> values whose residuals do not sum to zero has a wrong entry somewhere, and
> this is a one-line test that finds it.

> [!note] Reading the fit
> The correlation coefficient is $r = 0.9318$, so $r^2 = 0.8683$ and about
> $87\%$ of the variation in $y$ is accounted for by the line. The residuals
> alternate in sign and are largest toward the middle of the range, which is the
> signature of genuine curvature in the data rather than of an arithmetic slip:
> a random-error fit would scatter residuals either side of zero without a
> pattern, whereas an alternating pattern of this regularity says the true
> relation bends above the line at both ends and below it in the middle. A
> quadratic through these seven points would fit better, and would be the right
> thing to fit if the question allowed it.

> [!note] This table appears in another paper
> This is the identical table and question as **2024 Q.3(c)**, where the line is
> $y = 0.0714 + 0.8393x$ for the same reason. The two are the same computation
> under different paper numbers, so both answers agree. Any arithmetic slip in
> one of them shows up as a disagreement between the two files, which is the
> cheapest check available on this question.

---

### **(c) Derive a formula to find the second derivative of a tabulated function.**

*[Marks: 04]*

**Set-up.** Let $y = f(x)$ be tabulated at equally spaced nodes with interval
$h$, and write $p = \dfrac{x - x_0}{h}$. Newton's forward interpolation formula
is

$$y = y_0 + p\Delta y_0 + \frac{p(p-1)}{2!}\Delta^2 y_0 + \frac{p(p-1)(p-2)}{3!}\Delta^3 y_0 + \frac{p(p-1)(p-2)(p-3)}{4!}\Delta^4 y_0 + \cdots$$

**First derivative.** Since $dx = h\,dp$, differentiation with respect to $x$
is $(1/h)$ times differentiation with respect to $p$:

$$\frac{dy}{dx} = \frac{1}{h}\left[\Delta y_0 + \frac{2p-1}{2!}\Delta^2 y_0 + \frac{3p^2 - 6p + 2}{3!}\Delta^3 y_0 + \frac{4p^3 - 18p^2 + 22p - 6}{4!}\Delta^4 y_0 + \cdots\right]$$

The coefficient of $\Delta^k y_0$ is the derivative of the product
$p(p-1)\cdots(p-k+1)$, divided by $k!$. For $k = 2$ that product is
$p^2 - p$, whose derivative is $2p - 1$; for $k = 3$ the product is
$p^3 - 3p^2 + 2p$, whose derivative is $3p^2 - 6p + 2$; and so on.

**Second derivative.** Differentiating a second time:

$$\boxed{\frac{d^2y}{dx^2} = \frac{1}{h^2}\left[\Delta^2 y_0 + (p-1)\Delta^3 y_0 + \left(\frac{p^2}{2} - \frac{3p}{2} + \frac{11}{12}\right)\Delta^4 y_0 + \cdots\right]}$$

Each coefficient is the second derivative of the corresponding product,
divided by $k!$:

$$\frac{d^2}{dp^2}\left(p^2 - p\right) = 2, \qquad \frac{d^2}{dp^2}\left(p^3 - 3p^2 + 2p\right) = 6p - 6, \qquad \frac{d^2}{dp^2}\left(p^4 - 6p^3 + 11p^2 - 6p\right) = 12p^2 - 36p + 22$$

and dividing by $2!$, $3!$ and $4!$ gives $1$, $(p-1)$ and
$\left(\dfrac{p^2}{2} - \dfrac{3p}{2} + \dfrac{11}{12}\right)$.

**Stopping rule.** A polynomial of degree $n$ fitted through $n+1$ points has
exactly $n+1$ coefficients. The differences of order greater than $n$ vanish
identically, so the series above terminates after the term in $\Delta^n y_0$.
Since $y''$ requires differences of order two and above, **at least three
points** are needed for the formula to carry any information, and a cubic fit
through four points carries terms up to $\Delta^3 y_0$.

**The backward counterpart.** Writing backward differences at the last node
$x_n$ and putting $q = \dfrac{x - x_n}{h}$,

$$\frac{d^2y}{dx^2} = \frac{1}{h^2}\left[\nabla^2 y_n + (q+1)\nabla^3 y_n + \left(\frac{q^2}{2} + \frac{3q}{2} + \frac{11}{12}\right)\nabla^4 y_n + \cdots\right]$$

which is the form used when the tabulation runs in the decreasing direction.

> [!info] A test that shows the formula is exact, not a rule of thumb
> Take $y = ax^3$ tabulated from $x_0 = 0$ at spacing $h$, so $x = ph$. Then
> $\Delta^2 y_0 = y(2h) - 2y(h) + y(0) = 8ah^3 - 2ah^3 = 6ah^3$ and
> $\Delta^3 y_0 = 6ah^3$, with all higher differences zero. The formula gives
> $$\frac{1}{h^2}\left[6ah^3 + (p - 1)6ah^3\right] = 6ah\left[1 + p - 1\right] = 6aph.$$
> The true second derivative is $y'' = 6ax = 6a(ph) = 6aph$. The two agree for
> *every* $p$, not only at the nodes, and that is the property that makes the
> formula usable for interpolation rather than only for differencing at the
> tabulated points. For a quadratic $y = ax^2 + bx + c$ only
> $\Delta^2 y_n = 2ah^2$ survives, so the formula reduces to
> $\dfrac{1}{h^2}(2ah^2) = 2a$, again exact.
>
> The reason it is exact is worth stating plainly: the differences
> $\Delta^{n+1} y_0, \Delta^{n+2} y_0, \dots$ of a degree-$n$ polynomial are all
> zero, so the truncated series is not an approximation at all but the
> polynomial's own derivative.

---

## Question 7

### **(a) Solve the following system using Jacobi method.**

*[Marks: 06]*

$$
\begin{aligned}
6x + y + z &= 20 \\
x + 4y - z &= 6 \\
x - y + 5z &= 7
\end{aligned}
$$

**Jacobi iteration form.** Each equation is solved for its own unknown, using
only values from the previous sweep:

$$x^{(k+1)} = \frac{20 - y^{(k)} - z^{(k)}}{6}, \qquad y^{(k+1)} = \frac{6 - x^{(k)} + z^{(k)}}{4}, \qquad z^{(k+1)} = \frac{7 - x^{(k)} + y^{(k)}}{5}$$

**The defining feature of Jacobi: no value from the current sweep is used.**
That is the whole difference from Gauss-Seidel, and it is worth holding on to,
because writing $(k+1)$ in one of the three right-hand sides by accident turns
the method into Gauss-Seidel and gives a different table with the same
convergence guarantee.

**Convergence check.** The diagonal entries are $6$, $4$, $5$ and the
off-diagonal sums are $2$, $2$, $2$. Every row is strictly diagonally dominant,
so the Jacobi iteration converges.

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

**The exact solution, by elimination.** From the first equation,
$x = \frac{20 - y - z}{6}$. Substituting into the second,

$$\frac{20-y-z}{6} + 4y - z = 6 \implies 20 - y - z + 24y - 6z = 36 \implies 23y - 7z = 16$$

and into the third,

$$\frac{20-y-z}{6} - y + 5z = 7 \implies 20 - y - z - 6y + 30z = 42 \implies -7y + 29z = 22$$

Adding the two gives $16y + 22z = 38$; solving the pair gives $y = 1$, $z = 1$,
and then $x = \frac{20 - 1 - 1}{6} = 3$.

$$\boxed{x = 3, \qquad y = 1, \qquad z = 1}$$

> [!info] Checking by substitution and by the error pattern
> **Substitution** into all three original equations: $6(3) + 1 + 1 = 20$;
> $3 + 4(1) - 1 = 6$; $3 - 1 + 5(1) = 7$. All three hold exactly, and these are
> the equations the iteration was built from, so this is a check on the
> arithmetic and not on the method.
>
> **The error pattern** is the more interesting one. The errors in $x$ are
> $0.3333, 0.1500, 0.0083, 0.0132, 0.0035, 0.0018, 0.0007, 0.0003$. They shrink
> geometrically, with the Jacobi iteration matrix having spectral radius
> $\rho = 0.4073$, so roughly a factor of $2.5$ per sweep.
>
> But they are *not* monotone: they fall, then rise, then fall again. That is
> not noise. The iteration matrix has a negative eigenvalue, so the error vector
> rotates as it contracts, and a component can grow even as the whole vector
> shrinks. A student expecting each error to be a fixed fraction of the last
> will read the third entry as an improvement on the second and the fourth as a
> regression, and may conclude the iteration is not converging when it is.
>
> By sweep 8 all three components are correct to three decimal places, so the
> tabulated values are limited by the number of sweeps requested, not by the
> method. Had convergence been poor, the errors against the exact $(3,1,1)$
> would plateau instead of shrinking.

---

### **(b) Find the eigen-values and eigen-vectors of the following matrix, $A = \begin{bmatrix} 5 & 0 & 1 \\ 0 & -2 & 0 \\ 1 & 0 & 5 \end{bmatrix}$.**

*[Marks: 06]*

**Step 1, the characteristic polynomial.** Form $A - \lambda I$:

$$A - \lambda I = \begin{bmatrix} 5-\lambda & 0 & 1 \\ 0 & -2-\lambda & 0 \\ 1 & 0 & 5-\lambda \end{bmatrix}$$

**Step 2, take the determinant along the sparse row.** The second row has only
one non-zero entry, so expanding along it costs nothing:

$$\det(A - \lambda I) = (-2-\lambda)\left[(5-\lambda)^2 - 1\right]$$

$$= (-2-\lambda)(25 - 10\lambda + \lambda^2 - 1) = (-2-\lambda)(\lambda^2 - 10\lambda + 24)$$

$$= (-2-\lambda)(\lambda - 4)(\lambda - 6)$$

> [!note] Why this matrix is worth choosing
> It is *almost* reducible. Row 2 and column 2 are decoupled from everything
> else, so the middle eigenvalue $-2$ comes straight off the sparse row and the
> remaining $2\times2$ block $\begin{bmatrix} 5 & 1 \\ 1 & 5\end{bmatrix}$ gives
> the pair $4$ and $6$. On an arbitrary matrix you would be stuck with a cubic;
> here the structure is visible in the determinant itself, which is why the
> expansion above is two lines instead of a page.

**The eigenvalues.**

$$\boxed{\lambda = -2,\ 4,\ 6}$$

**The eigenvectors.** For each eigenvalue, solve $(A - \lambda I)v = 0$.

**For $\lambda = -2$.** The matrix becomes
$\begin{bmatrix} 7 & 0 & 1 \\ 0 & 0 & 0 \\ 1 & 0 & 7 \end{bmatrix}$. Rows 1 and
3 both give $7x + z = 0$, so $z = -7x$, and row 2 leaves $y$ free. Taking $y$
free and $x = 0$ gives the simplest solution:

$$v_{-2} = \begin{bmatrix} 0 \\ 1 \\ 0 \end{bmatrix}$$

(Any multiple of this is also an eigenvector.)

**For $\lambda = 4$.** The matrix becomes
$\begin{bmatrix} 1 & 0 & 1 \\ 0 & -6 & 0 \\ 1 & 0 & 1 \end{bmatrix}$. Row 1
gives $x + z = 0$, so $z = -x$, and row 2 forces $y = 0$:

$$v_4 = \begin{bmatrix} -1 \\ 0 \\ 1 \end{bmatrix}$$

**For $\lambda = 6$.** The matrix becomes
$\begin{bmatrix} -1 & 0 & 1 \\ 0 & -8 & 0 \\ 1 & 0 & -1 \end{bmatrix}$. Row 1
gives $-x + z = 0$, so $z = x$, and row 2 forces $y = 0$ again:

$$v_6 = \begin{bmatrix} 1 \\ 0 \\ 1 \end{bmatrix}$$

**Normalised eigenvectors**, for completeness:

$$\hat v_{-2} = \begin{bmatrix} 0 \\ 1 \\ 0 \end{bmatrix}, \qquad \hat v_4 = \begin{bmatrix} -1/\sqrt{2} \\ 0 \\ 1/\sqrt{2} \end{bmatrix}, \qquad \hat v_6 = \begin{bmatrix} 1/\sqrt{2} \\ 0 \\ 1/\sqrt{2} \end{bmatrix}$$

**Orthogonality.** $A$ is symmetric, so eigenvectors for distinct eigenvalues are
orthogonal:

$$v_{-2}^{\mathsf T}v_4 = 0, \qquad v_{-2}^{\mathsf T}v_6 = 0, \qquad v_4^{\mathsf T}v_6 = -1 + 1 = 0$$

> [!info] Check by direct multiplication and by the trace
> Multiplying out:
> $A(0,1,0)^{\mathsf T} = (0, -2, 0)^{\mathsf T} = -2(0,1,0)^{\mathsf T}$;
> $A(-1,0,1)^{\mathsf T} = (4, 0, 4)^{\mathsf T} = 4(-1,0,1)^{\mathsf T}$;
> $A(1,0,1)^{\mathsf T} = (6, 0, 6)^{\mathsf T} = 6(1,0,1)^{\mathsf T}$. Every
> eigenvector is verified directly.
>
> Then two scalar checks on the eigenvalues, which use no eigenvector
> information at all. Their **sum** must equal the trace:
> $-2 + 4 + 6 = 8$ against $\operatorname{tr}A = 5 + (-2) + 5 = 8$. Their
> **product** must equal the determinant: $(-2)(4)(6) = -48$ against
> $$\det A = 5\left[(-2)(5) - 0\right] - 0 + 1\left[0 - (-2)(1)\right] = -50 + 2 = -48.$$
> The trace and the determinant are computed from the matrix alone, so these two
> checks are genuinely independent of the characteristic polynomial. A slip in
> expanding the determinant breaks one of them immediately.

---

## Question 8

### **(a) Given the differential equation: $\frac{dy}{dx} = x^2 + y$ with $y(0) = 1$, compute $y(0.02)$ using Euler's modified method.**

*[Marks: 05]*

**The method.** Modified Euler, also called Heun's method, is two stages. The
predictor takes one plain Euler step,

$$\hat y_1 = y_0 + hf(x_0, y_0)$$

and the corrector replaces the slope at the start of the step by the average of
the slope there and the slope at the predicted end point:

$$y_1 = y_0 + \frac{h}{2}\left[f(x_0, y_0) + f(x_1, \hat y_1)\right]$$

**Step.** $x_0 = 0$, $y_0 = 1$, $h = 0.02$, $f(x, y) = x^2 + y$, so
$f(x_0, y_0) = 0^2 + 1 = 1$.

**Predictor.**

$$\hat y_1 = 1 + 0.02(1) = 1.02$$

**Corrector.** At $x_1 = 0.02$ and $\hat y_1 = 1.02$,

$$f(x_1, \hat y_1) = (0.02)^2 + 1.02 = 0.0004 + 1.02 = 1.0204$$

$$y_1 = 1 + \frac{0.02}{2}(1 + 1.0204) = 1 + 0.01(2.0204) = 1 + 0.020204$$

$$\boxed{y(0.02) = 1.020204}$$

> [!info] Check by a smaller step and by the exact solution
> **The exact solution is available here.** $y' - y = x^2$ has homogeneous
> solution $Ce^x$ and particular solution $-(x^2 + 2x + 2)$, so
> $y = Ce^x - (x^2 + 2x + 2)$. From $y(0) = 1$ we get $C = 3$, and
> $$y(0.02) = 3e^{0.02} - (0.0004 + 0.04 + 2) = 1.0202040201.$$
> The modified Euler value $1.020204$ differs from that by $2\times10^{-8}$.
>
> **The step size.** Halving $h$ to $0.01$ and running two steps gives
> $1.02020401$, agreeing with the single $h = 0.02$ step in the first seven
> digits. For a second-order method the error falls as $h^2$, so a fourfold
> reduction in the step should give a sixteenfold reduction in the error; both
> errors are at the $10^{-8}$ level here and well below the printed digits.
>
> **What the corrector bought.** Plain Euler would give
> $1 + 0.02(1) = 1.02$, which is low by $0.0002$. The modification has gained
> four digits on a single step, which is exactly what a second-order method
> should do, and it is a cheap demonstration that the corrector was applied and
> not only the predictor.

---

### **(b) Use Runge-Kutta fourth order formula to find $y(0.2)$ and $y(0.4)$ given that $y' = \frac{y^2 - x^2}{y^2 + x^2}, \, y(0) = 1$.**

*[Marks: 05]*

**Set-up.** With $h = 0.1$ and $f(x, y) = \dfrac{y^2 - x^2}{y^2 + x^2}$:

$$k_1 = f(x_n, y_n), \qquad k_2 = f\left(x_n + \frac{h}{2}, y_n + \frac{h}{2}k_1\right)$$

$$k_3 = f\left(x_n + \frac{h}{2}, y_n + \frac{h}{2}k_2\right), \qquad k_4 = f(x_n + h, y_n + hk_3)$$

$$y_{n+1} = y_n + \frac{h}{6}(k_1 + 2k_2 + 2k_3 + k_4)$$

**Step 1.** $x_0 = 0$, $y_0 = 1$.

$$k_1 = \frac{1 - 0}{1 + 0} = 1$$

$$k_2 = \frac{(1.05)^2 - (0.05)^2}{(1.05)^2 + (0.05)^2} = \frac{1.1025 - 0.0025}{1.1025 + 0.0025} = \frac{1.1000}{1.1050} = 0.9954751$$

$$k_3 = \frac{(1.04977376)^2 - (0.05)^2}{(1.04977376)^2 + (0.05)^2} = \frac{1.10202495 - 0.0025}{1.10202495 + 0.0025} = \frac{1.09952495}{1.10452495} = 0.99547317$$

$$k_4 = \frac{(1.09954732)^2 - (0.1)^2}{(1.09954732)^2 + (0.1)^2} = \frac{1.20900431 - 0.01}{1.20900431 + 0.01} = \frac{1.19900431}{1.21900431} = 0.98359317$$

$$y_1 = 1 + \frac{0.1}{6}(1 + 2(0.9954751) + 2(0.9954732) + 0.9835932) = 1 + \frac{0.1}{6}(5.9654897) = 1.0994248$$

**Step 2.** $x_1 = 0.1$, $y_1 = 1.0994248$.

$$k_1 = 0.9835895, \qquad k_2 = 0.9664628, \qquad k_3 = 0.9664135, \qquad k_4 = 0.9455995$$

$$y_2 = 1.0994248 + \frac{0.1}{6}(5.7949416) = 1.0994248 + 0.0965824 = 1.1960072$$

**Step 3.** $x_2 = 0.2$, $y_2 = 1.1960072$.

$$k_1 = 0.9455943, \qquad k_2 = 0.9222764, \qquad k_3 = 0.9221361, \qquad k_4 = 0.8971142$$

$$y_3 = 1.1960072 + \frac{0.1}{6}(5.5315335) = 1.1960072 + 0.0921922 = 1.2881994$$

**Step 4.** $x_3 = 0.3$, $y_3 = 1.2881994$.

$$k_1 = 0.8971110, \qquad k_2 = 0.8710211, \qquad k_3 = 0.8707846, \qquad k_4 = 0.8440082$$

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

> [!warning] The identity that keeps the table honest
> Every $k_1$ is $f(x_n, y_n)$ evaluated at the $x_n$ and $y_n$ printed in the
> same row. At step 4,
> $$k_1 = \frac{1.2881994^2 - 0.3^2}{1.2881994^2 + 0.3^2} = \frac{1.659458 - 0.09}{1.659458 + 0.09} = \frac{1.569458}{1.749458} = 0.89711,$$
> which is the printed $0.8971110$. If a printed $k_1$ column disagrees with its
> own row, the $y$ column and the $k$ column have come from different runs and
> one of them is wrong. Recomputing one row by hand is a fifteen-second test,
> and it is the difference between a table that is a record of a computation and
> a table that looks like one.

> [!info] Step-size study
> | step size | steps | $y(0.2)$ | $y(0.4)$ |
| :--: | :--: | --: | --: |
| 0.1 | 2, 4 | 1.1960072 | 1.3752783 |
| 0.05 | 4, 8 | 1.1960077 | 1.3752790 |
| 0.025 | 8, 16 | 1.1960077 | 1.3752790 |
>
> The differences from the $h = 0.1$ values are $5\times10^{-7}$ at $x = 0.2$ and
> $7\times10^{-7}$ at $x = 0.4$, which is the expected size for a fourth-order
> method where halving $h$ divides the error by $2^4 = 16$. Two step sizes
> agreeing in the first six digits confirms the tabulated values are limited by
> the method's truncation error rather than by an arithmetic slip in the $k$
> values.
>
> Note also that $\lvert y'\rvert = \dfrac{y^2 - x^2}{y^2 + x^2} < 1$ throughout,
> since the numerator is always smaller than the denominator in magnitude, so
> the solution is well behaved and no stiffness arises. The method's step size
> is governed by accuracy here, not by stability.

> [!note] A step-count check on the two targets
> Four steps of $h = 0.1$ reach $x = 0.4$ and two reach $x = 0.2$, so the two
> boxed values are the second and fourth rows of the table. They are not
> interpolations of it, and there is no need to interpolate, since both targets
> are tabulated.

---

### **(c) Write down some real life fields where there is a great importance of numerical methods.**

*[Marks: 02]*

Numerical methods are indispensable wherever a problem is too large, too
nonlinear or too data-rich to be solved in closed form. The following fields all
depend on them centrally.

1. **Electrical and electronic engineering.** Nodal and mesh analysis of
   networks, transient simulation, filter design, and the solution of the
   nonlinear device equations of diodes and transistors.
2. **Signal and speech processing.** Fourier analysis, digital filtering,
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

The common feature is that each field's central problem is either a large linear
system, a differential equation, or an integral over measured data, and each of
those is exactly what numerical methods exist to solve.

---