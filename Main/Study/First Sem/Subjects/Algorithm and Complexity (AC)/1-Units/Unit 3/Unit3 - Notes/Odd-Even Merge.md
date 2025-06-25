# Odd-Even Merge Algorithm (Batcher's Algorithm)

## Overview

The Odd-Even Merge algorithm, developed by Ken Batcher in 1968, is a divide-and-conquer parallel sorting network algorithm that merges two sorted sequences in O(log²n) time using O(n) processors. It's particularly notable for its regular structure and suitability for hardware implementation.

## Algorithm Description

### Core Principle

The algorithm is based on the **Odd-Even Merge Theorem**:

> If we have two sorted sequences of length n, we can merge them by:
> 
> 1. Separating elements by their indices (odd/even positions)
> 2. Recursively merging odd-indexed and even-indexed elements separately
> 3. Applying compare-exchange operations to adjacent pairs in the combined result

### Detailed Algorithm

```
ODD_EVEN_MERGE(A[1..m], B[1..n])
INPUT: Two sorted arrays A and B (assume m = n = 2^k for simplicity)
OUTPUT: Merged sorted array C[1..2n]

1. BASE CASE:
   IF m = n = 1:
      RETURN COMPARE_EXCHANGE(A[1], B[1])

2. DIVIDE:
   A_odd = [A[1], A[3], A[5], ...] // Odd-indexed elements
   A_even = [A[2], A[4], A[6], ...] // Even-indexed elements
   B_odd = [B[1], B[3], B[5], ...] // Odd-indexed elements
   B_even = [B[2], B[4], B[6], ...] // Even-indexed elements

3. CONQUER:
   C_odd = ODD_EVEN_MERGE(A_odd, B_odd)   // Recursive merge
   C_even = ODD_EVEN_MERGE(A_even, B_even) // Recursive merge

4. COMBINE:
   Interleave C_odd and C_even:
   temp[1] = C_odd[1]
   temp[2] = C_even[1]
   temp[3] = C_odd[2]
   temp[4] = C_even[2]
   ...

5. CLEAN UP:
   PARALLEL FOR i = 2 to 2n-1 step 2:
      COMPARE_EXCHANGE(temp[i], temp[i+1])

6. RETURN temp

COMPARE_EXCHANGE(a, b):
   RETURN (min(a,b), max(a,b))
```

## Detailed Example Walkthrough

### Example 1: Simple Case

**Input**: A = [1, 5], B = [2, 6]

**Step 1 - Divide:**

```
A_odd = [1] (position 1)
A_even = [5] (position 2)
B_odd = [2] (position 1)  
B_even = [6] (position 2)
```

**Step 2 - Recursive Merge:**

```
C_odd = ODD_EVEN_MERGE([1], [2]) = [1, 2]  // Base case
C_even = ODD_EVEN_MERGE([5], [6]) = [5, 6]  // Base case
```

**Step 3 - Interleave:**

```
temp = [1, 5, 2, 6]  // Interleave C_odd and C_even
```

**Step 4 - Compare-Exchange:**

```
Compare-exchange (5, 2): temp = [1, 2, 5, 6]
Compare-exchange (5, 6): temp = [1, 2, 5, 6] (no change)
```

**Result**: [1, 2, 5, 6]

### Example 2: Larger Case

**Input**: A = [1, 3, 7, 9], B = [2, 4, 6, 8]

**Step 1 - Divide:**

```
A_odd = [1, 7] (positions 1, 3)
A_even = [3, 9] (positions 2, 4)
B_odd = [2, 6] (positions 1, 3)
B_even = [4, 8] (positions 2, 4)
```

**Step 2 - Recursive Merge:**

```
C_odd = ODD_EVEN_MERGE([1, 7], [2, 6])
  ↳ Divide: [1], [7], [2], [6]
  ↳ Merge: [1, 2], [6, 7]
  ↳ Interleave: [1, 6, 2, 7]
  ↳ Compare-exchange: [1, 2, 6, 7]

C_even = ODD_EVEN_MERGE([3, 9], [4, 8])
  ↳ Divide: [3], [9], [4], [8]
  ↳ Merge: [3, 4], [8, 9]
  ↳ Interleave: [3, 8, 4, 9]
  ↳ Compare-exchange: [3, 4, 8, 9]
```

**Step 3 - Interleave:**

```
temp = [1, 3, 2, 4, 6, 8, 7, 9]
```

**Step 4 - Compare-Exchange:**

```
Position 2,3: Compare-exchange (3, 2) → [1, 2, 3, 4, 6, 8, 7, 9]
Position 4,5: Compare-exchange (4, 6) → [1, 2, 3, 4, 6, 8, 7, 9]
Position 6,7: Compare-exchange (8, 7) → [1, 2, 3, 4, 6, 7, 8, 9]
Position 8,9: Compare-exchange (9, 9) → [1, 2, 3, 4, 6, 7, 8, 9]
```

**Result**: [1, 2, 3, 4, 6, 7, 8, 9]

## Mathematical Foundation

### The Odd-Even Merge Theorem

**Theorem**: Let A and B be sorted sequences of length n. After applying the odd-even merge procedure, the resulting sequence has the property that at most one element can be out of place, and if so, it can only be with its immediate neighbor.

**Proof Sketch**:

1. Odd-indexed elements from both sequences maintain their relative order
2. Even-indexed elements from both sequences maintain their relative order
3. The interleaving step may create at most one adjacent pair that needs swapping
4. The final compare-exchange step corrects any such inversions

### Recursion Analysis

Let T(n) be the time complexity for merging two sorted arrays of size n:

```
T(n) = T(n/2) + O(1)  // Two recursive calls of size n/2, plus O(1) combine step
T(1) = O(1)           // Base case

Solution: T(n) = O(log n)  // Depth of recursion
```

However, the total time complexity is O(log²n) because:

- **Depth of recursion**: log n levels
- **Operations per level**: O(n) compare-exchange operations
- **Parallel execution**: Each level can be executed in O(log n) time
- **Total time**: O(log n) × O(log n) = O(log²n)

## Complexity Analysis

### Time Complexity

- **Sequential Time**: O(n log²n)
- **Parallel Time**: O(log²n) with O(n) processors
- **Depth**: log n levels of recursion
- **Work per level**: O(n) compare-exchange operations

### Space Complexity

- **Additional Space**: O(n) for temporary arrays
- **Stack Space**: O(log n) for recursion
- **Total Space**: O(n + log n) = O(n)

### Processor Complexity

- **Processors Needed**: O(n) processors
- **Processor Utilization**: Varies by level (some processors idle)
- **Communication**: Local communication only (adjacent elements)

## Network Structure

### Sorting Network Representation

The odd-even merge can be represented as a sorting network:

```
Level 0: Input elements
Level 1: First set of compare-exchange operations
Level 2: Second set of compare-exchange operations
...
Level log²n: Final output

Each level can be executed in parallel
```

### Network Properties

1. **Oblivious**: Comparison pattern independent of input data
2. **Regular**: Highly structured, suitable for hardware
3. **Scalable**: Extends naturally to larger inputs
4. **Fault-Tolerant**: Local failures don't propagate

## Implementation Variants

### Recursive Implementation

```python
def odd_even_merge(A, B):
    if len(A) == 1 and len(B) == 1:
        return sorted([A[0], B[0]])
    
    # Divide
    A_odd = A[::2]    # Elements at odd positions
    A_even = A[1::2]  # Elements at even positions
    B_odd = B[::2]
    B_even = B[1::2]
    
    # Conquer
    C_odd = odd_even_merge(A_odd, B_odd)
    C_even = odd_even_merge(A_even, B_even)
    
    # Combine
    temp = []
    for i in range(len(C_odd)):
        temp.append(C_odd[i])
        if i < len(C_even):
            temp.append(C_even[i])
    
    # Compare-exchange cleanup
    for i in range(1, len(temp)-1, 2):
        if temp[i] > temp[i+1]:
            temp[i], temp[i+1] = temp[i+1], temp[i]
    
    return temp
```

### Iterative Implementation

```python
def odd_even_merge_iterative(A, B):
    n = len(A) + len(B)
    result = A + B
    
    # Number of levels
    levels = int(math.log2(n))
    
    for level in range(levels):
        step = 2 ** (level + 1)
        
        # Parallel compare-exchange operations
        for i in range(0, n - step//2, step):
            for j in range(step//2):
                if result[i + j] > result[i + j + step//2]:
                    result[i + j], result[i + j + step//2] = \
                        result[i + j + step//2], result[i + j]
    
    return result
```

### Hardware Implementation

```verilog
// Simplified Verilog for 4-element odd-even merge
module odd_even_merge_4(
    input [31:0] a0, a1, b0, b1,
    output [31:0] out0, out1, out2, out3
);
    wire [31:0] temp0, temp1, temp2, temp3;
    
    // Level 1: Compare-exchange for base cases
    compare_exchange ce1(a0, b0, temp0, temp1);
    compare_exchange ce2(a1, b1, temp2, temp3);
    
    // Level 2: Interleave and final compare-exchange
    assign out0 = temp0;
    compare_exchange ce3(temp1, temp2, out1, out2);
    assign out3 = temp3;
endmodule
```

## Comparison with Other Merge Algorithms

|Algorithm|Time|Processors|Work|Space|Hardware Friendly|
|---|---|---|---|---|---|
|Sequential|O(n)|1|O(n)|O(1)|No|
|Binary Search|O(log n)|O(n)|O(n log n)|O(n)|No|
|Odd-Even|O(log²n)|O(n)|O(n log²n)|O(n)|Yes|
|Bitonic|O(log²n)|O(n)|O(n log²n)|O(n)|Yes|

## ## Advantages and Disadvantages
   
   ### Advantages
   
   1. **Regular Structure**: Highly suitable for hardware implementation
   2. **Oblivious**: Comparison pattern doesn't depend on input data
   3. **Parallelizable**: Natural parallel structure
   4. **Fault Tolerant**: Localized operations
   5. **Scalable**: Works for any power-of-2 size
   
   ### Disadvantages
   
   6. **Sub-optimal Work**: O(n log²n) vs O(n) optimal work
   7. **Restricted Input**: Works best with power-of-2 sizes
   8. **Complex Implementation**: More complex than simple merge
   9. **Resource Intensive**: Requires many processors for efficiency
   
   ## Applications and Extensions
   
   ### Bitonic Sorting
   
   Odd-even merge is a key component of bitonic sorting:
   
   ```
   10. Divide array into bitonic sequences
   11. Use odd-even merge to sort each sequence
   12. Recursively combine results
   ```
   
   ### Sorting Networks
   
   Used in building comparison-based sorting networks:
   
   - **Batcher's Odd-Even Sort**: Complete sorting algorithm
   - **Hardware Sorting**: FPGA and ASIC implementations
   - **GPU Sorting**: Parallel sorting on graphics processors
   
   ### External Sorting
   
   Applied in external sorting algorithms:
   
   - **Tape Sorting**: Historical tape-based sorting
   - **Disk Sorting**: Modern disk-based external sorting
   - **Distributed Sorting**: MapReduce-style distributed sorting
   
   ## Practical Considerations
   
   ### When to Use Odd-Even Merge
   
   1. **Hardware Implementation**: FPGA, ASIC, or custom hardware
   2. **Fixed-Size Inputs**: Known input sizes that are powers of 2
   3. **Predictable Performance**: Need guaranteed O(log²n) time
   4. **Parallel Architecture**: Abundant parallel processing resources
   
   ### When NOT to Use
   
   5. **General-Purpose Software**: Better alternatives available
   6. **Variable Input Sizes**: Irregular input sizes
   7. **Limited Processors**: Sequential merge is more efficient
   8. **Work-Optimal Required**: Need minimal computational work
   
   ### Optimization Strategies
   
   9. **Blocking**: Process data in cache-friendly blocks
   10. **Pipelining**: Overlap computation and communication
   11. **SIMD**: Use vector instructions for parallel compare-exchange
   12. **Memory Layout**: Optimize data placement for access patterns
   
   ## Historical Significance
   
   ### Batcher's Contribution
   
   Ken Batcher's 1968 paper introduced:
   
   - **Odd-Even Merge**: The algorithm described here
   - **Bitonic Sort**: A complete sorting algorithm
   - **Sorting Networks**: Theoretical framework for comparison networks
   
   ### Impact on Computer Science
   
   1. **Parallel Algorithms**: Early example of divide-and-conquer parallelism
   2. **Hardware Design**: Influenced VLSI and parallel processor design
   3. **Network Theory**: Contributed to development of interconnection networks
   4. **Complexity Theory**: Helped establish parallel complexity classes
   
   The Odd-Even Merge algorithm represents a beautiful marriage of theoretical computer science and practical parallel processing, demonstrating how regular, predictable algorithms can be highly effective in parallel computing environments despite not being work-optimal.