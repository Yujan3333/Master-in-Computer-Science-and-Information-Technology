## **Ensemble Techniques**

**Idea:**

* Combine **multiple models** to make a **better prediction** than a single model.
* Reduces **bias**, **variance**, or **both** depending on method.

---

### **Types of Ensemble Methods**

1. **Bagging (Bootstrap Aggregating)**

   * Build **multiple models independently** on **different random subsets** of training data.
   * **Average predictions** (regression) or **majority vote** (classification).
   * Reduces **variance** → prevents overfitting.
   * Example: **Random Forest** (bagging of decision trees)

2. **Boosting**

   * Build models **sequentially**, each focusing on **mistakes of previous model**.
   * Gives **higher weight** to misclassified points.
   * Reduces **bias** → improves accuracy.
   * Examples: **AdaBoost, Gradient Boosting, XGBoost**

3. **Stacking**

   * Combine predictions of **different models** using a **meta-model**.
   * Meta-model learns to weigh predictions of base models.
   * Example: Combine Logistic Regression + Decision Tree + SVM → meta-model predicts final output

---

### **Key Points**

| Technique | How it Works                             | Reduces                 |
| --------- | ---------------------------------------- | ----------------------- |
| Bagging   | Parallel models on random subsets        | Variance                |
| Boosting  | Sequential models correcting errors      | Bias                    |
| Stacking  | Combine different models with meta-model | Both (if done properly) |

---

### **Example (Bagging vs Boosting)**

* **Bagging:** 3 decision trees trained on 3 random subsets → final prediction = majority vote
* **Boosting:** 1st tree predicts, 2nd tree focuses on mistakes of 1st, 3rd tree focuses on mistakes of 2nd → combine weighted predictions

---
