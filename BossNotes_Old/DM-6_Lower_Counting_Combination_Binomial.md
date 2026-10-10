[← Previous: DM-6.3 Pigeonhole Principle](DM-6.3_Pigeonhole_Principle.md) | [🏠 Index](00_Index.md) | [Next: DM-7 Algorithms and Relevance →](DM-7_Algorithms_and_Relevance.md)

---

# DM-6 Lower: Counting, Combination, Binomial
> **Section:** B (Discrete Mathematics) | **Priority:** 🟠 (all three subtopics) | **Exam Frequency:** 3/3 DM papers (2022 Q.8(b) & (c), 2023 Q.8(b) & (c), 2024 Q.8(c))
> **Subtopics:** DM-6.1 (Basic Counting Techniques), DM-6.5 (Combination), DM-6.6 (Binomial Theorem)
> **Sources:** Rosen §6.1 (pp. 2–11), §6.3 (pp. 23–27, Theorems 1–2, Corollary 2), §6.4 (pp. 31–35, Theorems 1–2, Corollaries 1–3), Fahad Notes Class-20, Raidah Notes §6.1, §6.3, §6.4, Shishir Notes §1, §4, §5

## Why This Topic Matters

Three subtopics, one question each, and the whole thing is arithmetic plus one formula you have to state exactly right. The Binomial Theorem question in 2023 is worth four marks, the largest single counting mark in the DM section, and it is only a factorial and a sign. The combination question is three marks and the classic cancellation trap takes most of the marks away.

The DM papers sit at the end of the paper and the counting block is always in the same place. In 2022 the paper asked sum rule (b), generalized pigeonhole (c), and the remainder proof (d). In 2023 it asked pigeonhole (a), combination (b), binomial theorem (c), and relevance (d). Learn these three files and Question 8 in a DM paper is covered.

---

## 📝 Key Definitions

> **Product rule:** "Suppose that a procedure can be broken down into a sequence of two tasks. If there are $n_1$ ways to do the first task and for each of these ways of doing the first task, there are $n_2$ ways to do the second task, then there are $n_1n_2$ ways to do the procedure." — Rosen, §6.1 (p. 2)

> **Sum rule:** "If a task can be done either in one of $n_1$ ways or in one of $n_2$ ways, where none of the set of $n_1$ ways is the same as any of the set of $n_2$ ways, then there are $n_1 + n_2$ ways to do the task." — Rosen, §6.1 (p. 5)

> **Subtraction rule (inclusion-exclusion for two sets):** "If a task can be done in either $n_1$ ways or $n_2$ ways, then the number of ways to do the task is $n_1 + n_2$ minus the number of ways to do the task that are common to the two different ways." — Rosen, §6.1 (p. 9)

> **Division rule:** "There are $n/d$ ways to do a task if it can be done using a procedure that can be carried out in $n$ ways, and for every way $w$, exactly $d$ of the $n$ ways correspond to way $w$." — Rosen, §6.1 (p. 9)

> **Permutation:** "A **permutation** of a set of distinct objects is an ordered arrangement of these objects." — Rosen, §6.3 (p. 23)

> **Permutation count (Corollary 1):** "If $n$ and $r$ are integers with $0 \le r \le n$, then $P(n, r) = \dfrac{n!}{(n - r)!}$." — Rosen, §6.3 (p. 24)

> **Combination:** "An **$r$-combination** of elements of a set is an unordered selection of $r$ elements from the set. Thus, an $r$-combination is simply a subset of the set with $r$ elements." — Rosen, §6.3 (p. 26)

> **Combination count (Theorem 2):** "The number of $r$-combinations of a set with $n$ elements, where $n$ is a nonnegative integer and $r$ is an integer with $0 \le r \le n$, equals $C(n, r) = \dfrac{n!}{r!(n - r)!}$." — Rosen, §6.3 (p. 26)

> **Binomial theorem (Theorem 1):** "Let $x$ and $y$ be variables, and let $n$ be a nonnegative integer. Then $(x + y)^n = \sum_{j=0}^n \binom{n}{j} x^{n-j}y^j$." — Rosen, §6.4 (p. 31)

> **Pascal's identity (Theorem 2):** "Let $n$ and $k$ be positive integers with $n \ge k$. Then $\binom{n + 1}{k} = \binom{n}{k - 1} + \binom{n}{k}$." — Rosen, §6.4 (p. 34)

> **Why the name:** "The number of $r$-combinations from a set with $n$ elements is often denoted by $\binom{n}{r}$. This number is also called a **binomial coefficient** because these numbers occur as coefficients in the expansion of powers of binomial expressions such as $(a + b)^n$." — Rosen, §6.4 (p. 31)

---

## DM-6.1: Basic Counting Techniques

### Which rule, and how to tell

There are four rules and the exam never gives you a name. It gives you a story. Ask two questions of the story.

**Question 1: do the choices happen one after another, or instead of one another?**

- One after another, and each choice leaves the next one unchanged: **product rule**.
- One instead of another, never both, no overlap: **sum rule**.

**Question 2: do the two groups of ways share members?**

- Disjoint, so no overlap: sum rule, done.
- Overlapping: the sum overcounts the shared cases, so subtract them once. That is the **subtraction rule**.

The quickest test is to look for the words that signal each case. "Via", "and then", "each": sequential, so product. "Either ... or", "one of", "as well as": alternatives, so sum. If the alternatives are not disjoint, subtract the overlap.

### The product rule

Two tasks, then many tasks.

$$
\text{ways} = n_1 \times n_2 \quad \text{for two tasks}
$$

$$
\text{ways} = n_1 \cdot n_2 \cdots n_m \quad \text{for a sequence of } m \text{ tasks}
$$

The extended form only works if each task's count is **independent** of how the earlier tasks were done. That is the condition people forget.

Rosen's Example 5 (p. 2): license plates of three letters then three digits give $26 \cdot 26 \cdot 26 \cdot 10 \cdot 10 \cdot 10 = 17{,}576{,}000$ plates. Rosen's Example 6: functions from an $m$-element set to an $n$-element set number $n^m$, which is the same rule with $m$ identical choices. Rosen's Example 8: the North American numbering plan multiplies out to $1{,}024{,}000{,}000$ numbers under the old format and $6{,}400{,}000{,}000$ under the new one. Raidah notes §6.3 works that last example on the board.

### The sum rule

$$
\text{ways} = n_1 + n_2 + \dots + n_m \quad \text{when the } m \text{ sets are pairwise disjoint}
$$

The condition is **pairwise disjoint**, not just "different". If even one case is counted in two groups, the sum is wrong. That is the whole reason the subtraction rule exists.

### The subtraction rule

For two overlapping sets,

$$
|A_1 \cup A_2| = |A_1| + |A_2| - |A_1 \cap A_2|
$$

The overlap is counted twice in the sum, so subtract it once to bring it back to one. Rosen's Example 18 (p. 9): 8-bit strings starting with 1 number $2^7 = 128$, strings ending in 00 number $2^6 = 64$, and the strings doing both number $2^5 = 32$, giving $128 + 64 - 32 = 160$.

Raidah notes §6.4 gives the same two-line form and warns that the mutual-exclusivity condition is the part students skip.

### The division rule

When every outcome is produced exactly $d$ times by the procedure, divide:

$$
\text{ways} = \frac{n}{d}
$$

Rosen's Example 20 (p. 10): four people round a circular table give $4! = 24$ labelled seatings, but each real arrangement is produced four times, once per choice of who sits in seat 1. So $24/4 = 6$. This is also the rule that produces the combination formula: every combination corresponds to exactly $r!$ permutations.

> [!tip] The counting rules in one line each
> Product: tasks in sequence. Sum: alternatives, disjoint. Subtraction: alternatives, overlapping, subtract the overlap once. Division: every outcome counted $d$ times, divide by $d$.

---

## DM-6.5: Combinations

### Permutation or combination?

That is the entire decision, and it turns on a single question: **does order matter?**

| Situation | Type | Formula |
| :-- | :-- | :-- |
| Arrange, line up, award first/second/third, seat in order | Permutation | $P(n,r) = \dfrac{n!}{(n-r)!}$ |
| Select a team, a committee, a crew, a subset | Combination | $C(n,r) = \binom{n}{r} = \dfrac{n!}{r!(n-r)!}$ |

Fahad notes Class-20 put it as a margin note in Bengali: selection leads to $C$, arrangement leads to $P$. Raidah notes §6.1 repeat the pairing.

### Why the formulas differ by $r!$

Start from the permutation count, which is what the product rule gives:

$$
P(n, r) = \frac{n!}{(n-r)!}
$$

Every group of $r$ people appears in this list exactly $r!$ times, once for each way of writing the group down in order. Six people give $6! = 720$ orderings of the same crew. So the number of groups is the permutation count divided by $r!$:

$$
C(n,r) = \frac{P(n,r)}{r!} = \frac{n!}{r!(n-r)!}
$$

Rosen gives this as a second proof of Theorem 2 using the division rule (§6.3, p. 26).

### The symmetry identity

$$
\binom{n}{r} = \binom{n}{n-r}
$$

Choosing $r$ to include is the same act as choosing $n-r$ to leave out. The factorial formula shows it too: only the order of $r!$ and $(n-r)!$ in the denominator changes.

This is a free mark on any coefficient question. In 2023 Q.8(c) you need $\binom{25}{13}$, and the symmetry lets you compute $\binom{25}{12}$ instead, which is the same number with a smaller index.

### Computing the factorial ratio

The direct formula is useless for large $n$ because factorials overflow. Cancel $(n-r)!$ first:

$$
C(n,r) = \frac{n!}{r!(n-r)!} = \frac{n(n-1)\cdots(n-r+1)}{r!}
$$

So the practical recipe is: build the falling product of $r$ terms, then divide the **whole product** by the **whole** $r!$. Rosen is explicit about this on p. 27, and he warns that cancelling pairwise is where the work goes wrong.

> [!warning] The pairwise-cancellation trap
> A tempting grouping for $\binom{30}{6}$ is
> $\frac{30 \cdot 29}{2} \times \frac{28 \cdot 27}{6} \times 26 \cdot 25 = 435 \times 126 \times 650 = 35626500$,
> which is **60 times too large**.
>
> The reason is that 2 and 6 cancel only $12$ of the required $720$. To cancel correctly the divisors must multiply to $720$, for example $6! = 6 \times 120$ split as $2 \times 360$, or simply divide the whole numerator by $720$ in one step.
>
> The error is silent because the arithmetic still looks tidy and the number is still plausible. This is the same failure mode as the 2018 Runge-Kutta question, where every downstream figure was arithmetically correct and the head figure was wrong by a factor of ten.

### Repetition and multisets

When objects repeat, divide by the factorial of each multiplicity. Both Fahad (Class-20) and Raidah (§6.2) work the word `PROFESSOR` to show why. Letters are $\{P, R, O, F, E, S, S, O, R\}$: 9 letters, 6 distinct types, with $O$, $R$, $S$ each appearing twice. Arrangements of all nine letters number

$$
\frac{9!}{2! \cdot 2! \cdot 2!} = \frac{362880}{8} = 45360
$$

Raidah's variant asks for 4 letters chosen from `PROFESSOR`, which forces a three-case split by multiplicity: 4 distinct ($360$), one pair plus two singles ($360$), two pairs ($18$), totalling $738$. Shishir notes §4.4 give the multinomial general form

$$
\frac{n!}{n_1! \, n_2! \cdots n_k!}
$$

for $n$ objects with $n_1 + n_2 + \dots + n_k = n$.

---

## DM-6.6: Binomial Theorem

### The theorem

For a nonnegative integer $n$,

$$
(x + y)^n = \sum_{r=0}^{n}\binom{n}{r}x^{n-r}y^r
$$

Written out, this is

$$
(x + y)^n = \binom{n}{0}x^n + \binom{n}{1}x^{n-1}y + \dots + \binom{n}{n-1}xy^{n-1} + \binom{n}{n}y^n
$$

### The general term

$$
T_{r+1} = \binom{n}{r}x^{n-r}y^r, \qquad r = 0, 1, \dots, n
$$

This is the single most useful line in the topic. Every coefficient question reduces to: **find $r$ such that the exponents match.**

Two rules read straight off it:

1. The exponent of $x$ is $n - r$.
2. The exponent of $y$ is $r$.

So in any term, the two exponents add to $n$. Check that first. If they do not, $r$ is already wrong and no arithmetic is needed.

### Why the coefficient is a binomial coefficient

Rosen's proof (Theorem 1, p. 31) is a counting argument, and it is short. Write $(x+y)^n$ as a product of $n$ sums. To get a term of the form $x^{n-r}y^r$, you must pick $x$ from $n-r$ of the sums and $y$ from the other $r$. The number of ways to choose **which** $r$ sums give the $y$ is $\binom{n}{r}$. That count is the coefficient.

Shishir notes §5.3 give the same idea for $(x+y)^3$, where the coefficients $1, 3, 3, 1$ are read off as $\binom{3}{0}, \binom{3}{1}, \binom{3}{2}, \binom{3}{3}$.

### Pascal's identity

$$
\binom{n+1}{r} = \binom{n}{r-1} + \binom{n}{r}
$$

**Algebraic proof.** Take the right-hand side and put both terms over a common denominator, using $r! = r(r-1)!$ and $(n-r+1)! = (n-r+1)(n-r)!$:

$$
\begin{aligned}
\binom{n}{r-1} + \binom{n}{r}
&= \frac{n!}{(r-1)!(n-r+1)!} + \frac{n!}{r!(n-r)!} \\
&= \frac{n! \cdot r}{r!(n-r+1)!} + \frac{n! \cdot (n-r+1)}{r!(n-r+1)!} \\
&= \frac{n! \left[ r + (n - r + 1) \right]}{r!(n-r+1)!} \\
&= \frac{n!(n+1)}{r!(n+1-r)!} \\
&= \frac{(n+1)!}{r!(n+1-r)!} = \binom{n+1}{r}
\end{aligned}
$$

The two terms in the bracket add to $n+1$, which is the whole trick.

![Pascal's triangle shown in two forms. On the left the symbolic entries C(n, k); on the right the numerical rows. Two adjacent entries in row 6, C(6,4) and C(6,5), add to C(7,5) in row 7, which is Pascal's identity. Rosen §6.4 Figure 1, p. 35](diagrams/dm6_pascals_triangle_identities.jpg)

*Figure 1 — Pascal's Triangle. Rosen §6.4, p. 35.*

Read the highlighted entries. $\binom{6}{4} = 15$ and $\binom{6}{5} = 6$ sit next to each other in row 7, and they sum to $21 = \binom{7}{5}$ in row 8. That is the identity in the picture.

### Identities you get for free by substitution

| Substitution | Result | Where it comes from |
| :-- | :-- | :-- |
| $x = 1$, $y = 1$ | $\displaystyle\sum_{k=0}^{n}\binom{n}{k} = 2^n$ | Total number of subsets of an $n$-element set (Rosen Corollary 1, p. 33) |
| $x = -1$, $y = 1$ | $\displaystyle\sum_{k=0}^{n}(-1)^k \binom{n}{k} = 0$ | $((-1)+1)^n = 0$ for $n > 0$ (Rosen Corollary 2, p. 34) |
| $x = 1$, $y = 2$ | $\displaystyle\sum_{k=0}^{n} 2^k \binom{n}{k} = 3^n$ | $(1+2)^n$ (Rosen Corollary 3, p. 34) |

Shishir notes §5.3 add the second one expanded: the sum of the even-indexed coefficients equals the sum of the odd-indexed ones, and each is $2^{n-1}$.

### Finding a coefficient: the procedure

Work in this order. It kills both traps before any arithmetic happens.

1. **Write the substituted expansion on one line.** For $(2x - 3y)^{25}$ write
   $(2x - 3y)^{25} = \sum_{r=0}^{25}\binom{25}{r}(2x)^{25-r}(-3y)^r$.
   Now the exponents and the bases are visible together.
2. **Match the exponents.** For $x^{12}y^{13}$ you need $25 - r = 12$ and $r = 13$.
3. **Check they add to $n$.** $12 + 13 = 25$. If this fails, stop; $r$ is wrong.
4. **Read the coefficient off the same line.** $\binom{25}{13}\cdot 2^{12}\cdot(-3)^{13}$. The exponent on $x$ tells you the power of 2; the exponent on $y$ tells you the power of $-3$.
5. **Watch the sign.** The exponent of $y$ is odd here, so the answer is negative.

> [!warning] Two sign and index traps
> **The sign is negative.** The exponent of $y$ is $r = 13$, which is odd, and $(-3)^{13}$ is negative. Forgetting the sign of $(-3y)^{13}$ is the most common error here, and it is a factor-of-minus-one error that a sanity check on magnitude will not catch.
>
> **The power of 2 belongs to $x$, not to $y$.** $(2x)^{12}$ gives $2^{12} = 4096$. Writing $2^{13}$ instead is the second most common error, and it produces a wildly different number, so at least that one is self-detecting.
>
> The rule that prevents both: the exponent of $x$ in a term is $n - r$, so the factor $2$ carries $n - r = 12$ while the factor $-3$ carries $r = 13$. **The exponents in the monomial decide which base goes with which factor.**

---

## Exam Variants

| Year | Question | Subtopic | Marks | Key answer |
| :-- | :-- | :-- | --: | :-- |
| 2022 Q.8(b) | Routes Boston to Detroit to Los Angeles | DM-6.1 | 02 | $\boxed{24 \text{ routes}}$ |
| 2023 Q.8(b) | Select 6 crew from 30 astronaut candidates | DM-6.5 | 03 | $\boxed{\binom{30}{6} = 593775 \text{ ways}}$ |
| 2023 Q.8(c) | Coefficient of $x^{12}y^{13}$ in $(2x-3y)^{25}$ | DM-6.6 | 04 | $\boxed{\text{coefficient of } x^{12}y^{13} = -33959763545702400}$ |

The three questions are one mark apart in weight, and each one tests a different decision: which rule, which formula, which term.

---

## 🏆 Golden Questions (Past Exam Archive)

### 🎯 There are four major auto routes from Boston to Detroit and six from Detroit to Los Angeles. How many major auto routes are there from Boston to Los Angeles via Detroit?
> **Appeared:** 2022 Q.8(b) — (02 marks)

**Full Answer:**

**Setting up.** A route via Detroit is fully described by **one** choice from Boston to Detroit **and one** choice from Detroit to Los Angeles. There is no other freedom, and the order is fixed by the geography: Boston first, Detroit second, Los Angeles third.

This is the **product rule**, also called the multiplication principle:

$$
\text{number of routes} = 4 \times 6
$$

$$
\boxed{24 \text{ routes}}
$$

> [!info] Check
> The four Boston choices against the six Detroit choices form a $4 \times 6$ grid of 24 cells, one route each. The direct product confirms $4 \times 6 = 24$.

> [!warning] The sum rule does not apply here
> The **sum rule** applies to mutually exclusive alternatives: either go through Detroit or through Chicago, never both. Here every route *must* go through Detroit, so the choices are sequential rather than alternative, and the product rule is the one that fits.
>
> The quickest way to tell the two apart: ask whether the choices happen one after the other (product) or instead of one another (sum). "Via Detroit" is the clearest possible example of the first kind.

> [!note] Why permutations do not apply either
> A route is fixed by its two legs, so choosing leg 1 then leg 2 already fixes the whole route. No reordering is possible or meaningful, so this is a combination-like count of 24 distinct paths, not 24 orderings of something.
>
> If the question had asked about the round trip, the count would change shape entirely, because a return leg is not independent of the outward one.

---

### 🎯 A group of 30 people have been trained as astronauts to go on the first mission to mars. How many ways are there to select a crew of six people to go on this mission (assuming all crew members have the same job)?
> **Appeared:** 2023 Q.8(b) — (03 marks)

**Full Answer:**

**Setting up.** Selection is without regard to order, so order does **not** matter: the crew $\{A, B, C\}$ is the same crew whichever order you write it. Every crew member has the same job, so there is no assignment to count either. This is a combination, $\binom{n}{r}$, not a permutation.

$$
\text{Ways} = \binom{30}{6} = \frac{30!}{6!\,24!}
$$

**Computing the factorial ratio.**

$$
= \frac{30 \cdot 29 \cdot 28 \cdot 27 \cdot 26 \cdot 25}{6 \cdot 5 \cdot 4 \cdot 3 \cdot 2 \cdot 1} = \frac{30 \cdot 29 \cdot 28 \cdot 27 \cdot 26 \cdot 25}{720}
$$

Group the numerator in pairs:

$$
30 \cdot 29 = 870, \qquad 28 \cdot 27 = 756, \qquad 26 \cdot 25 = 650
$$

$$
870 \times 756 \times 650 = 427518000
$$

$$
\frac{427518000}{720} = 593775
$$

$$
\boxed{\binom{30}{6} = 593775 \text{ ways}}
$$

> [!info] Three routes to the same number
> - $\frac{30!}{6!\,24!}$ evaluated directly gives $593775$.
> - The paired product $\frac{870 \times 756 \times 650}{720}$ gives $\frac{427518000}{720} = 593775$.
> - An independent implementation of $\binom{30}{6}$ gives $593775$.
>
> Note $427518000 = 720 \times 593775$, which is the *ordered* count that appears below. The two numbers differ by exactly $6!$, as they must.

> [!warning] Do not cancel the numerator into three pairs
> A tempting grouping is
> $\frac{30\cdot29}{2}\times\frac{28\cdot27}{6}\times 26\cdot25 = 435 \times 126 \times 650 = 35626500$,
> which is **60 times too large**.
>
> The reason is that $2$ and $6$ cancel only $12$ of the required $720$. To cancel correctly the three divisors must multiply to $720$, for example $6! = 6 \times 120$ split as $2 \times 360$, or simply divide the whole numerator by $720$ in one step.
>
> Cancelling pairwise is where this answer most often goes wrong, and the error is silent because the arithmetic still looks tidy and the number is still plausible. It is the same failure mode as the $2018$ Runge-Kutta question, where every downstream figure was arithmetically correct and the head figure was wrong by a factor of ten.

> [!note] Why the assumption in the question matters
> "All crew members have the same job" is precisely what makes this $\binom{30}{6}$. Change the assumptions and the answer changes by a clean factor:
>
> - If the crew had a **commander**, the count would be
> $30 \times \binom{29}{5} = 30 \times 118755 = 3562650$, choosing the commander first.
> - If **order were counted**, the answer would be $\frac{30!}{24!} = 427518000$,
> which is exactly $6! = 720$ times larger, because each crew could be seated in
> $720$ orders.
>
> The question's assumption removes precisely that factor. Being able to say which assumption your formula depends on is what separates a combination answer from a memorised one.

---

### 🎯 Briefly describe Binomial theorem and what is the co-efficient of $x^{12}y^{13}$ in the expansion of $(2x - 3y)^{25}$ ?
> **Appeared:** 2023 Q.8(c) — (04 marks)

**Full Answer:**

**The theorem.** For positive integers $m$ and $n$,

$$
(x + y)^n = \sum_{r=0}^{n}\binom{n}{r}x^{n-r}y^r
$$

The general term is

$$
T_{r+1} = \binom{n}{r}x^{n-r}y^r, \qquad r = 0, 1, \ldots, n
$$

A proof by induction on $n$: the case $n = 1$ is immediate, and the step follows from Pascal's identity $\binom{n+1}{r} = \binom{n}{r} + \binom{n}{r-1}$ applied to $(x+y)^{n+1} = (x+y)^n \cdot (x+y)$.

**Applying it.** With $x \to 2x$ and $y \to -3y$ and $n = 25$,

$$
(2x - 3y)^{25} = \sum_{r=0}^{25}\binom{25}{r}(2x)^{25-r}(-3y)^r
$$

**Identify the term.** A general term carries $x^{25-r}y^r$. For $x^{12}y^{13}$ we need

$$
25 - r = 12 \quad \text{and} \quad r = 13
$$

Both give $r = 13$, and the powers $12 + 13 = 25$ check out.

**The coefficient.**

$$
\text{coefficient} = \binom{25}{13}(2)^{12}(-3)^{13}
$$

Since $\binom{25}{13} = \binom{25}{12} = 5200300$,

$$
= 5200300 \times 4096 \times (-1594323)
$$

$$
\boxed{\text{coefficient of } x^{12}y^{13} = -33959763545702400}
$$

> [!info] Confirming the product
> Expanding $(2x - 3y)^{25}$ directly and reading off the coefficient of
> $x^{12}y^{13}$ returns $-33959763545702400$, the same value as
> $5200300 \times 4096 \times (-1594323)$. The three factors multiply out as
> $21300428800 \times (-1594323)$, confirming the product.

> [!warning] Two sign and index traps
> **The sign is negative.** The exponent of $y$ is $r = 13$, which is odd, and
> $(-3)^{13}$ is negative. Forgetting the sign of $(-3y)^{13}$ is the most common
> error here, and it is a factor-of-minus-one error that a sanity check on
> magnitude will not catch.
>
> **The power of 2 belongs to $x$, not to $y$.** $(2x)^{12}$ gives
> $2^{12} = 4096$. Writing $2^{13}$ instead is the second most common error, and
> it produces a wildly different number, so at least that one is self-detecting.
>
> The rule that prevents both: the exponent of $x$ in a term is $n - r$, so the
> factor $2$ carries $n - r = 12$ while the factor $-3$ carries $r = 13$. **The
> exponents in the monomial decide which base goes with which factor.** Write
> $(2x)^{25-r}(-3y)^r$ on one line and read the exponents straight off it.
>
> A useful check on $r$: the two exponents must add to $n$. Here $12 + 13 = 25$.
> If your $r$ does not satisfy that, it is wrong before any arithmetic happens.

**PYQ coverage for DM-6.1, DM-6.5, DM-6.6:** 3 manifest rows (2022 Q.8(b), 2023 Q.8(b), 2023 Q.8(c)) across 3 unique questions, 3 blocks, 0 missing.

---

## ⚡ Exam Tips & Common Mistakes

1. **Name the rule before using it.** Writing "by the product rule, $4 \times 6$" earns the method mark. Writing just "$4 \times 6 = 24$" may not.
2. **Say why the sum rule does not apply.** In 2022 Q.8(b) the alternative reading is "either via Detroit or via Chicago". Pointing out that the question fixes Detroit removes the alternative and confirms the product rule.
3. **Divide by the whole $r!$ in one step.** The cancellation trap in $\binom{30}{6}$ costs a full mark and the arithmetic looks clean while it is wrong.
4. **Use the symmetry identity when it helps.** $\binom{25}{13} = \binom{25}{12}$, and 12 is easier to compute than 13.
5. **Write the substituted expansion before you match anything.** $(2x - 3y)^{25} = \sum \binom{25}{r}(2x)^{25-r}(-3y)^r$ puts both exponents and both bases in one place, which prevents the index swap.
6. **Check the exponents add to $n$.** $12 + 13 = 25$. One line, and it catches a wrong $r$ before any multiplication.
7. **Carry the odd-power sign through.** $r = 13$ is odd, so $(-3)^{13}$ is negative. State this; it is the mark that the final sign is deliberate.
8. **Combination, not permutation, for a crew.** If you give $427518000$ you have counted the orderings. The question says selection, and every crew has the same job.

## 🔗 Related Topics

- [DM-6.3: Pigeonhole Principle](DM-6.3_Pigeonhole_Principle.md) — previous in the chain; the same counting ideas turned into a guarantee rather than a count
- [DM-7: Algorithms and Relevance](DM-7_Algorithms_and_Relevance.md) — next in the chain, where counting becomes the operation count that gives time complexity
- [DM-3.9: Rules of Inference and Valid Arguments](DM-3.9_Rules_of_Inference_and_Valid_Arguments.md) — Pascal's identity is proved the same way as a valid argument, by exhaustively splitting the cases
- [DM-5.4: Modular Arithmetic and Congruence](DM-5.4_Modular_Arithmetic_and_Congruence.md) — the residue counting that produces the $d$ boxes in the pigeonhole proof

---

[← Previous: DM-6.3 Pigeonhole Principle](DM-6.3_Pigeonhole_Principle.md) | [🏠 Index](00_Index.md) | [Next: DM-7 Algorithms and Relevance →](DM-7_Algorithms_and_Relevance.md)