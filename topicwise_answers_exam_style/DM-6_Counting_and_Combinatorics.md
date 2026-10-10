---
title: "DM-6 · Counting & Combinatorics"
tags:
  - numerical-methods
  - discrete-mathematics
  - topicwise-clusters
---

[🏠 Master Index](00_Index.md) | [← Prev Topic: DM-5 · Number Theory](DM-5_Number_Theory.md) | [Next Topic: DM-7 · Supplementary DM →](DM-7_Supplementary_Discrete_Mathematics.md)

---

# DM-6 · Counting & Combinatorics

> **Topic ID:** DM-6  
> **Section:** Section B -- Discrete Mathematics  
> **Exam Weight:** 🔴 High Priority (Tier 1) | 3/3 Years (2022–2024) (100% Frequency) | Typical Weight: 7–10 marks (Question 7/8)  
> **Subtopics Included:** 4 subtopics (DM-6.1 through DM-6.6)  
> **Origin Layer:** Authored in `../answers_exam_style/`. All numerical results and boxed equations match character-for-character.

---

## 📑 Subtopics Covered in this Cluster

| Subtopic ID | Subtopic Title | Priority | Exam Frequency | Section Navigation |
|:---|:---|:---:|:---:|:---|
| **DM-6.1** | Basic Counting Techniques | 🟠 | 2022 | [Jump to DM-6.1](#dm-61) |
| **DM-6.3** | Pigeonhole Principle | 🔴 | 2022, 2023, 2024 | [Jump to DM-6.3](#dm-63) |
| **DM-6.5** | Combination | 🟠 | 2023 | [Jump to DM-6.5](#dm-65) |
| **DM-6.6** | Binomial Theorem | 🟠 | 2023 | [Jump to DM-6.6](#dm-66) |

---

<a id="dm-61"></a><a id="dm-6.1"></a>
## DM-6.1 · Basic Counting Techniques

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

<a id="dm-63"></a><a id="dm-6.3"></a>
## DM-6.3 · Pigeonhole Principle

### [2022 Q.8(c), 2024 Q.8(c)]

**Appeared in:** 2022 Q.8(c), 2024 Q.8(c)

**Question.** Give a real-world example of generalized pigeonhole principle.

**Solution.**

**The principle.** If $N$ objects are placed into $k$ boxes and $N > k$, then at
least one box holds at least two objects. The **generalized** form: if
$N > mk$, then some box holds at least $m + 1$ objects.

**Real-world examples.**

1. **Birth months in a class.** With 12 months, a class of 25 students guarantees
   that at least 3 share a birth month, since $25 > 2 \times 12 = 24$. Taking
   $m = 2$, $k = 12$ needs $N = 25$.

2. **Socks from a drawer.** A drawer holds only black and white socks. Drawing 5
   socks guarantees at least 3 of one colour, since $5 > 2 \times 2 = 4$.

3. **Hash tables.** Storing $n$ keys in $m$ buckets forces a collision once
   $n > m$. Keeping the load factor below 1, typically near 0.75, is what
   guarantees headroom before collisions become frequent.

4. **Servers.** A cluster with $r$ racks and $2r + 1$ machines must place at least
   3 machines in one rack.

$$
\boxed{\text{More than } mk \text{ objects in } k \text{ boxes forces some box to hold } m+1}
$$

> [!warning] The plain and generalized forms are different statements
> The plain principle is the case $m = 1$. Generalized needs
> $N > mk$, which is a **stronger** condition on $N$ and yields a **stronger**
> conclusion. The commonest slip is to use $N > k$ when $m > 1$, which forces
> only two in a box, not $m + 1$. With 25 students and 12 months, "more students
> than months" would force only a pair; the $2 \times 12 = 24$ threshold is what
> forces a triple.

---

### [2022 Q.8(d)]

**Question.** Let $d$ be a positive integer. Show that among any group of $d+1$ (not necessarily consecutive) integers there are two with exactly the same remainder when they are divided by $d$.

**Solution.**

**Proof.**

**Step 1. Count the possible remainders.** For any integer $a$, the division
algorithm gives

$$
a = qd + r, \qquad 0 \le r < d
$$

Every integer therefore has exactly one of the residues $0, 1, 2, \dots, d-1$.
There are exactly **$d$** possible remainders.

**Step 2. Identify the boxes.** Take the $d+1$ integers and let each box be one of
the $d$ possible remainders, $0$ through $d-1$. Place each integer in the box
named by its remainder.

**Step 3. Apply the pigeonhole principle.** There are $d + 1$ integers placed
into $d$ boxes, and $d + 1 > d$. By the pigeonhole principle, at least one box
contains two or more integers.

**Step 4. Conclude.** Two integers $a_1, a_2$ share a box, so they share a
remainder. Writing $a_1 = q_1 d + r$ and $a_2 = q_2 d + r$, subtracting gives

$$
a_1 - a_2 = (q_1 - q_2)d
$$

hence $d$ divides $a_1 - a_2$, which is exactly the statement that the two have the
same remainder on division by $d$.

$$
\boxed{\text{Any } d+1 \text{ integers include two congruent modulo } d}
$$

> [!info] Check
> For $d = 1, 2, \dots, 7$, explicit examples were constructed in which a repeated
> remainder occurs among $d+1$ integers: $d = 1$ gives $0, 0$; $d = 3$ gives
> $0, 1, 2, 0$; $d = 5$ gives $0, 1, 2, 3, 4, 0$. In every case the repetition is
> forced, matching the proof.

> [!note] The bound is sharp
> With only $d$ integers no repetition is forced: take $0, 1, 2, \dots, d-1$, whose
> remainders are all distinct. Hence $d + 1$ is the **smallest** number of integers
> that guarantees a collision, and the theorem says exactly that.

> [!note] What this is used for
> This is the statement behind every proof of the **pigeonhole principle** for
> congruences, and behind the fact that $x \equiv y \pmod d$ has infinitely many
> solutions while $x \equiv y \pmod n$ with the same residue class has at most
> $\gcd(x-y, n)$ distinct residues. It is also the reason a hash table with $m$
> buckets cannot hold $m+1$ distinct keys without a collision, which is the same
> counting argument with different words.

---

### [2023 Q.8(a)]

**Question.** Briefly describe the pigeonhole principle with a real world example.

**Solution.**

**The principle.** If $N$ objects are placed into $k$ boxes and $N > k$, then at
least one box holds at least two objects.

**Proof.** Suppose every box held at most one object. Then the boxes would hold
at most $k$ objects in total. But $N > k$, a contradiction.

**Real-world examples.**

1. **Birthdays.** With 366 possible birthdays, the *plain* principle needs $367$
   people to force a shared birthday, not 23. The famous result is therefore a
   **probabilistic** one, not a pigeonhole one: under a random model, past about
   23 people the chance of a shared birthday exceeds $50\%$. Quoting 23 as a
   pigeonhole result is wrong, and it is the most common error in this topic.

2. **Pigeonholes in a building.** A building with $n$ floors and $n + 1$ people
   must have two on the same floor.

3. **Socks.** From a drawer holding black and white socks only, drawing three
   socks guarantees two of a colour, since two boxes cannot take three objects
   with at most one each.

4. **Hash tables.** Storing $n$ keys in $m$ buckets forces a collision once
   $n > m$, which is why the load factor is kept below 1.

$$
\boxed{\text{More objects than boxes forces at least one box to hold two or more}}
$$

> [!warning] The pigeonhole principle is deterministic, not probabilistic
> It states that a collision **must** happen, with no randomness and no
> probability. The birthday paradox is a different result: it says a shared
> birthday is **likely** under a random model. Students mix these up because
> both are called "pigeonhole". Socks are certain, birthdays are only probable.

---

<a id="dm-65"></a><a id="dm-6.5"></a>
## DM-6.5 · Combination

### [2023 Q.8(b)]

**Question.** A group of 30 people have been trained as astronauts to go on the first mission to mars. How many ways are there to select a crew of six people to go on this mission (assuming all crew members have the same job)?

**Solution.**

**Setting up.** Selection is without regard to order, so order does **not**
matter. Every crew member has the same job, so there is no assignment to count.
This is a combination, $\binom{n}{r}$, not a permutation.

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

> [!info] Check
> Three routes agree:
> - $\frac{30!}{6!\,24!}$ evaluated directly gives $593775$
> - the paired product $\frac{870 \times 756 \times 650}{720}$ gives $\frac{427518000}{720} = 593775$
> - $\binom{30}{6}$ from an independent implementation gives $593775$
>
> Note $427518000 = 720 \times 593775$, which is the ordered count appearing below.

> [!warning] Do not split the numerator into three pairs and cancel incorrectly
> A tempting grouping is $\frac{30\cdot29}{2}\times\frac{28\cdot27}{6}\times 26\cdot25
> = 435 \times 126 \times 650 = 35626500$, which is **60 times too large**.
>
> The reason is that $2$ and $6$ cancel only $12$ of the required $720$. To
> cancel correctly the three divisors must multiply to $720$, for example
> $6! = 6 \times 120$ split as $2 \times 360$, or simply divide the whole
> numerator by $720$ in one step. Cancelling pairwise is where this answer most
> often goes wrong, and the error is silent because the arithmetic still looks
> tidy.

> [!note] Why the assumption matters
> "All crew members have the same job" is what makes this $\binom{30}{6}$. If
> the crew had a commander, the count would be $30 \times \binom{29}{5} =
> 30 \times 118755 = 3562650$, choosing the commander first. And if order were
> counted, $\frac{30!}{24!} = 427518000$, which is exactly $6! = 720$ times
> larger, because each crew could be seated in $720$ orders. The assumption in
> the question removes precisely that factor.

---

<a id="dm-66"></a><a id="dm-6.6"></a>
## DM-6.6 · Binomial Theorem

### [2023 Q.8(c)]

**Question.** Briefly describe the Binomial theorem, and what is the coefficient of $x^{12}y^{13}$ in the expansion of $(2x - 3y)^{25}$?

**Solution.**

**The theorem.** For positive integers $m$ and $n$,

$$
(x + y)^n = \sum_{r=0}^{n}\binom{n}{r}x^{n-r}y^r
$$

The general term is

$$
T_{r+1} = \binom{n}{r}x^{n-r}y^r, \qquad r = 0, 1, \ldots, n
$$

A proof by induction on $n$: the case $n = 1$ is immediate, and the step follows
from Pascal's identity $\binom{n+1}{r} = \binom{n}{r} + \binom{n}{r-1}$ applied to
$(x+y)^{n+1} = (x+y)^n \cdot (x+y)$.

**Applying it.** With $x \to 2x$ and $y \to -3y$ and $n = 25$,

$$
(2x - 3y)^{25} = \sum_{r=0}^{25}\binom{25}{r}(2x)^{25-r}(-3y)^r
$$

**Identify the term.** A general term carries $x^{25-r}y^r$. For
$x^{12}y^{13}$ we need

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

> [!info] Check
> Expanding $(2x - 3y)^{25}$ directly and reading off the coefficient of
> $x^{12}y^{13}$ returns $-33959763545702400$, the same value as
> $5200300 \times 4096 \times (-1594323)$. The three factors multiply out as
> $21300428800 \times (-1594323)$, confirming the product.

> [!warning] Two sign and index traps
> **The sign is negative.** The exponent of $y$ is $r = 13$, which is odd, and
> $(-3)^{13}$ is negative. Forgetting the sign of $(-3y)^{13}$ is the most
> common error here.
>
> **The power of 2 belongs to $x$, not to $y$.** $(2x)^{12}$ gives
> $2^{12} = 4096$. Writing $2^{13}$ instead is the second most common error.
> Since the exponent of $x$ is $n - r$, the factor $2$ carries $n - r = 12$
> while the factor $-3$ carries $r = 13$. The exponents of $x$ and $y$ in a term
> determine the base, hence the factor part.

---

[🏠 Master Index](00_Index.md) | [← Prev Topic: DM-5 · Number Theory](DM-5_Number_Theory.md) | [Next Topic: DM-7 · Supplementary DM →](DM-7_Supplementary_Discrete_Mathematics.md)
