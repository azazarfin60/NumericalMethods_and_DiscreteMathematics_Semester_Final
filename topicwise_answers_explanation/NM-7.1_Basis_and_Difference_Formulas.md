---
title: "NM-7.1 · Basis & Difference Formulas"
tags:
  - numerical-methods
  - discrete-mathematics
  - topicwise
---

# NM-7.1 · Basis & Difference Formulas

Every block below is copied from `../answers_explanation/`. The reasoning
is written once, in the year-wise file, and is not restated here.


### [2019 Q.6(a)]

**Question.** What is the basis of numerical differentiation? Write at least four difference equations to obtain numerical differentiation.

*[Marks: 04]*

**Solution.**

**The basis.** A function known only at discrete points is replaced by a polynomial
that passes through those points, and the derivative of that polynomial is used for
the derivative of the function. Starting from the Taylor series

$$f(x + h) = f(x) + hf'(x) + \frac{h^2}{2}f''(x) + \frac{h^3}{6}f'''(x) + \cdots$$

combinations of the series at neighbouring points cancel the terms that are not
wanted. Since the first omitted term is proportional to a power of $h$, the result
is an approximation with an error $O(h)$ or $O(h^2)$.

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

The central formulas are preferred where data exist on both sides, since their error
is $O(h^2)$ and above rather than $O(h)$, and their error constants are smaller by
the same factor.

> [!warning] The cancellation is the reason for the denominator
> Look at what the central formula is doing:
> $$\frac{f_{n+1} - f_{n-1}}{2h}$$
> Two values of order $f$ are being subtracted, and the difference is of order
> $h f'$. So roughly $1/h$ significant digits are lost to cancellation before the
> division.
>
> That is why the **five-point** formula, with its coefficients $1, -8, 8, -1$,
> is not automatically better. It reaches $O(h^4)$ in truncation but cancels more
> heavily, and against data rounded to four decimals it can be the *worse* choice.
> Part (b) is an instance: the three-point central formula there gives the same
> answer as the five-point, not a worse one, because the data are so close to
> straight that the higher-order terms contribute almost nothing.
>
> **Order of accuracy is not the whole story.** There is an optimal $h$, and past
> it more points make the answer worse.

---
