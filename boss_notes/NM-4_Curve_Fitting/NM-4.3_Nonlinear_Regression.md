[← Previous: NM-4.2 Linear Regression](NM-4.2_Linear_Regression.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: NM-4.4 Regression Theory →](NM-4.4_Regression_Theory.md)

---

# NM-4.3: Non-Linear Regression

> 🔴 ⚠️ **Priority:** Critical (Danger Zone) | **Tested:** 3/8 years | **Typical marks:** 4

## What This Is (and Why It Matters)

Just like linear regression, this subtopic was skipped in regular classroom lectures but showed up in 3 semester finals. When real engineering data does not follow a straight line (for instance, the exponential growth of semiconductor current or a saturation curve), you cannot use $y = a + bx$ directly.

Directly fitting a nonlinear curve using nonlinear least squares requires messy iterative optimization. But here is the secret trick: almost every nonlinear curve examined in RUET can be straightened into a simple line using logarithms or reciprocals. Once straightened out, you solve it using the exact same linear regression formulas you already know.

---

## 📝 Key Definitions

> **Linearization of Nonlinear Laws:** "The given data may not always follow a linear relationship. This can be ascertained from a plot of the given data. If a nonlinear model is to be fitted, it can be conveniently transformed to a linear relationship." -- Jain, §4.2.3 (p. 130)
>
> **In simple words:** Using an algebraic substitution (like taking logarithms or flipping fractions) to turn a curved relationship into a straight line so you can solve it easily with standard slope and intercept formulas.

> **Exponential Law:** "In this case, we write $\ln y = \ln a + bx \Rightarrow Y = A_0 + A_1 X$, where $Y = \ln y$, $A_0 = \ln a$, $A_1 = b$ and $X = x$." -- Jain, §4.2.3 (p. 131)
>
> **In simple words:** An equation where $x$ sits up in the exponent. Taking the natural logarithm brings the $x$ down from the exponent, turning the exponential curve into a straight line with slope $b$ and intercept $\ln a$.

---

## The Core Idea

The exam primarily tests two types of nonlinear curves:
1. The **Exponential Model:** $y = a e^{bx}$
2. The **Saturation / Reciprocal Model:** $y = \dfrac{x}{a + bx}$

Let's master the transformation trick for both.

### Model 1: The Exponential Curve $y = a e^{bx}$

Take the natural logarithm ($\ln$) of both sides:

$$
\ln y = \ln(a e^{bx}) = \ln a + \ln(e^{bx}) = \ln a + bx
$$

Define your new linear variables:

$$
Y = \ln y, \qquad A = \ln a, \qquad X = x
$$

Now you have a straight line:

$$
Y = A + bX
$$

- The slope is $b$.
- The intercept is $A$. Once you calculate $A$, recover the original constant by exponentiating: $a = e^A$.

### Model 2: The Saturation / Reciprocal Curve $y = \dfrac{x}{a + bx}$

Flip both sides upside down:

$$
\frac{1}{y} = \frac{a + bx}{x} = \frac{a}{x} + \frac{bx}{x} = a\left(\frac{1}{x}\right) + b
$$

Define your transformed variables:

$$
v = \frac{1}{y}, \qquad u = \frac{1}{x}
$$

Look at what you have:

$$
v = a u + b
$$

Notice the roles of the constants here:
- **Slope:** $a$
- **Intercept:** $b$

### Common Transformations Cheat Sheet

| Nonlinear Model | Algebraic Trick | Transformed Line | Slope | Intercept |
| :-- | :-- | :-- | :-- | :-- |
| **Exponential:** $y = ae^{bx}$ | Take $\ln$ | $\ln y = \ln a + bx$ | $b$ | $A = \ln a \implies a = e^A$ |
| **Reciprocal:** $y = \dfrac{x}{a + bx}$ | Take $1/y$ | $\dfrac{1}{y} = a\left(\dfrac{1}{x}\right) + b$ | $a$ | $b$ |
| **Power law:** $y = ax^b$ | Take $\log_{10}$ | $\log y = \log a + b\log x$ | $b$ | $A = \log a \implies a = 10^A$ |
| **General exponential:** $y = ab^x$ | Take $\log_{10}$ | $\log y = \log a + x\log b$ | $B = \log b \implies b = 10^B$ | $A = \log a \implies a = 10^A$ |

> [!WARNING] Common Trap
> Do not forget to invert your parameters at the end. In an exponential fit, students often find $A = 0.405$ and write $a = 0.405$. That is wrong. $A$ is $\ln a$, so you must calculate $a = e^{0.405} \approx 1.50$.
> Also, in the reciprocal fit $y = x/(a+bx)$, $a$ is the **slope** and $b$ is the **intercept**. Do not swap them.

---

## 🔧 Worked Example

> **From:** 2017 Q.5(b) / 2020 Q.3(c) -- [Marks: 04]

**The question:** Determine constants $a$ and $b$ by the method of least squares such that $y = a e^{bx}$ fits the following data:

| $x$ | 2 | 4 | 6 | 8 | 10 |
| :---: | :---: | :---: | :---: | :---: | :---: |
| $y$ | 4.077 | 11.084 | 30.128 | 81.897 | 222.62 |

**Let's solve this step by step.**

**Step 1: Straighten the equation**
Take natural logarithms:

$$
\ln y = \ln a + bx \implies Y = A + bx
$$

where $Y = \ln y$ and $A = \ln a$.

**Step 2: Build the transformed data table ($n = 5$)**
Use your calculator's $\ln$ button to transform each $y$ value:

| $x$ | $y$ | $Y = \ln y$ | $x^2$ | $xY$ |
| :--: | :--: | :--: | :--: | :--: |
| 2 | 4.077 | 1.405361 | 4 | 2.810722 |
| 4 | 11.084 | 2.405503 | 16 | 9.622012 |
| 6 | 30.128 | 3.405455 | 36 | 20.432730 |
| 8 | 81.897 | 4.405462 | 64 | 35.243696 |
| 10 | 222.62 | 5.405466 | 100 | 54.054660 |
| **$\sum x = 30$** | -- | **$\sum Y = 17.027248$** | **$\sum x^2 = 220$** | **$\sum xY = 122.163825$** |

*Tutor insight:* Notice how $Y$ jumps by almost exactly $1.0000$ every time $x$ increases by $2$. That tells you right away that $b \approx 1.0 / 2.0 = 0.5$.

**Step 3: Calculate the slope $b$**

$$
b = \frac{n\sum xY - \sum x\sum Y}{n\sum x^2 - (\sum x)^2} = \frac{5(122.163825) - (30)(17.027248)}{5(220) - 30^2}
$$

$$
b = \frac{610.819125 - 510.817440}{1100 - 900} = \frac{100.001685}{200} = 0.500008 \approx 0.50
$$

**Step 4: Calculate the intercept $A$ and recover $a$**

Find the means:

$$
\bar{x} = \frac{30}{5} = 6.0, \qquad \bar{Y} = \frac{17.027248}{5} = 3.405450
$$

Calculate $A$:

$$
A = \bar{Y} - b\bar{x} = 3.405450 - (0.500008)(6.0) = 3.405450 - 3.000048 = 0.405402
$$

Now recover $a$ by exponentiating:

$$
a = e^A = e^{0.405402} = 1.4999 \approx 1.50
$$

So the constants are:

$$
\boxed{a = 1.50, \qquad b = 0.5}
$$

**Quick sanity check:**
Plug $x = 2$ into $y = 1.5e^{0.5x}$:
$y(2) = 1.5 e^{1.0} = 1.5(2.71828) = 4.0774$. Matches $4.077$ perfectly!

---

## 🏆 Past Exam Questions

### 2022 Q.2(b): Saturation Curve Fitting [04 Marks]

**The question:** Using the method of least squares, fit a curve of the form $y = \frac{x}{a + bx}$ to fit the following data: $(3, 7.148)$, $(5, 10.231)$, $(8, 13.509)$, $(12, 16.434)$.

**Let's solve this step by step.**

**Step 1: Straighten the equation**
Take reciprocals:

$$
\frac{1}{y} = \frac{a + bx}{x} = a\left(\frac{1}{x}\right) + b
$$

Define:

$$
u = \frac{1}{x}, \qquad v = \frac{1}{y} \implies v = au + b
$$

Here the slope is $a$ and the intercept is $b$.

**Step 2: Table of transformed data ($n = 4$)**

| $x$ | $y$ | $u = 1/x$ | $v = 1/y$ |
| :--: | :--: | :--: | :--: |
| 3 | 7.148 | 0.333333 | 0.139899 |
| 5 | 10.231 | 0.200000 | 0.097742 |
| 8 | 13.509 | 0.125000 | 0.074025 |
| 12 | 16.434 | 0.083333 | 0.060849 |

**Step 3: Compute the sums**

$$
\sum u = 0.333333 + 0.200000 + 0.125000 + 0.083333 = 0.741666
$$

$$
\sum v = 0.139899 + 0.097742 + 0.074025 + 0.060849 = 0.372515
$$

$$
\sum u^2 = (0.333333)^2 + (0.2)^2 + (0.125)^2 + (0.083333)^2 = 0.111111 + 0.040000 + 0.015625 + 0.006944 = 0.173680
$$

$$
\sum uv = (0.333333)(0.139899) + (0.2)(0.097742) + (0.125)(0.074025) + (0.083333)(0.060849) = 0.080505
$$

**Step 4: Solve for slope $a$ and intercept $b$**

$$
a = \frac{n\sum uv - \sum u\sum v}{n\sum u^2 - (\sum u)^2} = \frac{4(0.080505) - (0.741666)(0.372515)}{4(0.173680) - (0.741666)^2}
$$

$$
a = \frac{0.322020 - 0.276281}{0.694720 - 0.550069} = \frac{0.045739}{0.144651} = 0.316202 \approx 0.3162
$$

Now calculate the means:

$$
\bar{u} = \frac{0.741666}{4} = 0.185417, \qquad \bar{v} = \frac{0.372515}{4} = 0.093129
$$

Calculate intercept $b$:

$$
b = \bar{v} - a\bar{u} = 0.093129 - (0.316202)(0.185417) = 0.093129 - 0.058629 = 0.034500 \approx 0.0345
$$

**Step 5: Write the final fitted equation**
Insert $a = 0.3162$ and $b = 0.0345$ into the original function:

$$
\boxed{y = \frac{x}{0.3162 + 0.0345x}}
$$

**Residual check:**
For $x = 3$: $\hat{y} = \frac{3}{0.3162 + 0.0345(3)} = \frac{3}{0.4197} = 7.1480$. Exactly matches $7.148$!

---

## ⚡ Quick Review

**The method in one sentence:** Transform the nonlinear function into a straight line by taking logarithms or reciprocals, solve for the linear slope and intercept, and invert the constants back.

**The two transformation formulas to memorize:**
1. $y = ae^{bx} \implies \ln y = \ln a + bx \quad (Y = A + bx \text{ with } a = e^A)$
2. $y = \dfrac{x}{a + bx} \implies \dfrac{1}{y} = a\left(\dfrac{1}{x}\right) + b \quad (v = au + b \text{ with slope } a, \text{ intercept } b)$

**The most common exam mistake:** Forgetting that in $v = au + b$, $a$ is the slope and $b$ is the intercept. If you swap them, your model gives completely backwards results.

**Time estimate in exam:** ~7 minutes to transform data, sum columns, and evaluate constants.

---

## 🔗 Connected Topics

- [← NM-4.2: Linear Regression](NM-4.2_Linear_Regression.md) -- the core linear formulas used by every transformed model.
- [→ NM-4.4: Regression Theory](NM-4.4_Regression_Theory.md) -- why least squares is the mathematically superior error criterion.
- [NM-4.1: Concepts](NM-4.1_Concepts.md) -- why we fit curves instead of forcing lines through noisy points.

---

[← Previous: NM-4.2 Linear Regression](NM-4.2_Linear_Regression.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: NM-4.4 Regression Theory →](NM-4.4_Regression_Theory.md)
