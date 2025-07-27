

## 🧠 **Unit 2: Computational Complexity Theory (10 Hours)**

This unit teaches you how to classify problems based on how difficult they are to **solve** or **verify**, and how to deal with hard problems when no efficient solutions are known.

---

### 🔹 **2.1 Basic Concepts**

#### 🔸 **Complexity Theory**

- A branch of theoretical computer science that studies the **resources (time, space)** required to solve computational problems.
    
- Goal: Classify problems into **easy** (tractable) and **hard** (intractable).
    

#### 🔸 **Complexity Classes**

|Class|Meaning|
|---|---|
|**P**|Problems solvable in **polynomial time**. Efficient algorithms exist.|
|**NP**|Problems whose solutions can be **verified** in polynomial time.|
|**NP-Complete**|Problems that are both in NP and **as hard as any problem in NP**.|
|**NP-Hard**|Problems **at least as hard as NP-Complete**, may not even be in NP.|

#### 🔸 **Decision Problems**

- Problems with a **yes/no** answer. Used for theoretical analysis.
    

#### 🔸 **Language Recognition Problems**

- Related to whether a string **belongs to a language** (set of strings). Used in automata theory and complexity.
    

---

### 🔹 **2.2 Problem Reduction**

#### 🔸 **Reduction**

- A way to **transform one problem into another**.
    
- Used to prove that solving one problem can help solve another.
    

#### 🔸 **Polynomial-Time Reduction**

- If Problem A reduces to Problem B in polynomial time, solving B lets you solve A efficiently.
    

#### 🔸 **Cook’s Theorem**

- The first major result in NP-Completeness.
    
- States that **SAT (Boolean Satisfiability)** is NP-Complete.  
    → All NP problems can be reduced to SAT.
    

#### 🔸 **Proving NP-Completeness**

To prove a problem is NP-Complete:

1. Show it’s in NP.
    
2. Reduce a known NP-Complete problem to it in polynomial time.
    

#### 🔸 **Examples of NP-Complete Problems**

These are classic problems used in reductions:

- **Formula Satisfiability (SAT)**
    
- **3SAT** (Each clause has 3 literals)
    
- **CLIQUE** (Find a complete subgraph of size k)
    
- **Vertex Cover** (Select k nodes covering all edges)
    
- **Hamiltonian Cycle** (Visit all nodes once in a cycle)
    
- **Traveling Salesman Problem (TSP)** – decision version
    
- **Subset Sum** (Find subset that adds to a target value)
    

---

### 🔹 **2.3 NP-Hard Code Generation Problems**

Some problems from **compiler optimization** are NP-Hard:

#### 🔸 **Code Generation with Common Subexpression**

- Optimize code by reusing common calculations (like a+ba + b appearing multiple times).
    

#### 🔸 **Parallel Assignment Instructions**

- Optimizing assignments where multiple variables can be updated **in parallel**, without conflicts.
    

> These are **NP-Hard** because they involve combinatorial choices with no known polynomial-time algorithm.

---

### 🔹 **2.4 Coping with NP-Completeness**

Since NP-Complete problems are hard, we use **approximations**.

#### 🔸 **Performance Ratio**

- Measures how close an approximate solution is to the optimal.
    
- Example: If optimal cost is 100 and approximate gives 120 → performance ratio = 1.2
    

#### 🔸 **Approximation Algorithms**

Used to **quickly find near-optimal solutions**. Examples include:

|Problem|Approximation Algorithm|
|---|---|
|**Vertex Cover**|Pick both endpoints of each uncovered edge|
|**TSP**|Use Minimum Spanning Tree + Shortcut|
|**Set Covering**|Greedy pick the set covering most uncovered elements|
|**Subset Sum**|Use rounding + dynamic programming|

---

## ✅ **Summary for Exam (Bullet Points)**

- **Complexity theory** classifies problems as P, NP, NP-Complete, and NP-Hard.
    
- **Reduction** is used to show one problem is at least as hard as another.
    
- **Cook’s Theorem** proves SAT is NP-Complete.
    
- Common NP-Complete problems: 3SAT, CLIQUE, Vertex Cover, Subset Sum, TSP.
    
- **Code generation problems** in compilers can be NP-Hard.
    
- We deal with NP-Complete problems using **approximation algorithms**, evaluated by **performance ratios**.
    
