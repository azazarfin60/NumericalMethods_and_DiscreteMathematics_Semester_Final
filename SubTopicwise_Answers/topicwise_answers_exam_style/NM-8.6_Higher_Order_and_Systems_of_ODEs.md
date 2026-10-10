---
title: "NM-8.6 · Higher-Order & Systems of ODEs"
tags:
  - numerical-methods
  - discrete-mathematics
  - topicwise
---





[🏠 Subtopic Index](00_Index.md) | [← Prev: NM-8.5 Runge-Kutta 4th Order](NM-8.5_Runge_Kutta_4th_Order.md) | [Next: NM-8.7 ODE Formulation from Physical Problems →](NM-8.7_ODE_Formulation_from_Physical_Problems.md)

---

# NM-8.6 · Higher-Order & Systems of ODEs

Every block below is copied from `../answers_exam_style/`, which is the
only place an answer is authored. A number here is the same number, character
for character, as the one it came from.


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

[🏠 Subtopic Index](00_Index.md) | [← Prev: NM-8.5 Runge-Kutta 4th Order](NM-8.5_Runge_Kutta_4th_Order.md) | [Next: NM-8.7 ODE Formulation from Physical Problems →](NM-8.7_ODE_Formulation_from_Physical_Problems.md)
