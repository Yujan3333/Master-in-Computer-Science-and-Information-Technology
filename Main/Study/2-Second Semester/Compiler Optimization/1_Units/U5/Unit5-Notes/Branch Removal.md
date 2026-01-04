# 1️⃣ What is “Branch Removal (Forward Branches)”?

### Core idea (in simple words)

> **Replace forward branches (`GOTO`) with boolean conditions (guards)** so that:

* control dependence is removed
* execution becomes **conditional**, not **jump-based**
* code becomes **vectorizable**

This is an extension of **IF-conversion**, applied to **multiple forward branches**.

---

# 2️⃣ The “cc” (controlling condition) idea

The notes say:

> Maintain a boolean expression `cc` that represents the condition that must be true for the current statement to be executed.

Think of `cc` as:

> “Under what condition can execution reach this statement?”

Instead of jumping, we **remember conditions**.

---

# 3️⃣ Original code: understand control flow first

```fortran
DO I = 1, N
C1  IF (A(I) > 10) GOTO 60
20  A(I) = A(I) + 10
C2  IF (B(I) > 10) GOTO 80
40  B(I) = B(I) + 10
60  A(I) = B(I) + A(I)
80  B(I) = A(I) - 5
END DO
```

---

## 3.1 Control-flow reasoning (VERY IMPORTANT)

Let:

* `M1 = (A(I) > 10)`
* `M2 = (B(I) > 10)`

---

### Statement 20

```fortran
A(I) = A(I) + 10
```

Executed **only if**:

* `C1` is false → `A(I) ≤ 10`

✔ Condition: `!M1`

---

### Statement 40

```fortran
B(I) = B(I) + 10
```

Executed only if:

* `C1` is false **and**
* `C2` is false

✔ Condition: `!M1 AND !M2`

---

### Statement 60

```fortran
A(I) = B(I) + A(I)
```

Reachable if:

* `C1` is true (direct jump), **OR**
* `C1` false and `C2` false (fall-through)

✔ Condition:

```
(M1) OR (!M1 AND !M2)
```

Simplifies to:

```
M1 OR !M2
```

---

### Statement 80

```fortran
B(I) = A(I) - 5
```

Reachable in **all paths**:

* from 60
* or from `C2` true
* or by fall-through

✔ Always executed → **no guard needed**

---

# 4️⃣ Why we introduce M1 and M2

```fortran
M1 = A(I) > 10
M2 = B(I) > 10
```

This:

* avoids recomputation
* makes conditions explicit
* allows **vector masks**

📌 This is exactly how vector processors think.

---

# 5️⃣ Guarded (branch-free) version — explained

```fortran
DO I = 1, N
  M1 = A(I) > 10

  IF (!M1)
     A(I) = A(I) + 10
  END IF

  IF (!M1)
     M2 = B(I) > 10
  END IF

  IF (!M1 AND !M2)
     B(I) = B(I) + 10
  END IF

  IF (M1 OR !M2)
     A(I) = B(I) + A(I)
  END IF

  B(I) = A(I) - 5
END DO
```

### What changed?

| Original           | After branch removal |
| ------------------ | -------------------- |
| GOTO               | Boolean guards       |
| Control dependence | Data dependence      |
| Unstructured flow  | Structured           |
| Not vectorizable   | Vectorizable         |

---

# 6️⃣ Why simplification is valid

Original guard for statement 60:

```
(M1) OR (!M1 AND !M2)
```

Boolean simplification:

```
= M1 OR !M2
```

📌 **Very common exam step** — they expect you to simplify guards.

---

# 7️⃣ Vectorized version — why it works

```fortran
M1(1:N) = A(1:N) > 10

WHERE (!M1)
  A(1:N) = A(1:N) + 10
END WHERE

WHERE (!M1)
  M2 = B(1:N) > 10
END WHERE

WHERE (!M1 AND !M2)
  B(1:N) = B(1:N) + 10
END WHERE

WHERE (M1 OR !M2)
  A(1:N) = B(1:N) + A(1:N)
END WHERE

B(1:N) = A(1:N) - 5
```

### Why safe?

* `WHERE` applies condition **element-wise**
* No jumps
* Each iteration independent
* Matches original semantics

✔ Forward branches successfully removed
✔ Control dependence eliminated
✔ Vectorization enabled

---

# 8️⃣ Why this works ONLY for forward branches

### Forward branches:

* Skip code ahead
* Can be replaced by guards

### Backward branches:

* Define loops
* Cannot be removed this way

### Exit branches:

* Change loop bounds
* Hard to vectorize

📌 That’s why your note says:

> Backward branch & Exit branch → refer notes

---

# 9️⃣ One-paragraph exam answer (write this)

> Branch removal for forward branches eliminates control dependence by replacing branch instructions with boolean guards. During a pass over the program, the compiler maintains controlling conditions and inserts them as conditional expressions on statements. Forward branches are converted into guarded assignments, allowing safe vectorization using WHERE constructs. This technique does not apply to backward or exit branches.

---

# 🔟 Key takeaway (remember this line)

> **Forward branch removal = IF-conversion + guard propagation**

---
