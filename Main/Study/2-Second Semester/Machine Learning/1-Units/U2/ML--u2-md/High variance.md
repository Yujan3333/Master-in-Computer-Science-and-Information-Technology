In **machine learning**, **high variance** means:

> **The model learns the training data too well, including noise, and performs poorly on new (unseen) data.**

In simple words 👉 the model is **too sensitive to the training data**.

---

### What happens in high variance?

* Model fits training data **almost perfectly**
* **Training error is very low**
* **Test/validation error is high**
* Small change in data ⇒ big change in prediction

This is basically **overfitting**.

---

### Intuition (exam-friendly)

Think of a student who **memorizes answers** instead of understanding concepts.

* Same questions → perfect marks
* New questions → poor performance

That’s **high variance**.

---

### Example

Suppose you fit a **very complex curve** to simple data:

* Training accuracy = 99%
* Test accuracy = 60%

The model learned **noise**, not the true pattern → **high variance**.

---

### Causes of high variance

* Model is **too complex**

  * Very deep neural network
  * High-degree polynomial
* **Too few training samples**
* **No regularization**
* Training for **too many epochs**

---

### How to reduce high variance

* Use **simpler model**
* Add **regularization** (L1 / L2)
* Get **more training data**
* Use **early stopping**
* Use **dropout** (in neural networks)

---

### One-line definition (for exams)

> **High variance occurs when a model overfits the training data and fails to generalize to unseen data.**
