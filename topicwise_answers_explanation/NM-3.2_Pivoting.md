---
title: "NM-3.2 · Pivoting"
tags:
  - numerical-methods
  - discrete-mathematics
  - topicwise
---

# NM-3.2 · Pivoting

Every block below is copied from `../answers_explanation/`. The reasoning
is written once, in the year-wise file, and is not restated here.


### [2017 Q.4(a)]

**Question.** What are pivots in solving system of linear equations using elimination methods? What are (i) partial & (ii) complete pivoting?

*[Marks: 03]*

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
value, and exchange it into position $(k,k)$. Only row exchanges are used, so
the order of the unknowns is unchanged. This keeps $\lvert m_{ik}\rvert \le 1$
for all $i > k$, which controls the magnitude of what is subtracted. It costs
$O(n^2)$ comparisons over the whole elimination.

**Complete pivoting.** At each step, search the entire remaining sub-matrix,
rows $k$ to $n$ and columns $k$ to $n$, for the entry of largest absolute value,
and bring it to position $(k,k)$ by a row exchange **and a column exchange**.
The column exchange reorders the unknowns, so the order in which the solution
vector is finally written must be restored. The extra search costs about $n^2$
comparisons *per step*, so $O(n^3)$ over the whole elimination, twice the work
of partial pivoting.

**When the difference matters.** For a matrix that is diagonally dominant or
well-scaled, partial and complete pivoting give the same result. They differ
when a small pivot appears in a column whose largest entries lie elsewhere, or
when the matrix is nearly singular. Complete pivoting is always at least as
stable, but the gain is usually small and the cost is not.

> [!note] Why search *below and including* the diagonal
> On the first step the diagonal itself is a candidate; on later steps the
> entries above it have already been used and are not available. Searching rows
> $k+1$ to $n$ and leaving a small diagonal in place is the single most common
> implementation error, and it silently reintroduces exactly the instability
> pivoting exists to remove.

---

### [2019 Q.3(b)]

**Question.** Discuss partial and complete pivoting in brief.

*[Marks: 04]*

**Solution.**

**Partial pivoting.** At step $k$ of the elimination, search column $k$ of the
rows $k$ through $n$ for the entry of largest absolute value, and exchange it with
the entry in position $(k,k)$ before forming the multipliers. The multiplier is
then

$$m_{ik} = \frac{a_{ik}}{a_{kk}}, \qquad |m_{ik}| \le 1$$

hence no multiplier exceeds one in magnitude, and the rounding introduced by the
multiplier is controlled. Partial pivoting searches one column only, and is
sufficient for the great majority of systems.

**Complete pivoting.** At step $k$, search the whole remaining sub-matrix, rows $k$
through $n$ and columns $k$ through $n$, for the entry of largest absolute value,
and bring it to position $(k,k)$ by a row exchange **and** a column exchange.
Column exchanges reorder the unknowns, so the order in which the solution vector is
written must be restored afterwards. The extra search raises the cost by a factor of
about $n^2$ per step, which is why complete pivoting is reserved for systems that
are nearly singular or where numerical stability is critical.

| | Partial pivoting | Complete pivoting |
| :--- | :--- | :--- |
| Search region | column $k$, rows $k$ to $n$ | sub-matrix, rows and columns $k$ to $n$ |
| Row exchange | yes | yes |
| Column exchange | no | yes, unknown order changes |
| Stability | adequate for most systems | best available |
| Cost | low | higher by a factor of about $n^2$ |

**When it matters.** If the pivot $a_{kk}$ is small relative to the entries below it,
the multiplier $m_{ik}$ is large, and the row $R_i - m_{ik}R_k$ carries a value
dominated by rounding. Choosing the largest available pivot keeps the magnitude of
what is subtracted under control, and prevents a small physical quantity from
being lost against a large one.

> [!warning] What pivoting cannot fix
> Pivoting improves **stability**, not **conditioning**. The condition number
> $\kappa(A)$ is a property of the problem and no reordering changes it.
>
> The practical consequence: a perfectly pivoted elimination of an
> ill-conditioned system returns a confidently wrong answer. Pivoting decides
> whether the arithmetic keeps its digits; it says nothing about whether the
> problem deserves those digits.

> [!note] Scaled pivoting is the compromise that is actually used
> The failure of plain partial pivoting is a row with a large entry elsewhere and a
> small pivot in this column: it is unfairly penalised. Dividing each candidate by
> its own row's largest magnitude first, then comparing, fixes that, and costs one
> pass.
>
> In engineering practice, **scaled partial pivoting** is the default and complete
> pivoting is rare, because the $n^2$ cost per step buys stability that scaled
> partial pivoting already provides for all but nearly singular systems.

---

### [2021 Q.7(a)]

**Question.** Why is pivoting important?

*[Marks: 02, CO: 1]*

**Solution.**

Every elimination step **divides** by the pivot, the element chosen as divisor.
Pivoting reorders rows or columns so that pivot is as large in magnitude as
possible.

**Two reasons.**

1. **A zero pivot stops the method.** If $a_{kk} = 0$, the step is undefined. Row
   interchange usually fixes it.
2. **A tiny pivot destroys accuracy.** If $a_{kk} = 10^{-9}$ while other entries are
   of order 1, then the multiplier $\frac{a_{ik}}{a_{kk}}$ is of order $10^9$, and
   subtracting such numbers loses most of the significant digits. The computation
   still runs and returns a wrong answer.

**Partial pivoting**, the usual choice, selects the largest $\lvert a_{ik}\rvert$ in
column $k$ below the diagonal and swaps it up. It costs one comparison per
candidate and no extra arithmetic.

$$\boxed{\text{Pivoting avoids a zero or tiny divisor, which is where elimination accuracy is lost}}$$

> [!warning] Stability is not conditioning
> Pivoting improves **stability**, not **conditioning**. The condition number
> $\kappa(A)$ is a property of the problem and cannot be changed by reordering.
>
> If $\kappa$ is large, the answer is unreliable no matter how carefully the
> elimination is done. **A perfectly pivoted elimination of an ill-conditioned
> system returns a confidently wrong answer**, which is the dangerous combination.
>
> Compare with Q.4(c) of 2022, where the question defines an ill-conditioned
> system. The two topics meet here and the distinction is the whole point of both.

---

### [2022 Q.3(c)]

**Question.** What is pivoting?

*[Marks: 02, CO: 1]*

**Solution.**

**Definition.** In Gaussian elimination, **pivoting** is interchanging rows, or
columns, so that the element chosen as the **pivot**, which is the next divisor,
is as large as possible in magnitude, or at least not negligibly small.

**Why it is needed.** Every elimination step divides by the pivot. If the pivot is
$0$ the step is impossible. If it is merely tiny, say $10^{-9}$, the multiplier
$a_{ik}/a_{kk}$ becomes enormous, and the elimination floods the remaining rows
with round off.

**Three forms.**

1. **Partial pivoting**, the usual choice. At step $k$, find the largest
   $|a_{ik}|$ in column $k$ below the diagonal and swap that row up. Cost is one
   comparison per candidate, no extra arithmetic, and it is stable in practice.
2. **Scaled partial pivoting**. Divide each candidate by its own row's largest
   magnitude first, then compare, choosing $k$ to maximise
   $$\frac{|a_{ik}|}{\max_j |a_{ij}|}$$.
   This stops a row with large entries but a small pivot from being unfairly
   penalised.
3. **Complete pivoting.** Search the whole remaining submatrix and permute both
   rows and columns. The most stable, but it scrambles the variable order, so it
   is confined largely to research codes.

$$\boxed{\text{Pivoting reorders rows or columns so the divisor is as large as possible, avoiding a tiny pivot and its round off}}$$

> [!warning] Pivoting cannot rescue a singular matrix
> If a whole column of the remaining submatrix is zero, the matrix is singular
> and no rearrangement helps. Pivoting makes a bad pivot large; it cannot
> manufacture a nonzero pivot where none exists.
>
> This is worth separating from **scaling**, which multiplies rows and columns
> by constants. Scaling is a legitimate operation on a system and changes the
> solution consistently. Row swapping changes nothing at all about the solution,
> which is why pivoting is always safe and scaling needs care.

> [!note] The one-line test for whether you need it
> Look at the first column. If the leading entry is smaller in magnitude than
> something below it, partial pivoting would have chosen differently. That single
> comparison costs nothing and covers the large majority of practical cases.

---
