[← Previous: NM-5.6 Error in Integration](NM-5.6_Error_in_Integration.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: NM-6.1 Optimization Concepts →](../NM-6_Optimization/NM-6.1_Concepts.md)

---

# NM-5.7: Applied Integration

> 🟠 **Priority:** Secondary | **Tested:** 3/8 years (2018, 2020, 2023) | **Typical marks:** 5 to 8

## What This Is (and Why It Matters)

Applied integration is where numerical mathematics meets real-world physical systems. In laboratory and field engineering, you do not integrate abstract polynomial exercises. You are given telemetry from an aerospace vehicle or sampled voltage waveforms from an electronic sensor, and you must compute physical quantities like distance traveled or output voltage.

In RUET examinations, applied integration appears in two classic engineering problems:
1. **Rocket flight mechanics (2018 Q.6(a), 2023 Q.4(b)):** Integrating vertical velocity under continuous fuel consumption and gravity to find the rocket's altitude.
2. **Analog op-amp integrator circuit (2020 Q.6(b)):** Integrating a sampled input voltage through an operational amplifier circuit to determine the output voltage.

Understanding the physics and circuit equations behind these problems ensures you never lose marks on units, signs, or boundary setups.

---

## 📝 Key Definitions

> **Kinematic Distance Integration:** "The displacement of a body moving along a straight line over a time interval $[t_0, t_1]$ is the definite integral of its velocity function: $x = \int_{t_0}^{t_1} v(t)\,dt$."
>
> **In simple words:** Distance is the area under the velocity-time graph. If you know the rocket's speed at different moments, integrating that speed gives you the total distance flown.

> **Op-Amp Integrator Circuit:** "An analog operational amplifier circuit configured with an input resistor $R$ and a feedback capacitor $C$, where the output voltage is proportional to the negative time-integral of the input voltage: $v_0(t) = -\frac{1}{RC}\int_0^t v_i(\tau)\,d\tau$."
>
> **In simple words:** An electronic circuit that computes integrals in real time. The input voltage pushes charge into a capacitor, and the resulting output voltage is the negative integral of the input scaled by $\frac{1}{RC}$.

> **Sampled Data Quadrature:** "The numerical evaluation of an integral when the integrand is known only at discrete, experimentally measured sample points rather than as a continuous closed-form equation."
>
> **In simple words:** When you measure real hardware in a lab, your oscilloscope or ADC only records numbers at discrete time intervals. You must use numerical integration rules to find the area under those sampled points.

---

## Application 1: Rocket Telemetry & Kinematics

In aerospace engineering, a rocket burns fuel at a constant rate $q$, causing its total mass $m(t) = m_0 - q t$ to decrease over time. According to Tsiolkovsky's rocket equation, the vertical velocity under downward gravitational acceleration $g$ is:

$$
v(t) = u \ln\left[\frac{m_0}{m_0 - q t}\right] - g t
$$

For the classic test rocket problem:
- Initial mass $m_0 = 140000\text{ kg}$
- Exhaust velocity $u = 2000\text{ m/s}$
- Fuel consumption rate $q = 2100\text{ kg/s}$
- Gravity $g = 9.8\text{ m/s}^2$
- Time span $t = 8\text{ s}$ to $t = 30\text{ s}$

The vertical distance traveled is the definite integral:

$$
x = \int_8^{30} \left( 2000 \ln \left[ \frac{140000}{140000 - 2100t} \right] - 9.8t \right) dt
$$

### Analytical vs Numerical Solution

Using integration by parts ($\int \ln(A - kt)\,dt = t\ln(A - kt) - t - \frac{A}{k}\ln(A - kt)$), the exact analytical integral is:

$$
x_{\text{exact}} = 11061.3355\text{ m}
$$

The exam tests this exact integral in two distinct ways:

#### Case A: Eight-Segment Composite Simpson's 1/3 (2018 Q.6(a) -- 8 Marks)
When the question specifies **eight segments** ($n = 8$):
- Step size is $h = \frac{30 - 8}{8} = 2.75\text{ s}$.
- We evaluate 9 nodes from $t = 8$ to $t = 30$ with weights $1, 4, 2, 4, 2, 4, 2, 4, 1$.
- Approximate distance:
  $$
  \boxed{x \approx 11061.3548\ \text{m}}
  $$
- True error:
  $$
  E_t = 11061.3355 - 11061.3548 = -0.0193\text{ m}
  $$
  $$
  \boxed{E_t \approx -0.0193\ \text{m}}
  $$
- Absolute relative true error:
  $$
  |\varepsilon_t| = \left|\frac{-0.0193}{11061.3355}\right| \times 100\% \approx 0.00017\%
  $$
  $$
  \boxed{|\varepsilon_t| \approx 0.00017\%}
  $$

---

#### Case B: Single-Application Simpson's 1/3 (2023 Q.4(b) -- 5 Marks)
When the question does **not** specify a segment count, standard convention calls for the fundamental two-segment single application ($n = 2$):
- Step size is $h = \frac{30 - 8}{2} = 11\text{ s}$.
- We evaluate only 3 nodes: $t_0 = 8, t_1 = 19, t_2 = 30$.
- Approximate distance:
  $$
  x \approx \frac{11}{3}[177.2667 + 4(484.7455) + 901.6740] \approx 11065.72\text{ m}
  $$
  $$
  \boxed{\text{(i) } x \approx 11065.72\text{ m}}
  $$
- True error:
  $$
  E_t = 11061.34 - 11065.72 = -4.38\text{ m}
  $$
  $$
  \boxed{\text{(ii) } E_t = -4.38\text{ m}}
  $$
- Absolute relative true error:
  $$
  |\epsilon_t| = \left|\frac{-4.38}{11061.34}\right| \times 100\% \approx 0.0396\%
  $$
  $$
  \boxed{\text{(iii) } |\epsilon_t| = 0.0396\%}
  $$

---

## Application 2: ECE Analog Op-Amp Integrator Circuit

In electrical engineering laboratories, an operational amplifier with an input resistor $R$ and feedback capacitor $C$ performs analog integration:

```
          C
     +---||---+
     |        |
Vi --/\/\/\---+--|\
       R      |  | \
              +--|- \
                 |   >--- Vo
              +--|+ /
              |  | /
             GND
```

### Deriving the Circuit Governing Equation

1. **Virtual ground:** Assuming an ideal op-amp, negative feedback holds the inverting terminal at virtual ground potential ($v_- = 0\text{ V}$).
2. **Resistor current:** The current flowing into the summing junction from the input is:
   $$
   i_R = \frac{v_i - 0}{R} = \frac{v_i}{R}
   $$
3. **Capacitor current:** Since ideal op-amp inputs draw zero current, all of $i_R$ must flow through the feedback capacitor $C$:
   $$
   i_C = C \frac{d(0 - v_0)}{dt} = -C \frac{dv_0}{dt}
   $$
4. **Equating currents:**
   $$
   \frac{v_i}{R} = -C \frac{dv_0}{dt} \implies \frac{dv_0}{dt} = -\frac{1}{RC} v_i(t)
   $$
5. **Integrating both sides from $0$ to $t$:**
   $$
   v_0(t) = -\frac{1}{RC} \int_0^t v_i(\tau)\,d\tau
   $$

---

### Step-by-Step Numerical Solution (2020 Q.6(b))

Let us review the laboratory dataset given in 2020 Q.6(b):
- $R = 10\text{ k}\Omega = 10^4\,\Omega$
- $C = 1\ \mu\text{F} = 10^{-6}\text{ F}$
- Query time: $t = 1.25\text{ s}$

| $t$ (s) | 0 | 0.25 | 0.50 | 0.75 | 1.00 | 1.25 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| $v_i(t)$ (V) | 1.0000 | 0.9793 | 0.9195 | 0.8261 | 0.7081 | 0.6201 |

**Step 1. Calculate the scaling constant $\frac{1}{RC}$:**

$$
RC = (10^4\,\Omega)(10^{-6}\,\text{F}) = 10^{-2}\text{ s} = 0.01\text{ s}
$$

$$
\frac{1}{RC} = \frac{1}{0.01\text{ s}} = 100\text{ s}^{-1}
$$

**Step 2. Identify the subinterval count constraint:**
There are 6 data points, which means there are $6 - 1 = 5$ subintervals of width $h = 0.25\text{ s}$.
Because 5 is **odd**, Simpson's 1/3 rule cannot cover all 5 subintervals directly.

**Step 3. Execute the mixed strategy:**
- **Intervals 1 to 4 ($t = 0$ to $t = 1.00$):** 4 subintervals (even). Apply Simpson's 1/3 rule:
  $$
  I_{1/3} = \frac{0.25}{3}[1 + 4(0.9793) + 2(0.9195) + 4(0.8261) + 0.7081]
  $$
  $$
  = \frac{0.25}{3}[1 + 3.9172 + 1.8390 + 3.3044 + 0.7081] = \frac{0.25}{3}(10.7687) \approx 0.89739167\text{ V}\cdot\text{s}
  $$

- **Interval 5 ($t = 1.00$ to $t = 1.25$):** 1 subinterval. Apply the trapezoidal rule:
  $$
  I_T = \frac{0.25}{2}(0.7081 + 0.6201) = 0.125(1.3282) = 0.166025\text{ V}\cdot\text{s}
  $$

- **Total integrated area:**
  $$
  I = I_{1/3} + I_T = 0.89739167 + 0.166025 = 1.06341667\text{ V}\cdot\text{s}
  $$

**Step 4. Compute output voltage with the mandatory minus sign:**

$$
v_0(1.25) = -\frac{1}{RC} I = -100(1.06341667) = -106.341667\text{ V}
$$

$$
\boxed{v_0(1.25) = -106.34 \text{ V}}
$$

---

## Common Traps in Applied Integration Problems

1. **Dropping the inverting minus sign:** In the op-amp problem, the inverting configuration carries a leading negative sign. If your answer is $+106.34\text{ V}$, you dropped the negative sign and lose points.
2. **Incorrect time constant conversion:** Remember that $1\ \mu\text{F} = 10^{-6}\text{ F}$ and $10\text{ k}\Omega = 10^4\,\Omega$. Their product is $10^{-2}\text{ s}$, which makes $\frac{1}{RC} = 100$, never $0.01$ or $10^{-8}$.
3. **Misreading the segment count instruction:** Always check whether the question specifies the segment count (e.g. "eight-segment" in 2018) or leaves it unspecified (e.g. single application in 2023).

---

### Exam Variants at a Glance

| Year | Physical Setup | Numerical Rule | Key Result |
|:---|:---|:---|:---|
| 2018 Q.6(a) | Rocket distance ($t = 8$ to $30$) | 8-segment composite Simpson's 1/3 | $\boxed{x \approx 11061.3548\ \text{m}}$ |
| 2018 Q.6(a)(ii) | Rocket true error ($n = 8$) | $x_{\text{exact}} - x$ | $\boxed{E_t \approx -0.0193\ \text{m}}$ |
| 2018 Q.6(a)(iii) | Rocket relative error ($n = 8$) | $\|E_t / x_{\text{exact}}\| \times 100\%$ | $\boxed{|\varepsilon_t| \approx 0.00017\%}$ |
| 2020 Q.6(b) | Op-amp integrator ($R=10\text{k}\Omega, C=1\mu\text{F}$) | Mixed Simpson 1/3 (4) + Trapezoid (1) | $\boxed{v_0(1.25) = -106.34 \text{ V}}$ |
| 2023 Q.4(b)(i) | Rocket distance (single application) | Fundamental Simpson 1/3 ($n = 2$) | $\boxed{\text{(i) } x \approx 11065.72\text{ m}}$ |
| 2023 Q.4(b)(ii) | Rocket true error ($n = 2$) | $I_{\text{exact}} - x$ | $\boxed{\text{(ii) } E_t = -4.38\text{ m}}$ |
| 2023 Q.4(b)(iii) | Rocket relative error ($n = 2$) | $\|E_t / I_{\text{exact}}\| \times 100\%$ | $\boxed{\text{(iii) } |\epsilon_t| = 0.0396\%}$ |

---

## ⚡ Quick Review

**The method in one sentence:** Convert physical equations into definite integrals, check whether interval counts require mixed rules, and preserve physical constants and signs.

**The key equations to memorize:**

$$
\text{Rocket: } x = \int_{t_0}^{t_1} v(t)\,dt, \qquad \text{Op-Amp: } v_0 = -\frac{1}{RC}\int_0^t v_i(\tau)\,d\tau
$$

**The most common exam mistake:** Forgetting the minus sign in inverting op-amp circuits, or applying a single Simpson rule to an odd interval count.

**Time estimate in exam:** ~10 minutes for rocket composite calculation; ~8 minutes for op-amp mixed calculation.

---

## 🔗 Connected Topics

- [← NM-5.6: Error in Integration](NM-5.6_Error_in_Integration.md) -- calculating true error and percentage error for applied integrals.
- [NM-5.2: Simpson's 1/3 Rule](NM-5.2_Simpsons_One_Third.md) -- primary numerical engine used for both rocket and op-amp problems.
- [NM-5.4: Rule Comparison](NM-5.4_Rule_Comparison.md) -- explains the odd-interval constraint that necessitates mixed rules in circuit problems.
- [Next: NM-6.1 Optimization Concepts →](../NM-6_Optimization/NM-6.1_Concepts.md) -- transitioning from integration to numerical optimization.

---

[← Previous: NM-5.6 Error in Integration](NM-5.6_Error_in_Integration.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: NM-6.1 Optimization Concepts →](../NM-6_Optimization/NM-6.1_Concepts.md)
