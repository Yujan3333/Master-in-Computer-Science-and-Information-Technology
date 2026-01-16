# 🔹 Topic: Constant Propagation & Alias Analysis

### 1️⃣ Constant Propagation

**Definition:**

* Constant propagation is a compiler optimization where the compiler replaces **variables known to hold constant values** with their constant value.

**Goal:**

* Improve performance by computing values at compile time instead of runtime.

---

### 2️⃣ The Example Code

```c
int x, y;
int *p;

p = &x;
x = 5;
*p = 42;
y = x + 1;
```

---

### 3️⃣ Step-by-Step Analysis

#### Step 1: Initialize

```
x = ?       (unknown)
y = ?       (unknown)
p = ?       (pointer)
```

---

#### Step 2: p = &x

* `p` now **points to x**
* So any write via `*p` modifies `x`

---

#### Step 3: x = 5

* `x` is assigned 5 → **constant so far**

```
x = 5
```

---

#### Step 4: *p = 42

* `p` points to `x`, so this **updates x**
* Now `x = 42`

```
x = 42
```

---

#### Step 5: y = x + 1

* What is the value of `x` here?

**Problem:**

* `x` was first 5, then potentially changed through `*p`
* Without **alias analysis**, the compiler cannot be sure if `x` was modified through `p`

✅ **Conclusion:**

* **x is not a constant**, because it can be changed via pointer alias `p`.
* So **constant propagation cannot replace `x` with 5** at compile time.

---

### 4️⃣ Alias Analysis

**Definition:**

* Alias analysis determines **if two expressions (like variables or pointers) refer to the same memory location**.

**In this example:**

* `p` aliases `x` (both refer to the same memory location)
* Any write via `p` **affects `x`**

**Key insight:**

* Compiler must check aliasing before propagating constants.
* If aliasing exists, constant propagation is **unsafe**.

---

### 5️⃣ Visual Flow of Values

| Step | Statement | x Value | Notes                                            |
| ---- | --------- | ------- | ------------------------------------------------ |
| 1    | int x, y  | ?       | uninitialized                                    |
| 2    | p = &x    | ?       | p points to x                                    |
| 3    | x = 5     | 5       | x assigned constant 5                            |
| 4    | *p = 42   | 42      | x updated via pointer                            |
| 5    | y = x + 1 | 43      | cannot assume x = 5 at compile time due to alias |

---

### 6️⃣ Exam Key Points

1. **x is not a constant** because it is **modified via an alias (`*p`)**.
2. **Alias analysis** is required before constant propagation.
3. Without alias analysis, compiler may incorrectly assume `x = 5` → **wrong code**.
4. Constant propagation is **safe only if no alias exists** that can modify the variable.

---

### 7️⃣ One-Line Takeaway

> **A variable cannot be treated as constant if it may be modified through an alias.**

---
