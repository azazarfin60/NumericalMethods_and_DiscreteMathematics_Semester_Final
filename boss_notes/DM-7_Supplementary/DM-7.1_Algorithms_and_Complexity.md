[← Previous: DM-6.6 Binomial Theorem](../DM-6_Counting/DM-6.6_Binomial_Theorem.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: DM-7.2 Relevance of Discrete Mathematics →](DM-7.2_Relevance_of_DM.md)

---

# DM-7.1: Algorithms and Complexity

> 🟡 📘 **Priority:** Secondary (Off-Syllabus, but Examined) | **Tested:** 1/3 DM papers (2024 Q.7(a)) | **Typical marks:** 6

## What This Is (and Why It Matters)

Imagine your boss asks you to build a package delivery system. You must sort addresses by distance, look up customer records by ID, and assign vans to the closest houses. How do you choose the right tools for the job? How do you prove your code will not freeze when user orders jump from ten to ten thousand?

This is what algorithms and complexity theory are all about. An algorithm is a step-by-step recipe that solves a problem. Complexity theory tells you how the run time and memory scale as input data grows.

Here is the twist: this topic is not listed in the official written syllabus (`ECE2213_Syllabus.md`). That is why it carries the 📘 flag. Yet in 2024, Question 7(a) asked a complete 6-mark design problem on sorting, binary search, greedy scheduling, and Big-O run times. Six marks is a huge haul in Discrete Mathematics. Preparing this topic gives you an easy, reliable scoring advantage.

---

## 📝 Key Definitions

> **Algorithm:** "An **algorithm** is a finite sequence of precise instructions for performing a computation or for solving a problem." -- Rosen, §3.1 (p. 1)
>
> **In simple words:** A step-by-step recipe with clear, unambiguous instructions that takes an input, finishes in a finite number of steps, and gives the correct answer.

> **Greedy algorithm:** "This approach selects the best choice at each step, instead of considering all sequences of steps that may lead to an optimal solution. Algorithms that make what seems to be the 'best' choice at each step are called **greedy algorithms**." -- Rosen, §3.1 (p. 8)
>
> **In simple words:** An algorithm that always grabs the immediate, locally best option right in front of it without looking ahead or second-guessing its past choices.

> **Big-O notation:** "Let $f$ and $g$ be functions from the set of integers or the set of real numbers to the set of real numbers. We say that $f(x)$ is $O(g(x))$ if there are constants $C$ and $k$ such that $|f(x)| \le C|g(x)|$ whenever $x > k$." -- Rosen, §3.2 (p. 15)
>
> **In simple words:** An upper speed limit on how fast a function grows. It means that past some starting threshold $k$, the curve $f(x)$ never climbs above a constant multiple $C$ of $g(x)$.

> **The witnesses ($C$ and $k$):** "To establish that $f(x)$ is $O(g(x))$ we need only find one pair of each of witnesses $C$ and $k$. That is, to show that $f(x)$ is $O(g(x))$, we need only find a pair of constants $C$ and $k$, the witnesses, such that $|f(x)| \le C|g(x)|$ whenever $x > k$." -- Rosen, §3.2 (p. 15)
>
> **In simple words:** The two specific numbers that prove your Big-O bound is true. $k$ is where you start looking, and $C$ is the scaling factor that keeps $C \cdot g(x)$ on top.

> **Time complexity (worst, average, best):** "The **worst-case** time complexity of an algorithm is the maximum number of operations used by the algorithm to solve a problem with input of a given size. The **average-case** time complexity of an algorithm is the average number of operations used by the algorithm to solve a problem with input of a given size, assuming some probability distribution on the input values. The **best-case** time complexity of an algorithm is the minimum number of operations used by the algorithm to solve a problem with input of a given size." -- Rosen, §3.3 (p. 29)
>
> **In simple words:** Worst-case is how slow the code runs on the nastiest possible input. Average-case is how it runs on typical daily input. Best-case is how fast it finishes when you get lucky.

> **Space complexity:** "A second measure of the efficiency of an algorithm is the amount of computer memory required by the algorithm to solve a problem, when input values are of a specified size." -- Rosen, §3.3 (p. 28)
>
> **In simple words:** How much extra scratchpad memory or RAM the algorithm needs to do its work.

> **Tractable and intractable problems:** "A problem that is solvable using an algorithm with polynomial worst-case complexity is called **tractable**." / "Such problems are called **intractable**." -- Rosen, §3.3 (p. 36)
>
> **In simple words:** Tractable problems can be solved in reasonable time by a computer using polynomial steps like $O(n^2)$. Intractable problems take exponential time like $O(2^n)$, making realistic inputs take centuries to finish.

![Graph of f(x) against g(x) showing the region where f(x) stays below the multiple C times g(x) for all x past the threshold k. Past k the curve f(x) is bounded above by the curve Cg(x). Rosen §3.2 Figure 2, p. 18](../diagrams/dm7_big_o_definition_witnesses.jpg)

*Figure: The function $f(x)$ is $O(g(x))$. Notice that to the left of $k$, the curves can cross. Big-O only cares about the tail behavior to the right of $k$.*

---

## The Core Idea

### The Seven Properties of an Algorithm

Rosen outlines seven properties that turn an ordinary procedure into a mathematical algorithm (§3.1, p. 3). If an exam asks "What are the properties of an algorithm?", list these seven:

| Property | Meaning in Plain Words |
| :-- | :-- |
| **Input** | It takes input values from a clearly defined set. |
| **Output** | It produces solution values for each set of inputs. |
| **Definiteness** | Every single step is clearly and precisely defined. |
| **Correctness** | It produces the right answer for every valid input. |
| **Finiteness** | It halts after a finite number of operations. It never loops forever. |
| **Effectiveness** | Each step can be carried out exactly in a finite amount of time. |
| **Generality** | It works on all problems of the desired form, not just one lucky instance. |

### Big-O Stated Properly: Finding Witnesses

When you write the formal definition of Big-O in an exam, write this exact inequality:

$$
|f(x)| \le C\,|g(x)| \qquad \text{for all } x > k
$$

Keep these three key facts in mind:
1. **$C$ and $k$ are fixed constants.** They do not change as $x$ grows.
2. **The rule only applies for $x > k$.** Big-O is an asymptotic bound. It ignores what happens for tiny inputs.
3. **One valid pair of witnesses is enough.** You do not need to find the absolute tightest $C$ or smallest $k$. Any working pair $(C, k)$ proves the statement.

#### Example: Witness Hunting (Rosen §3.2, p. 16)

Show that $f(x) = x^2 + 2x + 1$ is $O(x^2)$.

Let us look at $x > 1$. When $x > 1$, we know that $x < x^2$ and $1 < x^2$. So we can replace each term:

$$
x^2 + 2x + 1 \le x^2 + 2x^2 + x^2 = 4x^2
$$

So for all $x > 1$, we have $|f(x)| \le 4x^2$.  
Our witnesses are simply $C = 4$ and $k = 1$. This proves $f(x) = O(x^2)$.

### The Growth of Functions Hierarchy

![Six curves plotted against input size n, from bottom to top: 1, log n, n, n log n, n squared, 2 to the n, and n factorial. The gap between each pair widens as n grows. Rosen §3.3, p. 36](../diagrams/dm7_growth_of_functions_curves.jpg)

*Figure: Growth of common functions. As $n$ grows, the curves separate dramatically.*

The table below summarizes the standard complexity classes from Rosen Table 1 (§3.3, p. 36). Memorize this order:

| Complexity | Name | Practical Efficiency Verdict |
| :-- | :-- | :-- |
| $\Theta(1)$ | Constant | Ideal. A fixed number of CPU operations. |
| $\Theta(\log n)$ | Logarithmic | Super fast. Cuts the problem down exponentially (binary search). |
| $\Theta(n)$ | Linear | Fast. Touches every element once (linear scan). |
| $\Theta(n \log n)$ | Linearithmic | Excellent for sorting. The gold standard for comparison sorts (merge sort). |
| $\Theta(n^b)$, $b \ge 1$ | Polynomial | Tractable. Good when $b$ is small ($n^2, n^3$), but gets slow as $b$ grows. |
| $\Theta(b^n)$, $b > 1$ | Exponential | Intractable. Explodes rapidly. Only tiny inputs can run. |
| $\Theta(n!)$ | Factorial | Intractable. Exhaustive search over all permutations. Fails past small $n$. |

### Sorting and Searching Comparison

When a question asks you to choose an algorithm, use this master comparison table to justify your choice:

| Algorithm | Best Time | Average Time | Worst Time | Space | Sorted Input Needed? | Stable? |
| :-- | :-: | :-: | :-: | :-: | :-- | :-- |
| **Bubble sort** | $O(n)$ | $O(n^2)$ | $O(n^2)$ | $O(1)$ | No | Yes |
| **Insertion sort** | $O(n)$ | $O(n^2)$ | $O(n^2)$ | $O(1)$ | No | Yes |
| **Merge sort** | $O(n \log n)$ | $O(n \log n)$ | $O(n \log n)$ | $O(n)$ | No | Yes |
| **Quicksort** | $O(n \log n)$ | $O(n \log n)$ | $O(n^2)$ | $O(\log n)$ | No | No |
| **Heapsort** | $O(n \log n)$ | $O(n \log n)$ | $O(n \log n)$ | $O(1)$ | No | No |
| **Linear search** | $O(1)$ | $O(n)$ | $O(n)$ | $O(1)$ | No | N/A |
| **Binary search** | $O(1)$ | $O(\log n)$ | $O(\log n)$ | $O(1)$ | **Yes (Crucial)** | N/A |

#### Key Takeaways for the Exam

1. **Why pick Merge Sort?** Merge sort guarantees $O(n \log n)$ in the worst case. Quicksort can degrade to $O(n^2)$ if the array is already sorted and you pick a bad pivot. Merge sort is also stable, meaning items with equal values stay in their original relative order. The only trade-off is that it uses $O(n)$ extra memory.
2. **Binary Search has one strict rule:** The input list **must already be sorted** on the key you are searching for. If the list is sorted by delivery distance, you cannot use binary search to look up a customer by ID.

### How to Derive Complexities by Counting Operations

Do not just memorize Big-O numbers. You can derive them by counting operations:

- **Merge sort:** A list of size $n$ splits in half repeatedly until lists have size 1. This tree has $\lceil \log_2 n \rceil$ levels. At each level, merging the sublists takes $n$ comparisons. Multiplying levels by work per level gives $n \log_2 n$ operations, or $O(n \log n)$.
- **Binary search:** Each comparison cuts the search interval in half: $n, n/2, n/4, \dots, 1$. After $s$ steps, we have $n/2^s = 1$, which gives $s = \log_2 n$. So binary search needs at most $\lceil \log_2 n \rceil$ comparisons, or $O(\log n)$.
- **Linear search:** In the worst case, the target item is at the very end or absent. You must check all $n$ items, giving $n$ comparisons, or $O(n)$.
- **Greedy nearest-neighbor scan:** For $V$ vans and $A$ addresses, each van searches through remaining unserved addresses. That is $A + (A-1) + \dots + 1 = A(A+1)/2$ distance checks per van, which is $O(A^2)$. Across $V$ vans, this gives $O(V \cdot A^2)$.

### Greedy Algorithms: Power and Limitations

A greedy algorithm makes the best local choice right now and never turns back.

#### When Greedy Works
Greedy algorithms find the true global optimum when the problem has optimal substructure and the greedy-choice property. A great example is finding minimum spanning trees (Kruskal or Prim) or Huffman coding.

#### When Greedy Fails: Counterexample
Rosen presents a classic change-making example (§3.1, p. 8). Suppose you must make 30 cents using quarters (25¢), dimes (10¢), and pennies (1¢), with no nickels:
- The greedy approach picks the largest coin first: one quarter (25¢), leaving 5¢. Then it must take five pennies (1¢ each). Total = 6 coins.
- But picking three dimes ($10¢ + 10¢ + 10¢ = 30¢$) gives the same total in only 3 coins.
- Here greedy made the locally best choice (the quarter) but failed to find the globally optimal solution.

> [!WARNING] Common Exam Trap: The Binary Search Key
> When a problem asks to sort by distance and then search by customer ID, watch out.
> Sorting addresses by distance does not sort them by customer ID. Binary search will fail silently if you run it on the wrong key. Mentioning this distinction in your answer shows real engineering understanding and earns top marks.

---

## 🔧 Worked Example & 🏆 Past Exam Questions

### 2024 Q.7(a): Logistics System Algorithms & Complexity [06 marks]

> **The Question:**  
> A delivery company uses a computer system to manage customer orders. The system needs to perform the following tasks efficiently:
> - Sort all delivery address based on distance from warehouse.
> - Search for a customer's order by name or ID.
> - Use Greedy approach to assign delivery vans to the nearest unserved address.
> - Evaluate the time complexity of each algorithm used.
>
> (i) Which sorting algorithm would you choose to arrange delivery address efficiently? Write its name and state of average time complexity.  
> (ii) If the address list is already sorted, which search algorithm should be used? Write its pseudocode and time complexity.  
> (iii) Explain how a Greedy algorithm can be applied to assign vans to nearest delivery points.

#### Let's solve this step by step.

This question tests three separate algorithmic concepts and asks for time complexity evaluations on each.

#### Part (i): Sorting Addresses by Distance

**Algorithm chosen: Merge Sort.**

We need to sort addresses on a single numerical key: distance from the warehouse. Merge sort uses the divide-and-conquer paradigm. It divides the array in half, sorts each half recursively, and merges the two sorted halves in linear time.

- **Average time complexity:** $O(n \log n)$
- **Best-case time complexity:** $O(n \log n)$
- **Worst-case time complexity:** $O(n \log n)$
- **Space complexity:** $O(n)$

**Why Merge Sort over the alternatives:**
- **Bubble sort** takes $O(n^2)$ time, which crawls to a halt for thousands of customer deliveries.
- **Quicksort** has an average time of $O(n \log n)$, but degrades to $O(n^2)$ if the array is already sorted or nearly sorted. A delivery list updated through the day often arrives partially sorted.
- **Heapsort** runs in $O(n \log n)$ and takes $O(1)$ space, but it is not stable. Equal distances would lose their original order.
- **Counting / Radix sort** can run in linear time $O(n + k)$, but only works on integers. Delivery distances are real numbers with decimals.

Merge sort is the safest choice because its worst-case run time matches its average case. A logistics system with delivery deadlines can depend on this guarantee.

#### Part (ii): Searching for a Customer's Order

**Algorithm chosen: Binary Search.**

Since the address list is already sorted, binary search is the optimal choice.

**Pseudocode:**

```
function BINARY-SEARCH(A, key):
    low  <- 0
    high <- length(A) - 1
    while low <= high:
        mid <- floor((low + high) / 2)
        if A[mid].id = key:
            return mid
        else if A[mid].id < key:
            low <- mid + 1
        else:
            high <- mid - 1
    return NOT-FOUND
```

- **Average time complexity:** $O(\log n)$
- **Best-case time complexity:** $O(1)$ (when the target item sits right at the first midpoint)
- **Worst-case time complexity:** $O(\log n)$
- **Space complexity:** $O(1)$ (iterative version)

Binary search halves the search window on every iteration. For an address book with $n = 1{,}000{,}000$ entries, it finds any record in at most $\lceil \log_2(10^6) \rceil = 20$ comparisons. A linear search would need up to $1{,}000{,}000$ comparisons.

> [!NOTE] Practical Search Key Note
> Binary search requires the list to be sorted on the searched key. If the array is sorted by distance, searching by customer ID requires either a second index sorted by ID or a hash table ($O(1)$ lookup). Proposing binary search assumes an index sorted by ID is available.

#### Part (iii): Greedy Approach to Assign Vans

**Algorithm: Nearest-Neighbor Greedy Heuristic.**

At each step, look at the unassigned addresses, pick the address closest to the current van, assign the delivery, and repeat.

**Pseudocode:**

```
function GREEDY-ASSIGN(addresses, vans):
    served <- {}
    for each van in vans:
        current_pos <- warehouse_location
        while unserved addresses remain and van has capacity:
            best <- unserved address with minimum distance from current_pos
            assign best to van
            add best to served
            current_pos <- location of best
    return assignment
```

**Complexity Analysis:**
- If we pre-sort $n$ addresses by distance from the warehouse, sorting costs $O(n \log n)$.
- For $m$ vans and $n$ addresses, matching each van to nearby unserved addresses takes $O(nm)$ steps in the straightforward scan.
- Overall time complexity: $O(n \log n + nm)$.
- Space complexity: $O(n + m)$ to store assignments and served sets.

**Why Greedy Works Here:**
Every delivery costs fuel and driving distance. Minimizing the distance to the next immediate delivery point provides a fast, practical route that is close to optimal in practice.

**Where Greedy Can Fall Short:**
The true optimal route is the Travelling Salesperson Problem (TSP) / Vehicle Routing Problem, which is NP-hard. A simple greedy approach can get trapped if a van fills its capacity on small nearby packages, forcing a second van to make a long drive to serve a heavy package nearby. However, as an efficient heuristic, greedy runs fast and delivers practical solutions.

$$
\boxed{\text{Sort } O(n \log n), \quad \text{search } O(\log n), \quad \text{assign } O(n \log n + nm)}
$$

---

## 📊 Exam Variants at a Glance

| Year | What They Asked | Key Complexity Answer |
| :-- | :-- | :-- |
| **2024 Q.7(a)** | Delivery system: sort, search, greedy assignment, time complexity evaluation | $\boxed{\text{Sort } O(n \log n), \quad \text{search } O(\log n), \quad \text{assign } O(n \log n + nm)}$ |

---

## ⚡ Quick Review

**The method in one sentence:** Algorithms provide structured, finite steps to solve computational problems, and Big-O notation gives an upper bound on their running time and space as inputs grow.

**The formula to memorize (Big-O definition):**
$$
|f(x)| \le C\,|g(x)| \qquad \text{for all } x > k
$$

**The most common exam mistakes:**
1. Forgetting that binary search requires the list to be sorted specifically on the search key.
2. Quoting Quicksort's worst-case time as $O(n \log n)$ instead of $O(n^2)$.
3. Omitting the space complexity when evaluating algorithm efficiency.

**Time estimate in exam:** 12 to 15 minutes for a full 6-mark scenario question like 2024 Q.7(a).

---

## 🔗 Connected Topics

- [← DM-6.6: Binomial Theorem](../DM-6_Counting/DM-6.6_Binomial_Theorem.md) -- counting combinations provides the mathematical foundation for counting algorithmic operations.
- [→ DM-7.2: Relevance of Discrete Mathematics](DM-7.2_Relevance_of_DM.md) -- explains why discrete structures, logic, and counting are the foundational language of algorithm design.
- [DM-3.9: Rules of Inference](../DM-3_Propositional_Logic/DM-3.9_Rules_of_Inference.md) -- formal logic rules used to prove algorithm correctness.
- [DM-5.5: Modular Exponentiation](../DM-5_Number_Theory/DM-5.5_Modular_Exponentiation.md) -- an example of an efficient $O(\log n)$ algorithm in cryptography.

---

[← Previous: DM-6.6 Binomial Theorem](../DM-6_Counting/DM-6.6_Binomial_Theorem.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: DM-7.2 Relevance of Discrete Mathematics →](DM-7.2_Relevance_of_DM.md)
