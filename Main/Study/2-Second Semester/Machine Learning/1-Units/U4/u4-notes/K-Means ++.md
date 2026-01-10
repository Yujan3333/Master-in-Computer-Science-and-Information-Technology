### K-Means++ Algorithm

**K-Means++** is an **improved version of K-Means** that chooses **better initial centroids**, which leads to:

* Faster convergence
* Better clustering results

---

## **Why K-Means++?**

Normal K-Means picks initial centroids **randomly**, which can give poor clusters.
**K-Means++** chooses centroids that are **far apart** from each other.

---

## **Steps of K-Means++**

### **1. Choose First Centroid Randomly**

Select one data point at random as the first centroid.

---

### **2. Compute Distance from Nearest Centroid**

For each data point (x), compute:


$$D(x) = \min_{c \in C} |x - c|^2
$$

where:

* (C) = set of already chosen centroids
* $(|x - c|)$ = Euclidean distance

---

### **3. Choose Next Centroid Using Probability**

Select the next centroid with probability:


$$P(x) = \frac{D(x)}{\sum_{i=1}^{n} D(x_i)}
$$

Points **farther from existing centroids** have a **higher chance** of being selected.

Repeat steps 2 and 3 until **K centroids** are chosen.

---

### **4. Apply Standard K-Means**

Once centroids are initialized:

* Assign points to nearest centroid
* Update centroid using mean formula:

$$[
\mu_j = \frac{1}{|C_j|} \sum_{x \in C_j} x
]$$

Repeat until convergence.

---

## **Key Difference from K-Means**

| K-Means                       | K-Means++            |
| ----------------------------- | -------------------- |
| Random initialization         | Smart initialization |
| May converge to poor solution | Better clustering    |
| More iterations               | Fewer iterations     |

---

### **One-line exam answer ⭐**

> K-Means++ improves K-Means by initializing centroids using a probability proportional to the squared distance from existing centroids, resulting in faster and more accurate clustering.
