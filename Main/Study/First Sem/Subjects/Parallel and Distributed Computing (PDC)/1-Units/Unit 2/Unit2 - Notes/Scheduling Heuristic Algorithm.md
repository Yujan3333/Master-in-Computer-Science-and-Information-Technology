
## ✅ **1. Priority-Based Scheduling**

This is a dynamic list scheduling method. Here's how it works step-by-step:

### 🔷 **Steps:**

1. **Assign a priority** to each task
   (Common: based on number of children, or depth, or bottom-level time)
2. Put all **ready tasks** into a **priority queue** (tasks with no unsatisfied dependencies)
3. While the queue is **not empty**:

   * Pick the task with the **highest priority**
   * Assign it to an **idle processor**
   * Once all **predecessors of a task are done**, it becomes **ready** → add it to queue

### ✅ Characteristics:

* Simple, fast, greedy
* Communication delay can be added if needed
* Doesn’t require altering the graph

---

## ✅ **2. Scheduling Using Clustering Heuristics**

This approach is more **global and structural**, usually applied **before actual scheduling**.

### 🔷 **Steps:**

1. **Cluster tasks** together (based on communication, dependency closeness, etc.)

   * These clusters act like **super-tasks**
2. If number of clusters > number of processors → perform **cluster merging**
3. Do **physical mapping** of clusters to processors:

   * Try to **reduce communication cost**
4. Within each cluster, define **task execution ordering**

### ✅ Characteristics:

* Better global optimization
* Minimizes **inter-processor communication**
* Slower than greedy methods but **better schedule quality**
* Used in tools like **DSC, MCP, DCP**

---

## ✅ Summary Table:

| Feature                     | Priority-Based Scheduling | Clustering Heuristics Scheduling              |
| --------------------------- | ------------------------- | --------------------------------------------- |
| Scheduling type             | Greedy, local             | Global, structural                            |
| Task assignment             | One-by-one                | Grouped in clusters                           |
| Communication consideration | Can add 1 unit per edge   | Tries to minimize inter-cluster communication |
| Complexity                  | Simple                    | More complex                                  |
| Use case                    | Fast approximation        | High-quality schedule                         |

---

## Task Allocation Using Duplication
![](../../../../../../../../Images/First_Sem_Images/Scheduling%20Heuristic%20Algorithm-task%20allocation%20using%20duplication.png)
