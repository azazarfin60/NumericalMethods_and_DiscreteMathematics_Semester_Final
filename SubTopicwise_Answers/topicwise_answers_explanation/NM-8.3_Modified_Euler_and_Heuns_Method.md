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

Every block below is copied from `../answers_explanation/`. The reasoning
is written once, in the year-wise file, and is not restated here.


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

[🏠 Subtopic Index](00_Index.md) | [← Prev: NM-8.2 Euler's Method](NM-8.2_Eulers_Method.md) | [Next: NM-8.4 Runge-Kutta 2nd Order →](NM-8.4_Runge_Kutta_2nd_Order.md)
