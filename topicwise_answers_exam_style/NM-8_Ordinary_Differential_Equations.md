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
> **Origin Layer:** Authored in `../answers_exam_style/`. All numerical results and boxed equations match character-for-character.

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

**Finite difference form for a second-order BVP.** Discretise the interval into
$n+1$ points, replace $y''$ by the centred difference, and use the boundary
conditions to replace the two unavailable end rows:

$$
\frac{y_{i-1} - 2y_i + y_{i+1}}{h^2} + p(x_i)y_i + q(x_i)y_i = r_i
$$

$$
\begin{cases}
y_0 = \text{given}, \\
y_{i-1} - (2 - p(x_i)h^2 - q(x_i)h^4)\,y_i + y_{i+1} = r_i h^2, \quad 1 \le i \le n-1 \\
y_n = \text{given}
\end{cases}
$$

$$
\boxed{\text{IVP: conditions at one end, march forward. BVP: conditions at both ends, solve together.}}
$$

---

---

**Also asked here.**

- *2024 Q.4(a)* is the same question as [[NM-8.8_Boundary_Value_Problems|NM-8.8]], which is written in `NM-8.8`.

---

<a id="nm-82"></a><a id="nm-8.2"></a>
## NM-8.2 · Euler's Method

### [2019 Q.7(c)]

**Question.** Discuss Euler's method to solve ordinary differential equations.

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

### [2020 Q.7(b)]

**Question.** Solve, by Euler's method, the equation $\frac{dy}{dx} = x + y, \; y(0) = 0$. Choose $h = 0.2$ and compute $y(0.4)$ and $y(0.6)$.

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

Step 2: $y_2 = 0.04$. Step 3: $y_3 = 0.128$.

$$
\boxed{y(0.4) = 0.0400, \qquad y(0.6) = 0.1280 \quad (h = 0.2)}
$$

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
> Halving the step from $0.2$ to $0.1$ cut the error at $x = 0.4$ from
> $0.0518$ to $0.0277$, a ratio of $1.87$, close to the factor of 2 that
> **first order** accuracy predicts. That confirms both the error direction and
> the order.
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
> **Euler always runs low here.** The exact solution is convex,
> $y'' = e^x > 0$, and Euler's method uses a tangent that lies below a convex
> curve, so every iterate under-reads. That is a general property worth
> **Euler under-reads an increasing convex solution.** So an overshoot on such a
> solution points to an arithmetic error, not to a method error.

---

### [2021 Q.8(c), 2023 Q.3(b)]

**Appeared in:** 2021 Q.8(c), 2023 Q.3(b)

**Question.** Using Euler's method, determine $\frac{dy}{dx} = \frac{3}{5}x^3 y$; Consider $y(0) = 1$.

**Solution.**

> [!note] A gap in the printed question
> No step size $h$ and no interval are given, so numbers cannot be produced without
> a stated choice. Use $h = 0.25$ and $x: 0 \to 1$, and say so. The exact solution is
> provided below so the answer can be judged at any step size.

**The method.**

$$
y_{n+1} = y_n + h\,f(x_n, y_n) = y_n + h\cdot\frac{3}{5}x_n^3 y_n
$$

**Step 1. Step 1**, at $x_0 = 0$, $y_0 = 1$: slope $\frac{3}{5}(0)^3(1) = 0$, so
$y_1 = 1 + 0.25(0) = 1.0000000$.

**Step 2. Step 2**, at $x_1 = 0.25$, $y_1 = 1$: slope
$\frac{3}{5}(0.25)^3(1) = \frac{3}{5}(0.015625) = 0.0093750$, so
$y_2 = 1 + 0.25(0.009375) = 1.0023438$.

**Step 3. Step 3**, at $x_2 = 0.5$, $y_2 = 1.0023438$: slope
$\frac{3}{5}(0.5)^3(1.0023438) = \frac{3}{5}(0.125)(1.0023438) = 0.0751758$, so
$y_3 = 1.0023438 + 0.25(0.0751758) = 1.0211377$.

**Step 4. Step 4**, at $x_3 = 0.75$, $y_3 = 1.0211377$: slope
$\frac{3}{5}(0.75)^3(1.0211377) = \frac{3}{5}(0.421875)(1.0211377) = 0.2584755$, so
$y_4 = 1.0211377 + 0.25(0.2584755) = 1.0857566$.

| Step | $x_n$ | $y_n$ | Slope $\frac{3}{5}x_n^3y_n$ | $y_{n+1}$ |
| --: | --: | --: | --: | --: |
| 1 | 0.00 | 1.0000000 | 0.0000000 | 1.0000000 |
| 2 | 0.25 | 1.0000000 | 0.0093750 | 1.0023438 |
| 3 | 0.50 | 1.0023438 | 0.0751758 | 1.0211377 |
| 4 | 0.75 | 1.0211377 | 0.2584755 | 1.0857566 |

$$
\boxed{y(1) \approx 1.08576 \quad (h = 0.25)}
$$

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
> step changed.

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

**Solution.**

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

### [2018 Q.7(a)]

**Question.** Solve $\frac{dy}{dx} = 1 - y$ with the initial condition $x = 0, y = 0$ by using modified Euler's method. Tabulate the solutions at $x = 0.1, 0.2, 0.3$.

**Solution.**

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

### [2020 Q.7(a)]

**Question.** Derive modified Euler's method. What is the major limitation of Euler's method?

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

$$
\boxed{y_{n+1} = y_n + \frac{h}{2}\left[f(x_n, y_n) + f(x_n + h, y_n + h f(x_n, y_n))\right]}
$$

This is **Heun's method**, also called the **improved Euler method** or the
**trapezoidal method**. Another name for it is the **two-stage second-order
Runge-Kutta method**, since the $k$ values below reproduce it exactly.

**Step 5. The Runge-Kutta form**, to show where it comes from. With
$k_1 = h f(x_n, y_n)$ and $k_2 = h f(x_n + h, y_n + k_1)$,

$$y_{n+1} = y_n + \frac{1}{2}(k_1 + k_2)$$

**Step 6. Accuracy.** The two-slope average cancels the leading local error
term, so the local truncation error becomes $O(h^3)$ and the global error becomes
$O(h^2)$. The method is now **second order**: halving $h$ cuts the error by 4
instead of 2. The cost is one extra function evaluation per step, so roughly
double the work for one extra order of accuracy. That is nearly always worth it.

**The major limitation of Euler's method.**

> **Euler's method is first order accurate, so it needs far too many steps for
> the accuracy usually wanted, and it goes unstable when $h$ exceeds a stability
> limit.**

Two parts, and the second is the serious one.

1. **Low order.** Global error $O(h)$. Reaching four correct digits with
   $h = 10^{-4}$ means $10^4$ steps, and the accumulated round off grows with
   the step count, so the gain flattens out.

2. **Conditional stability.** For the test equation $y' = \lambda y$ with
   $\lambda < 0$, Euler gives $y_{n+1} = (1 + h\lambda)y_n$. Stability needs
   $\lvert 1 + h\lambda\rvert < 1$, that is
   $$h < \frac{2}{\lvert\lambda\rvert}$$
   and for a stiff system $\lvert\lambda\rvert$ is enormous, so $h$ must be
   tiny. Meanwhile the truncation error wants $h$ small too, so the two demands
   are compatible but expensive, and any step-size increase blows the solution up
   with no warning.

**Practical note.** Heun's method is not unconditionally stable either. For
$y' = \lambda y$ it gives $y_{n+1} = (1 + z + z^2/2)y_n$ with $z = h\lambda$, and
stability needs $\lvert 1 + z + z^2/2\rvert < 1$, which allows
$-2 < z < 0$, a range of $2$ against Euler's $2$. It is modestly better, not a
cure. Real stiff solvers use the backward or implicit trapezoidal methods, which
have unbounded stable regions.

> [!warning] The trap: "improved" does not mean "exact"
> Two names cause confusion and neither is wrong.
>
> **Modified Euler** sometimes means Heun's method above, and sometimes means the
> **midpoint method**, which uses the slope at the midpoint of the interval:
> $$y_{n+1} = y_n + h f\left(x_n + \frac{h}{2},\ y_n + \frac{h}{2} f(x_n, y_n)\right)$$
> Both are second order, and both are called "modified Euler" in the wild. Check
> which variant a course intends before using the name.
>
> A related trap: writing $y_{n+1} = y_n + h f\left(\frac{x_n + x_{n+1}}{2}, \frac{y_n + y_{n+1}}{2}\right)$
> is **not** an algorithm at all, because $y_{n+1}$ appears on the right-hand
> side. That is an implicit formula needing a solution, not a one-step method.
> Heun's method avoids the problem by replacing $y_{n+1}$ with an Euler **predictor**
> in the slope evaluation, which is exactly the point of Step 2.

$$
\boxed{y_{n+1} = y_n + \frac{h}{2}\left[f(x_n,y_n) + f(x_n+h,\, y_n + h f(x_n,y_n))\right],\quad \text{second order}}
$$

---

<a id="nm-84"></a><a id="nm-8.4"></a>
## NM-8.4 · Runge-Kutta 2nd Order

### [2020 Q.7(c)]

**Question.** Given, $\frac{dy}{dx} = y - x$, where $y(0) = 2$, find $y(0.1)$ and $y(0.2)$ by using Runge-Kutta second order formula.

**Solution.**

**Step 1. The method.** For $\frac{dy}{dx} = f(x,y)$ with $y(x_0) = y_0$ and
step $h$, the second-order Runge-Kutta method is

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

$$
\boxed{y(0.1) = 2.2050, \qquad y(0.2) = 2.4210 \quad (h = 0.1)}
$$

> [!info] Check against the exact solution
> The equation is $\frac{dy}{dx} - y = -x$. The homogeneous solution is $Ce^x$
> and a particular solution is $y_p = x + 1$, so
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
> The errors are $-1.7\times10^{-4}$ and $-3.8\times10^{-4}$, which is the right
> size. For a second-order method the global error is
> $\frac{h^3}{6}\lvert y'''\rvert$, and $y''' = e^x$ here, so
> $\frac{0.001}{6}e^{0.1} = 1.84\times10^{-4}$ at $x = 0.1$ and
> $2.04\times10^{-4}$ at $x = 0.2$. The observed errors match that scale.
>
> **RK4 for reference.** $h = 0.1$ gives $y(0.1) = 2.20517083$ and
> $y(0.2) = 2.42140257$, agreeing with the exact solution to $8 \times 10^{-8}$.
> Raising the order improves accuracy: RK4 is correct to eight digits where
> RK2 is right to four, for four function evaluations per step against two.

> [!note] The other second-order method gives a different fourth digit
> "Runge-Kutta second order" is not one formula but a family. The **midpoint**
> method, $k_1 = hf(x_n,y_n)$, $k_2 = hf(x_n + h/2, y_n + k_1/2)$,
> $y_{n+1} = y_n + k_2$, gives the **same** first step, $2.205000$, because at
> $x_0 = 0$ the two happen to coincide, and the same second step, $2.421025$.
>
> The **Ralston** variant, $k_1 = hf(x_n,y_n)$,
> $k_2 = hf(x_n + \frac{2}{3}h, y_n + \frac{2}{3}k_1)$,
> $y_{n+1} = y_n + \frac{1}{3}k_1 + \frac{2}{3}k_2$, gives
> $2.204444$ and $2.419798$, with errors $-7.3 \times 10^{-4}$ and
> $-1.6 \times 10^{-3}$. All three are second order, so all three converge at the
> same rate, but the constants differ and Ralston is about twice as far off here.
>
> **Heun's method is the one to write.** It is the most common textbook choice, it
> is the same method as in Q.7(a), and here it is the most accurate of the three.
> Never mix two second-order formulas in one answer, and never average three
> different RK2 answers hoping to land near the right one.

> [!warning] Three traps
> **1. No step size is printed.** Two output points with a second-order method
> means two steps, so $h = 0.1$ is the natural reading, and it happens to match
> the requested values. If a different $h$ were intended, RK2 with $h = 0.2$ would
> give only one value at $x = 0.2$, and RK2 needs the same $h$ used for both
> outputs. **State the choice.**
>
> **2. $f(x,y) = y - x$, not $x - y$.** The two have different solutions entirely.
> Here $f = y - x$, so $f(0, 2) = 2$, and $k_1 = 0.2$. Getting the sign of $x$
> wrong gives a completely different sequence.
>
> **3. Use $y_n + k_1$ in $k_2$, not $y_n$.** The second slope is evaluated at
> the **end** of the step, at the predicted value $y_n + k_1$. Substituting $y_n$
> makes $k_2 = k_1$ and the method collapses to plain Euler, which for this
> equation would give $2.2$ and $2.41$ by a wrong route and a wrong reason. The
> $x$ in the second slope must also be $x_n + h$, not $x_n$.

---

**Answered in phase P6, in `../CT_Questions/`.**

- *CT-02B Q.2(a)* is a class-test question. Its answer is in `../CT_Questions/CT_answers_exam_style.md`, with the reasoning in `../CT_Questions/CT_answers_explanation.md`.

---

<a id="nm-85"></a><a id="nm-8.5"></a>
## NM-8.5 · Runge-Kutta 4th Order

### [2017 Q.8(b)]

**Question.** Use Runge-Kutta fourth order formula to find $y(0.2)$ and $y(0.4)$ given that $y' = \frac{y^2 - x^2}{y^2 + x^2}, \, y(0) = 1$.

**Solution.**

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

### [2018 Q.7(b)]

**Question.** Use the Runge-Kutta method to solve $10\frac{dy}{dx} = x^2 - y^2, \, y(0) = 1$ for the interval $0 < x \le 0.4$ with $h = 0.1$.

**Solution.**

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

### [2019 Q.8(a)]

**Question.** Given, $\frac{dy}{dx} = x^2 + y^2$ where $y = 0$ when $x = 0$. Find $y(0.4)$ assuming $h = 0.2$.

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

### [2024 Q.4(b)]

**Question.** Use the fourth-order Runge-Kutta method (RK4) to solve $\frac{dy}{dx} = x + y$ with initial condition $y(0) = 1$ over the interval $x = 0$ to $x = 0.2$ with a step size $h = 0.1$. Show intermediate calculations.

**Solution.**

**The method.** With $f(x, y) = x + y$ and $h = 0.1$:

$$
k_1 = h f(x_i, y_i)
$$

$$
k_2 = h f\left(x_i + \frac{h}{2},\ y_i + \frac{k_1}{2}\right)
$$

$$
k_3 = h f\left(x_i + \frac{h}{2},\ y_i + \frac{k_2}{2}\right)
$$

$$
k_4 = h f\left(x_i + h,\ y_i + k_3\right)
$$

$$
y_{i+1} = y_i + \frac{1}{6}\left(k_1 + 2k_2 + 2k_3 + k_4\right)
$$

Each $k$ is a slope over a different point of the interval, and $y_3$ and $y_4$ are
staged estimates that get corrected by later stages. This is why RK4 needs four
function evaluations where Euler needs one.

**Step 1. From $x_0 = 0$ to $x_1 = 0.1$**, with $x_0 = 0$, $y_0 = 1$:

$$
k_1 = 0.1(0 + 1) = 0.1
$$

$$
k_2 = 0.1\left(0.05 + 1 + \frac{0.1}{2}\right) = 0.1(1.1) = 0.11
$$

$$
k_3 = 0.1\left(0.05 + 1 + \frac{0.11}{2}\right) = 0.1(1.105) = 0.1105
$$

$$
k_4 = 0.1\left(0.1 + 1 + 0.1105\right) = 0.1(1.2105) = 0.12105
$$

$$
y_1 = 1 + \frac{1}{6}\left(0.1 + 2(0.11) + 2(0.1105) + 0.12105\right)
= 1 + \frac{0.66205}{6}
= 1.1103417
$$

**Step 2. From $x_1 = 0.1$ to $x_2 = 0.2$**, with $x_1 = 0.1$, $y_1 = 1.1103417$:

$$
k_1 = 0.1(0.1 + 1.1103417) = 0.1210342
$$

$$
k_2 = 0.1\left(0.15 + 1.1103417 + \frac{0.1210342}{2}\right) = 0.1(1.3208588) = 0.1320859
$$

$$
k_3 = 0.1\left(0.15 + 1.1103417 + \frac{0.1320859}{2}\right) = 0.1(1.3263846) = 0.1326385
$$

$$
k_4 = 0.1\left(0.2 + 1.1103417 + 0.1326385\right) = 0.1(1.4429802) = 0.1442980
$$

$$
y_2 = 1.1103417 + \frac{1}{6}\left(0.1210342 + 2(0.1320859) + 2(0.1326385) + 0.1442980\right)
$$

$$
= 1.1103417 + \frac{0.7947810}{6} = 1.1103417 + 0.1324635 = 1.2428051
$$

$$
\boxed{y(0.2) = 1.2428051}
$$

> [!info] Check against the exact solution
> $y' - y = x$ is linear. The homogeneous solution is $Ce^x$ and a particular
> solution is $y_p = -x - 1$, so $y = Ce^x - x - 1$. Applying $y(0) = 1$ gives
> $C = 2$, hence
> $$y = 2e^x - x - 1$$
> $$y(0.2) = 2(1.2214028) - 0.2 - 1 = 1.2428055$$
> The RK4 answer $1.2428051$ differs by $3.7 \times 10^{-7}$. For a fourth-order
> method with $h = 0.1$ over two steps this difference is the expected size,
> which supports the RK4 result.

> [!note] Order of accuracy
> RK4 carries a local truncation error of $O(h^5)$ per step. Halving $h$ cuts
> the global error by about $16$. The cost is four function evaluations per step,
> so halving $h$ doubles the work.

---

**Answered in phase P6, in `../CT_Questions/`.**

- *CT-02B Q.2(b)* is a class-test question. Its answer is in `../CT_Questions/CT_answers_exam_style.md`, with the reasoning in `../CT_Questions/CT_answers_explanation.md`.

---

<a id="nm-86"></a><a id="nm-8.6"></a>
## NM-8.6 · Higher-Order & Systems of ODEs

### [2018 Q.8(b)]

**Question.** Use the Euler's method to solve, $\frac{d^2 y}{dt^2} - 0.5t = y$ where, $y(0) = 2$ and $y'(0) = 0$. Solve from $t = 0$ to $0.4$ using $h = 0.1$.

**Solution.**

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

<a id="nm-87"></a><a id="nm-8.7"></a>
## NM-8.7 · ODE Formulation from Physical Problems

### [2021 Q.5(c)]

**Question.** A capacitor loses 4% of its remaining charge every second. It is fully charged with 100 Coulomb of charge. What will be the remaining charge after 10 sec. Develop the ODE and also determine the solution.

**Solution.**

**Step 1. Set up the rate equation.** Losing $4\%$ of the remaining charge each
second means the loss is **proportional to the charge present**, not a constant
$4$ C per second. If $Q$ is the charge and $t$ the time,

$$
\frac{dQ}{dt} = -0.04\,Q, \qquad Q(0) = 100
$$

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

$$
\boxed{Q(10) = 67.03 \text{ Coulomb}}
$$

> [!info] Check by an independent route
> **Discrete compounding.** "Loses 4% of its remaining charge every second" read
> literally gives, second by second,
> $$Q(10) = 100(0.96)^{10} = 66.4833$$
> **Euler's method** with $h = 1$, which is exactly that recursion, returns
> $Q(10) = 66.4833$ as well: $96$, $92.16$, ... $66.4833$.
>
> The continuous answer $67.0320$ is $0.8\%$ higher. Both are defensible readings
> of the question. The distinction is genuine:
>
> | Reading | Value | Character |
> | :-- | --: | :-- |
> | Continuous exponential | 67.0320 | The physically correct law. Each individual decay is small, so compounding is continuous |
> | Discrete $0.96^n$ | 66.4833 | Treats each second as one exact $4\%$ step. Slightly under, since $1-0.04 < e^{-0.04}$ |
>
> The general identity is $(1-r)^n < e^{-rn}$ for $0<r<1$, so the discrete answer
> always under-reads. A capacitor really does decay continuously, so
> $67.0320$ is the intended answer.

> [!note] Half-life as a check
> From $Q(t) = Q_0e^{-t/\tau}$ with $\tau = 25$ s, the half-life is
> $\frac{\tau \ln 2}{1} = 17.33$ s. So in 10 s the charge should be somewhat **more**
> than half of 100, which is exactly what 67.03 shows. A reading of 66.48 is also
> plausible on that test alone, which is why the two are hard to separate by
> inspection and why the cross-check above uses a different method rather than a
> sanity check.

---

<a id="nm-88"></a><a id="nm-8.8"></a>
## NM-8.8 · Boundary Value Problems

### [2021 Q.5(b)]

**Question.** Solve the boundary value problem $\frac{d^2y}{dx^2} - y = 0$ with $y(0) = 0$ and $y(2) = 3.62686$.

**Solution.**

**Step 1. Discretise.** With the centred difference for $y''$,

$$
\frac{y_{i-1} - 2y_i + y_{i+1}}{h^2} - y_i = 0
$$

Multiplying by $h^2$,

$$
y_{i-1} - (2 + h^2)\,y_i + y_{i+1} = 0
$$

The system is tridiagonal with diagonal $-(2+h^2)$ and off-diagonal $1$. Note that
the matrix is **negatively diagonally dominant**, since $\lvert 2+h^2\rvert > 1+1$,
hence the solution is unique and the standard Thomas algorithm applies without
pivoting.

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

$$
\boxed{y(0.5) = 0.5263,\quad y(1.0) = 1.1843,\quad y(1.5) = 2.1383 \quad (h = 0.5)}
$$

> [!info] Check against the continuous solution
> The ODE $y'' - y = 0$ has the general solution $y = A\cosh x + B\sinh x$. From
> $y(0) = 0$, $A = 0$. From $y(2) = 3.62686$,
> $$B = \frac{3.62686}{\sinh 2} = \frac{3.62686}{3.6268604} = 0.99999989$$
> so
> $$y = 3.62686\,\frac{\sinh x}{\sinh 2}$$
> Exact values at the three interior nodes are $0.521095$, $1.175201$ and
> $2.129279$. The numerical values overshoot by under $1\%$, as expected for a
> second-order scheme on a growing exponential.

> [!note] Why the boundary value matters
> The printed $y(2) = 3.62686$ is a rounded value: $\sinh 2 = 3.6268604\ldots$
> gives $B$ exactly $1$ to seven figures, so the intended exact solution is
> almost certainly $y = \sinh x$. That is a strong hint the question was built
> backwards from a known answer, and it means the "error" quoted above is mostly
> the $4 \times 10^{-7}$ rounding in the boundary condition, not scheme error.
>
> With the exact condition $y(2) = \sinh 2$, the $h = 0.5$ numerical solution is
> $0.52634$ against an exact $0.52109$, and the same $0.9\%$ gap remains, so the
> error really is the finite difference scheme.

---

### [2024 Q.4(a)]

**Question.** Describe the general approach for solving boundary value problems numerically. How does it differ from solving initial value problems?

**Solution.**

**The shared starting point.** Both replace derivatives by finite differences and
solve the resulting algebraic system. The difference is which equations end up in
that system.

**Initial value problem.** One condition is given at one end of the domain, for
example $y(0) = 1$. Marching step by step from there, each new row uses only the
row just computed.

$$
y_{i+1} = f(x_i, y_i) h + O(h^2)
$$

This works because the system is **lower triangular in the unknowns**. It is
simple, needs no iteration, and each step is cheap.

**Boundary value problem.** Conditions are given at **both** ends, for example
$y(0) = 0$ and $y(1) = 1$. No starting value is known, so the grid cannot be
filled row by row.

**The general approach.**

1. Discretise the domain into a grid of $n + 1$ points.
2. Replace every derivative by a finite difference, usually the centred one
   $y''(x_i) \approx \frac{y_{i+1} - 2y_i + y_{i-1}}{h^2}$.
3. Apply the boundary conditions as algebraic equations replacing the
   unavailable end rows.
4. Solve the full linear system for all unknowns at once.

$$
\begin{cases}
y_0 = 0 \\
-\dfrac{y_{i-1} - 2y_i + y_{i+1}}{h^2} = f_i, \quad 1 \le i \le n-1 \\
y_n = 1
\end{cases}
$$

The interior equations couple neighbours, so the system is **tridiagonal**. The
standard efficient methods are the Thomas algorithm, or an iterative sweep such
as Gauss-Seidel, which works because the system is diagonally dominant.

**Key differences**

| | Initial value problem | Boundary value problem |
| :-- | :-- | :-- |
| Conditions | Given at one end | Given at both ends |
| Direction | Marches forward from the start | Whole domain solved at once |
| System structure | Lower triangular | Tridiagonal |
| Cost per step | Very low | Full linear solve |
| Sensitivity | Local, errors stay near the start | Global, a change anywhere moves the whole solution |
| Shooting method | Not applicable | Reduces a BVP to an IVP by adjusting the unknown start value until the far end matches |

> [!note] Where this exam meets the topic again
> The Gauss-Seidel iteration in part (b) of Question 2 is the same algorithm used
> on the tridiagonal system here. See
> [[NM-3.5_Gauss_Seidel_Iteration|NM-3.5 · Gauss-Seidel Iteration]] and [[NM-3.8_Circuit_Applications|NM-3.8 · Circuit Applications]].

---

[🏠 Master Index](00_Index.md) | [← Prev Topic: NM-7 · Numerical Differentiation](NM-7_Numerical_Differentiation.md) | [Next Topic: NM-9 · Eigenvalues & Eigenvectors →](NM-9_Eigenvalues_and_Eigenvectors.md)
