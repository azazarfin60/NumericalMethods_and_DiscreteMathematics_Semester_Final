---
title: "NM-1.3 · Accuracy, Precision & Significant Digits"
tags:
  - numerical-methods
  - discrete-mathematics
  - topicwise
---



[🏠 Subtopic Index](00_Index.md) | [← Prev: NM-1.2 Mathematical Modeling & Engineering Problem Solving](NM-1.2_Mathematical_Modeling_and_Engineering_Problem_Solving.md) | [Next: NM-1.4 Error Types & Sources →](NM-1.4_Error_Types_and_Sources.md)

---

# NM-1.3 · Accuracy, Precision & Significant Digits

Every block below is copied from `../answers_explanation/`. The reasoning
is written once, in the year-wise file, and is not restated here.


### [2017 Q.1(b)]

**Question.** Define the following terms with example: (i) Accuracy (ii) Precision (iii) truncation error (iv) round off error.

*[Marks: 04]*

**Solution.**

**Accuracy** is the closeness of a computed or measured value to the *true*
value. Quantitatively it is $1 - |{\text{relative error}}|$, or as a percentage
$100(1 - |{\text{relative error}}|)$. Accuracy is an **absolute** measure: it
says nothing about how far apart repeated readings are.

*Example.* A voltmeter reads $9.8\ \text{V}$ across a true $10\ \text{V}$
supply. The relative error is $-0.02$, so the accuracy is $98\%$.

**Precision** is the closeness of repeated measurements of the same quantity to
*one another*. It quantifies the spread of the readings, and is expressed as
$100(1 - |{\text{relative spread}}|)$ or through the variance. Precision is a
**relative** measure: it says nothing about whether the cluster sits near the
true value.

*Example.* Five readings of the same supply give $9.8, 9.9, 9.8, 9.9, 9.8$. The
spread is $0.1$ against a level of $9.8$, about $1\%$, so the readings are
$99\%$ precise. They are still only $98\%$ accurate, because the whole cluster
sits low.

> [!note] The classic picture, and why both examples are in the question
> Draw four targets. The four groups land on the bullseye, off the bullseye but
> tightly grouped, loosely grouped on the bullseye, and loosely grouped off it.
> **Accuracy** is distance from the bullseye; **precision** is how tightly the
> shots cluster. The pair here, "$99\%$ precise and $98\%$ accurate", is the
> second of those four. A repeatability cluster that sits $2\%$ off is the
> situation where averaging will not help you, and it is worth recognising on
> sight in the laboratory.

**Truncation error** is the error caused by cutting short an infinite process.
Every method that replaces an infinite series by a finite one, an integral by a
finite sum, or a differential equation by a finite number of steps introduces a
truncation error equal to the discarded remainder.

*Example.* $\sin x$ approximated by $x - x^3/6$ truncates after the cubic term;
the error is $x^5/120$ and it falls as the number of retained terms grows.

**Round-off error** is the error caused by the finite precision of the machine.
Every operation rounds its result to the number of digits available, and the
rounding introduced at each step propagates through the later ones.

*Example.* On a machine holding six significant digits, $1/3$ is stored as
$0.333333$. Adding it three times gives $0.999999$, not $1$, and the $10^{-6}$
shortfall is round-off error.

> [!warning] The pair that students merge
> Truncation error shrinks when you take more terms, more panels or a smaller
> $h$. Round-off error *grows* when you do any of those, because every extra
> operation is another rounding. They have opposite dependence on the same
> quantity, and the total error is not minimised by working harder. This is the
> point of Q.1(c), which is the demonstration rather than the statement.

---

### [2017 Q.3(a)]

**Question.** Sum all the numbers of provided list: $0.1532, 15.45, 0.000354, 305.4, 8.12, 143.3$ where in each of which all the given digits are correct.

*[Marks: 03]*

**Solution.**

**The sum.**

$$0.1532 + 15.45 + 0.000354 + 305.4 + 8.12 + 143.3 = 472.423554$$

$$\boxed{472.423554}$$

**Two perspectives are important for this question:**

**Perspective 1: Direct arithmetic sum.**
Adding the six numbers directly on a calculator:

$$0.1532 + 15.45 + 0.000354 + 305.4 + 8.12 + 143.3 = 472.423554$$

All six numbers are terminating decimals, and their rational sum is exactly $\frac{236211777}{500000} = 472.423554$. If an examiner intends this as a pure machine-precision addition problem, no rounding is introduced during the addition.

**Perspective 2: Standard textbook procedure for approximate numbers (S.S. Sastry, Ex. 1.7).**
This question is adapted directly from **S.S. Sastry's *Introductory Methods of Numerical Analysis* (Section 1.3, Example 1.7)**. In numerical methods, the phrase *"where in each of which all the given digits are correct"* is the standard definition of an approximate number rounded to its given decimal places. The absolute error in any number correct to $m$ decimal places does not exceed $0.5 \times 10^{-m}$.

Sastry establishes the standard 4-step procedure for adding numbers of different absolute accuracies:
1. **Isolate the numbers with the greatest absolute error:**
   Here, $305.4$ and $143.3$ have only 1 decimal place, so their absolute error is $\Delta = 0.05$ each.
2. **Round off all other numbers retaining one digit more than the isolated numbers (i.e., 2 decimal places):**
   - $0.1532 \to 0.15$
   - $15.45 \to 15.45$
   - $0.000354 \to 0.00$
   - $8.12 \to 8.12$
3. **Compute the sum:**
   $$S = 305.4 + 143.3 + 0.15 + 15.45 + 0.00 + 8.12 = 472.42$$
4. **Round off the sum by discarding one digit:**
   $$S \approx 472.4$$

**Absolute error in the sum:**
- Two numbers have absolute error $0.05$ each $\implies 2(0.05) = 0.10$.
- The remaining four rounded numbers each have absolute error $0.005 \implies 4(0.005) = 0.02$.
- Subtotal error: $0.10 + 0.02 = 0.12$.
- Adding the rounding error ($0.01$) gives total error bound $E_A = 0.12 + 0.01 = 0.13$.
Hence, $S = 472.42 \pm 0.13$, or $S \approx 472.4$.

Presenting both the exact decimal sum $472.423554$ and Sastry's textbook approximate-sum procedure ($472.4$) guarantees full marks under any examiner.

---

[🏠 Subtopic Index](00_Index.md) | [← Prev: NM-1.2 Mathematical Modeling & Engineering Problem Solving](NM-1.2_Mathematical_Modeling_and_Engineering_Problem_Solving.md) | [Next: NM-1.4 Error Types & Sources →](NM-1.4_Error_Types_and_Sources.md)
