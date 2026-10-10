[← Previous: DM-3.1 Propositions and Syntax](DM-3.1_Propositions_and_Syntax.md) | [🏠 Index](00_Index.md) | [Next: DM-3.3 Tautology, Contradiction, Contingency →](DM-3.3_Tautology_Contradiction_Contingency.md)

---

# DM-3.2: Logical Connectives and Truth Tables
> **Section:** B (Discrete Mathematics) | **Priority:** 🔴 | **Exam Frequency:** 4/4 DM sources (2022, 2024, CT-04 Q.2(c), CT-04 Q.3(c))
> **Sources:** Rosen §1.1 (pp. 3–9), Fahad Notes Class-12, Raidah Notes §2.2–2.6, Shishir Notes §2

## Why This Topic Matters

Six symbols and their tables carry this entire topic, and they turn up in every single logic question. The biconditional truth evaluation was set verbatim in 2022 and again in 2024. The CT asked for two full truth tables on the same connectives. Memorise the six tables and you can answer the connective part of almost any Section B paper.

---

## 📝 Key Definitions

> **Negation:** "Let $p$ be a proposition. The *negation of* $p$, denoted by $\neg p$ (also denoted by $\overline{p}$), is the statement 'It is not the case that $p$.' The proposition $\neg p$ is read 'not $p$.' The truth value of the negation of $p$, $\neg p$, is the opposite of the truth value of $p$." — Rosen, §1.1, Definition 1 (p. 3)

> **Conjunction:** "Let $p$ and $q$ be propositions. The *conjunction* of $p$ and $q$, denoted by $p \wedge q$, is the proposition '$p$ and $q$.' The conjunction $p \wedge q$ is true when both $p$ and $q$ are true and is false otherwise." — Rosen, §1.1, Definition 2 (p. 3)

> **Disjunction:** "Let $p$ and $q$ be propositions. The *disjunction* of $p$ and $q$, denoted by $p \vee q$, is the proposition '$p$ or $q$.' The disjunction $p \vee q$ is false when both $p$ and $q$ are false and is true otherwise." — Rosen, §1.1, Definition 3 (p. 3)

> **Exclusive or:** "Let $p$ and $q$ be propositions. The *exclusive or* of $p$ and $q$, denoted by $p \oplus q$, is the proposition that is true when exactly one of $p$ and $q$ is true and is false otherwise." — Rosen, §1.1, Definition 4 (p. 6)

> **Conditional:** "Let $p$ and $q$ be propositions. The *conditional statement* $p \to q$ is the proposition 'if $p$, then $q$.' The conditional statement $p \to q$ is false when $p$ is true and $q$ is false, and true otherwise. In the conditional statement $p \to q$, $p$ is called the *hypothesis* (or *antecedent* or *premise*) and $q$ is called the *conclusion* (or *consequence*)." — Rosen, §1.1, Definition 5 (p. 6)

> **Biconditional:** "Let $p$ and $q$ be propositions. The *biconditional statement* $p \leftrightarrow q$ is the proposition '$p$ if and only if $q$.' The biconditional statement $p \leftrightarrow q$ is true when $p$ and $q$ have the same truth values, and is false otherwise. Biconditional statements are also called *bi-implications*." — Rosen, §1.1, Definition 6 (p. 9)

---

## The Six Connectives at a Glance

| Connective | Symbol | Reads as | Name of compound | True exactly when |
| :-- | :-: | :-- | :-- | :-- |
| Negation | $\neg p$ | "not $p$" | negation | $p$ is false |
| Conjunction | $p \land q$ | "$p$ and $q$" | conjunction | both are true |
| Disjunction | $p \lor q$ | "$p$ or $q$" | disjunction | at least one is true |
| Exclusive or | $p \oplus q$ | "$p$ or $q$, but not both" | exclusive or | exactly one is true |
| Conditional | $p \to q$ | "if $p$ then $q$" | implication | $p$ is false, or $q$ is true |
| Biconditional | $p \leftrightarrow q$ | "$p$ if and only if $q$" | bi-implication | both agree |

The English words "but" and "however" are conjunction. "The sun is shining, but it is raining" is $p \land q$. The contrast is rhetorical, the logic is not.

---

## Negation $\neg p$

The negation flips the truth value. Nothing more.

| $p$ | $\neg p$ |
| :-: | :-: |
| T | F |
| F | T |

**In words.** "Michael's PC runs Linux" negates to "It is not the case that Michael's PC runs Linux", which is more simply "Michael's PC does not run Linux".

**Note.** $\neg\neg p \equiv p$. Two flips return the original.

---

## Conjunction $p \land q$

True only when **both** are true. Otherwise false.

| $p$ | $q$ | $p \land q$ |
| :-: | :-: | :-: |
| T | T | **T** |
| T | F | F |
| F | T | F |
| F | F | F |

One line to remember: **AND is F in three of four rows.** The single T is the all-T row.

---

## Disjunction $p \lor q$

This is the **inclusive** or. True when at least one is true. False only when both are false.

| $p$ | $q$ | $p \lor q$ |
| :-: | :-: | :-: |
| T | T | **T** |
| T | F | **T** |
| F | T | **T** |
| F | F | F |

One line: **OR is F in one of four rows**, and that row is F-F. "Soup or salad comes with an entree" at a restaurant is often exclusive in practice, but written as $p \lor q$ in logic it stays inclusive unless the word "but not both" is added.

---

## Exclusive Or $p \oplus q$

True when **exactly one** is true.

| $p$ | $q$ | $p \oplus q$ |
| :-: | :-: | :-: |
| T | T | F |
| T | F | **T** |
| F | T | **T** |
| F | F | F |

XOR is the negation of the biconditional:

$$
p \oplus q \equiv \neg(p \leftrightarrow q)
$$

"Students who have taken calculus or computer science, **but not both**, can take this class."

---

## Conditional $p \to q$

$p$ is the **hypothesis** (antecedent, premise). $q$ is the **conclusion** (consequent).

| $p$ | $q$ | $p \to q$ |
| :-: | :-: | :-: |
| T | T | **T** |
| T | F | **F** |
| F | T | **T** |
| F | F | **T** |

**The whole rule in one sentence.** A conditional is false **only** when the antecedent is true and the conclusion is false. In all three other rows it is true.

> [!WARNING] The two rows that cause all the damage
> When $p = \mathrm{F}$, the conditional is **T** whether $q$ is T or F. A conditional makes no claim about what happens when its hypothesis fails, so it is **vacuously true** there.
>
> This is why "If pigs fly then I am a queen" is true and not false. Every confusion in this subject traces back to reading more into the connective than the table puts into it.
>
> The contract reading helps. "If I am elected, then I will lower taxes." You are only judged on the pledge if you are elected. If you are not elected, nothing is claimed.

**Ways to say $p \to q$ in English.**

- "if $p$, then $q$"
- "$p$ is sufficient for $q$"
- "$q$ if $p$"
- "$q$ whenever $p$"
- "$q$ is necessary for $p$"
- "$p$ only if $q$"
- "$q$ unless $\neg p$"

The two that confuse everyone are "$p$ only if $q$" and "$q$ unless $\neg p$". Both mean the same thing as "if $p$ then $q$". Note "$p$ only if $q$" puts $p$ first and still means $p \to q$, not $q \to p$.

---

## Converse, Contrapositive and Inverse

Given $p \to q$, three related conditionals have their own names.

| Name | Form | Built by |
| :-- | :-- | :-- |
| **Original** | $p \to q$ | as given |
| **Converse** | $q \to p$ | swap hypothesis and conclusion |
| **Contrapositive** | $\neg q \to \neg p$ | swap and negate both |
| **Inverse** | $\neg p \to \neg q$ | negate both |

**Only the contrapositive is equivalent to the original.**

| $p$ | $q$ | $p \to q$ | $q \to p$ (converse) | $\neg q \to \neg p$ (contrapositive) | $\neg p \to \neg q$ (inverse) |
| :-: | :-: | :-: | :-: | :-: | :-: |
| T | T | T | T | T | T |
| T | F | **F** | **T** | **F** | **T** |
| F | T | T | **F** | T | T |
| F | F | T | T | T | T |
| | | | | **matches** | |

The converse and inverse columns are identical to each other and differ from the original on the T-F row. So:

$$
p \to q \equiv \neg q \to \neg p
$$

$$
q \to p \equiv \neg p \to \neg q
$$

> [!NOTE] "One of the most common logical errors is to assume that the converse or the inverse of a conditional statement is equivalent to this conditional statement." — Rosen, §1.1 (p. 8)

---

## Biconditional $p \leftrightarrow q$

True when the two sides have the **same** truth value.

| $p$ | $q$ | $p \leftrightarrow q$ |
| :-: | :-: | :-: |
| T | T | **T** |
| T | F | F |
| F | T | F |
| F | F | **T** |

It is exactly the conjunction of the two conditionals:

$$
P \leftrightarrow Q \equiv (P \to Q) \land (Q \to P)
$$

And it is written from three other angles:

$$
p \leftrightarrow q \equiv \neg p \leftrightarrow \neg q \equiv (p \land q) \lor (\neg p \land \neg q)
$$

**Ways to say it.** "$p$ is necessary and sufficient for $q$", "if $p$ then $q$, and conversely", "$p$ iff $q$".

> [!WARNING] Two false statements make a TRUE biconditional
> The biconditional asserts that the two sides have the **same** truth value. It does not assert that either is true. "False if and only if false" is true. "True if and only if false" is false.
>
> This single point is the whole of 2022 Q.6(b) and 2024 Q.7(b), and it is worth memorising before reading the worked example.

---

## Precedence of Operators

| Operator | Precedence |
| :-: | :-: |
| $\neg$ | 1, strongest |
| $\land$ | 2 |
| $\lor$ | 3 |
| $\to$ | 4 |
| $\leftrightarrow$ | 5, weakest |

So $\neg p \land q$ means $(\neg p) \land q$, and $p \lor q \to r$ means $(p \lor q) \to r$. Write the brackets anyway.

---

## Worked Example (PYQ 2022, 2024)

> **Source:** 2022 Q.6(b), 2024 Q.7(b) [Marks: 04]

**Question.** Determine whether the biconditionals are true or false: (i) $2 + 2 = 4$ if and only if $1 + 1 = 2$, (ii) $1 + 1 = 2$ if and only if $2 + 3 = 4$, (iii) $1 + 1 = 3$ if and only if monkeys can fly, (iv) $0 > 1$ if and only if $2 > 1$.

**Answer.**

The biconditional $P \leftrightarrow Q$ is true when $P$ and $Q$ have the **same** truth value, that is when both are true or both are false.

$$
P \leftrightarrow Q \equiv (P \to Q) \land (Q \to P)
$$

**(i) $2 + 2 = 4$ if and only if $1 + 1 = 2$**

$2 + 2 = 4$ is true. $1 + 1 = 2$ is true. Same value, so the biconditional holds.

$$
\boxed{\text{(i) TRUE}}
$$

**(ii) $1 + 1 = 2$ if and only if $2 + 3 = 4$**

$1 + 1 = 2$ is true. $2 + 3 = 5$, not $4$, so $2 + 3 = 4$ is false. The values disagree.

$$
\boxed{\text{(ii) FALSE}}
$$

**(iii) $1 + 1 = 3$ if and only if monkeys can fly**

$1 + 1 = 3$ is false. Monkeys cannot fly, so that is false. Both false, so they match.

$$
\boxed{\text{(iii) TRUE}}
$$

**(iv) $0 > 1$ if and only if $2 > 1$**

$0 > 1$ is false. $2 > 1$ is true. The values disagree.

$$
\boxed{\text{(iv) FALSE}}
$$

> [!warning] Part (iii): two false statements make a true biconditional
> Two false statements make a **true** biconditional. It asserts that the two have the same truth value, not that either is true. The answer "false, because $1+1 \ne 3$" misreads the claim.

---

## 🏆 Golden Questions (Past Exam Archive)

### 🎯 Determine whether the biconditionals are true or false: (i) $2 + 2 = 4$ if and only if $1 + 1 = 2$, (ii) $1 + 1 = 2$ if and only if $2 + 3 = 4$, (iii) $1 + 1 = 3$ if and only if monkeys can fly, (iv) $0 > 1$ if and only if $2 > 1$.
> **Appeared:** 2022 Q.6(b), 2024 Q.7(b) — (04 marks)

**Full Answer:**

The biconditional $P \leftrightarrow Q$ is true when $P$ and $Q$ have the **same** truth value, that is when both are true or both are false.

$$
P \leftrightarrow Q \equiv (P \to Q) \land (Q \to P)
$$

**(i) $2 + 2 = 4$ if and only if $1 + 1 = 2$**

$2+2=4$ is true. $1+1=2$ is true. Same value, so the biconditional holds.

$$
\boxed{\text{(i) TRUE}}
$$

**(ii) $1 + 1 = 2$ if and only if $2 + 3 = 4$**

$1+1=2$ is true. $2+3=5$, not $4$, so $2+3=4$ is false. The values disagree.

$$
\boxed{\text{(ii) FALSE}}
$$

**(iii) $1 + 1 = 3$ if and only if monkeys can fly**

$1+1=3$ is false. Monkeys cannot fly, so that is false as well. Both false, so they match.

$$
\boxed{\text{(iii) TRUE}}
$$

**(iv) $0 > 1$ if and only if $2 > 1$**

$0>1$ is false. $2>1$ is true. The values disagree.

$$
\boxed{\text{(iv) FALSE}}
$$

> [!warning] Part (iii) is the whole question: two false statements give a TRUE biconditional
> A biconditional asserts that the two sides have the **same** truth value, not that either of them is true. Answering "false, because $1+1 \ne 3$" misreads the claim entirely.
>
> A quick way to see it: $P \leftrightarrow Q$ is the negation of $P \oplus Q$, the exclusive or. So "false if and only if false" is true, and "true if and only if false" is false. Parts (i) and (iii) are both true-and-true or false-and-false; parts (ii) and (iv) are both mixed.

> [!note] Why this distinction shows up in engineering
> Two sensors that both report "not faulty" do not by themselves certify that the system is healthy: they may share a common cause. Logic built on $\leftrightarrow$ assumes the two statements are independent, and safety arguments that conflate "same truth value" with "both true" fail in exactly the way part (iii) demonstrates.

---

### 🎯 CT-04 Q.2(c). Construct a truth table for the resulting expression.
> **Appeared:** CT-04 Q.2(c) — (marks not printed in source)

**Full Answer:**

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

$$
\boxed{F \text{ is true in rows 1, 4, 6, 8 and false in rows 2, 3, 5, 7}}
$$

$$
\boxed{F \text{ is contingent: it is not a tautology and not a contradiction}}
$$

> [!tip] Reading the table back into the requirement
> The four true rows are the four states the specification permits. They are exactly the rows where $r$ agrees with $p \land q$, which is what $r \leftrightarrow (p \land q)$ asserts, so the rewrite has preserved the meaning and not merely the form.
>
> The false rows name the three defects a test plan should look for:
>
> | row | $p$ | $q$ | $r$ | what it is |
> | :--: | :-: | :-: | :-: | :-- |
> | 2 | T | T | F | authenticated, server up, cannot start |
> | 3 | T | F | T | **can start with the server down** |
> | 5 | F | T | T | **can start without authenticating** |
>
> Rows 3 and 5 are the security failures, and they are exactly what a one-way implication would have allowed.

> [!warning] The column that catches the commonest slip
> The middle column $\neg p \lor \neg q \lor r$ is T in seven of eight rows and false only in row 2, where $p = q = \mathrm{T}$ and $r = \mathrm{F}$: both conditions hold and the student still cannot start. Row 2 is the only state the first bracket alone forbids.
>
> The second bracket $\neg r \lor p \land q$ is false in rows 3 and 5, both of which have $r = \mathrm{T}$ with at least one condition unmet. So each bracket rules out a different failure, and **the statement is the conjunction of the two because the requirement has two halves**. Reading it as a disjunction, which is the sign error, admits either half being wrong.

---

### 🎯 CT-04 Q.3(c). Construct the complete truth table from (b).
> **Appeared:** CT-04 Q.3(c) — (marks not printed in source)

**Full Answer:**

| $p$ | $q$ | $p \to q$ | $q \to p$ | $S_3 = p \leftrightarrow q$ | $C = S_1 \land S_2 \land S_3$ |
| :-: | :-: | :-: | :-: | :-: | :-: |
| T | T | T | T | T | **T** |
| T | F | F | T | F | **F** |
| F | T | T | F | F | **F** |
| F | F | T | T | T | **T** |

$$
\boxed{C \text{ is true in rows 1 and 4, so it is contingent}}
$$

$$
\boxed{C \text{ is equivalent to } p \leftrightarrow q}
$$

> [!tip] The two true rows are the two consistent states
> Row 1: the sensor is active **and** the controller receives data. The system is working as intended.
>
> Row 4: the sensor is inactive **and** the controller receives nothing. The sensor is off, so nothing should arrive, and nothing does.
>
> Rows 2 and 3 are the failure modes: an active sensor with no data, which is a dead or disconnected sensor, and an inactive sensor with data, which means data is arriving from a sensor the system believes is off. The second of those is the dangerous one, since the controller would be acting on data it should treat as impossible.
>
> The table is also the check on part (b): the conjunction column matches the biconditional column in all four rows, which is what "the third statement subsumes the first two" means in a table.

---

## Exam Variants

| Year | Question | Connective under test | Key Answer |
| :--- | :--- | :--- | :--- |
| 2022 Q.6(b) | Four biconditionals, true or false | $\leftrightarrow$ | $\boxed{\text{(i) TRUE}}$, $\boxed{\text{(ii) FALSE}}$, $\boxed{\text{(iii) TRUE}}$, $\boxed{\text{(iv) FALSE}}$ |
| 2024 Q.7(b) | Same four biconditionals | $\leftrightarrow$ | identical |
| CT-04 Q.2(c) | Truth table of $(\neg p \lor \neg q \lor r) \land (\neg r \lor p \land q)$ | $\neg, \lor, \land$ | $\boxed{F \text{ is true in rows 1, 4, 6, 8 and false in rows 2, 3, 5, 7}}$ |
| CT-04 Q.3(c) | Truth table of $(p \to q) \land (q \to p)$ | $\to, \leftrightarrow$ | $\boxed{C \text{ is true in rows 1 and 4, so it is contingent}}$ |

---

## ⚡ Exam Tips & Common Mistakes

1. **The conditional has exactly one false row.** $p \to q$ is false only at $p = \mathrm{T}, q = \mathrm{F}$. Do not argue about cause and effect. Use the table.
2. **Biconditional means "same value", not "both true".** Read part (iii) of the 2022/2024 question twice before writing anything.
3. **$p \lor q$ is inclusive.** It is true at T-T. Only adding "but not both" makes it $\oplus$.
4. **"But" and "however" are $\land$.** Never treat them as a separate connective.
5. **Fill every column of every row.** "Show that" questions get no partial credit for a half-built table. Build left to right, one column at a time, and fill all rows.
6. **Only the contrapositive survives.** $p \to q \equiv \neg q \to \neg p$. The converse and the inverse are not equivalent to the original, and both are fallacies when used as inference rules.
7. **Write the brackets.** $\neg p \land q$ and $\neg(p \land q)$ are different formulas and only one of them is a tautology.

## 🔗 Related Topics

- [DM-3.3: Tautology, Contradiction, Contingency](DM-3.3_Tautology_Contradiction_Contingency.md) — what to do once the table is built
- [DM-3.8: Normal Forms and Functional Completeness](DM-3.8_Normal_Forms_and_Functional_Completeness.md) — rewriting formulas using only some of these connectives
- [DM-3.9: Rules of Inference](DM-3.9_Rules_of_Inference_and_Valid_Arguments.md) — where the conditional table is put to work
- [DM-3_Lower_b: Puzzles, Gates, Extensions](DM-3_Lower_b_Puzzles_Gates_Extensions.md) — building a digital circuit from a compound proposition

---

[← Previous: DM-3.1 Propositions and Syntax](DM-3.1_Propositions_and_Syntax.md) | [🏠 Index](00_Index.md) | [Next: DM-3.3 Tautology, Contradiction, Contingency →](DM-3.3_Tautology_Contradiction_Contingency.md)
