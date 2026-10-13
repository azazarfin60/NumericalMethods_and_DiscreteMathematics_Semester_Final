---
title: "NM-5.3 · Simpson's 3/8 Rule"
tags:
  - numerical-methods
  - discrete-mathematics
  - topicwise
---



[🏠 Subtopic Index](00_Index.md) | [← Prev: NM-5.2 Simpson's 1/3 Rule](NM-5.2_Simpsons_1_3_Rule.md) | [Next: NM-5.4 Rule Comparison & Step Constraints →](NM-5.4_Rule_Comparison_and_Step_Constraints.md)

---

# NM-5.3 · Simpson's 3/8 Rule

Every block below is copied from `../answers_explanation/`. The reasoning
is written once, in the year-wise file, and is not restated here.


### [2019 Q.7(b)]

**Question.** Evaluate, $\int_1^2 (x^2 + 1) \, dx$ using Simpson's 3/8 rule.

*[Marks: 04]*

**Solution.**

Simpson's **3/8 rule** applies over three subintervals, using four nodes. Over
$[1, 2]$, take $n = 3$, so

$$h = \frac{2 - 1}{3} = \frac{1}{3}, \qquad x = 1,\ \frac{4}{3},\ \frac{5}{3},\ 2$$

The ordinates:

$$f(1) = 1 + 1 = 2$$

$$f\!\left(\frac{4}{3}\right) = \frac{16}{9} + 1 = \frac{25}{9} \approx 2.777778$$

$$f\!\left(\frac{5}{3}\right) = \frac{25}{9} + 1 = \frac{34}{9} \approx 3.777778$$

$$f(2) = 4 + 1 = 5$$

$$\int_1^2(x^2 + 1)\,dx \approx \frac{3h}{8}\left[f_0 + 3f_1 + 3f_2 + f_3\right]$$

$$= \frac{3}{8}\cdot\frac{1}{3}\left[2 + 3\left(\frac{25}{9}\right) + 3\left(\frac{34}{9}\right) + 5\right]$$

$$= \frac{1}{8}\left[2 + \frac{25}{3} + \frac{34}{3} + 5\right] = \frac{1}{8}\left[7 + \frac{59}{3}\right] = \frac{1}{8}\cdot\frac{80}{3} = \frac{10}{3}$$

$$\boxed{\int_1^2(x^2 + 1)\,dx = \frac{10}{3} = 3.3333}$$

> [!warning] The subinterval count is 3, and using 4 gives a wrong answer
> The 3/8 rule needs a **multiple of three** intervals, not an even number. Taking
> $n = 3$ gives $h = \frac{1}{3}$ and the four nodes $1, \frac{4}{3}, \frac{5}{3}, 2$.
>
> Taking $n = 4$ on the same interval gives $h = 0.25$ and nodes at
> $1, 1.25, 1.5, 1.75, 2$, which is **five** nodes, and the 3/8 rule has only four
> weights. Applying it there and getting $4.5586$ instead of $3.3333$ is the standard
> error, and it is a large one.
>
> The distinction that separates the two Simpson rules is worth holding on to:
> **1/3 needs an even count, 3/8 needs a multiple of 3.**

> [!info] Check by direct integration
> Antidifferentiating, $\int_1^2(x^2+1)dx = \left[\dfrac{x^3}{3} + x\right]_1^2 = \left(\dfrac{8}{3} + 2\right) - \left(\dfrac{1}{3} + 1\right) = \dfrac{7}{3} + 1 = \dfrac{10}{3}$, exactly
> the value the rule returns. The rule integrates cubics exactly and the integrand
> is only quadratic, so agreement is the expected outcome rather than a
> coincidence; the check confirms that the subinterval count was set to $3$ as
> the $3/8$ rule requires and that no weight was mistyped.

---

[🏠 Subtopic Index](00_Index.md) | [← Prev: NM-5.2 Simpson's 1/3 Rule](NM-5.2_Simpsons_1_3_Rule.md) | [Next: NM-5.4 Rule Comparison & Step Constraints →](NM-5.4_Rule_Comparison_and_Step_Constraints.md)
