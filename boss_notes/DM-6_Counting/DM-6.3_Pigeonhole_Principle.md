[← Previous: DM-6.2 Inclusion-Exclusion](DM-6.2_Inclusion_Exclusion.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: DM-6.4 Permutations →](DM-6.4_Permutations.md)

---

# DM-6.3: Pigeonhole Principle

> 🔴 **Priority:** Critical | **Tested:** 3/3 DM papers (2022, 2023, 2024) | **Typical marks:** 4

## What This Is (and Why It Matters)

The pigeonhole principle is the single most frequently tested discrete mathematics topic in RUET. It appeared in 2022, 2023, and 2024 without exception.

It does not calculate an exact number of arrangements. Instead, it provides a solid, deterministic guarantee: if you have more items than containers, at least one container must hold multiple items. In electrical and computer engineering, this simple principle explains why hash tables inevitably experience collisions, why network buffers overflow during traffic bursts, and why lossless data compression cannot shrink every possible file.

The exam repeatedly tests two versions: the plain form and the generalized form. Mastering the definitions, the contradiction proofs, and the distinction from probability ensures full marks on Question 8.

---

## 📝 Key Definitions

> **Pigeonhole principle (Plain form, Theorem 1):** "If $k$ is a positive integer and $k + 1$ or more objects are placed into $k$ boxes, then there is at least one box containing two or more of the objects." (Rosen, §6.2, p. 15)
>
> **In simple words:** If you have more pigeons than holes, at least one hole must contain two or more pigeons.

> **Generalized pigeonhole principle (Theorem 2):** "If $N$ objects are placed into $k$ boxes, then there is at least one box containing at least $\lceil N/k \rceil$ objects." (Rosen, §6.2, p. 17)
>
> **In simple words:** If you distribute $N$ objects across $k$ boxes, divide $N$ by $k$ and round up; at least one box must hold that many objects.

> **Dirichlet drawer principle:** "The pigeonhole principle is also called the **Dirichlet drawer principle**, after the nineteenth-century German mathematician G. Lejeune Dirichlet, who often used this principle in his work." (Rosen, §6.2, p. 15)
>
> **In simple words:** The historical European name for the pigeonhole principle, visualizing items placed into desk drawers.

> **Function corollary (Corollary 1):** "A function $f$ from a set with $k + 1$ or more elements to a set with $k$ elements is not one-to-one." (Rosen, §6.2, p. 15)
>
> **In simple words:** If a function maps from a larger domain to a smaller codomain, it cannot be one-to-one; at least two inputs must map to the same output.

---

![Pigeons placed into a grid of pigeonholes](../diagrams/dm6_pigeonhole_principle_boxes.jpg)

*Figure 1: Visual demonstration of the pigeonhole principle. In a grid of 12 holes, 12 pigeons can occupy one hole each. The moment a 13th pigeon arrives, at least one hole must hold two or more pigeons. Rosen §6.2, p. 15.*

---

## The Core Idea

### The Two Forms, Side by Side

The plain principle and the generalized principle make different claims. Conflating them is the most common error in student exam scripts.

| Feature | Plain Form (Theorem 1) | Generalized Form (Theorem 2) |
| :-- | :-- | :-- |
| **Mathematical Statement** | $k + 1$ objects into $k$ boxes | $N$ objects into $k$ boxes |
| **Required Condition on $N$** | $N > k$ | $N > mk$ (guarantees $m + 1$), or $\lceil N/k \rceil \ge r$ |
| **Resulting Guarantee** | At least one pair ($\ge 2$) | At least $\lceil N/k \rceil$ objects in one box |
| **Threshold for Group of $r$** | Guarantees only $r = 2$ | $N = k(r - 1) + 1$ |

The plain principle is simply the generalized principle evaluated at $r = 2$. When an exam problem asks you to guarantee a group of size $r \ge 3$, you must use the generalized threshold $N = k(r - 1) + 1$.

### Finding the Minimum Number of Objects: The Worst-Case Method

To find the minimum number of objects $N$ needed to guarantee that at least one box contains $r$ objects:

1. Imagine the worst-case distribution where you fill every box as much as possible without reaching $r$.
2. Each of the $k$ boxes gets $r - 1$ objects, consuming $k(r - 1)$ objects in total.
3. Adding just one more object forces some box to reach $r$ objects.

$$
N_{\min} = k(r - 1) + 1
$$

### Identifying Objects and Boxes in Word Problems

In every exam scenario, count the categories to find the number of boxes $k$:
- 12 calendar months: $k = 12$ boxes
- 2 sock colors (black and white): $k = 2$ boxes
- $d$ integer remainders modulo $d$: $k = d$ boxes
- 5 letter grades (A, B, C, D, F): $k = 5$ boxes
- $m$ hash table buckets: $k = m$ boxes
- $n$ building floors: $k = n$ boxes

---

## Proofs by Contradiction

Both forms are proved cleanly by contradiction. These proofs take only four lines to write in an exam.

### Proof of the Plain Form
Suppose, for contradiction, that none of the $k$ boxes contains more than one object.
Then every box holds at most 1 object, which means the total number of objects across all $k$ boxes is at most:

$$
\underbrace{1 + 1 + \dots + 1}_{k \text{ times}} = k
$$

However, we were given that there are at least $k + 1$ objects. Since $k + 1 > k$, this is an immediate contradiction.
Therefore, at least one box must contain two or more objects.

### Proof of the Generalized Form
Suppose, for contradiction, that every box holds fewer than $\lceil N/k \rceil$ objects.
Then each of the $k$ boxes contains at most $\lceil N/k \rceil - 1$ objects. The total number of objects in all boxes would be at most:

$$
k \left(\left\lceil \frac{N}{k} \right\rceil - 1\right) < k \left(\left(\frac{N}{k} + 1\right) - 1\right) = k \left(\frac{N}{k}\right) = N
$$

The strict inequality holds because $\lceil N/k \rceil < N/k + 1$ for all real numbers.
This implies the total number of objects is strictly less than $N$, contradicting the fact that exactly $N$ objects were placed in the boxes.
Therefore, at least one box must contain at least $\lceil N/k \rceil$ objects.

> [!NOTE] Why the Ceiling Function Matters
> The quotient $N/k$ is rarely an integer. If 25 students are grouped by 12 birth months, $25 / 12 = 2.083$. Pigeons cannot be split into fractions. The box receiving the extra student must round up to the next integer: $\lceil 25/12 \rceil = 3$. Rounding down would claim a guarantee of only 2, which underestimates the true mathematical guarantee.

---

## Deterministic Guarantee vs. Probability (The Common Exam Trap)

The pigeonhole principle is **deterministic**: it states that a collision must happen with 100% certainty, with zero assumptions about randomness or probability distributions.

The famous **Birthday Paradox** is an entirely different result: it states that under a uniform random model, a group of 23 people has a greater than 50% chance of sharing a birthday. That is a probabilistic calculation, not a pigeonhole guarantee.

| Scenario | Boxes $k$ | Deterministic Pigeonhole Guarantee | Probabilistic 50% Threshold |
| :-- | :--: | :--: | :--: |
| Shared birth date (non-leap year) | 365 | **366 people** | 23 people |
| Shared birth date (leap year accounted) | 366 | **367 people** | 23 people |
| Shared birth month | 12 | **13 people** | 5 people |
| Exam marks (0 to 100 integer scale) | 101 | **102 students** | Not applicable |
| English alphabet first letter | 26 | **27 words** | Not applicable |

> [!WARNING] The Exact Mistake That Loses Marks
> If an exam question asks for a real-world example of the pigeonhole principle, writing "in a room of 23 people, two share a birthday" is incorrect. 23 people do not guarantee a shared birthday; they only make it probable. The pigeonhole guarantee requires 367 people. Use socks, birth months, or hash tables as your primary exam examples to avoid any ambiguity.

---

## 🔧 Classic Worked Examples from Rosen

### Example 1: Grade Distributions (Generalized Threshold)
How many students must be in a discrete mathematics class to guarantee that at least 6 receive the same letter grade, assuming grades are A, B, C, D, and F?
- Boxes: $k = 5$ letter grades.
- Desired size: $r = 6$ students with the same grade.
- Applying the worst-case threshold formula:

$$
N = k(r - 1) + 1 = 5(6 - 1) + 1 = 5(5) + 1 = 26 \text{ students}
$$

With 25 students, it is possible for each grade to be assigned to exactly 5 students, so 26 is the true minimum.

### Example 2: Drawing Cards from a Standard Deck
How many cards must be selected from a standard 52-card deck to guarantee that at least 3 cards belong to the same suit?
- Boxes: $k = 4$ suits (hearts, diamonds, clubs, spades).
- Desired size: $r = 3$ cards of one suit.
- Minimum count:

$$
N = 4(3 - 1) + 1 = 4(2) + 1 = 9 \text{ cards}
$$

### Example 3: Telephone Area Codes
A state has 25 million telephone subscribers and 8 million available phone numbers of the form $NXX\text{-}XXXX$. How many area codes are needed to ensure everyone has a number?
- Objects: $N = 25{,}000{,}000$ telephones.
- Boxes: $k = 8{,}000{,}000$ numbers.
- By the generalized pigeonhole principle:

$$
\left\lceil \frac{25{,}000{,}000}{8{,}000{,}000} \right\rceil = \lceil 3.125 \rceil = 4
$$

At least 4 telephones must share a local number, so at least 4 area codes are required.

### Example 4: A Multiple Made Entirely of 0s and 1s
Show that for every positive integer $n$, there exists a multiple of $n$ whose decimal representation contains only the digits 0 and 1.
- Consider the $n + 1$ integers formed by repeated ones: $1, 11, 111, \dots, \underbrace{11\dots1}_{n+1 \text{ ones}}$.
- When divided by $n$, there are only $n$ possible remainders: $\{0, 1, 2, \dots, n - 1\}$.
- By the pigeonhole principle, among these $n + 1$ numbers, at least two must have the identical remainder modulo $n$.
- Subtracting the smaller from the larger cancels the ones in the lower positions, resulting in a number of the form $11\dots100\dots0$ that is divisible by $n$.

---

## 💻 Connecting to Computer Engineering

1. **Hash Table Bucket Collisions:**
   When a hash table stores $n$ keys in $m$ buckets, the pigeonhole principle dictates that if $n > m$, at least one bucket must hold multiple keys. The generalized principle guarantees that at least one bucket holds $\lceil n/m \rceil$ keys. This is why engineers maintain the load factor $\alpha = n / m$ below 1.0 (typically $\alpha \approx 0.75$).

2. **Network Router Buffers:**
   A router queue with memory for $m$ packets that receives a burst of $n > m$ packets must either drop packets or route them to overflow storage. The guaranteed worst-case queue depth is at least $\lceil n/m \rceil$.

3. **Lossless Data Compression:**
   No lossless compression algorithm can compress all bit strings of length $n$ to strings of length $< n$. By the pigeonhole principle, there are $2^n$ strings of length $n$, but only $\sum_{i=0}^{n-1} 2^i = 2^n - 1$ shorter strings. Attempting to compress all files would force two different original files to map to the same compressed file, making decompression impossible.

---

## 🏆 Past Exam Questions

### 2022 Q.8(c) & 2024 Q.8(c): Real-World Example of Generalized Pigeonhole Principle [02 Marks]

> **The Question:** Give a real-world example of generalized pigeonhole principle.

**Let's solve this step by step like a tutor:**

First, state the principle clearly so the examiner knows you understand the mathematics.
If $N$ objects are placed into $k$ boxes and $N > k$, then at least one box holds at least two objects. The **generalized** form states that if $N > mk$, then some box holds at least $m + 1$ objects (or equivalently, at least $\lceil N/k \rceil$ objects).

Next, provide concrete, real-world examples:

1. **Birth Months in a Class:**
   There are $k = 12$ calendar months. In a class of $N = 25$ students, at least 3 students must share a birth month, because $25 > 2 \times 12 = 24$. Taking $m = 2$ and $k = 12$ requires $N > 24$, so 25 students guarantees a triple.

2. **Socks from a Drawer:**
   A drawer holds only black and white socks ($k = 2$ colors). Drawing $N = 5$ socks guarantees at least 3 of the same color, since $5 > 2 \times 2 = 4$.

3. **Hash Tables in Software:**
   Storing $n$ keys across $m$ memory buckets forces a collision whenever $n > m$. In general, some bucket holds at least $\lceil n/m \rceil$ keys, which governs hash table design.

4. **Server Distribution in Data Centers:**
   A cluster with $r$ server racks holding $2r + 1$ machines must place at least 3 machines in one rack, because $2r + 1 > 2 \times r$.

$$
\boxed{\text{More than } mk \text{ objects in } k \text{ boxes forces some box to hold } m+1}
$$

> [!WARNING] The Threshold Difference
> The plain principle uses $m = 1$. The generalized principle requires $N > mk$, which is a stronger condition on $N$ and yields the stronger conclusion of $m + 1$ objects in a box. Using $N > k$ when looking for 3 matching birth months would only prove a pair, not a triple.

---

### 2022 Q.8(d): Congruence Modulo $d$ Among $d + 1$ Integers [02 Marks]

> **The Question:** Let $d$ be a positive integer. Show that among any group of $d+1$ (not necessarily consecutive) integers there are two with exactly the same remainder when they are divided by $d$.

**Let's solve this step by step like a tutor:**

This is a classic proof that translates directly into the pigeonhole framework in four clear steps:

**Step 1: Count the possible remainders.**
For any integer $a$, the division algorithm states that:

$$
a = qd + r, \qquad 0 \le r < d
$$

Every integer divided by $d$ leaves exactly one remainder from the set $\{0, 1, 2, \dots, d - 1\}$.
Therefore, there are exactly **$d$ possible remainders**.

**Step 2: Identify the boxes and objects.**
- **Objects ($d + 1$ items):** The given $d + 1$ arbitrary integers.
- **Boxes ($d$ containers):** Label each box with one of the $d$ possible remainders: Box $0$, Box $1$, ..., Box $d - 1$.
Place each integer into the box corresponding to its remainder upon division by $d$.

**Step 3: Apply the pigeonhole principle.**
There are $d + 1$ integers distributed into $d$ boxes.
Since $d + 1 > d$, by the pigeonhole principle, at least one box must contain two or more integers.

**Step 4: Conclude the congruence.**
Let $a_1$ and $a_2$ be two integers that share the same box. Because they share a box, they have the identical remainder $r$.
Writing $a_1 = q_1 d + r$ and $a_2 = q_2 d + r$, subtract the two equations:

$$
a_1 - a_2 = (q_1 - q_2)d
$$

This shows that $d$ divides $a_1 - a_2$, which means $a_1 \equiv a_2 \pmod d$.
Thus, any group of $d + 1$ integers must contain two integers with the exact same remainder when divided by $d$.

$$
\boxed{\text{Any } d+1 \text{ integers include two congruent modulo } d}
$$

> [!NOTE] Sharpness of the Bound
> The bound $d + 1$ is sharp. If you choose only $d$ integers, you could pick $0, 1, 2, \dots, d - 1$, where every remainder is distinct and zero collisions occur. Exactly $d + 1$ integers are required to mathematically force a collision.

---

### 2023 Q.8(a): Pigeonhole Principle Description and Example [02 Marks]

> **The Question:** Briefly describe the pigeonhole principle with a real world example.

**Let's solve this step by step like a tutor:**

**The Principle:**
If $N$ objects are placed into $k$ boxes and $N > k$, then at least one box must hold at least two objects.

**Proof by Contradiction:**
Suppose every box held at most one object. Then the total number of objects in all $k$ boxes could not exceed $k \times 1 = k$. But we are given that $N > k$, which is a contradiction. Therefore, at least one box holds two or more objects.

**Real-World Examples:**
1. **Drawer of Socks:** A drawer contains only black and white socks. If you reach in and pull out 3 socks in the dark, you are guaranteed to have at least one matching pair (2 socks of the same color), because 3 socks distributed into 2 color categories forces $\ge 2$ in one category.
2. **Birthdays:** With 366 possible calendar birthdays (including February 29), a gathering of 367 people is guaranteed to contain at least two people who share a birthday.
3. **Office Floors:** If 11 employees work in a building with 10 floors, at least two employees must have offices on the same floor.
4. **Hash Tables:** When storing $n$ data records in a hash table with $m$ buckets where $n > m$, at least one bucket must hold two or more records, causing a hash collision.

$$
\boxed{\text{More objects than boxes forces at least one box to hold two or more}}
$$

---

## 📋 Exam Variants at a Glance

| Year | Question | Subtopic Focus | Marks | Boxed Result |
|:---|:---|:---|:---:|:---|
| **2022 Q.8(c)** | Real-world example of generalized pigeonhole principle | Generalized form ($N > mk$) | 02 | $\boxed{\text{More than } mk \text{ objects in } k \text{ boxes forces some box to hold } m+1}$ |
| **2024 Q.8(c)** | Real-world example of generalized pigeonhole principle | Verbatim repeat of 2022 Q.8(c) | 02 | $\boxed{\text{More than } mk \text{ objects in } k \text{ boxes forces some box to hold } m+1}$ |
| **2022 Q.8(d)** | $d+1$ integers share a remainder modulo $d$ | 4-step pigeonhole proof on congruences | 02 | $\boxed{\text{Any } d+1 \text{ integers include two congruent modulo } d}$ |
| **2023 Q.8(a)** | Describe pigeonhole principle with real-world example | Plain form ($N > k$) and proof | 02 | $\boxed{\text{More objects than boxes forces at least one box to hold two or more}}$ |

---

## ⚡ Quick Review

**The method in one sentence:** Map the given items to objects and the available categories to boxes; if items exceed boxes, a collision is guaranteed.

**The threshold formula you must memorize:**
$$
N_{\min} = k(r - 1) + 1 \quad \text{guarantees at least } r \text{ objects in one of the } k \text{ boxes}
$$

**The most common exam mistake:** Citing the 23-person birthday paradox as a pigeonhole example. The pigeonhole principle requires 367 people for a guaranteed shared birthday; 23 is a probability threshold.

**Time estimate in exam:** 3 to 4 minutes for a 2-mark question.

---

## 🔗 Connected Topics

- [← Previous: DM-6.2 Inclusion-Exclusion](DM-6.2_Inclusion_Exclusion.md): Counting overlapping set unions.
- [→ Next: DM-6.4 Permutations](DM-6.4_Permutations.md): Moving from existence guarantees back to ordered counting.
- [DM-5.4: Modular Arithmetic and Congruence](../DM-5_Number_Theory/DM-5.4_Modular_Arithmetic.md): Supplies the modulo residue classes for the 2022 Q.8(d) proof.
- [DM-7.1: Algorithms and Complexity](../DM-7_Supplementary/DM-7.1_Algorithms_and_Complexity.md): Connects pigeonhole guarantees to hash table collision limits and sorting tree depths.

---

[← Previous: DM-6.2 Inclusion-Exclusion](DM-6.2_Inclusion_Exclusion.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: DM-6.4 Permutations →](DM-6.4_Permutations.md)
