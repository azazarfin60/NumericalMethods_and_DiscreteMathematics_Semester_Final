# DM-5: Number Theory

> **Section:** Section B (Discrete Mathematics)  
> **Subtopics in this folder:** 9 files (DM-5.1 through DM-5.9)  
> **Exam weight:** Appears in 3/3 papers since discrete mathematics was added (100% exam frequency). Typically worth 10 to 14 marks per paper in Section B (regularly tested in Question 7 and Question 8).

---

## 📖 How to Read This Topic

Number theory is the study of integers and their properties. While it began as pure mathematical curiosity, modern computing turned it into the bedrock of computer engineering. Every digital communication, secure login, encryption protocol (like RSA), and computer arithmetic circuit relies directly on the principles in this folder.

In RUET examinations, number theory is high-yield. The exam problems are remarkably clean, predictable, and fast to solve once you understand the underlying machinery.

This entire topic follows a natural, cohesive progression:

1. **Foundations of Divisibility and Primes (DM-5.1, DM-5.2):**
   - **Divisibility (DM-5.1):** Understand factors, the Division Algorithm ($a = dq + r$), and the Fundamental Theorem of Arithmetic (unique prime factorization).
   - **Prime Numbers (DM-5.2):** Explore primality, composite bounds ($p \le \sqrt{n}$), and trial division limits.

2. **Greatest Common Divisors and Euclidean Machinery (DM-5.3):**
   - **GCD, LCM, and Euclidean Algorithms:** Compute greatest common divisors with Euclid's division identity. Master the Extended Euclidean Algorithm to find Bézout coefficients ($sa + tb = \gcd(a, b)$) using both back-substitution and tabular forward-shift methods.

3. **Modular Arithmetic Core (DM-5.4, DM-5.5):**
   - **Modular Arithmetic and Congruence (DM-5.4):** The most frequently tested topic in Section B. Learn to replace large variables with small residues before evaluating linear, quadratic, and cubic forms.
   - **Modular Exponentiation (DM-5.5):** Compute huge powers like $3^{644} \bmod 645$ using repeated squaring (binary exponentiation) in $O(\log n)$ operations instead of hopeless linear multiplications.

4. **Advanced Theorems (DM-5.6, DM-5.7):**
   - **Fermat's Little Theorem (DM-5.6):** Collapse powers modulo a prime ($a^{p-1} \equiv 1 \pmod p$).
   - **Chinese Remainder Theorem (DM-5.7):** Solve systems of simultaneous congruences with pairwise coprime moduli using both the construction formula and iterative substitution.

5. **Digital Representations and Proofs (DM-5.8, DM-5.9):**
   - **Number Bases and Binary Arithmetic (DM-5.8):** Convert between base 10 and base 2, and execute column-by-column binary addition with explicit carry management.
   - **Number-Theoretic Proofs (DM-5.9):** Learn the five-step framework to prove identities involving modular powers and Mersenne numbers like $(2^a - 1) \bmod (2^b - 1) \equiv 2^{a \bmod b} - 1$.

Read the subtopics in order from DM-5.1 to DM-5.9.

**Suggested reading time:** ~60 minutes for the entire folder.

---

## 📑 Subtopic Index

| # | File | Priority | Exam Frequency | Reading Time | Core Concept |
|:---:|:---|:---:|:---:|:---:|:---|
| 1 | [DM-5.1: Divisibility](DM-5.1_Divisibility.md) | ⚫ | Foundation (implicit) | ~6 min | Factors, division algorithm, unique prime factorization |
| 2 | [DM-5.2: Prime Numbers](DM-5.2_Prime_Numbers.md) | 🟠 | 1/3 papers (2023) | ~8 min | Prime divisor bound $p \le \sqrt{n}$, trial division, Euclid's lemma |
| 3 | [DM-5.3: GCD and Euclidean](DM-5.3_GCD_and_Euclidean.md) | 🟠 ⚠️ | 1/3 papers (2022) | ~10 min | Euclidean algorithm, Extended Euclidean, Bézout identity |
| 4 | [DM-5.4: Modular Arithmetic](DM-5.4_Modular_Arithmetic.md) | 🔴 | 3/3 papers (2022, 2023, 2024) | ~10 min | Congruence classes, substitution rule, linear and cubic forms |
| 5 | [DM-5.5: Modular Exponentiation](DM-5.5_Modular_Exponentiation.md) | 🔴 | 2/3 papers (2022, 2024) | ~10 min | Repeated squaring, binary expansion, intermediate reductions |
| 6 | [DM-5.6: Fermat's Little Theorem](DM-5.6_Fermats_Little_Theorem.md) | 🟡 | 1/3 papers (2022) | ~6 min | $a^{p-1} \equiv 1 \pmod p$, reducing exponents, pseudoprimes |
| 7 | [DM-5.7: Chinese Remainder Theorem](DM-5.7_Chinese_Remainder_Theorem.md) | 🟠 | 1/3 papers (2022) | ~10 min | CRT construction formula, modular inverses, unique solution mod $N$ |
| 8 | [DM-5.8: Number Bases](DM-5.8_Number_Bases.md) | 🟡 | 1/3 papers (2023) | ~7 min | Positional expansions, binary column addition, carry rows, bit overflow |
| 9 | [DM-5.9: Number Proofs](DM-5.9_Number_Proofs.md) | 🟠 | 2/3 papers (2022, 2023) | ~8 min | 5-step proof structure, division algorithm in exponents, bounding residues |

---

## 🎯 Exam Pattern for This Topic

In RUET semester final examinations, number theory questions consistently follow five standard archetypes:

### Pattern 1: Congruence Evaluation with Given Residues (3 to 4 Marks)
The most common question type in Section B (2022 Q.7(a), 2023 Q.7(a), 2024 Q.8(a)):
- Given residues of $a$ and $b$ modulo $m$ (such as $a \equiv 11, b \equiv 3 \pmod{19}$).
- Evaluate a linear expression like $7a + 3b \pmod{19}$ and a higher-degree expression like $a^3 + 4b^3 \pmod{19}$.
- Keep numbers small by substituting residues and reducing intermediates immediately.
- Report the unique representative $c$ satisfying $0 \le c \le m - 1$.

### Pattern 2: Fast Modular Exponentiation via Repeated Squaring (3 to 4 Marks)
Tested verbatim in both 2022 Q.7(b) and 2024 Q.8(b):
- "Solve $3^{644} \bmod 645$ using a well-known algorithm."
- Explicitly state the algorithm name: **repeated squaring** (or binary exponentiation).
- Write $644$ in binary: $(1010000100)_2$.
- Build the table of successive squarings modulo 645 and multiply the rows matching set bits.

### Pattern 3: Extended Euclidean Algorithm & Bézout Identity (2 to 3 Marks)
Tested in 2022 Q.7(c):
- Find the greatest common divisor of two integers (such as 414 and 662).
- Express the gcd as a linear combination $sa + tb = \gcd(a, b)$.
- Execute either reverse substitution or the forward recurrence table to find Bézout coefficients $s$ and $t$.

### Pattern 4: Fermat's Little Theorem and Chinese Remainder Theorem (4 Marks)
Tested in 2022 Q.8(a):
- Define Fermat's Little Theorem with its exact coprimality condition.
- Solve a system of simultaneous congruences with pairwise coprime moduli (such as $x \equiv 2 \pmod 3, x \equiv 1 \pmod 4, x \equiv 3 \pmod 5$).
- Compute $M_i = N/m_i$, find modular inverses $u_i$, evaluate the sum $\sum a_i u_i M_i$, and reduce modulo $N$.

### Pattern 5: Number-Theoretic Proofs and Binary Operations (2 to 3 Marks)
Tested in 2022 Q.7(d) and 2023 Q.7(b), Q.7(c):
- Binary column addition with full carry row and verification via decimal positional values.
- Direct proof of composite prime divisor bound $p \le \sqrt{n}$.
- Modular identity proof $(2^a - 1) \bmod (2^b - 1) \equiv 2^{a \bmod b} - 1$ using the division algorithm.

---

## 🔗 Topic Connections

- **Prerequisites:**
  - [DM-4.2: Direct Proofs](../DM-4_Proof_Techniques/DM-4.2_Direct_Proofs.md) -- prime divisor and modular proofs use direct and contradiction proof structures.
  - [DM-4.5: Mathematical Induction](../DM-4_Proof_Techniques/DM-4.5_Mathematical_Induction.md) -- inductive arguments justify exponent reduction and division theorems.
- **Leads directly to:**
  - [DM-6.1: Basic Counting Techniques](../DM-6_Counting/DM-6.1_Sum_and_Product_Rules.md) -- counting residue classes and divisibility distributions.
  - [DM-6.3: Pigeonhole Principle](../DM-6_Counting/DM-6.3_Pigeonhole_Principle.md) -- remainder grouping and modular pigeonhole applications.
- **Pairs with in exams:**
  - Regularly forms the bulk of Question 7 and Question 8 in Section B, often sharing question parts with counting principles or logic proofs.
