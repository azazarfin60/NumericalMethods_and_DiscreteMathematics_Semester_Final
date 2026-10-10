[← Previous: NM-2.7 Polynomial Roots](../NM-2_Root_Finding/NM-2.7_Polynomial_Roots.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: NM-3.2 Pivoting →](NM-3.2_Pivoting.md)

---

# NM-3.1: Gauss Elimination

> 🔴 **Priority:** Critical | **Tested:** 3 appearances | **Typical marks:** 4–5

## What This Is (and Why It Matters)

Imagine you are solving three simultaneous linear equations with pencil and paper. What do you naturally do? You take the first equation, use it to knock out the first variable from the other two equations, and repeat until you are left with a single equation in one variable. Once you find that last variable, you plug it back upward to find the rest.

That simple, intuitive high-school technique is **Gauss Elimination**. In numerical computing, we turn this procedure into an algorithm. It transforms an messy system matrix into an organized **upper triangular matrix**, and then computes every unknown through **back-substitution**.

The exam loves testing Gauss elimination in two ways: either as a theoretical essay question ("describe the direct elimination method and state its operation count"), or as a concrete numerical calculation where you must show your row operations cleanly without dropping signs.

---

## 📝 Key Definitions

> **Direct Methods:** "these methods yield the solution after an amount of computation that is known in advance ... in a direct method the amount of computation is fixed." -- Jain, §7.6 (p. 279)
> 
> **In simple words:** An algorithm with a fixed recipe and guaranteed end. You do a set number of calculations, and boom, you get the exact mathematical answer without guessing or iterating.

> **Gauss Elimination:** "This is the elementary elimination method and it reduces the system of equations to an equivalent upper-triangular system, which can be solved by *back substitution*." -- Jain, §7.5.1 (p. 263)
> 
> **In simple words:** Systematic row-by-row elimination that wipes out all numbers below the main diagonal, leaving a tidy triangle of equations that you can solve from bottom to top.

> **Upper Triangular System:** A system of equations where all coefficients below the main diagonal are zero ($a_{ij} = 0$ for all $i > j$).
> 
> **In simple words:** A staircase system. The last equation has only one unknown, the second-to-last has two, and so on.

---

## The Core Idea

Suppose you want to solve an $n \times n$ linear system:
$$
A\mathbf{x} = \mathbf{b}
$$

In full expanded form, the system looks like this:
$$
\begin{aligned}
a_{11}x_1 + a_{12}x_2 + \dots + a_{1n}x_n &= b_1 \\
a_{21}x_1 + a_{22}x_2 + \dots + a_{2n}x_n &= b_2 \\
&\;\;\vdots \\
a_{n1}x_1 + a_{n2}x_2 + \dots + a_{nn}x_n &= b_n
\end{aligned}
$$

We place the coefficients and right-hand side constants into an **augmented matrix**:
$$
[A \mid \mathbf{b}] = 
\left[\begin{array}{cccc|c}
a_{11} & a_{12} & \dots & a_{1n} & b_1 \\
a_{21} & a_{22} & \dots & a_{2n} & b_2 \\
\vdots & \vdots & \ddots & \vdots & \vdots \\
a_{n1} & a_{n2} & \dots & a_{nn} & b_n
\end{array}\right]
$$

Gauss elimination solves this in two distinct stages.

### Stage 1: Forward Elimination
Our goal is to create zeros under each diagonal entry (called the **pivot**).

For each column $k$ (from column $1$ to $n-1$):
1. Pick the diagonal element $a_{kk}$ as the pivot.
2. For every row below it ($i = k+1, k+2, \dots, n$), compute the row multiplier:
$$
m_{ik} = \frac{a_{ik}}{a_{kk}}
$$
3. Subtract $m_{ik}$ times row $k$ from row $i$:
$$
\text{Row}_i \leftarrow \text{Row}_i - m_{ik}\,\text{Row}_k
$$
This systematically wipes out $a_{ik}$, turning it into zero.

After $n-1$ elimination stages, your augmented matrix becomes strictly upper triangular:
$$
\left[\begin{array}{cccc|c}
u_{11} & u_{12} & \dots & u_{1n} & c_1 \\
0 & u_{22} & \dots & u_{2n} & c_2 \\
\vdots & \vdots & \ddots & \vdots & \vdots \\
0 & 0 & \dots & u_{nn} & c_n
\end{array}\right]
$$

### Stage 2: Back-Substitution
Now solve the equations from the bottom row up to the top row:

1. The bottom row gives $x_n$ instantly:
$$
x_n = \frac{c_n}{u_{nn}}
$$

2. For all remaining rows $i = n-1, n-2, \dots, 1$, substitute the already known values:
$$
x_i = \frac{1}{u_{ii}}\left( c_i - \sum_{j=i+1}^n u_{ij} x_j \right)
$$

### Computational Complexity: How Much Work Is It?
Examiners frequently ask for the arithmetic operation count:
- **Forward elimination:** Requires roughly $\frac{2}{3}n^3$ multiplications and additions. This is where almost all the computer's time is spent.
- **Back-substitution:** Requires only roughly $\frac{1}{2}n^2$ operations.
- **Total cost:** Scales as $O(n^3)$. If you double the number of equations, the elimination effort jumps by a factor of 8!

| Direct Method | Arithmetic Cost | Storage | Key Characteristic |
| :-- | :-- | :-- | :-- |
| **Gauss Elimination** | $\frac{2}{3}n^3$ | $n^2$ | Standard direct solver with back-substitution |
| **Gauss-Jordan** | $n^3$ | $n^2$ | Eliminates above and below; finds matrix inverse directly |
| **LU Decomposition** | $\frac{2}{3}n^3 + 2mn^2$ | $n^2$ | Best when solving $m$ systems with different right-hand sides |
| **Cholesky** | $\frac{1}{3}n^3$ | $\frac{1}{2}n^2$ | Efficient, but works only for symmetric positive-definite matrices |

### When Does Plain Gauss Elimination Fail?
1. **Division by zero:** If any pivot $a_{kk} = 0$, calculating $m_{ik} = a_{ik}/0$ crashes immediately.
2. **Tiny pivots:** If $a_{kk}$ is tiny (like $10^{-6}$) compared to other entries, the multiplier $m_{ik}$ becomes huge. Subtracting huge numbers creates catastrophic cancellation error.
3. *The cure:* **Partial pivoting** (swapping rows to put the largest available number on the diagonal). We explore this fully in [NM-3.2](NM-3.2_Pivoting.md).

> [!WARNING] Common Trap
> Don't forget the right-hand side! When performing row operations ($\text{Row}_i - m_{ik}\text{Row}_k$), many students update the matrix coefficients on the left but forget to update the constant $b_i$ on the right. Always operate on the entire augmented row.

---

## 🔧 Worked Example

> **The question:** Solve the following system using Gauss elimination:
> $$
> \begin{aligned}
> 2x_1 + x_2 - x_3 &= -1 \\
> x_1 - 2x_2 + 3x_3 &= 9 \\
> 3x_1 - x_2 + 5x_3 &= 14
> \end{aligned}
> $$
> Check your answer by substituting into the original equations.
> 
> *(Source: 2022 Q.4(b) [Marks: 05])*

**Let's solve this step by step.**

### Step 1: Write down the augmented matrix
Let's assemble all coefficients and constants into a single matrix:
$$
\left[\begin{array}{ccc|c}
2 & 1 & -1 & -1 \\
1 & -2 & 3 & 9 \\
3 & -1 & 5 & 14
\end{array}\right]
$$

### Step 2: Clear Column 1 (Eliminate $x_1$ from Rows 2 and 3)
Our pivot in Row 1 is $a_{11} = 2$.

- For Row 2, the multiplier is $m_{21} = \frac{1}{2} = 0.5$.  
  Row operation: $R_2 \leftarrow R_2 - \frac{1}{2}R_1$:
  - First element: $1 - \frac{1}{2}(2) = 0$
  - Second element: $-2 - \frac{1}{2}(1) = -\frac{5}{2}$
  - Third element: $3 - \frac{1}{2}(-1) = 3 + \frac{1}{2} = \frac{7}{2}$
  - Constant: $9 - \frac{1}{2}(-1) = 9 + \frac{1}{2} = \frac{19}{2}$

- For Row 3, the multiplier is $m_{31} = \frac{3}{2} = 1.5$.  
  Row operation: $R_3 \leftarrow R_3 - \frac{3}{2}R_1$:
  - First element: $3 - \frac{3}{2}(2) = 0$
  - Second element: $-1 - \frac{3}{2}(1) = -\frac{5}{2}$
  - Third element: $5 - \frac{3}{2}(-1) = 5 + \frac{3}{2} = \frac{13}{2}$
  - Constant: $14 - \frac{3}{2}(-1) = 14 + \frac{3}{2} = \frac{31}{2}$

Our updated matrix looks like this:
$$
\left[\begin{array}{ccc|c}
2 & 1 & -1 & -1 \\
0 & -\frac{5}{2} & \frac{7}{2} & \frac{19}{2} \\
0 & -\frac{5}{2} & \frac{13}{2} & \frac{31}{2}
\end{array}\right]
$$

### Step 3: Clear Column 2 (Eliminate $x_2$ from Row 3)
Now look at Row 2. The pivot is $a_{22} = -\frac{5}{2}$.  
Row 3 has $-\frac{5}{2}$ in that column as well!

The multiplier is $m_{32} = \frac{-5/2}{-5/2} = 1$.  
Row operation: $R_3 \leftarrow R_3 - 1 \times R_2$:
- Second element: $-\frac{5}{2} - \left(-\frac{5}{2}\right) = 0$
- Third element: $\frac{13}{2} - \frac{7}{2} = \frac{6}{2} = 3$
- Constant: $\frac{31}{2} - \frac{19}{2} = \frac{12}{2} = 6$

Our augmented matrix is now beautifully upper triangular:
$$
\left[\begin{array}{ccc|c}
2 & 1 & -1 & -1 \\
0 & -\frac{5}{2} & \frac{7}{2} & \frac{19}{2} \\
0 & 0 & 3 & 6
\end{array}\right]
$$

### Step 4: Back-Substitution
Now we work backward from the bottom row up to the top:

1. **From Row 3:**
$$
3x_3 = 6 \implies x_3 = 2
$$

2. **From Row 2:**
$$
-\frac{5}{2}x_2 + \frac{7}{2}x_3 = \frac{19}{2}
$$
Plug in $x_3 = 2$:
$$
-\frac{5}{2}x_2 + \frac{7}{2}(2) = \frac{19}{2} \implies -\frac{5}{2}x_2 + 7 = \frac{19}{2}
$$
$$
-\frac{5}{2}x_2 = \frac{19}{2} - 7 = \frac{5}{2} \implies x_2 = -1
$$

3. **From Row 1:**
$$
2x_1 + x_2 - x_3 = -1
$$
Plug in $x_2 = -1$ and $x_3 = 2$:
$$
2x_1 + (-1) - (2) = -1 \implies 2x_1 - 3 = -1 \implies 2x_1 = 2 \implies x_1 = 1
$$

$$
\boxed{x_1 = 1, \qquad x_2 = -1, \qquad x_3 = 2}
$$

### Step 5: Verification Check
Substitute $x_1 = 1$, $x_2 = -1$, and $x_3 = 2$ back into all three original equations:
1. $2(1) + (-1) - (2) = 2 - 1 - 2 = -1$ (Matches Row 1 RHS $\checkmark$)
2. $1 - 2(-1) + 3(2) = 1 + 2 + 6 = 9$ (Matches Row 2 RHS $\checkmark$)
3. $3(1) - (-1) + 5(2) = 3 + 1 + 10 = 14$ (Matches Row 3 RHS $\checkmark$)

All three equations balance perfectly!

---

## 🏆 Past Exam Questions

### 2019 Q.3(a): Discuss Gauss Elimination Method -- [04 marks]

**The question:** Discuss Gauss Elimination method to solve linear simultaneous algebraic equations.

**Tutor explanation & structured answer:**

**1. The Concept:**  
Gauss elimination solves a system $A\mathbf{x} = \mathbf{b}$ by converting the coefficient matrix into an equivalent upper triangular matrix using elementary row operations, and then finding the unknowns one by one through back-substitution. Because every row operation is reversible, the solution set never changes.

**2. The General System:**  
For $n$ equations with $n$ unknowns:
$$
\begin{aligned}
a_{11}x_1 + a_{12}x_2 + \dots + a_{1n}x_n &= b_1 \\
a_{21}x_1 + a_{22}x_2 + \dots + a_{2n}x_n &= b_2 \\
&\;\;\vdots \\
a_{n1}x_1 + a_{n2}x_2 + \dots + a_{nn}x_n &= b_n
\end{aligned}
$$

**3. Execution Steps:**
- **Step 1 (Forward Elimination):** Use equation 1 to clear $x_1$ from equations 2 through $n$ by replacing $\text{Row}_i \leftarrow \text{Row}_i - \frac{a_{i1}}{a_{11}}\text{Row}_1$. Next, use the updated equation 2 to clear $x_2$ from equations 3 through $n$. Continue this process for all $n-1$ columns.
- **Step 2 (Upper Triangular Matrix):** After $n-1$ passes, the augmented matrix reaches upper triangular form:
$$
\begin{aligned}
u_{11}x_1 + u_{12}x_2 + \dots + u_{1n}x_n &= b_1' \\
u_{22}x_2 + \dots + u_{2n}x_n &= b_2' \\
&\;\;\vdots \\
u_{nn}x_n &= b_n'
\end{aligned}
$$
- **Step 3 (Back-Substitution):** Solve the bottom equation for $x_n = b_n'/u_{nn}$. Plug $x_n$ into equation $n-1$ to solve for $x_{n-1}$, and climb upward until $x_1$ is found.
- **Step 4 (Pivoting safeguard):** If any pivot $u_{kk}$ is zero or close to zero, interchange row $k$ with a lower row having a larger coefficient in that column (partial pivoting).

**4. Operation Count:**  
Forward elimination requires roughly $\frac{n^3}{3}$ multiplications and subtractions, while back-substitution requires roughly $\frac{n^2}{2}$ operations. Total computational cost scales as $O(n^3)$.

---

### 2020 Q.4(a): Direct Methods to Solve Linear Systems -- [04 marks]

**The question:** What are the direct methods to solve linear system of equations? Describe any one of them.

**Tutor explanation & structured answer:**

**1. Classification of Direct Methods:**  
Direct methods produce the exact analytical solution in a **predetermined, fixed number of arithmetic operations**, without needing repeated iterative sweeps. They fall into two primary families:
1. **Elimination Methods:** Transform the augmented matrix into triangular or diagonal form using elementary row operations. Examples include **Gauss Elimination** and **Gauss-Jordan Elimination**.
2. **Matrix Factorization Methods:** Factor matrix $A$ into structured matrix components and solve triangular systems sequentially. Examples include **LU Factorization (Doolittle, Crout)**, **Cholesky Factorization** ($A = LL^T$), and **QR Factorization**.

**2. Detailed Description: Gaussian Elimination with Partial Pivoting:**  
Write down the augmented matrix $[A \mid \mathbf{b}]$. For each column $k = 1, \dots, n-1$:
1. Search column $k$ in rows $k$ through $n$ for the element with the largest absolute value, and swap that row into position $k$ (partial pivoting).
2. Calculate multipliers and eliminate entries below the pivot:
$$
m_{ik} = \frac{a_{ik}}{a_{kk}}, \qquad \text{Row}_i \leftarrow \text{Row}_i - m_{ik}\,\text{Row}_k \quad (i = k+1, \dots, n)
$$
3. Perform back-substitution from bottom to top:
$$
x_n = \frac{c_n}{u_{nn}}, \qquad x_i = \frac{1}{u_{ii}}\left(c_i - \sum_{j=i+1}^n u_{ij}x_j\right)
$$

**Worked Micro-Example:** Solve $2x + y = 5$ and $x - y = 1$.  
Augmented matrix:
$$
\left[\begin{array}{cc|c}
2 & 1 & 5 \\
1 & -1 & 1
\end{array}\right]
$$
Multiplier $m_{21} = \frac{1}{2}$. Row 2 becomes:
$$
\left[1 - \frac{1}{2}(2),\; -1 - \frac{1}{2}(1) \;\middle|\; 1 - \frac{1}{2}(5)\right] = \left[0,\; -\frac{3}{2} \;\middle|\; -\frac{3}{2}\right]
$$
Back-substituting gives:
$$
-\frac{3}{2}y = -\frac{3}{2} \implies y = 1
$$
$$
2x + (1) = 5 \implies 2x = 4 \implies x = 2
$$

$$
\boxed{x = 2, \qquad y = 1}
$$

$$
\boxed{\text{Eliminate to upper triangular form, pivot to stay safe, then back-substitute}}
$$

---

### Exam Variants at a Glance

| Year | What They Asked | Key Method / Answer |
|:---|:---|:---|
| **2019 Q.3(a)** | Discuss Gauss elimination method (04 marks) | Forward elimination + back-substitution algorithm |
| **2020 Q.4(a)** | Direct methods classification & describe one (04 marks) | $\boxed{x = 2, \qquad y = 1}$ (micro-example) |
| **2022 Q.4(b)** | Solve $3\times3$ system and verify by substitution (05 marks) | $\boxed{x_1 = 1, \qquad x_2 = -1, \qquad x_3 = 2}$ |

---

## ⚡ Quick Review

**The method in one sentence:** Turn $[A \mid \mathbf{b}]$ into an upper triangular matrix using row multipliers $m_{ik} = a_{ik}/a_{kk}$, then solve backward from the bottom equation.

**The multiplier formula you must memorize:**
$$
m_{ik} = \frac{a_{ik}}{a_{kk}}, \qquad \text{Row}_i \leftarrow \text{Row}_i - m_{ik}\,\text{Row}_k
$$

**The most common exam mistake:** Forgetting to update the right-hand side constant column $b$ during row subtractions, or getting tangled in negative signs when subtracting a negative multiplier.

**Time estimate in exam:** ~8 to 10 minutes for a complete $3\times3$ system including the substitution check.

---

## 🔗 Connected Topics

- [← NM-2.7: Polynomial Roots](../NM-2_Root_Finding/NM-2.7_Polynomial_Roots.md) -- single nonlinear polynomial roots vs multi-variable linear systems.
- [→ NM-3.2: Pivoting](NM-3.2_Pivoting.md) -- why small diagonal elements break Gauss elimination and how row swaps save the day.
- [NM-3.3: LU Decomposition](NM-3.3_LU_Decomposition.md) -- saving the elimination multipliers into a matrix $L$ so you can reuse them.

---

[← Previous: NM-2.7 Polynomial Roots](../NM-2_Root_Finding/NM-2.7_Polynomial_Roots.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: NM-3.2 Pivoting →](NM-3.2_Pivoting.md)
