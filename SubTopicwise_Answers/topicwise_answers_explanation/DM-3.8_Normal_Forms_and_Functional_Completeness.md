---
title: "DM-3.8 · Normal Forms & Functional Completeness"
tags:
  - numerical-methods
  - discrete-mathematics
  - topicwise
---



[🏠 Subtopic Index](00_Index.md) | [← Prev: DM-3.7 System Specification & Consistency](DM-3.7_System_Specification_and_Consistency.md) | [Next: DM-3.9 Rules of Inference & Valid Arguments →](DM-3.9_Rules_of_Inference_and_Valid_Arguments.md)

---

# DM-3.8 · Normal Forms & Functional Completeness

Every block below is copied from `../answers_explanation/`. The reasoning
is written once, in the year-wise file, and is not restated here.


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

[🏠 Subtopic Index](00_Index.md) | [← Prev: DM-3.7 System Specification & Consistency](DM-3.7_System_Specification_and_Consistency.md) | [Next: DM-3.9 Rules of Inference & Valid Arguments →](DM-3.9_Rules_of_Inference_and_Valid_Arguments.md)
