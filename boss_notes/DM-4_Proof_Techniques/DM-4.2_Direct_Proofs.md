[← Previous: DM-4.1 Formal Proofs](DM-4.1_Formal_Proofs.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: DM-4.3 Proof by Contradiction →](DM-4.3_Proof_by_Contradiction.md)

---

# DM-4.2: Direct Proofs

> ⚫ **Never examined standalone.** Direct proofs appear embedded within Number Theory questions (DM-5.9), but RUET has never tested this method by name. Skim to understand the structure.

## What This Is

A direct proof is the most natural way to prove a conditional statement $p \to q$. You assume the hypothesis $p$ is true, expand definitions, carry out algebraic deductions, and show that the conclusion $q$ must follow.

> **Direct proof:** "A proof of a conditional statement $p \to q$ where the first step is the assumption that $p$ is true; subsequent steps are constructed using rules of inference, with the final step showing that $q$ must also be true." (Rosen, §1.7)
>
> **In simple words:** Assume the starting condition is true, follow the math step by step, and arrive directly at the target conclusion.

---

## Key Idea: The Three-Step Strategy

To prove $p \to q$ directly:

1. **Assume $p$ holds:** State the hypothesis and rewrite it with explicit algebraic definitions (for instance, an odd integer $n$ becomes $n = 2k + 1$ for some integer $k$).
2. **Perform algebraic manipulation:** Substitute, expand, and regroup terms.
3. **Conclude $q$ holds:** Match the resulting form to the definition of $q$.

### Classic Example (Rosen §1.7)

**Theorem:** If $n$ is an odd integer, then $n^2$ is odd.

1. Assume $n$ is odd. By definition, $n = 2k + 1$ for some integer $k$.
2. Square both sides:
$$
n^2 = (2k + 1)^2 = 4k^2 + 4k + 1 = 2(2k^2 + 2k) + 1
$$
3. Let $m = 2k^2 + 2k$. Because $k$ is an integer, $m$ is also an integer.
4. Therefore, $n^2 = 2m + 1$, which is odd by definition.

---

## 🔗 Move On

RUET discrete math papers do not ask standalone direct proof questions. When direct proofs appear on exams, they are embedded inside number theory questions like divisibility and parity proofs. See [DM-5: Number Theory](../DM-5_Number_Theory/_Topic_Overview.md) for actual exam problems, or move ahead to [DM-4.3: Proof by Contradiction](DM-4.3_Proof_by_Contradiction.md).

---

[← Previous: DM-4.1 Formal Proofs](DM-4.1_Formal_Proofs.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: DM-4.3 Proof by Contradiction →](DM-4.3_Proof_by_Contradiction.md)
