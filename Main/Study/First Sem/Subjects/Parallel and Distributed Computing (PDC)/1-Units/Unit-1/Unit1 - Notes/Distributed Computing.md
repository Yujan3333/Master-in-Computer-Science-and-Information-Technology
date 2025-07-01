
## ⚙️ **Distributed Computing Model and Challenges**

### 🚧 **Major Obstacles in Distributed Computing:**

1. **Uncertainty**

   * Due to **asynchronous execution** (processors may run at different speeds).
   * **Message delays**, **losses**, or **reordering**.
2. **Failures**

   * Processor crashes or restarts.
   * Network or message loss.
   * Unreliable communication channels.

---

### 🖥️ **System Model:**

* The system has:

  $$
  \text{n processors: } P_1, P_2, \dots, P_n
  $$
* A **communication network**: `net`

---

### 🧠 **Processor Model:**

Each processor $P_i$ is:

* Modeled as a **state machine**:

  $$
  P_i = (Q_i, q_{0,i})
  $$

  * $Q_i$: Set of possible states
  * $q_{0,i}$: Initial state of processor $P_i$

* Equipped with:

  * A **buffer** $\text{buff}_i$ for **incoming messages**

    * Helps **store and queue messages** from the network
    * Required due to **asynchronous message arrival**

---

### 📡 **Communication Model:**

* Processors communicate by **sending/receiving messages** over `net`
* Messages can be:

  * **Delayed**
  * **Lost**
  * **Received out of order**
  * **Duplicated**

---

### 🧩 Summary:

| Component | Description                                     |
| --------- | ----------------------------------------------- |
| `P_i`     | Processor modeled as a state machine            |
| `Q_i`     | Set of all states for processor $P_i$           |
| `q_{0,i}` | Initial state of processor $P_i$                |
| `buff_i`  | Buffer for incoming messages to $P_i$           |
| `net`     | Underlying network for inter-processor messages |

---

