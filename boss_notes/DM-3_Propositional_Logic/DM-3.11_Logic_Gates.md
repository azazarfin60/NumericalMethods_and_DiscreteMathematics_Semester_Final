[← Previous: DM-3.10 Logic Puzzles](DM-3.10_Logic_Puzzles.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: DM-3.12 Predicates and Quantifiers →](DM-3.12_Predicates_and_Quantifiers.md)

---

# DM-3.11: Logic Gates

> 🟡 **Priority:** Light | **Tested:** 2023 Q.5(a) | **Typical marks:** 5

## What This Is (and Why It Matters)

This is the physical bridge where mathematical logic turns into electrical and computer engineering hardware. Every computer processor, microcontroller, and memory cell is built out of billions of microscopic transistors wired together to implement logic gates.

In the exam, Question 5(a) of 2023 set a 5-mark problem asking students to build a digital circuit from a compound proposition. The secret to earning full marks is two-fold: first, algebraically simplify the expression so you draw a minimal-cost circuit; second, draw the schematic cleanly and verify its truth table.

---

## 📝 Key Definitions

> **Logic Circuit:** "A logic circuit (or digital circuit) receives input signals $p_1, p_2, \dots, p_n$, each a bit [either 0 (off) or 1 (on)], and produces output signals $s_1, s_2, \dots, s_n$, each a bit." -- Rosen, §1.2, Logic Circuits (p. 20)
>
> **In simple words:** A hardware network of electronic switches that takes 0s and 1s as inputs and computes a boolean formula to produce output 0s and 1s.

> **The Three Primitive Gates:** "The inverter, or NOT gate, takes an input bit $p$, and produces as output $\neg p$. The OR gate takes two input signals $p$ and $q$, each a bit, and produces as output the signal $p \vee q$. The AND gate takes two input signals $p$ and $q$, each a bit, and produces as output the signal $p \wedge q$." -- Rosen, §1.2, Logic Circuits (p. 21)
>
> **In simple words:** The three basic electronic building blocks: an inverter flips the bit, an AND gate outputs 1 only when both inputs are 1, and an OR gate outputs 1 when at least one input is 1.

> **Circuit Implementability Theorem:** "Suppose that we have a formula for the output of a digital circuit in terms of negations, disjunctions, and conjunctions. Then, we can systematically build a digital circuit with the desired output." -- Rosen, §1.2 (p. 21)
>
> **In simple words:** Any logical formula you can write on paper using NOT, AND, and OR can be directly built into a physical silicon circuit.

---

## The Three Fundamental Gate Types

![Basic logic gates: Inverter (NOT gate), OR gate, and AND gate (Rosen §1.2, Figure 1.5, p. 21)](../diagrams/dm3_not_and_or_gates.jpg)

| Gate Type | Boolean Expression | Inputs | Outputs | Schematic Symbol Description |
|:---|:---:|:---:|:---:|:---|
| **NOT Gate (Inverter)** | $\neg p$ or $\overline{p}$ | 1 bit | 1 bit | Triangle pointing right with a small inversion bubble at the output tip. |
| **AND Gate** | $p \land q$ | 2 or more bits | 1 bit | Flat vertical edge on the input side, rounded curved edge on the output side. |
| **OR Gate** | $p \lor q$ | 2 or more bits | 1 bit | Curved inward edge on the input side, sharp pointed tip on the output side. |

---

## The 4-Step Procedure for Exam Circuit Questions

Whenever an exam asks you to "Build a digital circuit that produces the output $F$":

1. **Simplify the formula algebraically first:** 
   Examiners usually give an unsimplified formula containing 6 or 7 gates. Simplifying it drops the gate count down to 2 or 3 gates. This saves you drawing time and prevents wiring mistakes.
2. **List the gate inventory:**
   Count exactly how many NOT, AND, and OR gates are needed for your simplified design.
3. **Draw the logic diagram clearly:**
   Label all input signal lines on the left ($p, q, r$), label all intermediate wire outputs, and show the final output on the right.
4. **Verify over all input combinations:**
   Build an 8-row truth table to confirm that your simplified circuit produces the exact same output as the original formula in every row.

---

## 🔧 Worked Example

> **From:** 2023 Q.5(a) -- [Marks: 05]

**The question:** Build a digital circuit that produces the output $(p \lor \neg r) \land (\neg p \lor (q \lor \neg r))$ when given input bits $p, q$, and $r$.

**Let's solve this step by step:**

### Step 1: Simplify the Formula Algebraically
Let the given output expression be:
$$
F = (p \lor \neg r) \land \big[\neg p \lor (q \lor \neg r)\big]
$$
Notice that $\neg r$ appears in both clauses. Let's rearrange using associativity:
$$
F = (p \lor \neg r) \land \big[(\neg p \lor q) \lor \neg r\big]
$$
Now, apply the Distributive Law in reverse: $(A \lor C) \land (B \lor C) \equiv (A \land B) \lor C$, with $C = \neg r$, $A = p$, and $B = (\neg p \lor q)$:
$$
F = \neg r \lor \big[p \land (\neg p \lor q)\big]
$$
Distribute $p$ inside the bracket:
$$
p \land (\neg p \lor q) \equiv (p \land \neg p) \lor (p \land q)
$$
Since $p \land \neg p \equiv \mathbf{F}$:
$$
\equiv \mathbf{F} \lor (p \land q) \equiv p \land q
$$
Substitute this back:
$$
F = \neg r \lor (p \land q)
$$

$$
\boxed{F = \neg r \lor (p \land q)}
$$

---

### Step 2: Gate Count Inventory
- **1 NOT Gate (Inverter):** Takes input $r$ and produces $\neg r$.
- **1 AND Gate (2-input):** Takes inputs $p$ and $q$ and produces $p \land q$.
- **1 OR Gate (2-input):** Takes $\neg r$ and $(p \land q)$ to produce the final output $F$.
- **Total Gates Required:** **3 gates** (compared to 7 gates unsimplified!).

---

### Step 3: Draw the Logic Circuit Diagram

#### Clean Minimal Circuit (3 Gates):

![Clean minimal digital logic circuit diagram (3 gates) for F = ¬r ∨ (p ∧ q)](../diagrams/2023_Q5a_simplified_logic_circuit.png)

#### Alternative: Rosen's Direct Unsimplified Circuit (7 Gates)
If an examiner expects the direct literal diagram without simplification (Rosen §1.2, Figure 1.7, p. 22):

![Rosen's circuit for (p ∨ ¬r) ∧ (¬p ∨ (q ∨ ¬r)), built from three inverters, three OR gates and one AND gate (Rosen §1.2, Figure 1.7, p. 22)](../diagrams/dm3_circuit_pyq_2023_q5a_rosen_fig3.jpg)

Both designs are mathematically correct. The simplified 3-gate circuit is the best engineering solution; drawing both or providing the simplified circuit with the truth table verification earns top marks.

---

### Step 4: Verification Across All 8 Rows

| $p$ | $q$ | $r$ | $\neg r$ | $p \land q$ | Simplified: $\neg r \lor (p \land q)$ | Original: $(p \lor \neg r) \land (\neg p \lor q \lor \neg r)$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| $\text{F}$ | $\text{F}$ | $\text{F}$ | $\text{T}$ | $\text{F}$ | **T** | $\text{T} \land \text{T} = \mathbf{T}$ |
| $\text{F}$ | $\text{F}$ | $\text{T}$ | $\text{F}$ | $\text{F}$ | **F** | $\text{F} \land \text{T} = \mathbf{F}$ |
| $\text{F}$ | $\text{T}$ | $\text{F}$ | $\text{T}$ | $\text{F}$ | **T** | $\text{T} \land \text{T} = \mathbf{T}$ |
| $\text{F}$ | $\text{T}$ | $\text{T}$ | $\text{F}$ | $\text{F}$ | **F** | $\text{F} \land \text{T} = \mathbf{F}$ |
| $\text{T}$ | $\text{F}$ | $\text{F}$ | $\text{T}$ | $\text{F}$ | **T** | $\text{T} \land \text{T} = \mathbf{T}$ |
| $\text{T}$ | $\text{F}$ | $\text{T}$ | $\text{F}$ | $\text{F}$ | **F** | $\text{T} \land \text{F} = \mathbf{F}$ |
| $\text{T}$ | $\text{T}$ | $\text{F}$ | $\text{T}$ | $\text{T}$ | **T** | $\text{T} \land \text{T} = \mathbf{T}$ |
| $\text{T}$ | $\text{T}$ | $\text{T}$ | $\text{F}$ | $\text{T}$ | **T** | $\text{T} \land \text{T} = \mathbf{T}$ |

The simplified circuit matches the original expression in all 8 rows.

---

## ⚡ Quick Review

**The method in one sentence:** Simplify the Boolean formula using distributive and complement laws, count the required inverters, ANDs, and ORs, and draw the signal flow from inputs on the left to output on the right.

**The gate reduction formula to remember:**
$$
(p \lor \neg r) \land (\neg p \lor (q \lor \neg r)) \equiv \neg r \lor (p \land q)
$$

**The most common exam mistake:** Drawing crossed wires without clear junction dots, or confusing the curved input shape of an OR gate with the flat input shape of an AND gate.

**Time estimate in exam:** 5 minutes to simplify, draw, and verify the circuit.

---

## 🔗 Connected Topics

- [← Previous: DM-3.10 Logic Puzzles](DM-3.10_Logic_Puzzles.md) -- Review Boolean truth value evaluations.
- [→ Next: DM-3.12 Predicates and Quantifiers](DM-3.12_Predicates_and_Quantifiers.md) -- Move beyond propositional constants to quantified variables.
- [DM-3.8: Normal Forms](DM-3.8_Normal_Forms.md) -- See how DNF forms map onto two-level AND-OR digital hardware.

---

[← Previous: DM-3.10 Logic Puzzles](DM-3.10_Logic_Puzzles.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: DM-3.12 Predicates and Quantifiers →](DM-3.12_Predicates_and_Quantifiers.md)
