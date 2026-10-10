---
title: "DM-3.11 · Logic Gates & Digital Circuits"
tags:
  - numerical-methods
  - discrete-mathematics
  - topicwise
---





[🏠 Subtopic Index](00_Index.md) | [← Prev: DM-3.10 Logic Puzzles](DM-3.10_Logic_Puzzles.md) | [Next: DM-3.13 Logic Extensions →](DM-3.13_Logic_Extensions.md)

---

# DM-3.11 · Logic Gates & Digital Circuits

Every block below is copied from `../answers_exam_style/`, which is the
only place an answer is authored. A number here is the same number, character
for character, as the one it came from.


### [2023 Q.5(a)]

**Question.** Build a digital circuit that produces the output $(p \lor \neg r) \land (\neg p \lor (q \lor \neg r))$ when given input bits $p, q$ and $r$.

**Solution.**

**Step 1. Simplify algebraically.** Factor $\neg r$ out of the two bracketed
terms, since it appears in both:

$$
F = (p \lor \neg r) \land (\neg p \lor q \lor \neg r)
$$

Use $(a \lor c) \land (b \lor c) = (a \land b) \lor c$ with $c = \neg r$,
$a = p$, $b = (\neg p \lor q)$:

$$
F = \neg r \lor \big[p \land (\neg p \lor q)\big]
$$

Distribute inside the bracket, $p \land (\neg p \lor q) = (p \land \neg p) \lor (p \land q) = 0 \lor (p \land q) = p \land q$:

$$
F = \neg r \lor (p \land q)
$$

**Step 2. Read off the circuit.**

- **Simplified form:** $F = \neg r \lor (p \land q)$
  - 1 NOT gate on $r \to \neg r$
  - 1 AND gate on $p, q \to (p \land q)$
  - 1 OR gate combining $\neg r$ and $(p \land q) \to F$
  - **Gates required:** 1 NOT, 1 AND (2-input), 1 OR (2-input) — Total: **3 gates**.

**Logic Circuit Diagram (Simplified Form):**
```text
p ----\
       )---- AND ----(p ∧ q)----\
q ----/                          \
                                  )---- OR ----> F = ¬r ∨ (p ∧ q)
r ---->|NOT|---------(¬r)--------/
```

**Alternative: Direct (Unsimplified) Circuit:**
If implemented directly as $(p \lor \neg r) \land (\neg p \lor (q \lor \neg r))$:
```text
r ---->|NOT|--------(¬r)----+-------------------+
                            |                   |
p --------------------------+----\              |
                                  )--- OR1 ---+  |
                            +----/            |  |
                            |                 |  |
p ---->|NOT|---(¬p)---------|-----------------|--+----\
                            |                 |        )--- OR3 ---+
q --------------------------|----+            |  +----/            |
                            |     )--- OR2 ---+--+                 |
                            +----+/                                |
                                                                   )--- AND ---> Output
                                                              +---/
(Output from OR1) --------------------------------------------+
```

$$
\boxed{F = \neg r \lor (p \land q)}
$$

> [!info] Check over all eight input combinations
> Comparing the simplified form against the original on every assignment of
> $(p, q, r)$:
>
> | $p$ | $q$ | $r$ | Original | $\neg r \lor (p \land q)$ |
> | :-: | :-: | :-: | :-: | :-: |
> | F | F | F | T | T |
> | F | F | T | F | F |
> | F | T | F | T | T |
> | F | T | T | F | F |
> | T | F | F | T | T |
> | T | F | T | F | F |
> | T | T | F | T | T |
> | T | T | T | T | T |
>
> All eight rows agree, so the simplification is exact.
>
> Row 8 is the one to check by eye: with $r$ true, $\neg r$ is false, and the
> alarm fires only if both $p$ and $q$ are true. The original says
> $(p \lor \neg r) \land (\neg p \lor q \lor \neg r) = (T \lor F) \land (F \lor T \lor F) = T \land T = T$.
> ✓

> [!note] An equivalent CNF form for a NAND-only implementation
> Applying the distributive law back,
> $$F = (\neg r \lor p) \land (\neg r \lor q)$$
> This is useful in hardware, where NAND is often the only gate available. It
> maps directly onto two NAND-invertor stages.

---

[🏠 Subtopic Index](00_Index.md) | [← Prev: DM-3.10 Logic Puzzles](DM-3.10_Logic_Puzzles.md) | [Next: DM-3.13 Logic Extensions →](DM-3.13_Logic_Extensions.md)
