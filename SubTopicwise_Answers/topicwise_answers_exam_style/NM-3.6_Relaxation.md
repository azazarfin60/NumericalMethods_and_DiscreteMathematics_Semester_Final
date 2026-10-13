---
title: "NM-3.6 · Relaxation"
tags:
  - numerical-methods
  - discrete-mathematics
  - topicwise
---


[🏠 Subtopic Index](00_Index.md) | [← Prev: NM-3.5 Gauss-Seidel Iteration](NM-3.5_Gauss_Seidel_Iteration.md) | [Next: NM-3.7 Ill-Conditioned Systems →](NM-3.7_Ill_Conditioned_Systems.md)

---

# NM-3.6 · Relaxation

Every block below is copied from `../answers_exam_style/`, which is the
only place an answer is authored. A number here is the same number, character
for character, as the one it came from.


### [2017 Q.4(c)]

**Question.** Use the Gauss Seidel method with relaxation $(\lambda = 0.95)$ to solve the following system. If necessary rearrange the equations to achieve convergence (use 3 iterations only).

**Solution.**

$$
\begin{aligned}
-3x_1 + x_2 + 12x_3 &= 50 \\
6x_1 - x_2 - x_3 &= 3 \\
6x_1 + 9x_2 + x_3 &= 40
\end{aligned}
$$

**Check for diagonal dominance.** In the given printed order:
- Row 1: $|{-3}| = 3 < |1| + |12| = 13$ (not dominant)
- Row 2: $|{-1}| = 1 < |6| + |1| = 7$ (not dominant)
- Row 3: $|9| = 9 > |6| + |1| = 7$ (dominant)

The system in the printed order is not diagonally dominant, which would cause Gauss-Seidel to diverge.

**Rearrange the equations.** To achieve convergence, we rearrange the rows so that the largest coefficient in magnitude in each row lies on the main diagonal:
1. Make Equation 2 the **first row** (solve for $x_1$): $|6| > |-1| + |-1| = 2$.
2. Make Equation 3 the **second row** (solve for $x_2$): $|9| > |6| + |1| = 7$.
3. Make Equation 1 the **third row** (solve for $x_3$): $|12| > |-3| + |1| = 4$.

The rearranged system is:

$$
\begin{aligned}
6x_1 - x_2 - x_3 &= 3 \\
6x_1 + 9x_2 + x_3 &= 40 \\
-3x_1 + x_2 + 12x_3 &= 50
\end{aligned}
$$

The coefficient matrix is now:

$$A = \begin{bmatrix} 6 & -1 & -1 \\ 6 & 9 & 1 \\ -3 & 1 & 12 \end{bmatrix}$$

Every row satisfies strict diagonal dominance ($|a_{ii}| > \sum_{j \ne i} |a_{ij}|$), guaranteeing convergence of the Gauss-Seidel method.

**Iterative formulas.** Expressing each diagonal variable:

$$\hat x_1^{(k+1)} = \frac{3 + x_2^{(k)} + x_3^{(k)}}{6}$$

$$\hat x_2^{(k+1)} = \frac{40 - 6x_1^{(k+1)} - x_3^{(k)}}{9}$$

$$\hat x_3^{(k+1)} = \frac{50 + 3x_1^{(k+1)} - x_2^{(k+1)}}{12}$$

Applying relaxation with $\lambda = 0.95$:

$$x_i^{(k+1)} = (1 - \lambda)x_i^{(k)} + \lambda \hat x_i^{(k+1)} = 0.05\,x_i^{(k)} + 0.95\,\hat x_i^{(k+1)}$$

Starting from initial guess $x^{(0)} = (0, 0, 0)$:

**Iteration 1.**
- $\hat x_1^{(1)} = \frac{3 + 0 + 0}{6} = 0.500000 \implies x_1^{(1)} = 0.95(0.500000) = 0.475000$
- $\hat x_2^{(1)} = \frac{40 - 6(0.475000) - 0}{9} = \frac{37.150000}{9} = 4.127778 \implies x_2^{(1)} = 0.95(4.127778) = 3.921389$
- $\hat x_3^{(1)} = \frac{50 + 3(0.475000) - 3.921389}{12} = \frac{47.503611}{12} = 3.958634 \implies x_3^{(1)} = 0.95(3.958634) = 3.760703$

**Iteration 2.**
- $\hat x_1^{(2)} = \frac{3 + 3.921389 + 3.760703}{6} = 1.780349 \implies x_1^{(2)} = 0.05(0.475000) + 0.95(1.780349) = 1.715081$
- $\hat x_2^{(2)} = \frac{40 - 6(1.715081) - 3.760703}{9} = 2.883201 \implies x_2^{(2)} = 0.05(3.921389) + 0.95(2.883201) = 2.935111$
- $\hat x_3^{(2)} = \frac{50 + 3(1.715081) - 2.935111}{12} = 4.350844 \implies x_3^{(2)} = 0.05(3.760703) + 0.95(4.350844) = 4.321337$

**Iteration 3.**
- $\hat x_1^{(3)} = \frac{3 + 2.935111 + 4.321337}{6} = 1.709408 \implies x_1^{(3)} = 0.05(1.715081) + 0.95(1.709408) = 1.709692$
- $\hat x_2^{(3)} = \frac{40 - 6(1.709692) - 4.321337}{9} = 2.824501 \implies x_2^{(3)} = 0.05(2.935111) + 0.95(2.824501) = 2.830032$
- $\hat x_3^{(3)} = \frac{50 + 3(1.709692) - 2.830032}{12} = 4.358254 \implies x_3^{(3)} = 0.05(4.321337) + 0.95(4.358254) = 4.356408$

**Summary of iterations.**

| Iteration | $x_1$ | $x_2$ | $x_3$ |
| :--: | :-- | :-- | :-- |
| 0 | $0.000000$ | $0.000000$ | $0.000000$ |
| 1 | $0.475000$ | $3.921389$ | $3.760703$ |
| 2 | $1.715081$ | $2.935111$ | $4.321337$ |
| 3 | $1.709692$ | $2.830032$ | $4.356408$ |

$$\boxed{x_1 \approx 1.7097, \qquad x_2 \approx 2.8300, \qquad x_3 \approx 4.3564}$$

> [!info] Comparison with the exact solution
> The exact solution obtained by Gauss elimination is
> $(x_1, x_2, x_3) = (129/76, 215/76, 331/76) \approx (1.6974, 2.8289, 4.3553)$.
> After just 3 iterations of relaxed Gauss-Seidel on the rearranged system, all three
> unknowns are within $0.012$ of the exact solution, confirming rapid convergence.
>
> In contrast, running the iteration without rearranging the equations diverges
> immediately (growing to $10^7$ in 3 iterations) because the original row ordering
> violates diagonal dominance ($\rho(M) \approx 6.38$). Rearranging the equations was
> therefore essential to achieve convergence.

---

---

### [2018 Q.4(a)]

**Question.** What is meant by over-relaxation and under-relaxation?

**Solution.**

Both terms describe a modification of the Gauss-Seidel iteration in which a
**relaxation parameter** $\omega$ is introduced.

**Relaxed Gauss-Seidel.** The ordinary Gauss-Seidel update is replaced by

$$x_i^{(k+1)} = (1 - \omega)x_i^{(k)} + \omega\hat x_i^{(k)}$$

where $\hat x_i^{(k)}$ is the value obtained from the ordinary Gauss-Seidel
recursion applied to iteration $k$.

**Under-relaxation, $0 < \omega < 1$.** Each new iterate is a weighted blend of
the old value and the new one, so the sequence moves toward the solution by a
fraction of the full step. This damps oscillation and is used when the ordinary
iteration diverges or oscillates, because it reduces the effective step and
restores convergence at the cost of more iterations.

**Over-relaxation, $1 < \omega < 2$.** Each new iterate overshoots the ordinary
Gauss-Seidel value, so the sequence moves toward the solution faster than the
plain iteration. The method is then called Successive Over-Relaxation (SOR),
and the choice of optimal $\omega$ reduces the iteration count substantially.

**The two regimes separated by $\omega = 1$.** At $\omega = 1$ the formula
reduces to ordinary Gauss-Seidel. Above $1$ the iteration is accelerated; below
$1$ it is stabilised. The purpose in both cases is the same, which is to
control the rate at which error is carried from one iteration to the next.

---

[🏠 Subtopic Index](00_Index.md) | [← Prev: NM-3.5 Gauss-Seidel Iteration](NM-3.5_Gauss_Seidel_Iteration.md) | [Next: NM-3.7 Ill-Conditioned Systems →](NM-3.7_Ill_Conditioned_Systems.md)
