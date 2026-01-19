Here’s a **short and exam-friendly explanation** of **OPTICS**:

---

## **OPTICS (Ordering Points To Identify the Clustering Structure)**

**Type:** Density-based clustering

**Key Idea:**

* Similar to DBSCAN, but **does not require a single density threshold**.
* Produces an **ordering of points** that captures cluster structure at **multiple densities**.

---

### **How it works (short version)**

1. Compute **core distance** and **reachability distance** for each point.

   * Core distance = distance to MinPts-th nearest neighbor
   * Reachability distance = max(core distance of neighbor, distance to neighbor)
2. Order points based on reachability distance.
3. Plot reachability graph → valleys represent **clusters at different densities**.

---

### **Advantages**

* Can find clusters of **varying density**.
* Can handle **noise and outliers**.
* No need to choose epsilon like DBSCAN.

---

**One-line exam definition:**

> OPTICS is a density-based clustering method that orders points to reveal the clustering structure at multiple densities, handling varying cluster densities and noise.

---

