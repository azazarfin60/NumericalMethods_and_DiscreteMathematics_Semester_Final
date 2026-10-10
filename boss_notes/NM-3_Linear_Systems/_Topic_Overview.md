# NM-3: Linear Systems

> **Section:** Section A (Numerical Methods)  
> **Subtopics in this folder:** 8 files (NM-3.1 through NM-3.8)  
> **Exam weight:** Appears in 8/8 papers (100% frequency), typically worth 10–16 marks (usually Question 3, Question 4, or Question 7).

---

## 📖 How to Read This Topic

Solving simultaneous linear equations ($A\mathbf{x} = \mathbf{b}$) is the mathematical backbone of electrical engineering. Whenever you write Kirchhoff's Current Law (KCL) at circuit nodes or Kirchhoff's Voltage Law (KVL) around circuit loops, you produce a system of linear equations.

Numerical linear algebra splits cleanly into two distinct philosophies:
1. **Direct Methods (NM-3.1 to NM-3.3):** You perform a fixed sequence of arithmetic operations to get the exact algebraic answer in one go.
2. **Iterative Methods (NM-3.4 to NM-3.6):** You start with an initial guess (usually zeros) and repeatedly refine it until the numbers settle down to your desired precision.

Read the subtopics in this sequence:
- **NM-3.1** introduces **Gauss Elimination**: the classic school algorithm turned into a computer-ready upper-triangular reduction with back-substitution.
- **NM-3.2** tackles **Pivoting**: the essential safeguard against dividing by zero or letting tiny numbers create catastrophic round-off errors.
- **NM-3.3** covers **LU Decomposition**: factoring matrix $A$ into lower and upper triangular pieces so you can solve systems with multiple right-hand sides without redoing the heavy elimination.
- **NM-3.4** introduces iterative solving with **Jacobi Iteration**: updating all variables in lockstep using only values from the previous round.
- **NM-3.5** is the crown jewel of the topic: **Gauss-Seidel Iteration**. It plugs newly calculated values in immediately, cuts iterations in half, and is tested in almost every semester final.
- **NM-3.6** covers **Relaxation (SOR)**: steering the iteration step size with a relaxation factor $\lambda$ to speed up slow convergence or damp wild oscillations.
- **NM-3.7** discusses **Ill-Conditioned Systems**: why some physical problems are hyper-sensitive to small data errors, and why pivoting cannot fix a bad condition number.
- **NM-3.8** connects the theory to real engineering: **Circuit Applications**. You will learn how to write mesh and nodal equations so that strict diagonal dominance is guaranteed.

**Suggested reading time:** ~55 minutes for the entire topic folder.

---

## 📑 Subtopic Index

| # | File | Priority | Exam Freq | Reading Time | Core Concept |
|:---:|:---|:---:|:---:|:---:|:---|
| 1 | [NM-3.1: Gauss Elimination](NM-3.1_Gauss_Elimination.md) | 🔴 | 3 appearances | ~8 min | Forward elimination to upper triangular form, back-substitution, operation counts |
| 2 | [NM-3.2: Pivoting](NM-3.2_Pivoting.md) | 🔴 | 4/8 years | ~8 min | Divisor protection, partial vs complete pivoting, stability vs conditioning |
| 3 | [NM-3.3: LU Decomposition](NM-3.3_LU_Decomposition.md) | 🟠 | 2 appearances | ~7 min | Matrix factorization $A=LU$, Doolittle vs Crout, multiple right-hand side savings |
| 4 | [NM-3.4: Jacobi Iteration](NM-3.4_Jacobi_Iteration.md) | 🟠 | 2 appearances | ~7 min | Simultaneous displacements, iteration matrix, parallel computation |
| 5 | [NM-3.5: Gauss-Seidel](NM-3.5_Gauss_Seidel.md) | 🔴 ⚠️ | 7/8 years | ~14 min | Successive displacements, diagonal dominance, DC mesh/nodal circuits, CT problems |
| 6 | [NM-3.6: Relaxation](NM-3.6_Relaxation.md) | 🟠 | 2 appearances | ~7 min | Successive Over-Relaxation (SOR), relaxation parameter $\lambda$, under-relaxation damping |
| 7 | [NM-3.7: Ill-Conditioned Systems](NM-3.7_Ill_Conditioned_Systems.md) | 🟠 | 2 appearances | ~6 min | Condition number $\kappa(A)$, nearly singular matrices, stability vs problem conditioning |
| 8 | [NM-3.8: Circuit Applications](NM-3.8_Circuit_Applications.md) | 🔴 | 5/8 years | ~10 min | KVL loop analysis, KCL nodal analysis, outer-branch current source rules |

---

## 🎯 Exam Pattern for This Topic

In RUET semester finals, questions from NM-3 appear under Question 3, Question 4, or Question 7. The examiners follow two distinct styles:

### Style 1: The Circuit Problem (High Marks, Almost Every Year)
The exam gives a schematic diagram of a DC resistive circuit (with 2 to 4 meshes or nodes) and asks you to solve for branch currents or node potentials using Gauss-Seidel:
- **2018 Q.4(b):** 4-mesh DC circuit with a 10 A current source.
- **2019 Q.3(c):** 2-node DC network with two current sources (show two iterations).
- **2020 Q.4(b):** 3-mesh DC circuit with a 400 V source and 10 A source.
- **2021 Q.7(b):** DC network with an independent voltage source and a dependent source $5I_0$.
- **2024 Q.2(b):** 3-mesh DC circuit with a 500 V source and 5 A source.

*Key exam rule:* If an independent current source sits on an outer branch, that mesh current is already known! Never write a loop equation for it.

### Style 2: Theory Definitions and Comparisons (2–4 Marks)
Examiners frequently attach a conceptual definition question before or after the numerical circuit problem:
- **Pivoting theory (2–4 marks):** Define pivots; compare partial and complete pivoting; explain why pivoting is important (2017 Q.4(a), 2019 Q.3(b), 2021 Q.7(a), 2022 Q.3(c)).
- **Direct vs. Iterative (4 marks):** Classify direct methods and describe Gauss elimination (2019 Q.3(a), 2020 Q.4(a)).
- **Conditioning (2 marks):** Define an ill-conditioned system and state its causes (2022 Q.4(c)).
- **Relaxation concepts (3 marks):** Define over-relaxation and under-relaxation (2018 Q.4(a)).
- **LU Factorization (5 marks):** Show how a square matrix is factored into $LU$ (2017 Q.4(b)).

---

## 🔗 Topic Connections

- **Prerequisites:** Matrix algebra, basic determinants, and sophomore circuit theory (KCL, KVL, Ohm's law).
- **Leads to:**
  - [NM-4: Curve Fitting](../NM-4_Curve_Fitting/_Topic_Overview.md) -- solving the normal equations for polynomial and linear regression.
  - [NM-10: Partial Differential Equations](../NM-10_PDE/_Topic_Overview.md) -- Liebmann's method for Laplace and Poisson equations is simply Gauss-Seidel applied to a 2D spatial grid!
- **Pairs with in exam:** Often paired with root finding (NM-2) or numerical differentiation (NM-7) to form the computational core of Section A.
