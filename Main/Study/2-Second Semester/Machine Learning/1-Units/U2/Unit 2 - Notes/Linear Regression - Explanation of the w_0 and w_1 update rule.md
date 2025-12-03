
# ⭐ Understanding $w_1$ Update in Linear Regression (Gradient Descent)



We start with the formula:



$$

w_1 = w_1 + \alpha \frac{1}{n} \sum_{i=1}^{n} (y^i - w_0 - w_1 x^i) x^i

$$



---



## 1️⃣ Goal



We want to find the line:



$$

y = w_0 + w_1 x

$$



that **best fits the data** by minimizing the mean squared error (MSE):



$$

E = \frac{1}{2n} \sum_{i=1}^{n} \left( y^i - (w_0 + w_1 x^i) \right)^2

$$



---



## 2️⃣ Gradient Descent Idea



Gradient descent formula:



$$

\text{new parameter} = \text{old parameter} - \alpha \frac{\partial E}{\partial \text{parameter}}

$$



For $w_1$:



$$

w_1 = w_1 - \alpha \frac{\partial E}{\partial w_1}

$$



---



## 3️⃣ Compute derivative w.r.t $w_1$



$$

\frac{\partial E}{\partial w_1} = \frac{\partial}{\partial w_1} \frac{1}{2n} \sum_{i=1}^{n} \left( y^i - w_0 - w_1 x^i \right)^2

$$



Derivative of $\left(y^i - w_0 - w_1 x^i\right)^2$ w.r.t $w_1$ is:



$$

-2 (y^i - w_0 - w_1 x^i) x^i

$$



Divide by $2n$ from MSE:



$$

\frac{\partial E}{\partial w_1} = - \frac{1}{n} \sum_{i=1}^{n} (y^i - w_0 - w_1 x^i) x^i

$$



---



## 4️⃣ Plug into Gradient Descent



$$

w_1 = w_1 - \alpha \frac{\partial E}{\partial w_1}

$$



Substitute derivative:



$$

w_1 = w_1 - \alpha \Big( - \frac{1}{n} \sum_{i=1}^{n} (y^i - w_0 - w_1 x^i) x^i \Big)

$$



$$

{w_1 = w_1 + \alpha \frac{1}{n} \sum_{i=1}^{n} (y^i - w_0 - w_1 x^i) x^i}

$$


---

