[← Previous: NM-2.6 Method Comparison](NM-2.6_Method_Comparison_and_Convergence.md) | [🏠 Index](00_Index.md) | [Next: NM-3.2 Pivoting →](NM-3.2_Pivoting.md)

---

# NM-2 Lower Tier: Secant Method and Roots of Polynomials
> **Section:** A (Numerical Methods) | **Priority:** 🟠 (mixed) | **Subtopics:** NM-2.5, NM-2.7
> **Sources:** Jain Ch.2 §2.7, §2.1, Topicwise NM-2.5, NM-2.7

This file merges two lower-tier subtopics of NM-2. Each gets its own full treatment below: definitions, theory, worked example, and every past exam question.

---

## NM-2.5 — Secant Method

### 📝 Definitions for NM-2.5

> **Secant method (derivative substitution):** "the derivative at $x_i$ is approximated by the formula $f'(x_i) \approx \frac{f(x_i) - f(x_{i-1})}{x_i - x_{i-1}}$" — Jain, §2.7

> **Secant formula:** "$x_{i+1} = x_i - \frac{f_i (x_i - x_{i-1})}{f_i - f_{i-1}} = \frac{x_{i-1}f_i - x_i f_{i-1}}{f_i - f_{i-1}}$" — Jain, §2.7

> **Secant method:** An open root finder that replaces the Newton derivative with the slope through the last two iterates. It needs two starting values and no analytic derivative.

### Theory

**Where it comes from.** Newton needs $f'$, and $f'$ is not always available. Jain states the problem plainly: "the Newton-Raphson method requires the evaluation of derivatives of the function and this is not always possible, particularly in the case of functions arising in practical problems."

So approximate the derivative. Through the two most recent points, the slope is

$$
f'(x_i) \approx \frac{f_i - f_{i-1}}{x_i - x_{i-1}}
$$

Drop that into Newton's formula:

$$
x_{i+1} = x_i - \frac{f_i (x_i - x_{i-1})}{f_i - f_{i-1}} = \frac{x_{i-1}f_i - x_i f_{i-1}}{f_i - f_{i-1}}
$$

The textbook adds the warning: "this formula requires two initial approximations to the root."

**How it differs from Newton.**

| | Newton | Secant |
| :-- | :-- | :-- |
| Slope from | the analytic derivative | the last two iterates |
| Starting values | one, $x_0$ | two, $x_0$ and $x_1$ |
| Evaluations per step | 2 | 1 |
| Order | 2 | 1.618 |
| Bracket needed | no | no |
| Can it lose the root entirely | yes | yes |

The secant keeps almost all of Newton's speed. Order $1.618$ instead of $2$, but only one function call per step instead of two. Where $f'$ is expensive or unavailable, the secant's order per evaluation is competitive.

**The initial-guess hazard.** Two starts are needed, so there are two ways to go wrong. If the two guesses sit close together and the function is nearly flat between them, the denominator $f_i - f_{i-1}$ is tiny and the next iterate is thrown far away. If they straddle a stationary region, the secant line can miss the axis entirely. There is no bracket to catch either case, because the secant discards it.

**Relationship to regula falsi.** The algebra is identical. The difference is the update rule. Regula falsi keeps whichever endpoint has the opposite sign, so the root stays bracketed but one endpoint can stall. Secant always drops the older point, so it converges faster and can never stall, but it also cannot detect its own divergence. Regula falsi on $x^{2.2}=69$ took seven iterations with $b$ pinned at $8$; secant took four with both points moving.

---

### Worked Example for NM-2.5: $f(x) = x^3 - 3x^2 - x - 3 = 0$

**Problem.** Find the positive root of the equation $f(x) = x^3 - 3x^2 - x - 3 = 0$ by secant method. Use four iterations only.

> **Source:** 2017 Q.2(c) [Marks: 04]

*Note.* The constant term is faintly printed in the original. It is read here as $-3$, giving $f(x) = x^3 - 3x^2 - x - 3$, and the alternative reading $-1$ is discussed at the end.

**Step 1. Sign check.** $f(0) = -3$, $f(1) = -6$, $f(2) = 8 - 12 - 2 - 3 = -9$, and $f(4) = 64 - 48 - 4 - 3 = 9$. The sign changes between $2$ and $4$, so a positive root lies in that interval. Take $x_0 = 2$ and $x_1 = 3$, for which $f(2) = -9$ and $f(3) = 27 - 27 - 3 - 3 = -6$.

**Step 2. The iteration formula.**

$$
x_{n+1} = x_n - \frac{f(x_n)(x_n - x_{n-1})}{f(x_n) - f(x_{n-1})}
$$

**Step 3. Iteration 1.**

$$
x_2 = 3 - \frac{(-6)(3 - 2)}{(-6) - (-9)} = 3 - \frac{-6}{3} = 3 + 2 = 5.0000
$$

**Step 4. Iteration 2.** $f(5) = 125 - 75 - 5 - 3 = 42$.

$$
x_3 = 5 - \frac{42(5 - 3)}{42 - (-6)} = 5 - \frac{84}{48} = 5 - 1.7500 = 3.2500
$$

**Step 5. Iteration 3.** $f(3.25) = 3.25^3 - 3(3.25)^2 - 3.25 - 3 = 34.328125 - 31.6875 - 6.25 = -3.609375$.

$$
x_4 = 3.25 - \frac{(-3.609375)(3.25 - 5)}{(-3.609375) - 42} = 3.25 - \frac{6.316406}{-45.609375} = 3.25 + 0.138489 = 3.388489
$$

**Step 6. Iteration 4.** $f(3.388489) = 38.906148 - 34.445573 - 6.388489 = -1.927914$.

$$
x_5 = 3.388489 - \frac{(-1.927914)(3.388489 - 3.25)}{(-1.927914) - (-3.609375)} = 3.388489 + \frac{0.266995}{1.681461} = 3.547276
$$

**Step 7. The four iterations.**

| Iteration | $x_n$ | $f(x_n)$ |
| :--: | :-- | :-- |
| 1 | $5.000000$ | $42.000000$ |
| 2 | $3.250000$ | $-3.609375$ |
| 3 | $3.388489$ | $-1.927914$ |
| 4 | $3.547276$ | $0.339189$ |

$$
\boxed{x \approx 3.547 \text{ after four iterations}}
$$

> [!NOTE]
> Check by substitution and a second pair of starts. Substituting $x = 3.547276$ gives $f = 0.339189$, still a long way from zero, so the answer is the value after four steps as asked rather than the root. Solving the cubic exactly gives the real root $x = 3.525102$, so the four iterations are still $0.022$ away. Starting the secant from $x_0 = 3.5$, $x_1 = 3.6$ instead, which is much closer to the root, gives $3.525102$ after four iterations, converging on the exact root. That the two starts bracket $3.525102$ confirms $3.547$ is the outcome of the requested imperfect start, not of an arithmetic slip.
>
> A note on reading the four-step sequence: the secant is not monotone, so $5.0000, 3.2500, 3.3885, 3.5473$ overshoots low, undershoots, then overshoots again. A student expecting monotone convergence after the first step will misread the third value and stop early.

> [!WARNING]
> On the faint constant term. If the constant were read as $-1$, giving $f(x) = x^3 - 3x^2 - x - 1$, the exact root is $x = 3.382976$ and the same start pair $x_0 = 2$, $x_1 = 3$ gives $3.3888$ after four iterations. Both readings are handled here, with the $-3$ reading presented as the primary answer because it is the one that yields the sign change in the printed interval and the cleaner arithmetic.

---

### 🏆 Golden Questions for NM-2.5

#### 🎯 Find the positive root of the equation $f(x) = x^3 - 3x^2 - x - 3 = 0$ by secant method (Use four iterations only).
> **Appeared:** 2017 Q.2(c) — (04 marks)

**Full Answer:**

Set up the sign check first:

$$
f(x) = x^3 - 3x^2 - x - 3
$$

$f(0) = -3$, $f(1) = -6$, $f(2) = -9$, $f(4) = +9$. The sign change lies between $2$ and $4$, so a positive root is inside. Take $x_0 = 2$ and $x_1 = 3$, giving $f(2) = -9$ and $f(3) = -6$.

The iteration formula:

$$
x_{n+1} = x_n - \frac{f(x_n)(x_n - x_{n-1})}{f(x_n) - f(x_{n-1})}
$$

Iteration 1:

$$
x_2 = 3 - \frac{(-6)(3 - 2)}{(-6) - (-9)} = 3 - \frac{-6}{3} = 5.0000
$$

Iteration 2, with $f(5) = 42$:

$$
x_3 = 5 - \frac{42(5 - 3)}{42 - (-6)} = 5 - \frac{84}{48} = 3.2500
$$

Iteration 3, with $f(3.25) = -3.609375$:

$$
x_4 = 3.25 - \frac{(-3.609375)(3.25 - 5)}{(-3.609375) - 42} = 3.25 + 0.138489 = 3.388489
$$

Iteration 4, with $f(3.388489) = -1.927914$:

$$
x_5 = 3.388489 - \frac{(-1.927914)(3.388489 - 3.25)}{(-1.927914) - (-3.609375)} = 3.388489 + \frac{0.266995}{1.681461} = 3.547276
$$

| Iteration | $x_n$ | $f(x_n)$ |
| :--: | :-- | :-- |
| 1 | $5.000000$ | $42.000000$ |
| 2 | $3.250000$ | $-3.609375$ |
| 3 | $3.388489$ | $-1.927914$ |
| 4 | $3.547276$ | $0.339189$ |

$$
\boxed{x \approx 3.547 \text{ after four iterations}}
$$

The question asks for four iterations, not for the root, so $3.547$ is the correct answer even though $f(3.547276) = 0.339189$ is not zero. The exact real root is $3.525102$.

---

## NM-2.7 — Roots of Polynomials

### 📝 Definitions for NM-2.7

> **Polynomial (degree and root count):** "Every polynomial equation of the $n$th degree has $n$ and only $n$ roots." — Jain, §2.1

> **Odd degree:** "If $n$ is odd, the polynomial equation has atleast one real root whose sign is opposite to that of the last term." — Jain, §2.1

> **Descartes' Rule of Signs:** "A polynomial equation $f(x) = 0$ cannot have more number of positive real roots than the number of changes of sign in the coefficients of $f(x)$." — Jain, §2.1

> **Smallest root:** The least real value of $x$ at which $f(x) = 0$. Found by sign scan from below and confirmed by locating the turning points of $f$.

### Theory

**Locating roots before you solve them.** Every root-finding question on a polynomial is easier if you scan first. Evaluate $f$ at integer points and watch the sign. Where it flips, a root is inside. Where it lands on zero, you have found a root exactly and you can factor it out.

**Using Descartes' Rule of Signs.** Count sign changes in the coefficients to bound the number of positive roots, then evaluate $f(-x)$ to bound the negative roots. For $x^3 - 9x^2 + 26x - 24$ the signs are $+, -, +, -$, which is three changes. So at most three positive roots. The question asks for the smallest one, and the scan finds it immediately.

**Factoring beats iterating, when it works.** If the scan hits zero at an integer, factor. For $x^3 - 9x^2 + 26x - 24$:

| $x$ | $f(x)$ | Sign |
| --: | --: | :-: |
| 0 | $-24$ | $-$ |
| 1 | $1 - 9 + 26 - 24 = -6$ | $-$ |
| 2 | $8 - 36 + 52 - 24 = 0$ | $0$ |
| 3 | $27 - 81 + 78 - 24 = 0$ | $0$ |
| 4 | $64 - 144 + 104 - 24 = 0$ | $0$ |
| 5 | $125 - 225 + 130 - 24 = 6$ | $+$ |

All of $2, 3, 4$ are exact roots, and a cubic has at most three, so

$$
f(x) = (x-2)(x-3)(x-4)
$$

Verification by expansion: $(x-2)(x-3) = x^2 - 5x + 6$, and $(x^2-5x+6)(x-4) = x^3 - 4x^2 - 5x^2 + 20x + 6x - 24 = x^3 - 9x^2 + 26x - 24$. Correct.

**Physics-framed polynomial problems.** Some questions hide a polynomial behind a physical statement: a power balance in a circuit, a current from a nonlinear device. The method is the same: write $f = 0$, bracket the physical root, then iterate. Newton-Raphson is the natural choice because the derivative is easy.

---

### Worked Example for NM-2.7: Power Balance Current

**Problem.** Compute current, $I$ from the following power balance equation obtained from an electric circuit by using an iterative method: $5I^2 + 50I = 1000$.

> **Source:** 2019 Q.2(b) [Marks: 04]

**Step 1. Put it in the form $f(I) = 0$.**

$$
f(I) = 5I^2 + 50I - 1000 = 0, \qquad f'(I) = 10I + 50
$$

**Step 2. Closed-form check on the answer.** Dividing by 5:

$$
I^2 + 10I - 200 = 0 \implies I = \frac{-10 \pm \sqrt{100 + 800}}{2} = \frac{-10 \pm 30}{2}
$$

The two roots are $I = 10$ and $I = -20$. The current is positive, so $I = 10$ is the root of interest. This fixes the target against which the iterations are judged.

**Step 3. The Newton-Raphson iteration.**

$$
I_{k+1} = I_k - \frac{5I_k^2 + 50I_k - 1000}{10I_k + 50}
$$

Take $I_0 = 5$, and note $f(5) = 125 + 250 - 1000 = -625 < 0$ while $f(20) = 2000 + 1000 - 1000 > 0$, so the root lies above $I_0$ and the iteration moves the right way.

**Step 4. The march.**

| $k$ | $I_k$ | $f(I_k)$ | $f'(I_k)$ | $I_{k+1}$ |
| :--: | :-- | :-- | :-- | :-- |
| 0 | 5 | $-625$ | 100 | $11.25$ |
| 1 | $11.25$ | $195.3125$ | $162.5$ | $10.0480769$ |
| 2 | $10.0480769$ | $7.2231$ | $150.4808$ | $10.0000768$ |
| 3 | $10.0000768$ | $0.0115$ | $150.0008$ | $10.0000000$ |

The iterates settle on $I = 10$. The last correction is $0.0000768$, already below $10^{-4}$, so the value is accepted.

$$
\boxed{I = 10\ \text{A}}
$$

> [!NOTE]
> Check against the original equation. Substituting $I = 10$ directly, $5(100) + 50(10) = 500 + 500 = 1000$, matching the right-hand side exactly. The substitution is the simplest test available and it confirms both the arithmetic of the iteration and the algebraic solution $I = (-10 + 30)/2$.
>
> Reading the convergence off the table: the corrections are $6.25$, $1.2019$, $0.0480$, $0.0000768$. The ratios of successive corrections are $5.2$, $25.0$, $625$, which is the signature of quadratic convergence: the correction is roughly the square of the one before. Notice also that the derivative column settles at $150$, which is $f'(10) = 10(10) + 50$. Once the iterate is the root, the derivative printed beside it must be the true derivative there, and it is. That column is free and it catches a whole class of transcription error.

---

### Worked Example for NM-2.7: Smallest Root of a Cubic

**Problem.** Determine the smallest root of the equation: $f(x) = x^3 - 9x^2 + 26x - 24 = 0$.

> **Source:** 2021 Q.2(c) [Marks: 06, CO: 3]

**Step 1. Locate the roots by sign changes.** Evaluate at integer values, as in the table above. The values $2$, $3$ and $4$ give exactly zero.

**Step 2. Recognise the factorisation.**

$$
f(x) = (x-2)(x-3)(x-4)
$$

**Step 3. The smallest root.**

$$
\boxed{x = 2}
$$

**Step 4. Confirm with a numerical method**, since the question asks for root finding. Use Newton-Raphson with

$$
f(x) = x^3 - 9x^2 + 26x - 24, \qquad f'(x) = 3x^2 - 18x + 26
$$

Start at $x_0 = 1.5$, where $f(1.5) = 3.375 - 20.25 + 39 - 24 = -1.875$ and $f'(1.5) = 6.75 - 27 + 26 = 5.75$:

| Iteration | $x_n$ | $f(x_n)$ | $f'(x_n)$ |
| --: | --: | --: | --: |
| 0 | 1.5000000 | $-1.875000$ | 5.750000 |
| 1 | 1.8260870 | $-0.443823$ | 3.134215 |
| 2 | 1.9676929 | $-0.067779$ | 2.196974 |
| 3 | 1.9985440 | $-0.002918$ | 2.008742 |
| 4 | 1.9999968 | $-0.000006$ | 2.000019 |
| 5 | 2.0000000 | $0$ | 2.000000 |

Iteration 1: $x_1 = 1.5 - \frac{-1.875}{5.750000} = 1.5 + 0.326087 = 1.826087$.

Iteration 2: $x_2 = 1.826087 - \frac{-0.443823}{3.134215} = 1.826087 + 0.141606 = 1.967693$.

> [!WARNING]
> Choosing the bracket. The interval $[1, 2]$ is **not** usable, because $f(2) = 0$ puts the root exactly on the endpoint and $f(1)f(2) = 0$, not $< 0$. The pair $[1.5, 2.5]$ works: $f(1.5) = -1.875$ and $f(2.5) = 15.625 - 56.25 + 65 - 24 = 0.375$, so $f(1.5)f(2.5) = -0.703 < 0$.
>
> Also note there is **no** root below $2$: $f$ is negative throughout $(-\infty, 2)$ except at the single point $2$ itself, and $f'(x) = 3x^2 - 18x + 26$ has roots at $3 \pm \frac{\sqrt3}{3} \approx 2.423$ and $3.577$, so $f$ is increasing up to $2.423$. Since $f$ is negative on $[0, 2)$ and $f(2) = 0$, the value $2$ is indeed the smallest root, not merely one of three.

> [!WARNING]
> The derivative column is not decoration. Newton divides by $f'(x_n)$, and here $f'$ drifts from $5.75$ to $2.00$ across the five steps, so a value carried over from the previous row is visibly wrong. It settles at $2.00 = f'(2)$, which is the self-consistency check at the root: once the iterate is the root, the derivative in the same row must be the true derivative there. This column is the cheapest possible error check, because it is a function of $x$ alone. If $x_n$ and $f'(x_n)$ ever disagree, one of them is wrong.

> [!NOTE]
> Why six marks for a question this easy. Because the marks are not for the factorisation, which is two lines of algebra. They are for the bracket check, the iteration table, the derivative column, and the argument that $2$ is the smallest rather than merely a root. A correct boxed answer with none of that supporting work would not earn the marks.

---

### 🏆 Golden Questions for NM-2.7

#### 🎯 Compute current, $I$ from the following power balance equation obtained from an electric circuit by using an iterative method: $5I^2 + 50I = 1000$.
> **Appeared:** 2019 Q.2(b) — (04 marks)

**Full Answer:**

Write the equation in the form $f(I) = 0$:

$$
f(I) = 5I^2 + 50I - 1000 = 0, \qquad f'(I) = 10I + 50
$$

Check the answer in closed form first, by dividing by 5:

$$
I^2 + 10I - 200 = 0 \implies I = \frac{-10 \pm \sqrt{100 + 800}}{2} = \frac{-10 \pm 30}{2}
$$

The two roots are $I = 10$ and $I = -20$. A current is positive, so $I = 10$ is the root of interest.

The Newton-Raphson formula is

$$
I_{k+1} = I_k - \frac{5I_k^2 + 50I_k - 1000}{10I_k + 50}
$$

Take $I_0 = 5$, where $f(5) = 125 + 250 - 1000 = -625 < 0$ while $f(20) = 2000 + 1000 - 1000 > 0$, so the root lies above $I_0$ and the iteration moves the right way.

| $k$ | $I_k$ | $f(I_k)$ | $f'(I_k)$ | $I_{k+1}$ |
| :--: | :-- | :-- | :-- | :-- |
| 0 | 5 | $-625$ | 100 | $11.25$ |
| 1 | $11.25$ | $195.3125$ | $162.5$ | $10.0480769$ |
| 2 | $10.0480769$ | $7.2231$ | $150.4808$ | $10.0000768$ |
| 3 | $10.0000768$ | $0.0115$ | $150.0008$ | $10.0000000$ |

The last correction is $0.0000768$, already below $10^{-4}$, so the value is accepted.

$$
\boxed{I = 10\ \text{A}}
$$

Substituting $I = 10$ back into the original equation: $5(100) + 50(10) = 500 + 500 = 1000$, which matches exactly.

---

#### 🎯 Determine the smallest root of the equation: $f(x) = x^3 - 9x^2 + 26x - 24 = 0$.
> **Appeared:** 2021 Q.2(c) — (06 marks, CO: 3)

**Full Answer:**

**Step 1. Locate the roots by sign changes.**

| $x$ | $f(x)$ | Sign |
| --: | --: | :-: |
| 0 | $-24$ | $-$ |
| 1 | $1 - 9 + 26 - 24 = -6$ | $-$ |
| 2 | $8 - 36 + 52 - 24 = 0$ | $0$ |
| 3 | $27 - 81 + 78 - 24 = 0$ | $0$ |
| 4 | $64 - 144 + 104 - 24 = 0$ | $0$ |
| 5 | $125 - 225 + 130 - 24 = 6$ | $+$ |

**Step 2. Recognise the factorisation.** All of $2, 3, 4$ are exact roots, and a cubic has at most three, so

$$
f(x) = (x-2)(x-3)(x-4)
$$

Verification by expansion: $(x-2)(x-3) = x^2 - 5x + 6$, and $(x^2-5x+6)(x-4) = x^3 - 4x^2 - 5x^2 + 20x + 6x - 24 = x^3 - 9x^2 + 26x - 24$. Correct.

**Step 3. The smallest root.**

$$
\boxed{x = 2}
$$

**Step 4. Confirm with a numerical method**, since the question asks for root finding. Use Newton-Raphson with

$$
f(x) = x^3 - 9x^2 + 26x - 24, \qquad f'(x) = 3x^2 - 18x + 26
$$

Start at $x_0 = 1.5$, where $f(1.5) = -1.875$ and $f'(1.5) = 5.75$:

| Iteration | $x_n$ | $f(x_n)$ | $f'(x_n)$ |
| --: | --: | --: | --: |
| 0 | 1.5000000 | $-1.875000$ | 5.750000 |
| 1 | 1.8260870 | $-0.443823$ | 3.134215 |
| 2 | 1.9676929 | $-0.067779$ | 2.196974 |
| 3 | 1.9985440 | $-0.002918$ | 2.008742 |
| 4 | 1.9999968 | $-0.000006$ | 2.000019 |
| 5 | 2.0000000 | $0$ | 2.000000 |

Iteration 1: $x_1 = 1.5 - \frac{-1.875}{5.750000} = 1.5 + 0.326087 = 1.826087$.

Iteration 2: $x_2 = 1.826087 - \frac{-0.443823}{3.134215} = 1.826087 + 0.141606 = 1.967693$.

**Step 5. Prove that $2$ is the smallest.** $f'$ vanishes at $3 \pm \frac{\sqrt3}{3} \approx 2.423$ and $3.577$, so $f$ is increasing up to $2.423$ and has no turning point before $2$. Since $f$ is negative on $[0, 2)$ and $f(2) = 0$, the value $2$ is the smallest root.

---

## ⚡ Exam Tips & Common Mistakes

1. **Secant needs two starts. State both.** A question that prints one guess means you choose the second and say so.
2. **Secant can overshoot wildly on the first step.** In 2017 Q.2(c) the sequence goes $5.0, 3.25, 3.389, 3.547$. That is not an error; the secant is not monotone.
3. **"Use four iterations only" means four iterations.** Do not iterate until convergence and then give the root. The request fixes the number of steps.
4. **Scan integers before anything else on a polynomial.** It is one table and it either finds exact roots or gives you a bracket.
5. **Reject non-physical roots explicitly.** $I = -20$ is a root of the power equation and not a current. Write that sentence.
6. **"Smallest root" needs a proof, not just a scan.** Use $f'$ to show there is no turning point below the answer.
7. **Check your derivative column against the iterate in the same row.** It is the cheapest error check you have.

## 🔗 Related Topics

- [NM-2.4: Newton-Raphson Method](NM-2.4_Newton_Raphson_Method.md) — secant is Newton with a finite-difference derivative
- [NM-2.3: False Position & Regula Falsi](NM-2.3_False_Position_and_Regula_Falsi.md) — same chord algebra, but the bracket is kept
- [NM-2.2: Bisection Method](NM-2.2_Bisection_Method.md) — the bracket these open methods throw away
- [NM-2.6: Method Comparison & Convergence](NM-2.6_Method_Comparison_and_Convergence.md) — secant's order 1.618 in context
- [NM-2.1: Fundamentals & Classification](NM-2.1_Fundamentals_and_Classification.md) — the iterative steps both subtopics follow

---

[← Previous: NM-2.6 Method Comparison](NM-2.6_Method_Comparison_and_Convergence.md) | [🏠 Index](00_Index.md) | [Next: NM-3.2 Pivoting →](NM-3.2_Pivoting.md)
