# NM-2: Root Finding

> **Section:** Section A (Numerical Methods)  
> **Subtopics in this folder:** 7 files (NM-2.1 through NM-2.7)  
> **Exam weight:** Appears in 8/8 papers (100% frequency), typically worth 10–14 marks (almost always the entirety of Question 2).

---

## 📖 How to Read This Topic

Root finding is the workhorse of numerical computation. When a circuit diode equation or power balance cannot be solved with clean pencil-and-paper algebra, you turn to the methods in this folder.

Read the files in numerical order:
- **NM-2.1** sets the foundation: what a root is, why roots can be simple or multiple, and the great divide between **bracketing** and **open** methods.
- **NM-2.2** covers **Bisection**: the rock-solid, can-never-fail method that repeatedly cuts an interval in half.
- **NM-2.3** covers **False Position (Regula Falsi)**: bisection with a brain, drawing chords instead of midpoints, and how to deal with one-sided stagnation.
- **NM-2.4** is the undisputed heavyweight: **Newton-Raphson**. You will learn its Taylor-series derivation, quadratic convergence, and the four classic failure modes that examiners love to test.
- **NM-2.5** covers the **Secant Method**: keeping Newton's rapid speed when you cannot easily calculate an analytic derivative.
- **NM-2.6** brings all four methods together into the master comparison ladder (safe vs. fast).
- **NM-2.7** applies these tools to **Polynomial Roots**: scanning integer signs, using Descartes' Rule of Signs, and solving circuit power equations.

**Suggested reading time:** ~50 minutes for the entire topic folder.

---

## 📑 Subtopic Index

| # | File | Priority | Exam Freq | Reading Time | Core Concept |
|:---:|:---|:---:|:---:|:---:|:---|
| 1 | [NM-2.1: Fundamentals](NM-2.1_Fundamentals.md) | 🔴 | 4/8 years | ~8 min | Bracketing vs open methods, 8 generalized iterative steps |
| 2 | [NM-2.2: Bisection Method](NM-2.2_Bisection_Method.md) | 🔴 | 5/8 years | ~8 min | Interval halving, pre-computable iteration count, relative error test |
| 3 | [NM-2.3: False Position](NM-2.3_False_Position.md) | 🔴 | 5/8 years + CT-01 | ~10 min | Chord formula derivation, one-sided stagnation, Illinois fix |
| 4 | [NM-2.4: Newton-Raphson](NM-2.4_Newton_Raphson.md) | 🔴 ⚠️ | 6/8 years | ~12 min | Tangent line, quadratic convergence, 4 failure modes and fixes |
| 5 | [NM-2.5: Secant Method](NM-2.5_Secant_Method.md) | 🟠 | 2 appearances | ~7 min | Finite-difference derivative approximation, order 1.618 |
| 6 | [NM-2.6: Method Comparison](NM-2.6_Method_Comparison.md) | 🔴 | 3/8 years + CT-01 | ~8 min | Safe-to-fast ladder, 4-method comparison matrix, safety-critical picks |
| 7 | [NM-2.7: Polynomial Roots](NM-2.7_Polynomial_Roots.md) | 🟠 | 2 appearances | ~7 min | Sign scans, Descartes' rule, power balance circuit roots |

---

## 🎯 Exam Pattern for This Topic

Question 2 on your exam paper is dedicated almost exclusively to NM-2. It follows a very predictable structure:

1. **Part (a) -- Theory definition or comparison (2–4 marks):**
   - Define iterative / bracketing methods and their general steps (NM-2.1).
   - Compare open vs. bracketing methods (NM-2.1, NM-2.6).
   - Develop an algorithm for Bisection with a relative accuracy test (NM-2.2) or False Position (NM-2.3).
2. **Part (b) -- Numerical problem or derivation (4–6 marks):**
   - Derive the False Position chord formula from two points (NM-2.3).
   - Discuss the four limitations of Newton-Raphson and their remedies (NM-2.4).
   - Compute circuit current from a power balance equation using Newton-Raphson (NM-2.4, NM-2.7).
   - Run Regula Falsi on $x^{2.2} = 69$ (NM-2.3).
3. **Part (c) -- Numerical execution or special method (4–6 marks):**
   - Solve a transcendental equation like $x \sin x + \cos x = 0$ via Newton-Raphson (NM-2.4).
   - Run 4 iterations of the Secant method on a cubic (NM-2.5).
   - Determine the smallest root of a polynomial cubic (NM-2.7).
   - Provide the complete comparison table among all four methods (NM-2.6).

**Most common question combinations:**
- **Combination A:** NM-2.1 (Open vs. bracketing) + NM-2.3 (Regula Falsi on $x^{2.2} = 69$) + NM-2.7 (Smallest root of cubic).
- **Combination B:** NM-2.4 (Limitations of N-R and fixes) + NM-2.4 (Circuit current $3I^2 - 4I - 4 = 0$) + NM-2.6 (Comparison table).
- **Combination C:** NM-2.2 (Bisection algorithm) + NM-2.3 (Derive Regula Falsi) + NM-2.4 (Transcendental root $x\sin x + \cos x = 0$).

---

## 🔗 Topic Connections

- **Prerequisite:** [NM-1: Error Analysis](../NM-1_Error_Analysis/_Topic_Overview.md) -- stopping tolerances ($\varepsilon_s$), relative error formulas, and Taylor series expansions.
- **Leads to:** [NM-3: Linear Systems](../NM-3_Linear_Systems/_Topic_Overview.md) -- where single-variable iterations generalize to multi-variable matrix systems (Gauss-Seidel and Jacobi).
- **Pairs with in exam:** Sits immediately after Question 1 (NM-1) to form the bedrock of Section A.
