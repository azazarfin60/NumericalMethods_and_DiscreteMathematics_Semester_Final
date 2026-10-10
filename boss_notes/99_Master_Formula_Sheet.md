[← Previous: DM-7.2 Relevance of Discrete Mathematics](DM-7_Supplementary/DM-7.2_Relevance_of_DM.md) | [🏠 Index](00_Index.md)

---

# 📐 ECE 2213: Master Formula Sheet
> **Course:** ECE 2213 -- Numerical Methods & Discrete Mathematics | **Credits:** 3.00  
> **Coverage:** All 8 Exam Papers (2017 to 2024) + Class Tests (CT-01 to CT-04)  
> **Scope:** Complete reference of every display equation, recurrence, error bound, and law tested in RUET exams across all 105 subtopics.

---

## ⚡ High-Frequency Quick Reference (Must-Know Formulas)

These 12 formula families account for over 70% of all numerical marks in ECE 2213 exams:

| # | Method / Topic | Formula Summary | Exam Frequency | Key File |
|:---:|---|---|:---:|---|
| 1 | **Lagrange Interpolation** | $P(x) = \sum_{i=0}^n y_i \prod_{j \ne i} \frac{x - x_j}{x_i - x_j}$ | 7/8 years + CT | [NM-4.6](NM-4_Curve_Fitting/NM-4.6_Lagrange_Interpolation.md) |
| 2 | **Gauss-Seidel Iteration** | $x_i^{(k+1)} = \frac{1}{a_{ii}}\left(b_i - \sum_{j < i} a_{ij} x_j^{(k+1)} - \sum_{j > i} a_{ij} x_j^{(k)}\right)$ | 7/8 years + CT | [NM-3.5](NM-3_Linear_Systems/NM-3.5_Gauss_Seidel.md) |
| 3 | **Newton Forward Difference** | $y(x) = y_0 + p\Delta y_0 + \frac{p(p-1)}{2!}\Delta^2 y_0 + \cdots, \quad p = \frac{x-x_0}{h}$ | 6/8 years + CT | [NM-4.7](NM-4_Curve_Fitting/NM-4.7_Newton_Forward_Difference.md) |
| 4 | **Newton-Raphson Method** | $x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}, \quad \text{Order } p = 2$ | 6/8 years | [NM-2.4](NM-2_Root_Finding/NM-2.4_Newton_Raphson.md) |
| 5 | **Bisection Method Bound** | $x_{mid} = \frac{a+b}{2}, \quad n \ge \frac{\ln(b_0-a_0) - \ln\epsilon}{\ln 2}$ | 5/8 years + CT | [NM-2.2](NM-2_Root_Finding/NM-2.2_Bisection_Method.md) |
| 6 | **Runge-Kutta 4th Order (RK4)** | $y_{n+1} = y_n + \frac{1}{6}(k_1 + 2k_2 + 2k_3 + k_4)$ | 5/8 years + CT | [NM-8.5](NM-8_ODE/NM-8.5_RK4.md) |
| 7 | **Simpson 1/3 Rule** | $I \approx \frac{h}{3}[f_0 + 4\sum_{odd} f_i + 2\sum_{even} f_i + f_n], \quad E_t = -\frac{(b-a)h^4}{180}f^{(4)}(\xi)$ | 4/8 years + CT | [NM-5.2](NM-5_Integration/NM-5.2_Simpsons_One_Third.md) |
| 8 | **Laplace 5-Point Stencil** | $u_{i,j} = \frac{1}{4}(u_{i+1,j} + u_{i-1,j} + u_{i,j+1} + u_{i,j-1})$ | 4/8 years | [NM-10.2](NM-10_PDE/NM-10.2_Laplace_Equation.md) |
| 9 | **Pigeonhole Principle** | Plain: $N > k \implies \ge 2$; Generalized: $\ge \lceil N/k \rceil$ | 3/3 DM years | [DM-6.3](DM-6_Counting/DM-6.3_Pigeonhole_Principle.md) |
| 10 | **Binomial Theorem** | $(x+y)^n = \sum_{r=0}^n \binom{n}{r} x^{n-r} y^r, \quad T_{r+1} = \binom{n}{r} x^{n-r} y^r$ | 3/3 DM years | [DM-6.6](DM-6_Counting/DM-6.6_Binomial_Theorem.md) |
| 11 | **Modular Congruence & FLT** | $a^{p-1} \equiv 1 \pmod p \text{ for prime } p \nmid a; \quad ax \equiv b \pmod m$ | 3/3 DM years | [DM-5.4](DM-5_Number_Theory/DM-5.4_Modular_Arithmetic.md) |
| 12 | **Propositional Equivalences** | $p \to q \equiv \neg p \lor q, \quad \neg(p \land q) \equiv \neg p \lor \neg q$ | 4/4 DM sources | [DM-3.2](DM-3_Propositional_Logic/DM-3.2_Connectives_and_Truth_Tables.md) |

---

## Section A: Numerical Methods

### NM-1: Modeling, Computers & Error Analysis

#### True Error, True Fractional Relative Error, and Percentage Relative Error

$$
E_t = \text{True value} - \text{Approximation} = x - \hat{x}
$$

$$
\epsilon_t = \frac{x - \hat{x}}{x}, \qquad |\epsilon_t| = \left|\frac{x - \hat{x}}{x}\right| \times 100\%
$$

- **Symbols:** $x$ = true analytical value, $\hat{x}$ = computed approximation, $E_t$ = true error, $\epsilon_t$ = relative true error.
- **Used in:** [NM-1.4: Error Types](NM-1_Error_Analysis/NM-1.4_Error_Types.md), [NM-5.2: Simpson 1/3 Rule](NM-5_Integration/NM-5.2_Simpsons_One_Third.md)
- **Last tested:** 2023 Q.4(b) [05 marks], 2021 Q.1(b) [04 marks]

#### Approximate Relative Error (Stopping Criterion)

$$
|\epsilon_a| = \left|\frac{x_{current} - x_{previous}}{x_{current}}\right| \times 100\% < \epsilon_s
$$

$$
\epsilon_s = (0.5 \times 10^{2-n})\% \quad (\text{Scarborough criterion for } n \text{ significant figures})
$$

- **Symbols:** $x_{current}$ = iterate at step $k$, $x_{previous}$ = iterate at step $k-1$, $\epsilon_s$ = pre-set stopping tolerance, $n$ = required correct digits.
- **Used in:** [NM-1.5: Error Propagation](NM-1_Error_Analysis/NM-1.5_Error_Propagation.md), [NM-2.2: Bisection Method](NM-2_Root_Finding/NM-2.2_Bisection_Method.md)
- **Last tested:** 2018 Q.2(a) [04 marks]

#### Taylor Series Expansion with Lagrange Remainder

$$
f(x_{i+1}) = f(x_i) + f'(x_i)h + \frac{f''(x_i)}{2!}h^2 + \cdots + \frac{f^{(n)}(x_i)}{n!}h^n + R_n
$$

$$
R_n = \frac{f^{(n+1)}(\xi)}{(n+1)!}h^{n+1}, \qquad \xi \in [x_i, x_{i+1}]
$$

- **Symbols:** $h = x_{i+1} - x_i$ = step size, $R_n$ = truncation error of order $O(h^{n+1})$, $\xi$ = intermediate point.
- **Used in:** [NM-1.6: Taylor Series](NM-1_Error_Analysis/NM-1.6_Taylor_Series.md)
- **Last tested:** 2024 Q.1(b) [05 marks], 2021 Q.1(c) [05 marks]

#### Multivariate Error Propagation (Total Differential)

$$
\Delta u \approx \sum_{i=1}^n \left|\frac{\partial u}{\partial x_i}\right| \Delta x_i
$$

$$
\frac{\Delta u}{u} \approx \sum_{i=1}^n \left|\frac{\partial \ln u}{\partial x_i}\right| \Delta x_i = \sum_{i=1}^n \left|\frac{1}{u}\frac{\partial u}{\partial x_i}\right| \Delta x_i
$$

- **Symbols:** $u = f(x_1, x_2, \dots, x_n)$ = function of measurements, $\Delta x_i$ = absolute uncertainty in variable $x_i$, $\Delta u$ = maximum propagated error.
- **Used in:** [NM-1.5: Error Propagation](NM-1_Error_Analysis/NM-1.5_Error_Propagation.md)
- **Last tested:** 2023 Q.1(b) [04 marks], 2021 Q.1(a) [04 marks]

---

### NM-2: Roots of Equations

#### Bisection Method

$$
x_{m} = \frac{a + b}{2}
$$

$$
n \ge \frac{\ln(b_0 - a_0) - \ln \epsilon}{\ln 2} = \frac{\log_{10}(b_0 - a_0) - \log_{10} \epsilon}{\log_{10} 2}
$$

- **Symbols:** $[a, b]$ = bracketing interval where $f(a)f(b) < 0$, $x_m$ = midpoint, $n$ = minimum iterations to guarantee absolute error $< \epsilon$.
- **Convergence:** Linear ($p = 1$), error halves at each iteration ($\epsilon_{k+1} = 0.5 \epsilon_k$).
- **Used in:** [NM-2.2: Bisection Method](NM-2_Root_Finding/NM-2.2_Bisection_Method.md)
- **Last tested:** 2022 Q.1(b) [05 marks], 2019 Q.2(a) [05 marks]

#### Regula Falsi (False Position) Formula

$$
x_r = \frac{a f(b) - b f(a)}{f(b) - f(a)} = b - \frac{f(b)(b - a)}{f(b) - f(a)}
$$

- **Symbols:** $[a, b]$ = bracket where $f(a)f(b) < 0$, $x_r$ = root approximation from secant line $x$-intercept.
- **Illinois Modification:** If endpoint $a$ stalls for 2 successive steps, replace $f(a)$ with $\frac{1}{2}f(a)$ to force the step to cross over.
- **Used in:** [NM-2.3: False Position](NM-2_Root_Finding/NM-2.3_False_Position.md)
- **Last tested:** 2021 Q.2(b) [05 marks], CT-01 Q.2(a, b)

#### Newton-Raphson Iteration & Convergence Order

$$
x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}
$$

$$
\epsilon_{n+1} \approx \frac{f''(r)}{2f'(r)} \epsilon_n^2 \quad (\text{Quadratic convergence: } p = 2)
$$

- **Symbols:** $x_n$ = current estimate, $f'(x_n) \ne 0$ = first derivative, $r$ = exact simple root.
- **Failure Conditions:** $f'(x_n) \approx 0$ (division by zero), inflection points ($f''(x) = 0$), local extrema, cycle or oscillation.
- **Used in:** [NM-2.4: Newton-Raphson](NM-2_Root_Finding/NM-2.4_Newton_Raphson.md), [NM-2.6: Method Comparison](NM-2_Root_Finding/NM-2.6_Method_Comparison.md)
- **Last tested:** 2024 Q.2(a) [05 marks], 2023 Q.2(a) [04 marks]

#### Secant Method

$$
x_{i+1} = x_i - \frac{f(x_i)(x_i - x_{i-1})}{f(x_i) - f(x_{i-1})}
$$

- **Symbols:** $x_i, x_{i-1}$ = two most recent iterates (no bracketing required).
- **Convergence:** Superlinear ($p = \frac{1+\sqrt{5}}{2} \approx 1.618$).
- **Used in:** [NM-2.5: Secant Method](NM-2_Root_Finding/NM-2.5_Secant_Method.md)
- **Last tested:** 2020 Q.2(b) [04 marks], 2017 Q.2(c) [04 marks]

#### Descartes' Rule of Signs & Smallest Root Scans

$$
\text{Max positive real roots} = \text{sign changes of } P(x)
$$

$$
\text{Max negative real roots} = \text{sign changes of } P(-x)
$$

- **Used in:** [NM-2.7: Polynomial Roots](NM-2_Root_Finding/NM-2.7_Polynomial_Roots.md)
- **Last tested:** 2021 Q.2(c) [06 marks], 2019 Q.2(b) [04 marks]

---

### NM-3: Linear Algebraic Equations

#### Gauss Elimination Back-Substitution & Multipliers

$$
m_{ik} = \frac{a_{ik}^{(k)}}{a_{kk}^{(k)}} \quad (\text{multiplier for row } i \text{ using pivot row } k)
$$

$$
x_i = \frac{b_i - \sum_{j=i+1}^n a_{ij} x_j}{a_{ii}} \quad (\text{back-substitution for upper triangular system})
$$

- **Symbols:** $a_{kk}$ = pivot element, $m_{ik}$ = multiplier, $[A|b]$ = augmented matrix.
- **Partial Pivoting:** Swap row $k$ with row $p \ge k$ such that $|a_{pk}| = \max_{i \ge k} |a_{ik}|$.
- **Used in:** [NM-3.1: Gauss Elimination](NM-3_Linear_Systems/NM-3.1_Gauss_Elimination.md), [NM-3.2: Pivoting](NM-3_Linear_Systems/NM-3.2_Pivoting.md)
- **Last tested:** 2022 Q.4(b) [05 marks], 2020 Q.4(a) [04 marks], 2019 Q.3(a) [04 marks]

#### LU Decomposition (Doolittle vs Crout)

$$
A = L U
$$

$$
\text{Doolittle: } l_{ii} = 1 \text{ (unit lower)}, \qquad \text{Crout: } u_{ii} = 1 \text{ (unit upper)}
$$

$$
L y = b \quad (\text{forward substitution}), \qquad U x = y \quad (\text{back-substitution})
$$

- **Symbols:** $A$ = square coefficient matrix, $L$ = unit lower triangular factor, $U$ = unit upper triangular factor, $b$ = right-hand side vector, $y$ = intermediate forward-substitution vector.
- **Used in:** [NM-3.3: LU Decomposition](NM-3_Linear_Systems/NM-3.3_LU_Decomposition.md)
- **Last tested:** 2017 Q.4(b) [05 marks]

#### Jacobi Iteration Scheme

$$
x_i^{(k+1)} = \frac{1}{a_{ii}} \left( b_i - \sum_{j \ne i} a_{ij} x_j^{(k)} \right)
$$

- **Symbols:** Uses all old iterates $x_j^{(k)}$ from the previous iteration.
- **Used in:** [NM-3.4: Jacobi Iteration](NM-3_Linear_Systems/NM-3.4_Jacobi_Iteration.md)
- **Last tested:** 2022 Q.4(a) [05 marks], 2017 Q.7(a) [05 marks]

#### Gauss-Seidel Iteration Scheme & Convergence

$$
x_i^{(k+1)} = \frac{1}{a_{ii}} \left( b_i - \sum_{j < i} a_{ij} x_j^{(k+1)} - \sum_{j > i} a_{ij} x_j^{(k)} \right)
$$

- **Symbols:** Immediately substitutes newly updated variables $x_j^{(k+1)}$ for $j < i$.
- **Strict Diagonal Dominance Condition for Guaranteed Convergence:**

$$
|a_{ii}| > \sum_{j \ne i} |a_{ij}| \quad \text{for all } i = 1, 2, \dots, n
$$

- **Used in:** [NM-3.5: Gauss-Seidel](NM-3_Linear_Systems/NM-3.5_Gauss_Seidel.md), [NM-3.8: Circuit Applications](NM-3_Linear_Systems/NM-3.8_Circuit_Applications.md)
- **Last tested:** 2024 Q.2(b) [04 marks], 2021 Q.7(b) [06 marks], 2020 Q.4(b) [05 marks]

#### Successive Over-Relaxation (SOR) Formula

$$
x_i^{(k+1)} = (1 - \omega) x_i^{(k)} + \frac{\omega}{a_{ii}} \left( b_i - \sum_{j < i} a_{ij} x_j^{(k+1)} - \sum_{j > i} a_{ij} x_j^{(k)} \right)
$$

- **Symbols:** $\omega$ = relaxation parameter ($0 < \omega < 1$: under-relaxation to dampen oscillations, $1 < \omega < 2$: over-relaxation to accelerate convergence).
- **Used in:** [NM-3.6: Relaxation](NM-3_Linear_Systems/NM-3.6_Relaxation.md)
- **Last tested:** 2018 Q.4(a) [03 marks], 2017 Q.4(c) [05 marks]

#### Matrix Condition Number & Ill-Conditioning

$$
\kappa(A) = \|A\| \cdot \|A^{-1}\| \ge 1
$$

- **Symbols:** $\kappa(A)$ = condition number. If $\kappa(A) \gg 1$, system is ill-conditioned; small input disturbances cause wild solution swings.
- **Used in:** [NM-3.7: Ill-Conditioned Systems](NM-3_Linear_Systems/NM-3.7_Ill_Conditioned_Systems.md)
- **Last tested:** 2022 Q.4(c) [02 marks]

---

### NM-4: Interpolation & Curve Fitting

#### Least-Squares Linear Regression ($y = a_0 + a_1 x$)

$$
\begin{bmatrix} n & \sum x_i \\ \sum x_i & \sum x_i^2 \end{bmatrix} \begin{bmatrix} a_0 \\ a_1 \end{bmatrix} = \begin{bmatrix} \sum y_i \\ \sum x_i y_i \end{bmatrix}
$$

$$
a_1 = \frac{n \sum x_i y_i - \sum x_i \sum y_i}{n \sum x_i^2 - (\sum x_i)^2}, \qquad a_0 = \bar{y} - a_1 \bar{x}
$$

- **Symbols:** $n$ = number of data points, $x_i, y_i$ = data points, $a_0$ = intercept, $a_1$ = slope, $\bar{x}, \bar{y}$ = means.
- **Used in:** [NM-4.2: Linear Regression](NM-4_Curve_Fitting/NM-4.2_Linear_Regression.md), [NM-4.1: Concepts](NM-4_Curve_Fitting/NM-4.1_Concepts.md)
- **Last tested:** 2024 Q.3(c) [05 marks], 2018 Q.4(c) [05 marks], 2017 Q.6(b) [04 marks]

#### Non-Linear Transformations for Least-Squares

| Model | Form | Transformation | Transformed Linear Form | Recovered Parameters |
|:---|:---|:---|:---|:---|
| **Exponential** | $y = a e^{bx}$ | Take $\ln$ | $\ln y = \ln a + bx$ | $Y = A + bX, \quad a = e^A$ |
| **Power** | $y = a x^b$ | Take $\log$ | $\log y = \log a + b \log x$ | $Y = A + bX, \quad a = 10^A$ |
| **Saturation-Growth** | $y = \frac{x}{a + bx}$ | Invert ($1/y$) | $\frac{1}{y} = a\left(\frac{1}{x}\right) + b$ | $Y = a X + b, \quad Y = 1/y, X = 1/x$ |

- **Symbols:** $X, Y$ = linearized variables, $A, b$ = linear regression coefficients, $a, b$ = original model parameters.
- **Used in:** [NM-4.3: Nonlinear Regression](NM-4_Curve_Fitting/NM-4.3_Nonlinear_Regression.md)
- **Last tested:** 2022 Q.2(b) [05 marks], 2020 Q.3(c) [04 marks], 2017 Q.5(b) [04 marks]

#### Lagrange Interpolation Formula

$$
P_n(x) = \sum_{i=0}^n y_i L_i(x) = \sum_{i=0}^n y_i \prod_{\substack{j=0 \\ j \ne i}}^n \frac{x - x_j}{x_i - x_j}
$$

$$
L_i(x_k) = \delta_{ik} = \begin{cases} 1 & \text{if } i = k \\ 0 & \text{if } i \ne k \end{cases}, \qquad \sum_{i=0}^n L_i(x) = 1 \quad (\text{Partition of Unity})
$$

- **Symbols:** Operates on arbitrarily spaced nodes $x_0, x_1, \dots, x_n$.
- **Used in:** [NM-4.6: Lagrange Interpolation](NM-4_Curve_Fitting/NM-4.6_Lagrange_Interpolation.md)
- **Last tested:** 2024 Q.2(c) [05 marks], 2023 Q.2(b) [04 marks], CT-02A Q.1

#### Difference Operators & Fundamental Identities

$$
\Delta f_i = f_{i+1} - f_i \quad (\text{forward}), \qquad \nabla f_i = f_i - f_{i-1} \quad (\text{backward})
$$

$$
\delta f_i = f_{i+1/2} - f_{i-1/2} \quad (\text{central}), \qquad E f_i = f_{i+1} \quad (\text{shift})
$$

$$
E = 1 + \Delta = (1 - \nabla)^{-1} = e^{h D}, \qquad \Delta = E \nabla = \nabla E
$$

- **Symbols:** $\Delta$ = forward difference, $\nabla$ = backward difference, $\delta$ = central difference, $E$ = shift operator, $D$ = derivative operator, $h$ = step size.
- **Used in:** [NM-4.11: Difference Tables](NM-4_Curve_Fitting/NM-4.11_Difference_Tables.md)
- **Last tested:** 2024 Q.3(b) [04 marks], 2022 Q.2(c) [04 marks], 2020 Q.5(a) [04 marks]

#### Newton Forward Difference Interpolation

$$
y(x) = y_0 + p \Delta y_0 + \frac{p(p-1)}{2!} \Delta^2 y_0 + \frac{p(p-1)(p-2)}{3!} \Delta^3 y_0 + \cdots
$$

$$
p = \frac{x - x_0}{h}
$$

- **Condition:** Equispaced points with step $h$, interpolating near beginning of table ($0 < p < 1$).
- **Used in:** [NM-4.7: Newton Forward Difference](NM-4_Curve_Fitting/NM-4.7_Newton_Forward_Difference.md)
- **Last tested:** 2023 Q.2(a) [05 marks], 2021 Q.3(c) [05 marks], 2020 Q.5(a) [05 marks], CT-02A Q.2

#### Newton Backward Difference Interpolation

$$
y(x) = y_n + p \nabla y_n + \frac{p(p+1)}{2!} \nabla^2 y_n + \frac{p(p+1)(p+2)}{3!} \nabla^3 y_n + \cdots
$$

$$
p = \frac{x - x_n}{h}
$$

- **Condition:** Equispaced points with step $h$, interpolating near end of table ($-1 < p < 0$).
- **Used in:** [NM-4.8: Newton Backward Difference](NM-4_Curve_Fitting/NM-4.8_Newton_Backward_Difference.md)
- **Last tested:** 2024 Q.3(b) [05 marks], 2020 Q.3(b) [05 marks], 2017 Q.5(c) [05 marks]

#### Newton Divided Difference Interpolation

$$
f[x_0, x_1] = \frac{f(x_1) - f(x_0)}{x_1 - x_0}, \qquad f[x_0, x_1, x_2] = \frac{f[x_1, x_2] - f[x_0, x_1]}{x_2 - x_0}
$$

$$
P_n(x) = f[x_0] + (x - x_0)f[x_0, x_1] + (x - x_0)(x - x_1)f[x_0, x_1, x_2] + \dots
$$

- **Condition:** Unequally spaced data. Order-independent divided difference tables.
- **Used in:** [NM-4.9: Divided Difference](NM-4_Curve_Fitting/NM-4.9_Divided_Difference.md)
- **Last tested:** 2022 Q.2(a) [03 marks], 2020 Q.5(b) [05 marks], 2019 Q.5(c) [05 marks]

#### Central Difference Formulas (Gauss & Stirling)

$$
\text{Gauss Forward: } y_p = y_0 + p\Delta y_0 + \frac{p(p-1)}{2!}\Delta^2 y_{-1} + \frac{(p+1)p(p-1)}{3!}\Delta^3 y_{-1} + \cdots
$$

$$
\text{Gauss Backward: } y_p = y_0 + p\Delta y_{-1} + \frac{p(p+1)}{2!}\Delta^2 y_{-1} + \frac{(p+1)p(p-1)}{3!}\Delta^3 y_{-2} + \cdots
$$

$$
\text{Stirling: } y_p = y_0 + p \left(\frac{\Delta y_{-1} + \Delta y_0}{2}\right) + \frac{p^2}{2} \Delta^2 y_{-1} + \frac{p(p^2-1)}{3!} \left(\frac{\Delta^3 y_{-1} + \Delta^3 y_{-2}}{2}\right) + \cdots
$$

- **Condition:** Interpolating near center of table ($-0.5 \le p \le 0.5$).
- **Used in:** [NM-4.10: Gauss and Stirling](NM-4_Curve_Fitting/NM-4.10_Gauss_and_Stirling.md)
- **Last tested:** 2021 Q.4(b) [05 marks]

---

### NM-5: Numerical Integration

#### Trapezoidal Rule (Single & Composite)

$$
\text{Single: } I \approx \frac{h}{2}[f(a) + f(b)], \qquad E_t = -\frac{h^3}{12} f''(\xi)
$$

$$
\text{Composite: } I \approx \frac{h}{2}\left[ f_0 + 2\sum_{i=1}^{n-1} f_i + f_n \right], \qquad E_t = -\frac{(b-a)h^2}{12} f''(\xi)
$$

- **Degree of precision:** 1 (exact for linear polynomials).
- **Symbols:** $h = (b-a)/n$ = step size, $n$ = segment count, $\xi \in [a, b]$.
- **Used in:** [NM-5.1: Trapezoidal Rule](NM-5_Integration/NM-5.1_Trapezoidal_Rule.md)
- **Last tested:** 2022 Q.1(d) [04 marks], 2021 Q.6(a) [05 marks], 2018 Q.5(b) [04 marks]

#### Simpson 1/3 Rule (Single & Composite)

$$
\text{Single } (n=2): I \approx \frac{h}{3}[f_0 + 4f_1 + f_2], \qquad E_t = -\frac{h^5}{90} f^{(4)}(\xi)
$$

$$
\text{Composite (even } n): I \approx \frac{h}{3}\left[ f_0 + 4\sum_{i=1,3,\dots}^{n-1} f_i + 2\sum_{i=2,4,\dots}^{n-2} f_i + f_n \right], \qquad E_t = -\frac{(b-a)h^4}{180} f^{(4)}(\xi)
$$

- **Degree of precision:** 3 (exact for polynomials up to degree 3, despite using parabolas).
- **Constraint:** Segment count $n$ must be even (number of nodes $n+1$ is odd).
- **Used in:** [NM-5.2: Simpson 1/3 Rule](NM-5_Integration/NM-5.2_Simpsons_One_Third.md)
- **Last tested:** 2023 Q.4(b) [05 marks], 2020 Q.6(b) [06 marks], 2018 Q.6(a) [08 marks]

#### Simpson 3/8 Rule

$$
I \approx \frac{3h}{8}\left[ f_0 + 3f_1 + 3f_2 + 2f_3 + 3f_4 + 3f_5 + \cdots + f_n \right], \qquad E_t = -\frac{(b-a)h^4}{80} f^{(4)}(\xi)
$$

- **Constraint:** Segment count $n$ must be a multiple of 3.
- **Used in:** [NM-5.3: Simpson 3/8 Rule](NM-5_Integration/NM-5.3_Simpsons_Three_Eighth.md), [NM-5.4: Rule Comparison](NM-5_Integration/NM-5.4_Rule_Comparison.md)
- **Last tested:** 2019 Q.7(b) [05 marks]

#### Romberg Integration

$$
I_{j,k} = \frac{4^{k-1} I_{j+1,k-1} - I_{j,k-1}}{4^{k-1} - 1}
$$

- **Extrapolation order:** Column $k=1 \implies O(h^2)$, $k=2 \implies O(h^4)$, $k=3 \implies O(h^6)$.
- **Used in:** [NM-5.5: Romberg Method](NM-5_Integration/NM-5.5_Rombergs_Method.md)
- **Last tested:** 2023 Q.2(c) [04 marks], 2021 Q.8(b) [06 marks]

---

### NM-6: Optimization

#### Golden Section Search

$$
r = \frac{\sqrt{5} - 1}{2} \approx 0.618034 \quad (\text{golden ratio conjugate})
$$

$$
x_1 = b - r(b - a), \qquad x_2 = a + r(b - a)
$$

- **Rule for 1D Maximum:** If $f(x_1) > f(x_2)$, new interval is $[a, x_2]$. If $f(x_2) > f(x_1)$, new interval is $[x_1, b]$.
- **Interval Reduction:** After $k$ iterations, interval width is $L_k = r^k (b - a)$.
- **Used in:** [NM-6.2: Unconstrained Optimization](NM-6_Optimization/NM-6.2_Unconstrained_Optimization.md)
- **Last tested:** 2020 Q.7(b) [04 marks], 2018 Q.6(c) [05 marks]

#### 1D Newton Optimization for Extrema

$$
x_{n+1} = x_n - \frac{f'(x_n)}{f''(x_n)}
$$

- **Optimality Condition:** $f'(x^*) = 0$. Local minimum if $f''(x^*) > 0$, local maximum if $f''(x^*) < 0$.
- **Used in:** [NM-6.2: Unconstrained Optimization](NM-6_Optimization/NM-6.2_Unconstrained_Optimization.md)

---

### NM-7: Numerical Differentiation

#### Finite Difference Approximations of Derivatives

$$
\text{Forward } O(h): f'(x_i) \approx \frac{f(x_{i+1}) - f(x_i)}{h}
$$

$$
\text{Backward } O(h): f'(x_i) \approx \frac{f(x_i) - f(x_{i-1})}{h}
$$

$$
\text{Central } O(h^2): f'(x_i) \approx \frac{f(x_{i+1}) - f(x_{i-1})}{2h}
$$

$$
\text{Central 2nd Derivative } O(h^2): f''(x_i) \approx \frac{f(x_{i+1}) - 2f(x_i) + f(x_{i-1})}{h^2}
$$

- **Symbols:** $h$ = step size, $f_i$ = tabulated value.
- **Used in:** [NM-7.1: Difference Formulas](NM-7_Differentiation/NM-7.1_Difference_Formulas.md), [NM-7.2: First Derivative](NM-7_Differentiation/NM-7.2_First_Derivative.md), [NM-7.3: Second Derivative](NM-7_Differentiation/NM-7.3_Second_Derivative.md)
- **Last tested:** 2022 Q.3(b) [05 marks], 2021 Q.7(c) [04 marks], 2020 Q.6(c) [04 marks], 2019 Q.6(b) [04 marks]

---

### NM-8: Ordinary Differential Equations (IVP & BVP)

#### Euler Method

$$
y_{i+1} = y_i + h f(x_i, y_i)
$$

- **Error:** Local truncation error $O(h^2)$, global error $O(h)$.
- **Used in:** [NM-8.2: Euler Method](NM-8_ODE/NM-8.2_Eulers_Method.md)
- **Last tested:** 2021 Q.8(c) [05 marks], 2018 Q.7(b) [04 marks], 2017 Q.7(c) [05 marks]

#### Heun Method (Improved Euler / Predictor-Corrector)

$$
\tilde{y}_{i+1} = y_i + h f(x_i, y_i) \quad (\text{predictor})
$$

$$
y_{i+1} = y_i + \frac{h}{2}[f(x_i, y_i) + f(x_{i+1}, \tilde{y}_{i+1})] \quad (\text{corrector})
$$

- **Error:** Global error $O(h^2)$.
- **Used in:** [NM-8.3: Heun Method](NM-8_ODE/NM-8.3_Heuns_Method.md)
- **Last tested:** 2020 Q.7(c) [05 marks], 2017 Q.8(b) [05 marks]

#### Second-Order Runge-Kutta (RK2 Midpoint)

$$
k_1 = h f(x_n, y_n), \qquad k_2 = h f\left(x_n + \frac{h}{2}, y_n + \frac{k_1}{2}\right)
$$

$$
y_{n+1} = y_n + k_2
$$

- **Used in:** [NM-8.4: RK2](NM-8_ODE/NM-8.4_RK2.md)
- **Last tested:** CT-02B Q.2(a)

#### Runge-Kutta 4th Order (Classical RK4)

$$
y_{n+1} = y_n + \frac{1}{6}(k_1 + 2k_2 + 2k_3 + k_4)
$$

$$
\begin{cases}
k_1 = h f(x_n, y_n) \\
k_2 = h f\left(x_n + \frac{h}{2}, y_n + \frac{k_1}{2}\right) \\
k_3 = h f\left(x_n + \frac{h}{2}, y_n + \frac{k_2}{2}\right) \\
k_4 = h f(x_n + h, y_n + k_3)
\end{cases}
$$

- **Error:** Global error $O(h^4)$, matches Taylor expansion through $h^4$ without evaluating higher derivatives.
- **Used in:** [NM-8.5: RK4](NM-8_ODE/NM-8.5_RK4.md)
- **Last tested:** 2024 Q.4(b) [06 marks], 2022 Q.4(d) [06 marks], 2021 Q.5(b) [06 marks], 2018 Q.8(a) [05 marks]

#### Higher-Order ODE Reduction to First-Order Systems

$$
y'' + P(x)y' + Q(x)y = R(x) \implies \begin{cases} u_1 = y \\ u_2 = y' \end{cases} \implies \begin{cases} u_1' = u_2 \\ u_2' = R(x) - P(x)u_2 - Q(x)u_1 \end{cases}
$$

- **Used in:** [NM-8.6: Higher Order Systems](NM-8_ODE/NM-8.6_Higher_Order_Systems.md)
- **Last tested:** 2023 Q.3(b) [05 marks], 2020 Q.7(a) [05 marks], 2018 Q.7(a) [05 marks]

#### Boundary Value Problems (Finite Difference Stencil)

$$
y''(x_i) \approx \frac{y_{i+1} - 2y_i + y_{i-1}}{h^2}, \qquad y'(x_i) \approx \frac{y_{i+1} - y_{i-1}}{2h}
$$

- **Used in:** [NM-8.8: Boundary Value Problems](NM-8_ODE/NM-8.8_Boundary_Value_Problems.md)
- **Last tested:** 2021 Q.5(a) [04 marks]

---

### NM-9: Eigenvalues & Eigenvectors

#### Characteristic Polynomial & Power Method

$$
\det(A - \lambda I) = 0
$$

$$
\mathbf{x}^{(k+1)} = \frac{A \mathbf{x}^{(k)}}{\|A \mathbf{x}^{(k)}\|_\infty} \quad (\text{Power Method for dominant eigenvalue } \lambda_1)
$$

$$
\lambda \approx \frac{\mathbf{x}^T A \mathbf{x}}{\mathbf{x}^T \mathbf{x}} \quad (\text{Rayleigh Quotient})
$$

- **Properties:** $\sum \lambda_i = \operatorname{tr}(A)$, $\prod \lambda_i = \det(A)$.
- **Used in:** [NM-9.1: Eigenvalues and Eigenvectors](NM-9_Eigenvalues/NM-9.1_Eigenvalues_and_Eigenvectors.md)
- **Last tested:** 2023 Q.3(a) [04 marks], 2021 Q.6(b) [04 marks]

---

### NM-10: Partial Differential Equations

#### PDE Classification Criterion ($A u_{xx} + B u_{xy} + C u_{yy} + \dots = 0$)

$$
B^2 - 4AC < 0 \implies \text{Elliptic (Laplace, Poisson)}
$$

$$
B^2 - 4AC = 0 \implies \text{Parabolic (Heat / Diffusion equation)}
$$

$$
B^2 - 4AC > 0 \implies \text{Hyperbolic (Wave equation)}
$$

- **Used in:** [NM-10.1: Classification](NM-10_PDE/NM-10.1_Classification.md)
- **Last tested:** 2020 Q.8(a) [05 marks]

#### Five-Point Stencils on Square Mesh ($h = k$)

$$
\text{Laplace: } u_{i,j} = \frac{1}{4}(u_{i+1,j} + u_{i-1,j} + u_{i,j+1} + u_{i,j-1})
$$

$$
\text{Poisson: } u_{i+1,j} + u_{i-1,j} + u_{i,j+1} + u_{i,j-1} - 4u_{i,j} = -h^2 f(x_i, y_j)
$$

- **Liebmann Iteration:** Gauss-Seidel iterative updating of Laplace stencil over interior nodes:

$$
u_{i,j}^{(k+1)} = (1 - \lambda)u_{i,j}^{(k)} + \frac{\lambda}{4}\left(u_{i+1,j}^{(k)} + u_{i-1,j}^{(k+1)} + u_{i,j+1}^{(k)} + u_{i,j-1}^{(k+1)}\right)
$$

- **Used in:** [NM-10.2: Laplace Equation](NM-10_PDE/NM-10.2_Laplace_Equation.md), [NM-10.3: Poisson Equation](NM-10_PDE/NM-10.3_Poisson_Equation.md), [NM-10.4: Liebmann Method](NM-10_PDE/NM-10.4_Liebmanns_Method.md)
- **Last tested:** 2021 Q.6(c) [06 marks], 2020 Q.8(b) [06 marks], 2019 Q.8(b) [08 marks], 2018 Q.8(b) [06 marks]

---

## Section B: Discrete Mathematics

### DM-1: Set Theory

#### Fundamental Set Operations & Cardinality

$$
A \cup B = \{x \mid x \in A \lor x \in B\}, \qquad A \cap B = \{x \mid x \in A \land x \in B\}
$$

$$
A - B = \{x \mid x \in A \land x \notin B\}, \qquad \bar{A} = \{x \in U \mid x \notin A\}
$$

$$
A \oplus B = (A - B) \cup (B - A) = (A \cup B) - (A \cap B)
$$

$$
|A \times B| = |A| \cdot |B|, \qquad |\mathcal{P}(S)| = 2^{|S|}
$$

- **Symbols:** $A, B$ = sets, $U$ = universal set, $\mathcal{P}(S)$ = power set of $S$, $|S|$ = cardinality.
- **Used in:** [DM-1.1: Set Operations](DM-1_Set_Theory/DM-1.1_Set_Operations.md), [DM-1.4: Power Set](DM-1_Set_Theory/DM-1.4_Power_Set.md)

#### Essential Set Algebraic Identities

$$
\overline{A \cap B} = \bar{A} \cup \bar{B}, \qquad \overline{A \cup B} = \bar{A} \cap \bar{B} \quad (\text{De Morgan Laws})
$$

$$
A \cap (B \cup C) = (A \cap B) \cup (A \cap C), \qquad A \cup (B \cap C) = (A \cup B) \cap (A \cup C) \quad (\text{Distributive Laws})
$$

- **Bit String Representation:** A finite universal set $U = \{x_1, \dots, x_n\}$ maps subset $A$ to bit string where bit $i$ is $1$ if $x_i \in A$, else $0$. Union is bitwise OR, intersection is bitwise AND.
- **Used in:** [DM-1.2: Algebraic Properties](DM-1_Set_Theory/DM-1.2_Algebraic_Properties.md), [DM-1.3: Computer Representation](DM-1_Set_Theory/DM-1.3_Computer_Representation.md)

---

### DM-2: Relations

#### Binary Relation Properties on Set $A$

$$
\text{Reflexive: } \forall x \in A \; (x R x)
$$

$$
\text{Symmetric: } \forall x, y \in A \; (x R y \implies y R x)
$$

$$
\text{Antisymmetric: } \forall x, y \in A \; ((x R y \land y R x) \implies x = y)
$$

$$
\text{Transitive: } \forall x, y, z \in A \; ((x R y \land y R z) \implies x R z)
$$

- **Equivalence Relation:** Reflexive, symmetric, and transitive. Partitions set into disjoint equivalence classes $[a] = \{s \in A \mid a R s\}$.
- **Partial Order (Poset):** Reflexive, antisymmetric, and transitive. Represented visually by Hasse diagrams.
- **Used in:** [DM-2.1: Properties of Relations](DM-2_Relations/DM-2.1_Properties_of_Relations.md), [DM-2.3: Partial Orders](DM-2_Relations/DM-2.3_Partial_Orders.md), [DM-2.4: Equivalence Relations](DM-2_Relations/DM-2.4_Equivalence_Relations.md)

---

### DM-3: Propositional Logic

#### Fundamental Connective Truth Values

| $p$ | $q$ | $\neg p$ | $p \land q$ | $p \lor q$ | $p \oplus q$ | $p \to q$ | $p \leftrightarrow q$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| T | T | F | T | T | F | T | T |
| T | F | F | F | T | T | F | F |
| F | T | T | F | T | T | T | F |
| F | F | T | F | F | F | T | T |

- **Critical Rule:** $p \to q$ is false **only** when $p$ is T and $q$ is F. If $p$ is F, $p \to q$ is vacuously true.
- **Used in:** [DM-3.2: Connectives & Truth Tables](DM-3_Propositional_Logic/DM-3.2_Connectives_and_Truth_Tables.md)
- **Last tested:** 2024 Q.7(b) [04 marks], 2022 Q.6(b) [04 marks], CT-04 Q.2(c)

#### Essential Logical Equivalences

$$
p \to q \equiv \neg p \lor q \equiv \neg q \to \neg p \quad (\text{contrapositive})
$$

$$
\neg(p \land q) \equiv \neg p \lor \neg q, \qquad \neg(p \lor q) \equiv \neg p \land \neg q \quad (\text{De Morgan Laws})
$$

$$
p \land (q \lor r) \equiv (p \land q) \lor (p \land r), \qquad p \lor (q \land r) \equiv (p \lor q) \land (p \lor r) \quad (\text{Distributive Laws})
$$

$$
p \leftrightarrow q \equiv (p \to q) \land (q \to p) \equiv (\neg p \lor q) \land (\neg q \lor p) \equiv (p \land q) \lor (\neg p \land \neg q)
$$

- **Used in:** [DM-3.3: Tautology & Contradiction](DM-3_Propositional_Logic/DM-3.3_Tautology_and_Contradiction.md), [DM-3.5: Logical Equivalence](DM-3_Propositional_Logic/DM-3.5_Logical_Equivalence.md)
- **Last tested:** 2024 Q.6(a) [04 marks], 2023 Q.5(c) [04 marks], 2023 Q.6(a) [03 marks]

#### Conjunctive & Disjunctive Normal Forms (CNF / DNF)

$$
A \equiv \bigwedge_{i=1}^{m} \left( \bigvee_{j=1}^{n} l_{ij} \right) \quad (\text{CNF: conjunction of disjunctive clauses})
$$

$$
A \equiv \bigvee_{i=1}^{m} \left( \bigwedge_{j=1}^{n} l_{ij} \right) \quad (\text{DNF: disjunction of conjunctive minterms})
$$

- **Used in:** [DM-3.8: Normal Forms](DM-3_Propositional_Logic/DM-3.8_Normal_Forms.md)
- **Last tested:** 2022 Q.5(c) [02 marks], CT-04 Q.2(b)

#### Functional Completeness (NAND & NOR)

$$
\neg p \equiv p \uparrow p \equiv p \downarrow p
$$

$$
p \land q \equiv (p \uparrow q) \uparrow (p \uparrow q) \equiv (p \downarrow p) \downarrow (q \downarrow q)
$$

$$
p \lor q \equiv (p \uparrow p) \uparrow (q \uparrow q) \equiv (p \downarrow q) \downarrow (p \downarrow q)
$$

- **Used in:** [DM-3.8: Normal Forms](DM-3_Propositional_Logic/DM-3.8_Normal_Forms.md)
- **Last tested:** 2022 Q.5(c) [03 marks]

#### Core Rules of Inference

$$
\begin{array}{r l r l}
\text{Modus Ponens:} & \frac{p,\; p \to q}{\therefore q} & \text{Modus Tollens:} & \frac{\neg q,\; p \to q}{\therefore \neg p} \\
\text{Hypothetical Syllogism:} & \frac{p \to q,\; q \to r}{\therefore p \to r} & \text{Disjunctive Syllogism:} & \frac{p \lor q,\; \neg p}{\therefore q} \\
\text{Resolution:} & \frac{p \lor q,\; \neg p \lor r}{\therefore q \lor r} & \text{Universal Instantiation:} & \frac{\forall x\, P(x)}{\therefore P(c)}
\end{array}
$$

- **Used in:** [DM-3.9: Rules of Inference](DM-3_Propositional_Logic/DM-3.9_Rules_of_Inference.md)
- **Last tested:** 2024 Q.5(a) [03 marks], 2022 Q.6(a) [04 marks]

---

### DM-4: Proof Techniques

#### Proof Structures & Frameworks

$$
\text{Direct Proof of } p \to q: \quad \text{Assume } p \text{ is True} \implies \dots \implies \text{Deduce } q \text{ is True}
$$

$$
\text{Proof by Contraposition: } \quad \text{Assume } \neg q \text{ is True} \implies \dots \implies \text{Deduce } \neg p \text{ is True}
$$

$$
\text{Proof by Contradiction: } \quad \text{Assume } p \land \neg q \text{ is True} \implies \dots \implies \text{Deduce } r \land \neg r \text{ (Contradiction)}
$$

$$
\text{Mathematical Induction: } \quad [P(1) \land \forall k (P(k) \to P(k+1))] \implies \forall n \ge 1 \; P(n)
$$

- **Used in:** [DM-4.2: Direct Proofs](DM-4_Proof_Techniques/DM-4.2_Direct_Proofs.md), [DM-4.3: Contradiction](DM-4_Proof_Techniques/DM-4.3_Proof_by_Contradiction.md), [DM-4.4: Contraposition](DM-4_Proof_Techniques/DM-4.4_Proof_by_Contraposition.md), [DM-4.5: Mathematical Induction](DM-4_Proof_Techniques/DM-4.5_Mathematical_Induction.md)

---

### DM-5: Number Theory

#### Division Algorithm & Modular Congruence

$$
a = d q + r, \qquad 0 \le r < d
$$

$$
a \equiv b \pmod m \iff m \mid (a - b) \iff a \bmod m = b \bmod m
$$

$$
(a + b) \bmod m = ((a \bmod m) + (b \bmod m)) \bmod m
$$

$$
(a \cdot b) \bmod m = ((a \bmod m) \cdot (b \bmod m)) \bmod m
$$

- **Used in:** [DM-5.1: Divisibility](DM-5_Number_Theory/DM-5.1_Divisibility.md), [DM-5.4: Modular Arithmetic](DM-5_Number_Theory/DM-5.4_Modular_Arithmetic.md)
- **Last tested:** 2024 Q.8(a) [04 marks], 2023 Q.7(a) [04 marks], 2022 Q.7(a) [03 marks]

#### Prime Divisor Bound Theorem

$$
n \text{ is composite} \implies \exists \text{ prime } p \le \sqrt{n} \text{ such that } p \mid n
$$

- **Used in:** [DM-5.2: Prime Numbers](DM-5_Number_Theory/DM-5.2_Prime_Numbers.md), [DM-5.9: Number Proofs](DM-5_Number_Theory/DM-5.9_Number_Proofs.md)
- **Last tested:** 2023 Q.7(c) [03 marks]

#### Euclidean Algorithm & Extended Euclidean Algorithm (Bézout Identity)

$$
\gcd(a, b) = \gcd(b, a \bmod b), \qquad \gcd(a, 0) = a
$$

$$
\gcd(a, b) = s \cdot a + t \cdot b \quad (s, t \in \mathbb{Z} \text{ are Bézout coefficients})
$$

- **Modular Inverse:** If $\gcd(a, m) = 1$, then $s \cdot a \equiv 1 \pmod m$, so $a^{-1} \equiv s \pmod m$.
- **Used in:** [DM-5.3: GCD and Euclidean](DM-5_Number_Theory/DM-5.3_GCD_and_Euclidean.md)
- **Last tested:** 2022 Q.7(c) [02 marks]

#### Fast Modular Exponentiation (Repeated Squaring)

$$
b = \sum_{i=0}^{k-1} a_i 2^i \implies x^b \equiv \prod_{a_i = 1} x^{2^i} \pmod m
$$

- **Used in:** [DM-5.5: Modular Exponentiation](DM-5_Number_Theory/DM-5.5_Modular_Exponentiation.md)
- **Last tested:** 2024 Q.8(b) [04 marks], 2022 Q.7(b) [03 marks]

#### Fermat Little Theorem (FLT)

$$
a^{p-1} \equiv 1 \pmod p \quad \text{if } p \text{ is prime and } p \nmid a
$$

$$
a^p \equiv a \pmod p \quad \text{for all integers } a
$$

- **Exponent Reduction Technique:** To compute $a^b \bmod p$, divide $b = q(p-1) + r$; then $a^b \equiv a^r \pmod p$.
- **Used in:** [DM-5.6: Fermat Little Theorem](DM-5_Number_Theory/DM-5.6_Fermats_Little_Theorem.md)
- **Last tested:** 2022 Q.8(a) part 1 [02 marks]

#### Chinese Remainder Theorem (CRT)

$$
M_i = \frac{m}{m_i}, \qquad \gcd(M_i, m_i) = 1, \qquad m = m_1 m_2 \cdots m_n
$$

$$
M_i y_i \equiv 1 \pmod{m_i} \quad \implies \quad x = \sum_{i=1}^n a_i M_i y_i \pmod m
$$

- **Condition:** Moduli $m_1, \dots, m_n$ are pairwise relatively prime.
- **Used in:** [DM-5.7: Chinese Remainder Theorem](DM-5_Number_Theory/DM-5.7_Chinese_Remainder_Theorem.md)
- **Last tested:** 2022 Q.8(a) part 2 [04 marks]

---

### DM-6: Counting & Combinatorics

#### Counting Rules & Principle of Inclusion-Exclusion (PIE)

$$
\text{Product Rule: } |A \times B| = |A| \cdot |B|
$$

$$
\text{Sum Rule: } |A \cup B| = |A| + |B| \quad \text{if } A \cap B = \emptyset
$$

$$
\text{Subtraction Rule / PIE: } |A \cup B| = |A| + |B| - |A \cap B|
$$

- **Used in:** [DM-6.1: Sum & Product Rules](DM-6_Counting/DM-6.1_Sum_and_Product_Rules.md), [DM-6.2: Inclusion-Exclusion](DM-6_Counting/DM-6.2_Inclusion_Exclusion.md)
- **Last tested:** 2022 Q.8(b) [02 marks], 2024 Q.7(d) [03 marks]

#### Pigeonhole Principle (PHP)

$$
\text{Standard PHP: If } k+1 \text{ or more objects are placed into } k \text{ boxes, at least one box contains } \ge 2 \text{ objects.}
$$

$$
\text{Generalized PHP: If } N \text{ objects are placed into } k \text{ boxes, at least one box contains } \ge \left\lceil \frac{N}{k} \right\rceil \text{ objects.}
$$

- **Minimum Objects to Guarantee } m \text{ in One Box:** $N = k(m - 1) + 1$.
- **Used in:** [DM-6.3: Pigeonhole Principle](DM-6_Counting/DM-6.3_Pigeonhole_Principle.md)
- **Last tested:** 2024 Q.8(c) [02 marks], 2023 Q.8(a) [02 marks], 2022 Q.8(c, d) [04 marks], CT-04 Q.3(b)

#### Permutations & Combinations

$$
P(n, r) = \frac{n!}{(n - r)!} \quad (\text{order matters})
$$

$$
C(n, r) = \binom{n}{r} = \frac{n!}{r!(n - r)!} = \binom{n}{n - r} \quad (\text{order does not matter})
$$

$$
\text{Permutations of Multiset: } \frac{n!}{n_1! n_2! \cdots n_k!}
$$

- **Used in:** [DM-6.4: Permutations](DM-6_Counting/DM-6.4_Permutations.md), [DM-6.5: Combinations](DM-6_Counting/DM-6.5_Combinations.md)
- **Last tested:** 2023 Q.8(b) [03 marks]

#### Binomial Theorem & Pascal Identity

$$
(x + y)^n = \sum_{r=0}^n \binom{n}{r} x^{n-r} y^r
$$

$$
T_{r+1} = \binom{n}{r} x^{n-r} y^r \quad ((r+1)\text{-th term in expansion})
$$

$$
\binom{n+1}{r} = \binom{n}{r} + \binom{n}{r-1} \quad (\text{Pascal Identity})
$$

- **Used in:** [DM-6.6: Binomial Theorem](DM-6_Counting/DM-6.6_Binomial_Theorem.md)
- **Last tested:** 2023 Q.8(c) [04 marks]

---

### DM-7: Supplementary Topics

#### Big-O Formal Definition & Growth Hierarchy

$$
|f(n)| \le C |g(n)| \quad \text{for all } n > k \quad (C > 0, k \ge 0 \text{ are witnesses})
$$

$$
\Theta(1) < \Theta(\log n) < \Theta(n) < \Theta(n \log n) < \Theta(n^2) < \Theta(2^n) < \Theta(n!)
$$

- **Algorithm Complexities:**
  - **Linear Search:** Best $O(1)$, Worst/Average $O(n)$, Space $O(1)$
  - **Binary Search:** Best $O(1)$, Worst/Average $O(\log n)$, Space $O(1)$ (requires sorted array)
  - **Bubble Sort:** Best $O(n)$, Worst/Average $O(n^2)$, Space $O(1)$
  - **Merge Sort:** Best/Average/Worst $O(n \log n)$, Space $O(n)$
- **Used in:** [DM-7.1: Algorithms and Complexity](DM-7_Supplementary/DM-7.1_Algorithms_and_Complexity.md)
- **Last tested:** 2024 Q.7(a) [06 marks], 2023 Q.8(d) [01 mark]

---

[← Previous: DM-7.2 Relevance of Discrete Mathematics](DM-7_Supplementary/DM-7.2_Relevance_of_DM.md) | [🏠 Index](00_Index.md)
