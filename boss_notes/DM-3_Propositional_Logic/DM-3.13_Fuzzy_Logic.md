[← Previous: DM-3.12 Predicates and Quantifiers](DM-3.12_Predicates_and_Quantifiers.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: DM-4.1 Formal Proofs →](../DM-4_Proof_Techniques/DM-4.1_Formal_Proofs.md)

---

# DM-3.13: Fuzzy Logic

> 🟡 **Priority:** Light | **Tested:** 2022 Q.5(b) | **Typical marks:** 4

## What This Is (and Why It Matters)

Classical Boolean logic is rigid and unforgiving: everything is either 100% True ($1$) or 100% False ($0$). But in the physical engineering world, reality is rarely black and white. If you are designing an inverter air conditioner controller, a sensor reading cannot say that the room temperature is strictly "hot" or "cold". The room might be "moderately warm" or "slightly chilly".

Fuzzy logic extends propositional logic by allowing truth values to be any continuous real number in the closed interval $[0, 1]$. A truth value of $0$ means completely false, $1$ means completely true, and a value like $0.7$ means 70% true. In 2022 Q.5(b), a 4-mark question asked students to prove the fuzzy conjunction formula for two opposing real-world statements.

---

## 📝 Key Definitions

> **Fuzzy Logic:** "In fuzzy logic, a proposition has a truth value that is a number between 0 and 1, inclusive. A proposition with a truth value of 0 is completely false, and one with a truth value of 1 is completely true. Values between 0 and 1 indicate varying degrees of truth." -- Rosen, §1.2, Fuzzy Logic (p. 23)
>
> **In simple words:** A continuous logic where statements can be partially true. The truth value is a real number ranging smoothly from $0.0$ to $1.0$.

> **Fuzzy Operations:** "Fuzzy conjunction takes the minimum of the truth values, fuzzy disjunction takes the maximum, and fuzzy negation is $T(\neg P) = 1 - T(P)$." -- Rosen, §1.2 (p. 23); Shishir Notes, §12
>
> **In simple words:** The three basic rules: NOT is calculated by subtracting from 1, AND picks the minimum of the two numbers, and OR picks the maximum.

---

## The Three Core Operations of Fuzzy Logic

Let $T(P) \in [0, 1]$ represent the numerical truth value of proposition $P$:

| Logical Operation | Classical Boolean Logic | Fuzzy Logic Mathematical Definition | Plain English Rule |
|:---|:---:|:---:|:---|
| **Fuzzy Negation (NOT)** | $\neg P$ | $T(\neg P) = 1 - T(P)$ | Invert by subtracting from 1. If truth is 0.8, negation is 0.2. |
| **Fuzzy Conjunction (AND)** | $P \land Q$ | $T(P \land Q) = \min\big(T(P),\, T(Q)\big)$ | Take the smaller (minimum) truth value. |
| **Fuzzy Disjunction (OR)** | $P \lor Q$ | $T(P \lor Q) = \max\big(T(P),\, T(Q)\big)$ | Take the larger (maximum) truth value. |

### Classical Logic as a Special Case
Notice that classical binary logic is simply fuzzy logic restricted to the boundary points $\{0, 1\}$:
- If $T(P) = 1$ and $T(Q) = 0$:
  - $T(P \land Q) = \min(1, 0) = 0$ (Classical AND: $\text{T} \land \text{F} = \text{F}$)
  - $T(P \lor Q) = \max(1, 0) = 1$ (Classical OR: $\text{T} \lor \text{F} = \text{T}$)
  - $T(\neg P) = 1 - 1 = 0$ (Classical NOT: $\neg\text{T} = \text{F}$)

Fuzzy logic generalizes Boolean algebra without breaking any classical boundary results.

---

## 🔧 Worked Example

> **From:** 2022 Q.5(b) -- [Marks: 04]

**The question:** The truth value of the conjunction of two propositions in fuzzy logic is the minimum of the truth values of the statements:
- Statement A: "Fred and John are happy"
- Statement B: "Neither Fred nor John is happy"
Prove the statement.

**Let's solve this step by step:**

### Step 1: Mathematical Setup
In fuzzy logic, truth values lie in the interval $[0, 1]$.
Let:
$$
h = T(\text{Fred is happy}), \qquad j = T(\text{John is happy}), \qquad 0 \le h, j \le 1
$$

### Step 2: Formulate Statement A ("Fred and John are happy")
Statement A is a conjunction of two positive claims:
$$
A = \text{Fred is happy} \land \text{John is happy}
$$
By the definition of fuzzy conjunction:
$$
T(A) = \min(h, j)
$$

### Step 3: Formulate Statement B ("Neither Fred nor John is happy")
"Neither $X$ nor $Y$" means "not $X$ and not $Y$":
$$
B = \neg(\text{Fred is happy}) \land \neg(\text{John is happy})
$$
Using fuzzy negation ($T(\neg P) = 1 - T(P)$):
$$
T(B) = \min(1 - h,\; 1 - j)
$$
Notice that $\min(1 - h, 1 - j) = 1 - \max(h, j)$.

### Step 4: Evaluate the Conjunction $C = A \land B$
By the fundamental definition of fuzzy conjunction, the truth value of the combined proposition $C = A \land B$ is:
$$
T(C) = T(A \land B) = \min\big(T(A),\, T(B)\big)
$$
Substituting our expressions from Steps 2 and 3:
$$
T(C) = \min\Big(\min(h, j),\; \min(1 - h, 1 - j)\Big)
$$
Which combines into:
$$
T(C) = \min(h,\; j,\; 1 - h,\; 1 - j)
$$

This completes the direct algebraic proof of the definition.

---

### Step 5: The Mathematical Bound Property ($T(C) \le 0.5$)
Examiners often look for the qualitative insight behind this result:
Because Statement A and Statement B are contradictories, can their conjunction ever be fully true?

Consider the value of $\min(h, 1 - h)$ for any $h \in [0, 1]$:
- If $h \le 0.5$, then $\min(h, 1 - h) = h \le 0.5$.
- If $h \ge 0.5$, then $1 - h \le 0.5$, so $\min(h, 1 - h) = 1 - h \le 0.5$.

Applying this same logic to both $h$ and $j$:
$$
T(C) = \min\big(\min(h, 1-h),\, \min(j, 1-j)\big) \le 0.5
$$

**Numerical Sweep Table:**

| Fred's Happiness ($h$) | John's Happiness ($j$) | $T(A) = \min(h, j)$ | $T(B) = \min(1-h, 1-j)$ | Conjunction $T(C)$ |
|:---:|:---:|:---:|:---:|:---:|
| $1.0$ | $1.0$ | $1.0$ | $0.0$ | **0.0** |
| $0.0$ | $0.0$ | $0.0$ | $1.0$ | **0.0** |
| $0.8$ | $0.2$ | $0.2$ | $0.2$ | **0.2** |
| $0.3$ | $0.7$ | $0.3$ | $0.3$ | **0.3** |
| **0.5** | **0.5** | **0.5** | **0.5** | **0.5 (Maximum possible)** |

> [!NOTE] What This Means in the Real World
> In classical binary logic, a statement and its contradictory can NEVER both be true: $(A \land \neg A) \equiv \mathbf{F}$ (truth value $0$).
> In fuzzy logic, because opinions and emotions can be divided right down the middle ($h = 0.5$), the conjunction of contradictory statements can achieve a truth value of at most **0.5 ("half-true")**, but never any higher!

---

## ⚡ Quick Review

**The three formulas you must memorize:**
1. NOT: $T(\neg P) = 1 - T(P)$
2. AND: $T(A \land B) = \min(T(A), T(B))$
3. OR: $T(A \lor B) = \max(T(A), T(B))$

**The most common exam mistake:** Multiplying the truth values ($T(A) \times T(B)$) instead of taking the minimum. In standard fuzzy logic as defined by Rosen, conjunction is strictly the $\min$ operation.

**Time estimate in exam:** 4 to 5 minutes to define variables $h$ and $j$ and write out the minimum proof.

---

## 🔗 Connected Topics

- [← Previous: DM-3.12 Predicates and Quantifiers](DM-3.12_Predicates_and_Quantifiers.md) -- Review open sentences and properties.
- [📂 DM-3 Topic Overview](_Topic_Overview.md) -- Revisit the master index for all 13 subtopics in propositional logic.
- [→ Next Section: DM-4.1 Formal Proofs](../DM-4_Proof_Techniques/DM-4.1_Formal_Proofs.md) -- Move to Section B's proof techniques and mathematical induction.

---

[← Previous: DM-3.12 Predicates and Quantifiers](DM-3.12_Predicates_and_Quantifiers.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: DM-4.1 Formal Proofs →](../DM-4_Proof_Techniques/DM-4.1_Formal_Proofs.md)
