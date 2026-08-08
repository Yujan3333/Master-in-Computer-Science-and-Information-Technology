## **ROCK Algorithm (Clustering)**

**ROCK** stands for **RObust Clustering using linKs**.
It is a **hierarchical clustering algorithm** mainly designed for **categorical data**.

---

## **Key Idea**

Instead of using distance between data points, **ROCK uses links**.

* **Link** = number of **common neighbors** between two data points
* Two points are considered similar if they **share many neighbors**

👉 This makes ROCK **robust to noise** and suitable for categorical attributes.

---

## **Basic Definitions**

### **1. Neighbor**

Two points $(p_i)$ and $(p_j)$ are **neighbors** if their **similarity** is greater than a threshold $(\theta)$.

$$[
sim(p_i, p_j) \ge \theta
]$$

---

### **2. Link**

Number of **common neighbors** shared by two points.

$$[
link(p_i, p_j) = |N(p_i) \cap N(p_j)|
]$$

$where (N(p_i)) = neighbors of (p_i)$

---

## **How ROCK Works (Step-by-Step)**

1. **Compute similarity** between all data points
2. **Identify neighbors** using threshold $(\theta)$
3. **Create links** based on common neighbors
4. **Start with each point as a cluster**
5. **Merge clusters** that maximize the **link-based goodness measure**
6. **Stop when desired number of clusters is reached**

---

## **Goodness Measure (Conceptual)**

Clusters are merged if they have **many cross-links** compared to their sizes.

(Exact formula usually not required in exams)

---

## **Why ROCK is Special**

* Uses **connectivity**, not distance
* Handles **categorical data** well
* More **noise-resistant** than distance-based methods

---

## **Advantages**

✅ Works well for **categorical attributes**
✅ Robust to noise and outliers
✅ Captures **cluster shape** via links

---

## **Disadvantages**

❌ Computationally expensive
❌ Needs similarity threshold (\theta)
❌ Not suitable for very large datasets

---

## **Comparison with Other Clustering**

| Algorithm | Data Type       | Basis     |
| --------- | --------------- | --------- |
| K-means   | Numeric         | Distance  |
| DBSCAN    | Numeric         | Density   |
| **ROCK**  | **Categorical** | **Links** |

---

## **Exam-Friendly Definition**

> **ROCK is a hierarchical clustering algorithm that clusters data points based on the number of common neighbors (links), making it suitable for categorical data.**

---
# FORMULA
Yes ✅ — **ROCK is an agglomerative hierarchical clustering algorithm**.

Let’s answer both parts **clearly and exam-oriented**.

---

## **1️⃣ Is ROCK Agglomerative Hierarchical?**

**Yes.**

* ROCK starts with **each data point as a separate cluster**
* It **iteratively merges** the most similar clusters
* The process continues until the required number of clusters is obtained

👉 This is exactly the definition of **agglomerative hierarchical clustering**.

---

## **2️⃣ Formula Used in ROCK (Important Part)**

ROCK does **not use distance**.
It uses a **link-based goodness measure**.

---

### **Step 1: Neighbor Definition**

Two points $(p_i)$ and $(p_j)$are neighbors if:

$$[
sim(p_i, p_j) \ge \theta
]$$

where:

* (sim$(\cdot)$) = similarity measure
* $(\theta)$ = similarity threshold

---

### **Step 2: Link Between Two Points**

$$[
link(p_i, p_j) = |N(p_i) \cap N(p_j)|
]$$

---

### **Step 3: Goodness Measure (Main Formula)**

When merging **two clusters** $(C_i)$ and $(C_j)$:

$$[
g(C_i, C_j) = \frac{links(C_i, C_j)}{(n_i + n_j)^{1 + 2f(\theta)} - n_i^{1 + 2f(\theta)} - n_j^{1 + 2f(\theta)}}
]$$

where:

* $(links(C_i, C_j))$ = number of cross-links between clusters
* $(n_i, n_j)$ = sizes of clusters
* $(f(\theta))$ = function of similarity threshold

---

### **Function $(f(\theta))$**

$$[
f(\theta) = \frac{1 - \theta}{1 + \theta}
]$$

---

## **3️⃣ What This Formula Means (Simple Words)**

* **Numerator** → how strongly clusters are connected
* **Denominator** → penalizes large cluster size
* ROCK merges clusters that have **many links but reasonable size**

---

## **4️⃣ One-Line Exam Answer**

> **ROCK is an agglomerative hierarchical clustering algorithm that merges clusters using a link-based goodness measure instead of distance.**

---
