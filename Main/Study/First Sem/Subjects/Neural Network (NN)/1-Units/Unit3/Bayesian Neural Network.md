
---

### 🧠 **Bayesian Neural Networks (BNNs) – Summary**

### 🔹 **Motivation**

* Traditional neural networks **learn fixed weights**, which can lead to **overconfident and incorrect predictions**.
* **Probabilistic approach** allows the network to model **uncertainty** in predictions.

### 🔹 **Types of Uncertainty**

1. **Data uncertainty**: Measurement errors, label noise
2. **Model uncertainty**: Due to limited or insufficient data

---

### 🔹 **Bayesian Approach**

* **Weights are distributions**, not fixed values
* The network **learns probability distributions** over weights and biases
* During inference, weights are **sampled from these distributions** to produce **predictive distributions**

---

### 🔹 **Key Benefit**

* Outputs include **confidence levels**
* Allows the model to express **uncertainty** in its predictions—especially useful in critical applications like medicine or autonomous driving

---

