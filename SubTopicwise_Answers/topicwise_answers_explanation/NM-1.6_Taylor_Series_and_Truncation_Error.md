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

Every block below is copied from `../answers_explanation/`. The reasoning
is written once, in the year-wise file, and is not restated here.


### [2017 Q.1(c)]

**Question.** Evaluate $e^{-5}$ using following two approaches and compare with the true value of $6.737947 \cdot 10^{-3}$ as terms are added: $e^{-x} = 1 - x + \frac{x^2}{2!} - \frac{x^3}{3!} + \cdots \quad \text{and} \quad e^{-x} = \frac{1}{e^x} = \frac{1}{1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \cdots}$.

*[Marks: 04]*

**Solution.**

**This question is about catastrophic cancellation, and the two approaches are
mathematically identical.** Both compute $e^{-5}$. They differ only in
arithmetic, and at $x = 5$ that difference is fatal.

**Approach A: the alternating series directly, with $x = 5$.**

$$S_k = \sum_{n=0}^{k-1}\frac{(-5)^n}{n!}$$

| Terms $k$ | $S_k$ | Error $\lvert S_k - 6.737947\times10^{-3}\rvert$ |
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

**What is happening.** The partial sums grow to $13.7$ before they begin to
fall. The largest term is $\dfrac{5^5}{5!} = 26.0417$, and the answer is
$0.0067379$, so that one term is about $3866$ times the result.

**Why that destroys the computation.** Each partial sum is formed by adding
alternating terms of size up to $26$ to get a number of size $0.0067$. To hold
a final answer of size $10^{-3}$ to, say, four significant figures, the machine
must retain four digits past the point where cancellation has eaten the
leading digits. If the partial sums are carried to $d$ significant figures and
the largest term is $3866$ times the answer, then all but about
$\log_{10}(3866) \approx 3.6$ of those digits are consumed by cancellation.
The remaining answer is good to roughly $d - 4$ digits, and no amount of
further addition repairs it: each new term is again of size comparable to the
running total. This is **catastrophic cancellation**, and the defining feature
is that the error is *not* reduced by computing more terms.

**Approach B: the reciprocal of the positive series, with $x = 5$.**

$$T_k = \sum_{n=0}^{k-1}\frac{5^n}{n!}, \qquad e^{-5} \approx \frac{1}{T_k}$$

| Terms $k$ | $T_k$ | $\dfrac{1}{T_k}$ | Error |
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

**What is happening.** Every term is positive, so there is **no cancellation at
all**. The sum rises monotonically towards $e^5 = 148.4132$, and its magnitude
never differs wildly from itself, so the machine's digits all survive. The
reciprocal then approaches the true value from above.

$$\boxed{\text{Approach A is unusable at } x = 5; \text{ Approach B reaches } 6.7395\times10^{-3} \text{ in 15 terms}}$$

**The comparison.**

| | Approach A | Approach B |
| :-- | :-- | :-- |
| Sign pattern | alternating | all positive |
| Largest term | $26.0417$ at $n = 5$ | $26.0417$ at $n = 5$ |
| That term relative to the result | $\approx 3866 \times$ | $\approx 3866 \times$ |
| Cancellation | catastrophic | none |
| Behaviour | diverges then converges, pathologically | monotone |
| Terms for 4 significant figures | 23 | 16 |

Note the fourth row of the table. Both approaches have the *same* largest term
relative to the answer. That is exactly why the problem is interesting: the
data are identical and the only thing that differs is the arrangement of the
summation, and that arrangement alone decides whether the machine survives.

> [!info] What the two routes confirm
> The true value is $e^{-5} = 1/e^5 = 1/148.4132 = 6.737947\times10^{-3}$, the
> figure printed in the question, so Approach B's reciprocal *is* the direct
> route and Approach A must in principle reach the same place. It does, eventually:
> at the twenty-third term the alternating series gets within $3.8\times10^{-7}$,
> which is four significant figures. So Approach A is not *wrong*, it is
> unusable in practice, and the difference between "wrong" and "unusable" is
> worth holding on to.
>
> The practical rule follows: for $x \gtrsim 1$, evaluate $e^{-x}$ as $1/e^x$,
> never as the alternating series, because the cancellation factor is roughly
> $e^x/x!$ and grows without bound as $x$ grows. The same trap appears in
> $\cos x = 1 - x^2/2 + x^4/24 - \cdots$ for large $x$, and in any alternating
> series whose terms peak far above the answer.

> [!warning] The test that catches a fabricated partial-sum column
> Two identities must hold in any such table, and both are one line. The
> *printed sum* must satisfy $1/T_k = $ the *printed reciprocal*, and
> $T_k - T_{k-1} = 5^{k-1}/k!$ must hold between consecutive rows. An earlier
> draft of the answer script carried a column of partial sums that satisfied
> neither, while its reciprocal and error columns were correct for the true
> sums. A table can therefore look entirely reasonable and still be wrong, and
> the only defence is to check one row against the sum rule above.

---

### [2018 Q.1(c)]

**Question.** Find the number of terms in the exponential series such that their sum gives the value of $e^x$ correct to five decimal places for all values of $x$ in the range $0 \le x \le 1$.

*[Marks: 04]*

**Solution.**

**The phrase that decides the answer is "for all values of $x$".** You are not
being asked for a term count that works at one particular $x$. You are being
asked for one that works *everywhere* on $[0, 1]$. So the first job is to find
the worst point on that interval and work there.

**The series and its remainder.**

$$e^x = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \cdots + \frac{x^n}{n!} + \cdots$$

After $k$ terms the remainder is, by Taylor's theorem in Lagrange form,

$$R_k = \frac{e^{\xi}x^k}{k!}, \qquad 0 < \xi < x$$

Now bound each factor. On $[0,1]$ we have $x^k \le 1$, and since $\xi < x \le 1$
we have $e^{\xi} \le e$. So

$$|R_k| \le \frac{e}{k!} = \frac{2.718282}{k!}$$

**Where is the worst case?** The bound $\dfrac{e}{k!}$ is attained at $x = 1$,
and at $x=1$ the error really is its largest, since every term $x^n$ grows with
$x$ on $[0,1]$. So $x = 1$ is the point to test and no other point can be worse.

**"Correct to five decimal places" means an error below $0.5 \times 10^{-5}$.**
Not below $10^{-5}$. Getting this factor of two wrong doubles your term count
and is the single most common error in this question.

**Test $k$.**

| $k$ | Tail bound $\dfrac{1}{k!}\dfrac{k+1}{k}$ | Verdict |
| :--: | :-- | :-- |
| 8 | $\dfrac{1}{40320}\left(\dfrac{9}{8}\right) = 2.786 \times 10^{-5}$ | too large |
| 9 | $\dfrac{1}{362880}\left(\dfrac{10}{9}\right) = 3.062 \times 10^{-6}$ | below $5\times10^{-6}$ |

Hence the remainder tail is bounded by
$R_9 \le 3.062 \times 10^{-6} < 0.5 \times 10^{-5}$, which certifies nine terms.

**Direct check at the worst point.** Summing the first nine terms,

$$S_9 = 2 + 0.5 + 0.166667 + 0.041667 + 0.008333 + 0.001389 + 0.000198 + 0.0000248 = 2.71827877$$

against $e = 2.71828183$, so the actual error is $3.06 \times 10^{-6}$, about
half the bound. With eight terms $S_8 = 2.71825397$ and $|e - S_8| =
2.79 \times 10^{-5}$, far too large.

$$\boxed{9\ \text{terms}}$$

> [!info] Why the geometric tail resolves the bound
> The error after nine terms is the tail $R_9 = \sum_{n=9}^{\infty}\dfrac{1}{n!}$.
> Since $\dfrac{1}{9!} = 2.7557\times10^{-6}$ and the tail is bounded by
> $\dfrac{1}{9!}\left(1 + \dfrac{1}{10} + \dfrac{1}{10\cdot11} + \cdots\right) < \dfrac{10}{9\cdot9!} = 3.062\times10^{-6}$,
> the true error $3.06\times10^{-6}$ sits well below the tolerance $5\times10^{-6}$.
> Note that the cruder Lagrange bound $\dfrac{e}{k!}$ gives $\dfrac{e}{9!} = 7.491\times10^{-6}$,
> which exceeds $5\times10^{-6}$ only because $e \approx 2.718$ is a conservative bound for $e^\xi$ on $[0,1]$;
> the exact geometric tail certifies that nine terms clear the tolerance while eight do not.

---

### [2021 Q.1(c)]

**Question.** Compute the value of $\ln 3$ correct to five decimal places using Taylor's series expansion.

*[Marks: 04, CO: 2]*

**Solution.**

**Step 1. Choose a series that converges.** The familiar expansion

$$
\ln(1+x) = x - \frac{x^2}{2} + \frac{x^3}{3} - \cdots
$$

converges only for $\lvert x \rvert < 1$. Here $3 = 1 + 2$, so $x = 2$ and **the
series diverges**.

> [!warning] The arithmetic does not fail, the series does
> Substituting $x = 2$ and adding terms gives a number that drifts away from
> $\ln 3$ forever, and the partial sums *increase* past it. Nothing in the
> computation looks wrong: each term is a finite number and the running total
> updates cleanly. Only the convergence test catches it.
>
> **Check the radius before you start, not after.** The habit is one line:
> $x = 2$, and $|2| > 1$, so pick a different form. Finding this after twenty
> minutes of summation is the whole lesson of the question.

**Step 2. Use the hyperbolic form instead.** Write

$$
\ln\frac{1+y}{1-y} = 2\left(y + \frac{y^3}{3} + \frac{y^5}{5} + \cdots\right),
\qquad \lvert y\rvert < 1
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

Seven terms give an error of $5.23 \times 10^{-6}$, still above
$\frac{1}{2}10^{-5}$. Eight terms give $1.16 \times 10^{-6}$, comfortably inside, so
**eight terms are required**.

**Step 5. Round.**

$$\boxed{\ln 3 = 1.09861}$$

> [!info] Check by an independent route
> Split $\ln 3 = \ln 2 + \ln 1.5$ and use $y = \frac{1}{3}$ and $y = \frac{1}{5}$
> respectively. With twelve terms each, $\ln 2 = 0.6931471805$ and
> $\ln 1.5 = 0.4054651081$, and the sum is $1.0986122887$, whose first five
> decimals are **1.09861**. The same answer from a different decomposition.
>
> The closed-form check is that $\ln 3 = 1.0986122886681098$, and
> $\lvert 1.0986111314 - 1.0986122887 \rvert = 1.16 \times 10^{-6}$, matching the
> table.

> [!warning] Two ways to repair a divergent log series
> 1. **Use the hyperbolic form** above with $y = \frac{a-1}{a+1}$, which is always inside the radius once $a > 1$. This is the clean route and it is what the answer uses.
> 2. **Split the argument** so each piece has $\lvert x\rvert < 1$, as $\ln 3 = \ln 2 + \ln 1.5$. More work, but it works with the familiar series.
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
> Two different numbers appear for seven terms, and both are correct: the
> **bound** $5.425 \times 10^{-6}$ comes from the geometric estimate above, while
> the **actual** error is $1.0986122887 - 1.0986070624 = 5.226 \times 10^{-6}$,
> which the table lists. The true error is always the smaller of the two, because
> the bound replaces each remaining denominator $2k+1$ by the larger value $2N+1$.
> Both exceed $5 \times 10^{-6}$, so seven terms fail on either count and eight
> terms pass on both.

---

### [2022 Q.1(b)]

**Question.** Evaluate $f(1)$ using Taylor's series for $f(x)$, where $f(x) = x^3 - 3x^2 + 5x - 10$.

*[Marks: 04, CO: 1]*

**Solution.**

**Step 1. Write the series about $x = 0$.**

$$
f(x) = f(0) + x f'(0) + \frac{x^2}{2!}f''(0) + \frac{x^3}{3!}f'''(0) + \frac{x^4}{4!}f^{(4)}(0) + \cdots
$$

**Step 2. Differentiate and evaluate at zero.** All four rows are needed, because
a cubic is exactly the case where the fourth derivative decides whether the
series terminates.

| | $f(x)$ | $f'(x)$ | $f''(x)$ | $f'''(x)$ | $f^{(4)}(x)$ |
| :-- | :-- | :-- | :-- | :-- | :-- |
| | $x^3-3x^2+5x-10$ | $3x^2-6x+5$ | $6x-6$ | $6$ | $0$ |

$$
f(0) = -10, \qquad f'(0) = 5, \qquad f''(0) = -6, \qquad f'''(0) = 6, \qquad f^{(4)} = 0
$$

**Step 3. The series terminates.** The fourth derivative is identically zero, so
there is nothing after the cubic term:

$$
f(x) = -10 + 5x + \frac{-6}{2}x^2 + \frac{6}{6}x^3 = -10 + 5x - 3x^2 + x^3
$$

**Step 4. Put $x = 1$.**

$$
f(1) = -10 + 5(1) - 3(1)^2 + (1)^3 = -10 + 5 - 3 + 1
$$

$$\boxed{f(1) = -7}$$

> [!info] Three independent routes, all landing on $-7$
> **Direct substitution.** $1 - 3 + 5 - 10 = -7$.
>
> **Horner, with no powers written out.** $(-10 + 5 \cdot 1) \cdot 1 - 3 = -8$, then
> $-8 \cdot 1 + 1 = -7$.
>
> **The truncation error is exactly zero.** Because $f^{(4)} \equiv 0$, the
> remainder $R_3$ is identically zero, not merely small. There is no error term
> to bound here, which is the distinguishing feature of a cubic.

> [!note] Why this question has no error analysis
> Taylor's method earns its keep when the series is infinite. For a polynomial of
> degree $k$, the $k$-th order expansion is the polynomial itself, and the
> $(k+1)$-th derivative being zero is what makes the answer exact rather than
> approximate.
>
> So no remainder term is needed here, and writing one anyway would be padding.
> The four marks are for the derivative table: $f'$, $f''$, $f'''$ written out
> explicitly, then the substitution. That is the whole question.

---

### [2024 Q.1(b)]

**Question.** Given the function $f(x) = e^x$, derive the third order Taylor series expansion around $x = 0$. Estimate the truncation error if you use this expansion to approximate $f(0.5)$.

*[Marks: 03, CO: 1]*

**Solution.**

**The setup.** The Taylor series of $f$ about $x_0$ is

$$f(x) = \sum_{n=0}^{\infty}\frac{f^{(n)}(x_0)}{n!}(x - x_0)^n$$

For $f(x) = e^x$ about $x_0 = 0$, every derivative is $e^x$, and evaluated at
zero every derivative is $1$. This is why $e^x$ is the standard worked example:
the derivative never changes, so the series is simply

$$e^x = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \frac{x^4}{4!} + \cdots$$

**Third order means keeping terms up to $n = 3$.**

$$\boxed{e^x \approx P_3(x) = 1 + x + \frac{x^2}{2} + \frac{x^3}{6}}$$

At $x = 0.5$:

$$P_3(0.5) = 1 + 0.5 + \frac{0.25}{2} + \frac{0.125}{6} = 1 + 0.5 + 0.125 + 0.0208333 = 1.6458333$$

**The truncation error.** Taylor's theorem gives the exact remainder

$$R_n = \frac{f^{(n+1)}(\xi)}{(n+1)!}(x - x_0)^{n+1}$$

for some $\xi$ between $x_0$ and $x$. Here $n = 3$, so

$$R_3 = \frac{e^{\xi}}{4!}(0.5)^4 = \frac{e^{\xi}}{24}(0.0625) = e^{\xi} \times 0.0026042$$

To **bound** this, take the largest $e^\xi$ can be on the interval, which is at
$\xi = 0.5$:

$$|R_3| \le \frac{e^{0.5}}{24}(0.5)^4 = \frac{1.6487213}{24}(0.0625) = 0.0042935$$

$$\boxed{P_3(0.5) = 1.6458333, \qquad |E_3| = 0.0028879 \le 0.0042935}$$

**Why the bound and the actual differ.** The bound $0.0042935$ uses $e^\xi$ at
its worst, $\xi = 0.5$. The *actual* error is

$$|e^{0.5} - P_3(0.5)| = 1.6487213 - 1.6458333 = 0.0028879$$

which is about two thirds of the bound. The first neglected term alone is

$$\frac{(0.5)^4}{4!} = \frac{0.0625}{24} = 0.0026042$$

which is already $90\%$ of the actual error. This is the useful practical fact
about alternating-free Taylor series: **the first neglected term tells you the
size of the error**. For $e^x$ with positive $x$ the terms are all positive, so
the first neglected term is a lower bound on the error rather than an estimate
of it, and the ratio of consecutive terms tells you how many more terms you
would need.

> [!warning] The trap: which $x$ goes in the remainder
> The remainder carries $(x - x_0)^{n+1}$, evaluated at the point where you are
> approximating, that is $x = 0.5$, not at the expansion point. Writing
> $(0.5 - 0)^4$ and writing $(0.5)^4$ are the same thing, but writing
> $(0.5 - x_0)$ where $x_0 = 0$ and then forgetting the minus is the classic
> slip. Equally common is bounding $e^\xi$ by $e^0 = 1$, which is the *smallest*
> value on the interval, not the largest.

---

[🏠 Subtopic Index](00_Index.md) | [← Prev: NM-1.5 Error Representations & Propagation](NM-1.5_Error_Representations_and_Propagation.md) | [Next: NM-2.1 Fundamentals & Classification →](NM-2.1_Fundamentals_and_Classification.md)
