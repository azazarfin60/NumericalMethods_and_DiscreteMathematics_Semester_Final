[← Previous: NM-4.4 Regression Theory](NM-4.4_Regression_Theory.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: NM-4.6 Lagrange Interpolation →](NM-4.6_Lagrange_Interpolation.md)

---

# NM-4.5: Linear Interpolation

> 🟠 **Priority:** Secondary | **Tested:** 2 appearances (2018, 2019) | **Typical marks:** 3–4

## What This Is (and Why It Matters)

Linear interpolation is the most basic, intuitive estimation tool in all of engineering. If you know the value of something at $x_0$ and at $x_1$, and you want to estimate what it is halfway between them, you simply connect the two points with a straight line (a chord) and read off the height.

In RUET exams, questions on linear interpolation test two things: can you quickly set up the two-point straight-line formula without getting bogged down in higher-order difference tables, and do you understand how experimental error in the bracket points ruins your interpolated estimate?

---

## 📝 Key Definitions

> **Linear Interpolation:** "The equation of a straight line (a linear polynomial) passing through two points $(x_0, y_0)$ and $(x_1, y_1)$ is given by $L_1(x) = \dfrac{x - x_1}{x_0 - x_1}y_0 + \dfrac{x - x_0}{x_1 - x_0}y_1$." -- Jain, §3.9.1 (p. 101)
>
> **In simple words:** Drawing a straight line directly between two known data points and using that line to estimate any value that falls between them.

> **Truncation Error of Linear Interpolation:**
>
> $$
> R_1(x) = \frac{(x - x_0)(x - x_1)}{2} f''(\xi)
> $$
>
> **In simple words:** The difference between the true curved function and your straight chord. If the curve bends sharply (large second derivative $f''$), the straight chord cuts across the curve and produces a noticeable error.

---

## The Core Idea: The Straight-Line Chord

Given two points $(x_0, y_0)$ and $(x_1, y_1)$ that bracket your target $x$, the slope of the chord connecting them is:

$$
m = \frac{y_1 - y_0}{x_1 - x_0}
$$

The equation of the straight line through $(x_0, y_0)$ is:

$$
y(x) = y_0 + m(x - x_0) = y_0 + \frac{x - x_0}{x_1 - x_0}(y_1 - y_0)
$$

### How to Think About This Formula

Look at the fractional term $\frac{x - x_0}{x_1 - x_0}$:
- When $x = x_0$, the fraction is $0$, and you get $y = y_0$.
- When $x = x_1$, the fraction is $1$, and you get $y = y_0 + (y_1 - y_0) = y_1$.
- When $x$ is anywhere in between, the fraction is just the percentage of the journey from $x_0$ to $x_1$, and you add that exact percentage of the jump $(y_1 - y_0)$ to your starting height $y_0$.

### Why Linear Interpolation Inherits Noise

Linear interpolation has zero ability to filter out measurement error. Because it forces the chord to connect $(x_0, y_0)$ and $(x_1, y_1)$ exactly, any experimental error in either point is directly inherited by the interpolated value.

If point $(x_0, y_0)$ is shifted upward by $+0.1\text{ A}$ due to a bad meter reading, the entire chord tilts upward, pulling your interpolated estimate along with it.

---

## 🔧 Worked Example

> **From:** 2018 Q.3(b) -- [Marks: 03]

**The question:** The upward velocity of a rocket is given as a function of time in the table below. Determine the value of the velocity at $t = 16$ seconds using a $1^{\text{st}}$ order polynomial.

| $t$ (s) | 0 | 10 | 15 | 20 | 22.5 | 30 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| $v(t)$ (m/s) | 0 | 227.04 | 362.78 | 517.35 | 602.97 | 901.67 |

**Let's solve this step by step.**

**Step 1: Identify the bracketing points**
Our target time is $t = 16\text{ s}$.
Looking at the table, $16$ lies between $t = 15$ and $t = 20$.
So our two anchor points are:
- $(t_0, v_0) = (15, 362.78)$
- $(t_1, v_1) = (20, 517.35)$

**Step 2: Set up the first-order polynomial**
A first-order polynomial is a straight line:

$$
v(t) = v_0 + \frac{t - t_0}{t_1 - t_0}(v_1 - v_0)
$$

**Step 3: Substitute the numbers**

$$
v(16) = 362.78 + \frac{16 - 15}{20 - 15}(517.35 - 362.78)
$$

Compute the step difference:

$$
517.35 - 362.78 = 154.57
$$

The fraction is $\frac{1}{5} = 0.2$:

$$
v(16) = 362.78 + 0.2(154.57) = 362.78 + 30.914 = 393.694\ \text{m/s}
$$

$$
\boxed{v(16) = 393.694\ \text{m/s}}
$$

**Quick sanity check:**
$393.694$ sits smoothly between $362.78$ and $517.35$, closer to $15\text{ s}$ than to $20\text{ s}$. The result makes complete physical sense.

---

## 🏆 Past Exam Questions

### 2019 Q.5(b): Ohm's Law and Measurement Error Discrepancy [04 Marks]

**The question:** To verify Ohm's law, an experiment was performed and the results obtained are in the following table:

| $V$ (V) | 5 | 10 | 15 | 20 | 25 |
| :---: | :---: | :---: | :---: | :---: | :---: |
| $I$ (A) | 1 | 2.1 | 3 | 4.2 | 5 |

Use linear interpolation to determine the current for $12\text{ V}$ of supply. Explain why the result differs from actual value.

**Let's solve this step by step.**

**Part 1: Linear interpolation at $V = 12\text{ V}$**
The target voltage $V = 12\text{ V}$ is bracketed by:
- $(V_0, I_0) = (10, 2.1)$
- $(V_1, I_1) = (15, 3.0)$

Apply the linear interpolation formula:

$$
I(12) = I_0 + \frac{V - V_0}{V_1 - V_0}(I_1 - I_0)
$$

Substitute the values:

$$
I(12) = 2.1 + \frac{12 - 10}{15 - 10}(3.0 - 2.1) = 2.1 + \frac{2}{5}(0.9) = 2.1 + 0.36 = 2.46\ \text{A}
$$

$$
\boxed{I(12\ \text{V}) = 2.46\ \text{A}}
$$

**Part 2: Why the result differs from the actual value**
Ohm's law gives $V = IR \implies I = V/R$.
Look at the clean data points:
- At $5\text{ V}$: $I = 1\text{ A} \implies R = 5/1 = 5\ \Omega$
- At $15\text{ V}$: $I = 3\text{ A} \implies R = 15/3 = 5\ \Omega$
- At $25\text{ V}$: $I = 5\text{ A} \implies R = 25/5 = 5\ \Omega$

The true physical resistance is $R = 5\ \Omega$.
Therefore, the true physical current at $12\text{ V}$ is:

$$
I_{\text{actual}} = \frac{12\text{ V}}{5\ \Omega} = 2.40\ \text{A}
$$

Our interpolated value was $2.46\text{ A}$, leaving an error of $+0.06\text{ A}$.

**Why did this happen?**
The measurement recorded at $10\text{ V}$ contained an experimental error ($2.1\text{ A}$ instead of the true $2.0\text{ A}$). Because linear interpolation connects the two points with an exact straight chord, it accepts this $+0.1\text{ A}$ error as fact and propagates it directly into the interpolated result.

---

## ⚡ Quick Review

**The formula in one sentence:** Take the starting point and add the fraction of the step times the jump.

**The formula you must memorize:**
$$
y(x) = y_0 + \frac{x - x_0}{x_1 - x_0}(y_1 - y_0)
$$

**The most common exam mistake:** Picking points that do not bracket the target point. Always choose $x_0$ and $x_1$ such that $x_0 \le x \le x_1$.

**Time estimate in exam:** ~3 minutes to calculate and write down.

---

## 🔗 Connected Topics

- [← NM-4.4: Regression Theory](NM-4.4_Regression_Theory.md) -- why least squares regression smooths out measurement errors that linear interpolation blindly copies.
- [→ NM-4.6: Lagrange Interpolation](NM-4.6_Lagrange_Interpolation.md) -- generalizing two-point linear interpolation to $n$-point polynomial interpolation.
- [NM-4.1: Concepts](NM-4.1_Concepts.md) -- the definition of interpolation versus curve fitting.

---

[← Previous: NM-4.4 Regression Theory](NM-4.4_Regression_Theory.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: NM-4.6 Lagrange Interpolation →](NM-4.6_Lagrange_Interpolation.md)
