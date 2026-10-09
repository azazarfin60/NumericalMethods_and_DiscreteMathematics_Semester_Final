---
title: "NM-8.2 · Euler's Method"
tags:
  - numerical-methods
  - discrete-mathematics
  - topicwise
---

# NM-8.2 · Euler's Method

Every block below is copied from `../answers_exam_style/`, which is the
only place an answer is authored. A number here is the same number, character
for character, as the one it came from.


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

**Question.** Using Euler's method, solve the following problems:
(i) $\frac{dy}{dx} = \frac{3}{5}x^3 y$, with $y(0) = 1$. *(2021 Q.8(c), 2023 Q.3(b)(i))*
(ii) $\frac{dy}{dx} = 1 + y^2$, with $y(0) = 0$. *(2023 Q.3(b)(ii))*

**Solution.**

> [!note] A gap in the printed questions
> Neither paper specifies a step size $h$ or upper limit $x$. Standard practice is to choose $h = 0.25$ over $x \in [0, 1]$ (4 steps) and state the choice clearly.

#### **Part (i): $\frac{dy}{dx} = \frac{3}{5}x^3 y, \quad y(0) = 1, \quad h = 0.25$**

Euler's recurrence formula:

$$y_{n+1} = y_n + h\,f(x_n, y_n) = y_n + h\cdot\left(\frac{3}{5}x_n^3 y_n\right)$$

- **Step 1 ($x_0 = 0, y_0 = 1$):** Slope $= \frac{3}{5}(0)^3(1) = 0 \implies y_1 = 1 + 0.25(0) = 1.0000000$
- **Step 2 ($x_1 = 0.25, y_1 = 1$):** Slope $= \frac{3}{5}(0.25)^3(1) = 0.0093750 \implies y_2 = 1 + 0.25(0.0093750) = 1.0023438$
- **Step 3 ($x_2 = 0.50, y_2 = 1.0023438$):** Slope $= \frac{3}{5}(0.5)^3(1.0023438) = 0.0751758 \implies y_3 = 1.0023438 + 0.25(0.0751758) = 1.0211377$
- **Step 4 ($x_3 = 0.75, y_3 = 1.0211377$):** Slope $= \frac{3}{5}(0.75)^3(1.0211377) = 0.2584755 \implies y_4 = 1.0211377 + 0.25(0.2584755) = 1.0857566$

| Step | $x_n$ | $y_n$ | Slope $\frac{3}{5}x_n^3y_n$ | $y_{n+1}$ |
| --: | --: | --: | --: | --: |
| 1 | 0.00 | 1.0000000 | 0.0000000 | 1.0000000 |
| 2 | 0.25 | 1.0000000 | 0.0093750 | 1.0023438 |
| 3 | 0.50 | 1.0023438 | 0.0751758 | 1.0211377 |
| 4 | 0.75 | 1.0211377 | 0.2584755 | 1.0857566 |

$$
\boxed{y(1) \approx 1.08576 \quad (h = 0.25)}
$$

*(Exact: $y(x) = e^{0.15 x^4} \implies y(1) = e^{0.15} \approx 1.16183$; true error $E_t = 1.16183 - 1.08576 = 0.07608$.)*

---

#### **Part (ii): $\frac{dy}{dx} = 1 + y^2, \quad y(0) = 0, \quad h = 0.25$**

Euler's recurrence:

$$y_{n+1} = y_n + h\,(1 + y_n^2)$$

- **Step 1 ($x_0 = 0, y_0 = 0$):** Slope $= 1 + 0^2 = 1.0000000 \implies y_1 = 0 + 0.25(1) = 0.2500000$
- **Step 2 ($x_1 = 0.25, y_1 = 0.25$):** Slope $= 1 + (0.25)^2 = 1.0625000 \implies y_2 = 0.25 + 0.25(1.0625) = 0.5156250$
- **Step 3 ($x_2 = 0.50, y_2 = 0.515625$):** Slope $= 1 + (0.515625)^2 = 1.2658691 \implies y_3 = 0.515625 + 0.25(1.2658691) = 0.8320923$
- **Step 4 ($x_3 = 0.75, y_3 = 0.8320923$):** Slope $= 1 + (0.8320923)^2 = 1.6923776 \implies y_4 = 0.8320923 + 0.25(1.6923776) = 1.2551867$

| Step | $x_n$ | $y_n$ | Slope $1 + y_n^2$ | $y_{n+1}$ |
| --: | --: | --: | --: | --: |
| 1 | 0.00 | 0.0000000 | 1.0000000 | 0.2500000 |
| 2 | 0.25 | 0.2500000 | 1.0625000 | 0.5156250 |
| 3 | 0.50 | 0.5156250 | 1.2658691 | 0.8320923 |
| 4 | 0.75 | 0.8320923 | 1.6923776 | 1.2551867 |

$$
\boxed{y(1) \approx 1.25519 \quad (h = 0.25)}
$$

*(Exact: $\frac{dy}{1+y^2} = dx \implies y(x) = \tan x \implies y(1) = \tan(1\text{ rad}) \approx 1.55741$; true error $E_t = 1.55741 - 1.25519 = 0.30222$. Note: $y = \tan x$ has a vertical asymptote at $x = \pi/2 \approx 1.5708$, so step sizes must remain small.)*

---

---

**Also asked here.**

- *2018 Q.8(b)* is the same question as [[NM-8.6|NM-8.6]], which is written in `NM-8.6`.
- *2020 Q.7(a)* is the same question as [[NM-8.3|NM-8.3]], which is written in `NM-8.3`.

---
