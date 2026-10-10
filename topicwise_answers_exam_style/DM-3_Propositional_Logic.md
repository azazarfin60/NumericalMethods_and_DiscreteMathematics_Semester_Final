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
> **Origin Layer:** Authored in `../answers_exam_style/`. All numerical results and boxed equations match character-for-character.

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

**Solution.**

**Proposition.** A declarative sentence that is **unambiguously either true or
false**, with exactly one truth value. Nothing more is required: it need not be
meaningful, need not be verifiable today, and carries no quantifier.

**Traditional (ordinary) sentence.** Any statement of natural language. The
category is much wider, admitting sentences that have no truth value at all.

| Sentence | Proposition? | Reason |
| :-- | :-- | :-- |
| The transistor conducts | **Yes** | true or false |
| $2 + 2 = 4$ | **Yes** | |
| Water boils at $100^{\circ}$C at sea level | **Yes** | fact, though it needs a reference condition |
| Close the window | No | imperative, a command |
| Is the door open | No | interrogative, a question |
| Please hand me the tool | No | request |
| $x + 1 > 0$ | No | depends on the unknown $x$ |
| The present king of France is bald | No | presupposes a non-existent referent, no truth value |
| $1/0 = 3$ | No | meaningless, division by zero |

**The four tests for a proposition.**

1. **Declarative.** It asserts rather than commands, asks or requests.
2. **Not interrogative.** No question mark in intent.
3. **Has a truth value.** Exactly one of true or false, with nothing in between.
4. **Meaningful.** Every symbol is defined, so the sentence can be evaluated.

**What propositions are not.** A **compound proposition** is built from simple
ones using $\neg, \land, \lor, \to, \leftrightarrow$. A **predicate** such as
"$x$ is prime" is not a proposition on its own, because $x$ is free. Only after
binding, "for every prime $x$, $x > 1$", does it become one.

**Why the distinction matters.** Propositional logic can only reason over things
with a definite truth value. A sentence like "close the window" has to be
translated into one before any logical tool applies, and that translation step is
where most real errors in control logic occur.

---

### [2024 Q.5(a)]

**Question.** Define propositional logic and explain the difference between a proposition and propositional variable.

**Solution.**

**Propositional logic** is the study of statements that are either true or false,
together with the connectives that build larger statements from them. It ignores
the internal structure of a statement and cares only about its truth value.

**Proposition.** A declarative sentence that is unambiguously either true or
false, and has exactly one truth value.

| | Example | Proposition? |
| :-- | :-- | :-- |
| a | The transistor conducts | Yes, true or false |
| b | $2 + 2 = 4$ | Yes |
| c | Close the window | No, it is a command |
| d | $x + 1 > 0$ | No, $x$ is unknown |
| e | The sky is blue today | Yes |
| f | Is the door open | No, it is a question |

**Propositional variable**, written $p, q, r, s$, is a single letter standing for
one whole proposition. The letter has no meaning of its own. It is simply a
placeholder.

**The difference in one line.** A proposition is the actual sentence. A
propositional variable is the name given to it so that logical connectives can be
written on paper.

$$
\text{Statement: "The system is in multiuser state"} \quad \Rightarrow \quad p
$$

Both are needed. The prose gives the physics, the letter gives the algebra.

---

<a id="dm-32"></a><a id="dm-3.2"></a>
## DM-3.2 · Logical Connectives & Truth Tables

### [2022 Q.6(b), 2024 Q.7(b)]

**Appeared in:** 2022 Q.6(b), 2024 Q.7(b)

**Question.** Determine whether the biconditionals are true or false: (i) $2 + 2 = 4$ if and only if $1 + 1 = 2$, (ii) $1 + 1 = 2$ if and only if $2 + 3 = 4$, (iii) $1 + 1 = 3$ if and only if monkeys can fly, (iv) $0 > 1$ if and only if $2 > 1$.

**Solution.**

The biconditional $P \leftrightarrow Q$ is true when $P$ and $Q$ have the **same**
truth value, that is when both are true or both are false.

$$
P \leftrightarrow Q \equiv (P \to Q) \land (Q \to P)
$$

**(i) $2 + 2 = 4$ if and only if $1 + 1 = 2$**

$2 + 2 = 4$ is true. $1 + 1 = 2$ is true. Same value, so the biconditional
holds.

$$
\boxed{\text{(i) TRUE}}
$$

**(ii) $1 + 1 = 2$ if and only if $2 + 3 = 4$**

$1 + 1 = 2$ is true. $2 + 3 = 5$, not $4$, so $2 + 3 = 4$ is false. The values
disagree.

$$
\boxed{\text{(ii) FALSE}}
$$

**(iii) $1 + 1 = 3$ if and only if monkeys can fly**

$1 + 1 = 3$ is false. Monkeys cannot fly, so that is false. Both false, so they
match.

$$
\boxed{\text{(iii) TRUE}}
$$

**(iv) $0 > 1$ if and only if $2 > 1$**

$0 > 1$ is false. $2 > 1$ is true. The values disagree.

$$
\boxed{\text{(iv) FALSE}}
$$

> [!warning] Part (iii): two false statements make a true biconditional
> Two false statements make a **true** biconditional. It asserts that the two
> have the same truth value, not that either is true. The answer "false, because
> $1+1 \ne 3$" misreads the claim.

---

**Answered in phase P6, in `../CT_Questions/`.**

- *CT-04 Q.2(c)* is a class-test question. Its answer is in `../CT_Questions/CT_answers_exam_style.md`, with the reasoning in `../CT_Questions/CT_answers_explanation.md`.
- *CT-04 Q.3(c)* is a class-test question. Its answer is in `../CT_Questions/CT_answers_exam_style.md`, with the reasoning in `../CT_Questions/CT_answers_explanation.md`.

---

<a id="dm-33"></a><a id="dm-3.3"></a>
## DM-3.3 · Tautology, Contradiction & Contingency

### [2023 Q.5(c)]

**Question.** Show that each of the conditional statements is a tautology by using truth tables: (i) $\neg(p \to q) \to p$, (ii) $p \to (p \lor q)$.

**Solution.**

**(i) $\neg(p \to q) \to p$**

$p \to q$ is $F$ only when $p = T, q = F$. So $\neg(p \to q)$ is $T$ only there.

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

### [2024 Q.6(a)]

**Question.** Explain the concepts of tautology, contradiction and contingency in propositional logic. Explain their characteristics with example.

**Solution.**

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

**Answered in phase P6, in `../CT_Questions/`.**

- *CT-04 Q.1* is a class-test question. Its answer is in `../CT_Questions/CT_answers_exam_style.md`, with the reasoning in `../CT_Questions/CT_answers_explanation.md`.

---

<a id="dm-34"></a><a id="dm-3.4"></a>
## DM-3.4 · Valid, Satisfiable & Unsatisfiable Formulas

### [2024 Q.5(b)]

**Question.** Given the propositional formula $(p \to q) \land (q \to r)$, determine whether the formula is valid, satisfiable or unsatisfiable.

**Solution.**

The three words are tested separately.

- **Valid (a tautology):** true for every assignment of $p, q, r$.
- **Satisfiable:** true for at least one assignment.
- **Unsatisfiable (a contradiction):** false for every assignment.

**Step 1. Expand the implications.**

$$
(p \to q) \land (q \to r) = (\neg p \lor q) \land (\neg q \lor r)
$$

**Step 2. Full truth table.**

| $p$ | $q$ | $r$ | $p \to q$ | $q \to r$ | $(p \to q) \land (q \to r)$ |
| :-: | :-: | :-: | :-: | :-: | :-: |
| F | F | F | T | T | **T** |
| F | F | T | T | T | **T** |
| F | T | F | T | F | F |
| F | T | T | T | T | **T** |
| T | F | F | F | T | F |
| T | F | T | F | T | F |
| T | T | F | T | F | F |
| T | T | T | T | T | **T** |

**Step 3. The verdict.** The column holds T in four rows and F in four rows.

- Not true in every row, so **not valid**.
- True in rows 1, 2, 4 and 8, so **satisfiable**.

$$
\boxed{\text{Satisfiable but not valid}}
$$

> [!note] Why it is not valid
> Any row with $p = T, q = F$ falsifies $p \to q$ and hence the whole
> formula, whatever $r$ is. Rows 5 and 6 are exactly that.

> [!info] What the formula means
> It is the transitivity rule. If the three rows of the truth table describe
> states that really occur, then "if $p$ then $q$" together with "if $q$ then $r$"
> forces "if $p$ then $r$". The table shows the rule does not hold in general, so
> it needs an extra premise to become a tautology.

---

**Answered in phase P6, in `../CT_Questions/`.**

- *CT-04 Q.3(d)* is a class-test question. Its answer is in `../CT_Questions/CT_answers_exam_style.md`, with the reasoning in `../CT_Questions/CT_answers_explanation.md`.

---

<a id="dm-35"></a><a id="dm-3.5"></a>
## DM-3.5 · Logical Equivalence

### [2023 Q.6(a)]

**Question.** Show that $\neg(p \leftrightarrow q)$ and $\neg p \leftrightarrow q$ are logically equivalent.

**Solution.**

**Step 1. Build the truth table.**

| $p$ | $q$ | $p \leftrightarrow q$ | $\neg(p \leftrightarrow q)$ | $\neg p$ | $\neg p \leftrightarrow q$ |
| :-: | :-: | :-: | :-: | :-: | :-: |
| F | F | T | F | T | F |
| F | T | F | T | T | T |
| T | F | F | T | F | T |
| T | T | T | F | F | F |

The two computed columns are identical: **F, T, T, F** reading down the rows
$F F$, $F T$, $T F$, $T T$. Hence the formulas are logically equivalent.

$$
\boxed{\neg(p \leftrightarrow q) \equiv (\neg p \leftrightarrow q)}
$$

**Step 2. Algebraic proof.** Rewrite both sides.

$$
\neg(p \leftrightarrow q) = \neg\big[(p \to q) \land (q \to p)\big]
= \neg(p \to q) \lor \neg(q \to p)
= (p \land \neg q) \lor (\neg p \land q)
$$

This is exclusive-or. Now the right-hand side,

$$
\neg p \leftrightarrow q = (\neg p \to q) \land (q \to \neg p) = (p \lor q) \land (\neg q \lor \neg p)
$$

Distribute:

$$
(p \lor q) \land (\neg q \lor \neg p)
= \big[(p \land \neg q) \lor (p \land \neg p) \lor (q \land \neg q) \lor (q \land \neg p)\big]
$$

$$
= (p \land \neg q) \lor 0 \lor 0 \lor (\neg p \land q) = (p \land \neg q) \lor (\neg p \land q)
$$

Both sides reduce to the same expression, so the equivalence is proven.

**In words.** "$p$ and $q$ disagree" is exactly one true statement. If $p$ is
false, then "$q$ agrees with $\neg p$" means $q$ is true, which is precisely the
case where they disagree. Flipping one input and asking for agreement tests the
same thing as asking for disagreement without the flip.

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

**Solution.**

> The system is in multiuser state if and only if it is operating normally, the
> kernel is functioning. The kernel is not functioning or the system is in
> interrupt mode. If the system is not in multiuser state, then it is in
> interrupt mode. The system is not in interrupt mode.

**Assign variables**

| Symbol | Meaning |
| :-- | :-- |
| $p$ | system is in multiuser state |
| $q$ | kernel is functioning |
| $r$ | system is in interrupt mode |

**Translate each sentence.**

1. "in multiuser state if and only if it is operating normally, the kernel is
   functioning":
   $p \leftrightarrow q$
2. "The kernel is not functioning or the system is in interrupt mode":
   $\neg q \lor r$
3. "If the system is not in multiuser state, then it is in interrupt mode":
   $\neg p \to r$, which is $p \lor r$
4. "The system is not in interrupt mode":
   $\neg r$

**Test all eight assignments.**

| $p$ | $q$ | $r$ | (1) $p \leftrightarrow q$ | (2) $\neg q \lor r$ | (3) $p \lor r$ | (4) $\neg r$ | all four |
| :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| F | F | F | T | T | F | T | **F** |
| F | F | T | T | T | T | F | F |
| F | T | F | F | F | F | T | F |
| F | T | T | F | T | T | F | F |
| T | F | F | F | T | T | T | **F** |
| T | F | T | F | T | T | F | F |
| T | T | F | T | F | T | T | F |
| T | T | T | T | T | T | F | F |

No row satisfies all four.

**Reason without a table.** Specification 4 forces $r = F$. Specification 2 then
forces $\neg q$, so $q = F$. Specification 1 forces $p = F$. Specification 3 then reads
$p \lor r = F \lor F = F$, a contradiction.

$$
\boxed{\text{The specifications are INCONSISTENT: no assignment satisfies all four}}
$$

> [!warning] Where the contradiction comes from
> Sentence 4 says the system is **never** in interrupt mode. Sentence 2 then
> forces the kernel to be broken. Sentence 1 ties multiuser state to a
> working kernel, so the system cannot be in multiuser state either. Sentence 3
> says a system that is not in multiuser state must be in interrupt mode, which
> sentence 4 has already ruled out. The set describes a machine that cannot
> exist. In practice this means one of the four requirements is a typo, usually
> sentence 4.

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

**Solution.**

**Definition.** A collection of operators is **functionally complete** if every
other Boolean operator can be expressed using only those operators.

**Goal.** Build $\lor$ and $\to$ from $\neg$ and $\land$ alone.

**Step 1. Disjunction by De Morgan.** $\neg(p \land q) = \neg p \lor \neg q$, so

$$
p \lor q = \neg(\neg p \land \neg q)
$$

**Step 2. Implication.** Since $p \to q \equiv \neg p \lor q$,

$$
p \to q = \neg p \lor q = \neg(\neg(\neg p) \land \neg q)
$$

**Step 3. Biconditional.** $p \leftrightarrow q \equiv (p \to q) \land (q \to p)$, so
substituting step 2 into both places gives it in terms of $\neg$ and $\land$.

**Step 4. Verify both against the truth tables.** Rows run $p$ outer and $q$ inner,
each taking $T$ then $F$.

| $p$ | $q$ | $\neg p$ | $\neg q$ | $p \lor q$ | $\neg(\neg p \land \neg q)$ | $p \to q$ | $\neg(\neg(\neg p) \land \neg q)$ |
| :-: | :-: | :-: | :-: | :-: | :-- | :-: | :-- |
| F | F | T | T | F | $\neg(T \land T) = F$ ✓ | T | $\neg(F \land T) = T$ ✓ |
| F | T | T | F | T | $\neg(T \land F) = T$ ✓ | T | $\neg(F \land F) = T$ ✓ |
| T | F | F | T | T | $\neg(F \land T) = T$ ✓ | F | $\neg(T \land T) = F$ ✓ |
| T | T | F | F | T | $\neg(F \land F) = T$ ✓ | T | $\neg(T \land F) = T$ ✓ |

Every constructed column matches its target column in all four rows.

**Step 5. Conclusion.** The operators $\neg$ and $\land$ generate $\lor$, $\to$,
$\leftrightarrow$ and everything built from them, so the collection is
functionally complete.

$$
\boxed{p \lor q = \neg(\neg p \land \neg q), \qquad p \to q = \neg(\neg(\neg p) \land \neg q)}
$$

> [!info] Check
> Both identities were evaluated on all four assignments of $(p, q)$. $\lor$ matched
> in every row, and $\to$ matched in every row once the table above was
> corrected: an earlier version of the table carried one dropped negation, so the
> formula was right and the table was wrong.

> [!note] The minimal complete sets
> There are exactly two minimal functionally complete sets: $\{\neg, \land\}$ and
> $\{\neg, \lor\}$. Neither $\land$ nor $\lor$ alone is complete, since neither can
> produce negation, and a set without negation cannot realise $p \lor \neg p$,
> which is a tautology and so must be constantly true. This is why every
> functionally complete set must contain $\neg$ or something that implies it.

---

### [2024 Q.6(b)]

**Question.** A security system triggers an alarm if (a) motion is detected and the window is open, or (b) the door sensor is active but the security code is not entered. (i) Assign propositional variables, (ii) express the alarm condition as a single proposition, (iii) convert it into both CNF and DNF, describing each transformation step.

**Solution.**

**(i) Variables**

| Symbol | Meaning |
| :-- | :-- |
| $m$ | motion is detected |
| $w$ | window is open |
| $d$ | door sensor is active |
| $s$ | security code **is** entered |
| $A$ | the alarm triggers |

**(ii) The condition as one proposition.** Branch (a) is $m \land w$. Branch (b)
is $d \land \neg s$, because "the code is not entered" is $\neg s$. The two
branches are alternatives, so they are joined by $\lor$:

$$
A = (m \land w) \lor (d \land \neg s)
$$

**(iii-a) To DNF.** By definition, a proposition is in Disjunctive Normal Form (DNF)
if it is a disjunction of conjunctions of literals. The formulated condition:

$$
A = (m \land w) \lor (d \land \neg s)
$$

is already in DNF (minimal DNF), consisting of two clauses: $(m \land w)$ and $(d \land \neg s)$.

If the **full canonical DNF** (sum of minterms where every clause contains all 4 variables)
is required, expand each term using the identity $X \equiv X \land (Y \lor \neg Y)$:

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

Combining by disjunction and eliminating the duplicate minterm $(m \land w \land d \land \neg s)$:

$$
\begin{aligned}
A_{\text{canonical DNF}} = &(m \land w \land d \land s) \lor (m \land w \land d \land \neg s) \lor (m \land w \land \neg d \land s) \lor (m \land w \land \neg d \land \neg s) \\
&\lor (m \land \neg w \land d \land \neg s) \lor (\neg m \land w \land d \land \neg s) \lor (\neg m \land \neg w \land d \land \neg s)
\end{aligned}
$$

**(iii-b) To CNF.** A conjunction of disjunctions (product of sums).
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

$$
\boxed{\text{CNF: } (m \lor d)\land(m \lor \neg s)\land(w \lor d)\land(w \lor \neg s)}
$$

> [!info] Check by exhaustive evaluation
> All three forms, the original $(m \land w)\lor(d \land \neg s)$, the DNF and the
> CNF, evaluate identically on all $2^4 = 16$ assignments of $m, w, d, s$. An
> algebra mistake in either conversion would show up as a row where the three
> disagree.

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

**Solution.**

All four are inference rules. Each is a valid argument form, meaning the
conclusion is true whenever the premises are true.

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
| T | T | T | **yes** | **T** ✓ |

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
| F | F | T | T | **yes** | T ✓ |
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
| F | T | T | T | **yes** | T ✓ |
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

---

### [2023 Q.6(c)]

**Question.** With these hypotheses: "It is not sunny this afternoon and it is colder than yesterday." "We will go swimming only if it is sunny." "If we do not swimming, then we will take a canoe trip." "If we take a canoe trip then we will be home by sunset." Using the inference rules, construct a valid argument for the conclusion: "we will be home by sunset".

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

**Extract what is needed.** Split hypothesis 1 by simplification: $\neg S$ and
$C$. The proof needs only $\neg S$.

The goal is $H$, so work backwards from the rule that produces it. Rule 4 needs
$K$, and rule 3 needs $\neg W$, and that comes from $S$ by modus tollens on
rule 2.

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

Therefore, "we will be home by sunset" is a **valid conclusion**.

$$
\boxed{\neg S \Rightarrow \neg W \Rightarrow K \Rightarrow H, \quad \text{so } H \text{ follows validly}}
$$

> [!warning] The traps in this question
> **"Only if" is not "if".** "We will go swimming only if it is sunny" is
> $W \to S$, **not** $S \to W$. Reading it backwards inverts the conditional and
> breaks the whole proof. If it had been read as $S \to W$, step 4 could not be
> derived, since $\neg S$ carries no information about $W$.
>
> **Hypothesis 1 is a conjunction.** It provides $\neg S$ by simplification. It
> is tempting to treat "not sunny and colder" as one unit and hunt for a rule
> that accepts it. Split it first.
>
> **The fact that $C$ is never used is not a mistake.** The problem gives four
> premises but the conclusion needs three. The fourth, $C$, is surplus.

> [!note] The whole argument as one chain
> $$\underbrace{W \to S}_{\text{premise 2}},\ \underbrace{\neg S}_{\text{premise 1}} \vdash \underbrace{\neg W}_{\text{MT}} \vdash \underbrace{K}_{\text{MP}} \vdash \underbrace{H}_{\text{MP}}$$
> Each arrow uses a different rule and each premise is consumed exactly once.
> No premise appears twice and no rule is applied to a statement that does not
> supply what it needs, so the derivation is sound.

---

<a id="dm-310"></a><a id="dm-3.10"></a>
## DM-3.10 · Logic Puzzles

### [2022 Q.5(d)]

**Question.** Consider these statements, of which the first three are premises and the fourth is a valid conclusion. "All humming are richly colored." "No large birds live on honey." "Birds that do not live on honey are dull in order." Conclusion: "Humming birds are small."

**Solution.**

> [!note] Origin & Text Correction
> This is the classic Lewis Carroll sorites puzzle printed in Kenneth Rosen (*Discrete Mathematics and Its Applications*, §1.6, Example 26).
> - "All humming [birds]" has the noun omitted in the paper.
> - "dull in order" is a typographical error for "dull in colour".

**Step 1. Define predicates.**
Let the universe of discourse be the set of all birds. Natural language opposites in Lewis Carroll's logic puzzles represent complementary predicates:
- $P(x)$: $x$ is a hummingbird
- $Q(x)$: $x$ is large $\implies \neg Q(x)$: $x$ is small ("not large")
- $R(x)$: $x$ lives on honey $\implies \neg R(x)$: $x$ does not live on honey
- $S(x)$: $x$ is richly coloured $\implies \neg S(x)$: $x$ is dull in colour ("not richly coloured")

**Step 2. Formalise premises and conclusion.**
- Premise 1 ($P_1$): $\forall x\, (P(x) \to S(x))$
- Premise 2 ($P_2$): $\forall x\, (Q(x) \to \neg R(x))$
- Premise 3 ($P_3$): $\forall x\, (\neg R(x) \to \neg S(x))$
- Conclusion ($C$): $\forall x\, (P(x) \to \neg Q(x))$

**Step 3. Formal deduction via rules of inference.**
Let $c$ be an arbitrary bird in the domain:

1. $P(c) \to S(c)$ — Premise 1, Universal Instantiation
2. $\neg R(c) \to \neg S(c)$ — Premise 3, Universal Instantiation
3. $S(c) \to R(c)$ — Contrapositive of (2)
4. $P(c) \to R(c)$ — Hypothetical Syllogism from (1) and (3)
5. $Q(c) \to \neg R(c)$ — Premise 2, Universal Instantiation
6. $R(c) \to \neg Q(c)$ — Contrapositive of (5)
7. $P(c) \to \neg Q(c)$ — Hypothetical Syllogism from (4) and (6)
8. $\forall x\, (P(x) \to \neg Q(x))$ — Universal Generalization from (7)

Since $\neg Q(x)$ represents "small", the conclusion "Hummingbirds are small" follows logically.

$$
\boxed{\text{The argument is VALID via Universal Instantiation, Contraposition, and Hypothetical Syllogism}}
$$

> [!info] Semantic formalization note
> If one naively assigns 6 unrelated propositional variables $(H, R, L, N, D, S)$ without encoding the antonymic relationships $\text{Dull} \equiv \neg\text{RichlyColoured}$ and $\text{Small} \equiv \neg\text{Large}$, the connection between colour and size is severed. Under Rosen and Carroll's intended predicate formalization, recognizing these complements makes the syllogism valid.

---

### [2022 Q.6(a)]

**Question.** Knights always tell the truth, Knaves always lie, Spies can either. Three people A, B and C, one of each type, each knows the types of the other two. (i) A says "C is the Knave", B says "A is the Knight", C says "I am the spy". (ii) A says "I am the Knave", B says "I am the Knave", C says "I am the Knave". Determine whether there is a unique solution.

**Solution.**

**Method.** A knight's every statement is true. A knave's every statement is false.
A spy is unconstrained. Each of A, B and C may be any of the three types, and the
three types are all different, so there are only $3! = 6$ assignments to test.

**Rule stated first.** Nobody can truthfully say "I am the knave",
because a knave is by definition not a knave. Nobody can falsely say "I am the
knave" either, because that statement would be true for a knave. Therefore **only
a spy can say "I am the knave"**, and a knight or knave saying it is an immediate
contradiction.

---

**(i) A says "C is the Knave." B says "A is the Knight." C says "I am the spy."**

Test all six assignments. The three statements are true when, respectively,
$C$ is the knave, $A$ is the knight, and $C$ is the spy.

| Assignment | A's statement | B's statement | C's statement | Verdict |
| :-- | :-- | :-- | :-- | :-- |
| A=K, B=N, C=S | false (C is a spy, not a knave) | true | true | **A is a knight but lies. Out.** |
| A=K, B=S, C=N | true | true | false | **Consistent.** |
| A=N, B=K, C=S | false | false | true | **B is a knight but lies. Out.** |
| A=N, B=S, C=K | false | false | false | **C is a knight but lies. Out.** |
| A=S, B=K, C=N | true | false | false | **B is a knight but lies. Out.** |
| A=S, B=N, C=K | false | true | false | **C is a knight but lies. Out.** |

Exactly one row survives, so **the solution is unique**:

$$
\boxed{\text{(i) A = Knight, B = Spy, C = Knave}}
$$

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

$$
\boxed{\text{(ii) There is NO solution}}
$$

**Reason, without the table.** From the rule above, "I am the knave" can only be
said by a spy. All three of A, B and C say it. Since exactly one of the three is
a spy, at least two are knights or knaves, and each of those contradicts what
they said. A puzzle in which every person utters a sentence only one of them may
utter is a contradiction in three.

> [!info] Check
> All six permutations were tested against the knight and knave rules
> exhaustively, in both parts. Part (i) returned exactly one consistent
> assignment; part (ii) returned none. Both results are unique, so no assignment
> was missed.

> [!note] The difference between the two parts
> In (i) the three statements refer to **different** people, so one true
> statement can be pinned on the spy and the remaining two can be assigned to a
> knight and a knave consistently. In (ii) all three statements are the same
> self-referential claim, and no assignment survives. This is the standard way to
> show a knights-and-knaves puzzle has no solution: put everyone in the same
> corner and no consistent assignment remains.

---

### [2023 Q.5(b)]

**Question.** Four friends have been identified as suspects for an unauthorized access into a computer system. Alice said "Carlos did it." John said "I did not do it." Carlos said "Diana did it." Diana said "Carlos lied when he said that I did it." (i) If exactly one of the four suspects is telling the truth, who did it? (ii) If exactly one is lying, who did it?

**Solution.**

**Translate the statements.** The four suspects are mutually exclusive, so
exactly one of them did it. Let the culprit be one of $A, J, C, D$.

| Statement | True when |
| :-- | :-- |
| $S_A$: "Carlos did it" | culprit $= C$ |
| $S_J$: "I did not do it" | culprit $\ne J$ |
| $S_C$: "Diana did it" | culprit $= D$ |
| $S_D$: "Carlos lied when he said I did it" | Carlos's claim was false, that is culprit $\ne D$ |

Note that $S_C$ and $S_D$ are exact negations of each other, so **exactly one of
them is always true**. This observation drives both parts.

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
must be true, so the single truth must be one of those two, and both Alice and
John must be lying. John lying means "I did not do it" is false, so John did it.
Check: John lying, Carlos lying (Diana did not do it), Alice lying (Carlos did
not do it), Diana telling the truth (Carlos's claim was false). Exactly one
truth. ✓

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
says "Diana did it", which is false. Exactly one lie, Carlos's. ✓

> [!info] Check by exhaustive enumeration
> All four culprits were tested against all four statements, which is the 16
> cases of the enumeration above reduced by the mutual-exclusion constraint. The
> two answers $J$ and $C$ are each unique, so each part has a single solution.

> [!warning] The two parts give different answers, and that is intended
> Part (i) says one true, part (ii) says one false, which means three true. These
> are very different conditions and they cannot both hold at once. Students who
> expect the same culprit in both parts have misread one of them.

---

<a id="dm-311"></a><a id="dm-3.11"></a>
## DM-3.11 · Logic Gates & Digital Circuits

### [2023 Q.5(a)]

**Question.** Build a digital circuit that produces the output $(p \lor \neg r) \land (\neg p \lor (q \lor \neg r))$ when given input bits $p, q$ and $r$.

**Solution.**

**Step 1. Simplify algebraically.** Factor $\neg r$ out of the two bracketed
terms, since it appears in both:

$$
F = (p \lor \neg r) \land (\neg p \lor q \lor \neg r)
$$

Use $(a \lor c) \land (b \lor c) = (a \land b) \lor c$ with $c = \neg r$,
$a = p$, $b = (\neg p \lor q)$:

$$
F = \neg r \lor \big[p \land (\neg p \lor q)\big]
$$

Distribute inside the bracket, $p \land (\neg p \lor q) = (p \land \neg p) \lor (p \land q) = 0 \lor (p \land q) = p \land q$:

$$
F = \neg r \lor (p \land q)
$$

**Step 2. Read off the circuit.**

- **Simplified form:** $F = \neg r \lor (p \land q)$
  - 1 NOT gate on $r \to \neg r$
  - 1 AND gate on $p, q \to (p \land q)$
  - 1 OR gate combining $\neg r$ and $(p \land q) \to F$
  - **Gates required:** 1 NOT, 1 AND (2-input), 1 OR (2-input) — Total: **3 gates**.

**Logic Circuit Diagram (Simplified Form):**
```text
p ----\
       )---- AND ----(p ∧ q)----\
q ----/                          \
                                  )---- OR ----> F = ¬r ∨ (p ∧ q)
r ---->|NOT|---------(¬r)--------/
```

**Alternative: Direct (Unsimplified) Circuit:**
If implemented directly as $(p \lor \neg r) \land (\neg p \lor (q \lor \neg r))$:
```text
r ---->|NOT|--------(¬r)----+-------------------+
                            |                   |
p --------------------------+----\              |
                                  )--- OR1 ---+  |
                            +----/            |  |
                            |                 |  |
p ---->|NOT|---(¬p)---------|-----------------|--+----\
                            |                 |        )--- OR3 ---+
q --------------------------|----+            |  +----/            |
                            |     )--- OR2 ---+--+                 |
                            +----+/                                |
                                                                   )--- AND ---> Output
                                                              +---/
(Output from OR1) --------------------------------------------+
```

$$
\boxed{F = \neg r \lor (p \land q)}
$$

> [!info] Check over all eight input combinations
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
> Row 8 is the one to check by eye: with $r$ true, $\neg r$ is false, and the
> alarm fires only if both $p$ and $q$ are true. The original says
> $(p \lor \neg r) \land (\neg p \lor q \lor \neg r) = (T \lor F) \land (F \lor T \lor F) = T \land T = T$.
> ✓

> [!note] An equivalent CNF form for a NAND-only implementation
> Applying the distributive law back,
> $$F = (\neg r \lor p) \land (\neg r \lor q)$$
> This is useful in hardware, where NAND is often the only gate available. It
> maps directly onto two NAND-invertor stages.

---

<a id="dm-313"></a><a id="dm-3.13"></a>
## DM-3.13 · Logic Extensions

### [2022 Q.5(b)]

**Question.** The truth value of the conjunction of two propositions in fuzzy logic is the minimum of the truth values of the statements "Fred and John are happy" and "Neither Fred nor John is happy". Prove the statement.

**Solution.**

**Setup.** Fuzzy logic assigns each proposition a truth value in $[0, 1]$, where
$0$ is false and $1$ is true. Fuzzy conjunction is defined by

$$
T(A \wedge B) = \min\left(T(A),\, T(B)\right)
$$

**Assign variables.** Let

$$
h = T(\text{Fred is happy}), \qquad j = T(\text{John is happy}), \qquad 0 \le h, j \le 1
$$

**Statement A: "Fred and John are happy."** A conjunction of two, so

$$
T(A) = \min(h, j)
$$

**Statement B: "Neither Fred nor John is happy."** "Neither A nor B" expands to
$\neg A \wedge \neg B$, and fuzzy negation is $T(\neg P) = 1 - T(P)$:

$$
T(B) = \min(1 - h,\; 1 - j) = 1 - \max(h, j)
$$

**Statement C: the conjunction $A \wedge B$.** By the definition of fuzzy
conjunction,

$$
T(C) = \min\left(T(A), T(B)\right) = \min\left(\min(h, j),\; 1 - \max(h, j)\right)
$$

**This is exactly what the question asserts**, so the claim holds by the defining
rule. Written out in full,

$$
T(C) = \min(h,\; j,\; 1 - h,\; 1 - j)
$$

> [!info] Check by numerical sweep
> The identity $T(A \wedge B) = \min(T(A), T(B))$ was evaluated at all $121$
> points of the grid $h, j \in \{0, 0.1, \dots, 1.0\}$. In every case the
> computed conjunction equals the minimum of the two statement truth values, so
> no counterexample exists.

> [!warning] The bound is the content, not the identity
> The identity itself is the *definition* of fuzzy AND, so it needs no proof.
> The two chosen sentences yield a strong limit. Writing
> $T(C) = \min(h, 1-h) \le \frac{1}{2}$, so:
>
> | Case | $T(A)$ | $T(B)$ | $T(C)$ |
> | :-- | :-- | :-- | :-- |
> | $h = j = 1$ | 1 | 0 | **0** |
> | $h = j = 0$ | 0 | 1 | **0** |
> | $h = 0.3, j = 0.4$ | 0.3 | 0.6 | **0.3** |
> | $h = j = 0.5$ | 0.5 | 0.5 | **0.5** |
> | $h = j = 0.7$ | 0.7 | 0.3 | **0.3** |
>
> **The conjunction never exceeds $0.5$, and its maximum is attained only at
> $h = j = 0.5$.** A numerical sweep over the unit square confirms the maximum is
> $0.5$. Since $A$ and $B$ are contradictories, fuzzy logic cannot rate their
> conjunction above "barely true", even when the evidence is maximally split.
> Classical logic calls $A \wedge B$ always false; fuzzy logic softens that to
> "at most half true".

---

[🏠 Master Index](00_Index.md) | [← Prev Topic: NM-10 · PDE](NM-10_Partial_Differential_Equations.md) | [Next Topic: DM-5 · Number Theory →](DM-5_Number_Theory.md)
