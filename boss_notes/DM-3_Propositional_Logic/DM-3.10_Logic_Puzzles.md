[← Previous: DM-3.9 Rules of Inference](DM-3.9_Rules_of_Inference.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: DM-3.11 Logic Gates →](DM-3.11_Logic_Gates.md)

---

# DM-3.10: Logic Puzzles

> 🟠 **Priority:** Secondary | **Tested:** 2/3 DM papers (2022, 2023) | **Typical marks:** 4 to 9

## What This Is (and Why It Matters)

A logic puzzle is not just a brainteaser; it is a real-world Boolean satisfiability problem dressed up in a story. In these problems, you are given a set of people making statements about themselves and each other, along with rules about who tells the truth and who lies.

Although class notes sometimes label puzzles as informal recreational math, the RUET semester final heavily rewards them. In 2022 Q.6(a), students had to solve a 5-mark Knights, Knaves, and Spies puzzle. In 2023 Q.5(b), a 4-mark unauthorized computer access puzzle required finding the culprit under two different truth scenarios. In 2022 Q.5(d), a classic Lewis Carroll sorites syllogism was set. If you master the systematic case-elimination tables below, these problems become guaranteed full-mark questions.

---

## 📝 Key Definitions

> **Logic Puzzle:** "Puzzles that can be solved using logical reasoning are known as logic puzzles. Solving logic puzzles is an excellent way to practice working with the rules of logic." -- Rosen, §1.2, Logic Puzzles (p. 19)
>
> **In simple words:** A word problem where you deduce the exact truth state or identify culprits by systematically checking which scenarios obey all logical rules without contradiction.

> **Knights and Knaves:** "In Smullyan posed many puzzles about an island that has two kinds of inhabitants, knights, who always tell the truth, and their opposites, knaves, who always lie." -- Rosen, §1.2, Example 7 (p. 19)
>
> **In simple words:** An island where every person is strictly binary: a Knight speaks only true statements ($\text{T}$), and a Knave speaks only false statements ($\text{F}$).

> **The Spy Variant:** "In Exercises 24-31 we introduce related puzzles where we have three types of people, knights and knaves as in this puzzle together with spies who can lie [or tell the truth]." -- Rosen, §1.2 (p. 19)
>
> **In simple words:** A three-character puzzle where Knights always tell the truth, Knaves always lie, and Spies can do either.

---

## The Three Puzzle Families

| Puzzle Family | Core Rules | Systematic Solution Method |
|:---|:---|:---|
| **Knights, Knaves, Spies** | Knight = always $\text{T}$, Knave = always $\text{F}$, Spy = unconstrained ($\text{T}$ or $\text{F}$). Three distinct roles. | Enumerate all $3! = 6$ possible role assignments in a verification table. |
| **Suspect / Culprit Puzzles** | Exactly one culprit did the crime. Candidates make statements. Conditions specify "exactly one truth" or "exactly one lie". | Build a table testing each suspect as culprit. Use contradictory pairs to speed up the deduction. |
| **Lewis Carroll Sorites** | A multi-premise syllogism where natural language opposites represent complementary predicates. | Instantiate universal quantifiers, apply contraposition, and chain implications using Hypothetical Syllogism. |

---

## The Golden Secret of Knights, Knaves, and Spies

Here is the single rule that instantly solves half of all island puzzles:

> **Nobody except a Spy can ever say: "I am a Knave."**

Why?
1. Could a **Knight** say "I am a Knave"? No, because that would be a lie, and Knights never lie.
2. Could a **Knave** say "I am a Knave"? No, because if a Knave said it, the statement would be true, but Knaves never tell the truth.
3. Therefore, the statement "I am a Knave" is impossible for both Knights and Knaves. **Only a Spy can utter it.**

Whenever multiple people in a puzzle say "I am a Knave", you can immediately tell there is a contradiction if only one spy is available.

---

## 🔧 Worked Example 1: Knights, Knaves, and Spies

> **From:** 2022 Q.6(a) -- [Marks: 05]

**The question:** Knights always tell the truth, Knaves always lie, and Spies can either tell the truth or lie. There are three people: A, B, and C. Exactly one is a Knight, one is a Knave, and one is a Spy. Each knows the identity of the other two.
(i) A says "C is the Knave", B says "A is the Knight", and C says "I am the spy". Determine whether there is a unique solution.
(ii) A says "I am the Knave", B says "I am the Knave", and C says "I am the Knave". Determine whether there is a unique solution.

**Let's solve this step by step:**

With 3 distinct roles (Knight = K, Knave = N, Spy = S) distributed among 3 people, there are exactly $3! = 6$ possible permutations. We test all six in an exhaustive truth table.

### Part (i): A says "C is the Knave", B says "A is the Knight", C says "I am the spy"

Let's test each permutation:

| Assignment (A, B, C) | A's Claim: "C is Knave" | B's Claim: "A is Knight" | C's Claim: "I am Spy" | Evaluation & Verdict |
|:---:|:---:|:---:|:---:|:---|
| **(K, N, C=S)** | False (C is Spy) | True (A is Knight) | True (C is Spy) | **Eliminated:** A is Knight but lied! |
| **(K, B=S, C=N)** | **True** (C is Knave) | **True** (A is Knight) | **False** (C is Knave) | **CONSISTENT!** Knight A told truth; Knave C lied; Spy B told truth (allowed). |
| **(N, K, C=S)** | False (C is Spy) | False (A is Knave) | True (C is Spy) | **Eliminated:** B is Knight but lied! |
| **(N, B=S, C=K)** | False (C is Knight)| False (A is Knave) | False (C is Knight) | **Eliminated:** C is Knight but lied! |
| **(A=S, K, C=N)** | True (C is Knave) | False (A is Spy) | False (C is Knave) | **Eliminated:** B is Knight but lied! |
| **(A=S, N, C=K)** | False (C is Knight)| True (A is Spy) | False (C is Knight) | **Eliminated:** C is Knight but lied! |

Only one permutation survives:
$$
\boxed{\text{(i) A = Knight, B = Spy, C = Knave}}
$$

---

### Part (ii): A, B, and C all say "I am the Knave"

Recall our Golden Secret: **Only a Spy can say "I am a Knave."**
- In this puzzle, exactly one person is a Spy.
- But all three individuals (A, B, C) uttered the sentence "I am the Knave".
- Therefore, at least two of the speakers must be a Knight or a Knave.
- If a Knight said it, that Knight lied (impossible).
- If a Knave said it, that Knave spoke the truth (impossible).
- Thus, every single one of the $3! = 6$ permutations produces a direct contradiction:

| Assignment | A's Statement | B's Statement | C's Statement | Verdict |
|:---:|:---:|:---:|:---:|:---|
| (K, N, S) | False | True | False | Knight A lied, Knave B spoke truth. Impossible. |
| (K, S, N) | False | False | True | Knight A lied, Knave C spoke truth. Impossible. |
| (N, K, S) | True | False | False | Knave A spoke truth, Knight B lied. Impossible. |
| (N, S, K) | True | False | False | Knave A spoke truth, Knight C lied. Impossible. |
| (S, K, N) | False | False | True | Knight B lied, Knave C spoke truth. Impossible. |
| (S, N, K) | False | True | False | Knave B spoke truth, Knight C lied. Impossible. |

Every permutation is eliminated.

$$
\boxed{\text{(ii) There is NO solution}}
$$

---

## 🔧 Worked Example 2: The Four Suspects Puzzle

> **From:** 2023 Q.5(b) -- [Marks: 04]

**The question:** Four friends have been identified as suspects for an unauthorized computer system access: Alice, John, Carlos, and Diana. Exactly one of them did it.
- Alice said: "Carlos did it."
- John said: "I did not do it."
- Carlos said: "Diana did it."
- Diana said: "Carlos lied when he said that I did it."
(i) If exactly one of the four suspects is telling the truth, who did it?
(ii) If exactly one is lying, who did it?

**Let's solve this step by step:**

Let the single culprit be one of $A, J, C, D$. First, notice the statements made:
- $S_A$: True if culprit is $C$.
- $S_J$: True if culprit is NOT $J$.
- $S_C$: True if culprit is $D$.
- $S_D$: True if culprit is NOT $D$ (direct negation of Carlos's claim).

> [!TIP] The Contradictory Pair Shortcut
> Look at Carlos ($S_C$) and Diana ($S_D$). Their claims are direct negations of each other:
> $$
> S_D \equiv \neg S_C
> $$
> This means that no matter who the culprit is, **exactly one of Carlos or Diana is ALWAYS telling the truth**, and the other is lying!

Now, let's construct the verification table testing each possible culprit:

| Assumed Culprit | $S_A$: "Carlos did it" | $S_J$: "John did not do it" | $S_C$: "Diana did it" | $S_D$: "Carlos lied" | Total Truths | Total Lies |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **Alice (A)** | $\text{F}$ | $\text{T}$ | $\text{F}$ | $\text{T}$ | 2 | 2 |
| **John (J)** | $\text{F}$ | $\text{F}$ | $\text{F}$ | $\text{T}$ | **1** | 3 |
| **Carlos (C)** | $\text{T}$ | $\text{T}$ | $\text{F}$ | $\text{T}$ | 3 | **1** |
| **Diana (D)** | $\text{F}$ | $\text{T}$ | $\text{T}$ | $\text{F}$ | 2 | 2 |

### Part (i): Exactly ONE person is telling the truth
Look at the "Total Truths" column:
- Only when **John** is the culprit does the truth count equal exactly 1 (only Diana tells the truth).

$$
\boxed{\text{(i) John did it}}
$$

### Part (ii): Exactly ONE person is lying
Look at the "Total Lies" column (which means 3 people tell the truth):
- Only when **Carlos** is the culprit does the lie count equal exactly 1 (only Carlos lies; Alice, John, and Diana all tell the truth).

$$
\boxed{\text{(ii) Carlos did it}}
$$

---

## 🔧 Worked Example 3: Lewis Carroll Syllogism (Sorites)

> **From:** 2022 Q.5(d) -- [Marks: 04]

**The question:** Consider these statements, where the first three are premises and the fourth is a valid conclusion:
- Premise 1: "All hummingbirds are richly colored."
- Premise 2: "No large birds live on honey."
- Premise 3: "Birds that do not live on honey are dull in color."
- Conclusion: "Hummingbirds are small."
Show that the conclusion follows logically from the premises.

**Let's solve this step by step:**

### Step 1: Define Predicates Over the Domain of All Birds
In Lewis Carroll puzzles, natural language antonyms represent negations:
- $P(x)$: $x$ is a hummingbird
- $Q(x)$: $x$ is large $\implies \neg Q(x)$: $x$ is small ("not large")
- $R(x)$: $x$ lives on honey $\implies \neg R(x)$: $x$ does not live on honey
- $S(x)$: $x$ is richly colored $\implies \neg S(x)$: $x$ is dull in color ("not richly colored")

### Step 2: Formalize Premises and Conclusion
- Premise 1: $\forall x\, (P(x) \to S(x))$
- Premise 2: $\forall x\, (Q(x) \to \neg R(x))$
- Premise 3: $\forall x\, (\neg R(x) \to \neg S(x))$
- Conclusion: $\forall x\, (P(x) \to \neg Q(x))$

### Step 3: Formal Deduction (Let $c$ be an arbitrary bird)

| Step | Formal Statement | Justification / Rule Used |
|:---:|:---|:---|
| 1 | $P(c) \to S(c)$ | Premise 1 (Universal Instantiation) |
| 2 | $\neg R(c) \to \neg S(c)$ | Premise 3 (Universal Instantiation) |
| 3 | $S(c) \to R(c)$ | Contrapositive of Step 2 |
| 4 | $P(c) \to R(c)$ | Hypothetical Syllogism from Steps 1 and 3 |
| 5 | $Q(c) \to \neg R(c)$ | Premise 2 (Universal Instantiation) |
| 6 | $R(c) \to \neg Q(c)$ | Contrapositive of Step 5 |
| 7 | $P(c) \to \neg Q(c)$ | Hypothetical Syllogism from Steps 4 and 6 |
| 8 | $\forall x\, (P(x) \to \neg Q(x))$ | Universal Generalization from Step 7 |

Since $\neg Q(x)$ means "small", the conclusion "Hummingbirds are small" follows validly.

$$
\boxed{\text{The argument is VALID via Universal Instantiation, Contraposition, and Hypothetical Syllogism}}
$$

---

## ⚡ Quick Review

**The golden rule of Knights and Knaves:** Only a Spy can say "I am a Knave." If everyone says it, there is no solution.

**The suspect puzzle trick:** Spot the contradictory pair ($S_C$ and $S_D$). One must be true and one must be false, cutting your search in half.

**The Lewis Carroll trick:** Encode antonyms as logical negations ("small" = $\neg\text{large}$, "dull" = $\neg\text{richly colored}$), then chain implications using contrapositives and hypothetical syllogism.

**Time estimate in exam:** 5 to 7 minutes to draw a 4-row or 6-row verification table.

---

## 🔗 Connected Topics

- [← Previous: DM-3.9 Rules of Inference](DM-3.9_Rules_of_Inference.md) -- Review Hypothetical Syllogism and Contraposition used in the Lewis Carroll proof.
- [→ Next: DM-3.11 Logic Gates](DM-3.11_Logic_Gates.md) -- Transition from word puzzles to hardware circuits.
- [DM-3.12: Predicates and Quantifiers](DM-3.12_Predicates_and_Quantifiers.md) -- Explore the formal predicate logic underpinning $\forall x$ quantifiers.

---

[← Previous: DM-3.9 Rules of Inference](DM-3.9_Rules_of_Inference.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: DM-3.11 Logic Gates →](DM-3.11_Logic_Gates.md)
