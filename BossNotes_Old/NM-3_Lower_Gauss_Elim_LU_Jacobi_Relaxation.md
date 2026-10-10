[← Previous: NM-3.8 Circuit Applications](NM-3.8_Circuit_Applications.md) | [🏠 Index](00_Index.md) | [Next: NM-4.1 Curve Fitting Concepts →](NM-4.1_Curve_Fitting_Concepts.md)

---

# NM-3 Lower Tier: Gauss Elimination, LU Decomposition, Jacobi Iteration, Relaxation, and Ill-Conditioned Systems
> **Section:** A (Numerical Methods) | **Priority:** 🟠🟡 (merged lower tier)
> **Subtopics Covered:** NM-3.1 (Gauss Elimination), NM-3.3 (LU Decomposition), NM-3.4 (Jacobi Iteration), NM-3.6 (Relaxation), NM-3.7 (Ill-Conditioned Systems)
> **Sources:** Jain Ch.7 §7.3, §7.5, §7.6, Topicwise NM-3.1, NM-3.3, NM-3.4, NM-3.6, NM-3.7, Shishir Notes §02

## Why This Topic Matters

While Gauss-Seidel and pivoting dominate the numerical linear algebra questions, these five companion subtopics provide the complete theoretical framework tested across semester finals. They test direct elimination algorithms, matrix factorizations, alternative iterative schemes, convergence acceleration, and numerical stability. Mastering this note gives you complete coverage of direct solvers, LU factorisation, Jacobi iteration sweeps, relaxation acceleration, and matrix conditioning.

---

## NM-3.1: Direct Methods and Gauss Elimination

### 📝 Definitions for NM-3.1

> **Direct Methods:** "these methods yield the solution after an amount of computation that is known in advance ... in a direct method the amount of computation is fixed." — Jain, §7.6 (p. 279)

> **Gauss Elimination:** A direct elimination procedure that transforms the augmented matrix $[A \mid B]$ into upper triangular form via elementary row operations, followed by back-substitution to determine the unknowns.

---

### Core Theory: Gauss Elimination

To solve $A\mathbf{x} = \mathbf{b}$ for an $n \times n$ system:

1. **Forward Elimination:** For step $k = 1, 2, \dots, n-1$, eliminate unknown $x_k$ from all rows below row $k$:

$$
m_{ik} = \frac{a_{ik}}{a_{kk}}, \qquad \text{Row}_i \leftarrow \text{Row}_i - m_{ik}\,\text{Row}_k \quad (i = k+1, \dots, n)
$$

   This reduces the matrix to upper triangular form:
   $$
   \begin{bmatrix}
   u_{11} & u_{12} & \cdots & u_{1n} \\
   0 & u_{22} & \cdots & u_{2n} \\
   \vdots & \vdots & \ddots & \vdots \\
   0 & 0 & \cdots & u_{nn}
   \end{bmatrix}
   \begin{bmatrix} x_1 \\ x_2 \\ \vdots \\ x_n \end{bmatrix}
   =
   \begin{bmatrix} c_1 \\ c_2 \\ \vdots \\ c_n \end{bmatrix}
   $$

2. **Back-Substitution:** Compute the unknowns from bottom to top:

$$
x_n = \frac{c_n}{u_{nn}}
$$

$$
x_i = \frac{1}{u_{ii}}\left( c_i - \sum_{j=i+1}^n u_{ij} x_j \right), \quad i = n-1, n-2, \dots, 1
$$

3. **Computational Complexity:**
   - Forward elimination requires roughly $\frac{2}{3}n^3$ arithmetic operations.
   - Back-substitution requires roughly $n^2$ operations.
   - Total operation count scales as $O(n^3)$.

| Direct Method | Operation Count | Storage | Key Characteristic |
| :-- | :-- | :-- | :-- |
| **Gauss Elimination** | $\frac{2}{3}n^3$ | $n^2$ | Standard direct solver with back-substitution |
| **Gauss-Jordan** | $n^3$ | $n^2$ | Eliminates above and below; finds matrix inverse directly |
| **LU Factorisation** | $\frac{2}{3}n^3$ (factor) $+ 2n^2$ (solve) | $n^2$ | Efficient when solving multiple right-hand sides |
| **Cholesky** | $\frac{1}{3}n^3$ | $\frac{1}{2}n^2$ | Symmetric positive definite systems only |

---

### 🏆 Golden Questions for NM-3.1

#### 🎯 Discuss Gauss Elimination method to solve linear simultaneous algebraic equations.
> **Appeared:** 2019 Q.3(a) — (04 marks)

**Full Answer:**

**Gauss elimination** solves $Ax = b$ by transforming the coefficient matrix into upper triangular form using elementary row operations, then recovering the unknowns by back substitution. The solution set is unchanged, since every operation is reversible.

**The system.** For $n$ equations in $n$ unknowns:

$$
a_{11}x_1 + a_{12}x_2 + \cdots + a_{1n}x_n = b_1
$$

$$
\vdots
$$

$$
a_{n1}x_1 + a_{n2}x_2 + \cdots + a_{nn}x_n = b_n
$$

**Steps:**

1. **Forward elimination.** Using $R_1$, eliminate $x_1$ from $R_2$ through $R_n$ by forming $R_i \leftarrow R_i - \frac{a_{i1}}{a_{11}}R_1$. Then use the modified $R_2$ to eliminate $x_2$ from $R_3$ through $R_n$, and continue. After pass $k$ the first $k$ equations have $k$ non-zero coefficients and the remaining have zeros in the first $k$ columns.
2. **Triangular system.** After $n-1$ passes the matrix is upper triangular:

$$
u_{11}x_1 + u_{12}x_2 + \cdots + u_{1n}x_n = b_1'
$$

$$
\qquad\qquad u_{22}x_2 + \cdots + u_{2n}x_n = b_2'
$$

$$
\qquad\qquad\qquad\qquad \ddots \qquad \vdots
$$

$$
\qquad\qquad\qquad\qquad u_{nn}x_n = b_n'
$$

3. **Back substitution.** From the last equation, $x_n = b_n'/u_{nn}$. Substitute into the $(n-1)$-th, giving $x_{n-1}$, and continue upward to $x_1$.
4. **Division by zero.** If a pivot $u_{kk}$ is zero, the row is exchanged with one below having a non-zero entry in that column (partial pivoting).
5. **Verification.** Substitute the obtained vector back into the original system.

**Operation count.** Forward elimination needs roughly $\frac{n^3}{3}$ multiplications and divisions; back substitution needs $\frac{n^2}{2}$. Total cost grows as $n^3$.

---

#### 🎯 What are the direct methods to solve linear system of equations? Describe any one of them.
> **Appeared:** 2020 Q.4(a) — (04 marks)

**Full Answer:**

**The system.** To solve $A\mathbf{x} = \mathbf{b}$, where $A = [a_{ij}] \in \mathbb{R}^{n\times n}$.
Direct methods produce the exact solution in a **fixed** number of arithmetic steps determined in advance by $n$, without iterative refinement.

**The two primary families:**
1. **Elimination methods:** Reduce the augmented system to triangular or diagonal form by elementary row operations, followed by back-substitution. Examples: **Gaussian elimination**, **Gauss-Jordan elimination**.
2. **Matrix factorisation methods:** Factor $A$ into a product of structured matrices and solve each factor sequentially. Examples: **LU factorisation (Doolittle, Crout)**, **Cholesky factorisation** ($A = LL^T$ for symmetric positive-definite matrices), **QR factorisation**.

**Description: Gaussian elimination with partial pivoting.**
Write the augmented matrix $[\,A \mid \mathbf{b}\,]$. For column $k$, locate the row $p \ge k$ with the largest absolute pivot $\lvert a_{pk}\rvert$, and swap rows $k$ and $p$.
Eliminate entries below the pivot:

$$
\text{for } i = k+1, \dots, n: \qquad m_{ik} = \frac{a_{ik}}{a_{kk}}, \qquad \text{row}_i \leftarrow \text{row}_i - m_{ik}\,\text{row}_k
$$

Repeat for $k = 1, 2, \dots, n-1$. Back-substitute from the bottom:

$$
x_n = \frac{c_n}{a_{nn}}, \qquad x_i = \frac{1}{a_{ii}}\left(c_i - \sum_{j=i+1}^{n} a_{ij} x_j\right)
$$

**Worked micro-example:** Solve $2x + y = 5$ and $x - y = 1$.

$$
\begin{bmatrix} 2 & 1 & | & 5 \\ 1 & -1 & | & 1 \end{bmatrix}
$$

Multiplier $m_{21} = \frac{1}{2}$. Row 2 becomes:
$[0, -1 - \frac{1}{2} \mid 1 - \frac{5}{2}] = [0, -\frac{3}{2} \mid -\frac{3}{2}]$.
Back-substituting: $y = \frac{-3/2}{-3/2} = 1$, then $2x = 5 - 1 = 4 \implies x = 2$.

$$
\boxed{x = 2, \qquad y = 1}
$$

$$
\boxed{\text{Eliminate to upper triangular form, pivot to stay safe, then back-substitute}}
$$

---

#### 🎯 Solve the system using Gauss elimination: $2x_1 + x_2 - x_3 = -1$, $x_1 - 2x_2 + 3x_3 = 9$, $3x_1 - x_2 + 5x_3 = 14$. Check your answer by substituting into the original equations.
> **Appeared:** 2022 Q.4(b) — (05 marks)

**Full Answer:**

**Step 1: Write the augmented matrix.**

$$
\left[\begin{array}{ccc|c}
2 & 1 & -1 & -1 \\
1 & -2 & 3 & 9 \\
3 & -1 & 5 & 14
\end{array}\right]
$$

**Step 2: Eliminate $x_1$ from rows 2 and 3.**
Row 2: $R_2 \leftarrow R_2 - \frac{1}{2}R_1$:

$$
[1 - 1,\; -2 - \tfrac{1}{2},\; 3 - \tfrac{1}{2}(-1),\; 9 - \tfrac{1}{2}(-1)] = [0,\; -\tfrac{5}{2},\; \tfrac{7}{2},\; \tfrac{19}{2}]
$$

Row 3: $R_3 \leftarrow R_3 - \frac{3}{2}R_1$:

$$
[3 - 3,\; -1 - \tfrac{3}{2},\; 5 - \tfrac{3}{2}(-1),\; 14 - \tfrac{3}{2}(-1)] = [0,\; -\tfrac{5}{2},\; \tfrac{13}{2},\; \tfrac{31}{2}]
$$

$$
\left[\begin{array}{ccc|c}
2 & 1 & -1 & -1 \\
0 & -\frac{5}{2} & \frac{7}{2} & \frac{19}{2} \\
0 & -\frac{5}{2} & \frac{13}{2} & \frac{31}{2}
\end{array}\right]
$$

**Step 3: Eliminate $x_2$ from row 3.**
Multiplier is $\frac{-5/2}{-5/2} = 1$, so $R_3 \leftarrow R_3 - R_2$:

$$
[0,\; 0,\; \tfrac{13}{2} - \tfrac{7}{2},\; \tfrac{31}{2} - \tfrac{19}{2}] = [0,\; 0,\; 3,\; 6]
$$

$$
\left[\begin{array}{ccc|c}
2 & 1 & -1 & -1 \\
0 & -\frac{5}{2} & \frac{7}{2} & \frac{19}{2} \\
0 & 0 & 3 & 6
\end{array}\right]
$$

**Step 4: Back-substitution.**
- Row 3: $3x_3 = 6 \implies x_3 = 2$
- Row 2: $-\frac{5}{2}x_2 + \frac{7}{2}(2) = \frac{19}{2} \implies -\frac{5}{2}x_2 = \frac{19}{2} - 7 = \frac{5}{2} \implies x_2 = -1$
- Row 1: $2x_1 + (-1) - (2) = -1 \implies 2x_1 = 2 \implies x_1 = 1$

$$
\boxed{x_1 = 1, \qquad x_2 = -1, \qquad x_3 = 2}
$$

**Substitution check into original equations:**
1. $2(1) + (-1) - (2) = 2 - 1 - 2 = -1 \quad \checkmark$
2. $1 - 2(-1) + 3(2) = 1 + 2 + 6 = 9 \quad \checkmark$
3. $3(1) - (-1) + 5(2) = 3 + 1 + 10 = 14 \quad \checkmark$

---

## NM-3.3: LU Decomposition and Matrix Inversion

### 📝 Definitions for NM-3.3

> **LU Factorisation:** "Let $A$ be a nonsingular square matrix. Then $A$ can be factorized into the form $LU$ ... It is a standard result of linear algebra that such a factorization, when it exists, is *unique*." — Jain, §7.3 (p. 257-258)

> **Doolittle Form:** LU factorisation where $L$ is a *unit lower triangular* matrix (diagonal entries are $1$) and $U$ is upper triangular.

> **Crout Form:** LU factorisation where $U$ is a *unit upper triangular* matrix (diagonal entries are $1$) and $L$ is lower triangular.

---

### Core Theory: LU Decomposition

Solving $Ax = b$ using LU decomposition splits the problem into two triangular solves:

$$
Ax = b \implies LUx = b
$$

1. **Solve lower triangular system for $y$ by forward substitution:**

$$
Ly = b
$$

2. **Solve upper triangular system for $x$ by back substitution:**

$$
Ux = y
$$

#### Why LU Factorisation is Efficient
Computing the factorisation $A = LU$ requires roughly $\frac{2}{3}n^3$ operations. Once $L$ and $U$ are known, solving for any new right-hand side $b$ requires only forward and back substitution, costing $2n^2$ operations. If an engineering problem requires solving $m$ systems with the same coefficient matrix $A$ and varying right-hand sides $b_1, b_2, \dots, b_m$, LU factorisation solves all $m$ systems in $\frac{2}{3}n^3 + 2mn^2$ operations, compared to $\frac{2}{3}mn^3$ operations for repeated Gauss elimination.

---

### 🏆 Golden Questions for NM-3.3

#### 🎯 How can a square matrix be factorized into the form LU to solve linear system of equations?
> **Appeared:** 2017 Q.4(b) — (05 marks)

**Full Answer:**

**The idea.** A square matrix $A$ can be written as the product of a unit lower triangular matrix $L$ (ones on the diagonal) and an upper triangular matrix $U$:

$$
A = LU
$$

Solving $Ax = b$ then becomes two triangular substitutions, which are cheap and stable:

$$
LUx = b \implies Ly = b \implies Ux = y
$$

**The construction.** Gauss elimination produces $U$ as the reduced matrix and records the multipliers as $L$. For a $3\times3$ system:

**Step 1.** Eliminate below the first column using row 1. The multipliers are:

$$
l_{21} = \frac{a_{21}}{a_{11}}, \qquad l_{31} = \frac{a_{31}}{a_{11}}
$$

Form $R_2 \leftarrow R_2 - l_{21}R_1$ and $R_3 \leftarrow R_3 - l_{31}R_1$. These operations correspond to multiplying $A$ on the left by:

$$
L_1 = \begin{bmatrix} 1 & 0 & 0 \\ -l_{21} & 1 & 0 \\ -l_{31} & 0 & 1 \end{bmatrix}
$$

**Step 2.** Eliminate below the second column of the result. With:

$$
l_{32} = \frac{a_{32}^{(1)}}{a_{22}^{(1)}} = \frac{a_{32} - l_{31}a_{12}}{a_{22} - l_{21}a_{12}}
$$

form $R_3 \leftarrow R_3 - l_{32}R_2^{(1)}$, corresponding to:

$$
L_2 = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & -l_{32} & 1 \end{bmatrix}
$$

**The result.** $L_2L_1A = U$, so:

$$
A = LU, \qquad L = L_1^{-1}L_2^{-1} = \begin{bmatrix} 1 & 0 & 0 \\ l_{21} & 1 & 0 \\ l_{31} & l_{32} & 1 \end{bmatrix}
$$

The multipliers become the sub-diagonal entries of $L$ directly. This is the **Doolittle form**. A variant that puts $U$'s diagonal into $L$ is the **Crout form**.

**Solving.** Forward-substitute $Ly = b$:

$$
y_1 = b_1, \qquad y_2 = b_2 - l_{21}y_1, \qquad y_3 = b_3 - l_{31}y_1 - l_{32}y_2
$$

then back-substitute $Ux = y$:

$$
x_3 = \frac{y_3}{u_{33}}, \qquad x_2 = \frac{y_2 - u_{23}x_3}{u_{22}}, \qquad x_1 = \frac{y_1 - u_{12}x_2 - u_{13}x_3}{u_{11}}
$$

**Why it is useful.** The factorisation is computed once at $\frac{n^3}{3}$ operations, and any number of right-hand sides can then be solved at a cost of only $n^2$ each.

---

## NM-3.4: Jacobi Iteration Method

### 📝 Definitions for NM-3.4

> **Jacobi Method (Simultaneous Displacements):** "This method is due to Jacobi and is called the *method of simultaneous displacements*." — Jain, §7.6 (p. 280)

> **Iteration Formula:** In the Jacobi method, the $(k+1)$-th approximation vector is computed strictly from the $k$-th approximation vector:
> $$
> X^{(k+1)} = B X^{(k)} + C
> $$
> where $B = -D^{-1}(L + U)$ is the Jacobi iteration matrix.

---

### Core Theory: Jacobi vs. Gauss-Seidel

Jacobi iteration updates each unknown using only the values from the previous iteration sweep:

$$
x_i^{(k+1)} = \frac{1}{a_{ii}} \left( b_i - \sum_{j \ne i} a_{ij} x_j^{(k)} \right)
$$

Because all components at step $k+1$ depend solely on step $k$, Jacobi can be computed in parallel across processors. However, it takes roughly twice as many iterations to converge as Gauss-Seidel.

---

### 🏆 Golden Questions for NM-3.4

#### 🎯 Solve the following system using Jacobi method.
> **Appeared:** 2017 Q.7(a), 2022 Q.4(a) — (05 marks / 05 marks)

$$
\begin{aligned}
6x + y + z &= 20 \\
x + 4y - z &= 6 \\
x - y + 5z &= 7
\end{aligned}
$$

**Full Answer:**

**Jacobi iteration form.** Each equation is solved for its own unknown, using only the values from the previous sweep:

$$
x^{(k+1)} = \frac{20 - y^{(k)} - z^{(k)}}{6}
$$

$$
y^{(k+1)} = \frac{6 - x^{(k)} + z^{(k)}}{4}
$$

$$
z^{(k+1)} = \frac{7 - x^{(k)} + y^{(k)}}{5}
$$

**Convergence check.** The diagonal entries are $6$, $4$, $5$ and the off-diagonal sums are $2$, $2$, $2$:
- Row 1: $|6| > |1| + |1| = 2$
- Row 2: $|4| > |1| + |-1| = 2$
- Row 3: $|5| > |1| + |-1| = 2$

Every row is strictly diagonally dominant, guaranteeing convergence.

**Iterations starting from $x^{(0)} = y^{(0)} = z^{(0)} = 0$:**

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

Exact solution by direct substitution:

$$
x = 3, \qquad y = 1, \qquad z = 1
$$

$$
\boxed{x = 3, \qquad y = 1, \qquad z = 1}
$$

---

## NM-3.6: Relaxation Techniques (SOR)

### 📝 Definitions for NM-3.6

> **Relaxation Factor ($\omega$ or $\lambda$):** A weighting parameter applied to the Gauss-Seidel update to modify the step size taken toward the solution:
> $$
> x_i^{(k+1)} = (1 - \lambda)x_i^{(k)} + \lambda \hat x_i^{(k+1)}
> $$
> where $\hat x_i^{(k+1)}$ is the unrelaxed Gauss-Seidel iterate.

> **Under-Relaxation ($0 < \lambda < 1$):** Damps oscillations by taking a shorter step, stabilising divergent or oscillating iterative processes.

> **Over-Relaxation ($1 < \lambda < 2$):** Accelerates convergence by taking a larger step in the correction direction. Known as Successive Over-Relaxation (SOR).

---

### Core Theory: Relaxation Mechanics

At $\lambda = 1$, the formula reduces to standard Gauss-Seidel.
- When the spectral radius of the iteration matrix is close to 1, standard Gauss-Seidel converges slowly. Choosing an optimal over-relaxation factor $\lambda_{\text{opt}} \in (1, 2)$ reduces the spectral radius and cuts iteration counts by a large factor.
- For systems that oscillate or fail strict diagonal dominance, under-relaxation ($\lambda < 1$) pulls the new iterate back toward the previous iterate, preserving stability.

---

### 🏆 Golden Questions for NM-3.6

#### 🎯 What is meant by over-relaxation and under-relaxation?
> **Appeared:** 2018 Q.4(a) — (03 marks)

**Full Answer:**

Both terms describe a modification of the Gauss-Seidel iteration in which a **relaxation parameter** $\omega$ is introduced.

**Relaxed Gauss-Seidel.** The ordinary Gauss-Seidel update is replaced by:

$$
x_i^{(k+1)} = (1 - \omega)x_i^{(k)} + \omega\hat x_i^{(k)}
$$

where $\hat x_i^{(k)}$ is the value obtained from the ordinary Gauss-Seidel recursion applied to iteration $k$.

**Under-relaxation ($0 < \omega < 1$):** Each new iterate is a weighted blend of the old value and the new one, so the sequence moves toward the solution by a fraction of the full step. This damps oscillation and is used when the ordinary iteration diverges or oscillates. It reduces the effective step and restores convergence at the cost of more iterations.

**Over-relaxation ($1 < \omega < 2$):** Each new iterate overshoots the ordinary Gauss-Seidel value, so the sequence moves toward the solution faster than plain iteration. The method is called Successive Over-Relaxation (SOR), and choosing an optimal $\omega$ reduces the iteration count substantially.

**The two regimes separated by $\omega = 1$:** At $\omega = 1$ the formula reduces to ordinary Gauss-Seidel. Above $1$ the iteration is accelerated; below $1$ it is stabilised. The purpose in both cases is to control the rate at which error is carried between iterations.

---

#### 🎯 Use the Gauss Seidel method with relaxation $(\lambda = 0.95)$ to solve the following system. If necessary rearrange the equations to achieve convergence (use 3 iterations only).
> **Appeared:** 2017 Q.4(c) — (05 marks)

$$
\begin{aligned}
-3x_1 + x_2 + 12x_3 &= 50 \\
6x_1 - x_2 - x_3 &= 3 \\
6x_1 + 9x_2 + x_3 &= 40
\end{aligned}
$$

**Full Answer:**

**Check for diagonal dominance in printed order:**
- Row 1: $|{-3}| = 3 < |1| + |12| = 13$ (fails)
- Row 2: $|{-1}| = 1 < |6| + |1| = 7$ (fails)
- Row 3: $|9| = 9 > |6| + |1| = 7$ (dominant)

The original arrangement is not diagonally dominant.

**Rearrange equations:**
1. Equation 2 as **Row 1** (solve for $x_1$): $|6| > |-1| + |-1| = 2$.
2. Equation 3 as **Row 2** (solve for $x_2$): $|9| > |6| + |1| = 7$.
3. Equation 1 as **Row 3** (solve for $x_3$): $|12| > |-3| + |1| = 4$.

The rearranged system:

$$
\begin{aligned}
6x_1 - x_2 - x_3 &= 3 \\
6x_1 + 9x_2 + x_3 &= 40 \\
-3x_1 + x_2 + 12x_3 &= 50
\end{aligned}
$$

**Iterative formulas with relaxation $\lambda = 0.95$:**
First compute raw Gauss-Seidel predictors $\hat{x}_i^{(k+1)}$:

$$
\hat x_1^{(k+1)} = \frac{3 + x_2^{(k)} + x_3^{(k)}}{6}
$$

$$
\hat x_2^{(k+1)} = \frac{40 - 6x_1^{(k+1)} - x_3^{(k)}}{9}
$$

$$
\hat x_3^{(k+1)} = \frac{50 + 3x_1^{(k+1)} - x_2^{(k+1)}}{12}
$$

Apply relaxation:

$$
x_i^{(k+1)} = 0.05\,x_i^{(k)} + 0.95\,\hat x_i^{(k+1)}
$$

Starting from $x^{(0)} = (0, 0, 0)$:

- **Iteration 1:**
  - $\hat x_1^{(1)} = \frac{3 + 0 + 0}{6} = 0.500000 \implies x_1^{(1)} = 0.95(0.500000) = 0.475000$
  - $\hat x_2^{(1)} = \frac{40 - 6(0.475000) - 0}{9} = 4.127778 \implies x_2^{(1)} = 0.95(4.127778) = 3.921389$
  - $\hat x_3^{(1)} = \frac{50 + 3(0.475000) - 3.921389}{12} = 3.958634 \implies x_3^{(1)} = 0.95(3.958634) = 3.760703$

- **Iteration 2:**
  - $\hat x_1^{(2)} = \frac{3 + 3.921389 + 3.760703}{6} = 1.780349 \implies x_1^{(2)} = 0.05(0.475000) + 0.95(1.780349) = 1.715081$
  - $\hat x_2^{(2)} = \frac{40 - 6(1.715081) - 3.760703}{9} = 2.883201 \implies x_2^{(2)} = 0.05(3.921389) + 0.95(2.883201) = 2.935111$
  - $\hat x_3^{(2)} = \frac{50 + 3(1.715081) - 2.935111}{12} = 4.350844 \implies x_3^{(2)} = 0.05(3.760703) + 0.95(4.350844) = 4.321337$

- **Iteration 3:**
  - $\hat x_1^{(3)} = \frac{3 + 2.935111 + 4.321337}{6} = 1.709408 \implies x_1^{(3)} = 0.05(1.715081) + 0.95(1.709408) = 1.709692$
  - $\hat x_2^{(3)} = \frac{40 - 6(1.709692) - 4.321337}{9} = 2.824501 \implies x_2^{(3)} = 0.05(2.935111) + 0.95(2.824501) = 2.830032$
  - $\hat x_3^{(3)} = \frac{50 + 3(1.709692) - 2.830032}{12} = 4.358254 \implies x_3^{(3)} = 0.05(4.321337) + 0.95(4.358254) = 4.356408$

| Iteration | $x_1$ | $x_2$ | $x_3$ |
| :--: | :-- | :-- | :-- |
| 0 | $0.000000$ | $0.000000$ | $0.000000$ |
| 1 | $0.475000$ | $3.921389$ | $3.760703$ |
| 2 | $1.715081$ | $2.935111$ | $4.321337$ |
| 3 | $1.709692$ | $2.830032$ | $4.356408$ |

$$
\boxed{x_1 \approx 1.7097, \qquad x_2 \approx 2.8300, \qquad x_3 \approx 4.3564}
$$

---

## NM-3.7: Ill-Conditioned Systems

### 📝 Definitions for NM-3.7

> **Ill-Conditioned System:** "A system of linear equations is ill-conditioned when a small change in the input produces a disproportionately large change in the solution." — Topicwise NM-3.7

> **Condition Number $\kappa(A)$:** The magnification factor between relative data error and relative solution error:
> $$
> \frac{\|\delta x\| / \|x\|}{\|\delta b\| / \|b\|} \le \kappa(A) = \|A\|\,\|A^{-1}\|
> $$

---

### Core Theory: Condition Number and Engineering Significance

| $\kappa(A)$ | Numerical Behaviour |
| :-- | :-- |
| $\kappa = 1$ | Perfectly conditioned; error passes through without amplification |
| $\kappa \approx 10$ | Well conditioned; mild amplification |
| $\kappa \approx 10^6$ | Ill-conditioned; loss of approximately six decimal digits of accuracy |
| $\kappa > 10^{16}$ | Numerically singular; all significant precision lost |

#### Causes of Ill-Conditioning
1. **Nearly singular matrix:** Determinant is close to zero; two or more rows/columns are nearly linearly dependent.
2. **Wildly disparate scales:** Row or column coefficients differ by orders of magnitude.
3. **Redundant variables:** Two unknowns represent nearly identical physical quantities.

#### Remedies
- Normalize/scale rows and columns so elements have comparable magnitude.
- Reformulate the underlying physical equations.
- Use higher-precision floating-point arithmetic.
- **Pivoting does not fix conditioning:** Pivoting improves algorithm stability, but the condition number is an intrinsic property of matrix $A$.

---

### 🏆 Golden Questions for NM-3.7

#### 🎯 Define ill-conditioned system.
> **Appeared:** 2022 Q.4(c) — (02 marks)

**Full Answer:**

**Definition.** A system of linear equations is **ill-conditioned** when a small change in the input produces a disproportionately large change in the solution.

**Measure.** The **condition number** $\kappa$ of the coefficient matrix is the ratio of the largest to the smallest relative error:

$$
\frac{\dfrac{\|\delta x\|}{\|x\|}}{\dfrac{\|\delta b\|}{\|b\|}} \le \kappa(A)
$$

Thus a relative error of $\epsilon$ in the data may become up to $\kappa\epsilon$ in the answer.

| $\kappa$ | Behaviour |
| :-- | :-- |
| $\kappa = 1$ | Perfectly conditioned, error passes through unchanged |
| $\kappa \approx 10$ | Mild amplification |
| $\kappa \approx 10^6$ | Loss of about six significant digits |
| $\kappa > 10^{16}$ | All precision lost; the matrix is numerically singular |

**Causes:**
1. **A matrix that is nearly singular:** An eigenvalue is close to zero, or rows are nearly linearly dependent. Two nearly parallel equations constrain the solution very weakly.
2. **Rows or columns of wildly different magnitudes:** The smaller entries are effectively lost to round-off.
3. **A bad choice of variables:** Variables that measure nearly the same physical quantity make corresponding columns almost equal.

**Why it matters in engineering:** Data has uncertainty, typically $10^{-4}$ from instruments. If $\kappa = 10^8$, the answer carries a relative uncertainty of $10^4$, which is useless even if computed to double precision.

**What to do about it:** Row or column scaling, choosing better-conditioned variables, reformulating the physical problem, or using higher precision arithmetic. Pivoting improves stability but does not change $\kappa$, because conditioning is a property of the problem.

$$
\boxed{\text{ill-conditioned means small input errors produce large output errors; measured by }\kappa}
$$

---

## ⚡ Exam Tips & Common Mistakes

1. **Check your multipliers in Gauss elimination.** Multipliers are $m_{ik} = a_{ik}/a_{kk}$. Subtracting $m_{ik} \times \text{Row}_k$ clears the entry below. Watch your signs when subtracting negative values.
2. **In LU factorisation, $L$ stores multipliers directly.** For Doolittle's method, the sub-diagonal elements of $L$ are exactly the multipliers from forward elimination. You do not need matrix inversion.
3. **Jacobi sweeps use only old values.** In Jacobi iteration, every single update in sweep $k+1$ uses values from sweep $k$. Never use an updated value from the same sweep.
4. **Relaxation formula indexing.** $\hat{x}_i^{(k+1)}$ is the raw Gauss-Seidel value computed from the freshest available values. The relaxed iterate is $(1 - \lambda)x_i^{(k)} + \lambda \hat{x}_i^{(k+1)}$.
5. **Stability vs. Conditioning.** Memorize this distinction: Pivoting addresses numerical stability (an algorithm property). The condition number measures conditioning (a problem property). Pivoting cannot fix an ill-conditioned system.

## 🔗 Related Topics

- [NM-3.2: Pivoting](NM-3.2_Pivoting.md) — partial and complete pivoting mechanisms in Gauss elimination
- [NM-3.5: Gauss-Seidel Iteration](NM-3.5_Gauss_Seidel_Iteration.md) — the successive displacement counterpart to Jacobi iteration
- [NM-3.8: Circuit Applications](NM-3.8_Circuit_Applications.md) — physical network setups solved by elimination and iteration

---

[← Previous: NM-3.8 Circuit Applications](NM-3.8_Circuit_Applications.md) | [🏠 Index](00_Index.md) | [Next: NM-4.1 Curve Fitting Concepts →](NM-4.1_Curve_Fitting_Concepts.md)
