---
title: "DM-3.8 · Normal Forms & Functional Completeness"
tags:
  - numerical-methods
  - discrete-mathematics
  - topicwise
---

# DM-3.8 · Normal Forms & Functional Completeness

Every block below is copied from `../answers_exam_style/`, which is the
only place an answer is authored. A number here is the same number, character
for character, as the one it came from.


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
