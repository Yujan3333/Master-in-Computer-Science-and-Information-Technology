



## 📘 Prefix Computation on Hypercube

### 🔹 What is Prefix Computation?

> Given an array of values $[x_0, x_1, ..., x_{n-1}]$, prefix computation means computing:

$$
s_i = x_0 \oplus x_1 \oplus \cdots \oplus x_i
$$

Where $\oplus$ is an associative operator (e.g., +, \*, max).

---

## 💡 Why Use Hypercube?

A **d-dimensional hypercube** has $2^d$ processors. So if we place one value per processor, we can perform prefix computation **efficiently in parallel** using a binary tree structure.

---

## 🔄 Two Phases of Prefix Computation

We simulate a **binary tree on a hypercube**, and perform the computation in **2 phases**:
![](../../../../../../../../Images/First_Sem_Images/Prefix%20Computation%20in%20Hypercube.png)

---

### 🔸 1. **Forward Phase (Upward Reduction)**

* Each **leaf** sends its data **upward** to the root.
* Each **internal node** receives two values from its children:

  * Left child sends $y$, right child sends $z$
  * Node computes $w = y \oplus z$
  * It stores $y$ (left child's total) and $w$ (combined total)
  * It then **sends $w$** to its parent.

✅ At the end, the **root** has the **total sum of all values**.

---

### 🔸 2. **Reverse Phase (Downward Distribution)**

* The **root** starts by sending:

  * $0$ to its **left child**
  * $y$ (from forward phase) to its **right child**
* Each node then:

  * Receives a prefix value $q$ from parent
  * Sends:

    * $q$ to **left child**
    * $q \oplus y$ to **right child**
* Each **leaf** now receives its correct prefix value and **adds it to its own $x_i$**.

✅ Final prefix value is stored at each processor.

---

## ⏱️ Time Complexity

* Each phase takes $d$ steps (height of binary tree over $2^d$ leaves).
* So, total time:

  $$
  O(d)
  $$

---

## ✅ Summary (For Exam):

> **Prefix computation** on a hypercube with $2^d$ processors can be done using **binary tree embedding** in two phases:
>
> * **Forward Phase** computes partial results upward
> * **Reverse Phase** distributes prefix sums downward
>   This algorithm runs in **O(d)** time, where $d = \log_2 n$

