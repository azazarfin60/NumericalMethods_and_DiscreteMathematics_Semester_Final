[← Previous: NM-4.1 Concepts](NM-4.1_Concepts.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: NM-4.3 Nonlinear Regression →](NM-4.3_Nonlinear_Regression.md)

---

# NM-4.2: Least-Squares Linear Regression

> 🔴 ⚠️ **Priority:** Critical (Danger Zone) | **Tested:** 4/8 years | **Typical marks:** 4–5

## What This Is (and Why It Matters)

Here is a big warning: this topic was completely absent from student lecture notes, yet it appeared in 4 out of 8 semester final exams. If you only study from classroom lecture notebooks, you walk straight into an exam ambush.

The mathematics itself is straightforward and very satisfying. You have a table of experimental $(x, y)$ pairs, and you want to draw the best straight line $y = a + bx$ through them. Instead of eyeballing it with a plastic ruler, you use calculus to minimize the sum of squared errors. That produces two simple equations (the normal equations) that give you the exact slope $b$ and intercept $a$.

---

## 📝 Key Definitions

> **Method of Least Squares:** "Let the set of data points be $(x_i, y_i), i = 1, 2, \dots, m$, and let the curve given by $Y = f(x)$ be fitted to this data. At $x = x_i$, the given ordinate is $y_i$ and the corresponding value on the fitting curve is $f(x_i)$. If $e_i$ is the error of approximation at $x = x_i$, then we have $e_i = y_i - f(x_i)$. If we write $S = e_1^2 + e_2^2 + \dots + e_m^2$, then the method of least squares consists in minimizing $S$, i.e., the sum of the squares of the errors." -- Jain, §4.2 (p. 126–127)
>
> **In simple words:** For every data point, measure the vertical distance between the actual dot and your line. Square each distance (so negatives become positive and bigger misses hurt more), add them all up, and adjust your line until that total sum of squares is as small as mathematically possible.

> **Normal Equations:** "Equations (4.6) are called the *normal equations*, and can be solved for $a_0$ and $a_1$, since $x_i$ and $y_i$ are known quantities." -- Jain, §4.2.1 (p. 128)
>
> **In simple words:** The two simultaneous algebraic equations you get by setting the partial derivatives of the squared error to zero. You solve them just like school simultaneous equations to find the intercept $a$ and slope $b$.

> **Goodness of Fit (Correlation Coefficient):** "The correlation coefficient (cc) is defined as $\text{cc} = \sqrt{\dfrac{S_y - S}{S_y}}$, where $S_y = \sum_{i=1}^m (y_i - \bar{y})^2$ and $S = \sum_{i=1}^m [y_i - f(x_i)]^2$. If cc is close to 1, then the fit is considered to be good." -- Jain, §4.2.1 (p. 128)
>
> **In simple words:** A number between 0 and 1 that grades your line. A score near 1 means your points hug the line tightly; a score near 0 means your points are scattered like random shotgun pellets.

---

## The Core Idea

Let's derive the entire method from first principles so you can reproduce it on an exam sheet in five minutes flat.

### 1. Formulating the Problem

We are given $n$ experimental data pairs:

$$
(x_1, y_1), (x_2, y_2), \dots, (x_n, y_n)
$$

We want to fit a straight line:

$$
\hat{y} = a + bx
$$

At each point $i$, the difference between the true reading $y_i$ and the line's prediction is the residual:

$$
r_i = y_i - (a + bx_i)
$$

The sum of squared residuals is our objective function:

$$
S(a, b) = \sum_{i=1}^n r_i^2 = \sum_{i=1}^n [y_i - (a + bx_i)]^2
$$

We want to find the values of $a$ and $b$ that minimize $S$.

### 2. Deriving the Normal Equations

To find the minimum of a smooth 2D surface, both partial derivatives must equal zero:

$$
\frac{\partial S}{\partial a} = 0 \quad \text{and} \quad \frac{\partial S}{\partial b} = 0
$$

Let's differentiate with respect to intercept $a$:

$$
\frac{\partial S}{\partial a} = \sum_{i=1}^n 2[y_i - (a + bx_i)](-1) = -2 \sum_{i=1}^n [y_i - a - bx_i] = 0
$$

Divide by $-2$ and break up the summation:

$$
\sum_{i=1}^n y_i - \sum_{i=1}^n a - b \sum_{i=1}^n x_i = 0
$$

Because adding the constant $a$ across $n$ points gives $na$, we get the **First Normal Equation**:

$$
na + b \sum x_i = \sum y_i
$$

Now differentiate with respect to slope $b$:

$$
\frac{\partial S}{\partial b} = \sum_{i=1}^n 2[y_i - (a + bx_i)](-x_i) = -2 \sum_{i=1}^n [x_i y_i - ax_i - bx_i^2] = 0
$$

Divide by $-2$ and break up the summation to get the **Second Normal Equation**:

$$
a \sum x_i + b \sum x_i^2 = \sum x_i y_i
$$

### 3. Solving for Slope $b$ and Intercept $a$

Divide the first normal equation by $n$:

$$
a + b \bar{x} = \bar{y} \implies a = \bar{y} - b\bar{x}
$$

This tells you something wonderful: **the fitted line always passes through the data centroid $(\bar{x}, \bar{y})$!**

Substitute this expression for $a$ into the second normal equation:

$$
(\bar{y} - b\bar{x})\sum x_i + b\sum x_i^2 = \sum x_i y_i
$$

Using $\bar{y} = \frac{\sum y_i}{n}$ and $\bar{x} = \frac{\sum x_i}{n}$:

$$
\frac{\sum y_i}{n}\sum x_i - b\frac{(\sum x_i)^2}{n} + b\sum x_i^2 = \sum x_i y_i
$$

Multiply the whole equation by $n$:

$$
\left(\sum x_i\right)\left(\sum y_i\right) + b\left[n\sum x_i^2 - \left(\sum x_i\right)^2\right] = n\sum x_i y_i
$$

Rearrange to solve directly for the slope $b$:

$$
b = \frac{n \sum xy - \sum x \sum y}{n \sum x^2 - \left(\sum x\right)^2}
$$

Once you calculate $b$, the intercept $a$ is:

$$
a = \bar{y} - b\bar{x} = \frac{\sum y}{n} - b\frac{\sum x}{n}
$$

### Step-by-Step Algorithm for Numerical Problems

1. Count the number of data pairs $n$.
2. Create a neat 4-column table: $x$, $y$, $x^2$, and $xy$.
3. Compute the four column sums: $\sum x$, $\sum y$, $\sum x^2$, and $\sum xy$.
4. Calculate slope $b$ using the formula above.
5. Compute means $\bar{x} = \frac{\sum x}{n}$ and $\bar{y} = \frac{\sum y}{n}$.
6. Calculate intercept $a = \bar{y} - b\bar{x}$.
7. Write your final equation: $y = a + bx$.
8. **Sanity check:** Check if $a + b\bar{x} = \bar{y}$. It must match!

> [!WARNING] Common Trap
> Never confuse $\sum x^2$ with $(\sum x)^2$.
> - $\sum x^2$ means square each individual $x$ first, then sum them up: $1^2 + 2^2 + 3^2 = 14$.
> - $(\sum x)^2$ means sum the $x$ values first, then square the total: $(1 + 2 + 3)^2 = 6^2 = 36$.
> In the denominator, $n\sum x^2 - (\sum x)^2$ must always be strictly positive for distinct points.

---

## 🔧 Worked Example

> **From:** 2018 Q.4(c) -- [Marks: 05]

**The question:** The following data was taken from an experiment measuring current in a wire for various imposed voltages:

| $v$ (V) | 2 | 3 | 4 | 5 | 7 | 10 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| $i$ (A) | 5.2 | 7.8 | 10.7 | 13 | 19.3 | 27.5 |

On the basis of a linear regression of this data, determine current for a voltage of $3.5\text{ V}$. Plot the line to evaluate the fit.

**Let's solve this step by step.**

**Step 1: Set up the calculation table ($n = 6$)**

| $v$ | $i$ | $v^2$ | $vi$ |
| :--: | :--: | :--: | :--: |
| 2 | 5.2 | 4 | 10.4 |
| 3 | 7.8 | 9 | 23.4 |
| 4 | 10.7 | 16 | 42.8 |
| 5 | 13.0 | 25 | 65.0 |
| 7 | 19.3 | 49 | 135.1 |
| 10 | 27.5 | 100 | 275.0 |
| **$\sum v = 31$** | **$\sum i = 83.5$** | **$\sum v^2 = 203$** | **$\sum vi = 551.7$** |

**Step 2: Calculate the slope $b$**

$$
b = \frac{n\sum vi - \sum v\sum i}{n\sum v^2 - \left(\sum v\right)^2} = \frac{6(551.7) - (31)(83.5)}{6(203) - 31^2} = \frac{3310.2 - 2588.5}{1218 - 961} = \frac{721.7}{257} = 2.8082\ \text{A/V}
$$

**Step 3: Calculate the intercept $a$**

Find the means first:

$$
\bar{v} = \frac{31}{6} \approx 5.1667\ \text{V}, \qquad \bar{i} = \frac{83.5}{6} \approx 13.9167\ \text{A}
$$

Now compute $a$:

$$
a = \bar{i} - b\bar{v} = 13.9167 - (2.8082)(5.1667) = 13.9167 - 14.5089 = -0.5922\ \text{A}
$$

So the fitted linear regression line is:

$$
\boxed{i = -0.5922 + 2.8082\,v}
$$

**Step 4: Predict current at $v = 3.5\text{ V}$**

Plug $v = 3.5$ directly into your fitted line:

$$
i(3.5) = -0.5922 + 2.8082(3.5) = -0.5922 + 9.8287 = 9.2364\ \text{A}
$$

$$
\boxed{i(3.5\ \text{V}) = 9.2364\ \text{A}}
$$

**Step 5: Visualizing and evaluating the fit**

![Linear regression plot of current versus voltage with measured points, fitted line, and evaluated point at 3.5V](../diagrams/nm4_regression_scatter_plot_2018.jpg)

The plot shows every measured data point sitting right on the fitted line. The correlation coefficient is $r = 0.9996$, confirming an exceptional linear fit representing Ohm's law.

---

## 🏆 Past Exam Questions

### 2017 Q.6(b) / 2024 Q.3(c): Fit a Straight Line [04 Marks]

**The question:** Fit a straight line to the $x$ and $y$ values in the first two columns of the following table:

| $x$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| $y$ | 0.5 | 2.5 | 2.0 | 4.0 | 3.5 | 6.0 | 5.5 |

**Let's solve this step by step.**

Here $n = 7$. Let's compute the four sums:

$$
\sum x = 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28
$$

$$
\sum y = 0.5 + 2.5 + 2.0 + 4.0 + 3.5 + 6.0 + 5.5 = 24
$$

$$
\sum x^2 = 1^2 + 2^2 + 3^2 + 4^2 + 5^2 + 6^2 + 7^2 = 1 + 4 + 9 + 16 + 25 + 36 + 49 = 140
$$

For $\sum xy$:

$$
\sum xy = 1(0.5) + 2(2.5) + 3(2.0) + 4(4.0) + 5(3.5) + 6(6.0) + 7(5.5) = 0.5 + 5 + 6 + 16 + 17.5 + 36 + 38.5 = 119.5
$$

**Setting up the normal equations:**
1. $7a + 28b = 24$
2. $28a + 140b = 119.5$

Multiply equation (1) by $4$:

$$
28a + 112b = 96
$$

Subtract this from equation (2):

$$
28b = 119.5 - 96 = 23.5 \implies b = \frac{23.5}{28} = \frac{47}{56} \approx 0.839286
$$

Now substitute $b$ back into equation (1):

$$
7a = 24 - 28(0.839286) = 24 - 23.5 = 0.5 \implies a = \frac{0.5}{7} = \frac{1}{14} \approx 0.071429
$$

Rounding to four decimal places gives the fitted straight line:

$$
\boxed{y = 0.0714 + 0.8393x}
$$

**Quick check:** Check the sum of residuals $\sum (y_i - \hat{y}_i)$:
- $\hat{y} = [0.9107, 1.7500, 2.5893, 3.4286, 4.2679, 5.1071, 5.9464]$
- $e = [-0.4107, +0.7500, -0.5893, +0.5714, -0.7679, +0.8929, -0.4464]$
- $\sum e = 0.0000$. Verified!

---

### 2019 Q.4(c): Deduce the Linear Regression Expression [04 Marks]

**The question:** Deduce the linear regression expression.

**Let's write out the mathematical deduction cleanly.**

Let the $n$ data pairs be $(x_i, y_i)$. We want to fit the line $\hat{y} = a + bx$.
The residual at each point is $r_i = y_i - a - bx_i$.
The sum of squared residuals is:

$$
S(a, b) = \sum_{i=1}^n (y_i - a - bx_i)^2
$$

Setting the partial derivative with respect to $a$ to zero:

$$
\frac{\partial S}{\partial a} = -2\sum_{i=1}^n (y_i - a - bx_i) = 0 \implies \sum y_i = na + b\sum x_i
$$

Setting the partial derivative with respect to $b$ to zero:

$$
\frac{\partial S}{\partial b} = -2\sum_{i=1}^n x_i(y_i - a - bx_i) = 0 \implies \sum x_i y_i = a\sum x_i + b\sum x_i^2
$$

From the first equation, solve for $a$:

$$
a = \frac{\sum y_i}{n} - b\frac{\sum x_i}{n} = \bar{y} - b\bar{x}
$$

Substitute this expression for $a$ into the second normal equation:

$$
(\bar{y} - b\bar{x})\sum x_i + b\sum x_i^2 = \sum x_i y_i
$$

$$
\bar{y}\sum x_i + b\left[\sum x_i^2 - \bar{x}\sum x_i\right] = \sum x_i y_i
$$

Replace $\bar{y} = \frac{\sum y_i}{n}$ and $\bar{x} = \frac{\sum x_i}{n}$:

$$
\frac{\sum x_i \sum y_i}{n} + b\left[\sum x_i^2 - \frac{(\sum x_i)^2}{n}\right] = \sum x_i y_i
$$

Multiply through by $n$:

$$
\sum x_i \sum y_i + b\left[n\sum x_i^2 - \left(\sum x_i\right)^2\right] = n\sum x_i y_i
$$

Isolate $b$:

$$
b = \frac{n\sum xy - \sum x\sum y}{n\sum x^2 - \left(\sum x\right)^2}
$$

Thus, the final linear regression expression is:

$$
\boxed{y = \left(\bar y - b\bar x\right) + bx \quad\text{with}\quad b = \frac{n\sum xy - \sum x \sum y}{n\sum x^2 - \left(\sum x\right)^2}}
$$

---

## ⚡ Quick Review

**The method in one sentence:** Minimize the sum of squared errors by setting partial derivatives to zero, which gives two linear normal equations for slope $b$ and intercept $a$.

**The formulas you must memorize:**
$$
b = \frac{n\sum xy - \sum x\sum y}{n\sum x^2 - (\sum x)^2}, \qquad a = \bar{y} - b\bar{x}
$$

**The most common exam mistake:** Mixing up $\sum x^2$ with $(\sum x)^2$ in the denominator of $b$. Always remember that the first is the sum of squares, while the second is the square of the sum.

**Time estimate in exam:** ~6 minutes to build the table and compute $a$ and $b$.

---

## 🔗 Connected Topics

- [← NM-4.1: Concepts](NM-4.1_Concepts.md) -- foundations and why least squares is the best criterion.
- [→ NM-4.3: Nonlinear Regression](NM-4.3_Nonlinear_Regression.md) -- linearizing exponential and reciprocal models so these exact linear formulas can solve them.
- [NM-4.4: Regression Theory](NM-4.4_Regression_Theory.md) -- why alternative error criteria like absolute error fail.

---

[← Previous: NM-4.1 Concepts](NM-4.1_Concepts.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: NM-4.3 Nonlinear Regression →](NM-4.3_Nonlinear_Regression.md)
