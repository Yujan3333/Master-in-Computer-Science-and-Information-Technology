## Why O(n log n) for Randomized QuickSort?
   
   ### **The Recursion Tree Visualization**
   
   ```
   Level 0:     [entire array of size n]           ← n work
                /                    \
   Level 1:   [size n/2]           [size n/2]      ← n work total  
              /        \           /        \
   Level 2: [n/4]    [n/4]     [n/4]    [n/4]     ← n work total
            ...                                    
   Level log n: [size 1] [size 1] ... [size 1]    ← n work total
   ```
   
### Key Insights:
   
   1. **Each Level Does O(n) Work**
       - Partitioning at each level processes every element once
       - Sum of all partition work at level i = O(n)
   2. **There are O(log n) Levels**
       - Each level (on average) cuts problem size in half
       - n → n/2 → n/4 → ... → 1
       - Number of times you can halve n until you reach 1 = log₂ n
   3. **Total Work = Levels × Work per Level**
       - O(log n) levels × O(n) work per level = **O(n log n)**


---
## Detailed Breakdown of "log n"

### Where does log n come from?

The **depth** of recursion when we keep dividing by 2:

```
n elements → n/2 → n/4 → n/8 → ... → 1

How many divisions? 
n/2^k = 1
2^k = n  
k = log₂ n
```


---
## Concrete Example

**Sorting 1000 elements:**

- n = 1000
- log₂ 1000 ≈ 10 levels of recursion
- Work per level ≈ 1000 comparisons/moves
- Total work ≈ 1000 × 10 = 10,000 operations
- Compare to n² = 1,000,000 operations!