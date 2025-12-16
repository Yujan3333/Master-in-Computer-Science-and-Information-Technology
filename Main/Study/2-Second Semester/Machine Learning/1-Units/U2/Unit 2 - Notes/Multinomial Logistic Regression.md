
* An extension of **binary logistic regression** for **multi-class classification** ($K > 2$ classes).
* Predicts probabilities for **each class** instead of just two.

---
## **Multinomial Logistic Regression (MLR) – Step by Step**

### **1. Model Output**

In MLR, the goal is to predict probabilities for multiple classes ($k$ classes).

We first compute the **linear combination of inputs**:

$$
y = w_0 + w_1 x^{(1)} + w_2 x^{(2)} + \dots + w_n x^{(n)}
$$

* Example: If there are 3 input features ($x^{(1)}, x^{(2)}, x^{(3)}$), then

$$
y = w_0 + w_1 x^{(1)} + w_2 x^{(2)} + w_3 x^{(3)}
$$

Here $w_0$ is the bias, and $w_1, w_2, w_3$ are coefficients for the features.

**Unlike linear regression**, in MLR we need probabilities for each class. So we use the **softmax function**:

$$
\hat{y}^{(i)} = \sigma(y^{(i)}) = \frac{e^{y^{(i)}}}{\sum_{j=1}^k e^{y^{(j)}}}
$$

* $\hat{y}^{(i)}$ = predicted probability for class $i$
* $k$ = total number of classes
* Softmax ensures that all predicted probabilities sum to 1.

---

### **2. Loss Function**

We use **Categorical Cross-Entropy Loss**:

$$
L(y, \hat{y}) = - \sum_{i=1}^k y^{(i)} \log(\hat{y}^{(i)})
$$

* $y^{(i)}$ = true probability for class $i$ (usually **one-hot encoded**)
* $\hat{y}^{(i)}$ = predicted probability for class $i$

**Intuition:**

* The loss is small when predicted probability for the true class is high.
* The loss is large when predicted probability for the true class is low.

---

### **3. Gradient of Softmax and Loss**

To update weights, we need the **derivative of the loss w.r.t. the linear combination $y^{(i)}$**:

1. For softmax derivative:

   * When $j = i$ (same class):
     $$
     \frac{\partial \hat{y}^{(i)}}{\partial y^{(i)}} = \hat{y}^{(i)} (1 - \hat{y}^{(i)})
     $$
   * When $j \ne i$ (different class):
     $$
     \frac{\partial \hat{y}^{(i)}}{\partial y^{(j)}} = - \hat{y}^{(i)} \hat{y}^{(j)}
     $$

2. For loss derivative w.r.t. $y^{(i)}$:
   $$
   \frac{\partial L(\hat{y}^{(i)}, y^{(i)})}{\partial y^{(i)}} = \hat{y}^{(i)} - y^{(i)}
   $$

**Intuition:**

* The derivative is **positive** if the predicted probability is higher than the true label (we need to decrease it).
* The derivative is **negative** if the predicted probability is lower than the true label (we need to increase it).

---

### **4. Weight Update Rule**

Using **gradient descent**, we update the weights:

$$
w_j = w_j - \alpha \frac{\partial L}{\partial w_j}
$$

Where:

* $\alpha$ = learning rate
* Gradient w.r.t weights:

$$
\frac{\partial L}{\partial w_0} = \hat{y}^{(i)} - y^{(i)}
$$

$$
\frac{\partial L}{\partial w_1} = (\hat{y}^{(i)} - y^{(i)}) x^{(1)}
$$

$$
\frac{\partial L}{\partial w_2} = (\hat{y}^{(i)} - y^{(i)}) x^{(2)}
$$

$$
\frac{\partial L}{\partial w_3} = (\hat{y}^{(i)} - y^{(i)}) x^{(3)}
$$

So the **update rules** are:

$$
w_0 = w_0 - \alpha (\hat{y}^{(i)} - y^{(i)})
$$

$$
w_1 = w_1 - \alpha (\hat{y}^{(i)} - y^{(i)}) x^{(1)}
$$

$$
w_2 = w_2 - \alpha (\hat{y}^{(i)} - y^{(i)}) x^{(2)}
$$

$$
w_3 = w_3 - \alpha (\hat{y}^{(i)} - y^{(i)}) x^{(3)}
$$

**Intuition:**

* Each weight is updated proportional to **error times the input feature**.
* If prediction is too high, weight decreases; if too low, weight increases.

---

### ✅ **Summary Flow**

1. Compute linear combination: $y = w_0 + w_1 x_1 + \dots + w_n x_n$
2. Apply softmax: $\hat{y} = \sigma(y)$ → probability vector
3. Compute loss: $L(y, \hat{y}) = - \sum y \log(\hat{y})$
4. Compute gradient: $\frac{\partial L}{\partial w_j} = (\hat{y}^{(i)} - y^{(i)}) x^{(j)}$
5. Update weights: $w_j = w_j - \alpha \frac{\partial L}{\partial w_j}$
6. Repeat until convergence (gradient descent or batch updates)

---
