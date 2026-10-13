---
title: "NM-4.6 · Lagrange's Interpolation"
tags:
  - numerical-methods
  - discrete-mathematics
  - topicwise
---


[🏠 Subtopic Index](00_Index.md) | [← Prev: NM-4.5 Linear Interpolation](NM-4.5_Linear_Interpolation.md) | [Next: NM-4.7 Newton's Forward Difference →](NM-4.7_Newtons_Forward_Difference.md)

---

# NM-4.6 · Lagrange's Interpolation

Every block below is copied from `../answers_explanation/`. The reasoning
is written once, in the year-wise file, and is not restated here.


### [2018 Q.3(a)]

**Question.** Explain the use of Lagrange's interpolation formula.

*[Marks: 02]*

**Solution.**

**The use.** Given a tabulated set $(x_i, f_i)$, estimate $f(x)$ at a point $x$
lying inside the range of the table, without assuming the abscissae are equally
spaced.

**The formula.** For $n+1$ points,

$$f(x) \approx \sum_{i=0}^{n} f_i \prod_{\substack{j=0 \\ j \ne i}}^{n}\frac{x - x_j}{x_i - x_j}$$

**Four reasons it is used.**

1. **Unequal spacing is allowed.** This is the principal advantage over
   Newton's forward and backward formulas, which both need a common tabular
   spacing $h$. Experimental data with a varying interval can be used directly.
2. **The tabulated order is irrelevant.** The formula is symmetric in the
   points; permuting them leaves the result unchanged. Worth knowing when a
   printed table lists its entries out of order.
3. **One expression gives the value.** The whole formula is written once and
   evaluated at any $x$ in range, with no successive-difference table to build.
4. **The error is available.** With $n+1$ points,
   $R_n = \dfrac{f^{(n+1)}(\xi)}{(n+1)!}\prod_{i=0}^{n}(x - x_i)$, so the
   accuracy of a chosen set can be judged before any arithmetic is done.

**Limitations.** Adding a point means recomputing every coefficient, unlike
Newton's divided-difference form where earlier work is retained. And it is
inefficient for repeated evaluation at many points, where writing the single
interpolating polynomial out once and evaluating it is cheaper.

> [!note] Newton's form and Lagrange's form are the same polynomial
> They differ only in organisation. If you have a regular table, build the
> divided-difference table and use Newton's form. If the spacing is irregular
> or you have only the points to hand, write Lagrange's directly. Never build
> Newton's *forward* formula on an irregular table, because $h$ does not exist.

---

### [2018 Q.3(c)]

**Question.** Find $f(2.5)$ from the given data, $x$: 1, 2, 3 and $f(x)$: 0, 1, 8.

*[Marks: 04]*

**Solution.**

| $x$ | 1 | 2 | 3 |
| :---: | :---: | :---: | :---: |
| $f(x)$ | 0 | 1 | 8 |

**The method.** Three points, so a quadratic, so Lagrange's formula. Here the
spacing *is* uniform, but Lagrange is still the shortest route because there is
no difference table to build and only three basis polynomials to evaluate.

$$f(x) = \frac{(x - x_1)(x - x_2)}{(x_0 - x_1)(x_0 - x_2)}f_0 + \frac{(x - x_0)(x - x_2)}{(x_1 - x_0)(x_1 - x_2)}f_1 + \frac{(x - x_0)(x - x_1)}{(x_2 - x_0)(x_2 - x_1)}f_2$$

**Evaluate each basis polynomial at $x = 2.5$.**

$$L_0 = \frac{(2.5 - 2)(2.5 - 3)}{(1 - 2)(1 - 3)} = \frac{(0.5)(-0.5)}{(-1)(-2)} = -0.125$$

$$L_1 = \frac{(2.5 - 1)(2.5 - 3)}{(2 - 1)(2 - 3)} = \frac{(1.5)(-0.5)}{(1)(-1)} = 0.75$$

$$L_2 = \frac{(2.5 - 1)(2.5 - 2)}{(3 - 1)(3 - 2)} = \frac{(1.5)(0.5)}{(2)(1)} = 0.375$$

$$f(2.5) = 0(-0.125) + 1(0.75) + 8(0.375) = 0 + 0.75 + 3.0$$

$$\boxed{f(2.5) = 3.75}$$

> [!info] Two checks that catch different mistakes
> **Partition of unity.** $-0.125 + 0.75 + 0.375 = 1$ exactly. The Lagrange
> basis polynomials of degree $n$ must sum to the constant $1$ at every $x$,
> because they are interpolating the function $y = 1$. If your three numbers do
> not sum to $1$, at least one of them was miscomputed, and you can find which by
> checking them one at a time.
>
> **The polynomial itself.** Newton's divided differences give
> $f[x_0,x_1] = 1$, $f[x_1,x_2] = 7$ and $f[x_0,x_1,x_2] = \dfrac{7 - 1}{3 - 1} = 3$, so
> $f(x) = 0 + 1(x - 1) + 3(x-1)(x-2) = 3x^2 - 8x + 5$. At $x = 2.5$:
> $3(6.25) - 8(2.5) + 5 = 18.75 - 20 + 5 = 3.75$. And the polynomial
> reproduces the table: $f(1) = 0$, $f(2) = 1$, $f(3) = 8$. Note that the
> divided-difference route is *also* a check on the answer, not merely a
> restatement: it uses the data through a completely different arrangement of
> the arithmetic.

---

### [2019 Q.4(b)]

**Question.** A robot arm with a rapid laser scanner is doing a quick quality check on holes drilled in a $15'' \times 10''$ rectangular plate. The centers of the holes in the plate describe the path the arm needs to take, and the hole centers are located on a Cartesian coordinate system (with the origin at the bottom left corner of the plate) given by the specifications in the table below. If the leaser is traversing from $x = 2$ to $x = 4.25$ to $x = 5.25$ in a quadratic path, what is the value of the $y$ at $x = 4.00$ using a curve fitting technique.

*[Marks: 06]*

**Solution.**

| $x$ (in.) | 2 | 4.25 | 5.25 |
| --: | --: | --: | --: |
| $y$ (in.) | 7.2 | 7.1 | 6.0 |

The three tabulated points through which the quadratic path passes are

$$(x_0, y_0) = (2, 7.2), \qquad (x_1, y_1) = (4.25, 7.1), \qquad (x_2, y_2) = (5.25, 6.0)$$

Three points determine one quadratic, so the curve-fitting technique is **exact
interpolation** by a second-degree Lagrange polynomial. The rest of the table,
$(7.81, 5.0), (9.20, 3.5), (10.60, 5.0)$, is not part of the specified path.

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

> [!warning] A weight greater than one is normal, and $L_1 = 1.111$ looks wrong until it is checked
> Lagrange weights are not a partition of unity in value. $L_1 > 1$ and
> $L_2 < 0$ together are exactly what an **extrapolation-free but off-node**
> evaluation produces: the target $4.00$ is between $x_0 = 2$ and $x_1 = 4.25$,
> close to $x_1$, so its weight is large and the neighbouring weight compensates
> negatively.
>
> The check is not "all weights in $[0,1]$". The check is that the weights **sum
> to 1**, which they do:
> $0.04273504 + 1.11111111 - 0.15384615 = 1$ exactly. That identity holds at any $x$,
> because interpolating the constant function $1$ must return $1$.

> [!info] Check against the fitted polynomial in ordinary form
> Solving for $a, b, c$ in $y = a + bx + cx^2$ through the three points gives
> $c = -\dfrac{38}{117}$, $b = \dfrac{2323}{1170}$, $a = \dfrac{883}{195}$, so
> $y = -\dfrac{38x^2}{117} + \dfrac{2323x}{1170} + \dfrac{883}{195}$.
> Substituting $x = 4$ gives $-\dfrac{608}{117} + \dfrac{9292}{1170} + \dfrac{883}{195} = \dfrac{8510}{1170} = \dfrac{851}{117} = 7.27350427$, the
> same value. An exact fraction and a decimal evaluation agreeing to eight digits
> rules out a rounding loss in the Lagrange arithmetic.

---

### [2021 Q.3(b)]

**Question.** Differentiate between Newton's interpolation and Lagrange's interpolation.

*[Marks: 02, CO: 2]*

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

$$\boxed{\text{Newton updates and reuses; Lagrange rebuilds once and is spacing-agnostic}}$$

> [!note] The one distinction worth remembering
> Newton gives an **update** rule, cheap when data arrive incrementally. Lagrange
> gives a **construction**, direct, and equally spaced points require no special
> case.
>
> That is the whole difference in one sentence. Everything else in the table is a
> consequence of it: the update is why Newton is cheap to extend, and the direct
> construction is why Lagrange needs no difference table at all.
>
> In practice Newton's divided difference form is almost always what you compute,
> because it is both cheaper and better conditioned. Lagrange earns its place in
> an exam because it is the form with an obvious closed expression for the
> error term.

---

### [2021 Q.3(d), 2023 Q.2(b)]

**Appeared in:** 2021 Q.3(d), 2023 Q.2(b)

**Question.** Find $y(2)$ from the following data using Lagrange's formula.

*[Marks: 04, CO: 2]*

**Solution.**

| $x$ | 0 | 1 | 3 | 4 | 5 |
| --- | --: | --: | --: | --: | --: |
| $y$ | 0 | 1 | 81 | 256 | 625 |

**Step 1. The formula.** With five points $x_0 = 0, x_1 = 1, x_2 = 3, x_3 = 4,
x_4 = 5$,

$$
y(2) = \sum_{i=0}^{4} y_i L_i(2), \qquad L_i(2) = \prod_{j \neq i} \frac{2 - x_j}{x_i - x_j}
$$

**Step 2. Compute each weight**, keeping numerator and denominator factors
separate.

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

$$\boxed{y(2) = 16}$$

> [!info] Check by two independent routes
> **Route 2, Newton's divided difference.** The nodes are **not** equally spaced,
> so divided differences apply. The table is
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
>
> The sum-to-1 check above catches both of those and any other sign slip, for one
> line of work. Run it every time; it costs nothing and it is the only check
> available before the final assembly.

> [!note] Recognising the data beats computing them
> Route 3 is not a party trick. When the $y$ values look like familiar powers,
> identifying the generating function turns a twenty-line Lagrange sum into a
> single multiplication, and it also **validates** the table.
>
> If the data are $x^4$ then any interpolant must be $x^4$ exactly, since a
> degree 4 polynomial through five points on a quartic is that quartic. A computed
> answer that disagreed with $2^4 = 16$ would mean an arithmetic slip, not a
> modelling insight.

---

### [2024 Q.2(c)]

**Question.** Describe the Lagrange interpolation method. What are its advantages and disadvantages?

*[Marks: 03, CO: 1]*

**Solution.**

**The method.** Given $n+1$ points $(x_i, y_i)$, the unique polynomial of
degree at most $n$ through them is

$$\boxed{P_n(x) = \sum_{i=0}^{n} y_i \prod_{j \neq i} \frac{x - x_j}{x_i - x_j}}$$

Each $y_i$ is multiplied by a **basis polynomial** $L_i(x)$ that equals $1$ at
$x = x_i$ and $0$ at every other tabulated $x_j$. That construction is what
guarantees the interpolant passes through every point: at $x = x_k$, every term
except the $k$-th vanishes.

**The error.** With $n+1$ points,

$$f(x) - P_n(x) = \frac{f^{(n+1)}(\xi)}{(n+1)!}\prod_{i=0}^{n}(x - x_i)$$

for some $\xi$ in the interval. The product is zero at every node, so the error
is zero there, and it grows between nodes. This is why interpolation error is
not uniformly distributed across the interval.

**Advantages.**

1. **Equal spacing is not required.** This is the decisive advantage over
   Newton's formulas, which assume a constant tabular spacing $h$. Experimental
   data with irregular spacing are handled directly.
2. **The order of the points is irrelevant.** The formula is symmetric in the
   nodes, so a table printed with its entries out of order gives the same
   polynomial. This is useful when a printed table is disordered.
3. **The formula is written once.** A single expression evaluates at any $x$ in
   range, with no difference table to construct, and it is convenient for
   hand checking.

**Disadvantages.**

1. **Adding a point costs everything.** Every basis polynomial changes, so a new
   point forces a complete recomputation. Newton's divided-difference form keeps
   its earlier work, so appending a point costs one new column.
2. **It is inefficient for repeated evaluation.** Evaluating the product for
   every new $x$ costs $O(n^2)$ multiplications, whereas converting to power
   form once costs $O(n^2)$ and then gives $O(n)$ per evaluation.
3. **It cannot show the trend.** The formula gives a value, not a model. Fitting
   a line and reporting the slope is a different task, and interpolation does not
   answer it.

**When to use it.** Lagrangian interpolation is the right choice when the data
are exact, unevenly spaced, and evaluated at few points. For many points, or
when a model of the trend is wanted, use fitting instead.

---

---

**Also asked here.**

- *2022 Q.1(c)* is the same question as [[NM-4.1_Concepts|NM-4.1]], which is written in `NM-4.1`.
- *2022 Q.2(a)* is the same question as [[NM-4.9_Newtons_Divided_Difference_and_General_Interpolation|NM-4.9]], which is written in `NM-4.9`.

---

**Answered in phase P6, in `../CT_Questions/`.**

- *CT-02A Q.1* is a class-test question. Its answer is in `../CT_Questions/CT_answers_exam_style.md`, with the reasoning in `../CT_Questions/CT_answers_explanation.md`.

---

[🏠 Subtopic Index](00_Index.md) | [← Prev: NM-4.5 Linear Interpolation](NM-4.5_Linear_Interpolation.md) | [Next: NM-4.7 Newton's Forward Difference →](NM-4.7_Newtons_Forward_Difference.md)
