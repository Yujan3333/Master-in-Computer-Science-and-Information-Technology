
## 🚦 **Mutual Exclusion in Distributed Systems**

### 🔧 **The Problem:**

In a distributed system, **multiple processors or processes** may need to **access a shared resource**, but only **one at a time** is allowed.

This leads to the **critical section problem**:

> How can we ensure that **only one process** enters the **critical region** at a time?

---

### 🧩 **Program Partitioning into 4 Regions:**

Each process's program is divided into the following parts:

| Region           | Description                                                                                                                           |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| **1. Trying**    | The process attempts to **acquire the lock** or permission to use the resource.                                                       |
| **2. Critical**  | The **actual resource** (like a shared file or variable) is being **accessed/modified**. Only **one** process allowed here at a time. |
| **3. Exit**      | **Cleanup** or **release of the lock** happens here, allowing others to enter the critical section.                                   |
| **4. Remainder** | The rest of the program — no shared resource is used here.                                                                            |

---

### 🔁 **Example:**

```c
while (true) {
    Trying:     request_access();     // trying to enter critical section
    Critical:   shared_data += 1;     // accessing shared resource
    Exit:       release_access();     // exit and cleanup
    Remainder:  do_something_else();  // rest of the program
}
```

---

### 🚫 **The Main Requirements of Mutual Exclusion:**

1. **Mutual Exclusion** – Only one process in critical section at a time
2. **Progress** – If no one is in the critical section, one of the waiting processes should enter
3. **Bounded Waiting** – A process should not wait forever to enter

---
