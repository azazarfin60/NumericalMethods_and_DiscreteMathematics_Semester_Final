---
title: "ECE 2213 · 2018 Explanations"
tags:
  - numerical-methods
  - discrete-mathematics
  - previous-year
---

# ECE 2213: 2018 Semester Final · Explained

**RUET · ECE Dept · B.Sc. Engineering 2nd Year Even Semester Examination, 2018**

This file explains the same questions as
[[answers_exam_style/2018_answer|the 2018 answer script]], written to be read
rather than copied. Every step is named, the reason a formula is chosen is
stated, and the traps that catch people are called out.

> [!info] How to use this file
> Read this to understand *why* the answer script does what it does. When you
> are ready to write in the hall, work from
> [[answers_exam_style/2018_answer|the exam-style file]], which is shorter and
> carries no commentary.
>
> **The rule that matters.** Every boxed number here is the same number as the
> one in the answer script, character for character. Gate V5 checks this, and
> gate V12 checks that the marks on every section agree with the answer script
> and with the manifest.

> [!note] What this paper is made of
> The 2018 paper has **no discrete mathematics at all**: all 20 sub-questions are
> numerical methods, and it carries no CLO column. Questions 1 and 2 are error
> analysis and root finding, Questions 3 and 4 interpolation and linear systems,
> Questions 5 and 6 differentiation and integration, and Questions 7 and 8 ODEs
> and the Laplace equation.
>
> Three things in this paper are worth more study than the rest.
> **Q.1(c)** asks for a term count that must hold *for every* $x$ in a range, not
> at one point, and the whole answer turns on where the worst case sits.
> **Q.4(b)** is a mesh circuit with both a voltage source and a current source,
> and the current source removes one unknown rather than adding an equation.
> **Q.8(a)** is a five-point stencil, and reading the four neighbours off the
> diagram wrongly gives you a system that still solves, just to the wrong answer.

---

# SECTION A

## Question 1

### **(a) What are the importances of numerical techniques in engineering? Briefly discuss.**

*[Marks: 04]*

**What a numerical technique is.** A numerical technique obtains the answer of a
mathematical problem as a *finite* sequence of arithmetic operations. Nothing
more clever than that: add, subtract, multiply, divide, compare, repeat. If you
can write the steps down so that someone else gets the same digits, it is a
numerical technique.

**Why it matters, in four points.**

1. **Most engineering problems have no closed form.** The integral
   $\int e^{-x^2}\,dx$, the potential inside a transistor region, and the motion
   of three bodies under mutual gravity all lack an elementary answer, and all
   three come up in practice. Where a closed form does exist it is often so long
   that evaluating it numerically is faster *and* more accurate.
2. **Only arithmetic runs on a machine.** A numerical technique turns a problem
   into additions, multiplications, comparisons and divisions, which is exactly
   what a CPU does. This is what converts an analytic method into something that
   can be implemented.
3. **Measured data arrive as discrete samples.** Anything derived from a data
   sheet, whether a derivative, an integral, a regression line or a filter
   output, is a numerical result. An engineer working from measurements is doing
   numerical analysis whether or not the phrase appears.
4. **Design and optimisation are iterative.** Matching, bias-point selection,
   cut-off placement and root finding are all repeated improvement of an
   estimate. The numerical technique supplies the estimate rule, the stopping
   test and the error estimate.

> [!note] The consequence worth writing down
> A numerical technique is not judged on convergence alone. It is judged on
> three things: its **cost** in operations, its **stability**, and how its
> **error grows with the number of operations**. Everything from Q.2(c) onward
> in this paper is an instance of one of those three.

---

### **(b) What are the algorithmic errors that may occur in numerical calculation?**

*[Marks: 04]*

**Algorithmic error** is the error introduced by the computation itself, as
distinct from error already present in the data you started with.

**1. Truncation error.** Every numerical method replaces an infinite process by
a finite one. An infinite series is cut after $n$ terms, an interval is cut into
$n$ panels, a differential equation is stepped with finite $h$. The discarded
remainder is the truncation error, and it is the error that *shrinks* when the
approximation is refined.

**2. Round-off error.** A machine holds finitely many digits. Every operation
rounds its result to that precision, and the rounding introduced at one step
propagates into every later step. Round-off error *grows* with the number of
operations, which is why a method can become worse when you refine too far.

**3. Propagation of error.** The two above do not simply add. A method is
**unstable** if an error introduced early is amplified downstream, and
**well-conditioned** if it is damped. The amplification factor belongs to the
algorithm, not to the arithmetic precision: a stable method stays accurate at
high precision, an unstable one does not.

**The two errors oppose.** For a method with step size $h$, truncation error
falls as a power of $h$ while round-off error grows like $1/h$ (and worse if the
recurrence is unstable). The total therefore has a *minimum* at some optimal
$h$, and below that $h$ further refinement makes the answer worse. This is the
central practical fact of numerical computation, and it is why the choice of
$h$, the stopping test and the stability of the recurrence are all part of the
method rather than details of implementation.

> [!warning] The common slip
> Students write "truncation and round-off errors are both bad, take the
> average". They are not two estimates of the same quantity that you average.
> They have opposite dependence on $h$ and only their sum matters.

---

### **(c) Find the number of terms in the exponential series such that their sum gives the value of $e^x$ correct to five decimal places for all values of $x$ in the range $0 \le x \le 1$.**

*[Marks: 04]*

**The phrase that decides the answer is "for all values of $x$".** You are not
being asked for a term count that works at one particular $x$. You are being
asked for one that works *everywhere* on $[0, 1]$. So the first job is to find
the worst point on that interval and work there.

**The series and its remainder.**

$$e^x = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \cdots + \frac{x^n}{n!} + \cdots$$

After $k$ terms the remainder is, by Taylor's theorem in Lagrange form,

$$R_k = \frac{e^{\xi}x^k}{k!}, \qquad 0 < \xi < x$$

Now bound each factor. On $[0,1]$ we have $x^k \le 1$, and since $\xi < x \le 1$
we have $e^{\xi} \le e$. So

$$|R_k| \le \frac{e}{k!} = \frac{2.718282}{k!}$$

**Where is the worst case?** The bound $\dfrac{e}{k!}$ is attained at $x = 1$,
and at $x=1$ the error really is its largest, since every term $x^n$ grows with
$x$ on $[0,1]$. So $x = 1$ is the point to test and no other point can be worse.

**"Correct to five decimal places" means an error below $0.5 \times 10^{-5}$.**
Not below $10^{-5}$. Getting this factor of two wrong doubles your term count
and is the single most common error in this question.

**Test $k$.**

| $k$ | Tail bound $\dfrac{1}{k!}\dfrac{k+1}{k}$ | Verdict |
| :--: | :-- | :-- |
| 8 | $\dfrac{1}{40320}\left(\dfrac{9}{8}\right) = 2.786 \times 10^{-5}$ | too large |
| 9 | $\dfrac{1}{362880}\left(\dfrac{10}{9}\right) = 3.062 \times 10^{-6}$ | below $5\times10^{-6}$ |

Hence the remainder tail is bounded by
$R_9 \le 3.062 \times 10^{-6} < 0.5 \times 10^{-5}$, which certifies nine terms.

**Direct check at the worst point.** Summing the first nine terms,

$$S_9 = 2 + 0.5 + 0.166667 + 0.041667 + 0.008333 + 0.001389 + 0.000198 + 0.0000248 = 2.71827877$$

against $e = 2.71828183$, so the actual error is $3.06 \times 10^{-6}$, about
half the bound. With eight terms $S_8 = 2.71825397$ and $|e - S_8| =
2.79 \times 10^{-5}$, far too large.

$$\boxed{9\ \text{terms}}$$

> [!info] Why the geometric tail resolves the bound
> The error after nine terms is the tail $R_9 = \sum_{n=9}^{\infty}\dfrac{1}{n!}$.
> Since $\dfrac{1}{9!} = 2.7557\times10^{-6}$ and the tail is bounded by
> $\dfrac{1}{9!}\left(1 + \dfrac{1}{10} + \dfrac{1}{10\cdot11} + \cdots\right) < \dfrac{10}{9\cdot9!} = 3.062\times10^{-6}$,
> the true error $3.06\times10^{-6}$ sits well below the tolerance $5\times10^{-6}$.
> Note that the cruder Lagrange bound $\dfrac{e}{k!}$ gives $\dfrac{e}{9!} = 7.491\times10^{-6}$,
> which exceeds $5\times10^{-6}$ only because $e \approx 2.718$ is a conservative bound for $e^\xi$ on $[0,1]$;
> the exact geometric tail certifies that nine terms clear the tolerance while eight do not.

---

## Question 2

### **(a) Develop an algorithm to calculate the root of any non-linear equation by bisection method.**

*[Marks: 04]*

**The idea in one sentence.** $f$ is continuous and changes sign on $[a,b]$, so
halve the interval, keep the half that still changes sign, and repeat. The
error halves every step, so the method cannot stall.

**Algorithm.**

1. Read $f(x)$, the tolerance $\varepsilon$, and a maximum iteration count $N$.
2. Accept the bracket $a$, $b$.
3. Compute $f(a)$ and $f(b)$. If $f(a)f(b) > 0$, report that the interval does
   not bracket a root and stop.
4. Set $c = \dfrac{a + b}{2}$ and compute $f(c)$.
5. If $|f(c)| < \varepsilon$, or $|b - a| < \varepsilon$, accept $c$ and stop.
6. If $f(a)f(c) < 0$, set $b = c$; otherwise set $a = c$.
7. If the iteration count exceeds $N$, report non-convergence and stop.
   Otherwise return to step 4.

**Why the iteration count is known in advance.** After $n$ halvings the
interval has width $\dfrac{b-a}{2^n}$, and $c$ is its midpoint, so the error in
$c$ is at most half the width:

$$n = \left\lceil \log_2\frac{b-a}{\varepsilon}\right\rceil$$

That closed form is the reason bisection is worth writing an algorithm for at
all. Newton is faster but you cannot predict how long it will take.

**Merits.** Guaranteed convergence whenever the initial interval brackets a
root and $f$ is continuous, and exactly one evaluation of $f$ per step.

**Demerits.** Slow compared with Newton or regula falsi, because halving throws
away half the information each time. The count is fixed by the tolerance rather
than by the shape of $f$. And you must find a bracketing interval first, which
for an even-multiplicity root can be impossible.

> [!warning] Where bisection quietly fails
> If $f$ has a root at which it touches zero without changing sign, such as
> $(x-2)^2$, then $f(a)f(b) > 0$ at the true bracket and step 3 rejects it. The
> method cannot find an even-multiplicity root at all, and no amount of
> iteration will help. This is not a bug in the algorithm; it is a property of
> sign-change bracketing.

---

### **(b) Derive the expression of the next approximation of a root of the non-linear function $f(x) = 0$ using regula-falsi method.**

*[Marks: 04]*

**Setup.** Let $x_0$ and $x_1$ satisfy $f(x_0)f(x_1) < 0$, so a root lies
between them. Write $f_0 = f(x_0)$ and $f_1 = f(x_1)$.

**The idea.** Replace $f$ on $[x_0, x_1]$ by the straight line through the two
known points, and take where that line crosses the $x$-axis. Because the line
joins $f_0$ and $f_1$, which have opposite signs, it must cross.

**Derivation.** The chord has equation

$$\frac{y - f_0}{f_1 - f_0} = \frac{x - x_0}{x_1 - x_0}$$

Set $y = 0$ and call the resulting $x$ the next approximation $x_2$:

$$\frac{-f_0}{f_1 - f_0} = \frac{x_2 - x_0}{x_1 - x_0}$$

$$x_2 - x_0 = \frac{-f_0(x_1 - x_0)}{f_1 - f_0}$$

$$\boxed{x_2 = x_0 - \frac{f_0(x_1 - x_0)}{f_1 - f_0}}$$

**The same formula, written another way.** Combining over a common denominator,

$$x_2 = \frac{x_0(f_1 - f_0) - f_0(x_1 - x_0)}{f_1 - f_0} = \frac{x_0f_1 - x_1f_0}{f_1 - f_0}$$

which is the form most textbooks print. The two forms are identical, and the
second one shows immediately that $x_2$ is a *weighted average* of $x_0$ and
$x_1$ with weights $f_1$ and $-f_0$. A weighted average of two numbers stays
between them, which is why regula falsi never leaves the bracket, exactly like
bisection.

**Continuing.** Evaluate $f(x_2)$, replace whichever of $x_0$, $x_1$ has the
same sign as $f(x_2)$, and apply the same formula again.

**Convergence and the one weakness.** The sign change is always preserved, so
the method converges whenever the initial pair brackets a root. Convergence is
linear, and faster than bisection because a chord is a better model of $f$ than
a midpoint. The weakness is that *one end of the bracket can stall*: if the
function is strongly curved near the root, one function value stays much larger
in magnitude than the other for many iterations and that endpoint never moves
appreciably. The Illinois modification, which halves the retained function
value once an endpoint fails to update, exists to repair exactly this.

---

### **(c) Find the real root of the equation $x \sin x + \cos x = 0$ using N-R method.**

*[Marks: 04]*

**Write the function and differentiate it, carefully.**

$$f(x) = x\sin x + \cos x$$

$$f'(x) = \frac{d}{dx}(x\sin x) + \frac{d}{dx}(\cos x) = (\sin x + x\cos x) - \sin x = x\cos x$$

> [!warning] This derivative is the whole question
> The two $\sin x$ terms cancel and you are left with $x\cos x$. Students who
> differentiate $x\sin x$ as $\cos x$ get $f'(x) = \cos x - \sin x$ and then
> wander. Differentiate the whole expression once, do not term-slice it.

**Choose a starting value, and justify it by a sign check.**

| $x$ | $f(x) = x\sin x + \cos x$ |
| :--: | :-- |
| 2.0 | $2(0.90930) + (-0.41615) = 1.40245$ |
| 2.5 | $2.5(0.59847) + (-0.80114) = 0.69504$ |
| 3.0 | $3(0.14112) + (-0.98999) = -0.56663$ |

$f$ changes sign between $2.5$ and $3.0$, so a root lies there. Take $x_0 = 3$.

**Iterate.**

$$x_{n+1} = x_n - \frac{x_n\sin x_n + \cos x_n}{x_n\cos x_n}$$

| $n$ | $x_n$ | $f(x_n)$ | $f'(x_n) = x_n\cos x_n$ | $x_{n+1}$ |
| :--: | :--: | :-- | :-- | :-- |
| 0 | $3.0000000$ | $-0.56663$ | $-2.96998$ | $2.8092132$ |
| 1 | $2.8092132$ | $-0.02864$ | $-2.65546$ | $2.7984273$ |
| 2 | $2.7984273$ | $-1.087\times10^{-4}$ | $-2.63526$ | $2.7983860$ |

The correction at the last step is $4.1\times10^{-5}$, already below $10^{-4}$,
so the value is accepted.

$$\boxed{x = 2.7984}$$

**What the root means.** The equation rearranges to $x = -\cot x$, so the root
is where the line $y = x$ meets the curve $y = -\cot x$. There is one such
crossing near $2.80$, and that is the value found.

> [!info] Two things the iteration table alone will not tell you
> First, the table is not self-validating. The $f'(x_n)$ column must equal
> $x_n\cos x_n$ at the $x_n$ printed beside it, and in a printed table that
> identity is the cheapest way to catch a slip, because the next iterate is
> $x_n - f(x_n)/f'(x_n)$ and the division only works if the two columns belong
> to the same $x_n$.
>
> Second, convergence to a fixed point of the iteration is not the same as
> finding the root, unless the starting point is inside a basin that collapses
> to it. Running the same iteration from $x_0 = 2.6$ gives $2.8169812$, then
> $2.7985064$, then $2.7983861$ and then $2.7983860$. Two starts inside the
> same bracket landing on the same digits is the evidence that the iteration has
> found the root rather than a fixed point of its own.

---

## Question 3

### **(a) Explain the use of Lagrange's interpolation formula.**

*[Marks: 02]*

**The use.** Given a tabulated set $(x_i, f_i)$, estimate $f(x)$ at a point $x$
lying inside the range of the table, without assuming the abscissae are equally
spaced.

**The formula.** For $n+1$ points,

$$f(x) \approx \sum_{i=0}^{n} f_i \prod_{\substack{j=0 \\ j \ne i}}^{n}\frac{x - x_j}{x_i - x_j}$$

**Four reasons it is used.**

1. **Unequal spacing is allowed.** This is the principal advantage over
   Newton's forward and backward formulas, which both need a common tabular
   spacing $h$. Experimental data with a varying interval can be used directly.
2. **The tabulated order is irrelevant.** The formula is symmetric in the
   points; permuting them leaves the result unchanged. Worth knowing when a
   printed table lists its entries out of order.
3. **One expression gives the value.** The whole formula is written once and
   evaluated at any $x$ in range, with no successive-difference table to build.
4. **The error is available.** With $n+1$ points,
   $R_n = \dfrac{f^{(n+1)}(\xi)}{(n+1)!}\prod_{i=0}^{n}(x - x_i)$, so the
   accuracy of a chosen set can be judged before any arithmetic is done.

**Limitations.** Adding a point means recomputing every coefficient, unlike
Newton's divided-difference form where earlier work is retained. And it is
inefficient for repeated evaluation at many points, where writing the single
interpolating polynomial out once and evaluating it is cheaper.

> [!note] Newton's form and Lagrange's form are the same polynomial
> They differ only in organisation. If you have a regular table, build the
> divided-difference table and use Newton's form. If the spacing is irregular
> or you have only the points to hand, write Lagrange's directly. Never build
> Newton's *forward* formula on an irregular table, because $h$ does not exist.

---

### **(b) The upward velocity of a rocket is given as a function of time in table below. Determine the value of the velocity at $t = 16$ seconds using $1^{\text{st}}$ order polynomial.**

*[Marks: 06]*

| $t$ (sec) | 0 | 10 | 15 | 20 | 22.5 | 30 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| $v(t)$ (m/s) | 0 | 227.04 | 362.78 | 517.35 | 602.97 | 901.67 |

**"First order polynomial" means a straight line, and this is the trap in the
question.** Read the table and notice that $t = 16$ is *not* a tabulated value,
and the intervals are irregular: $10$, $5$, $5$, $2.5$, $7.5$. That rules out
every Newton's forward and backward formula, because there is no common $h$.
So the only tool that fits both the order requested and the spacing given is
the two-point linear form.

**Find the bracketing pair.** $16$ lies between $15$ and $20$, so use
$(t_0, v_0) = (15, 362.78)$ and $(t_1, v_1) = (20, 517.35)$. Using any other
pair would be extrapolation dressed up as interpolation.

**The linear polynomial.**

$$v(t) = v_0 + \frac{t - t_0}{t_1 - t_0}(v_1 - v_0) = 362.78 + \frac{t - 15}{5}(517.35 - 362.78)$$

**Evaluate at $t = 16$.**

$$v(16) = 362.78 + \frac{16 - 15}{5}(154.57) = 362.78 + \frac{154.57}{5} = 362.78 + 30.914$$

$$\boxed{v(16) = 393.694\ \text{m/s}}$$

> [!info] What a second-degree comparison tells you
> Fit a parabola through the *same three* points $(10, 227.04)$, $(15, 362.78)$
> and $(20, 517.35)$. Solving the three normal equations gives
> $v(t) = 0.37660t^2 + 17.7330t + 12.050$, and at $t = 16$ that is
> $96.4096 + 283.728 + 12.050 = 392.1876$. The two estimates differ by
> $1.5064$ m/s, about $0.38\%$.
>
> You can read that gap without solving for the parabola at all. The second
> difference of the three tabulated values is
> $\dfrac{227.04 - 2(362.78) + 517.35}{5^2} = \dfrac{18.83}{25} = 0.7532$, so
> $v'' \approx 0.7532$ m/s³ near $t = 16$. The error of a chord on $[15, 20]$
> at an interior point $x$ is $\tfrac12 v''(x)(x - a)(x - b)$, which at $x=16$
> is $\tfrac12(0.7532)(1)(-4) = -1.5064$. The linear value sits *above* the
> parabola because $(16-15)(16-20)$ is negative, and the size of the gap is
> exactly the printed $1.5064$. Two independent routes, one solving and one
> estimating from curvature, agreeing on both size and sign.
>
> The tabulated slopes make the sign inevitable anyway: they run $22.704$,
> $27.148$, $30.914$, $34.248$, $39.827$ across the successive steps $10$, $5$,
> $5$, $2.5$, $7.5$. The curve is steepening without interruption, so it is
> convex, so a chord lies below it on the left half of the interval and above it
> on the right, and $t=16$ is in the right half.

> [!warning] Do not over-answer this
> The question specifies a first-order polynomial and the answer is the linear
> value. Reporting the quadratic value as the answer costs the marks even
> though it is a defensible number. Report the requested order, and record the
> comparison only as a check.

---

### **(c) Find $f(2.5)$ from the given data, $x$: 1, 2, 3 and $f(x)$: 0, 1, 8.**

*[Marks: 04]*

| $x$ | 1 | 2 | 3 |
| :---: | :---: | :---: | :---: |
| $f(x)$ | 0 | 1 | 8 |

**The method.** Three points, so a quadratic, so Lagrange's formula. Here the
spacing *is* uniform, but Lagrange is still the shortest route because there is
no difference table to build and only three basis polynomials to evaluate.

$$f(x) = \frac{(x - x_1)(x - x_2)}{(x_0 - x_1)(x_0 - x_2)}f_0 + \frac{(x - x_0)(x - x_2)}{(x_1 - x_0)(x_1 - x_2)}f_1 + \frac{(x - x_0)(x - x_1)}{(x_2 - x_0)(x_2 - x_1)}f_2$$

**Evaluate each basis polynomial at $x = 2.5$.**

$$L_0 = \frac{(2.5 - 2)(2.5 - 3)}{(1 - 2)(1 - 3)} = \frac{(0.5)(-0.5)}{(-1)(-2)} = -0.125$$

$$L_1 = \frac{(2.5 - 1)(2.5 - 3)}{(2 - 1)(2 - 3)} = \frac{(1.5)(-0.5)}{(1)(-1)} = 0.75$$

$$L_2 = \frac{(2.5 - 1)(2.5 - 2)}{(3 - 1)(3 - 2)} = \frac{(1.5)(0.5)}{(2)(1)} = 0.375$$

$$f(2.5) = 0(-0.125) + 1(0.75) + 8(0.375) = 0 + 0.75 + 3.0$$

$$\boxed{f(2.5) = 3.75}$$

> [!info] Two checks that catch different mistakes
> **Partition of unity.** $-0.125 + 0.75 + 0.375 = 1$ exactly. The Lagrange
> basis polynomials of degree $n$ must sum to the constant $1$ at every $x$,
> because they are interpolating the function $y = 1$. If your three numbers do
> not sum to $1$, at least one of them was miscomputed, and you can find which by
> checking them one at a time.
>
> **The polynomial itself.** Newton's divided differences give
> $f[x_0,x_1] = 1$, $f[x_1,x_2] = 7$ and $f[x_0,x_1,x_2] = \dfrac{7 - 1}{3 - 1} = 3$, so
> $f(x) = 0 + 1(x - 1) + 3(x-1)(x-2) = 3x^2 - 8x + 5$. At $x = 2.5$:
> $3(6.25) - 8(2.5) + 5 = 18.75 - 20 + 5 = 3.75$. And the polynomial
> reproduces the table: $f(1) = 0$, $f(2) = 1$, $f(3) = 8$. Note that the
> divided-difference route is *also* a check on the answer, not merely a
> restatement: it uses the data through a completely different arrangement of
> the arithmetic.

---

## Question 4

### **(a) What is meant by over-relaxation and under-relaxation?**

*[Marks: 02]*

Both terms describe a modification of the Gauss-Seidel iteration that inserts a
**relaxation parameter** $\omega$:

$$x_i^{(k+1)} = (1 - \omega)x_i^{(k)} + \omega\hat x_i^{(k)}$$

where $\hat x_i^{(k)}$ is the value the ordinary Gauss-Seidel recursion would
have produced from iteration $k$.

**Under-relaxation, $0 < \omega < 1$.** Each new iterate is a blend of the old
value and the Gauss-Seidel value, so the sequence advances by a *fraction* of
the full step. This damps oscillation and is what you reach for when the plain
iteration oscillates or diverges: the effective step is smaller, so the spectral
radius of the iteration matrix comes down, at the cost of more iterations.

**Over-relaxation, $1 < \omega < 2$.** Each new iterate *overshoots* the plain
Gauss-Seidel value, so the sequence covers the distance faster. The method is
then called Successive Over-Relaxation, SOR, and an optimal $\omega$ can cut
the iteration count substantially.

**The two regimes are separated by $\omega = 1$.** At $\omega = 1$ the formula
reduces to ordinary Gauss-Seidel. Above $1$ it is accelerated, below $1$ it is
stabilised. The purpose in both cases is the same: to control the rate at which
error is carried from one iteration to the next.

> [!note] Why not simply take $\omega$ large?
> Overshoot only helps while the iteration is still contracting. Past
> $\omega_{\text{opt}}$ the spectral radius starts growing again and the
> iteration diverges, so $\omega$ must stay below $2$ and in practice close to
> $1$.

---

### **(b) Solve the following circuit by using Gauss-Seidel method.**

*[Marks: 05]*

**The circuit.** A planar four-mesh network in a $2\times2$ arrangement, with
both a voltage source and a current source.

```text
                  10 Ω                       10 A (←)
         +-------/\/\/\/\-------+------------( ← )-----------+
         |        10 Ω          |           10 A              |
         |                      |                            |
         |                    [20 Ω]                         |
         |      (↻ I₁)          |            (↻ I₂)          |
         |                      |                            |
         +-------/\/\/\/\-------+------------/\/\/\/\--------+
         |        25 Ω          |             25 Ω           |
         |                      |                            |
       ( ↑ ) 100 V            [4 Ω]                        [8 Ω]
         |                      |                            |
         |      (↻ I₄)          |            (↻ I₃)          |
         |                      |                            |
         +----------------------+----------------------------+
```

Reading the four meshes off the drawing:

| Mesh | Boundary |
| :-- | :-- |
| $I_1$ top-left | $10\ \Omega$ top, shared $20\ \Omega$ right, shared $25\ \Omega$ bottom, wire left |
| $I_2$ top-right | $10\ \text{A}$ source top, wire right, shared $25\ \Omega$ bottom, shared $20\ \Omega$ left |
| $I_3$ bottom-right | shared $25\ \Omega$ top, shared $4\ \Omega$ left, $8\ \Omega$ right, wire bottom |
| $I_4$ bottom-left | shared $25\ \Omega$ top, shared $4\ \Omega$ right, $100\ \text{V}$ source left, wire bottom |

**Step 1, and this is the idea the question is built to test: the current
source removes an unknown.** The $10\ \text{A}$ source sits alone in the top
branch of mesh 2; no other mesh touches that branch. So the branch current is
$I_2$ exactly. Taking mesh currents clockwise, the source drives current
*anticlockwise* through it, so

$$I_2 = -10\ \text{A}$$

You now have three equations and three unknowns. Writing four mesh equations
plus the source equation would be five equations in four unknowns.

**Step 2, the three remaining mesh equations.** A shared branch carries the
difference of the two mesh currents, with the sign fixed by which way each mesh
walks it.

*Mesh 1*, clockwise: $10I_1$ across the top, $20(I_1 - I_2)$ down the shared
$20\ \Omega$, $25(I_1 - I_4)$ back along the shared $25\ \Omega$, and nothing
across the left wire:

$$10I_1 + 20(I_1 - I_2) + 25(I_1 - I_4) = 0 \implies 55I_1 - 25I_4 = 20I_2 = -200$$

*Mesh 3*, clockwise: $25(I_3 - I_2)$ along the shared $25\ \Omega$, $8I_3$ down
the right branch, $4(I_3 - I_4)$ up the shared $4\ \Omega$:

$$8I_3 + 25(I_3 - I_2) + 4(I_3 - I_4) = 0 \implies 37I_3 - 4I_4 = 25I_2 = -250$$

*Mesh 4*, clockwise: the $100\ \text{V}$ source is entered *against* the
traversal, so it contributes $-100$ as a drop; the two shared branches give
$25(I_4 - I_1)$ and $4(I_4 - I_3)$:

$$25(I_4 - I_1) + 4(I_4 - I_3) = 100 \implies -25I_1 - 4I_3 + 29I_4 = 100$$

**Step 3, put each equation in Gauss-Seidel form**, solving for its own
diagonal unknown:

$$I_1^{(k+1)} = \frac{-200 + 25I_4^{(k)}}{55}, \qquad I_3^{(k+1)} = \frac{-250 + 4I_4^{(k)}}{37}, \qquad I_4^{(k+1)} = \frac{100 + 25I_1^{(k+1)} + 4I_3^{(k+1)}}{29}$$

Note the ordering. $I_1$ and $I_3$ are computed from the *old* $I_4$, then $I_4$
is computed from the two values just obtained. That is what distinguishes
Gauss-Seidel from Jacobi, in which every update uses only values from the
previous sweep. Start from $I_1 = I_3 = I_4 = 0$.

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

**Step 4, the limit.** The iteration is converging, and eliminating the same
three equations gives the exact values

$$I_1 = -\frac{14390}{3501} = -4.1103\ \text{A}, \qquad I_3 = -\frac{24050}{3501} = -6.8695\ \text{A}, \qquad I_4 = -\frac{3650}{3501} = -1.0426\ \text{A}$$

$$\boxed{I_1 = -4.1103\ \text{A}, \quad I_2 = -10\ \text{A}, \quad I_3 = -6.8695\ \text{A}, \quad I_4 = -1.0426\ \text{A}}$$

> [!warning] Diagonal dominance, and why the convergence is slow
> Look at the third equation: $|29|$ against $|{-25}| + |{-4}| = 29$. The
> inequality holds with *equality*, so the system is only weakly diagonally
> dominant and the Gauss-Seidel iteration converges, but slowly. That is
> visible in the table: the correction per sweep falls by only about a factor
> of two per sweep at the start and does not visibly accelerate. On the first
> two equations the inequality is comfortable, $55 > 25$ and $37 > 4$, so the
> system is convergent overall. A student who expects eight sweeps to reach
> eight decimals has misread this row.
>
> The elimination result is exact and is the value to report; the iteration is
> what the question asked for as the method.

> [!info] The check that is worth more than the arithmetic
> Take the four currents into the three mesh equations at the four-decimal
> precision they are quoted to: $55(-4.1103) - 25(-1.0426) = -226.0665 +
> 26.0650 = -200.0015$; $37(-6.8695) - 4(-1.0426) = -254.1715 + 4.1704 =
> -250.0011$; $-25(-4.1103) - 4(-6.8695) + 29(-1.0426) = 102.7575 + 27.4780 -
> 30.2354 = 100.0001$. Each residual sits at $10^{-4}$, which is what rounding
> four numbers to four decimals must produce, and on the exact fractions all
> three return their right-hand sides with no residual at all.
>
> Then confirm with a different formulation entirely. Nodal analysis, with the
> left node held at $100\ \text{V}$ by the source and the bottom rail as
> reference, needs only three unknowns: the top-middle node, the central node
> and the top-right node. Their KCL equations are
> $\dfrac{v_{tm}-100}{10} + \dfrac{v_{tm}-v_c}{20} - 10 = 0$ (the $10$ leaves as
> the source current), $\dfrac{v_c - v_{tm}}{20} + \dfrac{v_c-100}{25} +
> \dfrac{v_c - v_{tr}}{25} + \dfrac{v_c}{4} = 0$, and
> $\dfrac{v_{tr}-v_c}{25} + \dfrac{v_{tr}}{8} + 10 = 0$. Solving gives
> $v_{tm} = 141.103\ \text{V}$, $v_c = 23.308\ \text{V}$, $v_{tr} = -54.956\ \text{V}$.
> Reading the mesh currents back out of those potentials,
> $I_1 = (100 - 141.103)/10 = -4.1103$ and $I_3 = -54.956/8 = -6.8695$, with
> $I_2 = -10$ from the source, agreeing to four digits.
>
> Two formulations that share no unknown and no equation reach the same
> currents. That is the strongest confirmation available, and it costs about a
> minute.

---

### **(c) The following data was taken from an experiment that measured the current in a wire for various imposed voltages. On the basis of a linier regression of this data, determine current for a voltage of $3.5\text{ V}$. Plot the line to evaluate the fit.**

*[Marks: 05]*

| $v$ (V) | 2 | 3 | 4 | 5 | 7 | 10 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| $i$ (A) | 5.2 | 7.8 | 10.7 | 13 | 19.3 | 27.5 |

**The method.** Fit $i = a + bv$ by least squares, meaning the line that
minimises the sum of squared vertical residuals. With $n = 6$ the quantities
you need are

$$\sum v = 31, \qquad \sum i = 83.5, \qquad \sum v^2 = 203, \qquad \sum vi = 551.7$$

**The normal equations.**

$$na + b\sum v = \sum i, \qquad a\sum v + b\sum v^2 = \sum vi$$

Solving, or equivalently using the closed forms,

$$b = \frac{n\sum vi - \sum v\sum i}{n\sum v^2 - \left(\sum v\right)^2} = \frac{6(551.7) - 31(83.5)}{6(203) - 31^2} = \frac{721.7}{257} = 2.8082\ \text{A/V}$$

$$a = \bar i - b\bar v = \frac{83.5}{6} - 2.8082\left(\frac{31}{6}\right) = 13.9167 - 14.5089 = -0.5922\ \text{A}$$

$$\boxed{i = -0.5922 + 2.8082\,v}$$

**The current at $3.5\ \text{V}$.**

$$i(3.5) = -0.5922 + 2.8082(3.5) = -0.5922 + 9.8287 = 9.2364$$

$$\boxed{i(3.5\ \text{V}) = 9.2364\ \text{A}}$$

**Plotting the fit, and reading the quality off the plot.** The six measured points $(v, i)$ and the fitted line $i = -0.5922 + 2.8082\,v$:

![Linear regression plot of current versus voltage with measured points, fitted line, and evaluated point at 3.5V](../answers_exam_style/diagrams/2018_Q4c_regression.png)

The measured values and residuals against the line are:

| $v$ | measured $i$ | fitted $i$ | residual |
| :--: | :-- | :-- | :-- |
| 2 | 5.2 | $5.0241$ | $+0.1759$ |
| 3 | 7.8 | $7.8323$ | $-0.0323$ |
| 4 | 10.7 | $10.6405$ | $+0.0595$ |
| 5 | 13 | $13.4486$ | $-0.4486$ |
| 7 | 19.3 | $19.0650$ | $+0.2350$ |
| 10 | 27.5 | $27.4895$ | $+0.0105$ |

The residuals are small beside the values themselves, the largest in magnitude
being $0.4486$ against $13$, so a straight line is a reasonable model for a
wire at constant temperature.

> [!info] Three checks, each catching a different error
> **Residuals sum to zero.** A least-squares fit is defined by setting the
> derivatives of the sum of squared residuals to zero, and the derivative with
> respect to $a$ is $\sum (f_i - y_i)$. So the residuals *must* sum to zero, to
> rounding. Here they sum to $0.1759 - 0.0323 + 0.0595 - 0.4486 + 0.2350 +
> 0.0105 = 0.0000$. If a printed table of fitted values does not give residuals
> summing to zero, a fitted value is wrong, and this is a one-line test that
> finds it.
>
> **The line passes through the centroid.** The normal equations also give
> $a + b\bar v = \bar i$, so the fitted line must pass through
> $(\bar v, \bar i) = (5.1667, 13.9167)$. Substituting:
> $-0.5922 + 2.8082(5.1667) = 13.9167$. A line that misses the centroid has had
> the two normal equations swapped, which is the single commonest slip in this
> question.
>
> **Internal interpolation.** The fitted values at $v = 3$ and $v = 4$ are
> $7.8323$ and $10.6405$, and interpolating between them at $v = 3.5$ returns
> their mean, $9.2364$, which is the value computed above. This confirms the
> answer is not an artefact of rounding $a$ and $b$ to four decimals.
>
> **And the single summary number.** The correlation coefficient is
> $r = 0.9996$, so $r^2 = 0.9991$ and over $99.9\%$ of the variation in current
> is accounted for by the line.

> [!note] On the wording
> The paper prints "linier", an evident typo for "linear". It is also worth
> noticing that the question asks for the *current* at a *voltage*, so voltage
> is the independent variable and current is being regressed on voltage. Fitting
> the other way round, $v$ on $i$, is a different computation and a different
> answer.

---

# SECTION B

## Question 5

### **(a) State Newton's forward formula to evaluate $\frac{d^2 y}{dx^2}$ for any value $x \in [x_0, x_n]$.**

*[Marks: 06]*

**Start from the interpolation polynomial.** For a table of common spacing $h$,
Newton's forward formula is

$$y = y_0 + p\Delta y_0 + \frac{p(p-1)}{2!}\Delta^2 y_0 + \frac{p(p-1)(p-2)}{3!}\Delta^3 y_0 + \frac{p(p-1)(p-2)(p-3)}{4!}\Delta^4 y_0 + \cdots$$

with

$$p = \frac{x - x_0}{h}$$

**The chain rule is the whole method.** Since $x$ enters only through $p$,

$$\frac{d}{dx} = \frac{1}{h}\frac{d}{dp}, \qquad \frac{d^2y}{dx^2} = \frac{1}{h^2}\frac{d^2y}{dp^2}$$

So you differentiate the falling-factorial products with respect to $p$, not
with respect to $x$. That is why every coefficient in the answer is a
polynomial in $p$.

**First derivative.**

$$\frac{dy}{dx} = \frac{1}{h}\left[\Delta y_0 + \frac{2p - 1}{2!}\Delta^2 y_0 + \frac{3p^2 - 6p + 2}{3!}\Delta^3 y_0 + \frac{4p^3 - 18p^2 + 22p - 6}{4!}\Delta^4 y_0 + \cdots\right]$$

**Second derivative, differentiating once more.**

$$\frac{d^2y}{dx^2} = \frac{1}{h^2}\left[\Delta^2 y_0 + \frac{6p - 6}{3!}\Delta^3 y_0 + \frac{12p^2 - 36p + 22}{4!}\Delta^4 y_0 + \cdots\right]$$

**Simplifying the coefficients.**

$$\boxed{\frac{d^2y}{dx^2} = \frac{1}{h^2}\left[\Delta^2 y_0 + (p - 1)\Delta^3 y_0 + \left(\frac{p^2}{2} - \frac{3p}{2} + \frac{11}{12}\right)\Delta^4 y_0 + \cdots\right]}$$

**How many points are needed.** A polynomial of degree $n$ through $n+1$ points
has exactly $n+1$ coefficients, so for $n = 1$ only the $\Delta y_0$ term
exists, for $n = 2$ the terms up to $\Delta^2 y_0$, and so on. Since $y''$
needs differences of order two and above, the formula needs at least **three
points** for a quadratic fit, four for a cubic. The next term, omitted above,
carries the coefficient

$$\frac{p^3}{6} - p^2 + \frac{7p}{4} - \frac{5}{6}$$

on $\Delta^5 y_0$.

> [!info] The test that shows the formula is not merely a rule of thumb
> The formula reproduces $\dfrac{d^2y}{dx^2}$ *exactly* for any polynomial of
> degree four or lower, because every term from $\Delta^5 y_0$ onward then
> vanishes. A cubic is the first case where this can be checked without
> appealing to the derivation.
>
> Take $y = ax^3$ tabulated from $x_0 = 0$ at spacing $h$, so $x = ph$. Then
> $\Delta^2 y_0 = y(2h) - 2y(h) + y(0) = 8ah^3 - 2ah^3 = 6ah^3$ and
> $\Delta^3 y_0 = 6ah^3$, with all higher differences zero. The formula gives
> $\dfrac{1}{h^2}\left[6ah^3 + (p - 1)6ah^3\right] = 6ah\left[1 + p - 1\right] = 6aph$.
> The true second derivative is $y'' = 6ax = 6a(ph) = 6aph$. The two agree for
> *every* $p$, not only at the nodes, and that is the property that makes the
> formula useful for interpolation rather than only for differencing at the
> tabulated points.
>
> For a quadratic $y = ax^2 + bx + c$ only $\Delta^2 y_n = 2ah^2$ survives, so
> the formula reduces to $\dfrac{1}{h^2}(2ah^2) = 2a$, again exact.

---

### **(b) From the following table find $x$, correct to two decimal places for which $y$ is maximum and find this value of $y$.**

*[Marks: 06]*

| $x$ | 1.2 | 1.3 | 1.4 | 1.5 | 1.6 |
| :---: | :---: | :---: | :---: | :---: | :---: |
| $y$ | 0.9320 | 0.9636 | 0.9855 | 0.9975 | 0.9996 |

**Step 1, find the direction of the answer before computing anything.** Build
the difference table.

| | 0.9320 | 0.9636 | 0.9855 | 0.9975 | 0.9996 |
| :-- | :-- | :-- | :-- | :-- | :-- |
| $\Delta$ | | $0.0316$ | $0.0219$ | $0.0120$ | $0.0021$ |
| $\Delta^2$ | | | $-0.0097$ | $-0.0099$ | $-0.0099$ |
| $\Delta^3$ | | | | $-0.0002$ | $0.0000$ |
| $\Delta^4$ | | | | | $0.0002$ |

All four first differences are *positive*, so $y$ is still rising at $x = 1.5$.
But the last of them, $0.0021$, is small and the second differences are all
negative, so $y$ is levelling off and the peak lies just *inside* the end of the
table, close to but before $x = 1.6$. If you read that last $0.0021$ as having
"already changed sign" and go looking beyond $1.6$, you will extrapolate
outside the data and get a different answer.

**Step 2, use the backward form, because the maximum is at the far end.** At
$x_4 = 1.6$ with $q = (x - x_4)/h$,

$$\frac{dy}{dx} = \frac{1}{h}\left[\nabla y_4 + \frac{2q + 1}{2}\nabla^2 y_4 + \frac{3q^2 + 6q + 2}{6}\nabla^3 y_4 + \frac{4q^3 + 18q^2 + 22q + 6}{24}\nabla^4 y_4\right]$$

with

$$\nabla y_4 = 0.0021, \qquad \nabla^2 y_4 = -0.0099, \qquad \nabla^3 y_4 = 0.0000, \qquad \nabla^4 y_4 = 0.0002$$

**Step 3, set the derivative to zero.** With $\nabla^3 y_4 = 0$ and
$\nabla^4 y_4$ tiny, the stationary point is set almost entirely by the first
two terms:

$$0.0021 + \frac{2q + 1}{2}(-0.0099) = 0 \implies (q + 0.5)(0.0099) = 0.0021$$

$$q + 0.5 = \frac{0.0021}{0.0099} = 0.212121, \qquad q = -0.287879$$

$$x = x_4 + hq = 1.6 + 0.1(-0.287879) = 1.5712$$

The negative $q$ is the answer to "which side", stated numerically: the maximum
is inside the table.

**Step 4, evaluate $y$ there** with the full five-point backward polynomial,

$$y = y_4 + q\nabla y_4 + \frac{q(q+1)}{2}\nabla^2 y_4 + \frac{q(q+1)(q+2)}{6}\nabla^3 y_4 + \frac{q(q+1)(q+2)(q+3)}{24}\nabla^4 y_4$$

$$y = 0.9996 + (-0.287879)(0.0021) + \frac{(-0.287879)(0.712121)}{2}(-0.0099) + 0 + \frac{(-0.287879)(0.712121)(1.712121)(2.712121)}{24}(0.0002)$$

$$y = 0.9996 - 0.0006045 + 0.0010148 - 0.0000079 = 1.0000023$$

$$\boxed{x = 1.57 \text{ (correct to two decimal places)}, \qquad y_{\max} = 1.0000}$$

> [!note] Why $y_{\max} = 1.0000$ looks odd and is not an error
> The table's largest entry is $0.9996$, and the interpolated maximum comes out
> at $1.0000023$, which is just *above* $1$. That is exactly what a parabola
> through five points should do: the points at $1.5$ and $1.6$ are still rising
> at a decreasing rate, so the fitted curve peaks slightly above the last
> sample. Rounded to four decimals it reads $1.0000$. Do not "correct" it to
> $0.9996$; the tabulated value and the interpolated maximum are different
> quantities.

> [!info] Confirming with a completely separate route
> Fitting one polynomial through all five points by Lagrange interpolation gives
> $y = \dfrac{x^4}{12} - \dfrac{29x^3}{60} + \dfrac{133x^2}{240} +
> \dfrac{409x}{750} + \dfrac{71}{500}$, which reproduces $0.9320$, $0.9636$,
> $0.9855$, $0.9975$, $0.9996$ at $1.2$ through $1.6$ exactly. Differentiating,
> $y' = \dfrac{x^3}{3} - \dfrac{29x^2}{20} + \dfrac{133x}{120} +
> \dfrac{409}{750}$, and $y' = 0$ has three real roots, $x = -0.3344$,
> $x = 1.5713$ and $x = 3.1131$. Only $1.5713$ lies inside $[1.2, 1.6]$, so it
> is the only candidate, and $y$ there is $1.0000023$, matching the
> backward-difference route. The $\Delta^4$ term shifted the stationary point by
> $9.1\times10^{-5}$, which is why the two routes agree to the digits shown.
>
> Confirming it is a *maximum*: $y'' = x^2 - \dfrac{29x}{10} + \dfrac{133}{120}$
> evaluates to $-0.9795$ at $x = 1.5713$, which is negative. And the sign is
> forced by the second difference row, which is negative throughout, so $y$
> must be concave near the peak regardless of the polynomial used.

---

## Question 6

### **(a) The vertical distance covered by a rocket from $t = 8$ to $t = 30$ seconds is given by: $x = \int_8^{30} \left( 2000 \ln \left[ \frac{140000}{140000 - 2100t} \right] - 9.8t \right) dt$. (i) Use eight-segment Simpson's $\frac{1}{3}$ rule to find the distance covered. (ii) Find the true error of part (i). (iii) Find the absolute relative error for part (i).**

*[Marks: 08]*

**(i) Eight-segment Simpson's $\frac{1}{3}$ rule.**

Simpson's $\frac{1}{3}$ rule needs an **even** number of segments, because it
consumes nodes in pairs. Eight is even, so there are nine nodes. With $n = 8$,

$$h = \frac{30 - 8}{8} = 2.75, \qquad t_i = 8 + 2.75i,\quad i = 0,\dots,8$$

which gives $t = 8,\ 10.75,\ 13.5,\ 16.25,\ 19,\ 21.75,\ 24.5,\ 27.25,\ 30$.

Evaluate $f(t) = 2000\ln\left[\dfrac{140000}{140000 - 2100t}\right] - 9.8t$ at each
node:

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

The weights are $1, 4, 2, 4, \dots, 4, 1$: the odd-indexed interior nodes get
$4$ and the even-indexed ones get $2$, with both endpoints getting $1$.

$$x \approx \frac{h}{3}\left[f_0 + f_8 + 4(f_1 + f_3 + f_5 + f_7) + 2(f_2 + f_4 + f_6)\right]$$

Grouping the sums first keeps the arithmetic honest:

$$f_1 + f_3 + f_5 + f_7 = 246.3351814 + 399.5165393 + 576.6423135 + 783.9826784 = 2006.4767126$$

$$f_2 + f_4 + f_6 = 320.2468886 + 484.7454726 + 676.0501168 = 1481.0424780$$

$$x \approx \frac{2.75}{3}\left[177.2667430 + 901.6740015 + 4(2006.4767126) + 2(1481.0424780)\right]$$

$$= \frac{2.75}{3}\left[177.2667430 + 901.6740015 + 8025.9068504 + 2962.0849560\right] = \frac{2.75}{3}(12066.9325509)$$

$$\boxed{x \approx 11061.3548\ \text{m}}$$

**(ii) The true error.** "True error" is the exact value minus the
approximation, and it has a sign; the *absolute* error does not. The exact
integral is obtainable here, which is what makes the question possible:

$$x_{\text{exact}} = \int_8^{30}\left(2000\ln\left[\frac{140000}{140000 - 2100t}\right] - 9.8t\right)dt = 11061.3355\ \text{m}$$

$$E_t = x_{\text{exact}} - x \approx 11061.3355 - 11061.3548 = -0.0193\ \text{m}$$

$$\boxed{E_t \approx -0.0193\ \text{m}}$$

The sign says the Simpson estimate lies *above* the true distance. For a
positive integrand that is convex over the whole interval, which this one is,
that is the expected direction.

**(iii) The absolute relative error.**

$$|\varepsilon_t| = \left|\frac{\text{true error}}{\text{true value}}\right| \times 100\% = \left|\frac{-0.0193}{11061.3355}\right|\times 100\%$$

$$\boxed{|\varepsilon_t| \approx 0.00017\%}$$

> [!info] Showing the error is truncation, not arithmetic
> Obtain the exact value by antidifferentiation:
> $\int 2000\ln\left[\dfrac{140000}{140000-2100t}\right]dt =
> -\dfrac{2000}{2100}(140000-2100t)\left[\ln\left(\dfrac{140000-2100t}{140000}\right) - 1\right]$,
> evaluated between the limits, which gives $11061.3355$.
>
> Then repeat the numerical integration with the mesh refined. Sixteen segments
> gives $11061.3368$ and thirty-two gives $11061.3356$. The three errors against
> the exact value are
>
> | segments | estimate | error | ratio to previous |
| :--: | --: | --: | --: |
| 8 | 11061.3548 | $1.93\times10^{-2}$ | |
| 16 | 11061.3368 | $1.22\times10^{-3}$ | $15.9$ |
| 32 | 11061.3356 | $7.6\times10^{-5}$ | $16.0$ |
>
> Each halving of $h$ divides the error by sixteen. That is precisely the
> $O(h^4)$ convergence of Simpson's $\frac{1}{3}$ rule, and it is the strongest
> evidence available that the residual is a truncation error of the rule. An
> arithmetic slip does not shrink by a factor of sixteen when the mesh is
> refined; it stays where it is. Note also that all three estimates lie *above*
> the exact value and approach it monotonically, which is what convexity
> predicts.

---

### **(b) Determine the value of $n$ so that the trapezoidal rule will approximate the value of $\int_0^1 \sqrt{1 + x^2} \, dx$ with an error that is less than $0.01$.**

*[Marks: 04]*

**The bound.** The composite trapezoidal rule over $[a,b]$ with $n$
subintervals has error

$$|E| = \left|\frac{(b - a)h^2}{12}f''(\xi)\right| \le \frac{(b-a)h^2}{12}\max_{[a,b]}|f''|$$

**Compute $f''$ and its maximum.** With $f(x) = \sqrt{1 + x^2}$,

$$f'(x) = \frac{x}{\sqrt{1+x^2}}, \qquad f''(x) = \frac{1}{(1+x^2)^{3/2}}$$

This decreases as $x$ increases on $[0,1]$, so the maximum is at $x = 0$:

$$f''(0) = 1$$

**Solve the inequality.** With $a = 0$, $b = 1$:

$$\frac{h^2}{12} < 0.01 \implies h^2 < 0.12 \implies h < 0.3464$$

$$n = \frac{b-a}{h} > \frac{1}{0.3464} = 2.8868$$

$$\boxed{n = 3}$$

> [!note] Why the answer is the *smallest* integer that works
> The bound gives a sufficient condition, not a necessary one, so it is always
> safe to round the requirement *up*. Rounding down would be relying on the
> bound being loose, which is not a guarantee. Here $n = 3$ clears it and
> $n = 2$ does not, which the direct check below confirms.

> [!info] The direct check, which also shows the bound is not tight
> The exact value is available in closed form:
> $$\int_0^1\sqrt{1+x^2}\,dx = \left[\dfrac{x\sqrt{1+x^2}}{2} + \dfrac{\ln(x + \sqrt{1+x^2})}{2}\right]_0^1 = \frac{\sqrt2 + \ln(1+\sqrt2)}{2} = 1.1477936$$
>
> | $n$ | $h$ | Approximation | Error |
| :--: | :--: | :-- | :-- |
| 2 | 0.50 | 1.1625704 | $0.014777$ |
| 3 | 0.3333 | 1.1543499 | $0.006556$ |
>
> At $n = 2$ the error exceeds $0.01$ and at $n = 3$ it falls below, so the
> answer is confirmed rather than merely bounded. The bound itself is also
> consistent: at $n = 3$, $h = 1/3$, so $\dfrac{h^2}{12} = \dfrac{1}{108} =
> 0.009259$, and the actual error $0.006556$ is below it, as it must be.

---

## Question 7

### **(a) Solve $\frac{dy}{dx} = 1 - y$ with the initial condition $x = 0, y = 0$ by using modified Euler's method. Tabulate the solutions at $x = 0.1, 0.2, 0.3$.**

*[Marks: 06]*

**The method.** Modified Euler is two stages. The predictor takes one plain
Euler step,

$$\hat y_1 = y_n + hf(x_n, y_n)$$

and the corrector replaces the slope at the start of the step by the average of
the slope there and the slope at the predicted end point:

$$y_{n+1} = y_n + \frac{h}{2}\left[f(x_n, y_n) + f(x_{n+1}, \hat y_1)\right]$$

**Step 1.** $x_0 = 0$, $y_0 = 0$, $h = 0.1$, $f(x,y) = 1 - y$.

$$f(x_0, y_0) = 1, \qquad \hat y_1 = 0 + 0.1(1) = 0.1$$

$$f(x_1, \hat y_1) = 1 - 0.1 = 0.9, \qquad y_1 = 0 + \frac{0.1}{2}(1 + 0.9) = 0.095$$

**Step 2.** $x_1 = 0.1$, $y_1 = 0.095$.

$$f(x_1, y_1) = 0.905, \qquad \hat y_2 = 0.095 + 0.1(0.905) = 0.1855$$

$$f(x_2, \hat y_2) = 0.8145, \qquad y_2 = 0.095 + 0.05(0.905 + 0.8145) = 0.180975$$

**Step 3.** $x_2 = 0.2$, $y_2 = 0.180975$.

$$f(x_2, y_2) = 0.819025, \qquad \hat y_3 = 0.180975 + 0.1(0.819025) = 0.2628775$$

$$f(x_3, \hat y_3) = 0.7371225, \qquad y_3 = 0.180975 + 0.05(0.819025 + 0.7371225) = 0.2587824$$

**The tabulated solutions.**

| $x$ | $y$ |
| :--: | :-- |
| 0.1 | $0.0950000$ |
| 0.2 | $0.1809750$ |
| 0.3 | $0.2587824$ |

$$\boxed{y(0.1) = 0.095, \qquad y(0.2) = 0.181, \qquad y(0.3) = 0.259}$$

> [!info] Checking against the exact solution
> The equation is separable: $\dfrac{dy}{1-y} = dx$ gives
> $\ln|1-y| = -x + C$, and $y(0) = 0$ gives $C = 0$, so $y = 1 - e^{-x}$. The
> exact values at $x = 0.1, 0.2, 0.3$ are $0.0951626$, $0.1812692$ and
> $0.2591818$.
>
> The computed values are low by $1.6\times10^{-4}$, $2.9\times10^{-4}$ and
> $4.0\times10^{-4}$. Three things about that pattern are worth noticing. The
> errors all have the same sign, which is what a one-sided method does. They
> *grow* with $x$, which is expected, because with $h$ fixed the local error is
> fixed and the global error is the sum of the local errors over the steps
> taken. And they grow roughly linearly in $x$, the ratio of successive errors
> being very close to one, which says the effective order is two and the
> effective constant is small at this step size.
>
> The comparison that really tests the method is against plain Euler, whose
> values are $0.1$, $0.19$ and $0.271$ with errors $4.84\times10^{-3}$,
> $8.73\times10^{-3}$ and $1.18\times10^{-2}$. The modification has cut the
> error by about thirty times. If your own answer is only a factor of two or
> three better than plain Euler, you have applied the predictor and forgotten
> the corrector.

---

### **(b) Use the Runge-Kutta method to solve $10\frac{dy}{dx} = x^2 - y^2, \, y(0) = 1$ for the interval $0 < x \le 0.4$ with $h = 0.1$.**

*[Marks: 06]*

**Put the equation in standard form first.**

$$\frac{dy}{dx} = \frac{x^2 - y^2}{10}, \qquad y(0) = 1$$

so $f(x, y) = \dfrac{x^2 - y^2}{10}$. Students lose marks here by leaving the
$10$ inside $f$ and then forgetting to multiply by $h$ consistently.

**Fourth-order Runge-Kutta.** With $h = 0.1$,

$$k_1 = f(x_n, y_n), \qquad k_2 = f\left(x_n + \frac{h}{2}, y_n + \frac{h}{2}k_1\right)$$

$$k_3 = f\left(x_n + \frac{h}{2}, y_n + \frac{h}{2}k_2\right), \qquad k_4 = f(x_n + h, y_n + hk_3)$$

$$y_{n+1} = y_n + \frac{h}{6}(k_1 + 2k_2 + 2k_3 + k_4)$$

Note the pattern: $k_1$ and $k_4$ use $h$, the midpoints $k_2$ and $k_3$ use
$h/2$, and the combination weights are $1, 2, 2, 1$.

**Step 1.** $x_0 = 0$, $y_0 = 1$, $h/2 = 0.05$.

$$k_1 = \frac{0^2 - 1^2}{10} = -0.1$$

$$k_2 = \frac{(0.05)^2 - \left(1 + 0.05(-0.1)\right)^2}{10} = \frac{0.0025 - (0.995)^2}{10} = \frac{0.0025 - 0.990025}{10} = -0.0987525$$

$$k_3 = \frac{(0.05)^2 - \left(1 + 0.05(-0.0987525)\right)^2}{10} = \frac{0.0025 - (0.99506238)^2}{10} = \frac{0.0025 - 0.99014913}{10} = -0.09876491$$

$$k_4 = \frac{(0.1)^2 - \left(1 + 0.1(-0.09876491)\right)^2}{10} = \frac{0.01 - (0.99012351)^2}{10} = \frac{0.01 - 0.98034456}{10} = -0.09703446$$

$$y_1 = 1 + \frac{0.1}{6}\left(-0.1 + 2(-0.0987525) + 2(-0.09876491) + (-0.09703446)\right)$$

$$y_1 = 1 + 0.0166667(-0.59206928) = 0.9901322$$

**Steps 2 to 4**, the same procedure applied successively:

| Step | $x_n$ | $y_n$ | $k_1$ | $k_2$ | $k_3$ | $k_4$ | $y_{n+1}$ |
| :--: | :--: | :-- | :-- | :-- | :-- | :-- | :-- |
| 1 | 0.0 | 1.0000000 | $-0.1000000$ | $-0.0987525$ | $-0.0987649$ | $-0.0970345$ | $0.9901322$ |
| 2 | 0.1 | 0.9901322 | $-0.0970362$ | $-0.0948277$ | $-0.0948495$ | $-0.0921669$ | $0.9806562$ |
| 3 | 0.2 | 0.9806562 | $-0.0921687$ | $-0.0890169$ | $-0.0890477$ | $-0.0854301$ | $0.9717608$ |
| 4 | 0.3 | 0.9717608 | $-0.0854319$ | $-0.0813535$ | $-0.0813930$ | $-0.0768566$ | $0.9636311$ |

$$\boxed{y(0.4) = 0.9636}$$

**Full tabulation.**

| $x$ | $y$ |
| :--: | :-- |
| 0.1 | $0.9901322$ |
| 0.2 | $0.9806562$ |
| 0.3 | $0.9717608$ |
| 0.4 | $0.9636311$ |

> [!warning] The identity that keeps the table honest
> Every $k_1$ in that table is $f(x_n, y_n) = (x_n^2 - y_n^2)/10$ evaluated at
> the $x_n$ and $y_n$ printed in the same row. So at step 2,
> $k_1 = (0.1^2 - 0.9901322^2)/10 = (0.01 - 0.9803618)/10 = -0.0970362$,
> and at step 4,
> $k_1 = (0.3^2 - 0.9717608^2)/10 = (0.09 - 0.9443191)/10 = -0.0854319$.
> If a printed $k_1$ column disagrees with its own row, the $y$ column and the
> $k$ column have come from different runs, and one of them is wrong. Checking
> row 4 by hand is a fifteen-second test.
>
> Notice also that $y$ is *falling* while $f$ is negative throughout. That is
> not a contradiction: $y^2$ exceeds $x^2$ over this whole interval, so
> $f < 0$ and $y$ decreases, and as $y$ decreases towards $1$, $y^2$ decreases
> too, so $f$ becomes less negative. Both facts must hold at once, and the
> $k_1$ column drifting upwards from $-0.1000$ to $-0.0854$ shows exactly that.

> [!info] Step-size study, and what it does and does not prove
> | step size | steps | $y(0.4)$ |
| :--: | :--: | --: |
| 0.2 | 2 | 0.963631064 |
| 0.1 | 4 | 0.963631060 |
| 0.05 | 8 | 0.963631060 |
| 0.025 | 16 | 0.963631060 |
>
> The three step sizes agree to nine digits, and the differences between them,
> $4.3\times10^{-9}$ from $h = 0.2$ to $h = 0.1$ and $2.5\times10^{-10}$ from
> $h = 0.1$ to $h = 0.05$, fall by a factor of about sixteen on each halving of
> $h$. That factor of sixteen is the signature of a fourth-order method, and it
> confirms what remains is truncation error of the right order.
>
> It is worth being clear about what this does *not* show. The error here is
> genuinely tiny, on the order of $10^{-9}$, because the right-hand side is
> smooth and $y$ varies by less than $4\%$ across the interval. It is not tiny
> because of rounding. Students often read "the answer stops changing when I
> halve $h$" as "we are at the limit of double precision"; here the limit is
> about $10^{-16}$, three orders of magnitude below the residual, and refining
> $h$ further would keep improving the answer.
>
> A step-count check confirms the total: four steps of $h = 0.1$ reach $x = 0.4$
> exactly, and the question asks for $0 < x \le 0.4$, so the table is complete.

---

## Question 8

### **(a) Find the potential distribution at the interior nodes using Leibmann's method.**

*[Marks: 06]*

**The mesh.**

```text
                  Insulating Gap             V = 100 V            Insulating Gap
                                \                                 /
                         (0,3)   +-----------+-----------+-------+   (3,3)
                                 |           |           |       |
                         (0,2)   +-----------①-----------②-------+   (3,2)
                                 |        (Node 1)    (Node 2)   |
                       V = 75 V  |           |           |       |  V = 50 V
                         (0,1)   +-----------③-----------④-------+   (3,1)
                                 |        (Node 3)    (Node 4)   |
                                 |           |           |       |
                         (0,0)   +-----------+-----------+-------+   (3,0)
                                /                                 \
                  Insulating Gap              V = 0 V             Insulating Gap
```

**The governing equation.** With no charge or source inside the region, the
potential satisfies Laplace's equation, whose five-point finite-difference form
on a uniform square mesh is

$$u_{i,j} = \frac{1}{4}\left(u_{i+1,j} + u_{i-1,j} + u_{i,j+1} + u_{i,j-1}\right)$$

Four neighbours, four weights, all $1/4$. That symmetry is why this is called
the five-point stencil: the centre plus its four edge neighbours.

**Leibmann's method is Gauss-Seidel on this system.** Update each node from the
most recent values of its neighbours, as soon as those are available, rather
than from the previous sweep.

**The four node equations.** This is where the question is won or lost. Read
each node's four neighbours off the diagram, boundary values included:

$$V_1 = \frac{100 + V_2 + 75 + V_3}{4} = \frac{175 + V_2 + V_3}{4}$$

$$V_2 = \frac{100 + 50 + V_1 + V_4}{4} = \frac{150 + V_1 + V_4}{4}$$

$$V_3 = \frac{75 + V_4 + V_1 + 0}{4} = \frac{75 + V_1 + V_4}{4}$$

$$V_4 = \frac{V_3 + 50 + V_2 + 0}{4} = \frac{50 + V_2 + V_3}{4}$$

As a $4\times4$ system,

$$\begin{bmatrix} 4 & -1 & -1 & 0 \\ -1 & 4 & 0 & -1 \\ -1 & 0 & 4 & -1 \\ 0 & -1 & -1 & 4 \end{bmatrix}\begin{bmatrix} V_1 \\ V_2 \\ V_3 \\ V_4 \end{bmatrix} = \begin{bmatrix} 175 \\ 150 \\ 75 \\ 50 \end{bmatrix}$$

> [!warning] Counting off-diagonal entries catches a wrong neighbour
> Look at the matrix before you look at the answer. Each row of a five-point
> stencil row has one diagonal and **exactly two** off-diagonal entries. Here
> rows 1 to 4 carry $-1$ in columns two and three, two and four, one and four,
> and two and three respectively: two each. If you find three $-1$s in a row,
> you have put a diagonal neighbour in where an off-diagonal one belongs.
>
> A second test is to add all four equations. Every interior neighbour appears
> once with $+1$ and once with $-1$, so the interior terms cancel and what
> remains is $2(V_1+V_2+V_3+V_4) = 175 + 150 + 75 + 50 = 450$, giving
> $V_1+V_2+V_3+V_4 = 225$. The stated answer gives
> $71.875 + 65.625 + 46.875 + 40.625 = 225$ exactly, so the neighbour sets are
> mutually consistent. One line, and it catches a transposed pair of neighbours
> immediately.

**Leibmann iteration.** Starting from $V_1 = V_2 = V_3 = V_4 = 0$, and
updating in the order $1, 2, 3, 4$ so each node uses the freshest neighbours
available:

| Sweep | $V_1$ | $V_2$ | $V_3$ | $V_4$ |
| :--: | :--: | :--: | :--: | :--: |
| 1 | 43.750000 | 48.437500 | 29.687500 | 32.031250 |
| 2 | 63.281250 | 61.328125 | 42.578125 | 38.476562 |
| 3 | 69.726562 | 64.550781 | 45.800781 | 40.087891 |
| 4 | 71.337891 | 65.356445 | 46.606445 | 40.490723 |
| 5 | 71.740723 | 65.557861 | 46.807861 | 40.591431 |
| 6 | 71.841431 | 65.608215 | 46.858215 | 40.616608 |

**The solution.** The iteration converges, and solving the $4\times4$ system
directly gives

$$V_1 = \frac{575}{8} = 71.875, \qquad V_2 = \frac{525}{8} = 65.625$$

$$V_3 = \frac{375}{8} = 46.875, \qquad V_4 = \frac{325}{8} = 40.625$$

$$\boxed{V_1 = 71.875\ \text{V}, \quad V_2 = 65.625\ \text{V}, \quad V_3 = 46.875\ \text{V}, \quad V_4 = 40.625\ \text{V}}$$

> [!info] Checking by substitution, and what the fractions tell you
> Substitute back into the four stencil equations:
> $\dfrac{1}{4}(175 + 65.625 + 46.875) = \dfrac{287.5}{4} = 71.875$;
> $\dfrac{1}{4}(150 + 71.875 + 40.625) = \dfrac{262.5}{4} = 65.625$;
> $\dfrac{1}{4}(75 + 71.875 + 40.625) = \dfrac{187.5}{4} = 46.875$;
> $\dfrac{1}{4}(50 + 65.625 + 46.875) = \dfrac{162.5}{4} = 40.625$. All four hold
> exactly.
>
> The answer coming out as multiples of $\tfrac18$ is itself informative. The
> boundary data are multiples of $25$, and one sweep of the averaging process
> can only produce multiples of $\tfrac14$, so a multiple of $\tfrac18$ at the
> fixed point is a sign that the system is self-consistent. A wrong neighbour
> would leave a residual of order a tenth rather than zero, and the values
> would not settle on tidy fractions.
>
> On the convergence itself: all four nodes approach their limits from below,
> which is what a Gauss-Seidel start at the origin gives when every
> right-hand side is positive. The increments in $V_1$ over the first six sweeps
> are $43.7500$, $19.5313$, $6.4453$, $1.6113$, $0.4028$ and $0.1007$, so after
> the first sweep each increment is a fixed fraction, about one quarter, of the
> one before. That factor of four per sweep is the signature of a spectral
> radius near $0.25$. Six sweeps leave $V_1$ within $0.034$ V of its limit, so
> more sweeps would be needed for four-figure agreement; that is the honest
> reason an exact elimination is reported alongside the iteration.

---

### **(b) Use the Euler's method to solve, $\frac{d^2 y}{dt^2} - 0.5t = y$ where, $y(0) = 2$ and $y'(0) = 0$. Solve from $t = 0$ to $0.4$ using $h = 0.1$.**

*[Marks: 06]*

**Step 1, reduce to a first-order system.** Rearranging,

$$\frac{d^2y}{dt^2} = y + 0.5t$$

Introduce $v = \dfrac{dy}{dt}$, giving

$$\frac{dy}{dt} = v, \qquad \frac{dv}{dt} = y + 0.5t$$

with $y(0) = 2$ and $v(0) = 0$.

> [!warning] The one slip that ruins this question
> The equation is written as $\ddot y - 0.5t = y$, so $\ddot y = y + 0.5t$ and
> the $+0.5t$ goes on the **right**-hand side with a plus sign. Students who
> read "$-0.5t$" as the sign of the term in $\ddot y$ write $\ddot y = y -
> 0.5t$, and the whole table is then wrong while looking perfectly reasonable.
> Move the term across before writing anything else.

**Step 2, apply Euler to both equations at once**, using the *old* values on
the right:

$$y_{n+1} = y_n + h\,v_n, \qquad v_{n+1} = v_n + h\,(y_n + 0.5t_n)$$

**Step 1.** $t_0 = 0$, $y_0 = 2$, $v_0 = 0$.

$$y_1 = 2 + 0.1(0) = 2.0, \qquad v_1 = 0 + 0.1(2 + 0) = 0.2$$

**Step 2.** $t_1 = 0.1$, $y_1 = 2.0$, $v_1 = 0.2$.

$$y_2 = 2.0 + 0.1(0.2) = 2.02, \qquad v_2 = 0.2 + 0.1(2.0 + 0.05) = 0.405$$

**Step 3.** $t_2 = 0.2$, $y_2 = 2.02$, $v_2 = 0.405$.

$$y_3 = 2.02 + 0.1(0.405) = 2.0605, \qquad v_3 = 0.405 + 0.1(2.02 + 0.1) = 0.617$$

**Step 4.** $t_3 = 0.3$, $y_3 = 2.0605$, $v_3 = 0.617$.

$$y_4 = 2.0605 + 0.1(0.617) = 2.1222, \qquad v_4 = 0.617 + 0.1(2.0605 + 0.15) = 0.83805$$

**The results.**

| $t$ | $y$ | $v = y'$ |
| :--: | :--: | :--: |
| 0.0 | 2.0000 | 0.0000 |
| 0.1 | 2.0000 | 0.20000 |
| 0.2 | 2.0200 | 0.40500 |
| 0.3 | 2.0605 | 0.61700 |
| 0.4 | 2.1222 | 0.83805 |

$$\boxed{y(0.4) = 2.1222}$$

> [!note] Why $y$ does not move on the first step
> $y_1 = y_0 + h v_0 = 2 + 0.1(0) = 2$, because $v_0 = 0$. The velocity
> starts at rest, so the position cannot change on the first step no matter how
> large the acceleration is. $v_1 = 0.2$ records that the acceleration is
> $2$ and $h$ is $0.1$. A table that shows $y$ changing on the first row has
> used $v_1$ instead of $v_0$, which is the standard off-by-one in this pair of
> recursions.

> [!info] The exact solution is available here, so use it
> $\ddot y = y + \tfrac12 t$ rearranges to $\ddot y - y = \tfrac12 t$, whose
> homogeneous solution is $C_1 e^{-t} + C_2 e^{t}$ and whose particular solution
> is $-\tfrac12 t$. The initial conditions give $C_1 + C_2 = 2$ and
> $-C_1 + C_2 = 0.5$ (from $y'(0) = -C_1 + C_2 - 0.5 = 0$, giving $C_1 = 0.75, C_2 = 1.25$),
> so $y = 2\cosh t + \tfrac12\sinh t - \tfrac12 t$, and at $t = 0.4$
> $y(0.4) = 2.167521$. The Euler value $2.1222$ is low by $0.0453$, about $2.1\%$.
>
> To see that this is truncation error and not a slip, halve the step. With
> $h = 0.05$ over eight steps, $y(0.4) = 2.144385$; with $h = 0.025$ over
> sixteen steps, $y(0.4) = 2.155822$. The successive gains are $0.022$ and
> $0.011$, in the ratio $2:1$ that an $O(h)$ error requires. An arithmetic slip
> would not shrink when the step is halved.
>
> The same value can be reached from the other direction, without solving the
> ODE. Differentiating $\ddot y = y + \tfrac12 t$ repeatedly gives
> $y''(0) = 2$, $y'''(0) = y'(0) + \tfrac12 = 0.5$ and
> $y^{(4)} = y''$, so $y^{(4)}(0) = y(0) = 2$. The four-term series at $t = 0.4$
> is $2 + 0.16 + \frac{0.5}{6}(0.064) + \frac{2}{24}(0.0256) = 2 + 0.16 +
> 0.005333 + 0.002133 = 2.16747$, within $5\times10^{-5}$ of the exact value.
> The series and the closed form agreeing is a check on both.

---