---
title: "NM-2.1 · Fundamentals & Classification"
tags:
  - numerical-methods
  - discrete-mathematics
  - topicwise
---

# NM-2.1 · Fundamentals & Classification

Every block below is copied from `../answers_explanation/`. The reasoning
is written once, in the year-wise file, and is not restated here.


### [2019 Q.2(a)]

**Question.** What is meant by iterative method? Write the names of iterative methods to solve nonlinear equations. Write the generalized steps to solve the nonlinear equations using iterative methods.

*[Marks: 04]*

**Solution.**

An **iterative method** solves $f(x) = 0$ by producing a sequence
$x_0, x_1, x_2, \ldots$ from a starting estimate $x_0$, each term obtained from the
preceding ones by a fixed rule, so that the sequence converges to the root
$x = r$. The answer is accepted when successive terms agree to the required
precision, rather than when a formula closes.

**Methods for a nonlinear equation**

1. Bisection (or false position, regula falsi)
2. Fixed-point iteration
3. Newton-Raphson
4. Secant
5. Bairstow (for polynomial roots)

**Generalized steps**

1. Rewrite the problem in the form $f(x) = 0$.
2. Determine the interval of interest, and count the roots in it from a change of
   sign of $f$.
3. Choose a starting estimate $x_0$ and, where required, a second estimate.
4. Derive the iteration formula $x_{k+1} = g(x_k)$.
5. Apply the formula repeatedly, recording each iterate.
6. Test for convergence by comparing successive iterates,
   $|x_{k+1} - x_k| < \varepsilon$, with $\varepsilon$ the tolerance.
7. If the sequence diverges or stalls, restart from a better estimate or from
   another method, and note the failure.
8. Verify the accepted root by substitution back into $f(x) = 0$.

> [!warning] Step 6 is the one that fails quietly
> "Successive iterates agree" is a weak test. It reports convergence when the
> iteration has stalled rather than when it has arrived, and it says nothing about
> whether the root is real.
>
> Two safer habits, both free: test the **residual** $\lvert f(x_k)\rvert < \varepsilon$
> rather than the step size, and **substitute the answer back** at the end. A
> stalled sequence with a small step and a large residual is the standard failure
> of Newton near a stationary point, and only the residual exposes it.

> [!note] Why the answer is a sequence and not a number
> This is the conceptual difference from 2020 Q.2(a). A direct method produces
> $\frac{-10 + 30}{2}$ and the answer is exact. An iterative method produces
> $5, 11.25, 10.048, 10.0001, 10$ and the answer is a limit.
>
> That sounds worse and is usually better, because the limit is reached to a
> **chosen** precision in a **chosen** number of steps, while the closed form may
> not exist at all. The cost of the flexibility is the obligation to test
> convergence, and step 6 exists for that reason alone.

---

### [2021 Q.2(a)]

**Question.** Define bracketing methods with example.

*[Marks: 02, CO: 1]*

**Solution.**

**Definition.** A **bracketing method** is an iterative root finder that begins
with an interval $[a, b]$ in which the function changes sign,

$$
f(a) \cdot f(b) < 0
$$

By the intermediate value theorem a continuous $f$ must have at least one root in
$(a, b)$. Each iteration picks a new point inside the current interval and retains
the half that still shows a sign change, so the root is never lost.

**Properties.**

1. **Convergence is guaranteed**, from any valid bracket, for any continuous $f$.
2. Only the **sign** of $f$ is needed, never $f'$. That is the big practical
   advantage, since a derivative is often harder to obtain than a function value.
3. The interval halves each step for bisection, so the error bound after $n$ steps
   is $\frac{b_0-a_0}{2^{n+1}}$.
4. Convergence is **slow**, linear for bisection, because no curvature
   information is used.

**Examples.**

| Method | New point | Rate |
| :-- | :-- | :-- |
| Bisection | Midpoint, $\frac{a+b}{2}$ | Linear |
| Regula falsi | Chord, $\frac{a f(b) - b f(a)}{f(b)-f(a)}$ | Superlinear, often |
| Illinois method | Regula falsi with a halved stale value | Superlinear, robust |

$$\boxed{\text{Enclose the root in a sign-changing interval and keep halving it; convergence is guaranteed}}$$

> [!note] Why the name, and what the guarantee is worth
> "Bracketing" means the iterate is *trapped* between two values of opposite sign,
> and the trap can only shrink. That is a stronger statement than "it usually
> converges", and it is what makes bracketing the fallback of choice when an open
> method misbehaves.
>
> The cost is speed. Superlinear rates in the table are for regula falsi and
> Illinois on well-behaved functions; part (b) of this question shows regula
> falsi stagnating on a strongly convex one, where it is barely better than
> bisection.

---

### [2022 Q.1(a)]

**Question.** What is the difference between open and bracketing method of root finding?

*[Marks: 02, CO: 1]*

**Solution.**

**Bracketing.** You start with an interval $[a,b]$ in which $f$ changes sign.

$$
f(a) \cdot f(b) < 0
$$

Continuity then guarantees at least one root inside. Each iteration throws away
the half of the interval that does not contain the sign change, so the interval
can never lose the root. That guarantee is the whole point.

**Open.** No interval. You start from a single guess $x_0$ and generate the next
point from a formula. Nothing keeps the iterates near the root, so a bad start
can send them off to infinity.

| Property | Bracketing | Open |
| :-- | :-- | :-- |
| Initial data | an interval with a sign change | one estimate $x_0$ |
| Needs | $f$ and its sign | $f$ **and** $f'$ |
| Convergence | always, from any valid bracket | only if $x_0$ is close enough |
| Rate | linear, $O(h)$ | superlinear, or quadratic |
| Examples | bisection, regula falsi | Newton-Raphson, secant, fixed point |

$$\boxed{\text{bracketing encloses the root and always converges; open methods start free and may not}}$$

> [!warning] The trade is safety against speed, not right against wrong
> An open method that converges is usually much faster: Newton-Raphson is
> quadratic, bisection is only linear, so Newton gets six correct digits in
> about five steps where bisection needs about thirty. The catch is that Newton
> can also fail completely, and there is no way to tell from the output that it
> has.
>
> This is why production root-finders keep a bracket and fall back to bisection
> whenever a Newton step leaves it. The hybrid gets the speed of the open method
> and the guarantee of the bracketing one, which is the reason the distinction
> matters beyond the two marks.

---

---

**Also asked here.**

- *2019 Q.2(b)* is the same question as [[NM-2.7|NM-2.7]], which is written in `NM-2.7`.
- *2020 Q.2(a)* is the same question as [[NM-2.6|NM-2.6]], which is written in `NM-2.6`.

---
