---
title: "NM-4.10 · Gauss Forward / Backward & Stirling's Formulas"
tags:
  - numerical-methods
  - discrete-mathematics
  - topicwise
---


[🏠 Subtopic Index](00_Index.md) | [← Prev: NM-4.9 Newton's Divided Difference / General Interpolation](NM-4.9_Newtons_Divided_Difference_and_General_Interpolation.md) | [Next: NM-4.11 Difference Table Formation & Applications →](NM-4.11_Difference_Table_Formation_and_Applications.md)

---

# NM-4.10 · Gauss Forward / Backward & Stirling's Formulas

Every block below is copied from `../answers_explanation/`. The reasoning
is written once, in the year-wise file, and is not restated here.


### [2021 Q.4(b)]

**Question.** From the following table, calculate the value of $e^{1.17}$ using Gauss' forward formula.

*[Marks: 05, CO: 2]*

**Solution.**

| $x$ | 1.00 | 1.05 | 1.10 | 1.15 | 1.20 | 1.25 | 1.30 |
| --- | --: | --: | --: | --: | --: | --: | --: |
| $e^x$ | 2.7183 | 2.8577 | 3.0042 | 3.1582 | 3.3201 | 3.4903 | 3.6693 |

**Step 1. Choose origin $x_0$ and compute $p$.**
The target is $x = 1.17$ and step size $h = 0.05$.
Gauss' forward formula is a central-difference formula designed for $0 \le p \le 1$ (ideally $0 \le p \le 0.5$).
Choose origin $x_0 = 1.15$. Then:

$$
p = \frac{x - x_0}{h} = \frac{1.17 - 1.15}{0.05} = \frac{0.02}{0.05} = 0.4
$$

**Step 2. Difference table.**

| $x$ | 1.00 | 1.05 | 1.10 | 1.15 | 1.20 | 1.25 | 1.30 |
| --- | --: | --: | --: | --: | --: | --: | --: |
| $y$ | 2.7183 | 2.8577 | 3.0042 | 3.1582 | 3.3201 | 3.4903 | 3.6693 |
| $\Delta y$ | 0.1394 | 0.1465 | 0.1540 | 0.1619 | 0.1702 | 0.1790 | |
| $\Delta^2 y$ | 0.0071 | 0.0075 | 0.0079 | 0.0083 | 0.0088 | | |
| $\Delta^3 y$ | 0.0004 | 0.0004 | 0.0004 | 0.0005 | | | |
| $\Delta^4 y$ | 0.0000 | 0.0000 | 0.0001 | | | | |
| $\Delta^5 y$ | 0.0000 | 0.0001 | | | | | |
| $\Delta^6 y$ | 0.0001 | | | | | | |

**Step 3. Collect the central path differences.**
The central difference path traverses in a zigzag pattern:
$y_0 \to \Delta y_0 \to \Delta^2 y_{-1} \to \Delta^3 y_{-1} \to \Delta^4 y_{-2}$:

$$
y_0 = 3.1582, \quad \Delta y_0 = 0.1619, \quad \Delta^2 y_{-1} = 0.0079, \quad \Delta^3 y_{-1} = 0.0004, \quad \Delta^4 y_{-2} = 0.0000
$$

**Step 4. Evaluate the terms ($p = 0.4$).**

Gauss' forward interpolation formula is:

$$
y_p = y_0 + p\Delta y_0 + \frac{p(p-1)}{2!}\Delta^2 y_{-1} + \frac{(p+1)p(p-1)}{3!}\Delta^3 y_{-1} + \frac{(p+1)p(p-1)(p-2)}{4!}\Delta^4 y_{-2} + \cdots
$$

| Term | Algebraic form | Working | Value | Running sum |
| :-- | :-- | :-- | --: | --: |
| $T_0$ | $y_0$ | $3.1582$ | $3.1582000$ | $3.1582000$ |
| $T_1$ | $p\Delta y_0$ | $0.4(0.1619)$ | $+0.0647600$ | $3.2229600$ |
| $T_2$ | $\frac{p(p-1)}{2}\Delta^2 y_{-1}$ | $\frac{0.4(-0.6)}{2}(0.0079) = -0.12(0.0079)$ | $-0.0009480$ | $3.2220120$ |
| $T_3$ | $\frac{(p+1)p(p-1)}{6}\Delta^3 y_{-1}$ | $\frac{(1.4)(0.4)(-0.6)}{6}(0.0004) = -0.056(0.0004)$ | $-0.0000224$ | $3.2219896$ |
| $T_4$ | $\frac{(p+1)p(p-1)(p-2)}{24}\Delta^4 y_{-2}$ | $\frac{(1.4)(0.4)(-0.6)(-1.6)}{24}(0.0000)$ | $0$ | $3.2219896$ |

$$\boxed{e^{1.17} \approx 3.22199}$$

> [!note] The running column is the check that makes the table trustworthy
> Every term is a product of a coefficient and a central-difference entry. Adding
> them in a running total, as the last column does, means a single wrong cell shows
> up immediately as a wrong final sum, and you can back up the terms one at a
> time until it is found.
>
> It also shows *where* to stop. Here the $\Delta^4$ term is zero and the fifth
> would be smaller still, so the sum has converged at three significant
> contributions. The differences shrinking by roughly a factor of 10 to 20 per row is
> the visible signature of a well-behaved function sampled finely.

> [!info] Check by two independent routes
> **Lagrange on the same seven points** gives $3.22199020928$, which agrees to the
> seventh decimal. Lagrange on the nearest four points ($1.05, 1.10, 1.15, 1.20$)
> gives $3.2219896$, identical to the central difference result.
>
> **Against the true value.** $e^{1.17} = 3.2219926385$, so the error is
> $3.04 \times 10^{-6}$. The whole error comes from the table: those $e^x$ values
> are rounded to four decimals, and each carries an error up to $5\times10^{-5}$.
> Interpolating rounded data cannot beat the rounding in the data.

> [!note] Why Gauss' central difference formula is superior here
> Because $x = 1.17$ sits near the middle of the table, choosing $x_0 = 1.15$ gives
> a small interpolation parameter $p = 0.4$ ($0 \le p \le 0.5$). Gauss' forward formula
> draws differences along a central zigzag trajectory, ensuring balanced support from
> points on both sides of $x_0$.
>
> In contrast, using Newton's forward formula from $x_0 = 1.00$ requires $p = 3.4$,
> causing polynomial terms to grow large before cancelling, which degrades numerical stability.
> Central difference formulas like Gauss forward eliminate this issue.

---

[🏠 Subtopic Index](00_Index.md) | [← Prev: NM-4.9 Newton's Divided Difference / General Interpolation](NM-4.9_Newtons_Divided_Difference_and_General_Interpolation.md) | [Next: NM-4.11 Difference Table Formation & Applications →](NM-4.11_Difference_Table_Formation_and_Applications.md)
