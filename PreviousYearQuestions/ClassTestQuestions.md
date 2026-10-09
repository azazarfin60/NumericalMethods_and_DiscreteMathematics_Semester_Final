---
course_code: ECE 2213
course_title: Numerical Methods & Discrete Mathematics
document_type: Class Test Questions
tags:
  - class-tests
  - ece2213
  - numerical-methods
  - discrete-mathematics
---

# Department of Electrical & Computer Engineering
### Rajshahi University of Engineering & Technology (RUET)
**Course Code:** ECE 2213  
**Course Title:** Numerical Methods & Discrete Mathematics  
**Document:** Class Test (CT) Question Collection

---

## Navigation & Overview

- [Class Test 01](#class-test-01) — *Modeling, Truncation & Round-off Errors, Bisection & Regula Falsi Methods*
- [Class Test 02 (Set A)](#class-test-02-set-a) — *Lagrange & Newton's (Forward/Backward) Interpolation*
- [Class Test 02 (Set B)](#class-test-02-set-b) — *Gauss-Seidel Iteration & Runge-Kutta Methods (RK2, RK4)*
- [Class Test 04](#class-test-04) — *Propositional Logic, Tautology, Logical Equivalence & Embedded System Requirements*

---

## Class Test 01

| Parameter | Details |
| :--- | :--- |
| **Course Code** | ECE 2213 |
| **Course Title** | Numerical Methods & Discrete Mathematics |
| **Marks** | 20 |
| **Time** | 20 minutes |

---

### Question 01

An engineering company is developing software to estimate the temperature distribution inside a newly designed reactor. Due to limited computational resources, the embedded computer stores floating-point numbers with only 5 significant decimal digits. The software estimates the exponential function using the first four non-zero terms of the Taylor series. After several simulations, the software predicts a safe operating temperature, but experimental measurements differ significantly.

**Marks:** 10 &emsp; | &emsp; **CO:** CO1

- **(a)** Develop a mathematical model representing the temperature estimation problem and identify the assumptions made.
- **(b)** Identify at least three possible sources of numerical error in the software and explain how each affects the final prediction.

*(Note: Corrected from typographical numbering `(vii)` and `(viii)` on the original question script).*

---

### Question 02

A chemical plant uses a computerized system to find the operating temperature where the reaction pressure becomes zero, modeled by a continuous nonlinear equation $f(T) = 0$. The engineers must choose between the Bisection Method and the Regula Falsi Method.

**Marks:** 10 &emsp; | &emsp; **CO:** CO1

- **(a)** Compare the Bisection Method and Regula Falsi Method in terms of the required condition for application, convergence behavior, and suitability for a safety-critical system.
- **(b)** During testing, the Regula Falsi Method repeatedly updates only one endpoint of the interval, leading to slow convergence. Explain why this happens, compare it with the Bisection Method, and suggest a suitable improvement.

*(Note: Corrected from typographical labeling `(g)` and `(h)` on the original question script).*

---

## Class Test 02 (Set A)

| Parameter | Details |
| :--- | :--- |
| **Course Code** | ECE-2213 |
| **Test Title** | CT 02 |
| **Time** | 25 Minutes |

---

### Question 1

An environmental scientist measures the concentration of a pollutant in a river at different distances from the source.

| Distance (km) | 2 | 4 | 7 | 10 |
| :--- | :---: | :---: | :---: | :---: |
| **Concentration (mg/L)** | 18 | 26 | 43 | 60 |

The concentration at $5\text{ km}$ could not be measured due to equipment failure. Use the Lagrange Interpolation Formula to estimate the pollutant concentration at $5\text{ km}$.

---

### Question 2

A weather station records the temperature every 2 hours.

| Time (hours) | 0 | 2 | 4 | 6 | 8 |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Temperature (°C)** | 24 | 27 | 31 | 36 | 42 |

The meteorologist wants to estimate the temperature at $1.5$ and $7$ hours. Use Newton's (Forward/Backward) Interpolation Formula to estimate the temperature.

---

## Class Test 02 (Set B)

**Department of Electrical & Computer Engineering**

| Parameter | Details |
| :--- | :--- |
| **Course Code** | ECE 2213 |
| **Test Title** | CT#02 |
| **Total Marks** | 20 |
| **Time** | 40 Minutes |

---

### Question 1

Consider the following system of linear equations:

$$
\begin{aligned}
4x + y + z &= 7 \\
x + 5y + 2z &= -8 \\
2x + y + 6z &= 6
\end{aligned}
$$

*(Note: In the second equation, $x$ is printed as uppercase $X$ in the original script: $X + 5y + 2z = -8$)*

- **(a)** Rearrange the equations in a suitable form for the Gauss-Seidel iterative method.
- **(b)** Starting with $x_0 = 0$, $y_0 = 0$, $z_0 = 0$, perform four complete iterations using the Gauss-Seidel method.
- **(c)** Calculate the absolute error in $x$, $y$, and $z$ between the third and fourth iterations.

---

### Question 2

Consider the initial value problem:

$$
\frac{dy}{dx} = x^2 - y, \quad y(0) = 1
$$

- **(a)** Using RK2 method with step size $h = 0.2$, calculate $y(0.2)$ and $y(0.4)$. Show both the predictor and corrector calculations at each step.
- **(b)** Using the RK4 method calculate $y(0.2)$, also compare result with RK2 method.

---

## Class Test 04

**Department of Electrical & Computer Engineering**

| Parameter | Details |
| :--- | :--- |
| **Course Code** | ECE 2213 |
| **Test Title** | CT#04 |
| **Total Marks** | 20 |
| **Time** | 30 Minutes |

---

### Question 1

Let $p$, $q$, and $r$ be propositions. Using a complete truth table, establish that the following compound proposition is a tautology:

$$
[(p \to q) \land (q \to r)] \to (p \to r)
$$

**Marks:** 6

---

### Question 2

A university online examination system is described by the following requirement:

> *"A student can start the examination if and only if the student is authenticated and the examination server is available."*

Let:
- $p$: The student is authenticated.
- $q$: The examination server is available.
- $r$: The student can start the examination.

**Marks:** 7

- **(a)** Translate the requirement into propositional logic.
- **(b)** Rewrite the resulting expression using only $\neg$, $\lor$, and $\land$.
- **(c)** Construct a truth table for the resulting expression.

---

### Question 3

Consider the following three statements describing an embedded system:

- If the sensor is active, then the controller receives data.
- The controller does not receive data unless the sensor is active.
- The sensor is active if and only if the controller receives data.

Let:
- $p$: The sensor is active.
- $q$: The controller receives data.

**Marks:** 7 *(Printed as 6 on original script; Total marks: 20)*

- **(a)** Translate all three statements into propositional logic.
- **(b)** Form a single compound proposition by taking the conjunction of the three requirements.
- **(c)** Construct the complete truth table from **(b)**.
- **(d)** Establish the truth assignments that satisfy all three requirements simultaneously.
