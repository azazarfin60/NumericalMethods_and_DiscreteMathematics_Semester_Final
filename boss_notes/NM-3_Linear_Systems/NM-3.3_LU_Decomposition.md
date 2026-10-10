[← Previous: NM-3.2 Pivoting](NM-3.2_Pivoting.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: NM-3.4 Jacobi Iteration →](NM-3.4_Jacobi_Iteration.md)

---

# NM-3.3: LU Decomposition

> 🟠 **Priority:** Secondary | **Tested:** 2 appearances | **Typical marks:** 4–5

## What This Is (and Why It Matters)

In engineering practice, you almost never solve a circuit just once. Think about a power grid or an audio amplifier: the physical resistors and capacitors (matrix $A$) stay constant, but the input voltages or load demands ($\mathbf{b}$) change every millisecond.

If you use plain Gauss elimination, you have to repeat the entire $O(n^3)$ forward elimination process from scratch for every single new input vector. That is massive computational waste!

**LU Decomposition** solves this by separating the matrix into two parts:
$$
A = LU
$$
where $L$ is a **Lower triangular matrix** and $U$ is an **Upper triangular matrix**. You do the heavy $O(n^3)$ elimination once to find $L$ and $U$. After that, whenever a new input vector $\mathbf{b}$ arrives, you solve two lightning-fast triangular systems (one forward substitution, one back-substitution) costing only $O(n^2)$ operations each.

In RUET exams, this appears as an analytical derivation question (such as 2017 Q.4(b)): showing how a matrix is factorized into $LU$, how elementary multipliers build $L$, and why this is computationally superior for multiple right-hand sides.

---

## 📝 Key Definitions

> **LU Factorisation:** "Let $A$ be a nonsingular square matrix. Then $A$ can be factorized into the form $LU$ ... It is a standard result of linear algebra that such a factorization, when it exists, is *unique*." -- Jain, §7.3 (p. 257–258)
> 
> **In simple words:** Splitting a matrix into the product of a lower triangular matrix $L$ and an upper triangular matrix $U$.

> **Doolittle Form:** An LU factorization where $L$ is **unit lower triangular** (meaning its diagonal elements are strictly $1$, so $l_{ii} = 1$), while $U$ is upper triangular.
> 
> **In simple words:** The standard textbook form where the lower matrix has $1$s on the main diagonal and stores the elimination multipliers below the diagonal.

> **Crout Form:** An LU factorization where $U$ is **unit upper triangular** (meaning its diagonal elements are strictly $1$, so $u_{ii} = 1$), while $L$ is lower triangular.
> 
> **In simple words:** The mirror image of Doolittle, where the $1$s sit on the diagonal of the upper matrix instead.

> **Forward Substitution:** Solving a lower triangular system $L\mathbf{y} = \mathbf{b}$ by starting from the top equation ($y_1 = b_1$) and cascading downward.
> 
> **In simple words:** The downward counterpart of back-substitution.

---

## The Core Idea

### The Two-Stage Solve: Divide and Conquer
Suppose we want to solve:
$$
A\mathbf{x} = \mathbf{b}
$$
If we can write $A = LU$, the equation becomes:
$$
LU\mathbf{x} = \mathbf{b}
$$
Now, introduce an intermediate vector $\mathbf{y} = U\mathbf{x}$. The single hard problem splits into two simple triangular problems:

1. **Step 1 (Forward Substitution):** Solve for $\mathbf{y}$:
$$
L\mathbf{y} = \mathbf{b}
$$
Since $L$ is lower triangular, the top equation gives $y_1$ immediately, which gives $y_2$, and so on down to $y_n$.

2. **Step 2 (Back-Substitution):** Solve for $\mathbf{x}$:
$$
U\mathbf{x} = \mathbf{y}
$$
Since $U$ is upper triangular, the bottom equation gives $x_n$ immediately, which gives $x_{n-1}$, climbing back to $x_1$.

Both substitutions cost only $n^2$ operations combined. No matrix inverses, no determinants, no hassle!

### Where Do $L$ and $U$ Come From?
Here is the beauty of it: **$U$ is literally the matrix left over after standard Gauss elimination, and $L$ is just the table of multipliers!**

Let's trace this for a $3 \times 3$ matrix:
$$
A = \begin{bmatrix}
a_{11} & a_{12} & a_{13} \\
a_{21} & a_{22} & a_{23} \\
a_{31} & a_{32} & a_{33}
\end{bmatrix}
$$

1. **First elimination stage:** To eliminate entries in column 1 below $a_{11}$, we calculate multipliers:
$$
l_{21} = \frac{a_{21}}{a_{11}}, \qquad l_{31} = \frac{a_{31}}{a_{11}}
$$
Subtracting these multiples of Row 1 from Rows 2 and 3 corresponds to multiplying $A$ on the left by an elementary matrix $L_1$:
$$
L_1 = \begin{bmatrix}
1 & 0 & 0 \\
-l_{21} & 1 & 0 \\
-l_{31} & 0 & 1
\end{bmatrix}
$$

2. **Second elimination stage:** To eliminate the entry in column 2 below the new pivot $a_{22}^{(1)}$, the multiplier is:
$$
l_{32} = \frac{a_{32}^{(1)}}{a_{22}^{(1)}}
$$
This corresponds to multiplying by $L_2$:
$$
L_2 = \begin{bmatrix}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & -l_{32} & 1
\end{bmatrix}
$$

3. **The final factorisation:** After these two stages, the matrix has become upper triangular $U$:
$$
L_2 L_1 A = U \implies A = (L_2 L_1)^{-1} U = L_1^{-1} L_2^{-1} U
$$
Because the inverse of an elementary elimination matrix simply flips the signs of the sub-diagonal entries, we have:
$$
L = L_1^{-1} L_2^{-1} = 
\begin{bmatrix}
1 & 0 & 0 \\
l_{21} & 1 & 0 \\
l_{31} & l_{32} & 1
\end{bmatrix}
$$

Look at that result: the matrix $L$ simply collects all the multipliers you already calculated during forward elimination!

$$
L = \begin{bmatrix}
1 & 0 & 0 \\
l_{21} & 1 & 0 \\
l_{31} & l_{32} & 1
\end{bmatrix}, \qquad
U = \begin{bmatrix}
u_{11} & u_{12} & u_{13} \\
0 & u_{22} & u_{23} \\
0 & 0 & u_{33}
\end{bmatrix}
$$

This is the **Doolittle decomposition**. You do not need to do any extra algebra to find $L$: you just record each multiplier into its lower triangular slot as you eliminate.

### The Big Win: Multiple Right-Hand Sides
Why do engineers care so much about this? Look at the operation counts:

Suppose you have $m$ different loading conditions ($\mathbf{b}_1, \mathbf{b}_2, \dots, \mathbf{b}_m$):
- **Using Gauss Elimination every time:**
$$
\text{Total Operations} \approx m \times \left(\frac{2}{3}n^3\right)
$$
- **Using LU Decomposition once, then solving:**
$$
\text{Total Operations} \approx \frac{2}{3}n^3 + m \times (2n^2)
$$

For an electrical network with $n = 500$ nodes tested across $m = 100$ load variations:
- Gauss elimination requires $\approx 100 \times \frac{2}{3}(500)^3 \approx 8.33 \times 10^9$ operations.
- LU decomposition requires $\approx \frac{2}{3}(500)^3 + 100 \times 2(500)^2 \approx 8.33 \times 10^7 + 5.0 \times 10^7 \approx 1.33 \times 10^8$ operations.
- **LU decomposition is over 60 times faster!**

---

## 🔧 Worked Demonstration: Step-by-Step Triangular Solve

Let's see how the two-stage solve works on a clean system where $L$, $U$, and $\mathbf{b}$ are known:

Suppose we factored a system into:
$$
L = \begin{bmatrix}
1 & 0 & 0 \\
2 & 1 & 0 \\
-1 & 3 & 1
\end{bmatrix}, \qquad
U = \begin{bmatrix}
2 & 1 & 1 \\
0 & 4 & 2 \\
0 & 0 & 5
\end{bmatrix}, \qquad
\mathbf{b} = \begin{bmatrix} 4 \\ 14 \\ 13 \end{bmatrix}
$$

### Step 1: Forward Substitution ($L\mathbf{y} = \mathbf{b}$)
$$
\begin{bmatrix}
1 & 0 & 0 \\
2 & 1 & 0 \\
-1 & 3 & 1
\end{bmatrix}
\begin{bmatrix} y_1 \\ y_2 \\ y_3 \end{bmatrix}
=
\begin{bmatrix} 4 \\ 14 \\ 13 \end{bmatrix}
$$

- Top equation:
$$
y_1 = 4
$$
- Middle equation:
$$
2y_1 + y_2 = 14 \implies 2(4) + y_2 = 14 \implies y_2 = 6
$$
- Bottom equation:
$$
-y_1 + 3y_2 + y_3 = 13 \implies -4 + 3(6) + y_3 = 13 \implies 14 + y_3 = 13 \implies y_3 = -1
$$

So our intermediate vector is $\mathbf{y} = [4, 6, -1]^T$.

### Step 2: Back-Substitution ($U\mathbf{x} = \mathbf{y}$)
$$
\begin{bmatrix}
2 & 1 & 1 \\
0 & 4 & 2 \\
0 & 0 & 5
\end{bmatrix}
\begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix}
=
\begin{bmatrix} 4 \\ 6 \\ -1 \end{bmatrix}
$$

- Bottom equation:
$$
5x_3 = -1 \implies x_3 = -0.2
$$
- Middle equation:
$$
4x_2 + 2x_3 = 6 \implies 4x_2 + 2(-0.2) = 6 \implies 4x_2 = 6.4 \implies x_2 = 1.6
$$
- Top equation:
$$
2x_1 + x_2 + x_3 = 4 \implies 2x_1 + 1.6 - 0.2 = 4 \implies 2x_1 = 2.6 \implies x_1 = 1.3
$$

Notice how fast and effortless that was: not a single row subtraction was needed because the matrices were already triangular!

---

## 🏆 Past Exam Questions

### 2017 Q.4(b): How Can a Matrix Be Factorized into LU Form? -- [05 marks]

**The question:** How can a square matrix be factorized into the form LU to solve linear system of equations?

**Tutor explanation & structured answer:**

**1. The Fundamental Principle:**  
Any nonsingular square matrix $A$ can be decomposed into the product of a unit lower triangular matrix $L$ and an upper triangular matrix $U$:
$$
A = LU
$$
Solving $A\mathbf{x} = \mathbf{b}$ then splits into two consecutive triangular systems:
$$
LU\mathbf{x} = \mathbf{b} \implies L\mathbf{y} = \mathbf{b} \quad \text{followed by} \quad U\mathbf{x} = \mathbf{y}
$$
Because both $L$ and $U$ are triangular, solving each requires only simple substitution, which is computationally cheap and numerically stable.

**2. Matrix Construction for a $3 \times 3$ System:**  
Gauss elimination transforms $A$ into $U$ while the elimination multipliers assemble $L$.

- **Step 1 (First Column Elimination):**  
  Using row 1, eliminate entries below the pivot $a_{11}$. The multipliers are:
$$
l_{21} = \frac{a_{21}}{a_{11}}, \qquad l_{31} = \frac{a_{31}}{a_{11}}
$$
Form $R_2 \leftarrow R_2 - l_{21}R_1$ and $R_3 \leftarrow R_3 - l_{31}R_1$. This is equivalent to pre-multiplying $A$ by the lower triangular elementary matrix $L_1$:
$$
L_1 = \begin{bmatrix}
1 & 0 & 0 \\
-l_{21} & 1 & 0 \\
-l_{31} & 0 & 1
\end{bmatrix}
$$

- **Step 2 (Second Column Elimination):**  
  Using the updated row 2, eliminate the entry below pivot $a_{22}^{(1)}$. The multiplier is:
$$
l_{32} = \frac{a_{32}^{(1)}}{a_{22}^{(1)}} = \frac{a_{32} - l_{31}a_{12}}{a_{22} - l_{21}a_{12}}
$$
Form $R_3 \leftarrow R_3 - l_{32}R_2^{(1)}$, which corresponds to pre-multiplying by $L_2$:
$$
L_2 = \begin{bmatrix}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & -l_{32} & 1
\end{bmatrix}
$$

- **Step 3 (Forming $L$ and $U$):**  
  The forward elimination produces the upper triangular matrix $U$:
$$
L_2 L_1 A = U \implies A = (L_2 L_1)^{-1} U = L_1^{-1} L_2^{-1} U = LU
$$
Multiplying the inverse elementary matrices yields:
$$
L = \begin{bmatrix}
1 & 0 & 0 \\
l_{21} & 1 & 0 \\
l_{31} & l_{32} & 1
\end{bmatrix}
$$
The multipliers from elimination drop directly into the sub-diagonal positions of $L$. This unit lower triangular form is the **Doolittle method**. (If $U$ is chosen to have ones on its diagonal instead, it is called the **Crout method**.)

**3. Solving the System:**  
- **Forward substitution:** Solve $L\mathbf{y} = \mathbf{b}$:
$$
y_1 = b_1, \qquad y_2 = b_2 - l_{21}y_1, \qquad y_3 = b_3 - l_{31}y_1 - l_{32}y_2
$$
- **Back-substitution:** Solve $U\mathbf{x} = \mathbf{y}$:
$$
x_3 = \frac{y_3}{u_{33}}, \qquad x_2 = \frac{y_2 - u_{23}x_3}{u_{22}}, \qquad x_1 = \frac{y_1 - u_{12}x_2 - u_{13}x_3}{u_{11}}
$$

**4. Engineering Significance:**  
The factorisation is computed once at a cost of roughly $\frac{n^3}{3}$ multiplications. Any new right-hand side vector $\mathbf{b}$ can then be solved in only $2n^2$ operations. For $m$ different inputs, this saves enormous computational time compared to running Gauss elimination $m$ times.

---

### Exam Variants at a Glance

| Year | What They Asked | Key Method / Answer |
|:---|:---|:---|
| **2017 Q.4(b)** | How can matrix be factorized into LU to solve systems? (05 marks) | Doolittle derivation: $L_1, L_2$, $L = L_1^{-1}L_2^{-1}$, forward/back solve |

---

## ⚡ Quick Review

**The method in one sentence:** Factor $A$ into $L$ (unit lower triangular holding the elimination multipliers) and $U$ (upper triangular), then solve $L\mathbf{y} = \mathbf{b}$ followed by $U\mathbf{x} = \mathbf{y}$.

**The two-step recipe:**
$$
L\mathbf{y} = \mathbf{b} \quad (\text{forward substitution}) \implies U\mathbf{x} = \mathbf{y} \quad (\text{back substitution})
$$

**The key efficiency advantage:** Factor once at $O(n^3)$, then solve any new right-hand side $\mathbf{b}$ in just $O(n^2)$ time.

**Time estimate in exam:** ~8 minutes to write down the full algebraic derivation and elementary matrix explanation.

---

## 🔗 Connected Topics

- [← NM-3.2: Pivoting](NM-3.2_Pivoting.md) -- when row swaps are needed, we store them in a permutation matrix $P$ to form $PA = LU$.
- [→ NM-3.4: Jacobi Iteration](NM-3.4_Jacobi_Iteration.md) -- switching from direct matrix factorizations to iterative convergence sweeps.
- [NM-3.1: Gauss Elimination](NM-3.1_Gauss_Elimination.md) -- the elimination process whose multipliers form matrix $L$.

---

[← Previous: NM-3.2 Pivoting](NM-3.2_Pivoting.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: NM-3.4 Jacobi Iteration →](NM-3.4_Jacobi_Iteration.md)
