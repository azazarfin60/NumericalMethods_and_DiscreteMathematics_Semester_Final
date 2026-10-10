[← Previous: NM-5.2 Simpson's 1/3 Rule](NM-5.2_Simpsons_One_Third.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: NM-5.4 Rule Comparison →](NM-5.4_Rule_Comparison.md)

---

# NM-5.3: Simpson's Three-Eighth Rule

> 🟠 **Priority:** Secondary | **Tested:** 1 appearance (2019 Q.7(b)) | **Typical marks:** 4

## What This Is (and Why It Matters)

Simpson's 1/3 rule is wonderful, but it has one strict limitation: it demands an **even** number of subintervals. What happens if your experimental dataset gives you 3 intervals? Or 9 intervals? Or what if you have 5 intervals, and you do not want to drop down to a straight-line trapezoid for the leftover strip?

Simpson's 3/8 rule solves this puzzle. Instead of fitting a parabola across 3 points (2 intervals), it fits a cubic polynomial across 4 points (3 intervals). 

In RUET exams, this rule appears in two distinct roles:
1. **Direct numerical evaluation:** Evaluating an integral using Simpson's 3/8 rule over a 3-segment grid (2019 Q.7(b)).
2. **Comparative theory & mixed strategies:** Comparing its constraints and error constant against Simpson's 1/3 rule (2020 Q.6(a), 2023 Q.4(c)).

---

## 📝 Key Definitions

> **Simpson's 3/8 Rule (Single Panel):** "Setting $n = 3$ in Newton's general formula, we obtain $\int_{x_0}^{x_3} y\,dx = \frac{3h}{8}(y_0 + 3y_1 + 3y_2 + y_3)$." -- Jain, §6.4.3
>
> **In simple words:** You take four equally spaced points spanning three subintervals, fit a cubic curve through them, and find its exact area. The middle two points get multiplied by 3, the endpoints by 1, and the whole sum is scaled by $\frac{3h}{8}$.

> **Composite Simpson's 3/8 Rule:** "Summing across all panels where $n$ is a multiple of 3, we obtain $\int_{x_0}^{x_n} y\,dx = \frac{3h}{8}[y_0 + 3y_1 + 3y_2 + 2y_3 + 3y_4 + 3y_5 + 2y_6 + \cdots + y_n]$." -- Jain, §6.4.3
>
> **In simple words:** When you have many intervals (in multiples of 3), the weights follow the pattern $1, 3, 3, 2, 3, 3, 2, \dots, 3, 3, 1$. The boundary where two cubic panels meet gets weight $3/8 + 3/8 = 6/8 = 2(3/8)$, giving a weight of 2.

> **Truncation Error of Simpson's 3/8 Rule:** "The dominant term in the error of this formula is given by $-\frac{3}{80}h^5 y^{\text{iv}}(\bar{x})$ per panel, and composite error $-\frac{3(b-a)}{80}h^4 y^{\text{iv}}(\bar{x})$." -- Jain, §6.4.3
>
> **In simple words:** Simpson's 3/8 rule is fourth-order ($O(h^4)$), just like Simpson's 1/3 rule. But its error constant ($\frac{3}{80} = 0.0375$) is 3.375 times larger than that of Simpson's 1/3 rule ($\frac{1}{90} = 0.0111$). For the exact same step size $h$, Simpson's 1/3 is more accurate.

---

## The Core Idea

### Derivation from Newton's Forward Difference Formula

Recall the general Newton-Cotes formula obtained by integrating Newton's forward difference polynomial:

$$
\int_{x_0}^{x_n} y\,dx = nh\left[y_0 + \frac{n}{2}\Delta y_0 + \frac{n(2n - 3)}{12}\Delta^2 y_0 + \frac{n(n - 2)^2}{24}\Delta^3 y_0 + \cdots\right]
$$

Setting $n = 3$, all differences higher than the third vanish for a cubic:

$$
\int_{x_0}^{x_3} y\,dx = 3h\left[y_0 + \frac{3}{2}\Delta y_0 + \frac{3(3)}{12}\Delta^2 y_0 + \frac{3(1)^2}{24}\Delta^3 y_0\right]
$$

$$
= 3h\left[y_0 + \frac{3}{2}\Delta y_0 + \frac{3}{4}\Delta^2 y_0 + \frac{1}{8}\Delta^3 y_0\right]
$$

Now substitute the forward difference definitions:
- $\Delta y_0 = y_1 - y_0$
- $\Delta^2 y_0 = y_2 - 2y_1 + y_0$
- $\Delta^3 y_0 = y_3 - 3y_2 + 3y_1 - y_0$

Expanding and collecting coefficients for each ordinate:
- **Coefficient of $y_0$:** $1 - \frac{3}{2} + \frac{3}{4} - \frac{1}{8} = \frac{8 - 12 + 6 - 1}{8} = \frac{1}{8}$
- **Coefficient of $y_1$:** $\frac{3}{2} - \frac{6}{4} + \frac{3}{8} = \frac{3}{2} - \frac{3}{2} + \frac{3}{8} = \frac{3}{8}$
- **Coefficient of $y_2$:** $\frac{3}{4} - \frac{3}{8} = \frac{6 - 3}{8} = \frac{3}{8}$
- **Coefficient of $y_3$:** $\frac{1}{8}$

Multiplying through by $3h$:

$$
\int_{x_0}^{x_3} y\,dx \approx 3h\left[\frac{1}{8}y_0 + \frac{3}{8}y_1 + \frac{3}{8}y_2 + \frac{1}{8}y_3\right] = \frac{3h}{8}(y_0 + 3y_1 + 3y_2 + y_3)
$$

This is Simpson's three-eighth rule.

---

### The Subinterval Constraint: $n$ Must Be a Multiple of 3

Because each panel spans 3 subintervals and uses 4 nodes:
- The number of subintervals $n$ **must be a multiple of 3** ($n = 3, 6, 9, 12, \dots$).
- You cannot apply pure Simpson's 3/8 rule to 2, 4, or 5 subintervals.

### Accuracy Comparison: 1/3 vs 3/8

Both rules are fourth order ($O(h^4)$). Both integrate cubic polynomials exactly. But compare their error constants:

$$
\text{Simpson's 1/3 constant: } \frac{1}{90} \approx 0.0111
$$

$$
\text{Simpson's 3/8 constant: } \frac{3}{80} = 0.0375
$$

$$
\frac{3/80}{1/90} = \frac{270}{80} = 3.375
$$

For the same step size $h$, **Simpson's 3/8 rule produces 3.375 times more truncation error** than Simpson's 1/3 rule.

**Why does this happen?**  
Simpson's 1/3 rule gets a "free" boost in degree from symmetry: it fits a quadratic (2nd degree) and achieves cubic (3rd degree) exactness for free. Simpson's 3/8 fits a cubic directly, but because a 4-point symmetric stencil does not cancel the 4th-derivative error as tightly as the 3-point stencil, its error constant is larger.

Therefore:
- **Default choice:** Always use Simpson's 1/3 whenever $n$ is even.
- **When to use 3/8:** Use it when the number of intervals is an odd multiple of 3 (like $n = 3$ or $n = 9$), or in mixed strategies (like 5 intervals = 3 intervals by 3/8 + 2 intervals by 1/3).

---

## 🔧 Worked Example

> **From:** 2019 Q.7(b) [Marks: 04]

**The question:** Evaluate, $\int_1^2 (x^2 + 1) \, dx$ using Simpson's 3/8 rule.

**Let us solve this step by step.**

**Step 1. Determine the grid setup.**
The limits of integration are $a = 1$ and $b = 2$.
Simpson's 3/8 rule requires the number of subintervals to be a multiple of 3. Over a single application panel, we take:

$$
n = 3
$$

The step size is:

$$
h = \frac{b - a}{n} = \frac{2 - 1}{3} = \frac{1}{3}
$$

The four evaluation nodes are:

$$
x_0 = 1, \qquad x_1 = 1 + \frac{1}{3} = \frac{4}{3}, \qquad x_2 = 1 + \frac{2}{3} = \frac{5}{3}, \qquad x_3 = 2
$$

**Step 2. Compute the function ordinates.**
Here $f(x) = x^2 + 1$:

$$
f(x_0) = f(1) = 1^2 + 1 = 2
$$

$$
f(x_1) = f\!\left(\frac{4}{3}\right) = \left(\frac{4}{3}\right)^2 + 1 = \frac{16}{9} + 1 = \frac{25}{9} \approx 2.777778
$$

$$
f(x_2) = f\!\left(\frac{5}{3}\right) = \left(\frac{5}{3}\right)^2 + 1 = \frac{25}{9} + 1 = \frac{34}{9} \approx 3.777778
$$

$$
f(x_3) = f(2) = 2^2 + 1 = 4 + 1 = 5
$$

**Step 3. Apply the Simpson's 3/8 formula.**

$$
\int_1^2 (x^2 + 1)\,dx \approx \frac{3h}{8}\left[f(x_0) + 3f(x_1) + 3f(x_2) + f(x_3)\right]
$$

Substituting $h = \frac{1}{3}$:

$$
\frac{3h}{8} = \frac{3}{8}\cdot\frac{1}{3} = \frac{1}{8}
$$

Now substitute the ordinates:

$$
\int_1^2 (x^2 + 1)\,dx \approx \frac{1}{8}\left[2 + 3\left(\frac{25}{9}\right) + 3\left(\frac{34}{9}\right) + 5\right]
$$

Simplify the inner terms:

$$
3\left(\frac{25}{9}\right) = \frac{25}{3}, \qquad 3\left(\frac{34}{9}\right) = \frac{34}{3}
$$

$$
= \frac{1}{8}\left[2 + \frac{25}{3} + \frac{34}{3} + 5\right] = \frac{1}{8}\left[7 + \frac{59}{3}\right]
$$

$$
= \frac{1}{8}\left[\frac{21 + 59}{3}\right] = \frac{1}{8}\cdot\frac{80}{3} = \frac{10}{3} \approx 3.3333
$$

$$
\boxed{\int_1^2(x^2 + 1)\,dx = \frac{10}{3} = 3.3333}
$$

**Quick sanity check (by analytical integration):**

$$
\int_1^2 (x^2 + 1)\,dx = \left[\frac{x^3}{3} + x\right]_1^2 = \left(\frac{8}{3} + 2\right) - \left(\frac{1}{3} + 1\right) = \frac{14}{3} - \frac{4}{3} = \frac{10}{3}
$$

The numerical answer agrees with the exact analytical integral to all decimal places. 

**Why is there zero error?** Because Simpson's 3/8 rule fits a cubic polynomial and integrates all polynomials of degree $\le 3$ with zero truncation error. Since $x^2 + 1$ is a quadratic polynomial (degree 2), exact agreement is mathematically guaranteed.

---

### Exam Variants at a Glance

| Year | What They Asked | Key Method | Key Answer |
|:---|:---|:---|:---|
| 2019 Q.7(b) | Evaluate $\int_1^2 (x^2+1)\,dx$ with 3/8 rule | $n = 3, h = 1/3$, weights $1, 3, 3, 1$ | $\boxed{\int_1^2(x^2 + 1)\,dx = \frac{10}{3} = 3.3333}$ |
| 2020 Q.6(a) | Compare Simpson's 1/3 and 3/8 rules | Theory, constraints, error constants | $\boxed{\text{Both are fourth order; } 1/3 \text{ is more accurate at equal } h \text{ but needs an even interval count}}$ |
| 2023 Q.4(c) | Compare Simpson's 1/3 and 3/8 rules | Theory, constraints, error constants | $\boxed{\text{Both are fourth order; } 1/3 \text{ is more accurate at equal } h \text{ but needs an even interval count}}$ |

---

## ⚡ Quick Review

**The method in one sentence:** Fit a cubic polynomial through four equally spaced points, producing weights $1, 3, 3, 1$ with prefactor $\frac{3h}{8}$ and fourth-order accuracy.

**The formula you must memorize:**

$$
\int_{x_0}^{x_3} f(x)\,dx \approx \frac{3h}{8}(f_0 + 3f_1 + 3f_2 + f_3)
$$

**The composite formula:**

$$
\int_{x_0}^{x_n} f(x)\,dx \approx \frac{3h}{8}\left[f_0 + 3\sum_{i \ne 3k} f_i + 2\sum_{i = 3k} f_i + f_n\right]
$$

**The most common exam mistake:** Assuming 4 points means $n = 4$. Remember: 4 points means **3 subintervals**, so $n = 3$ and $h = \frac{b - a}{3}$.

**Time estimate in exam:** ~6 minutes for a single-panel problem.

---

## 🔗 Connected Topics

- [← NM-5.2: Simpson's 1/3 Rule](NM-5.2_Simpsons_One_Third.md) -- the more accurate fourth-order sibling that requires an even interval count.
- [→ NM-5.4: Rule Comparison](NM-5.4_Rule_Comparison.md) -- head-to-head structural comparison between 1/3 and 3/8 rules.
- [NM-5.7: Applied Integration](NM-5.7_Applied_Integration.md) -- using 3/8 in mixed strategies for odd-interval datasets.

---

[← Previous: NM-5.2 Simpson's 1/3 Rule](NM-5.2_Simpsons_One_Third.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: NM-5.4 Rule Comparison →](NM-5.4_Rule_Comparison.md)
