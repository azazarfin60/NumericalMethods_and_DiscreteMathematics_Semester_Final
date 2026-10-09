---
title: "DM-3.3 · Tautology, Contradiction & Contingency"
tags:
  - numerical-methods
  - discrete-mathematics
  - topicwise
---

# DM-3.3 · Tautology, Contradiction & Contingency

Every block below is copied from `../answers_explanation/`. The reasoning
is written once, in the year-wise file, and is not restated here.


### [2023 Q.5(c)]

**Question.** Show that each of the conditional statements is a tautology by using truth tables: (i) $\neg(p \to q) \to p$, (ii) $p \to (p \lor q)$.

*[Marks: 02, CO: 2]*

**Solution.**

A tautology is true on **every** assignment, so the last column of the table must
be T in all four rows. There is no partial credit in "show that", so both rows of
each table must be filled in; leaving the last column half blank defeats the
purpose.

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
> Both are tautologies, but (i) is doing something subtler and worth understanding
> rather than just tabulating.
>
> (ii) is the weakening rule: if a statement holds, then anything weaker also
> holds, and $p \lor q$ is weaker than $p$. Two marks for a table.
>
> (i) says something slightly more interesting. If $p \to q$ were false, then
> $\neg(p \to q)$ would be true, and the statement $p$ must follow. But
> $\neg(p \to q)$ being true *already means* $p$ is true, since $\neg(p \to q) =
> p \land \neg q$. So the whole formula reduces to "if $p$ then $p$", dressed up
> in an implication. That is the general shape of any statement of the form
> $\neg(p \to q) \to \text{something}$, and it is a common source of exam
> questions.

---

### [2024 Q.6(a)]

**Question.** Explain the concepts of tautology, contradiction and contingency in propositional logic. Explain their characteristics with example.

*[Marks: 04, CO: 2]*

**Solution.**

**The three classifications.** Given a formula, its class is decided by how many
rows of its truth table are true.

| Class | True in | Example |
| :-- | :-- | :-- |
| **Tautology** | every row | $p \lor \neg p$ |
| **Contradiction** | no row | $p \land \neg p$ |
| **Contingency** | some rows, not all | $p \land q$ |

The test is therefore mechanical: build the table, count the T's. A formula with
no variables is a tautology or a contradiction outright. A formula with $n$
variables is tested over $2^n$ rows.

**Where each class shows up.** Tautologies are the valid arguments of logic, and
they are what a proof system is designed to derive. Contradictions are what
makes a proof by contradiction work: if assuming $\neg \varphi$ yields a
contradiction, then $\varphi$ must be true. Contingencies are what describes
anything whose truth depends on facts, which is to say almost every sentence
actually used in a specification.

**The five connectives.**

| Connective | Symbol | Reads as | Truth condition |
| :-- | :-: | :-- | :-- |
| Negation | $\neg p$ | "not $p$" | true iff $p$ is false |
| Conjunction | $p \land q$ | "$p$ and $q$" | true iff both are true |
| Disjunction | $p \lor q$ | "$p$ or $q$" | true iff at least one is true |
| Implication | $p \to q$ | "if $p$ then $q$" | false only when $p$ true and $q$ false |
| Biconditional | $p \leftrightarrow q$ | "$p$ if and only if $q$" | true iff the two agree |

**Why the connectives matter.** They are the vocabulary in which every compound
proposition is written, and each one identifies a particular kind of valid
inference:

- **Negation** enables reductio ad absurdum, and it is what turns an assumption
  into its opposite.
- **Conjunction** combines hypotheses. A proof from $p \land q$ splits into two
  proofs, from $p$ and from $q$.
- **Disjunction** enables proof by cases. From $p \lor q$ and a conclusion that
  follows from each, the conclusion follows.
- **Implication** is the modus ponens engine: from $p$ and $p \to q$ follows $q$.
  Its truth table, which is true whenever the antecedent is false, is what makes
  "if pigs fly then I am a queen" a truth rather than a falsehood, and this is
  the single most counter-intuitive row in the subject.
- **Biconditional** records the two directions of an equivalence, so it lets one
  substitute one side for the other inside a larger argument.

**Functional completeness.** A set of connectives is functionally complete if
every truth function can be built from it. $\{\neg, \land, \lor\}$ is complete,
as is $\{\neg, \land\}$, as is $\{\mid\}$ (NAND) alone. The reason NAND alone
suffices is

$$\neg p \equiv p \mid p, \qquad p \land q \equiv (p \mid q) \mid (p \mid q)$$

and every other connective follows from those two. This is why a whole computer
processor can be built out of one gate type, and why the connectives are a
practical engineering matter rather than only a logical one.

$$\boxed{\text{tautology (always T), contradiction (always F), contingency (mixed)}}$$

> [!note] The row that catches people
> The $p \to q$ row with $p = \mathrm{F}$ and $q = \mathrm{F}$ returns **T**, and so does the
> row with $p = \mathrm{F}$ and $q = \mathrm{T}$. A conditional makes no claim about what
> happens when its antecedent is false, so it is vacuously true there. Every
> confusion about "if pigs fly then I am a queen" being true comes from reading
> more into the connective than the truth table puts in it.

---

**Answered in phase P6, in `../CT_Questions/`.**

- *CT-04 Q.1* is a class-test question. Its answer is in `../CT_Questions/CT_answers_exam_style.md`, with the reasoning in `../CT_Questions/CT_answers_explanation.md`.
