#second-semester #compiler-optimization #old-que 

---

## **Question 3**

### **a) What do you mean by ZIV, SIV, and MIV?**

**Answer:**
These are **subscript categories** used in dependence analysis to classify array subscript expressions based on the number of loop index variables they contain (Unit 2, Page 40–41).

---

### **ZIV (Zero Index Variable)**

A subscript expression that contains **no loop index variable**.

**Example:**

```fortran
DO I = 1, 100
    A(10) = A(20) + B(I)   ← '10' and '20' are ZIV
END DO
```

---

### **SIV (Single Index Variable)**

A subscript expression that contains **exactly one loop index variable**.

**Example:**

```fortran
DO I = 2, N
    A(2*I) = A(2*I + 2)   ← Only 'I' appears
END DO
```

---

### **MIV (Multiple Index Variable)**

A subscript expression that contains **more than one loop index variable**.

**Example:**

```fortran
DO I = 1, N
    DO J = 1, N
        A(2*I + 3*J) = ...   ← Both 'I' and 'J' appear
    END DO
END DO
```

---

## **b) Define induction variable and perform optimization in the following program**

### **Definition of Induction Variable** (Unit 3, Page 45)

An **induction variable** is a variable that increases or decreases by a fixed amount on each iteration of a loop, often as a linear function of the loop index.

**Example:**

```c
for (I = 0; I < N; I++) {
    J = 4 * I + 3;   // J is an induction variable
}
```

---

### **Program given**

```c
FOR (I = 0; I < N; I++) {
    J = 4 * I + 3;
    Y = f(J);
}
```

---

### **Step 1: Identify the induction variable**

Here, `J` is an **induction variable** because it is defined as `J = 4 * I + 3`, which is a linear function of the loop index `I`.

---

### **Step 2: Apply Induction Variable Optimization (Strength Reduction)**

Instead of recomputing `4 * I + 3` in each iteration, we can:

1. **Initialize `J` before the loop** using the formula when `I = 0`:

   ```
   J = 4 * 0 + 3 = 3
   ```
2. **Increment `J` by 4** in each iteration (since the coefficient of `I` is 4).

---

### **Step 3: Remove the redundant computation** from the loop body

---

### **Optimized Code**

```c
J = 3;
FOR (I = 0; I < N; I++) {
    Y = f(J);
    J = J + 4;
}
```

---

### **Why this is better**

* Replaces a **multiplication and addition** (`4*I + 3`) with a simple **addition** (`J + 4`) per iteration
* Reduces computational cost, especially for large `N`
* This is a standard **induction variable elimination** transformation (Unit 3, Pages 45–49)

---

## **Final Answer Summary**

1. **ZIV** = No loop index in subscript
   **SIV** = One loop index
   **MIV** = Multiple loop indices

2. **Induction variable** = Variable that changes linearly with loop index

3. **Optimized program** replaces `J = 4*I + 3` with incremental update `J = J + 4`

---
