---
title: "NM-2.1 · Fundamentals & Classification"
tags:
  - numerical-methods
  - discrete-mathematics
  - topicwise
---


[🏠 Subtopic Index](00_Index.md) | [← Prev: NM-1.6 Taylor Series & Truncation Error](NM-1.6_Taylor_Series_and_Truncation_Error.md) | [Next: NM-2.2 Bisection Method →](NM-2.2_Bisection_Method.md)

---

# NM-2.1 · Fundamentals & Classification

Every block below is copied from `../answers_exam_style/`, which is the
only place an answer is authored. A number here is the same number, character
for character, as the one it came from.


### [2019 Q.2(a)]

**Question.** What is meant by iterative method? Write the names of iterative methods to solve nonlinear equations. Write the generalized steps to solve the nonlinear equations using iterative methods.

**Solution.**

An **iterative method** solves $f(x) = 0$ by producing a sequence
$x_0, x_1, x_2, \ldots$ from a starting estimate $x_0$, each term obtained from
the preceding ones by a fixed rule, so that the sequence converges to the root
$x = r$. The answer is accepted when successive terms agree to the required
precision, rather than when a formula closes.

**Methods for a nonlinear equation**

1. Bisection (or false position, regula falsi)
2. Fixed-point iteration
3. Newton–Raphson
4. Secant
5. Bairstow (for polynomial roots)

**Generalized steps**

1. Rewrite the problem in the form $f(x) = 0$.
2. Determine the interval or interval of interest, and count the roots in it
   from a change of sign of $f$.
3. Choose a starting estimate $x_0$ and, where required, a second estimate.
4. Derive the iteration formula $x_{k+1} = g(x_k)$.
5. Apply the formula repeatedly, recording each iterate.
6. Test for convergence by comparing successive iterates,
   $|x_{k+1} - x_k| < \varepsilon$, with $\varepsilon$ the tolerance.
7. If the sequence diverges or stalls, restart from a better estimate or from
   another method, and note the failure.
8. Verify the accepted root by substitution back into $f(x) = 0$.

---

### [2021 Q.2(a)]

**Question.** Define bracketing methods with example.

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
3. The interval halves each step for bisection, so the error bound after $n$ steps is
   $\frac{b_0-a_0}{2^{n+1}}$.
4. Convergence is **slow**, linear for bisection, because no curvature information
   is used.

**Examples.**

| Method | New point | Rate |
| :-- | :-- | :-- |
| Bisection | Midpoint, $\frac{a+b}{2}$ | Linear |
| Regula falsi | Chord, $\frac{a f(b) - b f(a)}{f(b)-f(a)}$ | Superlinear, often |
| Illinois method | Regula falsi with a halved stale value | Superlinear, robust |

$$
\boxed{\text{Enclose the root in a sign-changing interval and keep halving it; convergence is guaranteed}}
$$

---

### [2022 Q.1(a)]

**Question.** What is the difference between open and bracketing method of root finding?

**Solution.**

**Bracketing method.** The root is first **enclosed** in an interval $[a, b]$
where $f(a)$ and $f(b)$ have opposite signs,

$$
f(a) \cdot f(b) < 0
$$

Continuity guarantees a root inside. Every step keeps the sign change, so the
interval shrinks and the root can never be lost.

| Property | Bracketing |
| :-- | :-- |
| Initial data | An interval with a sign change |
| Information needed | Only $f$ and its sign |
| Convergence | Always, from any valid bracket |
| Rate | Linear, $O(h)$ |
| Examples | Bisection, regula falsi |

**Open method.** No interval is needed. The method starts from a single guess
$x_0$ and generates the next point from a formula, so it may wander away from the
root and never come back.

| Property | Open method |
| :-- | :-- |
| Initial data | One estimate $x_0$ |
| Information needed | $f$ **and** $f'$ |
| Convergence | Only if $x_0$ is close enough |
| Rate | Superlinear or quadratic |
| Examples | Newton-Raphson, secant, fixed point |

**Why the distinction matters.** Bracketing is safe but slow. Open methods are
fast but can fail, so production codes keep a bracket and fall back to bisection
whenever a Newton step leaves it. That hybrid keeps the speed of the open method
and the guarantee of the bracketing one.

$$
\boxed{\text{bracketing encloses the root and always converges; open methods start free and may not}}
$$

---

---

**Also asked here.**

- *2019 Q.2(b)* is the same question as [[NM-2.7_Roots_of_Polynomials|NM-2.7]], which is written in `NM-2.7`.
- *2020 Q.2(a)* is the same question as [[NM-2.6_Method_Comparison_and_Convergence|NM-2.6]], which is written in `NM-2.6`.

---

[🏠 Subtopic Index](00_Index.md) | [← Prev: NM-1.6 Taylor Series & Truncation Error](NM-1.6_Taylor_Series_and_Truncation_Error.md) | [Next: NM-2.2 Bisection Method →](NM-2.2_Bisection_Method.md)
