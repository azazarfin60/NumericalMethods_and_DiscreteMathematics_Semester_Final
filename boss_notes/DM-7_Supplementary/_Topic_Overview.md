# DM-7: Supplementary Topics

> **Section:** Section B (Discrete Mathematics)  
> **Subtopics in this folder:** 2 files (DM-7.1 and DM-7.2)  
> **Exam weight:** Appears in 2/3 Discrete Mathematics papers (2023 Q.8(d), 2024 Q.7(a)), worth 1 to 6 marks.

---

## 📖 How to Read This Topic

This folder wraps up Section B with algorithms, complexity, and the big-picture purpose of discrete mathematics.

Start with **DM-7.1**. This is the practical, high-value file. Even though the official written syllabus skips algorithms, the 2024 exam tested it with a massive 6-mark design problem (2024 Q.7(a)). You will learn how to pick the right sorting algorithm, write binary search pseudocode, design a nearest-neighbor greedy heuristic, and count operations to derive Big-O running times.

Then read **DM-7.2**. This is a short, conceptual file that answers a classic 1-mark final exam question: *"Why is discrete mathematics essential in computer science and algorithm design?"* You will learn how to answer that question in three crisp sentences hitting specification, proof certificates, and combinatorial cost analysis.

**Suggested reading time:** ~20 minutes for both files combined.

---

## 📑 Subtopic Index

| # | File | Priority | Exam Freq | Reading Time | Core Concept |
|:---:|:---|:---:|:---:|:---:|:---|
| 1 | [DM-7.1: Algorithms and Complexity](DM-7.1_Algorithms_and_Complexity.md) | 🟡 📘 | 1 appearance (2024 Q.7(a), 6 marks) | ~15 min | Sorting algorithms, binary search pseudocode, greedy routing, Big-O witnesses, and operation counts |
| 2 | [DM-7.2: Relevance of Discrete Mathematics](DM-7.2_Relevance_of_DM.md) | 🟡 | 1 appearance (2023 Q.8(d), 1 mark) | ~5 min | Exact language of computation: naming structures, counting bounds, and certifying correctness |

---

## 🎯 Exam Pattern for This Topic

The questions from DM-7 fall into two very different shapes:

1. **The Comprehensive Design Scenario (6 marks):**
   - **Seen in 2024 Q.7(a):** A delivery company needs to sort warehouse packages, search customer records, and route vans with a greedy algorithm.
   - **What examiners look for:** Naming the best algorithm with a clear reason, giving exact best/average/worst Big-O running times, writing working pseudocode with loop bounds, and pointing out the key prerequisite (such as binary search requiring sorted data on the search key).

2. **The High-Yield Theory Closer (1 mark):**
   - **Seen in 2023 Q.8(d):** The final question of the paper asking why discrete mathematics is fundamental to software and algorithms.
   - **What examiners look for:** A concise, one-paragraph answer explaining that discrete mathematics provides the exact formal language to model computer structures, count algorithmic costs, and prove program correctness.

---

## 🔗 Topic Connections

- **Prerequisite:** [DM-3: Propositional Logic](../DM-3_Propositional_Logic/_Topic_Overview.md) gives the inference rules for proving program correctness. [DM-6: Counting](../DM-6_Counting/_Topic_Overview.md) gives the combinatorics used to count loop iterations and operations.
- **Leads to:** Real-world software engineering, algorithm design, data structures, and the [Master Formula Sheet](../99_Master_Formula_Sheet.md).
- **Pairs with in exam:** Often appears as an application question alongside logic, number theory, or counting in Section B.
