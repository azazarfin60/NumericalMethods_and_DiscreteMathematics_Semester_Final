---
title: "DM-3.1 · Propositions & Syntax"
tags:
  - numerical-methods
  - discrete-mathematics
  - topicwise
---



[🏠 Subtopic Index](00_Index.md) | [← Prev: NM-10.5 Boundary Conditions in PDEs](NM-10.5_Boundary_Conditions_in_PDEs.md) | [Next: DM-3.2 Logical Connectives & Truth Tables →](DM-3.2_Logical_Connectives_and_Truth_Tables.md)

---

# DM-3.1 · Propositions & Syntax

Every block below is copied from `../answers_explanation/`. The reasoning
is written once, in the year-wise file, and is not restated here.


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

[🏠 Subtopic Index](00_Index.md) | [← Prev: NM-10.5 Boundary Conditions in PDEs](NM-10.5_Boundary_Conditions_in_PDEs.md) | [Next: DM-3.2 Logical Connectives & Truth Tables →](DM-3.2_Logical_Connectives_and_Truth_Tables.md)
