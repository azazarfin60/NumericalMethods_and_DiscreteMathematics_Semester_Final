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

Every block below is copied from `../answers_explanation/`. The reasoning
is written once, in the year-wise file, and is not restated here.


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

[🏠 Subtopic Index](00_Index.md) | [← Prev: NM-8.5 Runge-Kutta 4th Order](NM-8.5_Runge_Kutta_4th_Order.md) | [Next: NM-8.7 ODE Formulation from Physical Problems →](NM-8.7_ODE_Formulation_from_Physical_Problems.md)
