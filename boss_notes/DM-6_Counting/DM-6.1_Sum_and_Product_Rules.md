[← DM-5.9: Number Proofs](../DM-5_Number_Theory/DM-5.9_Number_Proofs.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: DM-6.2 Inclusion-Exclusion →](DM-6.2_Inclusion_Exclusion.md)

---

# DM-6.1: Sum and Product Rules

> 🟠 **Priority:** Secondary | **Tested:** 2022 Q.8(b) | **Typical marks:** 2

## What This Is (and Why It Matters)

Whenever you solve an engineering counting problem, you are choosing between two fundamental questions: do these actions happen one after another, or do they happen instead of each other?

If a process consists of a sequence of successive stages (first pick $A$, and then pick $B$), you multiply their options using the product rule. If a process presents mutually exclusive alternatives (either pick from menu $A$, or pick from menu $B$), you add their options using the sum rule. In the RUET semester final, the exam gives you a story problem and expects you to name the rule, explain why the alternative rule does not apply, and state the exact count.

---

## 📝 Key Definitions

> **Product rule:** "Suppose that a procedure can be broken down into a sequence of two tasks. If there are $n_1$ ways to do the first task and for each of these ways of doing the first task, there are $n_2$ ways to do the second task, then there are $n_1n_2$ ways to do the procedure." (Rosen, §6.1, p. 2)
>
> **In simple words:** If you do step 1 and then step 2, multiply the number of choices for step 1 by the number of choices for step 2.

> **Sum rule:** "If a task can be done either in one of $n_1$ ways or in one of $n_2$ ways, where none of the set of $n_1$ ways is the same as any of the set of $n_2$ ways, then there are $n_1 + n_2$ ways to do the task." (Rosen, §6.1, p. 5)
>
> **In simple words:** If you choose between two separate options that cannot happen at the same time and share zero common choices, add the numbers together.

> **Division rule:** "There are $n/d$ ways to do a task if it can be done using a procedure that can be carried out in $n$ ways, and for every way $w$, exactly $d$ of the $n$ ways correspond to way $w$." (Rosen, §6.1, p. 9)
>
> **In simple words:** If your counting method accidentally produces every real outcome $d$ times, divide your total by $d$ to get the true count.

---

## The Core Idea

When reading an exam problem, ask two simple diagnostic questions:

1. **Do the actions happen in sequence, or as alternatives?**
   - Sequential ("and then", "via", "followed by"): Apply the **product rule**.
   - Alternatives ("either... or", "one of"): Apply the **sum rule**.

2. **Do the alternative groups share any common elements?**
   - Disjoint (zero overlap): The sum rule gives the exact total.
   - Overlapping (shared cases): Simple addition overcounts, requiring subtraction of the overlap.

### The Product Rule

For two sequential tasks, where the choices in the second task do not depend on the specific choice made in the first:

$$
\text{Total Ways} = n_1 \times n_2
$$

When a procedure extends to a sequence of $m$ consecutive tasks:

$$
\text{Total Ways} = n_1 \cdot n_2 \cdots n_m
$$

The critical requirement is that the number of ways to perform each subsequent task remains constant, regardless of which specific choice was made in earlier tasks.

### The Sum Rule

When a task can be performed by choosing from $m$ mutually exclusive sets of ways:

$$
\text{Total Ways} = n_1 + n_2 + \dots + n_m
$$

The mathematical condition is that the sets must be **pairwise disjoint**. If even a single outcome belongs to two sets simultaneously, simple addition will overcount.

### The Division Rule

The division rule comes into play when an easy counting procedure produces symmetrical duplicates. If each distinct outcome appears exactly $d$ times in your count:

$$
\text{Distinct Outcomes} = \frac{n}{d}
$$

For example, when arranging 4 people around a circular table, there are $4! = 24$ linear seating orders. But rotating everyone by 1, 2, or 3 positions yields the same relative circular arrangement. Each unique circular seating is generated $d = 4$ times, giving $24 / 4 = 6$ distinct circular seatings.

---

## 🔧 Classic Worked Examples from Rosen

### Example 1: License Plates (Product Rule)
A state issues license plates consisting of 3 uppercase English letters followed by 3 decimal digits.
- Choosing the letters: $26 \times 26 \times 26 = 26^3 = 17{,}576$ ways.
- Choosing the digits: $10 \times 10 \times 10 = 10^3 = 1{,}000$ ways.
- By the product rule, the total number of distinct license plates is:

$$
26^3 \times 10^3 = 17{,}576{,}000
$$

### Example 2: Counting Functions (Product Rule)
How many distinct functions exist from a set with $m$ elements to a set with $n$ elements?
- For each of the $m$ elements in the domain, we must choose one of the $n$ available targets in the codomain.
- This creates a sequence of $m$ independent decisions, each having $n$ choices:

$$
\underbrace{n \times n \times \dots \times n}_{m \text{ times}} = n^m
$$

### Example 3: Telephone Numbering Plan (Product Rule)
In the North American Numbering Plan, telephone numbers have 10 digits: a 3-digit area code, a 3-digit central office code, and a 4-digit station number.
- Under the traditional format $NYX\text{-}NNX\text{-}XXXX$ (where $N \in \{2,\dots,9\}$, $Y \in \{0,1\}$, and $X \in \{0,\dots,9\}$):
  - Area code choices: $8 \times 2 \times 10 = 160$
  - Office code choices: $8 \times 8 \times 10 = 640$
  - Station number choices: $10^4 = 10{,}000$
  - Total numbers: $160 \times 640 \times 10{,}000 = 1{,}024{,}000{,}000$
- Under the modern format $NXX\text{-}NXX\text{-}XXXX$:
  - Area code choices: $8 \times 10 \times 10 = 800$
  - Office code choices: $8 \times 10 \times 10 = 800$
  - Station number choices: $10^4 = 10{,}000$
  - Total numbers: $800 \times 800 \times 10{,}000 = 6{,}400{,}000{,}000$

---

## 🏆 Past Exam Questions

### 2022 Q.8(b): Boston to Los Angeles via Detroit [02 Marks]

> **The Question:** There are four major auto routes from Boston to Detroit and six from Detroit to Los Angeles. How many major auto routes are there from Boston to Los Angeles via Detroit?

**Let's solve this step by step like a tutor:**

First, look at the physical journey described in the problem. The traveler is going from Boston to Los Angeles, but they **must pass through Detroit**.

This means completing the journey requires two mandatory, successive stages:
1. **Leg 1:** Travel from Boston to Detroit (4 route choices available).
2. **Leg 2:** Travel from Detroit to Los Angeles (6 route choices available).

Because every complete route is formed by picking one choice for Leg 1 **and then** one choice for Leg 2, the choices are sequential. They do not substitute for one another.

Therefore, this problem is governed by the **product rule** (multiplication principle):

$$
\text{number of routes} = 4 \times 6
$$

$$
\boxed{24 \text{ routes}}
$$

**Quick sanity check:**
If you make a grid listing the 4 routes from Boston along the rows and the 6 routes from Detroit along the columns, you obtain a $4 \times 6$ table containing 24 distinct cells. Each cell corresponds to one unique route from Boston to Los Angeles.

> [!NOTE] Why the Sum Rule Does Not Apply
> The sum rule applies only when choices are mutually exclusive alternatives: for instance, if a traveler could go from Boston to Los Angeles *either* via Detroit *or* via Chicago, never visiting both. In this problem, Detroit is a mandatory waypoint on the path. The legs occur in series, not in parallel.

> [!WARNING] Why Permutations Do Not Apply
> A route is completely determined once Leg 1 and Leg 2 are selected. The geographic sequence is fixed: Boston first, Detroit second, Los Angeles third. Reordering the legs is physically impossible, so this is a product-of-choices count, not an arrangement count.

---

## ⚡ Quick Review

**The method in one sentence:** Use the product rule when actions happen in sequence ("and then"); use the sum rule when actions are disjoint alternatives ("either/or").

**The formulas you must memorize:**
$$
\text{Product Rule: } \text{Total} = n_1 \times n_2 \qquad \text{Sum Rule: } \text{Total} = n_1 + n_2
$$

**The most common exam mistake:** Forgetting to state the rule name explicitly. Always write "By the product rule" or "By the sum rule" before writing the calculation to secure full method marks.

**Time estimate in exam:** 2 to 3 minutes for a 2-mark question.

---

## 🔗 Connected Topics

- [← DM-5.9: Number Proofs](../DM-5_Number_Theory/DM-5.9_Number_Proofs.md): Completes the number theory section.
- [→ DM-6.2: Inclusion-Exclusion](DM-6.2_Inclusion_Exclusion.md): Extends the sum rule to sets that have non-empty overlap.
- [DM-6.4: Permutations](DM-6.4_Permutations.md): Uses the product rule repeatedly without replacement to derive factorials.

---

[← DM-5.9: Number Proofs](../DM-5_Number_Theory/DM-5.9_Number_Proofs.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: DM-6.2 Inclusion-Exclusion →](DM-6.2_Inclusion_Exclusion.md)
