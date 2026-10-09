---
title: "NM-6.1 · Optimization Concepts"
tags:
  - numerical-methods
  - discrete-mathematics
  - topicwise
---

# NM-6.1 · Optimization Concepts

Every block below is copied from `../answers_explanation/`. The reasoning
is written once, in the year-wise file, and is not restated here.


### [2021 Q.6(d)]

**Question.** Differentiate between constrained and unconstrained optimization.

*[Marks: 02, CO: 2]*

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
\text{minimise } f(x) \quad \text{subject to} \quad g_i(x) \le 0,\ i = 1\dots m, \quad h_j(x) = 0
$$

Example: minimise the weight of a truss subject to every member carrying at most
its rated load, or maximise a portfolio return subject to total risk staying under
a limit.

| | Unconstrained | Constrained |
| :-- | :-- | :-- |
| Restrictions | None | Equality and inequality conditions |
| Stationarity test | $\nabla f = 0$ | KKT multipliers: $\nabla f + \sum \mu_i \nabla g_i + \sum \lambda_j \nabla h_j = 0$ |
| Lagrange multipliers | Not needed | Essential |
| Optimum may be at | An interior point | A point on the boundary |
| Feasible region | Whole space | A subset |
| Harder | Easier | Harder; more constraints mean more cases |

$$\boxed{\text{Unconstrained: choose freely. Constrained: obey rules, solved with multipliers}}$$

> [!warning] The plain gradient test is not merely incomplete here, it is wrong
> In the unconstrained case the optimum satisfies $\nabla f = 0$. In the
> constrained case the optimum frequently sits **on** a boundary where the plain
> gradient test is useless: at a corner the feasible directions are restricted, so
> $f$ can be stationary in a sense that has nothing to do with $\nabla f$.
>
> The KKT conditions replace that with
> $\nabla f + \sum \mu_i \nabla g_i + \sum \lambda_j \nabla h_j = 0$ together with
> **complementary slackness**, $\mu_i \ge 0$ and $\mu_i g_i(x) = 0$. That second
> condition is the part people forget: a multiplier is nonzero only if its
> constraint is active. It is what encodes "the constraint bites exactly when it
> is touching".

---
