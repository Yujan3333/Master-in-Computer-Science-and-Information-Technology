
## ❌ Deficiencies of PRAM Algorithms

The PRAM model is idealized and **too abstract** to capture the realities of real-world parallel computation. Here’s why:

---

### 1. **No Mechanism to Represent Communication Between Processors**

* **PRAM assumes** that all processors share a common memory and can access any memory cell in **unit time** — regardless of how far apart the processors are.
* In reality, **processors need to communicate** via message-passing or shared-memory buses.
* The **cost and delay of communication** (network latency, bus contention, bandwidth limits) are **not modeled at all**.

> 📌 **Result**: PRAM algorithms **ignore** how processors interact — this makes them **unrealistic for distributed systems** or hardware-level implementations.

---

### 2. **Storage Management and Communication Are Hidden**

* PRAM assumes **unlimited shared memory** that all processors can access freely.
* There’s **no concern about memory allocation**, **conflicts**, or **local vs remote access**.
* It hides all hardware-level complexities such as:

  * **Memory hierarchies** (cache, main memory, etc.)
  * **Access contention** (multiple processors trying to access the same memory at once)
  * **Data locality** and **synchronization**

> 📌 **Result**: Algorithm designers may create theoretically efficient algorithms that **perform poorly in practice** due to memory bottlenecks and communication delays.

---

## 🧠 Summary Table

| Deficiency                           | Explanation                                                                                                |
| ------------------------------------ | ---------------------------------------------------------------------------------------------------------- |
| ❌ No communication model             | PRAM assumes cost-free, instant access to shared memory — doesn’t model how data is passed or synchronized |
| ❌ Hidden storage/communication costs | PRAM abstracts away memory conflicts, allocation, or access delays, making it less practical               |

---

## ⚠️ Why It Matters:

While PRAM is great for **theoretical analysis** and designing **work-efficient algorithms**, it’s not suitable for:

* Modeling performance on **real hardware**
* Dealing with **distributed** or **multi-core** systems with limited memory bandwidth

---

