[← Previous: NM-4.3 Non-Linear Regression](NM-4.3_Non_Linear_Regression.md) | [🏠 Index](00_Index.md) | [Next: NM-4.7 Newton's Forward Difference →](NM-4.7_Newtons_Forward_Difference.md)

---

# NM-4.6: Lagrange's Interpolation
> **Section:** A (Numerical Methods) | **Priority:** 🔴 | **Exam Frequency:** 7/8 years + CT
> **Sources:** Jain Ch.3 §3.9.1 (p. 101–103); Fahad Notes Class-05; Raidah Notes p.10–12

## Why This Topic Matters

Lagrange's interpolation is the most tested interpolation method in the entire course. It appears in 7 out of 8 semester finals and in class tests. The formula handles unevenly spaced data directly without requiring finite difference tables. Exams test both theoretical derivation and multi-point numerical problems.

---

## 📝 Key Definitions

> **Lagrange's Interpolation Formula:** "Given the $(n + 1)$ points $(x_0, y_0)$, $(x_1, y_1)$, ..., $(x_n, y_n)$ where the values of $x$ need not necessarily be equally spaced, we wish to find a polynomial of degree $n$, say $L_n(x)$, such that $L_n(x_i) = y(x_i) = y_i, i = 0, 1, \dots, n$." — Jain, §3.9.1 (p. 101)

> **Kronecker Delta Property of Basis Polynomials:** "$l_i(x_j) = \begin{cases} 1, & \text{if } i = j \\ 0, & \text{if } i \ne j \end{cases}$." — Jain, §3.9.1 (p. 102)

> **Partition of Unity Property:** "$\sum_{i=0}^n l_i(x) = 1$ for all $x$." — Jain, §3.9.1 (p. 102)

---

## Core Theory: Construction and Properties of the Lagrange Polynomial

### 1. The Core Idea

Given $n+1$ distinct points $(x_0, y_0), (x_1, y_1), \dots, (x_n, y_n)$, there exists a unique polynomial $P_n(x)$ of degree at most $n$ that passes through every point:

$$
P_n(x_i) = y_i \quad \text{for } i = 0, 1, \dots, n
$$

Lagrange constructs this polynomial as a linear combination of basis polynomials $L_i(x)$:

$$
P_n(x) = \sum_{i=0}^n y_i L_i(x)
$$

### 2. The Lagrange Basis Polynomials

Each basis polynomial $L_i(x)$ is designed to satisfy two specific conditions:

1. $L_i(x_i) = 1$ at its own node.
2. $L_i(x_j) = 0$ at all other nodes ($j \ne i$).

![Lagrange interpolation in two panels. Left: the four basis polynomials for the nodes (2,18), (4,26), (7,43) and (10,60), each rising to 1 at its own node and crossing zero at the other three. Right: the interpolating polynomial passing through all four tabulated points, with the queried value y(5) = 31.25 marked by a star](diagrams/nm4_lagrange_basis_polynomials.jpg)

*Figure 4.6: the left panel is the Kronecker delta property made visible. Each $L_i$ is a
cardinal function, 1 at its own node and 0 everywhere else on the table. The right panel is
the sum $\sum y_i L_i(x)$, which is forced through every point because at node $x_k$ only
$L_k$ survives.*

To make $L_i(x) = 0$ at every $x_j$ where $j \ne i$, the numerator must contain the product:

$$
\prod_{\substack{j=0 \\ j \ne i}}^n (x - x_j) = (x - x_0)\dots(x - x_{i-1})(x - x_{i+1})\dots(x - x_n)
$$

To make $L_i(x_i) = 1$, we divide by the value of this product evaluated at $x = x_i$:

$$
L_i(x) = \prod_{\substack{j=0 \\ j \ne i}}^n \frac{x - x_j}{x_i - x_j}
$$

When evaluated at $x = x_k$:
- If $k \ne i$, one factor in the numerator is $(x_k - x_k) = 0$, so $L_i(x_k) = 0$.
- If $k = i$, every factor is $\frac{x_i - x_j}{x_i - x_j} = 1$, so $L_i(x_i) = 1$.

Therefore, substituting $x = x_k$ into $P_n(x)$:

$$
P_n(x_k) = \sum_{i=0}^n y_i L_i(x_k) = y_k(1) + \sum_{i \ne k} y_i(0) = y_k
$$

The polynomial matches every given point exactly.

### 3. Key Properties and Checks

1. **Partition of unity:** The sum of all basis polynomials equals $1$ at every $x$:

$$
\sum_{i=0}^n L_i(x) = 1
$$

Always compute this sum as an arithmetic sanity check before multiplying by $y_i$.
2. **Spacing-agnostic:** The spacing between nodes $x_i$ can be completely arbitrary. No common difference $h$ is required.
3. **Interpolation error:** If $f(x)$ has $n+1$ continuous derivatives, the truncation error is:

$$
R_n(x) = f(x) - P_n(x) = \frac{f^{(n+1)}(\xi)}{(n+1)!}\prod_{i=0}^n (x - x_i)
$$

for some $\xi$ in the interval containing all $x_i$ and $x$.

### 4. Newton vs. Lagrange Comparison

| Comparison Feature | Newton's Interpolation | Lagrange's Interpolation |
| :-- | :-- | :-- |
| **Mathematical structure** | Incremental sum of divided differences | Direct weighted sum of products |
| **Adding a new data point** | Retains all previous terms; adds one new term | Must recompute all basis polynomials |
| **Unequal spacing** | Requires divided differences table | Works directly without extra machinery |
| **Equal spacing** | Fast forward/backward difference tables | Ignores equal spacing benefits |
| **Evaluation work** | $O(n)$ after table setup | $O(n^2)$ arithmetic operations |
| **Stability** | Better when evaluated near edges | Degrades rapidly for high degrees |

---

## Worked Example (PYQ 2021 Q.3(d) / 2023 Q.2(b))

Find $y(2)$ from the following data using Lagrange's formula:

| $x$ | 0 | 1 | 3 | 4 | 5 |
| :---: | :---: | :---: | :---: | :---: | :---: |
| $y$ | 0 | 1 | 81 | 256 | 625 |

Here $n = 4$ (five points) and the target is $x = 2$.

**Step 1: Compute the five Lagrange basis weights at $x = 2$**

$$
L_0(2) = \frac{(2-1)(2-3)(2-4)(2-5)}{(0-1)(0-3)(0-4)(0-5)} = \frac{(1)(-1)(-2)(-3)}{(-1)(-3)(-4)(-5)} = \frac{-6}{60} = -\frac{1}{10} = -0.1
$$

$$
L_1(2) = \frac{(2-0)(2-3)(2-4)(2-5)}{(1-0)(1-3)(1-4)(1-5)} = \frac{(2)(-1)(-2)(-3)}{(1)(-2)(-3)(-4)} = \frac{-12}{-24} = \frac{1}{2} = 0.5
$$

$$
L_2(2) = \frac{(2-0)(2-1)(2-4)(2-5)}{(3-0)(3-1)(3-4)(3-5)} = \frac{(2)(1)(-2)(-3)}{(3)(2)(-1)(-2)} = \frac{12}{12} = 1.0
$$

$$
L_3(2) = \frac{(2-0)(2-1)(2-3)(2-5)}{(4-0)(4-1)(4-3)(4-5)} = \frac{(2)(1)(-1)(-3)}{(4)(3)(1)(-1)} = \frac{6}{-12} = -\frac{1}{2} = -0.5
$$

$$
L_4(2) = \frac{(2-0)(2-1)(2-3)(2-4)}{(5-0)(5-1)(5-3)(5-4)} = \frac{(2)(1)(-1)(-2)}{(5)(4)(2)(1)} = \frac{4}{40} = \frac{1}{10} = 0.1
$$

**Step 2: Check the sum of weights**

$$
\sum_{i=0}^4 L_i(2) = -0.1 + 0.5 + 1.0 - 0.5 + 0.1 = 1.0 \quad \text{(Verified!)}
$$

**Step 3: Assemble the solution**

$$
y(2) = \sum_{i=0}^4 y_i L_i(2) = 0(-0.1) + 1(0.5) + 81(1.0) + 256(-0.5) + 625(0.1)
$$

$$
y(2) = 0 + 0.5 + 81 - 128 + 62.5 = 16
$$

$$
\boxed{y(2) = 16}
$$

Notice that the data points follow $y = x^4$ ($0^4 = 0, 1^4 = 1, 3^4 = 81, 4^4 = 256, 5^4 = 625$). The fifth point on this curve is $2^4 = 16$, which confirms the result.

---

## Exam Variants

| Year | Target & Given Points | Key Answer |
| :---| :---| :---|
| 2018 Q.3(a) | Theory: Explain the use of Lagrange's formula | Four main advantages and limitations |
| 2018 Q.3(c) | Find $f(2.5)$ from $(1, 0), (2, 1), (3, 8)$ | $\boxed{f(2.5) = 3.75}$ |
| 2019 Q.4(b) | Robot arm path: $(2, 7.2), (4.25, 7.1), (5.25, 6.0)$, find $y(4.00)$ | $\boxed{y(4.00) = 7.2735\ \text{in.}}$ |
| 2021 Q.3(b) | Theory: Differentiate Newton vs. Lagrange | $\boxed{\text{Newton updates and reuses; Lagrange rebuilds once and is spacing-agnostic}}$ |
| 2021 Q.3(d) / 2023 Q.2(b) | $x \in \{0, 1, 3, 4, 5\}$, $y \in \{0, 1, 81, 256, 625\}$, find $y(2)$ | $\boxed{y(2) = 16}$ |
| 2024 Q.2(c) | Theory: Describe method, advantages and disadvantages | $\boxed{P_n(x) = \sum_{i=0}^{n} y_i \prod_{j \neq i} \frac{x - x_j}{x_i - x_j}}$ |
| CT-02A Q.1 | Pollutant concentration at $5\text{ km}$ from $(2, 18), (4, 26), (7, 43), (10, 60)$ | $\boxed{C(5) = 31.25 \ \text{mg/L}}$ |

---

## 🏆 Golden Questions (Past Exam Archive)

### 🎯 Explain the use of Lagrange's interpolation formula.
> **Appeared:** 2018 Q.3(a) — (03 marks)

**Full Answer:**

**Use:** Lagrange's formula estimates an intermediate value $f(x)$ at a point $x$ within the range of a tabulated set $(x_i, f_i)$, without requiring the tabulated abscissae to be equally spaced.

**The formula:** For $n+1$ points:

$$
f(x) \approx \sum_{i=0}^n f_i \prod_{\substack{j=0 \\ j \ne i}}^n \frac{x - x_j}{x_i - x_j}
$$

**Why it is used:**

1. **Unequal spacing is allowed.** This is its principal advantage over Newton's forward and backward formulas, which assume a common tabular spacing $h$. Experimental data with uneven sampling intervals are handled directly.
2. **Order of points is irrelevant.** The formula is symmetric in the data points. Permuting the points leaves the resulting polynomial unchanged.
3. **No difference table needed.** The entire calculation is written and evaluated in a single step, without building forward, backward, or divided-difference tables.
4. **Analytic error estimate.** With $n+1$ points, the error is:

$$
R_n(x) = \frac{f^{(n+1)}(\xi)}{(n+1)!}\prod_{i=0}^n (x - x_i)
$$

**Limitations:** Adding a new data point requires recalculating all basis polynomials. It also requires $O(n^2)$ operations for each evaluation point.

---

### 🎯 Find $f(2.5)$ from the given data, $x$: 1, 2, 3 and $f(x)$: 0, 1, 8.
> **Appeared:** 2018 Q.3(c) — (03 marks)

**Full Answer:**

Given data:

| $x$ | 1 | 2 | 3 |
| :---: | :---: | :---: | :---: |
| $f(x)$ | 0 | 1 | 8 |

With three points ($x_0 = 1, x_1 = 2, x_2 = 3$ and $f_0 = 0, f_1 = 1, f_2 = 8$), the second-degree Lagrange formula is:

$$
f(x) = \frac{(x - x_1)(x - x_2)}{(x_0 - x_1)(x_0 - x_2)}f_0 + \frac{(x - x_0)(x - x_2)}{(x_1 - x_0)(x_1 - x_2)}f_1 + \frac{(x - x_0)(x - x_1)}{(x_2 - x_0)(x_2 - x_1)}f_2
$$

Evaluate each basis term at $x = 2.5$:

$$
L_0(2.5) = \frac{(2.5 - 2)(2.5 - 3)}{(1 - 2)(1 - 3)} = \frac{(0.5)(-0.5)}{(-1)(-2)} = \frac{-0.25}{2} = -0.125
$$

$$
L_1(2.5) = \frac{(2.5 - 1)(2.5 - 3)}{(2 - 1)(2 - 3)} = \frac{(1.5)(-0.5)}{(1)(-1)} = \frac{-0.75}{-1} = 0.75
$$

$$
L_2(2.5) = \frac{(2.5 - 1)(2.5 - 2)}{(3 - 1)(3 - 2)} = \frac{(1.5)(0.5)}{(2)(1)} = \frac{0.75}{2} = 0.375
$$

Check sum: $L_0 + L_1 + L_2 = -0.125 + 0.75 + 0.375 = 1.0$.

Assemble:

$$
f(2.5) = 0(-0.125) + 1(0.75) + 8(0.375) = 0 + 0.75 + 3.0 = 3.75
$$

$$
\boxed{f(2.5) = 3.75}
$$

---

### 🎯 A robot arm with a rapid laser scanner is doing a quick quality check on holes drilled in a $15'' \times 10''$ rectangular plate. The centers of the holes in the plate describe the path the arm needs to take, and the hole centers are located on a Cartesian coordinate system given by $(2, 7.2)$, $(4.25, 7.1)$, and $(5.25, 6.0)$. If the laser is traversing from $x = 2$ to $x = 4.25$ to $x = 5.25$ in a quadratic path, what is the value of $y$ at $x = 4.00$ using a curve fitting technique?
> **Appeared:** 2019 Q.4(b) — (04 marks)

**Full Answer:**

Three points specify a unique quadratic curve. We construct the second-degree Lagrange interpolating polynomial through:

$$
(x_0, y_0) = (2, 7.2), \quad (x_1, y_1) = (4.25, 7.1), \quad (x_2, y_2) = (5.25, 6.0)
$$

At target $x = 4.00$:

$$
L_0 = \frac{(4 - 4.25)(4 - 5.25)}{(2 - 4.25)(2 - 5.25)} = \frac{(-0.25)(-1.25)}{(-2.25)(-3.25)} = \frac{0.3125}{7.3125} = 0.04273504
$$

$$
L_1 = \frac{(4 - 2)(4 - 5.25)}{(4.25 - 2)(4.25 - 5.25)} = \frac{(2)(-1.25)}{(2.25)(-1)} = \frac{-2.5}{-2.25} = 1.11111111
$$

$$
L_2 = \frac{(4 - 2)(4 - 4.25)}{(5.25 - 2)(5.25 - 4.25)} = \frac{(2)(-0.25)}{(3.25)(1)} = \frac{-0.5}{3.25} = -0.15384615
$$

Check: $L_0 + L_1 + L_2 = 0.04273504 + 1.11111111 - 0.15384615 = 1.00000000$.

Assemble $y(4.00)$:

$$
y(4.00) = 7.2(0.04273504) + 7.1(1.11111111) + 6.0(-0.15384615)
$$

$$
y(4.00) = 0.30769231 + 7.88888889 - 0.92307692 = 7.27350427
$$

$$
\boxed{y(4.00) = 7.2735\ \text{in.}}
$$

---

### 🎯 Differentiate between Newton's interpolation and Lagrange's interpolation.
> **Appeared:** 2021 Q.3(b) — (03 marks)

**Full Answer:**

| Comparison Factor | Newton's Interpolation | Lagrange's Interpolation |
| :-- | :-- | :-- |
| **Mathematical form** | Successive sum of difference terms | Single weighted sum of basis polynomials |
| **Expansion basis** | Divided differences or forward differences | Basis products $\prod_{j \ne i} \frac{x - x_j}{x_i - x_j}$ |
| **Adding a new data node** | Old work is retained; adds one new term | Must recompute all basis terms |
| **Equally spaced nodes** | Fast finite difference tables ($h$) | Works, but does not exploit equal spacing |
| **Unequally spaced nodes** | Requires divided differences | Natural and direct without difference table |
| **Computational cost** | $O(n)$ after table setup | $O(n^2)$ direct evaluations |
| **Position in table** | Forward at start, backward at end | Symmetric across the whole interval |

$$
\boxed{\text{Newton updates and reuses; Lagrange rebuilds once and is spacing-agnostic}}
$$

---

### 🎯 Describe the Lagrange interpolation method. What are its advantages and disadvantages?
> **Appeared:** 2024 Q.2(c) — (04 marks)

**Full Answer:**

**Description:** Given $n+1$ distinct points $(x_0, y_0), \dots, (x_n, y_n)$, there is a unique polynomial of degree at most $n$ passing through all of them. Lagrange writes this polynomial directly as a linear combination of basis functions:

$$
P_n(x) = \sum_{i=0}^n y_i L_i(x), \qquad L_i(x) = \prod_{\substack{j=0 \\ j \ne i}}^n \frac{x - x_j}{x_i - x_j}
$$

Each basis polynomial satisfies $L_i(x_i) = 1$ and $L_i(x_j) = 0$ for $j \ne i$. Thus, each term contributes $y_i$ at its own node and zero at all other nodes.

**Advantages:**
1. No system of linear equations needs to be solved.
2. Directly handles unequally spaced points without difference tables.
3. The formula is symmetric in the data points.
4. Compact closed-form representation suitable for analytic manipulations.

**Disadvantages:**
1. Evaluating $P_n(x)$ costs $O(n^2)$ operations.
2. Adding a new data point requires recomputing all basis polynomials from scratch.
3. Sensitive to round-off error when points are clustered close together.
4. Suffers from Runge's phenomenon (wild oscillations near boundaries) for high polynomial degrees.

$$
\boxed{P_n(x) = \sum_{i=0}^{n} y_i \prod_{j \neq i} \frac{x - x_j}{x_i - x_j}}
$$

---

### 🎯 Use the Lagrange Interpolation Formula to estimate the concentration at 5 km.
> **Appeared:** CT-02A Q.1 — (04 marks)

**Full Answer:**

Given water pollutant concentration data:

| Distance $x$ (km) | 2 | 4 | 7 | 10 |
| :-- | :--: | :--: | :--: | :--: |
| Concentration $C$ (mg/L) | 18 | 26 | 43 | 60 |

The nodes are unequally spaced ($x_0 = 2, x_1 = 4, x_2 = 7, x_3 = 10$). We estimate $C(5)$ using Lagrange's third-degree polynomial.

Compute the basis polynomials at $x = 5$:

$$
L_0(5) = \frac{(5-4)(5-7)(5-10)}{(2-4)(2-7)(2-10)} = \frac{(1)(-2)(-5)}{(-2)(-5)(-8)} = \frac{10}{-80} = -\frac{1}{8} = -0.125
$$

$$
L_1(5) = \frac{(5-2)(5-7)(5-10)}{(4-2)(4-7)(4-10)} = \frac{(3)(-2)(-5)}{(2)(-3)(-6)} = \frac{30}{36} = \frac{5}{6} \approx 0.833333
$$

$$
L_2(5) = \frac{(5-2)(5-4)(5-10)}{(7-2)(7-4)(7-10)} = \frac{(3)(1)(-5)}{(5)(3)(-3)} = \frac{-15}{-45} = \frac{1}{3} \approx 0.333333
$$

$$
L_3(5) = \frac{(5-2)(5-4)(5-7)}{(10-2)(10-4)(10-7)} = \frac{(3)(1)(-2)}{(8)(6)(3)} = \frac{-6}{144} = -\frac{1}{24} \approx -0.041667
$$

**Sum check:**

$$
L_0 + L_1 + L_2 + L_3 = -\frac{1}{8} + \frac{5}{6} + \frac{1}{3} - \frac{1}{24} = \frac{-3 + 20 + 8 - 1}{24} = \frac{24}{24} = 1.0 \quad \text{✓}
$$

**Estimate concentration at $x = 5\text{ km}$:**

$$
P(5) = 18\left(-\frac{1}{8}\right) + 26\left(\frac{5}{6}\right) + 43\left(\frac{1}{3}\right) + 60\left(-\frac{1}{24}\right)
$$

$$
P(5) = -2.25 + 21.6667 + 14.3333 - 2.5 = 31.25\ \text{mg/L}
$$

$$
\boxed{C(5) = 31.25 \ \text{mg/L}}
$$

---

## ⚡ Exam Tips & Common Mistakes

1. **Always perform the partition of unity check.** Before multiplying $L_i$ by $y_i$, add the computed weights together: $\sum L_i = 1$. If their sum is not exactly $1$, you have a sign error in one of the factors.
2. **Watch the signs in the denominators.** For $L_i$, every denominator factor has the form $(x_i - x_j)$. The pivot $x_i$ appears first in every factor. When $x_i < x_j$, that factor is negative. Count the total negative signs carefully.
3. **Never skip factor listing.** Write out each $(x - x_j)/(x_i - x_j)$ explicitly with numbers before combining into fractions. This secures step marks even if an arithmetic slip occurs.
4. **Unequal intervals signal Lagrange.** Whenever you see unequal intervals (like $0, 1, 3, 4, 5$ or $2, 4, 7, 10$), immediately use Lagrange or divided differences. Never attempt Newton forward/backward differences on unequal steps.

## 🔗 Related Topics

- [NM-4.1: Curve Fitting Concepts](NM-4.1_Curve_Fitting_Concepts.md) — criteria for when to use Lagrange vs. least squares
- [NM-4.7: Newton's Forward Difference](NM-4.7_Newtons_Forward_Difference.md) — interpolation for equally spaced data points
- [NM-4_Lower: Regression Theory & Interpolation Methods](NM-4_Lower_Regression_Theory_Interpolation_Methods.md) — Newton's divided differences and central difference formulas

---

[← Previous: NM-4.3 Non-Linear Regression](NM-4.3_Non_Linear_Regression.md) | [🏠 Index](00_Index.md) | [Next: NM-4.7 Newton's Forward Difference →](NM-4.7_Newtons_Forward_Difference.md)
