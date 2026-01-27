## Q3. Dissimilarity and Partitioning Methods

**Question:** How is the dissimilarity between interval-scaled variables computed? Explain the general working principle of partitioning methods.

### Dissimilarity in Interval-Scaled Variables

Interval-scaled variables are continuous measurements (e.g., temperature, weight). Dissimilarity is typically measured using **distance metrics**.

1. **Standardization:** To ensure all features contribute equally, data is often standardized using the **Z-score**:


2. **Euclidean Distance:** The most common measure for dissimilarity, representing the straight-line distance between two points  and :


3. **Manhattan Distance:** The sum of absolute differences (city-block distance):



### Working Principle of Partitioning Methods

Partitioning methods (like **K-Means**) organize  objects into  clusters by iteratively optimizing a distance-based objective function.

**The Algorithm (K-Means):**

1. **Initialize:** Randomly choose  objects as the initial cluster centers (centroids).
2. **Assign:** Assign each remaining object to the cluster with the nearest centroid (typically using Euclidean distance).
3. **Update:** Calculate the new mean value (centroid) for each cluster based on the objects assigned to it.
4. **Iterate:** Repeat the assignment and update steps until the centroids no longer change (convergence).

> [!TIP]
> **Key Characteristic:** Partitioning methods are "relocation" algorithms—they move objects from one group to another until the total within-cluster variance is minimized.

---
