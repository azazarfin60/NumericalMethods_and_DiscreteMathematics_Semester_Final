[← Previous: NM-8.2 Euler's Method](NM-8.2_Eulers_Method.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: NM-8.4 RK2 →](NM-8.4_RK2.md)

---

# NM-8.3: Modified Euler / Heun's Method

> 🟠 **Priority:** Secondary | **Tested:** 3/8 years (2017, 2018, 2020) | **Typical marks:** 4–5

## What This Is (and Why It Matters)

Plain Euler has an obvious flaw: it calculates the slope at the very beginning of the interval ($x_n$) and assumes that exact slope stays true all the way to the end ($x_{n+1}$). For any curve that bends, that assumption causes the solution to drift off track rapidly.

Heun's method (frequently called **Modified Euler** or **Improved Euler**) fixes this with a brilliant two-step strategy called a **predictor-corrector**:
1. **Predict:** Use plain Euler to take a quick preliminary leap to the end of the step and guess what the future $y$ value looks like.
2. **Correct:** Evaluate the slope at that future point, average it with your starting slope, and take the real step using that balanced two-slope average.

By averaging the beginning slope and the ending slope, the primary error term cancels out completely. That jumps your method from first-order $O(h)$ all the way to second-order $O(h^2)$ global accuracy, for the price of just one extra slope calculation per step.

---

## 📝 Key Definitions

> **Modified Euler's Method:** "Instead of approximating $f(x, y)$ by $f(x_0, y_0)$ in Eq. (8.6), we now approximate the integral given in Eq. (8.6) by means of trapezoidal rule to obtain $y_1 = y_0 + \frac{h}{2} [f(x_0, y_0) + f(x_1, y_1)]$." -- Jain, §8.4.2 (p. 310), Eq. (8.13)
>
> **In simple words:** Instead of using only the starting slope, you use the trapezoidal rule to average the slope at the start of the step and the slope at the end of the step.

> **Predictor-Corrector Method:** "A predictor-corrector method uses an explicit formula to predict an initial estimate of the next value, and then uses an implicit formula to correct and refine that estimate." -- Jain, §8.6 (p. 315)
>
> **In simple words:** First make a rough guess of where you will land using a simple formula (the predictor), then calculate the slope at that guess and use it to compute an accurate final step (the corrector).

> **Second-Order Convergence:** "The error in this formula can be shown to be of order $h^3$ by expanding both sides by Taylor's series ... so that the method has an $h^2$-order of global convergence." -- Jain, §8.5 (p. 311, 314)
>
> **In simple words:** Halving the step size cuts the global error by a factor of 4 ($2^2$). It converges much faster than plain Euler.

---

## The Core Idea

### 1. Derivation from the Integral Equation

Consider the initial value problem:

$$
\frac{dy}{dx} = f(x, y), \qquad y(x_n) = y_n
$$

Integrating both sides over one step from $x_n$ to $x_{n+1} = x_n + h$:

$$
\int_{x_n}^{x_{n+1}} \frac{dy}{dx} \, dx = \int_{x_n}^{x_{n+1}} f(x, y) \, dx
$$

$$
y_{n+1} - y_n = \int_{x_n}^{x_{n+1}} f(x, y) \, dx
$$

$$
y_{n+1} = y_n + \int_{x_n}^{x_{n+1}} f(x, y) \, dx
$$

Plain Euler approximates this integral by a single rectangle using the left endpoint height $f(x_n, y_n)$.
Heun's method approximates the integral using the **trapezoidal rule**:

$$
\int_{x_n}^{x_{n+1}} f(x, y) \, dx \approx \frac{h}{2} \left[ f(x_n, y_n) + f(x_{n+1}, y_{n+1}) \right]
$$

This gives the implicit trapezoidal formula:

$$
y_{n+1} = y_n + \frac{h}{2} \left[ f(x_n, y_n) + f(x_{n+1}, y_{n+1}) \right]
$$

Notice the catch: $y_{n+1}$ appears on both the left side and inside the right-hand function $f(x_{n+1}, y_{n+1})$. To make this an explicit, practical algorithm, we use **plain Euler** to predict $y_{n+1}$ first!

### 2. The Predictor-Corrector Equations

**Step 1 (Predictor):** Use plain Euler to calculate a preliminary guess $\hat{y}_{n+1}$:

$$
\hat{y}_{n+1} = y_n + h f(x_n, y_n)
$$

**Step 2 (Corrector):** Evaluate the slope at the predicted point and average the two slopes:

$$
y_{n+1} = y_n + \frac{h}{2} \left[ f(x_n, y_n) + f(x_n + h, \hat{y}_{n+1}) \right]
$$

Substituting the predictor directly into the corrector gives the single unified formula:

$$
y_{n+1} = y_n + \frac{h}{2}\left[ f(x_n, y_n) + f(x_n + h, y_n + h f(x_n, y_n)) \right]
$$

### 3. Accuracy and Error Cancellation

Why does averaging two slopes buy an entire order of accuracy?
- The local truncation error of the trapezoidal quadrature rule is $-\frac{1}{12} h^3 y'''(\tau)$.
- Because the local error per step is $O(h^3)$, dividing by step size $h$ over the full interval gives a global error of:

$$
\text{Global Truncation Error} \approx \frac{L}{h} \times O(h^3) = O(h^2)
$$

This makes Heun's method a **second-order method**. Every time you cut $h$ in half, your error shrinks by $4$.

### 4. Why Plain Euler Failed (and Motivated This Method)

The 2020 exam specifically asked: *"What is the major limitation of Euler's method?"*
There are two major limitations:

1. **Low order of accuracy ($O(h)$):**
   Reaching four decimal places of accuracy with plain Euler requires step sizes around $h = 10^{-4}$ (meaning 10,000 steps). But taking 10,000 steps accumulates substantial round-off error from finite machine precision, creating a severe accuracy ceiling.
2. **Conditional stability on stiff systems:**
   For a decay equation $y' = \lambda y$ with $\lambda < 0$, Euler is only stable when $h < \frac{2}{|\lambda|}$. If $\lambda$ is large (a stiff system, common in circuits with fast transients), $h$ must be microscopic, making computation intolerably slow.

> [!WARNING] The Naming Trap: Heun vs. Midpoint
> In literature and lecture notes, the name "Modified Euler" is sometimes used for two different second-order methods:
> 1. **Heun's Method (Trapezoidal):** Averages slopes at $x_n$ and $x_n + h$. This is the standard RUET syllabus convention.
> 2. **The Midpoint Method:** Uses the slope at the half-step midpoint $x_n + h/2$, which is $y_{n+1} = y_n + h f\left(x_n + \frac{h}{2}, \, y_n + \frac{h}{2} f(x_n, y_n)\right)$.
>
> Both are second order, but Heun's method is the exact formula requested when RUET asks to "derive modified Euler".

---

## 🔧 Worked Example

> **From:** 2017 Q.8(a) -- [Marks: 04]

**The question:** Given the differential equation $\frac{dy}{dx} = x^2 + y$ with $y(0) = 1$, compute $y(0.02)$ using Euler's modified method.

**Let's solve this step by step.**

Here our ODE is $f(x, y) = x^2 + y$, our initial values are $x_0 = 0, y_0 = 1$, and our step size is $h = 0.02$. We need to reach $x = 0.02$ in a single step.

### Step 1: Evaluate the initial slope

At $(x_0, y_0) = (0, 1)$:

$$
f(x_0, y_0) = 0^2 + 1 = 1
$$

### Step 2: Calculate the Euler predictor ($\hat{y}_1$)

Take a preliminary Euler step:

$$
\hat{y}_1 = y_0 + h f(x_0, y_0) = 1 + 0.02(1) = 1.02
$$

### Step 3: Evaluate the slope at the predicted point

The endpoint is $x_1 = 0.02$, and our predicted ordinate is $\hat{y}_1 = 1.02$:

$$
f(x_1, \hat{y}_1) = (0.02)^2 + 1.02 = 0.0004 + 1.02 = 1.0204
$$

### Step 4: Apply the trapezoidal corrector

Average the two slopes:

$$
y_1 = y_0 + \frac{h}{2} \left[ f(x_0, y_0) + f(x_1, \hat{y}_1) \right]
$$

$$
y_1 = 1 + \frac{0.02}{2} [1 + 1.0204] = 1 + 0.01(2.0204) = 1 + 0.020204
$$

$$
\boxed{y(0.02) = 1.020204}
$$

**Quick sanity check:**
The exact analytical solution of $y' - y = x^2$ with $y(0) = 1$ is:

$$
y(x) = 3e^x - (x^2 + 2x + 2)
$$

At $x = 0.02$:

$$
y(0.02) = 3e^{0.02} - (0.0004 + 0.04 + 2) \approx 3(1.02020134) - 2.0404 = 1.02020402
$$

Heun's result $1.020204$ differs from the true value by only $2 \times 10^{-8}$! Plain Euler would have given $1.02$, so the corrector gained three extra decimal places of accuracy in a single step.

---

## 🏆 Past Exam Questions

### 2020 Q.7(a): Derive Modified Euler & Discuss Limitation -- [05 Marks]

**The question:** Derive modified Euler's method. What is the major limitation of Euler's method?

**Full Answer:**

**1. Derivation of Modified Euler's Method:**
Consider the first-order differential equation:

$$
\frac{dy}{dx} = f(x, y), \qquad y(x_0) = y_0
$$

Integrating from $x_n$ to $x_{n+1} = x_n + h$:

$$
y_{n+1} = y_n + \int_{x_n}^{x_{n+1}} f(x, y) \, dx
$$

Approximating the integral by the trapezoidal rule gives:

$$
y_{n+1} = y_n + \frac{h}{2} [f(x_n, y_n) + f(x_{n+1}, y_{n+1})]
$$

Since $y_{n+1}$ on the right-hand side is unknown, we predict it using Euler's formula:

$$
\hat{y}_{n+1} = y_n + h f(x_n, y_n)
$$

Substituting this predictor into the corrector yields the modified Euler (Heun) formula:

$$
\boxed{y_{n+1} = y_n + \frac{h}{2}\left[f(x_n, y_n) + f(x_n + h, y_n + h f(x_n, y_n))\right]}
$$

$$
\boxed{y_{n+1} = y_n + \frac{h}{2}\left[f(x_n,y_n) + f(x_n+h,\, y_n + h f(x_n,y_n))\right],\quad \text{second order}}
$$

The local truncation error is $O(h^3)$, giving a global truncation error of $O(h^2)$ (second-order accuracy).

**2. Major Limitations of Euler's Method:**
1. **Low order of accuracy:** The global error is $O(h)$, requiring a very small step size $h$ to achieve acceptable precision. This leads to excessive computation and severe round-off error accumulation.
2. **Conditional stability:** For stiff equations $y' = \lambda y$ ($\lambda < 0$), Euler is stable only when $h < \frac{2}{|\lambda|}$, making it unsuitable for problems with rapid decay rates.

---

### 2018 Q.7(a): Tabulate Solutions for $y' = 1 - y$ -- [05 Marks]

**The question:** Solve $\frac{dy}{dx} = 1 - y$ with the initial condition $x = 0, y = 0$ by using modified Euler's method. Tabulate the solutions at $x = 0.1, 0.2, 0.3$.

**Let's solve this step by step:**

Here $f(x, y) = 1 - y$, $x_0 = 0, y_0 = 0$, and $h = 0.1$.
For each step:
- Predictor: $\hat{y}_{n+1} = y_n + 0.1(1 - y_n)$
- Corrector: $y_{n+1} = y_n + 0.05[(1 - y_n) + (1 - \hat{y}_{n+1})]$

### Step 1 ($x_0 = 0 \to x_1 = 0.1$):
- Starting slope: $f(0, 0) = 1 - 0 = 1$
- Predictor: $\hat{y}_1 = 0 + 0.1(1) = 0.1$
- Predicted slope: $f(0.1, 0.1) = 1 - 0.1 = 0.9$
- Corrector:

$$
y_1 = 0 + 0.05(1 + 0.9) = 0.05(1.9) = 0.0950000
$$

### Step 2 ($x_1 = 0.1 \to x_2 = 0.2$):
- Current point: $x_1 = 0.1, y_1 = 0.095$
- Starting slope: $f(0.1, 0.095) = 1 - 0.095 = 0.905$
- Predictor: $\hat{y}_2 = 0.095 + 0.1(0.905) = 0.1855$
- Predicted slope: $f(0.2, 0.1855) = 1 - 0.1855 = 0.8145$
- Corrector:

$$
y_2 = 0.095 + 0.05(0.905 + 0.8145) = 0.095 + 0.05(1.7195) = 0.1809750
$$

### Step 3 ($x_2 = 0.2 \to x_3 = 0.3$):
- Current point: $x_2 = 0.2, y_2 = 0.1809750$
- Starting slope: $f(0.2, 0.1809750) = 1 - 0.1809750 = 0.8190250$
- Predictor: $\hat{y}_3 = 0.1809750 + 0.1(0.8190250) = 0.2628775$
- Predicted slope: $f(0.3, 0.2628775) = 1 - 0.2628775 = 0.7371225$
- Corrector:

$$
y_3 = 0.1809750 + 0.05(0.8190250 + 0.7371225) = 0.1809750 + 0.05(1.5561475) = 0.2587824
$$

### Tabulated Solutions

| $x$ | Computed $y$ (Modified Euler) | Exact $y = 1 - e^{-x}$ |
|:---:|:---:|:---:|
| 0.1 | $0.0950000$ | $0.0951626$ |
| 0.2 | $0.1809750$ | $0.1812692$ |
| 0.3 | $0.2587824$ | $0.2591818$ |

$$
\boxed{y(0.1) = 0.095, \qquad y(0.2) = 0.181, \qquad y(0.3) = 0.259}
$$

---

### Exam Variants at a Glance

| Year | What They Asked | ODE & Parameters | Key Answer |
|:---|:---|:---|:---|
| **2017 Q.8(a)** | Compute $y(0.02)$ using modified Euler | $y' = x^2 + y, y(0) = 1, h = 0.02$ | $\boxed{y(0.02) = 1.020204}$ |
| **2018 Q.7(a)** | Tabulate solutions at $x = 0.1, 0.2, 0.3$ | $y' = 1 - y, y(0) = 0, h = 0.1$ | $\boxed{y(0.1) = 0.095, \qquad y(0.2) = 0.181, \qquad y(0.3) = 0.259}$ |
| **2020 Q.7(a)** | Derive modified Euler + limitation of Euler | Theory | $\boxed{y_{n+1} = y_n + \frac{h}{2}\left[f(x_n, y_n) + f(x_n + h, y_n + h f(x_n, y_n))\right]}$ |

---

## ⚡ Quick Review

**The method in one sentence:** Predict a future point with plain Euler, calculate the slope there, and take the real step using the average of the two slopes.

**The formulas you must memorize:**
- **Predictor:** $\hat{y}_{n+1} = y_n + h f(x_n, y_n)$
- **Corrector:** $y_{n+1} = y_n + \frac{h}{2} [f(x_n, y_n) + f(x_{n+1}, \hat{y}_{n+1})]$

**The most common exam mistake:** Forgetting to substitute the predicted $\hat{y}_{n+1}$ into the second slope evaluation and accidentally plugging in the old $y_n$ instead.

**Time estimate in exam:** 8–10 minutes for derivation and a three-step table.

---

## 🔗 Connected Topics

- [← NM-8.2: Euler's Method](NM-8.2_Eulers_Method.md) -- the predictor formula used inside Heun's method.
- [→ NM-8.4: Runge-Kutta 2nd Order](NM-8.4_RK2.md) -- the formal stage-slope representation ($k_1, k_2$) of this exact method.
- [NM-8.5: Runge-Kutta 4th Order](NM-8.5_RK4.md) -- extending slope averaging to four points for $O(h^4)$ precision.
- [NM-5.1: Trapezoidal Rule](../NM-5_Integration/NM-5.1_Trapezoidal_Rule.md) -- the numerical integration rule that provides the derivation foundation for Heun's method.

---

[← Previous: NM-8.2 Euler's Method](NM-8.2_Eulers_Method.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: NM-8.4 RK2 →](NM-8.4_RK2.md)
