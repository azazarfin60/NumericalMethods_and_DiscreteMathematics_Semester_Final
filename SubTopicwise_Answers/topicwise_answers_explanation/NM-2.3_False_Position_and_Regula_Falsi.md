---
title: "NM-2.3 · False Position / Regula Falsi"
tags:
  - numerical-methods
  - discrete-mathematics
  - topicwise
---



[🏠 Subtopic Index](00_Index.md) | [← Prev: NM-2.2 Bisection Method](NM-2.2_Bisection_Method.md) | [Next: NM-2.4 Newton-Raphson Method →](NM-2.4_Newton_Raphson_Method.md)

---

# NM-2.3 · False Position / Regula Falsi

Every block below is copied from `../answers_explanation/`. The reasoning
is written once, in the year-wise file, and is not restated here.


### [2017 Q.2(b)]

**Question.** Write down the algorithm steps while finding the root of a nonlinear equation using false position method.

*[Marks: 04]*

**Solution.**

**The formula.** With $x_0, x_1$ bracketing the root, the next approximation is
the $x$-axis intercept of the chord through $(x_0, f_0)$ and $(x_1, f_1)$:

$$x_2 = \frac{x_0f_1 - x_1f_0}{f_1 - f_0}$$

**Algorithm.**

1. Accept the function $f(x)$, the tolerance $\varepsilon$, and the maximum
   iteration count $N$.
2. Accept the ends $a$ and $b$ of the bracketing interval.
3. Compute $f(a)$ and $f(b)$. If $f(a)f(b) > 0$, report that the interval does
   not bracket a root and stop.
4. Compute
   $$c = \frac{a\,f(b) - b\,f(a)}{f(b) - f(a)}$$
   and evaluate $f(c)$.
5. Test for convergence. If $\lvert f(c)\rvert < \varepsilon$, or if
   $\lvert b - a\rvert < \varepsilon$, accept $c$ as the root and stop.
6. If $f(a)f(c) < 0$, set $b = c$; otherwise set $a = c$.
7. If the iteration count exceeds $N$, report non-convergence and stop.
   Otherwise return to step 4.

**Step 6 is the whole method.** Note carefully that only *one* end of the
bracket moves at each iteration, and which one is decided by the sign of
$f(c)$. Write the test the other way round and the method silently becomes
something that does not converge.

**Note.** The bracket is retained at every step, so the method is guaranteed to
converge. Convergence is linear and can be slow when one end of the bracket
stalls against a nearly straight region of $f$; that is the defect the Illinois
modification addresses, by halving the retained function value at whichever end
failed to update.

---

### [2018 Q.2(b)]

**Question.** Derive the expression of the next approximation of a root of the non-linear function $f(x) = 0$ using regula-falsi method.

*[Marks: 04]*

**Solution.**

**Setup.** Let $x_0$ and $x_1$ satisfy $f(x_0)f(x_1) < 0$, so a root lies
between them. Write $f_0 = f(x_0)$ and $f_1 = f(x_1)$.

**The idea.** Replace $f$ on $[x_0, x_1]$ by the straight line through the two
known points, and take where that line crosses the $x$-axis. Because the line
joins $f_0$ and $f_1$, which have opposite signs, it must cross.

**Derivation.** The chord has equation

$$\frac{y - f_0}{f_1 - f_0} = \frac{x - x_0}{x_1 - x_0}$$

Set $y = 0$ and call the resulting $x$ the next approximation $x_2$:

$$\frac{-f_0}{f_1 - f_0} = \frac{x_2 - x_0}{x_1 - x_0}$$

$$x_2 - x_0 = \frac{-f_0(x_1 - x_0)}{f_1 - f_0}$$

$$\boxed{x_2 = x_0 - \frac{f_0(x_1 - x_0)}{f_1 - f_0}}$$

**The same formula, written another way.** Combining over a common denominator,

$$x_2 = \frac{x_0(f_1 - f_0) - f_0(x_1 - x_0)}{f_1 - f_0} = \frac{x_0f_1 - x_1f_0}{f_1 - f_0}$$

which is the form most textbooks print. The two forms are identical, and the
second one shows immediately that $x_2$ is a *weighted average* of $x_0$ and
$x_1$ with weights $f_1$ and $-f_0$. A weighted average of two numbers stays
between them, which is why regula falsi never leaves the bracket, exactly like
bisection.

**Continuing.** Evaluate $f(x_2)$, replace whichever of $x_0$, $x_1$ has the
same sign as $f(x_2)$, and apply the same formula again.

**Convergence and the one weakness.** The sign change is always preserved, so
the method converges whenever the initial pair brackets a root. Convergence is
linear, and faster than bisection because a chord is a better model of $f$ than
a midpoint. The weakness is that *one end of the bracket can stall*: if the
function is strongly curved near the root, one function value stays much larger
in magnitude than the other for many iterations and that endpoint never moves
appreciably. The Illinois modification, which halves the retained function
value once an endpoint fails to update, exists to repair exactly this.

---

### [2021 Q.2(b)]

**Question.** Given that the equation $x^{2.2} = 69$ has a root between 5 and 8. Use the method of regula-falsi to determine it.

*[Marks: 04, CO: 3]*

**Solution.**

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

$f(5) < 0 < f(8)$, so a root lies in $(5, 8)$. The function is continuous there
since $x^{2.2}$ is continuous for $x > 0$.

**Step 2. The formula.** Draw the straight line joining the two endpoints. It cuts
the $x$-axis at

$$
x = \frac{a f(b) - b f(a)}{f(b) - f(a)}
$$

> [!warning] The bracket is nearly balanced, and that is a coincidence worth noticing
> $f(5) = -34.51$ and $f(8) = +28.01$ are of similar size, so the chord's
> intercept lands near the middle of the interval, $6.656$, rather than near
> either end. Because the signs are already close in magnitude, the first step is
> nearly as good as bisection's.
>
> Check your own arithmetic against this: the first iterate is
> $\frac{5(28.0059) + 8(34.5068)}{28.0059 + 34.5068} = \frac{416.0839}{62.5127}$.
> A number far from $6.656$ means a sign was dropped somewhere.

**Step 3. Iterate.** Keep whichever endpoint has the same sign as the new point and
replace the other.

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

$$\boxed{x = 6.85237 \quad \text{(to five decimal places)}}$$

Or to four places, $x = 6.8524$.

> [!info] Check by two independent routes
> **Secant method.** Starting from the same two points, the secant iteration gives
> $6.65599006$, $6.83400179$, $6.85268624$, $6.85236460$, $6.85236512$. Same
> answer to more digits.
>
> **Closed form.** $x^{2.2} = 69$ with $2.2 = \frac{11}{5}$ gives
> $x = 69^{5/11} = 6.8523651204$. The last regula falsi iterate is $6.852365$, and
> the closed form rounds to $6.85237$. All three agree.
>
> **Bisection.** Starting from $(5, 8)$, after 18 iterations the bracket is
> $(6.85236359, 6.85237503)$ and the midpoint $6.85236931$ is within
> $4.2 \times 10^{-6}$ of the exact root. One more bisection halves that again.

> [!warning] Why the upper endpoint never moves
> The table gives $b = 8.000000$ for every iteration. This is the well known
> **one-sided stagnation** of regula falsi on this function. The graph is strongly
> convex over $(5, 8)$, so the chord always cuts the axis on the same side, and
> only the $a$ endpoint is replaced.
>
> The consequence is that convergence is much slower than the "superlinear" label
> suggests. Seven iterations to reach six figures looks like bisection's pace,
> not regula falsi's. The **Illinois variant** fixes it by halving the retained
> function value on each step:
> $$\text{repeat } a f(a) \text{ as } \frac{1}{2}a f(a) \text{ every second iteration}$$
> That restores the fast convergence while keeping the sign-change guarantee.
>
> The same function with a different bracket appears in 2017 Q.2(b), which is
> worth knowing about, since the stagnation behaves differently there.

---

**Answered in phase P6, in `../CT_Questions/`.**

- *CT-01 Q.2(b)* is a class-test question. Its answer is in `../CT_Questions/CT_answers_exam_style.md`, with the reasoning in `../CT_Questions/CT_answers_explanation.md`.

---

[🏠 Subtopic Index](00_Index.md) | [← Prev: NM-2.2 Bisection Method](NM-2.2_Bisection_Method.md) | [Next: NM-2.4 Newton-Raphson Method →](NM-2.4_Newton_Raphson_Method.md)
