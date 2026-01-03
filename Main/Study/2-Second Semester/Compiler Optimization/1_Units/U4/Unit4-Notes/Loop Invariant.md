# 🔁 What is a **Loop Invariant**?

### **Simple definition (core idea)**

> A **loop invariant** is a condition (or fact) that is **true before the loop starts**, **remains true after every iteration**, and is **still true when the loop ends**.

Think of it as **something that never changes**, no matter how many times the loop runs.

---

## 🧠 Why Loop Invariants Matter

Loop invariants are used to:

* **Prove correctness of loops** (very important in theory exams)
* **Optimize code** (compiler optimization)
* **Understand what a loop is really doing**

---

# 🪜 Three Key Properties (MUST remember)

A loop invariant must satisfy **all three**:

1. **Initialization** – true before first iteration
2. **Maintenance** – remains true after each iteration
3. **Termination** – helps prove loop correctness when loop ends

---

# 🔍 Very Simple Example

### Code

```c
int i = 0;
int sum = 0;

while (i < n) {
    sum = sum + i;
    i = i + 1;
}
```

---

## 🔹 What could be the loop invariant?

> **At the start of each iteration, `sum` equals the sum of numbers from `0` to `i-1`.**

---

### ✅ Check the 3 properties

#### 1️⃣ Initialization

Before loop starts:

* `i = 0`
* `sum = 0`
* Sum of numbers from `0` to `-1` is `0`

✔ invariant is true

---

#### 2️⃣ Maintenance

Assume invariant is true at start of iteration:

* sum = 0 + 1 + 2 + ... + (i − 1)

Loop body:

```c
sum = sum + i;
i = i + 1;
```

Now:

* sum = 0 + 1 + 2 + ... + i
* i increased

Invariant still holds ✔

---

#### 3️⃣ Termination

Loop ends when `i = n`

Invariant tells us:

* sum = 0 + 1 + 2 + ... + (n − 1)

This proves loop is correct ✔

---

# 📌 Another Easy Example (Searching)

```c
for (i = 0; i < n; i++) {
    if (a[i] == key)
        found = true;
}
```

### Loop Invariant

> At the start of each iteration, `found` is true **if and only if** `key` exists in `a[0 ... i-1]`.

---

# 🧱 Loop Invariant in Optimization (Compiler Side)

Sometimes a computation inside a loop **never changes**.

### Example

```c
for (i = 0; i < n; i++) {
    y = a * b;
    x[i] = y + i;
}
```

Here:

* `a * b` does not change

So compiler moves it **outside the loop**:

```c
y = a * b;
for (i = 0; i < n; i++) {
    x[i] = y + i;
}
```

This is called **Loop Invariant Code Motion**.

---

# 📝 One-Line Exam Definition

> A loop invariant is a condition that remains true before and after every iteration of a loop and is used to prove the correctness of the loop.

---

# 🧠 Memory Trick

> **Invariant = “in-variable” → does NOT change**

---

# ✨ Final Intuition (Very Important)

* Loop runs → invariant holds
* Loop runs again → invariant still holds
* Loop ends → invariant helps prove result is correct

---
