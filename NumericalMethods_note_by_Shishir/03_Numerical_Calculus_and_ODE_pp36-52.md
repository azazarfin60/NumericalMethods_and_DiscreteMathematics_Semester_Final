---
title: "Numerical Solutions of ODEs and Finite Differences (Pages 36–52)"
course: "ECE 2213 — Numerical Analysis / Numerical Methods"
author: "Shishir (Roll 2310002)"
batch: "Batch 3 (Pages 36–52)"
source: "Numerical Analysis By Shishir 2310002.pdf"
tags:
  - numerical-methods
  - ece2213
  - ordinary-differential-equations
  - eulers-method
  - modified-euler
  - taylors-series-method
  - runge-kutta
  - rk4
  - forward-differences
  - backward-differences
  - central-differences
  - newton-gregory-interpolation
  - gauss-forward-interpolation
---

# Numerical Solutions of Ordinary Differential Equations & Finite Difference Interpolation

---

## Part I: Numerical Solutions of Ordinary Differential Equations (ODEs)

<!-- Page 36 -->

### 1. Euler's Method

The **Euler Method** is the most fundamental single-step numerical procedure for solving first-order initial value problems (IVPs) of the form:

$$
\frac{dy}{dx} = f(x, y), \quad y(x_0) = y_0
$$

Given a uniform grid spacing $h = x_{n+1} - x_n$, Euler's forward-stepping recurrence formula is:

$$
y_{n+1} = y_n + h f(x_n, y_n)
$$

---

#### 1.1 Problem Statement

> **Problem (Page 36):**  
> Apply Euler's Method to solve:
> 
> $$
> \frac{dy}{dx} = x + y, \quad y(0) = 0
> $$
> 
> Choosing an appropriate step length, find $y(1.4)$.

---

#### 1.2 Initial Setup & Step Size Selection

From the problem statement:

$$
\begin{aligned}
f(x, y) &= x + y \\
x_0 &= 0, \quad y_0 = 0 \\
h &= 0.2 \quad \text{(Chosen step length)} \\
\text{Target:} &\quad y(1.4) = ?
\end{aligned}
$$

The target point $x = 1.4$ is reached in $N = \frac{1.4 - 0}{0.2} = 7$ successive steps.

---

#### 1.3 Step-by-Step Euler Iterations

##### Step 1: Calculation at $x_1 = 0.2$

The approximate value of $y$ at $x_1 = 0.2$:

$$
\begin{aligned}
y_1 &= y_0 + h f(x_0, y_0) \\
&= 0 + 0.2 [x_0 + y_0] \\
&= 0 + 0.2 [0 + 0] \\
y_1 &= 0
\end{aligned}
$$

$$
\therefore y(0.2) \approx 0
$$

---

<!-- Page 37 -->

##### Step 2: Calculation at $x_2 = 0.4$

The approximate value of $y$ at $x_2 = 0.4$:

$$
\begin{aligned}
y_2 &= y_1 + h f(x_1, y_1) \\
&= 0 + 0.2 (x_1 + y_1) \\
&= 0.2 (0.2 + 0) \\
y_2 &= 0.04
\end{aligned}
$$

$$
\therefore y(0.4) \approx 0.04
$$

---

##### Step 3: Calculation at $x_3 = 0.6$

The approximate value of $y$ at $x_3 = 0.6$:

$$
\begin{aligned}
y_3 &= y_2 + h f(x_2, y_2) \\
&= 0.04 + 0.2 (x_2 + y_2) \\
&= 0.04 + 0.2 (0.4 + 0.04) \\
&= 0.04 + 0.2(0.44) \\
&= 0.04 + 0.088 \\
y_3 &= 0.128
\end{aligned}
$$

$$
\therefore y(0.6) \approx 0.128
$$

---

##### Step 4: Calculation at $x_4 = 0.8$

The approximate value of $y$ at $x_4 = 0.8$:

$$
\begin{aligned}
y_4 &= y_3 + h f(x_3, y_3) \\
&= y_3 + h [x_3 + y_3] \\
&= 0.128 + 0.2 [0.6 + 0.128] \\
&= 0.128 + 0.2(0.728) \\
&= 0.128 + 0.1456 \\
y_4 &= 0.2736
\end{aligned}
$$

$$
\therefore y(0.8) \approx 0.2736
$$

---

<!-- Page 38 -->

##### Step 5: Calculation at $x_5 = 1.0$

The approximate value of $y$ at $x_5 = 1.0$:

$$
\begin{aligned}
y_5 &= y_4 + h f(x_4, y_4) \\
&= 0.2736 + 0.2 (0.8 + 0.2736) \\
&= 0.2736 + 0.2 (1.0736) \\
&= 0.2736 + 0.21472 \\
&= 0.48832 \approx 0.4883
\end{aligned}
$$

$$
\therefore y(1.0) \approx 0.4883
$$

---

##### Step 6: Calculation at $x_6 = 1.2$

The approximate value of $y$ at $x_6 = 1.2$:

$$
\begin{aligned}
y_6 &= y_5 + h f(x_5, y_5) \\
&= 0.4883 + 0.2 (1.0 + 0.4883) \\
&= 0.4883 + 0.2 (1.4883) \\
&= 0.4883 + 0.29766 \\
&= 0.78596 \approx 0.786
\end{aligned}
$$

$$
\therefore y(1.2) \approx 0.786
$$

---

##### Step 7: Calculation at $x_7 = 1.4$

The approximate value of $y$ at $x_7 = 1.4$:

$$
\begin{aligned}
y_7 &= y_6 + h f(x_6, y_6) \\
&= 0.786 + 0.2 (1.2 + 0.786) \\
&= 0.786 + 0.2 (1.986) \\
&= 0.786 + 0.3972 \\
y_7 &= 1.1832
\end{aligned}
$$

$$
\mathbf{y(1.4) \approx 1.1832 \quad (\text{Approx})}
$$

---

#### 1.4 Analytical Error Analysis & Summary Table

> [!note] Analytical Solution & Error Discussion
> The exact analytical solution of $\frac{dy}{dx} - y = x$ with $y(0) = 0$ is obtained using the integrating factor $I(x) = e^{\int -1 dx} = e^{-x}$:
> 
> $$
> y(x) = e^x - x - 1
> $$
> 
> At $x = 1.4$:
> 
> $$
> y_{\text{exact}}(1.4) = e^{1.4} - 1.4 - 1 \approx 4.0552 - 2.4 = 1.6552
> $$
> 
> The large deviation ($1.1832$ vs $1.6552$) demonstrates the substantial cumulative local truncation error $\mathcal{O}(h)$ inherent to standard Euler's method over multi-step intervals with coarse step size ($h = 0.2$). This directly motivates the higher-order methods studied next: **Modified Euler**, **Taylor Series**, and **Runge-Kutta**.

| Step $n$ | $x_n$ | $y_n$ (Euler Approximation) | $f(x_n, y_n) = x_n + y_n$ | Increment $h f(x_n, y_n)$ |
| :---: | :---: | :---: | :---: | :---: |
| $0$ | $0.0$ | $0.0000$ | $0.0000$ | $0.0000$ |
| $1$ | $0.2$ | $0.0000$ | $0.2000$ | $0.0400$ |
| $2$ | $0.4$ | $0.0400$ | $0.4400$ | $0.0880$ |
| $3$ | $0.6$ | $0.1280$ | $0.7280$ | $0.1456$ |
| $4$ | $0.8$ | $0.2736$ | $1.0736$ | $0.2147$ |
| $5$ | $1.0$ | $0.4883$ | $1.4883$ | $0.2977$ |
| $6$ | $1.2$ | $0.7860$ | $1.9860$ | $0.3972$ |
| **7** | **1.4** | **1.1832** | — | — |

---

<!-- Page 39 -->

### 2. Modified Euler's Method (Heun's Predictor-Corrector)

**Modified Euler's Method** improves accuracy by averaging the slopes at the beginning and the predicted end of each interval:

1. **Predictor Step (Euler):**
   
   $$
   y_{n+1}^{(0)} = y_n + h f(x_n, y_n)
   $$

2. **Corrector Step (Trapezoidal Iteration):**
   
   $$
   y_{n+1}^{(k)} = y_n + \frac{h}{2} \left[ f(x_n, y_n) + f\left(x_{n+1}, y_{n+1}^{(k-1)}\right) \right], \quad k = 1, 2, 3, \dots
   $$

The corrector is iterated until successive values of $y_{n+1}$ agree to the desired number of decimal places.

---

#### 2.1 Problem Statement

> **Problem (Page 39):**  
> Solve the differential equation:
> 
> $$
> \frac{dy}{dx} = -x y^2, \quad y = 2 \text{ at } x = 0
> $$
> 
> by Modified Euler's method and obtain $y$ at $x = 0.2$ in two steps of $0.1$ each.

---

#### 2.2 Initial Setup

$$
\begin{aligned}
f(x, y) &= -x y^2 \\
x_0 &= 0, \quad y_0 = 2 \\
h &= 0.1 \\
\text{Target:} &\quad y(0.2) = ? \quad \text{via } x_1 = 0.1 \text{ and } x_2 = 0.2
\end{aligned}
$$

---

#### 2.3 Step 1: Finding $y_1$ at $x_1 = 0.1$

##### Predictor for Step 1 ($x_1 = 0.1$):

$$
\begin{aligned}
y_1^{(0)} &= y_0 + h f(x_0, y_0) \\
&= 2 + 0.1 [-x_0 y_0^2] \\
&= 2 + 0.1 [-0 \times 2^2] \\
\therefore y_1^{(0)} &= 2
\end{aligned}
$$

##### Corrector Iteration 1 ($y_1^{(1)}$):

$$
\begin{aligned}
y_1^{(1)} &= y_0 + \frac{h}{2} \left[ f(x_0, y_0) + f(x_1, y_1^{(0)}) \right] \\
&= 2 + \frac{0.1}{2} \left[ -x_0 y_0^2 - x_1 (y_1^{(0)})^2 \right] \\
&= 2 + \frac{0.1}{2} \left[ -0 - 0.1(2)^2 \right] \\
&= 2 + 0.05 [-0.4] \\
&= 2 - 0.02 \\
y_1^{(1)} &= 1.98
\end{aligned}
$$

> [!tip] Pedagogical Guidance: Purpose of Corrector Iterations
> **Author's Annotation:**  
> `[ y₁⁽¹⁾ → Polish করলাম y₁ কে যে আরও accuracy আনা Possible কিনা ]`  
> **Translation & Explanation:**  
> *"We polished (refined) $y_1$ to see whether higher accuracy is achievable."*  
> The corrector step evaluates the slope at the predicted point $(x_1, y_1^{(0)})$ and averages it with the initial slope, systematically filtering out first-order truncation error until successive iterates converge.

---

<!-- Page 40 -->

##### Corrector Iteration 2 ($y_1^{(2)}$):

$$
\begin{aligned}
y_1^{(2)} &= y_0 + \frac{h}{2} \left[ f(x_0, y_0) + f(x_1, y_1^{(1)}) \right] \\
&= 2 + \frac{0.1}{2} \left[ -x_0 y_0^2 - x_1 (y_1^{(1)})^2 \right] \\
&= 2 + 0.05 \left[ 0 - 0.1 \times (1.98)^2 \right] \\
&= 2 + 0.05 [-0.39204] \\
&= 2 - 0.019602 \\
y_1^{(2)} &= 1.980398 \approx 1.9804
\end{aligned}
$$

##### Corrector Iteration 3 ($y_1^{(3)}$):

$$
\begin{aligned}
y_1^{(3)} &= y_0 + \frac{h}{2} \left[ f(x_0, y_0) + f(x_1, y_1^{(2)}) \right] \\
&= 2 + \frac{0.1}{2} \left[ -x_0 y_0^2 - x_1 (y_1^{(2)})^2 \right] \\
&= 2 + 0.05 \left[ 0 - 0.1 \times (1.9804)^2 \right] \\
&= 2 - 0.01961 \\
y_1^{(3)} &= 1.9804
\end{aligned}
$$

Since $y_1^{(2)} = y_1^{(3)} = 1.9804$, convergence is achieved to four decimal places.

$$
\mathbf{\text{Thus at } x_1 = 0.1: \quad y_1 = 1.9804}
$$

---

#### 2.4 Step 2: Finding $y_2$ at $x_2 = 0.2$

Base values: $x_1 = 0.1$, $y_1 = 1.9804$, $h = 0.1$.

##### Predictor for Step 2 ($x_2 = 0.2$):

$$
\begin{aligned}
y_2^{(0)} &= y_1 + h f(x_1, y_1) \\
&= 1.9804 + 0.1 (-x_1 y_1^2) \\
&= 1.9804 + 0.1 [-0.1 \times (1.9804)^2] \\
&= 1.9804 + 0.1 [-0.1 \times 3.9220] \\
&= 1.9804 - 0.03922 \\
y_2^{(0)} &= 1.94118 \approx 1.9412
\end{aligned}
$$

---

<!-- Page 41 -->

##### Corrector Iteration 1 ($y_2^{(1)}$):

$$
\begin{aligned}
y_2^{(1)} &= y_1 + \frac{h}{2} \left[ f(x_1, y_1) + f(x_2, y_2^{(0)}) \right] \\
&= 1.9804 + \frac{0.1}{2} \left[ -x_1 y_1^2 - x_2 (y_2^{(0)})^2 \right] \\
&= 1.9804 + 0.05 \left[ -0.1(1.9804)^2 - 0.2(1.9412)^2 \right] \\
&= 1.9804 + 0.05 [-0.3922 - 0.7537] \\
&= 1.9804 + 0.05 (-1.1459) \\
&= 1.9804 - 0.0573 \\
y_2^{(1)} &= 1.9231
\end{aligned}
$$

##### Corrector Iteration 2 ($y_2^{(2)}$):

$$
\begin{aligned}
y_2^{(2)} &= y_1 + \frac{h}{2} \left[ f(x_1, y_1) + f(x_2, y_2^{(1)}) \right] \\
&= 1.9804 + \frac{0.1}{2} \left[ -x_1 y_1^2 - x_2 (y_2^{(1)})^2 \right] \\
&= 1.9804 + 0.05 \left[ -0.3922 - 0.2(1.9231)^2 \right] \\
&= 1.9804 + 0.05 [-0.3922 - 0.7397] \\
&= 1.9804 - 0.0566 \\
y_2^{(2)} &= 1.9238
\end{aligned}
$$

##### Corrector Iteration 3 ($y_2^{(3)}$):

$$
\begin{aligned}
y_2^{(3)} &= y_1 + \frac{h}{2} \left[ f(x_1, y_1) + f(x_2, y_2^{(2)}) \right] \\
&= 1.9804 + \frac{0.1}{2} \left[ -x_1 y_1^2 - x_2 (y_2^{(2)})^2 \right] \\
&= 1.9804 + 0.05 \left[ -0.3922 - 0.2(1.9238)^2 \right] \\
&= 1.9804 + 0.05 [-0.3922 - 0.7402] \\
y_2^{(3)} &= 1.9238
\end{aligned}
$$

Since $y_2^{(2)} = y_2^{(3)} = 1.9238$, full convergence is achieved.

$$
\mathbf{\text{Thus at } x_2 = 0.2: \quad y(0.2) = 1.9238 \quad (\text{Approx})}
$$

> [!note] Analytical Cross-Check
> Separating variables in $\frac{dy}{dx} = -x y^2$:
> 
> $$
> -\frac{dy}{y^2} = x dx \implies \frac{1}{y} = \frac{x^2}{2} + C
> $$
> 
> Using $y(0) = 2 \implies C = \frac{1}{2}$. Thus:
> 
> $$
> y(x) = \frac{2}{1 + x^2}
> $$
> 
> At $x = 0.2$:
> 
> $$
> y_{\text{exact}}(0.2) = \frac{2}{1 + (0.2)^2} = \frac{2}{1.04} \approx 1.923077
> $$
> 
> The Modified Euler method yielded $1.9238$, maintaining high accuracy ($\approx 0.037\%$ error) in just two steps!

---

<!-- Page 42 -->

### 3. Taylor's Series Method

The **Taylor Series Method** expands $y(x)$ in the vicinity of $x_n$:

$$
y_{n+1} = y_n + h y_n' + \frac{h^2}{2!} y_n'' + \frac{h^3}{3!} y_n''' + \frac{h^4}{4!} y_n^{(iv)} + \dots
$$

Higher-order derivatives $y'', y''', \dots$ are obtained by successively differentiating the governing differential equation $y' = f(x, y)$ with respect to $x$.

---

#### 3.1 Problem Statement

> **Problem (Page 42):**  
> Solve $\frac{dy}{dx} = x + y$ using Taylor's series method.  
> Start from $x = 1$, $y = 0$ and carry to $x = 1.2$ with $h = 0.1$.

---

#### 3.2 Successive Differentiation of the ODE

Given:

$$
\frac{dy}{dx} = x + y
$$

Differentiating repeatedly with respect to $x$:

$$
\begin{aligned}
y' &= x + y \\
y'' &= \frac{d}{dx}(x + y) = 1 + y' \\
y''' &= \frac{d}{dx}(1 + y') = y'' \\
y^{(iv)} &= \frac{d}{dx}(y'') = y'''
\end{aligned}
$$

---

#### 3.3 Step 1: Calculation at $x_1 = 1.1$

Base conditions: $x_0 = 1$, $y_0 = 0$, $h = 0.1$.

Evaluating the derivatives at $(x_0, y_0)$:

$$
\begin{aligned}
y_0' &= x_0 + y_0 = 1 + 0 = 1 \\
y_0'' &= 1 + y_0' = 1 + 1 = 2 \\
y_0''' &= y_0'' = 2 \\
y_0^{(iv)} &= y_0''' = 2
\end{aligned}
$$

Substituting into the Taylor series expansion:

$$
\begin{aligned}
y_1 &= y_0 + h y_0' + \frac{h^2}{2!} y_0'' + \frac{h^3}{3!} y_0''' + \frac{h^4}{4!} y_0^{(iv)} + \dots \\
&= 0 + 0.1(1) + \frac{(0.1)^2}{2!} (2) + \frac{(0.1)^3}{3!} (2) + \frac{(0.1)^4}{4!} (2) + \dots \\
&= 0.1 + 0.01 + \frac{0.002}{6} + \frac{0.0002}{24} \\
&= 0.11 + 0.0003333 + 0.0000083 \\
y_1 &= 0.1103416 \approx 0.1103
\end{aligned}
$$

$$
\mathbf{\text{At } x_1 = 1.1: \quad y_1 = 0.1103}
$$

---

<!-- Page 43 -->

#### 3.4 Step 2: Calculation at $x_2 = 1.2$

Base conditions: $x_1 = 1.1$, $y_1 = 0.1103$, $h = 0.1$.

Evaluating derivatives at $(x_1, y_1)$:

$$
\begin{aligned}
y_1' &= x_1 + y_1 = 1.1 + 0.1103 = 1.2103 \\
y_1'' &= 1 + y_1' = 1 + 1.2103 = 2.2103 \\
y_1''' &= y_1'' = 2.2103 \\
y_1^{(iv)} &= y_1''' = 2.2103
\end{aligned}
$$

Substituting into the Taylor series expansion:

$$
\begin{aligned}
y_2 &= y_1 + h y_1' + \frac{h^2}{2!} y_1'' + \frac{h^3}{3!} y_1''' + \frac{h^4}{4!} y_1^{(iv)} + \dots \\
&= 0.1103 + 0.1(1.2103) + \frac{(0.1)^2}{2!} (2.2103) + \frac{(0.1)^3}{3!} (2.2103) + \dots \\
&= 0.1103 + 0.12103 + 0.005 \times (2.2103) + \frac{0.001}{6} \times (2.2103) \\
&= 0.1103 + 0.12103 + 0.0110515 + 0.0003684 \\
y_2 &= 0.24275 \approx 0.2428
\end{aligned}
$$

$$
\mathbf{\text{At } x_2 = 1.2: \quad y(1.2) = 0.2428 \quad (\text{Approx})}
$$

> [!note] Analytical Cross-Check
> General solution of $\frac{dy}{dx} - y = x$ is $y(x) = C e^x - x - 1$.  
> Using $y(1) = 0 \implies C e - 2 = 0 \implies C = 2e^{-1}$.  
> Thus, $y(x) = 2e^{x-1} - x - 1$.  
> At $x = 1.2$:
> 
> $$
> y_{\text{exact}}(1.2) = 2e^{0.2} - 1.2 - 1 = 2(1.2214028) - 2.2 = 2.4428056 - 2.2 = 0.242806
> $$
> 
> Taylor series up to the 4th derivative matches the true analytical solution to **four full decimal places**!

---

<!-- Page 44 -->

### 4. Runge-Kutta (R-K) Family of Methods

The **Runge-Kutta methods** achieve the high-order accuracy of Taylor series expansions without requiring analytical evaluation of higher-order derivatives. Instead, they compute weighted averages of function evaluations $f(x, y)$ at several sample points within each step.

---

#### 4.1 Runge-Kutta First Order Method

Equivalent to standard **Euler's Method**:

$$
\begin{aligned}
K_1 &= h f(x_0, y_0) \\
y_1 &= y_0 + K_1 = y_0 + h f(x_0, y_0)
\end{aligned}
$$

---

#### 4.2 Runge-Kutta Second Order Method

Equivalent to **Heun's Method**:

$$
\begin{aligned}
K_1 &= h f(x_0, y_0) \\
K_2 &= h f(x_0 + h, y_0 + K_1) \\
K &= \frac{1}{2}(K_1 + K_2) \\
y_1 &= y_0 + K
\end{aligned}
$$

---

#### 4.3 Runge-Kutta Third Order Method

$$
\begin{aligned}
K_1 &= h f(x_0, y_0) \\
K_2 &= h f\left(x_0 + \frac{h}{2}, y_0 + \frac{K_1}{2}\right) \\
K_3 &= h f(x_0 + h, y_0 + 2K_2 - K_1) \\
K &= \frac{1}{6}(K_1 + 4K_2 + K_3) \\
y_1 &= y_0 + K
\end{aligned}
$$

---

<!-- Page 45 -->

#### 4.4 Runge-Kutta Fourth Order Method (Classical RK4)

The classical **RK4** method is widely considered the gold standard for numerical integration of non-stiff ordinary differential equations due to its optimal balance between computational complexity and fourth-order local accuracy ($\mathcal{O}(h^5)$ local truncation error):

$$
\begin{aligned}
K_1 &= h f(x_0, y_0) \\
K_2 &= h f\left(x_0 + \frac{h}{2}, y_0 + \frac{K_1}{2}\right) \\
K_3 &= h f\left(x_0 + \frac{h}{2}, y_0 + \frac{K_2}{2}\right) \\
K_4 &= h f(x_0 + h, y_0 + K_3)
\end{aligned}
$$

The composite weighted increment $K$ and updated solution $y_1$ are:

$$
\begin{aligned}
K &= \frac{1}{6}(K_1 + 2K_2 + 2K_3 + K_4) \\
y_1 &= y_0 + K
\end{aligned}
$$

---

#### 4.5 Problem Statement (RK4)

> **Problem (Page 45):**  
> Apply Runge-Kutta fourth order method to find an approximate value of $y$ when $x = 0.2$, given that:
> 
> $$
> \frac{dy}{dx} = x + y, \quad \text{and } y = 1 \text{ when } x = 0
> $$

---

#### 4.6 Step-by-Step RK4 Calculation

##### Initial Setup:

$$
\begin{aligned}
f(x, y) &= x + y \\
x_0 &= 0, \quad y_0 = 1 \\
h &= 0.2 \\
x_1 &= x_0 + h = 0 + 0.2 = 0.2 \\
\text{Target:} &\quad y(0.2) = ?
\end{aligned}
$$

##### Evaluation of $K_1$:

$$
\begin{aligned}
K_1 &= h f(x_0, y_0) \\
&= 0.2 (x_0 + y_0) \\
&= 0.2 (0 + 1) \\
K_1 &= 0.2
\end{aligned}
$$

---

<!-- Page 46 -->

##### Evaluation of $K_2$:

$$
\begin{aligned}
K_2 &= h f\left(x_0 + \frac{h}{2}, y_0 + \frac{K_1}{2}\right) \\
&= 0.2 \left[ \left(x_0 + \frac{h}{2}\right) + \left(y_0 + \frac{K_1}{2}\right) \right] \\
&= 0.2 \left[ \left(0 + \frac{0.2}{2}\right) + \left(1 + \frac{0.2}{2}\right) \right] \\
&= 0.2 [0.1 + 1.1] \\
&= 0.2 [1.2] \\
K_2 &= 0.24
\end{aligned}
$$

##### Evaluation of $K_3$:

$$
\begin{aligned}
K_3 &= h f\left(x_0 + \frac{h}{2}, y_0 + \frac{K_2}{2}\right) \\
&= 0.2 \left[ \left(x_0 + \frac{h}{2}\right) + \left(y_0 + \frac{K_2}{2}\right) \right] \\
&= 0.2 \left[ (0 + 0.1) + \left(1 + \frac{0.24}{2}\right) \right] \\
&= 0.2 [0.1 + 1.12] \\
&= 0.2 [1.22] \\
K_3 &= 0.244
\end{aligned}
$$

##### Evaluation of $K_4$:

$$
\begin{aligned}
K_4 &= h f(x_0 + h, y_0 + K_3) \\
&= 0.2 [(x_0 + h) + (y_0 + K_3)] \\
&= 0.2 [(0 + 0.2) + (1 + 0.244)] \\
&= 0.2 [0.2 + 1.244] \\
&= 0.2 [1.444] \\
K_4 &= 0.2888
\end{aligned}
$$

##### Weighted Average Increment $K$:

$$
\begin{aligned}
K &= \frac{1}{6}(K_1 + 2K_2 + 2K_3 + K_4) \\
&= \frac{1}{6}[0.2 + 2(0.24) + 2(0.244) + 0.2888] \\
&= \frac{1}{6}[0.2 + 0.48 + 0.488 + 0.2888] \\
&= \frac{1}{6}[1.4568] \\
K &= 0.2428
\end{aligned}
$$

##### Final Solution Value:

$$
\begin{aligned}
y_1 &= y_0 + K \\
&= 1 + 0.2428 \\
y_1 &= 1.2428
\end{aligned}
$$

$$
\mathbf{y(0.2) \approx 1.2428 \quad (\text{Approx})}
$$

> [!note] Analytical Cross-Check for RK4
> The exact solution of $\frac{dy}{dx} - y = x$ with $y(0) = 1$ is:
> 
> $$
> y(x) = 2e^x - x - 1
> $$
> 
> At $x = 0.2$:
> 
> $$
> y_{\text{exact}}(0.2) = 2e^{0.2} - 0.2 - 1 = 2(1.22140276) - 1.2 = 2.4428055 - 1.2 = 1.2428055
> $$
> 
> RK4 achieves **exact agreement to four decimal places** ($1.2428$) in a single step with $h = 0.2$!

---

<!-- Page 47 -->

#### 4.7 Author's Pedagogical Rule for Multi-Step Runge-Kutta Problems

> [!important] Multi-Step RK Procedure Rule
> **Author's Annotation (Page 47):**  
> `[ এখন যদি h দেওয়া থাকে আর বলে y(1.2) বের কর তাহলে x₁=0.2, x₂=0.4, x₃=0.6, x₄=0.8 ... এইভাবে ধরে y₁, y₂, y₃, y₄ ... বের করব এবং last y(1.2) বের করব।`  
> `yₙ = yₙ₋₁ + K`  
> `যদি x₃ এর জন্য হয় তাহলে K তে x₂, y₂ বসবে মানে যত এর জন্য বের করব তার থেকে 1 কম হবে। ]`  
> 
> **Translation & Rigorous Explanation:**  
> 1. **Sequential Stepping:** If a distant target point (e.g., $y(1.2)$) is requested with a given step size $h = 0.2$, one must march forward step-by-step through the intermediate grid nodes:
>    
>    $$
>    x_1 = 0.2 \to x_2 = 0.4 \to x_3 = 0.6 \to x_4 = 0.8 \to x_5 = 1.0 \to x_6 = 1.2
>    $$
>    
> 2. **Recurrence Relation:** For step $n$, the state updates as:
>    
>    $$
>    y_n = y_{n-1} + K
>    $$
>    
> 3. **Base Coordinate Indexing:** To compute $y_n$ at node $x_n$, the slope increments $K_1, K_2, K_3, K_4$ must always evaluate the differential equation using the coordinates of the **immediately preceding point** $(x_{n-1}, y_{n-1})$. For example, to find $y_3$ at $x_3$, evaluate all $K$ expressions starting from $(x_2, y_2)$ — always indexed **one step lower**.

---

## Part II: Finite Differences and Interpolation

Finite differences form the backbone of numerical interpolation, differentiation, and integration for discrete data sets defined on equispaced grids $x_n = x_0 + n h$.

---

### 5. Forward Difference Table

The **forward difference operator** $\Delta$ is defined as:

$$
\Delta f(x_i) = f(x_{i+1}) - f(x_i) = y_{i+1} - y_i
$$

Higher-order forward differences are defined recursively:

$$
\Delta^n y_i = \Delta^{n-1} y_{i+1} - \Delta^{n-1} y_i
$$

---

#### 5.1 Problem Statement

> **Problem (Page 47):**  
> Construct a forward difference table for the following data:
> 
> | $x$ | $45$ | $50$ | $55$ | $60$ | $65$ |
> | :---: | :---: | :---: | :---: | :---: | :---: |
> | $f(x)$ | $2.871$ | $2.404$ | $2.083$ | $1.862$ | $1.712$ |

---

#### 5.2 Complete Forward Difference Table

The equispaced step size is $h = 5$.

```text
 x     f(x)      Δf(x)       Δ²f(x)      Δ³f(x)      Δ⁴f(x)
─────────────────────────────────────────────────────────────
45    2.871
                -0.467 (Δy₀)
50    2.404                  0.146 (Δ²y₀)
                -0.321 (Δy₁)             -0.046 (Δ³y₀)
55    2.083                  0.100 (Δ²y₁)             0.017 (Δ⁴y₀)
                -0.221 (Δy₂)             -0.029 (Δ³y₁)
60    1.862                  0.071 (Δ²y₂)
                -0.150 (Δy₃)
65    1.712
```

| $x$ | $f(x)$ | $\Delta f(x)$ | $\Delta^2 f(x)$ | $\Delta^3 f(x)$ | $\Delta^4 f(x)$ |
| :---: | :---: | :---: | :---: | :---: | :---: |
| $45$ ($x_0$) | **$2.871$** ($y_0$) | | | | |
| | | **$-0.467$** ($\Delta y_0$) | | | |
| $50$ ($x_1$) | $2.404$ ($y_1$) | | **$0.146$** ($\Delta^2 y_0$) | | |
| | | $-0.321$ ($\Delta y_1$) | | **$-0.046$** ($\Delta^3 y_0$) | |
| $55$ ($x_2$) | $2.083$ ($y_2$) | | $0.100$ ($\Delta^2 y_1$) | | **$0.017$** ($\Delta^4 y_0$) |
| | | $-0.221$ ($\Delta y_2$) | | $-0.029$ ($\Delta^3 y_1$) | |
| $60$ ($x_3$) | $1.862$ ($y_3$) | | $0.071$ ($\Delta^2 y_2$) | | |
| | | $-0.150$ ($\Delta y_3$) | | | |
| $65$ ($x_4$) | $1.712$ ($y_4$) | | | | |

> [!note] Forward Difference Diagonal Path
> The bold entries along the upper forward diagonal originating at $y_0 = 2.871$:
> 
> $$
> \Delta y_0 = -0.467, \quad \Delta^2 y_0 = 0.146, \quad \Delta^3 y_0 = -0.046, \quad \Delta^4 y_0 = 0.017
> $$
> 
> are the exact coefficients utilized in **Newton's Forward Interpolation formula**.

---

<!-- Page 48 -->

### 6. Backward Difference Table

The **backward difference operator** $\nabla$ is defined as:

$$
\nabla f(x_i) = f(x_i) - f(x_{i-1}) = y_i - y_{i-1}
$$

Higher-order backward differences are defined recursively:

$$
\nabla^n y_i = \nabla^{n-1} y_i - \nabla^{n-1} y_{i-1}
$$

---

#### 6.1 Problem Statement

> **Problem (Page 48):**  
> Construct a backward difference table for the following data:
> 
> | $x$ | $45$ | $50$ | $55$ | $60$ | $65$ |
> | :---: | :---: | :---: | :---: | :---: | :---: |
> | $f(x)$ | $2.871$ | $2.404$ | $2.083$ | $1.862$ | $1.712$ |

---

#### 6.2 Complete Backward Difference Table

```text
 x     f(x)      ∇f(x)       ∇²f(x)      ∇³f(x)      ∇⁴f(x)
─────────────────────────────────────────────────────────────
45    2.871
                -0.467 (∇y₁)
50    2.404                  0.146 (∇²y₂)
                -0.321 (∇y₂)             -0.046 (∇³y₃)
55    2.083                  0.100 (∇²y₃)             0.017 (∇⁴y₄)
                -0.221 (∇y₃)             -0.029 (∇³y₄)
60    1.862                  0.071 (∇²y₄)
                -0.150 (∇y₄)
65    1.712
```

| $x$ | $f(x)$ | $\nabla f(x)$ | $\nabla^2 f(x)$ | $\nabla^3 f(x)$ | $\nabla^4 f(x)$ |
| :---: | :---: | :---: | :---: | :---: | :---: |
| $45$ ($x_0$) | $2.871$ ($y_0$) | | | | |
| | | $-0.467$ ($\nabla y_1$) | | | |
| $50$ ($x_1$) | $2.404$ ($y_1$) | | $0.146$ ($\nabla^2 y_2$) | | |
| | | $-0.321$ ($\nabla y_2$) | | $-0.046$ ($\nabla^3 y_3$) | |
| $55$ ($x_2$) | $2.083$ ($y_2$) | | $0.100$ ($\nabla^2 y_3$) | | **$0.017$** ($\nabla^4 y_4$) |
| | | $-0.221$ ($\nabla y_3$) | | **$-0.029$** ($\nabla^3 y_4$) | |
| $60$ ($x_3$) | $1.862$ ($y_3$) | | **$0.071$** ($\nabla^2 y_4$) | | |
| | | **$-0.150$** ($\nabla y_4$) | | | |
| $65$ ($x_4$) | **$1.712$** ($y_4$) | | | | |

> [!note] Backward Difference Diagonal Path
> The bold entries along the lower backward diagonal ending at $y_4 = 1.712$:
> 
> $$
> \nabla y_4 = -0.150, \quad \nabla^2 y_4 = 0.071, \quad \nabla^3 y_4 = -0.029, \quad \nabla^4 y_4 = 0.017
> $$
> 
> are the exact coefficients utilized in **Newton's Backward Interpolation formula**. Notice that while the numerical differences in the interior of the table are identical to the forward table, their indexing is aligned with the lower/later row indices.

---

<!-- Page 49 -->

### 7. Newton-Gregory Forward Interpolation

The **Newton-Gregory Forward Interpolation Formula** approximates $f(x)$ for an interpolated point located near the beginning of a tabulated set of equispaced values:

$$
f(a + u h) = f(a) + u \Delta f(a) + \frac{u(u-1)}{2!} \Delta^2 f(a) + \frac{u(u-1)(u-2)}{3!} \Delta^3 f(a) + \dots
$$

Where:
- $a = x_0$ is the starting base point.
- $h$ is the uniform interval width.
- $u = \frac{x - a}{h}$ is the dimensionless interpolation coordinate.

---

#### 7.1 Problem Statement

> **Problem (Page 49):**  
> The values of $f(x)$ are given by:
> 
> | $x$ | $0$ | $1$ | $2$ | $3$ | $4$ | $5$ | $6$ |
> | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
> | $f(x)$ | $1$ | $4$ | $17$ | $46$ | $97$ | $176$ | $289$ |
> 
> Estimate the value of $f(2.3)$ using **only five of the given** values.

---

#### 7.2 Point Selection Strategy & Forward Table Construction

> [!tip] Pedagogical Guidance: When to Use Forward Interpolation
> **Author's Annotation (Page 49):**  
> `[ Table এর starting এর value লাগবে তাই forward interpolation করব। ]`  
> **Translation & Rationale:**  
> *"Since we need an interpolated value near the start of our selected table, we apply forward interpolation."*  
> 
> To estimate $f(2.3)$ using exactly 5 data points, we choose the contiguous sub-range $x \in \{2, 3, 4, 5, 6\}$. This places $x = 2.3$ immediately following the initial node $a = x_0 = 2$, ensuring $0 < u < 1$ and minimizing extrapolation error.

##### Difference Table for the Selected 5 Points:

$h = 1, \quad a = x_0 = 2, \quad x = 2.3$

$$
u = \frac{x - a}{h} = \frac{2.3 - 2}{1} = 0.3
$$

| $x$ | $f(x)$ | $\Delta f(x)$ | $\Delta^2 f(x)$ | $\Delta^3 f(x)$ | $\Delta^4 f(x)$ |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **2** | **17** ($y_0$) | | | | |
| | | **29** ($\Delta y_0$) | | | |
| 3 | 46 | | **22** ($\Delta^2 y_0$) | | |
| | | 51 | | **6** ($\Delta^3 y_0$) | |
| 4 | 97 | | 28 | | **0** ($\Delta^4 y_0$) |
| | | 79 | | 6 | |
| 5 | 176 | | 34 | | |
| | | 113 | | | |
| 6 | 289 | | | | |

Selected leading differences:

$$
f(2) = 17, \quad \Delta f(2) = 29, \quad \Delta^2 f(2) = 22, \quad \Delta^3 f(2) = 6
$$

---

<!-- Page 50 -->

#### 7.3 Calculation of $f(2.3)$

Substituting into the Newton-Gregory forward formula:

$$
\begin{aligned}
f(a + u h) &= f(a) + u \Delta f(a) + \frac{u(u-1)}{2!} \Delta^2 f(a) + \frac{u(u-1)(u-2)}{3!} \Delta^3 f(a) \\
f(2 + 0.3 \times 1) &= f(2) + 0.3 \Delta f(2) + \frac{(0.3)(0.3-1)}{2!} \Delta^2 f(2) + \frac{(0.3)(0.3-1)(0.3-2)}{3!} \Delta^3 f(2) \\
&= 17 + 0.3(29) + \frac{(0.3)(-0.7)}{2}(22) + \frac{(0.3)(-0.7)(-1.7)}{6}(6) \\
&= 17 + 8.7 + (-0.105)(22) + (0.357)(1) \\
&= 17 + 8.7 - 2.31 + 0.357 \\
&= 23.747
\end{aligned}
$$

$$
\mathbf{f(2.3) = 23.747 \quad (\text{Ans})}
$$

---

### 8. Newton's Backward Interpolation

The **Newton-Gregory Backward Interpolation Formula** approximates $f(x)$ when the query point lies near the end of a tabulated data sequence:

$$
f(a + n h + u h) = f(a + n h) + u \nabla f(a + n h) + \frac{u(u+1)}{2!} \nabla^2 f(a + n h) + \frac{u(u+1)(u+2)}{3!} \nabla^3 f(a + n h) + \dots
$$

Where:
- $a + n h = x_n$ is the last base point in the table.
- $u = \frac{x - x_n}{h}$ (typically negative, between $-1$ and $0$).

---

#### 8.1 Problem Statement

> **Problem (Page 50):**  
> Given the data:
> 
> | $x$ | $1$ | $2$ | $3$ | $4$ | $5$ | $6$ | $7$ | $8$ |
> | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
> | $f(x)$ | $1$ | $8$ | $27$ | $64$ | $125$ | $216$ | $343$ | $512$ |
> 
> Find the value of $f(7.5)$.

*(Observation: The tabulated data represents the cubic function $f(x) = x^3$.)*

---

#### 8.2 Backward Difference Table Construction

Step size $h = 1$. The query point $x = 7.5$ lies near the final entry $x_n = 8$.

| $x$ | $f(x)$ | $\nabla f(x)$ | $\nabla^2 f(x)$ | $\nabla^3 f(x)$ |
| :---: | :---: | :---: | :---: | :---: |
| $1$ | $1$ | | | |
| $2$ | $8$ | $7$ | | |
| $3$ | $27$ | $19$ | $12$ | |
| $4$ | $64$ | $37$ | $18$ | $6$ |
| $5$ | $125$ | $61$ | $24$ | $6$ |
| $6$ | $216$ | $91$ | $30$ | $6$ |
| $7$ | $343$ | $127$ | $36$ | $6$ |
| **8** | **512** | **169** | **42** | **6** |

Bottom diagonal values originating at $x_n = 8$:

$$
\begin{aligned}
f(8) &= 512 \\
\nabla f(8) &= 169 \\
\nabla^2 f(8) &= 42 \\
\nabla^3 f(8) &= 6
\end{aligned}
$$

---

<!-- Page 51 -->

#### 8.3 Calculation of $f(7.5)$

Parameters:

$$
\begin{aligned}
a + n h &= 8 \\
x &= 7.5 \\
h &= 1 \\
u &= \frac{x - (a + n h)}{h} = \frac{7.5 - 8}{1} = -0.5
\end{aligned}
$$

Substituting into the backward formula:

$$
\begin{aligned}
f(a + n h + u h) &= f(a + n h) + u \nabla f(a + n h) + \frac{u(u+1)}{2!} \nabla^2 f(a + n h) + \frac{u(u+1)(u+2)}{3!} \nabla^3 f(a + n h) \\
f(8 + (-0.5) \cdot 1) &= f(8) + (-0.5) \nabla f(8) + \frac{(-0.5)(-0.5 + 1)}{2!} \nabla^2 f(8) + \frac{(-0.5)(-0.5 + 1)(-0.5 + 2)}{3!} \nabla^3 f(8) \\
&= 512 + (-0.5)(169) + \frac{(-0.5)(0.5)}{2} (42) + \frac{(-0.5)(0.5)(1.5)}{6} (6) \\
&= 512 - 84.5 + (-0.125)(42) + (-0.375)(1) \\
&= 512 - 84.5 - 5.25 - 0.375 \\
&= 421.875
\end{aligned}
$$

$$
\mathbf{f(7.5) = 421.875 \quad (\text{Ans})}
$$

> [!note] Verification
> Since $f(x) = x^3$, the exact value is $(7.5)^3 = \left(\frac{15}{2}\right)^3 = \frac{3375}{8} = 421.875$.  
> Because third-degree polynomial data has zero fourth and higher differences, Newton's backward interpolation reproduces the exact analytical value.

---

<!-- Page 52 -->

### 9. Central Differences & Gauss's Forward Interpolation Formula

When the target value $x$ is situated near the **center (middle)** of a table, using forward or backward interpolation leads to asymmetric truncated polynomials with larger error terms. **Central difference formulas** (Gauss, Stirling, Bessel) provide rapid convergence and symmetric error distribution.

> [!tip] Pedagogical Guidance: Central Interpolation Criterion
> **Author's Annotation (Page 52):**  
> `[ মাঝের value বের করতে → ]`  
> **Translation & Explanation:**  
> *"When finding / evaluating a value located near the middle (center) of the table $\to$ use central difference formulas."*

---

#### 9.1 Gauss's Forward Interpolation Formula

Taking $x_0$ as the central base origin, with $u = \frac{x - x_0}{h}$ satisfying $0 \le u \le 1$:

$$
\begin{aligned}
y_u &= y_0 + u \Delta y_0 + \frac{u(u-1)}{2!} \Delta^2 y_{-1} + \frac{(u+1)u(u-1)}{3!} \Delta^3 y_{-1} \\
&\quad + \frac{(u+1)u(u-1)(u-2)}{4!} \Delta^4 y_{-2} + \frac{(u+2)(u+1)u(u-1)(u-2)}{5!} \Delta^5 y_{-2} + \dots
\end{aligned}
$$

The path through the difference table follows a characteristic **zigzag** line:  
$y_0 \to \Delta y_0 \to \Delta^2 y_{-1} \to \Delta^3 y_{-1} \to \Delta^4 y_{-2} \to \Delta^5 y_{-2}$.

---

#### 9.2 Problem Statement

> **Problem (Page 52):**  
> Use Gauss's forward interpolation formula to find the value of $y$ when $x = 3.75$ from the following table:
> 
> | $x$ | $2.5$ | $3.0$ | $3.5$ | $4.0$ | $4.5$ | $5.0$ |
> | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
> | $f(x)$ | $24.145$ | $22.043$ | $20.225$ | $18.644$ | $17.262$ | $16.047$ |

---

#### 9.3 Central Difference Table Construction

Since $x = 3.75$ lies between $3.5$ and $4.0$, we choose the central base origin as:

$$
x_0 = 3.5, \quad h = 0.5
$$

Then $u = \frac{3.75 - 3.5}{0.5} = \frac{0.25}{0.5} = 0.5$ (perfectly within $0 < u < 1$).

We index the grid points symmetrically around $x_0$:

| $i$ | $x_i$ | $y_i$ | $\Delta y$ | $\Delta^2 y$ | $\Delta^3 y$ | $\Delta^4 y$ | $\Delta^5 y$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| $-2$ | $2.5$ | $24.145$ | | | | | |
| | | | $-2.102$ ($\Delta y_{-2}$) | | | | |
| $-1$ | $3.0$ | $22.043$ | | $0.284$ ($\Delta^2 y_{-2}$) | | | |
| | | | $-1.818$ ($\Delta y_{-1}$) | | $-0.047$ ($\Delta^3 y_{-2}$) | | |
| **0** | **3.5** | **20.225** ($y_0$) | | **0.237** ($\Delta^2 y_{-1}$) | | **0.009** ($\Delta^4 y_{-2}$) | |
| | | | **$-1.581$** ($\Delta y_0$) | | **$-0.038$** ($\Delta^3 y_{-1}$) | | **$-0.003$** ($\Delta^5 y_{-2}$) |
| $1$ | $4.0$ | $18.644$ | | $0.199$ ($\Delta^2 y_0$) | | $0.006$ ($\Delta^4 y_{-1}$) | |
| | | | $-1.382$ ($\Delta y_1$) | | $-0.032$ ($\Delta^3 y_0$) | | |
| $2$ | $4.5$ | $17.262$ | | $0.167$ ($\Delta^2 y_1$) | | | |
| | | | $-1.215$ ($\Delta y_2$) | | | | |
| $3$ | $5.0$ | $16.047$ | | | | | |

##### Coefficients Along the Gauss Forward Zigzag Trajectory:

$$
\begin{aligned}
y_0 &= 20.225 \\
\Delta y_0 &= -1.581 \\
\Delta^2 y_{-1} &= 0.237 \\
\Delta^3 y_{-1} &= -0.038 \\
\Delta^4 y_{-2} &= 0.009 \\
\Delta^5 y_{-2} &= -0.003
\end{aligned}
$$

*(Note: The full numerical substitution and evaluation for $y(3.75) \approx 19.4076$ concludes seamlessly on Page 53 at the start of Batch 4).*

---

## 10. Summary Comparison of Batch 3 Numerical Methods

| Category | Method | Formulation / Recurrence | Order of Local Truncation Error | Primary Strengths / When to Use |
| :--- | :--- | :--- | :---: | :--- |
| **ODE Solver** | **Euler's Method** | $y_{n+1} = y_n + h f(x_n, y_n)$ | $\mathcal{O}(h^2)$ local, $\mathcal{O}(h)$ global | Conceptually simple; poor accuracy for large $h$. |
| **ODE Solver** | **Modified Euler** | $y_{n+1} = y_n + \frac{h}{2}[f_n + f_{n+1}^{(k-1)}]$ | $\mathcal{O}(h^3)$ local, $\mathcal{O}(h^2)$ global | Predictor-corrector eliminates 1st-order error iteratively. |
| **ODE Solver** | **Taylor Series** | $y_{n+1} = y_n + h y_n' + \frac{h^2}{2!} y_n'' + \dots$ | Truncated at $p$-th derivative $\mathcal{O}(h^{p+1})$ | Extremely accurate when symbolic derivatives are accessible. |
| **ODE Solver** | **Runge-Kutta 4th** | $y_{n+1} = y_n + \frac{1}{6}(K_1 + 2K_2 + 2K_3 + K_4)$ | $\mathcal{O}(h^5)$ local, $\mathcal{O}(h^4)$ global | Standard benchmark solver; 4th-order accuracy without analytical derivatives. |
| **Interpolation** | **Newton Forward** | $f(x_0 + uh) = y_0 + u \Delta y_0 + \frac{u(u-1)}{2!} \Delta^2 y_0 + \dots$ | Polynomial degree $n$ | Interpolation near the start/top of an equispaced table ($0 < u < 1$). |
| **Interpolation** | **Newton Backward** | $f(x_n + uh) = y_n + u \nabla y_n + \frac{u(u+1)}{2!} \nabla^2 y_n + \dots$ | Polynomial degree $n$ | Interpolation near the end/bottom of an equispaced table ($-1 < u < 0$). |
| **Interpolation** | **Gauss Forward** | $y_u = y_0 + u \Delta y_0 + \frac{u(u-1)}{2!} \Delta^2 y_{-1} + \dots$ | Central difference polynomial | Interpolation near the center of an equispaced table ($0 < u < 1$). |
