# 🔹 Iteration Vector 

## 1️⃣ What problem does an iteration vector solve?

When loops are **nested**, the same statement runs **many times**.

Example:

```fortran
DO I = 1, 3
  DO J = 1, 2
    S1
  END DO
END DO
```

👉 Statement `S1` executes **6 times**.

So the compiler asks:

* Which execution happened **before** which?
* Do two executions access the **same memory**?
* Can we **reorder or parallelize** these executions safely?

To answer this, we need a **precise way to name each execution**.

➡️ That is exactly what an **iteration vector** does.

---

## 2️⃣ What is an Iteration Vector? (Very simple)

### 📌 In simple words:

> An **iteration vector** tells us **which iteration of each loop** a statement execution belongs to.

Think of it as a **coordinate** or **address** of that execution inside nested loops.

---

## 3️⃣ Formal Definition (Exam-ready)

In a nest of (n) loops, the **iteration vector** of an execution of a statement is:

$$[ 
 \vec{i} = (i_1, i_2, \dots, i_n)
]$$

where:

* ($i_1$) → iteration number of **outermost loop**
* ($i_2$) → iteration number of next loop
* …
* ($i_n$) → iteration number of **innermost loop**

---

## 4️⃣ Basic Example (Very Important)

```fortran
DO I = 1, 2
  DO J = 1, 2
    S1
  END DO
END DO
```

### All executions of `S1`:

| I | J | Iteration Vector |
| - | - | ---------------- |
| 1 | 1 | (1, 1)           |
| 1 | 2 | (1, 2)           |
| 2 | 1 | (2, 1)           |
| 2 | 2 | (2, 2)           |

➡️ This complete set is called the **iteration space**.

📌 If `I = 2` and `J = 1`, the iteration vector is:
$$[
(2, 1)
]$$

---

## 5️⃣ Why “iteration number” and not index value?

Consider:

```fortran
DO I = 0, 10, 2
```

Here:

* Index values are: 0, 2, 4, 6, 8, 10
* But iteration numbers are: 1, 2, 3, 4, 5, 6

📌 Formula used in theory:

$$[
\text{Index value} = L + (k-1)S
]$$

where:

* (k) = iteration number
* (L) = lower bound
* (S) = step size

➡️ **Iteration vector always uses iteration numbers**, not raw index values.

---

## 6️⃣ Why Iteration Vectors are IMPORTANT (Core reason)

### 🔴 Dependence Analysis

Suppose:

* One execution writes to memory
* Another execution reads the same memory

To check dependence, compiler compares:

$$[
\vec{i} = (i_1, i_2, \dots) \quad \text{and} \quad \vec{j} = (j_1, j_2, \dots)
]$$

If:

* Same memory location
* $(\vec{i}) happens **before** (\vec{j})$

➡️ **Loop-carried dependence exists**

---

## 7️⃣ Distance Vector (using iteration vectors)

If dependence exists from:
$$[
\vec{i} = (2, 3, 5)
\quad \rightarrow \quad
\vec{j} = (3, 3, 4)
]$$

### Distance vector:

$$[
\vec{d} = \vec{j} - \vec{i} = (1, 0, -1)
]$$

Meaning:

* Outer loop: next iteration
* Middle loop: same iteration
* Inner loop: earlier iteration

---

## 8️⃣ Direction Vector (even simpler)

Direction vector shows **ordering**, not magnitude:

| Difference | Direction |
| ---------- | --------- |
| positive   | `<`       |
| zero       | `=`       |
| negative   | `>`       |

So:
$$[
(1, 0, -1) \Rightarrow (<, =, >)
]
$$
---

## 9️⃣ Why iteration vectors matter in transformations

When compiler does:

* Loop interchange
* Loop skewing
* Loop tiling

➡️ Execution **order changes**

But:

> Dependence defined using iteration vectors **must not be violated**

So iteration vectors act like **rules** that transformations must respect.

---

## 🔟 One-line exam definition (VERY USEFUL)

> An iteration vector represents a specific execution of a statement in a loop nest by recording the iteration number of each enclosing loop.

---

## 🧠 Ultra-Simple Analogy (Easy to remember)

Think of a **nested loop like a building**:

* Floor number → outer loop
* Room number → inner loop

📌 Iteration vector = **(floor, room)**
It tells you **exactly where you are**.

---
