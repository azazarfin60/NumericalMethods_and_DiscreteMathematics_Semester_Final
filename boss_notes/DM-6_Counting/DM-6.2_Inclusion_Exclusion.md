[← Previous: DM-6.1 Sum and Product Rules](DM-6.1_Sum_and_Product_Rules.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: DM-6.3 Pigeonhole Principle →](DM-6.3_Pigeonhole_Principle.md)

---

# DM-6.2: Inclusion-Exclusion Principle

> ⚫ **Never examined.** This note exists for reading flow and conceptual completeness. Skim it to connect the ideas, but do not spend heavy study time here.

## What This Is (and Why It Matters)

The sum rule works only when your alternatives share zero common items. But what happens in real life when options overlap? If you ask how many students are taking Computer Networks or Electronics, adding the two class rosters counts students enrolled in both courses twice.

The Principle of Inclusion-Exclusion (also called the subtraction rule) fixes this overcount. It tells you to add the individual sets together, and then subtract the intersection so that shared elements are counted exactly once.

---

## 📝 Key Definitions

> **Subtraction rule (Inclusion-Exclusion for two sets):** "If a task can be done in either $n_1$ ways or $n_2$ ways, then the number of ways to do the task is $n_1 + n_2$ minus the number of ways to do the task that are common to the two different ways." (Rosen, §6.1, p. 9)
>
> **In simple words:** Add the sizes of the two groups, then subtract the items that belong to both groups so you do not double-count them.

> **General Principle of Inclusion-Exclusion:** For finite sets $A_1, A_2, \dots, A_n$, the size of their union is found by alternating sums: add the sizes of individual sets, subtract all pairwise intersections, add all three-way intersections, and continue alternating signs until the intersection of all $n$ sets is reached.
>
> **In simple words:** Add the singles, subtract the doubles, add back the triples, and keep alternating plus and minus.

---

## The Core Idea

### The Two-Set Formula

For any two finite sets $A$ and $B$, the size of their union is:

$$
|A \cup B| = |A| + |B| - |A \cap B|
$$

**Why this formula works:**
When you compute $|A| + |B|$, every element that belongs strictly to $A$ is counted once, and every element strictly in $B$ is counted once. But every element in the shared overlap $A \cap B$ gets counted in $|A|$ and again in $|B|$. Subtracting $|A \cap B|$ removes that second count, leaving every element counted exactly once.

### The Three-Set Formula

When three sets $A$, $B$, and $C$ overlap:

$$
|A \cup B \cup C| = |A| + |B| + |C| - \left(|A \cap B| + |A \cap C| + |B \cap C|\right) + |A \cap B \cap C|
$$

**Why the triple intersection is added back:**
Summing the individual sets counts elements in all three sets three times. Subtracting the pairwise intersections subtracts them three times ($3 - 3 = 0$), completely erasing them from the total. Adding back $|A \cap B \cap C|$ restores their correct single count.

---

## 🔧 Worked Examples

### Example 1: Bit Strings with Specific Patterns (Rosen Example 18)
How many bit strings of length 8 either start with a 1 bit or end with the two bits 00?

Let $S$ be the set of all 8-bit strings:
- Let $A$ be the set of 8-bit strings starting with 1. The remaining 7 bits are free: $|A| = 2^7 = 128$.
- Let $B$ be the set of 8-bit strings ending with 00. The first 6 bits are free: $|B| = 2^6 = 64$.
- Let $A \cap B$ be the strings that start with 1 **and** end with 00. The middle 5 bits are free: $|A \cap B| = 2^5 = 32$.

Applying the subtraction rule:

$$
|A \cup B| = |A| + |B| - |A \cap B| = 128 + 64 - 32
$$

$$
\text{Total Valid Strings} = 160
$$

### Example 2: Integers Divisible by 2 or 3
How many positive integers from 1 to 100 are divisible by 2 or 3?
- Integers divisible by 2: $|A| = \lfloor 100 / 2 \rfloor = 50$.
- Integers divisible by 3: $|B| = \lfloor 100 / 3 \rfloor = 33$.
- Integers divisible by both 2 and 3 (divisible by $\text{lcm}(2, 3) = 6$): $|A \cap B| = \lfloor 100 / 6 \rfloor = 16$.

By the principle of inclusion-exclusion:

$$
|A \cup B| = 50 + 33 - 16 = 67
$$

---

## ⚡ Quick Review

**The method in one sentence:** When counting alternatives with overlap, add the separate totals and subtract the intersection.

**The formula to remember:**
$$
|A \cup B| = |A| + |B| - |A \cap B|
$$

---

## 🔗 Move On

This subtopic has never appeared in any RUET semester final paper (2017 to 2024). It exists here solely to show you why the sum rule requires disjoint sets.

If you are revising for exams, do not spend further time here. Head straight to the heavyweight topic: [DM-6.3: Pigeonhole Principle](DM-6.3_Pigeonhole_Principle.md).

---

[← Previous: DM-6.1 Sum and Product Rules](DM-6.1_Sum_and_Product_Rules.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: DM-6.3 Pigeonhole Principle →](DM-6.3_Pigeonhole_Principle.md)
