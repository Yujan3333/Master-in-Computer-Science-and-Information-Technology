
### 1. **Gradient Descent Sensitivity**

* Logistic regression uses the **sigmoid function**:

$$
\sigma(z) = \frac{1}{1 + e^{-z}}
$$

* When weights are updated with a **high learning rate**, the gradient step:

$$
\mathbf{w} := \mathbf{w} - \alpha \nabla J
$$

can **overshoot the minimum** of the loss function.

* This causes **weights to fluctuate or diverge**, especially at the start when values of $z = X \cdot w$ are large.

* In your results:

  * **Recall = 0.05**, meaning the model almost never predicted positive diabetes correctly.
  * **Specificity = 0.98**, so it predicts negatives correctly, but is “biased” toward negative class.

* This is a classic sign of **poor convergence due to a learning rate that’s too large** for the given data scale.

---

### 2. **Library Implementation Advantage**

* scikit-learn’s `LogisticRegression` uses **advanced solvers** like **LBFGS**, which:

  * Automatically **scale/normalize features** internally.
  * Use **adaptive step sizes** to prevent divergence.
  * Include **regularization** by default (penalizing extreme weights).

* This ensures **stable and faster convergence**, regardless of initial learning rate guesses.

---

### 3. **Why reducing lr to 0.00001 helped**

* Smaller learning rate = smaller weight updates:

$$
w := w - 0.00001 \cdot \nabla J
$$

* This made training **slower but more stable**, allowing the model to gradually learn weights that **better balance recall and specificity**.
* Recall improved from **0.05 → 0.4625**, F1-score also improved.

---

### ✅ **Summary**

* From-scratch implementation lagged because:

  1. Learning rate (0.01) was too high → unstable updates → poor recall.
  2. No feature scaling or adaptive optimization like scikit-learn uses.
* Library logistic regression handled this automatically, so it converged to a better solution faster.

---
