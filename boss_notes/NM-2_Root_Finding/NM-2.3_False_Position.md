[← Previous: NM-2.2 Bisection Method](NM-2.2_Bisection_Method.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: NM-2.4 Newton-Raphson →](NM-2.4_Newton_Raphson.md)

---

# NM-2.3: False Position and Regula Falsi

> 🔴 **Priority:** Critical | **Tested:** 5/8 years + CT-01 | **Typical marks:** 4–6

## What This Is (and Why It Matters)

Think of False Position (known classically as *Regula Falsi*, Latin for "rule of false position") as bisection with common sense. 

Bisection blindly cuts an interval right down the center, even if one end is sitting at $f(a) = -0.0001$ (nearly zero!) and the other is up at $f(b) = +1000$. False Position instead connects $(a, f(a))$ and $(b, f(b))$ with a straight line (a chord) and chooses where that chord slices through the horizontal axis as the next guess. Because it accounts for the magnitude of the function values, it usually converges much faster than bisection while keeping the 100% guarantee that the root stays bracketed.

In RUET exams, this is a major topic. You will be asked to derive its chord formula from scratch, write out its algorithmic steps, or compute a table of iterates on problems like $x^{2.2} = 69$.

---

## 📝 Key Definitions

> **Method of false position:** "This is the oldest method for finding the real root of a nonlinear equation $f(x) = 0$ and closely resembles the bisection method. In this method, also known as *regula-falsi* or the *method of chords*, we choose two points $a$ and $b$ such that $f(a)$ and $f(b)$ are of opposite signs... replacing the part of the curve between the points $[a, f(a)]$ and $[b, f(b)]$ by means of the *chord* joining these points, and taking the point of intersection of the chord with the $x$-axis as an *approximation* to the root." -- Jain, §2.3 (p. 28)
> 
> **In simple words:** Connect the two bracket endpoints with a straight chord, see where the chord crosses the horizontal axis, and make that your next guess.

> **Regula falsi:** Latin term meaning "rule of false position" -- the exact same algorithm as the method of chords.
> 
> **In simple words:** The historical name for the false position method.

> **Illinois modification:** A modified version of regula falsi where the function value at an endpoint that fails to update is divided by two ($f \leftarrow \frac{1}{2}f$), preventing one-sided stagnation.
> 
> **In simple words:** A simple fix for stuck endpoints. If one wall of your bracket gets pinned and refuses to move, cut its function height in half so the chord can swing free.

---

## The Core Idea

Here is the geometric intuition behind False Position:

![False Position Geometric Representation](../diagrams/nm2_false_position_geometric.jpg)
*Figure 2.3: The chord connecting $A[a, f(a)]$ and $B[b, f(b)]$ replaces the curve, and its intersection with the $x$-axis gives the next approximation $x_1$.*

### Deriving the False Position Formula (2018 Q.2(b))

Examiners regularly ask you to derive this expression from first principles. Here is the clean 5-step derivation:

**Step 1. Set up the two points:**
Let $x_0$ and $x_1$ be two values such that $f(x_0)$ and $f(x_1)$ have opposite signs ($f_0 \cdot f_1 < 0$). This guarantees that a root lies between them.

**Step 2. Write the two-point straight-line equation:**
The equation of the chord passing through $(x_0, f_0)$ and $(x_1, f_1)$ is:
$$
\frac{y - f_0}{f_1 - f_0} = \frac{x - x_0}{x_1 - x_0}
$$

**Step 3. Find the horizontal axis intercept:**
The chord crosses the $x$-axis where $y = 0$. Let this intersection point be the next approximation, $x_2$:
$$
\frac{0 - f_0}{f_1 - f_0} = \frac{x_2 - x_0}{x_1 - x_0}
$$

**Step 4. Solve for $x_2$:**
Multiply both sides by $(x_1 - x_0)$:
$$
x_2 - x_0 = -\frac{f_0(x_1 - x_0)}{f_1 - f_0}
$$
$$
\boxed{x_2 = x_0 - \frac{f_0(x_1 - x_0)}{f_1 - f_0}}
$$

**Step 5. Rearrange into the classic weighted-average form:**
$$
x_2 = \frac{x_0(f_1 - f_0) - f_0(x_1 - x_0)}{f_1 - f_0} = \frac{x_0 f_1 - x_1 f_0}{f_1 - f_0}
$$

Notice that $x_2 = \frac{x_0 f_1 - x_1 f_0}{f_1 - f_0}$ is a **weighted average** of the endpoints $x_0$ and $x_1$, weighted inversely by their function values. A weighted average of two values always stays between them, guaranteeing that $x_2$ never leaves the bracket!

### Step-by-Step Algorithm (2017 Q.2(b))

1. **Input:** Accept the function $f(x)$, initial bracket limits $a$ and $b$, tolerance $\varepsilon$, and maximum iterations $N$.
2. **Bracket verification:** Compute $f(a)$ and $f(b)$. If $f(a) \cdot f(b) > 0$, display an error ("No sign change detected; bracket invalid") and terminate.
3. **Compute the chord root:**
$$
c = \frac{a\,f(b) - b\,f(a)}{f(b) - f(a)}
$$
4. **Evaluate function at new point:** Compute $f(c)$.
5. **Check convergence:** If $|f(c)| < \varepsilon$ or $|b - a| < \varepsilon$, accept $c$ as the root and terminate.
6. **Update the interval:**
   - If $f(a) \cdot f(c) < 0$, the root lies in $[a, c]$: set $b = c$.
   - Otherwise, the root lies in $[c, b]$: set $a = c$.
7. **Loop control:** If iteration count exceeds $N$, report non-convergence; otherwise, loop back to Step 3.

---

## The Danger of One-Sided Stagnation (and the Illinois Fix)

False position has one notorious flaw that class tests and finals love to quiz: **one-sided stagnation**.

### Why One Endpoint Freezes
If a curve is strongly concave or convex throughout the bracket (like $f(x) = x^{2.2} - 69$ or $f(x) = x^3 - 2x - 5$), the chord always stays on one side of the curve. Because of this:
- The chord intercept $c$ always lands on the same side of the true root.
- The sign test $f(a) \cdot f(c) < 0$ continuously updates the same endpoint, while the opposite endpoint **never moves**.
- The bracket shrinks only from one side, and convergence degrades to a crawl -- behaving like a slow, one-sided secant step rather than a rapid search.

> [!WARNING] Never "Fix" a Stalled Endpoint by Hand!
> In 2021 Q.2(b) ($x^{2.2} = 69$), the upper endpoint stays pinned at $b = 8.000000$ across all seven iterations! Many students assume they made an arithmetic mistake and manually change $b$. That will cost you marks. Stagnation is the mathematically correct behavior of standard Regula Falsi on convex curves.

### The Fix: The Illinois Modification
Whenever an endpoint remains stuck for two consecutive iterations without updating, divide its retained function value by 2:
$$
f_{\text{stuck}} \leftarrow \frac{1}{2} f_{\text{stuck}}
$$
This effectively "lowers" the stubborn endpoint, pulling the chord downward and forcing the next intercept to jump across to the opposite side of the root. Both endpoints resume moving, restoring fast convergence.

---

## 🔧 Worked Example

> **Question:** Given that the equation $x^{2.2} = 69$ has a root between 5 and 8, use the method of regula-falsi to determine it to five decimal places.
> 
> *(Source: 2021 Q.2(b) [Marks: 04, CO: 3])*

**Let's solve this step by step.**

**Step 1. Formulate $f(x)$ and check the bracket:**
$$
f(x) = x^{2.2} - 69 = 0
$$
$$
f(5) = 5^{2.2} - 69 = 34.4932415 - 69 = -34.5067585
$$
$$
f(8) = 8^{2.2} - 69 = 97.0058603 - 69 = +28.0058603
$$
Since $f(5) \cdot f(8) < 0$, a real root lies within $(5, 8)$.

**Step 2. Apply the chord formula:**
$$
x_1 = \frac{a f(b) - b f(a)}{f(b) - f(a)} = \frac{5(28.0058603) - 8(-34.5067585)}{28.0058603 - (-34.5067585)}
$$
$$
x_1 = \frac{140.0293015 + 276.0540680}{62.5126188} = \frac{416.0833695}{62.5126188} \approx 6.655990
$$

**Step 3. Compute subsequent iterations:**
Evaluating $f(6.655990) = (6.655990)^{2.2} - 69 \approx -4.27563$.
Because $f(x_1) < 0$, the root lies in $[6.655990, 8]$. The upper endpoint $b = 8$ stays fixed, and $a$ updates to $6.655990$.

**Iteration table:**

| Iteration | $a$ | $b$ | Next approximation $x$ | $f(x)$ |
| :--: | :--: | :--: | :--: | :--: |
| 1 | 5.000000 | 8.000000 | 6.655990 | $-4.27563$ |
| 2 | 6.655990 | 8.000000 | 6.834002 | $-0.40615$ |
| 3 | 6.834002 | 8.000000 | 6.850670 | $-0.03755$ |
| 4 | 6.850670 | 8.000000 | 6.852209 | $-0.00346$ |
| 5 | 6.852209 | 8.000000 | 6.852351 | $-0.00032$ |
| 6 | 6.852351 | 8.000000 | 6.852364 | $-0.00003$ |
| 7 | 6.852364 | 8.000000 | 6.852365 | $-0.000003$ |

Notice how $b = 8.000000$ remains pinned throughout all seven iterations due to one-sided stagnation. Rounding $x_7 = 6.852365$ to five decimal places gives:

$$
\boxed{x = 6.85237 \quad \text{(to five decimal places)}}
$$

**Sanity checks:**
- **Exact closed form:** $x = 69^{1/2.2} = 69^{5/11} \approx 6.85236512$, which rounds to $6.85237$.
- **Secant check:** Running secant on the same points yields $6.852365$ in just 5 iterations.

---

## 🏆 Past Exam Questions

### 2018 Q.2(b): Regula-Falsi Next Approximation Formula [04 marks]

**The question:** Derive the expression of the next approximation of a root of the non-linear function $f(x) = 0$ using regula-falsi method.

**How to answer like a top student:**
Write the 2-point line equation, set $y = 0$, isolate the next estimate $x_2$, and explain its geometric interpretation as a weighted average.

**Solution:**

Let $x_0$ and $x_1$ be two approximations such that $f(x_0)$ and $f(x_1)$ have opposite signs ($f(x_0) \cdot f(x_1) < 0$). This ensures a real root exists between them. Let $f_0 = f(x_0)$ and $f_1 = f(x_1)$.

The method of false position replaces the curve $y = f(x)$ on $[x_0, x_1]$ by the chord passing through the points $(x_0, f_0)$ and $(x_1, f_1)$.

Using the two-point form of a straight line:
$$
\frac{y - f_0}{f_1 - f_0} = \frac{x - x_0}{x_1 - x_0}
$$

The next approximation to the root, denoted by $x_2$, is the point where this chord intersects the $x$-axis. Setting $y = 0$ and $x = x_2$:
$$
\frac{0 - f_0}{f_1 - f_0} = \frac{x_2 - x_0}{x_1 - x_0}
$$

Multiplying both sides by $(x_1 - x_0)$:
$$
x_2 - x_0 = -\frac{f_0(x_1 - x_0)}{f_1 - f_0}
$$

Solving for $x_2$:
$$
\boxed{x_2 = x_0 - \frac{f_0(x_1 - x_0)}{f_1 - f_0}}
$$

**Equivalent forms:**
Expanding the numerator over a common denominator:
$$
x_2 = \frac{x_0(f_1 - f_0) - f_0(x_1 - x_0)}{f_1 - f_0} = \frac{x_0 f_1 - x_1 f_0}{f_1 - f_0}
$$
This form shows that $x_2$ is a weighted average of the endpoints $x_0$ and $x_1$ with weights $f_1$ and $-f_0$. Because both weights have the same sign (since $f_0$ and $f_1$ have opposite signs), $x_2$ is guaranteed to lie strictly between $x_0$ and $x_1$.

---

### 2017 Q.2(b): False Position Algorithm Steps [04 marks]

**The question:** Write down the algorithm steps while finding the root of a nonlinear equation using false position method.

**How to answer like a top student:**
Deliver clean numbered steps, include the mathematical formula for the chord root, and state the update rule.

**Solution:**

1. **Input:** Accept the function $f(x)$, bracket endpoints $a$ and $b$, stopping tolerance $\varepsilon$, and maximum iterations $N$.
2. **Initial bracket test:** Compute $f(a)$ and $f(b)$. If $f(a) \cdot f(b) > 0$, display "Bracket does not contain a sign change" and terminate.
3. **Compute approximation:** Calculate the chord intercept:
$$
c = \frac{a\,f(b) - b\,f(a)}{f(b) - f(a)}
$$
4. **Evaluate function:** Compute $f(c)$.
5. **Convergence test:** If $|f(c)| < \varepsilon$ or $|b - a| < \varepsilon$, accept $c$ as the root and stop.
6. **Update bracket:**
   - If $f(a) \cdot f(c) < 0$, set $b = c$.
   - Else, set $a = c$.
7. **Iteration check:** Increment counter. If counter exceeds $N$, stop with non-convergence warning; otherwise, go back to Step 3.

---

### CT-01 Q.2(a): Bisection vs. Regula Falsi for Safety-Critical Systems [Class Test]

**The question:** Compare the Bisection Method and Regula Falsi Method in terms of the required condition for application, convergence behavior, and suitability for a safety-critical system.

**How to answer like a top student:**
Structure your response into clear thematic headings and provide a side-by-side comparison table.

**Solution:**

| Feature | Bisection Method | Regula Falsi Method |
| :-- | :-- | :-- |
| **Required condition** | Continuity of $f(x)$ and sign change $f(a)f(b) < 0$ | Continuity of $f(x)$ and sign change $f(a)f(b) < 0$ |
| **New point choice** | Arithmetic midpoint: $c = \frac{a+b}{2}$ | Chord intercept: $c = \frac{af(b) - bf(a)}{f(b) - f(a)}$ |
| **Convergence rate** | Strictly linear; interval halves each step | Linear; generally faster, but depends on function curvature |
| **Interval reduction** | Strictly predictable: width drops by $2^n$ | Unpredictable; one endpoint can stagnate indefinitely |
| **Safety-critical pick** | **Preferred** due to 100% predictable time bounds | Less suitable unless modified by the Illinois method |

**Analysis for safety-critical systems:**
1. **Predictability beats speed:** In an avionics or reactor control system, a deterministic execution time is essential. Bisection guarantees the exact number of iterations $n = \lceil \log_2((b-a)/\varepsilon) \rceil$ before starting. Regula Falsi offers no such fixed time bound.
2. **Immunity to function shape:** Strongly curved functions cause Regula Falsi to stagnate on one endpoint, crawling slowly. Bisection is completely unaffected by function curvature.
3. **Safety recommendation:** Use Bisection for deterministic safety interlocks. If Regula Falsi must be used, implement the Illinois modification to prevent endpoint stagnation.

---

### CT-01 Q.2(b): Endpoint Stagnation Mechanism & Remedy [Class Test]

**The question:** During testing, the Regula Falsi Method repeatedly updates only one endpoint of the interval, leading to slow convergence. Explain why this happens, compare it with the Bisection Method, and suggest a suitable improvement.

**How to answer like a top student:**
Explain the geometric mechanism (convexity keeps chords on one side), contrast it with bisection, and define the Illinois modification.

**Solution:**

**Why one endpoint stalls:**
When $f(x)$ is strongly convex (or concave) over the bracket $[a, b]$, the chord connecting $(a, f(a))$ and $(b, f(b))$ always lies entirely above (or below) the curve. As a result:
- The chord's $x$-intercept $c$ always lands on the same side of the true root.
- The sign of $f(c)$ consistently matches the sign of the starting point on that side.
- So, the algorithm replaces that same endpoint on every step, while the opposite endpoint never changes ($b$ remains pinned). The interval only shrinks from one direction, degrading convergence to a slow linear crawl.

**Comparison with Bisection:**
Bisection places its new point at the arithmetic midpoint $c = \frac{a+b}{2}$ without regard to function values or curvature. Thus, both boundaries continue to advance, and the interval width shrinks by exactly 50% on every iteration.

**Suggested improvements:**
1. **The Illinois Modification:** When an endpoint remains un-updated for two consecutive iterations, divide its retained function value by 2:
$$
f_{\text{stuck}} \leftarrow \frac{1}{2} f_{\text{stuck}}
$$
This artificial reduction pulls the next chord toward the opposite side, forcing the stuck endpoint to update and restoring superlinear-like speed while maintaining bracket safety.
2. **Interval pre-subdivision:** Subdivide the initial interval into 4 smaller equal sub-intervals and scan for a sign change. Applying Regula Falsi to a narrower, nearly linear sub-interval prevents stagnation.

---

### Exam Variants at a Glance

| Year | What They Asked | Key Answer / Formula |
|:---|:---|:---|
| 2017 Q.2(b) | Algorithm steps of false position method (04 marks) | Complete 7-step algorithm, $c = \frac{af(b) - bf(a)}{f(b) - f(a)}$ |
| 2018 Q.2(b) | Derive next approximation formula from two points (04 marks) | $\boxed{x_2 = x_0 - \frac{f_0(x_1 - x_0)}{f_1 - f_0}}$ |
| 2021 Q.2(b) | Regula Falsi on $x^{2.2} = 69$ between 5 and 8 (04 marks) | $\boxed{x = 6.85237 \quad \text{(to five decimal places)}}$ |
| CT-01 Q.2(a) | Bisection vs. Regula Falsi in safety-critical systems | Bisection preferred (predictability > speed) |
| CT-01 Q.2(b) | Endpoint stagnation cause and Illinois modification | Convexity causes one-sided pinning; halve retained $f$ |

---

## ⚡ Quick Review

**The method in one sentence:** False Position connects two bracketing points with a straight line and chooses the line's horizontal intercept as the next guess.

**The formula you must memorize:**
$$
c = \frac{a\,f(b) - b\,f(a)}{f(b) - f(a)} = a - \frac{f(a)(b - a)}{f(b) - f(a)}
$$

**The most common exam mistake:** Assuming you made a calculation error when one endpoint never changes. On convex curves, standard Regula Falsi naturally freezes one endpoint!

**Time estimate in exam:** 8 minutes for a derivation; 10–12 minutes for a multi-step table calculation.

---

## 🔗 Connected Topics

- [← NM-2.2: Bisection Method](NM-2.2_Bisection_Method.md) -- the simpler bracketing method that uses midpoints instead of chords.
- [→ NM-2.4: Newton-Raphson Method](NM-2.4_Newton_Raphson.md) -- replaces the two-point chord with a one-point tangent slope.
- [NM-2.5: Secant Method](NM-2.5_Secant_Method.md) -- uses the exact same chord formula as Regula Falsi, but drops the bracketing requirement.
- [NM-2.6: Method Comparison and Convergence](NM-2.6_Method_Comparison.md) -- where Regula Falsi sits on the safe-to-fast ladder.

---

[← Previous: NM-2.2 Bisection Method](NM-2.2_Bisection_Method.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: NM-2.4 Newton-Raphson →](NM-2.4_Newton_Raphson.md)
