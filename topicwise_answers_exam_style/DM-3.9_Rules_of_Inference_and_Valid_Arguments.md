---
title: "DM-3.9 · Rules of Inference & Valid Arguments"
tags:
  - numerical-methods
  - discrete-mathematics
  - topicwise
---

# DM-3.9 · Rules of Inference & Valid Arguments

Every block below is copied from `../answers_exam_style/`, which is the
only place an answer is authored. A number here is the same number, character
for character, as the one it came from.


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
