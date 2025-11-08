**Gradient Descent** is an optimization algorithm used to minimize a **cost (or loss) function** in machine learning and deep learning. 

It helps models learn by adjusting their parameters (like weights in neural networks) to reduce the error between the predicted and actual outputs.

### 🔧 Intuition
Imagine you're at the top of a hill (high error), and your goal is to reach the bottom of a valley (lowest error). 
 
 You take steps in the direction of the steepest descent — this direction is given by the **negative gradient** of the function.
###### Example 
![](../../../../../../../../Images/First_Sem_Images/Gradient%20Descent.png)
###### Direction of the descent depends on the slope / Derivative / Gradient / m
![](../../../../../../../../Images/First_Sem_Images/Gradient%20Descent%20a.png)


###### Gradient Descent Parameter change is gradual
![](../../../../../../../../Images/First_Sem_Images/Gradient%20Descent-%20formula.png)

### 📦 Types of Gradient Descent
1. **Batch Gradient Descent**: Uses the entire dataset to compute the gradient.
    
2. **Stochastic Gradient Descent (SGD)**: Uses one data point at a time — faster but more noisy.
    
3. **Mini-Batch Gradient Descent**: Uses small batches — balance between speed and accuracy.


### ⚠️ Key Concepts
- **Learning rate α**: Too small → slow learning; too large → might overshoot or diverge.
    
- **Convergence**: When changes in the cost function are minimal.
    
- **Local minima vs global minima**: In complex models, gradient descent might get stuck in a local minimum instead of the best (global) one.


### 🧠 Why It's Important
Gradient descent is the backbone of how machine learning models **learn from data**. It's used in:

- Linear regression
    
- Logistic regression
    
- Neural networks
    
- Many other ML algorithms


---
## [MORE on Gradient Descent and different learning rate](MORE%20on%20Gradient%20Descent%20and%20different%20learning%20rate.md)
