---
title: "ECE 2213 · 2023 Explanations"
tags:
  - numerical-methods
  - discrete-mathematics
  - previous-year
---

# ECE 2213: 2023 Semester Final · Explained

**RUET · ECE Dept · B.Sc. Engineering 2nd Year Even Semester Examination, 2023**

This file explains the same questions as
[[2023_answer|the 2023 answer script]], written to be read
rather than copied. Every step is named, the reason a formula is chosen is
stated, and the traps that catch people are called out.

> [!info] How to use this file
> Read this to understand *why* the answer script does what it does. When you
> are ready to write in the hall, work from
> [[2023_answer|the exam-style file]], which is shorter and
> carries no commentary.
>
> **The rule that matters.** Every boxed number here is the same number as the
> one in the answer script, character for character. Gate V5 checks this. If the
> answer script says `0.2876820735`, so does this file.

> [!note] What this paper is made of
> The 2023 paper is the first in this set that carries CLO labels, and it is the
> first with a clean split: Questions 1 to 4 are numerical methods, Questions 5
> to 8 are discrete mathematics. Section A and Section B are not just a layout
> convenience, they are the two halves of the syllabus sitting side by side.
>
> One thing to notice before you start. **Three questions in this paper are
> incomplete as printed**, and all three are numerical:
>
> | Where | What is missing |
> | :-- | :-- |
> | Q.2(a) | the nodes the formula is evaluated at |
> | Q.3(b) | the step size $h$ and the target interval, for both parts |
> | Q.4(b) | nothing, but $h$ must be chosen, since $n = 11$ is odd |
>
> A question that does not state $h$ is still fully answerable: you choose a
> value, you state it, and you get the marks. What loses marks is producing
> numbers without ever saying which $h$ produced them.

---

# SECTION A

## Question 1

### **(a) Explain the differences between analytical and numerical solution; also describe the significance of numerical analysis in engineering field.**

*[Marks: 04, CO: 1]*

An analytical solution is one where you manipulate symbols until the unknown
appears on its own, and the answer is valid at every point of the domain. A
numerical solution is one where you approximate the problem by something you
can evaluate, and the answer is a number valid near the point you evaluated it
at.

**The distinction that actually matters.** An analytical answer is a *rule*; a
numerical answer is a *reading*. If the answer is $y = 3x^2 + 1$, you can
evaluate it anywhere without computing anything new. If the answer is
$y(2.5) = 19.75$, that one number is all you have, and getting $y(3)$ means
starting again.

**Side by side.**

| | Analytical | Numerical |
| :-- | :-- | :-- |
| Result | Closed form, exact | Approximate |
| Domain | Whole domain | Local, near one point |
| Difficulty of problem | May be impossible | Grows slowly with size |
| Cost per answer | Fixed once derived | Grows with problem size |
| Round off error | None | Present |
| Typical size | Thousands of equations | Millions |

**The differences, stated as points.**

1. **Form.** Analytic gives $y = f(x)$ in symbols. Numeric gives a table of
   values or one point $y(x_0)$.
2. **Accuracy.** Analytic is exact. Numeric carries both truncation error, from
   the approximation itself, and round off error, from finite precision. A good
   method reports a bound on their sum, which is the part that distinguishes
   engineering practice from guesswork.
3. **Problem size.** Analytic solutions exist for a handful of textbook
   equations. Real systems give equations nobody can solve in symbols, and that
   is exactly where numeric methods begin.
4. **Changing the data.** Analytic re-evaluates instantly. Numeric must be run
   again from the start.
5. **Understanding.** Analytic reveals structure, such as a conservation law or
   a resonance condition. Numeric hides it.

**Why numerical analysis matters in engineering.** Six reasons, and the marks
are usually spread across them.

1. **It makes unsolvable problems solvable.** Most real systems have no closed
   form: a coupled circuit, a fluid flow, a heat-transfer body, a structural
   frame. These are not hard problems, they are problems whose closed form
   nobody has written down.
2. **It replaces an expensive experiment.** A structural analysis or a CFD run
   costs a fraction of a physical test and can be repeated at any parameter
   setting. It is also the only option when the real thing cannot be built,
   because it would be dangerous or too expensive.
3. **It handles irregular data.** Measurements arrive unevenly spaced and noisy.
   Interpolation and least squares fit them without demanding a functional form
   in advance.
4. **It supports design iteration.** Optimisation needs hundreds or thousands of
   evaluations, each one a numerical solve. An analytical solution would be
   faster per evaluation but frequently does not exist.
5. **It quantifies its own trust.** Every method carries an error bound, so the
   engineer knows how far to believe the answer. This is the difference between
   a method and a guess.
6. **It is cheap in time and memory**, which is why it is used before the
   hardware exists.

$$
\boxed{\text{Analytical is exact and general; numerical is approximate, local, and reaches further}}
$$

> [!note] How four marks are usually split
> Two for the differences and two for the significance, so four clean
> differences and four significance points with one sentence each is the target.
> Writing a long paragraph on analytical versus numerical and then one sentence
> on significance will lose the second half.
>
> The word *general* in the boxed line is doing real work. Analytical solutions
> are exact *and* global; numerical ones are local by construction. That is the
> single sharpest difference and it is worth stating explicitly.

---

### **(b) Given that $u = \frac{5xy^2}{z^3}$, find the relative error at $x = y = z = 1$ when the errors in each of $x, y, z$ is $0.001$.**

*[Marks: 03, CO: 2]*

This question deals with error propagation. In numerical analysis, errors in measured quantities can be treated in two standard ways:

---

### **Interpretation 1: Maximum Relative Error (Standard Textbook / Worst-Case Bound)**

In engineering and numerical analysis textbooks (e.g., S. S. Sastry, B. S. Grewal), an "error of $0.001$" in a measured variable represents an uncertainty bound:
$$|\Delta x| \le 0.001, \quad |\Delta y| \le 0.001, \quad |\Delta z| \le 0.001$$

The exact value at $x = y = z = 1$ is:
$$u = \frac{5(1)(1)^2}{1^3} = 5$$

Taking natural logarithms of $u = \frac{5xy^2}{z^3}$:
$$\ln u = \ln 5 + \ln x + 2\ln y - 3\ln z$$

Differentiating gives the relation between relative errors:
$$\frac{du}{u} = \frac{dx}{x} + 2\frac{dy}{y} - 3\frac{dz}{z}$$

To find the **maximum possible relative error**, we take absolute values of each component (since errors in different measurements can have opposing signs and conspire to produce the worst-case error bound):

$$(e_r)_{\max} = \left|\frac{\Delta u}{u}\right|_{\max} \approx \left|\frac{\Delta x}{x}\right| + 2\left|\frac{\Delta y}{y}\right| + 3\left|\frac{\Delta z}{z}\right|$$

Substituting $x = y = z = 1$ and $|\Delta x| = |\Delta y| = |\Delta z| = 0.001$:

$$(e_r)_{\max} = \frac{0.001}{1} + 2\left(\frac{0.001}{1}\right) + 3\left(\frac{0.001}{1}\right) = (1 + 2 + 3)(0.001) = 0.006 \quad (0.6\%)$$

The maximum absolute error is:
$$(\Delta u)_{\max} = |u| \cdot (e_r)_{\max} = 5 \times 0.006 = 0.030$$

$$
\boxed{(e_r)_{\max} = 0.006 \quad (0.6\%), \qquad (\Delta u)_{\max} = 0.030}
$$

---

### **Interpretation 2: Algebraic Perturbation (Identical Signs $\Delta x = \Delta y = \Delta z = +0.001$)**

If the errors are taken as signed algebraic increments that happen to be identical in both magnitude and sign:

$$u_p = \frac{5(1.001)(1.001)^2}{(1.001)^3} = \frac{5(1.001)^3}{(1.001)^3} = 5$$

$$\Delta u = u_p - u = 5 - 5 = 0 \quad\implies\quad e_r = 0$$

$$
\boxed{e_r = 0 \quad (\text{if signs are identically } +0.001)}
$$

> [!warning] The zero is structural, not a rounding coincidence
> The algebraic answer is zero because the powers of $(1 + 0.001)$ cancel:
> $(1.001)^1 \cdot (1.001)^2 \cdot (1.001)^{-3} = (1.001)^{1 + 2 - 3} = (1.001)^0 = 1$.
> The function is **homogeneous of degree zero** in $(x, y, z)$. Scaling all three inputs by the same factor leaves $u$ unchanged.
> However, an engineer cannot assume errors will conveniently cancel in sign, which is why the maximum relative error bound $(e_r)_{\max} = 0.006$ is the primary concept taught in numerical methods courses. Providing both interpretations ensures full credit in any exam setting.

---

### **(c) Derive the formula for root finding using Newton-Raphson method. Also, discuss the problems of it and how this problem can be solved.**

*[Marks: 03, CO: 1]*

Newton-Raphson is built on one idea: draw the tangent to the curve at your
current guess and see where it cuts the axis. Because the tangent touches the
curve, it tracks the curve closely near the root, so the intercept is a much
better guess than the current point.

**The derivation.** Let the root of $f(x) = 0$ be $x^*$. Start at $x_0$ and move
along the tangent to the curve at that point. The tangent at $x_0$ is

$$
f(x_0) + f'(x_0)(x - x_0)
$$

Set it to zero to find where the tangent meets the axis:

$$
f(x_0) + f'(x_0)(x_1 - x_0) = 0 \quad\Longrightarrow\quad x_1 = x_0 - \frac{f(x_0)}{f'(x_0)}
$$

Equivalently, and this is the form usually derived: let $x^* = x_0 + h$, so the
tangent crosses at $x_0 + h$. By the first-order mean value form of Taylor,

$$
0 = f(x^*) = f(x_0 + h) \approx f(x_0) + h f'(x_0)
$$

which gives $h = -\frac{f(x_0)}{f'(x_0)}$ and the same iteration. Repeating:

$$
\boxed{x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}}
$$

If $f'$ is not available in closed form, write
$f'(x_n) = \lim_{h \to 0}\frac{f(x_n + h) - f(x_n)}{h}$, which is the origin of
the secant method.

**Why it converges so fast.** Keep the second-order Taylor term:

$$
f(x^*) = 0 = f(x_n) + f'(x_n)\Delta x + \frac{f''(\xi)}{2}\Delta x^2
$$

Substituting $\Delta x = -\frac{f}{f'}$ shows the error satisfies
$e_{n+1} \approx \frac{f''(x^*)}{2f'(x^*)}e_n^2$. The error is **squared** at
every step. From six correct digits you get twelve, from twelve you get
twenty-four. That doubling of the digit count for one extra derivative
evaluation is why Newton-Raphson is the default root finder.

**The problems, and what fixes each.**

| Problem | Cause | Fix |
| :-- | :-- | :-- |
| Diverges or oscillates | Initial guess too far, or $f'$ small | Bracket the root first and start inside, or use bisection |
| Division by zero | $f'(x_n) = 0$, a stationary point | Choose another start, or use a method that does not divide by $f'$ |
| Cycle between two points | Overshoot from a bad start | Damp the step, or switch to bisection when two successive values repeat |
| False convergence | $f(x_n) \ne 0$ but $f'(x_n) = 0$ | Always check $\lvert f(x_n)\rvert$, not only $\lvert x_{n+1} - x_n\rvert$ |
| Slow near a repeated root | Squaring holds only for a **simple** root | Use $x_{n+1} = x_n - m\frac{f(x_n)}{f'(x_n)}$ with $m$ the multiplicity |
| No convergence on a step-like function | No tangent information, as on a signum | Bisection, which needs only a sign change |
| $f'$ unavailable | Only a formula for $f$ | Secant, which builds the derivative from two points |

> [!warning] The failure that actually bites
> The dangerous case is **false convergence at a stationary point**. Take
> $f(x) = x^3 - 2x^2 + x = x(x-1)^2$. It has roots at $0$ and at $1$, where $1$ is
> a double root, so $f'(1) = 0$. Starting near $1$, Newton-Raphson divides by a
> very small derivative, the step explodes, and the iteration can bounce away
> and come back. Meanwhile $\lvert x_{n+1} - x_n\rvert$ looks unremarkable.
>
> The lesson is that **convergence is $\lvert f(x_n) \rvert \to 0$, not
> $\lvert \Delta x \rvert \to 0$**. Always evaluate the function at the final
> answer.

> [!info] The production fix: keep a bracket
> The safeguard that solves almost every entry in that table at once is to carry
> a bracket $[a, b]$ with $f(a)f(b) < 0$ alongside the Newton step. If the
> Newton step leaves the bracket, take a bisection step instead. This hybrid
> keeps Newton's quadratic convergence while inheriting bisection's guarantee
> of eventual convergence, and it is the form used in real root finders such as
> `scipy.optimize.brentq`.
>
> Part (a) of Question 2 asks for the same distinction in the interpolation
> setting, where the finite-difference Newton takes over.

---

## Question 2

### **(a) Derive the Newton's forward interpolation formula: $y_n(x) = y_0 + p\Delta y_0 + \frac{p(p-1)}{2!}\Delta^2 y_0 + \frac{p(p-1)(p-2)}{3!}\Delta^3 y_0 + \cdots$**

*[Marks: 04, CO: 3]*

**The setup.** Let $y = f(x)$ be given at $n + 1$ equally spaced points:
$$x_0, x_1 = x_0 + h, x_2 = x_0 + 2h, \dots, x_n = x_0 + nh$$
with common spacing $h$ and values $y_0, y_1, y_2, \dots, y_n$.

Write any point in the domain as:
$$x = x_0 + ph \quad\Longrightarrow\quad p = \frac{x - x_0}{h}$$
where $p$ is the dimensionless parameter measuring distance from $x_0$ in units of $h$.

**Step 1. Newton's interpolating polynomial form.**
We assume the interpolating polynomial $P_n(x)$ of degree $n$ in factorial powers of $(x - x_0)$:

$$
P_n(x) = a_0 + a_1(x - x_0) + a_2(x - x_0)(x - x_1) + a_3(x - x_0)(x - x_1)(x - x_2) + \cdots + a_n(x - x_0)(x - x_1)\cdots(x - x_{n-1})
$$

where $a_0, a_1, \dots, a_n$ are constant coefficients to be determined so that $P_n(x_i) = y_i$ for all $i = 0, 1, \dots, n$.

**Step 2. Determine coefficients successively.**
Because each factor $(x - x_k)$ vanishes at all subsequent interpolation nodes, the coefficients decouple cleanly:

1. **At $x = x_0$:**
   All terms after $a_0$ vanish:
   $$P_n(x_0) = a_0 = y_0 \implies a_0 = y_0$$

2. **At $x = x_1 = x_0 + h$:**
   $$P_n(x_1) = a_0 + a_1(x_1 - x_0) = y_0 + a_1 h = y_1$$
   $$a_1 = \frac{y_1 - y_0}{h} = \frac{\Delta y_0}{1!\,h}$$

3. **At $x = x_2 = x_0 + 2h$:**
   $$P_n(x_2) = a_0 + a_1(2h) + a_2(2h)(h) = y_2$$
   $$y_0 + 2\Delta y_0 + 2h^2 a_2 = y_2$$
   $$2h^2 a_2 = y_2 - 2y_1 + y_0 = \Delta^2 y_0 \implies a_2 = \frac{\Delta^2 y_0}{2!\,h^2}$$

4. **By induction for any $k \le n$:**
   $$a_k = \frac{\Delta^k y_0}{k!\,h^k}$$

**Step 3. Change variable to $p = \frac{x - x_0}{h}$.**
Express each product of factors in terms of $p$:
- $x - x_0 = ph$
- $x - x_1 = ph - h = (p - 1)h$
- $x - x_2 = ph - 2h = (p - 2)h$
- $(x - x_0)(x - x_1)\cdots(x - x_{k-1}) = p(p - 1)\cdots(p - k + 1)h^k$

Substitute $a_k$ and the factor product into the $k$-th term of $P_n(x)$:

$$
a_k(x - x_0)(x - x_1)\cdots(x - x_{k-1}) = \frac{\Delta^k y_0}{k!\,h^k} \cdot \left[p(p - 1)\cdots(p - k + 1)h^k\right] = \frac{p(p - 1)\cdots(p - k + 1)}{k!} \Delta^k y_0
$$

**Step 4. The resulting formula.**
Summing all terms yields Newton's Forward Interpolation formula:

$$
\boxed{y_n(x) = y_0 + p\Delta y_0 + \frac{p(p-1)}{2!} \Delta^2 y_0 + \frac{p(p-1)(p-2)}{3!} \Delta^3 y_0 + \cdots + \frac{p(p-1)\cdots(p-n+1)}{n!} \Delta^n y_0}
$$

> [!info] The operator derivation (Shift Operator $E$)
> A rapid second derivation uses the finite difference shift operator $E$:
> $$E = 1 + \Delta$$
> By definition, $E^p y_0 = y(x_0 + ph) = y(x)$.
> Expanding $(1 + \Delta)^p$ via the generalized binomial theorem:
> $$y(x) = (1 + \Delta)^p y_0 = \left[1 + p\Delta + \frac{p(p-1)}{2!}\Delta^2 + \frac{p(p-1)(p-2)}{3!}\Delta^3 + \cdots\right]y_0$$
> $$= y_0 + p\Delta y_0 + \frac{p(p-1)}{2!}\Delta^2 y_0 + \frac{p(p-1)(p-2)}{3!}\Delta^3 y_0 + \cdots$$
> This proves the identity purely through difference algebra.

> [!note] When this formula degenerates
> Forward differences need a **constant** $h$. Hand this question a table with
> gaps of $0.5$ and then $1.0$ and the formula is simply not applicable; you
> need divided differences, which is what Question 5(b) of the 2020 paper asks
> for. Equally spaced is the whole precondition.

---

### **(b) Find $y(2)$ from the following data using Lagrange's formula.**

*[Marks: 03, CO: 2]*

| $x$ | 0 | 1 | 3 | 4 | 5 |
| --- | --: | --: | --: | --: | --: |
| $y$ | 0 | 1 | 81 | 256 | 625 |

**Step 1. The formula.** With five points $x_0 = 0, x_1 = 1, x_2 = 3, x_3 = 4,
x_4 = 5$,

$$
y(2) = \sum_{i=0}^{4} y_i L_i(2), \qquad L_i(2) = \prod_{j \neq i} \frac{2 - x_j}{x_i - x_j}
$$

The $L_i$ are **basis polynomials**: each one is 1 at its own node and 0 at every
other node, so the combination reproduces all five data values exactly.

**Step 2. Compute each weight.** The thing that goes wrong here is signs. Keep
the numerator factors and denominator factors separate and count them, because
the denominator carries one negative sign per factor below $x_i$.

**Node 0, at $x = 0$.** All four denominator factors are negative, so the product
is positive.

$$
L_0(2) = \frac{(2-1)(2-3)(2-4)(2-5)}{(0-1)(0-3)(0-4)(0-5)} = \frac{(1)(-1)(-2)(-3)}{(-1)(-3)(-4)(-5)} = \frac{-6}{60} = -\frac{1}{10}
$$

**Node 1, at $x = 1$.** Two negative denominator factors here, so the product is
negative.

$$
L_1(2) = \frac{(2-0)(2-3)(2-4)(2-5)}{(1-0)(1-3)(1-4)(1-5)} = \frac{(2)(-1)(-2)(-3)}{(1)(-2)(-3)(-4)} = \frac{-12}{-24} = \frac{1}{2}
$$

**Node 2, at $x = 3$.** Two negative denominator factors again.

$$
L_2(2) = \frac{(2-0)(2-1)(2-4)(2-5)}{(3-0)(3-1)(3-4)(3-5)} = \frac{(2)(1)(-2)(-3)}{(3)(2)(-1)(-2)} = \frac{12}{12} = 1
$$

**Node 3, at $x = 4$.** One negative denominator factor, so negative.

$$
L_3(2) = \frac{(2-0)(2-1)(2-3)(2-5)}{(4-0)(4-1)(4-3)(4-5)} = \frac{(2)(1)(-1)(-3)}{(4)(3)(1)(-1)} = \frac{6}{-12} = -\frac{1}{2}
$$

**Node 4, at $x = 5$.** All four denominator factors positive.

$$
L_4(2) = \frac{(2-0)(2-1)(2-3)(2-4)}{(5-0)(5-1)(5-3)(5-4)} = \frac{(2)(1)(-1)(-2)}{(5)(4)(2)(1)} = \frac{4}{40} = \frac{1}{10}
$$

**Check the weights before using them.** They must sum to 1:

$$
-\frac{1}{10} + \frac{1}{2} + 1 - \frac{1}{2} + \frac{1}{10} = 1
$$

**Step 3. Assemble.**

$$
\begin{aligned}
y(2) &= (0)\left(-\tfrac{1}{10}\right) + (1)\left(\tfrac{1}{2}\right) + (81)(1) + (256)\left(-\tfrac{1}{2}\right) + (625)\left(\tfrac{1}{10}\right) \\
     &= 0 + 0.5 + 81 - 128 + 62.5 \\
     &= 16
\end{aligned}
$$

$$
\boxed{y(2) = 16}
$$

> [!warning] The weights are the whole computation
> Every digit of the answer comes from those five ratios. One wrong sign in one
> denominator gives a plausible-looking but wrong number, and the error does not
> announce itself. Two conditions catch it:
>
> 1. **The weights must sum to 1.** This holds at *any* $x$, not only at a node,
>    because interpolating the constant function $1$ with a degree 4 polynomial
>    must return $1$. If the sum is not 1, a weight is wrong. It is the single
>    most useful check in this topic.
> 2. **Count the factors.** Each $L_i$ has four numerator and four denominator
>    factors, since $j$ runs over the four indices other than $i$. A weight
>    written with three factors is wrong by construction and will not sum to 1.
>
> $L_0(2)$ and $L_1(2)$ are the two most often mis-signed: their denominators are
> $60$ and $-24$, not $-60$ and $24$.

> [!info] Two further routes, both cheap
> **Recognise the data.** Look at the $y$ column before computing anything:
> $0^4 = 0$, $1^4 = 1$, $3^4 = 81$, $4^4 = 256$, $5^4 = 625$. All five points lie
> on $y = x^4$ exactly, so $y(2) = 2^4 = 16$. This is not a trick, it is the
> habit worth building: always check whether the data have a closed form, because
> when they do it is the fastest route and the best check on the slow one.
>
> **Newton's divided difference.** The nodes $0, 1, 3, 4, 5$ are **not** equally
> spaced, so forward differences do not apply and divided differences must be
> used. The table is
>
> | Order | Values |
> | :-- | :-- |
> | $f[x_i]$ | 0, 1, 81, 256, 625 |
> | $f[x_i, x_{i+1}]$ | 1, 40, 175, 369 |
> | $f[x_i, x_{i+1}, x_{i+2}]$ | 13, 45, 97 |
> | $f[x_i, x_{i+1}, x_{i+2}, x_{i+3}]$ | 8, 13 |
> | $f[x_0,\ldots,x_4]$ | 1 |
>
> One entry verifies directly:
> $f[x_1,x_2,x_3] = \frac{f[x_2,x_3] - f[x_1,x_2]}{x_3 - x_1} = \frac{175 - 40}{4 - 1} = \frac{135}{3} = 45$.
> Newton's polynomial uses the leading diagonal $0, 1, 13, 8, 1$, and evaluating
> at $x = 2$ gives 16 as well.
>
> Lagrange, divided differences and the closed form all return 16, so the result
> does not depend on the route.

---

### **(c) Use Romberg's method to compute $\int_1^2 \frac{1}{2+x}\,dx$. Consider $h = 0.5, 0.25, 0.125$.**

*[Marks: 03, CO: 3]*

Romberg is repeated Richardson extrapolation. The idea is worth understanding
before the arithmetic, because it explains every number in the table.

**The mechanism.** The trapezoid rule on a grid of width $h$ has error
$\frac{(b-a)}{12}h^2f''(\xi) + O(h^4)$, so the error is proportional to $h^2$ to
leading order. Halving $h$ therefore divides the error by $4$. If you have two
grids, you can subtract off the $h^2$ part and cancel it exactly. Apply the
same trick to what is left, and the $h^4$ part cancels. Each column of the
Romberg table buys two more orders of accuracy.

**Step 1. The first column, composite trapezoid.** With $f(x) = \frac{1}{2+x}$,
$T_n = \frac{h}{2}\left[f_0 + 2f_1 + \cdots + 2f_{n-1} + f_n\right]$.

At $h = 0.5$ the nodes are $x = 1, 1.5, 2$:

$$
T_2 = \frac{0.5}{2}\left[\frac{1}{3} + 2\cdot\frac{1}{3.5} + \frac{1}{4}\right] = 0.25\left[0.333333 + 0.571429 + 0.25\right] = 0.2886904762
$$

At $h = 0.25$, $n = 4$:

$$
T_4 = \frac{0.25}{2}\left[\frac{1}{3} + 2\left(\frac{1}{3.25} + \frac{1}{3.5} + \frac{1}{3.75}\right) + \frac{1}{4}\right] = 0.2879349817
$$

At $h = 0.125$, $n = 8$:

$$
T_8 = 0.2877453510
$$

**Step 2. The second column, extrapolate to Simpson's rule.** Since the trapezoid
error goes as $h^2$, the factor is $4 - 1 = 3$:

$$
R_{k,1} = R_{k,0} + \frac{R_{k,0} - R_{k-1,0}}{4^1 - 1}
$$

| $k$ | $R_{k,0}$ (trapezoid) | $R_{k,1}$ (Simpson) |
| ---: | ---: | ---: |
| 1 | 0.2886904762 | |
| 2 | 0.2879349817 | 0.2876831502 |
| 3 | 0.2877453510 | 0.2876821408 |

Row 2 checks as
$0.2879349817 + \frac{0.2879349817 - 0.2886904762}{3} = 0.2879349817 - 0.0002518315 = 0.2876831502$.

**Step 3. The third column, order four.** Simpson carries an $O(h^4)$ error, so
the factor is $4^2 - 1 = 15$:

$$
R_{3,2} = R_{3,1} + \frac{R_{3,1} - R_{2,1}}{4^2 - 1}
$$

$$
R_{3,2} = 0.2876821408 + \frac{0.2876821408 - 0.2876831502}{15} = 0.2876821408 - 0.0000000673 = 0.2876820735
$$

**The Romberg table**

$$
\begin{array}{c|ccc}
R_{k,0} & R_{k,1} & R_{k,2} \\
\hline
0.2886904762 & & \\
0.2879349817 & 0.2876831502 & \\
0.2877453510 & 0.2876821408 & 0.2876820735
\end{array}
$$

$$
\boxed{I \approx 0.2876820735}
$$

> [!info] What the third column actually bought
> The integral has a closed form:
>
> $$
> \int_1^2 \frac{1}{2+x}dx = \ln(2+x)\Big|_1^2 = \ln 4 - \ln 3 = \ln\frac{4}{3} = 0.2876820725
> $$
>
> The Romberg value differs by $1.05 \times 10^{-9}$, a relative error of
> $3.6 \times 10^{-9}$.
>
> Now compare with what plain Simpson gives on the **same** function values with
> **no** extra work. Composite Simpson with $n = 8$ is exactly $R_{3,1} =
> 0.2876821408$, whose relative error is $2.4 \times 10^{-7}\%$. One more column
> bought three more orders of magnitude, and the cost was one subtraction and one
> division. That is the entire argument for Romberg: it never evaluates the
> function again, it only recombines entries already in hand.

> [!warning] The factor is the thing to get right
> The divisors $3$, $15$, $63$ come from $4^j - 1$. They are not $2, 4, 8$ and they
> are not $3, 6, 12$.
>
> The reason is that halving $h$ multiplies the leading error term by $2^2 = 4$
> for a rule of order 2, so the extrapolation factor is $4 - 1 = 3$. For the
> second column the rule is order 4, so the factor is $4^2 - 1 = 15$. Writing
> $2^j - 1$ instead of $4^j - 1$ produces a table that still looks reasonable and
> is quietly wrong, which is why it is worth memorising the pattern $3, 15, 63$
> rather than re-derive it under exam pressure.

---

## Question 3

### **(a) Find the eigenvalues and eigenvectors of the matrix $A = \begin{bmatrix} 5 & 0 & 1 \\ 0 & -2 & 0 \\ 1 & 0 & 5 \end{bmatrix}$.**

*[Marks: 05, CO: 2]*

**Step 1. The characteristic equation.** Eigenvalues are the values of
$\lambda$ for which $A - \lambda I$ is singular:

$$
A - \lambda I = \begin{bmatrix} 5-\lambda & 0 & 1 \\ 0 & -2-\lambda & 0 \\ 1 & 0 & 5-\lambda \end{bmatrix}
$$

**Expand along the second row**, because it holds a single nonzero entry. This is
the whole trick: this matrix has a row of the form $(0, \cdot, 0)$, so the
determinant reduces to a $2 \times 2$ minor immediately.

$$
\det(A - \lambda I) = (-2-\lambda)\begin{vmatrix} 5-\lambda & 1 \\ 1 & 5-\lambda \end{vmatrix}
$$

$$
= (-2-\lambda)\left[(5-\lambda)^2 - 1\right]
$$

Now factor the bracket as a difference of squares, $(\,5-\lambda\,)^2 - 1^2$:

$$
= (-2-\lambda)\big[(5-\lambda) - 1\big]\big[(5-\lambda) + 1\big]
$$

$$
= (-2-\lambda)(4-\lambda)(6-\lambda) = 0
$$

Each factor gives one eigenvalue:

$$
\boxed{\lambda_1 = 6, \qquad \lambda_2 = 4, \qquad \lambda_3 = -2}
$$

**Step 2. Eigenvector for $\lambda_1 = 6$.** Solve $(A - 6I)v = 0$:

$$
\begin{bmatrix} -1 & 0 & 1 \\ 0 & -8 & 0 \\ 1 & 0 & -1 \end{bmatrix}\begin{bmatrix}v_1\\v_2\\v_3\end{bmatrix} = 0
$$

Row 1 gives $-v_1 + v_3 = 0$, so $v_3 = v_1$. Row 2 gives $-8v_2 = 0$, so
$v_2 = 0$. One free parameter, so one dimension of eigenvector space, which is
what you expect. Take $v_1 = 1$:

$$
v^{(1)} = \begin{bmatrix}1\\0\\1\end{bmatrix}, \qquad \|v^{(1)}\| = \sqrt2, \qquad \hat{v}^{(1)} = \frac{1}{\sqrt2}\begin{bmatrix}1\\0\\1\end{bmatrix}
$$

**Step 3. Eigenvector for $\lambda_2 = 4$.** Solve $(A - 4I)v = 0$:

$$
\begin{bmatrix} 1 & 0 & 1 \\ 0 & -6 & 0 \\ 1 & 0 & 1 \end{bmatrix}\begin{bmatrix}v_1\\v_2\\v_3\end{bmatrix} = 0
$$

Row 1 gives $v_1 + v_3 = 0$, so $v_3 = -v_1$, and row 2 gives $v_2 = 0$. Take
$v_1 = -1$, so $v_3 = 1$:

$$
v^{(2)} = \begin{bmatrix}-1\\0\\1\end{bmatrix}, \qquad \|v^{(2)}\| = \sqrt2, \qquad \hat{v}^{(2)} = \frac{1}{\sqrt2}\begin{bmatrix}-1\\0\\1\end{bmatrix}
$$

**Step 4. Eigenvector for $\lambda_3 = -2$.** Solve $(A + 2I)v = 0$:

$$
\begin{bmatrix} 7 & 0 & 1 \\ 0 & 0 & 0 \\ 1 & 0 & 7 \end{bmatrix}\begin{bmatrix}v_1\\v_2\\v_3\end{bmatrix} = 0
$$

Row 1 gives $7v_1 + v_3 = 0$, so $v_3 = -7v_1$. Row 2 is $0 = 0$, so $v_2$ is
free. Take $v_1 = 0$, hence $v_3 = 0$, and $v_2 = 1$:

$$
v^{(3)} = \begin{bmatrix}0\\1\\0\end{bmatrix}, \qquad \|v^{(3)}\| = 1, \qquad \hat{v}^{(3)} = \begin{bmatrix}0\\1\\0\end{bmatrix}
$$

**Answer**

$$
\boxed{
\lambda_1 = 6,\ \hat{v}^{(1)} = \frac{1}{\sqrt2}\begin{bmatrix}1\\0\\1\end{bmatrix};
\qquad
\lambda_2 = 4,\ \hat{v}^{(2)} = \frac{1}{\sqrt2}\begin{bmatrix}-1\\0\\1\end{bmatrix};
\qquad
\lambda_3 = -2,\ \hat{v}^{(3)} = \begin{bmatrix}0\\1\\0\end{bmatrix}
}
$$

> [!info] Three ways to confirm
> **Route 2, expand $\det(\lambda I - A)$ instead.** This gives
> $\lambda^3 - 8\lambda^2 - 4\lambda + 48$, and factoring that as
> $(\lambda - 6)(\lambda - 4)(\lambda + 2)$ returns the same three roots. Note
> that $\det(A - \lambda I)$ and $\det(\lambda I - A)$ differ by a factor of
> $(-1)^3 = -1$ for a $3 \times 3$ matrix, so the roots are identical and only
> the sign of the polynomial changes. The roots are what matter, so either
> convention gives the same answer.
>
> **Route 3, verify $Av = \lambda v$ directly.**
> $A\begin{bmatrix}1\\0\\1\end{bmatrix} = \begin{bmatrix}6\\0\\6\end{bmatrix} = 6v^{(1)}$, good.
> $A\begin{bmatrix}-1\\0\\1\end{bmatrix} = \begin{bmatrix}-4\\0\\4\end{bmatrix} = 4v^{(2)}$, good.
> $A\begin{bmatrix}0\\1\\0\end{bmatrix} = \begin{bmatrix}0\\-2\\0\end{bmatrix} = -2v^{(3)}$, good.
>
> **Route 4, orthogonality.** $A$ is real symmetric, so its eigenvectors must be
> mutually orthogonal. $v^{(1)}\cdot v^{(2)} = -1 + 0 + 1 = 0$ and
> $v^{(1)}\cdot v^{(3)} = 0$. Both hold. The matrix is symmetric, so this had to
> hold, which makes it a genuinely independent check: a sign error in one
> eigenvector would break the orthogonality immediately.

> [!note] See the answer without computing
> Reorder rows and columns together and $A$ splits into two blocks: the $2 \times 2$
> block $\begin{bmatrix}5&1\\1&5\end{bmatrix}$ formed by rows and columns 1 and 3,
> plus the isolated entry $-2$ in row and column 2.
>
> The $2\times 2$ block $\begin{bmatrix}a&b\\b&a\end{bmatrix}$ always has
> eigenvalues $a + b$ and $a - b$, because it is $aI$ plus
> $\begin{bmatrix}0&b\\b&0\end{bmatrix}$, and the latter is a reflection with
> eigenvalues $\pm b$. Here that gives $5 + 1 = 6$ and $5 - 1 = 4$, plus $-2$.
> All three answers, visible at a glance. When a matrix has that symmetry, spend
> ten seconds looking for it before spending ten minutes expanding a determinant.

---

### **(b) Using Euler's method, solve the following problems: (i) $\frac{dy}{dx} = \frac{3}{5}x^3y$, $y(0) = 1$, (ii) $\frac{dy}{dx} = 1 + y^2$, $y(0) = 0$.**

*[Marks: 05, CO: 2]*

**The method.** Take the slope at the left end of each step and project it
straight:

$$
\boxed{y_{n+1} = y_n + h f(x_n, y_n), \qquad x_{n+1} = x_n + h}
$$

Geometrically, that is drawing a straight line from $(x_n, y_n)$ to
$(x_n + h, y_n + h\,f)$ using the slope at the **start** of the interval. The
true curve bends away over the interval, and the accumulated error is why Euler
is only first order.

> [!warning] The printed question omits the step size
> The paper gives neither a step size $h$ nor an interval for either part, and
> both are needed before any number exists. Use $h = 0.25$ and $x: 0 \to 1$ for
> both parts, and **state the choice on the page**.
>
> This is worth dwelling on. A question with a missing parameter is not a
> question you cannot answer; it is a question where part of the mark is for
> choosing sensibly and saying so. Writing four rows of numbers with no
> indication of $h$ looks like an answer and is not one, because the examiner
> cannot tell what was computed. A single line saying "take $h = 0.25$, so four
> steps reach $x = 1$" settles the question and costs eight words.
>
> Why $h = 0.25$ and not $h = 0.5$? Because part (ii) is heading for a vertical
> asymptote, which the warning at the end of this section covers.

**(i) $y' = \frac{3}{5}x^3y$, $y(0) = 1$, $h = 0.25$**

| Step | $x_n$ | $y_n$ | Slope $\frac{3}{5}x_n^3y_n$ | $y_{n+1} = y_n + h \cdot \text{slope}$ |
| ---: | ---: | ---: | :--- | :---: |
| 1 | 0.00 | 1.0000000 | $\frac{3}{5}(0)^3(1) = 0$ | $1 + 0.25(0) = 1.0000000$ |
| 2 | 0.25 | 1.0000000 | $\frac{3}{5}(0.25)^3(1) = 0.0093750$ | $1 + 0.25(0.009375) = 1.0023440$ |
| 3 | 0.50 | 1.0023438 | $\frac{3}{5}(0.5)^3(1.002344) = 0.0751758$ | $1.002344 + 0.25(0.075176) = 1.0211377$ |
| 4 | 0.75 | 1.0211377 | $\frac{3}{5}(0.75)^3(1.021138) = 0.2584755$ | $1.021138 + 0.25(0.258475) = 1.0857566$ |

$$
\boxed{y(1) \approx 1.0857566}
$$

Step 1 is worth a second look, because a zero there is easy to misread as an
error. The slope is $\frac{3}{5}(0)^3(1) = 0$ because $x_0 = 0$, so $y$ does not
move at all on the first step and $y_1 = y_0 = 1$. That is correct, and it is why
$y_1$ and $y_2$ both start from exactly 1.

**(ii) $y' = 1 + y^2$, $y(0) = 0$, $h = 0.25$**

| Step | $x_n$ | $y_n$ | Slope $1 + y_n^2$ | $y_{n+1}$ |
| ---: | ---: | ---: | ---: | ---: |
| 1 | 0.00 | 0.0000000 | 1.0000000 | $0 + 0.25(1) = 0.2500000$ |
| 2 | 0.25 | 0.2500000 | 1.0625000 | $0.25 + 0.25(1.0625) = 0.5156250$ |
| 3 | 0.50 | 0.5156250 | 1.2658691 | $0.515625 + 0.25(1.265869) = 0.8320923$ |
| 4 | 0.75 | 0.8320923 | 1.6923776 | $0.832092 + 0.25(1.692378) = 1.2551867$ |

$$
\boxed{y(1) \approx 1.2551867}
$$

> [!info] What the exact solutions say
> Both parts are separable, which makes them unusually good checks.
>
> **(i)** $\frac{dy}{y} = \frac{3}{5}x^3dx$ gives $\ln y = \frac{3}{20}x^4$, so
> $$y = e^{\frac{3}{20}x^4} = e^{0.15x^4}$$
> At $x = 1$ this is $e^{0.15} = 1.1618342$. Euler's $1.0857566$ is low by
> $0.076$.
>
> **(ii)** $\frac{dy}{1+y^2} = dx$ gives $\arctan y = x$, so
> $$y = \tan x$$
> At $x = 1$: $\tan 1 = 1.5574077$. Euler's $1.2551867$ is low by $0.302$.
>
> Both are **underestimates**, and that is not a coincidence. Euler's method takes
> the slope at the left end of each interval, and both solutions are convex on
> $[0, 1]$, so the left-end tangent always lies below the curve. Euler
> systematically undershoots convex growth. If an Euler answer ever comes out
> *above* the exact value, that is a signal to look for an arithmetic error
> rather than a smaller step.

> [!warning] Part (ii) diverges at $h = 0.5$
> The exact solution is $y = \tan x$, which has a **vertical asymptote at
> $x = \frac{\pi}{2} \approx 1.5708$**. Any step crossing that point is asking for
> an infinite value, and Euler on a function whose slope grows with $|y|$ will run
> into it.
>
> With $h = 0.5$, the other natural choice, Euler from $y(0) = 0$ gives
> $y(0.5) = 0.5$ and then
> $$y(1) = 0.5 + 0.5\left(1 + 0.5^2\right) = 0.5 + 0.625 = 1.125$$
> against $\tan 1 = 1.5574$. The error is already $0.43$ after **two** steps,
> against $0.30$ after **four** steps at $h = 0.25$. Halving the step is buying
> real accuracy, so the method is not diverging yet, but it is heading for
> trouble, and the argument for $h = 0.25$ is not arbitrary preference.
>
> The general rule: when $|f|$ grows with $|y|$, as it does for $f = 1 + y^2$, the
> step must be small. Part (i) has the same structure, $\frac{3}{5}x^3y$ grows with
> $y$, but its slope starts at zero because $x_0 = 0$, so it tolerates a larger
> step and shows a smaller error.

> [!note] Confirming the order of accuracy
> Euler is first order: local error $O(h^2)$, global error $O(h)$. Halving $h$
> should therefore halve the error. Part (ii) gives $0.302$ at $h = 0.25$ against
> $0.432$ at $h = 0.5$, a ratio of $1.43$, moving toward $2$ as the step grows.
> Part (i) shows the same trend with a smaller error because its slope starts at
> zero. If halving $h$ were reducing the error by about 4, the method would be
> second order, and the suspect would be the arithmetic rather than the method.

---

## Question 4

### **(a) Briefly explain interpolation, extrapolation and curve fitting with examples.**

*[Marks: 03, CO: 1]*

All three take discrete data and produce a continuous relation. They differ in
what they **promise**, and the promise is what you are choosing when you pick
one.

**Interpolation** builds a function that passes through **every** given point
exactly:

$$
P(x_i) = y_i \quad \text{for every } i
$$

The answer is exact at the data and carries no modelling error at all. Example: a
thermocouple is calibrated at $0^{\circ}$C and $100^{\circ}$C, and its reading at
$37^{\circ}$C is found by interpolating between those two calibrations.

**Extrapolation** evaluates a fitted function **outside** the range of the data.
The function may pass through every point perfectly and still say nothing
trustworthy outside, because **nothing constrains it there**. Example: predicting
next year's sales figure from five years of history. The fit is exact on those
five years and can still be badly wrong on the sixth, because the polynomial that
threads five points has no particular opinion about the sixth.

**Curve fitting** finds the function that comes **closest** to all points without
passing through any, by minimising a misfit such as

$$
\sum_i \left[y_i - f(x_i)\right]^2
$$

Example: fitting a straight line to seven noisy voltage readings to recover the
true calibration slope. The line deliberately misses the readings, because
passing through them would reproduce the noise as well as the signal.

| | Interpolation | Extrapolation | Curve fitting |
| :-- | :-- | :-- | :-- |
| Passes through data | Yes | May or may not | No |
| Outside the data | Not defined | Defined but unreliable | Defined, degree dependent |
| Data assumed | Exact | Exact | Noisy |
| Point count | Need $n+1$ points for degree $n$ | Same | Can use fewer |
| Risk | Runge oscillation far out | Large and growing error | Under-fitting if too simple |

**Choosing between them.** Interpolate inside the data. Fit when the data are
noisy, or when the underlying trend rather than the individual points is the
object of interest. Extrapolation is required only when the target genuinely
lies outside the data range, and then only over a short distance, at most about
one data interval.

> [!warning] Extrapolation is not interpolation with a different number
> The trap is thinking that a degree 4 polynomial through five points is a
> reliable description of the function everywhere. It is an exact description
> at five points and an arbitrary one everywhere else. The dramatic version is
> Runge's phenomenon: a high-degree interpolant oscillates violently outside the
> data range while fitting perfectly inside it. Adding *more* data points makes
> this worse, not better.

> [!note] The one-line version
> $$\boxed{\text{interpolation passes through, extrapolation goes beyond, fitting minimises}}$$
>
> Three verbs, one per technique, and they are the whole distinction. If you
> remember nothing else from this question, remember that the first passes through,
> the second goes beyond, and the third gets as close as it can without touching.

---

### **(b) The distance covered by a rocket from $t = 8$ to $t = 30$ is given by $x = \int_8^{30}\left(2000\ln\left[\frac{140000}{140000 - 2100t}\right] - 9.8t\right)dt$. (i) Use Simpson's $1/3$ rule to find the approximate value of $x$, (ii) find the true error $E_t$, (iii) find the absolute relative true error $|\epsilon_t|$.**

*[Marks: 05, CO: 3]*

The integrand is the vertical velocity of the rocket:
$$f(t) = 2000\ln\left(\frac{140000}{140000 - 2100t}\right) - 9.8t$$
Interval $[a, b] = [8, 30]$, total interval width $b - a = 22$.

---

#### **Method 1: Single-Application Simpson's $1/3^{\text{rd}}$ Rule ($n = 2$, Standard Textbook Exam Solution)**

This problem is a classic exercise originally from Autar Kaw's *Numerical Methods with Applications*. In an examination setting without an explicit step size, "Simpson's 1/3rd rule" fundamentally refers to the single-application, 2-segment rule ($n = 2$):

**Step 1. Grid setup.**
With $n = 2$ segments:
$$h = \frac{b - a}{2} = \frac{30 - 8}{2} = 11\text{ s}$$
The three evaluation nodes are $t_0 = 8$, $t_1 = 19$, and $t_2 = 30$:
- $f(t_0) = f(8) = 2000\ln\left(\frac{140000}{140000 - 2100(8)}\right) - 9.8(8) = 177.2667\text{ m/s}$
- $f(t_1) = f(19) = 2000\ln\left(\frac{140000}{140000 - 2100(19)}\right) - 9.8(19) = 484.7455\text{ m/s}$
- $f(t_2) = f(30) = 2000\ln\left(\frac{140000}{140000 - 2100(30)}\right) - 9.8(30) = 901.6740\text{ m/s}$

**Step 2. Compute approximate distance $x$.**
$$
\begin{aligned}
x &\approx \frac{h}{3}\left[f(t_0) + 4f(t_1) + f(t_2)\right] \\
  &= \frac{11}{3}\left[177.2667 + 4(484.7455) + 901.6740\right] \\
  &= \frac{11}{3}[177.2667 + 1938.9820 + 901.6740] = \frac{11}{3}[3017.9227] = 11065.72\text{ m}
\end{aligned}
$$

$$
\boxed{\text{(i) } x \approx 11065.72\text{ m}}
$$

**Step 3. Analytical integration and error calculation.**
Integrating $f(t)$ by parts yields the exact distance:
$$I_{exact} = \int_8^{30} f(t)\,dt = 11061.34\text{ m}$$

- **(ii) True error ($E_t$):**
$$E_t = I_{exact} - x = 11061.34 - 11065.72 = -4.38\text{ m}$$
$$
\boxed{\text{(ii) } E_t = -4.38\text{ m}}
$$
*(Note: Because $E_t < 0$, the numerical approximation $x = 11065.72$ is slightly larger than the true distance, meaning Simpson's rule **overestimated** the true value).*

- **(iii) Absolute relative true error ($|\epsilon_t|$):**
$$|\epsilon_t| = \left|\frac{E_t}{I_{exact}}\right| \times 100\% = \left|\frac{-4.38}{11061.34}\right| \times 100\% = 0.0396\%$$
$$
\boxed{\text{(iii) } |\epsilon_t| = 0.0396\%}
$$

---

#### **Method 2: Composite Simpson's $1/3^{\text{rd}}$ Rule ($h = 1, n = 22$)**
If composite Simpson's rule is applied on $n = 22$ subintervals ($h = 1$):
- Summing the 23 points gives $x \approx 11061.335875\text{ m}$
- $E_t = 11061.335535 - 11061.335875 = -0.000340\text{ m}$ (overestimated)
- $|\epsilon_t| = 3.076 \times 10^{-6}\%$

---

### **(c) Compare Simpson's $1/3$ and $3/8$th rules.**

*[Marks: 02, CO: 1]*

| Feature | Simpson's $1/3^{\text{rd}}$ Rule | Simpson's $3/8^{\text{th}}$ Rule |
| :-- | :-- | :-- |
| **Formula weights** | $1, 4, 2, 4, \ldots, 4, 1$ (coefficients $\frac{h}{3}[1, 4, 1]$) | $1, 3, 3, 2, 3, 3, \ldots, 3, 1$ (coefficients $\frac{3h}{8}[1, 3, 3, 1]$) |
| **Panel width** | $2h$ (fits a 2nd-degree parabola) | $3h$ (fits a 3rd-degree cubic) |
| **Subintervals per panel** | 2 | 3 |
| **Subinterval constraint ($n$)** | $n$ must be **even** ($2 \mid n$) | $n$ must be a **multiple of 3** ($3 \mid n$) |
| **Order of accuracy** | 4th order ($O(h^4)$) | 4th order ($O(h^4)$) |
| **Truncation error** | $-\frac{(b-a)}{180}h^4 f^{(4)}(\xi)$ | $-\frac{(b-a)}{80}h^4 f^{(4)}(\xi)$ |
| **Error constant** | $\frac{1}{180} \approx 0.00556$ | $\frac{1}{80} = 0.0125$ |
| **Degree of precision** | 3 (exact for polynomials of degree $\le 3$) | 3 (exact for polynomials of degree $\le 3$) |

**Differences that matter in practice:**
1. **Accuracy comparison:** Simpson's $1/3$ rule is roughly $2.25$ times more accurate than the $3/8$ rule on the same step size because its error coefficient ($\frac{1}{180}$) is significantly smaller than that of the $3/8$ rule ($\frac{1}{80}$).
2. **Subinterval requirements:** Simpson's $1/3$ needs an even number of subintervals, whereas Simpson's $3/8$ requires $n$ to be divisible by 3. When $n$ is a multiple of 6, either rule may be used across the whole interval.
3. **Exactness on cubic polynomials:** Both rules have a degree of precision of 3. This means that for ANY polynomial of degree up to 3 (including cubics), both single-segment and composite Simpson's rules give the **exact** integral with zero truncation error, because $f^{(4)}(\xi) \equiv 0$. Truncation error only emerges for quartic (degree 4) and higher polynomials.
4. **Hybrid combination:** When $n$ is odd and not divisible by 3, a standard practice is to use Simpson's $1/3$ rule for the first $n - 3$ segments and Simpson's $3/8$ rule for the final 3 segments.

$$
\boxed{\text{Both are 4th order and exact for cubics; } 1/3 \text{ needs even } n,\ 3/8 \text{ needs } 3 \mid n,\ \text{and } 1/3 \text{ is more accurate}}
$$

---

# SECTION B

## Question 5

### **(a) Build a digital circuit that produces the output $(p \lor \neg r) \land (\neg p \lor (q \lor \neg r))$ when given input bits $p, q$ and $r$.**

*[Marks: 04, CO: 2]*

The question gives you an expression and asks for hardware. Building the circuit
straight from the expression works, but it needs four gates where three will do,
so the first job is simplification.

**Step 1. Simplify algebraically.** Look at the two bracketed terms:

$$
F = (p \lor \neg r) \land (\neg p \lor q \lor \neg r)
$$

$\neg r$ appears in both, and that is the handle to pull. Apply the distributive
identity

$$
(a \lor c) \land (b \lor c) = (a \land b) \lor c
$$

with $c = \neg r$, $a = p$ and $b = (\neg p \lor q)$:

$$
F = \neg r \lor \big[p \land (\neg p \lor q)\big]
$$

Now distribute inside the bracket:

$$
p \land (\neg p \lor q) = (p \land \neg p) \lor (p \land q) = 0 \lor (p \land q) = p \land q
$$

Therefore

$$
F = \neg r \lor (p \land q)
$$

**Step 2. Read off the circuit.**

1. Invert $r$ with a NOT gate to give $\neg r$.
2. AND $p$ with $q$ to give $p \land q$.
3. OR that with $\neg r$ to give the output $F$.

**Gates required:** 1 NOT, 1 AND (2-input), 1 OR (2-input) — Total: 3 gates.

**Logic Circuit Diagram (Simplified Form):**
```text
p ----\
       )---- AND ----(p ∧ q)----\
q ----/                          \
                                  )---- OR ----> F = ¬r ∨ (p ∧ q)
r ---->|NOT|---------(¬r)--------/
```

**Alternative: Direct (Unsimplified) Circuit:**
If implemented directly without simplification:
```text
r ---->|NOT|--------(¬r)----+-------------------+
                            |                   |
p --------------------------+----\              |
                                  )--- OR1 ---+  |
                            +----/            |  |
                            |                 |  |
p ---->|NOT|---(¬p)---------|-----------------|--+----\
                            |                 |        )--- OR3 ---+
q --------------------------|----+            |  +----/            |
                            |     )--- OR2 ---+--+                 |
                            +----+/                                |
                                                                   )--- AND ---> Output
                                                              +---/
(Output from OR1) --------------------------------------------+
```

$$
\boxed{F = \neg r \lor (p \land q)}
$$

> [!info] Confirming over all eight input combinations
> Comparing the simplified form against the original on every assignment of
> $(p, q, r)$:
>
> | $p$ | $q$ | $r$ | Original | $\neg r \lor (p \land q)$ |
> | :-: | :-: | :-: | :-: | :-: |
> | F | F | F | T | T |
> | F | F | T | F | F |
> | F | T | F | T | T |
> | F | T | T | F | F |
> | T | F | F | T | T |
> | T | F | T | F | F |
> | T | T | F | T | T |
> | T | T | T | T | T |
>
> All eight rows agree, so the simplification is exact.
>
> Row 8 is the one to check by eye. With $r$ true, $\neg r$ is false, and the
> output fires only if both $p$ and $q$ are true. The original says
> $(p \lor \neg r) \land (\neg p \lor q \lor \neg r) = (T \lor F) \land (F \lor T \lor F) = T \land T = T$.
> Agrees.
>
> **Why checking all eight rows is worth the eight lines.** A three-variable
> Boolean function is completely determined by its truth table, so eight agreeing
> rows is a *proof* of equivalence, not a sample. That is a rare situation in
> this subject where exhaustive checking is genuinely conclusive.

> [!note] An equivalent form if you only have NAND gates
> Applying the distributive law back the other way gives

> $$
> F = (\neg r \lor p) \land (\neg r \lor q)
> $$
>
> This is useful in hardware because NAND is often the only gate a cheap part
> family provides. De Morgan's theorem turns each bracket into a NAND followed by
> an inverter, and a NAND-inverter pair is itself a NAND with its inputs tied, so
> the whole thing maps onto two NAND stages.

> [!warning] The mistake that keeps this question's marks
> Building the original expression gate for gate: NOT $r$, OR with $p$, then NOT
> $p$, OR with $q$ and $\neg r$, then AND. Five gates instead of three. It is a
> correct circuit and it will earn the marks, but it leaves the simplification
> on the table, and simplification is what the four marks are for.
>
> The tell is that $\neg r$ appears twice in the printed expression. Any
> sub-expression that appears more than once is a candidate for factoring out.

---

### **(b) Four friends have been identified as suspects for an unauthorized access into a computer system. Alice said "Carlos did it." John said "I did not do it." Carlos said "Diana did it." Diana said "Carlos lied when he said that I did it." (i) If exactly one of the four suspects is telling the truth, who did it? (ii) If exactly one is lying, who did it?**

*[Marks: 04, CO: 3]*

**Translate the statements.** The four suspects are mutually exclusive, so exactly
one of them did it. Let the culprit be one of $A, J, C, D$.

| Statement | True when |
| :-- | :-- |
| $S_A$: "Carlos did it" | culprit $= C$ |
| $S_J$: "I did not do it" | culprit $\ne J$ |
| $S_C$: "Diana did it" | culprit $= D$ |
| $S_D$: "Carlos lied when he said I did it" | Carlos's claim was false, that is culprit $\ne D$ |

The structural observation that makes this easy: **$S_C$ and $S_D$ are exact
negations of each other.** Carlos says Diana did it; Diana says Carlos's claim
was false. Either Diana did it and Carlos is truthful, or she did not and Carlos
is lying. Exactly one of those two is therefore **always** true, whatever the
culprit. This drives both parts.

**(i) Exactly one telling the truth**

Test each culprit:

| Culprit | $S_A$ | $S_J$ | $S_C$ | $S_D$ | True count |
| :-- | :-: | :-: | :-: | :-: | --: |
| A | F | T | F | T | 2 |
| J | F | F | F | T | **1** |
| C | T | T | F | T | 3 |
| D | F | T | T | F | 2 |

Only one row gives a count of 1.

$$\boxed{\text{(i) John did it}}$$

**Reasoning without a table.** Since $S_C$ and $S_D$ are negations, one of them
must be true, so the single truth must be one of those two, which means Alice and
John are both lying. John lying means his statement "I did not do it" is false,
so John did it.

Verify: John lying, Carlos lying (Diana did not do it), Alice lying (Carlos did
not do it), Diana telling the truth (Carlos's claim was false). Exactly one truth.
Agrees.

**(ii) Exactly one lying**

Equivalently, exactly three telling the truth. The same table, reading the false
count:

| Culprit | $S_A$ | $S_J$ | $S_C$ | $S_D$ | Lying count |
| :-- | :-: | :-: | :-: | :-: | --: |
| A | F | T | F | T | 2 |
| J | F | F | F | T | 3 |
| C | T | T | F | T | **1** |
| D | F | T | T | F | 2 |

Only one row gives a lying count of 1.

$$\boxed{\text{(ii) Carlos did it}}$$

**Reasoning without a table.** Exactly one lying means Alice and Diana are both
telling the truth, since they cannot both lie. Alice true gives culprit $= C$.
Then John says "I did not do it", which is true since Carlos did it, and Carlos
says "Diana did it", which is false. Exactly one lie, Carlos's. Agrees.

> [!info] Why the enumeration is complete
> Four candidates for the culprit against four statements is 16 combinations, and
> the mutual-exclusion constraint that exactly one person did it removes none of
> them, since every candidate satisfies it. So testing four culprits against four
> statements **is** the full enumeration. Both answers are unique, so each part
> has a single solution, which is what the question asks you to establish rather
> than assume.

> [!warning] The two parts have different answers, and that is intended
> Part (i) says exactly one is true. Part (ii) says exactly one is lying, which
> means exactly three are true. These are very different conditions and they
> cannot both hold at once.
>
> Expecting the same culprit in both parts is the standard error here, and it is
> worth noticing *why* the intuition misfires. Both answers involve the phrase
> "exactly one", and it is natural to read the two parts as restatements of the
> same constraint. They are not. If you find yourself trying to make one culprit
> satisfy both, you have collapsed "one truth-teller" into "one liar", which is
> the same mistake as writing modus tollens and then applying it forwards.

---

### **(c) Show that each of the conditional statements is a tautology by using truth tables: (i) $\neg(p \to q) \to p$, (ii) $p \to (p \lor q)$.**

*[Marks: 02, CO: 2]*

A tautology is true on **every** assignment, so the last column of the table must
be T in all four rows. There is no partial credit in "show that", so both rows of
each table must be filled in; leaving the last column half blank defeats the
purpose.

**(i) $\neg(p \to q) \to p$**

$p \to q$ is F only when $p = T, q = F$. So $\neg(p \to q)$ is T only there.

| $p$ | $q$ | $p \to q$ | $\neg(p \to q)$ | $\neg(p \to q) \to p$ |
| :-: | :-: | :-: | :-: | :-: |
| F | F | T | F | T |
| F | T | T | F | T |
| T | F | F | T | T |
| T | T | T | F | T |

The final column is T in every row.

**Algebraic confirmation.** $\neg(p \to q) = \neg(\neg p \lor q) = p \land \neg q$.
Then $(p \land \neg q) \to p = \neg(p \land \neg q) \lor p = (\neg p \lor q) \lor p = \top$.

$$
\boxed{(i)\ \neg(p \to q) \to p \text{ is a tautology}}
$$

**(ii) $p \to (p \lor q)$**

| $p$ | $q$ | $p \lor q$ | $p \to (p \lor q)$ |
| :-: | :-: | :-: | :-: |
| F | F | F | T |
| F | T | T | T |
| T | F | T | T |
| T | T | T | T |

The final column is T in every row.

**Algebraic confirmation.** $p \to (p \lor q) = \neg p \lor (p \lor q) = (\neg p \lor p) \lor q = \top$.

$$
\boxed{(ii)\ p \to (p \lor q) \text{ is a tautology}}
$$

> [!note] Why (i) is the interesting one
> Both are tautologies, but (i) is doing something subtler and worth understanding
> rather than just tabulating.
>
> (ii) is the weakening rule: if a statement holds, then anything weaker also
> holds, and $p \lor q$ is weaker than $p$. Two marks for a table.
>
> (i) says something slightly more interesting. If $p \to q$ were false, then
> $\neg(p \to q)$ would be true, and the statement $p$ must follow. But
> $\neg(p \to q)$ being true *already means* $p$ is true, since $\neg(p \to q) =
> p \land \neg q$. So the whole formula reduces to "if $p$ then $p$", dressed up
> in an implication. That is the general shape of any statement of the form
> $\neg(p \to q) \to \text{something}$, and it is a common source of exam
> questions.

---

## Question 6

### **(a) Show that $\neg(p \leftrightarrow q)$ and $\neg p \leftrightarrow q$ are logically equivalent.**

*[Marks: 02, CO: 3]*

**Step 1. Build the truth table.**

| $p$ | $q$ | $p \leftrightarrow q$ | $\neg(p \leftrightarrow q)$ | $\neg p$ | $\neg p \leftrightarrow q$ |
| :-: | :-: | :-: | :-: | :-: | :-: |
| F | F | T | F | T | F |
| F | T | F | T | T | T |
| T | F | F | T | F | T |
| T | T | T | F | F | F |

The two computed columns are identical: F, T, T, F reading down the rows
$F F$, $F T$, $T F$, $T T$. Identical columns on every row means the formulas are
logically equivalent.

$$
\boxed{\neg(p \leftrightarrow q) \equiv (\neg p \leftrightarrow q)}
$$

**Step 2. Algebraic proof.** Rewrite both sides to the same thing.

Left side:

$$
\neg(p \leftrightarrow q) = \neg\big[(p \to q) \land (q \to p)\big]
= \neg(p \to q) \lor \neg(q \to p)
= (p \land \neg q) \lor (\neg p \land q)
$$

This is exclusive-or. Right side:

$$
\neg p \leftrightarrow q = (\neg p \to q) \land (q \to \neg p) = (p \lor q) \land (\neg q \lor \neg p)
$$

Distribute:

$$
(p \lor q) \land (\neg q \lor \neg p) = \big[(p \land \neg q) \lor (p \land \neg p) \lor (q \land \neg q) \lor (q \land \neg p)\big]
$$

The middle two terms are contradictions, since nothing is both a statement and its
negation:

$$
= (p \land \neg q) \lor 0 \lor 0 \lor (\neg p \land q) = (p \land \neg q) \lor (\neg p \land q)
$$

Both sides reduce to the same expression, so the equivalence is proven.

**In words.** "$p$ and $q$ disagree" means exactly one of them is true. If $p$ is
false, then "q agrees with $\neg p$" means $q$ is true, which is precisely the
case where they disagree. Flipping one input and asking for agreement tests the
same thing as asking for disagreement without the flip.

> [!note] Where the asymmetry comes from
> It is worth pausing on why this works for the *biconditional* and would not for
> the conditional. There is no analogous identity $\neg(p \to q) \equiv \neg p \to q$,
> and trying to assume one is a common slip.
>
> The reason is that $\leftrightarrow$ is symmetric under negation of an input
> while $\to$ is not. $p \leftrightarrow q$ is T when $p$ and $q$ agree. Negating
> $p$ makes it T when $p$ and $q$ *disagree*, which is exactly when
> $\neg(p \leftrightarrow q)$ is T. With $\to$, negating an input changes the
> structure of the formula rather than just flipping its value, so no such
> identity exists.

---

### **(b) Briefly explain modus ponens, modus tollens, hypothetical syllogism, disjunctive syllogism with truth tables and examples.**

*[Marks: 04, CO: 1]*

All four are **inference rules**. Each is a valid argument form, meaning the
conclusion is guaranteed true whenever the premises are true. Validity is about
the *form*, not about whether any particular conclusion happens to be true, which
is why a truth table is the right tool: you are checking the form.

---

**1. Modus ponens (MP), affirming the antecedent**

$$
p \to q, \quad p \ \therefore\ q
$$

| $p$ | $q$ | $p \to q$ | Premises both true | Conclusion $q$ |
| :-: | :-: | :-: | :-: | :-: |
| F | F | T | antecedent false | F |
| F | T | T | antecedent false | T |
| T | F | F | no | |
| T | T | T | **yes** | **T** |

Whenever both premises hold, so does the conclusion. Valid.

**Example.** "If the switch is closed the lamp is lit." The switch is closed.
Therefore the lamp is lit.

---

**2. Modus tollens (MT), denying the consequent**

$$
p \to q, \quad \neg q \ \therefore\ \neg p
$$

| $p$ | $q$ | $p \to q$ | $\neg q$ | Both true | Conclusion $\neg p$ |
| :-: | :-: | :-: | :-: | :-: | :-: |
| F | F | T | T | **yes** | T |
| F | T | T | F | no | |
| T | F | F | T | no | |
| T | T | T | F | no | |

Valid. MT is the contrapositive rule, since $p \to q \equiv \neg q \to \neg p$.

**Example.** "If the fuse has blown the lamp is dark." The lamp is not dark.
Therefore the fuse has not blown.

---

**3. Hypothetical syllogism (HS), chaining**

$$
p \to q, \quad q \to r \ \therefore\ p \to r
$$

| $p$ | $q$ | $r$ | $p \to q$ | $q \to r$ | $p \to r$ |
| :-: | :-: | :-: | :-: | :-: | :-: |
| F | F | F | T | T | T |
| F | F | T | T | T | T |
| F | T | F | T | F | T |
| F | T | T | T | T | T |
| T | F | F | F | T | F |
| T | F | T | F | T | T |
| T | T | F | T | F | F |
| T | T | T | T | T | T |

Whenever both premises are T, so is $p \to r$. Valid.

**Example.** "If it rains the ground is wet. If the ground is wet the crop grows."
Therefore if it rains the crop grows.

---

**4. Disjunctive syllogism (DS), eliminating by negation**

$$
p \lor q, \quad \neg p \ \therefore\ q
$$

| $p$ | $q$ | $p \lor q$ | $\neg p$ | Both true | Conclusion $q$ |
| :-: | :-: | :-: | :-: | :-: | :-: |
| F | F | F | T | no | |
| F | T | T | T | **yes** | T |
| T | F | T | F | no | |
| T | T | T | F | no | |

Valid.

**Example.** "The input is 0 or 1." The input is not 0. Therefore the input is 1.

---

**Summary and comparison**

| Rule | Form | Name | Uses |
| :-- | :-- | :-- | :-- |
| MP | $p \to q,\ p \therefore q$ | Affirming the antecedent | Forward chaining |
| MT | $p \to q,\ \neg q \therefore \neg p$ | Denying the consequent, that is contraposition | Backward chaining |
| HS | $p \to q,\ q \to r \therefore p \to r$ | Transitivity | Chaining rules |
| DS | $p \lor q,\ \neg p \therefore q$ | Elimination | Splitting a case |

**The invalid forms**

| Form | Status | Why it fails |
| :-- | :-- | :-- |
| $p \to q,\ q \therefore p$ | **Invalid** (Fallacy of affirming the consequent) | Counterexample: $p = F, q = T$. Premises $(F \to T) = T$ and $q = T$ are true, but conclusion $p = F$ is false. |
| $p \to q,\ \neg p \therefore \neg q$ | **Invalid** (Fallacy of denying the antecedent) | Counterexample: $p = F, q = T$. Premises $(F \to T) = T$ and $\neg p = T$ are true, but conclusion $\neg q = F$ is false. |

Both are the *converse* and *inverse* of a conditional, and a conditional is not
equivalent to its converse or its inverse. It is equivalent only to its
**contrapositive** $\neg q \to \neg p$, which is what MT uses.

$$
\boxed{\text{MP, MT, HS, DS are valid; affirming the consequent and denying the antecedent are not}}
$$

> [!warning] The converse trap, worked out
> "If the switch is closed, the lamp is lit" does **not** let you conclude "the
> lamp is lit, so the switch is closed". The lamp can be lit by a second switch,
> by a battery, or by daylight through the window. The lamp being lit is
> *consistent* with the switch being closed; it does not *entail* it.
>
> The general form of the mistake: $p \to q$ gives you one direction only. Forward
> from $p$ you may conclude $q$. Backward from $q$ you may conclude nothing about
> $p$ except via the contrapositive, which requires $\neg q$ and gives you
> $\neg p$, not $p$.
>
> **How to spot it in a proof.** If you ever find yourself concluding $p$ from
> $q$ using a conditional, stop. Either the rule you used was MT and you have
> negated something you should not have, or you have slipped into affirming the
> consequent.

> [!note] HS needs the matching middle term
> Hypothetical syllogism only works because the two conditionals share $q$. Given
> $p \to q$ and $r \to q$, you cannot conclude $p \to r$, and given $p \to q$ and
> $p \to r$ you cannot conclude $q \to r$. The chain has to be
> $p \to q \to r$ with the same statement in the middle, and it is worth reading
> the chain aloud to check that it is.

---

### **(c) With these hypotheses: "It is not sunny this afternoon and it is colder than yesterday." "We will go swimming only if it is sunny." "If we do not swimming, then we will take a canoe trip." "If we take a canoe trip then we will be home by sunset." Using the inference rules, construct a valid argument for the conclusion: "we will be home by sunset".**

*[Marks: 04, CO: 3]*

**Assign variables.**

| Symbol | Meaning |
| :-- | :-- |
| $S$ | it is sunny this afternoon |
| $C$ | it is colder than yesterday |
| $W$ | we go swimming |
| $K$ | we take a canoe trip |
| $H$ | we are home by sunset |

**Translate the four hypotheses.**

1. "It is not sunny this afternoon **and** it is colder than yesterday":
   $\neg S \land C$
2. "We will go swimming **only if** it is sunny". The phrase "only if" means
   swimming is a **necessary** condition of sunshine, so $W \to S$:
   $W \to S$
3. "If we do not swim, then we will take a canoe trip": $\neg W \to K$
4. "If we take a canoe trip then we will be home by sunset": $K \to H$

**Extract what is needed.** Split hypothesis 1 by simplification to get $\neg S$
and $C$. The proof needs only $\neg S$.

The goal is $H$, so work backwards from the rule that produces it. Rule 4 needs
$K$, rule 3 needs $\neg W$, and $\neg W$ comes from $S$ by modus tollens on rule
2.

**The valid argument, step by step.**

| Step | Statement | Rule |
| ---: | :-- | :-- |
| 1 | $\neg S \land C$ | Premise 1 |
| 2 | $\neg S$ | Simplification, 1 |
| 3 | $W \to S$ | Premise 2 |
| 4 | $\neg W$ | Modus tollens, 3 and 2 |
| 5 | $\neg W \to K$ | Premise 3 |
| 6 | $K$ | Modus ponens, 5 and 4 |
| 7 | $K \to H$ | Premise 4 |
| 8 | $H$ | Modus ponens, 7 and 6 |

Therefore "we will be home by sunset" is a **valid conclusion**.

$$
\boxed{\neg S \Rightarrow \neg W \Rightarrow K \Rightarrow H, \quad \text{so } H \text{ follows validly}}
$$

> [!warning] The traps in this question
> **"Only if" is not "if".** "We will go swimming only if it is sunny" is
> $W \to S$, **not** $S \to W$. Reading it backwards inverts the conditional and
> breaks the whole proof. If it had been read as $S \to W$, step 4 could not be
> derived, since $\neg S$ carries no information about $W$.
>
> The general form of the trap: "A **only if** B" gives $A \to B$, while "A
> **if** B" gives $B \to A$. The word order in English puts the *antecedent* in
> the "if" clause and the *consequent* in the "only if" clause, so read the phrase
> and identify which letter appears where before writing the arrow.
>
> **Hypothesis 1 is a conjunction.** It provides $\neg S$ by simplification. It is
> tempting to treat "not sunny and colder" as one unit and hunt for a rule that
> accepts it. Split it first.
>
> **$C$ is never used, and that is not a mistake.** The problem gives four
> premises but the conclusion needs three. The fourth, $C$, is surplus. Do not go
> looking for a way to involve it; a valid argument may use fewer premises than
> are supplied.

> [!note] The whole argument as one chain
> $$\underbrace{W \to S}_{\text{premise 2}},\ \underbrace{\neg S}_{\text{premise 1}} \vdash \underbrace{\neg W}_{\text{MT}} \vdash \underbrace{K}_{\text{MP}} \vdash \underbrace{H}_{\text{MP}}$$
>
> Each arrow uses a different rule, and each premise is consumed exactly once. No
> premise appears twice and no rule is applied to a statement that does not supply
> what it needs, so the derivation is sound.
>
> Reading the chain in one line is a good habit for longer arguments. A chain that
> will not compress into a single line of arrows usually has a step that does not
> follow, and that is much easier to spot in one line than in a numbered table.

---

## Question 7

### **(a) Suppose that $a$ and $b$ are integers, $a \equiv 4 \pmod{13}$, and $b \equiv 9 \pmod{13}$. Find the integer $c$ with $0 \le c \le 12$ such that (i) $c = 2a + 3b \pmod{13}$, (ii) $c = a^2 + b^2 \pmod{13}$.**

*[Marks: 04, CO: 2]*

Work entirely with the residues, then reduce to $0 \le c \le 12$. Congruence
arithmetic is exactly real arithmetic modulo the modulus, so substituting the
residues for $a$ and $b$ is valid from the start and keeps every intermediate
number small.

**(i) $c \equiv 2a + 3b \pmod{13}$**

$$
c \equiv 2(4) + 3(9) = 8 + 27 = 35 \pmod{13}
$$

Divide: $35 = 13(2) + 9$.

$$
\boxed{c = 9}
$$

**(ii) $c \equiv a^2 + b^2 \pmod{13}$**

$$
c \equiv 4^2 + 9^2 = 16 + 81 = 97 \pmod{13}
$$

Divide: $97 = 13(7) + 6$.

$$
\boxed{c = 6}
$$

> [!info] Two independent confirmations
> **(i)** $13 \times 2 = 26$ and $26 + 9 = 35$.
> **(ii)** $13 \times 7 = 91$ and $91 + 6 = 97$.
>
> Both remainders satisfy $0 \le c \le 12$ as the question requires.
>
> For (ii) there is a genuinely shorter route. Squaring reduced residues is safe
> because $16 \equiv 3 \pmod{13}$ and $81 \equiv 3 \pmod{13}$, so
> $c \equiv 3 + 3 = 6$. The same answer from much smaller numbers, which confirms
> the first computation.

> [!note] Reducing early keeps the numbers small
> Write $b \equiv 9$, then $b^2 \equiv 3$, then $c \equiv 3 + 3 = 6$. That route
> never produces a number above 9. Direct squaring gave 97. Same answer, and the
> first route cannot overflow a fixed-width register, which is not a cosmetic
> concern when the modulus is large or you are working by hand under time
> pressure.
>
> The reduction step to write $\begin{pmatrix} 1 \\ 0 \\ 1 \end{pmatrix}$, that is
> $35$ as $13(2) + 9$, must be shown. The answer is not "35 mod 13"; the answer is
> the remainder itself.

---

### **(b) Add $a = (1110)_2$ and $b = (1011)_2$.**

*[Marks: 03, CO: 2]*

**Method 1, positional value.**

$$
(1110)_2 = 1(2^3) + 1(2^2) + 1(2^1) + 0(2^0) = 8 + 4 + 2 + 0 = 14
$$

$$
(1011)_2 = 1(2^3) + 0(2^2) + 1(2^1) + 1(2^0) = 8 + 0 + 2 + 1 = 11
$$

$$
14 + 11 = 25
$$

Convert back: $25 = 16 + 8 + 1 = (11001)_2$.

**Method 2, binary addition, column by column.**

| Column | $2^4$ | $2^3$ | $2^2$ | $2^1$ | $2^0$ |
| :-- | :-: | :-: | :-: | :-: | :-: |
| **Carry row** | 1 | 1 | 1 | 0 | - |
| $a$ | 0 | 1 | 1 | 1 | 0 |
| $b$ | 0 | 1 | 0 | 1 | 1 |
| **Sum** | **1** | **1** | **0** | **0** | **1** |

Working right to left:

- $2^0$: $0 + 1 = 1$, write 1, carry 0
- $2^1$: $1 + 1 = 2$, write 0, carry 1
- $2^2$: $1 + 0 + 1 = 2$, write 0, carry 1
- $2^3$: $1 + 1 + 1 = 3$, write 1, carry 1 into $2^4$

$$
\boxed{(1110)_2 + (1011)_2 = (11001)_2 = 25_{10}}
$$

> [!info] What confirms the result
> Expand the result back to base 10:
> $(11001)_2 = 1(2^4) + 1(2^3) + 0(2^2) + 0(2^1) + 1(2^0) = 16 + 8 + 0 + 0 + 1 = 25$,
> which matches $14 + 11 = 25$.
>
> Both methods agree on 25, and the round trip is a complete check: positional
> value in, addition, positional value out.
>
> Note that $2^4$ appears in the answer, so the sum needs **five** bits.
> $14 + 11 = 25 > 15 = (1111)_2$, the largest four-bit value. This is overflow in
> four-bit arithmetic, so the result must be stored in five bits. That is the
> practical point of the question, and it is worth stating explicitly.

> [!warning] Carries are the only part that needs care
> The addition itself is trivial; the carries are where slips happen. Working
> right to left:
> $2^0$: $0 + 1 = 1$, write 1, **carry 0**.
> $2^1$: $1 + 1 = 2$, write 0, **carry 1**.
> $2^2$: $1 + 0 + 1 = 2$, write 0, **carry 1**.
> $2^3$: $1 + 1 + 1 = 3$, write 1, **carry 1** into $2^4$.
>
> Forgetting to add the incoming carry into the next column is the classic slip,
> and it is the only place where this problem can go wrong. Write the carry row
> explicitly in the table, as above, rather than holding it in your head.

---

### **(c) If $n$ is a composite integer then $n$ has a prime divisor less than or equal to $\sqrt{n}$.**

*[Marks: 03, CO: 2]*

**Proof.**

Let $n$ be composite. Then by definition $n = ab$ for integers $a, b$ with
$1 < a < n$ and $1 < b < n$.

**Key observation.** At least one of $a$ and $b$ is at most $\sqrt{n}$. Suppose
both were larger:

$$
a > \sqrt{n} \quad \text{and} \quad b > \sqrt{n} \quad \Longrightarrow \quad ab > \sqrt{n}\sqrt{n} = n
$$

Since $ab = n$, this is a contradiction. Hence $a \le \sqrt{n}$ or
$b \le \sqrt{n}$. Without loss of generality suppose $a \le \sqrt{n}$, so
$1 < a \le \sqrt{n}$.

**Now find a prime divisor at most $a$.** Every integer $a > 1$ has a prime
divisor: keep dividing by a prime factor until the result is 1, and the last
prime divided out is a prime $p$ dividing $a$. So there is a prime $p$ with
$p \mid a$.

Since $a \mid n$ and $p \mid a$, transitivity of divisibility gives $p \mid n$. And
$p \le a \le \sqrt{n}$.

$$
\boxed{\text{Every composite } n \text{ has a prime divisor } p \text{ with } p \le \sqrt{n}}
$$

> [!note] Why this matters
> This is the fact that makes trial division for factorisation terminate at
> $\sqrt{n}$ instead of at $n$. Without it you would test every integer up to $n$,
> which is about as slow as factoring can be; with it you test only up to the square
> root, which is the square root of the work. It is the reason a primality test
> runs in milliseconds rather than minutes.
>
> Worked examples: $91 = 7 \times 13$ with $\sqrt{91} = 9.539$, and the prime
> divisor $7$ is indeed below it. $97$ is prime, so the statement does not apply
> to it, which is why a trial division up to $9$ establishes its primality.

> [!warning] The precise statement is *at most*, not *less than*
> $p \le \sqrt{n}$, not $p < \sqrt{n}$. The equality case is real: $n = 49 = 7^2$
> has the prime divisor $7 = \sqrt{49}$. Getting this boundary wrong loses the
> proof of the $n = 4$, $9$, $25$, $49$ cases, and more importantly it loses the
> marks for precision in a question whose whole content is the inequality.
>
> The proof is also worth understanding structurally, because the key move is
> cheap: **if $ab = n$ then $\min(a, b) \le \sqrt{n}$**, since otherwise the product
> would exceed $n$. Every elementary factorisation algorithm is built on that one
> line.

---

## Question 8

### **(a) Briefly describe the pigeonhole principle with a real world example.**

*[Marks: 02, CO: 1]*

**The principle.** If $N$ objects are placed into $k$ boxes and $N > k$, then at
least one box holds at least two objects.

**Proof.** Suppose every box held at most one object. Then the boxes would hold
at most $k$ objects in total. But $N > k$, a contradiction.

**Real-world examples.**

1. **Socks.** From a drawer holding black and white socks only, drawing three
   socks guarantees two of a colour, since two boxes cannot take three objects
   with at most one each. This is the tightest version: $N = 3$ into $k = 2$.
2. **Birthdays.** With 366 possible birthdays, the *plain* principle needs $367$
   people to force a shared birthday, not 23. The famous result is therefore a
   **probabilistic** one, not a pigeonhole one: under a random model, past about
   23 people the chance of a shared birthday exceeds $50\%$.
3. **Pigeonholes in a building.** A building with $n$ floors and $n + 1$ people
   must have two on the same floor.
4. **Hash tables.** Storing $n$ keys in $m$ buckets forces a collision once
   $n > m$, which is why the load factor is kept below 1.

$$
\boxed{\text{More objects than boxes forces at least one box to hold two or more}}
$$

> [!warning] The principle is deterministic, not probabilistic
> It states that a collision **must** happen, with no randomness and no
> probability. The birthday paradox is a different result: it says a shared
> birthday is **likely** under a random model of birthdays.
>
> Students mix these up constantly because both get called "pigeonhole". Socks are
> certain; birthdays are only probable. If you quote 23 as a pigeonhole result
> you are wrong, and the correct pigeonhole figure for a year with 366 possible
> birthdays is 367.

> [!note] The tighter generalised form
> The generalised principle says that if $N$ objects go into $k$ boxes, then some
> box holds at least $\lceil N/k \rceil$ objects. The plain form is the special
> case $\lceil N/k \rceil \ge 2$. Part (c) of Question 8 in the 2022 paper asks
> for a real-world instance of the generalised version, and the hash table example
> above is the standard answer: $n$ keys in $m$ buckets forces some bucket to
> hold at least $\lceil n/m \rceil$ keys.

---

### **(b) A group of 30 people have been trained as astronauts to go on the first mission to mars. How many ways are there to select a crew of six people to go on this mission (assuming all crew members have the same job)?**

*[Marks: 03, CO: 2]*

**Setting up.** Selection is without regard to order, so order does **not**
matter: the crew $\{A, B, C\}$ is the same crew whichever order you write it.
Every crew member has the same job, so there is no assignment to count either.
This is a combination, $\binom{n}{r}$, not a permutation.

$$
\text{Ways} = \binom{30}{6} = \frac{30!}{6!\,24!}
$$

**Computing the factorial ratio.**

$$
= \frac{30 \cdot 29 \cdot 28 \cdot 27 \cdot 26 \cdot 25}{6 \cdot 5 \cdot 4 \cdot 3 \cdot 2 \cdot 1} = \frac{30 \cdot 29 \cdot 28 \cdot 27 \cdot 26 \cdot 25}{720}
$$

Group the numerator in pairs:

$$
30 \cdot 29 = 870, \qquad 28 \cdot 27 = 756, \qquad 26 \cdot 25 = 650
$$

$$
870 \times 756 \times 650 = 427518000
$$

$$
\frac{427518000}{720} = 593775
$$

$$
\boxed{\binom{30}{6} = 593775 \text{ ways}}
$$

> [!info] Three routes to the same number
> - $\frac{30!}{6!\,24!}$ evaluated directly gives $593775$.
> - The paired product $\frac{870 \times 756 \times 650}{720}$ gives
> $\frac{427518000}{720} = 593775$.
> - An independent implementation of $\binom{30}{6}$ gives $593775$.
>
> Note $427518000 = 720 \times 593775$, which is the *ordered* count that appears
> below. The two numbers differ by exactly $6!$, as they must.

> [!warning] Do not cancel the numerator into three pairs
> A tempting grouping is
> $\frac{30\cdot29}{2}\times\frac{28\cdot27}{6}\times 26\cdot25 = 435 \times 126 \times 650 = 35626500$,
> which is **60 times too large**.
>
> The reason is that $2$ and $6$ cancel only $12$ of the required $720$. To cancel
> correctly the three divisors must multiply to $720$, for example $6! = 6 \times 120$
> split as $2 \times 360$, or simply divide the whole numerator by $720$ in one
> step.
>
> Cancelling pairwise is where this answer most often goes wrong, and the error is
> silent because the arithmetic still looks tidy and the number is still
> plausible. It is the same failure mode as the $2018$ Runge-Kutta question, where
> every downstream figure was arithmetically correct and the head figure was
> wrong by a factor of ten.

> [!note] Why the assumption in the question matters
> "All crew members have the same job" is precisely what makes this
> $\binom{30}{6}$. Change the assumptions and the answer changes by a clean factor:
>
> - If the crew had a **commander**, the count would be
> $30 \times \binom{29}{5} = 30 \times 118755 = 3562650$, choosing the commander
> first.
> - If **order were counted**, the answer would be $\frac{30!}{24!} = 427518000$,
> which is exactly $6! = 720$ times larger, because each crew could be seated in
> $720$ orders.
>
> The question's assumption removes precisely that factor. Being able to say which
> assumption your formula depends on is what separates a combination answer from a
> memorised one.

---

### **(c) Briefly describe the Binomial theorem, and what is the coefficient of $x^{12}y^{13}$ in the expansion of $(2x - 3y)^{25}$?**

*[Marks: 04, CO: 3]*

**The theorem.** For positive integers $m$ and $n$,

$$
(x + y)^n = \sum_{r=0}^{n}\binom{n}{r}x^{n-r}y^r
$$

The general term is

$$
T_{r+1} = \binom{n}{r}x^{n-r}y^r, \qquad r = 0, 1, \ldots, n
$$

A proof by induction on $n$: the case $n = 1$ is immediate, and the step follows
from Pascal's identity $\binom{n+1}{r} = \binom{n}{r} + \binom{n}{r-1}$ applied to
$(x+y)^{n+1} = (x+y)^n \cdot (x+y)$.

**Applying it.** With $x \to 2x$ and $y \to -3y$ and $n = 25$,

$$
(2x - 3y)^{25} = \sum_{r=0}^{25}\binom{25}{r}(2x)^{25-r}(-3y)^r
$$

**Identify the term.** A general term carries $x^{25-r}y^r$. For $x^{12}y^{13}$ we
need

$$
25 - r = 12 \quad \text{and} \quad r = 13
$$

Both give $r = 13$, and the powers $12 + 13 = 25$ check out.

**The coefficient.**

$$
\text{coefficient} = \binom{25}{13}(2)^{12}(-3)^{13}
$$

Since $\binom{25}{13} = \binom{25}{12} = 5200300$,

$$
= 5200300 \times 4096 \times (-1594323)
$$

$$
\boxed{\text{coefficient of } x^{12}y^{13} = -33959763545702400}
$$

> [!info] Confirming the product
> Expanding $(2x - 3y)^{25}$ directly and reading off the coefficient of
> $x^{12}y^{13}$ returns $-33959763545702400$, the same value as
> $5200300 \times 4096 \times (-1594323)$. The three factors multiply out as
> $21300428800 \times (-1594323)$, confirming the product.

> [!warning] Two sign and index traps
> **The sign is negative.** The exponent of $y$ is $r = 13$, which is odd, and
> $(-3)^{13}$ is negative. Forgetting the sign of $(-3y)^{13}$ is the most common
> error here, and it is a factor-of-minus-one error that a sanity check on
> magnitude will not catch.
>
> **The power of 2 belongs to $x$, not to $y$.** $(2x)^{12}$ gives
> $2^{12} = 4096$. Writing $2^{13}$ instead is the second most common error, and
> it produces a wildly different number, so at least that one is self-detecting.
>
> The rule that prevents both: the exponent of $x$ in a term is $n - r$, so the
> factor $2$ carries $n - r = 12$ while the factor $-3$ carries $r = 13$. **The
> exponents in the monomial decide which base goes with which factor.** Write
> $(2x)^{25-r}(-3y)^r$ on one line and read the exponents straight off it.
>
> A useful check on $r$: the two exponents must add to $n$. Here $12 + 13 = 25$.
> If your $r$ does not satisfy that, it is wrong before any arithmetic happens.

---

### **(d) Why is discrete mathematics essential in computer science and algorithm design?**

*[Marks: 01, CO: 1]*

Discrete mathematics supplies the exact language for the structures a computer
represents, so that correctness and cost can be reasoned about rather than
guessed at.

Sets, relations, graphs, logic and counting describe what is stored and how it is
linked. Combinatorics counts the cases an algorithm must handle, which is what
converts "this is fast" into a bound. Logic gives proof rules that certify an
algorithm correct, so correctness is demonstrated rather than asserted. And the
binary system Question 7(b) uses is itself discrete: arithmetic on a fixed number
of bits is arithmetic in a finite structure, with overflow as one of its theorems.

$$
\boxed{\text{Discrete mathematics is the language in which algorithms are specified, proved and costed}}
$$

> [!note] One mark, so one tight paragraph
> This is a one-mark question and it is the last one in the paper. It is asking
> whether you can state the reason in a sentence, so a single paragraph of three
> connected claims is the right size. A page of examples will read as padding and
> will not earn a second mark, because there is no second mark.