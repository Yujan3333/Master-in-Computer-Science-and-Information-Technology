
## ✍️ **Polynomial Curve Fitting — Made Simple**

### 🔹 **What is it?**

Polynomial regression fits a curve (not just a straight line) to your data.

Instead of:

$$
y = w_0 + w_1 x
$$

You use a **polynomial**:

$$
y = w_0 + w_1 x + w_2 x^2 + \cdots + w_m x^m
$$

👉 Here, you **choose the degree** $m$, and then find the best coefficients $w_0, w_1, \dots, w_m$.

---

## 🧮 **Error Function (Cost Function)**

Let’s say we have $n$ data points:

$$
(x_1, y_1), (x_2, y_2), \dots, (x_n, y_n)
$$

The predicted value is:

$$
\hat{y}_i = w_0 + w_1 x_i + w_2 x_i^2 + \cdots + w_m x_i^m
$$

The **error** (difference between actual and predicted):

$$
e_i = y_i - \hat{y}_i
$$

The **Mean Squared Error (MSE)**:

$$
E = \frac{1}{2n} \sum_{i=1}^n (y_i - \hat{y}_i)^2
$$

---

## 🔁 **Gradient Descent to Minimize Error**

We want to find the weights $w_j$ (for all $j = 0$ to $m$) that **minimize E**.

So, we update each weight like this:

### General Formula:

$$
w_j = w_j - \alpha \cdot \frac{\partial E}{\partial w_j}
$$

Where:

* $\alpha$: learning rate
* $\frac{\partial E}{\partial w_j}$: derivative of error with respect to weight $w_j$

---

## 🔧 **Derivative Calculation (example for each weight)**

Let’s derive the formula for updating each weight:

---

### 🔹 For $w_0$:

$$
\frac{\partial E}{\partial w_0} = -\frac{1}{n} \sum_{i=1}^n (y_i - \hat{y}_i)
$$

So:

$$
w_0 = w_0 + \alpha \cdot \frac{1}{n} \sum_{i=1}^n (y_i - \hat{y}_i)
$$

---

### 🔹 For $w_1$:

$$
\frac{\partial E}{\partial w_1} = -\frac{1}{n} \sum_{i=1}^n (y_i - \hat{y}_i) \cdot x_i
$$

So:

$$
w_1 = w_1 + \alpha \cdot \frac{1}{n} \sum_{i=1}^n (y_i - \hat{y}_i) \cdot x_i
$$

---

### 🔹 For $w_2$:

$$
\frac{\partial E}{\partial w_2} = -\frac{1}{n} \sum_{i=1}^n (y_i - \hat{y}_i) \cdot x_i^2
$$

So:

$$
w_2 = w_2 + \alpha \cdot \frac{1}{n} \sum_{i=1}^n (y_i - \hat{y}_i) \cdot x_i^2
$$

And so on for $w_3, w_4, \dots, w_m$

---

## 💡 Key Intuition

* We try to **minimize the average squared error** between the true $y_i$ and predicted $\hat{y}_i$
* Each weight affects error based on how strongly that power of $x$ influences the output
* By applying **gradient descent**, we slowly adjust weights to make predictions closer to actual outputs

---

## 📌 **Quick Revision Table**

| Weight | Update Rule                                                   |
| ------ | ------------------------------------------------------------- |
| $w_0$  | $w_0 + \alpha \cdot \frac{1}{n} \sum (y_i - \hat{y}_i)$       |
| $w_1$  | $w_1 + \alpha \cdot \frac{1}{n} \sum (y_i - \hat{y}_i) x_i$   |
| $w_2$  | $w_2 + \alpha \cdot \frac{1}{n} \sum (y_i - \hat{y}_i) x_i^2$ |
| ...    | ...                                                           |
| $w_m$  | $w_m + \alpha \cdot \frac{1}{n} \sum (y_i - \hat{y}_i) x_i^m$ |

---

## [Numerical of Polynomial Curve Fitting](Numerical%20of%20Polynomial%20Curve%20Fitting.md)