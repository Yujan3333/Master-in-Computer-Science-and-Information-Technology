
![](../../../../../../../../Images/First_Sem_Images/Techniques%20for%20checkpointing.png)

## ✅ Fault Recovery Using Checkpoints and Rollbacks

### How it works:

* Each process **periodically saves its state** — called a **checkpoint**.
* If a fault is detected in a process, it **rolls back** (reverts) to the **last checkpoint**.

---

## ✅ The Domino Effect:

* When a process rolls back, **any other process that communicated with it after that checkpoint must also roll back** to maintain consistency.
* This **rollback can cascade**, causing many processes to roll back — like a line of dominoes falling.
* This cascading rollback is called the **Domino Effect**.

---

## ✅ Why Domino Effect Happens:

* Because messages sent **after a checkpoint** might have depended on faulty or inconsistent data.
* To avoid inconsistency, processes that received such messages must **undo their work**.

---

## ✅ Summary:

| Concept           | Explanation                                                      |
| ----------------- | ---------------------------------------------------------------- |
| **Checkpoint**    | Saved process state at a certain time                            |
| **Rollback**      | Revert to last checkpoint when fault detected                    |
| **Domino Effect** | Cascading rollback of multiple processes to maintain consistency |

---

## ✅ Importance:

* Prevents inconsistent system states after faults.
* But it **may cause significant performance overhead** due to many rollbacks.

---
