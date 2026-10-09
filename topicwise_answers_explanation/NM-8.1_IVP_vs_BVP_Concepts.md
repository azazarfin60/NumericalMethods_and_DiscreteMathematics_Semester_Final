---
title: "NM-8.1 · IVP vs BVP Concepts"
tags:
  - numerical-methods
  - discrete-mathematics
  - topicwise
---

# NM-8.1 · IVP vs BVP Concepts

Every block below is copied from `../answers_explanation/`. The reasoning
is written once, in the year-wise file, and is not restated here.


### [2021 Q.5(a)]

**Question.** Define boundary value and initial value problem.

*[Marks: 02, CO: 2]*

**Solution.**

**Initial value problem (IVP).** A differential equation together with conditions
given at a **single** point, for example $y(0) = 1$. The solution can be marched
forward from that point because each new value depends only on the values already
computed.

**Boundary value problem (BVP).** A differential equation together with conditions
given at **both ends** of the interval, for example $y(0) = 0$ and $y(1) = 1$. No
starting value is known, so the whole interval must be solved at once.

| | IVP | BVP |
| :-- | :-- | :-- |
| Conditions | At one end | At both ends |
| How it is solved | March forward step by step | Solve the full algebraic system |
| Resulting system | Lower triangular | Tridiagonal for a second-order ODE |
| Cost | Very low per step | Full linear solve |
| Sensitivity | Local; errors stay near the start | Global; a change anywhere moves the whole solution |
| Shooting method | Not applicable | Reduces it to an IVP by tuning the unknown start value |

$$\boxed{\text{IVP: conditions at one end, march forward. BVP: conditions at both ends, solve together.}}$$

**Finite difference form for a second-order BVP.** Discretise the interval into
$n+1$ points, replace $y''$ by the centred difference, and use the boundary
conditions to replace the two unavailable end rows:

$$
\begin{cases}
y_0 = \text{given}, \\
y_{i-1} - (2 - p(x_i)h^2 - q(x_i)h^4)\,y_i + y_{i+1} = r_i h^2, \quad 1 \le i \le n-1 \\
y_n = \text{given}
\end{cases}
$$

> [!note] Why the distinction is not academic
> Marching forward is cheap but only works **one way**. A BVP has no starting
> value, so the discretisation produces a tridiagonal system that must be solved
> as a whole.
>
> The **shooting method** bridges the gap: treat the unknown start value as the
> unknown, march forward as an IVP, measure the error at the far end, and adjust.
> That converts a BVP into a root-find on one number, which is why shooting works
> with any ODE solver. It is also why shooting is fragile when the ODE is
> unstable: the forward solution amplifies, and the adjustment needed becomes
> exponentially large.

---

---

**Also asked here.**

- *2024 Q.4(a)* is the same question as [[NM-8.8|NM-8.8]], which is written in `NM-8.8`.

---
