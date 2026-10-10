[← Previous: NM-4.12 Two-Variable Interpolation](../NM-4_Curve_Fitting/NM-4.12_Two_Variable_Interpolation.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: NM-5.2 Simpson's 1/3 Rule →](NM-5.2_Simpsons_One_Third.md)

---

# NM-5.1: Trapezoidal Rule

> 🟠 **Priority:** Secondary | **Tested:** 4/8 years (2018, 2019, 2021, 2022) | **Typical marks:** 3 to 5

## What This Is (and Why It Matters)

Imagine you want to calculate the area under a curving hill, but you only know its height at discrete points along the road. The simplest thing you can do is connect each pair of adjacent survey points with a straight line. 

Under each straight line segment, you get a simple geometric shape: a vertical trapezoid. You compute the area of each trapezoid, add them together, and that total gives you an approximation of the definite integral.

The RUET exam tests this in four distinct ways:
1. **Deriving the composite formula:** Showing why interior points get doubled while endpoints appear once (2021 Q.8(a)).
2. **Discussing the rule:** Stating the formula, error order, and physical meaning (2019 Q.6(c)).
3. **Calculating segment counts:** Finding the minimum number of intervals $n$ to guarantee an error below a specified threshold like $0.01$ (2018 Q.6(b)).
4. **Supplying the baseline for Romberg integration:** Computing trapezoidal values at $h = 0.5, 0.25, 0.125$ as column 0 of a Romberg table (2022 Q.3(a)).

---

## 📝 Key Definitions

> **Trapezoidal Rule (Single Panel):** "Setting $n = 1$ in the general formula, all differences higher than the first become zero: $\int_{x_0}^{x_1} y\,dx = \frac{h}{2}(y_0 + y_1)$." -- Jain, §6.4.1
>
> **In simple words:** You approximate the area under a curve between two points by drawing a straight chord between them and finding the area of that single trapezoid: width times the average of the two heights.

> **Composite Trapezoidal Rule:** "Combining all these expressions over $[x_0, x_n]$, we obtain $\int_{x_0}^{x_n} y\,dx = \frac{h}{2}[y_0 + 2(y_1 + y_2 + \cdots + y_{n-1}) + y_n]$." -- Jain, §6.4.1
>
> **In simple words:** When you have many strips, each interior height serves as the right boundary of one strip and the left boundary of the next strip. So every interior height gets counted twice, while the very first and last heights only get counted once.

> **Truncation Error of Trapezoidal Rule:** "The total error is given by $E = -\frac{b-a}{12}h^2 y''(\bar{x})$, where $y''(\bar{x})$ is the largest value of the second derivatives." -- Jain, §6.4.1
>
> **In simple words:** Because a straight line cannot capture the curvature of a hill, your estimate carries an error proportional to the second derivative $f''$ and the square of the step size $h^2$. Cut your step size in half, and your error drops to one quarter.

---

## The Core Idea

The trapezoidal rule is the first and simplest member of the **Newton-Cotes** integration family. It uses a first-degree polynomial (a straight line) through each pair of adjacent nodes.

![Trapezoidal rule: strips under the curve](diagrams/nm5_trapezoidal_rule_strips.jpg)

### Why Interior Nodes Get a Weight of 2

Look at the geometry of adjacent strips:
- Strip 1 covers $[x_0, x_1]$ with area $\frac{h}{2}(y_0 + y_1)$.
- Strip 2 covers $[x_1, x_2]$ with area $\frac{h}{2}(y_1 + y_2)$.
- Strip 3 covers $[x_2, x_3]$ with area $\frac{h}{2}(y_2 + y_3)$.

When you add them all up:
- $y_0$ appears only in Strip 1.
- $y_1$ appears in Strip 1 and Strip 2. That gives $\frac{h}{2}y_1 + \frac{h}{2}y_1 = h y_1 = 2 \cdot \frac{h}{2}y_1$.
- Every interior ordinate is shared between two neighbor panels.
- $y_n$ appears only in the final strip.

Factor out $\frac{h}{2}$, and the iconic formula appears naturally.

### The Composite Formula

$$
\int_a^b f(x)\,dx \approx \frac{h}{2}\left[f(a) + f(b) + 2\sum_{i=1}^{n-1}f(x_i)\right]
$$

**Reading this formula:**
- $h = \frac{b - a}{n}$ is the width of each strip.
- $f(a)$ and $f(b)$ are the two endpoint heights.
- $\sum_{i=1}^{n-1} f(x_i)$ is the sum of all interior heights, doubled.

### The Error Bound

For a function $f(x)$ with continuous second derivative on $[a, b]$, the global truncation error is bounded by:

$$
|E| \le \frac{(b - a)h^2}{12}\max_{x \in [a, b]}|f''(x)|
$$

This tells us:
- If $f(x)$ is a straight line, $f''(x) = 0$, so the error is exactly zero.
- If $f''(x) > 0$ (concave up, like a bowl), the straight chord hangs above the curve. The trapezoidal rule overshoots the true integral.
- If $f''(x) < 0$ (concave down, like an arch), the straight chord sits below the curve. The trapezoidal rule undershoots the true integral.

### Step-by-Step Algorithm

1. **Calculate step size:** $h = \frac{b - a}{n}$.
2. **List the evaluation nodes:** $x_i = a + i h$ for $i = 0, 1, 2, \dots, n$.
3. **Compute function values:** $f_i = f(x_i)$ at each node. Keep at least 6 decimal places.
4. **Sum the interior values:** Add all $f_1 + f_2 + \cdots + f_{n-1}$ and multiply by 2.
5. **Add endpoints:** Add $f_0 + f_n$ to the doubled interior sum.
6. **Multiply by prefactor:** Multiply the entire sum by $\frac{h}{2}$.

> [!WARNING] Common Trap in Error-Bound Problems
> When solving for the number of segments $n$ from an error inequality, you will often obtain a decimal like $n > 2.8868$. Students sometimes round to the nearest integer (which happens to be 3 here) or mistakenly round down. You must **always round UP to the next integer** to ensure the error stays strictly below the required tolerance.

---

## 🔧 Worked Example

> **From:** 2018 Q.6(b) [Marks: 04]

**The question:** Determine the value of $n$ so that the trapezoidal rule will approximate the value of $\int_0^1 \sqrt{1 + x^2} \, dx$ with an error that is less than $0.01$.

**Let us solve this step by step.**

**Step 1. Identify the given parameters.**
Here $a = 0$, $b = 1$, and the target error tolerance is:

$$
|E| < 0.01
$$

The integrand is:

$$
f(x) = \sqrt{1 + x^2} = (1 + x^2)^{1/2}
$$

**Step 2. Compute the first and second derivatives.**
Differentiating using the chain rule:

$$
f'(x) = \frac{1}{2}(1 + x^2)^{-1/2}(2x) = \frac{x}{\sqrt{1 + x^2}}
$$

Differentiating again using the quotient rule:

$$
f''(x) = \frac{\sqrt{1 + x^2}(1) - x \cdot \frac{x}{\sqrt{1 + x^2}}}{1 + x^2} = \frac{(1 + x^2) - x^2}{(1 + x^2)^{3/2}} = \frac{1}{(1 + x^2)^{3/2}}
$$

**Step 3. Find the maximum of $|f''(x)|$ on $[0, 1]$.**
Notice that the denominator $(1 + x^2)^{3/2}$ is smallest when $x = 0$. Since the numerator is a constant 1, the fraction reaches its maximum value at $x = 0$:

$$
\max_{x \in [0, 1]} |f''(x)| = f''(0) = \frac{1}{(1 + 0)^{3/2}} = 1
$$

**Step 4. Set up the error bound inequality.**
The composite trapezoidal error bound is:

$$
|E| \le \frac{(b - a)h^2}{12}\max|f''| = \frac{(1 - 0)h^2}{12}(1) = \frac{h^2}{12}
$$

We require this error to be strictly less than $0.01$:

$$
\frac{h^2}{12} < 0.01 \implies h^2 < 0.12 \implies h < \sqrt{0.12} \approx 0.3464
$$

**Step 5. Solve for $n$.**
Since $h = \frac{b - a}{n} = \frac{1}{n}$:

$$
\frac{1}{n} < 0.3464 \implies n > \frac{1}{0.3464} \approx 2.8868
$$

Since $n$ must be an integer, the smallest integer satisfying this condition is:

$$
\boxed{n = 3}
$$

**Quick sanity check:**
Let us test $n = 2$ and $n = 3$ explicitly:

| $n$ | $h$ | Approximation | Error | Meets $< 0.01$? |
|:---:|:---:|:---|:---|:---:|
| 2 | 0.5000 | 1.1625704 | $0.014777$ | No ($> 0.01$) |
| 3 | 0.3333 | 1.1543499 | $0.006556$ | **Yes** ($< 0.01$) |

At $n = 2$, the actual error is $0.0148$, which violates the requirement. At $n = 3$, the error drops to $0.0066$, which satisfies the requirement comfortably. Confirmed.

---

## 🏆 Past Exam Questions

### 2021 Q.8(a): Derive the Composite Trapezoidal Formula [04 marks]

**Question.** Derive the following numerical integration formula:

$$
\int_{x_0}^{x_n} y\,dx = \frac{h}{2}[y_0 + 2(y_1 + y_2 + \cdots + y_{n-1}) + y_n]
$$

**Solution.**

Let the interval $[x_0, x_n]$ be divided into $n$ equal subintervals of width:

$$
h = \frac{x_n - x_0}{n}
$$

with nodes $x_i = x_0 + i h$ and corresponding function ordinates $y_i = f(x_i)$.

**Step 1. Start from a single subinterval.**
On the single subinterval $[x_i, x_{i+1}]$, approximate the curve by a straight chord joining $(x_i, y_i)$ and $(x_{i+1}, y_{i+1})$. The area of this single trapezoid is:

$$
\int_{x_i}^{x_{i+1}} y\,dx = \frac{h}{2}(y_i + y_{i+1}) - \frac{h^3}{12}y''(\xi_i) + \cdots
$$

where $\xi_i \in [x_i, x_{i+1}]$.

**Step 2. Sum over all $n$ subintervals.**
The total integral across the full interval $[x_0, x_n]$ is the sum of integrals across each subinterval:

$$
\int_{x_0}^{x_n} y\,dx = \sum_{i=0}^{n-1} \int_{x_i}^{x_{i+1}} y\,dx = \sum_{i=0}^{n-1}\left[\frac{h}{2}(y_i + y_{i+1}) + \text{error}\right]
$$

**Step 3. Collect the terms.**
Writing out the terms explicitly:

$$
\int_{x_0}^{x_n} y\,dx = \frac{h}{2}(y_0 + y_1) + \frac{h}{2}(y_1 + y_2) + \frac{h}{2}(y_2 + y_3) + \cdots + \frac{h}{2}(y_{n-1} + y_n) - \sum_{i=0}^{n-1}\frac{h^3}{12}y''(\xi_i)
$$

Notice that every interior ordinate $y_1, y_2, \dots, y_{n-1}$ belongs to two adjacent trapezoids. Each interior ordinate collects two factors of $\frac{h}{2}$, giving a total coefficient of:

$$
\frac{h}{2} + \frac{h}{2} = h
$$

Only the two boundary ordinates $y_0$ and $y_n$ appear once, each with coefficient $\frac{h}{2}$.

**Step 4. Factor out $\frac{h}{2}$.**
Regrouping:

$$
\int_{x_0}^{x_n} y\,dx = \frac{h}{2}y_0 + h(y_1 + y_2 + \cdots + y_{n-1}) + \frac{h}{2}y_n - \frac{h^3}{12}\sum_{i=0}^{n-1}y''(\xi_i)
$$

Factoring out $\frac{h}{2}$ from all terms:

$$
\int_{x_0}^{x_n} y\,dx = \frac{h}{2}\left[y_0 + 2(y_1 + y_2 + \cdots + y_{n-1}) + y_n\right] - \frac{h^3}{12}\sum_{i=0}^{n-1}y''(\xi_i)
$$

**Step 5. Evaluate the leading error term.**
Since there are $n$ subintervals, the sum $\sum_{i=0}^{n-1} y''(\xi_i) = n y''(\bar{\xi})$. Using $n h = x_n - x_0$:

$$
E = -\frac{h^3}{12} n y''(\bar{\xi}) = -\frac{(x_n - x_0)h^2}{12}y''(\bar{\xi}) = O(h^2)
$$

Hence the composite formula is established:

$$
\boxed{\int_{x_0}^{x_n} y\,dx = \frac{h}{2}\left[y_0 + 2\sum_{i=1}^{n-1}y_i + y_n\right] + O(h^2)}
$$

---

### 2019 Q.6(c): Discuss Trapezoidal Rule of Numerical Integration [03 marks]

**Question.** Discuss trapezoidal rule of numerical integration.

**Solution.**

The **trapezoidal rule** approximates the definite integral $\int_a^b f(x)\,dx$ by replacing the true continuous curve with a series of straight line segments joining adjacent data points. The total area under the curve is approximated by the sum of the areas of the resulting trapezoids.

**Derivation:**
Over a single panel $[x_0, x_1]$ of width $h = x_1 - x_0$, the straight line through $(x_0, f_0)$ and $(x_1, f_1)$ has average height $\frac{f_0 + f_1}{2}$. Its area is:

$$
\int_{x_0}^{x_1} f(x)\,dx \approx \frac{h}{2}(f_0 + f_1)
$$

**Composite rule:**
Dividing $[a, b]$ into $n$ equal subintervals of width $h = \frac{b - a}{n}$ and summing across all panels:

$$
\int_a^b f(x)\,dx \approx \frac{h}{2}\left[f_0 + 2f_1 + 2f_2 + \cdots + 2f_{n-1} + f_n\right]
$$

$$
\boxed{\int_a^b f(x)\,dx \approx \frac{h}{2}\left[f(a) + f(b) + 2\sum_{i=1}^{n-1}f_i\right]}
$$

**Error:**
The error over a single panel is $-\frac{h^3}{12}f''(\xi)$. Over $n$ subintervals, the total composite error is:

$$
E = -\frac{(b - a)h^2}{12}f''(\xi), \qquad O(h^2)
$$

**Key Properties:**
1. **Order of accuracy:** It is a second-order method ($O(h^2)$). Halving the step size $h$ reduces the error by a factor of 4.
2. **Exactness:** It is exact for linear polynomials (degree $\le 1$). It overshoots when the curve is concave up ($f'' > 0$) because the straight chord sits above the curve.
3. **No interval count constraint:** It works for any integer $n \ge 1$ (unlike Simpson's rules, which demand even counts or multiples of 3).
4. **Basis for Romberg integration:** It provides the foundation for Richardson extrapolation to achieve higher-order accuracy.

---

### 2022 Q.3(a): Trapezoidal Baseline for Romberg [04 marks]

**Question.** Compute the value of $I = \int_0^1 \frac{dx}{1 + x^2}$ using the trapezoidal rule with $h = 0.5, 0.25$ and $0.125$. Then obtain a better estimate using Romberg's method.

**Solution.**

**Step 1. Tabulate function values.**
Here $f(x) = \frac{1}{1 + x^2}$ over $[0, 1]$:

| $x$ | 0 | 0.125 | 0.25 | 0.375 | 0.5 | 0.625 | 0.75 | 0.875 | 1 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| $f(x)$ | 1.000000 | 0.984615 | 0.941176 | 0.876712 | 0.800000 | 0.719101 | 0.640000 | 0.566372 | 0.500000 |

**Step 2. Compute composite trapezoidal estimates.**

- **At $h = 0.5$ ($n = 2$ intervals):**
  Nodes are $x = 0, 0.5, 1$:
  $$
  T_2 = \frac{0.5}{2}[f(0) + 2f(0.5) + f(1)] = 0.25[1 + 2(0.800000) + 0.5] = 0.25(3.1) = 0.775000
  $$

- **At $h = 0.25$ ($n = 4$ intervals):**
  Nodes are $x = 0, 0.25, 0.5, 0.75, 1$:
  $$
  T_4 = \frac{0.25}{2}[1 + 2(0.941176 + 0.800000 + 0.640000) + 0.5] = 0.125[1 + 2(2.381176) + 0.5] = 0.782794
  $$

- **At $h = 0.125$ ($n = 8$ intervals):**
  Nodes include all 9 points:
  $$
  \text{Sum of 7 interior points} = 0.984615 + 0.941176 + 0.876712 + 0.800000 + 0.719101 + 0.640000 + 0.566372 = 5.527976
  $$
  $$
  T_8 = \frac{0.125}{2}[1 + 2(5.527976) + 0.5] = 0.0625(12.555952) = 0.784747
  $$

**Step 3. Richardson extrapolation for Romberg.**
Using the extrapolation formula $R_{k,j} = R_{k,j-1} + \frac{R_{k,j-1} - R_{k-1,j-1}}{4^j - 1}$:

- **Column 1 ($j = 1$, divisor $4^1 - 1 = 3$):**
  $$
  R_{2,1} = 0.782794 + \frac{0.782794 - 0.775000}{3} = 0.782794 + 0.002598 = 0.785392
  $$
  $$
  R_{3,1} = 0.784747 + \frac{0.784747 - 0.782794}{3} = 0.784747 + 0.000651 = 0.785398
  $$

- **Column 2 ($j = 2$, divisor $4^2 - 1 = 15$):**
  $$
  R_{3,2} = 0.785398 + \frac{0.785398 - 0.785392}{15} = 0.785398 + 0.0000004 = 0.7853985
  $$

**The Romberg table:**

$$
\begin{array}{c|ccc}
R_{k,0} & R_{k,1} & R_{k,2} \\
\hline
0.775000 & & \\
0.782794 & 0.785392 & \\
0.784747 & 0.785398 & 0.7853985
\end{array}
$$

$$
\boxed{I \approx 0.7853985 \quad \text{(trapezoid alone gives } 0.784747\text{)}}
$$

*(Check: exact integral is $\arctan(1) = \frac{\pi}{4} \approx 0.7853981634$. Romberg matches to 6 decimal places).*

---

### Exam Variants at a Glance

| Year | What They Asked | Key Method | Key Answer |
|:---|:---|:---|:---|
| 2018 Q.6(b) | Minimum segments $n$ for error $< 0.01$ | $|E| \le \frac{(b-a)h^2}{12}\max|f''|$ | $\boxed{n = 3}$ |
| 2019 Q.6(c) | Discuss trapezoidal rule | Theory, formula, error $O(h^2)$ | $\boxed{\int_a^b f(x)\,dx \approx \frac{h}{2}\left[f(a) + f(b) + 2\sum_{i=1}^{n-1}f_i\right]}$ |
| 2021 Q.8(a) | Derive composite trapezoidal formula | Sum panels, collect shared nodes | $\boxed{\int_{x_0}^{x_n} y\,dx = \frac{h}{2}\left[y_0 + 2\sum_{i=1}^{n-1}y_i + y_n\right] + O(h^2)}$ |
| 2022 Q.3(a) | Trapezoidal at $h = 0.5, 0.25, 0.125$ + Romberg | 3 step sizes + Richardson table | $\boxed{I \approx 0.7853985 \quad \text{(trapezoid alone gives } 0.784747\text{)}}$ |

---

## ⚡ Quick Review

**The method in one sentence:** Replace the curve with straight line chords over each subinterval, giving a sum of trapezoid areas with weights $1, 2, 2, \dots, 2, 1$.

**The formula you must memorize:**

$$
\int_a^b f(x)\,dx \approx \frac{h}{2}\left[f_0 + 2\sum_{i=1}^{n-1}f_i + f_n\right], \qquad E = -\frac{(b - a)h^2}{12}f''(\xi)
$$

**The most common exam mistake:** Forgetting that interior terms are multiplied by 2 while the endpoints are multiplied by 1, or rounding down when solving for segment count $n$.

**Time estimate in exam:** ~6 to 8 minutes for an error bound or composite calculation.

---

## 🔗 Connected Topics

- [← NM-4.12: Two-Variable Interpolation](../NM-4_Curve_Fitting/NM-4.12_Two_Variable_Interpolation.md) -- previous subtopic in the syllabus sequence.
- [→ NM-5.2: Simpson's 1/3 Rule](NM-5.2_Simpsons_One_Third.md) -- replaces straight chords with parabolas, boosting accuracy from $O(h^2)$ to $O(h^4)$.
- [NM-5.5: Romberg's Method](NM-5.5_Rombergs_Method.md) -- uses composite trapezoidal values at halved step sizes to cancel error terms systematically.
- [NM-5.6: Error in Integration](NM-5.6_Error_in_Integration.md) -- detailed comparative error analysis across all quadrature rules.

---

[← Previous: NM-4.12 Two-Variable Interpolation](../NM-4_Curve_Fitting/NM-4.12_Two_Variable_Interpolation.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: NM-5.2 Simpson's 1/3 Rule →](NM-5.2_Simpsons_One_Third.md)
