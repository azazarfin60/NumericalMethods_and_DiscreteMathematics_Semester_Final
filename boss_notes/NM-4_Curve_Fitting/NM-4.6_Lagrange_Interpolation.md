[← Previous: NM-4.5 Linear Interpolation](NM-4.5_Linear_Interpolation.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: NM-4.7 Newton Forward Difference →](NM-4.7_Newton_Forward_Difference.md)

---

# NM-4.6: Lagrange Interpolation

> 🔴 **Priority:** Critical | **Tested:** 7/8 years + Class Tests | **Typical marks:** 3–5

## What This Is (and Why It Matters)

If you only master one interpolation formula for your semester final, make it Lagrange. It appears in almost every single exam paper.

Most interpolation formulas (like Newton forward or backward difference) require your data points to have perfectly equal steps ($h = \text{constant}$). But real-world data points are almost never equally spaced. Lagrange interpolation does not care about spacing at all. It takes any random collection of points, builds a custom set of blending curves (called basis polynomials), and adds them together to produce a single polynomial that passes through every point. Even better, you do not need to construct a difference table.

---

## 📝 Key Definitions

> **Lagrange's Interpolation Formula:** "Given the $(n + 1)$ points $(x_0, y_0)$, $(x_1, y_1)$, ..., $(x_n, y_n)$ where the values of $x$ need not necessarily be equally spaced, we wish to find a polynomial of degree $n$, say $L_n(x)$, such that $L_n(x_i) = y(x_i) = y_i, i = 0, 1, \dots, n$." -- Jain, §3.9.1 (p. 101)
>
> **In simple words:** A formula that connects $n+1$ points of any spacing with a smooth curve of degree $n$ by giving each point its own custom weighting function.

> **Kronecker Delta Property of Basis Polynomials:** "$l_i(x_j) = \begin{cases} 1, & \text{if } i = j \\ 0, & \text{if } i \ne j \end{cases}$." -- Jain, §3.9.1 (p. 102)
>
> **In simple words:** Each weighting function $L_i(x)$ is cleverly designed to equal exactly $1$ at its own point $x_i$, and flat zero at every other data point $x_j$. When you add them up, each point only speaks for itself.

> **Partition of Unity Property:** "$\sum_{i=0}^n l_i(x) = 1$ for all $x$." -- Jain, §3.9.1 (p. 102)
>
> **In simple words:** At any point along the curve, the sum of all the weighting factors must equal exactly 1. This is your built-in exam superpower: if your computed weights do not add up to 1, you caught a math mistake before handing in your paper.

---

## The Core Idea: How the Formula Works

Given $n+1$ distinct points $(x_0, y_0), (x_1, y_1), \dots, (x_n, y_n)$, we want a polynomial $P_n(x)$ such that:

$$
P_n(x_i) = y_i \quad \text{for every } i = 0, 1, \dots, n
$$

Lagrange writes this polynomial as a weighted sum:

$$
P_n(x) = y_0 L_0(x) + y_1 L_1(x) + \dots + y_n L_n(x) = \sum_{i=0}^n y_i L_i(x)
$$

### Constructing the Basis Polynomials $L_i(x)$

How do we build $L_i(x)$ so that it equals $1$ at $x_i$ and $0$ at all other nodes?

1. **Make it zero at other nodes:** The numerator must contain factors $(x - x_j)$ for every node except $x_i$:
   $$
   (x - x_0)(x - x_1)\dots(x - x_{i-1})(x - x_{i+1})\dots(x - x_n)
   $$
   If you plug in any $x = x_j$ (where $j \ne i$), one of those factors becomes $(x_j - x_j) = 0$, killing the whole term.
2. **Make it equal 1 at $x_i$:** Divide the numerator by the exact same product evaluated at $x = x_i$:
   $$
   L_i(x) = \prod_{\substack{j=0 \\ j \ne i}}^n \frac{x - x_j}{x_i - x_j}
   $$
   When $x = x_i$, every factor is $\frac{x_i - x_j}{x_i - x_j} = 1$, so the whole product equals $1$.

![Lagrange interpolation in two panels. Left: the four basis polynomials for the nodes (2,18), (4,26), (7,43) and (10,60), each rising to 1 at its own node and crossing zero at the other three. Right: the interpolating polynomial passing through all four tabulated points, with the queried value y(5) = 31.25 marked by a star](../diagrams/nm4_lagrange_basis_polynomials.jpg)

### Why the Partition of Unity Check Saves Your Grade

Always compute the sum of your basis weights before multiplying by the $y_i$ values:

$$
L_0(x) + L_1(x) + \dots + L_n(x) = 1.0
$$

If your sum equals $0.92$ or $1.15$, you made a sign slip in the denominator. Stop and fix it right there.

---

## 🔧 Worked Example

> **From:** 2021 Q.3(d) / 2023 Q.2(b) -- [Marks: 04]

**The question:** Find $y(2)$ from the following data using Lagrange's formula:

| $x$ | 0 | 1 | 3 | 4 | 5 |
| :---: | :---: | :---: | :---: | :---: | :---: |
| $y$ | 0 | 1 | 81 | 256 | 625 |

**Let's solve this step by step like a tutor.**

Here we have 5 data points ($n = 4$, 4th-degree polynomial) and our target is $x = 2$.
Notice the spacing: steps are $1, 2, 1, 1$. Unequal spacing means Newton forward differences cannot be used, but Lagrange handles it with ease.

**Step 1: Compute the 5 basis polynomials at $x = 2$**

- For $L_0(2)$ (skip $x_0 = 0$):
  $$
  L_0(2) = \frac{(2-1)(2-3)(2-4)(2-5)}{(0-1)(0-3)(0-4)(0-5)} = \frac{(1)(-1)(-2)(-3)}{(-1)(-3)(-4)(-5)} = \frac{-6}{60} = -0.1
  $$

- For $L_1(2)$ (skip $x_1 = 1$):
  $$
  L_1(2) = \frac{(2-0)(2-3)(2-4)(2-5)}{(1-0)(1-3)(1-4)(1-5)} = \frac{(2)(-1)(-2)(-3)}{(1)(-2)(-3)(-4)} = \frac{-12}{-24} = +0.5
  $$

- For $L_2(2)$ (skip $x_2 = 3$):
  $$
  L_2(2) = \frac{(2-0)(2-1)(2-4)(2-5)}{(3-0)(3-1)(3-4)(3-5)} = \frac{(2)(1)(-2)(-3)}{(3)(2)(-1)(-2)} = \frac{12}{12} = +1.0
  $$

- For $L_3(2)$ (skip $x_3 = 4$):
  $$
  L_3(2) = \frac{(2-0)(2-1)(2-3)(2-5)}{(4-0)(4-1)(4-3)(4-5)} = \frac{(2)(1)(-1)(-3)}{(4)(3)(1)(-1)} = \frac{6}{-12} = -0.5
  $$

- For $L_4(2)$ (skip $x_4 = 5$):
  $$
  L_4(2) = \frac{(2-0)(2-1)(2-3)(2-4)}{(5-0)(5-1)(5-3)(5-4)} = \frac{(2)(1)(-1)(-2)}{(5)(4)(2)(1)} = \frac{4}{40} = +0.1
  $$

**Step 2: The partition of unity check**
Let's add the weights together:

$$
\sum L_i = -0.1 + 0.5 + 1.0 - 0.5 + 0.1 = 1.0
$$

It equals exactly 1. We know with 100% certainty our weights are correct.

**Step 3: Assemble the final answer**
Multiply each $y_i$ by its weight:

$$
y(2) = 0(-0.1) + 1(0.5) + 81(1.0) + 256(-0.5) + 625(0.1)
$$

$$
y(2) = 0 + 0.5 + 81.0 - 128.0 + 62.5 = 16
$$

$$
\boxed{y(2) = 16}
$$

*Tutor insight:* Notice that the data follows $y = x^4$ ($0^4=0, 1^4=1, 3^4=81, 4^4=256, 5^4=625$). At $x = 2$, $2^4 = 16$. The polynomial recovered the exact underlying quartic curve.

---

## 🏆 Past Exam Questions

### 2018 Q.3(a): Explain the Use of Lagrange's Formula [03 Marks]

**The question:** Explain the use of Lagrange's interpolation formula.

**Let's answer this clearly:**
Lagrange's interpolation formula estimates values of an unknown function from discrete tabular data $(x_i, y_i)$.
It is specifically used when:
1. **The data points are unequally spaced:** This is its main advantage over Newton forward and backward formulas, which require constant step size $h$.
2. **Order of points does not matter:** Because the basis functions are symmetric in the data points, points do not need to be sorted.
3. **No difference tables required:** Values are evaluated directly in one single algebraic expression.

Limitations: Adding a new data point forces you to recompute all basis polynomials from scratch.

---

### 2018 Q.3(c): 3-Point Lagrange Interpolation [03 Marks]

**The question:** Find $f(2.5)$ from the given data, $x$: 1, 2, 3 and $f(x)$: 0, 1, 8.

**Let's solve this step by step.**

Points: $(x_0, y_0) = (1, 0)$, $(x_1, y_1) = (2, 1)$, $(x_2, y_2) = (3, 8)$. Target: $x = 2.5$.

Compute basis polynomials:

$$
L_0(2.5) = \frac{(2.5 - 2)(2.5 - 3)}{(1 - 2)(1 - 3)} = \frac{(0.5)(-0.5)}{(-1)(-2)} = \frac{-0.25}{2} = -0.125
$$

$$
L_1(2.5) = \frac{(2.5 - 1)(2.5 - 3)}{(2 - 1)(2 - 3)} = \frac{(1.5)(-0.5)}{(1)(-1)} = \frac{-0.75}{-1} = +0.75
$$

$$
L_2(2.5) = \frac{(2.5 - 1)(2.5 - 2)}{(3 - 1)(3 - 2)} = \frac{(1.5)(0.5)}{(2)(1)} = \frac{0.75}{2} = +0.375
$$

Check sum: $-0.125 + 0.75 + 0.375 = 1.0$.

Assemble $f(2.5)$:

$$
f(2.5) = 0(-0.125) + 1(0.75) + 8(0.375) = 0 + 0.75 + 3.0 = 3.75
$$

$$
\boxed{f(2.5) = 3.75}
$$

---

### 2019 Q.4(b): Robot Arm Quadratic Path [04 Marks]

**The question:** A robot arm with a rapid laser scanner is doing a quick quality check on holes drilled in a $15'' \times 10''$ rectangular plate. The centers of the holes in the plate describe the path the arm needs to take, and the hole centers are located on a Cartesian coordinate system given by $(2, 7.2)$, $(4.25, 7.1)$, and $(5.25, 6.0)$. If the laser is traversing from $x = 2$ to $x = 4.25$ to $x = 5.25$ in a quadratic path, what is the value of $y$ at $x = 4.00$ using a curve fitting technique?

**Let's solve this step by step.**

Nodes: $(x_0, y_0) = (2, 7.2)$, $(x_1, y_1) = (4.25, 7.1)$, $(x_2, y_2) = (5.25, 6.0)$. Target: $x = 4.00$.

Compute weights at $x = 4.00$:

$$
L_0 = \frac{(4 - 4.25)(4 - 5.25)}{(2 - 4.25)(2 - 5.25)} = \frac{(-0.25)(-1.25)}{(-2.25)(-3.25)} = \frac{0.3125}{7.3125} \approx 0.042735
$$

$$
L_1 = \frac{(4 - 2)(4 - 5.25)}{(4.25 - 2)(4.25 - 5.25)} = \frac{(2)(-1.25)}{(2.25)(-1.0)} = \frac{-2.5}{-2.25} = \frac{10}{9} \approx 1.111111
$$

$$
L_2 = \frac{(4 - 2)(4 - 4.25)}{(5.25 - 2)(5.25 - 4.25)} = \frac{(2)(-0.25)}{(3.25)(1.0)} = \frac{-0.5}{3.25} \approx -0.153846
$$

Check sum: $0.042735 + 1.111111 - 0.153846 = 1.000000$.

Assemble $y(4.00)$:

$$
y(4.00) = 7.2(0.042735) + 7.1(1.111111) + 6.0(-0.153846)
$$

$$
y(4.00) = 0.307692 + 7.888889 - 0.923077 = 7.273504\ \text{in.}
$$

$$
\boxed{y(4.00) = 7.2735\ \text{in.}}
$$

---

### 2021 Q.3(b): Newton vs. Lagrange [03 Marks]

**The question:** Differentiate between Newton's interpolation and Lagrange's interpolation.

**Comparison table:**

| Feature | Newton's Interpolation | Lagrange's Interpolation |
| :-- | :-- | :-- |
| **Mathematical structure** | Incremental sum of divided differences | Direct weighted sum of basis polynomials |
| **Adding a new data point** | Keeps all previous work; adds one new term | Must recompute all basis polynomials from scratch |
| **Spacing requirement** | Fast for equal spacing; requires table for unequal | Directly handles unequal spacing with no table |
| **Evaluation speed** | Fast $O(n)$ once table is built | Costs $O(n^2)$ for each evaluated point |

$$
\boxed{\text{Newton updates and reuses; Lagrange rebuilds once and is spacing-agnostic}}
$$

---

### 2024 Q.2(c): Method Description, Pros and Cons [04 Marks]

**The question:** Describe the Lagrange interpolation method. What are its advantages and disadvantages?

**Let's write out the description and points:**

**Description:** Given $n+1$ points $(x_0, y_0), \dots, (x_n, y_n)$, Lagrange constructs a unique polynomial of degree at most $n$:

$$
P_n(x) = \sum_{i=0}^n y_i \prod_{\substack{j=0 \\ j \ne i}}^n \frac{x - x_j}{x_i - x_j}
$$

**Advantages:**
1. Handles unequally spaced data directly without requiring difference tables.
2. Mathematically symmetric in the data points (ordering does not matter).
3. Compact closed-form representation.

**Disadvantages:**
1. Computationally inefficient ($O(n^2)$ per point).
2. Adding another data point requires rebuilding the entire formula from scratch.
3. Prone to Runge's phenomenon (wild edge oscillations) for high-degree polynomials.

$$
\boxed{P_n(x) = \sum_{i=0}^{n} y_i \prod_{j \neq i} \frac{x - x_j}{x_i - x_j}}
$$

---

### CT-02A Q.1: Water Pollutant Concentration [04 Marks]

**The question:** Use the Lagrange Interpolation Formula to estimate the concentration at 5 km from distance $x = [2, 4, 7, 10]\text{ km}$ and concentration $C = [18, 26, 43, 60]\text{ mg/L}$.

**Let's solve this cleanly:**
At $x = 5$:
- $L_0(5) = \frac{(5-4)(5-7)(5-10)}{(2-4)(2-7)(2-10)} = \frac{(1)(-2)(-5)}{(-2)(-5)(-8)} = \frac{10}{-80} = -0.125$
- $L_1(5) = \frac{(5-2)(5-7)(5-10)}{(4-2)(4-7)(4-10)} = \frac{(3)(-2)(-5)}{(2)(-3)(-6)} = \frac{30}{36} = \frac{5}{6} \approx 0.833333$
- $L_2(5) = \frac{(5-2)(5-4)(5-10)}{(7-2)(7-4)(7-10)} = \frac{(3)(1)(-5)}{(5)(3)(-3)} = \frac{-15}{-45} = \frac{1}{3} \approx 0.333333$
- $L_3(5) = \frac{(5-2)(5-4)(5-7)}{(10-2)(10-4)(10-7)} = \frac{(3)(1)(-2)}{(8)(6)(3)} = \frac{-6}{144} = -\frac{1}{24} \approx -0.041667$

Sum check: $-0.125 + \frac{5}{6} + \frac{1}{3} - \frac{1}{24} = 1.0$.

Assemble:

$$
C(5) = 18(-0.125) + 26\left(\frac{5}{6}\right) + 43\left(\frac{1}{3}\right) + 60\left(-\frac{1}{24}\right) = -2.25 + 21.6667 + 14.3333 - 2.5 = 31.25\ \text{mg/L}
$$

$$
\boxed{C(5) = 31.25 \ \text{mg/L}}
$$

---

## ⚡ Quick Review

**The method in one sentence:** Build a basis polynomial for each point that equals 1 at its own point and 0 at all others, check that their sum equals 1, and multiply by the $y$ values.

**The formula you must memorize:**
$$
L_i(x) = \prod_{j \ne i} \frac{x - x_j}{x_i - x_j}, \qquad P_n(x) = \sum_{i=0}^n y_i L_i(x)
$$

**The most common exam mistake:** Forgetting the partition of unity check and letting a sign slip in the denominator ruin the entire numerical answer.

**Time estimate in exam:** ~6 minutes for a 3-point problem; ~8 minutes for a 4-point problem.

---

## 🔗 Connected Topics

- [← NM-4.5: Linear Interpolation](NM-4.5_Linear_Interpolation.md) -- the 2-point special case of Lagrange's formula.
- [→ NM-4.7: Newton Forward Difference](NM-4.7_Newton_Forward_Difference.md) -- the faster alternative when data points are equally spaced.
- [NM-4.9: Divided Difference](NM-4.9_Divided_Difference.md) -- Newton's alternative for unequal intervals that allows adding new points without recomputing old ones.

---

[← Previous: NM-4.5 Linear Interpolation](NM-4.5_Linear_Interpolation.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: NM-4.7 Newton Forward Difference →](NM-4.7_Newton_Forward_Difference.md)
