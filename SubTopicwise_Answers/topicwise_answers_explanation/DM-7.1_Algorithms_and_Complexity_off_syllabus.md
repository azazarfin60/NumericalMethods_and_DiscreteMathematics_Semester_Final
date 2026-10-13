---
title: "DM-7.1 · Algorithms & Complexity"
tags:
  - numerical-methods
  - discrete-mathematics
  - topicwise
---



[🏠 Subtopic Index](00_Index.md) | [← Prev: DM-6.6 Binomial Theorem](DM-6.6_Binomial_Theorem.md) | [Next: DM-7.2 Relevance of Discrete Mathematics →](DM-7.2_Relevance_of_Discrete_Mathematics.md)

---

# DM-7.1 · Algorithms & Complexity

Every block below is copied from `../answers_explanation/`. The reasoning
is written once, in the year-wise file, and is not restated here.


### [2024 Q.7(a)]

**Question.** A delivery company uses a computer system to manage customer orders. Sort all delivery addresses based on distance from the warehouse. Search for a customer's order by name or ID. Use a greedy approach to assign delivery vans to the nearest unserved address. Evaluate the time complexity of each algorithm used.

*[Marks: 06, CO: 2]*

**Solution.**

This is three algorithmic tasks plus a complexity analysis for each. The tasks are
independent, and each one has a natural choice whose justification is what the
marks are for.

**(i) Sorting the addresses by distance.**

**Algorithm chosen: merge sort.** The addresses are sorted on a single numeric
key, the distance from the warehouse. Merge sort divides the list in half, sorts
each half recursively, and merges the two sorted halves in linear time.

- Average time complexity: $O(n \log n)$
- Best case: $O(n \log n)$
- Worst case: $O(n \log n)$
- Space: $O(n)$

**Why merge sort and not the others.**

- **Bubble sort** is $O(n^2)$, which fails at tens of thousands of addresses, and
  a delivery list over a few years is comfortably in that range.
- **Quicksort** is $O(n \log n)$ on average but $O(n^2)$ if the list is already
  sorted, which is close to what a distance list looks like. That worst case is
  avoidable with a random pivot, but the guarantee is not there by default.
- **Heapsort** is $O(n \log n)$ in all cases and $O(1)$ space, but it is not
  stable, and equal distances would lose their original order.
- **Counting or radix sort** would be faster at $O(n + k)$, but only if the
  distances are integers in a known range, which floating-point distances are
  not.

Merge sort's selling point here is that its worst case equals its average case,
so a delivery system with a hard deadline can rely on it. The cost is $O(n)$
extra space.

**(ii) Searching for a customer's order.**

**Algorithm chosen: binary search**, since the list is already sorted from step
(i).

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

- Average time complexity: $O(\log n)$
- Best case: $O(1)$, when the key sits at the first midpoint tried
- Worst case: $O(\log n)$
- Space: $O(1)$, since it iterates rather than recurses

Binary search halves the search interval at every step, so $n$ items need at
most $\lceil \log_2 n \rceil$ comparisons. For $n = 10^6$ that is 20 comparisons
against $10^6$ for a linear scan, which is the whole reason sorting is worth
doing once if many searches follow.

> [!warning] Binary search has one requirement
> The list must be sorted on the **same key** that is searched. Sorted by
> distance does **not** mean sorted by customer ID. Searching by ID requires
> either a second, ID-sorted index or a hash table. A hash table is the better
> answer for lookup by ID, at $O(1)$ average and $O(n)$ space, and this is the
> honest answer if the question allows more than one structure. The trap is to
> propose binary search on the distance-sorted list, which cannot find by ID.

**(iii) Assigning vans greedily.**

**Algorithm: nearest-neighbour greedy.** Scan the unserved addresses, take the
closest one, assign it, mark it served, and repeat.

```
function GREEDY-ASSIGN(addresses, vans):
    served <- {}
    for each van:
        current <- warehouse position
        while an unserved address remains and the van has capacity:
            best <- the unserved address nearest to current
            assign best to this van
            add best to served
            current <- position of best
    return assignment
```

- Time complexity: $O(V \cdot A)$ in the straightforward form, where $V$ is the
  number of vans and $A$ the number of addresses
- Space: $O(A)$

$$\boxed{\text{Sort } O(n \log n), \quad \text{search } O(\log n), \quad \text{assign } O(n \log n + nm)}$$

**The complexity analysis.** The outer loop runs $V$ times. For each van, the
inner loop scans the unserved list to find the nearest, and it does so once per
assigned address, giving $A$ scans in the worst case, each of cost $O(A)$ if the
list is not indexed. So the total is $O(V \cdot A^2)$ in the worst case, or
$O(A^2)$ when the number of vans is proportional to the address count. Using a
spatial index, a $k$-d tree or a grid hash, reduces the nearest-neighbour query
to $O(\log A)$, giving $O(V A \log A)$.

**Why greedy here, and what it costs.** Greedy is $O(VA^2)$ and simple, and for
a delivery list it is close to optimal in practice. It does **not** guarantee the
shortest total route, which is the travelling salesman problem and is NP-hard.
The bound is that greedy's tour is at most $O(\log A)$ times the optimal tour in
the worst case, and in practice it lands within a few percent. Since the exam
asks for a greedy approach, the answer is the nearest-neighbour construction with
its complexity stated, plus the note that it is a heuristic.

> [!info] Check the complexity by counting operations
> For $n$ items, merge sort performs about $n \log_2 n$ comparisons: $\log_2 n$
> levels, each doing a linear merge of $n$ items. Binary search does at most
> $\lceil \log_2 n \rceil$ comparisons, and the bound is tight when the key is
> absent. The greedy scan does one comparison per unserved address per assignment,
> so $A + (A-1) + \cdots + 1 = A(A+1)/2$ comparisons per van, which is $O(A^2)$,
> giving $O(VA^2)$ overall. These counts are what makes the table above more
> than a set of labels: each one can be derived by counting what the algorithm
> actually does, and the three agree with the standard classifications.

---

[🏠 Subtopic Index](00_Index.md) | [← Prev: DM-6.6 Binomial Theorem](DM-6.6_Binomial_Theorem.md) | [Next: DM-7.2 Relevance of Discrete Mathematics →](DM-7.2_Relevance_of_Discrete_Mathematics.md)
