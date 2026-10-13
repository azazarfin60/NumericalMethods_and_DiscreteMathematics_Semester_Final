[← Previous: NM-5.1 Trapezoidal Rule](NM-5.1_Trapezoidal_Rule.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: NM-5.3 Simpson's 3/8 Rule →](NM-5.3_Simpsons_Three_Eighth.md)

---

# NM-5.2: Simpson's One-Third Rule

> 🔴 **Priority:** Critical | **Tested:** 4/8 years (2018, 2019, 2020, 2023) | **Typical marks:** 4 to 8

## What This Is (and Why It Matters)

While the trapezoidal rule connects points with rigid straight lines, Simpson's 1/3 rule curves with the data. It takes data points in groups of three and passes a smooth parabola through them. Integrating parabolas instead of chords gives an enormous leap in accuracy.

Even better: by a stroke of mathematical symmetry, a parabola fitted through three symmetric points actually integrates cubic polynomials with zero error.

In RUET exams, Simpson's 1/3 rule is the undisputed heavyweight of numerical integration. You will see it in four recurring formats:
1. **Derivation and exactness proof:** Deriving the weights and proving it is exact up to degree three (2019 Q.7(a)).
2. **Rocket distance problem (composite):** Evaluating an 8-segment flight integral and calculating true error and relative percentage error (2018 Q.6(a)).
3. **Rocket distance problem (single application):** Applying the fundamental 2-segment rule when no segment count is specified (2023 Q.4(b)).
4. **Analog op-amp integrator circuit:** Calculating output voltage from sampled laboratory readings when the number of intervals is odd, forcing a mixed rule (2020 Q.6(b)).

---

## 📝 Key Definitions

> **Newton-Cotes Quadrature:** "A family of numerical integration formulas of the type $I_n = \sum_{i=0}^n C_i y_i$ where the interpolation points are equally spaced: $x_i = x_0 + i h$." -- Jain, §6.4.7
>
> **In simple words:** Formulas that estimate the area under a curve by passing an interpolating polynomial through evenly spaced data points and integrating that polynomial exactly.

> **Simpson's 1/3 Rule (Single Panel):** "This rule is obtained by replacing the curve by arcs of second-degree polynomials or parabolas: $\int_{x_0}^{x_2} y\,dx = \frac{h}{3}(y_0 + 4y_1 + y_2)$." -- Jain, §6.4.2
>
> **In simple words:** You take 3 equally spaced points spanning 2 intervals of width $h$, fit a parabola through them, and find its exact area. The formula multiplies the middle height by 4 and the outer heights by 1, with a prefactor of $\frac{h}{3}$.

> **Composite Simpson's 1/3 Rule:** "Summing up over $n$ intervals ($n$ even), we obtain $\int_{x_0}^{x_n} y\,dx = \frac{h}{3}[y_0 + 4(y_1 + y_3 + \cdots + y_{n-1}) + 2(y_2 + y_4 + \cdots + y_{n-2}) + y_n]$." -- Jain, §6.4.2
>
> **In simple words:** When you have many intervals, you pair them up. Odd-indexed interior points sit in the middle of a parabola and get weight 4. Even-indexed interior points connect two neighboring parabolas and get weight 2. The endpoints get weight 1.

> **Order of Accuracy & Truncation Error:** "The composite error is given by $E = -\frac{b - a}{180}h^4 y^{\text{iv}}(\bar{x})$, where $y^{\text{iv}}(\bar{x})$ is the largest value of the fourth derivatives." -- Jain, §6.4.2
>
> **In simple words:** Simpson's 1/3 rule is fourth-order ($O(h^4)$). If you halve your step size $h$, the error is divided by $2^4 = 16$. It is 16 times more accurate with half the step size.

---

## The Core Idea

### Derivation from Lagrange Quadratic Interpolation

Let us take three equally spaced nodes:

$$
x_0, \qquad x_1 = x_0 + h, \qquad x_2 = x_0 + 2h
$$

We replace $f(x)$ with the unique quadratic interpolating polynomial $P_2(x)$ passing through $(x_0, f_0)$, $(x_1, f_1)$, and $(x_2, f_2)$. 

We make the convenient change of variable $x = x_0 + ph$, where $p$ varies from $0$ to $2$, and $dx = h\,dp$. The Lagrange basis polynomials in terms of $p$ are:

$$
L_0(p) = \frac{(p - 1)(p - 2)}{(0 - 1)(0 - 2)} = \frac{(p - 1)(p - 2)}{2}
$$

$$
L_1(p) = \frac{(p - 0)(p - 2)}{(1 - 0)(1 - 2)} = -p(p - 2)
$$

$$
L_2(p) = \frac{(p - 0)(p - 1)}{(2 - 0)(2 - 1)} = \frac{p(p - 1)}{2}
$$

Now we integrate each basis polynomial from $p = 0$ to $p = 2$:

$$
\int_0^2 \frac{(p - 1)(p - 2)}{2}\,dp = \frac{1}{2}\int_0^2 (p^2 - 3p + 2)\,dp = \frac{1}{2}\left[\frac{8}{3} - 6 + 4\right] = \frac{1}{2}\cdot\frac{2}{3} = \frac{1}{3}
$$

$$
\int_0^2 -p(p - 2)\,dp = -\int_0^2 (p^2 - 2p)\,dp = -\left[\frac{8}{3} - 4\right] = \frac{4}{3}
$$

$$
\int_0^2 \frac{p(p - 1)}{2}\,dp = \frac{1}{2}\int_0^2 (p^2 - p)\,dp = \frac{1}{2}\left[\frac{8}{3} - 2\right] = \frac{1}{2}\cdot\frac{2}{3} = \frac{1}{3}
$$

Multiplying by $h$ and collecting:

$$
\int_{x_0}^{x_2} f(x)\,dx \approx h\left[\frac{1}{3}f_0 + \frac{4}{3}f_1 + \frac{1}{3}f_2\right] = \frac{h}{3}(f_0 + 4f_1 + f_2)
$$

This is Simpson's one-third rule.

---

### The Symmetry Miracle: Exactness up to Degree 3

Because we fitted a quadratic polynomial, the rule is guaranteed to be exact for polynomials of degree 0, 1, and 2. 

What happens for a cubic polynomial, $f(x) = x^3$? 
Let us test it on the symmetric interval $[-h, h]$ where $x_0 = -h$, $x_1 = 0$, $x_2 = h$:

**True analytical integral:**

$$
\int_{-h}^{h} x^3\,dx = \left[\frac{x^4}{4}\right]_{-h}^h = \frac{h^4}{4} - \frac{h^4}{4} = 0
$$

**Simpson's 1/3 evaluation:**

$$
\frac{h}{3}[f(-h) + 4f(0) + f(h)] = \frac{h}{3}[(-h)^3 + 4(0)^3 + h^3] = \frac{h}{3}[-h^3 + h^3] = 0
$$

Both equal zero exactly. Because a cubic is an odd, antisymmetric function about the midpoint, the true integral vanishes, and the symmetric weights $1, 4, 1$ annihilate it completely. 

**Does this continue to degree 4?**
Let us test $f(x) = x^4$ on $[-h, h]$:

$$
\int_{-h}^h x^4\,dx = \left[\frac{x^5}{5}\right]_{-h}^h = \frac{2h^5}{5}
$$

$$
\frac{h}{3}[f(-h) + 4f(0) + f(h)] = \frac{h}{3}[h^4 + 0 + h^4] = \frac{2h^5}{3}
$$

Since $\frac{2}{5} \ne \frac{2}{3}$, the rule fails for quartics. Therefore, Simpson's 1/3 rule is **exact for all polynomials of degree $\le 3$**.

---

### The Subinterval Constraint: $n$ Must Be Even

Each panel of Simpson's 1/3 rule requires 2 subintervals (3 data points). Therefore:
- The total number of subintervals $n$ **must be an even integer** ($n = 2, 4, 6, 8, \dots$).
- The total number of data points $N$ must be **odd** ($N = n + 1 = 3, 5, 7, 9, \dots$).

The composite formula with weights $1, 4, 2, 4, 2, \dots, 2, 4, 1$ is:

$$
\int_a^b f(x)\,dx \approx \frac{h}{3}\left[f_0 + 4(f_1 + f_3 + \cdots + f_{n-1}) + 2(f_2 + f_4 + \cdots + f_{n-2}) + f_n\right]
$$

> [!WARNING] The Count Trap: Points vs Subintervals
> If an exam table provides 6 data points, that means there are $6 - 1 = 5$ subintervals. Five is **odd**. You **cannot** apply Simpson's 1/3 rule across all five intervals at once. If you do, your weights will fail at the end. You must apply Simpson's 1/3 to 4 intervals and use the trapezoidal rule (or Simpson's 3/8) for the leftover interval.

---

## 🔧 Worked Example

> **From:** 2018 Q.6(a) [Marks: 08]

**The question:** The vertical distance covered by a rocket from $t = 8$ to $t = 30$ seconds is given by:

$$
x = \int_8^{30} \left( 2000 \ln \left[ \frac{140000}{140000 - 2100t} \right] - 9.8t \right) dt
$$

(i) Use eight-segment Simpson's $\frac{1}{3}$ rule to find the distance covered.  
(ii) Find the true error of part (i).  
(iii) Find the absolute relative error for part (i).

**Let us solve this step by step.**

**Step 1. Grid setup.**
The integration limits are $a = 8\text{ s}$ and $b = 30\text{ s}$. With $n = 8$ segments:

$$
h = \frac{b - a}{n} = \frac{30 - 8}{8} = \frac{22}{8} = 2.75\text{ s}
$$

Since $n = 8$ is an even number, composite Simpson's 1/3 rule applies directly.

**Step 2. Compute function values at all 9 nodes.**
The velocity integrand is:

$$
f(t) = 2000\ln\left[\frac{140000}{140000 - 2100t}\right] - 9.8t
$$

Evaluating at each node $t_i = 8 + i(2.75)$:

| $i$ | $t_i$ | $f(t_i)$ | Simpson Weight | Weighted Product |
|:---:|:---:|:---|:---:|:---|
| 0 | 8.00 | 177.2667430 | 1 | 177.2667430 |
| 1 | 10.75 | 246.3351814 | 4 | 985.3407256 |
| 2 | 13.50 | 320.2468886 | 2 | 640.4937772 |
| 3 | 16.25 | 399.5165393 | 4 | 1598.0661572 |
| 4 | 19.00 | 484.7454726 | 2 | 969.4909452 |
| 5 | 21.75 | 576.6423135 | 4 | 2306.5692540 |
| 6 | 24.50 | 676.0501168 | 2 | 1352.1002336 |
| 7 | 27.25 | 783.9826784 | 4 | 3135.9307136 |
| 8 | 30.00 | 901.6740015 | 1 | 901.6740015 |

**Step 3. Sum the odd and even interior ordinates.**

$$
\sum_{\text{odd}} = f_1 + f_3 + f_5 + f_7 = 246.3351814 + 399.5165393 + 576.6423135 + 783.9826784 = 2006.4767126
$$

$$
\sum_{\text{even interior}} = f_2 + f_4 + f_6 = 320.2468886 + 484.7454726 + 676.0501168 = 1481.0424780
$$

The weighted groupings are:

$$
4\sum_{\text{odd}} = 4(2006.4767126) = 8025.9068504
$$

$$
2\sum_{\text{even}} = 2(1481.0424780) = 2962.0849560
$$

**Step 4. Calculate the distance $x$.**

$$
x \approx \frac{h}{3}\left[f_0 + f_8 + 4\sum_{\text{odd}} + 2\sum_{\text{even}}\right]
$$

$$
= \frac{2.75}{3}[177.2667430 + 901.6740015 + 8025.9068504 + 2962.0849560]
$$

$$
= \frac{2.75}{3}[12066.9325509] \approx 11061.3548\text{ m}
$$

$$
\boxed{x \approx 11061.3548\ \text{m}}
$$

**Step 5. Compute the true error $E_t$.**
The exact analytical integral (computed via integration by parts) is:

$$
x_{\text{exact}} = 11061.3355\text{ m}
$$

The true error is exact minus approximate:

$$
E_t = x_{\text{exact}} - x \approx 11061.3355 - 11061.3548 = -0.0193\text{ m}
$$

$$
\boxed{E_t \approx -0.0193\ \text{m}}
$$

*(The negative sign indicates that Simpson's rule slightly overestimated the true distance).*

**Step 6. Compute the absolute relative true error $|\varepsilon_t|$.**

$$
|\varepsilon_t| = \left|\frac{\text{true error}}{\text{true value}}\right| \times 100\% = \left|\frac{-0.0193}{11061.3355}\right| \times 100\% \approx 0.00017\%
$$

$$
\boxed{|\varepsilon_t| \approx 0.00017\%}
$$

---

## 🏆 Past Exam Questions

### 2019 Q.7(a): Derive Simpson's 1/3 Rule and Prove Exactness to Degree 3 [04 marks]

**Question.** Derive Simpson's one-third rule and hence show that the rule is exact up to degree three.

**Solution.**

**Derivation:**
Consider three equally spaced nodes $x_0, x_1 = x_0 + h, x_2 = x_0 + 2h$.
Let $f(x)$ be approximated by the quadratic interpolating polynomial $P_2(x)$ through $(x_0, f_0), (x_1, f_1), (x_2, f_2)$.

Setting $x = x_0 + ph$, so $dx = h\,dp$, the interval $[x_0, x_2]$ maps to $p \in [0, 2]$. The Lagrange basis polynomials are:

$$
L_0(p) = \frac{(p - 1)(p - 2)}{2}, \qquad L_1(p) = -p(p - 2), \qquad L_2(p) = \frac{p(p - 1)}{2}
$$

Integrating each basis function over $[0, 2]$:

$$
\int_0^2 \frac{(p - 1)(p - 2)}{2}\,dp = \frac{1}{2}\int_0^2 (p^2 - 3p + 2)\,dp = \frac{1}{2}\left[\frac{8}{3} - 6 + 4\right] = \frac{1}{3}
$$

$$
\int_0^2 -p(p - 2)\,dp = -\int_0^2 (p^2 - 2p)\,dp = -\left[\frac{8}{3} - 4\right] = \frac{4}{3}
$$

$$
\int_0^2 \frac{p(p - 1)}{2}\,dp = \frac{1}{2}\int_0^2 (p^2 - p)\,dp = \frac{1}{2}\left[\frac{8}{3} - 2\right] = \frac{1}{3}
$$

Hence:

$$
\int_{x_0}^{x_2} f(x)\,dx \approx h\left[\frac{1}{3}f_0 + \frac{4}{3}f_1 + \frac{1}{3}f_2\right] = \frac{h}{3}(f_0 + 4f_1 + f_2)
$$

Summing over $n$ subintervals ($n$ even) yields the composite form:

$$
\int_a^b f(x)\,dx \approx \frac{h}{3}\left[f_0 + 4(f_1 + f_3 + \cdots + f_{n-1}) + 2(f_2 + f_4 + \cdots + f_{n-2}) + f_n\right]
$$

**Proof of exactness to degree 3:**
By construction, the rule is exact for any quadratic function (degree $\le 2$).
For a cubic polynomial, test $f(x) = x^3$ on $[-h, h]$:

$$
\int_{-h}^h x^3\,dx = \left[\frac{x^4}{4}\right]_{-h}^h = 0
$$

$$
\frac{h}{3}[f(-h) + 4f(0) + f(h)] = \frac{h}{3}[(-h)^3 + 4(0)^3 + h^3] = 0
$$

Both results agree identically. Since $x^3$ is antisymmetric about the origin, both the true integral and the weighted sum evaluate to zero. Therefore, Simpson's 1/3 rule is exact for $1, x, x^2, x^3$.

**Failure at degree 4:**
For $f(x) = x^4$ on $[-h, h]$:

$$
\int_{-h}^h x^4\,dx = \frac{2h^5}{5}, \qquad \frac{h}{3}[h^4 + 0 + h^4] = \frac{2h^5}{3}
$$

Since $\frac{2}{3} \ne \frac{2}{5}$, the rule fails for quartics.

$$
\boxed{\int_{x_0}^{x_2} f\,dx \approx \frac{h}{3}(f_0 + 4f_1 + f_2)\ \text{exact for all polynomials of degree}\ \le 3}
$$

---

### 2020 Q.6(b): Op-Amp Integrator with Odd Number of Intervals [05 marks]

**Question.** A circuit is giving following output voltage equation:

$$
v_0 = -\frac{1}{RC} \int_0^t v_i(t)\,dt
$$

where $R = 10\text{ k}\Omega, C = 1\ \mu\text{F}$. Use Simpson's $1/3^{\text{rd}}$ rule to find $v_0$ at $t = 1.25$.

| $t$ | 0 | 0.25 | 0.50 | 0.75 | 1.00 | 1.25 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| $v_i(t)$ | 1 | 0.9793 | 0.9195 | 0.8261 | 0.7081 | 0.6201 |

**Solution.**

**Step 1. Identify the odd interval constraint.**
There are 6 data points, which means there are $6 - 1 = 5$ subintervals of width $h = 0.25\text{ s}$. 
Five is an **odd** number. Simpson's 1/3 rule cannot be applied across all five subintervals in one piece.

**The standard repair:** Apply Simpson's 1/3 rule to the largest even block of subintervals (4 subintervals, from $t = 0$ to $t = 1.00$), and use the trapezoidal rule on the leftover single subinterval (from $t = 1.00$ to $t = 1.25$).

**Step 2. Compute the circuit constant $\frac{1}{RC}$.**

$$
R C = (10 \times 10^3\,\Omega)(1 \times 10^{-6}\,\text{F}) = 10^{-2}\text{ s} = 0.01\text{ s}
$$

$$
\frac{1}{RC} = \frac{1}{0.01} = 100\text{ s}^{-1}
$$

**Step 3. Compute Simpson's 1/3 integral on $[0, 1.00]$.**
Here $n = 4$, $h = 0.25$, with weights $1, 4, 2, 4, 1$:

$$
I_{1/3} = \frac{h}{3}[v_0 + 4v_1 + 2v_2 + 4v_3 + v_4]
$$

$$
= \frac{0.25}{3}[1 + 4(0.9793) + 2(0.9195) + 4(0.8261) + 0.7081]
$$

$$
= \frac{0.25}{3}[1 + 3.9172 + 1.8390 + 3.3044 + 0.7081] = \frac{0.25}{3}(10.7687) \approx 0.89739167
$$

**Step 4. Compute Trapezoidal integral on $[1.00, 1.25]$.**
Here $h = 0.25$ over one panel:

$$
I_T = \frac{h}{2}(v_4 + v_5) = \frac{0.25}{2}(0.7081 + 0.6201) = 0.125(1.3282) = 0.166025
$$

**Step 5. Sum the integrals.**

$$
I_{\text{total}} = I_{1/3} + I_T = 0.89739167 + 0.166025 = 1.06341667\text{ V}\cdot\text{s}
$$

**Step 6. Calculate the output voltage $v_0(1.25)$.**
Carrying the leading minus sign from the inverting op-amp:

$$
v_0(1.25) = -\frac{1}{RC} I_{\text{total}} = -100(1.06341667) = -106.341667\text{ V}
$$

$$
\boxed{v_0(1.25) = -106.34 \text{ V}}
$$

> [!TIP] Three Critical Traps to Avoid
> 1. **Do not drop the minus sign:** The circuit is an inverting op-amp integrator. The final voltage must be negative.
> 2. **Check the units:** $RC = 10^4 \times 10^{-6} = 10^{-2}\text{ s}$, so $1/RC = 100$, not $0.01$.
> 3. **Never apply Simpson's 1/3 blindly across 5 intervals:** That produces $-100.8\text{ V}$ and loses major marks.

---

### 2023 Q.4(b): Rocket Distance, Single Application [05 marks]

**Question.** The distance covered by a rocket from $t = 8$ to $t = 30$ is given by:

$$
x = \int_8^{30}\left(2000\ln\left[\frac{140000}{140000 - 2100t}\right] - 9.8t\right)dt
$$

(i) Use Simpson's $\frac{1}{3}$ rule to find the approximate value of $x$.  
(ii) Find the true error $E_t$.  
(iii) Find the absolute relative true error $|\epsilon_t|$.

**Solution.**

Notice that unlike 2018 Q.6(a), this question does not specify a segment count like "eight segments". In standard numerical analysis, when an exam asks for Simpson's 1/3 rule with no segment count given, it expects the fundamental single application ($n = 2$ segments).

**Step 1. Grid setup ($n = 2$).**
The limits are $a = 8\text{ s}$ and $b = 30\text{ s}$. With $n = 2$:

$$
h = \frac{30 - 8}{2} = 11\text{ s}
$$

The three nodes are $t_0 = 8$, $t_1 = 19$, and $t_2 = 30$:
- $f(t_0) = f(8) = 2000\ln\left(\frac{140000}{140000 - 2100(8)}\right) - 9.8(8) = 177.2667\text{ m/s}$
- $f(t_1) = f(19) = 2000\ln\left(\frac{140000}{140000 - 2100(19)}\right) - 9.8(19) = 484.7455\text{ m/s}$
- $f(t_2) = f(30) = 2000\ln\left(\frac{140000}{140000 - 2100(30)}\right) - 9.8(30) = 901.6740\text{ m/s}$

**Step 2. Compute approximate distance $x$.**

$$
x \approx \frac{h}{3}[f(t_0) + 4f(t_1) + f(t_2)]
$$

$$
= \frac{11}{3}[177.2667 + 4(484.7455) + 901.6740]
$$

$$
= \frac{11}{3}[177.2667 + 1938.9820 + 901.6740] = \frac{11}{3}[3017.9227] \approx 11065.72\text{ m}
$$

$$
\boxed{\text{(i) } x \approx 11065.72\text{ m}}
$$

**Step 3. Compute true error and relative error.**
The exact analytical integral is $I_{\text{exact}} = 11061.34\text{ m}$.

- **True error:**
  $$
  E_t = I_{\text{exact}} - x = 11061.34 - 11065.72 = -4.38\text{ m}
  $$
  $$
  \boxed{\text{(ii) } E_t = -4.38\text{ m}}
  $$

- **Absolute relative true error:**
  $$
  |\epsilon_t| = \left|\frac{E_t}{I_{\text{exact}}}\right| \times 100\% = \left|\frac{-4.38}{11061.34}\right| \times 100\% \approx 0.0396\%
  $$
  $$
  \boxed{\text{(iii) } |\epsilon_t| = 0.0396\%}
  $$

*(Notice the comparison: at $n = 2$, error is $-4.38\text{ m}$ ($0.0396\%$). At $n = 8$, error dropped to $-0.0193\text{ m}$ ($0.00017\%$), a 227-fold improvement).*

---

### Exam Variants at a Glance

| Year | What They Asked | Key Method | Key Answer |
|:---|:---|:---|:---|
| 2018 Q.6(a) | Rocket distance, 8 segments | Composite Simpson's 1/3 ($n = 8$) | $\boxed{x \approx 11061.3548\ \text{m}}$ |
| 2018 Q.6(a)(ii) | Rocket true error ($n = 8$) | $x_{\text{exact}} - x$ | $\boxed{E_t \approx -0.0193\ \text{m}}$ |
| 2018 Q.6(a)(iii) | Rocket relative error ($n = 8$) | $\lvert E_t / x_{\text{exact}}\rvert \times 100\%$ | $\boxed{\lvert\varepsilon_t\rvert \approx 0.00017\%}$ |
| 2019 Q.7(a) | Derive 1/3 rule & cubic exactness | Lagrange quadratic basis integration | $\boxed{\int_{x_0}^{x_2} f\,dx \approx \frac{h}{3}(f_0 + 4f_1 + f_2)\ \text{exact for all polynomials of degree}\ \le 3}$ |
| 2020 Q.6(b) | Op-amp integrator (5 intervals) | Mixed Simpson 1/3 on 4 + Trapezoid on 1 | $\boxed{v_0(1.25) = -106.34 \text{ V}}$ |
| 2023 Q.4(b)(i) | Rocket distance (single application) | Fundamental Simpson 1/3 ($n = 2$) | $\boxed{\text{(i) } x \approx 11065.72\text{ m}}$ |
| 2023 Q.4(b)(ii) | Rocket true error ($n = 2$) | $I_{\text{exact}} - x$ | $\boxed{\text{(ii) } E_t = -4.38\text{ m}}$ |
| 2023 Q.4(b)(iii) | Rocket relative error ($n = 2$) | $\lvert E_t / I_{\text{exact}}\rvert \times 100\%$ | $\boxed{\text{(iii) } \lvert\epsilon_t\rvert = 0.0396\%}$ |

---

## ⚡ Quick Review

**The method in one sentence:** Replace pairs of strips with parabolas, yielding weights $1, 4, 2, 4, \dots, 4, 1$ with prefactor $\frac{h}{3}$ and fourth-order $O(h^4)$ accuracy.

**The formula you must memorize:**

$$
\int_a^b f(x)\,dx \approx \frac{h}{3}\left[f_0 + 4\sum_{\text{odd}} f_i + 2\sum_{\text{even}} f_i + f_n\right], \qquad E = -\frac{(b - a)h^4}{180}f^{(4)}(\xi)
$$

**The most common exam mistake:** Forgetting that $n$ must be even (odd number of points). If given an odd interval count, you must break the domain into an even block for Simpson's and use trapezoid for the rest.

**Time estimate in exam:** ~10 to 12 minutes for an 8-segment calculation; ~5 minutes for single application.

---

## 🔗 Connected Topics

- [← NM-5.1: Trapezoidal Rule](NM-5.1_Trapezoidal_Rule.md) -- simpler second-order rule that pairs with Simpson's 1/3 on odd intervals.
- [→ NM-5.3: Simpson's 3/8 Rule](NM-5.3_Simpsons_Three_Eighth.md) -- cubic polynomial rule that handles multiples of 3.
- [NM-5.4: Rule Comparison](NM-5.4_Rule_Comparison.md) -- direct comparison between 1/3 and 3/8 rules.
- [NM-5.7: Applied Integration](NM-5.7_Applied_Integration.md) -- physical context and modeling of rocket flight and op-amp circuits.

---

[← Previous: NM-5.1 Trapezoidal Rule](NM-5.1_Trapezoidal_Rule.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: NM-5.3 Simpson's 3/8 Rule →](NM-5.3_Simpsons_Three_Eighth.md)
