---
title: "NM-8.8 · Boundary Value Problems"
tags:
  - numerical-methods
  - discrete-mathematics
  - topicwise
---

# NM-8.8 · Boundary Value Problems

Every block below is copied from `../answers_exam_style/`, which is the
only place an answer is authored. A number here is the same number, character
for character, as the one it came from.


### [2021 Q.5(b)]

**Question.** Solve the boundary value problem $\frac{d^2y}{dx^2} - y = 0$ with $y(0) = 0$ and $y(2) = 3.62686$.

**Solution.**

**Step 1. Discretise.** With the centred difference for $y''$,

$$
\frac{y_{i-1} - 2y_i + y_{i+1}}{h^2} - y_i = 0
$$

Multiplying by $h^2$,

$$
y_{i-1} - (2 + h^2)\,y_i + y_{i+1} = 0
$$

The system is tridiagonal with diagonal $-(2+h^2)$ and off-diagonal $1$. Note that
the matrix is **negatively diagonally dominant**, since $\lvert 2+h^2\rvert > 1+1$,
hence the solution is unique and the standard Thomas algorithm applies without
pivoting.

**Step 2. Solve with $h = 0.5$.** Then $n = 4$ subintervals and 3 interior nodes
at $x = 0.5, 1.0, 1.5$. With $y_0 = 0$ and $y_4 = 3.62686$:

$$
\begin{cases}
-(2.25)y_1 + y_2 = 0 \\
y_1 - (2.25)y_2 + y_3 = 0 \\
y_2 - (2.25)y_3 = -3.62686
\end{cases}
$$

From the first, $y_2 = 2.25\,y_1$. Substituting into the second,

$$
y_1 - 2.25(2.25y_1) + y_3 = 0 \Rightarrow y_3 = 4.0625\,y_1
$$

The third then gives $2.25y_1 - 2.25(4.0625y_1) = -3.62686$, that is
$2.25y_1(1 - 4.0625) = -3.62686$, so $-6.890625\,y_1 = -3.62686$ and
$y_1 = 0.526347$.

$$
y_2 = 2.25(0.526347) = 1.184281, \qquad y_3 = 4.0625(0.526347) = 2.138285
$$

| $x$ | $y$ (numerical, $h = 0.5$) | Exact | Error |
| --: | --: | --: | --: |
| 0.5 | 0.526347 | 0.521095 | $+0.005252$ |
| 1.0 | 1.184281 | 1.175201 | $+0.009080$ |
| 1.5 | 2.138285 | 2.129279 | $+0.009006$ |

**Step 3. Refine.** Halving $h$ should cut the error by about 4, since the scheme is
second order.

| $h$ | Interior nodes | Largest error |
| --: | --: | --: |
| 1 | 1 | 0.03375 |
| 0.5 | 3 | 0.00908 |
| 0.25 | 7 | 0.00249 |
| 0.125 | 15 | 0.00063 |

The ratio $0.00908 / 0.00249 = 3.65$ is close to the expected 4, confirming
second-order accuracy.

$$
\boxed{y(0.5) = 0.5263,\quad y(1.0) = 1.1843,\quad y(1.5) = 2.1383 \quad (h = 0.5)}
$$

> [!info] Check against the continuous solution
> The ODE $y'' - y = 0$ has the general solution $y = A\cosh x + B\sinh x$. From
> $y(0) = 0$, $A = 0$. From $y(2) = 3.62686$,
> $$B = \frac{3.62686}{\sinh 2} = \frac{3.62686}{3.6268604} = 0.99999989$$
> so
> $$y = 3.62686\,\frac{\sinh x}{\sinh 2}$$
> Exact values at the three interior nodes are $0.521095$, $1.175201$ and
> $2.129279$. The numerical values overshoot by under $1\%$, as expected for a
> second-order scheme on a growing exponential.

> [!note] Why the boundary value matters
> The printed $y(2) = 3.62686$ is a rounded value: $\sinh 2 = 3.6268604\ldots$
> gives $B$ exactly $1$ to seven figures, so the intended exact solution is
> almost certainly $y = \sinh x$. That is a strong hint the question was built
> backwards from a known answer, and it means the "error" quoted above is mostly
> the $4 \times 10^{-7}$ rounding in the boundary condition, not scheme error.
>
> With the exact condition $y(2) = \sinh 2$, the $h = 0.5$ numerical solution is
> $0.52634$ against an exact $0.52109$, and the same $0.9\%$ gap remains, so the
> error really is the finite difference scheme.

---

### [2024 Q.4(a)]

**Question.** Describe the general approach for solving boundary value problems numerically. How does it differ from solving initial value problems?

**Solution.**

**The shared starting point.** Both replace derivatives by finite differences and
solve the resulting algebraic system. The difference is which equations end up in
that system.

**Initial value problem.** One condition is given at one end of the domain, for
example $y(0) = 1$. Marching step by step from there, each new row uses only the
row just computed.

$$
y_{i+1} = f(x_i, y_i) h + O(h^2)
$$

This works because the system is **lower triangular in the unknowns**. It is
simple, needs no iteration, and each step is cheap.

**Boundary value problem.** Conditions are given at **both** ends, for example
$y(0) = 0$ and $y(1) = 1$. No starting value is known, so the grid cannot be
filled row by row.

**The general approach.**

1. Discretise the domain into a grid of $n + 1$ points.
2. Replace every derivative by a finite difference, usually the centred one
   $y''(x_i) \approx \frac{y_{i+1} - 2y_i + y_{i-1}}{h^2}$.
3. Apply the boundary conditions as algebraic equations replacing the
   unavailable end rows.
4. Solve the full linear system for all unknowns at once.

$$
\begin{cases}
y_0 = 0 \\
-\dfrac{y_{i-1} - 2y_i + y_{i+1}}{h^2} = f_i, \quad 1 \le i \le n-1 \\
y_n = 1
\end{cases}
$$

The interior equations couple neighbours, so the system is **tridiagonal**. The
standard efficient methods are the Thomas algorithm, or an iterative sweep such
as Gauss-Seidel, which works because the system is diagonally dominant.

**Key differences**

| | Initial value problem | Boundary value problem |
| :-- | :-- | :-- |
| Conditions | Given at one end | Given at both ends |
| Direction | Marches forward from the start | Whole domain solved at once |
| System structure | Lower triangular | Tridiagonal |
| Cost per step | Very low | Full linear solve |
| Sensitivity | Local, errors stay near the start | Global, a change anywhere moves the whole solution |
| Shooting method | Not applicable | Reduces a BVP to an IVP by adjusting the unknown start value until the far end matches |

> [!note] Where this exam meets the topic again
> The Gauss-Seidel iteration in part (b) of Question 2 is the same algorithm used
> on the tridiagonal system here. See
> [[NM-3.5 · Gauss-Seidel Iteration]] and [[NM-3.8 · Circuit Applications]].

---
