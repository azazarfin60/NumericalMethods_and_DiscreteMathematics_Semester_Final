[← Previous: DM-3.1 Propositions](DM-3.1_Propositions.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: DM-3.3 Tautology and Contradiction →](DM-3.3_Tautology_and_Contradiction.md)

---

# DM-3.2: Connectives and Truth Tables

> 🔴 **Priority:** Critical | **Tested:** 4/4 DM sources (2022, 2023, 2024, CT-04) | **Typical marks:** 4

## What This Is (and Why It Matters)

This is the mathematical toolkit of Discrete Mathematics. Just as ordinary arithmetic uses $+$, $-$, $\times$, $\div$ to combine numbers, propositional logic uses six logical connectives to combine factual statements into compound formulas.

Examiners test these operations constantly. In 2022 and 2024, the exact same 4-mark question appeared evaluating whether real-world biconditional statements were true or false. Class tests require building full 8-row and 10-column truth tables step by step. If you understand the exact conditions under which each operator evaluates to true or false, you will never lose marks here.

---

## 📝 Key Definitions

> **Negation:** "Let $p$ be a proposition. The *negation of* $p$, denoted by $\neg p$ (also denoted by $\overline{p}$), is the statement 'It is not the case that $p$.' The proposition $\neg p$ is read 'not $p$.' The truth value of the negation of $p$, $\neg p$, is the opposite of the truth value of $p$." -- Rosen, §1.1, Definition 1 (p. 3)
>
> **In simple words:** A logical inverter. If the input is true, it outputs false; if the input is false, it outputs true.

> **Conjunction:** "Let $p$ and $q$ be propositions. The *conjunction* of $p$ and $q$, denoted by $p \wedge q$, is the proposition '$p$ and $q$.' The conjunction $p \wedge q$ is true when both $p$ and $q$ are true and is false otherwise." -- Rosen, §1.1, Definition 2 (p. 3)
>
> **In simple words:** An AND operation. It is true only when every single component is true. If even one part is false, the whole thing is false.

> **Disjunction:** "Let $p$ and $q$ be propositions. The *disjunction* of $p$ and $q$, denoted by $p \vee q$, is the proposition '$p$ or $q$.' The disjunction $p \vee q$ is false when both $p$ and $q$ are false and is true otherwise." -- Rosen, §1.1, Definition 3 (p. 3)
>
> **In simple words:** An inclusive OR operation. It is true as long as at least one component is true. It is false only when both inputs are false.

> **Exclusive or:** "Let $p$ and $q$ be propositions. The *exclusive or* of $p$ and $q$, denoted by $p \oplus q$, is the proposition that is true when exactly one of $p$ and $q$ is true and is false otherwise." -- Rosen, §1.1, Definition 4 (p. 6)
>
> **In simple words:** An XOR operation. True when the inputs differ (one true and one false), but false if both are true or both are false.

> **Conditional statement:** "Let $p$ and $q$ be propositions. The *conditional statement* $p \to q$ is the proposition 'if $p$, then $q$.' The conditional statement $p \to q$ is false when $p$ is true and $q$ is false, and true otherwise. In the conditional statement $p \to q$, $p$ is called the *hypothesis* (or *antecedent* or *premise*) and $q$ is called the *conclusion* (or *consequence*)." -- Rosen, §1.1, Definition 5 (p. 6)
>
> **In simple words:** An "if-then" promise. It is broken (false) only when you fulfill the condition $p$ but the promised result $q$ fails to happen. If the condition $p$ was never met in the first place, the promise is automatically kept (vacuously true).

> **Biconditional statement:** "Let $p$ and $q$ be propositions. The *biconditional statement* $p \leftrightarrow q$ is the proposition '$p$ if and only if $q$.' The biconditional statement $p \leftrightarrow q$ is true when $p$ and $q$ have the same truth values, and is false otherwise. Biconditional statements are also called *bi-implications*." -- Rosen, §1.1, Definition 6 (p. 9)
>
> **In simple words:** An equivalence checker. True when both sides match: either both true, or both false.

---

## The Six Connectives at a Glance

| Connective | Symbol | Natural Reading | True When | False When |
|:---|:---:|:---|:---|:---|
| **Negation** | $\neg p$ | "not $p$" | $p$ is false | $p$ is true |
| **Conjunction** | $p \land q$ | "$p$ and $q$" | Both $p$ and $q$ are true | At least one input is false |
| **Disjunction** | $p \lor q$ | "$p$ or $q$" (inclusive) | At least one input is true | Both $p$ and $q$ are false |
| **Exclusive OR** | $p \oplus q$ | "$p$ or $q$, but not both" | Exactly one input is true | Inputs have identical values |
| **Conditional** | $p \to q$ | "if $p$, then $q$" | $p$ is false, or $q$ is true | $p$ is true AND $q$ is false |
| **Biconditional** | $p \leftrightarrow q$ | "$p$ if and only if $q$" | $p$ and $q$ agree in value | $p$ and $q$ disagree in value |

> [!NOTE] Natural Language Quirks
> In English, words like "but", "although", "yet", and "however" indicate contrast in rhetoric, but logically they are plain conjunctions ($\land$). 
> For example: "The circuit is powered, but the LED is dark" translates directly to $p \land \neg q$.

---

## Detailed Breakdown of Each Connective

### 1. Negation ($\neg p$)
Negation simply reverses the truth value:

| $p$ | $\neg p$ |
|:---:|:---:|
| $\text{T}$ | $\text{F}$ |
| $\text{F}$ | $\text{T}$ |

Note that double negation cancels out: $\neg(\neg p) \equiv p$.

### 2. Conjunction ($p \land q$)
Think of conjunction like two electrical switches in series. Current flows only if switch 1 AND switch 2 are closed:

| $p$ | $q$ | $p \land q$ |
|:---:|:---:|:---:|
| $\text{T}$ | $\text{T}$ | **T** |
| $\text{T}$ | $\text{F}$ | $\text{F}$ |
| $\text{F}$ | $\text{T}$ | $\text{F}$ |
| $\text{F}$ | $\text{F}$ | $\text{F}$ |

AND is false in three out of four rows. Only $(\text{T}, \text{T})$ yields $\text{T}$.

### 3. Disjunction ($p \lor q$)
Think of disjunction like two electrical switches in parallel. Current flows if switch 1 OR switch 2 (or both) are closed:

| $p$ | $q$ | $p \lor q$ |
|:---:|:---:|:---:|
| $\text{T}$ | $\text{T}$ | **T** |
| $\text{T}$ | $\text{F}$ | **T** |
| $\text{F}$ | $\text{T}$ | **T** |
| $\text{F}$ | $\text{F}$ | $\text{F}$ |

OR is true in three out of four rows. Only $(\text{F}, \text{F})$ yields $\text{F}$.

### 4. Exclusive OR ($p \oplus q$)
XOR outputs true when the two inputs differ:

| $p$ | $q$ | $p \oplus q$ |
|:---:|:---:|:---:|
| $\text{T}$ | $\text{T}$ | $\text{F}$ |
| $\text{T}$ | $\text{F}$ | **T** |
| $\text{F}$ | $\text{T}$ | **T** |
| $\text{F}$ | $\text{F}$ | $\text{F}$ |

Notice that $p \oplus q \equiv \neg(p \leftrightarrow q)$. It is the direct negation of the biconditional.

### 5. Conditional ($p \to q$)
The statement $p$ is the hypothesis (antecedent), and $q$ is the conclusion (consequent).

| $p$ | $q$ | $p \to q$ |
|:---:|:---:|:---:|
| $\text{T}$ | $\text{T}$ | **T** |
| $\text{T}$ | $\text{F}$ | **F** |
| $\text{F}$ | $\text{T}$ | **T** |
| $\text{F}$ | $\text{F}$ | **T** |

> [!WARNING] The Vacuous Truth Trap
> Notice rows 3 and 4 where $p = \text{F}$. Here, the conditional evaluates to $\text{T}$ regardless of whether $q$ is true or false.
> Think of it as a contract: "If you score 80% on the final exam, I will buy you a laptop." 
> If you do not score 80% ($p = \text{F}$), the contract was not violated whether a laptop is bought or not. The promise was not broken, so the statement is vacuously true.
> In mathematical logic: "A false hypothesis implies anything."

**Common English expressions for $p \to q$:**
- "if $p$, then $q$"
- "$p$ is sufficient for $q$"
- "$q$ whenever $p$"
- "$q$ provided that $p$"
- "$p$ only if $q$" (Note: the arrow points toward the "only if" clause!)
- "$q$ unless $\neg p$"

### Converse, Contrapositive, and Inverse
For any conditional statement $p \to q$, three related forms exist:

| Form | Symbolic Representation | How It Is Constructed |
|:---|:---:|:---|
| **Original** | $p \to q$ | The given implication. |
| **Converse** | $q \to p$ | Swap hypothesis and conclusion. |
| **Contrapositive** | $\neg q \to \neg p$ | Swap and negate both. |
| **Inverse** | $\neg p \to \neg q$ | Negate both without swapping. |

Let's compare their truth tables side by side:

| $p$ | $q$ | $p \to q$ | Converse ($q \to p$) | Contrapositive ($\neg q \to \neg p$) | Inverse ($\neg p \to \neg q$) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| $\text{T}$ | $\text{T}$ | **T** | $\text{T}$ | **T** | $\text{T}$ |
| $\text{T}$ | $\text{F}$ | **F** | $\text{T}$ | **F** | $\text{T}$ |
| $\text{F}$ | $\text{T}$ | **T** | $\text{F}$ | **T** | $\text{F}$ |
| $\text{F}$ | $\text{F}$ | **T** | $\text{T}$ | **T** | $\text{T}$ |

Look at the columns carefully:
- The **Contrapositive** matches the original conditional column for column in all 4 rows:
$$
p \to q \equiv \neg q \to \neg p
$$
- The **Converse** and the **Inverse** match each other, but they do NOT match the original conditional:
$$
q \to p \equiv \neg p \to \neg q
$$
Confusing the conditional with its converse is one of the most common logical fallacies in engineering arguments.

### 6. Biconditional ($p \leftrightarrow q$)
A biconditional states that both statements have the exact same truth value:

| $p$ | $q$ | $p \leftrightarrow q$ |
|:---:|:---:|:---:|
| $\text{T}$ | $\text{T}$ | **T** |
| $\text{T}$ | $\text{F}$ | $\text{F}$ |
| $\text{F}$ | $\text{T}$ | $\text{F}$ |
| $\text{F}$ | $\text{F}$ | **T** |

It is equivalent to the two-way implication:
$$
p \leftrightarrow q \equiv (p \to q) \land (q \to p)
$$

> [!WARNING] Two False Statements Make a True Biconditional
> Read row 4 carefully: When $p = \text{F}$ and $q = \text{F}$, $p \leftrightarrow q$ is **TRUE**.
> The biconditional does not claim that either statement is true in reality. It claims that both statements have the *same truth status*. If both are false, their truth values match, making the biconditional true.

---

## Operator Precedence

When brackets are omitted, evaluate operators in this strict order:

| Precedence Level | Operator | Name |
|:---:|:---:|:---|
| 1 (Highest) | $\neg$ | Negation |
| 2 | $\land$ | Conjunction |
| 3 | $\lor$ | Disjunction |
| 4 | $\to$ | Conditional |
| 5 (Lowest) | $\leftrightarrow$ | Biconditional |

For example:
- $\neg p \land q$ means $(\neg p) \land q$, NOT $\neg(p \land q)$.
- $p \lor q \to r$ means $(p \lor q) \to r$.
Always include parentheses in your answers to avoid ambiguity.

---

## 🔧 Worked Example

> **From:** 2022 Q.6(b) / 2024 Q.7(b) -- [Marks: 04]

**The question:** Determine whether the biconditionals are true or false:
(i) $2 + 2 = 4$ if and only if $1 + 1 = 2$
(ii) $1 + 1 = 2$ if and only if $2 + 3 = 4$
(iii) $1 + 1 = 3$ if and only if monkeys can fly
(iv) $0 > 1$ if and only if $2 > 1$

**Let's solve this step by step:**

Recall the rule: $P \leftrightarrow Q$ is true when $P$ and $Q$ have identical truth values (both $\text{T}$ or both $\text{F}$).

1. **Part (i):**
   - Let $P$ be "$2 + 2 = 4$" ($\text{T}$).
   - Let $Q$ be "$1 + 1 = 2$" ($\text{T}$).
   - Both statements are true ($\text{T} \leftrightarrow \text{T}$), so the biconditional is true.
$$
\boxed{\text{(i) TRUE}}
$$

2. **Part (ii):**
   - Let $P$ be "$1 + 1 = 2$" ($\text{T}$).
   - Let $Q$ be "$2 + 3 = 4$" ($\text{F}$, since $2 + 3 = 5$).
   - The truth values disagree ($\text{T} \leftrightarrow \text{F}$), so the biconditional is false.
$$
\boxed{\text{(ii) FALSE}}
$$

3. **Part (iii):**
   - Let $P$ be "$1 + 1 = 3$" ($\text{F}$).
   - Let $Q$ be "monkeys can fly" ($\text{F}$).
   - Both statements are false ($\text{F} \leftrightarrow \text{F}$). Since their truth values match, the biconditional is true.
$$
\boxed{\text{(iii) TRUE}}
$$

4. **Part (iv):**
   - Let $P$ be "$0 > 1$" ($\text{F}$).
   - Let $Q$ be "$2 > 1$" ($\text{T}$).
   - The truth values disagree ($\text{F} \leftrightarrow \text{T}$), so the biconditional is false.
$$
\boxed{\text{(iv) FALSE}}
$$

---

## 🏆 Past Exam Questions

### 2022 Q.6(b) / 2024 Q.7(b): Truth Value of Biconditionals -- [04 marks]

**Question:** Determine whether the biconditionals are true or false:
(i) $2 + 2 = 4$ if and only if $1 + 1 = 2$
(ii) $1 + 1 = 2$ if and only if $2 + 3 = 4$
(iii) $1 + 1 = 3$ if and only if monkeys can fly
(iv) $0 > 1$ if and only if $2 > 1$

**Answer:**
A biconditional statement $P \leftrightarrow Q$ is true if and only if $P$ and $Q$ have identical truth values:

(i) $2 + 2 = 4$ ($\text{T}$), $1 + 1 = 2$ ($\text{T}$). Both sides are true:
$$
\boxed{\text{(i) TRUE}}
$$

(ii) $1 + 1 = 2$ ($\text{T}$), $2 + 3 = 4$ ($\text{F}$). The truth values differ:
$$
\boxed{\text{(ii) FALSE}}
$$

(iii) $1 + 1 = 3$ ($\text{F}$), monkeys can fly ($\text{F}$). Both sides are false, so their truth values match:
$$
\boxed{\text{(iii) TRUE}}
$$

(iv) $0 > 1$ ($\text{F}$), $2 > 1$ ($\text{T}$). The truth values differ:
$$
\boxed{\text{(iv) FALSE}}
$$

---

### CT-04 Q.2(c): Complete Truth Table Construction

**Question:** Construct a truth table for the resulting expression $F = (\neg p \lor \neg q \lor r) \land (\neg r \lor p \land q)$.

**Answer:**
We construct the table column by column for all $2^3 = 8$ combinations:

| $p$ | $q$ | $r$ | $\neg p$ | $\neg q$ | $\neg r$ | $p \land q$ | $\neg p \lor \neg q \lor r$ | $\neg r \lor (p \land q)$ | $F$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| $\text{T}$ | $\text{T}$ | $\text{T}$ | $\text{F}$ | $\text{F}$ | $\text{F}$ | $\text{T}$ | $\text{T}$ | $\text{T}$ | **T** |
| $\text{T}$ | $\text{T}$ | $\text{F}$ | $\text{F}$ | $\text{F}$ | $\text{T}$ | $\text{T}$ | $\text{F}$ | $\text{T}$ | **F** |
| $\text{T}$ | $\text{F}$ | $\text{T}$ | $\text{F}$ | $\text{T}$ | $\text{F}$ | $\text{F}$ | $\text{T}$ | $\text{F}$ | **F** |
| $\text{T}$ | $\text{F}$ | $\text{F}$ | $\text{F}$ | $\text{T}$ | $\text{T}$ | $\text{F}$ | $\text{T}$ | $\text{T}$ | **T** |
| $\text{F}$ | $\text{T}$ | $\text{T}$ | $\text{T}$ | $\text{F}$ | $\text{F}$ | $\text{F}$ | $\text{T}$ | $\text{F}$ | **F** |
| $\text{F}$ | $\text{T}$ | $\text{F}$ | $\text{T}$ | $\text{F}$ | $\text{T}$ | $\text{F}$ | $\text{T}$ | $\text{T}$ | **T** |
| $\text{F}$ | $\text{F}$ | $\text{T}$ | $\text{T}$ | $\text{T}$ | $\text{F}$ | $\text{F}$ | $\text{T}$ | $\text{F}$ | **F** |
| $\text{F}$ | $\text{F}$ | $\text{F}$ | $\text{T}$ | $\text{T}$ | $\text{T}$ | $\text{F}$ | $\text{T}$ | $\text{T}$ | **T** |

$$
\boxed{F \text{ is true in rows 1, 4, 6, 8 and false in rows 2, 3, 5, 7}}
$$

$$
\boxed{F \text{ is contingent: it is not a tautology and not a contradiction}}
$$

---

### CT-04 Q.3(c): Truth Table of Two-Way Implication

**Question:** Construct the complete truth table for the conjunction of implications $C = (p \to q) \land (q \to p)$.

**Answer:**
We construct the truth table for two variables ($2^2 = 4$ rows):

| $p$ | $q$ | $p \to q$ | $q \to p$ | $p \leftrightarrow q$ | $C = (p \to q) \land (q \to p)$ |
|:---:|:---:|:---:|:---:|:---:|:---:|
| $\text{T}$ | $\text{T}$ | $\text{T}$ | $\text{T}$ | $\text{T}$ | **T** |
| $\text{T}$ | $\text{F}$ | $\text{F}$ | $\text{T}$ | $\text{F}$ | **F** |
| $\text{F}$ | $\text{T}$ | $\text{T}$ | $\text{F}$ | $\text{F}$ | **F** |
| $\text{F}$ | $\text{F}$ | $\text{T}$ | $\text{T}$ | $\text{T}$ | **T** |

$$
\boxed{C \text{ is true in rows 1 and 4, so it is contingent}}
$$

$$
\boxed{C \text{ is equivalent to } p \leftrightarrow q}
$$

---

## ⚡ Quick Review

**The connectives in one sentence:** Conjunction ($\land$) requires all true, disjunction ($\lor$) requires at least one true, conditional ($\to$) fails only on $(\text{T}, \text{F})$, and biconditional ($\leftrightarrow$) requires matching values.

**The most common exam mistake:** Forgetting that two false statements make a true biconditional ($\text{F} \leftrightarrow \text{F} \equiv \text{T}$).

**Time estimate in exam:** 4 to 5 minutes to write truth evaluations or construct a 4-row truth table.

---

## 🔗 Connected Topics

- [← Previous: DM-3.1 Propositions](DM-3.1_Propositions.md) -- Review what kinds of sentences feed into these truth tables.
- [→ Next: DM-3.3 Tautology and Contradiction](DM-3.3_Tautology_and_Contradiction.md) -- Learn how to classify compound propositions based on their truth table outputs.
- [DM-3.8: Normal Forms](DM-3.8_Normal_Forms.md) -- See how any truth table can be written as DNF (minterms) or CNF (maxterms).

---

[← Previous: DM-3.1 Propositions](DM-3.1_Propositions.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: DM-3.3 Tautology and Contradiction →](DM-3.3_Tautology_and_Contradiction.md)
