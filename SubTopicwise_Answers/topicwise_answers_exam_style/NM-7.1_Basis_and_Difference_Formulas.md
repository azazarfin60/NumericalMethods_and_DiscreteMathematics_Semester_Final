---
title: "NM-7.1 · Basis & Difference Formulas"
tags:
  - numerical-methods
  - discrete-mathematics
  - topicwise
---


[🏠 Subtopic Index](00_Index.md) | [← Prev: NM-6.3 Optima from Tabulated Data](NM-6.3_Optima_from_Tabulated_Data.md) | [Next: NM-7.2 First Derivative from Tabulated Data →](NM-7.2_First_Derivative_from_Tabulated_Data.md)

---

# NM-7.1 · Basis & Difference Formulas

Every block below is copied from `../answers_exam_style/`, which is the
only place an answer is authored. A number here is the same number, character
for character, as the one it came from.


### [2019 Q.6(a)]

**Question.** What is the basis of numerical differentiation? Write at least four difference equations to obtain numerical differentiation.

**Solution.**

**The basis.** A function known only at discrete points is replaced by a
polynomial that passes through those points, and the derivative of that
polynomial is used for the derivative of the function. Starting from the Taylor
series

$$f(x + h) = f(x) + hf'(x) + \frac{h^2}{2}f''(x) + \frac{h^3}{6}f'''(x) + \cdots$$

combinations of the series at neighbouring points cancel the terms that are not
wanted. Since the first omitted term is proportional to a power of $h$, the
result is an approximation with an error $O(h)$ or $O(h^2)$.

**Four difference equations.** With $h$ the tabular spacing and $f_n = f(x_n)$:

1. **Forward difference (two-point).**
$$f'(x_n) = \frac{f_{n+1} - f_n}{h}, \qquad \text{error } O(h)$$

2. **Backward difference (two-point).**
$$f'(x_n) = \frac{f_n - f_{n-1}}{h}, \qquad \text{error } O(h)$$

3. **Central difference (three-point).**
$$f'(x_n) = \frac{f_{n+1} - f_{n-1}}{2h}, \qquad \text{error } O(h^2)$$

4. **Forward difference (three-point).**
$$f'(x_n) = \frac{-3f_n + 4f_{n+1} - f_{n+2}}{2h}, \qquad \text{error } O(h^2)$$

5. **Central difference (five-point).**
$$f'(x_n) = \frac{f_{n-2} - 8f_{n-1} + 8f_{n+1} - f_{n+2}}{12h}, \qquad \text{error } O(h^4)$$

The central formulas are preferred where data exist on both sides, since their
error is $O(h^2)$ and above rather than $O(h)$, and their error constants are
smaller by the same factor.

---

[🏠 Subtopic Index](00_Index.md) | [← Prev: NM-6.3 Optima from Tabulated Data](NM-6.3_Optima_from_Tabulated_Data.md) | [Next: NM-7.2 First Derivative from Tabulated Data →](NM-7.2_First_Derivative_from_Tabulated_Data.md)
