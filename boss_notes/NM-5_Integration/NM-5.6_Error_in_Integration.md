[← Previous: NM-5.5 Romberg's Method](NM-5.5_Rombergs_Method.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: NM-5.7 Applied Integration →](NM-5.7_Applied_Integration.md)

---

# NM-5.6: Error in Integration

> 🟠 **Priority:** Secondary | **Tested:** 2 appearances (2018 Q.6(b), 2018 Q.6(a) / 2023 Q.4(b)) | **Typical marks:** 4

## What This Is (and Why It Matters)

Whenever you use a numerical method to compute an integral, you are replacing the true continuous curve with a polynomial approximation. Because the polynomial is not the exact function, your answer will contain an error.

Error analysis in numerical integration answers three vital questions for engineers:
1. **How fast does the error shrink?** (Is it proportional to $h^2$ or $h^4$?)
2. **How many segments do I need?** How do you choose $n$ ahead of time so that you are guaranteed that the error is smaller than $0.01$?
3. **How do I measure the error after computing?** What is the exact mathematical difference between true error $E_t$ and absolute relative percentage error $|\varepsilon_t|$?

In RUET semester exams, error analysis questions appear directly inside problems:
- Finding the required number of segments $n$ using the theoretical error bound (2018 Q.6(b)).
- Calculating true error $E_t$ and relative true error $|\varepsilon_t|$ for rocket velocity integration (2018 Q.6(a), 2023 Q.4(b)).

---

## 📝 Key Definitions

> **Local Truncation Error:** "The error incurred in a single panel of width $h$ by replacing the integrand $f(x)$ with an interpolating polynomial." -- Jain, §6.4.1
>
> **In simple words:** The slice of error you introduce across just one little strip. For the trapezoidal rule, the local error is $-\frac{h^3}{12}f''(\xi)$.

> **Global (Composite) Truncation Error:** "The sum of all local truncation errors over the entire interval of integration $[a, b]$ across all $n$ panels." -- Jain, §6.4.1
>
> **In simple words:** The total error accumulated across the whole integration range. Because there are $n = \frac{b-a}{h}$ panels, multiplying local error by $n$ cancels one power of $h$, so a local $h^3$ becomes a global $h^2$.

> **True Error vs Absolute Relative True Error:** "True error is defined as $E_t = \text{True Value} - \text{Approximate Value}$, while absolute relative true error is $|\varepsilon_t| = |\frac{E_t}{\text{True Value}}| \times 100\%$." -- Jain, §1.3
>
> **In simple words:** True error tells you the actual numerical difference (with units like meters). Relative true error tells you what percentage that error represents compared to the true answer.

---

## The Master Summary of Error Terms

Here is the complete theoretical error breakdown across all major Newton-Cotes rules:

| Integration Rule | Local Error (Per Panel) | Global Error (Composite) | Order of Accuracy | Exact For Polynomials |
|:---|:---|:---|:---:|:---:|
| **Trapezoidal Rule** | $-\frac{h^3}{12}f''(\xi)$ | $-\frac{(b-a)h^2}{12}f''(\xi)$ | $O(h^2)$ | Degree $\le 1$ |
| **Simpson's 1/3 Rule** | $-\frac{h^5}{90}f^{(4)}(\xi)$ | $-\frac{(b-a)h^4}{180}f^{(4)}(\xi)$ | $O(h^4)$ | Degree $\le 3$ |
| **Simpson's 3/8 Rule** | $-\frac{3h^5}{80}f^{(4)}(\xi)$ | $-\frac{3(b-a)h^4}{80}f^{(4)}(\xi)$ | $O(h^4)$ | Degree $\le 3$ |
| **Boole's Rule ($n = 4$)** | $-\frac{8h^7}{945}f^{(6)}(\xi)$ | $-\frac{2(b-a)h^6}{945}f^{(6)}(\xi)$ | $O(h^6)$ | Degree $\le 5$ |

### Why One Power of $h$ Disappears in the Composite Error

Notice that the local error of the trapezoid rule contains $h^3$, but the composite error contains $h^2$. Why?
Because you sum the error across $n$ panels:

$$
E_{\text{composite}} \approx \sum_{i=1}^n \left(-\frac{h^3}{12}f''(\xi_i)\right) \approx -\frac{h^3}{12} \cdot n \cdot f''(\bar{\xi})
$$

Since $n = \frac{b - a}{h}$, substitute for $n$:

$$
E_{\text{composite}} \approx -\frac{h^3}{12}\left(\frac{b - a}{h}\right)f''(\bar{\xi}) = -\frac{(b - a)h^2}{12}f''(\bar{\xi})
$$

One power of $h$ is absorbed by the number of panels $n$. Similarly, for Simpson's 1/3 rule, local $h^5$ becomes composite $h^4$.

---

## How to Determine Segment Count $n$ for a Target Error

When an exam question asks: *"Determine the value of $n$ so that the approximation has error less than $\epsilon$"*, follow this exact four-step recipe:

1. **Find the required derivative:**
   - For the trapezoidal rule, compute $f''(x)$.
   - For Simpson's rule, compute $f^{(4)}(x)$.
2. **Find the maximum absolute value on $[a, b]$:**
   - Evaluate $|f''(x)|$ (or $|f^{(4)}(x)|$) across $[a, b]$ and identify its absolute maximum value $M = \max_{x \in [a, b]}|f''(x)|$.
3. **Set up the bound inequality:**
   - For trapezoidal: $\frac{(b - a)h^2}{12} M < \epsilon$.
   - Substitute $h = \frac{b - a}{n}$ to express the bound in terms of $n$:
     $$
     \frac{(b - a)^3}{12 n^2} M < \epsilon \implies n^2 > \frac{(b - a)^3 M}{12 \epsilon} \implies n > \sqrt{\frac{(b - a)^3 M}{12 \epsilon}}
     $$
4. **Round UP to the next integer:**
   - Always take the ceiling of your calculated value. For example, if $n > 2.8868$, choose $n = 3$.

---

## 🔧 Worked Example 1: Segment Selection from Error Bound

> **From:** 2018 Q.6(b) [Marks: 04]

**The question:** Determine the value of $n$ so that the trapezoidal rule will approximate the value of $\int_0^1 \sqrt{1 + x^2} \, dx$ with an error that is less than $0.01$.

**Solution summary (worked in full in [NM-5.1](NM-5.1_Trapezoidal_Rule.md)):**
Here $a = 0, b = 1$, and $f(x) = \sqrt{1 + x^2}$.
The second derivative is:

$$
f''(x) = \frac{1}{(1 + x^2)^{3/2}}
$$

On the interval $[0, 1]$, the denominator is minimized at $x = 0$, so $|f''(x)|$ attains its maximum value at $x = 0$:

$$
\max_{x \in [0, 1]}|f''(x)| = f''(0) = 1
$$

Substitute into the error bound:

$$
|E| \le \frac{(1 - 0)h^2}{12}(1) = \frac{h^2}{12} < 0.01
$$

$$
h^2 < 0.12 \implies h < 0.3464
$$

Solve for $n$:

$$
n = \frac{1}{h} > \frac{1}{0.3464} \approx 2.8868
$$

Since $n$ must be an integer, the smallest acceptable integer is:

$$
\boxed{n = 3}
$$

---

## 🔧 Worked Example 2: True Error and Relative True Error

> **From:** 2018 Q.6(a), 2023 Q.4(b)

When evaluating rocket vertical distance:

$$
x = \int_8^{30} \left( 2000 \ln \left[ \frac{140000}{140000 - 2100t} \right] - 9.8t \right) dt
$$

The exact analytical integral (computed via integration by parts) is:

$$
x_{\text{exact}} = 11061.3355\text{ m}
$$

### Variant A: Eight-Segment Simpson's 1/3 (2018 Q.6(a))
With $n = 8$ segments, the numerical approximation gives:

$$
x \approx 11061.3548\text{ m}
$$

The true error:

$$
E_t = x_{\text{exact}} - x \approx 11061.3355 - 11061.3548 = -0.0193\text{ m}
$$

$$
\boxed{E_t \approx -0.0193\ \text{m}}
$$

The absolute relative true error:

$$
|\varepsilon_t| = \left|\frac{-0.0193}{11061.3355}\right| \times 100\% \approx 0.00017\%
$$

$$
\boxed{|\varepsilon_t| \approx 0.00017\%}
$$

---

### Variant B: Single-Application Simpson's 1/3 (2023 Q.4(b))
With $n = 2$ segments ($h = 11\text{ s}$), the numerical approximation gives:

$$
x \approx 11065.72\text{ m}
$$

The true error:

$$
E_t = I_{\text{exact}} - x = 11061.34 - 11065.72 = -4.38\text{ m}
$$

$$
\boxed{\text{(ii) } E_t = -4.38\text{ m}}
$$

The absolute relative true error:

$$
|\epsilon_t| = \left|\frac{-4.38}{11061.34}\right| \times 100\% \approx 0.0396\%
$$

$$
\boxed{\text{(iii) } |\epsilon_t| = 0.0396\%}
$$

---

### Comparing the Errors: Visualizing $O(h^4)$ Convergence

Look at the dramatic difference between the two variants:

| Configuration | Subintervals $n$ | Step Size $h$ | Approximate $x$ | True Error $E_t$ | Relative Error $\lvert\varepsilon_t\rvert$ |
|:---|:---:|:---:|:---|:---:|:---:|
| **Single application (2023)** | 2 | 11.00 s | 11065.72 m | $-4.38\text{ m}$ | $0.0396\%$ |
| **Composite 8-segment (2018)** | 8 | 2.75 s | 11061.3548 m | $-0.0193\text{ m}$ | $0.00017\%$ |

When we reduced $h$ from $11\text{ s}$ to $2.75\text{ s}$ (dividing $h$ by 4), the true error shrank from $4.38\text{ m}$ to $0.0193\text{ m}$. 
Notice that $4^4 = 256$, and $\frac{4.38}{0.0193} \approx 227$. This 227-fold error reduction confirms the theoretical fourth-order $O(h^4)$ convergence rate in action.

---

### Exam Variants at a Glance

| Year | What They Asked | Key Method | Key Answer |
|:---|:---|:---|:---|
| 2018 Q.6(b) | Minimum $n$ for error $< 0.01$ | Solve $\frac{(b-a)h^2}{12}\max\lvert f''\rvert < 0.01$ | $\boxed{n = 3}$ |
| 2018 Q.6(a)(ii) | Rocket true error ($n = 8$) | $x_{\text{exact}} - x$ | $\boxed{E_t \approx -0.0193\ \text{m}}$ |
| 2018 Q.6(a)(iii) | Rocket relative error ($n = 8$) | $\lvert E_t / x_{\text{exact}}\rvert \times 100\%$ | $\boxed{\lvert\varepsilon_t\rvert \approx 0.00017\%}$ |
| 2023 Q.4(b)(ii) | Rocket true error ($n = 2$) | $I_{\text{exact}} - x$ | $\boxed{\text{(ii) } E_t = -4.38\text{ m}}$ |
| 2023 Q.4(b)(iii) | Rocket relative error ($n = 2$) | $\lvert E_t / I_{\text{exact}}\rvert \times 100\%$ | $\boxed{\text{(iii) } \lvert\epsilon_t\rvert = 0.0396\%}$ |

---

## ⚡ Quick Review

**The method in one sentence:** Global error is bounded by $\frac{(b-a)h^p}{C}\max|f^{(p)}|$, which allows determining the required segment count $n$ and calculating true and relative errors.

**The key bound formulas to memorize:**

$$
\text{Trapezoidal: } |E| \le \frac{(b - a)h^2}{12}\max|f''|, \qquad \text{Simpson's 1/3: } |E| \le \frac{(b - a)h^4}{180}\max|f^{(4)}|
$$

**The most common exam mistake:** Forgetting the minus sign in true error ($E_t = \text{Exact} - \text{Approximate}$, so an overestimate yields a negative true error).

**Time estimate in exam:** ~4 minutes for error percentage; ~6 minutes for derivative maximization and $n$ calculation.

---

## 🔗 Connected Topics

- [← NM-5.5: Romberg's Method](NM-5.5_Rombergs_Method.md) -- uses the known order of error to cancel terms via Richardson extrapolation.
- [→ NM-5.7: Applied Integration](NM-5.7_Applied_Integration.md) -- applies error analysis to real-world rocket and circuit telemetry.
- [NM-1.4: Error Types and Sources](../NM-1_Error_Analysis/NM-1.4_Error_Types.md) -- foundational theory of truncation error and round-off error.

---

[← Previous: NM-5.5 Romberg's Method](NM-5.5_Rombergs_Method.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: NM-5.7 Applied Integration →](NM-5.7_Applied_Integration.md)
