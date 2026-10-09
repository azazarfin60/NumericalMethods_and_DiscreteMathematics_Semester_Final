---
title: "NM-7.3 · Second Derivative & Formula Derivation"
tags:
  - numerical-methods
  - discrete-mathematics
  - topicwise
---

# NM-7.3 · Second Derivative & Formula Derivation

Every block below is copied from `../answers_exam_style/`, which is the
only place an answer is authored. A number here is the same number, character
for character, as the one it came from.


### [2017 Q.6(c)]

**Question.** Derive a formula to find the second derivative of a tabulated function.

**Solution.**

**Set-up.** Let $y = f(x)$ be tabulated at equally spaced nodes with interval
$h$, and write $p = \dfrac{x - x_0}{h}$. Newton's forward interpolation formula
is

$$y = y_0 + p\Delta y_0 + \frac{p(p-1)}{2!}\Delta^2 y_0 + \frac{p(p-1)(p-2)}{3!}\Delta^3 y_0 + \frac{p(p-1)(p-2)(p-3)}{4!}\Delta^4 y_0 + \cdots$$

**First derivative.** Since $dx = h\,dp$, differentiation with respect to $x$
is $(1/h)$ times differentiation with respect to $p$:

$$\frac{dy}{dx} = \frac{1}{h}\left[\Delta y_0 + \frac{2p-1}{2!}\Delta^2 y_0 + \frac{3p^2-6p+2}{3!}\Delta^3 y_0 + \frac{4p^3-18p^2+22p-6}{4!}\Delta^4 y_0 + \cdots\right]$$

The coefficient of $\Delta^k y_0$ is the derivative of the product
$p(p-1)\cdots(p-k+1)$ divided by $k!$. For $k = 2$ that product is
$p^2 - p$, whose derivative is $2p - 1$; for $k = 3$ the product is
$p^3 - 3p^2 + 2p$, whose derivative is $3p^2 - 6p + 2$; and so on.

**Second derivative.** Differentiating a second time:

$$\boxed{\frac{d^2y}{dx^2} = \frac{1}{h^2}\left[\Delta^2 y_0 + (p-1)\Delta^3 y_0 + \left(\frac{p^2}{2} - \frac{3p}{2} + \frac{11}{12}\right)\Delta^4 y_0 + \cdots\right]}$$

Each coefficient is the second derivative of the corresponding product,
divided by $k!$:

$$\frac{d^2}{dp^2}\left(p^2 - p\right) = 2$$

$$\frac{d^2}{dp^2}\left(p^3 - 3p^2 + 2p\right) = 6p - 6$$

$$\frac{d^2}{dp^2}\left(p^4 - 6p^3 + 11p^2 - 6p\right) = 12p^2 - 36p + 22$$

and dividing by $3!$ and $4!$ respectively gives $(p - 1)$ and
$\left(\dfrac{p^2}{2} - \dfrac{3p}{2} + \dfrac{11}{12}\right)$.

**Stopping rule.** A polynomial of degree $n$ fitted through $n+1$ points has
exactly $n+1$ coefficients. The differences of order greater than $n$ vanish
identically, so the series above terminates after the term in $\Delta^n y_0$.
Since $y''$ requires differences of order two and above, **at least three
points are needed** for the formula to carry any information, and a cubic fit
through four points carries terms up to $\Delta^3 y_0$.

**The backward counterpart.** Writing backward differences at the last node
$x_n$ and putting $q = \dfrac{x - x_n}{h}$,

$$\frac{d^2y}{dx^2} = \frac{1}{h^2}\left[\nabla^2 y_n + (q+1)\nabla^3 y_n + \left(\frac{q^2}{2} + \frac{3q}{2} + \frac{11}{12}\right)\nabla^4 y_n + \cdots\right]$$

which is the form used when the tabulation runs in the decreasing direction.

---

### [2018 Q.5(a)]

**Question.** State Newton's forward formula to evaluate $\frac{d^2 y}{dx^2}$ for any value $x \in [x_0, x_n]$.

**Solution.**

**Newton's forward formula.** For a tabular spacing $h$, the forward difference
interpolation polynomial through $n+1$ points is

$$y = y_0 + p\Delta y_0 + \frac{p(p-1)}{2!}\Delta^2 y_0 + \frac{p(p-1)(p-2)}{3!}\Delta^3 y_0 + \frac{p(p-1)(p-2)(p-3)}{4!}\Delta^4 y_0 + \cdots$$

with

$$p = \frac{x - x_0}{h}$$

**First derivative.** Differentiating term by term,
$\dfrac{d}{dx} = \dfrac{1}{h}\dfrac{d}{dp}$:

$$\frac{dy}{dx} = \frac{1}{h}\left[\Delta y_0 + \frac{2p - 1}{2!}\Delta^2 y_0 + \frac{3p^2 - 6p + 2}{3!}\Delta^3 y_0 + \frac{4p^3 - 18p^2 + 22p - 6}{4!}\Delta^4 y_0 + \cdots\right]$$

**Second derivative.** Differentiating a second time:

$$\frac{d^2y}{dx^2} = \frac{1}{h^2}\left[\Delta^2 y_0 + \frac{6p - 6}{3!}\Delta^3 y_0 + \frac{12p^2 - 36p + 22}{4!}\Delta^4 y_0 + \cdots\right]$$

which simplifies to

$$\boxed{\frac{d^2y}{dx^2} = \frac{1}{h^2}\left[\Delta^2 y_0 + (p - 1)\Delta^3 y_0 + \left(\frac{p^2}{2} - \frac{3p}{2} + \frac{11}{12}\right)\Delta^4 y_0 + \cdots\right]}$$

**Validity.** The formula reproduces $\dfrac{d^2y}{dx^2}$ exactly for any
polynomial of degree four or lower, because every term from $\Delta^5 y_0$
onward then vanishes. For a table of noisy experimental data the higher
differences are not zero, and they are also the noisiest entries in the
difference table, so the terms beyond the data's smoothness are not worth
retaining.

**Terms retained.** A polynomial of degree $n$ through $n+1$ points has exactly
$n+1$ coefficients, so for $n = 1$ only the $\Delta y_0$ term exists, for
$n = 2$ the terms up to $\Delta^2 y_0$ exist, and so on. Since $y''$ requires
differences of order two and above, the formula needs at least **three points**
for a quadratic fit, four for a cubic, and so on. The next term, omitted above,
is

$$\left(\frac{p^3}{6} - p^2 + \frac{7p}{4} - \frac{5}{6}\right)\Delta^5 y_0$$

> [!info] Check against the exact second derivative of a cubic
> The formula is exact for any polynomial of degree at most the number of
> points used, and a cubic is the first case where this can be tested. Take
> $y = ax^3$ tabulated from $x_0 = 0$ at spacing $h$, so $x = ph$. Then
> $\Delta y_n = ah^3(9n^2 + 9n + 3)$, $\Delta^2 y_0 = 6ah^3$ and
> $\Delta^3 y_0 = 6ah^3$, with all higher differences zero. The formula gives
> $\dfrac{1}{h^2}\left[6ah^3 + (p - 1)6ah^3\right] = 6ah\left[1 + p - 1\right] = 6aph$.
> The true second derivative is $y'' = 6ax = 6a(ph) = 6aph$. The two agree for
> every $p$, not only at the nodes, which is the property that makes the formula
> usable for interpolation rather than only for differencing. For a quadratic
> $y = ax^2 + bx + c$ only $\Delta^2 y_n = 2ah^2$ survives, and the formula
> reduces to $\dfrac{1}{h^2}(2ah^2) = 2a$, again the exact second derivative.

---

---

**Also asked here.**

- *2021 Q.7(c)* is the same question as [[NM-7.2|NM-7.2]], which is written in `NM-7.2`.

---
