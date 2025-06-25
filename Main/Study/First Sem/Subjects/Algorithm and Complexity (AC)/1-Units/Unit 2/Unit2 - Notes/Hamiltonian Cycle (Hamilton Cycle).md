## 🔷 **Hamiltonian Cycle (Hamilton Cycle)**

---

### ✅ **Definition:**

- A **Hamiltonian cycle** is a **closed loop** in a graph that:
    
    - **Visits every vertex exactly once**
        
    - **Starts and ends at the same vertex**
        

---

### ✅ **Hamiltonian Graph:**

- A graph that **has a Hamiltonian cycle** is called a **Hamiltonian graph**.
    

---

### ✅ **Important Notes:**

- In the cycle, the **start and end vertex is the same**.
    
- All **other vertices appear exactly once**.
    
- The cycle must **use only existing edges** in the graph.
    

---

### ✅ **Special Cases:**

- **K₁ (single vertex)** is considered Hamiltonian by definition.
    
- **K₂ (2 vertices with one edge)** is **not** Hamiltonian, as it can't form a cycle.
    

---

### ✅ **Hamiltonian Path vs Cycle:**

|Term|Description|
|---|---|
|**Hamiltonian Path**|Visits each vertex **exactly once**, but **does not return** to the starting vertex|
|**Hamiltonian Cycle**|Visits each vertex once and **returns to the starting vertex**|

---

### ✅ **How to Solve the Problem:**

1. **Brute Force Method:**
    
    - Try all possible permutations of vertices.
        
    - Time complexity: **O(n!)**
        
    - Works only for small graphs.
        
2. **Frank Rubin Method:**
    
    - A rule-based method to **reduce the graph step-by-step**.
        
    - Checks for necessary conditions of Hamiltonian cycles.
        
3. **Dynamic Programming (Held-Karp Algorithm):**
    
    - Stores solutions to subproblems (like TSP).
        
    - Time complexity: **O(n²·2ⁿ)** (faster than brute force)
        
4. **Monte Carlo Algorithm:**
    
    - **Randomized algorithm** that guesses paths multiple times.
        
    - May not always give the correct answer but is faster.
        

---

### ✅ **Applications:**

- Route planning
    
- Puzzle solving (e.g. Knight’s tour in chess)
    
- DNA sequencing
    
- Circuit design
    

---

### 🟩 **Summary for Exam:**

- A **Hamiltonian cycle** is a path in a graph that visits every vertex exactly once and **returns to the start**.
    
- If a graph has such a cycle, it is called **Hamiltonian**.
    
- Can be solved using:
    
    - Brute force
        
    - Frank Rubin method
        
    - Dynamic programming
        
    - Monte Carlo method