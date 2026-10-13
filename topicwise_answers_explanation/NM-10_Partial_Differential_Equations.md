---
title: "NM-10 · Partial Differential Equations"
tags:
  - numerical-methods
  - discrete-mathematics
  - topicwise-clusters
---

[🏠 Master Index](00_Index.md) | [← Prev Topic: NM-9 · Eigenvalues & Eigenvectors](NM-9_Eigenvalues_and_Eigenvectors.md) | [Next Topic: DM-3 · Propositional Logic →](DM-3_Propositional_Logic.md)

---

# NM-10 · Partial Differential Equations

> **Topic ID:** NM-10  
> **Section:** Section A -- Numerical Methods  
> **Exam Weight:** 🟡 Light (Tier 3) | 3/8 Years Examined | Typical Weight: 7–10 marks  
> **Subtopics Included:** 5 subtopics (NM-10.1 through NM-10.5)  
> **Origin Layer:** Authored in `../answers_explanation/`. All numerical results and boxed equations match character-for-character.

---

## 📑 Subtopics Covered in this Cluster

| Subtopic ID | Subtopic Title | Priority | Exam Frequency | Section Navigation |
|:---|:---|:---:|:---:|:---|
| **NM-10.1** | PDE Classification & Theory | 🟡 | 2020 | [Jump to NM-10.1](#nm-101) |
| **NM-10.2** | Laplace Equation | 🟡 | 2018, 2019, 2020 | [Jump to NM-10.2](#nm-102) |
| **NM-10.3** | Poisson Equation | 🟡 | 2021 | [Jump to NM-10.3](#nm-103) |
| **NM-10.4** | Liebmann's Iterative Method | 🟡 | 2018, 2020 | [Jump to NM-10.4](#nm-104) |
| **NM-10.5** | Boundary Conditions in PDEs | 🟡 | 2024 | [Jump to NM-10.5](#nm-105) |

---

<a id="nm-101"></a><a id="nm-10.1"></a>
## NM-10.1 · PDE Classification & Theory

### [2020 Q.8(a)]

**Question.** Write 4 types of partial differential equations. Discuss briefly the solving process of any of the equations using numerical iterative technique.

*[Marks: 06]*

**Solution.**

**The four canonical types.** A second-order linear PDE in two variables
$A u_{xx} + B u_{xy} + C u_{yy} = f$ is classified by the sign of
$B^2 - 4AC$.

| Type | Discriminant | Form | Physical examples |
| :-- | :-- | :-- | :-- |
| **Elliptic** | $B^2 - 4AC < 0$ | $u_{xx} + u_{yy} = f$ | Steady-state heat conduction, electrostatics, potential flow, torsion |
| **Parabolic** | $B^2 - 4AC = 0$ | $u_t = \alpha u_{xx}$ | Transient heat conduction, diffusion, convection-dominated transport |
| **Hyperbolic** | $B^2 - 4AC > 0$ | $u_{tt} = c^2 u_{xx}$ | Wave equation, vibrating string, transmission lines, shallow water |
| **Mixed or general** | all three nonzero | $Au_{xx} + Bu_{xy} + Cu_{yy} = f$ | General second-order form, e.g. some fluid and structural problems |

$$\boxed{\text{Laplace, Poisson, wave, heat; the elliptic pair is solved by repeated averaging of the four neighbours}}$$

**The classification is not cosmetic.** It decides the boundary conditions, the
numerical method, and whether a well-posed problem exists at all.

| | Elliptic | Parabolic | Hyperbolic |
| :-- | :-- | :-- | :-- |
| Boundary conditions | **All** around the boundary | Along the inflow boundary only, plus an initial condition | Along two incoming characteristics |
| Prescribes | A steady state | How a state evolves | How a disturbance travels |
| Information direction | None, elliptic influence is instant | Forward in time | Along characteristic curves |
| Well posed with | Dirichlet, Neumann or mixed data | Initial plus inflow data | Initial plus inflow data |

> [!warning] An elliptic problem with only initial conditions is not well posed
> For the heat equation the initial condition is essential: it says where the
> system starts. For Laplace's equation there is no time and no initial
> condition, because there is no time. All the information arrives through the
> boundary.
>
> This is why every elliptic formula below is built from the boundary values
> alone. Q.8(b) uses four boundary values to determine four interior values, and
> no amount of iteration invents information that was not in the data.

**Solving the elliptic equation by an iterative technique.** For
$u_{xx} + u_{yy} = f$ with equal spacing $h$, the five-point stencil is

$$
u_{i,j} = \frac{1}{4}\left(u_{i-1,j} + u_{i+1,j} + u_{i,j-1} + u_{i,j+1} + h^2 f_{i,j}\right)
$$

each interior value being the average of its four neighbours plus a source term.

**The general iterative scheme.** Write the system as $A\mathbf{u} = \mathbf{b}$ and
split $A = D - (L + U)$, where $D$ is the diagonal and $L + U$ the rest. Then

$$
\mathbf{u}^{(k+1)} = D^{-1}\left[\mathbf{b} + (L + U)\mathbf{u}^{(k)}\right] = G\mathbf{u}^{(k)} + \mathbf{c}
$$

and iterate until the change falls below a tolerance. Three variants differ only
in which values $G$ uses:

| Method | Uses | Convergence for elliptic problems |
| :-- | :-- | :-- |
| **Jacobi** | the whole previous iterate | Slow; needs many sweeps |
| **Gauss-Seidel** | the newest values available | Faster; usually the default |
| **SOR** | newest values plus a relaxation factor $\omega$ | Fastest; the standard choice for large grids |

**Convergence.** Gauss-Seidel converges when the matrix is strictly diagonally
dominant, and the five-point Laplacian stencil is diagonally dominant by
construction: the centre entry is $4$ and the off-diagonal sum is $1+1+1+1 = 4$,
with strict dominance wherever a boundary node removes a neighbour. That is why
Liebmann's method, which is Gauss-Seidel on this stencil, always converges for
the problem in Q.8(b).

> [!note] Why relaxation speeds it up, and the number to remember
> Plain Gauss-Seidel corresponds to $\omega = 1$. The optimal relaxation factor for
> a square grid is
> $$\omega = \frac{2}{1 + \sin\frac{\pi}{n+1}} \approx 2 - \frac{2\pi}{n}$$
> which tends to $2$ as the grid grows, and is about $1.94$ for $n = 30$.
>
> $\omega = 1$ under-relaxes in effect and $\omega > 2$ diverges outright. The
> practical gain from a well-chosen $\omega$ is roughly a factor of two in sweep
> count, which is why every serious elliptic solver has one.

---

<a id="nm-102"></a><a id="nm-10.2"></a>
## NM-10.2 · Laplace Equation

### [2018 Q.8(a), 2020 Q.8(b)]

**Appeared in:** 2018 Q.8(a), 2020 Q.8(b)

**Question.** Find the potential distribution at the interior nodes using Leibmann's method.

*[Marks: 06]*

**Solution.**

**The mesh.**

![Square domain 3x3 finite-difference boundary value grid with boundary potentials Top=100V, Bottom=0V, Left=75V, Right=50V with insulating gap corners, and interior nodes 1, 2, 3, 4](../answers_exam_style/diagrams/2018_Q8a_liebmann_grid.jpg)

**The governing equation.** With no charge or source inside the region, the
potential satisfies Laplace's equation, whose five-point finite-difference form
on a uniform square mesh is

$$u_{i,j} = \frac{1}{4}\left(u_{i+1,j} + u_{i-1,j} + u_{i,j+1} + u_{i,j-1}\right)$$

Four neighbours, four weights, all $1/4$. That symmetry is why this is called
the five-point stencil: the centre plus its four edge neighbours.

**Leibmann's method is Gauss-Seidel on this system.** Update each node from the
most recent values of its neighbours, as soon as those are available, rather
than from the previous sweep.

**The four node equations.** This is where the question is won or lost. Read
each node's four neighbours off the diagram, boundary values included:

$$V_1 = \frac{100 + V_2 + 75 + V_3}{4} = \frac{175 + V_2 + V_3}{4}$$

$$V_2 = \frac{100 + 50 + V_1 + V_4}{4} = \frac{150 + V_1 + V_4}{4}$$

$$V_3 = \frac{75 + V_4 + V_1 + 0}{4} = \frac{75 + V_1 + V_4}{4}$$

$$V_4 = \frac{V_3 + 50 + V_2 + 0}{4} = \frac{50 + V_2 + V_3}{4}$$

As a $4\times4$ system,

$$\begin{bmatrix} 4 & -1 & -1 & 0 \\ -1 & 4 & 0 & -1 \\ -1 & 0 & 4 & -1 \\ 0 & -1 & -1 & 4 \end{bmatrix}\begin{bmatrix} V_1 \\ V_2 \\ V_3 \\ V_4 \end{bmatrix} = \begin{bmatrix} 175 \\ 150 \\ 75 \\ 50 \end{bmatrix}$$

> [!warning] Counting off-diagonal entries catches a wrong neighbour
> Look at the matrix before you look at the answer. Each row of a five-point
> stencil row has one diagonal and **exactly two** off-diagonal entries. Here
> rows 1 to 4 carry $-1$ in columns two and three, two and four, one and four,
> and two and three respectively: two each. If you find three $-1$s in a row,
> you have put a diagonal neighbour in where an off-diagonal one belongs.
>
> A second test is to add all four equations. Every interior neighbour appears
> once with $+1$ and once with $-1$, so the interior terms cancel and what
> remains is $2(V_1+V_2+V_3+V_4) = 175 + 150 + 75 + 50 = 450$, giving
> $V_1+V_2+V_3+V_4 = 225$. The stated answer gives
> $71.875 + 65.625 + 46.875 + 40.625 = 225$ exactly, so the neighbour sets are
> mutually consistent. One line, and it catches a transposed pair of neighbours
> immediately.

**Leibmann iteration.** Starting from $V_1 = V_2 = V_3 = V_4 = 0$, and
updating in the order $1, 2, 3, 4$ so each node uses the freshest neighbours
available:

| Sweep | $V_1$ | $V_2$ | $V_3$ | $V_4$ |
| :--: | :--: | :--: | :--: | :--: |
| 1 | 43.750000 | 48.437500 | 29.687500 | 32.031250 |
| 2 | 63.281250 | 61.328125 | 42.578125 | 38.476562 |
| 3 | 69.726562 | 64.550781 | 45.800781 | 40.087891 |
| 4 | 71.337891 | 65.356445 | 46.606445 | 40.490723 |
| 5 | 71.740723 | 65.557861 | 46.807861 | 40.591431 |
| 6 | 71.841431 | 65.608215 | 46.858215 | 40.616608 |

**The solution.** The iteration converges, and solving the $4\times4$ system
directly gives

$$V_1 = \frac{575}{8} = 71.875, \qquad V_2 = \frac{525}{8} = 65.625$$

$$V_3 = \frac{375}{8} = 46.875, \qquad V_4 = \frac{325}{8} = 40.625$$

$$\boxed{V_1 = 71.875\ \text{V}, \quad V_2 = 65.625\ \text{V}, \quad V_3 = 46.875\ \text{V}, \quad V_4 = 40.625\ \text{V}}$$

> [!info] Checking by substitution, and what the fractions tell you
> Substitute back into the four stencil equations:
> $\dfrac{1}{4}(175 + 65.625 + 46.875) = \dfrac{287.5}{4} = 71.875$;
> $\dfrac{1}{4}(150 + 71.875 + 40.625) = \dfrac{262.5}{4} = 65.625$;
> $\dfrac{1}{4}(75 + 71.875 + 40.625) = \dfrac{187.5}{4} = 46.875$;
> $\dfrac{1}{4}(50 + 65.625 + 46.875) = \dfrac{162.5}{4} = 40.625$. All four hold
> exactly.
>
> The answer coming out as multiples of $\tfrac18$ is itself informative. The
> boundary data are multiples of $25$, and one sweep of the averaging process
> can only produce multiples of $\tfrac14$, so a multiple of $\tfrac18$ at the
> fixed point is a sign that the system is self-consistent. A wrong neighbour
> would leave a residual of order a tenth rather than zero, and the values
> would not settle on tidy fractions.
>
> On the convergence itself: all four nodes approach their limits from below,
> which is what a Gauss-Seidel start at the origin gives when every
> right-hand side is positive. The increments in $V_1$ over the first six sweeps
> are $43.7500$, $19.5313$, $6.4453$, $1.6113$, $0.4028$ and $0.1007$, so after
> the first sweep each increment is a fixed fraction, about one quarter, of the
> one before. That factor of four per sweep is the signature of a spectral
> radius near $0.25$. Six sweeps leave $V_1$ within $0.034$ V of its limit, so
> more sweeps would be needed for four-figure agreement; that is the honest
> reason an exact elimination is reported alongside the iteration.

---

### [2019 Q.8(b)]

**Question.** Solve the Laplace's equation for the square region shown in the following figure, the boundary values being indicated in the figure.

*[Marks: 06]*

**Solution.**

**The mesh.** A uniform $3\times3$ mesh over the square, with four interior nodes
$u_1, u_2, u_3, u_4$ and the boundary values shown.

![Finite difference mesh for Laplace equation over square domain OCBA with boundary values and interior nodes u1, u2, u3, u4](../answers_exam_style/diagrams/2019_Q8b_laplace_grid.jpg)

**The standard Laplace finite-difference stencil.** For a square mesh with uniform
spacing $h$, $\nabla^2 u = 0$ gives

$$\frac{u_{i+1,j} - 2u_{i,j} + u_{i-1,j}}{h^2} + \frac{u_{i,j+1} - 2u_{i,j} + u_{i,j-1}}{h^2} = 0$$

and cancelling $h^2$:

$$u_{i,j} = \frac{1}{4}\left(u_{i+1,j} + u_{i-1,j} + u_{i,j+1} + u_{i,j-1}\right)$$

**The four nodal equations.** Reading the neighbours of each interior node from the
figure, and taking the boundary values in the order left, right, top, bottom:

$$u_1 = \frac{1}{4}\left(u_2 + u_3 + 4 + 2\right)$$

$$4u_1 - u_2 - u_3 = 6$$

$$u_2 = \frac{1}{4}\left(u_1 + u_4 + 5 + 5\right)$$

$$4u_2 - u_1 - u_4 = 10$$

$$u_3 = \frac{1}{4}\left(u_1 + u_4 + 1 + 1\right)$$

$$4u_3 - u_1 - u_4 = 2$$

$$u_4 = \frac{1}{4}\left(u_3 + u_2 + 2 + 4\right)$$

$$4u_4 - u_3 - u_2 = 6$$

> [!warning] This is the step the figure exists for
> Each interior node has **exactly two interior neighbours** and **exactly two
> boundary neighbours**. Writing the equations correctly means identifying which is
> which from the mesh, and the two are easy to swap because the node is diagonally
> opposite to its boundary neighbour.
>
> Two checks catch the swap immediately:
>
> 1. **Count the entries.** Each equation has one diagonal coefficient $4$ and
>    **two** off-diagonal $-1$. A row with three off-diagonal entries is not a
>    five-point stencil equation and cannot be right.
> 2. **Add all four equations.** Every column then sums to $2$, because each node is
>    an interior neighbour of exactly two others. Getting $2(u_1+u_2+u_3+u_4) = 24$
>    confirms the four equations are mutually consistent; a mislabelled neighbour
>    breaks the cancellation immediately.

**Solve the $4\times4$ system.**

$$4u_1 - u_2 - u_3 = 6$$
$$-u_1 + 4u_2 - u_4 = 10$$
$$-u_1 + 4u_3 - u_4 = 2$$
$$-u_3 - u_2 + 4u_4 = 6$$

Writing this as a matrix,

$$\begin{bmatrix} 4 & -1 & -1 & 0 \\ -1 & 4 & 0 & -1 \\ -1 & 0 & 4 & -1 \\ 0 & -1 & -1 & 4 \end{bmatrix} \begin{bmatrix} u_1 \\ u_2 \\ u_3 \\ u_4 \end{bmatrix} = \begin{bmatrix} 6 \\ 10 \\ 2 \\ 6 \end{bmatrix}$$

**Step 1. One relation from subtracting.** Equation 3 minus equation 2 cancels both
$u_1$ and $u_4$:

$$4u_3 - 4u_2 = -8 \implies u_3 = u_2 - 2$$

**Step 2. One relation from adding.** Adding all four, every column sums to $2$:

$$2(u_1 + u_2 + u_3 + u_4) = 24 \implies u_1 + u_2 + u_3 + u_4 = 12$$

**Step 3. Substitute $u_3 = u_2 - 2$** into that sum:

$$u_1 + 2u_2 + u_4 = 14, \quad u_4 = 14 - u_1 - 2u_2$$

**Step 4. Use equation 2.** Substituting that $u_4$ into $-u_1 + 4u_2 - u_4 = 10$:

$$-u_1 + 4u_2 - 14 + u_1 + 2u_2 = 10 \implies 6u_2 = 24 \implies u_2 = 4$$

Here $u_3 = 2$ and $u_4 = 6 - u_1$. Equation 1 then gives
$4u_1 - 4 - 2 = 6$, hence $u_1 = 3$ and $u_4 = 3$.

$$\boxed{u_1 = 3, \qquad u_2 = 4, \qquad u_3 = 2, \qquad u_4 = 3}$$

> [!info] Check against the individual nodal equations
> Substituting into the four nodal equations directly:
> $4(3) - 4 - 2 = 6$ ✓; $-(3) + 4(4) - 3 = 10$ ✓;
> $-(3) + 4(2) - 3 = 2$ ✓; $-(2) - 4 + 4(3) = 6$ ✓. All four hold exactly.
> The values also insert into the difference form consistently,
> $u_1 = \tfrac{1}{4}(2 + 4 + 4 + 2) = 3$ and
> $u_3 = \tfrac{1}{4}(1 + 1 + 3 + 3) = 2$, in each case the mean of the four
> neighbours as the Laplace stencil requires. That the solution is a set of small
> integers when the boundary data are also integers is a property of this
> particular mesh, and it is itself a strong check.

> [!note] Why small integers are the expected answer here, and why that is a check
> With integer boundary data and a small mesh, the exact solution of the
> five-point system is a rational with denominator equal to the determinant of the
> matrix. Here that determinant is $192$, and $\operatorname{adj}(A)b = [576, 768, 384, 576]^T$,
> so dividing by $192$ gives $[3, 4, 2, 3]^T$, making every entry an exact integer.
>
> **So the integrality is a property of this particular mesh and boundary data, not a general structural fact.** It
> is still a useful one, because a wrong neighbour almost never produces integers.
> The same boundary data with one neighbour transposed gives a non-integer vector with denominator $192$,
> which is the visible signature of the error this question is designed to catch.

> [!warning] Where this meets Q.3(c)
> The two-node Gauss-Seidel system there is the same construction two unknowns
> smaller, and the same two checks apply: count the off-diagonal entries per row,
> and check that adding the equations produces the symmetric cancellation.
>
> The one difference is that Q.3(c) used an **iterative** method and this one uses
> direct elimination. The answer script for Q.3(c) shows both, because the question
> asked for two Gauss-Seidel iterations and the exact values are worth having as the
> target they are converging toward. Both routes agree, and saying so is what makes
> the iteration table trustworthy.

---

<a id="nm-103"></a><a id="nm-10.3"></a>
## NM-10.3 · Poisson Equation

### [2021 Q.6(c)]

**Question.** Solve the Poisson equation $U_{xx} + U_{yy} = -10(x^2 + y^2 + 10)$ in the domain of the given figure.

*[Marks: 05, CO: 2]*

**Solution.**

![Square domain 3 by 3 finite difference grid for the Poisson equation with u=0 on all four sides, x and y from 0 to 3, and four interior nodes u1, u2, u3, u4](../answers_exam_style/diagrams/2021_Q6c_poisson_grid.jpg)
*Figure 2021 Q6(c): square domain finite-difference grid with Dirichlet boundary conditions for Poisson's equation (Source: Page 2, Q6(c))*

**Step 1. The grid.** The domain is $0 \le x \le 3$, $0 \le y \le 3$ with
$h = k = 1$. Here $u = 0$ on all four sides. Four interior nodes:

| Node | Location |
| :-- | :-- |
| $u_1$ | $(1, 1)$ |
| $u_2$ | $(2, 1)$ |
| $u_3$ | $(1, 2)$ |
| $u_4$ | $(2, 2)$ |

**Step 2. The five-point formula.** With $h = k = 1$,

$$
u_{i+1,j} + u_{i-1,j} + u_{i,j+1} + u_{i,j-1} - 4u_{i,j} = -10(x_i^2 + y_j^2 + 10)
$$

> [!note] Read the coefficient of $u_{ij}$ off the figure, not off memory
> $u_{i+1,j} + u_{i-1,j} - 2u_{ij}$ approximates $h^2 U_{xx}$ and
> $u_{i,j+1} + u_{i,j-1} - 2u_{ij}$ approximates $k^2 U_{yy}$. Adding them and
> dividing by $h^2$ gives a coefficient of $-4$ on $u_{ij}$ when $h = k = 1$.
>
> The five-point stencil is the whole method. Everything after this is bookkeeping.

**Step 3. Write one equation per interior node.** All boundary values are zero, so
those terms drop out.

At $u_1(1,1)$: $-10(1 + 1 + 10) = -120$

$$
u_2 + 0 + u_3 + 0 - 4u_1 = -120 \Rightarrow -4u_1 + u_2 + u_3 = -120
$$

At $u_2(2,1)$: $-10(4 + 1 + 10) = -150$

$$
0 + u_1 + u_4 + 0 - 4u_2 = -150 \Rightarrow u_1 - 4u_2 + u_4 = -150
$$

At $u_3(1,2)$: $-10(1 + 4 + 10) = -150$

$$
u_4 + 0 + 0 + u_1 - 4u_3 = -150 \Rightarrow u_1 - 4u_3 + u_4 = -150
$$

At $u_4(2,2)$: $-10(4 + 4 + 10) = -180$

$$
0 + u_3 + 0 + u_2 - 4u_4 = -180 \Rightarrow u_2 + u_3 - 4u_4 = -180
$$

**Step 4. The system.**

$$
\begin{bmatrix}
-4 & 1 & 1 & 0 \\
1 & -4 & 0 & 1 \\
1 & 0 & -4 & 1 \\
0 & 1 & 1 & -4
\end{bmatrix}
\begin{bmatrix} u_1 \\ u_2 \\ u_3 \\ u_4 \end{bmatrix}
= \begin{bmatrix} -120 \\ -150 \\ -150 \\ -180 \end{bmatrix}
$$

**Step 5. Exploit symmetry, then solve.** The domain and the source
$-10(x^2+y^2+10)$ are symmetric under $x \leftrightarrow y$, and $(2,1)$ maps to
$(1,2)$, so $u_2 = u_3$. Let $u_2 = u_3 = w$. Then

$$
\begin{cases}
-4u_1 + 2w = -120 \\
u_1 - 4w + u_4 = -150 \\
2w - 4u_4 = -180
\end{cases}
$$

From the first, $u_1 = \frac{2w + 120}{4} = \frac{w}{2} + 30$. From the third,
$u_4 = \frac{2w + 180}{4} = \frac{w}{2} + 45$. Substituting into the second,

$$
\frac{w}{2} + 30 - 4w + \frac{w}{2} + 45 = -150 \Rightarrow -3w + 75 = -150 \Rightarrow w = 75
$$

Then $u_1 = 37.5 + 30 = 67.5$ and $u_4 = 37.5 + 45 = 82.5$.

$$\boxed{u_1 = 67.5, \quad u_2 = 75, \quad u_3 = 75, \quad u_4 = 82.5}$$

**Step 6. Verify.** Substituting back:

$$
-4(67.5) + 75 + 75 = -270 + 150 = -120 \quad \checkmark
$$

$$
67.5 - 4(75) + 82.5 = 150 - 300 = -150 \quad \checkmark
$$

$$
67.5 - 4(75) + 82.5 = -150 \quad \checkmark
$$

$$
75 + 75 - 4(82.5) = 150 - 330 = -180 \quad \checkmark
$$

> [!info] Check
> The symmetry argument was confirmed by solving the full 4 by 4 system directly
> with exact rational arithmetic: it returns $(67.5, 75, 75, 82.5)$ and gives
> $u_2 = u_3$ without being told to. All four residuals are exactly zero.
>
> A second structural check: the matrix is symmetric and diagonally dominant, so it
> is a positive-definite M-matrix and the solution is unique. The pattern
> $u_1 < u_2 = u_3 < u_4$ matches the source term, since
> $x^2+y^2+10$ is smallest at $(1,1)$ and largest at $(2,2)$, and the negative
> source means the largest magnitude of $u$ must occur where the source is most
> negative, that is at $(2,2)$. Correct.

> [!warning] Symmetry is an optimisation, never an assumption
> Using $u_2 = u_3$ cut a $4 \times 4$ system to three equations. But it is only
> legitimate because the **source and the boundary data are both** symmetric under
> $x \leftrightarrow y$.
>
> If the source had been $-10(x^2 + 2y^2 + 10)$, or if the right-hand boundary had
> been non-zero, the symmetry would break and $u_2 = u_3$ would be a guess that
> silently returns a wrong answer. State the symmetry you are using and check that
> it is there.

> [!note] There is no polynomial exact solution for these boundary data
> It is tempting to look for a closed form. Try
> $U = ax^4 + bx^2y^2 + cy^4 + dx^2 + ey^2 + f$. Then
> $U_{xx} + U_{yy} = (12a+2b)x^2 + (2b+12c)y^2 + (2d+2e)$, and matching
> $-10(x^2+y^2+10)$ requires
> $$12a+2b=-10, \quad 2b+12c=-10, \quad 2d+2e=-100$$
> The condition $u = 0$ on $x = 0$ for all $y$ forces $c = e = f = 0$, and $u = 0$
> on $y = 0$ forces $a = d = f = 0$. Then the constant equation reads $0 = -100$, a
> contradiction. **No quartic satisfies both the PDE and these boundary values**, so
> the finite difference solution above is the answer and there is nothing to check
> it against.
>
> That is normal rather than disappointing. A polynomial can satisfy a PDE with
> compatible boundary data, but $u = 0$ on all four sides of a source that is
> everywhere negative is not compatible data.

---

<a id="nm-104"></a><a id="nm-10.4"></a>
## NM-10.4 · Liebmann's Iterative Method

---

**Every question that reaches this subtopic is written in the subtopic it is filed under.** Nothing is answered here, and that is deliberate rather than an omission: the subtopic holds the questions in the taxonomy but owns no block of its own.

- *2018 Q.8(a)* is the same question as [[NM-10.2_Laplace_Equation|NM-10.2]], which is written in `NM-10.2`.
- *2020 Q.8(b)* is the same question as [[NM-10.2_Laplace_Equation|NM-10.2]], which is written in `NM-10.2`.

---

<a id="nm-105"></a><a id="nm-10.5"></a>
## NM-10.5 · Boundary Conditions in PDEs

### [2024 Q.4(c)]

**Question.** State the importance of boundary conditions in solving PDEs numerically.

*[Marks: 02, CO: 1]*

**Solution.**

A partial differential equation on its own has infinitely many solutions. The
boundary conditions are what select one, and this is why they are not an
optional addition to the problem but part of its statement.

**What they do, concretely.** For a problem discretised on a mesh, the boundary
conditions do three jobs:

1. **They fix the unknowns.** A mesh with $N$ interior nodes gives $N$ equations
   from the PDE. The boundary values supply the known terms those equations
   need. Without them the system is under-determined and does not have a unique
   answer.
2. **They make the solution physical.** The Laplace equation $u_{xx} + u_{yy} = 0$
   is satisfied by $u = 0$ and by $u = 100x^3 - 3xy^2$ and by infinitely many
   others. Specifying the potential on the four edges selects the one that
   describes the actual apparatus.
3. **They determine the character of the discretisation.** Whether the boundary
   nodes take part in the difference equations, or are already known, decides
   whether the system is square.

**The two kinds, and why they behave differently.**

| Kind | What is given | Behaviour |
| :-- | :-- | :-- |
| Dirichlet | the value of $u$ itself on the boundary | the boundary nodes are eliminated, the system shrinks |
| Neumann | the normal derivative $\partial u/\partial n$ | a ghost row or one-sided difference is needed, the system grows |

For a Neumann condition the derivative is unknown in terms of nodal values, so
one-sided differences are used, and this is where extra discretisation error
enters. Getting the boundary condition *kind* right is therefore as important as
getting the interior discretisation right.

**Why this matters practically.** Most of the numerical difficulty in a PDE
problem is at the boundary, not in the interior. The interior stencil is uniform
and its error is a clean $O(h^2)$. The boundary treatment is where the order can
drop, where the system can become ill-conditioned, and where the physics of the
problem is actually encoded. A mesh refinement study that improves slowly is
almost always showing boundary error, not interior error.

$$\boxed{\text{PDE} + \text{boundary conditions} = \text{a problem with one unique numerical solution}}$$

The PDE on its own has a whole family of solutions. The boundary conditions are
what select one of them, and they do it by fixing both the solution and the size
of the algebraic system that the discretisation produces, since only the interior
nodes become unknowns.

---

[🏠 Master Index](00_Index.md) | [← Prev Topic: NM-9 · Eigenvalues & Eigenvectors](NM-9_Eigenvalues_and_Eigenvectors.md) | [Next Topic: DM-3 · Propositional Logic →](DM-3_Propositional_Logic.md)
