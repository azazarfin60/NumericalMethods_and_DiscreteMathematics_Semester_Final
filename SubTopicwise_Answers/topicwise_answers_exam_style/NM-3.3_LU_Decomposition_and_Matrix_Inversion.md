---
title: "NM-3.3 · LU Decomposition & Matrix Inversion"
tags:
  - numerical-methods
  - discrete-mathematics
  - topicwise
---





[🏠 Subtopic Index](00_Index.md) | [← Prev: NM-3.2 Pivoting](NM-3.2_Pivoting.md) | [Next: NM-3.4 Jacobi Iteration →](NM-3.4_Jacobi_Iteration.md)

---

# NM-3.3 · LU Decomposition & Matrix Inversion

Every block below is copied from `../answers_exam_style/`, which is the
only place an answer is authored. A number here is the same number, character
for character, as the one it came from.


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

[🏠 Subtopic Index](00_Index.md) | [← Prev: NM-3.2 Pivoting](NM-3.2_Pivoting.md) | [Next: NM-3.4 Jacobi Iteration →](NM-3.4_Jacobi_Iteration.md)
