[← Previous: DM-4.2 Direct Proofs](DM-4.2_Direct_Proofs.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: DM-4.4 Proof by Contraposition →](DM-4.4_Proof_by_Contraposition.md)

---

# DM-4.3: Proof by Contradiction

> ⚫ **Never examined.** This note exists for reading flow and syllabus completeness. Skim it in 2 minutes to grasp the logic, but do not spend revision time memorizing it.

## What This Is

Proof by contradiction (traditionally called *reductio ad absurdum*) is an indirect proof method. To prove that a statement $p$ is true, you assume its negation $\neg p$ is true, and show that this assumption inevitably leads to an impossible logical clash or contradiction.

> **Proof by contradiction:** "A proof that assumes the negation of the statement to be proved and derives a contradiction $r \land \neg r$, establishing that the original statement must be true." (Rosen, §1.7)
>
> **In simple words:** Assume what you want to prove is false, follow the logic until something impossible breaks, and conclude the original claim was true all along.

---

## Key Idea: The Logical Engine

The method is grounded on the propositional equivalence:
$$
(\neg p \to \mathbf{F}) \equiv p
$$

To carry out a proof by contradiction:
1. **Assume the opposite:** Start by assuming $\neg p$ is true. If proving a conditional statement $p \to q$, assume $p \land \neg q$.
2. **Deduce consequences:** Apply valid logic and algebraic rules.
3. **Expose the contradiction:** Arrive at a statement that clashes with an axiom, a premise, or basic mathematics (such as an integer being both even and odd).
4. **Conclude:** Because truth never implies a falsehood, the assumption $\neg p$ must be false, meaning $p$ is true.

### Classic Example (Rosen §1.7)

**Theorem:** $\sqrt{2}$ is irrational.

1. Assume the opposite: $\sqrt{2}$ is rational. Then $\sqrt{2} = \frac{a}{b}$ for non-zero integers $a, b$ in lowest terms ($\gcd(a, b) = 1$).
2. Square both sides:
$$
2 = \frac{a^2}{b^2} \implies a^2 = 2b^2
$$
3. Because $a^2$ is even, $a$ must be even. Let $a = 2c$.
4. Substitute $a = 2c$ back into the equation:
$$
(2c)^2 = 2b^2 \implies 4c^2 = 2b^2 \implies b^2 = 2c^2
$$
5. Because $b^2$ is even, $b$ must be even.
6. If both $a$ and $b$ are even, they share a common divisor 2. This contradicts the premise that $a/b$ was written in lowest terms.
7. So the assumption is false; $\sqrt{2}$ is irrational.

---

## 🔗 Move On

This subtopic has never appeared in any RUET exam paper from 2017 to 2024. If you are preparing for your semester final, move right ahead to [DM-4.4: Proof by Contraposition](DM-4.4_Proof_by_Contraposition.md).

---

[← Previous: DM-4.2 Direct Proofs](DM-4.2_Direct_Proofs.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: DM-4.4 Proof by Contraposition →](DM-4.4_Proof_by_Contraposition.md)
