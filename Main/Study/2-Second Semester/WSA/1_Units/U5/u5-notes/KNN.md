## **K-Nearest Neighbors (KNN) — In Short (Exam Ready)**

**KNN** is a **supervised, instance-based learning algorithm** used for **classification and regression**.
It classifies a new data point based on the **majority class of its K nearest neighbors**.

---

### **How it works**

1. Choose the value of **K**.
2. Compute distance (usually **Euclidean distance**) between the test point and all training points.
3. Select **K nearest neighbors**.
4. Assign the class by **majority voting** (or average for regression).

---

### **Distance Formula**

$$[
d = \sqrt{\sum (x_i - y_i)^2}
]$$

---

### **Advantages**

* Simple and easy to implement
* No training phase
* Works well for small datasets

---

### **Disadvantages**

* Slow for large datasets
* Sensitive to noise
* Performance depends on choice of **K**

---

### **One-line Exam Answer**

> KNN is a supervised learning algorithm that classifies a data point based on the majority class of its K nearest neighbors using distance measures.
