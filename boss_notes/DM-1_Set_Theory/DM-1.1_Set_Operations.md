[← Topic Overview](_Topic_Overview.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: DM-1.2 Algebraic Properties →](DM-1.2_Algebraic_Properties.md)

---

# DM-1.1: Set Operations

> ⚫ **Never examined.** This note exists for reading flow and syllabus completeness. Skim it in 3 minutes, but do not spend heavy study time here.

## What This Is

A set is an unordered collection of distinct objects. Set operations give us standard rules to combine and compare these collections.

---

## 📝 Key Definitions

> **Union:** "The union of the sets $A$ and $B$, denoted by $A \cup B$, is the set that contains those elements that are either in $A$ or in $B$, or in both." (Rosen, §2.2)
>
> **In simple words:** Merge everything from both sets into one common pool, dropping duplicates.

> **Intersection:** "The intersection of the sets $A$ and $B$, denoted by $A \cap B$, is the set containing those elements in both $A$ and $B$." (Rosen, §2.2)
>
> **In simple words:** Keep only the shared elements that appear in both sets. If $A \cap B = \emptyset$, the sets are disjoint.

> **Difference:** "The difference of $A$ and $B$, denoted by $A - B$, is the set containing those elements that are in $A$ but not in $B$." (Rosen, §2.2)
>
> **In simple words:** Take set $A$ and subtract away anything that also belongs to $B$.

> **Complement:** "Let $U$ be the universal set. The complement of the set $A$, denoted by $\overline{A}$, is $U - A$." (Rosen, §2.2)
>
> **In simple words:** Everything in the entire universe that is outside set $A$.

> **Cartesian Product:** "The Cartesian product of $A$ and $B$, denoted by $A \times B$, is the set of all ordered pairs $(a, b)$, where $a \in A$ and $b \in B$." (Rosen, §2.1)
>
> **In simple words:** Pair each element of $A$ with every element of $B$.

---

## Core Formulas

$$
A \cup B = \{x \mid x \in A \lor x \in B\}
$$

$$
A \cap B = \{x \mid x \in A \land x \in B\}
$$

$$
A - B = \{x \mid x \in A \land x \notin B\} = A \cap \overline{B}
$$

$$
\overline{A} = \{x \in U \mid x \notin A\}
$$

$$
A \times B = \{(a, b) \mid a \in A \land b \in B\}
$$

---

## 🔗 Move On

This subtopic has never appeared in RUET semester finals (2017 to 2024). Move forward to [DM-1.2: Algebraic Properties](DM-1.2_Algebraic_Properties.md).

---

[← Topic Overview](_Topic_Overview.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: DM-1.2 Algebraic Properties →](DM-1.2_Algebraic_Properties.md)
