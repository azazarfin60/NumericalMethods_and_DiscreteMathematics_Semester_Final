---
title: "DM-6.3 · Pigeonhole Principle"
tags:
  - numerical-methods
  - discrete-mathematics
  - topicwise
---





[🏠 Subtopic Index](00_Index.md) | [← Prev: DM-6.1 Basic Counting Techniques](DM-6.1_Basic_Counting_Techniques.md) | [Next: DM-6.5 Combination →](DM-6.5_Combination.md)

---

# DM-6.3 · Pigeonhole Principle

Every block below is copied from `../answers_explanation/`. The reasoning
is written once, in the year-wise file, and is not restated here.


### [2022 Q.8(c), 2024 Q.8(c)]

**Appeared in:** 2022 Q.8(c), 2024 Q.8(c)

**Question.** Give a real-world example of generalized pigeonhole principle.

*[Marks: 02, CO: 3]*

**Solution.**

**The principle.** If $N$ objects are placed into $k$ boxes and $N > k$, then at
least one box holds at least two objects. The **generalized** form: if
$N > mk$, then some box holds at least $m + 1$ objects.

**Real-world examples.**

1. **Birth months in a class.** With 12 months, a class of 25 students guarantees
   that at least 3 share a birth month, since $25 > 2 \times 12 = 24$. Here
   $m = 2$, $k = 12$, and $N = 25$ is the smallest class that forces a triple.
2. **Socks from a drawer.** A drawer holds only black and white socks. Drawing 5
   socks guarantees at least 3 of one colour, since $5 > 2 \times 2 = 4$.
3. **Hash tables.** Storing $n$ keys in $m$ buckets forces a collision once
   $n > m$. Keeping the load factor below 1, typically near 0.75, is what
   guarantees headroom before collisions become frequent.
4. **Servers.** A cluster with $r$ racks and $2r+1$ machines must place at least
   3 machines in one rack, since $2r + 1 > 2 \times r$.

$$\boxed{\text{More than } mk \text{ objects in } k \text{ boxes forces some box to hold } m+1}$$

> [!warning] The plain and generalized forms are different statements
> The plain principle is the case $m = 1$. The generalized form needs $N > mk$,
> which is a **stronger** condition on $N$ and yields a **stronger** conclusion.
>
> The commonest slip is to use $N > k$ when $m > 1$, which forces only *two* in a
> box rather than $m + 1$. With 25 students and 12 months, "more students than
> months" forces only a pair. The $2 \times 12 = 24$ threshold is what forces a
> triple.

> [!note] Reading off $m$ and $k$ from the story
> In every example, $k$ is the number of boxes and is counted directly from the
> story: 12 months, 2 colours, $m$ buckets, $r$ racks. Then $m$ is the number
> above which you want a guarantee, and $N$ must exceed $mk$.
>
> Hashing is the case worth internalising, because the principle is not an
> accident there but a design constraint. A table that guarantees no collision at
> all would need one bucket per key, which defeats the purpose of hashing.

---

### [2022 Q.8(d)]

**Question.** Let $d$ be a positive integer. Show that among any group of $d+1$ (not necessarily consecutive) integers there are two with exactly the same remainder when they are divided by $d$.

*[Marks: 02, CO: 3]*

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

**Step 3. Apply the pigeonhole principle.** There are $d+1$ integers placed into
$d$ boxes, and $d + 1 > d$. By the pigeonhole principle, at least one box contains
two or more integers.

**Step 4. Conclude.** Two integers $a_1, a_2$ share a box, so they share a
remainder. Writing $a_1 = q_1 d + r$ and $a_2 = q_2 d + r$ and subtracting gives

$$
a_1 - a_2 = (q_1 - q_2)d
$$

hence $d$ divides $a_1 - a_2$, which is exactly the statement that the two have the
same remainder on division by $d$.

$$\boxed{\text{Any } d+1 \text{ integers include two congruent modulo } d}$$

> [!info] Explicit cases
> | $d$ | Example with a forced repetition | Remainders |
> | --: | :-- | :-- |
> | 1 | $0, 0$ | $0, 0$ |
> | 3 | $0, 1, 2, 0$ | $0, 1, 2, 0$ |
> | 5 | $0, 1, 2, 3, 4, 0$ | $0, 1, 2, 3, 4, 0$ |
>
> In each case $d+1$ integers are given and $d$ remainders are available, so the
> repetition is forced rather than arranged.

> [!note] The bound is sharp, and that is what makes this a theorem
> With only $d$ integers no repetition is forced: take $0, 1, 2, \dots, d-1$,
> whose remainders are all distinct. Hence $d + 1$ is the **smallest** number of
> integers that guarantees a collision.
>
> The word "not necessarily consecutive" in the question is what rules out the
> other obvious route. If the integers were consecutive you could simply look at
> $d$ consecutive remainders, which cycle through all $d$ values and then repeat.
> The hypothesis has to be the general one for the pigeonhole argument to be
> needed at all.

> [!note] What this is used for
> This is the statement behind every proof of the pigeonhole principle for
> congruences, and behind the fact that $x \equiv y \pmod d$ has infinitely many
> solutions while $x \equiv y \pmod n$ with the same residue class has at most
> $\gcd(x-y, n)$ distinct residues.
>
> It is also the reason a hash table with $m$ buckets cannot hold $m+1$ distinct
> keys without a collision. Same counting argument, different words.

---

### [2023 Q.8(a)]

**Question.** Briefly describe the pigeonhole principle with a real world example.

*[Marks: 02, CO: 1]*

**Solution.**

**The principle.** If $N$ objects are placed into $k$ boxes and $N > k$, then at
least one box holds at least two objects.

**Proof.** Suppose every box held at most one object. Then the boxes would hold
at most $k$ objects in total. But $N > k$, a contradiction.

**Real-world examples.**

1. **Socks.** From a drawer holding black and white socks only, drawing three
   socks guarantees two of a colour, since two boxes cannot take three objects
   with at most one each. This is the tightest version: $N = 3$ into $k = 2$.
2. **Birthdays.** With 366 possible birthdays, the *plain* principle needs $367$
   people to force a shared birthday, not 23. The famous result is therefore a
   **probabilistic** one, not a pigeonhole one: under a random model, past about
   23 people the chance of a shared birthday exceeds $50\%$.
3. **Pigeonholes in a building.** A building with $n$ floors and $n + 1$ people
   must have two on the same floor.
4. **Hash tables.** Storing $n$ keys in $m$ buckets forces a collision once
   $n > m$, which is why the load factor is kept below 1.

$$
\boxed{\text{More objects than boxes forces at least one box to hold two or more}}
$$

> [!warning] The principle is deterministic, not probabilistic
> It states that a collision **must** happen, with no randomness and no
> probability. The birthday paradox is a different result: it says a shared
> birthday is **likely** under a random model of birthdays.
>
> Students mix these up constantly because both get called "pigeonhole". Socks are
> certain; birthdays are only probable. If you quote 23 as a pigeonhole result
> you are wrong, and the correct pigeonhole figure for a year with 366 possible
> birthdays is 367.

> [!note] The tighter generalised form
> The generalised principle says that if $N$ objects go into $k$ boxes, then some
> box holds at least $\lceil N/k \rceil$ objects. The plain form is the special
> case $\lceil N/k \rceil \ge 2$. Part (c) of Question 8 in the 2022 paper asks
> for a real-world instance of the generalised version, and the hash table example
> above is the standard answer: $n$ keys in $m$ buckets forces some bucket to
> hold at least $\lceil n/m \rceil$ keys.

---

[🏠 Subtopic Index](00_Index.md) | [← Prev: DM-6.1 Basic Counting Techniques](DM-6.1_Basic_Counting_Techniques.md) | [Next: DM-6.5 Combination →](DM-6.5_Combination.md)
