```python
# Lab 1 Continued
# 1.	Write python programs to predict diabetes using logistic regression. Implement the algorithm using library and without using library. Implement batch gradient descent. Find accuracy, precision, recall, F1-score, and specificity and compare both strategies (Use diabetes.csv). Assume train/test split is 70:30.
# 2.	Change value of learning rate 0.01 to 0.00001.
# 3.	Compare performance of both algorithms and write down conclusion.

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

# ---------------- Load Data ----------------
df = pd.read_csv("/content/drive/My Drive/Colab Notebooks/Machine Learning/Diabetes.csv")

# Features and target
X = df[['Pragnency', 'Glucose', 'Blod Pressure', 'Skin Thikness',
        'Insulin', 'BMI', 'DFP', 'Age']].values
y = df['Diabetes'].values

# Train/test split (70:30)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# ============================
# From-scratch Logistic Regression (Batch GD)
# ============================
def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def logistic_regression_batch_gd(X, y, lr=0.01, epochs=1000):
    m, n = X.shape
    X_b = np.c_[np.ones((m, 1)), X]  # add bias
    weights = np.zeros(n + 1)

    for _ in range(epochs):
        z = X_b.dot(weights)
        predictions = sigmoid(z)
        errors = predictions - y
        gradient = (1/m) * X_b.T.dot(errors)
        weights -= lr * gradient

    return weights

def predict(X, weights):
    X_b = np.c_[np.ones((X.shape[0], 1)), X]
    return (sigmoid(X_b.dot(weights)) >= 0.5).astype(int)

# ============================
# Function to evaluate model
# ============================
def evaluate_model(y_true, y_pred):
    acc = accuracy_score(y_true, y_pred)
    prec = precision_score(y_true, y_pred)
    rec = recall_score(y_true, y_pred)
    f1 = f1_score(y_true, y_pred)
    tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()
    spec = tn / (tn + fp)
    return acc, prec, rec, f1, spec

# ============================
# Run for both learning rates
# ============================
for lr in [0.01, 0.00001]:
    print(f"\n=== Learning rate: {lr} ===")

    # From scratch
    start = time.time()
    weights = logistic_regression_batch_gd(X_train, y_train, lr=lr, epochs=10000)
    train_time_scratch = time.time() - start
    y_pred_scratch = predict(X_test, weights)
    metrics_scratch = evaluate_model(y_test, y_pred_scratch)

    # With library
    start = time.time()
    model = LogisticRegression(max_iter=10000, solver='lbfgs')
    model.fit(X_train, y_train)
    train_time_lib = time.time() - start
    y_pred_lib = model.predict(X_test)
    metrics_lib = evaluate_model(y_test, y_pred_lib)

    # Print results
    print("From-scratch Logistic Regression:")
    print(f"Time: {train_time_scratch:.4f} s, Accuracy: {metrics_scratch[0]:.4f}, Precision: {metrics_scratch[1]:.4f}, Recall: {metrics_scratch[2]:.4f}, F1: {metrics_scratch[3]:.4f}, Specificity: {metrics_scratch[4]:.4f}")

    print("Library Logistic Regression:")
    print(f"Time: {train_time_lib:.4f} s, Accuracy: {metrics_lib[0]:.4f}, Precision: {metrics_lib[1]:.4f}, Recall: {metrics_lib[2]:.4f}, F1: {metrics_lib[3]:.4f}, Specificity: {metrics_lib[4]:.4f}")

```

---
## Explanation
### 1. **Importing Libraries**

```python
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
```

* `numpy` → numerical operations and arrays.
* `pandas` → load and handle tabular datasets (CSV).
* `train_test_split` → split data into training and testing sets.
* `LogisticRegression` → scikit-learn’s library implementation.
* `accuracy_score, precision_score, recall_score, f1_score, confusion_matrix` → evaluation metrics.

---

### 2. **Loading the Dataset**

```python
df = pd.read_csv("/content/drive/My Drive/Colab Notebooks/Machine Learning/Diabetes.csv")
```

* Reads the CSV file containing diabetes data into a Pandas DataFrame `df`.

---

### 3. **Selecting Features and Target**

```python
X = df[['Pragnency', 'Glucose', 'Blod Pressure', 'Skin Thikness',
        'Insulin', 'BMI', 'DFP', 'Age']].values
y = df['Diabetes'].values
```

* `X` → feature matrix containing the 8 input variables.
* `y` → target variable indicating diabetes (0 = no, 1 = yes).
* `.values` converts Pandas DataFrame/Series to **NumPy arrays**.

---

### 4. **Train/Test Split**

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
```

* Splits data into **training set (70%)** and **testing set (30%)**.
* `random_state=42` ensures reproducibility.

---

### 5. **Sigmoid Function**

```python
def sigmoid(z):
    return 1 / (1 + np.exp(-z))
```

* Sigmoid activation function for logistic regression:

$$
\sigma(z) = \frac{1}{1 + e^{-z}}
$$

* Converts linear combination of inputs to probability (0–1).

---

### 6. **From-Scratch Logistic Regression (Batch GD)**

```python
def logistic_regression_batch_gd(X, y, lr=0.01, epochs=1000):
    m, n = X.shape
    X_b = np.c_[np.ones((m, 1)), X]  # add bias
    weights = np.zeros(n + 1)
```

* `m` → number of samples, `n` → number of features.
* Adds **bias term** (column of 1s) to `X`.
* Initializes `weights` to zeros (`n+1` to include bias).

```python
    for _ in range(epochs):
        z = X_b.dot(weights)
        predictions = sigmoid(z)
        errors = predictions - y
        gradient = (1/m) * X_b.T.dot(errors)
        weights -= lr * gradient
```

* Computes **linear combination**: $z = X_b \cdot \mathbf{w}$.
* Applies **sigmoid** to get predicted probabilities.
* Computes **error**: $\hat{y} - y$.
* Computes **gradient of loss** (Batch GD):

$$
\nabla_{\mathbf{w}} J = \frac{1}{m} X_b^T (\hat{y} - y)
$$

* Updates weights: $\mathbf{w} := \mathbf{w} - \alpha \nabla_{\mathbf{w}} J$.

```python
    return weights
```

* Returns the **learned weights** after all epochs.

---

### 7. **Prediction Function**

```python
def predict(X, weights):
    X_b = np.c_[np.ones((X.shape[0], 1)), X]
    return (sigmoid(X_b.dot(weights)) >= 0.5).astype(int)
```

* Converts probabilities to **binary predictions**: 1 if ≥ 0.5, else 0.

---

### 8. **Evaluation Function**

```python
def evaluate_model(y_true, y_pred):
    acc = accuracy_score(y_true, y_pred)
    prec = precision_score(y_true, y_pred)
    rec = recall_score(y_true, y_pred)
    f1 = f1_score(y_true, y_pred)
    tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()
    spec = tn / (tn + fp)
    return acc, prec, rec, f1, spec
```

* Computes standard **classification metrics**:

  * Accuracy = $\frac{TP+TN}{TP+TN+FP+FN}$
  * Precision = $\frac{TP}{TP+FP}$
  * Recall = $\frac{TP}{TP+FN}$
  * F1-score = $2 \cdot \frac{Precision \cdot Recall}{Precision + Recall}$
  * Specificity = $\frac{TN}{TN+FP}$

---

### 9. **Training and Evaluation Loop**

```python
for lr in [0.01, 0.00001]:
    print(f"\n=== Learning rate: {lr} ===")
```

* Loops over **two learning rates**: 0.01 and 0.00001.

---

#### From-Scratch Logistic Regression

```python
    start = time.time()
    weights = logistic_regression_batch_gd(X_train, y_train, lr=lr, epochs=10000)
    train_time_scratch = time.time() - start
    y_pred_scratch = predict(X_test, weights)
    metrics_scratch = evaluate_model(y_test, y_pred_scratch)
```

* Measures **training time**.
* Trains **from-scratch BGD logistic regression**.
* Makes predictions on test set and evaluates metrics.

---

#### Library Logistic Regression

```python
    start = time.time()
    model = LogisticRegression(max_iter=10000, solver='lbfgs')
    model.fit(X_train, y_train)
    train_time_lib = time.time() - start
    y_pred_lib = model.predict(X_test)
    metrics_lib = evaluate_model(y_test, y_pred_lib)
```

* Trains scikit-learn’s `LogisticRegression` using the **LBFGS solver**.
* Measures training time and evaluates metrics.

---

### 10. **Printing Results**

```python
    print("From-scratch Logistic Regression:")
    print(f"Time: {train_time_scratch:.4f} s, Accuracy: {metrics_scratch[0]:.4f}, Precision: {metrics_scratch[1]:.4f}, Recall: {metrics_scratch[2]:.4f}, F1: {metrics_scratch[3]:.4f}, Specificity: {metrics_scratch[4]:.4f}")

    print("Library Logistic Regression:")
    print(f"Time: {train_time_lib:.4f} s, Accuracy: {metrics_lib[0]:.4f}, Precision: {metrics_lib[1]:.4f}, Recall: {metrics_lib[2]:.4f}, F1: {metrics_lib[3]:.4f}, Specificity: {metrics_lib[4]:.4f}")
```

* Prints **comparison of metrics and training time** for both from-scratch and library implementations.

---

### **Mathematical Summary**

1. **Logistic Regression Model**:

$$
P(y=1|x) = \sigma(z) = \frac{1}{1 + e^{-z}}, \quad z = w_0 + \sum_{i=1}^{n} w_i x_i
$$

2. **Loss Function (Binary Cross-Entropy)**:

$$
J(\mathbf{w}) = -\frac{1}{m} \sum_{i=1}^{m} \Big[ y_i \log(\hat{y}_i) + (1-y_i) \log(1-\hat{y}_i) \Big]
$$

3. **Gradient for Batch GD**:

$$
\nabla_{\mathbf{w}} J = \frac{1}{m} X_b^T (\hat{y} - y)
$$

4. **Weight Update**:

$$
\mathbf{w} := \mathbf{w} - \alpha \nabla_{\mathbf{w}} J
$$

5. **Prediction Rule**:

$$
\hat{y} = 
\begin{cases} 
1 & \text{if } \sigma(z) \ge 0.5 \\
0 & \text{if } \sigma(z) < 0.5
\end{cases}
$$

6. **Evaluation Metrics**:

* Accuracy, Precision, Recall, F1-score, Specificity as explained above.

---
## Conclusion
Here’s a clear conclusion based on your results:

---

### **Conclusion**

1. **From-scratch Logistic Regression performance depends heavily on the learning rate:**

   * At **learning rate 0.01**, the model achieved **low recall (0.05)**, meaning it failed to correctly identify most positive diabetes cases, even though specificity was very high (0.98).
   * Reducing the learning rate to **0.00001** improved **recall (0.4625)** and F1-score (0.5441), making the model better at identifying positive cases, but training became slightly slower.

2. **Library Logistic Regression is consistently better:**

   * Across both learning rates, scikit-learn’s implementation achieved higher **accuracy (0.7965)**, **precision (0.7797)**, **recall (0.5750)**, **F1-score (0.6619)**, and reasonably high specificity (0.9139).
   * It also trains faster than the from-scratch implementation.

3. **Key insights:**

   * **Learning rate matters** for gradient descent from scratch: too high can cause unstable training, too low slows convergence.
   * **From-scratch implementation** may struggle to match library performance without careful tuning, but it helps understand the **underlying math**.
   * **Library implementation** is optimized and robust, suitable for practical applications.

4. **Overall understanding:**

   * Batch Gradient Descent from scratch works but is sensitive to hyperparameters.
   * Using well-optimized libraries ensures better performance, faster training, and more reliable metrics.

---
## Question

[Why was Library giving better result when Learning rate was less](Why%20was%20Library%20giving%20better%20result%20when%20Learning%20rate%20was%20less.md)