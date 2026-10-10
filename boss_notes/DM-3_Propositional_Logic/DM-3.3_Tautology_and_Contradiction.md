[← Previous: DM-3.2 Connectives and Truth Tables](DM-3.2_Connectives_and_Truth_Tables.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: DM-3.4 Validity and Satisfiability →](DM-3.4_Validity_and_Satisfiability.md)

---

# DM-3.3: Tautology and Contradiction

> 🔴 **Priority:** Critical | **Tested:** 3/4 DM sources (2023, 2024, CT-04) | **Typical marks:** 4

## What This Is (and Why It Matters)

Once you build a compound proposition, you need to classify what kind of beast you are dealing with. In propositional logic, every single formula in existence lands in exactly one of three buckets: it is always true (tautology), always false (contradiction), or true under some conditions and false under others (contingency).

Examiners love this topic because it is objective and straightforward to grade. In 2023 Q.5(c), students had to prove two implication statements were tautologies using truth tables. In 2024 Q.6(a), they asked for definitions, characteristics, and examples for 4 marks. In Class Test 4, a full 8-row table proved the transitivity of implication. If you know how to build the table and confirm the result algebraically, this is an easy source of full marks.

---

## 📝 Key Definitions

> **Tautology:** "A compound proposition that is always true, no matter what the truth values of the propositional variables that occur in it, is called a tautology." -- Rosen, §1.3, Definition 1 (p. 24)
>
> **In simple words:** A statement that cannot fail. It is universally true in every conceivable scenario, like "$p \lor \neg p$" ("either the circuit is powered or it is not powered").

> **Contradiction:** "A compound proposition that is always false is called a contradiction." -- Rosen, §1.3, Definition 1 (p. 24)
>
> **In simple words:** A statement that is impossible. It is false in every single row of its truth table, like "$p \land \neg p$" ("the switch is both closed and open at the same time").

> **Contingency:** "A compound proposition that is neither a tautology nor a contradiction is called a contingency." -- Rosen, §1.3, Definition 1 (p. 24)
>
> **In simple words:** A normal real-world condition. It is true in some situations and false in others, depending on what values the variables take.

> **Logical Equivalence:** "The compound propositions $p$ and $q$ are called logically equivalent if $p \leftrightarrow q$ is a tautology. The notation $p \equiv q$ denotes that $p$ and $q$ are logically equivalent." -- Rosen, §1.3, Definition 2 (p. 24)
>
> **In simple words:** Two expressions that mean the exact same thing in every case. Connecting them with a biconditional produces a tautology.

---

## The Three Classes of Formulas

| Class | Final Truth Table Column | Alternative Technical Term | Canonical Example | Practical Role in Engineering |
|:---|:---:|:---|:---:|:---|
| **Tautology** | All $\text{T}$ ($2^n$ rows) | Valid formula | $p \lor \neg p$ | Represents universal laws of logic and valid inference rules. |
| **Contradiction** | All $\text{F}$ ($2^n$ rows) | Unsatisfiable formula | $p \land \neg p$ | Represents impossible states, system bugs, or conflicting specs. |
| **Contingency** | Mixed ($\text{T}$ and $\text{F}$) | Satisfiable non-tautology | $p \lor q$ | Represents realistic system specifications and operational conditions. |

```text
                           All Compound Propositions
                                       |
                +----------------------+----------------------+
                |                                             |
           Tautology                                    Satisfiable
     (True in ALL rows)                          (True in >= 1 row)
                |                                             |
                v                               +-------------+-------------+
         Valid Formula                          |                           |
                                           Contingency                  Tautology
                                        (Mixed T and F)             (Subset of Sat)
                                                |
                                                v
                                        Contradiction
                                     (False in ALL rows)
```

> [!NOTE] Negation Relationship
> The negation of a tautology is always a contradiction, and the negation of a contradiction is always a tautology:
> $$
> \neg(\text{Tautology}) \equiv \text{Contradiction}, \qquad \neg(\text{Contradiction}) \equiv \text{Tautology}
> $$
> The negation of a contingency is always another contingency.

---

## How to Prove a Statement is a Tautology

You have two reliable paths. In the exam, use Route 1 if the question specifies "using truth tables". If not specified, Route 2 is faster and shows deeper mathematical skill.

### Route 1: The Truth Table Method
1. Write down the $n$ propositional variables in standard binary order (for 2 variables: $\text{TT}, \text{TF}, \text{FT}, \text{FF}$; for 3 variables: $\text{TTT}, \dots, \text{FFF}$).
2. Create intermediate columns for each sub-expression from inside brackets outward.
3. Evaluate the final compound column.
4. Conclude explicitly: If every row in the final column is $\text{T}$, state: "Since the final column contains $\text{T}$ in all $2^n$ rows, the statement is a tautology."

![Hand-worked eight-row truth table showing (p -> (q -> r)) -> ((p -> q) -> (p -> r)) is a tautology, with the final column T in every row](../diagrams/dm3_tautology_truth_table_handworked.jpg)

### Route 2: Algebraic Equivalence Laws
Start from the formula and simplify using standard equivalence laws until it reduces to $\mathbf{T}$ (tautology) or $\mathbf{F}$ (contradiction).

### Core Law Library to Memorize

| Equivalence Law | Mathematical Identity |
|:---|:---|
| **Identity Laws** | $p \land \mathbf{T} \equiv p$, $\quad p \lor \mathbf{F} \equiv p$ |
| **Domination Laws** | $p \lor \mathbf{T} \equiv \mathbf{T}$, $\quad p \land \mathbf{F} \equiv \mathbf{F}$ |
| **Idempotent Laws** | $p \lor p \equiv p$, $\quad p \land p \equiv p$ |
| **Double Negation** | $\neg(\neg p) \equiv p$ |
| **Commutative Laws** | $p \lor q \equiv q \lor p$, $\quad p \land q \equiv q \land p$ |
| **Associative Laws** | $(p \lor q) \lor r \equiv p \lor (q \lor r)$, $\quad (p \land q) \land r \equiv p \land (q \land r)$ |
| **Distributive Laws** | $p \lor (q \land r) \equiv (p \lor q) \land (p \lor r)$, $\quad p \land (q \lor r) \equiv (p \land q) \lor (p \land r)$ |
| **De Morgan's Laws** | $\neg(p \land q) \equiv \neg p \lor \neg q$, $\quad \neg(p \lor q) \equiv \neg p \land \neg q$ |
| **Absorption Laws** | $p \lor (p \land q) \equiv p$, $\quad p \land (p \lor q) \equiv p$ |
| **Negation Laws** | $p \lor \neg p \equiv \mathbf{T}$, $\quad p \land \neg p \equiv \mathbf{F}$ |
| **Implication Law** | $p \to q \equiv \neg p \lor q$ |
| **Biconditional Law**| $p \leftrightarrow q \equiv (p \to q) \land (q \to p) \equiv (\neg p \lor q) \land (\neg q \lor p)$ |

---

## 🔧 Worked Example

> **From:** 2023 Q.5(c) -- [Marks: 02]

**The question:** Show that each of the conditional statements is a tautology by using truth tables:
(i) $\neg(p \to q) \to p$
(ii) $p \to (p \lor q)$

**Let's solve this step by step:**

### Part (i): Prove $\neg(p \to q) \to p$ is a tautology

**Step 1: Truth table construction**
We know $p \to q$ is false only when $p = \text{T}$ and $q = \text{F}$. Therefore, $\neg(p \to q)$ is true only in that row.

| $p$ | $q$ | $p \to q$ | $\neg(p \to q)$ | $\neg(p \to q) \to p$ |
|:---:|:---:|:---:|:---:|:---:|
| $\text{F}$ | $\text{F}$ | $\text{T}$ | $\text{F}$ | **T** |
| $\text{F}$ | $\text{T}$ | $\text{T}$ | $\text{F}$ | **T** |
| $\text{T}$ | $\text{F}$ | $\text{F}$ | $\text{T}$ | **T** |
| $\text{T}$ | $\text{T}$ | $\text{T}$ | $\text{F}$ | **T** |

The final column is $\text{T}$ in all four rows.

**Step 2: Algebraic verification**
$$
\neg(p \to q) \to p \equiv \neg(\neg p \lor q) \to p \equiv (p \land \neg q) \to p
$$
Rewriting the implication $A \to B \equiv \neg A \lor B$:
$$
\neg(p \land \neg q) \lor p \equiv (\neg p \lor q) \lor p \equiv (\neg p \lor p) \lor q \equiv \mathbf{T} \lor q \equiv \mathbf{T}
$$

$$
\boxed{(i)\ \neg(p \to q) \to p \text{ is a tautology}}
$$

---

### Part (ii): Prove $p \to (p \lor q)$ is a tautology

**Step 1: Truth table construction**

| $p$ | $q$ | $p \lor q$ | $p \to (p \lor q)$ |
|:---:|:---:|:---:|:---:|
| $\text{F}$ | $\text{F}$ | $\text{F}$ | **T** |
| $\text{F}$ | $\text{T}$ | $\text{T}$ | **T** |
| $\text{T}$ | $\text{F}$ | $\text{T}$ | **T** |
| $\text{T}$ | $\text{T}$ | $\text{T}$ | **T** |

The final column is $\text{T}$ in all four rows.

**Step 2: Algebraic verification**
Using $A \to B \equiv \neg A \lor B$:
$$
p \to (p \lor q) \equiv \neg p \lor (p \lor q) \equiv (\neg p \lor p) \lor q \equiv \mathbf{T} \lor q \equiv \mathbf{T}
$$

$$
\boxed{(ii)\ p \to (p \lor q) \text{ is a tautology}}
$$

---

## 🏆 Past Exam Questions

### 2024 Q.6(a): Concepts of Tautology, Contradiction, and Contingency -- [04 marks]

**Question:** Explain the concepts of tautology, contradiction and contingency in propositional logic. Explain their characteristics with example.

**Answer:**
In propositional logic, any compound proposition is classified into one of three fundamental categories based on its truth values across all possible truth assignments:

1. **Tautology:**
   - **Concept:** A compound proposition that evaluates to true for every possible assignment of truth values to its constituent variables.
   - **Characteristics:** The final column of its truth table contains exclusively $\text{T}$ in all $2^n$ rows. It is logically valid and its negation is a contradiction.
   - **Example:** $p \lor \neg p$ (Law of Excluded Middle). In every state, either $p$ holds or $\neg p$ holds.

2. **Contradiction:**
   - **Concept:** A compound proposition that evaluates to false for every possible assignment of truth values to its variables.
   - **Characteristics:** The final column of its truth table contains exclusively $\text{F}$ in all $2^n$ rows. It is unsatisfiable and its negation is a tautology.
   - **Example:** $p \land \neg p$. A proposition and its negation cannot be simultaneously true.

3. **Contingency:**
   - **Concept:** A compound proposition that is neither a tautology nor a contradiction; its truth value depends on the specific assignment of its variables.
   - **Characteristics:** The final column of its truth table contains a mixture of both $\text{T}$ and $\text{F}$.
   - **Example:** $A \to (B \lor \neg A)$.

**Illustrative Classification Table for $A \to (B \lor \neg A)$:**

| $A$ | $B$ | $\neg A$ | $B \lor \neg A$ | $A \to (B \lor \neg A)$ |
|:---:|:---:|:---:|:---:|:---:|
| $\text{F}$ | $\text{F}$ | $\text{T}$ | $\text{T}$ | **T** |
| $\text{F}$ | $\text{T}$ | $\text{T}$ | $\text{T}$ | **T** |
| $\text{T}$ | $\text{F}$ | $\text{F}$ | $\text{F}$ | **F** |
| $\text{T}$ | $\text{T}$ | $\text{F}$ | $\text{T}$ | **T** |

Because row 3 evaluates to $\text{F}$ while rows 1, 2, and 4 evaluate to $\text{T}$, the formula is a contingency.

$$
\boxed{\text{tautology (always T), contradiction (always F), contingency (mixed)}}
$$

---

### CT-04 Q.1: Tautology Proof for Hypothetical Syllogism

**Question:** Let $p, q, r$ be propositions. Using a complete truth table, establish that $[(p \to q) \land (q \to r)] \to (p \to r)$ is a tautology.

**Answer:**
Let $A = (p \to q) \land (q \to r)$, $C = p \to r$, and $E = A \to C$.
We evaluate the complete truth table for all $2^3 = 8$ rows:

| $p$ | $q$ | $r$ | $p \to q$ | $q \to r$ | $A = (p \to q) \land (q \to r)$ | $C = p \to r$ | $E = A \to C$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| $\text{T}$ | $\text{T}$ | $\text{T}$ | $\text{T}$ | $\text{T}$ | $\text{T}$ | $\text{T}$ | **T** |
| $\text{T}$ | $\text{T}$ | $\text{F}$ | $\text{T}$ | $\text{F}$ | $\text{F}$ | $\text{F}$ | **T** |
| $\text{T}$ | $\text{F}$ | $\text{T}$ | $\text{F}$ | $\text{T}$ | $\text{F}$ | $\text{T}$ | **T** |
| $\text{T}$ | $\text{F}$ | $\text{F}$ | $\text{F}$ | $\text{T}$ | $\text{F}$ | $\text{F}$ | **T** |
| $\text{F}$ | $\text{T}$ | $\text{T}$ | $\text{T}$ | $\text{T}$ | $\text{T}$ | $\text{T}$ | **T** |
| $\text{F}$ | $\text{T}$ | $\text{F}$ | $\text{T}$ | $\text{F}$ | $\text{F}$ | $\text{T}$ | **T** |
| $\text{F}$ | $\text{F}$ | $\text{T}$ | $\text{T}$ | $\text{T}$ | $\text{T}$ | $\text{T}$ | **T** |
| $\text{F}$ | $\text{F}$ | $\text{F}$ | $\text{T}$ | $\text{T}$ | $\text{T}$ | $\text{T}$ | **T** |

Notice that in rows 2, 3, 4, and 6, the premise $A$ is false, which makes the implication $A \to C$ vacuously true. In rows 1, 5, 7, and 8, the premise $A$ is true, and in every such row $C$ is also true. Thus $E$ evaluates to $\text{T}$ across all 8 rows.

$$
\boxed{E \text{ is true in all 8 rows, so } [(p \to q) \land (q \to r)] \to (p \to r) \text{ is a tautology}}
$$

---

## ⚡ Quick Review

**The three classes in one sentence:** A tautology is always true, a contradiction is always false, and a contingency depends on the input values.

**The quick classification trick:** To test if a formula is a contradiction, negate it and check if the negation reduces to $\mathbf{T}$ (tautology).

**The most common exam mistake:** Leaving blank cells in intermediate truth table columns. Examiners check your step-by-step evaluation columns, not just the final verdict.

**Time estimate in exam:** 4 to 6 minutes for an 8-row truth table proof.

---

## 🔗 Connected Topics

- [← Previous: DM-3.2 Connectives and Truth Tables](DM-3.2_Connectives_and_Truth_Tables.md) -- Review the individual truth tables for $\to$, $\land$, and $\lor$.
- [→ Next: DM-3.4 Validity and Satisfiability](DM-3.4_Validity_and_Satisfiability.md) -- Discover how tautologies relate to valid and satisfiable formulas.
- [DM-3.9: Rules of Inference](DM-3.9_Rules_of_Inference.md) -- See how every valid rule of inference is built directly from a tautology.

---

[← Previous: DM-3.2 Connectives and Truth Tables](DM-3.2_Connectives_and_Truth_Tables.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: DM-3.4 Validity and Satisfiability →](DM-3.4_Validity_and_Satisfiability.md)
