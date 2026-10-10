[← Previous: NM-8.1 IVP vs BVP](NM-8.1_IVP_vs_BVP.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: NM-8.3 Heun's Method →](NM-8.3_Heuns_Method.md)

---

# NM-8.2: Euler's Method

> 🔴 **Priority:** Critical | **Tested:** 5/8 years (2018, 2019, 2020, 2021, 2023) | **Typical marks:** 4–6

## What This Is (and Why It Matters)

Euler's method is where all numerical ODE solving begins. It is the oldest, simplest, and most intuitive numerical stepping method in existence.

Imagine walking along a curved hiking trail in dense fog. You can only see the trail right at your feet, and you know the exact direction (the tangent slope) it is heading at this moment. Euler's method says: *take a step of length $h$ straight along that tangent direction, look down at your new position, calculate the new direction, and repeat.*

The exam loves Euler's method for two reasons:
1. It is frequently tested as a theoretical essay question (asking you to derive the formula from Taylor series, discuss its local and global error, and state its practical limitations).
2. It appears as direct numerical stepping problems where you march across two to four intervals using a given step size $h$.

Euler's method also acts as the **predictor engine** inside higher-order methods like Heun's method and Runge-Kutta. Understanding exactly how Euler steps forward and where it loses accuracy explains why all the higher-order methods were invented.

---

## 📝 Key Definitions

> **Euler's Formula:** "Assuming that $f(x, y) = f(x_0, y_0)$ in $x_0 \le x \le x_1$, this gives Euler's formula $y_1 \approx y_0 + h f(x_0, y_0)$." -- Jain, §8.4 (p. 307), Eq. (8.7a)
>
> **In simple words:** To find the next $y$ value, take your current $y$ value and add the step size $h$ multiplied by the slope at your current point.

> **Local Truncation Error for Euler:** "$L_{n+1} = -\frac{1}{2} h^2 y''(\tau_n)$, where $x_n \le \tau_n \le x_{n+1}$." -- Jain, §8.4.1 (p. 308), Eq. (8.10)
>
> **In simple words:** In any single step, the error you create by following a straight tangent line instead of the true curved solution is proportional to $h^2$ and depends directly on the curvature $y''$.

> **Why Higher Methods Exist (Euler's Limitation):** "The process is very slow and to obtain reasonable accuracy with Euler's method, we need to take a smaller value for $h$. Because of this restriction on $h$, the method is unsuitable for practical use and a modification of it, known as the modified Euler method, which gives more accurate results, will be described..." -- Jain, §8.4 (p. 307)
>
> **In simple words:** Because Euler is only first-order accurate globally, getting one extra decimal place of accuracy requires taking 10 times as many steps. It requires too much work for practical precision, which is why second-order and fourth-order methods were developed.

---

## The Core Idea

### 1. Derivation from Taylor Series

Suppose we want to solve the initial value problem:

$$
\frac{dy}{dx} = f(x, y), \qquad y(x_0) = y_0
$$

Expand $y(x_{n+1}) = y(x_n + h)$ in a Taylor series about the current point $x_n$:

$$
y(x_{n+1}) = y(x_n) + h y'(x_n) + \frac{h^2}{2} y''(x_n) + \frac{h^3}{6} y'''(x_n) + \cdots
$$

Since $y'(x_n) = f(x_n, y_n)$, we substitute:

$$
y(x_{n+1}) = y_n + h f(x_n, y_n) + \frac{h^2}{2} y''(\tau_n)
$$

Euler's method keeps the first two terms and discards all higher-order terms:

$$
y_{n+1} = y_n + h f(x_n, y_n)
$$

### 2. Geometric Interpretation

Geometrically, the true solution curve $y(x)$ bends and curves. At the point $(x_n, y_n)$, Euler's method draws the straight tangent line with slope $m = f(x_n, y_n)$ and marches along that line for a horizontal distance $h$.

If the true solution is convex ($y'' > 0$, curving upwards like a bowl), the tangent line sits strictly **below** the curve. This means Euler will systematically **under-estimate** the true values. If the curve is concave ($y'' < 0$), Euler will systematically **over-estimate**.

### 3. Step-by-Step Algorithm

1. **Initialize:** Start at $(x_0, y_0)$ with chosen step size $h$.
2. **Compute current slope:** Calculate $m_n = f(x_n, y_n)$.
3. **Advance dependent variable:** Compute $y_{n+1} = y_n + h \cdot m_n$.
4. **Advance independent variable:** Compute $x_{n+1} = x_n + h$.
5. **Repeat:** Repeat steps 2 through 4 until you reach the target point.

### 4. Local Error vs. Global Error

This is one of the most tested concepts in oral exams and finals:
- **Local Truncation Error ($O(h^2)$):** The error made in a *single step*, assuming the starting value of that step was 100% exact. This comes from the first discarded Taylor term, $\frac{h^2}{2} y''$, so it is of order $O(h^2)$.
- **Global Truncation Error ($O(h)$):** The accumulated error at the end of the entire interval $[x_0, x_n]$. To cover an interval of length $L$, you must take $N = L/h$ steps. Multiplying the number of steps by the error per step gives:

$$
\text{Total Error} \approx N \times O(h^2) = \frac{L}{h} \times O(h^2) = O(h)
$$

Because the global error scales as $h^1$, Euler's method is classified as a **first-order method**.

> [!NOTE] What First-Order Means in Practice
> Halving the step size ($h \to h/2$) only cuts the error in half. If you want 6 decimal places of precision, Euler might require 1,000,000 steps. In contrast, RK4 cuts the error by $2^4 = 16$ every time you halve $h$.

### 5. When Does Euler's Method Fail?

1. **Large step sizes:** If $h$ is too large, the straight tangent lines shoot completely away from the true curve.
2. **Stiff differential equations:** For the test equation $y' = \lambda y$ where $\lambda < 0$ is a large negative number, the Euler update is $y_{n+1} = (1 + h\lambda) y_n$. The method only remains stable if $|1 + h\lambda| < 1$, which requires:

$$
h < \frac{2}{|\lambda|}
$$

If $h$ exceeds this critical limit, successive values oscillate wildly and explode to infinity, even when the true physical solution decays smoothly to zero.

> [!WARNING] Common Traps in Euler Problems
> 1. **Zero slope at the start:** In equations like $y' = x + y$ with $y(0) = 0$, or $y' = \frac{3}{5}x^3 y$ with $x_0 = 0$, the slope at the first step is exactly zero! That means $y_1 = y_0$. Do not panic and assume you made an error; a zero slope simply means the curve leaves the origin horizontally.
> 2. **Mixing old and new values:** In the update $y_{n+1} = y_n + h f(x_n, y_n)$, both inputs to $f$ must come from step $n$. Never accidentally plug $x_{n+1}$ into $f$.

---

## 🔧 Worked Example

> **From:** 2020 Q.7(b) -- [Marks: 04]

**The question:** Solve, by Euler's method, the equation $\frac{dy}{dx} = x + y, \; y(0) = 0$. Choose $h = 0.2$ and compute $y(0.4)$ and $y(0.6)$.

**Let's solve this step by step.**

Here our function is $f(x, y) = x + y$, our step size is $h = 0.2$, and we start at $x_0 = 0, y_0 = 0$.

The Euler update formula is:

$$
y_{n+1} = y_n + 0.2 \cdot (x_n + y_n), \qquad x_{n+1} = x_n + 0.2
$$

### Step 1: Advance from $x_0 = 0.0$ to $x_1 = 0.2$

Current point: $x_0 = 0.0, y_0 = 0.0$.
Current slope:

$$
f(x_0, y_0) = 0.0 + 0.0 = 0.0
$$

Next value:

$$
y_1 = 0.0 + 0.2(0.0) = 0.000000
$$

So at $x_1 = 0.2$, we have $y_1 = 0.0$.

### Step 2: Advance from $x_1 = 0.2$ to $x_2 = 0.4$

Current point: $x_1 = 0.2, y_1 = 0.0$.
Current slope:

$$
f(x_1, y_1) = 0.2 + 0.0 = 0.2
$$

Next value:

$$
y_2 = 0.0 + 0.2(0.2) = 0.040000
$$

So at $x_2 = 0.4$, our computed value is $y(0.4) = 0.0400$.

### Step 3: Advance from $x_2 = 0.4$ to $x_3 = 0.6$

Current point: $x_2 = 0.4, y_2 = 0.04$.
Current slope:

$$
f(x_2, y_2) = 0.4 + 0.04 = 0.44
$$

Next value:

$$
y_3 = 0.04 + 0.2(0.44) = 0.04 + 0.088 = 0.128000
$$

So at $x_3 = 0.6$, our computed value is $y(0.6) = 0.1280$.

### Summary Table

| Step $n$ | $x_n$ | $y_n$ | Slope $f(x_n, y_n) = x_n + y_n$ | $y_{n+1} = y_n + 0.2 \cdot f$ |
|:---:|:---:|:---:|:---:|:---:|
| 0 | 0.0 | 0.000000 | $0.0 + 0.0 = 0.0$ | $0.0 + 0.2(0.0) = 0.000000$ |
| 1 | 0.2 | 0.000000 | $0.2 + 0.0 = 0.2$ | $0.0 + 0.2(0.2) = 0.040000$ |
| 2 | 0.4 | 0.040000 | $0.4 + 0.04 = 0.44$ | $0.04 + 0.2(0.44) = 0.128000$ |

$$
\boxed{y(0.4) = 0.0400, \qquad y(0.6) = 0.1280 \quad (h = 0.2)}
$$

**Quick sanity check:**
The exact analytical solution of $y' - y = x$ with $y(0) = 0$ is:

$$
y(x) = e^x - x - 1
$$

At $x = 0.4$: $e^{0.4} - 0.4 - 1 \approx 1.491825 - 1.4 = 0.091825$. Euler gives $0.040000$.
At $x = 0.6$: $e^{0.6} - 0.6 - 1 \approx 1.822119 - 1.6 = 0.222119$. Euler gives $0.128000$.
Because the exact solution is convex ($y'' = e^x > 0$), Euler's tangent line sits below the curve and under-reads the solution, exactly as theory predicts.

---

## 🏆 Past Exam Questions

### 2019 Q.7(c): Discuss Euler's Method -- [04 Marks]

**The question:** Discuss Euler's method to solve ordinary differential equations.

**Full Answer:**

**1. Purpose and Setup:**
Given a first-order initial value problem:

$$
\frac{dy}{dx} = f(x, y), \qquad y(x_0) = y_0
$$

we want to estimate the values of $y$ at discrete points $x_n = x_0 + nh$ for a small step size $h$.

**2. Derivation:**
Expanding $y(x_{n+1})$ in a Taylor series about $x_n$:

$$
y(x_{n+1}) = y(x_n) + h y'(x_n) + \frac{h^2}{2} y''(x_n) + \cdots
$$

Since $y'(x_n) = f(x_n, y_n)$, retaining only the first two terms gives Euler's formula:

$$
y_{n+1} = y_n + h f(x_n, y_n)
$$

**3. Geometrical Interpretation:**
The method approximates the solution curve by a sequence of short straight line segments, each tangent to the integral curve at $(x_n, y_n)$.

**4. Error Characteristics:**
- **Local truncation error:** $O(h^2)$ per step, resulting from discarding the $\frac{1}{2}h^2 y''(\tau_n)$ term.
- **Global truncation error:** $O(h)$ over the full interval, since the error accumulates over $N = (b-a)/h$ steps.
Therefore, Euler's method is a **first-order method**.

**5. Advantages and Disadvantages:**
- *Advantages:* Conceptually simple, requires only one function evaluation of $f$ per step, and requires no higher-order analytical derivatives.
- *Disadvantages:* Poor accuracy requiring very small $h$; slow convergence; and conditional stability on stiff equations where $h$ must satisfy $h < 2/|\lambda|$.

$$
\boxed{y_{n+1} = y_n + h\,f(x_n, y_n), \qquad \text{global error } O(h)}
$$

---

### 2021 Q.8(c) & 2023 Q.3(b): Step March on $y' = \frac{3}{5}x^3 y$ -- [04 Marks]

**The question:** Using Euler's method, determine $\frac{dy}{dx} = \frac{3}{5}x^3 y$; Consider $y(0) = 1$.

**Let's solve this step by step:**

> [!NOTE] Handling Missing Parameters
> The exam paper specified no interval and no step size $h$. In such cases, standard examination convention is to choose a convenient step size such as $h = 0.25$ over the unit interval $[0, 1]$ (giving 4 steps), state the choice explicitly, and perform the march.

Here $f(x, y) = \frac{3}{5}x^3 y$, $x_0 = 0, y_0 = 1$, and $h = 0.25$.
The recursion formula is:

$$
y_{n+1} = y_n + 0.25 \cdot \left(\frac{3}{5} x_n^3 y_n\right) = y_n + 0.15 \, x_n^3 y_n
$$

**Step 1 ($x_0 = 0.0 \to x_1 = 0.25$):**
Slope: $f(0, 1) = \frac{3}{5}(0)^3(1) = 0$.

$$
y_1 = 1 + 0.25(0) = 1.0000000
$$

**Step 2 ($x_1 = 0.25 \to x_2 = 0.50$):**
Slope: $f(0.25, 1) = \frac{3}{5}(0.25)^3(1) = 0.6 \times 0.015625 = 0.0093750$.

$$
y_2 = 1.0000000 + 0.25(0.0093750) = 1.0023438
$$

**Step 3 ($x_2 = 0.50 \to x_3 = 0.75$):**
Slope: $f(0.5, 1.0023438) = 0.6(0.125)(1.0023438) = 0.0751758$.

$$
y_3 = 1.0023438 + 0.25(0.0751758) = 1.0211377
$$

**Step 4 ($x_3 = 0.75 \to x_4 = 1.00$):**
Slope: $f(0.75, 1.0211377) = 0.6(0.421875)(1.0211377) = 0.2584755$.

$$
y_4 = 1.0211377 + 0.25(0.2584755) = 1.0857566
$$

| Step $n$ | $x_n$ | $y_n$ | Slope $\frac{3}{5}x_n^3y_n$ | $y_{n+1} = y_n + 0.25 \cdot \text{slope}$ |
|:---:|:---:|:---:|:---:|:---:|
| 1 | 0.00 | 1.0000000 | 0.0000000 | 1.0000000 |
| 2 | 0.25 | 1.0000000 | 0.0093750 | 1.0023438 |
| 3 | 0.50 | 1.0023438 | 0.0751758 | 1.0211377 |
| 4 | 0.75 | 1.0211377 | 0.2584755 | 1.0857566 |

$$
\boxed{y(1) \approx 1.08576 \quad (h = 0.25)}
$$

**Exact solution comparison:**
Separating variables: $\frac{dy}{y} = \frac{3}{5}x^3 dx \implies \ln y = \frac{3}{20}x^4 = 0.15 x^4$.
With $y(0) = 1$, the exact solution is $y(x) = e^{0.15 x^4}$.
At $x = 1$, exact $y(1) = e^{0.15} \approx 1.161834$.
Euler's result $1.08576$ is low by about $0.076$, again agreeing with the expected convex under-reading.

---

### Exam Variants at a Glance

| Year | What They Asked | Step & Interval | Key Answer |
|:---|:---|:---|:---|
| **2019 Q.7(c)** | Discuss Euler's method, derivation, error, merits | Theory | $\boxed{y_{n+1} = y_n + h\,f(x_n, y_n), \qquad \text{global error } O(h)}$ |
| **2020 Q.7(b)** | Compute $y(0.4)$ and $y(0.6)$ for $y' = x + y, y(0) = 0$ | $h = 0.2$ | $\boxed{y(0.4) = 0.0400, \qquad y(0.6) = 0.1280 \quad (h = 0.2)}$ |
| **2021 Q.8(c)** | Solve $y' = \frac{3}{5}x^3 y, y(0) = 1$ | $h = 0.25, x \in [0, 1]$ | $\boxed{y(1) \approx 1.08576 \quad (h = 0.25)}$ |
| **2023 Q.3(b)** | Exact repeat of 2021 Q.8(c) | $h = 0.25, x \in [0, 1]$ | $\boxed{y(1) \approx 1.08576 \quad (h = 0.25)}$ |

---

## ⚡ Quick Review

**The method in one sentence:** Take a step of size $h$ along the tangent line calculated at your current point.

**The formula you must memorize:**

$$
y_{n+1} = y_n + h f(x_n, y_n)
$$

**The most common exam mistake:** Forgetting that the local error is $O(h^2)$ while the global error is $O(h)$.

**Time estimate in exam:** 6–8 minutes for a three-step numerical march with full tabulation.

---

## 🔗 Connected Topics

- [← NM-8.1: IVP vs BVP](NM-8.1_IVP_vs_BVP.md) -- why initial value problems allow step-by-step marching.
- [→ NM-8.3: Heun's Method](NM-8.3_Heuns_Method.md) -- how Heun uses Euler as a predictor, then averages slopes to achieve $O(h^2)$ accuracy.
- [NM-8.5: Runge-Kutta 4th Order](NM-8.5_RK4.md) -- fourth-order stepping that evaluates four probe slopes.
- [NM-8.6: Higher-Order Systems](NM-8.6_Higher_Order_Systems.md) -- using Euler to march systems of coupled first-order ODEs.

---

[← Previous: NM-8.1 IVP vs BVP](NM-8.1_IVP_vs_BVP.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: NM-8.3 Heun's Method →](NM-8.3_Heuns_Method.md)
