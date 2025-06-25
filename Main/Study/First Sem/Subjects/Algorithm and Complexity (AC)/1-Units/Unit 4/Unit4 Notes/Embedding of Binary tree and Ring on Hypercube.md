![](../../../../../../../../Attachments/Embedding%20of%20Binary%20tree%20on%20Hypercube.png)

---

## 🌳 **Embedding of a Binary Tree into Hypercube (Hd)**

### 🔹 What is the goal?

We want to map the structure of a **binary tree** into a **hypercube**, so that we can simulate tree-based algorithms efficiently on a hypercube network.

---

### 🔸 Key Points:

* We take a **binary tree T** with **p leaves**, where

  $$
  p = 2^d \Rightarrow \text{so we are embedding into a d-dimensional hypercube (Hd)}
  $$

* **Each leaf** of the binary tree is **mapped to a unique processor** in the hypercube.
  → i-th leaf → i-th processor of hypercube

* **Internal nodes** of the tree (non-leaf) are **mapped to the same processor as their leftmost descendant leaf**.

---

### 📌 Example:

Let’s say $d = 3$, so:

* Total leaves = $2^3 = 8$
* Leaf nodes = 0, 1, 2, 3, 4, 5, 6, 7
* Hypercube has 8 processors: labeled with 3-bit binary (000 to 111)

#### Mapping:

| Tree Node                         | Mapped Processor in Hypercube     |
| --------------------------------- | --------------------------------- |
| Leaf 0                            | 000                               |
| Leaf 1                            | 001                               |
| ...                               | ...                               |
| Leaf 7                            | 111                               |
| Internal node with children (2,3) | mapped to 010 (leftmost leaf = 2) |
| Root (leftmost leaf = 0)          | mapped to 000                     |

✅ This reduces communication steps when simulating tree operations like **broadcast**, **traversal**, or **computation**.

---

## 🔁 **Embedding a Ring into a Hypercube**

### 🔹 What is a Ring?

A **ring topology** connects $p$ processors in a circle:

* Processor $i$ is connected to $i-1$ and $i+1$, with wrap-around.

---

### 🔸 How to embed?

* For a ring of size $2^d$, we can embed it into **Hd** (d-dimensional hypercube).
* Each processor in the ring is mapped to a **processor in hypercube** using **Gray codes**.

---

### 🔸 What is a Gray Code?

A **Gray code** is a binary numbering system where **only one bit changes** between successive numbers.

#### For example (for $d = 3$):

| Ring Index | Gray Code |
| ---------- | --------- |
| 0          | 000       |
| 1          | 001       |
| 2          | 011       |
| 3          | 010       |
| 4          | 110       |
| 5          | 111       |
| 6          | 101       |
| 7          | 100       |

These Gray codes correspond to nodes in the **Hypercube Hd**, and since adjacent codes differ by only 1 bit, the mapping forms a valid ring inside the hypercube.

---

## ✅ Why Gray Codes?

* Because in a **hypercube**, processors are connected if their binary labels differ in **exactly one bit** (Hamming distance = 1).
* So using Gray code ensures that each step in the ring is a **valid move** in the hypercube — no illegal connections.

---

## 📘 Exam-Ready Summary:

> A **binary tree** with $2^d$ leaves can be embedded into a **d-dimensional hypercube (Hd)** by mapping each leaf to a unique processor and each internal node to its leftmost descendant's processor.
>
> A **ring** with $2^d$ processors can be embedded into Hd using **Gray codes**, ensuring each adjacent pair in the ring maps to hypercube neighbors (1-bit difference). This preserves the ring's structure and supports efficient simulation.

---

Let me know if you'd like:

* A **diagram** for these embeddings
* A **step-by-step Gray code generation**
* Or how these embeddings help in **algorithm design**
