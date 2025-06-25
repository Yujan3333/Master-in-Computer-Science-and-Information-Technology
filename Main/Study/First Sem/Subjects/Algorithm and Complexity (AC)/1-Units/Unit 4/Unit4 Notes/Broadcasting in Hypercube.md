

## 📢 **Broadcasting in Hypercube (Hd)**

---

### 🔹 What is Broadcasting?

> **Broadcasting** means **sending a message** from **one processor (source)** to **all other processors** in the network.

It is used in many parallel algorithms to share data quickly among all processors.

---

### 🔹 How it Works in a Hypercube?

A **d-dimensional hypercube** has:

* $2^d$ processors
* Each processor has $d$ neighbors
* The structure is similar to a **binary tree**, which is helpful for broadcasting

---

## ✅ Broadcasting Algorithm (Using Binary Tree Embedding)

Let’s assume:

* You have a message **M**
* The source processor is at node `0` (root)

---

### 📘 Step-by-Step Process:

1. **Root sends message to 1 neighbor (1-bit difference):**

   * For example, in **3D Hypercube**, processor `000` sends to `001`

2. In each **step**, every processor that just received the message will:

   * Make **2 copies**
   * Send it to **two more processors** (its children in the binary tree)

3. The process **continues recursively**:

   * Until **all processors** have received a copy

![](../../../../../../../../Attachments/Broadcasting%20in%20Hypercube.png)

---

### 🧠 Why is this efficient?

* Because in each step, the number of processors **with the message doubles**
* So in **d steps**, all $2^d$ processors will receive the message

---

### 🔢 Example: 3D Hypercube (8 processors)

| Step | Processors Receiving Message |
| ---- | ---------------------------- |
| 0    | `000` (root)                 |
| 1    | `001`, `010`                 |
| 2    | `011`, `100`                 |
| 3    | `101`, `110`, `111`          |

✅ All 8 processors have the message in just **3 steps** (equal to dimension $d$)!

---

## 📝 Summary for Exams:

> In a **d-dimensional hypercube**, broadcasting a message from a root processor is efficiently done using a **binary tree embedding**.
> The message is copied and sent to child processors level by level.
> In **each step**, the number of informed processors **doubles**.
> Thus, in **d steps**, all $2^d$ processors receive the message.

