If the training data is **linearly separable**, the **Perceptron Learning Rule** will:

- Converge to a correct solution
    
- Do so in a **finite number of steps**
    
- Work properly if the **learning rate is small**

#### Convergence Guarantee
- The learning rule will find a weight vector that **correctly classifies all training examples**, given linear separability.

#### Perceptron Learning Rule

![](../../../../../../../../Images/First_Sem_Images/Perceptron%20Convergence%20Theorem%20-%20another%20equivalent%20perceptron.png)

**$$
v = \sum_{i=1}^{m} w_i x_i + b
$$

Input vector: $x = [x_0, x_1, \dots, x_m]$

Weight vector: $w = [w_0, w_1, \dots, w_m]$

**At iteration $n$:**
- Input: $x(n) = [x_0(n), x_1(n), \dots, x_m(n)]$
- Weights: $w(n) = [w_0(n), w_1(n), \dots, w_m(n)]$

- **Equation for the Perceptron Output:**
    - The perceptron computes an output using this formula:
		
        $v = w^T x$
        
        - This just means:  
	        → Multiply each input value by its corresponding weight  
	        → Then **add them all up**
	        → [Why is the transpose of W needed?](Why%20is%20the%20transpose%20of%20W%20needed.md)
        
- **Input and Weight Vectors at Step n:**
    - At a specific training step $n$, the input and weight vectors are:
        
        - $x(n) = [x_0(n), x_1(n), \dots, x_m(n)]$ 
        - $w(n) = [w_0(n), w_1(n), \dots, w_m(n)]$ 
        
        - Where:
         $x_i(n)$ is the value of input $i$ at step $n$. 
         
         $w_i(n)$ is the value of weight $i$ at step $n$.
            
- **Equation at Step n:**
    - At step $n$, the perceptron computes: 
    
    - $v = w(n)^T x(n)$
        
    - Which again means:  
        → Multiply each input by its weight at that moment  
        → Add them all up to get the result $v$
        
- **Two-Class Classification:**
    - The perceptron is being trained to recognize **two types of inputs**, called **Class 1 (C1)** and **Class 2 (C2)**.
        
    - The **training data** must have **enough examples from both classes** so the perceptron can learn the correct pattern.

##### Two target classes:
$C_1$ and $C_2$.

Training sets:
$H_1 \in C_1$
$H_2 \in C_2$
Full training set: $H = H_1 \cup H_2$

##### Classification Rule:
If output $w^T x > 0$: input is in class $C_1$
If $w^T x \leq 0$: input is in class $C_2$

---
### Weight Update Rule at Step $n$
![](../../../../../../Images/Perceptron%20Convergence%20Theorem-%20weight%20update%20rule.png)
The Perceptron Learning Rule updates a perceptron's weights based on classification errors.

–Do not change weights in case of correct classification

–Increase weights when perceptron output is smaller than actual target

–Decrease weights when perceptron output is larger than actual target

This is **mathematically represented** as: 
$w(n+1)=w(n)+α \text{ } x(n)(t(n)−y(n))$, 

where,
- w is weights, 
- α is the learning rate, 
- x is the input, 
- t is the target output,
- y is the perceptron's output. 

The weights are adjusted proportionally to the input and the error, to move towards correct classification.