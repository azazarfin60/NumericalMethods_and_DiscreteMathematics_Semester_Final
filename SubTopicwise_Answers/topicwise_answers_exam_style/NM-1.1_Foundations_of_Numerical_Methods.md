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

Every block below is copied from `../answers_exam_style/`, which is the
only place an answer is authored. A number here is the same number, character
for character, as the one it came from.


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

[🏠 Subtopic Index](00_Index.md) | [Next: NM-1.2 Mathematical Modeling & Engineering Problem Solving →](NM-1.2_Mathematical_Modeling_and_Engineering_Problem_Solving.md)
