
## 🧠 **Auto-associative Neural Network (AANN) – Summary**

### 🔹 **Definition**

An AANN is a neural network trained to reproduce its input as the output. It serves as an **associative memory** that can reconstruct original patterns from partial or noisy inputs.

---

### 🔹 **Key Characteristics**

* **Input = Output** during training
* **Fully connected** network (no hidden layers in basic AANN)
* **Symmetric weight matrix**: $w_{ij} = w_{ji}$
* **Pattern recall from noisy/distorted inputs**

---

### 🔹 **Hebbian Learning Rule**

> *"Neurons that fire together, wire together"*

* **Weight update**:

  $$
  \Delta w_{ij} = \alpha \cdot x_i \cdot y_j
  $$
* For pattern $s$:

  $$
  W = s^T \cdot s
  $$

  (Outer product of the pattern)

---

### 🔹 **Activation Function** (Bipolar Step)

$$
y_j =
\begin{cases}
1 & \text{if } y_{in} > c \\
x_j & \text{if } y_{in} = c \\
-1 & \text{if } y_{in} < c
\end{cases}
\quad \text{(usually } c = 0\text{)}
$$

---

### 🔹 **Training Algorithm**

1. Initialize weights to 0
2. For each pattern:

   * Set input/output: $x = y = s$
   * Update weights using Hebb’s rule
3. Alternatively: Use outer product $W = s^T \cdot s$

---

### 🔹 **Numerical Example**

* **Stored pattern**: $[1, 1, -1, -1]$
* **Test input**: $[-1, 1, -1, -1]$
* **Recovered output**: $[1, 1, -1, -1]$ ✅

Network successfully corrected the noisy input and recalled the original pattern.

---

### 🔹 **Key Observations**

* Effective **noise correction** and **pattern completion**
* **Symmetric weight matrix**
* **Positive diagonals** (self-reinforcement)
* **Negative off-diagonals** for anti-correlated neurons

---

### 🔹 **Applications**

* Pattern recognition (e.g., faces, characters)
* Denoising and noise reduction
* Associative memory systems
* Feature extraction and dimensionality reduction

---
