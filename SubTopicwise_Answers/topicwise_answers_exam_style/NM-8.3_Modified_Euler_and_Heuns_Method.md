---
title: "NM-8.3 · Modified Euler / Heun's Method"
tags:
  - numerical-methods
  - discrete-mathematics
  - topicwise
---


[🏠 Subtopic Index](00_Index.md) | [← Prev: NM-8.2 Euler's Method](NM-8.2_Eulers_Method.md) | [Next: NM-8.4 Runge-Kutta 2nd Order →](NM-8.4_Runge_Kutta_2nd_Order.md)

---

# NM-8.3 · Modified Euler / Heun's Method

Every block below is copied from `../answers_exam_style/`, which is the
only place an answer is authored. A number here is the same number, character
for character, as the one it came from.


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

[🏠 Subtopic Index](00_Index.md) | [← Prev: NM-8.2 Euler's Method](NM-8.2_Eulers_Method.md) | [Next: NM-8.4 Runge-Kutta 2nd Order →](NM-8.4_Runge_Kutta_2nd_Order.md)
