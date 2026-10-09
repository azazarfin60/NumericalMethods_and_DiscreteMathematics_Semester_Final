---
title: "NM-5.1 · Trapezoidal Rule"
tags:
  - numerical-methods
  - discrete-mathematics
  - topicwise
---

# NM-5.1 · Trapezoidal Rule

Every block below is copied from `../answers_explanation/`. The reasoning
is written once, in the year-wise file, and is not restated here.


### [2018 Q.6(b)]

**Question.** Determine the value of $n$ so that the trapezoidal rule will approximate the value of $\int_0^1 \sqrt{1 + x^2} \, dx$ with an error that is less than $0.01$.

*[Marks: 04]*

**Solution.**

**The bound.** The composite trapezoidal rule over $[a,b]$ with $n$
subintervals has error

$$|E| = \left|\frac{(b - a)h^2}{12}f''(\xi)\right| \le \frac{(b-a)h^2}{12}\max_{[a,b]}|f''|$$

**Compute $f''$ and its maximum.** With $f(x) = \sqrt{1 + x^2}$,

$$f'(x) = \frac{x}{\sqrt{1+x^2}}, \qquad f''(x) = \frac{1}{(1+x^2)^{3/2}}$$

This decreases as $x$ increases on $[0,1]$, so the maximum is at $x = 0$:

$$f''(0) = 1$$

**Solve the inequality.** With $a = 0$, $b = 1$:

$$\frac{h^2}{12} < 0.01 \implies h^2 < 0.12 \implies h < 0.3464$$

$$n = \frac{b-a}{h} > \frac{1}{0.3464} = 2.8868$$

$$\boxed{n = 3}$$

> [!note] Why the answer is the *smallest* integer that works
> The bound gives a sufficient condition, not a necessary one, so it is always
> safe to round the requirement *up*. Rounding down would be relying on the
> bound being loose, which is not a guarantee. Here $n = 3$ clears it and
> $n = 2$ does not, which the direct check below confirms.

> [!info] The direct check, which also shows the bound is not tight
> The exact value is available in closed form:
> $$\int_0^1\sqrt{1+x^2}\,dx = \left[\dfrac{x\sqrt{1+x^2}}{2} + \dfrac{\ln(x + \sqrt{1+x^2})}{2}\right]_0^1 = \frac{\sqrt2 + \ln(1+\sqrt2)}{2} = 1.1477936$$
>
> | $n$ | $h$ | Approximation | Error |
| :--: | :--: | :-- | :-- |
| 2 | 0.50 | 1.1625704 | $0.014777$ |
| 3 | 0.3333 | 1.1543499 | $0.006556$ |
>
> At $n = 2$ the error exceeds $0.01$ and at $n = 3$ it falls below, so the
> answer is confirmed rather than merely bounded. The bound itself is also
> consistent: at $n = 3$, $h = 1/3$, so $\dfrac{h^2}{12} = \dfrac{1}{108} =
> 0.009259$, and the actual error $0.006556$ is below it, as it must be.

---

### [2019 Q.6(c)]

**Question.** Discuss trapezoidal rule of numerical integration.

*[Marks: 03]*

**Solution.**

The **trapezoidal rule** approximates $\int_a^b f(x)\,dx$ by replacing the curve
with a straight line joining the endpoints of each subinterval, so the area under
the curve becomes the area of a set of trapezoids.

**Derivation.** Over one interval $[x_0, x_0 + h]$, the straight line through
$(x_0, f_0)$ and $(x_1, f_1)$ has slope $\dfrac{f_1 - f_0}{h}$, and its integral is

$$\int_{x_0}^{x_1} f(x)\,dx \approx \frac{h}{2}(f_0 + f_1)$$

**Composite rule.** Over $[a, b]$ with $n$ subintervals of width
$h = \dfrac{b - a}{n}$, summing the one-interval result gives

$$\int_a^b f(x)\,dx \approx \frac{h}{2}\left[f_0 + 2f_1 + 2f_2 + \cdots + 2f_{n-1} + f_n\right]$$

$$\boxed{\int_a^b f(x)\,dx \approx \frac{h}{2}\left[f(a) + f(b) + 2\sum_{i=1}^{n-1}f_i\right]}$$

**Error.** The error over one interval is $-\dfrac{h^3}{12}f''(\xi)$, so the
composite error is

$$E = -\frac{(b - a)h^2}{12}f''(\xi), \qquad O(h^2)$$

**Properties.**

1. **Order of accuracy.** $O(h^2)$: halving $h$ reduces the error by a factor of
   four.
2. The rule is exact for a straight line, and over-shoots for a curve that is
   concave up, since the chord lies above the curve.
3. It is the basis of the trapezoidal rule for sampled data, where the area of a
   measured record is obtained with no requirement that the samples be equally
   spaced in value.
4. Its ease of use makes it the obvious first estimate, but Simpson's rules are
   preferred when smoothness and accuracy are required.

> [!warning] "Second order" and "halving the step" are different things
> The error is $O(h^2)$ **for a fixed interval**, which means $h \propto \frac{1}{n}$
> and therefore $E \propto \frac{1}{n^2}$. To halve the error you must **quadruple**
> the number of subintervals, and each of them costs a function evaluation.
>
> That is the real reason Simpson's rule is normally preferred. Its $O(h^4)$ error
> halves when $n$ multiplies by $4^{1/4} \approx 1.41$ rather than by $2$, so it
> buys the same accuracy for a third of the evaluations at these orders.
>
> **The factor of 4 is the halving test for a second-order rule.** It also holds for
> the central-difference formula in Q.6(a), and noticing that both are second order
> unifies the two topics.

---

### [2021 Q.8(a)]

**Question.** Derive the following numerical integration formula: $\int_{x_0}^{x_n} y\,dx = \frac{h}{2}[y_0 + 2(y_1 + y_2 + \cdots + y_{n-1}) + y_n]$

*[Marks: 04, CO: 1]*

**Solution.**

**The formula is the composite trapezoidal rule.** $h = \frac{x_n - x_0}{n}$, and
$y_i = f(x_i)$ at $x_i = x_0 + ih$.

**Step 1. Start from the trapezoidal rule on one interval.** On $[x_i, x_{i+1}]$, the
trapezoid of area $\frac{1}{2}h(y_i + y_{i+1})$,

$$
\int_{x_i}^{x_{i+1}} y\,dx = \frac{h}{2}(y_i + y_{i+1}) - \frac{h^3}{12}y''(\xi_i) + \cdots
$$

**Step 2. Sum over all $n$ intervals.**

$$
\int_{x_0}^{x_n} y\,dx = \sum_{i=0}^{n-1}\left[\frac{h}{2}(y_i + y_{i+1}) + \text{error}\right]
$$

**Step 3. Collect the interior terms.** Every $y_1, y_2, \dots, y_{n-1}$ appears in
**two** adjacent trapezoids, once from each side, so each collects a factor of
$\frac{h}{2} \times 2 = h$. Only $y_0$ and $y_n$ appear once, each with factor
$\frac{h}{2}$. Hence

$$
\int_{x_0}^{x_n} y\,dx = \frac{h}{2}y_0 + h\left(y_1 + y_2 + \cdots + y_{n-1}\right) + \frac{h}{2}y_n - \sum_{i=0}^{n-1}\frac{h^3}{12}y''(\xi_i)
$$

**Step 4. Factor out $h/2$.** Since $h = 2\cdot\frac{h}{2}$, the interior sum
becomes $2\cdot\frac{h}{2}(y_1 + \cdots + y_{n-1})$, giving

$$
\int_{x_0}^{x_n} y\,dx = \frac{h}{2}\left[y_0 + 2(y_1 + y_2 + \cdots + y_{n-1}) + y_n\right] - \frac{h^3}{12}\sum_{i=0}^{n-1}y''(\xi_i)
$$

**Step 5. The leading error term.** With $n$ intervals, $h = \frac{b-a}{n}$ and
$\sum y''(\xi_i) \approx \frac{1}{h}\int y''$, so

$$
E = -\frac{h^2}{12}\left[y'(x_n) - y'(x_0)\right] + O(h^4)
$$

which is $O(h^2)$, the signature of a second-order method.

$$\boxed{\int_{x_0}^{x_n} y\,dx = \frac{h}{2}\left[y_0 + 2\sum_{i=1}^{n-1}y_i + y_n\right] + O(h^2)}$$

> [!warning] The counting in step 3 is the whole derivation
> The factor 2 on the interior terms is not a convention. It is the count of how
> many panels each interior ordinate belongs to: one from the left, one from the
> right.
>
> **The ends get no 2 because they belong to only one panel.** That asymmetry is
> the fingerprint of the trapezoid rule, and it is what distinguishes it from
> Simpson's rule, where the interior terms get 4 and 2 in a pattern.
>
> If a derivation ever produces a 2 on the end terms, the error is not in the
> algebra but in the counting.

> [!note] Two ways to see it
> **Geometrically.** Each panel is a trapezoid. Draw them all, add the areas: the
> interior ordinates are shared by two panels and so counted twice, the ends once.
>
> **By an exact integral.** Linear interpolation between the nodes gives
> $y(x) = \frac{y_{i+1}-y_i}{h}(x-x_i) + y_i$ on each panel. Integrating that
> exactly over $[x_i, x_{i+1}]$ gives $\frac{h}{2}(y_i + y_{i+1})$ per panel, and
> summing reproduces the formula with no error analysis needed.

> [!note] Reading the error term, because it is easy to misjudge
> The error is $O(h^2)$, but **for a fixed interval** $h = \frac{b-a}{n}$, so
> $E \propto \frac{1}{n^2}$. To halve the error you must quadruple $n$, which
> means four times the function evaluations. That is the real cost of the
> trapezoid rule, and it is why Simpson's rule, at $O(h^4)$, is usually preferred
> when the same evaluations will do.

---

### [2022 Q.3(a)]

**Question.** Compute the value of $I = \int_0^1 \frac{dx}{1 + x^2}$ using the trapezoidal rule with $h = 0.5, 0.25$ and $0.125$. Then obtain a better estimate using Romberg's method.

*[Marks: 04, CO: 1]*

**Solution.**

**Step 1. Function values.** All nine are needed, because the finest trapezoid
rule uses the whole set.

| $x$ | 0 | 0.125 | 0.25 | 0.375 | 0.5 | 0.625 | 0.75 | 0.875 | 1 |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| $f(x) = \frac{1}{1+x^2}$ | 1.000000 | 0.984615 | 0.941176 | 0.876712 | 0.800000 | 0.719101 | 0.640000 | 0.566372 | 0.500000 |

**Step 2. The trapezoidal rule, three step sizes.**

$$
T_n = \frac{h}{2}\left[f_0 + 2f_1 + 2f_2 + \cdots + 2f_{n-1} + f_n\right]
$$

At $h = 0.5$, $n = 2$:

$$
T_2 = \frac{0.5}{2}\left[1 + 2(0.8) + 0.5\right] = 0.25(3.1) = 0.775000
$$

At $h = 0.25$, $n = 4$:

$$
T_4 = 0.125\left[1 + 2(0.941176 + 0.8 + 0.640000) + 0.5\right] = 0.125(6.262352) = 0.782794
$$

At $h = 0.125$, $n = 8$:

$$
T_8 = 0.0625\left[1 + 2(0.984615 + 0.941176 + 0.876712 + 0.800000 + 0.719101 + 0.640000 + 0.566372) + 0.5\right]
$$

$$
= 0.0625\left[1 + 2(5.527976) + 0.5\right] = 0.0625(12.555952) = 0.784747
$$

**Step 3. Richardson extrapolation.** The trapezoid rule has $O(h^2)$ error, so
halving $h$ cuts the error by $4$, and each extrapolation removes a factor of
$4^j - 1$:

$$
R_{k,j} = R_{k,j-1} + \frac{R_{k,j-1} - R_{k-1,j-1}}{4^j - 1}
$$

**Step 4. The table.**

$$
\begin{array}{c|ccc}
R_{k,0} & R_{k,1} & R_{k,2} \\
\hline
0.775000 & & \\
0.782794 & 0.785392 & \\
0.784747 & 0.785398 & 0.7853985
\end{array}
$$

Row 2: $0.782794 + \frac{0.782794 - 0.775000}{3} = 0.782794 + 0.002598 = 0.785392$
Row 3, column 1: $0.784747 + \frac{0.784747 - 0.782794}{3} = 0.784747 + 0.000651 = 0.785398$
Row 3, column 2: $0.785398 + \frac{0.785398 - 0.785392}{15} = 0.785398 + 0.0000004 = 0.7853985$

$$\boxed{I \approx 0.7853985 \quad \text{(trapezoid alone gives } 0.784747\text{)}}$$

> [!info] The exact answer is known here, so the error can be computed rather than estimated
> $$\int_0^1\frac{dx}{1+x^2} = \arctan x\Big|_0^1 = \arctan 1 = \frac{\pi}{4} = 0.7853981634$$
> The Romberg estimate $0.7853985235$ differs by $3.60 \times 10^{-7}$, a relative
> error of $4.6 \times 10^{-7}$. The bare trapezoid result at $h = 0.125$ is off by
> $6.51 \times 10^{-4}$, so Romberg improved the accuracy by a factor of about
> $1800$ using **no new function evaluations**.
>
> That last point is the whole appeal of Romberg. The same nine values of $f$
> serve every entry in the table, so accuracy is bought by rearranging numbers
> rather than by doing more work.

> [!note] Why each column divides by 3, then by 3, then by 15
> The denominators are $4^1 - 1 = 3$, $4^1 - 1 = 3$, $4^2 - 1 = 15$. The first
> column of extrapolations always uses $3$, because it is removing the $h^2$
> term. Only once two columns of trapezoid-like values have been combined does
> the order rise to $h^4$ and the denominator become $15$.
>
> The visible signature of a correct Romberg table is that each entry agrees with
> its neighbours to more digits than the one below it. If a column does not
> settle, the divisor is usually wrong rather than the arithmetic.

---
