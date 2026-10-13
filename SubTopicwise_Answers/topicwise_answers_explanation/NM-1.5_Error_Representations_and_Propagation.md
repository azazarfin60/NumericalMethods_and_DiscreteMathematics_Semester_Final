---
title: "NM-1.5 · Error Representations & Propagation"
tags:
  - numerical-methods
  - discrete-mathematics
  - topicwise
---



[🏠 Subtopic Index](00_Index.md) | [← Prev: NM-1.4 Error Types & Sources](NM-1.4_Error_Types_and_Sources.md) | [Next: NM-1.6 Taylor Series & Truncation Error →](NM-1.6_Taylor_Series_and_Truncation_Error.md)

---

# NM-1.5 · Error Representations & Propagation

Every block below is copied from `../answers_explanation/`. The reasoning
is written once, in the year-wise file, and is not restated here.


### [2017 Q.3(b), 2023 Q.1(b)]

**Appeared in:** 2017 Q.3(b), 2023 Q.1(b)

**Question.** Given that $u = \frac{5xy^2}{z^3}$. Find the relative error at $x = y = z = 1$ when the errors in each of $x, y, z$ is $0.001$.

*[Marks: 03]*

**Solution.**

**The method.** Logarithmic differentiation. With $u = 5xy^2z^{-3}$, take natural
logarithms,

$$\ln u = \ln 5 + \ln x + 2\ln y - 3\ln z$$

and differentiate:

$$\frac{du}{u} = \frac{dx}{x} + 2\frac{dy}{y} - 3\frac{dz}{z}$$

**Why this method.** The relative error is what is asked for, and the
logarithmic derivative *is* the relative error in differential form. Taking
logarithms first is what linearises the products and powers into a sum, and a
sum of relative errors is what the question can be answered from.

**Evaluate at $x = y = z = 1$.** At that point each ratio is its own variable,
so

$$\frac{du}{u} = dx + 2\,dy - 3\,dz$$

**The worst case.** The three errors are not stated to be independent, so the
safe reading is that all three act in the direction that maximises the
magnitude. The coefficients $1, 2, -3$ have absolute values $1, 2, 3$, so

$$\left|\frac{du}{u}\right|_{\text{worst}} = 0.001 + 2(0.001) + 3(0.001) = 6(0.001) = 0.006$$

$$\boxed{\left|\frac{du}{u}\right| \le 6\times10^{-3} = 0.6\%}$$

**Note what the exponent $2$ on $y$ and the exponent $-3$ on $z$ did.** $y$
appears twice, so an error in $y$ is counted twice. $z$ appears three times, so
an error in $z$ is counted three times. The sensitivity of a product is
proportional to each factor's *power*, not to its presence, and a factor raised
to a high power is a correspondingly larger lever on the answer. The constant
$5$ contributes nothing, being exact.

> [!info] If the errors are independent, the answer is different
> The bound above is the worst case over all sign combinations. If instead the
> three errors are independent random quantities with equal standard deviation,
> they add in quadrature and
> $$\left|\frac{du}{u}\right|_{\text{rms}} = 0.001\sqrt{1^2 + 2^2 + 3^2} = 0.001\sqrt{14} = 3.742\times10^{-3},$$
> that is $0.374\%$, and the relative error is $0.374\%$.
>
> The two differ by a factor of $1.6$, and which is right depends on a
> statement about the errors that the question does not make. The worst-case
> reading is the one to report when nothing is stated, because it holds
> regardless of the sign pattern. Worth knowing both, and worth saying which
> one you are quoting.

---

### [2019 Q.1(c)]

**Question.** What are the error representations? Two PT-voltmeter arrangements give $999\text{V}$ and $9999\text{V}$ instead of $1\text{kV}$ and $10\text{kV}$. Obtain error by all possible error representations. Hence comment on error strength of the readings.

*[Marks: 04]*

**Solution.**

**The representations.** Given a true value $T$ and an approximate value $A$,
with $e = A - T$:

1. **Absolute error:** $e = A - T$, and its magnitude $|e|$.
2. **Relative error:** $\dfrac{e}{T}$, the error measured against the true value.
3. **Percentage error:** $100\dfrac{e}{T}$.
4. **Relative (or percentage) accuracy:** $\dfrac{A}{T}$, equivalently
   $1 - \left|\dfrac{e}{T}\right|$, which measures how near $A$ is to $T$.
5. **Limiting error (error bound):** a stated bound $|e| \le \varepsilon$ within
   which the value is guaranteed to lie.

**Arrangement 1: $A = 999\ \text{V}$, $T = 1000\ \text{V}$.**

$$e = 999 - 1000 = -1\ \text{V}, \qquad |e| = 1\ \text{V}$$

$$E_{\text{rel}} = \frac{-1}{1000} = -10^{-3} = -0.1\%$$

$$E_{\text{rel, reading}} = \frac{-1}{999} = -1.001 \times 10^{-3} = -0.1001\%$$

$$\text{Accuracy} = \frac{999}{1000} = 0.999 = 99.9\%$$

**Arrangement 2: $A = 9999\ \text{V}$, $T = 10000\ \text{V}$.**

$$e = 9999 - 10000 = -1\ \text{V}, \qquad |e| = 1\ \text{V}$$

$$E_{\text{rel}} = \frac{-1}{10000} = -10^{-4} = -0.01\%$$

$$E_{\text{rel, reading}} = \frac{-1}{9999} = -1.0001 \times 10^{-4} = -0.010001\%$$

$$\text{Accuracy} = \frac{9999}{10000} = 0.9999 = 99.99\%$$

**Comment on the error strength.** The absolute error is identical in the two
arrangements, $1\ \text{V}$, so the absolute error separates them not at all.
Against the true value, the $9999\ \text{V}$ reading has a relative error of
$0.01\%$ while the $999\ \text{V}$ reading has $0.1\%$, a factor of ten difference.
The $9999\ \text{V}$ reading is therefore the stronger one.

$$\boxed{|e| = 1\ \text{V}\ \text{for both, but}\ E_{\text{rel}} = 10^{-3}\ \text{against}\ 10^{-4}}$$

> [!warning] This is the clearest demonstration of why relative error exists
> Both readings miss by exactly $1$ volt. Read as absolute errors they are
> **identical**, and a specification written as "accurate to $1$ volt" cannot
> distinguish them.
>
> Read as relative errors, one is ten times better than the other, and the
> specification "accurate to $0.01\%$" selects exactly one of the two
> instruments.
>
> **A voltmeter's accuracy is always specified as a percentage of full scale, never
> in volts.** That is not a convention; it is forced by exactly this observation.
> An instrument accurate to $1$ volt is useless on a $1$ kilovolt range and
> excellent on a $100$ kilovolt one.

> [!info] Check against the exact ratios
> The ratio of the two relative errors equals the inverse ratio of the true
> values: $\dfrac{10^{-3}}{10^{-4}} = 10 = \dfrac{10000}{1000}$. A common absolute
> error on magnitudes differing by a factor of ten produces relative errors
> differing by the same factor, which is the point the comment rests on.

---

### [2020 Q.1(b)]

**Question.** How are errors represented? Write down their expressions. Obtain their values to approximate a current as $9.05$ Amp instead of its true value $10$ Amp. Justify, which representation is better.

*[Marks: 06]*

**Solution.**

**Definitions.** Let $v_t$ be the true value and $v_a$ the approximate value.

**Absolute error.** The size of the mistake, in the units of the quantity.

$$
E_a = v_a - v_t \qquad \text{or} \qquad |E_a| = |v_a - v_t|
$$

It is the only error directly measurable, and it carries the same units as the
answer.

**Relative error.** The mistake as a fraction of the true value. It is
dimensionless, so it can be compared across quantities of different size.

$$
E_r = \frac{v_a - v_t}{v_t} \qquad \text{percentage relative error} = \frac{v_a - v_t}{v_t} \times 100
$$

**Now the numbers.** $v_a = 9.05$ Amp, $v_t = 10$ Amp.

$$
E_a = 9.05 - 10 = -0.95 \text{ Amp}, \qquad |E_a| = 0.95 \text{ Amp}
$$

$$
E_r = \frac{9.05 - 10}{10} = \frac{-0.95}{10} = -0.095
$$

$$
\text{percentage relative error} = -0.095 \times 100 = -9.5\%
$$

The sign says the approximation is **low**, which absolute error alone cannot
give a quantity that can be reasoned about directly.

| Representation | Value | Units |
| :-- | --: | :-- |
| Absolute error | $0.95$ | Amp |
| Relative error | $0.095$ | none |
| Percentage relative error | $9.5\%$ | none |

$$\boxed{|E_a| = 0.95 \text{ Amp}, \qquad E_r = -0.095, \qquad \text{percentage} = -9.5\%}$$

**Which is better, and why.** **Relative error** is the better representation, for
three reasons.

1. **It is scale-free.** A $0.95$ Amp error is trivial on a $10$ kA line and
   fatal on a $10$ mA sensor. The relative error says $9.5\%$ in both cases, so it
   ranks the two directly.
2. **It survives unit changes.** Measure the same current in milliamps and the
   absolute error becomes $950$ mA, which looks ten times worse. The relative
   error is still $0.095$. The relative error is invariant.
3. **It is what stopping criteria use.** A solver halts when the *relative* step
   falls below a tolerance, so that the test means the same thing at any
   magnitude.

Where absolute error wins: when the quantity is itself an error, a tolerance, or
a dimensional quantity where a fraction makes no sense, such as a length or a
time. Reporting "the beam is off by $2$ mm" beats "off by $0.4\%$".

> [!warning] The trap is the denominator
> Writing $\frac{9.05 - 10}{9.05} = -0.10497$ is the classic error. It looks
> reasonable and it is wrong. That figure is the error relative to the
> **approximate** value, which is not a standard measure and which changes as the
> iteration improves. Only the true value belongs in the denominator, and here it
> is $10$, not $9.05$.
>
> The gap is small, $9.5\%$ against $10.5\%$, and easy to overlook. At $99.5$
> against $100$ the same slip gives $0.5\%$ instead of $0.50\%$, still small, and
> students who never check it never find out.
>
> **Fix the true value in memory: relative error is always taken over the true
> value.** The same distinction appears in 2024 Q.1(b) and 2023 Q.1(b).

---

---

**Also asked here.**

- *CT-02B Q.1(c)* is the same question as [[NM-3.5_Gauss_Seidel_Iteration|NM-3.5]], which is written in `NM-3.5`.

---

[🏠 Subtopic Index](00_Index.md) | [← Prev: NM-1.4 Error Types & Sources](NM-1.4_Error_Types_and_Sources.md) | [Next: NM-1.6 Taylor Series & Truncation Error →](NM-1.6_Taylor_Series_and_Truncation_Error.md)
