[← Previous: NM-8.5 RK4](NM-8.5_RK4.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: NM-8.7 Physical ODE →](NM-8.7_Physical_ODE.md)

---

# NM-8.6: Higher-Order ODEs and Systems of ODEs

> 🟡 **Priority:** Light | **Tested:** 1/8 years (2018) | **Typical marks:** 5–6

## What This Is (and Why It Matters)

Every fundamental law of dynamics and electrical engineering involves second derivatives:
- Newton's second law: $F = m \frac{d^2x}{dt^2}$
- RLC electrical circuits: $L \frac{d^2q}{dt^2} + R \frac{dq}{dt} + \frac{1}{C}q = v(t)$
- Mechanical vibrations: $m \ddot{y} + c \dot{y} + k y = 0$

Yet every standard numerical solver you learned (Euler, Heun, RK2, RK4) was derived for a simple **first-order** equation $\frac{dy}{dt} = f(t, y)$.

How do we solve a second-order (or higher-order) differential equation with numerical code?

We use a technique called **State-Variable Reduction**. We invent a new auxiliary variable representing the first derivative (usually velocity $v = \frac{dy}{dt}$). This converts one second-order equation into two coupled first-order equations. Once they are both first-order, you can march them forward together in lockstep using standard Euler or Runge-Kutta!

---

## 📝 Key Definitions

> **System of Differential Equations:** "We consider the two equations $\frac{dx}{dt} = f(t, x, y)$ and $\frac{dy}{dt} = \phi(t, x, y)$ with the initial conditions $x = x_0$ and $y = y_0$, when $t = t_0$." -- Jain, §8.8 (p. 323), Eq. (8.42)
>
> **In simple words:** A set of multiple differential equations that are tangled together, where the rate of change of each variable depends on the values of the other variables.

> **Order Reduction of ODEs:** "By setting $z = y'$, the problem given in Eqs. (8.44a) and (8.45a) can be reduced to the problem of solving the system $y' = z$ and $z' = F(x, y, z)$ ... Similarly, any higher-order differential equation, in which we can solve for the highest derivative, can be reduced to a system of first-order differential equations." -- Jain, §8.8 (p. 324)
>
> **In simple words:** Turning an $n$-th order equation into $n$ first-order equations by giving each intermediate derivative its own variable name.

> **Synchronous State Stepping:** In a coupled system of equations, all variables must be updated using values measured at the exact same time step $t_n$.
>
> **In simple words:** When you step forward from $t_n$ to $t_{n+1}$, calculate the slope for every variable using old step-$n$ values before updating any of them.

---

## The Core Idea

### 1. The Conversion Recipe (State-Variable Method)

Suppose you are given a second-order initial value problem:

$$
\frac{d^2y}{dt^2} = F\left(t, y, \frac{dy}{dt}\right), \qquad y(t_0) = y_0, \quad y'(t_0) = v_0
$$

To reduce this to a system of two first-order equations:

1. **Define the first derivative as a new variable:**

$$
v = \frac{dy}{dt}
$$

2. **Differentiate $v$ to express the second derivative:**

$$
\frac{dv}{dt} = \frac{d^2y}{dt^2} = F(t, y, v)
$$

3. **Write the coupled first-order system:**

$$
\begin{cases}
\dfrac{dy}{dt} = v \\
\dfrac{dv}{dt} = F(t, y, v)
\end{cases}
$$

with the matching initial conditions:

$$
y(t_0) = y_0, \qquad v(t_0) = v_0
$$

We have traded one second-order equation for two first-order equations. The exact same procedure works for an $n$-th order equation: introduce $n-1$ new variables for the first $n-1$ derivatives, producing a system of $n$ coupled first-order equations.

---

### 2. Marching a System with Euler's Method

Once the system is in first-order form, apply Euler's formula to both variables simultaneously across step size $h$:

$$
y_{n+1} = y_n + h \cdot v_n
$$

$$
v_{n+1} = v_n + h \cdot F(t_n, y_n, v_n)
$$

$$
t_{n+1} = t_n + h
$$

> [!WARNING] The Critical Synchronous Update Rule
> Notice that the formula for $v_{n+1}$ uses $y_n$, **not** $y_{n+1}$.
> If you compute $y_{n+1}$ first and accidentally plug that new $y_{n+1}$ into the formula for $v_{n+1}$, you have accidentally implemented the *Euler-Cromer (semi-implicit)* method. While Euler-Cromer is popular in video game physics for energy conservation, it is an arithmetic error on a standard calculus exam! Always evaluate both slopes using the values from step $n$.

---

### 3. Marching a System with RK4 (For Reference)

For coupled systems $\frac{dy}{dt} = f(t, y, v)$ and $\frac{dv}{dt} = g(t, y, v)$, fourth-order Runge-Kutta computes four pairs of slopes ($k_i$ for $y$, and $l_i$ for $v$):

$$
\begin{aligned}
k_1 &= h f(t_n, y_n, v_n) \\
l_1 &= h g(t_n, y_n, v_n) \\
k_2 &= h f\left(t_n + \frac{h}{2}, \; y_n + \frac{k_1}{2}, \; v_n + \frac{l_1}{2}\right) \\
l_2 &= h g\left(t_n + \frac{h}{2}, \; y_n + \frac{k_1}{2}, \; v_n + \frac{l_1}{2}\right)
\end{aligned}
$$

and similarly for $k_3, l_3$ and $k_4, l_4$. The state vectors advance simultaneously:

$$
y_{n+1} = y_n + \frac{1}{6}(k_1 + 2k_2 + 2k_3 + k_4)
$$

$$
v_{n+1} = v_n + \frac{1}{6}(l_1 + 2l_2 + 2l_3 + l_4)
$$

---

## 🔧 Worked Example

> **From:** 2018 Q.8(b) -- [Marks: 06]

**The question:** Use the Euler's method to solve $\frac{d^2 y}{dt^2} - 0.5t = y$ where $y(0) = 2$ and $y'(0) = 0$. Solve from $t = 0$ to $0.4$ using $h = 0.1$.

**Let's solve this step by step.**

### Step 1: Convert to a first-order system

Rearrange the equation to isolate the highest derivative:

$$
\frac{d^2y}{dt^2} = y + 0.5t
$$

Introduce the velocity variable $v = \frac{dy}{dt}$. This gives the system:

$$
\begin{cases}
\dfrac{dy}{dt} = v \\
\dfrac{dv}{dt} = y + 0.5t
\end{cases}
$$

with initial values at $t_0 = 0$:

$$
y_0 = 2.0, \qquad v_0 = 0.0
$$

The Euler stepping formulas with $h = 0.1$ are:

$$
y_{n+1} = y_n + 0.1 \cdot v_n
$$

$$
v_{n+1} = v_n + 0.1 \cdot (y_n + 0.5t_n)
$$

We need to step from $t = 0$ to $t = 0.4$, which takes four steps of size $0.1$.

---

### Step 2: Step-by-Step Numerical Calculations

**Step 1 ($t_0 = 0.0 \to t_1 = 0.1$):**
- Current: $t_0 = 0.0, y_0 = 2.0, v_0 = 0.0$
- Next $y$:

$$
y_1 = y_0 + 0.1 \cdot v_0 = 2.0 + 0.1(0.0) = 2.0000
$$

- Next $v$:

$$
v_1 = v_0 + 0.1 \cdot (y_0 + 0.5t_0) = 0.0 + 0.1(2.0 + 0) = 0.2000
$$

**Step 2 ($t_1 = 0.1 \to t_2 = 0.2$):**
- Current: $t_1 = 0.1, y_1 = 2.0000, v_1 = 0.2000$
- Next $y$:

$$
y_2 = y_1 + 0.1 \cdot v_1 = 2.0 + 0.1(0.2) = 2.0200
$$

- Next $v$:

$$
v_2 = v_1 + 0.1 \cdot (y_1 + 0.5t_1) = 0.2 + 0.1(2.0 + 0.5(0.1)) = 0.2 + 0.1(2.05) = 0.2 + 0.205 = 0.4050
$$

**Step 3 ($t_2 = 0.2 \to t_3 = 0.3$):**
- Current: $t_2 = 0.2, y_2 = 2.0200, v_2 = 0.4050$
- Next $y$:

$$
y_3 = y_2 + 0.1 \cdot v_2 = 2.02 + 0.1(0.405) = 2.02 + 0.0405 = 2.0605
$$

- Next $v$:

$$
v_3 = v_2 + 0.1 \cdot (y_2 + 0.5t_2) = 0.405 + 0.1(2.02 + 0.5(0.2)) = 0.405 + 0.1(2.12) = 0.405 + 0.212 = 0.6170
$$

**Step 4 ($t_3 = 0.3 \to t_4 = 0.4$):**
- Current: $t_3 = 0.3, y_3 = 2.0605, v_3 = 0.6170$
- Next $y$:

$$
y_4 = y_3 + 0.1 \cdot v_3 = 2.0605 + 0.1(0.617) = 2.0605 + 0.0617 = 2.1222
$$

- Next $v$:

$$
v_4 = v_3 + 0.1 \cdot (y_3 + 0.5t_3) = 0.617 + 0.1(2.0605 + 0.5(0.3)) = 0.617 + 0.1(2.2105) = 0.617 + 0.22105 = 0.83805
$$

---

### Tabulated Results

| Step $n$ | $t_n$ | $y_n$ | $v_n = y'_n$ | $y_{n+1} = y_n + 0.1 v_n$ | $v_{n+1} = v_n + 0.1(y_n + 0.5t_n)$ |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 0 | 0.0 | 2.0000 | 0.0000 | 2.0000 | 0.2000 |
| 1 | 0.1 | 2.0000 | 0.2000 | 2.0200 | 0.4050 |
| 2 | 0.2 | 2.0200 | 0.4050 | 2.0605 | 0.6170 |
| 3 | 0.3 | 2.0605 | 0.6170 | 2.1222 | 0.8381 |
| 4 | 0.4 | 2.1222 | 0.8381 | -- | -- |

$$
\boxed{y(0.4) = 2.1222}
$$

**Quick sanity check:**
The second-order non-homogeneous equation $y'' - y = 0.5t$ has characteristic roots $r = \pm 1$.
The complementary function is $y_c = C_1 e^t + C_2 e^{-t}$.
A particular solution is $y_p = -0.5t$.
Applying the initial conditions $y(0) = 2$ and $y'(0) = 0$:

$$
y(t) = 2\cosh t + \frac{1}{2}\sinh t - \frac{1}{2}t
$$

Evaluating at $t = 0.4$:
$2\cosh(0.4) + 0.5\sinh(0.4) - 0.2 \approx 2(1.081072) + 0.5(0.410752) - 0.2 = 2.162144 + 0.205376 - 0.2 = 2.167520$.
Euler's numerical answer $2.1222$ is slightly lower by $0.0453$ (about $2.1\%$), which is the expected first-order truncation error for $h = 0.1$.

---

## ⚡ Quick Review

**The method in one sentence:** Turn a second-order ODE into two first-order ODEs by substituting $v = y'$, then step both equations simultaneously with Euler.

**The transformation you must memorize:**

$$
\frac{d^2y}{dt^2} = F(t, y, y') \implies
\begin{cases}
\dfrac{dy}{dt} = v \\
\dfrac{dv}{dt} = F(t, y, v)
\end{cases}
$$

**The most common exam mistake:** Using the newly computed $y_{n+1}$ inside the formula for $v_{n+1}$ instead of using $y_n$.

**Time estimate in exam:** 8–10 minutes for a four-step Euler system table.

---

## 🔗 Connected Topics

- [← NM-8.5: Runge-Kutta 4th Order](NM-8.5_RK4.md) -- the higher-order solver that can replace Euler for system stepping.
- [NM-8.2: Euler's Method](NM-8.2_Eulers_Method.md) -- the single-equation algorithm that powers this system march.
- [→ NM-8.7: Physical ODE](NM-8.7_Physical_ODE.md) -- modeling physical systems that lead to differential equations.
- [NM-8.8: Boundary Value Problems](NM-8.8_Boundary_Value_Problems.md) -- the alternative approach for second-order ODEs when conditions sit at boundaries instead of the initial point.

---

[← Previous: NM-8.5 RK4](NM-8.5_RK4.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: NM-8.7 Physical ODE →](NM-8.7_Physical_ODE.md)
