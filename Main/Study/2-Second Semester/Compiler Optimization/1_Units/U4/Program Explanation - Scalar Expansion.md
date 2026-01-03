## **Given Loop**

```fortran
DO I = 1, N
S1: T = A(I)
S2: A(I) = B(I)
S3: B(I) = T
END DO
```

* `T` is a **scalar variable** (single memory location) used **inside the loop**.
* It temporarily stores a value from `A(I)` to swap `A(I)` and `B(I)`.

---

### **Step 1: Look at the order of statements**

For iteration `i`:

1. `T = A(i)` → stores `A(i)` in `T`
2. `A(i) = B(i)` → writes `B(i)` into `A(i)`
3. `B(i) = T` → writes the old `A(i)` into `B(i)`

* So `T` holds **the temporary value of the current iteration**.

---

### **Step 2: Why dependency arises**

* Suppose the loop tried to **execute two iterations in parallel**, say `i` and `i+1`.
* Both iterations use **the same scalar `T`**.

---

**Iteration `i`**:

```
T = A(i)
A(i) = B(i)
B(i) = T
```

**Iteration `i+1` (parallel)**:

```
T = A(i+1)
A(i+1) = B(i+1)
B(i+1) = T
```

* If these run at the same time, the `T` in iteration `i+1` will **overwrite** the `T` from iteration `i`.
* That means `B(i)` may get **wrong value**.

✅ This is the **loop-carried dependency caused by scalar `T`**.

---

### **Step 3: How Scalar Expansion Fixes It**

* Replace `T` by an array `T(I)` so that **each iteration has its own copy**:

```fortran
DO I = 1, N
S1: T(I) = A(I)
S2: A(I) = B(I)
S3: B(I) = T(I)
END DO
```

* Now there’s **no dependency between iterations**, because `T(i)` and `T(i+1)` are **different memory locations**.
* Loop can be **parallelized safely**.

---

### **Step 4: Visualizing Dependency**

**Without scalar expansion (T is shared):**

```
Iteration i:   T <- A(i)
Iteration i+1: T <- A(i+1)  (overwrites T from i)
```

**With scalar expansion (T(I) array):**

```
Iteration i:   T(i) <- A(i)
Iteration i+1: T(i+1) <- A(i+1)  (no conflict)
```

---

### ✅ **Summary**

* Scalar `T` is **shared across iterations** → causes **loop-carried dependency**.
* Dependency prevents **parallel execution**.
* **Scalar expansion** (`T(I)`) solves this → each iteration has **its own copy of T**.

---
