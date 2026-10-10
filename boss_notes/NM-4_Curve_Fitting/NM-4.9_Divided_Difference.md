[← Previous: NM-4.8 Newton Backward Difference](NM-4.8_Newton_Backward_Difference.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: NM-4.10 Gauss and Stirling →](NM-4.10_Gauss_and_Stirling.md)

---

# NM-4.9: Newton's Divided Difference Interpolation

> 🟠 **Priority:** Secondary | **Tested:** 3 appearances (2019, 2020, 2022) | **Typical marks:** 3–5

## What This Is (and Why It Matters)

What happens when your data points have unequal spacing, but you also want to find the full algebraic equation of the polynomial (like $f(x) = x^4 - 3x^3 + 5x^2 - 6$) rather than just evaluating a single number? Or what if you want to be able to add new data points later without throwing away all your previous calculations?

Lagrange's formula cannot do that easily: expanding Lagrange basis polynomials into a standard polynomial takes pages of algebra, and adding a new point forces you to recalculate every single fraction. Newton's divided difference method solves both problems. It brings the convenience of difference tables to unequally spaced data, and it is completely unaffected by whether your data points are in sorted numerical order.

---

## 📝 Key Definitions

> **Divided Differences:** "The first divided difference of $f(x)$ for the arguments $x_0, x_1$ is defined as $f[x_0, x_1] = \dfrac{f(x_1) - f(x_0)}{x_1 - x_0}$. In general, the $k$-th divided difference is $f[x_0, x_1, \dots, x_k] = \dfrac{f[x_1, \dots, x_k] - f[x_0, \dots, x_{k-1}]}{x_k - x_0}$." -- Jain, §3.10 (p. 104)
>
> **In simple words:** Just like finite differences, but at each stage you divide the jump in $y$ by the total span in $x$ between the outermost points.

> **Symmetry of Divided Differences:** "Divided differences are symmetric functions of their arguments, i.e., the value of a divided difference is independent of the order in which the arguments are arranged." -- Jain, §3.10 (p. 105)
>
> **In simple words:** You can shuffle your data points in any order you want ($x_1$ before $x_0$, or jumbled up), and the divided difference value will never change: $f[x_0, x_1] = f[x_1, x_0]$.

---

## The Core Idea: Table Construction and Polynomial Expansion

### 1. The Divided Difference Table

Given data points $(x_0, y_0), (x_1, y_1), \dots$:
- **First order:** $f[x_0, x_1] = \dfrac{y_1 - y_0}{x_1 - x_0}$
- **Second order:** $f[x_0, x_1, x_2] = \dfrac{f[x_1, x_2] - f[x_0, x_1]}{x_2 - x_0}$ (notice the denominator is $x_2 - x_0$, spanning across two intervals!)
- **Third order:** $f[x_0, x_1, x_2, x_3] = \dfrac{f[x_1, x_2, x_3] - f[x_0, x_1, x_2]}{x_3 - x_0}$ (denominator spans across three intervals!)

### 2. Newton's Divided Difference Polynomial

Once you build the table, read the top diagonal just like Newton's forward difference formula:

$$
P_n(x) = f[x_0] + f[x_0, x_1](x - x_0) + f[x_0, x_1, x_2](x - x_0)(x - x_1) + \dots + f[x_0, \dots, x_n](x - x_0)\dots(x - x_{n-1})
$$

### The Two Major Superpowers of Divided Differences

1. **Permutation invariance:** If the exam question lists points out of numerical order (for example, 2020 Q.5(b) lists $t = 0.5$ before $t = 0.2$), you do not need to reorder the table. Divided differences naturally produce the exact same unique polynomial.
2. **Incremental updates:** If an experimenter collects one more point $(x_{n+1}, y_{n+1})$, you do not restart from scratch. All previous polynomial terms remain identical; you simply calculate one new row at the bottom of your table and add one extra term.

---

## 🔧 Worked Example

> **From:** 2019 Q.5(c) -- [Marks: 05]

**The question:** Using Newton's general interpolation formula find $f(x)$ as a polynomial in $x$ for the following table. Also, determine $f(3.5)$ using the polynomial.

| $x$ | $-1$ | 0 | 3 | 6 | 7 |
| :---: | :---: | :---: | :---: | :---: | :---: |
| $f(x)$ | 3 | $-6$ | 39 | 822 | 1611 |

**Let's solve this step by step like a tutor.**

Notice the intervals: steps are $1, 3, 3, 1$. Unequal spacing means divided differences is the perfect tool.

**Step 1: Construct the divided difference table**

- **Order 0 ($y$ values):** $3, -6, 39, 822, 1611$
- **Order 1:**
  - $f[x_0, x_1] = \frac{-6 - 3}{0 - (-1)} = \frac{-9}{1} = -9$
  - $f[x_1, x_2] = \frac{39 - (-6)}{3 - 0} = \frac{45}{3} = 15$
  - $f[x_2, x_3] = \frac{822 - 39}{6 - 3} = \frac{783}{3} = 261$
  - $f[x_3, x_4] = \frac{1611 - 822}{7 - 6} = \frac{789}{1} = 789$
- **Order 2:**
  - $f[x_0, x_1, x_2] = \frac{15 - (-9)}{3 - (-1)} = \frac{24}{4} = 6$
  - $f[x_1, x_2, x_3] = \frac{261 - 15}{6 - 0} = \frac{246}{6} = 41$
  - $f[x_2, x_3, x_4] = \frac{789 - 261}{7 - 3} = \frac{528}{4} = 132$
- **Order 3:**
  - $f[x_0, x_1, x_2, x_3] = \frac{41 - 6}{6 - (-1)} = \frac{35}{7} = 5$
  - $f[x_1, x_2, x_3, x_4] = \frac{132 - 41}{7 - 0} = \frac{91}{7} = 13$
- **Order 4:**
  - $f[x_0, x_1, x_2, x_3, x_4] = \frac{13 - 5}{7 - (-1)} = \frac{8}{8} = 1$

**Step 2: Collect the top diagonal coefficients**
- $f[x_0] = 3$
- $f[x_0, x_1] = -9$
- $f[x_0, x_1, x_2] = 6$
- $f[x_0, x_1, x_2, x_3] = 5$
- $f[x_0, x_1, x_2, x_3, x_4] = 1$

**Step 3: Build and expand the polynomial**

$$
f(x) = 3 - 9(x - (-1)) + 6(x - (-1))(x - 0) + 5(x - (-1))(x - 0)(x - 3) + 1(x - (-1))(x - 0)(x - 3)(x - 6)
$$

$$
f(x) = 3 - 9(x + 1) + 6x(x + 1) + 5x(x + 1)(x - 3) + x(x + 1)(x - 3)(x - 6)
$$

Let's expand each product carefully:
1. $x(x + 1)(x - 3)(x - 6) = (x^2 + x)(x^2 - 9x + 18) = x^4 - 8x^3 + 9x^2 + 18x$
2. $5x(x + 1)(x - 3) = 5(x^3 - 2x^2 - 3x) = 5x^3 - 10x^2 - 15x$
3. $6x(x + 1) = 6x^2 + 6x$
4. $-9(x + 1) = -9x - 9$
5. Constant term $= 3$

Combine like powers of $x$:
- $x^4$ term: $1x^4$
- $x^3$ term: $(-8 + 5)x^3 = -3x^3$
- $x^2$ term: $(9 - 10 + 6)x^2 = 5x^2$
- $x$ term: $(18 - 15 + 6 - 9)x = 0x$
- Constant: $3 - 9 = -6$

So the full algebraic polynomial is:

$$
\boxed{f(x) = x^4 - 3x^3 + 5x^2 - 6}
$$

**Step 4: Evaluate at $x = 3.5$**
Substitute $x = 3.5$ directly into the simplified polynomial:

$$
f(3.5) = (3.5)^4 - 3(3.5)^3 + 5(3.5)^2 - 6
$$

$$
(3.5)^4 = 150.0625, \qquad -3(3.5)^3 = -3(42.875) = -128.625, \qquad 5(3.5)^2 = 5(12.25) = 61.25
$$

$$
f(3.5) = 150.0625 - 128.625 + 61.25 - 6 = 76.6875
$$

$$
\boxed{f(3.5) = 76.6875}
$$

---

## 🏆 Past Exam Questions

### 2020 Q.5(b): Signal Estimation with Unsorted Data [05 Marks]

**The question:** Using Newton's divided difference interpolating polynomial estimate the value of signal $s(t)$ at $t = 2.25$ sec for the following tabulated values:

| $t$ | 0.5 | 0.2 | 1.4 | 2.2 | 3.0 |
| :---: | :---: | :---: | :---: | :---: | :---: |
| $s(t)$ | $-10.25$ | $-3.768$ | $5.976$ | $28.972$ | $79.0$ |

**Let's solve this step by step.**

Notice that $t_0 = 0.5$ is listed before $t_1 = 0.2$. Because divided differences are completely symmetric in their inputs, you do not need to sort the table. We evaluate directly from the given order.

**Step 1: Compute divided differences**
- First differences:
  - $f[t_0, t_1] = \frac{-3.768 - (-10.25)}{0.2 - 0.5} = \frac{6.482}{-0.3} = -21.606667$
  - $f[t_1, t_2] = \frac{5.976 - (-3.768)}{1.4 - 0.2} = \frac{9.744}{1.2} = 8.120000$
  - $f[t_2, t_3] = \frac{28.972 - 5.976}{2.2 - 1.4} = \frac{22.996}{0.8} = 28.745000$
  - $f[t_3, t_4] = \frac{79.0 - 28.972}{3.0 - 2.2} = \frac{50.028}{0.8} = 62.535000$

- Second differences:
  - $f[t_0, t_1, t_2] = \frac{8.120000 - (-21.606667)}{1.4 - 0.5} = \frac{29.726667}{0.9} = 33.029630$
  - $f[t_1, t_2, t_3] = \frac{28.745000 - 8.120000}{2.2 - 0.2} = \frac{20.625}{2.0} = 10.312500$
  - $f[t_2, t_3, t_4] = \frac{62.535000 - 28.745000}{3.0 - 1.4} = \frac{33.790}{1.6} = 21.118750$

- Third differences:
  - $f[t_0, \dots, t_3] = \frac{10.312500 - 33.029630}{2.2 - 0.5} = \frac{-22.717130}{1.7} = -13.363018$
  - $f[t_1, \dots, t_4] = \frac{21.118750 - 10.312500}{3.0 - 0.2} = \frac{10.806250}{2.8} = 3.859375$

- Fourth difference:
  - $f[t_0, \dots, t_4] = \frac{3.859375 - (-13.363018)}{3.0 - 0.5} = \frac{17.222393}{2.5} = 6.888957$

**Step 2: Evaluate at $t = 2.25$**
Compute the linear factors at $t = 2.25$:
- $(t - 0.5) = 1.75$
- $(t - 0.5)(t - 0.2) = (1.75)(2.05) = 3.5875$
- $(t - 0.5)(t - 0.2)(t - 1.4) = (3.5875)(0.85) = 3.049375$
- $(t - 0.5)(t - 0.2)(t - 1.4)(t - 2.2) = (3.049375)(0.05) = 0.15246875$

Sum the polynomial terms:

$$
s(2.25) = -10.25 - 21.606667(1.75) + 33.029630(3.5875) - 13.363018(3.049375) + 6.888957(0.15246875)
$$

$$
s(2.25) = -10.25 - 37.811667 + 118.49380 - 40.74872 + 1.05035 = 30.7336
$$

$$
\boxed{s(2.25) = 30.7336}
$$

---

### 2022 Q.2(a): 3-Point Quadratic Polynomial Fit [03 Marks]

**The question:** Find the polynomial which fits the following data: $(-1, 7)$, $(1, 5)$, $(2, 15)$.

**Let's solve this step by step.**

Points: $(x_0, y_0) = (-1, 7)$, $(x_1, y_1) = (1, 5)$, $(x_2, y_2) = (2, 15)$.

**Step 1: Divided difference table**
- First differences:
  - $f[x_0, x_1] = \frac{5 - 7}{1 - (-1)} = \frac{-2}{2} = -1$
  - $f[x_1, x_2] = \frac{15 - 5}{2 - 1} = \frac{10}{1} = 10$
- Second difference:
  - $f[x_0, x_1, x_2] = \frac{10 - (-1)}{2 - (-1)} = \frac{11}{3}$

**Step 2: Construct the polynomial**

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
y(x) = \frac{11}{3}x^2 - x + \left(\frac{18}{3} - \frac{11}{3}\right) = \frac{11}{3}x^2 - x + \frac{7}{3}
$$

$$
\boxed{y = \frac{11}{3}x^2 - x + \frac{7}{3}}
$$

**Quick check:**
- At $x = -1$: $\frac{11}{3} + 1 + \frac{7}{3} = \frac{18}{3} + 1 = 6 + 1 = 7$.
- At $x = 1$: $\frac{11}{3} - 1 + \frac{7}{3} = \frac{18}{3} - 1 = 6 - 1 = 5$.
- At $x = 2$: $\frac{11}{3}(4) - 2 + \frac{7}{3} = \frac{51}{3} - 2 = 17 - 2 = 15$. Matches every point!

---

## ⚡ Quick Review

**The method in one sentence:** Build a difference table dividing by the total span in $x$ at each order, and assemble the polynomial using the top diagonal coefficients.

**The key formula you must memorize:**
$$
P(x) = f[x_0] + f[x_0, x_1](x - x_0) + f[x_0, x_1, x_2](x - x_0)(x - x_1) + \dots
$$

**The most common exam mistake:** Forgetting that denominators span multiple intervals! For a 2nd difference, the denominator is $x_{i+2} - x_i$, not $x_{i+1} - x_i$.

**Time estimate in exam:** ~6 minutes for a 3-point or 4-point problem.

---

## 🔗 Connected Topics

- [← NM-4.8: Newton Backward Difference](NM-4.8_Newton_Backward_Difference.md) -- the specialized backward formula when steps are equal.
- [→ NM-4.10: Gauss and Stirling](NM-4.10_Gauss_and_Stirling.md) -- central difference formulas for points near the center of a table.
- [NM-4.6: Lagrange Interpolation](NM-4.6_Lagrange_Interpolation.md) -- the alternative unequal-interval formula that does not require building difference tables.

---

[← Previous: NM-4.8 Newton Backward Difference](NM-4.8_Newton_Backward_Difference.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: NM-4.10 Gauss and Stirling →](NM-4.10_Gauss_and_Stirling.md)
