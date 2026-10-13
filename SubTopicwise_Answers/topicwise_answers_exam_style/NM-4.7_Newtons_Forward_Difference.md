---
title: "NM-4.7 · Newton's Forward Difference"
tags:
  - numerical-methods
  - discrete-mathematics
  - topicwise
---


[🏠 Subtopic Index](00_Index.md) | [← Prev: NM-4.6 Lagrange's Interpolation](NM-4.6_Lagranges_Interpolation.md) | [Next: NM-4.9 Newton's Divided Difference / General Interpolation →](NM-4.9_Newtons_Divided_Difference_and_General_Interpolation.md)

---

# NM-4.7 · Newton's Forward Difference

Every block below is copied from `../answers_exam_style/`, which is the
only place an answer is authored. A number here is the same number, character
for character, as the one it came from.


### [2020 Q.5(a)]

**Question.** Deduce the Newton's forward difference interpolating polynomial.

**Solution.**

**The result.**

$$y_n(x) = y_0 + p\Delta y_0 + \frac{p(p-1)}{2!}\Delta^2 y_0 + \frac{p(p-1)(p-2)}{3!}\Delta^3 y_0 + \cdots + \frac{p(p-1)(p-2)\cdots(p-n+1)}{n!}\Delta^n y_0$$

with $p = \dfrac{x - x_0}{h}$ and $h$ the common spacing.

**Derivation.**

**Step 1. Set up.** Take $n+1$ equally spaced points $x_i = x_0 + ih$, with
$y_i = f(x_i)$ and $h = x_1 - x_0$. Write the target as $x = x_0 + ph$ so
$p = \frac{x - x_0}{h}$.

**Step 2. Newton's general form.** For arbitrary nodes the interpolating
polynomial is the Newton form

$$P_n(x) = f[x_0] + f[x_0,x_1](x-x_0) + f[x_0,x_1,x_2](x-x_0)(x-x_1) + \cdots$$

where $f[x_i, \dots, x_{i+k}]$ is a **divided difference**, defined
recursively by $f[x_i] = f(x_i)$ and

$$f[x_i, \dots, x_{i+k}] = \frac{f[x_{i+1},\dots,x_{i+k}] - f[x_i,\dots,x_{i+k-1}]}{x_{i+k} - x_i}$$

**Step 3. The special case of equal spacing.** When the nodes are equally spaced
the divided differences collapse onto ordinary finite differences:

$$
f[x_i, x_{i+1}, \dots, x_{i+k}] = \frac{\Delta^k y_i}{k!\,h^k}
$$

This is the key identity. To see why, the first divided difference on equal
steps is $\frac{y_{i+1} - y_i}{h} = \frac{\Delta y_i}{h}$. Each further
divided difference divides the difference of two $k!h^k$ multiples by one more
$h$ and by $k+1$, giving $(k+1)!h^{k+1}$. Induction finishes it.

**Step 4. Substitute into the Newton form.**

$$P_n(x) = y_0 + \frac{\Delta y_0}{1!h}(x-x_0) + \frac{\Delta^2 y_0}{2!h^2}(x-x_0)(x-x_1) + \frac{\Delta^3 y_0}{3!h^3}(x-x_0)(x-x_1)(x-x_2) + \cdots$$

**Step 5. Factor out the $h$.** Since $x - x_i = (p - i)h$, the product
$(x-x_0)(x-x_1)\cdots(x-x_{i-1}) = (p)(p-1)\cdots(p-i+1)h^i$. Substituting, the
$h^i$ in the numerator cancels the $h^i$ in the denominator:

$$
P_n(x) = y_0 + p\,\Delta y_0 + \frac{p(p-1)}{2!}\Delta^2 y_0 + \frac{p(p-1)(p-2)}{3!}\Delta^3 y_0 + \cdots
$$

**Step 6. The final form**, which is the box above.

**Another way to see it.** Expand $f$ in a Taylor series about $x_0$ and replace
each derivative by a finite difference, using $f^{(k)}(x_0) = \frac{\Delta^k y_0}{h^k}$:

$$f(x) = f(x_0) + p\,h f'(x_0) + \frac{p^2}{2!}h^2 f''(x_0) + \frac{p^3}{3!}h^3 f'''(x_0) + \cdots$$

The $h$'s cancel immediately, giving $y_0 + p\Delta y_0 + \frac{p^2}{2!}\Delta^2 y_0 + \cdots$. The
**only** difference from the standard formula is that the $p^2$ has become
$p(p-1)$ and the $p^3$ has become $p(p-1)(p-2)$. That substitution is not a
trick: the finite differences already carry the effect of the lower-order terms,
and replacing rising powers by falling products is what avoids double counting.

**Validity.** Accurate for $0 \le p \le n$, that is inside the table. Near the far
end use backward differences instead, and outside the table the result is an
extrapolation with the risks listed in Q.3(a). Part (b) applies this to unequally
spaced data, where divided differences are used instead.

> [!note] Where this is used again
> The forward form is applied in 2021 Q.4(b) and 2021 Q.4(c), and the backward
> form in 2020 Q.3(b). See
> [[NM-4.7_Newtons_Forward_Difference|NM-4.7 · Newton's Forward Difference]].

---

### [2021 Q.3(c), 2023 Q.2(a)]

**Appeared in:** 2021 Q.3(c), 2023 Q.2(a)

**Question.** Derive the Newton's forward interpolation formula: $y_n(x) = y_0 + p\Delta y_0 + \frac{p(p-1)}{2!}\Delta^2 y_0 + \frac{p(p-1)(p-2)}{3!}\Delta^3 y_0 + \cdots$

**Solution.**

**Set up.** Let the function $y = f(x)$ take values $y_0, y_1, y_2, \dots, y_n$ at $n+1$ equidistant points $x_0, x_1, x_2, \dots, x_n$ with constant step size $h$, such that $x_i = x_0 + ih$.

Assume the interpolating polynomial $P_n(x)$ of degree $n$ in the form:

$$
P_n(x) = a_0 + a_1(x - x_0) + a_2(x - x_0)(x - x_1) + a_3(x - x_0)(x - x_1)(x - x_2) + \cdots + a_n(x - x_0)(x - x_1)\cdots(x - x_{n-1})
$$

**Step 1. Determine the coefficients $a_0, a_1, a_2, \dots$ successively.**

- At $x = x_0$:
  $$y_0 = P_n(x_0) = a_0 \implies a_0 = y_0$$

- At $x = x_1 = x_0 + h$:
  $$y_1 = P_n(x_1) = a_0 + a_1(x_1 - x_0) = y_0 + a_1 h$$
  $$a_1 = \frac{y_1 - y_0}{h} = \frac{\Delta y_0}{1!\,h}$$

- At $x = x_2 = x_0 + 2h$:
  $$y_2 = P_n(x_2) = a_0 + a_1(x_2 - x_0) + a_2(x_2 - x_0)(x_2 - x_1) = y_0 + a_1(2h) + a_2(2h)(h)$$
  $$y_2 = y_0 + 2\Delta y_0 + 2h^2 a_2$$
  Since $\Delta^2 y_0 = y_2 - 2y_1 + y_0 = y_2 - 2(y_0 + \Delta y_0) + y_0 = y_2 - y_0 - 2\Delta y_0$:
  $$2h^2 a_2 = \Delta^2 y_0 \implies a_2 = \frac{\Delta^2 y_0}{2!\,h^2}$$

- By induction, the general coefficient is:
  $$a_k = \frac{\Delta^k y_0}{k!\,h^k}, \qquad k = 0, 1, 2, \dots, n$$

**Step 2. Express in terms of the dimensionless variable $p$.**

Let $x = x_0 + ph$, so that $p = \frac{x - x_0}{h}$. Then:
$$x - x_0 = ph$$
$$x - x_1 = x_0 + ph - (x_0 + h) = (p - 1)h$$
$$x - x_2 = (p - 2)h, \quad \dots, \quad x - x_{k-1} = (p - k + 1)h$$

The product of factors becomes:
$$(x - x_0)(x - x_1)\cdots(x - x_{k-1}) = (ph)((p-1)h)\cdots((p-k+1)h) = p(p-1)\cdots(p-k+1)\,h^k$$

**Step 3. Substitute $a_k$ and product factors into $P_n(x)$.**

$$a_k (x - x_0)(x - x_1)\cdots(x - x_{k-1}) = \frac{\Delta^k y_0}{k!\,h^k} \cdot p(p-1)\cdots(p-k+1)\,h^k = \frac{p(p-1)\cdots(p-k+1)}{k!}\Delta^k y_0$$

Cancelling $h^k$ term by term yields Newton's forward interpolation formula:

$$
\boxed{y_n(x) = y_0 + p\Delta y_0 + \frac{p(p-1)}{2!}\Delta^2 y_0 + \frac{p(p-1)(p-2)}{3!}\Delta^3 y_0 + \cdots + \frac{p(p-1)\cdots(p-n+1)}{n!}\Delta^n y_0}
$$

**Validity range.** The formula is accurate for $0 \le p \le 1$, primarily near the beginning of equidistant tables. For values near the end, backward differences are used.

> [!info] Alternate proof via Shift Operator $E$
> Using the relationship $E = 1 + \Delta$:
> $$y(x) = y(x_0 + ph) = E^p y_0 = (1 + \Delta)^p y_0$$
> Expanding $(1 + \Delta)^p$ by the binomial theorem:
> $$(1 + \Delta)^p = 1 + p\Delta + \frac{p(p-1)}{2!}\Delta^2 + \frac{p(p-1)(p-2)}{3!}\Delta^3 + \cdots$$
> Operating on $y_0$ immediately gives the formula.

> [!note] Where this is used again
> Part (d) applies this with $y = x^4$, and 2021 Q.4(b) applies central difference formulas to a table of $e^x$ values. See [[NM-4.7_Newtons_Forward_Difference|NM-4.7 · Newton's Forward Difference]].

---

### [2022 Q.2(c)]

**Question.** Using Newton's forward difference formula find the sum $S_n = 1^3 + 2^3 + 3^3 + \cdots + n^3$.

**Solution.**

**Step 1. Set up the difference table.** Here $y = r^3$ with $r = 1, 2, 3, \dots$
and $h = 1$, so $u = r - 1$.

| $r$ | 1 | 2 | 3 | 4 | 5 | $\cdots$ |
| --- | --: | --: | --: | --: | --: | :-- |
| $y = r^3$ | 1 | 8 | 27 | 64 | 125 | |
| $\Delta y$ | 7 | 19 | 37 | 61 | | |
| $\Delta^2 y$ | 12 | 18 | 24 | | | |
| $\Delta^3 y$ | 6 | 6 | | | | |
| $\Delta^4 y$ | 0 | | | | | |

**Step 2. Write the series.** With $y_0 = 1$, $\Delta y_0 = 7$,
$\Delta^2 y_0 = 12$, $\Delta^3 y_0 = 6$ and $\Delta^4 y_0 = 0$:

$$
y(u) = 1 + 7u + 12\frac{u(u-1)}{2!} + 6\frac{u(u-1)(u-2)}{3!}
$$

$$
= 1 + 7u + 6u(u-1) + u(u-1)(u-2) = 1 + 7u + 6u^2 - 6u + u^3 - 3u^2 + 2u
$$

$$
= u^3 + 3u^2 + 3u + 1 = (u+1)^3
$$

The series returns $r^3$ exactly, as it must, since $r^3$ is itself a cubic.

**Step 3. Sum from $u = 0$ to $u = n-1$.**

$$
S_n = \sum_{u=0}^{n-1}\left[1 + 7u + 6u(u-1) + u(u-1)(u-2)\right]
$$

Use $\sum_{u=0}^{n-1} 1 = n$, $\sum u = \frac{n(n-1)}{2}$,
$\sum u(u-1) = 2\sum\binom{u}{2} = 2\binom{n}{3} = \frac{n(n-1)(n-2)}{3}$ and
$\sum u(u-1)(u-2) = 6\sum\binom{u}{3} = 6\binom{n}{4} = \frac{n(n-1)(n-2)(n-3)}{4}$:

$$
S_n = n + 7\cdot\frac{n(n-1)}{2} + 6\cdot\frac{n(n-1)(n-2)}{3} + \frac{n(n-1)(n-2)(n-3)}{4}
$$

$$
= n + \frac{7n(n-1)}{2} + 2n(n-1)(n-2) + \frac{n(n-1)(n-2)(n-3)}{4}
$$

Putting over the common denominator 4 and collecting:

$$
S_n = \frac{4n + 14n(n-1) + 8n(n-1)(n-2) + n(n-1)(n-2)(n-3)}{4}
$$

Expanding each term, $4n$, $14n^2 - 14n$, $8n^3 - 24n^2 + 16n$,
$n^4 - 6n^3 + 11n^2 - 6n$, the sum is

$$
n^4 + 2n^3 + n^2 = n^2(n+1)^2
$$

$$
\boxed{S_n = \left[\frac{n(n+1)}{2}\right]^2}
$$

> [!info] Check
> Direct evaluation for $n = 1$ to $6$ gives $1, 9, 36, 100, 225, 441$, and the
> closed form gives $\left[\frac{n(n+1)}{2}\right]^2 = 1, 9, 36, 100, 225, 441$.
> All six agree.
>
> Note also that the difference table has $\Delta^4 y_0 = 0$, confirming $r^3$ is
> a cubic and that the Newton series terminates. The general form is the same:
> for any polynomial of degree $k$ in $r$, the $k$-th forward difference is
> constant and the $(k+1)$-th is zero.

---

---

**Also asked here.**

- *2021 Q.3(b)* is the same question as [[NM-4.6_Lagranges_Interpolation|NM-4.6]], which is written in `NM-4.6`.

---

**Answered in phase P6, in `../CT_Questions/`.**

- *CT-02A Q.2* is a class-test question. Its answer is in `../CT_Questions/CT_answers_exam_style.md`, with the reasoning in `../CT_Questions/CT_answers_explanation.md`.

---

[🏠 Subtopic Index](00_Index.md) | [← Prev: NM-4.6 Lagrange's Interpolation](NM-4.6_Lagranges_Interpolation.md) | [Next: NM-4.9 Newton's Divided Difference / General Interpolation →](NM-4.9_Newtons_Divided_Difference_and_General_Interpolation.md)
