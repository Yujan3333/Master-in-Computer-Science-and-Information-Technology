### ✅ **Unit 1: Advanced Algorithm Analysis and Design Techniques**

**Total Hours: 10**

This unit is about two main things:

1. How to analyze the performance of complex algorithms in smarter ways (not just time and space).
    
2. Learning **advanced algorithm design** techniques with real-world applications.
    

---

## 🧠 1.1 Advanced Algorithm Analysis Techniques

### a) Amortized Analysis

Used when an operation is **sometimes expensive**, but **on average**, it is **cheap** over a sequence of operations.  
It gives a more accurate picture than worst-case analysis.

#### 🧮 Techniques:

- **Aggregate Analysis**: Average cost per operation over _n_ operations.
    
- **Accounting Method**: Assign “fake” costs (credits/debits) to operations to balance expensive ones.
    
- **Potential Method**: Use a potential function (like stored energy) to measure change in "state" over time.
    

> 📌 **Example:** Inserting into a dynamic array – sometimes you need to resize, which is expensive, but it doesn't happen every time.

---

### b) **Probabilistic Analysis**

Analyzes algorithm behavior assuming input has **some probability distribution**.

- Often used for average-case performance.
    
- You assume inputs or behavior is random (e.g., quicksort's pivot choice).
    

---

### c) **Las Vegas and Monte Carlo Algorithms**

These are **randomized algorithms**, but with a difference:

|Type|Guarantees Correctness?|Runtime Guarantee?|
|---|---|---|
|**Las Vegas**|✅ Yes|❌ No (random runtime)|
|**Monte Carlo**|❌ No (might give wrong answer)|✅ Yes (fixed runtime)|

> 📌 **Example:**
> 
> - Las Vegas: Randomized QuickSort – always correct but time may vary.
>     
> - Monte Carlo: Primality test – may give a wrong answer with low probability but runs fast.
>     

---

## 🛠️ **1.2 Advanced Algorithm Design Techniques**

### a) **Greedy Algorithms**

Always make the **locally optimal** choice, hoping it leads to a global optimum.

#### Examples:

- **Tree Vertex Splitting** – optimizing tree structures.
    
- **Job Sequencing with Deadlines** – maximize profit with job-deadline constraints.
    

---

### b) **Dynamic Programming (DP)**

Solves problems by **breaking them into overlapping subproblems** and **storing results**.

#### Examples:

- **Greedy vs DP** – Compare when greedy fails, but DP works.
    
- **String Editing** – Minimum operations to convert one string to another (like edit distance).
    
- **Optimal BST (Binary Search Tree)** – Minimize search cost in a BST with known probabilities.
    

---

### c) **Backtracking**

Tries **all possibilities recursively**, but **abandons** paths that don’t lead to a solution (pruning).

#### Examples:

- **Sum of Subsets** – Find subsets that sum to a value.
    
- **Knapsack Problem** – Choose items to maximize value within a weight limit.
    

---

### d) **Randomized Algorithms**

Use **random numbers** to improve performance or simplicity.

#### Examples:

- **Identifying Repeated Elements** – like finding duplicates in a stream.
    
- **Primality Testing** – check if a number is prime probabilistically.
    
- **Karger’s Algorithm** – Randomized algorithm for **minimum cut** in a graph.
    

---

### 📌 Summary Table

| Technique                  | Focus                         | Example Problem           |
| -------------------------- | ----------------------------- | ------------------------- |
| **Amortized Analysis**     | Avg. cost over operations     | Dynamic arrays            |
| **Probabilistic Analysis** | Average-case behavior         | Random pivot in QuickSort |
| **Las Vegas Algorithm**    | Always correct, random time   | Randomized QuickSort      |
| **Monte Carlo Algorithm**  | Fast, may be wrong            | Random primality test     |
| **Greedy Algorithm**       | Local best at each step       | Job Sequencing            |
| **Dynamic Programming**    | Store overlapping subproblems | String editing            |
| **Backtracking**           | Try all with pruning          | Knapsack                  |
| **Randomized Algorithm**   | Use random choice             | Karger’s Min Cut          |