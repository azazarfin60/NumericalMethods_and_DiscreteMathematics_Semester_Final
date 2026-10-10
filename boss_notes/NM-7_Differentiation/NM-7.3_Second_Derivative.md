[← Previous: NM-7.2 First Derivative](NM-7.2_First_Derivative.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: NM-7.4 Applied Differentiation →](NM-7.4_Applied_Differentiation.md)

---

# NM-7.3: Second Derivative & Formula Derivation

> 🟠 ⚠️ **Priority:** Secondary (High Derivation Danger) | **Tested:** 3 appearances (2017, 2018, 2021) | **Typical marks:** 4–6

## What This Is (and Why It Matters)

In numerical methods, examiners distinguish between students who merely push buttons on a calculator and students who understand where the formulas come from. That is why the second-derivative derivation question is a perennial favorite in RUET semester finals.

Both in 2017 Q.6(c) (4 marks) and in 2018 Q.5(a) (6 marks), students were asked to derive Newton's forward difference formula for the second derivative $\frac{d^2y}{dx^2}$ of a tabulated function.

If you only memorize the final boxed formula, you will struggle to score full marks on a derivation question. But if you understand the four simple derivation steps (writing the Newton forward polynomial in $p$, applying the chain rule twice, differentiating the falling factorials, and dividing by factorials), the entire derivation unfolds naturally in under five minutes.

---

## 📝 Key Definitions

> **Second numerical derivative:** "The rate of change of the slope of a tabulated function, representing physical quantities such as acceleration in dynamics, bending moments in beams, or curvature in geometric modeling."
>
> **In simple words:** It tells you how rapidly the slope itself is changing. If the first derivative is speed, the second derivative is acceleration.

> **Dimensionless interpolation variable $p$:** "The normalized distance parameter defined by $p = \frac{x - x_0}{h}$, measuring how many step lengths $h$ the evaluation point $x$ lies away from the base node $x_0$."
>
> **In simple words:** Instead of tracking messy physical units like meters or seconds, $p$ counts how many steps you have walked from the start of the table ($p = 0$ at the first node, $p = 1$ at the second node, $p = 0.5$ halfway between).

> **Chain rule scaling factor:** "Since $x$ enters the polynomial solely through $p = (x - x_0)/h$, differentiation with respect to $x$ introduces a factor of $1/h$ for each derivative: $\frac{d}{dx} = \frac{1}{h}\frac{d}{dp}$ and $\frac{d^2}{dx^2} = \frac{1}{h^2}\frac{d^2}{dp^2}$."
>
> **In simple words:** Every time you take a derivative with respect to $x$, the chain rule pops a factor of $1/h$ out in front. For the second derivative, you get $(1/h) \times (1/h) = 1/h^2$.

> **Falling factorial polynomials:** "Polynomial products of the form $p^{(k)} = p(p-1)(p-2)\cdots(p-k+1)$, whose successive derivatives generate the coefficients of the difference formula."
>
> **In simple words:** The product $(p)(p-1)(p-2)\dots$ is what gives each term in Newton's polynomial its shape. We differentiate these products directly to find our formula.

---

## The Core Derivation: Step by Step

Let us walk through the complete derivation exactly as you should write it in your exam script.

### Step 1: Set Up Newton's Forward Interpolation Formula

Let $y = f(x)$ be tabulated at equally spaced nodes $x_0, x_1, x_2, \dots$ with constant step size $h$.
Define the dimensionless coordinate:

$$
p = \frac{x - x_0}{h} \implies x = x_0 + ph
$$

Newton's forward difference interpolation formula is:

$$
y = y_0 + p\Delta y_0 + \frac{p(p-1)}{2!}\Delta^2 y_0 + \frac{p(p-1)(p-2)}{3!}\Delta^3 y_0 + \frac{p(p-1)(p-2)(p-3)}{4!}\Delta^4 y_0 + \cdots
$$

### Step 2: Establish the Chain Rule Operators

Notice that $x$ appears in the interpolation formula only inside the variable $p$.
Differentiating $p$ with respect to $x$:

$$
\frac{dp}{dx} = \frac{d}{dx}\left(\frac{x - x_0}{h}\right) = \frac{1}{h}
$$

By the chain rule of calculus:

$$
\frac{dy}{dx} = \frac{dy}{dp} \cdot \frac{dp}{dx} = \frac{1}{h}\frac{dy}{dp}
$$

Now differentiate a second time with respect to $x$:

$$
\frac{d^2y}{dx^2} = \frac{d}{dx}\left(\frac{dy}{dx}\right) = \frac{d}{dp}\left(\frac{1}{h}\frac{dy}{dp}\right) \cdot \frac{dp}{dx} = \frac{1}{h}\left(\frac{d^2y}{dp^2}\right)\left(\frac{1}{h}\right) = \frac{1}{h^2}\frac{d^2y}{dp^2}
$$

This is the key insight of the entire derivation: **to find derivatives with respect to $x$, we differentiate the falling-factorial polynomials with respect to $p$, and scale by $1/h$ or $1/h^2$!**

### Step 3: Differentiate the Numerator Products

Let us expand and differentiate the numerator of each term with respect to $p$:

#### 1. Term in $\Delta y_0$:
Numerator is $p$.
- First derivative: $\frac{d}{dp}(p) = 1$
- Second derivative: $\frac{d^2}{dp^2}(p) = 0$
*(The first difference term produces zero in the second derivative!)*

#### 2. Term in $\Delta^2 y_0$:
Numerator is $p(p-1) = p^2 - p$.
- First derivative: $\frac{d}{dp}(p^2 - p) = 2p - 1$
- Second derivative: $\frac{d^2}{dp^2}(p^2 - p) = 2$

Dividing by $2! = 2$:

$$
\frac{2}{2!} = \frac{2}{2} = 1
$$

#### 3. Term in $\Delta^3 y_0$:
Numerator is $p(p-1)(p-2) = p^3 - 3p^2 + 2p$.
- First derivative: $\frac{d}{dp}(p^3 - 3p^2 + 2p) = 3p^2 - 6p + 2$
- Second derivative: $\frac{d^2}{dp^2}(p^3 - 3p^2 + 2p) = 6p - 6 = 6(p - 1)$

Dividing by $3! = 6$:

$$
\frac{6(p - 1)}{3!} = \frac{6(p - 1)}{6} = p - 1
$$

#### 4. Term in $\Delta^4 y_0$:
Numerator is $p(p-1)(p-2)(p-3) = p^4 - 6p^3 + 11p^2 - 6p$.
- First derivative: $\frac{d}{dp}(P_4) = 4p^3 - 18p^2 + 22p - 6$
- Second derivative: $\frac{d^2}{dp^2}(P_4) = 12p^2 - 36p + 22$

Dividing by $4! = 24$:

$$
\frac{12p^2 - 36p + 22}{24} = \frac{12p^2}{24} - \frac{36p}{24} + \frac{22}{24} = \frac{p^2}{2} - \frac{3p}{2} + \frac{11}{12}
$$

#### 5. Term in $\Delta^5 y_0$ (Optional Higher Term):
Numerator is $p^5 - 10p^4 + 35p^3 - 50p^2 + 24p$.
- First derivative: $5p^4 - 40p^3 + 105p^2 - 100p + 24$
- Second derivative: $20p^3 - 120p^2 + 210p - 100$

Dividing by $5! = 120$:

$$
\frac{20p^3 - 120p^2 + 210p - 100}{120} = \frac{p^3}{6} - p^2 + \frac{7p}{4} - \frac{5}{6}
$$

### Step 4: Assemble the First and Second Derivatives

Assembling the first derivative:

$$
\frac{dy}{dx} = \frac{1}{h}\left[\Delta y_0 + \frac{2p - 1}{2!}\Delta^2 y_0 + \frac{3p^2 - 6p + 2}{3!}\Delta^3 y_0 + \frac{4p^3 - 18p^2 + 22p - 6}{4!}\Delta^4 y_0 + \cdots\right]
$$

Assembling the second derivative:

$$
\frac{d^2y}{dx^2} = \frac{1}{h^2}\left[\Delta^2 y_0 + (p - 1)\Delta^3 y_0 + \left(\frac{p^2}{2} - \frac{3p}{2} + \frac{11}{12}\right)\Delta^4 y_0 + \cdots\right]
$$

---

## Special Case: Evaluating Derivatives at Tabular Nodes ($p = 0$)

When you want the derivative at the initial tabulated node $x = x_0$, we set $p = 0$.
The formula collapses into a clean alternating series:

### First Derivative at $x = x_0$ ($p = 0$):

$$
\left[\frac{dy}{dx}\right]_{x=x_0} = \frac{1}{h}\left(\Delta y_0 - \frac{1}{2}\Delta^2 y_0 + \frac{1}{3}\Delta^3 y_0 - \frac{1}{4}\Delta^4 y_0 + \frac{1}{5}\Delta^5 y_0 - \cdots\right)
$$

### Second Derivative at $x = x_0$ ($p = 0$):

$$
\left[\frac{d^2y}{dx^2}\right]_{x=x_0} = \frac{1}{h^2}\left(\Delta^2 y_0 - \Delta^3 y_0 + \frac{11}{12}\Delta^4 y_0 - \frac{5}{6}\Delta^5 y_0 + \cdots\right)
$$

---

## Stopping Rule & Minimum Data Points

In exam questions, you are often asked: *How many points are needed, and when does the formula terminate?*

1. **Termination for Polynomials:**
   An $n$-th degree polynomial fitted through $n+1$ points has constant $n$-th differences and zero $(n+1)$-th differences. Therefore, the series terminates exactly after the term in $\Delta^n y_0$.
   - For a quadratic ($n=2$): differences beyond $\Delta^2 y_0$ are zero.
   - For a cubic ($n=3$): differences beyond $\Delta^3 y_0$ are zero.
   - For a quartic ($n=4$): differences beyond $\Delta^4 y_0$ are zero.

2. **Minimum Points Required:**
   Because the formula for $\frac{d^2y}{dx^2}$ starts with $\Delta^2 y_0$, you need differences of at least second order. To compute a second difference $\Delta^2 y_0$, you need **at least three data points** ($x_0, x_1, x_2$).
   - 2 points give only a straight line (second derivative is identically zero).
   - 3 points give a quadratic fit (second derivative is constant: $\Delta^2 y_0 / h^2$).
   - 4 points give a cubic fit (second derivative varies linearly with $p$).

---

## The Backward Counterpart

If your evaluation point lies near the end of a tabulated dataset, forward differences would fall off the right edge of the table. You switch to Newton's backward difference formula anchored at $x_n$:

With $q = \frac{x - x_n}{h}$:

$$
\frac{d^2y}{dx^2} = \frac{1}{h^2}\left[\nabla^2 y_n + (q + 1)\nabla^3 y_n + \left(\frac{q^2}{2} + \frac{3q}{2} + \frac{11}{12}\right)\nabla^4 y_n + \cdots\right]
$$

At the final tabular node $x = x_n$ ($q = 0$), all signs become positive:

$$
\left[\frac{d^2y}{dx^2}\right]_{x=x_n} = \frac{1}{h^2}\left(\nabla^2 y_n + \nabla^3 y_n + \frac{11}{12}\nabla^4 y_n + \frac{5}{6}\nabla^5 y_n + \cdots\right)
$$

---

## 🧪 Proof of Exactness for a Cubic Function

To prove that this formula is mathematically rigorous and not an ad-hoc approximation, consider the test function $y = ax^3$.

Let $x_0 = 0$ with step size $h$, so that $x = ph$.
Tabulate the function values:
- $y_0 = y(0) = 0$
- $y_1 = y(h) = ah^3$
- $y_2 = y(2h) = 8ah^3$
- $y_3 = y(3h) = 27ah^3$

Compute the differences:
- $\Delta y_0 = ah^3 - 0 = ah^3$
- $\Delta y_1 = 8ah^3 - ah^3 = 7ah^3$
- $\Delta y_2 = 27ah^3 - 8ah^3 = 19ah^3$
- $\Delta^2 y_0 = 7ah^3 - ah^3 = 6ah^3$
- $\Delta^2 y_1 = 19ah^3 - 7ah^3 = 12ah^3$
- $\Delta^3 y_0 = 12ah^3 - 6ah^3 = 6ah^3$
- All higher differences $\Delta^4, \Delta^5, \dots$ are zero.

Now plug $\Delta^2 y_0 = 6ah^3$ and $\Delta^3 y_0 = 6ah^3$ into our second-derivative formula:

$$
\frac{d^2y}{dx^2} = \frac{1}{h^2}\left[6ah^3 + (p - 1)(6ah^3)\right] = \frac{6ah^3}{h^2}\left[1 + p - 1\right] = 6ah(p)
$$

Since $x = ph$, we have $ph = x$:

$$
\frac{d^2y}{dx^2} = 6ax
$$

Now calculate the true analytical derivative directly from calculus:

$$
y = ax^3 \implies y' = 3ax^2 \implies y'' = 6ax
$$

The numerical formula reproduces the exact derivative $6ax$ identically for **every single value of $p$**, not just at the tabular nodes!

---

## 🏆 Past Exam Questions

### 2017 Q.6(c): Derive Second Derivative Formula [04 Marks]

**The question:** Derive a formula to find the second derivative of a tabulated function.

**Full Solution:**

**Set-up:** Let $y = f(x)$ be tabulated at equally spaced nodes with interval $h$, and write $p = \dfrac{x - x_0}{h}$. Newton's forward interpolation formula is

$$
y = y_0 + p\Delta y_0 + \frac{p(p-1)}{2!}\Delta^2 y_0 + \frac{p(p-1)(p-2)}{3!}\Delta^3 y_0 + \frac{p(p-1)(p-2)(p-3)}{4!}\Delta^4 y_0 + \cdots
$$

**First derivative:** Since $dx = h\,dp$, differentiation with respect to $x$ is $(1/h)$ times differentiation with respect to $p$:

$$
\frac{dy}{dx} = \frac{1}{h}\left[\Delta y_0 + \frac{2p-1}{2!}\Delta^2 y_0 + \frac{3p^2-6p+2}{3!}\Delta^3 y_0 + \frac{4p^3-18p^2+22p-6}{4!}\Delta^4 y_0 + \cdots\right]
$$

The coefficient of $\Delta^k y_0$ is the derivative of the product $p(p-1)\cdots(p-k+1)$ divided by $k!$. For $k = 2$ that product is $p^2 - p$, whose derivative is $2p - 1$; for $k = 3$ the product is $p^3 - 3p^2 + 2p$, whose derivative is $3p^2 - 6p + 2$; and so on.

**Second derivative:** Differentiating a second time:

$$
\boxed{\frac{d^2y}{dx^2} = \frac{1}{h^2}\left[\Delta^2 y_0 + (p-1)\Delta^3 y_0 + \left(\frac{p^2}{2} - \frac{3p}{2} + \frac{11}{12}\right)\Delta^4 y_0 + \cdots\right]}
$$

Each coefficient is the second derivative of the corresponding product, divided by $k!$:

$$
\frac{d^2}{dp^2}\left(p^2 - p\right) = 2
$$

$$
\frac{d^2}{dp^2}\left(p^3 - 3p^2 + 2p\right) = 6p - 6
$$

$$
\frac{d^2}{dp^2}\left(p^4 - 6p^3 + 11p^2 - 6p\right) = 12p^2 - 36p + 22
$$

and dividing by $3!$ and $4!$ respectively gives $(p - 1)$ and $\left(\dfrac{p^2}{2} - \dfrac{3p}{2} + \dfrac{11}{12}\right)$.

**Stopping rule:** A polynomial of degree $n$ fitted through $n+1$ points has exactly $n+1$ coefficients. The differences of order greater than $n$ vanish identically, so the series above terminates after the term in $\Delta^n y_0$. Since $y''$ requires differences of order two and above, **at least three points are needed** for the formula to carry any information, and a cubic fit through four points carries terms up to $\Delta^3 y_0$.

**The backward counterpart:** Writing backward differences at the last node $x_n$ and putting $q = \dfrac{x - x_n}{h}$,

$$
\frac{d^2y}{dx^2} = \frac{1}{h^2}\left[\nabla^2 y_n + (q+1)\nabla^3 y_n + \left(\frac{q^2}{2} + \frac{3q}{2} + \frac{11}{12}\right)\nabla^4 y_n + \cdots\right]
$$

which is the form used when the tabulation runs in the decreasing direction.

---

### 2018 Q.5(a): State Newton's Forward Formula for Second Derivative [06 Marks]

**The question:** State Newton's forward formula to evaluate $\frac{d^2 y}{dx^2}$ for any value $x \in [x_0, x_n]$.

**Full Solution:**

**Newton's forward formula:** For a tabular spacing $h$, the forward difference interpolation polynomial through $n+1$ points is

$$
y = y_0 + p\Delta y_0 + \frac{p(p-1)}{2!}\Delta^2 y_0 + \frac{p(p-1)(p-2)}{3!}\Delta^3 y_0 + \frac{p(p-1)(p-2)(p-3)}{4!}\Delta^4 y_0 + \cdots
$$

with

$$
p = \frac{x - x_0}{h}
$$

**First derivative:** Differentiating term by term, $\dfrac{d}{dx} = \dfrac{1}{h}\dfrac{d}{dp}$:

$$
\frac{dy}{dx} = \frac{1}{h}\left[\Delta y_0 + \frac{2p - 1}{2!}\Delta^2 y_0 + \frac{3p^2 - 6p + 2}{3!}\Delta^3 y_0 + \frac{4p^3 - 18p^2 + 22p - 6}{4!}\Delta^4 y_0 + \cdots\right]
$$

**Second derivative:** Differentiating a second time:

$$
\frac{d^2y}{dx^2} = \frac{1}{h^2}\left[\Delta^2 y_0 + \frac{6p - 6}{3!}\Delta^3 y_0 + \frac{12p^2 - 36p + 22}{4!}\Delta^4 y_0 + \cdots\right]
$$

which simplifies to

$$
\boxed{\frac{d^2y}{dx^2} = \frac{1}{h^2}\left[\Delta^2 y_0 + (p - 1)\Delta^3 y_0 + \left(\frac{p^2}{2} - \frac{3p}{2} + \frac{11}{12}\right)\Delta^4 y_0 + \cdots\right]}
$$

**Validity:** The formula reproduces $\dfrac{d^2y}{dx^2}$ exactly for any polynomial of degree four or lower, because every term from $\Delta^5 y_0$ onward then vanishes. For a table of noisy experimental data the higher differences are not zero, and they are also the noisiest entries in the difference table, so the terms beyond the data's smoothness are not worth retaining.

**Terms retained:** A polynomial of degree $n$ through $n+1$ points has exactly $n+1$ coefficients, so for $n = 1$ only the $\Delta y_0$ term exists, for $n = 2$ the terms up to $\Delta^2 y_0$ exist, and so on. Since $y''$ requires differences of order two and above, the formula needs at least **three points** for a quadratic fit, four for a cubic, and so on. The next term, omitted above, is

$$
\left(\frac{p^3}{6} - p^2 + \frac{7p}{4} - \frac{5}{6}\right)\Delta^5 y_0
$$

---

## ⚡ Quick Review

**The derivation in four bullet points:**
1. Start with Newton forward interpolation: $y(p)$ with $p = (x - x_0)/h$.
2. Chain rule gives $\frac{d}{dx} = \frac{1}{h}\frac{d}{dp}$ and $\frac{d^2}{dx^2} = \frac{1}{h^2}\frac{d^2}{dp^2}$.
3. Differentiate falling factorials: $\frac{d^2}{dp^2}(p^2 - p) = 2$, $\frac{d^2}{dp^2}(p^3 - 3p^2 + 2p) = 6(p - 1)$, and $\frac{d^2}{dp^2}(P_4) = 12p^2 - 36p + 22$.
4. Divide each by $k!$ to get the coefficients: $1$, $(p-1)$, and $(p^2/2 - 3p/2 + 11/12)$.

**The golden formula:**
$$
\frac{d^2y}{dx^2} = \frac{1}{h^2}\left[\Delta^2 y_0 + (p - 1)\Delta^3 y_0 + \left(\frac{p^2}{2} - \frac{3p}{2} + \frac{11}{12}\right)\Delta^4 y_0 + \cdots\right]
$$

**The most common exam slips:**
- Forgetting the leading factor $1/h^2$ (writing $1/h$ or leaving it out).
- Writing $(p + 1)$ instead of $(p - 1)$ for the $\Delta^3 y_0$ coefficient.
- Failing to state that at least 3 points are required.

**Time estimate in exam:** 8 to 10 minutes for the complete derivation.

---

## 🔗 Connected Topics

- [← NM-7.2: First Derivative](NM-7.2_First_Derivative.md) -- evaluating numerical derivatives from actual tables and numbers.
- [→ NM-7.4: Applied Differentiation](NM-7.4_Applied_Differentiation.md) -- real-life engineering applications of first and second derivatives.
- [NM-4.7: Newton Forward Difference](../NM-4_Curve_Fitting/NM-4.7_Newton_Forward_Difference.md) -- the parent interpolation polynomial that is differentiated here.

---

[← Previous: NM-7.2 First Derivative](NM-7.2_First_Derivative.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: NM-7.4 Applied Differentiation →](NM-7.4_Applied_Differentiation.md)
