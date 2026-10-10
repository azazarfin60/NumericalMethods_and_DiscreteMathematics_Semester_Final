[← Previous: DM-7: Algorithms and Relevance](DM-7_Algorithms_and_Relevance.md) | [🏠 Index](00_Index.md)

---

# 📐 ECE 2213: Master Formula Sheet
> **Course:** ECE 2213 — Numerical Methods & Discrete Mathematics | **Credits:** 3.00  
> **Coverage:** All 8 Exam Papers (2017–2024) + Class Tests (CT-01 to CT-04)  
> **Scope:** Complete reference of every display equation, recurrence, error bound, and law tested in RUET exams.

---

## ⚡ High-Frequency Quick Reference (Must-Know Formulas)

These 12 formula families account for over 70% of all numerical marks in ECE 2213 exams:

| # | Method / Topic | Formula Summary | Exam Frequency | Key File |
|---|---|---|:---:|---|
| 1 | **Lagrange Interpolation** | $P(x) = \sum_{i=0}^n y_i \prod_{j \ne i} \frac{x - x_j}{x_i - x_j}$ | 7/8 years + CT | [NM-4.6](NM-4.6_Lagranges_Interpolation.md) |
| 2 | **Gauss-Seidel Iteration** | $x_i^{(k+1)} = \frac{1}{a_{ii}}\left(b_i - \sum_{j < i} a_{ij} x_j^{(k+1)} - \sum_{j > i} a_{ij} x_j^{(k)}\right)$ | 7/8 years + CT | [NM-3.5](NM-3.5_Gauss_Seidel_Iteration.md) |
| 3 | **Newton Forward Difference** | $y(x) = y_0 + p\Delta y_0 + \frac{p(p-1)}{2!}\Delta^2 y_0 + \cdots, \quad p = \frac{x-x_0}{h}$ | 6/8 years + CT | [NM-4.7](NM-4.7_Newtons_Forward_Difference.md) |
| 4 | **Newton-Raphson Method** | $x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}, \quad \text{Order } p = 2$ | 6/8 years | [NM-2.4](NM-2.4_Newton_Raphson_Method.md) |
| 5 | **Bisection Method Bound** | $x_{mid} = \frac{a+b}{2}, \quad n \ge \frac{\ln(b_0-a_0) - \ln\epsilon}{\ln 2}$ | 5/8 years + CT | [NM-2.2](NM-2.2_Bisection_Method.md) |
| 6 | **Runge-Kutta 4th Order (RK4)** | $y_{n+1} = y_n + \frac{1}{6}(k_1 + 2k_2 + 2k_3 + k_4)$ | 5/8 years + CT | [NM-8.5](NM-8.5_Runge_Kutta_4th_Order.md) |
| 7 | **Simpson's 1/3 Rule** | $I \approx \frac{h}{3}[f_0 + 4\sum_{odd} f_i + 2\sum_{even} f_i + f_n], \quad E_t = -\frac{(b-a)h^4}{180}f^{(4)}(\xi)$ | 4/8 years + CT | [NM-5.2](NM-5.2_Simpsons_One_Third_Rule.md) |
| 8 | **Laplace 5-Point Stencil** | $u_{i,j} = \frac{1}{4}(u_{i+1,j} + u_{i-1,j} + u_{i,j+1} + u_{i,j-1})$ | 4/8 years | [NM-10](NM-10_Partial_Differential_Equations.md) |
| 9 | **Pigeonhole Principle** | Plain: $N > k \implies \ge 2$; \quad Generalized: $\ge \lceil N/k \rceil$ | 3/3 DM years | [DM-6.3](DM-6.3_Pigeonhole_Principle.md) |
| 10 | **Binomial Theorem** | $(x+y)^n = \sum_{r=0}^n \binom{n}{r} x^{n-r} y^r, \quad T_{r+1} = \binom{n}{r} x^{n-r} y^r$ | 3/3 DM years | [DM-6 Lower](DM-6_Lower_Counting_Combination_Binomial.md) |
| 11 | **Modular Congruence & FLT** | $a^{p-1} \equiv 1 \pmod p \text{ for prime } p \nmid a; \quad a x \equiv b \pmod m$ | 3/3 DM years | [DM-5 Lower-a](DM-5_Lower_a_Primes_GCD_Fermat_CRT.md) |
| 12 | **Propositional Equivalences** | $p \to q \equiv \neg p \lor q, \quad \neg(p \land q) \equiv \neg p \lor \neg q$ | 4/4 DM sources | [DM-3.2](DM-3.2_Logical_Connectives_and_Truth_Tables.md) |

---

## Section A — Numerical Methods

### NM-1: Modeling, Computers & Error Analysis

#### True Error, True Fractional Relative Error, and Percentage Relative Error
$$
E_t = \text{True value} - \text{Approximation} = x - \hat{x}
$$
$$
\epsilon_t = \frac{x - \hat{x}}{x}, \qquad |\epsilon_t| = \left|\frac{x - \hat{x}}{x}\right| \times 100\%
$$
- **Symbols:** $x$ = true analytical value, $\hat{x}$ = computed approximation, $E_t$ = true error, $\epsilon_t$ = relative true error.
- **Used in:** [NM-1.4: Error Types and Sources](NM-1.4_Error_Types_and_Sources.md), [NM-5.2: Simpson's 1/3 Rule](NM-5.2_Simpsons_One_Third_Rule.md)
- **Last tested:** 2023 Q.4(b) [05 marks], 2021 Q.1(b) [04 marks]

#### Approximate Relative Error (Stopping Criterion)
$$
|\epsilon_a| = \left|\frac{x_{current} - x_{previous}}{x_{current}}\right| \times 100\% < \epsilon_s
$$
$$
\epsilon_s = (0.5 \times 10^{2-n})\% \quad (\text{Scarborough's criterion for } n \text{ significant figures})
$$
- **Symbols:** $x_{current}$ = iterate at step $k$, $x_{previous}$ = iterate at step $k-1$, $\epsilon_s$ = pre-set stopping tolerance, $n$ = required correct digits.
- **Used in:** [NM-1.5: Error Representations and Propagation](NM-1.5_Error_Representations_and_Propagation.md), [NM-2.2: Bisection Method](NM-2.2_Bisection_Method.md)
- **Last tested:** 2018 Q.2(a) [04 marks]

#### Taylor Series Expansion with Lagrange Remainder
$$
f(x_{i+1}) = f(x_i) + f'(x_i)h + \frac{f''(x_i)}{2!}h^2 + \cdots + \frac{f^{(n)}(x_i)}{n!}h^n + R_n
$$
$$
R_n = \frac{f^{(n+1)}(\xi)}{(n+1)!}h^{n+1}, \qquad \xi \in [x_i, x_{i+1}]
$$
- **Symbols:** $h = x_{i+1} - x_i$ = step size, $R_n$ = truncation error of order $O(h^{n+1})$, $\xi$ = intermediate point.
- **Used in:** [NM-1.6: Taylor Series and Truncation Error](NM-1.6_Taylor_Series_and_Truncation_Error.md)
- **Last tested:** 2024 Q.1(b) [05 marks], 2021 Q.1(c) [05 marks]

#### Multivariate Error Propagation (Total Differential)
$$
\Delta u \approx \sum_{i=1}^n \left|\frac{\partial u}{\partial x_i}\right| \Delta x_i
$$
$$
\frac{\Delta u}{u} \approx \sum_{i=1}^n \left|\frac{\partial \ln u}{\partial x_i}\right| \Delta x_i = \sum_{i=1}^n \left|\frac{1}{u}\frac{\partial u}{\partial x_i}\right| \Delta x_i
$$
- **Symbols:** $u = f(x_1, x_2, \dots, x_n)$ = function of measurements, $\Delta x_i$ = absolute uncertainty in variable $x_i$, $\Delta u$ = maximum propagated error.
- **Used in:** [NM-1.5: Error Representations and Propagation](NM-1.5_Error_Representations_and_Propagation.md)
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
- **Used in:** [NM-2.2: Bisection Method](NM-2.2_Bisection_Method.md)
- **Last tested:** 2022 Q.1(b) [05 marks], 2019 Q.2(a) [05 marks]

#### Regula Falsi (False Position) Formula
$$
x_r = \frac{a f(b) - b f(a)}{f(b) - f(a)} = b - \frac{f(b)(b - a)}{f(b) - f(a)}
$$
- **Symbols:** $[a, b]$ = bracket where $f(a)f(b) < 0$, $x_r$ = root approximation from secant line $x$-intercept.
- **Illinois Modification:** If endpoint $a$ stalls for 2 successive steps, replace $f(a)$ with $\frac{1}{2}f(a)$ to force step to cross over.
- **Used in:** [NM-2.3: False Position and Regula Falsi](NM-2.3_False_Position_and_Regula_Falsi.md)
- **Last tested:** 2021 Q.2(b) [05 marks], CT-01 Q.2(a, b)

#### Newton-Raphson Iteration & Convergence Order
$$
x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}
$$
$$
\epsilon_{n+1} \approx \frac{f''(r)}{2f'(r)} \epsilon_n^2 \quad (\text{Quadratic convergence: } p = 2)
$$
- **Symbols:** $x_n$ = current estimate, $f'(x_n) \ne 0$ = first derivative, $r$ = exact simple root.
- **Failure Conditions:** $f'(x_n) \approx 0$ (division by zero / shot to infinity), inflection points ($f''(x) = 0$), local extrema, cycle/oscillation.
- **Used in:** [NM-2.4: Newton-Raphson Method](NM-2.4_Newton_Raphson_Method.md), [NM-2.6: Method Comparison & Convergence](NM-2.6_Method_Comparison_and_Convergence.md)
- **Last tested:** 2024 Q.2(a) [05 marks], 2023 Q.2(a) [04 marks]

#### Secant Method
$$
x_{i+1} = x_i - \frac{f(x_i)(x_i - x_{i-1})}{f(x_i) - f(x_{i-1})}
$$
- **Symbols:** $x_i, x_{i-1}$ = two most recent iterates (no bracketing required).
- **Convergence:** Superlinear ($p = \frac{1+\sqrt{5}}{2} \approx 1.618$).
- **Used in:** [NM-2 Lower: Secant and Polynomial Roots](NM-2_Lower_Secant_and_Polynomial_Roots.md)
- **Last tested:** 2020 Q.2(b) [04 marks]

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
- **Used in:** [NM-3.2: Pivoting](NM-3.2_Pivoting.md), [NM-3 Lower: Gauss Elim, LU, Jacobi, Relaxation](NM-3_Lower_Gauss_Elim_LU_Jacobi_Relaxation.md)
- **Last tested:** 2022 Q.4(b) [06 marks], 2017 Q.3(b) [05 marks]

#### LU Decomposition (Doolittle vs. Crout)
$$
A = L U
$$
$$
\text{Doolittle: } l_{ii} = 1 \text{ (unit lower)}, \qquad \text{Crout: } u_{ii} = 1 \text{ (unit upper)}
$$
$$
L y = b \quad (\text{forward substitution}), \qquad U x = y \quad (\text{back-substitution})
$$
- **Symbols:** $A$ = square coefficient matrix, $L$ = unit lower triangular factor, $U$ = unit upper triangular factor, $b$ = right-hand side vector, $y$ = intermediate vector from the forward substitution.
- **Used in:** [NM-3 Lower: Gauss Elim, LU, Jacobi, Relaxation](NM-3_Lower_Gauss_Elim_LU_Jacobi_Relaxation.md)
- **Last tested:** 2022 Q.4(a) [05 marks]

#### Jacobi Iteration Scheme
$$
x_i^{(k+1)} = \frac{1}{a_{ii}} \left( b_i - \sum_{j \ne i} a_{ij} x_j^{(k)} \right)
$$
- **Symbols:** Uses all old iterates $x_j^{(k)}$ from previous pass.
- **Used in:** [NM-3 Lower: Gauss Elim, LU, Jacobi, Relaxation](NM-3_Lower_Gauss_Elim_LU_Jacobi_Relaxation.md)
- **Last tested:** 2023 Q.3(a) [05 marks]

#### Gauss-Seidel Iteration Scheme
$$
x_i^{(k+1)} = \frac{1}{a_{ii}} \left( b_i - \sum_{j < i} a_{ij} x_j^{(k+1)} - \sum_{j > i} a_{ij} x_j^{(k)} \right)
$$
- **Symbols:** Immediately substitutes newly updated variables $x_j^{(k+1)}$ for $j < i$.
- **Strict Diagonal Dominance Condition for Guaranteed Convergence:**
$$
|a_{ii}| > \sum_{j \ne i} |a_{ij}| \quad \text{for all } i = 1, 2, \dots, n
$$
- **Used in:** [NM-3.5: Gauss-Seidel Iteration](NM-3.5_Gauss_Seidel_Iteration.md), [NM-3.8: Circuit Applications](NM-3.8_Circuit_Applications.md)
- **Last tested:** 2024 Q.2(b) [04 marks], 2021 Q.7(b) [06 marks], 2020 Q.4(b) [05 marks]

#### Successive Over-Relaxation (SOR) Formula
$$
x_i^{(k+1)} = (1 - \omega) x_i^{(k)} + \frac{\omega}{a_{ii}} \left( b_i - \sum_{j < i} a_{ij} x_j^{(k+1)} - \sum_{j > i} a_{ij} x_j^{(k)} \right)
$$
- **Symbols:** $\omega$ = relaxation factor ($0 < \omega < 1$: under-relaxation for divergence, $1 < \omega < 2$: over-relaxation for faster convergence).
- **Used in:** [NM-3 Lower: Gauss Elim, LU, Jacobi, Relaxation](NM-3_Lower_Gauss_Elim_LU_Jacobi_Relaxation.md)
- **Last tested:** 2017 Q.4(c) [06 marks]

---

### NM-4: Interpolation & Curve Fitting

#### Least-Squares Linear Regression ($y = a_0 + a_1 x$)
$$
\begin{bmatrix} n & \sum x_i \\ \sum x_i & \sum x_i^2 \end{bmatrix} \begin{bmatrix} a_0 \\ a_1 \end{bmatrix} = \begin{bmatrix} \sum y_i \\ \sum x_i y_i \end{bmatrix}
$$
$$
a_1 = \frac{n \sum x_i y_i - \sum x_i \sum y_i}{n \sum x_i^2 - (\sum x_i)^2}, \qquad a_0 = \bar{y} - a_1 \bar{x}
$$
- **Symbols:** $n$ = number of data points, $x_i, y_i$ = the $i$-th observation, $a_0$ = intercept, $a_1$ = slope of the fitted line, $\bar{x}, \bar{y}$ = means of the $x$ and $y$ data.
- **Used in:** [NM-4.2: Least-Squares Linear Regression](NM-4.2_Least_Squares_Linear_Regression.md), [NM-4.1: Curve Fitting Concepts](NM-4.1_Curve_Fitting_Concepts.md)
- **Last tested:** 2024 Q.3(c) [05 marks], 2018 Q.4(c) [05 marks]

#### Non-Linear Transformations for Least-Squares
| Model | Form | Transformation | Transformed Linear Form | Parameters |
|---|---|---|---|---|
| **Exponential** | $y = a e^{bx}$ | Take $\ln$ | $\ln y = \ln a + bx$ | $Y = A + bX$, $a = e^A$ |
| **Power** | $y = a x^b$ | Take $\log$ | $\log y = \log a + b \log x$ | $Y = A + bX$, $a = 10^A$ |
| **Saturation-Growth** | $y = \frac{x}{a + bx}$ | Invert ($1/y$) | $\frac{1}{y} = a\left(\frac{1}{x}\right) + b$ | $Y = a X + b$, $Y = 1/y, X = 1/x$ |

- **Symbols:** $X, Y$ = variables after linearizing, $A, B$ = fitted intercept and slope in the transformed space, $a, b$ = original model parameters recovered from $A, B$.
- **Used in:** [NM-4.3: Non-Linear Regression](NM-4.3_Non_Linear_Regression.md)
- **Last tested:** 2022 Q.2(b) [05 marks], 2020 Q.3(c) [04 marks], 2017 Q.5(b) [04 marks]

#### Lagrange Interpolation Formula
$$
P_n(x) = \sum_{i=0}^n y_i L_i(x) = \sum_{i=0}^n y_i \prod_{\substack{j=0 \\ j \ne i}}^n \frac{x - x_j}{x_i - x_j}
$$
$$
L_i(x_k) = \delta_{ik} = \begin{cases} 1 & \text{if } i = k \\ 0 & \text{if } i \ne k \end{cases}
$$
- **Symbols:** Works for arbitrarily spaced data nodes $x_0, x_1, \dots, x_n$.
- **Used in:** [NM-4.6: Lagrange's Interpolation](NM-4.6_Lagranges_Interpolation.md)
- **Last tested:** 2024 Q.3(a) [05 marks], 2023 Q.4(a) [04 marks], CT-02A Q.1

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
- **Symbols:** $\Delta$ = forward difference, $\nabla$ = backward difference, $\delta$ = central difference, $E$ = shift operator, $D$ = derivative operator, $h$ = uniform step size.
- **Used in:** [NM-4.11: Difference Table Formation](NM-4.11_Difference_Table_Formation.md)
- **Last tested:** 2024 Q.4(a) [04 marks], 2022 Q.3(a) [04 marks], 2020 Q.5(a) [04 marks]

#### Newton's Forward Difference Interpolation
$$
y(x) = y_0 + p \Delta y_0 + \frac{p(p-1)}{2!} \Delta^2 y_0 + \frac{p(p-1)(p-2)}{3!} \Delta^3 y_0 + \cdots
$$
$$
p = \frac{x - x_0}{h}
$$
- **Condition:** Equispaced points with step $h$, interpolating near the beginning of table ($0 < p < 1$).
- **Symbols:** $y_0$ = function value at the first node, $\Delta^r y_0$ = $r$-th forward difference at the first node, $p$ = position of the target $x$ measured from $x_0$, $h$ = uniform step size.
- **Used in:** [NM-4.7: Newton's Forward Difference](NM-4.7_Newtons_Forward_Difference.md)
- **Last tested:** 2023 Q.2(a) [05 marks], 2021 Q.4(b) [05 marks], CT-02A Q.2

#### Newton's Backward Difference Interpolation
$$
y(x) = y_n + p \nabla y_n + \frac{p(p+1)}{2!} \nabla^2 y_n + \frac{p(p+1)(p+2)}{3!} \nabla^3 y_n + \cdots
$$
$$
p = \frac{x - x_n}{h}
$$
- **Condition:** Equispaced points with step $h$, interpolating near the end of table ($-1 < p < 0$).
- **Symbols:** $y_n$ = function value at the last node, $\nabla^r y_n$ = $r$-th backward difference at the last node, $p$ = position of the target $x$ measured from $x_n$, $h$ = uniform step size.
- **Used in:** [NM-4 Lower: Regression Theory + Other Interpolation](NM-4_Lower_Regression_Theory_Interpolation_Methods.md)
- **Last tested:** 2024 Q.3(b) [05 marks], 2017 Q.5(c) [05 marks]

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
- **Condition:** Interpolating near the center of table ($-0.5 \le p \le 0.5$).
- **Symbols:** $y_p$ = value at the target point, $p$ = position of the target $x$ measured from $x_0$, $\Delta^r y_i$ = $r$-th forward difference at node $i$, negative subscripts count nodes to the left of $x_0$.
- **Used in:** [NM-4 Lower: Regression Theory + Other Interpolation](NM-4_Lower_Regression_Theory_Interpolation_Methods.md)
- **Last tested:** 2022 Q.3(b) [05 marks]

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
- **Symbols:** $I$ = exact value of the integral, $f_i = f(x_i)$ = integrand at node $i$, $h = (b-a)/n$ = step size, $n$ = number of equal subintervals, $\xi$ = intermediate point where $f''$ is evaluated.
- **Used in:** [NM-5 Lower: Trapezoidal, 3/8, Romberg, Error, Applied](NM-5_Lower_Trapezoidal_38_Romberg_Error_Applied.md)
- **Last tested:** 2021 Q.8(b) [06 marks], 2020 Q.6(a) [04 marks]

#### Simpson's 1/3 Rule (Single & Composite)
$$
\text{Single } (n=2): I \approx \frac{h}{3}[f_0 + 4f_1 + f_2], \qquad E_t = -\frac{h^5}{90} f^{(4)}(\xi)
$$
$$
\text{Composite (even } n): I \approx \frac{h}{3}\left[ f_0 + 4\sum_{i=1,3,\dots}^{n-1} f_i + 2\sum_{i=2,4,\dots}^{n-2} f_i + f_n \right], \qquad E_t = -\frac{(b-a)h^4}{180} f^{(4)}(\xi)
$$
- **Degree of precision:** 3 (exact for polynomials up to degree 3, despite using parabolas).
- **Symbols:** $I$ = exact value of the integral, $f_i = f(x_i)$ = integrand at node $i$, $h = (b-a)/n$ = step size, $n$ = even number of subintervals, $\xi$ = intermediate point where $f^{(4)}$ is evaluated.
- **Used in:** [NM-5.2: Simpson's 1/3 Rule](NM-5.2_Simpsons_One_Third_Rule.md)
- **Last tested:** 2023 Q.4(b) [05 marks], 2018 Q.6(a) [08 marks], 2019 Q.7(a) [06 marks]

#### Simpson's 3/8 Rule
$$
I \approx \frac{3h}{8}\left[ f_0 + 3f_1 + 3f_2 + 2f_3 + 3f_4 + 3f_5 + \cdots + f_n \right], \qquad E_t = -\frac{(b-a)h^4}{80} f^{(4)}(\xi)
$$
- **Condition:** Number of segments $n$ must be a multiple of 3.
- **Symbols:** $I$ = exact value of the integral, $f_i = f(x_i)$ = integrand at node $i$, $h = (b-a)/n$ = step size, $n$ = number of subintervals, always a multiple of 3, $\xi$ = intermediate point where $f^{(4)}$ is evaluated.
- **Used in:** [NM-5 Lower: Trapezoidal, 3/8, Romberg, Error, Applied](NM-5_Lower_Trapezoidal_38_Romberg_Error_Applied.md), [NM-5.4: Rule Comparison & Step Constraints](NM-5.4_Rule_Comparison_and_Step_Constraints.md)
- **Last tested:** 2019 Q.6(b) [05 marks]

#### Romberg Integration
$$
I_{j,k} = \frac{4^{k-1} I_{j+1,k-1} - I_{j,k-1}}{4^{k-1} - 1}
$$
- **Extrapolation order:** $k=1 \implies O(h^2)$, $k=2 \implies O(h^4)$, $k=3 \implies O(h^6)$.
- **Symbols:** $I_{j,k}$ = extrapolated estimate in row $j$, column $k$ of the Romberg table, $I_{j+1,k-1}$ and $I_{j,k-1}$ = the two earlier estimates that combine to give it, $k$ = column index, which also fixes the order of accuracy.
- **Used in:** [NM-5 Lower: Trapezoidal, 3/8, Romberg, Error, Applied](NM-5_Lower_Trapezoidal_38_Romberg_Error_Applied.md)
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
- **Symbols:** $r$ = golden ratio conjugate, $a, b$ = current bracket endpoints, $x_1, x_2$ = two interior trial points, $f$ = the function being maximized or minimized.
- **Used in:** [NM-6: Optimization](NM-6_Optimization.md)
- **Last tested:** 2020 Q.8(a) [04 marks]

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
- **Symbols:** $f'(x_i)$ and $f''(x_i)$ = first and second derivative at node $x_i$, $f(x_i)$ = function value at node $x_i$, $h$ = step size, $O(h^m)$ = truncation error order.
- **Used in:** [NM-7: Numerical Differentiation](NM-7_Numerical_Differentiation.md)
- **Last tested:** 2023 Q.2(b) [04 marks], 2021 Q.3(d) [04 marks]

---

### NM-8: Ordinary Differential Equations (IVP & BVP)

#### Euler's Method
$$
y_{i+1} = y_i + h f(x_i, y_i)
$$
- **Error:** Local truncation error $O(h^2)$, global error $O(h)$.
- **Symbols:** $y_i = y(x_i)$ = solution value at node $x_i$, $h$ = step size, $f(x_i, y_i)$ = right-hand side of $dy/dx = f(x, y)$.
- **Used in:** [NM-8.2: Euler's Method](NM-8.2_Eulers_Method.md)
- **Last tested:** 2021 Q.8(c) [05 marks], 2018 Q.7(b) [04 marks]

#### Heun's Method (Improved Euler / Predictor-Corrector)
$$
\tilde{y}_{i+1} = y_i + h f(x_i, y_i) \quad (\text{predictor})
$$
$$
y_{i+1} = y_i + \frac{h}{2}[f(x_i, y_i) + f(x_{i+1}, \tilde{y}_{i+1})] \quad (\text{corrector})
$$
- **Error:** Global error $O(h^2)$.
- **Symbols:** $y_i$ = solution value at node $x_i$, $\tilde{y}_{i+1}$ = predicted Euler value at the next node, $h$ = step size, $f(x, y)$ = right-hand side of the ODE.
- **Used in:** [NM-8 Lower: IVP, BVP, Heun, RK2, Higher ODE](NM-8_Lower_IVP_BVP_Heun_RK2_Higher.md)
- **Last tested:** 2020 Q.7(c) [05 marks], CT-02B Q.2(a)

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
- **Symbols:** $y_n$ = solution value at node $x_n$, $h$ = step size, $k_1, k_2, k_3, k_4$ = the four slopes evaluated across one step, $f(x, y)$ = right-hand side of the ODE.
- **Used in:** [NM-8.5: Runge-Kutta 4th Order](NM-8.5_Runge_Kutta_4th_Order.md)
- **Last tested:** 2024 Q.4(b) [06 marks], 2018 Q.8(a) [05 marks], 2017 Q.7(b) [06 marks], CT-02B Q.2(b)

---

### NM-9: Eigenvalue Problems

#### Characteristic Polynomial & Power Method
$$
\det(A - \lambda I) = 0
$$
$$
\mathbf{x}^{(k+1)} = \frac{A \mathbf{x}^{(k)}}{\max(A \mathbf{x}^{(k)})} \quad (\text{Power Method for dominant eigenvalue } \lambda_1)
$$
$$
\lambda \approx \frac{\mathbf{x}^T A \mathbf{x}}{\mathbf{x}^T \mathbf{x}} \quad (\text{Rayleigh Quotient})
$$
- **Properties:** $\sum \lambda_i = \operatorname{tr}(A)$, $\prod \lambda_i = \det(A)$.
- **Symbols:** $A$ = square matrix, $\lambda$ = eigenvalue, $I$ = identity matrix of the same order, $\mathbf{x}^{(k)}$ = $k$-th iterate of the eigenvector estimate, $\mathbf{x}^T$ = transpose of $\mathbf{x}$.
- **Used in:** [NM-9: Eigenvalue Problems](NM-9_Eigenvalue_Problems.md)
- **Last tested:** 2023 Q.3(a) [04 marks]

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
- **Symbols:** $A, B, C$ = coefficients of $u_{xx}, u_{xy}, u_{yy}$ in a general second-order PDE, $B^2 - 4AC$ = the discriminant that decides the equation type.
- **Used in:** [NM-10: Partial Differential Equations](NM-10_Partial_Differential_Equations.md)
- **Last tested:** 2017 Q.8(a) [04 marks]

#### Five-Point Stencils on Square Mesh ($h = k$)
$$
\text{Laplace: } u_{i,j} = \frac{1}{4}(u_{i+1,j} + u_{i-1,j} + u_{i,j+1} + u_{i,j-1})
$$
$$
\text{Poisson: } u_{i+1,j} + u_{i-1,j} + u_{i,j+1} + u_{i,j-1} - 4u_{i,j} = -h^2 f(x_i, y_j)
$$
- **Liebmann's Method:** Gauss-Seidel iterative updating of Laplace stencil over interior grid nodes.
- **Symbols:** $u_{i,j}$ = solution at grid node $(i, j)$, $h = k$ = equal mesh spacing in $x$ and $y$, $f(x_i, y_j)$ = source term of the Poisson equation.
- **Used in:** [NM-10: Partial Differential Equations](NM-10_Partial_Differential_Equations.md)
- **Last tested:** 2021 Q.6(c) [06 marks], 2020 Q.8(b) [06 marks], 2019 Q.8(b) [08 marks], 2018 Q.8(a) [06 marks]

---

## Section B — Discrete Mathematics

### DM-3: Propositional Logic

#### Fundamental Connective Truth Values
| $p$ | $q$ | $\neg p$ | $p \land q$ | $p \lor q$ | $p \oplus q$ | $p \to q$ | $p \leftrightarrow q$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| T | T | F | T | T | F | T | T |
| T | F | F | F | T | T | F | F |
| F | T | T | F | T | T | T | F |
| F | F | T | F | F | F | T | T |

- **Critical Trap:** $p \to q$ is false **only** when $p$ is T and $q$ is F. If $p$ is F, $p \to q$ is vacuously true.
- **Symbols:** $p, q$ = the two propositions, $\neg p$ = negation, $p \land q$ = conjunction, $p \lor q$ = disjunction, $p \oplus q$ = exclusive or, $p \to q$ = implication, $p \leftrightarrow q$ = biconditional, T and F = true and false.
- **Used in:** [DM-3.2: Logical Connectives and Truth Tables](DM-3.2_Logical_Connectives_and_Truth_Tables.md)
- **Last tested:** 2023 Q.5(a) [03 marks], 2022 Q.5(a) [03 marks], CT-04 Q.2(c)

#### Essential Logical Equivalences
$$
p \to q \equiv \neg p \lor q \equiv \neg q \to \neg p \quad (\text{contrapositive})
$$
$$
\neg(p \land q) \equiv \neg p \lor \neg q, \qquad \neg(p \lor q) \equiv \neg p \land \neg q \quad (\text{De Morgan's Laws})
$$
$$
p \land (q \lor r) \equiv (p \land q) \lor (p \land r), \qquad p \lor (q \land r) \equiv (p \lor q) \land (p \lor r) \quad (\text{Distributive Laws})
$$
$$
p \leftrightarrow q \equiv (p \to q) \land (q \to p) \equiv (\neg p \lor q) \land (\neg q \lor p) \equiv (p \land q) \lor (\neg p \land \neg q)
$$
- **Symbols:** $p, q, r$ = arbitrary propositions, $\equiv$ = logical equivalence, $\neg$ = negation, $\land$ = conjunction, $\lor$ = disjunction, $\to$ = implication, $\leftrightarrow$ = biconditional.
- **Used in:** [DM-3.3: Tautology, Contradiction, Contingency](DM-3.3_Tautology_Contradiction_Contingency.md), [DM-3.8: Normal Forms](DM-3.8_Normal_Forms_and_Functional_Completeness.md), [DM-3 Lower-a: Validity, Equivalence, Translation](DM-3_Lower_a_Validity_Equivalence_Translation.md)
- **Last tested:** 2024 Q.6(b) [04 marks], 2023 Q.5(b) [03 marks]

#### Conjunctive & Disjunctive Normal Forms (CNF / DNF)
$$
A \equiv \bigwedge_{i=1}^{m} \left( \bigvee_{j=1}^{n} l_{ij} \right) \quad (\text{CNF: clauses joined by AND, each clause a disjunction of literals})
$$
$$
A \equiv \bigvee_{i=1}^{m} \left( \bigwedge_{j=1}^{n} l_{ij} \right) \quad (\text{DNF: terms joined by OR, each term a conjunction of literals})
$$
- **Symbols:** $A$ = the compound proposition being converted, $l_{ij}$ = a literal, which is a variable $p$ or its negation $\neg p$, $m$ = number of clauses (CNF) or terms (DNF), $n$ = literals per clause or term.
- **Procedure:** Rewrite $\to$, $\leftrightarrow$, $\oplus$ using the equivalences above. Push every $\neg$ inward with De Morgan's Laws. Then group into clauses (CNF) or terms (DNF).
- **Used in:** [DM-3.8: Normal Forms and Functional Completeness](DM-3.8_Normal_Forms_and_Functional_Completeness.md)
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
- **Symbols:** $p \uparrow q$ = NAND, true only when both inputs are true, $p \downarrow q$ = NOR, true only when both inputs are false.
- **Used in:** [DM-3.8: Normal Forms and Functional Completeness](DM-3.8_Normal_Forms_and_Functional_Completeness.md), [DM-3 Lower-b: Puzzles, Gates, Extensions](DM-3_Lower_b_Puzzles_Gates_Extensions.md)
- **Last tested:** 2022 Q.5(c) [03 marks]

#### Core Rules of Inference
$$
\begin{array}{r l r l}
\text{Modus Ponens:} & \frac{p,\; p \to q}{\therefore q} & \text{Modus Tollens:} & \frac{\neg q,\; p \to q}{\therefore \neg p} \\
\text{Hypothetical Syllogism:} & \frac{p \to q,\; q \to r}{\therefore p \to r} & \text{Disjunctive Syllogism:} & \frac{p \lor q,\; \neg p}{\therefore q} \\
\text{Resolution:} & \frac{p \lor q,\; \neg p \lor r}{\therefore q \lor r} & \text{Universal Instantiation:} & \frac{\forall x\, P(x)}{\therefore P(c)}
\end{array}
$$
- **Symbols:** $p, q, r$ = arbitrary propositions, $P(x)$ = an open statement, $c$ = a particular element of the domain, $\forall$ = universal quantifier, $\therefore$ = therefore.
- **Used in:** [DM-3.9: Rules of Inference and Valid Arguments](DM-3.9_Rules_of_Inference_and_Valid_Arguments.md)
- **Last tested:** 2024 Q.5(a) [03 marks], 2022 Q.6(a) [04 marks]

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
- **Symbols:** $a$ = dividend, $d$ = divisor, $q$ = quotient, $r$ = remainder with $0 \le r < d$, $m$ = modulus, $\mid$ = divides, $\iff$ = if and only if.
- **Used in:** [DM-5.4: Modular Arithmetic and Congruence](DM-5.4_Modular_Arithmetic_and_Congruence.md)
- **Last tested:** 2024 Q.8(a) [04 marks], 2022 Q.7(a) [04 marks]

#### Euclidean Algorithm & Extended Euclidean Algorithm (Bézout's Identity)
$$
\gcd(a, b) = \gcd(b, a \bmod b), \qquad \gcd(a, 0) = a
$$
$$
\gcd(a, b) = s \cdot a + t \cdot b \quad (s, t \in \mathbb{Z} \text{ are Bézout coefficients})
$$
- **Modular Inverse:** If $\gcd(a, m) = 1$, then $s \cdot a \equiv 1 \pmod m$, so $a^{-1} \equiv s \pmod m$.
- **Symbols:** $\gcd(a, b)$ = greatest common divisor, $s$ and $t$ = Bézout coefficients, $a \bmod b$ = remainder of $a$ divided by $b$, $a^{-1} \bmod m$ = modular inverse of $a$ modulo $m$.
- **Used in:** [DM-5 Lower-a: Primes, GCD, Fermat, CRT](DM-5_Lower_a_Primes_GCD_Fermat_CRT.md)
- **Last tested:** 2022 Q.7(c) [04 marks]

#### Fermat's Little Theorem (FLT)
$$
a^{p-1} \equiv 1 \pmod p \quad \text{if } p \text{ is prime and } p \nmid a
$$
$$
a^p \equiv a \pmod p \quad \text{for all integers } a
$$
- **Exponent Reduction Technique:** To compute $a^b \bmod p$, divide $b = q(p-1) + r$; then $a^b \equiv (a^{p-1})^q \cdot a^r \equiv 1^q \cdot a^r \equiv a^r \pmod p$.
- **Symbols:** $p$ = a prime number, $a$ = an integer not divisible by $p$, $b = q(p-1) + r$ = the exponent split, $q$ = quotient, $r$ = remainder used to reduce the exponent.
- **Used in:** [DM-5 Lower-a: Primes, GCD, Fermat, CRT](DM-5_Lower_a_Primes_GCD_Fermat_CRT.md), [DM-5.5: Modular Exponentiation](DM-5.5_Modular_Exponentiation.md)
- **Last tested:** 2024 Q.8(b) [03 marks], 2023 Q.7(b) [03 marks]

#### Chinese Remainder Theorem (CRT)
$$
M_i = \frac{m}{m_i}, \qquad \gcd(M_i, m_i) = 1
$$
$$
M_i c_i \equiv a_i \pmod{m_i} \quad (i = 1, 2, \dots, n)
$$
$$
x = \sum_{i=1}^n M_i c_i \pmod m, \qquad m = m_1 m_2 \cdots m_n
$$
- **Symbols:** $m_1, m_2, \dots, m_n$ = pairwise relatively prime moduli, each greater than 1, $a_i$ = the residue required modulo $m_i$, $M_i$ = product of all moduli except $m_i$, $c_i$ = scalar that makes $M_i c_i$ match $a_i$, $m = m_1 m_2 \cdots m_n$ = combined modulus.
- **Construction:** Compute $M_i$, solve each single congruence $M_i c_i \equiv a_i \pmod{m_i}$, then add the products. The solution is unique modulo $m$.
- **Used in:** [DM-5 Lower-a: Primes, GCD, Fermat, CRT](DM-5_Lower_a_Primes_GCD_Fermat_CRT.md)
- **Last tested:** 2022 Q.8(a) [04 marks]

---

### DM-6: Counting & Combinatorics

#### Counting Rules & Principle of Inclusion-Exclusion (PIE)
$$
\text{Product Rule (Independent / Sequential): } |A \times B| = |A| \cdot |B|
$$
$$
\text{Sum Rule (Disjoint choices): } |A \cup B| = |A| + |B| \quad \text{if } A \cap B = \emptyset
$$
$$
\text{Subtraction Rule / PIE: } |A \cup B| = |A| + |B| - |A \cap B|
$$
- **Symbols:** $A, B$ = sets, $|A|$ = cardinality of $A$, $A \times B$ = Cartesian product, $A \cap B$ = intersection, $\emptyset$ = empty set.
- **Used in:** [DM-6 Lower: Counting, Combination, Binomial](DM-6_Lower_Counting_Combination_Binomial.md)
- **Last tested:** 2022 Q.8(b) [02 marks]

#### Pigeonhole Principle (PHP)
$$
\text{Standard PHP: If } k+1 \text{ or more objects are placed into } k \text{ boxes, at least one box contains } \ge 2 \text{ objects.}
$$
$$
\text{Generalized PHP: If } N \text{ objects are placed into } k \text{ boxes, at least one box contains } \ge \left\lceil \frac{N}{k} \right\rceil \text{ objects.}
$$
- **Minimum Objects to Guarantee } m \text{ in One Box:** $N = k(m - 1) + 1$.
- **Symbols:** $N$ = number of objects, $k$ = number of boxes, $m$ = objects guaranteed in one box, $\lceil N/k \rceil$ = ceiling of $N/k$.
- **Used in:** [DM-6.3: Pigeonhole Principle](DM-6.3_Pigeonhole_Principle.md)
- **Last tested:** 2024 Q.8(c) [02 marks], 2023 Q.8(a) [02 marks], 2022 Q.8(c, d) [04 marks]

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
- **Symbols:** $n$ = total number of items, $r$ = number chosen, $P(n,r)$ = ordered arrangement, $C(n,r) = \binom{n}{r}$ = unordered selection, $n_1, n_2, \dots, n_k$ = multiplicities in a multiset.
- **Used in:** [DM-6 Lower: Counting, Combination, Binomial](DM-6_Lower_Counting_Combination_Binomial.md)
- **Last tested:** 2023 Q.8(b) [03 marks]

#### Binomial Theorem & Pascal's Identity
$$
(x + y)^n = \sum_{r=0}^n \binom{n}{r} x^{n-r} y^r
$$
$$
T_{r+1} = \binom{n}{r} x^{n-r} y^r \quad ((r+1)\text{-th term in expansion})
$$
$$
\binom{n+1}{r} = \binom{n}{r} + \binom{n}{r-1} \quad (\text{Pascal's Identity})
$$
- **Symbols:** $n$ = exponent in the expansion, $r$ = term index, $T_{r+1}$ = the $(r+1)$-th term, $\binom{n}{r}$ = binomial coefficient, $x$ and $y$ = the quantities being expanded.
- **Used in:** [DM-6 Lower: Counting, Combination, Binomial](DM-6_Lower_Counting_Combination_Binomial.md)
- **Last tested:** 2023 Q.8(c) [04 marks]

---

### DM-7: Algorithms & Complexity

#### Big-O Formal Definition & Growth Hierarchy
$$
|f(n)| \le C |g(n)| \quad \text{for all } n > k \quad (C > 0, k \ge 0 \text{ are witnesses})
$$
$$
\Theta(1) < \Theta(\log n) < \Theta(n) < \Theta(n \log n) < \Theta(n^2) < \Theta(2^n) < \Theta(n!)
$$
- **Complexity of Core Algorithms:**
  - **Binary Search:** Time: Best $O(1)$, Worst/Avg $O(\log n)$, Space $O(1)$ (array must be sorted)
  - **Merge Sort:** Time: Best/Avg/Worst $O(n \log n)$, Space $O(n)$ (stable)
  - **Greedy Assignment:** Time: $O(n \log n + nm)$, Space $O(n + m)$
- **Symbols:** $f(n)$ = the function whose growth is measured, $g(n)$ = the comparison function, $C$ = a positive constant witness, $k$ = a threshold beyond which the bound holds.
- **Used in:** [DM-7: Algorithms and Relevance](DM-7_Algorithms_and_Relevance.md)
- **Last tested:** 2024 Q.7(a) [06 marks], 2023 Q.8(d) [01 mark]

---

[← Previous: DM-7: Algorithms and Relevance](DM-7_Algorithms_and_Relevance.md) | [🏠 Index](00_Index.md)
