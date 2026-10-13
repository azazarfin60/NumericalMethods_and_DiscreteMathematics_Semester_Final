---
title: "NM-5.2 · Simpson's 1/3 Rule"
tags:
  - numerical-methods
  - discrete-mathematics
  - topicwise
---


[🏠 Subtopic Index](00_Index.md) | [← Prev: NM-5.1 Trapezoidal Rule](NM-5.1_Trapezoidal_Rule.md) | [Next: NM-5.3 Simpson's 3/8 Rule →](NM-5.3_Simpsons_3_8_Rule.md)

---

# NM-5.2 · Simpson's 1/3 Rule

Every block below is copied from `../answers_explanation/`. The reasoning
is written once, in the year-wise file, and is not restated here.


### [2018 Q.6(a), 2023 Q.4(b)]

**Appeared in:** 2018 Q.6(a), 2023 Q.4(b)

**Question.** The vertical distance covered by a rocket from $t = 8$ to $t = 30$ seconds is given by: $x = \int_8^{30} \left( 2000 \ln \left[ \frac{140000}{140000 - 2100t} \right] - 9.8t \right) dt$. (i) Use eight-segment Simpson's $\frac{1}{3}$ rule to find the distance covered. (ii) Find the true error of part (i). (iii) Find the absolute relative error for part (i).

*[Marks: 08]*

**Solution.**

**(i) Eight-segment Simpson's $\frac{1}{3}$ rule.**

Simpson's $\frac{1}{3}$ rule needs an **even** number of segments, because it
consumes nodes in pairs. Eight is even, so there are nine nodes. With $n = 8$,

$$h = \frac{30 - 8}{8} = 2.75, \qquad t_i = 8 + 2.75i,\quad i = 0,\dots,8$$

which gives $t = 8,\ 10.75,\ 13.5,\ 16.25,\ 19,\ 21.75,\ 24.5,\ 27.25,\ 30$.

Evaluate $f(t) = 2000\ln\left[\dfrac{140000}{140000 - 2100t}\right] - 9.8t$ at each
node:

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

The weights are $1, 4, 2, 4, \dots, 4, 1$: the odd-indexed interior nodes get
$4$ and the even-indexed ones get $2$, with both endpoints getting $1$.

$$x \approx \frac{h}{3}\left[f_0 + f_8 + 4(f_1 + f_3 + f_5 + f_7) + 2(f_2 + f_4 + f_6)\right]$$

Grouping the sums first keeps the arithmetic honest:

$$f_1 + f_3 + f_5 + f_7 = 246.3351814 + 399.5165393 + 576.6423135 + 783.9826784 = 2006.4767126$$

$$f_2 + f_4 + f_6 = 320.2468886 + 484.7454726 + 676.0501168 = 1481.0424780$$

$$x \approx \frac{2.75}{3}\left[177.2667430 + 901.6740015 + 4(2006.4767126) + 2(1481.0424780)\right]$$

$$= \frac{2.75}{3}\left[177.2667430 + 901.6740015 + 8025.9068504 + 2962.0849560\right] = \frac{2.75}{3}(12066.9325509)$$

$$\boxed{x \approx 11061.3548\ \text{m}}$$

**(ii) The true error.** "True error" is the exact value minus the
approximation, and it has a sign; the *absolute* error does not. The exact
integral is obtainable here, which is what makes the question possible:

$$x_{\text{exact}} = \int_8^{30}\left(2000\ln\left[\frac{140000}{140000 - 2100t}\right] - 9.8t\right)dt = 11061.3355\ \text{m}$$

$$E_t = x_{\text{exact}} - x \approx 11061.3355 - 11061.3548 = -0.0193\ \text{m}$$

$$\boxed{E_t \approx -0.0193\ \text{m}}$$

The sign says the Simpson estimate lies *above* the true distance. For a
positive integrand that is convex over the whole interval, which this one is,
that is the expected direction.

**(iii) The absolute relative error.**

$$|\varepsilon_t| = \left|\frac{\text{true error}}{\text{true value}}\right| \times 100\% = \left|\frac{-0.0193}{11061.3355}\right|\times 100\%$$

$$\boxed{|\varepsilon_t| \approx 0.00017\%}$$

> [!info] Showing the error is truncation, not arithmetic
> Obtain the exact value by antidifferentiation:
> $\int 2000\ln\left[\dfrac{140000}{140000-2100t}\right]dt =
> -\dfrac{2000}{2100}(140000-2100t)\left[\ln\left(\dfrac{140000-2100t}{140000}\right) - 1\right]$,
> evaluated between the limits, which gives $11061.3355$.
>
> Then repeat the numerical integration with the mesh refined. Sixteen segments
> gives $11061.3368$ and thirty-two gives $11061.3356$. The three errors against
> the exact value are
>
> | segments | estimate | error | ratio to previous |
| :--: | --: | --: | --: |
| 8 | 11061.3548 | $1.93\times10^{-2}$ | |
| 16 | 11061.3368 | $1.22\times10^{-3}$ | $15.9$ |
| 32 | 11061.3356 | $7.6\times10^{-5}$ | $16.0$ |
>
> Each halving of $h$ divides the error by sixteen. That is precisely the
> $O(h^4)$ convergence of Simpson's $\frac{1}{3}$ rule, and it is the strongest
> evidence available that the residual is a truncation error of the rule. An
> arithmetic slip does not shrink by a factor of sixteen when the mesh is
> refined; it stays where it is. Note also that all three estimates lie *above*
> the exact value and approach it monotonically, which is what convexity
> predicts.

---

### [2019 Q.7(a)]

**Question.** Derive Simpson's one-third rule and hence show that the rule is exact up to degree three.

*[Marks: 04]*

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
quadratic, since $P_2 = f$. For a cubic, apply the rule to $f(x) = x^3$ on
$[-h, h]$, which by symmetry is equivalent to any interval:

$$\int_{-h}^{h}x^3\,dx = \left[\frac{x^4}{4}\right]_{-h}^{h} = 0$$

$$\frac{h}{3}\left[(-h)^3 + 4(0)^3 + (h)^3\right] = \frac{h}{3}(-h^3 + h^3) = 0$$

The two agree.

**Failure at degree four.** For $f(x) = x^4$ on $[-h, h]$:

$$\int_{-h}^{h}x^4\,dx = \frac{2h^5}{5}, \qquad \frac{h}{3}\left(h^4 + 0 + h^4\right) = \frac{2h^5}{3}$$

and $\dfrac{2}{3} \ne \dfrac{2}{5}$, so the rule is not exact for quartics.

$$\boxed{\int_{x_0}^{x_2} f\,dx \approx \frac{h}{3}(f_0 + 4f_1 + f_2)\ \text{exact for all polynomials of degree}\ \le 3}}$$

> [!note] Why the cubic works, since symmetry alone would not be enough
> The two integrals above both vanish, which proves nothing on its own: any rule
> returning $0$ would "agree" with the integral of $x^3$ on a symmetric interval.
>
> The reason the agreement is meaningful is that the weights $1, 4, 1$ were
> themselves obtained by **exact** integration of the quadratic basis. For a cubic
> the integrand is the quadratic part, which the rule reproduces exactly, plus a
> cubic part that is antisymmetric about the midpoint, and both the true integral
> and the weighted sum annihilate the antisymmetric piece. The two parts
> contribute independently and each is handled exactly.
>
> That is also why degree four fails: $x^4$ has a symmetric cubic-order correction
> that the antisymmetry argument no longer kills.

---

### [2020 Q.6(b)]

**Question.** A circuit is giving following output voltage equation: $v_0 = -\frac{1}{RC} \int_0^t v_i(t)\,dt$ where $R = 10\text{ k}\Omega, C = 1\ \mu\text{F}$. Use Simpson's $1/3$rd rule to find $v_0$ at $t = 1.25$.

*[Marks: 05]*

**Solution.**

| $t$ | 0 | 0.25 | 0.50 | 0.75 | 1.00 | 1.25 |
| --- | --: | --: | --: | --: | --: | --: |
| $v_i(t)$ | 1 | 0.9793 | 0.9195 | 0.8261 | 0.7081 | 0.6201 |

> [!warning] The question cannot be answered as literally printed, and that is the point
> Six points means **five intervals**, and Simpson's $1/3$ rule requires an **even**
> number of intervals. So the rule as asked for cannot be applied to the whole
> range at once.
>
> The tempting move is to write
> $\frac{h}{3}[v_0 + 4v_1 + 2v_2 + 4v_3 + v_5]$
> and evaluate it. That looks like Simpson's 1/3 and gives $0.8901$, hence
> $v_0 = -89.01$. It is wrong, and the reason is worth seeing: with six points and
> weights $1,4,2,4,1$, **$v_4$ is skipped entirely**. The panel structure has
> collapsed, and one of the six tabulated values never enters the calculation.
>
> That is the single most common way to lose marks on this type of question.

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

$$\boxed{v_0(1.25) = -106.34 \text{ V}}$$

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
> $0.25$ on a value near $106$. For reference, the plain trapezoid rule on all
> five intervals gives $1.060763$, hence $v_0 = -106.08$, which brackets them.
> **The choice of repair is not the exam's discriminator; recognising that a repair
> is needed at all is.**

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
> **3. Simpson's $1/3$ requires an even interval count.** Count the intervals, not
> the points: six points means five intervals, and five is odd.

> [!note] What the circuit is
> The relation $v_0 = -\frac{1}{RC}\int v_i\,dt$ is an op-amp integrator. The
> capacitor current is $i = C\frac{dv}{dt} = \frac{v_i}{R}$, and the output is the
> negative of the voltage across the capacitor, hence the minus sign. Simpson's
> $1/3$ rule is being used because the integrand is only known at six sample
> points, which is the situation in every real digitised measurement.
>
> **The integral, not the final multiplication, is where the numerical work is.**
> Everything after step 2 is one multiplication. Spending care on the panel
> structure and none on the final $\times 100$ is exactly backwards.

---

[🏠 Subtopic Index](00_Index.md) | [← Prev: NM-5.1 Trapezoidal Rule](NM-5.1_Trapezoidal_Rule.md) | [Next: NM-5.3 Simpson's 3/8 Rule →](NM-5.3_Simpsons_3_8_Rule.md)
