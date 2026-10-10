[← Previous: DM-1.3 Computer Representation](DM-1.3_Computer_Representation.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: DM-2 Relations Overview →](../DM-2_Relations/_Topic_Overview.md)

---

# DM-1.4: The Power Set Theorem

> ⚫ **Never examined.** This note exists for reading flow and syllabus completeness. Skim it in 3 minutes to grasp subset cardinality.

## What This Is

Many computational algorithms evaluate every possible configuration of a system. The power set gathers all those subsets into a single collection.

---

## 📝 Key Definitions

> **Power Set:** "Given a set $S$, the power set of $S$ is the set of all subsets of the set $S$. The power set of $S$ is denoted by $\mathcal{P}(S)$." (Rosen, §2.1)
>
> **In simple words:** A master set holding every subset you can form from $S$, including the empty set and $S$ itself.

> **The Power Set Theorem:** "If a set $S$ has $n$ elements, then its power set has $2^n$ elements." (Rosen, §2.1)
>
> **In simple words:** Every element has two binary choices: present or absent. For $n$ items, this yields $2 \times 2 \times \dots \times 2 = 2^n$ possible subsets.

---

## Concrete Examples

Let $S = \{a, b, c\}$ with $|S| = 3$:

$$
\mathcal{P}(S) = \{\emptyset, \{a\}, \{b\}, \{c\}, \{a, b\}, \{a, c\}, \{b, c\}, \{a, b, c\}\}
$$

$$
|\mathcal{P}(S)| = 2^3 = 8
$$

### Edge Cases
- For the empty set: $\mathcal{P}(\emptyset) = \{\emptyset\}$, so $|\mathcal{P}(\emptyset)| = 2^0 = 1$.
- For a singleton containing the empty set: $\mathcal{P}(\{\emptyset\}) = \{\emptyset, \{\emptyset\}\}$, so $|\mathcal{P}(\{\emptyset\})| = 2^1 = 2$.

---

## Two Ways to Prove $|\mathcal{P}(S)| = 2^n$

### 1. The Product Rule of Counting (Bit Strings)
Building a subset corresponds to writing an $n$-bit string. For each element $a_i \in S$, we have 2 choices: include it ($1$) or exclude it ($0$). By the product rule of counting, there are $2 \times 2 \times \dots \times 2 = 2^n$ distinct bit strings. Each unique bit string specifies exactly one subset.

### 2. Mathematical Induction
- **Base Step ($n = 0$):** If $S = \emptyset$, its only subset is $\emptyset$. So $|\mathcal{P}(\emptyset)| = 1 = 2^0$. The claim holds for $n = 0$.
- **Inductive Step:** Assume any set with $k$ elements has $2^k$ subsets. Let $T = S \cup \{x\}$ have $k+1$ elements. Every subset of $T$ either does not contain $x$ (there are $2^k$ such subsets) or does contain $x$ (there are another $2^k$ such subsets). The total count is $2^k + 2^k = 2 \times 2^k = 2^{k+1}$.

---

## 🔗 Move On

This subtopic has never appeared in RUET semester finals (2017 to 2024). You have finished DM-1: Set Theory! Proceed to the next topic in Section B: [DM-2: Relations](../DM-2_Relations/_Topic_Overview.md).

---

[← Previous: DM-1.3 Computer Representation](DM-1.3_Computer_Representation.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: DM-2 Relations Overview →](../DM-2_Relations/_Topic_Overview.md)
