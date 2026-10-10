---
title: "DM-3.10 · Logic Puzzles"
tags:
  - numerical-methods
  - discrete-mathematics
  - topicwise
---





[🏠 Subtopic Index](00_Index.md) | [← Prev: DM-3.9 Rules of Inference & Valid Arguments](DM-3.9_Rules_of_Inference_and_Valid_Arguments.md) | [Next: DM-3.11 Logic Gates & Digital Circuits →](DM-3.11_Logic_Gates_and_Digital_Circuits.md)

---

# DM-3.10 · Logic Puzzles

Every block below is copied from `../answers_exam_style/`, which is the
only place an answer is authored. A number here is the same number, character
for character, as the one it came from.


### [2022 Q.5(d)]

**Question.** Consider these statements, of which the first three are premises and the fourth is a valid conclusion. "All humming are richly colored." "No large birds live on honey." "Birds that do not live on honey are dull in order." Conclusion: "Humming birds are small."

**Solution.**

> [!note] Origin & Text Correction
> This is the classic Lewis Carroll sorites puzzle printed in Kenneth Rosen (*Discrete Mathematics and Its Applications*, §1.6, Example 26).
> - "All humming [birds]" has the noun omitted in the paper.
> - "dull in order" is a typographical error for "dull in colour".

**Step 1. Define predicates.**
Let the universe of discourse be the set of all birds. Natural language opposites in Lewis Carroll's logic puzzles represent complementary predicates:
- $P(x)$: $x$ is a hummingbird
- $Q(x)$: $x$ is large $\implies \neg Q(x)$: $x$ is small ("not large")
- $R(x)$: $x$ lives on honey $\implies \neg R(x)$: $x$ does not live on honey
- $S(x)$: $x$ is richly coloured $\implies \neg S(x)$: $x$ is dull in colour ("not richly coloured")

**Step 2. Formalise premises and conclusion.**
- Premise 1 ($P_1$): $\forall x\, (P(x) \to S(x))$
- Premise 2 ($P_2$): $\forall x\, (Q(x) \to \neg R(x))$
- Premise 3 ($P_3$): $\forall x\, (\neg R(x) \to \neg S(x))$
- Conclusion ($C$): $\forall x\, (P(x) \to \neg Q(x))$

**Step 3. Formal deduction via rules of inference.**
Let $c$ be an arbitrary bird in the domain:

1. $P(c) \to S(c)$ — Premise 1, Universal Instantiation
2. $\neg R(c) \to \neg S(c)$ — Premise 3, Universal Instantiation
3. $S(c) \to R(c)$ — Contrapositive of (2)
4. $P(c) \to R(c)$ — Hypothetical Syllogism from (1) and (3)
5. $Q(c) \to \neg R(c)$ — Premise 2, Universal Instantiation
6. $R(c) \to \neg Q(c)$ — Contrapositive of (5)
7. $P(c) \to \neg Q(c)$ — Hypothetical Syllogism from (4) and (6)
8. $\forall x\, (P(x) \to \neg Q(x))$ — Universal Generalization from (7)

Since $\neg Q(x)$ represents "small", the conclusion "Hummingbirds are small" follows logically.

$$
\boxed{\text{The argument is VALID via Universal Instantiation, Contraposition, and Hypothetical Syllogism}}
$$

> [!info] Semantic formalization note
> If one naively assigns 6 unrelated propositional variables $(H, R, L, N, D, S)$ without encoding the antonymic relationships $\text{Dull} \equiv \neg\text{RichlyColoured}$ and $\text{Small} \equiv \neg\text{Large}$, the connection between colour and size is severed. Under Rosen and Carroll's intended predicate formalization, recognizing these complements makes the syllogism valid.

---

### [2022 Q.6(a)]

**Question.** Knights always tell the truth, Knaves always lie, Spies can either. Three people A, B and C, one of each type, each knows the types of the other two. (i) A says "C is the Knave", B says "A is the Knight", C says "I am the spy". (ii) A says "I am the Knave", B says "I am the Knave", C says "I am the Knave". Determine whether there is a unique solution.

**Solution.**

**Method.** A knight's every statement is true. A knave's every statement is false.
A spy is unconstrained. Each of A, B and C may be any of the three types, and the
three types are all different, so there are only $3! = 6$ assignments to test.

**Rule stated first.** Nobody can truthfully say "I am the knave",
because a knave is by definition not a knave. Nobody can falsely say "I am the
knave" either, because that statement would be true for a knave. Therefore **only
a spy can say "I am the knave"**, and a knight or knave saying it is an immediate
contradiction.

---

**(i) A says "C is the Knave." B says "A is the Knight." C says "I am the spy."**

Test all six assignments. The three statements are true when, respectively,
$C$ is the knave, $A$ is the knight, and $C$ is the spy.

| Assignment | A's statement | B's statement | C's statement | Verdict |
| :-- | :-- | :-- | :-- | :-- |
| A=K, B=N, C=S | false (C is a spy, not a knave) | true | true | **A is a knight but lies. Out.** |
| A=K, B=S, C=N | true | true | false | **Consistent.** |
| A=N, B=K, C=S | false | false | true | **B is a knight but lies. Out.** |
| A=N, B=S, C=K | false | false | false | **C is a knight but lies. Out.** |
| A=S, B=K, C=N | true | false | false | **B is a knight but lies. Out.** |
| A=S, B=N, C=K | false | true | false | **C is a knight but lies. Out.** |

Exactly one row survives, so **the solution is unique**:

$$
\boxed{\text{(i) A = Knight, B = Spy, C = Knave}}
$$

**Verification.** A, a knight, says C is the knave: true, since $C$ is the
knave. B, a spy, says A is the knight: true, and a spy may tell the truth. C, a
knave, says "I am the spy": false, since $C$ is the knave. All consistent.

---

**(ii) A says "I am the Knave." B says "I am the Knave." C says "I am the Knave."**

| Assignment | A's statement | B's statement | C's statement | Verdict |
| :-- | :-- | :-- | :-- | :-- |
| A=K, B=N, C=S | false | true | false | A is a knight but lies. Out. |
| A=K, B=S, C=N | false | false | true | A is a knight but lies. Out. |
| A=N, B=K, C=S | true | false | false | A is a knave but tells the truth. Out. |
| A=N, B=S, C=K | true | false | false | A is a knave but tells the truth. Out. |
| A=S, B=K, C=N | false | false | true | B is a knight but lies. Out. |
| A=S, B=N, C=K | false | true | true | B is a knave but tells the truth. Out. |

**Every row is eliminated.**

$$
\boxed{\text{(ii) There is NO solution}}
$$

**Reason, without the table.** From the rule above, "I am the knave" can only be
said by a spy. All three of A, B and C say it. Since exactly one of the three is
a spy, at least two are knights or knaves, and each of those contradicts what
they said. A puzzle in which every person utters a sentence only one of them may
utter is a contradiction in three.

> [!info] Check
> All six permutations were tested against the knight and knave rules
> exhaustively, in both parts. Part (i) returned exactly one consistent
> assignment; part (ii) returned none. Both results are unique, so no assignment
> was missed.

> [!note] The difference between the two parts
> In (i) the three statements refer to **different** people, so one true
> statement can be pinned on the spy and the remaining two can be assigned to a
> knight and a knave consistently. In (ii) all three statements are the same
> self-referential claim, and no assignment survives. This is the standard way to
> show a knights-and-knaves puzzle has no solution: put everyone in the same
> corner and no consistent assignment remains.

---

### [2023 Q.5(b)]

**Question.** Four friends have been identified as suspects for an unauthorized access into a computer system. Alice said "Carlos did it." John said "I did not do it." Carlos said "Diana did it." Diana said "Carlos lied when he said that I did it." (i) If exactly one of the four suspects is telling the truth, who did it? (ii) If exactly one is lying, who did it?

**Solution.**

**Translate the statements.** The four suspects are mutually exclusive, so
exactly one of them did it. Let the culprit be one of $A, J, C, D$.

| Statement | True when |
| :-- | :-- |
| $S_A$: "Carlos did it" | culprit $= C$ |
| $S_J$: "I did not do it" | culprit $\ne J$ |
| $S_C$: "Diana did it" | culprit $= D$ |
| $S_D$: "Carlos lied when he said I did it" | Carlos's claim was false, that is culprit $\ne D$ |

Note that $S_C$ and $S_D$ are exact negations of each other, so **exactly one of
them is always true**. This observation drives both parts.

**(i) Exactly one telling the truth**

Test each culprit:

| Culprit | $S_A$ | $S_J$ | $S_C$ | $S_D$ | True count |
| :-- | :-: | :-: | :-: | :-: | --: |
| A | F | T | F | T | 2 |
| J | F | F | F | T | **1** |
| C | T | T | F | T | 3 |
| D | F | T | T | F | 2 |

Only one row gives a count of 1.

$$\boxed{\text{(i) John did it}}$$

**Reasoning without a table.** Since $S_C$ and $S_D$ are negations, one of them
must be true, so the single truth must be one of those two, and both Alice and
John must be lying. John lying means "I did not do it" is false, so John did it.
Check: John lying, Carlos lying (Diana did not do it), Alice lying (Carlos did
not do it), Diana telling the truth (Carlos's claim was false). Exactly one
truth. ✓

**(ii) Exactly one lying**

Equivalently, exactly three telling the truth. The same table, reading the false
count:

| Culprit | $S_A$ | $S_J$ | $S_C$ | $S_D$ | Lying count |
| :-- | :-: | :-: | :-: | :-: | --: |
| A | F | T | F | T | 2 |
| J | F | F | F | T | 3 |
| C | T | T | F | T | **1** |
| D | F | T | T | F | 2 |

Only one row gives a lying count of 1.

$$\boxed{\text{(ii) Carlos did it}}$$

**Reasoning without a table.** Exactly one lying means Alice and Diana are both
telling the truth, since they cannot both lie. Alice true gives culprit $= C$.
Then John says "I did not do it", which is true since Carlos did it, and Carlos
says "Diana did it", which is false. Exactly one lie, Carlos's. ✓

> [!info] Check by exhaustive enumeration
> All four culprits were tested against all four statements, which is the 16
> cases of the enumeration above reduced by the mutual-exclusion constraint. The
> two answers $J$ and $C$ are each unique, so each part has a single solution.

> [!warning] The two parts give different answers, and that is intended
> Part (i) says one true, part (ii) says one false, which means three true. These
> are very different conditions and they cannot both hold at once. Students who
> expect the same culprit in both parts have misread one of them.

---

[🏠 Subtopic Index](00_Index.md) | [← Prev: DM-3.9 Rules of Inference & Valid Arguments](DM-3.9_Rules_of_Inference_and_Valid_Arguments.md) | [Next: DM-3.11 Logic Gates & Digital Circuits →](DM-3.11_Logic_Gates_and_Digital_Circuits.md)
