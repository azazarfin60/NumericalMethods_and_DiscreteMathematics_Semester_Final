---
title: "NM-2.7 · Roots of Polynomials"
tags:
  - numerical-methods
  - discrete-mathematics
  - topicwise
---

# NM-2.7 · Roots of Polynomials

Every block below is copied from `../answers_exam_style/`, which is the
only place an answer is authored. A number here is the same number, character
for character, as the one it came from.


### [2019 Q.2(b)]

**Question.** Compute current, $I$ from the following power balance equation obtained from an electric circuit by using an iterative method: $5I^2 + 50I = 1000$.

**Solution.**

Write the equation in the form $f(I) = 0$:

$$f(I) = 5I^2 + 50I - 1000 = 0, \qquad f'(I) = 10I + 50$$

**Closed-form check on the answer.** Completing the square, or dividing by 5,

$$I^2 + 10I - 200 = 0 \implies I = \frac{-10 \pm \sqrt{100 + 800}}{2} = \frac{-10 \pm 30}{2}$$

the two roots are $I = 10$ and $I = -20$. The current is positive, so $I = 10$ is
the root of interest. This fixes the target against which the iterations below
are judged.

**Iteration by Newton–Raphson.** The formula is

$$I_{k+1} = I_k - \frac{5I_k^2 + 50I_k - 1000}{10I_k + 50}$$

Take $I_0 = 5$, and note $f(5) = 125 + 250 - 1000 = -625 < 0$ while
$f(20) = 2000 + 1000 - 1000 > 0$, so the root lies above $I_0$ and the iteration
moves the right way.

| $k$ | $I_k$ | $f(I_k)$ | $f'(I_k)$ | $I_{k+1}$ |
| :--: | :-- | :-- | :-- | :-- |
| 0 | 5 | $-625$ | 100 | $11.25$ |
| 1 | $11.25$ | $195.3125$ | $162.5$ | $10.0480769$ |
| 2 | $10.0480769$ | $7.2231$ | $150.4808$ | $10.0000768$ |
| 3 | $10.0000768$ | $0.0115$ | $150.0008$ | $10.0000000$ |

The iterates settle on $I = 10$. The last correction is $0.0000768$, already
below $10^{-4}$, so the value is accepted.

$$\boxed{I = 10\ \text{A}}$$

> [!info] Check against the original equation
> Substituting $I = 10$ directly, $5(100) + 50(10) = 500 + 500 = 1000$, matching
> the right-hand side exactly. The substitution is the simplest test available
> and it confirms both the arithmetic of the iteration and the algebraic solution
> $I = (-10 + 30)/2$.

---

### [2021 Q.2(c)]

**Question.** Determine the smallest root of the equation: $f(x) = x^3 - 9x^2 + 26x - 24 = 0$.

**Solution.**

**Step 1. Locate the roots by sign changes.** Evaluate at integer values:

| $x$ | $f(x)$ | Sign |
| --: | --: | :-: |
| 0 | $-24$ | $-$ |
| 1 | $1 - 9 + 26 - 24 = -6$ | $-$ |
| 2 | $8 - 36 + 52 - 24 = 0$ | $0$ |
| 3 | $27 - 81 + 78 - 24 = 0$ | $0$ |
| 4 | $64 - 144 + 104 - 24 = 0$ | $0$ |
| 5 | $125 - 225 + 130 - 24 = 6$ | $+$ |

**Step 2. Recognise the factorisation.** All of $2, 3, 4$ are exact roots, and a
cubic has at most three, so

$$
f(x) = (x-2)(x-3)(x-4)
$$

Verification by expansion: $(x-2)(x-3) = x^2 - 5x + 6$, and
$(x^2-5x+6)(x-4) = x^3 - 4x^2 - 5x^2 + 20x + 6x - 24 = x^3 - 9x^2 + 26x - 24$.
Correct.

**Step 3. Smallest root.**

$$
\boxed{x = 2}
$$

**Step 4. Confirm with a numerical method**, since the question asks for root
finding. Use Newton-Raphson with

$$
f(x) = x^3 - 9x^2 + 26x - 24, \qquad f'(x) = 3x^2 - 18x + 26
$$

Start at $x_0 = 1.5$, where $f(1.5) = 3.375 - 20.25 + 39 - 24 = -1.875$ and
$f'(1.5) = 6.75 - 27 + 26 = 5.75$:

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

The derivative column matters. Newton divides by $f'(x_n)$, and here $f'$ drifts
from $5.75$ to $2.00$ across the five steps, so a value carried over from the
previous row is visibly wrong. It settles at $2.00 = f'(2)$, which is the
self-consistency check at the root.

> [!warning] Choosing the bracket
> The interval $[1, 2]$ is **not** usable, because $f(2) = 0$ puts the root exactly
> on the endpoint and $f(1)f(2) = 0$, not $< 0$. The pair $[1.5, 2.5]$ works:
> $f(1.5) = -1.875$ and $f(2.5) = 15.625 - 56.25 + 65 - 24 = 0.375$, so
> $f(1.5)f(2.5) = -0.703 < 0$.
>
> Also note there is **no** root below $2$: $f$ is negative throughout $(-\infty, 2)$
> except at the single point $2$ itself, and $f'(x) = 3x^2 - 18x + 26$ has roots at
> $3 \pm \frac{\sqrt3}{3} \approx 2.423$ and $3.577$, so $f$ is increasing up to
> $2.423$. Since $f$ is negative on $[0, 2)$ and $f(2) = 0$, the value $2$ is
> indeed the smallest root, not merely one of three.

---

---

**Also asked here.**

- *2020 Q.2(b)* is the same question as [[NM-2.4_Newton_Raphson_Method|NM-2.4]], which is written in `NM-2.4`.
- *2024 Q.2(a)* is the same question as [[NM-2.2_Bisection_Method|NM-2.2]], which is written in `NM-2.2`.

---
