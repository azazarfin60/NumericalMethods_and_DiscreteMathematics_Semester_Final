[← Previous: NM-2.4 Newton-Raphson](NM-2.4_Newton_Raphson.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: NM-2.6 Method Comparison →](NM-2.6_Method_Comparison.md)

---

# NM-2.5: Secant Method

> 🟠 **Priority:** Secondary | **Tested:** 2 appearances | **Typical marks:** 4

## What This Is (and Why It Matters)

Newton-Raphson is fantastic, but it has one big catch: you must calculate the derivative $f'(x)$. In real-world engineering, you might be reading data from sensors, running a massive circuit simulation sub-routine, or dealing with an ugly equation whose derivative takes an entire page of algebra to differentiate.

The **Secant Method** solves this by mimicking Newton-Raphson without ever taking a derivative. Instead of using the exact tangent slope, it approximates the slope using a finite-difference chord between your two most recent points. You get nearly all of Newton's blistering speed (order of convergence is $1.618$ -- the golden ratio!) with only a single function evaluation per step. 

In RUET examinations, this method appears as a computational problem (such as 2017 Q.2(c) asking for four iterations on a cubic polynomial) or as the key alternative to Newton when discussing derivative-related limitations.

---

## 📝 Key Definitions

> **Secant derivative approximation:** "the derivative at $x_i$ is approximated by the formula $f'(x_i) \approx \frac{f(x_i) - f(x_{i-1})}{x_i - x_{i-1}}$." -- Jain, §2.7 (p. 49)
> 
> **In simple words:** Replacing the exact calculus derivative with the rise-over-run slope connecting your last two calculated points.

> **Secant formula:** "$x_{i+1} = x_i - \frac{f_i(x_i - x_{i-1})}{f_i - f_{i-1}} = \frac{x_{i-1}f_i - x_i f_{i-1}}{f_i - f_{i-1}}$." -- Jain, §2.7 (p. 49)
> 
> **In simple words:** The Newton-Raphson formula with the finite-difference slope plugged in. It uses your two most recent guesses to predict the next one.

> **Order of convergence $1.618$:** The theoretical rate at which errors decrease in the Secant method: $\varepsilon_{n+1} \approx C \varepsilon_n^{1.618}$, where $1.618 = \frac{1 + \sqrt{5}}{2}$ is the golden ratio.
> 
> **In simple words:** It is superlinear -- much faster than bisection (which is order 1), and almost as fast as Newton (order 2), without needing any derivatives.

---

## The Core Idea

Where does the formula come from? Start with the familiar Newton-Raphson update:
$$
x_{i+1} = x_i - \frac{f(x_i)}{f'(x_i)}
$$

Now suppose you cannot evaluate $f'(x_i)$. Approximate the derivative using the two most recent approximations, $x_i$ and $x_{i-1}$:
$$
f'(x_i) \approx \frac{f(x_i) - f(x_{i-1})}{x_i - x_{i-1}} = \frac{f_i - f_{i-1}}{x_i - x_{i-1}}
$$

Substitute this slope approximation directly into the denominator of Newton's formula:
$$
x_{i+1} = x_i - \frac{f_i}{\left(\frac{f_i - f_{i-1}}{x_i - x_{i-1}}\right)} = x_i - \frac{f_i(x_i - x_{i-1})}{f_i - f_{i-1}}
$$
Putting this over a common denominator gives the symmetrical form:
$$
x_{i+1} = \frac{x_{i-1}f_i - x_i f_{i-1}}{f_i - f_{i-1}}
$$

> [!NOTE] Two Initial Guesses Required
> Unlike Newton-Raphson (which needs only one guess $x_0$), the Secant method requires two initial guesses, $x_0$ and $x_1$, to compute that very first finite-difference slope.

### Secant vs. Newton-Raphson: A Fair Comparison

Students often ask: "If Newton is order 2 and Secant is order 1.618, isn't Newton always better?" Not necessarily! Look at the computational cost per step:

| Feature | Newton-Raphson | Secant Method |
| :-- | :-- | :-- |
| **Slope calculated from** | Exact calculus derivative $f'(x)$ | Finite difference of last two iterates |
| **Initial starting guesses** | One ($x_0$) | Two ($x_0$ and $x_1$) |
| **Evaluations per iteration** | **2 evaluations:** $f(x)$ and $f'(x)$ | **1 evaluation:** only $f(x_{i+1})$ ($f_{i-1}$ is saved!) |
| **Convergence order ($p$)** | $2.0$ (quadratic) | $1.618$ (superlinear) |
| **Bracket required?** | No (open method) | No (open method) |
| **Can it diverge?** | Yes | Yes |

Notice that Secant evaluates only ONE new function value per iteration, because the previous value $f(x_{i-1})$ is already saved in memory from the previous step. In problems where evaluating a function takes time, Secant can actually find the root in less total computer time than Newton!

### Secant vs. False Position: Identical Algebra, Different Update Rules!

If you look closely at the math, the Secant formula is algebraically identical to the False Position formula:
$$
x_{\text{new}} = \frac{a f(b) - b f(a)}{f(b) - f(a)}
$$
So what is the difference? The update rule!
- **False Position (Regula Falsi):** Checks signs ($f(a)f(c) < 0$) and keeps whichever old endpoint preserves the bracket. One endpoint can stay frozen forever.
- **Secant Method:** Throws the bracket away completely. It **always discards the oldest point** ($x_{i-1}$) and adopts the newest point, regardless of sign.
Because it always moves forward with the freshest data, Secant never suffers from one-sided stagnation. However, because it discards the bracket, it can occasionally overshoot or diverge.

---

## 🔧 Worked Example

> **Question:** Find the positive root of the equation $f(x) = x^3 - 3x^2 - x - 3 = 0$ by the secant method. Use four iterations only.
> 
> *(Source: 2017 Q.2(c) [Marks: 04])*

**Let's solve this step by step.**

**Step 1. Locate the positive root with a sign check:**
Let's evaluate $f(x) = x^3 - 3x^2 - x - 3$:
- $f(0) = -3$
- $f(1) = 1 - 3 - 1 - 3 = -6$
- $f(2) = 8 - 12 - 2 - 3 = -9$
- $f(3) = 27 - 27 - 3 - 3 = -6$
- $f(4) = 64 - 48 - 4 - 3 = +9$

The function changes sign between $x = 3$ and $x = 4$. To demonstrate the method over four steps, let's take the initial guesses:
$$
x_0 = 2 \implies f_0 = f(2) = -9
$$
$$
x_1 = 3 \implies f_1 = f(3) = -6
$$

**Step 2. Set up the secant recurrence relation:**
$$
x_{n+1} = x_n - \frac{f(x_n)(x_n - x_{n-1})}{f(x_n) - f(x_{n-1})}
$$

**Step 3. Execute the 4 required iterations:**

- **Iteration 1 ($n = 1$ to find $x_2$):**
$$
x_2 = 3 - \frac{(-6)(3 - 2)}{(-6) - (-9)} = 3 - \frac{-6}{3} = 3 + 2 = 5.000000
$$
Now evaluate $f(x_2)$ at $x_2 = 5$:
$$
f(5) = 5^3 - 3(5)^2 - 5 - 3 = 125 - 75 - 5 - 3 = 42.000000
$$

- **Iteration 2 ($n = 2$ to find $x_3$ using $x_1 = 3, x_2 = 5$):**
$$
x_3 = 5 - \frac{42(5 - 3)}{42 - (-6)} = 5 - \frac{84}{48} = 5 - 1.75 = 3.250000
$$
Evaluate $f(x_3)$ at $x_3 = 3.25$:
$$
f(3.25) = (3.25)^3 - 3(3.25)^2 - 3.25 - 3 = 34.328125 - 31.6875 - 6.25 = -3.609375
$$

- **Iteration 3 ($n = 3$ to find $x_4$ using $x_2 = 5, x_3 = 3.25$):**
$$
x_4 = 3.25 - \frac{(-3.609375)(3.25 - 5)}{(-3.609375) - 42} = 3.25 - \frac{(-3.609375)(-1.75)}{-45.609375} = 3.25 - \frac{6.316406}{-45.609375}
$$
$$
x_4 = 3.25 + 0.138489 = 3.388489
$$
Evaluate $f(x_4)$ at $x_4 = 3.388489$:
$$
f(3.388489) = (3.388489)^3 - 3(3.388489)^2 - 3.388489 - 3 \approx -1.927914
$$

- **Iteration 4 ($n = 4$ to find $x_5$ using $x_3 = 3.25, x_4 = 3.388489$):**
$$
x_5 = 3.388489 - \frac{(-1.927914)(3.388489 - 3.25)}{(-1.927914) - (-3.609375)} = 3.388489 - \frac{(-1.927914)(0.138489)}{1.681461}
$$
$$
x_5 = 3.388489 + \frac{0.266995}{1.681461} = 3.388489 + 0.158787 = 3.547276
$$
Evaluating $f(3.547276) \approx +0.339189$.

**Iteration summary table:**

| Iteration | $x_n$ | $f(x_n)$ |
| :--: | :--: | :--: |
| 1 | 5.000000 | $+42.000000$ |
| 2 | 3.250000 | $-3.609375$ |
| 3 | 3.388489 | $-1.927914$ |
| 4 | 3.547276 | $+0.339189$ |

$$
\boxed{x \approx 3.547 \text{ after four iterations}}
$$

> [!NOTE] "Use Four Iterations Only"
> Notice that the problem explicitly says: *"Use four iterations only."* The examiner is not asking you to iterate until convergence, but to demonstrate your mastery of the four sequential arithmetic updates. The exact root of this cubic is $x \approx 3.525102$, and after four steps our sequence has narrowed to $3.547$.

> [!WARNING] The Non-Monotone Nature of Secant
> Look at the sequence of guesses: $5.0000 \to 3.2500 \to 3.3885 \to 3.5473$. The iterates jump above the root, drop below, and then climb back up. Unlike bisection, secant convergence is not monotonic! Do not panic if an iterate overshoots your expected value in step 1.

---

## 🏆 Past Exam Questions

### 2017 Q.2(c): Positive Root via Secant Method [04 marks]

**The question:** Find the positive root of the equation $f(x) = x^3 - 3x^2 - x - 3 = 0$ by secant method (Use four iterations only).

**How to answer like a top student:**
Follow the complete worked solution shown above:
1. Show the sign check on $f(x)$ to establish the existence of a positive root.
2. State the secant iteration formula clearly.
3. Compute the four iterations $x_2, x_3, x_4, x_5$ showing intermediate values.
4. Tabulate all four iterations.
5. Provide the boxed result matching the origin:

$$
\boxed{x \approx 3.547 \text{ after four iterations}}
$$

*(Note on exam question print: In the original 2017 question paper, the constant term is printed faintly and could potentially be read as $-1$. If solved as $x^3 - 3x^2 - x - 1 = 0$, the same start $x_0 = 2, x_1 = 3$ yields $x \approx 3.3888$ after four steps. The $-3$ reading is the standard textbook problem and provides the cleaner arithmetic presented here).*

---

## ⚡ Quick Review

**The method in one sentence:** The Secant method replaces the calculus derivative in Newton-Raphson with a finite difference between the two most recent iterates, delivering superlinear speed without derivatives.

**The formula you must memorize:**
$$
x_{n+1} = x_n - \frac{f(x_n)(x_n - x_{n-1})}{f(x_n) - f(x_{n-1})} = \frac{x_{n-1}f(x_n) - x_n f(x_{n-1})}{f(x_n) - f(x_{n-1})}
$$

**The most common exam mistake:** Mixing up the subscripts in the numerator. Writing $x_n f(x_n) - \dots$ will ruin the entire calculation. Always remember: the $x$-subscript and the $f$-subscript are opposites ($x_{n-1} f_n - x_n f_{n-1}$).

**Time estimate in exam:** 8–10 minutes for a 4-iteration numerical problem.

---

## 🔗 Connected Topics

- [← NM-2.4: Newton-Raphson Method](NM-2.4_Newton_Raphson.md) -- Secant is simply Newton-Raphson with an approximated derivative.
- [NM-2.3: False Position and Regula Falsi](NM-2.3_False_Position.md) -- uses the exact same chord equation, but enforces a sign-changing bracket.
- [→ NM-2.6: Method Comparison and Convergence](NM-2.6_Method_Comparison.md) -- comparing Secant's order $1.618$ against Bisection and Newton.
- [NM-2.7: Polynomial Roots](NM-2.7_Polynomial_Roots.md) -- solving higher-degree polynomials and evaluating multiple roots.

---

[← Previous: NM-2.4 Newton-Raphson](NM-2.4_Newton_Raphson.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: NM-2.6 Method Comparison →](NM-2.6_Method_Comparison.md)
