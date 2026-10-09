---
title: "Central Difference Interpolation, Unequally Spaced Interpolation, Numerical Integration, and Newton-Raphson Applications (Pages 53–72)"
course: "ECE 2213 — Numerical Analysis / Numerical Methods"
author: "Shishir (Roll 2310002)"
batch: "Batch 4 (Pages 53–72) — Final Notebook Batch"
source: "Numerical Analysis By Shishir 2310002.pdf"
tags:
  - numerical-methods
  - ece2213
  - central-interpolation
  - gauss-forward-interpolation
  - gauss-backward-interpolation
  - stirling-interpolation
  - lagrange-interpolation
  - newton-divided-difference
  - numerical-integration
  - trapezoidal-rule
  - simpsons-one-third-rule
  - simpsons-three-eighths-rule
  - weddles-rule
  - newton-raphson-method
  - square-root-iteration
---

# Central Interpolation, Unequal Spacing, Numerical Integration & Newton-Raphson Root Finding

---

## Part I: Central Difference Interpolation (Gauss Forward & Backward, Stirling)

<!-- Page 53 -->

### 1. Gauss Forward Interpolation (Conclusion of Page 52 Problem)

In the preceding batch (Page 52), we set up the central difference table to compute $y(3.75)$ from equispaced data centered at $x_0 = 3.5$ with uniform interval $h = 0.5$.

#### 1.1 Parameter Calculation
$$
x = 3.75, \quad x_0 = 3.5, \quad h = 0.5
$$

The dimensionless coordinate $u$ is:
$$
u = \frac{x - x_0}{h} = \frac{3.75 - 3.5}{0.5} = \frac{0.25}{0.5} = 0.5
$$

Since $0 < u < 1$ and lies close to the origin, Gauss's Forward formula provides rapid convergence.

---

#### 1.2 Gauss Forward Formula & Trajectory
The general Gauss Forward interpolation polynomial is:

$$
\begin{aligned}
y_u = y_0 &+ u \Delta y_0 + \frac{u(u-1)}{2!} \Delta^2 y_{-1} + \frac{(u+1)u(u-1)}{3!} \Delta^3 y_{-1} \\
&+ \frac{(u+1)u(u-1)(u-2)}{4!} \Delta^4 y_{-2} + \frac{(u+2)(u+1)u(u-1)(u-2)}{5!} \Delta^5 y_{-2} + \dots
\end{aligned}
$$

From the central difference table established on Page 52:
- $y_0 = 20.225$
- $\Delta y_0 = -1.581$
- $\Delta^2 y_{-1} = 0.237$
- $\Delta^3 y_{-1} = -0.038$
- $\Delta^4 y_{-2} = 0.009$
- $\Delta^5 y_{-2} = -0.003$

---

#### 1.3 Step-by-Step Numerical Substitution & Evaluation
Substituting $u = 0.5$ into each term:

$$
\begin{aligned}
y(3.75) &= 20.225 + (0.5)(-1.581) + \frac{(0.5)(0.5 - 1)}{2!} (0.237) \\
&\quad + \frac{(0.5 + 1)(0.5)(0.5 - 1)}{3!} (-0.038) \\
&\quad + \frac{(0.5 + 1)(0.5)(0.5 - 1)(0.5 - 2)}{4!} (0.009) \\
&\quad + \frac{(0.5 + 2)(0.5 + 1)(0.5)(0.5 - 1)(0.5 - 2)}{5!} (-0.003)
\end{aligned}
$$

Evaluating individual terms:
1. **Zeroth term:** $T_0 = 20.225$
2. **First term:** $T_1 = 0.5 \times (-1.581) = -0.7905$
3. **Second term:** $T_2 = \frac{0.5 \times (-0.5)}{2} \times 0.237 = -0.125 \times 0.237 = -0.029625$
4. **Third term:** $T_3 = \frac{1.5 \times 0.5 \times (-0.5)}{6} \times (-0.038) = \frac{-0.375}{6} \times (-0.038) = (-0.0625) \times (-0.038) = +0.002375$
5. **Fourth term:** $T_4 = \frac{1.5 \times 0.5 \times (-0.5) \times (-1.5)}{24} \times 0.009 = \frac{0.5625}{24} \times 0.009 = 0.0234375 \times 0.009 = +0.0002109$
6. **Fifth term:** $T_5 = \frac{2.5 \times 1.5 \times 0.5 \times (-0.5) \times (-1.5)}{120} \times (-0.003) = \frac{1.40625}{120} \times (-0.003) = -0.0000352$

Summing all contributions:
$$
\begin{aligned}
y_u &= 20.225 - 0.7905 - 0.029625 + 0.002375 + 0.0002109 - 0.0000352 \\
&= 19.4074257 \approx 19.4074
\end{aligned}
$$

$$
\mathbf{y(3.75) \approx 19.4074 \quad (\text{Exact sum; recorded as } 19.4076 \text{ in lecture note due to rounding})}
$$

---

<!-- Page 54 -->

### 2. Gauss Backward Interpolation Formula

#### 2.1 Formula Definition & Geometric Path
When the interpolation point $x$ lies slightly to the left of the central origin $x_0$ (i.e., $-1 < u < 0$), **Gauss's Backward Interpolation Formula** is employed. The difference terms follow a zigzag path that first steps upward:

$$
\begin{aligned}
y_u = y_0 &+ u \Delta y_{-1} + \frac{u(u+1)}{2!} \Delta^2 y_{-1} + \frac{u(u+1)(u-1)}{3!} \Delta^3 y_{-2} \\
&+ \frac{u(u+1)(u-1)(u+2)}{4!} \Delta^4 y_{-2} + \dots
\end{aligned}
$$

> [!TIP]
> **Zigzag Trajectory Comparison:**
> - **Gauss Forward:** Starts at $y_0 \to$ moves downward to $\Delta y_0 \to$ horizontally to $\Delta^2 y_{-1} \to$ downward to $\Delta^3 y_{-1} \to \dots$ (Best for $0 < u < 1$).
> - **Gauss Backward:** Starts at $y_0 \to$ moves upward to $\Delta y_{-1} \to$ horizontally to $\Delta^2 y_{-1} \to$ upward to $\Delta^3 y_{-2} \to \dots$ (Best for $-1 < u < 0$).

---

#### 2.2 Problem Statement (Page 54)
> **Problem:**  
> Find the population of the town in **1946** by Gauss's backward formula, given the census data:
> 
> | Year | 1931 | 1941 | 1951 | 1961 | 1971 |
> | :--- | :---: | :---: | :---: | :---: | :---: |
> | **Population (in thousands)** | 15 | 20 | 27 | 39 | 52 |

---

#### 2.3 Choice of Origin & Central Difference Table
We seek the value at $x = 1946$. The interval is $h = 10$.  
We choose the central reference year immediately above the target:
$$
x_0 = 1951, \quad h = 10
$$

The dimensionless coordinate is:
$$
u = \frac{x - x_0}{h} = \frac{1946 - 1951}{10} = \frac{-5}{10} = -0.5
$$
Since $-1 < u < 0$, Gauss Backward is the optimal formula.

We set up the difference table indexed around $x_0 = 1951$:

| Index $i$ | Year $x_i$ | Population $y_i$ | First Diff $\Delta y$ | Second Diff $\Delta^2 y$ | Third Diff $\Delta^3 y$ | Fourth Diff $\Delta^4 y$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| $-2$ | $1931$ | $15$ ($y_{-2}$) | | | | |
| | | | $5$ ($\Delta y_{-2}$) | | | |
| $-1$ | $1941$ | $20$ ($y_{-1}$) | | $2$ ($\Delta^2 y_{-2}$) | | |
| | | | **$7$** ($\Delta y_{-1}$) | | **$3$** ($\Delta^3 y_{-2}$) | |
| **0** | **1951** | **$27$** ($y_0$) | | **$5$** ($\Delta^2 y_{-1}$) | | **$-7$** ($\Delta^4 y_{-2}$) |
| | | | $12$ ($\Delta y_0$) | | $-4$ ($\Delta^3 y_{-1}$) | |
| $1$ | $1961$ | $39$ ($y_1$) | | $1$ ($\Delta^2 y_0$) | | |
| | | | $13$ ($\Delta y_1$) | | | |
| $2$ | $1971$ | $52$ ($y_2$) | | | | |

##### Difference Calculations (Census Data):
- $\Delta y_{-2} = 20 - 15 = 5$
- $\Delta y_{-1} = 27 - 20 = 7$
- $\Delta y_0 = 39 - 27 = 12$
- $\Delta y_1 = 52 - 39 = 13$
- $\Delta^2 y_{-2} = 7 - 5 = 2$
- $\Delta^2 y_{-1} = 12 - 7 = 5$
- $\Delta^2 y_0 = 13 - 12 = 1$
- $\Delta^3 y_{-2} = 5 - 2 = 3$
- $\Delta^3 y_{-1} = 1 - 5 = -4$
- $\Delta^4 y_{-2} = -4 - 3 = -7$

---

<!-- Page 55 -->

#### 2.4 Numerical Evaluation for $y(1946)$
Selected values along the Gauss Backward path:
- $y_0 = 27$
- $\Delta y_{-1} = 7$
- $\Delta^2 y_{-1} = 5$
- $\Delta^3 y_{-2} = 3$
- $\Delta^4 y_{-2} = -7$

Gauss Backward formula expansion:
$$
\begin{aligned}
y_u = y_0 &+ u \Delta y_{-1} + \frac{u(u+1)}{2!} \Delta^2 y_{-1} + \frac{u(u+1)(u-1)}{3!} \Delta^3 y_{-2} \\
&+ \frac{(u-1)u(u+1)(u+2)}{4!} \Delta^4 y_{-2} + \frac{u(u-2)(u+2)(u+1)(u-1)}{5!} \Delta^5 y_{-3} + \dots
\end{aligned}
$$

Substituting $u = -0.5$:
$$
\begin{aligned}
y(1946) &= 27 + (-0.5)(7) + \frac{(-0.5)(-0.5 + 1)}{2!} (5) + \frac{(-0.5 - 1)(-0.5)(-0.5 + 1)}{3!} (3) \\
&\quad + \frac{(-0.5 - 1)(-0.5)(-0.5 + 1)(-0.5 + 2)}{4!} (-7)
\end{aligned}
$$

Evaluating term by term:
1. $T_0 = 27$
2. $T_1 = (-0.5)(7) = -3.5$
3. $T_2 = \frac{(-0.5)(0.5)}{2} \times 5 = \frac{-0.25}{2} \times 5 = -0.125 \times 5 = -0.625$
4. $T_3 = \frac{(-1.5)(-0.5)(0.5)}{6} \times 3 = \frac{0.375}{6} \times 3 = 0.0625 \times 3 = +0.1875$
5. $T_4 = \frac{(-1.5)(-0.5)(0.5)(1.5)}{24} \times (-7) = \frac{0.5625}{24} \times (-7) = (0.0234375) \times (-7) = -0.1640625 \approx -0.1641$

Summing terms:
$$
\begin{aligned}
y(1946) &= 27 - 3.5 - 0.625 + 0.1875 - 0.1640625 \\
&= 22.8984375 \approx 22.8984 \quad \text{thousand}
\end{aligned}
$$

$$
\mathbf{y(1946) = 22.8984 \text{ thousand} \quad (\approx 22,898 \text{ people})}
$$

---

## Part II: Interpolation for Unequally Spaced Intervals

<!-- Page 56 -->

### 3. Lagrange's Interpolation Formula

> [!NOTE]
> **Pedagogical Note (Bengali Translation):**  
> *"যখন unequal step gap থাকে তখন $\rightarrow$ Lagrange's Formula"*  
> **English Translation:** *"When data points have unequal intervals ($h$ is not constant), standard finite difference formulas (Newton Forward/Backward, Gauss) cannot be applied. In that case, we must use Lagrange's formula or Newton's Divided Difference formula."*

#### 3.1 Mathematical Formulation
For $n+1$ distinct arbitrary points $(x_0, y_0), (x_1, y_1), \dots, (x_n, y_n)$:

$$
y = f(x) = \sum_{i=0}^n y_i \ell_i(x) = \sum_{i=0}^n f(x_i) \prod_{\substack{j=0 \\ j \ne i}}^n \frac{x - x_j}{x_i - x_j}
$$

Shishir's symmetric quotient notation (dividing by $\prod_{k=0}^n (x - x_k)$):
$$
\begin{aligned}
\frac{f(x)}{(x-x_0)(x-x_1)\dots(x-x_n)} &= \frac{f(x_0)}{(x_0-x_1)(x_0-x_2)\dots(x_0-x_n)(x-x_0)} \\
&\quad + \frac{f(x_1)}{(x_1-x_0)(x_1-x_2)\dots(x_1-x_n)(x-x_1)} \\
&\quad + \frac{f(x_2)}{(x_2-x_0)(x_2-x_1)\dots(x_2-x_n)(x-x_2)} \\
&\quad + \dots + \frac{f(x_n)}{(x_n-x_0)(x_n-x_1)\dots(x_n-x_{n-1})(x-x_n)}
\end{aligned}
$$

---

#### 3.2 Problem Statement (Page 56)
> **Problem:**  
> The values of the function $f(x)$ are given as:  
> $$
> f(1) = 4, \quad f(2) = 5, \quad f(7) = 5, \quad f(8) = 4
> $$  
> Find:
> 1. The interpolated value $f(6)$.
> 2. The value of $x$ for which $f(x)$ is maximum or minimum, and the corresponding extreme value.

---

<!-- Page 57 -->

#### 3.3 Setup of the Lagrange Polynomial
Tabulating the given points:

| $i$ | $x_i$ | $f(x_i)$ | Step Gap $\Delta x_i$ |
| :---: | :---: | :---: | :---: |
| $0$ | $x_0 = 1$ | $4$ | $x_1 - x_0 = 1$ |
| $1$ | $x_1 = 2$ | $5$ | $x_2 - x_1 = 5$ |
| $2$ | $x_2 = 7$ | $5$ | $x_3 - x_2 = 1$ |
| $3$ | $x_3 = 8$ | $4$ | — |

Applying Lagrange's symmetric formula for four points:
$$
\begin{aligned}
\frac{f(x)}{(x-1)(x-2)(x-7)(x-8)} &= \frac{4}{(1-2)(1-7)(1-8)(x-1)} + \frac{5}{(2-1)(2-7)(2-8)(x-2)} \\
&\quad + \frac{5}{(7-1)(7-2)(7-8)(x-7)} + \frac{4}{(8-1)(8-2)(8-7)(x-8)}
\end{aligned}
$$

##### Computing the Denominators:
1. For $x_0 = 1$: $(1-2)(1-7)(1-8) = (-1)(-6)(-7) = -42$
2. For $x_1 = 2$: $(2-1)(2-7)(2-8) = (1)(-5)(-6) = +30$
3. For $x_2 = 7$: $(7-1)(7-2)(7-8) = (6)(5)(-1) = -30$
4. For $x_3 = 8$: $(8-1)(8-2)(8-7) = (7)(6)(1) = +42$

Substituting these constants:
$$
\frac{f(x)}{(x-1)(x-2)(x-7)(x-8)} = -\frac{4}{42(x-1)} + \frac{5}{30(x-2)} - \frac{5}{30(x-7)} + \frac{4}{42(x-8)}
$$

---

<!-- Page 58 -->

#### 3.4 Algebraic Simplification & Evaluation of $f(6)$
Regrouping terms with common coefficients:
$$
= \frac{4}{42}\left[ \frac{1}{x-8} - \frac{1}{x-1} \right] + \frac{5}{30}\left[ \frac{1}{x-2} - \frac{1}{x-7} \right]
$$

Simplifying each bracket:
$$
\frac{1}{x-8} - \frac{1}{x-1} = \frac{(x-1) - (x-8)}{(x-8)(x-1)} = \frac{7}{(x-8)(x-1)}
$$
$$
\frac{1}{x-2} - \frac{1}{x-7} = \frac{(x-7) - (x-2)}{(x-2)(x-7)} = \frac{-5}{(x-2)(x-7)}
$$

Multiplying by outer factors:
$$
\frac{4}{42} \times \frac{7}{(x-8)(x-1)} = \frac{28}{42} \frac{1}{(x-8)(x-1)} = \frac{2}{3} \frac{1}{(x-8)(x-1)}
$$
$$
\frac{5}{30} \times \frac{-5}{(x-2)(x-7)} = \frac{-25}{30} \frac{1}{(x-2)(x-7)} = -\frac{5}{6} \frac{1}{(x-2)(x-7)}
$$

Combining both terms over the full denominator $(x-8)(x-1)(x-2)(x-7)$:
$$
\frac{f(x)}{(x-8)(x-1)(x-2)(x-7)} = \frac{\frac{2}{3}(x-2)(x-7) - \frac{5}{6}(x-8)(x-1)}{(x-8)(x-1)(x-2)(x-7)}
$$

Canceling the denominator on both sides:
$$
f(x) = \frac{2}{3}(x^2 - 9x + 14) - \frac{5}{6}(x^2 - 9x + 8)
$$

Expanding and combining like terms:
$$
\begin{aligned}
f(x) &= \left(\frac{2}{3} - \frac{5}{6}\right)x^2 - 9\left(\frac{2}{3} - \frac{5}{6}\right)x + \left(\frac{28}{3} - \frac{40}{6}\right) \\
&= \left(\frac{4 - 5}{6}\right)x^2 - 9\left(\frac{4 - 5}{6}\right)x + \left(\frac{56 - 40}{6}\right) \\
&= -\frac{x^2}{6} + \frac{9x}{6} + \frac{16}{6} \\
&= \frac{1}{6}(-x^2 + 9x + 16)
\end{aligned}
$$

##### Evaluation at $x = 6$:
$$
\begin{aligned}
f(6) &= \frac{1}{6}\left(-(6)^2 + 9(6) + 16\right) = \frac{1}{6}(-36 + 54 + 16) \\
&= \frac{1}{6}(34) = \frac{34}{6} \approx 5.667
\end{aligned}
$$

$$
\mathbf{f(6) \approx 5.667}
$$

---

<!-- Page 59 -->

#### 3.5 Determination of Extreme Values (Maximum or Minimum)
The analytical polynomial is:
$$
f(x) = \frac{1}{6}(-x^2 + 9x + 16)
$$

Taking the first derivative:
$$
f'(x) = \frac{1}{6}(-2x + 9)
$$

For stationary / critical points, set $f'(x) = 0$:
$$
\frac{1}{6}(-2x + 9) = 0 \implies -2x + 9 = 0 \implies \mathbf{x = 4.5}
$$

Second derivative test:
$$
f''(x) = \frac{d}{dx}\left[\frac{1}{6}(-2x + 9)\right] = -\frac{2}{6} = -\frac{1}{3} < 0 \quad (\text{negative})
$$
Since $f''(x) < 0$ everywhere, $f(x)$ attains a **maximum value** at $x = 4.5$.

##### Computing the Maximum Value:
$$
\begin{aligned}
f(4.5) &= \frac{1}{6}\left(-(4.5)^2 + 9(4.5) + 16\right) \\
&= \frac{1}{6}(-20.25 + 40.5 + 16) \\
&= \frac{1}{6}(36.25) = \frac{36.25}{6} \approx 6.0417 \approx \mathbf{6.04}
\end{aligned}
$$

$$
\mathbf{\text{Maximum value of } f(x) \text{ is } 6.04 \text{ at } x = 4.5}
$$

---

## Part III: Numerical Integration (Quadrature Formulas)

<!-- Page 60 -->

### 4. Trapezoidal Rule

#### 4.1 Theoretical Formula
The **Trapezoidal Rule** approximates the area under $f(x)$ by replacing the curve across each subinterval with a linear chord:

$$
\int_a^b f(x) \, dx = \frac{h}{2} \left[ (y_0 + y_n) + 2(y_1 + y_2 + \dots + y_{n-1}) \right]
$$

In verbal form:
$$
\int_a^b f(x) \, dx = \frac{h}{2} \left[ (\text{Sum of first and last ordinates}) + 2 \times (\text{Sum of all intermediate ordinates}) \right]
$$

> [!NOTE]
> **Subinterval Freedom:**  
> In the Trapezoidal rule, the number of intervals $n$ can be chosen freely as any positive integer ($n \ge 1$).

---

#### 4.2 Problem Statement & Computation (Page 60)
> **Problem:**  
> Evaluate $\int_0^6 \frac{1}{1+x^2} \, dx$ using the Trapezoidal rule.

##### Setup:
- Integrand: $f(x) = \frac{1}{1+x^2}$
- Limits: $a = 0, \quad b = 6$
- Step count: choose $n = 6$
- Step size: $h = \frac{b - a}{n} = \frac{6 - 0}{6} = 1$

##### Table of Ordinates:
| $i$ | $x_i$ | $f(x_i) = \frac{1}{1 + x_i^2}$ | Decimal Value ($y_i$) |
| :---: | :---: | :---: | :---: |
| $0$ | $0$ | $\frac{1}{1+0} = 1$ | $y_0 = 1.0000$ |
| $1$ | $1$ | $\frac{1}{1+1} = \frac{1}{2}$ | $y_1 = 0.5000$ |
| $2$ | $2$ | $\frac{1}{1+4} = \frac{1}{5}$ | $y_2 = 0.2000$ |
| $3$ | $3$ | $\frac{1}{1+9} = \frac{1}{10}$ | $y_3 = 0.1000$ |
| $4$ | $4$ | $\frac{1}{1+16} = \frac{1}{17}$ | $y_4 = 0.0588$ |
| $5$ | $5$ | $\frac{1}{1+25} = \frac{1}{26}$ | $y_5 = 0.0385$ |
| $6$ | $6$ | $\frac{1}{1+36} = \frac{1}{37}$ | $y_6 = 0.0270$ |

##### Applying the Trapezoidal Formula:
$$
\begin{aligned}
\int_0^6 \frac{1}{1+x^2} \, dx &= \frac{h}{2} \left[ (y_0 + y_6) + 2(y_1 + y_2 + y_3 + y_4 + y_5) \right] \\
&= \frac{1}{2} \left[ (1 + 0.0270) + 2(0.5 + 0.2 + 0.1 + 0.0588 + 0.0385) \right] \\
&= \frac{1}{2} \left[ 1.0270 + 2(0.8973) \right] \\
&= \frac{1}{2} [ 1.0270 + 1.7946 ] = \frac{1}{2} [2.8216] = 1.4108
\end{aligned}
$$

$$
\mathbf{\int_0^6 \frac{1}{1+x^2} \, dx \approx 1.4108 \quad (\text{Trapezoidal Rule})}
$$

---

<!-- Page 61 -->

### 5. Simpson's One-Third ($1/3$) Rule

#### 5.1 Subinterval Constraints for Numerical Quadrature Rules
The notes establish a crucial master classification table:

| Numerical Rule | Condition on Number of Subintervals $n$ | Step Size Calculation $h$ | Local Truncation Error |
| :--- | :--- | :---: | :---: |
| **Trapezoidal Rule** | Any positive integer $n$ | $h = \frac{b - a}{n}$ | $\mathcal{O}(h^2)$ |
| **Simpson's $1/3$ Rule** | $n$ must be **even** ($n = 2, 4, 6, \dots$) | $h = \frac{b - a}{\text{even } n}$ | $\mathcal{O}(h^4)$ |
| **Simpson's $3/8$ Rule** | $n$ must be **divisible by 3** ($n = 3, 6, 9, \dots$) | $h = \frac{b - a}{3k}$ | $\mathcal{O}(h^4)$ |
| **Weddle's Rule** | $n$ must be a **multiple of 6** ($n = 6, 12, 18, \dots$) | $h = \frac{b - a}{6k}$ | $\mathcal{O}(h^6)$ |

---

#### 5.2 Formula Definition
Simpson's $1/3$ rule approximates $f(x)$ piecewise by quadratic parabolas over pairs of intervals:

$$
\int_a^b f(x) \, dx = \frac{h}{3} \left[ (\text{Sum of first \& last ordinates}) + 4(\text{Sum of odd ordinates}) + 2(\text{Sum of even ordinates}) \right]
$$

$$
\int_a^b f(x) \, dx = \frac{h}{3} \left[ (y_0 + y_n) + 4(y_1 + y_3 + y_5 + \dots) + 2(y_2 + y_4 + y_6 + \dots) \right]
$$

---

#### 5.3 Problem Statement (Page 61)
> **Problem:**  
> Evaluate $\int_0^6 \frac{1}{1+x^2} \, dx$ using Simpson's one-third rule.

- Integrand: $f(x) = \frac{1}{1+x^2}$
- Range: $[0, 6]$
- Choice of $n$: $n = 6$ (even number, satisfying the condition)
- Step size: $h = \frac{6 - 0}{6} = 1$

---

<!-- Page 62 -->

#### 5.4 Evaluation of Simpson's $1/3$ Rule
Using the ordinates computed previously:
- First & last: $y_0 = 1, \quad y_6 = 0.0270$
- Odd ordinates: $y_1 = 0.5, \quad y_3 = 0.1, \quad y_5 = 0.0385$
- Even intermediate ordinates: $y_2 = 0.2, \quad y_4 = 0.0588$

Applying the formula:
$$
\begin{aligned}
\int_0^6 \frac{1}{1+x^2} \, dx &= \frac{1}{3} \left[ (y_0 + y_6) + 4(y_1 + y_3 + y_5) + 2(y_2 + y_4) \right] \\
&= \frac{1}{3} \left[ (1 + 0.0270) + 4(0.5 + 0.1 + 0.0385) + 2(0.2 + 0.0588) \right] \\
&= \frac{1}{3} \left[ 1.0270 + 4(0.6385) + 2(0.2588) \right] \\
&= \frac{1}{3} \left[ 1.0270 + 2.5540 + 0.5176 \right] \\
&= \frac{1}{3} [4.0986] = 1.3662
\end{aligned}
$$

$$
\mathbf{\int_0^6 \frac{1}{1+x^2} \, dx \approx 1.3662 \quad (\text{Simpson's } 1/3 \text{ Rule})}
$$

---

<!-- Page 63 -->

### 6. Simpson's Three-Eighths ($3/8$) Rule

#### 6.1 Theoretical Formula & Grouping Rules
Simpson's $3/8$ rule replaces $f(x)$ with cubic polynomials fitted across triplets of subintervals:

$$
\int_a^b f(x) \, dx = \frac{3h}{8} \left[ (y_0 + y_n) + 3(y_1 + y_2 + y_4 + y_5 + \dots + y_{n-1}) + 2(y_3 + y_6 + y_9 + \dots + y_{n-3}) \right]
$$

> [!NOTE]
> **Pedagogical Note (Bengali Translation):**  
> - *Under factor 3:* *"৩ দ্বারা ভাগ যায় এগুলো থাকবেনা"* $\to$ *"Indices that are NOT multiples of 3 are multiplied by 3."*  
> - *Under factor 2:* *"৩ দ্বারা ভাগ যায় এগুলো থাকবে"* $\to$ *"Intermediate indices that ARE multiples of 3 ($y_3, y_6, \dots$) are multiplied by 2."*  
> - *Right margin note on $y_6$:* *"$y_6$ হলো না কারন আগে বসানো হয়েছে"* $\to$ *"$y_6$ is excluded from the $\times 2$ group because it has already been accounted for in the boundary term $(y_0 + y_n)$."*

---

#### 6.2 Evaluation on Same Integral
- Limits: $[0, 6]$
- Choice of $n$: $n = 6$ (divisible by 3)
- Step size: $h = \frac{6 - 0}{6} = 1$

Grouping ordinates:
- $(y_0 + y_6) = 1 + 0.0270 = 1.0270$
- Non-multiples of 3: $y_1 + y_2 + y_4 + y_5 = 0.5 + 0.2 + 0.0588 + 0.0385 = 0.7973$
- Multiple of 3 (excluding endpoints): $y_3 = 0.1$

Substituting into Simpson's $3/8$ formula:
$$
\begin{aligned}
\int_0^6 \frac{1}{1+x^2} \, dx &= \frac{3}{8} \times 1 \left[ (y_0 + y_6) + 3(y_1 + y_2 + y_4 + y_5) + 2 y_3 \right] \\
&= \frac{3}{8} \left[ 1.0270 + 3(0.7973) + 2(0.1) \right] \\
&= \frac{3}{8} \left[ 1.0270 + 2.3919 + 0.2 \right] \\
&= \frac{3}{8} [3.6189] = \frac{10.8567}{8} = 1.3570875 \approx 1.3571
\end{aligned}
$$

$$
\mathbf{\int_0^6 \frac{1}{1+x^2} \, dx \approx 1.3571 \quad (\text{Simpson's } 3/8 \text{ Rule})}
$$

---

<!-- Page 64 -->

### 7. Weddle's Rule

#### 7.1 Formula & Coefficient Weighting Pattern
**Weddle's Rule** is a 6th-order Newton-Cotes closed quadrature formula applied to groups of 6 subintervals ($n = 6, 12, \dots$):

$$
\int_a^b f(x) \, dx = \frac{3h}{10} \left[ y_0 + 5y_1 + y_2 + 6y_3 + y_4 + 5y_5 + y_6 \right]
$$

> [!NOTE]
> **Pedagogical Note (Bengali Translation):**  
> *"এইখানে যতগুলো y থাকবে সরাসরি যোগ হবে এবং একটা Rest করবে আরেকটায় P. সংখ্যা বসবে 5 6 5 6 এইভাবে।"*  
> **English Translation:** *"Every ordinate in the block is summed directly with specific weights: the baseline ordinates have weight 1, while intermediate ordinates are weighted by the recurring sequence $5, 1, 6, 1, 5$ (i.e., weights $1, 5, 1, 6, 1, 5, 1$)."*

---

#### 7.2 Numerical Evaluation for $n = 6$
Applying Weddle's rule to $\int_0^6 \frac{1}{1+x^2} \, dx$ with $h = 1$:

$$
\begin{aligned}
\int_0^6 \frac{1}{1+x^2} \, dx &= \frac{3(1)}{10} \left[ y_0 + 5y_1 + y_2 + 6y_3 + y_4 + 5y_5 + y_6 \right] \\
&= \frac{3}{10} \left[ 1 + 5(0.5) + 0.2 + 6(0.1) + 0.0588 + 5(0.0385) + 0.0270 \right] \\
&= \frac{3}{10} \left[ 1 + 2.5 + 0.2 + 0.6 + 0.0588 + 0.1925 + 0.0270 \right] \\
&= \frac{3}{10} [4.5783] = 1.37349 \approx 1.3735
\end{aligned}
$$

$$
\mathbf{\int_0^6 \frac{1}{1+x^2} \, dx \approx 1.3735 \quad (\text{Weddle's Rule})}
$$

---

#### 7.3 Comparative Accuracy Benchmark for $\int_0^6 \frac{1}{1+x^2} \, dx$
The analytical exact value of the integral is:
$$
I_{\text{exact}} = \int_0^6 \frac{1}{1+x^2} \, dx = \left[ \tan^{-1}(x) \right]_0^6 = \tan^{-1}(6) \approx 1.4056476 \text{ rad}
$$

| Quadrature Method | Numerical Result | Absolute Error $|I_{\text{num}} - I_{\text{exact}}|$ | Relative Error (\%) |
| :--- | :---: | :---: | :---: |
| **Trapezoidal Rule** | $1.4108$ | $0.00515$ | $0.367\%$ |
| **Simpson's $1/3$ Rule** | $1.3662$ | $0.03945$ | $2.806\%$ |
| **Simpson's $3/8$ Rule** | $1.3571$ | $0.04855$ | $3.454\%$ |
| **Weddle's Rule** | $1.3735$ | $0.03215$ | $2.287\%$ |

---

## Part IV: Newton-Raphson Method & Iterative Root Formulas

<!-- Page 65 -->

### 8. Newton-Raphson Root-Finding Method

#### 8.1 Problem Statement
> **Problem:**  
> Find the real root of the polynomial equation:
> $$
> x^4 - x - 10 = 0
> $$
> using the Newton-Raphson method, correct to three decimal places.

---

#### 8.2 Root Bracketing & Initial Guess Selection
Let $f(x) = x^4 - x - 10$. Evaluating integer values:
- $f(0) = 0 - 0 - 10 = -10$
- $f(1) = 1^4 - 1 - 10 = -10 \quad (-\text{ve})$
- $f(2) = 2^4 - 2 - 10 = 16 - 12 = 4 \quad (+\text{ve})$

Since $f(1)$ and $f(2)$ have opposite signs ($f(1)f(2) < 0$), by the Intermediate Value Theorem, a real root exists in $(1, 2)$.

> [!TIP]
> **Heuristic for Initial Guess $x_0$:**  
> *Bengali Annotation:* *"[যে point এর কাছে]"* $\to$ *"[Select the boundary point closer to zero value]"*.  
> Here $|f(2)| = 4 < |-10| = |f(1)|$. Therefore, the root lies closer to $x = 2$.  
> We choose initial guess: **$x_0 = 2$**.

---

#### 8.3 Recurrence Formula & First Iteration
The Newton-Raphson recurrence relation is:
$$
x_{i+1} = x_i - \frac{f(x_i)}{f'(x_i)}
$$

Derivative:
$$
f'(x) = 4x^3 - 1
$$
At $x_0 = 2$:
$$
f(2) = 4, \quad f'(2) = 4(2)^3 - 1 = 32 - 1 = 31
$$

##### Iteration 1:
$$
x_1 = x_0 - \frac{f(x_0)}{f'(x_0)} = 2 - \frac{4}{31} = 2 - 0.12903 = 1.87097 \approx \mathbf{1.871}
$$

---

<!-- Page 66 -->

#### 8.4 Subsequent Iterations & Convergence

##### Iteration 2:
At $x_1 = 1.871$:
- $f(1.871) = (1.871)^4 - 1.871 - 10 = 12.2548 - 1.871 - 10 = 0.3838$
- $f'(1.871) = 4(1.871)^3 - 1 = 4(6.5497) - 1 = 26.1988 - 1 = 25.1988$

$$
x_2 = x_1 - \frac{f(x_1)}{f'(x_1)} = 1.871 - \frac{0.3838}{25.1988} = 1.871 - 0.01523 = 1.85577 \approx \mathbf{1.8558}
$$

##### Iteration 3:
At $x_2 = 1.8558$:
- $f(1.8558) = (1.8558)^4 - 1.8558 - 10 = 11.8611 - 1.8558 - 10 = 0.0053$
- $f'(1.8558) = 4(1.8558)^3 - 1 = 4(6.3914) - 1 = 25.5656 - 1 = 24.5656$

$$
x_3 = x_2 - \frac{f(x_2)}{f'(x_2)} = 1.8558 - \frac{0.0053}{24.5656} = 1.8558 - 0.0002157 = 1.85558 \approx \mathbf{1.856}
$$

Since $x_2 = 1.856$ and $x_3 = 1.856$ to three decimal places:
$$
\mathbf{\text{Required root is } 1.856}
$$

---

<!-- Page 67 -->

### 9. Proof of Square Root Iteration Formula & Finding $\sqrt{35}$

#### 9.1 Derivation / Proof
> **Problem:**  
> Using the Newton-Raphson formula, prove that the iterative formula for finding the square root of $N$ is:
> $$
> x_{i+1} = \frac{1}{2}\left[ x_i + \frac{N}{x_i} \right]
> $$
> Hence find the square root of $35$.

##### Proof:
Let $x = \sqrt{N}$. Squaring both sides:
$$
x^2 = N \implies x^2 - N = 0
$$

Define:
$$
f(x) = x^2 - N
$$
Differentiating with respect to $x$:
$$
f'(x) = 2x
$$

Substituting $f(x_i)$ and $f'(x_i)$ into the Newton-Raphson scheme:
$$
\begin{aligned}
x_{i+1} &= x_i - \frac{f(x_i)}{f'(x_i)} \\
&= x_i - \frac{x_i^2 - N}{2x_i} \\
&= \frac{2x_i^2 - (x_i^2 - N)}{2x_i} \\
&= \frac{x_i^2 + N}{2x_i} \\
&= \frac{1}{2} \left[ \frac{x_i^2}{x_i} + \frac{N}{x_i} \right] \\
\therefore x_{i+1} &= \frac{1}{2}\left[ x_i + \frac{N}{x_i} \right] \quad \mathbf{\text{(Proved)}}
\end{aligned}
$$
*(This classical recurrence is also known as Heron's formula or the Babylonian method).*

---

<!-- Page 68 -->

#### 9.2 Application: Finding $\sqrt{35}$
Let $N = 35$ and $f(x) = x^2 - 35$.

##### Bracketing the Root:
- $f(0) = -35$
- $f(1) = 1 - 35 = -34$
- $f(2) = 4 - 35 = -31$
- $f(3) = 9 - 35 = -26$
- $f(4) = 16 - 35 = -19$
- $f(5) = 25 - 35 = -10 \quad (-\text{ve})$
- $f(6) = 36 - 35 = +1 \quad (+\text{ve})$

$f(5)$ and $f(6)$ are of opposite signs, so the root lies in $(5, 6)$.  
Since $|f(6)| = 1 < |-10|$, the root is very close to $6$.  
We choose initial guess **$x_0 = 6$**.

##### Iteration Scheme:
$$
x_{i+1} = \frac{1}{2} \left[ x_i + \frac{35}{x_i} \right]
$$

1. **Iteration 1 ($i=0$):**
   $$
   x_1 = \frac{1}{2}\left[ x_0 + \frac{35}{x_0} \right] = \frac{1}{2}\left[ 6 + \frac{35}{6} \right] = \frac{1}{2}[6 + 5.83333] = 5.91667
   $$
   *(Note: The handwritten notebook recorded $x_1 = 5.9165$, which was subsequently used in the next step).*

2. **Iteration 2 ($i=1$):**
   $$
   x_2 = \frac{1}{2}\left[ x_1 + \frac{35}{x_1} \right] = \frac{1}{2}\left[ 5.9165 + \frac{35}{5.9165} \right] = \frac{1}{2}[5.9165 + 5.91566] = 5.91608 \approx \mathbf{5.9161}
   $$

3. **Iteration 3 ($i=2$):**
   $$
   x_3 = \frac{1}{2}\left[ x_2 + \frac{35}{x_2} \right] = \frac{1}{2}\left[ 5.9161 + \frac{35}{5.9161} \right] = \mathbf{5.9161}
   $$

Since $x_2$ and $x_3$ match up to four decimal places:
$$
\mathbf{\sqrt{35} \approx 5.916 \quad \text{(correct to three decimal places)}}
$$

---

<!-- Page 69 -->

### 10. Master Reference Table for Newton-Raphson Iterative Formulas

From the general Newton-Raphson framework, we can construct iterative formulas for common algebraic roots and inverses without performing explicit division:

| Target Mathematical Quantity | Setup Function $f(x)$ | Derivative $f'(x)$ | Newton-Raphson Iterative Recurrence $x_{i+1}$ |
| :--- | :---: | :---: | :--- |
| **Inverse ($x = \frac{1}{N}$)** | $\frac{1}{x} - N = 0$ | $-\frac{1}{x^2}$ | $x_{i+1} = x_i(2 - N x_i)$ |
| **Square Root ($x = \sqrt{N}$)** | $x^2 - N = 0$ | $2x$ | $x_{i+1} = \frac{1}{2}\left(x_i + \frac{N}{x_i}\right)$ |
| **Inverse Square Root ($x = \frac{1}{\sqrt{N}}$)** | $\frac{1}{x^2} - N = 0$ | $-\frac{2}{x^3}$ | $x_{i+1} = \frac{1}{2}x_i(3 - N x_i^2)$ |
| **General $p$-th Root ($x = N^{1/p}$)** | $x^p - N = 0$ | $p x^{p-1}$ | $x_{i+1} = \frac{1}{p}\left[(p-1)x_i + \frac{N}{x_i^{p-1}}\right]$ |
| **Reciprocal of $p$-th Root ($x = N^{-1/p}$)** | $\frac{1}{x^p} - N = 0$ | $-\frac{p}{x^{p+1}}$ | $x_{i+1} = \frac{x_i}{p}\left[(p+1) - N x_i^p\right]$ |

---

## Part V: Newton's Divided Difference & Stirling Interpolation

<!-- Page 70 -->

### 11. Newton's Divided Difference Interpolation Formula

#### 11.1 Mathematical Formulation
When given $n+1$ arbitrary data points $(x_0, f(x_0)), (x_1, f(x_1)), \dots, (x_n, f(x_n))$ with **unequal spacing**, Newton's divided difference polynomial is defined as:

$$
\begin{aligned}
f(x) = f(x_0) &+ (x - x_0) f[x_0, x_1] + (x - x_0)(x - x_1) f[x_0, x_1, x_2] \\
&+ (x - x_0)(x - x_1)(x - x_2) f[x_0, x_1, x_2, x_3] + \dots
\end{aligned}
$$

In Shishir's notation:
$$
f(x) = f(x_0) + (x - x_0)\Delta f(x_0) + (x - x_0)(x - x_1)\Delta^2 f(x_0) + (x - x_0)(x - x_1)(x - x_2)\Delta^3 f(x_0) + \dots
$$

> [!NOTE]
> **Pedagogical Note (Bengali Translation):**  
> *"[যদি $h$ এর Difference same না হয় তখন এটা use করে]"* $\to$ *"[Use this when step size differences ($h$) between successive points are unequal]."*

---

#### 11.2 Problem Statement (Page 70)
> **Problem:**  
> By means of Newton's divided difference formulae, find the values of **$f(8)$** and **$f(15)$** from the following data table:
> 
> | $x$ | 4 | 5 | 7 | 10 | 11 | 13 |
> | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
> | $f(x)$ | 48 | 100 | 294 | 900 | 1210 | 2028 |

---

#### 11.3 Divided Difference Table
Constructing the divided difference quotient table:

| $x$ | $f(x)$ | 1st Divided Diff $f[x_i, x_{i+1}]$ | 2nd Divided Diff $f[x_i, x_{i+1}, x_{i+2}]$ | 3rd Divided Diff $f[x_i, \dots, x_{i+3}]$ | 4th Divided Diff $f[x_i, \dots, x_{i+4}]$ |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **$4$ ($x_0$)** | **$48$** | | | | |
| | | $\frac{100 - 48}{5 - 4} =$ **$52$** | | | |
| $5$ ($x_1$) | $100$ | | $\frac{97 - 52}{7 - 4} = \frac{45}{3} =$ **$15$** | | |
| | | $\frac{294 - 100}{7 - 5} = \frac{194}{2} = 97$ | | $\frac{21 - 15}{10 - 4} = \frac{6}{6} =$ **$1$** | |
| $7$ ($x_2$) | $294$ | | $\frac{202 - 97}{10 - 5} = \frac{105}{5} = 21$ | | $\frac{1 - 1}{11 - 4} = 0$ |
| | | $\frac{900 - 294}{10 - 7} = \frac{606}{3} = 202$ | | $\frac{27 - 21}{11 - 5} = \frac{6}{6} = 1$ | |
| $10$ ($x_3$) | $900$ | | $\frac{310 - 202}{11 - 7} = \frac{108}{4} = 27$ | | $\frac{1 - 1}{13 - 5} = 0$ |
| | | $\frac{1210 - 900}{11 - 10} = \frac{310}{1} = 310$ | | $\frac{33 - 27}{13 - 7} = \frac{6}{6} = 1$ | |
| $11$ ($x_4$) | $1210$ | | $\frac{409 - 310}{13 - 10} = \frac{99}{3} = 33$ | | |
| | | $\frac{2028 - 1210}{13 - 11} = \frac{818}{2} = 409$ | | | |
| $13$ ($x_5$) | $2028$ | | | | |

*Notice that the third divided difference is constant ($= 1$), meaning all fourth and higher divided differences identically vanish.*

---

<!-- Page 71 -->

#### 11.4 Polynomial Formula & Evaluations
Using the leading diagonal entries of the table:
- $f(x_0) = 48$
- $f[x_0, x_1] = 52$
- $f[x_0, x_1, x_2] = 15$
- $f[x_0, x_1, x_2, x_3] = 1$

The polynomial is:
$$
f(x) = 48 + (x - 4)(52) + (x - 4)(x - 5)(15) + (x - 4)(x - 5)(x - 7)(1)
$$

##### 1. Calculating $f(8)$:
Substitute $x = 8$:
$$
\begin{aligned}
f(8) &= 48 + (8 - 4)(52) + (8 - 4)(8 - 5)(15) + (8 - 4)(8 - 5)(8 - 7)(1) \\
&= 48 + (4)(52) + (4)(3)(15) + (4)(3)(1)(1) \\
&= 48 + 208 + 180 + 12 = 448
\end{aligned}
$$

$$
\mathbf{f(8) = 448}
$$

##### 2. Calculating $f(15)$:
Substitute $x = 15$:
$$
\begin{aligned}
f(15) &= 48 + (15 - 4)(52) + (15 - 4)(15 - 5)(15) + (15 - 4)(15 - 5)(15 - 7)(1) \\
&= 48 + (11)(52) + (11)(10)(15) + (11)(10)(8)(1) \\
&= 48 + 572 + 1650 + 880 = 3150
\end{aligned}
$$

$$
\mathbf{f(15) = 3150}
$$

---

### 12. Stirling's Central Difference Interpolation Formula

#### 12.1 Mathematical Formulation
**Stirling's Formula** is obtained by taking the arithmetic mean of Gauss's Forward and Gauss's Backward formulas:

$$
\begin{aligned}
y = f(x) = y_0 &+ p \left[ \frac{\Delta y_0 + \Delta y_{-1}}{2} \right] + \frac{p^2}{2!} \Delta^2 y_{-1} \\
&+ \frac{p(p^2 - 1)}{3!} \left[ \frac{\Delta^3 y_{-1} + \Delta^3 y_{-2}}{2} \right] + \frac{p^2(p^2 - 1)}{4!} \Delta^4 y_{-2} \\
&+ \frac{p(p^2 - 1)(p^2 - 2^2)}{5!} \left[ \frac{\Delta^5 y_{-2} + \Delta^5 y_{-3}}{2} \right] + \frac{p^2(p^2 - 1)(p^2 - 2^2)}{6!} \Delta^6 y_{-3} + \dots
\end{aligned}
$$

where:
$$
p = \frac{x - x_0}{h}
$$

> [!TIP]
> **Optimal Range for Stirling's Formula:**  
> Stirling's formula is exceptionally accurate and fast-converging when $-\frac{1}{2} < p < \frac{1}{2}$ (i.e., near the central table node).

---

<!-- Page 72 -->

#### 12.2 Problem Statement (Page 72)
> **Problem:**  
> Use Stirling's formula to find $u_{32}$, given the following data:
> 
> | $x$ | 20 | 25 | 30 | 35 | 40 | 45 |
> | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
> | $u_x$ | 14.035 | 13.674 | 13.257 | 12.734 | 12.089 | 11.309 |

---

#### 12.3 Origin Selection & Central Difference Table
We want $u_{32}$ at $x = 32$. The grid interval is $h = 5$.  
We choose origin $x_0 = 30$ because $32$ is closest to $30$:
$$
p = \frac{x - x_0}{h} = \frac{32 - 30}{5} = \frac{2}{5} = 0.4 \quad (|p| < 0.5)
$$

We build the central difference table indexed around $x_0 = 30$:

| Index $i$ | $x_i$ | $y_i = u_{x_i}$ | First Diff $\Delta y$ | Second Diff $\Delta^2 y$ | Third Diff $\Delta^3 y$ | Fourth Diff $\Delta^4 y$ | Fifth Diff $\Delta^5 y$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| $-2$ | $20$ | $14.035$ ($y_{-2}$) | | | | | |
| | | | $-0.361$ ($\Delta y_{-2}$) | | | | |
| $-1$ | $25$ | $13.674$ ($y_{-1}$) | | $-0.056$ ($\Delta^2 y_{-2}$) | | | |
| | | | **$-0.417$** ($\Delta y_{-1}$) | | **$-0.050$** ($\Delta^3 y_{-2}$) | | |
| **0** | **30** | **13.257** ($y_0$) | | **$-0.106$** ($\Delta^2 y_{-1}$) | | **$0.034$** ($\Delta^4 y_{-2}$) | |
| | | | **$-0.523$** ($\Delta y_0$) | | **$-0.016$** ($\Delta^3 y_{-1}$) | | **$-0.031$** ($\Delta^5 y_{-2}$) |
| $1$ | $35$ | $12.734$ ($y_1$) | | $-0.122$ ($\Delta^2 y_0$) | | $0.003$ ($\Delta^4 y_{-1}$) | |
| | | | $-0.645$ ($\Delta y_1$) | | $-0.013$ ($\Delta^3 y_0$) | | |
| $2$ | $40$ | $12.089$ ($y_2$) | | $-0.135$ ($\Delta^2 y_1$) | | | |
| | | | $-0.780$ ($\Delta y_2$) | | | | |
| $3$ | $45$ | $11.309$ ($y_3$) | | | | | |

##### Difference Calculations (Stirling Table):
- $\Delta y_{-2} = 13.674 - 14.035 = -0.361$
- $\Delta y_{-1} = 13.257 - 13.674 = -0.417$
- $\Delta y_0 = 12.734 - 13.257 = -0.523$
- $\Delta y_1 = 12.089 - 12.734 = -0.645$
- $\Delta y_2 = 11.309 - 12.089 = -0.780$
- $\Delta^2 y_{-2} = -0.417 - (-0.361) = -0.056$
- $\Delta^2 y_{-1} = -0.523 - (-0.417) = -0.106$
- $\Delta^2 y_0 = -0.645 - (-0.523) = -0.122$
- $\Delta^2 y_1 = -0.780 - (-0.645) = -0.135$
- $\Delta^3 y_{-2} = -0.106 - (-0.056) = -0.050$
- $\Delta^3 y_{-1} = -0.122 - (-0.106) = -0.016$
- $\Delta^3 y_0 = -0.135 - (-0.122) = -0.013$
- $\Delta^4 y_{-2} = -0.016 - (-0.050) = 0.034$
- $\Delta^4 y_{-1} = -0.013 - (-0.016) = 0.003$
- $\Delta^5 y_{-2} = 0.003 - 0.034 = -0.031$

---

#### 12.4 Numerical Evaluation for $u_{32}$
From the formula with $p = 0.4$:

$$
\begin{aligned}
u_{32} = y_0 &+ p \left[ \frac{\Delta y_0 + \Delta y_{-1}}{2} \right] + \frac{p^2}{2!} \Delta^2 y_{-1} \\
&+ \frac{p(p^2 - 1)}{3!} \left[ \frac{\Delta^3 y_{-1} + \Delta^3 y_{-2}}{2} \right] + \frac{p^2(p^2 - 1)}{4!} \Delta^4 y_{-2} + \dots
\end{aligned}
$$

Evaluating terms:
1. **$y_0$:** $13.257$
2. **Mean of First Differences:**  
   $\frac{\Delta y_0 + \Delta y_{-1}}{2} = \frac{-0.523 + (-0.417)}{2} = \frac{-0.940}{2} = -0.470$  
   $p \times (-0.470) = 0.4 \times (-0.470) = -0.188$
3. **Second Difference:**  
   $\frac{p^2}{2} \Delta^2 y_{-1} = \frac{(0.4)^2}{2} (-0.106) = 0.08 \times (-0.106) = -0.00848$
4. **Mean of Third Differences:**  
   $\frac{\Delta^3 y_{-1} + \Delta^3 y_{-2}}{2} = \frac{-0.016 + (-0.050)}{2} = \frac{-0.066}{2} = -0.033$  
   $\frac{p(p^2 - 1)}{6} = \frac{0.4((0.4)^2 - 1)}{6} = \frac{0.4(0.16 - 1)}{6} = \frac{0.4(-0.84)}{6} = \frac{-0.336}{6} = -0.056$  
   $(-0.056) \times (-0.033) = +0.001848$
5. **Fourth Difference:**  
   $\frac{p^2(p^2 - 1)}{24} = \frac{0.16(-0.84)}{24} = \frac{-0.1344}{24} = -0.0056$  
   $(-0.056) \times 0.034 = -0.0001904$

Summing all calculated terms:
$$
\begin{aligned}
u_{32} &= 13.257 - 0.188 - 0.00848 + 0.001848 - 0.0001904 \\
&= 13.0621776
\end{aligned}
$$

$$
\mathbf{u_{32} \approx 13.0621776}
$$

---

## Part VI: Comparative Synthesis & Final Notebook Reference

### 13. Master Comparison of Interpolation Methods

| Method | Spacing Requirement | Optimal Target Location | Parameter Range | Order of Accuracy | Key Characteristic |
| :--- | :--- | :--- | :---: | :---: | :--- |
| **Newton Forward** | Equispaced ($h = \text{const}$) | Beginning of table | $0 < u < 1$ | Polynomial degree $n$ | Uses top diagonal forward differences $\Delta^k y_0$. |
| **Newton Backward** | Equispaced ($h = \text{const}$) | End of table | $-1 < u < 0$ | Polynomial degree $n$ | Uses bottom diagonal backward differences $\nabla^k y_n$. |
| **Gauss Forward** | Equispaced ($h = \text{const}$) | Near center, slightly right | $0 < u < 1$ | Central difference | Zigzag trajectory stepping downward. |
| **Gauss Backward** | Equispaced ($h = \text{const}$) | Near center, slightly left | $-1 < u < 0$ | Central difference | Zigzag trajectory stepping upward. |
| **Stirling's Formula** | Equispaced ($h = \text{const}$) | Center of table | $-\frac{1}{2} < p < \frac{1}{2}$ | Central difference | Arithmetic average of Gauss Forward & Backward. |
| **Bessel's Formula** | Equispaced ($h = \text{const}$) | Midway between two nodes | $\frac{1}{4} < p < \frac{3}{4}$ | Central difference | Uses mean of even differences and single odd differences. |
| **Lagrange's Formula** | Unequal or Arbitrary | Anywhere within span | Arbitrary | Polynomial degree $n$ | No difference table needed; computationally heavy to add new points. |
| **Newton Divided Difference** | Unequal or Arbitrary | Anywhere within span | Arbitrary | Polynomial degree $n$ | Incremental table; easily updated when a new data point is added. |

---

### 14. Master Comparison of Numerical Integration Rules

| Quadrature Rule | Subinterval Constraint ($n$) | Underlying Polynomial Approximation | Composite Formulation | Truncation Error | Exact For Polynomials Of Degree |
| :--- | :---: | :--- | :--- | :---: | :---: |
| **Trapezoidal Rule** | Any $n \ge 1$ | Linear ($1^{\text{st}}$ order) | $\frac{h}{2}[(y_0 + y_n) + 2\sum_{i=1}^{n-1} y_i]$ | $-\frac{(b-a)h^2}{12} f''(\xi)$ | $\le 1$ |
| **Simpson's $1/3$ Rule** | $n$ must be **even** ($2k$) | Quadratic ($2^{\text{nd}}$ order parabola) | $\frac{h}{3}[(y_0 + y_n) + 4\sum y_{\text{odd}} + 2\sum y_{\text{even}}]$ | $-\frac{(b-a)h^4}{180} f^{(4)}(\xi)$ | $\le 3$ |
| **Simpson's $3/8$ Rule** | $n$ must be **multiple of 3** ($3k$) | Cubic ($3^{\text{rd}}$ order) | $\frac{3h}{8}[(y_0 + y_n) + 3\sum y_{i \ne 3k} + 2\sum y_{3k}]$ | $-\frac{(b-a)h^4}{80} f^{(4)}(\xi)$ | $\le 3$ |
| **Weddle's Rule** | $n$ must be **multiple of 6** ($6k$) | 6th degree polynomial | $\frac{3h}{10}[y_0 + 5y_1 + y_2 + 6y_3 + y_4 + 5y_5 + y_6 + \dots]$ | $-\frac{(b-a)h^6}{140} f^{(6)}(\xi)$ | $\le 5$ |

---

### 15. Notebook Series Complete Overview (Pages 1–72)

With the completion of Batch 4, the entire 72-page handwritten course notebook of Shishir (Roll 2310002) is fully digitized into four structured, Obsidian-compatible study files:

1. **`01_Error_Analysis_and_Root_Finding_pp01-19.md`**  
   - Error types (Absolute, Relative, Percentage, Propagation)
   - Truncation error in Lagrange interpolation
   - Iterative root finding: Bisection Method, Regula Falsi (False Position), Secant Method
2. **`02_Systems_of_Linear_Equations_pp20-35.md`**  
   - Direct elimination: Gauss Elimination (Row operations and Multiplier method), Gauss-Jordan
   - Matrix Factorization: LU Decomposition (Doolittle's Method, Crout's Method)
   - Iterative methods: Gauss-Seidel Iteration with Diagonal Dominance criterion
3. **`03_Numerical_Calculus_and_ODE_pp36-52.md`**  
   - Initial Value ODE Solvers: Euler's Method, Modified Euler (Heun's Predictor-Corrector), Taylor Series Method, Runge-Kutta 4th Order (Classical RK4)
   - Finite Differences & Top/Bottom Interpolation: Forward Differences ($\Delta$), Backward Differences ($\nabla$), Newton-Gregory Forward & Backward Interpolation, Gauss Forward setup
4. **`04_Central_Interpolation_and_Numerical_Integration_pp53-72.md` (This File)**  
   - Central Difference Interpolation: Gauss Forward evaluation, Gauss Backward, Stirling's Formula
   - Unequally Spaced Interpolation: Lagrange's Interpolation (evaluation, extrema finding), Newton's Divided Difference
   - Numerical Quadrature: Trapezoidal Rule, Simpson's $1/3$, Simpson's $3/8$, Weddle's Rule with comparative error benchmarks
   - Root Finding Revisited: Newton-Raphson Method, Square Root ($\sqrt{N}$) derivation & computation, General $p$-th root / reciprocal master formulas
