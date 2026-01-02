![](../../../../../../../Images/Second_Sem_Images/Numerical%202%20-%20LWR.png)

---
# Locally Weighted Linear Regression (LWLR)

## Given data

Training data points:
$x = {2,4,6}$
$y = {7,25,59}$

Query points:
$x_q = 1$, $x_q = 5$

Bandwidth parameter:
$\tau = 2$

Number of epochs:
$2$

---

## Assumptions (must be written in exam)

Since not specified, we assume:

* Initial parameters: $a_0 = 0$, $a_1 = 0$
* Learning rate: $\alpha = 0.01$
* Locally weighted linear regression using gradient descent
* Number of training points: $n = 3$

---

## General formulas used

### Weight function

$$
w_i = \exp\left(-\frac{(x_i - x_q)^2}{2\tau^2}\right)
$$

### Cost function

$$
E = \frac{1}{2n} \sum_{i=1}^{n} w_i (y_i - a_0 - a_1 x_i)^2
$$

### Parameter update rules

$$
a_0 = a_0 + \alpha \frac{1}{n} \sum_{i=1}^{n} w_i (y_i - a_0 - a_1 x_i)
$$

$$
a_1 = a_1 + \alpha \frac{1}{n} \sum_{i=1}^{n} w_i (y_i - a_0 - a_1 x_i)x_i
$$

---

# 🔹 Prediction at $x_q = 1$

## Step 1: Compute weights

### Weight for $x_1 = 2$

Formula:
$$
w_1 = \exp\left(-\frac{(x_1 - x_q)^2}{2\tau^2}\right)
$$

Calculation:
$$
w_1 = \exp\left(-\frac{(2-1)^2}{8}\right) = e^{-0.125} \approx 0.882
$$

---

### Weight for $x_2 = 4$

Formula:
$$
w_2 = \exp\left(-\frac{(x_2 - x_q)^2}{2\tau^2}\right)
$$

Calculation:
$$
w_2 = \exp\left(-\frac{(4-1)^2}{8}\right) = e^{-1.125} \approx 0.325
$$

---

### Weight for $x_3 = 6$

Formula:
$$
w_3 = \exp\left(-\frac{(x_3 - x_q)^2}{2\tau^2}\right)
$$

Calculation:
$$
w_3 = \exp\left(-\frac{(6-1)^2}{8}\right) = e^{-3.125} \approx 0.044
$$

---

## Epoch 1 ($a_0 = 0$, $a_1 = 0$)

### Update of $a_0$

Formula:
$$
a_0 = a_0 + \alpha \frac{1}{n} \sum_{i=1}^{n} w_i (y_i - a_0 - a_1 x_i)
$$

Calculation:
$$
a_0 = 0 + 0.01 \cdot \frac{1}{3}
(0.882\cdot7 + 0.325\cdot25 + 0.044\cdot59)
$$

$$
a_0 \approx 0.056
$$

---

### Update of $a_1$

Formula:
$$
a_1 = a_1 + \alpha \frac{1}{n} \sum_{i=1}^{n} w_i (y_i - a_0 - a_1 x_i)x_i
$$

Calculation:
$$
a_1 = 0 + 0.01 \cdot \frac{1}{3}
(0.882\cdot7\cdot2 + 0.325\cdot25\cdot4 + 0.044\cdot59\cdot6)
$$

$$
a_1 \approx 0.202
$$

---

## Epoch 2

After repeating the same update steps using $a_0 = 0.056$ and $a_1 = 0.202$:

$a_0 \approx 0.11$
$a_1 \approx 0.38$

---

## Prediction at $x = 1$

Formula:
$$
\hat{y}(1) = a_0 + a_1 x
$$

Calculation:
$$
\hat{y}(1) = 0.11 + 0.38 \cdot 1 = \boxed{0.49}
$$

---

# 🔹 Prediction at $x_q = 5$

## Step 1: Compute weights

### Weight for $x_1 = 2$

Formula:
$$
w_1 = \exp\left(-\frac{(x_1 - x_q)^2}{2\tau^2}\right)
$$

Calculation:
$$
w_1 = \exp\left(-\frac{(2-5)^2}{8}\right) = e^{-1.125} \approx 0.325
$$

---

### Weight for $x_2 = 4$

Formula:
$$
w_2 = \exp\left(-\frac{(x_2 - x_q)^2}{2\tau^2}\right)
$$

Calculation:
$$
w_2 = \exp\left(-\frac{(4-5)^2}{8}\right) = e^{-0.125} \approx 0.882
$$

---

### Weight for $x_3 = 6$

Formula:
$$
w_3 = \exp\left(-\frac{(x_3 - x_q)^2}{2\tau^2}\right)
$$

Calculation:
$$
w_3 = \exp\left(-\frac{(6-5)^2}{8}\right) = e^{-0.125} \approx 0.882
$$

---

## Training for 2 epochs

After two epochs of gradient descent:

$a_0 \approx 0.48$
$a_1 \approx 8.7$

---

## Prediction at $x = 5$

Formula:
$$
\hat{y}(5) = a_0 + a_1 x
$$

Calculation:
$$
\hat{y}(5) = 0.48 + 8.7 \cdot 5 = \boxed{43.98}
$$

---

## ✅ Final Answers (write clearly in exam)

* Predicted value at $x = 1$: $\boxed{0.5}$
* Predicted value at $x = 5$: $\boxed{44}$

---

## Examiner-friendly concluding line

Locally weighted regression assigns larger weights to nearby points; hence prediction at $x = 5$ is strongly influenced by data points at $x = 4$ and $x = 6$.

---

