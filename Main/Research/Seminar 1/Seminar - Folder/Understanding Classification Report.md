
## 1️⃣ Confusion Matrix (Image)

![](../../../../../Images/First_Sem_Images/Understanding%20Classification%20Report-Confusion%20Matrix.png)

**Axes:**

* **Y-axis (rows):** True labels (`True Negative`, `True Neutral`, `True Positive`)
* **X-axis (columns):** Predicted labels (`Predicted Negative`, `Predicted Neutral`, `Predicted Positive`)

**Values:**

|                   | Pred Negative | Pred Neutral | Pred Positive |
| ----------------- | ------------- | ------------ | ------------- |
| **True Negative** | **1896**      | 686          | 617           |
| **True Neutral**  | 457           | **2027**     | 675           |
| **True Positive** | 437           | 653          | **2080**      |

---

### What it tells you:

✅ **Diagonal values (correct predictions):**

* 1896 Negatives correctly predicted as Negative.
* 2027 Neutrals correctly predicted as Neutral.
* 2080 Positives correctly predicted as Positive.

✅ **Off-diagonal values (confusions):**

* **686 Negatives → predicted Neutral**
* **617 Negatives → predicted Positive**
* **457 Neutrals → predicted Negative**
* **675 Neutrals → predicted Positive**
* **437 Positives → predicted Negative**
* **653 Positives → predicted Neutral**

---

### Interpretation:

* **Model does best on Positive class (2080/3170 correct).**
* **Model does well on Neutral class (2027/3159 correct).**
* **Model struggles the most with Negatives, predicting them often as Neutral or Positive.**

---

## 2️⃣ Classification Report

```
              precision    recall  f1-score   support

    Negative       0.68      0.59      0.63      3199
     Neutral       0.60      0.64      0.62      3159
    Positive       0.62      0.66      0.64      3170

    accuracy                           0.63      9528
   macro avg       0.63      0.63      0.63      9528
weighted avg       0.63      0.63      0.63      9528
```

### Metric meanings:

✅ **Precision** (of predicted class X, how many were actually X):

* Neg: 0.68
* Neutral: 0.60
* Positive: 0.62

✅ **Recall** (of actual X, how many predicted correctly):

* Neg: 0.59
* Neutral: 0.64
* Positive: 0.66

✅ **F1-score** (balance of precision and recall):

* Neg: 0.63
* Neutral: 0.62
* Positive: 0.64

✅ **Accuracy:** 0.63 (63% of total predictions correct)

✅ **Macro avg:** unweighted mean across classes
✅ **Weighted avg:** accounts for support (number of samples per class)

---

## Summary:

✅ **Model predicts Positive and Neutral better than Negative.**
✅ Class-wise:

* **Positive:** best recall (0.66)
* **Negative:** best precision (0.68)
* **Neutral:** hardest, but reasonably predicted.

