
## **K-Means Clustering Algorithm**

### **Definition**

**K-Means** is an **unsupervised learning algorithm** used to **partition data into K clusters**, where each data point belongs to the cluster with the **nearest mean (centroid)**.

---

## **Objective**

Minimize the **within-cluster sum of squares (WCSS)**, i.e., make points inside a cluster as close as possible to their centroid.

---

## **Algorithm Steps**

### **Step 1: Choose K**

Select the number of clusters **K** (given or decided using methods like Elbow method).

---

### **Step 2: Initialize Centroids**

Randomly choose **K data points** as initial cluster centroids.

---

### **Step 3: Assign Points to Nearest Centroid**

For each data point:

* Compute distance (usually **Euclidean distance**) to all centroids
* Assign the point to the **nearest centroid**

---

### **Step 4: Update Centroids**

For each cluster:

* Compute the **new centroid** as the **mean of all points** in that cluster

$$
\text{Centroid} = \frac{1}{n}\sum_{i=1}^{n} x_i
$$

---

### **Step 5: Repeat**

Repeat **Step 3 and Step 4** until:

* Centroids do not change **OR**
* Maximum number of iterations is reached

---

## **Output**

* K clusters
* Final centroids
* Cluster assignment for each data point

---

## **Example (Simple)**

Suppose K = 2 and points are:
(1,2), (2,3), (8,8), (9,9)

* Cluster 1 → (1,2), (2,3)
* Cluster 2 → (8,8), (9,9)

---

## **Advantages**

✔ Simple and easy to implement
✔ Fast for large datasets
✔ Works well when clusters are spherical and well separated

---

## **Disadvantages**

❌ Need to choose K beforehand
❌ Sensitive to initial centroids
❌ Performs poorly with non-spherical clusters
❌ Sensitive to outliers

---

## **Applications**

* Customer segmentation
* Image segmentation
* Document clustering
* Market analysis

---