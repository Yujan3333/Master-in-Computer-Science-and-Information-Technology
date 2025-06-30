
## 🧠 1. **Control Flow Model**

This is the **traditional model** used in most programming languages and von Neumann machines (like your CPU today).

### 🔧 How It Works:

* The program is a **sequence of instructions**
* The **order of execution** is determined by the **program counter (PC)** or **explicit control statements**
* One instruction is executed **at a time**, even if multiple are ready

### 🧪 Example:

```c
if (n == 0)
    c = a + b;
else
    c = a - b;
```

Here:

* The program checks the **condition** first (`n == 0`)
* Then, based on result, it executes **either** `a + b` or `a - b`
* Only **one path is taken**, and only **one operation is done** at that time

> ✅ Sequential, step-by-step execution
> ❌ Not inherently parallel — must wait for control to reach each instruction

---

## 🔁 2. **Data Flow Model**

This is a **parallel computation model** where operations execute **as soon as their input data is ready** — **no fixed instruction order**.

### 🔧 How It Works:

* Each operation is like a **node** in a graph
* An operation **fires (executes)** as soon as **all its input operands** are available
* There’s **no program counter** — only **data availability** drives execution

### 🧪 Same Example in Data Flow:

```plaintext
Node A: compute n == 0
Node B: compute a + b
Node C: compute a - b
Node D: choose result from B or C based on A
```

In this model:

* `a + b` and `a - b` can **both be computed in parallel**, even before we know which one is needed
* Once `n == 0` is known, we **select the correct result**
* Execution is **driven by data readiness**, not program counter

> ✅ Highly parallel
> ✅ Suitable for distributed and parallel systems
> ❌ Requires different hardware or runtime model than traditional CPUs

---

## 📊 Comparison Table

| Feature               | Control Flow                 | Data Flow                           |
| --------------------- | ---------------------------- | ----------------------------------- |
| Execution Order       | Follows instruction order    | Based on data readiness             |
| Trigger for Execution | Program Counter              | Availability of input data          |
| Parallelism           | Limited (explicit threading) | Implicit and natural                |
| Example Languages     | C, Java, Python              | SISAL, Lucid, LabView, TensorFlow\* |
| Hardware Model        | von Neumann                  | Dataflow Machines (experimental)    |

---

## 📌 Summary

* **Control Flow**: Execute **instructions in order**, driven by **control logic**
* **Data Flow**: Execute **operations as soon as their inputs are ready**, driven by **data availability**
* Data Flow offers **natural parallelism** and is used in **stream processing**, **AI frameworks**, and **hardware description languages**

---
