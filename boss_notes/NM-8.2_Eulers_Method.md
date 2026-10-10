[← Previous: NM-7 Numerical Differentiation](NM-7_Numerical_Differentiation.md) | [🏠 Index](00_Index.md) | [Next: NM-8.5 Runge-Kutta 4th Order →](NM-8.5_Runge_Kutta_4th_Order.md)

---

# NM-8.2: Euler's Method
> **Section:** A (Numerical Methods) | **Priority:** 🔴 | **Exam Frequency:** 5/8 years
> **Sources:** Jain Ch.8 §8.1, §8.4, Shishir Notes §03 pp.36–38

## Why This Topic Matters

Euler's method is where numerical ODE solving begins. It has appeared in 2019 (theory discussion), 2020 (worked march on $y' = x + y$), and twice in the same recycled form in 2021 and 2023. It is also the predictor inside Heun's method and RK2, so understanding exactly what Euler does and where it is wrong explains why the higher methods exist.

---

## 📝 Key Definitions

> **Step-by-step (marching) methods:** "the values of $y$ are computed by short steps ahead for equal intervals $h$ of the independent variable." — Jain, §8.1 (p. 302)

> **Euler's formula:** "Assuming that $f(x, y) = f(x_0, y_0)$ in $x_0 \le x \le x_1$, this gives Euler's formula $y_1 \approx y_0 + h f(x_0, y_0)$." — Jain, §8.4 (p. 307), Eq. (8.7a)

> **Local error for Euler:** $L_{n+1} = -\frac{1}{2} h^2 y''(\tau_n)$, where $x_n \le \tau_n \le x_{n+1}$. — Jain, §8.4.1 (p. 308), Eq. (8.10)

> **Why higher methods exist:** "The process is very slow and to obtain reasonable accuracy with Euler's method, we need to take a smaller value for $h$. Because of this restriction on $h$, the method is unsuitable for practical use and a modification of it, known as the modified Euler method, which gives more accurate results, will be described..." — Jain, §8.4 (p. 307)

---

## The Method

**Purpose.** Given $y' = f(x, y)$ and $y(x_0) = y_0$, the value of $y$ is wanted at $x_0 + nh$ for a step size $h$.

**Derivation.** Taylor expand about $x_n$:

$$
y_{n+1} = y_n + hy'_n + \frac{h^2}{2}y''_n + \cdots
$$

**Euler's method** keeps the first two terms and discards the rest:

$$
y_{n+1} = y_n + hf(x_n, y_n)
$$

Geometrically, $y_{n+1}$ is the value at $x_n + h$ of the tangent to the solution curve at $(x_n, y_n)$, so the solution is followed along successive short tangent segments.

**Procedure.** Set $x_{n+1} = x_n + h$. Starting from $(x_0, y_0)$, compute $y_1 = y_0 + hf(x_0, y_0)$, then $y_2 = y_1 + hf(x_1, y_1)$, and continue.

**Error.** The local truncation error is $O(h^2)$ per step, from the discarded $\dfrac{h^2}{2}y''$ term; over $n$ steps these accumulate into a global error $O(h)$. Halving $h$ therefore halves the global error, which is the defining property of a first-order method.

**Merits and demerits.**

1. Simple: one evaluation of $f$ per step, and no derivative of $f$ is needed.
2. Stable only for a sufficiently small $h$ on a stiff equation, because the method follows the tangent rather than the curve.
3. Inexact: the global error falls only linearly in $h$, so high accuracy requires many steps.
4. It is the foundation of the higher methods: Heun, the mid-point method, and the Runge-Kutta family all correct Euler's $\dfrac{h^2}{2}y''$ term.

$$
\boxed{y_{n+1} = y_n + h\,f(x_n, y_n), \qquad \text{global error } O(h)}
$$

> [!NOTE] The distinction that makes Euler usable anyway
> **Local** truncation error is $O(h^2)$; **global** error is $O(h)$. The step is to be taken as the second term of the Taylor series and the answer as a sum of $n$ steps, and the two orders differ by one because the local errors accumulate over $n \approx \frac{1}{h}$ steps.
>
> So the global error behaves as $n \cdot h^2 \approx h$, and that is why halving $h$ only halves the error. **Every first-order method behaves this way**, and recognising the local/global distinction is what makes the accuracy claims of any method predictable rather than memorised.

> [!WARNING] Why the tangent is the whole problem
> Euler takes the slope at the **left** endpoint of the interval and assumes it holds across the whole interval. For a convex solution the tangent lies below the curve, so every iterate **under-reads**, and the gap is exactly the discarded $\dfrac{h^2}{2}y''$.
>
> That gives a free diagnostic: when an Euler result disagrees with an exact or series solution, the sign of the disagreement should be the sign of the curvature.

---

## Worked Example (PYQ 2020): $y' = x + y$, $y(0) = 0$

> **Source:** 2020 Q.7(b) [Marks: 04]

**Question.** Solve, by Euler's method, the equation $\frac{dy}{dx} = x + y, \; y(0) = 0$. Choose $h = 0.2$ and compute $y(0.4)$ and $y(0.6)$.

**Step 1. The method.** With $f(x, y) = x + y$ and $h = 0.2$,

$$
y_{n+1} = y_n + 0.2(x_n + y_n), \qquad x_{n+1} = x_n + 0.2
$$

Start at $x_0 = 0$, $y_0 = 0$.

**Step 2. Three steps.**

| Step | $x_n$ | $y_n$ | Slope $x_n + y_n$ | $y_{n+1} = y_n + 0.2 \times \text{slope}$ |
| --: | --: | --: | --: | --: |
| 1 | 0.0 | 0.000000 | $0.0 + 0.0 = 0.0$ | $0.0 + 0.2(0) = 0.000000$ |
| 2 | 0.2 | 0.000000 | $0.2 + 0.0 = 0.2$ | $0.0 + 0.2(0.2) = 0.040000$ |
| 3 | 0.4 | 0.040000 | $0.4 + 0.04 = 0.44$ | $0.04 + 0.2(0.44) = 0.128000$ |

Step 1 in full: the slope at $x = 0$ is $0 + 0 = 0$, so $y_1 = 0 + 0.2(0) = 0$.
The curve leaves the origin horizontally, which is correct since $y' = x + y$ is zero at the origin.

$$
\boxed{y(0.4) = 0.0400, \qquad y(0.6) = 0.1280 \quad (h = 0.2)}
$$

> [!INFO] Check against the exact solution
> The equation is linear: $\frac{dy}{dx} - y = x$. A particular solution is $y_p = -x - 1$ and the homogeneous solution is $Ce^x$, so
> $$
> y = Ce^x - x - 1
> $$
> and $y(0) = 0$ gives $C = 1$:
> $$
> y = e^x - x - 1
> $$
> Check: $y' = e^x - 1$ and $x + y = x + e^x - x - 1 = e^x - 1$. They match.
>
> | $x$ | Exact | Euler $h=0.2$ | Error | Euler $h=0.1$ | Error |
> | --: | --: | --: | --: | --: | --: |
> | 0.4 | 0.091825 | 0.040000 | $-0.051825$ | 0.064100 | $-0.027725$ |
> | 0.6 | 0.222119 | 0.128000 | $-0.094119$ | 0.171561 | $-0.050558$ |
>
> Halving the step from $0.2$ to $0.1$ cut the error at $x = 0.4$ from $0.0518$ to $0.0277$, a ratio of $1.87$, close to the factor of 2 that **first order** accuracy predicts. That confirms both the error direction and the order.
>
> **Second order for comparison.** Heun's method from Q.7(a) with $h = 0.2$ gives $y(0.4) = 0.088400$ and $y(0.6) = 0.215848$, with errors $-0.0034$ and $-0.0063$. That is **15 times** more accurate than Euler at the same step size, for one extra slope evaluation per step.

> [!WARNING] Two things that catch people
> **1. The first step gives $y_1 = 0$, and that is correct.** The slope at the origin is $x + y = 0$. A nonzero first step would indicate the function $x - y$ in place of $x + y$.
>
> **2. Use the old $x$ and the old $y$ in the slope.** The update is $y_{n+1} = y_n + h f(x_n, y_n)$, both from step $n$. Computing the slope with $x_{n+1}$ or with $y_{n+1}$ mixes in the new point and quietly turns the method into something else. Update $y$ first, then $x$, from the saved values.
>
> **Euler always runs low here.** The exact solution is convex, $y'' = e^x > 0$, and Euler's method uses a tangent that lies below a convex curve, so every iterate under-reads. **Euler under-reads an increasing convex solution.** So an overshoot on such a solution points to an arithmetic error, not to a method error.

---

## 🏆 Golden Questions (Past Exam Archive)

### 🎯 Discuss Euler's method to solve ordinary differential equations.
> **Appeared:** 2019 Q.7(c) — (04 marks)

**Full Answer:**

**Purpose.** Given $y' = f(x, y)$ and $y(x_0) = y_0$, the value of $y$ is wanted at $x_0 + nh$ for a step size $h$.

**Derivation.** Taylor expand about $x_n$:

$$
y_{n+1} = y_n + hy'_n + \frac{h^2}{2}y''_n + \cdots
$$

**Euler's method** keeps the first two terms and discards the rest:

$$
y_{n+1} = y_n + hf(x_n, y_n)
$$

Geometrically, $y_{n+1}$ is the value at $x_n + h$ of the tangent to the solution curve at $(x_n, y_n)$, so the solution is followed along successive short tangent segments.

**Procedure.** Set $x_{n+1} = x_n + h$. Starting from $(x_0, y_0)$, compute $y_1 = y_0 + hf(x_0, y_0)$, then $y_2 = y_1 + hf(x_1, y_1)$, and continue.

**Error.** The local truncation error is $O(h^2)$ per step, from the discarded $\dfrac{h^2}{2}y''$ term; over $n$ steps these accumulate into a global error $O(h)$. Halving $h$ therefore halves the global error, which is the defining property of a first-order method.

**Merits and demerits.**

1. Simple: one evaluation of $f$ per step, and no derivative of $f$ is needed.
2. Stable only for a sufficiently small $h$ on a stiff equation, because the method follows the tangent rather than the curve.
3. Inexact: the global error falls only linearly in $h$, so high accuracy requires many steps.
4. It is the foundation of the higher methods: Heun, the mid-point method, and the Runge-Kutta family all correct Euler's $\dfrac{h^2}{2}y''$ term.

$$
\boxed{y_{n+1} = y_n + h\,f(x_n, y_n), \qquad \text{global error } O(h)}
$$

---

### 🎯 Using Euler's method, determine $\frac{dy}{dx} = \frac{3}{5}x^3 y$; Consider $y(0) = 1$.
> **Appeared:** 2021 Q.8(c), 2023 Q.3(b) — (04 marks, CO: 3)

**Full Answer:**

> [!WARNING] A gap in the printed question
> No step size $h$ and no interval are given, so numbers cannot be produced without a stated choice. Use $h = 0.25$ and $x: 0 \to 1$, and say so. The exact solution is provided below so the answer can be judged at any step size.

**The method.**

$$
y_{n+1} = y_n + h\,f(x_n, y_n) = y_n + h\cdot\frac{3}{5}x_n^3 y_n
$$

**Step 1.** At $x_0 = 0$, $y_0 = 1$: slope $\frac{3}{5}(0)^3(1) = 0$, so $y_1 = 1 + 0.25(0) = 1.0000000$.

**Step 2.** At $x_1 = 0.25$, $y_1 = 1$: slope $\frac{3}{5}(0.25)^3(1) = \frac{3}{5}(0.015625) = 0.0093750$, so $y_2 = 1 + 0.25(0.009375) = 1.0023438$.

**Step 3.** At $x_2 = 0.5$, $y_2 = 1.0023438$: slope $\frac{3}{5}(0.5)^3(1.0023438) = \frac{3}{5}(0.125)(1.0023438) = 0.0751758$, so $y_3 = 1.0023438 + 0.25(0.0751758) = 1.0211377$.

**Step 4.** At $x_3 = 0.75$, $y_3 = 1.0211377$: slope $\frac{3}{5}(0.75)^3(1.0211377) = \frac{3}{5}(0.421875)(1.0211377) = 0.2584755$, so $y_4 = 1.0211377 + 0.25(0.2584755) = 1.0857566$.

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

> [!INFO] Check against the exact solution
> The equation is separable: $\frac{dy}{y} = \frac{3}{5}x^3dx$, so $\ln y = \frac{3}{20}x^4 + C$, and $y(0) = 1$ gives $C = 0$.
> $$
> y = e^{\frac{3}{20}x^4} = e^{0.15x^4}
> $$
> At $x = 1$: $e^{0.15} = 1.1618342$. Euler's $1.0857566$ is **low** by $0.0760777$, which is expected: Euler always undershoots when the solution is convex and increasing. Differentiating once more,
> $$
> y' = \frac{3}{5}x^3 y, \qquad y'' = \frac{9}{5}x^2 y + \frac{3}{5}x^3\cdot\frac{3}{5}x^3 y = \frac{9}{25}x^2(x^4 + 5)\,y
> $$
> which is positive for every $x \ne 0$, since $y > 0$.

> [!WARNING] The zero first step is not a mistake
> Step 1 gives $y_1 = 1.0000000$, identical to $y_0$. That is because the slope is $\frac{3}{5}x^3y$ and $x_0 = 0$.
>
> A step that produces no change looks like a failure and is not one here. The right response is to check the **slope**, not the step: a zero slope at $x = 0$ for a function containing $x^3$ is exactly right, and it also tells you immediately that all the growth happens in the last few steps.
>
> Compare the slope column: $0$, $0.0094$, $0.0752$, $0.2585$. The last step contributes most of the answer, which is a strong hint that the coarse steps are wasting most of their accuracy.

> [!NOTE] First order accuracy confirmed
> Halving $h$ from $0.5$ to $0.25$ cut the error from $0.12433$ to $0.07608$, a ratio of $1.63$ rather than the expected 2, because four steps of a stiffly growing function do not sit neatly in the asymptotic range yet. Halving again to $h = 0.1$ gives $0.03459$, and $0.07608/0.03459 = 2.20$, which is the expected factor of 2 as $h \to 0$. Euler is first order: halving the step halves the error.

---

## Exam Variants

| Year | Question | ODE | Step | Key Answer |
| :--- | :--- | :--- | :--- | :--- |
| 2019 Q.7(c) | Discuss Euler's method | Theory | — | $\boxed{y_{n+1} = y_n + h\,f(x_n, y_n), \qquad \text{global error } O(h)}$ |
| 2020 Q.7(b) | Euler march, find $y(0.4)$, $y(0.6)$ | $y' = x + y$, $y(0) = 0$ | $h = 0.2$ | $\boxed{y(0.4) = 0.0400, \qquad y(0.6) = 0.1280 \quad (h = 0.2)}$ |
| 2021 Q.8(c) | Euler, $y(1)$ | $y' = \frac{3}{5}x^3y$, $y(0) = 1$ | $h = 0.25$ | $\boxed{y(1) \approx 1.08576 \quad (h = 0.25)}$ |
| 2023 Q.3(b) | Same as 2021 Q.8(c) | identical | identical | $\boxed{y(1) \approx 1.08576 \quad (h = 0.25)}$ |

---

## ⚡ Exam Tips & Common Mistakes

1. **Always evaluate the slope at the old point.** $y_{n+1} = y_n + h f(x_n, y_n)$ uses $x_n$ and $y_n$, both from step $n$. Using $x_{n+1}$ or $y_{n+1}$ in the slope is the single most common slip.
2. **A zero first step is usually correct, not wrong.** In 2020 and 2021 the slope at $x = 0$ was zero, so $y_1 = y_0$. Check the slope column before doubting the method.
3. **Count the steps.** To reach $x_n$ from $x_0$ with step $h$, take $n = (x_n - x_0)/h$ steps. Forgetting to march through the intermediate nodes is the other common error.
4. **Euler under-reads a convex, increasing solution.** If your result overshoots, look for an arithmetic error rather than blaming the method.
5. **Halving $h$ only halves the error.** That is the signature of first order. If your error falls by 4 or 16, you did not run Euler.
6. **Euler needs no derivative of $f$.** If a question is solvable by repeated evaluation of $f$, Euler applies. Only the slope $f$ itself is needed.

## 🔗 Related Topics

- [NM-8 Lower: IVP vs BVP, Heun, RK2, BVP](NM-8_Lower_IVP_BVP_Heun_RK2_Higher.md) — the modified Euler predictor-corrector that fixes Euler's discarded term
- [NM-8.5: Runge-Kutta 4th Order](NM-8.5_Runge_Kutta_4th_Order.md) — the fourth-order method that corrects Euler's error four times over
- [NM-7: Numerical Differentiation](NM-7_Numerical_Differentiation.md) — the Taylor series idea behind the derivation

---

[← Previous: NM-7 Numerical Differentiation](NM-7_Numerical_Differentiation.md) | [🏠 Index](00_Index.md) | [Next: NM-8.5 Runge-Kutta 4th Order →](NM-8.5_Runge_Kutta_4th_Order.md)