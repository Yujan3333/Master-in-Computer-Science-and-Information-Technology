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
 ![](../../../../../../../Attachments/Batch%20Perceptron%20Algorithm.png)

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


