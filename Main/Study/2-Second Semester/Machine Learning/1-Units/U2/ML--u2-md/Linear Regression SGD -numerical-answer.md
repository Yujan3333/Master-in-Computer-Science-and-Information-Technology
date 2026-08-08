![](../../../../../../../Images/Second_Sem_Images/Linear%20Regression-num.png)

---

### ✅ **SGD for Linear Regression (One Epoch, α = 0.1)**

Initial parameters:
$w_0 = 0$, $w_1 = 0$
Model: $\hat{y} = w_0 + w_1 x$
Error: $e = y - \hat{y}$
SGD update rules:
$w_0 \leftarrow w_0 + \alpha e$
$w_1 \leftarrow w_1 + \alpha e x$

---

### **Step 1: (x = 1, y = 3)**

$\hat{y} = 0 + 0 \cdot 1 = 0$
$e = 3 - 0 = 3$
$w_0 = 0 + 0.1 \cdot 3 = 0.3$
$w_1 = 0 + 0.1 \cdot 3 \cdot 1 = 0.3$

---

### **Step 2: (x = 2, y = 5)**

$\hat{y} = 0.3 + 0.3 \cdot 2 = 0.9$
$e = 5 - 0.9 = 4.1$
$w_0 = 0.3 + 0.1 \cdot 4.1 = 0.71$
$w_1 = 0.3 + 0.1 \cdot 4.1 \cdot 2 = 1.12$

---

### **Step 3: (x = 3, y = 7)**

$\hat{y} = 0.71 + 1.12 \cdot 3 = 4.07$
$e = 7 - 4.07 = 2.93$
$w_0 = 0.71 + 0.1 \cdot 2.93 = 1.003$
$w_1 = 1.12 + 0.1 \cdot 2.93 \cdot 3 = 1.999$

---

### **Step 4: (x = 4, y = 9)**

$\hat{y} = 1.003 + 1.999 \cdot 4 = 8.999$
$e = 9 - 8.999 = 0.001$
$w_0 = 1.003 + 0.1 \cdot 0.001 = 1.0031$
$w_1 = 1.999 + 0.1 \cdot 0.001 \cdot 4 = 1.9994$

---

### **Final values after one epoch**

$w_0 \approx 1.0031$
$w_1 \approx 1.9994$

---

#### [Things to be mindful of while doing the Linear Regression Numerical](Things%20to%20be%20mindful%20of%20while%20doing%20the%20Linear%20Regression%20Numerical.md)