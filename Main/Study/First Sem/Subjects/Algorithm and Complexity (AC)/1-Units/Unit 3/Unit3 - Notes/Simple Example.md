# Preparata's Algorithm - Simple Example

## Input Array: [6, 2, 8, 3]

Let's trace through Preparata's algorithm step by step with this 4-element array.

## Step 1: Build Bitonic Sequences

### What is a Bitonic Sequence?

A bitonic sequence goes **up then down** (like a mountain) or **down then up** (like a valley).

- Examples: [2, 6, 4, 1] (up then down) or [5, 3, 7, 9] (down then up)

### Building Bitonic Sequences from [6, 2, 8, 3]

**Level 1: Create 2-element bitonic sequences**

```
Pair 1: [6, 2] → Compare and arrange as ↑ (ascending): [2, 6]
Pair 2: [8, 3] → Compare and arrange as ↓ (descending): [8, 3]

Result: [2, 6] and [8, 3]
```

**Level 2: Combine into 4-element bitonic sequence**

```
Combine [2, 6] ↑ with [8, 3] ↓:
Merge them: [2, 6, 8, 3]

This is bitonic! (goes up: 2→6→8, then down: 8→3)
```

## Step 2: Bitonic Merge

### How Bitonic Merge Works

1. Split the bitonic sequence in half
2. Compare elements from first half with corresponding elements from second half
3. Put smaller elements in first half, larger in second half
4. Both halves become bitonic, recursively sort them

### Sorting [2, 6, 8, 3]

```
Step 2.1: Split in half
Left half: [2, 6]
Right half: [8, 3]

Step 2.2: Compare corresponding positions
Compare position 1: min(2, 8) = 2, max(2, 8) = 8
Compare position 2: min(6, 3) = 3, max(6, 3) = 6

Step 2.3: Rearrange
Left half gets smaller values: [2, 3]
Right half gets larger values: [8, 6]

Current state: [2, 3, 8, 6]

Step 2.4: Sort each half
Left half [2, 3]: Already sorted → [2, 3]
Right half [8, 6]: Sort descending → [8, 6] or ascending → [6, 8]

Let's sort ascending: [6, 8]
```

## Step 3: Final Result

```
Combine sorted halves: [2, 3] + [6, 8] = [2, 3, 6, 8]
```

## Visual Representation

```
Original:    [6, 2, 8, 3]
             /           \
Step 1:   [2,6] ↑    [8,3] ↓
             \           /
Step 1.2:   [2, 6, 8, 3]  (bitonic)
                 |
Step 2:     Split & Compare
            [2,6] vs [8,3]
            ↓
            [2,3] [8,6]
                 |
Step 2.2:   Sort each half
            [2,3] [6,8]
                 |
Final:      [2, 3, 6, 8]
```

## Why is this Better than Regular Merge Sort?

### Regular Merge Sort would do:

```
[6, 2, 8, 3]
↓
[6, 2] [8, 3] → Sort each: [2, 6] [3, 8]
↓
Merge [2, 6] and [3, 8]: Compare 2 vs 3, then 6 vs 3, then 6 vs 8
Result: [2, 3, 6, 8]
```

### Preparata's Algorithm:

```
[6, 2, 8, 3]
↓
Create bitonic: [2, 6, 8, 3]
↓
Bitonic merge: One comparison round gives us sorted halves
Result: [2, 3, 6, 8]
```

## Key Advantage: Fewer Comparisons

**Regular approach:**

- Sort [6,2] → 1 comparison
- Sort [8,3] → 1 comparison
- Merge results → 2-3 comparisons
- **Total: 4-5 comparisons**

**Preparata's approach:**

- Create bitonic → 2 comparisons
- Bitonic merge → 2 comparisons
- **Total: 4 comparisons (guaranteed)**

## Simple Rule to Remember

1. **Make it bitonic** (like a mountain: up then down)
2. **Split and compare** corresponding positions
3. **Recursively sort** the two halves

The magic is that bitonic sequences have a special property: when you split them and compare corresponding elements, you automatically get two smaller bitonic sequences that are easier to sort!

## Real-World Analogy

Think of sorting books by height:

- **Regular way**: Sort left pile, sort right pile, then carefully merge
- **Preparata's way**: Arrange books in a "mountain" shape first, then do one smart comparison that automatically gives you two sorted piles

The "mountain" arrangement (bitonic) makes the final sorting step much more efficient!