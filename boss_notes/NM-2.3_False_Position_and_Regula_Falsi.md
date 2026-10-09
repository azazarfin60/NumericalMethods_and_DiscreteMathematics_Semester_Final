[← Previous: NM-2.2 Bisection Method](NM-2.2_Bisection_Method.md) | [🏠 Index](00_Index.md) | [Next: NM-2.4 Newton-Raphson →](NM-2.4_Newton_Raphson_Method.md)

---

# NM-2.3: False Position and Regula Falsi
> **Section:** A (Numerical Methods) | **Priority:** 🔴 | **Exam Frequency:** 5/8 years + CT-01
> **Sources:** Jain Ch.2 §2.3, Topicwise NM-2.3, Fahad Notes §02, CT-01 Q.2

## Why This Topic Matters

Regula falsi is bisection with a brain. Same bracket, same guarantee, but the next point is chosen from the function values instead of the arithmetic mean. Two papers ask for the algorithm, one asks for the derivation, and one runs it on $x^{2.2} = 69$. The long iteration table on that question is where marks are lost, because the upper endpoint never moves and students "fix" it.

---

## 📝 Key Definitions

> **Method of false position:** The root is approximated by the $x$-axis intercept of the straight line through the two bracketing points, and the bracket is retained.

> **Regula falsi:** Latin for "rule of false position". The same method: replace $f$ on $[a,b]$ by its chord, and take the chord's intercept as the next iterate.

> **Illinois modification:** A variant of regula falsi that halves the retained function value at whichever endpoint failed to update, which removes one-sided stagnation.

---

## Core Theory

### How It Differs From Bisection

Bisection ignores the function values entirely. It sets $c = \frac{a+b}{2}$ no matter how steep the curve is.

Regula falsi uses them. It draws the chord through $(a, f(a))$ and $(b, f(b))$, and takes where that chord crosses the axis:

$$
c = \frac{a\,f(b) - b\,f(a)}{f(b) - f(a)}
$$

If $f(a)$ is tiny and $f(b)$ is huge, the chord crosses close to $a$. That is better information than a blind midpoint.

![False position: chord through A[a, f(a)] and B[b, f(b)] cutting the x-axis at x1](diagrams/nm2_false_position_geometric.jpg)

*Figure 2.2 (Jain, p. 28): the chord through the two bracketing points replaces the curve, and its intercept becomes the next iterate. The sign change is always kept, so the root stays trapped.*

### Derivation From Scratch (2018 Q.2(b))

The exam asks for this derivation, so write it out in full.

**Setup.** Let $x_0$ and $x_1$ satisfy $f(x_0)f(x_1) < 0$, so a root lies between them. Write $f_0 = f(x_0)$ and $f_1 = f(x_1)$.

**The idea.** Replace $f$ on $[x_0, x_1]$ by the straight line through $(x_0, f_0)$ and $(x_1, f_1)$, and take the intercept of that line with the $x$-axis.

**Step 1. Equation of the chord.** By the two-point form:

$$
\frac{y - f_0}{f_1 - f_0} = \frac{x - x_0}{x_1 - x_0}
$$

**Step 2. Set $y = 0$.** Call the resulting $x$ the next approximation $x_2$:

$$
\frac{-f_0}{f_1 - f_0} = \frac{x_2 - x_0}{x_1 - x_0}
$$

**Step 3. Solve for $x_2$.**

$$
x_2 - x_0 = \frac{-f_0(x_1 - x_0)}{f_1 - f_0}
$$

$$
\boxed{x_2 = x_0 - \frac{f_0(x_1 - x_0)}{f_1 - f_0}}
$$

**Step 4. Combine over a common denominator** to get the textbook form:

$$
x_2 = \frac{x_0(f_1 - f_0) - f_0(x_1 - x_0)}{f_1 - f_0} = \frac{x_0f_1 - x_1f_0}{f_1 - f_0}
$$

The second form shows that $x_2$ is a **weighted average** of $x_0$ and $x_1$, with weights $f_1$ and $-f_0$. A weighted average of two numbers stays between them, which is exactly why regula falsi never leaves the bracket.

**Step 5. Continue.** Evaluate $f(x_2)$, replace whichever of $x_0$ and $x_1$ has the same sign as $f(x_2)$, and apply the same formula again.

### The Algorithm (2017 Q.2(b))

1. Accept the function $f(x)$, the tolerance $\varepsilon$, and the maximum iteration count $N$.
2. Accept the ends $a$ and $b$ of the bracketing interval.
3. Compute $f(a)$ and $f(b)$. If $f(a)f(b) > 0$, report that the interval does not bracket a root and stop.
4. Compute
   $$
   c = \frac{a\,f(b) - b\,f(a)}{f(b) - f(a)}
   $$
   and evaluate $f(c)$.
5. Test for convergence. If $|f(c)| < \varepsilon$, or if $|b - a| < \varepsilon$, accept $c$ as the root and stop.
6. If $f(a)f(c) < 0$, set $b = c$; otherwise set $a = c$.
7. If the iteration count exceeds $N$, report non-convergence and stop. Otherwise return to step 4.

> [!WARNING]
> Step 6 is the whole method. Only **one** end of the bracket moves at each iteration, and which one is decided by the sign of $f(c)$. Write the test the other way round and the method silently becomes something that does not converge.

### Convergence, and the One Weakness

The sign change is always preserved, so the method converges whenever the initial pair brackets a root. Convergence is linear, and it is usually faster than bisection because a chord is a better model of $f$ than a midpoint.

The weakness is **one-sided stagnation**. If the function is strongly convex over the bracket, the chord always cuts the axis on the same side. One endpoint is retained forever, and the bracket shrinks only from the other side. The Illinois modification fixes it by halving the retained function value at whichever end failed to update.

---

## Worked Example: $x^{2.2} = 69$ by Regula Falsi

**Problem.** Given that the equation $x^{2.2} = 69$ has a root between 5 and 8, use the method of regula-falsi to determine it.

> **Source:** 2021 Q.2(b) [Marks: 04, CO: 3]

**Step 1. Define the function and check the bracket.**

$$
f(x) = x^{2.2} - 69
$$

$$
f(5) = 5^{2.2} - 69 = 34.4932 - 69 = -34.5068
$$

$$
f(8) = 8^{2.2} - 69 = 97.0059 - 69 = +28.0059
$$

$f(5) < 0 < f(8)$, so a root lies in $(5, 8)$. The function is continuous there since $x^{2.2}$ is continuous for $x > 0$.

**Step 2. The formula.** Draw the straight line joining the two endpoints. It cuts the $x$-axis at

$$
x = \frac{a f(b) - b f(a)}{f(b) - f(a)}
$$

**Step 3. Iterate.** Keep whichever endpoint has the same sign as the new point, and replace the other.

| Iteration | $a$ | $b$ | New point $x$ | $f(x)$ |
| --: | --: | --: | --: | --: |
| 1 | 5.000000 | 8.000000 | 6.655990 | $-4.27563$ |
| 2 | 6.655990 | 8.000000 | 6.834002 | $-0.40615$ |
| 3 | 6.834002 | 8.000000 | 6.850670 | $-0.03755$ |
| 4 | 6.850670 | 8.000000 | 6.852209 | $-0.00346$ |
| 5 | 6.852209 | 8.000000 | 6.852351 | $-0.00032$ |
| 6 | 6.852351 | 8.000000 | 6.852364 | $-0.00003$ |
| 7 | 6.852364 | 8.000000 | 6.852365 | $-0.000003$ |

Working the first row in full:

$$
x_1 = \frac{5(28.0059) - 8(-34.5068)}{28.0059 - (-34.5068)} = \frac{140.0295 + 276.0544}{62.5127} = \frac{416.0839}{62.5127} = 6.655990
$$

$$
\boxed{x = 6.85237 \quad \text{(to five decimal places)}}
$$

Or to four places, $x = 6.8524$.

> [!WARNING]
> Why the upper endpoint never moves. The table gives $b = 8.000000$ for every iteration. This is the well known **one-sided stagnation** of regula falsi on this function. The graph is strongly convex over $(5, 8)$, so the chord always cuts the axis on the same side, and only the $a$ endpoint is replaced. Seven iterations to reach six figures looks like bisection's pace, not regula falsi's. The **Illinois variant** fixes it by halving the retained function value on each step: repeat the retained end as half its function value every second iteration. That restores fast convergence while keeping the sign-change guarantee.

> [!NOTE]
> **Check by three independent routes.**
>
> *Secant method.* Starting from the same two points, the secant iteration gives $6.65599006$, $6.83400179$, $6.85268624$, $6.85236460$, $6.85236512$. Same answer to more digits.
>
> *Closed form.* $x^{2.2} = 69$ with $2.2 = \frac{11}{5}$ gives $x = 69^{5/11} = 6.8523651204$. The last regula falsi iterate is $6.852365$, and the closed form rounds to $6.85237$. All three agree.
>
> *Bisection.* Starting from $(5, 8)$, after 18 iterations the bracket is $(6.85236359, 6.85237503)$ and the midpoint $6.85236931$ is within $4.2 \times 10^{-6}$ of the exact root. One more bisection halves that again.

---

## Exam Variants

| Year | Question | Data Given | Key Answer |
|:---|:---|:---|:---|
| 2021 Q.2(b) | Regula falsi on a bracketed equation | $x^{2.2} = 69$, root in $(5, 8)$ | $\boxed{x = 6.85237 \quad \text{(to five decimal places)}}$ |
| 2018 Q.2(b) | Derive the next approximation | none (04 marks, theory) | $\boxed{x_2 = x_0 - \frac{f_0(x_1 - x_0)}{f_1 - f_0}}$ |
| 2017 Q.2(b) | Write the algorithm steps | none (04 marks, theory) | Algorithm with $c = \frac{a f(b) - b f(a)}{f(b) - f(a)}$ |
| CT-01 Q.2(a) | Compare bisection and regula falsi for a safety-critical system | none | Comparison table, prediction beats speed |
| CT-01 Q.2(b) | Why does one endpoint stall, and what fixes it | none | Illinois modification: halve the retained value |

---

## 🏆 Golden Questions (Past Exam Archive)

### 🎯 Write down the algorithm steps while finding the root of a nonlinear equation using false position method.
> **Appeared:** 2017 Q.2(b) — (04 marks)

**Full Answer:**

**The formula.** With $x_0, x_1$ bracketing the root, the next approximation is the $x$-axis intercept of the chord through $(x_0, f_0)$ and $(x_1, f_1)$:

$$
x_2 = \frac{x_0f_1 - x_1f_0}{f_1 - f_0}
$$

**Algorithm.**

1. Accept the function $f(x)$, the tolerance $\varepsilon$, and the maximum iteration count $N$.
2. Accept the ends $a$ and $b$ of the bracketing interval.
3. Compute $f(a)$ and $f(b)$. If $f(a)f(b) > 0$, report that the interval does not bracket a root and stop.
4. Compute
   $$
   c = \frac{a\,f(b) - b\,f(a)}{f(b) - f(a)}
   $$
   and evaluate $f(c)$.
5. Test for convergence. If $|f(c)| < \varepsilon$, or if $|b - a| < \varepsilon$, accept $c$ as the root and stop.
6. If $f(a)f(c) < 0$, set $b = c$; otherwise set $a = c$.
7. If the iteration count exceeds $N$, report non-convergence and stop. Otherwise return to step 4.

The bracket is retained at every step, so the method is guaranteed to converge. Convergence is linear and can be slow when one end of the bracket stalls against a nearly straight region of $f$; that is the defect the Illinois modification addresses, by halving the retained function value at whichever end failed to update.

---

### 🎯 Derive the expression of the next approximation of a root of the non-linear function $f(x) = 0$ using regula-falsi method.
> **Appeared:** 2018 Q.2(b) — (04 marks)

**Full Answer:**

Let $x_0$ and $x_1$ be two points with $f(x_0)f(x_1) < 0$, so that a root lies between them. Write $f_0 = f(x_0)$ and $f_1 = f(x_1)$.

Replace $f$ on $[x_0, x_1]$ by the straight line through $(x_0, f_0)$ and $(x_1, f_1)$, and take the intercept of that line with the $x$-axis.

The equation of the chord is

$$
\frac{y - f_0}{f_1 - f_0} = \frac{x - x_0}{x_1 - x_0}
$$

The chord meets the $x$-axis at $y = 0$. Writing the next approximation as $x_2$ and setting $y = 0$:

$$
\frac{-f_0}{f_1 - f_0} = \frac{x_2 - x_0}{x_1 - x_0}
$$

$$
x_2 - x_0 = \frac{-f_0(x_1 - x_0)}{f_1 - f_0}
$$

$$
\boxed{x_2 = x_0 - \frac{f_0(x_1 - x_0)}{f_1 - f_0}}
$$

**Equivalent forms.** Expanding the numerator:

$$
x_2 = \frac{x_0f_1 - x_1f_0}{f_1 - f_0}
$$

which shows that $x_2$ is a weighted average of $x_0$ and $x_1$, the weights being the opposing function values. A third form places the unknown on one side:

$$
x_2 = \frac{x_0f_1 - x_1f_0}{f_1 - f_0} = \frac{f_1x_0 - f_0x_1}{f_1 - f_0}
$$

**Continuing.** Once $x_2$ is computed, $f(x_2)$ is evaluated and either $x_0$ or $x_1$ is replaced by $x_2$, retaining the sub-interval in which the sign change occurs. The same formula is then applied again.

**Note on convergence.** The method always converges whenever the initial pair brackets the root, since the sign change is preserved. Convergence is linear, and is faster than bisection, because the chord is a better model of $f$ than the midpoint. A drawback is that one end of the bracket may stall, in which case the interval shrinks very slowly; this is the weakness the Illinois modification is designed to repair.

---

### 🎯 Given that the equation $x^{2.2} = 69$ has a root between 5 and 8. Use the method of regula-falsi to determine it.
> **Appeared:** 2021 Q.2(b) — (04 marks, CO: 3)

The full solution is the Worked Example above. The exam answer needs five things:

1. The function and the bracket test, $f(5) = -34.5068$ and $f(8) = +28.0059$.
2. The formula $x = \frac{a f(b) - b f(a)}{f(b) - f(a)}$ stated before the table.
3. The seven-row table, with $b = 8.000000$ left exactly as it falls out.
4. The first row worked out in full arithmetic, as the demonstration that the table is right.
5. The boxed answer to five decimal places.

$$
x_1 = \frac{5(28.0059) - 8(-34.5068)}{28.0059 - (-34.5068)} = \frac{140.0295 + 276.0544}{62.5127} = \frac{416.0839}{62.5127} = 6.655990
$$

$$
\boxed{x = 6.85237 \quad \text{(to five decimal places)}}
$$

> [!TIP]
> Sanity-check your first iterate before writing the rest. $f(5) = -34.51$ and $f(8) = +28.01$ are of similar size, so the chord's intercept lands near the middle of the interval, at $6.656$, rather than near either end. A number far from $6.656$ means a sign was dropped somewhere.

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
> Check by a curved function. Take $f(T) = T^3 - 2T - 5$ on $[2, 3]$, which is convex on the bracket. Bisection halves $[2,3]$ every step and reaches $10^{-3}$ in 10 steps by its bound. Unmodified regula falsi on the same bracket retains the upper endpoint for several consecutive steps, because the chord lies below $f$ and its intercept keeps landing on the same side. The Illinois modification removes the stalling in one step. That single function separates the two methods' behaviour completely, which is why it is the standard illustration.

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

1. **The chord formula has two common sign slips.** Write it once as $c = \frac{a f(b) - b f(a)}{f(b) - f(a)}$ and reuse that exact form every time. Students who switch between $a f(b) - b f(a)$ and $b f(a) - a f(b)$ halfway down a table produce garbage.
2. **Do not "correct" a stalled endpoint.** In 2021 Q.2(b), $b = 8.000000$ in every row is the correct answer. Changing it to make the table look tidier loses marks.
3. **One endpoint moves per iteration.** Always. State the rule before the table.
4. **Mention Illinois by name.** Any question about slow regula falsi convergence wants the word "Illinois" and the halving rule.
5. **The derivation is a fixed six lines.** Chord equation, set $y = 0$, cross-multiply, solve, combine, state the weighted-average interpretation. Practise it until it is automatic.
6. **Check your first iterate against the midpoint.** If the two bracketing values are similar in size, the chord intercept lands near the middle of the interval. A far-off first row means a dropped sign.

## 🔗 Related Topics

- [NM-2.2: Bisection Method](NM-2.2_Bisection_Method.md) — the same bracket with a blind midpoint
- [NM-2.4: Newton-Raphson Method](NM-2.4_Newton_Raphson_Method.md) — replaces the chord with a tangent, one point instead of two
- [NM-2.5 / NM-2 Lower: Secant Method](NM-2_Lower_Secant_and_Polynomial_Roots.md) — the same chord formula without keeping the bracket
- [NM-2.6: Method Comparison & Convergence](NM-2.6_Method_Comparison_and_Convergence.md) — where false position sits on the safe-to-fast ladder

---

[← Previous: NM-2.2 Bisection Method](NM-2.2_Bisection_Method.md) | [🏠 Index](00_Index.md) | [Next: NM-2.4 Newton-Raphson →](NM-2.4_Newton_Raphson_Method.md)
