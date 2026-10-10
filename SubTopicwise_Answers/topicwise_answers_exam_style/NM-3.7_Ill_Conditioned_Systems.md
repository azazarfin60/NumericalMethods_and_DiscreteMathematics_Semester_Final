---
title: "NM-3.7 · Ill-Conditioned Systems"
tags:
  - numerical-methods
  - discrete-mathematics
  - topicwise
---





[🏠 Subtopic Index](00_Index.md) | [← Prev: NM-3.6 Relaxation](NM-3.6_Relaxation.md) | [Next: NM-3.8 Circuit Applications →](NM-3.8_Circuit_Applications.md)

---

# NM-3.7 · Ill-Conditioned Systems

Every block below is copied from `../answers_exam_style/`, which is the
only place an answer is authored. A number here is the same number, character
for character, as the one it came from.


### [2022 Q.4(c)]

**Question.** Define ill-conditioned system.

**Solution.**

**Definition.** A system of linear equations is **ill-conditioned** when a small
change in the input produces a disproportionately large change in the solution.

**Measure.** The **condition number** $\kappa$ of the coefficient matrix is the
ratio of the largest to the smallest relative error:

$$
\frac{\dfrac{\|\delta x\|}{\|x\|}}{\dfrac{\|\delta b\|}{\|b\|}} \le \kappa(A)
$$

Thus a relative error of $\epsilon$ in the data may become up to $\kappa\epsilon$ in
the answer.

| $\kappa$ | Behaviour |
| :-- | :-- |
| $\kappa = 1$ | Perfectly conditioned, error passes through unchanged |
| $\kappa \approx 10$ | Mild amplification |
| $\kappa \approx 10^6$ | Loss of about six significant digits |
| $\kappa > 10^{16}$ | All precision lost; the matrix is numerically singular |

**Causes.**

1. **A matrix that is nearly singular**, that is one with an eigenvalue very
   close to zero, or one whose rows are almost linearly dependent. Two nearly
   parallel equations then constrain the solution very weakly.
2. **Rows or columns of wildly different magnitudes.** The small ones are
   effectively ignored.
3. **A bad choice of variables.** Two variables that measure nearly the same
   physical quantity make the corresponding columns almost equal.

**Why it matters in engineering.** The data itself has uncertainty, typically
$10^{-4}$ relative from the instrument. If $\kappa = 10^{8}$ then the answer
carries a relative uncertainty of $10^4$, which is useless, even though the
computation ran to machine precision.

**What to do about it.** Row or column scaling to make the entries comparable,
choosing better-conditioned variables, reformulating the physical problem, or
using higher precision. **Pivoting helps stability but does not change
$\kappa$.** Conditioning is a property of the problem, not of the algorithm.

$$
\boxed{\text{ill-conditioned means small input errors produce large output errors; measured by }\kappa}
$$

---

---

[🏠 Subtopic Index](00_Index.md) | [← Prev: NM-3.6 Relaxation](NM-3.6_Relaxation.md) | [Next: NM-3.8 Circuit Applications →](NM-3.8_Circuit_Applications.md)
