---
title: "NM-8.4 · Runge-Kutta 2nd Order"
tags:
  - numerical-methods
  - discrete-mathematics
  - topicwise
---

# NM-8.4 · Runge-Kutta 2nd Order

Every block below is copied from `../answers_exam_style/`, which is the
only place an answer is authored. A number here is the same number, character
for character, as the one it came from.


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
