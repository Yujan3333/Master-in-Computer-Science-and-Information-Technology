Let’s simplify and explain the concept of **Embedding** in networks — in a way that's **easy to understand**, **exam-ready**, and practical with examples.

---

## 🔷 What is **Embedding**?

> **Embedding** means mapping (placing) one network **into another network**.

It is used in parallel/distributed computing to **simulate** one network architecture (say, a ring or mesh) on **another network** (like a hypercube or butterfly).

---

## 🔹 Formal Definition:

> An **embedding** is a **one-to-one function** (mapping) from the **nodes of one graph G (domain)** to the **nodes of another graph H (range)**.

---

## 🔹 Why do we need embedding?

When we want to:

* Simulate an algorithm designed for network **G** on a hardware that has network **H**
* Embed smaller or simpler networks into more complex or scalable ones
* Reduce hardware cost or communication delays

---

## 🔹 Important Terms (with examples)

Let’s say we embed **graph G** into **graph H**:

---

### 🔸 1. **Dilation**

> The **longest distance (number of hops)** in H that any single edge in G is mapped to.

✅ Think of it as **“stretching”** an edge.

### Example:

* If edge (1 → 2) in G is mapped as (b → d → c) in H
* That’s 2 hops ⇒ **Dilation = 2**

---

### 🔸 2. **Expansion**

> Measures how many **extra nodes** are being used.

Formula:

$$
\text{Expansion} = \frac{|\text{Vertices of H used}|}{|\text{Vertices of G}|}
$$

✅ Example:

* G has 3 nodes
* H uses 4 nodes in mapping
  → **Expansion = 4/3**

---

### 🔸 3. **Congestion**

> Measures how many times a **single link (edge) in H** is used to simulate **multiple edges from G**.

✅ Example:

* If two different edges from G are mapped using the same path/link in H
  → **Congestion = 2**

---

## 🔸 Simple Mapping Example (Based on your content):
![](../../../../../../../../Attachments/Embedding%20of%20Other%20Network.png)
**Graph G (Original)**:
Vertices: {1, 2, 3}
Edges: (1-2), (1-3)

**Graph H (Target)**:
Vertices: {a, b, c, d}

### Mappings:

* 1 → b
* 2 → c
* 3 → a

### Mapping of edges:

* (1,2) → path (b → d → c)
* (1,3) → path (b → d → a)

### Calculate:

| Parameter      | Value                                                         |
| -------------- | ------------------------------------------------------------- |
| **Dilation**   | Max path length = 2 (for both edges)                          |
| **Expansion**  | 4/3 (4 nodes in H used for 3 in G)                            |
| **Congestion** | Link (b-d) and (d-c) are used multiple times → Congestion = 2 |

---

## ✅ Exam-Ready Summary:

> **Embedding** is a one-to-one mapping of a source graph G into a target graph H. Key parameters include:

* **Dilation**: Longest path in H for a single edge of G
* **Expansion**: Ratio of nodes used in H vs G
* **Congestion**: Max number of times a link in H is reused for simulating edges from G
  Efficient embeddings aim to minimize dilation, expansion, and congestion.
