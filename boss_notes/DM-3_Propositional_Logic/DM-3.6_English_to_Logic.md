[← Previous: DM-3.5 Logical Equivalence](DM-3.5_Logical_Equivalence.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: DM-3.7 System Specification →](DM-3.7_System_Specification.md)

---

# DM-3.6: English to Logic

> 🟠 **Priority:** Secondary | **Tested:** 2024, CT-04 | **Typical marks:** 3 to 4

## What This Is (and Why It Matters)

This is the highest marks-per-minute subtopic in Propositional Logic. In engineering, natural language is loose, sloppy, and ambiguous. If an engineer writes a specification in English, two programmers can interpret it in opposite ways. Formal logic eliminates that ambiguity.

In the exam, translating English into logic seems easy until you run into connective traps like "unless", "only if", and "neither... nor". A single misplaced arrow or flipped negation turns a correct system requirement into a broken formula that fails every subsequent truth table question. If you master the translation dictionary below, you will never get tricked.

---

## 📝 Key Definitions

> **Formal Specification:** "Logic is used in the specification of software and hardware, because these specifications need to be precise before development begins." -- Rosen, §1.2, Introduction (p. 16)
>
> **In simple words:** Writing engineering rules in symbolic logic so there is zero confusion about how the system must behave in every possible situation.

---

## The English-to-Logic Translation Dictionary

Here is the master table of natural language phrases and their exact mathematical symbols:

| Natural English Phrase | Logical Operator | Mathematical Meaning | Key Takeaway |
|:---|:---:|:---:|:---|
| "and", "also", "but", "however", "yet" | $\land$ | Conjunction | Both conditions must hold simultaneously. |
| "or" | $\lor$ | Disjunction (inclusive) | At least one condition must hold. |
| "either... or... but not both" | $\oplus$ | Exclusive OR | Exactly one condition holds; both cannot hold. |
| "not", "it is not the case that" | $\neg$ | Negation | Flips the truth value. |
| "neither $p$ nor $q$" | $\neg p \land \neg q$ | Negate both | Equivalent by De Morgan to $\neg(p \lor q)$. |
| "if $p$, then $q$" | $p \to q$ | Implication | $p$ is the hypothesis, $q$ is the conclusion. |
| "$p$ only if $q$" | $p \to q$ | Implication | The arrow points toward the "only if" statement! |
| "$p$ if $q$" | $q \to p$ | Implication | The condition follows "if", so the arrow points back from $q$ to $p$. |
| "$p$ whenever $q$" | $q \to p$ | Implication | "Whenever" is a direct synonym for "if". |
| "$p$ provided that $q$" | $q \to p$ | Implication | "Provided that" is a direct synonym for "if". |
| "$p$ is necessary for $q$" | $q \to p$ | Implication | $p$ is the required consequence. |
| "$p$ is sufficient for $q$" | $p \to q$ | Implication | $p$ is enough to guarantee $q$. |
| "$p$ unless $q$" | $\neg q \to p$ | Implication / Disjunction | Equivalent to $p \lor q$. |
| "if and only if", "iff", "exactly when" | $\leftrightarrow$ | Biconditional | Both directions hold simultaneously: $(p \to q) \land (q \to p)$. |

---

## The Two Critical Arrow Traps

### 1. The "Only If" vs "If" Trap
The most frequent mistake students make is confusing "if" with "only if":

- **"$p$ if $q$"** means $q$ is the condition that triggers $p$. So the arrow points:
$$
q \to p
$$
- **"$p$ only if $q$"** means $p$ cannot happen unless $q$ happens. That makes $q$ a necessary requirement for $p$. So the arrow points:
$$
p \to q
$$

> [!WARNING] Remember the Rule of Thumb
> The implication arrow **always points directly at the condition following "only if"**:
> - "$A$ only if $B$" $\implies A \to B$.
> - Rosen's classic textbook example: "You can access the Internet from campus ($a$) only if you are a computer science major ($c$) or you are not a freshman ($\neg f$)":
> $$
> a \to (c \lor \neg f)
> $$

### 2. The "Unless" Trap
In English, "$B$ unless $A$" means: "If $A$ does not happen, then $B$ will definitely happen."

Therefore, the literal translation is:
$$
\neg A \to B
$$
Using the implication law $\neg X \lor Y \equiv X \to Y$, this rewrites into three completely equivalent forms:
$$
\neg A \to B \;\equiv\; \neg(\neg A) \lor B \;\equiv\; A \lor B \;\equiv\; \neg B \to A
$$

| Equivalent Form | When to Use It in an Answer |
|:---|:---|
| $\neg A \to B$ | When emphasizing: "failing condition $A$ forces result $B$". |
| $A \lor B$ | When you need pure disjunctive notation. |
| $\neg B \to A$ | When matching a contrapositive in a proof. |

> [!CAUTION] "Unless" is NEVER a Biconditional
> Translating "$B$ unless $A$" as $A \leftrightarrow B$ is completely wrong. "Unless" only guarantees what happens when $A$ is false; it does not claim that $A$ and $B$ are identical.

---

## Translation Traps at a Glance

| Everyday English Phrase | Incorrect Common Guess | Correct Logical Formula | Why the Guess Fails |
|:---|:---:|:---:|:---|
| "$A$ only if $B$" | $B \to A$ | $A \to B$ | Confuses necessary condition with sufficient condition. |
| "$B$ unless $A$" | $A \leftrightarrow B$ | $\neg A \to B \equiv A \lor B$ | "Unless" does not assert two-way equivalence. |
| "Neither $A$ nor $B$" | $\neg(A \land B)$ | $\neg A \land \neg B$ | $\neg(A \land B)$ means "not both", which allows one to be true! |
| "Not both $A$ and $B$" | $\neg A \land \neg B$ | $\neg(A \land B) \equiv \neg A \lor \neg B$ | "Not both" allows one to be true; it only forbids both together. |
| "$A$ but not $B$" | $A \lor \neg B$ | $A \land \neg B$ | "But" is an AND connective ($\land$), not an OR connective. |
| "Either $A$ or $B$, but not both" | $A \lor B$ | $A \oplus B \equiv (A \lor B) \land \neg(A \land B)$ | Plain "or" is inclusive; "but not both" enforces exclusive OR. |

---

## Industrial Specification Example (Class Notes)

Consider the complex engineering specification from Fahad's Class-13 and Raidah's notes:
> "The system will operate in normal mode if and only if the primary controller or the backup controller is active, but not both. However, if the emergency sensor is triggered, then the system will enter emergency mode only if both controllers are inactive."

Let's break it down methodically:
1. **Assign variables:**
   - $r$: System operates in normal mode
   - $p$: Primary controller is active
   - $q$: Backup controller is active
   - $t$: Emergency sensor is triggered
   - $s$: System enters emergency mode
2. **Translate Clause 1:**
   - "primary or backup, but not both" $\implies p \oplus q$
   - "normal mode if and only if..." $\implies r \leftrightarrow (p \oplus q)$
3. **Translate Clause 2:**
   - "However" $\implies \land$
   - "both controllers are inactive" $\implies \neg p \land \neg q$
   - "emergency mode only if both controllers inactive" $\implies s \to (\neg p \land \neg q)$
   - "if emergency sensor triggered, then..." $\implies t \to \big(s \to (\neg p \land \neg q)\big)$
4. **Combine into a single master specification:**
$$
\big[r \leftrightarrow (p \oplus q)\big] \land \big[t \to (s \to (\neg p \land \neg q))\big]
$$

---

## 🔧 Worked Example

> **From:** CT-04 Q.2(a)

**The question:** Translate the requirement into propositional logic:
*"A student can start the examination if and only if the student is authenticated and the examination server is available."*

**Let's solve this step by step:**

1. **Assign clear propositional variables:**
   - $p$: The student is authenticated
   - $q$: The examination server is available
   - $r$: The student can start the examination

2. **Identify the main connective:**
   The key phrase is **"if and only if"**, which represents a biconditional ($\leftrightarrow$).

3. **Identify the right-hand compound statement:**
   "the student is authenticated **and** the examination server is available" $\implies p \land q$.

4. **Write the final propositional formula:**
$$
\boxed{r \leftrightarrow (p \land q)}
$$

**Evaluate its 8-row truth table:**

| $p$ | $q$ | $r$ | $p \land q$ | $r \leftrightarrow (p \land q)$ |
|:---:|:---:|:---:|:---:|:---:|
| $\text{T}$ | $\text{T}$ | $\text{T}$ | $\text{T}$ | **T** |
| $\text{T}$ | $\text{T}$ | $\text{F}$ | $\text{T}$ | **F** |
| $\text{T}$ | $\text{F}$ | $\text{T}$ | $\text{F}$ | **F** |
| $\text{T}$ | $\text{F}$ | $\text{F}$ | $\text{F}$ | **T** |
| $\text{F}$ | $\text{T}$ | $\text{T}$ | $\text{F}$ | **F** |
| $\text{F}$ | $\text{T}$ | $\text{F}$ | $\text{F}$ | **T** |
| $\text{F}$ | $\text{F}$ | $\text{T}$ | $\text{F}$ | **F** |
| $\text{F}$ | $\text{F}$ | $\text{F}$ | $\text{F}$ | **T** |

$$
\boxed{r \leftrightarrow (p \land q) \text{ is true in 4 of 8 rows, so it is contingent}}
$$

> [!NOTE] Practical Engineering Significance
> Notice rows 3 and 5 where the formula is false:
> - Row 3: The server is down ($q = \text{F}$), but the student starts ($r = \text{T}$).
> - Row 5: The student is unauthenticated ($p = \text{F}$), but starts ($r = \text{T}$).
> The biconditional strictly forbids both security loopholes. A one-way implication $(p \land q) \to r$ would have left unauthenticated access permitted.

---

## 🏆 Past Exam Questions

### CT-04 Q.3(a): Translating Sensor and Controller Requirements

**Question:** Translate the following three statements into propositional logic with $p$: the sensor is active, $q$: the controller receives data.
- Statement 1: "If the sensor is active, then the controller receives data."
- Statement 2: "The controller does not receive data unless the sensor is active."
- Statement 3: "The sensor is active if and only if the controller receives data."

**Answer:**
We translate each statement using standard formal definitions:

1. **Statement 1:** "If the sensor is active ($p$), then the controller receives data ($q$)":
$$
S_1 = p \to q
$$

2. **Statement 2:** "The controller does not receive data ($\neg q$) unless the sensor is active ($p$)":
   The phrase "$B$ unless $A$" translates to $\neg A \to B$. Here, $A$ is "$p$" and $B$ is "$\neg q$":
$$
\neg p \to \neg q
$$
   Taking the contrapositive of $\neg p \to \neg q$:
$$
S_2 = q \to p \quad (\equiv p \lor \neg q)
$$

3. **Statement 3:** "The sensor is active ($p$) if and only if the controller receives data ($q$)":
$$
S_3 = p \leftrightarrow q \quad (\equiv (p \to q) \land (q \to p))
$$

> [!NOTE] Redundancy in the Specification
> Notice that $S_1 = p \to q$ and $S_2 = q \to p$. Together, they form both directions of the biconditional $S_3 = p \leftrightarrow q$. Statements 1 and 2 already fully establish Statement 3, meaning the third requirement is completely redundant.

---

## ⚡ Quick Review

**The golden rule of implication arrows:**
- "$A$ only if $B$" $\implies A \to B$ (points toward the "only if" clause).
- "$A$ if $B$" $\implies B \to A$ (points toward $A$, away from the condition $B$).
- "$B$ unless $A$" $\implies \neg A \to B \equiv A \lor B$.

**The most common exam mistake:** Translating "neither... nor" as $\neg(A \land B)$. Remember that "neither... nor" negates both: $\neg A \land \neg B$.

**Time estimate in exam:** 2 to 3 minutes to define variables and write the compound formulas.

---

## 🔗 Connected Topics

- [← Previous: DM-3.5 Logical Equivalence](DM-3.5_Logical_Equivalence.md) -- Review algebraic rewrites of implications.
- [→ Next: DM-3.7 System Specification](DM-3.7_System_Specification.md) -- Test whether translated requirements contain hidden contradictions.
- [DM-3.8: Normal Forms](DM-3.8_Normal_Forms.md) -- Convert translated specifications into CNF and DNF.

---

[← Previous: DM-3.5 Logical Equivalence](DM-3.5_Logical_Equivalence.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: DM-3.7 System Specification →](DM-3.7_System_Specification.md)
