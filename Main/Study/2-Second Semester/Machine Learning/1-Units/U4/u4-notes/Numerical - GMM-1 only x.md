## **Given**

Data points:
$$X={1,2,3,6,10,11,12}$$

We want **2 clusters** ($k=2$).

Initial parameters:
$$\mu_1=1,\quad\mu_2=10$$
$$\sigma_1=0.8,\quad\sigma_2=0.8$$
$$p_1=0.5,\quad p_2=0.5$$

---

## **Step 1: Probability density function (Gaussian)**

For component $i$:
$$f_i(x)=\frac{1}{\sigma_i\sqrt{2\pi}}\exp\Big(-\frac{(x-\mu_i)^2}{2\sigma_i^2}\Big)$$

---

### **Precompute constants**

$$\sigma=0.8\Rightarrow\sigma\sqrt{2\pi}\approx0.8\times2.506628\approx2.0053$$

$$\frac{1}{\sigma\sqrt{2\pi}}\approx0.4987$$

Also
$$\frac{1}{2\sigma^2}=\frac{1}{2\times0.64}=\frac{1}{1.28}\approx0.78125$$

---

### **For $x=1$**

$$f_1(1)=0.4987\times e^{-0.78125(1-1)^2}=0.4987$$

$$f_2(1)=0.4987\times e^{-0.78125(1-10)^2}$$

$$0.78125\times81\approx63.28125$$

$$e^{-63.28125}\approx1.5\times10^{-28};(\text{effectively }0)$$

So, $f_2(1)\approx0$.

---

### **For $x=2$**

$$f_1(2)=0.4987\times e^{-0.78125(2-1)^2}$$

$$e^{-0.78125}\approx0.4578$$

$$f_1(2)\approx0.2283$$

$$f_2(2)=0.4987\times e^{-0.78125(2-10)^2}$$

$$0.78125\times64=50$$

$$e^{-50}\approx1.93\times10^{-22};(\approx0)$$

---

### **For $x=3$**

$$f_1(3)=0.4987\times e^{-0.78125(3-1)^2}$$

$$e^{-3.125}\approx0.04394$$

$$f_1(3)\approx0.02192$$

$$f_2(3)\approx0$$

---

### **For $x=6$**

$$f_1(6)=0.4987\times e^{-0.78125(6-1)^2}$$

$$e^{-19.53125}\approx3.33\times10^{-9}$$

$$f_2(6)=0.4987\times e^{-0.78125(6-10)^2}$$

$$e^{-12.5}\approx3.73\times10^{-6}$$

$$f_2(6)\approx1.86\times10^{-6}$$

---

### **For $x=10$**

$$f_1(10)\approx0$$

$$f_2(10)=0.4987$$

---

### **For $x=11$**

$$f_1(11)\approx0$$

$$f_2(11)=0.4987\times e^{-0.78125}\approx0.2283$$

---

### **For $x=12$**

$$f_1(12)\approx0$$

$$f_2(12)=0.4987\times e^{-0.78125(12-10)^2}\approx0.02192$$

---

## **Step 2: E-step – Responsibilities $y_{ni}$**

$$y_{n1}=\frac{p_1f_1(x_n)}{p_1f_1(x_n)+p_2f_2(x_n)}$$

Since $p_1=p_2=0.5$:
$$y_{n1}=\frac{f_1(x_n)}{f_1(x_n)+f_2(x_n)},\quad y_{n2}=1-y_{n1}$$

Results:

* $x=1$: $y_{11}\approx1,;y_{21}\approx0$
* $x=2$: $y_{12}\approx1,;y_{22}\approx0$
* $x=3$: $y_{13}\approx1,;y_{23}\approx0$
* $x=6$:
  $$y_{14}\approx\frac{3.33\times10^{-9}}{1.863\times10^{-6}}\approx0.00179,\quad y_{24}\approx0.99821$$
* $x=10$: $y_{15}\approx0,;y_{25}\approx1$
* $x=11$: $y_{16}\approx0,;y_{26}\approx1$
* $x=12$: $y_{17}\approx0,;y_{27}\approx1$

---

## **Step 3: M-step – Update parameters**

$$N_1=\sum_{n=1}^{7}y_{n1},\quad N_2=\sum_{n=1}^{7}y_{n2}$$

$$y_{n1}=[1,1,1,0.00179,0,0,0]\Rightarrow N_1\approx3.00179$$

$$y_{n2}=[0,0,0,0.99821,1,1,1]\Rightarrow N_2\approx3.99821$$

Check:
$$N_1+N_2=7$$

---

### **Update $\mu_1$**

$$\mu_1=\frac{1}{N_1}\sum_{n=1}^{7}y_{n1}x_n$$

$$\sum y_{n1}x_n=1\cdot1+1\cdot2+1\cdot3+0.00179\cdot6\approx6.01074$$

$$\mu_1\approx\frac{6.01074}{3.00179}\approx2.002$$

---

### **Update $\mu_2$**

$$\mu_2=\frac{1}{N_2}\sum_{n=1}^{7}y_{n2}x_n$$

$$\sum y_{n2}x_n=0.99821\cdot6+10+11+12\approx38.98926$$

$$\mu_2\approx\frac{38.98926}{3.99821}\approx9.751$$

---

### **Update $\sigma_1^2$**

$$\sigma_1^2=\frac{1}{N_1}\sum_{n=1}^{7}y_{n1}(x_n-\mu_1)^2$$

$$n=1:(1-2.002)^2\approx1.004,;n=2:(2-2.002)^2\approx4\times10^{-6},;n=3:(3-2.002)^2\approx0.996,;n=4:0.00179(6-2.002)^2\approx0.0286$$

Sum:
$$2.0286$$

$$\sigma_1^2\approx\frac{2.0286}{3.00179}\approx0.676,\quad\sigma_1\approx0.822$$

---

### **Update $\sigma_2^2$**

$$\sigma_2^2=\frac{1}{N_2}\sum_{n=1}^{7}y_{n2}(x_n-\mu_2)^2$$

$$n=4:0.99821(6-9.751)^2\approx14.04,;n=5:(10-9.751)^2\approx0.062,;n=6:(11-9.751)^2\approx1.562,;n=7:(12-9.751)^2\approx5.061$$

Sum:
$$20.725$$

$$\sigma_2^2\approx\frac{20.725}{3.99821}\approx5.183,\quad\sigma_2\approx2.277$$

---

### **Update mixing weights**

$$p_1=\frac{N_1}{N}\approx0.4288,\quad p_2=\frac{N_2}{N}\approx0.5712$$

---

## **Updated parameters after 1 iteration**

$$\mu_1\approx2.00,\quad\mu_2\approx9.75$$

$$\sigma_1\approx0.822,\quad\sigma_2\approx2.277$$

$$p_1\approx0.429,\quad p_2\approx0.571$$

---
