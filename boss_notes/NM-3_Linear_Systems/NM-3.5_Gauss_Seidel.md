[← Previous: NM-3.4 Jacobi Iteration](NM-3.4_Jacobi_Iteration.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: NM-3.6 Relaxation →](NM-3.6_Relaxation.md)

---

# NM-3.5: Gauss-Seidel Iteration

> 🔴 ⚠️ **Priority:** Highest in Numerical Linear Algebra | **Tested:** 7/8 years | **Typical marks:** 5–6

## What This Is (and Why It Matters)

In [NM-3.4](NM-3.4_Jacobi_Iteration.md), we saw Jacobi iteration: you update all your variables using only numbers from the previous round. But think about how unnatural that feels: if you just calculated an improved estimate for $x_1$, why on earth would you ignore it and use the old, outdated $x_1$ when calculating $x_2$?

You wouldn't! The moment you compute a fresher, better number, you plug it straight into the next equation.

That intuitive upgrade is the **Gauss-Seidel Method** (also known as the *method of successive displacements*). By recycling freshly computed numbers on the fly, Gauss-Seidel converges roughly **twice as fast** as Jacobi, requires less computer memory, and is the absolute favorite tool for solving electrical networks and boundary-value PDEs.

In RUET examinations, Gauss-Seidel is tested in almost every semester final. Examiners almost always disguise it as a **DC circuit problem**: they draw a network with 2 to 4 loops or nodes, ask you to formulate the KVL or KCL equations, and tell you to run Gauss-Seidel iterations. If you know the two circuit tricks (how to handle current sources and keep your row ordering strictly dominant), this is the easiest full marks on the paper.

---

## 📝 Key Definitions

> **Iterative Methods:** "We shall now describe the *iterative* or *indirect* methods, which start from an *approximation* to the true solution and, if convergent, derive a sequence of closer approximations, *the cycle of computations being repeated till the required accuracy is obtained*." -- Jain, §7.6 (p. 279)
> 
> **In simple words:** Instead of doing a rigid row elimination, you start with a ballpark guess and cycle through an update recipe until the numbers stop changing.

> **Gauss-Seidel Method (Successive Displacements):** "It is clear, therefore, that this method uses an improved component as soon as it is available and it is called the *method of successive displacements*, or the *Gauss–Seidel method*." -- Jain, §7.6 (p. 281)
> 
> **In simple words:** As soon as you finish computing a new value for any variable, you plug it into every following equation immediately in that same round.

> **Strict Diagonal Dominance Rule:** "provided that $\sum_{j=1, \, j \ne i}^n \left| \frac{a_{ij}}{a_{ii}} \right| < 1, \quad (i = 1, 2, \dots, n)$." -- Jain, §7.6 (p. 281)
> 
> **In simple words:** For every equation, the diagonal number must be strictly larger in magnitude than all other coefficients in that row combined. This guarantees convergence no matter what starting guess you pick.

---

## The Core Idea

### The Gauss-Seidel Update Equation
Consider an $n \times n$ system $A\mathbf{x} = \mathbf{b}$:
$$
\begin{aligned}
a_{11}x_1 + a_{12}x_2 + \dots + a_{1n}x_n &= b_1 \\
a_{21}x_1 + a_{22}x_2 + \dots + a_{2n}x_n &= b_2 \\
&\;\;\vdots \\
a_{n1}x_1 + a_{n2}x_2 + \dots + a_{nn}x_n &= b_n
\end{aligned}
$$

Solve equation $i$ for its diagonal unknown $x_i$:
$$
x_i = \frac{1}{a_{ii}}\left(b_i - \sum_{j=1}^{i-1} a_{ij}x_j - \sum_{j=i+1}^n a_{ij}x_j\right)
$$

Now look at the iteration superscripts:
$$
x_i^{(k+1)} = \frac{1}{a_{ii}}\left(b_i - \sum_{j=1}^{i-1} a_{ij} x_j^{(k+1)} - \sum_{j=i+1}^n a_{ij} x_j^{(k)}\right)
$$
Look at that split:
- For $j < i$ (variables already updated in this round), we use the **new values** $x_j^{(k+1)}$.
- For $j > i$ (variables not yet updated in this round), we use the **old values** $x_j^{(k)}$.

### For a $3 \times 3$ System:
$$
x^{(k+1)} = \frac{b_1 - a_{12}y^{(k)} - a_{13}z^{(k)}}{a_{11}}
$$
$$
y^{(k+1)} = \frac{b_2 - a_{21}x^{(k+1)} - a_{23}z^{(k)}}{a_{22}} \quad \longleftarrow \text{uses newly computed } x^{(k+1)}!
$$
$$
z^{(k+1)} = \frac{b_3 - a_{31}x^{(k+1)} - a_{32}y^{(k+1)}}{a_{33}} \quad \longleftarrow \text{uses newly computed } x^{(k+1)} \text{ and } y^{(k+1)}!
$$

### The Two Golden Rules for Circuit Analysis in RUET Exams

1. **The Boundary Current Source Rule:**  
   If an ideal independent current source sits on an outer boundary branch of mesh $k$, **that mesh current is already locked in!**
   $$
   I_k = \pm I_{\text{source}}
   $$
   Never write a KVL equation around that mesh! The voltage across a current source is unknown. You simply set $I_k$ as a constant and plug it into adjacent mesh equations. This reduces the number of unknowns by one.

2. **The Diagonal Dominance Rearrangement Rule:**  
   Gauss-Seidel only converges if each equation is solved for the variable with the largest coefficient in that row. If your natural circuit equations do not satisfy $|a_{ii}| > \sum_{j \ne i} |a_{ij}|$, you **must swap equations** before iterating. Solving the wrong equation for a variable causes the numbers to oscillate wildly and explode to infinity!

---

## 🔧 Worked Example (The Master Circuit Problem: 2020 Q.4(b))

> **The question:** Solve for $I_1$, $I_2$, and $I_3$ in the circuit below using the Gauss-Seidel method.
> 
> ![Three-mesh DC resistive network with a 400 V source, 20, 40, 10 and 100 ohm resistors, and a downward 10 A current source, with clockwise mesh currents I1, I2, I3](../diagrams/nm3_gs_circuit_2020_three_mesh.jpg)
> 
> *(Source: 2020 Q.4(b) [Marks: 06])*

**Let's solve this step by step.**

### Step 1: Identify Fixed Mesh Currents
Look at Mesh 3 (the rightmost loop): its outer branch holds a $10\text{ A}$ current source pointing downward. Taking clockwise mesh currents:
$$
I_3 = 10\text{ A}
$$
$I_3$ is a known constant. It is not an unknown to be iterated! It stays $10\text{ A}$ from start to finish.

### Step 2: Formulate KVL Equations for Mesh 1 and Mesh 2
- **Mesh 1 (clockwise):**  
  The $400\text{ V}$ source opposes the clockwise current (drops from $+$ to $-$):
  $$
  -400 + 20I_1 + 40(I_1 - I_2) = 0
  $$
  Combine like terms:
  $$
  60I_1 - 40I_2 = 400
  $$

- **Mesh 2 (clockwise):**  
  Traverse through the $40\,\Omega$, $10\,\Omega$, and $100\,\Omega$ resistors:
  $$
  40(I_2 - I_1) + 10I_2 + 100(I_2 - I_3) = 0
  $$
  Substitute the known constant $I_3 = 10\text{ A}$:
  $$
  -40I_1 + 150I_2 - 100(10) = 0 \implies -40I_1 + 150I_2 = 1000
  $$

### Step 3: Check Diagonal Dominance and Form Iteration Formulas
Let's inspect our $2 \times 2$ system:
- **Row 1:** $|60| > |-40| = 40$ (Strictly dominant in $I_1$ $\checkmark$)
- **Row 2:** $|150| > |-40| = 40$ (Strictly dominant in $I_2$ $\checkmark$)

Both rows are strictly diagonally dominant. Now isolate each unknown:
$$
I_1^{(k+1)} = \frac{400 + 40I_2^{(k)}}{60}
$$
$$
I_2^{(k+1)} = \frac{1000 + 40I_1^{(k+1)}}{150}
$$

### Step 4: Run the Gauss-Seidel Sweeps
Start with initial guess $I_1^{(0)} = 0$, $I_2^{(0)} = 0$ (and $I_3 = 10\text{ A}$ fixed):

- **Sweep 1:**
$$
I_1^{(1)} = \frac{400 + 40(0)}{60} = \frac{400}{60} = 6.666667\text{ A}
$$
Now plug this fresh $I_1^{(1)} = 6.666667$ immediately into the equation for $I_2$:
$$
I_2^{(1)} = \frac{1000 + 40(6.666667)}{150} = \frac{1000 + 266.66668}{150} = 8.444444\text{ A}
$$

- **Sweep 2:**
$$
I_1^{(2)} = \frac{400 + 40(8.444444)}{60} = \frac{400 + 337.77776}{60} = 12.296296\text{ A}
$$
Plug in fresh $I_1^{(2)}$:
$$
I_2^{(2)} = \frac{1000 + 40(12.296296)}{150} = \frac{1000 + 491.85184}{150} = 9.945679\text{ A}
$$

### Complete Iteration Sweep Table

| Sweep ($k$) | $I_1$ (A) | $I_2$ (A) | $I_3$ (A) |
| :--: | :-- | :-- | :-- |
| **0** | $0.000000$ | $0.000000$ | $10.0000$ (fixed) |
| **1** | $6.666667$ | $8.444444$ | $10.0000$ |
| **2** | $12.296296$ | $9.945679$ | $10.0000$ |
| **3** | $13.297119$ | $10.212565$ | $10.0000$ |
| **4** | $13.475043$ | $10.260012$ | $10.0000$ |
| **5** | $13.506674$ | $10.268447$ | $10.0000$ |
| **6** | $13.512298$ | $10.269946$ | $10.0000$ |
| **7** | $13.513297$ | $10.270213$ | $10.0000$ |
| **8** | $13.513475$ | $10.270260$ | $10.0000$ |
| **9** | $13.513507$ | $10.270268$ | $10.0000$ |
| **10** | $13.513512$ | $10.270270$ | $10.0000$ |

By sweep 8, the numbers have stabilized completely.

$$
\boxed{I_1 = 13.5135 \text{ A}, \qquad I_2 = 10.2703 \text{ A}, \qquad I_3 = 10.0000 \text{ A}}
$$

**Sanity check:** Solving the $2 \times 2$ system directly:
$$
60I_1 - 40I_2 = 400 \implies 3I_1 - 2I_2 = 20 \implies I_1 = \frac{20 + 2I_2}{3}
$$
$$
-4I_1 + 15I_2 = 100 \implies -4\left(\frac{20 + 2I_2}{3}\right) + 15I_2 = 100 \implies -80 - 8I_2 + 45I_2 = 300
$$
$$
37I_2 = 380 \implies I_2 = \frac{380}{37} \approx 10.2703\text{ A}
$$
$$
I_1 = \frac{20 + 2(10.2703)}{3} = \frac{40.5405}{3} \approx 13.5135\text{ A}
$$
The analytical solution matches our iterative result to four decimal places!

---

## 🏆 Past Exam Questions

### 2024 Q.2(b): Three-Mesh Circuit with 500 V and 5 A Sources -- [04 marks]

**The question:** Solve $I_1$, $I_2$ and $I_3$ using the Gauss-Seidel method.

![Planar three-mesh DC resistive network with a 500 V source, 10, 20 and 100 ohm resistors, and a 5 A source, with clockwise mesh currents I1, I2, I3](../diagrams/nm3_gs_circuit_2024_three_mesh.jpg)

**Tutor explanation & structured answer:**

**1. Mesh Equations (clockwise traversal):**
- **Mesh 3:** Outer right branch contains a $5\text{ A}$ current source aligned clockwise:
$$
I_3 = 5\text{ A}
$$
- **Mesh 1:** Traverses $500\text{ V}$ source, $10\,\Omega$, and shared $20\,\Omega$:
$$
-500 + 10I_1 + 20(I_1 - I_2) = 0 \implies 30I_1 - 20I_2 = 500
$$
- **Mesh 2:** Traverses shared $20\,\Omega$ and shared $100\,\Omega$:
$$
20(I_2 - I_1) + 100(I_2 - I_3) = 0 \implies -20I_1 + 120I_2 - 100(5) = 0 \implies -20I_1 + 120I_2 = 500
$$

**2. Form Gauss-Seidel Update Formulas:**
- Row 1 ($|30| > |-20|$):
$$
I_1^{(k+1)} = \frac{500 + 20I_2^{(k)}}{30}
$$
- Row 2 ($|120| > |-20|$):
$$
I_2^{(k+1)} = \frac{500 + 20I_1^{(k+1)}}{120} = \frac{20I_1^{(k+1)} + 100(5)}{120}
$$

**3. Iteration Table starting from $I_1^{(0)} = 0, I_2^{(0)} = 0$ (with $I_3 = 5\text{ A}$ fixed):**

| Iteration | $I_1$ (A) | $I_2$ (A) | $I_3$ (A) |
| :--: | :-- | :-- | :-- |
| 0 | 0 | 0 | 5.000000 |
| 1 | 16.666667 | 6.944444 | 5.000000 |
| 2 | 21.296296 | 7.716049 | 5.000000 |
| 3 | 21.810700 | 7.801783 | 5.000000 |
| 4 | 21.867856 | 7.811309 | 5.000000 |
| 5 | 21.874206 | 7.812368 | 5.000000 |
| 6 | 21.874912 | 7.812485 | 5.000000 |

Detailed Sweep 1:
$$
I_1^{(1)} = \frac{500 + 20(0)}{30} = \frac{50}{3} \approx 16.666667\text{ A}
$$
$$
I_2^{(1)} = \frac{20(16.666667) + 500}{120} = \frac{333.33334 + 500}{120} = \frac{125}{18} \approx 6.944444\text{ A}
$$

The changes drop by roughly a factor of 4 per iteration. By sweep 6, the values have settled:
$$
\boxed{I_1 \approx 21.875 \text{ A}, \quad I_2 \approx 7.8125 \text{ A}, \quad I_3 = 5 \text{ A}}
$$

> [!WARNING] Why $I_3 = 5$ at row 0 and not 0
> $I_3$ is a physical constant set by the current source. Setting $I_3 = 0$ at sweep 0 would contradict circuit law and distort the first sweep calculation of $I_2$.

---

### 2018 Q.4(b): Four-Mesh DC Circuit -- [05 marks]

**The question:** Solve the following circuit by using Gauss-Seidel method.

![Four-mesh DC circuit with independent 100 V source, 10 A current source, and five resistors](../diagrams/nm3_gs_circuit_2018_four_mesh.jpg)

**Tutor explanation & structured answer:**

**1. Constraint:** The top branch of Mesh 2 contains an independent $10\text{ A}$ current source directed leftward. Taking clockwise mesh currents:
$$
I_2 = -10\text{ A}
$$

**2. Formulate KVL for Remaining Meshes:**
- **Mesh 1:** $10I_1 + 20(I_1 - I_2) + 25(I_1 - I_4) = 0 \implies 55I_1 - 25I_4 = 20(-10) = -200$
- **Mesh 3:** $8I_3 + 25(I_3 - I_2) + 4(I_3 - I_4) = 0 \implies 37I_3 - 4I_4 = 25(-10) = -250$
- **Mesh 4:** $25(I_4 - I_1) + 4(I_4 - I_3) = 100 \implies -25I_1 - 4I_3 + 29I_4 = 100$

**3. Gauss-Seidel Update Formulas:**
$$
I_1^{(k+1)} = \frac{-200 + 25I_4^{(k)}}{55}
$$
$$
I_3^{(k+1)} = \frac{-250 + 4I_4^{(k)}}{37}
$$
$$
I_4^{(k+1)} = \frac{100 + 25I_1^{(k+1)} + 4I_3^{(k+1)}}{29}
$$

**4. Iteration Table starting from $I_1^{(0)} = I_3^{(0)} = I_4^{(0)} = 0$:**

| Sweep | $I_1$ (A) | $I_3$ (A) | $I_4$ (A) |
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
I_1 = -\frac{14390}{3501} \approx -4.1103\text{ A}, \quad I_3 = -\frac{24050}{3501} \approx -6.8695\text{ A}, \quad I_4 = -\frac{3650}{3501} \approx -1.0426\text{ A}
$$

$$
\boxed{I_1 = -4.1103\ \text{A}, \quad I_2 = -10\ \text{A}, \quad I_3 = -6.8695\ \text{A}, \quad I_4 = -1.0426\ \text{A}}
$$

---

### 2019 Q.3(c): Two-Node Circuit Nodal Analysis -- [04 marks]

**The question:** Obtain the nodal equations from the following circuit. Hence solve for the unknowns using Gauss-Seidel iterative method. Show two iterations only.

![Two-node DC resistive network with 5 A and 10 A current sources, and three resistors](../diagrams/nm3_gs_circuit_2019_nodal.jpg)

**Tutor explanation & structured answer:**

**1. KCL at Node 1:**  
Summing currents leaving node 1 (reference ground at bottom rail):
$$
\frac{V_1}{2} + \frac{V_1 - V_2}{4} - 5 = 0
$$
Multiply by 4:
$$
2V_1 + V_1 - V_2 - 20 = 0 \implies \boxed{3V_1 - V_2 = 20}
$$

**2. KCL at Node 2:**  
Summing currents leaving node 2:
$$
\frac{V_2}{6} + \frac{V_2 - V_1}{4} + 5 = 10 \implies \frac{V_2}{6} + \frac{V_2 - V_1}{4} = 5
$$
Multiply by 12:
$$
2V_2 + 3(V_2 - V_1) + 60 = 120 \implies \boxed{-3V_1 + 5V_2 = 60}
$$

**3. Gauss-Seidel Equations:**  
Row 1 has $|3| > |-1|$, Row 2 has $|5| > |-3|$. The system is strictly diagonally dominant:
$$
V_1^{(k+1)} = \frac{20 + V_2^{(k)}}{3}, \qquad V_2^{(k+1)} = \frac{60 + 3V_1^{(k+1)}}{5}
$$

**4. Perform Two Iterations from $(V_1^{(0)} = 0, V_2^{(0)} = 0)$:**
- **Iteration 1:**
$$
V_1^{(1)} = \frac{20 + 0}{3} = 6.666667\text{ V}
$$
$$
V_2^{(1)} = \frac{60 + 3(6.666667)}{5} = \frac{80}{5} = 16.000000\text{ V}
$$
- **Iteration 2:**
$$
V_1^{(2)} = \frac{20 + 16.000000}{3} = \frac{36}{3} = 12.000000\text{ V}
$$
$$
V_2^{(2)} = \frac{60 + 3(12.000000)}{5} = \frac{96}{5} = 19.200000\text{ V}
$$

Exact solution for reference: $4V_2 = 80 \implies V_2 = 20\text{ V}, 3V_1 = 40 \implies V_1 = 13.3333\text{ V}$.
$$
\boxed{V_1 = 13.3333\ \text{V}, \qquad V_2 = 20\ \text{V}}
$$

---

### 2021 Q.7(b): Circuit with Dependent Voltage Source $5I_0$ -- [06 marks, CO: 2]

**The question:** Determine the value of $I_0$ in the given circuit using Gauss-Seidel method.

![DC circuit with independent 30 V source, four resistors, and dependent voltage source 5I0](../diagrams/nm3_gs_circuit_2021_dependent_source.jpg)

**Tutor explanation & structured answer:**

**1. Label Nodes & Relate Dependent Source:**  
Take the bottom wire as reference ground ($0\text{ V}$). The top rail is fixed at $V_T = 30\text{ V}$.  
- Controlling current $I_0$ runs through the $10\,\Omega$ resistor from top rail to centre node $V_C$:
$$
I_0 = \frac{30 - V_C}{10}
$$
- The dependent voltage source drives right node $V_R$ with respect to ground:
$$
V_R = 5I_0 = 5\left(\frac{30 - V_C}{10}\right) = 15 - 0.5V_C \implies V_C + 2V_R = 30
$$

**2. KCL at Centre Node $V_C$:**
$$
\frac{V_C - 30}{10} + \frac{V_C}{15} + \frac{V_C - V_R}{8} = 0
$$
Multiply by 120:
$$
12(V_C - 30) + 8V_C + 15(V_C - V_R) = 0 \implies 35V_C - 15V_R = 360
$$

**3. Diagonally Dominant Ordering:**
- Equation 1: $35V_C - 15V_R = 360$ ($|35| > |-15|$, dominant in $V_C$)
- Equation 2: $V_C + 2V_R = 30$ ($|2| > |1|$, dominant in $V_R$)

Iteration formulas:
$$
V_C^{(k+1)} = \frac{360 + 15V_R^{(k)}}{35}, \qquad V_R^{(k+1)} = \frac{30 - V_C^{(k+1)}}{2}
$$

Starting from $(0, 0)$, the sweeps converge to $V_C = \frac{234}{17} \approx 13.7648\text{ V}$ and $V_R = \frac{138}{17} \approx 8.1176\text{ V}$.  
Computing branch current $I_0$:
$$
I_0 = \frac{30 - 13.7648}{10} = 1.6235\text{ A}
$$

$$
\boxed{I_0 = 1.6235 \text{ A}, \quad V_C = 13.7648 \text{ V}, \quad V_R = 8.1176 \text{ V}}
$$

---

### CT-02B Q.1(a–c): Rearrangement, 4 Iterations, and Absolute Error

**The system:**
$$
4x + y + z = 7, \qquad x + 5y + 2z = -8, \qquad 2x + y + 6z = 6
$$

**Part (a): Rearrange in suitable form for Gauss-Seidel.**  
The diagonals are $4, 5, 6$. Strict diagonal dominance holds:
- $|4| > 1 + 1 = 2 \quad \checkmark$
- $|5| > 1 + 2 = 3 \quad \checkmark$
- $|6| > 2 + 1 = 3 \quad \checkmark$
Update formulas:
$$
x^{(k+1)} = \frac{7 - y^{(k)} - z^{(k)}}{4}, \quad y^{(k+1)} = \frac{-8 - x^{(k+1)} - 2z^{(k)}}{5}, \quad z^{(k+1)} = \frac{6 - 2x^{(k+1)} - y^{(k+1)}}{6}
$$

**Part (b): Four complete iterations from $(0, 0, 0)$:**

| Sweep | $x$ | $y$ | $z$ |
| :--: | --: | --: | --: |
| 1 | 1.750000 | -1.950000 | 0.741667 |
| 2 | 2.052083 | -2.307083 | 0.700486 |
| 3 | 2.151649 | -2.310524 | 0.667871 |
| 4 | 2.160663 | -2.299281 | 0.662992 |

$$
\boxed{(x_4, y_4, z_4) = (2.160663,\ -2.299281,\ 0.662992)}
$$

**Part (c): Absolute error between 3rd and 4th iterations:**
$$
|\Delta x| = |2.160663 - 2.151649| = 0.009014
$$
$$
|\Delta y| = |-2.299281 - (-2.310524)| = 0.011243
$$
$$
|\Delta z| = |0.662992 - 0.667871| = 0.004879
$$

$$
\boxed{\lvert\Delta x\rvert = 0.009014, \quad \lvert\Delta y\rvert = 0.011243, \quad \lvert\Delta z\rvert = 0.004879}
$$

---

### Exam Variants at a Glance

| Year | Circuit / System Description | Key Result |
|:---|:---|:---|
| **2018 Q.4(b)** | 4-mesh DC network with $10\text{ A}$ source (05 marks) | $\boxed{I_1 = -4.1103\ \text{A}, \quad I_2 = -10\ \text{A}, \quad I_3 = -6.8695\ \text{A}, \quad I_4 = -1.0426\ \text{A}}$ |
| **2019 Q.3(c)** | 2-node DC network with 2 current sources (04 marks) | $\boxed{V_1 = 13.3333\ \text{V}, \qquad V_2 = 20\ \text{V}}$ |
| **2020 Q.4(b)** | 3-mesh DC network with $400\text{ V}$ & $10\text{ A}$ sources (06 marks) | $\boxed{I_1 = 13.5135 \text{ A}, \qquad I_2 = 10.2703 \text{ A}, \qquad I_3 = 10.0000 \text{ A}}$ |
| **2021 Q.7(b)** | DC network with dependent voltage source $5I_0$ (06 marks) | $\boxed{I_0 = 1.6235 \text{ A}, \quad V_C = 13.7648 \text{ V}, \quad V_R = 8.1176 \text{ V}}$ |
| **2024 Q.2(b)** | 3-mesh DC network with $500\text{ V}$ & $5\text{ A}$ sources (04 marks) | $\boxed{I_1 \approx 21.875 \text{ A}, \quad I_2 \approx 7.8125 \text{ A}, \quad I_3 = 5 \text{ A}}$ |
| **CT-02B** | $3\times3$ system 4 iterations and error analysis | $\boxed{(x_4, y_4, z_4) = (2.160663,\ -2.299281,\ 0.662992)}$ |

---

## ⚡ Quick Review

**The method in one sentence:** Solve each row for its own diagonal variable, and immediately substitute freshly calculated values into subsequent equations within the same round.

**The update formula:**
$$
x_i^{(k+1)} = \frac{1}{a_{ii}}\left(b_i - \sum_{j=1}^{i-1} a_{ij} x_j^{(k+1)} - \sum_{j=i+1}^n a_{ij} x_j^{(k)}\right)
$$

**The two circuit non-negotiables:**
1. Boundary current sources pin mesh currents permanently ($I = \text{const}$). Do not iterate them.
2. Order equations to guarantee strict diagonal dominance ($|a_{ii}| > \sum_{j \ne i} |a_{ij}|$).

**Time estimate in exam:** ~10 to 12 minutes for setting up KVL/KCL equations and calculating 4 to 6 sweeps.

---

## 🔗 Connected Topics

- [← NM-3.4: Jacobi Iteration](NM-3.4_Jacobi_Iteration.md) -- the simultaneous predecessor that Gauss-Seidel speeds up.
- [→ NM-3.6: Relaxation](NM-3.6_Relaxation.md) -- using parameter $\lambda$ to steer Gauss-Seidel convergence step sizes.
- [NM-3.8: Circuit Applications](NM-3.8_Circuit_Applications.md) -- master reference on writing mesh and nodal equations from circuit schematics.

---

[← Previous: NM-3.4 Jacobi Iteration](NM-3.4_Jacobi_Iteration.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: NM-3.6 Relaxation →](NM-3.6_Relaxation.md)
