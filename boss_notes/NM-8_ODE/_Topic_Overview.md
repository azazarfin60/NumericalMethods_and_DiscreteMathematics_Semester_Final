# NM-8: Ordinary Differential Equations (ODE)

> **Section:** Section A (Numerical Methods)  
> **Subtopics in this folder:** 8 files (NM-8.1 through NM-8.8)  
> **Exam weight:** Appears in 8/8 papers (100% frequency), typically worth 8–14 marks per paper (consistently featured in Question 7 or Question 8, and Question 4 or Question 5 in newer curriculum formats).

---

## 📖 How to Read This Topic

In electrical and computer engineering, differential equations model almost every dynamic process: transient responses in RLC circuits, signal propagation down transmission lines, thermal buildup in microprocessors, and electromagnetic fields. While textbook courses teach closed-form analytical calculus (like integrating factors or undetermined coefficients), real-world engineering equations rarely have clean closed-form solutions. That is why numerical ODE methods exist.

Numerical methods divide ODE problems into two major categories depending on where your given conditions sit:

1. **Initial Value Problems (IVPs) (NM-8.1 to NM-8.7):**
   All conditions are specified at a single starting point (usually time $t = 0$ or $x = x_0$). You start with known values and march forward step by step across the interval using a small step size $h$:
   - **First-Order Marching:** **Euler's Method** (NM-8.2) follows the tangent line at the start of each step. It is simple and cheap, but has a slow first-order global error $O(h)$.
   - **Second-Order Predictor-Corrector:** **Modified Euler / Heun's Method** (NM-8.3) and **Runge-Kutta 2nd Order** (NM-8.4) take a tentative Euler step, evaluate the slope at the predicted point, and average the two slopes. This cancels the leading error term, achieving second-order global error $O(h^2)$.
   - **Fourth-Order Precision:** **Runge-Kutta 4th Order (RK4)** (NM-8.5) evaluates four probe slopes per step and blends them using Simpson-style weights $(1, 2, 2, 1)$. It achieves fourth-order global error $O(h^4)$, making it the standard workhorse for practical engineering ODEs.
   - **Coupled Systems and Higher-Order ODEs:** (NM-8.6) shows how second-order ODEs (like Newton's second law or RLC loop equations) are split into systems of first-order equations and marched forward simultaneously.
   - **Physical Problem Modeling:** (NM-8.7) turns real-world engineering problem statements (such as continuous capacitor charge decay) into differential equations and solves them.

2. **Boundary Value Problems (BVPs) (NM-8.8):**
   Conditions are specified at two separate boundary points (such as the ends of a rod $x = 0$ and $x = L$, or potential across a boundary). You cannot march forward because you do not know the initial slope. Instead, you discretize the domain with finite differences, turning the differential equation into a coupled system of algebraic equations forming a **tridiagonal matrix** solved all at once.

Read the subtopics in this natural sequence:
- **NM-8.1** clarifies the foundational difference between IVPs and BVPs.
- **NM-8.2** establishes Euler's method, its geometric tangent stepping, and its truncation error limits.
- **NM-8.3** shows how Heun's method fixes Euler's slope error with predictor-corrector averaging.
- **NM-8.4** formalizes the two-stage Runge-Kutta framework.
- **NM-8.5** masters RK4, the highest-weight numerical ODE topic in the exam.
- **NM-8.6** converts higher-order ODEs into coupled first-order state-variable systems.
- **NM-8.7** derives ODEs directly from physical engineering descriptions.
- **NM-8.8** conquers the dangerous ambush topic of finite-difference boundary value problems.

**Suggested reading time:** ~50 minutes for the entire topic folder.

---

## 📑 Subtopic Index

| # | File | Priority | Exam Freq | Reading Time | Core Concept |
|:---:|:---|:---:|:---:|:---:|:---|
| 1 | [NM-8.1: IVP vs BVP](NM-8.1_IVP_vs_BVP.md) | 🟠 | 2/8 years | ~6 min | Conditions at one end vs both ends, marching vs simultaneous linear solve |
| 2 | [NM-8.2: Euler's Method](NM-8.2_Eulers_Method.md) | 🔴 | 5/8 years | ~10 min | Tangent stepping, derivation from Taylor series, local $O(h^2)$ vs global $O(h)$ error |
| 3 | [NM-8.3: Heun's Method](NM-8.3_Heuns_Method.md) | 🟠 | 3/8 years | ~9 min | Modified Euler, trapezoidal slope average, predictor-corrector derivation |
| 4 | [NM-8.4: RK2](NM-8.4_RK2.md) | 🟠 | 2/8 years + CT | ~8 min | Two-stage Runge-Kutta formula, $k_1$ and $k_2$ slope evaluations, second-order convergence |
| 5 | [NM-8.5: RK4](NM-8.5_RK4.md) | 🔴 | 5/8 years + CT | ~12 min | Classical four-slope march, Simpson weights $1:2:2:1$, $O(h^4)$ global accuracy |
| 6 | [NM-8.6: Higher-Order Systems](NM-8.6_Higher_Order_Systems.md) | 🟡 | 1 appearance | ~7 min | Converting $n$-th order ODE to $n$ first-order equations, synchronous state vector march |
| 7 | [NM-8.7: Physical ODE](NM-8.7_Physical_ODE.md) | 🟡 | 1 appearance | ~6 min | Mathematical modeling, capacitor charge decay rate law, separation of variables |
| 8 | [NM-8.8: Boundary Value Problems](NM-8.8_Boundary_Value_Problems.md) | 🟡 ⚠️ | 2 appearances | ~9 min | Danger zone topic, central difference discretization, tridiagonal matrix setup |

---

## 🎯 Exam Pattern for This Topic

In RUET examinations, ODE questions appear consistently in Question 7, Question 8, or Question 4/5. Examiners structure problems around four repeatable formats:

### Format 1: Euler and Modified Euler March (4–5 Marks)
- **Discussion and derivation:** State the purpose, derive Euler's formula from Taylor series, explain the local vs global error distinction, and discuss why Euler requires very small step sizes.
- **Numerical stepping:** Apply Euler or Modified Euler to solve first-order equations like $y' = x + y$, $y' = 1 - y$, or $y' = \frac{3}{5}x^3y$. Tabulate intermediate steps cleanly.

### Format 2: Runge-Kutta 4th Order Computations (6–8 Marks)
- High-mark centerpiece questions testing classical RK4:
  - Solve non-linear or coupled ODEs (e.g. $y' = \frac{y^2 - x^2}{y^2 + x^2}$, $10y' = x^2 - y^2$, or $y' = x + y$).
  - Calculate intermediate $k_1, k_2, k_3, k_4$ values step by step.
  - State the $k$-convention clearly and show the final weighted average.

### Format 3: RK2 vs RK4 Comparative Problems (4–5 Marks)
- Solve an ODE using RK2 (Heun form) and RK4 on the same test equation (e.g. CT-02B with $y' = x^2 - y$).
- Compare both numerical results against the exact analytical solution to prove second-order vs fourth-order convergence.

### Format 4: Danger Zone Ambush Questions (Systems, Physics, and BVPs) (4–6 Marks)
- **Higher-order systems:** Reduce second-order initial value problem $y'' - 0.5t = y$ into a two-variable first-order system and step with Euler.
- **Physical rate modeling:** Set up capacitor decay $\frac{dQ}{dt} = -0.04Q$ from English prose and solve for charge at 10 seconds.
- **BVP finite difference:** Set up and solve a second-order boundary value problem $y'' - y = 0$ using central differences, identifying the tridiagonal matrix equations.

---

## 🔗 Topic Connections

- **Prerequisites:**
  - [NM-1.6: Taylor Series](../NM-1_Error_Analysis/NM-1.6_Taylor_Series.md) -- all numerical ODE formulas (Euler, Heun, RK) are derived by matching terms of Taylor series expansions.
  - [NM-3.1: Gauss Elimination](../NM-3_Linear_Systems/NM-3.1_Gauss_Elimination.md) and [NM-3.5: Gauss-Seidel Iteration](../NM-3_Linear_Systems/NM-3.5_Gauss_Seidel_Iteration.md) -- solving the tridiagonal linear equations generated by finite-difference BVPs.
  - [NM-7.1: Difference Formulas](../NM-7_Differentiation/NM-7.1_Difference_Formulas.md) -- central differences for replacing first and second derivatives.
- **Leads directly to:**
  - [NM-9: Eigenvalues](../NM-9_Eigenvalues/_Topic_Overview.md) -- stability analysis of multi-degree dynamical systems.
  - [NM-10: Partial Differential Equations](../NM-10_PDE/_Topic_Overview.md) -- extending the finite-difference discretization from 1D intervals to 2D spatial grids (Laplace and Poisson equations).
