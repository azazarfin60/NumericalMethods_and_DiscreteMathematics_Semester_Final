---
title: "NM-6 · Numerical Optimization"
tags:
  - numerical-methods
  - discrete-mathematics
  - topicwise-clusters
---

[🏠 Master Index](00_Index.md) | [← Prev Topic: NM-5 · Numerical Integration](NM-5_Numerical_Integration.md) | [Next Topic: NM-7 · Numerical Differentiation →](NM-7_Numerical_Differentiation.md)

---

# NM-6 · Numerical Optimization

> **Topic ID:** NM-6  
> **Section:** Section A -- Numerical Methods  
> **Exam Weight:** 🟡 Low / Secondary (Tier 3) | 3/8 Years Examined | Typical Weight: 4–7 marks  
> **Subtopics Included:** 3 subtopics (NM-6.1 through NM-6.3)  
> **Origin Layer:** Authored in `../answers_explanation/`. All numerical results and boxed equations match character-for-character.

---

## 📑 Subtopics Covered in this Cluster

| Subtopic ID | Subtopic Title | Priority | Exam Frequency | Section Navigation |
|:---|:---|:---:|:---:|:---|
| **NM-6.1** | Optimization Concepts | 🟡 ⚠️ | 2021 | [Jump to NM-6.1](#nm-61) |
| **NM-6.2** | One-Dimensional Unconstrained Optimization | 🟡 ⚠️ | 2021 | [Jump to NM-6.2](#nm-62) |
| **NM-6.3** | Optima from Tabulated Data | 🟡 | 2018 | [Jump to NM-6.3](#nm-63) |

---

<a id="nm-61"></a><a id="nm-6.1"></a>
## NM-6.1 · Optimization Concepts

### [2021 Q.6(d)]

**Question.** Differentiate between constrained and unconstrained optimization.

*[Marks: 02, CO: 2]*

**Solution.**

**Unconstrained optimization.** No restrictions. Choose $x$ freely in the whole
domain to maximise or minimise $f(x)$.

$$
\text{minimise } f(x_1, x_2, \dots, x_n), \qquad x \in \mathbb{R}^n
$$

Example: fit $y = a + bx$ to data by least squares. Nothing forbids any $a$ or $b$,
hence it is unconstrained.

**Constrained optimization.** Extra conditions must hold. Each restriction is
written as $g(x) \le 0$ or $h(x) = 0$.

$$
\text{minimise } f(x) \quad \text{subject to} \quad g_i(x) \le 0,\ i = 1\dots m, \quad h_j(x) = 0
$$

Example: minimise the weight of a truss subject to every member carrying at most
its rated load, or maximise a portfolio return subject to total risk staying under
a limit.

| | Unconstrained | Constrained |
| :-- | :-- | :-- |
| Restrictions | None | Equality and inequality conditions |
| Stationarity test | $\nabla f = 0$ | KKT multipliers: $\nabla f + \sum \mu_i \nabla g_i + \sum \lambda_j \nabla h_j = 0$ |
| Lagrange multipliers | Not needed | Essential |
| Optimum may be at | An interior point | A point on the boundary |
| Feasible region | Whole space | A subset |
| Harder | Easier | Harder; more constraints mean more cases |

$$\boxed{\text{Unconstrained: choose freely. Constrained: obey rules, solved with multipliers}}$$

> [!warning] The plain gradient test is not merely incomplete here, it is wrong
> In the unconstrained case the optimum satisfies $\nabla f = 0$. In the
> constrained case the optimum frequently sits **on** a boundary where the plain
> gradient test is useless: at a corner the feasible directions are restricted, so
> $f$ can be stationary in a sense that has nothing to do with $\nabla f$.
>
> The KKT conditions replace that with
> $\nabla f + \sum \mu_i \nabla g_i + \sum \lambda_j \nabla h_j = 0$ together with
> **complementary slackness**, $\mu_i \ge 0$ and $\mu_i g_i(x) = 0$. That second
> condition is the part people forget: a multiplier is nonzero only if its
> constraint is active. It is what encodes "the constraint bites exactly when it
> is touching".

---

<a id="nm-62"></a><a id="nm-6.2"></a>
## NM-6.2 · One-Dimensional Unconstrained Optimization

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

<a id="nm-63"></a><a id="nm-6.3"></a>
## NM-6.3 · Optima from Tabulated Data

### [2018 Q.5(b)]

**Question.** From the following table find $x$, correct to two decimal places for which $y$ is maximum and find this value of $y$.

*[Marks: 06]*

**Solution.**

| $x$ | 1.2 | 1.3 | 1.4 | 1.5 | 1.6 |
| :---: | :---: | :---: | :---: | :---: | :---: |
| $y$ | 0.9320 | 0.9636 | 0.9855 | 0.9975 | 0.9996 |

**Step 1, find the direction of the answer before computing anything.** Build
the difference table.

| | 0.9320 | 0.9636 | 0.9855 | 0.9975 | 0.9996 |
| :-- | :-- | :-- | :-- | :-- | :-- |
| $\Delta$ | | $0.0316$ | $0.0219$ | $0.0120$ | $0.0021$ |
| $\Delta^2$ | | | $-0.0097$ | $-0.0099$ | $-0.0099$ |
| $\Delta^3$ | | | | $-0.0002$ | $0.0000$ |
| $\Delta^4$ | | | | | $0.0002$ |

All four first differences are *positive*, so $y$ is still rising at $x = 1.5$.
But the last of them, $0.0021$, is small and the second differences are all
negative, so $y$ is levelling off and the peak lies just *inside* the end of the
table, close to but before $x = 1.6$. If you read that last $0.0021$ as having
"already changed sign" and go looking beyond $1.6$, you will extrapolate
outside the data and get a different answer.

**Step 2, use the backward form, because the maximum is at the far end.** At
$x_4 = 1.6$ with $q = (x - x_4)/h$,

$$\frac{dy}{dx} = \frac{1}{h}\left[\nabla y_4 + \frac{2q + 1}{2}\nabla^2 y_4 + \frac{3q^2 + 6q + 2}{6}\nabla^3 y_4 + \frac{4q^3 + 18q^2 + 22q + 6}{24}\nabla^4 y_4\right]$$

with

$$\nabla y_4 = 0.0021, \qquad \nabla^2 y_4 = -0.0099, \qquad \nabla^3 y_4 = 0.0000, \qquad \nabla^4 y_4 = 0.0002$$

**Step 3, set the derivative to zero.** With $\nabla^3 y_4 = 0$ and
$\nabla^4 y_4$ tiny, the stationary point is set almost entirely by the first
two terms:

$$0.0021 + \frac{2q + 1}{2}(-0.0099) = 0 \implies (q + 0.5)(0.0099) = 0.0021$$

$$q + 0.5 = \frac{0.0021}{0.0099} = 0.212121, \qquad q = -0.287879$$

$$x = x_4 + hq = 1.6 + 0.1(-0.287879) = 1.5712$$

The negative $q$ is the answer to "which side", stated numerically: the maximum
is inside the table.

**Step 4, evaluate $y$ there** with the full five-point backward polynomial,

$$y = y_4 + q\nabla y_4 + \frac{q(q+1)}{2}\nabla^2 y_4 + \frac{q(q+1)(q+2)}{6}\nabla^3 y_4 + \frac{q(q+1)(q+2)(q+3)}{24}\nabla^4 y_4$$

$$y = 0.9996 + (-0.287879)(0.0021) + \frac{(-0.287879)(0.712121)}{2}(-0.0099) + 0 + \frac{(-0.287879)(0.712121)(1.712121)(2.712121)}{24}(0.0002)$$

$$y = 0.9996 - 0.0006045 + 0.0010148 - 0.0000079 = 1.0000023$$

$$\boxed{x = 1.57 \text{ (correct to two decimal places)}, \qquad y_{\max} = 1.0000}$$

> [!note] Why $y_{\max} = 1.0000$ looks odd and is not an error
> The table's largest entry is $0.9996$, and the interpolated maximum comes out
> at $1.0000023$, which is just *above* $1$. That is exactly what a parabola
> through five points should do: the points at $1.5$ and $1.6$ are still rising
> at a decreasing rate, so the fitted curve peaks slightly above the last
> sample. Rounded to four decimals it reads $1.0000$. Do not "correct" it to
> $0.9996$; the tabulated value and the interpolated maximum are different
> quantities.

> [!info] Confirming with a completely separate route
> Fitting one polynomial through all five points by Lagrange interpolation gives
> $y = \dfrac{x^4}{12} - \dfrac{29x^3}{60} + \dfrac{133x^2}{240} +
> \dfrac{409x}{750} + \dfrac{71}{500}$, which reproduces $0.9320$, $0.9636$,
> $0.9855$, $0.9975$, $0.9996$ at $1.2$ through $1.6$ exactly. Differentiating,
> $y' = \dfrac{x^3}{3} - \dfrac{29x^2}{20} + \dfrac{133x}{120} +
> \dfrac{409}{750}$, and $y' = 0$ has three real roots, $x = -0.3344$,
> $x = 1.5713$ and $x = 3.1131$. Only $1.5713$ lies inside $[1.2, 1.6]$, so it
> is the only candidate, and $y$ there is $1.0000023$, matching the
> backward-difference route. The $\Delta^4$ term shifted the stationary point by
> $9.1\times10^{-5}$, which is why the two routes agree to the digits shown.
>
> Confirming it is a *maximum*: $y'' = x^2 - \dfrac{29x}{10} + \dfrac{133}{120}$
> evaluates to $-0.9795$ at $x = 1.5713$, which is negative. And the sign is
> forced by the second difference row, which is negative throughout, so $y$
> must be concave near the peak regardless of the polynomial used.

---

[🏠 Master Index](00_Index.md) | [← Prev Topic: NM-5 · Numerical Integration](NM-5_Numerical_Integration.md) | [Next Topic: NM-7 · Numerical Differentiation →](NM-7_Numerical_Differentiation.md)
