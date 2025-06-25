# Maximum Selection with n² Processors

## Algorithm Overview

**Goal**: Find the maximum of n numbers in **O(1) time** using **n² processors**

**Key Idea**: Use brute force comparison - compare every element with every other element simultaneously using massive parallelism.

## The Algorithm Steps

### Step 0: Base Case

If n == 1, output the single element as maximum.

### Step 1: Pairwise Comparisons

For each pair (i,j) where 1 ≤ i,j ≤ n:

- Processor P_{ij} computes: m_{ij} = 1 if x_i < x_j, otherwise 0
- This creates an n×n comparison matrix

### Step 2: Group OR Operations

- Group processors into n groups: G₁, G₂, ..., Gₙ
- Group Gᵢ contains processors: P_{i1}, P_{i2}, ..., P_{in}
- Each group computes Boolean OR of all its m_{ij} values

### Step 3: Find Maximum

- If group Gᵢ computes 0 in Step 2, then processor P_{i1} outputs kᵢ as the maximum

## Detailed Example

**Input**: [7, 3, 9, 5] (n = 4)

### Step 1: Create Comparison Matrix

We have 16 processors (4²) comparing all pairs:

```
       j=1  j=2  j=3  j=4
       x₁=7 x₂=3 x₃=9 x₄=5
i=1 x₁=7:  0    0    1    0     (7<7:0, 7<3:0, 7<9:1, 7<5:0)
i=2 x₂=3:  1    0    1    1     (3<7:1, 3<3:0, 3<9:1, 3<5:1)  
i=3 x₃=9:  0    0    0    0     (9<7:0, 9<3:0, 9<9:0, 9<5:0)
i=4 x₄=5:  1    0    1    0     (5<7:1, 5<3:0, 5<9:1, 5<5:0)
```

**Matrix M:**

```
M = [0  0  1  0]
    [1  0  1  1]
    [0  0  0  0]
    [1  0  1  0]
```

### Step 2: Group OR Operations

Each group Gᵢ computes OR of row i:

- **Group G₁**: OR(0,0,1,0) = **1** ← Element 7 is smaller than at least one other
- **Group G₂**: OR(1,0,1,1) = **1** ← Element 3 is smaller than at least one other
- **Group G₃**: OR(0,0,0,0) = **0** ← Element 9 is NOT smaller than any other! 🎯
- **Group G₄**: OR(1,0,1,0) = **1** ← Element 5 is smaller than at least one other

### Step 3: Identify Maximum

Since **Group G₃ computed 0**, this means:

- Element x₃ = 9 is never smaller than any other element
- Therefore, x₃ = 9 is the **MAXIMUM**

## Why This Works

**Logic**: If an element is the maximum, then:

- It is **never smaller** than any other element
- All comparisons xᵢ < xⱼ where i = max_index will be FALSE (0)
- The OR of all zeros is 0
- Only the maximum element's group will output 0

**Non-maximum elements**:

- Will be smaller than at least one other element (the maximum)
- At least one comparison will be TRUE (1)
- The OR will be 1

## Complexity Analysis

- **Time**: O(1) - All operations happen in parallel
    
    - Step 1: All n² comparisons happen simultaneously
    - Step 2: All n OR operations happen simultaneously
    - Step 3: Identification happens simultaneously
- **Processors**: n² processors needed
    
    - Each processor P_{ij} handles one comparison
- **PRAM Model**: CRCW (Concurrent Read Concurrent Write)
    
    - Multiple processors can read the same input values
    - Multiple processors can write to determine the result

## Practical Considerations

**Advantages**:

- Extremely fast: O(1) time
- Simple logic: just pairwise comparisons

**Disadvantages**:

- Very expensive: requires n² processors
- Not practical for large n
- Better algorithms exist with fewer processors

## Alternative: Tournament Method

For comparison, the **tournament method** uses:

- **n processors** instead of n²
- **O(log n) time** instead of O(1)
- Often more practical for real implementations

**Trade-off**: This algorithm demonstrates the classic time vs. space trade-off in parallel computing - we can achieve constant time by using quadratically more resources.