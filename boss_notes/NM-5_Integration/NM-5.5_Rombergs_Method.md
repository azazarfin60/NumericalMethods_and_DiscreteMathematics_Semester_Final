[← Previous: NM-5.4 Rule Comparison](NM-5.4_Rule_Comparison.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: NM-5.6 Error in Integration →](NM-5.6_Error_in_Integration.md)

---

# NM-5.5: Romberg's Method

> 🟠 **Priority:** Secondary | **Tested:** 3/8 years (2021, 2022, 2023) | **Typical marks:** 4

## What This Is (and Why It Matters)

Suppose you calculate an integral using the trapezoidal rule. It is simple, but its accuracy is only second-order ($O(h^2)$). To get high precision with plain trapezoids, you would have to calculate hundreds or thousands of function evaluations, which is painfully slow.

Romberg's method is a brilliant shortcut. You compute trapezoidal estimates at just three halved step sizes (say $h = 0.5$, $0.25$, and $0.125$). Then, instead of evaluating the function again, you recombine those numbers using **Richardson extrapolation** to cancel out the error terms mathematically.

With zero new function evaluations, your second-order trapezoid values transform into sixth-order ($O(h^6)$) accuracy.

In RUET exams, Romberg integration is tested consistently:
- **2021 Q.8(b) and 2023 Q.2(c):** Evaluating $\int_1^2 \frac{1}{2+x}\,dx$ with $h = 0.5, 0.25, 0.125$.
- **2022 Q.3(a):** Evaluating $\int_0^1 \frac{dx}{1+x^2}$ with $h = 0.5, 0.25, 0.125$.

---

## 📝 Key Definitions

> **Richardson Extrapolation:** "This method, due to L.F. Richardson, is called the deferred approach to the limit: by combining approximations at two step sizes $h$ and $h/2$, the leading error term can be eliminated." -- Jain, §6.4.6
>
> **In simple words:** A formula that takes two answers calculated with step size $h$ and $h/2$, cancels out their known error pattern, and produces a far more accurate third answer without re-evaluating the function.

> **Romberg Integration:** "The systematic tabulation of successive Richardson extrapolations applied to the trapezoidal rule is called Romberg integration." -- Jain, §6.4.6
>
> **In simple words:** A triangular table where Column 0 contains trapezoidal approximations, Column 1 contains Simpson-level ($O(h^4)$) approximations, and Column 2 contains Boole-level ($O(h^6)$) approximations.

> **Romberg Recursive Formula:** "The general entry in the Romberg table is given by $R_{k,j} = R_{k,j-1} + \frac{R_{k,j-1} - R_{k-1,j-1}}{4^j - 1}$." -- Jain, §6.4.6
>
> **In simple words:** To calculate any cell in column $j$, take the cell directly to its left, subtract the cell above-left, divide that difference by $4^j - 1$, and add it back. For Column 1, divide by 3; for Column 2, divide by 15.

---

## The Core Idea

### Why the Error Cancels

The composite trapezoidal rule has an error expansion containing only even powers of $h$:

$$
I = T(h) + c_1 h^2 + c_2 h^4 + c_3 h^6 + \cdots
$$

Now halve the step size to $h/2$:

$$
I = T(h/2) + c_1 \left(\frac{h}{2}\right)^2 + c_2 \left(\frac{h}{2}\right)^4 + \cdots = T(h/2) + \frac{c_1 h^2}{4} + \frac{c_2 h^4}{16} + \cdots
$$

Notice that the leading error term $c_1 h^2$ shrank by exactly a factor of 4. Multiply the second equation by 4:

$$
4I = 4T(h/2) + c_1 h^2 + \frac{c_2 h^4}{4} + \cdots
$$

Now subtract the first equation from this new equation:

$$
4I - I = 4T(h/2) - T(h) + \left(\frac{c_2}{4} - c_2\right)h^4 + \cdots
$$

$$
3I = 4T(h/2) - T(h) + O(h^4)
$$

Divide by 3:

$$
I = \frac{4T(h/2) - T(h)}{3} + O(h^4) = T(h/2) + \frac{T(h/2) - T(h)}{3} + O(h^4)
$$

The $h^2$ error term vanished completely. The new estimate has fourth-order ($O(h^4)$) accuracy, identical to Simpson's rule.

### The Systematic Romberg Table

Repeating this process at the next level cancels the $h^4$ term by dividing by $4^2 - 1 = 15$. Repeating again cancels the $h^6$ term by dividing by $4^3 - 1 = 63$.

The general table layout is:

$$
\begin{array}{c|ccc}
\text{Step Size } h & R_{k,0}\text{ (Trapezoidal, } O(h^2)\text{)} & R_{k,1}\text{ (Simpson-level, } O(h^4)\text{)} & R_{k,2}\text{ (Boole-level, } O(h^6)\text{)} \\
\hline
h & R_{1,0} = T(h) & & \\
h/2 & R_{2,0} = T(h/2) & R_{2,1} = R_{2,0} + \frac{R_{2,0} - R_{1,0}}{3} & \\
h/4 & R_{3,0} = T(h/4) & R_{3,1} = R_{3,0} + \frac{R_{3,0} - R_{2,0}}{3} & R_{3,2} = R_{3,1} + \frac{R_{3,1} - R_{2,1}}{15}
\end{array}
$$

### Step-by-Step Algorithm

1. **Step 1:** Compute composite trapezoidal estimates for $h_1 = h$, $h_2 = h/2$, and $h_3 = h/4$. Write them down in Column 0 as $R_{1,0}, R_{2,0}, R_{3,0}$.
2. **Step 2:** Form Column 1 by taking adjacent entries in Column 0, finding their difference, dividing by 3, and adding to the more refined value:
   $$
   R_{2,1} = R_{2,0} + \frac{R_{2,0} - R_{1,0}}{3}, \qquad R_{3,1} = R_{3,0} + \frac{R_{3,0} - R_{2,0}}{3}
   $$
3. **Step 3:** Form Column 2 by taking the two entries in Column 1, finding their difference, dividing by 15, and adding to the lower value:
   $$
   R_{3,2} = R_{3,1} + \frac{R_{3,1} - R_{2,1}}{15}
   $$
4. **Step 4:** The bottom-right entry $R_{3,2}$ is your final, highest-accuracy Romberg answer.

> [!WARNING] The Divisor Trap
> Never mix up the divisors. Column 1 always divides by $4^1 - 1 = 3$. Column 2 always divides by $4^2 - 1 = 15$. If you divide by 3 in Column 2, your higher-order error terms will not cancel.

---

## 🔧 Worked Example 1

> **From:** 2021 Q.8(b), 2023 Q.2(c) [Marks: 04]

**The question:** Use Romberg's method to compute: $\int_1^2 \frac{1}{2+x}\,dx$. Consider $h = 0.5, 0.25, 0.125$.

**Let us solve this step by step.**

**Step 1. Compute the first column (composite trapezoidal values).**
Here $f(x) = \frac{1}{2 + x}$ over $[1, 2]$.

- **At $h = 0.5$ ($n = 2$ intervals):**
  Nodes are $x_0 = 1, x_1 = 1.5, x_2 = 2$:
  $$
  f(1) = \frac{1}{3} \approx 0.333333, \quad f(1.5) = \frac{1}{3.5} \approx 0.285714, \quad f(2) = \frac{1}{4} = 0.250000
  $$
  $$
  T_2 = \frac{0.5}{2}\left[\frac{1}{3} + 2\left(\frac{1}{3.5}\right) + \frac{1}{4}\right] = 0.25[0.333333 + 0.571429 + 0.250000] = 0.288690
  $$
  So $R_{1,0} = 0.288690$.

- **At $h = 0.25$ ($n = 4$ intervals):**
  Nodes are $x = 1, 1.25, 1.5, 1.75, 2$:
  $$
  f(1) = \frac{1}{3}, \quad f(1.25) = \frac{1}{3.25} \approx 0.307692, \quad f(1.5) = \frac{1}{3.5} \approx 0.285714, \quad f(1.75) = \frac{1}{3.75} \approx 0.266667, \quad f(2) = \frac{1}{4}
  $$
  Interior sum: $0.307692 + 0.285714 + 0.266667 = 0.860073$.
  $$
  T_4 = \frac{0.25}{2}\left[\frac{1}{3} + 2(0.860073) + \frac{1}{4}\right] = 0.125[0.333333 + 1.720146 + 0.25] = 0.287935
  $$
  So $R_{2,0} = 0.287935$.

- **At $h = 0.125$ ($n = 8$ intervals):**
  Evaluating across all 8 subintervals:
  $$
  T_8 = 0.287745
  $$
  So $R_{3,0} = 0.287745$.

---

**Step 2. Compute the second column (divisor $4^1 - 1 = 3$).**

For Row 2:

$$
R_{2,1} = R_{2,0} + \frac{R_{2,0} - R_{1,0}}{3} = 0.287935 + \frac{0.287935 - 0.288690}{3} = 0.287935 - 0.000252 = 0.287683
$$

For Row 3:

$$
R_{3,1} = R_{3,0} + \frac{R_{3,0} - R_{2,0}}{3} = 0.287745 + \frac{0.287745 - 0.287935}{3} = 0.287745 - 0.000063 = 0.287682
$$

---

**Step 3. Compute the third column (divisor $4^2 - 1 = 15$).**

For Row 3:

$$
R_{3,2} = R_{3,1} + \frac{R_{3,1} - R_{2,1}}{15}
$$

Carried with full precision from intermediate values ($R_{2,1} = 0.2876832$ and $R_{3,1} = 0.2876821$):

$$
R_{3,2} = 0.2876821
$$

---

**Step 4. Construct the complete Romberg table.**

$$
\begin{array}{c|ccc}
R_{k,0} & R_{k,1} & R_{k,2} \\
\hline
0.288690 & & \\
0.287935 & 0.287683 & \\
0.287745 & 0.287682 & 0.287682
\end{array}
$$

$$
\boxed{I \approx 0.2876821}
$$

**Quick sanity check (by analytical integration):**

$$
\int_1^2 \frac{dx}{2 + x} = [\ln(2 + x)]_1^2 = \ln(4) - \ln(3) = \ln\left(\frac{4}{3}\right) \approx 0.2876820725
$$

The Romberg value $0.2876821$ matches the exact analytical answer to 7 decimal places. The absolute error is about $1 \times 10^{-7}$, whereas the raw trapezoidal rule at $h = 0.125$ was off by $6.3 \times 10^{-5}$. Romberg is more than 600 times more accurate from the exact same data points.

---

## 🔧 Worked Example 2

> **From:** 2022 Q.3(a) [Marks: 04]

**The question:** Compute the value of $I = \int_0^1 \frac{dx}{1 + x^2}$ using the trapezoidal rule with $h = 0.5, 0.25$ and $0.125$. Then obtain a better estimate using Romberg's method.

**Solution.**

**Step 1. Function values:**
Here $f(x) = \frac{1}{1 + x^2}$:

| $x$ | 0 | 0.125 | 0.25 | 0.375 | 0.5 | 0.625 | 0.75 | 0.875 | 1 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| $f(x)$ | 1.000000 | 0.984615 | 0.941176 | 0.876712 | 0.800000 | 0.719101 | 0.640000 | 0.566372 | 0.500000 |

**Step 2. Trapezoidal Column ($R_{k,0}$):**

- **At $h = 0.5$ ($n = 2$):**
  $$
  T_2 = \frac{0.5}{2}[1 + 2(0.8) + 0.5] = 0.25(3.1) = 0.775000
  $$

- **At $h = 0.25$ ($n = 4$):**
  $$
  T_4 = \frac{0.25}{2}[1 + 2(0.941176 + 0.8 + 0.64) + 0.5] = 0.125(6.262352) = 0.782794
  $$

- **At $h = 0.125$ ($n = 8$):**
  $$
  T_8 = 0.0625[1 + 2(5.527976) + 0.5] = 0.0625(12.555952) = 0.784747
  $$

**Step 3. Extrapolation Columns:**

- **Column 1 (divisor 3):**
  $$
  R_{2,1} = 0.782794 + \frac{0.782794 - 0.775000}{3} = 0.782794 + 0.002598 = 0.785392
  $$
  $$
  R_{3,1} = 0.784747 + \frac{0.784747 - 0.782794}{3} = 0.784747 + 0.000651 = 0.785398
  $$

- **Column 2 (divisor 15):**
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

*(Check: exact analytical value is $\arctan(1) = \frac{\pi}{4} \approx 0.7853981634$. Romberg error is $3.6 \times 10^{-7}$, whereas the raw trapezoid was off by $6.5 \times 10^{-4}$).*

---

### Exam Variants at a Glance

| Year | What They Asked | Step Sizes | Key Answer |
|:---|:---|:---|:---|
| 2021 Q.8(b) | Romberg for $\int_1^2 \frac{dx}{2+x}$ | $h = 0.5, 0.25, 0.125$ | $\boxed{I \approx 0.2876821}$ |
| 2022 Q.3(a) | Trapezoid + Romberg for $\int_0^1 \frac{dx}{1+x^2}$ | $h = 0.5, 0.25, 0.125$ | $\boxed{I \approx 0.7853985 \quad \text{(trapezoid alone gives } 0.784747\text{)}}$ |
| 2023 Q.2(c) | Romberg for $\int_1^2 \frac{dx}{2+x}$ | $h = 0.5, 0.25, 0.125$ | $\boxed{I \approx 0.2876821}$ |

---

## ⚡ Quick Review

**The method in one sentence:** Take trapezoidal approximations from halved step sizes and combine them with Richardson extrapolation ($4^j - 1$ divisors) to cancel error terms without extra evaluations.

**The extrapolation formula you must memorize:**

$$
R_{k,j} = R_{k,j-1} + \frac{R_{k,j-1} - R_{k-1,j-1}}{4^j - 1}
$$

**The divisors:**
- Column 1 ($j = 1$): divide difference by $4^1 - 1 = 3$.
- Column 2 ($j = 2$): divide difference by $4^2 - 1 = 15$.

**The most common exam mistake:** Flipping the numerator subtraction (writing $R_{k-1} - R_k$ instead of $R_k - R_{k-1}$) or dividing by 15 in Column 1.

**Time estimate in exam:** ~8 to 10 minutes to evaluate function values, trapezoid sums, and the 6-entry table.

---

## 🔗 Connected Topics

- [← NM-5.4: Rule Comparison](NM-5.4_Rule_Comparison.md) -- explains why error expansions have only even powers of $h$.
- [→ NM-5.6: Error in Integration](NM-5.6_Error_in_Integration.md) -- detailed theory of truncation error and convergence rates.
- [NM-5.1: Trapezoidal Rule](NM-5.1_Trapezoidal_Rule.md) -- provides the baseline evaluations that feed Column 0 of the Romberg table.

---

[← Previous: NM-5.4 Rule Comparison](NM-5.4_Rule_Comparison.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: NM-5.6 Error in Integration →](NM-5.6_Error_in_Integration.md)
