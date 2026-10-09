---
title: "NM-4.4 · Regression Criteria & Theory"
tags:
  - numerical-methods
  - discrete-mathematics
  - topicwise
---

# NM-4.4 · Regression Criteria & Theory

Every block below is copied from `../answers_explanation/`. The reasoning
is written once, in the year-wise file, and is not restated here.


### [2017 Q.6(a)]

**Question.** With necessary figure(s) explain why minimum sum of error, minimum sum of absolute error and minimum error are ill-suited for regression. Which criterion is best suited for regression?

*[Marks: 04]*

**Solution.**

Take four data points, three of which lie near the line and one of which is a
spuriously displaced measurement.

```text
 y
 ^         .          .
 |      .        .          o <- (x4, y4) outlier
 |   .            .
 |  .         .            <- the true relation
 | .      .
 |________________________> x
```

**Criterion 1: minimum sum of errors, $\sum e_i = 0$.** The positive and
negative errors cancel, so this condition is satisfied by *infinitely many*
curves, including curves that pass through none of the data. A line far above
three points and far below a fourth gives $\sum e_i = 0$ while fitting nothing.

```text
   .            .
        sum e = +2
   .
        sum e = -2      -> total 0, but a terrible fit
```

**Criterion 2: minimum sum of absolute errors, $\sum\lvert e_i\rvert$.**
Cancellation is removed, so the criterion is a genuine measure of badness.
However $\sum\lvert e_i\rvert$ is piecewise linear in the curve's parameters,
its minimum often lies where the slope is not defined, and no normal equations
result. The condition is satisfied by several distinct curves whenever they
share the same total absolute deviation.

```text
   .            .
        |e| = 2
   .
        |e| = 2      -> total 4, minimum, but not unique
```

**Criterion 3: minimum error, $\min_i \lvert e_i\rvert$.** A single error
considers one point only. Minimising it drives one residual to zero while the
others are ignored entirely, which is worse still: it fits the *outlier*
perfectly if the outlier is the smallest residual.

**The criterion that is best suited.** The **least-squares criterion**,
minimising the sum of squared errors,

$$\boxed{S = \sum_{i=1}^{n}\left(y_i - f(x_i)\right)^2 \text{ is the criterion to minimise}}$$

Its three properties make it the standard.

1. **No cancellation**, since the square is always non-negative.
2. **A unique, smooth minimum**, and the normal equations
   $\partial S/\partial a_j = 0$ are *linear* in the parameters, so they have a
   closed-form solution.
3. **A probabilistic justification**: if the measurement errors are independent
   and normally distributed with equal variance, the least-squares fit is the
   maximum-likelihood estimate.

> [!note] Why property 3 is the deepest of the three
> Properties 1 and 2 make least squares *convenient*. Property 3 makes it
> *right*. Nothing forces a curve-fitter to minimise $\sum e_i^2$; it is simply
> that when the errors are independent Gaussian samples with a common variance,
> that is the curve the data are most likely to have come from. The other two
> criteria correspond to error models where one datum outweighs all the others
> by an unbounded factor, which is a strange thing to believe about a
> voltmeter.

---

---

**Also asked here.**

- *2019 Q.4(a)* is the same question as [[NM-4.1_Concepts|NM-4.1]], which is written in `NM-4.1`.

---
