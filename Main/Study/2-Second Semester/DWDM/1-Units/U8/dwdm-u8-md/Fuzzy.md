Here’s a **simple, exam-friendly explanation of Fuzzy Clustering**:

---

## **Fuzzy Clustering (Soft Clustering)**

**Definition:**

* Unlike hard clustering (k-means), where each point belongs to **only one cluster**, fuzzy clustering allows a **point to belong to multiple clusters** with **membership degrees** between 0 and 1.

---

### **Key Idea**

* Each point $x_i$ has a **membership value** $u_{ij}$ for cluster $j$:

$$
0 \le u_{ij} \le 1, \quad \sum_{j=1}^{c} u_{ij} = 1
$$

* $c$ = number of clusters

---

### **Most Common Algorithm: Fuzzy C-Means (FCM)**

1. **Initialize** membership matrix $U = [u_{ij}]$ randomly.
2. Compute **cluster centers**:

$$
v_j = \frac{\sum_{i=1}^{n} (u_{ij})^m x_i}{\sum_{i=1}^{n} (u_{ij})^m}
$$

Where $m>1$ is the **fuzziness parameter** (usually $m=2$).

3. Update membership values:

$$
u_{ij} = \frac{1}{\sum_{k=1}^{c} \left(\frac{|x_i-v_j|}{|x_i-v_k|}\right)^{2/(m-1)}}
$$

4. Repeat steps 2–3 until **convergence** (change in $U$ is small).

---

### **Advantages**

* Handles **overlapping clusters** naturally.
* More realistic for many real-world problems.

### **Disadvantages**

* Sensitive to **initialization**.
* More **computationally expensive** than k-means.
* Needs **number of clusters** in advance.

---

### **One-line exam definition**

> Fuzzy clustering allows data points to belong to multiple clusters with varying membership values, commonly implemented using the Fuzzy C-Means algorithm.

---
