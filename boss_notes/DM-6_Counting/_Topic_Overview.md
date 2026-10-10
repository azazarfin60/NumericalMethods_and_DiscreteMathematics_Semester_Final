# DM-6: Counting

> **Section:** Section B (Discrete Mathematics)
> **Subtopics in this folder:** 6 files (DM-6.1 through DM-6.6)
> **Exam weight:** Appears in all 3 DM papers (2022, 2023, 2024), representing a 100% appearance rate in Section B. Typically featured in Question 8, carrying between 6 and 9 marks per paper.

---

## 📖 How to Read This Topic

Counting sounds like child's play until you have to calculate how many valid IP addresses exist, how many states a finite automaton can take, or how many ways packets can collide in a network buffer. In computer engineering and discrete mathematics, counting is the science of finding the exact size of discrete sets without listing all their elements one by one.

In RUET examinations, counting questions in Section B are high-yield and predictable. If you master the core rules and watch out for a few classic arithmetic traps, Question 8 can easily become a source of full marks.

Read the subtopics in this natural order:

1. **DM-6.1 (Sum and Product Rules):**
   The two foundational pillars. If a process happens in sequential stages ("and then"), multiply using the product rule. If choices are mutually exclusive alternatives ("either/or"), add using the sum rule.

2. **DM-6.2 (Inclusion-Exclusion Principle):**
   What happens when alternatives overlap? The simple sum rule overcounts shared elements, so the subtraction rule steps in to subtract the overlap.

3. **DM-6.3 (Pigeonhole Principle):**
   The single most tested discrete math topic in RUET. It does not count exact possibilities; instead, it provides a deterministic guarantee. If you put more pigeons than pigeonholes, at least one hole must contain multiple pigeons.

4. **DM-6.4 (Permutations):**
   Arrangements where the sequence matters. This explains where factorials come from and provides the bridge to combinations.

5. **DM-6.5 (Combinations):**
   Selections where order does not matter, such as choosing a team or an astronaut crew. Learn the division rule that cancels $r!$ and watch out for the deadly pairwise cancellation trap.

6. **DM-6.6 (Binomial Theorem):**
   Expanding powers of $(x + y)^n$, reading general terms $T_{r+1}$, and extracting large numerical coefficients without expanding the entire polynomial.

**Suggested reading time:** ~35 minutes for the entire folder.

---

## 📑 Subtopic Index

| # | File | Priority | Exam Freq | Reading Time | Core Concept |
|:---:|:---|:---:|:---:|:---:|:---|
| 1 | [DM-6.1: Sum and Product Rules](DM-6.1_Sum_and_Product_Rules.md) | 🟠 | 2022 (1 appearance) | ~6 min | Sequential stages (multiply) vs disjoint alternatives (add) |
| 2 | [DM-6.2: Inclusion-Exclusion](DM-6.2_Inclusion_Exclusion.md) | ⚫ | Never examined | ~4 min | Overlapping sets, subtraction rule, Venn diagram logic |
| 3 | [DM-6.3: Pigeonhole Principle](DM-6.3_Pigeonhole_Principle.md) | 🔴 | 2022, 2023, 2024 (all 3 papers) | ~12 min | Plain vs generalized forms, modulo remainder proofs, hash collisions |
| 4 | [DM-6.4: Permutations](DM-6.4_Permutations.md) | ⚫ | Never examined standalone | ~5 min | Ordered arrangements, factorials, circular tables, multisets |
| 5 | [DM-6.5: Combinations](DM-6.5_Combinations.md) | 🟠 | 2023 (1 appearance) | ~6 min | Unordered selections $C(n, r)$, astronaut crew, cancellation safety |
| 6 | [DM-6.6: Binomial Theorem](DM-6.6_Binomial_Theorem.md) | 🟠 | 2023 (1 appearance) | ~8 min | $(x+y)^n$ expansion, general term $T_{r+1}$, coefficient extraction |

---

## 🎯 Exam Pattern for This Topic

In the RUET ECE 2213 semester final, counting problems consistently appear in **Question 8** of Section B. Across the papers from 2022 to 2024, the questions fall into distinct recurring patterns:

### Pattern 1: Sequential Choices vs Mutually Exclusive Alternatives (2 Marks)
The exam presents a practical journey or scenario (such as routes from Boston to Los Angeles via Detroit in 2022 Q.8(b)):
- Identify whether the task is broken into sequential stages or mutually exclusive branches.
- State the governing rule explicitly before computing (writing "By the product rule" earns the method mark).
- Compute the product or sum cleanly.

### Pattern 2: Pigeonhole Principle Real-World Applications (2 Marks)
Tested in 2022 Q.8(c), 2023 Q.8(a), and repeated verbatim in 2024 Q.8(c):
- Distinguish between the **plain form** ($N > k$) and the **generalized form** ($N > mk$).
- Provide deterministic engineering or daily life examples: hash table bucket collisions, drawer socks, class birth months, or server rack distribution.
- State clearly why deterministic guarantees differ from probabilistic claims (such as the 23-person birthday paradox).

### Pattern 3: Pigeonhole Congruence Proofs (2 Marks)
Tested in 2022 Q.8(d):
- Prove that among any $d + 1$ integers, two must share the same remainder modulo $d$.
- Explicitly map integers to objects and the $d$ possible remainders $\{0, 1, \dots, d-1\}$ to boxes.
- Show that sharing a remainder implies their difference is a multiple of $d$.

### Pattern 4: Selection and Combination without Order (3 Marks)
Tested in 2023 Q.8(b) (selecting 6 astronaut crew members from 30 candidates):
- Confirm that order does not matter and all roles are identical, establishing that the problem requires $C(n, r) = \binom{n}{r}$.
- Compute large factorial ratios by canceling the $(n-r)!$ tail first.
- Avoid premature pairwise division by calculating the entire numerator and dividing by the complete factorial $r!$.

### Pattern 5: Binomial Theorem and Term Coefficient Extraction (4 Marks)
Tested in 2023 Q.8(c) (coefficient of $x^{12}y^{13}$ in $(2x - 3y)^{25}$):
- State the theorem and write the general term $T_{r+1} = \binom{n}{r} x^{n-r} y^r$.
- Match the target exponents to find the index $r$.
- Verify that the exponents sum to $n$ ($12 + 13 = 25$).
- Preserve the negative sign on odd powers of negative bases and calculate the final integer.

---

## 🔗 Topic Connections

- **Prerequisites:**
  - [DM-1: Set Theory](../DM-1_Set_Theory/_Topic_Overview.md): Understanding sets, subsets, union, intersection, and set cardinality $|A|$.
  - [DM-5.4: Modular Arithmetic and Congruence](../DM-5_Number_Theory/DM-5.4_Modular_Arithmetic.md): The division algorithm $a = qd + r$ and residue classes modulo $d$ form the boxes for pigeonhole proofs.
- **Leads directly to:**
  - [DM-7.1: Algorithms and Complexity](../DM-7_Supplementary/DM-7.1_Algorithms_and_Complexity.md): Counting operations is the foundation of asymptotic complexity, loop analysis, and worst-case comparison counts in search and sort algorithms.
- **Pairs with in exams:**
  - In Section B, Question 8 regularly combines counting (sum/product rule, combination, or binomial theorem) with pigeonhole principle questions and DM-7 supplementary questions. Mastering DM-6 guarantees command over Question 8.
