[← Previous: NM-5.4 Rule Comparison](NM-5.4_Rule_Comparison_and_Step_Constraints.md) | [🏠 Index](00_Index.md) | [Next: NM-6 Optimization →](NM-6_Optimization.md)

---

# NM-5: Numerical Integration — Trapezoidal, Simpson's 3/8, Romberg, Error & Applied
> **Section:** A (Numerical Methods) | **Priority:** 🟠 (mixed) | **Subtopics:** NM-5.1, NM-5.3, NM-5.5, NM-5.6, NM-5.7
> **Sources:** Jain Ch.6 §6.4–§6.6, Shishir Notes §04 pp.53–72, Raidah Notes p.17

## Why This Topic Matters

The trapezoidal rule and Romberg integration appear together in exam problems. The 2022 paper asks for trapezoidal values at three step sizes then a Romberg table, all in one question worth 4 marks. The 2021 paper asks for the derivation of the composite trapezoidal formula. The 3/8 rule appears once (2019) and the error analysis subtopic feeds into the trapezoidal error-bound problem (2018). Applied integration questions (rocket, op-amp) are filed under NM-5.2 since Simpson's 1/3 is used there.

---

## NM-5.1 — Trapezoidal Rule

### 📝 Definitions for NM-5.1

> **Trapezoidal rule (single panel):** Approximate the integral by replacing the curve with a straight line through the two endpoints. The area of the resulting trapezoid is:

$$
\int_{x_0}^{x_1} f(x)\,dx \approx \frac{h}{2}(f_0 + f_1)
$$

> **Composite trapezoidal rule:** Over $[a, b]$ with $n$ subintervals of width $h = \frac{b-a}{n}$:

$$
\int_a^b f(x)\,dx \approx \frac{h}{2}\left[f_0 + 2f_1 + 2f_2 + \cdots + 2f_{n-1} + f_n\right]
$$

$$
= \frac{h}{2}\left[f(a) + f(b) + 2\sum_{i=1}^{n-1}f_i\right]
$$

### Theory

The trapezoidal rule is the simplest Newton-Cotes formula. It fits a straight line (degree 1 polynomial) through each pair of adjacent data points and integrates the line.

![Trapezoidal rule: strips under the curve](diagrams/nm5_trapezoidal_rule_strips.jpg)

**Why interior nodes get weight 2.** Each interior ordinate $f_i$ belongs to two adjacent trapezoids: one from the left, one from the right. So it gets counted twice. The endpoints $f_0$ and $f_n$ belong to only one trapezoid each and get counted once. That asymmetry is the fingerprint of the trapezoidal rule.

**Error:**

$$
E = -\frac{(b-a)h^2}{12}f''(\xi), \qquad O(h^2)
$$

Halving $h$ cuts the error by 4. The rule is exact for linear functions (degree $\le 1$) and overshoots for curves that are concave up.

### 🏆 Golden Questions for NM-5.1

#### 🎯 Determine $n$ so that the trapezoidal rule approximates $\int_0^1 \sqrt{1 + x^2}\,dx$ with error less than 0.01.
> **Appeared:** 2018 Q.6(b) — (04 marks)

**Full Answer:**

The composite trapezoidal rule has error bound:

$$
|E| \le \frac{(b-a)h^2}{12}\max|f''|
$$

With $f(x) = \sqrt{1 + x^2}$:

$$
f'(x) = \frac{x}{\sqrt{1+x^2}}, \qquad f''(x) = \frac{1}{(1+x^2)^{3/2}}
$$

On $[0, 1]$, the maximum of $|f''|$ is at $x = 0$: $f''(0) = 1$.

With $a = 0$, $b = 1$:

$$
\frac{h^2}{12} < 0.01 \implies h^2 < 0.12 \implies h < 0.3464
$$

$$
n = \frac{b-a}{h} > \frac{1}{0.3464} = 2.8868
$$

$$
\boxed{n = 3}
$$

**Direct check:**

| $n$ | $h$ | Approximation | Error |
| :--: | :--: | :-- | :-- |
| 2 | 0.50 | 1.1625704 | $0.014777$ |
| 3 | 0.3333 | 1.1543499 | $0.006556$ |

At $n = 2$ the error exceeds 0.01, at $n = 3$ it falls below. Confirmed.

---

#### 🎯 Derive the composite trapezoidal formula.
> **Appeared:** 2021 Q.8(a) — (04 marks)

**Full Answer:**

Let $h = \frac{x_n - x_0}{n}$ and $y_i = f(x_i)$ at $x_i = x_0 + ih$.

**Step 1.** On one interval $[x_i, x_{i+1}]$, the trapezoid gives:

$$
\int_{x_i}^{x_{i+1}} y\,dx = \frac{h}{2}(y_i + y_{i+1}) - \frac{h^3}{12}y''(\xi_i) + \cdots
$$

**Step 2.** Sum over all $n$ intervals:

$$
\int_{x_0}^{x_n} y\,dx = \sum_{i=0}^{n-1}\left[\frac{h}{2}(y_i + y_{i+1}) + \text{error}\right]
$$

**Step 3.** Collect interior terms. Every $y_1, y_2, \ldots, y_{n-1}$ appears in two adjacent trapezoids, so each gets factor $\frac{h}{2} \times 2 = h$. Only $y_0$ and $y_n$ appear once, each with factor $\frac{h}{2}$:

$$
\int_{x_0}^{x_n} y\,dx = \frac{h}{2}y_0 + h(y_1 + y_2 + \cdots + y_{n-1}) + \frac{h}{2}y_n - \sum_{i=0}^{n-1}\frac{h^3}{12}y''(\xi_i)
$$

**Step 4.** Factor out $h/2$:

$$
\int_{x_0}^{x_n} y\,dx = \frac{h}{2}\left[y_0 + 2(y_1 + y_2 + \cdots + y_{n-1}) + y_n\right] - \frac{h^3}{12}\sum_{i=0}^{n-1}y''(\xi_i)
$$

**Step 5.** The leading error term simplifies to $O(h^2)$:

$$
E = -\frac{h^2}{12}[y'(x_n) - y'(x_0)] + O(h^4)
$$

$$
\boxed{\int_{x_0}^{x_n} y\,dx = \frac{h}{2}\left[y_0 + 2\sum_{i=1}^{n-1}y_i + y_n\right] + O(h^2)}
$$

---

#### 🎯 Discuss the trapezoidal rule of numerical integration.
> **Appeared:** 2019 Q.6(c) — (03 marks)

**Full Answer:**

The trapezoidal rule approximates $\int_a^b f(x)\,dx$ by replacing the curve with straight lines joining the endpoints of each subinterval. The area under the curve becomes the area of a set of trapezoids.

**Single panel:** Over $[x_0, x_1]$, the area is $\frac{h}{2}(f_0 + f_1)$.

**Composite rule:** Over $[a, b]$ with $n$ subintervals:

$$
\boxed{\int_a^b f(x)\,dx \approx \frac{h}{2}\left[f(a) + f(b) + 2\sum_{i=1}^{n-1}f_i\right]}
$$

**Error:** $E = -\frac{(b-a)h^2}{12}f''(\xi)$, which is $O(h^2)$.

**Properties:**
1. Halving $h$ reduces the error by a factor of 4.
2. Exact for straight lines. Overshoots for concave-up curves.
3. Works for sampled data with no spacing constraint.
4. Simple, but Simpson's rules are preferred when accuracy matters.

---

## NM-5.3 — Simpson's 3/8 Rule

### 📝 Definitions for NM-5.3

> **Simpson's 3/8 rule:** A Newton-Cotes formula using four equally spaced nodes (three subintervals). It fits a cubic polynomial and integrates it exactly:

$$
\int_{x_0}^{x_3} f(x)\,dx \approx \frac{3h}{8}(f_0 + 3f_1 + 3f_2 + f_3)
$$

> The rule requires the number of subintervals to be a **multiple of 3**.

### Theory

The 3/8 rule fits a cubic through four points instead of a quadratic through three. The weights are $1, 3, 3, 1$ (compared to $1, 4, 1$ for the 1/3 rule), and the prefactor is $\frac{3h}{8}$ instead of $\frac{h}{3}$.

It is also fourth order ($O(h^4)$), same as Simpson's 1/3, but with a larger error constant ($\frac{3}{80}$ vs $\frac{1}{90}$). So at equal $h$, the 1/3 rule is more accurate. The 3/8 rule exists for situations where the interval count is a multiple of 3 but not even.

### 🏆 Golden Questions for NM-5.3

#### 🎯 Evaluate $\int_1^2 (x^2 + 1)\,dx$ using Simpson's 3/8 rule.
> **Appeared:** 2019 Q.7(b) — (04 marks)

**Full Answer:**

Over $[1, 2]$, take $n = 3$ (must be multiple of 3), so $h = \frac{2 - 1}{3} = \frac{1}{3}$.

Nodes: $x = 1,\ \frac{4}{3},\ \frac{5}{3},\ 2$.

Compute the ordinates:

$$
f(1) = 1 + 1 = 2
$$

$$
f\!\left(\frac{4}{3}\right) = \frac{16}{9} + 1 = \frac{25}{9} \approx 2.777778
$$

$$
f\!\left(\frac{5}{3}\right) = \frac{25}{9} + 1 = \frac{34}{9} \approx 3.777778
$$

$$
f(2) = 4 + 1 = 5
$$

Apply the formula:

$$
\int_1^2(x^2 + 1)\,dx \approx \frac{3h}{8}[f_0 + 3f_1 + 3f_2 + f_3]
$$

$$
= \frac{3}{8}\cdot\frac{1}{3}\left[2 + 3\left(\frac{25}{9}\right) + 3\left(\frac{34}{9}\right) + 5\right]
$$

$$
= \frac{1}{8}\left[2 + \frac{25}{3} + \frac{34}{3} + 5\right] = \frac{1}{8}\left[7 + \frac{59}{3}\right] = \frac{1}{8}\cdot\frac{80}{3} = \frac{10}{3}
$$

$$
\boxed{\int_1^2(x^2 + 1)\,dx = \frac{10}{3} = 3.3333}
$$

> [!NOTE] Check by direct integration
> $\int_1^2(x^2+1)\,dx = \left[\frac{x^3}{3} + x\right]_1^2 = \frac{10}{3}$. Exact agreement. The integrand is quadratic, and the 3/8 rule integrates cubics exactly, so agreement is expected.

> [!WARNING] Use $n = 3$, not $n = 4$
> Taking $n = 4$ gives $h = 0.25$ and five nodes. The 3/8 rule has only four weights and cannot be applied to five nodes. This mistake gives $4.5586$ instead of $3.3333$.

---

## NM-5.5 — Romberg Integration

### 📝 Definitions for NM-5.5

> **Romberg integration:** A method that improves trapezoidal rule estimates by Richardson extrapolation. Compute trapezoidal approximations at successively halved step sizes ($h, h/2, h/4, \ldots$), then combine them to cancel the leading error terms. Each column of the Romberg table raises the order of accuracy.

> **Richardson extrapolation formula:**

$$
R_{k,j} = R_{k,j-1} + \frac{R_{k,j-1} - R_{k-1,j-1}}{4^j - 1}
$$

> Column 0 = trapezoidal values, Column 1 = Simpson's-level accuracy ($O(h^4)$), Column 2 = $O(h^6)$, etc.

### Theory

The trapezoidal rule has error $O(h^2)$. When you compute $T(h)$ and $T(h/2)$, the leading errors are in the ratio $4:1$. By combining them:

$$
R = T(h/2) + \frac{T(h/2) - T(h)}{4 - 1}
$$

you cancel the $h^2$ term and get $O(h^4)$ accuracy. This is the first column of extrapolation.

The second column uses the factor $4^2 - 1 = 15$ and achieves $O(h^6)$. Each column buys two more orders of accuracy, using **no new function evaluations**. The same data points serve every entry in the table.

**Romberg table structure:**

| $R_{k,0}$ (Trapezoidal) | $R_{k,1}$ (Simpson-level) | $R_{k,2}$ (Higher-order) |
| :-- | :-- | :-- |
| $T(h)$ | | |
| $T(h/2)$ | $R_{2,1}$ (divide by 3) | |
| $T(h/4)$ | $R_{3,1}$ (divide by 3) | $R_{3,2}$ (divide by 15) |

### 🏆 Golden Questions for NM-5.5

#### 🎯 Use Romberg's method to compute $\int_1^2 \frac{1}{2+x}\,dx$. Consider $h = 0.5, 0.25, 0.125$.
> **Appeared:** 2021 Q.8(b), 2023 Q.2(c) — (04 marks)

**Full Answer:**

**Step 1. Trapezoidal values (first column).**

$f(x) = \frac{1}{2+x}$

At $h = 0.5$, $n = 2$, nodes $x = 1, 1.5, 2$:

$$
T_2 = \frac{0.5}{2}\left[\frac{1}{3} + 2\cdot\frac{1}{3.5} + \frac{1}{4}\right] = 0.25[0.333333 + 0.571429 + 0.25] = 0.288690
$$

At $h = 0.25$, $n = 4$:

$$
T_4 = \frac{0.25}{2}\left[\frac{1}{3} + 2\left(\frac{1}{3.25} + \frac{1}{3.5} + \frac{1}{3.75} + \frac{1}{4.25}\right) + \frac{1}{4}\right] = 0.287935
$$

At $h = 0.125$, $n = 8$:

$$
T_8 = 0.287745
$$

**Step 2. Second column** (extrapolate with divisor $4^1 - 1 = 3$):

Row 2: $0.287935 + \frac{0.287935 - 0.288690}{3} = 0.287935 - 0.000252 = 0.287683$

Row 3: $0.287745 + \frac{0.287745 - 0.287935}{3} = 0.287745 - 0.000063 = 0.287682$

**Step 3. Third column** (divisor $4^2 - 1 = 15$):

Row 3: $0.287682 + \frac{0.287682 - 0.287683}{15} = 0.287682$

**The complete Romberg table:**

| $R_{k,0}$ | $R_{k,1}$ | $R_{k,2}$ |
| :-- | :-- | :-- |
| 0.288690 | | |
| 0.287935 | 0.287683 | |
| 0.287745 | 0.287682 | 0.287682 |

$$
\boxed{I \approx 0.2876821}
$$

> [!NOTE] Check: $\int_1^2 \frac{dx}{2+x} = \ln(4/3) = 0.2876820725$. The Romberg value differs by $\sim 10^{-9}$. Plain trapezoidal at $h = 0.125$ is off by $6.5 \times 10^{-4}$. Romberg improved accuracy by three orders of magnitude from the same data.

---

#### 🎯 Compute $\int_0^1 \frac{dx}{1+x^2}$ using trapezoidal rule at $h = 0.5, 0.25, 0.125$, then Romberg.
> **Appeared:** 2022 Q.3(a) — (04 marks)

**Full Answer:**

**Function values:**

| $x$ | 0 | 0.125 | 0.25 | 0.375 | 0.5 | 0.625 | 0.75 | 0.875 | 1 |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| $f(x)$ | 1.000000 | 0.984615 | 0.941176 | 0.876712 | 0.800000 | 0.719101 | 0.640000 | 0.566372 | 0.500000 |

**Trapezoidal column:**

At $h = 0.5$, $n = 2$:

$$
T_2 = \frac{0.5}{2}[1 + 2(0.8) + 0.5] = 0.25(3.1) = 0.775000
$$

At $h = 0.25$, $n = 4$:

$$
T_4 = 0.125[1 + 2(0.941176 + 0.8 + 0.640000) + 0.5] = 0.125(6.262352) = 0.782794
$$

At $h = 0.125$, $n = 8$:

$$
T_8 = 0.0625[1 + 2(0.984615 + 0.941176 + 0.876712 + 0.800000 + 0.719101 + 0.640000 + 0.566372) + 0.5]
$$

$$
= 0.0625[1 + 2(5.527976) + 0.5] = 0.0625(12.555952) = 0.784747
$$

**Romberg table:**

Row 2, col 1: $0.782794 + \frac{0.782794 - 0.775000}{3} = 0.782794 + 0.002598 = 0.785392$

Row 3, col 1: $0.784747 + \frac{0.784747 - 0.782794}{3} = 0.784747 + 0.000651 = 0.785398$

Row 3, col 2: $0.785398 + \frac{0.785398 - 0.785392}{15} = 0.785398 + 0.0000004 = 0.7853985$

| $R_{k,0}$ | $R_{k,1}$ | $R_{k,2}$ |
| :-- | :-- | :-- |
| 0.775000 | | |
| 0.782794 | 0.785392 | |
| 0.784747 | 0.785398 | 0.7853985 |

$$
\boxed{I \approx 0.7853985 \quad \text{(trapezoid alone gives } 0.784747\text{)}}
$$

> [!NOTE] Exact value: $\int_0^1 \frac{dx}{1+x^2} = \frac{\pi}{4} = 0.7853981634$. Romberg error: $3.6 \times 10^{-7}$. Trapezoidal error at $h = 0.125$: $6.5 \times 10^{-4}$. Romberg is about 1800 times more accurate from the same nine function values.

---

## NM-5.6 — Error Analysis in Integration

### Theory

Error analysis in numerical integration is not examined as a standalone question. Instead, it appears embedded in other problems:

- The trapezoidal error-bound problem (2018 Q.6(b)) uses $|E| \le \frac{(b-a)h^2}{12}\max|f''|$.
- The rocket problem (2018 Q.6(a)) asks for the true error and relative error.

**Summary of error terms:**

| Rule | Error per panel | Composite error | Order |
| :-- | :-- | :-- | :--: |
| Trapezoidal | $-\frac{h^3}{12}f''(\xi)$ | $-\frac{(b-a)h^2}{12}f''(\xi)$ | $O(h^2)$ |
| Simpson's 1/3 | $-\frac{h^5}{90}f^{(4)}(\xi)$ | $-\frac{(b-a)h^4}{180}f^{(4)}(\xi)$ | $O(h^4)$ |
| Simpson's 3/8 | $-\frac{3h^5}{80}f^{(4)}(\xi)$ | $-\frac{(b-a)3h^4}{80}f^{(4)}(\xi)$ | $O(h^4)$ |

All PYQs for this subtopic are worked in their filed locations: [NM-5.2](NM-5.2_Simpsons_One_Third_Rule.md) and the trapezoidal error-bound question above.

---

## NM-5.7 — Applied Integration

### Theory

Applied integration questions combine a physical context (rocket velocity, op-amp integrator) with a numerical integration method. The integration technique itself is Simpson's 1/3 or 3/8. The "applied" part is recognising the physical setup and extracting the correct integral.

All PYQs for this subtopic are worked in [NM-5.2](NM-5.2_Simpsons_One_Third_Rule.md):
- **Rocket distance** (2018 Q.6(a), 2023 Q.4(b)): 8-segment Simpson's 1/3.
- **Op-amp integrator** (2020 Q.6(b)): Mixed Simpson + trapezoid.

---

## ⚡ Exam Tips & Common Mistakes

1. **Trapezoidal derivation:** The key insight is that interior ordinates belong to two panels (factor of 2), endpoints belong to one panel (factor of 1). Get the counting right and the formula follows.
2. **Romberg table:** Columns divide by $4^j - 1$. Column 1 uses divisor 3, column 2 uses divisor 15. Each entry combines two entries from the previous column.
3. **For the error-bound question:** Find $\max|f''|$ on the interval, plug into the bound, solve for $n$, round **up**.
4. **3/8 rule:** Weights are $1, 3, 3, 1$ (not $1, 4, 1$). Prefactor is $\frac{3h}{8}$ (not $\frac{h}{3}$). $n$ must be a multiple of 3.

## 🔗 Related Topics

- [NM-5.2: Simpson's 1/3 Rule](NM-5.2_Simpsons_One_Third_Rule.md) — derivation, exactness proof, rocket and op-amp problems
- [NM-5.4: Rule Comparison](NM-5.4_Rule_Comparison_and_Step_Constraints.md) — comparison table and constraint analysis
- [NM-7: Numerical Differentiation](NM-7_Numerical_Differentiation.md) — the derivative counterpart to integration
- [NM-4.11: Difference Table Formation](NM-4.11_Difference_Table_Formation.md) — difference tables used in derivative-based integration error

---

[← Previous: NM-5.4 Rule Comparison](NM-5.4_Rule_Comparison_and_Step_Constraints.md) | [🏠 Index](00_Index.md) | [Next: NM-6 Optimization →](NM-6_Optimization.md)
