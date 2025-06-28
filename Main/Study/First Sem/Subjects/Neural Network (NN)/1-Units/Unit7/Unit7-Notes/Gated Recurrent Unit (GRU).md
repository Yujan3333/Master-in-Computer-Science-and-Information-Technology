
### 🔁 **GRU (Gated Recurrent Unit) Summary**

**GRU** is a simplified variant of RNNs, designed to solve the **vanishing gradient problem** like LSTMs, but with a **simpler architecture** and **faster training**.

![](../../../../../../../../Images/First_Sem_Images/Gated%20Recurrent%20Unit%20(GRU).png)


---

### 🧠 **Key Features:**

* ✅ **No separate cell state** – Only maintains a **hidden state**, reducing complexity.
* ✅ **Two gates** control memory flow:

  1. **Reset Gate (𝑅ₜ)** – Controls how much past information is **forgotten** (short-term memory).

     * Formula:

       $$
       R_t = \sigma(x_t W_r + H_{t-1} V_r)
       $$
  2. **Update Gate (𝑈ₜ)** – Controls how much past information is **retained** (long-term memory).

     * Formula:

       $$
       U_t = \sigma(x_t W_u + H_{t-1} V_u)
       $$

---

### 🔄 **Hidden State Calculation:**

* **Candidate hidden state**:

  $$
  H'_t = \tanh(x_t W_h + V_h(R_t \times H_{t-1}))
  $$
* **Final hidden state**:

  $$
  H_t = (U_t \times H'_t) + (1 - U_t) \times H_{t-1}
  $$

Where:

* $x_t$ = input at time $t$
* $H_{t-1}$ = previous hidden state
* $W$, $V$ = weight matrices
* $\times$ = element-wise multiplication

---

### ✅ **Advantages of GRU:**

* Simpler and faster than LSTM
* Similar performance to LSTM in many tasks
* Efficient for sequence data like time series, language, and speech processing

---

