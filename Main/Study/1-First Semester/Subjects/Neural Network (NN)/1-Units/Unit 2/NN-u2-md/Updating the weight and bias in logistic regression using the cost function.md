
# (A) Proper mathematical derivation

## 1. Definitions

For one training example:

$y \in {0,1}$

$z = w_0 + w_1 x_1 + w_2 x_2$

$\hat y = \sigma(z) = \frac{1}{1 + e^{-z}}$

Loss function:

$L(y,\hat y) = -y \log(\hat y) - (1-y)\log(1-\hat y)$

---

## 2. Derivative of loss w.r.t. prediction $\hat y$

Differentiate term by term.

### First term

$-y \log(\hat y)$

$\frac{d}{d\hat y}[-y \log(\hat y)] = -y \cdot \frac{1}{\hat y}$

$= -\frac{y}{\hat y}$

---

### Second term

$-(1-y)\log(1-\hat y)$

Using chain rule:

$\frac{d}{d\hat y}\log(1-\hat y) = \frac{1}{1-\hat y} \cdot (-1)$

So:

$$\frac{d}{d\hat y}[-(1-y)\log(1-\hat y)]
= (1-y)\frac{1}{1-\hat y}$$

---

### Combine

$$\frac{\partial L}{\partial \hat y}
= -\frac{y}{\hat y} + \frac{1-y}{1-\hat y}$$

---

## 3. Derivative of prediction w.r.t. $z$ (sigmoid)

$\hat y = \frac{1}{1+e^{-z}}$

Derivative:

$\frac{d\hat y}{dz} = \hat y (1-\hat y)$

(This is a standard sigmoid identity.)

---

## 4. Chain rule: derivative of loss w.r.t. $z$

$$\frac{\partial L}{\partial z}
= \frac{\partial L}{\partial \hat y}
\cdot
\frac{\partial \hat y}{\partial z}$$

Substitute:

$$\frac{\partial L}{\partial z}=
\left(
-\frac{y}{\hat y} + \frac{1-y}{1-\hat y}
\right)
\hat y(1-\hat y)$$

---

## 5. Simplification (important step)

Multiply each term.

First term:

$$-\frac{y}{\hat y}\hat y(1-\hat y)
= -y(1-\hat y)$$

Second term:

$$\frac{1-y}{1-\hat y}\hat y(1-\hat y)
= (1-y)\hat y$$

Add:

$-y(1-\hat y) + (1-y)\hat y$

Expand:

$-y + y\hat y + \hat y - y\hat y$

Cancel terms:

$\frac{\partial L}{\partial z} = \hat y - y$

---

## 6. Derivative w.r.t. weights

Since:

$z = w_0 + w_1 x_1 + w_2 x_2$

### Bias term

$\frac{\partial z}{\partial w_0} = 1$

$$\frac{\partial L}{\partial w_0}
= (\hat y - y)$$

---

### Weight $w_1$

$\frac{\partial z}{\partial w_1} = x_1$

$$\frac{\partial L}{\partial w_1}
= (\hat y - y)x_1$$

---

### Weight $w_2$

$\frac{\partial z}{\partial w_2} = x_2$

$$\frac{\partial L}{\partial w_2}
= (\hat y - y)x_2$$

---

## 7. Gradient descent update

$w_j := w_j - \alpha \frac{\partial L}{\partial w_j}$

---

# (B) Description in simple words

Now what actually happened.

### 1. Why logs?

Log loss gives **huge penalty** when:

* $y=1$ and $\hat y$ is near 0
* $y=0$ and $\hat y$ is near 1

So the model is forced to correct confident mistakes.

---

### 2. Why differentiate w.r.t. $\hat y$ first?

Because:

* Loss depends on $\hat y$
* $\hat y$ depends on $z$
* $z$ depends on weights

So we move **backwards**, step by step.

This is **chain rule**.

---

### 3. Why sigmoid derivative matters?

Sigmoid converts linear output into probability.

Its derivative:

$\hat y(1-\hat y)$

automatically becomes **small near 0 and 1**, preventing unstable jumps.

---

### 4. Why everything becomes $\hat y - y$?

Because:

* Log loss
* Sigmoid
* Chain rule

**perfectly cancel messy terms**

What remains is pure error:

prediction − truth

---

### 5. Why weights multiply inputs?

Each weight affects prediction **through its input**.

Bigger input → bigger responsibility → bigger update.

---

### Final mental model (remember this)

Logistic regression learning rule:

**Error × Input**

Same structure as linear regression,
just with sigmoid + log loss underneath.

---
