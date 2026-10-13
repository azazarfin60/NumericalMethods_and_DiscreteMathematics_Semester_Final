---
title: "DM-6.1 · Basic Counting Techniques"
tags:
  - numerical-methods
  - discrete-mathematics
  - topicwise
---



[🏠 Subtopic Index](00_Index.md) | [← Prev: DM-5.9 Number-Theoretic Proofs](DM-5.9_Number_Theoretic_Proofs.md) | [Next: DM-6.3 Pigeonhole Principle →](DM-6.3_Pigeonhole_Principle.md)

---

# DM-6.1 · Basic Counting Techniques

Every block below is copied from `../answers_exam_style/`, which is the
only place an answer is authored. A number here is the same number, character
for character, as the one it came from.


### [2022 Q.8(b)]

**Question.** There are four major auto routes from Boston to Detroit and six from Detroit to Los Angeles. How many major auto routes are there from Boston to Los Angeles via Detroit?

**Solution.**

**Setting up.** A route via Detroit is fully described by **one** choice from
Boston to Detroit **and one** choice from Detroit to Los Angeles. There is no
other freedom, and the order is fixed by the geography: Boston first, Detroit
second, Los Angeles third.

This is the **product rule** (multiplication principle):

$$
\text{number of routes} = 4 \times 6
$$

$$
\boxed{24 \text{ routes}}
$$

> [!info] Check
> Listing the four Boston choices against the six Detroit choices gives a
> $4 \times 6$ grid of 24 cells, one route each. A direct product confirms
> $4 \times 6 = 24$.

> [!note] Why not the sum, and why not permutations
> The **sum rule** applies to alternatives that are mutually exclusive: either go
> through Detroit or through Chicago, never both. Here every route *must* go
> through Detroit, so the choices are sequential, not alternative, and the
> product rule is the one that applies.
>
> **Permutations do not apply** either. A route is fixed by its two legs, so
> choosing leg 1 then leg 2 already fixes the whole route and no reordering is
> possible or meaningful. This is a combination-like count of $24$ distinct
> paths, not $24$ orderings of something.

---

[🏠 Subtopic Index](00_Index.md) | [← Prev: DM-5.9 Number-Theoretic Proofs](DM-5.9_Number_Theoretic_Proofs.md) | [Next: DM-6.3 Pigeonhole Principle →](DM-6.3_Pigeonhole_Principle.md)
