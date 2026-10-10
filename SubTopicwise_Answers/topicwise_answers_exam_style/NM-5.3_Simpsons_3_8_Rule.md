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

Every block below is copied from `../answers_exam_style/`, which is the
only place an answer is authored. A number here is the same number, character
for character, as the one it came from.


### [2019 Q.7(b)]

**Question.** Evaluate, $\int_1^2 (x^2 + 1) \, dx$ using Simpson's 3/8 rule.

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

> [!info] Check by direct integration
> Antidifferentiating, $\int_1^2(x^2+1)dx = \left[\dfrac{x^3}{3} + x\right]_1^2 = \left(\dfrac{8}{3} + 2\right) - \left(\dfrac{1}{3} + 1\right) = \dfrac{7}{3} + 1 = \dfrac{10}{3}$, exactly
> the value the rule returns. The rule integrates cubics exactly and the
> integrand is only quadratic, so agreement is the expected outcome rather than a
> coincidence; the check confirms that the subinterval count was set to $3$ as
> the $3/8$ rule requires and that no weight was mistyped. Had the interval been
> left as one subinterval with $h = 1$, the four-node formula could not be
> applied at all, which is the error to avoid when the limits give a single
> interval.

---

[🏠 Subtopic Index](00_Index.md) | [← Prev: NM-5.2 Simpson's 1/3 Rule](NM-5.2_Simpsons_1_3_Rule.md) | [Next: NM-5.4 Rule Comparison & Step Constraints →](NM-5.4_Rule_Comparison_and_Step_Constraints.md)
