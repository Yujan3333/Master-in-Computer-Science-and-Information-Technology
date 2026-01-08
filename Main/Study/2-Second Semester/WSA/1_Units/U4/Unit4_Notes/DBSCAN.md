
# **Density-Based Clustering: DBSCAN Algorithm**

### **Definition**

**DBSCAN (Density-Based Spatial Clustering of Applications with Noise)** is a **density-based clustering algorithm** that:

* Forms clusters as **dense regions** in data space
* Can find clusters of **arbitrary shape**
* **Handles noise/outliers** automatically
* Uses **density parameters** instead of number of clusters

---

## **Important Parameters**

* **ε (Epsilon)**: Radius of neighborhood
* **MinPts**: Minimum number of points required to form a dense region

---

## **Key Concepts (Simplified)**

---

### **1. ε-Neighborhood**

The **ε-neighborhood** of a point *p* is the set of all points whose distance from *p* is **less than or equal to ε**.

$$
N_\varepsilon(p) = { q \mid dist(p,q) \le \varepsilon }
$$

---

### **2. Core Point**

A point *p* is called a **core point** if the number of points in its ε-neighborhood is **at least MinPts**.

**Example:**
If **MinPts = 5**, and point *q* has 5 or more neighbors within ε, then *q* is a **core point**.

---

### **3. Directly Density-Reachable**

A point *p* is **directly density-reachable** from point *q* if:

* *p* is within ε-neighborhood of *q*, and
* *q* is a **core point**

---

### **4. Density-Reachable**

A point *p* is **density-reachable** from point *q* if there exists a **chain of points**:
$$
q \rightarrow p_1 \rightarrow p_2 \rightarrow \dots \rightarrow p
$$
where each point is **directly density-reachable** from the previous one.

---

### **5. Density-Connected**

Two points *p* and *q* are **density-connected** if:

* There exists a point *o* such that both *p* and *q* are **density-reachable from *o***

---

## **Types of Points in DBSCAN**

| Type             | Description                                         |
| ---------------- | --------------------------------------------------- |
| **Core Point**   | Has at least **MinPts** within ε                    |
| **Border Point** | Not a core point, but lies within ε of a core point |
| **Noise Point**  | Neither core nor border point                       |

**Example:**
If **MinPts = 7**

* Point **A** → Core point
* Point **B** → Border point
* Point **C** → Noise point

---

## **Advantages of DBSCAN**

✔ No need to specify number of clusters
✔ Detects **arbitrary shaped clusters**
✔ Automatically detects **noise and outliers**
✔ Works well with spatial and geographic data

---

## **Disadvantages of DBSCAN**

❌ Choosing ε and MinPts is difficult
❌ Performs poorly when data densities vary
❌ Not suitable for high-dimensional data
❌ Distance computation is expensive for large datasets

---

## **One-Line Exam Answer**

> **DBSCAN is a density-based clustering algorithm that forms clusters using dense regions and identifies noise automatically.**

---

