[← Previous: NM-8.8 Boundary Value Problems](../NM-8_ODE/NM-8.8_Boundary_Value_Problems.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: NM-10.1 PDE Classification & Theory →](../NM-10_PDE/NM-10.1_Classification.md)

---

# NM-9.1: Eigenvalues and Eigenvectors

> 🟡 **Priority:** Light | **Tested:** 2/8 years (2017, 2023) | **Typical marks:** 5--6

## What This Is (and Why It Matters)

Whenever you multiply a matrix $A$ by an ordinary vector $\mathbf{x}$, the matrix normally does two things at once: it rotates the vector into a brand-new direction, and it alters its length.

However, almost every square matrix possesses a few special, privileged directions. When matrix $A$ multiplies a vector lying along one of these directions, it does not rotate the vector at all. The vector stays on its exact same directional line, and the matrix merely stretches, shrinks, or flips it by a constant numerical scaling factor $\lambda$:

$$
A\mathbf{x} = \lambda\mathbf{x}
$$

Those invariant directional vectors are called **eigenvectors**, and the corresponding scaling numbers $\lambda$ are called **eigenvalues**.

In electrical and computer engineering, eigenvalues are everywhere:
- In linear circuit networks (like multi-stage LC filters), eigenvalues represent the natural resonance frequencies of the system.
- In control engineering, the real parts of eigenvalues decide whether an amplifier circuit is stable or about to blow up in uncontrolled oscillations.
- In numerical computing, the largest eigenvalue (the spectral radius) determines whether iterative equation solvers like Gauss-Seidel converge or diverge.

In the RUET semester final, this is the easiest high-mark question in Section A. The exam has tested eigenvalues twice (in 2017 and 2023). Both times, the examiners set the exact same $3 \times 3$ symmetric matrix straight out of Jain's textbook (Example 7.15). Master this one problem, and you have locked down 5 to 6 marks.

---

## 📝 Key Definitions

> **Eigenvalue and Eigenvector:** "Let $A$ be a square matrix of order $n$ with elements $a_{ij}$. We wish to find a column vector $X$ and a constant $\lambda$ such that $AX = \lambda X$. In Eq. (7.67), $\lambda$ is called the *eigenvalue* and $X$ is called the corresponding *eigenvector*." -- Jain, §7.7 (p. 284)
>
> **In simple words:** An eigenvector is a special vector whose direction does not budge when multiplied by matrix $A$. The eigenvalue $\lambda$ is the scaling factor telling you how much the vector gets stretched or compressed.

> **Characteristic Equation:** "A nontrivial solution exists only when the coefficient determinant in (7.68) vanishes. Hence, we have $|A - \lambda I| = 0$. This equation, called the *characteristic equation* of the matrix $A$, is a polynomial equation of degree $n$ in $\lambda$, the polynomial being called the *characteristic-polynomial* of $A$." -- Jain, §7.7 (p. 284)
>
> **In simple words:** Setting the determinant of $(A - \lambda I)$ equal to zero turns the matrix equation into a standard algebraic polynomial whose roots are the eigenvalues.

> **Spectrum and Spectral Radius:** "The set of all eigenvalues, $\lambda_i$, of a matrix $A$ is called the *spectrum* of $A$ and the largest of $|\lambda_i|$ is called the *spectral radius* of $A$." -- Jain, §7.7 (p. 284)
>
> **In simple words:** The spectrum is the complete list of all eigenvalues belonging to the matrix. The spectral radius is simply the absolute magnitude of the single biggest eigenvalue on that list.

> **Physical Significance in Engineering:** "The eigenvalues of a matrix are of great importance in many engineering problems. For example, problems concerning the stability of an aircraft and those on vibrations of a beam require the computation of eigenvalues of a matrix." -- Jain, §7.1 (p. 256)
>
> **In simple words:** Eigenvalues reveal the fundamental natural frequencies and stability boundaries of physical systems, from vibrating transmission towers to power grid stability.

> **Normalized Eigenvector:** An eigenvector $\hat{\mathbf{v}}$ scaled so that its Euclidean length is exactly 1, meaning $\|\hat{\mathbf{v}}\| = \sqrt{v_1^2 + v_2^2 + \dots + v_n^2} = 1$. -- Jain, §7.7 (p. 286)
>
> **In simple words:** Dividing an eigenvector by its total length so that it points in the exact same direction but has a length of exactly one unit.

> **Iterative Power Method:** An iterative numerical technique that repeatedly multiplies an initial trial vector by matrix $A$ to isolate the numerically largest (dominant) eigenvalue and its corresponding eigenvector without solving the characteristic polynomial. -- Jain, §7.7 (pp. 284, 286)
>
> **In simple words:** A method where you keep hitting an arbitrary vector with the matrix over and over until the vector naturally lines up with the strongest eigenvalue direction.

---

## The Core Idea

Suppose you are given an $n \times n$ matrix $A$. You want to find non-zero vectors $\mathbf{x}$ and scalars $\lambda$ satisfying:

$$
A\mathbf{x} = \lambda\mathbf{x}
$$

Rewrite this by introducing the identity matrix $I$:

$$
(A - \lambda I)\mathbf{x} = \mathbf{0}
$$

This is a homogeneous system of linear equations. If the matrix $(A - \lambda I)$ had an inverse, you could multiply both sides by $(A - \lambda I)^{-1}$ to get $\mathbf{x} = \mathbf{0}$. But the zero vector $\mathbf{x} = \mathbf{0}$ is the trivial solution, which is completely useless.

For a non-trivial (non-zero) solution $\mathbf{x}$ to exist, the matrix $(A - \lambda I)$ must be singular. That means its determinant must equal zero:

$$
\det(A - \lambda I) = 0
$$

### Step-by-Step Procedure for a $3 \times 3$ Matrix

1. **Form the matrix $A - \lambda I$:** Subtract $\lambda$ from each element on the main diagonal. Leave every off-diagonal element completely untouched.
2. **Compute the determinant $\det(A - \lambda I) = 0$:** Look for a row or column with lots of zeros (sparse row/column) and expand along it. This avoids messy cubic algebra and factors the polynomial cleanly.
3. **Solve for the eigenvalues $\lambda_1, \lambda_2, \lambda_3$:** Set the factored characteristic polynomial to zero and record all roots.
4. **Find the eigenvector for each $\lambda_i$:** Plug $\lambda_i$ back into $(A - \lambda_i I)\mathbf{v} = \mathbf{0}$. Set one free variable to a convenient non-zero number (like $1$) and solve for the remaining variables.
5. **Normalize the eigenvectors:** Divide each eigenvector $\mathbf{v}$ by its length $\sqrt{v_1^2 + v_2^2 + v_3^2}$ to produce the unit eigenvector $\hat{\mathbf{v}}$.

### Two Free Sanity Checks

You can verify your calculated eigenvalues instantly without looking at the eigenvectors:

| Check Name | Formula | Why It Works |
|:---|:---|:---|
| **Trace Check** | $\lambda_1 + \lambda_2 + \lambda_3 = \operatorname{tr}(A) = \sum a_{ii}$ | The sum of all eigenvalues must equal the sum of the main diagonal entries of $A$. |
| **Determinant Check** | $\lambda_1 \cdot \lambda_2 \cdot \lambda_3 = \det(A)$ | The product of all eigenvalues must equal the determinant of the original matrix $A$. |

Because the trace and determinant are computed directly from the original matrix $A$, a sign error or arithmetic slip in your characteristic equation will fail these tests immediately!

### Orthogonality Property for Symmetric Matrices

A matrix is symmetric if $A = A^T$. A fundamental theorem of linear algebra states that:
- All eigenvalues of a real symmetric matrix are real numbers.
- Eigenvectors corresponding to distinct eigenvalues of a real symmetric matrix are **mutually orthogonal**:

$$
\mathbf{v}_i^T \mathbf{v}_j = 0 \quad (\text{for } \lambda_i \neq \lambda_j)
$$

Taking the dot product of your eigenvectors serves as a third rock-solid verification.

### When Does the Direct Method Fail?

For $2 \times 2$ and $3 \times 3$ matrices, finding roots of the characteristic polynomial with pencil and paper is easy. But for larger matrices ($n \ge 4$ or $n \ge 5$):
- Expanding determinants becomes computationally expensive ($O(n!)$ without reduction).
- Finding polynomial roots algebraically is impossible in general (by the Abel-Ruffini theorem).
- Small rounding errors in polynomial coefficients lead to massive errors in calculated roots (Wilkinson's phenomenon).

In practical engineering software, we use **iterative methods**:
- **Power Method:** To find the single largest (dominant) eigenvalue.
- **Householder's Method:** To reduce symmetric matrices to tridiagonal form.
- **QR Algorithm:** The gold-standard modern algorithm to extract all eigenvalues simultaneously.

> [!WARNING] Common Traps to Avoid
> 1. **Subtracting $\lambda$ from off-diagonal entries:** Remember, $I$ only has ones on the diagonal. Never subtract $\lambda$ from non-diagonal terms.
> 2. **Giving $\mathbf{v} = \mathbf{0}$ as an answer:** The zero vector is never an eigenvector. By definition, eigenvectors must be non-zero.
> 3. **Expanding the determinant along a dense row:** Always scan the matrix first! If row 2 has zeros, expand along row 2. It will turn two pages of algebra into two lines.
> 4. **Panic over eigenvector signs:** Any non-zero scalar multiple of an eigenvector is also an eigenvector. $\begin{bmatrix} 1 \\ 0 \\ 1 \end{bmatrix}$ and $\begin{bmatrix} -1 \\ 0 \\ -1 \end{bmatrix}$ represent the exact same line in 3D space.

---

## 🔧 Worked Example

> **From:** 2017 Q.7(b) [Marks: 06], repeated in 2023 Q.3(a) [Marks: 05, CLO2]

**The question:** Find the eigen-values and eigen-vectors of the following matrix, 

$$
A = \begin{bmatrix} 5 & 0 & 1 \\ 0 & -2 & 0 \\ 1 & 0 & 5 \end{bmatrix}
$$

**Let's solve this step by step.**

### Step 1: Form the characteristic matrix $(A - \lambda I)$

Subtract $\lambda$ from each diagonal entry of $A$:

$$
A - \lambda I = \begin{bmatrix} 5-\lambda & 0 & 1 \\ 0 & -2-\lambda & 0 \\ 1 & 0 & 5-\lambda \end{bmatrix}
$$

### Step 2: Set the determinant to zero along the sparse row

Look closely at the second row: it has zeros at positions $(2,1)$ and $(2,3)$, with only the center entry $(-2-\lambda)$ non-zero. Expanding along row 2 costs almost zero effort:

$$
\det(A - \lambda I) = (-2-\lambda) \begin{vmatrix} 5-\lambda & 1 \\ 1 & 5-\lambda \end{vmatrix} = 0
$$

Evaluate the $2 \times 2$ determinant:

$$
\begin{vmatrix} 5-\lambda & 1 \\ 1 & 5-\lambda \end{vmatrix} = (5-\lambda)^2 - (1)(1) = (5-\lambda)^2 - 1
$$

Factor using the difference of squares $a^2 - b^2 = (a-b)(a+b)$:

$$
(5-\lambda)^2 - 1 = [(5-\lambda) - 1][(5-\lambda) + 1] = (4-\lambda)(6-\lambda)
$$

So the complete factored characteristic equation is:

$$
(-2-\lambda)(4-\lambda)(6-\lambda) = 0
$$

Or alternatively, expanding out:

$$
(-2-\lambda)(\lambda^2 - 10\lambda + 24) = 0
$$

### Step 3: Extract the eigenvalues

Setting each factor to zero gives:

$$
\lambda = -2, \qquad \lambda = 4, \qquad \lambda = 6
$$

$$
\boxed{\lambda = -2,\ 4,\ 6}
$$

### Step 4: Find the eigenvector for $\lambda = -2$

Substitute $\lambda = -2$ into $(A - \lambda I)\mathbf{v} = \mathbf{0}$:

$$
(A + 2I)\mathbf{v} = \begin{bmatrix} 5 - (-2) & 0 & 1 \\ 0 & -2 - (-2) & 0 \\ 1 & 0 & 5 - (-2) \end{bmatrix} \begin{bmatrix} x \\ y \\ z \end{bmatrix} = \begin{bmatrix} 7 & 0 & 1 \\ 0 & 0 & 0 \\ 1 & 0 & 7 \end{bmatrix} \begin{bmatrix} x \\ y \\ z \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \\ 0 \end{bmatrix}
$$

Write out the linear equations:
- Row 1: $7x + z = 0 \implies z = -7x$
- Row 3: $x + 7z = 0 \implies x + 7(-7x) = -48x = 0 \implies x = 0$
- Since $x = 0$, we have $z = 0$.
- Row 2: $0x + 0y + 0z = 0$, which places zero constraints on $y$. So $y$ is completely free!

Pick the simplest non-zero value, $y = 1$:

$$
\mathbf{v}_{-2} = \begin{bmatrix} 0 \\ 1 \\ 0 \end{bmatrix}
$$

Its length is $\sqrt{0^2 + 1^2 + 0^2} = 1$, so it is already normalized:

$$
\hat{\mathbf{v}}_{-2} = \begin{bmatrix} 0 \\ 1 \\ 0 \end{bmatrix}
$$

### Step 5: Find the eigenvector for $\lambda = 4$

Substitute $\lambda = 4$ into $(A - 4I)\mathbf{v} = \mathbf{0}$:

$$
(A - 4I)\mathbf{v} = \begin{bmatrix} 5-4 & 0 & 1 \\ 0 & -2-4 & 0 \\ 1 & 0 & 5-4 \end{bmatrix} \begin{bmatrix} x \\ y \\ z \end{bmatrix} = \begin{bmatrix} 1 & 0 & 1 \\ 0 & -6 & 0 \\ 1 & 0 & 1 \end{bmatrix} \begin{bmatrix} x \\ y \\ z \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \\ 0 \end{bmatrix}
$$

Write out the equations:
- Row 2: $-6y = 0 \implies y = 0$
- Row 1: $x + z = 0 \implies z = -x$
- Row 3: $x + z = 0$ (redundant, confirms $z = -x$)

Choose $x = -1$ (or $x = 1$):
- If $x = -1$, then $z = -(-1) = 1$.

$$
\mathbf{v}_4 = \begin{bmatrix} -1 \\ 0 \\ 1 \end{bmatrix}
$$

Calculate its Euclidean length:

$$
\|\mathbf{v}_4\| = \sqrt{(-1)^2 + 0^2 + 1^2} = \sqrt{2}
$$

Normalize by dividing by $\sqrt{2}$:

$$
\hat{\mathbf{v}}_4 = \begin{bmatrix} -1/\sqrt{2} \\ 0 \\ 1/\sqrt{2} \end{bmatrix}
$$

### Step 6: Find the eigenvector for $\lambda = 6$

Substitute $\lambda = 6$ into $(A - 6I)\mathbf{v} = \mathbf{0}$:

$$
(A - 6I)\mathbf{v} = \begin{bmatrix} 5-6 & 0 & 1 \\ 0 & -2-6 & 0 \\ 1 & 0 & 5-6 \end{bmatrix} \begin{bmatrix} x \\ y \\ z \end{bmatrix} = \begin{bmatrix} -1 & 0 & 1 \\ 0 & -8 & 0 \\ 1 & 0 & -1 \end{bmatrix} \begin{bmatrix} x \\ y \\ z \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \\ 0 \end{bmatrix}
$$

Write out the equations:
- Row 2: $-8y = 0 \implies y = 0$
- Row 1: $-x + z = 0 \implies z = x$
- Row 3: $x - z = 0 \implies z = x$ (redundant)

Choose $x = 1$:
- Then $z = 1$.

$$
\mathbf{v}_6 = \begin{bmatrix} 1 \\ 0 \\ 1 \end{bmatrix}
$$

Calculate its Euclidean length:

$$
\|\mathbf{v}_6\| = \sqrt{1^2 + 0^2 + 1^2} = \sqrt{2}
$$

Normalize by dividing by $\sqrt{2}$:

$$
\hat{\mathbf{v}}_6 = \begin{bmatrix} 1/\sqrt{2} \\ 0 \\ 1/\sqrt{2} \end{bmatrix}
$$

### Step 7: Sanity checks

Let's run our quick verification checks:

1. **Direct multiplication check ($A\mathbf{v} = \lambda\mathbf{v}$):**
   - For $\lambda = -2$:
$$
A\mathbf{v}_{-2} = \begin{bmatrix} 5 & 0 & 1 \\ 0 & -2 & 0 \\ 1 & 0 & 5 \end{bmatrix} \begin{bmatrix} 0 \\ 1 \\ 0 \end{bmatrix} = \begin{bmatrix} 0 \\ -2 \\ 0 \end{bmatrix} = -2 \begin{bmatrix} 0 \\ 1 \\ 0 \end{bmatrix} \quad \checkmark
$$
   - For $\lambda = 4$:
$$
A\mathbf{v}_4 = \begin{bmatrix} 5 & 0 & 1 \\ 0 & -2 & 0 \\ 1 & 0 & 5 \end{bmatrix} \begin{bmatrix} -1 \\ 0 \\ 1 \end{bmatrix} = \begin{bmatrix} -4 \\ 0 \\ 4 \end{bmatrix} = 4 \begin{bmatrix} -1 \\ 0 \\ 1 \end{bmatrix} \quad \checkmark
$$
   - For $\lambda = 6$:
$$
A\mathbf{v}_6 = \begin{bmatrix} 5 & 0 & 1 \\ 0 & -2 & 0 \\ 1 & 0 & 5 \end{bmatrix} \begin{bmatrix} 1 \\ 0 \\ 1 \end{bmatrix} = \begin{bmatrix} 6 \\ 0 \\ 6 \end{bmatrix} = 6 \begin{bmatrix} 1 \\ 0 \\ 1 \end{bmatrix} \quad \checkmark
$$

2. **Trace check:**
$$
\lambda_1 + \lambda_2 + \lambda_3 = -2 + 4 + 6 = 8
$$
$$
\operatorname{tr}(A) = 5 + (-2) + 5 = 8 \quad \checkmark
$$

3. **Determinant check:**
$$
\lambda_1 \cdot \lambda_2 \cdot \lambda_3 = (-2)(4)(6) = -48
$$
$$
\det(A) = 5\left[(-2)(5) - 0\right] - 0 + 1\left[0 - (-2)(1)\right] = 5(-10) + 2 = -48 \quad \checkmark
$$

4. **Orthogonality check:**
   Since $A$ is symmetric, eigenvectors for distinct eigenvalues must have zero dot product:
$$
\mathbf{v}_{-2}^T \mathbf{v}_4 = (0)(-1) + (1)(0) + (0)(1) = 0 \quad \checkmark
$$
$$
\mathbf{v}_{-2}^T \mathbf{v}_6 = (0)(1) + (1)(0) + (0)(1) = 0 \quad \checkmark
$$
$$
\mathbf{v}_4^T \mathbf{v}_6 = (-1)(1) + (0)(0) + (1)(1) = -1 + 1 = 0 \quad \checkmark
$$

Every single check passes with 100% precision.

---

## 🏆 Past Exam Questions

### 2017 Q.7(b) & 2023 Q.3(a): Symmetric $3 \times 3$ Matrix

> **Appeared in:** 2017 Q.7(b) [Marks: 06], 2023 Q.3(a) [Marks: 05, CLO2]

**Question.** Find the eigen-values and eigen-vectors of the following matrix, 

$$
A = \begin{bmatrix} 5 & 0 & 1 \\ 0 & -2 & 0 \\ 1 & 0 & 5 \end{bmatrix}
$$

**Full Solution.**

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

**The eigenvectors.** For each eigenvalue, solve $(A - \lambda I)\mathbf{v} = \mathbf{0}$.

**For $\lambda = -2$.** The matrix becomes
$\begin{bmatrix} 7 & 0 & 1 \\ 0 & 0 & 0 \\ 1 & 0 & 7 \end{bmatrix}$, and the first
and third rows give $7x + z = 0$, so $z = -7x$ with $y$ free. Taking $y$ free
and $x = 0$ gives the simplest solution:

$$
v_{-2} = \begin{bmatrix} 0 \\ 1 \\ 0 \end{bmatrix}
$$

(Any multiple of this is also an eigenvector.)

**For $\lambda = 4$.** The matrix becomes
$\begin{bmatrix} 1 & 0 & 1 \\ 0 & -6 & 0 \\ 1 & 0 & 1 \end{bmatrix}$, and the first
row gives $x + z = 0$, so $z = -x$, with the second row forcing $y = 0$:

$$
v_4 = \begin{bmatrix} -1 \\ 0 \\ 1 \end{bmatrix}
$$

**For $\lambda = 6$.** The matrix becomes
$\begin{bmatrix} -1 & 0 & 1 \\ 0 & -8 & 0 \\ 1 & 0 & -1 \end{bmatrix}$, and the first
row gives $-x + z = 0$, so $z = x$, with $y = 0$ again:

$$
v_6 = \begin{bmatrix} 1 \\ 0 \\ 1 \end{bmatrix}
$$

**Normalised eigenvectors**, for completeness:

$$
\hat v_{-2} = \begin{bmatrix} 0 \\ 1 \\ 0 \end{bmatrix}, \qquad \hat v_4 = \begin{bmatrix} -1/\sqrt{2} \\ 0 \\ 1/\sqrt{2} \end{bmatrix}, \qquad \hat v_6 = \begin{bmatrix} 1/\sqrt{2} \\ 0 \\ 1/\sqrt{2} \end{bmatrix}
$$

**Orthogonality.** The matrix is symmetric, so its eigenvectors for distinct
eigenvalues are orthogonal:

$$
v_{-2}^{\mathsf T}v_4 = 0, \qquad v_{-2}^{\mathsf T}v_6 = 0, \qquad v_4^{\mathsf T}v_6 = -1 + 1 = 0
$$

> [!INFO] Independent Trace and Determinant Verification
> Multiplying out:
> $A(0,1,0)^{\mathsf T} = (0, -2, 0)^{\mathsf T} = -2(0,1,0)^{\mathsf T}$;
> $A(-1,0,1)^{\mathsf T} = (4, 0, 4)^{\mathsf T} = 4(-1,0,1)^{\mathsf T}$;
> $A(1,0,1)^{\mathsf T} = (6, 0, 6)^{\mathsf T} = 6(1,0,1)^{\mathsf T}$.
> Every eigenvector is verified directly.
>
> As an independent check on the eigenvalues, their sum must equal the trace:
> $-2 + 4 + 6 = 8$, matching $\operatorname{tr}(A) = 5 + (-2) + 5 = 8$.
> Their product must equal the determinant:
> $(-2)(4)(6) = -48$, matching $\det(A) = 5(-10) + 2 = -48$.
> The trace and determinant depend only on matrix $A$, confirming our polynomial roots with zero ambiguity.

---

### Jain §7.7 Example 7.16: Largest Eigenvalue by the Power Method

> **Source:** Jain §7.7, Example 7.16 (pp. 286--287) -- Essential theory background

**Question.** Determine the largest eigenvalue and the corresponding eigenvector of the matrix

$$
A = \begin{bmatrix} 1 & 6 & 1 \\ 1 & 2 & 0 \\ 0 & 0 & 3 \end{bmatrix}
$$

by the power (iterative) method.

**How the Power Method works in simple words:**
When you multiply a trial vector by $A$ repeatedly, the component of the vector pointing along the dominant eigenvector grows faster than all other components. After several iterations, the normalized vector settles directly onto the dominant eigenvector, and the scaling factor between successive steps settles onto the dominant eigenvalue.

**Let's step through the iterations:**

Start with an arbitrary initial vector, say:

$$
X^{(0)} = \begin{bmatrix} 1 \\ 0 \\ 0 \end{bmatrix}
$$

**Iteration 1:** Multiply $A$ by $X^{(0)}$:

$$
A X^{(0)} = \begin{bmatrix} 1 & 6 & 1 \\ 1 & 2 & 0 \\ 0 & 0 & 3 \end{bmatrix} \begin{bmatrix} 1 \\ 0 \\ 0 \end{bmatrix} = \begin{bmatrix} 1 \\ 1 \\ 0 \end{bmatrix} = X^{(1)}
$$

Here our running estimate for the eigenvalue is $1$, with vector estimate $X^{(1)} = \begin{bmatrix} 1 \\ 1 \\ 0 \end{bmatrix}$.

**Iteration 2:** Multiply $A$ by $X^{(1)}$:

$$
A X^{(1)} = \begin{bmatrix} 1 & 6 & 1 \\ 1 & 2 & 0 \\ 0 & 0 & 3 \end{bmatrix} \begin{bmatrix} 1 \\ 1 \\ 0 \end{bmatrix} = \begin{bmatrix} 7 \\ 3 \\ 0 \end{bmatrix} = 3 \begin{bmatrix} 2.33 \\ 1 \\ 0 \end{bmatrix}
$$

Factoring out $3$ gives the updated vector $X^{(2)} = \begin{bmatrix} 2.3 \\ 1 \\ 0 \end{bmatrix}$ with approximate eigenvalue $3$.

**Subsequent Iterations:** Repeating this multiplication and factoring out the largest component:

$$
4 \begin{bmatrix} 2.1 \\ 1.1 \\ 0 \end{bmatrix}; \quad 4 \begin{bmatrix} 2.2 \\ 1.1 \\ 0 \end{bmatrix}; \quad 4.4 \begin{bmatrix} 2 \\ 1 \\ 0 \end{bmatrix}; \quad 4 \begin{bmatrix} 2 \\ 1 \\ 0 \end{bmatrix}; \quad 4 \begin{bmatrix} 2 \\ 1 \\ 0 \end{bmatrix}
$$

The scaling constant settles firmly onto $4$, and the vector stabilizes at $\begin{bmatrix} 2 \\ 1 \\ 0 \end{bmatrix}$.

So the largest eigenvalue is $4$ and the corresponding eigenvector is:

$$
\mathbf{v}_{\text{max}} = \begin{bmatrix} 2 \\ 1 \\ 0 \end{bmatrix}
$$

> [!NOTE] When does the Power Method struggle?
> The power method converges quickly when the dominant eigenvalue $|\lambda_1|$ is strictly larger than all other eigenvalues. It runs into trouble when two eigenvalues share the exact same absolute magnitude with opposite signs (for instance, $\lambda_1 = 5$ and $\lambda_2 = -5$). In that case, the iterates oscillate and fail to converge to a single steady value.

---

### Exam Variants at a Glance

| Year | What They Asked | Given Matrix | Key Answer |
|:---|:---|:---|:---|
| 2017 Q.7(b) | Find eigenvalues & eigenvectors | $\begin{bmatrix} 5 & 0 & 1 \\ 0 & -2 & 0 \\ 1 & 0 & 5 \end{bmatrix}$ | $\boxed{\lambda = -2,\ 4,\ 6}$ with $\mathbf{v}_{-2} = \begin{bmatrix}0\\1\\0\end{bmatrix}, \mathbf{v}_4 = \begin{bmatrix}-1\\0\\1\end{bmatrix}, \mathbf{v}_6 = \begin{bmatrix}1\\0\\1\end{bmatrix}$ |
| 2023 Q.3(a) | Find eigenvalues & eigenvectors (identical problem) | $\begin{bmatrix} 5 & 0 & 1 \\ 0 & -2 & 0 \\ 1 & 0 & 5 \end{bmatrix}$ | $\boxed{\lambda = -2,\ 4,\ 6}$ with identical eigenvectors and normalized unit forms |

---

## ⚡ Quick Review

**The method in one sentence:** Subtract $\lambda$ from the diagonal entries, set the determinant to zero along the row with the most zeros to find the eigenvalues, and then solve the homogeneous system $(A - \lambda I)\mathbf{v} = \mathbf{0}$ for each root.

**The formulas you must memorize:**

1. Characteristic equation:
$$
\det(A - \lambda I) = 0
$$

2. Eigenvector equation:
$$
(A - \lambda I)\mathbf{v} = \mathbf{0}
$$

3. Trace check (instant verification):
$$
\sum_{i=1}^n \lambda_i = \operatorname{tr}(A) = \sum_{i=1}^n a_{ii}
$$

4. Determinant check:
$$
\prod_{i=1}^n \lambda_i = \det(A)
$$

**The most common exam mistake:** Forgetting that row 2 has zeros and grinding through a long 3-by-3 cofactor expansion. Expanding along row 2 immediately factors out $(-2 - \lambda)$ and gives you the roots in two lines.

**Time estimate in exam:** 8 to 10 minutes for full 5 or 6 marks.

---

## 🔗 Connected Topics

- [← NM-8.8: Boundary Value Problems](../NM-8_ODE/NM-8.8_Boundary_Value_Problems.md) -- Finite difference discretization of BVPs leads directly to large tridiagonal matrix systems.
- [NM-3.1: Gauss Elimination](../NM-3_Linear_Systems/NM-3.1_Gauss_Elimination.md) -- Systematic row operations used to solve homogeneous systems and extract nullspaces.
- [→ NM-10.1: PDE Classification & Theory](../NM-10_PDE/NM-10.1_Classification.md) -- In elliptical and parabolic PDEs, the spectral radius of the iteration matrix dictates whether Liebmann's method converges.

---

[← Previous: NM-8.8 Boundary Value Problems](../NM-8_ODE/NM-8.8_Boundary_Value_Problems.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: NM-10.1 PDE Classification & Theory →](../NM-10_PDE/NM-10.1_Classification.md)
