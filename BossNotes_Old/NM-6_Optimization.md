[← Previous: NM-5 Lower — Trapezoidal, 3/8, Romberg](NM-5_Lower_Trapezoidal_38_Romberg_Error_Applied.md) | [🏠 Index](00_Index.md) | [Next: NM-7 Numerical Differentiation →](NM-7_Numerical_Differentiation.md)

---

# NM-6: Optimization
> **Section:** A (Numerical Methods) | **Priority:** 🟡 | **Exam Frequency:** 2/8 years | **Subtopics:** NM-6.1, NM-6.2, NM-6.3
> **Sources:** Class Notes (no direct Jain chapter), Shishir Notes §04

## Why This Topic Matters

Optimization is a light topic. It appeared in 2018 (finding maxima from tabulated data, 6 marks) and 2021 (constrained vs. unconstrained theory + Newton's method for maxima, 5 marks total). That makes it a low-frequency topic, but when it appears, it carries decent marks. The Newton's method connection to NM-2.4 makes it easy to prepare if you already know root finding.

---

## 📝 Key Definitions

> **Optimization:** Finding the values of decision variables that maximise or minimise an objective function $f(x)$, possibly subject to constraints.

> **Unconstrained optimization:** No restrictions on the variables. The optimum satisfies $\nabla f = 0$ (gradient is zero).

> **Constrained optimization:** The variables must satisfy conditions written as $g(x) \le 0$ (inequality constraints) or $h(x) = 0$ (equality constraints). Solved using Lagrange multipliers or KKT conditions.

---

## NM-6.1 — Constrained vs. Unconstrained Optimization

### Theory

The difference is about whether the variables are free or restricted.

**Unconstrained:** Choose $x$ anywhere in the domain. The stationarity condition is:

$$
\nabla f = 0
$$

Example: fitting $y = a + bx$ by least squares. Nothing restricts $a$ or $b$.

**Constrained:** Extra rules apply. Written formally:

$$
\text{minimise } f(x) \quad \text{subject to} \quad g_i(x) \le 0, \quad h_j(x) = 0
$$

Example: minimise the weight of a structure subject to stress limits on each member.

**Comparison table:**

| | Unconstrained | Constrained |
| :-- | :-- | :-- |
| Restrictions | None | Equality and inequality conditions |
| Stationarity test | $\nabla f = 0$ | KKT conditions with multipliers |
| Lagrange multipliers | Not needed | Essential |
| Optimum location | Interior point | Often on the boundary |
| Feasible region | Whole space | A subset |
| Difficulty | Easier | Harder; more constraints mean more cases |

The key insight: in the constrained case, the optimum often sits **on** a boundary. There, the plain gradient test ($\nabla f = 0$) fails because the feasible directions are restricted. That is why Lagrange multipliers and KKT conditions exist.

---

## NM-6.2 — Newton's Method for Finding Optima

### Theory

To find a maximum or minimum of $f(x)$, solve $f'(x) = 0$. This is a root-finding problem for the derivative. Apply Newton-Raphson to $g(x) = f'(x)$:

$$
x_{n+1} = x_n - \frac{g(x_n)}{g'(x_n)} = x_n - \frac{f'(x_n)}{f''(x_n)}
$$

> [!WARNING] The denominator is $f''$, not $f'$
> This is Newton's method applied to $f' = 0$, so the "function" is $f'$ and its derivative is $f''$. Using $f'$ in the denominator gives a different (wrong) iteration.

**After finding the critical point, always check whether it is a maximum or minimum:**
- $f''(x^*) < 0$: maximum (concave)
- $f''(x^*) > 0$: minimum (convex)

This check is not optional. Newton applied to $f' = 0$ finds any critical point. It does not distinguish between maxima and minima.

### Algorithm

1. Compute $f'(x)$ and $f''(x)$ analytically.
2. Choose an initial guess $x_0$.
3. Iterate: $x_{n+1} = x_n - \frac{f'(x_n)}{f''(x_n)}$
4. Stop when $|f'(x_n)| < \epsilon$ or $|x_{n+1} - x_n| < \epsilon$.
5. Check $f''(x^*)$ to classify the critical point.

### 🏆 Golden Questions for NM-6.2

#### 🎯 Use Newton's method to find the maximum of $f(x) = 2\sin x - \frac{x^2}{10}$ with $x_0 = 2.5$.
> **Appeared:** 2021 Q.6(b) — (03 marks)

**Full Answer:**

**Step 1. Set up the iteration.** $f'(x) = 2\cos x - \frac{x}{5}$, $f''(x) = -2\sin x - \frac{1}{5}$.

$$
x_{n+1} = x_n - \frac{2\cos x_n - x_n/5}{-2\sin x_n - 1/5}
$$

**Step 2. Iterate from $x_0 = 2.5$.**

At $x_0 = 2.5$: $f'(2.5) = 2\cos 2.5 - 0.5 = -2.10229$, $f''(2.5) = -2\sin 2.5 - 0.2 = -1.39694$.

| Iteration | $x_n$ | $f'(x_n)$ | $f(x_n)$ |
| --: | --: | --: | --: |
| 0 | 2.5000000000 | $-2.1022872$ | 0.5719443 |
| 1 | 0.9950815513 | $+0.8898527$ | 1.5785880 |
| 2 | 1.4690107528 | $-0.0905823$ | 1.7738494 |
| 3 | 1.4276423210 | $-0.0001973$ | 1.7757256 |
| 4 | 1.4275517793 | $-0.0000000$ | 1.7757257 |
| 5 | 1.4275517788 | $0$ | 1.7757257 |

Iteration 1: $x_1 = 2.5 - \frac{-2.1022872}{-1.3969443} = 2.5 - 1.5049184 = 0.9950816$.

**Step 3. Confirm it is a maximum.**

$f''(1.42755) = -2\sin(1.42755) - 0.2 = -2.179516$, which is **negative**. So the critical point is a maximum.

$$
\boxed{x_{max} = 1.42755, \qquad f(x_{max}) = 1.77573}
$$

> [!TIP] The first iterate overshoots
> $x_0 = 2.5$ produces $x_1 = 0.995$, jumping past the answer at $1.4276$. This is normal. Both $f'$ and $f''$ are negative and of similar size at $x_0$, making the step large. From iteration 2 onward, convergence is monotone and fast.

---

#### 🎯 Differentiate between constrained and unconstrained optimization.
> **Appeared:** 2021 Q.6(d) — (02 marks)

**Full Answer:**

**Unconstrained optimization.** No restrictions. Choose $x$ freely to maximise or minimise $f(x)$. Stationarity condition: $\nabla f = 0$.

Example: least squares regression. Nothing restricts the coefficients.

**Constrained optimization.** Extra conditions must hold: $g_i(x) \le 0$ and $h_j(x) = 0$. Solved using Lagrange multipliers. The optimum frequently sits on a boundary, where the plain gradient test is useless.

Example: minimise weight of a truss subject to load limits on each member.

| | Unconstrained | Constrained |
| :-- | :-- | :-- |
| Restrictions | None | Equality and inequality |
| Stationarity | $\nabla f = 0$ | KKT with multipliers |
| Optimum location | Interior | Often on boundary |

$$
\boxed{\text{Unconstrained: choose freely. Constrained: obey rules, solved with multipliers}}
$$

---

## NM-6.3 — Optima from Tabulated Data

### Theory

When a function is known only at discrete points (a table), find the maximum or minimum by:

1. Build a difference table to understand the trend.
2. Use the backward (or forward) Newton polynomial derivative formula.
3. Set $\frac{dy}{dx} = 0$ and solve for $q$ (the fractional distance from the reference node).
4. Compute $x = x_{\text{ref}} + hq$.
5. Evaluate $y$ at that $x$ using the Newton polynomial.

The backward form is natural when the maximum is near the end of the table. The forward form is natural when it is near the start.

### 🏆 Golden Questions for NM-6.3

#### 🎯 From the table, find $x$ (correct to two decimal places) for which $y$ is maximum, and find this value of $y$.
> **Appeared:** 2018 Q.5(b) — (06 marks)

**Full Answer:**

| $x$ | 1.2 | 1.3 | 1.4 | 1.5 | 1.6 |
| :---: | :---: | :---: | :---: | :---: | :---: |
| $y$ | 0.9320 | 0.9636 | 0.9855 | 0.9975 | 0.9996 |

**Step 1. Build the difference table** ($h = 0.1$):

| | 0.9320 | 0.9636 | 0.9855 | 0.9975 | 0.9996 |
| :-- | :-- | :-- | :-- | :-- | :-- |
| $\Delta$ | | $0.0316$ | $0.0219$ | $0.0120$ | $0.0021$ |
| $\Delta^2$ | | | $-0.0097$ | $-0.0099$ | $-0.0099$ |
| $\Delta^3$ | | | | $-0.0002$ | $0.0000$ |
| $\Delta^4$ | | | | | $0.0002$ |

All first differences are positive but falling. The last one ($0.0021$) is small. The second differences are all negative. So $y$ is still rising at $x = 1.5$ but levelling off. The maximum lies just inside the end of the table, near $x = 1.6$.

**Step 2. Use the backward derivative.** At $x_4 = 1.6$ with $q = (x - x_4)/h$:

$$
\frac{dy}{dx} = \frac{1}{h}\left[\nabla y_4 + \frac{2q+1}{2}\nabla^2 y_4 + \frac{3q^2+6q+2}{6}\nabla^3 y_4 + \frac{4q^3+18q^2+22q+6}{24}\nabla^4 y_4\right]
$$

The backward differences at $x_4$:

$$
\nabla y_4 = 0.0021, \qquad \nabla^2 y_4 = -0.0099, \qquad \nabla^3 y_4 = 0.0000, \qquad \nabla^4 y_4 = 0.0002
$$

**Step 3. Set $\frac{dy}{dx} = 0$.** With $\nabla^3 y_4 = 0$ and $\nabla^4 y_4$ tiny, the first two terms dominate:

$$
0.0021 + \frac{2q+1}{2}(-0.0099) = 0
$$

$$
0.0021 = (q + 0.5)(0.0099)
$$

$$
q + 0.5 = \frac{0.0021}{0.0099} = 0.212121
$$

$$
q = -0.287879
$$

$$
x = x_4 + hq = 1.6 + 0.1(-0.287879) = 1.5712
$$

**Step 4. Evaluate $y$ there.** Using the backward Newton polynomial:

$$
y = y_4 + q\nabla y_4 + \frac{q(q+1)}{2}\nabla^2 y_4 + \frac{q(q+1)(q+2)}{6}\nabla^3 y_4 + \frac{q(q+1)(q+2)(q+3)}{24}\nabla^4 y_4
$$

At $q = -0.287879$:

$$
y = 0.9996 + (-0.287879)(0.0021) + \frac{(-0.287879)(0.712121)}{2}(-0.0099) + 0 + \frac{(-0.287879)(0.712121)(1.712121)(2.712121)}{24}(0.0002)
$$

$$
y = 0.9996 - 0.0006045 + 0.0010148 - 0.0000079 = 1.0000023
$$

$$
\boxed{x = 1.57 \text{ (correct to two decimal places)}, \qquad y_{\max} = 1.0000}
$$

> [!NOTE] $y_{\max} = 1.0000$ is slightly above the table's largest entry ($0.9996$)
> The interpolated maximum is $1.0000023$. The table's largest value is $0.9996$ at $x = 1.6$, but the fitted curve peaks at $x = 1.5712$ with a slightly higher value. Do not "correct" the answer to $0.9996$. The interpolated maximum and the tabulated values are different quantities.

---

## ⚡ Exam Tips & Common Mistakes

1. **For Newton's optimization:** The iteration formula uses $f''$ in the denominator, not $f'$. You are finding where $f' = 0$, so Newton's method applies to $f'$ and uses its derivative $f''$.
2. **Always check the second derivative** after finding the critical point. A negative $f''$ means maximum, positive means minimum. Do not skip this.
3. **For tabulated data:** Build the difference table first. The sign pattern of $\Delta$ and $\Delta^2$ tells you where the optimum is and whether it is inside or outside the table.
4. **Use the backward form** when the optimum is near the end of the table, forward when it is near the start. Here the first differences are all positive but shrinking, so the peak is near the end.
5. **Constrained vs. unconstrained:** This is a short theory question. State the definition, give an example of each, and draw the comparison table. No computation needed.

## 🔗 Related Topics

- [NM-2.4: Newton-Raphson Method](NM-2.4_Newton_Raphson_Method.md) — same iteration, applied to $f(x) = 0$ instead of $f'(x) = 0$
- [NM-5.2: Simpson's 1/3 Rule](NM-5.2_Simpsons_One_Third_Rule.md) — numerical integration (related topic in the same exam question group)
- [NM-4.11: Difference Table Formation](NM-4.11_Difference_Table_Formation.md) — building difference tables for interpolation and optimization
- [NM-7: Numerical Differentiation](NM-7_Numerical_Differentiation.md) — derivative formulas from tabulated data

---

[← Previous: NM-5 Lower — Trapezoidal, 3/8, Romberg](NM-5_Lower_Trapezoidal_38_Romberg_Error_Applied.md) | [🏠 Index](00_Index.md) | [Next: NM-7 Numerical Differentiation →](NM-7_Numerical_Differentiation.md)
