Prefix Sum
![](../../../../../../../../Images/First_Sem_Images/Computing%20a%20post%20order%20numbering-prefix%20sum.png)

### 🔁 Post-order Traversal Reminder:

* **Post-order:** Visit **Left**, then **Right**, then **Root**.
* For a tree: **Visit all children first, then the parent**.

---

### ✅ Goal:

To compute the **post-order number** for each node in a rooted tree **T** using its **Euler Tour**.

---

### 🔧 Key Idea: Use **weights** and **weighted rank** during the Euler Tour.

---

## 🪜 Step-by-step Process

### 1. Perform an Euler Tour of the tree

   * The **Euler Tour** is a sequence of visits to nodes, where each **edge is traversed twice** (forward and back).
   * Each node *v* is visited:

     * **Once before going to its first child**,
     * **Once after returning from each child**,
     * **Finally, once after returning from the last child (before returning to parent)**.

### 2. Label the Euler Tour sequence

   For a node `v` of degree `d(v)` (i.e., number of children):

   * Let the visits to `v` during the Euler Tour be `v₁, v₂, ..., v_{d(v)+1}`.

     * `v₁`: when you first visit `v`
     * `v₂` to `v_{d(v)}`: intermediate visits after each child
     * `v_{d(v)+1}`: final visit to `v` before returning to parent

### 3.  Assign weights to these visits

   * Assign weight **0** to each of `v₁`, `v₂`, ..., `v_{d(v)}`
   * Assign weight **1** to the final visit `v_{d(v)+1}`

### 4. Compute **weighted rank** (prefix sum of weights)

   * For each position in the Euler Tour, compute the total number of `1`s seen **so far**.
   * The **weighted rank** at `v_{d(v)+1}` gives the **post-order number** of node `v`.

---

## 📘 Example:

Consider this tree:

```
        A
       / \
      B   C
```

### Euler Tour sequence:

```
A → B → A → C → A
```

Euler visits:

* A₁ (before B)
* B₁ (leaf, no children)
* A₂ (after B, before C)
* C₁ (leaf)
* A₃ (after C, done)

### Assign weights:

* A₁ → 0
* B₁ → 1 (since B is a leaf, this is its last visit)
* A₂ → 0
* C₁ → 1
* A₃ → 1

### Compute weighted ranks:

| Visit | Node | Weight | Weighted Rank       |
| ----- | ---- | ------ | ------------------- |
| A₁    | A    | 0      | 0                   |
| B₁    | B    | 1      | 1 → Post-order of B |
| A₂    | A    | 0      | 1                   |
| C₁    | C    | 1      | 2 → Post-order of C |
| A₃    | A    | 1      | 3 → Post-order of A |

---

### 🧠 Final Post-order Numbering:

* B: 1
* C: 2
* A: 3

---
