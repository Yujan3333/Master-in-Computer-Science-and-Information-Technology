
## 🌳 Goal:

To compute the **level (depth)** of a node $v$ in a rooted tree $T$, using its **Euler Tour**.

---

## 🧠 Definition of Level:

* The **level of a node $v$** is the **number of edges** on the path from the **root** to $v$.
* Root has level = 0.
* A child has level = level of parent + 1.

---

## 🪜 Step-by-Step Method Using Euler Tour:

### 1. **Euler Tour**:

* Perform an Euler Tour traversal of the tree.
* In this tour, every node is visited **multiple times**:

  * Once when **entering** (first time)
  * Once **after returning** from each child
  * Once before leaving to parent

### 2. **Mark the Visit Points**:

Let the **first visit** to a node $v$ be denoted $v_1$, and other visits $v_2, v_3, \dots, v_{d(v)+1}$.

### 3. **Assign Weights**:

* Assign **+1** to the **first time** a node $v$ is visited (i.e., $v_1$)
* Assign **–1** to all **other visits** of $v$

---

## 🔢 Compute Prefix Sum:

* While traversing the Euler Tour, compute the **prefix sum of weights**.
* The **prefix sum at the first occurrence** $v_1$ of node $v$ gives the **level (depth)** of that node.

---

## ✅ Example

Let’s take a small tree:

```
        A
       / \
      B   C
```

### Euler Tour (nodes visited as):

```
A₁ → B₁ → B₂ → A₂ → C₁ → C₂ → A₃
```

### Assign Weights:

| Visit | Node | Weight |
| ----- | ---- | ------ |
| A₁    | A    | +1     |
| B₁    | B    | +1     |
| B₂    | B    | -1     |
| A₂    | A    | -1     |
| C₁    | C    | +1     |
| C₂    | C    | -1     |
| A₃    | A    | -1     |

### Compute Prefix Sum:

| Step | Node | Weight | Prefix Sum         |
| ---- | ---- | ------ | ------------------ |
| 1    | A₁   | +1     | 1                  |
| 2    | B₁   | +1     | 2 → **Level of B** |
| 3    | B₂   | -1     | 1                  |
| 4    | A₂   | -1     | 0                  |
| 5    | C₁   | +1     | 1 → **Level of C** |
| 6    | C₂   | -1     | 0                  |
| 7    | A₃   | -1     | -1                 |

### Final Levels:

* Level(A) = prefix sum at A₁ = **1**
* Level(B) = prefix sum at B₁ = **2**
* Level(C) = prefix sum at C₁ = **1**

🧩 But since root's level should be **0**, we adjust all values by subtracting 1:

---

### ✅ Final Adjusted Levels:

* Level(A) = 0
* Level(B) = 1
* Level(C) = 1

---

## 📌 Summary:

| Step | What to do                                                |
| ---- | --------------------------------------------------------- |
| 1.   | Do an Euler Tour                                          |
| 2.   | Assign +1 to first visit of each node                     |
| 3.   | Assign -1 to other visits                                 |
| 4.   | Compute prefix sums                                       |
| 5.   | The prefix sum at first visit minus 1 gives the **level** |

---
