[← Previous: DM-3.11 Logic Gates](DM-3.11_Logic_Gates.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: DM-3.13 Fuzzy Logic →](DM-3.13_Fuzzy_Logic.md)

---

# DM-3.12: Predicates and Quantifiers

> ⚫ **Never examined.** This note exists for reading flow and complete syllabus coverage. Skim it to connect the ideas, but do not spend heavy study time here.

## What This Is

Propositional logic is powerful, but it has a severe limitation: it cannot look inside a sentence. It cannot express simple statements like "All microcontrollers have clock oscillators" or "Some integers are prime" because it treats entire sentences as indivisible letters ($p, q$).

Predicate logic (first-order logic) extends propositional logic by introducing **predicates** (properties that depend on a variable $x$) and **quantifiers** ("for all" $\forall$, and "there exists" $\exists$). This allows mathematics and computer science to reason about collections, data structures, and algorithms.

---

## 📝 Key Definitions

> **Predicate:** "A statement involving the variable $x$, denoted by $P(x)$, is called the value of the propositional function $P$ at $x$. Once a value has been assigned to the variable $x$, the statement $P(x)$ becomes a proposition and has a truth value." -- Rosen, §1.4, Predicates (p. 37)
>
> **In simple words:** A sentence with an open variable, like "$x > 3$". It is not a proposition on its own, but it becomes one the moment you plug in a specific number for $x$.

> **Universal Quantifier:** "The universal quantification of $P(x)$ is the statement 'P(x) for all values of $x$ in the domain.' The notation $\forall x P(x)$ denotes the universal quantification of $P(x)$. Here $\forall$ is called the universal quantifier." -- Rosen, §1.4, The Universal Quantifier (p. 40)
>
> **In simple words:** A claim that a property holds for every single element in your domain without exception. If even one element fails (a counterexample), the whole statement is false.

> **Existential Quantifier:** "The existential quantification of $P(x)$ is the proposition 'There exists an element $x$ in the domain such that $P(x)$.' We use the notation $\exists x P(x)$ for the existential quantification of $P(x)$. Here $\exists$ is called the existential quantifier." -- Rosen, §1.4, The Existential Quantifier (p. 42)
>
> **In simple words:** A claim that you can find at least one element in your domain that satisfies the property.

---

## Core Quantifier Rules

### 1. The Translation Rule: Universal vs Existential

When translating English sentences into formal logic:
- **Universal quantification naturally pairs with implication ($\to$):**
  "Every student in ECE passed the course":
$$
\forall x \, (\text{ECE}(x) \to \text{Passed}(x))
$$
  *(Why not AND? If you wrote $\forall x (\text{ECE}(x) \land \text{Passed}(x))$, that would assert that every person in the entire universe is an ECE student who passed!)*

- **Existential quantification naturally pairs with conjunction ($\land$):**
  "Some student in ECE has an oscilloscope":
$$
\exists x \, (\text{ECE}(x) \land \text{HasScope}(x))
$$
  *(Why not implication? If you wrote $\exists x (\text{ECE}(x) \to \text{HasScope}(x))$, that would be trivially true because anyone who is not an ECE student makes the hypothesis false, rendering the conditional vacuously true!)*

### 2. De Morgan's Laws for Quantifiers

Negating quantifiers flips the quantifier type and pushes the negation inside:

| Negated Statement | Equivalent Form | Plain Meaning |
|:---|:---|:---|
| $\neg \forall x P(x)$ | $\exists x \neg P(x)$ | "Not all $x$ satisfy $P$" means "there exists at least one $x$ that fails $P$". |
| $\neg \exists x P(x)$ | $\forall x \neg P(x)$ | "There does not exist any $x$ satisfying $P$" means "all $x$ fail $P$". |

---

## Nested Quantifiers

When multiple quantifiers appear together, their order matters:
- $\forall x \exists y \, (x + y = 0)$ means: "For every real number $x$, there exists an additive inverse $y$ such that $x + y = 0$." This is **TRUE** (pick $y = -x$).
- $\exists y \forall x \, (x + y = 0)$ means: "There is one universal magic number $y$ that when added to every number $x$ gives zero." This is **FALSE**.

Switching the order of $\forall$ and $\exists$ completely changes the meaning of the theorem.

---

## 🔗 Move On

This topic has never appeared in any RUET final exam paper (2017–2024). It exists in the syllabus as theoretical groundwork for formal proofs. 

If you are preparing for your semester final, skip directly ahead to [DM-3.13: Fuzzy Logic](DM-3.13_Fuzzy_Logic.md).

---

[← Previous: DM-3.11 Logic Gates](DM-3.11_Logic_Gates.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: DM-3.13 Fuzzy Logic →](DM-3.13_Fuzzy_Logic.md)
