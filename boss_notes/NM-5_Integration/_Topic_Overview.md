# NM-5: Numerical Integration

> **Section:** Section A (Numerical Methods)  
> **Subtopics in this folder:** 7 files (NM-5.1 through NM-5.7)  
> **Exam weight:** Appears in 7/8 papers (87.5% frequency), typically worth 8 to 15 marks per paper (frequently featured in Question 6, Question 7, or Question 8).

---

## 📖 How to Read This Topic

In elementary calculus, you learned to evaluate definite integrals like $\int_a^b f(x)\,dx$ by finding an analytical antiderivative $F(x)$ and computing $F(b) - F(a)$. But in real engineering practice, that textbook path hits a brick wall for two reasons:

1. **No closed-form antiderivative exists:** Many everyday functions (like $\int e^{-x^2}\,dx$ or $\int \sqrt{1 + x^2}\,dx$) have no elementary antiderivative.
2. **The function is only known as sampled data points:** In digital signal processing, sensor telemetry, rocket flight logs, or circuit measurements, you do not have a formula. You only have a table of discrete data pairs $(x_i, y_i)$.

Numerical integration (also called **numerical quadrature**) solves this by replacing the difficult or unknown curve with a simple polynomial over small subintervals, and then integrating that polynomial instead.

This entire topic follows one elegant progression:

1. **Newton-Cotes Formulas (NM-5.1, NM-5.2, NM-5.3):**
   - **Trapezoidal Rule (NM-5.1):** Replace the curve on each strip with a straight line (degree 1 polynomial). Error is $O(h^2)$. Works for any number of segments $n \ge 1$.
   - **Simpson's 1/3 Rule (NM-5.2):** Group strips in pairs and fit a parabola (degree 2 polynomial) through every three points. By a symmetry miracle, it integrates cubics exactly. Error is $O(h^4)$. Requires $n$ to be an **even** number.
   - **Simpson's 3/8 Rule (NM-5.3):** Group strips in threes and fit a cubic (degree 3 polynomial) through every four points. Error is also $O(h^4)$, but with a larger error constant. Requires $n$ to be a **multiple of 3**.

2. **Comparative Strategy (NM-5.4):**
   - Learn the structural constraints, accuracy differences, and the classic mixed-rule strategies for odd numbers of intervals (like 5 intervals in op-amp circuit problems).

3. **Richardson Extrapolation & Romberg's Method (NM-5.5):**
   - Combine low-accuracy trapezoidal estimates from halved step sizes ($h, h/2, h/4$) to cancel the leading error terms systematically. You achieve $O(h^6)$ accuracy with zero new function evaluations.

4. **Error Analysis & Engineering Applications (NM-5.6, NM-5.7):**
   - Estimate the exact number of segments $n$ needed to meet a target error bound, calculate true and relative errors, and solve practical ECE physics problems like rocket distance and op-amp analog integrators.

Read the subtopics in numerical order from NM-5.1 to NM-5.7.

**Suggested reading time:** ~50 minutes for the entire topic folder.

---

## 📑 Subtopic Index

| # | File | Priority | Exam Frequency | Reading Time | Core Concept |
|:---:|:---|:---:|:---:|:---:|:---|
| 1 | [NM-5.1: Trapezoidal Rule](NM-5.1_Trapezoidal_Rule.md) | 🟠 | 4/8 years | ~9 min | Single and composite formulas, derivation, finding $n$ for target error |
| 2 | [NM-5.2: Simpson's 1/3 Rule](NM-5.2_Simpsons_One_Third.md) | 🔴 | 4/8 years | ~12 min | Parabolic panels, exactness to degree 3, rocket flight, op-amp circuit |
| 3 | [NM-5.3: Simpson's 3/8 Rule](NM-5.3_Simpsons_Three_Eighth.md) | 🟠 | 1 appearance | ~7 min | Four-node cubic panels, weights $1, 3, 3, 1$, multiple-of-3 interval constraint |
| 4 | [NM-5.4: Rule Comparison](NM-5.4_Rule_Comparison.md) | 🔴 | 2/8 years | ~8 min | Master comparison table, why 1/3 beats 3/8 at equal $h$, mixed strategies |
| 5 | [NM-5.5: Romberg's Method](NM-5.5_Rombergs_Method.md) | 🟠 | 3/8 years | ~9 min | Richardson extrapolation, halved step sizes, table construction |
| 6 | [NM-5.6: Error in Integration](NM-5.6_Error_in_Integration.md) | 🟠 | 2 appearances | ~7 min | Truncation error terms, error-bounded step selection, true vs relative error |
| 7 | [NM-5.7: Applied Integration](NM-5.7_Applied_Integration.md) | 🟠 | 3/8 years | ~8 min | Rocket kinematic distance, inverting op-amp analog integrator circuit |

---

## 🎯 Exam Pattern for This Topic

In RUET semester final examinations, numerical integration questions appear with strong regularity:

### Pattern 1: Formula Derivations & Theoretical Properties (3 to 4 Marks)
Examiners want to see if you understand where these formulas come from:
- **Composite Trapezoidal Derivation:** Summing single panels and showing why interior ordinates get multiplied by 2 while endpoints get multiplied by 1 (2021 Q.8(a)).
- **Simpson's 1/3 Derivation:** Integrating the Lagrange quadratic basis functions, and proving exactness for cubic polynomials via symmetry (2019 Q.7(a)).
- **Discussion of Properties:** Stating order of accuracy, geometric meaning, and overshooting conditions (2019 Q.6(c)).

### Pattern 2: Multi-Segment Integration with Error Bounds (4 Marks)
Problems where you find the number of segments $n$ to guarantee a specified error tolerance:
- Compute the maximum second derivative $\max|f''(x)|$ on $[a, b]$.
- Solve the inequality $\frac{(b-a)h^2}{12}\max|f''| < \epsilon$ for step size $h$ and segment count $n$ (2018 Q.6(b)).
- Always round $n$ up to the next integer.

### Pattern 3: Rule Comparisons & Odd-Interval Handling (3 to 5 Marks)
Examiners test if you understand subinterval constraints:
- "Compare Simpson's 1/3 and 3/8 rules" (2020 Q.6(a), 2023 Q.4(c)): present the master table and explain the 3.375 error constant ratio.
- Odd number of intervals (5 intervals from 6 points): recognize that Simpson's 1/3 alone cannot solve all 5 intervals, and combine it with the trapezoidal rule (2020 Q.6(b)).

### Pattern 4: Romberg Extrapolation Tables (4 Marks)
Building systematic extrapolation tables:
- Calculate composite trapezoidal values at $h = 0.5, 0.25, 0.125$.
- Apply Richardson extrapolation with divisor 3 for column 1 and divisor 15 for column 2 (2021 Q.8(b), 2022 Q.3(a), 2023 Q.2(c)).

### Pattern 5: ECE Engineering Applications (5 to 8 Marks)
Integrating real engineering data:
- **Rocket distance:** 8-segment composite Simpson's 1/3 (2018 Q.6(a)) or single-application 2-segment Simpson's 1/3 (2023 Q.4(b)), followed by true error and relative percentage error.
- **Op-amp integrator circuit:** Evaluating $v_0 = -\frac{1}{RC}\int_0^t v_i(t)\,dt$ from sampled laboratory values, remembering the leading minus sign and units (2020 Q.6(b)).

---

## 🔗 Topic Connections

- **Prerequisites:**
  - [NM-1.6: Taylor Series](../NM-1_Error_Analysis/NM-1.6_Taylor_Series.md) -- local and global truncation error expansions derive directly from Taylor series.
  - [NM-4.6: Lagrange Interpolation](../NM-4_Curve_Fitting/NM-4.6_Lagrange_Interpolation.md) -- Simpson's 1/3 rule is derived by integrating the Lagrange quadratic basis functions.
  - [NM-4.7: Newton Forward Difference](../NM-4_Curve_Fitting/NM-4.7_Newton_Forward_Difference.md) -- general Newton-Cotes quadrature formulas come from integrating Newton's forward difference formula.
- **Leads directly to:**
  - [NM-7: Numerical Differentiation](../NM-7_Differentiation/_Topic_Overview.md) -- differentiation is the companion inverse process, evaluating derivatives from discrete data.
  - [NM-8: Ordinary Differential Equations](../NM-8_ODE/_Topic_Overview.md) -- single-step and multistep ODE solvers (Euler, Heun, Runge-Kutta) are numerical integration steps applied to $y' = f(x, y)$.
- **Pairs with in exams:**
  - Often paired as a split question: Part (a) asks for a theoretical derivation or comparison, while Part (b) or (c) asks for a numerical problem or Romberg table.
