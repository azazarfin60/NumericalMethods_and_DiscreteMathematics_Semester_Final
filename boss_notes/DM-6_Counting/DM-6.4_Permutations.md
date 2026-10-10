[← Previous: DM-6.3 Pigeonhole Principle](DM-6.3_Pigeonhole_Principle.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: DM-6.5 Combinations →](DM-6.5_Combinations.md)

---

# DM-6.4: Permutations

> ⚫ **Never examined standalone.** Skim this note to understand how ordering creates factorials, which explains why combinations divide by $r!$.

## What This Is (and Why It Matters)

A permutation is an ordered arrangement of distinct objects. If you have three runners finishing a sprint, the podium order $(A, B, C)$ is completely different from $(B, A, C)$, even though the exact same runners are standing on the stage.

In discrete mathematics, permutations bridge the gap between simple product-rule counting and combinations. Understanding permutations explains where factorials come from, and why combinations require dividing by $r!$.

---

## 📝 Key Definitions

> **Permutation:** "A **permutation** of a set of distinct objects is an ordered arrangement of these objects." (Rosen, §6.3, p. 23)
>
> **In simple words:** Lining up or arranging items where the exact sequence matters.

> **$r$-permutation count (Theorem 1 / Corollary 1):** "If $n$ and $r$ are integers with $0 \le r \le n$, then $P(n, r) = \dfrac{n!}{(n - r)!}$." (Rosen, §6.3, p. 24)
>
> **In simple words:** The number of ways to pick $r$ items out of $n$ available items and line them up in order.

> **Permutations with indistinguishable objects (Multiset Permutations):** "The number of different permutations of $n$ objects, where there are $n_1$ indistinguishable objects of type 1, $n_2$ of type 2, ..., and $n_k$ of type $k$, is $\dfrac{n!}{n_1! \, n_2! \cdots n_k!}$." (Rosen, §6.5, p. 42)
>
> **In simple words:** If some letters or items repeat, take $n!$ and divide by the factorial of each repeating count to cancel identical scrambles.

---

## The Core Idea

### Deriving the Formula from the Product Rule

Suppose you have $n$ distinct items and want to arrange $r$ of them in a row:
- Position 1: You have $n$ possible choices.
- Position 2: You have $n - 1$ remaining choices.
- Position 3: You have $n - 2$ remaining choices.
- Position $r$: You have $n - (r - 1) = n - r + 1$ remaining choices.

By the product rule, the total number of ordered arrangements is:

$$
P(n, r) = n(n - 1)(n - 2) \cdots (n - r + 1)
$$

Multiplying and dividing by $(n - r)!$:

$$
P(n, r) = \frac{n(n - 1)\cdots(n - r + 1) \cdot (n - r)!}{(n - r)!} = \frac{n!}{(n - r)!}
$$

When you arrange all $n$ items ($r = n$):

$$
P(n, n) = \frac{n!}{(n - n)!} = \frac{n!}{0!} = n!
$$

### Circular Permutations

When arranging $n$ distinct people around a round table:
- Linear seatings would give $n!$.
- However, rotating everyone clockwise by any number of seats produces the exact same circular arrangement.
- Each unique circular arrangement corresponds to $n$ different linear shifts.
- Applying the division rule:

$$
\text{Circular Arrangements} = \frac{n!}{n} = (n - 1)!
$$

### Permutations with Repetition (Multisets)

If certain objects are identical, swapping them produces no observable difference:

$$
\text{Distinct Arrangements} = \frac{n!}{n_1! \, n_2! \cdots n_k!}
$$

where $n_1 + n_2 + \dots + n_k = n$.

---

## 🔧 Classic Worked Examples

### Example 1: Arranging the Word `PROFESSOR`
How many distinct arrangements can be formed using all the letters of the word `PROFESSOR`?

1. Total letters: $n = 9$.
2. Count the frequencies of each letter:
   - P: 1
   - R: 2
   - O: 2
   - F: 1
   - E: 1
   - S: 2
3. Repeated letters: R appears 2 times, O appears 2 times, S appears 2 times.
4. Total distinct permutations:

$$
\text{Arrangements} = \frac{9!}{2! \cdot 2! \cdot 2!} = \frac{362880}{2 \cdot 2 \cdot 2} = \frac{362880}{8} = 45360
$$

### Example 2: Selecting 4 Letters from `PROFESSOR` (Raidah Class Notes §6.2)
If we form 4-letter arrangements from `PROFESSOR`, the solution splits into three cases depending on how many letters repeat:
- **Case 1 (All 4 distinct):** Choose 4 of the 6 letter types $\{P, R, O, F, E, S\}$ and arrange them: $\binom{6}{4} \times 4! = 15 \times 24 = 360$.
- **Case 2 (One pair + two distinct singles):** Choose 1 pair from $\{R, O, S\}$ (3 choices), choose 2 singles from remaining 5 types ($\binom{5}{2} = 10$), arrange them ($\frac{4!}{2!} = 12$): $3 \times 10 \times 12 = 360$.
- **Case 3 (Two pairs):** Choose 2 pairs from $\{R, O, S\}$ ($\binom{3}{2} = 3$), arrange them ($\frac{4!}{2! 2!} = 6$): $3 \times 6 = 18$.
- **Total Arrangements:** $360 + 360 + 18 = 738$.

---

## Permutations vs. Combinations

| Situation | Type | Question to Ask | Formula |
|:---|:---|:---|:---|
| Line up runners, assign ranks, award 1st/2nd/3rd, create passwords | **Permutation** | Does the order of items matter? **Yes.** | $P(n, r) = \dfrac{n!}{(n - r)!}$ |
| Pick a committee, select a crew, choose a subset, deal a poker hand | **Combination** | Does the order of items matter? **No.** | $C(n, r) = \dfrac{n!}{r!(n - r)!}$ |

Fahad notes (Class-20) sum this up concisely: selection leads to $C$, arrangement leads to $P$.

---

## ⚡ Quick Review

**The method in one sentence:** Permutations count ordered arrangements where the sequence of elements distinguishes outcomes.

**The formulas to memorize:**
$$
P(n, r) = \frac{n!}{(n - r)!} \qquad \text{Multiset: } \frac{n!}{n_1! \, n_2! \cdots n_k!}
$$

---

## 🔗 Move On

This subtopic has never been tested as a standalone question in RUET exams. It serves as the foundation for the next topic, where dividing out the $r!$ ordering factor gives the combination formula.

Head directly to: [DM-6.5: Combinations](DM-6.5_Combinations.md).

---

[← Previous: DM-6.3 Pigeonhole Principle](DM-6.3_Pigeonhole_Principle.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: DM-6.5 Combinations →](DM-6.5_Combinations.md)
