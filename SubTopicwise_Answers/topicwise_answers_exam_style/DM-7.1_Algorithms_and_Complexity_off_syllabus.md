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

Every block below is copied from `../answers_exam_style/`, which is the
only place an answer is authored. A number here is the same number, character
for character, as the one it came from.


### [2024 Q.7(a)]

**Question.** A delivery company uses a computer system to manage customer orders. Sort all delivery addresses based on distance from the warehouse. Search for a customer's order by name or ID. Use a greedy approach to assign delivery vans to the nearest unserved address. Evaluate the time complexity of each algorithm used.

**Solution.**

**(i) Sorting the addresses by distance**

**Algorithm chosen: merge sort.**

The addresses are sorted by one key, the distance from the warehouse. Merge sort
splits the list in half, sorts each half recursively, then merges the two sorted
halves in linear time.

- Average time complexity: $O(n \log n)$
- Best case: $O(n \log n)$
- Worst case: $O(n \log n)$
- Space: $O(n)$

Merge sort is chosen over quicksort because the worst case is guaranteed, and
because the merges are stable, so two addresses at the same distance keep their
original order.

> [!note] Why not the others
> Bubble sort is $O(n^2)$, which fails at tens of thousands of addresses.
> Quicksort is $O(n \log n)$ on average but $O(n^2)$ if the list is already
> sorted, which is close to what a distance list looks like. Heapsort is
> $O(n \log n)$ in all cases but is not stable. Counting or radix sort would be
> faster still, at $O(n + k)$, but only if the distances are integers in a known
> range, which floating-point distances are not.

**(ii) Searching for a customer's order**

**Algorithm chosen: binary search**, since the question says the address list is
already sorted.

**Pseudocode**

```
function BINARY-SEARCH(A, key):
    low  ← 0
    high ← length(A) - 1
    while low ≤ high:
        mid ← floor((low + high) / 2)
        if A[mid].id = key:
            return mid
        else if A[mid].id < key:
            low ← mid + 1
        else:
            high ← mid - 1
    return NOT-FOUND
```

- Average time complexity: $O(\log n)$
- Best case: $O(1)$, when the key sits at the first midpoint tried
- Worst case: $O(\log n)$
- Space: $O(1)$, it iterates rather than recursing

Binary search halves the search interval at every step, so $n$ items take at most
$\lceil \log_2 n \rceil$ comparisons. For $n = 10^6$ that is 20 comparisons.

> [!warning] Binary search has one requirement
> The list must be sorted on the **same key** that is searched. Sorted by
> distance does **not** mean sorted by customer ID. Searching for a customer
> therefore needs a second list sorted by ID, kept in step with the first.
> Searching an unsorted list with this pseudocode returns a wrong answer silently,
> not an error. Linear search would be $O(n)$ but would at least be correct.

**(iii) Assigning vans to the nearest unserved address**

**Greedy algorithm: nearest-first assignment.**

At each step take the unassigned van that is closest to the warehouse and give it
the unassigned address that is closest to that van. This is the locally optimal
choice repeated.

```
function ASSIGN-VANS(vans, addresses):
    for each address in addresses, in ascending order of distance:
        best ← NONE
        for each free van v:
            if best = NONE or DISTANCE(v, address) < DISTANCE(best, address):
                best ← v
        assign address to best
        mark best as used
    return schedule
```

- Time complexity: $O(n \log n + nm)$, where $n$ addresses and $m$ vans. Sorting
  costs $O(n \log n)$ and the matching loop costs $O(nm)$.
- Space: $O(n + m)$

**Why greedy is defensible here.** Every delivery costs distance and there is no
interaction between vans, so the total distance is a sum of independent terms and
minimising each term separately minimises the total. That is the case where greedy
is exactly right.

**Where greedy would fail.** If a van had a capacity of 3 and one address needed a
truck, taking the nearest address for the van could block a heavier address that
only the truck can serve. Then the locally nearest choice is not safe, and a
matching algorithm is needed instead.

$$
\boxed{\text{Sort } O(n \log n), \quad \text{search } O(\log n), \quad \text{assign } O(n \log n + nm)}
$$

---

[🏠 Subtopic Index](00_Index.md) | [← Prev: DM-6.6 Binomial Theorem](DM-6.6_Binomial_Theorem.md) | [Next: DM-7.2 Relevance of Discrete Mathematics →](DM-7.2_Relevance_of_Discrete_Mathematics.md)
