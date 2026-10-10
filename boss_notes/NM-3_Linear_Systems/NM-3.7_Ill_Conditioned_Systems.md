[← Previous: NM-3.6 Relaxation](NM-3.6_Relaxation.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: NM-3.8 Circuit Applications →](NM-3.8_Circuit_Applications.md)

---

# NM-3.7: Ill-Conditioned Systems

> 🟠 **Priority:** Secondary | **Tested:** 2 appearances | **Typical marks:** 2–4

## What This Is (and Why It Matters)

In high school geometry, two distinct lines cross at a crisp, unmistakable point. If the lines are perpendicular, finding their intersection is rock solid: nudge either line a tiny bit, and the intersection point barely wiggles.

Now imagine two lines that are **almost parallel** (say, slopes of $1.000$ and $1.001$). Geometrically, they still intersect. But because their angle of intersection is microscopic, a tiny nudge of $0.0001$ to one of the lines will send the intersection point flying miles down the coordinate axis!

That is the essence of an **ill-conditioned system**: a system of equations where tiny uncertainties in your input data produce wildly exaggerated errors in your calculated answer.

In RUET exams, this appears as a sharp theory question (such as 2022 Q.4(c)): define an ill-conditioned system, state how it is measured, explain why it happens, and explain why pivoting cannot fix it.

---

## 📝 Key Definitions

> **Ill-Conditioned System:** "A system of linear equations is ill-conditioned when a small change in the input produces a disproportionately large change in the solution." -- Topicwise NM-3.7
> 
> **In simple words:** A system of equations representing nearly parallel lines. A tiny sneeze in your sensor reading completely throws off the calculated answer.

> **Condition Number $\kappa(A)$:** The mathematical magnification factor between input uncertainty and output error:
> $$
> \frac{\|\delta \mathbf{x}\| / \|\mathbf{x}\|}{\|\delta \mathbf{b}\| / \|\mathbf{b}\|} \le \kappa(A) = \|A\|\,\|A^{-1}\|
> $$
> 
> **In simple words:** The volume knob for error. If $\kappa = 10^4$, a $0.01\%$ error in your input data can turn into a $100\%$ error in your calculated result.

> **Well-Conditioned System:** A system where the condition number is close to $1$, meaning input errors pass through without being magnified.
> 
> **In simple words:** A healthy, stable system where lines cross at a wide angle. Small input errors stay small in the output.

---

## The Core Idea

### The Error Magnification Inequality
Suppose you are solving $A\mathbf{x} = \mathbf{b}$. In the real world, your input vector $\mathbf{b}$ comes from experimental measurements or sensor readings, so it carries some tiny noise $\delta \mathbf{b}$.
Because of this noise, your computed answer has an error $\delta \mathbf{x}$:
$$
A(\mathbf{x} + \delta \mathbf{x}) = \mathbf{b} + \delta \mathbf{b}
$$

Subtracting $A\mathbf{x} = \mathbf{b}$ gives $A\delta \mathbf{x} = \delta \mathbf{b}$, which means $\delta \mathbf{x} = A^{-1}\delta \mathbf{b}$.  
Taking norms:
$$
\|\delta \mathbf{x}\| \le \|A^{-1}\|\,\|\delta \mathbf{b}\|
$$
And since $\|\mathbf{b}\| \le \|A\|\,\|\mathbf{x}\|$, multiplying these two inequalities gives the master error bound:
$$
\frac{\|\delta \mathbf{x}\|}{\|\mathbf{x}\|} \le \left(\|A\|\,\|A^{-1}\|\right) \frac{\|\delta \mathbf{b}\|}{\|\mathbf{b}\|} = \kappa(A) \frac{\|\delta \mathbf{b}\|}{\|\mathbf{b}\|}
$$

Look at what this means: **$\kappa(A)$ is the worst-case error amplifier.**

### Reading the Condition Number

| Condition Number $\kappa(A)$ | Numerical Behavior | Practical Meaning |
| :-- | :-- | :-- |
| $\kappa = 1$ | Perfectly conditioned | Identity or orthogonal matrix; error passes through unchanged |
| $\kappa \approx 10$ | Well-conditioned | Mild, safe amplification |
| $\kappa \approx 10^3$ to $10^4$ | Moderately ill-conditioned | You lose 3 to 4 decimal digits of precision |
| $\kappa \approx 10^6$ | Severely ill-conditioned | Loss of about 6 significant digits; single precision is useless |
| $\kappa > 10^{16}$ | Numerically singular | In standard double-precision arithmetic, all precision is lost! |

*Rule of thumb:* If $\kappa(A) \approx 10^k$, you lose roughly $k$ decimal digits of precision during computation.

### The Three Root Causes of Ill-Conditioning
1. **Nearly Singular Matrix (Nearly Parallel Equations):**  
   The determinant is close to zero, or one row is almost a linear combination of other rows. The equations barely constrain the solution.
2. **Wildly Disparate Scales:**  
   Some rows describe voltages measured in kilovolts ($10^3\text{ V}$) while other rows describe currents in microamperes ($10^{-6}\text{ A}$). The tiny numbers are effectively washed out by floating-point rounding.
3. **Redundant Physical Variables:**  
   Choosing two state variables that measure nearly the same physical quantity (such as temperatures at two points separated by only one millimeter in a copper block). The corresponding columns of $A$ become nearly identical.

### Remedies: How to Fight Ill-Conditioning
- **Row and column scaling (preconditioning):** Multiply rows and columns by scaling constants so all entries have comparable order of magnitude.
- **Reformulate the physical model:** Change variables (for example, solve for the temperature difference $\Delta T$ instead of two nearly identical absolute temperatures).
- **Higher precision arithmetic:** Switch from single precision (32-bit, ~7 digits) to double precision (64-bit, ~16 digits) or quadruple precision.

### The Key Exam Distinction: Stability vs. Conditioning
Make sure you never confuse these two concepts:
- **Numerical Stability** is a property of the **algorithm** (such as Gauss elimination). Pivoting prevents instability by avoiding small divisors during execution.
- **Conditioning** is an intrinsic property of the **physical problem itself** (measured by $\kappa(A)$).

> [!WARNING] The Examiner's Favorite Trap
> **Pivoting CANNOT fix an ill-conditioned system!**  
> If $\kappa(A) = 10^{10}$, running Gauss elimination with partial or complete pivoting will still return a completely wrong answer. Pivoting ensures that the arithmetic does not add its own error; it cannot manufacture accuracy when the physical equations themselves are hyper-sensitive.

---

## 🔧 Worked Example & Golden Question

### 2022 Q.4(c): Define Ill-Conditioned System -- [02 marks]

**The question:** Define ill-conditioned system.

**Tutor explanation & structured answer:**

**1. Definition:**  
A system of linear equations $A\mathbf{x} = \mathbf{b}$ is said to be **ill-conditioned** when a small change or perturbation in the input data produces a disproportionately large change in the computed solution.

**2. Quantitative Measure (Condition Number):**  
The sensitivity of the system is measured by the **condition number** $\kappa(A)$ of the coefficient matrix:
$$
\frac{\dfrac{\|\delta \mathbf{x}\|}{\|\mathbf{x}\|}}{\dfrac{\|\delta \mathbf{b}\|}{\|\mathbf{b}\|}} \le \kappa(A) = \|A\|\,\|A^{-1}\|
$$
If the input data carries a relative uncertainty of $\varepsilon$, the computed answer may carry a relative error as large as $\kappa(A)\,\varepsilon$.

**3. Numerical Spectrum:**
- $\kappa \approx 1$: Well-conditioned system; errors pass through without amplification.
- $\kappa \approx 10^6$: Loss of approximately six significant decimal digits.
- $\kappa > 10^{16}$: Matrix is numerically singular in 64-bit floating point; all meaningful precision is destroyed.

**4. Causes and Engineering Impact:**  
- **Causes:** Nearly parallel constraint equations (nearly singular matrix), coefficients differing by many orders of magnitude, or redundant physical variables.
- **Why it matters:** Engineering sensor data typically has $0.1\%$ ($10^{-3}$) instrument uncertainty. If $\kappa = 10^6$, the solution carries an error of $10^3 = 1000\%$, rendering the computed answer completely useless.
- **Remedies:** Variable rescaling, problem reformulation, or using extended precision. (Note: Pivoting improves algorithmic stability but does not alter $\kappa(A)$.)

$$
\boxed{\text{ill-conditioned means small input errors produce large output errors; measured by }\kappa}
$$

---

### A Concrete 2D Demonstration

Consider this simple $2 \times 2$ system:
$$
\begin{aligned}
x + y &= 2 \\
x + 1.001y &= 2.001
\end{aligned}
$$
The exact solution is $x = 1, y = 1$.

Now suppose a sensor error changes the second right-hand side by just $0.001$ (from $2.001$ to $2.002$):
$$
\begin{aligned}
x + y &= 2 \\
x + 1.001y &= 2.002
\end{aligned}
$$
Subtracting the first equation gives:
$$
0.001y = 0.002 \implies y = 2
$$
And plugging back into the first equation:
$$
x = 2 - 2 = 0
$$

Look at that shocker:
- Input change: from $2.001$ to $2.002$ (a tiny $0.05\%$ shift).
- Output change: from $(1, 1)$ to $(0, 2)$ (a massive $100\%$ swing!).

That is ill-conditioning in action.

---

### Exam Variants at a Glance

| Year | What They Asked | Key Definition / Formula |
|:---|:---|:---|
| **2022 Q.4(c)** | Define ill-conditioned system (02 marks) | $\boxed{\text{ill-conditioned means small input errors produce large output errors; measured by }\kappa}$ |

---

## ⚡ Quick Review

**The concept in one sentence:** A system is ill-conditioned when tiny variations in input data cause massive swings in the calculated solution, because the equations describe nearly parallel constraints.

**The condition number formula:**
$$
\kappa(A) = \|A\|\,\|A^{-1}\|, \qquad \frac{\|\delta \mathbf{x}\|}{\|\mathbf{x}\|} \le \kappa(A)\frac{\|\delta \mathbf{b}\|}{\|\mathbf{b}\|}
$$

**The cardinal exam rule:** Pivoting fixes algorithm stability, NOT problem conditioning.

**Time estimate in exam:** ~3 to 4 minutes to write a crisp, complete definition with the error inequality and root causes.

---

## 🔗 Connected Topics

- [← NM-3.6: Relaxation](NM-3.6_Relaxation.md) -- why ill-conditioned systems fail to converge smoothly under iterative relaxation.
- [→ NM-3.8: Circuit Applications](NM-3.8_Circuit_Applications.md) -- how passive resistor networks naturally avoid ill-conditioning through strong diagonal dominance.
- [NM-3.2: Pivoting](NM-3.2_Pivoting.md) -- comparing algorithmic stability against intrinsic problem conditioning.

---

[← Previous: NM-3.6 Relaxation](NM-3.6_Relaxation.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: NM-3.8 Circuit Applications →](NM-3.8_Circuit_Applications.md)
