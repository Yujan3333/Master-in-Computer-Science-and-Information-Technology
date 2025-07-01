![](../../../../../../../../Images/First_Sem_Images/Computing%20number%20of%20descendants.png)
## 🧾 Problem:

Given:

* A **rooted tree** $T$
* The **Euler Tour** of $T$
* The goal is to compute the **number of descendants** of any node $u$ using prefix sums of weights.

---

### 🔁 Step-by-step Breakdown:

1. **Euler Tour Visits of a Node**
   In an Euler Tour:

   * Each node $u$ is visited $d(u) + 1$ times.

     * $u_1$: first visit (entering node)
     * $u_2, u_3, ..., u_{d(u)+1}$: intermediate visits (after visiting each child)

2. **Assigning Weights**

   * Weight of **1** to the **first visit** $u_1$
   * Weight of **0** to all other visits: $u_2, u_3, ..., u_{d(u)+1}$

3. **Prefix Sum of Weights**

   * Let $r(v)$ denote the **prefix sum of weights** up to position $v$ in the Euler Tour.

     * $r(u_1)$: prefix sum at the first visit to $u$
     * $r(u_{d(u)+1})$: prefix sum at the last visit to $u$

4. **Formula to Compute Number of Descendants**

   * The number of descendants of node $u$, including $u$ itself, is:

$$
\text{descendants}(u) = r(u_{d(u)+1}) - r(u_1) + 1
$$

---

### 📘 Why It Works

* The prefix sum increases only at **first visits** of nodes (those assigned weight 1).
* The difference $r(u_{d(u)+1}) - r(u_1)$ counts how many **first-time visits** to nodes (i.e., how many nodes in the subtree rooted at $u$) occurred **after $u_1$** and **up to $u_{d(u)+1}$**.
* Add 1 to include $u$ itself.

---

### 🧠 Example:

Let’s say Euler tour has:

```
A₁ (1) → B₁ (1) → B₂ (0) → C₁ (1) → C₂ (0) → A₂ (0)
```

* Node A:

  * $u_1 = A₁$, weight = 1, prefix sum = 1
  * $u_{d(u)+1} = A₂$, weight = 0, prefix sum = 3

$$
\text{descendants}(A) = r(A₂) - r(A₁) + 1 = 3 - 1 + 1 = 3
$$

✅ A has 3 descendants: A, B, C.

---
