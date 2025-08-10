### What is BiLSTM?

**BiLSTM** stands for **Bidirectional Long Short-Term Memory**, a type of deep learning model used for **sequence data** like text.

---

### Breakdown:

* **LSTM (Long Short-Term Memory)** is a special kind of **Recurrent Neural Network (RNN)** designed to remember information over long sequences and avoid problems like vanishing gradients.
* **Bidirectional** means the model processes the input **in both directions**:

  * Forward (left to right)
  * Backward (right to left)

This lets the model capture **context from both past and future words**, which improves understanding—especially useful in **sentiment analysis**, where meaning depends on word order and context.

---

### Example:

In the sentence:
**“The service was not good.”**
A regular LSTM might miss how "not" affects "good", but a **BiLSTM** sees both before and after words, helping it understand that the sentiment is **negative**.
