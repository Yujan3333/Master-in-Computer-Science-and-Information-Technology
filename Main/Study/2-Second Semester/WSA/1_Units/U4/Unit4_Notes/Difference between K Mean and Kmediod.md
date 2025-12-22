
### **Data Points:**

$P_1=(1,1),\ P_2=(2,2),\ P_3=(5,5),\ P_4=(6,6),\ P_5=(20,20)$
We want **k = 2 clusters**.

---

## **1️⃣ K-Means Clustering**

**Step 1: Initialize centroids**

* $C_1 = P_1=(1,1)$
* $C_2 = P_3=(5,5)$

**Step 2: Assign points to nearest centroid (Euclidean distance)**

| Point | d to C1 | d to C2 | Cluster |
| ----- | ------- | ------- | ------- |
| P1    | 0       | 5.66    | C1      |
| P2    | 1.41    | 4.24    | C1      |
| P3    | 5.66    | 0       | C2      |
| P4    | 7.07    | 1.41    | C2      |
| P5    | 26.87   | 21.21   | C2      |

**Step 3: Update centroids (mean of cluster points)**

* $C_1 = \text{mean of } P_1,P_2 = \left(\frac{1+2}{2}, \frac{1+2}{2}\right) = (1.5,1.5)$
* $C_2 = \text{mean of } P_3,P_4,P_5 = \left(\frac{5+6+20}{3}, \frac{5+6+20}{3}\right) = (10.33,10.33)$

✅ Notice how **outlier P5 shifts C2 centroid far away** → K-Means is sensitive to outliers.

---

## **2️⃣ K-Medoids Clustering**

**Step 1: Choose initial medoids**

* $M_1 = P_1=(1,1)$
* $M_2 = P_3=(5,5)$

**Step 2: Assign points to nearest medoid (distance)**

| Point | d to M1 | d to M2 | Cluster |
| ----- | ------- | ------- | ------- |
| P1    | 0       | 5.66    | M1      |
| P2    | 1.41    | 4.24    | M1      |
| P3    | 5.66    | 0       | M2      |
| P4    | 7.07    | 1.41    | M2      |
| P5    | 26.87   | 21.21   | M2      |

**Step 3: Swap medoids with non-medoid points to reduce cost**

* Check swapping M2 with P4 or P5:

  * New total distance (cost) is **less if we swap with P4** → final medoid = P4

**Step 4: Resulting clusters**

* Cluster1 = {P1,P2} → medoid = P1
* Cluster2 = {P3,P4,P5} → medoid = P4

✅ Notice how **K-Medoids chooses an actual point (P4) as medoid**, which is **less affected by outlier P5** → more robust than K-Means.

---

### **Key Difference in this Example**

| Feature                | K-Means              | K-Medoids                      |
| ---------------------- | -------------------- | ------------------------------ |
| Cluster center         | Mean → (10.33,10.33) | Medoid → P4=(6,6)              |
| Effect of outlier (P5) | Shifts centroid far  | Less affected                  |
| Cluster assignment     | Same initially       | Same initially, medoid refined |

---
# MORE ON K MEDIOD
Perfect! Let’s **see numerically how the medoid (center) changes** in K-Medoids. I’ll use a **small example** for clarity.

---

## **Data Points:**

$P_1=(1,1),\ P_2=(2,2),\ P_3=(5,5),\ P_4=(6,6),\ P_5=(20,20)$
We want **k = 2 clusters**.

---

### **Step 1: Initialize medoids**

* Choose: $M_1 = P_1=(1,1),\ M_2 = P_3=(5,5)$

---

### **Step 2: Assign points to nearest medoid**

| Point | d to M1 | d to M2 | Cluster |
| ----- | ------- | ------- | ------- |
| P1    | 0       | 5.66    | C1      |
| P2    | 1.41    | 4.24    | C1      |
| P3    | 5.66    | 0       | C2      |
| P4    | 7.07    | 1.41    | C2      |
| P5    | 26.87   | 21.21   | C2      |

**Clusters:**

* C1 = {P1, P2}
* C2 = {P3, P4, P5}

---

### **Step 3: Compute total cost for each medoid**

**Cluster C2 candidates for medoid:** P3, P4, P5

* **Cost if medoid = P3:**
  $$
  d(P3,P3)+d(P4,P3)+d(P5,P3) = 0 + 1.41 + 21.21 = 22.62
  $$

* **Cost if medoid = P4:**
  $$
  d(P3,P4)+d(P4,P4)+d(P5,P4) = 1.41 + 0 + 19.80 = 21.21
  $$

* **Cost if medoid = P5:**
  $$
  d(P3,P5)+d(P4,P5)+d(P5,P5) = 21.21 + 19.80 + 0 = 41.01
  $$

✅ Minimum cost = **21.21 → choose P4 as new medoid**

---

### **Step 4: Resulting medoids**

* **C1 medoid** = P1 (no change)
* **C2 medoid** = P4 (changed from P3 to P4 to reduce cost)

**Clusters after medoid update:**

* C1 = {P1, P2} → medoid = P1
* C2 = {P3, P4, P5} → medoid = P4

---

### **Key Observation**

* In **K-Medoids**, the “center” **does not move gradually like mean**.
* It **jumps to a data point** that minimizes the **total distance** of the cluster.
* Outlier P5 affects K-Means a lot, but K-Medoids chooses P4, which is more **representative of cluster**.

---
