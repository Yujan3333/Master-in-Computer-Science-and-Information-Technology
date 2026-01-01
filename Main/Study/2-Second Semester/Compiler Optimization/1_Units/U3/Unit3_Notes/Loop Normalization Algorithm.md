## Loop Normalization (What it Means)

**Loop normalization** is a compiler transformation that converts any loop into a **standard form**:

* **Lower bound = 1**
* **Step size = 1**

This makes **dependence testing easy and uniform** for the compiler.

---

## Why Compilers Normalize Loops

Loops may originally have:

* arbitrary lower bounds
* different step sizes

This makes dependency analysis **difficult**.

So compilers normalize loops **before performing optimizations** like:

* dependence testing
* parallelization
* loop interchange

---

## General Form of Original Loop

```fortran
DO I = L, U, S
   loop body
END DO
```

Where:

* `L` = lower bound
* `U` = upper bound
* `S` = step size

This loop is **not normalized** if `L ≠ 1` or `S ≠ 1`.

---

## Algorithm for Loop Normalization (Exam-Oriented)

### **Input**

Loop `L₀` to be normalized.

---

### **Step 1: Create a New Induction Variable**

* Let `k` be a **new compiler-generated induction variable**
* `k` will start from **1** and increase by **1**

---

### **Step 2: Replace the Loop Header**

Original loop:

```fortran
DO I = L, U, S
```

Normalized loop:

```fortran
DO k = 1, ⌊(U − L)/S⌋ + 1
```

Now:

* Lower bound = 1
* Step size = 1

---

### **Step 3: Replace All References to Old Variable**

Inside the loop body, replace every occurrence of `I` with:

$$
I = L + (k - 1) \times S
$$

This is a **linear function** of the new induction variable `k`.

---

## Why This Works

* `k` increases by **1**
* `I` increases by **S**
* Both loops execute the **same iterations**
* Only the form has changed, not the meaning

---

## Simple Example (Conceptual)

❌ Original loop:

```c
for (i = 3; i < N; i = i + 2)
```

✅ Normalized idea:

* New variable `k`
* Replace `i` with `3 + 2(k − 1)`
* Loop runs from `k = 1` with step `1`

---

## Definition (Perfect Exam Answer)

> Loop normalization is a transformation that converts loops with arbitrary bounds and step sizes into a standard form with lower bound 1 and step size 1 by replacing the original induction variable with a linear function of a new induction variable.

---

## Key Exam Keywords (Use These)

* dependence testing
* induction variable
* linear function
* compiler-generated variable
* standard loop form