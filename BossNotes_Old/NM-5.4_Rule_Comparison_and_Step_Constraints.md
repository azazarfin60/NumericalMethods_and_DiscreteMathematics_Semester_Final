[← Previous: NM-5.2 Simpson's 1/3 Rule](NM-5.2_Simpsons_One_Third_Rule.md) | [🏠 Index](00_Index.md) | [Next: NM-5 Lower — Trapezoidal, 3/8, Romberg →](NM-5_Lower_Trapezoidal_38_Romberg_Error_Applied.md)

---

# NM-5.4: Rule Comparison & Step Constraints
> **Section:** A (Numerical Methods) | **Priority:** 🔴 | **Exam Frequency:** 2/8 years
> **Sources:** Jain Ch.6 §6.5–§6.6, Shishir Notes §04 pp.53–72

## Why This Topic Matters

"Compare Simpson's 1/3 and 3/8 rules" appeared in 2020 and 2023. It is a short theory question worth 3 marks, and it tests whether you understand the structural difference between the two rules: the subinterval constraint. Getting this comparison right also helps you handle the mixed-rule problems where one rule fails because of an odd interval count.

---

## 📝 Key Definitions

> **Newton-Cotes formulas:** A family of numerical integration formulas that approximate $\int_a^b f(x)\,dx$ by fitting a polynomial through equally spaced data points and integrating the polynomial exactly. The trapezoidal rule, Simpson's 1/3, and Simpson's 3/8 are the first three members.

> **Order of accuracy:** The power of $h$ in the leading error term. A method with error $O(h^p)$ has order $p$. Higher order means faster convergence as $h$ shrinks.

---

## The Master Comparison Table

This table is the exam answer. Learn it.

| Property | Trapezoidal | Simpson's 1/3 | Simpson's 3/8 | Romberg |
| :-- | :-- | :-- | :-- | :-- |
| **Polynomial degree** | Linear (1) | Quadratic (2) | Cubic (3) | Uses trapezoidal + extrapolation |
| **Nodes per panel** | 2 | 3 | 4 | Varies |
| **Subintervals per panel** | 1 | 2 | 3 | — |
| **Constraint on $n$** | Any $n \ge 1$ | $n$ must be **even** | $n$ must be a **multiple of 3** | $n = 2^k$ (halving sequence) |
| **Weights** | $1, 1$ | $1, 4, 1$ | $1, 3, 3, 1$ | — |
| **Prefactor** | $\frac{h}{2}$ | $\frac{h}{3}$ | $\frac{3h}{8}$ | — |
| **Order of accuracy** | $O(h^2)$ | $O(h^4)$ | $O(h^4)$ | $O(h^{2k})$ for $k$-th column |
| **Leading error term** | $-\frac{h^3}{12}f''$ | $-\frac{h^5}{90}f^{(4)}$ | $-\frac{3h^5}{80}f^{(4)}$ | Depends on column |
| **Error constant** | $\frac{1}{12} = 0.0833$ | $\frac{1}{90} = 0.0111$ | $\frac{3}{80} = 0.0375$ | — |
| **Halving $h$ divides error by** | 4 | 16 | 16 | $4^k$ |
| **Exact for degree $\le$** | 1 | 3 | 3 | Depends on depth |

---

## Subinterval Constraints Explained

This is the part that costs marks. The constraints come from the panel structure.

### Simpson's 1/3: $n$ must be even

Each panel uses 2 subintervals (3 nodes). So the total number of subintervals must be divisible by 2. With $n$ odd, there is one leftover interval that cannot form a complete panel.

**Example:** 6 data points = 5 intervals. Five is odd. Simpson's 1/3 alone fails.

### Simpson's 3/8: $n$ must be a multiple of 3

Each panel uses 3 subintervals (4 nodes). So $n$ must be divisible by 3.

**Example:** 6 data points = 5 intervals. Five is not a multiple of 3 either. But $3 + 2 = 5$, so use 3/8 for three intervals and 1/3 for the remaining two.

### Trapezoidal: any $n$

Each panel uses 1 subinterval (2 nodes). Works for any $n \ge 1$. No constraint.

### Romberg: $n = 2, 4, 8, \ldots$

Romberg needs trapezoidal values at successively halved step sizes: $h$, $h/2$, $h/4$, etc. This means $n$ doubles each row.

---

## Accuracy at Equal Step Size

Both Simpson's rules are fourth order ($O(h^4)$). But the error constants differ:

$$
\text{Simpson's 1/3: } \frac{1}{90} = 0.0111, \qquad \text{Simpson's 3/8: } \frac{3}{80} = 0.0375
$$

The ratio is $\frac{3/80}{1/90} = 3.375$. For the same $h$, **Simpson's 3/8 has 3.375 times more error** than 1/3.

So 1/3 is the default choice. Use 3/8 only when the interval count forces it.

---

## The Mixed Strategy for Odd $n$

When $n$ is odd and not a multiple of 3, no single rule covers all intervals. The standard fix:

1. **Strategy A:** Apply Simpson's 1/3 to the largest even block, then the trapezoid rule to the one leftover interval.
2. **Strategy B:** Apply Simpson's 3/8 to three intervals and Simpson's 1/3 to the remaining (even number of) intervals.
3. **Strategy C:** Apply trapezoid to the first interval, then Simpson's 1/3 to the rest (which is now even).

All three strategies are legal. They give slightly different answers because they use different approximation methods on different parts of the interval. The difference is small.

> [!TIP] The 2020 Q.6(b) op-amp problem uses exactly this situation
> 5 intervals: Simpson's 1/3 on 4, trapezoid on 1. See [NM-5.2](NM-5.2_Simpsons_One_Third_Rule.md) for the full worked example.

---

## Why Both Rules Are Fourth Order

A natural question: Simpson's 1/3 uses a quadratic (degree 2), but it is exact for cubics (degree 3). Simpson's 3/8 uses a cubic (degree 3) and is also exact for cubics. Why do both reach fourth-order accuracy?

The answer is symmetry. Each panel is symmetric about its centre. The odd-order error terms cancel due to this symmetry. So the first surviving error term involves $f^{(4)}$, giving $O(h^4)$ for both rules.

This is also why the trapezoidal rule (linear, degree 1) has $O(h^2)$ accuracy. It is exact for linears (degree 1), and the symmetry argument bumps it up by one more degree.

---

## 🏆 Golden Questions (Past Exam Archive)

### 🎯 Compare Simpson's 1/3rd and 3/8th rules.
> **Appeared:** 2020 Q.6(a), 2023 Q.4(c) — (03 marks)

**Full Answer:**

Both are Newton-Cotes rules. They fit a polynomial through equally spaced nodes and integrate that polynomial exactly over the panel.

| | Simpson's $1/3$ | Simpson's $3/8$ |
| :-- | :-- | :-- |
| Subintervals per panel | 2 | 3 |
| Nodes per panel | 3 | 4 |
| Weights | $1,\ 4,\ 1$ | $1,\ 3,\ 3,\ 1$ |
| Prefactor | $\frac{h}{3}$ | $\frac{3h}{8}$ |
| Panel interval count | Must be **even** | Must be a **multiple of 3** |
| Total intervals $n$ | Even | Multiple of 3 |
| Order of accuracy | 4 | 4 |
| Leading error term | $-\frac{h^5}{90}f^{(4)}$ | $-\frac{3h^5}{80}f^{(4)}$ |
| Error constant | $\frac{1}{90} = 0.0111$ | $\frac{3}{80} = 0.0375$ |

Both are fourth order, so both need $f^{(4)}$ continuous. With the same $h$, Simpson's 3/8 has a leading error constant 3.375 times larger than 1/3. So for equal $h$, **1/3 is more accurate** and is the default choice.

The one place 3/8 wins: when the total interval count is odd, 1/3 is stuck while 3/8 can handle three of the intervals. Five intervals is the standard case. Use 3/8 for three and something else for two.

$$
\boxed{\text{Both are fourth order; } 1/3 \text{ is more accurate at equal } h \text{ but needs an even interval count}}
$$

---

## ⚡ Exam Tips & Common Mistakes

1. **Memorise the constraint:** 1/3 needs $n$ even, 3/8 needs $n$ divisible by 3, trapezoidal works for any $n$.
2. **Both Simpson's rules are $O(h^4)$.** Do not write $O(h^2)$ for Simpson's. That is the trapezoidal rule.
3. **The comparison table is the answer.** For a 3-mark question, draw the table and add one sentence about the mixed strategy. No derivation needed.
4. **Know the error constants.** $\frac{1}{90}$ for 1/3 and $\frac{3}{80}$ for 3/8. Their ratio is 3.375.

## 🔗 Related Topics

- [NM-5.2: Simpson's 1/3 Rule](NM-5.2_Simpsons_One_Third_Rule.md) — derivation, exactness proof, worked examples
- [NM-5 Lower: Trapezoidal, 3/8, Romberg](NM-5_Lower_Trapezoidal_38_Romberg_Error_Applied.md) — trapezoidal rule, Simpson's 3/8 worked example, Romberg method
- [NM-4.6: Lagrange's Interpolation](NM-4.6_Lagranges_Interpolation.md) — Simpson's 1/3 derivation uses Lagrange basis

---

[← Previous: NM-5.2 Simpson's 1/3 Rule](NM-5.2_Simpsons_One_Third_Rule.md) | [🏠 Index](00_Index.md) | [Next: NM-5 Lower — Trapezoidal, 3/8, Romberg →](NM-5_Lower_Trapezoidal_38_Romberg_Error_Applied.md)
