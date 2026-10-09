---
title: "NM-2.7 · Roots of Polynomials"
tags:
  - numerical-methods
  - discrete-mathematics
  - topicwise
---

# NM-2.7 · Roots of Polynomials

Every block below is copied from `../answers_explanation/`. The reasoning
is written once, in the year-wise file, and is not restated here.


### [2019 Q.2(b)]

**Question.** Compute current, $I$ from the following power balance equation obtained from an electric circuit by using an iterative method: $5I^2 + 50I = 1000$.

*[Marks: 04]*

**Solution.**

Write the equation in the form $f(I) = 0$:

$$f(I) = 5I^2 + 50I - 1000 = 0, \qquad f'(I) = 10I + 50$$

**Closed-form check on the answer.** Dividing by 5,

$$I^2 + 10I - 200 = 0 \implies I = \frac{-10 \pm \sqrt{100 + 800}}{2} = \frac{-10 \pm 30}{2}$$

the two roots are $I = 10$ and $I = -20$. The current is positive, so $I = 10$ is
the root of interest. This fixes the target against which the iterations below are
judged.

**Iteration by Newton-Raphson.** The formula is

$$I_{k+1} = I_k - \frac{5I_k^2 + 50I_k - 1000}{10I_k + 50}$$

Take $I_0 = 5$, and note $f(5) = 125 + 250 - 1000 = -625 < 0$ while
$f(20) = 2000 + 1000 - 1000 > 0$, so the root lies above $I_0$ and the iteration
moves the right way.

| $k$ | $I_k$ | $f(I_k)$ | $f'(I_k)$ | $I_{k+1}$ |
| --: | --: | --: | --: | --: |
| 0 | 5 | $-625$ | 100 | $11.25$ |
| 1 | $11.25$ | $195.3125$ | $162.5$ | $10.0480769$ |
| 2 | $10.0480769$ | $7.2231$ | $150.4808$ | $10.0000768$ |
| 3 | $10.0000768$ | $0.0115$ | $150.0008$ | $10.0000000$ |

The iterates settle on $I = 10$. The last correction is $0.0000768$, already below
$10^{-4}$, so the value is accepted.

$$\boxed{I = 10\ \text{A}}$$

> [!info] Check against the original equation
> Substituting $I = 10$ directly, $5(100) + 50(10) = 500 + 500 = 1000$, matching
> the right-hand side exactly. The substitution is the simplest test available
> and it confirms both the arithmetic of the iteration and the algebraic solution
> $I = (-10 + 30)/2$.

> [!note] Reading the convergence off the table
> The corrections are $6.25$, $1.2019$, $0.0480$, $0.0000768$. The ratios of
> successive corrections are $5.2$, $25.0$, $625$, which is the signature of
> quadratic convergence: the correction is roughly the square of the one before.
>
> **Notice also that the derivative column settles at $150$**, which is
> $f'(10) = 10(10) + 50$. Once the iterate is the root, the derivative printed
> beside it must be the true derivative there, and it is. That column is free and
> it catches a whole class of transcription error.

---

### [2021 Q.2(c)]

**Question.** Determine the smallest root of the equation: $f(x) = x^3 - 9x^2 + 26x - 24 = 0$.

*[Marks: 06, CO: 3]*

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

$$\boxed{x = 2}$$

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

> [!warning] The derivative column is not decoration
> Newton divides by $f'(x_n)$, and here $f'$ drifts from $5.75$ to $2.00$ across
> the five steps, so a value carried over from the previous row is visibly wrong.
> It settles at $2.00 = f'(2)$, which is the self-consistency check at the root:
> once the iterate is the root, the derivative in the same row must be the true
> derivative there.
>
> This column is the cheapest possible error check, because it is a function of
> $x$ alone. If $x_n$ and $f'(x_n)$ ever disagree, one of them is wrong.

> [!warning] Choosing the bracket
> The interval $[1, 2]$ is **not** usable, because $f(2) = 0$ puts the root
> exactly on the endpoint and $f(1)f(2) = 0$, not $< 0$. The pair $[1.5, 2.5]$
> works: $f(1.5) = -1.875$ and
> $f(2.5) = 15.625 - 56.25 + 65 - 24 = 0.375$, so $f(1.5)f(2.5) = -0.703 < 0$.
>
> Also note there is **no** root below $2$. Since $f$ is negative on $[0, 2)$ and
> $f(2) = 0$, the value $2$ is the smallest root, not merely one of three. To see
> that $f$ really is negative on that interval, note that
> $f'(x) = 3x^2 - 18x + 26$ vanishes at $3 \pm \frac{\sqrt3}{3} \approx 2.423$ and
> $3.577$, so $f$ increases up to $2.423$ and has no turning point before $2$.

> [!note] Why six marks for a question this easy
> Because the marks are not for the factorisation, which is two lines of algebra.
> They are for the bracket check, the iteration table, the derivative column, and
> the argument that $2$ is the *smallest* rather than merely *a* root. A correct
> boxed answer with none of that supporting work would not earn the marks.

---

---

**Also asked here.**

- *2020 Q.2(b)* is the same question as [[NM-2.4|NM-2.4]], which is written in `NM-2.4`.
- *2024 Q.2(a)* is the same question as [[NM-2.2|NM-2.2]], which is written in `NM-2.2`.

---
