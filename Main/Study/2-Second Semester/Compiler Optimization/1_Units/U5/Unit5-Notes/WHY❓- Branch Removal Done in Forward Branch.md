
# Branch Removal – Special Cases

## i) Backward Branch

### What is a backward branch?

A **backward branch** transfers control to a statement that appears **lexically before** the branch at the **same nesting level**.

### Example

```fortran
10 A = A + 1
IF (A < 100) GOTO 10
```

This jump **goes backward** → loop repetition.

---

### Why backward branches are NOT removed

Backward branches:

* **Define loops**
* Represent **iteration**, not conditional skipping
* Removing them would destroy loop structure

❌ Cannot be converted into guarded execution
❌ Cannot be replaced by boolean masks

📌 Forward branch → skip code
📌 Backward branch → repeat code

---

### Compiler treatment

* Backward branches are:

  * recognized as **loop-closing branches**
  * preserved during optimization
* Compilers optimize them using:

  * loop unrolling
  * software pipelining
  * induction variable optimization

---

### Exam line ✍️

> Backward branches define loop iteration and hence are not removed during branch elimination.

---

## ii) Exit Branch

### What is an exit branch?

An **exit branch** transfers control **outside a loop nest**, terminating one or more loops.

### Example

```fortran
DO I = 1, N
   IF (A(I) == 0) EXIT
   SUM = SUM + A(I)
END DO
```

or

```fortran
IF (A(I) == 0) GOTO 200
...
200 CONTINUE
```

---

### Why exit branches are difficult to remove

Exit branches:

* Make loop bounds **data-dependent**
* Cause **early termination**
* Prevent full vector execution

If vectorized:

* Some iterations should stop early
* Vector processors cannot “partially stop”

❌ IF-conversion unsafe
❌ Guarding insufficient

---

### Compiler treatment

* Exit branches usually:

  * block vectorization
  * force scalar execution
* Limited handling:

  * loop splitting
  * peeling
  * speculation (rare)

---

### Exam line ✍️

> Exit branches alter loop termination and generally inhibit vectorization.

---

## 🔁 Summary Table (Very Important)

| Branch Type     | Removed? | Reason                     |
| --------------- | -------- | -------------------------- |
| Forward branch  | ✅ Yes    | Can be guarded             |
| Backward branch | ❌ No     | Defines loops              |
| Exit branch     | ❌ No     | Data-dependent termination |

---

## 🔑 One-paragraph exam answer (perfect for notes)

> Branch removal techniques apply only to forward branches, which skip code and introduce control dependence. Backward branches are used to implement loops and cannot be removed without destroying loop structure. Exit branches transfer control outside loop nests and cause data-dependent termination, thereby inhibiting vectorization. Hence, branch elimination is restricted to forward branches only.

---

## 🧠 Memory trick

* **Forward** → skip → guard → vectorize
* **Backward** → repeat → loop → keep
* **Exit** → terminate → unsafe → block

---
