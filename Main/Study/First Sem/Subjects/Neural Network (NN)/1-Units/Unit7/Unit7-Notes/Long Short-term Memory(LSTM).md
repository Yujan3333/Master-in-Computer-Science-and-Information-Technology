
## 🔁 **What is an LSTM?**

LSTM (Long Short-Term Memory) is a special type of **Recurrent Neural Network (RNN)** designed to overcome the **vanishing gradient problem**, which limits a standard RNN’s ability to learn long-term dependencies in sequence data.


![](../../../../../../../../Images/First_Sem_Images/Long%20Short-term%20Memory(LSTM).png)

---

## 🧠 **Key Components of LSTM:**

### 1. **Memory Elements**

* **Hidden state ($H_t$)** – Stores **short-term memory** (like a normal RNN).

* **Cell state ($C_t$)** – Stores **long-term memory**, allowing LSTM to preserve important information across many time steps.

---

## 🚪 **Gates in LSTM:**

LSTMs use **gates** to **control the flow of information**. Each gate is a neural layer with a sigmoid activation function $\sigma \in (0,1)$, which decides how much information to keep or discard.

### 🔸 **Forget Gate** $F_t$

* **Purpose**: Decides **what to forget** from the previous cell state.
* **Formula**:

  $$
  F_t = \sigma(x_t W_f + H_{t-1} U_f)
  $$

---

### 🔸 **Input Gate** $I_t$

* **Purpose**: Decides **what new information** to store.
* **Components**:

  * **Gate value**:

    $$
    I_t = \sigma(x_t W_i + H_{t-1} U_i)
    $$
  * **Candidate new content**:

    $$
    H'_t = \tanh(x_t W_c + H_{t-1} U_c)
    $$

---

### 🔸 **Output Gate** $O_t$

* **Purpose**: Decides **what part of the cell state becomes the hidden state**.
* **Formula**:

  $$
  O_t = \sigma(x_t W_o + H_{t-1} U_o)
  $$

---

## 🔄 **State Updates:**

### 📦 **Cell State Update**:

The **new cell state $C_t$** is calculated using a combination of:

* The **previous cell state** (scaled by forget gate)
* The **new candidate** (scaled by input gate):

$$
C_t = F_t \times C_{t-1} + I_t \times H'_t
$$

---

### ⚡ **Hidden State Update**:

The new **hidden state $H_t$** is obtained by:

* Applying **tanh** to the updated cell state
* Multiplying it with the output gate value:

$$
H_t = \tanh(C_t) \times O_t
$$

---

## 🧮 **Variables Summary:**

| Symbol     | Meaning                                |
| ---------- | -------------------------------------- |
| $x_t$      | Input at time step $t$                 |
| $H_t$      | Hidden state (short-term memory)       |
| $C_t$      | Cell state (long-term memory)          |
| $W_*, U_*$ | Weight matrices                        |
| $\times$   | Pointwise multiplication               |
| $+$        | Pointwise addition                     |
| $\sigma$   | Sigmoid activation function            |
| $\tanh$    | Hyperbolic tangent activation function |

---
