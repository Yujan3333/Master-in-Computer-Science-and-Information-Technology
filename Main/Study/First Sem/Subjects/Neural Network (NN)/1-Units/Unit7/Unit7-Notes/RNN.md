### 📚Definition
**RNN** stands for **Recurrent Neural Network**. It is a type of **artificial neural network** designed to recognize patterns in **sequential data**, such as:

- Text
    
- Time series
    
- Speech
    
- Music
    
- Video frames

---
### 🧠 Key Idea:
Unlike traditional neural networks (like feedforward networks), **RNNs have memory**. They **"remember"** information from previous steps in the sequence by passing a hidden state from one time step to the next.

In **traditional neural networks**, all the inputs and outputs are *independent of each other*, but in cases like when it is required to predict the next word of a sentence, the previous words are required and hence there is a need to remember the previous words.

---
### ⚠️ Limitation:
RNNs have trouble learning **long-term dependencies** due to issues like the **vanishing gradient problem**.

---
### 🛠️ Solutions:
- **LSTM (Long Short-Term Memory)**: A type of RNN designed to handle long-term dependencies.
    
- **GRU (Gated Recurrent Unit)**: A simpler variant of LSTM.
    
- **Transformers**: Modern architectures that often outperform RNNs for many tasks, especially in NLP.
---
### Figure Of RNN
![](../../../../../../../../Images/First_Sem_Images/Fig%20RNN.png)
> [Understanding the RNN Figure and formula](Understanding%20the%20RNN%20Figure%20and%20formula.md)




---
### [From Sir Slide](From%20Sir%20Slide.md)
Understanding the slides content through AI answers

---
### Numerical
- Example: Consider the word ‘dogs’. Show forward propagation of RNN with three nodes in hidden layer to predict letter ‘s’ given the letters ‘d’, ‘o’, and ‘g’. Assume that hidden layer activation function is **Tanh** and activation in output layer is **softmax**. 

