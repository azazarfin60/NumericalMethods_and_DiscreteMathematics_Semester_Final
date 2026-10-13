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

Every block below is copied from `../answers_exam_style/`, which is the
only place an answer is authored. A number here is the same number, character
for character, as the one it came from.


### [2017 Q.2(b)]

**Question.** Write down the algorithm steps while finding the root of a nonlinear equation using false position method.

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
5. Test for convergence. If $|f(c)| < \varepsilon$, or if $|b - a| < \varepsilon$,
   accept $c$ as the root and stop.
6. If $f(a)f(c) < 0$, set $b = c$; otherwise set $a = c$.
7. If the iteration count exceeds $N$, report non-convergence and stop.
   Otherwise return to step 4.

**Note.** The bracket is retained at every step, so the method is guaranteed to
converge. Convergence is linear and can be slow when one end of the bracket
stalls against a nearly straight region of $f$; this is the defect that the
Illinois modification addresses.

---

### [2018 Q.2(b)]

**Question.** Derive the expression of the next approximation of a root of the non-linear function $f(x) = 0$ using regula-falsi method.

**Solution.**

**Setup.** Let $x_0$ and $x_1$ be two points with $f(x_0)f(x_1) < 0$, so that a
root lies between them. Write $f_0 = f(x_0)$ and $f_1 = f(x_1)$.

**The idea.** Replace $f$ on $[x_0, x_1]$ by the straight line through
$(x_0, f_0)$ and $(x_1, f_1)$, and take the intercept of that line with the
$x$-axis as the next approximation.

**Derivation.** The equation of the chord is

$$\frac{y - f_0}{f_1 - f_0} = \frac{x - x_0}{x_1 - x_0}$$

The chord meets the $x$-axis at $y = 0$. Writing the next approximation as
$x_2$ and setting $y = 0$:

$$\frac{-f_0}{f_1 - f_0} = \frac{x_2 - x_0}{x_1 - x_0}$$

$$x_2 - x_0 = \frac{-f_0(x_1 - x_0)}{f_1 - f_0}$$

$$\boxed{x_2 = x_0 - \frac{f_0(x_1 - x_0)}{f_1 - f_0}}$$

**Equivalent forms.** Expanding the numerator:

$$x_2 = \frac{x_0f_1 - x_1f_0}{f_1 - f_0}$$

which shows that $x_2$ is a weighted average of $x_0$ and $x_1$, the weights
being the opposing function values. A third form places the unknown on one side:

$$x_2 = \frac{x_0f_1 - x_1f_0}{f_1 - f_0} = \frac{f_1x_0 - f_0x_1}{f_1 - f_0}$$

**Continuing.** Once $x_2$ is computed, $f(x_2)$ is evaluated and either $x_0$
or $x_1$ is replaced by $x_2$, retaining the sub-interval in which the sign
change occurs. The same formula is then applied again.

**Note on convergence.** The method always converges whenever the initial pair
brackets the root, since the sign change is preserved. Convergence is linear,
and is faster than bisection, because the chord is a better model of $f$ than
the midpoint. A drawback is that one end of the bracket may stall, in which
case the interval shrinks very slowly; this is the weakness the Illinois
modification is designed to repair.

---

### [2021 Q.2(b)]

**Question.** Given that the equation $x^{2.2} = 69$ has a root between 5 and 8. Use the method of regula-falsi to determine it.

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

$$
\boxed{x = 6.85237 \quad \text{(to five decimal places)}}
$$

Or to four places, $x = 6.8524$.

> [!info] Check by two independent routes
> **Secant method.** Starting from the same two points, the secant iteration gives
> $6.65599006$, $6.83400179$, $6.85268624$, $6.85236460$, $6.85236512$. Same
> answer to more digits.
>
> **Closed form.** $x^{2.2} = 69$ with $2.2 = \frac{11}{5}$ gives
> $x = 69^{5/11} = 6.8523651204$. The last regula falsi iterate is
> $6.852365$, and the closed form rounds to $6.85237$. All three agree.
>
> **Bisection.** Starting from $(5, 8)$, after 18 iterations the bracket is
> $(6.85236359, 6.85237503)$ and the midpoint $6.85236931$ is within
> $4.2 \times 10^{-6}$ of the exact root. One more bisection halves that again.

> [!note] Why the upper endpoint never moves
> The table gives $b = 8.000000$ for every iteration. This is the well known
> **one-sided stagnation** of regula falsi on this function. The graph is strongly
> convex over $(5, 8)$, so the chord always cuts the axis on the same side, and
> only the $a$ endpoint is replaced.
>
> The consequence is that convergence is much slower than the "superlinear"
> label suggests. The **Illinois variant** fixes it by halving the retained
> function value on each step:
> $$\text{repeat } a f(a) \text{ as } \frac{1}{2}a f(a) \text{ every second iteration}$$
> That restores the fast convergence while keeping the sign-change guarantee. The
> same shape appears in 2017 Q.2(b), where the same function is used with a
> different bracket.

---

**Answered in phase P6, in `../CT_Questions/`.**

- *CT-01 Q.2(b)* is a class-test question. Its answer is in `../CT_Questions/CT_answers_exam_style.md`, with the reasoning in `../CT_Questions/CT_answers_explanation.md`.

---

[🏠 Subtopic Index](00_Index.md) | [← Prev: NM-2.2 Bisection Method](NM-2.2_Bisection_Method.md) | [Next: NM-2.4 Newton-Raphson Method →](NM-2.4_Newton_Raphson_Method.md)
