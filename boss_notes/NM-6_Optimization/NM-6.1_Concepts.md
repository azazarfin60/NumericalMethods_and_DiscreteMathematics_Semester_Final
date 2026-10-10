[← Previous: NM-5.7 Applied Integration](../NM-5_Integration/NM-5.7_Applied_Integration.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: NM-6.2 Unconstrained Optimization →](NM-6.2_Unconstrained_Optimization.md)

---

# NM-6.1: Optimization Concepts

> 🟡 **Priority:** Light (Emerging) | **Tested:** 1/8 years (2021 Q.6(d)) | **Typical marks:** 2

## What This Is (and Why It Matters)

Optimization is simply the mathematics of finding the best choice. In electrical and computer engineering, you constantly want the highest efficiency, the cleanest signal, the lowest power draw, or the smallest chip footprint.

Before writing a single line of code or taking a derivative, you must answer one fundamental question: *Are your design variables completely free to take any value, or are they bounded by strict limits?*

That question divides the entire discipline into two halves: unconstrained optimization and constrained optimization.

In the 2021 semester final, RUET tested this distinction as a neat 2-mark question. It is an easy question to answer if you clearly contrast the mathematical formulation, the stationarity conditions, the location of the optimum, and the engineering meaning of each.

---

## 📝 Key Definitions

> **Optimization:** "Optimization is the process of finding the conditions that give the maximum or minimum value of a function." -- Rao, Engineering Optimization §1.1
>
> **In simple words:** Finding the exact input values that give you the best possible output, such as the highest speed, lowest cost, or minimum energy loss.

> **Unconstrained Optimization:** "An unconstrained optimization problem seeks to find a vector $x \in \mathbb{R}^n$ that minimizes or maximizes an objective function $f(x)$ without any restrictions placed on the values of the decision variables." -- Rao, §1.4
>
> **In simple words:** You can choose any numbers in the entire universe. No rules or walls hold you back. The optimum always sits where the slope levels out completely flat ($\nabla f = 0$).

> **Constrained Optimization:** "A constrained optimization problem requires extremizing an objective function $f(x)$ subject to one or more equality constraints $h_j(x) = 0$ and inequality constraints $g_i(x) \le 0$." -- Rao, §1.4
>
> **In simple words:** You must obey strict budgets, safety limits, and physical rules. The best operating point is often pushed right up against a boundary wall, meaning the slope there is usually not zero.

> **Feasible Region:** "The feasible region is the collection of all points in the design space that satisfy all equality and inequality constraints simultaneously." -- Rao, §1.4
>
> **In simple words:** The allowable playing field. If an operating point breaks even one safety limit, it is outside the feasible region and cannot be used.

---

## The Core Idea

When you want to find an optimum, your strategy depends entirely on whether your variables roam freely across the entire space or remain trapped inside boundaries.

### Unconstrained Optimization

In unconstrained problems, you want to minimize or maximize an objective function $f(x)$ where $x = (x_1, x_2, \dots, x_n) \in \mathbb{R}^n$:

$$
\text{minimise } f(x_1, x_2, \dots, x_n), \qquad x \in \mathbb{R}^n
$$

Because you have zero restrictions, the optimum always settles where the function stops changing in every direction. That means the gradient vector must be exactly zero:

$$
\nabla f = 0
$$

For a single variable $x$, that is just $f'(x) = 0$.

**Real-world ECE example:**
Fitting a straight line $y = a + bx$ to noisy laboratory voltage-current data using least squares. Neither slope $b$ nor intercept $a$ has an artificial ceiling or floor. You choose both parameters freely across all real numbers to minimize the sum of squared errors.

### Constrained Optimization

In real engineering, design choices are rarely free. Components overheat, power supplies have voltage ceilings, and budgets run out.

Formally, a constrained problem is stated as:

$$
\text{minimise } f(x) \quad \text{subject to } \quad g_i(x) \le 0 \ (i = 1, \dots, m), \quad h_j(x) = 0 \ (j = 1, \dots, p)
$$

Here:
- $f(x)$ is your **objective function** (what you want to minimize or maximize).
- $g_i(x) \le 0$ are your **inequality constraints** (resource limits, temperature caps, minimum gain thresholds).
- $h_j(x) = 0$ are your **equality constraints** (conservation of charge, Kirchhoff's laws).

**Real-world ECE example:**
Designing a wireless transceiver amplifier. You want to minimize total DC power consumption $P_{DC}(I_B, V_{DD})$, but you must maintain an open-loop gain $\ge 40\text{ dB}$, keep supply voltage $V_{DD} \le 3.3\text{ V}$, and ensure the transistor junction temperature never exceeds $85^\circ\text{C}$.

### Why the Distinction Matters: The Boundary Phenomenon

This is the central mathematical insight:

1. **In unconstrained optimization**, the optimal point is an **interior point**. The curve reaches a smooth peak or trough, where the tangent plane is horizontal. Setting $\nabla f = 0$ finds the solution directly.
2. **In constrained optimization**, the optimal point very often sits **on a boundary wall**.
   - Think of maximizing current through a load resistor: the mathematical function might want infinite current, but your fuse blows at $5\text{ A}$. The optimal legal operating current is exactly $5\text{ A}$.
   - On that boundary, the gradient $\nabla f$ is **not zero**! If you were allowed to step past the boundary, the function could keep improving. But the constraint physically blocks you.
   - Because the plain gradient test $\nabla f = 0$ fails on boundaries, engineers must use **Lagrange multipliers** for equality constraints and **Karush-Kuhn-Tucker (KKT) conditions** for inequality constraints.

### Comparison Table

| Feature | Unconstrained Optimization | Constrained Optimization |
| :-- | :-- | :-- |
| **Restrictions** | None; variables take any real value | Equality ($h_j(x) = 0$) and inequality ($g_i(x) \le 0$) conditions |
| **Feasible Region** | Entire space $\mathbb{R}^n$ | Bounded subset of $\mathbb{R}^n$ |
| **Stationarity Test** | Gradient vanishes: $\nabla f = 0$ | KKT condition: $\nabla f + \sum \mu_i \nabla g_i + \sum \lambda_j \nabla h_j = 0$ |
| **Optimum Location** | Interior stationary point | Frequently sits directly on a boundary constraint |
| **Multipliers Needed?** | No multipliers required | Essential (Lagrange multipliers $\lambda_j$ and KKT multipliers $\mu_i$) |
| **Analytical Difficulty** | Simpler; solve a system of algebraic equations | Harder; must test which inequality constraints are active on boundaries |
| **ECE Example** | Least-squares linear regression line fitting | Maximizing amplifier bandwidth subject to fixed DC power supply limits |

---

## 🏆 Past Exam Questions

### 2021 Q.6(d): Differentiate between constrained and unconstrained optimization: [Marks: 02]

**The question:** Differentiate between constrained and unconstrained optimization.

**Let's answer this clearly step by step.**

To get full marks in an exam on a 2-mark comparison question, write concise definitions for both, state their mathematical governing conditions, give an example of each, and present a quick comparison table:

**1. Unconstrained optimization.** There are no restrictions on the decision variables. You choose $x$ freely in the entire domain $\mathbb{R}^n$ to maximize or minimize an objective function $f(x)$:

$$
\text{minimise } f(x_1, x_2, \dots, x_n), \qquad x \in \mathbb{R}^n
$$

The stationarity condition is simply that the gradient vanishes: $\nabla f = 0$.

*Example:* Fitting a straight line $y = a + bx$ to data using least squares. Nothing restricts parameters $a$ or $b$.

**2. Constrained optimization.** Restrictions apply to the decision variables. Each restriction is expressed as an inequality $g_i(x) \le 0$ or an equality $h_j(x) = 0$:

$$
\text{minimise } f(x) \quad \text{subject to } \quad g_i(x) \le 0 \ (i = 1, \dots, m), \quad h_j(x) = 0 \ (j = 1, \dots, p)
$$

The optimum frequently sits directly on a boundary constraint, where the ordinary gradient test $\nabla f = 0$ fails. It is solved using Lagrange multipliers or Karush-Kuhn-Tucker (KKT) conditions.

*Example:* Minimizing the weight of a transmission tower subject to stress limits on every crossbar, or designing an IC filter with a strict chip area budget.

| Feature | Unconstrained | Constrained |
| :-- | :-- | :-- |
| Restrictions | None | Equality and inequality conditions |
| Stationarity test | $\nabla f = 0$ | KKT multipliers: $\nabla f + \sum \mu_i \nabla g_i + \sum \lambda_j \nabla h_j = 0$ |
| Lagrange multipliers | Not needed | Essential |
| Optimum location | Interior point | Often on the boundary |
| Feasible region | Whole space | A subset |
| Solution effort | Easier | Harder; multiple constraint boundaries to test |

$$
\boxed{\text{Unconstrained: choose freely. Constrained: obey rules, solved with multipliers}}
$$

---

## ⚡ Quick Review

**The core difference in one sentence:** Unconstrained optimization lets variables take any value where the gradient vanishes ($\nabla f = 0$), while constrained optimization enforces boundaries and requires multiplier methods because the peak often lies against a wall.

**The condition you must memorize:**
$$
\nabla f = 0 \quad (\text{Unconstrained}) \qquad \text{versus} \qquad \nabla f + \sum \mu_i \nabla g_i + \sum \lambda_j \nabla h_j = 0 \quad (\text{Constrained KKT})
$$

**The most common exam mistake:** Forgetting to mention *why* the distinction matters mathematically (that constrained optima frequently sit on boundaries where $\nabla f \neq 0$).

**Time estimate in exam:** 4 to 5 minutes for a clean 2-mark answer.

---

## 🔗 Connected Topics

- [← NM-5.7: Applied Integration](../NM-5_Integration/NM-5.7_Applied_Integration.md): Completes numerical integration topics from earlier exam papers.
- [→ NM-6.2: One-Dimensional Unconstrained Optimization](NM-6.2_Unconstrained_Optimization.md): Applies numerical root-finding algorithms to solve unconstrained problems where $f'(x) = 0$.
- [NM-4.2: Least Squares Linear Regression](../NM-4_Curve_Fitting/NM-4.2_Linear_Regression.md): A classic unconstrained optimization problem solved by setting partial derivatives to zero.

---

[← Previous: NM-5.7 Applied Integration](../NM-5_Integration/NM-5.7_Applied_Integration.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: NM-6.2 Unconstrained Optimization →](NM-6.2_Unconstrained_Optimization.md)
