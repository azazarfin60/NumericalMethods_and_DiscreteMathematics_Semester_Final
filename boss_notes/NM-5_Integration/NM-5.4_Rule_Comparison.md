[← Previous: NM-5.3 Simpson's 3/8 Rule](NM-5.3_Simpsons_Three_Eighth.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: NM-5.5 Romberg's Method →](NM-5.5_Rombergs_Method.md)

---

# NM-5.4: Rule Comparison & Step Constraints

> 🔴 **Priority:** Critical | **Tested:** 2/8 years (2020 Q.6(a), 2023 Q.4(c)) | **Typical marks:** 3

## What This Is (and Why It Matters)

"Compare Simpson's 1/3rd and 3/8th rules" is an RUET exam classic. It is a crisp, high-yield 3-mark question. Examiners ask it because it tests whether you understand the structural constraints of numerical quadrature rather than just plugging numbers into a formula.

Beyond the direct theory question, understanding this comparison is essential for solving mixed-rule problems. When an exam hands you 6 data points (5 subintervals), you must understand why pure Simpson's 1/3 fails, why pure Simpson's 3/8 fails, and how combining them saves the day.

---

## 📝 Key Definitions

> **Subinterval Constraint:** "A rule cannot be applied across an arbitrary grid; Simpson's 1/3-rule requires an even number of subintervals, whereas Simpson's 3/8-rule requires the number of strips to be a multiple of three." -- Jain, §6.4.2–§6.4.3
>
> **In simple words:** Each numerical method packages data points into rigid blocks. The trapezoid rule takes 1 interval at a time; Simpson's 1/3 takes 2 intervals at a time (needing an even total); Simpson's 3/8 takes 3 intervals at a time (needing a multiple of 3).

> **Error Constant:** "The dominant error term for the 1/3-rule is $-\frac{1}{90}h^5 y^{\text{iv}}$, while for the 3/8-rule it is $-\frac{3}{80}h^5 y^{\text{iv}}$." -- Jain, §6.4.3
>
> **In simple words:** Both methods have error scaling with $h^4$, but the numerical multiplier in front is different. Because $\frac{3}{80} = 0.0375$ is larger than $\frac{1}{90} = 0.0111$, Simpson's 3/8 rule generates more error than Simpson's 1/3 for the exact same step size.

> **Mixed Integration Strategy:** "When the total number of subintervals is odd and not divisible by three, no single Simpson rule can cover the entire domain; the domain must be partitioned into segments handled by complementary rules." -- Jain, §6.4.3
>
> **In simple words:** If you have 5 intervals, you cannot cover all 5 with one rule. So you split the domain: use Simpson's 1/3 on the first 4 intervals and the trapezoid rule on the last 1 (or 1/3 on 2 intervals and 3/8 on 3 intervals).

---

## The Master Comparison Table

This comparison table contains everything needed for the 3-mark exam question. Memorize it:

| Property | Trapezoidal Rule | Simpson's 1/3 Rule | Simpson's 3/8 Rule | Romberg Integration |
|:---|:---|:---|:---|:---|
| **Polynomial Degree** | Linear (Degree 1) | Quadratic (Degree 2) | Cubic (Degree 3) | Extrapolated polynomials |
| **Nodes per Panel** | 2 points | 3 points | 4 points | Sequence of points |
| **Subintervals per Panel** | 1 subinterval | 2 subintervals | 3 subintervals | Doubles each stage ($2^k$) |
| **Constraint on Total $n$** | Any integer $n \ge 1$ | $n$ must be **even** | $n$ must be **multiple of 3** | $n = 2, 4, 8, \dots$ |
| **Panel Weights** | $1, 1$ | $1, 4, 1$ | $1, 3, 3, 1$ | Recombines table entries |
| **Formula Prefactor** | $\frac{h}{2}$ | $\frac{h}{3}$ | $\frac{3h}{8}$ | Divisors $4^j - 1$ |
| **Order of Accuracy** | $O(h^2)$ | $O(h^4)$ | $O(h^4)$ | $O(h^{2k})$ at column $k$ |
| **Leading Error Term** | $-\frac{h^3}{12}f''(\xi)$ | $-\frac{h^5}{90}f^{(4)}(\xi)$ | $-\frac{3h^5}{80}f^{(4)}(\xi)$ | Varies per column |
| **Error Constant** | $\frac{1}{12} \approx 0.0833$ | $\frac{1}{90} \approx 0.0111$ | $\frac{3}{80} = 0.0375$ | Highly accelerated |
| **Halving $h$ Reduces Error By** | Factor of 4 | Factor of 16 | Factor of 16 | Factor of 64 or more |
| **Exact for Polynomials of Degree** | $\le 1$ | $\le 3$ (due to symmetry) | $\le 3$ | Very high |

---

## Subinterval Constraints Explained

The constraints come directly from how many subintervals form a single panel:

### 1. Trapezoidal Rule: Any $n \ge 1$
Each panel spans 1 subinterval ($[x_i, x_{i+1}]$). You can have 1, 2, 3, 4, 5, or 100 intervals. There are zero restrictions on $n$.

### 2. Simpson's 1/3 Rule: $n$ Must Be Even
Each panel spans 2 subintervals ($[x_0, x_2]$). To partition the total domain into complete panels without any gaps or leftovers, $n$ must be divisible by 2.
- 4 intervals = 2 panels (works).
- 5 intervals = 2 panels plus 1 leftover strip (**fails**).
- 6 intervals = 3 panels (works).

### 3. Simpson's 3/8 Rule: $n$ Must Be a Multiple of 3
Each panel spans 3 subintervals ($[x_0, x_3]$). To partition the total domain cleanly, $n$ must be divisible by 3 ($n = 3, 6, 9, 12$).
- 3 intervals = 1 panel (works).
- 5 intervals = 1 panel plus 2 leftover strips (**fails**).
- 6 intervals = 2 panels (works).

---

## Why Both Simpson Rules Reach Fourth Order

A very common conceptual question:
*Simpson's 1/3 rule fits a quadratic (degree 2), while Simpson's 3/8 rule fits a cubic (degree 3). Why do both have fourth-order accuracy $O(h^4)$?*

**The reason is symmetry.**
- For Simpson's 1/3 rule, the evaluation stencil consists of three symmetric points: $-h, 0, h$. Any cubic term $x^3$ is odd and antisymmetric about the midpoint. Both the true integral of $x^3$ and the symmetric weighted sum evaluate to zero. This symmetry cancels the third-order error term completely, making the first surviving error term proportional to the fourth derivative $f^{(4)}$.
- For Simpson's 3/8 rule, we fit a cubic directly, which also leaves the first surviving error term proportional to $f^{(4)}$.
- Therefore, both rules are fourth order.

### Why Simpson's 1/3 Is Preferred Over 3/8

Compare their error constants at the exact same step size $h$:

$$
\frac{\text{Simpson's 3/8 error}}{\text{Simpson's 1/3 error}} = \frac{3/80}{1/90} = \frac{270}{80} = 3.375
$$

For the same $h$, Simpson's 3/8 rule has **3.375 times larger error** than Simpson's 1/3 rule. 

Therefore, whenever $n$ is even, Simpson's 1/3 rule is always the superior choice. You only reach for Simpson's 3/8 rule when the interval count forces your hand.

---

## The Mixed Strategy for Odd Interval Counts

What should you do when you are given a dataset with an odd number of intervals that is not divisible by 3, such as $n = 5$ (which comes from 6 data points)?

Three strategies are mathematically valid:

### Strategy A: Simpson's 1/3 on First 4 Intervals + Trapezoid on 5th
- Apply Simpson's 1/3 across $[x_0, x_4]$ (4 intervals, even).
- Apply the trapezoidal rule across $[x_4, x_5]$ (1 interval).
- Add the two results: $I = I_{1/3} + I_T$.
- *This is the standard exam solution used in 2020 Q.6(b).*

### Strategy B: Simpson's 1/3 on First 2 Intervals + Simpson's 3/8 on Last 3
- Apply Simpson's 1/3 across $[x_0, x_2]$ (2 intervals, even).
- Apply Simpson's 3/8 across $[x_2, x_5]$ (3 intervals, multiple of 3).
- Add the two results: $I = I_{1/3} + I_{3/8}$.
- *This maintains fourth-order accuracy across the entire domain.*

### Strategy C: Trapezoid on 1st Interval + Simpson's 1/3 on Remaining 4
- Apply the trapezoidal rule across $[x_0, x_1]$ (1 interval).
- Apply Simpson's 1/3 across $[x_1, x_5]$ (4 intervals, even).
- Add the two results: $I = I_T + I_{1/3}$.

All three strategies yield answers within a fraction of a percent of each other. The crucial exam insight is recognizing that an odd interval count cannot be computed by a single Simpson formula.

---

## 🏆 Past Exam Questions

### 2020 Q.6(a), 2023 Q.4(c): Compare Simpson's 1/3rd and 3/8th Rules [03 marks]

**Question.** Compare Simpson's $1/3^{\text{rd}}$ and $3/8^{\text{th}}$ rules.

**Solution.**

Both methods are **Newton-Cotes** quadrature formulas: they approximate the definite integral $\int_a^b f(x)\,dx$ by passing an interpolating polynomial through equally spaced points and integrating that polynomial exactly.

| Feature | Simpson's $1/3^{\text{rd}}$ Rule | Simpson's $3/8^{\text{th}}$ Rule |
|:---|:---|:---|
| **Interpolating Polynomial** | Quadratic (degree 2) | Cubic (degree 3) |
| **Nodes per Panel** | 3 nodes | 4 nodes |
| **Subintervals per Panel** | 2 subintervals | 3 subintervals |
| **Weights** | $1, 4, 1$ | $1, 3, 3, 1$ |
| **Prefactor** | $\frac{h}{3}$ | $\frac{3h}{8}$ |
| **Interval Count Requirement** | Total intervals $n$ must be **even** | Total intervals $n$ must be a **multiple of 3** |
| **Order of Accuracy** | Fourth order ($O(h^4)$) | Fourth order ($O(h^4)$) |
| **Leading Error Term** | $-\frac{h^5}{90}f^{(4)}(\xi)$ | $-\frac{3h^5}{80}f^{(4)}(\xi)$ |
| **Leading Error Constant** | $\frac{1}{90} \approx 0.0111$ | $\frac{3}{80} = 0.0375$ |

**Key Differences and Practical Usage:**
1. **Both are fourth order:** Both methods integrate polynomials up to degree 3 with zero error, requiring the fourth derivative $f^{(4)}$ to be continuous over the integration domain.
2. **Accuracy at equal step size:** At the same step size $h$, the leading error constant of Simpson's 3/8 rule ($\frac{3}{80}$) is $3.375$ times larger than that of Simpson's 1/3 rule ($\frac{1}{90}$). Therefore, Simpson's 1/3 rule is more accurate and is the default choice.
3. **Where Simpson's 3/8 wins:** When the total interval count $n$ is odd, Simpson's 1/3 rule cannot be applied across the entire domain. If $n$ is a multiple of 3 (such as $n = 3$ or $n = 9$), Simpson's 3/8 rule can be applied directly. When $n = 5$, a mixed strategy is used: Simpson's 3/8 handles 3 intervals, and Simpson's 1/3 handles the remaining 2 intervals.

$$
\boxed{\text{Both are fourth order; } 1/3 \text{ is more accurate at equal } h \text{ but needs an even interval count}}
$$

---

### Exam Variants at a Glance

| Year | What They Asked | Key Method | Key Answer |
|:---|:---|:---|:---|
| 2020 Q.6(a) | Compare Simpson's 1/3 and 3/8 | Table, constraints, error constant ratio | $\boxed{\text{Both are fourth order; } 1/3 \text{ is more accurate at equal } h \text{ but needs an even interval count}}$ |
| 2023 Q.4(c) | Compare Simpson's 1/3 and 3/8 | Table, constraints, error constant ratio | $\boxed{\text{Both are fourth order; } 1/3 \text{ is more accurate at equal } h \text{ but needs an even interval count}}$ |

---

## ⚡ Quick Review

**The method in one sentence:** Both Simpson rules are fourth order, but 1/3 needs $n$ even and is 3.375 times more accurate, while 3/8 needs $n$ divisible by 3 and handles odd blocks.

**The key numbers to memorize:**

$$
\text{1/3 error constant: } \frac{1}{90}, \qquad \text{3/8 error constant: } \frac{3}{80}, \qquad \text{Ratio: } \frac{3/80}{1/90} = 3.375
$$

**The most common exam mistake:** Stating that Simpson's 1/3 is second-order because it uses a quadratic. It is fourth-order because symmetry cancels the cubic error term!

**Time estimate in exam:** ~5 minutes to draw the table and write the 3-point explanation.

---

## 🔗 Connected Topics

- [← NM-5.3: Simpson's 3/8 Rule](NM-5.3_Simpsons_Three_Eighth.md) -- cubic Newton-Cotes formula details.
- [→ NM-5.5: Romberg's Method](NM-5.5_Rombergs_Method.md) -- accelerating lower-order rules to arbitrarily high order without subinterval constraints.
- [NM-5.2: Simpson's 1/3 Rule](NM-5.2_Simpsons_One_Third.md) -- contains the 2020 Q.6(b) op-amp problem where mixed rules are put to work.

---

[← Previous: NM-5.3 Simpson's 3/8 Rule](NM-5.3_Simpsons_Three_Eighth.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: NM-5.5 Romberg's Method →](NM-5.5_Rombergs_Method.md)
