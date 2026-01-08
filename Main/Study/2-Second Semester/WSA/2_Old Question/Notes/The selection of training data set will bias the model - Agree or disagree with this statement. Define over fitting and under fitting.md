### **Statement:**

**“The selection of training data set will bias the model.”**

### **Answer:** **AGREE**

---

## **Justification**

The **training dataset directly influences what a model learns**.
If the dataset is **not representative** of the real-world population, the model will learn **biased patterns**, leading to biased predictions.

### Examples of biased training data:

* Data collected from **only one region or group**
* Class imbalance (e.g., 95% class A, 5% class B)
* Noisy or incomplete data
* Historical or sampling bias

📌 As a result, the model performs well on training data but **fails to generalize** to unseen data.

---

## **Definition of Overfitting**

### **Overfitting**

Overfitting occurs when a model:

* Learns the **training data too well**
* Captures **noise and irrelevant patterns**
* Performs **very well on training data**
* Performs **poorly on test/validation data**

### Causes:

* Too complex model
* Too many features
* Small training dataset
* Training for too long

### Example:

A decision tree that memorizes all training samples.

---

## **Definition of Underfitting**

### **Underfitting**

Underfitting occurs when a model:

* Is **too simple**
* Fails to capture the underlying pattern
* Performs **poorly on both training and test data**

### Causes:

* Model too simple
* Too few features
* Insufficient training

### Example:

Using a linear model for highly nonlinear data.

---

## **Comparison Table**

| Aspect           | Overfitting | Underfitting |
| ---------------- | ----------- | ------------ |
| Model complexity | Too high    | Too low      |
| Training error   | Very low    | High         |
| Test error       | High        | High         |
| Generalization   | Poor        | Poor         |
| Captures noise?  | Yes         | No           |

---

## **Conclusion**

* The choice of training data **does bias the model**
* Proper dataset selection, preprocessing, and validation are essential
* Overfitting and underfitting represent two extremes of model learning

---

### **Exam-ready closing line**

> A well-chosen, balanced, and representative training dataset is critical to build a model that generalizes well and avoids bias, overfitting, and underfitting.

