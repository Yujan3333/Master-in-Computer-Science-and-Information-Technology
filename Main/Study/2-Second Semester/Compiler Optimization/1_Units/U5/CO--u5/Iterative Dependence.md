# Iterative Dependencies (Control Dependence from Loops)

Up to now, you saw **control dependence caused by branches** (`IF`, `GOTO`).
This section shows something more subtle and more dangerous:

> **Iteration constructs (`DO` loops) themselves create control dependence.**

This is often misunderstood, which is why **incorrect vectorization** happens.

---

## Original Program (Understand Execution First)

```fortran
20:  Do I = 1, 100          ! -> irange1()
40:    L = 2 * I
60:    Do J = 1, L          ! -> irange2()
80:      A(I, J) = 0
     End Do
     End Do
```

### What this code really does (semantics)

* Outer loop: `I = 1 to 100`
* Inner loop bound **depends on `I`**

  * `L = 2 * I`
  * `J = 1 to L`

So:

* When `I = 1` → `J = 1..2`
* When `I = 2` → `J = 1..4`
* When `I = 100` → `J = 1..200`

📌 **Important:**
Each row `A(I, :)` is filled only **up to column `2I`**.

This forms a **triangular (ragged) region**, not a rectangle.

---

## Visualizing the Write Pattern

What actually gets zeroed:

```
I = 1   → A(1, 1..2)
I = 2   → A(2, 1..4)
I = 3   → A(3, 1..6)
...
I = 100 → A(100, 1..200)
```

This is **not uniform across iterations**.

---

# The Dangerous Assumption

> “Iterative statements do not carry control dependence.”

If a compiler (or student!) assumes this, it may think:

* All iterations of `I` are independent
* All iterations of `J` are independent
* So let’s vectorize aggressively

---

## Incorrect Vectorization (Why it is WRONG)

```fortran
20:  Do I = 1, 100
40:    L = 2 * I
     End Do

     A(1:100, 1:L) = 0
```

### What this vectorized code actually means

* Compute **final value of `L`**

  * After loop: `L = 2 * 100 = 200`
* Then execute:

```fortran
A(1:100, 1:200) = 0
```

### Resulting write region

* **Rectangular region**
* Every row zeroed from column `1` to `200`

🚨 **This is NOT what the original program does**

---

## Key Difference (Very Important)

| Original Code                   | Incorrect Vectorization   |
| ------------------------------- | ------------------------- |
| Triangular region               | Rectangular region        |
| Inner loop bound depends on `I` | Bound treated as constant |
| Control dependence preserved    | Control dependence lost   |

---

## Why This Happens

Because the compiler **lost information** about:

> **How many times statement 80 executes for each `I`**

That information is not a data dependence — it is a **control dependence created by the loop bounds**.

---

# The Missing Concept: Iteration Control Dependence

### Core Insight

> A `DO` loop **controls the number of times** a statement executes.
> That control is a form of **control dependence**, even without branches.

So statement 80:

```fortran
A(I, J) = 0
```

is:

* Control dependent on the **inner loop**
* Which is itself control dependent on the **outer loop**

---

# Modeling This Properly: Iteration Ranges (irange)

To fix this, the compiler introduces a **formal model**:

> Each statement has an implicit **iteration range input**.

This answers:

* *Which iterations execute this statement?*

---

## Introducing `irange`

* `irange` = iteration range controlling execution
* Think of it as a **hidden condition** attached to a statement

---

## Code with Explicit Iteration Ranges

```fortran
20:  irange 1 = (1, 100)
     Do I = irange 1

40:    L = 2 * I                (irange 1)

60:    irange 2 = (1, L)        (irange 1)
       Do J = irange 2

80:      A(I, J) = 0            (irange 2)

       End Do
     End Do
```

---

## What This Means Conceptually

### `irange1 = (1, 100)`

* Controls **which values of `I` exist**

### `irange2 = (1, L)`

* Controls **which values of `J` exist**
* Depends on `I`

### Statement annotations

| Statement  | Controlled by |
| ---------- | ------------- |
| `L = 2*I`  | `irange1`     |
| `A(I,J)=0` | `irange2`     |

📌 This explicitly models **loop-induced control dependence**.

---

# Substituting Constants (Making Dependence Visible)

```fortran
Do I = 1, 100
  L = 2 * I                (1, 100)
  Do J = 1, L              (1, 100)
    A(I, J) = 0            (1, L) (1, 100)
  End Do
End Do
```

Now it becomes crystal clear:

* `A(I, J)` executes only when:

  * `I ∈ [1,100]`
  * `J ∈ [1, 2I]`

This is **not uniform** across `I`.

---

# Correct Vectorization (Preserving Semantics)

```fortran
Do I = 1, 100
  L = 2 * I
  A(I, 1:L) = 0
End Do
```

### Why this is correct

* Vectorization happens **inside each `I`**
* Inner loop is replaced by slice assignment
* Bound `L` remains **dependent on `I`**

✔ Same execution region
✔ Same number of executions
✔ Same semantics

---

# Deep Insight (This is the REAL lesson)

> **Vectorization must preserve iteration control dependence, not just data dependence.**

Ignoring loop control:

* changes execution count
* changes memory region
* breaks correctness

---

# Exam-Ready Summary (Very Important)

### Key points to write:

* Iterative constructs introduce control dependence.
* Loop bounds determine how many times a statement executes.
* Incorrect vectorization ignores iteration control dependence.
* Iteration ranges (`irange`) model this dependence explicitly.
* Correct vectorization preserves loop-dependent bounds.

---

# One Killer Exam Line (Memorize This)

> A `DO` statement controls the execution count of statements within it, and this control dependence must be preserved during vectorization.

---

