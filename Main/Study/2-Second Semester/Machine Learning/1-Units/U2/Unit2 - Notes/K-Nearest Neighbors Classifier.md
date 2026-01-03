 In KNN there is already a set of points and when a new point is added then according to the value of *k(nearest neighbors)* distance from the new point to these point are calculated and the majority to which class it is close to is selected. 

---
# **K-Nearest Neighbors (K-NN) Algorithm**

K-NN is a **non-parametric** and **lazy learning** algorithm used for classification and regression.

---

## **1️⃣ Key Properties**

1. **Non-Parametric**

   * The model structure is **determined directly from the dataset**.
   * No assumptions are made about the underlying data distribution.

2. **Lazy Learning Algorithm**

   * K-NN does **not require training** to build a model.
   * All training data is stored and used **during testing**.
   * **Training is fast**, but prediction can be slower and computationally expensive.

---
- [Further Expanding on Non-parametric and Lazy learning](Further%20Expanding%20on%20Non-parametric%20and%20Lazy%20learning.md)

---

## **2️⃣ Core Concept**

* **K**: Number of nearest neighbors considered for predicting the class of a new data point.
* The algorithm classifies a new data point based on **majority vote** from its K nearest neighbors.
* **Similarity (distance) calculation** is the main step.

---

## **3️⃣ Distance Metric: Minkowski Distance**

Minkowski distance is a generalization of both Euclidean and Manhattan distances:

$$
D(x, y) = \left( \sum_{i=1}^{n} |x_i - y_i|^p \right)^{1/p}
$$

* **Manhattan Distance (L1 norm)**: (p = 1)
  $$
  D(x, y) = \sum_{i=1}^{n} |x_i - y_i|
  $$
* **Euclidean Distance (L2 norm)**: (p = 2)
  $$
  D(x, y) = \sqrt{\sum_{i=1}^{n} (x_i - y_i)^2}
  $$

---

## **4️⃣ Algorithm Steps**

1. Decide the value of **K**.
2. Compute the **distance** between the new data point and all points in the training set.
3. Select the **K nearest neighbors** based on distance.
4. Count the **number of neighbors in each class**.
5. Assign the new data point to the class with the **highest count** (majority vote).

---

## **5️⃣ Choosing the Right K**

* **Small K (e.g., K = 1)**:

  * Predictions are **unstable** and sensitive to noise.
  * Example: If a point is surrounded by 9 points of class A and 1 point of class B, K = 1 will classify it as B.

* **Large K**:

  * Predictions become **more stable** due to averaging/majority vote.
  * Accuracy improves up to a point.
  * If K is too large, **errors increase** because neighbors from other classes dominate.

* **Practical Approach**:

  * Test multiple K values and choose the one that **maximizes accuracy** on validation data.

---

## **6️⃣ Summary**

* K-NN is **simple, non-parametric, and instance-based**.
* **Distance metric** (usually Euclidean) and **K value** are crucial for performance.
* **Trade-off**: small K → sensitive to noise, large K → smoother but can misclassify.

---