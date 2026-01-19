
## **Constraint-Based Clustering**

**Definition:**

* Clustering that incorporates **additional constraints or user-specified rules** to guide the clustering process.
* Ensures that the resulting clusters **satisfy specific conditions**, instead of purely relying on distance or density.

---

### **Types of Constraints**

1. **Must-Link (ML)**

   * Two points **must be in the same cluster**.
   * Example: Students in the same class must be grouped together.

2. **Cannot-Link (CL)**

   * Two points **cannot be in the same cluster**.
   * Example: Fraudulent and normal transactions must be in different clusters.

3. **Size Constraints**

   * Restrict cluster sizes (e.g., each cluster must have at least 5 points).

4. **Shape/Domain Constraints**

   * Clusters must satisfy domain-specific properties (e.g., geographic boundaries).

---

### **How it Works (General Steps)**

1. Input data and constraints.
2. Use clustering algorithm (k-means, hierarchical, density-based) **modified to respect constraints**.
3. Form clusters that **maximize similarity** while **satisfying constraints**.

---

### **Advantages**

* Produces **meaningful clusters** aligned with domain knowledge.
* Can improve clustering accuracy in **real-world applications**.

### **Disadvantages**

* Requires **user-defined constraints**.
* Can increase **computational complexity**.

---

### **One-line exam definition**

> Constraint-based clustering incorporates user-specified constraints (must-link, cannot-link, size, or shape) into the clustering process to produce meaningful clusters that satisfy these rules.

---
