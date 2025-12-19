![](../../../../../../../Images/Second_Sem_Images/Multinomial%20Logistic%20Regression%20-%20Numerical.png)

---
## 1️⃣ WHAT is this formula?

### The key formula confusing you is:

$$
\hat y^{(i)} = \frac{e^{y^{(i)}}}{\sum_{j=1}^k e^{y^{(j)}}}
$$

This is called **softmax**.

### What are these symbols REALLY?

* $y^{(i)}$ → raw score for class $i$
  (NOT probability, just a number)
* $e^{y^{(i)}}$ → makes the score **positive**
* denominator → makes all outputs **sum to 1**
* $\hat y^{(i)}$ → final **probability** of class $i$

👉 So softmax **converts raw scores into probabilities**.

---

## 2️⃣ WHY do we need softmax?

### Problem without softmax

Suppose your model outputs:

* Class 1 score = 2
* Class 2 score = 1
* Class 3 score = −1

These are **not probabilities**:

* They can be negative
* They don’t sum to 1

But classification **needs probabilities** like:

* 70% class A
* 20% class B
* 10% class C

### Softmax fixes this by:

✔ making everything positive
✔ scaling values between 0 and 1
✔ ensuring total = 1

That’s **why softmax exists**.

---
---

# GIVEN DATA

| $x_1$ | $x_2$ | Class |
| ----- | ----- | ----- |
| 0.1   | 0.5   | 0     |
| 1.1   | 2.3   | 1     |
| −1.1  | −2.3  | 2     |
| −1.5  | −2.5  | 2     |

---

## STEP 1: One-Hot Encoding

Class mapping:

* $0 \rightarrow (1,0,0)$
* $1 \rightarrow (0,1,0)$
* $2 \rightarrow (0,0,1)$

So targets:

| Sample | $y$       |
| ------ | --------- |
| 1      | $(1,0,0)$ |
| 2      | $(0,1,0)$ |
| 3      | $(0,0,1)$ |
| 4      | $(0,0,1)$ |

---

## STEP 2: Initial Weights (Given)

Each class has its own weight vector
($w_0$ = bias)

$$
W =
\begin{bmatrix}
0.01 & 0.1 & 0.1 \
0.1 & 0.2 & 0.3 \
0.1 & 0.2 & 0.3
\end{bmatrix}
$$

So:

* Class 0: $(w_0,w_1,w_2)=(0.01,0.1,0.1)$
* Class 1: $(0.1,0.2,0.3)$
* Class 2: $(0.1,0.2,0.3)$

---

## STEP 3: SGD → Sample 1

### Input

$$
x = (1,;0.1,;0.5)
$$

### True label

$$
y = (1,0,0)
$$

---

### STEP 3.1: Linear Scores $z$

Class 0:
$$
z_0 = 0.01 + 0.1(0.1) + 0.1(0.5) = 0.07
$$

Class 1:
$$
z_1 = 0.1 + 0.2(0.1) + 0.3(0.5) = 0.27
$$

Class 2:
$$
z_2 = 0.1 + 0.2(0.1) + 0.3(0.5) = 0.27
$$

---

### STEP 3.2: Softmax

$$
e^{0.07}=1.0725,\quad e^{0.27}=1.310
$$

Sum:
$$
1.0725 + 1.310 + 1.310 = 3.6925
$$

Predicted probabilities:
$$
\hat y = (0.290,;0.355,;0.355)
$$

---

### STEP 3.3: Error ($\hat y - y$)

$$
(0.290-1,;0.355-0,;0.355-0)
============

(-0.710,;0.355,;0.355)
$$

---

### STEP 3.4: Weight Update Formula

$$
w = w - \alpha(\hat y - y)x
$$

$\alpha = 0.1$

---

### Update Class 0 Weights

$$
w_0 = 0.01 - 0.1(-0.710) = 0.081
$$
$$
w_1 = 0.1 - 0.1(-0.710)(0.1) = 0.1071
$$
$$
w_2 = 0.1 - 0.1(-0.710)(0.5) = 0.1355
$$

---

### Update Class 1 Weights

$$
w_0 = 0.1 - 0.1(0.355) = 0.0645
$$
$$
w_1 = 0.2 - 0.1(0.355)(0.1) = 0.1965
$$
$$
w_2 = 0.3 - 0.1(0.355)(0.5) = 0.28225
$$

---

### Update Class 2 Weights

Same error as class 1:

$$
(0.0645,;0.1965,;0.28225)
$$

---

## STEP 4: SGD → Sample 2 (Shortened but Numerical)

Input:
$$
x=(1,1.1,2.3),\quad y=(0,1,0)
$$

After computing:
$$
\hat y \approx (0.21,;0.43,;0.36)
$$
*here x contains the value of bias and then x1 and x2*

Error:
$$
(0.21,;-0.57,;0.36)
$$

Update weights again using same formula.

---

## STEP 5: One Epoch Meaning

✔ One epoch = **each sample used once**
✔ SGD = **weights updated after every sample**

After 4 samples → **1 full epoch completed**

---

## EXAM-READY FINAL STATEMENT (WRITE THIS)

> One epoch of SGD was performed by computing linear scores, applying softmax, calculating error $(\hat y - y)$, and updating weights using gradient descent for each sample sequentially.

---
