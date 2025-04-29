## 🏗️ What is an RBF Network?
It’s a neural network with:
1. **Input layer** — passes the data
2. **Hidden layer** — uses **RBFs** (like Gaussian curves) as **activation functions**
3. **Output layer** — combines those RBF outputs (like a weighted sum)
### So, it is called an:
> **"RBF Basis Function Network"**  
> because it uses **RBFs as basis functions** in the network to model complex data.

---
**Radial basis function (RBF)** networks are artificial neural networks that typically have three layers: an input layer, a hidden layer with a non-linear RBF activation function and a linear output layer.

---
### Overview Info
#### 1. **Input Layer:**
This layer simply passes the input features (like height, weight, pixel values, etc.) to the next layer. There’s no computation here — just passing values forward.
#### 2. **Hidden Layer (with RBF units):**
This is where the real “magic” happens. Each hidden neuron computes how _close_ the input is to a specific center point (called a "prototype" or "centroid") using a **radial basis function**, usually a Gaussian function:

$$
K(x, y) = \exp\left(-\frac{\|x - y\|^2}{2\sigma^2}\right)
$$

Where,
$\sigma$ is a free parameter

 ==[Gaussian Kernel-More Info](U4-Notes/Gaussian%20Kernel.md)==

So instead of learning a complex weight like in normal neural networks, each neuron responds **strongly when the input is close to its center**.

#### 3. **Output Layer:**
This is a simple linear layer. It takes the output from the hidden layer and combines them (weighted sum) to give the final prediction — like classifying a digit, detecting an object, or predicting a value.

---
###  Sir Slides - Same Overview Info
#### Input Layer
This layer consists of **m0 source nodes**, where m0 is the *dimensionality* of the input vector x.
#### Hidden Layer
This layer consists of the **K computation units (K≤N)**, where *N is number training samples.* Each hidden unit is  equipped with a radial basis activation function.

==Note==
[Why (K≤N)?](Why%20K%20less%20then%20or%20equal%20to%20N.md)
#### Output Layer
This layer of neural network contains *one or more nodes* depending upon the need.
###### Visually
![](../../../../../../../Images/RBF%20Basis%20Function%20Network.png)

---
### RBF Continued

- RBF networks are typically trained from *pairs of input and target values by a two-step algorithm.*
	- Firstly gives like this
		`Input:  [0.2, 0.8, 0.5]   →   Target: "Politics"`
		`Input:  [0.9, 0.1, 0.3]   →   Target: "Sports"`
	- Input with their output to learn from the below 2 steps

- In the first step, the *center vectors*  of the RBF functions in the hidden layer are chosen. This step can be performed in several ways; centers can be *randomly sampled* from some set of examples, or they can be determined using *K-means clustering*.

- The second step simply fits a model with coefficients  to the hidden layer's outputs with respect to some objective function.

#### 2 step algorithm
✅ **Step 1: Choose the center vectors for RBFs**
These are the centers of the radial basis functions (like Gaussians) in the **hidden layer**.  
Each RBF neuron checks _how close_ the input is to its center.

There are a few ways to pick these centers:

1. **Random sampling from training data**
    
    - Just pick K random samples from your data.
        
    - Simple but may not be optimal.
        
2. **K-Means Clustering (better option)**
    
    - Run K-means on the input data to find **K cluster centers**.
        
    - Each RBF neuron then uses one cluster center as its center.
        
    - This way, your neurons represent **different “regions” of your data** nicely.
        

🔍 Why do this?  
→ So the RBF neurons can each "specialize" in recognizing patterns near their own center.
### ✅ **Step 2: Fit the output weights (w₁, w₂, ..., wₖ)**

Once the centers are fixed and your hidden neurons are set:

1. Each input vector is passed through the hidden layer → gives **K activations** (how close it is to each center).
    
2. The output layer is **just a linear model**:
   $y = w_1 \cdot \varphi_1(x) + w_2 \cdot \varphi_2(x) + \cdots + w_K \cdot \varphi_K(x)$
	
3. Now, you just need to **learn the weights www** so that the output **matches the target** as closely as possible.
    
This is done using **linear regression**, **least squares**, or any optimization technique based on an **objective function** (like Mean Squared Error).
#### Summary

|Step|What Happens|Goal|
|---|---|---|
|**1**|Choose centers for the RBF neurons|Spread neurons across the data|
|**2**|Learn weights from hidden layer to output|Make correct predictions|
