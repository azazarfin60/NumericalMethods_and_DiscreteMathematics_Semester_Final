[← Previous: NM-4.7 Newton Forward Difference](NM-4.7_Newton_Forward_Difference.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: NM-4.9 Divided Difference →](NM-4.9_Divided_Difference.md)

---

# NM-4.8: Newton's Backward Difference

> 🟠 **Priority:** Secondary | **Tested:** 4 appearances (2017, 2020, 2024, CT-02A) | **Typical marks:** 4–5

## What This Is (and Why It Matters)

If your target point sits near the end of a data table, using Newton's forward difference formula is awkward and prone to errors because you would have to calculate huge positive values of $p$ starting all the way back from $x_0$.

Newton's backward difference formula solves this by flipping the direction. It anchors itself at the very last data point $x_n$ and marches backward. It uses the bottom edge of the difference table and replaces falling factorials with rising factorials. Whenever you see a question asking for values near the bottom of an equidistant table (like population in 1925 or 1995 from census data, or temperature at 7 hours from an 8-hour log), this is the exact formula you need.

---

## 📝 Key Definitions

> **Newton's Backward Difference Formula:**
>
> $$
> y(x) = y_n + p\nabla y_n + \frac{p(p+1)}{2!}\nabla^2 y_n + \frac{p(p+1)(p+2)}{3!}\nabla^3 y_n + \cdots + \frac{p(p+1)\dots(p+n-1)}{n!}\nabla^n y_n
> $$
>
> where $p = \dfrac{x - x_n}{h}$. This formula is useful for interpolation near the end of the tabular values. -- Jain, §3.6 (p. 85)
>
> **In simple words:** A formula that starts at your final data point $y_n$ and looks backward through the bottom entries of your difference table. Because you are moving backward into the table, $p$ is negative, and the terms use plus signs $(p+1), (p+2)$ instead of minus signs.

> **Backward Difference Operator ($\nabla$):**
>
> $$
> \nabla y_k = y_k - y_{k-1}, \qquad \nabla^{n+1} y_k = \nabla^n y_k - \nabla^n y_{k-1}
> $$
>
> **In simple words:** The difference between a table entry and the entry directly above it.

---

## The Core Idea: Rising Factorials and the Bottom Diagonal

### 1. Why the Formula Uses Rising Factorials

In the forward formula, we anchored at $x_0$ and moved forward:

$$
p = \frac{x - x_0}{h} \implies x - x_k = (p - k)h
$$

In the backward formula, we anchor at the last point $x_n$:

$$
x_n = x_0 + nh
$$

Our step variable is measured from the bottom:

$$
p = \frac{x - x_n}{h} \implies x = x_n + ph
$$

Now look at the distance from preceding points $x_{n-1}, x_{n-2}, \dots$:

$$
x - x_{n-1} = x_n + ph - (x_n - h) = (p + 1)h
$$

$$
x - x_{n-2} = x_n + ph - (x_n - 2h) = (p + 2)h
$$

When multiplied together, the distance factors naturally produce **rising factorials**:

$$
(x - x_n)(x - x_{n-1})\dots(x - x_{n-k+1}) = p(p+1)(p+2)\dots(p+k-1)\,h^k
$$

That is why every term in Newton's backward formula has plus signs $(p+1), (p+2), \dots$ instead of minus signs!

### 2. Forward vs. Backward Side-by-Side

| Feature | Newton's Forward Formula | Newton's Backward Formula |
| :-- | :-- | :-- |
| **Best used when** | Target is near the start of the table | Target is near the end of the table |
| **Anchor node** | Top node: $x_0$ | Bottom node: $x_n$ |
| **Step variable** | $p = \dfrac{x - x_0}{h}$ | $p = \dfrac{x - x_n}{h}$ |
| **Typical sign of $p$** | Positive: $0 \le p \le 1$ | Negative: $-1 \le p \le 0$ |
| **Factorial terms** | Falling: $p(p-1)(p-2)\dots$ | Rising: $p(p+1)(p+2)\dots$ |
| **Path in table** | Top descending diagonal | Bottom ascending diagonal |

> [!WARNING] Common Trap
> When interpolating inside the table near the end, $x < x_n$, which means $p = \frac{x - x_n}{h}$ is **negative**!
> For example, if $x_n = 1931$, $x = 1925$, and $h = 10$, then $p = \frac{1925 - 1931}{10} = -0.6$.
> Do not make $p$ positive $+0.6$, or your formula will shoot off in the wrong direction.

---

## 🔧 Worked Example

> **From:** 2020 Q.3(b) -- [Marks: 04]

**The question:** The population of a town in the decennial census was as given below:

| Year $x$ | 1891 | 1901 | 1911 | 1921 | 1931 |
| :---: | :---: | :---: | :---: | :---: | :---: |
| Population $y$ (thousands) | 46 | 66 | 81 | 93 | 101 |

Estimate the population for the year 1925 using Newton's backward interpolation formula.

**Let's solve this step by step.**

**Step 1: Construct the difference table ($h = 10$)**

| Year $x$ | $y$ | $\Delta y$ | $\Delta^2 y$ | $\Delta^3 y$ | $\Delta^4 y$ |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1891 | 46 | 20 | $-5$ | 2 | $-3$ |
| 1901 | 66 | 15 | $-3$ | $-1$ | -- |
| 1911 | 81 | 12 | $-4$ | -- | -- |
| 1921 | 93 | 8 | -- | -- | -- |
| 1931 | 101 | -- | -- | -- | -- |

**Step 2: Read the backward differences from the bottom node ($x_n = 1931$)**
Trace the bottom ascending diagonal upward from $y_n = 101$:
- $y_n = 101$
- $\nabla y_n = 8$
- $\nabla^2 y_n = -4$
- $\nabla^3 y_n = -1$
- $\nabla^4 y_n = -3$

**Step 3: Calculate the dimensionless step parameter $p$**

$$
p = \frac{x - x_n}{h} = \frac{1925 - 1931}{10} = \frac{-6}{10} = -0.6
$$

Notice that $-1 \le p \le 0$, which confirms that 1925 lies inside the final interval $[1921, 1931]$.

**Step 4: Evaluate the formula terms**

$$
y(1925) = y_n + p\nabla y_n + \frac{p(p+1)}{2}\nabla^2 y_n + \frac{p(p+1)(p+2)}{6}\nabla^3 y_n + \frac{p(p+1)(p+2)(p+3)}{24}\nabla^4 y_n
$$

Compute each term carefully:
- **Term 0:** $y_n = 101$
- **Term 1:** $p\nabla y_n = (-0.6)(8) = -4.8$
- **Term 2:** $\frac{p(p+1)}{2}\nabla^2 y_n = \frac{(-0.6)(0.4)}{2}(-4) = (-0.12)(-4) = +0.48$
- **Term 3:** $\frac{p(p+1)(p+2)}{6}\nabla^3 y_n = \frac{(-0.6)(0.4)(1.4)}{6}(-1) = (-0.056)(-1) = +0.056$
- **Term 4:** $\frac{p(p+1)(p+2)(p+3)}{24}\nabla^4 y_n = \frac{(-0.6)(0.4)(1.4)(2.4)}{24}(-3) = (-0.0336)(-3) = +0.1008$

**Step 5: Sum all terms**

$$
y(1925) = 101 - 4.8 + 0.48 + 0.056 + 0.1008 = 96.8368\ \text{thousand}
$$

$$
\boxed{y(1925) = 96.8368 \text{ thousand} \approx 96\,837}
$$

**Quick sanity check:**
In 1921 the population was $93$, and in 1931 it was $101$. Our estimate of $96.84$ thousand sits right in between, slightly closer to 1931 because $1925$ is past the midpoint. It makes complete demographic sense.

---

## 🏆 Past Exam Questions

### 2024 Q.3(b): Population Extrapolation for 1995 [04 Marks]

**The question:** The population of a town in decennial census were as following table in thousand units. Estimate the population for the year 1995.

| Year $x$ | 1921 | 1931 | 1941 | 1951 | 1961 |
| :---: | :---: | :---: | :---: | :---: | :---: |
| Population $y$ | 46 | 66 | 81 | 93 | 101 |

**Let's solve this step by step.**

Step size $h = 10$. The target year $1995$ lies outside the table, far past the final census year $x_n = 1961$.

**Step 1: Backward differences from $x_n = 1961$**
From the census difference table:
- $y_n = 101$
- $\nabla y_n = 8$
- $\nabla^2 y_n = -4$
- $\nabla^3 y_n = -1$
- $\nabla^4 y_n = -3$

**Step 2: Step parameter $p$**

$$
p = \frac{1995 - 1961}{10} = \frac{34}{10} = 3.4
$$

**Step 3: Evaluate Newton's backward formula**

$$
y(1995) = y_n + p\nabla y_n + \frac{p(p+1)}{2}\nabla^2 y_n + \frac{p(p+1)(p+2)}{6}\nabla^3 y_n + \frac{p(p+1)(p+2)(p+3)}{24}\nabla^4 y_n
$$

Compute the individual terms:
- $y_n = 101$
- $p\nabla y_n = (3.4)(8) = 27.2$
- $\frac{p(p+1)}{2}\nabla^2 y_n = \frac{(3.4)(4.4)}{2}(-4) = -29.92$
- $\frac{p(p+1)(p+2)}{6}\nabla^3 y_n = \frac{(3.4)(4.4)(5.4)}{6}(-1) = -13.464$
- $\frac{p(p+1)(p+2)(p+3)}{24}\nabla^4 y_n = \frac{(3.4)(4.4)(5.4)(6.4)}{24}(-3) = -64.6272$

**Step 4: Sum all terms**

$$
y(1995) = 101 + 27.2 - 29.92 - 13.464 - 64.6272 = 20.1888
$$

$$
\boxed{P(1995) = 20.1888 \text{ thousand (Newton backward difference, all 5 points)}}
$$

*Tutor insight on extrapolation risk:* Mathematically, $20.19$ thousand is the exact value of the 4th-degree polynomial through all 5 points. But notice how dangerous extrapolation is: the large negative 4th-difference term $(-64.6)$ causes the population to crash from $101$ down to $20$. In real engineering work, long-term projections should use linear regression instead of high-degree polynomial extrapolation.

---

### CT-02A Q.2: Temperature at 7 Hours [05 Marks]

**The question:** From the temperature log $(0, 24), (2, 27), (4, 31), (6, 36), (8, 42)$, estimate temperature at $t = 7\text{ hours}$.

**Let's solve this cleanly:**
The table ends at $t_n = 8$ with step $h = 2$.
Target $t = 7$ is in the final interval $[6, 8]$.

Compute $p$:

$$
p = \frac{7 - 8}{2} = -0.5
$$

Bottom backward differences from $t_n = 8$:
- $T_n = 42$
- $\nabla T_n = 42 - 36 = 6$
- $\nabla^2 T_n = 6 - 5 = 1$
- $\nabla^3 T_n = 0$

Evaluate Newton's backward formula:

$$
T(7) = 42 + (-0.5)(6) + \frac{(-0.5)(-0.5 + 1)}{2}(1) = 42 - 3.0 + \frac{(-0.5)(0.5)}{2} = 39.0 - 0.125 = 38.875\ ^\circ\text{C}
$$

$$
\boxed{T(7) = 38.875 \approx 38.88 \ ^\circ\text{C}}
$$

---

## ⚡ Quick Review

**The method in one sentence:** Anchor at the last row $x_n$, calculate $p = (x - x_n)/h$ (which is negative inside the table), and use rising factorials $p(p+1)\dots$ along the bottom diagonal.

**The formula you must memorize:**
$$
y(x) = y_n + p\nabla y_n + \frac{p(p+1)}{2!}\nabla^2 y_n + \frac{p(p+1)(p+2)}{3!}\nabla^3 y_n + \dots
$$

**The most common exam mistake:** Using minus signs $(p-1)$ like the forward formula instead of plus signs $(p+1)$. Remember: backward uses rising factorials!

**Time estimate in exam:** ~5 minutes once the difference table is ready.

---

## 🔗 Connected Topics

- [← NM-4.7: Newton Forward Difference](NM-4.7_Newton_Forward_Difference.md) -- the counterpart formula for points near the start of the table.
- [→ NM-4.9: Divided Difference](NM-4.9_Divided_Difference.md) -- generalizing finite difference tables to arbitrary unequal step sizes.
- [NM-4.11: Difference Tables](NM-4.11_Difference_Tables.md) -- complete difference table construction and demographic problem sets.

---

[← Previous: NM-4.7 Newton Forward Difference](NM-4.7_Newton_Forward_Difference.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: NM-4.9 Divided Difference →](NM-4.9_Divided_Difference.md)
