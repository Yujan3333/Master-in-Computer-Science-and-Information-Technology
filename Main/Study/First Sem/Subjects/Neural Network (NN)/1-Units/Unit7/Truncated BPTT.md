### 🧠 **Truncated Backpropagation Through Time (TBPTT)**

**Truncated BPTT** (TBPTT) is a practical **optimization of Backpropagation Through Time (BPTT)** used for training Recurrent Neural Networks (RNNs) on long sequences. It helps **reduce memory and computational cost**.

---

## 🔄 Why Truncate BPTT?

In full BPTT:

* The RNN is **unrolled through all time steps**.
* Gradients are backpropagated through **entire sequences**.
* This becomes **very expensive** and **memory-heavy**, especially for long sequences.

---

## 🧩 TBPTT: The Core Idea

Instead of unrolling the RNN over the **entire sequence**, TBPTT unrolls it over **smaller chunks** of length $M$.

### 🔧 How It Works:

Let’s say the sequence is of length $T$, and truncation window is $M$:

1. Process sequence in chunks:

   * Step 1–M
   * Step M+1–2M
   * Step 2M+1–3M
   * ...

2. At each chunk:

   * **Forward pass**: from step $t$ to $t+M$
   * **Backward pass**: compute gradients only through this window

3. **Hidden state $h_t$ is preserved** across chunks — so **temporal dependencies are still maintained** (just not learned via full-length gradient).

---

## ✅ Benefits

* **Faster training**: Fewer time steps to backpropagate through.
* **Lower memory use**: Only store activations for $M$ steps.
* **Useful for online / streaming data**: Can process sequences chunk by chunk.

---

## ⚠️ Limitations

* May **miss long-term dependencies** (beyond window $M$).
* Choosing the right **window size $M$** is important:

  * Too small → weak learning of context
  * Too large → defeats the purpose

---

## 🧠 Summary

| Feature                     | TBPTT                                                     |
| --------------------------- | --------------------------------------------------------- |
| Purpose                     | Speed up training and reduce memory                       |
| Method                      | Backpropagate only through fixed number $M$ of time steps |
| Maintains sequence info?    | ✅ Yes (via hidden state)                                  |
| Captures long dependencies? | ❌ Only within window $M$                                  |
| Typical use cases           | Long sequences, online learning, streaming input          |

