This is about **measuring how well parallel computing performs** compared to sequential computing. Let me simplify:

## Key Concepts:

### 1. **Speedup**

**How much faster is parallel vs sequential?**

- Formula: `Speedup = Sequential Time / Parallel Time`
- **Example:** If sequential takes 100 seconds, parallel takes 25 seconds
- Speedup = 100/25 = **4x faster**

### 2. **Work Done**

**Total computational effort across all processors**

- Formula: `Work = Number of Processors × Time taken`
- **Example:** 4 processors working for 25 seconds = 4 × 25 = **100 units of work**

### 3. **Efficiency**

**How well are the processors being utilized?**

- Formula: `Efficiency = Sequential Time / Total Work Done`
- **Example:** Efficiency = 100/(4×25) = 100/100 = **1.0 = 100% efficient**

## The Given Example (Adding 1 to 100):

**Sequential:** Add one by one = 99 operations

**Parallel (2 processors):**

- Processor A: adds 1+2+...+50 = 50 operations
- Processor B: adds 51+52+...+100 = 50 operations
- Both work simultaneously, so total time = 50

**Results:**

- **Speedup** = 99/50 = 1.98 (almost 2x faster)
- **Efficiency** = 99/(2×50) = 0.99 = 99% (very efficient use of processors)

**Bottom line:** These metrics help you understand if adding more processors actually makes your program run better!