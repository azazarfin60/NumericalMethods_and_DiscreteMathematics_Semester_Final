[← Previous: NM-4 Lower — Regression & Interpolation](NM-4_Lower_Regression_Theory_Interpolation_Methods.md) | [🏠 Index](00_Index.md) | [Next: NM-5.4 Rule Comparison →](NM-5.4_Rule_Comparison_and_Step_Constraints.md)

---

# NM-5.2: Simpson's One-Third Rule
> **Section:** A (Numerical Methods) | **Priority:** 🔴 | **Exam Frequency:** 4/8 years
> **Sources:** Jain Ch.6 §6.5, Shishir Notes §04 pp.53–72, Raidah Notes p.17

## Why This Topic Matters

Simpson's 1/3 rule is the most-tested numerical integration method in ECE 2213. It appears with the rocket distance problem (2018, 2023), the op-amp integrator circuit (2020), and as a derivation question (2019). The rule sits at the heart of integration questions and pairs naturally with the 3/8 rule and Romberg's method.

---

## 📝 Key Definitions

> **Newton-Cotes formula:** A numerical integration formula that approximates the integral by fitting a polynomial through equally spaced data points and integrating that polynomial exactly over the interval. Simpson's 1/3 rule is the second Newton-Cotes formula (using a quadratic).

> **Simpson's 1/3 rule (single panel):** The approximation obtained by passing a quadratic through three equally spaced points and integrating it:

$$
\int_{x_0}^{x_2} f(x)\,dx \approx \frac{h}{3}(f_0 + 4f_1 + f_2)
$$

> **Composite Simpson's 1/3 rule:** The extension to $n$ subintervals ($n$ must be **even**), each of width $h = \frac{b-a}{n}$:

$$
\int_a^b f(x)\,dx \approx \frac{h}{3}\left[f_0 + 4f_1 + 2f_2 + 4f_3 + \cdots + 2f_{n-2} + 4f_{n-1} + f_n\right]
$$

---

## Derivation from Quadratic Interpolation

The idea is simple. Take three equally spaced nodes:

$$
x_0, \qquad x_1 = x_0 + h, \qquad x_2 = x_0 + 2h
$$

Replace $f$ by the quadratic $P_2(x)$ that passes through $(x_0, f_0)$, $(x_1, f_1)$, $(x_2, f_2)$. Then integrate $P_2$ instead of $f$.

**Change of variable.** Let $x = x_0 + ph$, so $dx = h\,dp$. The Lagrange basis polynomials become:

$$
L_0 = \frac{(p-1)(p-2)}{2}, \qquad L_1 = -p(p-2), \qquad L_2 = \frac{p(p-1)}{2}
$$

The integral of the interpolating polynomial is:

$$
\int_{x_0}^{x_2} P_2\,dx = h\int_0^2 \left[f_0\frac{(p-1)(p-2)}{2} - f_1\,p(p-2) + f_2\frac{p(p-1)}{2}\right]dp
$$

**Evaluate each integral separately.**

$$
\int_0^2 \frac{(p-1)(p-2)}{2}\,dp = \frac{1}{2}\int_0^2(p^2 - 3p + 2)\,dp = \frac{1}{2}\left[\frac{8}{3} - 6 + 4\right] = \frac{1}{2}\cdot\frac{2}{3} = \frac{1}{3}
$$

$$
\int_0^2 -p(p-2)\,dp = -\int_0^2(p^2 - 2p)\,dp = -\left[\frac{8}{3} - 4\right] = \frac{4}{3}
$$

$$
\int_0^2 \frac{p(p-1)}{2}\,dp = \frac{1}{2}\int_0^2(p^2 - p)\,dp = \frac{1}{2}\left[\frac{8}{3} - 2\right] = \frac{1}{2}\cdot\frac{2}{3} = \frac{1}{3}
$$

So the coefficients are $\frac{1}{3}$, $\frac{4}{3}$, $\frac{1}{3}$. Factor out $h$:

$$
\int_{x_0}^{x_2} f(x)\,dx \approx h\left[\frac{1}{3}f_0 + \frac{4}{3}f_1 + \frac{1}{3}f_2\right] = \frac{h}{3}(f_0 + 4f_1 + f_2)
$$

That is Simpson's one-third rule.

---

## Proof of Exactness for Polynomials of Degree ≤ 3

The rule was built from a quadratic interpolant, so it is exact for any polynomial of degree $\le 2$ by construction (the interpolant equals $f$ exactly).

**Cubic test.** Apply the rule to $f(x) = x^3$ on the symmetric interval $[-h, h]$:

$$
\int_{-h}^{h} x^3\,dx = \left[\frac{x^4}{4}\right]_{-h}^{h} = 0
$$

$$
\frac{h}{3}\left[(-h)^3 + 4(0)^3 + (h)^3\right] = \frac{h}{3}(-h^3 + h^3) = 0
$$

Both give zero. The weights $1, 4, 1$ were derived from exact integration of the quadratic basis, and the cubic part is antisymmetric about the midpoint. Both the true integral and the weighted sum annihilate the antisymmetric piece. So the rule handles $1, x, x^2, x^3$ all exactly.

**Failure at degree 4.** For $f(x) = x^4$ on $[-h, h]$:

$$
\int_{-h}^{h} x^4\,dx = \frac{2h^5}{5}, \qquad \frac{h}{3}(h^4 + 0 + h^4) = \frac{2h^5}{3}
$$

$\frac{2}{3} \ne \frac{2}{5}$. The rule is not exact for quartics.

$$
\boxed{\int_{x_0}^{x_2} f\,dx \approx \frac{h}{3}(f_0 + 4f_1 + f_2)\ \text{exact for all polynomials of degree}\ \le 3}
$$

---

## The Composite Rule and Subinterval Constraints

To integrate over $[a, b]$ with the composite form, divide $[a, b]$ into $n$ subintervals of width $h = \frac{b-a}{n}$.

**The constraint:** $n$ must be **even**. Each panel of Simpson's 1/3 uses two subintervals (three points), so the total number of subintervals must be divisible by 2.

The composite formula with weights $1, 4, 2, 4, 2, \ldots, 2, 4, 1$:

$$
\int_a^b f(x)\,dx \approx \frac{h}{3}\left[f_0 + 4f_1 + 2f_2 + 4f_3 + \cdots + 2f_{n-2} + 4f_{n-1} + f_n\right]
$$

The pattern: odd-indexed interior nodes get weight 4, even-indexed interior nodes get weight 2, both endpoints get weight 1.

> [!WARNING] Count intervals, not points
> Six data points means five intervals, and five is **odd**. Simpson's 1/3 cannot handle that. This is the most common way to lose marks in integration questions.

**Error.** The composite error is:

$$
E = -\frac{(b-a)h^4}{180}f^{(4)}(\xi), \qquad O(h^4)
$$

Halving $h$ cuts the error by a factor of 16. This is much better than the trapezoidal rule's $O(h^2)$.

---

## Worked Example (PYQ 2018): Rocket Distance, Eight Segments

> **Source:** 2018 Q.6(a) [Marks: 08]

**Question.** The vertical distance covered by a rocket from $t = 8$ to $t = 30$ seconds is given by:

$$
x = \int_8^{30} \left( 2000 \ln \left[ \frac{140000}{140000 - 2100t} \right] - 9.8t \right) dt
$$

(i) Use eight-segment Simpson's $\frac{1}{3}$ rule to find the distance covered.
(ii) Find the true error of part (i).
(iii) Find the absolute relative error for part (i).

> [!warning] 2023 asks the same integral with a different instruction
> 2023 Q.4(b) prints the same integral but says only "use Simpson's $\frac{1}{3}$ rule",
> with no segment count. It is answered with the **single-application** rule, $n = 2$,
> which gives a completely different answer. That version is worked in full in its own
> Golden Question below. Read the segment count before you start.

**Full Answer:**

**(i) Eight-segment Simpson's 1/3 rule.** With $n = 8$, $h = \frac{30 - 8}{8} = 2.75$, the nodes are $t = 8, 10.75, 13.5, 16.25, 19, 21.75, 24.5, 27.25, 30$.

Eight is even, so the rule applies directly.

Evaluate $f(t) = 2000\ln\left[\frac{140000}{140000 - 2100t}\right] - 9.8t$ at each node:

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

Group the weighted sums:

$$
f_1 + f_3 + f_5 + f_7 = 246.3351814 + 399.5165393 + 576.6423135 + 783.9826784 = 2006.4767126
$$

$$
f_2 + f_4 + f_6 = 320.2468886 + 484.7454726 + 676.0501168 = 1481.0424780
$$

$$
x \approx \frac{2.75}{3}\left[177.2667430 + 901.6740015 + 4(2006.4767126) + 2(1481.0424780)\right]
$$

$$
= \frac{2.75}{3}\left[177.2667430 + 901.6740015 + 8025.9068504 + 2962.0849560\right] = \frac{2.75}{3}(12066.9325509)
$$

$$
\boxed{x \approx 11061.3548\ \text{m}}
$$

**(ii) The true error.** The exact value of the integral is $x_{\text{exact}} = 11061.3355$ m.

$$
E_t = x_{\text{exact}} - x \approx 11061.3355 - 11061.3548 = -0.0193\ \text{m}
$$

$$
\boxed{E_t \approx -0.0193\ \text{m}}
$$

The negative sign means the Simpson estimate is above the true distance.

**(iii) The absolute relative error.**

$$
|\varepsilon_t| = \left|\frac{\text{true error}}{\text{true value}}\right| \times 100\% = \left|\frac{-0.0193}{11061.3355}\right|\times 100\%
$$

$$
\boxed{|\varepsilon_t| \approx 0.00017\%}
$$

> [!NOTE] The $O(h^4)$ convergence is visible in the data
> Repeating with 16 segments gives $x = 11061.3368$, and 32 segments gives $11061.3356$. The errors are $1.93 \times 10^{-2}$, $1.22 \times 10^{-3}$, and $7.6 \times 10^{-5}$. Each halving of $h$ divides the error by 16, which is the signature of $O(h^4)$.

---

## 🏆 Golden Questions (Past Exam Archive)

### 🎯 Derive Simpson's one-third rule and show it is exact up to degree three.
> **Appeared:** 2019 Q.7(a) — (04 marks)

**Full Answer:**

Take three equally spaced nodes $x_0$, $x_1 = x_0 + h$, $x_2 = x_0 + 2h$. Replace $f$ by the quadratic $P_2(x)$ through the three values $f_0, f_1, f_2$. Integrate $P_2$.

With $x = x_0 + ph$, $dx = h\,dp$, the Lagrange basis is:

$$
L_0 = \frac{(p-1)(p-2)}{2}, \qquad L_1 = -p(p-2), \qquad L_2 = \frac{p(p-1)}{2}
$$

Integrating each basis function from $0$ to $2$:

$$
\int_0^2 \frac{(p-1)(p-2)}{2}\,dp = \frac{1}{3}, \qquad \int_0^2 -p(p-2)\,dp = \frac{4}{3}, \qquad \int_0^2 \frac{p(p-1)}{2}\,dp = \frac{1}{3}
$$

Hence:

$$
\int_{x_0}^{x_2} f(x)\,dx \approx \frac{h}{3}(f_0 + 4f_1 + f_2)
$$

The composite form over $[a, b]$ with $n$ even:

$$
\int_a^b f(x)\,dx \approx \frac{h}{3}\left[f_0 + 4f_1 + 2f_2 + 4f_3 + \cdots + 2f_{n-2} + 4f_{n-1} + f_n\right]
$$

**Exactness to degree 3.** By construction, the rule is exact for degree $\le 2$. For cubic, test $f(x) = x^3$ on $[-h, h]$:

$$
\int_{-h}^{h} x^3\,dx = 0, \qquad \frac{h}{3}[(-h)^3 + 4(0)^3 + h^3] = 0
$$

Both agree. The cubic part is antisymmetric about the midpoint, and both the true integral and the weighted sum annihilate it.

**Failure at degree 4.** For $f(x) = x^4$: exact integral gives $\frac{2h^5}{5}$, rule gives $\frac{2h^5}{3}$. These differ, so the rule is not exact for quartics.

$$
\boxed{\int_{x_0}^{x_2} f\,dx \approx \frac{h}{3}(f_0 + 4f_1 + f_2)\ \text{exact for all polynomials of degree}\ \le 3}
$$

---

### 🎯 Op-amp integrator: find $v_0$ at $t = 1.25$ using Simpson's 1/3 rule.
> **Appeared:** 2020 Q.6(b) — (05 marks)

**Full Answer:**

The circuit equation is $v_0 = -\frac{1}{RC}\int_0^t v_i(t)\,dt$ with $R = 10$ k$\Omega$, $C = 1\ \mu$F.

| $t$ | 0 | 0.25 | 0.50 | 0.75 | 1.00 | 1.25 |
| --- | --: | --: | --: | --: | --: | --: |
| $v_i(t)$ | 1 | 0.9793 | 0.9195 | 0.8261 | 0.7081 | 0.6201 |

> [!WARNING] Six points = five intervals, and five is odd
> Simpson's 1/3 rule needs an **even** number of intervals. It cannot be applied to all five intervals at once. The fix: apply Simpson's 1/3 to the first four intervals ($t = 0$ to $1.00$) and the trapezoid rule to the last interval ($t = 1.00$ to $1.25$).

**Step 1. The constant.**

$$
RC = (10 \times 10^3)(1 \times 10^{-6}) = 10^{-2}\ \text{s}, \qquad \frac{1}{RC} = 100\ \text{s}^{-1}
$$

**Step 2. Simpson's 1/3 on $0$ to $1.00$** (4 intervals, $h = 0.25$):

$$
I_{1/3} = \frac{0.25}{3}\left[1 + 4(0.9793) + 2(0.9195) + 4(0.8261) + 0.7081\right]
$$

$$
= \frac{0.25}{3}\left[1 + 3.9172 + 1.8390 + 3.3044 + 0.7081\right] = \frac{0.25}{3}(10.7687) = 0.89739167
$$

**Step 3. Trapezoid on $1.00$ to $1.25$:**

$$
I_T = \frac{0.25}{2}(0.7081 + 0.6201) = 0.125(1.3282) = 0.166025
$$

**Step 4. Total integral:**

$$
I = 0.89739167 + 0.166025 = 1.06341667
$$

**Step 5. The output voltage.** The leading minus sign comes from the inverting amplifier:

$$
v_0 = -\frac{1}{RC}\,I = -100(1.06341667) = -106.341667
$$

$$
\boxed{v_0(1.25) = -106.34 \text{ V}}
$$

> [!TIP] Three things to get right
> 1. **The sign**: $v_0$ is negative. Dropping the minus is the most common slip.
> 2. **The units**: $\frac{1}{RC} = 100$, not $0.01$. Check: $10^4 \times 10^{-6} = 10^{-2}$ s.
> 3. **Interval count**: six points means five intervals. Five is odd. Must mix rules.

---

## 🏆 Golden Question: Rocket Distance, Single Application (PYQ 2023)

### 🎯 The distance covered by a rocket from $t = 8$ to $t = 30$ is given by $x = \int_8^{30}\left(2000\ln\left[\frac{140000}{140000 - 2100t}\right] - 9.8t\right)dt$. (i) Use Simpson's $\frac{1}{3}$ rule to find the approximate value of $x$, (ii) find the true error $E_t$, (iii) find the absolute relative true error $|\epsilon_t|$.
> **Appeared:** 2023 Q.4(b) — (05 marks)

**Full Answer:**

The integrand is the velocity function:

$$
f(t) = 2000\ln\left(\frac{140000}{140000 - 2100t}\right) - 9.8t
$$

The limits are $a = 8\text{ s}$ and $b = 30\text{ s}$, so the total interval width is $b - a = 22\text{ s}$.

**Why $n = 2$ and not $n = 8$.** The question prints no segment count. When a paper says only
"Simpson's $\frac{1}{3}$ rule" with no subdivision, it means the **fundamental two-segment
rule**, the one derived in the theory section. Composite application is a refinement that has
to be asked for by name, as 2018 Q.6(a) did when it said "eight-segment". State the choice in
the first line of the answer so the examiner can see the assumption was deliberate.

**Step 1. Grid setup ($n = 2$, $h = 11$).**

$$
h = \frac{b - a}{2} = \frac{30 - 8}{2} = 11\text{ s}
$$

The three evaluation nodes are $t_0 = 8$, $t_1 = 19$, $t_2 = 30$:

- $f(t_0) = f(8) = 2000\ln\left(\frac{140000}{140000 - 2100(8)}\right) - 9.8(8) = 177.2667\text{ m/s}$
- $f(t_1) = f(19) = 2000\ln\left(\frac{140000}{140000 - 2100(19)}\right) - 9.8(19) = 484.7455\text{ m/s}$
- $f(t_2) = f(30) = 2000\ln\left(\frac{140000}{140000 - 2100(30)}\right) - 9.8(30) = 901.6740\text{ m/s}$

**Step 2. The approximate distance $x$.**

$$
\begin{aligned}
x &\approx \frac{h}{3}\left[f(t_0) + 4f(t_1) + f(t_2)\right] \\
  &= \frac{11}{3}\left[177.2667 + 4(484.7455) + 901.6740\right] \\
  &= \frac{11}{3}\left[177.2667 + 1938.9820 + 901.6740\right] \\
  &= \frac{11}{3}[3017.9227] = 11065.7166\text{ m}
\end{aligned}
$$

$$
\boxed{\text{(i) } x \approx 11065.72\text{ m}}
$$

**Step 3. The exact value and the two errors.**

The exact analytical integral, by integration by parts using
$\int \ln(A - kt)dt = t\ln(A-kt) - t - \frac{A}{k}\ln(A-kt)$:

$$
I_{exact} = \int_8^{30} f(t)\,dt = 11061.34\text{ m}
$$

The true error:

$$
E_t = I_{exact} - x = 11061.34 - 11065.72 = -4.38\text{ m}
$$

$$
\boxed{\text{(ii) } E_t = -4.38\text{ m}}
$$

The negative sign says Simpson's rule overestimated the true distance.

The absolute relative true error:

$$
|\epsilon_t| = \left|\frac{E_t}{I_{exact}}\right| \times 100\% = \left|\frac{-4.38}{11061.34}\right| \times 100\% = 0.0396\%
$$

$$
\boxed{\text{(iii) } |\epsilon_t| = 0.0396\%}
$$

> [!note] The same integral, two answers, both defensible
> 2018 Q.6(a) and 2023 Q.4(b) print the **same integral**. The answers differ because the
> instruction differs, not because either is wrong.
>
> | | 2018 Q.6(a) | 2023 Q.4(b) |
> | :-- | :-- | :-- |
> | Segments | eight, $n = 8$, $h = 2.75$ | two, $n = 2$, $h = 11$ |
> | $x$ | $11061.3548$ m | $11065.72$ m |
> | $E_t$ | $-0.0193$ m | $-4.38$ m |
> | $|\epsilon_t|$ | $0.00017\%$ | $0.0396\%$ |
>
> The 2023 error is about 227 times larger, which is exactly what eight extra segments are
> worth. Always transcribe the segment count from the question. It is the one instruction
> that decides the answer.

---

## Exam Variants

| Year | Question | Data | Key Answer |
| :--- | :--- | :--- | :--- |
| 2018 Q.6(a) | Rocket distance, 8-segment Simpson's 1/3 | $t = 8$ to $30$, $n = 8$ | $\boxed{x \approx 11061.3548\ \text{m}}$ |
| 2019 Q.7(a) | Derive Simpson's 1/3, show exact to degree 3 | Theory | $\boxed{\int_{x_0}^{x_2} f\,dx \approx \frac{h}{3}(f_0 + 4f_1 + f_2)\ \text{exact for all polynomials of degree}\ \le 3}$ |
| 2023 Q.4(b)(ii) | Rocket distance, true error | $n = 2$ | $\boxed{\text{(ii) } E_t = -4.38\text{ m}}$ |
| 2023 Q.4(b)(iii) | Rocket distance, relative error | $n = 2$ | $\boxed{\text{(iii) } |\epsilon_t| = 0.0396\%}$ |
| 2020 Q.6(b) | Op-amp integrator, mixed Simpson + trapezoid | 6 data points | $\boxed{v_0(1.25) = -106.34 \text{ V}}$ |
| 2018 Q.6(a) | Rocket distance, eight-segment composite | $t = 8$ to $30$, $n = 8$ | $\boxed{x \approx 11061.3548\ \text{m}}$ |
| 2023 Q.4(b) | Rocket distance, single application | $t = 8$ to $30$, $n = 2$, $h = 11$ | $\boxed{\text{(i) } x \approx 11065.72\text{ m}}$ |

---

## ⚡ Exam Tips & Common Mistakes

1. **Count intervals, not points.** Six data points = five intervals. Simpson's 1/3 needs an even count. If odd, mix with trapezoid or 3/8 for the leftover.
2. **Weight pattern is 1, 4, 2, 4, 2, ..., 4, 1.** Odd-indexed interior nodes get 4, even-indexed get 2. Swapping them gives the wrong answer.
3. **Do not forget the minus sign** in the op-amp integrator problem. The relation $v_0 = -\frac{1}{RC}\int v_i\,dt$ has a leading negative.
4. **Check $1/RC$ units carefully.** $10$ k$\Omega \times 1\ \mu$F $= 10^4 \times 10^{-6} = 10^{-2}$ s, so $1/RC = 100$.
5. **The rule is $O(h^4)$, not $O(h^2)$.** Halving $h$ cuts the error by 16, not by 4.

## 🔗 Related Topics

- [NM-5.4: Rule Comparison](NM-5.4_Rule_Comparison_and_Step_Constraints.md) — Simpson's 1/3 vs. 3/8 constraints and accuracy
- [NM-5 Lower: Trapezoidal, 3/8, Romberg](NM-5_Lower_Trapezoidal_38_Romberg_Error_Applied.md) — trapezoidal rule, Simpson's 3/8, Romberg integration, error analysis
- [NM-6: Optimization](NM-6_Optimization.md) — finding optima of functions and tabulated data

---

[← Previous: NM-4 Lower — Regression & Interpolation](NM-4_Lower_Regression_Theory_Interpolation_Methods.md) | [🏠 Index](00_Index.md) | [Next: NM-5.4 Rule Comparison →](NM-5.4_Rule_Comparison_and_Step_Constraints.md)
