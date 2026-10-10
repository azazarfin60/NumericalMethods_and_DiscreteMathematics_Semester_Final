[← Previous: DM-1.2 Algebraic Properties](DM-1.2_Algebraic_Properties.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: DM-1.4 Power Set →](DM-1.4_Power_Set.md)

---

# DM-1.3: Computer Representation of Sets

> ⚫ **Never examined.** This note exists for reading flow and syllabus completeness. Skim it in 3 minutes to see how computers store sets.

## What This Is

Storing sets as raw lists makes union and intersection slow because the computer must search through arrays. When the universal set $U$ is finite and ordered, we store each subset as a compact string of bits.

---

## 📝 Key Definitions

> **Bit String Representation:** "Represent a subset $A$ of $U$ with the bit string of length $n$, where the $i$th bit in this string is 1 if $a_i$ belongs to $A$ and is 0 if $a_i$ does not belong to $A$." (Rosen, §2.2)
>
> **In simple words:** A bit string where the $i$-th bit is 1 if element $a_i$ is in the set, and 0 if it is absent.

---

## Core Operations via Bitwise Logic

Let the universal set be $U = \{1, 2, 3, 4, 5\}$ in natural order.

Consider two subsets:
- $A = \{1, 3, 5\} \implies \text{Bit string } = 10101$
- $B = \{2, 3, 4\} \implies \text{Bit string } = 01110$

Set operations map directly to bitwise Boolean operations:

### 1. Union ($A \cup B$) $\to$ Bitwise OR ($\lor$)
$$
10101 \lor 01110 = 11111 \implies \{1, 2, 3, 4, 5\}
$$

### 2. Intersection ($A \cap B$) $\to$ Bitwise AND ($\land$)
$$
10101 \land 01110 = 00100 \implies \{3\}
$$

### 3. Complement ($\overline{A}$) $\to$ Bitwise NOT ($\neg$)
$$
\neg(10101) = 01010 \implies \{2, 4\}
$$

### 4. Difference ($A - B = A \cap \overline{B}$) $\to$ Bitwise $A \land \neg B$
$$
10101 \land \neg(01110) = 10101 \land 10001 = 10001 \implies \{1, 5\}
$$

---

## Why Engineers Care

Bit strings turn set theory into hardware logic gates. Modern 64-bit CPU registers can process set unions and intersections of 64 elements in a single clock cycle. This is the exact mechanism behind bitmasks in embedded systems, access control matrices in operating systems, and network subnet masks.

---

## 🔗 Move On

This subtopic has never appeared in RUET semester finals (2017 to 2024). Move forward to [DM-1.4: The Power Set Theorem](DM-1.4_Power_Set.md).

---

[← Previous: DM-1.2 Algebraic Properties](DM-1.2_Algebraic_Properties.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: DM-1.4 Power Set →](DM-1.4_Power_Set.md)
