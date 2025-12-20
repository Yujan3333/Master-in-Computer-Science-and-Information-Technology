

#### 1. Replace References to auxiliary induction variable with function of loop index
```md
INC = 2
KI = 0
DO I = 1, 100
   DO J = 1, 100
      KI = KI + INC
      U(KI + J * INC) = U(KI + J * INC) + W(J)
   END DO
   KI = KI + 100 * INC
   S(I) = U(KI)
END DO
```

---
####  2. Remove all references to `KI`
```md
INC = 2
KI = 0
DO I = 1, 100
   DO J = 1, 100
      U(KI + (I-1) * 100 * INC + J * INC) = U(KI + (I-1) * 100 * INC + J * INC) + W(J)
   END DO
   S(I) = U(KI + I * (100 * INC))
END DO
KI = KI + 100 * 100 * INC
```

---
#### 3. Substitute Constants
```md
Step 3: Substitute the constants:
INC = 2
KI = 0
DO I = 1, 100
   DO J = 1, 100
      U(I * 200 + J * 2 - 200) = U(I * 200 + J * 2 - 200) + W(J)
   END DO
   S(I) = U(I * 200)
END DO
KI = 20000
```
---

#### 4. Remove all unused code AKA constants
```md
Do I = 1, 100
   Do J = 1, 100
      U(I * 200 + J * 2 - 200) = U(I * 200 + J * 2 - 200) + W(J)
   END DO
   S(I) = U(I * 200)
END DO
```

---
## Explanation
### Given Code (Original)

The original program uses an **auxiliary induction variable `KI`** whose value changes regularly inside nested loops.

* `I` → **basic induction variable**
* `KI` → **auxiliary induction variable**
* `INC = 2` → constant increment

---

### What is the problem?

* `KI` is updated repeatedly using **addition**
* Its value **depends entirely on loop indices `I` and `J`**
* Maintaining `KI` causes:

  * Extra instructions
  * Artificial loop-carried dependences
  * Poor parallelization opportunities

---

### Goal of Optimization

✔ Express `KI` **directly as a function of loop indices**
✔ Remove unnecessary updates to `KI`
✔ Make array subscripts **affine expressions** of loop indices
✔ Improve **loop optimization and parallelization**

---

### Step 1: Replace auxiliary induction variable with function of loop indices

#### Observation

Inside the inner loop:

* `KI` increases by `INC = 2` **every iteration of `J`**
* Over `100` iterations of `J`:

$$
KI_{inner} = J \times INC
$$

Across outer loop `I`:

* After each `I`, `KI` increases by `100 × INC`

$$
KI_{outer} = (I - 1) \times 100 \times INC
$$

---

#### Result

Total value of `KI` at any point:

$$
KI = (I - 1) \times 100 \times INC + J \times INC
$$

➡ All uses of `KI` are replaced by this expression

---

### Step 2: Remove all references to `KI`

* Since `KI` can be computed from `I` and `J`
* All assignments like:

  * `KI = KI + INC`
  * `KI = KI + 100 * INC`
    are **eliminated**

✔ `KI` is no longer needed inside the loop

---

### Step 3: Substitute constants

Given:

* `INC = 2`
* `100 × 2 = 200`

Substitute into expressions:

$$
(I - 1) \times 200 + J \times 2
$$

Which simplifies to:

$$
I \times 200 + J \times 2 - 200
$$

---

### Step 4: Remove unused code

* `KI` is no longer used
* Its final value (`20000`) has no effect
* All `KI`-related statements are removed

---

### Final Optimized Code

```
Do I = 1, 100
   Do J = 1, 100
      U(I * 200 + J * 2 - 200) =
         U(I * 200 + J * 2 - 200) + W(J)
   End Do
   S(I) = U(I * 200)
End Do
```

---

### What optimization is applied?

#### ✔ Induction Variable Elimination

#### ✔ Strength Reduction

#### ✔ Loop Normalization

---

### Why is this optimization important?

* Removes unnecessary loop-carried dependences
* Simplifies array indexing
* Improves:

  * Vectorization
  * Parallelization
  * Instruction scheduling
* Reduces runtime overhead

---

### One-line exam answer

> The auxiliary induction variable `KI` is replaced by an affine function of loop indices `I` and `J`. This **induction variable elimination** removes redundant updates, simplifies array subscripts, and improves loop optimization and parallelization.

---
