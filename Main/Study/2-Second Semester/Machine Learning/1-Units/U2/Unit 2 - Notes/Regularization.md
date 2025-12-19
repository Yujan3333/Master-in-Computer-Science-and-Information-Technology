## What is Regularization?

> **Regularization is a technique used to reduce overfitting by adding a penalty to large model weights.**

In simple words:

* It **discourages the model from becoming too complex**
* Keeps weights **small and controlled**
* Helps reduce **high variance**

---

## Why add regularization?

Without regularization, the model may:

* Fit noise
* Learn very large weights
* Overfit training data

So we **modify the cost function**.

---

## General idea (very important)

Original cost function:
$$
J(\theta) = \text{Loss}
$$

With regularization:
$$
J(\theta) = \text{Loss} + \text{Penalty}
$$

The **penalty depends on the weights**.

---

## L2 Regularization (Ridge)

### Formula

$$
J(\theta) = \text{Loss} + \lambda \sum_{j=1}^{n} \theta_j^2
$$

### What it does

* Penalizes **square of weights**
* Pushes weights **close to zero**
* Does **NOT make weights exactly zero**

### Effect

* Smooth decision boundary
* Commonly used
* Good default choice

👉 Used in **Linear Regression, Logistic Regression, Neural Networks**

---

## L1 Regularization (Lasso)

### Formula

$$
J(\theta) = \text{Loss} + \lambda \sum_{j=1}^{n} |\theta_j|
$$

### What it does

* Penalizes **absolute value of weights**
* Forces some weights to become **exactly zero**

### Effect

* Performs **feature selection**
* Produces sparse models

---

## Key difference (exam-friendly)

| L1                     | L2                      |     |                 |
| ---------------------- | ----------------------- | --- | --------------- |
| Uses $                 | $\theta$                | $   | Uses $\theta^2$ |
| Can make weights **0** | Makes weights **small** |     |                 |
| Feature selection      | No feature selection    |     |                 |
| Sparse model           | Smooth model            |     |                 |

---

## Role of $\lambda$ (lambda)

* $\lambda$ = regularization strength
* Large $\lambda$ → **more penalty** → simpler model
* Small $\lambda$ → behaves like no regularization

---

## One-line exam answers

* **Regularization**: Technique to reduce overfitting by penalizing large weights.
* **L1**: Adds absolute value of weights to loss.
* **L2**: Adds squared value of weights to loss.

---
