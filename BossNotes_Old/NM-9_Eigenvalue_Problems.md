[← Previous: NM-8 Lower — IVP, BVP, Heun, RK2](NM-8_Lower_IVP_BVP_Heun_RK2_Higher.md) | [🏠 Index](00_Index.md) | [Next: NM-10 Partial Differential Equations →](NM-10_Partial_Differential_Equations.md)

---

# NM-9: Eigenvalue Problems
> **Section:** A (Numerical Methods) | **Priority:** 🟡 | **Exam Frequency:** 2/8 years | **Subtopics:** NM-9.1
> **Sources:** Jain Ch.7 §7.7 (pp. 284–288), Example 7.15

## Why This Topic Matters

This is the lightest numerical topic in the course. It appeared twice, in 2017 and 2023, and **the exact same matrix was set both times**, lifted straight from Jain's Example 7.15. Learn that one matrix thoroughly and you have covered every eigenvalue question this course has ever asked.

---

## 📝 Key Definitions

> **Eigenvalue and eigenvector:** "Let $A$ be a square matrix of order $n$ with elements $a_{ij}$. We wish to find a column vector $X$ and a constant $\lambda$ such that $AX = \lambda X$. In Eq. (7.67), $\lambda$ is called the *eigenvalue* and $X$ is called the corresponding *eigenvector*." — Jain, §7.7 (p. 284)

> **Characteristic equation:** "A nontrivial solution exists only when the coefficient determinant in (7.68) vanishes. Hence, we have $|A - \lambda I| = 0$. This equation, called the *characteristic equation* of the matrix $A$, is a polynomial equation of degree $n$ in $\lambda$, the polynomial being called the *characteristic-polynomial* of $A$." — Jain, §7.7 (p. 284)

> **Spectrum and spectral radius:** "The set of all eigenvalues, $\lambda_i$, of a matrix $A$ is called the *spectrum* of $A$ and the largest of $|\lambda_i|$ is called the *spectral radius* of $A$." — Jain, §7.7 (p. 284)

> **Why it matters:** "The eigenvalues of a matrix are of great importance in many engineering problems. For example, problems concerning the stability of an aircraft and those on vibrations of a beam require the computation of eigenvalues of a matrix." — Jain, §7.1

> **When the direct method fails:** "The eigenvalues are obtained by solving the algebraic Eq. (7.69). This method ... is unsuitable for matrices of higher order and better methods must be applied." — Jain, §7.7 (p. 284)

---

## The Procedure

**Step 1. Form $A - \lambda I$.** Subtract $\lambda$ from each diagonal entry. The off-diagonal entries stay as they are.

**Step 2. Write the characteristic equation** $\det(A - \lambda I) = 0$ and solve it. For an $n \times n$ matrix it is a polynomial of degree $n$ in $\lambda$.

**Step 3. For each root $\lambda_i$, solve $(A - \lambda I)X = 0$.** This is a homogeneous system. It always has the trivial solution $X = 0$, which is useless. What you want is a nontrivial solution, and one component is free, so set that one to something convenient (usually $1$) and solve for the rest.

**Step 4. Normalise if asked.** Divide by $\sqrt{x_1^2 + x_2^2 + x_3^2}$ so the vector has unit length.

**Two free checks that need no eigenvector information:**

| Check | Statement |
| :--- | :--- |
| Trace | $\lambda_1 + \lambda_2 + \cdots + \lambda_n = \operatorname{tr} A = \sum a_{ii}$ |
| Determinant | $\lambda_1 \lambda_2 \cdots \lambda_n = \det A$ |

Both are computed from the matrix alone, so a slip in expanding the determinant breaks one of them immediately.

---

## Worked Example (PYQ 2017, 2023): The 3×3 Matrix

> **Source:** 2017 Q.7(b), 2023 Q.3(a) [Marks: 06]

**Question.** Find the eigen-values and eigen-vectors of the following matrix, $A = \begin{bmatrix} 5 & 0 & 1 \\ 0 & -2 & 0 \\ 1 & 0 & 5 \end{bmatrix}$.

**Step 1, the characteristic polynomial.** Form $A - \lambda I$:

$$
A - \lambda I = \begin{bmatrix} 5-\lambda & 0 & 1 \\ 0 & -2-\lambda & 0 \\ 1 & 0 & 5-\lambda \end{bmatrix}
$$

**Step 2, take the determinant along the sparse row.** The second row has only one non-zero entry, so expanding along it costs nothing:

$$
\det(A - \lambda I) = (-2-\lambda)\left[(5-\lambda)^2 - 1\right]
$$

$$
= (-2-\lambda)(25 - 10\lambda + \lambda^2 - 1) = (-2-\lambda)(\lambda^2 - 10\lambda + 24)
$$

$$
= (-2-\lambda)(\lambda - 4)(\lambda - 6)
$$

> [!NOTE] Why this matrix is worth choosing
> It is *almost* reducible. Row 2 and column 2 are decoupled from everything else, so the middle eigenvalue $-2$ comes straight off the sparse row and the remaining $2\times2$ block $\begin{bmatrix} 5 & 1 \\ 1 & 5\end{bmatrix}$ gives the pair $4$ and $6$. On an arbitrary matrix you would be stuck with a cubic; here the structure is visible in the determinant itself, which is why the expansion above is two lines instead of a page.

**The eigenvalues.** Setting the determinant to zero:

$$
\lambda = -2, \qquad \lambda = 4, \qquad \lambda = 6
$$

$$
\boxed{\lambda = -2,\ 4,\ 6}
$$

**The eigenvectors.** For each eigenvalue, solve $(A - \lambda I)v = 0$.

**For $\lambda = -2$.** The matrix becomes $\begin{bmatrix} 7 & 0 & 1 \\ 0 & 0 & 0 \\ 1 & 0 & 7 \end{bmatrix}$. Rows 1 and 3 both give $7x + z = 0$, so $z = -7x$, and row 2 leaves $y$ free. Taking $y$ free and $x = 0$ gives the simplest solution:

$$
v_{-2} = \begin{bmatrix} 0 \\ 1 \\ 0 \end{bmatrix}
$$

(Any multiple of this is also an eigenvector.)

**For $\lambda = 4$.** The matrix becomes $\begin{bmatrix} 1 & 0 & 1 \\ 0 & -6 & 0 \\ 1 & 0 & 1 \end{bmatrix}$. Row 1 gives $x + z = 0$, so $z = -x$, and row 2 forces $y = 0$:

$$
v_4 = \begin{bmatrix} -1 \\ 0 \\ 1 \end{bmatrix}
$$

**For $\lambda = 6$.** The matrix becomes $\begin{bmatrix} -1 & 0 & 1 \\ 0 & -8 & 0 \\ 1 & 0 & -1 \end{bmatrix}$. Row 1 gives $-x + z = 0$, so $z = x$, with $y = 0$ again:

$$
v_6 = \begin{bmatrix} 1 \\ 0 \\ 1 \end{bmatrix}
$$

**Normalised eigenvectors**, for completeness:

$$
\hat v_{-2} = \begin{bmatrix} 0 \\ 1 \\ 0 \end{bmatrix}, \qquad \hat v_4 = \begin{bmatrix} -1/\sqrt{2} \\ 0 \\ 1/\sqrt{2} \end{bmatrix}, \qquad \hat v_6 = \begin{bmatrix} 1/\sqrt{2} \\ 0 \\ 1/\sqrt{2} \end{bmatrix}
$$

**Orthogonality.** The matrix is symmetric, so its eigenvectors for distinct eigenvalues are orthogonal:

$$
v_{-2}^{\mathsf T}v_4 = 0, \qquad v_{-2}^{\mathsf T}v_6 = 0, \qquad v_4^{\mathsf T}v_6 = -1 + 1 = 0
$$

> [!INFO] Check by direct multiplication and by the trace
> Multiplying out: $A(0,1,0)^{\mathsf T} = (0, -2, 0)^{\mathsf T} = -2(0,1,0)^{\mathsf T}$ ✓;
> $A(-1,0,1)^{\mathsf T} = (4, 0, 4)^{\mathsf T} = 4(-1,0,1)^{\mathsf T}$ ✓;
> $A(1,0,1)^{\mathsf T} = (6, 0, 6)^{\mathsf T} = 6(1,0,1)^{\mathsf T}$ ✓. Every eigenvector is verified directly.
>
> Then two scalar checks on the eigenvalues. Their **sum** must equal the trace: $-2 + 4 + 6 = 8$ against $\operatorname{tr}A = 5 + (-2) + 5 = 8$ ✓. Their **product** must equal the determinant: $(-2)(4)(6) = -48$ against
> $$
> \det A = 5\left[(-2)(5) - 0\right] - 0 + 1\left[0 - (-2)(1)\right] = -50 + 2 = -48
> $$
> ✓.

---

## 🏆 Golden Questions (Past Exam Archive)

### 🎯 Find the eigen-values and eigen-vectors of the following matrix, $A = \begin{bmatrix} 5 & 0 & 1 \\ 0 & -2 & 0 \\ 1 & 0 & 5 \end{bmatrix}$.
> **Appeared:** 2017 Q.7(b), 2023 Q.3(a) — (06 marks)

**Full Answer:**

**The characteristic polynomial.** Form $A - \lambda I$:

$$
A - \lambda I = \begin{bmatrix} 5-\lambda & 0 & 1 \\ 0 & -2-\lambda & 0 \\ 1 & 0 & 5-\lambda \end{bmatrix}
$$

Taking the determinant along the second row, which has only one non-zero entry:

$$
\det(A - \lambda I) = (-2-\lambda)\left[(5-\lambda)^2 - 1\right]
$$

$$
= (-2-\lambda)(25 - 10\lambda + \lambda^2 - 1) = (-2-\lambda)(\lambda^2 - 10\lambda + 24)
$$

$$
= (-2-\lambda)(\lambda - 4)(\lambda - 6)
$$

**The eigenvalues.** Setting the determinant to zero:

$$
\lambda = -2, \qquad \lambda = 4, \qquad \lambda = 6
$$

$$
\boxed{\lambda = -2,\ 4,\ 6}
$$

**The eigenvectors.** For each eigenvalue, solve $(A - \lambda I)v = 0$.

**For $\lambda = -2$.** The matrix becomes $\begin{bmatrix} 7 & 0 & 1 \\ 0 & 0 & 0 \\ 1 & 0 & 7 \end{bmatrix}$, and the first and third rows give $7x + z = 0$, so $z = -7x$ with $y$ free. Taking $y$ free and $x = 0$ gives the simplest solution:

$$
v_{-2} = \begin{bmatrix} 0 \\ 1 \\ 0 \end{bmatrix}
$$

**For $\lambda = 4$.** The matrix becomes $\begin{bmatrix} 1 & 0 & 1 \\ 0 & -6 & 0 \\ 1 & 0 & 1 \end{bmatrix}$, and the first row gives $x + z = 0$, so $z = -x$, with the second row forcing $y = 0$:

$$
v_4 = \begin{bmatrix} -1 \\ 0 \\ 1 \end{bmatrix}
$$

**For $\lambda = 6$.** The matrix becomes $\begin{bmatrix} -1 & 0 & 1 \\ 0 & -8 & 0 \\ 1 & 0 & -1 \end{bmatrix}$, and the first row gives $-x + z = 0$, so $z = x$, with $y = 0$ again:

$$
v_6 = \begin{bmatrix} 1 \\ 0 \\ 1 \end{bmatrix}
$$

**Normalised eigenvectors**, for completeness:

$$
\hat v_{-2} = \begin{bmatrix} 0 \\ 1 \\ 0 \end{bmatrix}, \qquad \hat v_4 = \begin{bmatrix} -1/\sqrt{2} \\ 0 \\ 1/\sqrt{2} \end{bmatrix}, \qquad \hat v_6 = \begin{bmatrix} 1/\sqrt{2} \\ 0 \\ 1/\sqrt{2} \end{bmatrix}
$$

**Orthogonality.** The matrix is symmetric, so its eigenvectors for distinct eigenvalues are orthogonal:

$$
v_{-2}^{\mathsf T}v_4 = 0, \qquad v_{-2}^{\mathsf T}v_6 = 0, \qquad v_4^{\mathsf T}v_6 = -1 + 1 = 0
$$

> [!INFO] Check by direct multiplication and by the trace
> $A(0,1,0)^{\mathsf T} = (0, -2, 0)^{\mathsf T} = -2(0,1,0)^{\mathsf T}$ ✓;
> $A(-1,0,1)^{\mathsf T} = (4, 0, 4)^{\mathsf T} = 4(-1,0,1)^{\mathsf T}$ ✓;
> $A(1,0,1)^{\mathsf T} = (6, 0, 6)^{\mathsf T} = 6(1,0,1)^{\mathsf T}$ ✓.
>
> Their **sum** must equal the trace: $-2 + 4 + 6 = 8$ against $\operatorname{tr}A = 8$ ✓. Their **product** must equal the determinant: $(-2)(4)(6) = -48$ against $\det A = -50 + 2 = -48$ ✓. A slip in expanding the determinant breaks one of them immediately.

---

### 🎯 Determine the largest eigenvalue and the corresponding eigenvector of $A = \begin{bmatrix} 1 & 6 & 1 \\ 1 & 2 & 0 \\ 0 & 0 & 3 \end{bmatrix}$ by the power (iterative) method.
> **Source:** Jain §7.7, Example 7.16 (pp. 286–287) — background for the eigenvalue definition

**Full Answer:**

When only the largest eigenvalue is needed, the direct characteristic-polynomial route is wasteful. The power method multiplies repeatedly and lets the dominant direction dominate.

Start with an arbitrary vector, here $X^{(0)} = \begin{bmatrix} 1 \\ 0 \\ 0 \end{bmatrix}$:

$$
AX^{(0)} = \begin{bmatrix} 1 & 6 & 1 \\ 1 & 2 & 0 \\ 0 & 0 & 3 \end{bmatrix} \begin{bmatrix} 1 \\ 0 \\ 0 \end{bmatrix} = \begin{bmatrix} 1 \\ 1 \\ 0 \end{bmatrix} = X^{(1)}
$$

So an approximate eigenvalue is $1$ and an approximate eigenvector is $X^{(1)}$.

$$
AX^{(1)} = \begin{bmatrix} 1 & 6 & 1 \\ 1 & 2 & 0 \\ 0 & 0 & 3 \end{bmatrix} \begin{bmatrix} 1 \\ 1 \\ 0 \end{bmatrix} = \begin{bmatrix} 7 \\ 3 \\ 0 \end{bmatrix} = 3 \begin{bmatrix} 2.3 \\ 1 \\ 0 \end{bmatrix}
$$

So $X^{(2)} = \begin{bmatrix} 2.3 \\ 1 \\ 0 \end{bmatrix}$ and an approximate eigenvalue is $3$.

Repeating, the successive vectors settle:

$$
4 \begin{bmatrix} 2.1 \\ 1.1 \\ 0 \end{bmatrix}; \quad 4 \begin{bmatrix} 2.2 \\ 1.1 \\ 0 \end{bmatrix}; \quad 4.4 \begin{bmatrix} 2 \\ 1 \\ 0 \end{bmatrix}; \quad 4 \begin{bmatrix} 2 \\ 1 \\ 0 \end{bmatrix}; \quad 4 \begin{bmatrix} 2 \\ 1 \\ 0 \end{bmatrix}
$$

It follows that the largest eigenvalue is $4$ and the corresponding eigenvector is $\begin{bmatrix} 2 \\ 1 \\ 0 \end{bmatrix}$.

> [!NOTE] Why the method works, and when it does not
> Repeated multiplication projects the start vector onto the dominant eigenvector. The eigenvalue factor in front of each vector is the running estimate of the largest eigenvalue.
>
> It fails when the two largest eigenvalues have the **same modulus**, for example $5$ and $-5$. Then the signs alternate and the estimate never settles. It is the textbook method for a single dominant eigenvalue, which is the common case.

---

## Exam Variants

| Year | Question | Matrix | Key Answer |
| :--- | :--- | :--- | :--- |
| 2017 Q.7(b) | Eigenvalues and eigenvectors of a $3\times3$ | $\begin{bmatrix} 5&0&1\\0&-2&0\\1&0&5\end{bmatrix}$ | $\boxed{\lambda = -2,\ 4,\ 6}$ with $v_{-2}=(0,1,0)^{\mathsf T}$, $v_4=(-1,0,1)^{\mathsf T}$, $v_6=(1,0,1)^{\mathsf T}$ |
| 2023 Q.3(a) | Same matrix, same answer | identical | identical |

---

## ⚡ Exam Tips & Common Mistakes

1. **Subtract $\lambda$ from the diagonal only.** Off-diagonal entries stay unchanged. Writing $A + \lambda I$ gives the same roots but many students mix the two conventions mid-expansion.
2. **Expand along the sparsest row or column.** In this matrix row 2 has one non-zero entry, so the determinant is two lines. Expanding any other way invites algebra errors.
3. **$x = 0, y = 0, z = 0$ is not the answer.** The homogeneous system always has the trivial solution. Look for the row that reduces to $0 = 0$ and use it as the freedom in the solution.
4. **Set the free component to a simple number.** Usually $1$ or $0$. Do not leave the eigenvector in terms of an arbitrary constant unless the question asks for it.
5. **Check with the trace and the determinant.** Sum of eigenvalues equals the trace. Product equals $\det A$. Both are free and both catch a sign error.
6. **Sign convention on the eigenvector is arbitrary.** $\begin{bmatrix} -1 \\ 0 \\ 1\end{bmatrix}$ and $\begin{bmatrix} 1 \\ 0 \\ -1\end{bmatrix}$ are the same eigenvector. Do not be thrown when the textbook picks the opposite sign.

## 🔗 Related Topics

- [NM-3 Lower: Gauss Elimination, LU, Jacobi](NM-3_Lower_Gauss_Elim_LU_Jacobi_Relaxation.md) — matrix algebra and determinants used here
- [NM-10: Partial Differential Equations](NM-10_Partial_Differential_Equations.md) — next in the chain, where the spectral radius governs stability

---

[← Previous: NM-8 Lower — IVP, BVP, Heun, RK2](NM-8_Lower_IVP_BVP_Heun_RK2_Higher.md) | [🏠 Index](00_Index.md) | [Next: NM-10 Partial Differential Equations →](NM-10_Partial_Differential_Equations.md)