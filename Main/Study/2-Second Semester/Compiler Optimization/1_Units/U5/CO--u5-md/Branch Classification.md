## Why branch classification matters (big picture)

> **Control dependence arises because of branch instructions**, since they change the normal flow of execution.

Compilers classify branches to:

* understand **control dependence**
* decide **vectorization / IF-conversion**
* analyze **loop behavior**

---

## 1️⃣ Forward Branch

### Definition (expanded)

A **forward branch** transfers control to a statement that appears **later in the program text**, at the **same nesting level**.

📌 “Forward” = jump **ahead** in code

---

### Example

```fortran
DO I = 1, N
   IF (A(I) < 0) GOTO 100
   X = X + 1
100 CONTINUE
END DO
```

### What happens?

* If condition is true → skip `X = X + 1`
* Control jumps **forward** to label `100`

---

### Why forward branches cause problems

* They **skip statements**
* Statements after the branch become **control dependent**
* Prevent straightforward vectorization

📌 In your earlier example:

```fortran
IF (A(I-1) > 0) GOTO 100
A(I) = A(I) + B(I) * C
```

➡️ This is a **forward branch**
➡️ `A(I) = ...` is **control dependent**

---

### Exam line ✍️

> A forward branch skips a region of code and introduces control dependence on the skipped statements.

---

## 2️⃣ Backward Branch

### Definition (expanded)

A **backward branch** transfers control to a statement that appears **earlier in the program text**, at the **same nesting level**.

📌 “Backward” = jump **back** in code

---

### Example

```fortran
10 CONTINUE
A = A + 1
IF (A < 100) GOTO 10
```

### What does this represent?

* This is how **loops are implemented internally**
* Control jumps **back** to repeat execution

---

### Why backward branches are usually safe

* They define **iteration**
* Highly predictable
* Do **not introduce control dependence inside the loop body**

📌 Compilers **expect** backward branches in loops.

---

### Exam line ✍️

> A backward branch is typically used to implement loops and does not inhibit vectorization.

---

## 3️⃣ Exit Branch

### Definition (expanded)

An **exit branch** transfers control **out of one or more loops**, terminating loop execution.

---

### Example (C-style)

```c
for (i = 0; i < N; i++) {
    if (A[i] == 0)
        break;
    sum += A[i];
}
```

### Example (Fortran-style)

```fortran
DO I = 1, N
   IF (A(I) == 0) EXIT
   SUM = SUM + A(I)
END DO
```

---

### Why exit branches are difficult

* Loop bounds become **data-dependent**
* Compiler does not know:

  * how many iterations will execute
* Vectorization becomes **unsafe**

---

### Exam line ✍️

> Exit branches alter loop termination and generally inhibit vectorization.

---

## 🔁 Comparison Table (Very Exam Useful)

| Branch Type | Direction    | Purpose         | Effect on Optimization    |
| ----------- | ------------ | --------------- | ------------------------- |
| Forward     | Ahead        | Skip code       | Causes control dependence |
| Backward    | Back         | Loop repetition | Safe, predictable         |
| Exit        | Outside loop | Terminate loop  | Hard to vectorize         |

---

## 🔑 One-paragraph exam answer (ready to write)

> Control dependence arises due to branch instructions that alter the normal flow of execution. Branches are classified as forward branches, backward branches, and exit branches. A forward branch transfers control to a statement appearing later in the program and introduces control dependence. A backward branch transfers control to an earlier statement and is typically used to implement loops. An exit branch transfers control outside a loop nest, terminating loop execution and generally inhibiting vectorization.

---

## 🧠 Link to what you studied earlier

* **Forward branch** → causes **control dependence** → needs **IF-conversion**
* **Backward branch** → loop structure → usually OK
* **Exit branch** → limits vectorization

---
