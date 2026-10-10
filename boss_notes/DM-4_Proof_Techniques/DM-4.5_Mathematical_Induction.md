[← Previous: DM-4.4 Proof by Contraposition](DM-4.4_Proof_by_Contraposition.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: DM-5 Number Theory Overview →](../DM-5_Number_Theory/_Topic_Overview.md)

---

# DM-4.5: Mathematical Induction

> ⚫ **Never examined.** This note exists for reading flow and syllabus completeness. Skim it in 2 minutes to grasp the two-step structure, but do not spend revision time memorizing it.

## What This Is

Mathematical induction is a proof technique used to prove that a predicate $P(n)$ is true for all positive integers $n = 1, 2, 3, \dots$. It operates like an infinite line of standing dominoes: knock down the first domino ($P(1)$ is true), and make sure every falling domino knocks down the next one ($P(k) \to P(k+1)$).

> **Principle of Mathematical Induction:** "To prove that $P(n)$ is true for all positive integers $n$, verify that $P(1)$ is true (basis step), and show that the conditional statement $P(k) \to P(k + 1)$ is true for all positive integers $k$ (inductive step)." (Rosen, §5.1)
>
> **In simple words:** Verify that the formula holds for $n = 1$, then prove that if it works for step $k$, it must automatically work for step $k + 1$. Once both pieces click, the statement holds for every positive integer.

---

## Key Idea: The Two Essential Steps

Expressed as a rule of inference:
$$
[P(1) \land \forall k (P(k) \to P(k + 1))] \to \forall n P(n)
$$

Every proof by mathematical induction consists of two distinct steps:
1. **Basis Step:** Verify that $P(1)$ is true by direct calculation.
2. **Inductive Step:**
   - State the **Inductive Hypothesis**: Assume $P(k)$ is true for an arbitrary positive integer $k$.
   - Prove $P(k + 1)$ holds: Add the $(k + 1)$-th term, substitute the hypothesis, and simplify until the expression matches the formula evaluated at $k + 1$.

### Classic Example (Rosen §5.1)

**Theorem:** For every positive integer $n$, $\sum_{i=1}^n i = \frac{n(n + 1)}{2}$.

1. **Basis Step ($n = 1$):**
   Left side is $1$. Right side is $\frac{1(1 + 1)}{2} = 1$. The basis step holds.
2. **Inductive Step:**
   Assume the identity holds for $k$:
$$
\sum_{i=1}^k i = \frac{k(k + 1)}{2}
$$
   Now evaluate the sum for $k + 1$:
$$
\sum_{i=1}^{k+1} i = \left(\sum_{i=1}^k i\right) + (k + 1) = \frac{k(k + 1)}{2} + (k + 1) = \frac{k(k + 1) + 2(k + 1)}{2} = \frac{(k + 1)(k + 2)}{2}
$$
   This is exactly the formula for $n = k + 1$.
3. By the principle of mathematical induction, the identity holds for all positive integers $n$.

---

## 🔗 Move On

RUET discrete math papers (2022 to 2024) have never tested mathematical induction proofs. Move directly ahead to the next topic in Section B: [DM-5: Number Theory](../DM-5_Number_Theory/_Topic_Overview.md).

---

[← Previous: DM-4.4 Proof by Contraposition](DM-4.4_Proof_by_Contraposition.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: DM-5 Number Theory Overview →](../DM-5_Number_Theory/_Topic_Overview.md)
