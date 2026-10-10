---
title: "NM-5 · Numerical Integration"
tags:
  - numerical-methods
  - discrete-mathematics
  - topicwise-clusters
---

[🏠 Master Index](00_Index.md) | [← Prev Topic: NM-4 · Curve Fitting](NM-4_Curve_Fitting.md) | [Next Topic: NM-6 · Optimization →](NM-6_Optimization.md)

---

# NM-5 · Numerical Integration

> **Topic ID:** NM-5  
> **Section:** Section A -- Numerical Methods  
> **Exam Weight:** 🔴 High Priority (Tier 1) | 7/8 Years Examined (88% Frequency) | Typical Weight: 7–14 marks (Question 4/5)  
> **Subtopics Included:** 7 subtopics (NM-5.1 through NM-5.7)  
> **Origin Layer:** Authored in `../answers_exam_style/`. All numerical results and boxed equations match character-for-character.

---

## 📑 Subtopics Covered in this Cluster

| Subtopic ID | Subtopic Title | Priority | Exam Frequency | Section Navigation |
|:---|:---|:---:|:---:|:---|
| **NM-5.1** | Trapezoidal Rule | 🟠 | 2018, 2019, 2021, 2022 | [Jump to NM-5.1](#nm-51) |
| **NM-5.2** | Simpson's 1/3 Rule | 🔴 | 2018, 2019, 2020, 2023 | [Jump to NM-5.2](#nm-52) |
| **NM-5.3** | Simpson's 3/8 Rule | 🟠 | 2019 | [Jump to NM-5.3](#nm-53) |
| **NM-5.4** | Rule Comparison & Step Constraints | 🔴 | 2020, 2023 | [Jump to NM-5.4](#nm-54) |
| **NM-5.5** | Romberg's Method | 🟠 | 2021, 2022, 2023 | [Jump to NM-5.5](#nm-55) |
| **NM-5.6** | Error Analysis in Integration | 🟠 | 2018, 2023 | [Jump to NM-5.6](#nm-56) |
| **NM-5.7** | Applied Integration | 🟠 | 2018, 2020, 2023 | [Jump to NM-5.7](#nm-57) |

---

<a id="nm-51"></a><a id="nm-5.1"></a>
## NM-5.1 · Trapezoidal Rule

### [2018 Q.6(b)]

**Question.** Determine the value of $n$ so that the trapezoidal rule will approximate the value of $\int_0^1 \sqrt{1 + x^2} \, dx$ with an error that is less than $0.01$.

**Solution.**

**The error bound.** The composite trapezoidal rule over $[a, b]$ with $n$
subintervals has error

$$|E| = \left|\frac{(b - a)h^2}{12}f''(\xi)\right| \le \frac{(b - a)h^2}{12}\max|f''|$$

Here $a = 0$, $b = 1$, and

$$f(x) = \sqrt{1 + x^2}$$

$$f'(x) = \frac{x}{\sqrt{1+x^2}}, \qquad f''(x) = \frac{1}{(1+x^2)^{3/2}}$$

On $[0, 1]$ the maximum of $|f''|$ is at $x = 0$, where
$f''(0) = 1$. So

$$|E| \le \frac{h^2}{12}(1) = \frac{h^2}{12}$$

**Solve for $h$ then $n$.**

$$\frac{h^2}{12} < 0.01 \implies h^2 < 0.12 \implies h < 0.3464$$

$$n = \frac{b - a}{h} > \frac{1}{0.3464} = 2.8868$$

Hence the smallest integer satisfying the bound is

$$\boxed{n = 3}$$

**Direct check.** Evaluating the trapezoidal rule:

| $n$ | $h$ | Approximation | Error |
| :--: | :--: | :-- | :-- |
| 2 | 0.50 | 1.1625704 | $0.014777$ |
| 3 | 0.3333 | 1.1543499 | $0.006556$ |

At $n = 2$ the error exceeds $0.01$, and at $n = 3$ it falls below, confirming
$n = 3$.

> [!info] Check against the exact integral
> The exact value is
> $\int_0^1\sqrt{1+x^2}\,dx = \left[\dfrac{x\sqrt{1+x^2}}{2} + \dfrac{\ln(x + \sqrt{1+x^2})}{2}\right]_0^1 = \dfrac{\sqrt2 + \ln(1+\sqrt2)}{2} = 1.1477936$.
> The $n = 3$ value $1.1543499$ differs by $0.006556$, which is below $0.01$;
> the $n = 2$ value differs by $0.014777$, which is not. The error bound
> $\dfrac{h^2}{12}$ is also confirmed numerically: at $n = 3$, $h = 1/3$, the
> bound gives $\dfrac{1}{9\cdot12} = 0.009259$, and the actual error $0.006556$ is
> below the bound, as it must be.

---

### [2019 Q.6(c)]

**Question.** Discuss trapezoidal rule of numerical integration.

**Solution.**

The **trapezoidal rule** approximates $\int_a^b f(x)\,dx$ by replacing the curve
with a straight line joining the endpoints of each subinterval, so the area under
the curve becomes the area of a set of trapezoids.

**Derivation.** Over one interval $[x_0, x_0 + h]$, the straight line through
$(x_0, f_0)$ and $(x_1, f_1)$ has slope $\dfrac{f_1 - f_0}{h}$, and its integral
is

$$\int_{x_0}^{x_1} f(x)\,dx \approx \frac{h}{2}(f_0 + f_1)$$

**Composite rule.** Over $[a, b]$ with $n$ subintervals of width
$h = \dfrac{b - a}{n}$, summing the one-interval result gives

$$\int_a^b f(x)\,dx \approx \frac{h}{2}\left[f_0 + 2f_1 + 2f_2 + \cdots + 2f_{n-1} + f_n\right]$$

$$\boxed{\int_a^b f(x)\,dx \approx \frac{h}{2}\left[f(a) + f(b) + 2\sum_{i=1}^{n-1}f_i\right]}$$

**Error.** The error over one interval is $-\dfrac{h^3}{12}f''(\xi)$, so the
composite error is

$$E = -\frac{(b - a)h^2}{12}f''(\xi), \qquad O(h^2)$$

**Properties.**

1. First order of accuracy: halving $h$ reduces the error by a factor of four.
2. The rule is exact for a straight line, and over-shoots for a curve that
   is concave up, since the chord lies above the curve.
3. It is the basis of the trapezoidal rule for sampled data, where the area of a
   measured record is obtained with no requirement that the samples be equally
   spaced in value.
4. Its ease of use makes it the obvious first estimate, but Simpson's rules are
   preferred when smoothness and accuracy are required.

---

### [2021 Q.8(a)]

**Question.** Derive the following numerical integration formula: $\int_{x_0}^{x_n} y\,dx = \frac{h}{2}[y_0 + 2(y_1 + y_2 + \cdots + y_{n-1}) + y_n]$

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

$$
\boxed{\int_{x_0}^{x_n} y\,dx = \frac{h}{2}\left[y_0 + 2\sum_{i=1}^{n-1}y_i + y_n\right] + O(h^2)}
$$

> [!note] Two ways to see it
> **Geometrically.** Each panel is a trapezoid. Draw them all, add the areas: the
> interior ordinates are shared by two panels and so counted twice, the ends once.
> **By an exact integral.** Linear interpolation between the nodes gives
> $y(x) = \frac{y_{i+1}-y_i}{h}(x-x_i) + y_i$ on each panel. Integrating that
> exactly over $[x_i, x_{i+1}]$ gives $\frac{h}{2}(y_i + y_{i+1})$ per panel, and
> summing reproduces the formula with no error analysis needed.

---

### [2022 Q.3(a)]

**Question.** Compute the value of $I = \int_0^1 \frac{dx}{1 + x^2}$ using the trapezoidal rule with $h = 0.5, 0.25$ and $0.125$. Then obtain a better estimate using Romberg's method.

**Solution.**

**Step 1. Function values.**

| $x$ | 0 | 0.125 | 0.25 | 0.375 | 0.5 | 0.625 | 0.75 | 0.875 | 1 |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| $f(x) = \frac{1}{1+x^2}$ | 1.000000 | 0.984615 | 0.941176 | 0.876712 | 0.800000 | 0.719101 | 0.640000 | 0.566372 | 0.500000 |

**Step 2. Trapezoidal rule, first column.**

$$
T_n = \frac{h}{2}\left[f_0 + 2f_1 + 2f_2 + \cdots + 2f_{n-1} + f_n\right]
$$

At $h = 0.5$, $n = 2$:

$$
T_2 = \frac{0.5}{2}\left[1 + 2(0.8) + 0.5\right] = 0.25(3.1) = 0.775000
$$

At $h = 0.25$, $n = 4$:

$$
T_4 = \frac{0.25}{2}\left[1 + 2(0.941176 + 0.8 + 0.640000) + 0.5\right] = 0.125(6.262352) = 0.782794
$$

At $h = 0.125$, $n = 8$:

$$
T_8 = \frac{0.125}{2}\left[1 + 2(0.984615 + 0.941176 + 0.876712 + 0.800000 + 0.719101 + 0.640000 + 0.566372) + 0.5\right]
$$

$$
= 0.0625\left[1 + 2(5.527976) + 0.5\right] = 0.0625(12.555952) = 0.784747
$$

**Step 3. Richardson extrapolation.** The trapezoid rule has $O(h^2)$ error, so
each new column divides by $4^1 - 1 = 3$:

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

$$
\boxed{I \approx 0.7853985 \quad \text{(trapezoid alone gives } 0.784747\text{)}}
$$

> [!info] Check against the exact integral
> $$\int_0^1\frac{dx}{1+x^2} = \arctan x\Big|_0^1 = \arctan 1 - 0 = \frac{\pi}{4} = 0.7853981634$$
> The Romberg estimate $0.7853985235$ differs by $3.60\times10^{-7}$, a relative
> error of $4.6 \times 10^{-7}$. The bare trapezoid result at $h = 0.125$ is off
> by $6.5\times10^{-4}$, so Romberg improved the accuracy by about three orders
> of magnitude using **no new function evaluations**. The same nine values of
> $f$ serve every entry in the table.

> [!note] The error here is computable, not estimated
> $\pi/4$ is known exactly, so the true error can be computed rather than
> estimated. The trapezoid column converges as $h^2$, so successive differences
> shrink by roughly $4$ each time, which is what the factor of $3$ in the
> extrapolation removes.

---

<a id="nm-52"></a><a id="nm-5.2"></a>
## NM-5.2 · Simpson's 1/3 Rule

### [2018 Q.6(a), 2023 Q.4(b)]

**Appeared in:** 2018 Q.6(a), 2023 Q.4(b)

**Question.** The vertical distance covered by a rocket from $t = 8$ to $t = 30$ seconds is given by: $x = \int_8^{30} \left( 2000 \ln \left[ \frac{140000}{140000 - 2100t} \right] - 9.8t \right) dt$. (i) Use eight-segment Simpson's $\frac{1}{3}$ rule to find the distance covered. (ii) Find the true error of part (i). (iii) Find the absolute relative error for part (i).

**Solution.**

**(i) Eight-segment Simpson's $\frac{1}{3}$ rule.** With $n = 8$,
$h = \dfrac{30 - 8}{8} = 2.75$, the nodes are
$t = 8,\ 10.75,\ 13.5,\ 16.25,\ 19,\ 21.75,\ 24.5,\ 27.25,\ 30$.

Evaluating $f(t) = 2000\ln\left[\dfrac{140000}{140000 - 2100t}\right] - 9.8t$:

| $i$ | $t_i$ | $f(t_i)$ | weight |
| :--: | :--: | :-- | :--: |
| 0 | 8.00000 | 177.2667430 | 1 |
| 1 | 10.75000 | 246.3351814 | 4 |
| 2 | 13.50000 | 320.2468886 | 2 |
| 3 | 16.25000 | 399.5165393 | 4 |
| 4 | 19.00000 | 484.7454726 | 2 |
| 5 | 21.75000 | 576.6423135 | 4 |
| 6 | 24.50000 | 676.0501168 | 2 |
| 7 | 27.25000 | 783.9826784 | 4 |
| 8 | 30.00000 | 901.6740015 | 1 |

$$x \approx \frac{h}{3}\left[f_0 + f_8 + 4(f_1 + f_3 + f_5 + f_7) + 2(f_2 + f_4 + f_6)\right]$$

$$= \frac{2.75}{3}\left[177.2667430 + 901.6740015 + 4(246.3351814 + 399.5165393 + 576.6423135 + 783.9826784) + 2(320.2468886 + 484.7454726 + 676.0501168)\right]$$

The weighted sums are

$$4(2006.4767126) = 8025.9068504, \qquad 2(1481.0424780) = 2962.0849560$$

$$x \approx \frac{2.75}{3}(177.2667430 + 901.6740015 + 8025.9068504 + 2962.0849560) = \frac{2.75}{3}(12066.9325509)$$

$$\boxed{x \approx 11061.3548\ \text{m}}$$

**(ii) The true error.** The exact value of the integral is

$$x_{\text{exact}} = \int_8^{30}\left(2000\ln\left[\frac{140000}{140000 - 2100t}\right] - 9.8t\right)dt = 11061.3355\ \text{m}$$

Hence the true error is

$$E_t = x_{\text{exact}} - x \approx 11061.3355 - 11061.3548 = -0.0193\ \text{m}$$

$$\boxed{E_t \approx -0.0193\ \text{m}}$$

**(iii) The absolute relative error.**
 
$$|\varepsilon_t| = \left|\frac{\text{true error}}{\text{true value}}\right| \times 100\% = \left|\frac{-0.0193}{11061.3355}\right|\times 100\%$$

$$\boxed{|\varepsilon_t| \approx 0.00017\%}$$

> [!info] Check against the exact integral and a 16-segment estimate
> The exact value is obtained by antidifferentiation,
> $\int 2000\ln\left[\dfrac{140000}{140000-2100t}\right]dt = -\dfrac{2000}{2100}(140000-2100t)\left[\ln\left(\dfrac{140000-2100t}{140000}\right) - 1\right]$,
> which evaluates to $11061.3355$ between the limits. The eight-segment result
> $11061.3548$ is larger by $0.0193$, an error of $0.00017\%$. Repeating with
> $16$ segments gives $x = 11061.3368$, still above the exact integral but
> sixteen times closer to it, and a third pass with $32$ segments gives
> $11061.3356$. The errors $1.93\times10^{-2}$, $1.22\times10^{-3}$ and
> $7.6\times10^{-5}$ fall in the ratio $16:1$ at each halving of $h$, which is
> the $O(h^4)$ convergence of Simpson's rule and cannot be produced by an
> arithmetic slip. The error is a truncation error of the rule.

---

### [2019 Q.7(a)]

**Question.** Derive Simpson's one-third rule and hence show that the rule is exact up to degree three.

**Solution.**

**Derivation.** Take three equally spaced nodes

$$x_0,\qquad x_1 = x_0 + h,\qquad x_2 = x_0 + 2h$$

and replace $f$ by the quadratic $P_2(x)$ through the three values $f_0, f_1,
f_2$. The integral of $P_2$ is the approximation.

With $x = x_0 + ph$, so $dx = h\,dp$, the Lagrange basis is

$$L_0 = \frac{(p - 1)(p - 2)}{2}, \qquad L_1 = -p(p - 2), \qquad L_2 = \frac{p(p - 1)}{2}$$

and

$$\int_{x_0}^{x_2} P_2\,dx = h\int_0^2 \left[f_0\frac{(p-1)(p-2)}{2} - f_1 p(p-2) + f_2\frac{p(p-1)}{2}\right]dp$$

Integrating each basis function separately:

$$\int_0^2 \frac{(p-1)(p-2)}{2}dp = \frac{1}{2}\int_0^2(p^2 - 3p + 2)dp = \frac{1}{2}\left[\frac{8}{3} - 6 + 4\right] = \frac{1}{2}\cdot\frac{2}{3} = \frac{1}{3}$$

$$\int_0^2 -p(p - 2)\,dp = -\int_0^2(p^2 - 2p)dp = -\left[\frac{8}{3} - 4\right] = \frac{4}{3}$$

$$\int_0^2 \frac{p(p-1)}{2}dp = \frac{1}{2}\int_0^2(p^2 - p)dp = \frac{1}{2}\left[\frac{8}{3} - 2\right] = \frac{1}{2}\cdot\frac{2}{3} = \frac{1}{3}$$

Hence

$$\int_{x_0}^{x_2} f(x)\,dx \approx \frac{h}{3}\left(f_0 + 4f_1 + f_2\right)$$

which is **Simpson's one-third rule**. Over $[a, b]$ with $n$ even and
$h = \dfrac{b-a}{n}$, the composite form is

$$\int_a^b f(x)\,dx \approx \frac{h}{3}\left[f_0 + 4f_1 + 2f_2 + 4f_3 + \cdots + 2f_{n-2} + 4f_{n-1} + f_n\right]$$

**Exactness to degree three.** By construction the rule is exact for every
quadratic, since $P_2 = f$. For a cubic, apply the rule to
$f(x) = x^3$ on $[-h, h]$, which by symmetry is equivalent to any interval:

$$\int_{-h}^{h}x^3\,dx = \left[\frac{x^4}{4}\right]_{-h}^{h} = 0$$

$$\frac{h}{3}\left[(-h)^3 + 4(0)^3 + (h)^3\right] = \frac{h}{3}(-h^3 + h^3) = 0$$

The two agree. The cause is symmetry: for a cubic antisymmetric about the
midpoint, both the true integral and the weighted sum vanish identically, and
each weighted sum reproduces the exact area because the weights $1, 4, 1$ were
themselves derived from exact integration of the quadratic basis. Hence the rule
is exact for $1, x, x^2, x^3$.

**Failure at degree four.** For $f(x) = x^4$ on $[-h, h]$:

$$\int_{-h}^{h}x^4\,dx = \frac{2h^5}{5}, \qquad \frac{h}{3}\left(h^4 + 0 + h^4\right) = \frac{2h^5}{3}$$

and $\dfrac{2}{3} \ne \dfrac{2}{5}$, so the rule is not exact for quartics.

$$\boxed{\int_{x_0}^{x_2} f\,dx \approx \frac{h}{3}(f_0 + 4f_1 + f_2)\ \text{exact for all polynomials of degree}\ \le 3}$$

---

### [2020 Q.6(b)]

**Question.** A circuit is giving following output voltage equation: $v_0 = -\frac{1}{RC} \int_0^t v_i(t)\,dt$ where $R = 10\text{ k}\Omega, C = 1\ \mu\text{F}$. Use Simpson's $1/3$rd rule to find $v_0$ at $t = 1.25$.

**Solution.**

| $t$ | 0 | 0.25 | 0.50 | 0.75 | 1.00 | 1.25 |
| --- | --: | --: | --: | --: | --: | --: |
| $v_i(t)$ | 1 | 0.9793 | 0.9195 | 0.8261 | 0.7081 | 0.6201 |

> [!warning] Six points give five intervals, and five is odd
> Simpson's $1/3$ rule needs an **even** number of subintervals, because each
> panel spans two. This table has six points and therefore **five** subintervals.
> **The rule cannot be applied to the range $0$ to $1.25$ in one piece.**
>
> Applying the weights $1, 4, 2, 4, 2, 1$ across all six points gives $1.008075$,
> hence $v_0 = -100.8$, and that answer is wrong. Every individual
> multiplication is correct; the rule simply does not apply to an odd count.
> This is the single most common way to lose marks on this type of question.
>
> Three repairs are legal. They are given below, and they all land within
> $0.25$ of each other on a value near $106$.

**Step 1. The constant.**

$$RC = (10 \times 10^3)(1 \times 10^{-6}) = 10^{-2} \text{ s} = 0.01 \text{ s}, \qquad \frac{1}{RC} = 100 \text{ s}^{-1}$$

**Step 2. The integral.** Take $h = 0.25$ s. The largest even block is
$t = 0$ to $t = 1.00$, four intervals, and the leftover interval
$t = 1.00$ to $1.25$ goes to the trapezoid rule.

**Simpson's $1/3$ on $0$ to $1.00$**, with weights $1, 4, 2, 4, 1$:

$$
I_{1/3} = \frac{h}{3}\left[v_0 + 4v_1 + 2v_2 + 4v_3 + v_4\right]
= \frac{0.25}{3}\left[1 + 4(0.9793) + 2(0.9195) + 4(0.8261) + 0.7081\right]
$$

$$
= \frac{0.25}{3}\left[1 + 3.9172 + 1.8390 + 3.3044 + 0.7081\right] = \frac{0.25}{3}(10.7687) = 0.89739167
$$

**Trapezoid on $1.00$ to $1.25$:**

$$
I_T = \frac{h}{2}(v_4 + v_5) = \frac{0.25}{2}(0.7081 + 0.6201) = 0.125(1.3282) = 0.166025
$$

**Total:**

$$
I = 0.89739167 + 0.166025 = 1.06341667
$$

**Step 3. The output voltage.** The leading minus sign comes from the inverting
amplifier that realises the equation, and it must be carried through.

$$
v_0 = -\frac{1}{RC}\,I = -100(1.06341667) = -106.341667
$$

$$
\boxed{v_0(1.25) = -106.34 \text{ V}}
$$

> [!info] Check by two independent routes
> **Repair 2: trapezoid first, then Simpson.** Handle $t = 0$ to $0.25$ with the
> trapezoid rule and Simpson's $1/3$ on the remaining four intervals,
> $0.25$ to $1.25$:
> $$I_T = 0.125(1 + 0.9793) = 0.2474125, \qquad I_{1/3} = \frac{0.25}{3}\left[0.9793 + 4(0.9195) + 2(0.8261) + 4(0.7081) + 0.6201\right] = 0.8135000$$
> $$I = 1.0609125 \qquad\Rightarrow\qquad v_0 = -106.0913$$
> A different route, $0.25$ different on $106$, that is $0.24\%$.
>
> **Repair 3: mix Simpson's $1/3$ and $3/8$.** Two intervals from $0$ to $0.50$ by
> $1/3$, then three intervals from $0.50$ to $1.25$ by $3/8$:
> $$I_{1/3} = \frac{0.25}{3}\left[1 + 4(0.9793) + 0.9195\right] = 0.48639167$$
> $$I_{3/8} = \frac{3(0.25)}{8}\left[0.9195 + 3(0.8261) + 3(0.7081) + 0.6201\right] = \frac{0.09375}(6.1422) = 0.57583125$$
> $$I = 1.06222292 \qquad\Rightarrow\qquad v_0 = -106.2223$$
>
> All three legal repairs give $v_0$ between $-106.09$ and $-106.34$, a spread of
> $0.25$ on a value near $106$. **The choice of repair is not the exam's
> discriminator; recognising that a repair is needed at all is.**

> [!warning] Three things to get right here
> **1. The sign.** $v_0$ is **negative**. The equation carries a leading minus and
> the integral of a positive $v_i$ is positive, so the answer must be negative. A
> positive $v_0$ means the sign was dropped, and it is the most common slip in
> this question.
>
> **2. The units.** $\frac{1}{RC} = 100$, not $0.01$ and not $10^{-8}$. A $10$
> k$\Omega$ resistor and a $1\ \mu$F capacitor give a time constant of
> $10^4 \times 10^{-6} = 10^{-2}$ s, so the reciprocal is $100$. Converting
> microfarads to farads is where the factor of $10^6$ comes from.
>
> **3. Simpson's $1/3$ requires an even interval count.** Count the intervals,
> not the points: six points means five intervals, and five is odd.

> [!note] What the circuit is
> The relation $v_0 = -\frac{1}{RC}\int v_i\,dt$ is an op-amp integrator. The
> capacitor current is $i = C\frac{dv}{dt} = \frac{v_i}{R}$, and the output is the
> negative of the voltage across the capacitor, hence the minus sign. Simpson's
> $1/3$ rule is being used because the integrand is only known at six sample
> points, which is the situation in every real digitised measurement.

---

<a id="nm-53"></a><a id="nm-5.3"></a>
## NM-5.3 · Simpson's 3/8 Rule

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

<a id="nm-54"></a><a id="nm-5.4"></a>
## NM-5.4 · Rule Comparison & Step Constraints

### [2020 Q.6(a), 2023 Q.4(c)]

**Appeared in:** 2020 Q.6(a), 2023 Q.4(c)

**Question.** Compare Simpson's $1/3$rd and $3/8$th rules.

**Solution.**

Both are **Newton-Cotes** rules: they fit a polynomial through the data at
equally spaced nodes and integrate that polynomial exactly over the panel. They
differ in how many nodes each panel uses and therefore in which interval counts
each admits.

| | Simpson's $1/3$ | Simpson's $3/8$ |
| :-- | :-- | :-- |
| Subintervals per panel | 2 | 3 |
| Nodes per panel | 3 | 4 |
| Weights | $1,\ 4,\ 1$ | $1,\ 3,\ 3,\ 1$ |
| Prefactor | $\dfrac{h}{3}$ | $\dfrac{3h}{8}$ |
| Panel interval count | Must be **even** | Must be a **multiple of 3** |
| Total intervals $n$ | Even | Multiple of 3 |
| Order of accuracy | 4 | 4 |
| Leading error term | $-\dfrac{h^5}{90}f^{(4)}$ | $-\dfrac{3h^5}{80}f^{(4)}$ |
| Error constant | $\frac{1}{90} = 0.0111$ | $\frac{3}{80} = 0.0375$ |

**Both are fourth order**, so both need a function with $f^{(4)}$ continuous
over the range. Neither is fourth order on a function with a discontinuous
fourth derivative, and neither is safe near a vertical asymptote or a jump.

**The accuracy difference.** With the same $h$, Simpson's $3/8$ has a leading
error constant $3.375$ times larger than $1/3$. So for equal $h$, **$1/3$ is more
accurate**, and $1/3$ is the default choice.

**The one place $3/8$ wins.** When the total interval count is odd, $1/3$ is
inapplicable while $3/8$ can still be used, provided the count is a multiple of
$3$. Five intervals is the standard case: $1/3$ is stuck, $3/8$ takes three of
them and something else takes two. That exact situation is in Q.6(b) below, and it is why the rule is worth
knowing.

**Standard mixed strategy** for an odd $n$ not divisible by $3$, for example
$n = 5$: apply $3/8$ to the last three intervals and $1/3$ to the remaining two,
or apply $1/3$ to the largest even block and the trapezoid rule to the leftover
one interval. Both appear in Q.6(b).

**Why the error behaves as it does.** A $3$-node panel interpolates a quadratic,
whose integration error involves $f''$. A $4$-node panel interpolates a cubic,
involving $f^{(4)}$. Symmetry about the panel centre cancels the odd-order terms
in both cases, which is why both reach fourth order rather than third.

$$
\boxed{\text{Both are fourth order; } 1/3 \text{ is more accurate at equal } h \text{ but needs an even interval count}}
$$

---

<a id="nm-55"></a><a id="nm-5.5"></a>
## NM-5.5 · Romberg's Method

### [2021 Q.8(b), 2023 Q.2(c)]

**Appeared in:** 2021 Q.8(b), 2023 Q.2(c)

**Question.** Use Romberg's method to compute: $\int_1^2 \frac{1}{2+x}\,dx$. Consider $h = 0.5, 0.25, 0.125$.

**Solution.**

**Step 1. The first column, composite trapezoid.**

$$
T_n = \frac{h}{2}\left[f_0 + 2f_1 + \cdots + 2f_{n-1} + f_n\right], \qquad f_i = \frac{1}{2+x_i}
$$

At $h = 0.5$, $n = 2$, nodes $x = 1, 1.5, 2$:

$$
T_2 = \frac{0.5}{2}\left[\frac{1}{3} + 2\cdot\frac{1}{3.5} + \frac{1}{4}\right] = 0.25\left[0.333333 + 0.571429 + 0.25\right] = 0.288690
$$

At $h = 0.25$, $n = 4$:

$$
T_4 = \frac{0.25}{2}\left[\frac{1}{3} + 2\left(\frac{1}{3.25} + \frac{1}{3.5} + \frac{1}{3.75} + \frac{1}{4.25}\right) + \frac{1}{4}\right] = 0.287935
$$

At $h = 0.125$, $n = 8$:

$$
T_8 = 0.287745
$$

**Step 2. Second column.** The trapezoid rule has $O(h^2)$ error, so extrapolate with
the factor $4^1 - 1 = 3$:

$$
R_{k,1} = R_{k,0} + \frac{R_{k,0} - R_{k-1,0}}{4 - 1}
$$

**Step 3. Third column.** The result above is Simpson's rule, carrying $O(h^4)$, so
the factor is $4^2 - 1 = 15$:

$$
R_{k,2} = R_{k,1} + \frac{R_{k,1} - R_{k-1,1}}{16 - 1}
$$

**The table.**

$$
\begin{array}{c|ccc}
R_{k,0} & R_{k,1} & R_{k,2} \\
\hline
0.288690 & & \\
0.287935 & 0.287683 & \\
0.287745 & 0.287682 & 0.287682
\end{array}
$$

Row 2: $0.287935 + \frac{0.287935 - 0.288690}{3} = 0.287935 - 0.000252 = 0.287683$
Row 3, column 1: $0.287745 + \frac{0.287745 - 0.287935}{3} = 0.287745 - 0.000063 = 0.287682$
Row 3, column 2: $R_{3,2} = R_{3,1} + \frac{R_{3,1} - R_{2,1}}{15}$

Taken literally at the six decimals the table prints, this gives
$0.287682 - \frac{10^{-6}}{15} = 0.2876819$. Carried unrounded, which is what the
answer below uses, the same line gives $0.2876820735$, since the unrounded entries
are $R_{2,1} = 0.2876832$ and $R_{3,1} = 0.2876821$.

$$
\boxed{I \approx 0.2876821}
$$

> [!info] Check against the exact integral
> $$\int_1^2\frac{dx}{2+x} = \ln(2+x)\Big|_1^2 = \ln 4 - \ln 3 = \ln\frac{4}{3} = 0.2876820725$$
> The Romberg value differs by $1.05\times10^{-9}$, a relative error of
> $3.6\times10^{-9}$.
>
> For comparison, plain composite Simpson with $n = 8$ gives $0.2876821408$, whose
> relative error is $2.4\times10^{-7}$. **Romberg is about 65 times more accurate
> from the same function values**, because each column only recombines entries
> already in the table. No extra work.

> [!note] Reading the table
> The left column converges slowly, $0.2887 \to 0.2879 \to 0.2877$, alternating
> because the trapezoid error is negative and shrinking like $h^2$. Each step right
> multiplies the accuracy by about $4^2 = 16$ or better. Three levels give roughly
> eighth-order accuracy from a second-order rule, which is the whole point of the
> method.

---

---

**Also asked here.**

- *2022 Q.3(a)* is the same question as [[NM-5.1_Trapezoidal_Rule|NM-5.1]], which is written in `NM-5.1`.

---

<a id="nm-56"></a><a id="nm-5.6"></a>
## NM-5.6 · Error Analysis in Integration

---

**Every question that reaches this subtopic is written in the subtopic it is filed under.** Nothing is answered here, and that is deliberate rather than an omission: the subtopic holds the questions in the taxonomy but owns no block of its own.

- *2018 Q.6(a)* is the same question as [[NM-5.2_Simpsons_1_3_Rule|NM-5.2]], which is written in `NM-5.2`.
- *2018 Q.6(b)* is the same question as [[NM-5.1_Trapezoidal_Rule|NM-5.1]], which is written in `NM-5.1`.
- *2023 Q.4(b)* is the same question as [[NM-5.2_Simpsons_1_3_Rule|NM-5.2]], which is written in `NM-5.2`.

---

<a id="nm-57"></a><a id="nm-5.7"></a>
## NM-5.7 · Applied Integration

---

**Every question that reaches this subtopic is written in the subtopic it is filed under.** Nothing is answered here, and that is deliberate rather than an omission: the subtopic holds the questions in the taxonomy but owns no block of its own.

- *2018 Q.6(a)* is the same question as [[NM-5.2_Simpsons_1_3_Rule|NM-5.2]], which is written in `NM-5.2`.
- *2020 Q.6(b)* is the same question as [[NM-5.2_Simpsons_1_3_Rule|NM-5.2]], which is written in `NM-5.2`.
- *2023 Q.4(b)* is the same question as [[NM-5.2_Simpsons_1_3_Rule|NM-5.2]], which is written in `NM-5.2`.

---

[🏠 Master Index](00_Index.md) | [← Prev Topic: NM-4 · Curve Fitting](NM-4_Curve_Fitting.md) | [Next Topic: NM-6 · Optimization →](NM-6_Optimization.md)
