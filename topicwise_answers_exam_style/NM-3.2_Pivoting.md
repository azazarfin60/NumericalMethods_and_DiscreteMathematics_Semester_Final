---
title: "NM-3.2 · Pivoting"
tags:
  - numerical-methods
  - discrete-mathematics
  - topicwise
---

# NM-3.2 · Pivoting

Every block below is copied from `../answers_exam_style/`, which is the
only place an answer is authored. A number here is the same number, character
for character, as the one it came from.


### [2017 Q.4(a)]

**Question.** What are pivots in solving system of linear equations using elimination methods? What are (i) partial & (ii) complete pivoting?

**Solution.**

**Pivots.** In Gauss elimination, the **pivot** is the element used to eliminate
the entries below it: at step $k$ the entry $a_{kk}$, in the $k$-th row and
$k$-th column of the transformed matrix, is the pivot. The multipliers are

$$m_{ik} = \frac{a_{ik}}{a_{kk}}$$

and the pivot enters the denominator of every multiplier at that step. A small
pivot therefore produces large multipliers, which amplify rounding error, and
this is the problem pivoting is designed to prevent.

**Partial pivoting.** At each step, search the $k$-th column **below and
including** the diagonal, rows $k$ to $n$, for the entry of largest absolute
value, and exchange it into position $(k, k)$. Only row exchanges are used, so
the order of the unknowns is unchanged. This is sufficient to keep
$|m_{ik}| \le 1$ for all $i > k$, which controls the magnitude of what is
subtracted.

**Complete pivoting.** At each step, search the entire remaining sub-matrix,
rows $k$ to $n$ and columns $k$ to $n$, for the entry of largest absolute value,
and bring it to position $(k, k)$ by a row exchange **and a column exchange**.
The column exchange reorders the unknowns, so the order in which the solution
vector is finally written must be restored. The extra search costs about $n^2$
comparisons per step, so complete pivoting is reserved for systems that are
nearly singular or where stability is critical.

**When the difference matters.** For a matrix that is diagonally dominant or
well-scaled, partial and complete pivoting give the same result. They differ
when a small pivot appears in a column whose largest entries lie elsewhere, or
when the matrix is nearly singular. Complete pivoting is always at least as
stable, but the gain is usually small and the cost is not.

---

### [2019 Q.3(b)]

**Question.** Discuss partial and complete pivoting in brief.

**Solution.**

**Partial pivoting.** At step $k$ of the elimination, search column $k$ of the
rows $k$ through $n$ for the entry of largest absolute value, and exchange it
with the entry in position $(k,k)$ before forming the multipliers. The
multiplier is then

$$m_{ik} = \frac{a_{ik}}{a_{kk}}, \qquad |m_{ik}| \le 1$$

hence no multiplier exceeds one in magnitude, and the rounding introduced by the
multiplier is controlled. Partial pivoting searches one column only, and is
sufficient for the great majority of systems.

**Complete pivoting.** At step $k$, search the whole remaining sub-matrix, rows
$k$ through $n$ and columns $k$ through $n$, for the entry of largest absolute
value, and bring it to position $(k,k)$ by a row exchange **and** a column
exchange. Column exchanges reorder the unknowns, so the order in which the
solution vector is written must be restored afterwards. The extra search raises
the cost by a factor of about $n^2$ per step, which is why complete pivoting is
reserved for systems that are nearly singular or where numerical stability is
critical.

**Comparison.**

| | Partial pivoting | Complete pivoting |
| :--- | :--- | :--- |
| Search region | column $k$, rows $k$ to $n$ | sub-matrix, rows and columns $k$ to $n$ |
| Row exchange | yes | yes |
| Column exchange | no | yes, unknown order changes |
| Stability | adequate for most systems | best available |
| Cost | low | higher by a factor of about $n^2$ |

**When it matters.** If the pivot $a_{kk}$ is small relative to the entries below
it, the multiplier $m_{ik}$ is large, and the row $R_i - m_{ik}R_k$ carries a
value dominated by rounding. Choosing the largest available pivot keeps the
magnitude of what is subtracted under control, and prevents a small physical
quantity from being lost against a large one.

---

### [2021 Q.7(a)]

**Question.** Why is pivoting important?

**Solution.**

Every elimination step **divides** by the pivot, the element chosen as divisor.
Pivoting reorders rows or columns so that pivot is as large in magnitude as
possible.

**Two reasons.**

1. **A zero pivot stops the method.** If $a_{kk} = 0$, the step is undefined.
   Row interchange usually fixes it.
2. **A tiny pivot destroys accuracy.** If $a_{kk} = 10^{-9}$ while other entries are
   of order 1, then the multiplier $\frac{a_{ik}}{a_{kk}}$ is of order $10^9$, and
   subtracting such numbers loses most of the significant digits. The computation
   still runs and returns a wrong answer.

**Partial pivoting**, the usual choice, selects the largest $\lvert a_{ik}\rvert$ in
column $k$ below the diagonal and swaps it up. It costs one comparison per candidate
and no extra arithmetic.

**Important limit.** Pivoting improves **stability**, not **conditioning**. The
condition number $\kappa(A)$ is a property of the problem and cannot be changed by
reordering. If $\kappa$ is large, the answer is unreliable no matter how carefully
the elimination is done.

$$
\boxed{\text{Pivoting avoids a zero or tiny divisor, which is where elimination accuracy is lost}}
$$

---

### [2022 Q.3(c)]

**Question.** What is pivoting?

**Solution.**

**Definition.** In Gaussian elimination, **pivoting** is the act of interchanging
rows, or columns, so that the element chosen as the **pivot** (the next divisor)
is as large as possible in magnitude, or at least not negligibly small.

**Why it is needed.** Every elimination step divides by the pivot. If the pivot
happens to be $0$ the step is impossible. If it is merely tiny, say $10^{-9}$, the
multiplier $a_{ik}/a_{kk}$ becomes enormous and the elimination floods the
remaining rows with round off error.

**Two kinds.**

1. **Partial pivoting**, the usual choice: at step $k$, find the largest
   $\left|a_{ik}\right|$ in column $k$ below the diagonal and swap that row up.
   Cost is one comparison per candidate, no extra arithmetic, and it is provably
   stable in practice.
2. **Scaled pivoting**: divide each candidate by its row's largest magnitude
   first, then compare. This stops a row with large entries but a small pivot
   from being unfairly penalised.

**Scaled partial pivoting** chooses $k$ maximising
$\dfrac{\left|a_{ik}\right|}{\max_j\left|a_{ij}\right|}$.

**A third form.** Complete pivoting searches the whole remaining submatrix and
permutes both rows and columns. It is the most stable but costs more and scrambles
the variable order, so its use is confined largely to research codes.

**When pivoting cannot help.** If a whole column of the remaining submatrix is
zero, the matrix is singular and no rearrangement helps. Pivoting cannot create a
nonzero pivot where none exists.

$$
\boxed{\text{Pivoting reorders rows or columns so the divisor is as large as possible, avoiding a tiny pivot and its round off}}
$$

---
