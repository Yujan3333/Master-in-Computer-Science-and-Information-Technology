**PAM (Partitioning Around Medoids)** is the classic [K-Medoid Algorithm](../../../../WSA/1_Units/U4/WSA--u4-md/K%20Medoid.md).

---

### **Definition**

PAM is a **partitioning clustering algorithm** that divides the dataset into **k clusters** by selecting **actual data points as medoids** (centers), instead of centroids like k-means.

* Each cluster has a **medoid** (most centrally located object in the cluster).
* The goal is to **minimize total dissimilarity** (sum of distances from points to their cluster medoid).

---

### **Steps of PAM**

1. **Initialize**

   * Select k data points randomly as initial medoids.

2. **Assign points to nearest medoid**

   * Use a distance metric (usually Euclidean or Manhattan).

3. **Update medoids (Swap step)**

   * For each medoid, consider swapping with each non-medoid point.
   * Compute total cost (sum of distances).
   * Keep the swap **only if cost decreases**.

4. **Repeat**

   * Assign points to nearest medoid and try swaps until **no swap reduces the total cost**.

---

### **Key Points**

* Uses **actual data points** as cluster centers → robust to outliers.
* **Cost function**:

$$
Cost = \sum_{i=1}^{k}\sum_{x \in C_i} d(x, m_i)
$$

* More **computationally expensive** than k-means (O(k(n-k)²) per iteration).
* Variants for large datasets: **CLARA, CLARANS**.

---

**One-line exam definition:**

> PAM (Partitioning Around Medoids) is a k-medoids clustering algorithm that partitions data into k clusters by iteratively selecting actual data points as medoids to minimize total distance from points to their medoid.

---
