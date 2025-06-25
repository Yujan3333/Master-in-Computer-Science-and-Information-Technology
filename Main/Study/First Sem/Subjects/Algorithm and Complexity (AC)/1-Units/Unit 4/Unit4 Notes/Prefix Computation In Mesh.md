- Missed Class
## Prefix Computation In Mesh
The image describes a parallel algorithm for computing prefix sums (also known as scan operations) on a 2D mesh architecture using a row-major indexing scheme. Here's a step-by-step explanation of the process:

**PE**-> Processing Element
### Key Concepts:
1. **Prefix Sum**: For an array `[a1, a2, ..., an]`, the prefix sum is `[a1, a1+a2, a1+a2+a3, ..., sum of all elements]`.
2. **Mesh Architecture**: A grid of processing elements (PEs) arranged in rows and columns (e.g., a `jp x jp` mesh).
3. **Row-Major Indexing**: Elements are stored row by row, like reading left to right, top to bottom.

---

### Algorithm Steps:

#### **Step 1: Row-Wise Prefix Computation**
- Each row independently computes its own prefix sum.
  - For example, if a row has elements `[1, 2, 3]`, its prefix sum is `[1, 3, 6]`.
- This is done in parallel for all rows.

#### **Step 2: Column-Wise Prefix (Last Column Only)**
- Only the **last column** (column `jp`) computes a prefix sum of the values obtained from Step 1.
  - For example, if the last column has `[6, 10, 16]` (from Step 1), its prefix sum is `[6, 16, 32]`.
- This step aggregates the cumulative sums of each row's total.

#### **Step 3: Shift and Broadcast**
- **Shift Down**: The prefix sums from the last column are shifted down by one row.
  - For example, `[6, 16, 32]` becomes `[0, 6, 16]` (with the first row initialized to 0).
- **Broadcast**: Each shifted value is broadcast to all PEs in the corresponding row.
  - For example, the second row receives `6`, and the third row receives `16`.

#### **Step 4: Final Update**
- Each PE (except those in the first row) adds the broadcasted value from Step 3 to its local prefix sum (from Step 1).
  - For example, if a PE in the second row had a prefix sum of `[4, 11, 12]` (from Step 1), it adds `6` to each element to get `[10, 17, 18]`.
- The first row remains unchanged.

---

### Example Calculation:
The image shows a mesh with values like:
```
Row 1: [5, 8, 6]  
Row 2: [4, 11, 12]  
Row 3: [5, 6, 16]  
Row 4: [4, 21, 22]  
```

1. **Step 1**: Row-wise prefixes:
   - Row 1: `[5, 13, 19]`  
   - Row 2: `[4, 15, 27]`  
   - Row 3: `[5, 11, 27]`  
   - Row 4: `[4, 25, 47]`  

2. **Step 2**: Last column prefix (`[19, 27, 27, 47]` → `[19, 46, 73, 120]`).

3. **Step 3**: Shift down to `[0, 19, 46, 73]` and broadcast to rows.

4. **Step 4**: Add broadcasted values to each row:
   - Row 2: `[4+19, 15+19, 27+19] = [23, 34, 46]`  
   - Row 3: `[5+46, 11+46, 27+46] = [51, 57, 73]`  
   - Row 4: `[4+73, 25+73, 47+73] = [77, 98, 120]`  

---

### Complexity:
The algorithm runs in $O(\sqrt{P})$ time, where *P*  is the number of PEs, because:
- Each step (row/column prefix, shift, broadcast) takes \( $O(\sqrt{P})$  time on a mesh.

==Why $\sqrt{P}\text{ }$  is used here though? ==
- Row and column doesnot always needs to be equal But here P=9 means 3x3 mesh.
### Summary:
The algorithm efficiently computes prefix sums by breaking the problem into parallel row/column operations and combining results through shifting and broadcasting. This approach leverages the mesh's 2D structure to achieve logarithmic-time performance.