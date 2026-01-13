## **Given:**

Data points:
$$(1,2),(2,3),(1,4),(2,6),(2,8),(3,7),(2,4)$$

$k=2$ clusters.

---

### **Step 1: Initialization**

Let’s pick:
$$\mu_1=(1,2),\quad\mu_2=(3,7)$$

Covariance matrices:
$$\Sigma_1=\begin{bmatrix}1&0\0&1\end{bmatrix},\quad\Sigma_2=\begin{bmatrix}1&0\0&1\end{bmatrix}$$

Mixing coefficients:
$$p_1=0.5,\quad p_2=0.5$$

$N=7$ points.

---

### **Step 2: Probability density for multivariate Gaussian**

Since $\Sigma_i=I$:
$$f_i(\mathbf{x})=\frac{1}{2\pi}\exp\left(-\frac12|\mathbf{x}-\mu_i|^2\right)$$

---

### **Step 3: E-step — compute responsibilities**

$$\gamma_{ni}=\frac{p_i\cdot f_i(\mathbf{x}*n)}{\sum*{j=1}^2p_j\cdot f_j(\mathbf{x}_n)}$$

---

#### **Point (1,2):**

$$|\mathbf{x}-\mu_1|^2=0,\quad f_1\approx0.159155$$
$$|\mathbf{x}-\mu_2|^2=29,\quad f_2\approx7.96\times10^{-8}$$
$$\gamma_{11}\approx0.9999995,\quad\gamma_{12}\approx5\times10^{-7}$$

---

#### **Point (2,3):**

$$|\mathbf{x}-\mu_1|^2=2,\quad f_1\approx0.05855$$
$$|\mathbf{x}-\mu_2|^2=17,\quad f_2\approx3.183\times10^{-5}$$
$$\gamma_{21}\approx0.99946,\quad\gamma_{22}\approx0.00054$$

---

#### **Point (1,4):**

$$|\mathbf{x}-\mu_1|^2=4,\quad f_1\approx0.02154$$
$$|\mathbf{x}-\mu_2|^2=13,\quad f_2\approx2.387\times10^{-4}$$
$$\gamma_{31}\approx0.989,\quad\gamma_{32}\approx0.011$$

---

#### **Point (2,6):**

$$|\mathbf{x}-\mu_1|^2=17,\quad f_1\approx3.183\times10^{-5}$$
$$|\mathbf{x}-\mu_2|^2=2,\quad f_2\approx0.05855$$
$$\gamma_{41}\approx0.000543,\quad\gamma_{42}\approx0.999457$$

---

#### **Point (2,8):**

$$|\mathbf{x}-\mu_1|^2=37,\quad f_1\approx1.15\times10^{-9}$$
$$|\mathbf{x}-\mu_2|^2=2,\quad f_2\approx0.05855$$
$$\gamma_{51}\approx2\times10^{-8},\quad\gamma_{52}\approx1$$

---

#### **Point (3,7):**

$$|\mathbf{x}-\mu_1|^2=29,\quad f_1\approx7.96\times10^{-8}$$
$$|\mathbf{x}-\mu_2|^2=0,\quad f_2\approx0.159155$$
$$\gamma_{61}\approx5\times10^{-7},\quad\gamma_{62}\approx1$$

---

#### **Point (2,4):**

$$|\mathbf{x}-\mu_1|^2=5,\quad f_1\approx0.01306$$
$$|\mathbf{x}-\mu_2|^2=10,\quad f_2\approx0.001072$$
$$\gamma_{71}\approx0.924,\quad\gamma_{72}\approx0.076$$

---

### **Step 4: Compute $N_i$**

$$N_1=\sum_{n=1}^7\gamma_{n1}\approx3.913$$
$$N_2=7-N_1\approx3.087$$

---

### **Step 5: M-step — update parameters**

#### **New $\mu_1$:**

$$\mu_1=\frac{1}{N_1}\sum_n\gamma_{n1}\mathbf{x}_n$$

Weighted $x$-sum:
$1(0.9999995)+2(0.99946)+1(0.989)+2(0.000543)+2(2\times10^{-8})+3(5\times10^{-7})+2(0.924)\approx5.836$

Weighted $y$-sum:
$2(0.9999995)+3(0.99946)+4(0.989)+6(0.000543)+8(2\times10^{-8})+7(5\times10^{-7})+4(0.924)\approx12.654$

$$\mu_1\approx\left(\frac{5.836}{3.913},\frac{12.654}{3.913}\right)\approx(1.491,3.233)$$

---

#### **New $\mu_2$:**

$$\mu_2=\frac{1}{N_2}\sum_n\gamma_{n2}\mathbf{x}_n$$

Weighted $x$-sum:
$1(5\times10^{-7})+2(0.00054)+1(0.011)+2(0.999457)+2(1)+3(1)+2(0.076)\approx7.163$

Weighted $y$-sum:
$2(5\times10^{-7})+3(0.00054)+4(0.011)+6(0.999457)+8(1)+7(1)+4(0.076)\approx21.346$

$$\mu_2\approx\left(\frac{7.163}{3.087},\frac{21.346}{3.087}\right)\approx(2.321,6.915)$$

---

#### **New mixing coefficients:**

$$p_1=\frac{N_1}{N}\approx\frac{3.913}{7}\approx0.559$$
$$p_2=\frac{N_2}{N}\approx\frac{3.087}{7}\approx0.441$$

---

### **After 1 iteration:**

$$\mu_1\approx(1.49,3.23),\quad\mu_2\approx(2.32,6.92)$$
$$p_1\approx0.559,\quad p_2\approx0.441$$

Covariances $\Sigma_1,\Sigma_2$ can be updated similarly.
