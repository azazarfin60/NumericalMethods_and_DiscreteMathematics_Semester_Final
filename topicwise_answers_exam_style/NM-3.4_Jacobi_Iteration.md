---
title: "NM-3.4 · Jacobi Iteration"
tags:
  - numerical-methods
  - discrete-mathematics
  - topicwise
---

# NM-3.4 · Jacobi Iteration

Every block below is copied from `../answers_exam_style/`, which is the
only place an answer is authored. A number here is the same number, character
for character, as the one it came from.


### [2017 Q.7(a), 2022 Q.4(a)]

**Appeared in:** 2017 Q.7(a), 2022 Q.4(a)

**Question.** Solve the following system using Jacobi method.

**Solution.**

$$
\begin{aligned}
6x + y + z &= 20 \\
x + 4y - z &= 6 \\
x - y + 5z &= 7
\end{aligned}
$$

**Jacobi iteration form.** Each equation is solved for its own unknown, using
only the values from the previous sweep:

$$x^{(k+1)} = \frac{20 - y^{(k)} - z^{(k)}}{6}$$

$$y^{(k+1)} = \frac{6 - x^{(k)} + z^{(k)}}{4}$$

$$z^{(k+1)} = \frac{7 - x^{(k)} + y^{(k)}}{5}$$

**Convergence check.** The diagonal entries are $6$, $4$, $5$ and the
off-diagonal sums are $2$, $2$, $2$. Every row is strictly diagonally dominant,
and the Jacobi iteration converges.

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

The exact solution is obtained by eliminating, for instance $x$ from the second
and third equations using the first:

$$x = \frac{20 - y - z}{6}$$

Substituting into equations 2 and 3 and clearing fractions gives
$23y - 7z = 16$ and $-7y + 29z = 22$, whence $y = 1$, $z = 1$ and then
$x = 3$.

$$\boxed{x = 3, \qquad y = 1, \qquad z = 1}$$

> [!info] Check by substitution and by the Jacobi error pattern
> Substituting into all three original equations: $6(3) + 1 + 1 = 20$ ✓;
> $3 + 4(1) - 1 = 6$ ✓; $3 - 1 + 5(1) = 7$ ✓. All three are satisfied exactly.
> The iteration errors $\varepsilon^{(k)}$ themselves converge geometrically:
> $\varepsilon_x$ falls $0.3333, 0.1500, 0.0083, 0.0132, 0.0035, 0.0018,
> 0.0007, 0.0003$, the pattern of an iterative matrix whose spectral radius is
> $\rho = 0.4073$, about a factor of $2.5$ per sweep. Note the errors are *not*
> monotone: they fall, then rise, then fall again, because the iteration matrix
> has a negative eigenvalue and the error vector rotates as it contracts, so the
> third entry is not an improvement on the second and the fourth is not a
> regression.
> By sweep 8 all three components are correct to three decimal places, so the
> tabulated values are limited by the number of sweeps requested, not by the
> method. Had the convergence been poor the residuals against the exact
> $(3, 1, 1)$ would plateau instead of shrinking; here they shrink by roughly a
> factor of $2.5$ per sweep.

---
