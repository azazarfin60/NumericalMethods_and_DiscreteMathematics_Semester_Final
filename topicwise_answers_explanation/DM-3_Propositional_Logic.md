---
title: "DM-3 · Propositional Logic"
tags:
  - numerical-methods
  - discrete-mathematics
  - topicwise-clusters
---

[🏠 Master Index](00_Index.md) | [← Prev Topic: NM-10 · PDE](NM-10_Partial_Differential_Equations.md) | [Next Topic: DM-5 · Number Theory →](DM-5_Number_Theory.md)

---

# DM-3 · Propositional Logic

> **Topic ID:** DM-3  
> **Section:** Section B -- Discrete Mathematics  
> **Exam Weight:** 🔴 High Priority (Tier 1) | 3/3 Years (2022–2024) + CT-04 (100% Frequency) | Typical Weight: 14–21 marks (Questions 5 & 6)  
> **Subtopics Included:** 12 subtopics (DM-3.1 through DM-3.13)  
> **Origin Layer:** Authored in `../answers_explanation/`. All numerical results and boxed equations match character-for-character.

---

## 📑 Subtopics Covered in this Cluster

| Subtopic ID | Subtopic Title | Priority | Exam Frequency | Section Navigation |
|:---|:---|:---:|:---:|:---|
| **DM-3.1** | Propositions & Syntax | 🔴 | 2022, 2024 | [Jump to DM-3.1](#dm-31) |
| **DM-3.2** | Logical Connectives & Truth Tables | 🔴 | 2022, 2023, 2024, CT-04 | [Jump to DM-3.2](#dm-32) |
| **DM-3.3** | Tautology, Contradiction & Contingency | 🔴 | 2023, 2024, CT-04 | [Jump to DM-3.3](#dm-33) |
| **DM-3.4** | Valid, Satisfiable & Unsatisfiable Formulas | 🟠 | 2024, CT-04 | [Jump to DM-3.4](#dm-34) |
| **DM-3.5** | Logical Equivalence | 🟠 | 2023 | [Jump to DM-3.5](#dm-35) |
| **DM-3.6** | Translation: English → Logic | 🟠 | 2024, CT-04 | [Jump to DM-3.6](#dm-36) |
| **DM-3.7** | System Specification & Consistency | 🟠 | 2024, CT-04 | [Jump to DM-3.7](#dm-37) |
| **DM-3.8** | Normal Forms & Functional Completeness | 🔴 | 2022, 2024, CT-04 | [Jump to DM-3.8](#dm-38) |
| **DM-3.9** | Rules of Inference & Valid Arguments | 🔴 | 2022, 2023 | [Jump to DM-3.9](#dm-39) |
| **DM-3.10** | Logic Puzzles | 🟠 | 2022, 2023 | [Jump to DM-3.10](#dm-310) |
| **DM-3.11** | Logic Gates & Digital Circuits | 🟡 | 2023 | [Jump to DM-3.11](#dm-311) |
| **DM-3.13** | Logic Extensions | 🟡 | 2022 | [Jump to DM-3.13](#dm-313) |

---

<a id="dm-31"></a><a id="dm-3.1"></a>
## DM-3.1 · Propositions & Syntax

### [2022 Q.5(a)]

**Question.** Explain how proposition differs from traditional sentence. Give some examples.

*[Marks: 03, CO: 2]*

**Solution.**

**Proposition.** A declarative sentence that is **unambiguously either true or
false**, with exactly one truth value. Nothing more is required. It need not be
meaningful, need not be verifiable today, and carries no quantifier.

**Traditional sentence.** Any statement of natural language. The category is
much wider, admitting sentences with no truth value at all.

| Sentence | Proposition? | Reason |
| :-- | :-- | :-- |
| The transistor conducts | **Yes** | true or false |
| $2 + 2 = 4$ | **Yes** | |
| Water boils at $100^{\circ}$C at sea level | **Yes** | a fact, though it needs a reference condition |
| Close the window | No | imperative, a command |
| Is the door open | No | interrogative, a question |
| Please hand me the tool | No | a request |
| $x + 1 > 0$ | No | depends on the unknown $x$ |
| The present king of France is bald | No | presupposes a non-existent referent, so no truth value |
| $1/0 = 3$ | No | meaningless, division by zero |

**The four tests.**

1. **Declarative.** It asserts rather than commands, asks or requests.
2. **Not interrogative.** No question in intent.
3. **Has a truth value.** Exactly one of true or false, with nothing in between.
4. **Meaningful.** Every symbol is defined, so the sentence can be evaluated.

> [!warning] The four rows that trip people up
> "$x + 1 > 0$" fails because $x$ is free, not because it is false. It becomes a
> proposition only once $x$ is bound: "for every real $x$, $x + 1 > 0$".
>
> "The present king of France is bald" fails because it presupposes something
> that does not exist, so the sentence can be neither true nor false. This is a
> different failure from being undecidable in practice; it has no truth value at
> all.
>
> "$1/0 = 3$" fails on meaningfulness. It is not false, it is not an equation
> between numbers.

> [!note] Propositions, compound propositions and predicates are three different things
> A **compound proposition** is built from simple ones using
> $\neg, \land, \lor, \to, \leftrightarrow$.
>
> A **predicate** such as "$x$ is prime" is not a proposition on its own,
> because $x$ is free. Binding it gives one.
>
> Propositional logic can only reason over things with a definite truth value, so
> anything else has to be translated into propositions first. That translation
> step is where most real errors in control logic occur, which is why the
> distinction is worth two marks of care rather than a definition to memorise.

---

### [2024 Q.5(a)]

**Question.** Define propositional logic and explain the difference between a proposition and propositional variable.

*[Marks: 02, CO: 2]*

**Solution.**

**Propositional logic** is the branch of logic that deals with propositions,
which are declarative statements that are either true or false, and with the
connectives that combine them. Unlike first-order logic it does not look inside a
proposition: it treats each one as a single indivisible unit and studies how the
truth values of whole propositions combine.

**A proposition** is a declarative sentence that has a definite truth value.
"Swift is a functional language" is a proposition. So is "The bridge opened."
The two essential requirements are that the sentence is declarative rather than
interrogative or imperative, and that it is unambiguously either true or false.
"Jaffna is a city in the world" is true. "Cairo is the capital of Egypt" is true.
"Are you hungry?" is not a proposition at all, because it is a question and has
no truth value.

**A propositional variable** is a symbol, usually $p, q, r$, that stands for a
proposition. The variable does not have a truth value by itself: it takes the
truth value of the proposition it represents. The propositional variable $p$ in
the formula $p \to q$ is a placeholder; the propositions are the statements
behind $p$ and behind $q$.

**The difference in one sentence.** A proposition is a *statement* with a truth
value; a propositional variable is a *name* for one, whose own truth value
depends on which proposition it names.

| | Proposition | Propositional variable |
| :-- | :-- | :-- |
| What it is | A declarative sentence with a definite truth value | A single letter standing for a proposition |
| Truth value | Has one of its own | Borrows the one it stands for |
| Example | "Cairo is the capital of Egypt" | $p$, standing for that statement |
| Not one | "Close the switch", an imperative with no truth value | |

$$\text{Proposition} = \text{declarative statement with a definite truth value};\ \text{variable} = \text{its symbol}$$

**Why the distinction matters.** It is the reason a truth table can be finite. A
single proposition has two possible truth values, so $n$ propositional variables
need $2^n$ rows to enumerate, which is a finite and complete account. If
propositions were allowed to be compound in arbitrary ways, no finite table
would suffice.

---

<a id="dm-32"></a><a id="dm-3.2"></a>
## DM-3.2 · Logical Connectives & Truth Tables

### [2022 Q.6(b), 2024 Q.7(b)]

**Appeared in:** 2022 Q.6(b), 2024 Q.7(b)

**Question.** Determine whether the biconditionals are true or false: (i) $2 + 2 = 4$ if and only if $1 + 1 = 2$, (ii) $1 + 1 = 2$ if and only if $2 + 3 = 4$, (iii) $1 + 1 = 3$ if and only if monkeys can fly, (iv) $0 > 1$ if and only if $2 > 1$.

*[Marks: 04, CO: 1]*

**Solution.**

The biconditional $P \leftrightarrow Q$ is true when $P$ and $Q$ have the
**same** truth value, that is when both are true or both are false.

$$
P \leftrightarrow Q \equiv (P \to Q) \land (Q \to P)
$$

**(i) $2 + 2 = 4$ if and only if $1 + 1 = 2$**

$2+2=4$ is true. $1+1=2$ is true. Same value, so the biconditional holds.

$$\boxed{\text{(i) TRUE}}$$

**(ii) $1 + 1 = 2$ if and only if $2 + 3 = 4$**

$1+1=2$ is true. $2+3=5$, not $4$, so $2+3=4$ is false. The values disagree.

$$\boxed{\text{(ii) FALSE}}$$

**(iii) $1 + 1 = 3$ if and only if monkeys can fly**

$1+1=3$ is false. Monkeys cannot fly, so that is false as well. Both false, so
they match.

$$\boxed{\text{(iii) TRUE}}$$

**(iv) $0 > 1$ if and only if $2 > 1$**

$0 > 1$ is false. $2 > 1$ is true. The values disagree.

$$\boxed{\text{(iv) FALSE}}$$

> [!warning] Part (iii) is the whole question: two false statements give a TRUE biconditional
> A biconditional asserts that the two sides have the **same** truth value, not
> that either of them is true. Answering "false, because $1+1 \ne 3$" misreads
> the claim entirely.
>
> A quick way to see it: $P \leftrightarrow Q$ is the negation of
> $P \oplus Q$, the exclusive or. So "false if and only if false" is true, and
> "true if and only if false" is false. Parts (i) and (iii) are both
> true-and-true or false-and-false; parts (ii) and (iv) are both mixed.

> [!note] Why this distinction shows up in engineering
> Two sensors that both report "not faulty" do not by themselves certify that the
> system is healthy: they may share a common cause. Logic built on
> $\leftrightarrow$ assumes the two statements are independent, and safety
> arguments that conflate "same truth value" with "both true" fail in exactly the
> way part (iii) demonstrates.

---

**Answered in phase P6, in `../CT_Questions/`.**

- *CT-04 Q.2(c)* is a class-test question. Its answer is in `../CT_Questions/CT_answers_exam_style.md`, with the reasoning in `../CT_Questions/CT_answers_explanation.md`.
- *CT-04 Q.3(c)* is a class-test question. Its answer is in `../CT_Questions/CT_answers_exam_style.md`, with the reasoning in `../CT_Questions/CT_answers_explanation.md`.

---

<a id="dm-33"></a><a id="dm-3.3"></a>
## DM-3.3 · Tautology, Contradiction & Contingency

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

---

<a id="dm-34"></a><a id="dm-3.4"></a>
## DM-3.4 · Valid, Satisfiable & Unsatisfiable Formulas

### [2024 Q.5(b)]

**Question.** Given the propositional formula $(p \to q) \land (q \to r)$, determine whether the formula is valid, satisfiable or unsatisfiable.

*[Marks: 04, CO: 2]*

**Solution.**

**The three definitions, because the question needs them.**

- **Valid**: true in *every* row of the truth table. A valid formula is called a
  tautology. Validity means "true for all possible truth values of $p, q, r$".
- **Satisfiable**: true in *at least one* row. A satisfiable formula is not
  necessarily valid; it only needs one witness.
- **Unsatisfiable**: true in *no* row. An unsatisfiable formula is a
  contradiction.

These are not mutually exclusive categories in the order they were asked. Every
valid formula is also satisfiable, because it is true in every row including at
least one. The standard classification of a formula asks whether it is a
tautology, a contradiction, or neither, and then reports satisfiability
separately.

**Building the truth table.** Three variables means $2^3 = 8$ rows.

| $p$ | $q$ | $r$ | $p \to q$ | $q \to r$ | $(p \to q) \land (q \to r)$ |
| :-: | :-: | :-: | :-: | :-: | :-: |
| T | T | T | T | T | **T** |
| T | T | F | T | F | **F** |
| T | F | T | F | T | **F** |
| T | F | F | F | T | **F** |
| F | T | T | T | T | **T** |
| F | T | F | T | F | **F** |
| F | F | T | T | T | **T** |
| F | F | F | T | T | **T** |

**Reading the table.** The formula is true in rows 1, 5, 7 and 8, and false in
rows 2, 3, 4 and 6.

$$\boxed{\text{Satisfiable but not valid}}$$

The formula is **not valid**, because there are rows where it is false. It is
**satisfiable**, because there are rows where it is true. It is **not
unsatisfiable**, for the same reason.

**The reasoning behind the result, stated in English.** $p \to q$ says that $p$
being true requires $q$ to be true. $q \to r$ says $q$ requires $r$. Together
they say the chain $p$ then $q$ then $r$ is consistent, which is exactly the
hypothetical syllogism. The formula fails precisely when $p$ and $q$ are both
true but $r$ is false: then $p \to q$ holds and $q \to r$ fails. That row is the
counterexample to validity, and it is the one to name in an answer.

> [!warning] The trap: assuming a true implication is a true conjunction
> $p \to q$ is true in three of four rows, so it is "almost always true". Two of
> them conjoined are true only in four of eight rows, not six. Conjunction
> requires both parts, so the result is false whenever either implication is
> false. The common slip is to reason "successful thesis contains hypothesis,
> successful thesis contains conclusion, therefore the combined formula is
> successful" which conflates *each part being often true* with *both parts being
> true together*.

---

**Answered in phase P6, in `../CT_Questions/`.**

- *CT-04 Q.3(d)* is a class-test question. Its answer is in `../CT_Questions/CT_answers_exam_style.md`, with the reasoning in `../CT_Questions/CT_answers_explanation.md`.

---

<a id="dm-35"></a><a id="dm-3.5"></a>
## DM-3.5 · Logical Equivalence

### [2023 Q.6(a)]

**Question.** Show that $\neg(p \leftrightarrow q)$ and $\neg p \leftrightarrow q$ are logically equivalent.

*[Marks: 02, CO: 3]*

**Solution.**

**Step 1. Build the truth table.**

| $p$ | $q$ | $p \leftrightarrow q$ | $\neg(p \leftrightarrow q)$ | $\neg p$ | $\neg p \leftrightarrow q$ |
| :-: | :-: | :-: | :-: | :-: | :-: |
| F | F | T | F | T | F |
| F | T | F | T | T | T |
| T | F | F | T | F | T |
| T | T | T | F | F | F |

The two computed columns are identical: F, T, T, F reading down the rows
$F F$, $F T$, $T F$, $T T$. Identical columns on every row means the formulas are
logically equivalent.

$$
\boxed{\neg(p \leftrightarrow q) \equiv (\neg p \leftrightarrow q)}
$$

**Step 2. Algebraic proof.** Rewrite both sides to the same thing.

Left side:

$$
\neg(p \leftrightarrow q) = \neg\big[(p \to q) \land (q \to p)\big]
= \neg(p \to q) \lor \neg(q \to p)
= (p \land \neg q) \lor (\neg p \land q)
$$

This is exclusive-or. Right side:

$$
\neg p \leftrightarrow q = (\neg p \to q) \land (q \to \neg p) = (p \lor q) \land (\neg q \lor \neg p)
$$

Distribute:

$$
(p \lor q) \land (\neg q \lor \neg p) = \big[(p \land \neg q) \lor (p \land \neg p) \lor (q \land \neg q) \lor (q \land \neg p)\big]
$$

The middle two terms are contradictions, since nothing is both a statement and its
negation:

$$
= (p \land \neg q) \lor 0 \lor 0 \lor (\neg p \land q) = (p \land \neg q) \lor (\neg p \land q)
$$

Both sides reduce to the same expression, so the equivalence is proven.

**In words.** "$p$ and $q$ disagree" means exactly one of them is true. If $p$ is
false, then "q agrees with $\neg p$" means $q$ is true, which is precisely the
case where they disagree. Flipping one input and asking for agreement tests the
same thing as asking for disagreement without the flip.

> [!note] Where the asymmetry comes from
> It is worth pausing on why this works for the *biconditional* and would not for
> the conditional. There is no analogous identity $\neg(p \to q) \equiv \neg p \to q$,
> and trying to assume one is a common slip.
>
> The reason is that $\leftrightarrow$ is symmetric under negation of an input
> while $\to$ is not. $p \leftrightarrow q$ is T when $p$ and $q$ agree. Negating
> $p$ makes it T when $p$ and $q$ *disagree*, which is exactly when
> $\neg(p \leftrightarrow q)$ is T. With $\to$, negating an input changes the
> structure of the formula rather than just flipping its value, so no such
> identity exists.

---

<a id="dm-36"></a><a id="dm-3.6"></a>
## DM-3.6 · Translation: English → Logic

---

**Every question that reaches this subtopic is written in the subtopic it is filed under.** Nothing is answered here, and that is deliberate rather than an omission: the subtopic holds the questions in the taxonomy but owns no block of its own.

- *2023 Q.6(c)* is the same question as [[DM-3.9_Rules_of_Inference_and_Valid_Arguments|DM-3.9]], which is written in `DM-3.9`.
- *2024 Q.5(c)* is the same question as [[DM-3.7_System_Specification_and_Consistency|DM-3.7]], which is written in `DM-3.7`.
- *CT-04 Q.2(a)* is the same question as [[DM-3.7_System_Specification_and_Consistency|DM-3.7]], which is written in `DM-3.7`.

---

**Answered in phase P6, in `../CT_Questions/`.**

- *CT-04 Q.3(a)* is a class-test question. Its answer is in `../CT_Questions/CT_answers_exam_style.md`, with the reasoning in `../CT_Questions/CT_answers_explanation.md`.

---

<a id="dm-37"></a><a id="dm-3.7"></a>
## DM-3.7 · System Specification & Consistency

### [2024 Q.5(c)]

**Question.** Are these system specifications consistent?

*[Marks: 04, CO: 2]*

**Solution.**

> The system is in multiuser state if and only if it is operating normally, the
> kernel is functioning. The kernel is not functioning or the system is in
> interrupt mode. If the system is not in multiuser state, then it is in
> interrupt mode. The system is not in interrupt mode.

**What consistency means.** A set of specifications is consistent when at least
one assignment of truth values makes all of them true at the same time. The
object being tested is the **conjunction** of the four, not each one on its own.
Four individually plausible sentences can easily be jointly impossible.

**Assign variables.** One symbol per simple statement:

| Symbol | Meaning |
| :-- | :-- |
| $p$ | system is in multiuser state |
| $q$ | kernel is functioning |
| $r$ | system is in interrupt mode |

**Translate.** The four sentences become

| # | English | Logic |
| :-: | :-- | :-- |
| 1 | multiuser if and only if the kernel is functioning | $p \leftrightarrow q$ |
| 2 | kernel not functioning, or interrupt mode | $\neg q \lor r$ |
| 3 | if not multiuser, then interrupt mode | $\neg p \to r$, equivalent to $p \lor r$ |
| 4 | not in interrupt mode | $\neg r$ |

Two of these translations need care. Sentence 3 is a conditional whose
consequent is $r$, so $\neg p \to r$ is equivalent to $p \lor r$ by the
definition of implication, and writing it as $p \lor r$ makes the truth table
easier to read. Sentence 2 is a disjunction, so it is true whenever the kernel
is broken *or* interrupt mode holds; the mistake is to read it as a conjunction.

**Test all eight assignments.** Three variables, so $2^3 = 8$ rows.

| $p$ | $q$ | $r$ | (1) $p \leftrightarrow q$ | (2) $\neg q \lor r$ | (3) $p \lor r$ | (4) $\neg r$ | all four |
| :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| F | F | F | T | T | F | T | **F** |
| F | F | T | T | T | T | F | F |
| F | T | F | F | F | F | T | F |
| F | T | T | F | T | T | F | F |
| T | F | F | F | T | T | T | **F** |
| T | F | T | F | T | T | F | F |
| T | T | F | T | F | F | T | F |
| T | T | T | T | T | T | F | F |

No row satisfies all four, so the set is inconsistent.

**Reason without a table.** This is faster and worth writing alongside, since it
shows *where* the conflict is. Sentence 4 forces $r = \mathrm{F}$. Sentence 2,
$\neg q \lor r$, then has both terms false unless $q$ is false, so $q = \mathrm{F}$.
Sentence 1 ties $p$ to $q$, so $p = \mathrm{F}$. Sentence 3 then reads
$p \lor r = \mathrm{F} \lor \mathrm{F} = \mathrm{F}$, contradicting the requirement that
all four hold.

$$\boxed{\text{The specifications are INCONSISTENT: no assignment satisfies all four}}$$

> [!warning] Where the contradiction comes from
> Sentence 4 says the system is **never** in interrupt mode. Sentence 2 then
> forces the kernel to be broken. Sentence 1 ties multiuser state to a working
> kernel, so the system cannot be in multiuser state either. Sentence 3 says a
> system that is not in multiuser state must be in interrupt mode, which
> sentence 4 has already ruled out. The set describes a machine that cannot
> exist. In practice this means one of the four requirements is a typo, usually
> sentence 4.

> [!info] Check by exhaustive enumeration
> The truth table above is the exhaustive check: all $2^3 = 8$ assignments were
> tested and none satisfied the conjunction. The chain of forcing steps is the
> same argument presented as a derivation, and it reaches the same conclusion,
> which is the confirmation that no row was skipped. The two routes disagree only
> if a row in the table was mis-evaluated, so comparing the count of satisfying
> rows (zero) against the chain's result (zero) is a complete check.

---

---

**Also asked here.**

- *2024 Q.6(b)* is the same question as [[DM-3.8_Normal_Forms_and_Functional_Completeness|DM-3.8]], which is written in `DM-3.8`.
- *CT-04 Q.2(b)* is the same question as [[DM-3.8_Normal_Forms_and_Functional_Completeness|DM-3.8]], which is written in `DM-3.8`.
- *CT-04 Q.2(c)* is the same question as [[DM-3.2_Logical_Connectives_and_Truth_Tables|DM-3.2]], which is written in `DM-3.2`.
- *CT-04 Q.3(c)* is the same question as [[DM-3.2_Logical_Connectives_and_Truth_Tables|DM-3.2]], which is written in `DM-3.2`.

---

**Answered in phase P6, in `../CT_Questions/`.**

- *CT-04 Q.2(a)* is a class-test question. Its answer is in `../CT_Questions/CT_answers_exam_style.md`, with the reasoning in `../CT_Questions/CT_answers_explanation.md`.
- *CT-04 Q.3(b)* is a class-test question. Its answer is in `../CT_Questions/CT_answers_exam_style.md`, with the reasoning in `../CT_Questions/CT_answers_explanation.md`.

---

<a id="dm-38"></a><a id="dm-3.8"></a>
## DM-3.8 · Normal Forms & Functional Completeness

### [2022 Q.5(c)]

**Question.** Show that $\neg$ and $\land$ form a functionally complete collection of logical operators.

*[Marks: 02, CO: 2]*

**Solution.**

**Definition.** A collection of operators is **functionally complete** if every
other Boolean operator can be expressed using only those operators.

**Goal.** Build $\lor$ and $\to$ from $\neg$ and $\land$ alone.

**Step 1. Disjunction, by De Morgan.** Since $\neg(p \land q) = \neg p \lor \neg q$,

$$
p \lor q = \neg(\neg p \land \neg q)
$$

**Step 2. Implication.** Since $p \to q \equiv \neg p \lor q$,

$$
p \to q = \neg p \lor q = \neg(\neg(\neg p) \land \neg q)
$$

**Step 3. Biconditional.** Since $p \leftrightarrow q \equiv (p \to q) \land (q \to p)$,
substituting step 2 in both places expresses it in terms of $\neg$ and $\land$
too.

**Step 4. Verify against the truth tables.** Rows run $p$ outer, $q$ inner, each
taking $T$ then $F$.

| $p$ | $q$ | $\neg p$ | $\neg q$ | $p \lor q$ | $\neg(\neg p \land \neg q)$ | $p \to q$ | $\neg(\neg(\neg p) \land \neg q)$ |
| :-: | :-: | :-: | :-: | :-: | :-- | :-: | :-- |
| F | F | T | T | F | $\neg(T \land T) = F$ ✓ | T | $\neg(F \land T) = T$ ✓ |
| F | T | T | F | T | $\neg(T \land F) = T$ ✓ | T | $\neg(F \land F) = T$ ✓ |
| T | F | F | T | T | $\neg(F \land T) = T$ ✓ | F | $\neg(T \land T) = F$ ✓ |
| T | T | F | F | T | $\neg(F \land F) = T$ ✓ | T | $\neg(T \land F) = T$ ✓ |

Every constructed column matches its target in all four rows.

**Step 5. Conclusion.** The operators $\neg$ and $\land$ generate $\lor$, $\to$,
$\leftrightarrow$ and everything built from them, so the collection is
functionally complete.

$$\boxed{p \lor q = \neg(\neg p \land \neg q), \qquad p \to q = \neg(\neg(\neg p) \land \neg q)}$$

> [!warning] Count the negations in the implication formula, they are easy to lose
> $p \to q \equiv \neg p \lor q$, and then $\neg p \lor q$ is already in disjunctive
> form, so it needs no De Morgan step at all. The formula
> $\neg(\neg(\neg p) \land \neg q)$ comes from rewriting $\neg p$ as
> $\neg(\neg(\neg p))$ so that both operands of $\lor$ sit under negations.
>
> Dropping one of the three negations on $p$ gives a formula that looks
> perfectly reasonable and is false on the row $p = T, q = F$. That single row is
> the whole test, and the table above is where it is caught.

> [!note] There are exactly two minimal complete sets
> They are $\{\neg, \land\}$ and $\{\neg, \lor\}$.
>
> Neither $\land$ nor $\lor$ alone is complete, since neither can produce
> negation. A set containing no negation at all cannot realise $p \lor \neg p$,
> which is a tautology and must therefore be constantly true, and a monotone
> connective cannot do that. **This is why every functionally complete set must
> contain $\neg$, or something that produces it.**

---

### [2024 Q.6(b)]

**Question.** A security system triggers an alarm if (a) motion is detected and the window is open, or (b) the door sensor is active but the security code is not entered. (i) Assign propositional variables, (ii) express the alarm condition as a single proposition, (iii) convert it into both CNF and DNF, describing each transformation step.

*[Marks: 06, CO: 2]*

**Solution.**

**Assign variables.** Every variable is defined **positively**, so the negation
falls where the English puts it rather than where the reader expects it.

| Symbol | Meaning |
| :-- | :-- |
| $m$ | motion is detected |
| $w$ | window is open |
| $d$ | door sensor is active |
| $s$ | security code **is** entered |
| $A$ | the alarm triggers |

**The condition as one proposition.** Branch (a) is $m \land w$. Branch (b) is
$d \land \neg s$, because "the code is not entered" is $\neg s$ and not a new
variable. The two branches are alternatives, so they are joined by $\lor$:

$$A = (m \land w) \lor (d \land \neg s)$$

> [!warning] The trap: "but" is "and", and "not entered" negates the code
> "The code is not entered" is the negation of "$s$ = the code **is** entered".
> Defining $s$ to mean "the code is not entered" and then writing $\neg s$ gives
> $d \land s$ for the branch, which reads correctly but is the wrong polarity
> against the variable table. The safeguard is to state what each variable means
> **positively** in the table, then let the negation fall where the English puts
> it. The second trap is treating "but" as a different connective from "and".
> Logically it is conjunction, and the contrast is rhetorical, not logical.

**To DNF.** By definition, a compound proposition is in Disjunctive Normal Form (DNF)
if it is a disjunction of conjunctions of literals. The formulated condition:

$$A = (m \land w) \lor (d \land \neg s)$$

is already in DNF (minimal DNF), consisting of two clauses: $(m \land w)$ and $(d \land \neg s)$.

If the **full canonical DNF** (sum of minterms containing all 4 variables) is required,
we expand each clause using the identity $X \equiv X \land (Y \lor \neg Y)$:

$$
\begin{aligned}
m \land w &\equiv (m \land w) \land (d \lor \neg d) \land (s \lor \neg s) \\
&= (m \land w \land d \land s) \lor (m \land w \land d \land \neg s) \lor (m \land w \land \neg d \land s) \lor (m \land w \land \neg d \land \neg s)
\end{aligned}
$$

$$
\begin{aligned}
d \land \neg s &\equiv (m \lor \neg m) \land (w \lor \neg w) \land (d \land \neg s) \\
&= (m \land w \land d \land \neg s) \lor (m \land \neg w \land d \land \neg s) \lor (\neg m \land w \land d \land \neg s) \lor (\neg m \land \neg w \land d \land \neg s)
\end{aligned}
$$

Combining and removing the shared duplicate minterm $(m \land w \land d \land \neg s)$ yields the 7-minterm canonical DNF:

$$
\begin{aligned}
A_{\text{canonical DNF}} = &(m \land w \land d \land s) \lor (m \land w \land d \land \neg s) \lor (m \land w \land \neg d \land s) \lor (m \land w \land \neg d \land \neg s) \\
&\lor (m \land \neg w \land d \land \neg s) \lor (\neg m \land w \land d \land \neg s) \lor (\neg m \land \neg w \land d \land \neg s)
\end{aligned}
$$

**To CNF.** A conjunction of disjunctions, that is a product of sums.
Apply the distributive law $P \lor (Q \land R) \equiv (P \lor Q) \land (P \lor R)$:

$$
\begin{aligned}
A &= (m \land w) \lor (d \land \neg s) \\
  &= \big[(m \land w) \lor d\big] \land \big[(m \land w) \lor \neg s\big]
    && \text{distribute over } (d \land \neg s)\\
  &= \big[(m \lor d) \land (w \lor d)\big] \land \big[(m \lor \neg s) \land (w \lor \neg s)\big]
    && \text{distribute } d \text{ and } \neg s\\
  &= (m \lor d) \land (w \lor d) \land (m \lor \neg s) \land (w \lor \neg s)
    && \text{remove grouping brackets}\\
  &= (m \lor d) \land (m \lor \neg s) \land (w \lor d) \land (w \lor \neg s)
    && \text{reorder clauses}
\end{aligned}
$$

$$\boxed{\text{CNF: } (m \lor d)\land(m \lor \neg s)\land(w \lor d)\land(w \lor \neg s)}$$

**How to check the two forms.** The original proposition, the canonical DNF (7 minterms), and the CNF (4 clauses) are all logically equivalent and evaluate identically across all $2^4 = 16$ assignments of $(m, w, d, s)$.

> [!info] Check by exhaustive evaluation
> All three representations evaluate identically on all $2^4 = 16$ assignments of $m, w, d, s$.
> For instance, when $m = \mathrm{T}, w = \mathrm{T}, d = \mathrm{F}, s = \mathrm{T}$, $m \land w$ is true, so the alarm triggers;
> both the DNF and every clause of the CNF evaluate to true.
> An algebra mistake in either conversion shows up as a row where the representations disagree.

> [!note] Which form to use
> **CNF** suits resolution and automated theorem provers, which read conjunctions
> of disjunctions directly. **DNF** suits fast evaluation and hardware
> implementation, because each product can be tested in isolation and the first
> one that succeeds ends the computation. The CNF here also reads as four
> independent failure conditions: for no alarm, motion must be absent or the
> door inactive, the door must be active or no motion seen, the window must be
> shut or the door inactive, and the window must be shut or the code entered.

---

**Answered in phase P6, in `../CT_Questions/`.**

- *CT-04 Q.2(b)* is a class-test question. Its answer is in `../CT_Questions/CT_answers_exam_style.md`, with the reasoning in `../CT_Questions/CT_answers_explanation.md`.

---

<a id="dm-39"></a><a id="dm-3.9"></a>
## DM-3.9 · Rules of Inference & Valid Arguments

### [2023 Q.6(b)]

**Question.** Briefly explain modus ponens, modus tollens, hypothetical syllogism, disjunctive syllogism with truth tables and examples.

*[Marks: 04, CO: 1]*

**Solution.**

All four are **inference rules**. Each is a valid argument form, meaning the
conclusion is guaranteed true whenever the premises are true. Validity is about
the *form*, not about whether any particular conclusion happens to be true, which
is why a truth table is the right tool: you are checking the form.

---

**1. Modus ponens (MP), affirming the antecedent**

$$
p \to q, \quad p \ \therefore\ q
$$

| $p$ | $q$ | $p \to q$ | Premises both true | Conclusion $q$ |
| :-: | :-: | :-: | :-: | :-: |
| F | F | T | antecedent false | F |
| F | T | T | antecedent false | T |
| T | F | F | no | |
| T | T | T | **yes** | **T** |

Whenever both premises hold, so does the conclusion. Valid.

**Example.** "If the switch is closed the lamp is lit." The switch is closed.
Therefore the lamp is lit.

---

**2. Modus tollens (MT), denying the consequent**

$$
p \to q, \quad \neg q \ \therefore\ \neg p
$$

| $p$ | $q$ | $p \to q$ | $\neg q$ | Both true | Conclusion $\neg p$ |
| :-: | :-: | :-: | :-: | :-: | :-: |
| F | F | T | T | **yes** | T |
| F | T | T | F | no | |
| T | F | F | T | no | |
| T | T | T | F | no | |

Valid. MT is the contrapositive rule, since $p \to q \equiv \neg q \to \neg p$.

**Example.** "If the fuse has blown the lamp is dark." The lamp is not dark.
Therefore the fuse has not blown.

---

**3. Hypothetical syllogism (HS), chaining**

$$
p \to q, \quad q \to r \ \therefore\ p \to r
$$

| $p$ | $q$ | $r$ | $p \to q$ | $q \to r$ | $p \to r$ |
| :-: | :-: | :-: | :-: | :-: | :-: |
| F | F | F | T | T | T |
| F | F | T | T | T | T |
| F | T | F | T | F | T |
| F | T | T | T | T | T |
| T | F | F | F | T | F |
| T | F | T | F | T | T |
| T | T | F | T | F | F |
| T | T | T | T | T | T |

Whenever both premises are T, so is $p \to r$. Valid.

**Example.** "If it rains the ground is wet. If the ground is wet the crop grows."
Therefore if it rains the crop grows.

---

**4. Disjunctive syllogism (DS), eliminating by negation**

$$
p \lor q, \quad \neg p \ \therefore\ q
$$

| $p$ | $q$ | $p \lor q$ | $\neg p$ | Both true | Conclusion $q$ |
| :-: | :-: | :-: | :-: | :-: | :-: |
| F | F | F | T | no | |
| F | T | T | T | **yes** | T |
| T | F | T | F | no | |
| T | T | T | F | no | |

Valid.

**Example.** "The input is 0 or 1." The input is not 0. Therefore the input is 1.

---

**Summary and comparison**

| Rule | Form | Name | Uses |
| :-- | :-- | :-- | :-- |
| MP | $p \to q,\ p \therefore q$ | Affirming the antecedent | Forward chaining |
| MT | $p \to q,\ \neg q \therefore \neg p$ | Denying the consequent, that is contraposition | Backward chaining |
| HS | $p \to q,\ q \to r \therefore p \to r$ | Transitivity | Chaining rules |
| DS | $p \lor q,\ \neg p \therefore q$ | Elimination | Splitting a case |

**The invalid forms**

| Form | Status | Why it fails |
| :-- | :-- | :-- |
| $p \to q,\ q \therefore p$ | **Invalid** (Fallacy of affirming the consequent) | Counterexample: $p = F, q = T$. Premises $(F \to T) = T$ and $q = T$ are true, but conclusion $p = F$ is false. |
| $p \to q,\ \neg p \therefore \neg q$ | **Invalid** (Fallacy of denying the antecedent) | Counterexample: $p = F, q = T$. Premises $(F \to T) = T$ and $\neg p = T$ are true, but conclusion $\neg q = F$ is false. |

Both are the *converse* and *inverse* of a conditional, and a conditional is not
equivalent to its converse or its inverse. It is equivalent only to its
**contrapositive** $\neg q \to \neg p$, which is what MT uses.

$$
\boxed{\text{MP, MT, HS, DS are valid; affirming the consequent and denying the antecedent are not}}
$$

> [!warning] The converse trap, worked out
> "If the switch is closed, the lamp is lit" does **not** let you conclude "the
> lamp is lit, so the switch is closed". The lamp can be lit by a second switch,
> by a battery, or by daylight through the window. The lamp being lit is
> *consistent* with the switch being closed; it does not *entail* it.
>
> The general form of the mistake: $p \to q$ gives you one direction only. Forward
> from $p$ you may conclude $q$. Backward from $q$ you may conclude nothing about
> $p$ except via the contrapositive, which requires $\neg q$ and gives you
> $\neg p$, not $p$.
>
> **How to spot it in a proof.** If you ever find yourself concluding $p$ from
> $q$ using a conditional, stop. Either the rule you used was MT and you have
> negated something you should not have, or you have slipped into affirming the
> consequent.

> [!note] HS needs the matching middle term
> Hypothetical syllogism only works because the two conditionals share $q$. Given
> $p \to q$ and $r \to q$, you cannot conclude $p \to r$, and given $p \to q$ and
> $p \to r$ you cannot conclude $q \to r$. The chain has to be
> $p \to q \to r$ with the same statement in the middle, and it is worth reading
> the chain aloud to check that it is.

---

### [2023 Q.6(c)]

**Question.** With these hypotheses: "It is not sunny this afternoon and it is colder than yesterday." "We will go swimming only if it is sunny." "If we do not swimming, then we will take a canoe trip." "If we take a canoe trip then we will be home by sunset." Using the inference rules, construct a valid argument for the conclusion: "we will be home by sunset".

*[Marks: 04, CO: 3]*

**Solution.**

**Assign variables.**

| Symbol | Meaning |
| :-- | :-- |
| $S$ | it is sunny this afternoon |
| $C$ | it is colder than yesterday |
| $W$ | we go swimming |
| $K$ | we take a canoe trip |
| $H$ | we are home by sunset |

**Translate the four hypotheses.**

1. "It is not sunny this afternoon **and** it is colder than yesterday":
   $\neg S \land C$
2. "We will go swimming **only if** it is sunny". The phrase "only if" means
   swimming is a **necessary** condition of sunshine, so $W \to S$:
   $W \to S$
3. "If we do not swim, then we will take a canoe trip": $\neg W \to K$
4. "If we take a canoe trip then we will be home by sunset": $K \to H$

**Extract what is needed.** Split hypothesis 1 by simplification to get $\neg S$
and $C$. The proof needs only $\neg S$.

The goal is $H$, so work backwards from the rule that produces it. Rule 4 needs
$K$, rule 3 needs $\neg W$, and $\neg W$ comes from $S$ by modus tollens on rule
2.

**The valid argument, step by step.**

| Step | Statement | Rule |
| ---: | :-- | :-- |
| 1 | $\neg S \land C$ | Premise 1 |
| 2 | $\neg S$ | Simplification, 1 |
| 3 | $W \to S$ | Premise 2 |
| 4 | $\neg W$ | Modus tollens, 3 and 2 |
| 5 | $\neg W \to K$ | Premise 3 |
| 6 | $K$ | Modus ponens, 5 and 4 |
| 7 | $K \to H$ | Premise 4 |
| 8 | $H$ | Modus ponens, 7 and 6 |

Therefore "we will be home by sunset" is a **valid conclusion**.

$$
\boxed{\neg S \Rightarrow \neg W \Rightarrow K \Rightarrow H, \quad \text{so } H \text{ follows validly}}
$$

> [!warning] The traps in this question
> **"Only if" is not "if".** "We will go swimming only if it is sunny" is
> $W \to S$, **not** $S \to W$. Reading it backwards inverts the conditional and
> breaks the whole proof. If it had been read as $S \to W$, step 4 could not be
> derived, since $\neg S$ carries no information about $W$.
>
> The general form of the trap: "A **only if** B" gives $A \to B$, while "A
> **if** B" gives $B \to A$. The word order in English puts the *antecedent* in
> the "if" clause and the *consequent* in the "only if" clause, so read the phrase
> and identify which letter appears where before writing the arrow.
>
> **Hypothesis 1 is a conjunction.** It provides $\neg S$ by simplification. It is
> tempting to treat "not sunny and colder" as one unit and hunt for a rule that
> accepts it. Split it first.
>
> **$C$ is never used, and that is not a mistake.** The problem gives four
> premises but the conclusion needs three. The fourth, $C$, is surplus. Do not go
> looking for a way to involve it; a valid argument may use fewer premises than
> are supplied.

> [!note] The whole argument as one chain
> $$\underbrace{W \to S}_{\text{premise 2}},\ \underbrace{\neg S}_{\text{premise 1}} \vdash \underbrace{\neg W}_{\text{MT}} \vdash \underbrace{K}_{\text{MP}} \vdash \underbrace{H}_{\text{MP}}$$
>
> Each arrow uses a different rule, and each premise is consumed exactly once. No
> premise appears twice and no rule is applied to a statement that does not supply
> what it needs, so the derivation is sound.
>
> Reading the chain in one line is a good habit for longer arguments. A chain that
> will not compress into a single line of arrows usually has a step that does not
> follow, and that is much easier to spot in one line than in a numbered table.

---

<a id="dm-310"></a><a id="dm-3.10"></a>
## DM-3.10 · Logic Puzzles

### [2022 Q.5(d)]

**Question.** Consider these statements, of which the first three are premises and the fourth is a valid conclusion. "All humming are richly colored." "No large birds live on honey." "Birds that do not live on honey are dull in order." Conclusion: "Humming birds are small."

*[Marks: 02, CO: 3]*

**Solution.**

> [!note] Origin & Textual Corrections
> This question is taken verbatim from Kenneth H. Rosen, *Discrete Mathematics and Its Applications* (§1.6, Example 26: "Rules of Inference"), which adapts a classic sorites puzzle by Lewis Carroll (from *Symbolic Logic*, 1896).
> - *"All humming"* has the noun "birds" omitted in the printed question.
> - *"dull in order"* is a transcription error for *"dull in colour"*.

**Step 1. Formalise using Predicate Logic.**
In Lewis Carroll's logic puzzles and Rosen's formulation, natural-language antonyms are treated as logical complements:
- "dull in colour" is the exact complement of "richly coloured" ($\neg S(x)$).
- "small" is the exact complement of "large" ($\neg Q(x)$).

Let the universe of discourse $U$ be the set of all birds:
- $P(x)$: $x$ is a hummingbird
- $Q(x)$: $x$ is large $\implies \neg Q(x)$: $x$ is small
- $R(x)$: $x$ lives on honey $\implies \neg R(x)$: $x$ does not live on honey
- $S(x)$: $x$ is richly coloured $\implies \neg S(x)$: $x$ is dull in colour

**Step 2. Express premises and the conclusion.**
1. Premise 1 ($P_1$): "All hummingbirds are richly colored"
   $$\forall x\, (P(x) \to S(x))$$
2. Premise 2 ($P_2$): "No large birds live on honey" (if large, then does not live on honey)
   $$\forall x\, (Q(x) \to \neg R(x))$$
3. Premise 3 ($P_3$): "Birds that do not live on honey are dull in colour"
   $$\forall x\, (\neg R(x) \to \neg S(x))$$
4. Conclusion ($C$): "Hummingbirds are small"
   $$\forall x\, (P(x) \to \neg Q(x))$$

**Step 3. Rigorous proof using Rules of Inference.**
Let $c$ be an arbitrary bird in $U$:

| Step | Proposition | Justification |
| :--: | :-- | :-- |
| 1 | $P(c) \to S(c)$ | Premise 1 by Universal Instantiation |
| 2 | $\neg R(c) \to \neg S(c)$ | Premise 3 by Universal Instantiation |
| 3 | $S(c) \to R(c)$ | Contrapositive of Step 2 ($\neg B \to \neg A \equiv A \to B$) |
| 4 | $P(c) \to R(c)$ | Hypothetical Syllogism from Steps 1 and 3 |
| 5 | $Q(c) \to \neg R(c)$ | Premise 2 by Universal Instantiation |
| 6 | $R(c) \to \neg Q(c)$ | Contrapositive of Step 5 |
| 7 | $P(c) \to \neg Q(c)$ | Hypothetical Syllogism from Steps 4 and 6 |
| 8 | $\forall x\, (P(x) \to \neg Q(x))$ | Universal Generalization from Step 7 |

Since $\neg Q(x)$ means "$x$ is small", the deduction is complete and valid.

$$
\boxed{\text{The argument is VALID via Universal Instantiation, Contraposition, and Hypothetical Syllogism}}
$$

> [!tip] Why propositional translation fails
> If modeled naively with 6 independent propositional variables:
> $$P_1: H \to R, \quad P_2: L \to \neg N, \quad P_3: \neg N \to D, \quad \text{Claim: } H \to S$$
> there is no syntactic link connecting $D$ to $\neg R$ or $S$ to $\neg L$. A countermodel emerges where a bird is simultaneously richly coloured and dull ($R=T, D=T$). In natural language, however, "dull" and "richly coloured" are mutually exclusive antonyms. Lewis Carroll's Sorites relies on these semantic complements, which predicate logic formalizes directly as $S(x)$ and $\neg S(x)$.

---

### [2022 Q.6(a)]

**Question.** Knights always tell the truth, Knaves always lie, Spies can either. Three people A, B and C, one of each type, each knows the types of the other two. (i) A says "C is the Knave", B says "A is the Knight", C says "I am the spy". (ii) A says "I am the Knave", B says "I am the Knave", C says "I am the Knave". Determine whether there is a unique solution.

*[Marks: 06, CO: 3]*

**Solution.**

**Method.** A knight's every statement is true. A knave's every statement is
false. A spy is unconstrained. Each of A, B and C may be any of the three types
and the three types are all different, so there are only $3! = 6$ assignments to
test. Testing all six is exhaustive and cheap.

**Rule stated first, because it settles part (ii) outright.** Nobody can
truthfully say "I am the knave", because a knave is by definition not a knave.
Nobody can falsely say it either, because the statement would be true for a knave.
Therefore **only a spy can say "I am the knave"**, and a knight or knave saying
it is an immediate contradiction.

---

**(i) A says "C is the Knave." B says "A is the Knight." C says "I am the spy."**

The three statements are true when, respectively, $C$ is the knave, $A$ is the
knight, and $C$ is the spy.

| Assignment | A's statement | B's statement | C's statement | Verdict |
| :-- | :-- | :-- | :-- | :-- |
| A=K, B=N, C=S | false (C is a spy, not a knave) | true | true | **A is a knight but lies. Out.** |
| A=K, B=S, C=N | true | true | false | **Consistent.** |
| A=N, B=K, C=S | false | false | true | **B is a knight but lies. Out.** |
| A=N, B=S, C=K | false | false | false | **C is a knight but lies. Out.** |
| A=S, B=K, C=N | true | false | false | **B is a knight but lies. Out.** |
| A=S, B=N, C=K | false | true | false | **C is a knight but lies. Out.** |

Exactly one row survives, so **the solution is unique**:

$$\boxed{\text{(i) A = Knight, B = Spy, C = Knave}}$$

**Verification.** A, a knight, says C is the knave: true, since $C$ is the
knave. B, a spy, says A is the knight: true, and a spy may tell the truth. C, a
knave, says "I am the spy": false, since $C$ is the knave. All consistent.

---

**(ii) A says "I am the Knave." B says "I am the Knave." C says "I am the Knave."**

| Assignment | A's statement | B's statement | C's statement | Verdict |
| :-- | :-- | :-- | :-- | :-- |
| A=K, B=N, C=S | false | true | false | A is a knight but lies. Out. |
| A=K, B=S, C=N | false | false | true | A is a knight but lies. Out. |
| A=N, B=K, C=S | true | false | false | A is a knave but tells the truth. Out. |
| A=N, B=S, C=K | true | false | false | A is a knave but tells the truth. Out. |
| A=S, B=K, C=N | false | false | true | B is a knight but lies. Out. |
| A=S, B=N, C=K | false | true | true | B is a knave but tells the truth. Out. |

**Every row is eliminated.**

$$\boxed{\text{(ii) There is NO solution}}$$

**Reason, without the table.** From the rule above, "I am the knave" can only be
said by a spy. All three of A, B and C say it. Since exactly one of the three is
a spy, at least two are knights or knaves, and each of those contradicts what
they said.

> [!info] Exhaustive check
> All six permutations were tested against the knight and knave rules in both
> parts. Part (i) returned exactly one consistent assignment; part (ii) returned
> none. Both results are therefore unique, and no assignment was missed.

> [!note] What separates the two parts
> In **(i)** the three statements refer to **different** people, so one true
> statement can be pinned on the spy and the remaining two can be assigned to a
> knight and a knave consistently.
>
> In **(ii)** all three statements are the same self-referential claim. Only one
> spy exists, so two of the three speakers are making a sentence they cannot make.
> That is the standard way to show a knights-and-knaves puzzle has no solution: put
> everyone in the same corner and no consistent assignment remains.
>
> The rule stated before the tables is worth internalising, because it turns part
> (ii) from six rows of bookkeeping into one sentence.

---

### [2023 Q.5(b)]

**Question.** Four friends have been identified as suspects for an unauthorized access into a computer system. Alice said "Carlos did it." John said "I did not do it." Carlos said "Diana did it." Diana said "Carlos lied when he said that I did it." (i) If exactly one of the four suspects is telling the truth, who did it? (ii) If exactly one is lying, who did it?

*[Marks: 04, CO: 3]*

**Solution.**

**Translate the statements.** The four suspects are mutually exclusive, so exactly
one of them did it. Let the culprit be one of $A, J, C, D$.

| Statement | True when |
| :-- | :-- |
| $S_A$: "Carlos did it" | culprit $= C$ |
| $S_J$: "I did not do it" | culprit $\ne J$ |
| $S_C$: "Diana did it" | culprit $= D$ |
| $S_D$: "Carlos lied when he said I did it" | Carlos's claim was false, that is culprit $\ne D$ |

The structural observation that makes this easy: **$S_C$ and $S_D$ are exact
negations of each other.** Carlos says Diana did it; Diana says Carlos's claim
was false. Either Diana did it and Carlos is truthful, or she did not and Carlos
is lying. Exactly one of those two is therefore **always** true, whatever the
culprit. This drives both parts.

**(i) Exactly one telling the truth**

Test each culprit:

| Culprit | $S_A$ | $S_J$ | $S_C$ | $S_D$ | True count |
| :-- | :-: | :-: | :-: | :-: | --: |
| A | F | T | F | T | 2 |
| J | F | F | F | T | **1** |
| C | T | T | F | T | 3 |
| D | F | T | T | F | 2 |

Only one row gives a count of 1.

$$\boxed{\text{(i) John did it}}$$

**Reasoning without a table.** Since $S_C$ and $S_D$ are negations, one of them
must be true, so the single truth must be one of those two, which means Alice and
John are both lying. John lying means his statement "I did not do it" is false,
so John did it.

Verify: John lying, Carlos lying (Diana did not do it), Alice lying (Carlos did
not do it), Diana telling the truth (Carlos's claim was false). Exactly one truth.
Agrees.

**(ii) Exactly one lying**

Equivalently, exactly three telling the truth. The same table, reading the false
count:

| Culprit | $S_A$ | $S_J$ | $S_C$ | $S_D$ | Lying count |
| :-- | :-: | :-: | :-: | :-: | --: |
| A | F | T | F | T | 2 |
| J | F | F | F | T | 3 |
| C | T | T | F | T | **1** |
| D | F | T | T | F | 2 |

Only one row gives a lying count of 1.

$$\boxed{\text{(ii) Carlos did it}}$$

**Reasoning without a table.** Exactly one lying means Alice and Diana are both
telling the truth, since they cannot both lie. Alice true gives culprit $= C$.
Then John says "I did not do it", which is true since Carlos did it, and Carlos
says "Diana did it", which is false. Exactly one lie, Carlos's. Agrees.

> [!info] Why the enumeration is complete
> Four candidates for the culprit against four statements is 16 combinations, and
> the mutual-exclusion constraint that exactly one person did it removes none of
> them, since every candidate satisfies it. So testing four culprits against four
> statements **is** the full enumeration. Both answers are unique, so each part
> has a single solution, which is what the question asks you to establish rather
> than assume.

> [!warning] The two parts have different answers, and that is intended
> Part (i) says exactly one is true. Part (ii) says exactly one is lying, which
> means exactly three are true. These are very different conditions and they
> cannot both hold at once.
>
> Expecting the same culprit in both parts is the standard error here, and it is
> worth noticing *why* the intuition misfires. Both answers involve the phrase
> "exactly one", and it is natural to read the two parts as restatements of the
> same constraint. They are not. If you find yourself trying to make one culprit
> satisfy both, you have collapsed "one truth-teller" into "one liar", which is
> the same mistake as writing modus tollens and then applying it forwards.

---

<a id="dm-311"></a><a id="dm-3.11"></a>
## DM-3.11 · Logic Gates & Digital Circuits

### [2023 Q.5(a)]

**Question.** Build a digital circuit that produces the output $(p \lor \neg r) \land (\neg p \lor (q \lor \neg r))$ when given input bits $p, q$ and $r$.

*[Marks: 04, CO: 2]*

**Solution.**

The question gives you an expression and asks for hardware. Building the circuit
straight from the expression works, but it needs four gates where three will do,
so the first job is simplification.

**Step 1. Simplify algebraically.** Look at the two bracketed terms:

$$
F = (p \lor \neg r) \land (\neg p \lor q \lor \neg r)
$$

$\neg r$ appears in both, and that is the handle to pull. Apply the distributive
identity

$$
(a \lor c) \land (b \lor c) = (a \land b) \lor c
$$

with $c = \neg r$, $a = p$ and $b = (\neg p \lor q)$:

$$
F = \neg r \lor \big[p \land (\neg p \lor q)\big]
$$

Now distribute inside the bracket:

$$
p \land (\neg p \lor q) = (p \land \neg p) \lor (p \land q) = 0 \lor (p \land q) = p \land q
$$

Therefore

$$
F = \neg r \lor (p \land q)
$$

**Step 2. Read off the circuit.**

1. Invert $r$ with a NOT gate to give $\neg r$.
2. AND $p$ with $q$ to give $p \land q$.
3. OR that with $\neg r$ to give the output $F$.

**Gates required:** 1 NOT, 1 AND (2-input), 1 OR (2-input), total: 3 gates.

**Logic Circuit Diagram (Simplified Form):**

![Digital logic circuit diagram for simplified expression F = ¬r ∨ (p ∧ q) using 1 NOT gate, 1 AND gate, and 1 OR gate](diagrams/2023_Q5a_simplified_logic_circuit.png)

**Alternative: Direct (Unsimplified) Circuit:**
If implemented directly without simplification:

![Direct logic circuit diagram implementing (p ∨ ¬r) ∧ (¬p ∨ (q ∨ ¬r)) with 2 NOT gates, 3 OR gates, and 1 AND gate](diagrams/2023_Q5a_unsimplified_circuit.jpg)

$$
\boxed{F = \neg r \lor (p \land q)}
$$

> [!info] Confirming over all eight input combinations
> Comparing the simplified form against the original on every assignment of
> $(p, q, r)$:
>
> | $p$ | $q$ | $r$ | Original | $\neg r \lor (p \land q)$ |
> | :-: | :-: | :-: | :-: | :-: |
> | F | F | F | T | T |
> | F | F | T | F | F |
> | F | T | F | T | T |
> | F | T | T | F | F |
> | T | F | F | T | T |
> | T | F | T | F | F |
> | T | T | F | T | T |
> | T | T | T | T | T |
>
> All eight rows agree, so the simplification is exact.
>
> Row 8 is the one to check by eye. With $r$ true, $\neg r$ is false, and the
> output fires only if both $p$ and $q$ are true. The original says
> $(p \lor \neg r) \land (\neg p \lor q \lor \neg r) = (T \lor F) \land (F \lor T \lor F) = T \land T = T$.
> Agrees.
>
> **Why checking all eight rows is worth the eight lines.** A three-variable
> Boolean function is completely determined by its truth table, so eight agreeing
> rows is a *proof* of equivalence, not a sample. That is a rare situation in
> this subject where exhaustive checking is genuinely conclusive.

> [!note] An equivalent form if you only have NAND gates
> Applying the distributive law back the other way gives

> $$
> F = (\neg r \lor p) \land (\neg r \lor q)
> $$
>
> This is useful in hardware because NAND is often the only gate a cheap part
> family provides. De Morgan's theorem turns each bracket into a NAND followed by
> an inverter, and a NAND-inverter pair is itself a NAND with its inputs tied, so
> the whole thing maps onto two NAND stages.

> [!warning] The mistake that keeps this question's marks
> Building the original expression gate for gate: NOT $r$, OR with $p$, then NOT
> $p$, OR with $q$ and $\neg r$, then AND. Five gates instead of three. It is a
> correct circuit and it will earn the marks, but it leaves the simplification
> on the table, and simplification is what the four marks are for.
>
> The tell is that $\neg r$ appears twice in the printed expression. Any
> sub-expression that appears more than once is a candidate for factoring out.

---

<a id="dm-313"></a><a id="dm-3.13"></a>
## DM-3.13 · Logic Extensions

### [2022 Q.5(b)]

**Question.** The truth value of the conjunction of two propositions in fuzzy logic is the minimum of the truth values of the statements "Fred and John are happy" and "Neither Fred nor John is happy". Prove the statement.

*[Marks: 03, CO: 1]*

**Solution.**

**Setup.** Fuzzy logic assigns each proposition a truth value in $[0,1]$, where
$0$ is false and $1$ is true. Fuzzy conjunction is **defined** by

$$
T(A \wedge B) = \min\left(T(A),\, T(B)\right)
$$

Let $h = T(\text{Fred is happy})$ and $j = T(\text{John is happy})$, with
$0 \le h, j \le 1$.

**Statement A, "Fred and John are happy."** A conjunction of two, so

$$
T(A) = \min(h, j)
$$

**Statement B, "Neither Fred nor John is happy."** "Neither A nor B" expands to
$\neg A \wedge \neg B$, and fuzzy negation is $T(\neg P) = 1 - T(P)$, so

$$
T(B) = \min(1 - h,\; 1 - j) = 1 - \max(h, j)
$$

**Statement C, the conjunction $A \wedge B$.** Applying the defining rule:

$$
T(C) = \min\left(T(A), T(B)\right) = \min\left(\min(h, j),\; 1 - \max(h, j)\right)
$$

Written out in full, that is $T(C) = \min(h,\; j,\; 1 - h,\; 1 - j)$, which is
exactly the assertion to be proved. The claim holds by the defining rule.

> [!warning] The identity is the definition, so the real content of the question is the bound
> $T(A \wedge B) = \min(T(A), T(B))$ needs no proof: it *is* fuzzy AND. What the
> chosen pair of sentences delivers is a strong limit, because $A$ and $B$ are
> contradictories.
>
> Since $T(C) = \min(h, 1-h) \le \frac{1}{2}$:
>
> | Case | $T(A)$ | $T(B)$ | $T(C)$ |
> | :-- | --: | --: | --: |
> | $h = j = 1$ | 1 | 0 | **0** |
> | $h = j = 0$ | 0 | 1 | **0** |
> | $h = 0.3, j = 0.4$ | 0.3 | 0.6 | **0.3** |
> | $h = j = 0.5$ | 0.5 | 0.5 | **0.5** |
> | $h = j = 0.7$ | 0.7 | 0.3 | **0.3** |
>
> **The conjunction never exceeds $0.5$, and its maximum is attained only at
> $h = j = 0.5$.** A sweep of the unit square on a $0.1$ grid confirms the maximum
> is $0.5$.
>
> Classical logic calls $A \wedge B$ always false. Fuzzy logic softens that to "at
> most half true", which is what makes fuzzy logic useful on contradictory-looking
> sensor data rather than merely decorative.

> [!info] Exhaustive confirmation
> The identity $T(A \wedge B) = \min(T(A), T(B))$ was evaluated at all $121$
> points of the grid $h, j \in \{0, 0.1, \ldots, 1.0\}$. In every case the computed
> conjunction equals the minimum of the two statement truth values, so no
> counterexample exists.

---

[🏠 Master Index](00_Index.md) | [← Prev Topic: NM-10 · PDE](NM-10_Partial_Differential_Equations.md) | [Next Topic: DM-5 · Number Theory →](DM-5_Number_Theory.md)
