---
title: "NM-9.1 · Eigenvalues & Eigenvectors"
tags:
  - numerical-methods
  - discrete-mathematics
  - topicwise
---





[🏠 Subtopic Index](00_Index.md) | [← Prev: NM-8.8 Boundary Value Problems](NM-8.8_Boundary_Value_Problems.md) | [Next: NM-10.1 PDE Classification & Theory →](NM-10.1_PDE_Classification_and_Theory.md)

---

# NM-9.1 · Eigenvalues & Eigenvectors

Every block below is copied from `../answers_exam_style/`, which is the
only place an answer is authored. A number here is the same number, character
for character, as the one it came from.


### [2017 Q.7(b), 2023 Q.3(a)]

**Appeared in:** 2017 Q.7(b), 2023 Q.3(a)

**Question.** Find the eigen-values and eigen-vectors of the following matrix, $A = \begin{bmatrix} 5 & 0 & 1 \\ 0 & -2 & 0 \\ 1 & 0 & 5 \end{bmatrix}$.

**Solution.**

**The characteristic polynomial.** Form $A - \lambda I$:

$$A - \lambda I = \begin{bmatrix} 5-\lambda & 0 & 1 \\ 0 & -2-\lambda & 0 \\ 1 & 0 & 5-\lambda \end{bmatrix}$$

Taking the determinant along the second row, which has only one non-zero entry:

$$\det(A - \lambda I) = (-2-\lambda)\left[(5-\lambda)^2 - 1\right]$$

$$= (-2-\lambda)(25 - 10\lambda + \lambda^2 - 1) = (-2-\lambda)(\lambda^2 - 10\lambda + 24)$$

$$= (-2-\lambda)(\lambda - 4)(\lambda - 6)$$

**The eigenvalues.** Setting the determinant to zero:

$$\lambda = -2, \qquad \lambda = 4, \qquad \lambda = 6$$

$$\boxed{\lambda = -2,\ 4,\ 6}$$

**The eigenvectors.** For each eigenvalue, solve $(A - \lambda I)v = 0$.

**For $\lambda = -2$.** The matrix becomes
$\begin{bmatrix} 7 & 0 & 1 \\ 0 & 0 & 0 \\ 1 & 0 & 7 \end{bmatrix}$, and the first
and third rows give $7x + z = 0$, so $z = -7x$ with $y$ free. Taking $y$ free
and $x = 0$ gives the simplest solution:

$$v_{-2} = \begin{bmatrix} 0 \\ 1 \\ 0 \end{bmatrix}$$

(Any multiple of this is also an eigenvector.)

**For $\lambda = 4$.** The matrix becomes
$\begin{bmatrix} 1 & 0 & 1 \\ 0 & -6 & 0 \\ 1 & 0 & 1 \end{bmatrix}$, and the first
row gives $x + z = 0$, so $z = -x$, with the second row forcing $y = 0$:

$$v_4 = \begin{bmatrix} -1 \\ 0 \\ 1 \end{bmatrix}$$

**For $\lambda = 6$.** The matrix becomes
$\begin{bmatrix} -1 & 0 & 1 \\ 0 & -8 & 0 \\ 1 & 0 & -1 \end{bmatrix}$, and the first
row gives $-x + z = 0$, so $z = x$, with $y = 0$ again:

$$v_6 = \begin{bmatrix} 1 \\ 0 \\ 1 \end{bmatrix}$$

**Normalised eigenvectors**, for completeness:

$$\hat v_{-2} = \begin{bmatrix} 0 \\ 1 \\ 0 \end{bmatrix}, \qquad \hat v_4 = \begin{bmatrix} -1/\sqrt{2} \\ 0 \\ 1/\sqrt{2} \end{bmatrix}, \qquad \hat v_6 = \begin{bmatrix} 1/\sqrt{2} \\ 0 \\ 1/\sqrt{2} \end{bmatrix}$$

**Orthogonality.** The matrix is symmetric, so its eigenvectors for distinct
eigenvalues are orthogonal:

$$v_{-2}^{\mathsf T}v_4 = 0, \qquad v_{-2}^{\mathsf T}v_6 = 0, \qquad v_4^{\mathsf T}v_6 = -1 + 1 = 0$$

> [!info] Check by direct multiplication and by the trace
> Multiplying out: $A(0,1,0)^{\mathsf T} = (0, -2, 0)^{\mathsf T} = -2(0,1,0)^{\mathsf T}$ ✓;
> $A(-1,0,1)^{\mathsf T} = (4, 0, 4)^{\mathsf T} = 4(-1,0,1)^{\mathsf T}$ ✓;
> $A(1,0,1)^{\mathsf T} = (6, 0, 6)^{\mathsf T} = 6(1,0,1)^{\mathsf T}$ ✓. Every
> eigenvector is verified directly. As an independent check on the eigenvalues,
> their sum must equal the trace of $A$: $-2 + 4 + 6 = 8$, and
> $\operatorname{tr}A = 5 + (-2) + 5 = 8$ ✓. Their product must equal the
> determinant: $(-2)(4)(6) = -48$, and $\det A = 5(-2)(5) - 1(-2)(1) = -50 + 2 = -48$ ✓.
> The trace and determinant are computed from the matrix alone, so the two
> checks involve no knowledge of the eigenvectors, which makes them a genuinely
> independent confirmation of the characteristic polynomial.

---

[🏠 Subtopic Index](00_Index.md) | [← Prev: NM-8.8 Boundary Value Problems](NM-8.8_Boundary_Value_Problems.md) | [Next: NM-10.1 PDE Classification & Theory →](NM-10.1_PDE_Classification_and_Theory.md)
