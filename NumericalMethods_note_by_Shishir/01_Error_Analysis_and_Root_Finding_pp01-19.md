---
title: "Error Analysis, Finite Differences, and Root Finding (Pages 01–19)"
course: "ECE 2213 — Numerical Analysis / Numerical Methods"
author: "Shishir (Roll 2310002)"
batch: "Batch 1 (Pages 01–19)"
source: "Numerical Analysis By Shishir 2310002.pdf"
tags:
  - numerical-methods
  - ece2213
  - error-analysis
  - finite-differences
  - bisection-method
  - regula-falsi
  - secant-method
---

# Error Analysis and Root Finding

<!-- Page 1 -->

## 1. Error Analysis Fundamentals

Numerical error is the difference between the exact (analytical) solution and the approximate solution:

$$
\text{Numerical Error} = \text{Exact Solution} - \text{Approximate Solution}
$$

### 1.1 Inherent Error

**Definition:** Inherent error exists in the problem formulation itself, arising either from:
1. Approximations in the given input data (measurements, experimental data).
2. Physical or technological limitations of computing aids (e.g., mathematical tables, desk calculators, hardware precision).

**Mitigation:** Such errors can be minimized by obtaining higher-quality, more accurate input data and utilizing high-precision computational equipment.

### 1.2 Round-Off Error

**Definition:** Round-off errors occur due to rounding off numbers during computation to a fixed number of significant digits or decimal places.

**Example:**
Suppose a calculated quantity is rounded:

$$
1.24372 \approx 1.244
$$

The round-off error is given by:

$$
\text{Error} = 1.244 - 1.24372 = 0.00028
$$

---

<!-- Page 2 -->

### 1.3 Chopping (Truncating)

**Definition:** In chopping, extra digits beyond a fixed limit are simply dropped without rounding. This process is also called **truncating the number**.

For instance, a number like $11.25694$ stored to 4 digits (or 2 decimal places) will simply be retained as $11.25$.

**Illustrative Examples:**

| Exact Number | Chopped to 4 Digits | Chopping Error ($\text{Exact} - \text{Chopped}$) |
| :--- | :--- | :--- |
| $546.25$ | $546.2$ | $546.25 - 546.2 = 0.05$ |
| $846.7589$ | $846.7$ | $846.7589 - 846.7 = 0.0589$ |

### 1.4 Truncation Error

**Definition:** Truncation error arises due to truncating an infinite mathematical series after a finite number of approximate terms.

**Example (Maclaurin / Taylor Series Expansion):**
Consider the exponential series:

$$
e^x = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \dots
$$

The actual analytical value of $e^x$ at $x = 1$ is:

$$
e^1 = 2.71828\dots
$$

If we approximate the series by taking only the first two terms ($e_a$):

$$
e_a = 1 + x = 1 + 1 = 2
$$

Then the truncation error is:

$$
\text{Truncation Error} = 2.71828 - 2 = 0.71828
$$

---

<!-- Page 3 -->

## 2. Definitions of Error Metrics & General Error Formula

### 2.1 Absolute Error

**Absolute error ($E_A$)** is the positive difference between the true/actual value and the approximate value:

$$
E_A = |x - x_1| = \delta x
$$

*(where $x$ is the true value and $x_1$ is the approximate value)*

### 2.2 Relative Error

**Relative error ($E_R$)** is the ratio of the absolute error to the true/actual value:

$$
E_R = \frac{E_A}{x}
$$

### 2.3 Percentage Error

**Percentage error ($E_P$)** is the relative error expressed as a percentage:

$$
E_P = 100 \times E_R = \frac{E_A}{x} \times 100\%
$$

### 2.4 A General Error Formula

Let $u = f(x_1, x_2, \dots, x_n)$ be a multivariable differentiable function of independent variables $x_1, x_2, \dots, x_n$.

By total differential expansion, the propagation of error $\Delta u$ in $u$ due to errors $\Delta x_1, \Delta x_2, \dots, \Delta x_n$ is:

$$
\Delta u = \frac{\partial u}{\partial x_1}\Delta x_1 + \frac{\partial u}{\partial x_2}\Delta x_2 + \dots + \frac{\partial u}{\partial x_n}\Delta x_n
$$

The formula for the relative error $E_R$ is:

$$
E_R = \frac{\Delta u}{u}
$$

---

<!-- Page 4 -->

### 2.5 Worked Example: Relative Maximum Error of a Multivariable Function

**Problem:**
Find the relative maximum error in the function:

$$
u = \frac{7xy}{z^3}
$$

where $\Delta x = \Delta y = \Delta z = 0.001$ and $x = y = z = 1$.

**Solution:**
Given:

$$
u = \frac{7xy}{z^3}
$$

Taking the natural logarithm on both sides:

$$
\log u = \log\left(\frac{7xy}{z^3}\right)
$$

$$
\implies \log u = \log 7 + \log x + \log y - 3\log z
$$

Taking differentials on both sides:

$$
\implies \frac{\delta u}{u} = 0 + \frac{\delta x}{x} + \frac{\delta y}{y} - \frac{3\delta z}{z}
$$

> [!note] Pedagogical Rule: Maximum (Worst-Case) Error
> *Original handwritten note:* `maximum error তাই modulous ->`
> *Translation:* To find the **maximum error**, we take the modulus (absolute value) of each individual contribution so that errors add constructively in the worst-case scenario:

$$
\left|\frac{\delta u}{u}\right| = \left|\frac{\delta x}{x}\right| + \left|\frac{\delta y}{y}\right| + 3\left|\frac{\delta z}{z}\right|
$$

Substituting the given values $x = y = z = 1$ and $\delta x = \delta y = \delta z = 0.001$:

$$
\left|\frac{\delta u}{u}\right| = \left|\frac{0.001}{1}\right| + \left|\frac{0.001}{1}\right| + 3\left|\frac{0.001}{1}\right|
$$

$$
= 0.001 + 0.001 + 0.003
$$

$$
= 0.005
$$

Thus, the maximum relative error is **$0.005$**.

---

<!-- Page 5 -->

## 3. Truncation Error in Interpolation

### 3.1 Truncation Error for Lagrange's General Interpolation Formula

For an $n$-th degree Lagrange interpolating polynomial matching $f(x)$ at $n+1$ distinct points $x_0, x_1, \dots, x_n$, the truncation error is given by:

$$
E_n(f; x) = \frac{1}{(n+1)!} (x - x_0)(x - x_1)\dots(x - x_n) f^{(n+1)}(\xi)
$$

where $\xi \in (\min(x_i, x), \max(x_i, x))$.

#### Special Cases:
1. **Linear Interpolation Formula ($n = 1$):**
   $$
   E_1(f; x) = \frac{1}{2!} (x - x_0)(x - x_1) f''(\xi)
   $$

2. **Quadratic Interpolation Formula ($n = 2$):**
   $$
   E_2(f; x) = \frac{1}{3!} (x - x_0)(x - x_1)(x - x_2) f'''(\xi)
   $$

### 3.2 Example Problem Statement

**Problem:**
Determine the step size that can be used in the tabulation of $f(x) = \sin x$ in the interval $[0, \pi/4]$ at equally spaced nodal points so that the truncation error of the quadratic interpolation is less than $5 \times 10^{-8}$.

> [!note] Analytical Solution
> *(Left as an unsolved exercise in the handwritten lecture notes on Page 5; analytical solution provided below for completeness).*
> 
> 1. **Truncation error formula ($n = 2$):**
>    $$
>    |E_2(f; x)| = \frac{|(x - x_0)(x - x_1)(x - x_2)|}{3!} |f'''(\xi)|
>    $$
>    where $\xi \in [x_0, x_2] \subseteq [0, \pi/4]$.
> 
> 2. **Third derivative bound:**
>    $$
>    f(x) = \sin x \implies f'(x) = \cos x \implies f''(x) = -\sin x \implies f'''(x) = -\cos x
>    $$
>    On $[0, \pi/4]$, $|f'''(\xi)| = |-\cos \xi| \le 1$.
> 
> 3. **Node polynomial bound for equispaced nodes ($x_1 - x_0 = x_2 - x_1 = h$):**
>    Let $t = x - x_1 \in [-h, h]$. Then:
>    $$
>    |(x - x_0)(x - x_1)(x - x_2)| = |(t + h)t(t - h)| = |t(t^2 - h^2)|
>    $$
>    Maximizing over $[-h, h]$ yields the stationary point at $t = \frac{h}{\sqrt{3}}$, giving:
>    $$
>    \max_{x \in [x_0, x_2]} |(x - x_0)(x - x_1)(x - x_2)| = \frac{2h^3}{3\sqrt{3}}
>    $$
> 
> 4. **Setting up the error bound:**
>    $$
>    |E_2(f; x)| \le \frac{1}{6} \left(\frac{2h^3}{3\sqrt{3}}\right)(1) = \frac{h^3}{9\sqrt{3}} < 5 \times 10^{-8}
>    $$
>    $$
>    h^3 < 45\sqrt{3} \times 10^{-8} \approx 7.7942 \times 10^{-7} \implies h < 0.0092
>    $$
> 
> **Conclusion:** A step size $h \le 0.0092$ ensures that the quadratic interpolation truncation error remains below $5 \times 10^{-8}$.

---

<!-- Page 6 -->

## 4. Error Propagation in Physical and Mathematical Calculations

### 4.1 Relative Error in Sum of Two Quantities

**Question:**
If $\Delta x = 0.005$ and $\Delta y = 0.001$ are the absolute errors in $x = 2.11$ and $y = 4.15$, find the relative error in the computation of $x + y$.

**Solution:**
Let:

$$
z = x + y
$$

Taking logarithms:

$$
\log z = \log(x + y)
$$

Differentiating:

$$
\frac{\delta z}{z} = \frac{\delta x + \delta y}{x + y}
$$

Substituting the given values:

$$
\frac{\delta z}{z} = \frac{0.005 + 0.001}{2.11 + 4.15} = \frac{0.006}{6.26} \approx 0.0009
$$

*(Exact value: $\frac{0.006}{6.26} = 0.0009585\dots \approx 0.0009$ as recorded in the class notes).*

---

### 4.2 Percentage Error in Simple Pendulum Period

**Question:**
The period of a simple pendulum is given by:

$$
T = 2\pi \sqrt{\frac{l}{g}}
$$

Find the maximum percentage error in $T$ due to possible errors up to $1\%$ in $l$ and $2.5\%$ in $g$.

**Answer:**
Given percentage errors:

$$
\frac{\delta l}{l} \times 100 = 1\%, \quad \frac{\delta g}{g} \times 100 = 2.5\%
$$

Starting from the period relation:

$$
T = 2\pi \sqrt{\frac{l}{g}}
$$

Taking logarithms on both sides:

$$
\log T = \log\left(2\pi \sqrt{\frac{l}{g}}\right)
$$

$$
\implies \log T = \log 2\pi + \log \sqrt{l} - \log \sqrt{g}
$$

---

<!-- Page 7 -->

*(Simple Pendulum continued)*

$$
\implies \log T = \log 2\pi + \frac{1}{2}\log l - \frac{1}{2}\log g
$$

Differentiating:

$$
\implies \frac{\delta T}{T} = 0 + \frac{1}{2}\frac{\delta l}{l} - \frac{1}{2}\frac{\delta g}{g}
$$

Taking the maximum (worst-case) relative error by taking absolute values:

$$
\implies \left|\frac{\delta T}{T}\right| = \frac{1}{2}\left|\frac{\delta l}{l}\right| + \frac{1}{2}\left|\frac{\delta g}{g}\right|
$$

Multiplying by $100$ to obtain percentage errors:

$$
\implies \frac{\delta T}{T} \times 100 = \frac{1}{2}\left(\left|\frac{\delta l}{l}\right| \times 100\right) + \frac{1}{2}\left(\left|\frac{\delta g}{g}\right| \times 100\right)
$$

$$
\implies \frac{\delta T}{T} \times 100 = \frac{1}{2}(1 + 2.5) = \frac{3.5}{2}
$$

$$
\implies \frac{\delta T}{T} \times 100 = 1.75\% \quad \longrightarrow \text{Percentage Error}
$$

The maximum percentage error in $T$ is **$1.75\%$**.

---

### 4.3 Percentage Change in the Volume of a Composite Balloon

**Question:**
A balloon is in the form of a right circular cylinder of radius $1.5\text{ m}$ and length $4\text{ m}$, and is surmounted by hemispherical ends. If the radius is increased by $0.01\text{ m}$ and length by $0.05\text{ m}$, find the percentage change in the volume of the balloon.

---

<!-- Page 8 -->

*(Balloon Volume continued)*

**Answer:**
Given:
- Radius $r = 1.5\text{ m}$, $\delta r = 0.01\text{ m}$
- Length/height $h = 4\text{ m}$, $\delta h = 0.05\text{ m}$

The total volume $V$ of the balloon consists of the cylinder plus two hemispherical ends (forming one full sphere of radius $r$):

$$
V = \pi r^2 h + \frac{4}{3}\pi r^3
$$

Taking logarithms:

$$
\log V = \log\left(\pi r^2 h + \frac{4}{3}\pi r^3\right)
$$

Differentiating both sides:

$$
\implies \frac{\delta V}{V} = \frac{2\pi r h\,\delta r + \pi r^2\,\delta h + \frac{4}{3}\pi \cdot 3r^2\,\delta r}{\pi r^2 h + \frac{4}{3}\pi r^3}
$$

Factoring out $\pi r$ from numerator and denominator:

$$
\implies \frac{\delta V}{V} = \frac{\pi r \left[2h\,\delta r + r\,\delta h + 4r\,\delta r\right]}{\pi r \left[rh + \frac{4}{3}r^2\right]} = \frac{2h\,\delta r + r\,\delta h + 4r\,\delta r}{rh + \frac{4}{3}r^2}
$$

Multiplying by $100$ for percentage change:

$$
\frac{\delta V}{V} \times 100 = \left[\frac{2(4)(0.01) + 1.5(0.05) + 4(1.5)(0.01)}{(1.5)(4) + \frac{4}{3}(1.5)^2}\right] \times 100\%
$$

Evaluating terms:
- Numerator: $2(4)(0.01) + 1.5(0.05) + 4(1.5)(0.01) = 0.08 + 0.075 + 0.06 = 0.215$
- Denominator: $6 + \frac{4}{3}(2.25) = 6 + 3 = 9$

$$
\frac{\delta V}{V} \times 100 = \frac{0.215}{9} \times 100\% \approx 2.39\%
$$

The percentage change in the volume of the balloon is **$2.39\%$**.

---

<!-- Page 9 -->

## 5. Numerical Operators and Their Relations

### 5.1 Forward Difference Operator ($\Delta$)

Let $y = f(x)$ be a given function where the independent variable (argument) $x$ takes equidistant values:

$$
x_0 = a, \quad x_1 = a+h, \quad x_2 = a+2h, \quad \dots, \quad x_n = a+nh
$$

with step length $h$, and $f(a), f(a+h), f(a+2h), \dots, f(a+nh)$ are the corresponding function values at these points.

The **first forward differences** are defined by:

$$
\Delta f(a) = f(a+h) - f(a)
$$

$$
\Delta f(a+h) = f(a+2h) - f(a+h)
$$

$$
\Delta f(a+2h) = f(a+3h) - f(a+2h)
$$

In general:

$$
\Delta f(x) = f(x+h) - f(x)
$$

### 5.2 Higher Order Forward Differences

The **second forward difference** is defined as the forward difference of the first forward difference:

$$
\Delta^2 f(x) = \Delta(\Delta f(x)) = \Delta f(x+h) - \Delta f(x)
$$

Expanding using the definition:

$$
\Delta^2 f(x) = \left[f(x+2h) - f(x+h)\right] - \left[f(x+h) - f(x)\right]
$$

$$
= f(x+2h) - 2f(x+h) + f(x)
$$

> [!important] Crucial Distinction on Operator Notation
> **Note:** $\Delta^2$ is **not** the arithmetic square of the operator $\Delta$ (i.e., $\Delta^2 \neq \Delta \times \Delta$). Rather, $\Delta^2$ denotes the operator $\Delta$ applied twice successively:
> 
> $$
> \Delta^2 = \Delta \circ \Delta
> $$

---

<!-- Page 10 -->

## 6. Root Finding: Bisection Method

### 6.1 Problem Statement
**Problem:**
Find the real root of the equation $x^3 - x - 4 = 0$ using the **Bisection Method**, correct to three places of decimal.

### 6.2 Initial Interval Isolation
Let:

$$
f(x) = x^3 - x - 4
$$

Evaluating at integer points:
- $f(0) = 0^3 - 0 - 4 = -4$
- $f(1) = 1^3 - 1 - 4 = -4 \quad (< 0 \text{, negative})$
- $f(2) = 2^3 - 2 - 4 = 8 - 6 = 2 \quad (> 0 \text{, positive})$

Since $f(1)$ and $f(2)$ are of opposite signs ($f(1) \cdot f(2) < 0$):
$\therefore$ By the Intermediate Value Theorem, a real root lies in the interval $(1, 2)$.

### 6.3 Iterative Steps

#### First Approximation ($x_1$):
Taking the midpoint of $1^{(-)}$ and $2^{(+)}$:

$$
x_1 = \frac{1 + 2}{2} = \frac{3}{2} = 1.5
$$

Evaluating the function:

$$
f(1.5) = (1.5)^3 - 1.5 - 4 = 3.375 - 1.5 - 4 = -2.125 \quad (< 0 \text{, negative})
$$

Since $f(1.5)$ is negative and $f(2)$ is positive:
$\therefore$ The root lies between **$1.5$** and **$2$**.

---

<!-- Page 11 -->

#### Second Approximation ($x_2$):
Taking the midpoint of $1.5^{(-)}$ and $2^{(+)}$:

$$
x_2 = \frac{1.5 + 2}{2} = \frac{3.5}{2} = 1.75
$$

Evaluating the function:

$$
f(1.75) = (1.75)^3 - 1.75 - 4 = 5.359375 - 1.75 - 4 = -0.3906 \quad (< 0 \text{, negative})
$$

Since $f(1.75)$ and $f(2)$ are of opposite signs:
$\therefore$ The root lies between **$1.75$** and **$2$**.

#### Third Approximation ($x_3$):
Taking the midpoint of $1.75^{(-)}$ and $2^{(+)}$:

$$
x_3 = \frac{1.75 + 2}{2} = 1.875
$$

Evaluating the function:

$$
f(1.875) = (1.875)^3 - 1.875 - 4 = 6.591797 - 1.875 - 4 = 0.7168 \quad (> 0 \text{, positive})
$$

Since $f(1.75)$ is negative and $f(1.875)$ is positive:
$\therefore$ The root lies between **$1.75$** and **$1.875$**.

#### Fourth Approximation ($x_4$):
Taking the midpoint of $1.75^{(-)}$ and $1.875^{(+)}$:

$$
x_4 = \frac{1.75 + 1.875}{2} = 1.8125
$$

Evaluating the function:

$$
f(1.8125) = (1.8125)^3 - 1.8125 - 4 = 5.954346 - 1.8125 - 4 = 0.1418 \quad (> 0 \text{, positive})
$$

Since $f(1.75)$ is negative and $f(1.8125)$ is positive:
$\therefore$ The root lies between **$1.75$** and **$1.8125$**.

---

<!-- Page 12 -->

#### Fifth Approximation ($x_5$):
Taking the midpoint of $1.75^{(-)}$ and $1.8125^{(+)}$:

$$
x_5 = \frac{1.75 + 1.8125}{2} = 1.7813 \quad (\approx 1.78125)
$$

Evaluating the function:

$$
f(1.7813) = (1.7813)^3 - 1.7813 - 4 = -0.1292 \quad (< 0 \text{, negative})
$$

Since $f(1.7813)$ is negative and $f(1.8125)$ is positive:
$\therefore$ The root lies between **$1.7813$** and **$1.8125$**.

#### Sixth Approximation ($x_6$):
Taking the midpoint of $1.7813^{(-)}$ and $1.8125^{(+)}$:

$$
x_6 = \frac{1.7813 + 1.8125}{2} = 1.7969
$$

Evaluating the function:

$$
f(1.7969) = (1.7969)^3 - 1.7969 - 4 = 0.0050 \quad (> 0 \text{, positive})
$$

Since $f(1.7813)$ is negative and $f(1.7969)$ is positive:
$\therefore$ The root lies between **$1.7813$** and **$1.7969$**.

#### Seventh Approximation ($x_7$):
Taking the midpoint of $1.7813^{(-)}$ and $1.7969^{(+)}$:

$$
x_7 = \frac{1.7813 + 1.7969}{2} = 1.7891
$$

Evaluating the function:

$$
f(1.7891) = (1.7891)^3 - 1.7891 - 4 = -0.0624 \quad (< 0 \text{, negative})
$$

Since $f(1.7891)$ is negative and $f(1.7969)$ is positive:
$\therefore$ The root lies between **$1.7891$** and **$1.7969$**.

---

<!-- Page 13 -->

#### Eighth Approximation ($x_8$):
Taking the midpoint of $1.7891^{(-)}$ and $1.7969^{(+)}$:

$$
x_8 = \frac{1.7891 + 1.7969}{2} = 1.7930
$$

Evaluating the function:

$$
f(1.7930) = (1.7930)^3 - 1.7930 - 4 = -0.0288 \quad (< 0 \text{, negative})
$$

Since $f(1.7930)$ is negative and $f(1.7969)$ is positive:
$\therefore$ The root lies between **$1.7930$** and **$1.7969$**.

#### Ninth Approximation ($x_9$):
Taking the midpoint of $1.7930^{(-)}$ and $1.7969^{(+)}$:

$$
x_9 = \frac{1.7930 + 1.7969}{2} = 1.7950
$$

Evaluating the function:

$$
f(1.7950) = (1.7950)^3 - 1.7950 - 4 = -0.0115 \quad (< 0 \text{, negative})
$$

Since $f(1.7950)$ is negative and $f(1.7969)$ is positive:
$\therefore$ The root lies between **$1.7950$** and **$1.7969$**.

#### Tenth Approximation ($x_{10}$):
Taking the midpoint of $1.7950$ and $1.7969$:

$$
x_{10} = \frac{1.7950 + 1.7969}{2} = 1.79595 \approx 1.7960
$$

Rounding to three decimal places:

$$
\mathbf{x \approx 1.796}
$$

**Conclusion:** The required root correct to three decimal places is **$1.796$**.

---

<!-- Page 14 -->

## 7. Root Finding: Regula Falsi Method (Method of False Position)

### 7.1 Problem Statement
**Problem:**
Find the real root of the equation $x^4 - x - 10 = 0$ using the **Regula Falsi Method**, correct to three decimal places.

### 7.2 Initial Interval Isolation
Let:

$$
f(x) = x^4 - x - 10
$$

Evaluating:
- $f(0) = 0 - 0 - 10 = -10$
- $f(1) = 1^4 - 1 - 10 = -10 \quad (< 0 \text{, negative})$
- $f(2) = 2^4 - 2 - 10 = 16 - 12 = 4 \quad (> 0 \text{, positive})$

Since $f(1)$ and $f(2)$ have opposite signs:
$\therefore$ A real root lies in the interval $(1, 2)$.

Let initial bracketing points be:

$$
x_0^{(-)} = 1, \quad x_1^{(+)} = 2
$$

### 7.3 General Regula Falsi Formula

The false position formula connecting $(x_0, f(x_0))$ and $(x_1, f(x_1))$ is:

$$
x^{(1)} = x_0 - \frac{x_1 - x_0}{f(x_1) - f(x_0)} f(x_0)
$$

### 7.4 First Approximation ($x^{(1)}$)

$$
x^{(1)} = 1 - \frac{2 - 1}{4 - (-10)} \times (-10)
$$

$$
= 1 - \frac{1}{4 + 10} \times (-10) = 1 + \frac{10}{14} = 1 + 0.71428\dots
$$

$$
= 1.7143
$$

---

<!-- Page 15 -->

### 7.5 Second Approximation ($x^{(2)}$)
Evaluate $f(x)$ at $x^{(1)} = 1.7143$:

$$
f(1.7143) = (1.7143)^4 - 1.7143 - 10 = 8.6367 - 1.7143 - 10 = -3.0776 \quad (< 0 \text{, negative})
$$

Since $f(1.7143) < 0$ and $f(2) > 0$, the root lies between **$1.7143$** and **$2$**.
Set $x_0^{(-)} = 1.7143$ and $x_1^{(+)} = 2$:

$$
x^{(2)} = x_0 - \frac{x_1 - x_0}{f(x_1) - f(x_0)} f(x_0)
$$

$$
= 1.7143 - \frac{2 - 1.7143}{4 - (-3.0776)} \times (-3.0776)
$$

$$
= 1.7143 - \frac{0.2857}{4 + 3.0776} \times (-3.0776) = 1.7143 + \frac{0.2857 \times 3.0776}{7.0776}
$$

$$
= 1.8385
$$

Evaluate $f(x)$ at $x^{(2)} = 1.8385$:

$$
f(1.8385) = (1.8385)^4 - 1.8385 - 10 = -0.4135 \quad (< 0 \text{, negative})
$$

### 7.6 Third Approximation ($x^{(3)}$)
Root lies between **$1.8385$** and **$2$**. Set $x_0^{(-)} = 1.8385$ and $x_1^{(+)} = 2$:

$$
x^{(3)} = x_0 - \frac{x_1 - x_0}{f(x_1) - f(x_0)} f(x_0)
$$

$$
= 1.8385 - \frac{2 - 1.8385}{4 - (-0.4135)} \times (-0.4135)
$$

$$
= 1.8536
$$

Evaluate $f(x)$ at $x^{(3)} = 1.8536$:

$$
f(1.8536) = (1.8536)^4 - 1.8536 - 10 = -0.0486 \quad (< 0 \text{, negative})
$$

---

<!-- Page 16 -->

### 7.7 Fourth Approximation ($x^{(4)}$)
Root lies between **$1.8536$** and **$2$**. Set $x_0^{(-)} = 1.8536$ and $x_1^{(+)} = 2$:

$$
x^{(4)} = 1.8536 - \frac{2 - 1.8536}{4 - (-0.0486)} \times (-0.0486)
$$

$$
= 1.8554
$$

Evaluate $f(x)$ at $x^{(4)} = 1.8554$:

$$
f(1.8554) = (1.8554)^4 - 1.8554 - 10 = -0.0045 \quad (< 0 \text{, negative})
$$

Root lies between **$1.8554$** and **$2$**.

### 7.8 Fifth Approximation ($x^{(5)}$)
Set $x_0^{(-)} = 1.8554$ and $x_1^{(+)} = 2$:

$$
x^{(5)} = 1.8554 - \frac{2 - 1.8554}{4 - (-0.0045)} \times (-0.0045)
$$

$$
= 1.8556
$$

Rounding to three decimal places:

$$
\mathbf{x \approx 1.856}
$$

> [!tip] Pedagogical Guidance: Termination Criterion
> *Original handwritten note:* `[ 5 টা Approximation নেব ]`
> *Translation:* "We will take 5 approximations." In this problem, 5 iterations are performed until two successive approximations ($x^{(4)} = 1.8554$ and $x^{(5)} = 1.8556$) both round to **$1.856$**, confirming stability to three decimal places.

---

<!-- Page 17 -->

## 8. Root Finding: Secant Method

### 8.1 Problem Statement
**Problem:**
Find the real root of the equation $x^4 - x - 10 = 0$ using the **Secant Method**.

### 8.2 Initial Points Selection
Let:

$$
f(x) = x^4 - x - 10
$$

Evaluating at integer points:
- $f(0) = -10$
- $f(1) = 1 - 1 - 10 = -10 \quad (< 0 \text{, negative})$
- $f(2) = 16 - 2 - 10 = 4 \quad (> 0 \text{, positive})$

Since $f(1)$ and $f(2)$ are of opposite signs, a real root lies between $1$ and $2$.
Choose the two initial starting estimates:

$$
x_0 = 1, \quad x_1 = 2
$$

With corresponding function values:

$$
f(x_0) = -10, \quad f(x_1) = 4
$$

### 8.3 General Secant Recurrence Formula

The Secant recurrence relation uses the two most recent iterates without requiring them to bracket the root:

$$
x_{n+1} = x_{n-1} - \frac{x_n - x_{n-1}}{f(x_n) - f(x_{n-1})} f(x_{n-1})
$$

*(Equivalently written as $x_{n+1} = x_n - \frac{x_n - x_{n-1}}{f(x_n) - f(x_{n-1})} f(x_n)$)*

### 8.4 First Approximation ($x_2$)

$$
x_2 = x_0 - \frac{x_1 - x_0}{f(x_1) - f(x_0)} f(x_0)
$$

$$
= 1 - \frac{2 - 1}{4 - (-10)} \times (-10) = 1 - \frac{1}{4 + 10} \times (-10)
$$

$$
= 1.7143
$$

Evaluating $f(x_2)$:

$$
f(1.7143) = (1.7143)^4 - 1.7143 - 10 = -3.0776
$$

---

<!-- Page 18 -->

### 8.5 Second Approximation ($x_3$)

Using the previous two points $x_1 = 2$ ($f(x_1) = 4$) and $x_2 = 1.7143$ ($f(x_2) = -3.0776$):

$$
x_3 = x_1 - \frac{x_2 - x_1}{f(x_2) - f(x_1)} f(x_1)
$$

$$
= 2 - \frac{1.7143 - 2}{-3.0776 - 4} \times 4
$$

$$
= 2 - \frac{-0.2857}{-7.0776} \times 4
$$

$$
= 1.8385
$$

Evaluating $f(x_3)$:

$$
f(1.8385) = (1.8385)^4 - 1.8385 - 10 = -0.4135
$$

### 8.6 Third Approximation ($x_4$)

Using $x_2 = 1.7143$ ($f(x_2) = -3.0776$) and $x_3 = 1.8385$ ($f(x_3) = -0.4135$):

$$
x_4 = x_2 - \frac{x_3 - x_2}{f(x_3) - f(x_2)} f(x_2)
$$

$$
= 1.7143 - \frac{1.8385 - 1.7143}{-0.4135 - (-3.0776)} \times (-3.0776)
$$

$$
= 1.7143 - \frac{0.1242}{-0.4135 + 3.0776} \times (-3.0776)
$$

$$
= 1.8578
$$

Evaluating $f(x_4)$:

$$
f(1.8578) = (1.8578)^4 - 1.8578 - 10 = 0.0545
$$

---

<!-- Page 19 -->

### 8.7 Fourth Approximation ($x_5$)

Using $x_3 = 1.8385$ ($f(x_3) = -0.4135$) and $x_4 = 1.8578$ ($f(x_4) = 0.0545$):

$$
x_5 = x_3 - \frac{x_4 - x_3}{f(x_4) - f(x_3)} f(x_3)
$$

$$
= 1.8385 - \frac{1.8578 - 1.8385}{0.0545 - (-0.4135)} \times (-0.4135)
$$

$$
= 1.8556
$$

Evaluating $f(x_5)$:
*(Note: At $x_5 = 1.8556$, $f(1.8556) \approx -0.0045$, very close to zero).*

### 8.8 Fifth Approximation ($x_6$)

Using $x_4 = 1.8578$ ($f(x_4) = 0.0545$) and $x_5 = 1.8556$:

$$
x_6 = x_4 - \frac{x_5 - x_4}{f(x_5) - f(x_4)} f(x_4)
$$

$$
= 1.8556
$$

Since $x_5$ and $x_6$ match to four decimal places ($1.8556$):

$$
\mathbf{x \approx 1.8556}
$$

**Answer:** The required root using the Secant Method is **$1.8556$**.
