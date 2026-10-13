[← Previous: NM-1.4 Error Types](NM-1.4_Error_Types.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: NM-1.6 Taylor Series →](NM-1.6_Taylor_Series.md)

---

# NM-1.5: Error Representations and Propagation

> 🔴 **Priority:** Critical | **Tested:** 4/8 years | **Typical marks:** 3–6

## What This Is (and Why It Matters)

Suppose you are measuring a voltage, and your meter is off by $1\text{ Volt}$. Is that bad? 

If you are measuring a $3.3\text{ V}$ microcontroller pin, a $1\text{ V}$ error is fatal. If you are measuring a $100\text{ kV}$ power transmission line, a $1\text{ V}$ error is negligible. 

That is why absolute error alone is rarely enough. In this subtopic, you will learn the 5 formal ways engineers express error (especially **relative** and **percentage** error) and how to justify which one is better. 

Even more importantly, you will learn **error propagation**: when you plug numbers with small measurement errors into a formula like $u = \frac{5xy^2}{z^3}$, how much error comes out in the final result? This is a guaranteed 3 to 6-mark problem on RUET exams.

---

## 📝 Key Definitions

> **Absolute error:** "Absolute error is the numerical difference between the true value of a quantity and its approximate value... $E_A = X - X_1 = \delta X$." -- Jain, §1.3 (p. 8, Eq. 1.2)
> 
> **In simple words:** True value minus approximate value. It carries physical units (like Amps or Volts) and tells you the raw size of the mistake.

> **Relative error:** "$E_R = \frac{E_A}{X} = \frac{\delta X}{X}$." -- Jain, §1.3 (p. 8, Eq. 1.3)
> 
> **In simple words:** The absolute error divided by the true value. It tells you what fraction of the whole measurement was wrong.

> **Percentage error:** "$E_P = 100 \, E_R$." -- Jain, §1.3 (p. 8, Eq. 1.4)
> 
> **In simple words:** The relative error converted to a percentage by multiplying by 100.

> **Absolute accuracy:** "If $\Delta X$ is a number such that $|X_1 - X| \le \Delta X$, then $\Delta X$ is an upper limit on the magnitude of the absolute error and is said to measure absolute accuracy." -- Jain, §1.3 (p. 8)
> 
> **In simple words:** The guaranteed maximum error tolerance stamped on an instrument by the manufacturer.

> **Relative accuracy:** The ratio of the approximate value to the true value, $\frac{A}{T}$, or $1 - \left|\frac{e}{T}\right|$.
> 
> **In simple words:** A score between 0 and 1 (or 0% and 100%) telling you how close your estimate was to the bullseye.

---

## The Core Idea

### The 5 Ways to Represent Error

Given a **true value** $T$ and an **approximate value** $A$, where error $e = A - T$:

| # | Representation | Mathematical Formula | What It Tells You | Units |
| :--: | :-- | :-- | :-- | :-- |
| 1 | **Absolute error** | $e = A - T$, or magnitude $\lvert e\rvert = \lvert A - T\rvert$ | Raw size of mistake | Same as quantity (V, A, m) |
| 2 | **Relative error** | $E_r = \frac{A - T}{T} = \frac{e}{T}$ | Mistake as fraction of true value | Dimensionless |
| 3 | **Percentage error** | $E_p = \frac{e}{T} \times 100\%$ | Fraction scaled to percent | % |
| 4 | **Relative accuracy** | $\text{Acc} = \frac{A}{T} = 1 - \left\vert\frac{e}{T}\right\vert$ | Closeness score to 100% | Dimensionless or % |
| 5 | **Limiting error** | $\lvert e\rvert \le \varepsilon$ | Guaranteed boundary | Same as quantity |

> [!WARNING] The Denominator Trap
> The most frequent student mistake in the entire exam is writing $\frac{A - T}{A}$ (dividing by the approximate reading). That is wrong! The true value $T$ is the fixed physical reality. The denominator must **always** be the true value $T$.

### Why Relative Error Is Usually Superior

When asked to *"Justify which representation is better"*, give these three clear reasons:

1. **Scale-free comparison:** A $0.95\text{ A}$ error is negligible on a $10\text{ kA}$ industrial substation busbar, but destructive on a $10\text{ mA}$ sensor circuit. Relative error gives an objective metric regardless of operating level.
2. **Independent of units:** If you convert a current from Amperes to milliamperes, the absolute error multiplies by 1,000 (from $0.95\text{ A}$ to $950\text{ mA}$), making it look a thousand times worse. The relative error stays identical at $0.095$.
3. **Standard stopping criterion:** Numerical software algorithms (like SPICE or MATLAB) stop iterating when the relative change between successive approximations falls below a preset tolerance $\epsilon$.

**When does absolute error win?** When specifying machining tolerances (e.g., $\pm 0.01\text{ mm}$ on a bolt) or when the true value is zero (where dividing by zero would cause an error).

---

## Error Propagation by Logarithmic Differentiation

When multiple variables $x, y, z$ each have small uncertainties, how much error propagates into a computed result $u = f(x, y, z)$?

For products and powers of the form:
$$
u = C \cdot x^a \cdot y^b \cdot z^c
$$
do **not** take tedious partial derivatives directly! Use the logarithmic differentiation trick:

### The 3-Step Recipe:
1. **Take the natural logarithm of both sides:**
$$
\ln u = \ln C + a \ln x + b \ln y + c \ln z
$$
*(Note: the constant $C$ is exact, so its derivative is zero!)*

2. **Differentiate both sides:**
$$
\frac{du}{u} = a \frac{dx}{x} + b \frac{dy}{y} + c \frac{dz}{z}
$$
Notice how every term is now directly a **relative error** ($\frac{dx}{x}$, $\frac{dy}{y}$, $\frac{dz}{z}$). The exponent becomes the sensitivity multiplier!

3. **Take the worst-case upper bound:**
Errors can have positive or negative signs. In the worst-case scenario, the errors align to maximize the total deviation. We replace every coefficient with its absolute value:
$$
\left|\frac{du}{u}\right|_{\text{worst}} \le |a|\left|\frac{dx}{x}\right| + |b|\left|\frac{dy}{y}\right| + |c|\left|\frac{dz}{z}\right|
$$

*(If the errors are random and statistically independent, they add in quadrature:)*
$$
\left|\frac{du}{u}\right|_{\text{rms}} = \sqrt{a^2\left(\frac{dx}{x}\right)^2 + b^2\left(\frac{dy}{y}\right)^2 + c^2\left(\frac{dz}{z}\right)^2}
$$

---

## 🔧 Worked Example: Error Propagation in $u = \frac{5xy^2}{z^3}$

> **From:** 2017 Q.3(b) and 2023 Q.1(b) -- [Marks: 03]

**The question:** Given $u = \frac{5xy^2}{z^3}$, find the relative error at $x = y = z = 1$ when the errors in each of $x, y, z$ is $0.001$.

**Let's solve this step by step.**

**Step 1: Rewrite with explicit powers and take logarithms.**
We rewrite $u = 5 x^1 y^2 z^{-3}$. Taking natural logarithms:
$$
\ln u = \ln 5 + \ln x + 2\ln y - 3\ln z
$$

**Step 2: Differentiate to find relative errors.**
$$
\frac{du}{u} = \frac{dx}{x} + 2\frac{dy}{y} - 3\frac{dz}{z}
$$

**Step 3: Evaluate at the operating point.**
We are given $x = 1, y = 1, z = 1$:
$$
\frac{du}{u} = dx + 2\,dy - 3\,dz
$$

**Step 4: Apply the worst-case error bound.**
The individual uncertainties are bounded by $|dx| \le 0.001$, $|dy| \le 0.001$, and $|dz| \le 0.001$. In the worst case, the signs combine destructively:
$$
\begin{aligned}
\left|\frac{du}{u}\right| &\le |1|\,|dx| + |2|\,|dy| + |-3|\,|dz| \\
&= 1(0.001) + 2(0.001) + 3(0.001) \\
&= (1 + 2 + 3)(0.001) \\
&= 6 \times 0.001 = 0.006
\end{aligned}
$$

$$
\boxed{\left|\frac{du}{u}\right| \le 6\times10^{-3} = 0.6\%}
$$

**Quick sanity check:** The powers are 1, 2, and 3. The sum of powers is $1 + 2 + 3 = 6$. Since each input has an error of $0.001$, a total relative error of $6 \times 0.001 = 0.006$ is completely intuitive!

---

## 🏆 Past Exam Questions

### 2019 Q.1(c): Voltmeter arrangement error comparison [04 marks]

**The question:** What are the error representations? Two PT-voltmeter arrangements give $999\text{ V}$ and $9999\text{ V}$ instead of $1\text{ kV}$ and $10\text{ kV}$. Obtain the error by all possible representations. Comment on error strength.

**Solution:**

**The representations:**
Given true value $T$ and measured value $A$, with error $e = A - T$:
1. Absolute error: $e = A - T$, and magnitude $|e|$.
2. Relative error: $E_{\text{rel}} = \frac{e}{T}$.
3. Percentage error: $E_{\text{pct}} = 100 \times \frac{e}{T}$.
4. Relative accuracy: $\text{Acc} = \frac{A}{T} = 1 - |E_{\text{rel}}|$.

**Arrangement 1: Measured $A = 999\text{ V}$, True $T = 1000\text{ V}$ ($1\text{ kV}$):**
- Absolute error: $e_1 = 999 - 1000 = -1\text{ V}$, magnitude $|e_1| = 1\text{ V}$.
- Relative error: $E_{\text{rel}, 1} = \frac{-1}{1000} = -10^{-3} = -0.001$.
- Percentage error: $E_{\text{pct}, 1} = -0.1\%$.
- Relative accuracy: $\text{Acc}_1 = \frac{999}{1000} = 0.999 = 99.9\%$.

**Arrangement 2: Measured $A = 9999\text{ V}$, True $T = 10000\text{ V}$ ($10\text{ kV}$):**
- Absolute error: $e_2 = 9999 - 10000 = -1\text{ V}$, magnitude $|e_2| = 1\text{ V}$.
- Relative error: $E_{\text{rel}, 2} = \frac{-1}{10000} = -10^{-4} = -0.0001$.
- Percentage error: $E_{\text{pct}, 2} = -0.01\%$.
- Relative accuracy: $\text{Acc}_2 = \frac{9999}{10000} = 0.9999 = 99.99\%$.

**Comment on error strength:**
Both arrangements have the exact same absolute error of $1\text{ Volt}$. Looking only at absolute error, you might falsely conclude both instruments perform equally well. 

However, looking at relative error, Arrangement 2 has an error of only $0.01\%$, which is **ten times smaller** (ten times more accurate) than Arrangement 1's $0.1\%$. Arrangement 2 is significantly stronger and higher-grade.

$$
\boxed{|e| = 1\ \text{V}\ \text{for both, but}\ E_{\text{rel}} = 10^{-3}\ \text{against}\ 10^{-4}}
$$

---

### 2020 Q.1(b): Error Representations & Current Approximation [06 marks]

**The question:** How are errors represented? Write down their expressions. Obtain their values to approximate a current as $9.05\text{ Amp}$ instead of true value $10\text{ Amp}$. Justify which representation is better.

**Solution:**

**Definitions:**
Let $v_t = 10\text{ A}$ be the true current and $v_a = 9.05\text{ A}$ be the approximate current.

**1. Absolute error ($E_a$):**
$$
E_a = v_a - v_t = 9.05 - 10 = -0.95\text{ Amp}
$$
Magnitude of absolute error:
$$
|E_a| = 0.95\text{ Amp}
$$

**2. Relative error ($E_r$):**
$$
E_r = \frac{v_a - v_t}{v_t} = \frac{-0.95}{10} = -0.095
$$

**3. Percentage relative error:**
$$
\text{Percentage error} = E_r \times 100\% = -0.095 \times 100\% = -9.5\%
$$

**Summary Table:**

| Representation | Computed Value | Units |
| :-- | --: | :-- |
| Absolute error ($E_a$) | $-0.95$ (magnitude $0.95$) | Amp |
| Relative error ($E_r$) | $-0.095$ | None (dimensionless) |
| Percentage relative error | $-9.5\%$ | None |
| Relative accuracy | $90.5\%$ | None |

**Justification: Why Relative Error Is Better:**
**Relative error is significantly better** for three technical reasons:
1. **Context and scale independence:** An absolute error of $0.95\text{ A}$ is enormous if you are measuring a $10\text{ A}$ line (nearly $10\%$ off), but trivial if you are measuring a $10\text{ kA}$ power line. Relative error provides the true physical significance regardless of scale.
2. **Robustness to unit conversions:** In milliamps, the absolute error is $950\text{ mA}$, which artificially looks a thousand times worse. Relative error remains constant at $-0.095$.
3. **Algorithmic convergence:** Numerical termination criteria evaluate relative tolerance $|\Delta x / x| < \epsilon$ to avoid machine scale bias.

$$
\boxed{|E_a| = 0.95 \text{ Amp}, \qquad E_r = -0.095, \qquad \text{percentage} = -9.5\%}
$$

---

### Exam Variants at a Glance

| Year | What They Asked | Key Boxed Takeaway |
| :--- | :--- | :--- |
| **2017 Q.3(b)** | Relative error of $u = 5xy^2/z^3$ | $\boxed{\left\vert\frac{du}{u}\right\vert \le 6\times10^{-3} = 0.6\%}$ |
| **2019 Q.1(c)** | Voltmeter comparison: 999V vs 9999V | $\boxed{\lvert e\rvert = 1\ \text{V}\ \text{for both, but}\ E_{\text{rel}} = 10^{-3}\ \text{against}\ 10^{-4}}$ |
| **2020 Q.1(b)** | Current measurement: 9.05A vs 10A (6 marks) | $\boxed{\lvert E_a\rvert = 0.95 \text{ Amp}, \qquad E_r = -0.095, \qquad \text{percentage} = -9.5\%}$ |
| **2023 Q.1(b)** | Relative error of $u = 5xy^2/z^3$ (repeat) | Same logarithmic differentiation recipe: $0.6\%$ |

---

## ⚡ Quick Review

**The method in one sentence:** Always divide by the true value to find relative error, and use logarithmic differentiation to propagate errors through product/quotient formulas by turning powers into coefficients.

**The formula you must memorize:**
$$
\text{For } u = C x^a y^b z^c \implies \left|\frac{du}{u}\right|_{\max} \le |a|\left|\frac{\Delta x}{x}\right| + |b|\left|\frac{\Delta y}{y}\right| + |c|\left|\frac{\Delta z}{z}\right|
$$

**The most common exam mistake:** Dividing by the approximate reading instead of the true value in the denominator of relative error: $\frac{A-T}{A}$ instead of $\frac{A-T}{T}$.

**Time estimate in exam:** 5–8 minutes for a 3–6 mark question.

---

## 🔗 Connected Topics

- [← NM-1.4: Error Types](NM-1.4_Error_Types.md) -- the physical and algorithmic sources that produce these errors
- [→ NM-1.6: Taylor Series](NM-1.6_Taylor_Series.md) -- evaluating truncation errors and determining required terms
- [→ NM-3: Linear Systems Overview](../NM-3_Linear_Systems/_Topic_Overview.md) -- where tiny relative errors in matrix inputs explode into massive output errors

---

[← Previous: NM-1.4 Error Types](NM-1.4_Error_Types.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: NM-1.6 Taylor Series →](NM-1.6_Taylor_Series.md)
