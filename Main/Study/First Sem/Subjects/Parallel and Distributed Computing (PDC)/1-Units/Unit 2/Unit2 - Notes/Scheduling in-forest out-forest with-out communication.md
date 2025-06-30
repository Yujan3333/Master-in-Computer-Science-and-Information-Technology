
## 🔷 Why do we **augment** the task graph?

When scheduling parallel tasks, **communication between processors** (i.e., when tasks that depend on each other are assigned to different processors) causes **delays**.

The idea is:

> 💡 Instead of modeling communication delays explicitly, we **modify the task graph** by adding **extra dependencies** so that if we schedule **without communication**, we still **preserve correct behavior**.

---

## 🧩 What's an **Augmented Task Graph**?

An **augmented task graph** is the **original task graph** + **additional precedence edges** that simulate communication costs.

### Key Property:

> Scheduling the **augmented graph without modeling communication** = Scheduling the **original graph with communication**.

This trick was proposed in the referenced book by El-Rewini et al. (1994).

---

## 🧠 Step-by-Step Summary of the Algorithm:

### 1. **Input**: An **in-forest** graph (each node has at most one successor).

### 2. **Find Siblings**:

* A set of **siblings** are nodes that share a **common child**.
* Example: If `b → d` and `c → d`, then `b` and `c` are siblings (both dependents of `d`).

### 3. **Choose the Deepest Sibling**:

* For each sibling group $S_i$, pick the node with **maximum depth** (most work before it).
* That node will **keep the original edge** to the child.

### 4. **Modify Edges (Augment)**:

* For all other siblings $v \in S_i$ (except the deepest one `u`):

  * Remove edge $(v, \text{child}(S_i))$
  * Add new edge $(v, u)$
    This makes `v` dependent on `u`, which in turn is still connected to the original child.

This means:

* `v` → `u` → `child(Si)`
  So if `v` and `u` are on the **same processor**, communication is **avoided**!

---

## 🔁 `swap_all` Operation:

### What it does:

If `u` and `child(Si)` are scheduled **one after the other** on **different processors**, you can **swap the later tasks** between those processors to bring `u` and `child(Si)` on the **same processor**.

### Why?

To **minimize communication** — if two dependent tasks are on the same processor, **no communication delay** is needed.

---

## 📌 Summary:

| Step              | Purpose                                         |
| ----------------- | ----------------------------------------------- |
| Augment the graph | Add edges to simulate communication             |
| Depth calculation | Identify scheduling priority                    |
| Sibling analysis  | Modify graph to prefer deeper nodes             |
| `swap_all`        | Optimize final schedule to reduce communication |

---
