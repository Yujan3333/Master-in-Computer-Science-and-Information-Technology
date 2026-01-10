## 📘 **Unit 3 – Learning Theory and Model Evaluation**

### **1. Bias–Variance Tradeoff**
- **Prediction Error** = Bias² + Variance + Irreducible Error
- **Bias** → Error due to oversimplified model (underfitting)
- **Variance** → Error due to sensitivity to training data (overfitting)
- Goal: Balance bias and variance to minimize MSE

---

### **2. Cross-Validation**
- **k-Fold Cross-Validation**: Data split into *k* subsets
- Each subset used once as test set, remaining as training
- Example: 3-fold CV with 6 data points shown

---

### **3. Classification Metrics**
- **Confusion Matrix** (TP, FP, TN, FN)
- **Accuracy** = (TP + TN) / Total
- **Precision** = TP / (TP + FP)
- **Recall (Sensitivity)** = TP / (TP + FN)
- **F1-Score** = 2 × (Precision × Recall) / (Precision + Recall)
- **ROC Curve** plots TPR vs FPR, AUC measures performance
- **Log Loss** for probabilistic classification

---

### **4. Regression Metrics**
- **MSE** = Mean Squared Error
- **RMSE** = Root Mean Squared Error
- **MAE** = Mean Absolute Error
- **RMSLE** = Root Mean Squared Log Error
- **R²** = Coefficient of Determination
- **Adjusted R²** penalizes irrelevant features

---

### **5. Clustering Metrics**
- **Dunn Index**: Higher is better (compact & well-separated clusters)
- **Silhouette Coefficient**: Ranges from -1 to 1
- **Elbow Method**: Find optimal *k* using SSE plot

---

### **6. Multi-Class Evaluation**
- Confusion matrix of size N×N
- Macro-average vs Micro-average for Recall, Precision, F1
- Weighted accuracy calculation

---

### **7. Model Selection**
- **Train/Validation/Test Split**
- **Cross-Validation for model comparison**
- **Hyperparameter Optimization** vs Parameters
- Techniques: Grid Search, Random Search, etc.

---

## ✅ **Summary**
This unit covers **core model evaluation techniques** in machine learning for **classification, regression, and clustering**, along with methods to select and tune models using validation strategies.
