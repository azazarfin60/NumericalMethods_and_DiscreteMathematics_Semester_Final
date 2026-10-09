---
title: "NM-7.4 · Applied Differentiation"
tags:
  - numerical-methods
  - discrete-mathematics
  - topicwise
---

# NM-7.4 · Applied Differentiation

Every block below is copied from `../answers_exam_style/`, which is the
only place an answer is authored. A number here is the same number, character
for character, as the one it came from.


### [2021 Q.6(a)]

**Question.** Write down a real-life application of numerical differentiation.

**Solution.**

**Velocity and acceleration from position data.**

A vehicle's position $x(t)$ is logged by GPS, or a vibrating mass's displacement is
recorded by an accelerometer. Neither instrument measures velocity directly, yet
both are needed for control. The derivative is obtained from the finite difference

$$
v(t) = \frac{x(t+h) - x(t-h)}{2h}
$$

Accuracy is $O(h^2)$, and halving $h$ cuts the truncation error by 4 while
multiplying the round off error by 2, so the optimal $h$ sits where the two cross,
usually near the cube root of the machine epsilon.

Second application: finding the **peak** of a sampled signal, such as the peak
acceleration in a crash test, where the maximum of the numerical derivative locates
the maximum of the original.

$$
\boxed{\text{GPS or accelerometer data gives position; the numerical derivative gives velocity and acceleration}}
$$

---

---

**Also asked here.**

- *2019 Q.6(b)* is the same question as [[NM-7.2|NM-7.2]], which is written in `NM-7.2`.
- *2020 Q.6(c)* is the same question as [[NM-7.2|NM-7.2]], which is written in `NM-7.2`.

---
