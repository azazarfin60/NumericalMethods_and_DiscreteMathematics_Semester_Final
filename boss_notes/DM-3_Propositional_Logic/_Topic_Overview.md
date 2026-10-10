# DM-3: Propositional Logic

> **Section:** Section B (Discrete Mathematics)
> **Subtopics in this folder:** 13 files (DM-3.1 through DM-3.13)
> **Exam weight:** Heaviest topic in Discrete Mathematics. Appears in every single Discrete Mathematics final paper (2022, 2023, 2024) plus Class Tests. Worth 15 to 25 marks per final paper.

---

## 📖 How to Read This Topic

Propositional logic is the bedrock of Section B. If you master this folder, you can secure almost half of the Discrete Mathematics marks on exam day.

Here is the natural learning path:

1. **Foundations (DM-3.1 to DM-3.3):** Start with **DM-3.1** to understand what counts as a proposition and what does not. Then study **DM-3.2** for the six core logical connectives, their truth tables, and operator precedence. Move to **DM-3.3** to classify compound statements into tautologies, contradictions, and contingencies.
2. **Analysis and Translation (DM-3.4 to DM-3.7):** Learn how to test validity and satisfiability in **DM-3.4**, and prove logical equivalences algebraically or with truth tables in **DM-3.5**. Translate tricky English phrases into logic without falling into connective traps in **DM-3.6**. Then verify whether engineering requirements conflict with each other in **DM-3.7**.
3. **Core Techniques and Proofs (DM-3.8 to DM-3.9):** Master Disjunctive and Conjunctive Normal Forms (DNF and CNF) and functional completeness in **DM-3.8**. Learn the rules of inference (Modus Ponens, Modus Tollens, Syllogisms) and build formal multi-step proofs in **DM-3.9**.
4. **Applications and Extensions (DM-3.10 to DM-3.13):** Solve Knights, Knaves, Spies puzzles and Lewis Carroll syllogisms in **DM-3.10**. Build digital circuits from Boolean propositions in **DM-3.11**. Skim Predicates and Quantifiers in **DM-3.12** for conceptual completeness, and finish with Fuzzy Logic truth values in **DM-3.13**.

**Suggested total study time:** ~3.5 to 4 hours for complete mastery.

---

## 📑 Subtopic Index

| # | Subtopic | Priority | Exam Frequency | Est. Read Time |
|:--:|:---|:---:|:---:|:---:|
| 1 | [DM-3.1: Propositions](DM-3.1_Propositions.md) | 🔴 | 2022, 2024 | ~12 min |
| 2 | [DM-3.2: Connectives and Truth Tables](DM-3.2_Connectives_and_Truth_Tables.md) | 🔴 | 2022, 2023, 2024, CT-04 | ~18 min |
| 3 | [DM-3.3: Tautology and Contradiction](DM-3.3_Tautology_and_Contradiction.md) | 🔴 | 2023, 2024, CT-04 | ~18 min |
| 4 | [DM-3.4: Validity and Satisfiability](DM-3.4_Validity_and_Satisfiability.md) | 🟠 | 2024, CT-04 | ~14 min |
| 5 | [DM-3.5: Logical Equivalence](DM-3.5_Logical_Equivalence.md) | 🟠 | 2023 | ~14 min |
| 6 | [DM-3.6: English to Logic](DM-3.6_English_to_Logic.md) | 🟠 | 2024, CT-04 | ~15 min |
| 7 | [DM-3.7: System Specification](DM-3.7_System_Specification.md) | 🟠 | 2024, CT-04 | ~16 min |
| 8 | [DM-3.8: Normal Forms](DM-3.8_Normal_Forms.md) | 🔴 | 2022, 2024, CT-04 | ~22 min |
| 9 | [DM-3.9: Rules of Inference](DM-3.9_Rules_of_Inference.md) | 🔴 | 2022, 2023 | ~20 min |
| 10 | [DM-3.10: Logic Puzzles](DM-3.10_Logic_Puzzles.md) | 🟠 | 2022, 2023 | ~18 min |
| 11 | [DM-3.11: Logic Gates](DM-3.11_Logic_Gates.md) | 🟡 | 2023 | ~12 min |
| 12 | [DM-3.12: Predicates and Quantifiers](DM-3.12_Predicates_and_Quantifiers.md) | ⚫ | Syllabus foundation (0/3 papers) | ~10 min |
| 13 | [DM-3.13: Fuzzy Logic](DM-3.13_Fuzzy_Logic.md) | 🟡 | 2022 | ~12 min |

---

## 🎯 Exam Pattern for This Topic

In the RUET ECE 2213 exam, Section B questions always draw heavily from Propositional Logic:

1. **Question 5 or Question 6 Opening (2 to 4 marks):**
   - Direct definitions: Proposition vs. ordinary sentence, or proposition vs. propositional variable (2022 Q.5(a), 2024 Q.5(a)).
   - Truth evaluation of biconditionals or connectives (2022 Q.6(b), 2024 Q.7(b)).
2. **Middle Sub-questions (4 to 6 marks):**
   - Truth table proofs for tautology or logical equivalence (2023 Q.5(c), 2023 Q.6(a)).
   - System specification consistency checks (2024 Q.5(c)).
   - Conversion of English alarm/control conditions into DNF and CNF (2024 Q.6(b)).
   - Proof of functional completeness for $\{\neg, \land\}$ or $\{\neg, \lor\}$ (2022 Q.5(c)).
3. **Reasoning and Applied Logic (4 to 6 marks):**
   - Multi-premise deduction using Rules of Inference (2023 Q.6(c)).
   - Logic puzzles: Knights, Knaves, Spies enumeration (2022 Q.6(a)) or culprit elimination (2023 Q.5(b)).
   - Digital circuit drawing from compound propositions (2023 Q.5(a)).
   - Fuzzy logic truth value operations (2022 Q.5(b)).

---

## 🔗 Topic Connections

- **Prerequisites:** Basic set theory concepts (subsets, union, intersection) connect directly to logical operations (predicates, disjunction, conjunction).
- **Leads directly to:**
  - [DM-4: Proof Techniques](../DM-4_Proof_Techniques/_Topic_Overview.md) where direct proofs, contraposition, and contradiction formalize logical arguments into mathematical proofs.
  - [DM-5: Number Theory](../DM-5_Number_Theory/_Topic_Overview.md) where logical definitions define divisibility and prime properties.
- **Pairs with in exams:**
  - Logic gates pair with digital electronics and Karnaugh maps.
  - System consistency checks pair with Boolean satisfiability algorithms in computer engineering.

---

[🏠 Master Index](../00_Index.md) | [Next: DM-3.1 Propositions →](DM-3.1_Propositions.md)
