---
title: "NM-1 · Modeling, Computers and Error Analysis"
tags:
  - numerical-methods
  - discrete-mathematics
  - topicwise-clusters
---

[🏠 Master Index](00_Index.md) | [Next Topic: NM-2 · Roots of Equations →](NM-2_Roots_of_Equations.md)

---

# NM-1 · Modeling, Computers and Error Analysis

> **Topic ID:** NM-1  
> **Section:** Section A -- Numerical Methods  
> **Exam Weight:** 🔴 High Priority (Tier 1) | 8/8 Years Examined (100% Frequency) | Typical Weight: 10–14 marks (Question 1)  
> **Subtopics Included:** 6 subtopics (NM-1.1 through NM-1.6)  
> **Origin Layer:** Authored in `../answers_exam_style/`. All numerical results and boxed equations match character-for-character.

---

## 📑 Subtopics Covered in this Cluster

| Subtopic ID | Subtopic Title | Priority | Exam Frequency | Section Navigation |
|:---|:---|:---:|:---:|:---|
| **NM-1.1** | Foundations of Numerical Methods | 🔴 | 2017, 2018, 2019, 2020, 2021, 2023, 2024 | [Jump to NM-1.1](#nm-11) |
| **NM-1.2** | Mathematical Modeling & Engineering Problem Solving | 🟡 ⚠️ | 2024, CT-01 | [Jump to NM-1.2](#nm-12) |
| **NM-1.3** | Accuracy, Precision & Significant Digits | 🟠 | 2017 | [Jump to NM-1.3](#nm-13) |
| **NM-1.4** | Error Types & Sources | 🔴 | 2017, 2018, 2019, 2020, 2024, CT-01 | [Jump to NM-1.4](#nm-14) |
| **NM-1.5** | Error Representations & Propagation | 🔴 | 2017, 2019, 2020, 2023 | [Jump to NM-1.5](#nm-15) |
| **NM-1.6** | Taylor Series & Truncation Error | 🔴 ⚠️ | 2017, 2018, 2021, 2022, 2024, CT-01 | [Jump to NM-1.6](#nm-16) |

---

<a id="nm-11"></a><a id="nm-1.1"></a>
## NM-1.1 · Foundations of Numerical Methods

### [2017 Q.1(a)]

**Question.** Define Numerical Methods? Why do we need to use numerical methods to solve engineering problems?

**Solution.**

A **numerical method** is a procedure that solves a mathematical problem by a
finite sequence of arithmetic operations, producing an approximate value in
place of an exact closed form.

**Why they are needed.** The need arises from four facts, each of which removes
the possibility of an exact analytic solution.

1. **Most equations of interest have no closed-form solution.** The circuits
   actually built, the fields actually computed and the measurements actually
   taken all lead to equations for which no formula exists.
2. **The data are measured, not derived.** A quantity available experimentally
   arrives as a finite table of values, to which differential calculus does not
   directly apply.
3. **Only arithmetic executes on a machine.** A formula involving
   differentiation, integration or a limit is not directly executable, whereas a
   sum, a product or a comparison is.
4. **Iterative improvement is inherent to design.** Impedance matching,
   cut-off placement, root finding and least-squares fitting are all performed
   by repeated improvement of an estimate, with a tolerance as the stopping
   test.

A numerical method therefore has to be judged on more than whether it gives an
answer. Its convergence, its cost, its stability, and the way its error grows
with the number of operations are all part of the method itself, and the
analysis below develops each of them.

---

### [2017 Q.8(c)]

**Question.** Write down some real life fields where there is a great importance of numerical methods.

**Solution.**

Numerical methods are indispensable wherever a problem is too large, too
nonlinear or too data-rich to be solved in closed form. The following fields
all depend on them centrally.

1. **Electrical and electronic engineering.** Nodal and mesh analysis of
   networks, transient simulation, filter design, and the solution of the
   nonlinear device equations of diodes and transistors.
2. **Signal and speech processing.** Fourieranalysis, digital filtering,
   correlation, and the compression algorithms that govern how audio and images
   are stored and transmitted.
3. **Control systems.** Simulation of feedback loops, root-locus and
   frequency-response design, and the state-space integration of a controlled
   system's behaviour.
4. **Aerospace and mechanical engineering.** Rocket performance prediction,
   computational fluid dynamics, structural analysis, and the numerical
   integration of anisotropic elastic fields.
5. **Civil and environmental engineering.** Finite-element stress analysis of
   frames and plates, flood routing, and groundwater modelling.
6. **Medicine and biology.** Reconstruction in computed tomography and MRI,
   dose calculation in radiotherapy, and the compartmental models used in
   pharmacokinetics.
7. **Finance.** Option pricing by numerical integration, portfolio
   optimisation, and the stochastic simulation that underpins risk estimation.
8. **Meteorology.** The numerical weather models that integrate the atmosphere's
   governing equations forward in time on a three-dimensional grid.

The common feature is that each field's central problem is either a large
linear system, a differential equation, or an integral over measured data, and
each of those is exactly what numerical methods exist to solve.

---

### [2018 Q.1(a)]

**Question.** What are the importances of numerical techniques in engineering? Briefly discuss.

**Solution.**

A numerical technique obtains the answer of a mathematical problem as a finite
sequence of arithmetic operations. Its importance in engineering rests on four
points.

**1. Problems with no closed form.** Most engineering problems have no
elementary solution. The integral $\int e^{-x^2}dx$, the potential in a
transistor region, and the motion of three bodies under mutual gravity all
require numerical treatment, and all three arise in practice. Where an exact
formula exists at all, it is often so long that evaluation is slower and less
accurate than a numerical scheme.

**2. Only arithmetic executes on a machine.** A numerical technique converts a
problem into additions, multiplications, comparisons and divisions, which is
exactly what a computer or a microprocessor performs. This is what turns an
analytic method into something that runs on hardware, and it is the reason
numerical techniques accompany every physical engineering discipline.

**3. Experimental and tabulated data must be used.** Measured data arrive as
discrete samples. Any quantity derived from them, whether a derivative, an
integral, a regression line or a filter output, is obtained numerically. An
engineer working from a data sheet is doing numerical analysis whether or not
the word appears.

**4. Design and optimisation are iterative.** Matching, cut-off placement,
bias-point selection and root finding are all performed by repeated
improvement of an estimate. Numerical techniques supply the estimate rule,
the stopping test and the error estimate that make iteration trustworthy.

The consequence is that a numerical technique is judged not only on whether it
converges, but on its cost, its stability, and how its error grows with the
number of operations. All three are what the analysis below develops.

---

### [2019 Q.1(a)]

**Question.** Define numerical method. How does it become popular? Why do ECE engineers require numerical methods?

**Solution.**

A **numerical method** is a procedure that obtains the answer of a mathematical
problem as a finite sequence of arithmetic operations, yielding an approximate
value in place of the exact closed form.

**Why it became popular**

1. Most engineering problems have no closed-form solution at all. The integral
   $\int e^{-x^2}\,dx$, the motion of three bodies under gravity, and the
   boundary-value problem of a transistor region have no elementary antiderivative
   or formula, yet all three must be evaluated in practice.
2. Only arithmetic can be executed by a machine. A numerical method converts a
   problem into additions, multiplications and comparisons, which is exactly what
   a computer performs.
3. The growth of computing power made long arithmetic chains cheap. Methods that
   required thousands of operations, and were therefore once unusable, became
   routine.
4. Tabulated results and hand computation gave way to direct evaluation at the
   point of interest, with the error under the engineer's control.

**Why ECE engineers require them**

1. Circuit quantities are often implicit. The diode equation
   $I = I_s(e^{V/V_T}-1)$ and the power balance $P = VI - \sum I^2R$ give $V$ and
   $I$ through equations that cannot be solved for the current in closed form.
2. Field problems reduce to difference equations. The potential distribution in
   a semiconductor region or a screening geometry is a Laplace or Poisson problem
   that is solved on a mesh, not in symbols.
3. Signal quantities are sampled. Any quantity derived from a discrete set of
   measurements, whether by differentiation, integration or a filter, is obtained
   numerically.
4. Optimisation is iterative. Impedance matching, cut-off frequency placement and
   bias-point selection are all found by repeated improvement of an estimate.

$$\boxed{\text{Numerical method} = \text{a finite arithmetic procedure for a problem without a usable closed form}}$$

---

### [2021 Q.1(a)]

**Question.** Differentiate between numerical methods and analytical methods. Why do ECE engineers require numerical methods?

**Solution.**

**Analytical method.** Manipulates symbols to reduce the problem to a closed form.
The answer is exact and valid at every point of the domain.

**Numerical method.** Approximates the problem by a form that can be evaluated
digit by digit. The answer is a pair of numbers, valid near the point computed.

| | Analytical | Numerical |
| :-- | :-- | :-- |
| Result | Closed form, exact | Approximate |
| Domain of validity | Whole domain | Local, near one point |
| Problem size it can handle | Small | Grows nearly linearly with effort |
| Round off error | None | Present at every operation |
| Effect of changing data | Instant re-evaluation | Full recomputation |
| Structure it reveals | Conservation laws, invariants | Hides them |

**Why ECE engineers need numerical methods.**

1. **Most real systems have no closed form.** A coupled circuit, a heat exchanger,
   a transmission line, a semiconductor device: none has an analytic solution.
2. **The scale is far beyond hand algebra.** Thousands of unknowns from a
   discretised PDE, or a million from a mesh. No symbolic route exists.
3. **An experiment costs real money and real time.** A finite element run or a
   circuit simulation costs nothing to repeat and can be run at any parameter
   value, long before hardware exists.
4. **The data are irregular.** Measurements arrive unevenly spaced and noisy.
   Interpolation and least squares accept them without demanding a form.
5. **Design needs iteration.** An optimiser calls the solver hundreds of times
   while searching.
6. **The accuracy is quantifiable.** Every method carries an error bound, so the
   engineer knows how far to trust the answer rather than having to hope.

$$
\boxed{\text{Analytical is exact and closed-form; numerical is approximate but reaches problems no closed form can}}
$$

---

### [2023 Q.1(a)]

**Question.** Explain the differences between analytical and numerical solution; also describe the significance of numerical analysis in engineering field.

**Solution.**

**Analytical solution.** The governing equation is solved by manipulating symbols
to get a closed form. The answer is exact and valid at every point of the
domain.

**Numerical solution.** The equation is discretised, that is approximated by a
form that can be evaluated. The answer is a pair of numbers, valid only near the
point where it was computed.

| | Analytical | Numerical |
| :-- | :-- | :-- |
| Result | Closed form, exact | Approximate |
| Domain | Whole domain | Local, near one point |
| Difficulty of problem | May be impossible | Grows slowly with size |
| Cost per answer | Fixed once derived | Grows with problem size |
| Round off error | None | Present |
| Typical size | Thousands of equations | Millions |

**Differences in detail.**

1. **Form.** Analytic gives $y = f(x)$ in symbols. Numeric gives a table of
   values or one point $y(x_0)$.
2. **Accuracy.** Analytic is exact. Numeric carries both truncation and round off
   error, and a bound on the total.
3. **Problem size.** Analytic solutions exist for a handful of textbook
   equations. Real systems give equations no one can solve in symbols, and that
   is where numeric methods begin.
4. **Changing the data.** Analytic re-evaluates instantly. Numeric must run
   again.
5. **Understanding.** Analytic reveals structure, such as a conservation law.
   Numeric hides it.

**Significance of numerical analysis in engineering.**

1. **It makes unsolvable problems solvable.** Most real systems, a coupled
   circuit, a fluid flow, a heat transfer body, have no closed form.
2. **It replaces an expensive experiment.** A structural analysis or a CFD run is
   far cheaper than a physical test, and it can be repeated at any parameter
   setting.
3. **It handles irregular data.** Measurements arrive unevenly spaced and noisy.
   Interpolation and least squares fit them without demanding a form.
4. **It supports design iteration.** Optimisation needs hundreds of evaluations,
   each one a numerical solve.
5. **It quantifies its own trust.** Every method carries an error bound, so the
   engineer knows how much to believe the answer.
6. **It is cheap in time and memory** compared with an experiment, which is why it
   is used before hardware exists.

$$
\boxed{\text{Analytical is exact and general; numerical is approximate, local, and reaches further}}
$$

---

---

**Also asked here.**

- *2020 Q.1(a)* is the same question as [[NM-1.4_Error_Types_and_Sources|NM-1.4]], which is written in `NM-1.4`.

---

<a id="nm-12"></a><a id="nm-1.2"></a>
## NM-1.2 · Mathematical Modeling & Engineering Problem Solving

### [2024 Q.1(a)]

**Question.** Explain the importance of mathematical modeling in engineering problem solving; provide examples of how a real-world engineering problem can be represented using mathematical models.

**Solution.**

Engineering problems are too large to test directly. A model is a set of equations
that captures the behaviour that matters and drops the rest.

**Why it matters**

1. A real system cannot be rebuilt or damaged on demand, but its model can be run
   as many times as needed.
2. Trials on the model are cheap. One run costs nothing compared with one
   prototype.
3. The model shows which quantity drives the result, so effort goes where it
   helps.
4. It gives numbers before the hardware exists, which supports a budget.

**How a problem becomes a model**

1. List the quantities of interest and give each a symbol and a unit.
2. Write the physics, or the statistics, that relates them.
3. State the simplifications accepted. A model is wrong somewhere by design.
4. Fix the input data and solve.
5. Compare the answer against a measurement already trusted, then correct the
   model if it is off.

**Worked example.** A reactor's coolant temperature must be known every second,
and the thermocouple is slow. Model the exponential decay of the sensor reading:
store the last reading $T_{n-1}$, then

$$
T_n = T_{n-1} + (T_\infty - T_{n-1})e^{-\Delta t/\tau}
$$

with $\tau$ the sensor time constant. The thermocouple is the real system, and
the first-order lag is the model. For $\Delta t \ll \tau$ this reduces to
$T_n - T_{n-1} \approx (\Delta t/\tau)(T_\infty - T_{n-1})$, which is the linear
formula used in a circuit.

$$\boxed{\text{Model} = \text{physics written as equations, with stated limits}}$$

---

**Answered in phase P6, in `../CT_Questions/`.**

- *CT-01 Q.1(a)* is a class-test question. Its answer is in `../CT_Questions/CT_answers_exam_style.md`, with the reasoning in `../CT_Questions/CT_answers_explanation.md`.

---

<a id="nm-13"></a><a id="nm-1.3"></a>
## NM-1.3 · Accuracy, Precision & Significant Digits

### [2017 Q.1(b)]

**Question.** Define the following terms with example: (i) Accuracy (ii) Precision (iii) truncation error (iv) round off error.

**Solution.**

**Accuracy** is the closeness of a computed or measured value to the true
value. Quantitatively it is $1 - |{\text{relative error}}|$, or, as a
percentage, $100(1 - |{\text{relative error}}|)$. Accuracy is an absolute
measure: it does not depend on how far apart repeated readings are.

*Example.* A voltmeter reads $9.8\ \text{V}$ across a true $10\ \text{V}$
supply. The relative error is $-0.02$, so the accuracy is $98\%$.

**Precision** is the closeness of repeated measurements of the same quantity to
one another. It quantifies the spread of the readings, and is expressed as
$100(1 - |{\text{relative spread}}|)$ or through the variance of the readings.
Precision is a relative measure: it says nothing about whether the cluster of
readings is near the true value.

*Example.* Five readings of the same supply give $9.8, 9.9, 9.8, 9.9, 9.8$. The
spread is $0.1$ in $9.8$, about $1\%$, so the readings are $99\%$ precise. They
are still only $98\%$ accurate, because the whole cluster sits low.

**Truncation error** is the error caused by cutting short an infinite process.
Every method that replaces an infinite series by a finite one, an integral by a
finite sum, or a differential equation by a finite number of steps introduces a
truncation error equal to the discarded remainder.

*Example.* $\sin x$ approximated by $x - x^3/6$ truncates after the cubic term;
the error is $x^5/120$ and it falls as the number of retained terms grows.

**Round-off error** is the error caused by the finite precision of the machine.
Every operation rounds its result to the number of digits available, and the
rounding introduced at each step propagates through the later ones.

*Example.* On a machine holding six significant digits, $1/3$ is stored as
$0.333333$. Adding it three times gives $0.999999$, not $1$, and the $10^{-6}$
shortfall is round-off error.

---

### [2017 Q.3(a)]

**Question.** Sum all the numbers of provided list: $0.1532, 15.45, 0.000354, 305.4, 8.12, 143.3$ where in each of which all the given digits are correct.

**Solution.**

**Approach 1: Direct arithmetic sum.**
Adding the given numbers directly:

$$0.1532 + 15.45 + 0.000354 + 305.4 + 8.12 + 143.3 = 472.423554$$

$$\boxed{472.423554}$$

**Approach 2: Standard textbook procedure for approximate numbers (S.S. Sastry, Ex. 1.7).**
In numerical analysis, the statement *"where in each of which all the given digits are correct"* indicates that each number is an approximate value rounded to its specified decimal places, with an absolute error not exceeding half a unit in the last decimal digit ($\Delta x_i \le 0.5 \times 10^{-m}$).

Following the standard textbook procedure for adding numbers of different accuracies:
1. **Identify numbers with the largest absolute error:**
   The numbers with the fewest decimal places are $305.4$ and $143.3$ (1 decimal place). The absolute error in each is $E_A = 0.05$.
2. **Round all other numbers retaining one additional digit (2 decimal places):**
   - $0.1532 \to 0.15$
   - $15.45 \to 15.45$
   - $0.000354 \to 0.00$
   - $8.12 \to 8.12$
3. **Compute the sum:**
   $$S = 305.4 + 143.3 + 0.15 + 15.45 + 0.00 + 8.12 = 472.42$$
4. **Round off the sum by discarding one digit (to 1 decimal place):**
   $$S \approx 472.4$$
5. **Error bound:**
   The absolute error in the sum is $E_A = 2(0.05) + 4(0.005) = 0.10 + 0.02 = 0.12$. Adding the rounding error ($0.01$) gives total maximum absolute error $0.13$.
   Hence, $S = 472.42 \pm 0.13$ (or $472.4$).

---

<a id="nm-14"></a><a id="nm-1.4"></a>
## NM-1.4 · Error Types & Sources

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

<a id="nm-15"></a><a id="nm-1.5"></a>
## NM-1.5 · Error Representations & Propagation

### [2017 Q.3(b), 2023 Q.1(b)]

**Appeared in:** 2017 Q.3(b), 2023 Q.1(b)

**Question.** Given that $u = \frac{5xy^2}{z^3}$. Find the relative error at $x = y = z = 1$ when the errors in each of $x, y, z$ is $0.001$.

**Solution.**

**Logarithmic differentiation.** With $u = 5xy^2z^{-3}$, taking natural
logarithms,

$$\ln u = \ln 5 + \ln x + 2\ln y - 3\ln z$$

and differentiating,

$$\frac{du}{u} = \frac{dx}{x} + 2\frac{dy}{y} - 3\frac{dz}{z}$$

**Evaluate at $x = y = z = 1$.** At that point,

$$\frac{du}{u} = dx + 2\,dy - 3\,dz$$

With $dx = dy = dz = 0.001$:

$$\left|\frac{du}{u}\right|_{\text{worst}} = 0.001 + 2(0.001) + 3(0.001) = 6(0.001) = 0.006$$

$$\boxed{\left|\frac{du}{u}\right| \le 6\times10^{-3} = 0.6\%}$$

**Independent errors.** If the three errors are independent random quantities,
they add in quadrature rather than arithmetically:

$$\left|\frac{du}{u}\right|_{\text{rms}} = 0.001\sqrt{1 + 4 + 9} = 0.001\sqrt{14} = 3.742\times10^{-3}$$

and under the independence assumption the relative error is $0.374\%$. The
factor $5$ contributes nothing, being exact.

---

### [2019 Q.1(c)]

**Question.** What are the error representations? Two PT-voltmeter arrangements give $999\text{V}$ and $9999\text{V}$ instead of $1\text{kV}$ and $10\text{kV}$. Obtain error by all possible error representations. Hence comment on error strength of the readings.

**Solution.**

**The representations.** Given a true value $T$ and an approximate value $A$,
with $e = A - T$:

1. **Absolute error:** $e = A - T$, and its magnitude $|e|$.
2. **Relative error:** $\dfrac{e}{T}$, the error measured against the true value.
3. **Percentage error:** $100\dfrac{e}{T}$.
4. **Relative (or percentage) accuracy:** $\dfrac{A}{T}$, equivalently
   $1 - \left|\dfrac{e}{T}\right|$, which measures how near $A$ is to $T$.
5. **Limiting error (error bound):** a stated bound $|e| \le \varepsilon$
   within which the value is guaranteed to lie.

**Arrangement 1: $A = 999\ \text{V}$, $T = 1000\ \text{V}$.**

$$e = 999 - 1000 = -1\ \text{V}, \qquad |e| = 1\ \text{V}$$

$$E_{\text{rel}} = \frac{-1}{1000} = -10^{-3} = -0.1\%$$

$$E_{\text{rel, reading}} = \frac{-1}{999} = -1.001 \times 10^{-3} = -0.1001\%$$

$$\text{Accuracy} = \frac{999}{1000} = 0.999 = 99.9\%$$

**Arrangement 2: $A = 9999\ \text{V}$, $T = 10000\ \text{V}$.**

$$e = 9999 - 10000 = -1\ \text{V}, \qquad |e| = 1\ \text{V}$$

$$E_{\text{rel}} = \frac{-1}{10000} = -10^{-4} = -0.01\%$$

$$E_{\text{rel, reading}} = \frac{-1}{9999} = -1.0001 \times 10^{-4} = -0.010001\%$$

$$\text{Accuracy} = \frac{9999}{10000} = 0.9999 = 99.99\%$$

**Comment on the error strength.** The absolute error is identical in the two
arrangements, $1\ \text{V}$, so the absolute error separates them not at all.
Against the true value, the $9999\ \text{V}$ reading has a relative error of
$0.01\%$ while the $999\ \text{V}$ reading has $0.1\%$, a factor of ten
difference. The $9999\ \text{V}$ reading is therefore the stronger one.

$$\boxed{|e| = 1\ \text{V}\ \text{for both, but}\ E_{\text{rel}} = 10^{-3}\ \text{against}\ 10^{-4}}$$

> [!info] Check against the exact ratios
> The ratio of the two relative errors equals the inverse ratio of the true
> values: $\dfrac{10^{-3}}{10^{-4}} = 10 = \dfrac{10000}{1000}$. A common absolute
> error on magnitudes differing by a factor of ten produces relative errors
> differing by the same factor, which is the point the comment rests on.

---

### [2020 Q.1(b)]

**Question.** How are errors represented? Write down their expressions. Obtain their values to approximate a current as $9.05$ Amp instead of its true value $10$ Amp. Justify, which representation is better.

**Solution.**

**Definitions.** Let $v_t$ be the true value and $v_a$ the approximate value.

**Absolute error.** The size of the mistake, in the units of the quantity.

$$E_a = v_a - v_t \qquad \text{or} \qquad |E_a| = |v_a - v_t|$$

It is the only error directly measurable, and it carries the same units
as the answer.

**Relative error.** The mistake as a fraction of the true value. It is
dimensionless, so it can be compared across quantities of different size.

$$E_r = \frac{v_a - v_t}{v_t} \qquad \text{percentage relative error} = \frac{v_a - v_t}{v_t} \times 100$$

The denominator is the **true** value, not the approximate one. That choice is
what makes the measure meaningful, and it is the point examiners check.

**Now the numbers.** $v_a = 9.05$ Amp, $v_t = 10$ Amp.

$$
E_a = 9.05 - 10 = -0.95 \text{ Amp}, \qquad |E_a| = 0.95 \text{ Amp}
$$

$$
E_r = \frac{9.05 - 10}{10} = \frac{-0.95}{10} = -0.095
$$

$$
\text{percentage relative error} = -0.095 \times 100 = -9.5\%
$$

The sign says the approximation is **low**, which absolute error alone cannot
give a quantity that can be reasoned about directly.

| Representation | Value | Units |
| :-- | --: | :-- |
| Absolute error | $0.95$ | Amp |
| Relative error | $0.095$ | none |
| Percentage relative error | $9.5\%$ | none |

**Which is better, and why.** **Relative error** is the better representation, for
three reasons.

1. **It is scale-free.** A $0.95$ Amp error is trivial on a $10$ kA line and
   fatal on a $10$ mA sensor. The relative error says $9.5\%$ in both cases, so it
   ranks the two directly.
2. **It survives unit changes.** Measure the same current in milliamps and the
   absolute error becomes $950$ mA, which looks ten times worse. The relative
   error is still $0.095$. The relative error is invariant.
3. **It is what stopping criteria use.** A solver halts when the *relative* step
   falls below a tolerance, so that the test means the same thing at any
   magnitude.

Where absolute error wins: when the quantity is itself an error, a tolerance, or
a dimensional quantity where a fraction makes no sense, such as a length or a
time. Reporting "the beam is off by $2$ mm" beats "off by $0.4\%$".

> [!warning] The trap is the denominator
> Writing $\frac{9.05 - 10}{9.05} = -0.10497$ is the classic error. It looks
> reasonable and it is wrong. That figure is the error relative to the
> **approximate** value, which is not a standard measure and which changes as the
> iteration improves. Only the true value belongs in the denominator, and here it
> is $10$, not $9.05$.
>
> The gap is small, $9.5\%$ against $10.5\%$, and easy to overlook. At $99.5$
> against $100$ the same slip gives $0.5\%$ instead of $0.50\%$, still small, and
> students who never check it never find out.
>
> **Related:** this is the same distinction as 2024 Q.1(b) and 2023 Q.1(b). Fix
> the true value in memory: *relative error is always taken over the true value.*

$$
\boxed{|E_a| = 0.95 \text{ Amp}, \qquad E_r = -0.095, \qquad \text{percentage} = -9.5\%}
$$

---

---

**Also asked here.**

- *CT-02B Q.1(c)* is the same question as [[NM-3.5_Gauss_Seidel_Iteration|NM-3.5]], which is written in `NM-3.5`.

---

<a id="nm-16"></a><a id="nm-1.6"></a>
## NM-1.6 · Taylor Series & Truncation Error

### [2017 Q.1(c)]

**Question.** Evaluate $e^{-5}$ using following two approaches and compare with the true value of $6.737947 \cdot 10^{-3}$ as terms are added: $e^{-x} = 1 - x + \frac{x^2}{2!} - \frac{x^3}{3!} + \cdots \quad \text{and} \quad e^{-x} = \frac{1}{e^x} = \frac{1}{1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \cdots}$.

**Solution.**

**Approach A: the alternating series directly, with $x = 5$.**

| Terms $k$ | Sum $S_k = \sum_{n=0}^{k-1}\dfrac{(-5)^n}{n!}$ | Error $|S_k - 6.737947\times10^{-3}|$ |
| :--: | :-- | :-- |
| 1 | $1$ | $9.933\times10^{-1}$ |
| 2 | $-4$ | $4.007$ |
| 3 | $8.5$ | $8.493$ |
| 4 | $-12.3333$ | $1.234\times10^{1}$ |
| 5 | $13.7083$ | $1.370\times10^{1}$ |
| 8 | $-6.1329$ | $6.140$ |
| 10 | $-1.8271$ | $1.834$ |
| 12 | $-3.5921\times10^{-1}$ | $3.659\times10^{-1}$ |
| 14 | $-4.5555\times10^{-2}$ | $5.229\times10^{-2}$ |
| 15 | $2.4457\times10^{-2}$ | $1.772\times10^{-2}$ |

The partial sums grow to $13.7$ before they even begin to fall. At $x = 5$ the
largest term is $\dfrac{5^5}{5!} = 26.0417$, which is **over three thousand
times** the final answer. Every partial sum is dominated by that term, and no
amount of further addition repairs it on a finite-precision machine: the
cancellation destroys more digits than the machine holds.

**Approach B: the reciprocal of the positive series, with $x = 5$.**

| Terms $k$ | Sum $T_k = \sum_{n=0}^{k-1}\dfrac{5^n}{n!}$ | $\dfrac{1}{T_k}$ | Error |
| :--: | :-- | :-- | :-- |
| 1 | $1$ | $1$ | $9.933\times10^{-1}$ |
| 2 | $6$ | $1.6667\times10^{-1}$ | $1.599\times10^{-1}$ |
| 3 | $18.5000$ | $5.4054\times10^{-2}$ | $4.732\times10^{-2}$ |
| 5 | $65.3750$ | $1.5296\times10^{-2}$ | $8.558\times10^{-3}$ |
| 8 | $128.6190$ | $7.7749\times10^{-3}$ | $1.037\times10^{-3}$ |
| 10 | $143.6895$ | $6.9595\times10^{-3}$ | $2.215\times10^{-4}$ |
| 12 | $147.6038$ | $6.7749\times10^{-3}$ | $3.694\times10^{-5}$ |
| 14 | $148.3096$ | $6.7427\times10^{-3}$ | $4.706\times10^{-6}$ |
| 15 | $148.3796$ | $6.7395\times10^{-3}$ | $1.525\times10^{-6}$ |

All terms are positive, so no cancellation occurs, and the sum rises
monotonically towards $e^5 = 148.4132$. The reciprocal approaches the true
value from above, reaching four significant figures at the sixteenth term.

**The comparison.**

| | Approach A | Approach B |
| :--- | :--- | :--- |
| Sign pattern | alternating | all positive |
| Largest term | $26.0417$ at $n = 5$ | $26.0417$ at $n = 5$ |
| Relative size of that term | $\approx 3866 \times$ the result | $\approx 3866 \times$ the result |
| Cancellation | catastrophic | none |
| Behaviour | diverges then converges, pathologically | monotone |
| Terms for 4 significant figures | 23 | 16 |

$$\boxed{\text{Approach A is unusable at } x = 5; \text{ Approach B reaches } 6.7395\times10^{-3} \text{ in 15 terms}}$$

> [!info] Check by the exact reciprocal and the general warning
> The true value is $e^{-5} = 1/e^5 = 1/148.4132 = 6.737947\times10^{-3}$, the
> figure printed in the question, so Approach B's reciprocal is the direct route
> and Approach A must in principle reach the same place. The reason it does not
> is that at $x = 5$ the condition for the alternating series to be numerically
> safe, that the result is not small compared with the largest term, fails by a
> factor of nearly four thousand. Approach A does eventually converge, but only
> at the twenty-third term, against Approach B's sixteenth, and it passes
> through a partial sum of $-6.1329$ and one of $+13.7083$ on the way. The
> practical rule is that $e^{-x}$ for $x \gtrsim 1$ should be evaluated as
> $1/e^x$, never as the alternating series, because the cancellation grows with
> $x$. The two routes are expected to agree mathematically and to disagree
> numerically, which is the point of the comparison.

---

### [2018 Q.1(c)]

**Question.** Find the number of terms in the exponential series such that their sum gives the value of $e^x$ correct to five decimal places for all values of $x$ in the range $0 \le x \le 1$.

**Solution.**

**The series and its remainder.** For $0 \le x \le 1$,

$$e^x = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \cdots + \frac{x^n}{n!} + \cdots$$

After $k$ terms the remainder is, by Taylor's theorem with Lagrange form,

$$R_k = \frac{e^{\xi}x^k}{k!}, \qquad 0 < \xi < x$$

Since $0 \le x \le 1$ and $e^{\xi} \le e$, the largest possible remainder is
attained at $x = 1$ and

$$|R_k| \le \frac{e}{k!} = \frac{2.718282}{k!}$$

"Correct to five decimal places" requires the error to be below
$0.5 \times 10^{-5}$.

**Test $k$.** Taking the successive values:

| $k$ | Tail bound $\dfrac{1}{k!}\dfrac{k+1}{k}$ | Verdict |
| :--: | :-- | :-- |
| 8 | $\dfrac{1}{40320}\left(\dfrac{9}{8}\right) = 2.786 \times 10^{-5}$ | too large |
| 9 | $\dfrac{1}{362880}\left(\dfrac{10}{9}\right) = 3.062 \times 10^{-6}$ | below $5\times10^{-6}$ |

Hence the remainder tail is bounded by
$R_9 \le 3.062 \times 10^{-6} < 0.5 \times 10^{-5}$, which certifies 9 terms.

**Direct check at the worst point $x = 1$.** Summing the first nine terms:

$$S_9 = 1 + 1 + \frac{1}{2!} + \frac{1}{3!} + \frac{1}{4!} + \frac{1}{5!} + \frac{1}{6!} + \frac{1}{7!} + \frac{1}{8!}$$

$$S_9 = 2 + 0.5 + 0.166667 + 0.041667 + 0.008333 + 0.001389 + 0.000198 + 0.0000248$$

$$S_9 = 2.71827877$$

and $e = 2.71828183$, so the actual error is

$$|e - S_9| = 3.06 \times 10^{-6} < 0.5 \times 10^{-5}$$

With eight terms $S_8 = 2.71825397$, giving $|e - S_8| = 2.79 \times 10^{-5}$,
which is too large. Nine terms are therefore sufficient, and eight are not.

$$\boxed{9\ \text{terms}}$$

> [!info] Check by the Lagrange bound and exact tail
> The error after nine terms is the tail $R_9 = \sum_{n=9}^{\infty}\dfrac{1}{n!}$.
> Since $\dfrac{1}{9!} = 2.7557\times10^{-6}$ and the tail is bounded by
> $\dfrac{1}{9!}\left(1 + \dfrac{1}{10} + \dfrac{1}{10\cdot11} + \cdots\right) < \dfrac{10}{9\cdot9!} = 3.062\times10^{-6}$,
> the exact error $3.06\times10^{-6}$ clears the tolerance $0.5\times10^{-5}$ cleanly.
> Note that the cruder Lagrange bound $\dfrac{e}{k!}$ gives $\dfrac{e}{9!} = 7.491\times10^{-6}$,
> which exceeds $5\times10^{-6}$ only because $e \approx 2.718$ is a loose bound for $e^\xi$ on $[0,1]$;
> the exact geometric tail certifies that nine terms clear the tolerance while eight do not.

---

### [2021 Q.1(c)]

**Question.** Compute the value of $\ln 3$ correct to five decimal places using Taylor's series expansion.

**Solution.**

**Step 1. Choose a series that converges.** The familiar expansion

$$
\ln(1+x) = x - \frac{x^2}{2} + \frac{x^3}{3} - \cdots
$$

converges only for $\lvert x \rvert < 1$. Here $3 = 1 + 2$, so $x = 2$ and **the
series diverges**. Substituting $x = 2$ and adding terms gives a number that drifts
away from $\ln 3$ forever.

**Step 2. Use the hyperbolic form instead.** Write

$$
\ln\frac{1+y}{1-y} = 2\left(y + \frac{y^3}{3} + \frac{y^5}{5} + \cdots\right),
\qquad \lvert y \rvert < 1
$$

Set $\frac{1+y}{1-y} = 3$. Then $1 + y = 3 - 3y$, so $4y = 2$ and

$$
y = \frac{3-1}{3+1} = \frac{1}{2}
$$

which satisfies $\lvert y\rvert < 1$.

**Step 3. Expand.**

$$
\ln 3 = 2\left[\frac{1}{2} + \frac{1}{8 \times 3} + \frac{1}{32 \times 5} + \frac{1}{128 \times 7} + \frac{1}{512 \times 9} + \frac{1}{2048 \times 11} + \frac{1}{8192 \times 13} + \cdots\right]
$$

**Step 4. Add terms until the error is below $\frac{1}{2} \times 10^{-5}$.**

| Terms | Partial sum | Error |
| --: | --: | --: |
| 5 | 1.0984995040 | $1.13 \times 10^{-4}$ |
| 6 | 1.0985882824 | $2.40 \times 10^{-5}$ |
| 7 | 1.0986070624 | $5.23 \times 10^{-6}$ |
| 8 | 1.0986111314 | $1.16 \times 10^{-6}$ |

Seven terms give an error of $5.23 \times 10^{-6}$, still above $\frac{1}{2}10^{-5}$.
Eight terms give $1.16 \times 10^{-6}$, comfortably inside, so **eight terms are
required**.

**Step 5. Round.**

$$
\boxed{\ln 3 = 1.09861}
$$

> [!info] Check by an independent route
> Split $\ln 3 = \ln 2 + \ln 1.5$ and use $y = \frac{1}{3}$ and $y = \frac{1}{5}$
> respectively. With twelve terms each, $\ln 2 = 0.6931471805$ and
> $\ln 1.5 = 0.4054651081$, and the sum is $1.0986122887$, whose first five
> decimals are **1.09861**. The same answer from a different decomposition.
>
> The closed-form check is that $\ln 3 = 1.0986122886681098$, and
> $\lvert 1.0986111314 - 1.0986122887 \rvert = 1.16 \times 10^{-6}$, matching the
> table.

> [!warning] The series diverges; the arithmetic does not fail
> With $x = 2$ the partial sums **increase** past $\ln 3$ and keep going, which is
> the sign of a divergent series. Two standard repairs:
>
> 1. Use the hyperbolic form above with $y = \frac{a-1}{a+1}$, which is always inside the radius once $a > 1$.
> 2. Split the argument so each piece has $\lvert x\rvert < 1$, as $\ln 3 = \ln 2 + \ln 1.5$.
>
> A third option is $\ln 3 = 2\,\text{artanh}\frac{1}{2}$ followed by repeated
> halving of the argument. The first two are enough for five decimals.

> [!note] Error estimate, and why the bound is not the same as the actual error
> The tail after $N$ terms is bounded by
> $$2\sum_{k=N}^{\infty}\frac{y^{2k+1}}{2k+1} < \frac{2y^{2N+1}}{(2N+1)(1-y^2)}, \qquad y = \frac{1}{2}$$
> | $N$ | Bound | Below $\frac{1}{2}10^{-5}$? |
> | --: | --: | :-: |
> | 7 | $\frac{2(0.5)^{15}}{15 \times 0.75} = 5.425 \times 10^{-6}$ | No |
> | 8 | $\frac{2(0.5)^{17}}{17 \times 0.75} = 1.197 \times 10^{-6}$ | Yes |
>
> Two different numbers appear for seven terms, and both are correct:
> the **bound** $5.425\times10^{-6}$ comes from the geometric estimate above, while
> the **actual** error is $1.0986122887 - 1.0986070624 = 5.226\times10^{-6}$, which
> the table lists. The true error is always the smaller of the two, because the
> bound replaces each remaining denominator $2k+1$ by the larger value $2N+1$.
> Both exceed $5\times10^{-6}$, so seven terms fail on either count, and eight
> terms pass on both.

---

### [2022 Q.1(b)]

**Question.** Evaluate $f(1)$ using Taylor's series for $f(x)$, where $f(x) = x^3 - 3x^2 + 5x - 10$.

**Solution.**

**Step 1. Taylor's series about $x = 0$.**

$$
f(x) = f(0) + x f'(0) + \frac{x^2}{2!}f''(0) + \frac{x^3}{3!}f'''(0) + \frac{x^4}{4!}f^{(4)}(0) + \cdots
$$

**Step 2. Differentiate and evaluate at 0.**

| | $f(x)$ | $f'(x)$ | $f''(x)$ | $f'''(x)$ | $f^{(4)}(x)$ |
| :-- | :-- | :-- | :-- | :-- | :-- |
| | $x^3-3x^2+5x-10$ | $3x^2-6x+5$ | $6x-6$ | $6$ | $0$ |

$$
f(0) = -10, \qquad f'(0) = 5, \qquad f''(0) = -6, \qquad f'''(0) = 6, \qquad f^{(4)} = 0
$$

**Step 3. The series terminates.** Since the fourth derivative is identically zero,
the expansion is a polynomial with no terms beyond $x^3$:

$$
f(x) = -10 + 5x - 3x^2 + x^3
$$

**Step 4. Put $x = 1$.**

$$
f(1) = -10 + 5(1) - 3(1)^2 + (1)^3 = -10 + 5 - 3 + 1
$$

$$
\boxed{f(1) = -7}
$$

> [!info] Check by independent routes
> **Direct substitution.** $1 - 3 + 5 - 10 = -7$.
> **Structural check.** Because $f^{(4)} \equiv 0$, the third-order Taylor
> polynomial is **exact**, so there is no truncation error at all. The remainder
> $R_3$ is identically zero, not merely small. Route 3: factor-free Horner
> evaluation, $(-10 + 5\cdot1)\cdot1 - 3$ then $\cdot 1 + 1 = -7$.

> [!note] Why no error analysis is needed, and what the marks cover
> A cubic has an exact third-order expansion, so no error analysis is needed. The
> series must be built from derivatives rather than guessed at in order. The
> mark allocation of 4 corresponds to writing out $f'$, $f''$, $f'''$
> explicitly, which is exactly what is done above.

---

### [2024 Q.1(b)]

**Question.** Given the function $f(x) = e^x$, derive the third order Taylor series expansion around $x = 0$. Estimate the truncation error if you use this expansion to approximate $f(0.5)$.

**Solution.**

The Taylor series of $f$ about $x_0 = 0$ is

$$
f(x) = \sum_{n=0}^{\infty}\frac{f^{(n)}(0)}{n!}x^n
$$

For $f(x) = e^x$ every derivative is $e^x$, so $f^{(n)}(0) = 1$ for all $n$. Hence

$$
e^x = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \frac{x^4}{4!} + \cdots
$$

**Third order truncation**, keeping terms up to $x^3$:

$$
\boxed{e^x \approx P_3(x) = 1 + x + \frac{x^2}{2} + \frac{x^3}{6}}
$$

**At $x = 0.5$**

$$
P_3(0.5) = 1 + 0.5 + \frac{0.25}{2} + \frac{0.125}{6}
= 1 + 0.5 + 0.125 + 0.0208333
= 1.6458333
$$

**Truncation error, route 1, exact difference against the true value**

$$
e^{0.5} = 1.6487212707
$$

$$
|E_3| = |e^{0.5} - P_3(0.5)| = 1.6487212707 - 1.6458333333 = 0.0028879374
$$

**Truncation error, route 2, Lagrange remainder bound**

The remainder after three terms is

$$
R_3(x) = \frac{f^{(4)}(\xi)}{4!}x^4 = \frac{e^{\xi}}{24}x^4, \qquad 0 < \xi < x
$$

Substituting $x = 0.5$ and $e^{\xi} \le e^{0.5} = 1.6487213$ gives

$$
|R_3| \le \frac{1.6487213}{24}(0.5)^4 = \frac{1.6487213}{24}(0.0625) = 0.0042935
$$

The two routes are consistent: the exact error $0.0028879$ sits inside the bound
$0.0042935$. The first neglected term alone indicates the size of the error,
since the series terms fall fast at $x = 0.5$:

$$
\frac{x^4}{4!} = \frac{0.0625}{24} = 0.0026042
$$

$$
\boxed{P_3(0.5) = 1.6458333, \qquad |E_3| = 0.0028879 \le 0.0042935}
$$

---

[🏠 Master Index](00_Index.md) | [Next Topic: NM-2 · Roots of Equations →](NM-2_Roots_of_Equations.md)
