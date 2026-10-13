---
title: "NM-6.2 · One-Dimensional Unconstrained Optimization"
tags:
  - numerical-methods
  - discrete-mathematics
  - topicwise
---


[🏠 Subtopic Index](00_Index.md) | [← Prev: NM-6.1 Optimization Concepts](NM-6.1_Optimization_Concepts.md) | [Next: NM-6.3 Optima from Tabulated Data →](NM-6.3_Optima_from_Tabulated_Data.md)

---

# NM-6.2 · One-Dimensional Unconstrained Optimization

Every block below is copied from `../answers_explanation/`. The reasoning
is written once, in the year-wise file, and is not restated here.


### [2021 Q.6(b)]

**Question.** Use Newton's method to find the maximum of $f(x) = 2\sin x - \frac{x^2}{10}$ with an initial guess of $x_0 = 2.5$.

*[Marks: 03, CO: 2]*

**Solution.**

**Step 1. Reduce to a root problem.** An interior maximum of a smooth $f$ satisfies
$f'(x) = 0$, so apply Newton to the derivative. Since

$$
f'(x) = 2\cos x - \frac{x}{5}, \qquad f''(x) = -2\sin x - \frac{1}{5}
$$

Newton's iteration for $f'(x) = 0$ is

$$
x_{n+1} = x_n - \frac{f'(x_n)}{f''(x_n)} = x_n - \frac{2\cos x_n - x_n/5}{-2\sin x_n - 1/5}
$$

> [!warning] The denominator is $f''$, not $f'$
> The question says "find the maximum", so the function being solved is $f'$ and
> Newton's denominator is $(f')' = f''$. Using $f'$ in the denominator as well
> gives $x_{n+1} = x_n - 1 = 1.5$ on the first step and then $x_n$ decreases by 1
> forever: a perfectly tidy-looking iteration heading to $-\infty$.
>
> **The safeguard is a dimensional sanity check.** At the maximum the quantity
> being solved, $f'$, must be near zero. A sequence that is not settling towards a
> zero of $f'$ is not converging, however smooth it looks.

**Step 2. Iterate from $x_0 = 2.5$.**

At $x_0 = 2.5$: $f'(2.5) = 2\cos 2.5 - 0.5 = -1.60229 - 0.5 = -2.10229$ and
$f''(2.5) = -2\sin 2.5 - 0.2 = -1.19694 - 0.2 = -1.39694$.

| Iteration | $x_n$ | $f'(x_n)$ | $f(x_n)$ |
| --: | --: | --: | --: |
| 0 | 2.5000000000 | $-2.1022872$ | 0.5719443 |
| 1 | 0.9950815513 | $+0.8898527$ | 1.5785880 |
| 2 | 1.4690107528 | $-0.0905823$ | 1.7738494 |
| 3 | 1.4276423210 | $-0.0001973$ | 1.7757256 |
| 4 | 1.4275517793 | $-0.0000000$ | 1.7757257 |
| 5 | 1.4275517788 | $0$ | 1.7757257 |

Iteration 1: $x_1 = 2.5 - \frac{-2.1022872}{-1.3969443} = 2.5 - 1.5049184 = 0.9950816$.

$$\boxed{x_{max} = 1.42755, \qquad f(x_{max}) = 1.77573}$$

**Step 3. Confirm it is a maximum, not a minimum.**

$f''(1.42755) = -2\sin(1.42755) - 0.2 = -1.979516 - 0.2 = -2.179516$, which is
**negative**, so $f$ is concave there and the stationary point is a maximum.

> [!warning] This check is not optional
> Newton applied to $f' = 0$ finds a critical point of either kind. The
> substitution $f' = 0$ carries no information about which, and this particular
> function has several critical points, two of them minima.
>
> **Rule: whenever you solve for a stationary point, immediately report the sign
> of the second derivative.** One extra evaluation, and it is the difference
> between a maximum and a minimum.

> [!info] Check by two independent routes
> **Bisection on $f'$.** Since $f'(0) = 2 > 0$ and
> $f'(2) = 2\cos 2 - 0.4 = -1.2323 < 0$, bisection on $[0, 2]$ converges to
> $1.4275517788$, with $f = 1.7757256531$. Same value to ten decimals.
>
> **Shape argument.** $f''(x) = -2\sin x - 0.2 < 0$ for every $x \in (0, \pi)$,
> so $f$ is strictly concave on that interval and can have **at most one**
> stationary point there. Since $f'(0) = 2 > 0$ and $f'(\pi) = -2.6283 < 0$, it
> has exactly one, and it is therefore the maximum on $(0, \pi)$.
>
> **Is it the global maximum?** $f'$ has four further roots, near
> $x = -4.2713$, $-1.7462$, $5.2672$ and $7.0689$, with $f = -0.0158$, $-2.2742$,
> $-4.4743$ and $-3.5823$. All are minima or below the maximum, and
> $f(x) \to -\infty$ as $x \to \pm\infty$ because of the $x^2/10$ term. So
> $1.4276$ with $f = 1.7757$ is the global maximum over all of $\mathbb{R}$.

> [!warning] $x_0 = 2.5$ throws the first iterate clean across the root
> The first iterate crosses the root cleanly, jumping from $2.5$ to $0.9951$,
> landing **left** of the answer at $1.4276$, an error of $0.4325$. At
> $x_0 = 2.5$ both $f'$ and $f''$ are negative and of similar size, so the ratio
> $f'/f'' \approx 1.5$ is large, and the first step is correspondingly long.
>
> Convergence still follows, and **the reason is about $g = f'$, not about $f$**.
> Newton is being applied to $g(x) = 2\cos x - \frac{x}{5}$, and the shape that
> governs the step is
> $$g'(x) = -2\sin x - 0.2, \qquad g''(x) = -2\cos x$$
> so $g$ is **concave** for $x < \frac{\pi}{2} = 1.5708$ and **convex** for
> $x > \frac{\pi}{2}$. The start $2.5$ sits in the convex region, where the tangent
> to a convex decreasing curve cuts the axis to the left of the true root. Hence
> the overshoot past $1.4276$.
>
> From iteration 2 onward the iterate is in the concave region, where the tangent
> lies above the curve and the sequence decreases monotonically toward the root
> without crossing it:
> $$1.4690 > 1.4276 > 1.42755 > 1.4275517788$$
> The errors fall $0.4325 \to 0.4739 \to 0.0414 \to 9.05\times10^{-5} \to
> 5\times10^{-10}$, the last ratio being $0.0022$, consistent with the
> $O(e^2)$ signature of Newton.
>
> So $x_0 = 2.5$ is legitimate but uncomfortable. Starting from $0.5$ or from
> $1.5$ converges in fewer steps and never leaves the interval of interest.
>
> **The general lesson.** A first step that overshoots is not a failure, and a
> monotone tail afterwards means it worked. What would be a failure is a
> two-cycle, where the iterate alternates between two values indefinitely.

---

[🏠 Subtopic Index](00_Index.md) | [← Prev: NM-6.1 Optimization Concepts](NM-6.1_Optimization_Concepts.md) | [Next: NM-6.3 Optima from Tabulated Data →](NM-6.3_Optima_from_Tabulated_Data.md)
