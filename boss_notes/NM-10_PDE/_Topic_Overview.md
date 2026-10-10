# NM-10: Partial Differential Equations

> **Section:** Section A (Numerical Methods)  
> **Subtopics in this folder:** 5 files (NM-10.1 through NM-10.5)  
> **Exam weight:** Appears in 4/8 years (50% frequency), typically worth 6 to 14 marks (Question 6 or Question 8).

---

## 📖 How to Read This Topic

Partial Differential Equations (PDEs) describe physical fields in multiple dimensions, such as electrostatic potential across a semiconductor surface, heat flowing through a metal plate, or acoustic waves travelling down a transmission line.

In analytical calculus, solving PDEs with realistic boundary shapes is notoriously difficult. In numerical methods, however, the strategy is surprisingly simple:
1. Lay a square grid over the 2D region.
2. Replace spatial derivatives with central finite difference approximations.
3. At every interior point, the PDE turns into a simple algebraic equation relating the node to its immediate neighbors.

Read the subtopics in this sequence:
- **NM-10.1** gives the big picture with **Classification & Theory**: the discriminant test that sorts equations into elliptic, parabolic, and hyperbolic types, plus the standard numerical iterative framework.
- **NM-10.2** covers the most heavily examined equation: **Laplace Equation** ($\nabla^2 u = 0$). You will master the five-point stencil, where every node equals the exact average of its four neighbors, setting up a clean $4 \times 4$ linear system.
- **NM-10.3** moves to the **Poisson Equation** ($\nabla^2 u = -f(x,y)$): Laplace with an internal source or charge distribution. You will see how the source term shifts the right-hand side and alters the diagonal signs.
- **NM-10.4** focuses on the numerical solver: **Liebmann's Iterative Method**. This is simply Gauss-Seidel applied to 2D spatial grids. You will learn why it converges so reliably, how to sweep nodes, and when to use successive over-relaxation (SOR).
- **NM-10.5** wraps up the theory with **Boundary Conditions in PDEs**: explaining why a PDE without boundary values is mathematically meaningless, and how Dirichlet and Neumann conditions lock down a unique numerical solution.

**Suggested reading time:** ~40 minutes for the entire topic folder.

---

## 📑 Subtopic Index

| # | File | Priority | Exam Freq | Reading Time | Core Concept |
|:---:|:---|:---:|:---:|:---:|:---|
| 1 | [NM-10.1: Classification](NM-10.1_Classification.md) | 🟠 | 2020 Q.8(a) | ~8 min | Elliptic, parabolic, hyperbolic classification, discriminant test $B^2 - 4AC$, iterative heat conduction solve |
| 2 | [NM-10.2: Laplace Equation](NM-10.2_Laplace_Equation.md) | 🔴 ⚠️ | 3/8 years | ~12 min | Five-point stencil, averaging rule, $4 \times 4$ linear systems, 2018/2019/2020 exam grid solves |
| 3 | [NM-10.3: Poisson Equation](NM-10.3_Poisson_Equation.md) | 🟠 | 2021 Q.6(c) | ~9 min | Laplace with source term, $-h^2 f(x_i,y_j)$ right-hand side, symmetry reduction, full 2021 exam solve |
| 4 | [NM-10.4: Liebmann's Method](NM-10.4_Liebmanns_Method.md) | 🟠 | 2 appearances | ~7 min | Gauss-Seidel on 2D grids, fresh neighbor updates, spectral radius convergence, SOR acceleration |
| 5 | [NM-10.5: Boundary Conditions](NM-10.5_Boundary_Conditions.md) | 🟠 | 2024 Q.4(c) | ~6 min | Dirichlet, Neumann, Robin conditions, unique solvability, preventing numerical instability |

---

## 🎯 Exam Pattern for This Topic

In RUET semester finals, PDE questions appear under Question 6 or Question 8 of Section A. The questions follow two recurring patterns:

### Pattern 1: The Small Square Mesh Problem (6 to 8 Marks, High Frequency)
The exam prints a $3 \times 3$ mesh covering a square domain, giving you four interior nodes ($u_1, u_2, u_3, u_4$) and fixed Dirichlet boundary values:
- **2018 Q.8(a):** Laplace equation with potentials $100\text{ V}$ (top), $0\text{ V}$ (bottom), $75\text{ V}$ (left), $50\text{ V}$ (right).
- **2019 Q.8(b):** Laplace equation with integer boundaries ($1, 2, 4, 5, \dots$), solved by Gaussian elimination.
- **2020 Q.8(b):** Laplace potential $E(x,y)$ with boundary $1$ on the top edge and $0$ elsewhere, solved by Liebmann iteration.
- **2021 Q.6(c):** Poisson equation $U_{xx} + U_{yy} = -10(x^2 + y^2 + 10)$ with zero boundaries on all four sides.

*Key exam tip:* Every interior node in a $2 \times 2$ interior mesh has exactly two interior neighbors and two boundary neighbors. The resulting coefficient matrix always has 4 on the diagonal and two $-1$s off the diagonal.

### Pattern 2: Theory and Classification (3 to 5 Marks)
Examiners ask you to state definitions or explain numerical mechanics:
- **2020 Q.8(a):** Write the four types of PDEs (Laplace, Poisson, wave, heat) and explain how to solve one using an iterative technique.
- **2024 Q.4(c):** State the importance of boundary conditions in solving PDEs numerically.

---

## 🔗 Topic Connections

- **Prerequisites:**
  - [NM-7: Difference Formulas](../NM-7_Differentiation/NM-7.1_Difference_Formulas.md) -- central difference formulas for second derivatives $\frac{\partial^2 u}{\partial x^2} \approx \frac{u_{i+1,j} - 2u_{i,j} + u_{i-1,j}}{h^2}$.
  - [NM-3.5: Gauss-Seidel Iteration](../NM-3_Linear_Systems/NM-3.5_Gauss_Seidel.md) -- the core engine of Liebmann's method.
- **Leads to:**
  - Electrostatic field calculations, wave propagation, waveguide analysis, and thermal modeling in electronic packages.
- **Pairs with in exam:** Often paired with numerical integration (NM-5) or ordinary differential equations (NM-8) to complete Section A.
