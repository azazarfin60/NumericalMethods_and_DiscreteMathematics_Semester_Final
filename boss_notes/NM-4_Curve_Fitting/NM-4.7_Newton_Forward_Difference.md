[← Previous: NM-4.6 Lagrange Interpolation](NM-4.6_Lagrange_Interpolation.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: NM-4.8 Newton Backward Difference →](NM-4.8_Newton_Backward_Difference.md)

---

# NM-4.7: Newton's Forward Difference

> 🔴 **Priority:** Critical | **Tested:** 6/8 years + Class Tests | **Typical marks:** 4–5

## What This Is (and Why It Matters)

When your data points have perfectly equal spacing ($h = x_{i+1} - x_i = \text{constant}$), Lagrange interpolation feels clumsy because you are calculating long products of fractions by hand. Newton realized that for equally spaced data, you can build a simple pyramid of differences called a difference table.

Newton's forward difference formula reads right along the top edge of that difference pyramid. It is the premier tool for estimating values near the beginning of a data table. The exam tests this subtopic relentlessly: either asking for the full mathematical proof from scratch, or asking you to evaluate an unknown point, or even using it to derive classic series formulas like the sum of cubes $1^3 + 2^3 + \dots + n^3$.

---

## 📝 Key Definitions

> **Newton's Forward Difference Interpolation Formula:**
>
> $$
> y_n(x) = y_0 + p\Delta y_0 + \frac{p(p-1)}{2!}\Delta^2 y_0 + \frac{p(p-1)(p-2)}{3!}\Delta^3 y_0 + \cdots + \frac{p(p-1)\dots(p-n+1)}{n!}\Delta^n y_0
> $$
>
> which is *Newton's forward difference interpolation formula* and is useful for interpolation *near the beginning* of a set of tabular values. -- Jain, §3.6 (p. 84)
>
> **In simple words:** A formula that starts at your first data point $y_0$ and adds correction terms using the top forward differences from your table, with coefficients that look just like binomial coefficients.

> **Dimensionless Step Variable $p$:** "$p = \dfrac{x - x_0}{h}$, where $h = x_1 - x_0$ is the constant spacing between consecutive nodes." -- Jain, §3.6 (p. 84)
>
> **In simple words:** A counter that tells you how many steps $h$ your target $x$ is past your starting point $x_0$. For example, if your steps are 2 hours each and you want the value at 1.5 hours past zero, $p = 1.5 / 2 = 0.75$.

---

## The Core Idea: Complete Derivation

Examiners frequently ask you to derive this formula. Here is the cleanest, most bulletproof way to write it down on an exam sheet.

### 1. Problem Setup

Let $y = f(x)$ be tabulated at $n+1$ equidistant points $x_i = x_0 + ih$ with step size $h$. We want an $n$-th degree polynomial $P_n(x)$ passing through all points.

Assume the polynomial is expanded in factorial factors:

$$
P_n(x) = a_0 + a_1(x - x_0) + a_2(x - x_0)(x - x_1) + a_3(x - x_0)(x - x_1)(x - x_2) + \dots + a_n(x - x_0)\dots(x - x_{n-1})
$$

### 2. Evaluating the Coefficients $a_k$

We plug in the known nodes one by one:

1. **At $x = x_0$:**
   Every term after $a_0$ has a factor $(x_0 - x_0) = 0$:
   $$
   y_0 = P_n(x_0) = a_0 \implies a_0 = y_0
   $$

2. **At $x = x_1 = x_0 + h$:**
   $$
   y_1 = a_0 + a_1(x_1 - x_0) = y_0 + a_1 h
   $$
   $$
   a_1 = \frac{y_1 - y_0}{h} = \frac{\Delta y_0}{1!\,h}
   $$

3. **At $x = x_2 = x_0 + 2h$:**
   $$
   y_2 = a_0 + a_1(2h) + a_2(2h)(h) = y_0 + 2\Delta y_0 + 2h^2 a_2
   $$
   Recall that the second forward difference is:
   $$
   \Delta^2 y_0 = y_2 - 2y_1 + y_0 = y_2 - 2(y_0 + \Delta y_0) + y_0 = y_2 - y_0 - 2\Delta y_0
   $$
   Equating terms gives:
   $$
   2h^2 a_2 = \Delta^2 y_0 \implies a_2 = \frac{\Delta^2 y_0}{2!\,h^2}
   $$

4. **By mathematical induction:**
   $$
   a_k = \frac{\Delta^k y_0}{k!\,h^k} \quad \text{for all } k = 0, 1, \dots, n
   $$

### 3. Transforming to the Step Variable $p$

Let $x = x_0 + ph$, so $p = \frac{x - x_0}{h}$. Look at what happens to the distance factors:

$$
x - x_0 = ph
$$

$$
x - x_1 = x_0 + ph - (x_0 + h) = (p - 1)h
$$

$$
x - x_2 = (p - 2)h, \quad \dots, \quad x - x_{k-1} = (p - k + 1)h
$$

Multiply the first $k$ factors together:

$$
(x - x_0)(x - x_1)\dots(x - x_{k-1}) = p(p-1)\dots(p-k+1)\,h^k
$$

### 4. Assembling the Formula

Now plug $a_k$ and the product into the $k$-th term of $P_n(x)$:

$$
a_k(x - x_0)\dots(x - x_{k-1}) = \left(\frac{\Delta^k y_0}{k!\,h^k}\right) \cdot \left[p(p-1)\dots(p-k+1)\,h^k\right]
$$

The step sizes $h^k$ cancel out in the numerator and denominator:

$$
= \frac{p(p-1)\dots(p-k+1)}{k!}\Delta^k y_0
$$

Summing all terms yields Newton's forward difference interpolation formula:

$$
\boxed{y_n(x) = y_0 + p\Delta y_0 + \frac{p(p-1)}{2!}\Delta^2 y_0 + \frac{p(p-1)(p-2)}{3!}\Delta^3 y_0 + \cdots + \frac{p(p-1)\cdots(p-n+1)}{n!}\Delta^n y_0}
$$

### How to Read the Difference Table

![A forward difference table for the temperature data 24, 27, 31, 36, 42, with rows y, first difference, second difference, third difference and fourth difference. The leading diagonal of cells, tinted and joined by an arrow, runs from y_0 through the first, second, third and fourth forward differences](../diagrams/nm4_newton_forward_difference_path.jpg)

The forward formula only reads the **top descending diagonal**: $y_0 \to \Delta y_0 \to \Delta^2 y_0 \to \Delta^3 y_0 \dots$ You ignore all other entries in the table.

---

## 🔧 Worked Example

> **From:** 2022 Q.2(c) -- [Marks: 05]

**The question:** Using Newton's forward difference formula, find the sum of cubes:

$$
S_n = 1^3 + 2^3 + 3^3 + \dots + n^3
$$

**Let's solve this step by step like a tutor.**

**Step 1: Set up a finite difference table for $y = r^3$**
Let $r \in \{1, 2, 3, 4, 5\}$ with step size $h = 1$. Let the origin be $r_0 = 1$, so $u = r - 1$.

| $r$ | $y = r^3$ | $\Delta y$ | $\Delta^2 y$ | $\Delta^3 y$ | $\Delta^4 y$ |
| :--: | :--: | :--: | :--: | :--: | :--: |
| 1 | 1 | 7 | 12 | 6 | 0 |
| 2 | 8 | 19 | 18 | 6 | -- |
| 3 | 27 | 37 | 24 | -- | -- |
| 4 | 64 | 61 | -- | -- | -- |
| 5 | 125 | -- | -- | -- | -- |

Look at the third difference: $\Delta^3 y = 6 = \text{constant}$, and $\Delta^4 y = 0$. This confirms that $r^3$ is a 3rd-degree polynomial.

**Step 2: Express $r^3$ in terms of factorial polynomials**
Using Newton's forward formula with $y_0 = 1, \Delta y_0 = 7, \Delta^2 y_0 = 12, \Delta^3 y_0 = 6$:

$$
y(u) = 1 + 7u + 12\frac{u(u-1)}{2!} + 6\frac{u(u-1)(u-2)}{3!}
$$

$$
y(u) = 1 + 7u + 6u(u-1) + u(u-1)(u-2)
$$

**Step 3: Sum the terms from $u = 0$ to $u = n-1$**
We use standard combinatorial summation identities:
- $\sum_{u=0}^{n-1} 1 = n$
- $\sum_{u=0}^{n-1} u = \frac{n(n-1)}{2}$
- $\sum_{u=0}^{n-1} u(u-1) = 2\sum \binom{u}{2} = 2\binom{n}{3} = \frac{n(n-1)(n-2)}{3}$
- $\sum_{u=0}^{n-1} u(u-1)(u-2) = 6\sum \binom{u}{3} = 6\binom{n}{4} = \frac{n(n-1)(n-2)(n-3)}{4}$

Substitute these into the summation:

$$
S_n = n + 7\frac{n(n-1)}{2} + 6\frac{n(n-1)(n-2)}{3} + \frac{n(n-1)(n-2)(n-3)}{4}
$$

Multiply through by 4:

$$
4S_n = 4n + 14n(n-1) + 8n(n-1)(n-2) + n(n-1)(n-2)(n-3)
$$

Expand term by term:
- $4n$
- $14n^2 - 14n$
- $8n^3 - 24n^2 + 16n$
- $n^4 - 6n^3 + 11n^2 - 6n$

Combine all terms:

$$
4S_n = n^4 + (-6 + 8)n^3 + (14 - 24 + 11)n^2 + (4 - 14 + 16 - 6)n = n^4 + 2n^3 + n^2
$$

Factor the right side:

$$
4S_n = n^2(n^2 + 2n + 1) = n^2(n+1)^2
$$

Divide by 4:

$$
\boxed{S_n = \left[\frac{n(n+1)}{2}\right]^2}
$$

---

## 🏆 Past Exam Questions

### 2020 Q.5(a) / 2021 Q.3(c) / 2023 Q.2(a): Formula Derivation [04 Marks]

**The question:** Derive the Newton's forward interpolation formula:
$$
y_n(x) = y_0 + p\Delta y_0 + \frac{p(p-1)}{2!}\Delta^2 y_0 + \frac{p(p-1)(p-2)}{3!}\Delta^3 y_0 + \cdots + \frac{p(p-1)\cdots(p-n+1)}{n!}\Delta^n y_0
$$

**Full derivation:** See the step-by-step proof in Section "The Core Idea" above. The key points to show:
1. Expansion in factorial products $P_n(x) = \sum a_k \prod_{j=0}^{k-1}(x - x_j)$.
2. Substituting $x_0, x_1, x_2$ to show $a_k = \frac{\Delta^k y_0}{k!\,h^k}$.
3. Substituting $p = \frac{x - x_0}{h}$ and cancelling $h^k$.

$$
\boxed{y_n(x) = y_0 + p\Delta y_0 + \frac{p(p-1)}{2!}\Delta^2 y_0 + \frac{p(p-1)(p-2)}{3!}\Delta^3 y_0 + \cdots + \frac{p(p-1)\cdots(p-n+1)}{n!}\Delta^n y_0}
$$

---

### CT-02A Q.2: Temperature Interpolation [10 Marks]

**The question:** A weather station records the temperature every 2 hours.

| Time (hours) | 0 | 2 | 4 | 6 | 8 |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Temperature (°C)** | 24 | 27 | 31 | 36 | 42 |

The meteorologist wants to estimate the temperature at $1.5$ and $7$ hours. Use Newton's (Forward/Backward) Interpolation Formula to estimate the temperature.

**Let's solve this step by step.**

The step size is constant: $h = 2\text{ hours}$.

**Step 1: Construct the difference table**

| $t$ | $T$ | $\Delta T$ | $\Delta^2 T$ | $\Delta^3 T$ |
| :--: | :--: | :--: | :--: | :--: |
| 0 | 24 | 3 | 1 | 0 |
| 2 | 27 | 4 | 1 | 0 |
| 4 | 31 | 5 | 1 | -- |
| 6 | 36 | 6 | -- | -- |
| 8 | 42 | -- | -- | -- |

All third differences are zero ($\Delta^3 T = 0$), so the function is a clean quadratic curve.

**Step 2: Estimate at $t = 1.5\text{ h}$ (Newton Forward)**
Since $1.5$ is near the top of the table, choose $t_0 = 0$:

$$
p = \frac{t - t_0}{h} = \frac{1.5 - 0}{2} = 0.75
$$

Apply Newton's forward formula:

$$
T(1.5) = T_0 + p\Delta T_0 + \frac{p(p-1)}{2}\Delta^2 T_0 = 24 + (0.75)(3) + \frac{(0.75)(0.75 - 1)}{2}(1)
$$

$$
T(1.5) = 24 + 2.25 + \frac{(0.75)(-0.25)}{2} = 26.25 - 0.09375 = 26.15625\ ^\circ\text{C}
$$

$$
\boxed{T(1.5) = 26.15625 \approx 26.16 \ ^\circ\text{C}}
$$

**Step 3: Estimate at $t = 7\text{ h}$ (Newton Backward)**
Since $7$ is near the bottom of the table, choose $t_n = 8$:

$$
p = \frac{t - t_n}{h} = \frac{7 - 8}{2} = -0.5
$$

Apply Newton's backward formula:

$$
T(7) = T_n + p\nabla T_n + \frac{p(p+1)}{2}\nabla^2 T_n = 42 + (-0.5)(6) + \frac{(-0.5)(-0.5 + 1)}{2}(1)
$$

$$
T(7) = 42 - 3.0 + \frac{(-0.5)(0.5)}{2} = 39.0 - 0.125 = 38.875\ ^\circ\text{C}
$$

$$
\boxed{T(7) = 38.875 \approx 38.88 \ ^\circ\text{C}}
$$

---

## ⚡ Quick Review

**The method in one sentence:** For equally spaced data near the start of a table, calculate step $p = (x - x_0)/h$ and evaluate along the top forward diagonal using falling factorials $p(p-1)\dots$

**The formula you must memorize:**
$$
y(x) = y_0 + p\Delta y_0 + \frac{p(p-1)}{2!}\Delta^2 y_0 + \frac{p(p-1)(p-2)}{3!}\Delta^3 y_0 + \dots
$$

**The most common exam mistake:** Using the forward formula for a point near the bottom of the table. If your target is in the lower half of the table, switch to Newton's backward formula!

**Time estimate in exam:** ~6 minutes to build the table and compute the estimate.

---

## 🔗 Connected Topics

- [← NM-4.6: Lagrange Interpolation](NM-4.6_Lagrange_Interpolation.md) -- when data points do not have equal steps $h$.
- [→ NM-4.8: Newton Backward Difference](NM-4.8_Newton_Backward_Difference.md) -- the sister formula for points near the end of the table.
- [NM-4.11: Difference Tables](NM-4.11_Difference_Tables.md) -- comprehensive difference table construction and census forecasting.

---

[← Previous: NM-4.6 Lagrange Interpolation](NM-4.6_Lagrange_Interpolation.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: NM-4.8 Newton Backward Difference →](NM-4.8_Newton_Backward_Difference.md)
