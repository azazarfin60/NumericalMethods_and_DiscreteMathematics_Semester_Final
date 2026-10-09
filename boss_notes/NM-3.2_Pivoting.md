[← Previous: NM-2 Lower Tier](NM-2_Lower_Secant_and_Polynomial_Roots.md) | [🏠 Index](00_Index.md) | [Next: NM-3.5 Gauss-Seidel Iteration →](NM-3.5_Gauss_Seidel_Iteration.md)

---

# NM-3.2: Pivoting
> **Section:** A (Numerical Methods) | **Priority:** 🔴 | **Exam Frequency:** 4/8 years
> **Sources:** Jain Ch.7 §7.5.2, Topicwise NM-3.2, Shishir Notes §02

## Why This Topic Matters

Pivoting appears in four papers, always as a short theory question. The shapes are: define pivoting, discuss partial and complete pivoting, or say why pivoting matters. The marks are cheap. Learn one definition, the two search rules, and the stability-versus-conditioning distinction, and all four questions are covered. The topic also pays rent in every elimination answer: any Gauss elimination solution in this course is expected to mention pivoting.

---

## 📝 Key Definitions

> **Pivot:** "the first equation in the system (7.30) is called the *pivot equation*, and $a_{11}$ is called the *pivot* ... The method obviously fails if $a_{11} = 0$." — Jain, §7.5 (p. 264)

> **Necessity for pivoting:** "We now come to the important case of the pivot being zero or very close to zero. If the *pivot is zero*, the *entire process fails* and if it is close to zero, round-off errors may occur. These problems can be avoided by adopting a procedure called *pivoting*." — Jain, §7.5.2 (p. 265)

> **Partial pivoting:** "we find the largest available coefficient in the columns below the pivot equation and then *interchange* the two rows ... Such a process is called *partial pivoting*, since in this case we search only the columns below for the largest element." — Jain, §7.5.2 (p. 265)

> **Complete pivoting:** "If, on the other hand, we search both columns and rows for the largest element, the procedure is called *complete pivoting*." — Jain, §7.5.2 (p. 265)

---

## Core Theory

### The pivot is the divisor, and that is the whole problem

Every elimination step divides. At step $k$ the entry $a_{kk}$ is the pivot, and the multiplier that clears the entries below it is

$$
m_{ik} = \frac{a_{ik}}{a_{kk}}
$$

The pivot sits in the denominator of every multiplier in that column. So a small pivot forces large multipliers. Each multiplier scales what gets subtracted, and subtracting large nearly equal numbers cancels away the significant digits. The computation still runs. It returns a wrong answer with no warning.

Two failure sizes exist, and they are not equally dangerous:

1. **A zero pivot stops the method loud.** If $a_{kk} = 0$ the step is undefined. A row interchange usually fixes it.
2. **A tiny pivot kills accuracy silent.** If $a_{kk} = 10^{-9}$ while other entries are of order $1$, then $m_{ik}$ is of order $10^9$. The subtraction floods the remaining rows with round off error.

The silent failure is the dangerous one. A zero pivot is obvious; a tiny pivot is not.

### Partial pivoting: the standard safeguard

At step $k$, search column $k$ in rows $k$ through $n$ for the entry of largest absolute value. Exchange that row into position $k$. Then form the multipliers.

The search must include the diagonal itself, rows $k$ to $n$. On later steps the entries above the diagonal have already been used, so they are not candidates. Searching only rows $k+1$ to $n$ and leaving a small diagonal in place is the single most common implementation error. It silently reintroduces the instability pivoting exists to remove.

Two properties make partial pivoting the default choice:

- Only row exchanges are used, so the order of the unknowns never changes.
- Every multiplier satisfies $|m_{ik}| \le 1$, so nothing larger than what is already in the matrix gets subtracted.

The cost is one comparison per candidate row, and no extra arithmetic.

### Complete pivoting: the expensive option

At step $k$, search the whole remaining sub-matrix, rows $k$ to $n$ and columns $k$ to $n$, for the entry of largest absolute value. Bring it to position $(k, k)$ by a row exchange **and** a column exchange.

The column exchange reorders the unknowns. The order in which the solution vector is finally written must be restored afterwards. The extra search costs about $n^2$ comparisons per step, against roughly $n$ for partial pivoting. So complete pivoting is reserved for systems that are nearly singular or where stability is critical.

### Scaled partial pivoting: the compromise that is actually used

Plain partial pivoting can treat a row unfairly. A row with large entries elsewhere and a small pivot in this column looks bad, even though its pivot is reasonable for its own scale.

The fix is to divide each candidate by its own row's largest magnitude first, then compare. Choose the row $k$ maximising

$$
\frac{\left|a_{ik}\right|}{\max_j\left|a_{ij}\right|}
$$

In engineering practice, scaled partial pivoting is the default and complete pivoting is rare. The $n^2$ cost per step buys stability that scaled partial pivoting already provides for all but nearly singular systems.

### What pivoting cannot fix

Pivoting improves **stability**, not **conditioning**. The condition number $\kappa(A)$ is a property of the problem. No reordering changes it.

The practical consequence is sharp. A perfectly pivoted elimination of an ill-conditioned system returns a confidently wrong answer. Pivoting decides whether the arithmetic keeps its digits. It says nothing about whether the problem deserves those digits.

Pivoting also cannot rescue a singular matrix. If a whole column of the remaining submatrix is zero, no rearrangement helps. Pivoting makes a bad pivot large. It cannot manufacture a nonzero pivot where none exists.

---

## Worked Example (Textbook Demonstration: Jain, Example 7.5)

This is the textbook's own demonstration of why the tiny-pivot case matters. The exact solution is $x_1 = 1$ and $x_2 = 0.5$.

**With pivoting.** Swap the rows so the larger coefficient leads:

$$
\begin{aligned}
0.5000x_1 + 0.8942x_2 &= 0.9471 \\
0.000312x_1 + 0.006032x_2 &= 0.003328
\end{aligned}
$$

Eliminate $x_1$ from row 2. The multiplier is $\frac{0.000312}{0.5000} = 0.000624$, so

$$
\begin{aligned}
0.5000x_1 + 0.8942x_2 &= 0.9471 \\
0.005474x_2 &= 0.002737
\end{aligned}
$$

Back substitution gives $x_2 = 0.5$ and $x_1 = 1.0$. Both correct.

**Without pivoting.** Use the printed order:

$$
\begin{aligned}
0.000312x_1 + 0.006032x_2 &= 0.003328 \\
0.5000x_1 + 0.8942x_2 &= 0.9471
\end{aligned}
$$

The multiplier is $\frac{0.5000}{0.000312} = 1602.56$. Eliminating $x_1$ gives

$$
\begin{aligned}
0.000312x_1 + 0.006032x_2 &= 0.003328 \\
-8.7725x_2 &= -5.3300
\end{aligned}
$$

Back substitution gives $x_2 = 0.6076$ and $x_1 = -1.0803$. Both wrong, and the second is wrong by more than its own magnitude. The effect of pivoting is clearly seen.

---

## Exam Variants

| Year | Question | Data Given | Key Answer |
|:---|:---|:---|:---|
| 2017 Q.4(a) | Define pivots, partial and complete pivoting | none (03 marks) | Pivot is the divisor; partial searches a column, complete searches the sub-matrix |
| 2019 Q.3(b) | Discuss partial and complete pivoting in brief | none (04 marks) | Search region, exchanges, stability, cost |
| 2021 Q.7(a) | Why is pivoting important? | none (02 marks) | $\boxed{\text{Pivoting avoids a zero or tiny divisor, which is where elimination accuracy is lost}}$ |
| 2022 Q.3(c) | What is pivoting? | none (02 marks) | $\boxed{\text{Pivoting reorders rows or columns so the divisor is as large as possible, avoiding a tiny pivot and its round off}}$ |

---

## 🏆 Golden Questions (Past Exam Archive)

### 🎯 What are pivots in solving system of linear equations using elimination methods? What are (i) partial & (ii) complete pivoting?
> **Appeared:** 2017 Q.4(a) — (03 marks)

**Full Answer:**

**Pivots.** In Gauss elimination, the pivot is the element used to eliminate the entries below it. At step $k$ the entry $a_{kk}$, in the $k$-th row and $k$-th column of the transformed matrix, is the pivot. The multipliers are

$$
m_{ik} = \frac{a_{ik}}{a_{kk}}
$$

The pivot enters the denominator of every multiplier at that step. A small pivot produces large multipliers, which amplify rounding error. That is the problem pivoting is designed to prevent.

**(i) Partial pivoting.** At each step, search the $k$-th column below and including the diagonal, rows $k$ to $n$, for the entry of largest absolute value. Exchange it into position $(k, k)$. Only row exchanges are used, so the order of the unknowns is unchanged. This keeps $|m_{ik}| \le 1$ for all $i > k$, which controls the magnitude of what is subtracted. The cost is $O(n^2)$ comparisons over the whole elimination.

**(ii) Complete pivoting.** At each step, search the entire remaining sub-matrix, rows $k$ to $n$ and columns $k$ to $n$, for the entry of largest absolute value. Bring it to position $(k, k)$ by a row exchange and a column exchange. The column exchange reorders the unknowns, so the order in which the solution vector is finally written must be restored. The extra search costs about $n^2$ comparisons per step, so $O(n^3)$ over the whole elimination, twice the work of partial pivoting.

**When the difference matters.** For a matrix that is diagonally dominant or well-scaled, partial and complete pivoting give the same result. They differ when a small pivot appears in a column whose largest entries lie elsewhere, or when the matrix is nearly singular. Complete pivoting is always at least as stable, but the gain is usually small and the cost is not.

> [!WARNING]
> Why search below **and including** the diagonal. On the first step the diagonal itself is a candidate. On later steps the entries above it have already been used. Searching rows $k+1$ to $n$ and leaving a small diagonal in place is the single most common implementation error, and it silently reintroduces exactly the instability pivoting exists to remove.

---

### 🎯 Discuss partial and complete pivoting in brief.
> **Appeared:** 2019 Q.3(b) — (04 marks)

**Full Answer:**

**Partial pivoting.** At step $k$ of the elimination, search column $k$ of the rows $k$ through $n$ for the entry of largest absolute value. Exchange it with the entry in position $(k, k)$ before forming the multipliers. The multiplier is then

$$
m_{ik} = \frac{a_{ik}}{a_{kk}}, \qquad |m_{ik}| \le 1
$$

So no multiplier exceeds one in magnitude, and the rounding introduced by the multiplier is controlled. Partial pivoting searches one column only, and it is sufficient for the great majority of systems.

**Complete pivoting.** At step $k$, search the whole remaining sub-matrix, rows $k$ through $n$ and columns $k$ through $n$, for the entry of largest absolute value. Bring it to position $(k, k)$ by a row exchange **and** a column exchange. Column exchanges reorder the unknowns, so the order in which the solution vector is written must be restored afterwards. The extra search raises the cost by a factor of about $n^2$ per step. That is why complete pivoting is reserved for systems that are nearly singular or where numerical stability is critical.

| | Partial pivoting | Complete pivoting |
| :--- | :--- | :--- |
| Search region | column $k$, rows $k$ to $n$ | sub-matrix, rows and columns $k$ to $n$ |
| Row exchange | yes | yes |
| Column exchange | no | yes, unknown order changes |
| Stability | adequate for most systems | best available |
| Cost | low | higher by a factor of about $n^2$ |

**When it matters.** If the pivot $a_{kk}$ is small relative to the entries below it, the multiplier $m_{ik}$ is large. The row $R_i - m_{ik}R_k$ then carries a value dominated by rounding. Choosing the largest available pivot keeps the magnitude of what is subtracted under control, and prevents a small physical quantity from being lost against a large one.

> [!WARNING]
> What pivoting cannot fix. Pivoting improves stability, not conditioning. The condition number $\kappa(A)$ is a property of the problem and no reordering changes it. A perfectly pivoted elimination of an ill-conditioned system returns a confidently wrong answer. Pivoting decides whether the arithmetic keeps its digits; it says nothing about whether the problem deserves those digits.

> [!NOTE]
> Scaled pivoting is the compromise that is actually used. The failure of plain partial pivoting is a row with a large entry elsewhere and a small pivot in this column: it is unfairly penalised. Dividing each candidate by its own row's largest magnitude first, then comparing, fixes that, and costs one pass. In practice, scaled partial pivoting is the default and complete pivoting is rare, because the $n^2$ cost per step buys stability that scaled partial pivoting already provides for all but nearly singular systems.

---

### 🎯 Why is pivoting important?
> **Appeared:** 2021 Q.7(a) — (02 marks, CO: 1)

**Full Answer:**

Every elimination step **divides** by the pivot, the element chosen as divisor. Pivoting reorders rows or columns so that pivot is as large in magnitude as possible.

**Two reasons.**

1. **A zero pivot stops the method.** If $a_{kk} = 0$, the step is undefined. Row interchange usually fixes it.
2. **A tiny pivot destroys accuracy.** If $a_{kk} = 10^{-9}$ while other entries are of order 1, then the multiplier $\frac{a_{ik}}{a_{kk}}$ is of order $10^9$. Subtracting such numbers loses most of the significant digits. The computation still runs and returns a wrong answer.

**Partial pivoting**, the usual choice, selects the largest $\lvert a_{ik}\rvert$ in column $k$ below the diagonal and swaps it up. It costs one comparison per candidate and no extra arithmetic.

$$
\boxed{\text{Pivoting avoids a zero or tiny divisor, which is where elimination accuracy is lost}}
$$

> [!WARNING]
> Stability is not conditioning. Pivoting improves stability, not conditioning. The condition number $\kappa(A)$ is a property of the problem and cannot be changed by reordering. If $\kappa$ is large, the answer is unreliable no matter how carefully the elimination is done. **A perfectly pivoted elimination of an ill-conditioned system returns a confidently wrong answer**, which is the dangerous combination. Compare with Q.4(c) of 2022, which defines an ill-conditioned system. The two topics meet here, and the distinction is the whole point of both.

---

### 🎯 What is pivoting?
> **Appeared:** 2022 Q.3(c) — (02 marks, CO: 1)

**Full Answer:**

**Definition.** In Gaussian elimination, **pivoting** is the act of interchanging rows, or columns, so that the element chosen as the **pivot** (the next divisor) is as large as possible in magnitude, or at least not negligibly small.

**Why it is needed.** Every elimination step divides by the pivot. If the pivot happens to be $0$ the step is impossible. If it is merely tiny, say $10^{-9}$, the multiplier $a_{ik}/a_{kk}$ becomes enormous, and the elimination floods the remaining rows with round off error.

**Two kinds.**

1. **Partial pivoting**, the usual choice. At step $k$, find the largest $\left|a_{ik}\right|$ in column $k$ below the diagonal and swap that row up. Cost is one comparison per candidate, no extra arithmetic, and it is provably stable in practice.
2. **Scaled pivoting.** Divide each candidate by its row's largest magnitude first, then compare. This stops a row with large entries but a small pivot from being unfairly penalised.

**Scaled partial pivoting** chooses $k$ maximising

$$
\frac{\left|a_{ik}\right|}{\max_j\left|a_{ij}\right|}
$$

**A third form.** Complete pivoting searches the whole remaining submatrix and permutes both rows and columns. It is the most stable but costs more and scrambles the variable order, so its use is confined largely to research codes.

**When pivoting cannot help.** If a whole column of the remaining submatrix is zero, the matrix is singular and no rearrangement helps. Pivoting cannot create a nonzero pivot where none exists.

$$
\boxed{\text{Pivoting reorders rows or columns so the divisor is as large as possible, avoiding a tiny pivot and its round off}}
$$

> [!WARNING]
> Pivoting cannot rescue a singular matrix. If a whole column of the remaining submatrix is zero, the matrix is singular and no rearrangement helps. Pivoting makes a bad pivot large; it cannot manufacture a nonzero pivot where none exists. This is worth separating from **scaling**, which multiplies rows and columns by constants. Scaling is a legitimate operation on a system and changes the solution consistently. Row swapping changes nothing at all about the solution, which is why pivoting is always safe and scaling needs care.

> [!NOTE]
> The one-line test for whether you need it. Look at the first column. If the leading entry is smaller in magnitude than something below it, partial pivoting would have chosen differently. That single comparison costs nothing and covers the large majority of practical cases.

---

## ⚡ Exam Tips & Common Mistakes

1. Write the multiplier formula $m_{ik} = a_{ik}/a_{kk}$ first. It is one line, and it makes the whole "why" answer write itself.
2. State the search region precisely for both kinds: column $k$ rows $k$ to $n$ for partial, the whole sub-matrix rows and columns $k$ to $n$ for complete. Vague search regions lose the mark.
3. Mention that complete pivoting reorders the unknowns and the answer vector must be restored. That is the detail that separates a full answer from a partial one.
4. Always add the stability-versus-conditioning sentence. It is the standard examiner follow-up, and it costs one line.
5. Never claim pivoting fixes a singular system. Say instead that pivoting cannot create a nonzero pivot where none exists.

## 🔗 Related Topics

- [NM-3_Lower: Gauss Elimination, LU, Jacobi, Relaxation](NM-3_Lower_Gauss_Elim_LU_Jacobi_Relaxation.md) — partial pivoting is step one of a safe elimination, shown in action there
- [NM-3.5: Gauss-Seidel Iteration](NM-3.5_Gauss_Seidel_Iteration.md) — the iterative alternative, where row order decides convergence instead of stability
- [NM-3.8: Circuit Applications](NM-3.8_Circuit_Applications.md) — mesh and nodal systems that these methods solve

---

[← Previous: NM-2 Lower Tier](NM-2_Lower_Secant_and_Polynomial_Roots.md) | [🏠 Index](00_Index.md) | [Next: NM-3.5 Gauss-Seidel Iteration →](NM-3.5_Gauss_Seidel_Iteration.md)
