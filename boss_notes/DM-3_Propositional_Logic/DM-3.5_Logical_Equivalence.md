[← Previous: DM-3.4 Validity and Satisfiability](DM-3.4_Validity_and_Satisfiability.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: DM-3.6 English to Logic →](DM-3.6_English_to_Logic.md)

---

# DM-3.5: Logical Equivalence

> 🟠 **Priority:** Secondary | **Tested:** 2023 Q.6(a) | **Typical marks:** 3 to 4

## What This Is (and Why It Matters)

Logical equivalence is the mathematical equality of Discrete Mathematics. Just as $\frac{2}{4} = \frac{1}{2}$ in arithmetic, two completely different-looking logical statements can mean the exact same thing in every situation. 

Being able to prove equivalence is essential in digital logic and software verification. For example, if you can prove that a complicated 7-gate circuit is logically equivalent to a simple 3-gate circuit, you can save cost, power, and delay. In 2023 Q.6(a), students were asked to prove that the negation of a biconditional $\neg(p \leftrightarrow q)$ is logically equivalent to negating a single variable $\neg p \leftrightarrow q$.

---

## 📝 Key Definitions

> **Logical Equivalence:** "The compound propositions $p$ and $q$ are called logically equivalent if $p \leftrightarrow q$ is a tautology. The notation $p \equiv q$ denotes that $p$ and $q$ are logically equivalent." -- Rosen, §1.3, Definition 2 (p. 24)
>
> **In simple words:** Two compound propositions are logically equivalent if they output the exact same truth value in every single row of their truth tables. If you connect them with $\leftrightarrow$, the result is a tautology.

---

## Three Routes to Prove Logical Equivalence

When an exam problem asks you to "Show that statement $A$ and statement $B$ are logically equivalent", you can choose from three methods:

| Method | What You Do | When to Use It |
|:---|:---|:---|
| **Route 1: Truth Table** | Build truth tables for both sides and show that the two target columns match row for row. | Best for 2 variables ($2^2 = 4$ rows), or when the paper explicitly says "by truth table". |
| **Route 2: Algebraic Simplification** | Use established Boolean equivalence laws to transform side $A$ into side $B$, or reduce both sides to the same expression. | Best for 3 or more variables, or when the paper explicitly says "algebraically". |
| **Route 3: Canonical Normal Forms** | Convert both sides to canonical DNF (sum of minterms) or canonical CNF (product of maxterms). | Best for complex multi-variable expressions. If the canonical minterms match, the formulas are identical. |

---

## The Biconditional Negation Rules

A common exam pattern involves negating biconditionals. Remember this simple rule:

A biconditional $p \leftrightarrow q$ tests whether two statements agree:
- Both true or both false gives $\text{T}$.
- One true and one false gives $\text{F}$.

When you negate the biconditional $\neg(p \leftrightarrow q)$, you are testing whether they **disagree**. This is the exact definition of Exclusive OR ($p \oplus q$).

Notice what happens when you distribute negations:
1. **Negating an odd number of variables:** Flips agreement into disagreement.
$$
\neg(p \leftrightarrow q) \equiv (\neg p \leftrightarrow q) \equiv (p \leftrightarrow \neg q) \equiv p \oplus q
$$
2. **Negating an even number of variables:** Preserves agreement.
$$
(p \leftrightarrow q) \equiv (\neg p \leftrightarrow \neg q)
$$

---

## 🔧 Worked Example

> **From:** 2023 Q.6(a) -- [Marks: 03]

**The question:** Show that $\neg(p \leftrightarrow q)$ and $\neg p \leftrightarrow q$ are logically equivalent.

**Let's solve this step by step:**

We will provide both the truth table proof and the algebraic proof so you are prepared for whatever the examiner specifies.

### Route 1: Truth Table Proof

We construct the truth table for the 2 variables $p$ and $q$ ($2^2 = 4$ rows):

| $p$ | $q$ | $p \leftrightarrow q$ | $\neg(p \leftrightarrow q)$ | $\neg p$ | $\neg p \leftrightarrow q$ |
|:---:|:---:|:---:|:---:|:---:|:---:|
| $\text{F}$ | $\text{F}$ | $\text{T}$ | **F** | $\text{T}$ | **F** |
| $\text{F}$ | $\text{T}$ | $\text{F}$ | **T** | $\text{T}$ | **T** |
| $\text{T}$ | $\text{F}$ | $\text{F}$ | **T** | $\text{F}$ | **T** |
| $\text{T}$ | $\text{T}$ | $\text{T}$ | **F** | $\text{F}$ | **F** |

Notice the columns for $\neg(p \leftrightarrow q)$ and $\neg p \leftrightarrow q$:
- Row 1 ($F, F$): Both evaluate to $\text{F}$.
- Row 2 ($F, T$): Both evaluate to $\text{T}$.
- Row 3 ($T, F$): Both evaluate to $\text{T}$.
- Row 4 ($T, T$): Both evaluate to $\text{F}$.

Since the computed truth values are identical ($\text{F}, \text{T}, \text{T}, \text{F}$) in all 4 rows, the two propositions are logically equivalent.

$$
\boxed{\neg(p \leftrightarrow q) \equiv (\neg p \leftrightarrow q)}
$$

---

### Route 2: Algebraic Proof

Let's rewrite both sides into Disjunctive Normal Form (sum of products):

**Left-Hand Side (LHS):**
$$
\neg(p \leftrightarrow q) \equiv \neg \big[(p \to q) \land (q \to p)\big]
$$
Apply De Morgan's Law:
$$
\equiv \neg(p \to q) \lor \neg(q \to p)
$$
Using the conditional negation rule $\neg(A \to B) \equiv A \land \neg B$:
$$
\equiv (p \land \neg q) \lor (\neg p \land q)
$$
This is the standard form of Exclusive OR ($p \oplus q$).

**Right-Hand Side (RHS):**
Expand $\neg p \leftrightarrow q$ as two implications:
$$
\neg p \leftrightarrow q \equiv (\neg p \to q) \land (q \to \neg p)
$$
Using the implication law $A \to B \equiv \neg A \lor B$:
$$
\equiv (\neg(\neg p) \lor q) \land (\neg q \lor \neg p) \equiv (p \lor q) \land (\neg p \lor \neg q)
$$
Distribute the terms:
$$
\equiv \big[(p \lor q) \land \neg p\big] \lor \big[(p \lor q) \land \neg q\big]
$$
$$
\equiv \big[(p \land \neg p) \lor (q \land \neg p)\big] \lor \big[(p \land \neg q) \lor (q \land \neg q)\big]
$$
Since $p \land \neg p \equiv \mathbf{F}$ and $q \land \neg q \equiv \mathbf{F}$:
$$
\equiv \big[\mathbf{F} \lor (\neg p \land q)\big] \lor \big[(p \land \neg q) \lor \mathbf{F}\big]
$$
$$
\equiv (\neg p \land q) \lor (p \land \neg q) \equiv (p \land \neg q) \lor (\neg p \land q)
$$

Both the LHS and the RHS reduce to the exact same formula: $(p \land \neg q) \lor (\neg p \land q)$.
Therefore, the equivalence is proven algebraically.

---

## 🏆 Past Exam Questions

### 2023 Q.6(a): Prove $\neg(p \leftrightarrow q) \equiv (\neg p \leftrightarrow q)$ -- [03 marks]

**Question:** Show that $\neg(p \leftrightarrow q)$ and $\neg p \leftrightarrow q$ are logically equivalent.

**Answer:**
We construct the truth table comparing both compound expressions:

| $p$ | $q$ | $p \leftrightarrow q$ | $\neg(p \leftrightarrow q)$ | $\neg p$ | $\neg p \leftrightarrow q$ |
|:---:|:---:|:---:|:---:|:---:|:---:|
| $\text{F}$ | $\text{F}$ | $\text{T}$ | **F** | $\text{T}$ | **F** |
| $\text{F}$ | $\text{T}$ | $\text{F}$ | **T** | $\text{T}$ | **T** |
| $\text{T}$ | $\text{F}$ | $\text{F}$ | **T** | $\text{F}$ | **T** |
| $\text{T}$ | $\text{T}$ | $\text{T}$ | **F** | $\text{F}$ | **F** |

Because the truth values of $\neg(p \leftrightarrow q)$ and $\neg p \leftrightarrow q$ are identical in all possible assignments, the two compound propositions are logically equivalent.

$$
\boxed{\neg(p \leftrightarrow q) \equiv (\neg p \leftrightarrow q)}
$$

**Conceptual Intuition:**
The proposition $p \leftrightarrow q$ is true when $p$ and $q$ have the same truth value. Its negation $\neg(p \leftrightarrow q)$ is true when $p$ and $q$ have opposite truth values. Similarly, $\neg p \leftrightarrow q$ tests whether $\neg p$ and $q$ have the same truth value, which occurs precisely when $p$ and $q$ have opposite truth values. Thus, both formulas test for disagreement between $p$ and $q$.

---

## ⚡ Quick Review

**The definition in one sentence:** Two propositions are logically equivalent if and only if they yield identical truth values in every single row of their truth tables.

**The golden shortcut for biconditionals:** Negating one variable of a biconditional is completely equivalent to negating the entire biconditional:
$$
\neg(p \leftrightarrow q) \equiv \neg p \leftrightarrow q \equiv p \leftrightarrow \neg q
$$

**The most common exam mistake:** Forgetting to name the Boolean laws during an algebraic derivation. Always write "[De Morgan]", "[Distributive Law]", or "[Identity]" next to each step.

**Time estimate in exam:** 3 to 4 minutes for a 4-row truth table proof.

---

## 🔗 Connected Topics

- [← Previous: DM-3.4 Validity and Satisfiability](DM-3.4_Validity_and_Satisfiability.md) -- Review what makes a formula satisfiable.
- [→ Next: DM-3.6 English to Logic](DM-3.6_English_to_Logic.md) -- Master the rules of translating natural English phrases into precise logical statements.
- [DM-3.8: Normal Forms](DM-3.8_Normal_Forms.md) -- See how canonical DNF and CNF guarantee a unique algebraic form for any equivalence class.

---

[← Previous: DM-3.4 Validity and Satisfiability](DM-3.4_Validity_and_Satisfiability.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: DM-3.6 English to Logic →](DM-3.6_English_to_Logic.md)
