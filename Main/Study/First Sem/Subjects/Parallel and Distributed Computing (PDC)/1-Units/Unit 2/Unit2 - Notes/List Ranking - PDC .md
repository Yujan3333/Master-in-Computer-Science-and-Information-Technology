
[List Ranking - AC](../../../../Algorithm%20and%20Complexity%20(AC)/1-Units/Unit%203/Unit3%20-%20Notes/List%20Ranking.md)

---

## 🧠 Problem:

Given a singly linked list:

$$
\text{A} \rightarrow \text{B} \rightarrow \text{C} \rightarrow \text{D} \rightarrow \text{null}
$$

You want to compute, **for each node**, the **distance (number of hops)** from that node to the **end**.

| Node | Distance to End |
| ---- | --------------- |
| A    | 3               |
| B    | 2               |
| C    | 1               |
| D    | 0               |

---

## 🧩 Parallel Algorithm (Pointer Jumping)

### 🔁 Loop (repeats until all next pointers are null):

```plaintext
For each node i, do in parallel:
    i.d = i.d + i.next.d
    i.next = i.next.next
```

Let’s explain this in steps.

---

### 🔄 Initial Setup:

For each node:

* `i.d = 1` (1 hop to its next)
* If `i.next == null`, then `i.d = 0` (end of list)

---

### ✅ What is pointer jumping doing?

The idea is:

* Instead of moving one step at a time (A → B → C → D), we **jump over nodes** using:

  * `i.next = i.next.next`
  * That is, skip one node ahead

At the same time:

* We **accumulate the distance**:

  * `i.d = i.d + i.next.d`

So in each round, every node learns how far its **next-next** is from the end and adds that to its own distance.

---

## 💡 Example Walkthrough

List: A → B → C → D → null

Initialize:

* A.d = 1, A.next = B
* B.d = 1, B.next = C
* C.d = 1, C.next = D
* D.d = 0, D.next = null

---

### 🔁 Round 1:

Each node updates in parallel:

#### Node A:

* A.d = 1 + B.d = 1 + 1 = 2
* A.next = B.next = C

#### Node B:

* B.d = 1 + C.d = 1 + 1 = 2
* B.next = C.next = D

#### Node C:

* C.d = 1 + D.d = 1 + 0 = 1
* C.next = D.next = null

#### Node D:

* Already at end, unchanged.

---

Now:

| Node | d | next |
| ---- | - | ---- |
| A    | 2 | C    |
| B    | 2 | D    |
| C    | 1 | null |
| D    | 0 | null |

---

### 🔁 Round 2:

Only nodes with `i.next ≠ null` do updates.

#### Node A:

* A.d = 2 + C.d = 2 + 1 = 3
* A.next = C.next = null

#### Node B:

* B.d = 2 + D.d = 2 + 0 = 2 (no change)
* B.next = D.next = null

Now:

| Node | d | next |
| ---- | - | ---- |
| A    | 3 | null |
| B    | 2 | null |
| C    | 1 | null |
| D    | 0 | null |

---

✅ All `.next` pointers are null → **done**.

---

## 📘 Final Distances:

| Node | Distance |
| ---- | -------- |
| A    | 3        |
| B    | 2        |
| C    | 1        |
| D    | 0        |

---

## ⏱️ Time Complexity:

* Each round **halves the list** (you jump over one more node).
* Total rounds: $O(\log N)$
* Processors used: $O(N)$

---

## 🧠 Summary:

| Concept         | Explanation                               |
| --------------- | ----------------------------------------- |
| Pointer Jumping | Skip one node each round (jump ahead)     |
| Distance Update | Accumulate distance from jumped-over node |
| Goal            | Compute how far each node is from end     |
| Time            | $O(\log N)$                               |
| Processors      | $O(N)$, one per node                      |

---
