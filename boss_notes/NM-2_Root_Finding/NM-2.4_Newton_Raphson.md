[← Previous: NM-2.3 False Position](NM-2.3_False_Position.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: NM-2.5 Secant Method →](NM-2.5_Secant_Method.md)

---

# NM-2.4: Newton-Raphson Method

> 🔴 ⚠️ **Priority:** Critical | **Tested:** 6/8 years | **Typical marks:** 4–6

## What This Is (and Why It Matters)

If Bisection is a cautious walker, Newton-Raphson is a jet engine. It is the most celebrated, powerful, and frequently tested root-finding algorithm in numerical analysis.

Instead of needing two endpoints to trap a root inside a bracket, Newton-Raphson needs only a single guess $x_0$. It evaluates the function at that point, calculates the slope of the curve (the tangent), and slides down that tangent to find where it strikes the horizontal axis. That striking point becomes your next guess. Near a root, its error squares on every iteration (quadratic convergence), meaning the number of accurate decimal places roughly doubles with every single step.

Because it appears in almost every single RUET exam paper, you must master its Taylor-series derivation, its proof of quadratic convergence, its four classic failure modes (with fixes!), and how to solve both algebraic and transcendental equations by hand.

---

## 📝 Key Definitions

> **Newton-Raphson formula:** "Successive approximations are given by $x_2, x_3, \dots, x_{n+1}$, where $x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}$, which is the *Newton-Raphson formula*." -- Jain, §2.5 (p. 38)
> 
> **In simple words:** Take your current guess, calculate the ratio of the function height to the curve's slope, and subtract it to get your next, much better guess.

> **Geometric interpretation:** "Geometrically, the method consists in replacing the part of the curve between the point $[x_0, f(x_0)]$ and the $x$-axis by means of the tangent to the curve at the point... so that the root is approached along successive tangents." -- Jain, §2.5 (p. 39)
> 
> **In simple words:** Drawing a tangent line at your current point and following it down to where it hits the ground ($x$-axis) to find your next point.

> **Generalized Newton formula (multiple roots):** "$x_{n+1} = x_n - p\frac{f(x_n)}{f'(x_n)}$, where $p$ is the multiplicity of the root." -- Jain, §2.5 (p. 42)
> 
> **In simple words:** If a root repeats $p$ times (like a double root where $p = 2$), multiply the standard correction step by $p$ to restore full quadratic speed.

> **Quadratic convergence:** A convergence rate where the error at step $n+1$ is proportional to the square of the error at step $n$: $\varepsilon_{n+1} \approx C \varepsilon_n^2$.
> 
> **In simple words:** The error squares on every lap. If your error is $0.01$ ($10^{-2}$), the next error is roughly $0.0001$ ($10^{-4}$), then $10^{-8}$. You double your correct digits each step!

---

## The Core Idea

The geometric heart of Newton-Raphson is the tangent line:

![Newton-Raphson Tangent Representation](../diagrams/nm2_newton_raphson_tangent.jpg)
*Figure 2.4: The tangent at $P(x_0, f(x_0))$ intersects the $x$-axis at $x_1$, which is much closer to the true root $\xi$ than $x_0$.*

### Derivation from Taylor Series (Step-by-Step)

Examiners love asking for this derivation. Here is the formal procedure:

**Step 1. Set up the expansion:**
Let $x_0$ be an approximate guess for the root of $f(x) = 0$. Let $h$ be the exact correction such that $x_1 = x_0 + h$ is the true root:
$$
f(x_0 + h) = 0
$$

**Step 2. Expand using Taylor series:**
Expanding $f(x_0 + h)$ around $x_0$:
$$
f(x_0) + h f'(x_0) + \frac{h^2}{2!} f''(x_0) + \frac{h^3}{3!} f'''(x_0) + \cdots = 0
$$

**Step 3. Truncate higher-order terms:**
Assuming that $h$ is relatively small, terms involving $h^2, h^3, \dots$ are negligible. Dropping the second and higher-order derivatives leaves:
$$
f(x_0) + h f'(x_0) \approx 0
$$

**Step 4. Solve for the step size $h$:**
$$
h f'(x_0) \approx -f(x_0) \implies h \approx -\frac{f(x_0)}{f'(x_0)}
$$

**Step 5. Form the next approximation:**
Substitute $h$ back into $x_1 = x_0 + h$:
$$
x_1 = x_0 - \frac{f(x_0)}{f'(x_0)}
$$

**Step 6. Generalize to the recurrence relation:**
Applying this formula repeatedly yields the celebrated Newton-Raphson formula:
$$
x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}
$$

---

## Proof of Quadratic Convergence

Why is Newton-Raphson so fast? Let's prove that its order of convergence is 2 (quadratic).

Let $\xi$ be the exact root, so $f(\xi) = 0$. Let the error at iteration $n$ be:
$$
\varepsilon_n = x_n - \xi \implies x_n = \xi + \varepsilon_n
$$
Similarly, at step $n+1$:
$$
\varepsilon_{n+1} = x_{n+1} - \xi
$$

Expand $f(x_n)$ and $f'(x_n)$ around the true root $\xi$ using Taylor series:
$$
f(x_n) = f(\xi + \varepsilon_n) = f(\xi) + \varepsilon_n f'(\xi) + \frac{\varepsilon_n^2}{2} f''(\xi) + O(\varepsilon_n^3)
$$
Since $f(\xi) = 0$:
$$
f(x_n) = \varepsilon_n f'(\xi) + \frac{\varepsilon_n^2}{2} f''(\xi) + O(\varepsilon_n^3)
$$
Similarly, for the derivative:
$$
f'(x_n) = f'(\xi + \varepsilon_n) = f'(\xi) + \varepsilon_n f''(\xi) + O(\varepsilon_n^2) = f'(\xi) \left[ 1 + \varepsilon_n \frac{f''(\xi)}{f'(\xi)} \right]
$$

Substitute these into the Newton-Raphson update equation:
$$
x_{n+1} - \xi = x_n - \xi - \frac{f(x_n)}{f'(x_n)}
$$
$$
\varepsilon_{n+1} = \varepsilon_n - \frac{\varepsilon_n f'(\xi) + \frac{1}{2}\varepsilon_n^2 f''(\xi)}{f'(\xi) \left[ 1 + \varepsilon_n \frac{f''(\xi)}{f'(\xi)} \right]}
$$
Factor out $f'(\xi)$ and use the binomial expansion $(1 + u)^{-1} \approx 1 - u$:
$$
\varepsilon_{n+1} = \varepsilon_n - \left( \varepsilon_n + \frac{1}{2}\varepsilon_n^2 \frac{f''(\xi)}{f'(\xi)} \right) \left( 1 - \varepsilon_n \frac{f''(\xi)}{f'(\xi)} \right)
$$
Expanding and keeping terms up to $\varepsilon_n^2$:
$$
\varepsilon_{n+1} = \varepsilon_n - \left[ \varepsilon_n - \varepsilon_n^2 \frac{f''(\xi)}{f'(\xi)} + \frac{1}{2}\varepsilon_n^2 \frac{f''(\xi)}{f'(\xi)} \right] = \varepsilon_n - \varepsilon_n + \frac{1}{2}\varepsilon_n^2 \frac{f''(\xi)}{f'(\xi)}
$$
$$
\varepsilon_{n+1} \approx \frac{1}{2} \left[ \frac{f''(\xi)}{f'(\xi)} \right] \varepsilon_n^2
$$

Since $\varepsilon_{n+1} \propto \varepsilon_n^2$, Newton-Raphson has **second-order (quadratic) convergence**!

---

## The Four Limitations and Their Fixes

This question has appeared repeatedly in RUET semester finals (2017 Q.2(a), 2021 Q.1(b), 2023 Q.1(c)). Learn all four failure modes and their standard remedies:

| Limitation / Failure Mode | Why It Happens | Standard Fix / Solution |
| :-- | :-- | :-- |
| **1. Division by zero / flat tangent** | If $f'(x_n) \approx 0$ (near an extremum or stationary point), the denominator vanishes and the tangent shoots off horizontally, throwing $x_{n+1}$ to infinity. | Switch to the **Secant method** (which uses a finite difference instead of $f'$), or add a check: if $|f'(x_n)| < \delta$, perturb the guess slightly. |
| **2. Divergence from poor starting guess** | If initial guess $x_0$ is far from the root, the tangent can intersect outside the basin of attraction, causing iterations to diverge to infinity or bounce into a limit cycle. | **Pre-bracket the root:** Perform an initial sign scan ($f(a)f(b) < 0$) and use a few steps of Bisection to place $x_0$ sufficiently close to the root before switching to Newton. |
| **3. Slowdown at multiple roots** | If the root has multiplicity $m > 1$ (e.g. $f(x) = (x - r)^2$), then $f'(\xi) = 0$ as well. The quadratic term collapses and convergence degrades to slow linear speed ($p = 1$). | Use the **Modified Newton formula**: $x_{n+1} = x_n - m \frac{f(x_n)}{f'(x_n)}$, or define an auxiliary function $u(x) = \frac{f(x)}{f'(x)}$ which converts multiple roots into simple roots. |
| **4. Inflection point oscillations & complex roots** | If $x_0$ is near an inflection point ($f''(x) = 0$), the tangents can bounce back and forth in an endless two-cycle ($x_0 \to x_1 \to x_0$). Also, complex roots cannot be found if started on the real line. | **Damped Newton step:** Introduce a damping factor $\alpha \in (0, 1]$ such that $x_{n+1} = x_n - \alpha \frac{f(x_n)}{f'(x_n)}$, or enforce a bracketing guard. |

---

## Merits and Demerits (2019 Q.2(c))

### Merits
1. **Unrivaled speed:** Quadratic convergence ($p = 2$) near simple roots; correct decimal digits double on every step.
2. **Minimal starting data:** Needs only a single initial guess $x_0$, unlike bracketing methods that require two sign-changing bounds.
3. **Solves transcendental equations:** Handles sines, cosines, and exponentials directly without needing algebraic inversion.
4. **Generalizes to systems:** Easily extends to solve nonlinear systems of $n$ simultaneous equations using the Jacobian matrix.

### Demerits
1. **Requires analytical derivative:** You must compute $f'(x)$. If $f(x)$ is complicated or given as discrete experimental data, Newton-Raphson cannot be applied directly.
2. **Expensive per step:** Requires two function evaluations per iteration ($f(x_n)$ and $f'(x_n)$).
3. **No safety guarantee:** If the initial guess is outside the convergence basin, it can diverge or cycle endlessly.
4. **Fails at stationary points:** Blows up whenever $f'(x_n) = 0$.

---

## 🔧 Worked Example 1: Transcendental Equation

> **Question:** Find the real root of the equation $x \sin x + \cos x = 0$ using the Newton-Raphson method.
> 
> *(Source: 2018 Q.2(c) [Marks: 04])*

**Let's solve this step by step.**

**Step 1. Formulate the function and derivative:**
$$
f(x) = x \sin x + \cos x
$$
Differentiate carefully using the product rule:
$$
f'(x) = \frac{d}{dx}(x \sin x) + \frac{d}{dx}(\cos x) = (\sin x + x \cos x) - \sin x = x \cos x
$$
Notice the beauty here: $\sin x$ cancels out completely!
$$
f'(x) = x \cos x
$$

> [!WARNING] The Product Rule Trap
> Students often make the mistake of differentiating $x \sin x$ as simply $\cos x$. You must apply the full product rule: $\frac{d}{dx}(x \sin x) = 1 \cdot \sin x + x \cos x$.

**Step 2. Locate a starting guess with a sign check:**
Let's test values in radians:
- $f(2.0) = 2.0 \sin(2.0) + \cos(2.0) = 2.0(0.909297) - 0.416147 = +1.40245$
- $f(2.5) = 2.5 \sin(2.5) + \cos(2.5) = 2.5(0.598472) - 0.801144 = +0.69504$
- $f(3.0) = 3.0 \sin(3.0) + \cos(3.0) = 3.0(0.141120) - 0.989992 = -0.56663$

The sign flips between $2.5$ and $3.0$. Choose $x_0 = 3.0$.

**Step 3. Set up the Newton-Raphson iteration formula:**
$$
x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)} = x_n - \frac{x_n \sin x_n + \cos x_n}{x_n \cos x_n}
$$

**Step 4. Run the iterations:**
- **At $x_0 = 3.0$:**
  $f(3.0) = -0.566632$
  $f'(3.0) = 3.0 \cos(3.0) = 3.0(-0.989992) = -2.969977$
$$
x_1 = 3.0 - \frac{-0.566632}{-2.969977} = 3.0 - 0.190787 = 2.809213
$$

- **At $x_1 = 2.809213$:**
  $f(x_1) = 2.809213 \sin(2.809213) + \cos(2.809213) \approx -0.028643$
  $f'(x_1) = 2.809213 \cos(2.809213) \approx -2.655458$
$$
x_2 = 2.809213 - \frac{-0.028643}{-2.655458} = 2.809213 - 0.010786 = 2.798427
$$

- **At $x_2 = 2.798427$:**
  $f(x_2) \approx -0.0001087$
  $f'(x_2) \approx -2.635261$
$$
x_3 = 2.798427 - \frac{-0.0001087}{-2.635261} = 2.798427 - 0.000041 = 2.798386
$$

**Summary iteration table:**

| $n$ | $x_n$ | $f(x_n)$ | $f'(x_n)$ | $x_{n+1}$ |
| :--: | :--: | :--: | :--: | :--: |
| 0 | 3.000000 | $-0.56663$ | $-2.96998$ | 2.809213 |
| 1 | 2.809213 | $-0.02864$ | $-2.65546$ | 2.798427 |
| 2 | 2.798427 | $-1.087 \times 10^{-4}$ | $-2.63526$ | 2.798386 |

The change between $x_2$ and $x_3$ is only $0.000041 < 10^{-4}$. Rounding to four decimal places gives:

$$
\boxed{x = 2.7984}
$$

---

## 🔧 Worked Example 2: Electrical Power Equation

> **Question:** An electrical power equation is given as follows: $3I^2 - 4I - 4 = 0$. Calculate 3 iterations of the Newton-Raphson method to obtain the value of current.
> 
> *(Source: 2020 Q.2(b) [Marks: 06])*

**Let's solve this step by step.**

**Step 1. Formulate function and derivative:**
$$
f(I) = 3I^2 - 4I - 4, \qquad f'(I) = 6I - 4
$$

**Step 2. Algebraic sanity check:**
Using the quadratic formula:
$$
I = \frac{-(-4) \pm \sqrt{(-4)^2 - 4(3)(-4)}}{2(3)} = \frac{4 \pm \sqrt{16 + 48}}{6} = \frac{4 \pm 8}{6}
$$
This gives $I = 2\text{ A}$ and $I = -\frac{2}{3}\text{ A}$. Since electric current in a physical power circuit must be positive, the true physical root is $I = 2\text{ A}$.

**Step 3. Select starting value:**
Testing positive values:
- $f(1) = 3(1)^2 - 4(1) - 4 = -5 < 0$
- $f(3) = 3(3)^2 - 4(3) - 4 = 27 - 12 - 4 = +11 > 0$
A root lies in $(1, 3)$. Let's start at $I_0 = 1\text{ A}$.

**Step 4. Perform the 3 iterations:**

- **Iteration 1:**
  $f(I_0) = f(1) = -5$
  $f'(I_0) = f'(1) = 6(1) - 4 = 2$
$$
I_1 = 1 - \frac{-5}{2} = 1 + 2.5 = 3.500000\text{ A}
$$

- **Iteration 2:**
  $f(3.5) = 3(3.5)^2 - 4(3.5) - 4 = 36.75 - 14 - 4 = 18.75$
  $f'(3.5) = 6(3.5) - 4 = 21 - 4 = 17$
$$
I_2 = 3.5 - \frac{18.75}{17} = 3.5 - 1.102941 = 2.397059\text{ A}
$$

- **Iteration 3:**
  $f(2.397059) = 3(2.397059)^2 - 4(2.397059) - 4 = 17.237679 - 9.588236 - 4 = 3.649443$
  $f'(2.397059) = 6(2.397059) - 4 = 14.382354 - 4 = 10.382354$
$$
I_3 = 2.397059 - \frac{3.649443}{10.382354} = 2.397059 - 0.351504 = 2.045555\text{ A}
$$

**Summary table:**

| $n$ | $I_n$ | $f(I_n)$ | $f'(I_n)$ | $I_{n+1}$ |
| :--: | :--: | :--: | :--: | :--: |
| 0 | 1.000000 | $-5.000000$ | 2.000000 | 3.500000 |
| 1 | 3.500000 | 18.750000 | 17.000000 | 2.397059 |
| 2 | 2.397059 | 3.649443 | 10.382354 | 2.045555 |

Rounding to four decimal places gives:

$$
\boxed{I_3 = 2.0456 \text{ Amp after three iterations, and the true root is } I = 2 \text{ Amp}}
$$

---

## 🏆 Past Exam Questions

### 2017 Q.2(a), 2021 Q.1(b), 2023 Q.1(c): Briefly discuss the limitations of N-R method to find the root of any non-linear equation. How can we solve it? [04 marks]

**How to answer like a top student:**
Organize your response into four clearly defined failure modes paired directly with their practical engineering solutions.

**Solution:**

The Newton-Raphson update formula is:
$$
x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}
$$
Its quadratic error behavior $\varepsilon_{n+1} \approx \frac{1}{2} \left[\frac{f''(\xi)}{f'(\xi)}\right] \varepsilon_n^2$ reveals why and where the method breaks down.

**Four Limitations and Their Solutions:**

1. **Stationary points / vanishing derivative ($f'(x) \approx 0$):**
   - *Problem:* If an iterate lands near a local maximum, minimum, or plateau where $f'(x_n) \approx 0$, the denominator vanishes. The tangent is nearly horizontal, sending the next iterate off to a massive value or causing division-by-zero errors.
   - *Remedy:* Replace the analytical derivative with a finite-difference approximation using the **Secant method**, or implement a numerical check that perturbs $x_n$ slightly if $|f'(x_n)| < 10^{-6}$.

2. **Divergence from remote initial guesses:**
   - *Problem:* Newton-Raphson guarantees convergence only locally (when $x_0$ is already close to the root). If $x_0$ is chosen poorly, the iterations can diverge to infinity or bounce aimlessly across multiple valleys.
   - *Remedy:* **Hybridize with Bisection:** Scan the domain for a sign change ($f(a)f(b) < 0$) and apply a few iterations of Bisection to shrink the bracket. Once safely inside the basin of attraction, release Newton-Raphson for rapid quadratic convergence.

3. **Multiple roots ($m > 1$):**
   - *Problem:* If the root has multiplicity $m \ge 2$, both $f(x)$ and $f'(x)$ approach zero simultaneously. The convergence order drops from quadratic ($p = 2$) to slow linear ($p = 1$).
   - *Remedy:* Use the modified Newton formula $x_{n+1} = x_n - m \frac{f(x_n)}{f'(x_n)}$, or transform the problem using $u(x) = \frac{f(x)}{f'(x)}$, which has only simple roots.

4. **Oscillation around inflection points:**
   - *Problem:* Near an inflection point where $f''(x) = 0$, the tangents can overshoot repeatedly, trapping the iterates in an infinite two-point oscillation loop ($x_0 \to x_1 \to x_0$).
   - *Remedy:* Use a **damped Newton method** with a step relaxation factor $\alpha \in (0, 1]$: $x_{n+1} = x_n - \alpha \frac{f(x_n)}{f'(x_n)}$, or enforce strict interval bounds.

---

### 2019 Q.2(c): Write the steps of N-R method. Discuss its merits and demerits. [04 marks]

**How to answer like a top student:**
Write the 6 algorithmic steps concisely, followed by distinct bullet points for merits and demerits.

**Solution:**

**Steps of Newton-Raphson Method:**
1. Express the problem in standard form $f(x) = 0$.
2. Compute the first derivative analytically: $f'(x) = \frac{df}{dx}$.
3. Choose an initial estimate $x_0$ close to the suspected root.
4. Compute the next approximation using the formula:
$$
x_{k+1} = x_k - \frac{f(x_k)}{f'(x_k)}
$$
5. Check convergence: if $|x_{k+1} - x_k| < \varepsilon$ or $|f(x_{k+1})| < \varepsilon$, accept $x_{k+1}$ as the root and stop.
6. Verify the final result by substituting the accepted root back into $f(x) = 0$.

**Merits:**
- Fastest root-finding algorithm: quadratic convergence ($p = 2$) near simple roots.
- Requires only one starting guess $x_0$.
- Directly solves complex transcendental equations.
- Readily generalizes to systems of nonlinear equations using the Jacobian.

**Demerits:**
- Requires analytical evaluation of $f'(x)$, which may be tedious or impossible for sampled data.
- Two function evaluations required per step ($f$ and $f'$).
- Can diverge or fail if the initial guess is far from the root or near $f'(x) = 0$.
- Slows down to linear convergence for multiple roots.

---

### Exam Variants at a Glance

| Year | What They Asked | Key Answer / Formula |
|:---|:---|:---|
| 2017 Q.2(a), 2021 Q.1(b), 2023 Q.1(c) | Four limitations of N-R and how to solve them (04 marks) | Flat tangents, divergence, multiple roots, oscillation; hybrid bracket |
| 2018 Q.2(c) | Find root of $x \sin x + \cos x = 0$ (04 marks) | $\boxed{x = 2.7984}$ |
| 2019 Q.2(c) | Steps, merits, and demerits of N-R (04 marks) | 6 steps, quadratic speed vs. derivative requirement |
| 2020 Q.2(b) | Calculate 3 iterations for $3I^2 - 4I - 4 = 0$ (06 marks) | $\boxed{I_3 = 2.0456 \text{ Amp after three iterations, and the true root is } I = 2 \text{ Amp}}$ |

---

## ⚡ Quick Review

**The method in one sentence:** Newton-Raphson draws a tangent line at the current guess and slides down to its horizontal axis intercept to get the next guess with quadratic speed.

**The formula you must memorize:**
$$
x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}
$$

**The most common exam mistake:** Forgetting to differentiate using the product rule on expressions like $x \sin x$, or failing to reject non-physical negative roots in circuit problems.

**Time estimate in exam:** 8 minutes for theory / limitations; 10–12 minutes for a full 3-iteration numerical problem.

---

## 🔗 Connected Topics

- [← NM-2.3: False Position and Regula Falsi](NM-2.3_False_Position.md) -- replaces the tangent slope with a chord across two bracketing endpoints.
- [→ NM-2.5: Secant Method](NM-2.5_Secant_Method.md) -- keeps Newton's speed when calculating $f'(x)$ analytically is impossible.
- [NM-2.6: Method Comparison and Convergence](NM-2.6_Method_Comparison.md) -- why order 2 is worth the risk of divergence.
- [NM-2.7: Polynomial Roots](NM-2.7_Polynomial_Roots.md) -- applying Newton-Raphson to solve higher-order polynomials and circuit power balances.

---

[← Previous: NM-2.3 False Position](NM-2.3_False_Position.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: NM-2.5 Secant Method →](NM-2.5_Secant_Method.md)
