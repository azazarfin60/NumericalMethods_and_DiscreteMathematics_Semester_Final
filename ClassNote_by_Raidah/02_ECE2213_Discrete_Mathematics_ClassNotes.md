---
course: ECE 2213 - Discrete Mathematics & Numerical Methods
part: 2
title: Discrete Mathematics Class Notes
student: Raidah (Roll 2310035)
instructor: Nadim Sir
textbook: Discrete Mathematics and Its Applications (Kenneth H. Rosen, 7th/8th Edition)
pages: 19-40
tags:
  - discrete-mathematics
  - set-theory
  - propositional-logic
  - predicate-logic
  - rules-of-inference
  - number-theory
  - modular-arithmetic
  - chinese-remainder-theorem
  - combinatorics
  - pigeonhole-principle
  - methods-of-proof
---

# ECE 2213: Discrete Mathematics — Class Notes

**Source**: Handwritten notebook of Raidah (Roll: 2310035)  
**Instructor**: Nadim Sir  
**Textbook**: *Discrete Mathematics and Its Applications* by Kenneth H. Rosen  
**Scope**: PDF Pages 19 to 40  

> [!INFO] Document Mapping & Structure
> - **Source PDF**: Pages 19–40 of `Numerical & Discrete classnote - 2310035 .pdf`
> - **Companion Note**: Part 1 (Numerical Methods, Pages 01–18) is located at [[01_ECE2213_Numerical_Methods_ClassNotes]].
> - **Spread Accounting**: Pages 19–32 and 36–37 are scanned two-page notebook spreads; Pages 33–35 and 38–40 are single-page scans (~38 physical notebook pages).
> - **Note on Pedagogical Ordering**: Combinatorics & Pigeonhole Principle (Pages 39–40, dated 26.09.2026) are organized before the final Proof review (Pages 36–38, dated 28.09.2026) to preserve topical coherence.
> - **Translation**: All handwritten Bengali annotations have been translated into English callouts while preserving pedagogical meaning.

---

## 1. Set Theory (Rosen Chapter 2)

<!-- Page 19 (Dual spread: Set definitions, roster/builder form, interval notation) -->

### 1.1 Fundamental Definitions

- **Set**: An unordered collection of objects.
- **Elements (Objects)**: The members belonging to a set.
  - $a \in A$: "$a$ belongs to $A$" ($a$ is an element of set $A$).
  - $a \notin A$: "$a$ does not belong to $A$".

### 1.2 Standard Number Sets

- $\mathbb{N} = \{0, 1, 2, 3, \dots\}$: Set of natural numbers (discrete math convention including $0$).
- $\mathbb{Z} = \{\dots, -2, -1, 0, 1, 2, \dots\}$: Set of integers $(-n, \dots, n)$.
- $\mathbb{Z}^+ = \{1, 2, 3, \dots\}$: Set of positive integers.
- $\mathbb{R}$: Set of real numbers.
- $\mathbb{Q}$: Set of rational numbers *(translated from Bengali annotation: মূলদ সংখ্যা)*.
- $\mathbb{C}$: Set of complex numbers.

### 1.3 Intervals vs. Discrete Sets

A key conceptual distinction between continuous intervals and discrete sets:
- **Open Interval**: $A = (0, 5) = \{x \in \mathbb{R} \mid 0 < x < 5\}$ (endpoints $0$ and $5$ are excluded).
- **Closed Interval**: $A = [0, 5] = \{x \in \mathbb{R} \mid 0 \le x \le 5\}$ (endpoints $0$ and $5$ are included).
- **Discrete Set**: $A = \{0, 5\}$ (contains **only** the two discrete numbers $0$ and $5$, not the numbers in between).

![Fig_Discrete01.1: Hand-drawn comparison of open interval (0,5), closed interval [0,5], and discrete set {0,5} on number line](diagrams/discrete_p19_fig1_intervals.jpg)
*Figure 2.1 — Hand-drawn comparison of open interval (0,5), closed interval [0,5], and discrete set {0,5} on the number line (Page 19)*

### 1.4 Methods of Representing Sets

*(Translated from Bengali annotation: সেট গঠন পদ্ধতি)*

1. **Roster / Tabular Method** *(তালিকা পদ্ধতি)*: Explicitly listing all elements separated by commas inside braces.
2. **Set-Builder Method** *(সেট গঠন পদ্ধতি)*: Stating the predicate property that elements must satisfy:
   $$S = \{x \mid P(x)\}$$

**Example:**
$$S = \{x : x \in \mathbb{N}, x^2 > 25 \land x^3 < 1000\}$$
- Condition 1: $x^2 > 25 \implies x > 5$
- Condition 2: $x^3 < 1000 \implies x < 10$
- Natural numbers satisfying both:
  $$S = \{6, 7, 8, 9\}$$

### 1.5 Special Sets

- **Empty Set (Null Set)**: A set with no elements, denoted $\emptyset$ or $\{\}$.
- **Universal Set**: The set containing all possible objects under consideration, denoted $U$ *(translated from Bengali: সার্বিক সেট)*.

### 1.6 Set Equality

Two sets are equal if and only if they contain exactly the same elements:
$$\forall x (x \in A \leftrightarrow x \in B)$$

#### Key Quantifier & Logic Notations
- $\forall$: For all / Universal quantifier
- $\exists$: There exists / Existential quantifier
- $\exists!$: There exists uniquely / Exists exactly one
- $\nexists$: Does not exist

### 1.7 Subsets and Proper Subsets

- **Subset ($A \subseteq B$)**:
  Set $A$ is a subset of set $B$ if every element of $A$ is also present in $B$:
  $$\forall x (x \in A \to x \in B)$$
- **Proper Subset ($A \subset B$ or $A \subsetneq B$)**:
  Set $A$ is a proper subset of $B$ if $A$ is a subset of $B$, but $A$ is not equal to $B$ ($B$ contains at least one element not present in $A$):
  $$A \subseteq B \land A \neq B$$
  - The set cannot be identical to the parent set.
  - The superset must have at least one additional element compared to the subset.

---

<!-- Page 20 -->

### 1.8 Cardinality of Sets

*(Translated from Bengali annotation: উপাদান সংখ্যা — the number of elements in a set)*

For a finite set $S$, the cardinality is the number of distinct elements, denoted $|S|$:
- $|\emptyset| = 0$
- If $B = \{1, 3, 5\}$, then $|B| = 3$.
- $|\mathbb{N}| = \infty$ (infinite cardinality).

### 1.9 Power Set

The power set of a set $S$, denoted $\mathcal{P}(S)$, is the set of all subsets of $S$:
$$\mathcal{P}(S) = \{A \mid A \subseteq S\}$$

**Example:**
For $S = \{1, 2\}$:
$$\mathcal{P}(S) = \{\emptyset, \{1\}, \{2\}, \{1, 2\}\}$$

> **Cardinality Rule for Power Sets**:  
> If $|S| = n$, then the cardinality of the power set is:
> $$|\mathcal{P}(S)| = 2^n$$

### 1.10 Cartesian Product

For sets $A$ and $B$, the Cartesian product $A \times B$ is the set of all ordered pairs $(a, b)$ where $a \in A$ and $b \in B$:
$$A \times B = \{(a, b) \mid a \in A \land b \in B\}$$

**Example:**
- Let $A = \{a, b\}$ and $B = \{1, 2, 3\}$.
- $A \times B = \{(a, 1), (a, 2), (a, 3), (b, 1), (b, 2), (b, 3)\}$
- Notice $|A \times B| = |A| \times |B| = 2 \times 3 = 6$.

### 1.11 Set Operations

- **Union**:
  $$A \cup B = \{x \mid x \in A \lor x \in B\}$$
- **Intersection**:
  $$A \cap B = \{x \mid x \in A \land x \in B\}$$
- **Complement**:
  $$\overline{A} = \{x \in U \mid x \notin A\}$$
- **Set Difference (Relative Complement)**:
  $$A - B = \{x \mid x \in A \land x \notin B\} = A \cap \overline{B}$$
- **Symmetric Difference**:
  $$A \oplus B = (A - B) \cup (B - A)$$

*(Logical connectives key: $\lor \equiv \text{OR}$, $\land \equiv \text{AND}$, $\neg \equiv \text{NOT}$)*

---

### 1.12 Functions and Mappings

*(Translated from Bengali annotation: প্রত্যেক different input এর জন্য output — A relation assigns to each input in the domain exactly one output in the codomain)*

- **Domain**: Set of all allowable input values ($A$).
- **Codomain**: Target set containing all potential outputs ($B$).
- **Range**: Actual set of mapped output values:
  $$f(A) = \{f(x) \mid x \in A\} \subseteq B$$

#### Classification of Functions
1. **One-to-One (Injective)**:
   Distinct domain elements map to distinct codomain elements:
   $$f(a) = f(b) \implies a = b$$
2. **Onto (Surjective)**:
   Every element of the codomain is mapped to at least one element of the domain:
   $$\text{Range} = \text{Codomain}$$
3. **Into Function**:
   The range is a proper subset of the codomain ($\text{Range} \subset \text{Codomain}$), meaning at least one codomain element is not mapped.
4. **Bijective (One-to-One Correspondence)**:
   A function that is both **Injective** and **Surjective**.
5. **Inverse Function ($f^{-1}$)**:
   An inverse function exists if and only if $f$ is **Bijective**.

#### Function Composition
Let $g: A \to B$ and $f: B \to C$:
- $(f \circ g)(x) = f(g(x))$
- $(g \circ f)(x) = g(f(x))$

---

## 2. Propositional Logic (Rosen Chapter 1)

<!-- Page 21 -->

### 2.1 Propositions and Truth Values

- **Proposition**: A declarative statement that is either True ($T$) or False ($F$), but not both.
- **Propositional Variables**: Conventional symbols representing propositions: $p, q, r, s, \dots$
  - Example: Let $p =$ "Today is Saturday".
- **Truth Values**: Denoted by $T$ (True) or $F$ (False).

### 2.2 Logical Connectives

1. **Negation ($\neg p$, NOT)**:
   - Reverses the truth value of proposition $p$.
   - Example: Let $p =$ "The earth is round".  
     $\neg p =$ "It is not the case that the earth is round" or "The earth is not round."
   - Truth Table:
     | $p$ | $\neg p$ |
     | :---: | :---: |
     | $T$ | $F$ |
     | $F$ | $T$ |

2. **Conjunction ($p \land q$, AND)**:
   - True only when both $p$ and $q$ are True; functions like a logic AND gate.
   - Example: $p =$ "I am at home", $q =$ "It is raining".  
     $p \land q =$ "I am at home and it is raining."
   - Truth Table:
     | $p$ | $q$ | $p \land q$ |
     | :---: | :---: | :---: |
     | $T$ | $T$ | $T$ |
     | $T$ | $F$ | $F$ |
     | $F$ | $T$ | $F$ |
     | $F$ | $F$ | $F$ |

3. **Disjunction ($p \lor q$, Inclusive OR)**:
   - True if at least one of $p$ or $q$ is True; False only when both are False.
   - Example: $p \lor q =$ "I am at home or it is raining."
   - Truth Table:
     | $p$ | $q$ | $p \lor q$ |
     | :---: | :---: | :---: |
     | $T$ | $T$ | $T$ |
     | $T$ | $F$ | $T$ |
     | $F$ | $T$ | $T$ |
     | $F$ | $F$ | $F$ |

4. **Exclusive OR ($p \oplus q$, XOR)**:
   - True when exactly one of $p$ or $q$ is True, but not both.
   - Truth Table:
     | $p$ | $q$ | $p \oplus q$ |
     | :---: | :---: | :---: |
     | $T$ | $T$ | $F$ |
     | $T$ | $F$ | $T$ |
     | $F$ | $T$ | $T$ |
     | $F$ | $F$ | $F$ |

---

<!-- Page 22 -->

### 2.3 Conditional Statement (Implication, $p \to q$)

- **Form**: "If $p$, then $q$".
- $p$: Hypothesis / Antecedent / Premise.
- $q$: Conclusion / Consequence.

#### Truth Table
| $p$ (Hypothesis) | $q$ (Conclusion) | $p \to q$ |
| :---: | :---: | :---: |
| $T$ | $T$ | $T$ |
| $T$ | $F$ | $F$ |
| $F$ | $T$ | $T$ |
| $F$ | $F$ | $T$ |

> **Pedagogical Meaning of Implication** *(translated from handwritten Bengali)*:  
> - **When $p$ is True**: The hypothesis has occurred; therefore $q$ **must** happen for the promise to remain unbroken. If $q$ does not happen ($q = F$), the statement is **False**.  
> - **When $p$ is False**: The hypothesis did not occur. The consequence $q$ may happen or may not happen; in either case, no promise was broken, so the implication is vacuously **True**.  
> - *Summary rule*: The only way $p \to q$ is False is when the main condition (premise) is True, but the secondary condition (conclusion) is False ($T \to F \equiv F$).

#### 10 Ways to Express $p \to q$ in Natural English
1. "If $p$, then $q$"
2. "If $p, q$"
3. "$q$ unless $\neg p$"
4. "$q$ if $p$"
5. "$q$ whenever $p$"
6. "$q$ follows from $p$"
7. "$p$ only if $q$"
8. "$q$ when $p$"
9. "$p$ is sufficient for $q$"
10. "$q$ is necessary for $p$"

### 2.4 Biconditional Statement ($p \leftrightarrow q$)

- **Form**: "$p$ if and only if $q$" ($p$ iff $q$).
- Example: "I am at home if and only if it is raining."
- Truth Table:
  | $p$ | $q$ | $p \leftrightarrow q$ |
  | :---: | :---: | :---: |
  | $T$ | $T$ | $T$ |
  | $T$ | $F$ | $F$ |
  | $F$ | $T$ | $F$ |
  | $F$ | $F$ | $T$ |

#### Ways of Expressing Biconditional
- "$p$ is necessary and sufficient for $q$"
- "If $p$ then $q$, and conversely"
- "$p$ iff $q$"

### 2.5 Converse, Contrapositive, and Inverse

Given the conditional statement $p \to q$:
- **Converse**: $q \to p$
- **Contrapositive**: $\neg q \to \neg p$  
  *(Logically equivalent to the original statement: $p \to q \equiv \neg q \to \neg p$)*
- **Inverse**: $\neg p \to \neg q$  
  *(Logically equivalent to the converse: $\neg p \to \neg q \equiv q \to p$)*

---

<!-- Page 23 | 31.08.2026 -->

### 2.6 Logical Operator Precedence

When parentheses are omitted, logical operators are evaluated in this strict order:
1. $\neg$ (Negation) — Highest precedence
2. $\land$ (Conjunction)
3. $\lor$ (Disjunction)
4. $\to$ (Conditional / Implication)
5. $\leftrightarrow$ (Biconditional) — Lowest precedence

### 2.7 Natural Language Translation Examples

#### Example 1: Basic Connectives
- $p$: "I go to university library"
- $q$: "I will go to country"
- $r$: "I will go shopping"
- Expression: $(p \lor q) \to \neg r$

#### Example 2: Campus Internet Access
- $a$: "You can access the internet from campus"
- $c$: "You are a computer science major"
- $f$: "You are a freshman"
- Statement: "You can access the internet from campus only if you are a computer science major or not a freshman."
- Expression: $a \to (c \lor \neg f)$

#### Example 3: System Specification Translation
> **Specification**:  
> "The system will operate in normal mode if and only if the primary controller or the backup controller is active, but not both. However, if the emergency sensor is triggered, then the system will enter emergency mode only if both the controllers are inactive."

- Identify variables:
  - $O$: System operates in normal mode
  - $P$: Primary controller is active
  - $B$: Backup controller is active
  - $T$: Emergency sensor is triggered
  - $E$: System enters emergency mode
- Key logical word translations:
  - "However", "moreover" $\to$ translated as Conjunction ($\land$).
  - "Or ..., but not both" $\to$ Exclusive OR ($\oplus$).
  - "Only if" $\to$ Implication ($\to$).
  - "Both controllers are inactive" $\to \neg P \land \neg B$.
- **Formalized Logic Translation**:
  $$O \leftrightarrow (P \oplus B) \land (T \to (E \to (\neg P \land \neg B)))$$

#### Example 4: Student Examination & Certificate
- Variables:
  - $p$: The students study regularly
  - $q$: The students attend the tutorial class
  - $r$: The student passes the examination
  - $s$: The students receive a certificate
- Sentence:
  "If the students study regularly or attend the tutorial class but not both, then the student passes the exam. However, the student receives a certificate if and only if they pass the exam."
- **Formalized Expression**:
  $$((p \oplus q) \to r) \land (r \leftrightarrow s)$$

---

<!-- Page 24 | 06.09.2026 -->

### 2.8 Propositional Classifications

- **Tautology**: A compound proposition that is always True, regardless of the truth values of its individual variables (e.g., $p \lor \neg p \equiv T$).
- **Contradiction**: A compound proposition that is always False (e.g., $p \land \neg p \equiv F$).
- **Contingency**: A compound proposition that is neither a tautology nor a contradiction (it can be True or False depending on the variables).

### 2.9 Important Logical Equivalences

Two statements are logically equivalent ($p \equiv q$) if $p \leftrightarrow q$ is a tautology.

#### 1. Implication Equivalence
$$p \to q \equiv \neg p \lor q$$

**Verification via Truth Table:**
| $p$ | $q$ | $p \to q$ | $\neg p$ | $\neg p \lor q$ |
| :---: | :---: | :---: | :---: | :---: |
| $T$ | $T$ | $T$ | $F$ | $T$ |
| $T$ | $F$ | $F$ | $F$ | $F$ |
| $F$ | $T$ | $T$ | $T$ | $T$ |
| $F$ | $F$ | $T$ | $T$ | $T$ |

*(The columns for $p \to q$ and $\neg p \lor q$ are identical, proving equivalence).*

#### 2. Key Equivalence Laws
- **Identity Laws**:
  $$p \land T \equiv p, \quad p \lor F \equiv p$$
- **Domination Laws**:
  $$p \lor T \equiv T, \quad p \land F \equiv F$$
- **Idempotent Laws**:
  $$p \lor p \equiv p, \quad p \land p \equiv p$$
- **Double Negation Law**:
  $$\neg(\neg p) \equiv p$$
- **De Morgan's Laws**:
  $$\neg(p \lor q) \equiv \neg p \land \neg q$$
  $$\neg(p \land q) \equiv \neg p \lor \neg q$$

> **Exam Preparation Tip** *(translated from Bengali annotation)*:  
> Proving tautologies and equivalences is extremely important for exams. You must be prepared to solve them using two distinct methods:  
> 1. Algebraic deduction using equivalence laws.  
> 2. Exhaustive truth table construction.

---

## 3. Predicate Logic and Quantifiers

### 3.1 Predicates

A predicate is a statement containing variables that becomes a proposition when values are assigned to those variables:
- Example: $P(x) = "x + y = 9" \to$ function $f(x, y) = x + y$.
  - For $(5, 7)$: $5 + 7 = 12 \neq 9 \implies \text{False}$.
- $P(x) = "x \text{ is mortal}"$ (Predicate).
- $P(\text{Socrates}) = "\text{Socrates is mortal}"$ (Proposition).

---

<!-- Page 25 | 07.09.2026 -->

### 3.2 Quantifiers

1. **Universal Quantifier ($\forall$)**:
   - $\forall x P(x)$: "$P(x)$ is true for all $x$ in the domain of discourse."
   - Finite domain expansion:
     $$\forall x P(x) \equiv P(x_1) \land P(x_2) \land \dots \land P(x_n)$$
2. **Existential Quantifier ($\exists$)**:
   - $\exists x P(x)$: "There exists an element $x$ in the domain of discourse such that $P(x)$ is true."
   - Finite domain expansion:
     $$\exists x P(x) \equiv P(x_1) \lor P(x_2) \lor \dots \lor P(x_n)$$

### 3.3 Translating English to Predicate Logic

**Example**: "Every student in the class has taken a course in Java."
- Let $S(x)$: "$x$ is a student in the class".
- Let $J(x)$: "$x$ has taken a course in Java".
- Correct Translation:
  $$\forall x (S(x) \to J(x))$$
- *Common Pitfall*: Writing $\forall x (S(x) \land J(x))$ is incorrect because it asserts that every entity in the entire universe is both a student in this class and has taken Java.

### 3.4 De Morgan's Laws for Quantifiers

1. $\neg \forall x P(x) \equiv \exists x \neg P(x)$
2. $\neg \exists x P(x) \equiv \forall x \neg P(x)$

---

<!-- Page 26 | 09.09.2026 -->

### 3.5 Predicate Logic Translation Problems

#### Problem 1: Students visiting Mexico
"Some students in the class have visited Mexico."
- Let $U =$ All people.
- $S(x)$: "$x$ is a student in the class".
- $M(x)$: "$x$ has visited Mexico".
- Translation:
  $$\exists x (S(x) \land M(x))$$
- *(If the domain is restricted only to students in the class, it simplifies to $\exists x M(x)$).*

#### Problem 2: Visiting Canada or Mexico
"Every student in the class has visited Canada or Mexico."
- Let $C(x)$: "$x$ has visited Canada", $M(x)$: "$x$ has visited Mexico".
- Translation:
  $$\forall x (S(x) \to (C(x) \lor M(x)))$$

#### Problem 3: Universe of Abstract Entities
Let $U = \{\text{fleegles}, \text{snurds}, \text{thingamabobs}\}$.
- $F(x)$: "$x$ is a fleegle"
- $S(x)$: "$x$ is a snurd"
- $T(x)$: "$x$ is a thingamabob"

1. "Everything is a fleegle":
   $$\forall x F(x)$$
2. "Nothing is a snurd":
   $$\neg \exists x S(x) \equiv \forall x \neg S(x)$$
3. "All fleegles are snurds":
   $$\forall x (F(x) \to S(x))$$

---

<!-- Page 27 -->

4. "Some fleegles are thingamabobs":
   $$\exists x (F(x) \land T(x))$$

> **Fundamental Translation Rules** *(translated from Bengali annotations)*:  
> - For **Universal statements ($\forall$)**, always use **Implication ($\to$)**.  
> - For **Existential statements ($\exists$)**, always use **Conjunction ($\land$)**.  
> - *If a property does not hold universally for all entities, use existential quantification.*

5. "No snurd is a thingamabob":
   $$\neg \exists x (S(x) \land T(x)) \equiv \forall x \neg (S(x) \land T(x)) \equiv \forall x (\neg S(x) \lor \neg T(x))$$
6. "If any fleegle is a snurd, then it is also a thingamabob":
   $$\forall x ((F(x) \land S(x)) \to T(x))$$

### 3.6 System Specifications Using Quantifiers

**Specification 1**: "Every mail message larger than one kilobyte will be compressed."
- $P(x, y)$: "message $x$ is larger than $y$ KB".
- $Q(x)$: "message $x$ will be compressed".
- Translation:
  $$\forall m (P(m, 1) \to Q(m))$$

**Specification 2**: "If a user is active, at least one network link will be available."
- $A(u)$: "User $u$ is active".
- $S(n, \text{available})$: "Network link $n$ is available".
- Translation:
  $$\exists u A(u) \to \exists n S(n, \text{available})$$

---

<!-- Page 28 | 12.09.2026 (Dual spread) -->

> [!NOTE] Class Test (CT) Syllabus Announcement *(from top-left margin)*
> - **Textbook & Slides**: Rosen textbook; Slides 1.1 & 1.2 (up to before Nested Quantifiers).
> - **Focus**: Translation practice (English to logic & logic to English).

### 3.7 Nested Quantifiers

Nested quantifiers can be thought of as **nested loops** in programming: the outer quantifier specifies the outer loop, and the inner quantifier specifies the inner loop.

#### Commutativity of Quantifiers
- $\forall x \forall y P(x, y) \equiv \forall y \forall x P(x, y)$ (Order does not matter).
- $\exists x \exists y P(x, y) \equiv \exists y \exists x P(x, y)$ (Order does not matter).

> **Crucial Rule on Quantifier Order** *(translated from Bengali annotation)*:  
> You must pay close attention to the order of quantifiers. If both quantifiers are identical (both $\forall$ or both $\exists$), the order can be swapped without changing meaning. However, when mixing $\forall$ and $\exists$, **the order is critical!** Always evaluate the outer quantifier first, then the inner quantifier.

#### Examples over the Real Numbers ($\mathbb{R}$)

1. "Every real number has an opposite (additive inverse)":
   $$\forall x \exists y (x + y = 0) \quad \text{[True; for every } x \text{, take } y = -x\text{]}$$
2. "Every real number has an inverse (multiplicative inverse)":
   $$\forall x \exists y (x \cdot y = 1) \quad \text{[False; } x = 0 \text{ has no multiplicative inverse]}$$
3. Let $P(x, y): x \cdot y = 0$ over $\mathbb{R}$:
   - $\forall x \forall y P(x, y)$: **False** (e.g., $1 \cdot 2 \neq 0$).
   - $\forall x \exists y P(x, y)$: **True** (for any given $x$, choose $y = 0$).
   - $\exists x \forall y P(x, y)$: **True** (choose $x = 0$, then $0 \cdot y = 0$ for all $y$).
   - $\exists x \exists y P(x, y)$: **True** (e.g., $0 \cdot 0 = 0$).

#### Complex Translation Example
"Every student in your school has a computer or has a friend who has a computer."
- $C(x)$: "$x$ has a computer"
- $F(x, y)$: "$x$ and $y$ are friends"
- **Translation**:
  $$\forall x (C(x) \lor \exists y (C(y) \land F(x, y)))$$

---

<!-- Page 29 -->

#### Triply Nested Quantifier Example
"There is a student none of whose friends are also friends with each other."
$$\exists x \forall y \forall z ((F(x, y) \land F(x, z) \land (y \neq z)) \to \neg F(y, z))$$

---

## 4. Rules of Inference and Valid Arguments (Rosen 1.6)

An argument in propositional logic is a sequence of propositions ending in a conclusion:
$$(p_1 \land p_2 \land \dots \land p_n) \to q$$
where $p_1, p_2, \dots, p_n$ are the **premises**, and $q$ is the **conclusion**.  
An argument is **valid** if the conditional statement is a **tautology**.

### 4.1 Table of Inference Rules

*(The conclusion is conventionally denoted with $\therefore$ meaning "therefore")*

| Rule of Inference | Name | Tautology Form |
| :--- | :--- | :--- |
| $\frac{p \to q, \quad p}{\therefore q}$ | **Modus Ponens** | $(p \land (p \to q)) \to q$ |
| $\frac{p \to q, \quad \neg q}{\therefore \neg p}$ | **Modus Tollens** | $(\neg q \land (p \to q)) \to \neg p$ |
| $\frac{p \to q, \quad q \to r}{\therefore p \to r}$ | **Hypothetical Syllogism** | $((p \to q) \land (q \to r)) \to (p \to r)$ |
| $\frac{p \lor q, \quad \neg p}{\therefore q}$ | **Disjunctive Syllogism** | $((p \lor q) \land \neg p) \to q$ |
| $\frac{p}{\therefore p \lor q}$ | **Addition** | $p \to (p \lor q)$ |
| $\frac{p \land q}{\therefore p}$ (or $q$) | **Simplification** | $(p \land q) \to p$ |
| $\frac{p, \quad q}{\therefore p \land q}$ | **Conjunction** | $((p) \land (q)) \to (p \land q)$ |
| $\frac{p \lor q, \quad \neg p \lor r}{\therefore q \lor r}$ | **Resolution** | $((p \lor q) \land (\neg p \lor r)) \to (q \lor r)$ |

> **Exam Tip** *(translated from Bengali annotation)*:  
> Direct short notes and derivation problems are frequently set on **Resolution** and the Rules of Inference.

### 4.2 Worked Derivation Examples

#### Example 1: Formal deduction of $q$
Show that $[p \land (p \to q)] \to q$ is a valid argument:
1. $p \land (p \to q)$ [Hypothesis]
2. $p$ [Simplification from 1]
3. $p \to q$ [Simplification from 1]
4. $q$ [Modus Ponens from 2 and 3]

---

<!-- Page 30 (Left page of spread: Logic Derivation) -->

#### Example 2: Story Problem Deduction
Given the propositions:
- $p$: "It is sunny this afternoon"
- $q$: "It is colder than yesterday"
- $r$: "We will go swimming"
- $s$: "We will take a canoe trip"
- $t$: "We will be home by sunset"

Premises:
1. $\neg p \land q$
2. $r \to p$
3. $\neg r \to s$
4. $s \to t$

**Conclusion to prove**: $\therefore t$

**Formal Proof Steps**:
1. $\neg p \land q$ [Premise 1]
2. $\neg p$ [Simplification of 1]
3. $r \to p$ [Premise 2]
4. $\neg r$ [Modus Tollens from 2 and 3]
5. $\neg r \to s$ [Premise 3]
6. $s$ [Modus Ponens from 4 and 5]
7. $s \to t$ [Premise 4]
8. $\therefore t$ [Modus Ponens from 6 and 7] $\quad \blacksquare$

---

## 5. Number Theory, Divisibility & Modular Arithmetic

<!-- Page 30 (Right page of spread: Divisibility | 15.09.2026) -->

### 5.1 Divisibility

Let $a, b \in \mathbb{Z}$ with $a \neq 0$. We say that **$a$ divides $b$** (written $a \mid b$) if there exists an integer $c$ such that:
$$b = ac$$

> **Core Principle** *(translated from Bengali annotation)*:  
> The division must be exact with no remainder, and the resulting quotient must be an integer.

#### Properties of Divisibility
1. If $a \mid b$ and $a \mid c$, then $a \mid (b + c)$.
   - *Example*: $3 \mid 9$ and $3 \mid 12 \implies 3 \mid (9 + 12) = 21$.
2. If $a \mid b$, then $a \mid bc$ for all integers $c$.
3. If $a \mid b$ and $b \mid c$, then $a \mid c$ (Transitivity).

#### Proof of Property 1
- $a \mid b \implies b = as$ for some integer $s$.
- $a \mid c \implies c = at$ for some integer $t$.
- Adding both: $b + c = as + at = a(s + t)$.
- Since $(s + t)$ is an integer, $a \mid (b + c)$. $\blacksquare$

#### Corollary (Linear Combinations)
If $a \mid b$ and $a \mid c$, then $a \mid (mb + nc)$ for any integers $m, n$.

---

<!-- Page 31 (Dual spread: Division Algorithm & Congruences [Left] / CRT Introduction [Right]) -->

### 5.2 The Division Algorithm

Let $a$ be an integer and $d$ a positive integer ($d \in \mathbb{Z}^+$). Then there exist unique integers $q$ and $r$, with $0 \le r < d$, such that:
$$a = dq + r$$
- $d$: Divisor
- $a$: Dividend
- $q = a \text{ div } d$: Quotient
- $r = a \bmod d$: Remainder

*Example*: $10 = 3 \times 3 + 1 \implies 10 \text{ div } 3 = 3$, $10 \bmod 3 = 1$.

### 5.3 Modular Congruence

If $a$ and $b$ are integers and $m$ is a positive integer, then **$a$ is congruent to $b$ modulo $m$** (written $a \equiv b \pmod m$) if $m$ divides $(a - b)$:
$$a \equiv b \pmod m \iff m \mid (a - b)$$

> **Conceptual Meaning** *(translated from Bengali annotation)*:  
> If the difference between $a$ and $b$ is divisible by $m$ without remainder, then $a$ and $b$ are congruent modulo $m$.

**Example**:
$$17 \equiv 5 \pmod 6 \iff 6 \mid (17 - 5) = 12 \quad (\text{Since } 12/6 = 2 \in \mathbb{Z})$$

#### Key Theorems on Congruence
- **Theorem 3**: $a \equiv b \pmod m \iff a \bmod m = b \bmod m$.
- **Theorem 4**: $a \equiv b \pmod m \iff a = b + km$ for some integer $k$ *(updated general form)*.
- **Theorem 5 (Algebraic Properties)**:
  If $a \equiv b \pmod m$ and $c \equiv d \pmod m$, then:
  $$a + c \equiv b + d \pmod m$$
  $$ac \equiv bd \pmod m$$

---

### 5.4 Chinese Remainder Theorem (CRT)

> **Study Directive** *(translated from Bengali annotation)*:  
> *Chinese Remainder Theorem $\to$ Must study / high exam priority topic!*

#### Theorem Statement
Let $m_1, m_2, \dots, m_n$ be pairwise relatively prime positive integers greater than $1$ ($\gcd(m_i, m_j) = 1$ for all $i \neq j$). Then the system of congruences:
$$x \equiv a_1 \pmod{m_1}$$
$$x \equiv a_2 \pmod{m_2}$$
$$\vdots$$
$$x \equiv a_n \pmod{m_n}$$
has a unique solution modulo $M = m_1 \times m_2 \times \dots \times m_n$.

#### General Formula
$$x \equiv \left( \sum_{i=1}^n a_i M_i M_i^{-1} \right) \pmod M$$
where $M_i = \frac{M}{m_i}$, and $M_i^{-1}$ is the modular inverse of $M_i$ modulo $m_i$ ($M_i M_i^{-1} \equiv 1 \pmod{m_i}$).

#### Complete Worked Problem
Solve the system:
$$x \equiv 2 \pmod 3$$
$$x \equiv 3 \pmod 5$$
$$x \equiv 2 \pmod 7$$

<!-- Page 33 (Single page: CRT solution continuation) -->

**Step 1: Compute $M$ and individual $M_i$**
- $M = 3 \times 5 \times 7 = 105$
- $M_1 = 105 / 3 = 35$
- $M_2 = 105 / 5 = 21$
- $M_3 = 105 / 7 = 15$

**Step 2: Find modular inverses $M_i^{-1}$**
- For $M_1 = 35$ modulo $3$:
  $$35 M_1^{-1} \equiv 1 \pmod 3 \implies 2 M_1^{-1} \equiv 1 \pmod 3 \implies M_1^{-1} = 2$$
  *(Verification: $\frac{35 \times 2}{3} = \frac{70}{3} = 23$ with remainder $1$)*
- For $M_2 = 21$ modulo $5$:
  $$21 M_2^{-1} \equiv 1 \pmod 5 \implies 1 M_2^{-1} \equiv 1 \pmod 5 \implies M_2^{-1} = 1$$
- For $M_3 = 15$ modulo $7$:
  $$15 M_3^{-1} \equiv 1 \pmod 7 \implies 1 M_3^{-1} \equiv 1 \pmod 7 \implies M_3^{-1} = 1$$

**Step 3: Calculate $x$**
$$x = (a_1 M_1 M_1^{-1} + a_2 M_2 M_2^{-1} + a_3 M_3 M_3^{-1}) \bmod M$$
$$x = (2 \times 35 \times 2 + 3 \times 21 \times 1 + 2 \times 15 \times 1) \bmod 105$$
$$x = (140 + 63 + 30) \bmod 105 = 233 \bmod 105$$
$$233 = 105 \times 2 + 23 \implies x = 23$$

---

<!-- Page 33 (Header Section: Course Slides Index & LCM Topic) -->
### 5.4.1 Course Slide Roadmap & LCM Topic

> [!INFO] Slide Cross-Reference Index *(from notebook header on Page 33)*
> - **Slides 1.1, 1.2, 1.3, 1.4**: Mathematical Reasoning & Methods of Proof
> - **Slides 2.1, 2.2**: Basic Structures (Sets, Functions, Sequences)
> - **Slide 4**: Number Theory (Divisibility, Modular Arithmetic, Primes)
> - **Slide 6**: Counting & Combinatorics (Pigeonhole Principle, Permutations)

#### Least Common Multiple (LCM)
- **Definition**: The least common multiple of positive integers $a$ and $b$ is the smallest positive integer that is divisible by both $a$ and $b$, denoted $\operatorname{lcm}(a, b)$.
- **Key Fundamental Relationship with GCD**:
  $$a \cdot b = \gcd(a, b) \cdot \operatorname{lcm}(a, b)$$

---

<!-- Page 32 (Dual spread: Primes, GCD, Euclidean Algorithm | 19.09.2026 | Nadim Sir) -->

### 5.5 Prime Numbers & Prime Factorization

- **Prime Number**: An integer $p > 1$ whose only positive divisors are $1$ and $p$.
- **Composite Number**: An integer that can be factored into a product of primes *(translated from Bengali: prime number এর গুণফল আকারে)*.
- **Fundamental Theorem of Arithmetic**: Every integer greater than $1$ can be written uniquely as a prime or as the product of two or more primes where prime factors are written in non-decreasing order.
- **Sieve of Eratosthenes Theorem**:
  > If $n$ is a composite integer, then $n$ must have a prime divisor less than or equal to $\sqrt{n}$ *(translated from Bengali: একটি composite number $n$ হয়, তাহলে এর divisor $\sqrt{n}$ এর ছোট অথবা সমান)*.

- **Mersenne Primes**: Primes of the form $2^p - 1$, where $p$ is prime.  
  *Counterexample*: $2^{11} - 1 = 2047 = 23 \times 89$ (composite).

### 5.6 Greatest Common Divisor (GCD) and Least Common Multiple (LCM)

The greatest common divisor of two integers $a$ and $b$ (not both zero), denoted $\gcd(a, b)$, is the largest integer that divides both $a$ and $b$.

#### Prime Factorization Method
- Prime factors of $24$: $24 = 2^3 \times 3^1$
- Prime factors of $36$: $36 = 2^2 \times 3^2$
- $\gcd(24, 36) = 2^{\min(3, 2)} \times 3^{\min(1, 2)} = 2^2 \times 3^1 = 12$

Another example:
- $120 = 2^3 \times 3^1 \times 5^1$
- $500 = 2^2 \times 3^0 \times 5^3$
- $\gcd(120, 500) = 2^2 \times 3^0 \times 5^1 = 20$

> **Self-Study Directive** *(translated from Bengali annotation)*:  
> Extended Euclidean Algorithm $\to$ Self-study topic, best practiced and prepared in tabular format.

#### Euclidean Algorithm
Based on the property: $\gcd(a, b) = \gcd(b, a \bmod b)$.
- Example: $\gcd(81, 287)$
  $$\gcd(287, 81) = \gcd(81, 44) = \gcd(44, 37) \dots = 7$$

---

## 6. Combinatorics and Counting

<!-- Pages 34–35 (Single pages: Permutations & Combinations | 21.09.2026) -->

### 6.1 Permutations and Combinations

- **Selection $\to$ Combination ($C$)** *(un-ordered choices)*
- **Arrangement $\to$ Permutation ($P$)** *(ordered sequences)*

For a set of $n$ distinct elements, the number of $r$-permutations is:
$$P(n, r) = {}^n P_r = \frac{n!}{(n - r)!}$$

### 6.2 Word Arrangement with Repetitions: "PROFESSOR"

Letters in `PROFESSOR`:
- Letters: $\{P, R, O, F, E, S, S, O, R\}$ (Total $9$ letters)
- Distinct letters: $\{P, R, O, F, E, S\}$ ($6$ distinct letter types)
- Multiplicities:
  - $O \to 2$
  - $R \to 2$
  - $S \to 2$
  - $P \to 1$
  - $F \to 1$
  - $E \to 1$

> **Problem**: How many ways can you arrange 4 letters chosen from the word `PROFESSOR`?

To solve this, we must decompose into three mutually exclusive cases based on letter multiplicities:

#### Case 1: All 4 letters are distinct
- Choose 4 distinct letters from the 6 available distinct letters:
  $$\binom{6}{4} = 15$$
- Arrange the 4 distinct letters:
  $$4! = 24$$
- Total for Case 1:
  $$\binom{6}{4} \times 4! = 15 \times 24 = 360$$

#### Case 2: Exactly one letter repeats twice (1 pair + 2 distinct singles)
*(Translated from Bengali annotation: যেকোনো একটা দুইবার নিতে পারবো? — Can we choose any one letter twice?)*
- Choose which letter has the pair from the 3 available pairs $\{O, R, S\}$:
  $$\binom{3}{1} = 3$$
- Choose the remaining 2 distinct letters from the remaining 5 distinct letters:
  $$\binom{5}{2} = 10$$
- Arrange the 4 letters (with 2 identical):
  $$\frac{4!}{2!} = 12$$
- Total for Case 2:
  $$\binom{3}{1} \times \binom{5}{2} \times \frac{4!}{2!} = 3 \times 10 \times 12 = 360$$

*(Explanation translated: After selecting the letters, arrange them in $4!$ ways, but since identical letters exist, divide by the factorial of the repeated counts: $\frac{4!}{2!}$)*

---

<!-- Page 35 -->

#### Case 3: Two letters repeat twice (2 pairs, e.g., OORR)
*(Translated from Bengali annotation: দুইটা letter repeat হতে পারবে — Two letters can repeat)*
- Choose 2 pairs from the 3 available pairs $\{O, R, S\}$:
  $$\binom{3}{2} = 3$$
- Arrange the 4 letters (with two pairs of identical letters):
  $$\frac{4!}{2! 2!} = \frac{24}{4} = 6$$
- Total for Case 3:
  $$\binom{3}{2} \times \frac{4!}{2! 2!} = 3 \times 6 = 18$$

#### Final Answer
*(Translated from Bengali: এই তিনটা case যদি যোগ করি তাহলে ans পেয়ে যাবো — If we sum these three cases, we obtain the answer)*
$$\text{Total Arrangements} = \text{Case 1} + \text{Case 2} + \text{Case 3} = 360 + 360 + 18 = 738$$

---

<!-- Pages 39–40 (Single pages: Counting Principles & Pigeonhole Principle | 26.09.2026) -->

> [!NOTE] Chronological & Topical Placement Note
> Pages 39–40 (dated 26-09-2026) are placed here directly after Permutations (Pages 34–35) to maintain the continuity of the Combinatorics unit, before the final class review on Proof Methods (Pages 36–38, dated 28-09-2026).

### 6.3 Product Rule

If a procedure can be broken down into a sequence of $k$ tasks, where task $1$ can be done in $n_1$ ways, task $2$ in $n_2$ ways, etc., then the procedure can be done in $n_1 \times n_2 \times \dots \times n_k$ ways.

#### Application: Telephone Numbering Plan
- **Old Format**:
  $$\underbrace{[NYX]}_{\text{Area code (3)}} - \underbrace{[NNX]}_{\text{Office code (3)}} - \underbrace{[XXXX]}_{\text{Station code (4)}}$$
  Where:
  - $X \in \{0, 1, \dots, 9\}$ ($10$ choices)
  - $N \in \{2, 3, \dots, 9\}$ ($8$ choices)
  - $Y \in \{0, 1\}$ ($2$ choices)
  - Total old format numbers:
    $$(8 \times 2 \times 10) \times (8 \times 8 \times 10) \times (10^4) = 160 \times 640 \times 10,000 = 1.024 \times 10^9$$

- **New Format**:
  $$\underbrace{[NXX]}_{\text{Area code}} - \underbrace{[NXX]}_{\text{Office code}} - \underbrace{[XXXX]}_{\text{Station code}}$$
  - Total new format numbers:
    $$(8 \times 10 \times 10) \times (8 \times 10 \times 10) \times (10^4) = 800 \times 800 \times 10^4 = 6.4 \times 10^9$$

### 6.4 Sum Rule and Principle of Inclusion-Exclusion

- **Sum Rule**: If tasks are **mutually exclusive** (cannot be performed simultaneously; have no common elements):
  $$|A \cup B| = |A| + |B|$$
- **Principle of Inclusion-Exclusion**: If tasks are not disjoint:
  $$|A \cup B| = |A| + |B| - |A \cap B|$$

### 6.5 The Pigeonhole Principle (PHP)

If $N$ objects are placed into $k$ boxes, then at least one box contains at least:
$$\left\lceil \frac{N}{k} \right\rceil \text{ objects}$$

#### Problem 1: Students Born in the Same Month
> "How many students are required to guarantee that at least 5 students were born in the same month?"

<!-- Page 40 -->

**Solution**:
- Boxes $k = 12$ (12 months in a year).
- We want: $\lceil \frac{N}{12} \rceil \ge 5$.
- *(Translated from Bengali explanation)*: To find the minimum guaranteed number, consider the worst-case scenario where each month has at most $4$ students (one less than the target $5$):
  $$4 \times 12 = 48 \text{ students}$$
- Adding $1$ additional student guarantees by PHP that at least one month has $5$ students:
  $$\therefore \text{Required Students} = 48 + 1 = 49$$

#### Problem 2: University ID Generation
> "A university ID consists of two uppercase letters followed by 4 digits. Letters and digits may be repeated. However, IDs beginning with `AA` are reserved and cannot be assigned. How many valid IDs are possible?"

**Solution**:
- Structure: $\text{Letter} \times \text{Letter} \times \text{Digit} \times \text{Digit} \times \text{Digit} \times \text{Digit}$
- Total possible IDs with repetition allowed:
  $$26 \times 26 \times 10 \times 10 \times 10 \times 10 = 26^2 \times 10^4 = 6,760,000$$
- Reserved IDs starting with `AA`:
  $$1 \times 1 \times 10 \times 10 \times 10 \times 10 = 10,000$$
- **Valid IDs**:
  $$\text{Valid IDs} = 6,760,000 - 10,000 = 6,750,000 = 6.75 \times 10^6$$

> **Extension Question** *(translated from Bengali annotation: যদি থাকতো digit repeat হতে পারবে না, তাহলে কি হতো?)*:  
> What if digits were **NOT allowed to repeat**?  
> - Total IDs with non-repeating digits:
>   $$26 \times 26 \times P(10, 4) = 676 \times (10 \times 9 \times 8 \times 7) = 676 \times 5040 = 3,407,040$$
> - Reserved IDs starting with `AA`:
>   $$1 \times 1 \times P(10, 4) = 5040$$
> - Valid non-repeating IDs:
>   $$(676 - 1) \times 5040 = 675 \times 5040 = 3,402,000$$

---

## 7. Methods of Proof (Rosen 1.7 & 1.8)

<!-- Pages 36–37 (Dual spread: Methods of Proof & Final Class Review | 28.09.2026) -->

### 7.1 Mathematical Terminology

- **Theorem**: A mathematical statement that can be shown to be true using definitions, previously proven theorems, axioms, and rules of inference.
- **Proposition**: A less important or secondary theorem.
- **Lemma**: A simple "helping theorem" used in the proof of a larger theorem.
- **Corollary**: A theorem that follows directly from an already proven theorem.
- **Conjecture**: A statement proposed to be true that has neither been proven nor disproven.
  - *(Translated from Bengali)*: If a conjecture is proven true, it becomes a **Theorem**. If proven false, it is refuted.
- **Axiom / Postulate**: A basic underlying statement assumed to be true without proof.

### 7.2 Method 1: Direct Proof

To prove $p \to q$:
1. Assume $p$ is True.
2. Apply definitions and established algebraic truths.
3. Derive that $q$ must be True.

#### Example 1: Parity of $n^2$
> Prove: "If $n$ is odd, then $n^2$ is odd."

- **Hypothesis**: $n$ is odd.
- By definition of odd integers: $n = 2k + 1$ for some integer $k$.
- Compute $n^2$:
  $$n^2 = (2k + 1)^2 = 4k^2 + 4k + 1 = 2(2k^2 + 2k) + 1$$
- Let $r = 2k^2 + 2k \in \mathbb{Z}$.
- Then $n^2 = 2r + 1$, which is odd by definition. $\blacksquare$

#### Example 2: Sum of Two Even Integers
> Prove: "The sum of two even integers is even."

- Let $m = 2j$ and $n = 2k$ for integers $j, k$.
- $\text{Sum} = m + n = 2j + 2k = 2(j + k)$.
- Since $(j + k)$ is an integer, the sum is even. $\blacksquare$

---

<!-- Page 37 -->

### 7.3 Method 2: Proof by Contraposition (Indirect Proof)

To prove $p \to q$, we prove its logically equivalent contrapositive:
$$\neg q \to \neg p$$

*(Translated from Bengali note: $\neg q$ ধরতে হবে — You must assume the negation of the conclusion)*

#### Example: "If $n^2$ is odd, then $n$ is odd"
- Statement: $p \to q$, where $p: n^2 \text{ is odd}$, $q: n \text{ is odd}$.
- **Contrapositive**: $\neg q \to \neg p \implies$ "If $n$ is even, then $n^2$ is even."
- Assume $n$ is even $\implies n = 2k$ for some integer $k$.
- Compute $n^2$:
  $$n^2 = (2k)^2 = 4k^2 = 2(2k^2)$$
- Since $2k^2$ is an integer, $n^2$ is even.
- Since $\neg q \to \neg p$ is True, the original statement $p \to q$ is proved. $\blacksquare$

### 7.4 Method 3: Proof by Contradiction

To prove statement $p$:
1. Assume the negation $\neg p$ is True.
2. Show that this assumption leads to a contradiction ($r \land \neg r$).
3. Conclude that $\neg p$ is False, and therefore $p$ must be True.

*(Translated from Bengali note: $p$ থাকলে $\neg p$ কে false প্রমাণ করতে হবে)*

#### Classic Example: Prove that $\sqrt{3}$ is Irrational
- Assume $\neg p$: $\sqrt{3}$ is rational.
- Then $\sqrt{3}$ can be written as:
  $$\sqrt{3} = \frac{a}{b}, \quad a, b \in \mathbb{Z}, b \neq 0$$
  where $a$ and $b$ are **coprime** ($\gcd(a, b) = 1$, i.e., the fraction is in simplest form) *(translated from Bengali: পরস্পর সহমৌলিক হতে হবে: $a$ ও $b$, যাদের গ.সা.গু. $\gcd(a, b) = 1$)*.
- Squaring both sides:
  $$3 = \frac{a^2}{b^2} \implies a^2 = 3b^2$$
- This implies $3 \mid a^2$, which means $3 \mid a$.
- Since $3 \mid a$, we can write $a = 3k$ for some integer $k$.
- Substituting into the equation:
  $$(3k)^2 = 3b^2 \implies 9k^2 = 3b^2 \implies b^2 = 3k^2$$
- This implies $3 \mid b^2$, which means $3 \mid b$.
- Thus, $3$ divides both $a$ and $b$, which contradicts the assumption that $\gcd(a, b) = 1$.
- Therefore, the assumption that $\sqrt{3}$ is rational is False, proving $\sqrt{3}$ is **irrational**. $\blacksquare$

### 7.5 Method 4: Bidirectional Proofs ($p \leftrightarrow q$)

To prove a biconditional statement $p \leftrightarrow q$, you must prove both directions:
$$p \to q \quad \text{and} \quad q \to p$$

*(Translated from Bengali note: দুই direction থেকেই solve করতে হবে — Must solve from both forward and backward directions)*

#### Example: "An integer $n$ is odd if and only if $n^2$ is odd"
1. **Forward Direction ($p \to q$)**: If $n$ is odd, then $n^2$ is odd.  
   *(Proved directly: $n = 2k + 1 \implies n^2 = 2(2k^2 + 2k) + 1 \implies \text{odd}$)*.
2. **Backward Direction ($q \to p$)**: If $n^2$ is odd, then $n$ is odd.  
   *(Proved by contraposition: if $n$ is even, $n = 2k \implies n^2 = 2(2k^2) \implies \text{even}$)*.

---

<!-- Page 38 (Single page: Final Exam Preparation Suggestions) -->

## 8. Exam Suggestions & Question Weightage Pattern

*(Transcribed from class suggestions on Page 38)*

### 8.1 Chapter Question Weightage Breakdown
- **Propositional Logic** (Rosen 1.1, 1.2, 1.3, 1.4): Minimum **2 sets**
- **Number Theory**: Minimum **1 set – 1.5 sets**
- **Counting / Combinatorics**: Minimum **1 set – 1.5 sets**
- **Sets and Functions**: Minimum **0.5 set – 1 set**

### 8.2 High-Yield Exam Advice
- **Lecture slides are mandatory reading** *(translated from Bengali: slide পড়তেই হবে)*.
- **Natural language proposition translation practice**: Special focus on challenging connectors:
  - `"unless"`
  - `"however"`
  - `"until"`
