A multilayer feedforward neural network consists of an input layer, one or more hidden layers, and an output layer.

 **Feedforward:**
- Data flows only in one direction — from the input layer to the output layer.

- There are no loops or cycles, unlike recurrent neural networks (RNNs).
---

The input signal propagates through the network in a forward direction, layer by layer—without any loops or cycles.

Such neural networks are known as **Multilayer Perceptron's (MLPs).**
###### Fig of Multilayer Feedforward NN
![](../../../../../../../../Images/First_Sem_Images/Multilayer%20Feedforward%20Network%20Fully%20Connected.png)

### 
---
### Non-linearities is important
If you remove all the nonlinear activation functions (i.e., use only linear functions like f(x)=x), no matter how many layers you add, the entire neural network becomes equivalent to a *single-layer linear model.*

Example:
If you stack multiple linear layers:
![](../../../../../../../../Images/First_Sem_Images/Multilayer%20Feedforward%20Network-1.png)

#### **This is just one big matrix multiplication — still linear.**

   So, without nonlinearity:
   
- MLPs *can't model XOR*
- MLPs *can’t learn complex patterns*
- They're no better than logistic regression or linear regression**

### 
---
### Signals in Multi-Layer Feedforward NN
##### Function Signals
- Input Signals
- Propagate in forward direction and produces the output signal in last phase
##### Error Signals
- Originates at Output Signals
- Propagates through each layer backward direction.
##### Figure Illustrating Signals
![](../../../../../../../../Images/First_Sem_Images/Multilayer%20Feedforward%20Network-signals.png)

### 
---
### Phases  Forward and Backward
#### Forward Pass (Prediction)
A neuron takes inputs ($x_1, x_2$), multiplies them by corresponding weights ($w_1, w_2$), adds a bias, and then applies an activation function (like ReLU) to produce an output.

**Example:**

$$\text{Output} = \text{ReLU}(w_1 x_1 + w_2 x_2 + \text{bias})$$

#### Backward Pass (Learning)
During the backward pass, the neuron receives an error signal. It then calculates how much each weight contributed to this error and updates the weights to minimize future errors. This process uses gradient descent.

**Example Weight Update:**

$$w_{\text{new}} = w_{\text{old}} - \text{Learning Rate} \times \frac{\partial \text{Error}}{\partial w}$$
#### Summary
* **Forward Pass:** Computes the output (prediction).
* **Backward Pass:** Adjusts weights (learning) based on the error.

