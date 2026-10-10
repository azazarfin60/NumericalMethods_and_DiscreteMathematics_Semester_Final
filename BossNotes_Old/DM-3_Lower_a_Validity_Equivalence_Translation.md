[← Previous: DM-3.9 Rules of Inference and Valid Arguments](DM-3.9_Rules_of_Inference_and_Valid_Arguments.md) | [🏠 Index](00_Index.md) | [Next: DM-3 Lower-b: Puzzles, Gates, Extensions →](DM-3_Lower_b_Puzzles_Gates_Extensions.md)

---

# DM-3 Lower-a: Validity, Equivalence, Translation
> **Section:** B (Discrete Mathematics) | **Priority:** 🟠 | **Exam Frequency:** 4/5 appearances (2023, 2024, CT-04 ×5)
> **Subtopics:** DM-3.4 (Valid/Satisfiable/Unsatisfiable), DM-3.5 (Logical Equivalence), DM-3.6 (English to Logic), DM-3.7 (System Specification and Consistency)
> **Sources:** Rosen §1.2 (pp. 16–22), §1.3 (pp. 29–33), §1.1 (p. 11), Fahad Notes Class-13 to Class-14, Raidah Notes §3–§5, Shishir Notes §6–§9

## Why This Topic Matters

This file carries the whole applied half of propositional logic. Two things get tested: sorting a formula into valid / satisfiable / unsatisfiable, and turning English into logic without losing a word. The English-to-logic direction is the one that eats marks, because a single wrong connective produces a formula that is true in all the wrong rows. 2024 Q.5(b) and Q.5(c) tested both directions in the same question. CT-04 Q.2(a) and Q.3(a) to Q.3(d) tested the translation direction five times.

> [!WARNING] Teacher signal, and how to read it
> Fahad's notes record that Sir skipped **propositional satisfiability** in class and said **logic puzzles** would not be asked. The exam disagreed on both counts. 2024 Q.5(b) is a straight satisfiability question and 2022 Q.6(a) plus 2023 Q.5(b) are straight logic puzzles. The skip was about the section number, not the topic. Treat the notes as a warning about depth, never as permission to leave a gap.

---

## 📝 Key Definitions

> **Satisfiable:** "A compound proposition is **satisfiable** if there is an assignment of truth values to its variables that makes it true. When no such assignments exists, that is, when the compound proposition is false for all assignments of truth values to its variables, the compound proposition is **unsatisfiable**." — Rosen, §1.3, Propositional Satisfiability (p. 32)

> **Valid:** "A compound proposition that is always true is called a **tautology**; one that is always false is called a **contradiction**. A compound proposition that is sometimes true and sometimes false is called a **contingency**. A compound proposition is **satisfiable** if there is an assignment of truth values to its variables that makes it true." — Rosen, §1.3, Key Terms (p. 33)

> **Consistent:** "System specifications should be **consistent**, that is, they should not contain conflicting requirements that could be used to derive a contradiction. When specifications are not consistent, there would be no way to develop a system that satisfies all specifications." — Rosen, §1.2, System Specifications (p. 18)

> **Logically equivalent:** "compound propositions that always have the same truth values" — Rosen, §1.3, Key Terms (p. 33). More fully: two compound propositions are **logically equivalent** if $p \leftrightarrow q$ is a tautology. Fahad Notes, Class-14 (p. 34).

> **Why translate at all:** "logic is used in the specification of software and hardware, because these specifications need to be precise before development begins." — Rosen, §1.2, Introduction (p. 16)

---

## DM-3.4: Valid, Satisfiable and Unsatisfiable Formulas

### The three words, tested separately

A formula with $n$ variables has $2^n$ rows in its truth table. Read the final column and count.

| Count of T in the final column | Verdict | Synonym |
| :-- | :-- | :-- |
| every row | **valid** | tautology |
| at least one row, not every row | **satisfiable** | contingency |
| no row | **unsatisfiable** | contradiction |

**"Valid" is the strongest word.** A tautology is automatically satisfiable, so the two are not alternatives in the way the exam wording suggests. When a question says "valid, satisfiable or unsatisfiable", write down how many T rows you found and let the count decide.

| Wording in the paper | What you must show |
| :-- | :-- |
| "is it a tautology?" | all $2^n$ rows T |
| "is it satisfiable?" | at least one T row, or a row you can name |
| "is it unsatisfiable?" | all $2^n$ rows F, or a proof that no row works |
| "valid, satisfiable or unsatisfiable?" | the row count, stated explicitly |

> [!NOTE] Proving unsatisfiability without a table
> Rosen says a truth table is not always the fastest route: "Although we can always use a truth table to determine whether a compound proposition is satisfiable, it is often more efficient not to." — Rosen, §1.3 (p. 32)
>
> The trick: force values one at a time. Take a literal that must be false, substitute, take the next. If you reach $0 = 1$ or $T \land F$, the formula is unsatisfiable and you have a shorter proof than the table.

### Worked Example (PYQ 2024 Q.5(b))

> **Source:** 2024 Q.5(b)

**Question.** Given the propositional formula $(p \to q) \land (q \to r)$, determine whether the formula is valid, satisfiable or unsatisfiable.

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
> Any row with $p = T, q = F$ falsifies $p \to q$ and hence the whole formula, whatever $r$ is. Rows 5 and 6 are exactly that.

> [!info] What the formula means
> It is the transitivity rule. If the three rows of the truth table describe states that really occur, then "if $p$ then $q$" together with "if $q$ then $r$" forces "if $p$ then $r$". The table shows the rule does not hold in general, so it needs an extra premise to become a tautology.

**The missing premise, written out.** Add $p \to r$ as a conjunct and CT-04 Q.1 gives the tautology:

$$
[(p \to q) \land (q \to r)] \to (p \to r)
$$

You met that in [DM-3.9](DM-3.9_Rules_of_Inference_and_Valid_Arguments.md) as the hypothetical syllogism rule. Its truth table is the eight rows above with a ninth column that is T in every row.

---

## DM-3.5: Logical Equivalence

Two formulas are **logically equivalent** when they agree in every row. Two routes prove it, and examiners accept either.

| Route | What you show | When to use it |
| :-- | :-- | :-- |
| **Truth table** | the two computed columns match row by row | two variables, or when asked "by truth table" |
| **Algebraic** | both sides reduce to the same normal form | three or more variables, or when asked "algebraically" |

**The third route.** Normalize both sides to CNF or DNF using [DM-3.8](DM-3.8_Normal_Forms_and_Functional_Completeness.md). If the two normal forms are character-identical, the formulas are equivalent. This is the fastest route on long expressions.

### Worked Example (PYQ 2023 Q.6(a))

> **Source:** 2023 Q.6(a)

**Question.** Show that $\neg(p \leftrightarrow q)$ and $\neg p \leftrightarrow q$ are logically equivalent.

**Step 1. Build the truth table.**

| $p$ | $q$ | $p \leftrightarrow q$ | $\neg(p \leftrightarrow q)$ | $\neg p$ | $\neg p \leftrightarrow q$ |
| :-: | :-: | :-: | :-: | :-: | :-: |
| F | F | T | F | T | F |
| F | T | F | T | T | T |
| T | F | F | T | F | T |
| T | T | T | F | F | F |

The two computed columns are identical: **F, T, T, F** reading down the rows $F F$, $F T$, $T F$, $T T$. Hence the formulas are logically equivalent.

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

**In words.** "$p$ and $q$ disagree" is exactly one true statement. If $p$ is false, then "$q$ agrees with $\neg p$" means $q$ is true, which is precisely the case where they disagree. Flipping one input and asking for agreement tests the same thing as asking for disagreement without the flip.

> [!TIP] A shortcut worth memorizing
> $(p \leftrightarrow q) \equiv (\neg p \leftrightarrow \neg q) \equiv (\neg p \leftrightarrow q) \equiv (p \leftrightarrow \neg q)$. Negating an odd number of inputs flips agreement to disagreement; negating an even number keeps it. Every one of these four collapses into the same fact, which is exactly what the 2023 proof demonstrates.

---

## DM-3.6: Translation: English to Logic

This is the highest-marks-per-minute subtopic in the file. The formula is worth nothing if the connective is wrong, so the whole job is choosing the connective correctly.

### The connective table

| English phrase | Symbol | Reading |
| :-- | :-- | :-- |
| "is", "and", "also", "but" | $\land$ | both |
| "or" | $\lor$ | at least one |
| "not", "no" | $\neg$ | negation |
| "but not both" | $\oplus$ | exactly one |
| "if $p$ then $q$" | $p \to q$ | $p$ is the antecedent |
| "$q$ only if $p$" | $q \to p$ | the arrow points at "only if" |
| "$p$ if $q$" | $q \to p$ | arrow points back at "if" |
| "if and only if", "iff", "exactly when" | $\leftrightarrow$ | both directions |
| "neither $p$ nor $q$" | $\neg p \land \neg q$ | negate both |
| "$p$ unless $q$" | $\neg q \to p$ | see below |
| "$p$ whenever $q$" | $q \to p$ | synonym of "if" |
| "$p$ provided that $q$" | $q \to p$ | synonym of "if" |

### The arrow rule, stated once

The arrow **points at the condition**. "Only if" and "if" are synonyms that live on opposite sides of the consequent.

- "$p$ **only if** $q$" reads as "$p$ holds, and this depends on $q$", so $p \to q$. Rosen's own example: "You can access the Internet from campus only if you are a computer science major or you are not a freshman" becomes $a \to (c \vee \neg f)$ (Rosen, §1.2, Example 1, p. 17).
- "$p$ **if** $q$" reads as "$q$ is the condition, and $p$ follows", so $q \to p$.
- The two are **not** interchangeable. Confusing them is the single most common translation error.

### The "unless" trap, in full

"$B$ unless $A$" means **if not $A$, then $B$**. So the translation is $\neg A \to B$. That form then rewrites three ways, all equivalent:

$$
\neg A \to B \;\equiv\; \neg(\neg A) \lor B \;=\; A \lor B \;\equiv\; \neg B \to A
$$

| Form | Use it when |
| :-- | :-- |
| $\neg A \to B$ | the sentence is about "failing $A$ leads to $B$" |
| $A \lor B$ | you need $\lor$ notation only |
| $\neg B \to A$ | you want to match a conditional written the other way |

> [!WARNING] "unless" is never a biconditional
> Reading "$B$ unless $A$" as $A \leftrightarrow B$ claims both directions. The sentence only asserts one. CT-04 Q.3(a) is built around this exact point: reading "unless" as an implication in the forward direction makes statement 2 collapse into statement 1 and add nothing, which is the signal that the reading is backwards.

### The "only if" trap, in full

"$P$ only if $Q$" is $P \to Q$, never $Q \to P$. But English is looser than logic here, and Rosen says so:

> "You should be aware that biconditionals are not always explicit in natural language. In particular, the 'if and only if' construction used in biconditionals is rarely used in common language. Instead, biconditionals are often expressed using an 'if, then' or an 'only if' construction. The other part of the 'if and only if' is implicit." — Rosen, §1.1 (p. 12)

So in everyday speech "If you finish your meal, then you can have dessert" usually **means** $P \leftrightarrow Q$. In an exam translation question, you must decide whether the sentence carries the implied converse. The safe reading is the literal one, and the safe answer states which reading you took. Write one line: "Taking the sentence literally, since only 'if' appears, this is a one-way implication."

### Translation traps in one glance

| Trap | Wrong | Right |
| :-- | :-- | :-- |
| "A only if B" | $B \to A$ | $A \to B$ |
| "B unless A" | $A \leftrightarrow B$ | $\neg A \to B \equiv A \lor B$ |
| "neither A nor B" | $\neg(A \land B)$ | $\neg A \land \neg B$ |
| "not (A and B)" | $\neg A \land \neg B$ | $\neg(A \land B) \equiv \neg A \lor \neg B$ |
| dropping a bracket | $\neg p \lor \neg q \lor r \land \neg r$ | bracket the outer conjunction |
| "but" | $\lor$ | $\land$ |

> [!NOTE] "but" is a conjunction, not a disjunction
> "A but not B" is $A \land \neg B$. "Either A or B, but not both" is $A \oplus B$. Fahad's Class-13 industrial specification treats "However" as $\land$ and "or ... but not both" as $\oplus$.

### Class-note translation specimens

Fahad Class-13 Example 2. "The system will operate in normal mode if and only if the primary controller or the backup controller is active, but not both. However, if the emergency sensor is triggered, then the system will enter emergency mode only if both controllers are inactive."

| Symbol | Meaning |
| :-- | :-- |
| $r$ | system operates in normal mode |
| $p$ | primary controller is active |
| $q$ | backup controller is active |
| $t$ | emergency sensor is triggered |
| $s$ | system enters emergency mode |

Parsing: "if and only if" gives $\leftrightarrow$; "or ... but not both" gives $\oplus$; "However" gives $\land$; "only if" gives $\to$; "both inactive" gives $\neg p \land \neg q$.

$$
r \leftrightarrow (p \oplus q) \land (t \to (s \to (\neg p \land \neg q)))
$$

Raidah's §3 carries the same example, so it is a repeat, not a one-off.

---

## DM-3.7: System Specification and Consistency

A **system specification** is a list of sentences describing what a system must do. Translating each one gives a set of formulas. Then one of three things is true.

| Result | Meaning | What you say |
| :-- | :-- | :-- |
| some row satisfies all | **consistent** | "the specifications are consistent" |
| no row satisfies all | **inconsistent** | "the specifications are inconsistent, no assignment satisfies all" |
| rows exist but the system must never be in them | **consistent but incomplete** | add a sentence closing the gap |

The third case is the one students miss. CT-04 Q.3 turns out to be exactly that.

### Two ways to test consistency

1. **Truth table.** Build one column per sentence, then a final "all" column. Any T in the final column means consistent.
2. **Chase.** Force values from the most restrictive sentence outward. Faster, and it reads well in the exam.

### Worked Example (PYQ 2024 Q.5(c))

> **Source:** 2024 Q.5(c)

**Question.** Are these system specifications consistent?

> The system is in multiuser state if and only if it is operating normally, the kernel is functioning. The kernel is not functioning or the system is in interrupt mode. If the system is not in multiuser state, then it is in interrupt mode. The system is not in interrupt mode.

**Assign variables**

| Symbol | Meaning |
| :-- | :-- |
| $p$ | system is in multiuser state |
| $q$ | kernel is functioning |
| $r$ | system is in interrupt mode |

**Translate each sentence.**

1. "in multiuser state if and only if it is operating normally, the kernel is functioning": $p \leftrightarrow q$
2. "The kernel is not functioning or the system is in interrupt mode": $\neg q \lor r$
3. "If the system is not in multiuser state, then it is in interrupt mode": $\neg p \to r$, which is $p \lor r$
4. "The system is not in interrupt mode": $\neg r$

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

**Reason without a table.** Specification 4 forces $r = F$. Specification 2 then forces $\neg q$, so $q = F$. Specification 1 forces $p = F$. Specification 3 then reads $p \lor r = F \lor F = F$, a contradiction.

$$
\boxed{\text{The specifications are INCONSISTENT: no assignment satisfies all four}}
$$

> [!warning] Where the contradiction comes from
> Sentence 4 says the system is **never** in interrupt mode. Sentence 2 then forces the kernel to be broken. Sentence 1 ties multiuser state to a working kernel, so the system cannot be in multiuser state either. Sentence 3 says a system that is not in multiuser state must be in interrupt mode, which sentence 4 has already ruled out. The set describes a machine that cannot exist. In practice this means one of the four requirements is a typo, usually sentence 4.

**A shorter chase than the paper used.** Sentence 2 is $\neg q \lor r$, and sentence 4 gives $\neg r$. From $\neg q \lor r$ and $\neg r$, disjunctive syllogism forces $\neg q$, so $q = F$. Sentence 1 is $p \leftrightarrow q$, so $q = F$ forces $p = F$. Sentence 3 is $\neg p \to r$, which with $p = F$ reads $T \to r$, forcing $r = T$. But sentence 4 says $\neg r$. Contradiction. Same verdict, six lines, no table.

---

## 🏆 Golden Questions (Past Exam Archive)

### 🎯 CT-04 Q.2(a): Translate the requirement into propositional logic
> **Appeared:** CT-04 Q.2(a) — (marks not printed in source)

*"A student can start the examination if and only if the student is authenticated and the examination server is available."*

With $p$: authenticated, $q$: server available, $r$: can start the examination:

$$
\boxed{r \leftrightarrow (p \land q)}
$$

The connective matters and is fixed by one word. "**if and only if**" is a biconditional, $\leftrightarrow$, and the compound $p \land q$ is its whole right side. So the requirement says both

$$
(p \land q) \to r \qquad \text{and} \qquad r \to (p \land q)
$$

Reading it as a one-way implication, $(p \land q) \to r$, states only half the requirement and permits a student to start the examination who is not authenticated, which is precisely what the sentence forbids.

**The complete truth table.**

| $p$ | $q$ | $r$ | $p \land q$ | $r \leftrightarrow (p \land q)$ |
| :-: | :-: | :-: | :-: | :-: |
| T | T | T | T | **T** |
| T | T | F | T | **F** |
| T | F | T | F | **F** |
| T | F | F | F | **T** |
| F | T | T | F | **F** |
| F | T | F | F | **T** |
| F | F | T | F | **F** |
| F | F | F | F | **T** |

$$
\boxed{r \leftrightarrow (p \land q) \text{ is true in 4 of 8 rows, so it is contingent}}
$$

It is not a tautology: rows 2, 3 and 5 are false. Nor is it a contradiction: rows 1, 4, 6 and 8 are true. A statement that permits four assignments is contingent, and that is the honest classification of this requirement.

> [!info] What the four true rows mean
> The formula holds when $r$ matches $p \land q$: the student may start exactly when both conditions hold. Rows 1 and 4 are the interesting pair, because they are the only ones where $r$ and $p \land q$ agree, and they are what the requirement asserts and nothing else. Rows 2 and 5 are the states the system must **prevent**: an authenticated student with an available server who cannot start, and an unauthenticated student who can.
>
> The second is the security case, and it is the reason the biconditional is written at all. A one-way implication would leave row 5 permitted.

**Follow-on parts of the same CT question, in brief.** Part (b) rewrote the biconditional using only $\neg, \lor, \land$, giving $(\neg p \lor \neg q \lor r) \land (\neg r \lor p \land q)$. Part (c) built the ten-column truth table of that rewritten form and returned the same four true rows, 1, 4, 6 and 8. Both parts are in [DM-3.8](DM-3.8_Normal_Forms_and_Functional_Completeness.md) and [DM-3.2](DM-3.2_Logical_Connectives_and_Truth_Tables.md), where they were already answered in Phase 7.

---

### 🎯 CT-04 Q.3(a): Translate all three statements into propositional logic
> **Appeared:** CT-04 Q.3(a) — (marks not printed in source)

With $p$: the sensor is active, $q$: the controller receives data.

**Statement 1.** "If the sensor is active, then the controller receives data."

$$
S_1 = p \to q
$$

**Statement 2.** "The controller does not receive data **unless** the sensor is active."

The word "unless" is the whole difficulty. "$B$ unless $A$" means *if not $A$, then $B$*, which is $\neg A \to B$, and equivalently $A \lor B$. Here $A$ = the sensor is active, $p$; $B$ = the controller receives data, $q$. So

$$
S_2 = \neg p \to q \quad\equiv\quad p \lor q \quad\equiv\quad q \to p
$$

**Statement 3.** "The sensor is active if and only if the controller receives data."

$$
S_3 = p \leftrightarrow q
$$

> [!warning] "Unless" is not "if and only if", and the difference is the whole question
> Read "does not receive data unless the sensor is active" as "$q \to p$": receiving data requires an active sensor. Read instead as "$p \to q$" it collapses into statement 1 and the second statement adds nothing, which is a sign that the reading is wrong.
>
> The three statements are therefore $p \to q$, $q \to p$ and $p \leftrightarrow q$, and the first two are already the two halves of the third. Statements 1 and 2 are **redundant**. That is not a defect in the question, it is the point: the specification states its central requirement twice, and a student who notices that has understood what the third statement adds, which is nothing.
>
> The related trap is reading "unless" as "$p \leftrightarrow q$". That would make the three statements a single biconditional and the specification vacuous.

---

### 🎯 CT-04 Q.3(b): Form a single compound proposition by taking the conjunction
> **Appeared:** CT-04 Q.3(b) — (marks not printed in source)

$$
C = S_1 \land S_2 \land S_3 = (p \to q) \land (q \to p) \land (p \leftrightarrow q)
$$

Replace the biconditional by its two implications:

$$
C = (p \to q) \land (q \to p) \land (p \to q) \land (q \to p)
$$

and since the first pair already contains both directions,

$$
\boxed{C = (p \to q) \land (q \to p)}
$$

$$
\boxed{C = (\neg p \lor q) \land (\neg q \lor p)}
$$

$$
\boxed{C = (\neg p \lor q) \land (\neg q \lor p) \equiv (p \land q) \lor (\neg p \land \neg q)}
$$

The last line is the distributive form: the conjunction is false in every row where exactly one of $p, q$ is true, and true only where they agree.

> [!info] Check by simplification, and by noting what was thrown away
> Simplifying $C$ gives $(p \land q) \lor (\neg p \land \neg q)$, which is exactly $p \leftrightarrow q$. So the conjunction of all three requirements is **equivalent to the third one alone**, because the third subsumes the first two.
>
> That is the correct and expected result, and it is worth stating plainly rather than presenting six conjuncts and leaving the reader to find the redundancy. The specification is satisfiable, and how it is satisfiable is the content of part (d).

---

### 🎯 CT-04 Q.3(c): Construct the complete truth table
> **Appeared:** CT-04 Q.3(c) — (marks not printed in source)

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

> [!info] The two true rows are the two consistent states
> Row 1: the sensor is active **and** the controller receives data. The system is working as intended.
>
> Row 4: the sensor is inactive **and** the controller receives nothing. The sensor is off, so nothing should arrive, and nothing does.
>
> Rows 2 and 3 are the failure modes: an active sensor with no data, which is a dead or disconnected sensor, and an inactive sensor with data, which means data is arriving from a sensor the system believes is off. The second of those is the dangerous one, since the controller would be acting on data it should treat as impossible.
>
> The table is also the check on part (b): the conjunction column matches the biconditional column in all four rows, which is what "the third statement subsumes the first two" means in a table.

---

### 🎯 CT-04 Q.3(d): Establish the truth assignments that satisfy all three requirements simultaneously
> **Appeared:** CT-04 Q.3(d) — (marks not printed in source)

Reading the $C$ column of the table in part (c), the conjunction is true in rows 1 and 4 only:

| assignment | $p$ | $q$ | meaning | satisfies all three |
| :-- | :-: | :-: | :-- | :-: |
| 1 | **T** | **T** | sensor active, controller receives data | **yes** |
| 4 | **F** | **F** | sensor inactive, controller receives nothing | **yes** |

$$
\boxed{\text{The specification is satisfiable, and the satisfying assignments are exactly } (p,q) = (\mathrm{T},\mathrm{T}) \text{ and } (\mathrm{F},\mathrm{F})}
$$

$$
\boxed{\text{Equivalently: the requirements hold if and only if } p = q}
$$

**Check that no other assignment works.** Row 2, $p = \mathrm{T}, q = \mathrm{F}$, fails statement 2, since data does arrive while the sensor is inactive. Row 3, $p = \mathrm{F}, q = \mathrm{T}$, fails statement 1, since data arrives with no active sensor. Those two are the only rows excluded, and they are excluded by different statements, which is what makes the exclusion complete.

> [!info] Two ways to confirm this without the table
> **By cases on $p$.** If $p$ is true, statement 1 forces $q$ true. If $p$ is false, statement 2 reads $\neg p \to q$, whose antecedent is true, so it forces $q$ false. Either way $q = p$, giving exactly the two assignments above.
>
> **By the simplified form.** Part (b) gave $C \equiv (p \land q) \lor (\neg p \land \neg q)$, and $C$ holds precisely when $p$ and $q$ agree. Agreement of two propositions is exactly two assignments.
>
> All three routes agree, and the answer is a pair of assignments rather than a single state, which is the substantive finding: **the specification permits the system to be idle.** Nothing in the three requirements forces the sensor to be active.

> [!warning] The engineering conclusion, and what the specification fails to say
> If a system is required to be *monitoring* at all times, then $p$ must be true, and only row 1 survives: $(p, q) = (\mathrm{T}, \mathrm{T})$. But none of the three statements says that. They constrain the relationship between sensor and controller, not the state of the sensor.
>
> This is the substantive defect in the requirement, and it is the kind of thing a specification review exists to find. A fourth statement, "the sensor is active", or the operational condition that the system is powered and enabled, would close it. An idle state that satisfies every written requirement is not a contradiction in the logic; it is a gap in the requirement, and the truth table is what makes it visible.

---

## Exam Variants

| Year | Question | Task | Key Answer |
| :--- | :--- | :--- | :--- |
| 2024 Q.5(b) | Classify $(p \to q) \land (q \to r)$ | 8-row truth table, count T rows | $\boxed{\text{Satisfiable but not valid}}$ |
| 2023 Q.6(a) | Show $\neg(p \leftrightarrow q) \equiv (\neg p \leftrightarrow q)$ | truth table **and** algebraic proof | $\boxed{\neg(p \leftrightarrow q) \equiv (\neg p \leftrightarrow q)}$ |
| 2024 Q.5(c) | Are these four specifications consistent? | translate, 8 rows, contradiction chase | $\boxed{\text{The specifications are INCONSISTENT: no assignment satisfies all four}}$ |
| CT-04 Q.2(a) | Translate an exam-access requirement | biconditional plus 8-row table | $\boxed{r \leftrightarrow (p \land q)}$ |
| CT-04 Q.3(a) | Translate sensor/controller requirements | three formulas, "unless" trap | $S_2 = \neg p \to q \equiv p \lor q \equiv q \to p$ |
| CT-04 Q.3(b) | Conjoin the three requirements | expand, simplify, box | $\boxed{C = (\neg p \lor q) \land (\neg q \lor p) \equiv (p \land q) \lor (\neg p \land \neg q)}$ |
| CT-04 Q.3(c) | Truth table of the conjunction | 4 rows since 2 variables | $\boxed{C \text{ is true in rows 1 and 4, so it is contingent}}$ |
| CT-04 Q.3(d) | Assignments satisfying all three | read the table, confirm by cases | $\boxed{\text{Equivalently: the requirements hold if and only if } p = q}$ |

**PYQ coverage for DM-3.4, DM-3.5, DM-3.6, DM-3.7:** 4 exam questions plus 5 CT-04 parts, 9 blocks, 0 missing.

---

## ⚡ Exam Tips & Common Mistakes

1. **Write the variable table before anything else.** Four sentences means four rows of symbol and meaning. It costs thirty seconds and kills every polarity error.
2. **"unless" is $\neg A \to B$.** Not $A \to B$, not $A \leftrightarrow B$. Write all three equivalent forms on the page; examiners award the mark for recognizing the family.
3. **"only if" points the arrow at itself.** "$P$ only if $Q$" is $P \to Q$. If your arrow points the other way you have silently swapped the sentence.
4. **Never count T rows without saying so.** "Satisfiable but not valid" is only earned once you state the row count.
5. **A tautology is automatically satisfiable.** If the three options are offered as a menu, never answer "valid" and stop. Say "valid, and therefore also satisfiable".
6. **Bracket before you evaluate.** $\neg p \lor \neg q \lor r \land \neg r$ is not the same formula as its bracketed self. Write brackets even when you think they are obvious.
7. **For inconsistency, chase rather than tabulate.** One forced value at a time is usually shorter than eight rows and reads as more confident.
8. **Redundancy is a finding, not a mistake.** CT-04 Q.3 has three requirements and two of them are implied by the third. Say so explicitly; it earns the part (b) mark in full.
9. **If the paper asks "algebraically", do not submit a truth table.** The 2023 question asked for both, and the algebraic half carries its own marks.

## 🔗 Related Topics

- [DM-3.2: Logical Connectives and Truth Tables](DM-3.2_Logical_Connectives_and_Truth_Tables.md) — the connective table and the row order used in every table here
- [DM-3.3: Tautology, Contradiction, Contingency](DM-3.3_Tautology_Contradiction_Contingency.md) — the three-way classification that "valid, satisfiable or unsatisfiable" is testing
- [DM-3.8: Normal Forms and Functional Completeness](DM-3.8_Normal_Forms_and_Functional_Completeness.md) — CNF as the third route to proving equivalence
- [DM-3.9: Rules of Inference and Valid Arguments](DM-3.9_Rules_of_Inference_and_Valid_Arguments.md) — the chase used to prove 2024 Q.5(c) inconsistent without a table
- [DM-3_Lower_b: Puzzles, Gates, Extensions](DM-3_Lower_b_Puzzles_Gates_Extensions.md) — next in the chain, where a compound proposition becomes a circuit

---

[← Previous: DM-3.9 Rules of Inference and Valid Arguments](DM-3.9_Rules_of_Inference_and_Valid_Arguments.md) | [🏠 Index](00_Index.md) | [Next: DM-3 Lower-b: Puzzles, Gates, Extensions →](DM-3_Lower_b_Puzzles_Gates_Extensions.md)