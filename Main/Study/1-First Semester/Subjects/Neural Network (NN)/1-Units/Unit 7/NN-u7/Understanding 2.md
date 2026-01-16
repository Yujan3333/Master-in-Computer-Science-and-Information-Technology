### 🧠 Original:
> **"RNN converts the independent activations into dependent activations by providing the same weights and biases to all the layers..."**

### ✅ What it means:
In a normal neural network (like a feedforward network), each input is handled **independently**. There’s no link between previous and current inputs.

But in an RNN:

- Each step depends on the **previous step’s output**.
    
- This creates **dependent activations** (output depends on past inputs).
    
- RNN does this by using the **same weights and biases** at every step, which helps it learn **patterns over time** instead of treating each input separately.
    

---
### 🧠 Original:
> **"...thus reducing the complexity of increasing parameters..."**

### ✅ What it means:
If a network used **new weights and biases for every time step**, the number of parameters would grow a lot.

But RNN uses the **same weights and biases** for all time steps, which:

- Keeps the model simple
    
- Uses **fewer parameters**
    
- Makes training more efficient
    

---
### 🧠 Original:
> **"...and memorizing each previous output by giving each output as input to the next hidden layer."**

### ✅ What it means:
The **output from one time step** is **fed as input** to the next time step (via the hidden state). This is how the RNN **remembers** past information.

So, each time step has:

- The current input
    
- The previous hidden state (which holds past information)
    

Together, this helps the RNN build memory.

---
### 🧠 Original:
> **"Hence layers of neural network in right side can be joined together such that the weights and bias of all the hidden layers is the same, into a single recurrent layer."**

### ✅ What it means:
In diagrams (like the one you’ll see on the next slide), RNNs are often "unfolded" to show each time step.

But actually:

- All these time steps **share the same layer** with **shared weights and biases**.
    
- So, instead of thinking of them as many layers, you can think of it as **one recurrent layer** applied multiple times — once for each time step.
    
![](../../../../../../../../Images/First_Sem_Images/Fig%20RNN.png)

---

### 🔁 Final Simple Explanation You Can Use:

> In RNN, each output depends on the previous one. It uses the **same weights and biases** at every step, which reduces complexity and allows the network to **remember past outputs** by feeding them into the next step. This repeated structure is called a **recurrent layer**, and it helps turn independent inputs into a connected sequence.

---

