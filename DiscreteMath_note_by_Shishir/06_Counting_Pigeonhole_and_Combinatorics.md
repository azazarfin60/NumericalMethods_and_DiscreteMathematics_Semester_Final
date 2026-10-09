---
title: "06. Counting, Pigeonhole Principle and Combinatorics"
course: "ECE 2213 — Discrete Mathematics"
batch: "6 (Curriculum Completion Module)"
source: "ECE 2213 Course Syllabus & Exam Standards"
tags:
  - discrete-mathematics
  - counting
  - pigeonhole-principle
  - permutations
  - combinations
  - combinatorics
---

# ECE 2213: Counting, Pigeonhole Principle & Combinatorics (Module 6)

**Course**: ECE 2213 — Discrete Mathematics  
**Module**: 6 of 6 (Curriculum Completion Module: Syllabus Section 2.6)  
**Topics Covered**: Basic Counting Rules (Product Rule, Sum Rule); Principle of Inclusion-Exclusion (General $n$-set Formulation, Derangements); The Pigeonhole Principle (Standard Form, Generalized Form $\lceil N/k \rceil$, Dirichlet's Box Argument, Classical Number-Theoretic and Geometric Proofs); Permutations ($n!$, Partial Permutations $P(n, r)$, Circular Permutations $(n-1)!$, Permutations with Indistinguishable Objects); Combinations ($C(n, r) = \binom{n}{r}$, Algebraic Proofs, Pascal's Identity, The Binomial Theorem); Combinations with Repetition (Stars and Bars Theorem); Comprehensive Exam-Style Worked Problems.

**Navigation**: [[00_Discrete_Mathematics_Index|📋 Master Study Index]] | [[05_Induction_II_and_Number_Theory|⬅ Previous: Batch 5 (Pages 80–95)]]

---

## 1. Fundamental Rules of Counting

Combinatorics is the branch of discrete mathematics concerned with counting, arrangement, and structural configurations of finite sets. Two primary axiomatic rules underpin all counting techniques:

### 1.1 The Product Rule (Rule of Sequential Operations)
If a procedure can be broken down into a sequence of two consecutive tasks, such that the first task can be performed in $n_1$ distinct ways, and for each of these ways, the second task can be performed in $n_2$ distinct ways, then the entire procedure can be carried out in:
$$
n_1 \times n_2 \quad \text{ways}
$$

#### Extended Product Rule:
For a sequence of $k$ consecutive operations with $n_1, n_2, \dots, n_k$ choices respectively:
$$
\text{Total Outcomes} = \prod_{i=1}^k n_i = n_1 \times n_2 \times \dots \times n_k
$$

> [!tip] Practical Identification Rule
> Use the **Product Rule** whenever all component tasks must occur together or sequentially (logical **AND** relationship).

---

### 1.2 The Sum Rule (Rule of Disjoint Alternatives)
If a task can be performed either in one of $n_1$ ways or in one of $n_2$ ways, where none of the set of $n_1$ ways is identical to any of the set of $n_2$ ways (the two sets of choices are mutually exclusive / disjoint), then the task can be done in:
$$
n_1 + n_2 \quad \text{ways}
$$

#### Extended Sum Rule:
For $k$ mutually disjoint tasks $A_1, A_2, \dots, A_k$ where $A_i \cap A_j = \emptyset$ for $i \neq j$:
$$
\left| \bigcup_{i=1}^k A_i \right| = \sum_{i=1}^k |A_i| = n_1 + n_2 + \dots + n_k
$$

> [!tip] Practical Identification Rule
> Use the **Sum Rule** when you choose between non-overlapping mutually exclusive alternative options (logical **OR** relationship).

---

### 1.3 Worked Example: Computer Network Port & Password Addressing

**Problem Statement**:  
A university network requires student login passwords satisfying these criteria:
1. The password length is exactly 6 characters.
2. The first character must be an uppercase English letter ($A$ through $Z$).
3. The remaining 5 characters can be any lowercase letter ($a$ through $z$) or any decimal digit ($0$ through $9$).
4. No repetition of characters is permitted within the password.

Determine the total number of valid passwords possible.

#### Step-by-Step Solution for Network Password Problem:
1. **Position 1 (First Character)**:
   Must be an uppercase letter:
   $$
   n_1 = 26 \text{ choices}
   $$
2. **Positions 2 through 6 (Remaining 5 Characters)**:
   Available alphabet pool: $26 \text{ (lowercase)} + 10 \text{ (digits)} = 36 \text{ symbols}$.
   Since repetition is strictly prohibited and 1 character from lowercase/digits pool has not been used yet (the first was uppercase):
   - Position 2: $36$ choices
   - Position 3: $35$ choices
   - Position 4: $34$ choices
   - Position 5: $33$ choices
   - Position 6: $32$ choices

3. **By the Product Rule**:
   $$
   \text{Total Passwords} = 26 \times 36 \times 35 \times 34 \times 33 \times 32
   $$
   $$
   \text{Total Passwords} = 26 \times 45{,}239{,}040 = 1{,}176{,}215{,}040
   $$

$$\therefore \mathbf{\text{Total valid passwords} = 1{,}176{,}215{,}040}$$

---

## 2. The Principle of Inclusion-Exclusion (PIE)

When subsets are **not disjoint**, applying the sum rule directly overcounts elements that belong to multiple sets. The Principle of Inclusion-Exclusion systematically corrects for multiple counting.

### 2.1 Two-Set and Three-Set Formulation

#### Two Sets:
$$
|A \cup B| = |A| + |B| - |A \cap B|
$$

#### Three Sets:
$$
|A \cup B \cup C| = |A| + |B| + |C| - \big(|A \cap B| + |B \cap C| + |C \cap A|\big) + |A \cap B \cap C|
$$

---

### 2.2 General $n$-Set Inclusion-Exclusion Formulation
For any collection of $n$ finite sets $A_1, A_2, \dots, A_n$:
$$
\left| \bigcup_{i=1}^n A_i \right| = \sum_{1 \le i \le n} |A_i| - \sum_{1 \le i < j \le n} |A_i \cap A_j| + \sum_{1 \le i < j < k \le n} |A_i \cap A_j \cap A_k| - \dots + (-1)^{n-1} |A_1 \cap A_2 \cap \dots \cap A_n|
$$

In compact sigma notation:
$$
\left| \bigcup_{i=1}^n A_i \right| = \sum_{k=1}^n (-1)^{k-1} \sum_{1 \le i_1 < i_2 < \dots < i_k \le n} \left| A_{i_1} \cap A_{i_2} \cap \dots \cap A_{i_k} \right|
$$

---

### 2.3 Classical Application: Counting Integers Divisible by Moduli

**Problem Statement**:  
Find the number of integers between $1$ and $1000$ (inclusive) that are divisible by $3$, $5$, or $7$.

#### Step-by-Step Solution for Divisibility Counting:
Let the universal set be $U = \{1, 2, 3, \dots, 1000\}$, so $|U| = 1000$.  
Define the subset divisibility events:
- $A$: Integers divisible by $3 \implies |A| = \lfloor 1000 / 3 \rfloor = 333$
- $B$: Integers divisible by $5 \implies |B| = \lfloor 1000 / 5 \rfloor = 200$
- $C$: Integers divisible by $7 \implies |C| = \lfloor 1000 / 7 \rfloor = 142$

Now compute the pairwise intersections ($\operatorname{lcm}$ of coprime pairs):
- $|A \cap B| = \lfloor 1000 / \operatorname{lcm}(3, 5) \rfloor = \lfloor 1000 / 15 \rfloor = 66$
- $|B \cap C| = \lfloor 1000 / \operatorname{lcm}(5, 7) \rfloor = \lfloor 1000 / 35 \rfloor = 28$
- $|C \cap A| = \lfloor 1000 / \operatorname{lcm}(7, 3) \rfloor = \lfloor 1000 / 21 \rfloor = 47$

Compute the triple intersection:
- $|A \cap B \cap C| = \lfloor 1000 / \operatorname{lcm}(3, 5, 7) \rfloor = \lfloor 1000 / 105 \rfloor = 9$

Apply the Principle of Inclusion-Exclusion:
$$
\begin{aligned}
|A \cup B \cup C| &= (|A| + |B| + |C|) - (|A \cap B| + |B \cap C| + |C \cap A|) + |A \cap B \cap C| \\
&= (333 + 200 + 142) - (66 + 28 + 47) + 9 \\
&= 675 - 141 + 9 \\
&= \mathbf{543}
\end{aligned}
$$

$$\therefore \mathbf{543 \text{ integers between } 1 \text{ and } 1000 \text{ are divisible by } 3, 5, \text{ or } 7.}$$

---

### 2.4 Derangements (Permutations with No Fixed Points)
A **derangement** is a permutation of elements such that no element appears in its original position.
By PIE, the number of derangements of $n$ elements, denoted $D_n$ or $!n$, is:
$$
D_n = n! \sum_{k=0}^n \frac{(-1)^k}{k!} = n! \left( 1 - \frac{1}{1!} + \frac{1}{2!} - \frac{1}{3!} + \dots + \frac{(-1)^n}{n!} \right)
$$
As $n \to \infty$, $\frac{D_n}{n!} \approx \frac{1}{e} \approx 0.3679$.

---

## 3. The Pigeonhole Principle (Dirichlet's Box Principle)

The **Pigeonhole Principle** is one of the most powerful and fundamental non-constructive proof tools in discrete mathematics.

```text
               THE PIGEONHOLE PRINCIPLE
       k+1 or more pigeons       k pigeonholes
       ┌───┐ ┌───┐ ┌───┐ ┌───┐        ┌───┐ ┌───┐ ┌───┐
       │ • │ │ • │ │ • │ │ • │ ───►   │•• │ │ • │ │   │
       └───┘ └───┘ └───┘ └───┘        └───┘ └───┘ └───┘
                                  At least one hole holds >= 2
```

### 3.1 Basic Statement of the Principle
> [!important] Theorem: Standard Pigeonhole Principle
> If $k$ is a positive integer and $k + 1$ or more objects (pigeons) are placed into $k$ boxes (pigeonholes), then **at least one box must contain two or more objects**.

#### Formal Proof by Contradiction:
Assume the contrary: suppose no box contains two or more objects.  
Then every box contains at most $1$ object.  
Since there are $k$ boxes, the total number of objects across all boxes cannot exceed:
$$
\sum_{i=1}^k 1 = k
$$
However, we have $k + 1$ or more objects. This contradicts the given condition.  
Therefore, at least one box must contain two or more objects. $\blacksquare$

---

### 3.2 The Generalized Pigeonhole Principle
> [!important] Theorem: Generalized Pigeonhole Principle
> If $N$ objects are placed into $k$ boxes, then **at least one box contains at least**:
> $$
> \left\lceil \frac{N}{k} \right\rceil \quad \text{objects}
> $$
> where $\lceil x \rceil$ is the ceiling function (the smallest integer greater than or equal to $x$).

#### Formal Proof:
Suppose to the contrary that every box contains fewer than $\lceil N/k \rceil$ objects.  
Then every box contains at most $\lceil N/k \rceil - 1$ objects.  
The total number of objects in all $k$ boxes would satisfy:
$$
\text{Total Objects} \le k \left( \left\lceil \frac{N}{k} \right\rceil - 1 \right) < k \left( \left(\frac{N}{k} + 1\right) - 1 \right) = k \cdot \frac{N}{k} = N
$$
This is a direct contradiction because there are $N$ total objects.  
Therefore, at least one box must contain at least $\lceil N/k \rceil$ objects. $\blacksquare$

---

### 3.3 Classic Exam Problems on Pigeonhole Principle

#### Problem 1: Minimum Class Size for Matching Grades
**Question**:  
In an ECE 2213 class, letter grades can be $A, B, C, D,$ or $F$ (5 possible grades). What is the minimum number of students needed to guarantee that at least 6 students receive the exact same grade?

**Solution**:  
- Pigeons ($N$): Number of students (unknown).
- Pigeonholes ($k$): Number of possible letter grades $\implies k = 5$.
- Desired minimum in at least one box: $\lceil N/k \rceil = 6$.

By the Generalized Pigeonhole Principle:
$$
\left\lceil \frac{N}{5} \right\rceil = 6
$$
The minimum integer $N$ satisfying $\lceil N/5 \rceil \ge 6$ is obtained when:
$$
\frac{N - 1}{5} = 5 \implies N - 1 = 25 \implies N = 26
$$
- If there were only 25 students, by the worst-case distribution, exactly $5 \times 5 = 25$ students could each receive 5 of each grade (no grade has 6).
- Adding the 26th student forces at least one grade to be assigned to $5 + 1 = 6$ students.

$$\therefore \mathbf{\text{Minimum number of students required} = 26}$$

---

#### Problem 2: Birthday Paradox in a Hall
**Question**:  
How many people must be in a room to guarantee that at least two of them share the same birth month?

**Solution**:
- Pigeons: $N$ people.
- Pigeonholes: $k = 12$ months of the year.
- By the standard Pigeonhole Principle: To guarantee at least one box has $\ge 2$ people, we need:
  $$
  N = k + 1 = 12 + 1 = \mathbf{13} \text{ people}
  $$

---

#### Problem 3: Subset Sum Property
**Question**:  
Let $S$ be any set of 10 integers chosen from $\{1, 2, 3, \dots, 100\}$. Prove that there exist two disjoint non-empty subsets of $S$ whose elements have the exact same sum.

**Solution**:
1. **Pigeons**: The total number of non-empty subsets of $S$.
   Since $|S| = 10$, the total number of non-empty subsets is:
   $$
   2^{10} - 1 = 1024 - 1 = 1023 \text{ subsets}
   $$
2. **Pigeonholes**: The possible sums of subsets.
   - The minimum possible sum is $1$.
   - The maximum possible sum occurs if $S$ contained the 10 largest integers:
     $$
     91 + 92 + 93 + 94 + 95 + 96 + 97 + 98 + 99 + 100 = 955
     $$
   - Thus, any subset sum must lie in the discrete integer range $[1, 955]$.
   - The number of possible distinct sums (pigeonholes) is at most $955$.
3. **Application**:
   We have $1023$ subsets (pigeons) distributed among at most $955$ possible sums (pigeonholes).
   Since $1023 > 955$, by the Pigeonhole Principle, **at least two distinct subsets $A$ and $B$ must have the exact same sum**:
   $$
   \sum_{x \in A} x = \sum_{y \in B} y
   $$
4. **Disjointness**:
   If $A$ and $B$ share elements ($A \cap B \neq \emptyset$), subtract the common elements from both sets:
   $$
   A' = A - (A \cap B), \quad B' = B - (A \cap B)
   $$
   $A'$ and $B'$ are non-empty, disjoint, and still have identical sums. $\blacksquare$

---

## 4. Permutations

A **permutation** of a set of distinct objects is an **ordered arrangement** of these objects.

```text
            PERMUTATIONS (ORDER MATTERS)
   Objects: {A, B, C}
   Arrangements of length 2:
   (A, B)  !=  (B, A)   <-- Distinct permutations!
   (A, C)  !=  (C, A)
   (B, C)  !=  (C, B)   Total: P(3, 2) = 6
```

### 4.1 Permutations of $n$ Distinct Elements
The number of ways to arrange all $n$ distinct elements in a linear sequence is:
$$
n! = n \times (n-1) \times (n-2) \times \dots \times 2 \times 1
$$
By convention, $0! = 1$.

---

### 4.2 $r$-Permutations ($P(n, r)$)
An **$r$-permutation** is an ordered arrangement of $r$ elements selected from a set of $n$ distinct elements.
$$
P(n, r) = n(n-1)(n-2)\dots(n-r+1) = \frac{n!}{(n-r)!}
$$
where $0 \le r \le n$.

#### Special Cases:
- $P(n, 0) = \frac{n!}{n!} = 1$
- $P(n, 1) = \frac{n!}{(n-1)!} = n$
- $P(n, n) = \frac{n!}{0!} = n!$

---

### 4.3 Circular Permutations
When $n$ distinct objects are arranged around a **closed circle**, shifting all elements circularly by one position does not create a new relative ordering:
$$
P_{\text{circular}} = \frac{n!}{n} = (n - 1)!
$$

#### Key Variations:
1. **Clockwise vs. Counter-Clockwise Distinguished** (e.g., people around a dining table):
   $$
   \text{Ways} = (n - 1)!
   $$
2. **Clockwise vs. Counter-Clockwise Indistinguishable** (e.g., beads on a necklace or keys on a ring, which can be flipped over):
   $$
   \text{Ways} = \frac{(n - 1)!}{2}
   $$

---

### 4.4 Permutations with Indistinguishable Objects (Multinomial Coefficients)
If a collection of $n$ objects contains:
- $n_1$ identical objects of type 1
- $n_2$ identical objects of type 2
- $\dots$
- $n_k$ identical objects of type $k$

such that $n_1 + n_2 + \dots + n_k = n$, then the number of distinct linear permutations is given by the **multinomial coefficient**:
$$
\frac{n!}{n_1! \, n_2! \, \dots \, n_k!}
$$

#### Classic Example: Arranging Letters in "MISSISSIPPI"
- Total letters: $n = 11$
- Frequencies: $M: 1, \quad I: 4, \quad S: 4, \quad P: 2$
- Distinct linear arrangements:
  $$
  \frac{11!}{1! \times 4! \times 4! \times 2!} = \frac{39{,}916{,}800}{1 \times 24 \times 24 \times 2} = \mathbf{34{,}650} \text{ arrangements}
  $$

---

## 5. Combinations

A **combination** is an **unordered selection** of $r$ elements from a set of $n$ distinct elements. Order does not matter.

```text
            COMBINATIONS (ORDER DOES NOT MATTER)
   Objects: {A, B, C}
   Selections of size 2:
   {A, B}  ==  {B, A}   <-- Same combination!
   {A, C}  ==  {C, A}
   {B, C}  ==  {C, B}   Total: C(3, 2) = 3
```

### 5.1 $r$-Combinations ($C(n, r)$ or $\binom{n}{r}$)
The number of ways to choose $r$ elements from $n$ distinct elements without regard to order is:
$$
C(n, r) = \binom{n}{r} = \frac{P(n, r)}{r!} = \frac{n!}{r!(n - r)!}
$$
where $0 \le r \le n$.

#### Fundamental Symmetry Identity:
$$
\binom{n}{r} = \binom{n}{n - r}
$$
*Intuition*: Choosing $r$ elements to include is equivalent to choosing $(n - r)$ elements to leave behind.

---

### 5.2 Pascal's Identity & Triangle
> [!important] Theorem: Pascal's Identity
> For all positive integers $n$ and $r$ with $1 \le r \le n$:
> $$
> \binom{n + 1}{r} = \binom{n}{r - 1} + \binom{n}{r}
> $$

#### Algebraic Proof:
Expand the right-hand side using factorial definitions:
$$
\begin{aligned}
\binom{n}{r - 1} + \binom{n}{r} &= \frac{n!}{(r - 1)!(n - (r - 1))!} + \frac{n!}{r!(n - r)!} \\
&= \frac{n!}{(r - 1)!(n - r + 1)!} + \frac{n!}{r!(n - r)!}
\end{aligned}
$$
Find a common denominator, noting $r! = r(r - 1)!$ and $(n - r + 1)! = (n - r + 1)(n - r)!$:
$$
\begin{aligned}
&= \frac{n! \cdot r}{r!(n - r + 1)!} + \frac{n! \cdot (n - r + 1)}{r!(n - r + 1)!} \\
&= \frac{n! \big[ r + (n - r + 1) \big]}{r!(n - r + 1)!} \\
&= \frac{n! (n + 1)}{r!(n + 1 - r)!} \\
&= \frac{(n + 1)!}{r!(n + 1 - r)!} = \binom{n + 1}{r} \quad \blacksquare
\end{aligned}
$$

---

### 5.3 The Binomial Theorem
For any real numbers $x, y$ and non-negative integer $n$:
$$
(x + y)^n = \sum_{k=0}^n \binom{n}{k} x^{n - k} y^k = \binom{n}{0} x^n + \binom{n}{1} x^{n-1} y + \dots + \binom{n}{n} y^n
$$

#### Key Corollary Identities:
1. Setting $x = 1, y = 1$:
   $$
   \sum_{k=0}^n \binom{n}{k} = \binom{n}{0} + \binom{n}{1} + \dots + \binom{n}{n} = 2^n
   $$
   *(The total number of subsets of an $n$-element set equals the cardinality of its power set $|P(S)| = 2^n$).*

2. Setting $x = 1, y = -1$:
   $$
   \sum_{k=0}^n (-1)^k \binom{n}{k} = \binom{n}{0} - \binom{n}{1} + \binom{n}{2} - \dots + (-1)^n \binom{n}{n} = 0
   $$
   $$\implies \binom{n}{0} + \binom{n}{2} + \binom{n}{4} + \dots = \binom{n}{1} + \binom{n}{3} + \binom{n}{5} + \dots = 2^{n - 1}$$

---

### 5.4 Combinations with Repetition (Stars and Bars Theorem)
The number of ways to select $r$ elements from a set of $n$ distinct types of items when **repetition is allowed** (unlimited supply of each type) is:
$$
\binom{n + r - 1}{r} = \binom{n + r - 1}{n - 1}
$$

#### Equivalence to Integer Equations:
This is identical to finding the number of **non-negative integer solutions** to the linear equation:
$$
x_1 + x_2 + \dots + x_n = r \quad (x_i \ge 0, \; x_i \in \mathbb{Z})
$$

#### Visualization via "Stars and Bars":
- Represent $r$ identical items as $r$ stars ($\star$).
- Partition the stars into $n$ bins using $n - 1$ dividers/bars ($|$).
- The total number of positions is $r + (n - 1) = n + r - 1$.
- Choosing which $r$ positions hold stars yields:
  $$
  \binom{n + r - 1}{r}
  $$

---

## 6. Comprehensive Summary Table: Counting Paradigms

| Selection Type | Order Matters? (Sequence) | Repetition Allowed? | Formula |
| :--- | :---: | :---: | :---: |
| **$r$-Permutation** | **Yes** | **No** | $P(n, r) = \frac{n!}{(n - r)!}$ |
| **Permutation with Repetition** | **Yes** | **Yes** | $n^r$ |
| **$r$-Combination** | **No** | **No** | $C(n, r) = \binom{n}{r} = \frac{n!}{r!(n - r)!}$ |
| **Combination with Repetition** | **No** | **Yes** | $\binom{n + r - 1}{r} = \frac{(n + r - 1)!}{r!(n - 1)!}$ |

---

## 7. Master Exam Problem Solutions

### 7.1 Problem 1: Committee Selection with Gender Restrictions
**Question**:  
A department committee of 5 members is to be formed from a group of 7 male professors and 6 female professors. In how many ways can the committee be formed if:
1. There are no restrictions?
2. The committee must contain at least 3 female professors?
3. Professor A and Professor B refuse to serve together?

#### Solution for Committee Selection Problem:
- **Part (a): No Restrictions**:
  Total pool of professors: $7 + 6 = 13$. Choose 5:
  $$
  \binom{13}{5} = \frac{13 \times 12 \times 11 \times 10 \times 9}{5 \times 4 \times 3 \times 2 \times 1} = \mathbf{1287} \text{ ways}
  $$

- **Part (b): At Least 3 Female Professors**:
  Break down into mutually exclusive cases:
  1. Exactly 3 females and 2 males:
     $$
     \binom{6}{3} \times \binom{7}{2} = 20 \times 21 = 420
     $$
  2. Exactly 4 females and 1 male:
     $$
     \binom{6}{4} \times \binom{7}{1} = 15 \times 7 = 105
     $$
  3. Exactly 5 females and 0 males:
     $$
     \binom{6}{5} \times \binom{7}{0} = 6 \times 1 = 6
     $$
  By the Sum Rule:
  $$
  \text{Total Ways} = 420 + 105 + 6 = \mathbf{531} \text{ ways}
  $$

- **Part (c): Professor A and B Refuse to Serve Together**:
  Use complementary counting:
  $$
  \text{Permitted} = \text{Total Committees} - \text{Committees containing BOTH A and B}
  $$
  If both A and B are on the committee, we must choose the remaining $5 - 2 = 3$ members from the remaining $13 - 2 = 11$ candidates:
  $$
  \binom{11}{3} = \frac{11 \times 10 \times 9}{3 \times 2 \times 1} = 165
  $$
  $$
  \text{Permitted Committees} = 1287 - 165 = \mathbf{1122} \text{ ways}
  $$

---

### 7.2 Problem 2: Non-negative vs. Strictly Positive Integer Solutions
**Question**:  
Find the number of solutions to the equation:
$$
x_1 + x_2 + x_3 + x_4 = 17
$$
such that:
1. $x_1, x_2, x_3, x_4 \ge 0$ (non-negative integers).
2. $x_1, x_2, x_3, x_4 \ge 1$ (strictly positive integers).

#### Solution for Integer Equation Problem:
- **Part (a): Non-negative Solutions ($x_i \ge 0$)**:
  Here $n = 4$ variables, $r = 17$ sum.
  By Stars and Bars:
  $$
  \binom{n + r - 1}{r} = \binom{4 + 17 - 1}{17} = \binom{20}{17} = \binom{20}{3}
  $$
  $$
  \binom{20}{3} = \frac{20 \times 19 \times 18}{3 \times 2 \times 1} = \mathbf{1140} \text{ solutions}
  $$

- **Part (b): Strictly Positive Solutions ($x_i \ge 1$)**:
  Substitute $y_i = x_i - 1$, so $y_i \ge 0$.
  $$
  (y_1 + 1) + (y_2 + 1) + (y_3 + 1) + (y_4 + 1) = 17
  $$
  $$
  y_1 + y_2 + y_3 + y_4 = 17 - 4 = 13 \quad (y_i \ge 0)
  $$
  Now apply Stars and Bars with $n = 4$ and $r' = 13$:
  $$
  \binom{4 + 13 - 1}{13} = \binom{16}{13} = \binom{16}{3}
  $$
  $$
  \binom{16}{3} = \frac{16 \times 15 \times 14}{3 \times 2 \times 1} = \mathbf{560} \text{ solutions}
  $$

---

### 7.3 Problem 3: Pigeonhole Proof on Grid Distances
**Question**:  
Given an equilateral triangle with side length $1$ unit. If $5$ points are chosen anywhere inside or on the boundary of the triangle, prove that there exist at least two points whose distance apart is at most $0.5$ units.

#### Solution for Equilateral Triangle Grid Proof:
1. Divide the equilateral triangle into $4$ smaller congruent equilateral triangles by connecting the midpoints of its three sides.
2. The side length of each of the 4 small triangles is:
   $$
   \frac{1}{2} = 0.5 \text{ units}
   $$
3. Maximum distance between any two points lying within or on the boundary of a small triangle of side length $0.5$ is its side length:
   $$
   d_{\max} \le 0.5 \text{ units}
   $$
4. Treat the $4$ small triangles as **pigeonholes** ($k = 4$) and the $5$ chosen points as **pigeons** ($N = 5$).
5. Since $N = 5 > 4 = k$, by the Pigeonhole Principle, **at least one small triangle must contain at least 2 points**:
   $$
   \left\lceil \frac{5}{4} \right\rceil = 2 \text{ points}
   $$
6. Since both points reside within the same small triangle, the Euclidean distance between them cannot exceed the diameter of the small triangle:
   $$
   \text{Distance}(P_1, P_2) \le 0.5 \text{ units} \quad \blacksquare
   $$

---

## 8. Summary of Module 6 Key Equations

- **Product Rule**: $\text{Outcomes} = \prod n_i$
- **Sum Rule (Disjoint)**: $\text{Outcomes} = \sum n_i$
- **Principle of Inclusion-Exclusion**: $|A \cup B| = |A| + |B| - |A \cap B|$
- **Pigeonhole Principle (Generalized)**: At least one box contains $\ge \lceil N/k \rceil$ objects
- **Linear Permutations**: $P(n, r) = \frac{n!}{(n - r)!}$
- **Circular Permutations**: $(n - 1)!$
- **Multiset Permutations**: $\frac{n!}{n_1! n_2! \dots n_k!}$
- **Combinations**: $C(n, r) = \binom{n}{r} = \frac{n!}{r!(n - r)!}$
- **Pascal's Identity**: $\binom{n+1}{r} = \binom{n}{r-1} + \binom{n}{r}$
- **Binomial Theorem**: $(x + y)^n = \sum_{k=0}^n \binom{n}{k} x^{n-k} y^k$
- **Combinations with Repetition**: $\binom{n + r - 1}{r}$

---

**Navigation**: [[00_Discrete_Mathematics_Index|📋 Master Study Index]] | [[05_Induction_II_and_Number_Theory|⬅ Previous: Batch 5 (Pages 80–95)]]
