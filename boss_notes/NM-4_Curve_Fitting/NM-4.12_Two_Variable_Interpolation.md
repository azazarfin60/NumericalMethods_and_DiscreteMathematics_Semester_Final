[← Previous: NM-4.11 Difference Tables](NM-4.11_Difference_Tables.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: NM-5 Integration Overview →](../NM-5_Integration/_Topic_Overview.md)

---

# NM-4.12: Two-Variable Interpolation (Double Interpolation)

> ⚫ **Never examined.** This note exists for reading flow and syllabus completeness. Skim it to understand the concept, but do not spend your valuable revision hours memorizing derivations here.

## What This Is

All the interpolation methods we studied so far (Lagrange, Newton forward, backward, divided differences) dealt with a function of a single independent variable $y = f(x)$. But in electrical engineering, many physical quantities depend on two variables at once: for example, the electric potential $V(x, y)$ across a 2D conductive sheet, transistor current $I_D(V_{GS}, V_{DS})$, or antenna gain $G(\theta, \phi)$ in spherical coordinates.

When a function depends on two variables $z = f(x, y)$ given on a grid of points, how do we estimate an intermediate value $z(x^*, y^*)$?

---

## The Key Idea: Successive 1D Interpolation

Instead of deriving complicated, multi-dimensional formulas, the standard numerical technique is **successive one-dimensional interpolation** (often called *double interpolation* or *bilinear/bicubic interpolation*):

1. **Step 1 (Interpolate along $x$):** Hold $y$ constant along each row. Use standard 1D linear or polynomial interpolation along $x$ to evaluate $z$ at your target $x^*$ for every row. This condenses the 2D grid into a single column of values at $x = x^*$.
2. **Step 2 (Interpolate along $y$):** Now take that new column and perform one final 1D interpolation along the $y$-direction to find the value at your target $y^*$.

### Quick Illustrative Example (from Jain §3.12)

Suppose you have a 2D table of $z$ values for grid points of $x$ and $y$, and you want $z(2.5, 1.5)$:
- First, you interpolate across each row at $x = 2.5$. That gives you a single list of intermediate values $z(2.5, y_j)$ for each $y_j$.
- Next, you interpolate down that list at $y = 1.5$. That gives you your final estimate $z(2.5, 1.5)$.

This decoupled approach means you never need to learn new formulas: any 1D method you already know (linear, Lagrange, or Newton) can be applied in succession.

---

## 🔗 Move On

This subtopic has never appeared in any RUET semester final exam from 2017 to 2024. If you are preparing for exams, move directly to [NM-5: Numerical Integration](../NM-5_Integration/_Topic_Overview.md).

---

[← Previous: NM-4.11 Difference Tables](NM-4.11_Difference_Tables.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: NM-5 Integration Overview →](../NM-5_Integration/_Topic_Overview.md)
