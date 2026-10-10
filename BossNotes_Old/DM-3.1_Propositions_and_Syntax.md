[← Previous: NM-10 Partial Differential Equations](NM-10_Partial_Differential_Equations.md) | [🏠 Index](00_Index.md) | [Next: DM-3.2 Logical Connectives and Truth Tables →](DM-3.2_Logical_Connectives_and_Truth_Tables.md)

---

# DM-3.1: Propositions and Syntax
> **Section:** B (Discrete Mathematics) | **Priority:** 🔴 | **Exam Frequency:** 2/3 DM papers (2022, 2024)
> **Sources:** Rosen §1.1 (pp. 1–2), Fahad Notes Class-12, Raidah Notes §2.1

## Why This Topic Matters

This is the doorway to the whole Discrete Mathematics half of the paper. Every logic question in Section B, from truth tables to rules of inference, rests on knowing what counts as a proposition and what does not. It has been asked twice in three years, both times as a short opening sub-question worth 2 or 3 marks. Learn the two tests and both questions are done.

---

## 📝 Key Definitions

> **Proposition:** "A **proposition** is a declarative sentence (that is, a sentence that declares a fact) that is either true or false, but not both." — Rosen, §1.1 (p. 1)

> **Propositional variable:** "We use letters to denote **propositional variables** (or **statement variables**), that is, variables that represent propositions, just as letters are used to denote numerical variables." — Rosen, §1.1 (p. 2)

> **Truth value:** "The **truth value** of a proposition is true, denoted by $\text{T}$, if it is a true proposition, and the truth value of a proposition is false, denoted by $\text{F}$, if it is a false proposition." — Rosen, §1.1 (p. 2)

> **Propositional logic:** "The area of logic that deals with propositions is called the **propositional calculus** or **propositional logic**. It was first developed systematically by the Greek philosopher Aristotle more than 2300 years ago." — Rosen, §1.1 (p. 2)

> **Compound proposition:** "New propositions, called **compound propositions**, are formed from existing propositions using logical operators." — Rosen, §1.1 (p. 2)

> **Not a proposition:** "Sentences 1 and 2 are not propositions because they are not declarative sentences. Sentences 3 and 4 are not propositions because they are neither true nor false." — Rosen, §1.1, Example 2 (p. 1)

---

## What Propositional Logic Is

**Propositional logic** is the study of statements that are either true or false, together with the connectives that build larger statements from them. It ignores the internal structure of a statement and cares only about its truth value.

So two sentences with completely different meanings can be treated as the same object in this logic. "The transistor conducts" and "$2 + 2 = 4$" look nothing alike, but both are just a single proposition that happens to be true. Once you name them, say $p$ and $q$, you can write $\neg p$, $p \land q$ and so on, and every tool of logic applies.

The payoff is that the whole subject becomes finite. One proposition has exactly two truth values. So $n$ propositional variables need exactly $2^n$ rows, and that table is a complete account of every case. Nothing is left out.

| Variables | Rows needed |
| :-: | :-: |
| 1 | 2 |
| 2 | 4 |
| 3 | 8 |
| 4 | 16 |
| $n$ | $2^n$ |

---

## What Is a Proposition

A proposition must pass **two** tests. That is the whole definition.

**Test 1, declarative.** The sentence asserts something. It does not command, ask or request.

**Test 2, has a truth value.** It is unambiguously true, or unambiguously false, but not both at once. Nothing may sit in between, and nothing may be undefined.

If both tests pass, it is a proposition. If either fails, it is not. No further requirement is asked. A proposition does not have to be meaningful to a beginner, does not have to be verifiable today, and carries no quantifier.

> [!NOTE] The "not both" clause is not decoration
> A statement cannot be true and false at the same time. That single rule is what makes a truth value well defined, and it is why "the present king of France is bald" fails. There is no such person, so the sentence is not false, and it is not true either. It has no truth value at all.

---

## Propositions and Non-Propositions

| Sentence | Proposition? | Reason |
| :-- | :-- | :-- |
| The transistor conducts | **Yes** | declarative and true or false |
| $2 + 2 = 4$ | **Yes** | declarative and true |
| $2 + 2 = 3$ | **Yes** | false is still a truth value |
| Water boils at $100^{\circ}$C at sea level | **Yes** | a fact, though it needs a reference condition |
| The sky is blue today | **Yes** | declarative |
| Close the window | No | imperative, a command |
| Is the door open | No | interrogative, a question |
| Please hand me the tool | No | a request |
| Read this carefully | No | not declarative |
| $x + 1 > 0$ | No | $x$ is free, so no truth value yet |
| $x + y = z$ | No | neither true nor false |
| The present king of France is bald | No | presupposes a non-existent referent |
| $1/0 = 3$ | No | meaningless, division by zero |

### The four tests, as a checklist

1. **Declarative.** It asserts rather than commands, asks or requests.
2. **Not interrogative.** No question mark in intent.
3. **Has a truth value.** Exactly one of true or false, with nothing in between.
4. **Meaningful.** Every symbol is defined, so the sentence can be evaluated.

> [!WARNING] The three rows that trip people up
> "$x + 1 > 0$" fails because $x$ is free, not because it is false. It becomes a proposition the moment $x$ is bound: "for every real $x$, $x + 1 > 0$".
>
> "The present king of France is bald" fails on truth value. It presupposes something that does not exist, so the sentence can be neither true nor false. That is a different failure from being undecidable in practice.
>
> "$1/0 = 3$" fails on meaningfulness. It is not false, it is not an equation between numbers at all.

---

## Proposition Versus Ordinary Sentence

This is the comparison 2022 Q.5(a) asks for directly.

**Proposition.** A declarative sentence that is unambiguously either true or false, with exactly one truth value.

**Traditional (ordinary) sentence.** Any statement of natural language. The category is much wider and admits sentences with no truth value at all.

| | Proposition | Ordinary sentence |
| :-- | :-- | :-- |
| What it is | A declarative sentence with a definite truth value | Any statement of natural language |
| How many | A narrow class | A very wide class |
| Truth value | Always exactly one | May have none |
| Examples | "The transistor conducts", "$2 + 2 = 4$" | also "Close the window", "Is the door open" |

So every proposition is an ordinary sentence, but not the other way round.

**What propositions are not.** A **compound proposition** is built from simple ones using $\neg, \land, \lor, \to, \leftrightarrow$. A **predicate** such as "$x$ is prime" is not a proposition on its own, because $x$ is free. Only after binding does it become one: "for every prime $x$, $x > 1$".

**Why the distinction matters.** Propositional logic can only reason over things with a definite truth value. A sentence like "close the window" has to be translated into one before any logical tool applies, and that translation step is where most real errors in control logic occur.

---

## Proposition Versus Propositional Variable

This is the comparison 2024 Q.5(a) asks for.

A **propositional variable**, written $p, q, r, s$, is a single letter standing for one whole proposition. The letter has no meaning of its own. It is a placeholder.

| | Proposition | Propositional variable |
| :-- | :-- | :-- |
| What it is | A declarative sentence with a definite truth value | A single letter standing for a proposition |
| Truth value | Has one of its own | Borrows the one it stands for |
| Example | "Cairo is the capital of Egypt" | $p$, standing for that statement |
| Not one | "Close the switch", an imperative with no truth value | |

**The difference in one line.** A proposition is the actual sentence. A propositional variable is the name given to it so that logical connectives can be written on paper.

$$
\text{Statement: "The system is in multiuser state"} \quad \Rightarrow \quad p
$$

Both are needed. The prose gives the physics, the letter gives the algebra.

---

## Atomic and Compound Propositions

**Atomic (simple) proposition.** One with no connective inside it. It is a single indivisible statement.

- "The transistor conducts" is atomic.
- "$2 + 2 = 4$ is true and the window is open" is not.

**Compound proposition.** Built from two or more atomic propositions joined by connectives.

$$
\underbrace{\neg p \lor (q \land r)}_{\text{one proposition, not three}}
$$

**Precedence.** When brackets are omitted, the operators bind in this order, strongest first:

| Operator | Precedence |
| :-: | :-: |
| $\neg$ | 1 |
| $\land$ | 2 |
| $\lor$ | 3 |
| $\to$ | 4 |
| $\leftrightarrow$ | 5 |

So $\neg p \land q$ means $(\neg p) \land q$ and not $\neg(p \land q)$. And $p \land q \lor r$ means $(p \land q) \lor r$. Write the brackets anyway. It costs nothing and removes every argument about what the question meant.

---

## Worked Example (PYQ 2022)

> **Source:** 2022 Q.5(a) [Marks: 03]

**Question.** Explain how proposition differs from traditional sentence. Give some examples.

**Answer.**

**Proposition.** A declarative sentence that is **unambiguously either true or false**, with exactly one truth value. Nothing more is required: it need not be meaningful, need not be verifiable today, and carries no quantifier.

**Traditional (ordinary) sentence.** Any statement of natural language. The category is much wider, admitting sentences that have no truth value at all.

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

**What propositions are not.** A **compound proposition** is built from simple ones using $\neg, \land, \lor, \to, \leftrightarrow$. A **predicate** such as "$x$ is prime" is not a proposition on its own, because $x$ is free. Only after binding, "for every prime $x$, $x > 1$", does it become one.

**Why the distinction matters.** Propositional logic can only reason over things with a definite truth value. A sentence like "close the window" has to be translated into one before any logical tool applies, and that translation step is where most real errors in control logic occur.

---

## 🏆 Golden Questions (Past Exam Archive)

### 🎯 Explain how proposition differs from traditional sentence. Give some examples.
> **Appeared:** 2022 Q.5(a) — (03 marks)

**Full Answer:**

**Proposition.** A declarative sentence that is **unambiguously either true or false**, with exactly one truth value. Nothing more is required. It need not be meaningful, need not be verifiable today, and carries no quantifier.

**Traditional sentence.** Any statement of natural language. The category is much wider, admitting sentences with no truth value at all.

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

> [!warning] The three rows that trip people up
> "$x + 1 > 0$" fails because $x$ is free, not because it is false. It becomes a proposition only once $x$ is bound: "for every real $x$, $x + 1 > 0$".
>
> "The present king of France is bald" fails because it presupposes something that does not exist, so the sentence can be neither true nor false. This is a different failure from being undecidable in practice; it has no truth value at all.
>
> "$1/0 = 3$" fails on meaningfulness. It is not false, it is not an equation between numbers.

> [!note] Propositions, compound propositions and predicates are three different things
> A **compound proposition** is built from simple ones using $\neg, \land, \lor, \to, \leftrightarrow$.
>
> A **predicate** such as "$x$ is prime" is not a proposition on its own, because $x$ is free. Binding it gives one.
>
> Propositional logic can only reason over things with a definite truth value, so anything else has to be translated into propositions first. That translation step is where most real errors in control logic occur, which is why the distinction is worth two marks of care rather than a definition to memorise.

---

### 🎯 Define propositional logic and explain the difference between a proposition and propositional variable.
> **Appeared:** 2024 Q.5(a) — (02 marks)

**Full Answer:**

**Propositional logic** is the branch of logic that deals with propositions, which are declarative statements that are either true or false, and with the connectives that combine them. Unlike first-order logic it does not look inside a proposition: it treats each one as a single indivisible unit and studies how the truth values of whole propositions combine.

**A proposition** is a declarative sentence that has a definite truth value. "Swift is a functional language" is a proposition. So is "The bridge opened." The two essential requirements are that the sentence is declarative rather than interrogative or imperative, and that it is unambiguously either true or false. "Jaffna is a city in the world" is true. "Cairo is the capital of Egypt" is true. "Are you hungry?" is not a proposition at all, because it is a question and has no truth value.

**A propositional variable** is a symbol, usually $p, q, r$, that stands for a proposition. The variable does not have a truth value by itself: it takes the truth value of the proposition it represents. The propositional variable $p$ in the formula $p \to q$ is a placeholder; the propositions are the statements behind $p$ and behind $q$.

**The difference in one sentence.** A proposition is a *statement* with a truth value; a propositional variable is a *name* for one, whose own truth value depends on which proposition it names.

| | Proposition | Propositional variable |
| :-- | :-- | :-- |
| What it is | A declarative sentence with a definite truth value | A single letter standing for a proposition |
| Truth value | Has one of its own | Borrows the one it stands for |
| Example | "Cairo is the capital of Egypt" | $p$, standing for that statement |
| Not one | "Close the switch", an imperative with no truth value | |

$$
\text{Proposition} = \text{declarative statement with a definite truth value}; \ \text{variable} = \text{its symbol}
$$

**Why the distinction matters.** It is the reason a truth table can be finite. A single proposition has two possible truth values, so $n$ propositional variables need $2^n$ rows to enumerate, which is a finite and complete account. If propositions were allowed to be compound in arbitrary ways, no finite table would suffice.

---

## Exam Variants

| Year | Question | Data Given | Key Answer |
| :--- | :--- | :--- | :--- |
| 2022 Q.5(a) | Proposition vs. traditional sentence | definition plus examples | two tests, 4-step checklist, 9-row example table |
| 2024 Q.5(a) | Define propositional logic, proposition vs. propositional variable | definition plus a 6-row example table | $p$ is a placeholder, statement is the sentence |

---

## ⚡ Exam Tips & Common Mistakes

1. **Two tests, not one.** Students check only "declarative". A declarative sentence with no truth value, such as "$x + 1 > 0$", still fails. Say both conditions out loud.
2. **Never judge by meaning.** A meaningless sentence like "$1/0 = 3$" still looks declarative, and it is still not a proposition, because it cannot be evaluated.
3. **The answer to "difference between proposition and ordinary sentence" is a superset relation.** Every proposition is an ordinary sentence. Not the reverse. Say it explicitly.
4. **The answer to "proposition vs. propositional variable" is one of object vs. name.** The variable has no truth value of its own. That single clause earns the mark.
5. **Give a table, not a list.** Both years asked for examples, and a table with a "reason" column answers more per line than a bullet list does.
6. **Do not mix up "not a proposition" with "false".** "$2+2=3$" is a proposition. It is just a false one. Confusing the two is the most expensive slip in this topic.

## 🔗 Related Topics

- [DM-3.2: Logical Connectives and Truth Tables](DM-3.2_Logical_Connectives_and_Truth_Tables.md) — next in the chain, where these propositions get joined together
- [DM-3.3: Tautology, Contradiction, Contingency](DM-3.3_Tautology_Contradiction_Contingency.md) — classifies the compound propositions built here
- [DM-3_Lower_a: Validity, Equivalence, Translation](DM-3_Lower_a_Validity_Equivalence_Translation.md) — the "unless" and "only if" traps in full English translation

---

[← Previous: NM-10 Partial Differential Equations](NM-10_Partial_Differential_Equations.md) | [🏠 Index](00_Index.md) | [Next: DM-3.2 Logical Connectives and Truth Tables →](DM-3.2_Logical_Connectives_and_Truth_Tables.md)
