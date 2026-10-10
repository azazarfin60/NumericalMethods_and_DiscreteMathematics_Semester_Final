---
title: "NM-9 · Matrix Eigenvalues & Eigenvectors"
tags:
  - numerical-methods
  - discrete-mathematics
  - topicwise-clusters
---

[🏠 Master Index](00_Index.md) | [← Prev Topic: NM-8 · ODE](NM-8_Ordinary_Differential_Equations.md) | [Next Topic: NM-10 · PDE →](NM-10_Partial_Differential_Equations.md)

---

# NM-9 · Matrix Eigenvalues & Eigenvectors

> **Topic ID:** NM-9  
> **Section:** Section A -- Numerical Methods  
> **Exam Weight:** 🟡 Low / Light (Tier 3) | 2/8 Years Examined | Typical Weight: 3–5 marks  
> **Subtopics Included:** 1 subtopics (NM-9.1 through NM-9.1)  
> **Origin Layer:** Authored in `../answers_exam_style/`. All numerical results and boxed equations match character-for-character.

---

## 📑 Subtopics Covered in this Cluster

| Subtopic ID | Subtopic Title | Priority | Exam Frequency | Section Navigation |
|:---|:---|:---:|:---:|:---|
| **NM-9.1** | Eigenvalues & Eigenvectors | 🟡 ⚠️ | 2017, 2023 | [Jump to NM-9.1](#nm-91) |

---

<a id="nm-91"></a><a id="nm-9.1"></a>
## NM-9.1 · Eigenvalues & Eigenvectors

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

[🏠 Master Index](00_Index.md) | [← Prev Topic: NM-8 · ODE](NM-8_Ordinary_Differential_Equations.md) | [Next Topic: NM-10 · PDE →](NM-10_Partial_Differential_Equations.md)
