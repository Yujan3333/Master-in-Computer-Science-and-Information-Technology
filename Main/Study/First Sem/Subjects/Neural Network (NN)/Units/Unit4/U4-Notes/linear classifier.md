A **linear classifier** is a type of model used in **machine learning** and **statistics** to separate data into different categories (or classes) using a **straight line** (in 2D), **plane** (in 3D), or **hyperplane** (in higher dimensions).

---

### 📌 Simple Definition:

A **linear classifier** makes predictions based on a **linear decision boundary**.  
It tries to find the best straight line (or plane) that separates the data points of different classes.

---

### 🧠 How It Works:

Given input features `x₁, x₂, ..., xₙ`, a linear classifier uses a **linear combination**:

z=w1x1+w2x2+...+wnxn+bz = w₁x₁ + w₂x₂ + ... + wₙxₙ + b

Then, it applies a decision rule:

- If `z ≥ 0`, classify as **Class A**
    
- If `z < 0`, classify as **Class B**
    

Here:

- `w₁, w₂, ..., wₙ` are **weights**
    
- `b` is the **bias**
    
- The line `z = 0` is the **decision boundary**
    

---

### 📉 Example in 2D:

Imagine two types of flowers plotted using `petal length` and `petal width`.

A **linear classifier** would try to draw a straight line that best separates the two types of flowers.

---

### ✅ Examples of Linear Classifiers:

|Model|Description|
|---|---|
|**Logistic Regression**|Often used for binary classification|
|**Perceptron**|A simple neural network model|
|**Support Vector Machine (SVM)** (with linear kernel)|Maximizes the margin between classes|
|**Linear Discriminant Analysis (LDA)**|Projects data to a line that best separates classes|

---

### ⚠️ Limitation:

A linear classifier **cannot** solve problems where the classes are **not linearly separable**, like:

- XOR problem
    
- Spiral data
    
- Complex curved boundaries
    

In such cases, **non-linear classifiers** (like neural networks or kernel SVMs) are needed.

---
