### RNN have a “memory” which remembers all information about what has been calculated. It uses the same parameters for each input as it performs the same task on all the inputs or hidden states to produce the output. 

---
### 🧠 Think of RNN as a student reading a paragraph word by word:
- The student **remembers** what they’ve read before (memory).
    
- Each new word is understood based on what came before.
    
- The student **uses the same brain** (same thinking process) for each word — not a new brain every time!
    

---

### 🔁 What does "same set of weights" mean?
In RNNs:
- The **"weights"** are the rules the RNN uses to understand input and update memory.
    
- For **every word or input in a sequence**, RNN **uses the same rules** (same weights) again and again.
    
- This repetition helps the RNN **learn patterns** over time.
    

---
### 🔗 Why is this important?
Because of the shared weights:
- The model can **connect earlier inputs with later ones**.
    
- It can **remember past information** and **relate it to current input**, which is useful in tasks like predicting the next word in a sentence.
    

---
### ✅ Super Simple Summary:
> RNNs use the same set of rules (weights) for each input, so they can remember past steps and relate them to current ones while processing a sequence.

---