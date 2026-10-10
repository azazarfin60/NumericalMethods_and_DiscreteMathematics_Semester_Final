[← Previous: NM-2.3 False Position](NM-2.3_False_Position_and_Regula_Falsi.md) | [🏠 Index](00_Index.md) | [Next: NM-2.6 Method Comparison →](NM-2.6_Method_Comparison_and_Convergence.md)

---

# NM-2.4: Newton-Raphson Method
> **Section:** A (Numerical Methods) | **Priority:** 🔴⚠️ | **Exam Frequency:** 6/8 years
> **Sources:** Jain Ch.2 §2.5, Topicwise NM-2.4, Fahad Notes §02, Shishir Notes §01

## Why This Topic Matters

This is the most tested method in NM-2 and the one that pays the most marks. It appears in six out of eight papers, in four different question shapes: discuss the limitations and their fixes, discuss merits and demerits, find a root of a transcendental equation, and run three iterations on a power equation. Newton also reappears inside Gauss-Newton, inside Gauss-Seidel's spirit, and inside optimization. Learn the derivation, the four failure modes, and one full numeric example, and you are covered.

---

## 📝 Key Definitions

> **Newton-Raphson formula:** "$x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}$" — Jain, §2.5

> **Geometric meaning:** "the method consists in replacing the part of the curve between the point $[x_0, f(x_0)]$ and the $x$-axis by means of the tangent to the curve at the point." — Jain, §2.5

> **Generalized Newton's formula (multiple roots):** "$x_{n+1} = x_n - p\frac{f(x_n)}{f'(x_n)}$" where $p$ is the multiplicity of the root. — Jain, §2.5

> **Newton-Raphson method:** An open root finder that uses the tangent at the current guess to predict the next one. It converges quadratically near a simple root.

---

## Core Theory

### The Derivation, Step by Step

The exam rewards a full derivation. Here it is, from Taylor's theorem.

**Step 1.** Let $x_0$ be an approximation to a root, and let $x_1 = x_0 + h$ be a better one. Then $f(x_1) = 0$ at convergence.

**Step 2.** Expand $f(x_0 + h)$ by Taylor's series:

$$
f(x_0) + h f'(x_0) + \frac{h^2}{2!} f''(x_0) + \cdots = 0
$$

**Step 3.** Neglect the second and higher-order derivatives. What remains is a linear equation in $h$:

$$
f(x_0) + h f'(x_0) = 0
$$

**Step 4.** Solve for $h$:

$$
h = -\frac{f(x_0)}{f'(x_0)}
$$

**Step 5.** The better approximation is $x_1 = x_0 + h$:

$$
x_1 = x_0 - \frac{f(x_0)}{f'(x_0)}
$$

**Step 6.** Generalise to step $n$:

$$
x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}
$$

That is the Newton-Raphson formula. Notice how little of Taylor's series survived. Newton is a first-order truncation of Taylor's theorem, applied over and over.

### Why the Convergence Is Quadratic

Keep the extra term this time. Taylor about the true root $\xi$ gives:

$$
f(x_n) + (\xi - x_n)f'(x_n) + \frac{1}{2}(\xi - x_n)^2 f''(x_n) + \cdots = 0
$$

Divide by $f'(x_n)$ and rearrange:

$$
-\frac{f(x_n)}{f'(x_n)} = (\xi - x_n) + \frac{1}{2}(\xi - x_n)^2 \frac{f''(x_n)}{f'(x_n)}
$$

The left side is exactly the correction that Newton applies. Substituting into $x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}$:

$$
x_{n+1} - \xi = \frac{1}{2}(x_n - \xi)^2 \frac{f''(x_n)}{f'(x_n)}
$$

Writing $\varepsilon_n = x_n - \xi$:

$$
\varepsilon_{n+1} \approx \frac{1}{2}\varepsilon_n^2 \frac{f''(\xi)}{f'(\xi)}
$$

The error is squared each step. That is **second-order (quadratic) convergence**, and it means the number of correct digits roughly doubles per iteration. Three or four steps usually suffice where bisection needs thirty.

### Geometric Picture

![Newton-Raphson: tangent at point P(x0, y0) intersecting the x-axis at x1](diagrams/nm2_newton_raphson_tangent.jpg)

*Figure 2.3 (Jain, p. 39): the tangent replaces the curve near the guess. Where the tangent crosses the axis is the next iterate $x_1$, visibly closer to the root than $x_0$.*

Read the picture once and it explains everything. A steep tangent gives a short step. A nearly flat tangent gives a huge step and possibly divergence. That intuition is the entire limitations section.

### The Algorithm (2019 Q.2(c))

1. Write the equation as $f(x) = 0$.
2. Compute the derivative $f'(x)$.
3. Choose $x_0$ close to the root, from a sign change or a physical estimate.
4. Apply $x_{k+1} = x_k - \dfrac{f(x_k)}{f'(x_k)}$.
5. Stop when $|x_{k+1} - x_k| < \varepsilon$, or when $|f(x_k)| < \varepsilon$.
6. Verify by substituting the root back into $f(x) = 0$.

Geometrically, $x_{k+1}$ is the intercept on the $x$-axis of the tangent to $y = f(x)$ at $x_k$, so the root is approached along successive tangents.

---

## The Four Limitations and Their Fixes (2017 Q.2(a), 2021 Q.1(b), 2023 Q.1(c))

This is the single most-repeated root-finding question in the whole paper. Learn all four failure modes and all four remedies.

**Limitation 1. Division by a near-zero derivative.** If $f'(x_n) \approx 0$ the tangent is nearly horizontal and the next iterate is thrown far away. The method fails outright at a stationary point of $f$.

*Fix.* Replace Newton-Raphson by the secant method, which uses a finite difference in place of $f'$ and so cannot divide by zero. Alternatively, detect a small $|f'|$ and halt with a diagnostic.

**Limitation 2. Divergence from a poor start.** Away from the root the tangent can intersect the axis well outside the region of interest, and the iteration can move off to infinity or into a cycle rather than toward the root.

*Fix.* Bracket the root first. Find an interval $[a, b]$ with $f(a)f(b) < 0$ by scanning, then use bisection or regula falsi, both of which keep the bracket and cannot diverge.

**Limitation 3. A root of multiplicity greater than one.** At a root where $f(x) = (x-r)^m g(x)$ with $m > 1$, $f'$ also vanishes there. The quadratic term in the error relation collapses, and the iteration degrades to first order, so each step gains little.

*Fix.* Use the modified iteration $x_{n+1} = x_n - m\dfrac{f(x_n)}{f'(x_n)}$, or work with $g(x) = f'(x)/f(x)$, which has only simple roots.

**Limitation 4. Asymptotes and complex excursions.** A root near a vertical asymptote of $f$ or $f'$ sends the iterate to large values. At a complex root of the derivative the iterates can leave the real axis.

*Fix.* Keep a bracket, or hybridise. Run Newton-Raphson but revert to a bracketed step whenever the iterate leaves the bracket. This is the standard practical remedy and it recovers fast convergence near the root with global safety away from it.

> [!NOTE]
> Three of the four failures are the same failure seen from different sides: nothing keeps the iterate near the root. The bracket is the only device that does, which is why every production root finder of consequence, Brent's method among them, is built around one.

### Merits and Demerits (2019 Q.2(c))

**Merits**

1. **Fastest available.** Second-order convergence near the root: the number of correct digits roughly doubles per step, so three or four steps usually suffice where bisection needs thirty.
2. **One estimate is enough.** Only $x_0$ is needed, unlike the secant or regula-falsi methods which require two.
3. **Non-polynomial equations are handled.** Transcendental equations, for instance $x = \cos x$ or $I = I_s(e^{V/V_T}-1)$, are solved directly, with no need to isolate $x$.
4. **Extends to systems.** The same tangent idea applies to $n$ simultaneous equations through the Jacobian, which makes it the standard method for a nonlinear network.

**Demerits**

1. **$f'(x)$ must be available.** An analytic derivative is needed. When it is difficult or costly, the method loses its advantage.
2. **Poor $x_0$ can fail.** If the tangent is nearly horizontal, $f'(x_k) \approx 0$ and the next iterate is thrown far away. Starting far from the root can send the sequence into divergence rather than toward it.
3. **No bracket is maintained.** Unlike bisection, the method gives no guaranteed interval containing the root, so a failure may not be detected until late.
4. **Repeated roots slow it down.** At a root of multiplicity $m > 1$ the convergence order falls from 2 toward 1, and each step gains little.
5. **Complex roots are awkward.** The iterates can leave the real axis when $f$ or $f'$ takes complex values, so real-root isolation must be done beforehand.

> [!WARNING]
> Demerits 3 and 2 have a single fix. Keep a sign-changing bracket $[a, b]$ with $f(a)f(b) < 0$, and take a bisection step whenever a Newton step leaves it. That restores the guarantee of demerit 3 and removes most of the failures of demerit 2, at the cost of one comparison per step. Newton alone is the teaching form; Newton inside a bracket is the engineering form.

---

## Worked Example: $x \sin x + \cos x = 0$

**Problem.** Find the real root of the equation $x \sin x + \cos x = 0$ using the N-R method.

> **Source:** 2018 Q.2(c) [Marks: 04]

**Step 1. The function and its derivative.**

$$
f(x) = x\sin x + \cos x
$$

$$
f'(x) = \frac{d}{dx}(x\sin x) + \frac{d}{dx}(\cos x) = (\sin x + x\cos x) - \sin x = x\cos x
$$

The $\sin x$ terms cancel, which leaves the simple form $f'(x) = x\cos x$.

> [!WARNING]
> This derivative is the whole question. The two $\sin x$ terms cancel and you are left with $x\cos x$. Students who differentiate $x\sin x$ as $\cos x$ get $f'(x) = \cos x - \sin x$ and then wander. Differentiate the whole expression once, do not term-slice it.

**Step 2. Sign check for the starting value.**

| $x$ | $f(x) = x\sin x + \cos x$ |
| :--: | :-- |
| 2.0 | $2(0.90930) + (-0.41615) = 1.40245$ |
| 2.5 | $2.5(0.59847) + (-0.80114) = 0.69504$ |
| 3.0 | $3(0.14112) + (-0.98999) = -0.56663$ |

The sign changes between $2.5$ and $3.0$, so a root lies in that interval. Take $x_0 = 3$.

**Step 3. The iteration.**

$$
x_{n+1} = x_n - \frac{x_n\sin x_n + \cos x_n}{x_n\cos x_n}
$$

| $n$ | $x_n$ | $f(x_n)$ | $f'(x_n) = x_n\cos x_n$ | $x_{n+1}$ |
| :--: | :--: | :--: | :--: | :--: |
| 0 | $3.0000000$ | $-0.56663$ | $-2.96998$ | $2.8092132$ |
| 1 | $2.8092132$ | $-0.02864$ | $-2.65546$ | $2.7984273$ |
| 2 | $2.7984273$ | $-1.087\times10^{-4}$ | $-2.63526$ | $2.7983860$ |

The correction at the last step is $4.1 \times 10^{-5}$, already below $10^{-4}$, so the value is accepted.

$$
\boxed{x = 2.7984}
$$

**Physical reading.** The equation rearranges to $x = -\cot x$, so the root is the first positive point at which the line $y = x$ meets the curve $y = -\cot x$. There is one such point near $2.80$, which is the value found.

> [!NOTE]
> Two things the table alone will not tell you. First, the $f'(x_n)$ column must equal $x_n \cos x_n$ at the $x_n$ printed beside it, and in a printed table that identity is the cheapest way to catch a slip, because the next iterate is $x_n - f(x_n)/f'(x_n)$ and the division only works if the two columns belong to the same $x_n$.
>
> Second, running the same iteration from $x_0 = 2.6$ gives $2.8169812$, then $2.7985064$, then $2.7983861$ and then $2.7983860$. Two starts inside the same bracket landing on the same digits is the evidence that the iteration has found the root rather than a fixed point of its own. Substituting $x = 2.7983860$ back gives $f = -1.2 \times 10^{-7}$, which is zero to the seven digits quoted.

---

## Worked Example: $3I^2 - 4I - 4 = 0$, Three Iterations

**Problem.** An electrical power equation is given as follows: $3I^2 - 4I - 4 = 0$. Calculate 3 iterations of the Newton-Raphson method to obtain the value of current.

> **Source:** 2020 Q.2(b) [Marks: 06]

**Step 1. Set up.**

$$
f(I) = 3I^2 - 4I - 4, \qquad f'(I) = 6I - 4
$$

**Step 2. Choose a starting value.** The paper prints none, so pick one and say so. A current is a positive quantity, and

$$
f(1) = 3 - 4 - 4 = -5 < 0, \qquad f(3) = 27 - 12 - 4 = 11 > 0
$$

Hence a root lies in $(1, 3)$. Take the left end, $I_0 = 1$.

**Step 3. The iteration.**

$$
I_{n+1} = I_n - \frac{f(I_n)}{f'(I_n)} = I_n - \frac{3I_n^2 - 4I_n - 4}{6I_n - 4}
$$

**Step 4. Three iterations.**

At $I_0 = 1$: $f(1) = -5$ and $f'(1) = 2$.

$$
I_1 = 1 - \frac{-5}{2} = 1 + 2.5 = 3.500000
$$

At $I_1 = 3.5$: $f(3.5) = 3(12.25) - 14 - 4 = 36.75 - 18 = 18.75$ and $f'(3.5) = 21 - 4 = 17$.

$$
I_2 = 3.5 - \frac{18.75}{17} = 3.5 - 1.102941 = 2.397059
$$

At $I_2 = 2.397059$: $f = 3(5.745893) - 9.588236 - 4 = 17.237679 - 13.588236 = 3.649443$ and $f' = 14.382354 - 4 = 10.382354$.

$$
I_3 = 2.397059 - \frac{3.649443}{10.382354} = 2.397059 - 0.351504 = 2.045555
$$

| $n$ | $I_n$ | $f(I_n)$ | $f'(I_n)$ |
| --: | --: | --: | --: |
| 0 | 1.000000 | $-5.000000$ | 2.000000 |
| 1 | 3.500000 | 18.750000 | 17.000000 |
| 2 | 2.397059 | 3.649443 | 10.382354 |
| 3 | 2.045555 | 0.370665 | 8.273329 |

$$
\boxed{I_3 = 2.0456 \text{ Amp after three iterations, and the true root is } I = 2 \text{ Amp}}
$$

**Step 5. Check the exact root.** The quadratic formula settles it:

$$
I = \frac{4 \pm \sqrt{16 + 48}}{6} = \frac{4 \pm 8}{6}
$$

which gives $I = 2$ and $I = -\frac{2}{3}$. Only $I = 2$ is a physical current, and $I_3 = 2.045555$ is closing on it.

> [!WARNING]
> Two traps in this question.
>
> **1. The start matters more than the count.** $I_0 = 1$ throws the first iterate to $3.5$, a full $1.5$ past the answer at $2$. The reason is visible in the table: at $I_0 = 1$ the derivative is only $2$ while $f$ is $-5$, so the ratio $f/f'$ is $2.5$ and the first step is long. Starting from $3$, where $f/f' = 0.786$, the first step is short. Three iterations from a good start nearly reaches the root; three from a poor start only gets close.
>
> **2. There are two roots and only one is physical.** Newton's method has no built-in preference, and a careless start can land on $I = -\frac{2}{3}$. The quadratic formula shows both. Discard the negative one on physical grounds, and say that this is why. Starting from $I_0 = 0$ is unsuitable: it gives $f(0) = -4$, $f'(0) = -4$, so $I_1 = 0 - \frac{-4}{-4} = -1$, which walks straight off toward the negative root.

> [!NOTE]
> A different starting value. Starting from $I_0 = 3$, the right end of the same bracket:
>
> | $n$ | $I_n$ | $f(I_n)$ | $f'(I_n)$ |
> | --: | --: | --: | --: |
> | 0 | 3.000000 | 11.000000 | 14.000000 |
> | 1 | 2.214286 | 1.852041 | 9.285714 |
> | 2 | 2.014835 | 0.119342 | 8.089011 |
> | 3 | 2.000082 | 0.000653 | 8.000490 |
>
> Three iterations from $I_0 = 3$ reach $2.000082$, an error of $8.2 \times 10^{-5}$, against $0.0456$ from $I_0 = 1$. Both are correct Newton runs; the start nearer the root simply needs fewer steps. Same root, different arithmetic. The error ratio $0.0456 / 8.2 \times 10^{-5} \approx 556$ over two steps is near $2^{2 \cdot 4}$, which is what quadratic convergence looks like once the iterate is in the basin.

---

## Exam Variants

| Year | Question | Data Given | Key Answer |
|:---|:---|:---|:---|
| 2017 Q.2(a), 2021 Q.1(b), 2023 Q.1(c) | Limitations of N-R and their fixes | none (04 marks) | Four failures, four fixes |
| 2018 Q.2(c) | Find the real root, transcendental | $x \sin x + \cos x = 0$ | $\boxed{x = 2.7984}$ |
| 2019 Q.2(c) | Steps, merits and demerits | none (04 marks) | 6 steps, 4 merits, 5 demerits |
| 2020 Q.2(b) | Three iterations for current | $3I^2 - 4I - 4 = 0$ | $\boxed{I_3 = 2.0456 \text{ Amp after three iterations, and the true root is } I = 2 \text{ Amp}}$ |

---

## 🏆 Golden Questions (Past Exam Archive)

### 🎯 Briefly discuss the limitations of N-R method to find the root of any non-linear equation. How can we solve it?
> **Appeared:** 2017 Q.2(a), 2021 Q.1(b), 2023 Q.1(c) — (04 marks)

**Full Answer:**

The method iterates

$$
x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}
$$

Geometrically it follows the tangent: the tangent at $x_n$ crosses the axis at $x_{n+1}$. The local error satisfies $e_{n+1} \approx \dfrac{f''(r)}{2f'(r)}e_n^2$, which is where the quadratic convergence comes from, and also where all four limitations come from.

**Four distinct failure modes exist.**

1. **Division by a near-zero derivative.** The tangent is nearly horizontal and the next iterate is thrown far away. The method fails outright at a stationary point of $f$.
2. **Divergence from a poor start.** Away from the root the tangent can intersect the axis well outside the region of interest, and the iteration can move off to infinity or into a cycle rather than toward the root.
3. **A root of multiplicity greater than one.** At a root where $f(x) = (x - r)^m g(x)$ with $m > 1$, $f'$ also vanishes there, the quadratic term in the error relation collapses, and the iteration degrades to first order, so each step gains little.
4. **Asymptotes and complex excursions.** A root near a vertical asymptote of $f$ or $f'$ sends the iterate to large values; at a complex root of the derivative the iterates can leave the real axis entirely.

**How each is solved.**

1. **Guard the derivative.** Replace Newton-Raphson by the secant method, which uses a finite difference in place of $f'$ and so cannot divide by zero. Alternatively detect a small $|f'|$ and halt with a diagnostic.
2. **Bracket the root first.** Find an interval $[a, b]$ with $f(a)f(b) < 0$ by scanning, then use bisection or regula falsi, both of which keep the bracket and cannot diverge.
3. **Fix the multiplicity.** Use the modified iteration $x_{n+1} = x_n - m\dfrac{f(x_n)}{f'(x_n)}$, or work with $g(x) = f'(x)/f(x)$, which has only simple roots.
4. **Keep a bracket, or hybridise.** Run Newton-Raphson but revert to a bracketed step whenever the iterate leaves the bracket. This is the standard practical remedy and it recovers fast convergence near the root with global safety away from it.

---

### 🎯 Write the steps of N-R method. Discuss its merits and demerits.
> **Appeared:** 2019 Q.2(c) — (04 marks)

**Full Answer:** The steps, merits and demerits are given in full in the Core Theory section above. For the exam, write the six numbered steps, then the four merits and five demerits, then close with the hybrid remedy:

Geometrically, $x_{k+1}$ is the intercept on the $x$-axis of the tangent to $y = f(x)$ at $x_k$, so the root is approached along successive tangents.

Every merit is a consequence of the quadratic error relation $\varepsilon_{n+1} \approx \frac{1}{2}\varepsilon_n^2 \frac{f''(\xi)}{f'(\xi)}$. Every demerit is a consequence of $f'$ appearing in the denominator or of the absence of a bracket.

---

### 🎯 Find the real root of the equation $x \sin x + \cos x = 0$ using N-R method.
> **Appeared:** 2018 Q.2(c) — (04 marks)

**Full Answer:**

Differentiate first, and do it in one pass:

$$
f'(x) = \frac{d}{dx}(x\sin x) + \frac{d}{dx}(\cos x) = (\sin x + x\cos x) - \sin x = x\cos x
$$

Scan for a sign change to justify the start: $f(2.0) = 1.40245$, $f(2.5) = 0.69504$, $f(3.0) = -0.56663$. The sign flips between $2.5$ and $3.0$, so take $x_0 = 3$.

$$
x_{n+1} = x_n - \frac{x_n\sin x_n + \cos x_n}{x_n\cos x_n}
$$

| $n$ | $x_n$ | $f(x_n)$ | $f'(x_n) = x_n\cos x_n$ | $x_{n+1}$ |
| :--: | :--: | :--: | :--: | :--: |
| 0 | $3.0000000$ | $-0.56663$ | $-2.96998$ | $2.8092132$ |
| 1 | $2.8092132$ | $-0.02864$ | $-2.65546$ | $2.7984273$ |
| 2 | $2.7984273$ | $-1.087\times10^{-4}$ | $-2.63526$ | $2.7983860$ |

The correction at the last step is $4.1 \times 10^{-5}$, below $10^{-4}$, so the value is accepted.

$$
\boxed{x = 2.7984}
$$

The equation rearranges to $x = -\cot x$, so the root is the first positive point at which the line $y = x$ meets the curve $y = -\cot x$. There is one such point near $2.80$, which is the value found.

---

### 🎯 An electrical power equation is given as follows: $3I^2 - 4I - 4 = 0$. Calculate 3 iterations of the Newton-Raphson method to obtain the value of current.
> **Appeared:** 2020 Q.2(b) — (06 marks)

**Full Answer:**

The function, derivative and iteration formula:

$$
f(I) = 3I^2 - 4I - 4, \qquad f'(I) = 6I - 4
$$

$$
I_{n+1} = I_n - \frac{3I_n^2 - 4I_n - 4}{6I_n - 4}
$$

Choose and justify the start. $f(1) = -5 < 0$ and $f(3) = 11 > 0$, so a root lies in $(1, 3)$. Take $I_0 = 1$.

$$
I_1 = 1 - \frac{-5}{2} = 3.500000
$$

$$
I_2 = 3.5 - \frac{18.75}{17} = 3.5 - 1.102941 = 2.397059
$$

$$
I_3 = 2.397059 - \frac{3.649443}{10.382354} = 2.397059 - 0.351504 = 2.045555
$$

| $n$ | $I_n$ | $f(I_n)$ | $f'(I_n)$ |
| --: | --: | --: | --: |
| 0 | 1.000000 | $-5.000000$ | 2.000000 |
| 1 | 3.500000 | 18.750000 | 17.000000 |
| 2 | 2.397059 | 3.649443 | 10.382354 |
| 3 | 2.045555 | 0.370665 | 8.273329 |

$$
\boxed{I_3 = 2.0456 \text{ Amp after three iterations, and the true root is } I = 2 \text{ Amp}}
$$

The exact roots from the quadratic formula are $I = 2$ and $I = -\frac{2}{3}$. Only $I = 2$ is a physical current, so $I_3 = 2.045555$ is closing on the right root. The general safeguard is the same as in the limitations question: keep a bracket, and fall back to bisection whenever a Newton step leaves it.

---

## ⚡ Exam Tips & Common Mistakes

1. **Differentiate once, in a single pass.** The 2018 derivative $f'(x) = x\cos x$ comes out only if you differentiate the whole expression. Term-by-term differentiation of $x\sin x$ as $\cos x$ is the most common error on this paper.
2. **Always justify $x_0$ with a sign check.** One line: $f(2.5) = +0.695$, $f(3.0) = -0.567$, so the start is inside a bracket. It costs nothing and it earns method marks.
3. **Three marks live in the derivative column.** Write it every row. At the root, the printed derivative must equal the true $f'$ at that point. If $x_n$ and $f'(x_n)$ disagree, one of them is wrong.
4. **For a physically framed question, reject a non-physical root and say why.** The current question has a negative root. State that a current is positive, and move on.
5. **If the paper gives no starting value, pick one and write that you picked it.** Do not silently invent it. The justification is worth more than the number.
6. **A long Newton step is not an error.** $I_1 = 3.5$ overshoots the answer and still converges. Trust the table you computed rather than "fixing" it.
7. **Practise the four limitations as a table.** Failure mode on the left, remedy on the right. This question has appeared three times under two different wordings.

## 🔗 Related Topics

- [NM-2.1: Fundamentals & Classification](NM-2.1_Fundamentals_and_Classification.md) — Newton is the open method on the safe-to-fast ladder
- [NM-2.2: Bisection Method](NM-2.2_Bisection_Method.md) — the bracket that rescues Newton when it diverges
- [NM-2.3: False Position & Regula Falsi](NM-2.3_False_Position_and_Regula_Falsi.md) — two points and no derivative
- [NM-2 Lower: Secant Method](NM-2_Lower_Secant_and_Polynomial_Roots.md) — Newton with the derivative replaced by a finite difference
- [NM-2.6: Method Comparison & Convergence](NM-2.6_Method_Comparison_and_Convergence.md) — why order 2 is worth the loss of guarantee

---

[← Previous: NM-2.3 False Position](NM-2.3_False_Position_and_Regula_Falsi.md) | [🏠 Index](00_Index.md) | [Next: NM-2.6 Method Comparison →](NM-2.6_Method_Comparison_and_Convergence.md)
