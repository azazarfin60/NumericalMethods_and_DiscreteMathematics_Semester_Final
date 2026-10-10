[← Previous: DM-3.3 Tautology, Contradiction, Contingency](DM-3.3_Tautology_Contradiction_Contingency.md) | [🏠 Index](00_Index.md) | [Next: DM-3.9 Rules of Inference and Valid Arguments →](DM-3.9_Rules_of_Inference_and_Valid_Arguments.md)

---

# DM-3.8: Normal Forms and Functional Completeness
> **Section:** B (Discrete Mathematics) | **Priority:** 🔴 | **Exam Frequency:** 3/4 DM sources (2022, 2024, CT-04 Q.2(b))
> **Sources:** Shishir Notes §7.2 and §8 (pp. 54–57), Rosen §1.2–1.3, Raidah Notes §2.9

## Why This Topic Matters

Normal forms are the shapes you can rewrite any formula into without changing what it means. They are what automatic theorem provers read, what hardware designers build, and what turns a messy specification into something checkable. Functional completeness is the companion question: which connectives are enough to build all the rest. Both were asked in 2022 and again in 2024, and the CT asked for a rewrite using only $\neg, \lor, \land$.

---

## 📝 Key Definitions

> **Disjunctive Normal Form:** "A statement form that consists of a **disjunction of conjunctions** (a sum of products) is called **Disjunctive Normal Form (DNF)**:
> $\bigvee_i \left( \bigwedge_j l_{ij} \right)$ where each $l_{ij}$ is a literal (a variable $p$ or its negation $\sim p$)." — Shishir Notes §7.2 (p. 54)
>
> **Example:** $(p \land q) \lor q \lor (\sim q \land p)$

> **Conjunctive Normal Form:** "A statement form that consists of a **conjunction of disjunctions** (a product of sums) is called **Conjunctive Normal Form (CNF)**:
> $\bigwedge_i \left( \bigvee_j l_{ij} \right)$ where each clause is a disjunction of literals." — Shishir Notes §7.2 (p. 54)
>
> **Example:** $(p \lor q) \land (\sim p \lor q) \land (\sim q)$

> **Functionally complete:** "A collection of operators is **functionally complete** if every other Boolean operator can be expressed using only those operators." — `topicwise_answers_exam_style/DM-3.8`, 2022 Q.5(c)

> **Literal:** a variable $p$ or its negation $\neg p$. The building block of both normal forms.

> **The rewrites you will need first:** $p \to q \equiv \neg p \lor q$ and $p \leftrightarrow q \equiv (\neg p \lor q) \land (\neg q \lor p)$ — Rosen §1.3, Tables 7 and 8

---

## DNF: Sum of Products

A formula is in **DNF** when it is a disjunction of conjunctions of literals.

$$
(l_{11} \land l_{12} \land \cdots) \lor (l_{21} \land l_{22} \land \cdots) \lor \cdots
$$

Read it as: **any one of these conditions is enough.**

**Minimal DNF.** Every clause is a conjunction of literals, but not necessarily of all variables. This is the shape you get from reading the English of a specification.

**Canonical DNF.** Every clause is a **minterm**: it contains every variable exactly once, either positive or negated. It has $2^n$ rows available and is unique.

| | Minimal DNF | Canonical DNF |
| :-- | :-- | :-- |
| Clauses | Conjunctions of some literals | Minterms, all $n$ variables |
| Uniqueness | Not unique | **Unique** |
| Clause count | Fewer | One per row where the formula is T |
| Used for | Fast evaluation, hardware | Proof, comparison |

## CNF: Product of Sums

A formula is in **CNF** when it is a conjunction of disjunctions of literals.

$$
(l_{11} \lor l_{12} \lor \cdots) \land (l_{21} \lor l_{22} \lor \cdots) \land \cdots
$$

Read it as: **all of these conditions must hold.**

**Minimal CNF.** Every clause is a disjunction of some literals.

**Canonical CNF.** Every clause is a **maxterm**: all $n$ variables, one per row where the formula is false, with each value negated.

| | Minimal CNF | Canonical CNF |
| :-- | :-- | :-- |
| Clauses | Disjunctions of some literals | Maxterms, all $n$ variables |
| Uniqueness | Not unique | **Unique** |
| Clause count | Fewer | One per row where the formula is F |
| Used for | Reading failure conditions | Resolution, automated provers |

---

## Building a Normal Form from a Truth Table

This is the method that earns full marks. It is mechanical and it cannot go wrong.

### Canonical DNF, from the table

Take **every row where the formula is T**. For each such row write the minterm for that row. Join them with $\lor$.

> **How to read the minterm for a row.** Write all the variables in the same order every time. If the value in the row is T write the variable plain, if it is F write it negated.

### Canonical CNF, from the table

Take **every row where the formula is F**. For each such row write the maxterm for that row. Join them with $\land$.

> **How to read the maxterm for a row.** Same variable order. If the value in the row is **T** write the variable **negated**, if it is **F** write it plain. That is the exact opposite of the minterm rule, and the reason is simple: the maxterm must be false on that row and true on every other row.

### Worked example

Build both forms of $(p \lor \neg q) \to (p \land q)$.

| $p$ | $q$ | $\neg q$ | $p \lor \neg q$ | $p \land q$ | $(p \lor \neg q) \to (p \land q)$ |
| :-: | :-: | :-: | :-: | :-: | :-: |
| T | T | F | T | T | **T** |
| T | F | T | T | F | **F** |
| F | T | F | F | F | **T** |
| F | F | T | T | F | **F** |

**Canonical DNF.** The T rows are row 1 and row 3.

$$
(p \land q) \lor (\neg p \land q)
$$

**Minimal DNF.** $q$ is common to both clauses, so factor it out: $(p \lor \neg p) \land q \equiv q$.

$$
\text{minimal DNF} = q
$$

**Canonical CNF.** The F rows are rows 2, 3 and 4.

| row | $p$ | $q$ | maxterm |
| :--: | :-: | :-: | :-- |
| 2 | T | F | $(\neg p \lor q)$ |
| 3 | F | T | $(p \lor \neg q)$ |
| 4 | F | F | $(p \lor q)$ |

$$
\text{canonical CNF} = (\neg p \lor q) \land (p \lor \neg q) \land (p \lor q)
$$

> [!NOTE] Check the DNF against the table
> The minimal DNF is $q$, and $q$ is T in rows 1 and 3, exactly the rows where the formula is T. ✓

---

## Building a Normal Form Algebraically

Push every $\to$ and $\leftrightarrow$ into $\neg, \lor, \land$ first, then push every negation down to the variables, then distribute.

### Four worked conversions from Shishir's notes

**Step 1. DNF of $(p \to q) \land (q \to p)$**

$$
\begin{aligned}
(p \to q) \land (q \to p) &\equiv (\neg p \lor q) \land (\neg q \lor p) && \text{[Implication Equivalence]} \\
&\equiv \Big[(\neg p \lor q) \land \neg q\Big] \lor \Big[(\neg p \lor q) \land p\Big] && \text{[Distributive Law]} \\
&\equiv \Big[(\neg p \land \neg q) \lor (q \land \neg q)\Big] \lor \Big[(\neg p \land p) \lor (q \land p)\Big] && \text{[Distributive Law]} \\
&\equiv \Big[(\neg p \land \neg q) \lor \mathbf{F}\Big] \lor \Big[\mathbf{F} \lor (p \land q)\Big] && \text{[Contradiction Law]} \\
&\equiv (\neg p \land \neg q) \lor (p \land q) && \text{[Identity Law: } X \lor \mathbf{F} \equiv X]
\end{aligned}
$$

**Step 2. CNF of $p \land (p \to q)$**

$$
\begin{aligned}
p \land (p \to q) &\equiv p \land (\neg p \lor q) && \text{[Implication Equivalence]} \\
&\equiv (p \land \neg p) \lor (p \land q) && \text{[Distributive Law]} \\
&\equiv \mathbf{F} \lor (p \land q) && \text{[Contradiction Law]} \\
&\equiv p \land q && \text{[Identity Law]}
\end{aligned}
$$

**Step 3. DNF of $\big(p \land (p \to q)\big) \to q$**

$$
\begin{aligned}
\big(p \land (p \to q)\big) \to q &\equiv \big(p \land (\neg p \lor q)\big) \to q && \text{[Implication Equivalence]} \\
&\equiv \neg\big(p \land (\neg p \lor q)\big) \lor q && \text{[Implication Equivalence]} \\
&\equiv \Big(\neg p \lor \neg(\neg p \lor q)\Big) \lor q && \text{[De Morgan's Law]} \\
&\equiv \neg p \lor (p \land \neg q) \lor q && \text{[De Morgan's \& Double Negation]}
\end{aligned}
$$

**Step 4. DNF of $\big((p \to q) \land (q \to p)\big) \lor p$**

$$
\begin{aligned}
\big((\neg p \lor q) \land (\neg q \lor p)\big) \lor p &\equiv p \lor \big((\neg p \lor q) \land (\neg q \lor p)\big) && \text{[Commutative Law]} \\
&\equiv \big(p \lor (\neg p \lor q)\big) \land \big(p \lor (\neg q \lor p)\big) && \text{[Distributive Law]} \\
&\equiv \big((p \lor \neg p) \lor q\big) \land \big((p \lor p) \lor \neg q\big) && \text{[Associative \& Idempotent]} \\
&\equiv (\mathbf{T} \lor q) \land (p \lor \neg q) && \text{[Negation Law]} \\
&\equiv \mathbf{T} \land (p \lor \neg q) && \text{[Domination Law]} \\
&\equiv p \lor \neg q && \text{[Identity Law]}
\end{aligned}
$$

> [!TIP] Notice the pattern in step 1
> The distributive law $P \land (Q \land R) \equiv (P \land Q) \land (P \land R)$ applied backwards is what turns a CNF into a DNF. Any formula can go either way; the law just has to be applied from the inside out.

### The distributive law checked by table

Every algebraic conversion above rests on this one law. It is worth being able to prove it directly:

![Hand-worked eight-row truth table proving p -> (q or r) and (p -> q) or (p -> r) are equivalent, the two columns matching in all rows](diagrams/dm3_equivalence_truth_table_handworked.jpg)

*The last two columns are identical in all eight rows, so the two formulas are logically equivalent. Two formulas with the same column are the same formula.*

---

## Functional Completeness

A collection of operators is **functionally complete** if every other Boolean operator can be expressed using only those operators.

### Proving $\{\neg, \land\}$ is complete

**Goal.** Build $\lor$ and $\to$ from $\neg$ and $\land$ alone.

**Step 1. Disjunction by De Morgan.** Since $\neg(p \land q) = \neg p \lor \neg q$,

$$
p \lor q = \neg(\neg p \land \neg q)
$$

**Step 2. Implication.** Since $p \to q \equiv \neg p \lor q$,

$$
p \to q = \neg p \lor q = \neg(\neg(\neg p) \land \neg q)
$$

**Step 3. Biconditional.** Since $p \leftrightarrow q \equiv (p \to q) \land (q \to p)$, substituting step 2 into both places gives it in terms of $\neg$ and $\land$ too.

**Step 4. Verify both against the truth tables.** Rows run $p$ outer and $q$ inner, each taking T then F.

| $p$ | $q$ | $\neg p$ | $\neg q$ | $p \lor q$ | $\neg(\neg p \land \neg q)$ | $p \to q$ | $\neg(\neg(\neg p) \land \neg q)$ |
| :-: | :-: | :-: | :-: | :-: | :-- | :-: | :-- |
| F | F | T | T | F | $\neg(T \land T) = F$ ✓ | T | $\neg(F \land T) = T$ ✓ |
| F | T | T | F | T | $\neg(T \land F) = T$ ✓ | T | $\neg(F \land F) = T$ ✓ |
| T | F | F | T | T | $\neg(F \land T) = T$ ✓ | F | $\neg(T \land T) = F$ ✓ |
| T | T | F | F | T | $\neg(F \land F) = T$ ✓ | T | $\neg(T \land F) = T$ ✓ |

Every constructed column matches its target column in all four rows.

**Step 5. Conclusion.** The operators $\neg$ and $\land$ generate $\lor$, $\to$, $\leftrightarrow$ and everything built from them, so the collection is functionally complete.

$$
\boxed{p \lor q = \neg(\neg p \land \neg q), \qquad p \to q = \neg(\neg(\neg p) \land \neg q)}
$$

> [!warning] Count the negations in the implication formula, they are easy to lose
> $p \to q \equiv \neg p \lor q$, and then $\neg p \lor q$ is already in disjunctive form, so it needs no De Morgan step at all. The formula $\neg(\neg(\neg p) \land \neg q)$ comes from rewriting $\neg p$ as $\neg(\neg(\neg p))$ so that both operands of $\lor$ sit under negations.
>
> Dropping one of the three negations on $p$ gives a formula that looks perfectly reasonable and is false on the row $p = T, q = F$. That single row is the whole test, and the table above is where it is caught.

### Proving $\{\neg, \lor\}$ is complete

By the same method, using $\neg(p \lor q) \equiv \neg p \land \neg q$:

$$
p \land q = \neg(\neg p \lor \neg q)
$$

$$
p \to q = \neg p \lor q \qquad \text{(already in the set)}
$$

So $\{\neg, \lor\}$ is complete as well.

### The two minimal complete sets, and why nothing smaller works

> **Minimal complete sets:** There are exactly two: $\{\neg, \land\}$ and $\{\neg, \lor\}$. Neither $\land$ nor $\lor$ alone is complete, since neither can produce negation, and a set without negation cannot realise $p \lor \neg p$, which is a tautology and so must be constantly true. This is why every functionally complete set must contain $\neg$ or something that implies it.

**NAND alone is enough.** With $p \mid q = \neg(p \land q)$:

$$
\neg p \equiv p \mid p, \qquad p \land q \equiv (p \mid q) \mid (p \mid q)
$$

So $\{\mid\}$ is functionally complete on its own. That is why a processor can be built from one gate type.

![Inverter, OR gate and AND gate, the three primitives behind functional completeness](diagrams/dm3_not_and_or_gates.jpg)

*Rosen §1.2, p. 21. Negation, conjunction and disjunction are the physical gates that $\neg, \land, \lor$ correspond to.*

---

## Worked Example (PYQ 2022)

> **Source:** 2022 Q.5(c) [Marks: 02]

**Question.** Show that $\neg$ and $\land$ form a functionally complete collection of logical operators.

**Answer.**

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
each taking T then F.

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

> [!note] The minimal complete sets
> There are exactly two minimal functionally complete sets: $\{\neg, \land\}$ and $\{\neg, \lor\}$. Neither $\land$ nor $\lor$ alone is complete, since neither can produce negation, and a set without negation cannot realise $p \lor \neg p$, which is a tautology and so must be constantly true.

---

## Worked Example (PYQ 2024)

> **Source:** 2024 Q.6(b) [Marks: 06]

**Question.** A security system triggers an alarm if (a) motion is detected and the window is open, or (b) the door sensor is active but the security code is not entered. (i) Assign propositional variables, (ii) express the alarm condition as a single proposition, (iii) convert it into both CNF and DNF, describing each transformation step.

**Answer.**

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

> [!note] Which form to use
> **CNF** suits resolution and automated theorem provers, which read conjunctions of disjunctions directly. **DNF** suits fast evaluation and hardware implementation, because each product can be tested in isolation and the first one that succeeds ends the computation. The CNF here also reads as four independent failure conditions: for no alarm, motion must be absent or the door inactive, the door must be active or no motion seen, the window must be shut or the door inactive, and the window must be shut or the code entered.

---

## 🏆 Golden Questions (Past Exam Archive)

### 🎯 Show that $\neg$ and $\land$ form a functionally complete collection of logical operators.
> **Appeared:** 2022 Q.5(c) — (02 marks)

**Full Answer:**

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
substituting step 2 in both places expresses it in terms of $\neg$ and $\land$ too.

**Step 4. Verify against the truth tables.** Rows run $p$ outer, $q$ inner, each
taking T then F.

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

$$
\boxed{p \lor q = \neg(\neg p \land \neg q), \qquad p \to q = \neg(\neg(\neg p) \land \neg q)}
$$

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

### 🎯 CT-04 Q.2(b). Rewrite the resulting expression using only $\neg$, $\lor$, and $\land$.
> **Appeared:** CT-04 Q.2(b) — (marks not printed in source)

**Full Answer:**

Start from $r \leftrightarrow (p \land q)$ and replace the biconditional by its
two implications:

$$
r \leftrightarrow (p \land q) \equiv \big[(p \land q) \to r\big] \land \big[r \to (p \land q)\big]
$$

Replace each implication by $P \to Q \equiv \neg P \lor Q$:

$$
\equiv \big[\neg(p \land q) \lor r\big] \land \big[\neg r \lor (p \land q)\big]
$$

Apply De Morgan's law $\neg(p \land q) \equiv \neg p \lor \neg q$ to the first
bracket:

$$
\boxed{\big[(\neg p \lor \neg q) \lor r\big] \land \big[\neg r \lor (p \land q)\big]}
$$

$$
\boxed{\equiv (\neg p \lor \neg q \lor r) \land (\neg r \lor p \land q)}
$$

which uses only $\neg$, $\lor$ and $\land$, as required.

**Step by step, with the law named at each move:**

$$
\begin{aligned}
r \leftrightarrow (p \land q)
  &\equiv \big[(p \land q) \to r\big] \land \big[r \to (p \land q)\big]
    && \text{biconditional as two implications}\\
  &\equiv \big[\neg(p \land q) \lor r\big] \land \big[\neg r \lor (p \land q)\big]
    && P \to Q \equiv \neg P \lor Q\\
  &\equiv \big[(\neg p \lor \neg q) \lor r\big] \land \big[\neg r \lor (p \land q)\big]
    && \text{De Morgan}\\
  &\equiv (\neg p \lor \neg q \lor r) \land (\neg r \lor p \land q)
    && \text{associativity of } \lor
\end{aligned}
$$

> [!tip] Check by truth table, on all eight rows
> The rewritten formula and $r \leftrightarrow (p \land q)$ are true in exactly
> the same four rows, 1, 4, 6 and 8, and false in the other four. Two formulas
> with the same table are the same formula, so the rewrite is correct.
>
> There is a check in the other direction, and it is the more satisfying one,
> because it shows the algebra preserved the *meaning*. The final form reads as a
> requirement rather than as algebra: $\neg p \lor \neg q \lor r$ says *something
> must fail or the student may start*, and $\neg r \lor p \land q$ says *if the
> student starts, both must hold*. Those are the two halves of "if and only if",
> recovered from the rewritten form.

> [!warning] The bracket that must not be dropped
> $(\neg p \lor \neg q \lor r) \land (\neg r \lor p \land q)$ is **not** the same
> as $\neg p \lor \neg q \lor r \land \neg r \lor p \land q$ without the outer
> brackets, because $\lor$ binds more weakly than $\land$. The outer conjunction
> is the whole statement: drop it and the formula becomes trivially true in rows
> where only one half is satisfied, and the requirement silently weakens to a
> single implication.
>
> Note also that $\neg r \lor p \land q$ parses as $\neg r \lor (p \land q)$,
> which is what is intended, since $\land$ binds tighter than $\lor$. Both
> readings are correct as written; they are not the same formula, and the one to
> quote is the bracketed pair.

---

## Exam Variants

| Year | Question | Task | Key Answer |
| :--- | :--- | :--- | :--- |
| 2022 Q.5(c) | Show $\{\neg, \land\}$ is functionally complete | build $\lor$, $\to$ from two primitives | $\boxed{p \lor q = \neg(\neg p \land \neg q), \qquad p \to q = \neg(\neg(\neg p) \land \neg q)}$ |
| 2024 Q.6(b) | Alarm specification | variables, DNF, CNF with every step | $\boxed{\text{CNF: } (m \lor d)\land(m \lor \neg s)\land(w \lor d)\land(w \lor \neg s)}$ |
| CT-04 Q.2(b) | Rewrite $r \leftrightarrow (p \land q)$ | using only $\neg, \lor, \land$ | $\boxed{\equiv (\neg p \lor \neg q \lor r) \land (\neg r \lor p \land q)}$ |

---

## ⚡ Exam Tips & Common Mistakes

1. **Name the law at every algebraic step.** 2024 Q.6(b) asks for "each transformation step" and CT-04 Q.2(b) is graded the same way. A chain with no annotations loses the marks even when the final line is right.
2. **Canonical DNF uses T rows, canonical CNF uses F rows.** This is the single rule that gets canonical forms built correctly the first time.
3. **Minterm rule: T plain, F negated.** Maxterm rule: T negated, F plain. They are exact opposites. Write both in your margin.
4. **State what each variable means positively.** Then let the negation fall where the English puts it. Defining $s$ to mean "the code is not entered" and then writing $\neg s$ flips the polarity against your own table.
5. **"But" is $\land$.** "Or" joining two branches is $\lor$. The contrast in "but" is rhetorical, not logical.
6. **Do not drop the outer brackets in a rewrite.** $\lor$ binds more weakly than $\land$, so removing them silently weakens the requirement to a single implication.
7. **Check both forms against the original on at least one row.** One row is enough to catch a dropped negation, which is the only realistic algebra error.

## 🔗 Related Topics

- [DM-3.2: Logical Connectives and Truth Tables](DM-3.2_Logical_Connectives_and_Truth_Tables.md) — the tables every normal form is read off
- [DM-3.3: Tautology, Contradiction, Contingency](DM-3.3_Tautology_Contradiction_Contingency.md) — the equivalence laws used in the algebraic route
- [DM-3.9: Rules of Inference](DM-3.9_Rules_of_Inference_and_Valid_Arguments.md) — the final topic in this chain
- [DM-3_Lower_b: Puzzles, Gates, Extensions](DM-3_Lower_b_Puzzles_Gates_Extensions.md) — where functional completeness becomes circuit design

---

[← Previous: DM-3.3 Tautology, Contradiction, Contingency](DM-3.3_Tautology_Contradiction_Contingency.md) | [🏠 Index](00_Index.md) | [Next: DM-3.9 Rules of Inference and Valid Arguments →](DM-3.9_Rules_of_Inference_and_Valid_Arguments.md)
