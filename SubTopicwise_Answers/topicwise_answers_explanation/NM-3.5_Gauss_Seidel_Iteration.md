---
title: "NM-3.5 · Gauss-Seidel Iteration"
tags:
  - numerical-methods
  - discrete-mathematics
  - topicwise
---





[🏠 Subtopic Index](00_Index.md) | [← Prev: NM-3.4 Jacobi Iteration](NM-3.4_Jacobi_Iteration.md) | [Next: NM-3.6 Relaxation →](NM-3.6_Relaxation.md)

---

# NM-3.5 · Gauss-Seidel Iteration

Every block below is copied from `../answers_explanation/`. The reasoning
is written once, in the year-wise file, and is not restated here.


### [2018 Q.4(b)]

**Question.** Solve the following circuit by using Gauss-Seidel method.

*[Marks: 05]*

**Solution.**

**The circuit.** A planar four-mesh network in a $2\times2$ arrangement, with
both a voltage source and a current source.

```text
                  10 Ω                       10 A (←)
         +-------/\/\/\/\-------+------------( ← )-----------+
         |        10 Ω          |           10 A              |
         |                      |                            |
         |                    [20 Ω]                         |
         |      (↻ I₁)          |            (↻ I₂)          |
         |                      |                            |
         +-------/\/\/\/\-------+------------/\/\/\/\--------+
         |        25 Ω          |             25 Ω           |
         |                      |                            |
       ( ↑ ) 100 V            [4 Ω]                        [8 Ω]
         |                      |                            |
         |      (↻ I₄)          |            (↻ I₃)          |
         |                      |                            |
         +----------------------+----------------------------+
```

Reading the four meshes off the drawing:

| Mesh | Boundary |
| :-- | :-- |
| $I_1$ top-left | $10\ \Omega$ top, shared $20\ \Omega$ right, shared $25\ \Omega$ bottom, wire left |
| $I_2$ top-right | $10\ \text{A}$ source top, wire right, shared $25\ \Omega$ bottom, shared $20\ \Omega$ left |
| $I_3$ bottom-right | shared $25\ \Omega$ top, shared $4\ \Omega$ left, $8\ \Omega$ right, wire bottom |
| $I_4$ bottom-left | shared $25\ \Omega$ top, shared $4\ \Omega$ right, $100\ \text{V}$ source left, wire bottom |

**Step 1, and this is the idea the question is built to test: the current
source removes an unknown.** The $10\ \text{A}$ source sits alone in the top
branch of mesh 2; no other mesh touches that branch. So the branch current is
$I_2$ exactly. Taking mesh currents clockwise, the source drives current
*anticlockwise* through it, so

$$I_2 = -10\ \text{A}$$

You now have three equations and three unknowns. Writing four mesh equations
plus the source equation would be five equations in four unknowns.

**Step 2, the three remaining mesh equations.** A shared branch carries the
difference of the two mesh currents, with the sign fixed by which way each mesh
walks it.

*Mesh 1*, clockwise: $10I_1$ across the top, $20(I_1 - I_2)$ down the shared
$20\ \Omega$, $25(I_1 - I_4)$ back along the shared $25\ \Omega$, and nothing
across the left wire:

$$10I_1 + 20(I_1 - I_2) + 25(I_1 - I_4) = 0 \implies 55I_1 - 25I_4 = 20I_2 = -200$$

*Mesh 3*, clockwise: $25(I_3 - I_2)$ along the shared $25\ \Omega$, $8I_3$ down
the right branch, $4(I_3 - I_4)$ up the shared $4\ \Omega$:

$$8I_3 + 25(I_3 - I_2) + 4(I_3 - I_4) = 0 \implies 37I_3 - 4I_4 = 25I_2 = -250$$

*Mesh 4*, clockwise: the $100\ \text{V}$ source is entered *against* the
traversal, so it contributes $-100$ as a drop; the two shared branches give
$25(I_4 - I_1)$ and $4(I_4 - I_3)$:

$$25(I_4 - I_1) + 4(I_4 - I_3) = 100 \implies -25I_1 - 4I_3 + 29I_4 = 100$$

**Step 3, put each equation in Gauss-Seidel form**, solving for its own
diagonal unknown:

$$I_1^{(k+1)} = \frac{-200 + 25I_4^{(k)}}{55}, \qquad I_3^{(k+1)} = \frac{-250 + 4I_4^{(k)}}{37}, \qquad I_4^{(k+1)} = \frac{100 + 25I_1^{(k+1)} + 4I_3^{(k+1)}}{29}$$

Note the ordering. $I_1$ and $I_3$ are computed from the *old* $I_4$, then $I_4$
is computed from the two values just obtained. That is what distinguishes
Gauss-Seidel from Jacobi, in which every update uses only values from the
previous sweep. Start from $I_1 = I_3 = I_4 = 0$.

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

**Step 4, the limit.** The iteration is converging, and eliminating the same
three equations gives the exact values

$$I_1 = -\frac{14390}{3501} = -4.1103\ \text{A}, \qquad I_3 = -\frac{24050}{3501} = -6.8695\ \text{A}, \qquad I_4 = -\frac{3650}{3501} = -1.0426\ \text{A}$$

$$\boxed{I_1 = -4.1103\ \text{A}, \quad I_2 = -10\ \text{A}, \quad I_3 = -6.8695\ \text{A}, \quad I_4 = -1.0426\ \text{A}}$$

> [!warning] Diagonal dominance, and why the convergence is slow
> Look at the third equation: $|29|$ against $|{-25}| + |{-4}| = 29$. The
> inequality holds with *equality*, so the system is only weakly diagonally
> dominant and the Gauss-Seidel iteration converges, but slowly. That is
> visible in the table: the correction per sweep falls by only about a factor
> of two per sweep at the start and does not visibly accelerate. On the first
> two equations the inequality is comfortable, $55 > 25$ and $37 > 4$, so the
> system is convergent overall. A student who expects eight sweeps to reach
> eight decimals has misread this row.
>
> The elimination result is exact and is the value to report; the iteration is
> what the question asked for as the method.

> [!info] The check that is worth more than the arithmetic
> Take the four currents into the three mesh equations at the four-decimal
> precision they are quoted to: $55(-4.1103) - 25(-1.0426) = -226.0665 +
> 26.0650 = -200.0015$; $37(-6.8695) - 4(-1.0426) = -254.1715 + 4.1704 =
> -250.0011$; $-25(-4.1103) - 4(-6.8695) + 29(-1.0426) = 102.7575 + 27.4780 -
> 30.2354 = 100.0001$. Each residual sits at $10^{-4}$, which is what rounding
> four numbers to four decimals must produce, and on the exact fractions all
> three return their right-hand sides with no residual at all.
>
> Then confirm with a different formulation entirely. Nodal analysis, with the
> left node held at $100\ \text{V}$ by the source and the bottom rail as
> reference, needs only three unknowns: the top-middle node, the central node
> and the top-right node. Their KCL equations are
> $\dfrac{v_{tm}-100}{10} + \dfrac{v_{tm}-v_c}{20} - 10 = 0$ (the $10$ leaves as
> the source current), $\dfrac{v_c - v_{tm}}{20} + \dfrac{v_c-100}{25} +
> \dfrac{v_c - v_{tr}}{25} + \dfrac{v_c}{4} = 0$, and
> $\dfrac{v_{tr}-v_c}{25} + \dfrac{v_{tr}}{8} + 10 = 0$. Solving gives
> $v_{tm} = 141.103\ \text{V}$, $v_c = 23.308\ \text{V}$, $v_{tr} = -54.956\ \text{V}$.
> Reading the mesh currents back out of those potentials,
> $I_1 = (100 - 141.103)/10 = -4.1103$ and $I_3 = -54.956/8 = -6.8695$, with
> $I_2 = -10$ from the source, agreeing to four digits.
>
> Two formulations that share no unknown and no equation reach the same
> currents. That is the strongest confirmation available, and it costs about a
> minute.

---

### [2019 Q.3(c)]

**Question.** Obtain the nodal equations from the following circuit. Hence solve for the unknowns using Gauss-Seidel iterative method. Show two iterations only.

*[Marks: 04]*

**Solution.**

**Circuit.** Two non-reference nodes, $V_1$ and $V_2$, with a common reference
ground. Node 1 connects to ground through $2\ \Omega$ and to node 2 through
$4\ \Omega$, with a $5\ \text{A}$ source entering node 1 through the top branch.
Node 2 connects to ground through $6\ \Omega$ and to node 1 through $4\ \Omega$,
with a $5\ \text{A}$ source leaving toward node 1 and a $10\ \text{A}$ source
entering node 2.

```text
                    5 A (enters Node 1)
                +-----------( <- )-----------+
                |                           |
          Node 1|            4 Ω            |Node 2
          ------+----------/\/\/\-----------+-------+
          |                                 |       |
          |                                 |       |
        [2 Ω]                             [6 Ω]   ( ^ ) 10 A
          |                                 |       |
          |                                 |       |
          +---------------------------------+-------+
                          Reference Ground
```

**KCL at node 1.** Currents leaving: through $2\ \Omega$ to ground, through
$4\ \Omega$ to node 2, and $5\ \text{A}$ back through the top branch.

$$\frac{V_1}{2} + \frac{V_1 - V_2}{4} - 5 = 0$$

Multiplying by 4:

$$2V_1 + V_1 - V_2 - 20 = 0 \implies \boxed{3V_1 - V_2 = 20}$$

**KCL at node 2.** Currents leaving: through $6\ \Omega$ to ground, through
$4\ \Omega$ to node 1, and $5\ \text{A}$ through the top branch. The $10\ \text{A}$
source enters, so it stands on the other side.

$$\frac{V_2}{6} + \frac{V_2 - V_1}{4} + 5 = 10$$

Multiplying by 12:

$$2V_2 + 3(V_2 - V_1) + 60 = 120 \implies \boxed{-3V_1 + 5V_2 = 60}$$

**Gauss-Seidel form.** Solve each equation for the diagonal unknown, and use the
most recent value of the other as soon as it is available.

$$V_1^{(k+1)} = \frac{20 + V_2^{(k)}}{3}, \qquad V_2^{(k+1)} = \frac{60 + 3V_1^{(k+1)}}{5}$$

The coefficient matrix is diagonally dominant, since $|3| > |-1|$ in the first row
and $|5| > |-3|$ in the second, so the iteration converges. Start from
$V_1^{(0)} = V_2^{(0)} = 0$.

| Iteration | $V_1^{(k+1)} = \dfrac{20 + V_2^{(k)}}{3}$ | $V_2^{(k+1)} = \dfrac{60 + 3V_1^{(k+1)}}{5}$ |
| :--: | :-- | :-- |
| 1 | $\dfrac{20 + 0}{3} = 6.666667$ | $\dfrac{60 + 3(6.666667)}{5} = 16.000000$ |
| 2 | $\dfrac{20 + 16}{3} = 12.000000$ | $\dfrac{60 + 3(12)}{5} = 19.200000$ |

Two iterations only, as required.

$$V_1^{(1)} = 6.666667\ \text{V}, \quad V_2^{(1)} = 16.000000\ \text{V}$$
$$V_1^{(2)} = 12.000000\ \text{V}, \quad V_2^{(2)} = 19.200000\ \text{V}$$

**The exact solution, for reference.** Adding the two equations eliminates $V_1$:

$$4V_2 = 80 \implies V_2 = 20\ \text{V}, \qquad 3V_1 = 40 \implies V_1 = 13.333333\ \text{V}$$

$$\boxed{V_1 = 13.3333\ \text{V}, \qquad V_2 = 20\ \text{V}}$$

> [!info] Check against the exact solution
> The iterates approach the exact pair from below in both components:
> $6.6667 \to 12 \to 13.0667 \to 13.28$ against $13.3333$, and
> $16 \to 19.2 \to 19.84 \to 19.968$ against $20$. The errors are
> $6.6667, 1.3333, 0.2667, 0.0533$ and $4, 0.8, 0.16, 0.032$, so each falls by a
> factor of exactly **five** per sweep.
>
> That factor is not an accident and it is worth deriving rather than accepting.
> The Jacobi iteration matrix is $T_J = \begin{bmatrix} 0 & 1/3 \\ 3/5 & 0 \end{bmatrix}$
> with spectral radius $\rho(T_J) = 1/\sqrt{5}$. For Gauss-Seidel, the iteration matrix is
> $T_{GS} = (D-L)^{-1}U = \begin{bmatrix} 0 & 1/3 \\ 0 & 1/5 \end{bmatrix}$, whose non-zero
> eigenvalue is $\lambda = 1/5 = \rho(T_J)^2$. The Gauss-Seidel spectral radius is therefore
> $\rho(T_{GS}) = 1/5$, which means the error contracts by a factor of exactly five in every sweep.
> Either way the recursion was written down the right way round, since a wrong ordering gives a
> spectral radius near or above one.

> [!warning] Where this exam meets the topic again
> The two-node Gauss-Seidel pattern above is the same construction used in
> **Q.8(b)**, where four interior nodes are solved instead of two. The only
> differences are that the equations come from a differential operator rather
> than from KCL, and that the neighbour values are boundary data rather than
> unknowns.

---

### [2020 Q.4(b), 2024 Q.2(b)]

**Appeared in:** 2020 Q.4(b), 2024 Q.2(b)

**Question.** Solve $I_1$, $I_2$ and $I_3$ using Gauss-Seidal method.

*[Marks: 06]*

**Solution.**

![Three-mesh DC resistive network with a 400 V source, 20, 40, 10 and 100 ohm resistors, and a downward 10 A current source, with clockwise mesh currents I1, I2, I3](../answers_exam_style/diagrams/2020_Q4b_circuit.jpg)
*Figure 2020 Q4(b): three-mesh DC circuit with an independent voltage source and an independent current source (Source: Page 1, Q4(b))*

**Step 1. Deal with the current source first.** Mesh 3 is bounded on the right by
an ideal $10$ A current source and on the left by the $100\ \Omega$ resistor
shared with mesh 2. A current source **fixes** the branch current, so the clockwise
mesh current is

$$I_3 = 10 \text{ A}$$

This is the step that trips people up. A current source in a branch forces $I_3$
to equal it, full stop, and it drops out of the system entirely.

> [!warning] A current source is not an unknown to be iterated
> Treating $I_3$ as a variable that starts at zero and converges contradicts the
> circuit. The source fixes the branch current, so $I_3$ is $10$ A in **every** row
> of the table, including row $0$.
>
> This is the third circuit in this set with a current source, and the same trap
> appears in 2021 Q.7(b) with a dependent source and in 2024 Q.2(b) with an
> independent one. **Read the circuit for sources that pin a variable before
> writing any iteration.** The tell is that the variable is fixed, so it never
> needs a column of its own.

**Step 2. Mesh 1, KVL.** Going clockwise around the left loop: rise $400$ V
through the source, drop across the $20\ \Omega$, then across the shared
$40\ \Omega$ which carries $I_1 - I_2$ because $I_2$ returns through it.

$$-400 + 20 I_1 + 40(I_1 - I_2) = 0$$

$$60 I_1 - 40 I_2 = 400$$

**Step 3. Mesh 2, KVL.** The $40\ \Omega$ carries $I_2 - I_1$, the $10\ \Omega$
carries $I_2$ alone, and the $100\ \Omega$ carries $I_2 - I_3$.

$$40(I_2 - I_1) + 10 I_2 + 100(I_2 - I_3) = 0$$

$$-40 I_1 + 150 I_2 = 100 I_3 = 1000$$

**Step 4. The system to iterate.** Three equations, but $I_3$ is already known, so
two unknowns remain:

$$
\begin{cases} 60 I_1 - 40 I_2 = 400 \\ -40 I_1 + 150 I_2 = 1000 \end{cases}
$$

Solve each for its own variable, newest value first:

$$
\begin{cases} I_1 = \dfrac{40 I_2 + 400}{60} \\[3mm] I_2 = \dfrac{1000 + 40 I_1}{150} \end{cases}
$$

**Step 5. Gauss-Seidel.** Use the value just computed, never the previous
iteration's. Start from $I_1^{(0)} = I_2^{(0)} = 0$.

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

Iteration 1: $I_1^{(1)} = \frac{40(0) + 400}{60} = 6.666667$, then
$I_2^{(1)} = \frac{1000 + 40(6.666667)}{150} = \frac{1000 + 266.6667}{150} = 8.444444$.

**Step 6. Answer.**

$$\boxed{I_1 = 13.5135 \text{ A}, \qquad I_2 = 10.2703 \text{ A}, \qquad I_3 = 10.0000 \text{ A}}$$

> [!info] Check by two independent routes
> **Exact solution.** The $2\times2$ system is solved directly by elimination:
> multiply the first equation by $150$ and the second by $40$, then add.
> $9000 I_1 - 6000 I_2 = 60000$ and $-1600 I_1 + 6000 I_2 = 40000$. Adding gives
> $7400 I_1 = 100000$, so
> $$I_1 = \frac{500}{37} = 13.513514, \qquad I_2 = \frac{380}{37} = 10.270270$$
> Both are exact rationals and the table is converging to them.
>
> **Diagonal dominance.** Row 1 has $|60|$ against $40$, and row 2 has $|150|$
> against $40$, so the matrix is strictly diagonally dominant and Gauss-Seidel is
> guaranteed to converge from any start. That check costs one line and it is what
> tells you the table is worth running.

> [!warning] The row order decides whether this converges
> The guarantee above depends on the order. Written as it is, the rows are
> $\begin{bmatrix} 60 & -40 \\ -40 & 150\end{bmatrix}$ and both are dominant.
> Swap them and row 1 becomes $\begin{bmatrix} -40 & 150\end{bmatrix}$, where
> $|40| < 150$, and the dominance is lost.
>
> In this case the reversed order still converges, because the coupling is mild.
> That is luck, not a property. **The same two-equation circuit with the current
> source on a different mesh diverges**, and the answer script's worked warning in
> 2021 Q.7(b) shows exactly that, with spectral radii $0.214$ and $4.67$.
>
> So check dominance before iterating, and if it fails, reorder rather than hope.

---

### [2021 Q.7(b)]

**Question.** Determine the value of $I_0$ in the given circuit using Gauss-Seidel method.

*[Marks: 06, CO: 2]*

**Solution.**

![DC circuit with a 30 V independent voltage source, 10, 15, 8 and 20 ohm resistors, and a dependent voltage source 5I0, with branch current I0 through the 10 ohm resistor](../answers_exam_style/diagrams/2021_Q7b_circuit.jpg)
*Figure 2021 Q7(b): DC circuit with independent 30 V source, four resistors, and dependent voltage source $5I_0$ (Source: Page 2, Q7(b))*

**Step 1. Name the nodes.** Take the bottom rail as reference, $0$ V.

| Node | Voltage |
| :-- | :-- |
| Top rail | $V_T = 30$ V, held by the ideal source |
| Centre node $C$ | $V_C$ |
| Right node $R$ | $V_R$ |

**Step 2. Express the controlling current.**

$$
I_0 = \frac{V_T - V_C}{10} = \frac{30 - V_C}{10}
$$

**Step 3. Apply the dependent source.** The $5I_0$ source sets the right node:

$$
V_R = 5I_0 = 5\left(\frac{30 - V_C}{10}\right) = 15 - 0.5V_C
$$

Rearranged, that is one equation ready for iteration:

$$
V_C + 2V_R = 30
$$

> [!warning] A dependent source is not an unknown to be iterated
> $V_R$ is **defined** as $5I_0$, and $I_0$ is defined by the $10\ \Omega$ branch.
> Neither is free. Treating $V_R$ as an unknown that starts at zero and converges
> contradicts the circuit: the dependent source fixes it exactly, from the first
> sweep onward.
>
> This is the same error as starting $I_3$ at zero in 2024 Q.2(b), where a $5$ A
> current source fixed a mesh current. **Read the circuit for sources that pin a
> variable before writing any iteration.**

**Step 4. KCL at node $C$.** Three branches leave it, toward the top rail, toward
ground, and toward node $R$:

$$
\frac{V_C - 30}{10} + \frac{V_C - 0}{15} + \frac{V_C - V_R}{8} = 0
$$

Multiplying by $120$,

$$
12(V_C - 30) + 8V_C + 15(V_C - V_R) = 0
$$

$$
12V_C - 360 + 8V_C + 15V_C - 15V_R = 0
$$

$$
35V_C - 15V_R = 360
$$

**Step 5. The system to iterate.**

$$
\begin{cases}
V_C = \dfrac{15V_R + 360}{35} \\[2mm]
V_R = \dfrac{30 - V_C}{2}
\end{cases}
$$

**Step 6. Gauss-Seidel.** Use the value just computed, never the previous
iteration's. Start from $V_C^{(0)} = V_R^{(0)} = 0$.

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

Iteration 1: $V_C^{(1)} = \frac{15(0) + 360}{35} = 10.285714$, then
$V_R^{(1)} = \frac{30 - 10.285714}{2} = 9.857143$.

**Step 7. Read off $I_0$.**

$$
I_0 = \frac{30 - 13.764778}{10} = \frac{16.235222}{10} = 1.6235 \text{ A}
$$

$$\boxed{I_0 = 1.6235 \text{ A}, \quad V_C = 13.7648 \text{ V}, \quad V_R = 8.1176 \text{ V}}$$

> [!warning] The $V_R$ column alternates, and that is not a sign of divergence
> $V_C$ values run high, low, high, low, $13.764778$ then $13.764690$. Gauss-Seidel
> overshoots one way then the other while it contracts, so the residual is **not**
> monotone even though the answer is.
>
> Judging convergence by "is the last step change small" therefore needs a
> tolerance, not an exact-match test. And a bracketing check on $I_0$ is the
> cheapest test of all: the answer must lie between the smallest and largest
> $I_0$ values the table produces, and it does.

> [!info] Check by two independent routes
> **Direct solution.** Eliminating $V_C$ from the two equations gives
> $V_C = \frac{234}{17} = 13.7647058824$ and $V_R = \frac{138}{17} = 8.1176470588$,
> so
> $$I_0 = \frac{30 - 234/17}{10} = \frac{138}{85} = 1.6235294118$$
> Iteration 8 gives $I_0 = 1.623522$, agreeing with the closed form to four
> decimals. The residual in $V_C$ is $7.2 \times 10^{-5}$ there, and it falls by a
> factor of about $4.6$ per sweep: iteration 10 gives $I_0 = 1.623529$ and
> iteration 12 gives $1.6235294$, matching the closed form to seven figures.
>
> **Consistency of the dependent source.** $5I_0 = 5(1.6235294) = 8.1176471$, and
> $V_R = \frac{138}{17} = 8.1176471$. The two agree, which they must, since
> $V_R$ was **defined** as $5I_0$.
>
> **KCL residual.** $\frac{V_C-30}{10} + \frac{V_C}{15} + \frac{V_C-V_R}{8} = 0$ exactly
> at the converged values.

> [!warning] The row order decides whether Gauss-Seidel converges at all
> Solve equation 2 first, $V_C = 30 - 2V_R$, and use equation 1 for $V_R$, and the
> iteration **diverges**:
> $V_C = 30.0$, then $-62.0$, then $367.3$, then $-1636.2$, then $7713.7$. The
> sequence grows without bound.
>
> The reason is visible in the diagonal of the coefficient matrix. Written in the
> order above, rows $35V_C - 15V_R = 360$ and $V_C + 2V_R = 30$, it is
> $$\begin{bmatrix} 35 & -15 \\ 1 & 2\end{bmatrix}$$
> with diagonal magnitudes $35$ and $2$ against off-diagonal sums $15$ and $1$.
> Both rows are strictly dominant, $35 > 15$ and $2 > 1$, which is what guarantees
> convergence in this ordering.
>
> Reversed, the rows become $\begin{bmatrix} 1 & 2 \\ 35 & -15\end{bmatrix}$, and
> now neither row is dominant: $1 < 2$ and $15 < 35$. That loss of dominance is
> exactly the divergence.
>
> The Gauss-Seidel iteration matrices confirm it. In the working order,
> $V_R^{(k+1)} = \frac{690 - 15V_R^{(k)}}{70}$, so the matrix is
> $$\begin{bmatrix} 0 & 15/35 \\ 0 & -15/70 \end{bmatrix}$$
> with spectral radius $\frac{15}{70} = 0.214 < 1$, so it converges. In the
> reversed order, $V_R^{(k+1)} = 46 - \frac{14}{3}V_R^{(k)}$, so the matrix is
> $$\begin{bmatrix} 0 & -2 \\ 0 & -14/3 \end{bmatrix}$$
> with spectral radius $\frac{14}{3} = 4.67 > 1$, which diverges.
>
> This is the same trap as the Gauss-Seidel questions in 2023 and 2024, and the
> fix is always the same: keep a diagonal-dominant ordering.

---

---

**Also asked here.**

- *2017 Q.4(c)* is the same question as [[NM-3.6_Relaxation|NM-3.6]], which is written in `NM-3.6`.

---

**Answered in phase P6, in `../CT_Questions/`.**

- *CT-02B Q.1(a)* is a class-test question. Its answer is in `../CT_Questions/CT_answers_exam_style.md`, with the reasoning in `../CT_Questions/CT_answers_explanation.md`.
- *CT-02B Q.1(b)* is a class-test question. Its answer is in `../CT_Questions/CT_answers_exam_style.md`, with the reasoning in `../CT_Questions/CT_answers_explanation.md`.
- *CT-02B Q.1(c)* is a class-test question. Its answer is in `../CT_Questions/CT_answers_exam_style.md`, with the reasoning in `../CT_Questions/CT_answers_explanation.md`.

---

[🏠 Subtopic Index](00_Index.md) | [← Prev: NM-3.4 Jacobi Iteration](NM-3.4_Jacobi_Iteration.md) | [Next: NM-3.6 Relaxation →](NM-3.6_Relaxation.md)
