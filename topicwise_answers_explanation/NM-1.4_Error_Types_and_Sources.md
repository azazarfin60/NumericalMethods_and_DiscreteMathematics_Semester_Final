---
title: "NM-1.4 · Error Types & Sources"
tags:
  - numerical-methods
  - discrete-mathematics
  - topicwise
---

# NM-1.4 · Error Types & Sources

Every block below is copied from `../answers_explanation/`. The reasoning
is written once, in the year-wise file, and is not restated here.


### [2018 Q.1(b)]

**Question.** What are the algorithmic errors that may occur in numerical calculation?

*[Marks: 04]*

**Solution.**

**Algorithmic error** is the error introduced by the computation itself, as
distinct from error already present in the data you started with.

**1. Truncation error.** Every numerical method replaces an infinite process by
a finite one. An infinite series is cut after $n$ terms, an interval is cut into
$n$ panels, a differential equation is stepped with finite $h$. The discarded
remainder is the truncation error, and it is the error that *shrinks* when the
approximation is refined.

**2. Round-off error.** A machine holds finitely many digits. Every operation
rounds its result to that precision, and the rounding introduced at one step
propagates into every later step. Round-off error *grows* with the number of
operations, which is why a method can become worse when you refine too far.

**3. Propagation of error.** The two above do not simply add. A method is
**unstable** if an error introduced early is amplified downstream, and
**well-conditioned** if it is damped. The amplification factor belongs to the
algorithm, not to the arithmetic precision: a stable method stays accurate at
high precision, an unstable one does not.

**The two errors oppose.** For a method with step size $h$, truncation error
falls as a power of $h$ while round-off error grows like $1/h$ (and worse if the
recurrence is unstable). The total therefore has a *minimum* at some optimal
$h$, and below that $h$ further refinement makes the answer worse. This is the
central practical fact of numerical computation, and it is why the choice of
$h$, the stopping test and the stability of the recurrence are all part of the
method rather than details of implementation.

> [!warning] The common slip
> Students write "truncation and round-off errors are both bad, take the
> average". They are not two estimates of the same quantity that you average.
> They have opposite dependence on $h$ and only their sum matters.

---

### [2019 Q.1(b)]

**Question.** What are the errors involved in numerical methods? How do they enter into the process? Give example.

*[Marks: 04]*

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

Inherent error is not produced by the arithmetic and cannot be reduced by carrying
more digits.

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

> [!warning] The example carries two errors from different steps, and that is the point
> The $-1\%$ has two sources. The display rounding the reading to three decimals is
> round-off in the **reporting**, and the tolerance of the resistor is data error
> in the **input**. They are different steps of the list above and only one of them
> is removable by carrying more digits.
>
> **This is why "use more significant figures" is not always the answer.** If the
> error is data error, no amount of arithmetic precision recovers the information,
> and the honest response is to state a tolerance rather than to print more
> decimals.

---

### [2020 Q.1(a)]

**Question.** Why are numerical methods for? What are the sources of errors in numerical methods? Discuss them.

*[Marks: 06]*

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

$$\boxed{\text{No closed form exists, the data are irregular, and design needs many repeated solves}}$$

**Sources of error.** Two families, both of which must be tracked.

| Error | What it is | Where it comes from | How to fight it |
| :-- | :-- | :-- | :-- |
| **Truncation** | The method is not exact | Replacing a derivative by a finite difference, or cutting an infinite series | Use a higher-order formula, or a smaller $h$ |
| **Round off** | Digits are lost | Floating point is finite, and each operation adds a small error | Use higher precision, or reformulate to cancel less |

**Truncation error in detail.** For a central difference,

$$
\frac{f(x+h)-f(x-h)}{2h} = f'(x) + \frac{h^2}{6}f'''(x) + \cdots
$$

Hence the error is $O(h^2)$: halving $h$ reduces it by a factor of 4. For the
trapezoid rule it is $O(h^2)$ too. For Euler's method it is only $O(h)$, so halving
$h$ halves the error. The order of accuracy fixes the error for a given step size.

**Round off error in detail.** A number with $p$ significant digits carries a
relative uncertainty near $10^{-p}$. Every addition roughly doubles the absolute
error of the operands, and every multiplication squares the relative error. With
$n$ sequential steps the errors accumulate, giving a growth like $n\epsilon$ for
additions.

> [!warning] The two errors pull in opposite directions, and that has a consequence
> - Truncation error $\propto h^p$, and it **falls** as $h$ falls.
> - Round off error $\propto \frac{\epsilon}{h^p}$, and it **rises** as $h$ falls,
>   because dividing by a small $h$ amplifies the rounding in the numerator.
>
> The total is smallest where the two cross, and for a central difference that is
> near $h \approx \epsilon^{1/3}$, about $6 \times 10^{-6}$ in double precision.
> **Below that, adding more points makes the answer worse.**
>
> This is not a corner case. Any scheme that takes a finite difference of
> tabulated data inherits the trade, and "use more points" is not a free
> improvement. It is only free when the data are exact, because then the round
> off side is zero.

> [!note] Why Q.3(b) of this paper can use a very small $h$
> Its $y$ values are integers, $46, 66, 81, 93, 101$, and carry no rounding at
> all. With exact data the round off side of the trade vanishes, so refining the
> mesh is free and only truncation matters.
>
> **This is why some questions can be refined indefinitely and others cannot.** The
> difference is not the method, it is whether the input already carries error.
> Tables of $e^x$ rounded to four decimals, as in 2021 Q.7(c), set a floor on
> accuracy that no amount of arithmetic gets past.

---

### [2024 Q.1(c)]

**Question.** What are round off and truncation errors? Discuss how each arises in numerical computation.

*[Marks: 04, CO: 2]*

**Solution.**

**Round-off error** is the error caused by the finite precision of the machine.
A computer holding $t$ significant digits cannot represent most numbers
exactly, so every arithmetic operation rounds its result to the $t$ digits
available. That rounding, introduced at one step, propagates into every later
step.

It arises in three distinct ways, and naming the type is usually what the marks
are for:

- **Representation error**, the error in storing a number at all. $1/3$ stored
  in six digits is $0.333333$, and the error is already there before anything is
  computed.
- **Arithmetic rounding**, the error in the result of an operation. Adding two
  $t$-digit numbers can require $t+1$ digits, so the last is dropped.
- **Absorption**, when a small number is added to a large one and vanishes.
  Adding $10^{-7}$ to $10^{6}$ on a six-digit machine leaves $10^6$ unchanged;
  the small number has been absorbed without effect.

**Truncation error** is the error caused by replacing an infinite process by a
finite one. It is not a property of the machine at all: it would be present even
with infinite precision, because it comes from the method.

It arises in three ways too:

- **Cutting a series**, as with the Taylor series in part (b), where keeping $n$
  terms discards the remainder.
- **Stepping a differential equation**, as with Euler, where advancing by a finite
  $h$ discards the $O(h^2)$ and higher terms.
- **Subdividing an integral**, as with Simpson's rule, where a finite number of
  panels approximates a continuous curve.

**The opposition between them.** This is the part of the answer that
distinguishes a good response from a listing. The two errors behave differently
as a method is refined:

- Truncation error **falls** as the number of terms, panels or steps is
  increased.
- Round-off error **grows**, because more terms means more operations, and each
  operation adds its own rounding.

So the total error has a minimum at some optimal refinement level, below which
making the method finer makes the answer **worse**. This is why the answer to
"how accurately can this integral be computed" is not always "use more panels".

**Why it matters in practice.** The stability of the method, not the precision
of the machine, decides whether round-off is amplified or damped. A method is
**well-conditioned** if an error introduced early is damped in later steps, and
**unstable** if it is amplified. The same machine precision can give six correct
digits on one method and none on another.

$$\boxed{\text{Total error} = \text{truncation} + \text{round off} + \text{data error}}$$

Note the three terms, not two. **Data error** is the error already present in the
inputs, and it is not reduced by choosing a better method. A method can drive
truncation and round off down indefinitely; data error only comes down by
measuring more carefully. The three do not always add, since a truncation error
and a round-off error can partly cancel, so the practical statement is a bound
rather than an equality. The box writes the standard decomposition, which is what
an exam expects.

> [!info] Check by an independent route: the sum of $e^{-5}$ two ways
> The cleanest demonstration that the two errors are distinct is 2017 Q.1(c).
> Evaluating $e^{-5}$ as the alternating series $1 - 5 + 25/2! - \cdots$ is
> mathematically exact and numerically hopeless, because the terms reach $26$
> while the answer is $0.0067$. The truncation error goes to zero as terms are
> added, while the round-off error from the cancellation that precedes it grows
> without bound. Recasting the same computation as $1/e^5$ removes the
> cancellation entirely, and the answer then converges monotonically. The method
> changed, the arithmetic precision did not, and only the round-off error moved.
> That is the separation the definition is describing.

---

---

**Also asked here.**

- *2017 Q.1(b)* is the same question as [[NM-1.3_Accuracy_Precision_and_Significant_Digits|NM-1.3]], which is written in `NM-1.3`.
- *2017 Q.1(c)* is the same question as [[NM-1.6_Taylor_Series_and_Truncation_Error|NM-1.6]], which is written in `NM-1.6`.

---

**Answered in phase P6, in `../CT_Questions/`.**

- *CT-01 Q.1(b)* is a class-test question. Its answer is in `../CT_Questions/CT_answers_exam_style.md`, with the reasoning in `../CT_Questions/CT_answers_explanation.md`.
