# NM-6: Optimization

> **Section:** Section A (Numerical Methods)
> **Subtopics in this folder:** 3 files (NM-6.1 through NM-6.3)
> **Exam weight:** Appears in 2/8 papers (25% frequency), worth 5 to 6 marks when tested (Question 5 or Question 6 in Section A).

---

## 📖 How to Read This Topic

Engineers constantly seek optimal solutions. You want to maximize the efficiency of an antenna, maximize signal-to-noise ratio, or minimize the power dissipation and silicon area of a circuit.

When an objective function is given, numerical optimization tackles it in two distinct ways:

1. **Continuous Functions (NM-6.1 and NM-6.2):**
   When you have an explicit mathematical formula $f(x)$, finding a peak or valley means finding where the slope is zero: $f'(x) = 0$. We adapt Newton-Raphson from root finding to solve $f'(x) = 0$, dividing by the second derivative $f''(x)$. Before computing, you must also recognize whether any restrictions bind your variables (constrained versus unconstrained).

2. **Sampled Tabulated Data (NM-6.3):**
   In real life, you often have only discrete sensor readings without an analytical formula. To find where the measured quantity reaches its peak, you build a finite difference table, construct the interpolating polynomial derivative, and solve for the fractional step $q$ where $\frac{dy}{dx} = 0$.

Read the subtopics in this natural order:
- **NM-6.1** sets the conceptual foundation: unconstrained versus constrained optimization, stationarity tests ($\nabla f = 0$ versus KKT conditions), and why boundary constraints matter.
- **NM-6.2** covers **One-Dimensional Unconstrained Optimization**: Newton's method applied to derivatives, why $f''(x)$ sits in the denominator, the second derivative concavity check, and convergence behavior.
- **NM-6.3** covers **Optima from Tabulated Data**: difference table trends, Newton backward derivative formulas, and calculating the exact peak coordinate $(x, y_{\max})$.

**Suggested reading time:** ~25 minutes for the entire folder.

---

## 📑 Subtopic Index

| # | File | Priority | Exam Freq | Reading Time | Core Concept |
|:---:|:---|:---:|:---:|:---:|:---|
| 1 | [NM-6.1: Concepts](NM-6.1_Concepts.md) | 🟡 ⚠️ | 2021 (1 appearance) | ~6 min | Constrained vs unconstrained, feasible region, KKT and Lagrange multipliers |
| 2 | [NM-6.2: Unconstrained Optimization](NM-6.2_Unconstrained_Optimization.md) | 🟡 ⚠️ | 2021 (1 appearance) | ~8 min | Newton method on derivative $f'(x)=0$, denominator $f''(x)$, concave/convex test |
| 3 | [NM-6.3: Tabulated Optima](NM-6.3_Tabulated_Optima.md) | 🟡 | 2018 (1 appearance) | ~10 min | Difference tables, backward derivative formula, finding peak $x$ and $y_{\max}$ |

---

## 🎯 Exam Pattern for This Topic

In RUET semester finals, questions on Optimization appear in Section A under Question 5 or Question 6. Although tested less frequently than root finding or numerical integration, questions on this topic are direct and carry substantial marks:

### Pattern 1: Conceptual Distinctions (2 Marks)
The exam asks you to compare constrained and unconstrained optimization:
- Define both terms clearly.
- State stationarity conditions ($\nabla f = 0$ vs KKT conditions).
- Give physical engineering examples (free curve fitting vs structural stress limits).
- Draw a clean comparison table.

### Pattern 2: Newton's Method for Extrema (3 Marks)
Given an analytical function $f(x)$ and an initial guess $x_0$:
- Differentiate twice to get $f'(x)$ and $f''(x)$.
- Set up the recurrence $x_{n+1} = x_n - \frac{f'(x_n)}{f''(x_n)}$.
- Carry out iterations until the iterate stabilizes.
- Confirm whether the stationary point is a maximum by checking that $f''(x^*) < 0$.

### Pattern 3: Maximum from Tabulated Data (6 Marks)
Given a table of sampled $(x_i, y_i)$ pairs:
- Construct the finite difference table with step size $h$.
- Identify whether the peak is near the start or the end of the table.
- Apply the Newton forward or backward derivative formula.
- Set $\frac{dy}{dx} = 0$, solve for the dimensionless displacement $q$, and compute the physical peak location $x = x_n + hq$.
- Evaluate the interpolating polynomial at that location to find $y_{\max}$.

---

## 🔗 Topic Connections

- **Prerequisites:**
  - [NM-2.4: Newton-Raphson Method](../NM-2_Root_Finding/NM-2.4_Newton_Raphson.md): Newton's optimization formula is identical to Newton-Raphson applied to $g(x) = f'(x) = 0$.
  - [NM-4.11: Difference Tables](../NM-4_Curve_Fitting/NM-4.11_Difference_Tables.md): Forming diagonal difference tables is the foundation of finding optima from discrete tabular data.
- **Leads directly to:**
  - [NM-7.1: Difference Formulas](../NM-7_Differentiation/NM-7.1_Difference_Formulas.md): Numerical differentiation uses the exact same finite difference derivative expansions.
- **Pairs with in exams:**
  - In 2021 Q.6, optimization theory and Newton optimization were paired with numerical differentiation applications. In 2018 Q.5, tabulated optimization was paired with Newton second derivative formulas.
