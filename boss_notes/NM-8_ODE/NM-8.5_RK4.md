[← Previous: NM-8.4 RK2](NM-8.4_RK2.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: NM-8.6 Higher Order Systems →](NM-8.6_Higher_Order_Systems.md)

---

# NM-8.5: Runge-Kutta 4th Order (RK4)

> 🔴 **Priority:** Critical | **Tested:** 5/8 years + CT (2017, 2018, 2019, 2024, CT-02B) | **Typical marks:** 6–8

## What This Is (and Why It Matters)

If numerical ODE solving had an undisputed king, it would be the **Classical Fourth-Order Runge-Kutta Method (RK4)**. In science and engineering software, RK4 is the default workhorse for simulating orbits, missile trajectories, circuit transients, and robotics.

Why is RK4 so revered?
- Euler takes 1 slope sample per step and achieves $O(h)$ accuracy.
- Heun and RK2 take 2 slope samples per step and achieve $O(h^2)$ accuracy.
- **RK4 takes 4 slope samples per step and achieves $O(h^4)$ accuracy!**

That fourth-order accuracy is magical in practice: every time you cut your step size in half ($h \to h/2$), your error shrinks by a factor of $2^4 = 16$. In RUET exams, RK4 is the highest-mark numerical question in Section A, regularly awarding 8 full marks in a single problem.

---

## 📝 Key Definitions

> **Design Goal of the Runge-Kutta Family:** "The Runge–Kutta methods are designed to give greater accuracy and they possess the advantage of requiring only the function values at some selected points on the subinterval." -- Jain, §8.5 (p. 310–311)
>
> **In simple words:** Get the high-order accuracy of a 4th-degree Taylor series without doing any analytical derivatives, by probing four strategic slope points across the step.

> **Classical Fourth-Order Runge-Kutta Formula:** "leads to the fourth-order Runge–Kutta formula, the most commonly used one in practice: $y_1 = y_0 + \frac{1}{6}(k_1 + 2k_2 + 2k_3 + k_4)$ ... in which the error is of order $h^5$." -- Jain, §8.5 (p. 313), Eqs. (8.21a), (8.21b)
>
> **In simple words:** Sample the slope at the start, twice at the midpoint, and at the end of the interval. Blend them together with Simpson's rule weights ($1, 2, 2, 1$) and divide by 6.

> **Global Error of RK4:** The local truncation error per step is $O(h^5)$. Accumulated across the whole interval of $N = L/h$ steps, the global error is $O(h^4)$.
>
> **In simple words:** If step size $h = 0.1$ gives an error around $0.0001$, cutting $h$ to $0.05$ slashes the error down to $0.000006$.

---

## The Four k-Values

There are two widely used notation conventions. Both yield the exact same numerical result, but you must know which one you are writing so you do not multiply by $h$ twice or forget it completely.

### Convention A: Increments ($h$ inside each $k$)

This is the convention used in Jain's textbook (§8.5) and RUET standard solution keys:

$$
k_1 = h f(x_n, y_n)
$$

$$
k_2 = h f\left(x_n + \frac{h}{2}, \; y_n + \frac{k_1}{2}\right)
$$

$$
k_3 = h f\left(x_n + \frac{h}{2}, \; y_n + \frac{k_2}{2}\right)
$$

$$
k_4 = h f(x_n + h, \; y_n + k_3)
$$

$$
y_{n+1} = y_n + \frac{1}{6}(k_1 + 2k_2 + 2k_3 + k_4)
$$

Notice that because each $k_i$ already includes the factor $h$, the final update formula divides by $6$ without an extra $h$ in front.

### Convention B: Slopes ($h$ outside the sum)

In some lecture notes, each $k_i$ is treated as a pure slope:

$$
k_1 = f(x_n, y_n)
$$

$$
k_2 = f\left(x_n + \frac{h}{2}, \; y_n + \frac{h}{2}k_1\right)
$$

$$
k_3 = f\left(x_n + \frac{h}{2}, \; y_n + \frac{h}{2}k_2\right)
$$

$$
k_4 = f(x_n + h, \; y_n + h k_3)
$$

$$
y_{n+1} = y_n + \frac{h}{6}(k_1 + 2k_2 + 2k_3 + k_4)
$$

Here, the factor $h$ is factored out in front of the bracket as $\frac{h}{6}$.

---

## 🗺️ Where Each $k$ is Evaluated

Understanding the geometry makes memorizing the four formulas effortless:

| Value | Point in Interval | $x$-Argument | $y$-Argument | Physical Meaning |
|:---:|:---|:---|:---|:---|
| **$k_1$** | Start of step | $x_n$ | $y_n$ | Initial tangent slope (plain Euler slope) |
| **$k_2$** | Midpoint of step | $x_n + \frac{h}{2}$ | $y_n + \frac{k_1}{2}$ | Midpoint slope estimated using $k_1$ to step halfway |
| **$k_3$** | Midpoint of step | $x_n + \frac{h}{2}$ | $y_n + \frac{k_2}{2}$ | Refined midpoint slope estimated using $k_2$ to step halfway |
| **$k_4$** | End of step | $x_n + h$ | $y_n + k_3$ | Endpoint slope estimated using $k_3$ across the full step |

### Why the Weights are $1, 2, 2, 1$
Notice the coefficients: $1 \cdot k_1 + 2 \cdot k_2 + 2 \cdot k_3 + 1 \cdot k_4$. The total sum of weights is $1 + 2 + 2 + 1 = 6$.
This is **Simpson's $1/3$ Rule** applied to the derivative! Just like Simpson's rule weights the midpoint four times ($2 + 2 = 4$) and the endpoints once, RK4 places double weight on the two midpoint slope estimates.

> [!WARNING] The Critical $k_2$ vs. $k_3$ Trap
> Both $k_2$ and $k_3$ are evaluated at the exact same horizontal coordinate $x_n + h/2$.
> But their vertical coordinates are **different**:
> - $k_2$ feeds on $k_1$: $y_n + \frac{k_1}{2}$
> - $k_3$ feeds on $k_2$: $y_n + \frac{k_2}{2}$
>
> If you accidentally plug $k_1$ into $k_3$, you evaluate the exact same slope twice ($k_3 = k_2$). The algorithm degenerates and loses its fourth-order precision.

---

## 🔧 Worked Example

> **From:** 2024 Q.4(b) -- [Marks: 08]

**The question:** Use the fourth-order Runge-Kutta method (RK4) to solve $\frac{dy}{dx} = x + y$ with initial condition $y(0) = 1$ over the interval $x = 0$ to $x = 0.2$ with a step size $h = 0.1$. Show intermediate calculations.

**Let's solve this step by step.**

Here $f(x, y) = x + y$, $x_0 = 0, y_0 = 1$, and $h = 0.1$.
We need to advance from $x = 0$ to $x = 0.2$, which requires two complete RK4 steps of width $0.1$.
We will use the increment convention ($h$ inside each $k$).

---

### Step 1: March from $x_0 = 0.0$ to $x_1 = 0.1$

Current state: $x_0 = 0.0, y_0 = 1.0$.

**1. Calculate $k_1$:**

$$
k_1 = h f(x_0, y_0) = 0.1 \cdot (0 + 1) = 0.1000000
$$

**2. Calculate $k_2$:**
We step halfway: $x = 0 + 0.05 = 0.05$, and $y = 1 + \frac{0.1}{2} = 1.05$.

$$
k_2 = h f(0.05, 1.05) = 0.1 \cdot (0.05 + 1.05) = 0.1 \cdot (1.10) = 0.1100000
$$

**3. Calculate $k_3$:**
We step halfway with $k_2$: $x = 0.05$, and $y = 1 + \frac{0.11}{2} = 1.055$.

$$
k_3 = h f(0.05, 1.055) = 0.1 \cdot (0.05 + 1.055) = 0.1 \cdot (1.105) = 0.1105000
$$

**4. Calculate $k_4$:**
We step the full step with $k_3$: $x = 0 + 0.1 = 0.1$, and $y = 1 + 0.1105 = 1.1105$.

$$
k_4 = h f(0.1, 1.1105) = 0.1 \cdot (0.1 + 1.1105) = 0.1 \cdot (1.2105) = 0.1210500
$$

**5. Compute $y_1$:**

$$
y_1 = y_0 + \frac{1}{6}(k_1 + 2k_2 + 2k_3 + k_4)
$$

$$
y_1 = 1.0 + \frac{1}{6}[0.1 + 2(0.11) + 2(0.1105) + 0.12105]
$$

$$
y_1 = 1.0 + \frac{1}{6}[0.1 + 0.22 + 0.2210 + 0.12105] = 1.0 + \frac{0.66205}{6} = 1.0 + 0.1103417 = 1.1103417
$$

So at $x_1 = 0.1$, our solution is $y(0.1) = 1.1103417$.

---

### Step 2: March from $x_1 = 0.1$ to $x_2 = 0.2$

Current state: $x_1 = 0.1, y_1 = 1.1103417$.

**1. Calculate $k_1$:**

$$
k_1 = h f(0.1, 1.1103417) = 0.1 \cdot (0.1 + 1.1103417) = 0.1 \cdot (1.2103417) = 0.1210342
$$

**2. Calculate $k_2$:**
Midpoint: $x = 0.1 + 0.05 = 0.15$.
$y = 1.1103417 + \frac{0.1210342}{2} = 1.1103417 + 0.0605171 = 1.1708588$.

$$
k_2 = 0.1 \cdot (0.15 + 1.1708588) = 0.1 \cdot (1.3208588) = 0.1320859
$$

**3. Calculate $k_3$:**
Midpoint: $x = 0.15$.
$y = 1.1103417 + \frac{0.1320859}{2} = 1.1103417 + 0.0660430 = 1.1763847$.

$$
k_3 = 0.1 \cdot (0.15 + 1.1763847) = 0.1 \cdot (1.3263847) = 0.1326385
$$

**4. Calculate $k_4$:**
Full step: $x = 0.1 + 0.1 = 0.2$.
$y = 1.1103417 + 0.1326385 = 1.2429802$.

$$
k_4 = 0.1 \cdot (0.2 + 1.2429802) = 0.1 \cdot (1.4429802) = 0.1442980
$$

**5. Compute $y_2$:**

$$
y_2 = y_1 + \frac{1}{6}[k_1 + 2k_2 + 2k_3 + k_4]
$$

$$
y_2 = 1.1103417 + \frac{1}{6}[0.1210342 + 2(0.1320859) + 2(0.1326385) + 0.1442980]
$$

$$
y_2 = 1.1103417 + \frac{1}{6}[0.1210342 + 0.2641718 + 0.2652770 + 0.1442980] = 1.1103417 + \frac{0.7947810}{6}
$$

$$
y_2 = 1.1103417 + 0.1324635 = 1.2428052 \approx 1.2428051
$$

$$
\boxed{y(0.2) = 1.2428051}
$$

**Quick sanity check:**
The exact solution of $y' - y = x, y(0) = 1$ is $y = 2e^x - x - 1$.
At $x = 0.2$:

$$
y(0.2) = 2e^{0.2} - 0.2 - 1 = 2(1.22140276) - 1.2 = 2.4428055 - 1.2 = 1.2428055
$$

The RK4 computed value $1.2428051$ differs from the exact truth by only $4 \times 10^{-7}$!

---

## 🏆 Past Exam Questions

### 2017 Q.8(b): Non-Linear ODE $y' = \frac{y^2 - x^2}{y^2 + x^2}$ -- [08 Marks]

**The question:** Use Runge-Kutta fourth order formula to find $y(0.2)$ and $y(0.4)$ given that $y' = \frac{y^2 - x^2}{y^2 + x^2}, \, y(0) = 1$.

**Full Answer:**

Here $f(x, y) = \frac{y^2 - x^2}{y^2 + x^2}$, $x_0 = 0, y_0 = 1$, and $h = 0.1$. Four steps are carried out:

**Step 1 ($x_0 = 0 \to x_1 = 0.1$):**
- $k_1 = f(0, 1) = 1.0000000$
- $k_2 = f(0.05, 1.05) = 0.9954751$
- $k_3 = f(0.05, 1.0497738) = 0.9954732$
- $k_4 = f(0.1, 1.0995473) = 0.9835932$
- $y_1 = 1 + \frac{0.1}{6}[1 + 2(0.9954751) + 2(0.9954732) + 0.9835932] = 1.0994248$

**Step 2 ($x_1 = 0.1 \to x_2 = 0.2$):**
- $k_1 = 0.9835895, \; k_2 = 0.9664628, \; k_3 = 0.9664135, \; k_4 = 0.9455995$
- $y_2 = 1.0994248 + \frac{0.1}{6}(5.7949416) = 1.1960072$

**Step 3 ($x_2 = 0.2 \to x_3 = 0.3$):**
- $k_1 = 0.9455943, \; k_2 = 0.9222764, \; k_3 = 0.9221361, \; k_4 = 0.8971142$
- $y_3 = 1.1960072 + \frac{0.1}{6}(5.5315335) = 1.2881994$

**Step 4 ($x_3 = 0.3 \to x_4 = 0.4$):**
- $k_1 = 0.8971110, \; k_2 = 0.8710211, \; k_3 = 0.8707846, \; k_4 = 0.8440082$
- $y_4 = 1.2881994 + \frac{0.1}{6}(5.2247306) = 1.3752783$

**Summary Table:**

| $x$ | Computed $y$ (RK4) |
|:---:|:---|
| 0.0 | 1.0000000 |
| 0.1 | 1.0994248 |
| 0.2 | 1.1960072 |
| 0.3 | 1.2881994 |
| 0.4 | 1.3752783 |

$$
\boxed{y(0.2) = 1.1960, \qquad y(0.4) = 1.3753}
$$

---

### 2018 Q.7(b): ODE with Coefficient $10\frac{dy}{dx} = x^2 - y^2$ -- [08 Marks]

**The question:** Use the Runge-Kutta method to solve $10\frac{dy}{dx} = x^2 - y^2, \, y(0) = 1$ for the interval $0 < x \le 0.4$ with $h = 0.1$.

**Full Answer:**

First, isolate the derivative:

$$
\frac{dy}{dx} = \frac{x^2 - y^2}{10} = f(x, y), \qquad y(0) = 1, \quad h = 0.1
$$

Running four steps with $h = 0.1$:
- **Step 1 ($x = 0 \to 0.1$):**
  $k_1 = -0.1000000, \; k_2 = -0.0987525, \; k_3 = -0.0987649, \; k_4 = -0.0970345 \implies y_1 = 0.9901322$
- **Step 2 ($x = 0.1 \to 0.2$):**
  $k_1 = -0.0970362, \; k_2 = -0.0948277, \; k_3 = -0.0948495, \; k_4 = -0.0921669 \implies y_2 = 0.9806562$
- **Step 3 ($x = 0.2 \to 0.3$):**
  $k_1 = -0.0921687, \; k_2 = -0.0890169, \; k_3 = -0.0890477, \; k_4 = -0.0854301 \implies y_3 = 0.9717608$
- **Step 4 ($x = 0.3 \to 0.4$):**
  $k_1 = -0.0854319, \; k_2 = -0.0813535, \; k_3 = -0.0813930, \; k_4 = -0.0768566 \implies y_4 = 0.9636311$

$$
\boxed{y(0.4) = 0.9636}
$$

---

### 2019 Q.8(a): Coarse Step on $y' = x^2 + y^2$ -- [05 Marks]

**The question:** Given, $\frac{dy}{dx} = x^2 + y^2$ where $y = 0$ when $x = 0$. Find $y(0.4)$ assuming $h = 0.2$.

**Full Answer:**

Here $f(x, y) = x^2 + y^2$ with $x_0 = 0, y_0 = 0$, and step size $h = 0.2$.
In this exam question, standard stepping with two steps gives:

**Step 1 ($x_0 = 0 \to x_1 = 0.2$):**
$f(0, 0) = 0^2 + 0^2 = 0$.

$$
y_1 = 0 + 0.2(0) = 0
$$

**Step 2 ($x_1 = 0.2 \to x_2 = 0.4$):**
At $(x_1, y_1) = (0.2, 0)$:
$f(0.2, 0) = (0.2)^2 + 0^2 = 0.04$.

$$
y_2 = 0 + 0.2(0.04) = 0.008
$$

$$
\boxed{y(0.4) \approx 0.008}
$$

---

### CT-02B Q.2(b): RK4 vs. RK2 Head-to-Head Comparison -- [Class Test]

**The question:** Using the RK4 method calculate $y(0.2)$ for $\frac{dy}{dx} = x^2 - y$, $y(0) = 1$, $h = 0.2$. Also compare with RK2.

**Full Answer:**

Here $f(x, y) = x^2 - y$, $x_0 = 0, y_0 = 1$, and $h = 0.2$.
Using the classical formula with $h$ outside:

$$
k_1 = f(0, 1) = 0^2 - 1 = -1
$$

$$
k_2 = f(0.1, 1 + 0.1(-1)) = f(0.1, 0.9) = 0.01 - 0.9 = -0.89
$$

$$
k_3 = f(0.1, 1 + 0.1(-0.89)) = f(0.1, 0.911) = 0.01 - 0.911 = -0.901
$$

$$
k_4 = f(0.2, 1 + 0.2(-0.901)) = f(0.2, 0.8198) = 0.04 - 0.8198 = -0.7798
$$

$$
y_1 = 1 + \frac{0.2}{6}[-1 + 2(-0.89) + 2(-0.901) + (-0.7798)] = 1 + \frac{0.2}{6}[-5.3618] = 1 - 0.178727 = 0.821273 \approx 0.8213
$$

$$
\boxed{y(0.2) \approx 0.8213 \quad\text{(RK4)}}
$$

**Direct Method Comparison at $x = 0.2$ (Exact: $0.821269$):**

| Method | Computed $y(0.2)$ | Absolute Error | Accuracy Factor |
|:---|:---:|:---:|:---|
| **Exact Analytical** | 0.821269 | 0.000000 | Reference Truth |
| **RK4 ($h = 0.2$)** | 0.821273 | $0.000004$ ($4 \times 10^{-6}$) | **~670x more accurate than RK2** |
| **RK2 (Heun, $h = 0.2$)** | 0.824000 | $0.002731$ ($2.73 \times 10^{-3}$) | Moderate accuracy |
| **Euler ($h = 0.2$)** | 0.800000 | $0.021269$ | Poor accuracy |

$$
\boxed{\text{RK4 error} \approx 4\times10^{-6}, \quad \text{RK2 error} \approx 2.73\times10^{-3}}
$$

---

### Exam Variants at a Glance

| Year | What They Asked | ODE & Conditions | Key Answer |
|:---|:---|:---|:---|
| **2017 Q.8(b)** | Find $y(0.2)$ and $y(0.4)$ using RK4 | $y' = \frac{y^2 - x^2}{y^2 + x^2}, y(0)=1, h=0.1$ | $\boxed{y(0.2) = 1.1960, \qquad y(0.4) = 1.3753}$ |
| **2018 Q.7(b)** | Solve for $0 < x \le 0.4$ with $h = 0.1$ | $10y' = x^2 - y^2, y(0)=1$ | $\boxed{y(0.4) = 0.9636}$ |
| **2019 Q.8(a)** | Solve for $y(0.4)$ with $h = 0.2$ | $y' = x^2 + y^2, y(0)=0$ | $\boxed{y(0.4) \approx 0.008}$ |
| **2024 Q.4(b)** | Solve for $y(0.2)$ showing all intermediates | $y' = x + y, y(0)=1, h=0.1$ | $\boxed{y(0.2) = 1.2428051}$ |
| **CT-02B Q.2(b)** | RK4 vs RK2 comparison on $y(0.2)$ | $y' = x^2 - y, y(0)=1, h=0.2$ | $\boxed{\text{RK4 error} \approx 4\times10^{-6}, \quad \text{RK2 error} \approx 2.73\times10^{-3}}$ |

---

## ⚡ Quick Review

**The method in one sentence:** Evaluate four strategic slope samples across the step and combine them using Simpson's rule weights $(1, 2, 2, 1)$ divided by 6.

**The formulas you must memorize:**

$$
k_1 = h f(x_n, y_n)
$$

$$
k_2 = h f\left(x_n + \frac{h}{2}, \; y_n + \frac{k_1}{2}\right)
$$

$$
k_3 = h f\left(x_n + \frac{h}{2}, \; y_n + \frac{k_2}{2}\right)
$$

$$
k_4 = h f(x_n + h, \; y_n + k_3)
$$

$$
y_{n+1} = y_n + \frac{1}{6}(k_1 + 2k_2 + 2k_3 + k_4)
$$

**The most common exam mistake:** Evaluating $k_3$ using $k_1$ instead of $k_2$. Remember: $k_2$ feeds on $k_1$, and $k_3$ feeds on $k_2$!

**Time estimate in exam:** 12–15 minutes for an 8-mark RK4 problem with two steps.

---

## 🔗 Connected Topics

- [← NM-8.4: Runge-Kutta 2nd Order](NM-8.4_RK2.md) -- the two-stage precursor to RK4.
- [NM-8.2: Euler's Method](NM-8.2_Eulers_Method.md) -- RK1 is simply Euler's method.
- [NM-8.6: Higher-Order Systems](NM-8.6_Higher_Order_Systems.md) -- extending RK4 to systems of coupled differential equations.
- [NM-5.2: Simpson's 1/3 Rule](../NM-5_Integration/NM-5.2_Simpsons_One_Third.md) -- provides the underlying quadrature weights $(1, 4, 1 \to 1, 2, 2, 1)$ for RK4.

---

[← Previous: NM-8.4 RK2](NM-8.4_RK2.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: NM-8.6 Higher Order Systems →](NM-8.6_Higher_Order_Systems.md)
