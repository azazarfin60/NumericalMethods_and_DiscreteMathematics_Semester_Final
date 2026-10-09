---
title: "NM-8.8 · Boundary Value Problems"
tags:
  - numerical-methods
  - discrete-mathematics
  - topicwise
---

# NM-8.8 · Boundary Value Problems

Every block below is copied from `../answers_explanation/`. The reasoning
is written once, in the year-wise file, and is not restated here.


### [2021 Q.5(b)]

**Question.** Solve the boundary value problem $\frac{d^2y}{dx^2} - y = 0$ with $y(0) = 0$ and $y(2) = 3.62686$.

*[Marks: 05, CO: 3]*

**Solution.**

**Step 1. Discretise.** With the centred difference for $y''$,

$$
\frac{y_{i-1} - 2y_i + y_{i+1}}{h^2} - y_i = 0
$$

Multiplying by $h^2$,

$$
y_{i-1} - (2 + h^2)\,y_i + y_{i+1} = 0
$$

The system is tridiagonal with diagonal $-(2+h^2)$ and off-diagonal $1$.

> [!note] Check the sign and the dominance before iterating
> The matrix is **negatively diagonally dominant**, since $\lvert 2+h^2\rvert > 1+1$
> for every $h$. That guarantees a unique solution and means the standard Thomas
> algorithm applies **without pivoting**.
>
> Worth pausing on, because it is the first question in this paper where the sign
> of $y_i$ on the diagonal is decided by the ODE rather than by taste. $y'' - y = 0$
> gives $\frac{y_{i-1}-2y_i+y_{i+1}}{h^2} = y_i$, and moving $y_i$ across gives a
> diagonal of $-(2+h^2)$, not $+(2+h^2)$. Writing the positive sign produces a
> system with a completely different spectrum and, for this $y(2)$, no consistent
> solution.

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

$$\boxed{y(0.5) = 0.5263,\quad y(1.0) = 1.1843,\quad y(1.5) = 2.1383 \quad (h = 0.5)}$$

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

> [!info] Check against the continuous solution
> The ODE $y'' - y = 0$ has the general solution $y = A\cosh x + B\sinh x$. From
> $y(0) = 0$, $A = 0$. From $y(2) = 3.62686$,
> $$B = \frac{3.62686}{\sinh 2} = \frac{3.62686}{3.6268604} = 0.99999989$$
> so
> $$y = 3.62686\,\frac{\sinh x}{\sinh 2}$$
> Exact values at the three interior nodes are $0.521095$, $1.175201$ and
> $2.129279$. The numerical values overshoot by under $1\%$, as expected for a
> second-order scheme on a growing exponential.

> [!warning] The halving ratio is the check that the order is what you think
> The four rows of the refinement table are not decoration; they are the only
> evidence that the scheme is second order. A ratio near 4 means the
> $O(h^2)$ term dominates. A ratio near 2 would mean the scheme is only first
> order, and a ratio near 8 or 16 would mean something is wrong with the
> difference stencil rather than right about it.
>
> $3.65$ rather than exactly $4$ is expected: at $h = 0.5$ there are only three
> interior nodes, so higher-order terms have not yet died away.

> [!note] Why the boundary value is suspicious, and what it tells you
> The printed $y(2) = 3.62686$ is a rounded value: $\sinh 2 = 3.6268604\ldots$
> gives $B$ exactly $1$ to seven figures, so the intended exact solution is almost
> certainly $y = \sinh x$. That is a strong hint the question was built backwards
> from a known answer.
>
> It also means the "error" quoted above is almost entirely scheme error, not the
> $4 \times 10^{-7}$ rounding in the boundary condition. With the exact condition
> $y(2) = \sinh 2$, the $h = 0.5$ numerical solution is $0.52634$ against an exact
> $0.52109$, and the same $0.9\%$ gap remains. So the gap is real and belongs to
> the scheme.

---

### [2024 Q.4(a)]

**Question.** Describe the general approach for solving boundary value problems numerically. How does it differ from solving initial value problems?

*[Marks: 03, CO: 1]*

**Solution.**

**What a boundary value problem is.** A boundary value problem (BVP) gives
conditions at more than one point of the domain. The standard statement is a
differential equation on $[a, b]$ plus values of $y$ at $a$ and at $b$:

$$y'' = f(x, y, y'), \qquad y(a) = y_a, \qquad y(b) = y_b$$

An initial value problem (IVP) gives both conditions at the same point, usually
the left end, and asks for the solution at later points.

**The general numerical approach.** Three steps, and they are the same for every
BVP method:

1. **Discretise the domain.** Replace $[a, b]$ by a finite set of nodes
   $x_0, x_1, \ldots, x_n$ with spacing $h$. The solution is now sought at the
   nodes only, rather than at every point.
2. **Replace derivatives by finite differences.** Each derivative in the
   equation is replaced by an approximation involving nodal values. For
   $y''$ the standard choice is the central difference

   $$y''_i \approx \frac{y_{i+1} - 2y_i + y_{i-1}}{h^2}$$

   After this step the differential equation has become a linear (or nonlinear)
   **algebraic** equation at each interior node.
3. **Assemble and solve.** Collecting the nodal equations gives one algebraic
   system with $n - 1$ unknowns for $n-1$ interior nodes. The boundary values
   supply the terms that are already known. Solve the system, by elimination or,
   for a large mesh, by an iterative method such as Gauss-Seidel.

**Why the discretisation is sound.** The central difference for $y''$ is
second-order accurate, meaning the error is $O(h^2)$. Taylor expanding
$y(x \pm h)$ and subtracting gives

$$\frac{y_{i+1} - 2y_i + y_{i-1}}{h^2} = y''_i + \frac{h^2}{12}y^{(4)}_i + \cdots$$

so the approximation becomes exact as $h \to 0$, and the method converges.

**How it differs from an initial value problem.** The difference is not cosmetic;
it changes the whole structure of the computation.

| | Initial value problem | Boundary value problem |
| :-- | :-- | :-- |
| Where conditions are given | all at $x = a$ | at both $x = a$ and $x = b$ |
| Shape of the computation | marching, one node at a time | simultaneous, all nodes together |
| Does the solution grow or decay | matters greatly, errors accumulate | irrelevant, solved as a system |
| Method family | Euler, RK4, predictor-corrector | shooting, finite differences, relaxation |
| Can one value be found alone | yes, by marching to it | no, the whole mesh is coupled |

The one-line version: **an IVP can be solved by marching, a BVP cannot.** A BVP
must be solved as a simultaneous system, which is why the numerical linear
algebra of the earlier sections suddenly becomes relevant.

**Shooting, as the alternative.** The shooting method converts the BVP into a
sequence of IVPs: guess the missing initial slope, march forward, compare the
result at $x = b$ against the required value, and correct the guess. It is the
method of choice when the IVP machinery is already reliable and the interval is
long, and it fails when the underlying IVP is unstable, which is common.

> [!note] Why this is worth three marks
> The marks are for the three-step discretise-replace-solve structure and for the
> marching-versus-simultaneous contrast. Writing down the central difference
> formula without saying *why* a system appears gets the first mark only.

---
