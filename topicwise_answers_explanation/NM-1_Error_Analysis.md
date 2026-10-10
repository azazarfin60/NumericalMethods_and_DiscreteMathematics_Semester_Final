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
> **Origin Layer:** Authored in `../answers_explanation/`. All numerical results and boxed equations match character-for-character.

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

*[Marks: 04]*

**Solution.**

**The definition.** A **numerical method** is a procedure that solves a
mathematical problem by a *finite* sequence of arithmetic operations, producing
an approximate value in place of an exact closed form. Three words carry the
whole idea: *finite*, *arithmetic*, *approximate*.

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

> [!note] The consequence worth writing down
> A numerical method is not judged on whether it gives an answer. It is judged
> on three things: its **convergence**, its **cost**, its **stability**, and
> the way its **error grows with the number of operations**. Everything from
> Q.2(a) onward in this paper is an instance of one of those three.

---

### [2017 Q.8(c)]

**Question.** Write down some real life fields where there is a great importance of numerical methods.

*[Marks: 02]*

**Solution.**

Numerical methods are indispensable wherever a problem is too large, too
nonlinear or too data-rich to be solved in closed form. The following fields all
depend on them centrally.

1. **Electrical and electronic engineering.** Nodal and mesh analysis of
   networks, transient simulation, filter design, and the solution of the
   nonlinear device equations of diodes and transistors.
2. **Signal and speech processing.** Fourier analysis, digital filtering,
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

The common feature is that each field's central problem is either a large linear
system, a differential equation, or an integral over measured data, and each of
those is exactly what numerical methods exist to solve.

---

### [2018 Q.1(a)]

**Question.** What are the importances of numerical techniques in engineering? Briefly discuss.

*[Marks: 04]*

**Solution.**

**What a numerical technique is.** A numerical technique obtains the answer of a
mathematical problem as a *finite* sequence of arithmetic operations. Nothing
more clever than that: add, subtract, multiply, divide, compare, repeat. If you
can write the steps down so that someone else gets the same digits, it is a
numerical technique.

**Why it matters, in four points.**

1. **Most engineering problems have no closed form.** The integral
   $\int e^{-x^2}\,dx$, the potential inside a transistor region, and the motion
   of three bodies under mutual gravity all lack an elementary answer, and all
   three come up in practice. Where a closed form does exist it is often so long
   that evaluating it numerically is faster *and* more accurate.
2. **Only arithmetic runs on a machine.** A numerical technique turns a problem
   into additions, multiplications, comparisons and divisions, which is exactly
   what a CPU does. This is what converts an analytic method into something that
   can be implemented.
3. **Measured data arrive as discrete samples.** Anything derived from a data
   sheet, whether a derivative, an integral, a regression line or a filter
   output, is a numerical result. An engineer working from measurements is doing
   numerical analysis whether or not the phrase appears.
4. **Design and optimisation are iterative.** Matching, bias-point selection,
   cut-off placement and root finding are all repeated improvement of an
   estimate. The numerical technique supplies the estimate rule, the stopping
   test and the error estimate.

> [!note] The consequence worth writing down
> A numerical technique is not judged on convergence alone. It is judged on
> three things: its **cost** in operations, its **stability**, and how its
> **error grows with the number of operations**. Everything from Q.2(c) onward
> in this paper is an instance of one of those three.

---

### [2019 Q.1(a)]

**Question.** Define numerical method. How does it become popular? Why do ECE engineers require numerical methods?

*[Marks: 04]*

**Solution.**

**Definition.** A **numerical method** is a finite arithmetic procedure for
solving a problem that has no usable closed form. It replaces the problem by a
sequence of additions, subtractions, multiplications, divisions and comparisons
that can be carried out to a stated precision.

$$\boxed{\text{Numerical method} = \text{a finite arithmetic procedure for a problem without a usable closed form}}$$

**How it became popular.**

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

**Why ECE engineers require them.**

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

> [!note] The point in item 1 of each list is not the same point
> "The problem has no closed form" is a statement about the mathematics.
> "A machine can only do arithmetic" is a statement about the hardware. They are
> the same fact seen from two directions, and together they are why numerical
> methods exist at all: **there is both something to compute and a machine to
> compute it on.**
>
> The consequence for the engineer is that accuracy becomes a choice rather than
> a property. Every method has an error term, and picking a step size is choosing
> how much error to accept. That is not true of an analytic solution, which has
> none.

---

### [2021 Q.1(a)]

**Question.** Differentiate between numerical methods and analytical methods. Why do ECE engineers require numerical methods?

*[Marks: 04, CO: 1]*

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

$$\boxed{\text{Analytical is exact and closed-form; numerical is approximate but reaches problems no closed form can}}$$

> [!warning] The last row is the one that matters
> An analytical solution exposes **structure**: a conservation law, an invariant,
> a symmetry. A numerical solution gives you a number and nothing else.
>
> This is the real cost of the method, and it is not visible in the answer. An
> engineer who knows $\frac{dQ}{dt} = -kQ$ analytically knows the half-life is
> $\frac{\ln 2}{k}$ whatever $k$ is. An engineer who has run the ODE numerically
> for one particular $k$ knows a number, and has to rerun to discover the
> pattern. Use numerical methods for the answer and analytical reasoning for the
> design.

**Why ECE engineers need them.**

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

> [!note] The hybrid answer
> Almost no real computation is purely one or the other. An analytical
> reduction that leaves a small nonlinear system, solved numerically, is the
> normal pattern. The skill being marked here is knowing which part of a problem
> deserves the closed form and which part has to be iterated.

---

### [2023 Q.1(a)]

**Question.** Explain the differences between analytical and numerical solution; also describe the significance of numerical analysis in engineering field.

*[Marks: 04, CO: 1]*

**Solution.**

An analytical solution is one where you manipulate symbols until the unknown
appears on its own, and the answer is valid at every point of the domain. A
numerical solution is one where you approximate the problem by something you
can evaluate, and the answer is a number valid near the point you evaluated it
at.

**The distinction that actually matters.** An analytical answer is a *rule*; a
numerical answer is a *reading*. If the answer is $y = 3x^2 + 1$, you can
evaluate it anywhere without computing anything new. If the answer is
$y(2.5) = 19.75$, that one number is all you have, and getting $y(3)$ means
starting again.

**Side by side.**

| | Analytical | Numerical |
| :-- | :-- | :-- |
| Result | Closed form, exact | Approximate |
| Domain | Whole domain | Local, near one point |
| Difficulty of problem | May be impossible | Grows slowly with size |
| Cost per answer | Fixed once derived | Grows with problem size |
| Round off error | None | Present |
| Typical size | Thousands of equations | Millions |

**The differences, stated as points.**

1. **Form.** Analytic gives $y = f(x)$ in symbols. Numeric gives a table of
   values or one point $y(x_0)$.
2. **Accuracy.** Analytic is exact. Numeric carries both truncation error, from
   the approximation itself, and round off error, from finite precision. A good
   method reports a bound on their sum, which is the part that distinguishes
   engineering practice from guesswork.
3. **Problem size.** Analytic solutions exist for a handful of textbook
   equations. Real systems give equations nobody can solve in symbols, and that
   is exactly where numeric methods begin.
4. **Changing the data.** Analytic re-evaluates instantly. Numeric must be run
   again from the start.
5. **Understanding.** Analytic reveals structure, such as a conservation law or
   a resonance condition. Numeric hides it.

**Why numerical analysis matters in engineering.** Six reasons, and the marks
are usually spread across them.

1. **It makes unsolvable problems solvable.** Most real systems have no closed
   form: a coupled circuit, a fluid flow, a heat-transfer body, a structural
   frame. These are not hard problems, they are problems whose closed form
   nobody has written down.
2. **It replaces an expensive experiment.** A structural analysis or a CFD run
   costs a fraction of a physical test and can be repeated at any parameter
   setting. It is also the only option when the real thing cannot be built,
   because it would be dangerous or too expensive.
3. **It handles irregular data.** Measurements arrive unevenly spaced and noisy.
   Interpolation and least squares fit them without demanding a functional form
   in advance.
4. **It supports design iteration.** Optimisation needs hundreds or thousands of
   evaluations, each one a numerical solve. An analytical solution would be
   faster per evaluation but frequently does not exist.
5. **It quantifies its own trust.** Every method carries an error bound, so the
   engineer knows how far to believe the answer. This is the difference between
   a method and a guess.
6. **It is cheap in time and memory**, which is why it is used before the
   hardware exists.

$$
\boxed{\text{Analytical is exact and general; numerical is approximate, local, and reaches further}}
$$

> [!note] How four marks are usually split
> Two for the differences and two for the significance, so four clean
> differences and four significance points with one sentence each is the target.
> Writing a long paragraph on analytical versus numerical and then one sentence
> on significance will lose the second half.
>
> The word *general* in the boxed line is doing real work. Analytical solutions
> are exact *and* global; numerical ones are local by construction. That is the
> single sharpest difference and it is worth stating explicitly.

---

---

**Also asked here.**

- *2020 Q.1(a)* is the same question as [[NM-1.4_Error_Types_and_Sources|NM-1.4]], which is written in `NM-1.4`.

---

<a id="nm-12"></a><a id="nm-1.2"></a>
## NM-1.2 · Mathematical Modeling & Engineering Problem Solving

### [2024 Q.1(a)]

**Question.** Explain the importance of mathematical modeling in engineering problem solving; provide examples of how a real-world engineering problem can be represented using mathematical models.

*[Marks: 03, CO: 1]*

**Solution.**

Engineering problems are too large to test directly. A model is a set of
equations that captures the behaviour that matters and drops the rest. That last
clause is the whole idea, and it is worth being precise about: a model is not a
copy of reality, it is a deliberate simplification of it. Choosing what to leave
out is the engineering judgement, and the choice is what a modelling question is
really testing.

**Why it matters.** Four reasons, in the order they tend to be asked:

1. **A real system cannot be tested directly.** A bridge cannot be built to see
   whether it falls down. A satellite cannot be launched to check the antenna
   gain. The model can be run as many times as needed, which is the only way the
   question "does this design survive X" gets asked before the design exists.
2. **Trials on the model are almost free.** One run costs nothing compared with
   one prototype. When a trial costs nothing, you run thousands of them, and
   thousands of trials is what tells you which parameter actually matters.
3. **The model identifies the driving quantity.** With a model you can vary one
   input and hold the rest, which is exactly what an experiment cannot do.
   Finding that the answer depends on $\tau$ and not on $R$ is worth a great deal
   before any hardware is chosen.
4. **It gives numbers before the hardware exists.** A budget is a set of numbers.
   So is a specification. Both need the model first.

**How a problem becomes a model.** The five steps are the standard ones, and
they are worth learning as a sequence because the question can be asked in the
form "describe the modelling process":

1. List the quantities of interest, with a symbol and a unit for each.
2. Write the physics or the statistics that relates them.
3. State the simplifications accepted. A model is wrong somewhere by design,
   and saying where is part of the answer.
4. Fix the input data and solve.
5. Compare the answer against a measurement already trusted, and correct the
   model if it is off.

**The worked example.** The answer script uses a thermocouple on a reactor
coolant loop. The thermocouple is slow, and the model is a first-order lag:

$$T_n = T_{n-1} + (T_\infty - T_{n-1})e^{-\Delta t/\tau}$$

with $\tau$ the sensor time constant. The reason this model is chosen is that
first-order lag is the standard description of any sensor whose response is
limited by a single energy or charge storage. For $\Delta t \ll \tau$ the
exponential reduces to a linear update, which is the form that can actually be
implemented in a loop running every second.

$$\boxed{\text{Model} = \text{physics written as equations, with stated limits}}$$

> [!note] What the marker is looking for
> Three marks divide naturally into three things: a definition, the reasons, and
> an example. The example needs to be concrete, with symbols and units. A common
> loss of marks is giving the reasons as a list of adjectives rather than as
> statements about what a model lets you do that an experiment does not.

---

**Answered in phase P6, in `../CT_Questions/`.**

- *CT-01 Q.1(a)* is a class-test question. Its answer is in `../CT_Questions/CT_answers_exam_style.md`, with the reasoning in `../CT_Questions/CT_answers_explanation.md`.

---

<a id="nm-13"></a><a id="nm-1.3"></a>
## NM-1.3 · Accuracy, Precision & Significant Digits

### [2017 Q.1(b)]

**Question.** Define the following terms with example: (i) Accuracy (ii) Precision (iii) truncation error (iv) round off error.

*[Marks: 04]*

**Solution.**

**Accuracy** is the closeness of a computed or measured value to the *true*
value. Quantitatively it is $1 - |{\text{relative error}}|$, or as a percentage
$100(1 - |{\text{relative error}}|)$. Accuracy is an **absolute** measure: it
says nothing about how far apart repeated readings are.

*Example.* A voltmeter reads $9.8\ \text{V}$ across a true $10\ \text{V}$
supply. The relative error is $-0.02$, so the accuracy is $98\%$.

**Precision** is the closeness of repeated measurements of the same quantity to
*one another*. It quantifies the spread of the readings, and is expressed as
$100(1 - |{\text{relative spread}}|)$ or through the variance. Precision is a
**relative** measure: it says nothing about whether the cluster sits near the
true value.

*Example.* Five readings of the same supply give $9.8, 9.9, 9.8, 9.9, 9.8$. The
spread is $0.1$ against a level of $9.8$, about $1\%$, so the readings are
$99\%$ precise. They are still only $98\%$ accurate, because the whole cluster
sits low.

> [!note] The classic picture, and why both examples are in the question
> Draw four targets. The four groups land on the bullseye, off the bullseye but
> tightly grouped, loosely grouped on the bullseye, and loosely grouped off it.
> **Accuracy** is distance from the bullseye; **precision** is how tightly the
> shots cluster. The pair here, "$99\%$ precise and $98\%$ accurate", is the
> second of those four. A repeatability cluster that sits $2\%$ off is the
> situation where averaging will not help you, and it is worth recognising on
> sight in the laboratory.

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

> [!warning] The pair that students merge
> Truncation error shrinks when you take more terms, more panels or a smaller
> $h$. Round-off error *grows* when you do any of those, because every extra
> operation is another rounding. They have opposite dependence on the same
> quantity, and the total error is not minimised by working harder. This is the
> point of Q.1(c), which is the demonstration rather than the statement.

---

### [2017 Q.3(a)]

**Question.** Sum all the numbers of provided list: $0.1532, 15.45, 0.000354, 305.4, 8.12, 143.3$ where in each of which all the given digits are correct.

*[Marks: 03]*

**Solution.**

**The sum.**

$$0.1532 + 15.45 + 0.000354 + 305.4 + 8.12 + 143.3 = 472.423554$$

$$\boxed{472.423554}$$

**Two perspectives are important for this question:**

**Perspective 1: Direct arithmetic sum.**
Adding the six numbers directly on a calculator:

$$0.1532 + 15.45 + 0.000354 + 305.4 + 8.12 + 143.3 = 472.423554$$

All six numbers are terminating decimals, and their rational sum is exactly $\frac{236211777}{500000} = 472.423554$. If an examiner intends this as a pure machine-precision addition problem, no rounding is introduced during the addition.

**Perspective 2: Standard textbook procedure for approximate numbers (S.S. Sastry, Ex. 1.7).**
This question is adapted directly from **S.S. Sastry's *Introductory Methods of Numerical Analysis* (Section 1.3, Example 1.7)**. In numerical methods, the phrase *"where in each of which all the given digits are correct"* is the standard definition of an approximate number rounded to its given decimal places. The absolute error in any number correct to $m$ decimal places does not exceed $0.5 \times 10^{-m}$.

Sastry establishes the standard 4-step procedure for adding numbers of different absolute accuracies:
1. **Isolate the numbers with the greatest absolute error:**
   Here, $305.4$ and $143.3$ have only 1 decimal place, so their absolute error is $\Delta = 0.05$ each.
2. **Round off all other numbers retaining one digit more than the isolated numbers (i.e., 2 decimal places):**
   - $0.1532 \to 0.15$
   - $15.45 \to 15.45$
   - $0.000354 \to 0.00$
   - $8.12 \to 8.12$
3. **Compute the sum:**
   $$S = 305.4 + 143.3 + 0.15 + 15.45 + 0.00 + 8.12 = 472.42$$
4. **Round off the sum by discarding one digit:**
   $$S \approx 472.4$$

**Absolute error in the sum:**
- Two numbers have absolute error $0.05$ each $\implies 2(0.05) = 0.10$.
- The remaining four rounded numbers each have absolute error $0.005 \implies 4(0.005) = 0.02$.
- Subtotal error: $0.10 + 0.02 = 0.12$.
- Adding the rounding error ($0.01$) gives total error bound $E_A = 0.12 + 0.01 = 0.13$.
Hence, $S = 472.42 \pm 0.13$, or $S \approx 472.4$.

Presenting both the exact decimal sum $472.423554$ and Sastry's textbook approximate-sum procedure ($472.4$) guarantees full marks under any examiner.

---

<a id="nm-14"></a><a id="nm-1.4"></a>
## NM-1.4 · Error Types & Sources

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

---

<a id="nm-15"></a><a id="nm-1.5"></a>
## NM-1.5 · Error Representations & Propagation

### [2017 Q.3(b), 2023 Q.1(b)]

**Appeared in:** 2017 Q.3(b), 2023 Q.1(b)

**Question.** Given that $u = \frac{5xy^2}{z^3}$. Find the relative error at $x = y = z = 1$ when the errors in each of $x, y, z$ is $0.001$.

*[Marks: 03]*

**Solution.**

**The method.** Logarithmic differentiation. With $u = 5xy^2z^{-3}$, take natural
logarithms,

$$\ln u = \ln 5 + \ln x + 2\ln y - 3\ln z$$

and differentiate:

$$\frac{du}{u} = \frac{dx}{x} + 2\frac{dy}{y} - 3\frac{dz}{z}$$

**Why this method.** The relative error is what is asked for, and the
logarithmic derivative *is* the relative error in differential form. Taking
logarithms first is what linearises the products and powers into a sum, and a
sum of relative errors is what the question can be answered from.

**Evaluate at $x = y = z = 1$.** At that point each ratio is its own variable,
so

$$\frac{du}{u} = dx + 2\,dy - 3\,dz$$

**The worst case.** The three errors are not stated to be independent, so the
safe reading is that all three act in the direction that maximises the
magnitude. The coefficients $1, 2, -3$ have absolute values $1, 2, 3$, so

$$\left|\frac{du}{u}\right|_{\text{worst}} = 0.001 + 2(0.001) + 3(0.001) = 6(0.001) = 0.006$$

$$\boxed{\left|\frac{du}{u}\right| \le 6\times10^{-3} = 0.6\%}$$

**Note what the exponent $2$ on $y$ and the exponent $-3$ on $z$ did.** $y$
appears twice, so an error in $y$ is counted twice. $z$ appears three times, so
an error in $z$ is counted three times. The sensitivity of a product is
proportional to each factor's *power*, not to its presence, and a factor raised
to a high power is a correspondingly larger lever on the answer. The constant
$5$ contributes nothing, being exact.

> [!info] If the errors are independent, the answer is different
> The bound above is the worst case over all sign combinations. If instead the
> three errors are independent random quantities with equal standard deviation,
> they add in quadrature and
> $$\left|\frac{du}{u}\right|_{\text{rms}} = 0.001\sqrt{1^2 + 2^2 + 3^2} = 0.001\sqrt{14} = 3.742\times10^{-3},$$
> that is $0.374\%$, and the relative error is $0.374\%$.
>
> The two differ by a factor of $1.6$, and which is right depends on a
> statement about the errors that the question does not make. The worst-case
> reading is the one to report when nothing is stated, because it holds
> regardless of the sign pattern. Worth knowing both, and worth saying which
> one you are quoting.

---

### [2019 Q.1(c)]

**Question.** What are the error representations? Two PT-voltmeter arrangements give $999\text{V}$ and $9999\text{V}$ instead of $1\text{kV}$ and $10\text{kV}$. Obtain error by all possible error representations. Hence comment on error strength of the readings.

*[Marks: 04]*

**Solution.**

**The representations.** Given a true value $T$ and an approximate value $A$,
with $e = A - T$:

1. **Absolute error:** $e = A - T$, and its magnitude $|e|$.
2. **Relative error:** $\dfrac{e}{T}$, the error measured against the true value.
3. **Percentage error:** $100\dfrac{e}{T}$.
4. **Relative (or percentage) accuracy:** $\dfrac{A}{T}$, equivalently
   $1 - \left|\dfrac{e}{T}\right|$, which measures how near $A$ is to $T$.
5. **Limiting error (error bound):** a stated bound $|e| \le \varepsilon$ within
   which the value is guaranteed to lie.

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
$0.01\%$ while the $999\ \text{V}$ reading has $0.1\%$, a factor of ten difference.
The $9999\ \text{V}$ reading is therefore the stronger one.

$$\boxed{|e| = 1\ \text{V}\ \text{for both, but}\ E_{\text{rel}} = 10^{-3}\ \text{against}\ 10^{-4}}$$

> [!warning] This is the clearest demonstration of why relative error exists
> Both readings miss by exactly $1$ volt. Read as absolute errors they are
> **identical**, and a specification written as "accurate to $1$ volt" cannot
> distinguish them.
>
> Read as relative errors, one is ten times better than the other, and the
> specification "accurate to $0.01\%$" selects exactly one of the two
> instruments.
>
> **A voltmeter's accuracy is always specified as a percentage of full scale, never
> in volts.** That is not a convention; it is forced by exactly this observation.
> An instrument accurate to $1$ volt is useless on a $1$ kilovolt range and
> excellent on a $100$ kilovolt one.

> [!info] Check against the exact ratios
> The ratio of the two relative errors equals the inverse ratio of the true
> values: $\dfrac{10^{-3}}{10^{-4}} = 10 = \dfrac{10000}{1000}$. A common absolute
> error on magnitudes differing by a factor of ten produces relative errors
> differing by the same factor, which is the point the comment rests on.

---

### [2020 Q.1(b)]

**Question.** How are errors represented? Write down their expressions. Obtain their values to approximate a current as $9.05$ Amp instead of its true value $10$ Amp. Justify, which representation is better.

*[Marks: 06]*

**Solution.**

**Definitions.** Let $v_t$ be the true value and $v_a$ the approximate value.

**Absolute error.** The size of the mistake, in the units of the quantity.

$$
E_a = v_a - v_t \qquad \text{or} \qquad |E_a| = |v_a - v_t|
$$

It is the only error directly measurable, and it carries the same units as the
answer.

**Relative error.** The mistake as a fraction of the true value. It is
dimensionless, so it can be compared across quantities of different size.

$$
E_r = \frac{v_a - v_t}{v_t} \qquad \text{percentage relative error} = \frac{v_a - v_t}{v_t} \times 100
$$

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

$$\boxed{|E_a| = 0.95 \text{ Amp}, \qquad E_r = -0.095, \qquad \text{percentage} = -9.5\%}$$

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
> **Fix the true value in memory: relative error is always taken over the true
> value.** The same distinction appears in 2024 Q.1(b) and 2023 Q.1(b).

---

---

**Also asked here.**

- *CT-02B Q.1(c)* is the same question as [[NM-3.5_Gauss_Seidel_Iteration|NM-3.5]], which is written in `NM-3.5`.

---

<a id="nm-16"></a><a id="nm-1.6"></a>
## NM-1.6 · Taylor Series & Truncation Error

### [2017 Q.1(c)]

**Question.** Evaluate $e^{-5}$ using following two approaches and compare with the true value of $6.737947 \cdot 10^{-3}$ as terms are added: $e^{-x} = 1 - x + \frac{x^2}{2!} - \frac{x^3}{3!} + \cdots \quad \text{and} \quad e^{-x} = \frac{1}{e^x} = \frac{1}{1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \cdots}$.

*[Marks: 04]*

**Solution.**

**This question is about catastrophic cancellation, and the two approaches are
mathematically identical.** Both compute $e^{-5}$. They differ only in
arithmetic, and at $x = 5$ that difference is fatal.

**Approach A: the alternating series directly, with $x = 5$.**

$$S_k = \sum_{n=0}^{k-1}\frac{(-5)^n}{n!}$$

| Terms $k$ | $S_k$ | Error $\lvert S_k - 6.737947\times10^{-3}\rvert$ |
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

**What is happening.** The partial sums grow to $13.7$ before they begin to
fall. The largest term is $\dfrac{5^5}{5!} = 26.0417$, and the answer is
$0.0067379$, so that one term is about $3866$ times the result.

**Why that destroys the computation.** Each partial sum is formed by adding
alternating terms of size up to $26$ to get a number of size $0.0067$. To hold
a final answer of size $10^{-3}$ to, say, four significant figures, the machine
must retain four digits past the point where cancellation has eaten the
leading digits. If the partial sums are carried to $d$ significant figures and
the largest term is $3866$ times the answer, then all but about
$\log_{10}(3866) \approx 3.6$ of those digits are consumed by cancellation.
The remaining answer is good to roughly $d - 4$ digits, and no amount of
further addition repairs it: each new term is again of size comparable to the
running total. This is **catastrophic cancellation**, and the defining feature
is that the error is *not* reduced by computing more terms.

**Approach B: the reciprocal of the positive series, with $x = 5$.**

$$T_k = \sum_{n=0}^{k-1}\frac{5^n}{n!}, \qquad e^{-5} \approx \frac{1}{T_k}$$

| Terms $k$ | $T_k$ | $\dfrac{1}{T_k}$ | Error |
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

**What is happening.** Every term is positive, so there is **no cancellation at
all**. The sum rises monotonically towards $e^5 = 148.4132$, and its magnitude
never differs wildly from itself, so the machine's digits all survive. The
reciprocal then approaches the true value from above.

$$\boxed{\text{Approach A is unusable at } x = 5; \text{ Approach B reaches } 6.7395\times10^{-3} \text{ in 15 terms}}$$

**The comparison.**

| | Approach A | Approach B |
| :-- | :-- | :-- |
| Sign pattern | alternating | all positive |
| Largest term | $26.0417$ at $n = 5$ | $26.0417$ at $n = 5$ |
| That term relative to the result | $\approx 3866 \times$ | $\approx 3866 \times$ |
| Cancellation | catastrophic | none |
| Behaviour | diverges then converges, pathologically | monotone |
| Terms for 4 significant figures | 23 | 16 |

Note the fourth row of the table. Both approaches have the *same* largest term
relative to the answer. That is exactly why the problem is interesting: the
data are identical and the only thing that differs is the arrangement of the
summation, and that arrangement alone decides whether the machine survives.

> [!info] What the two routes confirm
> The true value is $e^{-5} = 1/e^5 = 1/148.4132 = 6.737947\times10^{-3}$, the
> figure printed in the question, so Approach B's reciprocal *is* the direct
> route and Approach A must in principle reach the same place. It does, eventually:
> at the twenty-third term the alternating series gets within $3.8\times10^{-7}$,
> which is four significant figures. So Approach A is not *wrong*, it is
> unusable in practice, and the difference between "wrong" and "unusable" is
> worth holding on to.
>
> The practical rule follows: for $x \gtrsim 1$, evaluate $e^{-x}$ as $1/e^x$,
> never as the alternating series, because the cancellation factor is roughly
> $e^x/x!$ and grows without bound as $x$ grows. The same trap appears in
> $\cos x = 1 - x^2/2 + x^4/24 - \cdots$ for large $x$, and in any alternating
> series whose terms peak far above the answer.

> [!warning] The test that catches a fabricated partial-sum column
> Two identities must hold in any such table, and both are one line. The
> *printed sum* must satisfy $1/T_k = $ the *printed reciprocal*, and
> $T_k - T_{k-1} = 5^{k-1}/k!$ must hold between consecutive rows. An earlier
> draft of the answer script carried a column of partial sums that satisfied
> neither, while its reciprocal and error columns were correct for the true
> sums. A table can therefore look entirely reasonable and still be wrong, and
> the only defence is to check one row against the sum rule above.

---

### [2018 Q.1(c)]

**Question.** Find the number of terms in the exponential series such that their sum gives the value of $e^x$ correct to five decimal places for all values of $x$ in the range $0 \le x \le 1$.

*[Marks: 04]*

**Solution.**

**The phrase that decides the answer is "for all values of $x$".** You are not
being asked for a term count that works at one particular $x$. You are being
asked for one that works *everywhere* on $[0, 1]$. So the first job is to find
the worst point on that interval and work there.

**The series and its remainder.**

$$e^x = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \cdots + \frac{x^n}{n!} + \cdots$$

After $k$ terms the remainder is, by Taylor's theorem in Lagrange form,

$$R_k = \frac{e^{\xi}x^k}{k!}, \qquad 0 < \xi < x$$

Now bound each factor. On $[0,1]$ we have $x^k \le 1$, and since $\xi < x \le 1$
we have $e^{\xi} \le e$. So

$$|R_k| \le \frac{e}{k!} = \frac{2.718282}{k!}$$

**Where is the worst case?** The bound $\dfrac{e}{k!}$ is attained at $x = 1$,
and at $x=1$ the error really is its largest, since every term $x^n$ grows with
$x$ on $[0,1]$. So $x = 1$ is the point to test and no other point can be worse.

**"Correct to five decimal places" means an error below $0.5 \times 10^{-5}$.**
Not below $10^{-5}$. Getting this factor of two wrong doubles your term count
and is the single most common error in this question.

**Test $k$.**

| $k$ | Tail bound $\dfrac{1}{k!}\dfrac{k+1}{k}$ | Verdict |
| :--: | :-- | :-- |
| 8 | $\dfrac{1}{40320}\left(\dfrac{9}{8}\right) = 2.786 \times 10^{-5}$ | too large |
| 9 | $\dfrac{1}{362880}\left(\dfrac{10}{9}\right) = 3.062 \times 10^{-6}$ | below $5\times10^{-6}$ |

Hence the remainder tail is bounded by
$R_9 \le 3.062 \times 10^{-6} < 0.5 \times 10^{-5}$, which certifies nine terms.

**Direct check at the worst point.** Summing the first nine terms,

$$S_9 = 2 + 0.5 + 0.166667 + 0.041667 + 0.008333 + 0.001389 + 0.000198 + 0.0000248 = 2.71827877$$

against $e = 2.71828183$, so the actual error is $3.06 \times 10^{-6}$, about
half the bound. With eight terms $S_8 = 2.71825397$ and $|e - S_8| =
2.79 \times 10^{-5}$, far too large.

$$\boxed{9\ \text{terms}}$$

> [!info] Why the geometric tail resolves the bound
> The error after nine terms is the tail $R_9 = \sum_{n=9}^{\infty}\dfrac{1}{n!}$.
> Since $\dfrac{1}{9!} = 2.7557\times10^{-6}$ and the tail is bounded by
> $\dfrac{1}{9!}\left(1 + \dfrac{1}{10} + \dfrac{1}{10\cdot11} + \cdots\right) < \dfrac{10}{9\cdot9!} = 3.062\times10^{-6}$,
> the true error $3.06\times10^{-6}$ sits well below the tolerance $5\times10^{-6}$.
> Note that the cruder Lagrange bound $\dfrac{e}{k!}$ gives $\dfrac{e}{9!} = 7.491\times10^{-6}$,
> which exceeds $5\times10^{-6}$ only because $e \approx 2.718$ is a conservative bound for $e^\xi$ on $[0,1]$;
> the exact geometric tail certifies that nine terms clear the tolerance while eight do not.

---

### [2021 Q.1(c)]

**Question.** Compute the value of $\ln 3$ correct to five decimal places using Taylor's series expansion.

*[Marks: 04, CO: 2]*

**Solution.**

**Step 1. Choose a series that converges.** The familiar expansion

$$
\ln(1+x) = x - \frac{x^2}{2} + \frac{x^3}{3} - \cdots
$$

converges only for $\lvert x \rvert < 1$. Here $3 = 1 + 2$, so $x = 2$ and **the
series diverges**.

> [!warning] The arithmetic does not fail, the series does
> Substituting $x = 2$ and adding terms gives a number that drifts away from
> $\ln 3$ forever, and the partial sums *increase* past it. Nothing in the
> computation looks wrong: each term is a finite number and the running total
> updates cleanly. Only the convergence test catches it.
>
> **Check the radius before you start, not after.** The habit is one line:
> $x = 2$, and $|2| > 1$, so pick a different form. Finding this after twenty
> minutes of summation is the whole lesson of the question.

**Step 2. Use the hyperbolic form instead.** Write

$$
\ln\frac{1+y}{1-y} = 2\left(y + \frac{y^3}{3} + \frac{y^5}{5} + \cdots\right),
\qquad \lvert y\rvert < 1
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

Seven terms give an error of $5.23 \times 10^{-6}$, still above
$\frac{1}{2}10^{-5}$. Eight terms give $1.16 \times 10^{-6}$, comfortably inside, so
**eight terms are required**.

**Step 5. Round.**

$$\boxed{\ln 3 = 1.09861}$$

> [!info] Check by an independent route
> Split $\ln 3 = \ln 2 + \ln 1.5$ and use $y = \frac{1}{3}$ and $y = \frac{1}{5}$
> respectively. With twelve terms each, $\ln 2 = 0.6931471805$ and
> $\ln 1.5 = 0.4054651081$, and the sum is $1.0986122887$, whose first five
> decimals are **1.09861**. The same answer from a different decomposition.
>
> The closed-form check is that $\ln 3 = 1.0986122886681098$, and
> $\lvert 1.0986111314 - 1.0986122887 \rvert = 1.16 \times 10^{-6}$, matching the
> table.

> [!warning] Two ways to repair a divergent log series
> 1. **Use the hyperbolic form** above with $y = \frac{a-1}{a+1}$, which is always inside the radius once $a > 1$. This is the clean route and it is what the answer uses.
> 2. **Split the argument** so each piece has $\lvert x\rvert < 1$, as $\ln 3 = \ln 2 + \ln 1.5$. More work, but it works with the familiar series.
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
> Two different numbers appear for seven terms, and both are correct: the
> **bound** $5.425 \times 10^{-6}$ comes from the geometric estimate above, while
> the **actual** error is $1.0986122887 - 1.0986070624 = 5.226 \times 10^{-6}$,
> which the table lists. The true error is always the smaller of the two, because
> the bound replaces each remaining denominator $2k+1$ by the larger value $2N+1$.
> Both exceed $5 \times 10^{-6}$, so seven terms fail on either count and eight
> terms pass on both.

---

### [2022 Q.1(b)]

**Question.** Evaluate $f(1)$ using Taylor's series for $f(x)$, where $f(x) = x^3 - 3x^2 + 5x - 10$.

*[Marks: 04, CO: 1]*

**Solution.**

**Step 1. Write the series about $x = 0$.**

$$
f(x) = f(0) + x f'(0) + \frac{x^2}{2!}f''(0) + \frac{x^3}{3!}f'''(0) + \frac{x^4}{4!}f^{(4)}(0) + \cdots
$$

**Step 2. Differentiate and evaluate at zero.** All four rows are needed, because
a cubic is exactly the case where the fourth derivative decides whether the
series terminates.

| | $f(x)$ | $f'(x)$ | $f''(x)$ | $f'''(x)$ | $f^{(4)}(x)$ |
| :-- | :-- | :-- | :-- | :-- | :-- |
| | $x^3-3x^2+5x-10$ | $3x^2-6x+5$ | $6x-6$ | $6$ | $0$ |

$$
f(0) = -10, \qquad f'(0) = 5, \qquad f''(0) = -6, \qquad f'''(0) = 6, \qquad f^{(4)} = 0
$$

**Step 3. The series terminates.** The fourth derivative is identically zero, so
there is nothing after the cubic term:

$$
f(x) = -10 + 5x + \frac{-6}{2}x^2 + \frac{6}{6}x^3 = -10 + 5x - 3x^2 + x^3
$$

**Step 4. Put $x = 1$.**

$$
f(1) = -10 + 5(1) - 3(1)^2 + (1)^3 = -10 + 5 - 3 + 1
$$

$$\boxed{f(1) = -7}$$

> [!info] Three independent routes, all landing on $-7$
> **Direct substitution.** $1 - 3 + 5 - 10 = -7$.
>
> **Horner, with no powers written out.** $(-10 + 5 \cdot 1) \cdot 1 - 3 = -8$, then
> $-8 \cdot 1 + 1 = -7$.
>
> **The truncation error is exactly zero.** Because $f^{(4)} \equiv 0$, the
> remainder $R_3$ is identically zero, not merely small. There is no error term
> to bound here, which is the distinguishing feature of a cubic.

> [!note] Why this question has no error analysis
> Taylor's method earns its keep when the series is infinite. For a polynomial of
> degree $k$, the $k$-th order expansion is the polynomial itself, and the
> $(k+1)$-th derivative being zero is what makes the answer exact rather than
> approximate.
>
> So no remainder term is needed here, and writing one anyway would be padding.
> The four marks are for the derivative table: $f'$, $f''$, $f'''$ written out
> explicitly, then the substitution. That is the whole question.

---

### [2024 Q.1(b)]

**Question.** Given the function $f(x) = e^x$, derive the third order Taylor series expansion around $x = 0$. Estimate the truncation error if you use this expansion to approximate $f(0.5)$.

*[Marks: 03, CO: 1]*

**Solution.**

**The setup.** The Taylor series of $f$ about $x_0$ is

$$f(x) = \sum_{n=0}^{\infty}\frac{f^{(n)}(x_0)}{n!}(x - x_0)^n$$

For $f(x) = e^x$ about $x_0 = 0$, every derivative is $e^x$, and evaluated at
zero every derivative is $1$. This is why $e^x$ is the standard worked example:
the derivative never changes, so the series is simply

$$e^x = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \frac{x^4}{4!} + \cdots$$

**Third order means keeping terms up to $n = 3$.**

$$\boxed{e^x \approx P_3(x) = 1 + x + \frac{x^2}{2} + \frac{x^3}{6}}$$

At $x = 0.5$:

$$P_3(0.5) = 1 + 0.5 + \frac{0.25}{2} + \frac{0.125}{6} = 1 + 0.5 + 0.125 + 0.0208333 = 1.6458333$$

**The truncation error.** Taylor's theorem gives the exact remainder

$$R_n = \frac{f^{(n+1)}(\xi)}{(n+1)!}(x - x_0)^{n+1}$$

for some $\xi$ between $x_0$ and $x$. Here $n = 3$, so

$$R_3 = \frac{e^{\xi}}{4!}(0.5)^4 = \frac{e^{\xi}}{24}(0.0625) = e^{\xi} \times 0.0026042$$

To **bound** this, take the largest $e^\xi$ can be on the interval, which is at
$\xi = 0.5$:

$$|R_3| \le \frac{e^{0.5}}{24}(0.5)^4 = \frac{1.6487213}{24}(0.0625) = 0.0042935$$

$$\boxed{P_3(0.5) = 1.6458333, \qquad |E_3| = 0.0028879 \le 0.0042935}$$

**Why the bound and the actual differ.** The bound $0.0042935$ uses $e^\xi$ at
its worst, $\xi = 0.5$. The *actual* error is

$$|e^{0.5} - P_3(0.5)| = 1.6487213 - 1.6458333 = 0.0028879$$

which is about two thirds of the bound. The first neglected term alone is

$$\frac{(0.5)^4}{4!} = \frac{0.0625}{24} = 0.0026042$$

which is already $90\%$ of the actual error. This is the useful practical fact
about alternating-free Taylor series: **the first neglected term tells you the
size of the error**. For $e^x$ with positive $x$ the terms are all positive, so
the first neglected term is a lower bound on the error rather than an estimate
of it, and the ratio of consecutive terms tells you how many more terms you
would need.

> [!warning] The trap: which $x$ goes in the remainder
> The remainder carries $(x - x_0)^{n+1}$, evaluated at the point where you are
> approximating, that is $x = 0.5$, not at the expansion point. Writing
> $(0.5 - 0)^4$ and writing $(0.5)^4$ are the same thing, but writing
> $(0.5 - x_0)$ where $x_0 = 0$ and then forgetting the minus is the classic
> slip. Equally common is bounding $e^\xi$ by $e^0 = 1$, which is the *smallest*
> value on the interval, not the largest.

---

[🏠 Master Index](00_Index.md) | [Next Topic: NM-2 · Roots of Equations →](NM-2_Roots_of_Equations.md)
