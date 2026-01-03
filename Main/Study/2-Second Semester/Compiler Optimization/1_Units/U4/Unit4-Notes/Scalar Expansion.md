
## **Scalar Expansion**

**Definition:**
Scalar expansion is a **compiler optimization** where a **scalar variable** (single value) inside a loop is **replaced by an array** so that **each iteration gets its own copy**.

* This helps to **eliminate loop-carried dependencies** and **enable parallelization or vectorization**.

---

### **Example**

Original code (dependency prevents parallelism):

```c
sum = 0
for (i = 1; i <= 4; i++)
    sum = sum + a[i]
```

* `sum` is a **scalar**, updated in each iteration → dependency between iterations.

---

**After Scalar Expansion:**

```c
for (i = 1; i <= 4; i++)
    sum[i] = a[i]
```

* Each iteration writes to a **separate location** → no dependency.
* Now the loop can be **parallelized**.

---

### **Key Points**

1. Converts **scalar variables** to **arrays**.
2. Eliminates **loop-carried dependencies**.
3. Enables **parallelization/vectorization**.
4. Often used in **loops with reductions**.

---

**Exam Tip:**

> Scalar expansion = replace scalar by array to remove dependencies and allow parallel execution.

---
