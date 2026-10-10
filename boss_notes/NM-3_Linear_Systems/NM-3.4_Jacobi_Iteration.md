[← Previous: NM-3.3 LU Decomposition](NM-3.3_LU_Decomposition.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: NM-3.5 Gauss-Seidel →](NM-3.5_Gauss_Seidel.md)

---

# NM-3.4: Jacobi Iteration

> 🟠 **Priority:** Secondary | **Tested:** 2 appearances | **Typical marks:** 5

## What This Is (and Why It Matters)

Up to this point, we have solved linear systems using **direct elimination**: crunching through row subtractions to get an exact algebraic answer. But what happens when you have a circuit network with 100,000 nodes, where each node connects to only 3 or 4 neighbors? The matrix is massive, but mostly filled with zeros (a **sparse matrix**). If you run Gauss elimination, those zeros fill up with numbers, eating all your computer's memory.

This is where **iterative methods** take over. Instead of eliminating variables, you start with an initial guess (often all zeros: $x=0, y=0, z=0$) and repeatedly plug your numbers into an update formula until they stabilize.

The **Jacobi Iteration Method** is the purest, most democratic iterative method: during each iteration round, every unknown is updated using **only the old values from the previous round**. Because no variable waits for another, you can compute all unknowns simultaneously in parallel on a modern graphics card (GPU).

In RUET exams, this appears as a 5-mark numerical problem (such as 2017 Q.7(a) and 2022 Q.4(a)) asking you to run iteration sweeps on a $3 \times 3$ system until convergence.

---

## 📝 Key Definitions

> **Jacobi Method (Simultaneous Displacements):** "This method is due to Jacobi and is called the *method of simultaneous displacements*." -- Jain, §7.6 (p. 280)
> 
> **In simple words:** A team iteration where everyone gets updated at the exact same moment using only the notes from the previous round. Nobody looks at their neighbor's freshly computed answer until the round is over.

> **Jacobi Iteration Formula:** The mathematical update rule for the $i$-th unknown:
> $$
> x_i^{(k+1)} = \frac{1}{a_{ii}} \left( b_i - \sum_{j \ne i} a_{ij} x_j^{(k)} \right)
> $$
> 
> **In simple words:** Solve equation $i$ for its own diagonal variable $x_i$, and plug in all the other variables from iteration step $k$.

> **Strict Diagonal Dominance:** "provided that $\sum_{j=1, \, j \ne i}^n \left| \frac{a_{ij}}{a_{ii}} \right| < 1, \quad (i = 1, 2, \dots, n)$." -- Jain, §7.6 (p. 281)
> 
> **In simple words:** In every single row, the magnitude of the diagonal number is strictly bigger than the sum of the magnitudes of all the other numbers in that row combined.

---

## The Core Idea

### Setting Up the Iteration
Consider a $3 \times 3$ system of equations:
$$
\begin{aligned}
a_{11}x + a_{12}y + a_{13}z &= b_1 \\
a_{21}x + a_{22}y + a_{23}z &= b_2 \\
a_{31}x + a_{32}y + a_{33}z &= b_3
\end{aligned}
$$

Assume no diagonal entry is zero ($a_{ii} \ne 0$). We isolate each variable on the diagonal:
$$
x = \frac{b_1 - a_{12}y - a_{13}z}{a_{11}}
$$
$$
y = \frac{b_2 - a_{21}x - a_{23}z}{a_{22}}
$$
$$
z = \frac{b_3 - a_{31}x - a_{32}y}{a_{33}}
$$

In the Jacobi method, we add iteration counters: to compute the new values at step $k+1$, we plug in **strictly step $k$ values** on the right side:
$$
x^{(k+1)} = \frac{b_1 - a_{12}y^{(k)} - a_{13}z^{(k)}}{a_{11}}
$$
$$
y^{(k+1)} = \frac{b_2 - a_{21}x^{(k)} - a_{23}z^{(k)}}{a_{22}}
$$
$$
z^{(k+1)} = \frac{b_3 - a_{31}x^{(k)} - a_{32}y^{(k)}}{a_{33}}
$$

Notice that even after you calculate $x^{(k+1)}$, you **do not** plug it into the formula for $y^{(k+1)}$! You still use the old $x^{(k)}$. All three updates are calculated in parallel from the old snapshot.

### Matrix Formulation: Splitting Matrix $A$
We can split the matrix $A$ into three pieces:
$$
A = D + L + U
$$
where $D$ is the diagonal matrix, $L$ is strictly lower triangular, and $U$ is strictly upper triangular.
Then:
$$
(D + L + U)\mathbf{x} = \mathbf{b} \implies D\mathbf{x} = \mathbf{b} - (L + U)\mathbf{x}
$$
Multiplying by $D^{-1}$ gives the Jacobi iteration matrix:
$$
\mathbf{x}^{(k+1)} = -D^{-1}(L + U)\mathbf{x}^{(k)} + D^{-1}\mathbf{b} = B_J \mathbf{x}^{(k)} + \mathbf{c}
$$
where $B_J = -D^{-1}(L + U)$ is the **Jacobi iteration matrix**.

### When Is Convergence Guaranteed?
The iteration converges to the true solution for **any starting vector** if and only if the spectral radius of the iteration matrix satisfies $\rho(B_J) < 1$.

In practice, we check the simple **Strict Diagonal Dominance** rule:
$$
|a_{ii}| > \sum_{j \ne i} |a_{ij}| \quad \text{for every row } i
$$
If every row satisfies this condition, the system is mathematically guaranteed to converge!

### Jacobi vs. Gauss-Seidel: What Is the Difference?

| Feature | Jacobi Iteration | Gauss-Seidel Iteration |
| :-- | :-- | :-- |
| **Alternative Name** | Simultaneous displacements | Successive displacements |
| **Update Mechanism** | Uses only old values from sweep $k$ | Uses new values as soon as available |
| **Formula for $y^{(k+1)}$** | Uses $x^{(k)}$ | Uses $x^{(k+1)}$ |
| **Convergence Speed** | Slower (roughly takes $2\times$ sweeps) | Faster (spectral radius $\rho_{GS} \approx \rho_J^2$) |
| **Parallel Computation** | Trivial: each variable computed independently | Harder: variables depend on earlier outputs |
| **Memory Needed** | Must store two full vectors ($X^{(k)}$ and $X^{(k+1)}$) | Can overwrite in-place in a single memory vector |

---

## 🔧 Worked Example & Golden Question

> **The question:** Solve the following system using the Jacobi method:
> $$
> \begin{aligned}
> 6x + y + z &= 20 \\
> x + 4y - z &= 6 \\
> x - y + 5z &= 7
> \end{aligned}
> $$
> 
> *(Source: 2017 Q.7(a), 2022 Q.4(a) [Marks: 05])*

**Let's solve this step by step.**

### Step 1: Check Strict Diagonal Dominance
Before writing iteration formulas, we must inspect the diagonal elements:
- **Row 1:** Diagonal is $|6|$. Off-diagonal sum is $|1| + |1| = 2$.  
  $|6| > 2$ (Strictly dominant! $\checkmark$)
- **Row 2:** Diagonal is $|4|$. Off-diagonal sum is $|1| + |-1| = 2$.  
  $|4| > 2$ (Strictly dominant! $\checkmark$)
- **Row 3:** Diagonal is $|5|$. Off-diagonal sum is $|1| + |-1| = 2$.  
  $|5| > 2$ (Strictly dominant! $\checkmark$)

Every row satisfies strict diagonal dominance. Convergence from any initial guess is guaranteed!

### Step 2: Form the Jacobi Update Equations
Isolate the diagonal variable in each equation:
$$
x^{(k+1)} = \frac{20 - y^{(k)} - z^{(k)}}{6}
$$
$$
y^{(k+1)} = \frac{6 - x^{(k)} + z^{(k)}}{4}
$$
$$
z^{(k+1)} = \frac{7 - x^{(k)} + y^{(k)}}{5}
$$

### Step 3: Run the Iteration Sweeps
Let's choose the standard starting guess:
$$
x^{(0)} = 0, \qquad y^{(0)} = 0, \qquad z^{(0)} = 0
$$

#### Sweep 1:
- $x^{(1)} = \frac{20 - 0 - 0}{6} = \frac{20}{6} \approx 3.333333$
- $y^{(1)} = \frac{6 - 0 + 0}{4} = \frac{6}{4} = 1.500000$
- $z^{(1)} = \frac{7 - 0 + 0}{5} = \frac{7}{5} = 1.400000$

#### Sweep 2:
Plug in $x^{(1)} = 3.333333$, $y^{(1)} = 1.500000$, and $z^{(1)} = 1.400000$:
- $x^{(2)} = \frac{20 - 1.500000 - 1.400000}{6} = \frac{17.100000}{6} = 2.850000$
- $y^{(2)} = \frac{6 - 3.333333 + 1.400000}{4} = \frac{4.066667}{4} = 1.016667$
- $z^{(2)} = \frac{7 - 3.333333 + 1.500000}{5} = \frac{5.166667}{5} = 1.033333$

#### Sweep 3:
Plug in the Sweep 2 values:
- $x^{(3)} = \frac{20 - 1.016667 - 1.033333}{6} = \frac{17.950000}{6} = 2.991667$
- $y^{(3)} = \frac{6 - 2.850000 + 1.033333}{4} = \frac{4.183333}{4} = 1.045833$
- $z^{(3)} = \frac{7 - 2.850000 + 1.016667}{5} = \frac{5.166667}{5} = 1.033333$

### Complete Iteration History Table

| Sweep ($k$) | $x^{(k)}$ | $y^{(k)}$ | $z^{(k)}$ |
| :--: | :-- | :-- | :-- |
| **0** | $0.000000$ | $0.000000$ | $0.000000$ |
| **1** | $3.333333$ | $1.500000$ | $1.400000$ |
| **2** | $2.850000$ | $1.016667$ | $1.033333$ |
| **3** | $2.991667$ | $1.045833$ | $1.033333$ |
| **4** | $2.986806$ | $1.010417$ | $1.010833$ |
| **5** | $2.996458$ | $1.006007$ | $1.004722$ |
| **6** | $2.998212$ | $1.002066$ | $1.001910$ |
| **7** | $2.999337$ | $1.000924$ | $1.000771$ |
| **8** | $2.999717$ | $1.000358$ | $1.000317$ |

Look how cleanly the numbers march toward integer values! By sweep 8, they have converged to 4 decimal places.

### Verification by Direct Substitution
Let's test the integer target $(x = 3, y = 1, z = 1)$:
1. $6(3) + 1 + 1 = 18 + 2 = 20 \quad \checkmark$
2. $3 + 4(1) - 1 = 3 + 4 - 1 = 6 \quad \checkmark$
3. $3 - 1 + 5(1) = 2 + 5 = 7 \quad \checkmark$

$$
\boxed{x = 3, \qquad y = 1, \qquad z = 1}
$$

---

### Exam Variants at a Glance

| Year | What They Asked | Key Result |
|:---|:---|:---|
| **2017 Q.7(a)** | Solve $6x+y+z=20, x+4y-z=6, x-y+5z=7$ via Jacobi (05 marks) | $\boxed{x = 3, \qquad y = 1, \qquad z = 1}$ |
| **2022 Q.4(a)** | Solve identical $3\times3$ system via Jacobi (05 marks) | $\boxed{x = 3, \qquad y = 1, \qquad z = 1}$ |

---

## ⚡ Quick Review

**The method in one sentence:** Solve each row for its own diagonal unknown, and update all variables simultaneously using only the numbers from the previous round.

**The update rule you must remember:**
$$
x_i^{(k+1)} = \frac{1}{a_{ii}}\left(b_i - \sum_{j \ne i} a_{ij} x_j^{(k)}\right)
$$

**The most common exam mistake:** Accidentally slipping a freshly computed $x^{(k+1)}$ into the equation for $y^{(k+1)}$. That turns your solution into Gauss-Seidel! Keep your hands off the new values until the entire sweep is finished.

**Time estimate in exam:** ~8 to 10 minutes to compute 4 to 6 sweeps on your calculator.

---

## 🔗 Connected Topics

- [← NM-3.3: LU Decomposition](NM-3.3_LU_Decomposition.md) -- direct triangular factorizations vs iterative updates.
- [→ NM-3.5: Gauss-Seidel](NM-3.5_Gauss_Seidel.md) -- the upgraded sibling that uses fresh numbers immediately to converge twice as fast.
- [NM-3.6: Relaxation](NM-3.6_Relaxation.md) -- weighting iteration steps to accelerate convergence.

---

[← Previous: NM-3.3 LU Decomposition](NM-3.3_LU_Decomposition.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: NM-3.5 Gauss-Seidel →](NM-3.5_Gauss_Seidel.md)
