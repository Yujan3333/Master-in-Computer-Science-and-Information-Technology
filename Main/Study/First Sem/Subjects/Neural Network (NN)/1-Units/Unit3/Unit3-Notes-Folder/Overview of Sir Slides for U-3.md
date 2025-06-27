
### 🔑 Summary: Feedforward Neural Networks (FFNN)

#### 1. **Perceptron**

* A single-layer neural network used for classifying linearly separable patterns.
* Uses **adjustable weights and bias**.
* Learns via **Rosenblatt’s algorithm**.
* Works for AND/OR but **fails on XOR** due to linearity limitation.

#### 2. **Gradient Descent**

* Optimization method that updates weights to minimize error.
* **Learning rate** controls step size:

  * Too high: may overshoot.
  * Too low: slow convergence.

#### 3. **Batch Perceptron Algorithm**

* Updates weights **after processing all samples in a batch**.
* Reduces error by adjusting weights using gradient direction.

#### 4. **Multilayer Perceptron (MLP) / Feedforward Network**

* Has **input, hidden, and output layers**.
* Learns both classification and regression tasks.
* Trained using the **backpropagation algorithm**.
* Uses **non-linear activation** (e.g., sigmoid, tanh).

#### 5. **Learning Methods**

* **Batch Learning**: Updates after full dataset; accurate but slow.
* **Online Learning**: Updates after each sample; faster but noisy.
* **Mini-Batch Learning**: Combines both; balances speed and stability.

#### 6. **Backpropagation Algorithm**

* **Forward phase**: Computes output.
* **Backward phase**: Propagates error back and updates weights.
* Relies on **activation function derivatives** for gradient computation.

#### 7. **XOR Problem**

* Cannot be solved by a single-layer perceptron.
* Needs a **hidden layer** (i.e., a multilayer network).

#### 8. **Jacobian & Hessian**

* **Jacobian**: First-order partial derivatives matrix.
* **Hessian**: Second-order derivatives; used for fine-tuning learning.

#### 9. **Learning Rate Techniques**

* **Annealing**: Slowly decreases learning rate over time.
* **Adaptive Control**:

  * **Momentum, RMSProp, Adam, etc.**
  * Adjusts learning rate dynamically for each parameter.

#### 10. **Cross-Validation**

* Divides data into **training, validation, and testing** sets.
* **K-Fold CV** ensures all data is used efficiently.

---

