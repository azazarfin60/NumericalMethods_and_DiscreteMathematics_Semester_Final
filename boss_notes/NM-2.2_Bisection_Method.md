[← Previous: NM-2.1 Fundamentals](NM-2.1_Fundamentals_and_Classification.md) | [🏠 Index](00_Index.md) | [Next: NM-2.3 False Position →](NM-2.3_False_Position_and_Regula_Falsi.md)

---

# NM-2.2: Bisection Method
> **Section:** A (Numerical Methods) | **Priority:** 🔴 | **Exam Frequency:** 5/8 years
> **Sources:** Jain Ch.2 §2.2, Topicwise NM-2.2, Fahad Notes §02

## Why This Topic Matters

Bisection is the only root finder that cannot fail. That guarantee is why it is the fallback inside every production solver, and why three papers have asked you to write its algorithm. The exam gives you three question shapes: explain the method and write the algorithm, write the algorithm alone, or run two iterations on a given polynomial. All three need the same six steps.

---

## 📝 Key Definitions

> **Bisection method basis:** "if a function $f(x)$ is continuous between $a$ and $b$, and $f(a)$ and $f(b)$ are of opposite signs, then there exists at least one root between $a$ and $b$." — Jain, §2.2

> **Relative error (termination test):** "$\varepsilon_r = \left|\frac{x_r' - x_r}{x_r'}\right| \times 100\%$ where $x_r'$ is the new value of $x_r$." — Jain, §2.2

> **Bisection:** A bracketing method that repeatedly halves the interval $[a,b]$ and keeps the half that still contains a sign change, so the root is trapped in a shrinking interval.

---

## Core Theory

### The Idea

You have a continuous $f$ that changes sign on $[a, b]$. So a root sits somewhere inside. You do not know where, so you cut the interval in half and test which half still changes sign. Keep that half. Repeat.

The interval width after $n$ halvings is:

$$
\text{width}_n = \frac{b_0 - a_0}{2^n}
$$

And the midpoint you keep has error at most half the width:

$$
|x_n - r| \le \frac{b_0 - a_0}{2^{n+1}}
$$

This is the only place in NM-2 where you know the error bound **before you start**. That is the whole selling point.

### Geometric Picture

![Bisection method: interval halving between a and b with points x0, x1 and x2 marked on the x-axis](diagrams/nm2_bisection_method_geometric.jpg)

*Figure 2.1 (Jain, p. 24): each bisection replaces the bracketing interval by half of itself. The interval can only shrink, so the root cannot escape.*

### The Algorithm (2017 Q.3(c), 2018 Q.2(a))

1. Read $f(x)$, the tolerance $\varepsilon$, and a maximum iteration count $N$.
2. Accept the ends $a$ and $b$ of the bracketing interval.
3. Compute $f(a)$ and $f(b)$. If $f(a)f(b) > 0$, report that the interval does not bracket a root and stop.
4. Set the midpoint $c = \dfrac{a + b}{2}$ and compute $f(c)$.
5. Test for convergence. If $|f(c)| < \varepsilon$, or if $|b - a| < \varepsilon$, accept $c$ as the root and stop.
6. If $f(a)f(c) < 0$, set $b = c$. Otherwise set $a = c$.
7. If the iteration count exceeds $N$, report non-convergence and stop. Otherwise return to step 4.

### The Relative Accuracy Test (2017 Q.3(c) specifically)

2017 Q.3(c) asks for the algorithm **with a test for relative accuracy**. Step 5 then becomes:

$$
|e_a| = \left|\frac{c - c_{\text{old}}}{c}\right|\times 100\%
$$

Accept $c$ when $|e_a| < \varepsilon_r$, or when $|f(c)| < \varepsilon$. The old midpoint is stored at step 6.

Because the interval halves each step, $|e_a|$ roughly halves each step too. So when $|e_a|$ drops below the tolerance, the remaining uncertainty is at most the current interval width, and the reported number is a valid statement of how far the answer may be from the truth.

### How Many Iterations, Known in Advance

Rearrange the width formula for a target tolerance $\varepsilon$:

$$
n = \left\lceil \log_2\frac{b - a}{\varepsilon}\right\rceil
$$

Worked: on $[1, 2]$ with $\varepsilon = 0.001$, that is $n \ge \log_2(1000) \approx 9.97$, so ten iterations. Bisection is worth writing an algorithm for precisely because of this closed count. Newton is faster, but you cannot predict how long it will take.

### Merits and Demerits (2018 Q.2(a))

**Merits.** Convergence is guaranteed whenever the initial interval brackets a root and $f$ is continuous. Exactly one evaluation of $f$ per step. The error bound is computable in advance.

**Demerits.** Slow compared with Newton or regula falsi, because halving discards half the information each step. The iteration count is fixed by the tolerance, not by the shape of $f$. And a bracketing interval must be found first, which is impossible for an even-multiplicity root.

---

## Worked Example: $f(x) = x^3 - x - 2$ on $[1, 2]$

**Problem.** Bisect $f(x) = x^3 - x - 2$ on $[1, 2]$ and watch the bracket narrow.

**Step 1. Confirm the bracket.** $f(1) = 1 - 1 - 2 = -2 < 0$ and $f(2) = 8 - 2 - 2 = 4 > 0$. The sign changes, so a root is inside.

**Step 2. March.** Each row takes the midpoint of the row above and keeps the half where the sign flips.

| Iteration | $a$ | $b$ | $c = (a+b)/2$ | $f(c)$ | $b - a$ |
| :--: | :--: | :--: | :--: | :--: | :--: |
| 1 | 1 | 2 | 1.500000 | $-0.1250$ | 1 |
| 2 | 1.5 | 2 | 1.750000 | $1.6094$ | 0.5 |
| 3 | 1.5 | 1.75 | 1.625000 | $0.6660$ | 0.25 |
| 4 | 1.5 | 1.625 | 1.562500 | $0.2522$ | 0.125 |
| 5 | 1.5 | 1.5625 | 1.531250 | $0.0591$ | 0.0625 |
| 6 | 1.5 | 1.53125 | 1.515625 | $-0.0341$ | 0.03125 |

**Step 3. Read the result.** The true root is $x = 1.5214$. After six halvings the width is $0.03125$, so the half-width $0.015625$ bounds the error and the approximate relative error is under $1.1\%$.

$$
n = \left\lceil \log_2\frac{b - a}{\varepsilon}\right\rceil
$$

> [!WARNING]
> Look down the $a$ and $b$ columns. $a$ stays at $1$ until iteration 6, and $b$ walks down from $2$. That is forced by the function. $f$ is negative on $[1, 1.5214]$ and positive above it, so every midpoint above the root sends $b$ down, and every midpoint below it sends $a$ up. A table where both ends move in the same iteration has a sign error in step 6. It will still print plausible midpoints, because the midpoint is computed before either end is updated.

---

## Worked Example: $f(x) = x^3 - 6x^2 + 11x - 6$ on $[2.5, 3.4]$

**Problem.** Use the bisection method to find a root in the interval, up to two iterations.

> **Source:** 2024 Q.2(a) [Marks: 03, CO: 2]

**Step 1. Factor first, because it is the free check.**

$$
x^3 - 6x^2 + 11x - 6 = (x-1)(x-2)(x-3)
$$

The three roots are exactly $1$, $2$ and $3$. Any bisection run must converge to one of them. A run that converges anywhere else is wrong, and this is the check to apply before trusting any number.

**Step 2. Choose the interval.** The paper prints none, so state your choice. Take $[2.5, 3.4]$, which brackets $x = 3$ without landing on it.

$$
f(2.5) = 15.625 - 37.5 + 27.5 - 6 = -0.375, \qquad f(3.4) = 39.304 - 69.36 + 37.4 - 6 = +1.344
$$

$f(2.5) \cdot f(3.4) = -0.504 < 0$, so a root lies in $(2.5, 3.4)$.

> [!WARNING]
> Do not bisect on $[1, 2]$ or $[2, 3]$. The three roots are $1$, $2$ and $3$, so the intervals between consecutive roots look attractive. They are the worst possible choice: $f(1) = f(2) = f(3) = 0$, so both endpoints of $[1, 2]$ are already roots and there is no sign change to narrow. Pick an interval that contains one root strictly inside it, and whose endpoints are not roots.

**Step 3. Iteration 1.** Midpoint $x_1 = (2.5 + 3.4)/2 = 2.95$.

$$
f(2.95) = 25.6724 - 52.2150 + 32.45 - 6 = -0.092625
$$

$f(2.95) < 0$, same sign as $f(2.5)$, so the root is in $(2.95, 3.4)$.

**Step 4. Iteration 2.** Midpoint $x_2 = (2.95 + 3.4)/2 = 3.175$.

$$
f(3.175) = 32.005984 - 60.483750 + 34.925 - 6 = +0.447234
$$

$f(3.175) > 0$, so the root is in $(2.95, 3.175)$.

$$
\boxed{x_2 = 3.175, \qquad \text{root} \in (2.95,\ 3.175), \qquad \text{true root} = 3}
$$

**Step 5. Check the width.** Each iteration halves the width, so $\text{width}_n = \frac{b_0 - a_0}{2^n}$. Here $b_0 - a_0 = 3.4 - 2.5 = 0.9$, and after two iterations the bracket is $(2.95, 3.175)$, of width $0.225$. That matches $0.9/2^2 = 0.9/4 = 0.225$.

The maximum error bound for the midpoint after $n$ iterations is $|x_n - r| \le \frac{b_0 - a_0}{2^n}$. For $n = 2$:

$$
|x_2 - r| \le \frac{0.9}{2^2} = 0.225
$$

Since the true root is $r = 3$, the actual error is $|3.175 - 3| = 0.175$, which satisfies the theoretical bound:

$$
\text{guaranteed: root} \in (2.95, 3.175), \quad |3.175 - 3| = 0.175 \le 0.225
$$

> [!NOTE]
> The interval $[2.5, 3.5]$ also works, and is the one the paper's own margin note suggests. Its first midpoint is exactly $3.0$, and $f(3.0) = 0$, so the root is found in a single step and the second iteration is unnecessary. That is still a correct answer. A midpoint landing exactly on the root is a coincidence of this polynomial, not a general property.

> [!WARNING]
> The repeated-root trap. If the root sits exactly at an endpoint, the test $f(a)f(c) < 0$ selects the wrong half, because one factor is zero rather than negative. A correct algorithm checks $f(c) = 0$ separately before testing the sign. Without it, a root at an endpoint is lost.

---

## Exam Variants

| Year | Question | Data Given | Key Answer |
|:---|:---|:---|:---|
| 2024 Q.2(a) | Two iterations of bisection | $f(x) = x^3 - 6x^2 + 11x - 6$, interval not printed | $\boxed{x_2 = 3.175, \qquad \text{root} \in (2.95,\ 3.175), \qquad \text{true root} = 3}$ |
| 2017 Q.3(c) | Explain and write the algorithm with a relative accuracy test | none (06 marks, theory) | Algorithm plus $|e_a| = \left|\frac{c - c_{\text{old}}}{c}\right|\times 100\%$ |
| 2018 Q.2(a) | Develop an algorithm for the bisection method | none (04 marks, theory) | Algorithm plus $n = \left\lceil \log_2\frac{b - a}{\varepsilon}\right\rceil$ |

---

## 🏆 Golden Questions (Past Exam Archive)

### 🎯 Explain the bisection method for finding a real root of the equation $f(x) = 0$ and write an algorithm for its implementation with a test for relative accuracy.
> **Appeared:** 2017 Q.3(c) — (06 marks)

**Full Answer:**

**The method.** Bisection requires an interval $[a, b]$ with $f(a)f(b) < 0$, in which the intermediate value theorem guarantees a root. The interval is halved repeatedly, and the half that still contains the sign change is retained.

**Algorithm.**

1. Read $f(x)$, the relative tolerance $\varepsilon_r$, and the maximum iteration count $N$.
2. Accept the ends $a$ and $b$.
3. Compute $f(a)$ and $f(b)$. If $f(a)f(b) > 0$, report that the interval does not bracket a root and stop.
4. Set the midpoint $c = \dfrac{a + b}{2}$ and compute $f(c)$.
5. **Test for relative accuracy.** Compute
   $$
   |e_a| = \left|\frac{c - c_{\text{old}}}{c}\right|\times 100\%
   $$
   If $|e_a| < \varepsilon_r$, or if $|f(c)| < \varepsilon$, accept $c$ and stop.
6. If $f(a)f(c) < 0$, set $b = c$; otherwise set $a = c$. Store the previous midpoint as $c_{\text{old}}$.
7. If the iteration count exceeds $N$, report non-convergence and stop. Otherwise return to step 4.

**The relative accuracy test, in detail.** The approximate relative error after step $k$ is

$$
|e_a|_k = \left|\frac{c_k - c_{k-1}}{c_k}\right|\times100\%
$$

It measures the change between successive midpoints, not the distance from the current midpoint to the true root. Because the interval halves each time, $|e_a|$ roughly halves each time too, so it is a reliable monitor: when it falls below $\varepsilon_r$ the remaining uncertainty is at most the current interval width, and the computed relative error is a valid statement of how far the answer may be from the true root.

**Convergence.** After $n$ halvings the interval has width $\dfrac{b-a}{2^n}$, and the midpoint error is at most half that. The number of iterations needed for a target tolerance is therefore known in advance:

$$
n = \left\lceil \log_2\frac{b - a}{\varepsilon}\right\rceil
$$

**Merits and demerits.** Guaranteed convergence from a valid bracket, and one evaluation of $f$ per step. Slow compared with Newton or regula falsi. The count is fixed by the tolerance rather than by the shape of $f$. And a bracket must be found first.

---

### 🎯 Develop an algorithm to calculate the root of any non-linear equation by bisection method.
> **Appeared:** 2018 Q.2(a) — (04 marks)

**Full Answer:**

**Bisection** solves $f(x) = 0$ on an interval $[a, b]$ in which $f$ changes sign, by repeatedly halving the interval and retaining the half that still contains the sign change.

**Algorithm.**

1. Read $f(x)$, the tolerance $\varepsilon$, and the maximum iteration count $N$.
2. Accept the ends $a$ and $b$ of the bracketing interval.
3. Compute $f(a)$ and $f(b)$. If $f(a)f(b) > 0$, report that the interval does not bracket a root and stop.
4. Set $c = \dfrac{a + b}{2}$ and compute $f(c)$.
5. Test for convergence. If $|f(c)| < \varepsilon$, or if $|b - a| < \varepsilon$, accept $c$ as the root and stop.
6. If $f(a)f(c) < 0$, set $b = c$; otherwise set $a = c$.
7. If the iteration count exceeds $N$, report non-convergence and stop. Otherwise return to step 4.

**Convergence.** After $n$ bisections the interval has width $\dfrac{b-a}{2^n}$, and the error in the midpoint is at most $\dfrac{b-a}{2^{n+1}}$. Halving the interval therefore halves the error, and the number of iterations needed for error below $\varepsilon$ is

$$
n = \left\lceil \log_2\frac{b-a}{\varepsilon}\right\rceil
$$

**Merits and demerits.** The method is guaranteed to converge whenever the initial interval brackets a root and $f$ is continuous, and the error is known in advance. It requires only one evaluation of $f$ per step. Its drawbacks are that convergence is slow compared with Newton or regula falsi, that the number of iterations is fixed by the tolerance rather than by the shape of $f$, and that a bracketing interval must be found first.

> [!WARNING]
> Where bisection quietly fails. If $f$ has a root at which it touches zero without changing sign, such as $(x-2)^2$, then $f(a)f(b) > 0$ at the true bracket and step 3 rejects it. The method cannot find an even-multiplicity root at all, and no amount of iteration will help. This is not a bug in the algorithm; it is a property of sign-change bracketing.

---

### 🎯 Given the polynomial $f(x) = x^3 - 6x^2 + 11x - 6$, use the bisection (bracketing) method to find a root in the interval up to two iterations.
> **Appeared:** 2024 Q.2(a) — (03 marks, CO: 2)

The full solution is the second Worked Example above. The essential points for the exam answer:

$$
f(x) = x^3 - 6x^2 + 11x - 6 = (x-1)(x-2)(x-3)
$$

$$
f(2.5) = -0.375, \qquad f(3.4) = +1.344, \qquad f(2.5)f(3.4) = -0.504 < 0
$$

Iteration 1: $x_1 = 2.95$, $f(2.95) = -0.092625$, root in $(2.95, 3.4)$.

Iteration 2: $x_2 = 3.175$, $f(3.175) = +0.447234$, root in $(2.95, 3.175)$.

$$
\boxed{x_2 = 3.175, \qquad \text{root} \in (2.95,\ 3.175), \qquad \text{true root} = 3}
$$

The interval halves each time, so after $n$ iterations its width is $\dfrac{b_0 - a_0}{2^n}$, and the answer is known to lie inside it. This is the feature that makes bisection valuable despite being slow: the error is bounded at every step, whether or not the iteration has converged.

**Why bisection is chosen here.** The marks are for the method, not the algebra, so the factoring is the check rather than the answer. The question asks for the bracketing procedure, and the demonstration of it needs a valid bracket, which needs a sign change.

---

## ⚡ Exam Tips & Common Mistakes

1. **Write $f(a)f(b) < 0$ on its own line before iterating.** If the product is positive, stop and pick another interval. That single line is worth method marks.
2. **Store the old midpoint when using the relative error test.** 2017 Q.3(c) wants $c_{\text{old}}$ explicitly. A table with no previous midpoint cannot compute $|e_a|$ on row 2.
3. **Both ends never move in the same iteration.** One end changes, always. If your table moves both, step 6 has a sign error.
4. **If the paper gives no interval, factor the polynomial first.** In 2024 Q.2(a) factoring gives $1, 2, 3$ for free, and then a bracket around one of them is obvious.
5. **State the convergence criterion.** Write it, then apply it to your last two rows. A bare table scores less.
6. **Quote the closed iteration count.** $n = \left\lceil \log_2\frac{b-a}{\varepsilon}\right\rceil$ is the line that separates a good bisection answer from a mediocre one.

## 🔗 Related Topics

- [NM-2.1: Fundamentals & Classification](NM-2.1_Fundamentals_and_Classification.md) — where bisection sits in the bracketing family
- [NM-2.3: False Position & Regula Falsi](NM-2.3_False_Position_and_Regula_Falsi.md) — same bracket, better guess, and the stagnation problem
- [NM-2.6: Method Comparison & Convergence](NM-2.6_Method_Comparison_and_Convergence.md) — why the guaranteed rate is worth less than the order 2 of Newton
- [NM-2.4: Newton-Raphson Method](NM-2.4_Newton_Raphson_Method.md) — the open method that bisection rescues

---

[← Previous: NM-2.1 Fundamentals](NM-2.1_Fundamentals_and_Classification.md) | [🏠 Index](00_Index.md) | [Next: NM-2.3 False Position →](NM-2.3_False_Position_and_Regula_Falsi.md)
