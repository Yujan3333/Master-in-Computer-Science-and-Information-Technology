## 2️⃣ Loop-Carried Dependence (LCD)

### 🔹 Definition

A **loop-carried dependence** occurs when **one iteration depends on a previous iteration**.

➡️ Data flows **from iteration i to iteration i+1 (or later)**.

---

### 🔹 Example

```c
for (i = 1; i < n; i++) {
    A[i] = A[i-1] + 1;   // S
}
```

### 🔹 Explanation

* Iteration `i` needs the value from iteration `i-1`
* So:

  * Iteration `i` **cannot execute before** iteration `i-1`

✔️ This is **loop-carried dependence**

---

### 🔹 Impact on Optimization

* **Prevents parallel execution of loop iterations**
* Limits:

  * Loop unrolling
  * Vectorization
  * Parallelization

---
