[← Previous: DM-2.1 Properties of Relations](DM-2.1_Properties_of_Relations.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: DM-2.3 Partial Orders →](DM-2.3_Partial_Orders.md)

---

# DM-2.2: Binary Relations

> ⚫ **Never examined.** This note exists for reading flow and complete syllabus coverage. Skim it to connect the ideas, but do not spend heavy study time here.

## What This Is

A binary relation from set $A$ to set $B$ is any subset of the Cartesian product $A \times B$. Computers represent relations with zero-one matrices, while humans visualize them with directed graphs (digraphs).

## 📝 Key Definitions

> **Binary relation:** "Let $A$ and $B$ be sets. A binary relation from $A$ to $B$ is a subset of $A \times B$." -- Rosen, §9.1
>
> **In simple words:** A list of ordered pairs $(a, b)$ that says which inputs from $A$ pair with which outputs from $B$.

> **Zero-one matrix:** "The relation $R$ can be represented by the matrix $\mathbf{M}_R = [m_{ij}]$, where $m_{ij} = 1$ if $(a_i, b_j) \in R$, and $m_{ij} = 0$ if $(a_i, b_j) \notin R$." -- Rosen, §9.3
>
> **In simple words:** A table with 1 if a pair exists, and 0 if it does not.

## Reading Properties

- **Reflexive:** Matrix has 1s down the main diagonal. Digraph has loops at every vertex.
- **Symmetric:** Matrix equals its transpose ($\mathbf{M}_R = \mathbf{M}_R^T$). Digraph has two-way arrows between connected nodes.
- **Antisymmetric:** No off-diagonal symmetric 1s. Digraph has no opposing arrows between distinct nodes.

## 🔗 Move On

This topic has never appeared in any RUET exam paper (2017–2024). Next, see how relations order objects in [DM-2.3 Partial Orders](DM-2.3_Partial_Orders.md).

---

[← Previous: DM-2.1 Properties of Relations](DM-2.1_Properties_of_Relations.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: DM-2.3 Partial Orders →](DM-2.3_Partial_Orders.md)
