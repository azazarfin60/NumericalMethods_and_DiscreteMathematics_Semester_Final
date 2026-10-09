---
title: "DM-6.3 · Pigeonhole Principle"
tags:
  - numerical-methods
  - discrete-mathematics
  - topicwise
---

# DM-6.3 · Pigeonhole Principle

Every block below is copied from `../answers_exam_style/`, which is the
only place an answer is authored. A number here is the same number, character
for character, as the one it came from.


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
