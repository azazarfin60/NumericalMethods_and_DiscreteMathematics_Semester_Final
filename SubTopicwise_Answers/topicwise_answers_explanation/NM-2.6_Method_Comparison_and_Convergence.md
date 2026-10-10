---
title: "NM-2.6 · Method Comparison & Convergence"
tags:
  - numerical-methods
  - discrete-mathematics
  - topicwise
---





[🏠 Subtopic Index](00_Index.md) | [← Prev: NM-2.5 Secant Method](NM-2.5_Secant_Method.md) | [Next: NM-2.7 Roots of Polynomials →](NM-2.7_Roots_of_Polynomials.md)

---

# NM-2.6 · Method Comparison & Convergence

Every block below is copied from `../answers_explanation/`. The reasoning
is written once, in the year-wise file, and is not restated here.


### [2020 Q.2(a)]

**Question.** Define roots of an equation. List the comparisons among bisection, secant, false position and Newton-Raphson methods.

*[Marks: 06]*

**Solution.**

**Root of an equation.** A **root** of $f(x) = 0$ is a value $x^*$ with $f(x^*) = 0$.
The graph of $f$ crosses or touches the $x$-axis at $x^*$.

A root is **simple** if $f'(x^*) \ne 0$, and **multiple** (or repeated) if
$f'(x^*) = 0$. The distinction matters because the methods below all assume a
simple root; a repeated root makes their convergence much slower.

A root is **explicit** if it can be written in closed form, and **implicit** if it
can only be found numerically. $\sqrt{2}$ is explicit. The root of
$x^5 - x - 1 = 0$ is implicit.

**The four methods compared.**

| | Bisection | False position | Secant | Newton-Raphson |
| :-- | :-- | :-- | :-- | :-- |
| Type | Bracketing | Bracketing | Open | Open |
| Needs $f'$ | No | No | No | **Yes** |
| Needs a sign change | **Yes** | **Yes** | No | No |
| Information used | Endpoints only | Endpoints, keeps one fixed | Last **two** points | Value **and** slope at one point |
| New point from | Midpoint | Chord crossing | Chord through last two | Tangent at last point |
| Convergence order | 1 (linear) | 1, often faster | 1.618 (golden ratio) | **2 (quadratic)** |
| Starts from | $a_0$ | $a_0$ | $x_0, x_1$ | $x_0$ only |
| Guaranteed | **Yes**, from any valid bracket | **Yes** | No | No |
| Function calls per step | 1 | 1 | 1 | 2 (value and derivative) |
| Weakness | Slow, and halves the interval | Stalls on one side for strong convexity | Can diverge, can lose the bracket | Sensitive to the start |

$$\boxed{\text{Bracketing methods are safe and slow; open methods are fast and unguaranteed}}$$

**How they relate.** They form a ladder from safest to fastest.

- **Bisection** is the safety net. It only needs a sign change, and it can never
  fail. That guarantee is why it survives in production codes.
- **False position** uses the same bracket but wastes it, because it keeps only
  one endpoint and lets the other run away. Faster than bisection, but it stalls
  on strongly convex functions, as 2021 Q.2(b) shows on $x^{2.2} = 69$.
- **Secant** throws the bracket away and fits a line through the last two
  points. The order $1.618$ is better than the labels "linear" suggest.
- **Newton** throws away the history except one point and uses the slope. It
  converges quadratically, so it is the method of choice when $f'$ is available
  and the start is good.

**The practical rule.** Keep a bracket. Try Newton. If a step leaves the bracket,
take a bisection step instead. This hybrid keeps Newton's speed and bisection's
guarantee, and it is what real root finders do.

> [!note] Why the "golden ratio" order is worth remembering
> The secant method's order $1.618 = \frac{1+\sqrt5}{2}$ is what makes it a real
> alternative to Newton rather than a consolation prize. It needs no derivative,
> and it is still superlinear.
>
> Compare the cost lines in the table: secant makes one function call per step,
> Newton makes two. Where $f'$ is expensive or genuinely unavailable, the secant
> method's order per function evaluation is actually competitive.
>
> The price is that the secant has no guarantee at all, while bisection does, and
> in a production code the guarantee is usually worth more than the order.

---

---

**Also asked here.**

- *CT-01 Q.2(b)* is the same question as [[NM-2.3_False_Position_and_Regula_Falsi|NM-2.3]], which is written in `NM-2.3`.

---

**Answered in phase P6, in `../CT_Questions/`.**

- *CT-01 Q.2(a)* is a class-test question. Its answer is in `../CT_Questions/CT_answers_exam_style.md`, with the reasoning in `../CT_Questions/CT_answers_explanation.md`.

---

[🏠 Subtopic Index](00_Index.md) | [← Prev: NM-2.5 Secant Method](NM-2.5_Secant_Method.md) | [Next: NM-2.7 Roots of Polynomials →](NM-2.7_Roots_of_Polynomials.md)
