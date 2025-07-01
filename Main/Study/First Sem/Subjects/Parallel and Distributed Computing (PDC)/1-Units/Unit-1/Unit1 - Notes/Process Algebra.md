
## Definition of Process Algebra
Process Algebra is a **mathematical framework** for modeling and reasoning about the behavior of processes — especially in concurrent or communicating systems.

It focuses mainly on process behavior and interactions, not data storage or structure.

It's about how processes act, what actions they perform, and how they compose (e.g., sequentially, in parallel, with choice).

---

## 📘 System Behavior: Processes and Data

### 1. **System Behavior = Processes + Data**

* The behavior of any system is defined by:

  * **Processes**: the active parts (do the work)
  * **Data**: the passive parts (used and changed by processes)

---

### 2. **Role of Processes**

* **Processes** are **control mechanisms** that operate on data.
* They perform tasks like:

  * reading,
  * modifying,
  * storing,
  * or transmitting data.
* **Dynamic and active**: They run, change state, make decisions.

---

### 3. **Role of Data**

* **Data** is **static and passive**.
* It does **not act on its own**, but it is essential for process behavior.
* It can **influence the control flow** of a process based on its values.

---

### 4. **Concurrency in Systems**

* Real-world systems often have **multiple processes** running **concurrently**.
* These processes:

  * Run in parallel (e.g., threads, agents)
  * **Exchange data** with each other (through shared memory, messages, etc.)
  * The **data exchange influences how each process behaves**.

---
