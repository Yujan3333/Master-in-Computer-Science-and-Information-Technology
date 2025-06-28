

### 🔁 **Recurrent Neural Networks (RNNs)**

* RNNs process **sequential data** by passing **hidden state** information from one time step to the next.
* This allows **memory** of past inputs, unlike traditional feedforward networks where inputs/outputs are independent.
* **Key Feature:** Shared weights and a hidden state that acts as memory.

### ✅ **Applications**

* Time series forecasting
* Sequence prediction (e.g., next word in a sentence)
* Natural Language Processing (NLP)
* Speech recognition

---

### 🔄 **Forward Propagation in RNN**

* For each input in the sequence:

  * Compute new hidden state: $h_t = f(W_{xh} x_t + W_{hh} h_{t-1})$
  * Compute output: $y_t = W_{hy} h_t$

---

### 🧠 **Computational Power**

* RNNs are **Turing complete**, capable of simulating any Turing machine by mimicking a pushdown automaton with two stacks.

---

### 🧪 **Training with Backpropagation Through Time (BPTT)**

* Involves **unrolling the RNN** over time and computing gradients across time steps.
* **Loss:** Sum of losses across all time steps.
* Loss functions:

  * **Cross-entropy** → classification
  * **Mean squared error** → regression

---

### ⚠️ **Challenges in Training**

* **Vanishing gradients**: Small weight updates → hard to learn long dependencies.
* **Exploding gradients**: Very large updates → unstable learning.
* **High computational cost**: Especially for long sequences.

**Solutions:**

* **Gradient clipping**: Prevents exploding gradients.
* **Truncated BPTT**: Backpropagation is limited to a fixed number of steps.
* **Use of LSTM / GRU**: Designed to handle long-term dependencies.

---

### 🧩 **LSTM (Long Short-Term Memory) Networks**

* Solve vanishing gradient problem.
* Have two memory components:

  * **Hidden state** (short-term memory)
  * **Cell state** (long-term memory)

**3 Gates:**

1. **Forget gate**: Discards unnecessary information
2. **Input gate**: Adds useful new information
3. **Output gate**: Determines the next hidden state

---

### 🧮 **GRU (Gated Recurrent Unit) Networks**

* Simplified version of LSTM with similar performance.
* Only uses **hidden state** (no cell state).
* **2 Gates:**

  1. **Reset gate**: Controls how much past info to forget
  2. **Update gate**: Controls how much past info to carry forward

---

### 🧠 **Hopfield Networks**

* Single-layer fully connected recurrent networks.
* Work as **associative memory systems**: retrieve the closest stored pattern.
* Can be **discrete or continuous**.
* No self-loops; symmetric weights.

---

### 🎲 **Boltzmann Machines**

* Stochastic, recurrent neural networks.
* Neurons randomly choose binary states (0 or 1).
* Learn to represent binary data through weight optimization.
* Use a stochastic update rule and energy-based learning.

---
