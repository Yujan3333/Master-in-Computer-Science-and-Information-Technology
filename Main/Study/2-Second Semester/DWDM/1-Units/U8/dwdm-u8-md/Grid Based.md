
## **Grid-Based Clustering**

**Idea:**

* Divide the **data space into a finite number of cells (grids)**.
* Perform clustering on **cells** instead of individual points → very fast.
* Complexity depends on **number of grids**, not number of data points.

---

### **1️⃣ STING (Statistical Information Grid)**

* Divides data space into **rectangular cells** hierarchically.
* Stores **statistical info** (mean, variance, count) for each cell.
* Uses statistics to **identify dense regions (clusters)**.
* Works well for **large spatial databases**.

**Steps:**

1. Construct hierarchy of grids.
2. Compute statistics for each cell.
3. Identify dense cells → clusters.

---

### **2️⃣ WaveCluster**

* Uses **wavelet transform** to find dense regions.
* Treats data in a **multi-resolution grid space**.
* Noise and outliers are naturally filtered out.
* Finds **clusters of arbitrary shape**.

**Steps:**

1. Map points to grid cells.
2. Apply wavelet transform → highlight dense regions.
3. Identify connected dense regions → clusters.

---

### **3️⃣ CLIQUE (Clustering In QUEst)**

* Works for **high-dimensional data**.
* Finds **dense units (cells) in subspaces**.
* Automatically detects relevant **subspace clusters**.

**Steps:**

1. Divide each dimension into intervals → create multi-dimensional grids.
2. Identify dense cells in each subspace.
3. Combine adjacent dense cells → clusters.

---

### **Key Points / Advantages of Grid-Based Methods**

* Very **fast and scalable**.
* Handles **large datasets efficiently**.
* Can discover **clusters of arbitrary shape** (WaveCluster, CLIQUE).

**One-line exam definition:**

> Grid-based clustering divides data space into cells and forms clusters by identifying dense cells; examples include STING (statistics-based), WaveCluster (wavelet-based), and CLIQUE (high-dimensional subspace clustering).

---