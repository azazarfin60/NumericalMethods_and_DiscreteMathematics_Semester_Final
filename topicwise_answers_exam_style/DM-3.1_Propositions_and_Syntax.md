---
title: "DM-3.1 · Propositions & Syntax"
tags:
  - numerical-methods
  - discrete-mathematics
  - topicwise
---

# DM-3.1 · Propositions & Syntax

Every block below is copied from `../answers_exam_style/`, which is the
only place an answer is authored. A number here is the same number, character
for character, as the one it came from.


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
