---
title: "NM-4.9 · Newton's Divided Difference / General Interpolation"
tags:
  - numerical-methods
  - discrete-mathematics
  - topicwise
---



[🏠 Subtopic Index](00_Index.md) | [← Prev: NM-4.7 Newton's Forward Difference](NM-4.7_Newtons_Forward_Difference.md) | [Next: NM-4.10 Gauss Forward / Backward & Stirling's Formulas →](NM-4.10_Gauss_Forward_and_Backward_and_Stirlings_Formulas.md)

---

# NM-4.9 · Newton's Divided Difference / General Interpolation

Every block below is copied from `../answers_explanation/`. The reasoning
is written once, in the year-wise file, and is not restated here.


### [2019 Q.5(c)]

**Question.** Using Newton's general interpolation formula find $f(x)$ as a polynomial in $x$ for the following table. Also, determine $f(3.5)$ using the polynomial.

*[Marks: 04]*

**Solution.**

| $x$ | $-1$ | 0 | 3 | 6 | 7 |
| :---: | :---: | :---: | :---: | :---: | :---: |
| $f(x)$ | 3 | $-6$ | 39 | 822 | 1611 |

**Divided differences.** Each entry is
$f[x_i, \ldots, x_{i+k}] = \dfrac{f[x_{i+1}, \ldots, x_{i+k}] - f[x_i, \ldots, x_{i+k-1}]}{x_{i+k} - x_i}$.

| Order | Values |
| :---: | :--- |
| 0 | $3,\ -6,\ 39,\ 822,\ 1611$ |
| 1 | $\dfrac{-6-3}{0-(-1)} = -9$; $\dfrac{39-(-6)}{3-0} = 15$; $\dfrac{822-39}{6-3} = 261$; $\dfrac{1611-822}{7-6} = 789$ |
| 2 | $\dfrac{15-(-9)}{3-(-1)} = 6$; $\dfrac{261-15}{6-0} = 41$; $\dfrac{789-261}{7-3} = 132$ |
| 3 | $\dfrac{41-6}{6-(-1)} = 5$; $\dfrac{132-41}{7-0} = 13$ |
| 4 | $\dfrac{13-5}{7-(-1)} = 1$ |

**Newton's general (divided difference) form.**

$$f(x) = f[x_0] + f[x_0, x_1](x - x_0) + f[x_0, x_1, x_2](x - x_0)(x - x_1) + \cdots$$

$$f(x) = 3 - 9(x + 1) + 6(x + 1)x + 5(x + 1)x(x - 3) + (x + 1)x(x - 3)(x - 6)$$

**Expand to a polynomial in $x$.** Working outward from the last term:

$$(x + 1)x(x - 3)(x - 6) = x^4 - 8x^3 + 9x^2 + 18x$$

$$5(x + 1)x(x - 3) = 5(x^3 - 2x^2 - 3x) = 5x^3 - 10x^2 - 15x$$

$$6(x + 1)x = 6x^2 + 6x, \qquad -9(x + 1) = -9x - 9$$

Collecting all terms:

$$f(x) = x^4 - 3x^3 + 5x^2 - 6$$

$$\boxed{f(x) = x^4 - 3x^3 + 5x^2 - 6}$$

**Apply it to $f(3.5)$.** Substituting into the expanded form:

$$f(3.5) = 150.0625 - 128.625 + 61.25 - 6 = 76.6875$$

$$\boxed{f(3.5) = 76.6875}$$

> [!info] Check against the Newton form and the tabulated values
> Substituting $x = 3.5$ into the unevaluated Newton form gives
> $3 - 9(4.5) + 6(15.75) + 5(7.875) + (-19.6875) = 76.6875$, the same value by a
> second route. And substituting the polynomial back into the tabulated
> abscissae reproduces every printed entry: $f(-1) = 1 + 3 + 5 - 6 = 3$,
> $f(0) = -6$, $f(3) = 81 - 81 + 45 - 6 = 39$, $f(6) = 1296 - 648 + 180 - 6 = 822$,
> and $f(7) = 2401 - 1029 + 245 - 6 = 1611$. The table is recovered exactly, so
> the polynomial is the interpolation polynomial and no tabulated value is
> contradicted.

> [!note] The expansion is the part that gets skipped and should not be
> The Newton form and the expanded form are the same polynomial, and a common
> shortcut is to quote the Newton form and then evaluate $f(3.5)$ from it. That is
> perfectly valid arithmetic and produces the right number, but the question asks
> for the polynomial in $x$, so the expansion is part of the answer.
>
> **Expand from the outside in.** The highest-order product is the one with the
> most factors, so expand it first and work down. Working inward-out instead means
> carrying an unexpanded product through three lines, and the errors compound.

---

### [2020 Q.5(b)]

**Question.** Using Newton's divided difference interpolating polynomial estimate the value of signal $s(t)$ at $t = 2.25$ sec for the following tabulated values.

*[Marks: 06]*

**Solution.**

| $t$ | 0.5 | 0.2 | 1.4 | 2.2 | 3.0 |
| --- | --: | --: | --: | --: | --: |
| $s(t)$ | $-10.25$ | $-3.768$ | $5.976$ | $28.972$ | $79.0$ |

> [!warning] The table is printed out of order, and it turns out not to matter
> The $t$ column runs $0.5, 0.2, 1.4, 2.2, 3.0$, with $0.5$ printed **before**
> $0.2$. This looks like a typesetting slip, and it is worth checking what it does
> to the answer.
>
> **It changes nothing.** Newton's divided difference interpolation is
> **invariant under any permutation of the nodes**. Run it in the printed order
> and run it sorted, and every value of $s(2.25)$ is identical:
> $30.73362901$ in both cases, to ten decimals.
>
> The reason is short. The divided difference $f[x_0, x_1, \dots, x_k]$ is
> **symmetric** in its $k+1$ nodes, so reordering them does not change its value.
> And the product $(t-x_0)(t-x_1)\cdots(t-x_{k-1})$ covers the same set of factors
> whichever order they are listed in. Both halves of the formula are unchanged, so
> the polynomial is unchanged.
>
> Contrast this with the **forward difference** formula, where the leading
> diagonal $\Delta^k y_0$ is tied to $x_0$ and reordering the table destroys it.
> That is the real reason equal spacing and ascending order matter there and not
> here.

**Step 1. Build the divided difference table.** Each entry divides by the
$x$-difference of the two nodes it spans.

| Order | Values |
| :-- | :-- |
| $s(t_i)$ | $-10.250000$, $-3.768000$, $5.976000$, $28.972000$, $79.000000$ |
| $1^{st}$ | $-21.606667$, $8.120000$, $28.745000$, $62.535000$ |
| $2^{nd}$ | $33.029630$, $10.312500$, $21.118750$ |
| $3^{rd}$ | $-13.363017$, $3.859375$ |
| $4^{th}$ | $6.888957$ |

Worked entries, so nothing is asserted on trust:

$$
f[x_0,x_1] = \frac{-3.768 - (-10.25)}{0.2 - 0.5} = \frac{6.482}{-0.3} = -21.606667
$$

$$
f[x_1,x_2] = \frac{5.976 - (-3.768)}{1.4 - 0.2} = \frac{9.744}{1.2} = 8.12
$$

$$
f[x_0,x_1,x_2] = \frac{8.12 - (-21.606667)}{1.4 - 0.5} = \frac{29.726667}{0.9} = 33.029630
$$

$$
f[x_1,x_2,x_3] = \frac{f[x_2,x_3] - f[x_1,x_2]}{2.2 - 0.2}, \qquad f[x_2,x_3] = \frac{28.972 - 5.976}{2.2-1.4} = \frac{22.996}{0.8} = 28.745
$$

$$
f[x_1,x_2,x_3] = \frac{28.745 - 8.12}{2.0} = 10.3125, \qquad f[x_0,x_1,x_2,x_3] = \frac{10.3125 - 33.029630}{2.2 - 0.5} = \frac{-22.717130}{1.7} = -13.363017
$$

$$
f[x_2,x_3,x_4] = \frac{f[x_3,x_4] - f[x_2,x_3]}{3.0-1.4}, \qquad f[x_3,x_4] = \frac{79.0 - 28.972}{3.0-2.2} = \frac{50.028}{0.8} = 62.535
$$

$$
f[x_2,x_3,x_4] = \frac{62.535 - 28.745}{1.6} = 21.11875, \qquad f[x_1,x_2,x_3,x_4] = \frac{21.11875 - 10.3125}{3.0-0.2} = \frac{10.80625}{2.8} = 3.859375
$$

$$
f[x_0,x_1,x_2,x_3,x_4] = \frac{3.859375 - (-13.363017)}{3.0-0.5} = \frac{17.222392}{2.5} = 6.888957
$$

**Step 2. Write the polynomial.** The leading diagonal is
$-10.25,\ -21.606667,\ 33.029630,\ -13.363017,\ 6.888957$.

$$
s(t) = -10.25 + (-21.606667)(t - 0.5) + (33.029630)(t-0.5)(t-0.2) + (-13.363017)(t-0.5)(t-0.2)(t-1.4) + (6.888957)(t-0.5)(t-0.2)(t-1.4)(t-2.2)
$$

**Step 3. Evaluate at $t = 2.25$.** The factors are $1.75,\ 2.05,\ 0.85,\ 0.05$.

| Term | Working | Value | Running |
| :-- | :-- | --: | --: |
| $s_0$ | | $-10.250000$ | $-10.250000$ |
| $f[x_0,x_1](t-x_0)$ | $(-21.606667)(1.75)$ | $-37.811667$ | $-48.061667$ |
| $f[x_0,x_1,x_2](t-x_0)(t-x_1)$ | $(33.029630)(1.75)(2.05) = (33.029630)(3.5875)$ | $+118.494$ | $+70.432$ |
| $f[x_0..x_3](\cdot)(\cdot)(\cdot)$ | $(-13.363017)(1.75)(2.05)(0.85) = (-13.363017)(3.049375)$ | $-40.749$ | $29.683$ |
| $f[x_0..x_4](\cdot)(\cdot)(\cdot)(\cdot)$ | $(6.888957)(1.75)(2.05)(0.85)(0.05) = (6.888957)(0.15246875)$ | $+1.050$ | $30.734$ |

$$\boxed{s(2.25) = 30.7336}$$

> [!info] Check
> **Exact rational evaluation.** Carrying the table in fractions rather than
> decimals, the leading diagonal is
> $-\frac{41}{4},\ -\frac{3241}{150},\ \frac{4459}{135},\ -\frac{49069}{3672},\ \frac{101185}{14688}$
> and the result is exactly
> $$s(2.25) = \frac{2265929}{73728} = 30.7336290148$$
> The decimal working above agrees to every digit shown.
>
> **The unique quartic through the five points.** Solving for the polynomial
> directly in powers of $t$ and evaluating at $2.25$ gives the same
> $\frac{2265929}{73728}$. Two different methods, one answer.
>
> **Ordering.** Sorting the table to $0.2, 0.5, 1.4, 2.2, 3.0$ and re-running
> gives $30.7336290148$ again, to ten decimals, as the warning above states. The
> **intermediate rows differ** though, because each divided difference divides by
> the span of the two nodes it covers. That is worth expecting: the first row is
> $-21.606667, 18.028889, 28.745, 62.535$ sorted against $-21.606667, 8.12,
> 28.745, 62.535$ printed, and both are correct for their own node order.

> [!warning] The one choice that would change the answer
> A second reading is available: suppose the *values* were transposed rather than
> the labels, so that $s(0.2) = -10.25$ and $s(0.5) = -3.768$. That reading makes
> the signal **monotonically increasing**, $-10.25, -3.768, 5.976, 28.972, 79.0$,
> which is what a real rising signal looks like, whereas the printed pairing makes
> it dip from $-3.768$ down to $-10.25$ and then climb.
>
> That reading gives $s(2.25) = 31.2821$, which is $0.548$, or $1.8\%$, away from
> the printed answer. Neither reading is generated by a cubic: fitting a cubic
> through the first four points of either reading and evaluating it at $t = 3.0$
> gives $17.27$ against the actual $79.0$, or $96.70$ against $79.0$. Both are
> hopeless, so all five points are genuinely needed and a quartic is the right
> degree in either case. The table is just data.
>
> **The table as printed is the answer.** Pair each $s$ with the $t$ on its own
> row, which gives $30.7336$. But the dip at $t = 0.5$ is odd enough to be worth
> naming in an answer: state the reading used, and give $31.2821$ as the
> alternative. An answer that silently picks one hides a $1.8\%$ assumption.

---

### [2022 Q.2(a)]

**Question.** Find the polynomial which fits the following data: $(-1, 7)$, $(1, 5)$, $(2, 15)$.

*[Marks: 04, CO: 1]*

**Solution.**

With three points the lowest-degree polynomial that can pass through all three
is a **quadratic** $y = a_0 + a_1 x + a_2 x^2$. A linear fit would need the
points to be collinear, and they are not, so the degree is forced.

**Method: simultaneous equations.** Substitute each point:

$$
a_0 - a_1 + a_2 = 7
$$

$$
a_0 + a_1 + a_2 = 5
$$

$$
a_0 + 2a_1 + 4a_2 = 15
$$

Subtract the first from the second to kill $a_0$ and $a_2$ at once:

$$
2a_1 = -2 \quad \Rightarrow \quad a_1 = -1
$$

With $a_1 = -1$ the first equation gives $a_0 + a_2 = 6$, and the third gives
$a_0 + 4a_2 = 17$. Subtract: $3a_2 = 11$, so $a_2 = \frac{11}{3}$, and
$a_0 = 6 - \frac{11}{3} = \frac{7}{3}$.

$$\boxed{y = \frac{11}{3}x^2 - x + \frac{7}{3}}$$

**Check every point**, which takes one line each and settles the answer.

$$
x = -1: \quad \frac{11}{3}(1) + 1 + \frac{7}{3} = 6 + 1 = 7 \quad \checkmark
$$

$$
x = 1: \quad \frac{11}{3} - 1 + \frac{7}{3} = 6 - 1 = 5 \quad \checkmark
$$

$$
x = 2: \quad \frac{11}{3}(4) - 2 + \frac{7}{3} = 17 - 2 = 15 \quad \checkmark
$$

> [!info] Two more routes to the same coefficients
> **Lagrange form**, which is the method the question's neighbours ask about:
> $$y = 7\frac{(x-1)(x-2)}{(-1-1)(-1-2)} + 5\frac{(x+1)(x-2)}{(1+1)(1-2)} + 15\frac{(x+1)(x-1)}{(2+1)(2-1)}$$
> $$= \frac{7}{6}(x^2-3x+2) - \frac{5}{2}(x^2-x-2) + \frac{15}{3}(x^2-1)$$
> $$= \left(\frac{7}{6} - \frac{5}{2} + 5\right)x^2 + \left(-\frac{7}{2} + \frac{5}{2}\right)x + \left(\frac{7}{3} + 5 - 5\right)$$
> $$= \frac{11}{3}x^2 - x + \frac{7}{3}$$
>
> **Newton divided differences.** With the nodes already in increasing order,
> which they happen to be here,
>
> | Order | Values |
> | :-- | :-- |
> | $y$ | 7, 5, 15 |
> | $1^{st}$ | $-1$, $10$ |
> | $2^{nd}$ | $\frac{11}{3}$ |
>
> Newton's form is $y = 7 - (x+1) + \frac{11}{3}(x+1)(x-1)$, and expanding gives
> $7 - x - 1 + \frac{11}{3}(x^2 - 1) = \frac{11}{3}x^2 - x + \frac{7}{3}$. Same again.

> [!note] Why a quadratic is the right degree, and how you can tell in advance
> The degree rises one at a time as points are added, so three points mean a
> quadratic unless the points happen to be collinear. Check that first: if the
> slopes between consecutive points agree, a linear fit is enough and the third
> equation will be redundant.
>
> Here the slopes are $\frac{5-7}{1-(-1)} = -1$ and $\frac{15-5}{2-1} = 10$, which
> disagree, so the quadratic term is genuinely needed.

---

---

**Also asked here.**

- *2019 Q.4(b)* is the same question as [[NM-4.6_Lagranges_Interpolation|NM-4.6]], which is written in `NM-4.6`.

---

[🏠 Subtopic Index](00_Index.md) | [← Prev: NM-4.7 Newton's Forward Difference](NM-4.7_Newtons_Forward_Difference.md) | [Next: NM-4.10 Gauss Forward / Backward & Stirling's Formulas →](NM-4.10_Gauss_Forward_and_Backward_and_Stirlings_Formulas.md)
