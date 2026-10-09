[← Previous: NM-4.7 Newton's Forward Difference](NM-4.7_Newtons_Forward_Difference.md) | [🏠 Index](00_Index.md) | [Next: NM-4_Lower Regression Theory & Interpolation Methods →](NM-4_Lower_Regression_Theory_Interpolation_Methods.md)

---

# NM-4.11: Difference Table Formation
> **Section:** A (Numerical Methods) | **Priority:** 🔴 | **Exam Frequency:** 5/8 years
> **Sources:** Jain Ch.3 §3.3–§3.4 (p. 76–81); Fahad Notes Class-05; Raidah Notes p.14–16

## Why This Topic Matters

Finite difference tables are the foundation of numerical interpolation, differentiation, and integration. This topic appears in 5 out of 8 semester finals. Exam questions provide real-world demographic or sensor data tables and ask you to estimate intermediate values or extrapolate future trends using forward and backward difference tables.

---

## 📝 Key Definitions

> **Forward Difference Operator ($\Delta$):** "The differences $y_1 - y_0, y_2 - y_1, \dots, y_n - y_{n-1}$ are called the *first forward differences* of the function $y = f(x)$, and are denoted by $\Delta y_0, \Delta y_1, \dots, \Delta y_{n-1}$, respectively. In general, $\Delta^{k+1} y_i = \Delta^k y_{i+1} - \Delta^k y_i$." — Jain, §3.3.1 (p. 76)

> **Backward Difference Operator ($\nabla$):** "The differences $y_1 - y_0, y_2 - y_1, \dots, y_n - y_{n-1}$ are called *first backward differences* and are denoted by $\nabla y_1, \nabla y_2, \dots, \nabla y_n$, respectively. In general, $\nabla^{k+1} y_i = \nabla^k y_i - \nabla^k y_{i-1}$." — Jain, §3.3.2 (p. 78)

> **Fundamental Theorem of Finite Differences:** "If $f(x)$ is a polynomial of degree $n$ in $x$ and the values of $x$ are equally spaced, then the $n$-th difference of $f(x)$ is constant and all higher-order differences are identically zero ($\Delta^{n+1} f(x) = 0$)." — [paraphrased from Jain §3.5, p. 83]

---

## Core Theory: Difference Tables and Practical Interpolation

### 1. Constructing a Finite Difference Table

For an equidistant sequence of inputs $x_0, x_1, \dots, x_n$ with constant step size $h$:

1. List the given values of $x$ and $y$ in the first two columns.
2. In the column for first differences ($\Delta y$), compute each entry by subtracting the upper value from the lower value: $\Delta y_i = y_{i+1} - y_i$.
3. In each subsequent column, subtract adjacent entries: $\Delta^2 y_i = \Delta y_{i+1} - \Delta y_i$.
4. Repeat until only a single entry remains or higher differences become zero.

#### Standard Diagonal Table Layout

| $x$ | $y$ | $\Delta y$ | $\Delta^2 y$ | $\Delta^3 y$ | $\Delta^4 y$ |
| :--: | :--: | :--: | :--: | :--: | :--: |
| $x_0$ | $y_0$ | $\Delta y_0$ | $\Delta^2 y_0$ | $\Delta^3 y_0$ | $\Delta^4 y_0$ |
| $x_1$ | $y_1$ | $\Delta y_1$ | $\Delta^2 y_1$ | $\Delta^3 y_1$ | — |
| $x_2$ | $y_2$ | $\Delta y_2$ | $\Delta^2 y_2$ | — | — |
| $x_3$ | $y_3$ | $\Delta y_3$ | — | — | — |
| $x_4$ | $y_4$ | — | — | — | — |

- The **top descending diagonal** ($\Delta y_0, \Delta^2 y_0, \Delta^3 y_0, \dots$) contains the **forward differences** from $x_0$.
- The **bottom ascending diagonal** ($\nabla y_4 = \Delta y_3, \nabla^2 y_4 = \Delta^2 y_2, \dots$) contains the **backward differences** from $x_4$.

### 2. Choosing Between Forward and Backward Formulas

Always inspect where the target point $x$ lies relative to the tabulated domain $[x_0, x_n]$:

| Target Location | Recommended Formula | Anchor Node | Step Parameter $p$ | Range of $p$ |
| :-- | :-- | :-- | :-- | :-- |
| Near beginning of table ($x \approx x_0$) | **Newton Forward** | $x_0$ (top node) | $p = \dfrac{x - x_0}{h}$ | $0 \le p \le 1$ |
| Near end of table ($x \approx x_n$) | **Newton Backward** | $x_n$ (bottom node) | $p = \dfrac{x - x_n}{h}$ | $-1 \le p \le 0$ |
| Beyond the end (Extrapolation) | **Newton Backward** | $x_n$ (bottom node) | $p = \dfrac{x - x_n}{h}$ | $p > 0$ (unstable!) |

### 3. The Formulas

**Newton's Forward Interpolation Formula:**

$$
y(x) = y_0 + p\Delta y_0 + \frac{p(p-1)}{2!}\Delta^2 y_0 + \frac{p(p-1)(p-2)}{3!}\Delta^3 y_0 + \frac{p(p-1)(p-2)(p-3)}{4!}\Delta^4 y_0
$$

**Newton's Backward Interpolation Formula:**

$$
y(x) = y_n + p\nabla y_n + \frac{p(p+1)}{2!}\nabla^2 y_n + \frac{p(p+1)(p+2)}{3!}\nabla^3 y_n + \frac{p(p+1)(p+2)(p+3)}{4!}\nabla^4 y_n
$$

Notice the algebraic distinction:
- Forward uses **falling factorials**: $p(p-1)(p-2)\dots$
- Backward uses **rising factorials**: $p(p+1)(p+2)\dots$

### 4. The Risk of Extrapolation Beyond the Table

When estimating values beyond the last node ($x > x_n$), the parameter $p$ exceeds $1$. The factorial multiplier terms grow rapidly with each order. Higher-order differences then oscillate wildly, often producing physically impossible estimates (such as a declining population when all census figures are growing). For values more than one step outside the table, linear least-squares regression is safer than polynomial extrapolation.

---

## Worked Example (PYQ 2020 Q.3(b))

The population of a town in the decennial census was as given below:

| Year $x$ | 1891 | 1901 | 1911 | 1921 | 1931 |
| :---: | :---: | :---: | :---: | :---: | :---: |
| Population $y$ (thousands) | 46 | 66 | 81 | 93 | 101 |

Estimate the population for: (i) 1895 and (ii) 1925.

**Step 1: Build the Finite Difference Table ($h = 10$)**

| Year $x$ | Population $y$ | $\Delta y$ | $\Delta^2 y$ | $\Delta^3 y$ | $\Delta^4 y$ |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1891 | 46 | 20 | $-5$ | 2 | $-3$ |
| 1901 | 66 | 15 | $-3$ | $-1$ | — |
| 1911 | 81 | 12 | $-4$ | — | — |
| 1921 | 93 | 8 | — | — | — |
| 1931 | 101 | — | — | — | — |

**Step 2: Estimate for 1895 (Newton's Forward Formula)**

The target 1895 is near the top of the table. Choose $x_0 = 1891$:

$$
p = \frac{1895 - 1891}{10} = +0.4
$$

Compute the terms using the forward diagonal:

- $y_0 = 46$
- $p\Delta y_0 = (0.4)(20) = 8.0$
- $\frac{p(p-1)}{2}\Delta^2 y_0 = \frac{(0.4)(-0.6)}{2}(-5) = (-0.12)(-5) = +0.6$
- $\frac{p(p-1)(p-2)}{6}\Delta^3 y_0 = \frac{(0.4)(-0.6)(-1.6)}{6}(2) = (0.064)(2) = +0.128$
- $\frac{p(p-1)(p-2)(p-3)}{24}\Delta^4 y_0 = \frac{(0.4)(-0.6)(-1.6)(-2.6)}{24}(-3) = (-0.0416)(-3) = +0.1248$

Sum the terms:

$$
y(1895) = 46 + 8.0 + 0.6 + 0.128 + 0.1248 = 54.8528
$$

$$
\boxed{y(1895) = 54.8528 \text{ thousand} \approx 54\,853}
$$

**Step 3: Estimate for 1925 (Newton's Backward Formula)**

The target 1925 is near the bottom of the table. Choose $x_n = 1931$:

$$
p = \frac{1925 - 1931}{10} = -0.6
$$

Compute the terms using the backward diagonal:

- $y_n = 101$
- $p\nabla y_n = (-0.6)(8) = -4.8$
- $\frac{p(p+1)}{2}\nabla^2 y_n = \frac{(-0.6)(0.4)}{2}(-4) = (-0.12)(-4) = +0.48$
- $\frac{p(p+1)(p+2)}{6}\nabla^3 y_n = \frac{(-0.6)(0.4)(1.4)}{6}(-1) = (-0.056)(-1) = +0.056$
- $\frac{p(p+1)(p+2)(p+3)}{24}\nabla^4 y_n = \frac{(-0.6)(0.4)(1.4)(2.4)}{24}(-3) = (-0.0336)(-3) = +0.1008$

Sum the terms:

$$
y(1925) = 101 - 4.8 + 0.48 + 0.056 + 0.1008 = 96.8368
$$

$$
\boxed{y(1925) = 96.8368 \text{ thousand} \approx 96\,837}
$$

---

## Exam Variants

| Year | Given Table | Target Year / Time | Key Answer |
| :---| :---| :---| :---|
| 2017 Q.5(c) | Census 1921–1961 ($46, 66, 81, 93, 101$) | Estimate population for 1955 ($p = 3.4$) | $\boxed{\text{Population in 1955} \approx 96.8368 \approx 96.84 \text{ thousand}}$ |
| 2020 Q.3(b) | Census 1891–1931 ($46, 66, 81, 93, 101$) | (i) 1895 (Forward) and (ii) 1925 (Backward) | $\boxed{y(1895) = 54.8528 \text{ thousand} \approx 54\,853}$, $\boxed{y(1925) = 96.8368 \text{ thousand} \approx 96\,837}$ |
| 2021 Q.4(c) | Gas sensor $t \in \{1, 3, 5, 7, 9\}$, values $\{24, 120, 336, 720, 1200\}$ | Estimate reading at $t = 10\text{ s}$ | $\boxed{\text{Five points (quartic): } y(10) = 1420.6875 \qquad \text{Four points (cubic): } y(10) = 1716}$ |
| 2024 Q.3(b) | Census 1921–1961 ($46, 66, 81, 93, 101$) | Estimate population for 1995 (Extrapolation) | $\boxed{P(1995) = 20.1888 \text{ thousand (Newton backward difference, all 5 points)}}$ |

---

## 🏆 Golden Questions (Past Exam Archive)

### 🎯 The population of a town in decennial census were as following table in thousand unit. Estimate the population for the year 1955.
> **Appeared:** 2017 Q.5(c) — (04 marks)

**Full Answer:**

Given census table:

| Year | 1921 | 1931 | 1941 | 1951 | 1961 |
| :---: | :---: | :---: | :---: | :---: | :---: |
| Population ($y$, thousands) | 46 | 66 | 81 | 93 | 101 |

Here step size $h = 10$. Choose base year $x_0 = 1921$. For $x = 1955$:

$$
p = \frac{1955 - 1921}{10} = \frac{34}{10} = 3.4
$$

**Difference table:**

| $x$ | $y$ | $\Delta y$ | $\Delta^2 y$ | $\Delta^3 y$ | $\Delta^4 y$ |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1921 | 46 | 20 | $-5$ | 2 | $-3$ |
| 1931 | 66 | 15 | $-3$ | $-1$ | — |
| 1941 | 81 | 12 | $-4$ | — | — |
| 1951 | 93 | 8 | — | — | — |
| 1961 | 101 | — | — | — | — |

**Apply Newton's forward difference formula:**

$$
y(1955) = y_0 + p\Delta y_0 + \frac{p(p-1)}{2}\Delta^2 y_0 + \frac{p(p-1)(p-2)}{6}\Delta^3 y_0 + \frac{p(p-1)(p-2)(p-3)}{24}\Delta^4 y_0
$$

Compute the terms individually:

$$
y_0 = 46
$$

$$
p\Delta y_0 = 3.4(20) = 68.0
$$

$$
\frac{p(p-1)}{2}\Delta^2 y_0 = \frac{(3.4)(2.4)}{2}(-5) = 4.08(-5) = -20.4
$$

$$
\frac{p(p-1)(p-2)}{6}\Delta^3 y_0 = \frac{(3.4)(2.4)(1.4)}{6}(2) = \frac{11.424}{6}(2) = 1.904(2) = 3.808
$$

$$
\frac{p(p-1)(p-2)(p-3)}{24}\Delta^4 y_0 = \frac{(3.4)(2.4)(1.4)(0.4)}{24}(-3) = \frac{4.5696}{24}(-3) = 0.1904(-3) = -0.5712
$$

Sum the terms:

$$
y(1955) = 46 + 68 - 20.4 + 3.808 - 0.5712 = 96.8368
$$

$$
\boxed{\text{Population in 1955} \approx 96.8368 \approx 96.84 \text{ thousand}}
$$

---

### 🎯 You have a gas sensor. It sends a value in 2 seconds. The table of received values is $t = 1, 3, 5, 7, 9$ with values $24, 120, 336, 720, 1200$. What will be the sensor's reading at 10 s?
> **Appeared:** 2021 Q.4(c) — (04 marks)

**Full Answer:**

Given sensor data table ($h = 2\text{ s}$):

| $t$ (s) | 1 | 3 | 5 | 7 | 9 |
| :---: | :---: | :---: | :---: | :---: | :---: |
| Value $y$ | 24 | 120 | 336 | 720 | 1200 |

**Step 1: Construct the difference table:**

| $t$ | $y$ | $\Delta y$ | $\Delta^2 y$ | $\Delta^3 y$ | $\Delta^4 y$ |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | 24 | 96 | 120 | 48 | $-120$ |
| 3 | 120 | 216 | 168 | $-72$ | — |
| 5 | 336 | 384 | 96 | — | — |
| 7 | 720 | 480 | — | — | — |
| 9 | 1200 | — | — | — | — |

**Step 2: Analysis of the readings:**
Notice that the first four points match $(t+1)(t+2)(t+3)$ exactly ($24, 120, 336, 720$). At $t = 9$, this cubic predicts $(10)(11)(12) = 1320$, whereas the recorded value is $1200$. We report both standard interpretations:

**Case A: Using all five points (Quartic Polynomial):**
With $t_0 = 1$ and $p = \frac{10 - 1}{2} = 4.5$:

- $y_0 = 24$
- $p\Delta y_0 = (4.5)(96) = 432$
- $\frac{p(p-1)}{2}\Delta^2 y_0 = \frac{(4.5)(3.5)}{2}(120) = 7.875(120) = 945$
- $\frac{p(p-1)(p-2)}{6}\Delta^3 y_0 = \frac{(4.5)(3.5)(2.5)}{6}(48) = 6.5625(48) = 315$
- $\frac{p(p-1)(p-2)(p-3)}{24}\Delta^4 y_0 = \frac{(4.5)(3.5)(2.5)(1.5)}{24}(-120) = 2.4609375(-120) = -295.3125$

Sum:

$$
y(10) = 24 + 432 + 945 + 315 - 295.3125 = 1420.6875
$$

**Case B: Using the underlying clean cubic (First four points):**
Truncating at the third difference:

$$
y(10) = 24 + 432 + 945 + 315 = 1716
$$

Both interpretations are recognized in the marking scheme:

$$
\boxed{\text{Five points (quartic): } y(10) = 1420.6875 \qquad \text{Four points (cubic): } y(10) = 1716}
$$

---

### 🎯 The population of a town in decennial census were as in the following table in thousand units. Estimate the population for the year 1995.
> **Appeared:** 2024 Q.3(b) — (04 marks)

**Full Answer:**

Given table:

| Year $x$ | 1921 | 1931 | 1941 | 1951 | 1961 |
| :---: | :---: | :---: | :---: | :---: | :---: |
| Population $y$ (thousands) | 46 | 66 | 81 | 93 | 101 |

Here $h = 10$. The target year 1995 lies far beyond the last node $x_n = 1961$.

**Step 1: Difference table:**

| Year | $y$ | $\Delta y$ | $\Delta^2 y$ | $\Delta^3 y$ | $\Delta^4 y$ |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1921 | 46 | 20 | $-5$ | 2 | $-3$ |
| 1931 | 66 | 15 | $-3$ | $-1$ | — |
| 1941 | 81 | 12 | $-4$ | — | — |
| 1951 | 93 | 8 | — | — | — |
| 1961 | 101 | — | — | — | — |

Backward differences at the bottom node ($x_n = 1961$):

$$
y_n = 101, \quad \nabla y_n = 8, \quad \nabla^2 y_n = -4, \quad \nabla^3 y_n = -1, \quad \nabla^4 y_n = -3
$$

**Step 2: Step parameter $p$:**

$$
p = \frac{1995 - 1961}{10} = \frac{34}{10} = 3.4
$$

**Step 3: Evaluate Newton's backward interpolation formula:**

$$
y = y_n + p\nabla y_n + \frac{p(p+1)}{2!}\nabla^2 y_n + \frac{p(p+1)(p+2)}{3!}\nabla^3 y_n + \frac{p(p+1)(p+2)(p+3)}{4!}\nabla^4 y_n
$$

Compute the terms:
- $y_n = 101$
- $p\nabla y_n = (3.4)(8) = 27.2$
- $\frac{p(p+1)}{2}\nabla^2 y_n = \frac{(3.4)(4.4)}{2}(-4) = -29.92$
- $\frac{p(p+1)(p+2)}{6}\nabla^3 y_n = \frac{(3.4)(4.4)(5.4)}{6}(-1) = -13.464$
- $\frac{p(p+1)(p+2)(p+3)}{24}\nabla^4 y_n = \frac{(3.4)(4.4)(5.4)(6.4)}{24}(-3) = -64.6272$

Sum:

$$
y(1995) = 101 + 27.2 - 29.92 - 13.464 - 64.6272 = 20.1888
$$

$$
\boxed{P(1995) = 20.1888 \text{ thousand (Newton backward difference, all 5 points)}}
$$

**Note on physical validity:** Although mathematically correct for the 4th-degree polynomial through all 5 points, this extrapolated value illustrates the instability of high-order polynomial extrapolation far outside the domain ($p = 3.4$). The large negative 4th-difference term forces a sudden drop to $20.19\text{ thousand}$. For a realistic long-term demographic projection, linear least-squares regression is preferred.

---

## ⚡ Exam Tips & Common Mistakes

1. **Verify signs in difference tables.** When subtracting negative numbers in higher orders, be vigilant: $\Delta^2 y_1 - \Delta^2 y_0 = (-3) - (-5) = +2$. A single sign mistake in the second column corrupts every subsequent order.
2. **Backward formula rising factorials.** When using the backward formula, remember that the terms use $(p+1), (p+2), \dots$ not $(p-1), (p-2)$.
3. **Sign of backward $p$ inside the table.** When the target lies inside the table near the end, $x < x_n$, so $p = (x - x_n)/h$ is **negative**. Do not make it positive.
4. **State both cases for corrupted data.** In the gas sensor question (2021 Q.4(c)), always state both the 5-point quartic result ($1420.6875$) and the 4-point cubic result ($1716$) to ensure full credit under any marking scheme.

## 🔗 Related Topics

- [NM-4.6: Lagrange's Interpolation](NM-4.6_Lagranges_Interpolation.md) — interpolation for unequal intervals
- [NM-4.7: Newton's Forward Difference](NM-4.7_Newtons_Forward_Difference.md) — derivation and theoretical foundations of forward differences
- [NM-4_Lower: Regression Theory & Interpolation Methods](NM-4_Lower_Regression_Theory_Interpolation_Methods.md) — Newton's backward and divided difference methods

---

[← Previous: NM-4.7 Newton's Forward Difference](NM-4.7_Newtons_Forward_Difference.md) | [🏠 Index](00_Index.md) | [Next: NM-4_Lower Regression Theory & Interpolation Methods →](NM-4_Lower_Regression_Theory_Interpolation_Methods.md)
