[← Previous: NM-8.7 Physical ODE](NM-8.7_Physical_ODE.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next Topic: NM-9 Eigenvalues →](../NM-9_Eigenvalues/_Topic_Overview.md)

---

# NM-8.8: Boundary Value Problems (BVP)

> 🟡 ⚠️ **Priority:** Light (Danger Zone -- Absent from Classroom Lecture Notes!) | **Tested:** 2/8 years (2021, 2024) | **Typical marks:** 4–5

## What This Is (and Why It Matters)

This is one of the biggest exam ambush topics in the entire ECE 2213 syllabus. If you look through student classroom notebooks, Boundary Value Problems are almost completely absent. Yet RUET examiners hit students with a full 5-mark numerical problem in 2021 (Q.5b) and a 4-mark theoretical derivation in 2024 (Q.4a).

In all the earlier subtopics (Euler, Heun, RK2, RK4), you were solving **Initial Value Problems (IVPs)**. You knew what happened at $t = 0$, so you took your marching boots and walked forward one step at a time.

In a **Boundary Value Problem (BVP)**, you are given conditions at two opposite physical ends (such as $y(0) = 0$ and $y(2) = 3.62686$). You cannot march forward from $x = 0$ because you do not know the initial launch angle or derivative $y'(0)$. If you guess wrong, you will completely miss the target at $x = 2$.

Instead of marching, we divide the interval into a grid, replace every derivative with central finite differences, and solve for all interior points simultaneously. The resulting system of equations forms a beautiful **tridiagonal matrix**, which we solve in one go.

---

## 📝 Key Definitions

> **Boundary Value Problem (BVP):** "in problems involving second-and higher-order differential equations, we may prescribe the conditions at two or more points. Such problems are called *boundary value problems*." -- Jain, §8.1 (p. 303)
>
> **In simple words:** A differential equation where the known facts are pinned down at two different spatial walls (like the two ends of a rod) instead of all being known at the starting time.

> **Finite-Difference Method for BVP:** "The finite-difference method for the solution of a two-point boundary value problem consists in replacing the derivatives occurring in the differential equation (and in the boundary conditions as well) by means of their finite-difference approximations and then solving the resulting linear system of equations by a standard procedure." -- Jain, §8.10.1 (p. 325)
>
> **In simple words:** Lay down a mesh of grid points across the span. Swap every derivative with central difference formulas ($y'' \approx \frac{y_{i-1} - 2y_i + y_{i+1}}{h^2}$). That turns the calculus equation into high-school linear algebra.

> **Tridiagonal Linear System:** A matrix equation where non-zero coefficients exist only along the main diagonal, the sub-diagonal directly below it, and the super-diagonal directly above it.
>
> **In simple words:** Each interior point talks only to its immediate left neighbor and its immediate right neighbor. This creates a very sparse, easy-to-solve ribbon of equations.

---

## The Core Idea

### 1. The Four-Step General Approach

Whenever an exam asks you to *"Describe the general approach for solving boundary value problems numerically"* (as in 2024 Q.4a), write these four structured steps:

#### Step 1: Domain Discretization (Grid Mesh)
Divide the continuous domain $[x_0, x_n]$ into $n$ equal subintervals of width $h = \frac{x_n - x_0}{n}$.
The grid coordinates are:

$$
x_i = x_0 + i h, \qquad i = 0, 1, 2, \dots, n
$$

The boundary values $y_0 = y(x_0)$ and $y_n = y(x_n)$ are already fixed by the given boundary conditions. That leaves $n - 1$ unknown interior values: $y_1, y_2, \dots, y_{n-1}$.

#### Step 2: Finite Difference Replacement
At every interior grid point $x_i$ ($1 \le i \le n - 1$), replace the derivatives using second-order central difference formulas:

$$
y''(x_i) \approx \frac{y_{i-1} - 2y_i + y_{i+1}}{h^2}
$$

$$
y'(x_i) \approx \frac{y_{i+1} - y_{i-1}}{2h}
$$

#### Step 3: Assembly into Difference Equations
Substitute these approximations into the governing ODE. For example, for the linear ODE:

$$
y''(x) + f(x) y'(x) + g(x) y(x) = r(x)
$$

at node $i$, multiplying through by $h^2$ gives:

$$
\left(1 - \frac{h}{2} f_i\right) y_{i-1} + \left(-2 + g_i h^2\right) y_i + \left(1 + \frac{h}{2} f_i\right) y_{i+1} = h^2 r_i
$$

For node $i = 1$, the term $y_0$ is known and moves to the right-hand side.
For node $i = n - 1$, the term $y_n$ is known and moves to the right-hand side.

#### Step 4: Solve the Tridiagonal Linear System
The resulting $(n-1) \times (n-1)$ system is tridiagonal:

$$
\begin{bmatrix}
d_1 & u_1 & 0 & \dots & 0 \\
l_2 & d_2 & u_2 & \dots & 0 \\
0 & l_3 & d_3 & \dots & 0 \\
\vdots & & \ddots & \ddots & \vdots \\
0 & \dots & 0 & l_{n-1} & d_{n-1}
\end{bmatrix}
\begin{bmatrix}
y_1 \\
y_2 \\
y_3 \\
\vdots \\
y_{n-1}
\end{bmatrix}
=
\begin{bmatrix}
b_1 \\
b_2 \\
b_3 \\
\vdots \\
b_{n-1}
\end{bmatrix}
$$

Solve this system simultaneously using the **Thomas algorithm** (specialized tridiagonal Gaussian elimination) or **Gauss-Seidel iteration**.

---

### 2. How BVP Differs from IVP

This table answers the second half of 2024 Q.4(a):

| Feature | Initial Value Problem (IVP) | Boundary Value Problem (BVP) |
|:---|:---|:---|
| **Condition Placement** | Given at one single starting point (e.g. $y(0) = y_0, y'(0) = v_0$) | Given at both boundaries of the domain (e.g. $y(a) = \alpha, y(b) = \beta$) |
| **Solving Direction** | Marches sequentially forward from start to finish | Solves all interior grid points simultaneously |
| **Matrix Structure** | Lower-triangular (each step depends only on previous step) | Tridiagonal system coupling neighboring nodes |
| **Computational Work** | Very cheap per step; simple explicit function evaluation | Requires solving an $(n-1) \times (n-1)$ simultaneous linear system |
| **Error Propagation** | Local errors accumulate downstream in time | Global error sensitivity; a change at either boundary shifts every interior value |
| **The Shooting Method** | Not applicable | Converts BVP to IVP by guessing $y'(a)$ and tuning it iteratively until it hits $y(b)$ |

---

### 3. The Crucial Diagonal Sign Trap

Look at the simple test equation from the 2021 exam:

$$
\frac{d^2y}{dx^2} - y = 0
$$

Substitute the central difference:

$$
\frac{y_{i-1} - 2y_i + y_{i+1}}{h^2} - y_i = 0
$$

Multiply through by $h^2$:

$$
(y_{i-1} - 2y_i + y_{i+1}) - h^2 y_i = 0
$$

Collect like terms:

$$
y_{i-1} - (2 + h^2) y_i + y_{i+1} = 0
$$

> [!WARNING] Watch the Sign on the Diagonal!
> The coefficient of $y_i$ on the main diagonal is **$-(2 + h^2)$**, NOT $+(2 + h^2)$!
> Because $|-(2 + h^2)| = 2 + h^2 > 1 + 1 = 2$, the diagonal element is strictly larger than the sum of the off-diagonal elements. That means the matrix is **strictly diagonally dominant**.
> Strict diagonal dominance guarantees that:
> 1. A unique solution exists.
> 2. The Thomas algorithm will never divide by zero (no pivoting needed).
> 3. Gauss-Seidel iteration is guaranteed to converge!
>
> If you mess up the minus sign and write $+(2 - h^2)$, the matrix loses diagonal dominance, gives wildly incorrect signs, and fails completely.

---

## 🔧 Worked Example

> **From:** 2021 Q.5(b) -- [Marks: 05, CO: 3]

**The question:** Solve the boundary value problem $\frac{d^2y}{dx^2} - y = 0$ with $y(0) = 0$ and $y(2) = 3.62686$.

**Let's solve this step by step.**

### Step 1: Set up the grid and discretization

We are given the domain $[0, 2]$ with boundary values:

$$
y(0) = 0, \qquad y(2) = 3.62686
$$

Choose a step size $h = 0.5$.
This partitions the interval $[0, 2]$ into $n = 4$ subintervals:
- $x_0 = 0.0 \implies y_0 = 0$ (given boundary condition)
- $x_1 = 0.5 \implies y_1$ (unknown interior point)
- $x_2 = 1.0 \implies y_2$ (unknown interior point)
- $x_3 = 1.5 \implies y_3$ (unknown interior point)
- $x_4 = 2.0 \implies y_4 = 3.62686$ (given boundary condition)

We have 3 interior unknowns: $y_1, y_2, y_3$.

### Step 2: Formulate the difference equation

Using central differences for $y''$:

$$
\frac{y_{i-1} - 2y_i + y_{i+1}}{h^2} - y_i = 0
$$

With $h = 0.5$, $h^2 = 0.25$:

$$
\frac{y_{i-1} - 2y_i + y_{i+1}}{0.25} - y_i = 0
$$

Multiply through by $0.25$:

$$
y_{i-1} - 2y_i + y_{i+1} - 0.25 y_i = 0
$$

$$
y_{i-1} - 2.25 y_i + y_{i+1} = 0, \qquad \text{for } i = 1, 2, 3
$$

### Step 3: Write out the three simultaneous equations

**For $i = 1$ ($x_1 = 0.5$):**

$$
y_0 - 2.25 y_1 + y_2 = 0
$$

Since $y_0 = 0$:

$$
-2.25 y_1 + y_2 = 0 \implies y_2 = 2.25 y_1 \tag{Eq. 1}
$$

**For $i = 2$ ($x_2 = 1.0$):**

$$
y_1 - 2.25 y_2 + y_3 = 0 \tag{Eq. 2}
$$

Substitute $y_2 = 2.25 y_1$ into Eq. 2:

$$
y_1 - 2.25(2.25 y_1) + y_3 = 0
$$

$$
y_1 - 5.0625 y_1 + y_3 = 0 \implies y_3 = 4.0625 y_1 \tag{Eq. 3}
$$

**For $i = 3$ ($x_3 = 1.5$):**

$$
y_2 - 2.25 y_3 + y_4 = 0
$$

Since $y_4 = 3.62686$:

$$
y_2 - 2.25 y_3 = -3.62686 \tag{Eq. 4}
$$

### Step 4: Solve the system

Substitute $y_2 = 2.25 y_1$ and $y_3 = 4.0625 y_1$ into Eq. 4:

$$
2.25 y_1 - 2.25(4.0625 y_1) = -3.62686
$$

$$
2.25 y_1 - 9.140625 y_1 = -3.62686
$$

$$
-6.890625 y_1 = -3.62686
$$

$$
y_1 = \frac{-3.62686}{-6.890625} \approx 0.5263469 \approx 0.5263
$$

Now compute $y_2$ and $y_3$:

$$
y_2 = 2.25 y_1 = 2.25 \times 0.5263469 \approx 1.1842805 \approx 1.1843
$$

$$
y_3 = 4.0625 y_1 = 4.0625 \times 0.5263469 \approx 2.1382843 \approx 2.1383
$$

### Summary of Results

| Grid Point | $x$ | Numerical $y$ ($h = 0.5$) | Exact Solution | Absolute Error |
|:---:|:---:|:---:|:---:|:---:|
| Boundary $x_0$ | 0.0 | 0.0000 | 0.000000 | Exact |
| Node $x_1$ | 0.5 | 0.5263 | 0.521095 | $+0.0052$ |
| Node $x_2$ | 1.0 | 1.1843 | 1.175201 | $+0.0091$ |
| Node $x_3$ | 1.5 | 2.1383 | 2.129279 | $+0.0090$ |
| Boundary $x_4$ | 2.0 | 3.6269 | 3.626860 | Exact |

$$
\boxed{y(0.5) = 0.5263,\quad y(1.0) = 1.1843,\quad y(1.5) = 2.1383 \quad (h = 0.5)}
$$

**Quick sanity check against exact calculus:**
The general solution of $y'' - y = 0$ is $y(x) = A \cosh x + B \sinh x$.
$y(0) = 0 \implies A = 0$.
$y(2) = B \sinh 2 = 3.62686 \implies B = \frac{3.62686}{\sinh 2} = \frac{3.62686}{3.6268604} \approx 1.000000$.
So the exact analytical solution is simply:

$$
y(x) = \sinh x
$$

- At $x = 0.5$: $\sinh(0.5) \approx 0.521095$. (Numerical: $0.5263$).
- At $x = 1.0$: $\sinh(1.0) \approx 1.175201$. (Numerical: $1.1843$).
- At $x = 1.5$: $\sinh(1.5) \approx 2.129279$. (Numerical: $2.1383$).
Our coarse $h = 0.5$ numerical solution overshoots the exact hyperbolic curve by less than $1\%$, exactly matching expected second-order finite difference behavior.

---

## 🏆 Past Exam Questions

### 2024 Q.4(a): General Approach for BVP vs. IVP -- [04 Marks]

**The question:** Describe the general approach for solving boundary value problems numerically. How does it differ from solving initial value problems?

**Full Answer:**

**1. The General Numerical Approach for BVPs:**
The standard finite-difference approach proceeds in four steps:
1. **Grid Discretization:** The domain $[a, b]$ is divided into $n$ equal subintervals of width $h = (b - a)/n$, creating $n + 1$ grid points $x_i = a + ih$. The end points $y_0$ and $y_n$ are known from the boundary conditions, leaving $n - 1$ interior unknowns.
2. **Derivative Replacement:** At each interior node $x_i$, derivatives are replaced by central difference approximations:

$$
y''_i \approx \frac{y_{i-1} - 2y_i + y_{i+1}}{h^2}, \qquad y'_i \approx \frac{y_{i+1} - y_{i-1}}{2h}
$$

3. **Formulation of Difference Equations:** Substituting these approximations into the differential equation at each interior node produces $n - 1$ coupled algebraic equations. Known boundary values $y_0$ and $y_n$ are shifted into the right-hand load vector.
4. **Simultaneous Linear Solve:** The resulting linear system is tridiagonal:

$$
A \vec{y} = \vec{b}
$$

It is solved simultaneously for all interior unknowns $\vec{y} = [y_1, y_2, \dots, y_{n-1}]^T$ using the Thomas algorithm or Gauss-Seidel iteration.

**2. Key Differences Between BVP and IVP:**

| Criterion | Initial Value Problem (IVP) | Boundary Value Problem (BVP) |
|:---|:---|:---|
| **Conditions** | All conditions given at one end ($x = x_0$) | Conditions given at two separate ends ($x = a$ and $x = b$) |
| **Solution Method** | March forward step-by-step | Solve full linear system simultaneously |
| **System Type** | Lower triangular (explicit evaluation) | Tridiagonal linear algebraic system |
| **Computational Cost** | Low cost per step | Requires solving an $(n-1) \times (n-1)$ linear system |
| **Error Sensitivity** | Local error accumulates forward in time | Global sensitivity across the whole domain |
| **Shooting Method** | Not applicable | Converts BVP to IVP by iterating on initial slope guess |

---

### Exam Variants at a Glance

| Year | What They Asked | Problem Type | Key Answer |
|:---|:---|:---|:---|
| **2021 Q.5(b)** | Solve $y'' - y = 0, y(0)=0, y(2)=3.62686$ | Numerical BVP ($h = 0.5$) | $\boxed{y(0.5) = 0.5263,\quad y(1.0) = 1.1843,\quad y(1.5) = 2.1383 \quad (h = 0.5)}$ |
| **2024 Q.4(a)** | General approach for BVPs vs IVPs | Theory and comparison | Four-step finite difference construction, tridiagonal matrix solve |

---

## ⚡ Quick Review

**The method in one sentence:** Replace derivatives with central differences, plug in the known boundary values at both ends, and solve the resulting tridiagonal matrix simultaneously.

**The central difference substitutions to memorize:**

$$
y''_i = \frac{y_{i-1} - 2y_i + y_{i+1}}{h^2}, \qquad y'_i = \frac{y_{i+1} - y_{i-1}}{2h}
$$

**The most common exam mistake:** Forgetting that for $n$ subintervals, there are only $n - 1$ interior unknowns. With $h = 0.5$ on $[0, 2]$, $n = 4$, so there are 3 unknowns ($y_1, y_2, y_3$), while $y_0$ and $y_4$ are already known constants!

**Time estimate in exam:** 10–12 minutes for setting up the tridiagonal system and solving the 3 linear equations.

---

## 🔗 Connected Topics

- [← NM-8.7: Physical ODE](NM-8.7_Physical_ODE.md) -- previous subtopic covering physical modeling.
- [NM-8.1: IVP vs BVP](NM-8.1_IVP_vs_BVP.md) -- the theoretical foundation contrasting initial values and boundary values.
- [NM-3.5: Gauss-Seidel Iteration](../NM-3_Linear_Systems/NM-3.5_Gauss_Seidel_Iteration.md) -- iterative matrix solver used for large tridiagonal BVP systems.
- [NM-10.2: Laplace Equation](../NM-10_PDE/NM-10.2_Laplace_Equation.md) -- extending 1D finite-difference BVP stencils to 2D elliptic PDEs.
- [Next Topic: NM-9 Eigenvalues →](../NM-9_Eigenvalues/_Topic_Overview.md) -- characteristic value problems in differential systems.

---

[← Previous: NM-8.7 Physical ODE](NM-8.7_Physical_ODE.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next Topic: NM-9 Eigenvalues →](../NM-9_Eigenvalues/_Topic_Overview.md)
