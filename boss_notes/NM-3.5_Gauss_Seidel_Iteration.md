[← Previous: NM-3.2 Pivoting](NM-3.2_Pivoting.md) | [🏠 Index](00_Index.md) | [Next: NM-3.8 Circuit Applications →](NM-3.8_Circuit_Applications.md)

---

# NM-3.5: Gauss-Seidel Iteration
> **Section:** A (Numerical Methods) | **Priority:** 🔴 | **Exam Frequency:** 7/8 years
> **Sources:** Jain Ch.7 §7.6, Topicwise NM-3.5, Fahad Notes §01, Shishir Notes §02, CT-02B

## Why This Topic Matters

Gauss-Seidel is the single highest-yield topic in numerical linear algebra for ECE 2213. It appears in almost every semester final. In RUET exams, the examiners almost always dress Gauss-Seidel as a DC circuit problem. You must write the mesh or nodal equations first, arrange them for diagonal dominance, and then execute the iteration sweeps. If you know how to handle current sources and keep your row ordering strictly dominant, these are the easiest 5 to 6 marks on the entire paper.

---

## 📝 Key Definitions

> **Iterative Methods:** "We shall now describe the *iterative* or *indirect* methods, which start from an *approximation* to the true solution and, if convergent, derive a sequence of closer approximations, *the cycle of computations being repeated till the required accuracy is obtained*." — Jain, §7.6 (p. 279)

> **Gauss-Seidel Method (Successive Displacements):** "It is clear, therefore, that this method uses an improved component as soon as it is available and it is called the *method of successive displacements*, or the *Gauss–Seidel method*." — Jain, §7.6 (p. 281)

> **Jacobi Method (Simultaneous Displacements):** "This method is due to Jacobi and is called the *method of simultaneous displacements*." — Jain, §7.6 (p. 280)

> **Convergence Condition (Diagonal Dominance):** "The Jacobi and Gauss–Seidel methods converge, for any choice of the first approximation $x_j^{(1)}$ $(j = 1, 2, \dots, n)$, if every equation of the system (7.60) satisfies the condition that the sum of the absolute values of the coefficients $a_{ij}/a_{ii}$ is almost equal to, or in at least one equation less than unity, i.e. provided that $\sum_{j=1, \, j \ne i}^n \left| \frac{a_{ij}}{a_{ii}} \right| \le 1, \quad (i = 1, 2, \dots, n)$." — Jain, §7.6 (p. 281)

---

## Core Theory

### Direct vs. Iterative Methods

Direct methods like Gaussian elimination find the exact solution in a predetermined number of arithmetic steps. But for large or sparse matrices, round-off errors accumulate rapidly.

Iterative methods start from an initial guess vector $X^{(0)}$ and generate a sequence of vectors $X^{(1)}, X^{(2)}, \dots, X^{(k)}$ that converge toward the true solution.

| Feature | Direct Methods (Gauss Elimination, LU) | Iterative Methods (Gauss-Seidel, Jacobi) |
| :-- | :-- | :-- |
| **Operation Count** | Fixed in advance ($O(n^3)$ operations) | Depends on desired precision and convergence rate |
| **Round-off Sensitivity** | High for large or ill-conditioned systems | Self-correcting; round-off in early steps washes out |
| **Zero Preservation** | Fill-in destroys matrix sparsity | Ideal for large sparse systems (circuits, PDEs) |
| **Storage Need** | Must store full matrix during elimination | Only stores non-zero coefficients and current vector |

### The Gauss-Seidel Update Mechanism

Consider an $n \times n$ linear system $AX = B$:

$$
\begin{aligned}
a_{11}x_1 + a_{12}x_2 + \dots + a_{1n}x_n &= b_1 \\
a_{21}x_1 + a_{22}x_2 + \dots + a_{2n}x_n &= b_2 \\
&\;\;\vdots \\
a_{n1}x_1 + a_{n2}x_2 + \dots + a_{nn}x_n &= b_n
\end{aligned}
$$

Assume every diagonal element $a_{ii} \ne 0$. Solve the $i$-th equation for $x_i$:

$$
x_i = \frac{1}{a_{ii}} \left( b_i - \sum_{j=1}^{i-1} a_{ij}x_j - \sum_{j=i+1}^n a_{ij}x_j \right)
$$

The difference between Jacobi and Gauss-Seidel lies entirely in the iteration superscripts:

1. **Jacobi (Simultaneous Displacements):** Uses only values from iteration $k$ to compute all values at iteration $k+1$:

$$
x_i^{(k+1)} = \frac{1}{a_{ii}} \left( b_i - \sum_{j \ne i} a_{ij} x_j^{(k)} \right)
$$

2. **Gauss-Seidel (Successive Displacements):** Uses the newly computed values $x_1^{(k+1)}, \dots, x_{i-1}^{(k+1)}$ as soon as they are ready:

$$
x_i^{(k+1)} = \frac{1}{a_{ii}} \left( b_i - \sum_{j=1}^{i-1} a_{ij} x_j^{(k+1)} - \sum_{j=i+1}^n a_{ij} x_j^{(k)} \right)
$$

Because fresh values propagate immediately, Gauss-Seidel typically converges **twice as fast** as Jacobi. The spectral radius satisfies $\rho(T_{GS}) \approx \rho(T_J)^2$.

### The Strict Diagonal Dominance Rule

A matrix $A$ is **strictly diagonally dominant** if in every single row, the absolute value of the diagonal entry strictly exceeds the sum of the absolute values of all other entries in that row:

$$
|a_{ii}| > \sum_{j \ne i} |a_{ij}| \quad \text{for all } i = 1, 2, \dots, n
$$

**Theorem:** If matrix $A$ is strictly diagonally dominant, the Gauss-Seidel iteration converges to the unique solution for **any** arbitrary starting vector $X^{(0)}$.

> [!WARNING]
> **Row ordering decides convergence or divergence.**
> If your system is not diagonally dominant as given, you must rearrange the equations before iterating. Solving the wrong equation for a variable can make the spectral radius exceed unity, causing the iteration to blow up to infinity.

### Special Rules for Circuit Analysis in ECE 2213

Exam questions in this topic are almost always DC circuits. Keep these two circuit rules in mind:

1. **Independent current source on an outer branch:** It fixes the mesh current completely. Do not create an iteration equation for it. Set $I = I_{\text{source}}$ as a known constant.
2. **Dependent source:** Relate the dependent source variable directly to node voltages or branch currents first. Substitute it into the KCL/KVL equations before setting up the iteration.

---

## Worked Example (PYQ 2020 Q.4(b) / 2024 Q.2(b))

Solve for $I_1$, $I_2$, and $I_3$ in the circuit below using the Gauss-Seidel method.

![Three-mesh DC resistive network with a 400 V source, 20, 40, 10 and 100 ohm resistors, and a downward 10 A current source, with clockwise mesh currents I1, I2, I3](diagrams/nm3_gs_circuit_2020_three_mesh.jpg)

> **Source:** 2020 Q.4(b), 2024 Q.2(b) [Marks: 06 / 04]

### Step 1: Identify Fixed Branch Currents
Mesh 3 contains a $10\text{ A}$ current source on its outer branch pointing downward. Because no other mesh shares this outer branch:

$$
I_3 = 10\text{ A}
$$

$I_3$ is constant. It drops out of the unknowns.

### Step 2: Formulate KVL for Mesh 1 and Mesh 2
Around Mesh 1 clockwise:

$$
-400 + 20I_1 + 40(I_1 - I_2) = 0 \implies 60I_1 - 40I_2 = 400
$$

Around Mesh 2 clockwise:

$$
40(I_2 - I_1) + 10I_2 + 100(I_2 - I_3) = 0
$$

Substitute $I_3 = 10\text{ A}$:

$$
-40I_1 + 150I_2 - 100(10) = 0 \implies -40I_1 + 150I_2 = 1000
$$

### Step 3: Check Diagonal Dominance and Form Iteration Formulas
Row 1: $|60| > |-40| = 40$ (dominant in $I_1$).  
Row 2: $|150| > |-40| = 40$ (dominant in $I_2$).  
Both rows are strictly diagonally dominant. Express each variable:

$$
I_1^{(k+1)} = \frac{400 + 40I_2^{(k)}}{60}
$$

$$
I_2^{(k+1)} = \frac{1000 + 40I_1^{(k+1)}}{150}
$$

### Step 4: Iteration Table
Start from $I_1^{(0)} = 0$, $I_2^{(0)} = 0$:

- **Iteration 1:**

$$
I_1^{(1)} = \frac{400 + 40(0)}{60} = 6.666667
$$

$$
I_2^{(1)} = \frac{1000 + 40(6.666667)}{150} = \frac{1266.66668}{150} = 8.444444
$$

- **Iteration 2:**

$$
I_1^{(2)} = \frac{400 + 40(8.444444)}{60} = 12.296296
$$

$$
I_2^{(2)} = \frac{1000 + 40(12.296296)}{150} = 9.945679
$$

Running the iterations gives:

| $k$ | $I_1$ | $I_2$ |
| --: | --: | --: |
| 0 | 0.000000 | 0.000000 |
| 1 | 6.666667 | 8.444444 |
| 2 | 12.296296 | 9.945679 |
| 3 | 13.297119 | 10.212565 |
| 4 | 13.475043 | 10.260012 |
| 5 | 13.506674 | 10.268447 |
| 6 | 13.512298 | 10.269946 |
| 7 | 13.513297 | 10.270213 |
| 8 | 13.513475 | 10.270260 |
| 9 | 13.513507 | 10.270268 |
| 10 | 13.513512 | 10.270270 |

$$
\boxed{I_1 = 13.5135 \text{ A}, \qquad I_2 = 10.2703 \text{ A}, \qquad I_3 = 10.0000 \text{ A}}
$$

---

## Exam Variants

| Year | Circuit / System Type | Unknowns | Key Answer |
| :-- | :-- | :-- | :-- |
| **2018 Q.4(b)** | 4-mesh DC network with $10\text{ A}$ source | $I_1, I_3, I_4$ ($I_2 = -10\text{ A}$) | $\boxed{I_1 = -4.1103\ \text{A}, \quad I_2 = -10\ \text{A}, \quad I_3 = -6.8695\ \text{A}, \quad I_4 = -1.0426\ \text{A}}$ |
| **2019 Q.3(c)** | 2-node DC network with 2 current sources | $V_1, V_2$ (2 sweeps) | $\boxed{V_1 = 13.3333\ \text{V}, \qquad V_2 = 20\ \text{V}}$ |
| **2020 Q.4(b)** / **2024 Q.2(b)** | 3-mesh DC network with $10\text{ A}$ source | $I_1, I_2$ ($I_3 = 10\text{ A}$) | $\boxed{I_1 = 13.5135 \text{ A}, \qquad I_2 = 10.2703 \text{ A}, \qquad I_3 = 10.0000 \text{ A}}$ |
| **2021 Q.7(b)** | DC network with dependent source $5I_0$ | $V_C, V_R, I_0$ | $\boxed{I_0 = 1.6235 \text{ A}, \quad V_C = 13.7648 \text{ V}, \quad V_R = 8.1176 \text{ V}}$ |
| **2017 Q.4(c)** | $3 \times 3$ algebraic system with $\lambda = 0.95$ | $x_1, x_2, x_3$ | $\boxed{x_1 \approx 1.7097, \qquad x_2 \approx 2.8300, \qquad x_3 \approx 4.3564}$ |
| **CT-02B Q.1(a-c)** | $3 \times 3$ algebraic system, 4 iterations | $x, y, z$ and $\Delta$ | $\boxed{(x_4, y_4, z_4) = (2.160663,\ -2.299281,\ 0.662992)}$ |

---

## 🏆 Golden Questions (Past Exam Archive)

### 🎯 Solve the following circuit by using Gauss-Seidel method.
> **Appeared:** 2018 Q.4(b) — (05 marks)

![Four-mesh DC circuit with independent 100 V source, 10 A current source, and five resistors](diagrams/nm3_gs_circuit_2018_four_mesh.jpg)

**Full Answer:**

**The circuit.** A planar four-mesh DC network in a $2\times2$ arrangement.
Mesh 1 (top-left) contains a $10\ \Omega$ top branch, a $20\ \Omega$ right branch shared with mesh 2, a $25\ \Omega$ bottom branch shared with mesh 4, and a connecting wire on the left.
Mesh 2 (top-right) contains a $10\ \text{A}$ current source in its top branch directed leftward, the shared $20\ \Omega$ on its left, a $25\ \Omega$ bottom branch shared with mesh 3, and a wire on the right.
Mesh 3 (bottom-right) contains the shared $25\ \Omega$ on top, a $4\ \Omega$ left branch shared with mesh 4, an $8\ \Omega$ right branch, and a wire on the bottom.
Mesh 4 (bottom-left) contains the shared $25\ \Omega$ on top, the shared $4\ \Omega$ on the right, a $100\ \text{V}$ source on the left directed upward, and a wire on the bottom.

**Step 1: The current-source constraint.** The $10\ \text{A}$ source occupies the top branch of mesh 2 alone. Taking mesh currents clockwise, the branch carries $I_2$ and the source opposes it:

$$
I_2 = -10\ \text{A}
$$

**Step 2: Mesh KVL equations.**
- **Mesh 1:** Traversing clockwise:

$$
10I_1 + 20(I_1 - I_2) + 25(I_1 - I_4) = 0 \implies 55I_1 - 25I_4 = 20I_2 = -200
$$

- **Mesh 3:** Traversing clockwise:

$$
8I_3 + 25(I_3 - I_2) + 4(I_3 - I_4) = 0 \implies 37I_3 - 4I_4 = 25I_2 = -250
$$

- **Mesh 4:** Traversing clockwise:

$$
25(I_4 - I_1) + 4(I_4 - I_3) = 100 \implies -25I_1 - 4I_3 + 29I_4 = 100
$$

**Step 3: Gauss-Seidel recursions.** Solve each equation for its diagonal unknown:

$$
I_1^{(k+1)} = \frac{-200 + 25I_4^{(k)}}{55}
$$

$$
I_3^{(k+1)} = \frac{-250 + 4I_4^{(k)}}{37}
$$

$$
I_4^{(k+1)} = \frac{100 + 25I_1^{(k+1)} + 4I_3^{(k+1)}}{29}
$$

Start from $I_1^{(0)} = I_3^{(0)} = I_4^{(0)} = 0$.

| Iteration | $I_1$ | $I_3$ | $I_4$ |
| :--: | :-- | :-- | :-- |
| 1 | $-3.636364$ | $-6.756757$ | $-0.618487$ |
| 2 | $-3.917494$ | $-6.823620$ | $-0.870063$ |
| 3 | $-4.031847$ | $-6.850818$ | $-0.972395$ |
| 4 | $-4.078361$ | $-6.861880$ | $-1.014019$ |
| 5 | $-4.097281$ | $-6.866380$ | $-1.030950$ |
| 6 | $-4.104977$ | $-6.868211$ | $-1.037837$ |
| 7 | $-4.108108$ | $-6.868955$ | $-1.040638$ |
| 8 | $-4.109381$ | $-6.869258$ | $-1.041778$ |

Exact values by direct elimination:

$$
I_1 = -\frac{14390}{3501} = -4.1103\ \text{A}, \qquad I_3 = -\frac{24050}{3501} = -6.8695\ \text{A}, \qquad I_4 = -\frac{3650}{3501} = -1.0426\ \text{A}
$$

$$
\boxed{I_1 = -4.1103\ \text{A}, \quad I_2 = -10\ \text{A}, \quad I_3 = -6.8695\ \text{A}, \quad I_4 = -1.0426\ \text{A}}
$$

---

### 🎯 Obtain the nodal equations from the following circuit. Hence solve for the unknowns using Gauss-Seidel iterative method. Show two iterations only.
> **Appeared:** 2019 Q.3(c) — (04 marks)

![Two-node DC resistive network with 5 A and 10 A current sources, and three resistors](diagrams/nm3_gs_circuit_2019_nodal.jpg)

**Full Answer:**

**The circuit.** Two non-reference nodes, $V_1$ and $V_2$, with a common reference ground. Node 1 connects to ground through $2\ \Omega$ and to node 2 through $4\ \Omega$, with a $5\ \text{A}$ source entering node 1 through the top branch. Node 2 connects to ground through $6\ \Omega$ and to node 1 through $4\ \Omega$, with a $5\ \text{A}$ source leaving toward node 1 and a $10\ \text{A}$ source entering node 2.

**Step 1: KCL at node 1.** Currents leaving node 1:

$$
\frac{V_1}{2} + \frac{V_1 - V_2}{4} - 5 = 0
$$

Multiplying by 4:

$$
2V_1 + V_1 - V_2 - 20 = 0 \implies \boxed{3V_1 - V_2 = 20}
$$

**Step 2: KCL at node 2.** Currents leaving node 2:

$$
\frac{V_2}{6} + \frac{V_2 - V_1}{4} + 5 = 10
$$

Multiplying by 12:

$$
2V_2 + 3(V_2 - V_1) + 60 = 120 \implies \boxed{-3V_1 + 5V_2 = 60}
$$

**Step 3: Gauss-Seidel form.**
Check diagonal dominance: $|3| > |-1|$ and $|5| > |-3|$. The system is strictly diagonally dominant. Express each variable:

$$
V_1^{(k+1)} = \frac{20 + V_2^{(k)}}{3}, \qquad V_2^{(k+1)} = \frac{60 + 3V_1^{(k+1)}}{5}
$$

Start from $V_1^{(0)} = 0$, $V_2^{(0)} = 0$:

| Iteration | $V_1^{(k+1)} = \dfrac{20 + V_2^{(k)}}{3}$ | $V_2^{(k+1)} = \dfrac{60 + 3V_1^{(k+1)}}{5}$ |
| :--: | :-- | :-- |
| 1 | $\dfrac{20 + 0}{3} = 6.666667$ | $\dfrac{60 + 3(6.666667)}{5} = 16.000000$ |
| 2 | $\dfrac{20 + 16}{3} = 12.000000$ | $\dfrac{60 + 3(12)}{5} = 19.200000$ |

Two iterations only, as required:

$$
V_1^{(1)} = 6.666667\ \text{V}, \quad V_2^{(1)} = 16.000000\ \text{V}
$$

$$
V_1^{(2)} = 12.000000\ \text{V}, \quad V_2^{(2)} = 19.200000\ \text{V}
$$

**Exact solution for reference:**

$$
4V_2 = 80 \implies V_2 = 20\ \text{V}, \qquad 3V_1 = 40 \implies V_1 = 13.333333\ \text{V}
$$

$$
\boxed{V_1 = 13.3333\ \text{V}, \qquad V_2 = 20\ \text{V}}
$$

---

### 🎯 Determine the value of $I_0$ in the given circuit using Gauss-Seidel method.
> **Appeared:** 2021 Q.7(b) — (06 marks, CO: 2)

![DC circuit with independent 30 V source, four resistors, and dependent voltage source 5I0](diagrams/nm3_gs_circuit_2021_dependent_source.jpg)

**Full Answer:**

**Step 1: Identify node voltages.**
Take the bottom rail as reference ($0\text{ V}$).
- Top rail: $V_T = 30\text{ V}$ (held by independent voltage source).
- Centre node: $V_C$.
- Right node: $V_R$.

**Step 2: Express the controlling current $I_0$.**
The branch through the $10\ \Omega$ resistor runs from the top rail to the centre node:

$$
I_0 = \frac{V_T - V_C}{10} = \frac{30 - V_C}{10}
$$

**Step 3: Account for the dependent voltage source.**
The dependent voltage source $5I_0$ connects between ground and node $R$:

$$
V_R = 5I_0 = 5\left(\frac{30 - V_C}{10}\right) = 15 - 0.5V_C
$$

Rearranging into linear form:

$$
V_C + 2V_R = 30
$$

**Step 4: KCL at centre node $C$.**
Three branches leave node $C$: upward to $30\text{ V}$ rail, downward to ground, and rightward to node $R$:

$$
\frac{V_C - 30}{10} + \frac{V_C - 0}{15} + \frac{V_C - V_R}{8} = 0
$$

Multiply through by 120:

$$
12(V_C - 30) + 8V_C + 15(V_C - V_R) = 0
$$

$$
12V_C - 360 + 8V_C + 15V_C - 15V_R = 0 \implies 35V_C - 15V_R = 360
$$

**Step 5: Diagonally dominant arrangement.**
We have two equations:
1. $35V_C - 15V_R = 360$ (row 1: $|35| > |-15|$, dominant in $V_C$)
2. $V_C + 2V_R = 30$ (row 2: $|2| > |1|$, dominant in $V_R$)

Express the variables:

$$
V_C^{(k+1)} = \frac{360 + 15V_R^{(k)}}{35}
$$

$$
V_R^{(k+1)} = \frac{30 - V_C^{(k+1)}}{2}
$$

**Step 6: Gauss-Seidel iterations.**
Start from $V_C^{(0)} = 0$, $V_R^{(0)} = 0$:

| $k$ | $V_C$ | $V_R$ |
| ---: | --: | --: |
| 0 | 0.000000 | 0.000000 |
| 1 | 10.285714 | 9.857143 |
| 2 | 14.510204 | 7.744898 |
| 3 | 13.604956 | 8.197522 |
| 4 | 13.798938 | 8.100531 |
| 5 | 13.757370 | 8.121315 |
| 6 | 13.766278 | 8.116861 |
| 7 | 13.764369 | 8.117815 |
| 8 | 13.764778 | 8.117611 |

**Step 7: Compute $I_0$.**

$$
I_0 = \frac{30 - 13.764778}{10} = \frac{16.235222}{10} = 1.6235\text{ A}
$$

$$
\boxed{I_0 = 1.6235 \text{ A}, \quad V_C = 13.7648 \text{ V}, \quad V_R = 8.1176 \text{ V}}
$$

---

### 🎯 Use the Gauss Seidel method with relaxation $(\lambda = 0.95)$ to solve the following system. If necessary rearrange the equations to achieve convergence (use 3 iterations only).
> **Appeared:** 2017 Q.4(c) — (05 marks)

**Full Answer:**

Given system:

$$
\begin{aligned}
-3x_1 + x_2 + 12x_3 &= 50 \\
6x_1 - x_2 - x_3 &= 3 \\
6x_1 + 9x_2 + x_3 &= 40
\end{aligned}
$$

**Step 1: Check for diagonal dominance.**
- Row 1: $|{-3}| = 3 < |1| + |12| = 13$ (fails dominance)
- Row 2: $|{-1}| = 1 < |6| + |1| = 7$ (fails dominance)
- Row 3: $|9| = 9 > |6| + |1| = 7$ (dominant)

The original arrangement is not diagonally dominant.

**Step 2: Rearrange equations.**
1. Equation 2 as **Row 1** (solve for $x_1$): $|6| > |-1| + |-1| = 2$.
2. Equation 3 as **Row 2** (solve for $x_2$): $|9| > |6| + |1| = 7$.
3. Equation 1 as **Row 3** (solve for $x_3$): $|12| > |-3| + |1| = 4$.

The rearranged system:

$$
\begin{aligned}
6x_1 - x_2 - x_3 &= 3 \\
6x_1 + 9x_2 + x_3 &= 40 \\
-3x_1 + x_2 + 12x_3 &= 50
\end{aligned}
$$

**Step 3: Iteration formulas with relaxation $\lambda = 0.95$.**
First compute the raw Gauss-Seidel predictor $\hat{x}_i^{(k+1)}$:

$$
\hat x_1^{(k+1)} = \frac{3 + x_2^{(k)} + x_3^{(k)}}{6}
$$

$$
\hat x_2^{(k+1)} = \frac{40 - 6x_1^{(k+1)} - x_3^{(k)}}{9}
$$

$$
\hat x_3^{(k+1)} = \frac{50 + 3x_1^{(k+1)} - x_2^{(k+1)}}{12}
$$

Then apply relaxation:

$$
x_i^{(k+1)} = (1 - \lambda)x_i^{(k)} + \lambda \hat x_i^{(k+1)} = 0.05\,x_i^{(k)} + 0.95\,\hat x_i^{(k+1)}
$$

Start from $x^{(0)} = (0, 0, 0)$:

- **Iteration 1:**
  - $\hat x_1^{(1)} = \frac{3 + 0 + 0}{6} = 0.500000 \implies x_1^{(1)} = 0.95(0.500000) = 0.475000$
  - $\hat x_2^{(1)} = \frac{40 - 6(0.475000) - 0}{9} = 4.127778 \implies x_2^{(1)} = 0.95(4.127778) = 3.921389$
  - $\hat x_3^{(1)} = \frac{50 + 3(0.475000) - 3.921389}{12} = 3.958634 \implies x_3^{(1)} = 0.95(3.958634) = 3.760703$

- **Iteration 2:**
  - $\hat x_1^{(2)} = \frac{3 + 3.921389 + 3.760703}{6} = 1.780349 \implies x_1^{(2)} = 0.05(0.475000) + 0.95(1.780349) = 1.715081$
  - $\hat x_2^{(2)} = \frac{40 - 6(1.715081) - 3.760703}{9} = 2.883201 \implies x_2^{(2)} = 0.05(3.921389) + 0.95(2.883201) = 2.935111$
  - $\hat x_3^{(2)} = \frac{50 + 3(1.715081) - 2.935111}{12} = 4.350844 \implies x_3^{(2)} = 0.05(3.760703) + 0.95(4.350844) = 4.321337$

- **Iteration 3:**
  - $\hat x_1^{(3)} = \frac{3 + 2.935111 + 4.321337}{6} = 1.709408 \implies x_1^{(3)} = 0.05(1.715081) + 0.95(1.709408) = 1.709692$
  - $\hat x_2^{(3)} = \frac{40 - 6(1.709692) - 4.321337}{9} = 2.824501 \implies x_2^{(3)} = 0.05(2.935111) + 0.95(2.824501) = 2.830032$
  - $\hat x_3^{(3)} = \frac{50 + 3(1.709692) - 2.830032}{12} = 4.358254 \implies x_3^{(3)} = 0.05(4.321337) + 0.95(4.358254) = 4.356408$

| Iteration | $x_1$ | $x_2$ | $x_3$ |
| :--: | :-- | :-- | :-- |
| 0 | $0.000000$ | $0.000000$ | $0.000000$ |
| 1 | $0.475000$ | $3.921389$ | $3.760703$ |
| 2 | $1.715081$ | $2.935111$ | $4.321337$ |
| 3 | $1.709692$ | $2.830032$ | $4.356408$ |

$$
\boxed{x_1 \approx 1.7097, \qquad x_2 \approx 2.8300, \qquad x_3 \approx 4.3564}
$$

---

### 🎯 [CT-02B Q.1(a)] Rearrange the equations in a suitable form for the Gauss-Seidel iterative method.
> **Appeared:** CT-02B Q.1(a)

Given system:

$$
4x + y + z = 7, \qquad x + 5y + 2z = -8, \qquad 2x + y + 6z = 6
$$

**Full Answer:**

Solve each equation for its own diagonal unknown:

$$
x = \frac{7 - y - z}{4}, \qquad y = \frac{-8 - x - 2z}{5}, \qquad z = \frac{6 - 2x - y}{6}
$$

**Check that the system is suitable:**
The diagonal entries are $4, 5, 6$ and the off-diagonal row sums are $2, 3, 3$. Every row is strictly diagonally dominant:

$$
\lvert 4\rvert > 1 + 1 = 2, \qquad \lvert 5\rvert > 1 + 2 = 3, \qquad \lvert 6\rvert > 2 + 1 = 3
$$

Strict dominance of every row guarantees convergence from any starting vector. $\det A = 101 \ne 0$, so the solution is unique.

**The Gauss-Seidel form with proper ordering:**

$$
x^{(k+1)} = \frac{7 - y^{(k)} - z^{(k)}}{4}
$$

$$
y^{(k+1)} = \frac{-8 - x^{(k+1)} - 2z^{(k)}}{5}
$$

$$
z^{(k+1)} = \frac{6 - 2x^{(k+1)} - y^{(k+1)}}{6}
$$

---

### 🎯 [CT-02B Q.1(b)] Starting with $x_0 = 0$, $y_0 = 0$, $z_0 = 0$, perform four complete iterations using the Gauss-Seidel method.
> **Appeared:** CT-02B Q.1(b)

**Full Answer:**

**Iteration 1**, from $(0, 0, 0)$:

$$
x_1 = \frac{7 - 0 - 0}{4} = 1.75
$$

$$
y_1 = \frac{-8 - 1.75 - 2(0)}{5} = \frac{-9.75}{5} = -1.95
$$

$$
z_1 = \frac{6 - 2(1.75) - (-1.95)}{6} = \frac{6 - 3.5 + 1.95}{6} = \frac{4.45}{6} = 0.741667
$$

**Iteration 2:**

$$
x_2 = \frac{7 - (-1.95) - 0.741667}{4} = \frac{8.208333}{4} = 2.052083
$$

$$
y_2 = \frac{-8 - 2.052083 - 2(0.741667)}{5} = \frac{-11.535417}{5} = -2.307083
$$

$$
z_2 = \frac{6 - 2(2.052083) - (-2.307083)}{6} = \frac{4.202917}{6} = 0.700486
$$

**Iteration 3:**

$$
x_3 = \frac{7 - (-2.307083) - 0.700486}{4} = \frac{8.606597}{4} = 2.151649
$$

$$
y_3 = \frac{-8 - 2.151649 - 2(0.700486)}{5} = \frac{-11.552621}{5} = -2.310524
$$

$$
z_3 = \frac{6 - 2(2.151649) - (-2.310524)}{6} = \frac{4.007225}{6} = 0.667871
$$

**Iteration 4:**

$$
x_4 = \frac{7 - (-2.310524) - 0.667871}{4} = \frac{8.642653}{4} = 2.160663
$$

$$
y_4 = \frac{-8 - 2.160663 - 2(0.667871)}{5} = \frac{-11.496405}{5} = -2.299281
$$

$$
z_4 = \frac{6 - 2(2.160663) - (-2.299281)}{6} = \frac{3.977955}{6} = 0.662992
$$

**Summary of the four iterations:**

| $k$ | $x$ | $y$ | $z$ |
| :--: | --: | --: | --: |
| 1 | 1.750000 | -1.950000 | 0.741667 |
| 2 | 2.052083 | -2.307083 | 0.700486 |
| 3 | 2.151649 | -2.310524 | 0.667871 |
| 4 | 2.160663 | -2.299281 | 0.662992 |

$$
\boxed{(x_4, y_4, z_4) = (2.160663,\ -2.299281,\ 0.662992)}
$$

---

### 🎯 [CT-02B Q.1(c)] Calculate the absolute error in $x$, $y$, and $z$ between the third and fourth iterations.
> **Appeared:** CT-02B Q.1(c)

**Full Answer:**

The absolute errors are the differences between consecutive iterates:

$$
\lvert x_4 - x_3\rvert = \lvert 2.160663 - 2.151649\rvert = 0.009014
$$

$$
\lvert y_4 - y_3\rvert = \lvert -2.299281 - (-2.310524)\rvert = 0.011243
$$

$$
\lvert z_4 - z_3\rvert = \lvert 0.662992 - 0.667871\rvert = 0.004879
$$

$$
\boxed{\lvert\Delta x\rvert = 0.009014, \quad \lvert\Delta y\rvert = 0.011243, \quad \lvert\Delta z\rvert = 0.004879}
$$

---

## ⚡ Exam Tips & Common Mistakes

1. **Always check diagonal dominance first.** If $|a_{ii}| \le \sum_{j \ne i} |a_{ij}|$, swap rows until each diagonal entry is the largest in its row. If you skip this, your iterations may diverge.
2. **Current sources remove mesh variables.** An ideal current source on the boundary pins that mesh current to a fixed constant. Do not iterate it. Write it down immediately.
3. **Use the freshest values immediately.** When calculating $y^{(k+1)}$, use $x^{(k+1)}$, not $x^{(k)}$. Using old values everywhere turns your solution into Jacobi iteration and costs marks.
4. **Sign errors in negative terms.** When computing $x = \frac{7 - y - z}{4}$ and $y$ is negative, $7 - (-1.95) = 7 + 1.95$. Double-check signs on your calculator.
5. **Keep at least 6 decimal places in working tables.** Rounding intermediate numbers to 2 or 3 decimals introduces artificial error that corrupts convergence.

## 🔗 Related Topics

- [NM-3.2: Pivoting](NM-3.2_Pivoting.md) — direct elimination counterpart where row interchanges ensure numerical stability
- [NM-3.8: Circuit Applications](NM-3.8_Circuit_Applications.md) — formulating mesh and nodal equations before numerical solution
- [NM-3_Lower: Gauss Elimination, LU, Jacobi, Relaxation](NM-3_Lower_Gauss_Elim_LU_Jacobi_Relaxation.md) — Jacobi iteration and relaxation fundamentals

---

[← Previous: NM-3.2 Pivoting](NM-3.2_Pivoting.md) | [🏠 Index](00_Index.md) | [Next: NM-3.8 Circuit Applications →](NM-3.8_Circuit_Applications.md)
