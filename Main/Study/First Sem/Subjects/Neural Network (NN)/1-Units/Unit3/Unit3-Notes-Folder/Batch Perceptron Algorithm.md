 Batch Perceptron Algorithm is a supervised learning algorithm used to train a perceptron for binary classification. It updates the model’s weights only after evaluating all training examples in one batch, using the total accumulated error from the entire dataset to adjust the weights.


> [!example]+ 📌 Simple Example 
 >  Imagine you have 10 emails to classify as spam or not spam:
 >  
 >      - Instead of updating the model after each email (like in online/stochastic perceptron),
 >  
 >      -  You check all 10, collect the total error,
 >  
 >      - Then adjust your model once.
 >  
 >  ✅ Key Points
 >  
 >      - Batch = all data at once before updating.
 >  
 >      - Used for linearly separable data.
 >  
 >      - Slower than online (stochastic) perceptron but smoother updates.
 

---
### Formula
 ![](../../../../../../../../Images/First_Sem_Images/Batch%20Perceptron%20Algorithm.png)

#### Why the Gradient is Negated in Optimization?
> [!info]- Gradient is negated Becase: 
> > The gradient is a fundamental concept in optimization, especially in machine learning algorithms like gradient descent. The reason we negate the gradient in the weight update rule boils down to our objective: minimizing the cost function.
>   
>   #### Gradient Points Uphill
>   
>   The gradient vector, denoted as ∇J(w), always points in the direction of the steepest ascent of the cost function J(w). Imagine you're on a mountain and want to reach the peak; the gradient tells you which way to go to climb fastest.
>   
>   #### Moving Downhill for Minimization
>   
>   However, our goal in most machine learning models is to minimize the cost function. This means we want to descend the "mountain" to find the lowest point, not climb to the peak. To achieve this, we must move in the opposite direction of the steepest ascent.
>   The Weight Update Rule
>   
>   This opposing direction is precisely why the weight update rule includes a negative sign:
>   
>   w(n+1)=w(n)−α∇J(w)
>   
>   Here's what each part signifies:
>    >    w(n+1): The new (updated) weight vector.
>    >    w(n): The current weight vector.
>    >    α: The learning rate, a small positive scalar that controls the size of the step we take in the direction of descent.
>   
>   ∇J(w): The gradient of the cost function with respect to the weights.
>   
>   The negative sign ensures that each update to the weight vector w moves it in the direction that reduces the cost function J(w).
>   
>   #### Intuition Behind the Negation
>   
>   Consider a simple scenario with a single weight w:
>   
>   - If **the gradient ∇J(w) is positive:** This means increasing w would cause J(w) to increase (moving uphill). To decrease J(w), we need to decrease w. The negative sign in the update rule (−α∇J(w)) achieves this.
>   
>   - I**f the gradient ∇J(w) is negative:** This means increasing w would cause J(w) to decrease (moving downhill). To decrease J(w), we need to increase w. The negative sign in the update rule, combined with the negative gradient, results in a positive update to w, thus increasing it.

---
### Numerical Given By Sir
> ![](../../../../../../../../Images/First_Sem_Images/Batch%20Perceptron%20Algorithm-1.png)

> [!example]+ Solution
>   
>   ## Batch Perceptron Algorithm Training Walkthrough (Corrected)
>   
>   This walkthrough demonstrates the training of a Batch Perceptron algorithm, including a step-by-step correction of the weight update calculation and a clear conclusion about its convergence.
>   
>   ---
>   
>   ### 🧠 Formulas Used
>   
>   Before applying updates, let's recall the formulas:
>   
>   * **Prediction:**
>       $$y = \text{sign}(w \cdot x + b)$$
>   * **Batch weight update:**
>       $$\Delta w = \alpha \sum_{x_i \in M} t_i x_i$$
>   * **Batch bias update:**
>       $$\Delta b = \alpha \sum_{x_i \in M} t_i$$
>   
>   Where:
>   * $M$ is the set of **misclassified samples**.
>   * $t_i \in \{-1, +1\}$ is the **true label**.
>   * $\alpha$ is the **learning rate**.
>   
>   ---
>   
>   ### ✅ Step-by-Step Training (Corrected)
>   
>   #### Step 1: Initialize
>   
>   We start with the following initial parameters:
>   * **Weights:** $w = [0, 0]$
>   * **Bias:** $b = 0$
>   * **Learning Rate:** $\alpha = 1$
>   
>   ---
>   
>   #### Step 2: Epoch 1
>   
>   Let's process the first epoch with the initial parameters $w = [0, 0]$ and $b = 0$.
>   
>   | Input   | Target ($t$) | Output ($y = \text{sign}(w \cdot x + b)$) | Correct? |
>   | :------ | :----------- | :------------------------------------------ | :------- |
>   | $[1, 1]$  | $+1$         | $\text{sign}(0 \cdot [1,1] + 0) = \text{sign}(0) = +1$ | ✅       |
>   | $[1, -1]$ | $-1$         | $\text{sign}(0 \cdot [1,-1] + 0) = \text{sign}(0) = +1$ | ❌       |
>   | $[-1, 1]$ | $-1$         | $\text{sign}(0 \cdot [-1,1] + 0) = \text{sign}(0) = +1$ | ❌       |
>   | $[-1, -1]$| $-1$         | $\text{sign}(0 \cdot [-1,-1] + 0) = \text{sign}(0) = +1$ | ❌       |
>   
>   The **misclassified samples ($M$)** are:
>   $\{ [1, -1], [-1, 1], [-1, -1] \}$, where the true target $t = -1$ for all of them.
>   
>   ---
>   
>   ##### 🔸 Using the Update Formula:
>   
>   Let's calculate the weight and bias updates:
>   
>   * **Weight update ($\Delta w$):**
>       $$\Delta w = \alpha \sum t_i x_i = 1 \cdot [(-1)[1, -1] + (-1)[-1, 1] + (-1)[-1, -1]]$$
>       Step-by-step calculation:
>       $$\Delta w = [-1, 1] + [1, -1] + [1, 1] = [1, 1]$$
>       ✅ **Correct $\Delta w = [1, 1]$** (Note: Previous calculation was $[3, -1]$, which was incorrect.)
>   
>   * **Bias update ($\Delta b$):**
>       $$\Delta b = \alpha \sum t_i = 1 \cdot (-1 + -1 + -1) = -3$$
>       ✅ **Correct $\Delta b = -3$**
>   
>   ---
>   
>   ##### Updated parameters after Epoch 1:
>   
>   * **New weights ($w$):**
>       $$w = [0, 0] + [1, 1] = [1, 1]$$
>   * **New bias ($b$):**
>       $$b = 0 - 3 = -3$$
>   
>   ---
>   
>   #### Epoch 2
>   
>   Now, we use the updated parameters $w = [1, 1]$ and $b = -3$.
>   
>   | Input   | Target ($t$) | $v = w \cdot x + b$               | Output ($y = \text{sign}(v)$) | Correct? |
>   | :------ | :----------- | :---------------------------------- | :----------------------------- | :------- |
>   | $[1, 1]$  | $+1$         | $(1 \cdot 1) + (1 \cdot 1) - 3 = -1$ | $-1$                           | ❌       |
>   | $[1, -1]$ | $-1$         | $(1 \cdot 1) + (1 \cdot -1) - 3 = -3$ | $-1$                           | ✅       |
>   | $[-1, 1]$ | $-1$         | $(1 \cdot -1) + (1 \cdot 1) - 3 = -3$ | $-1$                           | ✅       |
>   | $[-1, -1]$| $-1$         | $(1 \cdot -1) + (1 \cdot -1) - 3 = -5$ | $-1$                           | ✅       |
>   
>   Only one sample was misclassified: $[1, 1]$, with a true target $t = +1$.
>   
>   ---
>   
>   ##### Update after Epoch 2:
>   
>   * **Weight update ($\Delta w$):**
>       $$\Delta w = 1 \cdot (1 \cdot [1, 1]) = [1, 1]$$
>   * **Bias update ($\Delta b$):**
>       $$\Delta b = 1 \cdot 1 = 1$$
>   
>   ---
>   
>   ##### Updated parameters after Epoch 2:
>   
>   * **New weights ($w$):**
>       $$w = [1, 1] + [1, 1] = [2, 2]$$
>   * **New bias ($b$):**
>       $$b = -3 + 1 = -2$$
>   
>   ---
>   
>   #### Epoch 3
>   
>   Now, we use the updated parameters $w = [2, 2]$ and $b = -2$.
>   
>   | Input   | Target ($t$) | $v = w \cdot x + b$                | Output ($y = \text{sign}(v)$) | Correct? |
>   | :------ | :----------- | :----------------------------------- | :----------------------------- | :------- |
>   | $[1, 1]$  | $+1$         | $(2 \cdot 1) + (2 \cdot 1) - 2 = 2$  | $+1$                           | ✅       |
>   | $[1, -1]$ | $-1$         | $(2 \cdot 1) + (2 \cdot -1) - 2 = -2$ | $-1$                           | ✅       |
>   | $[-1, 1]$ | $-1$         | $(2 \cdot -1) + (2 \cdot 1) - 2 = -2$ | $-1$                           | ✅       |
>   | $[-1, -1]$| $-1$         | $(2 \cdot -1) + (2 \cdot -1) - 2 = -6$ | $-1$                           | ✅       |
>   
>   ✅ **No misclassifications** in Epoch 3! This means the training is complete as the perceptron has converged.
>   
>   ---
>   
>   ### ✅ Final Model Parameters:
>   
>   * **Weights:** $[2, 2]$
>   * **Bias:** $-2$
>   
>   ---
>   
>   ### Decision Boundary:
>   
>   The decision boundary for this perceptron is given by $w \cdot x + b = 0$:
>   $$2x_1 + 2x_2 - 2 = 0 \implies x_1 + x_2 = 1$$
>   
>   ---
>   
>   ### ❌ Fixing the XOR Conclusion:
>   
>   Previous versions might have incorrectly stated that this dataset is "like XOR" or that the perceptron "fails" to converge.
>   
>   ✔️ The dataset used in this example (specifically, the input points $[1,1]$, $[1,-1]$, $[-1,1]$, $[-1,-1]$ with targets $+1,-1,-1,-1$ respectively) **is linearly separable**. Therefore, the Perceptron algorithm correctly converges and finds a perfect decision boundary. It does not exhibit the characteristics of an XOR problem, which is famously non-linearly separable.
>   
>   ---
>   
>   ### ✅ Final Summary
>   
>   | Aspect           | Your Version (Initial) | Correction                 |
>   | :--------------- | :--------------------- | :------------------------- |
>   | $\Delta w$ in Epoch 1 | $[3, -1]$              | ✅ Should be $[1, 1]$      |
>   | Dataset Type     | Said "like XOR"        | ❌ It's not XOR            |
>   | Convergence      | Said "Fails"           | ✅ Actually converges      |
>   
>   ---
>   
