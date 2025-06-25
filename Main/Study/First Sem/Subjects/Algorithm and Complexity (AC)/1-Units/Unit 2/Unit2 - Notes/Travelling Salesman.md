## 🔷 **Traveling Salesman Problem (TSP)**

---

### ✅ **Definition:**

- The **Traveling Salesman Problem (TSP)** involves:
    
    - A **salesman**
        
    - A set of **cities**
        
    - **Distances** between each pair of cities
        
- The salesman must:
    
    1. **Start from a city (e.g., hometown)**
        
    2. **Visit every other city exactly once**
        
    3. **Return to the starting city**
        
- The goal is to find the **shortest possible route** (minimum total distance).
    

---

### ✅ **Example:**

Suppose the cities are: A, B, C, D

The salesman needs to find the shortest route that goes:

$A \to B \to C \to D \to A$

Trying all possible paths manually is possible for small numbers but becomes difficult as cities increase.

---

### ✅ **Applications of TSP:**

1. Delivery of meals or packages
    
2. Routing courier trucks (e.g., FedEx, DHL)
    
3. Designing circuits in microchip manufacturing
    
4. Sales routes and logistics
    

---

### ✅ **Solution Methods:**

---

### **1) Brute-Force Approach:**

- Try **all possible tours** (permutations of cities).
    
- For **$n$ cities**, number of tours is:
    
    $(n-1)!$
    
- Example: For 5 cities $\rightarrow$ $(5-1)! = 24$ possible routes
    
- Time complexity is **factorial**, so it is very slow for large $n$.
    

---

### **2) Dynamic Programming Approach (Efficient):**

|Step|What Happens|
|---|---|
|1|Start with base case: only city 1 visited|
|2|Build up answers for 2, 3, ..., n cities visited|
|3|At each step, pick the cheapest next city|
|4|Store results in a table so we don’t repeat work|
|5|At the end, return to starting city and output minimum total cost|

Uses a recurrence relation to reduce redundant calculations.

#### **Algorithm Sketch:**

Let:

- $C(S, j)$ = minimum cost to reach city $j$ from starting city (1), visiting all cities in set $S$
    

##### **Steps:**

![](../../../../../../../../Attachments/Travelling%20Salesman.png)

- Time complexity:
    
    $\mathcal{O}(n^2 \cdot 2^n)$
    
    Much faster than factorial time, but still exponential.
    

---

### ✅ **Key Points for Exam:**

- TSP is an **NP-Hard** optimization problem.
    
- Goal: Visit all cities once and return to start with **minimum cost**.
    
- **Brute-force** checks all possibilities: $(n-1)!$
    
- **Dynamic Programming** is more efficient:  
    Uses subset-based cost table to build optimal route.