# DM-1: Set Theory

> **Section:** Section B (Discrete Mathematics)  
> **Subtopics in this folder:** 4 files (DM-1.1 to DM-1.4)  
> **Exam weight:** Appears in 0/8 papers (0% frequency: never examined in 2017 to 2024 RUET finals).

---

## 📖 How to Read This Topic

Set theory is the foundation of discrete mathematics. Sets provide the basic vocabulary for binary relations, formal logic, number theory, and combinatorics.

In RUET exams, DM-1 has never been tested in final exam papers (2022 to 2024). Examiners focus their Section B marks on Propositional Logic (DM-3), Number Theory (DM-5), and Counting (DM-6). But class tests and the course syllabus cover set theory fully.

Here is the learning flow:
- Start with **DM-1.1** to master the five fundamental operations: union, intersection, difference, complement, and Cartesian product.
- Proceed to **DM-1.2** for algebraic set identities and De Morgan's laws. These directly parallel logical equivalences in DM-3.
- Skim **DM-1.3** to see how computers store sets as bit strings and execute set operations via fast bitwise logic gates.
- Finish with **DM-1.4** to understand the Power Set Theorem, which links set theory to combinatorial counting.

**Suggested reading time:** ~15 minutes for the entire folder.

---

## 📑 Subtopic Index

| # | File | Priority | Exam Freq | Reading Time | Core Concept |
|:---:|:---|:---:|:---:|:---:|:---|
| 1 | [DM-1.1: Set Operations](DM-1.1_Set_Operations.md) | ⚫ | 0/8 papers | ~4 min | Union, intersection, difference, complement, Cartesian product, Venn diagrams |
| 2 | [DM-1.2: Algebraic Properties](DM-1.2_Algebraic_Properties.md) | ⚫ | 0/8 papers | ~4 min | Identity, domination, distributive laws, De Morgan's laws, membership tables |
| 3 | [DM-1.3: Computer Representation](DM-1.3_Computer_Representation.md) | ⚫ | 0/8 papers | ~3 min | Characteristic bit vectors, bitwise AND/OR/NOT operations |
| 4 | [DM-1.4: The Power Set Theorem](DM-1.4_Power_Set.md) | ⚫ | 0/8 papers | ~4 min | Power set $\mathcal{P}(S)$, cardinality theorem $\lvert\mathcal{P}(S)\rvert = 2^n$, binary choice proof |

---

## 🎯 Exam Pattern for This Topic

Although DM-1 has not appeared in semester final papers, it is a frequent source of short questions in class tests:

### 1. Set Operations and Venn Diagrams
Questions give two or three small sets and ask for union, intersection, difference, or symmetric difference $A \oplus B = (A - B) \cup (B - A)$.

### 2. Proving Set Identities
Examiners test De Morgan's laws ($\overline{A \cap B} = \overline{A} \cup \overline{B}$) using membership tables (0/1 truth tables) or double containment ($A \subseteq B$ and $B \subseteq A$).

### 3. Bit String Representation
Given a small universal set $U$, write the bit vectors for subsets $A$ and $B$, then find $A \cup B$ and $A \cap B$ using bitwise OR and AND.

### 4. Power Set Cardinality
State the Power Set Theorem and list all $2^n$ subsets for a given set with $n=3$ elements.

---

## 🔗 Topic Connections

- **Prerequisites:**
  - Basic high school algebra and arithmetic.
- **Leads to:**
  - [DM-2: Relations](../DM-2_Relations/_Topic_Overview.md): Relations are defined as subsets of the Cartesian product $A \times B$.
  - [DM-3: Propositional Logic](../DM-3_Propositional_Logic/_Topic_Overview.md): Set operations map directly to logic connectives ($\cap \leftrightarrow \land$, $\cup \leftrightarrow \lor$, $\overline{A} \leftrightarrow \neg$).
  - [DM-6: Counting](../DM-6_Counting/_Topic_Overview.md): The Principle of Inclusion-Exclusion (PIE) counts set unions.
- **Previous topic in syllabus:**
  - [NM-10: Partial Differential Equations](../NM-10_PDE/_Topic_Overview.md) (End of Section A).
- **Next topic in syllabus:**
  - [DM-2: Relations](../DM-2_Relations/_Topic_Overview.md).
