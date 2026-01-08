## **Evaluating a Classification Model**

After building a classification model, we need to **measure how well it performs**.

### **1️⃣ Use a Test Set**

* The **test set** contains **labeled data** **not used** in training.
* The model predicts the class of each test sample.
* Compare **predicted label vs actual label**.

---

### **2️⃣ Key Metrics**

#### **a) Accuracy**

* Percentage of correctly classified samples.
* Formula:
  $$\text{Accuracy} = \frac{\text{Number of correct predictions}}{\text{Total number of predictions}} \times 100$$

#### **b) Confusion Matrix**

* Shows counts of **true vs predicted classes**.

| | Predicted Positive | Predicted Negative |
|---------------|-----------------|-----------------|
| Actual Positive | True Positive (TP) | False Negative (FN) |
| Actual Negative | False Positive (FP) | True Negative (TN) |

---

#### **c) Precision**

* Measures how many predicted positives are actually positive.
  $$\text{Precision} = \frac{TP}{TP + FP}$$

#### **d) Recall (Sensitivity)**

* Measures how many actual positives are correctly predicted.
  $$\text{Recall} = \frac{TP}{TP + FN}$$

#### **e) F1-Score**

* Harmonic mean of **Precision** and **Recall**.
  $$\text{F1} = 2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision + Recall}}$$

---

### **3️⃣ ROC Curve & AUC**

* **ROC Curve:** Plots True Positive Rate (Recall) vs False Positive Rate (FPR).
* **AUC (Area Under Curve):** Measures overall ability of model to discriminate classes.

---

### **4️⃣ Other Points**

* **Cross-validation:** Helps estimate model performance more reliably.
* **Overfitting check:** Accuracy on training vs test set should not differ too much.

---

✅ **Summary for exams:**

1. Test on **independent test set**.
2. Use **Accuracy, Precision, Recall, F1-score**.
3. Optional: ROC & AUC for binary classification.
4. Avoid overfitting by keeping test set separate.

---
