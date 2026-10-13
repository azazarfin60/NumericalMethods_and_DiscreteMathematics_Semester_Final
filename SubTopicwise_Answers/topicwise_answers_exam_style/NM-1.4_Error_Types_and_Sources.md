---
title: "NM-1.4 · Error Types & Sources"
tags:
  - numerical-methods
  - discrete-mathematics
  - topicwise
---


[🏠 Subtopic Index](00_Index.md) | [← Prev: NM-1.3 Accuracy, Precision & Significant Digits](NM-1.3_Accuracy_Precision_and_Significant_Digits.md) | [Next: NM-1.5 Error Representations & Propagation →](NM-1.5_Error_Representations_and_Propagation.md)

---

# NM-1.4 · Error Types & Sources

Every block below is copied from `../answers_exam_style/`, which is the
only place an answer is authored. A number here is the same number, character
for character, as the one it came from.


### [2018 Q.1(b)]

**Question.** What are the algorithmic errors that may occur in numerical calculation?

**Solution.**

Algorithmic error is the error introduced by the computation itself, as opposed
to that already present in the data. It has three sources.

**1. Truncation error.** Every numerical method approximates an infinite process
by a finite one: an infinite series is cut after $n$ terms, an interval is cut
into $n$ panels, a differential equation is stepped with finite $h$. The
discarded remainder is the truncation error, and it is the error that decreases
as the approximation is refined.

**2. Round-off error.** A computer holds only a finite number of digits. Every
arithmetic operation rounds its result to that precision, and the rounding
introduced at one step propagates into every later step. Round-off error
grows with the number of operations, and is the reason a method may become
*less* accurate when refined too far.

**3. Propagation of error.** The two above do not simply add. A method is
**unstable** if an error introduced early is amplified in later steps, and
**well-conditioned** if it is damped. The amplification factor is a property of
the algorithm, not of the arithmetic precision.

**The two errors oppose each other.** For a method with step size $h$,
truncation error falls as a power of $h$ while round-off error grows with
$1/h$ (or worse, if the algorithm is unstable). The total error therefore has a
minimum at some optimal $h$, below which further refinement makes the answer
worse. This is the central practical fact of numerical computation, and it is
why the choice of $h$, the stopping test and the stability of the recurrence
are all parts of the method rather than details of implementation.

---

### [2019 Q.1(b)]

**Question.** What are the errors involved in numerical methods? How do they enter into the process? Give example.

**Solution.**

The errors are **inherent error**, **absolute error**, and **relative error**.

**Inherent error.** The error already present in the physical statement, before
any computation. It subdivides into:

- **Data error**, from measurement. A resistance read off a meter as $4.7\ \Omega$
   carries the meter's own error, whatever is done afterwards.
- **Conversion error**, from the problem statement. When a continuous law is
   written as a formula, finite precision in the law's constants is carried in.
- **Modelling error**, from the assumptions made. The formula $I = V/R$ ignores
   temperature and tolerance; the neglected terms are the modelling error.

Inherent error is not produced by the arithmetic and cannot be reduced by
carrying more digits.

**Absolute error.** The difference between the approximate value $A$ and the true
value $T$:

$$E_{\text{abs}} = A - T, \qquad |E_{\text{abs}}| = |A - T|$$

**Relative error.** The absolute error measured against the true value:

$$E_{\text{rel}} = \frac{E_{\text{abs}}}{T}, \qquad E_{\text{pct}} = 100\frac{E_{\text{abs}}}{T}$$

**How they enter the process.** The steps of any computation are:

1. Formulate the physical problem, where **modelling error** enters.
2. Gather the data, where **data error** enters.
3. Choose a method and carry out the arithmetic, where **round-off error**
   enters at every step.
4. Apply truncation when an infinite process is cut short, where
   **truncation error** enters.
5. Report the result, where the errors of steps 1, 2, 4 and the propagated
   round-off of step 3 appear together.

**Example.** Take $R = 220\ \Omega$ and $V = 10\ \text{V}$, so
$I = 10/220 = 0.0454545\ \text{A}$. Reading the current as $0.045\ \text{A}$ on a
three-digit display gives

$$E_{\text{abs}} = 0.045 - 0.0454545 = -0.0004545\ \text{A}$$

$$E_{\text{rel}} = \frac{-0.0004545}{0.0454545} = -0.01 = -1\%$$

The $-1\%$ has two sources: the display rounding the reading to three decimals,
and the tolerance of the resistor. The first is round-off in the reporting, the
second is data error in the input.

---

### [2020 Q.1(a)]

**Question.** Why are numerical methods for? What are the sources of errors in numerical methods? Discuss them.

**Solution.**

**Why we need them.** Most engineering problems have no closed-form answer.

1. **No analytic solution exists.** A coupled circuit, a heat exchanger, a
   transmission line, a semiconductor device. The governing equation is known and
   the answer is not.
2. **The scale kills hand algebra.** A discretised PDE gives thousands of
   unknowns. A million from a fine mesh. No symbolic route exists.
3. **Data arrive irregular.** Measurements are unevenly spaced and noisy.
   Interpolation and least squares take them as they come.
4. **Experiments are expensive.** A simulation can be rerun at any parameter
   value, for free, long before the hardware is built.
5. **Design needs iteration.** An optimiser calls the solver hundreds of times
   while it searches.

**Sources of error.** Two families, both of which must be tracked.

| Error | What it is | Where it comes from | How to fight it |
| :-- | :-- | :-- | :-- |
| **Truncation** | The method is not exact | Replacing a derivative by a finite difference, or cutting an infinite series | Use a higher-order formula, or a smaller $h$ |
| **Round off** | Digits are lost | Floating point is finite, and each operation adds a small error | Use higher precision, or reformulate to cancel less |

**Truncation error in detail.** For a central difference,

$$\frac{f(x+h)-f(x-h)}{2h} = f'(x) + \frac{h^2}{6}f'''(x) + \cdots$$

Hence the error is $O(h^2)$: halving $h$ reduces it by a factor of 4. For the trapezoid
rule it is $O(h^2)$ too. For Euler's method it is only $O(h)$, so halving $h$
halves the error. The order of accuracy fixes the error for a given step size.

**Round off error in detail.** A number with $p$ significant digits carries a
relative uncertainty near $10^{-p}$. Every addition roughly doubles the absolute
error of the operands, and every multiplication squares the relative error. With
$n$ sequential steps the errors accumulate, giving a growth like $n \epsilon$ for
additions.

**Round off, truncation, and the optimal step size.** The two errors pull in
opposite directions.

- Truncation error $\propto h^p$, and it **falls** as $h$ falls.
- Round off error $\propto \frac{\epsilon}{h^p}$, and it **rises** as $h$ falls,
  because dividing by a small $h$ amplifies the rounding in the numerator.

The total is smallest where the two cross, and for a central difference that is
near $h \approx \epsilon^{1/3}$, about $6 \times 10^{-6}$ in double precision.
Below that, adding more points makes the answer **worse**. This is why a table
like 2020 Q.3(b), whose $y$ values are integers and so carry no rounding at all,
permits a very small $h$ with no penalty.

$$
\boxed{\text{No closed form exists, the data are irregular, and design needs many repeated solves}}
$$

---

### [2024 Q.1(c)]

**Question.** What are round off and truncation errors? Discuss how each arises in numerical computation.

**Solution.**

Both errors make the computed answer differ from the true answer. They come from
different places and cannot be removed the same way.

**Round off error.** The true value cannot be stored exactly in the machine's
finite number of digits. Every number is chopped or rounded to the nearest
representable value. It enters at every single arithmetic operation and it
accumulates, roughly like a random walk.

- **Chopping versus rounding.** Chopping always drops digits and biases the
  result downward. Rounding to nearest is unbiased but costs more work.
- **It grows with the number of operations.** $n$ steps at $10^{-16}$ each give a
  worst case of about $n \times 10^{-16}$.
- **It is amplified by ill conditioning.** A steep function turns a small input
  error into a large output error.

**Truncation error.** The exact mathematics is replaced by a finite formula. The
formula itself is wrong, and no amount of extra digits will fix it.

- **It comes from dropping terms.** A Taylor series cut at $n$ terms, an
  integral replaced by a finite sum, a derivative replaced by a finite
  difference.
- **It shrinks by making the step smaller.** A finite difference error goes as
  $h^2$, a trapezoidal rule error as $h^2$, RK4 as $h^5$.
- **It is a modelling choice, not an accident.** It is accepted on purpose, and
  the error bound gives the price.

**Comparison**

| | Round off | Truncation |
| :-- | :-- | :-- |
| Source | Finite number of digits | Dropping terms of an exact formula |
| Controlled by | More digits, better algorithm order | Smaller step size, more terms |
| Effect of shrinking $h$ | No help, often worse | Decreases |
| Sign | Random, no pattern | Fixed by which terms were dropped |
| Cure | Higher precision, rearranged sums | Refine the formula |

$$
\boxed{\text{Total error} = \text{truncation} + \text{round off} + \text{data error}}
$$

> [!warning] The trade-off in choosing $h$
> Halving the step cuts the truncation error but doubles the number of
> operations, so the round off error grows. Past some point the two curves cross
> and making $h$ smaller makes the answer worse. That crossing is the reason a
> method has an optimal step size rather than an infinitely fine one.

---

---

**Also asked here.**

- *2017 Q.1(b)* is the same question as [[NM-1.3_Accuracy_Precision_and_Significant_Digits|NM-1.3]], which is written in `NM-1.3`.
- *2017 Q.1(c)* is the same question as [[NM-1.6_Taylor_Series_and_Truncation_Error|NM-1.6]], which is written in `NM-1.6`.

---

**Answered in phase P6, in `../CT_Questions/`.**

- *CT-01 Q.1(b)* is a class-test question. Its answer is in `../CT_Questions/CT_answers_exam_style.md`, with the reasoning in `../CT_Questions/CT_answers_explanation.md`.

---

[🏠 Subtopic Index](00_Index.md) | [← Prev: NM-1.3 Accuracy, Precision & Significant Digits](NM-1.3_Accuracy_Precision_and_Significant_Digits.md) | [Next: NM-1.5 Error Representations & Propagation →](NM-1.5_Error_Representations_and_Propagation.md)
