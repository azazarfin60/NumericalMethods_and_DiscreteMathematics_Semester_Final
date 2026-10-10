---
title: "NM-8.5 · Runge-Kutta 4th Order"
tags:
  - numerical-methods
  - discrete-mathematics
  - topicwise
---





[🏠 Subtopic Index](00_Index.md) | [← Prev: NM-8.4 Runge-Kutta 2nd Order](NM-8.4_Runge_Kutta_2nd_Order.md) | [Next: NM-8.6 Higher-Order & Systems of ODEs →](NM-8.6_Higher_Order_and_Systems_of_ODEs.md)

---

# NM-8.5 · Runge-Kutta 4th Order

Every block below is copied from `../answers_explanation/`. The reasoning
is written once, in the year-wise file, and is not restated here.


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

[🏠 Subtopic Index](00_Index.md) | [← Prev: NM-8.4 Runge-Kutta 2nd Order](NM-8.4_Runge_Kutta_2nd_Order.md) | [Next: NM-8.6 Higher-Order & Systems of ODEs →](NM-8.6_Higher_Order_and_Systems_of_ODEs.md)
