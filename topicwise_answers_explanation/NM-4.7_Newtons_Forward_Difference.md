---
title: "NM-4.7 · Newton's Forward Difference"
tags:
  - numerical-methods
  - discrete-mathematics
  - topicwise
---

# NM-4.7 · Newton's Forward Difference

Every block below is copied from `../answers_explanation/`. The reasoning
is written once, in the year-wise file, and is not restated here.


### [2020 Q.5(a)]

**Question.** Deduce the Newton's forward difference interpolating polynomial.

*[Marks: 06]*

**Solution.**

**Set up.** For $n+1$ equally spaced points with common difference $h$, write
$x = x_0 + ph$ so that $p = \frac{x - x_0}{h}$. The forward difference operator is
$\Delta y_0 = y_1 - y_0$.

**Step 1. Taylor expansion about $x_0$.**

$$
y(x) = y_0 + p\,h\,y'(x_0) + \frac{p^2}{2!}h^2 y''(x_0) + \frac{p^3}{3!}h^3 y'''(x_0) + \cdots
$$

**Step 2. Express the derivatives through differences.** For a polynomial sampled at
spacing $h$, the $k$-th derivative at $x_0$ satisfies

$$
y^{(k)}(x_0) = \frac{\Delta^k y_0}{h^k}
$$

because each forward difference lowers the degree of the underlying polynomial by
one and contributes a factor of $h$.

**Step 3. Substitute.** The factors of $h$ cancel term by term:

$$
y(x) = y_0 + p\,\Delta y_0 + \frac{p^2}{2!}\Delta^2 y_0 + \frac{p^3}{3!}\Delta^3 y_0 + \cdots
$$

**Step 4. Replace the rising powers by falling products.** This is the step that
produces the standard form. The identity needed is

$$
p^k = \sum_{j=0}^{k} s(k, j)\,p(p-1)(p-2)\cdots(p-j+1)
$$

where $s(k,j)$ is a Stirling number of the second kind, and the empty product for
$j = 0$ equals $1$. Equivalently, shifting the index,
$p^k = \sum_{j=0}^{k-1} s(k, j+1)\,p(p-1)\cdots(p-j)$. Spot check at $k = 2$:
$1\cdot p + 1\cdot p(p-1) = p^2$.

More directly, Newton's interpolation polynomial for a node set is

$$
P(x) = f[x_0] + f[x_0,x_1](x-x_0) + f[x_0,x_1,x_2](x-x_0)(x-x_1) + \cdots
$$

where $f[x_0,x_1,\dots,x_k] = \frac{\Delta^k y_0}{k!\,h^k}$ for equally spaced
points. Substituting $x - x_i = (p-i)h$ and cancelling $h^k$:

$$
P(x) = y_0 + \frac{\Delta y_0}{1!h}\,(p)h + \frac{\Delta^2 y_0}{2!h^2}\,p(p-1)h^2 + \frac{\Delta^3 y_0}{3!h^3}\,p(p-1)(p-2)h^3 + \cdots
$$

**Step 5. The result.**

$$
y_n(x) = y_0 + p\Delta y_0 + \frac{p(p-1)}{2!}\Delta^2 y_0 + \frac{p(p-1)(p-2)}{3!}\Delta^3 y_0 + \cdots + \frac{p(p-1)\cdots(p-n+1)}{n!}\Delta^n y_0
$$

> [!note] Why step 4 is not a trick
> The Taylor form has rising powers $p^2, p^3$; the Newton form has falling products
> $p(p-1)$, $p(p-1)(p-2)$. The substitution is not cosmetic.
>
> The finite differences already carry the effect of the lower-order terms, and
> replacing rising powers by falling products is what avoids double counting. A
> derivation that stops at step 3 has a formula that is correct and useless,
> because no one builds a difference table and then has to raise $p$ to a power
> for each row.

**Validity.** Accurate for $0 \le p \le n$, that is inside the table. Near the far
end use backward differences instead, and outside the table the result is an
extrapolation with the risks listed in Q.3(a). Part (b) applies this to unequally
spaced data, where divided differences are used instead.

> [!note] Where this is used again
> The forward form is applied in 2021 Q.4(b) and 2021 Q.4(c), and the backward
> form in Q.3(b) above. See [[NM-4.7_Newtons_Forward_Difference|NM-4.7 · Newton's Forward Difference]].

---

### [2021 Q.3(c), 2023 Q.2(a)]

**Appeared in:** 2021 Q.3(c), 2023 Q.2(a)

**Question.** Derive the Newton's forward interpolation formula: $y_n(x) = y_0 + p\Delta y_0 + \frac{p(p-1)}{2!}\Delta^2 y_0 + \frac{p(p-1)(p-2)}{3!}\Delta^3 y_0 + \cdots$

*[Marks: 04, CO: 2]*

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

$$\boxed{y_n(x) = y_0 + p\Delta y_0 + \frac{p(p-1)}{2!}\Delta^2 y_0 + \frac{p(p-1)(p-2)}{3!}\Delta^3 y_0 + \cdots + \frac{p(p-1)\cdots(p-n+1)}{n!}\Delta^n y_0}$$

**Validity range.** The formula is accurate for $0 \le p \le 1$, primarily near the beginning of equidistant tables. For values near the end, backward differences are used.

> [!info] Alternate proof via Shift Operator $E$
> Using the relationship $E = 1 + \Delta$:
> $$y(x) = y(x_0 + ph) = E^p y_0 = (1 + \Delta)^p y_0$$
> Expanding $(1 + \Delta)^p$ by the binomial theorem:
> $$(1 + \Delta)^p = 1 + p\Delta + \frac{p(p-1)}{2!}\Delta^2 + \frac{p(p-1)(p-2)}{3!}\Delta^3 + \cdots$$
> Operating on $y_0$ immediately gives the formula.

> [!note] Why the falling product appears at all, and how to spot a wrong formula
> The pattern in the coefficients is
> $$1,\quad p,\quad \frac{p(p-1)}{2!},\quad \frac{p(p-1)(p-2)}{3!},\quad \cdots$$
> Each one is the previous one multiplied by $\frac{p-k}{k}$. That single
> recurrence is the fingerprint of the formula, and it is why the coefficient of
> $\Delta^k y_0$ is always a *falling* factorial divided by $k!$.
>
> A formula built from **rising** powers, $\frac{p^k}{k!}$, is not Newton's
> forward formula. It looks similar, produces plausible numbers for small $k$, and
> is wrong. Part (b) and part (d) of this question both use the falling form, and
> you can check any derivation against those.

> [!note] Where this is used again
> Part (d) applies this with $y = x^4$, and Q.4(b) applies central difference formulas to a table of $e^x$
> values. See [[NM-4.7_Newtons_Forward_Difference|NM-4.7 · Newton's Forward Difference]].

---

### [2022 Q.2(c)]

**Question.** Using Newton's forward difference formula find the sum $S_n = 1^3 + 2^3 + 3^3 + \cdots + n^3$.

*[Marks: 03, CO: 1]*

**Solution.**

**Step 1. Build the difference table.** Here $y = r^3$ for $r = 1, 2, 3, \ldots$
with $h = 1$, so $u = r - 1$ and $r = u + 1$.

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

The series returns $r^3$ exactly, as it must, since $r^3$ is itself a cubic. The
$\Delta^4$ row of zeros confirms it: a degree-$k$ polynomial has a constant
$k$-th forward difference and a zero $(k+1)$-th.

**Step 3. Sum from $u = 0$ to $u = n-1$.**

$$
S_n = \sum_{u=0}^{n-1}\left[1 + 7u + 6u(u-1) + u(u-1)(u-2)\right]
$$

Now use the standard sums, each of which is a hockey-stick identity in disguise:

$$
\sum_{u=0}^{n-1} 1 = n, \qquad \sum u = \frac{n(n-1)}{2}, \qquad \sum u(u-1) = 2\binom{n}{3} = \frac{n(n-1)(n-2)}{3}
$$

$$
\sum u(u-1)(u-2) = 6\sum\binom{u}{3} = 6\binom{n}{4} = \frac{n(n-1)(n-2)(n-3)}{4}
$$

So

$$
S_n = n + \frac{7n(n-1)}{2} + 2n(n-1)(n-2) + \frac{n(n-1)(n-2)(n-3)}{4}
$$

**Step 4. Collect over the common denominator 4.**

$$
S_n = \frac{4n + 14n(n-1) + 8n(n-1)(n-2) + n(n-1)(n-2)(n-3)}{4}
$$

Expanding the four terms, $4n$, $14n^2 - 14n$, $8n^3 - 24n^2 + 16n$ and
$n^4 - 6n^3 + 11n^2 - 6n$, and collecting:

$$
4n - 14n + 16n - 6n = 0, \qquad 14n^2 - 24n^2 + 11n^2 = n^2, \qquad 8n^3 - 6n^3 = 2n^3, \qquad n^4
$$

$$
n^4 + 2n^3 + n^2 = n^2(n+1)^2
$$

$$\boxed{S_n = \left[\frac{n(n+1)}{2}\right]^2}$$

> [!info] Check by direct evaluation
> | $n$ | $1^3 + \cdots + n^3$ | $\left[\frac{n(n+1)}{2}\right]^2$ |
> | --: | --: | --: |
> | 1 | 1 | 1 |
> | 2 | 9 | 9 |
> | 3 | 36 | 36 |
> | 4 | 100 | 100 |
> | 5 | 225 | 225 |
> | 6 | 441 | 441 |
>
> All six agree.

> [!note] Why the hockey-stick identity is the tool here, and what it costs
> Every sum in step 3 is of the form $\sum \binom{u}{k}$, and each of those has
> the closed form $\binom{n}{k+1}$ by the hockey-stick identity. Recognising
> that pattern is what makes the algebra short; expanding each sum term by term
> instead turns a four-line calculation into a page and is where mistakes enter.
>
> Worth noting that $u(u-1)(u-2)$ appears rather than $u^3$, which is the reason
> the hockey-stick form is available at all. Working with falling factorials
> rather than powers is what Newton difference formulas are built on.

---

---

**Also asked here.**

- *2021 Q.3(b)* is the same question as [[NM-4.6_Lagranges_Interpolation|NM-4.6]], which is written in `NM-4.6`.

---

**Answered in phase P6, in `../CT_Questions/`.**

- *CT-02A Q.2* is a class-test question. Its answer is in `../CT_Questions/CT_answers_exam_style.md`, with the reasoning in `../CT_Questions/CT_answers_explanation.md`.
