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

Every block below is copied from `../answers_exam_style/`, which is the
only place an answer is authored. A number here is the same number, character
for character, as the one it came from.


### [2021 Q.5(c)]

**Question.** A capacitor loses 4% of its remaining charge every second. It is fully charged with 100 Coulomb of charge. What will be the remaining charge after 10 sec. Develop the ODE and also determine the solution.

**Solution.**

**Step 1. Set up the rate equation.** Losing $4\%$ of the remaining charge each
second means the loss is **proportional to the charge present**, not a constant
$4$ C per second. If $Q$ is the charge and $t$ the time,

$$
\frac{dQ}{dt} = -0.04\,Q, \qquad Q(0) = 100
$$

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

$$
\boxed{Q(10) = 67.03 \text{ Coulomb}}
$$

> [!info] Check by an independent route
> **Discrete compounding.** "Loses 4% of its remaining charge every second" read
> literally gives, second by second,
> $$Q(10) = 100(0.96)^{10} = 66.4833$$
> **Euler's method** with $h = 1$, which is exactly that recursion, returns
> $Q(10) = 66.4833$ as well: $96$, $92.16$, ... $66.4833$.
>
> The continuous answer $67.0320$ is $0.8\%$ higher. Both are defensible readings
> of the question. The distinction is genuine:
>
> | Reading | Value | Character |
> | :-- | --: | :-- |
> | Continuous exponential | 67.0320 | The physically correct law. Each individual decay is small, so compounding is continuous |
> | Discrete $0.96^n$ | 66.4833 | Treats each second as one exact $4\%$ step. Slightly under, since $1-0.04 < e^{-0.04}$ |
>
> The general identity is $(1-r)^n < e^{-rn}$ for $0<r<1$, so the discrete answer
> always under-reads. A capacitor really does decay continuously, so
> $67.0320$ is the intended answer.

> [!note] Half-life as a check
> From $Q(t) = Q_0e^{-t/\tau}$ with $\tau = 25$ s, the half-life is
> $\frac{\tau \ln 2}{1} = 17.33$ s. So in 10 s the charge should be somewhat **more**
> than half of 100, which is exactly what 67.03 shows. A reading of 66.48 is also
> plausible on that test alone, which is why the two are hard to separate by
> inspection and why the cross-check above uses a different method rather than a
> sanity check.

---

---

[🏠 Subtopic Index](00_Index.md) | [← Prev: NM-8.6 Higher-Order & Systems of ODEs](NM-8.6_Higher_Order_and_Systems_of_ODEs.md) | [Next: NM-8.8 Boundary Value Problems →](NM-8.8_Boundary_Value_Problems.md)
