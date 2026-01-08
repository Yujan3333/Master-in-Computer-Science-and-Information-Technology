### **Silhouette Score (Simple Explanation)**

The **silhouette score** measures **how well a data point fits in its cluster** compared to other clusters.

---

### **How it works (intuition)**

For each data point:

* **a** = average distance to other points in the **same cluster**
* **b** = average distance to points in the **nearest other cluster**

$$[
\text{Silhouette score} = \frac{b - a}{\max(a, b)}
]$$

---

### **Score Range & Meaning**

| Score value | Meaning                 |
| ----------- | ----------------------- |
| **+1**      | Very well clustered     |
| **≈ 0**     | On the cluster boundary |
| **< 0**     | Wrongly clustered       |

---

### **One-line exam definition**

> **Silhouette score measures how similar a data point is to its own cluster compared to other clusters.**

