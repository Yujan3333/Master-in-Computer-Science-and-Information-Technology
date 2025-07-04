
### **Dataset Splitting in Machine Learning**

* **Data is split into three sets:**

  * **Training Set**: Used to train the model and update weights.
  * **Validation Set**: Used to monitor performance and fine-tune the model.
  * **Test Set**: Used to evaluate final model performance on unseen data.

* **Split Ratios** vary based on dataset size:

  * Large datasets: 98:1:1
  * Smaller datasets: 80:10:10 or 70:15:15, etc.

---

### **Cross-Validation**

* **Purpose**: Evaluates model performance, especially when data is limited.

* **k-Fold Cross-Validation**:

  * Data is split into *k* equal folds.
  * Each fold is used once as the test set; the remaining *k−1* folds form the training set.
  * The model is trained and tested *k* times, and the results are averaged.
  * Example (k=3): If dataset has 6 samples, they are divided into 3 folds. Each fold is used once for testing.

* **Special cases**:

  * **k = 2**: 2-fold cross-validation (train on one half, test on the other).
  * **k = n**: Leave-One-Out Cross-Validation (suitable for small datasets).

---

### **Holdout Method vs Cross-Validation**

* **Holdout**: Splits dataset once into train/test sets.
* **Limitation**: Performance depends heavily on the split and may be misleading.
* **Cross-Validation**: More stable and reliable by averaging results from multiple folds.

---

