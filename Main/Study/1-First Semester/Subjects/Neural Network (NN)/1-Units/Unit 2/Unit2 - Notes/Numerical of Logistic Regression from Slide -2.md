![](../../../../../../../../Images/Second_Sem_Images/Numerical%20of%20Logistic%20Regression%20from%20Slide%20-2.png)

---
## Answer

## **Given Data**

We have 4 samples:

| $x_1$ | $x_2$ | $y$ |
| ----- | ----- | --- |
| 0.78  | 0.69  | 1   |
| 0.67  | 1.00  | 1   |
| 0.00  | 0.00  | 0   |
| 0.22  | 0.14  | 0   |

We want to fit a **logistic regression model**:

$$
\hat{y} = \sigma(z), \quad z = w_0 + w_1 x_1 + w_2 x_2, \quad \sigma(z) = \frac{1}{1 + e^{-z}}
$$

We will use **Batch Gradient Descent**:

$$
w_j := w_j - \alpha \frac{\partial J}{\partial w_j}, \quad j = 0,1,2
$$

where the **cost gradient** is:

$$
\frac{\partial J}{\partial w_j} = \frac{1}{N} \sum_{i=1}^N (\hat{y}^{(i)} - y^{(i)}) x_j^{(i)}
$$

and for $w_0$, $x_0 = 1$.

Assume **learning rate $\alpha = 0.1$** and initialize all weights to zero:

$$
w_0 = 0, \quad w_1 = 0, \quad w_2 = 0
$$

---

## **Step 1: Compute $z$ and $\hat{y}$ for each sample**

Since all weights are 0:

$$
z^{(i)} = w_0 + w_1 x_1^{(i)} + w_2 x_2^{(i)} = 0
$$

Then the sigmoid:

$$
\hat{y}^{(i)} = \sigma(0) = \frac{1}{1 + e^0} = 0.5
$$

So predictions for all 4 samples:

$$
\hat{y}^{(1)} = 0.5, \quad \hat{y}^{(2)} = 0.5, \quad \hat{y}^{(3)} = 0.5, \quad \hat{y}^{(4)} = 0.5
$$

---

## **Step 2: Compute errors**

$$
\hat{y}^{(i)} - y^{(i)}:
$$

* Sample 1: $0.5 - 1 = -0.5$
* Sample 2: $0.5 - 1 = -0.5$
* Sample 3: $0.5 - 0 = 0.5$
* Sample 4: $0.5 - 0 = 0.5$

---

## **Step 3: Compute gradients**

**Gradient for $w_0$:**

$$
\frac{\partial J}{\partial w_0} = \frac{1}{4} \sum_{i=1}^4 (\hat{y}^{(i)} - y^{(i)})
= \frac{-0.5 - 0.5 + 0.5 + 0.5}{4} = 0
$$

**Gradient for $w_1$:**

$$
\frac{\partial J}{\partial w_1} = \frac{1}{4} \sum_{i=1}^4 (\hat{y}^{(i)} - y^{(i)}) x_1^{(i)}
$$

Compute each term:

1. $(-0.5) * 0.78 = -0.39$
2. $(-0.5) * 0.67 = -0.335$
3. $(0.5) * 0 = 0$
4. $(0.5) * 0.22 = 0.11$

Sum: $-0.39 - 0.335 + 0 + 0.11 = -0.615$

Average: $-0.615 / 4 = -0.15375 \approx -0.154$

**Gradient for $w_2$:**

$$
\frac{\partial J}{\partial w_2} = \frac{1}{4} \sum_{i=1}^4 (\hat{y}^{(i)} - y^{(i)}) x_2^{(i)}
$$

Compute each term:

1. $(-0.5) * 0.69 = -0.345$
2. $(-0.5) * 1.00 = -0.5$
3. $(0.5) * 0 = 0$
4. $(0.5) * 0.14 = 0.07$

Sum: $-0.345 - 0.5 + 0 + 0.07 = -0.775$

Average: $-0.775 / 4 = -0.19375 \approx -0.194$

---

## **Step 4: Update weights**

$$
w_j := w_j - \alpha \frac{\partial J}{\partial w_j}
$$

* $w_0 = 0 - 0.1 * 0 = 0$
* $w_1 = 0 - 0.1 * (-0.154) = 0 + 0.0154 \approx 0.015$
* $w_2 = 0 - 0.1 * (-0.194) = 0 + 0.0194 \approx 0.019$

---

## ✅ **After one epoch, the updated weights are:**

$$
\boxed{w_0 = 0, \quad w_1 \approx 0.015, \quad w_2 \approx 0.019}
$$

This completes **one epoch of BGD** for the logistic regression model.

---
