
## 🕰️ **Vector Clock Algorithm – Summary**

### ✅ **Purpose:**

To assign **timestamps** to events in distributed systems such that:

* We can **determine causal order**
* We can **detect concurrency** between events

---

## 🧠 **Rules for Vector Clocks**

### 1. **Initialization:**

Each process $P_i$ maintains a vector clock $V_i[1 \ldots N]$ where:

* $V_i[j] = 0$ for all $j$
* $V_i[i]$ tracks **its own** local time

---

### 2. **Before executing an event at $P_i$:**

```plaintext
V_i[i] := V_i[i] + 1
```

Every event increments the **local entry** of the vector.

---

### 3. **Sending a message from $P_i$:**

* Include the current vector $V_i$ in the message.

---

### 4. **Receiving a message at $P_j$:**

Assume $P_j$ receives vector $V_{\text{msg}}$ from $P_i$

Then:

```plaintext
∀ k:  V_j[k] := max(V_j[k], V_msg[k])
```

After that, increment local clock:

```plaintext
V_j[j] := V_j[j] + 1
```

---

## 📏 **Vector Comparison Rules**

To compare two vectors $V$ and $V'$:

| Relation    | Meaning                                     |
| ----------- | ------------------------------------------- |
| $V = V'$    | All entries are equal: $V[i] = V'[i]$ ∀ i   |
| $V \leq V'$ | $V[i] \leq V'[i]$ ∀ i                       |
| $V < V'$    | $V \leq V'$ and at least one $V[i] < V'[i]$ |
| Concurrent  | Neither $V < V'$ nor $V' < V$ holds         |

---

## 🔁 **Causal Relationships:**

| Rule                                        | Interpretation                                                           |
| ------------------------------------------- | ------------------------------------------------------------------------ |
| $e \rightarrow e' \Rightarrow V(e) < V(e')$ | If event `e` happened before `e'`, then `V(e)` is less                   |
| $V(e) < V(e') \Rightarrow e \rightarrow e'$ | Vector timestamps fully preserve causality                               |
| **Concurrent:**                             | If neither $V(e) < V(e')$ nor $V(e') < V(e)$ → **Events are concurrent** |

---

## 📘 **Example:**

Let’s say we have 3 processes: $P_1, P_2, P_3$

At some event:

* $V(e) = (2, 1, 0)$
* $V(e') = (3, 1, 1)$

Compare:

* $V(e)[1] = 2 < 3 = V(e')[1]$
* $V(e)[2] = 1 = 1 = V(e')[2]$
* $V(e)[3] = 0 < 1 = V(e')[3]$

So: $V(e) < V(e') \Rightarrow e \rightarrow e'$

Now try:

* $V(a) = (2, 1, 0)$
* $V(b) = (1, 2, 0)$

Then:

* $V(a)[1] > V(b)[1]$
* $V(a)[2] < V(b)[2]$

So neither is fully ≤ the other → **a and b are concurrent**

---

