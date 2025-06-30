
## ✅ **Task Duplication (Shadowing)**

> It's a **fault-tolerant scheduling** technique — used in **reliable parallel/distributed systems** to detect and recover from faults.

---

### 🔧 **Core Idea:**

* **Duplicate the same task** on **two or more processors**
* Let them execute **in parallel**
* At **checkpointing points**, **compare their internal states or outputs**
* If they match → assume everything is okay
* If they don't match → a fault occurred in one processor

---

## 🔁 Analogy to Database Shadowing

Like **shadowing in databases**:

* You keep **two versions** of the data (primary + shadow)
* In case one is corrupted, you use the **backup version**
* Similarly, task duplication keeps multiple **task executions** for comparison

---

### 📍 Where This Is Used:

* Real-time systems
* Aerospace / military-grade fault-tolerant systems
* Safety-critical parallel programs

---

## ✅ Benefits:

* Detects **silent errors**
* Allows **fault isolation**
* Supports **checkpoint-based recovery**

## ⚠️ Trade-offs:

* Consumes **more processors**
* Adds **overhead** in comparison and duplication

---

### ✅ Final Summary:

> **Task Duplication** helps catch hardware/software faults by executing the same task on multiple processors and comparing results at checkpoints — similar to **shadow copies in databases** used for recovery.
