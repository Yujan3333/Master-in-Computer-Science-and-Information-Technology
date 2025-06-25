## What is Prefix Computing?

Given array [5, 3, -6, 2, 7, 10, -2, 8] and operation + Output: [5, 8, 2, 4, 11, 21, 19, 27]

- Position 0: 5
- Position 1: 5+3 = 8
- Position 2: 5+3+(-6) = 2
- Position 3: 5+3+(-6)+2 = 4, etc.

## The Parallel Algorithm:

**Setup:** 16 elements, 4 processors (n/log n = 16/4 = 4 processors) Each processor gets log n = 4 elements

### Step 1: Local Prefix Computation

Each processor computes prefixes for its assigned elements:

- **Processor 1:** [5,12,8,6] → [5, 17, 25, 31]
- **Processor 2:** [3,9,11,12] → [3, 12, 23, 35]
- **Processor 3:** [1,5,6,7] → [1, 6, 12, 19]
- **Processor 4:** [10,4,3,5] → [10, 14, 17, 22]

### Step 2: Process Last Elements

Take the last element from each group: [31, 35, 19, 22] Compute prefixes of these: [31, 66, 85, 107]

### Step 3: Update All Prefixes

Add the cumulative values from Step 2 to update all prefixes:

- **Processor 1:** [5, 17, 25, 31] (no change - it's first)
- **Processor 2:** [3, 12, 23, 35] + 31 = [34, 43, 54, 66]
- **Processor 3:** [1, 6, 12, 19] + 66 = [67, 72, 78, 85]
- **Processor 4:** [10, 14, 17, 22] + 85 = [95, 99, 102, 107]

## Why This Works:

1. **Step 1:** Each processor handles its portion independently
2. **Step 2:** Figure out how much to "carry over" between groups
3. **Step 3:** Add the carry-over to get final results

## Performance:

- **Time:** O(log n) - all steps run in parallel
- **Speedup:** O(n)/O(log n) = n/log n
- **Efficiency:** Nearly 100% because total work = n (same as sequential)

This is **work-optimal** because it uses the minimum total work while achieving good speedup!