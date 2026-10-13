---
title: "DM-3.11 · Logic Gates & Digital Circuits"
tags:
  - numerical-methods
  - discrete-mathematics
  - topicwise
---


[🏠 Subtopic Index](00_Index.md) | [← Prev: DM-3.10 Logic Puzzles](DM-3.10_Logic_Puzzles.md) | [Next: DM-3.13 Logic Extensions →](DM-3.13_Logic_Extensions.md)

---

# DM-3.11 · Logic Gates & Digital Circuits

Every block below is copied from `../answers_explanation/`. The reasoning
is written once, in the year-wise file, and is not restated here.


### [2023 Q.5(a)]

**Question.** Build a digital circuit that produces the output $(p \lor \neg r) \land (\neg p \lor (q \lor \neg r))$ when given input bits $p, q$ and $r$.

*[Marks: 04, CO: 2]*

**Solution.**

The question gives you an expression and asks for hardware. Building the circuit
straight from the expression works, but it needs four gates where three will do,
so the first job is simplification.

**Step 1. Simplify algebraically.** Look at the two bracketed terms:

$$
F = (p \lor \neg r) \land (\neg p \lor q \lor \neg r)
$$

$\neg r$ appears in both, and that is the handle to pull. Apply the distributive
identity

$$
(a \lor c) \land (b \lor c) = (a \land b) \lor c
$$

with $c = \neg r$, $a = p$ and $b = (\neg p \lor q)$:

$$
F = \neg r \lor \big[p \land (\neg p \lor q)\big]
$$

Now distribute inside the bracket:

$$
p \land (\neg p \lor q) = (p \land \neg p) \lor (p \land q) = 0 \lor (p \land q) = p \land q
$$

Therefore

$$
F = \neg r \lor (p \land q)
$$

**Step 2. Read off the circuit.**

1. Invert $r$ with a NOT gate to give $\neg r$.
2. AND $p$ with $q$ to give $p \land q$.
3. OR that with $\neg r$ to give the output $F$.

**Gates required:** 1 NOT, 1 AND (2-input), 1 OR (2-input), total: 3 gates.

**Logic Circuit Diagram (Simplified Form):**

![Digital logic circuit diagram for simplified expression F = ¬r ∨ (p ∧ q) using 1 NOT gate, 1 AND gate, and 1 OR gate](diagrams/2023_Q5a_simplified_logic_circuit.png)

**Alternative: Direct (Unsimplified) Circuit:**
If implemented directly without simplification:

![Direct logic circuit diagram implementing (p ∨ ¬r) ∧ (¬p ∨ (q ∨ ¬r)) with 2 NOT gates, 3 OR gates, and 1 AND gate](diagrams/2023_Q5a_unsimplified_circuit.jpg)

$$
\boxed{F = \neg r \lor (p \land q)}
$$

> [!info] Confirming over all eight input combinations
> Comparing the simplified form against the original on every assignment of
> $(p, q, r)$:
>
> | $p$ | $q$ | $r$ | Original | $\neg r \lor (p \land q)$ |
> | :-: | :-: | :-: | :-: | :-: |
> | F | F | F | T | T |
> | F | F | T | F | F |
> | F | T | F | T | T |
> | F | T | T | F | F |
> | T | F | F | T | T |
> | T | F | T | F | F |
> | T | T | F | T | T |
> | T | T | T | T | T |
>
> All eight rows agree, so the simplification is exact.
>
> Row 8 is the one to check by eye. With $r$ true, $\neg r$ is false, and the
> output fires only if both $p$ and $q$ are true. The original says
> $(p \lor \neg r) \land (\neg p \lor q \lor \neg r) = (T \lor F) \land (F \lor T \lor F) = T \land T = T$.
> Agrees.
>
> **Why checking all eight rows is worth the eight lines.** A three-variable
> Boolean function is completely determined by its truth table, so eight agreeing
> rows is a *proof* of equivalence, not a sample. That is a rare situation in
> this subject where exhaustive checking is genuinely conclusive.

> [!note] An equivalent form if you only have NAND gates
> Applying the distributive law back the other way gives

> $$
> F = (\neg r \lor p) \land (\neg r \lor q)
> $$
>
> This is useful in hardware because NAND is often the only gate a cheap part
> family provides. De Morgan's theorem turns each bracket into a NAND followed by
> an inverter, and a NAND-inverter pair is itself a NAND with its inputs tied, so
> the whole thing maps onto two NAND stages.

> [!warning] The mistake that keeps this question's marks
> Building the original expression gate for gate: NOT $r$, OR with $p$, then NOT
> $p$, OR with $q$ and $\neg r$, then AND. Five gates instead of three. It is a
> correct circuit and it will earn the marks, but it leaves the simplification
> on the table, and simplification is what the four marks are for.
>
> The tell is that $\neg r$ appears twice in the printed expression. Any
> sub-expression that appears more than once is a candidate for factoring out.

---

[🏠 Subtopic Index](00_Index.md) | [← Prev: DM-3.10 Logic Puzzles](DM-3.10_Logic_Puzzles.md) | [Next: DM-3.13 Logic Extensions →](DM-3.13_Logic_Extensions.md)
