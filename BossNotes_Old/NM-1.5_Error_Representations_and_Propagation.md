[← Previous: NM-1.4 Error Types](NM-1.4_Error_Types_and_Sources.md) | [🏠 Index](00_Index.md) | [Next: NM-1.6 Taylor Series →](NM-1.6_Taylor_Series_and_Truncation_Error.md)

---

# NM-1.5: Error Representations and Propagation
> **Section:** A (Numerical Methods) | **Priority:** 🔴 | **Exam Frequency:** 4/8 years
> **Sources:** Jain Ch.1 §1.3–1.4, Fahad Notes §01, Shishir Notes §01

## Why This Topic Matters

Error representation questions appear in 4 out of 8 years. They test two things: computing absolute/relative/percentage errors from given data, and propagating errors through composite functions using logarithmic differentiation. Both are numerical exercises worth 3-6 marks.

---

## 📝 Key Definitions

> **Absolute error:** "Absolute error is the numerical difference between the true value of a quantity and its approximate value... $E_A = X - X_1 = \delta X$." — Jain, §1.3 (p. 8, Eq. 1.2)

> **Relative error:** "$E_R = \frac{E_A}{X} = \frac{\delta X}{X}$." — Jain, §1.3 (p. 8, Eq. 1.3)

> **Percentage error:** "$E_P = 100 \, E_R$." — Jain, §1.3 (p. 8, Eq. 1.4)

> **Absolute accuracy:** "If $\Delta X$ is a number such that $|X_1 - X| \le \Delta X$, then $\Delta X$ is an upper limit on the magnitude of the absolute error and is said to measure absolute accuracy." — Jain, §1.3 (p. 8)

> **Relative accuracy:** "$\frac{A}{T}$, equivalently $1 - \left|\frac{e}{T}\right|$, which measures how near $A$ is to $T$."

> **Limiting error (error bound):** A stated bound $|e| \le \varepsilon$ within which the value is guaranteed to lie.

---

## The Five Error Representations

Given a true value $T$ and an approximate value $A$, with $e = A - T$:

| # | Representation | Formula | What it tells you |
| :--: | :-- | :-- | :-- |
| 1 | Absolute error | $e = A - T$, $|e| = |A - T|$ | Size of mistake, in units |
| 2 | Relative error | $\frac{e}{T}$ | Fraction of true value |
| 3 | Percentage error | $100 \frac{e}{T}$ | Same as above, in percent |
| 4 | Accuracy | $\frac{A}{T}$ or $1 - \left|\frac{e}{T}\right|$ | How near $A$ is to $T$ |
| 5 | Limiting error | $|e| \le \varepsilon$ | Guaranteed bound |

> [!WARNING] The denominator trap
> The denominator is the **true** value, not the approximate one. Writing $\frac{A - T}{A}$ is wrong. It gives a number that changes as the iteration improves, which is not a fixed measure. Only the true value belongs in the denominator.

### Why Relative Error Is Usually Better

1. **Scale-free.** A $0.95$ Amp error is trivial on a $10$ kA line and fatal on a $10$ mA sensor. Relative error says $9.5\%$ in both cases.
2. **Survives unit changes.** Measure the same current in milliamps and the absolute error becomes $950$ mA, which looks ten times worse. The relative error stays $0.095$.
3. **What stopping criteria use.** A solver halts when the relative step falls below a tolerance.

**When absolute error wins:** when the quantity is itself an error, a tolerance, or a dimensional quantity where a fraction makes no physical sense.

---

## Error Propagation by Logarithmic Differentiation

For a function of the form $u = C \cdot x^a \cdot y^b \cdot z^c$, the relative error is found by:

1. Take logarithms: $\ln u = \ln C + a \ln x + b \ln y + c \ln z$
2. Differentiate: $\frac{du}{u} = a\frac{dx}{x} + b\frac{dy}{y} + c\frac{dz}{z}$
3. Worst-case bound: $\left|\frac{du}{u}\right| \le |a|\left|\frac{dx}{x}\right| + |b|\left|\frac{dy}{y}\right| + |c|\left|\frac{dz}{z}\right|$

The constant $C$ contributes nothing (being exact). The sensitivity of a product is proportional to each factor's **power**, not just its presence.

If errors are independent, they add in quadrature:

$$
\left|\frac{du}{u}\right|_{\text{rms}} = \sqrt{a^2\left(\frac{dx}{x}\right)^2 + b^2\left(\frac{dy}{y}\right)^2 + c^2\left(\frac{dz}{z}\right)^2}
$$

---

## Worked Example (PYQ 2017, 2023)

**Problem.** Given $u = \frac{5xy^2}{z^3}$, find the relative error at $x = y = z = 1$ when the errors in each of $x, y, z$ is $0.001$.

> **Source:** 2017 Q.3(b), 2023 Q.1(b) [Marks: 03]

**Step 1.** Write $u = 5xy^2z^{-3}$ and take logarithms:

$$
\ln u = \ln 5 + \ln x + 2\ln y - 3\ln z
$$

**Step 2.** Differentiate:

$$
\frac{du}{u} = \frac{dx}{x} + 2\frac{dy}{y} - 3\frac{dz}{z}
$$

**Step 3.** Evaluate at $x = y = z = 1$. At that point:

$$
\frac{du}{u} = dx + 2\,dy - 3\,dz
$$

**Step 4.** Worst case with $dx = dy = dz = 0.001$:

$$
\left|\frac{du}{u}\right|_{\text{worst}} = 0.001 + 2(0.001) + 3(0.001) = 6(0.001) = 0.006
$$

$$
\boxed{\left|\frac{du}{u}\right| \le 6\times10^{-3} = 0.6\%}
$$

**If independent:** $\left|\frac{du}{u}\right|_{\text{rms}} = 0.001\sqrt{1 + 4 + 9} = 0.001\sqrt{14} = 3.742\times10^{-3}$, giving $0.374\%$.

---

## 🏆 Golden Questions (Past Exam Archive)

### 🎯 What are the error representations? Two PT-voltmeter arrangements give 999V and 9999V instead of 1kV and 10kV. Obtain error by all possible representations. Comment on error strength.
> **Appeared:** 2019 Q.1(c) — (04 marks)

**Full Answer:**

**The representations.** Given true value $T$ and approximate value $A$, with $e = A - T$:

1. **Absolute error:** $e = A - T$, and its magnitude $|e|$.
2. **Relative error:** $\frac{e}{T}$, the error measured against the true value.
3. **Percentage error:** $100\frac{e}{T}$.
4. **Relative accuracy:** $\frac{A}{T}$, equivalently $1 - \left|\frac{e}{T}\right|$.
5. **Limiting error:** a stated bound $|e| \le \varepsilon$.

**Arrangement 1: $A = 999\ \text{V}$, $T = 1000\ \text{V}$.**

$$
e = 999 - 1000 = -1\ \text{V}, \qquad |e| = 1\ \text{V}
$$

$$
E_{\text{rel}} = \frac{-1}{1000} = -10^{-3} = -0.1\%
$$

$$
E_{\text{rel, reading}} = \frac{-1}{999} = -1.001 \times 10^{-3} = -0.1001\%
$$

$$
\text{Accuracy} = \frac{999}{1000} = 0.999 = 99.9\%
$$

**Arrangement 2: $A = 9999\ \text{V}$, $T = 10000\ \text{V}$.**

$$
e = 9999 - 10000 = -1\ \text{V}, \qquad |e| = 1\ \text{V}
$$

$$
E_{\text{rel}} = \frac{-1}{10000} = -10^{-4} = -0.01\%
$$

$$
E_{\text{rel, reading}} = \frac{-1}{9999} = -1.0001 \times 10^{-4} = -0.010001\%
$$

$$
\text{Accuracy} = \frac{9999}{10000} = 0.9999 = 99.99\%
$$

**Comment.** The absolute error is identical, $1\ \text{V}$, so it separates the two not at all. The $9999\ \text{V}$ reading has a relative error of $0.01\%$ against the $999\ \text{V}$ reading's $0.1\%$, a factor of ten. The $9999\ \text{V}$ reading is the stronger one.

$$
\boxed{|e| = 1\ \text{V}\ \text{for both, but}\ E_{\text{rel}} = 10^{-3}\ \text{against}\ 10^{-4}}
$$

> [!NOTE] Why this example exists
> Both readings miss by exactly 1 volt. As absolute errors they are identical. As relative errors, one is ten times better. A voltmeter's accuracy is always specified as a percentage of full scale, never in volts. That is forced by exactly this observation.

---

### 🎯 How are errors represented? Obtain values to approximate a current as 9.05 Amp instead of true value 10 Amp. Justify which representation is better.
> **Appeared:** 2020 Q.1(b) — (06 marks)

**Full Answer:**

**Definitions.** Let $v_t$ be the true value and $v_a$ the approximate value.

**Absolute error.** The size of the mistake, in the units of the quantity.

$$
E_a = v_a - v_t \qquad \text{or} \qquad |E_a| = |v_a - v_t|
$$

**Relative error.** The mistake as a fraction of the true value. Dimensionless.

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

| Representation | Value | Units |
| :-- | --: | :-- |
| Absolute error | $0.95$ | Amp |
| Relative error | $0.095$ | none |
| Percentage relative error | $9.5\%$ | none |

**Which is better.** **Relative error** is better, for three reasons:

1. **Scale-free.** A $0.95$ Amp error is trivial on a $10$ kA line and fatal on a $10$ mA sensor. Relative error says $9.5\%$ in both cases.
2. **Survives unit changes.** In milliamps the absolute error becomes $950$ mA, looking ten times worse. Relative error stays $0.095$.
3. **What stopping criteria use.** A solver halts when the relative step falls below a tolerance.

$$
\boxed{|E_a| = 0.95 \text{ Amp}, \qquad E_r = -0.095, \qquad \text{percentage} = -9.5\%}
$$

> [!WARNING] The trap is the denominator
> Writing $\frac{9.05 - 10}{9.05} = -0.10497$ is the classic error. That figure is the error relative to the **approximate** value, not the true value. Only the true value belongs in the denominator.

---

## Exam Variants

| Year | Question | Data Given | Key Answer |
| :--- | :--- | :--- | :--- |
| 2017 Q.3(b), 2023 Q.1(b) | Relative error of $u = 5xy^2/z^3$ | $x=y=z=1$, errors $= 0.001$ | Worked Example above |
| 2019 Q.1(c) | Error representations, voltmeter comparison | 999V vs 1kV, 9999V vs 10kV | Golden Question below |
| 2020 Q.1(b) | Error representations, current measurement | $v_a = 9.05$, $v_t = 10$ | Golden Question below |

---

## ⚡ Exam Tips & Common Mistakes

1. **Always divide by the TRUE value.** $E_r = (A - T)/T$, not $(A - T)/A$. This is the single most common mistake in error questions.
2. **The sign tells direction.** A negative relative error means the approximation is low. State this explicitly.
3. **For propagation, take logarithms first.** Logarithmic differentiation turns products into sums and powers into coefficients. The worst-case bound sums the absolute values of the coefficients.
4. **State which bound you are quoting.** Worst-case vs. independent (quadrature) give different numbers. Say which one and why.
5. **Constants contribute nothing.** The factor $5$ in $5xy^2/z^3$ is exact and drops out during differentiation.

## 🔗 Related Topics

- [NM-1.4: Error Types and Sources](NM-1.4_Error_Types_and_Sources.md) — classification of truncation vs. round-off vs. inherent
- [NM-1.6: Taylor Series and Truncation Error](NM-1.6_Taylor_Series_and_Truncation_Error.md) — truncation error computed explicitly
- [NM-1.1: Foundations](NM-1.1_Foundations_of_Numerical_Methods.md) — why errors matter in the first place

---

[← Previous: NM-1.4 Error Types](NM-1.4_Error_Types_and_Sources.md) | [🏠 Index](00_Index.md) | [Next: NM-1.6 Taylor Series →](NM-1.6_Taylor_Series_and_Truncation_Error.md)
