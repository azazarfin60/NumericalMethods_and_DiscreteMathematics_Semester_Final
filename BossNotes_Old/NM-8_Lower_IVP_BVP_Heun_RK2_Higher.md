[← Previous: NM-8.5 Runge-Kutta 4th Order](NM-8.5_Runge_Kutta_4th_Order.md) | [🏠 Index](00_Index.md) | [Next: NM-9 Eigenvalue Problems →](NM-9_Eigenvalue_Problems.md)

---

# NM-8: Lower Tier — IVP vs BVP, Modified Euler, RK2, Higher-Order, Physical ODEs, BVP
> **Section:** A (Numerical Methods) | **Priority:** 🟠🟡 (mixed) | **Exam Frequency:** 7/8 years | **Subtopics:** NM-8.1, NM-8.3, NM-8.4, NM-8.6, NM-8.7, NM-8.8
> **Sources:** Jain Ch.8 §8.1, §8.10, Shishir Notes §03 pp.39–43

## Why This Topic Matters

This file holds everything in ODEs that does not get its own boss note. Two theory definitions (IVP vs BVP), the second-order method, the higher-order-to-first-order conversion, a physical modelling question, and the boundary value method. The BVP material is the dangerous part: 2021 spent a full 5-mark question on it and 2024 asked the theory. Boundary conditions are what separate an IVP from a BVP, and that distinction decides the whole algorithm.

---

## NM-8.1 — IVP vs BVP Concepts

### 📝 Definitions

> **Initial value problem:** "Problems in which all the initial conditions are specified at the *initial* point only are called *initial value problems*." — Jain, §8.1 (p. 303)

> **Boundary value problem:** "in problems involving second-and-higher-order differential equations, we may prescribe the conditions at two or more points. Such problems are called *boundary value problems*." — Jain, §8.1 (p. 303)

> **Why marching methods exist:** "the values of $y$ are computed by short steps ahead for equal intervals $h$ of the independent variable." — Jain, §8.1 (p. 302)

### Theory

**Initial value problem (IVP).** A differential equation together with conditions given at a **single** point, for example $y(0) = 1$. The solution can be marched forward from that point because each new value depends only on the values already computed.

**Boundary value problem (BVP).** A differential equation together with conditions given at **both ends** of the interval, for example $y(0) = 0$ and $y(1) = 1$. No starting value is known, so the whole interval must be solved at once.

| | IVP | BVP |
| :-- | :-- | :-- |
| Conditions | At one end | At both ends |
| How it is solved | March forward step by step | Solve the full algebraic system |
| Resulting system | Lower triangular | Tridiagonal for a second-order ODE |
| Cost | Very low per step | Full linear solve |
| Sensitivity | Local; errors stay near the start | Global; a change anywhere moves the whole solution |
| Shooting method | Not applicable | Reduces it to an IVP by tuning the unknown start value |

**Finite difference form for a second-order BVP.** Discretise the interval into $n+1$ points, replace $y''$ by the centred difference, and use the boundary conditions to replace the two unavailable end rows:

$$
\frac{y_{i-1} - 2y_i + y_{i+1}}{h^2} + p(x_i)y_i + q(x_i)y_i = r_i
$$

$$
\begin{cases}
y_0 = \text{given}, \\
y_{i-1} - (2 - p(x_i)h^2 - q(x_i)h^4)\,y_i + y_{i+1} = r_i h^2, \quad 1 \le i \le n-1 \\
y_n = \text{given}
\end{cases}
$$

### 🏆 Golden Question for NM-8.1

#### 🎯 Define boundary value and initial value problem.
> **Appeared:** 2021 Q.5(a) — (03 marks)

**Full Answer:**

**Initial value problem (IVP).** A differential equation together with conditions given at a **single** point, for example $y(0) = 1$. The solution can be marched forward from that point because each new value depends only on the values already computed.

**Boundary value problem (BVP).** A differential equation together with conditions given at **both ends** of the interval, for example $y(0) = 0$ and $y(1) = 1$. No starting value is known, so the whole interval must be solved at once.

| | IVP | BVP |
| :-- | :-- | :-- |
| Conditions | At one end | At both ends |
| How it is solved | March forward step by step | Solve the full algebraic system |
| Resulting system | Lower triangular | Tridiagonal for a second-order ODE |
| Cost | Very low per step | Full linear solve |
| Sensitivity | Local; errors stay near the start | Global; a change anywhere moves the whole solution |
| Shooting method | Not applicable | Reduces it to an IVP by tuning the unknown start value |

$$
\boxed{\text{IVP: conditions at one end, march forward. BVP: conditions at both ends, solve together.}}
$$

---

## NM-8.3 — Modified Euler and Heun's Method

### Theory

**Euler's method, for reference.** For $\frac{dy}{dx} = f(x, y)$ with $y(x_0) = y_0$ and step $h$,

$$
y_{n+1} = y_n + h f(x_n, y_n)
$$

It takes the slope at the **left** endpoint of the interval and assumes it holds across the whole interval. The local truncation error is $O(h^2)$ and the global error is $O(h)$, so the method is **first order**.

**Step 1. The idea of the modification.** Euler's weakness is that it uses only one slope per step and that slope is at the wrong end. Average two slopes, one at each end of the interval, and the error drops by a whole order.

**Step 2. Compute the slope at the left end.** Predict with plain Euler:

$$
y_p = y_n + h f(x_n, y_n)
$$

**Step 3. Compute the slope at the right end**, using that predicted value:

$$
f_{n+1} = f(x_n + h, y_p)
$$

**Step 4. Average the two slopes and take the step.**

$$
y_{n+1} = y_n + \frac{h}{2}\left[f(x_n, y_n) + f(x_n + h, y_n + h f(x_n, y_n))\right]
$$

This is **Heun's method**, also called the **improved Euler method** or the **trapezoidal method**. Another name for it is the **two-stage second-order Runge-Kutta method**, since the $k$ values reproduce it exactly.

**Step 5. The Runge-Kutta form**, to show where it comes from. With $k_1 = h f(x_n, y_n)$ and $k_2 = h f(x_n + h, y_n + k_1)$,

$$
y_{n+1} = y_n + \frac{1}{2}(k_1 + k_2)
$$

**Step 6. Accuracy.** The two-slope average cancels the leading local error term, so the local truncation error becomes $O(h^3)$ and the global error becomes $O(h^2)$. The method is now **second order**: halving $h$ cuts the error by 4 instead of 2. The cost is one extra function evaluation per step.

> [!NOTE] Why averaging two slopes buys a whole order
> Euler takes one slope and lets it hold across the interval. The error is the difference between the true curve and the straight line, which is $O(h^2)$ per step. Heun's method takes the average of the left slope and a right-end slope, and the difference between the trapezoid of slopes and the true curve is $O(h^3)$ per step. Over $n$ steps with $h \approx (b-a)/n$ that is a global $O(h^2)$.

> [!WARNING] The limitation is the accuracy, not the stability
> Students often say Euler is "unstable". It is not, in the usual sense. The characteristic that actually limits it is that its global error is $O(h)$, so reaching six correct digits costs about a million steps instead of about a hundred.
>
> That is a practical ceiling, not a correctness one. Euler converges; it simply refuses to converge quickly.
>
> **The cost of the first order is brutal.** Halving $h$ doubles the number of steps and halves the error, so getting one more digit costs twice the work. Going from three digits to six costs a factor of $1000$ in function evaluations. Compare RK4, where each halving gains two digits, so the same nine digits cost a factor of $32$ in steps and $64$ in evaluations.

> [!WARNING] The trap: "improved" does not mean "exact"
> Two names cause confusion and neither is wrong.
>
> **Modified Euler** sometimes means Heun's method above, and sometimes means the **midpoint method**:
> $$
> y_{n+1} = y_n + h f\left(x_n + \frac{h}{2},\ y_n + \frac{h}{2} f(x_n, y_n)\right)
> $$
> Both are second order, and both are called "modified Euler" in the wild.
>
> A related trap: writing $y_{n+1} = y_n + h f\left(\frac{x_n + x_{n+1}}{2}, \frac{y_n + y_{n+1}}{2}\right)$ is **not** an algorithm at all, because $y_{n+1}$ appears on the right-hand side. That is an implicit formula needing a solution, not a one-step method. Heun's method avoids the problem by replacing $y_{n+1}$ with an Euler **predictor** in the slope evaluation, which is exactly the point of Step 2.

> [!NOTE] Read the recursion, not the name
> Heun's method is also called the improved Euler, the modified Euler, and RK2. All four names refer to the same recursion. The formula in the box above is unambiguous, and if an exam asks to "derive" it, the derivation settles which scheme is meant.

### 🏆 Golden Question for NM-8.3

#### 🎯 Derive modified Euler's method. What is the major limitation of Euler's method?
> **Appeared:** 2020 Q.7(a) — (05 marks)

**Full Answer:**

**Euler's method, for reference.** For $\frac{dy}{dx} = f(x, y)$ with $y(x_0) = y_0$ and step $h$,

$$
y_{n+1} = y_n + h f(x_n, y_n)
$$

It takes the slope at the **left** endpoint of the interval and assumes it holds across the whole interval. The local truncation error is $O(h^2)$ and the global error is $O(h)$, so the method is **first order**.

**Step 1. The idea of the modification.** Euler's weakness is that it uses only one slope per step and that slope is at the wrong end. Average two slopes, one at each end of the interval, and the error drops by a whole order.

**Step 2. Compute the slope at the left end.** Predict with plain Euler:

$$
y_p = y_n + h f(x_n, y_n)
$$

**Step 3. Compute the slope at the right end**, using that predicted value:

$$
f_{n+1} = f(x_n + h, y_p)
$$

**Step 4. Average the two slopes and take the step.**

$$
\boxed{y_{n+1} = y_n + \frac{h}{2}\left[f(x_n, y_n) + f(x_n + h, y_n + h f(x_n, y_n))\right]}
$$

This is **Heun's method**, also called the **improved Euler method** or the **trapezoidal method**. Another name for it is the **two-stage second-order Runge-Kutta method**, since the $k$ values below reproduce it exactly.

**Step 5. The Runge-Kutta form.** With $k_1 = h f(x_n, y_n)$ and $k_2 = h f(x_n + h, y_n + k_1)$,

$$
y_{n+1} = y_n + \frac{1}{2}(k_1 + k_2)
$$

**Step 6. Accuracy.** The two-slope average cancels the leading local error term, so the local truncation error becomes $O(h^3)$ and the global error becomes $O(h^2)$. The method is now **second order**: halving $h$ cuts the error by 4 instead of 2.

**The major limitation of Euler's method.**

> **Euler's method is first order accurate, so it needs far too many steps for the accuracy usually wanted, and it goes unstable when $h$ exceeds a stability limit.**

Two parts, and the second is the serious one.

1. **Low order.** Global error $O(h)$. Reaching four correct digits with $h = 10^{-4}$ means $10^4$ steps, and the accumulated round off grows with the step count, so the gain flattens out.

2. **Conditional stability.** For the test equation $y' = \lambda y$ with $\lambda < 0$, Euler gives $y_{n+1} = (1 + h\lambda)y_n$. Stability needs $\lvert 1 + h\lambda\rvert < 1$, that is
$$
h < \frac{2}{\lvert\lambda\rvert}
$$
and for a stiff system $\lvert\lambda\rvert$ is enormous, so $h$ must be tiny.

**Practical note.** Heun's method is not unconditionally stable either. For $y' = \lambda y$ it gives $y_{n+1} = (1 + z + z^2/2)y_n$ with $z = h\lambda$, and stability needs $\lvert 1 + z + z^2/2\rvert < 1$, which allows $-2 < z < 0$, a range of $2$ against Euler's $2$. It is modestly better, not a cure. Real stiff solvers use the backward or implicit trapezoidal methods, which have unbounded stable regions.

$$
\boxed{y_{n+1} = y_n + \frac{h}{2}\left[f(x_n,y_n) + f(x_n+h,\, y_n + h f(x_n,y_n))\right],\quad \text{second order}}
$$

---

#### 🎯 Given the differential equation: $\frac{dy}{dx} = x^2 + y$ with $y(0) = 1$, compute $y(0.02)$ using Euler's modified method.
> **Appeared:** 2017 Q.8(a) — (04 marks)

**Full Answer:**

**Modified Euler (Heun's method).** With $h = 0.02$ and $f(x, y) = x^2 + y$, the predictor is

$$
\hat y_1 = y_0 + hf(x_0, y_0)
$$

and the corrector averages the two slopes:

$$
y_1 = y_0 + \frac{h}{2}\left[f(x_0, y_0) + f(x_1, \hat y_1)\right]
$$

**Step.** $x_0 = 0$, $y_0 = 1$, so $f(x_0, y_0) = 0^2 + 1 = 1$.

**Predictor.**

$$
\hat y_1 = 1 + 0.02(1) = 1.02
$$

**Corrector.** At $x_1 = 0.02$ and $\hat y_1 = 1.02$,

$$
f(x_1, \hat y_1) = (0.02)^2 + 1.02 = 0.0004 + 1.02 = 1.0204
$$

$$
y_1 = 1 + \frac{0.02}{2}(1 + 1.0204) = 1 + 0.01(2.0204) = 1 + 0.020204
$$

$$
\boxed{y(0.02) = 1.020204}
$$

> [!INFO] Check by a smaller step and by the exact solution
> Repeating with $h = 0.01$ over two steps gives $y(0.02) = 1.02020401$, which agrees with the single $h = 0.02$ step in the first eight digits. The exact solution of $y' - y = x^2$ is $y = Ce^x - (x^2 + 2x + 2)$, and $y(0) = 1$ gives $C = 3$, so $y(0.02) = 3e^{0.02} - (0.0004 + 0.04 + 2) = 1.0202040201$. The modified Euler value $1.020204$ differs from the exact value by $2\times10^{-8}$. The plain Euler value would be $1.02$, so the modification has already gained three digits.

---

#### 🎯 Solve $\frac{dy}{dx} = 1 - y$ with the initial condition $x = 0, y = 0$ by using modified Euler's method. Tabulate the solutions at $x = 0.1, 0.2, 0.3$.
> **Appeared:** 2018 Q.7(a) — (05 marks)

**Full Answer:**

**The method.** With $h = 0.1$ and $f(x, y) = 1 - y$, the predictor is $\hat y_1 = y_n + hf(x_n, y_n)$ and the corrector takes the average of the two slopes:

$$
y_{n+1} = y_n + \frac{h}{2}\left[f(x_n, y_n) + f(x_{n+1}, \hat y_1)\right]
$$

**Step 1.** $x_0 = 0$, $y_0 = 0$, $h = 0.1$.

$$
f(x_0, y_0) = 1 - 0 = 1
$$

$$
\hat y_1 = 0 + 0.1(1) = 0.1
$$

$$
f(x_1, \hat y_1) = 1 - 0.1 = 0.9
$$

$$
y_1 = 0 + \frac{0.1}{2}(1 + 0.9) = 0.05(1.9) = 0.095
$$

**Step 2.** $x_1 = 0.1$, $y_1 = 0.095$.

$$
f(x_1, y_1) = 1 - 0.095 = 0.905
$$

$$
\hat y_2 = 0.095 + 0.1(0.905) = 0.1855
$$

$$
f(x_2, \hat y_2) = 1 - 0.1855 = 0.8145
$$

$$
y_2 = 0.095 + \frac{0.1}{2}(0.905 + 0.8145) = 0.095 + 0.05(1.7195) = 0.180975
$$

**Step 3.** $x_2 = 0.2$, $y_2 = 0.180975$.

$$
f(x_2, y_2) = 1 - 0.180975 = 0.819025
$$

$$
\hat y_3 = 0.180975 + 0.1(0.819025) = 0.2628775
$$

$$
f(x_3, \hat y_3) = 1 - 0.2628775 = 0.7371225
$$

$$
y_3 = 0.180975 + \frac{0.1}{2}(0.819025 + 0.7371225) = 0.180975 + 0.05(1.5561475) = 0.2587824
$$

**The tabulated solutions.**

| $x$ | $y$ |
| :--: | :-- |
| 0.1 | $0.0950000$ |
| 0.2 | $0.1809750$ |
| 0.3 | $0.2587824$ |

$$
\boxed{y(0.1) = 0.095, \qquad y(0.2) = 0.181, \qquad y(0.3) = 0.259}
$$

> [!INFO] Check against the exact solution
> The equation is separable: $\dfrac{dy}{1-y} = dx$ gives $y = 1 - Ce^{-x}$, and $y(0) = 0$ gives $C = 1$, so $y = 1 - e^{-x}$. The exact values are $0.0951626$, $0.1812692$ and $0.2591818$ at $x = 0.1, 0.2, 0.3$. The computed values are low by $1.6\times10^{-4}$, $2.9\times10^{-4}$ and $4.0\times10^{-4}$ respectively, a pattern of errors growing with $x$ as expected of a second-order method with fixed $h$. The plain Euler values would be $0.1$, $0.19$ and $0.271$, whose errors are $4.84\times10^{-3}$, $8.73\times10^{-3}$ and $1.18\times10^{-2}$. The modification has therefore reduced the error by about thirty times, which confirms the corrector was applied rather than only the predictor.

---

## NM-8.4 — Runge-Kutta 2nd Order

### Theory

For $\frac{dy}{dx} = f(x,y)$ with $y(x_0) = y_0$ and step $h$, the **Heun** form of the second-order Runge-Kutta method is:

$$
k_1 = h f(x_n, y_n), \qquad k_2 = h f\left(x_n + h, \; y_n + k_1\right), \qquad y_{n+1} = y_n + \frac{1}{2}(k_1 + k_2)
$$

This is exactly the modified Euler method above. Global error $O(h^2)$.

> [!WARNING] "RK2" is a family, not one formula
> Heun averages the two slopes. The **midpoint** method uses $k_2 = h f\left(x_n + \frac{h}{2}, y_n + \frac{k_1}{2}\right)$ with $y_{n+1} = y_n + k_2$. The **Ralston** variant uses $2/3$ and $1/3$. All are second order but their constants differ. Heun is the convention used in this course and the one to write.

### 🏆 Golden Question for NM-8.4

#### 🎯 Given, $\frac{dy}{dx} = y - x$, where $y(0) = 2$, find $y(0.1)$ and $y(0.2)$ by using Runge-Kutta second order formula.
> **Appeared:** 2020 Q.7(c) — (05 marks)

**Full Answer:**

**Step 1. The method.** For $\frac{dy}{dx} = f(x,y)$ with $y(x_0) = y_0$ and step $h$, the second-order Runge-Kutta method is

$$
k_1 = h f(x_n, y_n), \qquad k_2 = h f\left(x_n + h, \; y_n + k_1\right), \qquad y_{n+1} = y_n + \frac{1}{2}(k_1 + k_2)
$$

Here $f(x,y) = y - x$ and the paper gives no step size. Two steps are needed to reach $0.2$, so take $h = 0.1$. Start at $x_0 = 0$, $y_0 = 2$.

**Step 2. Step 1: $x_0 = 0$ to $x_1 = 0.1$.**

$$
k_1 = 0.1 f(0, 2) = 0.1(2 - 0) = 0.2
$$

$$
k_2 = 0.1 f(0 + 0.1, \; 2 + 0.2) = 0.1(2.2 - 0.1) = 0.1(2.1) = 0.21
$$

$$
y_1 = 2 + \frac{0.2 + 0.21}{2} = 2 + 0.205 = 2.205000
$$

**Step 3. Step 2: $x_1 = 0.1$ to $x_2 = 0.2$.**

$$
k_1 = 0.1 f(0.1, 2.205) = 0.1(2.205 - 0.1) = 0.1(2.105) = 0.2105
$$

$$
k_2 = 0.1 f(0.1 + 0.1, \; 2.205 + 0.2105) = 0.1(2.4155 - 0.2) = 0.1(2.2155) = 0.22155
$$

$$
y_2 = 2.205 + \frac{0.2105 + 0.22155}{2} = 2.205 + 0.216025 = 2.421025
$$

| Step | $x_n$ | $y_n$ | $k_1$ | $k_2$ | $y_{n+1}$ |
| --: | --: | --: | --: | --: | --: |
| 1 | 0.0 | 2.000000 | 0.200000 | 0.210000 | 2.205000 |
| 2 | 0.1 | 2.205000 | 0.210500 | 0.221550 | 2.421025 |

$$
\boxed{y(0.1) = 2.2050, \qquad y(0.2) = 2.4210 \quad (h = 0.1)}
$$

> [!INFO] Check against the exact solution
> The equation is $\frac{dy}{dx} - y = -x$. The homogeneous solution is $Ce^x$ and a particular solution is $y_p = x + 1$, so $y = Ce^x + x + 1$ and $y(0) = 2$ gives $C = 1$: $y = e^x + x + 1$.
>
> | $x$ | Exact $e^x + x + 1$ | RK2 Heun $h=0.1$ | Error |
> | --: | --: | --: | --: |
> | 0.1 | 2.20517092 | 2.20500000 | $-0.000171$ |
> | 0.2 | 2.42140276 | 2.42102500 | $-0.000378$ |
>
> The errors are $-1.7\times10^{-4}$ and $-3.8\times10^{-4}$, which is the right size. For a second-order method the global error is $\frac{h^3}{6}\lvert y'''\rvert$, and $y''' = e^x$ here, so $\frac{0.001}{6}e^{0.1} = 1.84\times10^{-4}$ at $x = 0.1$.
>
> **RK4 for reference.** $h = 0.1$ gives $y(0.1) = 2.20517083$ and $y(0.2) = 2.42140257$, agreeing with the exact solution to $8 \times 10^{-8}$. RK4 is correct to eight digits where RK2 is right to four.

> [!NOTE] The other second-order method gives a different fourth digit
> The **Ralston** variant gives $2.204444$ and $2.419798$, with errors $-7.3 \times 10^{-4}$ and $-1.6 \times 10^{-3}$. All second-order methods converge at the same rate, but the constants differ and Ralston is about twice as far off here. **Heun's method is the one to write.** Never mix two second-order formulas in one answer.

> [!WARNING] Three traps
> **1. No step size is printed.** Two output points with a second-order method means two steps, so $h = 0.1$ is the natural reading. **State the choice.**
>
> **2. $f(x,y) = y - x$, not $x - y$.** The two have different solutions entirely. Here $f = y - x$, so $f(0, 2) = 2$, and $k_1 = 0.2$.
>
> **3. Use $y_n + k_1$ in $k_2$, not $y_n$.** The second slope is evaluated at the **end** of the step, at the predicted value. Substituting $y_n$ makes $k_2 = k_1$ and the method collapses to plain Euler.

---

#### 🎯 Using RK2 method with step size $h = 0.2$, calculate $y(0.2)$ and $y(0.4)$ for $\frac{dy}{dx} = x^2 - y$, $y(0) = 1$. Show both the predictor and corrector calculations at each step.
> **Appeared:** CT-02B Q.2(a) — (marks not printed in source)

**Full Answer:**

$$
\frac{dy}{dx} = x^2 - y, \qquad y(0) = 1, \qquad f(x,y) = x^2 - y
$$

**The two-stage form.** RK2 in Heun's arrangement is a predictor slope and a corrector slope averaged over the step:

$$
k_1 = f(x_n, y_n), \qquad k_2 = f\left(x_n + h,\ y_n + hk_1\right)
$$

$$
y_{n+1} = y_n + \frac{h}{2}\left(k_1 + k_2\right)
$$

**Step 1: $x_0 = 0$ to $x_1 = 0.2$, with $y_0 = 1$.**

$$
k_1 = 0^2 - 1 = -1
$$

$$
y_1^{*} = y_0 + hk_1 = 1 + 0.2(-1) = 0.8
$$

$$
k_2 = (0 + 0.2)^2 - \left(1 + 0.2(-1)\right) = 0.04 - 0.8 = -0.76
$$

$$
y_1 = 1 + \frac{0.2}{2}\left(-1 + (-0.76)\right) = 1 + 0.1(-1.76) = 1 - 0.176
$$

$$
\boxed{y(0.2) \approx 0.8240}
$$

**Step 2: $x_1 = 0.2$ to $x_2 = 0.4$, with $y_1 = 0.824$.**

$$
k_1 = (0.2)^2 - 0.824 = 0.04 - 0.824 = -0.784
$$

$$
y_2^{*} = 0.824 + 0.2(-0.784) = 0.824 - 0.1568 = 0.6672
$$

$$
k_2 = (0.2 + 0.2)^2 - 0.6672 = 0.16 - 0.6672 = -0.5072
$$

$$
y_2 = 0.824 + \frac{0.2}{2}\left(-0.784 + (-0.5072)\right) = 0.824 + 0.1(-1.2912) = 0.824 - 0.12912
$$

$$
\boxed{y(0.4) \approx 0.6949}
$$

**The results.**

| $x$ | $y$ |
| :--: | --: |
| 0.0 | 1.0000 |
| 0.2 | 0.8240 |
| 0.4 | 0.6949 |

> [!INFO] Check against the exact solution
> $y' + y = x^2$ has the particular solution $x^2 - 2x + 2$ and homogeneous part $Ce^{-x}$. With $y(0) = 1$ we get $C = -1$, so $y = x^2 - 2x + 2 - e^{-x}$, and $y(0.2) = 0.821269$ and $y(0.4) = 0.689680$.
>
> So RK2 with $h = 0.2$ overshoots by $0.002731$ at $x = 0.2$ and by $0.005200$ at $x = 0.4$. **The error grows as the interval is traversed.**
>
> The step-size effect is tested by halving $h$, not by going further along $x$. With $h = 0.1$ the same method gives $0.821928$ and $0.690931$, whose errors are $0.000658$ and $0.001251$. The ratios are $4.15$ and $4.16$, and $4 \approx 2^2$ is the second-order convergence signature.

> [!WARNING] Three traps in a two-stage method
> **The corrector must be evaluated at the predicted point**, not at the start of the step. Writing $k_2 = f(x_n + h, y_n)$ instead of $f(x_n+h, y_n + hk_1)$ reduces RK2 to the trapezoidal rule applied without the prediction, and it is no longer second order.
>
> **The predictor must not be used as the answer.** Heun's method reports $y_n + \frac{h}{2}(k_1 + k_2)$, not the predicted value $y_n + hk_1$. A method that returns its own predictor has silently degenerated to Euler.

---

## NM-8.6 — Higher-Order ODEs and Systems

### Theory

A single $n$th-order equation is converted into a system of $n$ first-order equations by introducing the intermediate derivatives. Then every marching method applies to the system unchanged.

For $\frac{d^2y}{dt^2} = F(t, y, y')$, set $v = \frac{dy}{dt}$, giving

$$
\frac{dy}{dt} = v, \qquad \frac{dv}{dt} = F(t, y, v)
$$

Euler on the system:

$$
y_{n+1} = y_n + h\,v_n, \qquad v_{n+1} = v_n + h\,F(t_n, y_n, v_n)
$$

Both updates use values from step $n$. The initial conditions of the original equation become the initial conditions of the system: $y(0) = 2$ and $v(0) = 0$.

### 🏆 Golden Question for NM-8.6

#### 🎯 Use the Euler's method to solve, $\frac{d^2 y}{dt^2} - 0.5t = y$ where, $y(0) = 2$ and $y'(0) = 0$. Solve from $t = 0$ to $0.4$ using $h = 0.1$.
> **Appeared:** 2018 Q.8(b) — (06 marks)

**Full Answer:**

**Convert to a first-order system.** Rearranging,

$$
\frac{d^2y}{dt^2} = y + 0.5t
$$

Introduce $v = \dfrac{dy}{dt}$. Then

$$
\frac{dy}{dt} = v, \qquad \frac{dv}{dt} = y + 0.5t
$$

with $y(0) = 2$ and $v(0) = 0$.

**Euler's method applied to both equations.**

$$
y_{n+1} = y_n + h\,v_n
$$

$$
v_{n+1} = v_n + h\,(y_n + 0.5t_n)
$$

**Step 1.** $t_0 = 0$, $y_0 = 2$, $v_0 = 0$.

$$
y_1 = 2 + 0.1(0) = 2.0
$$

$$
v_1 = 0 + 0.1(2 + 0) = 0.2
$$

**Step 2.** $t_1 = 0.1$, $y_1 = 2.0$, $v_1 = 0.2$.

$$
y_2 = 2.0 + 0.1(0.2) = 2.02
$$

$$
v_2 = 0.2 + 0.1(2.0 + 0.05) = 0.2 + 0.205 = 0.405
$$

**Step 3.** $t_2 = 0.2$, $y_2 = 2.02$, $v_2 = 0.405$.

$$
y_3 = 2.02 + 0.1(0.405) = 2.0605
$$

$$
v_3 = 0.405 + 0.1(2.02 + 0.1) = 0.405 + 0.212 = 0.617
$$

**Step 4.** $t_3 = 0.3$, $y_3 = 2.0605$, $v_3 = 0.617$.

$$
y_4 = 2.0605 + 0.1(0.617) = 2.1222
$$

$$
v_4 = 0.617 + 0.1(2.0605 + 0.15) = 0.617 + 0.22105 = 0.83805
$$

**The results.**

| $t$ | $y$ | $v = y'$ |
| :--: | :-- | :-- |
| 0.0 | 2.0000 | 0.0000 |
| 0.1 | 2.0000 | 0.20000 |
| 0.2 | 2.0200 | 0.40500 |
| 0.3 | 2.0605 | 0.61700 |
| 0.4 | 2.1222 | 0.83805 |

$$
\boxed{y(0.4) = 2.1222}
$$

> [!INFO] Check against the exact solution
> The equation $\ddot y - \tfrac12 t = y$ has the solution $y = C_1 e^{-t} + C_2 e^{t} - \tfrac12 t$, and the two initial conditions give $y = 2\cosh t + \tfrac12\sinh t - \tfrac12 t$. At $t = 0.4$ that is $y(0.4) = 2.167521$, against which the Euler value $2.1222$ is low by $0.0453$, about $2.1\%$. That shortfall is the expected truncation error of a first-order method.
>
> Halving $h$ to $0.05$ and running eight steps gives $y(0.4) = 2.144385$, and halving it again to $0.025$ gives $2.155822$: the successive gains are $0.022$ and $0.011$, in the ratio $2:1$ that an $O(h)$ error requires.

---

## NM-8.7 — ODE Formulation from Physical Problems

### Theory

A physical statement becomes an ODE when the **rate** is expressed as proportional to the **quantity**. "Loses 4% of its remaining charge per second" means the rate of loss is $4\%$ of the charge present, not a constant $4$ C/s. Recognising this distinction is the whole of the modelling question.

### 🏆 Golden Question for NM-8.7

#### 🎯 A capacitor loses 4% of its remaining charge every second. It is fully charged with 100 Coulomb of charge. What will be the remaining charge after 10 sec. Develop the ODE and also determine the solution.
> **Appeared:** 2021 Q.5(c) — (04 marks)

**Full Answer:**

**Step 1. Set up the rate equation.** Losing $4\%$ of the remaining charge each second means the loss is **proportional to the charge present**, not a constant $4$ C per second. If $Q$ is the charge and $t$ the time,

$$
\frac{dQ}{dt} = -0.04\,Q, \qquad Q(0) = 100
$$

The negative sign is essential: the charge is decreasing.

**Step 2. Solve by separation of variables.**

$$
\frac{dQ}{Q} = -0.04\,dt
$$

Integrating,

$$
\ln Q = -0.04\,t + C
$$

At $t = 0$, $\ln 100 = C$, so

$$
Q(t) = 100\,e^{-0.04t}
$$

**Step 3. Evaluate at $t = 10$ s.**

$$
Q(10) = 100\,e^{-0.4} = 100(0.670320046) = 67.0320
$$

$$
\boxed{Q(10) = 67.03 \text{ Coulomb}}
$$

> [!INFO] Check by an independent route
> **Discrete compounding.** "Loses 4% of its remaining charge every second" read literally gives, second by second, $Q(10) = 100(0.96)^{10} = 66.4833$. **Euler's method** with $h = 1$, which is exactly that recursion, returns $Q(10) = 66.4833$ as well.
>
> The continuous answer $67.0320$ is $0.8\%$ higher. Both are defensible readings of the question.
>
> | Reading | Value | Character |
> | :-- | --: | :-- |
> | Continuous exponential | 67.0320 | The physically correct law. Each individual decay is small, so compounding is continuous |
> | Discrete $0.96^n$ | 66.4833 | Treats each second as one exact $4\%$ step. Slightly under, since $1-0.04 < e^{-0.04}$ |
>
> The general identity is $(1-r)^n < e^{-rn}$ for $0<r<1$, so the discrete answer always under-reads. A capacitor really does decay continuously, so $67.0320$ is the intended answer.

> [!NOTE] Half-life as a check
> From $Q(t) = Q_0e^{-t/\tau}$ with $\tau = 25$ s, the half-life is $17.33$ s. So in 10 s the charge should be somewhat **more** than half of 100, which is exactly what 67.03 shows.

---

## NM-8.8 — Boundary Value Problems ⚠️

> [!CAUTION] This is the danger zone
> 2021 Q.5(b) gave a full 5 marks to this, and 2024 Q.4(a) asked the theory. Learn the tridiagonal construction and the sign of the diagonal.

### Theory

**The shared starting point.** Both IVPs and BVPs replace derivatives by finite differences and solve the resulting algebraic system. The difference is which equations end up in that system.

**Boundary value problem: the general approach.**

1. Discretise the domain into a grid of $n + 1$ points.
2. Replace every derivative by a finite difference, usually the centred one $y''(x_i) \approx \frac{y_{i+1} - 2y_i + y_{i-1}}{h^2}$.
3. Apply the boundary conditions as algebraic equations replacing the unavailable end rows.
4. Solve the full linear system for all unknowns at once.

$$
\begin{cases}
y_0 = 0 \\
-\dfrac{y_{i-1} - 2y_i + y_{i+1}}{h^2} = f_i, \quad 1 \le i \le n-1 \\
y_n = 1
\end{cases}
$$

The interior equations couple neighbours, so the system is **tridiagonal**. The standard efficient methods are the Thomas algorithm, or an iterative sweep such as Gauss-Seidel, which works because the system is diagonally dominant.

**Key differences**

| | Initial value problem | Boundary value problem |
| :-- | :-- | :-- |
| Conditions | Given at one end | Given at both ends |
| Direction | Marches forward from the start | Whole domain solved at once |
| System structure | Lower triangular | Tridiagonal |
| Cost per step | Very low | Full linear solve |
| Sensitivity | Local, errors stay near the start | Global, a change anywhere moves the whole solution |
| Shooting method | Not applicable | Reduces a BVP to an IVP by adjusting the unknown start value until the far end matches |

> [!NOTE] Where this exam meets the topic again
> The Gauss-Seidel iteration in part (b) of Question 2 is the same algorithm used on the tridiagonal system here. See [NM-3.5: Gauss-Seidel Iteration](NM-3.5_Gauss_Seidel_Iteration.md) and [NM-3.8: Circuit Applications](NM-3.8_Circuit_Applications.md).

### 🏆 Golden Question for NM-8.8

#### 🎯 Solve the boundary value problem $\frac{d^2y}{dx^2} - y = 0$ with $y(0) = 0$ and $y(2) = 3.62686$.
> **Appeared:** 2021 Q.5(b) — (05 marks, CO: 3)

**Full Answer:**

**Step 1. Discretise.** With the centred difference for $y''$,

$$
\frac{y_{i-1} - 2y_i + y_{i+1}}{h^2} - y_i = 0
$$

Multiplying by $h^2$,

$$
y_{i-1} - (2 + h^2)\,y_i + y_{i+1} = 0
$$

The system is tridiagonal with diagonal $-(2+h^2)$ and off-diagonal $1$. Note that the matrix is **negatively diagonally dominant**, since $\lvert 2+h^2\rvert > 1+1$, hence the solution is unique and the standard Thomas algorithm applies without pivoting.

**Step 2. Solve with $h = 0.5$.** Then $n = 4$ subintervals and 3 interior nodes at $x = 0.5, 1.0, 1.5$. With $y_0 = 0$ and $y_4 = 3.62686$:

$$
\begin{cases}
-(2.25)y_1 + y_2 = 0 \\
y_1 - (2.25)y_2 + y_3 = 0 \\
y_2 - (2.25)y_3 = -3.62686
\end{cases}
$$

From the first, $y_2 = 2.25\,y_1$. Substituting into the second,

$$
y_1 - 2.25(2.25y_1) + y_3 = 0 \Rightarrow y_3 = 4.0625\,y_1
$$

The third then gives $2.25y_1 - 2.25(4.0625y_1) = -3.62686$, that is $2.25y_1(1 - 4.0625) = -3.62686$, so $-6.890625\,y_1 = -3.62686$ and $y_1 = 0.526347$.

$$
y_2 = 2.25(0.526347) = 1.184281, \qquad y_3 = 4.0625(0.526347) = 2.138285
$$

| $x$ | $y$ (numerical, $h = 0.5$) | Exact | Error |
| --: | --: | --: | --: |
| 0.5 | 0.526347 | 0.521095 | $+0.005252$ |
| 1.0 | 1.184281 | 1.175201 | $+0.009080$ |
| 1.5 | 2.138285 | 2.129279 | $+0.009006$ |

**Step 3. Refine.** Halving $h$ should cut the error by about 4, since the scheme is second order.

| $h$ | Interior nodes | Largest error |
| --: | --: | --: |
| 1 | 1 | 0.03375 |
| 0.5 | 3 | 0.00908 |
| 0.25 | 7 | 0.00249 |
| 0.125 | 15 | 0.00063 |

The ratio $0.00908 / 0.00249 = 3.65$ is close to the expected 4, confirming second-order accuracy.

$$
\boxed{y(0.5) = 0.5263,\quad y(1.0) = 1.1843,\quad y(1.5) = 2.1383 \quad (h = 0.5)}
$$

> [!INFO] Check against the continuous solution
> The ODE $y'' - y = 0$ has the general solution $y = A\cosh x + B\sinh x$. From $y(0) = 0$, $A = 0$. From $y(2) = 3.62686$,
> $$
> B = \frac{3.62686}{\sinh 2} = \frac{3.62686}{3.6268604} = 0.99999989
> $$
> so $y = 3.62686\,\frac{\sinh x}{\sinh 2}$. Exact values at the three interior nodes are $0.521095$, $1.175201$ and $2.129279$. The numerical values overshoot by under $1\%$, as expected for a second-order scheme on a growing exponential.

> [!NOTE] Check the sign and the dominance before iterating
> The matrix is **negatively diagonally dominant**, since $\lvert 2+h^2\rvert > 1+1$ for every $h$. That guarantees a unique solution and means the standard Thomas algorithm applies **without pivoting**.
>
> Worth pausing on, because it is the first question in this paper where the sign of $y_i$ on the diagonal is decided by the ODE rather than by taste. $y'' - y = 0$ gives $\frac{y_{i-1}-2y_i+y_{i+1}}{h^2} = y_i$, and moving $y_i$ across gives a diagonal of $-(2+h^2)$, not $+(2+h^2)$. Writing the positive sign produces a system with a completely different spectrum and, for this $y(2)$, no consistent solution.
>
> The printed $y(2) = 3.62686$ is a rounded value: $\sinh 2 = 3.6268604\ldots$ gives $B$ exactly $1$ to seven figures, so the intended exact solution is almost certainly $y = \sinh x$.

---

#### 🎯 Describe the general approach for solving boundary value problems numerically. How does it differ from solving initial value problems?
> **Appeared:** 2024 Q.4(a) — (04 marks)

**Full Answer:**

**The shared starting point.** Both replace derivatives by finite differences and solve the resulting algebraic system. The difference is which equations end up in that system.

**Initial value problem.** One condition is given at one end of the domain, for example $y(0) = 1$. Marching step by step from there, each new row uses only the row just computed.

$$
y_{i+1} = f(x_i, y_i) h + O(h^2)
$$

This works because the system is **lower triangular in the unknowns**. It is simple, needs no iteration, and each step is cheap.

**Boundary value problem.** Conditions are given at **both** ends, for example $y(0) = 0$ and $y(1) = 1$. No starting value is known, so the grid cannot be filled row by row.

**The general approach.**

1. Discretise the domain into a grid of $n + 1$ points.
2. Replace every derivative by a finite difference, usually the centred one $y''(x_i) \approx \frac{y_{i+1} - 2y_i + y_{i-1}}{h^2}$.
3. Apply the boundary conditions as algebraic equations replacing the unavailable end rows.
4. Solve the full linear system for all unknowns at once.

$$
\begin{cases}
y_0 = 0 \\
-\dfrac{y_{i-1} - 2y_i + y_{i+1}}{h^2} = f_i, \quad 1 \le i \le n-1 \\
y_n = 1
\end{cases}
$$

The interior equations couple neighbours, so the system is **tridiagonal**. The standard efficient methods are the Thomas algorithm, or an iterative sweep such as Gauss-Seidel, which works because the system is diagonally dominant.

**Key differences**

| | Initial value problem | Boundary value problem |
| :-- | :-- | :-- |
| Conditions | Given at one end | Given at both ends |
| Direction | Marches forward from the start | Whole domain solved at once |
| System structure | Lower triangular | Tridiagonal |
| Cost per step | Very low | Full linear solve |
| Sensitivity | Local, errors stay near the start | Global, a change anywhere moves the whole solution |
| Shooting method | Not applicable | Reduces a BVP to an IVP by adjusting the unknown start value until the far end matches |

---

## Exam Variants

| Year | Question | Subtopic | Key Answer |
| :--- | :--- | :-- | :--- |
| 2017 Q.8(a) | Modified Euler, $y(0.02)$ | NM-8.3 | $\boxed{y(0.02) = 1.020204}$ |
| 2018 Q.7(a) | Modified Euler tabulate $0.1, 0.2, 0.3$ | NM-8.3 | $\boxed{y(0.1) = 0.095, \qquad y(0.2) = 0.181, \qquad y(0.3) = 0.259}$ |
| 2018 Q.8(b) | Euler on a second-order system | NM-8.6 | $\boxed{y(0.4) = 2.1222}$ |
| 2020 Q.7(a) | Derive modified Euler + limitation | NM-8.3 | $\boxed{y_{n+1} = y_n + \frac{h}{2}\left[f(x_n,y_n) + f(x_n+h,\, y_n + h f(x_n,y_n))\right],\quad \text{second order}}$ |
| 2020 Q.7(c) | RK2, $y(0.1)$, $y(0.2)$ | NM-8.4 | $\boxed{y(0.1) = 2.2050, \qquad y(0.2) = 2.4210 \quad (h = 0.1)}$ |
| 2021 Q.5(a) | Define IVP and BVP | NM-8.1 | $\boxed{\text{IVP: conditions at one end, march forward. BVP: conditions at both ends, solve together.}}$ |
| 2021 Q.5(b) | Solve a BVP | NM-8.8 | $\boxed{y(0.5) = 0.5263,\quad y(1.0) = 1.1843,\quad y(1.5) = 2.1383 \quad (h = 0.5)}$ |
| 2021 Q.5(c) | Capacitor discharge ODE | NM-8.7 | $\boxed{Q(10) = 67.03 \text{ Coulomb}}$ |
| 2024 Q.4(a) | BVP approach vs IVP | NM-8.8 | Four-step construction, tridiagonal system |
| CT-02B Q.2(a) | RK2 predictor + corrector | NM-8.4 | $\boxed{y(0.2) \approx 0.8240}$ and $\boxed{y(0.4) \approx 0.6949}$ |

---

## ⚡ Exam Tips & Common Mistakes

1. **Predictor first, corrector second.** Heun's method computes $\hat y_{n+1} = y_n + h f(x_n, y_n)$, then averages. Writing the answer as the predictor alone silently gives Euler.
2. **The corrector is evaluated at the predicted point**, not at the start of the step. Using $y_n$ there collapses the method.
3. **"Modified Euler" is ambiguous.** It can mean Heun or the midpoint method. Both are second order. Read the recursion, not the name.
4. **For a system, update both variables from the old step.** In 2018 Q.8(b) both $y$ and $v$ are updated using step-$n$ values.
5. **The BVP diagonal sign comes from the ODE.** $y'' - y = 0$ gives diagonal $-(2 + h^2)$, not $+(2+h^2)$. The wrong sign produces a system with no consistent solution.
6. **Count interior nodes, not points.** With $h = 0.5$ on $[0, 2]$ there are 4 subintervals and 3 unknowns $y_1, y_2, y_3$. The boundary values $y_0$ and $y_4$ are given, not unknown.
7. **"Loses 4% of remaining" means proportional to the amount present.** A constant $4$ C/s loss is a different problem entirely.

## 🔗 Related Topics

- [NM-8.2: Euler's Method](NM-8.2_Eulers_Method.md) — the predictor inside Heun's method
- [NM-8.5: Runge-Kutta 4th Order](NM-8.5_Runge_Kutta_4th_Order.md) — the fourth-order method that supersedes RK2
- [NM-3.5: Gauss-Seidel Iteration](NM-3.5_Gauss_Seidel_Iteration.md) — the iterative solver for tridiagonal BVP systems
- [NM-9: Eigenvalue Problems](NM-9_Eigenvalue_Problems.md) — next in the chain

---

[← Previous: NM-8.5 Runge-Kutta 4th Order](NM-8.5_Runge_Kutta_4th_Order.md) | [🏠 Index](00_Index.md) | [Next: NM-9 Eigenvalue Problems →](NM-9_Eigenvalue_Problems.md)