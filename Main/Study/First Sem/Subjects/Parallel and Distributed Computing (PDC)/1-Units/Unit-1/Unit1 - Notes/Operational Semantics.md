
## ⚙️ **Operational Semantics**

### ✅ **Definition:**

**Operational semantics** defines the **meaning of a program** in terms of the **changes it makes to the program state** during execution.

It **focuses on the computation process**, step by step — showing **how each instruction modifies the state** of the system.

---

### 🔹 **Key Concepts:**

* **State**: A mapping of variable names to their values (e.g., $S = [x \mapsto 5, y \mapsto 7, z \mapsto 0]$)

* **Notation**:

  $$
  \langle P, S \rangle
  $$

  This denotes **"program P in state S"**

* **Execution** is shown as:

  $$
  \langle P, S \rangle \Rightarrow \langle P', S' \rangle
  $$

  Where:

  * $P'$: remaining part of the program after a step
  * $S'$: updated state

---

### 📘 **Example:**

Let’s evaluate the program:

```c
z = x; x = y; y = z;
```

With initial state:

$$
[x \mapsto 5, y \mapsto 7, z \mapsto 0]
$$

Step-by-step execution:

1. **First statement: `z = x`**

   $$
   \langle z = x, x = y, y = z, [x \mapsto 5, y \mapsto 7, z \mapsto 0] \rangle
   \Rightarrow \langle x = y, y = z, [x \mapsto 5, y \mapsto 7, z \mapsto 5] \rangle
   $$

2. **Second statement: `x = y`**

   $$
   \langle x = y, y = z, [x \mapsto 5, y \mapsto 7, z \mapsto 5] \rangle
   \Rightarrow \langle y = z, [x \mapsto 7, y \mapsto 7, z \mapsto 5] \rangle
   $$

3. **Third statement: `y = z`**

   $$
   \langle y = z, [x \mapsto 7, y \mapsto 7, z \mapsto 5] \rangle
   \Rightarrow \langle\;, [x \mapsto 7, y \mapsto 5, z \mapsto 5] \rangle
   $$

✅ Final state: `[x → 7, y → 5, z → 5]`

---

### 📝 **Exam-Style Answer:**

> **Operational semantics** defines program behavior by describing **how the state of the program changes during execution**.
> It uses the notation $\langle P, S \rangle$ to denote **program P in state S**, and tracks how each statement **modifies variables**.
>
> For example, executing `z = x; x = y; y = z;` starting from `[x → 5, y → 7, z → 0]`, the final state becomes `[x → 7, y → 5, z → 5]`, showing how the semantics describe computation **step by step**.

---
