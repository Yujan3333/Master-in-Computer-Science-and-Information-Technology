
# 🔹 ZIV Test (Zero Index Variable)

### 1️⃣ What it says

> *ZIV subscripts contain no references to any loop induction variables.*
> *They do not vary within any loop.*

* **Meaning:**

  * A **ZIV subscript** is **completely constant within the loop**.
  * It does **not depend on the loop variable** (like `I` in your example).

**Example from the text:**

```fortran
DO I = 1, N
    A(e1) = A(e2) + B(I)
END DO
```

* `e1` and `e2` are **ZIV subscripts** because they **do not involve `I`**
* `B(I)` involves the loop variable → **not ZIV**

### 2️⃣ Dependence Analysis

* Since `A(e1)` and `A(e2)` are **fixed indices**, the compiler can **compare them at compile time**:

  * If `e1 != e2` → **no dependence** → statements can execute in **parallel**
  * If `e1 = e2` → dependence exists → must respect execution order

> ✅ **Key idea:** ZIV test is simple and fast because indices are **constant within the loop**.

---

# 🔹 SIV Test (Single Index Variable)

### 1️⃣ What it says

> *The image provides a hierarchy for SIV (Single Induction Variable): Strong, Weak, Zero, Crossing.*

* **SIV subscripts** involve **one loop variable linearly**, like `A[i]` or `A[i+1]`.
* Compiler must solve a **dependence equation** to see if two SIV accesses can refer to the **same memory location** in different iterations.

---

### 2️⃣ Classification Explained

| SIV Type     | Meaning                                                     | Example             |
| ------------ | ----------------------------------------------------------- | ------------------- |
| **Strong**   | Exact, guaranteed dependence across iterations              | `A[i+1] = A[i] + 1` |
| **Weak**     | Possible dependence, cannot resolve exactly at compile time | `A[2*i] = A[i] + 1` |
| **Zero**     | Dependence within **same iteration** (`i` vs `i`)           | `A[i] = A[i] + 1`   |
| **Crossing** | Dependence **across iterations** (`i` vs `i+k`)             | `A[i+1] = A[i] + 1` |

---

### 3️⃣ How They Are Used in Compiler Optimization

1. **ZIV Test** → check **loop-independent indices**

   * If no dependence → statements can run **in parallel** or **vectorized**
2. **SIV Test** → check **loop-dependent indices**

   * Solve integer equations to find **dependence distance** (`i - j`)
   * Strong SIV → strict ordering needed
   * Weak SIV → conservative assumption

---

### 🔹 Summary in Simple Words

* **ZIV:** indices are constant → check equality → simple → fast
* **SIV:** indices linear in loop variable → solve equation → may be strong/weak, zero/crossing
* Both are **tools to detect dependencies in loops**, enabling **parallelization and other optimizations**.

---

✅ **One-Line Golden Insight:**

> *“ZIV detects dependence with constant indices, SIV detects dependence with single-loop-variable indices; both help the compiler optimize loops safely.”*

---
