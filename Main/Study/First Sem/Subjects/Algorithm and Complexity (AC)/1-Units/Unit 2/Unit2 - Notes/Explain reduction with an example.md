

## 🧩 **What is Reduction?**

> **Reduction** is a technique used to **transform one problem (A)** into another problem (B) in such a way that **solving B also solves A**.

This helps in:

* Proving **problem difficulty** (like NP-completeness)
* Designing **efficient algorithms** using known ones

---

## ✅ **Types of Reduction:**

* **Polynomial-Time Reduction**: The transformation happens in polynomial time, so the hardness of one problem carries over to the other.

---

## 🔍 **Why is Reduction Important?**

* To show a problem is **NP-Complete**, we **reduce a known NP-Complete problem** to it.
* If Problem A is known to be hard, and you reduce A to B, then **B must be at least as hard**.

---

## 💡 **Example: Reduction from 3SAT to CLIQUE**

Let’s walk through a classic reduction to show how it works:

### 🎯 Goal:

Reduce the **3SAT** problem (known NP-Complete) to **CLIQUE**.

### 🔹 3SAT:

Given a formula with clauses like:

$$
(C_1 \wedge C_2 \wedge C_3), \quad \text{where } C_1 = (x_1 \vee \neg x_2 \vee x_3), \dots
$$

Each clause has 3 literals. Question: Can we assign TRUE/FALSE so that the whole formula becomes **true**?

---

### 🔹 CLIQUE Problem:

Given a graph $G$ and an integer $k$, does $G$ contain a **clique** (complete subgraph) of **k** vertices?

---

### 🔸 Idea of the Reduction:

We’ll **construct a graph from the 3SAT formula** such that:

* **Each node** in the graph represents a **literal from a clause**.
* We draw an **edge** between **compatible literals** (not negations of each other, and from different clauses).
* A **k-clique** in this graph means: one literal per clause that do not contradict each other → satisfying assignment.

---

### 🧮 Example Sketch:

Let’s say we have a 3SAT formula with 3 clauses:

$$
C_1 = (x_1 \vee x_2 \vee x_3)  
\quad C_2 = (\neg x_1 \vee x_2 \vee \neg x_4)  
\quad C_3 = (x_3 \vee \neg x_2 \vee x_4)
$$

Now:

* Create a graph with 3 nodes per clause (9 total)
* Connect each node to nodes in other clauses if the literals are not contradictory
* Find a 3-clique = 1 compatible literal from each clause

---

### ✅ If a **3-clique** exists, then the original formula is **satisfiable**

✅ If no 3-clique, then the formula is **not satisfiable**

---

## 🔁 Summary of Steps in a Reduction (Exam-Ready):

1. **Take a known NP-Complete problem A** (e.g., 3SAT)
2. **Transform it into a new problem B** (e.g., CLIQUE)
3. **Prove** that:

   * The transformation takes **polynomial time**
   * Solving B helps solve A

If both conditions are met → problem B is **at least as hard** as A.

---


