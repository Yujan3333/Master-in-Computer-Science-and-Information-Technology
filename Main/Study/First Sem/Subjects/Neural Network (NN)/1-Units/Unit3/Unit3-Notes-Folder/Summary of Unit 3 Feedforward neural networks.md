

## ✅ Unit 3 Overview: Feedforward Neural Networks (FNNs)

### [Overview of Sir Slides for U-3](Overview%20of%20Sir%20Slides%20for%20U-3.md)
---

### 🔸 1. **Pattern classification using Perceptron**

* **Perceptron** is the **simplest neural network** model.
* It can classify data that is **linearly separable** (i.e., can be separated with a straight line).
* Uses:

  $$
  y = \text{sign}(w \cdot x + b)
  $$
* Learning rule:

  $$
  w_{\text{new}} = w_{\text{old}} + \eta (y_{\text{true}} - y_{\text{pred}})x
  $$
* ❗Only solves binary classification problems.

---

### 🔸 2. **Multilayer Feedforward Neural Networks (MLFFNNs)**

* **Also called MLP (Multilayer Perceptron)**.
* Has:

  * Input layer
  * One or more **hidden layers**
  * Output layer
* Each layer is **fully connected** to the next.

---

### 🔸 3. **Pattern Classification and Regression using MLFFNNs**

* **Classification**: Output is a **class label** (e.g., cat or dog).
* **Regression**: Output is a **real number** (e.g., house price).
* MLFFNNs can do both:

  * Use **sigmoid/softmax** for classification
  * Use **linear activation** for regression

---

### 🔸 4. **Error Backpropagation Learning**

* **Backpropagation** is the algorithm to **train MLFFNNs**.
* Steps:

  1. **Forward pass**: Calculate output
  2. **Compute error**: Error = target − output
  3. **Backward pass**: Use chain rule to update weights:

     $$
     w \leftarrow w - \eta \cdot \frac{\partial E}{\partial w}
     $$
* Repeats until error is small

---

### 🔸 5. **Fast Learning Methods: Conjugate Gradient Method**

* Backpropagation is **slow** for large networks
* Conjugate Gradient is a **faster optimization** method

  * Uses **second-order** info (not just gradients)
  * Better direction of weight update
* Doesn't need learning rate

---

### 🔸 6. **Autoassociative Neural Networks**

* Also called **Autoencoders**
* Used to **compress and reconstruct** input data
* Training goal: Make output = input
* Applications:

  * Noise reduction
  * Feature extraction

---

### 🔸 7. **Bayesian Neural Networks**

* Introduce **probability** to weights instead of fixed numbers
* Output is **distribution**, not just a number
* Useful when you want **uncertainty** in predictions
* Complex but powerful

---

## 📝 For Exam Preparation:

| Topic              | Focus On                                       |
| ------------------ | ---------------------------------------------- |
| Perceptron         | Learning rule, limitations                     |
| MLFFNN             | Structure, use for classification & regression |
| Backpropagation    | Forward & backward steps, weight update        |
| Conjugate Gradient | How it speeds up training                      |
| Autoencoder        | What it does, applications                     |
| Bayesian NN        | Basic idea, uncertainty, vs regular NN         |

---

