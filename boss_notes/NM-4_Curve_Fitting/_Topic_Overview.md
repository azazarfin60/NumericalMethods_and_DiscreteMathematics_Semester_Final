# NM-4: Curve Fitting

> **Section:** Section A (Numerical Methods)  
> **Subtopics in this folder:** 12 files (NM-4.1 through NM-4.12)  
> **Exam weight:** Appears in 8/8 papers (100% frequency), typically worth 12–16 marks per paper (frequently featured in Question 3, Question 4, Question 5, or Question 6).

---

## 📖 How to Read This Topic

In electrical and computer engineering, data comes from real-world sensors, lab experiments, component characterizations, or discrete digital samples. Once you collect discrete data pairs $(x_i, y_i)$, you always face one central question: *What is happening between our data points, and what underlying law generated them?*

Numerical analysis divides this challenge into two major mathematical worlds:

1. **Regression / Curve Fitting (NM-4.1 to NM-4.4):**
   Use this when your data has experimental noise, measurement wobble, or thermal drift. You do **not** want the curve to pass through every noisy point. Instead, you fit a smooth equation (straight line, exponential, or reciprocal model) that captures the true underlying physical trend by minimizing the sum of squared errors.
2. **Exact Interpolation (NM-4.5 to NM-4.12):**
   Use this when your data is exact (from standard tables, certified calibrations, or clean mathematical functions). You construct a polynomial that passes through **every single tabulated point exactly**. The technique you pick depends purely on how your data points are spaced and where your target value sits:
   - **Unequal spacing:** Use **Lagrange** (NM-4.6) or **Newton Divided Differences** (NM-4.9).
   - **Equal spacing near the top:** Use **Newton Forward Differences** (NM-4.7, NM-4.11).
   - **Equal spacing near the bottom:** Use **Newton Backward Differences** (NM-4.8, NM-4.11).
   - **Equal spacing near the middle:** Use **Gauss Forward/Backward or Stirling** (NM-4.10).
   - **Two input variables:** Use **Two-Variable Double Interpolation** (NM-4.12).

Read the subtopics in this sequence:
- **NM-4.1** sets the foundation: the three-way distinction between interpolation, extrapolation, and curve fitting, why ECE engineers need fitting, and the mathematical signature of least squares.
- **NM-4.2** covers **Least-Squares Linear Regression**: deriving the normal equations from scratch and fitting straight lines $y = a + bx$ to experimental $v\text{--}i$ data.
- **NM-4.3** tackles **Non-Linear Regression**: linearizing exponential curves ($y = ae^{bx}$) and saturation curves ($y = x/(a+bx)$) through clever variable substitutions.
- **NM-4.4** explains **Regression Criteria Theory**: why minimizing simple sum of errors or absolute errors fails mathematically, and why least squares is the best criterion.
- **NM-4.5** explores **Linear Interpolation**: connecting two adjacent data points with a straight chord and analyzing measurement error propagation.
- **NM-4.6** is the most tested interpolation method: **Lagrange Interpolation**. It requires no difference tables, works on unevenly spaced points, and obeys the Kronecker delta and partition of unity properties.
- **NM-4.7** covers **Newton Forward Difference**: the complete formula derivation, factorials in $p$, and application to series summation identities.
- **NM-4.8** covers **Newton Backward Difference**: anchoring at the bottom node using rising factorials for points near the end of a table.
- **NM-4.9** covers **Newton Divided Differences**: handling arbitrary unequal steps, invariant table construction, and expanding general polynomials.
- **NM-4.10** covers **Central Difference Formulas (Gauss & Stirling)**: following the zig-zag path to minimize round-off error near the center of a table.
- **NM-4.11** details **Difference Table Formation**: constructing clean diagonal tables, verifying higher-order differences, and population census forecasting problems.
- **NM-4.12** rounds out the topic with **Two-Variable Interpolation**: performing successive one-dimensional interpolations on 2D grids.

**Suggested reading time:** ~75 minutes for the entire topic folder.

---

## 📑 Subtopic Index

| # | File | Priority | Exam Freq | Reading Time | Core Concept |
|:---:|:---|:---:|:---:|:---:|:---|
| 1 | [NM-4.1: Concepts](NM-4.1_Concepts.md) | 🔴 | 7/8 years | ~10 min | Interpolation vs extrapolation vs fitting, ECE real-life examples, normal equations |
| 2 | [NM-4.2: Linear Regression](NM-4.2_Linear_Regression.md) | 🔴 ⚠️ | 4/8 years | ~10 min | Deriving normal equations, slope $b$ and intercept $a$, wire $v\text{--}i$ experiment |
| 3 | [NM-4.3: Nonlinear Regression](NM-4.3_Nonlinear_Regression.md) | 🔴 ⚠️ | 3/8 years | ~9 min | Linearizing exponential $ae^{bx}$ and reciprocal saturation $x/(a+bx)$ |
| 4 | [NM-4.4: Regression Theory](NM-4.4_Regression_Theory.md) | 🟠 ⚠️ | 2 appearances | ~7 min | Why $\sum e_i=0$ and $\sum \|e_i\|$ fail, least-squares quadratic optimality |
| 5 | [NM-4.5: Linear Interpolation](NM-4.5_Linear_Interpolation.md) | 🟠 | 2 appearances | ~6 min | Two-point chord approximation, rocket velocity, Ohm's law measurement error |
| 6 | [NM-4.6: Lagrange Interpolation](NM-4.6_Lagrange_Interpolation.md) | 🔴 | 7/8 years + CT | ~12 min | Unequal spacing, basis polynomials, partition of unity, laser arm path |
| 7 | [NM-4.7: Newton Forward Difference](NM-4.7_Newton_Forward_Difference.md) | 🔴 | 6/8 years + CT | ~10 min | Forward formula derivation, dimensionless $p$, sum of cubes identity $S_n$ |
| 8 | [NM-4.8: Newton Backward Difference](NM-4.8_Newton_Backward_Difference.md) | 🟠 | 4 appearances | ~8 min | Bottom node anchoring, rising factorials, weather station and census data |
| 9 | [NM-4.9: Divided Difference](NM-4.9_Divided_Difference.md) | 🟠 | 3 appearances | ~9 min | Unequal intervals, symmetric table construction, polynomial extraction |
| 10 | [NM-4.10: Gauss and Stirling](NM-4.10_Gauss_and_Stirling.md) | 🟡 ⚠️ | 1 appearance | ~8 min | Central differences, zig-zag path, evaluating $e^{1.17}$ with 5-decimal accuracy |
| 11 | [NM-4.11: Difference Tables](NM-4.11_Difference_Tables.md) | 🔴 | 5/8 years | ~10 min | Diagonal difference tables, census estimation, gas sensor interpretation |
| 12 | [NM-4.12: Two-Variable Interpolation](NM-4.12_Two_Variable_Interpolation.md) | ⚫ | Never examined | ~4 min | Double interpolation on 2D surface grids for reading flow completeness |

---

## 🎯 Exam Pattern for This Topic

In RUET semester finals, questions from NM-4 consistently appear in Question 3, Question 4, Question 5, or Question 6. The examiners design problems around four distinct patterns:

### Pattern 1: Conceptual Definitions & Distinctions (2–4 Marks)
Examiners frequently ask you to clearly distinguish between interpolation, extrapolation, and curve fitting:
- Define all three terms and state where the target point $x$ must lie.
- Explain why polynomial extrapolation is risky (unbounded error outside data range).
- Give real-world ECE examples (thermocouple temperature calibration, wire resistance from noisy $v\text{--}i$ data).

### Pattern 2: Least-Squares Curve Fitting (4–5 Marks)
Either straight-line fitting or non-linear curve fitting:
- **Linear regression derivation:** Deduce the formulas for slope $b$ and intercept $a$ from the principle of least squares by setting partial derivatives to zero.
- **Linear numerical problems:** Fit $y = a + bx$ or $i = a + bv$ to experimental points and predict a value (such as current at $3.5\text{ V}$).
- **Non-linear problems:** Linearize $y = ae^{bx}$ using natural logarithms, or linearize $y = \frac{x}{a + bx}$ using reciprocals $1/y = a(1/x) + b$.

### Pattern 3: Equal Interval Difference Tables & Polynomials (3–5 Marks)
Equally spaced data tables ($h = \text{constant}$):
- **Newton Forward:** Derivation of the formula, or computing series sums like $\sum_{r=1}^n r^3$.
- **Difference Table Construction:** Build the difference table and estimate values near the top using forward differences, or values near the bottom using backward differences (such as town census population in 1895, 1925, 1955, or 1995).
- **Central Differences:** Gauss forward formula along the central zig-zag path to evaluate functions like $e^{1.17}$.

### Pattern 4: Unequal Interval Interpolation (3–5 Marks)
When step size $h$ is not constant:
- **Lagrange interpolation:** Evaluating polynomials at target points without building difference tables (such as robot laser scanner path or pollutant concentration).
- **Newton divided differences:** Building divided difference tables and expanding the polynomial $f(x)$ explicitly.

---

## 🔗 Topic Connections

- **Prerequisites:**
  - [NM-1.4: Error Types](../NM-1_Error_Analysis/NM-1.4_Error_Types.md) and [NM-1.5: Error Propagation](../NM-1_Error_Analysis/NM-1.5_Error_Propagation.md) -- understanding round-off error, truncation error, and how measurement uncertainty propagates into chords and fits.
  - [NM-3.1: Gauss Elimination](../NM-3_Linear_Systems/NM-3.1_Gauss_Elimination.md) -- solving the linear normal equations produced by multivariable or polynomial least-squares regression.
- **Leads directly to:**
  - [NM-5: Numerical Integration](../NM-5_Integration/_Topic_Overview.md) -- numerical integration formulas (like Trapezoidal and Simpson's rules) are derived by integrating Newton forward and Lagrange interpolating polynomials over discrete subintervals!
  - [NM-7: Numerical Differentiation](../NM-7_Differentiation/_Topic_Overview.md) -- numerical differentiation evaluates derivatives directly from finite difference tables.
- **Pairs with in exams:**
  - Questions often pair a theoretical definition from NM-4.1 with a numerical problem from NM-4.2, NM-4.6, or NM-4.11.

---

[← Previous: NM-3.8 Circuit Applications](../NM-3_Linear_Systems/NM-3.8_Circuit_Applications.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: NM-4.1 Concepts →](NM-4.1_Concepts.md)
