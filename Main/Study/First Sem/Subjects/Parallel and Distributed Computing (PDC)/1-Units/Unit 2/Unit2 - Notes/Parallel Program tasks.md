
## 🧠 **Formal Model of a Task System**

This model defines the components needed to schedule tasks in a **Directed Acyclic Graph (DAG)** for execution on parallel systems.

---

### 🧱 System Definition:

$$
\text{System } = (T, \prec, D_{ij}, A_i)
$$

---

### 🔍 Components Explained:

| Symbol                         | Meaning                                                                                                         |
| ------------------------------ | --------------------------------------------------------------------------------------------------------------- |
| $T = \{ t_1, t_2, ..., t_n \}$ | Set of **tasks** to be executed                                                                                 |
| $\prec$ (partial order)        | Defines **dependencies** between tasks. If $t_i \prec t_j$, then $t_i$ must complete **before** $t_j$ starts.   |
| $D_{ij}$                       | Communication cost matrix. $D_{ij} \geq 0$: amount of **data sent from task $t_i$ to task $t_j$**.              |
| $A_i$                          | Computation cost vector. $A_i > 0$: number of **instructions or units of work** required to execute task $t_i$. |

---

### 📘 Interpreting the Model with Example

Imagine a simple task graph:

* $t_1$: Read data
* $t_2$: Preprocess
* $t_3$: Analyze
* $t_4$: Write results

Now:

* $T = \{ t_1, t_2, t_3, t_4 \}$
* Dependencies (partial order):

  $$
  t_1 \prec t_2,\quad t_2 \prec t_3,\quad t_3 \prec t_4
  $$
* $D_{ij}$: Shows how much data is sent from one task to another
* $A_i$: Shows how long (how much work) each task takes

---

### 🧠 What This Model Helps With

This formal system helps:

* Represent the **task graph** clearly
* Model **computation and communication costs**
* Design and analyze **scheduling algorithms**
* Evaluate **parallel execution time**

---

### 🧩 Use in Scheduling Algorithms

Schedulers use this model to:

* Assign tasks to processors
* Minimize **total execution time**
* Minimize **communication overhead**
* Respect **task dependencies**

---

## ✅ Summary

| Component | Purpose                          |
| --------- | -------------------------------- |
| $T$       | Set of tasks                     |
| $\prec$   | Dependency order between tasks   |
| $D_{ij}$  | Communication cost between tasks |
| $A_i$     | Computation cost of each task    |

This system is foundational for **task scheduling**, **performance modeling**, and **parallel execution planning** in multicore/distributed systems.

---
