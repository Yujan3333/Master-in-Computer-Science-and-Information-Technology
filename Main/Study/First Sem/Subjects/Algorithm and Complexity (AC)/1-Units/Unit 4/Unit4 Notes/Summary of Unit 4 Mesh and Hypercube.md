## 📘 **4.1 Mesh Algorithms**

### ✅ A. **Computational Model (Mesh Network)**

- A **mesh** is a **2D grid** of processors (like rows and columns).
    
- Each processor is connected to its **neighbors (up, down, left, right)**.
    
- **Data moves step by step** from one processor to another via neighbors.
    

> Think of it like people passing messages in a group of connected desks in a classroom grid.

---

### ✅ B. **Packet Routing**

**i. Packet Routing on a Linear Array:**

- Linear array = processors arranged in a **single row**
    
- Each processor has a **message** to send to another processor.
    
- Goal: route packets efficiently **without collisions** (2 packets at same place at same time)
    

**ii. Greedy Algorithm for PPR (Permutation Packet Routing) on a Mesh:**

- Each processor has **one message**, destined for another processor.
    
- Strategy:
    
    - First move message in **rows** (horizontal)
        
    - Then move in **columns** (vertical)
        
- Greedy: move message **if the next step is free**
    

> This routing takes **at most 2n steps** on an n × n mesh.

---

### ✅ C. **Fundamental Algorithms**

**i. Broadcasting:**

- One processor wants to send the same data to **all others**.
    
- Done in steps:
    
    - First row-wise, then column-wise
        
- Time = **O(√n)** on √n × √n mesh
    

**ii. Prefix Computation:**

- Each processor has a value
    
- Compute prefix sums (like cumulative sum of values up to each point)
    
- Uses row and column communication
    

**iii. Data Concentration:**

- **Gather data** from all processors to a **single processor** (usually at top-left)
    
- Done in **phases** from rows → columns
    

---

### ✅ D. **Selection**

**i. Randomized Algorithm for n = p (1 value per processor):**

- Each processor picks a random sample
    
- Use sampling + parallel comparison to find the k-th smallest element
    

**ii. Randomized Selection for n > p (multiple elements per processor):**

- Each processor selects a few elements
    
- Master processor selects a pivot and filters out unnecessary elements
    
- Repeats until selection is done
    

---

### ✅ E. **Sorting**

**i. Sorting on a Linear Array:**

- Processors in 1D line
    
- Use **odd-even transposition sort**
    
- Time = **O(n)** for n processors
    

**ii. Sorting on a Mesh:**

- 2D grid processors
    
- Use **Shear Sort**:
    
    1. Row-wise sort (left to right for even rows, right to left for odd rows)
        
    2. Column-wise sort
        
    3. Repeat several times
        
- Total time: **O(√n log n)** for n processors in √n × √n mesh
    

---

## 🟩 Summary for Exam:

| Topic              | Key Point                  | Time        |
| ------------------ | -------------------------- | ----------- |
| Mesh Model         | 2D grid of processors      | —           |
| Packet Routing     | Greedy row-then-column     | O(n)        |
| Broadcasting       | One to all                 | O(√n)       |
| Prefix Sum         | Cumulative sum             | O(√n)       |
| Data Concentration | All to one                 | O(√n)       |
| Selection (n = p)  | Randomized sample & filter | O(√n)       |
| Sorting (Mesh)     | Shear sort                 | O(√n log n) |

---
## 🧊 **4.2 Hypercube Algorithms**

A **hypercube** is a powerful parallel computing model, useful for fast interprocessor communication and efficient algorithm design.

---

## 🔹 1. **Computational Model**

### ✅ **What is a Hypercube?**

- A **d-dimensional hypercube** (Q<sub>d</sub>) is a graph with **2<sup>d</sup> nodes**.
    
- Each node is connected to **d other nodes** (1-bit difference in binary address).
    
- Example:
    
    - **Q₁**: 2 nodes (0,1)
        
    - **Q₂**: 4 nodes → (00, 01, 10, 11)
        
    - **Q₃**: 8 nodes → 3D cube
        

### 📌 Properties:

- **log₂(p)** distance between any two nodes
    
- **Highly symmetric**
    
- Efficient for algorithms like broadcasting, sorting, etc.
    

---

## 🔸 **Butterfly Network (Optional)**

- Special structure used in parallel algorithms like **Fast Fourier Transform (FFT)**
    
- Related to hypercube, but with structured stages
    

---

## 🔹 2. **Embedding of Other Networks**

Hypercube can simulate other network topologies:

- **Ring**
    
- **Mesh**
    
- **Tree**
    
- Efficient mapping helps simulate algorithms from those models
    

---

## 🔹 3. **PPR Routing (Permutation Packet Routing)**

Each processor sends a packet to a unique destination (permutation of nodes)

### ✅ Greedy Algorithm:

- Routes packet one bit at a time toward destination
    
- Always fix the leftmost differing bit first
    
- Can cause **congestion**
    

### ✅ Randomized Algorithm:

- Sends packets first to a **random intermediate node**, then to destination
    
- **Reduces collision**
    
- Expected time: **O(log n)**
    

---

## 🔹 4. **Fundamental Algorithms**

### ✅ **Broadcasting**

- One node sends message to all others
    
- Uses hypercube dimensions:
    
    - Each round, sender sends to neighbor differing in one bit
        
- Time: **O(log n)**
    

### ✅ **Prefix Computation**

- Compute prefix sums (or other associative operations)
    
- Each bit level contributes to final result
    
- Time: **O(log n)**
    

### ✅ **Data Concentration**

- Reverse of broadcasting
    
- All nodes send data to a single node (e.g., for sum, min, max)
    
- Time: **O(log n)**
    

---

## 🔹 5. **Selection Algorithms**

### ✅ Case 1: n = p (1 element per processor)

**Randomized Algorithm:**

- Pick a random sample
    
- Use sampling and ranking to reduce candidate set
    
- Expected Time: **O(log n)**
    

### ✅ Case 2: n > p (more data per processor)

- First, locally reduce data (sample or partial selection)
    
- Use communication to gather and select globally
    

---

## 🔹 6. **Sorting on Hypercube**

### ✅ **Odd-Even Merge Sort**

- Compare-exchange operations follow odd-even rules
    
- Works recursively
    
- Uses network structure (but slower than bitonic)
    

### ✅ **Bitonic Sort**

- Efficient parallel sorting algorithm
    
- Based on **bitonic sequences** (increasing then decreasing)
    
- Can be mapped well to hypercube connections
    
- Time: **O(log² n)**
    

---

## 📝 **Summary for Exams**

|Concept|Time Complexity|Notes|
|---|---|---|
|Broadcasting|O(log n)|Spread message to all nodes|
|Data Concentration|O(log n)|Collect data to one node|
|Prefix Computation|O(log n)|Parallel prefix sum|
|PPR (Greedy)|O(n) worst case|Bit-by-bit routing|
|PPR (Randomized)|O(log n) expected|Less collision|
|Bitonic Sort|O(log² n)|Efficient parallel sorting|
|Odd-Even Merge Sort|O(log² n)|Based on merging strategy|