[← Previous: DM-1.1 Set Operations](DM-1.1_Set_Operations.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: DM-1.3 Computer Representation →](DM-1.3_Computer_Representation.md)

---

# DM-1.2: Algebraic Properties of Sets

> ⚫ **Never examined.** This note exists for reading flow and syllabus completeness. Skim it in 3 minutes to grasp set identities.

## What This Is

Set operations follow algebraic laws just like ordinary arithmetic. These identities let you simplify complex set expressions without drawing Venn diagrams every time.

---

## 📝 Key Definitions

> **Set Identity:** "An identity is an equation involving sets that is true for all possible sets substituted for the variables." (Rosen, §2.2)
>
> **In simple words:** A universal equivalence between set expressions that always holds true.

> **De Morgan's Laws for Sets:** "The complement of the union of two sets is the intersection of their complements, and the complement of the intersection of two sets is the union of their complements." (Rosen, §2.2)
>
> **In simple words:** Negating an intersection flips it into a union of complements, and negating a union flips it into an intersection of complements.

$$
\overline{A \cap B} = \overline{A} \cup \overline{B}
$$

$$
\overline{A \cup B} = \overline{A} \cap \overline{B}
$$

---

## Key Set Identities at a Glance

| Identity Law | Formula |
|:---|:---|
| **Identity Laws** | $A \cap U = A$, $\quad A \cup \emptyset = A$ |
| **Domination Laws** | $A \cup U = U$, $\quad A \cap \emptyset = \emptyset$ |
| **Idempotent Laws** | $A \cup A = A$, $\quad A \cap A = A$ |
| **Double Complement** | $\overline{\overline{A}} = A$ |
| **Commutative Laws** | $A \cup B = B \cup A$, $\quad A \cap B = B \cap A$ |
| **Associative Laws** | $A \cup (B \cup C) = (A \cup B) \cup C$, $\quad A \cap (B \cap C) = (A \cap B) \cap C$ |
| **Distributive Laws** | $A \cap (B \cup C) = (A \cap B) \cup (A \cap C)$<br>$A \cup (B \cap C) = (A \cup B) \cap (A \cup C)$ |
| **Absorption Laws** | $A \cup (A \cap B) = A$, $\quad A \cap (A \cup B) = A$ |
| **Complement Laws** | $A \cup \overline{A} = U$, $\quad A \cap \overline{A} = \emptyset$ |

---

## How to Prove Set Identities

Rosen §2.2 outlines three proof methods:
1. **Double containment:** Prove $X \subseteq Y$ and $Y \subseteq X$.
2. **Membership tables:** Build a 0/1 table for all membership combinations. If the two result columns match, the sets are identical.
3. **Set builder translation:** Convert set conditions to logic formulas and apply propositional equivalence laws.

---

## 🔗 Move On

This subtopic has never appeared in RUET semester finals (2017 to 2024). Move forward to [DM-1.3: Computer Representation of Sets](DM-1.3_Computer_Representation.md).

---

[← Previous: DM-1.1 Set Operations](DM-1.1_Set_Operations.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: DM-1.3 Computer Representation →](DM-1.3_Computer_Representation.md)
