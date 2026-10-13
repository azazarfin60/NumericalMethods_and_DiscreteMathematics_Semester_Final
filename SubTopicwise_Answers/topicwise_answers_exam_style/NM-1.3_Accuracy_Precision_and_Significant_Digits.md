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

Every block below is copied from `../answers_exam_style/`, which is the
only place an answer is authored. A number here is the same number, character
for character, as the one it came from.


### [2017 Q.1(b)]

**Question.** Define the following terms with example: (i) Accuracy (ii) Precision (iii) truncation error (iv) round off error.

**Solution.**

**Accuracy** is the closeness of a computed or measured value to the true
value. Quantitatively it is $1 - |{\text{relative error}}|$, or, as a
percentage, $100(1 - |{\text{relative error}}|)$. Accuracy is an absolute
measure: it does not depend on how far apart repeated readings are.

*Example.* A voltmeter reads $9.8\ \text{V}$ across a true $10\ \text{V}$
supply. The relative error is $-0.02$, so the accuracy is $98\%$.

**Precision** is the closeness of repeated measurements of the same quantity to
one another. It quantifies the spread of the readings, and is expressed as
$100(1 - |{\text{relative spread}}|)$ or through the variance of the readings.
Precision is a relative measure: it says nothing about whether the cluster of
readings is near the true value.

*Example.* Five readings of the same supply give $9.8, 9.9, 9.8, 9.9, 9.8$. The
spread is $0.1$ in $9.8$, about $1\%$, so the readings are $99\%$ precise. They
are still only $98\%$ accurate, because the whole cluster sits low.

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

---

### [2017 Q.3(a)]

**Question.** Sum all the numbers of provided list: $0.1532, 15.45, 0.000354, 305.4, 8.12, 143.3$ where in each of which all the given digits are correct.

**Solution.**

**Approach 1: Direct arithmetic sum.**
Adding the given numbers directly:

$$0.1532 + 15.45 + 0.000354 + 305.4 + 8.12 + 143.3 = 472.423554$$

$$\boxed{472.423554}$$

**Approach 2: Standard textbook procedure for approximate numbers (S.S. Sastry, Ex. 1.7).**
In numerical analysis, the statement *"where in each of which all the given digits are correct"* indicates that each number is an approximate value rounded to its specified decimal places, with an absolute error not exceeding half a unit in the last decimal digit ($\Delta x_i \le 0.5 \times 10^{-m}$).

Following the standard textbook procedure for adding numbers of different accuracies:
1. **Identify numbers with the largest absolute error:**
   The numbers with the fewest decimal places are $305.4$ and $143.3$ (1 decimal place). The absolute error in each is $E_A = 0.05$.
2. **Round all other numbers retaining one additional digit (2 decimal places):**
   - $0.1532 \to 0.15$
   - $15.45 \to 15.45$
   - $0.000354 \to 0.00$
   - $8.12 \to 8.12$
3. **Compute the sum:**
   $$S = 305.4 + 143.3 + 0.15 + 15.45 + 0.00 + 8.12 = 472.42$$
4. **Round off the sum by discarding one digit (to 1 decimal place):**
   $$S \approx 472.4$$
5. **Error bound:**
   The absolute error in the sum is $E_A = 2(0.05) + 4(0.005) = 0.10 + 0.02 = 0.12$. Adding the rounding error ($0.01$) gives total maximum absolute error $0.13$.
   Hence, $S = 472.42 \pm 0.13$ (or $472.4$).

---

[🏠 Subtopic Index](00_Index.md) | [← Prev: NM-1.2 Mathematical Modeling & Engineering Problem Solving](NM-1.2_Mathematical_Modeling_and_Engineering_Problem_Solving.md) | [Next: NM-1.4 Error Types & Sources →](NM-1.4_Error_Types_and_Sources.md)
