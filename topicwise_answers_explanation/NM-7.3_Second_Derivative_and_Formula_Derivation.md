---
title: "NM-7.3 · Second Derivative & Formula Derivation"
tags:
  - numerical-methods
  - discrete-mathematics
  - topicwise
---

# NM-7.3 · Second Derivative & Formula Derivation

Every block below is copied from `../answers_explanation/`. The reasoning
is written once, in the year-wise file, and is not restated here.


### [2017 Q.6(c)]

**Question.** Derive a formula to find the second derivative of a tabulated function.

*[Marks: 04]*

**Solution.**

**Set-up.** Let $y = f(x)$ be tabulated at equally spaced nodes with interval
$h$, and write $p = \dfrac{x - x_0}{h}$. Newton's forward interpolation formula
is

$$y = y_0 + p\Delta y_0 + \frac{p(p-1)}{2!}\Delta^2 y_0 + \frac{p(p-1)(p-2)}{3!}\Delta^3 y_0 + \frac{p(p-1)(p-2)(p-3)}{4!}\Delta^4 y_0 + \cdots$$

**First derivative.** Since $dx = h\,dp$, differentiation with respect to $x$
is $(1/h)$ times differentiation with respect to $p$:

$$\frac{dy}{dx} = \frac{1}{h}\left[\Delta y_0 + \frac{2p-1}{2!}\Delta^2 y_0 + \frac{3p^2 - 6p + 2}{3!}\Delta^3 y_0 + \frac{4p^3 - 18p^2 + 22p - 6}{4!}\Delta^4 y_0 + \cdots\right]$$

The coefficient of $\Delta^k y_0$ is the derivative of the product
$p(p-1)\cdots(p-k+1)$, divided by $k!$. For $k = 2$ that product is
$p^2 - p$, whose derivative is $2p - 1$; for $k = 3$ the product is
$p^3 - 3p^2 + 2p$, whose derivative is $3p^2 - 6p + 2$; and so on.

**Second derivative.** Differentiating a second time:

$$\boxed{\frac{d^2y}{dx^2} = \frac{1}{h^2}\left[\Delta^2 y_0 + (p-1)\Delta^3 y_0 + \left(\frac{p^2}{2} - \frac{3p}{2} + \frac{11}{12}\right)\Delta^4 y_0 + \cdots\right]}$$

Each coefficient is the second derivative of the corresponding product,
divided by $k!$:

$$\frac{d^2}{dp^2}\left(p^2 - p\right) = 2, \qquad \frac{d^2}{dp^2}\left(p^3 - 3p^2 + 2p\right) = 6p - 6, \qquad \frac{d^2}{dp^2}\left(p^4 - 6p^3 + 11p^2 - 6p\right) = 12p^2 - 36p + 22$$

and dividing by $2!$, $3!$ and $4!$ gives $1$, $(p-1)$ and
$\left(\dfrac{p^2}{2} - \dfrac{3p}{2} + \dfrac{11}{12}\right)$.

**Stopping rule.** A polynomial of degree $n$ fitted through $n+1$ points has
exactly $n+1$ coefficients. The differences of order greater than $n$ vanish
identically, so the series above terminates after the term in $\Delta^n y_0$.
Since $y''$ requires differences of order two and above, **at least three
points** are needed for the formula to carry any information, and a cubic fit
through four points carries terms up to $\Delta^3 y_0$.

**The backward counterpart.** Writing backward differences at the last node
$x_n$ and putting $q = \dfrac{x - x_n}{h}$,

$$\frac{d^2y}{dx^2} = \frac{1}{h^2}\left[\nabla^2 y_n + (q+1)\nabla^3 y_n + \left(\frac{q^2}{2} + \frac{3q}{2} + \frac{11}{12}\right)\nabla^4 y_n + \cdots\right]$$

which is the form used when the tabulation runs in the decreasing direction.

> [!info] A test that shows the formula is exact, not a rule of thumb
> Take $y = ax^3$ tabulated from $x_0 = 0$ at spacing $h$, so $x = ph$. Then
> $\Delta^2 y_0 = y(2h) - 2y(h) + y(0) = 8ah^3 - 2ah^3 = 6ah^3$ and
> $\Delta^3 y_0 = 6ah^3$, with all higher differences zero. The formula gives
> $$\frac{1}{h^2}\left[6ah^3 + (p - 1)6ah^3\right] = 6ah\left[1 + p - 1\right] = 6aph.$$
> The true second derivative is $y'' = 6ax = 6a(ph) = 6aph$. The two agree for
> *every* $p$, not only at the nodes, and that is the property that makes the
> formula usable for interpolation rather than only for differencing at the
> tabulated points. For a quadratic $y = ax^2 + bx + c$ only
> $\Delta^2 y_n = 2ah^2$ survives, so the formula reduces to
> $\dfrac{1}{h^2}(2ah^2) = 2a$, again exact.
>
> The reason it is exact is worth stating plainly: the differences
> $\Delta^{n+1} y_0, \Delta^{n+2} y_0, \dots$ of a degree-$n$ polynomial are all
> zero, so the truncated series is not an approximation at all but the
> polynomial's own derivative.

---

### [2018 Q.5(a)]

**Question.** State Newton's forward formula to evaluate $\frac{d^2 y}{dx^2}$ for any value $x \in [x_0, x_n]$.

*[Marks: 06]*

**Solution.**

**Start from the interpolation polynomial.** For a table of common spacing $h$,
Newton's forward formula is

$$y = y_0 + p\Delta y_0 + \frac{p(p-1)}{2!}\Delta^2 y_0 + \frac{p(p-1)(p-2)}{3!}\Delta^3 y_0 + \frac{p(p-1)(p-2)(p-3)}{4!}\Delta^4 y_0 + \cdots$$

with

$$p = \frac{x - x_0}{h}$$

**The chain rule is the whole method.** Since $x$ enters only through $p$,

$$\frac{d}{dx} = \frac{1}{h}\frac{d}{dp}, \qquad \frac{d^2y}{dx^2} = \frac{1}{h^2}\frac{d^2y}{dp^2}$$

So you differentiate the falling-factorial products with respect to $p$, not
with respect to $x$. That is why every coefficient in the answer is a
polynomial in $p$.

**First derivative.**

$$\frac{dy}{dx} = \frac{1}{h}\left[\Delta y_0 + \frac{2p - 1}{2!}\Delta^2 y_0 + \frac{3p^2 - 6p + 2}{3!}\Delta^3 y_0 + \frac{4p^3 - 18p^2 + 22p - 6}{4!}\Delta^4 y_0 + \cdots\right]$$

**Second derivative, differentiating once more.**

$$\frac{d^2y}{dx^2} = \frac{1}{h^2}\left[\Delta^2 y_0 + \frac{6p - 6}{3!}\Delta^3 y_0 + \frac{12p^2 - 36p + 22}{4!}\Delta^4 y_0 + \cdots\right]$$

**Simplifying the coefficients.**

$$\boxed{\frac{d^2y}{dx^2} = \frac{1}{h^2}\left[\Delta^2 y_0 + (p - 1)\Delta^3 y_0 + \left(\frac{p^2}{2} - \frac{3p}{2} + \frac{11}{12}\right)\Delta^4 y_0 + \cdots\right]}$$

**How many points are needed.** A polynomial of degree $n$ through $n+1$ points
has exactly $n+1$ coefficients, so for $n = 1$ only the $\Delta y_0$ term
exists, for $n = 2$ the terms up to $\Delta^2 y_0$, and so on. Since $y''$
needs differences of order two and above, the formula needs at least **three
points** for a quadratic fit, four for a cubic. The next term, omitted above,
carries the coefficient

$$\frac{p^3}{6} - p^2 + \frac{7p}{4} - \frac{5}{6}$$

on $\Delta^5 y_0$.

> [!info] The test that shows the formula is not merely a rule of thumb
> The formula reproduces $\dfrac{d^2y}{dx^2}$ *exactly* for any polynomial of
> degree four or lower, because every term from $\Delta^5 y_0$ onward then
> vanishes. A cubic is the first case where this can be checked without
> appealing to the derivation.
>
> Take $y = ax^3$ tabulated from $x_0 = 0$ at spacing $h$, so $x = ph$. Then
> $\Delta^2 y_0 = y(2h) - 2y(h) + y(0) = 8ah^3 - 2ah^3 = 6ah^3$ and
> $\Delta^3 y_0 = 6ah^3$, with all higher differences zero. The formula gives
> $\dfrac{1}{h^2}\left[6ah^3 + (p - 1)6ah^3\right] = 6ah\left[1 + p - 1\right] = 6aph$.
> The true second derivative is $y'' = 6ax = 6a(ph) = 6aph$. The two agree for
> *every* $p$, not only at the nodes, and that is the property that makes the
> formula useful for interpolation rather than only for differencing at the
> tabulated points.
>
> For a quadratic $y = ax^2 + bx + c$ only $\Delta^2 y_n = 2ah^2$ survives, so
> the formula reduces to $\dfrac{1}{h^2}(2ah^2) = 2a$, again exact.

---

---

**Also asked here.**

- *2021 Q.7(c)* is the same question as [[NM-7.2|NM-7.2]], which is written in `NM-7.2`.

---
