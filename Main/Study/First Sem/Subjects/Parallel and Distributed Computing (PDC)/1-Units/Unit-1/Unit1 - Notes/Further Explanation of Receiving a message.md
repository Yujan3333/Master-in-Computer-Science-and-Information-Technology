
### 📨 **Receiving a Message in Lamport’s Algorithm**

When **a process receives a message**, it must update its **logical clock (LC)** to ensure that **causality is preserved**.

---

## 🔧 What’s in the message?

Every message has:

* Some **data**
* A **timestamp** $T_{\text{msg}}$ → the **sender's logical clock value at the time it sent the message**

---

## 🎯 Goal:

Ensure that:

$$
\text{If event } a \rightarrow b \text{ (i.e., } a \text{ happened before } b \text{)}, \text{ then } T(a) < T(b)
$$

So, when a message is received, the receiving process’s clock must **advance if needed** to reflect that **the message came from an earlier event**.

---

## 🔁 The Logic:

### ✅ Case 1:

**If your current clock $LC < T_{\text{msg}}$**

Then set your clock to:

$$
LC := T_{\text{msg}} + 1
$$

💡 Why?
Because this message was sent at $T_{\text{msg}}$, so your receiving of it must happen **after** that. You set your clock ahead to reflect that.

---

### 🔁 Case 2:

**Else (your clock $LC \geq T_{\text{msg}}$)**

Then just increment:

$$
LC := LC + 1
$$

💡 Why?
Because your clock is already **ahead or equal** to the message’s timestamp. You’re not violating causality, but you must still advance your clock to move forward in logical time.

---

### 🧠 Example:

#### Initial State:

* **Process P1** has clock = 5
* **Process P2** has clock = 3

#### P1 sends a message to P2:

* Message carries: `T_msg = 5`

#### P2 receives the message:

* P2's local clock is 3
* Since $3 < 5$, apply:

  $$
  LC := T_{\text{msg}} + 1 = 5 + 1 = 6
  $$
* So now, P2 updates its clock to 6.

---

### Final Intuition:

Lamport timestamps **don’t give exact time**, but ensure that:

* If **a causes b**, then **timestamp(a) < timestamp(b)**.
* By updating the clock this way, we **preserve causal ordering** across distributed processes.

---
## Swapping the value in numerical

### 🔁 **Setup After Swapping:**

* **Process P1 (sender)**: Clock = **3**
* **Process P2 (receiver)**: Clock = **5**

---

### 📨 **Step-by-Step Execution:**

#### 1. **P1 sends a message**

* Timestamp included in the message:

  $$
  T_{\text{msg}} = 3
  $$

#### 2. **P2 receives the message**

* P2's local clock before receiving = **5**
* Compare: $LC = 5$ vs $T_{\text{msg}} = 3$

Now:

$$
LC = 5 \geq 3 = T_{\text{msg}}
$$

So, we use the second rule:

### ✅ **Apply Rule:**

$$
LC := LC + 1 = 5 + 1 = 6
$$

---

### 📌 **Final Result:**

* P2 updates its clock to **6**
* Logical time has advanced, and **causality is preserved**
