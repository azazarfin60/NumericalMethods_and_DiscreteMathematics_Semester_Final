[📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: NM-2.2 Bisection Method →](NM-2.2_Bisection_Method.md)

---

# NM-2.1: Fundamentals and Classification of Root Finding

> 🔴 **Priority:** Critical | **Tested:** 4/8 years | **Typical marks:** 2–4

## What This Is (and Why It Matters)

Whenever an engineering equation has the unknown variable trapped where simple algebra cannot rescue it -- like a diode voltage sitting inside an exponential and outside it simultaneously -- you have to find a root numerically. 

A root is simply any value of $x$ that makes $f(x) = 0$. Finding it numerically means starting with a guess and refining it step by step until you are as close to zero as you need to be. In the exam, this topic provides easy theory marks. Examiners regularly ask you to define an iterative method, list the generalized steps, or compare the two great families of root finders: **bracketing methods** and **open methods**.

---

## 📝 Key Definitions

> **Root of an equation:** "In scientific and engineering studies, a frequently occurring problem is to find the roots of equations of the form $f(x) = 0$." -- Jain, §2.1 (p. 22)
> 
> **In simple words:** A root is the exact point on the horizontal axis where a curve crosses or touches zero. If you plug that number into the function, you get zero out.

> **Polynomial:** "algebraic functions of the form $f_n(x) = a_0x^n + a_1x^{n-1} + a_2x^{n-2} + \cdots + a_{n-1}x + a_n$ are called *polynomials*." -- Jain, §2.1 (p. 22)
> 
> **In simple words:** An equation built purely out of non-negative integer powers of $x$ and constants, like $x^3 - 6x^2 + 11x - 6 = 0$.

> **Transcendental function:** "A non-algebraic function is called a *transcendental function*, e.g., $f(x) = \ln x^3 - 0.7$, $\phi(x) = e^{-0.5x} - 5x$, $\psi(x) = \sin^2 x - x^2 - 2$, etc." -- Jain, §2.1 (p. 22)
> 
> **In simple words:** Any equation containing functions that go beyond simple algebra, such as sines, cosines, logs, or exponentials.

> **Iterative method:** A procedure that generates a sequence of successive approximations $x_0, x_1, x_2, \dots$ according to a fixed algorithmic rule, converging toward the true root $x^*$.
> 
> **In simple words:** An algorithmic guess-and-check loop where every new guess is calculated from the previous one, getting closer to the true answer on every lap.

> **Bracketing method:** An iterative root-finding method that begins with two points enclosing a sign change, shrinking the interval on each cycle while keeping the root trapped inside.
> 
> **In simple words:** A safe trap. You start with two points on opposite sides of the horizontal axis, and you squeeze the walls inward without ever letting the root escape.

> **Open method:** A root-finding algorithm that begins with one or two starting estimates without enclosing the root in a guaranteed interval.
> 
> **In simple words:** A fast leap. You start from a guess and follow a mathematical formula (like a tangent slope) wherever it leads. It runs much faster, but if your guess is poor, it can fly off into nowhere.

---

## The Core Idea

All root-finding algorithms share one ultimate goal: solving $f(x) = 0$. But how they hunt down that root divides the entire subject into two distinct camps.

### The Great Divide: Bracketing vs. Open Methods

The exam asks about this comparison frequently (2022 Q.1(a), 2021 Q.2(a), 2020 Q.2(a)). Here is how the two families compare side by side:

| Feature | Bracketing Methods | Open Methods |
| :-- | :-- | :-- |
| **Initial data required** | An interval $[a, b]$ where $f(a) \cdot f(b) < 0$ | One starting guess $x_0$ (or two for secant) |
| **Information used** | Signs and values of $f(x)$ | Function value $f(x)$ and derivative $f'(x)$ |
| **Convergence guarantee** | Guaranteed 100% for continuous functions | No guarantee; can diverge if start is poor |
| **Speed of convergence** | Slow (linear, $O(h)$) | Very fast (quadratic for Newton, order 1.618 for Secant) |
| **Can it escape the root?** | Never; root remains trapped inside | Yes; can cycle or shoot off to infinity |
| **Standard examples** | Bisection, False Position (Regula Falsi) | Newton-Raphson, Secant Method |

Think of it this way: bracketing is like walking toward an animal inside a fenced cage (safe, certain, but slow). Open methods are like tracking an animal in an open safari (much faster if you spot it right away, but you might run off in the wrong direction).

### Why Sign Changes Guarantee a Root: The Intermediate Value Theorem

If a continuous curve $f(x)$ has $f(a) < 0$ and $f(b) > 0$, the curve must cross the horizontal axis at least once between $a$ and $b$. That means $f(a) \cdot f(b) < 0$ is the universal green light for bracketing algorithms.

> [!WARNING] The Even-Multiplicity Blind Spot
> If a curve touches the horizontal axis without crossing it -- like $f(x) = (x - 2)^2$ at $x = 2$ -- both $f(a)$ and $f(b)$ will have positive signs ($f(a) \cdot f(b) > 0$). Bracketing methods cannot detect this root and will reject the interval. Open methods like Newton-Raphson are needed to locate multiple roots.

### Four Important Ways to Classify Roots

Examiners love to ask you to define and distinguish types of roots:
1. **Simple root:** A root where $f(x^*) = 0$ but $f'(x^*) \ne 0$. The curve crosses cleanly through the axis.
2. **Multiple root:** A root where $f(x^*) = 0$ and $f'(x^*) = 0$. The curve touches or flattens at the axis. This slows down methods like Newton-Raphson.
3. **Explicit root:** A root that can be written down directly as a closed algebraic formula, such as $x = \sqrt{2}$.
4. **Implicit root:** A root that cannot be expressed in a finite formula, such as $x^5 - x - 1 = 0$, requiring numerical iteration.

---

## The Generalized Iterative Framework

A direct method (like the quadratic formula) solves an equation in a single, closed-form algebraic step. An iterative method generates a sequence of numbers ($x_0 \to x_1 \to x_2 \to \dots$) that approaches the target.

### The 8 Generalized Steps (2019 Q.2(a))

When an exam question asks for the generalized steps to solve nonlinear equations iteratively, write down this standard 8-step recipe:

1. **Formulate the problem:** Rearrange the original equation into the canonical form $f(x) = 0$.
2. **Locate the interval:** Scan values to identify sign changes, confirming where roots exist.
3. **Choose initial guesses:** Select a starting value $x_0$ (or a bracketing pair $a, b$).
4. **Establish the iteration formula:** Derive or state the update rule $x_{k+1} = g(x_k)$.
5. **Execute the iterations:** Compute successive values and record them in a neat table.
6. **Check stopping criteria:** Evaluate error after each step to decide when the solution is accurate enough.
7. **Handle failure or stalling:** If iterates diverge or stall, restart with a closer guess or switch methods.
8. **Verify the final result:** Substitute the calculated value back into $f(x) = 0$ to verify the residual is practically zero.

### Three Ways to Know When to Stop

Never iterate blindly. In your answers, always state which stopping criterion you are using:

1. **Step-size tolerance:**
$$
|x_{k+1} - x_k| < \varepsilon
$$
2. **Residual tolerance:**
$$
|f(x_k)| < \varepsilon
$$
3. **Relative percentage error tolerance:**
$$
\varepsilon_a = \left|\frac{x_{k+1} - x_k}{x_{k+1}}\right| \times 100\% < \varepsilon_s
$$

> [!TIP] Testing the Residual vs. the Step Size
> Checking the residual $|f(x_k)|$ is safer than checking only the step size. If an algorithm stalls near a flat region where the derivative is tiny, the step $|x_{k+1} - x_k|$ can look small even while you are still far from zero. Checking $|f(x_k)|$ ensures you are actually on the axis.

---

## 🔧 Worked Example

> **Question:** Classify the four standard root-finding methods (Bisection, False Position, Secant, Newton-Raphson) by method family, starting requirements, need for derivatives, and convergence guarantee.

**Let's solve this step by step.**

**Step 1. Identify the bracketing methods.**
Bisection and False Position (Regula Falsi) both require an interval $[a, b]$ where the function changes sign ($f(a) \cdot f(b) < 0$). They maintain this bracket throughout, so they are guaranteed to converge for any continuous function.

**Step 2. Identify the open methods.**
Secant and Newton-Raphson do not maintain a bracket. Newton-Raphson starts with a single point $x_0$ and evaluates the analytic derivative $f'(x)$. Secant starts with two points $x_0, x_1$ and approximates the derivative using a finite-difference chord. Neither has a guaranteed convergence.

**Step 3. Summarize in the standard exam comparison table:**

| Method | Family | Starting Data | Needs Derivative $f'$? | Convergence Order | Guaranteed? |
| :-- | :-- | :-- | :--: | :--: | :--: |
| **Bisection** | Bracketing | Interval $[a, b]$ with $f(a)f(b) < 0$ | No | 1 (linear) | Yes |
| **False Position** | Bracketing | Interval $[a, b]$ with $f(a)f(b) < 0$ | No | 1 (linear) | Yes |
| **Secant** | Open | Two initial points $x_0, x_1$ | No | 1.618 (superlinear) | No |
| **Newton-Raphson** | Open | One initial point $x_0$ | **Yes** | 2 (quadratic) | No |

---

## 🏆 Past Exam Questions

### 2019 Q.2(a): Define iterative method. Name the iterative methods to solve nonlinear equations. Write the generalized steps to solve nonlinear equations using iterative methods. [04 marks]

**How to answer like a top student:**
Deliver a crisp definition, provide a bulleted list of methods, and present the 8 generalized steps clearly.

**Solution:**

**Definition:**
An **iterative method** is a mathematical procedure that solves an equation $f(x) = 0$ by generating a sequence of successive approximations $x_0, x_1, x_2, \dots$ from one or more initial guesses according to a specific recurrence relation. The iteration continues until the difference between consecutive values or the function residual falls below a prescribed tolerance.

**Names of iterative methods for nonlinear equations:**
1. Bisection Method
2. False Position Method (Regula Falsi)
3. Newton-Raphson Method
4. Secant Method
5. Fixed-Point Iteration Method
6. Lin-Bairstow Method (for polynomial roots)

**Generalized steps to solve nonlinear equations:**
1. **Formulation:** Express the equation in the standard form $f(x) = 0$.
2. **Interval location:** Locate an interval containing roots by evaluating sign changes ($f(a) \cdot f(b) < 0$).
3. **Initialization:** Select suitable initial approximations (either a bracket $[a, b]$ or starting values $x_0, x_1$).
4. **Formula derivation:** Derive or set up the iteration formula $x_{k+1} = g(x_k)$.
5. **Execution:** Compute successive approximations systematically, tracking values in a calculation table.
6. **Convergence testing:** After each iteration, evaluate stopping criteria such as $|x_{k+1} - x_k| < \varepsilon$ or $|f(x_k)| < \varepsilon$.
7. **Error handling:** If iterations fail to converge or oscillate, choose closer initial values or switch algorithms.
8. **Verification:** Substitute the final calculated root back into the original equation $f(x) = 0$ to verify that the residual is negligible.

---

### 2021 Q.2(a): Define bracketing methods with example. [02 marks, CO: 1]

**How to answer like a top student:**
Give the formal condition ($f(a)f(b) < 0$), cite the Intermediate Value Theorem, state the key property, and give standard examples.

**Solution:**

A **bracketing method** is an iterative root-finding algorithm that starts with an initial interval $[a, b]$ where the function values have opposite signs:
$$
f(a) \cdot f(b) < 0
$$
By the Intermediate Value Theorem, if $f(x)$ is continuous on $[a, b]$, there is guaranteed to be at least one root within the interval. At each iteration, the method evaluates an intermediate point and replaces one of the bounds such that the opposite-sign condition is preserved, continuously narrowing the interval around the root.

**Key properties:**
- Convergence is mathematically guaranteed for any continuous function.
- Requires only function evaluations and sign tests; no derivatives are needed.

**Examples:**
- **Bisection Method:** Evaluates the midpoint $c = \frac{a + b}{2}$.
- **False Position Method (Regula Falsi):** Evaluates the chord intercept $c = \frac{a f(b) - b f(a)}{f(b) - f(a)}$.

$$
\boxed{\text{Enclose the root in a sign-changing interval and keep halving it; convergence is guaranteed}}
$$

---

### 2022 Q.1(a): What is the difference between open and bracketing method of root finding? [02 marks, CO: 1]

**How to answer like a top student:**
A structured table with a concluding summary sentence gets full marks immediately.

**Solution:**

| Feature | Bracketing Method | Open Method |
| :-- | :-- | :-- |
| **Starting requirement** | Requires two points $a, b$ bracketing a sign change ($f(a)f(b) < 0$) | Requires one point $x_0$ (or two points without sign constraint) |
| **Convergence** | Always guaranteed to converge for continuous functions | Not guaranteed; may diverge if the initial guess is far from the root |
| **Speed / Order** | Slower; linear convergence ($p = 1$) | Fast; superlinear ($p = 1.618$) or quadratic ($p = 2$) |
| **Derivative needed?** | No derivatives required; only signs and function values | Often requires evaluation of the derivative $f'(x)$ |
| **Examples** | Bisection Method, Regula Falsi Method | Newton-Raphson Method, Secant Method |

$$
\boxed{\text{bracketing encloses the root and always converges; open methods start free and may not}}
$$

---

## ⚡ Quick Review

**The method in one sentence:** Bracketing methods trap the root in a guaranteed sign-changing interval, while open methods follow slopes rapidly from an initial guess without a safety net.

**The formula you must memorize:**
$$
f(a) \cdot f(b) < 0
$$

**The most common exam mistake:** Forgetting that bracketing methods fail to locate even-multiplicity roots (such as $f(x) = (x - 2)^2$), because the curve touches the axis without changing sign.

**Time estimate in exam:** 3–5 minutes for a short theory or classification question.

---

## 🔗 Connected Topics

- [← NM-1.6: Taylor Series and Truncation Error](../NM-1_Error_Analysis/NM-1.6_Taylor_Series.md) -- Taylor series expansions provide the mathematical foundation for open methods.
- [→ NM-2.2: Bisection Method](NM-2.2_Bisection_Method.md) -- the simplest and safest bracketing method.
- [NM-2.4: Newton-Raphson Method](NM-2.4_Newton_Raphson.md) -- the premier open method with quadratic convergence.
- [NM-2.6: Method Comparison and Convergence](NM-2.6_Method_Comparison.md) -- the master comparison table among all four root-finding methods.

---

[← Previous: NM-1.6 Taylor Series](../NM-1_Error_Analysis/NM-1.6_Taylor_Series.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: NM-2.2 Bisection Method →](NM-2.2_Bisection_Method.md)
