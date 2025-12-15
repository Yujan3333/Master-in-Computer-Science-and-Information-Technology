
## 🌻 What is Logistic Regression?
   
   * A **binary classification algorithm** (predicts 0 or 1).
   * Similar to linear regression but **uses a logistic (sigmoid) function** to convert outputs into **probabilities between 0 and 1**.
##### Figure of fitting the curve
![](../../../../../../../../Images/Second_Sem_Images/Logistic%20Regression-%20figure.png)
- Describing the curve here using the `sigmoid function` we change -$\infty$  to +$\infty$ to `0 to 1`.
- [Sigmoid Function](../../../../../../2-Second%20Semester/Machine%20Learning/1-Units/U2/Unit%202%20-%20Notes/Sigmoid%20Function.md) makes the `S-shape curve`


   ---
   
## 🌻 Logistic (Sigmoid) Function:
   
   $$
   \sigma(z) = \frac{1}{1 + e^{-z}}
   $$
   
   where:
   
   $$
   z = w_0 + w_1 x_1 + w_2 x_2 + \ldots + w_n x_n
   $$
   
   ✅ **If z → large +ve** → σ(z) → 1
   ✅ **If z → large -ve** → σ(z) → 0
   
   ---
   
## 🌻 Prediction Rule:
   
   * If **σ(z) > 0.5** ⇒ predict class **1** (positive)
   * If **σ(z) ≤ 0.5** ⇒ predict class **0** (negative)
   
   ---
   
## 🌻 Why not MSE (Mean Squared Error)?
   
   * Logistic regression’s output **σ(z) is non-linear**.
   * Using MSE leads to a **non-convex cost function with many local minima**, making **gradient descent unreliable**.
   
   ---
   
## 🌻 Logistic Regression Cost (Loss) Function:
   
   We use **Log-Loss (Cross-Entropy Loss):**
   
   For **one training example**:
   
   $$
   \text{Cost} = -y \log(\hat{y}) - (1 - y)\log(1 - \hat{y})
   $$
   
   where:
   
   * $y$ = actual label (0 or 1)
   * $\hat{y} = \sigma(z)$ = predicted probability
   
   ---
   
   ✅ If **y = 1**, cost is low if $\hat{y} \to 1$, cost high if $\hat{y} \to 0$.
   ✅ If **y = 0**, cost is low if $\hat{y} \to 0$, cost high if $\hat{y} \to 1$.
   
   **This forces the model to heavily penalize wrong confident predictions, which is good for learning.**
   
   ---
   
## 🌻 Total Cost Function:
   
   Over **m training examples**:
   
   $$
   J(w) = -\frac{1}{m} \sum_{i=1}^{m} \left[ y^{(i)} \log(\hat{y}^{(i)}) + (1 - y^{(i)}) \log(1 - \hat{y}^{(i)}) \right]
   $$
   
   ✅ This function is **convex** ⇒ gradient descent can find the **global minimum reliably**.
   
   ---
   
## 🌻 Gradient Descent in Logistic Regression:
   
   To **update weights:**
   
   $$
   w_j := w_j - \alpha \frac{\partial J(w)}{\partial w_j}
   $$
   
   The **gradient (partial derivative)**:
   
   $$
   \frac{\partial J(w)}{\partial w_j} = \frac{1}{m} \sum_{i=1}^{m} \left( \hat{y}^{(i)} - y^{(i)} \right) x_j^{(i)}
   $$
   
   ✅ Same structure as in linear regression, but **uses $\hat{y} = \sigma(z)$ instead of linear output.**
   
   ---
   
## 🌻 Numerical Example (if you want to practice):
   
   * Suppose:
   
     * $x_1 = 0.5, x_2 = 1$
     * $w_0 = 0.1, w_1 = 0.2, w_2 = -0.1$
   
   Then:
   
   $$
   z = 0.1 + 0.2 \times 0.5 - 0.1 \times 1 = 0.1 + 0.1 - 0.1 = 0.1
   $$
   
   $$
   \hat{y} = \frac{1}{1 + e^{-0.1}} \approx 0.525
   $$
   
   Since $\hat{y} > 0.5$, predict **class 1**.
   
   ---
   
   ## ✏️ Summary to memorize:
   
   ✅ **Uses sigmoid to map linear function into \[0, 1].**
   ✅ **Predicts 1 if output > 0.5, else 0.**
   ✅ **Uses log-loss as cost function for convexity.**
   ✅ **Gradient descent updates weights using difference between predicted prob and actual label.**
   
   ---
   
