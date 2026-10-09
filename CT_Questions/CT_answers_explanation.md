---
title: "ECE 2213 · Class Test Answers, Explained"
tags:
  - numerical-methods
  - discrete-mathematics
  - class-tests
---

# ECE 2213: Class Test Answers, Explained

**RUET · ECE Dept · B.Sc. Engineering 2nd Year**

The same 19 answers as `CT_answers_exam_style.md`, with the reasoning shown.
This layer may address you directly, explain at length, and say why a step is
hard. Every number is identical to the exam-style file, character for character,
and the exam-style file is where each one is authored.

> [!info] How to read this against the exam-style file
> The exam-style file says **what the answer is**. This file says **why that
> answer, why the tempting wrong answer is wrong, and how to check the result in
> ten seconds**. When you are revising for an exam, read this one. When you are
> writing an answer under time pressure, read the other one.
>
> The marks line is the same in both files, and it is the same everywhere:
>
> ```
> **[Marks: not printed in source]**
> ```
>
> Class tests print marks per question, never per part, so there is nothing to
> print. No split has been guessed. See `CT_Questions/README.md`.

---

## Class Test 01

**Modeling, truncation and round-off errors · bisection and regula falsi**

### **(a) Develop a mathematical model representing the temperature estimation problem and identify the assumptions made.**

*[Marks: not printed in source]*

Let us start from the actual engineering problem, because "develop a model" sounds
like a formality and is not. The company cannot put thermocouples inside a
running reactor, so it wants software that predicts $T(t)$ from what it can
measure. The first question is therefore not *which formula* but *what is being
approximated*, and the honest answer has two halves: the software approximates a
**model**, and the model approximates the **reactor**. Those are two separate
approximations with two separate error budgets, and a question that asks for both
a model and its assumptions is asking you to keep them apart.

**Step 1: the balance.** Energy in minus energy out equals energy stored. For a
well-mixed reactor of mass $m$ and specific heat $C$:

$$C \frac{dT}{dt} = Q(t) - hA\bigl(T - T_a(t)\bigr)$$

Four terms, and each one is a modelling decision rather than a fact:

- $C\frac{dT}{dt}$, the stored energy. Proportional to $T$ because raising a
  temperature costs energy.
- $Q(t)$, the reaction heat. Assumed **known**, which is the assumption most
  likely to be wrong.
- $-hA(T - T_a)$, the loss to ambient. Newton's law of cooling: proportional to
  the temperature *difference*, not to $T$ itself.
- $T_a(t)$, the ambient. Assumed **measured**, not predicted, so the model
  carries no weather uncertainty.

**Step 2: what the software actually computes.** The question says the software
evaluates the exponential with the first four non-zero Taylor terms. For
$z = (T - T_a)/T_a$,

$$e^z \approx 1 + z + \frac{z^2}{2!} + \frac{z^3}{3!}$$

with remainder $\dfrac{z^4 e^{\xi}}{4!}$ for some $\xi$ between $0$ and $z$.

**Step 3: check the model before trusting the software.** Set $dT/dt = 0$:

$$T_{ss} = T_a + \frac{Q}{hA}$$

and read off the time constant $\tau = C/hA$. The model therefore predicts **one
exponential approach, no overshoot, no second stage**. That is a testable
prediction, and it is the most useful thing on this page: if the real reactor
overshoots or responds in two stages, a model is wrong, and no amount of
precision in the exponential will fix it.

> [!tip] The question behind the question
> "Identify the assumptions made" is not asking for a list to memorise. It is
> asking you to show that each assumption, if false, produces an *observable*
> mismatch. Six assumptions, each with a stated failure signature, is a
> different and better answer than six assumptions with a bullet each. The
> radiation omission below is the clearest example: at high temperature it is not
> a small correction, it is a term of the same order as the one you kept.

**The six assumptions, each with what breaks it:**

| # | Assumption | If it is wrong |
| :-- | :-- | :-- |
| 1 | Well mixed, one state variable | A measurable internal gradient appears; a distributed model is needed |
| 2 | $C$, $h$, $A$ constant | For a gas $C$ varies with $T$; a fouled surface loses $h$ over time |
| 3 | $Q(t)$ known | A changing composition makes the heat release uncertain, and it feeds the model directly |
| 4 | Linear heat loss, $hA(T - T_a)$ | Radiation scales as $T^4$ and is **omitted entirely** |
| 5 | Ambient measured, not predicted | No weather term, so no weather error in the model |
| 6 | Sensors and stirring negligible | Safe only for a large, slowly driven vessel |

Assumption 4 is the one that bites here, and it is worth understanding *why*.
We kept a term linear in $T$ and discarded one proportional to $T^4$. At $T = 300$
those are comparable in order of magnitude; at $T = 600$ the discarded term is
many times the kept one. So the model is not slightly wrong at high temperature,
it is *qualitatively* wrong, and the software is being asked to be accurate about
a quantity that is itself inaccurate. This is the deepest point in the question
and the one most answers miss.

> [!warning] The follow-on question this sets up
> Part (b) asks for sources of numerical error. The distinction that earns the
> marks is that **part (a)'s assumption 4 is a modelling error and part (b)'s
> items are numerical errors**, and no numerical method can repair the first. A
> perfect solver applied to a wrong model returns a confidently wrong answer,
> which is worse than an obviously wrong one because nothing flags it.

### **(b) Identify at least three possible sources of numerical error in the software and explain how each affects the final prediction.**

*[Marks: not printed in source]*

The machine stores 5 significant decimal digits. Every error below is live in
that regime.

**The framing that makes this a good answer.** "At least three sources" invites a
list, and a list is what most answers give. The stronger answer classifies them,
because the classification *tells you which ones you can fix*. Two of the four
kinds below are reduced by working harder and two are made worse by it, and a
candidate who knows that can say something a list cannot.

**1. Truncation error from the Taylor series.** Discarding terms past $z^3/3!$
leaves $\dfrac{z^4 e^{\xi}}{4!}$. This is a **systematic** error: one sign, the
same on every cycle, and it does not average away over repeated runs. It grows
like $z^4$, so for a reactor running well above ambient it dominates. Because it
truncates from above, the software reads slightly **low**.

**2. Round-off error from 5-digit storage.** Every operation is performed to five
figures and the rest discarded. This is **random** in sign, so over many
simulations it partly cancels; accumulated size grows like $\sqrt{n}$ for $n$
independent roundings, and like $n$ in the worst case where every rounding is
biased the same way. Magnitude is about $10^{-5}$ relative per operation.

**3. Catastrophic cancellation.** This is the one that is specifically a function
of the problem, not the method, and it deserves more than a line. When $z$ is
small, $e^z$ is close to $1$, so computing it as $1 + z + z^2/2 + z^3/6$ subtracts
almost as much as it adds. Watch the partial sums at $z = 0.1$:

| partial sum | value | digits gained | digits already lost |
| :-- | --: | :-- | :-- |
| $1$ | 1.000000 | 0 | 0 |
| $1 + 0.1$ | 1.100000 | 0 | 0 |
| $+ 0.005$ | 1.105000 | 1 | 1 |
| $+ 0.0001667$ | 1.105167 | 3 | 3 |

The answer is $1.105170$, correct to six figures, but the **leading digit was
destroyed in the first addition** and never recovered. The relative error is
amplified by roughly $1/(1 - e^{-z})$ times machine epsilon, which at $z = 0.1$
is about a factor of ten. The general rule: cancellation is dangerous exactly when
the answer is small compared to the intermediate quantities, and $e^z \approx 1$
is the standard example.

**4. Truncation error from the time-stepping.** Whatever scheme advances $T$ in
time replaces an integral by a finite sum, with error $\propto h^p$ for order
$p$. The subtle part: with $h$ too large, the discrete solution settles at a
**different steady state** from the continuous one. That is a modelling error
wearing a numerical disguise, and it is why the step size is not a free
parameter.

**5. Input and measurement error.** $Q$, $h$, $A$, $T_a$ all carry error, and the
sensitivity to $hA$ is the sharpest: an error $\epsilon$ in $h$ shifts the steady
state by roughly $\epsilon Q/(hA)^2$.

**6. Accumulation across repeated simulations.** If each cycle starts from the
previous cycle's rounded output, errors compound rather than resetting. One
computation at 5 digits is fine; ten thousand chained ones are not.

> [!tip] The one experiment that separates them
> Run the software twice. Once at **half the step** with 5 digits; once at **full
> step with 10 digits**.
>
> | observation | diagnosis |
> | :-- | :-- |
> | answer moves when the step is halved | truncation dominates |
> | answer moves when precision is widened | round-off dominates |
> | neither moves it | the error is in the **model** or the **inputs** |
>
> That single comparison turns "there are several sources" into a diagnosis, and
> it is the difference between listing and explaining.

> [!warning] The trap: the two errors move in opposite directions
> Truncation shrinks with more terms, smaller $h$, or a higher-order scheme.
> Round-off **grows** under every one of those, because each is another
> arithmetic operation to be rounded. So the software cannot be made accurate
> simply by working harder; there is an optimum beyond which precision is traded
> for accuracy. With 5 digits the round-off floor sits near $10^{-5}$ relative, so
> extending the Taylor series is worth it only until its remainder falls below
> that level, and no further. Knowing where the optimum is **is** the answer to
> "how each affects the final prediction."

---

## Class Test 02 (Set A)

**Lagrange and Newton's forward/backward interpolation**

### **Use the Lagrange Interpolation Formula to estimate the concentration at 5 km.**

*[Marks: not printed in source]*

| Distance (km) | 2 | 4 | 7 | 10 |
| :-- | --: | --: | --: | --: |
| Concentration (mg/L) | 18 | 26 | 43 | 60 |

**Why Lagrange is the right tool here, before any arithmetic.** Look at the node
spacing: $2, 4, 7, 10$, with gaps of $2, 3, 3$. They are **not** an arithmetic
progression. Newton's forward and backward formulas in their standard forms both
require equal spacing, because they are built on a difference table whose first
column is constant. Lagrange needs no such thing. The method choice is forced by
the data, and saying so is part of the answer.

**The formula.**

$$P(x) = \sum_{i=0}^{n} y_i L_i(x), \qquad L_i(x) = \prod_{j \neq i}\frac{x - x_j}{x_i - x_j}$$

Each $L_i$ is $1$ at its own node and $0$ at every other, which is exactly why
the interpolant passes through all four points.

**The four basis values at $x = 5$.**

$$L_0(5) = \frac{(5-4)(5-7)(5-10)}{(2-4)(2-7)(2-10)} = \frac{(1)(-2)(-5)}{(-2)(-5)(-8)} = \frac{10}{-80} = -\frac{1}{8}$$

$$L_1(5) = \frac{(5-2)(5-7)(5-10)}{(4-2)(4-7)(4-10)} = \frac{(3)(-2)(-5)}{(2)(-3)(-6)} = \frac{30}{36} = \frac{5}{6}$$

$$L_2(5) = \frac{(5-2)(5-4)(5-10)}{(7-2)(7-4)(7-10)} = \frac{(3)(1)(-5)}{(5)(3)(-3)} = \frac{-15}{-45} = \frac{1}{3}$$

$$L_3(5) = \frac{(5-2)(5-4)(5-7)}{(10-2)(10-4)(10-7)} = \frac{(3)(1)(-2)}{(8)(6)(3)} = \frac{-6}{144} = -\frac{1}{24}$$

> [!tip] The free check, and you should do it every time
> $$L_0 + L_1 + L_2 + L_3 = -\frac18 + \frac56 + \frac13 - \frac{1}{24} = -\frac{3}{24} + \frac{20}{24} + \frac{8}{24} - \frac{1}{24} = \frac{24}{24} = 1$$
>
> It is $1$ at **every** $x$, not just here. It costs one line and it catches the
> commonest error in the whole method, a sign slip in one denominator, which
> otherwise produces a plausible number that is wrong.

**The estimate.**

$$P(5) = 18\left(-\frac{1}{8}\right) + 26\left(\frac{5}{6}\right) + 43\left(\frac{1}{3}\right) + 60\left(-\frac{1}{24}\right)$$

$$= -2.25 + 21.6667 + 14.3333 - 2.5$$

$$\boxed{C(5) = 31.25 \ \text{mg/L}}$$

**Second route, and it is worth doing in an exam.** Newton's divided-difference
form uses the same four points through a completely different algorithm:

| order | divided differences |
| :-- | :-- |
| 0 | $18, 26, 43, 60$ |
| 1 | $4, \frac{17}{3}, \frac{17}{3}$ |
| 2 | $\frac{1}{3}, 0$ |
| 3 | $-\frac{1}{24}$ |

so $P(x) = 18 + 4(x-2) + \frac13(x-2)(x-4) - \frac{1}{24}(x-2)(x-4)(x-7)$, and at
$x = 5$:

$$P(5) = 18 + 4(3) + \frac13(3)(1) - \frac{1}{24}(3)(1)(-2) = 18 + 12 + 1 + 0.25 = 31.25$$

Same value by a different arrangement, so neither route's arithmetic is
responsible for it. Note also that the order-3 coefficient $-\frac{1}{24}$ is
$L_3$'s numerator-independent constant, which is a good sign the two agree
structurally and not just numerically.

**What the polynomial actually is.** Expanding:

$$P(x) = -\frac{1}{24}x^3 + \frac78 x^2 - \frac{1}{12}x + 15$$

Two observations that belong in a good answer. First, $x = 5$ lies **inside**
$[2, 10]$, so this is interpolation, not extrapolation, and the value carries the
data's own reliability rather than an extrapolation risk. Second, the cubic is
mild: the concentration curve is concave, and a cubic tracks a concave curve
without the wild oscillation that high-degree interpolation produces on
unevenly spaced nodes. Unequal spacing is exactly where high-degree Lagrange
turns dangerous, and at degree 3 there is no room for trouble.

### **Use Newton's Forward/Backward Interpolation Formula to estimate the temperature at 1.5 and 7 hours.**

*[Marks: not printed in source]*

| Time (hours) | 0 | 2 | 4 | 6 | 8 |
| :-- | :--: | :--: | :--: | :--: | :--: |
| Temperature (°C) | 24 | 27 | 31 | 36 | 42 |

**The difference table, with $h = 2$:**

| order | values |
| :-- | :-- |
| $y$ | 24, 27, 31, 36, 42 |
| $\Delta y$ | 3, 4, 5, 6 |
| $\Delta^2 y$ | 1, 1, 1 |
| $\Delta^3 y$ | 0, 0 |
| $\Delta^4 y$ | 0 |

> [!tip] Stop here for a moment: the third differences are zero
> The table terminates after order two, so the data lie **exactly** on a
> quadratic, and **Newton's formula is exact here, not an approximation.**
>
> This costs nothing to notice and it is the strongest check available, because
> it explains the answer rather than merely confirming it. If a later digit
> disagrees, the data or the table is wrong, not the method.

**At 1.5 hours, Newton's forward formula.** $1.5$ is near the *start* of the
table, so measure forward from $x_0 = 0$:

$$p = \frac{x - x_0}{h} = \frac{1.5}{2} = 0.75$$

$$y = y_0 + p\Delta y_0 + \frac{p(p-1)}{2!}\Delta^2 y_0 + \frac{p(p-1)(p-2)}{3!}\Delta^3 y_0$$

$$= 24 + (0.75)(3) + \frac{(0.75)(-0.25)}{2}(1) + 0$$

$$= 24 + 2.25 - 0.09375$$

$$\boxed{T(1.5) = 26.15625 \approx 26.16 \ ^\circ\text{C}}$$

Note the middle term is **negative**, because $0 < p < 1$ makes $(p-1)$ negative.
That is correct and it surprises people: the curve is concave up, but at $p$
between 0 and 1 the forward series subtracts to place the point below the linear
interpolation of the endpoints. Linear interpolation would give $24 + 0.75(3) =
26.25$; the true value is slightly lower.

**At 7 hours, Newton's backward formula.** $7$ is near the *end*, so measure
backward from $x_n = 8$:

$$p = \frac{x - x_n}{h} = \frac{7 - 8}{2} = -0.5$$

$$y = y_n + p\nabla y_n + \frac{p(p+1)}{2!}\nabla^2 y_n + \frac{p(p+1)(p+2)}{3!}\nabla^3 y_n$$

$$= 42 + (-0.5)(6) + \frac{(-0.5)(0.5)}{2}(1) + 0$$

$$= 42 - 3 - 0.125$$

$$\boxed{T(7) = 38.875 \approx 38.88 \ ^\circ\text{C}}$$

**Third route: the exact quadratic.** Since the third differences vanish, fit the
quadratic directly. With $y = a + bx + cx^2$ and $h = 2$, $\Delta^2 y = 2ch^2$ so
$c = \frac{1}{8}$; then $y(2) = 27$ gives $b = \frac54$, and $y(0) = 24$ gives
$a = 24$:

$$P(x) = \frac{x^2}{8} + \frac{5x}{4} + 24$$

$$P(1.5) = \frac{2.25}{8} + 1.875 + 24 = 0.28125 + 1.875 + 24 = \frac{837}{32} = 26.15625 \checkmark$$

$$P(7) = \frac{49}{8} + \frac{35}{4} + 24 = 6.125 + 8.75 + 24 = \frac{311}{8} = 38.875 \checkmark$$

Three routes, all exact, all agreeing.

> [!warning] The sign of $p$ is where marks are lost here, every time
> Newton's **backward** formula uses $p = (x - x_n)/h$, which is **negative** for
> a point inside the table. Writing $p = (x_n - x)/h = +0.5$ gives
> $42 + 3 + 0.375 = 45.375$ instead of $38.875$, and the error is large because
> the **first-order** term has the opposite sign.
>
> **Three habits that prevent it.**
>
> 1. The backward formula's argument is a *rising* factorial $p(p+1)(p+2)$;
>    the forward formula's is *falling*, $p(p-1)(p-2)$. If you wrote a minus,
>    you are in the forward formula.
> 2. Check $p$'s sign before computing anything: forward means $0 \le p < 1$
>    from the start of the table, backward means $-1 < p \le 0$ from the end.
> 3. **Sanity-check against the data.** At 7 hours the tabulated values go
>    $36$ then $42$, so the answer must lie strictly between them. $45.375$
>    exceeds the last tabulated value, which should have rejected it on sight.
>    $38.875$ sits between $36$ and $42$, as it must.
>
> Habit 3 is the strongest, because it needs no memory of formulae at all. It
> catches the sign error, a wrong node, and a wrong column of the difference
> table, all at once.

---

## Class Test 02 (Set B)

**Gauss-Seidel iteration and Runge-Kutta methods**

### **(a) Rearrange the equations in a suitable form for the Gauss-Seidel iterative method.**

*[Marks: not printed in source]*

$$4x + y + z = 7, \qquad x + 5y + 2z = -8, \qquad 2x + y + 6z = 6$$

**The rearrangement.** Solve each equation for its own diagonal unknown:

$$x = \frac{7 - y - z}{4}, \qquad y = \frac{-8 - x - 2z}{5}, \qquad z = \frac{6 - 2x - y}{6}$$

That is the mechanical step. The interesting step is the check that follows.

**Check that the system suits the method.** Compare each diagonal entry against
the sum of the off-diagonal entries in its own row:

$$\lvert 4\rvert > 1 + 1 = 2, \qquad \lvert 5\rvert > 1 + 2 = 3, \qquad \lvert 6\rvert > 2 + 1 = 3$$

Every row is **strictly diagonally dominant**. Strict dominance in every row is
the sufficient condition for Gauss-Seidel to converge from *any* starting vector,
so this system is set up for the method and no reordering can improve it. Also
$\det A = 101 \neq 0$, so the solution is unique and iteration has something to
converge to.

> [!tip] Why the check is worth the two minutes
> Diagonal dominance is the difference between a convergence guarantee and a
> hope. Without it, Gauss-Seidel can diverge, and the 2017 paper contains a
> worked example where it does, in **every** variable ordering. Being able to say
> "strictly diagonally dominant, so convergence is guaranteed from any start" is
> a stronger statement than any numerical answer, and it is two lines of
> arithmetic.

**The Gauss-Seidel form, written so the ordering is visible.**

$$x^{(k+1)} = \frac{7 - y^{(k)} - z^{(k)}}{4}$$

$$y^{(k+1)} = \frac{-8 - x^{(k+1)} - 2z^{(k)}}{5}$$

$$z^{(k+1)} = \frac{6 - 2x^{(k+1)} - y^{(k+1)}}{6}$$

The superscripts are the entire content of the method. $x$ uses the **old** $y$
and $z$; $y$ uses the **new** $x$ and the old $z$; $z$ uses the **new** $x$ and the
**new** $y$. The two $(k+1)$ superscripts on the right of the second and third
equations are precisely the difference from Jacobi, where every right-hand side
would read $(k)$.

> [!warning] The transcription slip in the source, and why it matters
> The source prints $X$ in the second equation where the other two use $x$:
> $X + 5y + 2z = -8$. Read as a fourth distinct variable the system is not square,
> and Gauss-Seidel has nothing to iterate. It must mean $x$, since it is one
> system in three unknowns, and the source says as much in a parenthetical note.
> Worth writing the equation correctly in your answer rather than copying the
> capital, and worth a half-line saying why: a marker reading nine systems with
> a stray fourth variable is entitled to doubt the other eight.

### **(b) Starting with $x_0 = 0$, $y_0 = 0$, $z_0 = 0$, perform four complete iterations using the Gauss-Seidel method.**

*[Marks: not printed in source]*

**Iteration 1**, from $(0, 0, 0)$:

$$x_1 = \frac{7 - 0 - 0}{4} = 1.75$$

$$y_1 = \frac{-8 - 1.75 - 2(0)}{5} = \frac{-9.75}{5} = -1.95$$

$$z_1 = \frac{6 - 2(1.75) - (-1.95)}{6} = \frac{6 - 3.5 + 1.95}{6} = \frac{4.45}{6} = 0.741667$$

**Iteration 2:**

$$x_2 = \frac{7 - (-1.95) - 0.741667}{4} = \frac{7 + 1.95 - 0.741667}{4} = \frac{8.208333}{4} = 2.052083$$

$$y_2 = \frac{-8 - 2.052083 - 2(0.741667)}{5} = \frac{-8 - 2.052083 - 1.483333}{5} = \frac{-11.535417}{5} = -2.307083$$

$$z_2 = \frac{6 - 2(2.052083) - (-2.307083)}{6} = \frac{6 - 4.104167 + 2.307083}{6} = \frac{4.202917}{6} = 0.700486$$

**Iteration 3:**

$$x_3 = \frac{7 - (-2.307083) - 0.700486}{4} = \frac{7 + 2.307083 - 0.700486}{4} = \frac{8.606597}{4} = 2.151649$$

$$y_3 = \frac{-8 - 2.151649 - 2(0.700486)}{5} = \frac{-8 - 2.151649 - 1.400972}{5} = \frac{-11.552621}{5} = -2.310524$$

$$z_3 = \frac{6 - 2(2.151649) - (-2.310524)}{6} = \frac{6 - 4.303299 + 2.310524}{6} = \frac{4.007225}{6} = 0.667871$$

**Iteration 4:**

$$x_4 = \frac{7 - (-2.310524) - 0.667871}{4} = \frac{7 + 2.310524 - 0.667871}{4} = \frac{8.642653}{4} = 2.160663$$

$$y_4 = \frac{-8 - 2.160663 - 2(0.667871)}{5} = \frac{-8 - 2.160663 - 1.335742}{5} = \frac{-11.496405}{5} = -2.299281$$

$$z_4 = \frac{6 - 2(2.160663) - (-2.299281)}{6} = \frac{6 - 4.321326 + 2.299281}{6} = \frac{3.977955}{6} = 0.662992$$

**The four iterations.**

| $k$ | $x$ | $y$ | $z$ |
| :--: | --: | --: | --: |
| 1 | 1.750000 | -1.950000 | 0.741667 |
| 2 | 2.052083 | -2.307083 | 0.700486 |
| 3 | 2.151649 | -2.310524 | 0.667871 |
| 4 | 2.160663 | -2.299281 | 0.662992 |

$$\boxed{(x_4, y_4, z_4) = (2.160663,\ -2.299281,\ 0.662992)}$$

> [!warning] The slip this method invites, and the free check that catches it
> The numerator of $x_2$ is $7 - y_1 - z_1 = 7 - (-1.95) - 0.741667$. The two
> subtractions have **opposite signs**, because $y_1$ is negative and $z_1$ is
> positive. Writing $7 + 1.95 - 0.741667 - 0.741667$ double-counts the second
> term and gives $x_2 = 1.866667$ instead of $2.052083$, an error of $0.19$, about
> four times the largest error anywhere in the correct table.
>
> The catch is free and it is not arithmetic: **the new $x$ must lie between the
> old $x$ and the true root.** The exact solution is $218/101 = 2.158416$, so a
> second iterate below that is required. $2.052083$ satisfies it;
> $1.866667$ has moved *away* from the root it was converging to. An iterate that
> moves away from a known solution has an arithmetic error somewhere, and the
> bracket test finds it in one comparison.

> [!tip] Two independent checks on the table, both worth doing
> **Substitution of the exact solution.** $(218/101,\ -232/101,\ 67/101) =
> (2.158416,\ -2.297030,\ 0.663366)$ satisfies the original system exactly:
> $$4\left(\frac{218}{101}\right) + \left(-\frac{232}{101}\right) + \left(\frac{67}{101}\right) = \frac{872 - 232 + 67}{101} = \frac{707}{101} = 7 \checkmark$$
> $$\frac{218}{101} + 5\left(-\frac{232}{101}\right) + 2\left(\frac{67}{101}\right) = \frac{218 - 1160 + 134}{101} = \frac{-808}{101} = -8 \checkmark$$
> $$2\left(\frac{218}{101}\right) + \left(-\frac{232}{101}\right) + 6\left(\frac{67}{101}\right) = \frac{436 - 232 + 402}{101} = \frac{606}{101} = 6 \checkmark$$
> so the iteration is heading for the right point.
>
> **The convergence rate.** The Gauss-Seidel iteration matrix has spectral radius
> $\rho = 0.5281$, so the error should shrink by roughly half per sweep. The
> errors in $x$ across the four sweeps are $0.4084,\ 0.1063,\ 0.0068,\ 0.0022$,
> whose ratios $0.26,\ 0.06,\ 0.33$ bracket $0.528$ closely enough to confirm both
> the table and the order in which the equations were applied. A wrong ordering
> gives a different iteration matrix and different ratios, so this check tests
> the ordering as well as the arithmetic.

### **(c) Calculate the absolute error in $x$, $y$, and $z$ between the third and fourth iterations.**

*[Marks: not printed in source]*

The absolute errors are the differences between consecutive iterates:

$$\lvert x_4 - x_3\rvert = \lvert 2.160663 - 2.151649\rvert = 0.009014$$

$$\lvert y_4 - y_3\rvert = \lvert -2.299281 - (-2.310524)\rvert = 0.011243$$

$$\lvert z_4 - z_3\rvert = \lvert 0.662992 - 0.667871\rvert = 0.004879$$

$$\boxed{\lvert\Delta x\rvert = 0.009014, \quad \lvert\Delta y\rvert = 0.011243, \quad \lvert\Delta z\rvert = 0.004879}$$

**Why the question says *between* iterations.** This is a precise phrase and it
is asking for the **approximate** error, which is the difference of consecutive
iterates. That is *not* the error in the answer:

| | $x$ | $y$ | $z$ |
| :-- | --: | --: | --: |
| approximate, $\lvert x_4 - x_3\rvert$ | 0.009014 | 0.011243 | 0.004879 |
| true, $\lvert x_4 - x_{\text{exact}}\rvert$ | 0.002247 | 0.002251 | 0.000374 |
| relative approximate | 0.42% | 0.49% | 0.74% |

Both numbers are legitimate. The question asks for the first, and answering with
the second is a real and common error, so it is worth being able to state which
is which without hesitating. The approximate error bounds nothing; it only
describes the progress of the last sweep. On a slowly converging system the two
can differ by an order of magnitude.

> [!note] A caveat that is usually left out, and it is honest to include it
> The true errors here are close to a quarter of the approximate ones, which
> invites the tidy conclusion that the two are always in a fixed ratio. They are
> not, and the theory says why. With $\rho = 0.5281$ and the error contracting
> geometrically,
> $$e_4 = \rho e_3, \qquad \lvert\Delta\rvert = e_3 - e_4 = (1-\rho)e_3, \qquad \frac{e_4}{\lvert\Delta\rvert} = \frac{\rho}{1-\rho} = 1.12$$
> so in the **asymptotic** regime the true error is slightly *larger* than the
> approximate one. The observed factor of four is smaller still, because these
> four sweeps are still in the transient: the error sequence
> $0.4084,\ 0.1063,\ 0.0068,\ 0.0022$ has ratios $0.26,\ 0.06,\ 0.33$ that bracket
> $0.53$ only loosely. The "quarter" is an empirical observation from this table,
> not a theorem, and worth knowing so it is not over-relied on elsewhere.

### **(a) Using RK2 method with step size $h = 0.2$, calculate $y(0.2)$ and $y(0.4)$. Show both the predictor and corrector calculations at each step.**

*[Marks: not printed in source]*

$$\frac{dy}{dx} = x^2 - y, \qquad y(0) = 1, \qquad f(x,y) = x^2 - y$$

**Which RK2, and why this one.** "RK2" names a family, not a method. The
convention in this course, taken from the past papers, is **Heun's method**: a
slope at the start of the step, a slope at the predicted end point, averaged.

$$k_1 = f(x_n, y_n), \qquad k_2 = f\left(x_n + h,\ y_n + hk_1\right)$$

$$y_{n+1} = y_n + \frac{h}{2}\left(k_1 + k_2\right)$$

The three arrangements and what they give on this problem are tabulated below.
Naming which one you used is part of a correct answer.

**Step 1: $x_0 = 0$ to $x_1 = 0.2$, with $y_0 = 1$.**

Predictor slope:

$$k_1 = 0^2 - 1 = -1$$

Predicted value at the end of the step:

$$y_1^{*} = y_0 + hk_1 = 1 + 0.2(-1) = 0.8$$

Corrector slope, evaluated at the predicted end point:

$$k_2 = (0 + 0.2)^2 - \left(1 + 0.2(-1)\right) = 0.04 - 0.8 = -0.76$$

Update:

$$y_1 = 1 + \frac{0.2}{2}\left(-1 + (-0.76)\right) = 1 + 0.1(-1.76) = 1 - 0.176$$

$$\boxed{y(0.2) \approx 0.8240}$$

**Step 2: $x_1 = 0.2$ to $x_2 = 0.4$, with $y_1 = 0.824$.**

$$k_1 = (0.2)^2 - 0.824 = 0.04 - 0.824 = -0.784$$

$$y_2^{*} = 0.824 + 0.2(-0.784) = 0.824 - 0.1568 = 0.6672$$

$$k_2 = (0.2 + 0.2)^2 - 0.6672 = 0.16 - 0.6672 = -0.5072$$

$$y_2 = 0.824 + \frac{0.2}{2}\left(-0.784 + (-0.5072)\right) = 0.824 + 0.1(-1.2912) = 0.824 - 0.12912$$

$$\boxed{y(0.4) \approx 0.6949}$$

**The results.**

| $x$ | $y$ |
| :--: | --: |
| 0.0 | 1.0000 |
| 0.2 | 0.8240 |
| 0.4 | 0.6949 |

> [!tip] Check against the exact solution, which here is available
> $y' + y = x^2$ has particular solution $x^2 - 2x + 2$ and homogeneous part
> $Ce^{-x}$. With $y(0) = 1$ we get $C = -1$, so
> $$y = x^2 - 2x + 2 - e^{-x}$$
> $$y(0.2) = 0.04 - 0.4 + 2 - e^{-0.2} = 1.64 - 0.818731 = 0.821269$$
> $$y(0.4) = 0.16 - 0.8 + 2 - e^{-0.4} = 1.36 - 0.670320 = 0.689680$$
>
> So RK2 with $h = 0.2$ **overshoots** by $0.002731$ at $x = 0.2$ and by
> $0.005200$ at $x = 0.4$. Having the exact solution for a practice IVP is
> unusual and worth exploiting: it turns "my answer looks plausible" into a
> measured error.

**Two different error behaviours, and keeping them apart is the point.**

| effect | how to test it | result here |
| :-- | :-- | :-- |
| truncation grows as $x$ advances along the interval | compare $e(0.2)$ with $e(0.4)$ | $0.002731 \to 0.005200$ |
| truncation falls as $h$ shrinks | **halve $h$ and compare at the same $x$** | ratios $4.15$ and $4.16$ |

The second row is the convergence-order test, and it must be done at a **fixed
$x$**. Halving to $h = 0.1$ gives $y(0.2) = 0.821928$ and $y(0.4) = 0.690931$,
with errors $0.000658$ and $0.001251$, so

$$\frac{0.002731}{0.000658} = 4.15, \qquad \frac{0.005200}{0.001251} = 4.16$$

$4 \approx 2^2$ is the second-order signature. The ratios are $4.15$ rather than
exactly $4$ because a third-order term still survives at the coarser step: at
$h = 0.2$ it is roughly a quarter of the second-order contribution. That is a
feature, not an error, and it tells you the asymptotic regime has not quite been
reached.

> [!warning] Three traps in a two-stage method
> **The corrector must be evaluated at the predicted point.** Writing
> $k_2 = f(x_n + h,\ y_n)$ instead of $f(x_n+h,\ y_n + hk_1)$ applies the
> trapezoidal rule with no prediction, which is no longer second order. The
> halving test exposes it immediately: the ratio comes out near $2$, not near $4$.
>
> **The predictor is not the answer.** Heun reports
> $y_n + \frac{h}{2}(k_1 + k_2)$, not the predicted $y_n + hk_1$. The two differ
> by $\frac{h}{2}(k_2 - k_1)$; at step 1 that is $0.1(0.24) = 0.024$, about nine
> times the error of the finished answer. A method that returns its own predictor
> has silently degenerated to Euler.
>
> **The intermediate $y$ must be carried, not rounded away.** Step 2 starts from
> $y_1 = 0.824$, the *rounded* value from step 1. Carrying full precision changes
> later digits slightly; with 5-digit working it is not important, but a method
> that resets $y$ to $y_0$ at each step is not Runge-Kutta at all.

**The three arrangements side by side**, since "RK2" is a family and the constants
genuinely differ:

| arrangement | $y(0.2)$ | $y(0.4)$ | error at $0.2$ |
| :-- | --: | --: | --: |
| **Heun** | 0.824000 | 0.694880 | $+0.002731$ |
| midpoint | 0.822000 | 0.691240 | $+0.000731$ |
| Ralston | 0.820148 | 0.687469 | $-0.001121$ |

The midpoint method takes $k_2 = f\left(x_n + \frac{h}{2},\ y_n + \frac{h}{2}k_1\right)$
and $y_{n+1} = y_n + hk_2$, with **no averaging**; Ralston weights $1/3$ and
$2/3$. All three are second order, so all three converge at the same rate, and
their constants differ. Heun is the course convention and the most accurate of
the three on this problem, which is an observation about this problem and not a
general claim.

### **(b) Using the RK4 method calculate $y(0.2)$, also compare result with RK2 method.**

*[Marks: not printed in source]*

$$\frac{dy}{dx} = x^2 - y, \qquad y(0) = 1, \qquad h = 0.2$$

**The four-stage formula.**

$$k_1 = f(x_n, y_n), \qquad k_2 = f\left(x_n + \frac{h}{2},\ y_n + \frac{h}{2}k_1\right)$$

$$k_3 = f\left(x_n + \frac{h}{2},\ y_n + \frac{h}{2}k_2\right), \qquad k_4 = f(x_n + h, y_n + hk_3)$$

$$y_{n+1} = y_n + \frac{h}{6}\left(k_1 + 2k_2 + 2k_3 + k_4\right)$$

**Step 1: $x_0 = 0$, $y_0 = 1$, $h = 0.2$.**

$$k_1 = 0^2 - 1 = -1$$

$$k_2 = (0.1)^2 - \left(1 + 0.1(-1)\right) = 0.01 - 0.9 = -0.89$$

$$k_3 = (0.1)^2 - \left(1 + 0.1(-0.89)\right) = 0.01 - 0.911 = -0.901$$

$$k_4 = (0.2)^2 - \left(1 + 0.2(-0.901)\right) = 0.04 - 0.8198 = -0.7798$$

$$y_1 = 1 + \frac{0.2}{6}\left(-1 + 2(-0.89) + 2(-0.901) + (-0.7798)\right)$$

$$= 1 + \frac{0.2}{6}\left(-1 - 1.78 - 1.802 - 0.7798\right) = 1 + \frac{0.2}{6}(-5.3618)$$

$$= 1 - 0.178727$$

$$\boxed{y(0.2) \approx 0.8213 \quad\text{(RK4)}}$$

**The comparison.**

| method | $y(0.2)$ | absolute error against $0.821269$ |
| :-- | --: | --: |
| exact | 0.821269 | 0 (reference) |
| RK4, $h = 0.2$ | 0.821273 | $0.000004$ |
| RK2 Heun, $h = 0.2$ | 0.824000 | $0.002731$ |
| Euler, $h = 0.2$ | 0.800000 | $0.021269$ |

$$\boxed{\text{RK4 error} \approx 4\times10^{-6}, \quad \text{RK2 error} \approx 2.73\times10^{-3}}$$

> [!tip] The comparison that actually decides the choice
> "RK4 is 670 times more accurate" is true but the wrong comparison, because it
> ignores cost. The right one is **equal cost**: one RK4 step costs four function
> evaluations, which is exactly what two RK2 steps of $h = 0.1$ cost. Those two
> RK2 steps give $y(0.2) = 0.821928$, error $0.000658$, still **160 times** RK4's
> error, for the same number of evaluations.
>
> | equal cost, 4 evaluations | $y(0.2)$ | error |
> | :-- | --: | --: |
> | two RK2 steps, $h = 0.1$ | 0.821928 | 0.000658 |
> | one RK4 step, $h = 0.2$ | 0.821273 | 0.000004 |
>
> RK2's error falls as $h^2$ and RK4's as $h^4$, so the gap **widens** as $h$
> shrinks. Buying accuracy by shrinking $h$ under a second-order method is the
> losing side of that trade, and only changing method wins.

Euler's row is included for a reason: $0.800000$ is the predictor RK2 discards,
and the gap from the exact solution, $0.021269$, is about eight times RK2's own
error. That ratio is the share of the work the corrector is doing, which is a
useful way to say *why* a two-stage method beats Euler by an order of magnitude
rather than a small percentage.

> [!warning] The RK4 table, and the row that must be recomputed
> Every $k_i$ is $f(x, y)$ at the $x$ and $y$ printed **beside it in the same
> row**, not at the start of the step. At step 1, $k_2$ is evaluated at
> $(0.1,\ 0.9)$ and $k_3$ at $(0.1,\ 0.911)$; those two arguments differ by
> $0.011$ because they come from different stages. A table in which $k_2$ and
> $k_3$ share an argument was computed by a modified Euler step, not RK4, and its
> result will be wrong in the fourth digit while still looking reasonable.
>
> The arithmetic itself is the easy part; the ordering is the skill. A reliable
> routine is to write the **evaluation point** next to each $k_i$ as you go,
> so the table cannot be misread later.
>
> **Independent check.** $y(0.2) = 1.64 - e^{-0.2} = 0.821269$ against RK4's
> $0.821273$: four correct decimal places from a **single** step of size
> $0.2$. That is what a fourth-order method promises, and RK2 at the same step
> is three orders of magnitude away.

---

## Class Test 04

**Propositional logic, tautology, equivalence and requirements**

### **Question 1. Let $p$, $q$, $r$ be propositions. Using a complete truth table, establish that $[(p \to q) \land (q \to r)] \to (p \to r)$ is a tautology.**

*[Marks: not printed in source]*

**Write the antecedent and conclusion separately first.** This one line of
notation is what makes the table readable:

$$A = (p \to q) \land (q \to r), \qquad C = p \to r, \qquad E = A \to C$$

**And reduce it, so the table is a formality rather than a struggle.** Using
$P \to Q \equiv \neg P \lor Q$:

$$E = \neg\left[(p \to q) \land (q \to r)\right] \lor (p \to r) = \neg(p \to q) \lor \neg(q \to r) \lor (p \to r)$$

which expands to $\neg(\neg p \lor q) \lor \neg(\neg q \lor r) \lor (\neg p \lor r)$ and
then to

$$E = (p \land \neg q) \lor (q \land \neg r) \lor (\neg p \lor r)$$

For $E$ to be false, **all three** disjuncts must be false. That requires
$p \land \neg q$, which needs $q$ false, and $q \land \neg r$, which needs $q$ true.
A contradiction. So $E$ can never be false, which is exactly what the table
below then shows row by row.

**The complete truth table.**

| $p$ | $q$ | $r$ | $p \to q$ | $q \to r$ | $A = (p \to q) \land (q \to r)$ | $p \to r$ | $E = A \to C$ |
| :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| T | T | T | T | T | T | T | **T** |
| T | T | F | T | F | F | F | **T** |
| T | F | T | F | T | F | T | **T** |
| T | F | F | F | T | F | F | **T** |
| F | T | T | T | T | T | T | **T** |
| F | T | F | T | F | F | T | **T** |
| F | F | T | T | T | T | T | **T** |
| F | F | F | T | T | T | T | **T** |

$$\boxed{E \text{ is true in all 8 rows, so } [(p \to q) \land (q \to r)] \to (p \to r) \text{ is a tautology}}$$

**What the table is actually showing.** The interesting column is $A$. It is false
in rows 2, 3, 4 and 6, and in each of those the implication $A \to C$ is
**vacuously true** regardless of $C$.

That observation collapses the work. The only rows where $E$ *could* fail are
those with $A$ true and $C$ false, and $A$ is true in just four of the eight:
rows 1, 5, 7 and 8. In all four, $p \to q$ and $q \to r$ both hold, and those
together force $p \to r$. So the table settles the question in four rows rather
than eight, and the reduction is visible rather than assumed.

> [!tip] The second route, and it is a genuinely different argument
> This statement *is* **transitivity of implication**, proved by **modus
> ponens** on $p$: from $p$ and $p \to q$ get $q$; from $q$ and $q \to r$ get $r$;
> hence $p \to r$.
>
> The two routes are not restatements of each other. The table checks eight
> cases by exhaustion and gives no insight into *why*. Modus ponens derives the
> conclusion from the premises in two steps and works for any number of
> variables. Agreement between them is a genuinely strong check, and mentioning
> it is what lifts an answer above the minimum.

> [!warning] The row that gets marked wrong, and the cell to read twice
> Row 4, $p = \mathrm{T},\ q = \mathrm{F},\ r = \mathrm{F}$. Two things are true there
> and neither is obvious:
>
> | cell | value | why |
> | :-- | :-: | :-- |
> | $p \to q$ | F | $T \to F$, the ordinary falsifying case |
> | $q \to r$ | **T** | $\neg q \lor r$, true because $q$ is false |
>
> The second is the **vacuously true** implication: true because its antecedent is
> false. It is the single most-missed cell in this topic, and it is the one that
> makes row 4 read as "everything false" at a glance.
>
> So $A$ is F, and $E$ is vacuously T. It is tempting to read the false $A$ as
> making $E$ false. The rule: **$A \to C$ is false only when $A$ is true *and*
> $C$ is false.** A false antecedent can never falsify an implication. Worth
> writing the rule next to the table rather than relying on having remembered it.

### **(a) Translate the requirement into propositional logic.**

*[Marks: not printed in source]*

> *"A student can start the examination if and only if the student is
> authenticated and the examination server is available."*

Let $p$: authenticated, $q$: server available, $r$: can start the examination.

$$\boxed{r \leftrightarrow (p \land q)}$$

**The connective is fixed by one word.** "**if and only if**" is a biconditional,
$\leftrightarrow$, and $p \land q$ is its **whole** right-hand side. So the
requirement says both:

$$(p \land q) \to r \qquad \text{and} \qquad r \to (p \land q)$$

Reading it as the one-way implication $(p \land q) \to r$ states only half the
requirement, and permits a student to start the examination who is not
authenticated. That is precisely what the sentence forbids, so the half-reading
is not a simplification, it is a **different and weaker specification**.

**The complete truth table.**

| $p$ | $q$ | $r$ | $p \land q$ | $r \leftrightarrow (p \land q)$ |
| :-: | :-: | :-: | :-: | :-: |
| T | T | T | T | **T** |
| T | T | F | T | **F** |
| T | F | T | F | **F** |
| T | F | F | F | **T** |
| F | T | T | F | **F** |
| F | T | F | F | **T** |
| F | F | T | F | **F** |
| F | F | F | F | **T** |

$$\boxed{r \leftrightarrow (p \land q) \text{ is true in 4 of 8 rows, so it is contingent}}$$

It is not a tautology: rows 2, 3 and 5 are false. Nor is it a contradiction: rows
1, 4, 6 and 8 are true. A statement permitting four assignments is contingent,
and that is the honest classification. **Contingent is the right answer here, and
the classification matters more than the table**: a requirement that is a
tautology constrains nothing, and one that is a contradiction is unsatisfiable,
so only "contingent" describes a specification that is both restrictive and
implementable.

> [!tip] Reading the four true rows as engineering
> The formula holds when $r$ matches $p \land q$: the student may start exactly
> when both conditions hold. Rows 1 and 4 are the only states where $r$ and
> $p \land q$ agree, and they are what the requirement asserts, nothing more.
>
> | row | $p$ | $q$ | $r$ | what it is |
> | :--: | :-: | :-: | :-: | :-- |
> | 2 | T | T | F | authenticated, server up, **cannot start** |
> | 3 | T | F | T | **starts with the server down** |
> | 5 | F | T | T | **starts without authenticating** |
>
> Rows 3 and 5 are the security failures, and they are exactly the states a
> one-way implication would have permitted. This is why the biconditional is
> written at all, and it is a better justification for the translation than
> pointing at the word "only".

### **(b) Rewrite the resulting expression using only $\neg$, $\lor$, and $\land$.**

*[Marks: not printed in source]*

Start from $r \leftrightarrow (p \land q)$ and replace the biconditional by its
two implications:

$$r \leftrightarrow (p \land q) \equiv \big[(p \land q) \to r\big] \land \big[r \to (p \land q)\big]$$

Replace each implication by $P \to Q \equiv \neg P \lor Q$:

$$\equiv \big[\neg(p \land q) \lor r\big] \land \big[\neg r \lor (p \land q)\big]$$

Apply De Morgan's law $\neg(p \land q) \equiv \neg p \lor \neg q$ to the first
bracket:

$$\boxed{\big[(\neg p \lor \neg q) \lor r\big] \land \big[\neg r \lor (p \land q)\big]}$$

$$\boxed{\equiv (\neg p \lor \neg q \lor r) \land (\neg r \lor p \land q)}$$

which uses only $\neg$, $\lor$ and $\land$, as required.

**Every step with the law named at it**, which is what earns the marks:

$$
\begin{aligned}
r \leftrightarrow (p \land q)
  &\equiv \big[(p \land q) \to r\big] \land \big[r \to (p \land q)\big]
    && \text{biconditional as two implications}\\
  &\equiv \big[\neg(p \land q) \lor r\big] \land \big[\neg r \lor (p \land q)\big]
    && P \to Q \equiv \neg P \lor Q\\
  &\equiv \big[(\neg p \lor \neg q) \lor r\big] \land \big[\neg r \lor (p \land q)\big]
    && \text{De Morgan}\\
  &\equiv (\neg p \lor \neg q \lor r) \land (\neg r \lor p \land q)
    && \text{associativity of } \lor
\end{aligned}
$$

> [!tip] Check by truth table, on all eight rows
> The rewritten formula and $r \leftrightarrow (p \land q)$ are true in exactly
> the same four rows, 1, 4, 6 and 8, and false in the other four. Two formulas
> with the same table **are** the same formula, so the rewrite is correct. Part
> (c) builds that table anyway, which is why the two questions pair up.
>
> There is also a check in the other direction, and it is the more satisfying
> one, because it shows the algebra preserved the *meaning*. The final form
> reads as a requirement rather than as algebra: $\neg p \lor \neg q \lor r$ says
> *something must fail or the student may start*, and $\neg r \lor p \land q$ says
> *if the student starts, both must hold*. Those are the two halves of "if and
> only if", recovered from the rewritten form.

> [!warning] The bracket that must not be dropped
> $(\neg p \lor \neg q \lor r) \land (\neg r \lor p \land q)$ is **not** the same
> as $\neg p \lor \neg q \lor r \land \neg r \lor p \land q$ with the outer
> brackets omitted, because $\lor$ binds more weakly than $\land$. Drop the outer
> conjunction and the formula becomes trivially true wherever only one half is
> satisfied, so the requirement silently weakens to a single implication. The
> outer brackets are not cosmetic; they are the conjunction of two requirements.
>
> One subtlety in the last bracket, stated so it is not misread: $\neg r \lor p
> \land q$ parses as $\neg r \lor (p \land q)$, since $\land$ binds tighter than
> $\lor$. That is what is intended, and it is also what is written, so no extra
> brackets are needed. The form to quote is the bracketed pair.

### **(c) Construct a truth table for the resulting expression.**

*[Marks: not printed in source]*

The resulting expression is
$F = (\neg p \lor \neg q \lor r) \land (\neg r \lor p \land q)$. Build it one
column at a time, which is the only way to be sure each row is right.

| $p$ | $q$ | $r$ | $\neg p$ | $\neg q$ | $\neg r$ | $p \land q$ | $\neg p \lor \neg q \lor r$ | $\neg r \lor p \land q$ | $F$ |
| :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| T | T | T | F | F | F | T | **T** | **T** | **T** |
| T | T | F | F | F | T | T | **F** | **T** | **F** |
| T | F | T | F | T | F | F | **T** | **F** | **F** |
| T | F | F | F | T | T | F | **T** | **T** | **T** |
| F | T | T | T | F | F | F | **T** | **F** | **F** |
| F | T | F | T | F | T | F | **T** | **T** | **T** |
| F | F | T | T | T | F | F | **T** | **F** | **F** |
| F | F | F | T | T | T | F | **T** | **T** | **T** |

$$\boxed{F \text{ is true in rows 1, 4, 6, 8 and false in rows 2, 3, 5, 7}}$$

$$\boxed{F \text{ is contingent: it is not a tautology and not a contradiction}}$$

> [!tip] Reading the table back into the requirement
> The four true rows are the four states the specification permits, and they are
> exactly the rows where $r$ agrees with $p \land q$. The rewrite preserved the
> meaning and not merely the form, which is the thing worth saying about it.
>
> The false rows name the three defects a test plan should look for:
>
> | row | $p$ | $q$ | $r$ | what it is |
> | :--: | :-: | :-: | :-: | :-- |
> | 2 | T | T | F | authenticated, server up, cannot start |
> | 3 | T | F | T | **can start with the server down** |
> | 5 | F | T | T | **can start without authenticating** |
>
> Rows 3 and 5 are the security failures, and they are exactly what a one-way
> implication would have allowed. A requirements table is worth more than its
> truth values for this reason: it turns an abstract formula into a test plan.

> [!warning] The column that catches the commonest slip
> The first bracket, $\neg p \lor \neg q \lor r$, is T in seven of eight rows and
> false only in row 2, where $p = q = \mathrm{T}$ and $r = \mathrm{F}$: both
> conditions hold and the student still cannot start. Row 2 is the only state
> that the first bracket alone forbids.
>
> The second bracket, $\neg r \lor p \land q$, is false in rows 3 and 5, both of
> which have $r = \mathrm{T}$ with at least one condition unmet. So **each
> bracket rules out a different failure, and the statement is the conjunction of
> the two because the requirement has two halves.** Reading it as a disjunction,
> which is the sign error, admits either half being wrong, and a specification
> that tolerates half its own failures is not a specification.

### **(a) Translate all three statements into propositional logic.**

*[Marks: not printed in source]*

Let $p$: the sensor is active, $q$: the controller receives data.

**Statement 1.** "If the sensor is active, then the controller receives data."

$$S_1 = p \to q$$

**Statement 2.** "The controller does not receive data **unless** the sensor is
active."

This is the hard one, and it is where this part is actually tested.

The word "unless" has a precise reading. "$B$ unless $A$" means *if not $A$,
then $B$*, which is $\neg A \to B$, and equivalently $A \lor B$. Here
$A$ = the sensor is active, $p$; $B$ = the controller receives data, $q$. So

$$S_2 = \neg p \to q \quad\equiv\quad p \lor q \quad\equiv\quad q \to p$$

**Statement 3.** "The sensor is active if and only if the controller receives
data."

$$S_3 = p \leftrightarrow q$$

> [!warning] "Unless" is not "if and only if", and the difference is the question
> Read "does not receive data unless the sensor is active" as $q \to p$:
> receiving data *requires* an active sensor. Read instead as $p \to q$ it
> collapses into statement 1, and the second statement then adds nothing.
>
> **That is the diagnostic.** A translation under which one of three statements
> becomes a duplicate of another is almost always the wrong translation, and you
> can tell without evaluating anything.
>
> Notice the result: the three statements are $p \to q$, $q \to p$ and
> $p \leftrightarrow q$, and the first two are already the two halves of the
> third. **Statements 1 and 2 are redundant.** That is not a defect in the
> question, it is the point: the specification states its central requirement
> twice, and a student who notices that has understood what the third statement
> adds, which is nothing.
>
> The related trap is reading "unless" as $p \leftrightarrow q$, which would make
> all three statements a single biconditional and the specification vacuous.

### **(b) Form a single compound proposition by taking the conjunction of the three requirements.**

*[Marks: not printed in source]*

$$C = S_1 \land S_2 \land S_3 = (p \to q) \land (q \to p) \land (p \leftrightarrow q)$$

Replace the biconditional by its two implications:

$$C = (p \to q) \land (q \to p) \land (p \to q) \land (q \to p)$$

and since the first pair already contains both directions,

$$\boxed{C = (p \to q) \land (q \to p)}$$

$$\boxed{C = (\neg p \lor q) \land (\neg q \lor p)}$$

$$\boxed{C = (\neg p \lor q) \land (\neg q \lor p) \equiv (p \land q) \lor (\neg p \land \neg q)}$$

The last line is the distributive form, and it is the useful one: the conjunction
is false in every row where exactly one of $p, q$ is true, and true only where
they agree.

> [!tip] Check by simplification, and say what was thrown away
> Simplifying $C$ gives $(p \land q) \lor (\neg p \land \neg q)$, which is exactly
> $p \leftrightarrow q$. So the conjunction of all three requirements is
> **equivalent to the third alone**, because the third subsumes the first two.
>
> State that plainly rather than presenting four conjuncts and leaving the reader
> to find the redundancy. The specification is satisfiable, and *how* it is
> satisfiable is the content of part (d).

### **(c) Construct the complete truth table from (b).**

*[Marks: not printed in source]*

| $p$ | $q$ | $p \to q$ | $q \to p$ | $S_3 = p \leftrightarrow q$ | $C = S_1 \land S_2 \land S_3$ |
| :-: | :-: | :-: | :-: | :-: | :-: |
| T | T | T | T | T | **T** |
| T | F | F | T | F | **F** |
| F | T | T | F | F | **F** |
| F | F | T | T | T | **T** |

$$\boxed{C \text{ is true in rows 1 and 4, so it is contingent}}$$

$$\boxed{C \text{ is equivalent to } p \leftrightarrow q}$$

**The two true rows are the two consistent states.**

Row 1: the sensor is active **and** the controller receives data. The system is
working as intended.

Row 4: the sensor is inactive **and** the controller receives nothing. The sensor
is off, so nothing should arrive, and nothing does.

Rows 2 and 3 are the failure modes: an active sensor with no data, which is a
dead or disconnected sensor, and an inactive sensor with data, which means data
is arriving from a sensor the system believes is off. The second is the dangerous
one, since the controller would then be acting on data it should treat as
impossible.

> [!tip] The table is also the check on part (b)
> The conjunction column matches the biconditional column in all four rows,
> which is precisely what "the third statement subsumes the first two" means once
> written as a table. If the two columns ever diverged, part (b)'s simplification
> would be wrong, and this table is where you would see it.

### **(d) Establish the truth assignments that satisfy all three requirements simultaneously.**

*[Marks: not printed in source]*

Reading the $C$ column, the conjunction is true in rows 1 and 4 only:

| assignment | $p$ | $q$ | meaning | satisfies all three |
| :-- | :-: | :-: | :-: | :-: |
| 1 | **T** | **T** | sensor active, controller receives data | **yes** |
| 4 | **F** | **F** | sensor inactive, controller receives nothing | **yes** |

$$\boxed{\text{The specification is satisfiable, and the satisfying assignments are exactly } (p,q) = (\mathrm{T},\mathrm{T}) \text{ and } (\mathrm{F},\mathrm{F})}$$

$$\boxed{\text{Equivalently: the requirements hold if and only if } p = q}$$

**That no other assignment works.** Row 2, $p = \mathrm{T}, q = \mathrm{F}$, fails
statement 2, since data does arrive while the sensor is inactive. Row 3,
$p = \mathrm{F}, q = \mathrm{T}$, fails statement 1, since data arrives with no
active sensor. Those are the only rows excluded, and they are excluded by
*different* statements, which is what makes the exclusion complete.

> [!tip] Two routes that avoid the table entirely
> **By cases on $p$.** If $p$ is true, statement 1 forces $q$ true. If $p$ is
> false, statement 2 reads $\neg p \to q$, whose antecedent is true, so it forces
> $q$ false. Either way $q = p$, giving exactly the two assignments above.
>
> **By the simplified form.** Part (b) gave $C \equiv (p \land q) \lor (\neg p
> \land \neg q)$, and $C$ holds precisely when $p$ and $q$ agree. Agreement of
> two propositions is exactly two assignments.
>
> All three routes agree. The answer is a **pair** of assignments rather than a
> single state, and that is the substantive finding: **the specification permits
> the system to be idle.** Nothing in the three requirements forces the sensor to
> be active.

> [!warning] The engineering conclusion, and what the requirement fails to say
> If the system is required to be *monitoring* at all times, then $p$ must be
> true and only row 1 survives: $(p, q) = (\mathrm{T},\mathrm{T})$. But **none of
> the three statements says that.** They constrain the relationship between
> sensor and controller, not the state of the sensor.
>
> This is a real defect in the requirement, and it is the kind of thing a
> specification review exists to find. A fourth statement, "the sensor is
> active", or the operational condition that the system is powered and enabled,
> would close it. An idle state that satisfies every written requirement is not
> a contradiction in the logic; it is a gap in the requirement, and the truth
> table is what makes it visible.
>
> So part (d) has two answers and the second is the better one: *what are the
> satisfying assignments*, and *is that set what the designer intended*.

---

*Every figure here is character identical to the one in `CT_answers_exam_style.md`,
and was derived twice by independent routes. Where the routes disagreed, the
disagreement was settled before the answer was written: `CT-02B Q.2(a)`'s
$y(0.2)$ was wrong in an early draft, with a boxed value that contradicted the
line above it, and was corrected against the closed form*
$y = x^2 - 2x + 2 - e^{-x}$. See `ANSWER_BUILD_PLAN.md` §32.2.*