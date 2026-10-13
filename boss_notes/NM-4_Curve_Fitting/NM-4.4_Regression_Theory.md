[← Previous: NM-4.3 Nonlinear Regression](NM-4.3_Nonlinear_Regression.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: NM-4.5 Linear Interpolation →](NM-4.5_Linear_Interpolation.md)

---

# NM-4.4: Regression Theory & Criteria

> 🟠 ⚠️ **Priority:** Secondary (Exam Trap) | **Tested:** 2 appearances (2017, 2019) | **Typical marks:** 4

## What This Is (and Why It Matters)

When someone first learns about curve fitting, their immediate reaction is: *Why do we square the errors? Why not just add the errors up, or take their absolute values?*

That is not just a student question: RUET examiners love asking this exact question in semester finals. If you do not know the mathematical flaws of the alternative error criteria, you lose 4 easy marks. In this note, we examine the three obvious error criteria, show why each one breaks down mathematically, and explain why least squares is the undisputed gold standard of engineering regression.

---

## 📝 Key Definitions

> **Least-Squares Criterion:** "The curve drawn is such that the discrepancy between the data points and the curve is least. In the method of least squares, the sum of the squares of the errors is minimized." -- Jain, §4.1 (p. 126)
>
> **In simple words:** The rule that says: measure each vertical error, square it, add them up, and find the curve that minimizes this total squared sum.

> **Residual:** "If $e_i$ is the error of approximation at $x = x_i$, then we have $e_i = y_i - f(x_i)$." -- Jain, §4.2 (p. 127)
>
> **In simple words:** The vertical gap between the real data point and the curve you drew. If the point sits above your curve, the residual is positive; if it sits below, it is negative.

---

## The Core Idea: Why Alternative Criteria Fail

When fitting a curve $y = f(x)$ to $n$ data points $(x_i, y_i)$, we want the residuals $e_i = y_i - f(x_i)$ to be as small as possible. Let's look at three intuitive alternatives to least squares and see why they fail.

### Criterion 1: Minimum Sum of Errors ($\sum e_i = 0$)

The simplest idea is to add up all the errors and try to make the total zero:

$$
\sum_{i=1}^n e_i = \sum_{i=1}^n [y_i - f(x_i)] = 0
$$

**The fatal flaw:** Positive and negative errors cancel each other out completely.
Suppose you have two data points. Your line passes 10 units *above* the first point ($e_1 = -10$) and 10 units *below* the second point ($e_2 = +10$). The sum of errors is:

$$
(-10) + (+10) = 0
$$

Your sum of errors is zero, yet your line completely misses both points. In fact, an infinite number of terrible, slanted lines will have zero total error. This criterion is useless.

![Comparison of regression error criteria: minimum sum of errors allows cancelling errors, minimum absolute error yields non-unique fits, and least squares produces a unique optimum](../diagrams/2017_Q6a_regression_criteria.png)

---

### Criterion 2: Minimum Sum of Absolute Errors ($\sum |e_i|$)

To stop positive and negative errors from canceling, you could take absolute values:

$$
S_{\text{abs}} = \sum_{i=1}^n |e_i| = \sum_{i=1}^n |y_i - f(x_i)|
$$

**The fatal flaw:** The absolute value function $|e|$ has a sharp "V" corner at $e = 0$.
Because it has a sharp corner, its derivative does not exist at zero ($\frac{d|e|}{de}$ is undefined at $e=0$). You cannot take partial derivatives and set them to zero to get nice linear normal equations. To solve it, you must use iterative linear programming (like the Simplex algorithm), which is difficult to do by hand on an exam paper.

Also, the solution is often **not unique**. You can tilt the line slightly without changing the sum of absolute deviations, meaning there is no single best line.

---

### Criterion 3: Minimum Single Error or Minimax ($\min_i |e_i|$)

What if we try to make at least one point have the smallest possible error?

$$
\min_{i} |e_i| \to 0
$$

**The fatal flaw:** This criterion focuses entirely on one lucky point. It forces the line directly through one single data point while completely ignoring the remaining $n-1$ data points, even if they sit miles away.

---

### Why the Least-Squares Criterion Wins

Minimizing the sum of squared errors:

$$
S = \sum_{i=1}^n e_i^2 = \sum_{i=1}^n [y_i - f(x_i)]^2
$$

is the standard engineering criterion because of three powerful mathematical reasons:

1. **No cancellation:** Squaring makes every term non-negative ($e_i^2 \ge 0$). An error of $+5$ and an error of $-5$ both become $+25$.
2. **Smooth, unique minimum with linear equations:** The function $S(a, b)$ is a smooth, continuous bowl (a paraboloid). Its partial derivatives are linear in the unknown parameters. Setting $\frac{\partial S}{\partial a} = 0$ and $\frac{\partial S}{\partial b} = 0$ yields a set of linear normal equations that can be solved directly by basic algebra.
3. **Statistical optimality (Gauss-Markov Theorem):** If experimental measurement noise is independent, zero-mean, and normally distributed (Gaussian noise), least squares is proven to be the **maximum-likelihood estimator**. It provides the most probable physical line in the presence of natural random noise.

---

## 🏆 Past Exam Questions

### 2017 Q.6(a): Compare Error Criteria with Figures [04 Marks]

**The question:** With necessary figure(s) explain why minimum sum of error, minimum sum of absolute error and minimum error are ill-suited for regression. Which criterion is best suited for regression?

**Let's answer this step by step, exactly as expected by examiners.**

**1. Why Minimum Sum of Error ($\sum e_i = 0$) is ill-suited:**
Positive and negative residuals cancel each other out. Consider two points where one sits 5 units above the line and the other sits 5 units below:

![Comparison of regression error criteria: minimum sum of errors allows cancelling errors, minimum absolute error yields non-unique fits, and least squares produces a unique optimum](../diagrams/2017_Q6a_regression_criteria.png)

The sum of errors is $(+5) + (-5) = 0$. This condition is satisfied by infinitely many different lines, including lines that fail to capture the data trend completely.

**2. Why Minimum Sum of Absolute Error ($\sum |e_i|$) is ill-suited:**
Taking absolute values removes sign cancellation, but $|e_i|$ has a sharp non-differentiable corner at zero. Because partial derivatives $\frac{\partial}{\partial a}$ and $\frac{\partial}{\partial b}$ do not exist when residuals are zero, we cannot write simple linear normal equations. Also, the optimal fit is often non-unique.

**3. Why Minimum Error ($\min_i |e_i|$) is ill-suited:**
Minimizing the smallest error focuses on a single point. It forces the line through that one point while allowing the errors at all other $n-1$ points to become arbitrarily large.

**4. The Best Suited Criterion: Least-Squares Criterion**
Minimizing the sum of squared residuals:

$$
S = \sum_{i=1}^n e_i^2 = \sum_{i=1}^n [y_i - f(x_i)]^2
$$

is the best suited criterion because:
- **No cancellation:** Squaring guarantees $e_i^2 \ge 0$ for all points.
- **Smooth, closed-form solution:** Differentiating $S$ yields linear normal equations with a guaranteed unique, closed-form solution.
- **Heavily penalizes outliers:** Squaring penalizes large deviations much more severely than small deviations.
- **Statistically optimal:** For normally distributed noise, least squares yields the maximum-likelihood estimate.

$$
\boxed{S = \sum_{i=1}^{n}\left(y_i - f(x_i)\right)^2 \text{ is the criterion to minimise}}
$$

---

## ⚡ Quick Review

**The three flaws to remember:**
1. $\sum e_i = 0 \implies$ positive and negative errors cancel out.
2. $\sum |e_i| \implies$ sharp corners at zero, non-differentiable, no linear normal equations.
3. $\min |e_i| \implies$ fits one point, ignores the other $n-1$ points.

**The least-squares formula you must write:**
$$
S = \sum_{i=1}^n [y_i - f(x_i)]^2
$$

**Time estimate in exam:** ~5 minutes to sketch the sketch and list the three reasons.

---

## 🔗 Connected Topics

- [← NM-4.3: Nonlinear Regression](NM-4.3_Nonlinear_Regression.md) -- applying the least squares criterion to linearized curves.
- [→ NM-4.5: Linear Interpolation](NM-4.5_Linear_Interpolation.md) -- when data is exact and you connect points with chords instead of minimizing squared error.
- [NM-4.2: Linear Regression](NM-4.2_Linear_Regression.md) -- full mathematical derivation of normal equations from the least-squares criterion.

---

[← Previous: NM-4.3 Nonlinear Regression](NM-4.3_Nonlinear_Regression.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: NM-4.5 Linear Interpolation →](NM-4.5_Linear_Interpolation.md)
