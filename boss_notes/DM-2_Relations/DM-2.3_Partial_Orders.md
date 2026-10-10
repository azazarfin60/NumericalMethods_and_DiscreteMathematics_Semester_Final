[← Previous: DM-2.2 Binary Relations](DM-2.2_Binary_Relations.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: DM-2.4 Equivalence Relations →](DM-2.4_Equivalence_Relations.md)

---

# DM-2.3: Partial Orders

> ⚫ **Never examined.** This note exists for reading flow and complete syllabus coverage. Skim it to connect the ideas, but do not spend heavy study time here.

## What This Is

A partial order is a relation that ranks elements without forcing every pair to be comparable. Examples include prerequisites in a degree curriculum, divisibility among integers, and task schedules in project management.

## 📝 Key Definitions

> **Partial order and poset:** "A relation $R$ on a set $S$ is called a partial ordering or partial order if it is reflexive, antisymmetric, and transitive. A set $S$ together with a partial ordering $R$ is called a partially ordered set, or poset, and is denoted by $(S, R)$." -- Rosen, §9.6
>
> **In simple words:** An ordering where some items can be compared, but some items may not be comparable to each other.

> **Hasse diagram:** "A graphical representation of a finite poset where loops and all edges resulting from the transitive property are removed, and the direction of edges is upward from initial to terminal vertex without arrows." -- Rosen, §9.6
>
> **In simple words:** A clean hierarchy tree drawn bottom-to-top. You delete self-loops and shortcut arrows to show only the direct covering steps.

## Key Poset Concepts

- **Comparable:** Two elements $a$ and $b$ are comparable if $a \preceq b$ or $b \preceq a$. Otherwise, they are incomparable (like 2 and 3 under divisibility).
- **Total order (chain):** A poset where every pair of elements is comparable (like numbers with $\le$).
- **Lattice:** A poset where every pair of elements has a unique least upper bound (LUB) and greatest lower bound (GLB).

## 🔗 Move On

This topic has never appeared in any RUET exam paper (2017–2024). Next, see relations that group similar objects together in [DM-2.4 Equivalence Relations](DM-2.4_Equivalence_Relations.md).

---

[← Previous: DM-2.2 Binary Relations](DM-2.2_Binary_Relations.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: DM-2.4 Equivalence Relations →](DM-2.4_Equivalence_Relations.md)
