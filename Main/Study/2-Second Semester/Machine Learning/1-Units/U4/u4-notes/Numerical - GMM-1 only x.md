
## **Given:**

Data points:
$$
X = {1, 2, 3, 6, 10, 11, 12}
$$
We want **2 clusters** ($k = 2$).

Initial parameters:
$$
\mu_1 = 1, \quad \mu_2 = 10
$$
$$
\sigma_1 = 0.8, \quad \sigma_2 = 0.8
$$
$$
p_1 = 0.5, \quad p_2 = 0.5
$$

---

## **Step 1: Probability density function (Gaussian)**

For component $i$:
$$
f_i(x) = \frac{1}{\sigma_i \sqrt{2\pi}} \exp\Big(-\frac{(x - \mu_i)^2}{2 \sigma_i^2}\Big)
$$

Let’s compute $f_1(x)$ and $f_2(x)$ for each $x$:

### **Precompute constants:**

$$
\sigma = 0.8 \quad \Rightarrow \quad \sigma \sqrt{2\pi} \approx 0.8 \times 2.506628 \approx 2.0053
$$
$$
\frac{1}{\sigma \sqrt{2\pi}} \approx 0.4987
$$
Also
$$
\frac{1}{2\sigma^2} = \frac{1}{2 \times 0.64} = \frac{1}{1.28} \approx 0.78125
$$

---

**For $x=1$:**
$$
f_1(1) = 0.4987 \times e^{-0.78125 \times (1-1)^2} = 0.4987 \times e^{0} = 0.4987
$$
$$
f_2(1) = 0.4987 \times e^{-0.78125 \times (1-10)^2} = 0.4987 \times e^{-0.78125 \times 81}
$$
$$
0.78125 \times 81 \approx 63.28125
$$
$$
e^{-63.28125} \approx 1.5 \times 10^{-28} \ (\text{effectively } 0)
$$
So $f_2(1) \approx 0$.

---

**For $x=2$:**
$$
f_1(2) = 0.4987 \times e^{-0.78125 \times (2-1)^2} = 0.4987 \times e^{-0.78125}
$$
$$
e^{-0.78125} \approx 0.4578
$$
$$
f_1(2) \approx 0.4987 \times 0.4578 \approx 0.2283
$$
$$
f_2(2) = 0.4987 \times e^{-0.78125 \times (2-10)^2} = 0.4987 \times e^{-0.78125 \times 64}
$$
$$
0.78125 \times 64 = 50
$$
$$
e^{-50} \approx 1.93 \times 10^{-22} \ (\approx 0)
$$

---

**For $x=3$:**
$$
f_1(3) = 0.4987 \times e^{-0.78125 \times (3-1)^2} = 0.4987 \times e^{-0.78125 \times 4}
$$
$$
e^{-3.125} \approx 0.04394
$$
$$
f_1(3) \approx 0.4987 \times 0.04394 \approx 0.02192
$$
$$
f_2(3) \approx 0 \ (\text{because } (3-10)^2 = 49, \ e^{-0.78125 \times 49} \text{ tiny})
$$

---

**For $x=6$:**
$$
f_1(6) = 0.4987 \times e^{-0.78125 \times (6-1)^2} = 0.4987 \times e^{-0.78125 \times 25}
$$
$$
e^{-19.53125} \approx 3.33 \times 10^{-9} \ (\text{very small})
$$
$$
f_2(6) = 0.4987 \times e^{-0.78125 \times (6-10)^2} = 0.4987 \times e^{-0.78125 \times 16}
$$
$$
e^{-12.5} \approx 3.73 \times 10^{-6}
$$
$$
f_2(6) \approx 0.4987 \times 3.73 \times 10^{-6} \approx 1.86 \times 10^{-6}
$$

---

**For $x=10$:**
$$
f_1(10) \approx 0 \ ((10-1)^2=81, \text{ huge})
$$
$$
f_2(10) = 0.4987 \times e^{0} = 0.4987
$$

---

**For $x=11$:**
$$
f_1(11) \approx 0
$$
$$
f_2(11) = 0.4987 \times e^{-0.78125 \times (11-10)^2} = 0.4987 \times e^{-0.78125} \approx 0.2283
$$

---

**For $x=12$:**
$$
f_1(12) \approx 0
$$
$$
f_2(12) = 0.4987 \times e^{-0.78125 \times (12-10)^2} = 0.4987 \times e^{-0.78125 \times 4}
$$
$$
= 0.4987 \times 0.04394 \approx 0.02192
$$

---

## **Step 2: E-step – compute responsibilities $y_{ni}$**

$$
y_{n1} = \frac{p_1 f_1(x_n)}{p_1 f_1(x_n) + p_2 f_2(x_n)}
$$
Since $p_1 = p_2 = 0.5$, simplifies to:
$$
y_{n1} = \frac{f_1(x_n)}{f_1(x_n) + f_2(x_n)}, \quad y_{n2} = 1 - y_{n1}
$$

---

Let’s compute:

* $x=1$: $f_1=0.4987$, $f_2\approx 0$
  $y_{11} \approx 1$, $y_{21} \approx 0$

* $x=2$: $f_1=0.2283$, $f_2\approx 0$
  $y_{12} \approx 1$, $y_{22} \approx 0$

* $x=3$: $f_1=0.02192$, $f_2\approx 0$
  $y_{13} \approx 1$, $y_{23} \approx 0$

* $x=6$: $f_1 \approx 3.33\times 10^{-9}$, $f_2 \approx 1.86\times 10^{-6}$
  $f_1+f_2 \approx 1.863\times 10^{-6}$
  $y_{14} \approx 3.33\times 10^{-9} / 1.863\times 10^{-6} \approx 0.00179$
  $y_{24} \approx 0.99821$

* $x=10$: $f_1\approx 0$, $f_2=0.4987$
  $y_{15} \approx 0$, $y_{25} \approx 1$

* $x=11$: $f_1\approx 0$, $f_2=0.2283$
  $y_{16} \approx 0$, $y_{26} \approx 1$

* $x=12$: $f_1\approx 0$, $f_2=0.02192$
  $y_{17} \approx 0$, $y_{27} \approx 1$

---

## **Step 3: M-step – update parameters**

$$
N_1 = \sum_{n=1}^7 y_{n1}, \quad N_2 = \sum_{n=1}^7 y_{n2}
$$

From above:
$$
y_{n1} = [1, 1, 1, 0.00179, 0, 0, 0] \quad \Rightarrow \quad N_1 \approx 3.00179
$$
$$
y_{n2} = [0, 0, 0, 0.99821, 1, 1, 1] \quad \Rightarrow \quad N_2 \approx 3.99821
$$

Check: $N_1 + N_2 = 7$.

---

**New $\mu_1$:**
$$
\mu_1 = \frac{1}{N_1} \sum_{n=1}^{7} y_{n1} x_n
$$
$$
\sum y_{n1} x_n = 1\times1 + 1\times2 + 1\times3 + 0.00179\times6 \approx 6.01074
$$
$$
\mu_1 \approx 6.01074 / 3.00179 \approx 2.002
$$

---

**New $\mu_2$:**
$$
\mu_2 = \frac{1}{N_2} \sum_{n=1}^{7} y_{n2} x_n
$$
$$
\sum y_{n2} x_n = 0.99821\times6 + 10 + 11 + 12 \approx 38.98926
$$
$$
\mu_2 \approx 38.98926 / 3.99821 \approx 9.751
$$

---

**New $\sigma_1^2$:**
$$
\sigma_1^2 = \frac{1}{N_1} \sum_{n=1}^{7} y_{n1} (x_n - \mu_1)^2
$$
Values for $n=1,2,3,4$:

$$
\begin{aligned}
n=1 &: 1 \times (1 - 2.002)^2 = 1.004 \
n=2 &: 1 \times (2 - 2.002)^2 \approx 4\times 10^{-6} \
n=3 &: 1 \times (3 - 2.002)^2 \approx 0.996 \
n=4 &: 0.00179 \times (6 - 2.002)^2 \approx 0.0286
\end{aligned}
$$
Sum: $2.0286$
$$
\sigma_1^2 \approx 2.0286 / 3.00179 \approx 0.676, \quad \sigma_1 \approx 0.822
$$

---

**New $\sigma_2^2$:**
$$
\sigma_2^2 = \frac{1}{N_2} \sum_{n=1}^{7} y_{n2} (x_n - \mu_2)^2
$$
Values for $n=4,5,6,7$:

$$
\begin{aligned}
n=4 &: 0.99821 \times (6 - 9.751)^2 \approx 14.04 \
n=5 &: (10 - 9.751)^2 \approx 0.062 \
n=6 &: (11 - 9.751)^2 \approx 1.562 \
n=7 &: (12 - 9.751)^2 \approx 5.061
\end{aligned}
$$
Sum: $20.725$
$$
\sigma_2^2 \approx 20.725 / 3.99821 \approx 5.183, \quad \sigma_2 \approx 2.277
$$

---

**New mixing weights:**
$$
p_1 = \frac{N_1}{N} \approx 0.4288, \quad p_2 = \frac{N_2}{N} \approx 0.5712
$$

---

## **Updated parameters after 1 iteration:**

$$
\mu_1 \approx 2.00, \quad \mu_2 \approx 9.75
$$
$$
\sigma_1 \approx 0.822, \quad \sigma_2 \approx 2.277
$$
$$
p_1 \approx 0.429, \quad p_2 \approx 0.571
$$

---
