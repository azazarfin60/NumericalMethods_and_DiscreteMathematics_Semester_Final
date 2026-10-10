[← Previous: NM-7.3 Second Derivative](NM-7.3_Second_Derivative.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: NM-8.1 IVP vs BVP →](../NM-8_ODE/NM-8.1_IVP_vs_BVP.md)

---

# NM-7.4: Applied Differentiation

> 🟠 **Priority:** Secondary | **Tested:** 3 appearances (2021, 2019, 2020) | **Typical marks:** 2–5

## What This Is (and Why It Matters)

Why do electrical and computer engineers need numerical differentiation? In textbooks, you are given smooth functions like $i(t) = I_0 \sin(\omega t)$. But in the real world, hardware sensors do not output smooth formulas. A microcontroller reading an analog-to-digital converter (ADC) only sees an array of raw numbers recorded at discrete time intervals.

Also, many crucial physical quantities cannot be measured directly with sensors. We measure what is cheap, convenient, and reliable (like position from a GPS module, current through a shunt resistor, or shaft angle from an optical encoder), and then use numerical differentiation to recover the hidden quantities we actually need: velocity, acceleration, inductor voltage, and motor speed.

In the semester finals, examiners test this in two ways:
1. **Descriptive theory:** Asking you directly to write down a real-life engineering application of numerical differentiation (2021 Q.6(a)).
2. **Applied numerical problems:** Handing you an inductor current table or a motor shaft angle table and asking you to compute the physical response (2019 Q.6(b), 2020 Q.6(c)).

---

## 📝 Key Definitions

> **Applied numerical differentiation:** "The computational recovery of physical rates of change (such as velocity, acceleration, or induced EMF) from discrete sampled sensor data where no continuous analytical expression exists."
>
> **In simple words:** Using math to calculate speed or voltage from a series of snapshot measurements when you do not have a formula.

> **Faraday's Law for inductors:** "The voltage across an ideal inductor is proportional to the time rate of change of the current passing through it: $v(t) = L \frac{di(t)}{dt}$."
>
> **In simple words:** An inductor resists changes in current. If you know the current at each microsecond, the slope of that current multiplied by inductance $L$ tells you the voltage across the component.

> **Kinematic rate estimation:** "The numerical differentiation of sampled position coordinates $x(t)$ to obtain instantaneous velocity $v(t) = \frac{dx}{dt}$ and instantaneous acceleration $a(t) = \frac{d^2x}{dt^2}$."
>
> **In simple words:** GPS tells you where you are; differencing consecutive GPS timestamps tells you how fast you are moving and how hard you are accelerating.

> **Signal peak detection:** "Locating the local extrema of a continuous signal by identifying the zero-crossings of its numerical first derivative ($f'(t) = 0$)."
>
> **In simple words:** A signal hits its maximum height at the exact moment its slope switches from positive to negative. Taking the numerical derivative reveals precisely where the peak occurs.

---

## The Core Real-World Applications in ECE

Here are the four primary engineering domains where numerical differentiation is indispensable:

### 1. Navigation & Robotics: Velocity and Acceleration from GPS

Autonomous drones, self-driving cars, and robotic arms rely on GPS and optical tracking systems. A GPS receiver logs position coordinates $x(t)$ at a fixed sampling interval $h$ (typically $0.1\text{ s}$ or $0.01\text{ s}$).

The onboard flight controller cannot wait for an analytical equation. It estimates velocity using the three-point central difference formula:

$$
v(t) \approx \frac{x(t + h) - x(t - h)}{2h}
$$

and estimates acceleration using the central second-difference formula:

$$
a(t) \approx \frac{x(t + h) - 2x(t) + x(t - h)}{h^2}
$$

Because the central difference has $O(h^2)$ truncation error, halving the sampling period $h$ cuts the mathematical error by a factor of 4.

> [!NOTE] The Sensor Noise Trade-Off
> If GPS readings contain random measurement noise $\epsilon$, differencing two nearby readings can amplify that noise by $\epsilon / h$. In practical navigation software, engineers apply a low-pass digital filter (such as a Kalman filter) to smooth the data before taking numerical derivatives.

---

### 2. Electrical Circuits: Inductor Voltage from Sampled Current

In power electronics and motor drives, current is easy to measure by placing a low-value precision resistor (a shunt) in series with the circuit and reading the voltage across it with an ADC.

Once the current $I(t)$ is recorded in a tabular array, the voltage across an inductor $L$ is obtained directly from Faraday's law:

$$
v(t) = L \frac{dI}{dt}
$$

This was the exact problem asked in **2019 Q.6(b)**:
- Inductance: $L = 1\text{ H}$
- Current table at $t = 0.25$ to $0.29\text{ s}$ with $h = 0.01\text{ s}$
- Target: find voltage $v$ at $t = 0.27\text{ s}$
- Using 5-point central difference:
  $$
  \frac{dI}{dt}\bigg|_{0.27} = 0.965\text{ A/s} \implies v(0.27) = 1 \times 0.965 = 0.965\text{ V}
  $$

---

### 3. Motion Control: Angular Velocity from Shaft Encoders

Electric motors and robotic joints use optical rotary encoders. An encoder produces digital pulses as the motor turns, providing a table of angular positions $\theta$ at fixed time intervals $t$:

| $t$ (sec) | 0.00 | 0.02 | 0.04 | 0.06 | 0.08 | 0.10 | 0.12 |
| :-- | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| $\theta$ (rad) | 0.052 | 0.105 | 0.168 | 0.242 | 0.327 | 0.408 | 0.489 |

To run closed-loop PID speed control, the microcontroller needs the angular velocity $\omega$:

$$
\omega = \frac{d\theta}{dt}
$$

This was the exact problem asked in **2020 Q.6(c)**:
- Step size: $h = 0.02\text{ s}$
- Target: find $\omega$ at $t = 0.06\text{ s}$
- Using 3-point central difference:
  $$
  \omega(0.06) \approx \frac{\theta(0.08) - \theta(0.04)}{2(0.02)} = \frac{0.327 - 0.168}{0.04} = 3.975\text{ rad/s}
  $$

---

### 4. Signal Processing & Crash Testing: Peak Detection

In automotive crash tests, accelerometer sensors log thousands of impact force samples per second. Safety engineers must find the **peak deceleration** to determine whether passenger airbags deploy in time.

The maximum of a sampled signal occurs where its slope is zero:

$$
\frac{df}{dt} = 0
$$

By tracking the numerical derivative $f'(t)$, the computer detects the exact instant the derivative crosses zero from positive to negative, pinpointing the peak impact force.

Similar algorithms run inside medical ECG monitors to detect heartbeats by finding the sharp peak of the QRS cardiac wave.

---

## 🏆 Past Exam Questions

### 2021 Q.6(a): Real-Life Application of Numerical Differentiation [02/03 Marks]

**The question:** Write down a real-life application of numerical differentiation.

**Full Solution:**

**Velocity and acceleration from position data.**

A vehicle's position $x(t)$ is logged by GPS, or a vibrating mass's displacement is recorded by an accelerometer. Neither instrument measures velocity directly, yet both are needed for control. The derivative is obtained from the finite difference

$$
v(t) = \frac{x(t+h) - x(t-h)}{2h}
$$

Accuracy is $O(h^2)$, and halving $h$ cuts the truncation error by 4 while multiplying the round off error by 2, so the optimal $h$ sits where the two cross, usually near the cube root of the machine epsilon.

Second application: finding the **peak** of a sampled signal, such as the peak acceleration in a crash test, where the maximum of the numerical derivative locates the maximum of the original.

$$
\boxed{\text{GPS or accelerometer data gives position; the numerical derivative gives velocity and acceleration}}
$$

---

## 📊 Summary of Applied Differentiation Exam Problems

| Year & Paper | Physical Scenario | Governing Equation | Numerical Method | Full Solution Link |
| :-- | :-- | :-- | :-- | :-- |
| **2021 Q.6(a)** | GPS / Accelerometer telemetry & peak sensing | $v = \frac{dx}{dt}$, $a = \frac{d^2x}{dt^2}$ | 3-point central difference theory | Discussed above (Boxed origin) |
| **2019 Q.6(b)** | Inductor voltage from current table ($L = 1\text{ H}$) | $v(t) = L \frac{dI}{dt}$ | 5-point central difference ($h = 0.01$) | [See NM-7.2 Problem 2](NM-7.2_First_Derivative.md#problem-2-2019-q6b-inductor-voltage-from-sampled-current-05-marks) |
| **2020 Q.6(c)** | Motor shaft angular velocity from displacement $\theta(t)$ | $\omega = \frac{d\theta}{dt}$ | 3-point central difference ($h = 0.02$) | [See NM-7.2 Problem 3](NM-7.2_First_Derivative.md#problem-3-2020-q6c-angular-velocity-from-angular-displacement-04-marks) |

---

## ⚡ Quick Review

**The core concept in one sentence:** Numerical differentiation allows engineers to convert readily measurable state variables (like position, angle, and current) into hidden dynamic rates (like velocity, acceleration, and induced voltage).

**The three physical formulas to remember:**
1. **Kinematics:** $v(t) = \frac{dx}{dt}$, $a(t) = \frac{d^2x}{dt^2}$
2. **Circuit inductors:** $v(t) = L \frac{di}{dt}$
3. **Rotary mechanics:** $\omega(t) = \frac{d\theta}{dt}$

**Practical engineering tip:** In real hardware systems, raw sensor readings contain high-frequency electrical noise. Differentiating noise directly amplifies high frequencies! Always apply a smoothing filter to the table before calculating finite differences.

**Time estimate in exam:** 4 to 5 minutes for a 2–3 mark descriptive question.

---

## 🔗 Connected Topics

- [← NM-7.3: Second Derivative](NM-7.3_Second_Derivative.md) -- mathematical derivation of the second-derivative formula used in acceleration calculations.
- [← NM-7.2: First Derivative](NM-7.2_First_Derivative.md) -- complete numerical calculations for the inductor and angular velocity exam problems.
- [→ NM-8.1: IVP vs BVP](../NM-8_ODE/NM-8.1_IVP_vs_BVP.md) -- using differential rate equations to model dynamic engineering systems over time.

---

[← Previous: NM-7.3 Second Derivative](NM-7.3_Second_Derivative.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: NM-8.1 IVP vs BVP →](../NM-8_ODE/NM-8.1_IVP_vs_BVP.md)
