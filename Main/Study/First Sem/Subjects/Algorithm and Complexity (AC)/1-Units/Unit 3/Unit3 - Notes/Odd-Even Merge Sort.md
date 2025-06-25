# Odd-Even Merge Sort - Exam Summary
   
## Algorithm Overview
   
   **Odd-Even Merge Sort** combines divide-and-conquer with Batcher's odd-even merge to achieve parallel sorting.
   
### Basic Algorithm
   
   ```
   ODD_EVEN_MERGE_SORT(A[1..n]):
   1. IF n = 1: RETURN A
   2. Divide A into two halves: A1[1..n/2] and A2[n/2+1..n]
   3. Recursively sort: S1 = ODD_EVEN_MERGE_SORT(A1)
                        S2 = ODD_EVEN_MERGE_SORT(A2)
   4. Merge using odd-even merge: RETURN ODD_EVEN_MERGE(S1, S2)
   ```
   
   ## Step-by-Step Example
   
   **Input**: [8,3,5,4,7,6,1,2]
   
### Level 1: Base Cases (Sort pairs)
   
   ```
   [8,3] → [3,8]
   [5,4] → [4,5]  
   [7,6] → [6,7]
   [1,2] → [1,2]
   ```
   
### Level 2: Merge Adjacent Pairs
   
   ```
   ODD_EVEN_MERGE([3,8], [4,5]):
   - Odd elements: [3], [4] → [3,4]
   - Even elements: [8], [5] → [5,8]
   - Interleave: [3,5,4,8]
   - Compare-exchange: [3,4,5,8]
   
   ODD_EVEN_MERGE([6,7], [1,2]):
   - Odd elements: [6], [1] → [1,6]
   - Even elements: [7], [2] → [2,7]
   - Interleave: [1,2,6,7]
   - Compare-exchange: [1,2,6,7]
   ```
   
### Level 3: Final Merge
   
   ```
   ODD_EVEN_MERGE([3,4,5,8], [1,2,6,7]):
   - Odd elements: [3,5], [1,6] → [1,3,5,6]
   - Even elements: [4,8], [2,7] → [2,4,7,8]
   - Interleave: [1,2,3,4,5,7,6,8]
   - Compare-exchange: [1,2,3,4,5,6,7,8]
   ```
   
## Recursion Tree Structure
   
   ```
                   [1,2,3,4,5,6,7,8]
                  /                 \
           [3,4,5,8]               [1,2,6,7]
           /       \               /       \
       [3,8]     [4,5]         [6,7]     [1,2]
       /  \      /  \          /  \      /  \
      8    3    5    4        7    6    1    2
   ```
   
## Key Properties
   
### Complexity Analysis
   
   - **Time Complexity**: O(log²n) with n processors
   - **Work Complexity**: O(n log²n) total operations
   - **Space Complexity**: O(n log n) for all recursive levels
   - **Depth**: log n levels of recursion
   
### Recurrence Relations
   
   ```
   T(n) = T(n/2) + O(log²n)  // Two recursive sorts + odd-even merge
   T(1) = O(1)               // Base case
   
   Solution: T(n) = O(log²n) parallel time
   ```
   
### Work Analysis
   
   ```
   W(n) = 2W(n/2) + O(n log²n)  // Work for sorting + merging
   W(1) = O(1)
   
   Solution: W(n) = O(n log²n) total work
   ```
   
## Algorithm Characteristics
   
### Advantages
   
   1. **Highly Parallel**: Each level can execute in parallel
   2. **Regular Structure**: Suitable for hardware implementation
   3. **Predictable**: Oblivious to input data distribution
   4. **Scalable**: Works for any power-of-2 input size
   
### Disadvantages
   
   5. **Not Work-Optimal**: O(n log²n) vs O(n log n) optimal
   6. **Complex Implementation**: More complex than standard sorts
   7. **Resource Intensive**: Requires many processors
   8. **Power-of-2 Restriction**: Works best with 2^k elements