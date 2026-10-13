---
title: "NM-7.4 · Applied Differentiation"
tags:
  - numerical-methods
  - discrete-mathematics
  - topicwise
---


[🏠 Subtopic Index](00_Index.md) | [← Prev: NM-7.3 Second Derivative & Formula Derivation](NM-7.3_Second_Derivative_and_Formula_Derivation.md) | [Next: NM-8.1 IVP vs BVP Concepts →](NM-8.1_IVP_vs_BVP_Concepts.md)

---

# NM-7.4 · Applied Differentiation

Every block below is copied from `../answers_explanation/`. The reasoning
is written once, in the year-wise file, and is not restated here.


### [2021 Q.6(a)]

**Question.** Write down a real-life application of numerical differentiation.

*[Marks: 02, CO: 2]*

**Solution.**

**Velocity and acceleration from position data.**

A vehicle's position $x(t)$ is logged by GPS, or a vibrating mass's displacement
is recorded by an accelerometer. Neither instrument measures velocity directly,
yet both are needed for control. The derivative is obtained from the finite
difference

$$
v(t) = \frac{x(t+h) - x(t-h)}{2h}
$$

$$\boxed{\text{GPS or accelerometer data gives position; the numerical derivative gives velocity and acceleration}}$$

Second application: finding the **peak** of a sampled signal, such as the peak
acceleration in a crash test, where the maximum of the numerical derivative locates
the maximum of the original.

> [!note] Why this application needs numerical differentiation at all
> A GPS receiver integrates satellite timing signals to produce position, and an
> accelerometer integrates its proof mass to produce displacement. In both cases
> **position is the measured quantity and velocity is not.** Somebody has to take
> the derivative, and in the field that is always done by finite differences.
>
> So numerical differentiation is not a convenience here. It is the only route
> from the instrument's output to the quantity the controller needs.

> [!warning] The optimal step size is a real trade-off, and knowing its order matters
> Accuracy is $O(h^2)$, so halving $h$ cuts the truncation error by 4. But round
> off grows as $1/h$, because the difference of two nearly equal numbers loses
> significant digits. Halving $h$ therefore multiplies the round off error by 2.
>
> The two cross at $h \approx \varepsilon^{1/3}$, where $\varepsilon$ is the machine
> epsilon, about $6 \times 10^{-6}$ in double precision. The optimal step is
> therefore near $1.8 \times 10^{-2}$, not "as small as possible". Making $h$
> smaller makes the answer worse, which is counter-intuitive enough to be worth
> remembering.

---

---

**Also asked here.**

- *2019 Q.6(b)* is the same question as [[NM-7.2_First_Derivative_from_Tabulated_Data|NM-7.2]], which is written in `NM-7.2`.
- *2020 Q.6(c)* is the same question as [[NM-7.2_First_Derivative_from_Tabulated_Data|NM-7.2]], which is written in `NM-7.2`.

---

[🏠 Subtopic Index](00_Index.md) | [← Prev: NM-7.3 Second Derivative & Formula Derivation](NM-7.3_Second_Derivative_and_Formula_Derivation.md) | [Next: NM-8.1 IVP vs BVP Concepts →](NM-8.1_IVP_vs_BVP_Concepts.md)
