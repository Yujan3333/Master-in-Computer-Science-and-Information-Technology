# **K-Medoids Clustering**

---

## **What is K-Medoids?**

**K-Medoids** is a **partitioning clustering algorithm** similar to K-Means, but:

* The **cluster center (medoid)** is an **actual data point**
* It minimizes **total dissimilarity** instead of squared distance
* It is **robust to noise and outliers**

---

## **Definition**

> **K-Medoids partitions the dataset into K clusters by selecting K representative objects (medoids) such that the sum of distances between points and their medoids is minimized.**

---

## **Why K-Medoids instead of K-Means?**

| Feature        | K-Means               | K-Medoids           |
| -------------- | --------------------- | ------------------- |
| Cluster center | Mean (not real point) | Medoid (real point) |
| Distance       | Euclidean only        | Any distance        |
| Outliers       | Sensitive             | Robust              |
| Cost function  | Squared distance      | Absolute distance   |

---

## **Objective Function**

K-Medoids minimizes:

$$
\sum_{i=1}^{k} \sum_{x \in C_i} d(x, m_i)
$$

where:

* $m_i$ = medoid of cluster $C_i$
* $d(x, m_i)$ = distance between point and medoid

---

## **K-Medoids Algorithm (PAM – Partitioning Around Medoids)**

### **Step-by-Step Algorithm**

1. Choose **K random points as initial medoids**
2. Assign each data point to the **nearest medoid**
3. For each medoid, try swapping it with a non-medoid
4. Compute total cost (sum of distances)
5. If cost decreases, **accept the swap**
6. Repeat steps 2–5 until no improvement

---

# **Numerical Example (Very Important)**

---

## **Given Data Points**

| Point | Value |
| ----- | ----- |
| $A$   | 2     |
| $B$   | 3     |
| $C$   | 6     |
| $D$   | 8     |
| $E$   | 9     |

Number of clusters:
$$
K = 2
$$

Distance measure:
$$
d(x,y) = |x - y|
$$

---

## **Step 1: Choose Initial Medoids**

Assume:
$$
m_1 = A(2), \quad m_2 = D(8)
$$

---

## **Step 2: Assign Points to Nearest Medoid**

| Point | Distance to 2 | Distance to 8 | Cluster |
| ----- | ------------- | ------------- | ------- |
| 2     | 0             | 6             | $C_1$   |
| 3     | 1             | 5             | $C_1$   |
| 6     | 4             | 2             | $C_2$   |
| 8     | 6             | 0             | $C_2$   |
| 9     | 7             | 1             | $C_2$   |

Clusters:

* $C_1 = {2,3}$
* $C_2 = {6,8,9}$

---

## **Step 3: Compute Total Cost**

$$
\text{Cost} = (0+1) + (2+0+1) = 4
$$

---

## **Step 4: Try Swapping Medoid**

Try swapping medoid $2$ with $3$:

New medoids:
$$
m_1 = 3,\quad m_2 = 8
$$

Recompute distances:

| Point | To 3 | To 8 | Cluster |
| ----- | ---- | ---- | ------- |
| 2     | 1    | 6    | $C_1$   |
| 3     | 0    | 5    | $C_1$   |
| 6     | 3    | 2    | $C_2$   |
| 8     | 5    | 0    | $C_2$   |
| 9     | 6    | 1    | $C_2$   |

New cost:
$$
(1+0) + (2+0+1) = 4
$$

No improvement → keep original medoids.

---

## **Step 5: Final Clusters**

$$
\boxed{C_1 = {2,3}}
$$

$$
\boxed{C_2 = {6,8,9}}
$$

Medoids:
$$
\boxed{m_1 = 2,\quad m_2 = 8}
$$

---

## **Advantages**

* Robust to outliers
* Works with any distance metric
* Medoids are real objects

---

## **Disadvantages**

* Computationally expensive
* Slower than K-Means
* Not suitable for very large datasets

---

## **2-Mark Exam Answer**

> **K-Medoids is a partitioning clustering algorithm that represents each cluster by a real data object (medoid) and minimizes total dissimilarity between points and medoids.**

---
