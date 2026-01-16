
## 🕓 **Lamport’s Logical Clocks**

### 🔍 **The Problem:**

> “A man with one clock knows what time it is, but a man with two is never sure.”

In **distributed systems**, there's **no global clock**, so it’s hard to say **which event happened before another** — especially across different processes.

---

### ✅ **Happened-Before Relation (→ or $\prec_h$):**

* $a \rightarrow b$ means **event a happened before b**.
* If:

  * $a \rightarrow b$ and $b \rightarrow c$, then $a \rightarrow c$ (**transitive**).
* If $a \prec_h b$, then:

  $$
  T(a) < T(b)
  $$

  where $T$ is the logical timestamp.

But:

> If $T(a) < T(b)$, we **cannot guarantee** $a \rightarrow b$.
> This is a **limitation** of Lamport timestamps: **timestamps preserve causality**, but **not all ordering**.

---

### 📌 **Concurrent Events:**

If **no message is exchanged** between events `a` and `b` on different processes:

* Then neither $a \rightarrow b$ nor $b \rightarrow a$
* ⇒ `a` and `b` are **concurrent**

---

### ⏱️ **Lamport's Algorithm – How it Works:**

Each process maintains a **logical clock**, `LC`, initialized to 0.

#### Rules:

1. **Before executing an event**, increment local clock:

   $$
   LC := LC + 1
   $$

2. **When sending a message**, include the timestamp:

   $$
   msg := (data, LC)
   $$

3. **When receiving a message (msg, T\_msg):**

   * If local clock $LC < T_{msg}$, then:

     $$
     LC := T_{msg} + 1
     $$
   * Else:

     $$
     LC := LC + 1
     $$

$T_{msg}$ -> Timestamp attached to the message

==[Further Explanation of Receiving a message](Further%20Explanation%20of%20Receiving%20a%20message.md)==

---

### 📘 **Summary Table:**

| Concept                                   | Meaning                                   |
| ----------------------------------------- | ----------------------------------------- |
| $a \rightarrow b$                         | `a` causally happened before `b`          |
| $T(a) < T(b)$                             | Lamport timestamp of `a` is less than `b` |
| $T(a) < T(b) \Rightarrow a \rightarrow b$ | ❌ **Not guaranteed**                      |
| Concurrent events                         | No causal relationship                    |
| Timestamp update on receive               | `LC = max(LC, T_msg) + 1`                 |

---
