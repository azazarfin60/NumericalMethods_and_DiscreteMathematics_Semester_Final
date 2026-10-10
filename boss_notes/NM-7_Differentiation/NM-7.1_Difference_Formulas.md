[← Previous: NM-6.3 Tabulated Optima](../NM-6_Optimization/NM-6.3_Tabulated_Optima.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: NM-7.2 First Derivative →](NM-7.2_First_Derivative.md)

---

# NM-7.1: Basis & Difference Formulas

> 🟠 **Priority:** Secondary | **Tested:** 2019 Q.6(a) | **Typical marks:** 4

## What This Is (and Why It Matters)

In introductory calculus, finding a derivative is easy: you take the formal definition $f'(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}$ and let $h$ slide smoothly down to zero. In actual engineering work, however, you cannot take that limit. You do not have a continuous function. You only have a table of numbers measured at discrete sampling intervals $h$ (like voltage sampled every 10 milliseconds).

Numerical differentiation gives us formulas to calculate derivatives directly from those discrete table values.

The exam likes to test this foundation as a theoretical opener. In 2019 Q.6(a), examiners asked students to state what numerical differentiation rests on and write out at least four difference equations with their error orders. It is an easy 4 marks if you know the formulas and the Taylor series logic behind them.

---

## 📝 Key Definitions

> **Basis of numerical differentiation:** "The general method for deriving the numerical differentiation formulae is to differentiate the interpolating polynomial. Hence, corresponding to each of the formulae derived in Chapter 3, we may derive a formula for the derivative." -- Jain, §6.2 (p. 207)
>
> **In simple words:** We do not know the real curve between data points, so we draw an interpolating polynomial through the points and take the derivative of that polynomial instead.

> **Numerical differentiation problem:** "given the set of values of $x$ and $y$, as above, we shall derive formulae to compute (i) $\frac{dy}{dx}, \frac{d^2y}{dx^2}, \dots$ for any value of $x$ in $[x_0, x_n]$" -- Jain, §6.1 (p. 207)
>
> **In simple words:** Given a spreadsheet of $x$ and $y$ measurements, we want to calculate the slope or curvature at any chosen point without guessing.

> **Why numerical differentiation is unreliable:** "although the tabulated function and its approximating polynomial would agree at the set of data points, *their slopes at these points may vary considerably*. Numerical differentiation, is, therefore, an unsatisfactory process and should be used only in 'rare cases.'" -- Jain, §6.2 (p. 212)
>
> **In simple words:** A polynomial can pass through every single data point perfectly, yet wiggle wildly between the points. Its slope can be completely wrong even when the curve fits the data exactly.

> **Order of accuracy:** "The symbol $O(h^p)$ denotes that the truncation error is bounded by a constant times $h^p$ as the step size $h$ approaches zero."
>
> **In simple words:** If a formula is $O(h)$, cutting your step size in half cuts your error in half. If a formula is $O(h^2)$, cutting your step size in half cuts your error by a factor of 4!

---

## The Core Idea

All numerical differentiation formulas come from one mathematical engine: the **Taylor series expansion**.

When you write the Taylor expansion of $f(x)$ at nearby nodes $x+h$, $x-h$, $x+2h$, and so forth, you get a system of equations:

$$
f(x + h) = f(x) + hf'(x) + \frac{h^2}{2!}f''(x) + \frac{h^3}{3!}f'''(x) + \frac{h^4}{4!}f^{(4)}(x) + \cdots
$$

$$
f(x - h) = f(x) - hf'(x) + \frac{h^2}{2!}f''(x) - \frac{h^3}{3!}f'''(x) + \frac{h^4}{4!}f^{(4)}(x) - \cdots
$$

By taking clever linear combinations of these equations, you can cancel out the terms you do not want (like $f''(x)$ or $f'''(x)$) and isolate $f'(x)$.

### 1. Two-Point Forward Difference ($O(h)$)

Take the expansion of $f(x+h)$ and solve directly for $f'(x)$:

$$
f(x+h) - f(x) = hf'(x) + \frac{h^2}{2}f''(\xi)
$$

Dividing across by $h$:

$$
f'(x) = \frac{f(x+h) - f(x)}{h} - \frac{h}{2}f''(\xi)
$$

Dropping the remainder gives the standard **two-point forward formula**:

$$
f'(x_n) = \frac{f_{n+1} - f_n}{h}, \qquad \text{error } O(h)
$$

### 2. Two-Point Backward Difference ($O(h)$)

Take the expansion of $f(x-h)$ and isolate $f'(x)$:

$$
f(x) - f(x-h) = hf'(x) - \frac{h^2}{2}f''(\xi)
$$

Dividing by $h$:

$$
f'(x) = \frac{f(x) - f(x-h)}{h} + \frac{h}{2}f''(\xi)
$$

Dropping the remainder gives the **two-point backward formula**:

$$
f'(x_n) = \frac{f_n - f_{n-1}}{h}, \qquad \text{error } O(h)
$$

### 3. Three-Point Central Difference ($O(h^2)$)

Notice what happens if you subtract the backward expansion from the forward expansion:

$$
f(x+h) - f(x-h) = 2hf'(x) + 2\frac{h^3}{6}f'''(\xi) = 2hf'(x) + \frac{h^3}{3}f'''(\xi)
$$

The even-power terms ($\frac{h^2}{2}f''(x)$, $\frac{h^4}{24}f^{(4)}(x)$) cancel out completely! Dividing by $2h$:

$$
f'(x) = \frac{f(x+h) - f(x-h)}{2h} - \frac{h^2}{6}f'''(\xi)
$$

This gives the celebrated **three-point central formula**:

$$
f'(x_n) = \frac{f_{n+1} - f_{n-1}}{2h}, \qquad \text{error } O(h^2)
$$

Because the error is $O(h^2)$ instead of $O(h)$, the central formula is far more accurate than the one-sided two-point formulas. Whenever you have data points on both sides of your target, always choose the central formula.

### 4. Three-Point Forward Difference ($O(h^2)$)

What if you are at the beginning of a table and cannot look backward, but you still need $O(h^2)$ accuracy? You can use three forward points: $x$, $x+h$, and $x+2h$.

Write the expansions:
1. $f(x+h) = f(x) + hf'(x) + \frac{h^2}{2}f''(x) + \frac{h^3}{6}f'''(x) + \cdots$
2. $f(x+2h) = f(x) + 2hf'(x) + \frac{(2h)^2}{2}f''(x) + \frac{(2h)^3}{6}f'''(x) + \cdots = f(x) + 2hf'(x) + 2h^2f''(x) + \frac{4h^3}{3}f'''(x) + \cdots$

To eliminate the $f''(x)$ term, multiply equation (1) by 4 and subtract equation (2):

$$
4f(x+h) - f(x+2h) = 3f(x) + 2hf'(x) - \frac{2h^3}{3}f'''(\xi)
$$

Solving for $f'(x)$:

$$
2hf'(x) = -3f(x) + 4f(x+h) - f(x+2h) + \frac{2h^3}{3}f'''(\xi)
$$

$$
f'(x_n) = \frac{-3f_n + 4f_{n+1} - f_{n+2}}{2h}, \qquad \text{error } O(h^2)
$$

### 5. Three-Point Backward Difference ($O(h^2)$)

By reflecting the points backward ($x$, $x-h$, $x-2h$), we get the counterpart for the end of a table:

$$
f'(x_n) = \frac{3f_n - 4f_{n-1} + f_{n-2}}{2h}, \qquad \text{error } O(h^2)
$$

### 6. Five-Point Central Difference ($O(h^4)$)

If you have two points available on each side ($x-2h, x-h, x, x+h, x+2h$), you can cancel out both the $h^2$ and $h^3$ error terms:

$$
f'(x_n) = \frac{f_{n-2} - 8f_{n-1} + 8f_{n+1} - f_{n+2}}{12h}, \qquad \text{error } O(h^4)
$$

Notice the pattern of coefficients in the numerator: $+1, -8, 0, +8, -1$, divided by $12h$. It achieves an impressive $O(h^4)$ truncation error.

---

## 📊 Summary of Difference Formulas

Here is the complete menu of first-derivative difference formulas:

| Formula Name | Algebraic Expression | Nodes Needed | Truncation Error | Where to Use |
| :--- | :--- | :--: | :--: | :--- |
| **Two-point forward** | $\displaystyle f'(x_n) = \frac{f_{n+1} - f_n}{h}$ | $n, n+1$ | $O(h)$ | Left boundary (rough estimate) |
| **Two-point backward** | $\displaystyle f'(x_n) = \frac{f_n - f_{n-1}}{h}$ | $n-1, n$ | $O(h)$ | Right boundary (rough estimate) |
| **Three-point central** | $\displaystyle f'(x_n) = \frac{f_{n+1} - f_{n-1}}{2h}$ | $n-1, n+1$ | $O(h^2)$ | Interior points (standard choice) |
| **Three-point forward** | $\displaystyle f'(x_n) = \frac{-3f_n + 4f_{n+1} - f_{n+2}}{2h}$ | $n, n+1, n+2$ | $O(h^2)$ | Left boundary ($O(h^2)$ accuracy) |
| **Three-point backward** | $\displaystyle f'(x_n) = \frac{3f_n - 4f_{n-1} + f_{n-2}}{2h}$ | $n-2, n-1, n$ | $O(h^2)$ | Right boundary ($O(h^2)$ accuracy) |
| **Five-point central** | $\displaystyle f'(x_n) = \frac{f_{n-2} - 8f_{n-1} + 8f_{n+1} - f_{n+2}}{12h}$ | $n-2, \dots, n+2$ | $O(h^4)$ | Interior points (high accuracy) |

---

## ⚡ Second-Derivative Formulas (Function-Value Form)

We can also express the second derivative directly in terms of tabulated function values (Jain §6.2.3):

| Direction | First Derivative Formula | Second Derivative Formula | Error |
| :--- | :--- | :--- | :--: |
| **Forward (3-pt)** | $\displaystyle y'_i = \frac{-y_{i+2} + 4y_{i+1} - 3y_i}{2h}$ | $\displaystyle y''_i = \frac{y_i - 2y_{i+1} + y_{i+2}}{h^2}$ | $O(h)$ |
| **Backward (3-pt)** | $\displaystyle y'_i = \frac{3y_i - 4y_{i-1} + y_{i-2}}{2h}$ | $\displaystyle y''_i = \frac{y_i - 2y_{i-1} + y_{i-2}}{h^2}$ | $O(h)$ |
| **Central (3-pt)** | $\displaystyle y'_i = \frac{y_{i+1} - y_{i-1}}{2h}$ | $\displaystyle y''_i = \frac{y_{i-1} - 2y_i + y_{i+1}}{h^2}$ | $O(h^2)$ |
| **Central (5-pt)** | $\displaystyle y'_i = \frac{-y_{i+2} + 8y_{i+1} - 8y_{i-1} + y_{i-2}}{12h}$ | $\displaystyle y''_i = \frac{-y_{i+2} + 16y_{i+1} - 30y_i + 16y_{i-1} - y_{i-2}}{12h^2}$ | $O(h^4)$ |

> [!WARNING] Watch Out for Subtractive Cancellation
> Look closely at what the central difference numerator is doing: $[f_{n+1} - f_{n-1}] / (2h)$.
>
> When the step size $h$ is small, $f_{n+1}$ and $f_{n-1}$ are almost identical numbers. When you subtract two numbers that share their first four or five significant digits, those leading digits cancel out and vanish! The difference consists mostly of round-off noise.
>
> Then, you divide that noisy difference by a tiny number $2h$, which blows the error up by a factor of $1/(2h)$.
>
> For second derivatives, you divide by $h^2$, blowing up round-off errors even faster!
>
> This creates a fundamental trade-off:
> - Making $h$ smaller reduces **truncation error** ($O(h^2)$ shrinks).
> - Making $h$ smaller increases **round-off error** ($\epsilon / h$ grows).
>
> There is an optimal step size $h_{\text{opt}}$. Making $h$ smaller than that optimal value makes your answer worse, not better!

---

## 🏆 Past Exam Questions

### 2019 Q.6(a): Basis of Numerical Differentiation & Four Difference Equations [04 Marks]

**The question:** What is the basis of numerical differentiation? Write at least four difference equations to obtain numerical differentiation.

**Let's answer this step by step like an exam tutor.**

**1. The basis of numerical differentiation:**
A function known only at discrete tabulated points is replaced by an interpolating polynomial that passes through those points, and the derivative of that polynomial is used as the approximation for the derivative of the function.

Starting from the Taylor series expansions of neighboring points:

$$
f(x + h) = f(x) + hf'(x) + \frac{h^2}{2}f''(x) + \frac{h^3}{6}f'''(x) + \cdots
$$

linear combinations of the series at neighboring points cancel unwanted terms. Since the first omitted term is proportional to a power of $h$, the result is an approximation with a truncation error of order $O(h)$, $O(h^2)$, or $O(h^4)$.

**2. Four difference equations:**
Let $h$ be the uniform tabular spacing and $f_n = f(x_n)$:

1. **Two-point forward difference:**
$$
f'(x_n) = \frac{f_{n+1} - f_n}{h}, \qquad \text{error } O(h)
$$

2. **Two-point backward difference:**
$$
f'(x_n) = \frac{f_n - f_{n-1}}{h}, \qquad \text{error } O(h)
$$

3. **Three-point central difference:**
$$
f'(x_n) = \frac{f_{n+1} - f_{n-1}}{2h}, \qquad \text{error } O(h^2)
$$

4. **Three-point forward difference:**
$$
f'(x_n) = \frac{-3f_n + 4f_{n+1} - f_{n+2}}{2h}, \qquad \text{error } O(h^2)
$$

5. **Five-point central difference:**
$$
f'(x_n) = \frac{f_{n-2} - 8f_{n-1} + 8f_{n+1} - f_{n+2}}{12h}, \qquad \text{error } O(h^4)
$$

The central formulas are preferred whenever data exists on both sides of the point, because their symmetric error is $O(h^2)$ or $O(h^4)$ rather than $O(h)$, and their error constants are significantly smaller.

---

## ⚡ Quick Review

**The method in one sentence:** Numerical differentiation calculates derivatives of discrete data by differentiating an interpolating polynomial or by combining Taylor expansions to cancel error terms.

**The key formulas you must memorize:**
- Central first derivative (3-point):
$$
f'(x_n) = \frac{f_{n+1} - f_{n-1}}{2h}
$$
- Central second derivative (3-point):
$$
f''(x_n) = \frac{f_{n-1} - 2f_n + f_{n+1}}{h^2}
$$
- Central first derivative (5-point):
$$
f'(x_n) = \frac{f_{n-2} - 8f_{n-1} + 8f_{n+1} - f_{n+2}}{12h}
$$

**The most common exam mistake:** Forgetting the $2$ in the denominator of the central first derivative ($2h$, not $h$) or forgetting that the second derivative divides by $h^2$.

**Time estimate in exam:** 5 to 7 minutes for a 4-mark theoretical question.

---

## 🔗 Connected Topics

- [← NM-6.3: Tabulated Optima](../NM-6_Optimization/NM-6.3_Tabulated_Optima.md) -- finding maxima and minima by identifying where numerical derivatives equal zero.
- [→ NM-7.2: First Derivative](NM-7.2_First_Derivative.md) -- applying these difference formulas to numerical tables and real exam datasets.
- [NM-1.6: Taylor Series](../NM-1_Error_Analysis/NM-1.6_Taylor_Series.md) -- the foundational series expansion used to derive all difference formulas.

---

[← Previous: NM-6.3 Tabulated Optima](../NM-6_Optimization/NM-6.3_Tabulated_Optima.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: NM-7.2 First Derivative →](NM-7.2_First_Derivative.md)
