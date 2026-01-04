## **Section-Based Splitting**

### **Definition**

**Section-based splitting** is a **loop transformation technique** where a loop body is **divided into multiple sections** (loops) so that **independent statements are separated from dependent ones**.

* This helps in **parallelization**, **vectorization**, and **better scheduling**.
* Often used **after scalar expansion or dependence analysis**.

---

### **Idea (in simple words)**

* Some statements in a loop **depend on each other**.
* Some statements are **independent**.
* Instead of keeping everything in one loop, we **split the loop into sections**:

  * One section per group of dependent statements.

---

### **Example**

Original loop:

```fortran
DO I = 1, N
S1: X(I) = A(I) + B(I)
S2: Y(I) = C(I) * D(I)
S3: Z(I) = X(I) + Y(I)
END DO
```

* `S1` and `S2` are **independent**
* `S3` depends on results of `S1` and `S2`

---

### **After Section-Based Splitting**

```fortran
DO I = 1, N
S1: X(I) = A(I) + B(I)
S2: Y(I) = C(I) * D(I)
END DO

DO I = 1, N
S3: Z(I) = X(I) + Y(I)
END DO
```

---

### **Why This Helps**

| Benefit              | Explanation                              |
| -------------------- | ---------------------------------------- |
| Parallelism          | Independent sections can run in parallel |
| Vectorization        | Simpler loop bodies                      |
| Better scheduling    | Compiler can optimize each section       |
| Dependency isolation | Clear separation of dependent code       |

---

### **Relation to Scalar Expansion**

* Scalar expansion removes **false dependencies**.
* Section-based splitting then **separates independent computations** into different loops.
* Both together help in **parallel execution**.

---

### **Exam Tip (One-liner)**

> **Section-based splitting** divides a loop into multiple loops so that independent and dependent statements are separated, enabling parallelism and optimization.

---

### **Very Short Example (for memory)**

Before:

```fortran
DO I = 1, N
A(I) = B(I)
C(I) = D(I)
END DO
```

After splitting:

```fortran
DO I = 1, N
A(I) = B(I)
END DO

DO I = 1, N
C(I) = D(I)
END DO
```

---
