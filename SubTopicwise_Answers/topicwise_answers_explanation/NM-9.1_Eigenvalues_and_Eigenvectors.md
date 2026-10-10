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

Every block below is copied from `../answers_explanation/`. The reasoning
is written once, in the year-wise file, and is not restated here.


### [2017 Q.7(b), 2023 Q.3(a)]

**Appeared in:** 2017 Q.7(b), 2023 Q.3(a)

**Question.** Find the eigen-values and eigen-vectors of the following matrix, $A = \begin{bmatrix} 5 & 0 & 1 \\ 0 & -2 & 0 \\ 1 & 0 & 5 \end{bmatrix}$.

*[Marks: 06]*

**Solution.**

**Step 1, the characteristic polynomial.** Form $A - \lambda I$:

$$A - \lambda I = \begin{bmatrix} 5-\lambda & 0 & 1 \\ 0 & -2-\lambda & 0 \\ 1 & 0 & 5-\lambda \end{bmatrix}$$

**Step 2, take the determinant along the sparse row.** The second row has only
one non-zero entry, so expanding along it costs nothing:

$$\det(A - \lambda I) = (-2-\lambda)\left[(5-\lambda)^2 - 1\right]$$

$$= (-2-\lambda)(25 - 10\lambda + \lambda^2 - 1) = (-2-\lambda)(\lambda^2 - 10\lambda + 24)$$

$$= (-2-\lambda)(\lambda - 4)(\lambda - 6)$$

> [!note] Why this matrix is worth choosing
> It is *almost* reducible. Row 2 and column 2 are decoupled from everything
> else, so the middle eigenvalue $-2$ comes straight off the sparse row and the
> remaining $2\times2$ block $\begin{bmatrix} 5 & 1 \\ 1 & 5\end{bmatrix}$ gives
> the pair $4$ and $6$. On an arbitrary matrix you would be stuck with a cubic;
> here the structure is visible in the determinant itself, which is why the
> expansion above is two lines instead of a page.

**The eigenvalues.**

$$\boxed{\lambda = -2,\ 4,\ 6}$$

**The eigenvectors.** For each eigenvalue, solve $(A - \lambda I)v = 0$.

**For $\lambda = -2$.** The matrix becomes
$\begin{bmatrix} 7 & 0 & 1 \\ 0 & 0 & 0 \\ 1 & 0 & 7 \end{bmatrix}$. Rows 1 and
3 both give $7x + z = 0$, so $z = -7x$, and row 2 leaves $y$ free. Taking $y$
free and $x = 0$ gives the simplest solution:

$$v_{-2} = \begin{bmatrix} 0 \\ 1 \\ 0 \end{bmatrix}$$

(Any multiple of this is also an eigenvector.)

**For $\lambda = 4$.** The matrix becomes
$\begin{bmatrix} 1 & 0 & 1 \\ 0 & -6 & 0 \\ 1 & 0 & 1 \end{bmatrix}$. Row 1
gives $x + z = 0$, so $z = -x$, and row 2 forces $y = 0$:

$$v_4 = \begin{bmatrix} -1 \\ 0 \\ 1 \end{bmatrix}$$

**For $\lambda = 6$.** The matrix becomes
$\begin{bmatrix} -1 & 0 & 1 \\ 0 & -8 & 0 \\ 1 & 0 & -1 \end{bmatrix}$. Row 1
gives $-x + z = 0$, so $z = x$, and row 2 forces $y = 0$ again:

$$v_6 = \begin{bmatrix} 1 \\ 0 \\ 1 \end{bmatrix}$$

**Normalised eigenvectors**, for completeness:

$$\hat v_{-2} = \begin{bmatrix} 0 \\ 1 \\ 0 \end{bmatrix}, \qquad \hat v_4 = \begin{bmatrix} -1/\sqrt{2} \\ 0 \\ 1/\sqrt{2} \end{bmatrix}, \qquad \hat v_6 = \begin{bmatrix} 1/\sqrt{2} \\ 0 \\ 1/\sqrt{2} \end{bmatrix}$$

**Orthogonality.** $A$ is symmetric, so eigenvectors for distinct eigenvalues are
orthogonal:

$$v_{-2}^{\mathsf T}v_4 = 0, \qquad v_{-2}^{\mathsf T}v_6 = 0, \qquad v_4^{\mathsf T}v_6 = -1 + 1 = 0$$

> [!info] Check by direct multiplication and by the trace
> Multiplying out:
> $A(0,1,0)^{\mathsf T} = (0, -2, 0)^{\mathsf T} = -2(0,1,0)^{\mathsf T}$;
> $A(-1,0,1)^{\mathsf T} = (4, 0, 4)^{\mathsf T} = 4(-1,0,1)^{\mathsf T}$;
> $A(1,0,1)^{\mathsf T} = (6, 0, 6)^{\mathsf T} = 6(1,0,1)^{\mathsf T}$. Every
> eigenvector is verified directly.
>
> Then two scalar checks on the eigenvalues, which use no eigenvector
> information at all. Their **sum** must equal the trace:
> $-2 + 4 + 6 = 8$ against $\operatorname{tr}A = 5 + (-2) + 5 = 8$. Their
> **product** must equal the determinant: $(-2)(4)(6) = -48$ against
> $$\det A = 5\left[(-2)(5) - 0\right] - 0 + 1\left[0 - (-2)(1)\right] = -50 + 2 = -48.$$
> The trace and the determinant are computed from the matrix alone, so these two
> checks are genuinely independent of the characteristic polynomial. A slip in
> expanding the determinant breaks one of them immediately.

---

[🏠 Subtopic Index](00_Index.md) | [← Prev: NM-8.8 Boundary Value Problems](NM-8.8_Boundary_Value_Problems.md) | [Next: NM-10.1 PDE Classification & Theory →](NM-10.1_PDE_Classification_and_Theory.md)
