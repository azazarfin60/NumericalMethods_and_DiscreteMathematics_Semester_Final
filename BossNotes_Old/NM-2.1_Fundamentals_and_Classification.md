[← Previous: NM-1 Lower Tier](NM-1_Lower_Modeling_Accuracy_Precision.md) | [🏠 Index](00_Index.md) | [Next: NM-2.2 Bisection Method →](NM-2.2_Bisection_Method.md)

---

# NM-2.1: Fundamentals and Classification of Root-Finding Methods
> **Section:** A (Numerical Methods) | **Priority:** 🔴 | **Exam Frequency:** 4/8 years
> **Sources:** Jain Ch.2 §2.1, §2.4, Topicwise NM-2.1, Fahad Notes §02

## Why This Topic Matters

NM-2 is the gateway to every numerical solver you will meet later. Gauss-Seidel, Runge-Kutta and the Newton step inside Gauss-Newton all borrow the same ideas from root finding. In the exam it appears as short theory questions: define an iterative method, define a bracketing method, or explain open versus bracketing. Each is worth 2 to 4 marks and takes two minutes to write once you know the shape of the answer.

---

## 📝 Key Definitions

> **Root of an equation:** "a frequently occurring problem is to find the roots of equations of the form $f(x) = 0$." — Jain, §2.1

> **Polynomial:** "algebraic functions of the form $f_n(x) = a_0x^n + a_1x^{n-1} + a_2x^{n-2} + \cdots + a_{n-1}x + a_n$ are called *polynomials*." — Jain, §2.1

> **Transcendental function:** "A non-algebraic function is called a *transcendental function*, e.g., $f(x) = \ln x^3 - 0.7$, $\phi(x) = e^{-0.5x} - 5x$, $\psi(x) = \sin^2 x - x^2 - 2$." — Jain, §2.1

> **Root (working definition):** A **root** of $f(x) = 0$ is a value $x^*$ such that $f(x^*) = 0$. The graph of $f$ crosses or touches the $x$-axis at $x^*$.

> **Iterative method:** A method that solves $f(x) = 0$ by producing a sequence $x_0, x_1, x_2, \ldots$ from a starting estimate, each term obtained from the previous ones by a fixed rule, until the sequence converges to the root.

> **Bracketing method:** An iterative root finder that starts with an interval $[a, b]$ where $f$ changes sign, and repeatedly shrinks that interval while keeping the sign change.

> **Open method:** A root finder that starts from one or two guesses and applies a formula. No interval is maintained, so the iterates can wander away from the root.

---

## Core Theory: What a Root Is

A root is just an $x$-value where the curve meets the $x$-axis. Nothing more. Everything else in this chapter is machinery for finding that $x$ when algebra cannot give it in closed form.

**The classification that matters.** Every method in NM-2 falls into one of two families, and the exam asks about this split directly (2022 Q.1(a), 2020 Q.2(a)).

| Family | What it needs | Can it fail? | Speed |
| :-- | :-- | :--: | :-- |
| **Bracketing** | an interval $[a,b]$ with $f(a)f(b) < 0$ | Never, once the bracket is valid | Slow, linear |
| **Open** | one guess $x_0$, or two for secant | Yes, badly | Fast, quadratic for Newton |

Bracketing methods keep the root inside a shrinking interval. Open methods throw the interval away and chase the root with a formula. Safe and slow against fast and unguaranteed is the whole trade.

### Why a Sign Change Guarantees a Root

The intermediate value theorem does the work. If $f$ is continuous on $[a, b]$ and $f(a)f(b) < 0$, then $f$ must pass through zero somewhere between them. That is why every algorithm in this chapter opens with the same check: compute $f(a)$ and $f(b)$, and reject the interval if their product is positive.

> [!WARNING]
> An even-multiplicity root is invisible to this test. If $f$ touches the axis without crossing it, as $f(x) = (x-2)^2$ does, then $f(a)f(b) > 0$ at the true bracket and step 1 rejects it. No bracketing method can find it. This single fact explains why so many bracketing questions ask you to pick the interval first.

### Simple, Multiple, Explicit, Implicit

The exam asks you to define a root (2020 Q.2(a)), so cover all four adjectives:

- **Simple** root: $f'(x^*) \ne 0$. The curve actually crosses the axis.
- **Multiple** (repeated) root: $f'(x^*) = 0$. The curve touches the axis. Slows Newton down badly.
- **Explicit** root: writable in closed form, like $\sqrt{2}$.
- **Implicit** root: no closed form exists, like the root of $x^5 - x - 1 = 0$. Only numerical methods reach it.

---

## The Iterative Idea

A **direct** method runs a fixed number of arithmetic steps and hands back the exact answer. Solve $I^2 + 10I - 200 = 0$ and you get $I = \frac{-10 \pm 30}{2}$, done.

An **iterative** method hands back a sequence and asks you to watch it. Solve $5I^2 + 50I = 1000$ by Newton and you get $5, 11.25, 10.048, 10.0001, 10$. The answer is the limit, not any single line.

That sounds worse. It is usually better, for two reasons.

1. Most equations of interest have no closed form at all.
2. You choose the precision. Stop when the correction drops below your tolerance.

The cost is that you must test for convergence. Every iteration needs a stopping rule.

### The Eight Generalized Steps (2019 Q.2(a))

The exam asks for these verbatim, so memorise the list:

1. Rewrite the problem as $f(x) = 0$.
2. Find the interval of interest, and count roots in it from sign changes of $f$.
3. Choose a starting estimate $x_0$, plus a second one if the method needs it.
4. Derive the iteration formula $x_{k+1} = g(x_k)$.
5. Apply the formula repeatedly, recording every iterate.
6. Test convergence: accept when $|x_{k+1} - x_k| < \varepsilon$.
7. If the sequence diverges or stalls, restart from a better estimate or another method.
8. Verify the accepted root by substituting it back into $f(x) = 0$.

### Convergence Criteria

Three stopping rules exist, and the exam expects you to name the one you use:

$$
|x_{k+1} - x_k| < \varepsilon
$$

$$
|f(x_k)| < \varepsilon
$$

$$
\frac{|x_{k+1} - x_k|}{|x_{k+1}|} \times 100\% < \varepsilon_r
$$

> [!TIP]
> Test the residual $|f(x_k)|$, not the step size, whenever you can. A stalled Newton run near a stationary point produces a tiny step and a huge residual. Step size alone cannot tell the two apart. The residual can.

---

## Worked Example: Classifying the Four Methods

**Problem.** For each of bisection, false position, secant and Newton-Raphson, state the family, the starting data, and the convergence guarantee.

**Step 1.** Bisection and false position start from a bracket. They are bracketing methods.

**Step 2.** Secant and Newton-Raphson start from free guesses. They are open methods.

**Step 3.** The table below is the answer in the form the exam wants.

| | Bisection | False position | Secant | Newton-Raphson |
| :-- | :-- | :-- | :-- | :-- |
| Family | Bracketing | Bracketing | Open | Open |
| Starts from | $a_0$, a bracket | $a_0$, a bracket | $x_0, x_1$ | $x_0$ only |
| Needs $f'$ | No | No | No | **Yes** |
| Needs a sign change | **Yes** | **Yes** | No | No |
| Order | 1 | 1, often faster | 1.618 | **2** |
| Guaranteed | **Yes** | **Yes** | No | No |

Full discussion of the numbers in this table lives in [NM-2.6](NM-2.6_Method_Comparison_and_Convergence.md).

### Exam Variants

| Year | Question | Data Given | Key Answer |
|:---|:---|:---|:---|
| 2019 Q.2(a) | Define iterative method, name the methods, give the generalized steps | none (04 marks) | Eight numbered steps, ending with substitution back into $f(x) = 0$ |
| 2021 Q.2(a) | Define bracketing methods with example | none (02 marks) | $\boxed{\text{Enclose the root in a sign-changing interval and keep halving it; convergence is guaranteed}}$ |
| 2022 Q.1(a) | Difference between open and bracketing methods | none (02 marks) | $\boxed{\text{bracketing encloses the root and always converges; open methods start free and may not}}$ |

---

## 🏆 Golden Questions (Past Exam Archive)

### 🎯 What is meant by iterative method? Write the names of iterative methods to solve nonlinear equations. Write the generalized steps to solve the nonlinear equations using iterative methods.
> **Appeared:** 2019 Q.2(a) — (04 marks)

**Full Answer:**

An **iterative method** solves $f(x) = 0$ by producing a sequence $x_0, x_1, x_2, \ldots$ from a starting estimate $x_0$. Each term is obtained from the preceding ones by a fixed rule, and the sequence converges to the root $x = r$. The answer is accepted when successive terms agree to the required precision, not when a formula closes.

**Methods for a nonlinear equation**

1. Bisection, or false position, or regula falsi
2. Fixed-point iteration
3. Newton-Raphson
4. Secant
5. Bairstow, for polynomial roots

**Generalized steps**

1. Rewrite the problem in the form $f(x) = 0$.
2. Determine the interval of interest, and count the roots in it from a change of sign of $f$.
3. Choose a starting estimate $x_0$ and, where required, a second estimate.
4. Derive the iteration formula $x_{k+1} = g(x_k)$.
5. Apply the formula repeatedly, recording each iterate.
6. Test for convergence by comparing successive iterates, $|x_{k+1} - x_k| < \varepsilon$, where $\varepsilon$ is the tolerance.
7. If the sequence diverges or stalls, restart from a better estimate or from another method, and note the failure.
8. Verify the accepted root by substitution back into $f(x) = 0$.

> [!WARNING]
> Step 6 is the one that fails quietly. Successive iterates agreeing is a weak test. It reports convergence when the iteration stalled, and it says nothing about whether the root is real. Two safer habits, both free: test the residual $|f(x_k)| < \varepsilon$ instead of the step size, and substitute the answer back at the end. A stalled sequence with a small step and a large residual is the standard failure of Newton near a stationary point, and only the residual exposes it.

> [!NOTE]
> From $5I^2 + 50I = 1000$, a direct method produces $\frac{-10+30}{2}$ and the answer is exact. The iterative method produces $5, 11.25, 10.048, 10.0001, 10$ and the answer is a limit. The limit is reached to a chosen precision in a chosen number of steps, which is what the flexibility buys.

---

### 🎯 Define bracketing methods with example.
> **Appeared:** 2021 Q.2(a) — (02 marks, CO: 1)

**Full Answer:**

**Definition.** A **bracketing method** is an iterative root finder that begins with an interval $[a, b]$ in which the function changes sign,

$$
f(a) \cdot f(b) < 0
$$

By the intermediate value theorem a continuous $f$ must have at least one root in $(a, b)$. Each iteration picks a new point inside the current interval and retains the half that still shows a sign change, so the root is never lost.

**Properties.**

1. Convergence is guaranteed, from any valid bracket, for any continuous $f$.
2. Only the **sign** of $f$ is needed, never $f'$. That is the practical advantage, since a derivative is often harder to obtain than a function value.
3. The interval halves each step for bisection, so the error bound after $n$ steps is $\frac{b_0-a_0}{2^{n+1}}$.
4. Convergence is slow, linear for bisection, because no curvature information is used.

**Examples.**

| Method | New point | Rate |
| :-- | :-- | :-- |
| Bisection | Midpoint, $\frac{a+b}{2}$ | Linear |
| Regula falsi | Chord, $\frac{a f(b) - b f(a)}{f(b)-f(a)}$ | Superlinear, often |
| Illinois method | Regula falsi with a halved stale value | Superlinear, does not stall |

$$
\boxed{\text{Enclose the root in a sign-changing interval and keep halving it; convergence is guaranteed}}
$$

> [!NOTE]
> "Bracketing" means the iterate is trapped between two values of opposite sign, and the trap can only shrink. That is a stronger statement than "it usually converges". It is what makes bracketing the fallback of choice when an open method misbehaves. The cost is speed: the superlinear rates above are for well-behaved functions, and 2021 Q.2(b) shows regula falsi stagnating on a strongly convex one.

---

### 🎯 What is the difference between open and bracketing method of root finding?
> **Appeared:** 2022 Q.1(a) — (02 marks, CO: 1)

**Full Answer:**

**Bracketing method.** The root is first enclosed in an interval $[a, b]$ where $f(a)$ and $f(b)$ have opposite signs,

$$
f(a) \cdot f(b) < 0
$$

Continuity guarantees a root inside. Every step keeps the sign change, so the interval shrinks and the root can never be lost.

| Property | Bracketing |
| :-- | :-- |
| Initial data | An interval with a sign change |
| Information needed | Only $f$ and its sign |
| Convergence | Always, from any valid bracket |
| Rate | Linear, $O(h)$ |
| Examples | Bisection, regula falsi |

**Open method.** No interval is needed. The method starts from a single guess $x_0$ and generates the next point from a formula, so it may wander away from the root and never come back.

| Property | Open method |
| :-- | :-- |
| Initial data | One estimate $x_0$ |
| Information needed | $f$ **and** $f'$ |
| Convergence | Only if $x_0$ is close enough |
| Rate | Superlinear or quadratic |
| Examples | Newton-Raphson, secant, fixed point |

$$
\boxed{\text{bracketing encloses the root and always converges; open methods start free and may not}}
$$

**Why the distinction matters.** Bracketing is safe but slow. Open methods are fast but can fail, so production codes keep a bracket and fall back to bisection whenever a Newton step leaves it. That hybrid keeps the speed of the open method and the guarantee of the bracketing one.

---

## ⚡ Exam Tips & Common Mistakes

1. **Learn the eight generalized steps as a list.** 2019 Q.2(a) is four marks for pure reproduction. Numbered lists score better than a paragraph.
2. **Do not confuse "iterative" with "bracketing".** Every method here is iterative. Only some are bracketing. Newton is iterative and open, and that combination is exactly why it can diverge.
3. **State the check, not just the method.** Any question that gives you an interval, start by writing $f(a)f(b) < 0$ and confirming it. It is one line and it earns method marks.
4. **Name the stopping rule you used.** A table of iterates with no stated criterion is incomplete. Write $|x_{k+1} - x_k| < 10^{-4}$ or similar, then apply it.
5. **Open versus bracketing is a two-mark question.** Answer it with a table plus one boxed sentence. Do not write a paragraph.

## 🔗 Related Topics

- [NM-2.2: Bisection Method](NM-2.2_Bisection_Method.md) — the simplest bracketing method, and the fallback for everything else
- [NM-2.4: Newton-Raphson Method](NM-2.4_Newton_Raphson_Method.md) — the most important open method, and its four failure modes
- [NM-2.6: Method Comparison & Convergence](NM-2.6_Method_Comparison_and_Convergence.md) — the full four-method comparison table
- [NM-1.1: Foundations of Numerical Methods](NM-1.1_Foundations_of_Numerical_Methods.md) — why an approximate method is needed at all

---

[← Previous: NM-1 Lower Tier](NM-1_Lower_Modeling_Accuracy_Precision.md) | [🏠 Index](00_Index.md) | [Next: NM-2.2 Bisection Method →](NM-2.2_Bisection_Method.md)
