
## **1️⃣ K-Means Clustering**

**Goal:** Group data into $k$ clusters by minimizing distance to centroids.

**Example:**

Data points: $(1,2), (2,1), (4,5), (5,4)$
Choose $k=2$

**Step 1: Initialize centroids**

* $C_1 = (1,2), C_2 = (4,5)$

**Step 2: Assign points to nearest centroid**

* Distance formula: $d(x_i, c_j) = \sqrt{(x_i^1 - c_j^1)^2 + (x_i^2 - c_j^2)^2}$

| Point | d to C1 | d to C2 | Cluster |
| ----- | ------- | ------- | ------- |
| (1,2) | 0       | 5       | C1      |
| (2,1) | 1.41    | 4.24    | C1      |
| (4,5) | 4.24    | 0       | C2      |
| (5,4) | 4.24    | 1.41    | C2      |

**Step 3: Update centroids**
$$
C_1 = \frac{(1,2) + (2,1)}{2} = (1.5, 1.5), \quad
C_2 = \frac{(4,5) + (5,4)}{2} = (4.5, 4.5)
$$

**Repeat assignment → update** until centroids stop changing.

**Objective function:**
$$
J = \sum_{j=1}^{k} \sum_{x_i \in C_j} ||x_i - c_j||^2
$$

**Key:** Sensitive to outliers.

---

## **2️⃣ K-Medoids Clustering**

**Goal:** Like K-Means but uses actual points as **medoids**, robust to outliers.

**Example:**

Data points: $(1,2), (2,1), (4,5), (5,4), (20,20)$
Choose $k=2$

**Step 1: Choose medoids**

* Medoid candidates: $(1,2), (4,5)$

**Step 2: Assign points to nearest medoid** (use distance)

| Point   | d to (1,2) | d to (4,5) | Cluster |
| ------- | ---------- | ---------- | ------- |
| (1,2)   | 0          | 5          | M1      |
| (2,1)   | 1.41       | 4.24       | M1      |
| (4,5)   | 5.00       | 0          | M2      |
| (5,4)   | 5.00       | 1.41       | M2      |
| (20,20) | 19.80      | 21.21      | M1      |

**Step 3: Swap medoids if cost decreases**

* Medoid is the point minimizing total distance in cluster.

**Cost function:**
$$
J = \sum_{j=1}^{k} \sum_{x_i \in C_j} d(x_i, m_j)
$$

**Key:** Handles outliers better than K-Means.

---

## **3️⃣ ROCK Clustering (for categorical data)**

Robust Objective Clustering using links
**Goal:** Merge clusters based on **links** between points (common neighbors).

**Example:**

Data (neighbors in a graph):

* $A$ connected to $B,C$
* $B$ connected to $A,C$
* $C$ connected to $A,B,D$
* $D$ connected to $C,E$

**Step 1: Compute similarity (Jaccard coefficient)**
$$
sim(X,Y) = \frac{|Neighbors(X) \cap Neighbors(Y)|}{|Neighbors(X) \cup Neighbors(Y)|}
$$

* $sim(A,B) = |{B,C} \cap {A,C}| / |{B,C} \cup {A,C}| = 1/3 = 0.33$

**Step 2: Compute links (common neighbors)**

* $link(A,B) = 1$ (common neighbor C)

**Step 3: Merge clusters with highest link score**

* Continue until stopping criterion met.

**Key:** Works well for categorical data, no need to fix $k$.

---

## **4️⃣ DBSCAN (Density-Based Clustering)**

**Goal:** Identify clusters by **dense regions**, detect **noise**.

**Example:**

Points: $P1=(1,1), P2=(2,1), P3=(1,2), P4=(8,8)$

* $\epsilon = 1.5$, MinPts = 2

**Step 1: Find $\epsilon$-neighborhood**

* $N_\epsilon(P1) = {P1, P2, P3}$ → core point (≥ MinPts)
* $N_\epsilon(P2) = {P1,P2,P3}$ → core
* $N_\epsilon(P3) = {P1,P2,P3}$ → core
* $N_\epsilon(P4) = {P4}$ → noise

**Step 2: Form clusters**

* Cluster 1 = {P1, P2, P3}
* P4 = noise

**Definitions:**

* **Directly density-reachable:** $x_j \in N_\epsilon(x_i)$ & $|N_\epsilon(x_i)| \geq MinPts$
* **Density-reachable:** Through chain of core points
* **Density-connected:** Connected via some core point

**Key:** Can detect arbitrary-shaped clusters, robust to noise.

---

### ✅ Copy-Friendly Summary

**K-Means**: centroid = mean, minimize $J = \sum ||x_i - c_j||^2$
**K-Medoids**: medoid = actual point, minimize $J = \sum d(x_i,m_j)$
**ROCK**: merge based on links, similarity $sim(X,Y) = \frac{|N(X)\cap N(Y)|}{|N(X)\cup N(Y)|}$
**DBSCAN**: density clusters, $\epsilon$-neighborhood & MinPts

---
