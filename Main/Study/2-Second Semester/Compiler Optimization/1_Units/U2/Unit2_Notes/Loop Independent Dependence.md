
## 1️⃣ Loop-Independent Dependence (LID)

### 🔹 Definition

A **loop-independent dependence** occurs when **two statements in the *same iteration*** of a loop depend on each other.

➡️ The dependence exists **even if the loop runs only once**.

---

### 🔹 Example

```c
for (i = 0; i < n; i++) {
    A[i] = B[i] + 1;   // S1
    C[i] = A[i] * 2;  // S2
}
```

### 🔹 Explanation

* In the **same iteration i**:

  * `S2` uses `A[i]` produced by `S1`
* So `S2` **depends on `S1` within the same loop iteration**

✔️ This is **loop-independent dependence**

---

### 🔹 Impact on Optimization

* **Cannot reorder S1 and S2 within the same iteration**
* **Iterations can still be parallelized** if no other dependency exists

---
