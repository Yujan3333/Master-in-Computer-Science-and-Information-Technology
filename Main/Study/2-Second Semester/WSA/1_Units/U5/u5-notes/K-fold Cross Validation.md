## **K-Fold Cross Validation (Exam-oriented & Simple)**

### **Definition**

**K-Fold Cross Validation** is a **model evaluation technique** where the dataset is divided into **K equal parts (folds)**.
The model is trained **K times**, each time using **K−1 folds for training** and **1 fold for testing**.
The final performance is the **average of all K results**.

---

### **How it works (Step-by-Step)**

1. Divide the dataset into **K folds** of equal size.
2. Select **1 fold as test data**.
3. Use the remaining **K−1 folds as training data**.
4. Train the model and evaluate it.
5. Repeat steps 2–4 **K times**, changing the test fold each time.
6. Compute the **average accuracy/error**.

---

### **Example (K = 5)**

* Dataset → split into **5 folds**
* Iteration 1 → Fold 1 = test, others = train
* Iteration 2 → Fold 2 = test, others = train
* …
* Iteration 5 → Fold 5 = test, others = train

Final result = **Average of 5 evaluations**

---

### **Why use K-Fold Cross Validation?**

* Uses **entire dataset efficiently**
* Reduces **overfitting**
* Gives **more reliable performance estimate**
* Better than single train-test split

---

### **Advantages**

* Uses all data for training and testing
* Less bias in performance estimation
* Works well for **small datasets**

---

### **Disadvantages**

* Computationally expensive
* Not suitable for very large datasets
* Training time increases by **K times**

---

### **Common Values of K**

* **K = 5** → Faster, commonly used
* **K = 10** → More accurate, standard choice

---

### **One-line Exam Answer**

> K-Fold Cross Validation is a technique where the dataset is divided into K folds, the model is trained K times using K−1 folds for training and one fold for testing, and the final performance is the average of all trials.

