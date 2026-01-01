**Loop normalization** is a compiler optimization technique in which loops are converted into a **standard form** so that they are **easy to analyze for dependencies and optimization**.

The standard (normalized) form is:

* Loop starts from **1**
* Loop ends at some **upper bound**
* Loop increments by **1**

---

### Why Loop Normalization is Needed

Compilers perform **dependence testing** to check whether loop iterations can run in parallel.

If loops have:

* different start values
* different step sizes
* irregular bounds

then dependence analysis becomes **complex**.

So the compiler **normalizes loops** to make:

* dependence testing simpler
* optimization safer and faster

---

### Normalized Loop Form

✅ **Normalized loop**

```c
for (i = 1; i < N; i++)
```

Conditions:

* Lower bound = 1
* Step size = 1

---

❌ **Non-normalized loop**

```c
for (i = 3; i < N; i = i + 2)
```

Problems:

* Lower bound ≠ 1
* Step size ≠ 1

---

### What the Compiler Does (Key Idea)

The compiler:

1. Introduces a **new induction variable**
2. Rewrites the old induction variable as a **linear function** of the new one

Example idea:

* Original variable: `i`
* New variable: `k`
* Relationship:
  $i = 3 + 2k$

Now the loop can be written in normalized form using `k`.

---

### Definition (Exam-Ready)

> Loop normalization is a transformation in which loops are converted to a standard form with lower bound 1 and step size 1 by replacing the original induction variable with a linear function of a new induction variable.

---

### Benefits (Write Any 2–3 in Exam)

* Simplifies **dependence testing**
* Helps **parallelization**
* Makes **compiler analysis uniform**
* Supports further optimizations like **loop interchange** and **strength reduction**

---

### One-Line Exam Answer

> Loop normalization converts loops with arbitrary bounds and steps into a standard form to simplify dependence analysis in compiler optimization.

---
