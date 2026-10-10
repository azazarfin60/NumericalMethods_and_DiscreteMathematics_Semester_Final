# NM-7: Numerical Differentiation

> **Section:** Section A (Numerical Methods)  
> **Subtopics in this folder:** 4 files (NM-7.1 through NM-7.4)  
> **Exam weight:** Appears in 5/8 papers (62.5% frequency), typically worth 4 to 10 marks per paper (frequently featured in Question 6 or Question 7 in 2017 to 2021, and Question 3 in 2022).

---

## 📖 How to Read This Topic

In calculus class, taking a derivative is straightforward: you are handed an explicit formula like $f(x) = \sin(x)$ or $f(x) = x^3$, and you apply formal differentiation rules. In engineering practice, however, you almost never have a neat formula. Instead, you have a discrete table of numbers logged by instruments at specific moments in time: current readings through an inductor, angular positions of a motor shaft, or GPS coordinates of a moving vehicle.

Numerical differentiation answers one central question: *How do we find the rate of change when all we have is a table of numbers?*

The core trick is simple: we replace the unknown function with an approximating interpolating polynomial that passes through the data points, and then differentiate that polynomial. Alternatively, we combine Taylor series expansions from neighboring points so that unwanted terms cancel out, leaving the derivative plus an error term.

Read the subtopics in this sequence:

1. **NM-7.1 (Difference Formulas):**
   Start here to build your foundation. You will learn the Taylor series basis of numerical differentiation and derive the standard menu of difference equations: two-point forward and backward ($O(h)$), three-point central ($O(h^2)$), three-point forward and backward ($O(h^2)$), and five-point central ($O(h^4)$). You will also understand why dividing by small intervals $h$ causes dangerous subtractive cancellation.

2. **NM-7.2 (First Derivative from Tabulated Data):**
   This is the computational workhorse tested in 4 out of 8 semester finals. You will master the three-step decision rule for selecting the right formula (checking node availability, picking central differences for interior points, and verifying data smoothness). You will also work through four actual RUET exam problems, including an exponential table, an inductor circuit, an angular motion dataset, and an out-of-order quartic table.

3. **NM-7.3 (Second Derivative & Formula Derivation):**
   This is the heavy derivation question that students fear most. In 2017 and 2018, examiners asked students to derive Newton's forward difference formula for the second derivative $d^2y/dx^2$. You will learn the four-step derivation dance using the dimensionless variable $p = (x - x_0)/h$, the chain rule factor $1/h^2$, and falling factorial polynomials.

4. **NM-7.4 (Applied Differentiation):**
   Finish here to connect the math to real-world electrical and computer engineering. You will see how numerical differentiation recovers quantities that sensors cannot measure directly: inductor voltage from current ($v = L\,di/dt$), angular velocity from shaft encoders ($\omega = d\theta/dt$), vehicle speed and acceleration from GPS logs, and signal peak detection.

**Suggested reading time:** ~35 minutes for the entire topic folder.

---

## 📑 Subtopic Index

| # | File | Priority | Exam Freq | Reading Time | Core Concept |
|:---:|:---|:---:|:---:|:---:|:---|
| 1 | [NM-7.1: Difference Formulas](NM-7.1_Difference_Formulas.md) | 🟠 | 2019 (1/8) | ~8 min | Taylor series basis, two-point, three-point, five-point equations, truncation vs round-off |
| 2 | [NM-7.2: First Derivative](NM-7.2_First_Derivative.md) | 🟠 | 4/8 years (2019, 2020, 2021, 2022) | ~12 min | Formula selection protocol, node availability check, four complete exam calculations |
| 3 | [NM-7.3: Second Derivative](NM-7.3_Second_Derivative.md) | 🟠 ⚠️ | 3 appearances (2017, 2018, 2021) | ~10 min | Newton forward derivation, chain rule scaling $1/h^2$, falling factorials, exactness test |
| 4 | [NM-7.4: Applied Differentiation](NM-7.4_Applied_Differentiation.md) | 🟠 | 3 appearances (2019, 2020, 2021) | ~7 min | Real-life ECE applications, inductor voltage, shaft velocity, GPS telemetry, peak sensing |

---

## 🎯 Exam Pattern for This Topic

In RUET semester finals, questions from NM-7 appear in four recognizable shapes:

### Pattern 1: Conceptual Basis & Formula Recall (4 Marks)
Examiners ask you to state what numerical differentiation rests on and write down standard difference equations:
- Explain that numerical differentiation differentiates the interpolating polynomial or uses Taylor series cancellations.
- State at least four difference formulas with their order of error: forward ($O(h)$), backward ($O(h)$), central ($O(h^2)$), and higher-order forms.
- Example: 2019 Q.6(a).

### Pattern 2: Second Derivative Formula Derivation (4–6 Marks)
This is an exam favorite that tests pure mathematical derivation:
- Start with Newton's forward difference interpolation polynomial in $p = (x - x_0)/h$.
- Apply the chain rule $d/dx = (1/h)(d/dp)$ to find $dy/dx$.
- Differentiate again to deduce the formula for $d^2y/dx^2$ with the leading factor $1/h^2$.
- State the stopping rule and the minimum number of data points needed (at least three points).
- Examples: 2017 Q.6(c), 2018 Q.5(a).

### Pattern 3: Tabular First & Second Derivatives (4–5 Marks)
You are given a table of numbers and asked to find $dy/dx$ and $d^2y/dx^2$ at a specific node:
- **Check node availability first:** Do not grab a 5-point formula if the boundary nodes do not exist in the table (such as $x = 1.2$ with $h = 0.2$ needing $x = 0.8$).
- **Use central differences at interior points:** Symmetric cancellation gives $O(h^2)$ accuracy with far smaller error constants than one-sided formulas.
- **Pay attention to denominators:** $2h$ for first derivative, $h^2$ for second derivative.
- Examples: 2021 Q.7(c), 2022 Q.3(b).

### Pattern 4: ECE Physical Applications (2–5 Marks)
The exam frames the problem around a physical measurement table:
- **Inductor voltage:** Given current $I(t)$, compute $v(t) = L \frac{dI}{dt}$ (2019 Q.6(b)).
- **Rotary dynamics:** Given angular displacement $\theta(t)$, compute angular velocity $\omega = \frac{d\theta}{dt}$ (2020 Q.6(c)).
- **Descriptive application:** State real-life engineering applications like GPS telemetry or crash testing (2021 Q.6(a)).

---

## 🔗 Topic Connections

- **Prerequisites:**
  - [NM-1.4: Error Types](../NM-1_Error_Analysis/NM-1.4_Error_Types.md) and [NM-1.5: Error Propagation](../NM-1_Error_Analysis/NM-1.5_Error_Propagation.md) -- understanding round-off error, truncation error, and how subtraction of nearly equal numbers causes catastrophic cancellation.
  - [NM-1.6: Taylor Series](../NM-1_Error_Analysis/NM-1.6_Taylor_Series.md) -- the expansion engine that generates all difference equations and dictates their truncation error orders.
  - [NM-4.7: Newton Forward Difference](../NM-4_Curve_Fitting/NM-4.7_Newton_Forward_Difference.md) and [NM-4.11: Difference Tables](../NM-4_Curve_Fitting/NM-4.11_Difference_Tables.md) -- the interpolation polynomial and finite difference tables that NM-7 differentiates.
- **Leads directly to:**
  - [NM-8: Ordinary Differential Equations](../NM-8_ODE/_Topic_Overview.md) -- methods like Euler's method and Runge-Kutta solve differential equations by replacing continuous derivatives with finite difference quotients.
- **Pairs with in exams:**
  - In RUET finals, NM-7 questions frequently pair with NM-5 (Numerical Integration) or NM-8 (ODEs) to form a full 14-mark question in Section A.
