[← Previous: NM-3.1 Gauss Elimination](NM-3.1_Gauss_Elimination.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: NM-3.3 LU Decomposition →](NM-3.3_LU_Decomposition.md)

---

# NM-3.2: Pivoting

> 🔴 **Priority:** Critical | **Tested:** 4/8 years | **Typical marks:** 2–4

## What This Is (and Why It Matters)

Every elimination step divides by the diagonal entry. That divisor is called the **pivot**. And that single division is where Gauss elimination can blow up in your face.

Think about what happens when you divide by zero: your calculator screams an error, and your program crashes. But there is something far more dangerous than a zero divisor: a **tiny divisor**. If your pivot is $10^{-6}$, dividing by it produces multipliers on the order of $10^6$. When you subtract numbers that have been multiplied by a million, you flood the rest of the matrix with massive rounding errors. The computer never crashes. It happily runs to the end and hands you completely bogus numbers.

**Pivoting** is the simple, elegant safeguard: before doing any division, you scan the numbers and swap rows (or columns) so the largest possible number sits in the pivot position.

In RUET exams, this appears in 4 out of 8 papers. The questions are short, conceptual, and easy marks: "What is pivoting?", "Compare partial and complete pivoting", or "Why is pivoting important?" Learn this note, and those 2 to 4 marks are guaranteed.

---

## 📝 Key Definitions

> **Pivot Element:** "the first equation in the system (7.30) is called the *pivot equation*, and $a_{11}$ is called the *pivot* ... The method obviously fails if $a_{11} = 0$." -- Jain, §7.5.1 (p. 264)
> 
> **In simple words:** The diagonal number you use as the divisor to wipe out all the other numbers below it in that column.

> **Necessity for Pivoting:** "We now come to the important case of the pivot being zero or very close to zero. If the *pivot is zero*, the *entire process fails* and if it is close to zero, round-off errors may occur. These problems can be avoided by adopting a procedure called *pivoting*." -- Jain, §7.5.2 (p. 265)
> 
> **In simple words:** If your divisor is zero, you crash; if it is microscopic, rounding errors destroy your accuracy. Pivoting swaps rows so you always divide by a solid, healthy number.

> **Partial Pivoting:** "we find the largest available coefficient in the columns below the pivot equation and then *interchange* the two rows ... Such a process is called *partial pivoting*, since in this case we search only the columns below for the largest element." -- Jain, §7.5.2 (p. 265)
> 
> **In simple words:** Scanning straight down your current column, picking the row with the biggest number in that column, and swapping that entire row up to the diagonal.

> **Complete Pivoting:** "If, on the other hand, we search both columns and rows for the largest element, the procedure is called *complete pivoting*." -- Jain, §7.5.2 (p. 265)
> 
> **In simple words:** Searching the entire remaining submatrix (rows and columns) for the king of all numbers, then doing both a row swap and a column swap to drop it right onto the diagonal.

---

## The Core Idea

### The Pivot Is the Divisor: Why Size Matters
Look back at the elimination multiplier formula from [NM-3.1](NM-3.1_Gauss_Elimination.md):
$$
m_{ik} = \frac{a_{ik}}{a_{kk}}
$$

Notice that $a_{kk}$ (the pivot) sits straight in the denominator. Two failure modes can occur:
1. **The Loud Crash ($a_{kk} = 0$):** Division by zero. The algorithm stops dead in its tracks.
2. **The Silent Killer ($a_{kk} \approx 0$):** If $a_{kk} = 0.00001$, then $m_{ik} \approx 100{,}000$. Every number in row $k$ gets magnified by $100{,}000$ before being subtracted from row $i$. The subtle digits of your original problem are drowned out by floating-point truncation.

The silent failure is the dangerous one. A crash alerts you immediately; a tiny pivot hands you nonsense with a straight face.

### Strategy 1: Partial Pivoting (The Industry Standard)
At step $k$:
1. Look at column $k$.
2. Search through rows $k, k+1, \dots, n$ for the element with the maximum absolute value:
$$
\text{find row } p \text{ such that } |a_{pk}| = \max_{k \le i \le n} |a_{ik}|
$$
3. Swap row $k$ with row $p$.
4. Now your new pivot satisfies $|a_{kk}| \ge |a_{ik}|$ for all $i > k$.
5. Therefore, every single multiplier satisfies:
$$
|m_{ik}| = \left|\frac{a_{ik}}{a_{kk}}\right| \le 1
$$

Because every multiplier has magnitude $\le 1$, you never scale up numbers during elimination. Rounding errors stay safely boxed in!

> [!WARNING] The Classic Search Region Trap
> When searching for the pivot in column $k$, you must search from row $k$ down to row $n$ (including the diagonal itself!). Never start your search at row $k+1$. If the diagonal is already the biggest number, you leave it alone. Searching only below the diagonal and blindly swapping can put a tiny number on the diagonal!

### Strategy 2: Complete Pivoting (Maximum Safety, Heavy Cost)
At step $k$:
1. Search the **entire remaining submatrix** (all rows from $k$ to $n$ and all columns from $k$ to $n$) for the largest absolute entry:
$$
\max_{\substack{k \le i \le n \\ k \le j \le n}} |a_{ij}|
$$
2. Swap rows to bring it to row $k$.
3. Swap columns to bring it to column $k$.

**Why is complete pivoting rarely used?**
- Swapping columns scrambles the order of your unknowns ($x_1, x_2, \dots, x_n$). You must keep track of every swap and unscramble the variable names at the very end.
- It requires $O(n^2)$ comparisons at every step (roughly $O(n^3)$ overall), compared to just $O(n)$ comparisons per step for partial pivoting.
- In practice, partial pivoting already provides near-flawless stability for almost all real-world engineering systems.

### Comparison: Partial vs. Complete Pivoting

| Feature | Partial Pivoting | Complete Pivoting |
| :-- | :-- | :-- |
| **Search Region** | Column $k$ only (rows $k$ to $n$) | Entire submatrix (rows $k$ to $n$, cols $k$ to $n$) |
| **Interchanges** | Row swaps only | Both row and column swaps |
| **Variable Order** | Preserved (unknowns stay in place) | Scrambled (must be restored at the end) |
| **Comparison Cost** | $O(n^2)$ comparisons total | $O(n^3)$ comparisons total |
| **Numerical Stability** | Excellent for almost all problems | The absolute theoretical maximum |
| **Real-world use** | Standard in LAPACK, MATLAB, SciPy | Restricted to specialized research codes |

### Scaled Partial Pivoting: When Raw Size Misleads
Sometimes a row has a small pivot entry in column 1, but all other entries in that row are even smaller! Comparing raw numbers without looking at row scale can be misleading.
In **scaled partial pivoting**, we compute the maximum magnitude of each row $s_i = \max_j |a_{ij}|$, and pick the pivot row that maximizes the relative ratio:
$$
\frac{|a_{ik}|}{s_i}
$$
This prevents rows that were artificially multiplied by large constants from dominating the choice.

### What Pivoting CANNOT Fix: Stability vs. Conditioning
This is the single most tested theoretical distinction in RUET exams:
- **Numerical Stability** is a property of the **algorithm**. Pivoting fixes numerical instability by preventing catastrophic round-off during arithmetic.
- **Ill-Conditioning** is an intrinsic property of the **physical problem itself** (measured by the condition number $\kappa(A)$).

If a physical system is ill-conditioned (meaning the equations represent nearly parallel lines), running Gauss elimination with perfect pivoting will still return an incorrect answer! Pivoting guarantees that your calculations do not invent artificial error; it cannot heal a problem whose physical inputs are inherently touchy.

---

## 🔧 Worked Example (The Tiny Pivot Demonstration)

> **The system (from Jain, Example 7.5):**
> $$
> \begin{aligned}
> 0.000312x_1 + 0.006032x_2 &= 0.003328 \\
> 0.5000x_1 + 0.8942x_2 &= 0.9471
> \end{aligned}
> $$
> The exact analytical solution is $x_1 = 1.0$ and $x_2 = 0.5$. Let's solve this with 4-digit floating-point arithmetic to see what pivoting actually does!

**Let's solve this step by step.**

### Case A: Solving WITHOUT Pivoting (Natural Order)
Look at Row 1: the pivot is $a_{11} = 0.000312$ (tiny!).  
Compute the multiplier to eliminate $x_1$ from Row 2:
$$
m_{21} = \frac{0.5000}{0.000312} \approx 1602.56
$$
Now perform Row 2 operation: $R_2 \leftarrow R_2 - 1602.56 \times R_1$:
- For $x_2$:
$$
0.8942 - 1602.56(0.006032) = 0.8942 - 9.6667 = -8.7725
$$
- For the constant:
$$
0.9471 - 1602.56(0.003328) = 0.9471 - 5.3333 = -4.3862
$$

Back-substituting gives:
$$
x_2 = \frac{-4.3862}{-8.7725} \approx 0.6076 \quad (\text{Wrong! True value is } 0.5)
$$
Now plug $x_2 = 0.6076$ back into Row 1:
$$
0.000312x_1 + 0.006032(0.6076) = 0.003328
$$
$$
0.000312x_1 + 0.003665 = 0.003328 \implies 0.000312x_1 = -0.000337 \implies x_1 \approx -1.0803
$$
The calculated value $x_1 = -1.0803$ is not only completely wrong, it even has the wrong sign! The true answer is $+1.0$.

### Case B: Solving WITH Partial Pivoting (Swap Rows First)
In column 1, compare $|0.000312|$ and $|0.5000|$.  
$0.5000$ is much larger! Swap Row 1 and Row 2 before eliminating:
$$
\begin{aligned}
0.5000x_1 + 0.8942x_2 &= 0.9471 \\
0.000312x_1 + 0.006032x_2 &= 0.003328
\end{aligned}
$$

Now compute the multiplier:
$$
m_{21} = \frac{0.000312}{0.5000} = 0.000624 \quad (\text{Safe! Multiplier is } \le 1)
$$
Perform Row 2 operation: $R_2 \leftarrow R_2 - 0.000624 \times R_1$:
- For $x_2$:
$$
0.006032 - 0.000624(0.8942) = 0.006032 - 0.000558 = 0.005474
$$
- For the constant:
$$
0.003328 - 0.000624(0.9471) = 0.003328 - 0.000591 = 0.002737
$$

Back-substitution:
$$
x_2 = \frac{0.002737}{0.005474} = 0.5000 \quad (\text{Exact!})
$$
Substitute into Row 1:
$$
0.5000x_1 + 0.8942(0.5000) = 0.9471 \implies 0.5000x_1 + 0.4471 = 0.9471
$$
$$
0.5000x_1 = 0.5000 \implies x_1 = 1.0000 \quad (\text{Exact!})
$$

A simple row swap made the difference between total garbage and mathematical perfection!

---

## 🏆 Past Exam Questions

### 2021 Q.7(a): Why Is Pivoting Important? -- [02 marks]

**The question:** Why is pivoting important?

**Tutor explanation & structured answer:**

Every stage of Gauss elimination divides by the pivot element ($a_{kk}$). Pivoting reorders rows or columns so that this divisor is as large in magnitude as possible.

**Two critical reasons:**
1. **Prevents division by zero:** If $a_{kk} = 0$, the elimination step is mathematically impossible and crashes. Swapping rows puts a nonzero entry on the diagonal.
2. **Prevents catastrophic round-off error:** If $a_{kk}$ is tiny, the multiplier $m_{ik} = a_{ik}/a_{kk}$ becomes enormous. Subtracting massively scaled rows causes severe cancellation of significant digits. The calculation finishes but returns completely incorrect answers.

Partial pivoting selects the largest available entry in column $k$ on or below the diagonal and swaps it into place, ensuring $|m_{ik}| \le 1$ at zero extra arithmetic cost.

$$
\boxed{\text{Pivoting avoids a zero or tiny divisor, which is where elimination accuracy is lost}}
$$

---

### 2022 Q.3(c): What Is Pivoting? -- [02 marks]

**The question:** What is pivoting?

**Tutor explanation & structured answer:**

**Definition:**  
In Gaussian elimination, **pivoting** is the process of interchanging rows, or both rows and columns, so that the element chosen as the pivot (the divisor for that stage) has the largest possible absolute value, or at least is not negligibly small.

**Why it is needed:**  
Every elimination step divides by the pivot. If the pivot is $0$, the step is undefined. If the pivot is tiny, the multiplier becomes huge, flooding all subsequent rows with round-off errors.

**The two primary forms:**
1. **Partial Pivoting:** At step $k$, search column $k$ from row $k$ through $n$ for the element with the largest magnitude and swap that row into position $k$. It preserves the order of unknowns and costs only $O(n^2)$ comparisons.
2. **Complete Pivoting:** Search the entire remaining $(n-k+1) \times (n-k+1)$ submatrix for the maximum magnitude entry and swap both rows and columns. It provides maximum stability but scrambles the variable order and costs $O(n^3)$ comparisons.

$$
\boxed{\text{Pivoting reorders rows or columns so the divisor is as large as possible, avoiding a tiny pivot and its round off}}
$$

---

### 2017 Q.4(a): What Are Pivots? Partial vs Complete Pivoting -- [03 marks]

**The question:** What are pivots in solving system of linear equations using elimination methods? What are (i) partial & (ii) complete pivoting?

**Tutor explanation & structured answer:**

**Pivots:**  
In Gauss elimination, a pivot is the diagonal coefficient $a_{kk}$ used at stage $k$ to eliminate the unknown $x_k$ from all rows below it. Because every multiplier takes the form $m_{ik} = a_{ik}/a_{kk}$, the pivot acts as the divisor for the entire stage.

**(i) Partial Pivoting:**  
At stage $k$, we search strictly within column $k$, scanning from row $k$ down to row $n$ for the entry with the largest absolute value. That row is swapped with row $k$.  
- *Key feature:* Only row interchanges are performed, so the order of the variables $(x_1, \dots, x_n)$ remains unchanged.  
- *Advantage:* Guarantees all multipliers satisfy $|m_{ik}| \le 1$ with minimal comparison effort ($O(n^2)$ total).

**(ii) Complete Pivoting:**  
At stage $k$, we search the entire active submatrix (all rows $k$ to $n$ and all columns $k$ to $n$) for the entry with the largest absolute value. That entry is moved to position $(k, k)$ using both a row exchange and a column exchange.  
- *Key feature:* Swapping columns permutes the order of the unknowns, requiring an index tracking table so the final answer vector can be unscrambled.  
- *Cost:* Requires $O(n^3)$ comparisons across the elimination.

---

### 2019 Q.3(b): Discuss Partial and Complete Pivoting in Brief -- [04 marks]

**The question:** Discuss partial and complete pivoting in brief.

**Tutor explanation & structured answer:**

When solving $A\mathbf{x} = \mathbf{b}$ via elimination, selecting the natural diagonal entry as the divisor can lead to numerical instability if that entry is zero or near zero. Pivoting systematically relocates a larger element to the pivot position.

| Comparison Point | Partial Pivoting | Complete Pivoting |
| :-- | :-- | :-- |
| **Search Territory** | Column $k$ only (rows $k$ to $n$) | Full remaining submatrix (rows & cols $k$ to $n$) |
| **Row Swaps?** | Yes | Yes |
| **Column Swaps?** | No | Yes (scrambles unknown sequence) |
| **Multiplier Bound** | $\lvert m_{ik}\rvert \le 1$ | $\lvert m_{ik}\rvert \le 1$ |
| **Computational Cost** | $O(n^2)$ comparisons | $O(n^3)$ comparisons (roughly double work) |
| **Practical Use** | Standard default in engineering | Used only for near-singular research systems |

**Crucial Exam Note on Conditioning:**  
Pivoting improves the **numerical stability of the elimination algorithm**. It does not change the **condition number** $\kappa(A)$ of the matrix. If a physical system is ill-conditioned, pivoting cannot make the solution accurate because the problem itself is hyper-sensitive to error.

---

### Exam Variants at a Glance

| Year | What They Asked | Key Answer / Formula |
|:---|:---|:---|
| **2017 Q.4(a)** | Define pivots, partial & complete pivoting (03 marks) | Search regions, row vs column swaps, multiplier bounds |
| **2019 Q.3(b)** | Discuss partial & complete pivoting in brief (04 marks) | Comparison table, stability vs conditioning distinction |
| **2021 Q.7(a)** | Why is pivoting important? (02 marks) | $\boxed{\text{Pivoting avoids a zero or tiny divisor, which is where elimination accuracy is lost}}$ |
| **2022 Q.3(c)** | What is pivoting? (02 marks) | $\boxed{\text{Pivoting reorders rows or columns so the divisor is as large as possible, avoiding a tiny pivot and its round off}}$ |

---

## ⚡ Quick Review

**The concept in one sentence:** Pivoting swaps rows (or columns) before each elimination step so you never divide by zero or a tiny number that blows up round-off error.

**The multiplier guarantee:**
$$
|m_{ik}| = \left|\frac{a_{ik}}{a_{kk}}\right| \le 1 \quad \text{for all } i > k
$$

**The golden distinction:** Pivoting fixes algorithm stability; it cannot fix problem conditioning.

**Time estimate in exam:** ~3 to 5 minutes to write down a complete 2 to 4 mark answer with definition, search regions, and why it matters.

---

## 🔗 Connected Topics

- [← NM-3.1: Gauss Elimination](NM-3.1_Gauss_Elimination.md) -- the elimination engine where pivoting acts as the safety brake.
- [→ NM-3.3: LU Decomposition](NM-3.3_LU_Decomposition.md) -- storing row permutations as a permutation matrix $P$ such that $PA = LU$.
- [NM-3.7: Ill-Conditioned Systems](NM-3.7_Ill_Conditioned_Systems.md) -- why an ill-conditioned system fools even the best-pivoted elimination.

---

[← Previous: NM-3.1 Gauss Elimination](NM-3.1_Gauss_Elimination.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: NM-3.3 LU Decomposition →](NM-3.3_LU_Decomposition.md)
