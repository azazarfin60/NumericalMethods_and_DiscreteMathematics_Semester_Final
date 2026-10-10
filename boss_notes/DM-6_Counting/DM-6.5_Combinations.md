[← Previous: DM-6.4 Permutations](DM-6.4_Permutations.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: DM-6.6 Binomial Theorem →](DM-6.6_Binomial_Theorem.md)

---

# DM-6.5: Combinations

> 🟠 **Priority:** Secondary | **Tested:** 2023 Q.8(b) | **Typical marks:** 3

## What This Is (and Why It Matters)

A combination is an unordered selection of items from a set. If you are picking a six-person astronaut crew for a mission, the team $\{A, B, C, D, E, F\}$ is the exact same crew no matter which name you write down first on the roster.

In the RUET semester final, combinations test your ability to distinguish unordered selection from ordered arrangement, calculate large factorial fractions safely without overflow, and avoid the classic pairwise cancellation trap that costs many students full marks.

---

## 📝 Key Definitions

> **Combination:** "An **$r$-combination** of elements of a set is an unordered selection of $r$ elements from the set. Thus, an $r$-combination is simply a subset of the set with $r$ elements." (Rosen, §6.3, p. 26)
>
> **In simple words:** Choosing $r$ items from a larger pool where the order of choosing does not matter.

> **Combination count (Theorem 2):** "The number of $r$-combinations of a set with $n$ elements, where $n$ is a nonnegative integer and $r$ is an integer with $0 \le r \le n$, equals $C(n, r) = \dfrac{n!}{r!(n - r)!}$." (Rosen, §6.3, p. 26)
>
> **In simple words:** The formula for the number of ways to pick $r$ items out of $n$, denoted as $C(n, r)$ or $\binom{n}{r}$.

> **Combinatorial symmetry identity (Corollary 2):** "Let $n$ and $r$ be nonnegative integers with $r \le n$. Then $C(n, r) = C(n, n - r)$." (Rosen, §6.3, p. 27)
>
> **In simple words:** Choosing which $r$ items to include is the exact same decision as choosing which $n - r$ items to leave behind.

---

## The Core Idea

### Why the Formula Divides Permutations by $r!$

To see why the combination formula works, connect it back to permutations using the division rule:

1. Suppose you first arrange $r$ items out of $n$ in order. By the product rule, this gives $P(n, r) = \frac{n!}{(n - r)!}$ ordered sequences.
2. In that list of permutations, every distinct subset of $r$ items appears exactly $r!$ times, corresponding to the $r!$ different ways to arrange those $r$ specific items.
3. Because order does not matter in a combination, all $r!$ arrangements represent the exact same subset.
4. By the division rule:

$$
C(n, r) = \frac{P(n, r)}{r!} = \frac{n!}{r!(n - r)!}
$$

### The Symmetry Property: $\binom{n}{r} = \binom{n}{n - r}$

Whenever $r > n/2$, you should always use the symmetry identity before doing any arithmetic:

$$
\binom{n}{r} = \binom{n}{n - r}
$$

**Why this is true:**
If a committee of 27 people needs to select 25 delegates, choosing the 25 people who attend is identical to choosing the 2 people who stay behind. The arithmetic $\binom{27}{2} = \frac{27 \times 26}{2} = 351$ takes ten seconds, whereas computing $\binom{27}{25}$ directly with large factorials invites arithmetic mistakes.

### Safe Factorial Calculation Strategy

Never attempt to evaluate large factorials like $30!$ directly; they will overflow standard calculator registers and lead to precision loss.

Always cancel the $(n - r)!$ tail from the numerator first:

$$
\binom{n}{r} = \frac{n(n - 1)(n - 2)\cdots(n - r + 1)}{r(r - 1)\cdots 2 \cdot 1}
$$

The recipe is:
1. Write the falling product of $r$ terms in the numerator.
2. Write the complete factorial $r!$ in the denominator.
3. Multiply the whole numerator product, or cancel common factors deliberately.
4. Divide the complete numerator by the complete denominator.

> [!WARNING] The Pairwise Cancellation Trap
> When evaluating $\binom{30}{6}$, students often attempt to divide individual pairs:
>
> $\frac{30 \cdot 29}{2} \times \frac{28 \cdot 27}{6} \times (26 \cdot 25) = 435 \times 126 \times 650 = 35{,}626{,}500$
>
> **This answer is 60 times too large!**
>
> The reason for this disaster is that dividing by 2 and 6 only cancels a factor of $2 \times 6 = 12$, whereas the actual denominator is $6! = 720$. The missing divisor $720 / 12 = 60$ remains in the numerator.
>
> To cancel safely, either cancel factors that multiply completely to 720, or compute the paired numerator product and divide by 720 in one step.

---

## 🏆 Past Exam Questions

### 2023 Q.8(b): Mars Astronaut Mission Crew Selection [03 Marks]

> **The Question:** A group of 30 people have been trained as astronauts to go on the first mission to mars. How many ways are there to select a crew of six people to go on this mission (assuming all crew members have the same job)?

**Let's solve this step by step like a tutor:**

**Step 1: Determine whether order matters.**
The problem asks to select a crew of 6 people from 30 candidates, explicitly noting that *all crew members have the same job*.
Because every crew member shares the identical role, there is no commander, pilot, or specialist distinction. The team $\{A, B, C, D, E, F\}$ is the same team regardless of the sequence of selection.
Therefore, this is a combination problem:

$$
\text{Ways} = \binom{30}{6} = C(30, 6) = \frac{30!}{6! \, (30 - 6)!} = \frac{30!}{6! \, 24!}
$$

**Step 2: Set up the canceled factorial ratio.**
Cancel the common $24!$ from numerator and denominator:

$$
\binom{30}{6} = \frac{30 \cdot 29 \cdot 28 \cdot 27 \cdot 26 \cdot 25}{6 \cdot 5 \cdot 4 \cdot 3 \cdot 2 \cdot 1} = \frac{30 \cdot 29 \cdot 28 \cdot 27 \cdot 26 \cdot 25}{720}
$$

**Step 3: Compute the numerator product.**
To keep mental arithmetic and calculator inputs manageable, group the numerator terms in three clean pairs:

$$
30 \cdot 29 = 870
$$

$$
28 \cdot 27 = 756
$$

$$
26 \cdot 25 = 650
$$

Now multiply the three partial products:

$$
870 \times 756 \times 650 = 427{,}518{,}000
$$

**Step 4: Divide by $6! = 720$.**

$$
\frac{427518000}{720} = 593775
$$

$$
\boxed{\binom{30}{6} = 593775 \text{ ways}}
$$

**Quick sanity checks:**
1. Direct evaluation of $\frac{30!}{6! \, 24!}$ confirms $593775$.
2. The ordered permutation count is $P(30, 6) = 427{,}518{,}000$. Dividing this by $6! = 720$ gives $593775$, confirming that the ordered count is exactly 720 times the combination count.

> [!NOTE] Why the Problem's Assumption Matters
> The statement *"assuming all crew members have the same job"* is the exact reason this is a combination.
>
> - If the mission had **distinct roles** (e.g., Commander, Pilot, Navigator, Engineer, Medic, Scientist), the count would be the permutation $P(30, 6) = 427{,}518{,}000$ (720 times larger).
> - If the crew had **one designated Commander** while the other five members were general crew, we would pick the commander first ($30$ ways) and then the remaining 5 from 29 ($\binom{29}{5} = 118{,}755$), yielding $30 \times 118{,}755 = 3{,}562{,}650$ ways.
>
> Identifying the role structure is what distinguishes an expert solution from a guess.

---

## ⚡ Quick Review

**The method in one sentence:** Use combinations $C(n, r)$ when selecting an unordered subset where all chosen members share equal status.

**The formula you must memorize:**
$$
C(n, r) = \binom{n}{r} = \frac{n!}{r!(n - r)!} = \frac{n(n - 1)\cdots(n - r + 1)}{r!}
$$

**The most common exam mistake:** Falling into the pairwise cancellation trap. Always verify that your canceled denominator factors multiply to the full value of $r!$.

**Time estimate in exam:** 3 to 4 minutes for a 3-mark question.

---

## 🔗 Connected Topics

- [← Previous: DM-6.4 Permutations](DM-6.4_Permutations.md): Permutations provide the ordered count $P(n, r)$ which combinations divide by $r!$.
- [→ Next: DM-6.6 Binomial Theorem](DM-6.6_Binomial_Theorem.md): The combination numbers $\binom{n}{r}$ appear as the coefficients in binomial expansions.
- [DM-1.4: Power Set](../DM-1_Set_Theory/DM-1.4_Power_Set.md): The total number of all subsets of an $n$-element set is $\sum_{r=0}^n \binom{n}{r} = 2^n$.

---

[← Previous: DM-6.4 Permutations](DM-6.4_Permutations.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: DM-6.6 Binomial Theorem →](DM-6.6_Binomial_Theorem.md)
