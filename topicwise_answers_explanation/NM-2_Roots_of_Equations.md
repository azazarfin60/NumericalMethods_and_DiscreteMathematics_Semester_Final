---
title: "NM-2 · Roots of Equations"
tags:
  - numerical-methods
  - discrete-mathematics
  - topicwise-clusters
---

[🏠 Master Index](00_Index.md) | [← Prev Topic: NM-1 · Error Analysis](NM-1_Error_Analysis.md) | [Next Topic: NM-3 · Linear Systems →](NM-3_Linear_Systems.md)

---

# NM-2 · Roots of Equations

> **Topic ID:** NM-2  
> **Section:** Section A -- Numerical Methods  
> **Exam Weight:** 🔴 High Priority (Tier 1) | 8/8 Years Examined (100% Frequency) | Typical Weight: 10–14 marks (Question 2)  
> **Subtopics Included:** 7 subtopics (NM-2.1 through NM-2.7)  
> **Origin Layer:** Authored in `../answers_explanation/`. All numerical results and boxed equations match character-for-character.

---

## 📑 Subtopics Covered in this Cluster

| Subtopic ID | Subtopic Title | Priority | Exam Frequency | Section Navigation |
|:---|:---|:---:|:---:|:---|
| **NM-2.1** | Fundamentals & Classification | 🔴 | 2019, 2020, 2021, 2022 | [Jump to NM-2.1](#nm-21) |
| **NM-2.2** | Bisection Method | 🔴 | 2017, 2018, 2020, 2024, CT-01 | [Jump to NM-2.2](#nm-22) |
| **NM-2.3** | False Position / Regula Falsi | 🔴 | 2017, 2018, 2020, 2021, CT-01 | [Jump to NM-2.3](#nm-23) |
| **NM-2.4** | Newton-Raphson Method | 🔴 | 2017, 2018, 2019, 2020, 2021, 2023 | [Jump to NM-2.4](#nm-24) |
| **NM-2.5** | Secant Method | 🟠 | 2017, 2020 | [Jump to NM-2.5](#nm-25) |
| **NM-2.6** | Method Comparison & Convergence | 🔴 | 2020, 2022, CT-01 | [Jump to NM-2.6](#nm-26) |
| **NM-2.7** | Roots of Polynomials | 🟠 | 2017, 2019, 2020, 2021, 2024 | [Jump to NM-2.7](#nm-27) |

---

<a id="nm-21"></a><a id="nm-2.1"></a>
## NM-2.1 · Fundamentals & Classification

### [2019 Q.2(a)]

**Question.** What is meant by iterative method? Write the names of iterative methods to solve nonlinear equations. Write the generalized steps to solve the nonlinear equations using iterative methods.

*[Marks: 04]*

**Solution.**

An **iterative method** solves $f(x) = 0$ by producing a sequence
$x_0, x_1, x_2, \ldots$ from a starting estimate $x_0$, each term obtained from the
preceding ones by a fixed rule, so that the sequence converges to the root
$x = r$. The answer is accepted when successive terms agree to the required
precision, rather than when a formula closes.

**Methods for a nonlinear equation**

1. Bisection (or false position, regula falsi)
2. Fixed-point iteration
3. Newton-Raphson
4. Secant
5. Bairstow (for polynomial roots)

**Generalized steps**

1. Rewrite the problem in the form $f(x) = 0$.
2. Determine the interval of interest, and count the roots in it from a change of
   sign of $f$.
3. Choose a starting estimate $x_0$ and, where required, a second estimate.
4. Derive the iteration formula $x_{k+1} = g(x_k)$.
5. Apply the formula repeatedly, recording each iterate.
6. Test for convergence by comparing successive iterates,
   $|x_{k+1} - x_k| < \varepsilon$, with $\varepsilon$ the tolerance.
7. If the sequence diverges or stalls, restart from a better estimate or from
   another method, and note the failure.
8. Verify the accepted root by substitution back into $f(x) = 0$.

> [!warning] Step 6 is the one that fails quietly
> "Successive iterates agree" is a weak test. It reports convergence when the
> iteration has stalled rather than when it has arrived, and it says nothing about
> whether the root is real.
>
> Two safer habits, both free: test the **residual** $\lvert f(x_k)\rvert < \varepsilon$
> rather than the step size, and **substitute the answer back** at the end. A
> stalled sequence with a small step and a large residual is the standard failure
> of Newton near a stationary point, and only the residual exposes it.

> [!note] Why the answer is a sequence and not a number
> This is the conceptual difference from 2020 Q.2(a). A direct method produces
> $\frac{-10 + 30}{2}$ and the answer is exact. An iterative method produces
> $5, 11.25, 10.048, 10.0001, 10$ and the answer is a limit.
>
> That sounds worse and is usually better, because the limit is reached to a
> **chosen** precision in a **chosen** number of steps, while the closed form may
> not exist at all. The cost of the flexibility is the obligation to test
> convergence, and step 6 exists for that reason alone.

---

### [2021 Q.2(a)]

**Question.** Define bracketing methods with example.

*[Marks: 02, CO: 1]*

**Solution.**

**Definition.** A **bracketing method** is an iterative root finder that begins
with an interval $[a, b]$ in which the function changes sign,

$$
f(a) \cdot f(b) < 0
$$

By the intermediate value theorem a continuous $f$ must have at least one root in
$(a, b)$. Each iteration picks a new point inside the current interval and retains
the half that still shows a sign change, so the root is never lost.

**Properties.**

1. **Convergence is guaranteed**, from any valid bracket, for any continuous $f$.
2. Only the **sign** of $f$ is needed, never $f'$. That is the big practical
   advantage, since a derivative is often harder to obtain than a function value.
3. The interval halves each step for bisection, so the error bound after $n$ steps
   is $\frac{b_0-a_0}{2^{n+1}}$.
4. Convergence is **slow**, linear for bisection, because no curvature
   information is used.

**Examples.**

| Method | New point | Rate |
| :-- | :-- | :-- |
| Bisection | Midpoint, $\frac{a+b}{2}$ | Linear |
| Regula falsi | Chord, $\frac{a f(b) - b f(a)}{f(b)-f(a)}$ | Superlinear, often |
| Illinois method | Regula falsi with a halved stale value | Superlinear, robust |

$$\boxed{\text{Enclose the root in a sign-changing interval and keep halving it; convergence is guaranteed}}$$

> [!note] Why the name, and what the guarantee is worth
> "Bracketing" means the iterate is *trapped* between two values of opposite sign,
> and the trap can only shrink. That is a stronger statement than "it usually
> converges", and it is what makes bracketing the fallback of choice when an open
> method misbehaves.
>
> The cost is speed. Superlinear rates in the table are for regula falsi and
> Illinois on well-behaved functions; part (b) of this question shows regula
> falsi stagnating on a strongly convex one, where it is barely better than
> bisection.

---

### [2022 Q.1(a)]

**Question.** What is the difference between open and bracketing method of root finding?

*[Marks: 02, CO: 1]*

**Solution.**

**Bracketing.** You start with an interval $[a,b]$ in which $f$ changes sign.

$$
f(a) \cdot f(b) < 0
$$

Continuity then guarantees at least one root inside. Each iteration throws away
the half of the interval that does not contain the sign change, so the interval
can never lose the root. That guarantee is the whole point.

**Open.** No interval. You start from a single guess $x_0$ and generate the next
point from a formula. Nothing keeps the iterates near the root, so a bad start
can send them off to infinity.

| Property | Bracketing | Open |
| :-- | :-- | :-- |
| Initial data | an interval with a sign change | one estimate $x_0$ |
| Needs | $f$ and its sign | $f$ **and** $f'$ |
| Convergence | always, from any valid bracket | only if $x_0$ is close enough |
| Rate | linear, $O(h)$ | superlinear, or quadratic |
| Examples | bisection, regula falsi | Newton-Raphson, secant, fixed point |

$$\boxed{\text{bracketing encloses the root and always converges; open methods start free and may not}}$$

> [!warning] The trade is safety against speed, not right against wrong
> An open method that converges is usually much faster: Newton-Raphson is
> quadratic, bisection is only linear, so Newton gets six correct digits in
> about five steps where bisection needs about thirty. The catch is that Newton
> can also fail completely, and there is no way to tell from the output that it
> has.
>
> This is why production root-finders keep a bracket and fall back to bisection
> whenever a Newton step leaves it. The hybrid gets the speed of the open method
> and the guarantee of the bracketing one, which is the reason the distinction
> matters beyond the two marks.

---

---

**Also asked here.**

- *2019 Q.2(b)* is the same question as [[NM-2.7_Roots_of_Polynomials|NM-2.7]], which is written in `NM-2.7`.
- *2020 Q.2(a)* is the same question as [[NM-2.6_Method_Comparison_and_Convergence|NM-2.6]], which is written in `NM-2.6`.

---

<a id="nm-22"></a><a id="nm-2.2"></a>
## NM-2.2 · Bisection Method

### [2017 Q.3(c)]

**Question.** Explain the bisection method for finding a real root of the equation $f(x) = 0$ and write an algorithm for its implementation with a test for relative accuracy.

*[Marks: 06]*

**Solution.**

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

### [2018 Q.2(a)]

**Question.** Develop an algorithm to calculate the root of any non-linear equation by bisection method.

*[Marks: 04]*

**Solution.**

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

### [2024 Q.2(a)]

**Question.** Given the polynomial $f(x) = x^3 - 6x^2 + 11x - 6$, use the bisection (bracketing) method to find a root in the interval up to two iterations.

*[Marks: 03, CO: 2]*

**Solution.**

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

<a id="nm-23"></a><a id="nm-2.3"></a>
## NM-2.3 · False Position / Regula Falsi

### [2017 Q.2(b)]

**Question.** Write down the algorithm steps while finding the root of a nonlinear equation using false position method.

*[Marks: 04]*

**Solution.**

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

### [2018 Q.2(b)]

**Question.** Derive the expression of the next approximation of a root of the non-linear function $f(x) = 0$ using regula-falsi method.

*[Marks: 04]*

**Solution.**

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

### [2021 Q.2(b)]

**Question.** Given that the equation $x^{2.2} = 69$ has a root between 5 and 8. Use the method of regula-falsi to determine it.

*[Marks: 04, CO: 3]*

**Solution.**

**Step 1. Define the function and check the bracket.**

$$
f(x) = x^{2.2} - 69
$$

$$
f(5) = 5^{2.2} - 69 = 34.4932 - 69 = -34.5068
$$

$$
f(8) = 8^{2.2} - 69 = 97.0059 - 69 = +28.0059
$$

$f(5) < 0 < f(8)$, so a root lies in $(5, 8)$. The function is continuous there
since $x^{2.2}$ is continuous for $x > 0$.

**Step 2. The formula.** Draw the straight line joining the two endpoints. It cuts
the $x$-axis at

$$
x = \frac{a f(b) - b f(a)}{f(b) - f(a)}
$$

> [!warning] The bracket is nearly balanced, and that is a coincidence worth noticing
> $f(5) = -34.51$ and $f(8) = +28.01$ are of similar size, so the chord's
> intercept lands near the middle of the interval, $6.656$, rather than near
> either end. Because the signs are already close in magnitude, the first step is
> nearly as good as bisection's.
>
> Check your own arithmetic against this: the first iterate is
> $\frac{5(28.0059) + 8(34.5068)}{28.0059 + 34.5068} = \frac{416.0839}{62.5127}$.
> A number far from $6.656$ means a sign was dropped somewhere.

**Step 3. Iterate.** Keep whichever endpoint has the same sign as the new point and
replace the other.

| Iteration | $a$ | $b$ | New point $x$ | $f(x)$ |
| --: | --: | --: | --: | --: |
| 1 | 5.000000 | 8.000000 | 6.655990 | $-4.27563$ |
| 2 | 6.655990 | 8.000000 | 6.834002 | $-0.40615$ |
| 3 | 6.834002 | 8.000000 | 6.850670 | $-0.03755$ |
| 4 | 6.850670 | 8.000000 | 6.852209 | $-0.00346$ |
| 5 | 6.852209 | 8.000000 | 6.852351 | $-0.00032$ |
| 6 | 6.852351 | 8.000000 | 6.852364 | $-0.00003$ |
| 7 | 6.852364 | 8.000000 | 6.852365 | $-0.000003$ |

Working the first row in full:

$$
x_1 = \frac{5(28.0059) - 8(-34.5068)}{28.0059 - (-34.5068)} = \frac{140.0295 + 276.0544}{62.5127} = \frac{416.0839}{62.5127} = 6.655990
$$

$$\boxed{x = 6.85237 \quad \text{(to five decimal places)}}$$

Or to four places, $x = 6.8524$.

> [!info] Check by two independent routes
> **Secant method.** Starting from the same two points, the secant iteration gives
> $6.65599006$, $6.83400179$, $6.85268624$, $6.85236460$, $6.85236512$. Same
> answer to more digits.
>
> **Closed form.** $x^{2.2} = 69$ with $2.2 = \frac{11}{5}$ gives
> $x = 69^{5/11} = 6.8523651204$. The last regula falsi iterate is $6.852365$, and
> the closed form rounds to $6.85237$. All three agree.
>
> **Bisection.** Starting from $(5, 8)$, after 18 iterations the bracket is
> $(6.85236359, 6.85237503)$ and the midpoint $6.85236931$ is within
> $4.2 \times 10^{-6}$ of the exact root. One more bisection halves that again.

> [!warning] Why the upper endpoint never moves
> The table gives $b = 8.000000$ for every iteration. This is the well known
> **one-sided stagnation** of regula falsi on this function. The graph is strongly
> convex over $(5, 8)$, so the chord always cuts the axis on the same side, and
> only the $a$ endpoint is replaced.
>
> The consequence is that convergence is much slower than the "superlinear" label
> suggests. Seven iterations to reach six figures looks like bisection's pace,
> not regula falsi's. The **Illinois variant** fixes it by halving the retained
> function value on each step:
> $$\text{repeat } a f(a) \text{ as } \frac{1}{2}a f(a) \text{ every second iteration}$$
> That restores the fast convergence while keeping the sign-change guarantee.
>
> The same function with a different bracket appears in 2017 Q.2(b), which is
> worth knowing about, since the stagnation behaves differently there.

---

**Answered in phase P6, in `../CT_Questions/`.**

- *CT-01 Q.2(b)* is a class-test question. Its answer is in `../CT_Questions/CT_answers_exam_style.md`, with the reasoning in `../CT_Questions/CT_answers_explanation.md`.

---

<a id="nm-24"></a><a id="nm-2.4"></a>
## NM-2.4 · Newton-Raphson Method

### [2017 Q.2(a), 2021 Q.1(b), 2023 Q.1(c)]

**Appeared in:** 2017 Q.2(a), 2021 Q.1(b), 2023 Q.1(c)

**Question.** Briefly discuss the limitations of N-R method to find the root of any non-linear equation. How can we solve it?

*[Marks: 04]*

**Solution.**

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

### [2018 Q.2(c)]

**Question.** Find the real root of the equation $x \sin x + \cos x = 0$ using N-R method.

*[Marks: 04]*

**Solution.**

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

### [2019 Q.2(c)]

**Question.** Write the steps of N-R method. Discuss its merits and demerits.

*[Marks: 04]*

**Solution.**

**Newton-Raphson for $f(x) = 0$.**

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
   correct digits roughly doubles per step, so three or four steps usually suffice
   where bisection needs thirty.
2. **One estimate is enough.** Only $x_0$ is needed, unlike the secant or
   regula-falsi methods which require two.
3. **Non-polynomial equations are handled.** Transcendental equations, for instance
   $x = \cos x$ or $I = I_s(e^{V/V_T}-1)$, are solved directly, with no need to
   isolate $x$.
4. **Extends to systems.** The same tangent idea applies to $n$ simultaneous
   equations through the Jacobian, which makes it the standard method for a
   nonlinear network.

**Demerits**

1. **$f'(x)$ must be available.** An analytic derivative is needed. When it is
   difficult or costly, the method loses its advantage.
2. **Poor $x_0$ can fail.** If the tangent is nearly horizontal, $f'(x_k) \approx 0$
   and the next iterate is thrown far away. Starting far from the root can send the
   sequence into divergence rather than toward it.
3. **No bracket is maintained.** Unlike bisection, the method gives no guaranteed
   interval containing the root, so a failure may not be detected until late.
4. **Repeated roots slow it down.** At a root of multiplicity $m > 1$ the
   convergence order falls from 2 toward 1, and each step gains little.
5. **Complex roots are awkward.** The iterates can leave the real axis when $f$ or
   $f'$ takes complex values, so real-root isolation must be done beforehand.

> [!warning] Demerits 3 and 2 have a single fix
> Keep a sign-changing bracket $[a, b]$ with $f(a)f(b) < 0$, and take a bisection
> step whenever a Newton step leaves it. That restores the guarantee of demerit 3
> and removes most of the failures of demerit 2, at the cost of a comparison per
> step.
>
> This hybrid is what production root finders actually do. Newton alone is the
> teaching form; Newton inside a bracket is the engineering form.

---

### [2020 Q.2(b)]

**Question.** An electrical power equation is given as follows: $3I^2 - 4I - 4 = 0$. Calculate 3 iterations of the Newton-Raphson method to obtain the value of current.

*[Marks: 06]*

**Solution.**

**Step 1. Set up.**

$$
f(I) = 3I^2 - 4I - 4, \qquad f'(I) = 6I - 4
$$

**Step 2. Choose a starting value.** The paper prints none, so pick one and say
so. A current is a positive quantity, and

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

$$\boxed{I_3 = 2.0456 \text{ Amp after three iterations, and the true root is } I = 2 \text{ Amp}}$$

**Step 5. Check the exact root.** The quadratic formula settles it:

$$
I = \frac{4 \pm \sqrt{16 + 48}}{6} = \frac{4 \pm 8}{6}
$$

which gives $I = 2$ and $I = -\frac{2}{3}$. Only $I = 2$ is a physical current,
and $I_3 = 2.045555$ is closing on it.

> [!warning] Two traps in this question
> **1. The start matters more than the count.** $I_0 = 1$ throws the first iterate
> to $3.5$, a full $1.5$ past the answer at $2$. The reason is visible in the
> table: at $I_0 = 1$ the derivative is only $2$ while $f$ is $-5$, so the ratio
> $f/f'$ is $2.5$ and the first step is long.
>
> **2. There are two roots and only one is physical.** Newton's method has no
> built-in preference, and a careless start can land on $I = -\tfrac{2}{3}$. The
> quadratic formula shows both. Discard the negative one on physical grounds, and
> say that this is why. Starting from $I_0 = 0$ is unsuitable: it gives
> $f(0) = -4$, $f'(0) = -4$, so $I_1 = 0 - \frac{-4}{-4} = -1$, which walks
> straight off toward the negative root.

> [!info] Check by two independent routes
> **Closed form.** $I = 2$ and $I = -\tfrac{2}{3}$, from the quadratic formula.
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
> against $0.0456$ from $I_0 = 1$. Both are correct Newton runs; the start nearer
> the root simply needs fewer steps. **Same root, different arithmetic.**
>
> Note that the error ratio $0.0456 / 8.2\times10^{-5} \approx 556$ over two steps is
> near $2^{2\cdot 4}$, which is what quadratic convergence looks like once the
> iterate is in the basin.

---

<a id="nm-25"></a><a id="nm-2.5"></a>
## NM-2.5 · Secant Method

### [2017 Q.2(c)]

**Question.** Find the positive root of the equation $f(x) = x^3 - 3x^2 - x - 3 = 0$ by secant method (Use four iterations only).

*[Marks: 04]*

**Solution.**

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

<a id="nm-26"></a><a id="nm-2.6"></a>
## NM-2.6 · Method Comparison & Convergence

### [2020 Q.2(a)]

**Question.** Define roots of an equation. List the comparisons among bisection, secant, false position and Newton-Raphson methods.

*[Marks: 06]*

**Solution.**

**Root of an equation.** A **root** of $f(x) = 0$ is a value $x^*$ with $f(x^*) = 0$.
The graph of $f$ crosses or touches the $x$-axis at $x^*$.

A root is **simple** if $f'(x^*) \ne 0$, and **multiple** (or repeated) if
$f'(x^*) = 0$. The distinction matters because the methods below all assume a
simple root; a repeated root makes their convergence much slower.

A root is **explicit** if it can be written in closed form, and **implicit** if it
can only be found numerically. $\sqrt{2}$ is explicit. The root of
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

$$\boxed{\text{Bracketing methods are safe and slow; open methods are fast and unguaranteed}}$$

**How they relate.** They form a ladder from safest to fastest.

- **Bisection** is the safety net. It only needs a sign change, and it can never
  fail. That guarantee is why it survives in production codes.
- **False position** uses the same bracket but wastes it, because it keeps only
  one endpoint and lets the other run away. Faster than bisection, but it stalls
  on strongly convex functions, as 2021 Q.2(b) shows on $x^{2.2} = 69$.
- **Secant** throws the bracket away and fits a line through the last two
  points. The order $1.618$ is better than the labels "linear" suggest.
- **Newton** throws away the history except one point and uses the slope. It
  converges quadratically, so it is the method of choice when $f'$ is available
  and the start is good.

**The practical rule.** Keep a bracket. Try Newton. If a step leaves the bracket,
take a bisection step instead. This hybrid keeps Newton's speed and bisection's
guarantee, and it is what real root finders do.

> [!note] Why the "golden ratio" order is worth remembering
> The secant method's order $1.618 = \frac{1+\sqrt5}{2}$ is what makes it a real
> alternative to Newton rather than a consolation prize. It needs no derivative,
> and it is still superlinear.
>
> Compare the cost lines in the table: secant makes one function call per step,
> Newton makes two. Where $f'$ is expensive or genuinely unavailable, the secant
> method's order per function evaluation is actually competitive.
>
> The price is that the secant has no guarantee at all, while bisection does, and
> in a production code the guarantee is usually worth more than the order.

---

---

**Also asked here.**

- *CT-01 Q.2(b)* is the same question as [[NM-2.3_False_Position_and_Regula_Falsi|NM-2.3]], which is written in `NM-2.3`.

---

**Answered in phase P6, in `../CT_Questions/`.**

- *CT-01 Q.2(a)* is a class-test question. Its answer is in `../CT_Questions/CT_answers_exam_style.md`, with the reasoning in `../CT_Questions/CT_answers_explanation.md`.

---

<a id="nm-27"></a><a id="nm-2.7"></a>
## NM-2.7 · Roots of Polynomials

### [2019 Q.2(b)]

**Question.** Compute current, $I$ from the following power balance equation obtained from an electric circuit by using an iterative method: $5I^2 + 50I = 1000$.

*[Marks: 04]*

**Solution.**

Write the equation in the form $f(I) = 0$:

$$f(I) = 5I^2 + 50I - 1000 = 0, \qquad f'(I) = 10I + 50$$

**Closed-form check on the answer.** Dividing by 5,

$$I^2 + 10I - 200 = 0 \implies I = \frac{-10 \pm \sqrt{100 + 800}}{2} = \frac{-10 \pm 30}{2}$$

the two roots are $I = 10$ and $I = -20$. The current is positive, so $I = 10$ is
the root of interest. This fixes the target against which the iterations below are
judged.

**Iteration by Newton-Raphson.** The formula is

$$I_{k+1} = I_k - \frac{5I_k^2 + 50I_k - 1000}{10I_k + 50}$$

Take $I_0 = 5$, and note $f(5) = 125 + 250 - 1000 = -625 < 0$ while
$f(20) = 2000 + 1000 - 1000 > 0$, so the root lies above $I_0$ and the iteration
moves the right way.

| $k$ | $I_k$ | $f(I_k)$ | $f'(I_k)$ | $I_{k+1}$ |
| --: | --: | --: | --: | --: |
| 0 | 5 | $-625$ | 100 | $11.25$ |
| 1 | $11.25$ | $195.3125$ | $162.5$ | $10.0480769$ |
| 2 | $10.0480769$ | $7.2231$ | $150.4808$ | $10.0000768$ |
| 3 | $10.0000768$ | $0.0115$ | $150.0008$ | $10.0000000$ |

The iterates settle on $I = 10$. The last correction is $0.0000768$, already below
$10^{-4}$, so the value is accepted.

$$\boxed{I = 10\ \text{A}}$$

> [!info] Check against the original equation
> Substituting $I = 10$ directly, $5(100) + 50(10) = 500 + 500 = 1000$, matching
> the right-hand side exactly. The substitution is the simplest test available
> and it confirms both the arithmetic of the iteration and the algebraic solution
> $I = (-10 + 30)/2$.

> [!note] Reading the convergence off the table
> The corrections are $6.25$, $1.2019$, $0.0480$, $0.0000768$. The ratios of
> successive corrections are $5.2$, $25.0$, $625$, which is the signature of
> quadratic convergence: the correction is roughly the square of the one before.
>
> **Notice also that the derivative column settles at $150$**, which is
> $f'(10) = 10(10) + 50$. Once the iterate is the root, the derivative printed
> beside it must be the true derivative there, and it is. That column is free and
> it catches a whole class of transcription error.

---

### [2021 Q.2(c)]

**Question.** Determine the smallest root of the equation: $f(x) = x^3 - 9x^2 + 26x - 24 = 0$.

*[Marks: 06, CO: 3]*

**Solution.**

**Step 1. Locate the roots by sign changes.** Evaluate at integer values:

| $x$ | $f(x)$ | Sign |
| --: | --: | :-: |
| 0 | $-24$ | $-$ |
| 1 | $1 - 9 + 26 - 24 = -6$ | $-$ |
| 2 | $8 - 36 + 52 - 24 = 0$ | $0$ |
| 3 | $27 - 81 + 78 - 24 = 0$ | $0$ |
| 4 | $64 - 144 + 104 - 24 = 0$ | $0$ |
| 5 | $125 - 225 + 130 - 24 = 6$ | $+$ |

**Step 2. Recognise the factorisation.** All of $2, 3, 4$ are exact roots, and a
cubic has at most three, so

$$
f(x) = (x-2)(x-3)(x-4)
$$

Verification by expansion: $(x-2)(x-3) = x^2 - 5x + 6$, and
$(x^2-5x+6)(x-4) = x^3 - 4x^2 - 5x^2 + 20x + 6x - 24 = x^3 - 9x^2 + 26x - 24$.
Correct.

**Step 3. Smallest root.**

$$\boxed{x = 2}$$

**Step 4. Confirm with a numerical method**, since the question asks for root
finding. Use Newton-Raphson with

$$
f(x) = x^3 - 9x^2 + 26x - 24, \qquad f'(x) = 3x^2 - 18x + 26
$$

Start at $x_0 = 1.5$, where $f(1.5) = 3.375 - 20.25 + 39 - 24 = -1.875$ and
$f'(1.5) = 6.75 - 27 + 26 = 5.75$:

| Iteration | $x_n$ | $f(x_n)$ | $f'(x_n)$ |
| --: | --: | --: | --: |
| 0 | 1.5000000 | $-1.875000$ | 5.750000 |
| 1 | 1.8260870 | $-0.443823$ | 3.134215 |
| 2 | 1.9676929 | $-0.067779$ | 2.196974 |
| 3 | 1.9985440 | $-0.002918$ | 2.008742 |
| 4 | 1.9999968 | $-0.000006$ | 2.000019 |
| 5 | 2.0000000 | $0$ | 2.000000 |

Iteration 1: $x_1 = 1.5 - \frac{-1.875}{5.750000} = 1.5 + 0.326087 = 1.826087$.
Iteration 2: $x_2 = 1.826087 - \frac{-0.443823}{3.134215} = 1.826087 + 0.141606 = 1.967693$.

> [!warning] The derivative column is not decoration
> Newton divides by $f'(x_n)$, and here $f'$ drifts from $5.75$ to $2.00$ across
> the five steps, so a value carried over from the previous row is visibly wrong.
> It settles at $2.00 = f'(2)$, which is the self-consistency check at the root:
> once the iterate is the root, the derivative in the same row must be the true
> derivative there.
>
> This column is the cheapest possible error check, because it is a function of
> $x$ alone. If $x_n$ and $f'(x_n)$ ever disagree, one of them is wrong.

> [!warning] Choosing the bracket
> The interval $[1, 2]$ is **not** usable, because $f(2) = 0$ puts the root
> exactly on the endpoint and $f(1)f(2) = 0$, not $< 0$. The pair $[1.5, 2.5]$
> works: $f(1.5) = -1.875$ and
> $f(2.5) = 15.625 - 56.25 + 65 - 24 = 0.375$, so $f(1.5)f(2.5) = -0.703 < 0$.
>
> Also note there is **no** root below $2$. Since $f$ is negative on $[0, 2)$ and
> $f(2) = 0$, the value $2$ is the smallest root, not merely one of three. To see
> that $f$ really is negative on that interval, note that
> $f'(x) = 3x^2 - 18x + 26$ vanishes at $3 \pm \frac{\sqrt3}{3} \approx 2.423$ and
> $3.577$, so $f$ increases up to $2.423$ and has no turning point before $2$.

> [!note] Why six marks for a question this easy
> Because the marks are not for the factorisation, which is two lines of algebra.
> They are for the bracket check, the iteration table, the derivative column, and
> the argument that $2$ is the *smallest* rather than merely *a* root. A correct
> boxed answer with none of that supporting work would not earn the marks.

---

---

**Also asked here.**

- *2020 Q.2(b)* is the same question as [[NM-2.4_Newton_Raphson_Method|NM-2.4]], which is written in `NM-2.4`.
- *2024 Q.2(a)* is the same question as [[NM-2.2_Bisection_Method|NM-2.2]], which is written in `NM-2.2`.

---

[🏠 Master Index](00_Index.md) | [← Prev Topic: NM-1 · Error Analysis](NM-1_Error_Analysis.md) | [Next Topic: NM-3 · Linear Systems →](NM-3_Linear_Systems.md)
