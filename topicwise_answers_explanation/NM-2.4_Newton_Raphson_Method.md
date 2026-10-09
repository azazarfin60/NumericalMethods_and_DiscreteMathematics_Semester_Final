---
title: "NM-2.4 · Newton-Raphson Method"
tags:
  - numerical-methods
  - discrete-mathematics
  - topicwise
---

# NM-2.4 · Newton-Raphson Method

Every block below is copied from `../answers_explanation/`. The reasoning
is written once, in the year-wise file, and is not restated here.


### [2017 Q.2(a), 2021 Q.1(b), 2023 Q.1(c)]

**Appeared in:** 2017 Q.2(a), 2021 Q.1(b), 2023 Q.1(c)

**Question.** Briefly discuss the limitations of N-R method to find the root of any non-linear equation. How can we solve it?

*[Marks: 04]*

**Solution.**

**The method.** Newton-Raphson iterates

$$x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}$$

Geometrically it follows the tangent: the tangent at $x_n$ crosses the axis at
$x_{n+1}$. The local error satisfies $e_{n+1} \approx \dfrac{f''(r)}{2f'(r)}e_n^2$,
which is where the famous quadratic convergence comes from, and also where all
four limitations come from.

**Four distinct failure modes.**

1. **Division by a near-zero derivative.** The tangent is nearly horizontal and
   the next iterate is thrown far away. The method fails outright at a
   stationary point of $f$.
2. **Divergence from a poor start.** Away from the root the tangent can
   intersect the axis well outside the region of interest, and the iteration can
   move off to infinity or into a cycle rather than toward the root.
3. **A root of multiplicity greater than one.** At a root where
   $f(x) = (x-r)^m g(x)$ with $m > 1$, $f'$ also vanishes there, the quadratic
   term in the error relation collapses, and the iteration degrades to first
   order, so each step gains little.
4. **Asymptotes and complex excursions.** A root near a vertical asymptote of
   $f$ or $f'$ sends the iterate to large values; at a complex root of the
   derivative the iterates can leave the real axis entirely.

**How each is solved.**

1. **Guard the derivative.** Replace Newton-Raphson by the secant method, which
   uses a finite difference in place of $f'$ and so cannot divide by zero.
   Alternatively detect a small $\lvert f'\rvert$ and halt with a diagnostic.
2. **Bracket the root first.** Find an interval $[a,b]$ with $f(a)f(b) < 0$ by
   scanning, then use bisection or regula falsi, both of which keep the bracket
   and cannot diverge.
3. **Fix the multiplicity.** Use the modified iteration
   $x_{n+1} = x_n - m\dfrac{f(x_n)}{f'(x_n)}$, or work with
   $g(x) = f'(x)/f(x)$, which has only simple roots.
4. **Keep a bracket, or hybridise.** Run Newton-Raphson but revert to a
   bracketed step whenever the iterate leaves the bracket. This is the standard
   practical remedy and it recovers fast convergence near the root with global
   safety away from it.

> [!note] The unifying idea
> Three of the four failures are the same failure seen from different sides:
> nothing keeps the iterate near the root. The bracket is the only device that
> does, which is why every production root finder of consequence, Brent's method
> among them, is built around one.

---

### [2018 Q.2(c)]

**Question.** Find the real root of the equation $x \sin x + \cos x = 0$ using N-R method.

*[Marks: 04]*

**Solution.**

**Write the function and differentiate it, carefully.**

$$f(x) = x\sin x + \cos x$$

$$f'(x) = \frac{d}{dx}(x\sin x) + \frac{d}{dx}(\cos x) = (\sin x + x\cos x) - \sin x = x\cos x$$

> [!warning] This derivative is the whole question
> The two $\sin x$ terms cancel and you are left with $x\cos x$. Students who
> differentiate $x\sin x$ as $\cos x$ get $f'(x) = \cos x - \sin x$ and then
> wander. Differentiate the whole expression once, do not term-slice it.

**Choose a starting value, and justify it by a sign check.**

| $x$ | $f(x) = x\sin x + \cos x$ |
| :--: | :-- |
| 2.0 | $2(0.90930) + (-0.41615) = 1.40245$ |
| 2.5 | $2.5(0.59847) + (-0.80114) = 0.69504$ |
| 3.0 | $3(0.14112) + (-0.98999) = -0.56663$ |

$f$ changes sign between $2.5$ and $3.0$, so a root lies there. Take $x_0 = 3$.

**Iterate.**

$$x_{n+1} = x_n - \frac{x_n\sin x_n + \cos x_n}{x_n\cos x_n}$$

| $n$ | $x_n$ | $f(x_n)$ | $f'(x_n) = x_n\cos x_n$ | $x_{n+1}$ |
| :--: | :--: | :-- | :-- | :-- |
| 0 | $3.0000000$ | $-0.56663$ | $-2.96998$ | $2.8092132$ |
| 1 | $2.8092132$ | $-0.02864$ | $-2.65546$ | $2.7984273$ |
| 2 | $2.7984273$ | $-1.087\times10^{-4}$ | $-2.63526$ | $2.7983860$ |

The correction at the last step is $4.1\times10^{-5}$, already below $10^{-4}$,
so the value is accepted.

$$\boxed{x = 2.7984}$$

**What the root means.** The equation rearranges to $x = -\cot x$, so the root
is where the line $y = x$ meets the curve $y = -\cot x$. There is one such
crossing near $2.80$, and that is the value found.

> [!info] Two things the iteration table alone will not tell you
> First, the table is not self-validating. The $f'(x_n)$ column must equal
> $x_n\cos x_n$ at the $x_n$ printed beside it, and in a printed table that
> identity is the cheapest way to catch a slip, because the next iterate is
> $x_n - f(x_n)/f'(x_n)$ and the division only works if the two columns belong
> to the same $x_n$.
>
> Second, convergence to a fixed point of the iteration is not the same as
> finding the root, unless the starting point is inside a basin that collapses
> to it. Running the same iteration from $x_0 = 2.6$ gives $2.8169812$, then
> $2.7985064$, then $2.7983861$ and then $2.7983860$. Two starts inside the
> same bracket landing on the same digits is the evidence that the iteration has
> found the root rather than a fixed point of its own.

---

### [2019 Q.2(c)]

**Question.** Write the steps of N-R method. Discuss its merits and demerits.

*[Marks: 04]*

**Solution.**

**Newton-Raphson for $f(x) = 0$.**

1. Write the equation as $f(x) = 0$.
2. Compute the derivative $f'(x)$.
3. Choose $x_0$ close to the root, from a sign change or a physical estimate.
4. Apply $x_{k+1} = x_k - \dfrac{f(x_k)}{f'(x_k)}$.
5. Stop when $|x_{k+1} - x_k| < \varepsilon$, or when $|f(x_k)| < \varepsilon$.
6. Verify by substituting the root back into $f(x) = 0$.

Geometrically, $x_{k+1}$ is the intercept on the $x$-axis of the tangent to
$y = f(x)$ at $x_k$, so the root is approached along successive tangents.

**Merits**

1. **Fastest available.** Second-order convergence near the root: the number of
   correct digits roughly doubles per step, so three or four steps usually suffice
   where bisection needs thirty.
2. **One estimate is enough.** Only $x_0$ is needed, unlike the secant or
   regula-falsi methods which require two.
3. **Non-polynomial equations are handled.** Transcendental equations, for instance
   $x = \cos x$ or $I = I_s(e^{V/V_T}-1)$, are solved directly, with no need to
   isolate $x$.
4. **Extends to systems.** The same tangent idea applies to $n$ simultaneous
   equations through the Jacobian, which makes it the standard method for a
   nonlinear network.

**Demerits**

1. **$f'(x)$ must be available.** An analytic derivative is needed. When it is
   difficult or costly, the method loses its advantage.
2. **Poor $x_0$ can fail.** If the tangent is nearly horizontal, $f'(x_k) \approx 0$
   and the next iterate is thrown far away. Starting far from the root can send the
   sequence into divergence rather than toward it.
3. **No bracket is maintained.** Unlike bisection, the method gives no guaranteed
   interval containing the root, so a failure may not be detected until late.
4. **Repeated roots slow it down.** At a root of multiplicity $m > 1$ the
   convergence order falls from 2 toward 1, and each step gains little.
5. **Complex roots are awkward.** The iterates can leave the real axis when $f$ or
   $f'$ takes complex values, so real-root isolation must be done beforehand.

> [!warning] Demerits 3 and 2 have a single fix
> Keep a sign-changing bracket $[a, b]$ with $f(a)f(b) < 0$, and take a bisection
> step whenever a Newton step leaves it. That restores the guarantee of demerit 3
> and removes most of the failures of demerit 2, at the cost of a comparison per
> step.
>
> This hybrid is what production root finders actually do. Newton alone is the
> teaching form; Newton inside a bracket is the engineering form.

---

### [2020 Q.2(b)]

**Question.** An electrical power equation is given as follows: $3I^2 - 4I - 4 = 0$. Calculate 3 iterations of the Newton-Raphson method to obtain the value of current.

*[Marks: 06]*

**Solution.**

**Step 1. Set up.**

$$
f(I) = 3I^2 - 4I - 4, \qquad f'(I) = 6I - 4
$$

**Step 2. Choose a starting value.** The paper prints none, so pick one and say
so. A current is a positive quantity, and

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

At $I_1 = 3.5$: $f(3.5) = 3(12.25) - 14 - 4 = 36.75 - 18 = 18.75$ and
$f'(3.5) = 21 - 4 = 17$.

$$
I_2 = 3.5 - \frac{18.75}{17} = 3.5 - 1.102941 = 2.397059
$$

At $I_2 = 2.397059$: $f = 3(5.745893) - 9.588236 - 4 = 17.237679 - 13.588236 = 3.649443$
and $f' = 14.382354 - 4 = 10.382354$.

$$
I_3 = 2.397059 - \frac{3.649443}{10.382354} = 2.397059 - 0.351504 = 2.045555
$$

| $n$ | $I_n$ | $f(I_n)$ | $f'(I_n)$ |
| --: | --: | --: | --: |
| 0 | 1.000000 | $-5.000000$ | 2.000000 |
| 1 | 3.500000 | 18.750000 | 17.000000 |
| 2 | 2.397059 | 3.649443 | 10.382354 |
| 3 | 2.045555 | 0.370665 | 8.273329 |

$$\boxed{I_3 = 2.0456 \text{ Amp after three iterations, and the true root is } I = 2 \text{ Amp}}$$

**Step 5. Check the exact root.** The quadratic formula settles it:

$$
I = \frac{4 \pm \sqrt{16 + 48}}{6} = \frac{4 \pm 8}{6}
$$

which gives $I = 2$ and $I = -\frac{2}{3}$. Only $I = 2$ is a physical current,
and $I_3 = 2.045555$ is closing on it.

> [!warning] Two traps in this question
> **1. The start matters more than the count.** $I_0 = 1$ throws the first iterate
> to $3.5$, a full $1.5$ past the answer at $2$. The reason is visible in the
> table: at $I_0 = 1$ the derivative is only $2$ while $f$ is $-5$, so the ratio
> $f/f'$ is $2.5$ and the first step is long.
>
> **2. There are two roots and only one is physical.** Newton's method has no
> built-in preference, and a careless start can land on $I = -\tfrac{2}{3}$. The
> quadratic formula shows both. Discard the negative one on physical grounds, and
> say that this is why. Starting from $I_0 = 0$ is unsuitable: it gives
> $f(0) = -4$, $f'(0) = -4$, so $I_1 = 0 - \frac{-4}{-4} = -1$, which walks
> straight off toward the negative root.

> [!info] Check by two independent routes
> **Closed form.** $I = 2$ and $I = -\tfrac{2}{3}$, from the quadratic formula.
> Substituting back: $3(2)^2 - 4(2) - 4 = 12 - 8 - 4 = 0$ exactly.
>
> **A different starting value.** Starting from $I_0 = 3$, which is the right end
> of the same bracket:
>
> | $n$ | $I_n$ | $f(I_n)$ | $f'(I_n)$ |
> | --: | --: | --: | --: |
> | 0 | 3.000000 | 11.000000 | 14.000000 |
> | 1 | 2.214286 | 1.852041 | 9.285714 |
> | 2 | 2.014835 | 0.119342 | 8.089011 |
> | 3 | 2.000082 | 0.000653 | 8.000490 |
>
> Three iterations from $I_0 = 3$ reach $2.000082$, an error of $8.2 \times 10^{-5}$,
> against $0.0456$ from $I_0 = 1$. Both are correct Newton runs; the start nearer
> the root simply needs fewer steps. **Same root, different arithmetic.**
>
> Note that the error ratio $0.0456 / 8.2\times10^{-5} \approx 556$ over two steps is
> near $2^{2\cdot 4}$, which is what quadratic convergence looks like once the
> iterate is in the basin.

---
