![](../../../../../../../Images/Second_Sem_Images/Exam%20Numerical%20-%20IF%20Conversion.png)

---
# 🔁 Iterative Dependence and IF-Conversion

## 1️⃣ What is Iterative Dependence?

**Iterative dependence (loop-carried dependence)** occurs when:

* an operation in iteration $i$ depends on
* an operation in iteration $i-1$ (or earlier)

### Two types involved here:

### 🔹 Data Dependence

A value produced in one iteration is used in the same or next iteration.

### 🔹 Control Dependence

Execution of a statement depends on a **branch decision** (`IF`, `GOTO`) taken earlier in the loop.

📌 **Problem:**
Control dependences prevent:

* parallel execution
* vectorization
* software pipelining

---

## 2️⃣ Why IF-Conversion is Needed

The original loop contains **multiple GOTOs**, which create:

* multiple paths
* multiple exits
* complex control dependences

👉 Compilers cannot easily reorder or parallelize such loops.

### ✅ IF-Conversion solves this by:

* removing branches
* replacing them with **predicated execution**
* converting **control flow → data flow**

---

## 3️⃣ Original Code (With Control Dependence)

```fortran
DO I = 1, N
    IF (A(I) > 10) GOTO 100
200 A(I) = A(I) + 10

    IF (B(I) > 10) GOTO 300
400 B(I) = B(I) + 10

100 A(I) = B(I) + A(I)
300 B(I) = A(I) - 5
END DO
```

---

## 4️⃣ Understanding the Control Flow (Very Important)

Let:

* $C_1$: $A(I) > 10$
* $C_2$: $B(I) > 10$

### Execution Rules

| Statement             | Executes when                         |
| --------------------- | ------------------------------------- |
| `200: A(I)=A(I)+10`   | $C_1$ is false                        |
| `400: B(I)=B(I)+10`   | $C_1$ is false **and** $C_2$ is false |
| `100: A(I)=B(I)+A(I)` | $C_2$ is false                        |
| `300: B(I)=A(I)-5`    | Always executes                       |

📌 **Key insight**
Statement `100` is skipped **only if** we jump to `300`.

---

## 5️⃣ Predicate Definitions (IF-Conversion Step)

Define logical masks:

* $P_1 = (A(I) \le 10)$
* $P_2 = (B(I) \le 10)$

These predicates replace branches.

---

## 6️⃣ IF-Converted Code (Branch-Free)

```fortran
DO I = 1, N

    P1 = (A(I) <= 10)
    P2 = (B(I) <= 10)

    ! Statement 200
    IF (P1) A(I) = A(I) + 10

    ! Statement 400
    IF (P1 .AND. P2) B(I) = B(I) + 10

    ! Statement 100
    IF (P2) A(I) = B(I) + A(I)

    ! Statement 300 (always executes)
    B(I) = A(I) - 5

END DO
```

---

## 7️⃣ What IF-Conversion Achieves

### ✅ Control dependences eliminated

* No `IF–GOTO`
* No jumps

### ✅ Single entry and exit

* Easier dependence analysis

### ✅ Compiler-friendly loop

* Vectorization possible
* Software pipelining possible
* Better instruction scheduling

---

## 8️⃣ Exam-Ready Summary (Write This!)

> IF-conversion eliminates control dependence by replacing conditional branches with predicated execution. It converts control flow into data flow using logical predicates, making loops suitable for parallelization and vectorization.

---

## 🏆 One-Line Golden Insight

> **IF-conversion removes branches by executing statements conditionally using predicates instead of jumps.**

---
