Example
Suppose that we have to classify 100 people as pregnant or not pregnant. This includes 40 pregnant women and the remaining 60 are not pregnant. Out of 40 pregnant women 30 pregnant women are classified correctly and the remaining 10 pregnant women are classified as not pregnant by the machine learning algorithm. On the other hand, out of 60 people in the not pregnant category, 55 are classified as not pregnant and the remaining 5 are classified as pregnant.
Compute accuracy, precision, recall, and F1-score for the above example.

## Answer
We are given a **binary classification problem**:

* Positive class (Pregnant) = 40
* Negative class (Not Pregnant) = 60

From the data:

| Actual \ Predicted      | Pregnant (Predicted +) | Not Pregnant (Predicted -) |
| ----------------------- | ---------------------- | -------------------------- |
| Pregnant (Actual +)     | 30 (TP)                | 10 (FN)                    |
| Not Pregnant (Actual -) | 5 (FP)                 | 55 (TN)                    |

Where:

* TP = True Positive = 30
* FN = False Negative = 10
* FP = False Positive = 5
* TN = True Negative = 55

---

### **1️⃣ Accuracy**

$$[
\text{Accuracy} = \frac{TP + TN}{TP + TN + FP + FN}
]$$

$$[
\text{Accuracy} = \frac{30 + 55}{30 + 55 + 5 + 10} = \frac{85}{100} = 0.85
]$$

✅ **Accuracy = 85%**

---

### **2️⃣ Precision (Positive Predictive Value)**

$$[
\text{Precision} = \frac{TP}{TP + FP}
]$$

$$[
\text{Precision} = \frac{30}{30 + 5} = \frac{30}{35} \approx 0.857
]$$

✅ **Precision ≈ 85.7%**

---

### **3️⃣ Recall (Sensitivity / True Positive Rate)**

$$
\text{Recall} = \frac{TP}{TP + FN}
$$

$$[
\text{Recall} = \frac{30}{30 + 10} = \frac{30}{40} = 0.75
]$$

✅ **Recall = 75%**

---

### **4️⃣ F1-Score**

F1-score is the **harmonic mean of precision and recall**:

$$[
F1 = 2 \cdot \frac{\text{Precision} \cdot \text{Recall}}{\text{Precision} + \text{Recall}}
]$$

$$[
F1 = 2 \cdot \frac{0.857 \cdot 0.75}{0.857 + 0.75} = 2 \cdot \frac{0.64275}{1.607} \approx 0.799
]$$

✅ **F1-score ≈ 79.9%**

---

### **✅ Summary Table**

| Metric    | Value |
| --------- | ----- |
| Accuracy  | 85%   |
| Precision | 85.7% |
| Recall    | 75%   |
| F1-Score  | 79.9% |

---