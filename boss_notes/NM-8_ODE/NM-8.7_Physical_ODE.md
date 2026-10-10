[← Previous: NM-8.6 Higher Order Systems](NM-8.6_Higher_Order_Systems.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: NM-8.8 Boundary Value Problems →](NM-8.8_Boundary_Value_Problems.md)

---

# NM-8.7: ODE Formulation from Physical Problems

> 🟡 **Priority:** Light | **Tested:** 1/8 years (2021) | **Typical marks:** 4

## What This Is (and Why It Matters)

In engineering exams, the problem is not always handed to you on a silver platter as a pre-packaged equation like $\frac{dy}{dx} = f(x, y)$.

Often, examiners test your ability to think like an engineer by describing a physical situation in English words:
- *"A capacitor loses 4% of its remaining charge every second..."*
- *"A cooling fin loses heat to the ambient air at a rate proportional to the temperature difference..."*
- *"A contaminated chemical tank is flushed with fresh water..."*

Your job is two-fold:
1. **Model the physics:** Translate the verbal description into a differential equation with an initial condition.
2. **Solve the equation:** Find the exact or numerical solution and calculate the numerical quantity requested.

The classic trap here is confusing a **constant rate of loss** (which gives a straight line) with a **rate proportional to the remaining amount** (which gives an exponential decay curve).

---

## 📝 Key Definitions

> **Physical Rate Law (Proportional Decay):** When a physical quantity changes at a rate proportional to its current instantaneous value, the governing equation is $\frac{dQ}{dt} = -k Q$, where $k > 0$ is the rate constant.
>
> **In simple words:** The more charge you have left in the capacitor, the faster it leaks out. As the charge dwindles, the leakage slows down to a trickle.

> **Separation of Variables:** An analytical technique for solving first-order ODEs where all terms containing the dependent variable are gathered on one side with its differential, and all terms containing the independent variable are gathered on the other side.
>
> **In simple words:** Put all the $Q$'s with $dQ$ on the left side, put all the $t$'s with $dt$ on the right side, and integrate both sides.

> **Time Constant ($\tau$):** In an electrical RC circuit, the time constant $\tau = RC$ is the time required for a decaying quantity to fall to $1/e \approx 36.8\%$ of its original charge.
>
> **In simple words:** A single number that sets the speed limit of your circuit's discharge. A bigger time constant means a slower leak.

---

## The Core Idea

### 1. Translating English into Calculus

Let's carefully parse the phrasing: *"A capacitor loses 4% of its remaining charge every second."*

- Let $Q(t)$ represent the charge (in Coulombs) in the capacitor at time $t$ (in seconds).
- The phrase *"loses 4% of its remaining charge"* means the loss rate is:

$$
\text{Rate of loss} = 0.04 \times Q(t)
$$

- In calculus, the rate of change of charge is the derivative $\frac{dQ}{dt}$.
- Because the charge is **decreasing** over time, the rate of change must be **negative**:

$$
\frac{dQ}{dt} = -0.04 \, Q(t)
$$

- The problem states it starts fully charged with $100\text{ Coulombs}$:

$$
Q(0) = 100
$$

> [!WARNING] The Subtraction vs. Proportion Trap
> A student who misreads the question as "loses 4 Coulombs per second" writes $\frac{dQ}{dt} = -4$, leading to $Q(10) = 100 - 4(10) = 60\text{ C}$.
>
> This is completely wrong! The question says **4% of its remaining charge**, not 4 Coulombs. As charge leaks away, 4% of the remaining amount becomes smaller each second. The decay is exponential, not linear.

---

### 2. Solving by Separation of Variables

To solve $\frac{dQ}{dt} = -0.04 Q$:

1. **Separate the variables:**

$$
\frac{dQ}{Q} = -0.04 \, dt
$$

2. **Integrate both sides:**

$$
\int \frac{dQ}{Q} = -0.04 \int dt
$$

$$
\ln Q = -0.04 t + C
$$

3. **Apply the exponential:**

$$
Q(t) = e^{-0.04 t + C} = e^C \cdot e^{-0.04 t} = Q_0 e^{-0.04 t}
$$

4. **Use initial condition $Q(0) = 100$:**

$$
Q(0) = Q_0 e^0 = 100 \implies Q_0 = 100
$$

Thus, the exact continuous solution is:

$$
Q(t) = 100 \, e^{-0.04 t}
$$

---

### 3. Continuous Exponential vs. Discrete Compounding

Why do we use the continuous exponential $e^{-0.04 t}$ instead of multiplying by $0.96$ ten times?

If you treat each second as an isolated discrete jump (like bank interest compounded once a year):

$$
Q(10) = 100 \times (1 - 0.04)^{10} = 100 \times (0.96)^{10} \approx 66.4833\text{ C}
$$

In a real physical capacitor, charge does not wait until the clock ticks exactly one second to dump 4%. Electrons leak continuously through the dielectric or resistor at every microsecond.
The mathematical identity:

$$
(1 - r)^n < e^{-rn} \quad \text{for } 0 < r < 1
$$

proves that discrete yearly compounding always slightly underestimates a smooth continuous decay. Because physical circuits operate continuously, the differential equation $\frac{dQ}{dt} = -0.04 Q$ yielding $Q(t) = 100 e^{-0.04t}$ is the exact physical reality.

---

## 🔧 Worked Example

> **From:** 2021 Q.5(c) -- [Marks: 04]

**The question:** A capacitor loses 4% of its remaining charge every second. It is fully charged with 100 Coulomb of charge. What will be the remaining charge after 10 sec. Develop the ODE and also determine the solution.

**Let's solve this step by step.**

### Part 1: Develop the ODE

Let $Q(t)$ denote the charge stored in the capacitor at time $t$ seconds.
The rate of loss of charge is proportional to the charge present at that instant, with a decay rate of $4\% = 0.04$ per second.

Since the charge decreases with time, the rate of change is negative:

$$
\frac{dQ}{dt} = -0.04 \, Q
$$

with the initial condition:

$$
Q(0) = 100\text{ Coulombs}
$$

### Part 2: Determine the Solution

Separating variables:

$$
\frac{dQ}{Q} = -0.04 \, dt
$$

Integrating both sides:

$$
\ln Q = -0.04 t + C_1
$$

Exponentiating both sides:

$$
Q(t) = e^{C_1} \cdot e^{-0.04 t} = A e^{-0.04 t}
$$

Applying the initial condition $Q(0) = 100$:

$$
100 = A e^{0} \implies A = 100
$$

Therefore, the analytical solution is:

$$
Q(t) = 100 \, e^{-0.04 t}
$$

### Part 3: Calculate the Remaining Charge after 10 Seconds

Substitute $t = 10\text{ s}$:

$$
Q(10) = 100 \, e^{-0.04 \times 10} = 100 \, e^{-0.4}
$$

Using the exponential value $e^{-0.4} \approx 0.670320046$:

$$
Q(10) = 100 \times 0.670320046 = 67.0320046 \approx 67.03\text{ Coulombs}
$$

$$
\boxed{Q(10) = 67.03 \text{ Coulomb}}
$$

**Quick physical sanity check:**
The equivalent circuit time constant is:

$$
\tau = \frac{1}{0.04} = 25\text{ seconds}
$$

The half-life of the charge is:

$$
t_{1/2} = \tau \ln 2 = 25 \times 0.69315 \approx 17.33\text{ seconds}
$$

At $t = 10\text{ s}$, less than one half-life has elapsed ($10 < 17.33$). Therefore, more than half of the initial charge ($> 50\text{ Coulombs}$) must remain. Our answer of $67.03\text{ C}$ makes complete physical sense.

---

### Exam Variants at a Glance

| Year | What They Asked | Physical System | Key Answer |
|:---|:---|:---|:---|
| **2021 Q.5(c)** | Develop ODE and find charge after 10 s | Capacitor 4% decay per second, $Q_0 = 100\text{ C}$ | $\boxed{Q(10) = 67.03 \text{ Coulomb}}$ |

---

## ⚡ Quick Review

**The method in one sentence:** Translate "loses $k\%$ per second" into the proportional decay ODE $\frac{dQ}{dt} = -k Q$, separate variables, integrate, and solve for the constant using initial charge.

**The key model you must memorize:**

$$
\frac{dQ}{dt} = -k Q \implies Q(t) = Q_0 e^{-kt}
$$

**The most common exam mistake:** Forgetting the minus sign in the rate equation ($\frac{dQ}{dt} = +0.04 Q$), which would make the capacitor gain charge exponentially instead of losing it!

**Time estimate in exam:** 4–6 minutes for modeling and solving.

---

## 🔗 Connected Topics

- [← NM-8.6: Higher-Order Systems](NM-8.6_Higher_Order_Systems.md) -- modeling second-order physical systems like RLC circuits.
- [NM-8.2: Euler's Method](NM-8.2_Eulers_Method.md) -- solving the same decay equation numerically with $h = 1$ step.
- [→ NM-8.8: Boundary Value Problems](NM-8.8_Boundary_Value_Problems.md) -- modeling spatial physical problems (steady-state heat and potential distribution).

---

[← Previous: NM-8.6 Higher Order Systems](NM-8.6_Higher_Order_Systems.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: NM-8.8 Boundary Value Problems →](NM-8.8_Boundary_Value_Problems.md)
