[← Previous: NM-8.3 Heun's Method](NM-8.3_Heuns_Method.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: NM-8.5 RK4 →](NM-8.5_RK4.md)

---

# NM-8.4: Runge-Kutta 2nd Order (RK2)

> 🟠 **Priority:** Secondary | **Tested:** 2/8 years (2020, CT-02B) | **Typical marks:** 4–5

## What This Is (and Why It Matters)

If you want higher-order accuracy from a Taylor series, calculus says you must differentiate the differential equation again and again to find $y''$, $y'''$, and $y^{(4)}$. For complex engineering equations, taking higher-order analytical derivatives is an algebraic nightmare.

The **Runge-Kutta family** solves this cleanly. It gives you the exact same accuracy as a high-order Taylor series, but *without calculating a single derivative of $f(x, y)$*. Instead, it evaluates the basic function $f(x, y)$ at a few cleverly chosen test points across the step and combines them with specific mathematical weights.

**Runge-Kutta 2nd Order (RK2)** uses two stage evaluations ($k_1$ and $k_2$) per step. While Heun's method expresses this as a predictor-corrector loop, RK2 formalizes it as a weighted sum of slopes. It is the stepping stone to understanding the famous fourth-order RK4 method.

---

## 📝 Key Definitions

> **The Runge-Kutta Principle:** "The Runge–Kutta methods are designed to give greater accuracy and they possess the advantage of requiring only the function values at some selected points on the subinterval." -- Jain, §8.5 (p. 311)
>
> **In simple words:** You get the precision of high-order Taylor series without having to do complicated calculus derivatives, just by sampling the basic function $f(x, y)$ at strategic points.

> **Second-Order Runge-Kutta Formula (Heun Form):** "$y_1 = y_0 + \frac{1}{2}(k_1 + k_2)$ where $k_1 = h f_0$ and $k_2 = h f(x_0 + h, y_0 + k_1)$." -- Jain, §8.5 (p. 311), Eq. (8.15)
>
> **In simple words:** Calculate the initial step increment $k_1$, use it to evaluate an end-of-step increment $k_2$, and take the average of the two increments to update $y$.

> **The RK2 Parameter Family:** "Equating the coefficients of $f(x, y)$ and its derivatives on both sides, we obtain the relations $W_1 + W_2 = 1, W_2 \alpha_0 = \frac{1}{2}, W_2 \beta_0 = \frac{1}{2}$." -- Jain, §8.5 (p. 312), Eq. (8.17)
>
> **In simple words:** RK2 is not just one single formula. It is an entire family of formulas with one free mathematical knob. Setting the knob to 1 gives Heun's method, setting it to $1/2$ gives the midpoint method, and setting it to $3/4$ gives Ralston's method.

---

## The Core Idea

### 1. The Two $k$-Values Formulation

For solving $\frac{dy}{dx} = f(x, y)$ with $y(x_0) = y_0$ and step size $h$, the classical Heun form of RK2 is written in two interchangeable ways:

#### Increment Convention ($h$ included inside $k$):
Here, $k_1$ and $k_2$ represent actual vertical shifts ($\Delta y$):

$$
k_1 = h f(x_n, y_n)
$$

$$
k_2 = h f(x_n + h, \; y_n + k_1)
$$

$$
y_{n+1} = y_n + \frac{1}{2}(k_1 + k_2)
$$

#### Slope Convention (slopes without $h$):
Here, $k_1$ and $k_2$ represent slopes, and $h$ sits outside:

$$
k_1 = f(x_n, y_n)
$$

$$
k_2 = f(x_n + h, \; y_n + h k_1)
$$

$$
y_{n+1} = y_n + \frac{h}{2}(k_1 + k_2)
$$

Both conventions give character-identical results. The increment convention (with $h$ inside) is the one used in Jain and in the RUET exam solutions.

### 2. How the Parameters are Derived

To see why RK2 works, assume a general two-stage form:

$$
y_{n+1} = y_n + W_1 k_1 + W_2 k_2
$$

where:

$$
k_1 = h f(x_n, y_n)
$$

$$
k_2 = h f(x_n + \alpha_0 h, \; y_n + \beta_0 k_1)
$$

Expand $y(x_n + h)$ in a Taylor series about $x_n$:

$$
y(x_n + h) = y_n + h f + \frac{h^2}{2}\left( \frac{\partial f}{\partial x} + f \frac{\partial f}{\partial y} \right) + O(h^3)
$$

Now expand $k_2$ using two-variable Taylor series about $(x_n, y_n)$:

$$
k_2 = h\left[ f + \alpha_0 h \frac{\partial f}{\partial x} + \beta_0 k_1 \frac{\partial f}{\partial y} + O(h^2) \right] = h f + h^2\left(\alpha_0 \frac{\partial f}{\partial x} + \beta_0 f \frac{\partial f}{\partial y}\right) + O(h^3)
$$

Substitute $k_1$ and $k_2$ into $y_{n+1}$:

$$
y_{n+1} = y_n + (W_1 + W_2) h f + h^2\left( W_2 \alpha_0 \frac{\partial f}{\partial x} + W_2 \beta_0 f \frac{\partial f}{\partial y} \right) + O(h^3)
$$

Matching coefficients with the true Taylor series yields three equations with four unknowns:

$$
W_1 + W_2 = 1, \qquad W_2 \alpha_0 = \frac{1}{2}, \qquad W_2 \beta_0 = \frac{1}{2}
$$

Because there are 3 equations and 4 parameters, one parameter is arbitrary:

| Choice of Parameters | Resulting Method Name | Formulas |
|:---|:---|:---|
| $\alpha_0 = 1, \beta_0 = 1 \implies W_1 = \frac{1}{2}, W_2 = \frac{1}{2}$ | **Heun's Method (Standard RK2)** | $y_{n+1} = y_n + \frac{1}{2}(k_1 + k_2)$ |
| $\alpha_0 = \frac{1}{2}, \beta_0 = \frac{1}{2} \implies W_1 = 0, W_2 = 1$ | **Midpoint Method** | $y_{n+1} = y_n + k_2$ |
| $\alpha_0 = \frac{3}{4}, \beta_0 = \frac{3}{4} \implies W_1 = \frac{1}{4}, W_2 = \frac{3}{4}$ | **Ralston's Method** | $y_{n+1} = y_n + \frac{1}{4}k_1 + \frac{3}{4}k_2$ |

In RUET exams, **Heun's form ($\alpha_0 = \beta_0 = 1$)** is the standard convention.

> [!WARNING] Three Common Traps
> 1. **Evaluating $k_2$ at $y_n$ instead of $y_n + k_1$:**
>    If you forget $k_1$ inside the second argument, $k_2$ reduces to plain Euler, destroying second-order accuracy.
> 2. **Function argument order:**
>    In 2020 Q.7(c), the differential equation is $\frac{dy}{dx} = y - x$, not $x - y$. Subtracting in the wrong order inverts all slope signs.
> 3. **Unstated step size:**
>    If a question asks for $y(0.1)$ and $y(0.2)$ starting from $x = 0$ without specifying $h$, taking $h = 0.1$ gives two clean steps. Explicitly state: "Choosing step size $h = 0.1$".

---

## 🔧 Worked Example

> **From:** 2020 Q.7(c) -- [Marks: 05]

**The question:** Given, $\frac{dy}{dx} = y - x$, where $y(0) = 2$, find $y(0.1)$ and $y(0.2)$ by using Runge-Kutta second order formula.

**Let's solve this step by step.**

Here $f(x, y) = y - x$, with initial conditions $x_0 = 0, y_0 = 2$.
To reach $0.2$ in two equal steps, we choose $h = 0.1$.

### Step 1: March from $x_0 = 0.0$ to $x_1 = 0.1$

Starting with $x_0 = 0, y_0 = 2$:

$$
k_1 = h f(x_0, y_0) = 0.1 \cdot (2 - 0) = 0.2
$$

Now compute $k_2$ at $(x_0 + h, y_0 + k_1) = (0 + 0.1, 2 + 0.2) = (0.1, 2.2)$:

$$
k_2 = h f(0.1, 2.2) = 0.1 \cdot (2.2 - 0.1) = 0.1 \cdot (2.1) = 0.21
$$

Advance $y$:

$$
y_1 = y_0 + \frac{1}{2}(k_1 + k_2) = 2 + \frac{0.2 + 0.21}{2} = 2 + 0.205 = 2.205000
$$

So at $x_1 = 0.1$, we have $y(0.1) = 2.2050$.

### Step 2: March from $x_1 = 0.1$ to $x_2 = 0.2$

Starting with $x_1 = 0.1, y_1 = 2.205$:

$$
k_1 = h f(x_1, y_1) = 0.1 \cdot (2.205 - 0.1) = 0.1 \cdot (2.105) = 0.2105
$$

Now compute $k_2$ at $(x_1 + h, y_1 + k_1) = (0.1 + 0.1, 2.205 + 0.2105) = (0.2, 2.4155)$:

$$
k_2 = h f(0.2, 2.4155) = 0.1 \cdot (2.4155 - 0.2) = 0.1 \cdot (2.2155) = 0.22155
$$

Advance $y$:

$$
y_2 = y_1 + \frac{1}{2}(k_1 + k_2) = 2.205 + \frac{0.2105 + 0.22155}{2} = 2.205 + 0.216025 = 2.421025
$$

So at $x_2 = 0.2$, we have $y(0.2) = 2.4210$.

### Tabulated Calculation

| Step | $x_n$ | $y_n$ | $k_1$ | $k_2$ | $y_{n+1} = y_n + \frac{k_1 + k_2}{2}$ |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | 0.0 | 2.000000 | 0.200000 | 0.210000 | 2.205000 |
| 2 | 0.1 | 2.205000 | 0.210500 | 0.221550 | 2.421025 |

$$
\boxed{y(0.1) = 2.2050, \qquad y(0.2) = 2.4210 \quad (h = 0.1)}
$$

**Quick sanity check:**
The exact analytical solution of $y' - y = -x$ with $y(0) = 2$ is:

$$
y(x) = e^x + x + 1
$$

- Exact at $x = 0.1$: $e^{0.1} + 0.1 + 1 \approx 1.105171 + 1.1 = 2.205171$. (RK2 error: $-0.000171$).
- Exact at $x = 0.2$: $e^{0.2} + 0.2 + 1 \approx 1.221403 + 1.2 = 2.421403$. (RK2 error: $-0.000378$).
The error is tiny, roughly $0.0002$, which fits the expected $O(h^2)$ second-order accuracy.

---

## 🏆 Past Exam Questions

### CT-02B Q.2(a): RK2 with Predictor & Corrector Shown -- [Class Test]

**The question:** Using RK2 method with step size $h = 0.2$, calculate $y(0.2)$ and $y(0.4)$ for $\frac{dy}{dx} = x^2 - y$, $y(0) = 1$. Show both the predictor and corrector calculations at each step.

**Let's solve this step by step:**

Here $f(x, y) = x^2 - y$, initial values $x_0 = 0, y_0 = 1$, and step size $h = 0.2$.

### Step 1: March from $x_0 = 0$ to $x_1 = 0.2$
- Slope at start:

$$
k_1 = f(x_0, y_0) = 0^2 - 1 = -1
$$

- Predictor calculation:

$$
y_1^* = y_0 + h k_1 = 1 + 0.2(-1) = 0.8
$$

- Slope at predicted point $(x_0 + h, y_1^*)$:

$$
k_2 = f(0.2, 0.8) = (0.2)^2 - 0.8 = 0.04 - 0.8 = -0.76
$$

- Corrector calculation:

$$
y_1 = y_0 + \frac{h}{2}(k_1 + k_2) = 1 + \frac{0.2}{2}[-1 + (-0.76)] = 1 + 0.1(-1.76) = 1 - 0.176 = 0.8240
$$

$$
\boxed{y(0.2) \approx 0.8240}
$$

### Step 2: March from $x_1 = 0.2$ to $x_2 = 0.4$
- Current point: $x_1 = 0.2, y_1 = 0.8240$
- Slope at start:

$$
k_1 = f(0.2, 0.824) = (0.2)^2 - 0.824 = 0.04 - 0.824 = -0.784
$$

- Predictor calculation:

$$
y_2^* = y_1 + h k_1 = 0.824 + 0.2(-0.784) = 0.824 - 0.1568 = 0.6672
$$

- Slope at predicted point $(x_1 + h, y_2^*)$:

$$
k_2 = f(0.4, 0.6672) = (0.4)^2 - 0.6672 = 0.16 - 0.6672 = -0.5072
$$

- Corrector calculation:

$$
y_2 = 0.824 + \frac{0.2}{2}[-0.784 + (-0.5072)] = 0.824 + 0.1(-1.2912) = 0.824 - 0.12912 = 0.69488 \approx 0.6949
$$

$$
\boxed{y(0.4) \approx 0.6949}
$$

### Summary Table

| $x$ | $y$ (RK2) | Exact $y = x^2 - 2x + 2 - e^{-x}$ | Error |
|:---:|:---:|:---:|:---:|
| 0.0 | 1.0000 | 1.000000 | 0.0000 |
| 0.2 | 0.8240 | 0.821269 | $+0.0027$ |
| 0.4 | 0.6949 | 0.689680 | $+0.0052$ |

---

### Exam Variants at a Glance

| Year | What They Asked | ODE & Conditions | Key Answer |
|:---|:---|:---|:---|
| **2020 Q.7(c)** | Find $y(0.1)$ and $y(0.2)$ by RK2 | $y' = y - x, y(0) = 2, h = 0.1$ | $\boxed{y(0.1) = 2.2050, \qquad y(0.2) = 2.4210 \quad (h = 0.1)}$ |
| **CT-02B Q.2(a)** | Calculate $y(0.2)$ and $y(0.4)$ showing predictor/corrector | $y' = x^2 - y, y(0) = 1, h = 0.2$ | $\boxed{y(0.2) \approx 0.8240}$ and $\boxed{y(0.4) \approx 0.6949}$ |

---

## ⚡ Quick Review

**The method in one sentence:** Evaluate the initial slope $k_1$, evaluate the slope at the predicted end point $k_2$, and take the step using their arithmetic mean.

**The formulas you must memorize:**

$$
k_1 = h f(x_n, y_n)
$$

$$
k_2 = h f(x_n + h, \; y_n + k_1)
$$

$$
y_{n+1} = y_n + \frac{1}{2}(k_1 + k_2)
$$

**The most common exam mistake:** Forgetting to multiply $k_1$ by $h$ when using the slope convention, or multiplying by $h$ twice. Pick either the increment convention or the slope convention and stick to it.

**Time estimate in exam:** 6–8 minutes for a two-step RK2 problem.

---

## 🔗 Connected Topics

- [← NM-8.3: Heun's Method](NM-8.3_Heuns_Method.md) -- the predictor-corrector perspective of the exact same algorithm.
- [→ NM-8.5: Runge-Kutta 4th Order](NM-8.5_RK4.md) -- the four-stage generalization that achieves fourth-order accuracy.
- [NM-8.2: Euler's Method](NM-8.2_Eulers_Method.md) -- RK1 is simply Euler's method.

---

[← Previous: NM-8.3 Heun's Method](NM-8.3_Heuns_Method.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: NM-8.5 RK4 →](NM-8.5_RK4.md)
