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

Every block below is copied from `../answers_explanation/`. The reasoning
is written once, in the year-wise file, and is not restated here.


### [2022 Q.4(c)]

**Question.** Define ill-conditioned system.

*[Marks: 02, CO: 1]*

**Solution.**

**Definition.** A system of linear equations is **ill-conditioned** when a small
change in the input produces a disproportionately large change in the solution.

**Measure.** The **condition number** $\kappa$ of the coefficient matrix is the
ratio of the largest to the smallest relative error:

$$
\frac{\dfrac{\|\delta x\|}{\|x\|}}{\dfrac{\|\delta b\|}{\|b\|}} \le \kappa(A)
$$

So a relative error of $\epsilon$ in the data may become up to $\kappa\epsilon$ in
the answer.

| $\kappa$ | Behaviour |
| :-- | :-- |
| $\kappa = 1$ | Perfectly conditioned, error passes through unchanged |
| $\kappa \approx 10$ | Mild amplification |
| $\kappa \approx 10^{6}$ | Loss of about six significant digits |
| $\kappa > 10^{16}$ | All precision lost, the matrix is numerically singular |

**Causes.**

1. **A matrix that is nearly singular**, with an eigenvalue very close to zero
   or rows that are almost linearly dependent. Two nearly parallel equations
   constrain the solution very weakly.
2. **Rows or columns of wildly different magnitudes.** The small ones are
   effectively ignored.
3. **A bad choice of variables.** Two variables measuring nearly the same
   physical quantity make the corresponding columns almost equal.

$$\boxed{\text{ill-conditioned means small input errors produce large output errors; measured by }\kappa}$$

> [!warning] Conditioning is a property of the problem, not of the algorithm
> **Pivoting helps stability but does not change $\kappa$.** Switching to a better
> elimination order makes the computed answer closer to the exact answer of the
> system you were given; it does not make the system you were given better
> posed.
>
> This is the single most important distinction in the topic. A well-conditioned
> system solved badly gives a slightly wrong answer, and a badly conditioned
> system solved well gives a wildly wrong one. No amount of care in the
> algorithm repairs the second case.

> [!note] Why it matters in engineering
> The data itself has uncertainty, typically $10^{-4}$ relative from the
> instrument. With $\kappa = 10^{8}$ the answer then carries a relative
> uncertainty of $10^{4}$, which is useless, even though the computation ran to
> machine precision and printed fifteen digits.
>
> The remedies are all about the problem rather than the arithmetic: row or
> column scaling to make entries comparable, choosing better-conditioned
> variables, reformulating the physical problem, or using higher precision.

---

---

[🏠 Subtopic Index](00_Index.md) | [← Prev: NM-3.6 Relaxation](NM-3.6_Relaxation.md) | [Next: NM-3.8 Circuit Applications →](NM-3.8_Circuit_Applications.md)
