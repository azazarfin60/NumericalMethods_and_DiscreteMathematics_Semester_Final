---
title: "NM-4.6 · Lagrange's Interpolation"
tags:
  - numerical-methods
  - discrete-mathematics
  - topicwise
---

# NM-4.6 · Lagrange's Interpolation

Every block below is copied from `../answers_exam_style/`, which is the
only place an answer is authored. A number here is the same number, character
for character, as the one it came from.


### [2018 Q.3(a)]

**Question.** Explain the use of Lagrange's interpolation formula.

**Solution.**

**Use.** Lagrange's formula estimates an intermediate value $f(x)$ at a point
$x$ within the range of a tabulated set $(x_i, f_i)$, without requiring the
tabulated abscissae to be equally spaced.

**The formula.** For $n+1$ points,

$$f(x) \approx \sum_{i=0}^{n} f_i \prod_{\substack{j=0 \\ j \ne i}}^{n}\frac{x - x_j}{x_i - x_j}$$

**Why it is used.**

1. **Unequal spacing is allowed.** This is its principal advantage over
   Newton's formulas, which assume a common tabular spacing $h$. Data from
   experiment or from a table with a varying interval are handled directly.
2. **The tabulated order is irrelevant.** The formula is symmetric in the
   points; permuting them leaves the result unchanged, which is worth noting
   when a table is printed with its entries out of order.
3. **A single expression gives the value.** The whole formula is written once
   and evaluated at any $x$ in range, with no successive-difference table to
   construct.
4. **The error is available.** With $n+1$ points the error is
   $R_n = \dfrac{f^{(n+1)}(\xi)}{(n+1)!}\prod_{i=0}^{n}(x - x_i)$, so the
   accuracy of a chosen set can be judged before evaluating.

**Limitations.** Adding a new point requires recomputing every coefficient,
unlike Newton's divided-difference form where earlier work is retained. The
formula is also inefficient for repeated evaluation at many points, where a
single polynomial written out once is preferable.

---

### [2018 Q.3(c)]

**Question.** Find $f(2.5)$ from the given data, $x$: 1, 2, 3 and $f(x)$: 0, 1, 8.

**Solution.**

| $x$ | 1 | 2 | 3 |
| :---: | :---: | :---: |
| $f(x)$ | 0 | 1 | 8 |

**Lagrange's formula.** With three points,

$$f(x) = \frac{(x - x_1)(x - x_2)}{(x_0 - x_1)(x_0 - x_2)}f_0 + \frac{(x - x_0)(x - x_2)}{(x_1 - x_0)(x_1 - x_2)}f_1 + \frac{(x - x_0)(x - x_1)}{(x_2 - x_0)(x_2 - x_1)}f_2$$

At $x = 2.5$:

$$L_0 = \frac{(2.5 - 2)(2.5 - 3)}{(1 - 2)(1 - 3)} = \frac{(0.5)(-0.5)}{(-1)(-2)} = \frac{-0.25}{2} = -0.125$$

$$L_1 = \frac{(2.5 - 1)(2.5 - 3)}{(2 - 1)(2 - 3)} = \frac{(1.5)(-0.5)}{(1)(-1)} = \frac{-0.75}{-1} = 0.75$$

$$L_2 = \frac{(2.5 - 1)(2.5 - 2)}{(3 - 1)(3 - 2)} = \frac{(1.5)(0.5)}{(2)(1)} = \frac{0.75}{2} = 0.375$$

$$f(2.5) = 0(-0.125) + 1(0.75) + 8(0.375) = 0.75 + 3.0 = 3.75$$

$$\boxed{f(2.5) = 3.75}$$

> [!info] Check against the polynomial and against the original equation
> Newton's divided differences give $f[x_0,x_1] = 1$, $f[x_1,x_2] = 7$ and
> $f[x_0,x_1,x_2] = 3$, so the polynomial is
> $f(x) = 0 + 1(x - 1) + 3(x - 1)(x - 2) = 3x^2 - 8x + 5$. Substituting gives
> $f(2.5) = 3(6.25) - 20 + 5 = 3.75$, agreeing with the Lagrange result, and the
> three basis polynomials sum to $-0.125 + 0.75 + 0.375 = 1$ exactly, as the
> Lagrange basis of a quadratic must. The polynomial also reproduces the table:
> $f(1) = 0$, $f(2) = 1$ and $f(3) = 8$. Two routes, a partition-of-unity
> check and a table-reproduction check all give the same value, so no tabulated
> entry is contradicted and the arithmetic is confirmed.

---

### [2019 Q.4(b)]

**Question.** A robot arm with a rapid laser scanner is doing a quick quality check on holes drilled in a $15'' \times 10''$ rectangular plate. The centers of the holes in the plate describe the path the arm needs to take, and the hole centers are located on a Cartesian coordinate system (with the origin at the bottom left corner of the plate) given by the specifications in the table below. If the leaser is traversing from $x = 2$ to $x = 4.25$ to $x = 5.25$ in a quadratic path, what is the value of the $y$ at $x = 4.00$ using a curve fitting technique.

**Solution.**

The three tabulated points through which the quadratic path passes are

$$(x_0, y_0) = (2, 7.2), \qquad (x_1, y_1) = (4.25, 7.1), \qquad (x_2, y_2) = (5.25, 6.0)$$

Three points determine one quadratic, so the curve-fitting technique is exact
interpolation by a second-degree Lagrange polynomial.

**Lagrange basis.** With $x = 4.00$:

$$L_0 = \frac{(x - x_1)(x - x_2)}{(x_0 - x_1)(x_0 - x_2)} = \frac{(4 - 4.25)(4 - 5.25)}{(2 - 4.25)(2 - 5.25)} = \frac{(-0.25)(-1.25)}{(-2.25)(-3.25)}$$

$$L_0 = \frac{0.3125}{7.3125} = 0.04273504$$

$$L_1 = \frac{(x - x_0)(x - x_2)}{(x_1 - x_0)(x_1 - x_2)} = \frac{(4 - 2)(4 - 5.25)}{(4.25 - 2)(4.25 - 5.25)} = \frac{(2)(-1.25)}{(2.25)(-1)}$$

$$L_1 = \frac{-2.5}{-2.25} = 1.11111111$$

$$L_2 = \frac{(x - x_0)(x - x_1)}{(x_2 - x_0)(x_2 - x_1)} = \frac{(4 - 2)(4 - 4.25)}{(5.25 - 2)(5.25 - 4.25)} = \frac{(2)(-0.25)}{(3.25)(1)}$$

$$L_2 = \frac{-0.5}{3.25} = -0.15384615$$

**Evaluate the polynomial.**

$$y(4) = y_0 L_0 + y_1 L_1 + y_2 L_2 = 7.2(0.04273504) + 7.1(1.11111111) + 6.0(-0.15384615)$$

$$y(4) = 0.30769231 + 7.88888889 - 0.92307692 = 7.27350427$$

$$\boxed{y(4.00) = 7.2735\ \text{in.}}$$

> [!info] Check against the fitted polynomial in ordinary form
> Solving for $a, b, c$ in $y = a + bx + cx^2$ through the three points gives
> $c = -\dfrac{38}{117}$, $b = \dfrac{2323}{1170}$, $a = \dfrac{883}{195}$, so
> $y = -\dfrac{38x^2}{117} + \dfrac{2323x}{1170} + \dfrac{883}{195}$.
> Substituting $x = 4$ gives $-\dfrac{608}{117} + \dfrac{9292}{1170} + \dfrac{883}{195} = \dfrac{8510}{1170} = \dfrac{851}{117} = 7.27350427$, the
> same value. An exact fraction and a decimal evaluation agreeing to eight
> digits rules out a rounding loss in the Lagrange arithmetic. As a further
> structural check, $L_0 + L_1 + L_2 = 0.04273504 + 1.11111111 - 0.15384615 = 1$
> exactly, as a quadratic's three Lagrange basis polynomials must.

---

### [2021 Q.3(b)]

**Question.** Differentiate between Newton's interpolation and Lagrange's interpolation.

**Solution.**

| | Newton's interpolation | Lagrange's interpolation |
| :-- | :-- | :-- |
| Form | **Successive approximation**, applied one point at a time | **Single polynomial**, all points at once |
| Basis | Divided differences or forward/backward differences | Products $\prod_{j\neq i}\frac{x-x_j}{x_i-x_j}$ |
| Adding a new point | Old result is **retained**; only a new term is added | Whole polynomial must be **rebuilt** |
| Equally spaced points | Forward/backward difference form is fastest | Works but ignores the equal spacing |
| Unequal spacing | Needs **divided** differences | Natural, no change needed |
| Cost per evaluation | $O(n)$ after setup | $O(n^2)$ directly, $O(n)$ with Neville |
| Near the table ends | Forward at the start, backward at the end | One formula for everywhere |
| Numerical stability | Better with the Neville form | Degrades with many points |

Newton gives an **update** rule, cheap when data arrive incrementally. Lagrange
gives a **construction**, direct, and equally spaced points require no special
case.

$$
\boxed{\text{Newton updates and reuses; Lagrange rebuilds once and is spacing-agnostic}}
$$

---

### [2021 Q.3(d), 2023 Q.2(b)]

**Appeared in:** 2021 Q.3(d), 2023 Q.2(b)

**Question.** Find $y(2)$ from the following data using Lagrange's formula.

**Solution.**

| $x$ | 0 | 1 | 3 | 4 | 5 |
| --- | --: | --: | --: | --: | --: |
| $y$ | 0 | 1 | 81 | 256 | 625 |

**Step 1. The formula.** With five points $x_0 = 0, x_1 = 1, x_2 = 3, x_3 = 4,
x_4 = 5$,

$$
y(2) = \sum_{i=0}^{4} y_i L_i(2), \qquad L_i(2) = \prod_{j \neq i} \frac{2 - x_j}{x_i - x_j}
$$

**Step 2. Compute each weight**, keeping numerator and denominator factors separate.

$$
L_0(2) = \frac{(2-1)(2-3)(2-4)(2-5)}{(0-1)(0-3)(0-4)(0-5)} = \frac{(1)(-1)(-2)(-3)}{(-1)(-3)(-4)(-5)} = \frac{-6}{60} = -\frac{1}{10}
$$

$$
L_1(2) = \frac{(2-0)(2-3)(2-4)(2-5)}{(1-0)(1-3)(1-4)(1-5)} = \frac{(2)(-1)(-2)(-3)}{(1)(-2)(-3)(-4)} = \frac{-12}{-24} = \frac{1}{2}
$$

$$
L_2(2) = \frac{(2-0)(2-1)(2-4)(2-5)}{(3-0)(3-1)(3-4)(3-5)} = \frac{(2)(1)(-2)(-3)}{(3)(2)(-1)(-2)} = \frac{12}{12} = 1
$$

$$
L_3(2) = \frac{(2-0)(2-1)(2-3)(2-5)}{(4-0)(4-1)(4-3)(4-5)} = \frac{(2)(1)(-1)(-3)}{(4)(3)(1)(-1)} = \frac{6}{-12} = -\frac{1}{2}
$$

$$
L_4(2) = \frac{(2-0)(2-1)(2-3)(2-4)}{(5-0)(5-1)(5-3)(5-4)} = \frac{(2)(1)(-1)(-2)}{(5)(4)(2)(1)} = \frac{4}{40} = \frac{1}{10}
$$

**Check.** The weights sum to 1:
$-\frac{1}{10} + \frac{1}{2} + 1 - \frac{1}{2} + \frac{1}{10} = 1$ ✓

This holds at **any** $x$, not only at a node, because interpolating the constant
function $1$ with a degree 4 polynomial must return $1$.

**Step 3. Assemble.**

$$
\begin{aligned}
y(2) &= (0)\left(-\tfrac{1}{10}\right) + (1)\left(\tfrac{1}{2}\right) + (81)(1) + (256)\left(-\tfrac{1}{2}\right) + (625)\left(\tfrac{1}{10}\right) \\
     &= 0 + 0.5 + 81 - 128 + 62.5 \\
     &= 16
\end{aligned}
$$

$$
\boxed{y(2) = 16}
$$

> [!info] Check by two independent routes
> **Route 2, Newton's divided difference.** The nodes are **not** equally spaced, so
> divided differences apply. The table is
>
> | Order | Values |
> | :-- | :-- |
> | $f[x_i]$ | 0, 1, 81, 256, 625 |
> | $1^{st}$ | 1, 40, 175, 369 |
> | $2^{nd}$ | 13, 45, 97 |
> | $3^{rd}$ | 8, 13 |
> | $4^{th}$ | 1 |
>
> Spot check: $f[x_1,x_2,x_3] = \frac{f[x_2,x_3] - f[x_1,x_2]}{x_3 - x_1} = \frac{175-40}{4-1} = 45$.
> The leading diagonal is $0, 1, 13, 8, 1$, and evaluating that polynomial at
> $x = 2$ gives **16**.
>
> **Route 3, recognise the data.** $0^4 = 0$, $1^4 = 1$, $3^4 = 81$,
> $4^4 = 256$, $5^4 = 625$. All five points lie on $y = x^4$ exactly, so
> $y(2) = 2^4 = 16$.

> [!warning] The weights are the whole calculation
> Each $L_i$ has four numerator and four denominator factors, since $j$ runs over
> the four indices other than $i$. A weight with three factors is wrong by
> construction. The two most often mis-signed are $L_0(2)$ and $L_1(2)$, whose
> denominators are $+60$ and $-24$.

---

### [2024 Q.2(c)]

**Question.** Describe the Lagrange interpolation method. What are its advantages and disadvantages?

**Solution.**

**Idea.** With $n+1$ points $(x_0, y_0), \ldots, (x_n, y_n)$ there is exactly one
polynomial of degree at most $n$ passing through all of them. Lagrange writes
that polynomial directly, as a sum where each term is arranged to be correct at
one point and zero at all the others.

**The formula**

$$
P_n(x) = \sum_{i=0}^{n} y_i L_i(x), \qquad
L_i(x) = \prod_{\substack{j=0 \\ j \neq i}}^{n} \frac{x - x_j}{x_i - x_j}
$$

**Why $L_i$ behaves as it must.** At $x = x_k$ every factor with $k \neq i$ has a
numerator of $x_k - x_k = 0$, so $L_i(x_k) = 0$. At $x = x_i$ every ratio is
$(x_i - x_j)/(x_i - x_j) = 1$, so $L_i(x_i) = 1$. Each term therefore contributes
$y_i$ at its own point and nothing at the others.

**Advantages**

1. No need to solve any equation. The coefficients are written down directly.
2. Unequal spacing is handled with no change to the formula.
3. A new point can be added by adding one term, without rebuilding the rest.
4. It gives an exact fit for any data type, including unevenly spaced samples.

**Disadvantages**

1. Evaluating $P_n$ costs $O(n^2)$ operations, which grows fast.
2. Round off error grows with $n$ and with the distance from the data points.
3. It is unstable for extrapolation. Runge's phenomenon shows large oscillation
   outside the data range.
4. Adding a point changes nothing about the fit quality elsewhere, so it gives no measure
   of whether the model is adequate.

$$
\boxed{P_n(x) = \sum_{i=0}^{n} y_i \prod_{j \neq i} \frac{x - x_j}{x_i - x_j}}
$$

---

---

**Also asked here.**

- *2022 Q.1(c)* is the same question as [[NM-4.1|NM-4.1]], which is written in `NM-4.1`.
- *2022 Q.2(a)* is the same question as [[NM-4.9|NM-4.9]], which is written in `NM-4.9`.

---

**Answered in phase P6, in `../CT_Questions/`.**

- *CT-02A Q.1* is a class-test question. Its answer is in `../CT_Questions/CT_answers_exam_style.md`, with the reasoning in `../CT_Questions/CT_answers_explanation.md`.
