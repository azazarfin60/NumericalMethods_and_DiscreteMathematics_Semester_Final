[← Previous: NM-6.1 Concepts](NM-6.1_Concepts.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: NM-6.3 Tabulated Optima →](NM-6.3_Tabulated_Optima.md)

---

# NM-6.2: One-Dimensional Unconstrained Optimization

> 🟡 **Priority:** Light (Emerging) | **Tested:** 1/8 years (2021 Q.6(b)) | **Typical marks:** 3

## What This Is (and Why It Matters)

Suppose you have a smooth, continuous mathematical function $f(x)$ with no boundaries or restrictions, and you want to locate its maximum or minimum value.

From elementary calculus, you know that a smooth function reaches a local peak or valley wherever its tangent line is completely flat:

$$
f'(x) = 0
$$

This single equation holds the secret to optimization: **finding an optimum is identical to finding a root of the derivative!**

If you already know the Newton-Raphson root-finding method from NM-2.4, you already understand how this works. But there is a famous trap that trips students up every single year: what goes in the denominator? In optimization, the denominator is the second derivative $f''(x)$, not the first derivative $f'(x)$.

In this note, we will derive Newton's optimization formula, explain the second derivative test, see how parabolas guide each step, and solve the 2021 RUET exam problem completely.

---

## 📝 Key Definitions

> **Stationary Point / Critical Point:** "A point $x^*$ is called a stationary point of a differentiable function $f(x)$ if the first derivative vanishes at that point, that is, $f'(x^*) = 0$." -- Jain, §2.1
>
> **In simple words:** A location on a curve where the slope is zero and the tangent line is completely horizontal. It can be a local hill peak, a local valley bottom, or a flat terrace (saddle point).

> **Newton's Method for Optimization:** "Newton's method determines an unconstrained extremum of a twice-differentiable function $f(x)$ by applying the Newton-Raphson iteration to the derivative equation $f'(x) = 0$, yielding the recurrence $x_{n+1} = x_n - \frac{f'(x_n)}{f''(x_n)}$." -- Rao, §2.4
>
> **In simple words:** You start with a guess, fit a parabola to the curve that matches its slope and bending, jump directly to that parabola's peak or valley, and repeat until the answers settle down.

> **Second Derivative Test:** "Let $x^*$ be a stationary point where $f'(x^*) = 0$. If $f''(x^*) < 0$, the function is locally strictly concave and $x^*$ is a local maximum. If $f''(x^*) > 0$, the function is locally strictly convex and $x^*$ is a local minimum." -- Jain, §2.1
>
> **In simple words:** The second derivative tells you how the curve curves. If it bends downward like an umbrella ($f'' < 0$), you are standing at the top of a hill. If it bends upward like a bowl ($f'' > 0$), you are sitting at the bottom of a bowl.

---

## The Core Idea

### Deriving the Iteration Formula

We want to find $x^*$ such that $f'(x^*) = 0$.

Define a helper function $g(x) = f'(x)$. Our goal is to solve the standard root-finding problem $g(x) = 0$.

Recall the standard Newton-Raphson formula for solving $g(x) = 0$ from NM-2.4:

$$
x_{n+1} = x_n - \frac{g(x_n)}{g'(x_n)}
$$

Now substitute $g(x) = f'(x)$ and $g'(x) = f''(x)$:

$$
x_{n+1} = x_n - \frac{f'(x_n)}{f''(x_n)}
$$

**Reading this formula:**
- The numerator $f'(x_n)$ is the **slope** of the function at your current position. It tells you whether you are moving uphill or downhill.
- The denominator $f''(x_n)$ is the **curvature** of the function. It tells you how fast the slope is changing.
- Their ratio $\frac{f'(x_n)}{f''(x_n)}$ gives the step size needed to reach a flat point.

### The Parabolic View: Why Newton Works

Why does this formula converge so fast? Because it fits a local parabola to the curve at every step.

Consider the second-order Taylor series expansion of $f(x)$ around your current guess $x_n$:

$$
f(x) \approx f(x_n) + f'(x_n)(x - x_n) + \frac{1}{2}f''(x_n)(x - x_n)^2
$$

This is a quadratic polynomial (a parabola). To find the vertex of this approximating parabola, take its derivative with respect to $x$ and set it to zero:

$$
\frac{d}{dx}[f(x)] \approx f'(x_n) + f''(x_n)(x - x_n) = 0
$$

Solving for $x$:

$$
f''(x_n)(x - x_n) = -f'(x_n) \implies x - x_n = -\frac{f'(x_n)}{f''(x_n)}
$$

$$
x = x_n - \frac{f'(x_n)}{f''(x_n)}
$$

This is identical to Newton's iteration! At each step, Newton's method approximates the function by a local parabola and leaps straight to the vertex of that parabola.

> [!WARNING] Common Trap: The denominator is $f''$, not $f'$
> Newton's root-finding formula for $f(x) = 0$ has $f'$ in the denominator: $x_{n+1} = x_n - \frac{f}{f'}$.
> But Newton's optimization formula is solving $f'(x) = 0$, so its denominator is $(f')' = f''$:
> $$
> x_{n+1} = x_n - \frac{f'(x_n)}{f''(x_n)}
> $$
> If you mistakenly use $f'$ in the denominator, you will find where the curve crosses the axis ($f = 0$), not where it reaches its peak!

### The Second Derivative Check is Mandatory

Newton's method solves $f'(x) = 0$. That means it finds stationary points blindly: it cannot tell whether the point it found is a maximum, a minimum, or an inflection point.

Once the iteration converges to $x^*$, you must always evaluate $f''(x^*)$:
- If $f''(x^*) < 0$: The stationary point is a **maximum**.
- If $f''(x^*) > 0$: The stationary point is a **minimum**.
- If $f''(x^*) = 0$: The test is inconclusive.

In an exam script, never stop after calculating $x^*$. Always compute $f''(x^*)$, state its sign, and conclude whether it is a maximum or minimum.

### Step-by-Step Algorithm

1. **Differentiate twice:** Calculate analytical expressions for $f'(x)$ and $f''(x)$.
2. **Choose an initial guess:** Pick $x_0$ close to the suspected peak.
3. **Iterate:** For $n = 0, 1, 2, \dots$, evaluate $f'(x_n)$ and $f''(x_n)$, then compute:
   $$
   x_{n+1} = x_n - \frac{f'(x_n)}{f''(x_n)}
   $$
4. **Check convergence:** Stop when $|x_{n+1} - x_n| < \epsilon$ or $|f'(x_n)| < \epsilon$.
5. **Classify the extremum:** Evaluate $f''(x^*)$. Confirm $f''(x^*) < 0$ for a maximum.
6. **Evaluate the optimal value:** Compute $f(x^*)$.

---

## 🔧 Worked Example

> **From:** 2021 Q.6(b), [Marks: 03]

**The question:** Use Newton's method to find the maximum of $f(x) = 2\sin x - \frac{x^2}{10}$ with an initial guess of $x_0 = 2.5$.

**Let's solve this step by step.**

### Step 1. Reduce to a root-finding problem and differentiate

An interior maximum of a smooth function $f(x)$ satisfies $f'(x) = 0$. We apply Newton's method to the derivative function.

First, compute the first and second derivatives:

$$
f'(x) = 2\cos x - \frac{x}{5}
$$

$$
f''(x) = -2\sin x - \frac{1}{5}
$$

Newton's iteration for $f'(x) = 0$ is:

$$
x_{n+1} = x_n - \frac{f'(x_n)}{f''(x_n)} = x_n - \frac{2\cos x_n - x_n/5}{-2\sin x_n - 1/5}
$$

### Step 2. Carry out the iterations from $x_0 = 2.5$

Remember that angles in trigonometric functions must be in **radians** on your calculator!

**Iteration 0 ($x_0 = 2.5$):**
- $f'(2.5) = 2\cos(2.5) - \frac{2.5}{5} = 2(-0.8011436) - 0.5 = -1.6022872 - 0.5 = -2.1022872$
- $f''(2.5) = -2\sin(2.5) - \frac{1}{5} = -2(0.5984721) - 0.2 = -1.1969443 - 0.2 = -1.3969443$
- $f(2.5) = 2\sin(2.5) - \frac{2.5^2}{10} = 2(0.5984721) - 0.625 = 1.1969443 - 0.625 = 0.5719443$

Now compute the next iterate:

$$
x_1 = 2.5 - \frac{-2.1022872}{-1.3969443} = 2.5 - 1.5049184 = 0.9950816
$$

Notice that the first step is large. It leaps past the answer from $2.5$ down to $0.9951$.

**Iteration 1 ($x_1 = 0.9950816$):**
- $f'(0.9950816) = 2\cos(0.9950816) - \frac{0.9950816}{5} = 2(0.5444342) - 0.1990163 = 1.0888684 - 0.1990163 = +0.8898527$
- $f''(0.9950816) = -2\sin(0.9950816) - 0.2 = -2(0.8388019) - 0.2 = -1.6776038 - 0.2 = -1.8776038$
- $f(0.9950816) = 1.5785880$

$$
x_2 = 0.9950816 - \frac{0.8898527}{-1.8776038} = 0.9950816 - (-0.4739299) = 1.4690108
$$

**Iteration 2 ($x_2 = 1.4690108$):**
- $f'(1.4690108) = 2\cos(1.4690108) - 0.2938022 = -0.0905823$
- $f''(1.4690108) = -2\sin(1.4690108) - 0.2 = -2.1895931$
- $f(1.4690108) = 1.7738494$

$$
x_3 = 1.4690108 - \frac{-0.0905823}{-2.1895931} = 1.4690108 - 0.0413695 = 1.4276423
$$

**Iteration 3 ($x_3 = 1.4276423$):**
- $f'(1.4276423) = -0.0001973$
- $f''(1.4276423) = -2.1795328$
- $f(1.4276423) = 1.7757256$

$$
x_4 = 1.4276423 - \frac{-0.0001973}{-2.1795328} = 1.4275518
$$

**Iteration 4 ($x_4 = 1.4275518$):**
- $f'(1.4275518) = -0.0000000$
- $f(1.4275518) = 1.7757257$

### Full Iteration Summary Table

| Iteration $n$ | $x_n$ | $f'(x_n)$ | $f(x_n)$ |
| --: | --: | --: | --: |
| 0 | 2.5000000000 | $-2.1022872$ | 0.5719443 |
| 1 | 0.9950815513 | $+0.8898527$ | 1.5785880 |
| 2 | 1.4690107528 | $-0.0905823$ | 1.7738494 |
| 3 | 1.4276423210 | $-0.0001973$ | 1.7757256 |
| 4 | 1.4275517793 | $-0.0000000$ | 1.7757257 |
| 5 | 1.4275517788 | $0$ | 1.7757257 |

The sequence stabilizes to 5 decimal places at $x = 1.42755$, where $f(x) = 1.77573$.

### Step 3. Confirm it is a maximum, not a minimum

We evaluate the second derivative at the stationary point $x = 1.42755$:

$$
f''(1.42755) = -2\sin(1.42755) - 0.2 = -1.979516 - 0.2 = -2.179516
$$

Because $f''(1.42755) < 0$ is **negative**, the function is strictly concave downward at this critical point. Therefore, the stationary point is confirmed to be a local maximum.

$$
\boxed{x_{max} = 1.42755, \qquad f(x_{max}) = 1.77573}
$$

---

## 🔍 Tutor Deep Dive: What Happened Behind the Scenes?

> [!NOTE] Why $x_0 = 2.5$ threw the first iterate across the peak
> Look at iteration 1: $x_0 = 2.5$ jumped all the way to $x_1 = 0.9951$, landing well to the left of the true peak at $1.4276$. Why such a wild jump?
>
> At $x_0 = 2.5$, both $f'$ and $f''$ are negative and similar in magnitude ($-2.10$ and $-1.40$). Their ratio $\frac{f'}{f''} \approx 1.5$ creates a very large step:
> $$
> \Delta x = -\frac{-2.10}{-1.40} = -1.50
> $$
> Mathematically, we are applying Newton to $g(x) = f'(x) = 2\cos x - x/5$.
> The second derivative of $g(x)$ is $g''(x) = -2\cos x$.
> - For $x < \pi/2 \approx 1.57$, $g(x)$ is concave.
> - For $x > \pi/2 \approx 1.57$, $g(x)$ is convex.
>
> The starting point $x_0 = 2.5$ sits in the convex region of $g(x)$, where the tangent cuts the axis to the left of the true root. That causes the initial overshoot.
> But starting from iteration 2, the iterate lands in the concave region. From that point on, the sequence converges monotonically and quadratically: the error collapses from $0.0415$ to $9 \times 10^{-5}$ to $5 \times 10^{-10}$!

> [!NOTE] Is this the global maximum over all real numbers?
> Yes! We can verify this with two facts:
> 1. On the interval $(0, \pi)$, $\sin x > 0$, so $f''(x) = -2\sin x - 0.2$ is strictly negative everywhere. This guarantees that $f(x)$ is concave throughout $(0, \pi)$ and can have at most one stationary point there. Since $f'(0) = 2 > 0$ and $f'(\pi) = -2.628 < 0$, it has exactly one stationary point, which is our peak at $x \approx 1.4276$.
> 2. For very large $|x|$, the quadratic term $-x^2/10$ dominates and drives $f(x) \to -\infty$ as $x \to \pm\infty$. The other roots of $f'(x)$ are minima with negative values ($f \approx -4.47$ and $-3.58$). Thus, $1.42755$ is the global maximum over all of $\mathbb{R}$.

---

## ⚡ Quick Review

**The method in one sentence:** Newton's optimization method solves $f'(x) = 0$ by iteratively jumping to the vertex of a local approximating parabola using $x_{n+1} = x_n - \frac{f'(x_n)}{f''(x_n)}$.

**The formula you must memorize:**
$$
x_{n+1} = x_n - \frac{f'(x_n)}{f''(x_n)} \qquad \text{with test } f''(x^*) < 0 \ (\text{maximum})
$$

**The most common exam mistake:** Putting $f'$ in the denominator instead of $f''$, or forgetting to report the sign of the second derivative to confirm whether you found a maximum or a minimum.

**Time estimate in exam:** 8 to 10 minutes for a complete 3-mark numerical problem.

---

## 🔗 Connected Topics

- [← NM-6.1: Optimization Concepts](NM-6.1_Concepts.md): Defines the theoretical boundary between unconstrained and constrained optimization.
- [→ NM-6.3: Optima from Tabulated Data](NM-6.3_Tabulated_Optima.md): Finds optima when you do not have an analytical formula and must work with discrete difference tables.
- [NM-2.4: Newton-Raphson Method](../NM-2_Root_Finding/NM-2.4_Newton_Raphson.md): The root-finding ancestor of Newton optimization.

---

[← Previous: NM-6.1 Concepts](NM-6.1_Concepts.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: NM-6.3 Tabulated Optima →](NM-6.3_Tabulated_Optima.md)
