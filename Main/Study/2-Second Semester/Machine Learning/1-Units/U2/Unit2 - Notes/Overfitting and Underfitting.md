- [Overfitting VS Underfitting](Overfitting%20VS%20Underfitting.md)
## 1️⃣ What does “fitting” mean in ML?

In Machine Learning, **fitting** means:

> How well a model **learns the pattern** from training data and **generalizes** to new (unseen) data.

---

## 2️⃣ Underfitting

### 🔹 What is Underfitting?

Underfitting happens when a model is **too simple** to capture the underlying pattern in the data.

> The model **has not learned enough**.

### 🔹 Characteristics

* Poor performance on **training data**
* Poor performance on **test data**
* High **bias**
* Model assumptions are too strong or unrealistic

### 🔹 Example (Intuition)

Trying to fit a **straight line** to data that clearly follows a **curve**.

📉 The model ignores important patterns.

### 🔹 Causes

* Model is too simple (e.g., linear model for complex data)
* Too few features
* Insufficient training time
* High regularization

### 🔹 In one line (for exams):

> **Underfitting** occurs when a model is too simple and fails to learn the data patterns.

---

## 3️⃣ Overfitting

### 🔹 What is Overfitting?

Overfitting happens when a model **learns the training data too well**, including **noise and random fluctuations**.

> The model learns **too much**.

### 🔹 Characteristics

* Very high accuracy on **training data**
* Poor performance on **test/unseen data**
* [High variance](High%20variance.md) 
* Poor generalization

### 🔹 Example (Intuition)

A model that memorizes **every single point** instead of learning the general trend.

📈 The curve passes through all training points but fails on new data.

### 🔹 Causes

* Model is too complex
* Too many parameters
* Small training dataset
* Training for too many epochs

### 🔹 In one line (for exams):

> **Overfitting** occurs when a model learns noise in the training data and fails to generalize.

---

## 4️⃣ Bias–Variance View (Very Important)

| Case         | Bias | Variance |
| ------------ | ---- | -------- |
| Underfitting | High | Low      |
| Overfitting  | Low  | High     |
| Good Fit     | Low  | Low      |

---

## 5️⃣ Simple Analogy (Easy to Remember)

🎯 **Exam preparation analogy**:

* **Underfitting** → Studied only definitions, failed both practice and exam
* **Overfitting** → Memorized past questions, failed new questions
* **Good fit** → Understood concepts, passed both

---

## 6️⃣ How to Fix Them (Short Points)

### Fix Underfitting:

* Use a more complex model
* Add more features
* Reduce [Regularization](Regularization.md)
* Train longer

### Fix Overfitting:

* Use more training data
* Use [Regularization](Regularization.md) (L1, L2)
* Reduce model complexity
* Use early stopping
* Use cross-validation

---

## 7️⃣ One-Shot Exam Answer (5 Marks)

> **Underfitting** occurs when a machine learning model is too simple to capture the underlying pattern of the data, resulting in poor performance on both training and test datasets.
> **Overfitting** occurs when a model is too complex and learns noise from the training data, achieving high training accuracy but poor test accuracy.
> Underfitting is associated with high bias, while overfitting is associated with high variance.

---
## Figurative
![](../../../../../../../Images/Second_Sem_Images/Overfitting%20and%20Underfitting.png)