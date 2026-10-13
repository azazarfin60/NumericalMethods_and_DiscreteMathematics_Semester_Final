---
title: "NM-3.1 · Direct Methods & Gauss Elimination"
tags:
  - numerical-methods
  - discrete-mathematics
  - topicwise
---



[🏠 Subtopic Index](00_Index.md) | [← Prev: NM-2.7 Roots of Polynomials](NM-2.7_Roots_of_Polynomials.md) | [Next: NM-3.2 Pivoting →](NM-3.2_Pivoting.md)

---

# NM-3.1 · Direct Methods & Gauss Elimination

Every block below is copied from `../answers_explanation/`. The reasoning
is written once, in the year-wise file, and is not restated here.


### [2019 Q.3(a)]

**Question.** Discuss Gauss Elimination method to solve linear simultaneous algebraic equations.

*[Marks: 04]*

**Solution.**

**Gauss elimination** solves $Ax = b$ by transforming the coefficient matrix into
upper triangular form using elementary row operations, then recovering the unknowns
by back substitution. The solution set is unchanged, since every operation is
reversible.

**The system.** For $n$ equations in $n$ unknowns,

$$a_{11}x_1 + a_{12}x_2 + \cdots + a_{1n}x_n = b_1$$
$$\vdots$$
$$a_{n1}x_1 + a_{n2}x_2 + \cdots + a_{nn}x_n = b_n$$

**Steps**

1. **Forward elimination.** Using $R_1$, eliminate $x_1$ from $R_2$ through $R_n$
   by forming $R_i \leftarrow R_i - \dfrac{a_{i1}}{a_{11}}R_1$. Then use the modified
   $R_2$ to eliminate $x_2$ from $R_3$ through $R_n$, and continue. After pass $k$
   the first $k$ equations have $k$ non-zero coefficients and the remaining have
   zeros in the first $k$ columns.
2. **Triangular system.** After $n-1$ passes the matrix is upper triangular:

$$u_{11}x_1 + u_{12}x_2 + \cdots + u_{1n}x_n = b_1'$$
$$\qquad\qquad u_{22}x_2 + \cdots + u_{2n}x_n = b_2'$$
$$\qquad\qquad\qquad\qquad \ddots \qquad \vdots$$
$$\qquad\qquad\qquad\qquad u_{nn}x_n = b_n'$$

3. **Back substitution.** From the last equation, $x_n = b_n'/u_{nn}$. Substitute
   into the $(n-1)$-th, giving $x_{n-1}$, and continue upward to $x_1$.
4. **Division by zero.** If a pivot $u_{kk}$ is zero, the row is exchanged with one
   below having a non-zero entry in that column.
5. **Verification.** Substitute the obtained vector back into the original system.

**Operation count.** Forward elimination needs roughly $\dfrac{n^3}{3}$
multiplications and divisions; back substitution needs $\dfrac{n^2}{2}$. Total cost
grows as $n^3$, so the method is practical for moderate $n$ and for a single
right-hand side.

**Use in ECE.** Nodal analysis of a network with more than two nodes produces a
set of simultaneous equations larger than is comfortable by hand. Gauss elimination
converts it to a triangular set whose values are read off successively, which is
the standard automated form of that solution.

> [!note] Why triangular form is worth the $O(n^3)$
> Once the matrix is upper triangular, each unknown needs only the ones already
> found. That is $O(n^2)$ work total, against $O(n^3)$ to build the form.
>
> The triangular shape is also what makes the **Thomas algorithm** work on
> tridiagonal systems in $O(n)$ rather than $O(n^3)$, and tridiagonal systems are
> what discretised second-order ODEs and the five-point Laplace stencil produce.
> Most of the large solves in practice are tridiagonal, and Gauss elimination is
> the reason that is not a problem.

> [!warning] Step 4 is not an afterthought
> The step divides by the pivot. A **zero** pivot stops the method; a **tiny** pivot
> is worse, because the multiplier $\frac{a_{i1}}{a_{11}}$ becomes huge and the
> subtraction destroys the significant digits of what remains.
>
> The method still runs and returns a wrong answer, with no warning. Row
> interchanging costs one comparison per step and is not optional in a general
> solver. See part (b).

---

### [2020 Q.4(a)]

**Question.** What are the direct methods to solve linear system of equations? Describe any one of them.

*[Marks: 06]*

**Solution.**

**The system.** To solve

$$
A\mathbf{x} = \mathbf{b}, \qquad A = [a_{ij}] \in \mathbb{R}^{n\times n}
$$

Direct methods produce the exact solution in a **fixed** number of steps, decided
in advance by $n$. They do not iterate toward the answer, which is what
distinguishes them from iterative methods.

**The two families.**

1. **Elimination methods.** Reduce the augmented system to upper triangular form
   by elementary row operations, then back-substitute. Examples: **Gaussian
   elimination**, **Gauss-Jordan elimination**, and **LU factorisation**.
2. **Matrix factorisation methods.** Write $A$ as a product of simpler matrices
   and solve the pieces in sequence. Examples: **Crout**, **Cholesky**
   (symmetric positive definite only), **QR**.

Everything else is a variant of one of these two ideas.

**Described: Gaussian elimination with partial pivoting.**

Write the augmented matrix $[\,A \mid \mathbf{b}\,]$. For column $k$, find the row
$p \ge k$ with the largest $\lvert a_{pk}\rvert$, and swap rows $k$ and $p$. Then
eliminate the entries below the pivot:

$$
\text{for } i = k+1, \dots, n: \qquad m_{ik} = \frac{a_{ik}}{a_{kk}}, \qquad \text{row}_i \leftarrow \text{row}_i - m_{ik}\,\text{row}_k
$$

This makes every entry below the diagonal of column $k$ zero. Repeat for
$k = 1, 2, \dots, n-1$. The result is upper triangular:

$$
\begin{bmatrix}
a_{11} & a_{12} & \cdots & a_{1n} \\
0 & a_{22} & \cdots & a_{2n} \\
\vdots & & \ddots & \vdots \\
0 & 0 & \cdots & a_{nn}
\end{bmatrix} \mathbf{x} = \mathbf{c}
$$

Now back-substitute from the bottom:

$$x_n = \frac{c_n}{a_{nn}}, \qquad x_i = \frac{1}{a_{ii}}\left(c_i - \sum_{j=i+1}^{n} a_{ij} x_j\right)$$

**Worked micro-example.** Solve $2x + y = 5$ and $x - y = 1$.

$$
\begin{bmatrix} 2 & 1 & | & 5 \\ 1 & -1 & | & 1 \end{bmatrix}
$$

Pivot in column 1 is $2$; the row 2 entry is $1$, so no swap is needed.
$m_{21} = \frac{1}{2}$, and row 2 becomes
$\left[0, -1 - \frac{1}{2}\mid 1 - \frac{5}{2}\right] = \left[0, -\frac{3}{2} \mid -\frac{3}{2}\right]$.

Back-substitute: $y = \frac{-3/2}{-3/2} = 1$, then $2x = 5 - 1 = 4$ so $x = 2$.

$$\boxed{x = 2, \qquad y = 1}$$

Check: $2(2) + 1 = 5$ and $2 - 1 = 1$. Both hold.

> [!note] This box is a two-equation micro-example, not the answer to a question
> Nothing here is asked for. Q.4(a) is a theory question, and the two-equation
> system exists only to demonstrate the method on something that fits on a page.
> Read it as a demonstration of the **procedure**, not as a computed result, and
> do not spend time defending $x = 2$.

$$\boxed{\text{Eliminate to upper triangular form, pivot to stay safe, then back-substitute}}$$

**Why pivoting is not optional.** The step divides by the pivot. A **zero** pivot
stops the method dead. A **tiny** pivot is worse, because the multiplier
$m_{ik} = \frac{a_{ik}}{a_{kk}}$ becomes huge, and subtracting large nearly equal
numbers destroys most of the significant digits. The method still runs and returns
a wrong answer, with no warning. Partial pivoting costs one comparison per
candidate and no extra arithmetic, and it is the standard safeguard.

| Method | Work | Storage | Notes |
| :-- | :-- | :-- | :-- |
| Gaussian elimination | $\frac{2}{3}n^3$ | $n^2$ | Triangular solve is $O(n^2)$ |
| Gauss-Jordan | $n^3$ | $n^2$ | Gives the inverse directly |
| LU factorisation | $\frac{2}{3}n^3$ | $n^2$ | Reuse the factors for many right sides |
| Cholesky | $\frac{1}{3}n^3$ | $\frac{1}{2}n^2$ | Half the work, but needs $A$ symmetric positive definite |

**Direct against iterative.** Direct methods cost $O(n^3)$ and are unbeatable for
small and dense systems. But $n^3$ becomes hopeless: at $n = 10^4$ it is $10^{12}$
operations, and the matrix alone needs $8 \times 10^7$ entries. Large sparse
systems, which is what discretised PDEs produce, are handled by iterative methods
that touch only the non-zero entries. The Gauss-Seidel method in Q.4(b) is the
other side of that trade.

> [!warning] The one thing to say about pivoting, even though nothing is computed
> Two failures, and the second is much worse. A **zero** pivot is loud: the method
> stops. A **tiny** pivot is silent: the method runs to completion and returns a
> wrong answer.
>
> The reason is that the multiplier $m_{ik} = a_{ik}/a_{kk}$ blows up, and
> subtracting a huge number from another huge number cancels away the significant
> digits. Partial pivoting takes one comparison per candidate row and no extra
> arithmetic, so there is no reason ever to leave it off.

---

### [2022 Q.4(b)]

**Question.** Solve the system using Gauss elimination: $2x_1 + x_2 - x_3 = -1$, $x_1 - 2x_2 + 3x_3 = 9$, $3x_1 - x_2 + 5x_3 = 14$. Check your answer by substituting into the original equations.

*[Marks: 04, CO: 2]*

**Solution.**

**Step 1. The augmented matrix.**

$$
\left[\begin{array}{ccc|c}
2 & 1 & -1 & -1 \\
1 & -2 & 3 & 9 \\
3 & -1 & 5 & 14
\end{array}\right]
$$

**Step 2. Eliminate $x_1$ from rows 2 and 3.** The multipliers are $\frac{1}{2}$
and $\frac{3}{2}$, taken as row entry over pivot.

Row 2: $R_2 \leftarrow R_2 - \frac{1}{2}R_1$

$$
[1 - \tfrac{1}{2}(2),\; -2 - \tfrac{1}{2},\; 3 - \tfrac{1}{2}(-1),\; 9 - \tfrac{1}{2}(-1)]
= [0,\; -\tfrac{5}{2},\; \tfrac{7}{2},\; \tfrac{19}{2}]
$$

Row 3: $R_3 \leftarrow R_3 - \frac{3}{2}R_1$

$$
[3 - 3,\; -1 - \tfrac{3}{2},\; 5 - \tfrac{3}{2}(-1),\; 14 - \tfrac{3}{2}(-1)]
= [0,\; -\tfrac{5}{2},\; \tfrac{13}{2},\; \tfrac{31}{2}]
$$

$$
\left[\begin{array}{ccc|c}
2 & 1 & -1 & -1 \\
0 & -\frac{5}{2} & \frac{7}{2} & \frac{19}{2} \\
0 & -\frac{5}{2} & \frac{13}{2} & \frac{31}{2}
\end{array}\right]
$$

Note the signs in the last two columns: $\frac{7}{2} = 3 - \frac{1}{2}(-1)$ is
positive because subtracting a negative $\frac{1}{2}(-1)$ adds $\frac{1}{2}$.

**Step 3. Eliminate $x_2$ from row 3.** The multiplier is
$\frac{-5/2}{-5/2} = 1$, so $R_3 \leftarrow R_3 - R_2$:

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

**Step 4. Back substitution.**

Row 3: $3x_3 = 6 \Rightarrow x_3 = 2$

Row 2: $-\frac{5}{2}x_2 + \frac{7}{2}(2) = \frac{19}{2}$, so

$$
-\frac{5}{2}x_2 = \frac{19}{2} - 7 = \frac{19}{2} - \frac{14}{2} = \frac{5}{2}
\quad \Rightarrow \quad x_2 = -\frac{5/2}{5/2} = -1
$$

Row 1: $2x_1 + (-1) - (2) = -1 \Rightarrow 2x_1 = 2 \Rightarrow x_1 = 1$

$$\boxed{x_1 = 1, \qquad x_2 = -1, \qquad x_3 = 2}$$

**The required check, by substitution into the original equations.**

$$
2x_1 + x_2 - x_3 = 2(1) + (-1) - 2 = 2 - 1 - 2 = -1 \quad \checkmark
$$

$$
x_1 - 2x_2 + 3x_3 = 1 - 2(-1) + 3(2) = 1 + 2 + 6 = 9 \quad \checkmark
$$

$$
3x_1 - x_2 + 5x_3 = 3(1) - (-1) + 5(2) = 3 + 1 + 10 = 14 \quad \checkmark
$$

All three residuals are exactly zero.

> [!warning] The sign of $x_2$ is decided in one line, and it is easy to lose
> Row 2 gives $-\frac{5}{2}x_2 = +\frac{5}{2}$, so $x_2 = -1$. The minus sign is
> on both sides and cancels, but the minus on the left comes from the negative
> diagonal entry, not from the arithmetic of the step.
>
> A useful symmetry check: the same elimination written the other way round,
> $R_2 \leftarrow R_2 - R_3$, gives the row $[0, 0, -3, -6]$ instead of
> $[0, 0, 3, 6]$. Both give $x_3 = 2$, because the signs cancel. Writing one
> convention into the matrix and the other into the back substitution does not,
> so keep to whichever direction you started with.

> [!info] Independent confirmation
> The determinant of the coefficient matrix is
> $$\det = 2(-10 + 3) - 1(5 - 9) + (-1)(-1 + 6) = -14 + 4 - 5 = -15 \ne 0$$
> so the system has a unique solution, and Cramer's rule returns $(1, -1, 2)$.
> Note also that the three pivots $2$, $-\frac{5}{2}$ and $3$ are all comfortably
> away from zero, so no pivoting was needed here.

---

[🏠 Subtopic Index](00_Index.md) | [← Prev: NM-2.7 Roots of Polynomials](NM-2.7_Roots_of_Polynomials.md) | [Next: NM-3.2 Pivoting →](NM-3.2_Pivoting.md)
