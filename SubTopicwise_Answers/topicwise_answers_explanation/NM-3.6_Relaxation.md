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

Every block below is copied from `../answers_explanation/`. The reasoning
is written once, in the year-wise file, and is not restated here.


### [2017 Q.4(c)]

**Question.** Use the Gauss Seidel method with relaxation $(\lambda = 0.95)$ to solve the following system. If necessary rearrange the equations to achieve convergence (use 3 iterations only).

*[Marks: 05]*

**Solution.**

$$
\begin{aligned}
-3x_1 + x_2 + 12x_3 &= 50 \\
6x_1 - x_2 - x_3 &= 3 \\
6x_1 + 9x_2 + x_3 &= 40
\end{aligned}
$$

**Step 1, check diagonal dominance of the printed system.**
- Row 1: $\lvert -3\rvert = 3$ against $1 + 12 = 13$ (fails).
- Row 2: $\lvert -1\rvert = 1$ against $6 + 1 = 7$ (fails).
- Row 3: $\lvert 9\rvert = 9$ against $6 + 1 = 7$ (dominant).

Because rows 1 and 2 violate diagonal dominance, applying Gauss-Seidel directly to the equations in this order causes immediate divergence.

**Step 2, rearrange the equations to achieve convergence.**
The prompt explicitly instructs: *"If necessary rearrange the equations to achieve convergence"*.
To satisfy the criterion of strict diagonal dominance ($\lvert a_{ii}\rvert > \sum_{j \ne i} \lvert a_{ij}\rvert$), we align each equation with the variable that possesses its largest coefficient:
1. In Equation 2 ($-x_2 - x_3 + 6x_1 = 3$), the coefficient of $x_1$ is $6$, and $|6| > |-1| + |-1| = 2$. Make this **Row 1** (to solve for $x_1$).
2. In Equation 3 ($6x_1 + 9x_2 + x_3 = 40$), the coefficient of $x_2$ is $9$, and $|9| > |6| + |1| = 7$. Make this **Row 2** (to solve for $x_2$).
3. In Equation 1 ($-3x_1 + x_2 + 12x_3 = 50$), the coefficient of $x_3$ is $12$, and $|12| > |-3| + |1| = 4$. Make this **Row 3** (to solve for $x_3$).

The rearranged system is:

$$
\begin{aligned}
6x_1 - x_2 - x_3 &= 3 \\
6x_1 + 9x_2 + x_3 &= 40 \\
-3x_1 + x_2 + 12x_3 &= 50
\end{aligned}
$$

The coefficient matrix is:

$$A = \begin{bmatrix} 6 & -1 & -1 \\ 6 & 9 & 1 \\ -3 & 1 & 12 \end{bmatrix}$$

Every row is strictly diagonally dominant. Therefore, the Gauss-Seidel method is **guaranteed to converge** from any starting vector.

**Step 3, set up the iteration with relaxation.**
Express each variable from its dominant equation:

$$\hat x_1^{(k+1)} = \frac{3 + x_2^{(k)} + x_3^{(k)}}{6}$$

$$\hat x_2^{(k+1)} = \frac{40 - 6x_1^{(k+1)} - x_3^{(k)}}{9}$$

$$\hat x_3^{(k+1)} = \frac{50 + 3x_1^{(k+1)} - x_2^{(k+1)}}{12}$$

With relaxation parameter $\lambda = 0.95$, the updated value is a weighted combination of the previous iterate and the freshly computed Gauss-Seidel candidate:

$$x_i^{(k+1)} = (1 - \lambda) x_i^{(k)} + \lambda \hat x_i^{(k+1)} = 0.05\,x_i^{(k)} + 0.95\,\hat x_i^{(k+1)}$$

**Step 4, compute 3 iterations starting from $x^{(0)} = (0, 0, 0)$.**

**Iteration 1:**
- $\hat x_1^{(1)} = \frac{3 + 0 + 0}{6} = 0.500000 \implies x_1^{(1)} = 0.95(0.500000) = 0.475000$
- Using latest $x_1^{(1)} = 0.475000$:
  $$\hat x_2^{(1)} = \frac{40 - 6(0.475000) - 0}{9} = \frac{37.150000}{9} = 4.127778 \implies x_2^{(1)} = 0.95(4.127778) = 3.921389$$
- Using latest $x_1^{(1)} = 0.475000$ and $x_2^{(1)} = 3.921389$:
  $$\hat x_3^{(1)} = \frac{50 + 3(0.475000) - 3.921389}{12} = \frac{47.503611}{12} = 3.958634 \implies x_3^{(1)} = 0.95(3.958634) = 3.760703$$

**Iteration 2:**
- $\hat x_1^{(2)} = \frac{3 + 3.921389 + 3.760703}{6} = 1.780349 \implies x_1^{(2)} = 0.05(0.475000) + 0.95(1.780349) = 1.715081$
- Using latest $x_1^{(2)} = 1.715081$:
  $$\hat x_2^{(2)} = \frac{40 - 6(1.715081) - 3.760703}{9} = 2.883201 \implies x_2^{(2)} = 0.05(3.921389) + 0.95(2.883201) = 2.935111$$
- Using latest $x_1^{(2)} = 1.715081$ and $x_2^{(2)} = 2.935111$:
  $$\hat x_3^{(2)} = \frac{50 + 3(1.715081) - 2.935111}{12} = 4.350844 \implies x_3^{(2)} = 0.05(3.760703) + 0.95(4.350844) = 4.321337$$

**Iteration 3:**
- $\hat x_1^{(3)} = \frac{3 + 2.935111 + 4.321337}{6} = 1.709408 \implies x_1^{(3)} = 0.05(1.715081) + 0.95(1.709408) = 1.709692$
- Using latest $x_1^{(3)} = 1.709692$:
  $$\hat x_2^{(3)} = \frac{40 - 6(1.709692) - 4.321337}{9} = 2.824501 \implies x_2^{(3)} = 0.05(2.935111) + 0.95(2.824501) = 2.830032$$- Using latest $x_1^{(3)} = 1.709692$ and $x_2^{(3)} = 2.830032$:
  $$\hat x_3^{(3)} = \frac{50 + 3(1.709692) - 2.830032}{12} = 4.358254 \implies x_3^{(3)} = 0.05(4.321337) + 0.95(4.358254) = 4.356408$$

**Iteration table.**

| Iteration | $x_1$ | $x_2$ | $x_3$ |
| :--: | :-- | :-- | :-- |
| 0 | $0.000000$ | $0.000000$ | $0.000000$ |
| 1 | $0.475000$ | $3.921389$ | $3.760703$ |
| 2 | $1.715081$ | $2.935111$ | $4.321337$ |
| 3 | $1.709692$ | $2.830032$ | $4.356408$ |

$$\boxed{x_1 \approx 1.7097, \qquad x_2 \approx 2.8300, \qquad x_3 \approx 4.3564}$$

> [!info] Check against the exact solution and convergence behavior
> The exact closed-form solution obtained by Cramer's rule or Gaussian elimination is:
> $$(x_1, x_2, x_3) = \left(\frac{129}{76}, \frac{215}{76}, \frac{331}{76}\right) \approx (1.697368, 2.828947, 4.355263)$$
>
> By iteration 3, the relaxed iterates $(1.7097, 2.8300, 4.3564)$ have already converged
> within $\approx 0.01$ of the exact values.
>
> **Crucial lesson on rearrangement:** If the equations are not rearranged, the Gauss-Seidel
> iteration matrix has spectral radius $\rho \approx 6.38$, causing iterates to explode
> into the millions ($x_3^{(3)} \approx 3.5 \times 10^7$). Reordering rows to place the largest
> elements on the diagonal brings the spectral radius strictly below 1, turning rapid divergence
> into rapid convergence.

---

---

### [2018 Q.4(a)]

**Question.** What is meant by over-relaxation and under-relaxation?

*[Marks: 02]*

**Solution.**

Both terms describe a modification of the Gauss-Seidel iteration that inserts a
**relaxation parameter** $\omega$:

$$x_i^{(k+1)} = (1 - \omega)x_i^{(k)} + \omega\hat x_i^{(k)}$$

where $\hat x_i^{(k)}$ is the value the ordinary Gauss-Seidel recursion would
have produced from iteration $k$.

**Under-relaxation, $0 < \omega < 1$.** Each new iterate is a blend of the old
value and the Gauss-Seidel value, so the sequence advances by a *fraction* of
the full step. This damps oscillation and is what you reach for when the plain
iteration oscillates or diverges: the effective step is smaller, so the spectral
radius of the iteration matrix comes down, at the cost of more iterations.

**Over-relaxation, $1 < \omega < 2$.** Each new iterate *overshoots* the plain
Gauss-Seidel value, so the sequence covers the distance faster. The method is
then called Successive Over-Relaxation, SOR, and an optimal $\omega$ can cut
the iteration count substantially.

**The two regimes are separated by $\omega = 1$.** At $\omega = 1$ the formula
reduces to ordinary Gauss-Seidel. Above $1$ it is accelerated, below $1$ it is
stabilised. The purpose in both cases is the same: to control the rate at which
error is carried from one iteration to the next.

> [!note] Why not simply take $\omega$ large?
> Overshoot only helps while the iteration is still contracting. Past
> $\omega_{\text{opt}}$ the spectral radius starts growing again and the
> iteration diverges, so $\omega$ must stay below $2$ and in practice close to
> $1$.

---

[🏠 Subtopic Index](00_Index.md) | [← Prev: NM-3.5 Gauss-Seidel Iteration](NM-3.5_Gauss_Seidel_Iteration.md) | [Next: NM-3.7 Ill-Conditioned Systems →](NM-3.7_Ill_Conditioned_Systems.md)
