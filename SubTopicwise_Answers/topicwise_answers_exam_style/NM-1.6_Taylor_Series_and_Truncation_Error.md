---
title: "NM-1.6 · Taylor Series & Truncation Error"
tags:
  - numerical-methods
  - discrete-mathematics
  - topicwise
---



[🏠 Subtopic Index](00_Index.md) | [← Prev: NM-1.5 Error Representations & Propagation](NM-1.5_Error_Representations_and_Propagation.md) | [Next: NM-2.1 Fundamentals & Classification →](NM-2.1_Fundamentals_and_Classification.md)

---

# NM-1.6 · Taylor Series & Truncation Error

Every block below is copied from `../answers_exam_style/`, which is the
only place an answer is authored. A number here is the same number, character
for character, as the one it came from.


### [2017 Q.1(c)]

**Question.** Evaluate $e^{-5}$ using following two approaches and compare with the true value of $6.737947 \cdot 10^{-3}$ as terms are added: $e^{-x} = 1 - x + \frac{x^2}{2!} - \frac{x^3}{3!} + \cdots \quad \text{and} \quad e^{-x} = \frac{1}{e^x} = \frac{1}{1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \cdots}$.

**Solution.**

**Approach A: the alternating series directly, with $x = 5$.**

| Terms $k$ | Sum $S_k = \sum_{n=0}^{k-1}\dfrac{(-5)^n}{n!}$ | Error $|S_k - 6.737947\times10^{-3}|$ |
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

The partial sums grow to $13.7$ before they even begin to fall. At $x = 5$ the
largest term is $\dfrac{5^5}{5!} = 26.0417$, which is **over three thousand
times** the final answer. Every partial sum is dominated by that term, and no
amount of further addition repairs it on a finite-precision machine: the
cancellation destroys more digits than the machine holds.

**Approach B: the reciprocal of the positive series, with $x = 5$.**

| Terms $k$ | Sum $T_k = \sum_{n=0}^{k-1}\dfrac{5^n}{n!}$ | $\dfrac{1}{T_k}$ | Error |
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

All terms are positive, so no cancellation occurs, and the sum rises
monotonically towards $e^5 = 148.4132$. The reciprocal approaches the true
value from above, reaching four significant figures at the sixteenth term.

**The comparison.**

| | Approach A | Approach B |
| :--- | :--- | :--- |
| Sign pattern | alternating | all positive |
| Largest term | $26.0417$ at $n = 5$ | $26.0417$ at $n = 5$ |
| Relative size of that term | $\approx 3866 \times$ the result | $\approx 3866 \times$ the result |
| Cancellation | catastrophic | none |
| Behaviour | diverges then converges, pathologically | monotone |
| Terms for 4 significant figures | 23 | 16 |

$$\boxed{\text{Approach A is unusable at } x = 5; \text{ Approach B reaches } 6.7395\times10^{-3} \text{ in 15 terms}}$$

> [!info] Check by the exact reciprocal and the general warning
> The true value is $e^{-5} = 1/e^5 = 1/148.4132 = 6.737947\times10^{-3}$, the
> figure printed in the question, so Approach B's reciprocal is the direct route
> and Approach A must in principle reach the same place. The reason it does not
> is that at $x = 5$ the condition for the alternating series to be numerically
> safe, that the result is not small compared with the largest term, fails by a
> factor of nearly four thousand. Approach A does eventually converge, but only
> at the twenty-third term, against Approach B's sixteenth, and it passes
> through a partial sum of $-6.1329$ and one of $+13.7083$ on the way. The
> practical rule is that $e^{-x}$ for $x \gtrsim 1$ should be evaluated as
> $1/e^x$, never as the alternating series, because the cancellation grows with
> $x$. The two routes are expected to agree mathematically and to disagree
> numerically, which is the point of the comparison.

---

### [2018 Q.1(c)]

**Question.** Find the number of terms in the exponential series such that their sum gives the value of $e^x$ correct to five decimal places for all values of $x$ in the range $0 \le x \le 1$.

**Solution.**

**The series and its remainder.** For $0 \le x \le 1$,

$$e^x = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \cdots + \frac{x^n}{n!} + \cdots$$

After $k$ terms the remainder is, by Taylor's theorem with Lagrange form,

$$R_k = \frac{e^{\xi}x^k}{k!}, \qquad 0 < \xi < x$$

Since $0 \le x \le 1$ and $e^{\xi} \le e$, the largest possible remainder is
attained at $x = 1$ and

$$|R_k| \le \frac{e}{k!} = \frac{2.718282}{k!}$$

"Correct to five decimal places" requires the error to be below
$0.5 \times 10^{-5}$.

**Test $k$.** Taking the successive values:

| $k$ | Tail bound $\dfrac{1}{k!}\dfrac{k+1}{k}$ | Verdict |
| :--: | :-- | :-- |
| 8 | $\dfrac{1}{40320}\left(\dfrac{9}{8}\right) = 2.786 \times 10^{-5}$ | too large |
| 9 | $\dfrac{1}{362880}\left(\dfrac{10}{9}\right) = 3.062 \times 10^{-6}$ | below $5\times10^{-6}$ |

Hence the remainder tail is bounded by
$R_9 \le 3.062 \times 10^{-6} < 0.5 \times 10^{-5}$, which certifies 9 terms.

**Direct check at the worst point $x = 1$.** Summing the first nine terms:

$$S_9 = 1 + 1 + \frac{1}{2!} + \frac{1}{3!} + \frac{1}{4!} + \frac{1}{5!} + \frac{1}{6!} + \frac{1}{7!} + \frac{1}{8!}$$

$$S_9 = 2 + 0.5 + 0.166667 + 0.041667 + 0.008333 + 0.001389 + 0.000198 + 0.0000248$$

$$S_9 = 2.71827877$$

and $e = 2.71828183$, so the actual error is

$$|e - S_9| = 3.06 \times 10^{-6} < 0.5 \times 10^{-5}$$

With eight terms $S_8 = 2.71825397$, giving $|e - S_8| = 2.79 \times 10^{-5}$,
which is too large. Nine terms are therefore sufficient, and eight are not.

$$\boxed{9\ \text{terms}}$$

> [!info] Check by the Lagrange bound and exact tail
> The error after nine terms is the tail $R_9 = \sum_{n=9}^{\infty}\dfrac{1}{n!}$.
> Since $\dfrac{1}{9!} = 2.7557\times10^{-6}$ and the tail is bounded by
> $\dfrac{1}{9!}\left(1 + \dfrac{1}{10} + \dfrac{1}{10\cdot11} + \cdots\right) < \dfrac{10}{9\cdot9!} = 3.062\times10^{-6}$,
> the exact error $3.06\times10^{-6}$ clears the tolerance $0.5\times10^{-5}$ cleanly.
> Note that the cruder Lagrange bound $\dfrac{e}{k!}$ gives $\dfrac{e}{9!} = 7.491\times10^{-6}$,
> which exceeds $5\times10^{-6}$ only because $e \approx 2.718$ is a loose bound for $e^\xi$ on $[0,1]$;
> the exact geometric tail certifies that nine terms clear the tolerance while eight do not.

---

### [2021 Q.1(c)]

**Question.** Compute the value of $\ln 3$ correct to five decimal places using Taylor's series expansion.

**Solution.**

**Step 1. Choose a series that converges.** The familiar expansion

$$
\ln(1+x) = x - \frac{x^2}{2} + \frac{x^3}{3} - \cdots
$$

converges only for $\lvert x \rvert < 1$. Here $3 = 1 + 2$, so $x = 2$ and **the
series diverges**. Substituting $x = 2$ and adding terms gives a number that drifts
away from $\ln 3$ forever.

**Step 2. Use the hyperbolic form instead.** Write

$$
\ln\frac{1+y}{1-y} = 2\left(y + \frac{y^3}{3} + \frac{y^5}{5} + \cdots\right),
\qquad \lvert y \rvert < 1
$$

Set $\frac{1+y}{1-y} = 3$. Then $1 + y = 3 - 3y$, so $4y = 2$ and

$$
y = \frac{3-1}{3+1} = \frac{1}{2}
$$

which satisfies $\lvert y\rvert < 1$.

**Step 3. Expand.**

$$
\ln 3 = 2\left[\frac{1}{2} + \frac{1}{8 \times 3} + \frac{1}{32 \times 5} + \frac{1}{128 \times 7} + \frac{1}{512 \times 9} + \frac{1}{2048 \times 11} + \frac{1}{8192 \times 13} + \cdots\right]
$$

**Step 4. Add terms until the error is below $\frac{1}{2} \times 10^{-5}$.**

| Terms | Partial sum | Error |
| --: | --: | --: |
| 5 | 1.0984995040 | $1.13 \times 10^{-4}$ |
| 6 | 1.0985882824 | $2.40 \times 10^{-5}$ |
| 7 | 1.0986070624 | $5.23 \times 10^{-6}$ |
| 8 | 1.0986111314 | $1.16 \times 10^{-6}$ |

Seven terms give an error of $5.23 \times 10^{-6}$, still above $\frac{1}{2}10^{-5}$.
Eight terms give $1.16 \times 10^{-6}$, comfortably inside, so **eight terms are
required**.

**Step 5. Round.**

$$
\boxed{\ln 3 = 1.09861}
$$

> [!info] Check by an independent route
> Split $\ln 3 = \ln 2 + \ln 1.5$ and use $y = \frac{1}{3}$ and $y = \frac{1}{5}$
> respectively. With twelve terms each, $\ln 2 = 0.6931471805$ and
> $\ln 1.5 = 0.4054651081$, and the sum is $1.0986122887$, whose first five
> decimals are **1.09861**. The same answer from a different decomposition.
>
> The closed-form check is that $\ln 3 = 1.0986122886681098$, and
> $\lvert 1.0986111314 - 1.0986122887 \rvert = 1.16 \times 10^{-6}$, matching the
> table.

> [!warning] The series diverges; the arithmetic does not fail
> With $x = 2$ the partial sums **increase** past $\ln 3$ and keep going, which is
> the sign of a divergent series. Two standard repairs:
>
> 1. Use the hyperbolic form above with $y = \frac{a-1}{a+1}$, which is always inside the radius once $a > 1$.
> 2. Split the argument so each piece has $\lvert x\rvert < 1$, as $\ln 3 = \ln 2 + \ln 1.5$.
>
> A third option is $\ln 3 = 2\,\text{artanh}\frac{1}{2}$ followed by repeated
> halving of the argument. The first two are enough for five decimals.

> [!note] Error estimate, and why the bound is not the same as the actual error
> The tail after $N$ terms is bounded by
> $$2\sum_{k=N}^{\infty}\frac{y^{2k+1}}{2k+1} < \frac{2y^{2N+1}}{(2N+1)(1-y^2)}, \qquad y = \frac{1}{2}$$
> | $N$ | Bound | Below $\frac{1}{2}10^{-5}$? |
> | --: | --: | :-: |
> | 7 | $\frac{2(0.5)^{15}}{15 \times 0.75} = 5.425 \times 10^{-6}$ | No |
> | 8 | $\frac{2(0.5)^{17}}{17 \times 0.75} = 1.197 \times 10^{-6}$ | Yes |
>
> Two different numbers appear for seven terms, and both are correct:
> the **bound** $5.425\times10^{-6}$ comes from the geometric estimate above, while
> the **actual** error is $1.0986122887 - 1.0986070624 = 5.226\times10^{-6}$, which
> the table lists. The true error is always the smaller of the two, because the
> bound replaces each remaining denominator $2k+1$ by the larger value $2N+1$.
> Both exceed $5\times10^{-6}$, so seven terms fail on either count, and eight
> terms pass on both.

---

### [2022 Q.1(b)]

**Question.** Evaluate $f(1)$ using Taylor's series for $f(x)$, where $f(x) = x^3 - 3x^2 + 5x - 10$.

**Solution.**

**Step 1. Taylor's series about $x = 0$.**

$$
f(x) = f(0) + x f'(0) + \frac{x^2}{2!}f''(0) + \frac{x^3}{3!}f'''(0) + \frac{x^4}{4!}f^{(4)}(0) + \cdots
$$

**Step 2. Differentiate and evaluate at 0.**

| | $f(x)$ | $f'(x)$ | $f''(x)$ | $f'''(x)$ | $f^{(4)}(x)$ |
| :-- | :-- | :-- | :-- | :-- | :-- |
| | $x^3-3x^2+5x-10$ | $3x^2-6x+5$ | $6x-6$ | $6$ | $0$ |

$$
f(0) = -10, \qquad f'(0) = 5, \qquad f''(0) = -6, \qquad f'''(0) = 6, \qquad f^{(4)} = 0
$$

**Step 3. The series terminates.** Since the fourth derivative is identically zero,
the expansion is a polynomial with no terms beyond $x^3$:

$$
f(x) = -10 + 5x - 3x^2 + x^3
$$

**Step 4. Put $x = 1$.**

$$
f(1) = -10 + 5(1) - 3(1)^2 + (1)^3 = -10 + 5 - 3 + 1
$$

$$
\boxed{f(1) = -7}
$$

> [!info] Check by independent routes
> **Direct substitution.** $1 - 3 + 5 - 10 = -7$.
> **Structural check.** Because $f^{(4)} \equiv 0$, the third-order Taylor
> polynomial is **exact**, so there is no truncation error at all. The remainder
> $R_3$ is identically zero, not merely small. Route 3: factor-free Horner
> evaluation, $(-10 + 5\cdot1)\cdot1 - 3$ then $\cdot 1 + 1 = -7$.

> [!note] Why no error analysis is needed, and what the marks cover
> A cubic has an exact third-order expansion, so no error analysis is needed. The
> series must be built from derivatives rather than guessed at in order. The
> mark allocation of 4 corresponds to writing out $f'$, $f''$, $f'''$
> explicitly, which is exactly what is done above.

---

### [2024 Q.1(b)]

**Question.** Given the function $f(x) = e^x$, derive the third order Taylor series expansion around $x = 0$. Estimate the truncation error if you use this expansion to approximate $f(0.5)$.

**Solution.**

The Taylor series of $f$ about $x_0 = 0$ is

$$
f(x) = \sum_{n=0}^{\infty}\frac{f^{(n)}(0)}{n!}x^n
$$

For $f(x) = e^x$ every derivative is $e^x$, so $f^{(n)}(0) = 1$ for all $n$. Hence

$$
e^x = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \frac{x^4}{4!} + \cdots
$$

**Third order truncation**, keeping terms up to $x^3$:

$$
\boxed{e^x \approx P_3(x) = 1 + x + \frac{x^2}{2} + \frac{x^3}{6}}
$$

**At $x = 0.5$**

$$
P_3(0.5) = 1 + 0.5 + \frac{0.25}{2} + \frac{0.125}{6}
= 1 + 0.5 + 0.125 + 0.0208333
= 1.6458333
$$

**Truncation error, route 1, exact difference against the true value**

$$
e^{0.5} = 1.6487212707
$$

$$
|E_3| = |e^{0.5} - P_3(0.5)| = 1.6487212707 - 1.6458333333 = 0.0028879374
$$

**Truncation error, route 2, Lagrange remainder bound**

The remainder after three terms is

$$
R_3(x) = \frac{f^{(4)}(\xi)}{4!}x^4 = \frac{e^{\xi}}{24}x^4, \qquad 0 < \xi < x
$$

Substituting $x = 0.5$ and $e^{\xi} \le e^{0.5} = 1.6487213$ gives

$$
|R_3| \le \frac{1.6487213}{24}(0.5)^4 = \frac{1.6487213}{24}(0.0625) = 0.0042935
$$

The two routes are consistent: the exact error $0.0028879$ sits inside the bound
$0.0042935$. The first neglected term alone indicates the size of the error,
since the series terms fall fast at $x = 0.5$:

$$
\frac{x^4}{4!} = \frac{0.0625}{24} = 0.0026042
$$

$$
\boxed{P_3(0.5) = 1.6458333, \qquad |E_3| = 0.0028879 \le 0.0042935}
$$

---

[🏠 Subtopic Index](00_Index.md) | [← Prev: NM-1.5 Error Representations & Propagation](NM-1.5_Error_Representations_and_Propagation.md) | [Next: NM-2.1 Fundamentals & Classification →](NM-2.1_Fundamentals_and_Classification.md)
