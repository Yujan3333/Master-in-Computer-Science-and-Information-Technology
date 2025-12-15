![](../../../../../../../../Images/Second_Sem_Images/Numerical%20of%20Logistic%20Regression%20from%20Slide-1.png)

---
## Answer

## Given data

We have $4$ training samples:

Sample 1:
$x_1 = 0.78,\ x_2 = 0.69,\ y = 1$

Sample 2:
$x_1 = 0.67,\ x_2 = 1.00,\ y = 1$

Sample 3:
$x_1 = 0.00,\ x_2 = 0.00,\ y = 0$

Sample 4:
$x_1 = 0.22,\ x_2 = 0.14,\ y = 0$

---

## Logistic Regression Model

Linear combination:
$$
z = w_0 + w_1 x_1 + w_2 x_2
$$

Sigmoid (prediction):
$$
\hat y = \frac{1}{1 + e^{-z}}
$$

---

## Initial weights (given)

$$
w_0 = 0,\quad w_1 = 0,\quad w_2 = 0
$$

---

## Learning rate (assumed)

Since not given, we assume:
$$
\alpha = 0.1
$$

---

## SGD Gradient formulas (single sample)

Error:
$$
\text{error} = \hat y - y
$$

Weight updates:
$$
w_0 = w_0 - \alpha(\hat y - y)
$$
$$
w_1 = w_1 - \alpha(\hat y - y)x_1
$$
$$
w_2 = w_2 - \alpha(\hat y - y)x_2
$$

---

# One Epoch of Stochastic Gradient Descent

Weights are updated **after each sample**.

---

## Sample 1

$x_1 = 0.78,\ x_2 = 0.69,\ y = 1$

### Step 1: Compute $z$

$$
z = 0 + 0 + 0 = 0
$$

### Step 2: Prediction

$$
\hat y = \frac{1}{1 + e^{0}} = 0.5
$$

### Step 3: Error

$$
\hat y - y = 0.5 - 1 = -0.5
$$

### Step 4: Update weights

$$
w_0 = 0 - 0.1(-0.5) = 0.05
$$
$$
w_1 = 0 - 0.1(-0.5 \times 0.78) = 0.039
$$
$$
w_2 = 0 - 0.1(-0.5 \times 0.69) = 0.0345
$$

---

## Sample 2

$x_1 = 0.67,\ x_2 = 1.00,\ y = 1$

### Step 1: Compute $z$

$$
z = 0.05 + 0.039(0.67) + 0.0345(1.00)
$$
$$
z \approx 0.1106
$$

### Step 2: Prediction

$$
\hat y = \frac{1}{1 + e^{-0.1106}} \approx 0.528
$$

### Step 3: Error

$$
\hat y - y = 0.528 - 1 = -0.472
$$

### Step 4: Update weights

$$
w_0 = 0.05 - 0.1(-0.472) = 0.0972
$$
$$
w_1 = 0.039 - 0.1(-0.472 \times 0.67) = 0.0706
$$
$$
w_2 = 0.0345 - 0.1(-0.472 \times 1.00) = 0.0817
$$

---

## Sample 3

$x_1 = 0,\ x_2 = 0,\ y = 0$

### Step 1: Compute $z$

$$
z = 0.0972
$$

### Step 2: Prediction

$$
\hat y = \frac{1}{1 + e^{-0.0972}} \approx 0.524
$$

### Step 3: Error

$$
\hat y - y = 0.524 - 0 = 0.524
$$

### Step 4: Update weights

$$
w_0 = 0.0972 - 0.1(0.524) = 0.0448
$$
$$
w_1 = 0.0706 \quad (\text{unchanged})
$$
$$
w_2 = 0.0817 \quad (\text{unchanged})
$$

---

## Sample 4

$x_1 = 0.22,\ x_2 = 0.14,\ y = 0$

### Step 1: Compute $z$

$$
z = 0.0448 + 0.0706(0.22) + 0.0817(0.14)
$$
$$
z \approx 0.0718
$$

### Step 2: Prediction

$$
\hat y = \frac{1}{1 + e^{-0.0718}} \approx 0.518
$$

### Step 3: Error

$$
\hat y - y = 0.518 - 0 = 0.518
$$

### Step 4: Update weights

$$
w_0 = 0.0448 - 0.1(0.518) = -0.007
$$
$$
w_1 = 0.0706 - 0.1(0.518 \times 0.22) = 0.0592
$$
$$
w_2 = 0.0817 - 0.1(0.518 \times 0.14) = 0.0745
$$

---

## Final weights after one epoch

$$
w_0 \approx -0.007,\quad
w_1 \approx 0.059,\quad
w_2 \approx 0.075
$$

---

### Exam conclusion sentence

After one epoch of stochastic gradient descent, the updated weights are
$w_0 = -0.007,\ w_1 = 0.059,\ w_2 = 0.075$.
