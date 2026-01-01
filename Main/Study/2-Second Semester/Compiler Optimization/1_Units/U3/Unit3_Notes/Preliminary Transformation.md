### Meaning (Exam Definition):
Preliminary transformations are **source-level program transformations** applied **before dependence analysis and advanced optimizations** to make loops **simpler, analyzable, and suitable for optimization**.

Their main goal is to **expose induction variables and linear subscript expressions** so the compiler can detect dependencies and apply optimizations like **strength reduction, loop parallelization, and vectorization**.

---

## Induction Variables (Key Concept)

### Definition (Very Important for Exam)

An **induction variable** is a variable whose value changes by a **constant amount** on every iteration of a loop.

### Types:

1. **Basic Induction Variable (BIV)**
   Example: `I`, `J` (loop counters)

2. **[Auxiliary Induction Variable (AIV)](Auxiliary%20Induction%20Variable%20(AIV).md)**
   Example: `KI`

---

## Understanding Your Code (Line-by-Line Logic)

```fortran
INC = 2        ← loop invariant
KI = 0         ← auxiliary induction variable

DO I = 1, 100
   DO J = 1, 100
      KI = KI + INC
      U(KI) = U(KI) + W(J)
   END DO
   S(I) = U(KI)
END DO
```

---

## Why is **KI** an Auxiliary Induction Variable?

Because:

* `KI` is **not a loop counter**
* It is updated as:

$$
KI = KI + INC
$$

* `INC` is constant → `KI` increases by **2 every iteration**
* So values of `KI` are:

$$
2, 4, 6, 8, \dots
$$

✅ Hence, **KI is an auxiliary induction variable**

---

## Why This Code is Hard to Analyze Directly

### From your notes:

> “The expression cannot be tested in the form written because KI varies within the loop”

### Meaning:

* Array subscript `U(KI)` depends on `KI`
* `KI` changes **inside the inner loop**
* Compiler **cannot directly determine**:

  * which memory locations are accessed
  * whether there is data dependence

This **blocks parallelization and optimization**.

---

## Role of Preliminary Transformation Here

The compiler performs a **preliminary transformation** to:

1. **Express KI as a function of loop variables**
2. Convert subscripts into **linear functions of I and J**

---

## Mathematical Interpretation (Exam-Friendly)

Inside inner loop:

$$
KI = KI_0 + INC \times J
$$

Since `KI_0 = 0` and `INC = 2`:

$$
KI = 2J
$$

So the statement:

```fortran
U(KI) = U(KI) + W(J)
```

becomes:

```fortran
U(2J) = U(2J) + W(J)
```

✅ Now the subscript is a **linear function of J**

---

## Why Notes Say “Only two subscripts are linear”

Because after transformation:

* `J` is basic induction variable
* `KI = 2J` → linear function
* This allows:

  * dependence testing
  * strength reduction
  * loop optimization

---

## INC is Loop Invariant (Important Point)

* `INC = 2` does **not change inside the loop**
* So compiler can safely treat it as a constant
* Enables algebraic simplification

---

## Strength Reduction (One-Line Exam Link)

Instead of repeatedly doing:

```fortran
KI = KI + 2
```

Compiler replaces it with:

```fortran
U(2J)
```

which avoids unnecessary updates and improves performance.

---

## Final Exam-Ready Summary (Write This)

> Preliminary transformations simplify loop structures by identifying induction variables and rewriting array subscripts as linear functions of loop indices. In the given code, `KI` is an auxiliary induction variable incremented by a loop-invariant constant `INC`. By expressing `KI` as `2J`, the compiler converts non-analyzable subscripts into linear forms, enabling dependence analysis and further optimizations such as strength reduction and parallelization.

---
