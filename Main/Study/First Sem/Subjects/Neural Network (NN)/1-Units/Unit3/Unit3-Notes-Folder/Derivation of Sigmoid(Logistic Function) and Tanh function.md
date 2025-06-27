
## ✅ 1. **Sigmoid Function** (also called logistic function)

### 📌 Formula:

$$
\sigma(x) = \frac{1}{1 + e^{-x}}
$$

---

### 📈 What it does:

* Takes **any real number**
* Outputs a value between **0 and 1**
* Looks like an “S” curve

![](../../../../../../../../Images/First_Sem_Images/Sigmoid%20graph.png)

---

### 📘 Derivative of sigmoid:

Let’s derive it in a very easy way:

We start from:

$$
\sigma(x) = \frac{1}{1 + e^{-x}}
$$

Let’s denote $\sigma(x)$ as $y$. So:

$$
y = \frac{1}{1 + e^{-x}}
$$

Now differentiate using chain rule:

$$
\frac{dy}{dx} = y(1 - y)
$$

#### [Process of Derivation of sigmiod](Process%20of%20Derivation%20of%20sigmiod.md)

---

### ✅ Final result:

$$
\frac{d}{dx} \sigma(x) = \sigma(x)(1 - \sigma(x))
$$

---

## ✅ 2. **Tanh Function** (Hyperbolic tangent)

### 📌 Formula:

$$
\tanh(x) = \frac{e^x - e^{-x}}{e^x + e^{-x}}
$$

---

### 📈 What it does:

* Takes any real number
* Outputs a value between **−1 and 1**
* Also looks like an “S” curve but centered at 0

![](../../../../../../../../Images/First_Sem_Images/tanh%20graph.png)

---

### 📘 Derivative of tanh:

Let’s denote:

$$
y = \tanh(x)
$$

The derivative is:

$$
\frac{dy}{dx} = 1 - y^2
$$


#### [Derivation steps of Tanh](Derivation%20steps%20of%20Tanh.md)

---

### ✅ Final result:

$$
\frac{d}{dx} \tanh(x) = 1 - \tanh^2(x)
$$

---

## 🎯 Summary Table:

| Function | Output Range | Formula                             | Derivative                 |
| -------- | ------------ | ----------------------------------- | -------------------------- |
| Sigmoid  | 0 to 1       | $\frac{1}{1 + e^{-x}}$              | $\sigma(x)(1 - \sigma(x))$ |
| Tanh     | −1 to 1      | $\frac{e^x - e^{-x}}{e^x + e^{-x}}$ | $1 - \tanh^2(x)$           |
