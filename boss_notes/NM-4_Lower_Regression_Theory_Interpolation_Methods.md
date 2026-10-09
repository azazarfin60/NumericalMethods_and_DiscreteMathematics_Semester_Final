[← Previous: NM-4.11 Difference Table Formation](NM-4.11_Difference_Table_Formation.md) | [🏠 Index](00_Index.md) | [Next: NM-5.2 Simpson's 1/3 Rule →](NM-5.2_Simpsons_One_Third_Rule.md)

---

# NM-4: Curve Fitting — Regression Theory & Other Interpolation Methods
> **Section:** A (Numerical Methods) | **Priority:** 🟠🟡 (mixed) | **Subtopics:** NM-4.4, NM-4.5, NM-4.8, NM-4.9, NM-4.10
> **Sources:** Jain Ch.3 §3.6–§3.7, §3.9; Ch.4 §4.1–§4.2; Class Notes Class-05; Raidah Notes p.8–16

## Why This Topic Matters

This merged guide covers the secondary and specialized topics of curve fitting and interpolation. It brings together regression optimization theory, linear interpolation on chords, Newton's backward and divided difference methods, and central difference formulas (Gauss and Stirling). Knowing these techniques ensures you are prepared for unexpected theory questions and specialized data tables.

---

## NM-4.4: Regression Criteria & Theory

### 📝 Key Definitions for NM-4.4

> **Least-Squares Criterion:** "The curve drawn is such that the discrepancy between the data points and the curve is least. In the method of least squares, the sum of the squares of the errors is minimized." — Jain, §4.1 (p. 126)

> **Residual:** "If $e_i$ is the error of approximation at $x = x_i$, then we have $e_i = y_i - f(x_i)$." — Jain, §4.2 (p. 127)

### Core Theory: Why Alternative Criteria Fail

When fitting a model $y = f(x)$ to $n$ data points $(x_i, y_i)$, we can define error criteria in several ways. Three obvious alternatives suffer from fatal mathematical flaws:

1. **Minimum sum of errors ($\sum e_i = 0$):** Positive and negative errors cancel out. Infinitely many terrible lines satisfy $\sum e_i = 0$. For instance, a line passing far above three points and far below a fourth point has zero sum of error while fitting none of the data.
2. **Minimum sum of absolute errors ($\sum |e_i|$):** This removes sign cancellation, but the absolute value function $|e_i|$ is not differentiable at zero. It has sharp corners. Thus, we cannot take simple derivatives to obtain linear normal equations. Also, the minimum is often non-unique.
3. **Minimax or minimum single error ($\min_i |e_i|$):** Considering only the single smallest error drives one residual to zero while ignoring all remaining points.

#### Why the Least-Squares Criterion is Best Suited

Minimizing the sum of squared errors:

$$
S = \sum_{i=1}^n e_i^2 = \sum_{i=1}^n [y_i - f(x_i)]^2
$$

is the standard engineering criterion for three reasons:
- **No cancellation:** Squaring makes every residual non-negative.
- **Unique, smooth minimum:** $S$ is a smooth, differentiable quadratic surface. Setting partial derivatives $\frac{\partial S}{\partial a_j} = 0$ yields linear normal equations with a unique closed-form solution.
- **Probabilistic optimality:** If measurement errors are independent and normally distributed with equal variance, least-squares gives the maximum-likelihood estimator.

### 🏆 Golden Questions for NM-4.4

#### 🎯 With necessary figure(s) explain why minimum sum of error, minimum sum of absolute error and minimum error are ill-suited for regression. Which criterion is best suited for regression?
> **Appeared:** 2017 Q.6(a) — (04 marks)

**Full Answer:**

Consider four data points where three points lie near a trendline and one point is an outlier:

```text
 y
 ^         .          .
 |      .        .          o <- outlier
 |   .            .
 |  .         .            <- true relation
 | .      .
 |________________________> x
```

**1. Minimum sum of errors ($\sum e_i = 0$):**
Positive and negative residuals cancel each other out. This condition is satisfied by infinitely many lines, including lines that miss every data point:

```text
   .            .
        sum e = +2
   .    
        sum e = -2      -> total sum = 0, but a terrible fit
```

**2. Minimum sum of absolute errors ($\sum |e_i|$):**
Cancellation is eliminated. But $|e_i|$ has sharp corners (non-differentiable at $e_i = 0$), so no simple linear normal equations exist. The solution is also often non-unique when multiple distinct lines share the same total absolute deviation.

**3. Minimum error ($\min_i |e_i|$):**
Looking at $\min_i |e_i|$ focuses on a single point. It forces the line through one point while ignoring errors at all other $n-1$ points.

**Best suited criterion: The Least-Squares Criterion.**
Minimizing the sum of squared errors:

$$
S = \sum_{i=1}^n e_i^2 = \sum_{i=1}^n [y_i - f(x_i)]^2
$$

is best suited because:
1. **No cancellation:** Squaring guarantees every term is non-negative ($e_i^2 \ge 0$).
2. **Smooth unique minimum:** Differentiating with respect to unknown parameters yields linear normal equations with a direct closed-form solution.
3. **Statistical optimality:** For normally distributed experimental noise, least squares provides the maximum-likelihood estimate.

$$
\boxed{S = \sum_{i=1}^{n}\left(y_i - f(x_i)\right)^2 \text{ is the criterion to minimise}}
$$

---

## NM-4.5: Linear Interpolation

### 📝 Key Definitions for NM-4.5

> **Linear Interpolation:** "The equation of a straight line (a linear polynomial) passing through two points $(x_0, y_0)$ and $(x_1, y_1)$ is given by $L_1(x) = \dfrac{x - x_1}{x_0 - x_1}y_0 + \dfrac{x - x_0}{x_1 - x_0}y_1$." — Jain, §3.9.1 (p. 101)

### Core Theory: Two-Point Linear Interpolation

Linear interpolation approximates a function between two known points $(x_0, y_0)$ and $(x_1, y_1)$ by a straight secant line (chord):

$$
y(x) = y_0 + \frac{x - x_0}{x_1 - x_0}(y_1 - y_0)
$$

The truncation error of linear interpolation depends on the second derivative of the underlying function:

$$
R_1(x) = \frac{(x - x_0)(x - x_1)}{2} f''(\xi)
$$

If the data points carry experimental error, the interpolated chord inherits the slope error directly, creating an offset from the true physical value.

### 🏆 Golden Questions for NM-4.5

#### 🎯 The upward velocity of a rocket is given as a function of time in table below. Determine the value of the velocity at $t = 16$ seconds using $1^{\text{st}}$ order polynomial.
> **Appeared:** 2018 Q.3(b) — (03 marks)

**Full Answer:**

Given rocket velocity table:

| $t$ (s) | 0 | 10 | 15 | 20 | 22.5 | 30 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| $v(t)$ (m/s) | 0 | 227.04 | 362.78 | 517.35 | 602.97 | 901.67 |

The target $t = 16\text{ s}$ is bracketed by $(t_0, v_0) = (15, 362.78)$ and $(t_1, v_1) = (20, 517.35)$.

A first-order polynomial is a straight line:

$$
v(t) = v_0 + \frac{t - t_0}{t_1 - t_0}(v_1 - v_0)
$$

Substitute the values:

$$
v(16) = 362.78 + \frac{16 - 15}{20 - 15}(517.35 - 362.78) = 362.78 + \frac{1}{5}(154.57)
$$

$$
v(16) = 362.78 + 30.914 = 393.694\ \text{m/s}
$$

$$
\boxed{v(16) = 393.694\ \text{m/s}}
$$

---

#### 🎯 To verify Ohm's law, an experiment was performed and the results obtained are in the following table. Use linear interpolation to determine the current for $12\text{V}$ of supply. Explain why the result differs from actual value.
> **Appeared:** 2019 Q.5(b) — (04 marks)

**Full Answer:**

Given experimental data:

| $V$ (V) | 5 | 10 | 15 | 20 | 25 |
| :---: | :---: | :---: | :---: | :---: | :---: |
| $I$ (A) | 1 | 2.1 | 3 | 4.2 | 5 |

The target $V = 12\text{ V}$ is bracketed by $(V_0, I_0) = (10, 2.1)$ and $(V_1, I_1) = (15, 3.0)$.

**Linear interpolation:**

$$
I(12) = I_0 + \frac{V - V_0}{V_1 - V_0}(I_1 - I_0) = 2.1 + \frac{12 - 10}{15 - 10}(3.0 - 2.1)
$$

$$
I(12) = 2.1 + \frac{2}{5}(0.9) = 2.1 + 0.36 = 2.46\ \text{A}
$$

$$
\boxed{I(12\ \text{V}) = 2.46\ \text{A}}
$$

**Why this differs from the actual value:**
Ohm's law states $V = IR$. From the accurate data points at $5\text{ V}, 15\text{ V}, 25\text{ V}$, the resistance is $R = 5\ \Omega$. Thus, the true physical current at $12\text{ V}$ is:

$$
I_{\text{true}} = \frac{12\text{ V}}{5\ \Omega} = 2.40\ \text{A}
$$

The interpolated result is $2.46\text{ A}$, giving a discrepancy of $0.06\text{ A}$. This difference occurs because the reading at $10\text{ V}$ carries a measurement error ($2.1\text{ A}$ instead of $2.0\text{ A}$). Linear interpolation connects the two points with a straight chord, propagating the $+0.1\text{ A}$ measurement error directly into the interpolated value.

---

## NM-4.8: Newton's Backward Difference Interpolation

### 📝 Key Definitions for NM-4.8

> **Newton's Backward Difference Formula:** "$$y_n(x) = y_n + p\nabla y_n + \frac{p(p+1)}{2!}\nabla^2 y_n + \cdots + \frac{p(p+1)\dots(p+n-1)}{n!}\nabla^n y_n$$ where $p = \dfrac{x - x_n}{h}$. This formula is useful for interpolation near the end of the tabular values." — Jain, §3.6 (p. 85)

### Core Theory: Structure and Usage

Newton's backward formula is designed for points located near the end of an equidistant table. It anchors at the final tabular point $(x_n, y_n)$ and moves backward along the bottom diagonal of the difference table.

Key operational rules:
1. **Anchor point:** Use $x_n$, the last node in the table.
2. **Dimensionless parameter:** $p = \frac{x - x_n}{h}$. For a point inside the table near the end, $x < x_n$, so $p$ is negative ($-1 \le p \le 0$).
3. **Rising factorials:** The terms use rising products: $p(p+1)(p+2)\dots$

### 🏆 Golden Questions for NM-4.8

For full step-by-step solutions of the exam questions involving Newton's backward difference formula, see:
- **Census estimation for 1925** ($p = -0.6$, backward from 1931): Worked in [NM-4.11 Difference Table Formation](NM-4.11_Difference_Table_Formation.md), yielding $\boxed{y(1925) = 96.8368 \text{ thousand} \approx 96\,837}$.
- **Census extrapolation for 1995** ($p = 3.4$, backward from 1961): Worked in [NM-4.11 Difference Table Formation](NM-4.11_Difference_Table_Formation.md), yielding $\boxed{P(1995) = 20.1888 \text{ thousand (Newton backward difference, all 5 points)}}$.
- **Temperature estimation at 7 hours** ($p = -0.5$, backward from 8 hours): Worked in [NM-4.7 Newton's Forward Difference](NM-4.7_Newtons_Forward_Difference.md), yielding $\boxed{T(7) = 38.875 \approx 38.88 \ ^\circ\text{C}}$.

---

## NM-4.9: Newton's Divided Difference Interpolation

### 📝 Key Definitions for NM-4.9

> **Divided Differences:** "The first divided difference of $f(x)$ for the arguments $x_0, x_1$ is defined as $f[x_0, x_1] = \dfrac{f(x_1) - f(x_0)}{x_1 - x_0}$. In general, the $k$-th divided difference is $f[x_0, x_1, \dots, x_k] = \dfrac{f[x_1, \dots, x_k] - f[x_0, \dots, x_{k-1}]}{x_k - x_0}$." — Jain, §3.10 (p. 104)

> **Symmetry of Divided Differences:** "Divided differences are symmetric functions of their arguments, i.e., the value of a divided difference is independent of the order in which the arguments are arranged." — Jain, §3.10 (p. 105)

### Core Theory: General Interpolation for Unequal Intervals

Newton's divided difference interpolating polynomial expresses $P_n(x)$ as:

$$
P_n(x) = f[x_0] + f[x_0, x_1](x - x_0) + f[x_0, x_1, x_2](x - x_0)(x - x_1) + \dots + f[x_0, \dots, x_n](x - x_0)\dots(x - x_{n-1})
$$

#### Key Advantages of Divided Differences
- **Permutation invariance:** Because divided differences are completely symmetric in their arguments, sorting the table is not required mathematically. The same unique polynomial is obtained regardless of node order.
- **Incremental updates:** If a new data point $(x_{n+1}, y_{n+1})$ is added, all previously computed terms remain unchanged. Only one additional divided difference term must be calculated.

### 🏆 Golden Questions for NM-4.9

#### 🎯 Using Newton's general interpolation formula find $f(x)$ as a polynomial in $x$ for the following table. Also, determine $f(3.5)$ using the polynomial.
> **Appeared:** 2019 Q.5(c) — (05 marks)

**Full Answer:**

Given data:

| $x$ | $-1$ | 0 | 3 | 6 | 7 |
| :---: | :---: | :---: | :---: | :---: | :---: |
| $f(x)$ | 3 | $-6$ | 39 | 822 | 1611 |

**Step 1: Construct the divided difference table**

- Order 0: $f[x_i] = 3, -6, 39, 822, 1611$
- Order 1:
  - $f[x_0, x_1] = \frac{-6 - 3}{0 - (-1)} = -9$
  - $f[x_1, x_2] = \frac{39 - (-6)}{3 - 0} = 15$
  - $f[x_2, x_3] = \frac{822 - 39}{6 - 3} = 261$
  - $f[x_3, x_4] = \frac{1611 - 822}{7 - 6} = 789$
- Order 2:
  - $f[x_0, x_1, x_2] = \frac{15 - (-9)}{3 - (-1)} = \frac{24}{4} = 6$
  - $f[x_1, x_2, x_3] = \frac{261 - 15}{6 - 0} = \frac{246}{6} = 41$
  - $f[x_2, x_3, x_4] = \frac{789 - 261}{7 - 3} = \frac{528}{4} = 132$
- Order 3:
  - $f[x_0, x_1, x_2, x_3] = \frac{41 - 6}{6 - (-1)} = \frac{35}{7} = 5$
  - $f[x_1, x_2, x_3, x_4] = \frac{132 - 41}{7 - 0} = \frac{91}{7} = 13$
- Order 4:
  - $f[x_0, x_1, x_2, x_3, x_4] = \frac{13 - 5}{7 - (-1)} = \frac{8}{8} = 1$

**Step 2: Form Newton's divided difference polynomial**

$$
f(x) = 3 - 9(x + 1) + 6(x + 1)x + 5(x + 1)x(x - 3) + 1(x + 1)x(x - 3)(x - 6)
$$

Expand term by term:
- $(x + 1)x(x - 3)(x - 6) = x^4 - 8x^3 + 9x^2 + 18x$
- $5(x + 1)x(x - 3) = 5x^3 - 10x^2 - 15x$
- $6(x + 1)x = 6x^2 + 6x$
- $-9(x + 1) = -9x - 9$
- Constant $= 3$

Combine all terms:

$$
f(x) = x^4 + (-8 + 5)x^3 + (9 - 10 + 6)x^2 + (18 - 15 + 6 - 9)x + (3 - 9)
$$

$$
\boxed{f(x) = x^4 - 3x^3 + 5x^2 - 6}
$$

**Step 3: Evaluate at $x = 3.5$**

$$
f(3.5) = (3.5)^4 - 3(3.5)^3 + 5(3.5)^2 - 6 = 150.0625 - 128.625 + 61.25 - 6 = 76.6875
$$

$$
\boxed{f(3.5) = 76.6875}
$$

---

#### 🎯 Using Newton's divided difference interpolating polynomial estimate the value of signal $s(t)$ at $t = 2.25$ sec for the following tabulated values.
> **Appeared:** 2020 Q.5(b) — (05 marks)

**Full Answer:**

Given signal table:

| $t$ | 0.5 | 0.2 | 1.4 | 2.2 | 3.0 |
| :---: | :---: | :---: | :---: | :---: | :---: |
| $s(t)$ | $-10.25$ | $-3.768$ | $5.976$ | $28.972$ | $79.0$ |

*(Note: The table lists $0.5$ before $0.2$. Because divided differences are symmetric functions of their nodes, Newton's divided difference formula is invariant under any permutation of the data).*

**Step 1: Divided difference table**

- First divided differences:
  - $f[t_0, t_1] = \frac{-3.768 - (-10.25)}{0.2 - 0.5} = \frac{6.482}{-0.3} = -21.606667$
  - $f[t_1, t_2] = \frac{5.976 - (-3.768)}{1.4 - 0.2} = \frac{9.744}{1.2} = 8.120000$
  - $f[t_2, t_3] = \frac{28.972 - 5.976}{2.2 - 1.4} = \frac{22.996}{0.8} = 28.745000$
  - $f[t_3, t_4] = \frac{79.0 - 28.972}{3.0 - 2.2} = \frac{50.028}{0.8} = 62.535000$
- Second divided differences:
  - $f[t_0, t_1, t_2] = \frac{8.12 - (-21.606667)}{1.4 - 0.5} = \frac{29.726667}{0.9} = 33.029630$
  - $f[t_1, t_2, t_3] = \frac{28.745 - 8.12}{2.2 - 0.2} = \frac{20.625}{2.0} = 10.312500$
  - $f[t_2, t_3, t_4] = \frac{62.535 - 28.745}{3.0 - 1.4} = \frac{33.79}{1.6} = 21.118750$
- Third divided differences:
  - $f[t_0, \dots, t_3] = \frac{10.3125 - 33.029630}{2.2 - 0.5} = \frac{-22.717130}{1.7} = -13.363017$
  - $f[t_1, \dots, t_4] = \frac{21.11875 - 10.3125}{3.0 - 0.2} = \frac{10.80625}{2.8} = 3.859375$
- Fourth divided difference:
  - $f[t_0, \dots, t_4] = \frac{3.859375 - (-13.363017)}{3.0 - 0.5} = \frac{17.222392}{2.5} = 6.888957$

**Step 2: Evaluate at $t = 2.25$**

Linear factors at $t = 2.25$:
- $(t - 0.5) = 1.75$
- $(t - 0.5)(t - 0.2) = (1.75)(2.05) = 3.5875$
- $(t - 0.5)(t - 0.2)(t - 1.4) = (3.5875)(0.85) = 3.049375$
- $(t - 0.5)(t - 0.2)(t - 1.4)(t - 2.2) = (3.049375)(0.05) = 0.15246875$

Sum the polynomial terms:

$$
s(2.25) = -10.25 - 21.606667(1.75) + 33.029630(3.5875) - 13.363017(3.049375) + 6.888957(0.15246875)
$$

$$
s(2.25) = -10.25 - 37.811667 + 118.49380 - 40.74872 + 1.05035 = 30.7336
$$

$$
\boxed{s(2.25) = 30.7336}
$$

---

#### 🎯 Find the polynomial which fits the following data: $(-1, 7)$, $(1, 5)$, $(2, 15)$.
> **Appeared:** 2022 Q.2(a) — (03 marks)

**Full Answer:**

Three points specify a unique quadratic polynomial $y = a_0 + a_1 x + a_2 x^2$.

**Method: Divided Differences Table**

| $x$ | $y$ | First Divided Difference | Second Divided Difference |
| :--: | :--: | :--: | :--: |
| $-1$ | 7 | $\frac{5 - 7}{1 - (-1)} = -1$ | $\frac{10 - (-1)}{2 - (-1)} = \frac{11}{3}$ |
| 1 | 5 | $\frac{15 - 5}{2 - 1} = 10$ | — |
| 2 | 15 | — | — |

**Form the Newton polynomial:**

$$
y(x) = y_0 + f[x_0, x_1](x - x_0) + f[x_0, x_1, x_2](x - x_0)(x - x_1)
$$

$$
y(x) = 7 - 1(x + 1) + \frac{11}{3}(x + 1)(x - 1)
$$

$$
y(x) = 7 - x - 1 + \frac{11}{3}(x^2 - 1) = 6 - x + \frac{11}{3}x^2 - \frac{11}{3}
$$

$$
y(x) = \frac{11}{3}x^2 - x + \left(6 - \frac{11}{3}\right) = \frac{11}{3}x^2 - x + \frac{7}{3}
$$

$$
\boxed{y = \frac{11}{3}x^2 - x + \frac{7}{3}}
$$

---

## NM-4.10: Central Difference Formulas (Gauss & Stirling) ⚠️

### 📝 Key Definitions for NM-4.10

> **Gauss' Forward Formula:** "$$y_p = y_0 + p\Delta y_0 + \frac{p(p-1)}{2!}\Delta^2 y_{-1} + \frac{(p+1)p(p-1)}{3!}\Delta^3 y_{-1} + \frac{(p+1)p(p-1)(p-2)}{4!}\Delta^4 y_{-2} + \cdots$$ where the differences lie on the zig-zag path shown in Table 3.6." — Jain, §3.7.1 (p. 91)

> **Gauss' Backward Formula:** "$$y_p = y_0 + p\Delta y_{-1} + \frac{p(p+1)}{2!}\Delta^2 y_{-1} + \frac{(p+1)p(p-1)}{3!}\Delta^3 y_{-2} + \frac{(p+2)(p+1)p(p-1)}{4!}\nabla^4 y_{-2} + \cdots$$ where the differences lie on the zig-zag path shown in Table 3.7." — Jain, §3.7.1 (p. 92–93)

> **Stirling's Formula:** "Taking the mean of Gauss' forward and backward formulae, we obtain: $$y_p = y_0 + p \frac{\Delta y_{-1} + \Delta y_0}{2} + \frac{p^2}{2} \Delta^2 y_{-1} + \frac{p(p^2 - 1)}{3!} \frac{\Delta^3 y_{-1} + \Delta^3 y_{-2}}{2} + \frac{p^2(p^2 - 1)}{4!} \Delta^4 y_{-2} + \cdots$$" — Jain, §3.7.2 (p. 94)

### Core Theory: Central Difference Zig-Zag Paths

When interpolating near the middle of a table, Newton's forward and backward formulas become unbalanced. Central difference formulas keep the points symmetrically arranged around the origin $x_0$, keeping $|p| \le 0.5$. This guarantees that factorial multipliers decay quickly and round-off error is minimized.

#### Gauss' Forward Difference Path

The differences follow a zig-zag trajectory starting at $y_0$, stepping down to $\Delta y_0$, then up to $\Delta^2 y_{-1}$, down to $\Delta^3 y_{-1}$, and up to $\Delta^4 y_{-2}$:

![Table 3.6 Gauss Forward Formula difference table showing the zig-zag path connecting central differences](diagrams/nm4_gauss_forward_difference_table.jpg)

#### Gauss' Backward Difference Path

The differences follow the alternate zig-zag trajectory starting at $y_0$, stepping up to $\Delta y_{-1}$, down to $\Delta^2 y_{-1}$, up to $\Delta^3 y_{-2}$, and down to $\Delta^4 y_{-2}$:

![Table 3.7 Gauss Backward Formula difference table showing the zig-zag path connecting central differences](diagrams/nm4_gauss_backward_difference_table.jpg)

### 🏆 Golden Questions for NM-4.10

#### 🎯 From the following table, calculate the value of $e^{1.17}$ using Gauss' forward formula.
> **Appeared:** 2021 Q.4(b) — (05 marks)

**Full Answer:**

Given table ($h = 0.05$):

| $x$ | 1.00 | 1.05 | 1.10 | 1.15 | 1.20 | 1.25 | 1.30 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| $e^x$ | 2.7183 | 2.8577 | 3.0042 | 3.1582 | 3.3201 | 3.4903 | 3.6693 |

**Step 1: Choose base node $x_0$ and compute $p$**
The target is $x = 1.17$. Near the middle, choose $x_0 = 1.15$:

$$
p = \frac{x - x_0}{h} = \frac{1.17 - 1.15}{0.05} = \frac{0.02}{0.05} = 0.4 \quad (0 \le p \le 0.5)
$$

**Step 2: Construct the difference table**

| $x$ | $y$ | $\Delta y$ | $\Delta^2 y$ | $\Delta^3 y$ | $\Delta^4 y$ |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1.00 | 2.7183 | 0.1394 | 0.0071 | 0.0004 | 0.0000 |
| 1.05 | 2.8577 | 0.1465 | 0.0075 | 0.0004 | 0.0000 |
| 1.10 | 3.0042 | 0.1540 | 0.0079 | 0.0004 | 0.0001 |
| 1.15 ($x_0$) | 3.1582 ($y_0$) | 0.1619 ($\Delta y_0$) | 0.0083 | 0.0005 | — |
| 1.20 | 3.3201 | 0.1702 | 0.0088 | — | — |
| 1.25 | 3.4903 | 0.1790 | — | — | — |
| 1.30 | 3.6693 | — | — | — | — |

**Step 3: Collect central differences along Gauss' forward path**
- $y_0 = 3.1582$
- $\Delta y_0 = 0.1619$
- $\Delta^2 y_{-1} = 0.0079$
- $\Delta^3 y_{-1} = 0.0004$
- $\Delta^4 y_{-2} = 0.0000$

**Step 4: Evaluate Gauss' forward formula ($p = 0.4$)**

$$
y_p = y_0 + p\Delta y_0 + \frac{p(p-1)}{2!}\Delta^2 y_{-1} + \frac{(p+1)p(p-1)}{3!}\Delta^3 y_{-1} + \frac{(p+1)p(p-1)(p-2)}{4!}\Delta^4 y_{-2}
$$

Compute the terms:
- $T_0 = 3.1582$
- $T_1 = 0.4(0.1619) = +0.06476$
- $T_2 = \frac{0.4(-0.6)}{2}(0.0079) = -0.12(0.0079) = -0.000948$
- $T_3 = \frac{(1.4)(0.4)(-0.6)}{6}(0.0004) = -0.056(0.0004) = -0.0000224$
- $T_4 = 0$

Sum:

$$
e^{1.17} \approx 3.1582 + 0.06476 - 0.000948 - 0.0000224 = 3.2219896 \approx 3.22199
$$

$$
\boxed{e^{1.17} \approx 3.22199}
$$

The true value is $e^{1.17} = 3.221993$, verifying that Gauss' forward central difference formula is accurate to 5 decimal places.

---

## ⚡ Exam Tips & Common Mistakes

1. **Know the regression criteria by heart.** When asked why $\sum e_i = 0$ is unsuitable, write the two-point cancellation argument. When asked why $\sum |e_i|$ is unsuitable, mention the lack of derivatives at zero and non-unique solutions.
2. **Divided differences do not require sorted tables.** If exam data lists points out of numerical order, do not panic. Divided differences yield the exact same polynomial either way.
3. **Trace the central path carefully.** For Gauss' forward formula, follow the zigzag: $y_0 \to \Delta y_0 \to \Delta^2 y_{-1} \to \Delta^3 y_{-1} \to \Delta^4 y_{-2}$. Check the subscripts on your scratch paper before copying values from the table.
4. **Distinguish falling vs. rising factorials.** Forward differences use falling terms $p(p-1)\dots$, while backward differences use rising terms $p(p+1)\dots$ Gauss central formulas interleave both: $(p+1)p(p-1)\dots$

## 🔗 Related Topics

- [NM-4.2: Least-Squares Linear Regression](NM-4.2_Least_Squares_Linear_Regression.md) — normal equations and straight-line regression fits
- [NM-4.6: Lagrange's Interpolation](NM-4.6_Lagranges_Interpolation.md) — alternative formulation for unequal interval interpolation
- [NM-4.7: Newton's Forward Difference](NM-4.7_Newtons_Forward_Difference.md) — forward difference derivation and applications
- [NM-4.11: Difference Table Formation](NM-4.11_Difference_Table_Formation.md) — table construction and population census variants
- [NM-5.2: Simpson's 1/3 Rule](NM-5.2_Simpsons_One_Third_Rule.md) — numerical integration using parabolic interpolation

---

[← Previous: NM-4.11 Difference Table Formation](NM-4.11_Difference_Table_Formation.md) | [🏠 Index](00_Index.md) | [Next: NM-5.2 Simpson's 1/3 Rule →](NM-5.2_Simpsons_One_Third_Rule.md)
