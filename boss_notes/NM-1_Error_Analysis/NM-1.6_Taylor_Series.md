[← Previous: NM-1.5 Error Propagation](NM-1.5_Error_Propagation.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: NM-1.7 Programming & Software →](NM-1.7_Programming_and_Software.md)

---

# NM-1.6: Taylor Series and Truncation Error

> 🔴 ⚠️ **Priority:** Critical (Danger Zone -- missed in some class notes) | **Tested:** 6/8 years | **Typical marks:** 3–4

## What This Is (and Why It Matters)

Taylor series is the mathematical backbone of almost all numerical methods. When you use Newton-Raphson, numerical differentiation, or Runge-Kutta ODE solvers, you are secretly using Taylor series under the hood.

In this subtopic, the exam asks three specific styles of questions:
1. **Expand and approximate:** Write down a polynomial (like 3rd-order for $e^x$) and estimate its truncation error at a specific point.
2. **Find the number of terms:** How many terms of a series do you need so the answer is guaranteed correct to 5 decimal places?
3. **Catastrophic cancellation:** Why evaluating $e^{-5}$ by adding and subtracting terms directly fails horribly on a computer, and why calculating $\frac{1}{e^5}$ fixes it completely.

> [!WARNING] Danger Zone: Missing From Some Class Notes
> This subtopic is absent from Raidah's class notes, yet it appeared in 6 out of 8 exam papers. If you only relied on student notes, you would miss this major question block entirely. Master every derivation below.

---

## 📝 Key Definitions

> **Taylor series:** "If $f(x)$ is continuous and possesses continuous derivatives of all orders in an interval containing $a$, then $f(x) = f(a) + (x-a)f'(a) + \frac{(x-a)^2}{2!}f''(a) + \cdots + \frac{(x-a)^n}{n!}f^{(n)}(a) + R_n$." -- Jain, §1.5
> 
> **In simple words:** A formula that expresses any smooth mathematical curve as an infinite polynomial using its derivatives evaluated at a single known starting point.

> **Lagrange remainder (truncation error bound):** "$R_n = \frac{f^{(n+1)}(\xi)}{(n+1)!}(x-a)^{n+1}$ for some $\xi$ between $a$ and $x$." -- Jain, §1.5
> 
> **In simple words:** The exact mathematical formula for the chunk of the infinite series that you threw away. It tells you the maximum possible error in your polynomial estimate.

> **Maclaurin series:** The special case of a Taylor series when the base expansion point is $a = 0$.
> 
> **In simple words:** Expanding a function directly around zero: $f(x) = f(0) + x f'(0) + \frac{x^2}{2} f''(0) + \dots$.

---

## The Core Idea

### The Formula

The Taylor series of $f(x)$ expanded around $x = a$ is:
$$
f(x) = \sum_{n=0}^{\infty} \frac{f^{(n)}(a)}{n!}(x - a)^n
$$
Written out term by term:
$$
f(x) = f(a) + (x-a)f'(a) + \frac{(x-a)^2}{2!}f''(a) + \frac{(x-a)^3}{3!}f'''(a) + \dots
$$
When expanded around $a = 0$, we call it the **Maclaurin series**:
$$
f(x) = f(0) + x f'(0) + \frac{x^2}{2!}f''(0) + \frac{x^3}{3!}f'''(0) + \dots
$$

### The Remainder (How to Bound Truncation Error)

When we stop the polynomial after degree $n$ (retaining $n+1$ terms), the discarded remainder is given by Lagrange's formula:
$$
R_n(x) = \frac{f^{(n+1)}(\xi)}{(n+1)!}(x - a)^{n+1}, \qquad \xi \in (a, x)
$$
We do not know the exact value of $\xi$ inside the interval $(a, x)$. But we don't need to! To get an unbreakable **upper bound**, we simply find the maximum possible value that $|f^{(n+1)}(\xi)|$ could reach anywhere in the interval $[a, x]$:
$$
|R_n(x)| \le \frac{\max_{\xi \in [a, x]} |f^{(n+1)}(\xi)|}{(n+1)!} |x - a|^{n+1}
$$

### The Golden Rule: "Correct to $n$ Decimal Places"

Memorize this criterion permanently:

> **"Correct to $n$ decimal places" means:**
> $$
> \text{Error} < \frac{1}{2} \times 10^{-n}
> $$

For example, "correct to 5 decimal places" means the error must be strictly less than $0.5 \times 10^{-5} = 5 \times 10^{-6}$. If you forget the $\frac{1}{2}$ factor and write $< 10^{-5}$, you will miscalculate the required number of terms!

### Standard Series You Must Know by Heart

| Function | Maclaurin Series ($a = 0$) | Convergence Radius |
| :-- | :-- | :--: |
| $e^x$ | $1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \dots$ | All $x \in (-\infty, \infty)$ |
| $\sin x$ | $x - \frac{x^3}{3!} + \frac{x^5}{5!} - \dots$ | All $x \in (-\infty, \infty)$ |
| $\cos x$ | $1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \dots$ | All $x \in (-\infty, \infty)$ |
| $\ln(1+x)$ | $x - \frac{x^2}{2} + \frac{x^3}{3} - \frac{x^4}{4} + \dots$ | $|x| < 1$ (Diverges for $|x| \ge 1$!) |
| $\ln\left(\frac{1+y}{1-y}\right)$ | $2\left(y + \frac{y^3}{3} + \frac{y^5}{5} + \dots\right)$ | $|y| < 1$ |

---

## 🔧 Worked Example: 3rd-Order Taylor of $e^x$ at $x = 0.5$

> **From:** 2024 Q.1(b) -- [Marks: 03]

**The question:** Derive the third-order Taylor series expansion of $f(x) = e^x$ around $x = 0$. Estimate the truncation error at $f(0.5)$.

**Let's solve this step by step.**

**Step 1: Compute derivatives at $x = 0$.**
For $f(x) = e^x$, every derivative is $e^x$. Therefore:
$$
f(0) = 1, \quad f'(0) = 1, \quad f''(0) = 1, \quad f'''(0) = 1, \quad f^{(4)}(0) = 1
$$

**Step 2: Construct the third-order polynomial $P_3(x)$.**
Keeping terms up to power $x^3$:
$$
P_3(x) = f(0) + x f'(0) + \frac{x^2}{2!} f''(0) + \frac{x^3}{3!} f'''(0)
$$
Substituting values:
$$
\boxed{e^x \approx P_3(x) = 1 + x + \frac{x^2}{2} + \frac{x^3}{6}}
$$

**Step 3: Evaluate at $x = 0.5$.**
$$
\begin{aligned}
P_3(0.5) &= 1 + 0.5 + \frac{(0.5)^2}{2} + \frac{(0.5)^3}{6} \\
&= 1 + 0.5 + \frac{0.25}{2} + \frac{0.125}{6} \\
&= 1 + 0.5 + 0.125 + 0.02083333 \\
&= 1.6458333
\end{aligned}
$$

**Step 4: Compute exact truncation error.**
Using true $e^{0.5} \approx 1.64872127$:
$$
|E_3| = |e^{0.5} - P_3(0.5)| = |1.64872127 - 1.64583333| = 0.00288794
$$

**Step 5: Estimate the error bound using the Lagrange remainder.**
The remainder is:
$$
R_3(x) = \frac{f^{(4)}(\xi)}{4!} x^4 = \frac{e^\xi}{24} x^4, \qquad 0 < \xi < 0.5
$$
Since $e^\xi$ is strictly increasing, its maximum on $[0, 0.5]$ occurs at the right endpoint $\xi = 0.5$:
$$
|R_3| \le \frac{e^{0.5}}{24} (0.5)^4 = \frac{1.6487213}{24} \times 0.0625 \approx 0.0042935
$$
The exact error ($0.0028879$) comfortably satisfies the upper bound ($0.0042935$).

$$
\boxed{P_3(0.5) = 1.6458333, \qquad |E_3| = 0.0028879 \le 0.0042935}
$$

---

## 🏆 Past Exam Questions

### 2017 Q.1(c): Evaluate $e^{-5}$ using two approaches and compare [04 marks]

**The question:** Evaluate $e^{-5}$ using two approaches and compare with the true value $6.737947 \times 10^{-3}$.

**Solution:**

**Approach A: The alternating series directly ($x = -5$).**
We substitute $x = -5$ into the standard exponential series:
$$
e^{-5} = 1 - 5 + \frac{5^2}{2!} - \frac{5^3}{3!} + \frac{5^4}{4!} - \frac{5^5}{5!} + \dots
$$
Let's see what happens to the partial sums $S_k$:
- $k=1$: $S_1 = 1$
- $k=2$: $S_2 = 1 - 5 = -4$
- $k=3$: $S_3 = -4 + 12.5 = +8.5$
- $k=4$: $S_4 = 8.5 - 20.8333 = -12.3333$
- $k=5$: $S_5 = -12.3333 + 26.0417 = +13.7083$
- ...
- $k=15$: $S_{15} = 2.4457 \times 10^{-2}$ (Error is $1.772 \times 10^{-2}$, which is massive!)

Notice that the individual terms swell up to $26.0417$ (which is roughly **3,866 times larger** than the final answer $0.006738$). The large positive and negative numbers cancel each other out, wiping out the machine's precision digits. This is **catastrophic cancellation**.

**Approach B: Reciprocal of the positive series ($e^{-5} = \frac{1}{e^5}$).**
We compute $e^5$ first where every single term is positive:
$$
e^5 = 1 + 5 + \frac{5^2}{2!} + \frac{5^3}{3!} + \frac{5^4}{4!} + \dots
$$
The partial sum $T_k$ grows monotonically:
- $k=5$: $T_5 = 65.3750 \implies \frac{1}{T_5} = 1.5296 \times 10^{-2}$
- $k=10$: $T_{10} = 143.6895 \implies \frac{1}{T_{10}} = 6.9595 \times 10^{-3}$
- $k=15$: $T_{15} = 148.3796 \implies \frac{1}{T_{15}} = 6.7395 \times 10^{-3}$ (Error is only $1.525 \times 10^{-6}$!)

**Comparison Table:**

| Feature | Approach A ($e^{-5}$) | Approach B ($1/e^5$) |
| :-- | :-- | :-- |
| **Signs** | Alternating ($+ - + -$) | Strictly positive ($++++$) |
| **Cancellation** | Catastrophic precision loss | Zero cancellation |
| **Convergence** | Oscillates violently before settling | Smooth, monotone convergence |
| **Accuracy at 15 terms** | Error $\approx 1.77 \times 10^{-2}$ | Error $\approx 1.53 \times 10^{-6}$ |

$$
\boxed{\text{Approach A is unusable at } x = 5; \text{ Approach B reaches } 6.7395\times10^{-3} \text{ in 15 terms}}
$$

---

### 2018 Q.1(c): Number of terms for $e^x$ correct to 5 d.p. on $[0, 1]$ [04 marks]

**Solution:**
We write the Maclaurin expansion of $e^x$:
$$
e^x = 1 + x + \frac{x^2}{2!} + \dots + \frac{x^{k-1}}{(k-1)!} + R_k(x)
$$
After keeping $k$ terms, the Lagrange remainder is:
$$
R_k(x) = \frac{e^\xi}{k!} x^k, \qquad 0 < \xi < x
$$
For $x \in [0, 1]$, the maximum error occurs at the upper bound $x = 1$:
$$
|R_k| \le \frac{e^1}{k!} (1)^k = \frac{e}{k!} \approx \frac{2.718282}{k!}
$$
The condition "correct to 5 decimal places" requires:
$$
|R_k| < \frac{1}{2} \times 10^{-5} = 5 \times 10^{-6}
$$

Let's test integer values of $k$:
- For $k = 8$:
$$
\frac{e}{8!} = \frac{2.718282}{40320} \approx 6.74 \times 10^{-5} > 5 \times 10^{-6} \quad (\text{Fails})
$$
- For $k = 9$:
$$
\frac{e}{9!} = \frac{2.718282}{362880} \approx 7.49 \times 10^{-6}
$$
Wait, let's check the exact sum at $x = 1$ with $k = 9$ terms:
$$
S_9 = \sum_{n=0}^{8} \frac{1}{n!} = 1 + 1 + \frac{1}{2} + \frac{1}{6} + \frac{1}{24} + \frac{1}{120} + \frac{1}{720} + \frac{1}{5040} + \frac{1}{40320} = 2.71827877
$$
The exact error is:
$$
|e - S_9| = |2.71828183 - 2.71827877| = 3.06 \times 10^{-6} < 5 \times 10^{-6} \quad (\text{Passes!})
$$
Therefore, exactly 9 terms are required.

$$
\boxed{9\ \text{terms}}
$$

---

### 2021 Q.1(c): Compute $\ln 3$ correct to 5 d.p. using Taylor series [04 marks]

**Solution:**

**Step 1: Check convergence radius (the classic trap!).**
The standard Maclaurin series for logarithm is:
$$
\ln(1+x) = x - \frac{x^2}{2} + \frac{x^3}{3} - \frac{x^4}{4} + \dots
$$
This series converges **only** for $-1 < x \le 1$. If you try to put $1 + x = 3 \implies x = 2$, the series **diverges** to infinity!

**Step 2: Use the hyperbolic logarithmic identity.**
We subtract the series for $\ln(1-y)$ from $\ln(1+y)$:
$$
\ln\left(\frac{1+y}{1-y}\right) = 2\left(y + \frac{y^3}{3} + \frac{y^5}{5} + \frac{y^7}{7} + \dots\right), \qquad |y| < 1
$$
We set the argument equal to 3:
$$
\frac{1+y}{1-y} = 3 \implies 1 + y = 3 - 3y \implies 4y = 2 \implies y = \frac{1}{2}
$$
Since $|1/2| < 1$, this series converges extremely rapidly!

**Step 3: Evaluate terms with $y = 0.5$.**
$$
\ln 3 = 2\left[\frac{1}{2} + \frac{1}{3(2^3)} + \frac{1}{5(2^5)} + \frac{1}{7(2^7)} + \frac{1}{9(2^9)} + \frac{1}{11(2^{11})} + \frac{1}{13(2^{13})} + \dots\right]
$$
Evaluating the terms inside:
- Term 1: $0.5$
- Term 2: $\frac{1}{24} \approx 0.04166667$
- Term 3: $\frac{1}{160} \approx 0.00625000$
- Term 4: $\frac{1}{896} \approx 0.00111607$
- Term 5: $\frac{1}{4608} \approx 0.00021701$
- Term 6: $\frac{1}{22528} \approx 0.00004439$
- Term 7: $\frac{1}{106496} \approx 0.00000939$
- Term 8: $\frac{1}{491520} \approx 0.00000203$

Summing 8 terms and multiplying by 2 yields $1.098611$. Rounded to 5 decimal places:
$$
\boxed{\ln 3 = 1.09861}
$$

---

### 2022 Q.1(b): Evaluate $f(1)$ using Taylor series for $f(x) = x^3 - 3x^2 + 5x - 10$ [04 marks]

**Solution:**

**Step 1: Compute derivatives of $f(x)$ at $x = 0$.**
$$
\begin{aligned}
f(x) &= x^3 - 3x^2 + 5x - 10 &\implies f(0) &= -10 \\
f'(x) &= 3x^2 - 6x + 5 &\implies f'(0) &= 5 \\
f''(x) &= 6x - 6 &\implies f''(0) &= -6 \\
f'''(x) &= 6 &\implies f'''(0) &= 6 \\
f^{(4)}(x) &= 0 &\implies f^{(4)}(0) &= 0
\end{aligned}
$$
All derivatives of order 4 and higher are identically zero!

**Step 2: Write the Taylor series about $a = 0$.**
$$
f(x) = f(0) + x f'(0) + \frac{x^2}{2!} f''(0) + \frac{x^3}{3!} f'''(0)
$$
Substituting our derivative values:
$$
f(x) = -10 + 5x + \frac{-6}{2}x^2 + \frac{6}{6}x^3 = -10 + 5x - 3x^2 + x^3
$$

**Step 3: Evaluate at $x = 1$.**
$$
f(1) = -10 + 5(1) - 3(1)^2 + (1)^3 = -10 + 5 - 3 + 1 = -7
$$

$$
\boxed{f(1) = -7}
$$

*(Note: Because $f(x)$ is a 3rd-degree polynomial, its 3rd-order Taylor polynomial is exact. The remainder is exactly 0!)*

---

### Exam Variants at a Glance

| Year | What They Asked | Key Boxed Takeaway |
| :--- | :--- | :--- |
| **2017 Q.1(c)** | $e^{-5}$ evaluated two ways | $\boxed{\text{Approach A is unusable at } x = 5; \text{ Approach B reaches } 6.7395\times10^{-3} \text{ in 15 terms}}$ |
| **2018 Q.1(c)** | Terms for $e^x$ correct to 5 d.p. on $[0,1]$ | $\boxed{9\ \text{terms}}$ |
| **2021 Q.1(c)** | $\ln 3$ correct to 5 d.p. | $\boxed{\ln 3 = 1.09861}$ |
| **2022 Q.1(b)** | $f(1)$ for cubic polynomial | $\boxed{f(1) = -7}$ |
| **2024 Q.1(b)** | Third-order Taylor of $e^x$, error at $x = 0.5$ | $\boxed{e^x \approx P_3(x) = 1 + x + \frac{x^2}{2} + \frac{x^3}{6}}$, $\boxed{P_3(0.5) = 1.6458333, \quad |E_3| = 0.0028879 \le 0.0042935}$ |

---

## ⚡ Quick Review

**The method in one sentence:** Taylor series approximates any function near a known point with a polynomial whose error is bounded by the next derivative's maximum magnitude divided by $(n+1)!$.

**The formula you must memorize:**
$$
f(x) \approx \sum_{k=0}^n \frac{f^{(k)}(a)}{k!}(x-a)^k, \qquad |R_n| \le \frac{\max |f^{(n+1)}(\xi)|}{(n+1)!}|x-a|^{n+1}
$$

**The most common exam mistake:** Forgetting to check the convergence radius for $\ln(1+x)$ (diverges for $x \ge 1$) and calculating $e^{-x}$ directly instead of using $1/e^x$.

**Time estimate in exam:** 8–10 minutes for a 4-mark calculation problem.

---

## 🔗 Connected Topics

- [← NM-1.4: Error Types](NM-1.4_Error_Types.md) -- where truncation error was first classified
- [← NM-1.5: Error Propagation](NM-1.5_Error_Propagation.md) -- how to bound errors in composite functions
- [→ NM-4: Curve Fitting Overview](../NM-4_Curve_Fitting/_Topic_Overview.md) -- finite-difference counterpart of Taylor series for discrete data

---

[← Previous: NM-1.5 Error Propagation](NM-1.5_Error_Propagation.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: NM-1.7 Programming & Software →](NM-1.7_Programming_and_Software.md)
