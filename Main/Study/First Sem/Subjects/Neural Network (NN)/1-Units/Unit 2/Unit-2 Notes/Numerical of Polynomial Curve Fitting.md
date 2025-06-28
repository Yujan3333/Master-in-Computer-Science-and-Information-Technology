
![](../../../../../../../../Images/First_Sem_Images/Numerical%20of%20Polynomial%20Curve%20Fitting1.png)
![](../../../../../../../../Images/First_Sem_Images/Numerical%20of%20Polynomial%20Curve%20Fitting.png)



### ✅ **Initial weights from Iteration 1:**

Continued from above👆
$$
w_0 = 0.02,\quad w_1 = 0.02,\quad w_2 = 0.02
$$

---

### 🔁 **Iteration 2: x = 2, y = 7**

$$
\hat{y} = w_0 + w_1 x + w_2 x^2 = 0.02 + 0.02×2 + 0.02×4 = 0.02 + 0.04 + 0.08 = 0.14
$$

$$
\text{Error} = y - \hat{y} = 7 - 0.14 = 6.86
$$

**Update weights:**

$$
w_0 = w_0 + \alpha \cdot \text{Error} = 0.02 + 0.01 × 6.86 = \boxed{0.0886}
$$

$$
w_1 = w_1 + \alpha \cdot \text{Error} \cdot x = 0.02 + 0.01 × 6.86 × 2 = 0.02 + 0.1372 = \boxed{0.1572}
$$

$$
w_2 = w_2 + \alpha \cdot \text{Error} \cdot x^2 = 0.02 + 0.01 × 6.86 × 4 = 0.02 + 0.2744 = \boxed{0.2944}
$$

---

### 🔁 **Iteration 3: x = 3, y = 14**

$$
\hat{y} = w_0 + w_1 x + w_2 x^2 = 0.0886 + 0.1572×3 + 0.2944×9 \\
= 0.0886 + 0.4716 + 2.6496 = \boxed{3.2098}
$$

$$
\text{Error} = 14 - 3.2098 = \boxed{10.7902}
$$

**Update weights:**

$$
w_0 = 0.0886 + 0.01 × 10.7902 = \boxed{0.1965}
$$

$$
w_1 = 0.1572 + 0.01 × 10.7902 × 3 = 0.1572 + 0.3237 = \boxed{0.4809}
$$

$$
w_2 = 0.2944 + 0.01 × 10.7902 × 9 = 0.2944 + 0.9711 = \boxed{1.2655}
$$

---

### 🔁 **Iteration 4: x = 4, y = 23**

$$
\hat{y} = 0.1965 + 0.4809×4 + 1.2655×16 \\
= 0.1965 + 1.9236 + 20.248 = \boxed{22.3681}
$$

$$
\text{Error} = 23 - 22.3681 = \boxed{0.6319}
$$

**Update weights:**

$$
w_0 = 0.1965 + 0.01 × 0.6319 = \boxed{0.2028}
$$

$$
w_1 = 0.4809 + 0.01 × 0.6319 × 4 = 0.4809 + 0.0253 = \boxed{0.5062}
$$

$$
w_2 = 1.2655 + 0.01 × 0.6319 × 16 = 1.2655 + 0.1011 = \boxed{1.3666}
$$

---

### ✅ Final Weights After 1 Epoch:

$$
\boxed{
w_0 = 0.2028,\quad
w_1 = 0.5062,\quad
w_2 = 1.3666
}
$$

---

Would you like this formatted as a handwritten-style PDF for printing?
