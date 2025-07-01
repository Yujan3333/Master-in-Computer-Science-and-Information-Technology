## ✳️ 2. **Tolerating Processor Failure in Asynchronous Systems**

### 🔹 Definition:

Handling **failures of processors** in an **asynchronous system** where:

* No bounds on **message delay**
* No guarantees on **process speed**

### ✅ Key Points:

* In asynchronous systems, **failure detection is hard** because silence may mean delay or crash.
* **Crash faults** are typically tolerated, but **Byzantine faults** are harder.
* Algorithms must not rely on timing assumptions (e.g., heartbeat timeout fails here).
* **Consensus is impossible** in fully asynchronous systems with even **one crash** (proved by **FLP impossibility** result).
* Solutions involve:

  * Using **failure detectors** (with some assumptions)
  * Designing **wait-free algorithms**
  * Relying on **majority-based voting** or **quorums**
* Examples:

  * Paxos algorithm (handles crash faults)
  * Randomized consensus protocols

### 📌 Note:

Must carefully **design protocols** that do not wait forever on failed processes.

---
