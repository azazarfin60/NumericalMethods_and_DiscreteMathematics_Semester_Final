---
title: "NM-8.4 · Runge-Kutta 2nd Order"
tags:
  - numerical-methods
  - discrete-mathematics
  - topicwise
---

# NM-8.4 · Runge-Kutta 2nd Order

Every block below is copied from `../answers_explanation/`. The reasoning
is written once, in the year-wise file, and is not restated here.


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
