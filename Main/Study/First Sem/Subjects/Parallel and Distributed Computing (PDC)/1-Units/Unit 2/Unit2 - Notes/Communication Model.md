
## 🧠 **Two Main Contributors to Completion Cost**

1. **Execution Time**
   → Total time taken to execute all tasks = **Schedule Length**

2. **Communication Delay**
   → Time spent sending data between processors for dependent tasks

---

## 📘 **Model A – Edge-Based Communication Count**

### 🔷 Formula:

$$
\text{Total Cost} = \text{Execution Cost} + \text{Communication Cost}
$$

Where:

* Execution Cost = **Schedule Length**
* Communication Cost =

  $$
  \text{Number of messages} \times \text{Cost per message}
  $$
* Number of messages =

  $$
  \left| \{(u, v) \in A \mid \text{proc}(u) \ne \text{proc}(v) \} \right|
  $$

✅ In this model, **each edge (u, v)** across processors is counted as **one separate communication**.

> ⚠️ If one task sends the same data to two tasks on **different processors**, it's counted **twice**.

---

## 📘 **Model B – Destination-Based Counting**

This model avoids **counting the same data transfer multiple times** if multiple dependent tasks are on the **same processor**.

* **If task $u$** sends output to **$v$** and **$w$**

  * And both are on the **same processor**, count as **1 message**
  * If on **different processors**, still **1 message per destination processor**

✅ So, if **both $v$ and $w$** are on **P2**, and $u$ is on P1 → counted as **1 message**

🧠 **Communication is counted only once per destination processor.**

---

## 📘 **Model C – Overlapped Communication and Computation**

This model **assumes there is an I/O processor** associated with each main processor.

> ✅ So, a processor can **communicate and compute at the same time**

### Key Idea:

* **Communication delay does not block** the processor from **executing other tasks**
* More **realistic** in systems where:

  * DMA (Direct Memory Access) handles I/O
  * Multithreading allows overlap of communication and execution

This leads to **lower effective communication cost** than Models A or B.

---

## ✅ Summary Table

| Model | How It Counts Communication                    | Overlap Allowed? | Best Suited For                              |
| ----- | ---------------------------------------------- | ---------------- | -------------------------------------------- |
| A     | One message **per edge** across processors     | ❌ No             | Simple modeling                              |
| B     | One message **per destination processor**      | ❌ No             | Avoids double counting                       |
| C     | Communication can **overlap with computation** | ✅ Yes            | Realistic parallel systems with I/O hardware |

---
