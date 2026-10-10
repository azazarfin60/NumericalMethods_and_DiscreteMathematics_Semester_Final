# NM-9: Eigenvalues & Eigenvectors

> **Section:** Section A (Numerical Methods)  
> **Subtopics in this folder:** 1 file (NM-9.1)  
> **Exam weight:** Appears in 2/8 papers (25% frequency: 2017 Q.7(b), 2023 Q.3(a)), worth 5--6 marks when tested.

---

## 📖 How to Read This Topic

Eigenvalue problems sit at the crossroads of matrix algebra and physical engineering systems. In circuit analysis, mechanical vibrations, and control systems, eigenvalues represent natural resonant frequencies, time constants, and stability boundaries.

Whenever an $n \times n$ matrix $A$ acts on a vector $\mathbf{x}$, it typically rotates the vector and changes its length. But for certain special directions, the matrix acts like a simple scalar multiplier:

$$
A\mathbf{x} = \lambda\mathbf{x}
$$

Those invariant directions are **eigenvectors**, and the scaling factors $\lambda$ are **eigenvalues**.

In RUET semester finals, NM-9 is the most predictable topic in the entire syllabus:
- The exam has tested eigenvalues twice (2017 and 2023).
- **Both times, the examiners set the exact same $3 \times 3$ symmetric matrix**, taken directly from Jain, §7.7, Example 7.15!
- The matrix features a sparse row that makes determinant evaluation effortless if you expand along the second row.

Mastering this single subtopic guarantees you full marks whenever an eigenvalue problem appears on your paper.

**Suggested reading time:** ~15 minutes for the entire topic folder.

---

## 📑 Subtopic Index

| # | File | Priority | Exam Freq | Reading Time | Core Concept |
|:---:|:---|:---:|:---:|:---:|:---|
| 1 | [NM-9.1: Eigenvalues and Eigenvectors](NM-9.1_Eigenvalues_and_Eigenvectors.md) | 🟡 | 2/8 years (2017, 2023) | ~15 min | Characteristic polynomial $|A - \lambda I| = 0$, sparse cofactor expansion, homogeneous nullspace solving, unit normalization, trace and determinant verification |

---

## 🎯 Exam Pattern for This Topic

In RUET semester finals, eigenvalue questions appear in Section A under Question 3 or Question 7:

### 1. The Classic $3 \times 3$ Symmetric Matrix (5--6 Marks)
Both 2017 Q.7(b) (6 marks) and 2023 Q.3(a) (5 marks) asked for the eigenvalues and eigenvectors of:

$$
A = \begin{bmatrix} 5 & 0 & 1 \\ 0 & -2 & 0 \\ 1 & 0 & 5 \end{bmatrix}
$$

Examiners expect four clear components in your solution:
1. **Characteristic polynomial:** Setting $\det(A - \lambda I) = 0$ and factoring it into $(\lambda + 2)(\lambda - 4)(\lambda - 6) = 0$.
2. **Eigenvalues:** Stating $\lambda = -2, 4, 6$.
3. **Eigenvectors:** Solving $(A - \lambda I)\mathbf{v} = \mathbf{0}$ for each eigenvalue by assigning convenient values to free variables.
4. **Normalized eigenvectors & orthogonality:** Dividing each vector by its Euclidean norm and noting that distinct eigenvectors of a symmetric matrix are mutually orthogonal.

### 2. The Sparse Expansion Shortcut
The second row of matrix $A$ contains only one non-zero entry ($a_{22} = -2$). Expanding the determinant along row 2 pulls out the factor $(-2 - \lambda)$ immediately. You never need to expand a tedious $3 \times 3$ cubic polynomial from scratch.

### 3. Iterative Power Method Context
Textbook Section §7.7 in Jain also presents the iterative **Power Method** (Example 7.16) for finding the dominant eigenvalue of higher-order systems. While RUET has so far only examined the direct algebraic method, knowing the power method gives you a solid backup if a theory question asks how large engineering matrices are solved.

---

## 🔗 Topic Connections

- **Prerequisites:** 
  - Matrix operations, determinants, and homogeneous linear systems from [NM-3: Linear Systems](../NM-3_Linear_Systems/_Topic_Overview.md).
- **Leads to:**
  - [NM-10: Partial Differential Equations](../NM-10_PDE/_Topic_Overview.md) -- the spectral radius (largest absolute eigenvalue) governs the convergence rate of iterative solvers like Liebmann's method and the numerical stability of finite difference schemes.
- **Pairs with in exam:**
  - Often paired with ODE numerical schemes ([NM-8](../NM-8_ODE/_Topic_Overview.md)) or PDE boundary value formulations ([NM-10](../NM-10_PDE/_Topic_Overview.md)) to complete Section A.
