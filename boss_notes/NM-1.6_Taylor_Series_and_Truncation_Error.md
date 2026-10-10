[← Previous: NM-1.5 Error Representations](NM-1.5_Error_Representations_and_Propagation.md) | [🏠 Index](00_Index.md) | [Next: NM-1 Lower Tier →](NM-1_Lower_Modeling_Accuracy_Precision.md)

---

# NM-1.6: Taylor Series and Truncation Error
> **Section:** A (Numerical Methods) | **Priority:** 🔴 | **Exam Frequency:** 6/8 years
> **Sources:** Jain Ch.1 §1.5, Fahad Notes §01, Shishir Notes §01

## Why This Topic Matters

Taylor series expansion appears in 6 out of 8 years. The questions fall into three types: (1) expand and compute a value, (2) find how many terms are needed for a given accuracy, (3) compare two approaches to the same computation. This subtopic has the highest combined source KB (~30 KB) in all of NM-1. Master it completely.

> [!WARNING] Danger zone
> This subtopic is absent from Raidah's class notes. If you relied only on her notes, you would miss the most-tested NM-1 subtopic.

---

## 📝 Key Definitions

> **Taylor series:** "If $f(x)$ is continuous and possesses continuous derivatives of all orders in an interval containing $a$, then $f(x) = f(a) + (x-a)f'(a) + \frac{(x-a)^2}{2!}f''(a) + \cdots + \frac{(x-a)^n}{n!}f^{(n)}(a) + R_n$." — Jain, §1.5

> **Remainder (Lagrange form):** "$R_n = \frac{f^{(n+1)}(\xi)}{(n+1)!}(x-a)^{n+1}$ for some $\xi$ between $a$ and $x$." — Jain, §1.5

> **Truncation error:** The error from keeping only finitely many terms. It equals the remainder $R_n$, and it decreases as $n$ increases or as $|x - a|$ decreases.

---

## Core Theory: Taylor Series Expansion

### The Formula

The Taylor series of $f(x)$ about $x = a$ is:

$$
f(x) = \sum_{n=0}^{\infty} \frac{f^{(n)}(a)}{n!}(x - a)^n
$$

Written out:

$$
f(x) = f(a) + (x-a)f'(a) + \frac{(x-a)^2}{2!}f''(a) + \frac{(x-a)^3}{3!}f'''(a) + \cdots
$$

When expanded about $a = 0$, this is called the **Maclaurin series**.

### The Remainder (Truncation Error)

If the series is cut after $n$ terms, the truncation error is the Lagrange remainder:

$$
R_n = \frac{f^{(n+1)}(\xi)}{(n+1)!}(x - a)^{n+1}, \qquad \xi \in (a, x)
$$

To **bound** the error, replace $f^{(n+1)}(\xi)$ by its largest possible value on the interval. This gives a guaranteed upper bound on the error.

### Key Series to Know

| Function | Series about $x = 0$ | Radius |
| :-- | :-- | :--: |
| $e^x$ | $1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \cdots$ | $\infty$ |
| $\sin x$ | $x - \frac{x^3}{3!} + \frac{x^5}{5!} - \cdots$ | $\infty$ |
| $\cos x$ | $1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \cdots$ | $\infty$ |
| $\ln(1+x)$ | $x - \frac{x^2}{2} + \frac{x^3}{3} - \cdots$ | $|x| < 1$ |
| $\ln\frac{1+y}{1-y}$ | $2\left(y + \frac{y^3}{3} + \frac{y^5}{5} + \cdots\right)$ | $|y| < 1$ |

### The "Correct to $n$ Decimal Places" Rule

"Correct to $n$ decimal places" means the error must be below $\frac{1}{2} \times 10^{-n}$.

Not below $10^{-n}$. Getting this factor of two wrong doubles the number of terms needed.

---

## Worked Example: $e^x$ Taylor Expansion (PYQ 2024)

**Problem.** Derive the third-order Taylor series expansion of $f(x) = e^x$ around $x = 0$. Estimate the truncation error at $f(0.5)$.

> **Source:** 2024 Q.1(b) [Marks: 03]

**Step 1.** For $f(x) = e^x$, every derivative is $e^x$, so $f^{(n)}(0) = 1$ for all $n$.

$$
e^x = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \frac{x^4}{4!} + \cdots
$$

**Step 2.** Third-order truncation (keep terms up to $x^3$):

$$
\boxed{e^x \approx P_3(x) = 1 + x + \frac{x^2}{2} + \frac{x^3}{6}}
$$

**Step 3.** At $x = 0.5$:

$$
P_3(0.5) = 1 + 0.5 + \frac{0.25}{2} + \frac{0.125}{6} = 1 + 0.5 + 0.125 + 0.0208333 = 1.6458333
$$

**Step 4.** Truncation error by exact difference:

$$
e^{0.5} = 1.6487212707
$$

$$
|E_3| = |e^{0.5} - P_3(0.5)| = 1.6487212707 - 1.6458333333 = 0.0028879374
$$

**Step 5.** Truncation error by Lagrange remainder bound:

$$
R_3(x) = \frac{e^{\xi}}{4!}x^4, \qquad 0 < \xi < 0.5
$$

$$
|R_3| \le \frac{e^{0.5}}{24}(0.5)^4 = \frac{1.6487213}{24}(0.0625) = 0.0042935
$$

The exact error $0.0028879$ sits inside the bound $0.0042935$.

$$
\boxed{P_3(0.5) = 1.6458333, \qquad |E_3| = 0.0028879 \le 0.0042935}
$$

> [!WARNING] Common trap: which $x$ goes in the remainder
> The remainder carries $(x - x_0)^{n+1}$, evaluated at the approximation point $x = 0.5$, not at the expansion point. Equally common is bounding $e^\xi$ by $e^0 = 1$, which is the *smallest* value on the interval, not the largest.

---

## 🏆 Golden Questions (Past Exam Archive)

### 🎯 Evaluate $e^{-5}$ using two approaches and compare with true value $6.737947 \cdot 10^{-3}$.
> **Appeared:** 2017 Q.1(c) — (04 marks)

**Full Answer:**

**Approach A: the alternating series directly, with $x = 5$.**

| Terms $k$ | Sum $S_k = \sum_{n=0}^{k-1}\frac{(-5)^n}{n!}$ | Error $|S_k - 6.737947\times10^{-3}|$ |
| :--: | :-- | :-- |
| 1 | $1$ | $9.933\times10^{-1}$ |
| 2 | $-4$ | $4.007$ |
| 3 | $8.5$ | $8.493$ |
| 4 | $-12.3333$ | $1.234\times10^{1}$ |
| 5 | $13.7083$ | $1.370\times10^{1}$ |
| 8 | $-6.1329$ | $6.140$ |
| 10 | $-1.8271$ | $1.834$ |
| 12 | $-3.5921\times10^{-1}$ | $3.659\times10^{-1}$ |
| 14 | $-4.5555\times10^{-2}$ | $5.229\times10^{-2}$ |
| 15 | $2.4457\times10^{-2}$ | $1.772\times10^{-2}$ |

The partial sums grow to $13.7$ before they even begin to fall. The largest term is $\frac{5^5}{5!} = 26.0417$, about **3866 times** the final answer. This is **catastrophic cancellation**: the error is not reduced by computing more terms because the cancellation destroys more digits than the machine holds.

**Approach B: the reciprocal of the positive series, with $x = 5$.**

| Terms $k$ | Sum $T_k = \sum_{n=0}^{k-1}\frac{5^n}{n!}$ | $\frac{1}{T_k}$ | Error |
| :--: | :-- | :-- | :-- |
| 1 | $1$ | $1$ | $9.933\times10^{-1}$ |
| 2 | $6$ | $1.6667\times10^{-1}$ | $1.599\times10^{-1}$ |
| 3 | $18.5000$ | $5.4054\times10^{-2}$ | $4.732\times10^{-2}$ |
| 5 | $65.3750$ | $1.5296\times10^{-2}$ | $8.558\times10^{-3}$ |
| 8 | $128.6190$ | $7.7749\times10^{-3}$ | $1.037\times10^{-3}$ |
| 10 | $143.6895$ | $6.9595\times10^{-3}$ | $2.215\times10^{-4}$ |
| 12 | $147.6038$ | $6.7749\times10^{-3}$ | $3.694\times10^{-5}$ |
| 14 | $148.3096$ | $6.7427\times10^{-3}$ | $4.706\times10^{-6}$ |
| 15 | $148.3796$ | $6.7395\times10^{-3}$ | $1.525\times10^{-6}$ |

All terms are positive, so no cancellation occurs. The sum rises monotonically towards $e^5 = 148.4132$. The reciprocal approaches the true value from above.

**The comparison.**

| | Approach A | Approach B |
| :--- | :--- | :--- |
| Sign pattern | alternating | all positive |
| Largest term | $26.0417$ at $n = 5$ | $26.0417$ at $n = 5$ |
| Relative size of that term | $\approx 3866 \times$ the result | $\approx 3866 \times$ the result |
| Cancellation | catastrophic | none |
| Behaviour | diverges then converges, pathologically | monotone |
| Terms for 4 significant figures | 23 | 16 |

$$
\boxed{\text{Approach A is unusable at } x = 5; \text{ Approach B reaches } 6.7395\times10^{-3} \text{ in 15 terms}}
$$

**Practical rule:** For $x \gtrsim 1$, evaluate $e^{-x}$ as $1/e^x$, never as the alternating series.

---

### 🎯 Find the number of terms in the exponential series such that their sum gives $e^x$ correct to five decimal places for all $x$ in $[0, 1]$.
> **Appeared:** 2018 Q.1(c) — (04 marks)

**Full Answer:**

**The series and its remainder.** For $0 \le x \le 1$,

$$
e^x = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \cdots + \frac{x^n}{n!} + \cdots
$$

After $k$ terms the remainder is, by Taylor's theorem with Lagrange form,

$$
R_k = \frac{e^{\xi}x^k}{k!}, \qquad 0 < \xi < x
$$

Since $0 \le x \le 1$ and $e^{\xi} \le e$, the largest possible remainder is at $x = 1$:

$$
|R_k| \le \frac{e}{k!} = \frac{2.718282}{k!}
$$

"Correct to five decimal places" requires the error to be below $0.5 \times 10^{-5}$.

**Test $k$:**

| $k$ | Tail bound $\frac{1}{k!}\frac{k+1}{k}$ | Verdict |
| :--: | :-- | :-- |
| 8 | $\frac{1}{40320}\left(\frac{9}{8}\right) = 2.786 \times 10^{-5}$ | too large |
| 9 | $\frac{1}{362880}\left(\frac{10}{9}\right) = 3.062 \times 10^{-6}$ | below $5\times10^{-6}$ |

**Direct check at $x = 1$:**

$$
S_9 = 1 + 1 + \frac{1}{2!} + \frac{1}{3!} + \frac{1}{4!} + \frac{1}{5!} + \frac{1}{6!} + \frac{1}{7!} + \frac{1}{8!}
$$

$$
S_9 = 2 + 0.5 + 0.166667 + 0.041667 + 0.008333 + 0.001389 + 0.000198 + 0.0000248
$$

$$
S_9 = 2.71827877
$$

And $e = 2.71828183$, so the actual error is $|e - S_9| = 3.06 \times 10^{-6} < 0.5 \times 10^{-5}$.

With eight terms $S_8 = 2.71825397$, giving $|e - S_8| = 2.79 \times 10^{-5}$, which is too large.

$$
\boxed{9\ \text{terms}}
$$

---

### 🎯 Compute the value of $\ln 3$ correct to five decimal places using Taylor's series expansion.
> **Appeared:** 2021 Q.1(c) — (04 marks)

**Full Answer:**

**Step 1. Check convergence.** The familiar expansion $\ln(1+x) = x - \frac{x^2}{2} + \frac{x^3}{3} - \cdots$ converges only for $|x| < 1$. Here $3 = 1 + 2$, so $x = 2$ and **the series diverges**.

> [!WARNING] Check the radius before you start
> $x = 2$ and $|2| > 1$, so pick a different form. Finding this after twenty minutes of summation is the whole lesson.

**Step 2. Use the hyperbolic form.**

$$
\ln\frac{1+y}{1-y} = 2\left(y + \frac{y^3}{3} + \frac{y^5}{5} + \cdots\right), \qquad |y| < 1
$$

Set $\frac{1+y}{1-y} = 3$. Then $1 + y = 3 - 3y$, so $4y = 2$ and $y = \frac{1}{2}$, which satisfies $|y| < 1$.

**Step 3. Expand.**

$$
\ln 3 = 2\left[\frac{1}{2} + \frac{1}{8 \times 3} + \frac{1}{32 \times 5} + \frac{1}{128 \times 7} + \frac{1}{512 \times 9} + \frac{1}{2048 \times 11} + \frac{1}{8192 \times 13} + \cdots\right]
$$

**Step 4. Add terms until error is below $\frac{1}{2} \times 10^{-5}$.**

| Terms | Partial sum | Error |
| --: | --: | --: |
| 5 | 1.0984995040 | $1.13 \times 10^{-4}$ |
| 6 | 1.0985882824 | $2.40 \times 10^{-5}$ |
| 7 | 1.0986070624 | $5.23 \times 10^{-6}$ |
| 8 | 1.0986111314 | $1.16 \times 10^{-6}$ |

Seven terms give $5.23 \times 10^{-6}$, still above $5 \times 10^{-6}$. Eight terms give $1.16 \times 10^{-6}$, comfortably inside. **Eight terms are required.**

$$
\boxed{\ln 3 = 1.09861}
$$

---

### 🎯 Evaluate $f(1)$ using Taylor's series for $f(x) = x^3 - 3x^2 + 5x - 10$.
> **Appeared:** 2022 Q.1(b) — (04 marks)

**Full Answer:**

**Step 1.** Taylor's series about $x = 0$:

$$
f(x) = f(0) + x f'(0) + \frac{x^2}{2!}f''(0) + \frac{x^3}{3!}f'''(0) + \frac{x^4}{4!}f^{(4)}(0) + \cdots
$$

**Step 2.** Differentiate and evaluate at 0:

| | $f(x)$ | $f'(x)$ | $f''(x)$ | $f'''(x)$ | $f^{(4)}(x)$ |
| :-- | :-- | :-- | :-- | :-- | :-- |
| | $x^3-3x^2+5x-10$ | $3x^2-6x+5$ | $6x-6$ | $6$ | $0$ |

$$
f(0) = -10, \qquad f'(0) = 5, \qquad f''(0) = -6, \qquad f'''(0) = 6, \qquad f^{(4)} = 0
$$

**Step 3.** The series terminates (fourth derivative is identically zero):

$$
f(x) = -10 + 5x - 3x^2 + x^3
$$

**Step 4.** Put $x = 1$:

$$
f(1) = -10 + 5(1) - 3(1)^2 + (1)^3 = -10 + 5 - 3 + 1
$$

$$
\boxed{f(1) = -7}
$$

> [!NOTE] No error analysis needed
> A cubic has an exact third-order expansion. The remainder $R_3$ is identically zero, not merely small. The four marks are for the derivative table, written out explicitly.

---

## Exam Variants

| Year | Question | Key Answer |
| :--- | :--- | :--- |
| 2017 Q.1(c) | Evaluate $e^{-5}$ two ways, compare | $\boxed{\text{Approach A is unusable at } x = 5; \text{ Approach B reaches } 6.7395\times10^{-3} \text{ in 15 terms}}$ |
| 2018 Q.1(c) | Terms for $e^x$ correct to 5 d.p. on $[0,1]$ | $\boxed{9\ \text{terms}}$ |
| 2021 Q.1(c) | $\ln 3$ correct to 5 d.p. | $\boxed{\ln 3 = 1.09861}$ |
| 2022 Q.1(b) | $f(1)$ for $f(x) = x^3 - 3x^2 + 5x - 10$ | $\boxed{f(1) = -7}$ |
| 2024 Q.1(b) | Third-order Taylor of $e^x$, error at $x = 0.5$ | Worked Example above |

---

## ⚡ Exam Tips & Common Mistakes

1. **Check convergence radius before computing.** $\ln(1+x)$ diverges for $|x| \ge 1$. Use the hyperbolic form $\ln\frac{1+y}{1-y}$ with $y = \frac{a-1}{a+1}$ instead.
2. **"Correct to $n$ decimal places" means error $< \frac{1}{2} \times 10^{-n}$.** Not $10^{-n}$. Getting this wrong changes the answer.
3. **For polynomials, Taylor series terminates.** A degree-$k$ polynomial has $f^{(k+1)} \equiv 0$, so the expansion is exact. No error analysis needed.
4. **For $e^{-x}$ with large $x$: compute $1/e^x$.** The alternating series suffers catastrophic cancellation. The reciprocal of the positive series does not.
5. **Bound $f^{(n+1)}(\xi)$ by its LARGEST value on the interval.** Not the smallest. Using $e^0 = 1$ instead of $e^{0.5}$ gives a lower bound, not an upper bound.
6. **Write the derivative table.** For polynomial questions, examiners want $f'$, $f''$, $f'''$ written out explicitly.

## 🔗 Related Topics

- [NM-1.4: Error Types and Sources](NM-1.4_Error_Types_and_Sources.md) — truncation error is one of the three error types
- [NM-1.5: Error Representations](NM-1.5_Error_Representations_and_Propagation.md) — how to measure the error Taylor series produce
- [NM-4.7: Newton's Forward Difference](NM-4.7_Newtons_Forward_Difference.md) — Taylor-like expansions for discrete data

---

[← Previous: NM-1.5 Error Representations](NM-1.5_Error_Representations_and_Propagation.md) | [🏠 Index](00_Index.md) | [Next: NM-1 Lower Tier →](NM-1_Lower_Modeling_Accuracy_Precision.md)
