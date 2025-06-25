## 🧠 Definitions

### ✅ **Divide and Conquer**

> A paradigm where a problem is **divided** into smaller independent subproblems, solved **recursively**, and their results are **combined**.

- **Subproblems are independent** (no overlapping).
    
- **Recursive** solution.
    

**Examples**:

- Merge Sort
    
- Quick Sort
    
- Binary Search
    
- Strassen's Matrix Multiplication
    

---

### ✅ **Dynamic Programming**

> A technique used when a problem has **overlapping subproblems** and **optimal substructure**.  
> It **stores solutions** of subproblems to avoid recomputation (**memoization** or **tabulation**).

- **Subproblems overlap** (solved multiple times)
    
- Avoids recomputation using a **table**
    

**Examples**:

- Fibonacci sequence
    
- Longest Common Subsequence (LCS)
    
- Matrix Chain Multiplication
    
- 0/1 Knapsack Problem
    
- Optimal BST
    

---

## 📊 Comparison Table

|Feature|Divide and Conquer|Dynamic Programming|
|---|---|---|
|**Problem Type**|Subproblems are **independent**|Subproblems are **overlapping**|
|**Subproblem Solving**|Solved recursively, no reuse|Solved once and **stored for reuse**|
|**Overlapping Subproblems**|❌ No|✅ Yes|
|**Optimal Substructure**|✅ Usually required|✅ Required|
|**Uses Memoization?**|❌ No|✅ Yes (or Tabulation)|
|**Example Problems**|Merge Sort, Quick Sort, Binary Search|LCS, Fibonacci, 0/1 Knapsack, Matrix Chain|
|**Efficiency**|May recompute subproblems|Avoids recomputation → **more efficient**|
|**Storage**|Low|Requires **extra space** for tables|

---

## 🧮 Example to Illustrate Difference

### 🔸 Fibonacci Number

- **Naive Recursion (Divide and Conquer-like)**
    
    F(n)=F(n−1)+F(n−2)F(n) = F(n-1) + F(n-2)F(n)=F(n−1)+F(n−2)
    
    Time: O(2n)O(2^n)O(2n) — **inefficient** due to repeated calls.
    
- **Dynamic Programming**  
    Store F(0),F(1),...,F(n)F(0), F(1), ..., F(n)F(0),F(1),...,F(n) in an array  
    Time: O(n)O(n)O(n)
    

✅ DP is faster due to **memoization**.

---

## ✍️ Exam Answer Summary

> **Divide and Conquer** breaks problems into independent subproblems and solves them recursively, combining results.  
> **Dynamic Programming** is used when subproblems overlap and stores their results to avoid recomputation.  
> DP is generally more efficient for problems with **overlapping subproblems** and **optimal substructure**.

---

### 🧠 Bonus Tip:

To decide between the two:

- **If subproblems are independent** → use **Divide and Conquer**
    
- **If subproblems repeat** → use **Dynamic Programming**