[← Previous: NM-2.6 Method Comparison](NM-2.6_Method_Comparison.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: NM-3 Linear Systems Overview →](../NM-3_Linear_Systems/_Topic_Overview.md)

---

# NM-2.7: Roots of Polynomials

> 🟠 **Priority:** Secondary | **Tested:** 2 appearances | **Typical marks:** 4–6

## What This Is (and Why It Matters)

Polynomials are special. Unlike generic equations with tangled sines, cosines, and logarithms, a polynomial of degree $n$ plays by rigid mathematical rules: it has exactly $n$ roots, its roots can be bounded using Descartes' Rule of Signs, and an integer scan can often expose exact roots before you even begin iterating.

In RUET examinations, polynomial root-finding appears in two distinct ways:
1. **Circuit equations in disguise:** Real electrical power balance problems like $5I^2 + 50I = 1000$, where you must use an iterative method to find the physical current and explicitly reject unphysical negative roots.
2. **"Find the smallest root":** Questions like 2021 Q.2(c) giving a cubic $x^3 - 9x^2 + 26x - 24 = 0$ worth 6 marks. The trick here is that examiners want more than just factoring: they want you to locate the root with a sign scan, confirm it with an iterative algorithm, and mathematically prove that no smaller root exists.

---

## 📝 Key Definitions

> **Polynomial degree and root count:** "Every polynomial equation of the $n$th degree has $n$ and only $n$ roots." -- Jain, §2.1 (p. 23)
> 
> **In simple words:** A quadratic has 2 roots, a cubic has 3 roots, and an $n$-degree polynomial has exactly $n$ roots (counting real and complex roots).

> **Odd-degree real root theorem:** "If $n$ is odd, the polynomial equation has at least one real root whose sign is opposite to that of the last term." -- Jain, §2.1 (p. 23)
> 
> **In simple words:** Any cubic or fifth-degree curve will definitely cross the real horizontal axis at least once, and you can tell whether that root is positive or negative just by glancing at the constant term.

> **Descartes' Rule of Signs:** "(a) A polynomial equation $f(x) = 0$ cannot have more number of positive real roots than the number of changes of sign in the coefficients of $f(x)$. (b) $f(x) = 0$ cannot have more number of negative real roots than the number of changes of sign in the coefficients of $f(-x)$." -- Jain, §2.1 (p. 23)
> 
> **In simple words:** Count how many times the signs flip ($+ \to -$ or $- \to +$) as you read across the coefficients. That number sets the maximum possible count of positive roots.

> **Smallest root:** The smallest real value of $x$ for which $f(x) = 0$.
> 
> **In simple words:** The leftmost real crossing point on the horizontal axis.

---

## The Core Idea

### Superpower 1: The Integer Sign Scan

Before you apply any numerical method to a polynomial, always construct a quick integer evaluation table from $x = 0$ upward. This takes 60 seconds on your calculator and does two wonderful things:
1. It reveals sign flips, giving you instant, foolproof bracketing intervals.
2. If the polynomial happens to have clean integer roots, the function value evaluates to exactly zero ($f(x) = 0$), revealing the exact root on the spot!

For example, on $f(x) = x^3 - 9x^2 + 26x - 24$:
- $f(0) = -24$
- $f(1) = 1 - 9 + 26 - 24 = -6$
- $f(2) = 8 - 36 + 52 - 24 = 0$ $\to$ Exact root!
- $f(3) = 27 - 81 + 78 - 24 = 0$ $\to$ Exact root!
- $f(4) = 64 - 144 + 104 - 24 = 0$ $\to$ Exact root!

All three roots ($2, 3, 4$) are found before running a single iteration!

### Superpower 2: Descartes' Rule of Signs

Examiners love this theoretical property. Here is how to use it:

Take $f(x) = x^3 - 9x^2 + 26x - 24$:
- Look at the signs of the coefficients: $+1, -9, +26, -24$.
- The signs transition: $(+) \to (-)$ (1st change), $(-) \to (+)$ (2nd change), $(+) \to (-)$ (3rd change).
- Total sign variations = $3$. Therefore, there are either $3$ or $1$ positive real roots.

Now evaluate $f(-x)$:
$$
f(-x) = (-x)^3 - 9(-x)^2 + 26(-x) - 24 = -x^3 - 9x^2 - 26x - 24
$$
- All coefficients are negative: $(-), (-), (-), (-)$.
- Total sign variations = $0$. Therefore, there are **zero negative real roots**!

This immediately tells you not to waste study time looking on the negative axis.

### Physics-Framed Polynomials: Rejecting Unphysical Roots

When an engineering question derives an equation from circuit laws, like:
$$
5I^2 + 50I = 1000
$$
Algebra gives two roots: $I = 10\text{ A}$ and $I = -20\text{ A}$. 

> [!WARNING] The Physical Boundary Condition
> Never leave negative roots unaddressed in circuit problems! Always explicitly state: *"Since current in this physical circuit branch must be positive, $I = -20\text{ A}$ is unphysical and discarded, leaving $I = 10\text{ A}$."* Examiners award marks for recognizing the physical context.

---

## 🔧 Worked Example 1: Circuit Power Balance Equation

> **Question:** Compute current, $I$ from the following power balance equation obtained from an electric circuit by using an iterative method: $5I^2 + 50I = 1000$.
> 
> *(Source: 2019 Q.2(b) [Marks: 04])*

**Let's solve this step by step.**

**Step 1. Formulate in standard form:**
$$
f(I) = 5I^2 + 50I - 1000 = 0
$$
$$
f'(I) = 10I + 50
$$

**Step 2. Algebraic check to know the true target:**
Divide by 5:
$$
I^2 + 10I - 200 = 0 \implies I = \frac{-10 \pm \sqrt{100 - 4(1)(-200)}}{2} = \frac{-10 \pm \sqrt{900}}{2} = \frac{-10 \pm 30}{2}
$$
The roots are $I = 10\text{ A}$ and $I = -20\text{ A}$. The positive physical current is $I = 10\text{ A}$.

**Step 3. Set up the Newton-Raphson iteration formula:**
$$
I_{k+1} = I_k - \frac{f(I_k)}{f'(I_k)} = I_k - \frac{5I_k^2 + 50I_k - 1000}{10I_k + 50}
$$

**Step 4. Select starting value:**
Testing $I_0 = 5$:
- $f(5) = 5(25) + 50(5) - 1000 = 125 + 250 - 1000 = -625 < 0$
- $f'(5) = 10(5) + 50 = 100$
$$
I_1 = 5 - \frac{-625}{100} = 5 + 6.25 = 11.25\text{ A}
$$

**Step 5. Compute iterations:**

| $k$ | $I_k$ | $f(I_k)$ | $f'(I_k)$ | $I_{k+1}$ |
| :--: | :-- | :-- | :-- | :-- |
| 0 | 5.000000 | $-625.0000$ | 100.0000 | 11.250000 |
| 1 | 11.250000 | $+195.3125$ | 162.5000 | 10.048077 |
| 2 | 10.048077 | $+7.2231$ | 150.4808 | 10.000077 |
| 3 | 10.000077 | $+0.0115$ | 150.0008 | 10.000000 |

The last correction is below $10^{-4}$. The iterates settle cleanly on:

$$
\boxed{I = 10\ \text{A}}
$$

**Substitution check:** $5(10)^2 + 50(10) = 500 + 500 = 1000\text{ W}$, exactly matching the right-hand side.

---

## 🔧 Worked Example 2: Determining the Smallest Root of a Cubic

> **Question:** Determine the smallest root of the equation: $f(x) = x^3 - 9x^2 + 26x - 24 = 0$.
> 
> *(Source: 2021 Q.2(c) [Marks: 06, CO: 3])*

**Let's solve this step by step.**

**Step 1. Integer sign scan:**
Evaluate $f(x)$ at integer points:
- $f(0) = -24$ (negative)
- $f(1) = 1 - 9 + 26 - 24 = -6$ (negative)
- $f(2) = 8 - 36 + 52 - 24 = 0$ (exact root!)
- $f(3) = 27 - 81 + 78 - 24 = 0$ (exact root!)
- $f(4) = 64 - 144 + 104 - 24 = 0$ (exact root!)
- $f(5) = 125 - 225 + 130 - 24 = +6$ (positive)

All three roots are exact integers: $x = 2, 3, 4$.
Factoring:
$$
f(x) = (x - 2)(x - 3)(x - 4) = 0
$$

The smallest candidate root is clearly $x = 2$.

**Step 2. Numerical confirmation via Newton-Raphson:**
Because the question belongs to a Numerical Methods examination (worth 6 marks), examiners expect a demonstration of numerical root finding.

Let:
$$
f(x) = x^3 - 9x^2 + 26x - 24, \qquad f'(x) = 3x^2 - 18x + 26
$$
Select initial estimate $x_0 = 1.5$:
- $f(1.5) = (1.5)^3 - 9(1.5)^2 + 26(1.5) - 24 = 3.375 - 20.25 + 39 - 24 = -1.875$
- $f'(1.5) = 3(1.5)^2 - 18(1.5) + 26 = 6.75 - 27 + 26 = 5.75$

Compute iterations:
- **Iteration 1:**
$$
x_1 = 1.5 - \frac{-1.875}{5.75} = 1.5 + 0.326087 = 1.826087
$$
- **Iteration 2:**
  $f(1.826087) \approx -0.443823$, $f'(1.826087) \approx 3.134215$
$$
x_2 = 1.826087 - \frac{-0.443823}{3.134215} = 1.826087 + 0.141606 = 1.967693
$$

**Iteration table:**

| Iteration | $x_n$ | $f(x_n)$ | $f'(x_n)$ |
| :--: | :-- | :-- | :-- |
| 0 | 1.500000 | $-1.875000$ | 5.750000 |
| 1 | 1.826087 | $-0.443823$ | 3.134215 |
| 2 | 1.967693 | $-0.067779$ | 2.196974 |
| 3 | 1.998544 | $-0.002918$ | 2.008742 |
| 4 | 1.999997 | $-0.000006$ | 2.000019 |
| 5 | 2.000000 | 0.000000 | 2.000000 |

**Step 3. Prove that $x = 2$ is strictly the smallest root:**
Why is $x = 2$ the smallest root and not just one of three?
1. **Stationary points of $f(x)$:**
   Set $f'(x) = 3x^2 - 18x + 26 = 0$:
$$
x = \frac{18 \pm \sqrt{(-18)^2 - 4(3)(26)}}{6} = \frac{18 \pm \sqrt{324 - 312}}{6} = \frac{18 \pm \sqrt{12}}{6} = 3 \pm \frac{\sqrt{3}}{3} \approx 2.423, \; 3.577
$$
2. The first turning point occurs at $x \approx 2.423$. Thus, $f(x)$ is strictly increasing on $(-\infty, 2.423)$.
3. For all $x < 2$, since $f(x) = (x-2)(x-3)(x-4)$, all three factors are negative, making $f(x) < 0$ strictly.
4. Because $f(x)$ has no turning points and remains strictly negative on $(-\infty, 2)$, it cannot cross the axis anywhere below $x = 2$.
Therefore, $x = 2$ is guaranteed to be the smallest root.

$$
\boxed{x = 2}
$$

---

## 🏆 Past Exam Questions

### 2019 Q.2(b): Compute current, $I$ from the following power balance equation obtained from an electric circuit by using an iterative method: $5I^2 + 50I = 1000$. [04 marks]

**How to answer like a top student:**
Follow the complete worked solution shown above:
1. Express as $f(I) = 5I^2 + 50I - 1000 = 0$ with $f'(I) = 10I + 50$.
2. Note the quadratic roots are $I = 10$ and $I = -20$, and explain why $I = -20$ is rejected on physical grounds.
3. Choose an initial positive estimate $I_0 = 5$ and set up Newton-Raphson.
4. Show the four-iteration table settling on $I = 10$.
5. Provide the boxed result matching the origin:

$$
\boxed{I = 10\ \text{A}}
$$

---

### 2021 Q.2(c): Determine the smallest root of the equation: $f(x) = x^3 - 9x^2 + 26x - 24 = 0$. [06 marks, CO: 3]

**How to answer like a top student:**
Follow the complete 3-step proof shown above:
1. Show the integer evaluation scan and identify the factorization $(x-2)(x-3)(x-4) = 0$.
2. State $x = 2$ and confirm it numerically with Newton-Raphson starting at $x_0 = 1.5$.
3. Write the turning-point proof showing $f'(x) > 0$ for $x \le 2$ to guarantee that no smaller root exists.
4. Provide the boxed result matching the origin:

$$
\boxed{x = 2}
$$

---

### Exam Variants at a Glance

| Year | What They Asked | Key Answer / Formula |
|:---|:---|:---|
| 2019 Q.2(b) | Current from power balance $5I^2 + 50I = 1000$ (04 marks) | $\boxed{I = 10\ \text{A}}$ (reject unphysical $I = -20$) |
| 2021 Q.2(c) | Smallest root of $x^3 - 9x^2 + 26x - 24 = 0$ (06 marks) | $\boxed{x = 2}$ (scan + Newton + turning point proof) |

---

## ⚡ Quick Review

**The method in one sentence:** For polynomial equations, scan integer signs first to discover roots or narrow brackets, run an iterative solver, and explicitly justify physical roots or proofs of smallest roots.

**The formula you must memorize:**
$$
\text{Descartes' Rule: Count sign flips in } f(x) \text{ for positive roots, } f(-x) \text{ for negative roots}
$$

**The most common exam mistake:** Factoring the cubic in 2 lines and stopping. A 6-mark question expects the numerical iteration table and a mathematical explanation for why 2 is the smallest root!

**Time estimate in exam:** 8–10 minutes for a complete 6-mark polynomial problem.

---

## 🔗 Connected Topics

- [← NM-2.4: Newton-Raphson Method](NM-2.4_Newton_Raphson.md) -- the engine used to converge onto polynomial roots.
- [← NM-2.6: Method Comparison and Convergence](NM-2.6_Method_Comparison.md) -- comparing solver options for polynomial equations.
- [→ NM-3: Linear Systems Overview](../NM-3_Linear_Systems/_Topic_Overview.md) -- moving from single-variable polynomial equations to multi-variable linear algebraic systems.

---

[← Previous: NM-2.6 Method Comparison](NM-2.6_Method_Comparison.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: NM-3 Linear Systems Overview →](../NM-3_Linear_Systems/_Topic_Overview.md)
