
## 🔄 **Ring-Based Election Algorithm**

### 📌 **Purpose:**

To elect a new **coordinator (leader)** in a distributed system **organized as a ring**, when the current coordinator fails.

---

### ⚙️ **System Assumptions:**

* Processes are arranged **logically in a ring**
* **Unidirectional links**: Each process can **only send to its right neighbor**
* Each process has a **unique identifier (priority number)**
* Uses an **active list** to store participating process IDs

---

### 🔁 **Algorithm Steps:**

1. **Failure Detection:**

   * If a process (e.g., $P_1$) detects that the current **coordinator has failed**, it:

     * Creates a new **empty active list**
     * Adds **its own ID** to the list
     * Sends an **election message** to its right neighbor

2. **Message Propagation:**

   * Each receiving process:

     * Adds **its own ID** to the active list
     * Forwards the message to its **right neighbor**

3. **Leader Election:**

   * When the message returns to the **originator**, it:

     * Scans the active list for the **highest-numbered process**
     * Declares it as the **new coordinator**
     * Broadcasts the coordinator info to all processes

---

### 📘 **Example:**

If processes have IDs: `[1, 3, 5, 2]` arranged in ring

* $P_1$ initiates:

  * Active list: `[1] → [1,3] → [1,3,5] → [1,3,5,2]`
* When list returns to $P_1$:

  * Max ID = 5 → new coordinator is $P_5$

---

### 🧠 **Key Points:**

| Feature               | Description                                    |
| --------------------- | ---------------------------------------------- |
| **Type**              | Ring-based distributed election                |
| **Message direction** | Unidirectional (clockwise or right)            |
| **Message content**   | Active list with all participating process IDs |
| **Election winner**   | Process with the **highest ID**                |
| **Message overhead**  | O(n) messages (1 full ring traversal)          |

---

### ✅ **Summary Statement:**

> The Ring Election Algorithm elects a new coordinator by circulating an election message around a unidirectional ring of processes. Each process adds its ID to the message. The originator, upon receiving its own message, selects the process with the highest ID as the new leader and informs all nodes.

---
