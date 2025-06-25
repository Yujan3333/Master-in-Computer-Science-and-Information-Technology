# List Ranking Algorithm - Detailed Explanation

## What is List Ranking?

**List Ranking** assigns a **rank (position number)** to each node in a linked list, where:

- The **last node** (tail) gets rank = 1
- Each previous node gets rank = rank of next node + 1

## The Challenge

In a **sequential algorithm**, we'd traverse from head to tail, but this takes O(n) time because we have to visit each node one by one.

In **parallel computing**, we want multiple processors to work simultaneously, but a linked list is inherently sequential - each node only knows about its next node.

## The PRAM Solution: Pointer Jumping

The key insight is to use **pointer jumping** - instead of following one link at a time, we can "jump" over multiple nodes simultaneously.

## Step-by-Step Example

Let's say we have a linked list: **A → B → C → D → E → NULL**

### Initial Setup:

```
Node:  A    B    C    D    E
Next:  B    C    D    E   NULL
Rank:  ?    ?    ?    ?    1    (E gets rank 1 since it's the tail)
```

### Round 1: First Pointer Jump

Each processor assigned to a node does:

- If my next node is not NULL, add my next node's rank to my rank
- Update my next pointer to jump over one node

```
A: next = C (was B), rank = ? (B's rank unknown)
B: next = D (was C), rank = ? (C's rank unknown)  
C: next = E (was D), rank = ? (D's rank unknown)
D: next = NULL (was E), rank = 1 + 1 = 2 (E's rank was 1)
E: next = NULL, rank = 1 (unchanged)
```

After Round 1:

```
Node:  A    B    C    D    E
Next:  C    D    E   NULL NULL
Rank:  ?    ?    ?    2    1
```

### Round 2: Second Pointer Jump

```
A: next = E (was C), rank = ? (C's rank still unknown)
B: next = NULL (was D), rank = ? + 2 = ? (D's rank is 2)
C: next = NULL (was E), rank = ? + 1 = ? (E's rank is 1)
D: next = NULL, rank = 2 (unchanged)
E: next = NULL, rank = 1 (unchanged)
```

But wait - we still have unknowns. Let me show the correct approach:

## Correct Pointer Jumping Algorithm

### Initial State:

```
Node:  A    B    C    D    E
Next:  B    C    D    E   NULL
Dist:  1    1    1    1    0    (distance to next node)
```

### Round 1:

For each node i (in parallel):

- If next[i] ≠ NULL:
    - dist[i] = dist[i] + dist[next[i]]
    - next[i] = next[next[i]]

```
A: dist = 1 + 1 = 2, next = C
B: dist = 1 + 1 = 2, next = D  
C: dist = 1 + 1 = 2, next = E
D: dist = 1 + 0 = 1, next = NULL
E: dist = 0, next = NULL
```

After Round 1:

```
Node:  A    B    C    D    E
Next:  C    D    E   NULL NULL
Dist:  2    2    2    1    0
```

### Round 2:

```
A: dist = 2 + 2 = 4, next = E
B: dist = 2 + 1 = 3, next = NULL
C: dist = 2 + 0 = 2, next = NULL
D: dist = 1, next = NULL
E: dist = 0, next = NULL
```

After Round 2:

```
Node:  A    B    C    D    E
Next:  E   NULL NULL NULL NULL
Dist:  4    3    2    1    0
```

### Round 3:

```
A: dist = 4 + 0 = 4, next = NULL
B: dist = 3, next = NULL
C: dist = 2, next = NULL
D: dist = 1, next = NULL
E: dist = 0, next = NULL
```

### Final Result:

The **rank** of each node is its **distance + 1**:

```
Node:  A    B    C    D    E
Rank:  5    4    3    2    1
```

## Why This Works

1. **Initially**: Each node knows its distance to the next node (1 for most, 0 for tail)
2. **Pointer Jumping**: In each round, we "jump" over intermediate nodes
3. **Distance Accumulation**: We accumulate the distances as we jump
4. **Logarithmic Rounds**: After O(log n) rounds, all pointers reach NULL
5. **Final Rank**: Each node's rank = accumulated distance + 1

## Time Complexity

- **Rounds needed**: O(log n) because we double the jump distance each time
- **Processors**: n (one per node)
- **Total time**: O(log n) with n processors

## Practical Applications

- **Parallel list processing**: Converting linked lists to arrays
- **Tree algorithms**: Many tree problems can be reduced to list ranking
- **Graph algorithms**: Path finding in certain graph structures

This algorithm demonstrates how **parallel thinking** can solve inherently sequential problems by using clever techniques like pointer jumping!