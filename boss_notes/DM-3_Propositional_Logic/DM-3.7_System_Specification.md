[← Previous: DM-3.6 English to Logic](DM-3.6_English_to_Logic.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: DM-3.8 Normal Forms →](DM-3.8_Normal_Forms.md)

---

# DM-3.7: System Specification

> 🟠 **Priority:** Secondary | **Tested:** 2024 Q.5(c), CT-04 | **Typical marks:** 4 to 6

## What This Is (and Why It Matters)

In real-world engineering, before anyone writes code or solders a PCB, a systems engineer writes down what the system must do. A system specification is simply a list of these requirements written in plain language.

The fundamental engineering question is: **"Can this system actually exist?"** 
If the requirements contain hidden conflicts that lead to a logical contradiction, the system is impossible to build. In the RUET 2024 exam, Question 5(c) gave a 4-sentence specification for an operating system and asked students to determine whether the specifications were consistent. If you know how to run a contradiction chase or construct an 8-row table, you can solve this with total confidence.

---

## 📝 Key Definitions

> **Consistent System Specifications:** "System specifications should be consistent, that is, they should not contain conflicting requirements that could be used to derive a contradiction. When specifications are not consistent, there would be no way to develop a system that satisfies all specifications." -- Rosen, §1.2, System Specifications (p. 18)
>
> **In simple words:** A list of rules is consistent if there is at least one real-world operating state where all rules are satisfied at the same time. If following one rule forces you to break another, the rules are inconsistent.

---

## Three Possible Outcomes of a Consistency Check

When you analyze a system specification, exactly one of three cases will hold:

| Outcome | Mathematical Meaning | Engineering Reality | What You Must State |
|:---|:---|:---|:---|
| **Consistent** | At least one truth assignment satisfies every single requirement simultaneously. | The system can be designed and built. | "The specifications are consistent; satisfying state(s) exist." |
| **Inconsistent** | No truth assignment can satisfy all requirements simultaneously (conjunction is a contradiction). | The system is impossible to build; one or more requirements must be rewritten. | "The specifications are inconsistent: no assignment satisfies all requirements." |
| **Consistent but Incomplete** | The rules are mathematically consistent, but permit unintended or idle states (e.g., both sensors powered off). | The logic works, but the specification forgot to rule out dangerous or idle conditions. | State the satisfying assignments and point out the missing constraint. |

---

## Two Methods to Test Consistency

### Method 1: The Truth Table Method
1. Translate each English requirement into a propositional formula: $S_1, S_2, \dots, S_k$.
2. Form the grand conjunction of all specifications:
$$
C = S_1 \land S_2 \land \dots \land S_k
$$
3. Build the truth table with a dedicated column for each requirement and a final column for $C$.
4. **Read the result:** If the final column contains at least one $\text{T}$, the specifications are **consistent**. If the final column contains only $\text{F}$ entries across all rows, the specifications are **inconsistent**.

### Method 2: The Contradiction Chase (Much Faster!)
When a truth table would be 8 or 16 rows, a deduction chase can prove inconsistency in 6 lines:
1. Locate the most restrictive requirement (typically a single literal like "The alarm is off", $\neg r$).
2. Force that variable's value ($\neg r \implies r = \text{F}$).
3. Propagate that forced value into the other requirements using inference rules like Modus Ponens or Disjunctive Syllogism.
4. If a requirement forces $r = \text{T}$ while an earlier requirement forced $r = \text{F}$, you have trapped a direct contradiction ($\text{T} \land \text{F}$).
5. Conclude: The specifications are inconsistent.

---

## 🔧 Worked Example

> **From:** 2024 Q.5(c) -- [Marks: 05]

**The question:** Are these system specifications consistent?
> "The system is in multiuser state if and only if it is operating normally, the kernel is functioning. The kernel is not functioning or the system is in interrupt mode. If the system is not in multiuser state, then it is in interrupt mode. The system is not in interrupt mode."

**Let's solve this step by step:**

### Step 1: Assign Propositional Variables
- $p$: The system is in multiuser state
- $q$: The kernel is functioning
- $r$: The system is in interrupt mode

### Step 2: Translate Each Requirement
1. "The system is in multiuser state if and only if... the kernel is functioning":
$$
S_1 = p \leftrightarrow q
$$
2. "The kernel is not functioning or the system is in interrupt mode":
$$
S_2 = \neg q \lor r
$$
3. "If the system is not in multiuser state, then it is in interrupt mode":
$$
S_3 = \neg p \to r \quad (\equiv p \lor r)
$$
4. "The system is not in interrupt mode":
$$
S_4 = \neg r
$$

---

### Step 3: Test All 8 Assignments via Truth Table

| $p$ | $q$ | $r$ | $S_1: p \leftrightarrow q$ | $S_2: \neg q \lor r$ | $S_3: p \lor r$ | $S_4: \neg r$ | Grand Conjunction ($S_1 \land S_2 \land S_3 \land S_4$) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| $\text{F}$ | $\text{F}$ | $\text{F}$ | $\text{T}$ | $\text{T}$ | $\text{F}$ | $\text{T}$ | **F** |
| $\text{F}$ | $\text{F}$ | $\text{T}$ | $\text{T}$ | $\text{T}$ | $\text{T}$ | $\text{F}$ | **F** |
| $\text{F}$ | $\text{T}$ | $\text{F}$ | $\text{F}$ | $\text{F}$ | $\text{F}$ | $\text{T}$ | **F** |
| $\text{F}$ | $\text{T}$ | $\text{T}$ | $\text{F}$ | $\text{T}$ | $\text{T}$ | $\text{F}$ | **F** |
| $\text{T}$ | $\text{F}$ | $\text{F}$ | $\text{F}$ | $\text{T}$ | $\text{T}$ | $\text{T}$ | **F** |
| $\text{T}$ | $\text{F}$ | $\text{T}$ | $\text{F}$ | $\text{T}$ | $\text{T}$ | $\text{F}$ | **F** |
| $\text{T}$ | $\text{T}$ | $\text{F}$ | $\text{T}$ | $\text{F}$ | $\text{T}$ | $\text{T}$ | **F** |
| $\text{T}$ | $\text{T}$ | $\text{T}$ | $\text{T}$ | $\text{T}$ | $\text{T}$ | $\text{F}$ | **F** |

Notice that the final column is $\text{F}$ in all 8 rows. Not a single assignment satisfies all four requirements.

$$
\boxed{\text{The specifications are INCONSISTENT: no assignment satisfies all four}}
$$

---

### Step 4: The Rapid Contradiction Chase (6-Line Proof)
You can confirm this without drawing the table:
1. Requirement 4 asserts $\neg r$, forcing $r = \text{F}$.
2. Substitute $r = \text{F}$ into Requirement 2 ($\neg q \lor r$). For this to be true, we must have $\neg q = \text{T}$, which forces $q = \text{F}$.
3. Substitute $q = \text{F}$ into Requirement 1 ($p \leftrightarrow q$). For the biconditional to hold, $p$ must match $q$, forcing $p = \text{F}$.
4. Now check Requirement 3 ($\neg p \to r$, which is $p \lor r$):
   Since $p = \text{F}$ and $r = \text{F}$, we have $p \lor r = \text{F} \lor \text{F} = \text{F}$.
5. But Requirement 3 requires $p \lor r$ to be true. This is a direct contradiction ($\mathbf{F} \equiv \mathbf{T}$).

Therefore, no valid operating state exists. The specifications are mathematically inconsistent.

---

## 🏆 Past Exam Questions

### 2024 Q.5(c): Operating System Consistency Check -- [05 marks]

**Question:** Are these system specifications consistent?
> "The system is in multiuser state if and only if it is operating normally, the kernel is functioning. The kernel is not functioning or the system is in interrupt mode. If the system is not in multiuser state, then it is in interrupt mode. The system is not in interrupt mode."

**Answer:**
Let $p$: multiuser state, $q$: kernel is functioning, $r$: interrupt mode.
The four specifications are:
1. $S_1 = p \leftrightarrow q$
2. $S_2 = \neg q \lor r$
3. $S_3 = \neg p \to r \equiv p \lor r$
4. $S_4 = \neg r$

We analyze the system for consistency:
- From $S_4$, we require $r = \text{F}$.
- With $r = \text{F}$, $S_2$ becomes $\neg q \lor \text{F} \equiv \neg q$. Thus, $q$ must be $\text{F}$.
- With $q = \text{F}$, $S_1$ becomes $p \leftrightarrow \text{F} \equiv \neg p$. Thus, $p$ must be $\text{F}$.
- With $p = \text{F}$ and $r = \text{F}$, $S_3$ evaluates to $\text{F} \lor \text{F} = \text{F}$, contradicting the requirement that $S_3$ is true.

Because no truth assignment satisfies all four requirements simultaneously, the specifications are inconsistent.

$$
\boxed{\text{The specifications are INCONSISTENT: no assignment satisfies all four}}
$$

---

### CT-04 Q.3(b), (c), (d): Complete Sensor/Controller Consistency Analysis

**Question:** Given the sensor/controller specifications:
- $S_1 = p \to q$
- $S_2 = q \to p$
- $S_3 = p \leftrightarrow q$
(b) Form the conjunction $C = S_1 \land S_2 \land S_3$ and simplify.
(c) Construct the truth table for $C$.
(d) Find all truth assignments that satisfy all requirements simultaneously.

**Answer:**

#### Part (b): Conjunction and Simplification
$$
C = (p \to q) \land (q \to p) \land (p \leftrightarrow q)
$$
Since $(p \to q) \land (q \to p) \equiv p \leftrightarrow q$:
$$
\boxed{C = (p \to q) \land (q \to p)}
$$
Rewriting implications using disjunction:
$$
\boxed{C = (\neg p \lor q) \land (\neg q \lor p)}
$$
Expanding via distributive law:
$$
\boxed{C = (\neg p \lor q) \land (\neg q \lor p) \equiv (p \land q) \lor (\neg p \land \neg q)}
$$

---

#### Part (c): Truth Table of the Conjunction

| $p$ | $q$ | $p \to q$ | $q \to p$ | $S_3: p \leftrightarrow q$ | $C = S_1 \land S_2 \land S_3$ |
|:---:|:---:|:---:|:---:|:---:|:---:|
| $\text{T}$ | $\text{T}$ | $\text{T}$ | $\text{T}$ | $\text{T}$ | **T** |
| $\text{T}$ | $\text{F}$ | $\text{F}$ | $\text{T}$ | $\text{F}$ | **F** |
| $\text{F}$ | $\text{T}$ | $\text{T}$ | $\text{F}$ | $\text{F}$ | **F** |
| $\text{F}$ | $\text{F}$ | $\text{T}$ | $\text{T}$ | $\text{T}$ | **T** |

$$
\boxed{C \text{ is true in rows 1 and 4, so it is contingent}}
$$

$$
\boxed{C \text{ is equivalent to } p \leftrightarrow q}
$$

---

#### Part (d): Satisfying Truth Assignments
From the truth table, $C$ evaluates to $\text{T}$ in rows 1 and 4:
1. Assignment 1: $(p, q) = (\text{T}, \text{T})$ -- Sensor active AND controller receives data.
2. Assignment 2: $(p, q) = (\text{F}, \text{F})$ -- Sensor inactive AND controller receives nothing.

$$
\boxed{\text{The specification is satisfiable, and the satisfying assignments are exactly } (p,q) = (\mathrm{T},\mathrm{T}) \text{ and } (\mathrm{F},\mathrm{F})}
$$

$$
\boxed{\text{Equivalently: the requirements hold if and only if } p = q}
$$

> [!NOTE] Practical Engineering Observation
> Notice that the specification permits $(p, q) = (\text{F}, \text{F})$. The system satisfies all requirements even when it is completely powered off and idle! If the engineer intended for the sensor to actively monitor at all times, a fourth requirement ("The sensor is active", $p$) must be added.

---

## ⚡ Quick Review

**Consistency in one sentence:** Specifications are consistent if their grand conjunction is satisfiable (at least one $\text{T}$ row); they are inconsistent if their conjunction is a contradiction (all rows $\text{F}$).

**The fastest exam technique:** Use the 6-line contradiction chase first. If you trap a contradiction, you save 5 minutes of drawing an 8-row table.

**The most common exam mistake:** Forgetting to state whether the specifications are consistent or inconsistent in words after calculating the truth table. Always write the explicit boxed verdict.

**Time estimate in exam:** 4 to 6 minutes for translation and consistency testing.

---

## 🔗 Connected Topics

- [← Previous: DM-3.6 English to Logic](DM-3.6_English_to_Logic.md) -- Review the translation of "unless" and "only if".
- [→ Next: DM-3.8 Normal Forms](DM-3.8_Normal_Forms.md) -- Master how to convert compound system requirements into standard CNF and DNF.
- [DM-3.9: Rules of Inference](DM-3.9_Rules_of_Inference.md) -- See how formal deduction rules automate the contradiction chase.

---

[← Previous: DM-3.6 English to Logic](DM-3.6_English_to_Logic.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: DM-3.8 Normal Forms →](DM-3.8_Normal_Forms.md)
