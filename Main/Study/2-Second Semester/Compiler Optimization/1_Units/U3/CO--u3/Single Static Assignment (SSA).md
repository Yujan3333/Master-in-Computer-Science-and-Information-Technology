Ah! You want **SSA – Single Static Assignment**, a fundamental concept in compiler optimization. Let’s explain it **clearly, step by step**, exam-style.

---

## **Single Static Assignment (SSA)**

**Definition:**
A program is in **SSA form** if **each variable is assigned exactly once** and **every variable is defined before it is used**.

* To achieve this, **new variable names** are introduced for multiple assignments to the same variable.
* Makes **data-flow analysis, constant propagation, and dead code elimination** much easier.

---

### **Example**

Original code:

```c
a = 5
b = a + 3
a = 7
c = a + b
```

* Notice `a` is assigned **twice**.

Convert to SSA:

```c
a1 = 5
b1 = a1 + 3
a2 = 7
c1 = a2 + b1
```

✅ Now, **each variable is assigned exactly once**.

---

### **Handling Branches (Φ-functions)**

SSA introduces **Φ (phi) functions** to merge values from different control paths.

**Example:**

```c
if (x > 0) {
    a = 1
} else {
    a = 2
}
b = a + 5
```

* Two assignments to `a` → SSA needs **φ-function** to merge:

```c
if (x > 0) {
    a1 = 1
} else {
    a2 = 2
}
a3 = φ(a1, a2)
b1 = a3 + 5
```

* `φ(a1, a2)` means: "if control came from then-branch, use a1; else use a2."

##### Sir Example
![](../../../../../../../Images/Second_Sem_Images/Single%20Static%20Assignment%20(SSA).png)

---

### **Algorithm to Convert to SSA (High-Level)**

1. **Rename variables** so that each assignment gets a **unique name**.
2. **Insert φ-functions** at **join points** in the control flow graph (CFG) for variables assigned in multiple paths.
3. **Replace variable uses** with the correct SSA name.

---

### **Benefits of SSA**

1. **Simplifies optimization:**

   * Constant propagation
   * Dead code elimination
   * Copy propagation

2. **Easy to perform liveness analysis:**

   * Each variable is assigned once → no ambiguity about which definition reaches a use.

3. **Facilitates parallelization** and other advanced compiler optimizations.

---

### **Example Combining Everything**

Original code:

```c
x = 5
y = x + 3
x = 7
z = x + y
```

SSA form:

```c
x1 = 5
y1 = x1 + 3
x2 = 7
z1 = x2 + y1
```

With **if-else branch**:

```c
if (cond) {
    a1 = 10
} else {
    a2 = 20
}
a3 = φ(a1, a2)
b1 = a3 + 5
```

---

✅ **Key points for exam:**

1. **SSA guarantees:** each variable assigned once.
2. **Φ-function:** needed at control flow joins.
3. Makes **data-flow analysis** and optimizations easier.
4. Used in **modern compilers** like LLVM and GCC internally.

---
