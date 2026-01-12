
### 1. Data Breakdown

The diagonal elements (top-left to bottom-right) represent the **True Positives (TP)** for each class.

| Class | Ideal | Premium | Good | V. Good | Fair | **Total (Row Sum)** |
| --- | --- | --- | --- | --- | --- | --- |
| **Ideal** | **5389** | 626 | 93 | 353 | 5 | **6466** |
| **Premium** | 1213 | **2288** | 142 | 484 | 8 | **4135** |
| **Good** | 391 | 447 | **305** | 209 | 30 | **1382** |
| **V. Good** | 1539 | 1047 | 250 | **769** | 20 | **3625** |
| **Fair** | 102 | 108 | 104 | 98 | **71** | **483** |
| **Total Samples ()** |  |  |  |  |  | **16091** |

---

### 2. Calculating the Requested Metrics

#### **A. Overall Accuracy**

Accuracy is the sum of all correct predictions (the diagonal) divided by the total number of samples.


#### **B. Weighted Average Accuracy**

In multiclass classification, "Weighted Average Accuracy" often refers to **Weighted Recall**. This is calculated by taking the accuracy (Recall) of each individual class and weighting it by the number of actual instances (support) of that class.

1. **Recall for each class ():**
* **Ideal:** 
* **Premium:** 
* **Good:** 
* **V. Good:** 
* **Fair:** 


2. **Weighted Average:**



*Note: Mathematically, Weighted Recall is identical to the Overall Accuracy calculated above () because the weights cancel out the denominators.*

#### **C. Macro Recall**

Macro Recall is the simple arithmetic average of the recall for all classes, giving each class equal weight regardless of its size.


#### **D. Micro Recall**

Micro Recall aggregates the TPs and False Negatives across all classes. In a standard confusion matrix where every sample belongs to exactly one class, **Micro Recall is always equal to Overall Accuracy**.


---

### Summary Table

| Metric | Value |
| --- | --- |
| **Overall Accuracy** | 54.83% |
| **Weighted Avg Accuracy** | 54.83% |
| **Macro Recall** | 39.32% |
| **Micro Recall** | 54.83% |
