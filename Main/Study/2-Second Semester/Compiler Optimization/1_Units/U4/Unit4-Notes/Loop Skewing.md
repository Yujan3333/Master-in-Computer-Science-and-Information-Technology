
## **Loop Skewing**

**Definition:**
Loop skewing is a **loop transformation technique** used in compiler optimization to **change the iteration space of nested loops** in order to:

1. **Enable parallel execution**
2. **Improve data locality**
3. **Avoid loop-carried dependencies**

It’s often used **before vectorization or parallelization**.

---

### **Idea**

* **Nested loops** sometimes have dependencies between iterations that prevent **parallel execution**.
* **Skewing** modifies the loop indices so that the **dependencies are preserved**, but the loops can now be **executed in parallel**.

---

### **Example**

Original loop:

```c
for (i = 1; i <= N; i++)
    for (j = 1; j <= N; j++)
        a[i][j] = a[i-1][j] + a[i][j-1];
```

* Problem: `a[i][j]` depends on **previous row (`i-1`)** and **previous column (`j-1`)**
* This **loop-carried dependency** prevents parallel execution along `i` or `j`.

---

### **Skewed loop**

```c
for (i = 1; i <= N; i++)
    for (j = i; j <= N+i-1; j++)
        a[i][j-i+1] = a[i-1][j-i+1] + a[i][j-i];
```

* Dependency along **diagonals** is preserved.
* Iterations along the **new inner loop** can now be executed **in parallel**.

---

### **Steps for Loop Skewing**

1. Identify **nested loops** with loop-carried dependencies.
2. Choose a **skewing factor** to transform the inner loop index:

$$ j' = j + k \cdot i $$

* `k` = skewing factor
* Shifts the **iteration space diagonally**.

3. Rewrite the loops using the **new indices**.
4. Ensure dependencies are **maintained**, but loops can be **parallelized/vectorized**.

---

### **Key Points**

* Loop skewing is mainly used in **scientific computing / matrix operations**.
* Allows **parallelism along previously dependent loops**.
* Often combined with **loop tiling/blocking** for cache optimization.

---

### **Step 1: Original Nested Loop**

```c
for (i = 1; i <= 3; i++)
    for (j = 1; j <= 3; j++)
        a[i][j] = a[i-1][j] + a[i][j-1];
```

**Iteration Space (i,j) Table:**

| i \ j | 1     | 2     | 3     |
| ----- | ----- | ----- | ----- |
| 1     | (1,1) | (1,2) | (1,3) |
| 2     | (2,1) | (2,2) | (2,3) |
| 3     | (3,1) | (3,2) | (3,3) |

* **Dependencies:**

  * `a[i][j]` depends on `(i-1,j)` → previous row
  * `a[i][j]` depends on `(i,j-1)` → previous column

* Cannot run inner loop in parallel.

---

### **Step 2: Apply Loop Skewing**

* Transform `j` to a **new index**:

$$ j' = j + i - 1 $$

* Skewed loop:

```c
for (i = 1; i <= 3; i++)
    for (j = i; j <= i + 2; j++)
        a[i][j-i+1] = a[i-1][j-i+1] + a[i][j-i];
```

---

### **Skewed Iteration Space (i, j') Table**

| i \ j' | 1     | 2     | 3     | 4     | 5     |
| ------ | ----- | ----- | ----- | ----- | ----- |
| 1      | (1,1) | (1,2) | (1,3) |       |       |
| 2      |       | (2,1) | (2,2) | (2,3) |       |
| 3      |       |       | (3,1) | (3,2) | (3,3) |

* Iterations are now along **diagonals**.
* Each diagonal can be executed **in parallel**.
* Example diagonal: `(1,3)`, `(2,2)`, `(3,1)` → independent.

---

### **Step 3: Parallelism Enabled**

* Original loop → sequential execution.
* Skewed loop → diagonals can run **in parallel**.
* Enables **vectorization** and **parallel execution**.

---

### **Visual Diagram**

```
Original iteration space (i,j):

(1,1)  (1,2)  (1,3)
(2,1)  (2,2)  (2,3)
(3,1)  (3,2)  (3,3)

Dependencies: arrows pointing up (i-1) and left (j-1)

After skewing (i,j'):

(1,1)  (1,2)  (1,3)
       (2,1)  (2,2)  (2,3)
              (3,1)  (3,2)  (3,3)

Diagonals → parallel execution
```

---

### **Exam Tip**

> **Loop skewing** = shifting inner loop indices to preserve dependencies while enabling **parallelism** and **vectorization**.

---

