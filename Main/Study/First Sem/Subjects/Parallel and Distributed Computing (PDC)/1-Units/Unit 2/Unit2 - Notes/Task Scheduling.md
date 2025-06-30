
## 🧠 **Task Scheduling in Parallel Computing**

Once a program is **partitioned into tasks**, the next goal is to **schedule** those tasks on available processors so that:

* **Total execution time is minimized**
* **Processor utilization is maximized**
* **Dependencies are respected**

---

## 🧩 **Types of Scheduling**

### 1️⃣ **Deterministic Scheduling**

> 📌 **All information is known in advance**

#### ✅ Characteristics:

* Task execution times, dependencies, and structure are **completely known** before the program runs.
* Suitable for **static scheduling** and predictable programs (e.g., matrix multiplication).
* Often used in **real-time systems** and embedded devices.

#### 🧪 Example:

* In a fixed loop with 10 independent iterations, tasks can be pre-assigned to processors.

---

### 2️⃣ **Non-Deterministic Scheduling**

> 📌 **Some information is only known during execution**

#### ✅ Characteristics:

* Some tasks depend on **runtime conditions**, such as:

  * Conditional branches (`if/else`)
  * Loops with unknown bounds
  * Dynamic task creation
* Requires **dynamic scheduling** during runtime.
* Often used in general-purpose and interactive systems.

#### 🧪 Example:

* A function with `if (x > 0)` may or may not execute certain code, so the **task graph is unknown before execution**.

---

## 📊 Comparison Table

| Feature                 | Deterministic        | Non-Deterministic        |
| ----------------------- | -------------------- | ------------------------ |
| Info available at start | ✅ Yes                | ❌ No (partially unknown) |
| Task graph              | Fixed                | Dynamic / partial        |
| Scheduler type          | Static               | Dynamic                  |
| Runtime overhead        | Low                  | High                     |
| Use cases               | Scientific computing | General-purpose apps, AI |

---

## ✅ Summary

* **Scheduling** is the assignment of tasks to processors to **minimize execution time**
* Can be **deterministic** (known ahead of time) or **non-deterministic** (depends on runtime)
* Efficient scheduling = faster execution and better parallel performance

---
