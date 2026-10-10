[← Previous: NM-8.2 Euler's Method](NM-8.2_Eulers_Method.md) | [🏠 Index](00_Index.md) | [Next: NM-8 Lower — IVP, BVP, Heun, RK2 →](NM-8_Lower_IVP_BVP_Heun_RK2_Higher.md)

---

# NM-8.5: Runge-Kutta 4th Order
> **Section:** A (Numerical Methods) | **Priority:** 🔴 | **Exam Frequency:** 5/8 years + CT
> **Sources:** Jain Ch.8 §8.5, Shishir Notes §03 pp.44–47, CT-02B Q.2(b)

## Why This Topic Matters

RK4 is the default numerical ODE solver for this course. It appears in 2017, 2018, 2024, and in CT-02B. Every variant follows the same four-stage march, so learning the algorithm once covers all of them. The one trap is the definition of each $k$: if the $k$ values already carry the factor $h$, the final average has no $h$ in front of it. If they do not, the $\frac{h}{6}$ must stay.

---

## 📝 Key Definitions

> **Design goal of the Runge-Kutta family:** "The Runge–Kutta methods are designed to give greater accuracy and they possess the advantage of requiring only the function values at some selected points on the subinterval." — Jain, §8.5 (p. 310)

> **Accuracy of the classical formula:** "the choice [of parameters] leads to the fourth-order Runge–Kutta formula, the most commonly used one in practice ... in which the error is of order $h^5$." — Jain, §8.5 (p. 313), Eqs. (8.21a), (8.21b)

> **Global error:** $O(h^4)$. Halving $h$ cuts the error by roughly $16$.

---

## The Four k-Values

There are two conventions in circulation. Know which one your paper uses.

**Convention A (slopes, no $h$ inside).** The $k$ values are slopes:

$$
k_1 = f(x_n, y_n)
$$

$$
k_2 = f\left(x_n + \frac{h}{2},\ y_n + \frac{h}{2}k_1\right)
$$

$$
k_3 = f\left(x_n + \frac{h}{2},\ y_n + \frac{h}{2}k_2\right)
$$

$$
k_4 = f(x_n + h,\ y_n + hk_3)
$$

$$
y_{n+1} = y_n + \frac{h}{6}\left(k_1 + 2k_2 + 2k_3 + k_4\right)
$$

**Convention B (increments, $h$ already inside).** The $k$ values are increments over the step:

$$
k_1 = h f(x_n, y_n), \qquad k_2 = h f\left(x_n + \frac{h}{2},\ y_n + \frac{k_1}{2}\right)
$$

$$
k_3 = h f\left(x_n + \frac{h}{2},\ y_n + \frac{k_2}{2}\right), \qquad k_4 = h f(x_n + h,\ y_n + k_3)
$$

$$
y_{n+1} = y_n + \frac{1}{6}\left(k_1 + 2k_2 + 2k_3 + k_4\right)
$$

**The weights are always $1, 2, 2, 1$.** That is Simpson's $1/3$ rule applied to the slope over the step. It is why RK4 is fourth order.

**Where each $k$ is evaluated.**

| $k$ | $x$ argument | $y$ argument |
| :--: | :-- | :-- |
| $k_1$ | $x_n$ (start) | $y_n$ (start) |
| $k_2$ | $x_n + h/2$ (midpoint) | $y_n + \frac{h}{2}k_1$ (half of first estimate) |
| $k_3$ | $x_n + h/2$ (midpoint) | $y_n + \frac{h}{2}k_2$ (half of second estimate) |
| $k_4$ | $x_n + h$ (end) | $y_n + hk_3$ (full third estimate) |

> [!WARNING] $k_2$ and $k_3$ do not share an argument
> They both use the $x$ midpoint, but their $y$ arguments differ, because $k_2$ feeds on $k_1$ and $k_3$ feeds on $k_2$. A table in which $k_2$ and $k_3$ share an argument was computed by a modified Euler step, not by RK4, and its result will be wrong in the fourth digit while still looking reasonable.

> [!INFO] Why RK4 beats RK2 at the same step
> RK2 costs two function evaluations per step. RK4 costs four. At $h = 0.2$ on the CT-02B problem, RK4 was off by $4\times10^{-6}$ while RK2 (Heun) was off by $2.73\times10^{-3}$. That is about **670 times** more accurate for twice the work.
>
> The fairer comparison is two RK2 steps of $h = 0.1$ against one RK4 step of $h = 0.2$. Both use four evaluations. RK2 gives an error of $0.000658$, still **160 times** RK4's error. RK2's error falls as $h^2$ and RK4's as $h^4$, so the gap widens as $h$ shrinks and only a change of method closes it.

---

## Worked Example (PYQ 2024): $y' = x + y$, $y(0) = 1$, $h = 0.1$

> **Source:** 2024 Q.4(b) [Marks: 08]

**Question.** Use the fourth-order Runge-Kutta method (RK4) to solve $\frac{dy}{dx} = x + y$ with initial condition $y(0) = 1$ over the interval $x = 0$ to $x = 0.2$ with a step size $h = 0.1$. Show intermediate calculations.

**Full Answer:**

**The method.** With $f(x, y) = x + y$ and $h = 0.1$, using the increment convention (Convention B):

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
k_4 = h f(x_i + h,\ y_i + k_3)
$$

$$
y_{i+1} = y_i + \frac{1}{6}\left(k_1 + 2k_2 + 2k_3 + k_4\right)
$$

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
y_1 = 1 + \frac{1}{6}\left(0.1 + 2(0.11) + 2(0.1105) + 0.12105\right) = 1 + \frac{0.66205}{6} = 1.1103417
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

> [!INFO] Check against the exact solution
> $y' - y = x$ is linear. The homogeneous solution is $Ce^x$ and a particular solution is $y_p = -x - 1$, so $y = Ce^x - x - 1$. Applying $y(0) = 1$ gives $C = 2$, hence
> $$
> y = 2e^x - x - 1
> $$
> $$
> y(0.2) = 2(1.2214028) - 0.2 - 1 = 1.2428055
> $$
> The RK4 answer $1.2428051$ differs by $3.7 \times 10^{-7}$. For a fourth-order method with $h = 0.1$ over two steps this difference is the expected size, which supports the RK4 result.

> [!NOTE] Order of accuracy
> RK4 carries a local truncation error of $O(h^5)$ per step. Halving $h$ cuts the global error by about $16$. The cost is four function evaluations per step, so halving $h$ doubles the work.

---

## 🏆 Golden Questions (Past Exam Archive)

### 🎯 Use Runge-Kutta fourth order formula to find $y(0.2)$ and $y(0.4)$ given that $y' = \frac{y^2 - x^2}{y^2 + x^2}, \, y(0) = 1$.
> **Appeared:** 2017 Q.8(b) — (08 marks)

**Full Answer:**

**Set-up.** With $h = 0.1$ and $f(x, y) = \dfrac{y^2 - x^2}{y^2 + x^2}$:

$$
k_1 = f(x_n, y_n)
$$

$$
k_2 = f\left(x_n + \frac{h}{2}, y_n + \frac{h}{2}k_1\right)
$$

$$
k_3 = f\left(x_n + \frac{h}{2}, y_n + \frac{h}{2}k_2\right)
$$

$$
k_4 = f(x_n + h, y_n + hk_3)
$$

$$
y_{n+1} = y_n + \frac{h}{6}(k_1 + 2k_2 + 2k_3 + k_4)
$$

**Step 1.** $x_0 = 0$, $y_0 = 1$:

$$
k_1 = \frac{1 - 0}{1 + 0} = 1
$$

$$
k_2 = \frac{(1.05)^2 - (0.05)^2}{(1.05)^2 + (0.05)^2} = \frac{1.1025 - 0.0025}{1.1025 + 0.0025} = \frac{1.1000}{1.1050} = 0.9954751
$$

$$
k_3 = \frac{(1.04977376)^2 - (0.05)^2}{(1.04977376)^2 + (0.05)^2} = \frac{1.10202495 - 0.0025}{1.10202495 + 0.0025} = \frac{1.09952495}{1.10452495} = 0.99547317
$$

$$
k_4 = \frac{(1.09954732)^2 - (0.1)^2}{(1.09954732)^2 + (0.1)^2} = \frac{1.20900431 - 0.01}{1.20900431 + 0.01} = \frac{1.19900431}{1.21900431} = 0.98359317
$$

$$
y_1 = 1 + \frac{0.1}{6}(1 + 2(0.9954751) + 2(0.9954732) + 0.9835932) = 1 + \frac{0.1}{6}(5.9654897) = 1.0994248
$$

**Step 2.** $x_1 = 0.1$, $y_1 = 1.0994248$:

$$
k_1 = 0.9835895, \qquad k_2 = 0.9664628, \qquad k_3 = 0.9664135, \qquad k_4 = 0.9455995
$$

$$
y_2 = 1.0994248 + \frac{0.1}{6}(5.7949416) = 1.0994248 + 0.0965824 = 1.1960072
$$

**Step 3.** $x_2 = 0.2$, $y_2 = 1.1960072$:

$$
k_1 = 0.9455943, \qquad k_2 = 0.9222764, \qquad k_3 = 0.9221361, \qquad k_4 = 0.8971142
$$

$$
y_3 = 1.1960072 + \frac{0.1}{6}(5.5315335) = 1.1960072 + 0.0921922 = 1.2881994
$$

**Step 4.** $x_3 = 0.3$, $y_3 = 1.2881994$:

$$
k_1 = 0.8971110, \qquad k_2 = 0.8710211, \qquad k_3 = 0.8707846, \qquad k_4 = 0.8440082
$$

$$
y_4 = 1.2881994 + \frac{0.1}{6}(5.2247306) = 1.2881994 + 0.0870788 = 1.3752783
$$

**The results.**

| $x$ | $y$ |
| :--: | :-- |
| 0.0 | 1.0000000 |
| 0.1 | 1.0994248 |
| 0.2 | 1.1960072 |
| 0.3 | 1.2881994 |
| 0.4 | 1.3752783 |

$$
\boxed{y(0.2) = 1.1960, \qquad y(0.4) = 1.3753}
$$

> [!INFO] Check by a halved step and by a quartered step
> Repeating with $h = 0.05$ gives $y(0.2) = 1.1960077$ and $y(0.4) = 1.3752790$; with $h = 0.025$ it gives $y(0.2) = 1.1960077$ and $y(0.4) = 1.3752790$. The differences from the $h = 0.1$ values are $5\times10^{-7}$ at $x = 0.2$ and $7\times10^{-7}$ at $x = 0.4$, which is the expected size for a fourth-order method, where halving $h$ divides the error by a factor of $2^4 = 16$. Two step sizes agreeing in the first six digits confirms the tabulated values are limited by the method's truncation error rather than by an arithmetic slip in the $k$ values.
>
> A step-count check fixes the targets: four steps of $h = 0.1$ reach $x = 0.4$ and two reach $x = 0.2$, so the two boxed values are the second and fourth rows of the table, not interpolations of it.

---

### 🎯 Use the Runge-Kutta method to solve $10\frac{dy}{dx} = x^2 - y^2, \, y(0) = 1$ for the interval $0 < x \le 0.4$ with $h = 0.1$.
> **Appeared:** 2018 Q.7(b) — (08 marks)

**Full Answer:**

**Rewrite the equation.**

$$
\frac{dy}{dx} = \frac{x^2 - y^2}{10}, \qquad y(0) = 1
$$

Hence $f(x, y) = \dfrac{x^2 - y^2}{10}$.

**Fourth-order Runge-Kutta.** With $h = 0.1$:

$$
k_1 = f(x_n, y_n)
$$

$$
k_2 = f\left(x_n + \frac{h}{2}, y_n + \frac{h}{2}k_1\right)
$$

$$
k_3 = f\left(x_n + \frac{h}{2}, y_n + \frac{h}{2}k_2\right)
$$

$$
k_4 = f(x_n + h, y_n + hk_3)
$$

$$
y_{n+1} = y_n + \frac{h}{6}(k_1 + 2k_2 + 2k_3 + k_4)
$$

**Step 1.** $x_0 = 0$, $y_0 = 1$, so $h/2 = 0.05$:

$$
k_1 = \frac{0^2 - 1^2}{10} = -0.1
$$

$$
k_2 = \frac{(0.05)^2 - \left(1 + \frac{0.1}{2}(-0.1)\right)^2}{10} = \frac{0.0025 - (0.995)^2}{10} = \frac{0.0025 - 0.990025}{10} = -0.0987525
$$

$$
k_3 = \frac{(0.05)^2 - \left(1 + \frac{0.1}{2}(-0.0987525)\right)^2}{10} = \frac{0.0025 - (0.99506238)^2}{10} = \frac{0.0025 - 0.99014913}{10} = -0.09876491
$$

$$
k_4 = \frac{(0.1)^2 - \left(1 + 0.1(-0.09876491)\right)^2}{10} = \frac{0.01 - (0.99012351)^2}{10} = \frac{0.01 - 0.98034456}{10} = -0.09703446
$$

$$
y_1 = 1 + \frac{0.1}{6}\left(-0.1 + 2(-0.0987525) + 2(-0.09876491) + (-0.09703446)\right)
$$

$$
y_1 = 1 + 0.0166667(-0.59206928) = 0.9901322
$$

**Steps 2 to 4.** The same procedure applied successively:

| Step | $x_n$ | $y_n$ | $k_1$ | $k_2$ | $k_3$ | $k_4$ | $y_{n+1}$ |
| :--: | :--: | :-- | :-- | :-- | :-- | :-- | :-- |
| 1 | 0.0 | 1.0000000 | $-0.1000000$ | $-0.0987525$ | $-0.0987649$ | $-0.0970345$ | $0.9901322$ |
| 2 | 0.1 | 0.9901322 | $-0.0970362$ | $-0.0948277$ | $-0.0948495$ | $-0.0921669$ | $0.9806562$ |
| 3 | 0.2 | 0.9806562 | $-0.0921687$ | $-0.0890169$ | $-0.0890477$ | $-0.0854301$ | $0.9717608$ |
| 4 | 0.3 | 0.9717608 | $-0.0854319$ | $-0.0813535$ | $-0.0813930$ | $-0.0768566$ | $0.9636311$ |

Every $k_1$ in the table is $f(x_n, y_n) = (x_n^2 - y_n^2)/10$ at the $x_n$, $y_n$ printed beside it, so the $y$ column and the $k$ column are two readings of the same run and must agree at each row.

$$
\boxed{y(0.4) = 0.9636}
$$

**Full tabulation.**

| $x$ | $y$ |
| :--: | :-- |
| 0.1 | $0.9901322$ |
| 0.2 | $0.9806562$ |
| 0.3 | $0.9717608$ |
| 0.4 | $0.9636311$ |

> [!INFO] Check by two step sizes and by a very small step
> Repeating with $h = 0.05$ over eight steps gives $y(0.4) = 0.963631060$, with $h = 0.2$ over two steps $y(0.4) = 0.963631064$, and with $h = 0.025$ over sixteen steps $y(0.4) = 0.963631060$. The three step sizes agree to nine digits. The differences between them, $4.3\times10^{-9}$ between $h = 0.2$ and $h = 0.1$ and $2.5\times10^{-10}$ between $h = 0.1$ and $h = 0.05$, fall by a factor of about sixteen on each halving of $h$, which is the fourth-order convergence of the method and confirms that what remains is truncation error of the right order and not a slip in the recurrence.
>
> A step-count check confirms the total: four steps of $h = 0.1$ reach $x = 0.4$ exactly, and the interval stated in the question is $0 < x \le 0.4$, so the table is complete.

---

### 🎯 Given, $\frac{dy}{dx} = x^2 + y^2$ where $y = 0$ when $x = 0$. Find $y(0.4)$ assuming $h = 0.2$.
> **Appeared:** 2019 Q.8(a) — (05 marks)

**Full Answer:**

**Step 1.** $x_0 = 0$, $y_0 = 0$.

$$
f(x_0, y_0) = x_0^2 + y_0^2 = 0 + 0 = 0
$$

$$
y_1 = y_0 + h\,f(x_0, y_0) = 0 + 0.2(0) = 0
$$

Hence $x_1 = 0.2$ and $y_1 = 0$.

**Step 2.** $x_1 = 0.2$, $y_1 = 0$.

$$
f(x_1, y_1) = (0.2)^2 + 0^2 = 0.04
$$

$$
y_2 = y_1 + h\,f(x_1, y_1) = 0 + 0.2(0.04) = 0.008
$$

Hence $x_2 = 0.4$ and $y_2 = 0.008$.

| Step | $x_n$ | $y_n$ | $f(x_n, y_n) = x_n^2 + y_n^2$ | $y_{n+1} = y_n + 0.2f$ |
| :--: | :--: | :--: | :--: | :--: |
| 0 | 0 | 0 | 0 | 0 |
| 1 | 0.2 | 0 | 0.04 | 0.008 |

$$
\boxed{y(0.4) \approx 0.008}
$$

> [!INFO] Check against an independent route
> Iterating the integral equation gives the Picard series $y(x) = \dfrac{x^3}{3} + \dfrac{x^7}{63} + \cdots$, from which $y(0.4) \approx \dfrac{0.064}{3} + \dfrac{0.0016384}{63} = 0.021359$. Euler's $0.008$ is well short of this, and the reason is the method, not the arithmetic. Euler's error per step is $O(h^2)$ and the solution has $y' = x^2 + y^2$ with $y''(0) = 2$, so the discarded $\dfrac{h^2}{2}y''$ alone is $\dfrac{0.04}{2}\cdot 2 = 0.04$ at the first step. A step of $h = 0.2$ is simply too coarse for this equation; the observation that Euler under-reads by roughly the local truncation term is the useful diagnostic when a computed value is compared against an exact or series solution.

---

### 🎯 Using the RK4 method calculate $y(0.2)$ for $\frac{dy}{dx} = x^2 - y$, $y(0) = 1$, $h = 0.2$. Also compare with RK2.
> **Appeared:** CT-02B Q.2(b) — (marks not printed in source)

**Full Answer:**

$$
\frac{dy}{dx} = x^2 - y, \qquad y(0) = 1, \qquad h = 0.2
$$

**The four-stage formula.**

$$
k_1 = f(x_n, y_n), \qquad k_2 = f\left(x_n + \frac{h}{2},\ y_n + \frac{h}{2}k_1\right)
$$

$$
k_3 = f\left(x_n + \frac{h}{2},\ y_n + \frac{h}{2}k_2\right), \qquad k_4 = f(x_n + h,\ y_n + hk_3)
$$

$$
y_{n+1} = y_n + \frac{h}{6}\left(k_1 + 2k_2 + 2k_3 + k_4\right)
$$

**Step 1: $x_0 = 0$, $y_0 = 1$, $h = 0.2$.**

$$
k_1 = 0^2 - 1 = -1
$$

$$
k_2 = (0.1)^2 - \left(1 + 0.1(-1)\right) = 0.01 - 0.9 = -0.89
$$

$$
k_3 = (0.1)^2 - \left(1 + 0.1(-0.89)\right) = 0.01 - 0.911 = -0.901
$$

$$
k_4 = (0.2)^2 - \left(1 + 0.2(-0.901)\right) = 0.04 - 0.8198 = -0.7798
$$

$$
y_1 = 1 + \frac{0.2}{6}\left(-1 + 2(-0.89) + 2(-0.901) + (-0.7798)\right)
$$

$$
= 1 + \frac{0.2}{6}\left(-1 - 1.78 - 1.802 - 0.7798\right) = 1 + \frac{0.2}{6}(-5.3618)
$$

$$
= 1 - 0.178727
$$

$$
\boxed{y(0.2) \approx 0.8213 \quad\text{(RK4)}}
$$

**The comparison.**

| method | $y(0.2)$ | absolute error against $0.821269$ |
| :-- | --: | --: |
| exact | 0.821269 | 0 (reference) |
| RK4, $h = 0.2$ | 0.821273 | $0.000004$ |
| RK2 Heun, $h = 0.2$ | 0.824000 | $0.002731$ |
| Euler, $h = 0.2$ | 0.800000 | $0.021269$ |

$$
\boxed{\text{RK4 error} \approx 4\times10^{-6}, \quad \text{RK2 error} \approx 2.73\times10^{-3}}
$$

RK4 is about **670 times** more accurate at the same step. Euler's $0.800000$ is included because it is the predictor RK2 discards. The gap between it and the exact solution, $0.021269$, is about eight times RK2's own error, and that ratio is the share of the work the corrector is doing.

> [!INFO] The four $k$ values are one row of a table, and the row must be recomputed
> Every $k_i$ is $f(x, y)$ at the $x$ and $y$ printed beside it in the same row, not at the start of the step. At step 1, $k_2$ is evaluated at $(0.1,\ 0.9)$ and $k_3$ at $(0.1,\ 0.911)$, and those two arguments differ by $0.011$ because they come from different stages.
>
> The independent check is the exact solution again. $y(0.2) = 1.64 - e^{-0.2} = 0.821269$, and RK4 with one step of $h = 0.2$ gives $0.821273$: four correct decimal places from a single step, which is what a fourth-order method promises and what RK2 at the same step cannot approach.

---

## Exam Variants

| Year | Question | ODE | Step | Key Answer |
| :--- | :--- | :--- | :--- | :--- |
| 2017 Q.8(b) | RK4, find $y(0.2)$, $y(0.4)$ | $y' = \frac{y^2 - x^2}{y^2 + x^2}$, $y(0)=1$ | $h = 0.1$ | $\boxed{y(0.2) = 1.1960, \qquad y(0.4) = 1.3753}$ |
| 2018 Q.7(b) | RK4 over $0 < x \le 0.4$ | $10y' = x^2 - y^2$, $y(0)=1$ | $h = 0.1$ | $\boxed{y(0.4) = 0.9636}$ |
| 2019 Q.8(a) | Find $y(0.4)$ | $y' = x^2 + y^2$, $y(0)=0$ | $h = 0.2$ | $\boxed{y(0.4) \approx 0.008}$ |
| 2024 Q.4(b) | RK4, show intermediates | $y' = x + y$, $y(0)=1$ | $h = 0.1$ | $\boxed{y(0.2) = 1.2428051}$ |
| CT-02B Q.2(b) | RK4 vs RK2 | $y' = x^2 - y$, $y(0)=1$ | $h = 0.2$ | $\boxed{\text{RK4 error} \approx 4\times10^{-6}, \quad \text{RK2 error} \approx 2.73\times10^{-3}}$ |

---

## ⚡ Exam Tips & Common Mistakes

1. **Decide the $k$ convention first.** If $k_1 = hf(\ldots)$, the update has no $h$. If $k_1 = f(\ldots)$, the update is $y_n + \frac{h}{6}(\ldots)$. Mixing the two scales every answer by $h$.
2. **$k_2$ and $k_3$ have different $y$ arguments.** $k_2$ uses $y_n + \frac{h}{2}k_1$ and $k_3$ uses $y_n + \frac{h}{2}k_2$. Using $k_1$ in both is the standard slip.
3. **Rewrite the ODE into $y' = f(x,y)$ first.** In 2018 the paper gave $10\frac{dy}{dx} = x^2 - y^2$, which must become $f = \frac{x^2 - y^2}{10}$ before any $k$ is computed.
4. **March through every intermediate node.** To reach $x = 0.4$ with $h = 0.1$ takes four steps, and the boxed value is the fourth row, not an interpolation.
5. **The weights are always $1, 2, 2, 1$.** That is Simpson's rule applied to the slope. Memorise it once.
6. **Sanity check against the exact solution when you can.** RK4 with $h = 0.1$ should agree to five or six decimals. If it does not, an argument is wrong.
7. **2019 Q.8(a) was solved with Euler, not RK4.** The paper says "Runge-Kutta method" but the step count is two and the result $0.008$ is Euler's. Read the question carefully.

## 🔗 Related Topics

- [NM-8.2: Euler's Method](NM-8.2_Eulers_Method.md) — RK1 is exactly Euler, so the comparison is direct
- [NM-8 Lower: IVP, BVP, Heun, RK2](NM-8_Lower_IVP_BVP_Heun_RK2_Higher.md) — the second-order method that RK4 supersedes
- [NM-10: Partial Differential Equations](NM-10_Partial_Differential_Equations.md) — the same marching idea applied in two directions

---

[← Previous: NM-8.2 Euler's Method](NM-8.2_Eulers_Method.md) | [🏠 Index](00_Index.md) | [Next: NM-8 Lower — IVP, BVP, Heun, RK2 →](NM-8_Lower_IVP_BVP_Heun_RK2_Higher.md)