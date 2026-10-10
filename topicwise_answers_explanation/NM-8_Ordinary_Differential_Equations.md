---
title: "NM-8 · Ordinary Differential Equations"
tags:
  - numerical-methods
  - discrete-mathematics
  - topicwise-clusters
---

[🏠 Master Index](00_Index.md) | [← Prev Topic: NM-7 · Numerical Differentiation](NM-7_Numerical_Differentiation.md) | [Next Topic: NM-9 · Eigenvalues & Eigenvectors →](NM-9_Eigenvalues_and_Eigenvectors.md)

---

# NM-8 · Ordinary Differential Equations

> **Topic ID:** NM-8  
> **Section:** Section A -- Numerical Methods  
> **Exam Weight:** 🔴 High Priority (Tier 1) | 7/8 Years Examined | Typical Weight: 10–14 marks  
> **Subtopics Included:** 8 subtopics (NM-8.1 through NM-8.8)  
> **Origin Layer:** Authored in `../answers_explanation/`. All numerical results and boxed equations match character-for-character.

---

## 📑 Subtopics Covered in this Cluster

| Subtopic ID | Subtopic Title | Priority | Exam Frequency | Section Navigation |
|:---|:---|:---:|:---:|:---|
| **NM-8.1** | IVP vs BVP Concepts | 🟠 | 2021, 2024 | [Jump to NM-8.1](#nm-81) |
| **NM-8.2** | Euler's Method | 🔴 | 2018, 2019, 2020, 2021, 2023 | [Jump to NM-8.2](#nm-82) |
| **NM-8.3** | Modified Euler / Heun's Method | 🟠 | 2017, 2018, 2020 | [Jump to NM-8.3](#nm-83) |
| **NM-8.4** | Runge-Kutta 2nd Order | 🟠 | 2020, CT-02B | [Jump to NM-8.4](#nm-84) |
| **NM-8.5** | Runge-Kutta 4th Order | 🔴 | 2017, 2018, 2019, 2024, CT-02B | [Jump to NM-8.5](#nm-85) |
| **NM-8.6** | Higher-Order & Systems of ODEs | 🟡 | 2018 | [Jump to NM-8.6](#nm-86) |
| **NM-8.7** | ODE Formulation from Physical Problems | 🟡 | 2021 | [Jump to NM-8.7](#nm-87) |
| **NM-8.8** | Boundary Value Problems | 🟡 ⚠️ | 2021, 2024 | [Jump to NM-8.8](#nm-88) |

---

<a id="nm-81"></a><a id="nm-8.1"></a>
## NM-8.1 · IVP vs BVP Concepts

### [2021 Q.5(a)]

**Question.** Define boundary value and initial value problem.

*[Marks: 02, CO: 2]*

**Solution.**

**Initial value problem (IVP).** A differential equation together with conditions
given at a **single** point, for example $y(0) = 1$. The solution can be marched
forward from that point because each new value depends only on the values already
computed.

**Boundary value problem (BVP).** A differential equation together with conditions
given at **both ends** of the interval, for example $y(0) = 0$ and $y(1) = 1$. No
starting value is known, so the whole interval must be solved at once.

| | IVP | BVP |
| :-- | :-- | :-- |
| Conditions | At one end | At both ends |
| How it is solved | March forward step by step | Solve the full algebraic system |
| Resulting system | Lower triangular | Tridiagonal for a second-order ODE |
| Cost | Very low per step | Full linear solve |
| Sensitivity | Local; errors stay near the start | Global; a change anywhere moves the whole solution |
| Shooting method | Not applicable | Reduces it to an IVP by tuning the unknown start value |

$$\boxed{\text{IVP: conditions at one end, march forward. BVP: conditions at both ends, solve together.}}$$

**Finite difference form for a second-order BVP.** Discretise the interval into
$n+1$ points, replace $y''$ by the centred difference, and use the boundary
conditions to replace the two unavailable end rows:

$$
\begin{cases}
y_0 = \text{given}, \\
y_{i-1} - (2 - p(x_i)h^2 - q(x_i)h^4)\,y_i + y_{i+1} = r_i h^2, \quad 1 \le i \le n-1 \\
y_n = \text{given}
\end{cases}
$$

> [!note] Why the distinction is not academic
> Marching forward is cheap but only works **one way**. A BVP has no starting
> value, so the discretisation produces a tridiagonal system that must be solved
> as a whole.
>
> The **shooting method** bridges the gap: treat the unknown start value as the
> unknown, march forward as an IVP, measure the error at the far end, and adjust.
> That converts a BVP into a root-find on one number, which is why shooting works
> with any ODE solver. It is also why shooting is fragile when the ODE is
> unstable: the forward solution amplifies, and the adjustment needed becomes
> exponentially large.

---

---

**Also asked here.**

- *2024 Q.4(a)* is the same question as [[NM-8.8_Boundary_Value_Problems|NM-8.8]], which is written in `NM-8.8`.

---

<a id="nm-82"></a><a id="nm-8.2"></a>
## NM-8.2 · Euler's Method

### [2019 Q.7(c)]

**Question.** Discuss Euler's method to solve ordinary differential equations.

*[Marks: 04]*

**Solution.**

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

$$\boxed{y_{n+1} = y_n + h\,f(x_n, y_n), \qquad \text{global error } O(h)}$$

**Merits and demerits.**

1. **Simple.** One evaluation of $f$ per step, and no derivative of $f$ is needed.
2. **Stable only for a sufficiently small $h$** on a stiff equation, because the
   method follows the tangent rather than the curve.
3. **Inexact.** The global error falls only linearly in $h$, so high accuracy
   requires many steps.
4. **It is the foundation of the higher methods.** Heun, the mid-point method, and
   the Runge-Kutta family all correct Euler's $\dfrac{h^2}{2}y''$ term.

> [!note] The distinction that makes Euler usable anyway
> **Local** truncation error is $O(h^2)$; **global** error is $O(h)$. The step is to
> be taken as the second term of the Taylor series and the answer as a sum of $n$
> steps, and the two orders differ by one because the local errors accumulate
> over $n \approx \frac{1}{h}$ steps.
>
> So the global error behaves as $n \cdot h^2 \approx h$, and that is why halving
> $h$ only halves the error. **Every first-order method behaves this way**, and
> recognising the local/global distinction is what makes the accuracy claims of
> any method predictable rather than memorised.

> [!warning] Why the tangent is the whole problem
> Euler takes the slope at the **left** endpoint of the interval and assumes it
> holds across the whole interval. For a convex solution the tangent lies below
> the curve, so every iterate **under-reads**, and the gap is exactly the discarded
> $\dfrac{h^2}{2}y''$.
>
> That gives a free diagnostic: when an Euler result disagrees with an exact or
> series solution, the sign of the disagreement should be the sign of the
> curvature. Part (a) is the case where this is used deliberately.

---

### [2020 Q.7(b)]

**Question.** Solve, by Euler's method, the equation $\frac{dy}{dx} = x + y, \; y(0) = 0$. Choose $h = 0.2$ and compute $y(0.4)$ and $y(0.6)$.

*[Marks: 04]*

**Solution.**

**Step 1. The method.** With $f(x, y) = x + y$ and $h = 0.2$,

$$y_{n+1} = y_n + 0.2(x_n + y_n), \qquad x_{n+1} = x_n + 0.2$$

Start at $x_0 = 0$, $y_0 = 0$.

**Step 2. Three steps.**

| Step | $x_n$ | $y_n$ | Slope $x_n + y_n$ | $y_{n+1} = y_n + 0.2 \times \text{slope}$ |
| --: | --: | --: | --: | --: |
| 1 | 0.0 | 0.000000 | $0.0 + 0.0 = 0.0$ | $0.0 + 0.2(0) = 0.000000$ |
| 2 | 0.2 | 0.000000 | $0.2 + 0.0 = 0.2$ | $0.0 + 0.2(0.2) = 0.040000$ |
| 3 | 0.4 | 0.040000 | $0.4 + 0.04 = 0.44$ | $0.04 + 0.2(0.44) = 0.128000$ |

Step 1 in full: the slope at $x = 0$ is $0 + 0 = 0$, so $y_1 = 0 + 0.2(0) = 0$.
The curve leaves the origin horizontally, which is correct since $y' = x + y$ is
zero at the origin.

$$\boxed{y(0.4) = 0.0400, \qquad y(0.6) = 0.1280 \quad (h = 0.2)}$$

> [!info] Check against the exact solution
> The equation is linear: $\frac{dy}{dx} - y = x$. A particular solution is
> $y_p = -x - 1$ and the homogeneous solution is $Ce^x$, so
> $$y = Ce^x - x - 1$$
> and $y(0) = 0$ gives $C = 1$:
> $$y = e^x - x - 1$$
> Check: $y' = e^x - 1$ and $x + y = x + e^x - x - 1 = e^x - 1$. They match.
>
> | $x$ | Exact | Euler $h=0.2$ | Error | Euler $h=0.1$ | Error |
> | --: | --: | --: | --: | --: | --: |
> | 0.4 | 0.091825 | 0.040000 | $-0.051825$ | 0.064100 | $-0.027725$ |
> | 0.6 | 0.222119 | 0.128000 | $-0.094119$ | 0.171561 | $-0.050558$ |
>
> Halving the step from $0.2$ to $0.1$ cut the error at $x = 0.4$ from $0.0518$
> to $0.0277$, a ratio of $1.87$, close to the factor of 2 that **first order**
> accuracy predicts. That confirms both the error direction and the order.
>
> **Second order for comparison.** Heun's method from Q.7(a) with $h = 0.2$ gives
> $y(0.4) = 0.088400$ and $y(0.6) = 0.215848$, with errors $-0.0034$ and $-0.0063$.
> That is **15 times** more accurate than Euler at the same step size, for one
> extra slope evaluation per step. This is the practical argument for never using
> plain Euler when the answer matters.

> [!warning] Two things that catch people
> **1. The first step gives $y_1 = 0$, and that is correct.** The slope at the
> origin is $x + y = 0$. A nonzero first step would indicate the function $x - y$
> in place of $x + y$.
>
> **2. Use the old $x$ and the old $y$ in the slope.** The update is
> $y_{n+1} = y_n + h f(x_n, y_n)$, both from step $n$. Computing the slope with
> $x_{n+1}$ or with $y_{n+1}$ mixes in the new point and quietly turns the method
> into something else. Update $y$ first, then $x$, from the saved values.
>
> **Euler always runs low here.** The exact solution is convex, $y'' = e^x > 0$,
> and Euler's method uses a tangent that lies below a convex curve, so every
> iterate under-reads. **Euler under-reads an increasing convex solution.** So an
> overshoot on such a solution points to an arithmetic error, not to a method
> error.

---

### [2021 Q.8(c), 2023 Q.3(b)]

**Appeared in:** 2021 Q.8(c), 2023 Q.3(b)

**Question.** Using Euler's method, determine $\frac{dy}{dx} = \frac{3}{5}x^3 y$; Consider $y(0) = 1$.

*[Marks: 04, CO: 3]*

**Solution.**

> [!warning] A gap in the printed question
> No step size $h$ and no interval are given, so numbers cannot be produced
> without a stated choice. Use $h = 0.25$ and $x: 0 \to 1$, and say so. The exact
> solution is provided below so the answer can be judged at any step size.

**The method.**

$$
y_{n+1} = y_n + h\,f(x_n, y_n) = y_n + h\cdot\frac{3}{5}x_n^3 y_n
$$

**Step 1.** At $x_0 = 0$, $y_0 = 1$: slope $\frac{3}{5}(0)^3(1) = 0$, so
$y_1 = 1 + 0.25(0) = 1.0000000$.

**Step 2.** At $x_1 = 0.25$, $y_1 = 1$: slope
$\frac{3}{5}(0.25)^3(1) = \frac{3}{5}(0.015625) = 0.0093750$, so
$y_2 = 1 + 0.25(0.009375) = 1.0023438$.

**Step 3.** At $x_2 = 0.5$, $y_2 = 1.0023438$: slope
$\frac{3}{5}(0.5)^3(1.0023438) = \frac{3}{5}(0.125)(1.0023438) = 0.0751758$, so
$y_3 = 1.0023438 + 0.25(0.0751758) = 1.0211377$.

**Step 4.** At $x_3 = 0.75$, $y_3 = 1.0211377$: slope
$\frac{3}{5}(0.75)^3(1.0211377) = \frac{3}{5}(0.421875)(1.0211377) = 0.2584755$, so
$y_4 = 1.0211377 + 0.25(0.2584755) = 1.0857566$.

| Step | $x_n$ | $y_n$ | Slope $\frac{3}{5}x_n^3y_n$ | $y_{n+1}$ |
| --: | --: | --: | --: | --: |
| 1 | 0.00 | 1.0000000 | 0.0000000 | 1.0000000 |
| 2 | 0.25 | 1.0000000 | 0.0093750 | 1.0023438 |
| 3 | 0.50 | 1.0023438 | 0.0751758 | 1.0211377 |
| 4 | 0.75 | 1.0211377 | 0.2584755 | 1.0857566 |

$$\boxed{y(1) \approx 1.08576 \quad (h = 0.25)}$$

**Other step sizes**, to show the choice is not arbitrary:

| $h$ | Steps to $x=1$ | $y(1)$ | Error against exact |
| --: | --: | --: | --: |
| 0.5 | 2 | 1.03750 | $-0.12433$ |
| 0.25 | 4 | 1.08576 | $-0.07608$ |
| 0.1 | 10 | 1.12725 | $-0.03459$ |

> [!info] Check against the exact solution
> The equation is separable: $\frac{dy}{y} = \frac{3}{5}x^3dx$, so
> $\ln y = \frac{3}{20}x^4 + C$, and $y(0) = 1$ gives $C = 0$.
> $$y = e^{\frac{3}{20}x^4} = e^{0.15x^4}$$
> At $x = 1$: $e^{0.15} = 1.1618342$. Euler's $1.0857566$ is **low** by
> $0.0760777$, which is expected: Euler always undershoots when the solution is
> convex and increasing. Differentiating once more,
> $$y' = \frac{3}{5}x^3 y, \qquad y'' = \frac{9}{5}x^2 y + \frac{3}{5}x^3\cdot\frac{3}{5}x^3 y = \frac{9}{25}x^2(x^4 + 5)\,y$$
> which is positive for every $x \ne 0$, since $y > 0$.

> [!warning] The zero first step is not a mistake
> Step 1 gives $y_1 = 1.0000000$, identical to $y_0$. That is because the slope is
> $\frac{3}{5}x^3y$ and $x_0 = 0$.
>
> A step that produces no change looks like a failure and is not one here. The
> right response is to check the **slope**, not the step: a zero slope at $x = 0$
> for a function containing $x^3$ is exactly right, and it also tells you
> immediately that all the growth happens in the last few steps.
>
> Compare the slope column: $0$, $0.0094$, $0.0752$, $0.2585$. The last step
> contributes most of the answer, which is a strong hint that the coarse steps are
> wasting most of their accuracy.

> [!note] First order accuracy confirmed
> Halving $h$ from $0.5$ to $0.25$ cut the error from $0.12433$ to $0.07608$, a
> ratio of $1.63$ rather than the expected 2, because four steps of a stiffly
> growing function do not sit neatly in the asymptotic range yet. Halving again to
> $h = 0.1$ gives $0.03459$, and $0.07608/0.03459 = 2.20$, which is the expected
> factor of 2 as $h \to 0$. Euler is first order: halving the step halves the
> error.

> [!note] This is the same question as 2023 Q.3(b), the first of its two parts
> Identical ODE and identical initial condition. The only differences are the step
> size and the interval, neither of which the paper prints. That makes it a clean
> L2 merge under the plan's rule: same method, same structure, only the target
> step changed. Both papers need the same missing choice of $h$ and interval, so
> answering this one twice is an opportunity to state the choice once and be
> explicit about it.

---

---

**Also asked here.**

- *2018 Q.8(b)* is the same question as [[NM-8.6_Higher_Order_and_Systems_of_ODEs|NM-8.6]], which is written in `NM-8.6`.
- *2020 Q.7(a)* is the same question as [[NM-8.3_Modified_Euler_and_Heuns_Method|NM-8.3]], which is written in `NM-8.3`.

---

<a id="nm-83"></a><a id="nm-8.3"></a>
## NM-8.3 · Modified Euler / Heun's Method

### [2017 Q.8(a)]

**Question.** Given the differential equation: $\frac{dy}{dx} = x^2 + y$ with $y(0) = 1$, compute $y(0.02)$ using Euler's modified method.

*[Marks: 05]*

**Solution.**

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

### [2018 Q.7(a)]

**Question.** Solve $\frac{dy}{dx} = 1 - y$ with the initial condition $x = 0, y = 0$ by using modified Euler's method. Tabulate the solutions at $x = 0.1, 0.2, 0.3$.

*[Marks: 06]*

**Solution.**

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

### [2020 Q.7(a)]

**Question.** Derive modified Euler's method. What is the major limitation of Euler's method?

*[Marks: 04]*

**Solution.**

**Euler's method, for reference.** For $\frac{dy}{dx} = f(x, y)$ with
$y(x_0) = y_0$ and step $h$,

$$y_{n+1} = y_n + h f(x_n, y_n)$$

It takes the slope at the **left** endpoint of the interval and assumes it holds
across the whole interval. The local truncation error is $O(h^2)$ and the global
error is $O(h)$, so the method is **first order**.

**Step 1. The idea of the modification.** Euler's weakness is that it uses only
one slope per step and that slope is at the wrong end. Average two slopes, one at
each end of the interval, and the error drops by a whole order.

**Step 2. Compute the slope at the left end.** Predict with plain Euler:

$$y_p = y_n + h f(x_n, y_n)$$

**Step 3. Compute the slope at the right end**, using that predicted value:

$$f_{n+1} = f(x_n + h, y_p)$$

**Step 4. Average the two slopes and take the step.**

$$\boxed{y_{n+1} = y_n + \frac{h}{2}\left[f(x_n, y_n) + f(x_n + h, y_n + h f(x_n, y_n))\right]}$$

$$\boxed{y_{n+1} = y_n + \frac{h}{2}\left[f(x_n,y_n) + f(x_n+h,\, y_n + h f(x_n,y_n))\right],\quad \text{second order}}$$

> [!note] Why averaging two slopes buys a whole order
> Euler takes one slope and lets it hold across the interval. The error is the
> difference between the true curve and the straight line, which is $O(h^2)$ per
> step. Heun's method takes the average of the left slope and a right-end slope, and
> the difference between the trapezoid of slopes and the true curve is $O(h^3)$ per
> step. Over $n$ steps with $h \approx (b-a)/n$ that is a global $O(h^2)$.
>
> The price is one extra function evaluation per step. That is the whole trade,
> and Q.7(b) below measures it: about 15 times more accurate for twice the work.

**The major limitation of Euler's method.**

**The major limitation is that the method is only first order**, so the global
error is $O(h)$: halving $h$ only halves the error.

> [!warning] The limitation is the accuracy, not the stability
> Students often say Euler is "unstable". It is not, in the usual sense. The
> characteristic that actually limits it is that its global error is $O(h)$, so
> reaching six correct digits costs about a million steps instead of about a
> hundred.
>
> That is a practical ceiling, not a correctness one. Euler converges; it simply
> refuses to converge quickly.
>
> **The cost of the first order is brutal.** Halving $h$ doubles the number of steps
> and halves the error, so getting one more digit costs twice the work. Going from
> three digits to six costs a factor of $1000$ in function evaluations. Compare
> RK4, where each halving gains two digits, so the same nine digits cost a factor
> of $32$ in steps and $64$ in evaluations.

> [!note] Heun's method is also called the improved Euler, the modified Euler, and
> RK2. All four names refer to the same recursion.
>
> The genuinely confusing one is **"modified Euler"**, because some textbooks use
> it for a *different* scheme: the midpoint method, where the right-end slope is
> taken at $x_n + \tfrac{h}{2}$ rather than at the Euler prediction. Both are second
> order and both are called "modified Euler".
>
> **Read the recursion, not the name.** The formula in the box above is
> unambiguous, and if an exam asks to "derive" it, the derivation settles which
> scheme is meant.

---

<a id="nm-84"></a><a id="nm-8.4"></a>
## NM-8.4 · Runge-Kutta 2nd Order

### [2020 Q.7(c)]

**Question.** Given, $\frac{dy}{dx} = y - x$, where $y(0) = 2$, find $y(0.1)$ and $y(0.2)$ by using Runge-Kutta second order formula.

*[Marks: 04]*

**Solution.**

**Step 1. The method.** For $\frac{dy}{dx} = f(x,y)$ with $y(x_0) = y_0$ and step
$h$, the second-order Runge-Kutta method is

$$
k_1 = h f(x_n, y_n), \qquad k_2 = h f\left(x_n + h, \; y_n + k_1\right), \qquad y_{n+1} = y_n + \frac{1}{2}(k_1 + k_2)
$$

Here $f(x,y) = y - x$ and the paper gives no step size. Two steps are needed to
reach $0.2$, so take $h = 0.1$, which also matches the requested output points.
Start at $x_0 = 0$, $y_0 = 2$.

**Step 2. Step 1: $x_0 = 0$ to $x_1 = 0.1$.**

$$k_1 = 0.1 f(0, 2) = 0.1(2 - 0) = 0.2$$

$$k_2 = 0.1 f(0 + 0.1, \; 2 + 0.2) = 0.1(2.2 - 0.1) = 0.1(2.1) = 0.21$$

$$y_1 = 2 + \frac{0.2 + 0.21}{2} = 2 + 0.205 = 2.205000$$

**Step 3. Step 2: $x_1 = 0.1$ to $x_2 = 0.2$.**

$$k_1 = 0.1 f(0.1, 2.205) = 0.1(2.205 - 0.1) = 0.1(2.105) = 0.2105$$

$$k_2 = 0.1 f(0.1 + 0.1, \; 2.205 + 0.2105) = 0.1(2.4155 - 0.2) = 0.1(2.2155) = 0.22155$$

$$y_2 = 2.205 + \frac{0.2105 + 0.22155}{2} = 2.205 + 0.216025 = 2.421025$$

| Step | $x_n$ | $y_n$ | $k_1$ | $k_2$ | $y_{n+1}$ |
| --: | --: | --: | --: | --: | --: |
| 1 | 0.0 | 2.000000 | 0.200000 | 0.210000 | 2.205000 |
| 2 | 0.1 | 2.205000 | 0.210500 | 0.221550 | 2.421025 |

$$\boxed{y(0.1) = 2.2050, \qquad y(0.2) = 2.4210 \quad (h = 0.1)}$$

> [!warning] RK2 here is identical to Heun, and the two $k$ values are the trap
> This is the same recursion as Q.7(a). Both $k$ values are already scaled by $h$,
> so the update is $\frac{1}{2}(k_1 + k_2)$ with **no** $h$ in front.
>
> Writing $y_{n+1} = y_n + \frac{h}{2}(k_1 + k_2)$ when $k_1$ and $k_2$ already
> contain $h$ gives an answer $h$ times too large: $2.205$ becomes $2.2205$. The
> two conventions coexist in textbooks, and the only defence is to look at whether
> $h$ appears in the definition of $k_1$.
>
> **Two conventions, one formula.** Either $k_1 = f(x_n, y_n)$ and the update is
> $y_{n+1} = y_n + \frac{h}{2}(k_1 + k_2)$, or $k_1 = h f(x_n, y_n)$ and the update
> is $y_{n+1} = y_n + \frac{1}{2}(k_1 + k_2)$. Mixing them double-counts $h$.

> [!info] Check against the exact solution
> The equation is $\frac{dy}{dx} - y = -x$. The homogeneous solution is $Ce^x$ and
> a particular solution is $y_p = x + 1$, so
> $$y = Ce^x + x + 1$$
> and $y(0) = 2$ gives $C = 1$:
> $$y = e^x + x + 1$$
> Check: $y' = e^x + 1$ and $y - x = e^x + x + 1 - x = e^x + 1$. They match.
>
> | $x$ | Exact $e^x + x + 1$ | RK2 Heun $h=0.1$ | Error |
> | --: | --: | --: | --: |
> | 0.1 | 2.20517092 | 2.20500000 | $-0.000171$ |
> | 0.2 | 2.42140276 | 2.42102500 | $-0.000378$ |
>
> RK2 is low by $0.000171$ and $0.000378$, which is the right size. For a
> second-order method the global error is $\frac{h^3}{6}\lvert y'''\rvert$, and
> $y''' = e^x$ here, so $\frac{0.001}{6}e^{0.1} = 1.84\times10^{-4}$ at $x = 0.1$
> and $2.04\times10^{-4}$ at $x = 0.2$. The observed errors match that scale, which
> is a stronger check than simply being "close".
>
> **Compare with Euler on the same problem.** Euler with $h = 0.1$ gives
> $y(0.1) = 2.2$ and $y(0.2) = 2.41$, low by $0.005171$ and $0.011403$. So RK2 is
> about **30 times** more accurate here, for one extra slope evaluation per step.
>
> **Write the check callout from the exact solution, not from memory.** The exact
> values here are $2.205171$ and $2.421403$, and they sit within $2\times10^{-4}$ of
> the RK2 answer. Any check callout reporting errors of order $10^{-2}$ would be
> describing a different ODE, and it is the kind of slip no gate catches: the box
> is unaffected either way.

> [!note] Choosing $h$ when the paper does not print one
> Here the requested output points, $0.1$ and $0.2$, make the natural choice
> obvious: $h = 0.1$ lands exactly on them with no leftover interval. Where the
> requested points do not divide the interval, say what you chose and why, and
> give the exact solution so the answer can be judged at any step size.

---

---

**Answered in phase P6, in `../CT_Questions/`.**

- *CT-02B Q.2(a)* is a class-test question. Its answer is in `../CT_Questions/CT_answers_exam_style.md`, with the reasoning in `../CT_Questions/CT_answers_explanation.md`.

---

<a id="nm-85"></a><a id="nm-8.5"></a>
## NM-8.5 · Runge-Kutta 4th Order

### [2017 Q.8(b)]

**Question.** Use Runge-Kutta fourth order formula to find $y(0.2)$ and $y(0.4)$ given that $y' = \frac{y^2 - x^2}{y^2 + x^2}, \, y(0) = 1$.

*[Marks: 05]*

**Solution.**

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

### [2018 Q.7(b)]

**Question.** Use the Runge-Kutta method to solve $10\frac{dy}{dx} = x^2 - y^2, \, y(0) = 1$ for the interval $0 < x \le 0.4$ with $h = 0.1$.

*[Marks: 06]*

**Solution.**

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

### [2019 Q.8(a)]

**Question.** Given, $\frac{dy}{dx} = x^2 + y^2$ where $y = 0$ when $x = 0$. Find $y(0.4)$ assuming $h = 0.2$.

*[Marks: 06]*

**Solution.**

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

> [!warning] Two things that look like errors and are not
> **The zero first step.** $f(0,0) = 0$, so $y_1 = 0$. The solution leaves the
> origin horizontally because $y' = x^2 + y^2$ is zero there. A nonzero first step
> would mean the $x^2$ term had been dropped.
>
> **The tiny answer.** $0.008$ against an exact $0.0214$ looks like a factor of
> three too small, and it is. But $y$ grows like $\frac{x^3}{3}$ here, so at
> $x = 0.4$ it *should* be small. Compare $0.008$ with $0.16$, not with $1$.

> [!info] Check against an independent route
> Iterating the integral equation gives the Picard series
> $y(x) = \dfrac{x^3}{3} + \dfrac{x^7}{63} + \cdots$, from which
> $y(0.4) \approx \dfrac{0.064}{3} + \dfrac{0.0016384}{63} = 0.021359$. Euler's
> $0.008$ is well short of this, and the reason is the method, not the arithmetic.
> Euler's error per step is $O(h^2)$ and the solution has
> $y' = x^2 + y^2$ with $y''(0) = 2$, so the discarded $\dfrac{h^2}{2}y''$ alone
> is $\dfrac{0.04}{2}\cdot 2 = 0.04$ at the first step. A step of $h = 0.2$ is
> simply too coarse for this equation; the observation that Euler under-reads by
> roughly the local truncation term is the useful diagnostic when a computed value
> is compared against an exact or series solution.

> [!note] The diagnostic, stated generally
> Euler under-reads a convex solution, and the shortfall at the first step is
> exactly the discarded term $\frac{h^2}{2}y''$. Here that term is $0.04$, which is
> five times the answer itself.
>
> **That ratio is the measure of whether the step size is usable.** When
> $\frac{h^2}{2}y''$ is comparable to $y$, the method is being asked for more than it
> can deliver, and the answer is not worth reporting to three figures. Halving $h$
> to $0.1$ and doubling the step count gives the answer to roughly twice the
> accuracy, which is exactly what a first-order method promises and no more.

---

### [2024 Q.4(b)]

**Question.** Use the fourth-order Runge-Kutta method (RK4) to solve $\frac{dy}{dx} = x + y$ with initial condition $y(0) = 1$ over the interval $x = 0$ to $x = 0.2$ with a step size $h = 0.1$. Show intermediate calculations.

*[Marks: 05, CO: 1]*

**Solution.**

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

**Answered in phase P6, in `../CT_Questions/`.**

- *CT-02B Q.2(b)* is a class-test question. Its answer is in `../CT_Questions/CT_answers_exam_style.md`, with the reasoning in `../CT_Questions/CT_answers_explanation.md`.

---

<a id="nm-86"></a><a id="nm-8.6"></a>
## NM-8.6 · Higher-Order & Systems of ODEs

### [2018 Q.8(b)]

**Question.** Use the Euler's method to solve, $\frac{d^2 y}{dt^2} - 0.5t = y$ where, $y(0) = 2$ and $y'(0) = 0$. Solve from $t = 0$ to $0.4$ using $h = 0.1$.

*[Marks: 06]*

**Solution.**

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

<a id="nm-87"></a><a id="nm-8.7"></a>
## NM-8.7 · ODE Formulation from Physical Problems

### [2021 Q.5(c)]

**Question.** A capacitor loses 4% of its remaining charge every second. It is fully charged with 100 Coulomb of charge. What will be the remaining charge after 10 sec. Develop the ODE and also determine the solution.

*[Marks: 05, CO: 2]*

**Solution.**

**Step 1. Set up the rate equation.** Losing $4\%$ of the *remaining* charge each
second means the loss is **proportional to the charge present**, not a constant
$4$ C per second. If $Q$ is the charge and $t$ the time,

$$
\frac{dQ}{dt} = -0.04\,Q, \qquad Q(0) = 100
$$

> [!warning] The phrase "of its remaining charge" is the whole question
> Two readings are available and they differ by $0.8\%$.
>
> | Reading | Value | Character |
> | :-- | --: | :-- |
> | Continuous exponential | 67.0320 | The physically correct law. Each individual decay is small, so compounding is continuous |
> | Discrete $0.96^n$ | 66.4833 | Treats each second as one exact $4\%$ step. Slightly under, since $1-0.04 < e^{-0.04}$ |
>
> The general identity is $(1-r)^n < e^{-rn}$ for $0<r<1$, so the discrete answer
> always under-reads. A capacitor really does decay continuously, so $67.0320$ is
> the intended answer, and the ODE the question asks you to develop is the
> exponential one.
>
> The trap is writing $Q' = -4$. That is a constant loss of 4 Coulombs per second,
> which would give $Q(10) = 60$ and is a different physical situation entirely.

The negative sign is essential: the charge is decreasing.

**Step 2. Solve by separation of variables.**

$$
\frac{dQ}{Q} = -0.04\,dt
$$

Integrating,

$$
\ln Q = -0.04\,t + C
$$

At $t = 0$, $\ln 100 = C$, so

$$
Q(t) = 100\,e^{-0.04t}
$$

**Step 3. Evaluate at $t = 10$ s.**

$$
Q(10) = 100\,e^{-0.4} = 100(0.670320046) = 67.0320
$$

$$\boxed{Q(10) = 67.03 \text{ Coulomb}}$$

> [!info] Check by an independent route
> **Discrete compounding.** "Loses 4% of its remaining charge every second" read
> literally gives, second by second,
> $$Q(10) = 100(0.96)^{10} = 66.4833$$
> **Euler's method** with $h = 1$, which is exactly that recursion, returns
> $Q(10) = 66.4833$ as well: $96$, $92.16$, ... $66.4833$.

> [!note] Half-life as a check
> From $Q(t) = Q_0e^{-t/\tau}$ with $\tau = 25$ s, the half-life is $\tau\ln 2 = 17.33$ s.
> So in 10 s the charge should be somewhat **more** than half of 100, which is
> exactly what 67.03 shows.
>
> A reading of 66.48 also passes that test, which is why it is worth noticing that
> a sanity check cannot separate these two readings. When two readings differ by
> less than a percent, the check has to be a different method rather than a
> plausibility test.

> [!note] Generalising the form
> Every first-order decay problem has the shape $Q' = -kQ$ with
> $Q(t) = Q_0e^{-kt}$, and the two useful numbers are the time constant $\tau = 1/k$
> and the half-life $\frac{\ln 2}{k}$. Working in half-lives is often easier than
> working in $e$'s: at 10 s the capacitor has been discharging for
> $10/17.33 = 0.577$ half-lives, so it holds $2^{-0.577} = 0.670$ of its charge.

---

<a id="nm-88"></a><a id="nm-8.8"></a>
## NM-8.8 · Boundary Value Problems

### [2021 Q.5(b)]

**Question.** Solve the boundary value problem $\frac{d^2y}{dx^2} - y = 0$ with $y(0) = 0$ and $y(2) = 3.62686$.

*[Marks: 05, CO: 3]*

**Solution.**

**Step 1. Discretise.** With the centred difference for $y''$,

$$
\frac{y_{i-1} - 2y_i + y_{i+1}}{h^2} - y_i = 0
$$

Multiplying by $h^2$,

$$
y_{i-1} - (2 + h^2)\,y_i + y_{i+1} = 0
$$

The system is tridiagonal with diagonal $-(2+h^2)$ and off-diagonal $1$.

> [!note] Check the sign and the dominance before iterating
> The matrix is **negatively diagonally dominant**, since $\lvert 2+h^2\rvert > 1+1$
> for every $h$. That guarantees a unique solution and means the standard Thomas
> algorithm applies **without pivoting**.
>
> Worth pausing on, because it is the first question in this paper where the sign
> of $y_i$ on the diagonal is decided by the ODE rather than by taste. $y'' - y = 0$
> gives $\frac{y_{i-1}-2y_i+y_{i+1}}{h^2} = y_i$, and moving $y_i$ across gives a
> diagonal of $-(2+h^2)$, not $+(2+h^2)$. Writing the positive sign produces a
> system with a completely different spectrum and, for this $y(2)$, no consistent
> solution.

**Step 2. Solve with $h = 0.5$.** Then $n = 4$ subintervals and 3 interior nodes
at $x = 0.5, 1.0, 1.5$. With $y_0 = 0$ and $y_4 = 3.62686$:

$$
\begin{cases}
-(2.25)y_1 + y_2 = 0 \\
y_1 - (2.25)y_2 + y_3 = 0 \\
y_2 - (2.25)y_3 = -3.62686
\end{cases}
$$

From the first, $y_2 = 2.25\,y_1$. Substituting into the second,

$$
y_1 - 2.25(2.25y_1) + y_3 = 0 \Rightarrow y_3 = 4.0625\,y_1
$$

The third then gives $2.25y_1 - 2.25(4.0625y_1) = -3.62686$, that is
$2.25y_1(1 - 4.0625) = -3.62686$, so $-6.890625\,y_1 = -3.62686$ and
$y_1 = 0.526347$.

$$
y_2 = 2.25(0.526347) = 1.184281, \qquad y_3 = 4.0625(0.526347) = 2.138285
$$

| $x$ | $y$ (numerical, $h = 0.5$) | Exact | Error |
| --: | --: | --: | --: |
| 0.5 | 0.526347 | 0.521095 | $+0.005252$ |
| 1.0 | 1.184281 | 1.175201 | $+0.009080$ |
| 1.5 | 2.138285 | 2.129279 | $+0.009006$ |

$$\boxed{y(0.5) = 0.5263,\quad y(1.0) = 1.1843,\quad y(1.5) = 2.1383 \quad (h = 0.5)}$$

**Step 3. Refine.** Halving $h$ should cut the error by about 4, since the scheme is
second order.

| $h$ | Interior nodes | Largest error |
| --: | --: | --: |
| 1 | 1 | 0.03375 |
| 0.5 | 3 | 0.00908 |
| 0.25 | 7 | 0.00249 |
| 0.125 | 15 | 0.00063 |

The ratio $0.00908 / 0.00249 = 3.65$ is close to the expected 4, confirming
second-order accuracy.

> [!info] Check against the continuous solution
> The ODE $y'' - y = 0$ has the general solution $y = A\cosh x + B\sinh x$. From
> $y(0) = 0$, $A = 0$. From $y(2) = 3.62686$,
> $$B = \frac{3.62686}{\sinh 2} = \frac{3.62686}{3.6268604} = 0.99999989$$
> so
> $$y = 3.62686\,\frac{\sinh x}{\sinh 2}$$
> Exact values at the three interior nodes are $0.521095$, $1.175201$ and
> $2.129279$. The numerical values overshoot by under $1\%$, as expected for a
> second-order scheme on a growing exponential.

> [!warning] The halving ratio is the check that the order is what you think
> The four rows of the refinement table are not decoration; they are the only
> evidence that the scheme is second order. A ratio near 4 means the
> $O(h^2)$ term dominates. A ratio near 2 would mean the scheme is only first
> order, and a ratio near 8 or 16 would mean something is wrong with the
> difference stencil rather than right about it.
>
> $3.65$ rather than exactly $4$ is expected: at $h = 0.5$ there are only three
> interior nodes, so higher-order terms have not yet died away.

> [!note] Why the boundary value is suspicious, and what it tells you
> The printed $y(2) = 3.62686$ is a rounded value: $\sinh 2 = 3.6268604\ldots$
> gives $B$ exactly $1$ to seven figures, so the intended exact solution is almost
> certainly $y = \sinh x$. That is a strong hint the question was built backwards
> from a known answer.
>
> It also means the "error" quoted above is almost entirely scheme error, not the
> $4 \times 10^{-7}$ rounding in the boundary condition. With the exact condition
> $y(2) = \sinh 2$, the $h = 0.5$ numerical solution is $0.52634$ against an exact
> $0.52109$, and the same $0.9\%$ gap remains. So the gap is real and belongs to
> the scheme.

---

### [2024 Q.4(a)]

**Question.** Describe the general approach for solving boundary value problems numerically. How does it differ from solving initial value problems?

*[Marks: 03, CO: 1]*

**Solution.**

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

[🏠 Master Index](00_Index.md) | [← Prev Topic: NM-7 · Numerical Differentiation](NM-7_Numerical_Differentiation.md) | [Next Topic: NM-9 · Eigenvalues & Eigenvectors →](NM-9_Eigenvalues_and_Eigenvectors.md)
