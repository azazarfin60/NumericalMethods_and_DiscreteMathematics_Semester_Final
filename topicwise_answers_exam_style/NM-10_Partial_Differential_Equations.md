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
> **Origin Layer:** Authored in `../answers_exam_style/`. All numerical results and boxed equations match character-for-character.

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

**Solution.**

A partial differential equation involves partial derivatives with respect to two
or more independent variables. The four classical types depend on the order of
the highest derivatives.

**1. Laplace equation.** No time or reaction term, steady state.

$$\frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} = 0$$

Physical meaning: steady-state heat conduction, electrostatics, incompressible
irrotational flow, torsional rigidity. Boundaries are prescribed values of $u$
on the edges of a region. Solved by Q.8(b) of this paper.

**2. Poisson equation.** Laplace with a source term.

$$\nabla^2 u = -f(x,y)$$

Physical meaning: steady heat conduction with internal heat generation,
electrostatics with a charge density, potential flow with sources. Same boundary
condition type as Laplace. Solved by 2021 Q.6(c).

**3. Wave equation.** Time-dependent, second order in both space and time.

$$\frac{\partial^2 u}{\partial t^2} = c^2\nabla^2 u$$

Physical meaning: vibrating string, sound in air, water waves, electromagnetic
waves. $c$ is the wave speed. Needs an **initial condition** $u(x,0) = f(x)$,
$\frac{\partial u}{\partial t}(x,0) = g(x)$, plus boundary conditions.

**4. Heat equation, or diffusion equation.** Time-dependent, second order in
space, first order in time.

$$\frac{\partial u}{\partial t} = \alpha\nabla^2 u$$

Physical meaning: heat conduction in a solid, diffusion of a solute, spread of an
epidemic. $\alpha = \frac{k}{\rho c}$ is the thermal diffusivity. Needs an
initial condition $u(x,y,0) = f(x,y)$ plus boundary conditions.

**The deciding test.** For a linear second-order PDE
$A u_{xx} + 2B u_{xy} + C u_{yy} + \cdots = 0$, compute the discriminant
$B^2 - AC$:

| Sign of $B^2 - AC$ | Type | Example |
| :-- | :-- | :-- |
| $< 0$ | **Elliptic** | Laplace, Poisson |
| $= 0$ | **Parabolic** | Heat equation |
| $> 0$ | **Hyperbolic** | Wave equation |

**The solved example: the heat equation by an iterative numerical technique.**

$$\frac{\partial u}{\partial t} = \alpha\left(\frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2}\right)$$

**Step 1. Discretise the grid.** Divide the region into a mesh of spacing $h$ in
space and $\Delta t$ in time. The stability condition is the key practical
result:

$$\alpha \frac{\Delta t}{h^2} \le \frac{1}{4} \qquad \text{in two dimensions}$$

**Step 2. Replace the second derivative by its central difference.**

$$\frac{u^{n+1}_{i,j} - u^n_{i,j}}{\Delta t} = \alpha \frac{u^n_{i+1,j} - 2u^n_{i,j} + u^n_{i-1,j}}{h^2}$$

**Step 3. Rearrange into the update formula** with
$\lambda = \frac{\alpha \Delta t}{h^2}$:

$$u^{n+1}_{i,j} = \lambda u^n_{i+1,j} + \lambda u^n_{i-1,j} + \lambda u^n_{i,j+1} + \lambda u^n_{i,j-1} + (1 - 4\lambda)u^n_{i,j}$$

Each new value is a **weighted average of the four neighbours plus the old
centre**. The weights are all non-negative as long as
$\lambda \le \frac{1}{4}$, which is the stability condition.

**Step 4. The explicit scheme above is one choice.** The two alternatives are
the **implicit (backward Euler)** scheme, which writes the same update at time
$n+1$ instead of $n$ and is unconditionally stable but needs a linear solve each
step, and the **Crank-Nicolson** scheme, which averages the explicit and implicit
forms and is second order in time while still unconditionally stable.

**Step 5. March in time.** The scheme is explicit, so each time level follows
directly from the previous one. Start from the initial condition, apply the
boundary values at every level, and step forward until the desired time.

**Why iterative methods are used at all.** The same problem in the Laplace or
Poisson form gives a large linear system at every instant. A finite difference
discretisation of a $100 \times 100$ mesh gives over $10^4$ unknowns, and solving
it directly at every time step is wasteful when the change between steps is
small. The iterative methods trade a little work per step for a much cheaper
step, and for the elliptic case they converge to the steady state directly.

**The iterative method used in this paper.** For an **elliptic** equation, time
does not appear, so instead of marching one marches the **iteration count**.
Replacing each interior node by the average of its four neighbours and repeating
is exactly the **Liebmann method**, and the averaging weights of $\frac{1}{4}$ are
the same as above with $\lambda = \frac{1}{4}$. Q.8(b) works it through.

| | Explicit | Implicit | Crank-Nicolson |
| :-- | :-- | :-- | :-- |
| Stability | Needs $\lambda \le \frac{1}{4}$ | Unconditional | Unconditional |
| Work per step | Very low | Linear solve | Linear solve |
| Order in time | 1 | 1 | 2 |
| When to use | Short runs, small $\lambda$ | Stiff problems | Accuracy needed |

$$
\boxed{\text{Laplace, Poisson, wave, heat; the elliptic pair is solved by repeated averaging of the four neighbours}}
$$

---

<a id="nm-102"></a><a id="nm-10.2"></a>
## NM-10.2 · Laplace Equation

### [2018 Q.8(a), 2020 Q.8(b)]

**Appeared in:** 2018 Q.8(a), 2020 Q.8(b)

**Question.** Find the potential distribution at the interior nodes using Leibmann's method.

**Solution.**

**The mesh.** A $3\times3$ grid over a square region with uniform spacing $h$,
four interior nodes $1$ to $4$, and Dirichlet boundaries: top $100\ \text{V}$,
bottom $0\ \text{V}$, left $75\ \text{V}$, right $50\ \text{V}$.

```text
              Insulating Gap            V = 100 V           Insulating Gap
                            \                                /
                   (0,3)   +-----------+-----------+-------+   (3,3)
                           |           |           |       |
                           |    ①     |     ②     |       |
                   (0,2)   +-----------+-----------+-------+   (3,2)
                           |  (Node 1) | (Node 2)  |       |
             V = 75 V      |           |           |       |   V = 50 V
                   (0,1)   +-----------+-----------+-------+   (3,1)
                           |    ③     |     ④     |       |
                           |  (Node 3) | (Node 4)  |       |
                   (0,0)   +-----------+-----------+-------+   (3,0)
                            /                                \
              Insulating Gap             V = 0 V             Insulating Gap
```

**The stencil.** The Laplace finite-difference equation at an interior node is

$$u_{i,j} = \frac{1}{4}\left(u_{i+1,j} + u_{i-1,j} + u_{i,j+1} + u_{i,j-1}\right)$$

**Leibmann's method** is Gauss-Seidel applied to this system: each node is
updated from the most recent values of its neighbours as soon as they are
available.

**The four node equations.** Reading the neighbours of each interior node from
the figure:

$$V_1 = \frac{100 + V_2 + 75 + V_3}{4} = \frac{175 + V_2 + V_3}{4}$$

$$V_2 = \frac{100 + 50 + V_1 + V_4}{4} = \frac{150 + V_1 + V_4}{4}$$

$$V_3 = \frac{75 + V_4 + V_1 + 0}{4} = \frac{75 + V_1 + V_4}{4}$$

$$V_4 = \frac{V_3 + 50 + V_2 + 0}{4} = \frac{50 + V_2 + V_3}{4}$$

As a $4\times4$ system:

$$\begin{bmatrix} 4 & -1 & -1 & 0 \\ -1 & 4 & 0 & -1 \\ -1 & 0 & 4 & -1 \\ 0 & -1 & -1 & 4 \end{bmatrix}\begin{bmatrix} V_1 \\ V_2 \\ V_3 \\ V_4 \end{bmatrix} = \begin{bmatrix} 175 \\ 150 \\ 75 \\ 50 \end{bmatrix}$$

**Leibmann iteration.** Starting from $V_1 = V_2 = V_3 = V_4 = 0$:

| Sweep | $V_1$ | $V_2$ | $V_3$ | $V_4$ |
| :--: | :-- | :-- | :-- | :-- |
| 1 | 43.750000 | 48.437500 | 29.687500 | 32.031250 |
| 2 | 63.281250 | 61.328125 | 42.578125 | 38.476563 |
| 3 | 69.726563 | 64.550781 | 45.800781 | 40.087891 |
| 4 | 71.337891 | 65.356445 | 46.606445 | 40.490723 |
| 5 | 71.740723 | 65.557861 | 46.807861 | 40.591431 |
| 6 | 71.841431 | 65.608215 | 46.858215 | 40.616608 |

**The solution.** The iteration converges, and solving the $4\times4$ system
directly gives

$$V_1 = \frac{575}{8} = 71.875, \qquad V_2 = \frac{525}{8} = 65.625$$

$$V_3 = \frac{375}{8} = 46.875, \qquad V_4 = \frac{325}{8} = 40.625$$

$$\boxed{V_1 = 71.875\ \text{V}, \quad V_2 = 65.625\ \text{V}, \quad V_3 = 46.875\ \text{V}, \quad V_4 = 40.625\ \text{V}}$$

> [!info] Check by substitution into the four stencil equations
> Substituting back: $\dfrac{1}{4}(175 + 65.625 + 46.875) = \dfrac{287.5}{4} = 71.875$ ✓;
> $\dfrac{1}{4}(150 + 71.875 + 40.625) = \dfrac{262.5}{4} = 65.625$ ✓;
> $\dfrac{1}{4}(75 + 71.875 + 40.625) = \dfrac{187.5}{4} = 46.875$ ✓;
> $\dfrac{1}{4}(50 + 65.625 + 46.875) = \dfrac{162.5}{4} = 40.625$ ✓. All four hold
> exactly. The values come out as multiples of $1/8$, which is a strong check in
> itself, since the boundary data are multiples of $25$ and the average of four
> such numbers is a multiple of $1/4$ at worst; a wrong entry would leave a
> residual of order one-tenth rather than zero. Every one of the four sweeps
> approaches its limit from below, which is what a Gauss-Seidel start at the
> origin gives when the right-hand side is positive, and the increments in $V_1$
> fall in the ratio $19.53 : 6.45 : 1.61 : 0.40 : 0.10$, a factor of about four
> per sweep.

---

### [2019 Q.8(b)]

**Question.** Solve the Laplace's equation for the square region shown in the following figure, the boundary values being indicated in the figure.

**Solution.**

**The mesh.** A uniform $3\times3$ mesh over the square, with four interior nodes
$u_1, u_2, u_3, u_4$ and the boundary values shown.

```text
                Y
                |       1       2       B
             C  +-------+-------+-------+
                |       |       |       |
                |       |  u₃   |  u₄   |
                |       |       |       |
             1  +-------+-------+-------+  4
                |       |       |       |
                |       |  u₁   |  u₂   |
                |       |       |       |
             2  +-------+-------+-------+  5
                |       |       |       |
                |       |       |       |
                +-------+-------+-------+---------> X
                0       4       5       A
```

**The standard Laplace finite-difference stencil.** For a square mesh with
uniform spacing $h$, $\nabla^2 u = 0$ gives

$$\frac{u_{i+1,j} - 2u_{i,j} + u_{i-1,j}}{h^2} + \frac{u_{i,j+1} - 2u_{i,j} + u_{i,j-1}}{h^2} = 0$$

and cancelling $h^2$:

$$u_{i,j} = \frac{1}{4}\left(u_{i+1,j} + u_{i-1,j} + u_{i,j+1} + u_{i,j-1}\right)$$

**The four nodal equations.** Reading the neighbours of each interior node from
the figure, and taking the boundary values in the order left, right, top, bottom:

$$u_1 = \frac{1}{4}\left(u_2 + u_3 + 4 + 2\right)$$

$$4u_1 - u_2 - u_3 = 6$$

$$u_2 = \frac{1}{4}\left(u_1 + u_4 + 5 + 5\right)$$

$$4u_2 - u_1 - u_4 = 10$$

$$u_3 = \frac{1}{4}\left(u_1 + u_4 + 1 + 1\right)$$

$$4u_3 - u_1 - u_4 = 2$$

$$u_4 = \frac{1}{4}\left(u_3 + u_2 + 2 + 4\right)$$

$$4u_4 - u_3 - u_2 = 6$$

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

Every value is an integer, which is not a coincidence: the boundary data are
integers and the mesh is small, so the solution is a small rational that happens to
be integral.

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
> particular mesh, and it is itself a strong check: a wrong neighbour would leave
> a residual of order one-tenth rather than zero.

> [!info] Check by Gauss-Seidel iteration
> Taking the iteration form $u\leftarrow\tfrac{1}{4}(\text{sum of four neighbours})$
> and starting from $u_1 = u_2 = u_3 = u_4 = 0$ gives $1.500, 2.875, 0.875, 2.438$
> on the first iteration, then $2.438, 3.719, 1.719, 2.859$, then
> $2.859, 3.930, 1.930, 2.965$, approaching $3, 4, 2, 3$ as the iteration count
> rises, with the residual falling at each sweep. The coefficient matrix has
> diagonal $4$ and off-diagonal sum $2$, so it is strictly diagonally dominant
> and convergence is guaranteed. The iteration and the direct elimination agree
> on the same target, which is the independent confirmation of the solution.

---

<a id="nm-103"></a><a id="nm-10.3"></a>
## NM-10.3 · Poisson Equation

### [2021 Q.6(c)]

**Question.** Solve the Poisson equation $U_{xx} + U_{yy} = -10(x^2 + y^2 + 10)$ in the domain of the given figure.

**Solution.**

![Square domain 3 by 3 finite difference grid for the Poisson equation with u=0 on all four sides, x and y from 0 to 3, and four interior nodes u1, u2, u3, u4](diagrams/2021_Q6c_poisson_grid.jpg)
*Figure 2021 Q6(c): square domain finite-difference grid with Dirichlet boundary conditions for Poisson's equation (Source: Page 2, Q6(c))*

**Step 1. The grid.** The domain is $0 \le x \le 3$, $0 \le y \le 3$ with $h = k = 1$,
Here $u = 0$ on all four sides. Four interior nodes:

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

$$
\boxed{u_1 = 67.5, \quad u_2 = 75, \quad u_3 = 75, \quad u_4 = 82.5}
$$

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
> with exact rational arithmetic: it returns $(67.5, 75, 75, 82.5)$ and gives $u_2 = u_3$
> without being told to. All four residuals are exactly zero.
>
> A second structural check: the matrix is symmetric and diagonally dominant, so it
> is a positive-definite M-matrix and the solution is unique. The pattern
> $u_1 < u_2 = u_3 < u_4$ matches the source term, since
> $x^2+y^2+10$ is smallest at $(1,1)$ and largest at $(2,2)$, and the negative
> source means the largest magnitude of $u$ must occur where the source is most
> negative, that is at $(2,2)$. Correct.

> [!note] There is no polynomial exact solution for these boundary data
> It is tempting to look for a closed form. Try
> $U = ax^4 + bx^2y^2 + cy^4 + dx^2 + ey^2 + f$. Then
> $U_{xx} + U_{yy} = (12a+2b)x^2 + (2b+12c)y^2 + (2d+2e)$, and matching
> $-10(x^2+y^2+10)$ requires
> $$12a+2b=-10, \quad 2b+12c=-10, \quad 2d+2e=-100$$
> The condition $u = 0$ on $x = 0$ for all $y$ forces $c = e = f = 0$, and $u = 0$ on
> $y = 0$ forces $a = d = f = 0$. Then the constant equation reads $0 = -100$, a
> contradiction. **No quartic satisfies both the PDE and these boundary values**, so
> the finite difference solution above is the answer and there is nothing to check
> it against. That is normal: a polynomial can satisfy a PDE with compatible
> boundary data, but $u = 0$ on all four sides of a source that is everywhere
> negative is not compatible data.

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

**Solution.**

**Why they decide the answer.** A partial differential equation gives the
behaviour **inside** a region. Boundary conditions say what happens at the edges.
Together with the PDE they form a complete problem; without them the problem is
under-determined and the numerical solution is not unique.

**What breaks without them.**

1. **Non-uniqueness.** Second-order equations need two conditions. Supply one and
   the solution is still not fixed.
2. **Unstable growth.** An error at a boundary, or any small error at all,
   grows as it is carried across the grid, so a badly posed problem produces a
   wrong answer that grows with the grid size.
3. **Solvability.** The linear system from part (a) is singular without boundary
   equations, so standard solvers fail or return nonsense.

**Their role in practice.**

1. They supply the missing end rows when the interior difference equations leave
   the two outermost rows undefined.
2. They are enforced **exactly**, not approximately. Imposing $y(0) = 0$ to four
   significant figures injects that same error into every computed value.
3. Corner points, where two boundary curves meet, must satisfy **both**
   conditions. If they disagree at the corner the problem has no solution, and
   this is a common cause of a solver reporting a singular matrix.
4. The type of condition matters. For a diffusion problem, prescribing $u$
   (Dirichlet) is stable, while prescribing its derivative (Neumann) requires a
   compatibility check on the corner data.

$$\boxed{\text{PDE} + \text{boundary conditions} = \text{a problem with one unique numerical solution}}$$

---

[🏠 Master Index](00_Index.md) | [← Prev Topic: NM-9 · Eigenvalues & Eigenvectors](NM-9_Eigenvalues_and_Eigenvectors.md) | [Next Topic: DM-3 · Propositional Logic →](DM-3_Propositional_Logic.md)
