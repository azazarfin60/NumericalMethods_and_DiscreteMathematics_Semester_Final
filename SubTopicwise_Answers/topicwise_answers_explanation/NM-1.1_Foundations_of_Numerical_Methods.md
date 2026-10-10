---
title: "NM-1.1 · Foundations of Numerical Methods"
tags:
  - numerical-methods
  - discrete-mathematics
  - topicwise
---





[🏠 Subtopic Index](00_Index.md) | [Next: NM-1.2 Mathematical Modeling & Engineering Problem Solving →](NM-1.2_Mathematical_Modeling_and_Engineering_Problem_Solving.md)

---

# NM-1.1 · Foundations of Numerical Methods

Every block below is copied from `../answers_explanation/`. The reasoning
is written once, in the year-wise file, and is not restated here.


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

[🏠 Subtopic Index](00_Index.md) | [Next: NM-1.2 Mathematical Modeling & Engineering Problem Solving →](NM-1.2_Mathematical_Modeling_and_Engineering_Problem_Solving.md)
