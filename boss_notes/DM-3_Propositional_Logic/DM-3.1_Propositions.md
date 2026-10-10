[← Previous: DM-2.4 Equivalence Relations](../DM-2_Relations/DM-2.4_Equivalence_Relations.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: DM-3.2 Connectives and Truth Tables →](DM-3.2_Connectives_and_Truth_Tables.md)

---

# DM-3.1: Propositions

> 🔴 **Priority:** Critical | **Tested:** 2/3 DM final papers (2022, 2024) | **Typical marks:** 2 to 3

## What This Is (and Why It Matters)

This is the front doorway to the entire Discrete Mathematics section of the exam. Every topic in Section B, from truth tables to resolution proofs and logic puzzles, depends on knowing what counts as a proposition and what gets thrown out.

The semester final loves to use this as an easy opening question worth 2 or 3 marks right at the start of Section B. Examiners typically ask you to contrast a proposition with an ordinary natural sentence, or contrast a proposition with a propositional variable. If you memorize the two core tests and keep a few crisp examples ready, you can pick up these marks in less than three minutes.

---

## 📝 Key Definitions

> **Proposition:** "A proposition is a declarative sentence (that is, a sentence that declares a fact) that is either true or false, but not both." -- Rosen, §1.1 (p. 1)
>
> **In simple words:** A factual statement that is definitely true or definitely false. If it is a question, a command, an opinion, or an open algebraic formula with unknown variables, it is not a proposition.

> **Propositional variable:** "We use letters to denote propositional variables (or statement variables), that is, variables that represent propositions, just as letters are used to denote numerical variables." -- Rosen, §1.1 (p. 2)
>
> **In simple words:** A placeholder letter like $p$, $q$, or $r$ chosen to represent a full sentence so you can write formulas instead of long paragraphs.

> **Truth value:** "The truth value of a proposition is true, denoted by $\text{T}$, if it is a true proposition, and the truth value of a proposition is false, denoted by $\text{F}$, if it is a false proposition." -- Rosen, §1.1 (p. 2)
>
> **In simple words:** The status of the statement: either $\text{T}$ or $\text{F}$. Every proposition has exactly one truth value at any given moment.

> **Propositional logic:** "The area of logic that deals with propositions is called the propositional calculus or propositional logic. It was first developed systematically by the Greek philosopher Aristotle more than 2300 years ago." -- Rosen, §1.1 (p. 2)
>
> **In simple words:** The system of math that studies how whole propositions combine using logical operators like AND, OR, and NOT, without caring about the inner words inside the sentence.

> **Compound proposition:** "New propositions, called compound propositions, are formed from existing propositions using logical operators." -- Rosen, §1.1 (p. 2)
>
> **In simple words:** A bigger statement created by gluing smaller statements together with words like "and", "or", or "if... then".

---

## The Core Idea

In propositional logic, we do not care about the artistic meaning of a sentence. We only care about its truth value. 

For instance, the electrical engineering fact "The transistor conducts" and the arithmetic fact "$2 + 2 = 4$" look completely different. Yet in propositional logic, both are treated as identical objects: a single proposition whose truth value happens to be $\text{T}$.

Because a single proposition has only two possible values ($\text{T}$ or $\text{F}$), a system of $n$ propositions has a strictly finite universe of possibilities: exactly $2^n$ combinations.

| Variables ($n$) | Total Truth Table Rows ($2^n$) |
|:---:|:---:|
| 1 | 2 |
| 2 | 4 |
| 3 | 8 |
| 4 | 16 |
| $n$ | $2^n$ |

---

## The Two Tests for a Proposition

To decide if any sentence is a proposition, run it through two tests:

1. **Test 1: Is it declarative?** It must state a fact. It cannot be a question ("What time is it?"), a command ("Close the door!"), or a greeting.
2. **Test 2: Does it have an unambiguous truth value?** It must be definitely true or definitely false, never both, and never undefined.

### 4-Point Checklist for the Exam Room

When an exam question asks you to classify sentences, verify these four points:
- **Declarative:** Asserts a fact rather than commanding or requesting.
- **Not interrogative or imperative:** No question marks or hidden orders.
- **Definite truth value:** Strictly $\text{T}$ or strictly $\text{F}$.
- **Well-defined meaning:** All symbols and terms must be specified. Division by zero ($1/0 = 3$) or undefined terms fail this test.

### Classification Examples Table

| Sentence | Proposition? | Reason |
|:---|:---:|:---|
| "The transistor conducts" | **Yes** | Declarative sentence, either true or false. |
| "$2 + 2 = 4$" | **Yes** | Declarative mathematical statement, truth value is $\text{T}$. |
| "$2 + 2 = 5$" | **Yes** | Declarative mathematical statement, truth value is $\text{F}$ (still a proposition!). |
| "Water boils at $100^\circ\text{C}$ at sea level" | **Yes** | Declarative scientific statement, truth value is $\text{T}$. |
| "Close the laboratory door" | **No** | Imperative command, has no truth value. |
| "Is the power supply turned on?" | **No** | Interrogative question, has no truth value. |
| "$x + 1 > 0$" | **No** | Open formula with free variable $x$. True for $x = 2$, false for $x = -5$. |
| "$x + y = z$" | **No** | Variables are unbound, so it cannot be evaluated. |
| "The present king of France is bald" | **No** | Presupposes an entity that does not exist, so no truth value can be assigned. |
| "$1/0 = 3$" | **No** | Mathematically undefined due to division by zero. |

> [!WARNING] Common Traps to Watch Out For
> 1. **Do not confuse "False" with "Not a proposition".** The statement "$2 + 2 = 5$" is completely false, but it is 100% a proposition because it has a definite truth value ($\text{F}$).
> 2. **Free variables destroy truth values.** An expression like "$x + 2 = 5$" is a predicate, not a proposition. It only becomes a proposition when $x$ is specified (e.g., "for $x = 3$") or bound by a quantifier ("there exists an integer $x$ such that $x + 2 = 5$").

---

## Key Exam Comparisons

### Comparison 1: Proposition vs. Traditional Sentence

This was tested directly in 2022 Q.5(a):

| Feature | Proposition | Traditional (Ordinary) Sentence |
|:---|:---|:---|
| **Scope** | A narrow subset of language. | The entire broad spectrum of human language. |
| **Sentence Type** | Exclusively declarative sentences. | Declarative, interrogative, imperative, or exclamatory. |
| **Truth Value** | Must have exactly one truth value ($\text{T}$ or $\text{F}$). | Frequently has no truth value at all. |
| **Examples** | "$2 + 3 = 5$", "Silicon is a semiconductor". | "Please pass the multimeter", "Why is the circuit overheating?". |

In short: **Every proposition is an ordinary sentence, but not every ordinary sentence is a proposition.**

### Comparison 2: Proposition vs. Propositional Variable

This was tested directly in 2024 Q.5(a):

| Feature | Proposition | Propositional Variable |
|:---|:---|:---|
| **What it is** | The actual sentence stating a fact. | A single symbolic letter ($p$, $q$, $r$) acting as a placeholder. |
| **Origin of truth value** | Possesses its own inherent truth value based on reality. | Has no truth value of its own; borrows whatever value the assigned proposition has. |
| **Example** | "The microcontroller clock frequency is 16 MHz". | The variable $p$ used in the expression $p \to q$. |

In simple words: The proposition is the physical object, while the propositional variable is the label you stick on it so you can do algebra.

---

## 🔧 Worked Example

> **From:** 2022 Q.5(a) -- [Marks: 03]

**The question:** Explain how proposition differs from traditional sentence. Give some examples.

**Let's solve this step by step:**

1. **Define both terms clearly:**
   A proposition is a declarative sentence that is unambiguously either true or false, but not both.
   A traditional (ordinary) sentence is any grammatically complete expression in natural language, which includes questions, commands, requests, and exclamations.
2. **State the relationship:**
   Every proposition is an ordinary sentence, but the reverse is not true. Propositions form a strict subset of ordinary sentences.
3. **Provide illustrative examples in a clean table:**

| Example Sentence | Type of Sentence | Is it a Proposition? | Explanation |
|:---|:---|:---:|:---|
| "RUET is an engineering university." | Declarative | Yes | True statement of fact. |
| "$5 \times 4 = 20$" | Declarative | Yes | True mathematical fact. |
| "$7$ is an even number." | Declarative | Yes | False statement of fact, truth value is $\text{F}$. |
| "Turn off the oscilloscope." | Imperative | No | Command, no truth value. |
| "What is the voltage across $R_1$?" | Interrogative | No | Question, no truth value. |
| "$x^2 - 1 = 0$" | Open sentence | No | Truth depends on unknown variable $x$. |

---

## 🏆 Past Exam Questions

### 2022 Q.5(a): Proposition vs. Traditional Sentence -- [03 marks]

**Question:** Explain how proposition differs from traditional sentence. Give some examples.

**Answer:**
A proposition is a declarative sentence that declares a fact and has a definite truth value: it is unambiguously true or false, but not both. A traditional sentence is any syntactically complete unit of natural language, encompassing questions, commands, exclamations, and open statements.

The core distinction lies in the existence of a truth value:
1. **Truth Value:** A proposition always carries a truth value ($\text{T}$ or $\text{F}$). Traditional sentences often carry no truth value (such as commands or questions).
2. **Grammatical Form:** Propositions can only be declarative. Traditional sentences can be imperative ("Halt"), interrogative ("Who are you?"), or exclamatory ("Great job!").

**Examples:**
- Proposition: "Copper is an electrical conductor" (Declarative, True).
- Proposition: "The binary number $10_2$ equals $5_{10}$" (Declarative, False).
- Traditional sentence (Not a proposition): "Calculate the mesh currents" (Imperative command).
- Traditional sentence (Not a proposition): "Is the circuit grounded?" (Interrogative question).

---

### 2024 Q.5(a): Propositional Logic & Proposition vs. Propositional Variable -- [02 marks]

**Question:** Define propositional logic and explain the difference between a proposition and propositional variable.

**Answer:**
**Propositional logic** is the mathematical branch of formal logic that studies propositions and the rules governing their combinations through logical connectives ($\neg, \land, \lor, \to, \leftrightarrow$). It evaluates the truth values of compound formulas while treating each constituent proposition as an indivisible atomic unit.

**Difference between a Proposition and a Propositional Variable:**
- **Proposition:** The concrete, declarative sentence expressing an actual fact with a definite truth value. Example: "The sensor temperature exceeds $50^\circ\text{C}$".
- **Propositional Variable:** A symbolic letter (typically lowercase letters $p, q, r, s$) used as an abstract placeholder representing a proposition. A variable has no inherent truth value of its own; it receives a truth value only when assigned to a specific proposition or truth assignment.

$$
\text{Proposition} = \text{declarative statement}; \quad \text{Propositional Variable} = \text{its symbolic placeholder}
$$

---

## ⚡ Quick Review

**The topic in one sentence:** A proposition is a declarative sentence that is either true or false (never both), and propositional variables ($p, q, r$) are the algebraic letters that stand for them.

**The test you must memorize:**
1. Is it declarative?
2. Does it have an unambiguous truth value?

**The most common exam mistake:** Assuming a false sentence like "$3 + 3 = 7$" is not a proposition. It is a proposition because its truth value is cleanly $\text{F}$.

**Time estimate in exam:** 2 to 3 minutes to write out definitions and the example table.

---

## 🔗 Connected Topics

- [📂 DM-3 Topic Overview](_Topic_Overview.md) -- Review the full scope of propositional logic.
- [→ Next: DM-3.2 Connectives and Truth Tables](DM-3.2_Connectives_and_Truth_Tables.md) -- See how atomic propositions combine into compound formulas using $\neg, \land, \lor, \to, \leftrightarrow$.
- [DM-3.12: Predicates and Quantifiers](DM-3.12_Predicates_and_Quantifiers.md) -- See what happens when sentences contain free variables like $P(x)$.

---

[← Previous: DM-2.4 Equivalence Relations](../DM-2_Relations/DM-2.4_Equivalence_Relations.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: DM-3.2 Connectives and Truth Tables →](DM-3.2_Connectives_and_Truth_Tables.md)
