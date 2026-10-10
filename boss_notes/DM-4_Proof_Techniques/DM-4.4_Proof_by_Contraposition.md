[← Previous: DM-4.3 Proof by Contradiction](DM-4.3_Proof_by_Contradiction.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: DM-4.5 Mathematical Induction →](DM-4.5_Mathematical_Induction.md)

---

# DM-4.4: Proof by Contraposition

> ⚫ **Never examined.** This note exists for reading flow and syllabus completeness. Skim it to understand the concept, but do not spend revision time memorizing it.

## What This Is

Proof by contraposition is an indirect proof method designed for conditional statements $p \to q$. When a direct algebraic path from $p$ to $q$ runs into messy algebra, you instead prove the logically equivalent contrapositive statement: $\neg q \to \neg p$.

> **Proof by contraposition:** "An indirect proof of $p \to q$ that establishes the truth of the equivalent contrapositive $\neg q \to \neg p$." (Rosen, §1.7)
>
> **In simple words:** Instead of trying to prove "if $p$, then $q$", you prove "if not $q$, then not $p$". Because both statements are logically identical, proving one proves the other.

---

## Key Idea: When and How to Use It

The method rests on the fundamental equivalence from propositional logic:
$$
(p \to q) \equiv (\neg q \to \neg p)
$$

### Execution Steps
1. **Identify components:** Distinguish hypothesis $p$ and conclusion $q$.
2. **State the contrapositive:** Form $\neg q \to \neg p$.
3. **Assume $\neg q$:** Start by assuming the conclusion is false.
4. **Directly deduce $\neg p$:** Carry out algebraic manipulation until you reach the negation of the hypothesis.

### Classic Example (Rosen §1.7)

**Theorem:** If $3n + 2$ is odd, then $n$ is odd (where $n$ is an integer).

1. A direct attempt assuming $3n + 2 = 2k + 1$ yields $3n = 2k - 1$, making it hard to isolate $n$.
2. Form the contrapositive: "If $n$ is even, then $3n + 2$ is even."
3. Assume $n$ is even, meaning $n = 2k$ for some integer $k$.
4. Substitute $n = 2k$ into the expression:
$$
3n + 2 = 3(2k) + 2 = 6k + 2 = 2(3k + 1)
$$
5. Because $3k + 1$ is an integer, $3n + 2$ is a multiple of 2 and thus even.
6. The contrapositive is established, so the original theorem is proved.

---

## 🔗 Move On

RUET semester finals (2017 to 2024) have never tested proof by contraposition as a standalone question. Move directly to the final subtopic in this folder: [DM-4.5: Mathematical Induction](DM-4.5_Mathematical_Induction.md).

---

[← Previous: DM-4.3 Proof by Contradiction](DM-4.3_Proof_by_Contradiction.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: DM-4.5 Mathematical Induction →](DM-4.5_Mathematical_Induction.md)
