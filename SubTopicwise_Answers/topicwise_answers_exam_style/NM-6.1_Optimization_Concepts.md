---
title: "NM-6.1 · Optimization Concepts"
tags:
  - numerical-methods
  - discrete-mathematics
  - topicwise
---



[🏠 Subtopic Index](00_Index.md) | [← Prev: NM-5.7 Applied Integration](NM-5.7_Applied_Integration.md) | [Next: NM-6.2 One-Dimensional Unconstrained Optimization →](NM-6.2_One_Dimensional_Unconstrained_Optimization.md)

---

# NM-6.1 · Optimization Concepts

Every block below is copied from `../answers_exam_style/`, which is the
only place an answer is authored. A number here is the same number, character
for character, as the one it came from.


### [2021 Q.6(d)]

**Question.** Differentiate between constrained and unconstrained optimization.

**Solution.**

**Unconstrained optimization.** No restrictions. Choose $x$ freely in the whole
domain to maximise or minimise $f(x)$.

$$
\text{minimise } f(x_1, x_2, \dots, x_n), \qquad x \in \mathbb{R}^n
$$

Example: fit $y = a + bx$ to data by least squares. Nothing forbids any $a$ or $b$,
hence it is unconstrained.

**Constrained optimization.** Extra conditions must hold. Each restriction is
written as $g(x) \le 0$ or $h(x) = 0$.

$$
\text{minimise } f(x) \quad \text{subject to } \quad g_i(x) \le 0,\ i = 1\dots m, \quad h_j(x) = 0
$$

Example: minimise the weight of a truss subject to every member carrying at most
its rated load, or maximise a portfolio return subject to total risk staying under a
limit.

| | Unconstrained | Constrained |
| :-- | :-- | :-- |
| Restrictions | None | Equality and inequality conditions |
| Stationarity test | $\nabla f = 0$ | KKT multipliers: $\nabla f + \sum \mu_i \nabla g_i + \sum \lambda_j \nabla h_j = 0$ |
| Lagrange multipliers | Not needed | Essential |
| Optimum may be at | An interior point | A point on the boundary |
| Feasible region | Whole space | A subset |
| Harder | Easier | Harder; more constraints mean more cases |

**Why the distinction matters.** The unconstrained case is solved by finding where
the gradient vanishes. The constrained case must also satisfy every restriction, and
the optimum frequently sits **on** a boundary, where the plain gradient test is
useless. That is exactly why Lagrange multipliers exist.

$$
\boxed{\text{Unconstrained: choose freely. Constrained: obey rules, solved with multipliers}}
$$

---

[🏠 Subtopic Index](00_Index.md) | [← Prev: NM-5.7 Applied Integration](NM-5.7_Applied_Integration.md) | [Next: NM-6.2 One-Dimensional Unconstrained Optimization →](NM-6.2_One_Dimensional_Unconstrained_Optimization.md)
