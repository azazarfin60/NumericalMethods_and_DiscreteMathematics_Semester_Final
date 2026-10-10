---
title: "DM-3.2 · Logical Connectives & Truth Tables"
tags:
  - numerical-methods
  - discrete-mathematics
  - topicwise
---





[🏠 Subtopic Index](00_Index.md) | [← Prev: DM-3.1 Propositions & Syntax](DM-3.1_Propositions_and_Syntax.md) | [Next: DM-3.3 Tautology, Contradiction & Contingency →](DM-3.3_Tautology_Contradiction_and_Contingency.md)

---

# DM-3.2 · Logical Connectives & Truth Tables

Every block below is copied from `../answers_explanation/`. The reasoning
is written once, in the year-wise file, and is not restated here.


### [2022 Q.6(b), 2024 Q.7(b)]

**Appeared in:** 2022 Q.6(b), 2024 Q.7(b)

**Question.** Determine whether the biconditionals are true or false: (i) $2 + 2 = 4$ if and only if $1 + 1 = 2$, (ii) $1 + 1 = 2$ if and only if $2 + 3 = 4$, (iii) $1 + 1 = 3$ if and only if monkeys can fly, (iv) $0 > 1$ if and only if $2 > 1$.

*[Marks: 04, CO: 1]*

**Solution.**

The biconditional $P \leftrightarrow Q$ is true when $P$ and $Q$ have the
**same** truth value, that is when both are true or both are false.

$$
P \leftrightarrow Q \equiv (P \to Q) \land (Q \to P)
$$

**(i) $2 + 2 = 4$ if and only if $1 + 1 = 2$**

$2+2=4$ is true. $1+1=2$ is true. Same value, so the biconditional holds.

$$\boxed{\text{(i) TRUE}}$$

**(ii) $1 + 1 = 2$ if and only if $2 + 3 = 4$**

$1+1=2$ is true. $2+3=5$, not $4$, so $2+3=4$ is false. The values disagree.

$$\boxed{\text{(ii) FALSE}}$$

**(iii) $1 + 1 = 3$ if and only if monkeys can fly**

$1+1=3$ is false. Monkeys cannot fly, so that is false as well. Both false, so
they match.

$$\boxed{\text{(iii) TRUE}}$$

**(iv) $0 > 1$ if and only if $2 > 1$**

$0 > 1$ is false. $2 > 1$ is true. The values disagree.

$$\boxed{\text{(iv) FALSE}}$$

> [!warning] Part (iii) is the whole question: two false statements give a TRUE biconditional
> A biconditional asserts that the two sides have the **same** truth value, not
> that either of them is true. Answering "false, because $1+1 \ne 3$" misreads
> the claim entirely.
>
> A quick way to see it: $P \leftrightarrow Q$ is the negation of
> $P \oplus Q$, the exclusive or. So "false if and only if false" is true, and
> "true if and only if false" is false. Parts (i) and (iii) are both
> true-and-true or false-and-false; parts (ii) and (iv) are both mixed.

> [!note] Why this distinction shows up in engineering
> Two sensors that both report "not faulty" do not by themselves certify that the
> system is healthy: they may share a common cause. Logic built on
> $\leftrightarrow$ assumes the two statements are independent, and safety
> arguments that conflate "same truth value" with "both true" fail in exactly the
> way part (iii) demonstrates.

---

**Answered in phase P6, in `../CT_Questions/`.**

- *CT-04 Q.2(c)* is a class-test question. Its answer is in `../CT_Questions/CT_answers_exam_style.md`, with the reasoning in `../CT_Questions/CT_answers_explanation.md`.
- *CT-04 Q.3(c)* is a class-test question. Its answer is in `../CT_Questions/CT_answers_exam_style.md`, with the reasoning in `../CT_Questions/CT_answers_explanation.md`.

---

[🏠 Subtopic Index](00_Index.md) | [← Prev: DM-3.1 Propositions & Syntax](DM-3.1_Propositions_and_Syntax.md) | [Next: DM-3.3 Tautology, Contradiction & Contingency →](DM-3.3_Tautology_Contradiction_and_Contingency.md)
