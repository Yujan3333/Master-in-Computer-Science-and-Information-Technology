## 1️⃣ Original loop (understand execution first)

```fortran
DO 100 I = 1, N
S1: IF (A(I-1) > 0.0) GOTO 100
S2: A(I) = A(I) + B(I) * C
100: CONTINUE
```

### What happens in ONE iteration?

For each `I`:

* First **S1 is checked**
* If `A(I-1) > 0`
  → jump to label `100`
  → **S2 is SKIPPED**
* Else (`A(I-1) <= 0`)
  → **S2 is executed**

So:

👉 **S2 executes conditionally**, not always.

---

## 2️⃣ Why S2 has NO data dependence (but still a problem)

Look at `S2`:

```fortran
A(I) = A(I) + B(I) * C
```

* Reads: `A(I)`, `B(I)`
* Writes: `A(I)`
* Different iterations access **different indices** `I`

✅ No loop-carried data dependence
❌ But **this is not enough** for parallelism

---

## 3️⃣ What is CONTROL DEPENDENCE? (key idea)

### Definition (exam-friendly)

> A statement **S2** is *control dependent* on **S1** if the execution of **S2** depends on the outcome of a branch in **S1**.

Here:

* `S2` executes **only if** `A(I-1) <= 0`
* That condition comes from `S1`

👉 **S2 is control-dependent on S1**

---

## 4️⃣ Why naive vectorization is WRONG

You tried:

```fortran
S2: A(1:N) = A(1:N) + B(1:N) * C
DO 100 I = 1, N
S1: IF (A(I-1) > 0.0) GOTO 100
100: CONTINUE
```

### What does this do?

* Executes **S2 for ALL elements**
* Completely ignores the condition `A(I-1) > 0`

### Why incorrect?

Original code:

* `A(I)` is updated **only when** `A(I-1) <= 0`

Vectorized code:

* `A(I)` is updated **unconditionally**

🚫 **Program semantics changed**

📌 **Key exam line**:

> Even though there is no data dependence, control dependence prevents safe vectorization.

---

## 5️⃣ IF Conversion – the core idea

### Goal:

👉 **Remove control dependence**
👉 **Convert it into data dependence**

### How?

Instead of *skipping statements*, we **guard them with conditions**.

---

## 6️⃣ IF Conversion (Example 1)

### Original

```fortran
DO 100 I = 1, N
IF (A(I-1) > 0.0) GOTO 100
A(I) = A(I) + B(I) * C
100: CONTINUE
```

### After IF-conversion

```fortran
DO I = 1, N
IF (A(I-1) <= 0.0)
A(I) = A(I) + B(I) * C
END DO
```

✔ Same behavior
✔ No jumps
✔ Clear condition guarding the update

---

## 7️⃣ Why this can be vectorized now

Because the condition is **data-based**, not control-based.

```fortran
WHERE (A(0:N-1) <= 0.0)
A(1:N) = A(1:N) + B(1:N) * C
```

### Meaning of `WHERE`

* For **each element independently**
* If condition true → execute assignment
* If false → skip that element

✅ Perfect match with original semantics
✅ Safe vectorization

---

## 8️⃣ Example 2 – more subtle case

### Original code

```fortran
DO 100 I = 1, N
IF (A(I-1) > 0.0) GOTO 100
A(I) = A(I) + B(I) * C
B(I) = B(I) + A(I)
100: CONTINUE
```

### Important observation

* `B(I)` update uses **new value of `A(I)`**
* Both statements execute **together or not at all**

---

## 9️⃣ IF Conversion (Example 2)

```fortran
DO I = 1, N
IF (A(I-1) <= 0.0) A(I) = A(I) + B(I) * C
IF (A(I-1) <= 0.0) B(I) = B(I) + A(I)
END DO
```

Now:

* Both statements depend on **same condition**
* Control dependence → **data dependence**

---

## 🔟 Why we CANNOT vectorize both together

If we did:

```fortran
WHERE (A(0:N-1) <= 0.0)
B(1:N) = B(1:N) + A(1:N)
```

⚠ Problem:

* `A(I)` must already be updated
* But vector execution may read old `A(I)`

👉 **Order matters**

---

## 1️⃣1️⃣ Correct vectorization strategy

### Step 1: Compute `A` first (scalar or vector-safe)

```fortran
DO I = 1, N
IF (A(I-1) <= 0.0) A(I) = A(I) + B(I) * C
END DO
```

### Step 2: Vectorize `B` update

```fortran
WHERE (A(0:N-1) <= 0.0)
B(1:N) = B(1:N) + A(1:N)
```

✔ Preserves order
✔ Preserves semantics
✔ Safe vectorization

---

## 1️⃣2️⃣ Final exam-ready summary ✍️

### Why naive vectorization fails

* Ignores **control dependence**
* Executes statements that should be conditionally skipped

### What IF conversion does

* Replaces control dependence with data dependence
* Uses conditional execution instead of branches

### Why vectorization becomes legal

* Each iteration becomes independent
* Conditions apply per element (`WHERE`)

---

## 1️⃣3️⃣ One-line exam answer you can memorize

> Although statement S2 has no data dependence, it is control-dependent on S1. Naive vectorization violates program semantics. IF conversion eliminates control dependence by transforming branches into conditional assignments, enabling safe vectorization.

---
