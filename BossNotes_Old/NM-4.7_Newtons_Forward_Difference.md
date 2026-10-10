[← Previous: NM-4.6 Lagrange's Interpolation](NM-4.6_Lagranges_Interpolation.md) | [🏠 Index](00_Index.md) | [Next: NM-4.11 Difference Table Formation →](NM-4.11_Difference_Table_Formation.md)

---

# NM-4.7: Newton's Forward Difference
> **Section:** A (Numerical Methods) | **Priority:** 🔴 | **Exam Frequency:** 6/8 years + CT
> **Sources:** Jain Ch.3 §3.6 (p. 84–86); Fahad Notes Class-05; Raidah Notes p.13–15

## Why This Topic Matters

Newton's forward difference interpolation formula is the standard tool for equally spaced data. It appears in 6 out of 8 semester finals. Exam questions focus on two core requirements: the full theoretical derivation of the formula, and applying it to finite series summation and interpolation tables.

---

## 📝 Key Definitions

> **Newton's Forward Difference Interpolation Formula:**
>
> $$
> y_n(x) = y_0 + p\Delta y_0 + \frac{p(p-1)}{2!}\Delta^2 y_0 + \frac{p(p-1)(p-2)}{3!}\Delta^3 y_0 + \cdots + \frac{p(p-1)(p-2)\dots(p-n+1)}{n!}\Delta^n y_0
> $$
>
> which is *Newton's forward difference interpolation formula* and is useful for interpolation
> *near the beginning* of a set of tabular values. — Jain, §3.6 (p. 84)

> **Dimensionless Step Variable $p$:** "$p = \dfrac{x - x_0}{h}$, where $h = x_1 - x_0$ is the constant spacing between consecutive nodes." — Jain, §3.6 (p. 84)

---

## Core Theory: Derivation of the Forward Difference Formula

### 1. Problem Formulation

Let $y = f(x)$ be tabulated at $n+1$ equidistant points:

$$
x_i = x_0 + ih, \quad i = 0, 1, 2, \dots, n
$$

The step size is constant: $h = x_{i+1} - x_i$. We wish to construct a polynomial $P_n(x)$ of degree at most $n$ such that $P_n(x_i) = y_i$ for all $i = 0, 1, \dots, n$.

Assume the polynomial has the form:

$$
P_n(x) = a_0 + a_1(x - x_0) + a_2(x - x_0)(x - x_1) + a_3(x - x_0)(x - x_1)(x - x_2) + \dots + a_n(x - x_0)\dots(x - x_{n-1})
$$

### 2. Successive Evaluation of Coefficients

We determine the constants $a_0, a_1, \dots, a_n$ by imposing the interpolation conditions at consecutive nodes:

- At $x = x_0$:
  All terms except the first vanish:

$$
y_0 = P_n(x_0) = a_0 \implies a_0 = y_0
$$

- At $x = x_1 = x_0 + h$:

$$
y_1 = P_n(x_1) = a_0 + a_1(x_1 - x_0) = y_0 + a_1 h
$$

$$
a_1 = \frac{y_1 - y_0}{h} = \frac{\Delta y_0}{1!\,h}
$$

- At $x = x_2 = x_0 + 2h$:

$$
y_2 = P_n(x_2) = a_0 + a_1(x_2 - x_0) + a_2(x_2 - x_0)(x_2 - x_1)
$$

$$
y_2 = y_0 + a_1(2h) + a_2(2h)(h) = y_0 + 2\Delta y_0 + 2h^2 a_2
$$

Recall the definition of the second forward difference:

$$
\Delta^2 y_0 = y_2 - 2y_1 + y_0 = y_2 - 2(y_0 + \Delta y_0) + y_0 = y_2 - y_0 - 2\Delta y_0
$$

Equating the expressions gives:

$$
2h^2 a_2 = \Delta^2 y_0 \implies a_2 = \frac{\Delta^2 y_0}{2!\,h^2}
$$

- By mathematical induction, the general coefficient is:

$$
a_k = \frac{\Delta^k y_0}{k!\,h^k}, \qquad k = 0, 1, 2, \dots, n
$$

### 3. Change of Variable to $p$

![A forward difference table for the temperature data 24, 27, 31, 36, 42, with rows y, first difference, second difference, third difference and fourth difference. The leading diagonal of cells, tinted and joined by an arrow, runs from y_0 through the first, second, third and fourth forward differences](diagrams/nm4_newton_forward_difference_path.jpg)

*Figure 4.7: the whole formula in one picture. The forward formula reads only the tinted
diagonal, $y_0$ then $\Delta y_0$ then $\Delta^2 y_0$ and so on. Everything off that diagonal
is either a boundary value or a number the formula never uses.*

Define the dimensionless coordinate:

$$
p = \frac{x - x_0}{h} \implies x = x_0 + ph
$$

Express the linear factors in terms of $p$ and $h$:

$$
x - x_0 = ph
$$

$$
x - x_1 = x_0 + ph - (x_0 + h) = (p - 1)h
$$

$$
x - x_2 = (p - 2)h, \quad \dots, \quad x - x_{k-1} = (p - k + 1)h
$$

The product of the first $k$ factors becomes:

$$
(x - x_0)(x - x_1)\dots(x - x_{k-1}) = (ph)((p-1)h)\dots((p-k+1)h) = p(p-1)\dots(p-k+1)\,h^k
$$

### 4. Assembling the Final Formula

Substitute $a_k$ and the product expression into $P_n(x)$:

$$
a_k(x - x_0)\dots(x - x_{k-1}) = \frac{\Delta^k y_0}{k!\,h^k} \cdot p(p-1)\dots(p-k+1)\,h^k = \frac{p(p-1)\dots(p-k+1)}{k!}\Delta^k y_0
$$

The step sizes $h^k$ cancel out completely:

$$
\boxed{y_n(x) = y_0 + p\Delta y_0 + \frac{p(p-1)}{2!}\Delta^2 y_0 + \frac{p(p-1)(p-2)}{3!}\Delta^3 y_0 + \cdots + \frac{p(p-1)\cdots(p-n+1)}{n!}\Delta^n y_0}
$$

### 5. Operator Derivation (Fast Check)

We can also derive the formula using the shift operator $E$ and forward difference operator $\Delta$:

$$
E = 1 + \Delta
$$

By definition, $E^p y_0 = y(x_0 + ph) = y(x)$. Expanding $(1 + \Delta)^p$ with the binomial theorem:

$$
y(x) = (1 + \Delta)^p y_0 = \left[1 + p\Delta + \frac{p(p-1)}{2!}\Delta^2 + \frac{p(p-1)(p-2)}{3!}\Delta^3 + \dots\right]y_0
$$

Distributing $y_0$ produces the exact same equation.

---

## Worked Example (PYQ 2022 Q.2(c))

Using Newton's forward difference formula, find the sum of cubes:

$$
S_n = 1^3 + 2^3 + 3^3 + \dots + n^3
$$

**Step 1: Set up the finite difference table for $y = r^3$**

Let $r \in \{1, 2, 3, 4, 5\}$ with step size $h = 1$. The origin is $r_0 = 1$, so $u = r - 1$.

| $r$ | $y = r^3$ | $\Delta y$ | $\Delta^2 y$ | $\Delta^3 y$ | $\Delta^4 y$ |
| :--: | :--: | :--: | :--: | :--: | :--: |
| 1 | 1 | 7 | 12 | 6 | 0 |
| 2 | 8 | 19 | 18 | 6 | — |
| 3 | 27 | 37 | 24 | — | — |
| 4 | 64 | 61 | — | — | — |
| 5 | 125 | — | — | — | — |

The differences terminate at $\Delta^3 y_0 = 6$, and all higher differences are zero ($\Delta^4 y = 0$). This confirms that $r^3$ is an exact third-degree polynomial.

**Step 2: Express $r^3$ in factorial polynomials**

With $y_0 = 1, \Delta y_0 = 7, \Delta^2 y_0 = 12, \Delta^3 y_0 = 6$:

$$
y(u) = 1 + 7u + 12\frac{u(u-1)}{2!} + 6\frac{u(u-1)(u-2)}{3!}
$$

$$
y(u) = 1 + 7u + 6u(u-1) + u(u-1)(u-2)
$$

**Step 3: Sum the terms from $u = 0$ to $u = n-1$**

$$
S_n = \sum_{u=0}^{n-1} y(u) = \sum_{u=0}^{n-1} \left[1 + 7u + 6\frac{u(u-1)}{2} \cdot 2 + 6\frac{u(u-1)(u-2)}{6}\right]
$$

Using standard combinatorial summation identities:
- $\sum_{u=0}^{n-1} 1 = n$
- $\sum_{u=0}^{n-1} u = \frac{n(n-1)}{2}$
- $\sum_{u=0}^{n-1} u(u-1) = 2\sum \binom{u}{2} = 2\binom{n}{3} = \frac{2n(n-1)(n-2)}{6} = \frac{n(n-1)(n-2)}{3}$
- $\sum_{u=0}^{n-1} u(u-1)(u-2) = 6\sum \binom{u}{3} = 6\binom{n}{4} = \frac{n(n-1)(n-2)(n-3)}{4}$

Substitute these into the summation:

$$
S_n = n + \frac{7n(n-1)}{2} + 2n(n-1)(n-2) + \frac{n(n-1)(n-2)(n-3)}{4}
$$

Multiply through by $4$ to find a common denominator:

$$
4S_n = 4n + 14n(n-1) + 8n(n-1)(n-2) + n(n-1)(n-2)(n-3)
$$

Expand each polynomial:
- $4n$
- $14n^2 - 14n$
- $8n^3 - 24n^2 + 16n$
- $n^4 - 6n^3 + 11n^2 - 6n$

Combine all terms:

$$
4S_n = n^4 + (-6 + 8)n^3 + (14 - 24 + 11)n^2 + (4 - 14 + 16 - 6)n
$$

$$
4S_n = n^4 + 2n^3 + n^2 = n^2(n^2 + 2n + 1) = n^2(n+1)^2
$$

Dividing by $4$:

$$
\boxed{S_n = \left[\frac{n(n+1)}{2}\right]^2}
$$

---

## Exam Variants

| Year | Topic & Task | Key Result |
| :---| :---| :---|
| 2020 Q.5(a) | Theory: Deduce Newton's forward difference polynomial | Full step-by-step derivation |
| 2021 Q.3(c) / 2023 Q.2(a) | Theory: Derive the forward difference formula | $\boxed{y_n(x) = y_0 + p\Delta y_0 + \frac{p(p-1)}{2!}\Delta^2 y_0 + \frac{p(p-1)(p-2)}{3!}\Delta^3 y_0 + \cdots + \frac{p(p-1)\cdots(p-n+1)}{n!}\Delta^n y_0}$ |
| 2022 Q.2(c) | Sum of cubes $S_n = \sum_{r=1}^n r^3$ using forward differences | $\boxed{S_n = \left[\frac{n(n+1)}{2}\right]^2}$ |
| CT-02A Q.2 | Temperature at $1.5\text{ h}$ and $7\text{ h}$ from $h = 2$ table | $\boxed{T(1.5) = 26.15625 \approx 26.16 \ ^\circ\text{C}}$, $\boxed{T(7) = 38.875 \approx 38.88 \ ^\circ\text{C}}$ |

---

## 🏆 Golden Questions (Past Exam Archive)

### 🎯 Deduce the Newton's forward difference interpolating polynomial.
> **Appeared:** 2020 Q.5(a) — (04 marks)

**Full Answer:**

Let $n+1$ equidistant data points $(x_0, y_0), (x_1, y_1), \dots, (x_n, y_n)$ have constant step size $h = x_{i+1} - x_i$.

**Step 1. Newton's general divided difference polynomial:**
For arbitrary nodes, the interpolating polynomial is:

$$
P_n(x) = f[x_0] + f[x_0, x_1](x - x_0) + f[x_0, x_1, x_2](x - x_0)(x - x_1) + \dots
$$

**Step 2. Relation to forward differences:**
When the nodes are equally spaced with step $h$, divided differences collapse into finite forward differences:

$$
f[x_0, x_1, \dots, x_k] = \frac{\Delta^k y_0}{k!\,h^k}
$$

**Step 3. Dimensionless coordinate $p$:**
Let $x = x_0 + ph$, where $p = \frac{x - x_0}{h}$. The linear factors become:

$$
x - x_0 = ph
$$

$$
x - x_1 = (p - 1)h, \quad \dots, \quad x - x_{k-1} = (p - k + 1)h
$$

Their product is:

$$
\prod_{j=0}^{k-1} (x - x_j) = p(p-1)\dots(p-k+1)\,h^k
$$

**Step 4. Substitute into the polynomial:**

$$
P_n(x) = y_0 + \sum_{k=1}^n \frac{\Delta^k y_0}{k!\,h^k} \cdot \left[p(p-1)\dots(p-k+1)\,h^k\right]
$$

Cancelling the $h^k$ terms yields Newton's forward difference formula:

$$
y_n(x) = y_0 + p\Delta y_0 + \frac{p(p-1)}{2!}\Delta^2 y_0 + \frac{p(p-1)(p-2)}{3!}\Delta^3 y_0 + \dots + \frac{p(p-1)\dots(p-n+1)}{n!}\Delta^n y_0
$$

The formula is valid and most accurate near the beginning of the table ($0 \le p \le 1$).

---

### 🎯 Derive the Newton's forward interpolation formula: $y_n(x) = y_0 + p\Delta y_0 + \frac{p(p-1)}{2!}\Delta^2 y_0 + \frac{p(p-1)(p-2)}{3!}\Delta^3 y_0 + \cdots$
> **Appeared:** 2021 Q.3(c), 2023 Q.2(a) — (04 marks)

**Full Answer:**

Let $y = f(x)$ take values $y_0, y_1, \dots, y_n$ at $n+1$ equidistant points $x_i = x_0 + ih$.

Assume an $n$-th degree polynomial:

$$
P_n(x) = a_0 + a_1(x - x_0) + a_2(x - x_0)(x - x_1) + \dots + a_n(x - x_0)\dots(x - x_{n-1})
$$

1. At $x = x_0$:

   $$
   y_0 = a_0 \implies a_0 = y_0
   $$

2. At $x = x_1 = x_0 + h$:

   $$
   y_1 = a_0 + a_1 h = y_0 + a_1 h \implies a_1 = \frac{y_1 - y_0}{h} = \frac{\Delta y_0}{1!\,h}
   $$

3. At $x = x_2 = x_0 + 2h$:

   $$
   y_2 = a_0 + a_1(2h) + a_2(2h)(h) = y_0 + 2\Delta y_0 + 2h^2 a_2
   $$

   Since $\Delta^2 y_0 = y_2 - 2y_1 + y_0 = y_2 - y_0 - 2\Delta y_0$, we obtain:

   $$
   2h^2 a_2 = \Delta^2 y_0 \implies a_2 = \frac{\Delta^2 y_0}{2!\,h^2}
   $$

4. By induction:

   $$
   a_k = \frac{\Delta^k y_0}{k!\,h^k}, \qquad k = 0, 1, \dots, n
   $$

Let $p = \frac{x - x_0}{h}$, then $(x - x_0)(x - x_1)\dots(x - x_{k-1}) = p(p-1)\dots(p-k+1)h^k$.

Substituting $a_k$ and cancelling $h^k$:

$$
\boxed{y_n(x) = y_0 + p\Delta y_0 + \frac{p(p-1)}{2!}\Delta^2 y_0 + \frac{p(p-1)(p-2)}{3!}\Delta^3 y_0 + \cdots + \frac{p(p-1)\cdots(p-n+1)}{n!}\Delta^n y_0}
$$

---

### 🎯 Use Newton's Forward/Backward Interpolation Formula to estimate the temperature at 1.5 and 7 hours.
> **Appeared:** CT-02A Q.2 — (05 marks)

**Full Answer:**

Given temperature measurements:

| Time $t$ (hours) | 0 | 2 | 4 | 6 | 8 |
| :-- | :--: | :--: | :--: | :--: | :--: |
| Temperature $T$ (°C) | 24 | 27 | 31 | 36 | 42 |

The step size is uniform: $h = 2\text{ hours}$.

**Step 1: Construct the difference table**

| $t$ | $T$ | $\Delta T$ | $\Delta^2 T$ | $\Delta^3 T$ |
| :--: | :--: | :--: | :--: | :--: |
| 0 | 24 | 3 | 1 | 0 |
| 2 | 27 | 4 | 1 | 0 |
| 4 | 31 | 5 | 1 | — |
| 6 | 36 | 6 | — | — |
| 8 | 42 | — | — | — |

Because all third differences are zero ($\Delta^3 T = 0$), the data follow an exact quadratic function.

**Step 2: Estimate at $t = 1.5\text{ h}$ (Newton's Forward Formula)**
Since $1.5$ is near the beginning of the table, choose $t_0 = 0$:

$$
p = \frac{t - t_0}{h} = \frac{1.5 - 0}{2} = 0.75
$$

$$
T(1.5) = T_0 + p\Delta T_0 + \frac{p(p-1)}{2!}\Delta^2 T_0 = 24 + (0.75)(3) + \frac{(0.75)(0.75 - 1)}{2}(1)
$$

$$
T(1.5) = 24 + 2.25 + \frac{(0.75)(-0.25)}{2} = 26.25 - 0.09375 = 26.15625\ ^\circ\text{C}
$$

$$
\boxed{T(1.5) = 26.15625 \approx 26.16 \ ^\circ\text{C}}
$$

**Step 3: Estimate at $t = 7\text{ h}$ (Newton's Backward Formula)**
Since $7$ is near the end of the table, choose $t_n = 8$:

$$
p = \frac{t - t_n}{h} = \frac{7 - 8}{2} = -0.5
$$

$$
T(7) = T_n + p\nabla T_n + \frac{p(p+1)}{2!}\nabla^2 T_n = 42 + (-0.5)(6) + \frac{(-0.5)(-0.5 + 1)}{2}(1)
$$

$$
T(7) = 42 - 3.0 + \frac{(-0.5)(0.5)}{2} = 39.0 - 0.125 = 38.875\ ^\circ\text{C}
$$

$$
\boxed{T(7) = 38.875 \approx 38.88 \ ^\circ\text{C}}
$$

---

## ⚡ Exam Tips & Common Mistakes

1. **Keep step size $h$ uniform.** Newton's forward and backward formulas require constant $h$. If data points have uneven steps, you must use Lagrange's formula or Newton's divided differences.
2. **Select forward vs. backward correctly.** Use the forward formula when the target point lies in the upper half of the table ($0 \le p \le 1$). Use the backward formula when the target lies in the lower half of the table ($-1 \le p \le 0$).
3. **Falling factorials.** Remember that the forward formula uses falling products: $p(p-1)(p-2)\dots$ In contrast, the backward formula uses rising products: $p(p+1)(p+2)\dots$
4. **Spot polynomial degree in the difference table.** If differences of order $k$ are constant, then $\Delta^{k+1} y = 0$. The underlying function is a polynomial of degree $k$, and the interpolation formula is exact.

## 🔗 Related Topics

- [NM-4.6: Lagrange's Interpolation](NM-4.6_Lagranges_Interpolation.md) — interpolation when step sizes are unequal
- [NM-4.11: Difference Table Formation](NM-4.11_Difference_Table_Formation.md) — constructing and verifying forward, backward, and divided difference tables
- [NM-4_Lower: Regression Theory & Interpolation Methods](NM-4_Lower_Regression_Theory_Interpolation_Methods.md) — Newton's backward and divided difference formulas

---

[← Previous: NM-4.6 Lagrange's Interpolation](NM-4.6_Lagranges_Interpolation.md) | [🏠 Index](00_Index.md) | [Next: NM-4.11 Difference Table Formation →](NM-4.11_Difference_Table_Formation.md)
