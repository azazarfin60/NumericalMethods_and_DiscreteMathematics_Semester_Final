---
title: "NM-3.4 · Jacobi Iteration"
tags:
  - numerical-methods
  - discrete-mathematics
  - topicwise
---



[🏠 Subtopic Index](00_Index.md) | [← Prev: NM-3.3 LU Decomposition & Matrix Inversion](NM-3.3_LU_Decomposition_and_Matrix_Inversion.md) | [Next: NM-3.5 Gauss-Seidel Iteration →](NM-3.5_Gauss_Seidel_Iteration.md)

---

# NM-3.4 · Jacobi Iteration

Every block below is copied from `../answers_explanation/`. The reasoning
is written once, in the year-wise file, and is not restated here.


### [2017 Q.7(a), 2022 Q.4(a)]

**Appeared in:** 2017 Q.7(a), 2022 Q.4(a)

**Question.** Solve the following system using Jacobi method.

*[Marks: 06]*

**Solution.**

$$
\begin{aligned}
6x + y + z &= 20 \\
x + 4y - z &= 6 \\
x - y + 5z &= 7
\end{aligned}
$$

**Jacobi iteration form.** Each equation is solved for its own unknown, using
only values from the previous sweep:

$$x^{(k+1)} = \frac{20 - y^{(k)} - z^{(k)}}{6}, \qquad y^{(k+1)} = \frac{6 - x^{(k)} + z^{(k)}}{4}, \qquad z^{(k+1)} = \frac{7 - x^{(k)} + y^{(k)}}{5}$$

**The defining feature of Jacobi: no value from the current sweep is used.**
That is the whole difference from Gauss-Seidel, and it is worth holding on to,
because writing $(k+1)$ in one of the three right-hand sides by accident turns
the method into Gauss-Seidel and gives a different table with the same
convergence guarantee.

**Convergence check.** The diagonal entries are $6$, $4$, $5$ and the
off-diagonal sums are $2$, $2$, $2$. Every row is strictly diagonally dominant,
so the Jacobi iteration converges.

**Iteration**, starting from $x = y = z = 0$:

| Sweep | $x$ | $y$ | $z$ |
| :--: | :-- | :-- | :-- |
| 1 | $3.333333$ | $1.500000$ | $1.400000$ |
| 2 | $2.850000$ | $1.016667$ | $1.033333$ |
| 3 | $2.991667$ | $1.045833$ | $1.033333$ |
| 4 | $2.986806$ | $1.010417$ | $1.010833$ |
| 5 | $2.996458$ | $1.006007$ | $1.004722$ |
| 6 | $2.998212$ | $1.002066$ | $1.001910$ |
| 7 | $2.999337$ | $1.000924$ | $1.000771$ |
| 8 | $2.999717$ | $1.000358$ | $1.000317$ |

**The exact solution, by elimination.** From the first equation,
$x = \frac{20 - y - z}{6}$. Substituting into the second,

$$\frac{20-y-z}{6} + 4y - z = 6 \implies 20 - y - z + 24y - 6z = 36 \implies 23y - 7z = 16$$

and into the third,

$$\frac{20-y-z}{6} - y + 5z = 7 \implies 20 - y - z - 6y + 30z = 42 \implies -7y + 29z = 22$$

Adding the two gives $16y + 22z = 38$; solving the pair gives $y = 1$, $z = 1$,
and then $x = \frac{20 - 1 - 1}{6} = 3$.

$$\boxed{x = 3, \qquad y = 1, \qquad z = 1}$$

> [!info] Checking by substitution and by the error pattern
> **Substitution** into all three original equations: $6(3) + 1 + 1 = 20$;
> $3 + 4(1) - 1 = 6$; $3 - 1 + 5(1) = 7$. All three hold exactly, and these are
> the equations the iteration was built from, so this is a check on the
> arithmetic and not on the method.
>
> **The error pattern** is the more interesting one. The errors in $x$ are
> $0.3333, 0.1500, 0.0083, 0.0132, 0.0035, 0.0018, 0.0007, 0.0003$. They shrink
> geometrically, with the Jacobi iteration matrix having spectral radius
> $\rho = 0.4073$, so roughly a factor of $2.5$ per sweep.
>
> But they are *not* monotone: they fall, then rise, then fall again. That is
> not noise. The iteration matrix has a negative eigenvalue, so the error vector
> rotates as it contracts, and a component can grow even as the whole vector
> shrinks. A student expecting each error to be a fixed fraction of the last
> will read the third entry as an improvement on the second and the fourth as a
> regression, and may conclude the iteration is not converging when it is.
>
> By sweep 8 all three components are correct to three decimal places, so the
> tabulated values are limited by the number of sweeps requested, not by the
> method. Had convergence been poor, the errors against the exact $(3,1,1)$
> would plateau instead of shrinking.

---

[🏠 Subtopic Index](00_Index.md) | [← Prev: NM-3.3 LU Decomposition & Matrix Inversion](NM-3.3_LU_Decomposition_and_Matrix_Inversion.md) | [Next: NM-3.5 Gauss-Seidel Iteration →](NM-3.5_Gauss_Seidel_Iteration.md)
