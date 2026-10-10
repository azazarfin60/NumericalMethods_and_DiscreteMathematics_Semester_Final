[← Previous: DM-2.3 Partial Orders](DM-2.3_Partial_Orders.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: DM-3.1 Propositions →](../DM-3_Propositional_Logic/DM-3.1_Propositions.md)

---

# DM-2.4: Equivalence Relations

> ⚫ **Never examined.** This note exists for reading flow and complete syllabus coverage. Skim it to connect the ideas, but do not spend heavy study time here.

## What This Is

An equivalence relation groups elements that share a common feature. It splits an entire set into non-overlapping clusters called equivalence classes, creating a partition of the set.

## 📝 Key Definitions

> **Equivalence relation:** "A relation on a set $A$ is called an equivalence relation if it is reflexive, symmetric, and transitive." -- Rosen, §9.5
>
> **In simple words:** A relation that behaves like generalized equality. Every element relates to itself, connections are two-way, and chains carry through.

> **Equivalence class:** "Let $R$ be an equivalence relation on a set $A$. The set of all elements that are related to an element $a$ of $A$ is called the equivalence class of $a$. The equivalence class of $a$ with respect to $R$ is denoted by $[a]_R$." -- Rosen, §9.5
>
> **In simple words:** The club of all elements that are equivalent to $a$.

## The Partition Theorem

Every equivalence relation on a set $S$ partitions $S$ into disjoint, non-empty equivalence classes:

$$
\bigcup_{a \in S} [a] = S \quad \text{and} \quad [a] \cap [b] = \emptyset \quad \text{whenever } [a] \neq [b]
$$

A classic example is congruence modulo $m$ ($a \equiv b \pmod m$). On the integers $\mathbf{Z}$, congruence modulo 3 partitions all integers into three disjoint classes: $[0]_3$, $[1]_3$, and $[2]_3$.

## 🔗 Move On

This completes the DM-2 Relations folder. Next, proceed to the main exam topic of Section B: [DM-3.1 Propositions](../DM-3_Propositional_Logic/DM-3.1_Propositions.md).

---

[← Previous: DM-2.3 Partial Orders](DM-2.3_Partial_Orders.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: DM-3.1 Propositions →](../DM-3_Propositional_Logic/DM-3.1_Propositions.md)
