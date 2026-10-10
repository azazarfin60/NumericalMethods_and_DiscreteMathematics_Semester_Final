[← Previous: NM-6.2 Unconstrained Optimization](NM-6.2_Unconstrained_Optimization.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: NM-7.1 Difference Formulas →](../NM-7_Differentiation/NM-7.1_Difference_Formulas.md)

---

# NM-6.3: Optima from Tabulated Data

> 🟡 **Priority:** Light | **Tested:** 1/8 years (2018 Q.5(b)) | **Typical marks:** 6

## What This Is (and Why It Matters)

What happens when you do not have an analytical formula like $f(x) = 2\sin x - x^2/10$, but only a table of numbers measured in an experiment?

For example, imagine logging the efficiency of an RF amplifier at different bias voltages, or recording the gain of an antenna at different angles. You want to answer two practical engineering questions:
1. *At what exact operating coordinate $x$ does the response reach its absolute peak?*
2. *What is that peak value $y_{\max}$?*

The true peak almost never lands neatly on one of your recorded sample rows. It hides in the gap between two data points.

To find it, you build a finite difference table, construct the interpolating polynomial, differentiate that polynomial with respect to the step coordinate $q$, set the derivative to zero ($\frac{dy}{dx} = 0$), and solve for the peak position.

In the 2018 semester final, RUET asked this exact question for 6 marks. It is one of the highest-scoring problems in Section A if you follow the step-by-step workflow.

---

## 📝 Key Definitions

> **Tabulated Function Optimum:** "The maximum or minimum value of a function tabulated at equal intervals is determined by representing the function by an interpolation polynomial, equating the first derivative to zero, and solving for the location of the stationary point." -- Jain, §5.2
>
> **In simple words:** Fitting a smooth polynomial curve through your recorded data table, taking its derivative, and finding the point where the slope levels out to zero.

> **Dimensionless Step Coordinate $q$ (or $p$):** "The dimensionless variable $q = \frac{x - x_n}{h}$ denotes the normalized distance from the chosen reference node $x_n$, measured in units of the equal spacing interval $h$." -- Jain, §3.2
>
> **In simple words:** A scaled position counter. A value of $q = -0.28$ means your target point sits $28\%$ of a step size to the left of your anchor node.

> **Newton Backward Derivative:** "The derivative of the Newton backward difference interpolating polynomial with respect to $x$ at reference point $x_n$ is given by $\frac{dy}{dx} = \frac{1}{h}\left[\nabla y_n + \frac{2q+1}{2}\nabla^2 y_n + \frac{3q^2+6q+2}{6}\nabla^3 y_n + \dots\right]$." -- Jain, §5.2
>
> **In simple words:** The slope of the curve near the end of your data table, expressed using backward differences and the fractional coordinate $q$.

---

## The Core Idea

### How to Diagnose the Peak from the Difference Table

Before running through any algebra, the difference table tells you where the peak is hiding and whether it is a maximum or a minimum:

1. **First differences ($\Delta y$ or $\nabla y$):**
   - If first differences are positive, the function is rising.
   - If they are negative, the function is falling.
   - If first differences are positive but shrink toward zero (for example, $0.0316 \to 0.0219 \to 0.0120 \to 0.0021$), the function is flattening out. The peak is imminent!
2. **Second differences ($\Delta^2 y$ or $\nabla^2 y$):**
   - If the second differences are negative throughout the table, the curve is concave downward (like an upside-down bowl). That guarantees your stationary point is a **maximum**.

### Forward vs. Backward Choice

- If the peak sits near the **beginning** of the table, anchor at $x_0$ and use the **Newton forward derivative formula** with $p = (x - x_0)/h$.
- If the peak sits near the **end** of the table, anchor at $x_n$ and use the **Newton backward derivative formula** with $q = (x - x_n)/h$.

### Differentiating the Newton Backward Polynomial

Recall the 5-point Newton backward interpolating polynomial:

$$
y(q) = y_n + q\nabla y_n + \frac{q(q+1)}{2}\nabla^2 y_n + \frac{q(q+1)(q+2)}{6}\nabla^3 y_n + \frac{q(q+1)(q+2)(q+3)}{24}\nabla^4 y_n
$$

Because $q = \frac{x - x_n}{h}$, the chain rule gives:

$$
\frac{dy}{dx} = \frac{dy}{dq} \frac{dq}{dx} = \frac{1}{h} \frac{dy}{dq}
$$

Now differentiate each polynomial coefficient with respect to $q$:
- $\frac{d}{dq}[q] = 1$
- $\frac{d}{dq}\left[\frac{q^2 + q}{2}\right] = \frac{2q + 1}{2} = q + \frac{1}{2}$
- $\frac{d}{dq}\left[\frac{q^3 + 3q^2 + 2q}{6}\right] = \frac{3q^2 + 6q + 2}{6}$
- $\frac{d}{dq}\left[\frac{q^4 + 6q^3 + 11q^2 + 6q}{24}\right] = \frac{4q^3 + 18q^2 + 22q + 6}{24}$

Putting these together gives the backward derivative formula:

$$
\frac{dy}{dx} = \frac{1}{h}\left[\nabla y_n + \frac{2q+1}{2}\nabla^2 y_n + \frac{3q^2+6q+2}{6}\nabla^3 y_n + \frac{4q^3+18q^2+22q+6}{24}\nabla^4 y_n\right]
$$

### Setting $\frac{dy}{dx} = 0$

To find the stationary point, set $\frac{dy}{dx} = 0$.

In practical problems, higher differences like $\nabla^3$ and $\nabla^4$ are very small or zero. The first two terms dominate completely:

$$
\nabla y_n + \frac{2q+1}{2}\nabla^2 y_n \approx 0
$$

$$
(q + 0.5)\nabla^2 y_n \approx -\nabla y_n
$$

$$
q + 0.5 \approx -\frac{\nabla y_n}{\nabla^2 y_n} \implies q \approx -\frac{\nabla y_n}{\nabla^2 y_n} - 0.5
$$

Once you have $q$:
1. Calculate the physical $x$-coordinate: $x = x_n + hq$.
2. Substitute $q$ back into the original Newton polynomial to find $y_{\max}$.

---

## 🔧 Worked Example

> **From:** 2018 Q.5(b), [Marks: 06]

**The question:** From the following table find $x$, correct to two decimal places for which $y$ is maximum and find this value of $y$.

| $x$ | 1.2 | 1.3 | 1.4 | 1.5 | 1.6 |
| :---: | :---: | :---: | :---: | :---: | :---: |
| $y$ | 0.9320 | 0.9636 | 0.9855 | 0.9975 | 0.9996 |

**Let's solve this step by step.**

### Step 1. Build the difference table and analyze the trend

The step size is constant: $h = 1.3 - 1.2 = 0.1$.

Let's compute the difference table:

| $x$ | $y$ | First Diff $\Delta$ | Second Diff $\Delta^2$ | Third Diff $\Delta^3$ | Fourth Diff $\Delta^4$ |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1.2 | 0.9320 | | | | |
| | | $0.0316$ | | | |
| 1.3 | 0.9636 | | $-0.0097$ | | |
| | | $0.0219$ | | $-0.0002$ | |
| 1.4 | 0.9855 | | $-0.0099$ | | $0.0002$ |
| | | $0.0120$ | | $0.0000$ | |
| 1.5 | 0.9975 | | $-0.0099$ | | |
| | | $0.0021$ | | | |
| 1.6 | 0.9996 | | | | |

**Physical inspection of the numbers:**
- All four first differences are positive ($0.0316, 0.0219, 0.0120, 0.0021$), so $y$ is rising across the entire table.
- But the last first difference, $0.0021$, is tiny, and the second differences are all negative ($\approx -0.0099$).
- That tells us the curve is leveling off rapidly. The peak lies just inside the end of the table, slightly before $x = 1.6$.
- Because the peak is at the far end of the table, the **Newton backward difference formula** anchored at $x_4 = 1.6$ is the natural choice.

### Step 2. Set up the backward derivative formula

At the bottom node $x_4 = 1.6$, the dimensionless coordinate is:

$$
q = \frac{x - x_4}{h} = \frac{x - 1.6}{0.1}
$$

The backward differences along the bottom diagonal are:

$$
\nabla y_4 = 0.0021, \qquad \nabla^2 y_4 = -0.0099, \qquad \nabla^3 y_4 = 0.0000, \qquad \nabla^4 y_4 = 0.0002
$$

The derivative formula is:

$$
\frac{dy}{dx} = \frac{1}{h}\left[\nabla y_4 + \frac{2q + 1}{2}\nabla^2 y_4 + \frac{3q^2 + 6q + 2}{6}\nabla^3 y_4 + \frac{4q^3 + 18q^2 + 22q + 6}{24}\nabla^4 y_4\right]
$$

### Step 3. Set $\frac{dy}{dx} = 0$ and solve for $q$ and $x$

Because $\nabla^3 y_4 = 0.0000$ and $\nabla^4 y_4 = 0.0002$ is extremely small, the stationary point is determined by the first two terms:

$$
0.0021 + \frac{2q + 1}{2}(-0.0099) = 0
$$

$$
0.0021 = (q + 0.5)(0.0099)
$$

$$
q + 0.5 = \frac{0.0021}{0.0099} = 0.212121
$$

$$
q = 0.212121 - 0.5 = -0.287879
$$

Notice that $q$ is negative! A value of $q = -0.287879$ confirms that the peak lies inside the table, about $29\%$ of a step to the left of $x_4 = 1.6$.

Now calculate the physical position $x$:

$$
x = x_4 + hq = 1.6 + 0.1(-0.287879) = 1.6 - 0.028788 = 1.571212
$$

Rounding correct to two decimal places:

$$
x = 1.57
$$

### Step 4. Evaluate the maximum value $y$

Now substitute $q = -0.287879$ into the full 5-point backward Newton polynomial:

$$
y = y_4 + q\nabla y_4 + \frac{q(q+1)}{2}\nabla^2 y_4 + \frac{q(q+1)(q+2)}{6}\nabla^3 y_4 + \frac{q(q+1)(q+2)(q+3)}{24}\nabla^4 y_4
$$

Let's compute the individual factors for $q = -0.287879$:
- $q = -0.287879$
- $q + 1 = 0.712121$
- $q + 2 = 1.712121$
- $q + 3 = 2.712121$

Now evaluate term by term:
- **Term 0:** $y_4 = 0.9996$
- **Term 1:** $q\nabla y_4 = (-0.287879)(0.0021) = -0.0006045$
- **Term 2:** $\frac{(-0.287879)(0.712121)}{2}(-0.0099) = \frac{-0.2049947}{2}(-0.0099) = (-0.1024974)(-0.0099) = +0.0010148$
- **Term 3:** Third difference is zero, so this term vanishes: $0$
- **Term 4:** $\frac{(-0.287879)(0.712121)(1.712121)(2.712121)}{24}(0.0002) = \frac{-0.9518889}{24}(0.0002) = -0.0000079$

Summing all terms together:

$$
y = 0.9996 - 0.0006045 + 0.0010148 - 0.0000079 = 1.0000023
$$

Rounding to four decimal places gives:

$$
y_{\max} = 1.0000
$$

$$
\boxed{x = 1.57 \text{ (correct to two decimal places)}, \qquad y_{\max} = 1.0000}
$$

---

## 🔍 Tutor Deep Dive: What Happened Behind the Numbers?

> [!NOTE] Why is $y_{\max} = 1.0000$ slightly above the table's largest entry ($0.9996$)?
> A common student worry: *"The table ends at 0.9996. Can the maximum really be 1.0000?"*
>
> Absolutely yes! Think about what a smooth curve does. At $x = 1.5$, $y = 0.9975$. At $x = 1.6$, $y = 0.9996$.
> Because the curve is still rising between $1.5$ and $1.6$ (the slope is positive), it must reach its peak slightly before $x = 1.6$ and then turn downward, reaching $0.9996$ at $x = 1.6$.
> That means the peak value $1.0000023$ must be slightly higher than $0.9996$.
> Never "round down" or "force" the maximum to match the table value of $0.9996$. The interpolated peak and the tabulated sample points are different quantities.

> [!NOTE] Verifying with a completely independent route: 5-Point Lagrange Interpolation
> If you fit a single quartic polynomial through all five points using Lagrange interpolation, you get:
> $$
> y(x) = \frac{x^4}{12} - \frac{29x^3}{60} + \frac{133x^2}{240} + \frac{409x}{750} + \frac{71}{500}
> $$
> Differentiating with respect to $x$:
> $$
> y'(x) = \frac{x^3}{3} - \frac{29x^2}{20} + \frac{133x}{120} + \frac{409}{750}
> $$
> Solving $y'(x) = 0$ gives three real roots: $x = -0.3344$, $x = 1.5713$, and $x = 3.1131$.
> Only $x = 1.5713$ lies inside our data span $[1.2, 1.6]$.
> Evaluating $y$ at $x = 1.5713$ yields $y = 1.0000023$, matching the backward-difference result to seven decimal places!
> Checking the second derivative confirms it is a maximum:
> $$
> y''(1.5713) = (1.5713)^2 - \frac{29(1.5713)}{10} + \frac{133}{120} = -0.9795 < 0
> $$

---

## ⚡ Quick Review

**The method in one sentence:** Build a difference table, use the Newton backward derivative formula to set $\frac{dy}{dx} = 0$, solve for the fractional displacement $q$, and evaluate the polynomial at that $q$.

**The formulas you must memorize:**
$$
\frac{dy}{dx} = \frac{1}{h}\left[\nabla y_n + \frac{2q+1}{2}\nabla^2 y_n\right] = 0 \implies q = -\frac{\nabla y_n}{\nabla^2 y_n} - 0.5
$$
$$
x = x_n + hq, \qquad y_{\max} = y_n + q\nabla y_n + \frac{q(q+1)}{2}\nabla^2 y_n + \dots
$$

**The most common exam mistake:** Forgetting the factor of $\frac{1}{h}$ when writing the derivative, or mistaking the negative sign of $q$ (a negative $q$ simply means moving backward into the table).

**Time estimate in exam:** 10 to 12 minutes for a complete 6-mark table problem.

---

## 🔗 Connected Topics

- [← NM-6.2: One-Dimensional Unconstrained Optimization](NM-6.2_Unconstrained_Optimization.md): Finds optima when an analytical function formula is given.
- [→ NM-7.1: Difference Formulas](../NM-7_Differentiation/NM-7.1_Difference_Formulas.md): Uses the same finite difference expansions to evaluate derivatives at arbitrary points.
- [NM-4.11: Difference Tables](../NM-4_Curve_Fitting/NM-4.11_Difference_Tables.md): How to form and check diagonal difference tables.

---

[← Previous: NM-6.2 Unconstrained Optimization](NM-6.2_Unconstrained_Optimization.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: NM-7.1 Difference Formulas →](../NM-7_Differentiation/NM-7.1_Difference_Formulas.md)
