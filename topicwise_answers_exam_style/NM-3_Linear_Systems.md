---
title: "NM-3 · Linear Algebraic Equations"
tags:
  - numerical-methods
  - discrete-mathematics
  - topicwise-clusters
---

[🏠 Master Index](00_Index.md) | [← Prev Topic: NM-2 · Roots of Equations](NM-2_Roots_of_Equations.md) | [Next Topic: NM-4 · Curve Fitting →](NM-4_Curve_Fitting.md)

---

# NM-3 · Linear Algebraic Equations

> **Topic ID:** NM-3  
> **Section:** Section A -- Numerical Methods  
> **Exam Weight:** 🔴 High Priority (Tier 1) | 8/8 Years Examined (100% Frequency) | Typical Weight: 10–14 marks (Question 2/3)  
> **Subtopics Included:** 8 subtopics (NM-3.1 through NM-3.8)  
> **Origin Layer:** Authored in `../answers_exam_style/`. All numerical results and boxed equations match character-for-character.

---

## 📑 Subtopics Covered in this Cluster

| Subtopic ID | Subtopic Title | Priority | Exam Frequency | Section Navigation |
|:---|:---|:---:|:---:|:---|
| **NM-3.1** | Direct Methods & Gauss Elimination | 🟠 | 2019, 2020, 2022 | [Jump to NM-3.1](#nm-31) |
| **NM-3.2** | Pivoting | 🔴 | 2017, 2019, 2021, 2022 | [Jump to NM-3.2](#nm-32) |
| **NM-3.3** | LU Decomposition & Matrix Inversion | 🟡 ⚠️ | 2017 | [Jump to NM-3.3](#nm-33) |
| **NM-3.4** | Jacobi Iteration | 🟠 | 2017, 2022 | [Jump to NM-3.4](#nm-34) |
| **NM-3.5** | Gauss-Seidel Iteration | 🔴 | 2017, 2018, 2019, 2020, 2021, 2024, CT-02B | [Jump to NM-3.5](#nm-35) |
| **NM-3.6** | Relaxation | 🟡 | 2017, 2018 | [Jump to NM-3.6](#nm-36) |
| **NM-3.7** | Ill-Conditioned Systems | 🟡 | 2022 | [Jump to NM-3.7](#nm-37) |
| **NM-3.8** | Circuit Applications | 🔴 | 2018, 2019, 2020, 2021, 2024 | [Jump to NM-3.8](#nm-38) |

---

<a id="nm-31"></a><a id="nm-3.1"></a>
## NM-3.1 · Direct Methods & Gauss Elimination

### [2019 Q.3(a)]

**Question.** Discuss Gauss Elimination method to solve linear simultaneous algebraic equations.

**Solution.**

**Gauss elimination** solves $Ax = b$ by transforming the coefficient matrix into
upper triangular form using elementary row operations, then recovering the
unknowns by back substitution. The solution set is unchanged, since every
operation is reversible.

**The system.** For $n$ equations in $n$ unknowns,

$$a_{11}x_1 + a_{12}x_2 + \cdots + a_{1n}x_n = b_1$$

$$\vdots$$

$$a_{n1}x_1 + a_{n2}x_2 + \cdots + a_{nn}x_n = b_n$$

**Steps**

1. **Forward elimination.** Using $R_1$, eliminate $x_1$ from $R_2$ through $R_n$
   by forming $R_i \leftarrow R_i - \dfrac{a_{i1}}{a_{11}}R_1$. Then use the
   modified $R_2$ to eliminate $x_2$ from $R_3$ through $R_n$, and continue.
   After pass $k$ the first $k$ equations have $k$ non-zero coefficients and the
   remaining have zeros in the first $k$ columns.
2. **Triangular system.** After $n-1$ passes the matrix is upper triangular:

$$u_{11}x_1 + u_{12}x_2 + \cdots + u_{1n}x_n = b_1'$$

$$\qquad\qquad u_{22}x_2 + \cdots + u_{2n}x_n = b_2'$$

$$\qquad\qquad\qquad\qquad \ddots \qquad \vdots$$

$$\qquad\qquad\qquad\qquad u_{nn}x_n = b_n'$$

3. **Back substitution.** From the last equation,
   $x_n = b_n'/u_{nn}$. Substitute into the $(n-1)$-th, giving $x_{n-1}$, and
   continue upward to $x_1$.
4. **Division by zero.** If a pivot $u_{kk}$ is zero, the row is exchanged with
   one below having a non-zero entry in that column.
5. **Verification.** Substitute the obtained vector back into the original
   system.

**Operation count.** Forward elimination needs roughly $\dfrac{n^3}{3}$
multiplications and divisions; back substitution needs $\dfrac{n^2}{2}$. Total
cost grows as $n^3$, so the method is practical for moderate $n$ and for a single
right-hand side.

**Use in ECE.** Nodal analysis of a network with more than two nodes produces a
set of simultaneous equations larger than is comfortable by hand. Gauss
elimination converts it to a triangular set whose values are read off
successively, which is the standard automated form of that solution.

---

### [2020 Q.4(a)]

**Question.** What are the direct methods to solve linear system of equations? Describe any one of them.

**Solution.**

**The system.** To solve

$$A\mathbf{x} = \mathbf{b}, \qquad A = [a_{ij}] \in \mathbb{R}^{n\times n}$$

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

Write the augmented matrix $[\,A \mid \mathbf{b}\,]$. For column $k$, find the
row $p \ge k$ with the largest $\lvert a_{pk}\rvert$, and swap rows $k$ and $p$.
Then eliminate the entries below the pivot:

$$\text{for } i = k+1, \dots, n: \qquad m_{ik} = \frac{a_{ik}}{a_{kk}}, \qquad \text{row}_i \leftarrow \text{row}_i - m_{ik}\,\text{row}_k$$

This makes every entry below the diagonal of column $k$ zero. Repeat for
$k = 1, 2, \dots, n-1$. The result is upper triangular:

$$
\begin{bmatrix} a_{11} & a_{12} & \cdots & a_{1n} \\
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

$$
\boxed{x = 2, \qquad y = 1}
$$

Check: $2(2) + 1 = 5$ and $2 - 1 = 1$. Both hold.

**Why pivoting is not optional.** The step divides by the pivot. A **zero** pivot
stops the method dead. A **tiny** pivot is worse, because the multiplier
$m_{ik} = \frac{a_{ik}}{a_{kk}}$ becomes huge, and subtracting large nearly equal
numbers destroys most of the significant digits. The method still runs and
returns a wrong answer, with no warning. Partial pivoting costs one comparison
per candidate and no extra arithmetic, and it is the standard safeguard.

| Method | Work | Storage | Notes |
| :-- | :-- | :-- | :-- |
| Gaussian elimination | $\frac{2}{3}n^3$ | $n^2$ | Triangular solve is $O(n^2)$ |
| Gauss-Jordan | $n^3$ | $n^2$ | Gives the inverse directly |
| LU factorisation | $\frac{2}{3}n^3$ | $n^2$ | Reuse the factors for many right sides |
| Cholesky | $\frac{1}{3}n^3$ | $\frac{1}{2}n^2$ | Half the work, but needs $A$ symmetric positive definite |

**Direct against iterative.** Direct methods cost $O(n^3)$ and are unbeatable for
small and dense systems. But $n^3$ becomes hopeless: at $n = 10^4$ it is
$10^{12}$ operations, and the matrix alone needs $8 \times 10^7$ entries. Large
sparse systems, which is what discretised PDEs produce, are handled by iterative
methods that touch only the non-zero entries. The iterative methods in
Q.4(b) and Q.7(b) of this paper are the other side of that trade.

$$
\boxed{\text{Eliminate to upper triangular form, pivot to stay safe, then back-substitute}}
$$

---

### [2022 Q.4(b)]

**Question.** Solve the system using Gauss elimination: $2x_1 + x_2 - x_3 = -1$, $x_1 - 2x_2 + 3x_3 = 9$, $3x_1 - x_2 + 5x_3 = 14$. Check your answer by substituting into the original equations.

**Solution.**

**Step 1. Write the augmented matrix.**

$$
\left[\begin{array}{ccc|c}
2 & 1 & -1 & -1 \\
1 & -2 & 3 & 9 \\
3 & -1 & 5 & 14
\end{array}\right]
$$

**Step 2. Eliminate $x_1$ from rows 2 and 3.**

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

**Step 3. Eliminate $x_2$ from row 3.**

The multiplier is $\frac{-5/2}{-5/2} = 1$, so $R_3 \leftarrow R_3 - R_2$:

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

> [!note] The signs in the last two rows
> Row 2 gives $\frac{5}{2}$ for $-\frac{5}{2}x_2$, so $x_2 = -1$, not $+1$. The
> elimination step yields the row $[0, 0, -3, -6]$ if written as
> $R_2 \leftarrow R_2 - R_3$, and $[0, 0, 3, 6]$ if written as
> $R_3 \leftarrow R_3 - R_2$. Both give $x_3 = 2$ because the signs cancel, but
> writing one convention into the matrix and the other into the back substitution
> does not.

$$
\boxed{x_1 = 1, \qquad x_2 = -1, \qquad x_3 = 2}
$$

**Required check, by substitution into the original equations.**

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

> [!info] Check by an independent route
> Computing the determinant of the coefficient matrix gives
> $\det = 2(-10 + 3) - 1(5 - 9) + (-1)(-1 + 6) = -14 + 4 - 5 = -15 \ne 0$, so the
> system has a unique solution, and Cramer's rule returns $(1, -1, 2)$.
>
> Note the pivots are $2$, $-\frac{5}{2}$ and $3$, all comfortably away from
> zero, so no pivoting was needed here.

---

<a id="nm-32"></a><a id="nm-3.2"></a>
## NM-3.2 · Pivoting

### [2017 Q.4(a)]

**Question.** What are pivots in solving system of linear equations using elimination methods? What are (i) partial & (ii) complete pivoting?

**Solution.**

**Pivots.** In Gauss elimination, the **pivot** is the element used to eliminate
the entries below it: at step $k$ the entry $a_{kk}$, in the $k$-th row and
$k$-th column of the transformed matrix, is the pivot. The multipliers are

$$m_{ik} = \frac{a_{ik}}{a_{kk}}$$

and the pivot enters the denominator of every multiplier at that step. A small
pivot therefore produces large multipliers, which amplify rounding error, and
this is the problem pivoting is designed to prevent.

**Partial pivoting.** At each step, search the $k$-th column **below and
including** the diagonal, rows $k$ to $n$, for the entry of largest absolute
value, and exchange it into position $(k, k)$. Only row exchanges are used, so
the order of the unknowns is unchanged. This is sufficient to keep
$|m_{ik}| \le 1$ for all $i > k$, which controls the magnitude of what is
subtracted.

**Complete pivoting.** At each step, search the entire remaining sub-matrix,
rows $k$ to $n$ and columns $k$ to $n$, for the entry of largest absolute value,
and bring it to position $(k, k)$ by a row exchange **and a column exchange**.
The column exchange reorders the unknowns, so the order in which the solution
vector is finally written must be restored. The extra search costs about $n^2$
comparisons per step, so complete pivoting is reserved for systems that are
nearly singular or where stability is critical.

**When the difference matters.** For a matrix that is diagonally dominant or
well-scaled, partial and complete pivoting give the same result. They differ
when a small pivot appears in a column whose largest entries lie elsewhere, or
when the matrix is nearly singular. Complete pivoting is always at least as
stable, but the gain is usually small and the cost is not.

---

### [2019 Q.3(b)]

**Question.** Discuss partial and complete pivoting in brief.

**Solution.**

**Partial pivoting.** At step $k$ of the elimination, search column $k$ of the
rows $k$ through $n$ for the entry of largest absolute value, and exchange it
with the entry in position $(k,k)$ before forming the multipliers. The
multiplier is then

$$m_{ik} = \frac{a_{ik}}{a_{kk}}, \qquad |m_{ik}| \le 1$$

hence no multiplier exceeds one in magnitude, and the rounding introduced by the
multiplier is controlled. Partial pivoting searches one column only, and is
sufficient for the great majority of systems.

**Complete pivoting.** At step $k$, search the whole remaining sub-matrix, rows
$k$ through $n$ and columns $k$ through $n$, for the entry of largest absolute
value, and bring it to position $(k,k)$ by a row exchange **and** a column
exchange. Column exchanges reorder the unknowns, so the order in which the
solution vector is written must be restored afterwards. The extra search raises
the cost by a factor of about $n^2$ per step, which is why complete pivoting is
reserved for systems that are nearly singular or where numerical stability is
critical.

**Comparison.**

| | Partial pivoting | Complete pivoting |
| :--- | :--- | :--- |
| Search region | column $k$, rows $k$ to $n$ | sub-matrix, rows and columns $k$ to $n$ |
| Row exchange | yes | yes |
| Column exchange | no | yes, unknown order changes |
| Stability | adequate for most systems | best available |
| Cost | low | higher by a factor of about $n^2$ |

**When it matters.** If the pivot $a_{kk}$ is small relative to the entries below
it, the multiplier $m_{ik}$ is large, and the row $R_i - m_{ik}R_k$ carries a
value dominated by rounding. Choosing the largest available pivot keeps the
magnitude of what is subtracted under control, and prevents a small physical
quantity from being lost against a large one.

---

### [2021 Q.7(a)]

**Question.** Why is pivoting important?

**Solution.**

Every elimination step **divides** by the pivot, the element chosen as divisor.
Pivoting reorders rows or columns so that pivot is as large in magnitude as
possible.

**Two reasons.**

1. **A zero pivot stops the method.** If $a_{kk} = 0$, the step is undefined.
   Row interchange usually fixes it.
2. **A tiny pivot destroys accuracy.** If $a_{kk} = 10^{-9}$ while other entries are
   of order 1, then the multiplier $\frac{a_{ik}}{a_{kk}}$ is of order $10^9$, and
   subtracting such numbers loses most of the significant digits. The computation
   still runs and returns a wrong answer.

**Partial pivoting**, the usual choice, selects the largest $\lvert a_{ik}\rvert$ in
column $k$ below the diagonal and swaps it up. It costs one comparison per candidate
and no extra arithmetic.

**Important limit.** Pivoting improves **stability**, not **conditioning**. The
condition number $\kappa(A)$ is a property of the problem and cannot be changed by
reordering. If $\kappa$ is large, the answer is unreliable no matter how carefully
the elimination is done.

$$
\boxed{\text{Pivoting avoids a zero or tiny divisor, which is where elimination accuracy is lost}}
$$

---

### [2022 Q.3(c)]

**Question.** What is pivoting?

**Solution.**

**Definition.** In Gaussian elimination, **pivoting** is the act of interchanging
rows, or columns, so that the element chosen as the **pivot** (the next divisor)
is as large as possible in magnitude, or at least not negligibly small.

**Why it is needed.** Every elimination step divides by the pivot. If the pivot
happens to be $0$ the step is impossible. If it is merely tiny, say $10^{-9}$, the
multiplier $a_{ik}/a_{kk}$ becomes enormous and the elimination floods the
remaining rows with round off error.

**Two kinds.**

1. **Partial pivoting**, the usual choice: at step $k$, find the largest
   $\left|a_{ik}\right|$ in column $k$ below the diagonal and swap that row up.
   Cost is one comparison per candidate, no extra arithmetic, and it is provably
   stable in practice.
2. **Scaled pivoting**: divide each candidate by its row's largest magnitude
   first, then compare. This stops a row with large entries but a small pivot
   from being unfairly penalised.

**Scaled partial pivoting** chooses $k$ maximising
$\dfrac{\left|a_{ik}\right|}{\max_j\left|a_{ij}\right|}$.

**A third form.** Complete pivoting searches the whole remaining submatrix and
permutes both rows and columns. It is the most stable but costs more and scrambles
the variable order, so its use is confined largely to research codes.

**When pivoting cannot help.** If a whole column of the remaining submatrix is
zero, the matrix is singular and no rearrangement helps. Pivoting cannot create a
nonzero pivot where none exists.

$$
\boxed{\text{Pivoting reorders rows or columns so the divisor is as large as possible, avoiding a tiny pivot and its round off}}
$$

---

<a id="nm-33"></a><a id="nm-3.3"></a>
## NM-3.3 · LU Decomposition & Matrix Inversion

### [2017 Q.4(b)]

**Question.** How can a square matrix be factorized into the form LU to solve linear system of equations?

**Solution.**

**The idea.** A square matrix $A$ can be written as the product of a unit lower
triangular matrix $L$ (ones on the diagonal) and an upper triangular matrix $U$:

$$A = LU$$

Solving $Ax = b$ then becomes two triangular substitutions, which are cheap and
stable:

$$LUx = b \implies Ly = b \implies Ux = y$$

**The construction.** Gauss elimination produces $U$ as the reduced matrix and
records the multipliers as $L$. For a $3\times3$ system:

**Step 1.** Eliminate below the first column using row 1. The multipliers are

$$l_{21} = \frac{a_{21}}{a_{11}}, \qquad l_{31} = \frac{a_{31}}{a_{11}}$$

Form $R_2 \leftarrow R_2 - l_{21}R_1$ and $R_3 \leftarrow R_3 - l_{31}R_1$.
These operations correspond to multiplying $A$ on the left by

$$L_1 = \begin{bmatrix} 1 & 0 & 0 \\ -l_{21} & 1 & 0 \\ -l_{31} & 0 & 1 \end{bmatrix}$$

**Step 2.** Eliminate below the second column of the result. With

$$l_{32} = \frac{a_{32}^{(1)}}{a_{22}^{(1)}} = \frac{a_{32} - l_{31}a_{12}}{a_{22} - l_{21}a_{12}}$$

form $R_3 \leftarrow R_3 - l_{32}R_2^{(1)}$, corresponding to

$$L_2 = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & -l_{32} & 1 \end{bmatrix}$$

**The result.** $L_2L_1A = U$, so

$$A = LU, \qquad L = L_1^{-1}L_2^{-1} = \begin{bmatrix} 1 & 0 & 0 \\ l_{21} & 1 & 0 \\ l_{31} & l_{32} & 1 \end{bmatrix}$$

The multipliers become the sub-diagonal entries of $L$ directly, because the
product of the inverse elementary matrices is the lower triangular matrix with
those multipliers below the diagonal. This is the **Doolittle form**. A variant
that puts $U$'s diagonal into $L$ is the **Crout form**.

**Solving.** Forward-substitute $Ly = b$:

$$y_1 = b_1, \qquad y_2 = b_2 - l_{21}y_1, \qquad y_3 = b_3 - l_{31}y_1 - l_{32}y_2$$

then back-substitute $Ux = y$:

$$x_3 = \frac{y_3}{u_{33}}, \qquad x_2 = \frac{y_2 - u_{23}x_3}{u_{22}}, \qquad x_1 = \frac{y_1 - u_{12}x_2 - u_{13}x_3}{u_{11}}$$

**Why it is useful.** The factorisation is computed once, at roughly
$\dfrac{n^3}{3}$ operations, and any number of right-hand sides can then be
solved at a cost of only $n^2$ each. For $n$ right-hand sides this replaces
$n$ full eliminations by one, and the separation into forward and back
substitution makes the numerical behaviour easy to analyse.

---

<a id="nm-34"></a><a id="nm-3.4"></a>
## NM-3.4 · Jacobi Iteration

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

<a id="nm-35"></a><a id="nm-3.5"></a>
## NM-3.5 · Gauss-Seidel Iteration

### [2018 Q.4(b)]

**Question.** Solve the following circuit by using Gauss-Seidel method.

**Solution.**

**The circuit.** A planar four-mesh DC network in a $2\times2$ arrangement.
Mesh 1 (top-left) contains a $10\ \Omega$ top branch, a $20\ \Omega$ right
branch shared with mesh 2, a $25\ \Omega$ bottom branch shared with mesh 4, and
a connecting wire on the left. Mesh 2 (top-right) contains a $10\ \text{A}$
current source in its top branch directed leftward, the shared $20\ \Omega$ on
its left, a $25\ \Omega$ bottom branch shared with mesh 3, and a wire on the
right. Mesh 3 (bottom-right) contains the shared $25\ \Omega$ on top, a
$4\ \Omega$ left branch shared with mesh 4, an $8\ \Omega$ right branch, and a
wire on the bottom. Mesh 4 (bottom-left) contains the shared $25\ \Omega$ on
top, the shared $4\ \Omega$ on the right, a $100\ \text{V}$ source on the left
directed upward, and a wire on the bottom.

```text
                  10 Ω                         10 A (←)
         +-------/\/\/\/\-------+-------------( ← )-----------+
         |                      |                            |
         |                      |                            |
         |                    [20 Ω]                         |
         |      (↻ I₁)          |            (↻ I₂)          |
         |                      |                            |
         +-------/\/\/\/\-------+------------/\/\/\/\--------+
         |        25 Ω          |             25 Ω           |
         |                      |                            |
       ( ↑ ) 100 V            [4 Ω]                        [8 Ω]
         |                      |                            |
         |      (↻ I₄)          |            (↻ I₃)          ||
         |                      |                            |
         +----------------------+----------------------------+
```

**The current-source constraint.** The $10\ \text{A}$ source occupies the top
branch of mesh 2 alone, so the current in that branch is fixed. Taking the mesh
currents clockwise, the branch carries $I_2$ and the source opposes it:

$$I_2 = -10\ \text{A}$$

**Mesh 1.** Traversing clockwise, the drops are $10I_1$ across the top branch,
$20(I_1 - I_2)$ across the shared $20\ \Omega$, and $25(I_1 - I_4)$ across the
shared $25\ \Omega$:

$$10I_1 + 20(I_1 - I_2) + 25(I_1 - I_4) = 0 \implies 55I_1 - 25I_4 = 20I_2 = -200$$

**Mesh 3.** Traversing clockwise, $8I_3$ across the right branch,
$25(I_3 - I_2)$ across the shared $25\ \Omega$, and $4(I_3 - I_4)$ across the
shared $4\ \Omega$:

$$8I_3 + 25(I_3 - I_2) + 4(I_3 - I_4) = 0 \implies 37I_3 - 4I_4 = 25I_2 = -250$$

**Mesh 4.** Traversing clockwise, $25(I_4 - I_1)$ and $4(I_4 - I_3)$ across the
two shared branches, and the $100\ \text{V}$ source entered against the
traversal:

$$25(I_4 - I_1) + 4(I_4 - I_3) = 100 \implies -25I_1 - 4I_3 + 29I_4 = 100$$

**Gauss-Seidel recursions.** Solve each equation for its diagonal unknown:

$$I_1^{(k+1)} = \frac{-200 + 25I_4^{(k)}}{55}$$

$$I_3^{(k+1)} = \frac{-250 + 4I_4^{(k)}}{37}$$

$$I_4^{(k+1)} = \frac{100 + 25I_1^{(k+1)} + 4I_3^{(k+1)}}{29}$$

Note the ordering: $I_1$ and $I_3$ are computed from the old $I_4$, then $I_4$
is computed from the two just-obtained values. Start from
$I_1 = I_3 = I_4 = 0$.

| Iteration | $I_1$ | $I_3$ | $I_4$ |
| :--: | :-- | :-- | :-- |
| 1 | $-3.636364$ | $-6.756757$ | $-0.618487$ |
| 2 | $-3.917494$ | $-6.823620$ | $-0.870063$ |
| 3 | $-4.031847$ | $-6.850818$ | $-0.972395$ |
| 4 | $-4.078361$ | $-6.861880$ | $-1.014019$ |
| 5 | $-4.097281$ | $-6.866380$ | $-1.030950$ |
| 6 | $-4.104977$ | $-6.868211$ | $-1.037837$ |
| 7 | $-4.108108$ | $-6.868955$ | $-1.040638$ |
| 8 | $-4.109381$ | $-6.869258$ | $-1.041778$ |

**The solution.** The iteration converges, and eliminating gives the same
values:

$$I_1 = -\frac{14390}{3501} = -4.1103\ \text{A}, \qquad I_3 = -\frac{24050}{3501} = -6.8695\ \text{A}, \qquad I_4 = -\frac{3650}{3501} = -1.0426\ \text{A}$$

$$\boxed{I_1 = -4.1103\ \text{A}, \quad I_2 = -10\ \text{A}, \quad I_3 = -6.8695\ \text{A}, \quad I_4 = -1.0426\ \text{A}}$$

> [!info] Check by mesh KVL and by nodal analysis
> Substituting the four mesh currents into the three mesh equations, at the
> four-decimal precision to which they are quoted, gives
> $55(-4.1103) - 25(-1.0426) = -226.0665 + 26.0650 = -200.0015 \approx -200$;
> $37(-6.8695) - 4(-1.0426) = -254.1715 + 4.1704 = -250.0011 \approx -250$;
> $-25(-4.1103) - 4(-6.8695) + 29(-1.0426) = 102.7575 + 27.4780 - 30.2354 = 100.0001 \approx 100$.
> Each residual is at the $10^{-4}$ level, which is what rounding four currents
> to four decimals must produce; on the exact fractions the three equations
> return $-200$, $-250$ and $100$ with no residual at all. Independently,
> nodal analysis with the top-middle, central and top-right nodes as unknowns,
> the left node held at $100\ \text{V}$ and the bottom rail as reference, gives
> node potentials $141.103\ \text{V}$, $23.308\ \text{V}$ and $-54.956\ \text{V}$.
> Reading the mesh currents back out of those potentials,
> $I_1 = (100 - 141.103)/10 = -4.1103$, $I_3 = -54.956/8 = -6.8695$, and
> $I_2 = -10$ follows from the source, agreeing with the mesh solution to four
> digits. Two entirely different formulations reaching the same currents is the
> strongest available confirmation.

> [!note] A convergence note
> The third row has $|29| = |{-25}| + |{-4}| = 29$, so the system is weakly
> diagonally dominant rather than strictly so, and the Gauss-Seidel iteration
> converges slowly. This is visible in the table: the correction per iteration
> falls only gradually. The elimination result is exact and is the value to
> report; the iteration demonstrates the method as asked.

---

### [2019 Q.3(c)]

**Question.** Obtain the nodal equations from the following circuit. Hence solve for the unknowns using Gauss-Seidel iterative method. Show two iterations only.

**Solution.**

**Circuit.** Two non-reference nodes, $V_1$ and $V_2$, with a common reference
ground. Node 1 connects to ground through $2\ \Omega$ and to node 2 through
$4\ \Omega$, with a $5\ \text{A}$ source entering node 1 through the top branch.
Node 2 connects to ground through $6\ \Omega$ and to node 1 through
$4\ \Omega$, with a $5\ \text{A}$ source leaving toward node 1 and a
$10\ \text{A}$ source entering node 2.

```text
                    5 A (enters Node 1)
                +-----------( <- )-----------+
                |                           |
          Node 1|            4 Ω            |Node 2
          ------+----------/\/\/\-----------+-------+
          |                                 |       |
          |                                 |       |
        [2 Ω]                             [6 Ω]   ( ^ ) 10 A
          |                                 |       |
          |                                 |       |
          +---------------------------------+-------+
                          Reference Ground
```

**KCL at node 1.** Currents leaving: through $2\ \Omega$ to ground, through
$4\ \Omega$ to node 2, and $5\ \text{A}$ back through the top branch.

$$\frac{V_1}{2} + \frac{V_1 - V_2}{4} - 5 = 0$$

Multiplying by 4:

$$2V_1 + V_1 - V_2 - 20 = 0 \implies \boxed{3V_1 - V_2 = 20}$$

**KCL at node 2.** Currents leaving: through $6\ \Omega$ to ground, through
$4\ \Omega$ to node 1, and $5\ \text{A}$ through the top branch. The
$10\ \text{A}$ source enters, so it stands on the other side.

$$\frac{V_2}{6} + \frac{V_2 - V_1}{4} + 5 = 10$$

Multiplying by 12:

$$2V_2 + 3(V_2 - V_1) + 60 = 120 \implies \boxed{-3V_1 + 5V_2 = 60}$$

**Gauss-Seidel form.** Solve each equation for the diagonal unknown, and use the
most recent value of the other as soon as it is available.

$$V_1^{(k+1)} = \frac{20 + V_2^{(k)}}{3}, \qquad V_2^{(k+1)} = \frac{60 + 3V_1^{(k+1)}}{5}$$

The coefficient matrix is diagonally dominant, since $|3| > |-1|$ in the first
row and $|5| > |-3|$ in the second, so the iteration converges. Start from
$V_1^{(0)} = V_2^{(0)} = 0$.

| Iteration | $V_1^{(k+1)} = \dfrac{20 + V_2^{(k)}}{3}$ | $V_2^{(k+1)} = \dfrac{60 + 3V_1^{(k+1)}}{5}$ |
| :--: | :-- | :-- |
| 1 | $\dfrac{20 + 0}{3} = 6.666667$ | $\dfrac{60 + 3(6.666667)}{5} = 16.000000$ |
| 2 | $\dfrac{20 + 16}{3} = 12.000000$ | $\dfrac{60 + 3(12)}{5} = 19.200000$ |

Two iterations only, as required.

$$V_1^{(1)} = 6.666667\ \text{V}, \quad V_2^{(1)} = 16.000000\ \text{V}$$
$$V_1^{(2)} = 12.000000\ \text{V}, \quad V_2^{(2)} = 19.200000\ \text{V}$$

**The exact solution, for reference.** Adding the two equations eliminates $V_1$:

$$4V_2 = 80 \implies V_2 = 20\ \text{V}, \qquad 3V_1 = 40 \implies V_1 = 13.333333\ \text{V}$$

$$\boxed{V_1 = 13.3333\ \text{V}, \qquad V_2 = 20\ \text{V}}$$

> [!info] Check against the exact solution
> The iterates approach the exact pair from below in both components:
> $6.6667 \to 12 \to 13.0667 \to 13.28$ against $13.3333$, and
> $16 \to 19.2 \to 19.84 \to 19.968$ against $20$. The errors are
> $6.6667, 1.3333, 0.2667, 0.0533$ and $4, 0.8, 0.16, 0.032$, so each falls by a
> factor of exactly **five** per sweep.
>
> That factor is not an accident and it is worth deriving rather than accepting.
> The Jacobi iteration matrix is $T_J = \begin{bmatrix} 0 & 1/3 \\ 3/5 & 0 \end{bmatrix}$
> with spectral radius $\rho(T_J) = 1/\sqrt{5}$. For Gauss-Seidel, the iteration matrix is
> $T_{GS} = (D-L)^{-1}U = \begin{bmatrix} 0 & 1/3 \\ 0 & 1/5 \end{bmatrix}$, whose non-zero
> eigenvalue is $\lambda = 1/5 = \rho(T_J)^2$. The Gauss-Seidel spectral radius is therefore
> $\rho(T_{GS}) = 1/5$, which means the error contracts by a factor of exactly five in every sweep.
> Either way the recursion was written down the right way round, since a wrong ordering gives a
> spectral radius near or above one.

> [!warning] Where this exam meets the topic again
> The two-node Gauss-Seidel pattern above is the same construction used in
> **Q.8(b)**, where four interior nodes are solved instead of two.

---

### [2020 Q.4(b), 2024 Q.2(b)]

**Appeared in:** 2020 Q.4(b), 2024 Q.2(b)

**Question.** Solve $I_1$, $I_2$ and $I_3$ using Gauss-Seidal method.

**Solution.**

![Three-mesh DC resistive network with a 400 V source, 20, 40, 10 and 100 ohm resistors, and a downward 10 A current source, with clockwise mesh currents I1, I2, I3](diagrams/2020_Q4b_circuit.jpg)
*Figure 2020 Q4(b): three-mesh DC circuit with an independent voltage source and an independent current source (Source: Page 1, Q.4(b))*

**Step 1. Deal with the current source first.** Mesh 3 is bounded on the right by
an ideal $10$ A current source and on the left by the $100\ \Omega$ resistor
shared with mesh 2. A current source **fixes** the branch current, so the
clockwise mesh current is

$$I_3 = 10 \text{ A}$$

This is the step that trips people up. A current source in a branch forces
$I_3$ to equal it, full stop, and it drops out of the system entirely.

**Step 2. Mesh 1, KVL.** Going clockwise around the left loop: rise $400$ V
through the source, drop across the $20\ \Omega$, then across the shared
$40\ \Omega$ which carries $I_1 - I_2$ because $I_2$ returns through it.

$$-400 + 20 I_1 + 40(I_1 - I_2) = 0$$

$$60 I_1 - 40 I_2 = 400$$

**Step 3. Mesh 2, KVL.** The $40\ \Omega$ carries $I_2 - I_1$, the $10\ \Omega$
carries $I_2$ alone, and the $100\ \Omega$ carries $I_2 - I_3$.

$$40(I_2 - I_1) + 10 I_2 + 100(I_2 - I_3) = 0$$

$$-40 I_1 + 150 I_2 = 100 I_3 = 1000$$

**Step 4. The system to iterate.** Three equations, but $I_3$ is already known, so
two unknowns remain:

$$\begin{cases} 60 I_1 - 40 I_2 = 400 \\ -40 I_1 + 150 I_2 = 1000 \end{cases}$$

Solve each for its own variable, newest value first:

$$\begin{cases} I_1 = \dfrac{40 I_2 + 400}{60} \\[3mm] I_2 = \dfrac{1000 + 40 I_1}{150} \end{cases}$$

**Step 5. Gauss-Seidel.** Use the value just computed, never the previous
iteration's. Start from $I_1^{(0)} = I_2^{(0)} = 0$.

| $k$ | $I_1$ | $I_2$ |
| --: | --: | --: |
| 0 | 0.000000 | 0.000000 |
| 1 | 6.666667 | 8.444444 |
| 2 | 12.296296 | 9.945679 |
| 3 | 13.297119 | 10.212565 |
| 4 | 13.475043 | 10.260012 |
| 5 | 13.506674 | 10.268447 |
| 6 | 13.512298 | 10.269946 |
| 7 | 13.513297 | 10.270213 |
| 8 | 13.513475 | 10.270260 |
| 9 | 13.513507 | 10.270268 |
| 10 | 13.513512 | 10.270270 |

Iteration 1: $I_1^{(1)} = \frac{40(0) + 400}{60} = 6.666667$, then
$I_2^{(1)} = \frac{1000 + 40(6.666667)}{150} = \frac{1000 + 266.6667}{150} = 8.444444$.

**Step 6. Answer.**

$$
\boxed{I_1 = 13.5135 \text{ A}, \qquad I_2 = 10.2703 \text{ A}, \qquad I_3 = 10.0000 \text{ A}}
$$

> [!info] Check by two independent routes
> **Exact solution.** The $2\times2$ system is solved directly by elimination:
> multiply the first equation by $150$ and the second by $40$, then add.
> $9000 I_1 - 6000 I_2 = 60000$ and $-1600 I_1 + 6000 I_2 = 40000$. Adding gives
> $7400 I_1 = 100000$, so
> $$I_1 = \frac{100000}{7400} = \frac{500}{37} = 13.513514, \qquad I_2 = \frac{380}{37} = 10.270270$$
> Both are exact rationals. Gauss-Seidel iteration 10 returns $13.513512$ and
> $10.270270$: the second matches to six decimal places, the first to six
> significant figures. $I_1$ needs iteration 13 to reach $13.513514$ on the nose.
> The two variables converge at different rates because $I_1$ is updated first in
> each sweep and $I_2$ therefore always uses a fresher $I_1$.
>
> **Substitute back into the mesh equations.** Mesh 1:
> $60(13.513514) - 40(10.270270) = 810.8108 - 410.8108 = 400$ exactly.
> Mesh 2: $-40(13.513514) + 150(10.270270) - 100(10) = -540.5406 + 1540.5405 - 1000 = 0$
> to within $10^{-13}$. Both KVL loops close.
>
> **Convergence rate.** The errors in $I_1$ fall $6.8468, 1.2172, 0.2164, 0.0385$,
> $0.0068$ over the first five sweeps, a factor of exactly $5.625$ each time.
> That factor is $1/\rho^2$ where $\rho = 0.4216$ is the spectral radius computed
> below: $1/(0.4216)^2 = 5.625$. The errors in $I_2$ fall $1.8258, 0.3246, 0.0577$,
> $0.0103, 0.0018$, the same ratio.

> [!warning] The row order decides whether this converges at all
> Solve equation 2 first, $I_2 = \frac{1000 + 40 I_1}{150}$, and the iteration
> **diverges**: $-25$, $-203.1$, $-1205.1$, $-6841.1$, $-38543$. The values grow
> without bound.
>
> The reason is the iteration matrix. In the order used above it is
> $$\begin{bmatrix} 0 & \frac{40}{60} \\ \frac{40}{150} & 0 \end{bmatrix} = \begin{bmatrix} 0 & 0.6667 \\ 0.2667 & 0 \end{bmatrix}$$
> whose eigenvalues are $\pm\sqrt{0.6667 \times 0.2667} = \pm 0.4216$, so the
> spectral radius is $0.4216 < 1$ and the iteration contracts. Reverse the order
> and it becomes
> $$\begin{bmatrix} 0 & \frac{150}{40} \\ \frac{60}{40} & 0 \end{bmatrix}$$
> with spectral radius $\sqrt{3.75 \times 1.5} = 2.3717 > 1$, which diverges.
>
> The fix is the same everywhere in this course: **keep a diagonal-dominant
> ordering.** Each equation should solve for the variable with the largest
> coefficient in that row. Here that is $I_1$ in row 1 ($60$ beats $40$) and
> $I_2$ in row 2 ($150$ beats $40$), which is exactly the order used. The same
> trap appears in 2021 Q.7(b), 2023 and 2024.

> [!note] Sanity check on the current directions
> All three mesh currents come out positive, so all three really do run clockwise
> as assumed. $I_2 = 10.27$ A exceeds the $10$ A in the source branch, and that
> is consistent: the $10$ A source pushes current into the node shared with the
> $100\ \Omega$ resistor, and the $150\ \Omega$ mesh must carry slightly more
> than that because it also returns some of $I_1$'s current through the shared
> $40\ \Omega$. A negative value anywhere would mean the assumed direction was
> wrong and must be flipped before the answer means anything.

---

---

### [2021 Q.7(b)]

**Question.** Determine the value of $I_0$ in the given circuit using Gauss-Seidel method.

**Solution.**

![DC circuit with a 30 V independent voltage source, 10, 15, 8 and 20 ohm resistors, and a dependent voltage source 5I0, with branch current I0 through the 10 ohm resistor](diagrams/2021_Q7b_circuit.jpg)
*Figure 2021 Q7(b): DC circuit with independent 30 V source, four resistors, and dependent voltage source $5I_0$ (Source: Page 2, Q7(b))*

**Step 1. Name the nodes.** Take the bottom rail as reference, $0$ V.

| Node | Voltage |
| :-- | :-- |
| Top rail | $V_T = 30$ V, held by the ideal source |
| Centre node $C$ | $V_C$ |
| Right node $R$ | $V_R$ |

**Step 2. Express the controlling current.**

$$
I_0 = \frac{V_T - V_C}{10} = \frac{30 - V_C}{10}
$$

**Step 3. Apply the dependent source.** The $5I_0$ source sets the right node:

$$
V_R = 5I_0 = 5\left(\frac{30 - V_C}{10}\right) = 15 - 0.5V_C
$$

Rearranged, that is one equation ready for iteration:

$$
V_C + 2V_R = 30
$$

**Step 4. KCL at node $C$.** Three branches leave it, toward the top rail, toward
ground, and toward node $R$:

$$
\frac{V_C - 30}{10} + \frac{V_C - 0}{15} + \frac{V_C - V_R}{8} = 0
$$

Multiplying by $120$,

$$
12(V_C - 30) + 8V_C + 15(V_C - V_R) = 0
$$

$$
12V_C - 360 + 8V_C + 15V_C - 15V_R = 0
$$

$$
35V_C - 15V_R = 360
$$

**Step 5. The system to iterate.**

$$
\begin{cases}
V_C = \dfrac{15V_R + 360}{35} \\[2mm]
V_R = \dfrac{30 - V_C}{2}
\end{cases}
$$

**Step 6. Gauss-Seidel.** Use the value just computed, never the previous
iteration's. Start from $V_C^{(0)} = V_R^{(0)} = 0$.

| $k$ | $V_C$ | $V_R$ |
| ---: | --: | --: |
| 0 | 0.000000 | 0.000000 |
| 1 | 10.285714 | 9.857143 |
| 2 | 14.510204 | 7.744898 |
| 3 | 13.604956 | 8.197522 |
| 4 | 13.798938 | 8.100531 |
| 5 | 13.757370 | 8.121315 |
| 6 | 13.766278 | 8.116861 |
| 7 | 13.764369 | 8.117815 |
| 8 | 13.764778 | 8.117611 |

Iteration 1: $V_C^{(1)} = \frac{15(0) + 360}{35} = 10.285714$, then
$V_R^{(1)} = \frac{30 - 10.285714}{2} = 9.857143$.

**Step 7. Read off $I_0$.**

$$
I_0 = \frac{30 - 13.764778}{10} = \frac{16.235222}{10} = 1.6235 \text{ A}
$$

$$
\boxed{I_0 = 1.6235 \text{ A}, \quad V_C = 13.7648 \text{ V}, \quad V_R = 8.1176 \text{ V}}
$$

> [!info] Check by two independent routes
> **Direct solution.** Eliminating $V_C$ from the two equations gives
> $V_C = \frac{234}{17} = 13.7647058824$ and $V_R = \frac{138}{17} = 8.1176470588$,
> so
> $$I_0 = \frac{30 - 234/17}{10} = \frac{138}{85} = 1.6235294118$$
> Iteration 8 gives $I_0 = 1.623522$, agreeing with the closed form to four
> decimals. The residual in $V_C$ is $7.2 \times 10^{-5}$ there, and it falls by a
> factor of about $4.6$ per sweep: iteration 10 gives $I_0 = 1.623529$ and
> iteration 12 gives $1.6235294$, matching the closed form to seven figures.
>
> Note the alternation in the $V_C$ column: high, low, high, low, $13.764778$ then
> $13.764690$. Gauss-Seidel overshoots one way then the other while it contracts,
> so the residual is **not** monotone even though the answer is. Judging
> convergence by "is the last step change small" therefore needs a tolerance, not
> an exact-match test.
>
> **Consistency of the dependent source.** $5I_0 = 5(1.6235294) = 8.1176471$, and
> $V_R = \frac{138}{17} = 8.1176471$. The two agree, which they must, since
> $V_R$ was **defined** as $5I_0$.
>
> **KCL residual.** $\frac{V_C-30}{10} + \frac{V_C}{15} + \frac{V_C-V_R}{8} = 0$ exactly at
> the converged values.

> [!warning] The row order decides whether Gauss-Seidel converges at all
> Solve equation 2 first, $V_C = 30 - 2V_R$, and the iteration **diverges**:
> $V_C = 30.0$, then $-62.0$, then $367.3$, then $-1636.2$, then $7713.7$. The
> sequence grows without bound.
>
> The reason is visible in the diagonal of the coefficient matrix. Written in the
> order above, rows $35V_C - 15V_R = 360$ and $V_C + 2V_R = 30$, it is
> $$\begin{bmatrix} 35 & -15 \\ 1 & 2\end{bmatrix}$$
> with diagonal magnitudes $35$ and $2$ against off-diagonal sums $15$ and $1$.
> Both rows are strictly dominant, $35 > 15$ and $2 > 1$, which is what guarantees
> convergence in this ordering.
>
> Reversed, the rows become $\begin{bmatrix} 1 & 2 \\ 35 & -15\end{bmatrix}$, and
> now neither row is dominant: $1 < 2$ and $15 < 35$. That loss of dominance is
> exactly the divergence.
>
> The Gauss-Seidel iteration matrices confirm it. In the working order,
> $V_R^{(k+1)} = \frac{690 - 15V_R^{(k)}}{70}$, so the matrix is
> $$\begin{bmatrix} 0 & 15/35 \\ 0 & -15/70 \end{bmatrix}$$
> with spectral radius $\frac{15}{70} = 0.214 < 1$, so it converges. In the
> reversed order, $V_R^{(k+1)} = 46 - \frac{14}{3}V_R^{(k)}$, so the matrix is
> $$\begin{bmatrix} 0 & -2 \\ 0 & -14/3 \end{bmatrix}$$
> with spectral radius $\frac{14}{3} = 4.67 > 1$, which diverges.
>
> This is the same trap as the Gauss-Seidel questions in 2023 and 2024, and the
> fix is always the same: keep a diagonal-dominant ordering.

---

---

**Also asked here.**

- *2017 Q.4(c)* is the same question as [[NM-3.6_Relaxation|NM-3.6]], which is written in `NM-3.6`.

---

**Answered in phase P6, in `../CT_Questions/`.**

- *CT-02B Q.1(a)* is a class-test question. Its answer is in `../CT_Questions/CT_answers_exam_style.md`, with the reasoning in `../CT_Questions/CT_answers_explanation.md`.
- *CT-02B Q.1(b)* is a class-test question. Its answer is in `../CT_Questions/CT_answers_exam_style.md`, with the reasoning in `../CT_Questions/CT_answers_explanation.md`.
- *CT-02B Q.1(c)* is a class-test question. Its answer is in `../CT_Questions/CT_answers_exam_style.md`, with the reasoning in `../CT_Questions/CT_answers_explanation.md`.

---

<a id="nm-36"></a><a id="nm-3.6"></a>
## NM-3.6 · Relaxation

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

<a id="nm-37"></a><a id="nm-3.7"></a>
## NM-3.7 · Ill-Conditioned Systems

### [2022 Q.4(c)]

**Question.** Define ill-conditioned system.

**Solution.**

**Definition.** A system of linear equations is **ill-conditioned** when a small
change in the input produces a disproportionately large change in the solution.

**Measure.** The **condition number** $\kappa$ of the coefficient matrix is the
ratio of the largest to the smallest relative error:

$$
\frac{\dfrac{\|\delta x\|}{\|x\|}}{\dfrac{\|\delta b\|}{\|b\|}} \le \kappa(A)
$$

Thus a relative error of $\epsilon$ in the data may become up to $\kappa\epsilon$ in
the answer.

| $\kappa$ | Behaviour |
| :-- | :-- |
| $\kappa = 1$ | Perfectly conditioned, error passes through unchanged |
| $\kappa \approx 10$ | Mild amplification |
| $\kappa \approx 10^6$ | Loss of about six significant digits |
| $\kappa > 10^{16}$ | All precision lost; the matrix is numerically singular |

**Causes.**

1. **A matrix that is nearly singular**, that is one with an eigenvalue very
   close to zero, or one whose rows are almost linearly dependent. Two nearly
   parallel equations then constrain the solution very weakly.
2. **Rows or columns of wildly different magnitudes.** The small ones are
   effectively ignored.
3. **A bad choice of variables.** Two variables that measure nearly the same
   physical quantity make the corresponding columns almost equal.

**Why it matters in engineering.** The data itself has uncertainty, typically
$10^{-4}$ relative from the instrument. If $\kappa = 10^{8}$ then the answer
carries a relative uncertainty of $10^4$, which is useless, even though the
computation ran to machine precision.

**What to do about it.** Row or column scaling to make the entries comparable,
choosing better-conditioned variables, reformulating the physical problem, or
using higher precision. **Pivoting helps stability but does not change
$\kappa$.** Conditioning is a property of the problem, not of the algorithm.

$$
\boxed{\text{ill-conditioned means small input errors produce large output errors; measured by }\kappa}
$$

---

<a id="nm-38"></a><a id="nm-3.8"></a>
## NM-3.8 · Circuit Applications

---

**Every question that reaches this subtopic is written in the subtopic it is filed under.** Nothing is answered here, and that is deliberate rather than an omission: the subtopic holds the questions in the taxonomy but owns no block of its own.

- *2018 Q.4(b)* is the same question as [[NM-3.5_Gauss_Seidel_Iteration|NM-3.5]], which is written in `NM-3.5`.
- *2019 Q.3(c)* is the same question as [[NM-3.5_Gauss_Seidel_Iteration|NM-3.5]], which is written in `NM-3.5`.
- *2020 Q.4(b)* is the same question as [[NM-3.5_Gauss_Seidel_Iteration|NM-3.5]], which is written in `NM-3.5`.
- *2021 Q.7(b)* is the same question as [[NM-3.5_Gauss_Seidel_Iteration|NM-3.5]], which is written in `NM-3.5`.
- *2024 Q.2(b)* is the same question as [[NM-3.5_Gauss_Seidel_Iteration|NM-3.5]], which is written in `NM-3.5`.

---

[🏠 Master Index](00_Index.md) | [← Prev Topic: NM-2 · Roots of Equations](NM-2_Roots_of_Equations.md) | [Next Topic: NM-4 · Curve Fitting →](NM-4_Curve_Fitting.md)
