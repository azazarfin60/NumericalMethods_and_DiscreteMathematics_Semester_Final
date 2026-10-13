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

Every block below is copied from `../answers_explanation/`. The reasoning
is written once, in the year-wise file, and is not restated here.


### [2022 Q.5(d)]

**Question.** Consider these statements, of which the first three are premises and the fourth is a valid conclusion. "All humming are richly colored." "No large birds live on honey." "Birds that do not live on honey are dull in order." Conclusion: "Humming birds are small."

*[Marks: 02, CO: 3]*

**Solution.**

> [!note] Origin & Textual Corrections
> This question is taken verbatim from Kenneth H. Rosen, *Discrete Mathematics and Its Applications* (§1.6, Example 26: "Rules of Inference"), which adapts a classic sorites puzzle by Lewis Carroll (from *Symbolic Logic*, 1896).
> - *"All humming"* has the noun "birds" omitted in the printed question.
> - *"dull in order"* is a transcription error for *"dull in colour"*.

**Step 1. Formalise using Predicate Logic.**
In Lewis Carroll's logic puzzles and Rosen's formulation, natural-language antonyms are treated as logical complements:
- "dull in colour" is the exact complement of "richly coloured" ($\neg S(x)$).
- "small" is the exact complement of "large" ($\neg Q(x)$).

Let the universe of discourse $U$ be the set of all birds:
- $P(x)$: $x$ is a hummingbird
- $Q(x)$: $x$ is large $\implies \neg Q(x)$: $x$ is small
- $R(x)$: $x$ lives on honey $\implies \neg R(x)$: $x$ does not live on honey
- $S(x)$: $x$ is richly coloured $\implies \neg S(x)$: $x$ is dull in colour

**Step 2. Express premises and the conclusion.**
1. Premise 1 ($P_1$): "All hummingbirds are richly colored"
   $$\forall x\, (P(x) \to S(x))$$
2. Premise 2 ($P_2$): "No large birds live on honey" (if large, then does not live on honey)
   $$\forall x\, (Q(x) \to \neg R(x))$$
3. Premise 3 ($P_3$): "Birds that do not live on honey are dull in colour"
   $$\forall x\, (\neg R(x) \to \neg S(x))$$
4. Conclusion ($C$): "Hummingbirds are small"
   $$\forall x\, (P(x) \to \neg Q(x))$$

**Step 3. Rigorous proof using Rules of Inference.**
Let $c$ be an arbitrary bird in $U$:

| Step | Proposition | Justification |
| :--: | :-- | :-- |
| 1 | $P(c) \to S(c)$ | Premise 1 by Universal Instantiation |
| 2 | $\neg R(c) \to \neg S(c)$ | Premise 3 by Universal Instantiation |
| 3 | $S(c) \to R(c)$ | Contrapositive of Step 2 ($\neg B \to \neg A \equiv A \to B$) |
| 4 | $P(c) \to R(c)$ | Hypothetical Syllogism from Steps 1 and 3 |
| 5 | $Q(c) \to \neg R(c)$ | Premise 2 by Universal Instantiation |
| 6 | $R(c) \to \neg Q(c)$ | Contrapositive of Step 5 |
| 7 | $P(c) \to \neg Q(c)$ | Hypothetical Syllogism from Steps 4 and 6 |
| 8 | $\forall x\, (P(x) \to \neg Q(x))$ | Universal Generalization from Step 7 |

Since $\neg Q(x)$ means "$x$ is small", the deduction is complete and valid.

$$
\boxed{\text{The argument is VALID via Universal Instantiation, Contraposition, and Hypothetical Syllogism}}
$$

> [!tip] Why propositional translation fails
> If modeled naively with 6 independent propositional variables:
> $$P_1: H \to R, \quad P_2: L \to \neg N, \quad P_3: \neg N \to D, \quad \text{Claim: } H \to S$$
> there is no syntactic link connecting $D$ to $\neg R$ or $S$ to $\neg L$. A countermodel emerges where a bird is simultaneously richly coloured and dull ($R=T, D=T$). In natural language, however, "dull" and "richly coloured" are mutually exclusive antonyms. Lewis Carroll's Sorites relies on these semantic complements, which predicate logic formalizes directly as $S(x)$ and $\neg S(x)$.

---

### [2022 Q.6(a)]

**Question.** Knights always tell the truth, Knaves always lie, Spies can either. Three people A, B and C, one of each type, each knows the types of the other two. (i) A says "C is the Knave", B says "A is the Knight", C says "I am the spy". (ii) A says "I am the Knave", B says "I am the Knave", C says "I am the Knave". Determine whether there is a unique solution.

*[Marks: 06, CO: 3]*

**Solution.**

**Method.** A knight's every statement is true. A knave's every statement is
false. A spy is unconstrained. Each of A, B and C may be any of the three types
and the three types are all different, so there are only $3! = 6$ assignments to
test. Testing all six is exhaustive and cheap.

**Rule stated first, because it settles part (ii) outright.** Nobody can
truthfully say "I am the knave", because a knave is by definition not a knave.
Nobody can falsely say it either, because the statement would be true for a knave.
Therefore **only a spy can say "I am the knave"**, and a knight or knave saying
it is an immediate contradiction.

---

**(i) A says "C is the Knave." B says "A is the Knight." C says "I am the spy."**

The three statements are true when, respectively, $C$ is the knave, $A$ is the
knight, and $C$ is the spy.

| Assignment | A's statement | B's statement | C's statement | Verdict |
| :-- | :-- | :-- | :-- | :-- |
| A=K, B=N, C=S | false (C is a spy, not a knave) | true | true | **A is a knight but lies. Out.** |
| A=K, B=S, C=N | true | true | false | **Consistent.** |
| A=N, B=K, C=S | false | false | true | **B is a knight but lies. Out.** |
| A=N, B=S, C=K | false | false | false | **C is a knight but lies. Out.** |
| A=S, B=K, C=N | true | false | false | **B is a knight but lies. Out.** |
| A=S, B=N, C=K | false | true | false | **C is a knight but lies. Out.** |

Exactly one row survives, so **the solution is unique**:

$$\boxed{\text{(i) A = Knight, B = Spy, C = Knave}}$$

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

$$\boxed{\text{(ii) There is NO solution}}$$

**Reason, without the table.** From the rule above, "I am the knave" can only be
said by a spy. All three of A, B and C say it. Since exactly one of the three is
a spy, at least two are knights or knaves, and each of those contradicts what
they said.

> [!info] Exhaustive check
> All six permutations were tested against the knight and knave rules in both
> parts. Part (i) returned exactly one consistent assignment; part (ii) returned
> none. Both results are therefore unique, and no assignment was missed.

> [!note] What separates the two parts
> In **(i)** the three statements refer to **different** people, so one true
> statement can be pinned on the spy and the remaining two can be assigned to a
> knight and a knave consistently.
>
> In **(ii)** all three statements are the same self-referential claim. Only one
> spy exists, so two of the three speakers are making a sentence they cannot make.
> That is the standard way to show a knights-and-knaves puzzle has no solution: put
> everyone in the same corner and no consistent assignment remains.
>
> The rule stated before the tables is worth internalising, because it turns part
> (ii) from six rows of bookkeeping into one sentence.

---

### [2023 Q.5(b)]

**Question.** Four friends have been identified as suspects for an unauthorized access into a computer system. Alice said "Carlos did it." John said "I did not do it." Carlos said "Diana did it." Diana said "Carlos lied when he said that I did it." (i) If exactly one of the four suspects is telling the truth, who did it? (ii) If exactly one is lying, who did it?

*[Marks: 04, CO: 3]*

**Solution.**

**Translate the statements.** The four suspects are mutually exclusive, so exactly
one of them did it. Let the culprit be one of $A, J, C, D$.

| Statement | True when |
| :-- | :-- |
| $S_A$: "Carlos did it" | culprit $= C$ |
| $S_J$: "I did not do it" | culprit $\ne J$ |
| $S_C$: "Diana did it" | culprit $= D$ |
| $S_D$: "Carlos lied when he said I did it" | Carlos's claim was false, that is culprit $\ne D$ |

The structural observation that makes this easy: **$S_C$ and $S_D$ are exact
negations of each other.** Carlos says Diana did it; Diana says Carlos's claim
was false. Either Diana did it and Carlos is truthful, or she did not and Carlos
is lying. Exactly one of those two is therefore **always** true, whatever the
culprit. This drives both parts.

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
must be true, so the single truth must be one of those two, which means Alice and
John are both lying. John lying means his statement "I did not do it" is false,
so John did it.

Verify: John lying, Carlos lying (Diana did not do it), Alice lying (Carlos did
not do it), Diana telling the truth (Carlos's claim was false). Exactly one truth.
Agrees.

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
says "Diana did it", which is false. Exactly one lie, Carlos's. Agrees.

> [!info] Why the enumeration is complete
> Four candidates for the culprit against four statements is 16 combinations, and
> the mutual-exclusion constraint that exactly one person did it removes none of
> them, since every candidate satisfies it. So testing four culprits against four
> statements **is** the full enumeration. Both answers are unique, so each part
> has a single solution, which is what the question asks you to establish rather
> than assume.

> [!warning] The two parts have different answers, and that is intended
> Part (i) says exactly one is true. Part (ii) says exactly one is lying, which
> means exactly three are true. These are very different conditions and they
> cannot both hold at once.
>
> Expecting the same culprit in both parts is the standard error here, and it is
> worth noticing *why* the intuition misfires. Both answers involve the phrase
> "exactly one", and it is natural to read the two parts as restatements of the
> same constraint. They are not. If you find yourself trying to make one culprit
> satisfy both, you have collapsed "one truth-teller" into "one liar", which is
> the same mistake as writing modus tollens and then applying it forwards.

---

[🏠 Subtopic Index](00_Index.md) | [← Prev: DM-3.9 Rules of Inference & Valid Arguments](DM-3.9_Rules_of_Inference_and_Valid_Arguments.md) | [Next: DM-3.11 Logic Gates & Digital Circuits →](DM-3.11_Logic_Gates_and_Digital_Circuits.md)
