---
title: "NM-8.7 · ODE Formulation from Physical Problems"
tags:
  - numerical-methods
  - discrete-mathematics
  - topicwise
---



[🏠 Subtopic Index](00_Index.md) | [← Prev: NM-8.6 Higher-Order & Systems of ODEs](NM-8.6_Higher_Order_and_Systems_of_ODEs.md) | [Next: NM-8.8 Boundary Value Problems →](NM-8.8_Boundary_Value_Problems.md)

---

# NM-8.7 · ODE Formulation from Physical Problems

Every block below is copied from `../answers_explanation/`. The reasoning
is written once, in the year-wise file, and is not restated here.


### [2021 Q.5(c)]

**Question.** A capacitor loses 4% of its remaining charge every second. It is fully charged with 100 Coulomb of charge. What will be the remaining charge after 10 sec. Develop the ODE and also determine the solution.

*[Marks: 05, CO: 2]*

**Solution.**

**Step 1. Set up the rate equation.** Losing $4\%$ of the *remaining* charge each
second means the loss is **proportional to the charge present**, not a constant
$4$ C per second. If $Q$ is the charge and $t$ the time,

$$
\frac{dQ}{dt} = -0.04\,Q, \qquad Q(0) = 100
$$

> [!warning] The phrase "of its remaining charge" is the whole question
> Two readings are available and they differ by $0.8\%$.
>
> | Reading | Value | Character |
> | :-- | --: | :-- |
> | Continuous exponential | 67.0320 | The physically correct law. Each individual decay is small, so compounding is continuous |
> | Discrete $0.96^n$ | 66.4833 | Treats each second as one exact $4\%$ step. Slightly under, since $1-0.04 < e^{-0.04}$ |
>
> The general identity is $(1-r)^n < e^{-rn}$ for $0<r<1$, so the discrete answer
> always under-reads. A capacitor really does decay continuously, so $67.0320$ is
> the intended answer, and the ODE the question asks you to develop is the
> exponential one.
>
> The trap is writing $Q' = -4$. That is a constant loss of 4 Coulombs per second,
> which would give $Q(10) = 60$ and is a different physical situation entirely.

The negative sign is essential: the charge is decreasing.

**Step 2. Solve by separation of variables.**

$$
\frac{dQ}{Q} = -0.04\,dt
$$

Integrating,

$$
\ln Q = -0.04\,t + C
$$

At $t = 0$, $\ln 100 = C$, so

$$
Q(t) = 100\,e^{-0.04t}
$$

**Step 3. Evaluate at $t = 10$ s.**

$$
Q(10) = 100\,e^{-0.4} = 100(0.670320046) = 67.0320
$$

$$\boxed{Q(10) = 67.03 \text{ Coulomb}}$$

> [!info] Check by an independent route
> **Discrete compounding.** "Loses 4% of its remaining charge every second" read
> literally gives, second by second,
> $$Q(10) = 100(0.96)^{10} = 66.4833$$
> **Euler's method** with $h = 1$, which is exactly that recursion, returns
> $Q(10) = 66.4833$ as well: $96$, $92.16$, ... $66.4833$.

> [!note] Half-life as a check
> From $Q(t) = Q_0e^{-t/\tau}$ with $\tau = 25$ s, the half-life is $\tau\ln 2 = 17.33$ s.
> So in 10 s the charge should be somewhat **more** than half of 100, which is
> exactly what 67.03 shows.
>
> A reading of 66.48 also passes that test, which is why it is worth noticing that
> a sanity check cannot separate these two readings. When two readings differ by
> less than a percent, the check has to be a different method rather than a
> plausibility test.

> [!note] Generalising the form
> Every first-order decay problem has the shape $Q' = -kQ$ with
> $Q(t) = Q_0e^{-kt}$, and the two useful numbers are the time constant $\tau = 1/k$
> and the half-life $\frac{\ln 2}{k}$. Working in half-lives is often easier than
> working in $e$'s: at 10 s the capacitor has been discharging for
> $10/17.33 = 0.577$ half-lives, so it holds $2^{-0.577} = 0.670$ of its charge.

---

---

[🏠 Subtopic Index](00_Index.md) | [← Prev: NM-8.6 Higher-Order & Systems of ODEs](NM-8.6_Higher_Order_and_Systems_of_ODEs.md) | [Next: NM-8.8 Boundary Value Problems →](NM-8.8_Boundary_Value_Problems.md)
