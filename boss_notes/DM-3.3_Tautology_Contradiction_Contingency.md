[← Previous: DM-3.2 Logical Connectives and Truth Tables](DM-3.2_Logical_Connectives_and_Truth_Tables.md) | [🏠 Index](00_Index.md) | [Next: DM-3.8 Normal Forms and Functional Completeness →](DM-3.8_Normal_Forms_and_Functional_Completeness.md)

---

# DM-3.3: Tautology, Contradiction and Contingency
> **Section:** B (Discrete Mathematics) | **Priority:** 🔴 | **Exam Frequency:** 3/4 DM sources (2023, 2024, CT-04 Q.1)
> **Sources:** Rosen §1.3 (pp. 24–26), Fahad Notes Class-14, Raidah Notes §2.8, Shishir Notes §5

## Why This Topic Matters

Every formula in propositional logic falls into exactly one of three boxes, and the classification decides what you can do with it. Tautologies are what a proof system is built to derive. Contradictions are what make proof by contradiction work. Contingencies are almost every sentence in a real specification. Three marks for 2023 Q.5(c), four for 2024 Q.6(a), and a full eight-row table in CT-04 Q.1.

---

## 📝 Key Definitions

> **Tautology, contradiction, contingency:** "A compound proposition that is always true, no matter what the truth values of the propositional variables that occur in it, is called a **tautology**. A compound proposition that is always false is called a **contradiction**. A compound proposition that is neither a tautology nor a contradiction is called a **contingency**." — Rosen, §1.3, Definition 1 (p. 24)

> **Logical equivalence:** "The compound propositions $p$ and $q$ are called **logically equivalent** if $p \leftrightarrow q$ is a tautology. The notation $p \equiv q$ denotes that $p$ and $q$ are logically equivalent." — Rosen, §1.3, Definition 2 (p. 24)

> **The canonical pair:** "Because $p \vee \neg p$ is always true, it is a tautology. Because $p \wedge \neg p$ is always false, it is a contradiction." — Rosen, §1.3, Example 1 (p. 24)

> **Exhaustive method:** "In general, $2^n$ rows are required if a compound proposition involves $n$ propositional variables." — Rosen, §1.3 (p. 26)

---

## The Three Classes

| Class | True in | Also called | Example |
| :-- | :-- | :-- | :-- |
| **Tautology** | every row | valid formula | $p \lor \neg p$ |
| **Contradiction** | no row | unsatisfiable, inconsistent | $p \land \neg p$ |
| **Contingency** | some rows but not all | satisfiable, non-tautology | $p \lor q$ |

The test is mechanical. Build the table, count the T's in the final column.

| Count of T in last column | Class |
| :-: | :-- |
| All $2^n$ rows | Tautology |
| Zero rows | Contradiction |
| Between 1 and $2^n - 1$ | Contingency |

A formula with no variables is a tautology or a contradiction outright, since there is nothing to vary.

---

## Tautology

True for **every** assignment of its variables. It states a fact that cannot fail.

- **Characteristic:** the final column of the truth table is T throughout.
- **Example:** $p \lor \neg p$. One of $p$ and $\neg p$ must hold, so the disjunction is always true. No values needed.
- **Why it matters:** tautologies are exactly the valid arguments of logic. Every rule of inference in [DM-3.9](DM-3.9_Rules_of_Inference_and_Valid_Arguments.md) is a tautology in disguise.

## Contradiction

False for **every** assignment.

- **Characteristic:** the final column is F throughout. The negation is a tautology.
- **Example:** $p \land \neg p$. A proposition cannot be true and false at once.
- **Why it matters:** this is what makes proof by contradiction work. If assuming $\neg \varphi$ yields a contradiction, then $\varphi$ must be true.

## Contingency

True for **some** assignments and false for **others**.

- **Characteristic:** the final column holds both T and F. It is the only class that depends on the input.
- **Example:** $p \lor q$. True unless both $p$ and $q$ are false.
- **Why it matters:** almost every sentence in an engineering specification is a contingency. A specification that is a tautology constrains nothing, and one that is a contradiction is impossible to build. Only "contingent" describes a requirement that is both restrictive and implementable.

---

## Comparison

| | Tautology | Contradiction | Contingency |
| :-- | :-- | :-- | :-- |
| True for | All assignments | None | Some |
| False for | None | All assignments | Some |
| Negation | Contradiction | Tautology | Contingency |
| Truth table last column | All T | All F | Mixed |
| Satisfiable | Yes | No | Yes |

The negation row is the useful one. To classify a formula without a table, classify its negation instead. If $\neg\varphi$ is a tautology then $\varphi$ is a contradiction, and vice versa.

---

## Two Ways to Decide

Raidah's notes are explicit that both routes must be ready for the exam.

### Route 1, the truth table

Always works, always accepted, and slow for many variables.

**Step 1.** Write one column per variable. Use $2^n$ rows.
**Step 2.** Add a column for every intermediate sub-expression, left to right.
**Step 3.** Read the last column. All T means tautology, all F means contradiction, mixed means contingency.

> [!NOTE] Order of the rows
> For two variables the standard order is TT, TF, FT, FF. For three it is TTT, TTF, TFT, TFF, FTT, FTF, FFT, FFF. Every variable takes T then F, and the **leftmost** variable changes slowest. Getting this wrong flips the table.

### Route 2, algebra with equivalence laws

Faster once you know the laws, and it is the route that scales.

**Step 1.** Replace every connective that is not $\neg, \land, \lor$ using the implication and biconditional equivalences:

$$
p \to q \equiv \neg p \lor q
$$

$$
p \leftrightarrow q \equiv (p \land q) \lor (\neg p \land \neg q)
$$

**Step 2.** Push every negation down to the variables with De Morgan:

$$
\neg(p \land q) \equiv \neg p \lor \neg q, \qquad \neg(p \lor q) \equiv \neg p \land \neg q
$$

**Step 3.** Reduce. If you reach $\mathbf{T}$ it is a tautology, $\mathbf{F}$ a contradiction, and anything else a contingency.

### The law library

| Law | Identity |
| :-- | :-- |
| Identity | $p \land \mathbf{T} \equiv p$, $p \lor \mathbf{F} \equiv p$ |
| Domination | $p \lor \mathbf{T} \equiv \mathbf{T}$, $p \land \mathbf{F} \equiv \mathbf{F}$ |
| Idempotent | $p \lor p \equiv p$, $p \land p \equiv p$ |
| Double negation | $\neg(\neg p) \equiv p$ |
| Commutative | $p \lor q \equiv q \lor p$, $p \land q \equiv q \land p$ |
| Associative | $(p \lor q) \lor r \equiv p \lor (q \lor r)$ and the same for $\land$ |
| Distributive | $p \lor (q \land r) \equiv (p \lor q) \land (p \lor r)$ and the dual |
| De Morgan | $\neg(p \land q) \equiv \neg p \lor \neg q$, $\neg(p \lor q) \equiv \neg p \land \neg q$ |
| Absorption | $p \lor (p \land q) \equiv p$, $p \land (p \lor q) \equiv p$ |
| Negation | $p \lor \neg p \equiv \mathbf{T}$, $p \land \neg p \equiv \mathbf{F}$ |

> [!TIP] Extend De Morgan to any number of terms
> $$
> \neg\left(\bigvee_{j=1}^n p_j\right) \equiv \bigwedge_{j=1}^n \neg p_j
> \quad \text{and} \quad
> \neg\left(\bigwedge_{j=1}^n p_j\right) \equiv \bigvee_{j=1}^n \neg p_j
> $$

---

## Worked Example: Building a Table for Eight Variables' Worth of Rows

The canonical hand-worked proof of a tautology by table, done as a class:

![Hand-worked eight-row truth table showing (p -> (q -> r)) -> ((p -> q) -> (p -> r)) is a tautology, with the final column T in every row](diagrams/dm3_tautology_truth_table_handworked.jpg)

*The last column is T in all eight rows, so the statement is a tautology. This is also transitivity of implication: if $p$ implies $q$ and $q$ implies $r$, then $p$ implies $r$.*

---

## Worked Example (PYQ 2023)

> **Source:** 2023 Q.5(c) [Marks: 02]

**Question.** Show that each of the conditional statements is a tautology by using truth tables: (i) $\neg(p \to q) \to p$, (ii) $p \to (p \lor q)$.

**Answer.**

**(i) $\neg(p \to q) \to p$**

$p \to q$ is F only when $p = T, q = F$. So $\neg(p \to q)$ is T only there.

| $p$ | $q$ | $p \to q$ | $\neg(p \to q)$ | $\neg(p \to q) \to p$ |
| :-: | :-: | :-: | :-: | :-: |
| F | F | T | F | T |
| F | T | T | F | T |
| T | F | F | T | T |
| T | T | T | F | T |

The final column is T in every row.

**Algebraic confirmation.** $\neg(p \to q) = \neg(\neg p \lor q) = p \land \neg q$.
Then $(p \land \neg q) \to p = \neg(p \land \neg q) \lor p = (\neg p \lor q) \lor p = \top$.

$$
\boxed{(i)\ \neg(p \to q) \to p \text{ is a tautology}}
$$

**(ii) $p \to (p \lor q)$**

| $p$ | $q$ | $p \lor q$ | $p \to (p \lor q)$ |
| :-: | :-: | :-: | :-: |
| F | F | F | T |
| F | T | T | T |
| T | F | T | T |
| T | T | T | T |

The final column is T in every row.

**Algebraic confirmation.** $p \to (p \lor q) = \neg p \lor (p \lor q) = (\neg p \lor p) \lor q = \top$.

$$
\boxed{(ii)\ p \to (p \lor q) \text{ is a tautology}}
$$

---

## Worked Example (PYQ 2024)

> **Source:** 2024 Q.6(a) [Marks: 04]

**Question.** Explain the concepts of tautology, contradiction and contingency in propositional logic. Explain their characteristics with example.

**Answer.**

Every propositional formula falls into exactly one of three classes, decided by
its truth value across all assignments.

**1. Tautology.** True for **every** assignment of its variables. It is also called a
valid formula. It states a fact that cannot fail.

- Characteristic: the final column of the truth table is T throughout.
- Example: $p \lor \neg p$. One of $p$ and $\neg p$ must hold, so the disjunction
  is always true. No values needed.

**2. Contradiction.** False for **every** assignment. It is also called an unsatisfiable
formula, or an inconsistent set of conditions.

- Characteristic: the final column is F throughout. The negation is a tautology.
- Example: $p \land \neg p$. A proposition cannot be true and false at once.

**3. Contingency.** True for **some** assignments and false for **others**. It is also
called a satisfiable formula, or a non-tautology.

- Characteristic: the final column holds both T and F. It is the only class that
  depends on the input.
- Example: $p \lor q$. True unless both $p$ and $q$ are false.

**Comparison**

| | Tautology | Contradiction | Contingency |
| :-- | :-- | :-- | :-- |
| True for | All assignments | None | Some |
| False for | None | All assignments | Some |
| Negation | Contradiction | Tautology | Contingency |
| Truth table last column | All T | All F | Mixed |

**Worked example, classifying $A \to (B \lor \neg A)$**

| $A$ | $B$ | $\neg A$ | $B \lor \neg A$ | $A \to (B \lor \neg A)$ |
| :-: | :-: | :-: | :-: | :-: |
| F | F | T | T | T |
| F | T | T | T | T |
| T | F | F | F | F |
| T | T | F | T | T |

The last column holds T, T, F, T, so the formula is a **contingency**.

$$
\boxed{\text{tautology (always T), contradiction (always F), contingency (mixed)}}
$$

---

## 🏆 Golden Questions (Past Exam Archive)

### 🎯 Show that each of the conditional statements is a tautology by using truth tables: (i) $\neg(p \to q) \to p$, (ii) $p \to (p \lor q)$.
> **Appeared:** 2023 Q.5(c) — (02 marks)

**Full Answer:**

A tautology is true on **every** assignment, so the last column of the table must be T in all four rows. There is no partial credit in "show that", so both rows of each table must be filled in; leaving the last column half blank defeats the purpose.

**(i) $\neg(p \to q) \to p$**

$p \to q$ is F only when $p = T, q = F$. So $\neg(p \to q)$ is T only there.

| $p$ | $q$ | $p \to q$ | $\neg(p \to q)$ | $\neg(p \to q) \to p$ |
| :-: | :-: | :-: | :-: | :-: |
| F | F | T | F | T |
| F | T | T | F | T |
| T | F | F | T | T |
| T | T | T | F | T |

The final column is T in every row.

**Algebraic confirmation.** $\neg(p \to q) = \neg(\neg p \lor q) = p \land \neg q$.
Then $(p \land \neg q) \to p = \neg(p \land \neg q) \lor p = (\neg p \lor q) \lor p = \top$.

$$
\boxed{(i)\ \neg(p \to q) \to p \text{ is a tautology}}
$$

**(ii) $p \to (p \lor q)$**

| $p$ | $q$ | $p \lor q$ | $p \to (p \lor q)$ |
| :-: | :-: | :-: | :-: |
| F | F | F | T |
| F | T | T | T |
| T | F | T | T |
| T | T | T | T |

The final column is T in every row.

**Algebraic confirmation.** $p \to (p \lor q) = \neg p \lor (p \lor q) = (\neg p \lor p) \lor q = \top$.

$$
\boxed{(ii)\ p \to (p \lor q) \text{ is a tautology}}
$$

> [!note] Why (i) is the interesting one
> Both are tautologies, but (i) is doing something subtler and worth understanding rather than just tabulating.
>
> (ii) is the weakening rule: if a statement holds, then anything weaker also holds, and $p \lor q$ is weaker than $p$. Two marks for a table.
>
> (i) says something slightly more interesting. If $p \to q$ were false, then $\neg(p \to q)$ would be true, and the statement $p$ must follow. But $\neg(p \to q)$ being true *already means* $p$ is true, since $\neg(p \to q) = p \land \neg q$. So the whole formula reduces to "if $p$ then $p$", dressed up in an implication. That is the general shape of any statement of the form $\neg(p \to q) \to \text{something}$, and it is a common source of exam questions.

---

### 🎯 Explain the concepts of tautology, contradiction and contingency in propositional logic. Explain their characteristics with example.
> **Appeared:** 2024 Q.6(a) — (04 marks)

**Full Answer:**

**The three classifications.** Given a formula, its class is decided by how many rows of its truth table are true.

| Class | True in | Example |
| :-- | :-- | :-- |
| **Tautology** | every row | $p \lor \neg p$ |
| **Contradiction** | no row | $p \land \neg p$ |
| **Contingency** | some rows, not all | $p \land q$ |

The test is therefore mechanical: build the table, count the T's. A formula with no variables is a tautology or a contradiction outright. A formula with $n$ variables is tested over $2^n$ rows.

**Where each class shows up.** Tautologies are the valid arguments of logic, and they are what a proof system is designed to derive. Contradictions are what makes a proof by contradiction work: if assuming $\neg \varphi$ yields a contradiction, then $\varphi$ must be true. Contingencies are what describes anything whose truth depends on facts, which is to say almost every sentence actually used in a specification.

**The five connectives.**

| Connective | Symbol | Reads as | Truth condition |
| :-- | :-: | :-- | :-- |
| Negation | $\neg p$ | "not $p$" | true iff $p$ is false |
| Conjunction | $p \land q$ | "$p$ and $q$" | true iff both are true |
| Disjunction | $p \lor q$ | "$p$ or $q$" | true iff at least one is true |
| Implication | $p \to q$ | "if $p$ then $q$" | false only when $p$ true and $q$ false |
| Biconditional | $p \leftrightarrow q$ | "$p$ if and only if $q$" | true iff the two agree |

**Why the connectives matter.** They are the vocabulary in which every compound proposition is written, and each one identifies a particular kind of valid inference:

- **Negation** enables reductio ad absurdum, and it is what turns an assumption into its opposite.
- **Conjunction** combines hypotheses. A proof from $p \land q$ splits into two proofs, from $p$ and from $q$.
- **Disjunction** enables proof by cases. From $p \lor q$ and a conclusion that follows from each, the conclusion follows.
- **Implication** is the modus ponens engine: from $p$ and $p \to q$ follows $q$. Its truth table, which is true whenever the antecedent is false, is what makes "if pigs fly then I am a queen" a truth rather than a falsehood, and this is the single most counter-intuitive row in the subject.
- **Biconditional** records the two directions of an equivalence, so it lets one substitute one side for the other inside a larger argument.

**Functional completeness.** A set of connectives is functionally complete if every truth function can be built from it. $\{\neg, \land, \lor\}$ is complete, as is $\{\neg, \land\}$, as is $\{\mid\}$ (NAND) alone. The reason NAND alone suffices is

$$
\neg p \equiv p \mid p, \qquad p \land q \equiv (p \mid q) \mid (p \mid q)
$$

and every other connective follows from those two. This is why a whole computer processor can be built out of one gate type, and why the connectives are a practical engineering matter rather than only a logical one.

$$
\boxed{\text{tautology (always T), contradiction (always F), contingency (mixed)}}
$$

> [!note] The row that catches people
> The $p \to q$ row with $p = \mathrm{F}$ and $q = \mathrm{F}$ returns **T**, and so does the row with $p = \mathrm{F}$ and $q = \mathrm{T}$. A conditional makes no claim about what happens when its antecedent is false, so it is vacuously true there. Every confusion about "if pigs fly then I am a queen" being true comes from reading more into the connective than the truth table puts in it.

---

### 🎯 CT-04 Q.1. Let $p$, $q$, $r$ be propositions. Using a complete truth table, establish that $[(p \to q) \land (q \to r)] \to (p \to r)$ is a tautology.
> **Appeared:** CT-04 Q.1 — (marks not printed in source)

**Full Answer:**

**The statement.** Write the antecedent and conclusion separately:

$$
A = (p \to q) \land (q \to r), \qquad C = p \to r, \qquad E = A \to C
$$

Using $P \to Q \equiv \neg P \lor Q$, the whole statement reduces to

$$
E = \neg\left[(p \to q) \land (q \to r)\right] \lor (p \to r) = \neg(p \to q) \lor \neg(q \to r) \lor (p \to r)
$$

which expands to $\neg(\neg p \lor q) \lor \neg(\neg q \lor r) \lor (\neg p \lor r)$ and then to

$$
E = (p \land \neg q) \lor (q \land \neg r) \lor (\neg p \lor r)
$$

For $E$ to be false, all three disjuncts must be false, which requires
$p \land \neg q$, $q \land \neg r$ and $\neg p \lor r$ simultaneously. The first
needs $q$ false and the second needs $q$ true: a contradiction. So $E$ can never
be false, which is the argument the table below makes explicit.

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

$$
\boxed{E \text{ is true in all 8 rows, so } [(p \to q) \land (q \to r)] \to (p \to r) \text{ is a tautology}}
$$

**What the table shows.** The interesting column is $A$. It is false in rows 2, 3,
4 and 6, and in each of those the implication $A \to C$ is **vacuously true**
regardless of $C$. So the eight rows collapse to four that actually need
checking: rows 1, 5, 7 and 8 are the only ones where $A$ is true, and $p \to r$ is
true in all four. The only rows where $E$ could fail are those with $A$ true and
$p \to r$ false, and there are none.

> [!tip] This is transitivity, and the argument form is modus ponens
> The statement *is* transitivity of implication: if $p$ implies $q$ and $q$
> implies $r$, then $p$ implies $r$. A tautology is a theorem of propositional
> logic precisely when some argument form proves it, and this one is proved by
> **modus ponens** on $p$: from $p$ and $p \to q$ get $q$; from $q$ and
> $q \to r$ get $r$; hence $p \to r$.
>
> That is a genuine second route, not a restatement: the truth table checks eight
> cases, while modus ponens derives the conclusion from the premises in two steps
> and is independent of how many variables there are. Agreement between them is
> the check worth quoting.

> [!warning] The row that gets marked wrong, and the cell to read twice
> Row 4, $p = \mathrm{T}, q = \mathrm{F}, r = \mathrm{F}$. Here $p \to q$ is F, since
> the antecedent holds and the conclusion does not. But $q \to r$ is **T**: both
> $q$ and $r$ are false, and $\neg q \lor r$ holds because $q$ is false. That is
> the vacuously true implication, the one that is true because its antecedent is
> false.
>
> So $A$ is F, and $E$ is vacuously T. It is tempting to read the false $A$ as
> making $E$ false, or to read the two F's in the middle as agreeing. The rule is
> that $A \to C$ is false only when $A$ is true **and** $C$ is false, so a false
> antecedent can never falsify an implication.

---

## Exam Variants

| Year | Question | Formula | Class |
| :--- | :--- | :--- | :--- |
| 2023 Q.5(c) | Show two conditionals are tautologies | $\neg(p \to q) \to p$, $p \to (p \lor q)$ | $\boxed{(i)\ \neg(p \to q) \to p \text{ is a tautology}}$ and $\boxed{(ii)\ p \to (p \lor q) \text{ is a tautology}}$ |
| 2024 Q.6(a) | Explain the three concepts with characteristics | definitions plus $A \to (B \lor \neg A)$ | $\boxed{\text{tautology (always T), contradiction (always F), contingency (mixed)}}$ |
| CT-04 Q.1 | Prove $[(p \to q) \land (q \to r)] \to (p \to r)$ | 8-row table | tautology |

---

## ⚡ Exam Tips & Common Mistakes

1. **Fill the entire last column.** "Show that it is a tautology" means every row is T. A table with a blank bottom-right cell is marked wrong even when the other seven rows are right.
2. **Fill every intermediate column too.** Build left to right, one column at a time. Never evaluate the final expression directly in your head while skipping the middle columns.
3. **Use the row order TT, TF, FT, FF and TTT, TTF, ... FFF.** The leftmost variable changes slowest.
4. **A false antecedent never falsifies an implication.** This one sentence prevents the most common error in CT-04 Q.1.
5. **Quote the algebraic confirmation too.** The truth table and the algebraic proof are two independent routes, and Raidah's notes say both are exam-ready. Agreement between them is what lifts the answer.
6. **To classify fast, classify the negation.** If $\neg\varphi$ reduces to $\mathbf{T}$ then $\varphi$ is a contradiction.
7. **Contingency is the most common answer for a real specification.** Do not reach for "tautology" just because the statement sounds obviously true.

## 🔗 Related Topics

- [DM-3.2: Logical Connectives and Truth Tables](DM-3.2_Logical_Connectives_and_Truth_Tables.md) — the tables every classification here is built on
- [DM-3.8: Normal Forms and Functional Completeness](DM-3.8_Normal_Forms_and_Functional_Completeness.md) — where the same equivalences get used to rewrite formulas
- [DM-3.9: Rules of Inference](DM-3.9_Rules_of_Inference_and_Valid_Arguments.md) — each rule is a tautology of the form above
- [DM-3_Lower_a: Validity, Equivalence, Translation](DM-3_Lower_a_Validity_Equivalence_Translation.md) — full equivalence proofs and the classification of formulas as valid, satisfiable or unsatisfiable

---

[← Previous: DM-3.2 Logical Connectives and Truth Tables](DM-3.2_Logical_Connectives_and_Truth_Tables.md) | [🏠 Index](00_Index.md) | [Next: DM-3.8 Normal Forms and Functional Completeness →](DM-3.8_Normal_Forms_and_Functional_Completeness.md)
