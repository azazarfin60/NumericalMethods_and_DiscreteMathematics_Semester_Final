---
course_code: ECE 2213
course_title: Numerical Methods & Discrete Mathematics
document_type: Topic-wise Sorted Question Bank
years_covered: 2017-2024 + Class Tests
taxonomy: topic_subtopic_list.md
tags:
  - question-bank
  - ece2213
  - topic-wise
  - numerical-methods
  - discrete-mathematics
---

# ECE 2213 — Topic-wise Sorted Question Bank (2017–2024 + Class Tests)

**Institution:** Rajshahi University of Engineering & Technology (RUET)
**Department:** Electrical & Computer Engineering

Every sub-question from the eight semester-final papers (2017–2024) and the four class tests, sorted into the subtopic taxonomy defined in [`topic_subtopic_list.md`](topic_subtopic_list.md).

---

## How to Read This File

**Entry format**

```
- **[Year Q.No — Marks]** Question text  — 🔁 **Repeat marker**  *(also → cross-reference)*
```

**Conventions**

| Element | Meaning |
| :--- | :--- |
| `### Theory` | Definitions, derivations, comparisons, discussions |
| `### Computation` | Numeric problems, truth tables, proofs, iterative marches |
| 🔁 | Verbatim or near-verbatim repeat — the marker names the other year(s) |
| `*(also → NM-x.y)*` | The sub-question also belongs to another subtopic, which is where it is *filed* |
| `— —` | Class test part with no individual mark printed |
| **Appearances: None** | Syllabus subtopic that has never been examined |

> **Reading the "Appearances" line.** It counts **every source that touched the subtopic** — including
> cross-referenced and secondary appearances, not only the questions listed in that block. It therefore
> matches the "Years Appeared" column of `topic_subtopic_list.md`, from which it is derived. `NM-2.2`
> (Bisection) is the worked example: 2020 Q.2(a) names bisection inside a four-way comparison, so that
> question is *filed* under `NM-2.6` (Method Comparison) and is not duplicated under `NM-2.2` — yet 2020
> still counts as an appearance of bisection. If you want only the questions printed under a subtopic,
> count the entry lines.

**Mark scales differ by era — read marks in context:**

| Era | Years | Full marks | Per question | Section content |
| :--- | :--- | :---: | :---: | :--- |
| **Pre-OBE** | 2017 – 2021 | 72 | 12 | Numerical Methods in **both** Section A and Section B |
| **OBE** | 2022 – 2024 | 60 | 10 | Section A = Numerical Methods, Section B = Discrete Mathematics |

> **Why there are no Discrete Mathematics questions before 2022:** the course was titled simply *"Numerical Methods"* until the 2022 OBE curriculum revision, which added the Discrete Mathematics half. The 2017–2021 papers contain **zero** discrete mathematics — both of their sections are numerical. All `DM-*` entries therefore come from 2022, 2023, 2024 and CT-04 only.

**Class test labels:** `CT-01` (errors & root-finding comparison), `CT-02A` (interpolation), `CT-02B` (Gauss-Seidel & Runge-Kutta), `CT-04` (propositional logic).

**Deliberate double-filing.** A few questions are listed under two subtopics on purpose, because they test two separately-marked skills:
- Circuit → Gauss-Seidel questions appear under both **NM-3.5** (the iteration) and **NM-3.8** (formulating the circuit equations).
- Applied integration questions appear under both their rule (**NM-5.1/5.2/5.3**) and **NM-5.7**; those chaining *value → true error → absolute relative true error* also appear under **NM-5.6**.
- Laplace/Poisson grid questions appear under the equation type (**NM-10.2/10.3**) and under **NM-10.4** when the question names Liebmann's method.

---

## Contents

### Section 1 — Numerical Methods
| Topic | Subtopics |
| :--- | :--- |
| [NM-1 · Modeling, Computers and Error Analysis](#nm-1--modeling-computers-and-error-analysis) | NM-1.1 – NM-1.7 |
| [NM-2 · Roots of Equations](#nm-2--roots-of-equations) | NM-2.1 – NM-2.7 |
| [NM-3 · Linear Algebraic Equations](#nm-3--linear-algebraic-equations) | NM-3.1 – NM-3.8 |
| [NM-4 · Curve Fitting](#nm-4--curve-fitting) | NM-4.1 – NM-4.12 |
| [NM-5 · Numerical Integration](#nm-5--numerical-integration) | NM-5.1 – NM-5.7 |
| [NM-6 · Optimization](#nm-6--optimization) | NM-6.1 – NM-6.3 |
| [NM-7 · Numerical Differentiation](#nm-7--numerical-differentiation) | NM-7.1 – NM-7.4 |
| [NM-8 · Ordinary Differential Equations](#nm-8--ordinary-differential-equations) | NM-8.1 – NM-8.8 |
| [NM-9 · Eigenvalue Problems](#nm-9--eigenvalue-problems) | NM-9.1 |
| [NM-10 · Partial Differential Equations](#nm-10--partial-differential-equations) | NM-10.1 – NM-10.5 |

### Section 2 — Discrete Mathematics *(2022 onward only)*
| Topic | Subtopics |
| :--- | :--- |
| [DM-1 · Set Theory](#dm-1--set-theory) | DM-1.1 – DM-1.4 |
| [DM-2 · Relations](#dm-2--relations) | DM-2.1 – DM-2.4 |
| [DM-3 · Propositional Logic](#dm-3--propositional-logic) | DM-3.1 – DM-3.13 |
| [DM-4 · Proof Techniques](#dm-4--proof-techniques) | DM-4.1 – DM-4.5 |
| [DM-5 · Number Theory](#dm-5--number-theory) | DM-5.1 – DM-5.9 |
| [DM-6 · Introduction to Counting](#dm-6--introduction-to-counting) | DM-6.1 – DM-6.6 |
| [DM-7 · Supplementary Topics](#dm-7--supplementary-topics) | DM-7.1 – DM-7.2 |

---

<br>

# ═══ SECTION 1 — NUMERICAL METHODS ═══

*Source papers: 2017, 2018, 2019, 2020, 2021 (both sections) · 2022, 2023, 2024 (Section A) · CT-01, CT-02A, CT-02B*

<br>

# NM-1 · Modeling, Computers and Error Analysis

## NM-1.1 · Foundations of Numerical Methods

**Appearances:** 2017, 2018, 2019, 2020, 2021, 2023, 2024 · **7 papers**

### Theory
- **[2017 Q.1(a) — 04]** Define Numerical Methods? Why do we need to use numerical methods to solve engineering problems?
- **[2017 Q.8(c) — 02]** Write down some real life fields where there is a great importance of numerical methods.
- **[2018 Q.1(a) — 04]** What are the importances of numerical techniques in engineering? Briefly discuss.
- **[2019 Q.1(a) — 04]** Define numerical method. How does it become popular? Why do ECE engineers require numerical methods?
- **[2021 Q.1(a) — 04]** Differentiate between numerical methods and analytical methods. Why do ECE engineers require numerical methods?
- **[2023 Q.1(a) — 04]** Explain the differences between analytical and numerical solution also describe the significance of numerical analysis in engineering field.

---

## NM-1.2 · Mathematical Modeling & Engineering Problem Solving

**Appearances:** 2024, CT-01 · **2 papers**

### Theory
- **[2024 Q.1(a) — 03]** Explain the importance of mathematical modeling in engineering problem solving; provide examples of how a real-world engineering problem can be represented using mathematical models.
- **[CT-01 Q.1(a) — 10]** (Scenario: embedded reactor-temperature estimation software storing only 5 significant decimal digits and using the first four non-zero Taylor terms for the exponential; predictions differ from experiment.) Develop a mathematical model representing the temperature estimation problem and identify the assumptions made. *(Note: labelled (vii) in original script.)*

---

## NM-1.3 · Accuracy, Precision & Significant Digits

**Appearances:** 2017 · **1 paper**

### Theory
- **[2017 Q.1(b) — 04]** Define the following terms with example: (i) Accuracy (ii) Precision (iii) truncation error (iv) round off error *(also → NM-1.4)*

### Computation
- **[2017 Q.3(a) — 03]** Sum all the numbers of provided list: $0.1532, 15.45, 0.000354, 305.4, 8.12, 143.3$ where in each of which all the given digits are correct.

---

## NM-1.4 · Error Types & Sources

**Appearances:** 2017, 2018, 2019, 2020, 2024, CT-01 · **5 papers + CT-01**

### Theory
- **[2018 Q.1(b) — 04]** What are the algorithmic errors that may occur in numerical calculation?
- **[2019 Q.1(b) — 04]** What are the errors involved in numerical methods? How do they enter into the process? Give example.
- **[2020 Q.1(a) — 06]** Why are numerical methods for? What are the sources of errors in numerical methods? Discuss them. *(also → NM-1.1)*
- **[2024 Q.1(c) — 04]** What are round off and truncation errors? Discuss how each arises in numerical computation.
- **[CT-01 Q.1(b) — 10]** (Same reactor-software scenario as CT-01 Q.1(a): 5 significant digits, four-term Taylor exponential.) Identify at least three possible sources of numerical error in the software and explain how each affects the final prediction. *(Note: labelled (viii) in original script.)*

---

## NM-1.5 · Error Representations & Propagation

**Appearances:** 2017, 2019, 2020, 2023 · **4 papers**

### Computation
- **[2017 Q.3(b) — 03]** Given that $u = \frac{5xy^2}{z^3}$. Find the relative error at $x = y = z = 1$ when the errors in each of $x, y, z$ is $0.001$. 🔁 **Repeated in 2023 Q.1(b)**
- **[2019 Q.1(c) — 04]** What are the error representations? Two PT-voltmeter arrangements give $999\text{V}$ and $9999\text{V}$ instead of $1\text{kV}$ and $10\text{kV}$. Obtain error by all possible error representations. Hence comment on error strength of the readings.
- **[2020 Q.1(b) — 06]** How are errors represented? Write down their expressions. Obtain their values to approximate a current as $9.05\text{ Amp}$ instead of its true value $10\text{ Amp}$. Justify, which representation is better.
- **[2023 Q.1(b) — 03]** Given that, $u = \frac{5xy^2}{z^3}$, find the relative error at $x = y = z = 1$ when the errors in each of $x, y, z$ is $0.001$. 🔁 **Repeat of 2017 Q.3(b)**

---

## NM-1.6 · Taylor Series & Truncation Error

**Appearances:** 2017, 2018, 2021, 2022, 2024, CT-01 · **5 papers + CT-01**

### Computation
- **[2017 Q.1(c) — 04]** Evaluate $e^{-5}$ using following two approaches and compare with the true value of $6.737947 \cdot 10^{-3}$ as terms are added: $e^{-x} = 1 - x + \frac{x^2}{2!} - \frac{x^3}{3!} + \cdots$ and $e^{-x} = \frac{1}{e^x} = \frac{1}{1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \cdots}$ *(also → NM-1.4)*
- **[2018 Q.1(c) — 04]** Find the number of terms in the exponential series such that their sum gives the value of $e^x$ correct to five decimal places for all values of $x$ in the range $0 \le x \le 1$.
- **[2021 Q.1(c) — 04]** Compute the value of $\ln 3$ correct to five decimal places using Taylor's series expansion.
- **[2022 Q.1(b) — 04]** Evaluate $f(1)$ using Taylor's Series for $f(x)$, where $f(x) = x^3 - 3x^2 + 5x - 10$.
- **[2024 Q.1(b) — 03]** Given the function $f(x) = e^x$, derive the third order Taylor series expansion around $x = 0$. Estimate the truncation error if you use this expansion to approximate $f(0.5)$. *(Note: "his expansion" printed in original.)*

---

## NM-1.7 · Programming and Software

**Appearances:** None — not examined in any paper 2017–2024.

---

# NM-2 · Roots of Equations

## NM-2.1 · Fundamentals & Classification

**Appearances:** 2019, 2020, 2021, 2022 · **4 papers**

### Theory
- **[2019 Q.2(a) — 04]** What is meant by iterative method? Write the names of iterative methods to solve nonlinear equations. Write the generalized steps to solve the nonlinear equations using iterative methods.
- **[2021 Q.2(a) — 02]** Define bracketing methods with example.
- **[2022 Q.1(a) — 02]** What is the difference between open and bracketing method of root finding?

---

## NM-2.2 · Bisection Method

**Appearances:** 2017, 2018, 2020, 2024, CT-01 · **4 papers + CT-01**

### Theory
- **[2017 Q.3(c) — 06]** Explain the bisection method for finding a real root of the equation $f(x) = 0$ and write an algorithm for its implementation with a test for relative accuracy.
- **[2018 Q.2(a) — 04]** Develop an algorithm to calculate the root of any non-linear equation by bisection method.

### Computation
- **[2024 Q.2(a) — 03]** Given the polynomial $f(x) = x^3 - 6x^2 + 11x - 6$, use the bisection (bracketing) method to find a root in the interval up to two iterations. *(Note: no explicit initial interval $[a,b]$ printed; roots are $x = 1, 2, 3$, so a sign-change interval such as $[0.5, 1.5]$ or $[2.5, 3.5]$ is chosen.)* *(also → NM-2.7)*

---

## NM-2.3 · False Position / Regula Falsi

**Appearances:** 2017, 2018, 2020, 2021, CT-01 · **4 papers + CT-01**

### Theory
- **[2017 Q.2(b) — 04]** Write down the algorithm steps while finding the root of a nonlinear equation using false position method.
- **[2018 Q.2(b) — 04]** Derive the expression of the next approximation of a root of the non-linear function $f(x) = 0$ using regula-falsi method.
- **[CT-01 Q.2(b) — 10]** (Chemical-plant scenario: find operating temperature where reaction pressure is zero, $f(T) = 0$.) During testing, the Regula Falsi Method repeatedly updates only one endpoint of the interval, leading to slow convergence. Explain why this happens, compare it with the Bisection Method, and suggest a suitable improvement. *(Note: labelled (h) in original script.)* *(also → NM-2.6)*

### Computation
- **[2021 Q.2(b) — 04]** Given that the equation $x^{2.2} = 69$ has a root between 5 and 8. Use the method of regula-falsi to determine it.

---

## NM-2.4 · Newton-Raphson Method

**Appearances:** 2017, 2018, 2019, 2020, 2021, 2023 · **6 papers**

### Theory
- **[2017 Q.2(a) — 04]** Briefly discuss the limitations of N-R method to find the root of any non-linear equation. How can we solve it?
- **[2019 Q.2(c) — 04]** Write the steps of N-R method. Discuss its merits and demerits.
- **[2021 Q.1(b) — 04]** Derive the formula for root finding using Newton-Raphson method. Also, discuss the problems of it and how this problem can be solved. 🔁 **Repeated in 2023 Q.1(c)**
- **[2023 Q.1(c) — 03]** Derive the formula for root findings using Newton-Raphson method. Also, discuss this problems of it and how this problem can be solved. 🔁 **Repeat of 2021 Q.1(b)**

### Computation
- **[2018 Q.2(c) — 04]** Find the real root of the equation $x \sin x + \cos x = 0$ using N-R method.
- **[2020 Q.2(b) — 06]** An electrical power equation is given as follows: $3I^2 - 4I - 4 = 0$. Calculate 3 iterations of the Newton-Raphson method to obtain the value of current. *(also → NM-2.7)*

---

## NM-2.5 · Secant Method

**Appearances:** 2017, 2020 · **2 papers**

### Computation
- **[2017 Q.2(c) — 04]** Find the positive root of the equation $f(x) = x^3 - 3x^2 - x - 3 = 0$ by secant method (Use four iterations only). *(Note: constant term faint in original scan; read as $-3$ or $-1$.)*

---

## NM-2.6 · Method Comparison & Convergence

**Appearances:** 2020, 2022, CT-01 · **2 papers + CT-01**

### Theory
- **[2020 Q.2(a) — 06]** Define roots of an equation. List the comparisons among bisection, secant, false position and Newton-Raphson methods. *(also → NM-2.1)*
- **[CT-01 Q.2(a) — 10]** (Chemical-plant scenario: computerized system finds operating temperature where reaction pressure becomes zero, modeled by a continuous nonlinear $f(T) = 0$.) Compare the Bisection Method and Regula Falsi Method in terms of the required condition for application, convergence behavior, and suitability for a safety-critical system. *(Note: labelled (g) in original script.)*

---

## NM-2.7 · Roots of Polynomials

**Appearances:** 2017, 2019, 2020, 2021, 2024 · **5 papers**

### Computation
- **[2019 Q.2(b) — 04]** Compute current, $I$ from the following power balance equation obtained from an electric circuit by using an iterative method: $5I^2 + 50I = 1000$ *(also → NM-2.1)*
- **[2021 Q.2(c) — 06]** Determine the smallest root of the equation: $f(x) = x^3 - 9x^2 + 26x - 24 = 0$

---

# NM-3 · Linear Algebraic Equations

## NM-3.1 · Direct Methods & Gauss Elimination

**Appearances:** 2019, 2020, 2022 · **3 papers**

### Theory
- **[2019 Q.3(a) — 04]** Discuss Gauss Elimination method to solve linear simultaneous algebraic equations.
- **[2020 Q.4(a) — 06]** What are the direct methods to solve linear system of equations? Describe any one of them.

### Computation
- **[2022 Q.4(b) — 04]** Solve the system using Gauss elimination: $2x_1 + x_2 - x_3 = -1$, $x_1 - 2x_2 + 3x_3 = 9$, $3x_1 - x_2 + 5x_3 = 14$. Check your answer by substituting into the original equations.

---

## NM-3.2 · Pivoting

**Appearances:** 2017, 2019, 2021, 2022 · **4 papers**

### Theory
- **[2017 Q.4(a) — 03]** What are pivots in solving system of linear equations using elimination methods? What are (i) partial & (ii) complete pivoting? 🔁 **Repeated in 2019 Q.3(b), 2021 Q.7(a), 2022 Q.3(c)**
- **[2019 Q.3(b) — 04]** Discuss partial and complete pivoting in brief. 🔁 **Repeat of 2017 Q.4(a)**
- **[2021 Q.7(a) — 02]** Why is pivoting important? 🔁 **Repeat of 2017 Q.4(a)**
- **[2022 Q.3(c) — 02]** What is pivoting? 🔁 **Repeat of 2017 Q.4(a)**

---

## NM-3.3 · LU Decomposition & Matrix Inversion

**Appearances:** 2017 · **1 paper**

### Theory
- **[2017 Q.4(b) — 04]** How can a square matrix be factorized into the form LU to solve linear system of equations?

---

## NM-3.4 · Jacobi Iteration

**Appearances:** 2017, 2022 · **2 papers**

### Computation
- **[2017 Q.7(a) — 06]** Solve the following system using Jacobi method: $6x + y + z = 20$, $x + 4y - z = 6$, $x - y + 5z = 7$. 🔁 **Repeated in 2022 Q.4(a)**
- **[2022 Q.4(a) — 04]** Solve the system using Jacobi method: $6x + y + z = 20$, $x + 4y - z = 6$, $x - y + 5z = 7$. 🔁 **Repeat of 2017 Q.7(a)**

---

## NM-3.5 · Gauss-Seidel Iteration

**Appearances:** 2017, 2018, 2019, 2020, 2021, 2024, CT-02B · **6 papers + CT-02B**

### Computation
- **[2018 Q.4(b) — 05]** Solve the following circuit by using Gauss-Seidel method. (4-mesh planar DC network in a 2x2 grid: 100 V source, 10 A current source, 10/20/25/25/4/8 Ω, mesh currents $I_1$–$I_4$ — see 2018.md Fig Q.4(b))
- **[2019 Q.3(c) — 04]** Obtain the nodal equations from the following circuit. Hence solve for the unknowns using Gauss-Seidel iterative method. Show two iterations only. (2-node DC circuit: 5 A and 10 A current sources, 2/4/6 Ω — see 2019.md Fig Q.3(c))
- **[2020 Q.4(b) — 06]** Solve $I_1, I_2$ and $I_3$ using Gauss-Seidal method. (3-mesh DC circuit: 400 V source, 20/40/10/100 Ω, 10 A source — see 2020.md Fig Q.4(b)) 🔁 **Repeated in 2024 Q.2(b)** (values changed)
- **[2021 Q.7(b) — 06]** Determine the value of $I_0$ in the given circuit using gauss seidel method. (DC circuit: 30 V source, 10/15/8/20 Ω, dependent CCVS $5I_0$ — see 2021.md Fig Q.7(b))
- **[2024 Q.2(b) — 04]** Solve $I_1, I_2$ and $I_3$ using Gauss-Seidal method. (3-mesh DC circuit: 500 V source, 10/20/100 Ω, 5 A source — see 2024.md Fig Q.2(b)) 🔁 **Repeat of 2020 Q.4(b)** (values changed)
- **[CT-02B Q.1(a) — —]** For the system $4x + y + z = 7$, $x + 5y + 2z = -8$, $2x + y + 6z = 6$: rearrange the equations in a suitable form for the Gauss-Seidel iterative method. *(Note: second equation printed with uppercase $X$.)*
- **[CT-02B Q.1(b) — —]** Starting with $x_0 = 0$, $y_0 = 0$, $z_0 = 0$, perform four complete iterations using the Gauss-Seidel method.
- **[CT-02B Q.1(c) — —]** Calculate the absolute error in $x$, $y$, and $z$ between the third and fourth iterations. *(also → NM-1.5)*

---

## NM-3.6 · Relaxation

**Appearances:** 2017, 2018 · **2 papers**

### Theory
- **[2018 Q.4(a) — 02]** What is meant by over-relaxation and under-relaxation?

### Computation
- **[2017 Q.4(c) — 05]** Use the Gauss Seidel method with relaxation $(\lambda = 0.95)$ to solve the following system. If necessary rearrange the equations to achieve convergence (use 3 iterations only). $-3x_1 + x_2 + 12x_3 = 50$, $6x_1 - x_2 - x_3 = 3$, $6x_1 + 9x_2 + x_3 = 40$ *(also → NM-3.5)*

---

## NM-3.7 · Ill-Conditioned Systems

**Appearances:** 2022 · **1 paper**

### Theory
- **[2022 Q.4(c) — 02]** Define ill-conditioned system.

---

## NM-3.8 · Circuit Applications

**Appearances:** 2018, 2019, 2020, 2021, 2024 · **5 papers**

### Computation
- **[2018 Q.4(b) — 05]** Solve the following circuit by using Gauss-Seidel method. (4-mesh planar DC network in a 2x2 grid: 100 V source, 10 A current source, 10/20/25/25/4/8 Ω, mesh currents $I_1$–$I_4$ — see 2018.md Fig Q.4(b)) *(also → NM-3.5)*
- **[2019 Q.3(c) — 04]** Obtain the nodal equations from the following circuit. Hence solve for the unknowns using Gauss-Seidel iterative method. Show two iterations only. (2-node DC circuit: 5 A and 10 A current sources, 2/4/6 Ω — see 2019.md Fig Q.3(c)) *(also → NM-3.5)*
- **[2020 Q.4(b) — 06]** Solve $I_1, I_2$ and $I_3$ using Gauss-Seidal method. (3-mesh DC circuit: 400 V source, 20/40/10/100 Ω, 10 A source; mesh KVL gives $60I_1 - 40I_2 = 400$, $-40I_1 + 150I_2 = 1000$ with $I_3 = 10$ A — see 2020.md Fig Q.4(b)) *(also → NM-3.5)* 🔁 **Repeated in 2024 Q.2(b)** (values changed)
- **[2021 Q.7(b) — 06]** Determine the value of $I_0$ in the given circuit using gauss seidel method. (DC circuit: 30 V source, 10/15/8/20 Ω, dependent CCVS $5I_0$; nodal form $35V_C - 15V_R = 360$, $V_C + 2V_R = 30$ — see 2021.md Fig Q.7(b)) *(also → NM-3.5)*
- **[2024 Q.2(b) — 04]** Solve $I_1, I_2$ and $I_3$ using Gauss-Seidal method. (3-mesh DC circuit: 500 V source, 10/20/100 Ω, 5 A source; mesh KVL gives $30I_1 - 20I_2 = 500$, $-20I_1 + 120I_2 = 500$ with $I_3 = 5$ A — see 2024.md Fig Q.2(b)) *(also → NM-3.5)* 🔁 **Repeat of 2020 Q.4(b)** (values changed)

---

# NM-4 · Curve Fitting

## NM-4.1 · Concepts

**Appearances:** 2017, 2019, 2020, 2021, 2022, 2023, 2024 · **7 papers**

### Theory
- **[2017 Q.5(a) — 03]** Define: (i) Interpolation (ii) Extrapolation (iii) Curve Fitting 🔁 **Repeated in 2019 Q.5(a), 2020 Q.3(a), 2021 Q.3(a), 2023 Q.4(a), 2024 Q.3(a)**
- **[2019 Q.4(a) — 04]** What is curve fitting? Why is it required for ECE engineers? Discuss least square technique condition. *(also → NM-4.4)*
- **[2019 Q.5(a) — 03]** Define interpolation and extrapolation. List two general techniques of curve fitting. 🔁 **Repeat of 2017 Q.5(a)**
- **[2020 Q.3(a) — 03]** What is the main difference between interpolation and extrapolation? Where are they used? 🔁 **Repeat of 2017 Q.5(a)**
- **[2021 Q.3(a) — 02]** When should we use interpolation instead of curve fitting? 🔁 **Repeat of 2017 Q.5(a)**
- **[2021 Q.4(a) — 02]** Give a real life example of curve fitting.
- **[2022 Q.1(c) — 04]** Explain a real life application of curve-fitting. For what type of data points will you use Lagrange's interpolation formula? *(also → NM-4.6)*
- **[2023 Q.4(a) — 03]** Briefly explain interpolation, extrapolation and curve fitting with examples. 🔁 **Repeat of 2017 Q.5(a)**
- **[2024 Q.3(a) — 02]** Discuss the operation of curve fitting and interpolation. 🔁 **Repeat of 2017 Q.5(a)**

---

## NM-4.2 · Least-Squares Linear Regression

**Appearances:** 2017, 2018, 2019, 2024 · **4 papers**

### Theory
- **[2019 Q.4(c) — 02]** Deduce the linear regression expression.

### Computation
- **[2017 Q.6(b) — 04]** Fit a straight line to the $x$ and $y$ values in the first two columns of the following table: $x = 1, 2, 3, 4, 5, 6, 7$; $y = 0.5, 2.5, 2.0, 4.0, 3.5, 6.0, 5.5$. *(Note: "first two columns" printed as is; table arranged in rows in the paper.)* 🔁 **Repeated in 2024 Q.3(c)**
- **[2018 Q.4(c) — 05]** The following data was taken from an experiment that measured the current in a wire for various imposed voltages: $v(\text{V}) = 2, 3, 4, 5, 7, 10$; $i(\text{A}) = 5.2, 7.8, 10.7, 13, 19.3, 27.5$. On the basis of a linear regression of this data, determine current for a voltage of $3.5\text{ V}$. Plot the line to evaluate the fit. *(Note: "linier" printed as is.)*
- **[2024 Q.3(c) — 04]** Fit a straight line to the $x$ and $y$ values in the following table: $x = 1, 2, 3, 4, 5, 6, 7$; $y = 0.5, 2.5, 2, 4, 3.5, 6, 5.5$. 🔁 **Repeat of 2017 Q.6(b)**

---

## NM-4.3 · Non-Linear Regression

**Appearances:** 2017, 2020, 2022 · **3 papers**

### Computation
- **[2017 Q.5(b) — 04]** Determine the constants $a$ & $b$ by the method of least squares such that $y = a e^{bx}$ fits the following data: $x = 2, 4, 6, 8, 10$; $y = 4.077, 11.084, 30.128, 81.897, 222.62$. 🔁 **Repeated in 2020 Q.3(c)**
- **[2020 Q.3(c) — 05]** Define curve fitting. Also determine the constants $a$ and $b$ by the method of least squares such that $y = a e^{bx}$ fits the following data: $x = 2, 4, 6, 8, 10$; $y = 4.077, 11.084, 30.128, 81.897, 222.62$. 🔁 **Repeat of 2017 Q.5(b)** *(also → NM-4.1)*
- **[2022 Q.2(b) — 03]** Using the method of least squares, fit a curve of the form $y = \frac{x}{a + bx}$ to fit the following data $(3, 7.148), (5, 10.231), (8, 13.509), (12, 16.434)$.

---

## NM-4.4 · Regression Criteria & Theory

**Appearances:** 2017, 2019 · **2 papers**

### Theory
- **[2017 Q.6(a) — 04]** With necessary figure(s) explain why minimum sum of error, minimum sum of absolute error and minimum error are ill-suited for regression. Which criterion is best suited for regression?

---

## NM-4.5 · Linear Interpolation

**Appearances:** 2018, 2019 · **2 papers**

### Computation
- **[2018 Q.3(b) — 06]** The upward velocity of a rocket is given as a function of time in table below: $t(\text{s}) = 0, 10, 15, 20, 22.5, 30$; $v(t)(\text{m/s}) = 0, 227.04, 362.78, 517.35, 602.97, 901.67$. Determine the value of the velocity at $t = 16$ seconds using $1^{\text{st}}$ order polynomial.
- **[2019 Q.5(b) — 05]** To verify Ohm's law, an experiment was performed and the results obtained are: $V(\text{volt}) = 5, 10, 15, 20, 25$; $I(\text{amps}) = 1, 2.1, 3, 4.2, 5$. Use linear interpolation to determine the current for $12\text{V}$ of supply. Explain why the result differs from actual value.

---

## NM-4.6 · Lagrange's Interpolation

**Appearances:** 2018, 2019, 2021, 2022, 2023, 2024, CT-02A · **6 papers + CT-02A**

### Theory
- **[2018 Q.3(a) — 02]** Explain the use of Lagrange's interpolation formula.
- **[2021 Q.3(b) — 02]** Differentiate between Newton's interpolation and Lagrange's interpolation. *(also → NM-4.7)*
- **[2024 Q.2(c) — 03]** Describe the Lagrange interpolation method. What are its advantages and disadvantages?

### Computation
- **[2018 Q.3(c) — 04]** Find $f(2.5)$ from the given data: $x = 1, 2, 3$; $f(x) = 0, 1, 8$. *(also → NM-4.8)*
- **[2019 Q.4(b) — 06]** A robot arm with a rapid laser scanner is doing a quick quality check on holes drilled in a $15'' \times 10''$ rectangular plate. The hole centers (origin at bottom left corner) are: $x(\text{in.}) = 2, 4.25, 5.25, 7.81, 9.20, 10.60$; $y(\text{in.}) = 7.2, 7.1, 6.0, 5.0, 3.5, 5.0$. If the laser is traversing from $x = 2$ to $x = 4.25$ to $x = 5.25$ in a quadratic path, what is the value of the $y$ at $x = 4.00$ using a curve fitting technique. *(Note: "leaser" printed as is.)* *(also → NM-4.9)*
- **[2021 Q.3(d) — 04]** Find $y(2)$ from the following data using Lagrange's formula: $x = 0, 1, 3, 4, 5$; $y = 0, 1, 81, 256, 625$. 🔁 **Repeated in 2023 Q.2(b)**
- **[2023 Q.2(b) — 03]** Find $y(2)$ from the following data using Lagrange's formula: $x = 0, 1, 3, 4, 5$; $y = 0, 1, 81, 256, 625$. 🔁 **Repeat of 2021 Q.3(d)**
- **[CT-02A Q.1 — —]** An environmental scientist measures the concentration of a pollutant in a river at different distances from the source: Distance $(\text{km}) = 2, 4, 7, 10$; Concentration $(\text{mg/L}) = 18, 26, 43, 60$. The concentration at $5\text{ km}$ could not be measured due to equipment failure. Use the Lagrange Interpolation Formula to estimate the pollutant concentration at $5\text{ km}$.

---

## NM-4.7 · Newton's Forward Difference

**Appearances:** 2018, 2020, 2021, 2022, 2023, CT-02A · **5 papers + CT-02A**

### Theory
- **[2020 Q.5(a) — 06]** Deduce the Newton's forward difference interpolating polynomial.
- **[2021 Q.3(c) — 04]** Derive the Newton's forward interpolation formula: $y_n(x) = y_0 + p\Delta y_0 + \frac{p(p-1)}{2!}\Delta^2 y_0 + \frac{p(p-1)(p-2)}{3!}\Delta^3 y_0 + \cdots$ 🔁 **Repeated in 2023 Q.2(a)**
- **[2023 Q.2(a) — 04]** Derive the Newton's forward interpolation formula: $y_n(x) = y_0 + p\Delta y_0 + \frac{p(p-1)}{2!}\Delta^2 y_0 + \frac{p(p-1)(p-2)}{3!}\Delta^3 y_0 + \cdots$ 🔁 **Repeat of 2021 Q.3(c)**

### Computation
- **[2022 Q.2(c) — 03]** Using Newton's forward difference formula find the sum $S_n = 1^3 + 2^3 + 3^3 + \cdots + n^3$.
- **[CT-02A Q.2 — —]** A weather station records the temperature every 2 hours: Time $(\text{h}) = 0, 2, 4, 6, 8$; Temperature $(^\circ\text{C}) = 24, 27, 31, 36, 42$. The meteorologist wants to estimate the temperature at $1.5$ and $7$ hours. Use Newton's (Forward/Backward) Interpolation Formula to estimate the temperature. *(also → NM-4.8)*

---

## NM-4.8 · Newton's Backward Difference

**Appearances:** 2017, 2020, 2024, CT-02A · **3 papers + CT-02A**

### Computation
- **[2017 Q.5(c) — 05]** The population of a town in decennial census were as following table in thousand unit. Estimate the population for the year 1955: Year $= 1921, 1931, 1941, 1951, 1961$; Population $= 46, 66, 81, 93, 101$. 🔁 **Repeated (same data, different target year) in 2020 Q.3(b), 2024 Q.3(b)** *(also → NM-4.11)*

---

## NM-4.9 · Newton's Divided Difference / General Interpolation

**Appearances:** 2019, 2020, 2022 · **3 papers**

### Computation
- **[2019 Q.5(c) — 04]** Using Newton's general interpolation formula find $f(x)$ as a polynomial in $x$ for the following table: $x = -1, 0, 3, 6, 7$; $f(x) = 3, -6, 39, 822, 1611$. Also, determine $f(3.5)$ using the polynomial.
- **[2020 Q.5(b) — 06]** Using Newton's divided difference interpolating polynomial estimate the value of signal $s(t)$ at $t = 2.25\text{ sec}$ for the following tabulated values: $t = 0.5, 0.2, 1.4, 2.2, 3.0$; $s(t) = -10.25, -3.768, 5.976, 28.972, 79.0$.
- **[2022 Q.2(a) — 04]** Find the polynomial which fits the following data: $x = -1, 1, 2$; $y = 7, 5, 15$. *(also → NM-4.6)*

---

## NM-4.10 · Gauss Forward / Backward & Stirling's Formulas

**Appearances:** 2021 · **1 paper**

### Computation
- **[2021 Q.4(b) — 05]** From the following table, calculate the value of $e^{1.17}$ using Gauss' forward formula: $x = 1.00, 1.05, 1.10, 1.15, 1.20, 1.25, 1.30$; $e^x = 2.7183, 2.8577, 3.0042, 3.1582, 3.3201, 3.4903, 3.6693$.

---

## NM-4.11 · Difference Table Formation & Applications

**Appearances:** 2017, 2020, 2021, 2022, 2024 · **5 papers**

### Computation
- **[2020 Q.3(b) — 04]** The population of a town in the decennial census was as given below. Estimate the population for the year (i) 1895 and (ii) 1925. Year $x = 1891, 1901, 1911, 1921, 1931$; Population (in thousands) $y = 46, 66, 81, 93, 101$. 🔁 **Repeat (same data, different target years) of 2017 Q.5(c); also in 2024 Q.3(b)** *(also → NM-4.7 / NM-4.8)*
- **[2021 Q.4(c) — 05]** You have a gas sensor. It sends a value in 2 seconds. The table of received values: $t(\text{s}) = 1, 3, 5, 7, 9$; Value $= 24, 120, 336, 720, 1200$. What will be the sensor's reading at 10s? *(also → NM-4.8)*
- **[2024 Q.3(b) — 04]** The population of a town in decennial census were as following table in thousand units. Estimate the population for the year 1995. Year $= 1921, 1931, 1941, 1951, 1961$; Population (in thousands) $= 46, 66, 81, 93, 101$. 🔁 **Repeat (same data, different target year) of 2017 Q.5(c), 2020 Q.3(b)** *(also → NM-4.8)*

---

## NM-4.12 · Interpolation with Two Independent Variables

**Appearances:** None — not examined in any paper 2017–2024.

---

# NM-5 · Numerical Integration

## NM-5.1 · Trapezoidal Rule

**Appearances:** 2018, 2019, 2021, 2022 · **4 papers**

### Theory
- **[2019 Q.6(c) — 03]** Discuss trapezoidal rule of numerical integration.
- **[2021 Q.8(a) — 04]** Derive the following numerical integration formula: $\int_{x_0}^{x_n} y\,dx = \frac{h}{2}[y_0 + 2(y_1 + y_2 + \cdots + y_{n-1}) + y_n]$

### Computation
- **[2018 Q.6(b) — 04]** Determine the value of $n$ so that the trapezoidal rule will approximate the value of $\int_0^1 \sqrt{1 + x^2}\,dx$ with an error that is less than $0.01$. *(also → NM-5.6)*
- **[2022 Q.3(a) — 04]** Compute the value of $I = \int_0^1 \frac{dx}{1 + x^2}$ using the trapezoidal rule with $h = 0.5, 0.25$ and $0.125$. Then obtain a better estimate using Romberg's method. *(also → NM-5.5)*

---

## NM-5.2 · Simpson's 1/3 Rule

**Appearances:** 2018, 2019, 2020, 2023 · **4 papers**

### Theory
- **[2019 Q.7(a) — 04]** Derive Simpson's one-third rule and hence show that the rule is exact up to degree three.

### Computation
- **[2018 Q.6(a) — 08]** 🔁 **Repeated in 2023 Q.4(b)** The vertical distance covered by a rocket from $t = 8$ to $t = 30$ seconds is given by: $x = \int_8^{30}\left(2000 \ln\left[\frac{140000}{140000 - 2100t}\right] - 9.8t\right)dt$ — (i) Use eight-segment Simpson's $\frac{1}{3}$ rule to find the distance covered. (ii) Find the true error of part (i). (iii) Find the absolute relative error for part (i).
- **[2020 Q.6(b) — 05]** A circuit is giving the following output voltage equation: $v_0 = -\frac{1}{RC}\int_0^t v_i(t)\,dt$ where $R = 10\text{ k}\Omega$, $C = 1\ \mu\text{F}$ and the input is tabulated as $t = 0, 0.25, 0.50, 0.75, 1.00, 1.25$; $v_i(t) = 1, 0.9793, 0.9195, 0.8261, 0.7081, 0.6201$. Obtain the value of $v_0$ when $t = 1.25$. Use Simpson's $1/3$rd rule.
- **[2023 Q.4(b) — 05]** 🔁 **Repeat of 2018 Q.6(a)** The distance covered by a rocket from $t = 8$ to $t = 30$ is given by $x = \int_8^{30}\left(2000 \ln\left[\frac{140000}{140000 - 2100t}\right] - 9.8t\right)dt$ — (i) Use Simpson's $1/3^{\text{rd}}$ rule to find the approximate value of $x$. (ii) Find the true error, $E_t$. (iii) Find the absolute relative true error, $\lvert\epsilon_t\rvert$.

---

## NM-5.3 · Simpson's 3/8 Rule

**Appearances:** 2019 · **1 paper**

### Computation
- **[2019 Q.7(b) — 04]** Evaluate $\int_1^2 (x^2 + 1)\,dx$ using Simpson's 3/8 rule.

---

## NM-5.4 · Rule Comparison & Step Constraints

**Appearances:** 2020, 2023 · **2 papers**

### Theory
- **[2020 Q.6(a) — 03]** 🔁 **Repeated in 2023 Q.4(c)** Compare Simpson's $1/3$rd and $3/8$th rules.
- **[2023 Q.4(c) — 02]** 🔁 **Repeat of 2020 Q.6(a)** Compare Simpson's $1/3^{\text{rd}}$ and $3/8^{\text{th}}$ rules.

---

## NM-5.5 · Romberg's Method

**Appearances:** 2021, 2022, 2023 · **3 papers**

### Computation
- **[2021 Q.8(b) — 04]** 🔁 **Repeated in 2023 Q.2(c)** Use Romberg's method to compute: $\int_1^2 \frac{1}{2+x}\,dx$. Consider $h = 0.5, 0.25, 0.125$.
- **[2023 Q.2(c) — 03]** 🔁 **Repeat of 2021 Q.8(b)** Use Romberg's method to compute: $\int_1^2 \frac{1}{2+x}\,dx$. Consider $h = 0.5, 0.25, 0.125$.

---

## NM-5.6 · Error Analysis in Integration

**Appearances:** 2018, 2023 · **2 papers**

### Computation
- **[2018 Q.6(a) — 08]** 🔁 **Repeated in 2023 Q.4(b)** The vertical distance covered by a rocket from $t = 8$ to $t = 30$ seconds is given by: $x = \int_8^{30}\left(2000 \ln\left[\frac{140000}{140000 - 2100t}\right] - 9.8t\right)dt$ — (i) Use eight-segment Simpson's $\frac{1}{3}$ rule to find the distance covered. (ii) Find the true error of part (i). (iii) Find the absolute relative error for part (i).
- **[2023 Q.4(b) — 05]** 🔁 **Repeat of 2018 Q.6(a)** The distance covered by a rocket from $t = 8$ to $t = 30$ is given by $x = \int_8^{30}\left(2000 \ln\left[\frac{140000}{140000 - 2100t}\right] - 9.8t\right)dt$ — (i) Use Simpson's $1/3^{\text{rd}}$ rule to find the approximate value of $x$. (ii) Find the true error, $E_t$. (iii) Find the absolute relative true error, $\lvert\epsilon_t\rvert$.

---

## NM-5.7 · Applied Integration

**Appearances:** 2018, 2020, 2023 · **3 papers**

### Computation
- **[2018 Q.6(a) — 08]** 🔁 **Repeated in 2023 Q.4(b)** The vertical distance covered by a rocket from $t = 8$ to $t = 30$ seconds is given by: $x = \int_8^{30}\left(2000 \ln\left[\frac{140000}{140000 - 2100t}\right] - 9.8t\right)dt$ — (i) Use eight-segment Simpson's $\frac{1}{3}$ rule to find the distance covered. (ii) Find the true error of part (i). (iii) Find the absolute relative error for part (i).
- **[2020 Q.6(b) — 05]** A circuit is giving the following output voltage equation: $v_0 = -\frac{1}{RC}\int_0^t v_i(t)\,dt$ where $R = 10\text{ k}\Omega$, $C = 1\ \mu\text{F}$ and the input is tabulated as $t = 0, 0.25, 0.50, 0.75, 1.00, 1.25$; $v_i(t) = 1, 0.9793, 0.9195, 0.8261, 0.7081, 0.6201$. Obtain the value of $v_0$ when $t = 1.25$. Use Simpson's $1/3$rd rule.
- **[2023 Q.4(b) — 05]** 🔁 **Repeat of 2018 Q.6(a)** The distance covered by a rocket from $t = 8$ to $t = 30$ is given by $x = \int_8^{30}\left(2000 \ln\left[\frac{140000}{140000 - 2100t}\right] - 9.8t\right)dt$ — (i) Use Simpson's $1/3^{\text{rd}}$ rule to find the approximate value of $x$. (ii) Find the true error, $E_t$. (iii) Find the absolute relative true error, $\lvert\epsilon_t\rvert$.

---

# NM-6 · Optimization

## NM-6.1 · Optimization Concepts

**Appearances:** 2021 · **1 paper**

### Theory
- **[2021 Q.6(d) — 02]** Differentiate between constrained and unconstrained optimization.

---

## NM-6.2 · One-Dimensional Unconstrained Optimization

**Appearances:** 2021 · **1 paper**

### Computation
- **[2021 Q.6(b) — 03]** Use Newton's method to find the maximum of $f(x) = 2\sin x - \frac{x^2}{10}$ with an initial guess of $x_0 = 2.5$.

---

## NM-6.3 · Optima from Tabulated Data

**Appearances:** 2018 · **1 paper**

### Computation
- **[2018 Q.5(b) — 06]** From the following table find $x$, correct to two decimal places for which $y$ is maximum and find this value of $y$: $x = 1.2, 1.3, 1.4, 1.5, 1.6$; $y = 0.9320, 0.9636, 0.9855, 0.9975, 0.9996$.

---

# NM-7 · Numerical Differentiation

## NM-7.1 · Basis & Difference Formulas

**Appearances:** 2019 · **1 paper**

### Theory
- **[2019 Q.6(a) — 04]** What is the basis of numerical differentiation? Write at least four difference equations to obtain numerical differentiation.

---

## NM-7.2 · First Derivative from Tabulated Data

**Appearances:** 2019, 2020, 2021, 2022 · **4 papers**

### Computation
- **[2019 Q.6(b) — 05]** A 1 Henry inductance gets current through it at different times as follows. Obtain the voltage across it at $t = 0.27\text{ sec}$ using numerical differentiation: $t_{\text{sec}} = 0.25, 0.26, 0.27, 0.28, 0.29$; $I_{\text{amp}} = 0.2474, 0.2571, 0.2667, 0.2764, 0.2860$. *(also → NM-7.4)*
- **[2020 Q.6(c) — 04]** The following table gives the angular displacements $\theta$ (radian) at different intervals of time $t$ (sec): $\theta = 0.052, 0.105, 0.168, 0.242, 0.327, 0.408, 0.489$; $t = 0, 0.02, 0.04, 0.06, 0.08, 0.10, 0.12$. Calculate the angular velocity at the instant $t = 0.06\text{ sec}$. *(also → NM-7.4)*
- **[2021 Q.7(c) — 05]** From the values of $x$ and $y$ in the following table, determine $\frac{dy}{dx}$ and $\frac{d^2y}{dx^2}$ for $x = 1.2$: $x = 1.0, 1.2, 1.4, 1.6, 1.8, 2.0, 2.2$; $y = 2.7183, 3.3201, 4.0552, 4.9530, 6.0496, 7.3891, 9.0250$. *(also → NM-7.3)*
- **[2022 Q.3(b) — 04]** A cubic function $y = f(x)$ satisfies the following data: $x = 0, 1, 3, 4, 2$; $f(x) = 1, 4, 40, 85, 17$. Determine the value of $f'(4)$.

---

## NM-7.3 · Second Derivative & Formula Derivation

**Appearances:** 2017, 2018, 2021 · **3 papers**

### Theory
- **[2017 Q.6(c) — 04]** Derive a formula to find the second derivative of a tabulated function.
- **[2018 Q.5(a) — 06]** State Newton's forward formula to evaluate $\frac{d^2 y}{dx^2}$ for any value $x \in [x_0, x_n]$.

---

## NM-7.4 · Applied Differentiation

**Appearances:** 2019, 2020, 2021 · **3 papers**

### Theory
- **[2021 Q.6(a) — 02]** Write down a real-life application of numerical differentiation.

---

# NM-8 · Ordinary Differential Equations

## NM-8.1 · IVP vs BVP Concepts

**Appearances:** 2021, 2024 · **2 papers**

### Theory
- **[2021 Q.5(a) — 02]** Define boundary value and initial value problem.

---

## NM-8.2 · Euler's Method

**Appearances:** 2018, 2019, 2020, 2021, 2023 · **5 papers**

### Theory
- **[2019 Q.7(c) — 04]** Discuss Euler's method to solve ordinary differential equations.

### Computation
- **[2020 Q.7(b) — 04]** 🔁 **Repeated in 2024 Q.4(b)** (same ODE; 2024 asks RK4) Solve, by Euler's method, the equation $\frac{dy}{dx} = x + y$, $y(0) = 0$. Choose $h = 0.2$ and compute $y(0.4)$ and $y(0.6)$.
- **[2021 Q.8(c) — 04]** 🔁 **Repeated in 2023 Q.3(b)(i)** Using Euler's method, determine $\frac{dy}{dx} = \frac{3}{5}x^3 y$; Consider $y(0) = 1$.
- **[2023 Q.3(b) — 05]** 🔁 **Part (i) is a repeat of 2021 Q.8(c)** Using Euler's method, solve the following problems: (i) $\frac{dy}{dx} = \frac{3}{5}x^3 y$, $y(0) = 1$; (ii) $\frac{dy}{dx} = 1 + y^2$, $y(0) = 0$.

---

## NM-8.3 · Modified Euler / Heun's Method

**Appearances:** 2017, 2018, 2020 · **3 papers**

### Theory
- **[2020 Q.7(a) — 04]** Derive modified Euler's method. What is the major limitation of Euler's method? *(also → NM-8.2)*

### Computation
- **[2017 Q.8(a) — 05]** Given the differential equation $\frac{dy}{dx} = x^2 + y$ with $y(0) = 1$, compute $y(0.02)$ using Euler's modified method.
- **[2018 Q.7(a) — 06]** Solve $\frac{dy}{dx} = 1 - y$ with the initial condition $x = 0$, $y = 0$ by using modified Euler's method. Tabulate the solutions at $x = 0.1, 0.2, 0.3$.

---

## NM-8.4 · Runge-Kutta 2nd Order

**Appearances:** 2020, CT-02B · **2 papers**

### Computation
- **[2020 Q.7(c) — 04]** Given $\frac{dy}{dx} = y - x$, where $y(0) = 2$, find $y(0.1)$ and $y(0.2)$ by using Runge-Kutta second order formula.
- **[CT-02B Q.2(a) — —]** Consider the initial value problem $\frac{dy}{dx} = x^2 - y$, $y(0) = 1$. Using RK2 method with step size $h = 0.2$, calculate $y(0.2)$ and $y(0.4)$. Show both the predictor and corrector calculations at each step.

---

## NM-8.5 · Runge-Kutta 4th Order

**Appearances:** 2017, 2018, 2019, 2024, CT-02B · **5 papers**

### Computation
- **[2017 Q.8(b) — 05]** Use Runge-Kutta fourth order formula to find $y(0.2)$ and $y(0.4)$ given that $y' = \frac{y^2 - x^2}{y^2 + x^2}$, $y(0) = 1$.
- **[2018 Q.7(b) — 06]** Use the Runge-Kutta method to solve $10\frac{dy}{dx} = x^2 - y^2$, $y(0) = 1$ for the interval $0 < x \le 0.4$ with $h = 0.1$.
- **[2019 Q.8(a) — 06]** Given $\frac{dy}{dx} = x^2 + y^2$ where $y = 0$ when $x = 0$. Find $y(0.4)$ assuming $h = 0.2$. *(Note: no method named in the paper; standardly worked by RK4)*
- **[2024 Q.4(b) — 05]** 🔁 **Repeat of 2020 Q.7(b)** (same ODE; 2020 asks Euler) Use the fourth-order Runge-Kutta method (RK4) to solve $\frac{dy}{dx} = x + y$ with initial condition $y(0) = 1$ over the interval $x = 0$ to $x = 0.2$ with a step size $h = 0.1$. Show an intermediate calculation. *(Note: "circulation" printed in original; means intermediate calculation/iteration)*
- **[CT-02B Q.2(b) — —]** Consider the initial value problem $\frac{dy}{dx} = x^2 - y$, $y(0) = 1$. Using the RK4 method calculate $y(0.2)$, also compare result with RK2 method.

---

## NM-8.6 · Higher-Order & Systems of ODEs

**Appearances:** 2018 · **1 paper**

### Computation
- **[2018 Q.8(b) — 06]** Use the Euler's method to solve $\frac{d^2 y}{dt^2} - 0.5t = y$ where $y(0) = 2$ and $y'(0) = 0$. Solve from $t = 0$ to $0.4$ using $h = 0.1$. *(also → NM-8.2)*

---

## NM-8.7 · ODE Formulation from Physical Problems

**Appearances:** 2021 · **1 paper**

### Computation
- **[2021 Q.5(c) — 05]** A capacitor loses 4% of its remaining charge every second. It is fully charged with 100 Coulomb of charge. What will be the remaining charge after 10 sec. Develop the ODE and also determine the solution.

---

## NM-8.8 · Boundary Value Problems

**Appearances:** 2021, 2024 · **2 papers**

### Theory
- **[2024 Q.4(a) — 03]** Describe the general approach for solving boundary value problems numerically. How does it differ from solving initial value problems? *(also → NM-8.1)*

### Computation
- **[2021 Q.5(b) — 05]** Solve the boundary value problem $\frac{d^2y}{dx^2} - y = 0$ with $y(0) = 0$ and $y(2) = 3.62686$.

---

# NM-9 · Eigenvalue Problems

## NM-9.1 · Eigenvalues & Eigenvectors

**Appearances:** 2017, 2023 · **2 papers**

### Computation
- **[2017 Q.7(b) — 06]** 🔁 **Repeated in 2023 Q.3(a)** Find the eigen-values and eigen-vectors of the following matrix: $A = \begin{bmatrix} 5 & 0 & 1 \\ 0 & -2 & 0 \\ 1 & 0 & 5 \end{bmatrix}$
- **[2023 Q.3(a) — 05]** 🔁 **Repeat of 2017 Q.7(b)** Find the Eigen-values and Eigen-vectors of the following matrix: $A = \begin{bmatrix} 5 & 0 & 1 \\ 0 & -2 & 0 \\ 1 & 0 & 5 \end{bmatrix}$

---

# NM-10 · Partial Differential Equations

## NM-10.1 · PDE Classification & Theory

**Appearances:** 2020 · **1 paper**

### Theory
- **[2020 Q.8(a) — 06]** Write 4 types of partial differential equations. Discuss briefly the solving process of any of the equations using numerical iterative technique.

---

## NM-10.2 · Laplace Equation

**Appearances:** 2018, 2019, 2020 · **3 papers**

### Computation
- **[2018 Q.8(a) — 06]** Find the potential distribution at the interior nodes using Leibmann's method. `(3×3 grid, boundaries Top = 100V, Bottom = 0V, Left = 75V, Right = 50V, insulating gaps at the four corners, interior nodes 1–4 — see 2018.md Fig Q.8(a))`
- **[2019 Q.8(b) — 06]** Solve the Laplace's equation for the square region shown in the following figure, the boundary values being indicated in the figure. `(3×3 mesh on square region OCBA; boundary values Bottom = 0, 4, 5; Right = 5, 4; Top = 1, 2; Left = 0, 2, 1; interior nodes u₁–u₄ — see 2019.md Fig Q.8(b))`
- **[2020 Q.8(b) — 06]** Solve the equation $\frac{\partial^2 E(x,y)}{\partial x^2} + \frac{\partial^2 E(x,y)}{\partial y^2} = 0$ in the domain of the following figure by Liebmann method. Consider $\Delta x = \Delta y$. `(3×3 grid, boundaries Top = 1, Bottom = 0, Left = 0, Right = 0, interior nodes E₁–E₄ — see 2020.md Fig Q.8(b))`

---

## NM-10.3 · Poisson Equation

**Appearances:** 2021 · **1 paper**

### Computation
- **[2021 Q.6(c) — 05]** Solve the Poisson equation $U_{xx} + U_{yy} = -10(x^2 + y^2 + 10)$ in the domain of the given figure below. `(3×3 grid on 0 ≤ x ≤ 3, 0 ≤ y ≤ 3 with h = k = 1, u = 0 on all four boundaries, interior nodes u₁–u₄ — see 2021.md Fig Q.6(c))`

---

## NM-10.4 · Liebmann's Iterative Method

**Appearances:** 2018, 2020 · **2 papers**

### Computation
- **[2018 Q.8(a) — 06]** Find the potential distribution at the interior nodes using Leibmann's method. `(3×3 grid, boundaries Top = 100V, Bottom = 0V, Left = 75V, Right = 50V, insulating gaps at the four corners, interior nodes 1–4 — see 2018.md Fig Q.8(a))`
- **[2020 Q.8(b) — 06]** Solve the equation $\frac{\partial^2 E(x,y)}{\partial x^2} + \frac{\partial^2 E(x,y)}{\partial y^2} = 0$ in the domain of the following figure by Liebmann method. Consider $\Delta x = \Delta y$. `(3×3 grid, boundaries Top = 1, Bottom = 0, Left = 0, Right = 0, interior nodes E₁–E₄ — see 2020.md Fig Q.8(b))`

---

## NM-10.5 · Boundary Conditions in PDEs

**Appearances:** 2024 · **1 paper**

### Theory
- **[2024 Q.4(c) — 02]** State the importance of boundary conditions in solving PDEs numerically.

<br>

# ═══ SECTION 2 — DISCRETE MATHEMATICS ═══

*Source papers: 2022, 2023, 2024 (Section B) · CT-04*
*Not present in the 2017–2021 papers — Discrete Mathematics entered the course with the 2022 OBE curriculum revision.*

<br>

# DM-1 · Set Theory

## DM-1.1 · Operations on Sets

**Appearances:** None — not examined in 2022, 2023, 2024 or CT-04.

---

## DM-1.2 · Algebraic Properties of Sets

**Appearances:** None — not examined in 2022, 2023, 2024 or CT-04.

---

## DM-1.3 · Computer Representation of Sets

**Appearances:** None — not examined in 2022, 2023, 2024 or CT-04.

---

## DM-1.4 · Power Set Theorem

**Appearances:** None — not examined in 2022, 2023, 2024 or CT-04.

---

# DM-2 · Relations

## DM-2.1 · Properties of Relations

**Appearances:** None — not examined in 2022, 2023, 2024 or CT-04.

---

## DM-2.2 · Binary Relations

**Appearances:** None — not examined in 2022, 2023, 2024 or CT-04.

---

## DM-2.3 · Partial Ordering Relations

**Appearances:** None — not examined in 2022, 2023, 2024 or CT-04.

---

## DM-2.4 · Equivalence Relations

**Appearances:** None — not examined in 2022, 2023, 2024 or CT-04.

---

# DM-3 · Propositional Logic

## DM-3.1 · Propositions & Syntax

**Appearances:** 2022, 2024 · **2 of 3 OBE papers**

### Theory
- **[2022 Q.5(a) — 03]** Explain how proposition differs from traditional sentence. Give some examples.
- **[2024 Q.5(a) — 02]** Define propositional logic and explain the difference between a proposition and propositional variable.

---

## DM-3.2 · Logical Connectives & Truth Tables

**Appearances:** 2022, 2023, 2024, CT-04 · **3 of 3 OBE papers**

### Computation
- **[2022 Q.6(b) — 04]** Determine whether the bi-conditionals are true or false: (i) $2 + 2 = 4$ if and only if $1 + 1 = 2$; (ii) $1 + 1 = 2$ if and only if $2 + 3 = 4$; (iii) $1 + 1 = 3$ if and only if monkeys can fly; (iv) $0 > 1$ if and only if $2 > 1$ — 🔁 **Repeated verbatim in 2024 Q.7(b)**
- **[2024 Q.7(b) — 04]** Determine whether the bi-conditionals are true of false: i) $2 + 2 = 4$ if and only if $1 + 1 = 2$; ii) $1 + 1 = 2$ if and only if $2 + 3 = 4$; iii) $1 + 1 = 3$ if and only if monkeys can fly; iv) $0 > 1$ if and only if $2 > 1$ *(Note: "true of false" printed as is; means true or false)* — 🔁 **Repeat of 2022 Q.6(b)**
- **[CT-04 Q.2(c) — 7]** Construct a truth table for the resulting expression. (The expression from the requirement *"A student can start the examination if and only if the student is authenticated and the examination server is available"*, with $p$: The student is authenticated; $q$: The examination server is available; $r$: The student can start the examination — rewritten using only $\neg$, $\lor$, $\land$.) *(also → DM-3.7)*
- **[CT-04 Q.3(c) — 7]** Construct the complete truth table from (b) — i.e. of the conjunction of the three embedded-system requirements over $p$: The sensor is active; $q$: The controller receives data. *(also → DM-3.7)*

---

## DM-3.3 · Tautology, Contradiction & Contingency

**Appearances:** 2023, 2024, CT-04 · **2 of 3 OBE papers**

### Theory
- **[2024 Q.6(a) — 04]** Explain the concepts of tautology, contradiction and contingency in propositional logic. Explain their characteristics with example.

### Computation
- **[2023 Q.5(c) — 02]** Show that each of the conditional statements is a tautology by using truth tables. (i) $\neg(p \to q) \to p$ (ii) $p \to (p \lor q)$
- **[CT-04 Q.1 — 6]** Let $p$, $q$, and $r$ be propositions. Using a complete truth table, establish that the following compound proposition is a tautology: $[(p \to q) \land (q \to r)] \to (p \to r)$ — *(related: 2024 Q.5(b) classifies $(p \to q) \land (q \to r)$ as valid/satisfiable/unsatisfiable; 2023 Q.6(c) is the inference-rule form of the same hypothetical-syllogism idea)*

---

## DM-3.4 · Valid, Satisfiable & Unsatisfiable Formulas

**Appearances:** 2024, CT-04 · **1 of 3 OBE papers**

### Computation
- **[2024 Q.5(b) — 04]** Given the propositional formula $(p \to q) \land (q \to r)$, whether the formula is valid, satisfiable or unsatisfiable. *(Note: i.e. determine whether the formula is valid, satisfiable or unsatisfiable)* — *(related: CT-04 Q.1 proves $[(p \to q) \land (q \to r)] \to (p \to r)$ is a tautology; 2023 Q.6(c) is the inference-rule form of the same hypothetical-syllogism idea)*
- **[CT-04 Q.3(d) — 7]** Establish the truth assignments that satisfy all three requirements simultaneously. (Requirements: *If the sensor is active, then the controller receives data; The controller does not receive data unless the sensor is active; The sensor is active if and only if the controller receives data* — with $p$: The sensor is active; $q$: The controller receives data.)

---

## DM-3.5 · Logical Equivalence

**Appearances:** 2023 · **1 of 3 OBE papers**

### Computation
- **[2023 Q.6(a) — 02]** Show that $\neg(p \leftrightarrow q)$ and $\neg p \leftrightarrow q$ are logically equivalent.

---

## DM-3.6 · Translation: English → Logic

**Appearances:** 2024, CT-04 · **1 of 3 OBE papers**

### Computation
- **[CT-04 Q.3(a) — 7]** Translate all three statements into propositional logic. The three statements describing an embedded system are: *If the sensor is active, then the controller receives data.* / *The controller does not receive data unless the sensor is active.* / *The sensor is active if and only if the controller receives data.* Let $p$: The sensor is active; $q$: The controller receives data. *(Note: Q.3 printed as 6 marks on the original script; total marks 20)*

---

## DM-3.7 · System Specification & Consistency

**Appearances:** 2024, CT-04 · **1 of 3 OBE papers**

### Computation
- **[2024 Q.5(c) — 04]** Are these system specifications consistent? *"The system is in multiuser state if and only if it is operating normally, the kernel is functioning. The kernel is not functioning or the system is in interrupt mode. If the system is not in multiuser state, then it is in interrupt mode. The system is not in interrupt mode."* *(also → DM-3.6)*
- **[CT-04 Q.2(a) — 7]** Translate the requirement into propositional logic. A university online examination system is described by the following requirement: *"A student can start the examination if and only if the student is authenticated and the examination server is available."* Let $p$: The student is authenticated; $q$: The examination server is available; $r$: The student can start the examination. *(also → DM-3.6)*
- **[CT-04 Q.3(b) — 7]** Form a single compound proposition by taking the conjunction of the three requirements. (The three embedded-system statements of Q.3(a), with $p$: The sensor is active; $q$: The controller receives data.)

---

## DM-3.8 · Normal Forms & Functional Completeness

**Appearances:** 2022, 2024, CT-04 · **2 of 3 OBE papers**

### Computation
- **[2022 Q.5(c) — 02]** Show that $\neg$ and $\land$ form a functionally complete collection of logical operators.
- **[2024 Q.6(b) — 06]** A security system triggers an alarm if (a) motion is detected and the window is open, or (b) the door sensor is active but the security code is not entered. i) Assign propositional variables; ii) Express the alarm condition as a single proposition; iii) Convert it into both CNF and DNF, describe each transformation step. *(also → DM-3.7)*
- **[CT-04 Q.2(b) — 7]** Rewrite the resulting expression using only $\neg$, $\lor$, and $\land$. (The translation of *"A student can start the examination if and only if the student is authenticated and the examination server is available"*, i.e. $r \leftrightarrow (p \land q)$.) *(also → DM-3.7)*

---

## DM-3.9 · Rules of Inference & Valid Arguments

**Appearances:** 2022, 2023 · **2 of 3 OBE papers**

### Theory
- **[2023 Q.6(b) — 04]** Briefly explain modus ponens, modus tollens, hypothetical syllogism, disjunctive syllogism with truth tables and examples.

### Computation
- **[2023 Q.6(c) — 04]** With these hypothesis: → *"It is not sunny this afternoon and it is colder than yesterday."* → *"We will go swimming only if it is sunny."* → *"If we do not swimming, then we will take a canoe trip".* → *"If we take a canoe trip then we will be home by sunset".* Using the inference rules, construct a valid argument for the conclusion: *"we will be home by sunset"*. — *(related: CT-04 Q.1 proves $[(p \to q) \land (q \to r)] \to (p \to r)$ is a tautology; 2024 Q.5(b) classifies $(p \to q) \land (q \to r)$ — the same hypothetical-syllogism idea)* *(also → DM-3.6)*

---

## DM-3.10 · Logic Puzzles

**Appearances:** 2022, 2023 · **2 of 3 OBE papers**

### Computation
- **[2022 Q.5(d) — 02]** Consider these statements, of which the first three are premises and the fourth is a valid conclusion. *"All humming are richly colored"* / *"No large birds live on honey"* / *"Birds that do not live on honey are dull in order"* / *"Humming birds are small"* *(Note: classic Lewis Carroll puzzle printed verbatim as in the paper)*
- **[2022 Q.6(a) — 06]** Knights who always tell the truth, Knaves who always lie and Spies who can either lie or tell the truth. You encounter three people A, B and C. You know one of those is a knight, one is knave and one is spy. Each of the three people knows the type of person each of other two is for each of these situations. If possible determine whether there is a unique solution and determine who the knave, knight and spy are. When there is no unique solution, list all possible solutions or state that there are no solutions. (i) A says "C is the Knave", B says "A is the Knight" and C says "I am the spy" (ii) A says "I am the Knave", B says "I am the Knave" and C says "I am the Knave"
- **[2023 Q.5(b) — 04]** Four friends have been identified as suspects for an unauthorized access into a computer system. They have made statements to the investigating authorities. Alice said *"Carlos did it."* John said *"I did not do it."* Carlos said *"Diana did it."* Diana said *"Carlos lied when he said that I did it."* (i) If the authorities also know that exactly one of the four suspects is telling the truth, who did it? Explain your reasoning. (ii) If the authorities also know that exactly one is lying, who did it? Explain your reasoning.

---

## DM-3.11 · Logic Gates & Digital Circuits

**Appearances:** 2023 · **1 of 3 OBE papers**

### Computation
- **[2023 Q.5(a) — 04]** Build a digital circuit that produces the output $(p \lor \neg r) \land (\neg p \lor (q \lor \neg r))$ when given input bits $p, q,$ and $r$.

---

## DM-3.12 · Predicates & Quantifiers

**Appearances:** None — not examined in 2022, 2023, 2024 or CT-04.

---

## DM-3.13 · Logic Extensions

**Appearances:** 2022 · **1 of 3 OBE papers** *(2023 Q.7(c) also cross-references here — filed primary under DM-5.2)*

### Computation
- **[2022 Q.5(b) — 03]** The truth value of the conjunction of two propositions in fuzzy logic is the minimum of the truth values of the statements "Fred and John are happy" and "Neither Fred nor John is happy". Prove the statement.

---

# DM-4 · Proof Techniques

## DM-4.1 · Structure of Formal Proofs

**Appearances:** None — not examined in 2022, 2023, 2024 or CT-04.

---

## DM-4.2 · Direct Proofs

**Appearances:** 2022, 2023 *(embedded only)* — never asked as a standalone Proof Techniques
question. 2022 Q.7(d) (the congruence identity `(2^a − 1) mod (2^b − 1)`) and 2023 Q.7(c) (composite
`n` has a prime divisor ≤ √n) each contain a proof, and both are filed under DM-5.9 with an
`*(also → DM-4.2)*` cross-reference. No paper has asked for a proof *technique* by name.

---

## DM-4.3 · Proof by Contradiction

**Appearances:** None — not examined in 2022, 2023, 2024 or CT-04.

---

## DM-4.4 · Proof by Contraposition

**Appearances:** None — not examined in 2022, 2023, 2024 or CT-04.

---

## DM-4.5 · Mathematical Induction

**Appearances:** None — not examined in 2022, 2023, 2024 or CT-04.

---

# DM-5 · Number Theory

## DM-5.1 · Divisibility & Fundamental Theorem of Arithmetic

**Appearances:** None as an examined topic — not asked in 2022, 2023, 2024 or CT-04. *Invoked only
implicitly by 2023 Q.7(c) (a composite number has a prime divisor ≤ √n), which is filed under DM-5.2
and is listed there with a `*(also → DM-5.2)*` cross-reference. Unique prime factorisation itself is
never stated or required.*

---

## DM-5.2 · Prime Numbers

**Appearances:** 2023 · **1 of 3 OBE papers**

### Computation
- **[2023 Q.7(c) — 03]** If $n$ is a composite integer then $n$ has a prime divisor less than or equal to $\sqrt{n}$. *(Note: i.e. prove that if $n$ is a composite integer…)* *(also → DM-5.9)*

---

## DM-5.3 · GCD, LCM & Euclidean Algorithm

**Appearances:** 2022 · **1 of 3 OBE papers** *(2023 Q.7(c) also cross-references here — filed primary under DM-5.2)*

### Computation
- **[2022 Q.7(c) — 02]** Find the greatest common divisor of 414 and 662 using the extended Euclidian algorithm.

---

## DM-5.4 · Modular Arithmetic & Congruence

**Appearances:** 2022, 2023, 2024 · **3 of 3 OBE papers**

### Computation
- **[2022 Q.7(a) — 03]** Suppose that $a$ and $b$ are integers, $a \equiv 11 \pmod{19}$ and $b \equiv 3 \pmod{19}$. Find the integer $c$ with $0 \le c \le 18$ such that (i) $c \equiv 7a + 3b \pmod{19}$ (ii) $c \equiv a^3 + 4b^3 \pmod{19}$ — 🔁 **Repeated verbatim in 2024 Q.8(a)**
- **[2023 Q.7(a) — 04]** Suppose that $a$ and $b$ are integers, $a \equiv 4 \pmod{13}$, and $b \equiv 9 \pmod{13}$. Find the integer $c$ with $0 \le c \le 12$ such that (i) $c = 2a + 3b \pmod{13}$ (ii) $c = a^2 + b^2 \pmod{13}$ — *(related: same modular-arithmetic template as 2022 Q.7(a) / 2024 Q.8(a), different numbers)*
- **[2024 Q.8(a) — 04]** Suppose that $a$ and $b$ are integers, $a \equiv 11 \pmod{19}$ and $b \equiv 3 \pmod{19}$. Find the integer $c$ with $0 \le c \le 18$ such that i) $c \equiv 7a + 3b \pmod{19}$ ii) $c \equiv a^3 + 4b^3 \pmod{19}$ — 🔁 **Repeat of 2022 Q.7(a)**

---

## DM-5.5 · Modular Exponentiation

**Appearances:** 2022, 2024 · **2 of 3 OBE papers**

### Computation
- **[2022 Q.7(b) — 03]** Solve $3^{644} \bmod 645$ using a well-known algorithm. — 🔁 **Repeated verbatim in 2024 Q.8(b)**
- **[2024 Q.8(b) — 04]** Solve $3^{644} \bmod 645$ using a well-known algorithm. — 🔁 **Repeat of 2022 Q.7(b)**

---

## DM-5.6 · Fermat's Little Theorem

**Appearances:** Not examined as a standalone part — the definition is asked as the opening clause of **2022 Q.8(a) — 04**, which is filed under DM-5.7 below.

---

## DM-5.7 · Chinese Remainder Theorem

**Appearances:** 2022 · **1 of 3 OBE papers** *(2023 Q.7(c) also cross-references here — filed primary under DM-5.2)*

### Computation
- **[2022 Q.8(a) — 04]** Define Fermat's little theorem. Use the construction in the proof of the Chinese remainder theorem to find all solutions to the system of congrueness $x \equiv 2 \pmod 3$, $x \equiv 1 \pmod 4$ and $x \equiv 3 \pmod 5$. *(Note: "congrueness" printed as is)* *(also → DM-5.6)*

---

## DM-5.8 · Number Bases & Binary Arithmetic

**Appearances:** 2023 · **1 of 3 OBE papers**

### Computation
- **[2023 Q.7(b) — 03]** Add $a = (1110)_2$ and $b = (1011)_2$

---

## DM-5.9 · Number-Theoretic Proofs

**Appearances:** 2022, 2023 · **2 of 3 OBE papers** *(2023 Q.7(c) also cross-references here — filed primary under DM-5.2)*

### Computation
- **[2022 Q.7(d) — 02]** Show that $a$ and $b$ are both positive integers then $(2^a - 1) \bmod (2^b - 1) \equiv 2^{a \bmod b} - 1$. *(Note: reads "Show that [if] $a$ and $b$ are both positive integers…")*

---

# DM-6 · Introduction to Counting

## DM-6.1 · Basic Counting Techniques

**Appearances:** 2022 · **1 of 3 OBE papers** *(2023 Q.7(c) also cross-references here — filed primary under DM-5.2)*

### Computation
- **[2022 Q.8(b) — 02]** There are four major auto routes from Boston to Detroit and six from Detroit to Los Angles. How many major auto routes are there from Boston to Los Angles via Detroit? *(Note: "Los Angles" printed as is in the original)*

---

## DM-6.2 · Inclusion and Exclusion

**Appearances:** None — not examined in 2022, 2023, 2024 or CT-04.

---

## DM-6.3 · Pigeonhole Principle

**Appearances:** 2022, 2023, 2024 · **3 of 3 OBE papers**

### Theory
- **[2022 Q.8(c) — 02]** Give a real-world example of generalized pigeonhole principle. — 🔁 **Repeated verbatim in 2024 Q.8(c)**
- **[2023 Q.8(a) — 02]** Briefly describe pigeonhole principle with real world example.
- **[2024 Q.8(c) — 02]** Give a real-world example of generalized pigeonhole principle. — 🔁 **Repeat of 2022 Q.8(c)**

### Computation
- **[2022 Q.8(d) — 02]** Let $d$ be a positive integer. Show that among any group of $d+1$ (not necessarily consecutive) integers there are two with exactly the same remainder when they are divided by $d$. *(also → DM-5.9)*

---

## DM-6.4 · Permutation

**Appearances:** None — not examined in 2022, 2023, 2024 or CT-04.

---

## DM-6.5 · Combination

**Appearances:** 2023 · **1 of 3 OBE papers**

### Computation
- **[2023 Q.8(b) — 03]** A group of 30 people have been trained as astronauts to go on the first mission to mars. How many ways are there to select a crew of six people to go on this mission (assuming all crew members have the same job)?

---

## DM-6.6 · Binomial Theorem

**Appearances:** 2023 · **1 of 3 OBE papers**

### Computation
- **[2023 Q.8(c) — 04]** Briefly describe Binomial theorem and what is the co-efficient of $x^{12}y^{13}$ in the expansion of $(2x - 3y)^{25}$ ?

---

# DM-7 · Supplementary Topics

## DM-7.1 · Algorithms & Complexity  *(OFF-SYLLABUS)*

**Appearances:** 2024 · **1 of 3 OBE papers**

### Theory
- **[2024 Q.7(a) — 06]** A delivery company uses a computer system to manage customer orders. The system needs to perform the following tasks efficiently. • Sort all delivery address based on distance from warehouse. • Search for a customer's order by name or ID • Use Greedy approach to assign delivery vans to the nearest unserved address. • Evaluate the time complexity of each algorithm used. i) Which sorting algorithm would you choose to arrange delivery address efficiently? Write its name and state of average time complexity. ii) If the address list is already sorted, which search algorithm should be used? Write its pseudocode and time complexity. iii) Explain how a Greedy algorithm can be applied to assign vans to nearest delivery points.

---

## DM-7.2 · Relevance of Discrete Mathematics

**Appearances:** 2023 · **1 of 3 OBE papers**

### Theory
- **[2023 Q.8(d) — 01]** Why is discrete mathematics essential in computer science and algorithm design?

---

## Coverage Summary

| Part | Subtopics | With entries | Entries |
| :--- | :---: | :---: | :---: |
| NM-1 … NM-4 (Errors, Roots, Linear Systems, Curve Fitting) | 34 | 32 | 111 |
| NM-5 … NM-10 (Integration, Optimization, Differentiation, ODE, Eigenvalue, PDE) | 28 | 28 | 58 |
| DM-1 … DM-7 (Discrete Mathematics) | 43 | 25 | 45 |
| **Total** | **105** | **85** | **214** |

**Completeness check.** Every one of the **183 sub-questions** set across the eight papers appears in this
bank — none omitted, none invented — and every mark value matches its source paper (verified
sub-question by sub-question). Of the 214 entry lines, **195 are paper sub-questions** (183 distinct, plus
12 deliberate cross-refiled duplicates) and **19 are class-test parts**. Per-paper marks set:
96 / 96 / 96 / 96 / **97** / 80 / 80 / 80 (2021's source lists Q.7 as 2+6+5, hence 97).

Entry counts exceed 183 because of the deliberate double-filing described at the top: circuit →
Gauss-Seidel under NM-3.5 + NM-3.8; applied integration under NM-5.x + NM-5.7 + NM-5.6; PDE grids under
NM-10.2/10.3 + NM-10.4. Of the 105 subtopics, **20 carry no entry** (marked *Appearances: None* or as an
opening clause of a question filed elsewhere) — these are syllabus items never examined in any paper
from 2017 to 2024.

**Companion documents**
- [`PreviousYearAnalysisReport.md`](PreviousYearAnalysisReport.md) — trend, frequency and repeat analysis of the papers
- [`combined_analysis_report.md`](combined_analysis_report.md) — papers cross-validated against both class-note analyses
- [`topic_subtopic_list.md`](topic_subtopic_list.md) — the taxonomy, with tier ratings and self-study gap flags
