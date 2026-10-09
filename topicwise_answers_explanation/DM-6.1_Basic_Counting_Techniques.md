---
title: "DM-6.1 · Basic Counting Techniques"
tags:
  - numerical-methods
  - discrete-mathematics
  - topicwise
---

# DM-6.1 · Basic Counting Techniques

Every block below is copied from `../answers_explanation/`. The reasoning
is written once, in the year-wise file, and is not restated here.


### [2022 Q.8(b)]

**Question.** There are four major auto routes from Boston to Detroit and six from Detroit to Los Angeles. How many major auto routes are there from Boston to Los Angeles via Detroit?

*[Marks: 02, CO: 3]*

**Solution.**

**Setting up.** A route via Detroit is fully described by **one** choice from
Boston to Detroit **and one** choice from Detroit to Los Angeles. There is no
other freedom, and the order is fixed by the geography: Boston first, Detroit
second, Los Angeles third.

This is the **product rule**, also called the multiplication principle:

$$
\text{number of routes} = 4 \times 6
$$

$$\boxed{24 \text{ routes}}$$

> [!info] Check
> The four Boston choices against the six Detroit choices form a $4 \times 6$ grid
> of $24$ cells, one route each. The direct product confirms $4 \times 6 = 24$.

> [!warning] The sum rule does not apply here
> The **sum rule** applies to mutually exclusive alternatives: either go through
> Detroit or through Chicago, never both. Here every route *must* go through
> Detroit, so the choices are sequential rather than alternative, and the product
> rule is the one that fits.
>
> The quickest way to tell the two apart: ask whether the choices happen one after
> another (product) or instead of one another (sum). "Via Detroit" is the clearest
> possible example of the first kind.

> [!note] Why permutations do not apply either
> A route is fixed by its two legs, so choosing leg 1 then leg 2 already fixes the
> whole route. No reordering is possible or meaningful, so this is a
> combination-like count of $24$ distinct paths, not $24$ orderings of something.
>
> If the question had asked about the round trip, the count would change shape
> entirely, because a return leg is not independent of the outward one.

---
