[← Previous: NM-2.4 Newton-Raphson](NM-2.4_Newton_Raphson_Method.md) | [🏠 Index](00_Index.md) | [Next: NM-2 Lower Tier →](NM-2_Lower_Secant_and_Polynomial_Roots.md)

---

# NM-2.6: Method Comparison and Convergence
> **Section:** A (Numerical Methods) | **Priority:** 🔴 | **Exam Frequency:** 3/8 years + CT-01
> **Sources:** Jain Ch.2 §2.2, §2.3, §2.5, §2.7, Topicwise NM-2.6

## Why This Topic Matters

One paper asked for the full four-method comparison and gave it six marks. The class test asked which method belongs in a safety-critical system. Once you have written the table once, the answer is a copy. This file is that table, plus the reasoning that makes it memorable instead of memorised.

---

## 📝 Key Definitions

> **Root of an equation:** A value $x^*$ such that $f(x^*) = 0$. The graph of $f$ crosses or touches the $x$-axis at $x^*$.

> **Simple root:** A root with $f'(x^*) \ne 0$. The graph crosses the axis.

> **Multiple (repeated) root:** A root with $f'(x^*) = 0$. The graph touches the axis.

> **Explicit root:** A root writable in closed form, for example $\sqrt{2}$.

> **Implicit root:** A root that can only be found numerically, for example the root of $x^5 - x - 1 = 0$.

> **Order of convergence $p$:** If the errors satisfy $\varepsilon_{n+1} \approx C \varepsilon_n^p$, then $p$ is the order. $p = 1$ is linear, $p = 2$ is quadratic, $p \approx 1.618$ is superlinear.

---

## Core Theory

### The Ladder From Safe to Fast

The four methods are not four unrelated recipes. They are four rungs on a ladder, and each rung spends a different resource.

- **Bisection** uses the bracket only. It throws away the function values entirely. In exchange, it can never fail.
- **False position** uses the same bracket but reads the function values. It usually beats bisection, and it can stall.
- **Secant** drops the bracket entirely and fits a line through the last two points. Order $1.618$.
- **Newton** drops the history except one point and uses the slope. Order $2$, but it needs $f'$.

Move up the ladder and you gain speed. You lose the guarantee.

### The Comparison Table (2020 Q.2(a), 06 marks)

Memorise the rows, not the prose. This table is the answer.

| | Bisection | False position | Secant | Newton-Raphson |
| :-- | :-- | :-- | :-- | :-- |
| Type | Bracketing | Bracketing | Open | Open |
| Needs $f'$ | No | No | No | **Yes** |
| Needs a sign change | **Yes** | **Yes** | No | No |
| Information used | Endpoints only | Endpoints, keeps one fixed | Last **two** points | Value **and** slope at one point |
| New point from | Midpoint | Chord crossing | Chord through last two | Tangent at last point |
| Convergence order | 1 (linear) | 1, often faster | 1.618 (golden ratio) | **2 (quadratic)** |
| Starts from | $a_0$ | $a_0$ | $x_0, x_1$ | $x_0$ only |
| Guaranteed | **Yes**, from any valid bracket | **Yes** | No | No |
| Function calls per step | 1 | 1 | 1 | 2 (value and derivative) |
| Weakness | Slow, and halves the interval | Stalls on one side for strong convexity | Can diverge, can lose the bracket | Sensitive to the start |

$$
\boxed{\text{Bracketing methods are safe and slow; open methods are fast and unguaranteed}}
$$

### Reading the Order Column

**Bisection is order 1,** and the constant is exactly $\frac{1}{2}$. The error halves every step with no exceptions. That regularity is the real product, not the speed.

**False position is order 1 with an unknown constant.** Usually the constant is much smaller than $\frac{1}{2}$. But on a strongly convex function it approaches $1$, and the method crawls. You cannot know in advance which case you are in.

**Secant is order $1.618$.** That is the golden ratio, $\frac{1+\sqrt5}{2}$, and it is not a curiosity. The secant replaces the derivative with a finite difference, and the error in that difference costs you the gap between $1.618$ and $2$. It needs no derivative and it is still genuinely superlinear.

**Newton is order 2.** The error squares each step. This is the whole reason it exists.

### Cost, Not Just Order

Order alone is a misleading metric. Newton makes two function evaluations per step, one for $f$ and one for $f'$. Secant makes one. So per function evaluation, the secant can be competitive with Newton when $f'$ is expensive or unavailable.

But in a production code the guarantee is usually worth more than the order. Bisection makes one evaluation per step, and the error after $n$ steps is known before you write the first line of code.

### The Practical Rule

Keep a bracket. Try Newton. If a step leaves the bracket, take a bisection step instead.

That hybrid keeps Newton's speed and bisection's guarantee, and it is what real root finders do. The 2020 Q.2(b) table on $3I^2 - 4I - 4 = 0$ shows what happens without it: the start $I_0 = 1$ throws the first iterate to $3.5$, while the start $I_0 = 3$ reaches $2.000082$ in the same three steps.

---

## Worked Example: Ranking the Methods by Iterations

**Problem.** On $x^{2.2} = 69$ with the root in $(5, 8)$, compare how many iterations each method needs for four decimal places.

**Step 1. The closed form.** $x^{2.2} = 69$ with $2.2 = \frac{11}{5}$ gives $x = 69^{5/11} = 6.8523651204$. This is the target.

**Step 2. Regula falsi.** Seven iterations reach $6.852365$, matching the closed form to six figures.

**Step 3. Secant.** From the same two points, the secant gives $6.65599006$, $6.83400179$, $6.85268624$, $6.85236460$, $6.85236512$. Five iterations, and the endpoint $8$ is not retained.

**Step 4. Bisection.** After 18 iterations the bracket is $(6.85236359, 6.85237503)$ and the midpoint $6.85236931$ is within $4.2 \times 10^{-6}$ of the exact root.

**Step 5. Conclusion.** Secant is the fastest here, and regula falsi is the slowest of the three despite the bracket, because of one-sided stagnation. Bisection is the slowest overall but its bound is exact at every step.

$$
x = 6.85237 \quad \text{(to five decimal places)}
$$

> [!NOTE]
> Why this example is worth remembering. The same function separates the methods cleanly. Regula falsi stagnates, secant flies, bisection grinds. That is the entire comparison table in one question.

---

## Exam Variants

| Year | Question | Data Given | Key Answer |
|:---|:---|:---|:---|
| 2020 Q.2(a) | Define roots. List comparisons among the four methods | none (06 marks) | $\boxed{\text{Bracketing methods are safe and slow; open methods are fast and unguaranteed}}$ |
| CT-01 Q.2(a) | Bisection vs regula falsi for a safety-critical system | none | Prediction beats speed; use Illinois if you must use regula falsi |
| CT-01 Q.2(b) | Why does one endpoint stall, and the fix | none | Convexity pins the chord to one side; Illinois halves the retained value |

---

## 🏆 Golden Questions (Past Exam Archive)

### 🎯 Define roots of an equation. List the comparisons among bisection, secant, false position and Newton-Raphson methods.
> **Appeared:** 2020 Q.2(a) — (06 marks)

**Full Answer:**

**Root of an equation.** A **root** of $f(x) = 0$ is a value $x^*$ with $f(x^*) = 0$. The graph of $f$ crosses or touches the $x$-axis at $x^*$.

A root is **simple** if $f'(x^*) \ne 0$, and **multiple** (or repeated) if $f'(x^*) = 0$. The distinction matters because the methods below all assume a simple root; a repeated root makes their convergence much slower.

A root is **explicit** if it can be written in closed form, and **implicit** if it can only be found numerically. $\sqrt{2}$ is explicit. The root of $x^5 - x - 1 = 0$ is implicit.

**The four methods compared.**

| | Bisection | False position | Secant | Newton-Raphson |
| :-- | :-- | :-- | :-- | :-- |
| Type | Bracketing | Bracketing | Open | Open |
| Needs $f'$ | No | No | No | **Yes** |
| Needs a sign change | **Yes** | **Yes** | No | No |
| Information used | Endpoints only | Endpoints, keeps one fixed | Last **two** points | Value **and** slope at one point |
| New point from | Midpoint | Chord crossing | Chord through last two | Tangent at last point |
| Convergence order | 1 (linear) | 1, often faster | 1.618 (golden ratio) | **2 (quadratic)** |
| Starts from | $a_0$ | $a_0$ | $x_0, x_1$ | $x_0$ only |
| Guaranteed | **Yes**, from any valid bracket | **Yes** | No | No |
| Function calls per step | 1 | 1 | 1 | 2 (value and derivative) |
| Weakness | Slow, and halves the interval | Stalls on one side for strong convexity | Can diverge, can lose the bracket | Sensitive to the start |

$$
\boxed{\text{Bracketing methods are safe and slow; open methods are fast and unguaranteed}}
$$

**How they relate.** They form a ladder from safest to fastest.

- **Bisection** is the safety net. It only needs a sign change, and it can never fail. That guarantee is why it survives in production codes.
- **False position** uses the same bracket but wastes it, because it keeps only one endpoint and lets the other run away. Faster than bisection, but it stalls on strongly convex functions, as 2021 Q.2(b) shows on $x^{2.2} = 69$.
- **Secant** throws the bracket away and fits a line through the last two points. The order $1.618$ is better than the labels "linear" suggest.
- **Newton** throws away the history except one point and uses the slope. It converges quadratically, so it is the method of choice when $f'$ is available and the start is good.

**The practical rule.** Keep a bracket. Try Newton. If a step leaves the bracket, take a bisection step instead. This hybrid keeps Newton's speed and bisection's guarantee, and it is what real root finders do.

The 2020 Q.2(b) table on $3I^2 - 4I - 4 = 0$ shows what happens without it: the start $I_0 = 1$ throws the first iterate to $3.5$, while the start $I_0 = 3$ reaches $2.000082$ in the same three steps.

> [!NOTE]
> The origin file points to 2021 Q.7(b) and 2023 Q.5(c) for the same lesson. Neither is an NM-2 question. 2021 Q.7(b) is a Gauss-Seidel circuit problem filed under NM-3.5, and it diverges without a diagonally dominant rearrangement. 2023 Q.5(c) is a tautology check filed under DM-3.3. Both reach the same conclusion as the bracketing rule above: an unguarded iteration fails silently, and the guard costs one comparison per step.

> [!NOTE]
> Why the golden ratio order is worth remembering. The secant method's order $1.618 = \frac{1+\sqrt5}{2}$ is what makes it a real alternative to Newton rather than a consolation prize. It needs no derivative, and it is still superlinear. Compare the cost lines: secant makes one function call per step, Newton makes two. Where $f'$ is expensive or genuinely unavailable, the secant method's order per function evaluation is actually competitive. The price is that the secant has no guarantee at all, while bisection does, and in a production code the guarantee is usually worth more than the order.

---

### 🎯 Compare the Bisection Method and Regula Falsi Method in terms of the required condition for application, convergence behavior, and suitability for a safety-critical system.
> **Appeared:** CT-01 Q.2(a) — (marks not printed in source)

**Full Answer:**

Both methods find a root of $f(T) = 0$ by maintaining a bracketing interval, and the difference between them is entirely in how the next point is chosen.

| | Bisection | Regula Falsi |
| :-- | :-- | :-- |
| Requires $f(a)f(b) < 0$ | yes | yes |
| How the next point is chosen | the midpoint $c = (a+b)/2$ | the chord's intercept $c = \dfrac{a f(b) - b f(a)}{f(b) - f(a)}$ |
| Number of function values per step | 1 | 1 |
| Convergence rate | guaranteed linear, $\lvert b-a\rvert$ halves every step | linear, but *rate depends on the function* |
| Interval width | strictly decreases, and predictably | one end may stall indefinitely |
| Needs $f$ to be monotone | no | no |
| Preserves the bracket | always | always, unless modified |

**Required condition.** Identical: a sign change across the initial bracket. Bisection additionally requires only continuity, and it does not care whether the function is monotone, convex or well behaved. Regula Falsi uses the straight line through the two endpoints, so it implicitly assumes the function is reasonably close to linear over the bracket. For a strongly curved function the chord's intercept can be far from the true root.

**Convergence.** Bisection's rate is bounded in advance: after $n$ steps the interval is $(b-a)/2^n$, so the number of steps for a tolerance $\varepsilon$ is $\lceil \log_2\lvert b-a\rvert/\varepsilon\rceil$, known before starting. Regula Falsi is also linear in the interval width but the constant is function-dependent and can be arbitrarily poor. Its classic failure is the **stagnating endpoint**: if $f$ is strongly convex on the bracket, the chord always cuts the same side, one endpoint is retained forever, and convergence degrades to the rate of a single Newton-like step from that end.

**Suitability for a safety-critical system.** This is the part with a real answer, and it is not "regula falsi is faster".

1. **Predictability beats speed.** For a system that must be shown to converge, bisection offers a bound computable in advance; regula falsi offers none. A safety case can state "the bracket is at most $\varepsilon$ after $n$ iterations" and be done.
2. **Bisection cannot be fooled by the function's shape.** A failed sensor or a mis-entered coefficient changes the chord in regula falsi but cannot break the halving in bisection.
3. **Regula falsi is still worth using, with the Illinois modification.** The unmodified method stalls; halving the retained function value at whichever end failed to update removes the stalling and restores a guaranteed linear rate. With that modification it converges faster than bisection and remains bracketed.
4. **Never a bracketing method for a critical interlock.** Both are iterative and neither certifies a root. A safety-critical trip should act on a sign test or a hard bound, with the iteration used to diagnose rather than to decide.

> [!NOTE]
> Check by a curved function. Take $f(T) = T^3 - 2T - 5$ on $[2, 3]$, which is convex on the bracket. Bisection halves $[2, 3]$ every step and reaches $10^{-3}$ in 10 steps by its bound. Unmodified regula falsi on the same bracket retains the upper endpoint for several consecutive steps, because the chord lies below $f$ and its intercept keeps landing on the same side. The Illinois modification removes the stalling in one step. That single function separates the two methods' behaviour completely, which is why it is the standard illustration.

---

### 🎯 During testing, the Regula Falsi Method repeatedly updates only one endpoint of the interval, leading to slow convergence. Explain why this happens, compare it with the Bisection Method, and suggest a suitable improvement.
> **Appeared:** CT-01 Q.2(b) — (marks not printed in source)

**Full Answer:**

**Why one endpoint stalls.** Write the update as

$$
c = b - f(b)\frac{b - a}{f(b) - f(a)}
$$

and let $g(x)$ be the **secant slope** $\dfrac{f(b)-f(a)}{b-a}$. Then

$$
c - b = -\frac{f(b)}{g}
$$

Consider a convex $f$ on $[a,b]$ with $f(a) < 0 < f(b)$. Convexity means the chord lies above the curve, so $c$ always falls on the side nearer $a$, and $f(c) < 0$ always. The update rule is $f(a)f(c) < 0 \Rightarrow a \leftarrow c$, so **$b$ never moves**. The bracket shrinks only from the $a$ side, and it shrinks at the rate of a single Newton step from a fixed endpoint rather than by halving.

The mechanism is that $g$ stays roughly constant while $f(b)$ stays fixed at its original value, so $c$ approaches $b$ geometrically with a ratio set by how much the curve's slope at $b$ exceeds the chord's. For a strongly curved $f$ that ratio is close to $1$ and the method crawls. The limit is that the iteration becomes a Newton step from $b$ alone, which for many functions is fast; the pathology is the many wasted steps before it gets there.

**Comparison with bisection.** Bisection sets $c = (a+b)/2$ with no reference to the function values, so both endpoints move, the width halves exactly, and the iteration count for a tolerance is $\lceil \log_2\lvert b-a\rvert/\varepsilon\rceil$ regardless of the shape of $f$. Regula falsi may converge faster when it works and far slower when it does not, and there is no bound that distinguishes the two cases in advance. The trade is speed against predictability.

**The suitable improvement: the Illinois modification.** At each step, halve the retained function value at whichever endpoint did not move:

$$
f(a) \leftarrow \frac{1}{2}f(a) \quad \text{if } a \text{ was retained}, \qquad f(b) \leftarrow \frac{1}{2}f(b) \quad \text{if } b \text{ was retained}
$$

This is exactly the perturbation that removes the stalling. Once $f(b)$ is halved, the next chord's intercept $c - b = -f(b)/g$ is halved too, so $c$ lands nearer $b$, and the method restores a guaranteed linear rate better than bisection's. Three further variants exist and all behave similarly: **Pegasus**, which halves by $f \leftarrow f(1 - f)$; **Anderson-Björck**, which uses a $1 - 1/(1 + g)$ factor; and a secant-based restart.

**A second, cheaper improvement.** Before iterating, subdivide the initial bracket into, say, four equal parts and test each for a sign change. The sub-interval that brackets the root is usually far more nearly linear, so regula falsi on it has no stalling to suffer. This costs three extra function evaluations once, and it is worth doing when the initial bracket is wide and the function is known to be badly curved.

> [!WARNING]
> What the modification is not. Illinois does not make regula falsi a quadratically convergent method like Newton-Raphson. It restores a linear rate, and a good one, but the guarantee is still a guarantee about a bracket rather than about a root estimate. It also does not help when the failure is a mis-signed bracket to begin with: no amount of damping finds a root the initial interval does not contain.

> [!NOTE]
> The diagnostic is not the number of iterations but **which endpoints move**. Run unmodified regula falsi on the convex bracket and watch $b$ sit still for several steps: that is the pathology. Run the Illinois version and watch both endpoints move from the first step onward. A second check: the Illinois method must never lose the bracket. At every step $f(a)f(c) < 0$ still decides the update, so a root remains bracketed, and the only thing that changes is the weight used in drawing the chord.

---

## ⚡ Exam Tips & Common Mistakes

1. **Build the table once and keep it.** The six-mark question is a table with a one-line box at the end. Writing prose for it wastes time and earns fewer marks.
2. **Order 1.618 is the number that shows you know the material.** Most students write "superlinear" and stop. Write $1.618$ and add that it is the golden ratio.
3. **Add a cost row.** Function evaluations per step is not in every table, but it is what a marker notices. Newton costs two, secant one.
4. **The hybrid is the closing line of every comparison answer.** Keep a bracket, try Newton, fall back to bisection. Say it.
5. **Do not claim bisection converges quadratically because false position sometimes does.** The guarantee and the order move in opposite directions, and the table is what separates them.

## 🔗 Related Topics

- [NM-2.1: Fundamentals & Classification](NM-2.1_Fundamentals_and_Classification.md) — the open versus bracketing split behind this table
- [NM-2.2: Bisection Method](NM-2.2_Bisection_Method.md) — the order-1 method with an exact bound
- [NM-2.3: False Position & Regula Falsi](NM-2.3_False_Position_and_Regula_Falsi.md) — the bracket that can stall
- [NM-2.4: Newton-Raphson Method](NM-2.4_Newton_Raphson_Method.md) — the order-2 method with four failure modes
- [NM-2 Lower: Secant Method](NM-2_Lower_Secant_and_Polynomial_Roots.md) — the order-1.618 middle ground

---

[← Previous: NM-2.4 Newton-Raphson](NM-2.4_Newton_Raphson_Method.md) | [🏠 Index](00_Index.md) | [Next: NM-2 Lower Tier →](NM-2_Lower_Secant_and_Polynomial_Roots.md)
